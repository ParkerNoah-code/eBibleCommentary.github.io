function updateURLParameter(param, value) {
  const url = new URL(window.location);
  if (value === null || value === undefined) {
    url.searchParams.delete(param);
  } else {
    url.searchParams.set(param, encodeURIComponent(value).replace(/\//g, "-"));
  }
  window.history.pushState({}, "", url);
}

function loadContentFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  let content = urlParams.get("content") || "about";
  content = decodeURIComponent(content).replace(/-/g, "/");
  loadContent(content);
}

function loadContent(value) {
  const urlParams = new URLSearchParams(window.location.search);
  const contentInURL = urlParams.get("content");
  const decodedContentInURL = decodeURIComponent(
    (contentInURL || "").replace(/-/g, "/")
  );

  if (decodedContentInURL !== value) {
    updateURLParameter("section", null);
  }

  const fileName = value.replace(/\//g, "-") + ".html";
  updateURLParameter("content", value.replace(/\//g, "-"));

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

      let hiddenInput = document.getElementById("current-content");
      if (!hiddenInput) {
        hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.id = "current-content";
        contentArea.appendChild(hiddenInput);
      }
      hiddenInput.value = value;

      populateSectionDropdown();
      checkForNavTargets();
    })
    .catch((error) => {
      console.error("There was a problem with your fetch operation:", error);
      document.getElementById(
        "content-area"
      ).innerHTML = `<p>Error loading content. Please try again.</p>`;
    });
}

function checkForNavTargets() {
  const navButton = document.getElementById("back-button");
  const contentArea = document.getElementById("content-area");
  const nav = contentArea.querySelector(".nav");

  if (nav) {
    const targetContent = nav.getAttribute("data-content");
    const targetSection = nav.getAttribute("data-section");

    if (targetContent) {
      navButton.style.display = "inline-block";
      navButton.onclick = () => {
        loadContent(targetContent);
        if (targetSection) {
          filterSection(targetSection);
        }
      };
    } else {
      navButton.style.display = "none";
    }
  } else {
    navButton.style.display = "none";
  }
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

  if (sections.length > 0) {
    sectionDropdown.style.display = "";
    if (section) {
      document.getElementById("section-dropdown").value = section;
      filterSection(section);
    }
  } else {
    sectionDropdown.style.display = "none";
  }
}

function filterSection(sectionId) {
  updateURLParameter("section", sectionId);

  const sections = document.querySelectorAll("#content-area > div");

  sections.forEach((section) => {
    section.style.display = section.id === sectionId ? "" : "none";
  });

  window.scrollTo(0, 0);
}

document.addEventListener("DOMContentLoaded", () => {
  loadContentFromURL();
});
