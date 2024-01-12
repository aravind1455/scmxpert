
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

// Add an event listener to the element with the id "loginButton" for click events
document.getElementById("loginButton").addEventListener("click", function() {
    // Redirect to the login page when the "loginButton" is clicked
    window.location.href = "login";
});




