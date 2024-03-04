document.addEventListener("DOMContentLoaded", function () {
  // Define references to the content area, dropdown, and right-side buttons
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");

  // Create a hidden input to store the current content name for state management
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content-name";
  contentArea.appendChild(hiddenInput);

  // Function to load content based on the content name and button ID
  window.loadContent = function (
    contentName,
    buttonId = null,
    isNavigateAction = false
  ) {
    // Update the hidden input value to the current content name
    hiddenInput.value = contentName;

    // Fetch the content HTML from the server
    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.text();
      })
      .then((html) => {
        // Update the content area with the fetched HTML
        contentArea.innerHTML = html;
        // Update the visibility of buttons based on available content sections
        updateButtonVisibility();
        // If it's not a navigation action, display the content by button ID
        if (!isNavigateAction) {
          displayContentById(buttonId);
        }
        // Update the browser's URL to reflect the current content and button ID
        updateURL(contentName, isNavigateAction ? null : buttonId);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  };

  // Function to update the visibility of right-side buttons based on content availability
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

  // Function to display specific content by ID, hiding others
  function displayContentById(buttonId) {
    if (!buttonId) return;
    const contentDivs = contentArea.querySelectorAll("div");
    contentDivs.forEach((div) => {
      div.style.display = div.id === buttonId ? "" : "none";
    });
  }

  // Function to update the browser's URL to reflect the current state
  function updateURL(contentName, buttonId) {
    const newUrl = `${window.location.pathname}?content=${contentName}${
      buttonId ? `&buttonId=${buttonId}` : ""
    }`;
    window.history.pushState({ path: newUrl }, "", newUrl);
  }

  // Set up event listeners for right-side buttons to handle clicks
  rightBoxes.forEach((button) => {
    button.addEventListener("click", function () {
      const navigateValue = this.getAttribute("navigate");
      // If a 'navigate' attribute exists, load the specified content and indicate it's a navigate action
      if (navigateValue) {
        window.loadContent(navigateValue, null, true);
      } else {
        // Otherwise, handle the click as per the original button ID-based navigation
        const buttonId = this.id.replace("show", "");
        window.loadContent(hiddenInput.value, buttonId);
      }
    });
  });

  // Set up an event listener for the content dropdown to load selected content
  contentDropdown.addEventListener("change", function () {
    window.loadContent(this.value);
  });

  // Initialize content based on URL parameters on page load
  (function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentName = urlParams.get("content");
    const buttonId = urlParams.get("buttonId");

    // If URL parameters specify content, load it; otherwise, update button visibility
    if (contentName) {
      contentDropdown.value = contentName;
      window.loadContent(contentName, buttonId);
    } else {
      updateButtonVisibility();
    }
  })();
});
