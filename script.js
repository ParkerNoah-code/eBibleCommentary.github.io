function loadContent(contentName) {
  if (!contentName) return; // Do nothing if no content is selected

  // Fetch the HTML file based on contentName
  fetch(`Bible/${contentName}.html`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((html) => {
      // Inject the fetched HTML into the content area
      document.getElementById("content-area").innerHTML = html;
    })
    .catch((error) => {
      console.error("Failed to load content:", error);
    });
}

function show(id) {
  // Hide all content divs
  const contentDivs = document.querySelectorAll("#content-area > div");
  contentDivs.forEach((div) => {
    div.style.display = "none"; // Hide each div
  });

  // Show the selected content div
  const selectedContent = document.getElementById(id);
  if (selectedContent) {
    selectedContent.style.display = "block"; // Show the div with the matching id
  }
}

document.addEventListener("DOMContentLoaded", (event) => {
  document.getElementById("showI").addEventListener("click", () => show("I"));
  document.getElementById("showT").addEventListener("click", () => show("T"));
  document.getElementById("showC").addEventListener("click", () => show("C"));
  document.getElementById("showH").addEventListener("click", () => show("H"));
});
