function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
    // You can add more cleanup here if needed
}