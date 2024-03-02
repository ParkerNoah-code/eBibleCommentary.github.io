document.addEventListener("DOMContentLoaded", function () {
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content";
  contentArea.appendChild(hiddenInput);

  // Dynamically load content and manage button visibility
  function loadContent(contentName) {
    if (!contentName) return;

    // Check if content needs to be reloaded
    if (hiddenInput.value !== contentName) {
      fetch(`${contentName}.html`)
        .then((response) => {
          if (!response.ok) throw new Error("Network response was not ok");
          return response.text();
        })
        .then((html) => {
          contentArea.innerHTML = html + contentArea.innerHTML; // Keep hidden input
          hiddenInput.value = contentName;
          updateButtonVisibility();
          updateURL(contentName);
        })
        .catch((error) => {
          console.error("Failed to load content:", error);
        });
    }
  }

  // Update button visibility based on available content IDs
  function updateButtonVisibility() {
    rightBoxes.forEach((button) => {
      const contentId = button.id.replace("show", "");
      document.getElementById(contentId)
        ? (button.style.display = "")
        : (button.style.display = "none");
    });
  }

  // Single content display management
  rightBoxes.forEach((button) => {
    button.addEventListener("click", function () {
      const contentId = this.id.replace("show", "");
      const content = document.getElementById(contentId);
      if (content) {
        // Hide all content except the clicked one
        contentArea.childNodes.forEach((child) => {
          if (child.id && child.id !== "current-content") {
            child.style.display = child.id === contentId ? "" : "none";
          }
        });
        updateURL(hiddenInput.value, contentId);
      }
    });
  });

  // URL state management
  function updateURL(contentName, contentId = "") {
    const newUrl = `${window.location.pathname}?content=${contentName}${
      contentId ? `&id=${contentId}` : ""
    }`;
    window.history.pushState({ path: newUrl }, "", newUrl);
  }

  // URL parsing and content initialization
  function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentName = urlParams.get("content");
    const contentId = urlParams.get("id");

    if (contentName) {
      contentDropdown.value = contentName;
      loadContent(contentName);

      if (contentId) {
        const content = document.getElementById(contentId);
        if (content) {
          content.style.display = "";
        }
      }
    }
  }

  // Listen to dropdown changes
  contentDropdown.addEventListener("change", function () {
    loadContent(this.value);
  });

  initContentFromURL();
});
