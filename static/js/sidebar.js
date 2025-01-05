document.getElementById("burger").addEventListener("click", () => {
  var uploads = document.getElementById("uploads");
  var downloads = document.getElementById("downloads");
  fetch("http://127.0.0.1:8000/dashboard/attributeSetup", {
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => {
      uploads.textContent = data.uploads;
      downloads.textContent = data.downloads;
    });
});
