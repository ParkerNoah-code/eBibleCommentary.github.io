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
      document.getElementById("content-area").innerHTML = html;

      // Update the button visibility based on the new content
      updateButtonVisibility();
    })
    .catch((error) => {
      console.error("Failed to load content:", error);
    });
}

function updateButtonVisibility() {
  // Get all buttons within the right-boxes container
  const buttons = document.querySelectorAll(".right-boxes button");

  buttons.forEach((button) => {
    // Extract the content id from the button id (e.g., 'showI' => 'I')
    const contentId = button.id.replace("show", "");

    // Check if there is an element with the corresponding id within the content-area
    const contentExists =
      document.querySelector(`#content-area #${contentId}`) !== null;

    // Show the button if the corresponding content exists, otherwise hide it
    button.style.display = contentExists ? "inline-block" : "none";
  });
}

// Initial update to set the correct visibility state for all buttons
document.addEventListener("DOMContentLoaded", updateButtonVisibility);
