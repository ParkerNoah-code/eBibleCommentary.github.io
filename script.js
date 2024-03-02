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

      // Re-attach event listeners to buttons
      attachEventListenersToButtons();
    })
    .catch((error) => {
      console.error("Failed to load content:", error);
    });
}

function attachEventListenersToButtons() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    button.removeEventListener("click", toggleContentVisibility); // Prevent duplicate listeners
    button.addEventListener("click", toggleContentVisibility);
  });
}

function toggleContentVisibility(event) {
  const buttonId = event.target.id; // Get the ID of the clicked button
  const contentId = buttonId.replace("show", ""); // Determine the corresponding content ID

  // Toggle the visibility of the corresponding content
  const content = document.getElementById(contentId);
  if (content) {
    content.style.display = content.style.display === "none" ? "block" : "none";
  }
}

// Attach event listeners when the document is initially loaded
document.addEventListener("DOMContentLoaded", attachEventListenersToButtons);

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
