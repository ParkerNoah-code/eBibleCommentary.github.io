document.addEventListener("DOMContentLoaded", function () {
  // Accessing essential DOM elements
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content-name";
  contentArea.appendChild(hiddenInput);

  // Function to load content based on the contentName and optionally a displayId
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
        } else {
          // Update without specifying a displayId
          updateURL(contentName);
        }
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  };

  // Updates the visibility of buttons based on content availability
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

  // Displays content by id
  function displayContentById(buttonId) {
    const contentDivs = contentArea.querySelectorAll("div");
    contentDivs.forEach((div) => {
      div.style.display = div.id === buttonId ? "" : "none";
    });
  }

  // Updates the URL based on contentName and optionally a buttonId/displayId
  function updateURL(contentName, displayId = null) {
    let newPath = `${window.location.pathname}?content=${contentName}`;
    if (displayId) {
      // Update the path with displayId if provided
      newPath += `&buttonId=${displayId}`;
    }
    window.history.pushState({ path: newPath }, "", newPath);
  }

  // Event listeners for right box buttons to handle custom navigation and display
  rightBoxes.forEach((button) => {
    button.addEventListener("click", function () {
      const buttonId = this.id.replace("show", "");
      const targetDiv = contentArea.querySelector(`#${buttonId}`);
      const navigateAttribute = targetDiv?.getAttribute("navigate");
      const displayId = targetDiv?.getAttribute("display-id");

      if (navigateAttribute) {
        // Load content based on navigate attribute, and optionally display content by displayId
        window.loadContent(navigateAttribute, displayId);
      } else {
        // Default functionality if 'navigate' and 'display-id' attributes do not exist
        displayContentById(buttonId);
        updateURL(hiddenInput.value, buttonId);
      }
    });
  });

  contentDropdown.addEventListener("change", function () {
    window.loadContent(this.value);
  });

  // Initializes content based on URL parameters
  (function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentName = urlParams.get("content");
    const buttonId = urlParams.get("buttonId");

    if (contentName) {
      contentDropdown.value = contentName;
      window.loadContent(contentName, buttonId);
    } else {
      updateButtonVisibility();
    }
  })();
});
