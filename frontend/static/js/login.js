const registerButton = document.getElementById("register");
const loginButton = document.getElementById("login");
const container = document.getElementById("container");
const loginPassword = document.getElementById("login-password");
const showPassword = document.getElementById("show-password");
const registerForm = document.getElementById("registerForm");
const loginContainer = document.querySelector(".login-container");
const registerContainer = document.querySelector(".register-container");
const overlayRight = document.querySelector(".overlay-right");
const overlayLeft = document.querySelector(".overlay-left");

const setRegistrationActive = (active) => {
    if (!container) return;

    container.classList.toggle("right-panel-active", active);
    if (loginContainer) loginContainer.inert = active;
    if (registerContainer) registerContainer.inert = !active;
    if (overlayRight) overlayRight.inert = active;
    if (overlayLeft) {
        overlayLeft.inert = !active;
        overlayLeft.setAttribute("aria-hidden", String(!active));
    }
    if (overlayRight) overlayRight.setAttribute("aria-hidden", String(active));
};

if (registerButton && container) {
    registerButton.addEventListener("click", () => {
        setRegistrationActive(true);
    });
}

if (loginButton && container) {
    loginButton.addEventListener("click", () => {
        setRegistrationActive(false);
    });
}

if (showPassword && loginPassword) {
    showPassword.addEventListener("change", () => {
        loginPassword.type = showPassword.checked ? "text" : "password";
    });
}

if (registerForm) {
    const fields = registerForm.querySelectorAll(".validated-input input");

    fields.forEach((field) => {
        const updateValidity = () => {
            const wrapper = field.closest(".validated-input");
            wrapper.classList.toggle("is-valid", field.value.length > 0 && field.validity.valid);
            wrapper.classList.toggle("is-invalid", field.value.length > 0 && !field.validity.valid);
        };

        field.addEventListener("input", updateValidity);
        field.addEventListener("change", updateValidity);
        updateValidity();
    });

    if (registerForm.querySelector(".error-message") && container) {
        setRegistrationActive(true);
    }
}
