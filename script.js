document.addEventListener("DOMContentLoaded", function () {
  attachEventListenersToButtons();
  updateButtonVisibility();
});

function attachEventListenersToButtons() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const contentId = button.id.replace("show", "");
      showOnlyContent(contentId);
    });
  });
}

function showOnlyContent(contentId) {
  const allContentDivs = document.querySelectorAll("#content-area > div");
  allContentDivs.forEach((div) => {
    if (div.id === contentId) {
      div.style.display = "block"; // Show the div corresponding to the clicked button
    } else {
      div.style.display = "none"; // Hide all other divs
    }
  });
}

function updateButtonVisibility() {
  const buttons = document.querySelectorAll(".right-boxes button");
  buttons.forEach((button) => {
    const contentId = button.id.replace("show", "");
    const contentExists =
      document.querySelector(`#content-area #${contentId}`) !== null;
    button.style.display = contentExists ? "inline-block" : "none";
  });
}
