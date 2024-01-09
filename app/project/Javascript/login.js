document.getElementById('loginForm').addEventListener('submit', function(event) {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username.trim() === '' || password.trim() === '') {
        event.preventDefault(); // Prevent form submission
        alert('Please enter both username and password.');
        return false;
    }
    return true; // Submit the form
});
// ----------------------------------------------
$("submit").on("click", function(event) {
    event.preventDefault();

    const user = $("#username").val();
    const password = $("#password").val();

    const formData = new FormData();
    formData.append("username", user); 
    formData.append("password", password);

    fetch("/login", {
        method: "POST",
        mode: 'cors',
        body: formData
    })
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error("Invalid credentials");
        }
    })
    .then(response => {
        localStorage.setItem("access_token", `Bearer ${response.access_token}`);
        sessionStorage.setItem("username", response.username);
        if (localStorage.getItem("access_token") !== null) {
            window.location.href = "/dashboard";
        }
    })
    .catch(error => {
        $(".error-message").css("visibility", "visible");
    });
});


