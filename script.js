function loadContent(contentName) {
  if (!contentName) return; // Do nothing if no content is selected

  fetch(`${contentName}.json`)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("content-area").innerHTML = data.html;
    })
    .catch((error) => console.error("Failed to load content:", error));
}
