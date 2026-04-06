document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");

    form.addEventListener("submit", function (e) {
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const error = document.getElementById("error");

        error.textContent = "";

        if (name === "") {
            e.preventDefault();
            error.textContent = "Name is required!";
            return;
        }

        if (!email.includes("@")) {
            e.preventDefault();
            error.textContent = "Enter a valid email!";
            return;
        }
        if (password.length < 6) {
            e.preventDefault();
            error.textContent = "Password must be at least 6 characters";
            return;
        }

        if (password !== confirmPassword) {
            e.preventDefault();
            error.textContent = "Passwords do not match";
            return;
        }
    });
});