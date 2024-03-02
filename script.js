// Function to directly show or hide the corresponding content without loading from HTML files
function showContent(contentId) {
  const contentAreaDivs = document.querySelectorAll("#content-area > div");
  let isContentAlreadyVisible = false;

  contentAreaDivs.forEach((div) => {
    if (div.id === contentId) {
      isContentAlreadyVisible = div.style.display === "block";
    }
    div.style.display = "none"; // Hide all contents initially
  });

  // Only show the content if it was not already visible
  if (!isContentAlreadyVisible) {
    const contentToShow = document.getElementById(contentId);
    if (contentToShow) {
      contentToShow.style.display = "block";
    }
  }

  // Update button visibility based on current content. It might be unnecessary if the content does not dynamically change what is available.
  updateButtonVisibility();
}

// Adjusted function to attach event listeners to buttons. It now calls showContent instead of loadContent.
function attachEventListenersToButtons() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const contentName = button.id.replace("show", "");
      showContent(contentName);
    });
  });
}

// Update button visibility logic remains the same
function updateButtonVisibility() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    const contentId = button.id.replace("show", "");
    const contentExists =
      document.querySelector(`#content-area #${contentId}`) !== null;
    button.style.display = contentExists ? "inline-block" : "none";
  });
}

// Initial setup for attaching event listeners and updating button visibility
document.addEventListener("DOMContentLoaded", function () {
  attachEventListenersToButtons();
  updateButtonVisibility();
});
