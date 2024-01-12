console.log("working");

document.addEventListener("DOMContentLoaded", function() {
document.getElementById('submit').addEventListener('click', function(event) {
    // Prevent the default action (navigation to the specified URL)
    event.preventDefault();
 
    // Now, you can add your custom logic
    console.log($("#username").val())
    console.log($("#password").val())
    const formData = new FormData();
    formData.append("username", $("#username").val());
    formData.append("password", $("#password").val());
    fetch("/login", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if(response.status === 200)
        {
            return response.json();
        }
        else
        {
            throw new Error("User Not Found or Invalid Credentials");
        }
    })
    .then(response => {
        // console.log(response);
        // alert(response);
        localStorage.setItem("access_token", `Bearer ${response.access_token}`);
        sessionStorage.setItem("username", `${response.username}`);
        sessionStorage.setItem("email", `${response.email}`);
        sessionStorage.setItem("role", `${response.role}`);
        // sessionStorage.setItem("email", `${response.email}`);
        // sessionStorage.setItem("role", `${response.role}`);
        if (localStorage.getItem("access_token") !== null) {
            window.location.href= "/dashboard";
        }
    })
    .catch(error => {
        $(".error-message").text(error.message);
        $(".error-message").css("visibility", "visible");
    })
 
});


});

// logout
function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
    // You can add more cleanup here if needed
}

