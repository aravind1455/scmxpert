if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

$(document).ready(function(){
  const token = localStorage.getItem("access_token");

  function redirectToLogin() {
      console.log("Redirecting to login page");
      window.location.href = "/login"; // Change "/login" to the actual login page URL
  }

  console.log("Token:", token);

  // Check if token exists and not expired
  if (token) {
      fetch(`/shipment`, {
          method: "GET",
          headers: {
              "Authorization": `${localStorage.getItem("access_token")}`,
              'Content-Type': 'application/json',
          },
      })
      .then(response => {
        console.log("Response Status:", response.status);
    
        // Check if the response status is 401 (Unauthorized)
        if (response.status === 401) {
            console.log("Redirecting to login due to 401 error");
            redirectToLogin();
            return Promise.reject("Unauthorized");
        }
    
        // Continue processing for other response statuses
        if (response.status !== 200) {
            throw new Error(`Status ${response.status}`);
        }
    
        return response.json();
    })
      .then(response => {
          console.log("API Response:", response);
          if (response.status_code === 400) {
              console.log("Error:", response.detail);
              $("#error").text(response.detail);
          }

          let shipment_data = "";
          for (let shipment_no = 0; shipment_no < response.length; shipment_no++) {
              const shipment = response[shipment_no];

              shipment_data = shipment_data + "<tr><td>"
                  + shipment.shipment_number + "</td><td>"
                  + shipment.container_number + "</td><td>"
                  + shipment.route_details + "</td><td>"
                  + shipment.goods_type + "</td><td>"
                  + shipment.device + "</td><td>"
                  + shipment.expected_delivery + "</td><td>"
                  + shipment.po_number + "</td><td>"
                  + shipment.delivery_number + "</td><td>"
                  + shipment.ndc_number + "</td><td>"
                  + shipment.batch_id + "</td><td>"
                  + shipment.serial_number + "</td><td>"
                  + shipment.shipment_description + "</td></tr>";
          }

          console.log("Shipment Data:", shipment_data);
          $("#table_data").html(shipment_data);
      })
      .catch(error => {
          console.log("Error:", error.message);
          // Check if the error is due to token expiration
          if (error.status === 401) {
              console.log("Redirecting to login due to 401 error");
              redirectToLogin();
          }
      });
  } else {
      // Token is missing, redirect to login page
      console.log("Token is missing, redirecting to login page");
      redirectToLogin();
  }
});





function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
        // You can add more cleanup here if needed
    }
    