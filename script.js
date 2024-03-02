// Function to load content based on the button clicked
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
      // Clear existing content and inject the fetched HTML into the content area
      const contentArea = document.getElementById("content-area");
      contentArea.innerHTML = html; // Inject new content

      // Update the button visibility and attach event listeners again in case new content affects them
      updateButtonVisibility();
    })
    .catch((error) => {
      console.error("Failed to load content:", error);
    });
}

// Function to update button visibility based on the current content within the #content-area
function updateButtonVisibility() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    const contentId = button.id.replace("show", "");
    const contentExists =
      document.querySelector(`#content-area #${contentId}`) !== null;

    // Show or hide button based on the existence of the corresponding content
    button.style.display = contentExists ? "inline-block" : "none";
  });
}

// Function to attach event listeners to each button for loading content
function attachEventListenersToButtons() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      // Extract content name from button id
      const contentName = button.id.replace("show", "");

      // Hide all content divs
      document.querySelectorAll("#content-area > div").forEach((div) => {
        div.style.display = "none";
      });

      // Load the content corresponding to the clicked button
      // Note: If the content is already loaded and just needs to be shown, adjust this logic accordingly
      loadContent(contentName);
    });
  });
}

// Initial setup to attach event listeners and update button visibility
document.addEventListener("DOMContentLoaded", function () {
  attachEventListenersToButtons();
  updateButtonVisibility();
});
