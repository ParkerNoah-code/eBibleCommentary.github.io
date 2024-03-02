document.addEventListener("DOMContentLoaded", function () {
  updateButtonVisibility();
  restoreStateFromUrl();
  attachButtonEventListeners();
});

let currentContent = ""; // Track the currently loaded content for efficiency

function loadContent(contentId, preventDuplicate = true) {
  if (!preventDuplicate || currentContent !== contentId) {
    currentContent = contentId; // Update the current content tracker

    // Update the dropdown selection if it's different
    const dropdown = document.getElementById("content-dropdown");
    if (dropdown.value !== contentId) {
      dropdown.value = contentId;
    }

    // Update URL with the selected option and reset button state to 'default'
    // Use history.pushState to manage history without causing a page reload
    const newState = { content: contentId, section: "default" };
    history.pushState(newState, "", `#content=${contentId}&section=default`);

    // Placeholder for actual fetching logic
    fetch(contentId + ".html")
      .then((response) => response.text())
      .then((html) => {
        document.getElementById("content-area").innerHTML =
          html + `<div>Loaded: ${contentId}</div>`; // Note indicating loaded content
        updateButtonVisibility();
        // After content is loaded, check if a specific section needs to be shown
        restoreSectionState();
      })
      .catch((error) => console.error("Error loading the content:", error));
  }
}

function showContentById(contentId) {
  document.querySelectorAll("#content-area > div").forEach((div) => {
    div.style.display = "none";
  });
  const sectionToShow = document.getElementById(contentId);
  if (sectionToShow) {
    sectionToShow.style.display = "block";
  }

  // Update the URL to reflect the new section, keeping the content part unchanged
  const newState = { content: currentContent, section: contentId };
  history.pushState(
    newState,
    "",
    `#content=${currentContent}&section=${contentId}`
  );
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
    loadContent(this.value, false);
  });

window.onpopstate = function (event) {
  if (event.state) {
    currentContent = ""; // Reset current content to ensure the content is reloaded
    restoreStateFromUrl();
  }
};

function restoreStateFromUrl() {
  const hashParams = new URLSearchParams(window.location.hash.slice(1));
  if (hashParams.has("content")) {
    const contentId = hashParams.get("content");
    loadContent(contentId, false); // Load content without preventing duplicates to ensure state updates
  }
  if (hashParams.has("section") && hashParams.get("section") !== "default") {
    const sectionId = hashParams.get("section");
    showContentById(sectionId);
  }
}

function restoreSectionState() {
  const hashParams = new URLSearchParams(window.location.hash.slice(1));
  if (hashParams.has("section") && hashParams.get("section") !== "default") {
    const sectionId = hashParams.get("section");
    showContentById(sectionId);
  }
}
