document.addEventListener("DOMContentLoaded", function () {
  updateButtonVisibility();
  attachButtonEventListeners();
  restoreStateFromUrl();
});

function loadContent(contentId) {
  // Update URL hash to reflect the loaded content file
  window.location.hash = `content=${contentId}`;
  // Simulate fetching and displaying content for demonstration
  // You'll need to replace this with actual content loading logic
  // Assuming the content-area can be directly updated for simplicity
  fetch(contentId + ".html")
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("content-area").innerHTML = html;
      updateButtonVisibility();
      // After loading new content, reset the displayed section in the URL
      window.location.hash += `&section=default`;
    })
    .catch((error) => console.error("Error loading the content:", error));
}

function showContentById(contentId) {
  // Assuming all content divs are hidden by default or by previous actions
  // Show the selected content div
  document.querySelectorAll("#content-area > div").forEach((div) => {
    div.style.display = "none"; // Hide all first
  });
  document.getElementById(contentId).style.display = "block"; // Show the selected one

  // Update URL hash to reflect the shown section along with the current content
  const currentContent = new URLSearchParams(window.location.hash.slice(1)).get(
    "content"
  );
  window.location.hash = `content=${currentContent}&section=${contentId}`;
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
  }
  if (hashParams.has("section") && hashParams.get("section") !== "default") {
    const sectionId = hashParams.get("section");
    showContentById(sectionId);
  }
}

window.addEventListener("hashchange", function () {
  restoreStateFromUrl();
});
