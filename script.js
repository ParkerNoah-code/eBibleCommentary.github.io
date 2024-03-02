document.addEventListener("DOMContentLoaded", () => {
  const contentArea = document.getElementById("content-area");
  const dropdown = document.getElementById("content-dropdown");

  // Function to load content based on the dropdown selection or URL parameter
  function loadContent(contentName) {
    if (!contentName) return; // Do nothing if no content is selected

    // Fetch the HTML file based on contentName
    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.text();
      })
      .then((html) => {
        // Inject the fetched HTML into the content area
        contentArea.innerHTML = html;
        updateButtonVisibility();
        updateURLState(contentName);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  }

  // Update button visibility based on the content in the content-area
  function updateButtonVisibility() {
    document.querySelectorAll(".right-boxes button").forEach((button) => {
      const contentId = button.id.replace("show", "");
      button.style.display = document.getElementById(contentId) ? "" : "none";
    });
  }

  // Update the browser's URL without reloading the page
  function updateURLState(contentName) {
    history.pushState({ contentName }, "", `?content=${contentName}`);
  }

  // Initialize content based on URL parameters
  function initContentFromURL() {
    const params = new URLSearchParams(window.location.search);
    const contentName = params.get("content");
    if (contentName) {
      dropdown.value = contentName;
      loadContent(contentName);
    }
  }

  // Dropdown change event listener
  dropdown.addEventListener("change", (event) => {
    loadContent(event.target.value);
  });

  // Initialize content and button visibility on page load
  initContentFromURL();
  updateButtonVisibility();
});
