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
    // If the selected content is already loaded, only update button visibility
    if (hiddenInput.value === contentName) {
      updateButtonVisibility();
      return;
    }

    // Clear existing content and load new content
    contentArea.innerHTML = ""; // Clear the content area
    contentArea.appendChild(hiddenInput); // Re-add the hidden input to the content area
    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.text();
      })
      .then((html) => {
        contentArea.innerHTML = html; // Load new content
        hiddenInput.value = contentName; // Update the hidden value
        updateButtonVisibility();
        updateURL(contentName);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
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
    } else {
      // No specific content requested, check button visibility based on initial content
      hiddenInput.value = ""; // Ensure hidden input is reset for initial state
      updateButtonVisibility();
    }

    if (contentId) {
      const content = document.getElementById(contentId);
      if (content) {
        content.style.display = "";
      }
    }
  }

  // Listen to dropdown changes
  contentDropdown.addEventListener("change", function () {
    loadContent(this.value);
  });

  initContentFromURL();
});
