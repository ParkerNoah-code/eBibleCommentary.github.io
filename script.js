document.addEventListener("DOMContentLoaded", function () {
  attachButtonEventListeners();
  window.addEventListener("popstate", restoreStateFromUrl);
  restoreStateFromUrl(true); // Initial state restoration with page load flag
});

function loadContent(contentId, updateHistory = true) {
  // Check if this content is already loaded to avoid unnecessary updates
  const isCurrentContent = window.location.hash.includes(
    `content=${contentId}`
  );
  if (!isCurrentContent) {
    if (updateHistory) {
      const newState = { content: contentId };
      history.pushState(newState, "", `#content=${contentId}`);
    }

    // Simulate fetching content
    document.getElementById(
      "content-area"
    ).innerHTML = `<div>Content for ${contentId} Loaded</div>`;
    document
      .getElementById("content-area")
      .querySelectorAll("div")
      .forEach((div) => (div.style.display = "none")); // Hide all content including the placeholder

    // Update dropdown selection
    document.getElementById("content-dropdown").value = contentId;

    updateButtonVisibility();
  }
}

function showContentById(contentId) {
  // Logic to show the content by ID, assuming content is already loaded
  document.querySelectorAll("#content-area > div").forEach((div) => {
    div.style.display = "none"; // Hide all first
  });
  document.getElementById(contentId).style.display = "block"; // Show the selected one

  // No need to update URL hash here for section since we're focusing on content navigation
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
  document
    .getElementById("content-dropdown")
    .addEventListener("change", function () {
      loadContent(this.value);
    });
}

function restoreStateFromUrl(initialLoad = false) {
  const hashParams = new URLSearchParams(window.location.hash.slice(1));
  if (hashParams.has("content")) {
    const contentId = hashParams.get("content");
    loadContent(contentId, !initialLoad); // Update history only if it's not the initial page load
  } else {
    // Default content loading logic if no specific content is specified in the URL
  }
}
