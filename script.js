document.addEventListener("DOMContentLoaded", function () {
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content-name";
  contentArea.appendChild(hiddenInput);

  window.loadContent = function (contentName, displayId = null) {
    hiddenInput.value = contentName;

    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.text();
      })
      .then((html) => {
        contentArea.innerHTML = html;
        updateButtonVisibility();
        if (displayId) {
          // Display content by the specified id if provided
          displayContentById(displayId);
        }
        updateURL(contentName, displayId);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  };

  function updateButtonVisibility() {
    rightBoxes.forEach((button) => {
      const contentId = button.id.replace("show", "");
      if (contentArea.querySelector(`#${contentId}`)) {
        button.style.display = "";
      } else {
        button.style.display = "none";
      }
    });
  }

  function displayContentById(buttonId) {
    const contentDivs = contentArea.querySelectorAll("div");
    contentDivs.forEach((div) => {
      div.style.display = div.id === buttonId ? "" : "none";
    });
  }

  function updateURL(contentName, displayId) {
    let newPath = `${window.location.pathname}?content=${contentName}`;
    if (displayId) {
      newPath += `&buttonId=${displayId}`;
    }
    window.history.pushState({ path: newPath }, "", newPath);
  }

  rightBoxes.forEach((button) => {
    button.addEventListener("click", function () {
      const buttonId = this.id.replace("show", "");
      const targetDiv = contentArea.querySelector(`#${buttonId}`);
      const navigateAttribute = targetDiv?.getAttribute("navigate");
      const displayId = targetDiv?.getAttribute("display-id");

      if (navigateAttribute) {
        window.loadContent(navigateAttribute, displayId);
      } else {
        displayContentById(buttonId);
        updateURL(hiddenInput.value, buttonId);
      }
    });
  });

  contentDropdown.addEventListener("change", function () {
    window.loadContent(this.value);
  });

  function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentNameFromURL = urlParams.get("content");
    const buttonIdFromURL = urlParams.get("buttonId");

    if (contentNameFromURL && hiddenInput.value !== contentNameFromURL) {
      window.loadContent(contentNameFromURL, buttonIdFromURL);
    } else if (hiddenInput.value) {
      // Load content from the hidden value if it doesn't match the URL parameter
      window.loadContent(hiddenInput.value, buttonIdFromURL);
    }
    contentDropdown.value = contentNameFromURL || hiddenInput.value;
  }

  // Initialize content based on URL parameters
  initContentFromURL();

  // Handle browser navigation events (back and forward button presses)
  window.addEventListener("popstate", function () {
    initContentFromURL();
  });
});
