document.addEventListener("DOMContentLoaded", function () {
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content-name"; // Adjusted the ID for clarity
  contentArea.appendChild(hiddenInput);

  // Dynamically load content and manage button visibility
  function loadContent(contentName) {
    // Update hidden input value immediately for comparison purposes
    hiddenInput.value = contentName;

    // Fetch and load new content only if different from current
    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.text();
      })
      .then((html) => {
        contentArea.innerHTML = html; // Replace existing content
        updateButtonVisibility(); // Update visibility after content is loaded
        updateURL(contentName);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  }

  // Update button visibility based on available content IDs within the content area
  function updateButtonVisibility() {
    rightBoxes.forEach((button) => {
      const contentId = button.id.replace("show", ""); // Extract the ID meant for content
      if (contentArea.querySelector(`#${contentId}`)) {
        button.style.display = ""; // Show button if content ID exists
      } else {
        button.style.display = "none"; // Hide button if content ID does not exist
      }
    });
  }

  // URL state management for reflecting current content and button states in the URL
  function updateURL(contentName, contentId = "") {
    const newUrl = `${window.location.pathname}?content=${contentName}${
      contentId ? `&id=${contentId}` : ""
    }`;
    window.history.pushState({ path: newUrl }, "", newUrl);
  }

  // Initialize content and buttons based on URL parameters
  function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentName = urlParams.get("content");

    if (contentName) {
      contentDropdown.value = contentName;
      loadContent(contentName); // Load content if specified in URL
    } else {
      // No content specified, ensure correct initial state
      updateButtonVisibility(); // This ensures buttons are correctly shown/hidden based on initial content
    }
  }

  // Listen for dropdown changes to load corresponding content
  contentDropdown.addEventListener("change", function () {
    loadContent(this.value);
  });

  initContentFromURL(); // Ensure proper initialization on document load
});
