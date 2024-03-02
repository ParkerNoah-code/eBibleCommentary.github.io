document.addEventListener("DOMContentLoaded", function () {
  updateButtonVisibility();
  attachButtonEventListeners();
});

function loadContent(contentId) {
  // Assuming you have a function to load the content dynamically
  // You can use AJAX or Fetch API to load content from "About.html", "Book1.html", etc.
  // After loading the content, you should call `updateButtonVisibility()` to update button states
  fetch(contentId + ".html")
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("content-area").innerHTML = html;
      updateButtonVisibility();
    })
    .catch((error) => console.error("Error loading the content:", error));
}

function updateButtonVisibility() {
  // Query all buttons within .right-boxes
  document.querySelectorAll(".right-boxes button").forEach((button) => {
    // Extract ID from button's ID attribute
    let contentId = button.id.replace("show", "");
    // Check if an element with the corresponding ID exists within #content-area
    let contentExists = !!document.getElementById(contentId);
    // Show button if content exists, otherwise hide
    button.style.display = contentExists ? "inline-block" : "none";
  });
}

function attachButtonEventListeners() {
  document.querySelectorAll(".right-boxes button").forEach((button) => {
    button.addEventListener("click", function () {
      let contentId = this.id.replace("show", "");
      showContentById(contentId);
    });
  });
}

function showContentById(contentId) {
  // Hide all content first
  document.querySelectorAll("#content-area > div").forEach((div) => {
    div.style.display = "none";
  });
  // Show the selected content
  let content = document.getElementById(contentId);
  if (content) {
    content.style.display = "block";
  }
}

// Optional: If the dropdown change should also trigger content loading dynamically
document
  .getElementById("content-dropdown")
  .addEventListener("change", function () {
    loadContent(this.value);
  });
