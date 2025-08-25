const form = document.querySelector("form");
const btn = document.getElementById("analyze-btn");
const btnText = document.getElementById("analyze-btn-text");
const btnLoading = document.getElementById("analyze-btn-loading");

if (form && btn && btnText && btnLoading) {
  form.addEventListener("submit", function () {
    btn.disabled = true;
    btnText.style.display = "none";
    btnLoading.style.display = "inline-flex";
  });
}

function copyResponse() {
  const text = document.getElementById("response-text").innerText;
  navigator.clipboard.writeText(text);
}
