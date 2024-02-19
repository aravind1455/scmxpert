if (localStorage.getItem("access_token") === null) {
    window.location.href = "/login";
}

// Function to authenticate user
function authenticate(form) {
    // Make a POST request to the authentication endpoint
    fetch("/changepassword1", {
        method: "POST",
        headers: {
            "Authorization": `${localStorage.getItem("access_token")}`,
        },
        body: form,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Handle successful authentication
        alert("password changed");
        // Redirect the user to the desired page
        window.location.href = "/login";
    })
    .catch(error => {
        // Handle authentication errors
        $("#error").text("invalid email");
        // Display error message to the user
    });
}

// Event listener for login form submission
document.getElementById("submit1").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get user input
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmpassword=document.getElementById("confirm_password").value;
    const form = new FormData();
    form.append("email",email);
    form.append("password",password);
    form.append("confirm",confirmpassword);
console.log("logined",form.get("confirm"))

    // Call the authenticate function with user input
    authenticate(form);
});
