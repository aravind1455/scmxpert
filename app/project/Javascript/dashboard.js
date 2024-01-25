$(document).ready(function(){
    if (sessionStorage.getItem("role")==="admin"){
        $("#update").css("display","flex")
    }
    console.log("working");
    $("#username").html(`Welcome to SCM-Xpert, <span style="color: red;">${sessionStorage.getItem("username")}</span>`);
    
  });


// Check if the access_token is not present in the localStorage
if (localStorage.getItem("access_token") === null) {
    // Redirect to the login page if the access_token is not found
    window.location.href = "/login";
}

// Select the elements with the class "menuicn" and "navcontainer"
let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

// Add an event listener to the "menuicn" element for click events
menuicn.addEventListener("click", () => {
    // Toggle the "navclose" class on the "navcontainer" element
    // This class likely controls the visibility of a navigation menu
    nav.classList.toggle("navclose");
});

if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
        // You can add more cleanup here if needed
    }
    



