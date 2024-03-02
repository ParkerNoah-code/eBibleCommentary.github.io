document.addEventListener("DOMContentLoaded", function () {
  const contentArea = document.getElementById("content-area");
  const contentDropdown = document.getElementById("content-dropdown");
  const rightBoxes = document.querySelectorAll(".right-boxes button");
  const hiddenInput = document.createElement("input");
  hiddenInput.type = "hidden";
  hiddenInput.id = "current-content-name";
  contentArea.appendChild(hiddenInput);

  function loadContent(contentName, buttonId = null) {
    // Update hidden input value
    hiddenInput.value = contentName;

    fetch(`${contentName}.html`)
      .then((response) => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.text();
      })
      .then((html) => {
        contentArea.innerHTML = html;
        updateButtonVisibility();
        // Display content associated with button ID, if specified
        displayContentById(buttonId);
        updateURL(contentName, buttonId);
      })
      .catch((error) => {
        console.error("Failed to load content:", error);
      });
  }

  function updateButtonVisibility() {
    rightBoxes.forEach((button) => {
      const contentId = button.id.replace("show", "");
      if (contentArea.querySelector(`#${contentId}`)) {
        button.style.display = "";
      } else {
        button.style.display = "none";
      }
    });
  }

  function displayContentById(buttonId) {
    if (!buttonId) return;
    const contentDivs = contentArea.querySelectorAll("div");
    contentDivs.forEach((div) => {
      div.style.display = div.id === buttonId ? "" : "none";
    });
  }

  function updateURL(contentName, buttonId) {
    const newUrl = `${window.location.pathname}?content=${contentName}${
      buttonId ? `&buttonId=${buttonId}` : ""
    }`;
    window.history.pushState({ path: newUrl }, "", newUrl);
  }

  function initContentFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const contentName = urlParams.get("content");
    const buttonId = urlParams.get("buttonId");

    if (contentName) {
      contentDropdown.value = contentName;
      loadContent(contentName, buttonId);
    } else {
      updateButtonVisibility(); // Ensure buttons are shown/hidden based on initial content
      displayContentById(buttonId); // Display content for the button ID if present
    }
  }

  rightBoxes.forEach((button) => {
    button.addEventListener("click", function () {
      const buttonId = this.id.replace("show", "");
      displayContentById(buttonId);
      updateURL(hiddenInput.value, buttonId);
    });
  });

  contentDropdown.addEventListener("change", function () {
    loadContent(this.value);
  });

  initContentFromURL();
});
