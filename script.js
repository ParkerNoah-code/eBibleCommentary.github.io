document.addEventListener("DOMContentLoaded", function () {
  updateButtonVisibility();
  attachButtonEventListeners();
  restoreStateFromUrl();
});

let currentContent = ""; // Track the currently loaded content

function loadContent(contentId) {
  // Check if the content is already loaded to avoid unnecessary fetches
  if (currentContent !== contentId) {
    currentContent = contentId; // Update the current content tracker
    // Update URL with the selected option and reset button state to 'default'
    window.location.hash = `content=${contentId}&section=default`;

    // Placeholder for actual fetching logic
    // Replace this with your content loading implementation
    fetch(contentId + ".html")
      .then((response) => response.text())
      .then((html) => {
        document.getElementById("content-area").innerHTML =
          html + `<div>Loaded: ${contentId}</div>`; // Note indicating loaded content
        updateButtonVisibility();
      })
      .catch((error) => console.error("Error loading the content:", error));
  }
}

function showContentById(contentId) {
  // Only proceed if a different section is selected
  if (
    new URLSearchParams(window.location.hash.slice(1)).get("section") !==
    contentId
  ) {
    // Update the URL to reflect the new section, keeping the content part unchanged
    const hashParams = new URLSearchParams(window.location.hash.slice(1));
    hashParams.set("section", contentId);
    window.location.hash = hashParams.toString();

    // Show the selected section
    document.querySelectorAll("#content-area > div").forEach((div) => {
      div.style.display = "none";
    });
    const sectionToShow = document.getElementById(contentId);
    if (sectionToShow) {
      sectionToShow.style.display = "block";
    }
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
  }
  if (hashParams.has("section") && hashParams.get("section") !== "default") {
    const sectionId = hashParams.get("section");
    showContentById(sectionId);
  }
}
