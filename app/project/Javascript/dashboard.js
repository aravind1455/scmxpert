if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function(){
    if (sessionStorage.getItem("role")==="admin"){
        $("#update").css("display","flex");
        $("#update1").css("display","flex");
    }
    $("#username").html(`Welcome to SCM-Xpert, <span style="color: red;">${sessionStorage.getItem("username")}</span>`);
});


let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
});

function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
}



