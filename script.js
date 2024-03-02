document.addEventListener("DOMContentLoaded", function () {
  updateButtonVisibility();
  attachButtonEventListeners();
  restoreStateFromUrl();
});

function loadContent(contentId) {
  // Update URL hash to reflect the loaded content
  window.location.hash = `content=${contentId}`;
  // Placeholder for actual content loading logic
  // Simulate fetching and displaying content
  fetch(contentId + ".html")
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("content-area").innerHTML = html;
      updateButtonVisibility();
    })
    .catch((error) => console.error("Error loading the content:", error));
}

function showContentById(contentId) {
  // Update URL hash to reflect the shown section
  window.location.hash = `section=${contentId}`;
  // Hide all sections first
  document.querySelectorAll("#content-area > div").forEach((div) => {
    div.style.display = "none";
  });
  // Show the selected section
  let content = document.getElementById(contentId);
  if (content) {
    content.style.display = "block";
  }
}

function updateButtonVisibility() {
  document.querySelectorAll(".right-boxes button").forEach((button) => {
    let contentId = button.id.replace("show", "");
    let contentExists = !!document.getElementById(contentId);
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

document
  .getElementById("content-dropdown")
  .addEventListener("change", function () {
    loadContent(this.value);
  });

function restoreStateFromUrl() {
  const hashParams = new URLSearchParams(window.location.hash.slice(1));
  if (hashParams.has("content")) {
    const contentId = hashParams.get("content");
    loadContent(contentId);
  } else if (hashParams.has("section")) {
    const sectionId = hashParams.get("section");
    showContentById(sectionId);
  }
}

window.addEventListener("hashchange", function () {
  restoreStateFromUrl();
});
