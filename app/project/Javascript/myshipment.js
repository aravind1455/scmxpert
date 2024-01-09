
document.querySelector('.nextBtn').addEventListener('click', function(event) {
    event.preventDefault(); // Prevents default form submission behavior

    var inputs = document.querySelectorAll('input[type="text"], input[type="number"], select, input[type="date"]');
    var isValid = true;

    inputs.forEach(function(input) {
        if (input.value.trim() === '') {
            isValid = false;
            input.classList.add('error'); // Add error class for styling
        } else {
            input.classList.remove('error'); // Remove error class if input is filled
        }
    });

    if (isValid) {
        // All fields are filled, so you can proceed with form submission or other actions
        // For example, you can submit the form by uncommenting the line below:
        // document.querySelector('form').submit();
        alert('Form submitted successfully!');
    } else {
        alert('Please fill in all fields.');
    }
});
// document.getElementById('shipment_number').addEventListener('input', function() {
//     var shipmentInput = document.getElementById('shipment_number').value;
//     var errorSpan = document.getElementById('shipment_error');
    
//     if (shipmentInput.length > 0 && parseInt(shipmentInput) <= 7) {
//         errorSpan.textContent = "Shipment number must be greater than 7";
//     } else {
//         errorSpan.textContent = "";
//     }
// });