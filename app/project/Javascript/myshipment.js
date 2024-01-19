if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}
document.addEventListener("DOMContentLoaded", function () {
    // Set the minimum date for the date input field to today's date
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    var yyyy = today.getFullYear();

    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById('expected_delivery').min = today;

    document.querySelector('.nextBtn').addEventListener('click', function (event) {
        event.preventDefault(); // Prevents default form submission behavior

        var inputs = document.querySelectorAll('input[type="text"], input[type="number"], select, input[type="date"]');
        var isValid = true;

        inputs.forEach(function (input) {
            if (input.value.trim() === '') {
                isValid = false;
                input.classList.add('error'); // Add error class for styling
            } else {
                input.classList.remove('error'); // Remove error class if input is filled
            }
        });

        // Additional check for Shipment Number length
        var shipmentNumberInput = document.getElementById('shipment_number');
        if (shipmentNumberInput.value.trim().length !== 7) {
            isValid = false;
            shipmentNumberInput.classList.add('error');
        } else {
            shipmentNumberInput.classList.remove('error');
        }

        if (isValid) {
            // All fields are filled and Shipment Number is of length 7
            // You can proceed with form submission or other actions
            // For example, you can submit the form by uncommenting the line below:
            // document.querySelector('form').submit();
            alert('Form submitted successfully!');

            // Clear all input fields
            
        } else {
            alert('Please fill in all fields and ensure Shipment Number has a length of 7.');
        }
    });
});





document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submit").addEventListener("click", function(event) {
      event.preventDefault();
        console.log("Dom load", localStorage.getItem("access_token"));
        fetch("/myshipments", {
              method: "POST",
              headers: {
                  'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
                  'Content-Type': 'application/json',
              },
              body : JSON.stringify({
                "shipment_number": $("#shipment_number").val(),
                "container_number": $("#container_number").val(),
                "route_details": $("#route_details").val(),
                "goods_type": $("#goods_type").val(),
                "device": $("#device").val(),
                "expected_delivery":$("#expected_delivery").val(),
                "po_number": $("#po_number").val(),
                "delivery_number": $("#delivery_number").val(),
                "ndc_number": $("#ndc_number").val(),
                "batch_id": $("#batch_id").val(),
                "serial_number": $("#serial_number").val(),
                "shipment_description": $("#shipment_description").val(),
              }),
          })
              .then(response => {
                  if (response.status === 200) {
                    
                      return response.json();
                  }
                  else {
                    $("#error-message").text("Please Enter the emplty fields");
                    $("#error-message").css("visibility", "visible");
                }
              }).then(jsonresponse => {
                console.log(jsonresponse.error_message);
                $("#error").text(jsonresponse.error_message);
              })
              .catch(error => {
                $("#error-message").text(error.message);
                $("#error-message").css("visibility", "visible");
            });
            
    });
});


function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/login";
    // You can add more cleanup here if needed
}