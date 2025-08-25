const form = document.querySelector("form");
const btn = document.getElementById("analyze-btn");
const btnText = document.getElementById("analyze-btn-text");
const btnLoading = document.getElementById("analyze-btn-loading");
const textarea = document.querySelector('textarea[name="email_text"]');
const fileInput = document.querySelector('input[name="email_file"]');

// Function to check if form has content
function validateForm() {
  const hasText = textarea.value.trim().length > 0;
  const hasFile = fileInput.files.length > 0;

  if (hasText || hasFile) {
    btn.disabled = false;
    btn.style.opacity = "1";
    btn.style.cursor = "pointer";
  } else {
    btn.disabled = true;
    btn.style.opacity = "0.5";
    btn.style.cursor = "not-allowed";
  }
}

// Initialize form validation
if (form && btn && btnText && btnLoading && textarea && fileInput) {
  // Set initial state
  validateForm();

  // Add event listeners
  textarea.addEventListener("input", validateForm);
  fileInput.addEventListener("change", validateForm);

  form.addEventListener("submit", function (e) {
    // Double check before submitting
    const hasText = textarea.value.trim().length > 0;
    const hasFile = fileInput.files.length > 0;

    if (!hasText && !hasFile) {
      e.preventDefault();
      return false;
    }

    btn.disabled = true;
    btnText.style.display = "none";
    btnLoading.style.display = "inline-flex";
  });
}

function copyResponse() {
  const text = document.getElementById("response-text").innerText;
  navigator.clipboard.writeText(text);
}
