function validateForm() {
    // Get form inputs
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirm = document.getElementById("confirm").value;

    // Regular expression for email validation
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validation
    if (username === "") {
      document.getElementById("usernameError").innerHTML = "Please enter a username";
      return false;
    }
    document.getElementById("usernameError").innerHTML = "";

    if (!emailRegex.test(email)) {
      document.getElementById("emailError").innerHTML = "Please enter a valid email";
      return false;
    }
    document.getElementById("emailError").innerHTML = "";

    if (password === "") {
      document.getElementById("passwordError").innerHTML = "Please enter a password";
      return false;
    }
    document.getElementById("passwordError").innerHTML = "";

    if (confirm !== password) {
      document.getElementById("confirmError").innerHTML = "Passwords do not match";
      return false;
    }
    document.getElementById("confirmError").innerHTML = "";

    // If all validations pass, the form will submit
    return true;
  }


//--------------------------new valid
const signInData = {
  user: user,
  password: password
};

const formData = new URLSearchParams()
formData.append('username', `${user}`);
formData.append('password', `${password}`);

try {
  const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      mode: 'cors',
      body: formData,
  });

  // Check if the sign-in was successful
  if (response.ok) {
      const signin = await response.json();

      // Store in local storage
      localStorage.setItem('token', signin.token);
      sessionStorage.setItem("username", signin.user);
      sessionStorage.setItem("password", signin.password);
      // sessionStorage.setItem("role", signin.role);

      document.getElementById('success-message').innerText = `Success: ${signin.message}`;
      clearAfterDelay(3000);
      // Redirect to Dashboard

  } else {
      document.getElementById('userpassword').innerText = ` ${errorData.detail}`;
      return false;
  }
} catch (error) {
  console.error('Error during sign-in:', error);
}