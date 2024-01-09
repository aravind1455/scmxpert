let menuicn = document.querySelector(".menuicn"); 
let nav = document.querySelector(".navcontainer"); 

menuicn.addEventListener("click", () => { 
	nav.classList.toggle("navclose"); 
})


document.getElementById("loginButton").addEventListener("click", function() {
    window.location.href = "login";
});