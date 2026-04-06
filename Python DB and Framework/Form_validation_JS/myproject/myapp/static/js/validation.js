function validateForm() {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone").value.trim();

    // NAME VALIDATION
    if (name === "") {
        alert("Name is required");
        return false;
    }

    // Only letters and spaces allowed
    let namePattern = /^[A-Za-z ]+$/;
    if (!name.match(namePattern)) {
        alert("Name must contain only letters");
        return false;
    }

    // EMAIL VALIDATION
    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        alert("Enter valid email (example@gmail.com)");
        return false;
    }

    // PHONE VALIDATION
    let phonePattern = /^[0-9]{10}$/;
    if (!phone.match(phonePattern)) {
        alert("Enter valid 10-digit phone number");
        return false;
    }

    alert("Register Succesfully..!");
    return true;
}