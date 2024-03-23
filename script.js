function updateURLParameter(param, value) {
  const url = new URL(window.location);
  url.searchParams.set(param, value);
  window.history.pushState({}, "", url);
}

function loadContentFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  const content = urlParams.get("content") || "about";
  loadContent(content);
}

function loadContent(value) {
  const fileName = value + ".html";
  updateURLParameter("content", value);

  fetch(fileName)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((html) => {
      const contentArea = document.getElementById("content-area");
      contentArea.innerHTML = html;
      populateSectionDropdown();
    })
    .catch((error) => {
      console.error("There was a problem with your fetch operation:", error);
      document.getElementById(
        "content-area"
      ).innerHTML = `<p>Error loading content. Please try again.</p>`;
    });
}

function populateSectionDropdown() {
  const sections = document.querySelectorAll("#content-area > div");
  const sectionDropdown = document.getElementById("section-dropdown");

  sectionDropdown.innerHTML = "";

  sections.forEach((section) => {
    const option = document.createElement("option");
    option.value = section.id;
    option.textContent = section.getAttribute("dropdownName");
    sectionDropdown.appendChild(option);
  });

  const urlParams = new URLSearchParams(window.location.search);
  const section = urlParams.get("section");
  if (section) {
    document.getElementById("section-dropdown").value = section;
    filterSection(section);
  } else {
    sectionDropdown.selectedIndex = -1;
  }
}

function filterSection(sectionId) {
  updateURLParameter("section", sectionId);

  const sections = document.querySelectorAll("#content-area > div");

  sections.forEach((section) => {
    section.style.display =
      section.id === sectionId || sectionId === "" ? "" : "none";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  loadContentFromURL();
});
