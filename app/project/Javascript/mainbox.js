const left = document.querySelector(".left");
const right = document.querySelector(".right");
const container = document.querySelector(".container");
// Select the elements with the classes "left", "right", and "container" from the DOM

// Add event listeners for mouseenter and mouseleave events on the "left" element
left.addEventListener("mouseenter", () => {
    // Add the "hover-left" class to the "container" element on mouseenter
    container.classList.add("hover-left");
});

left.addEventListener("mouseleave", () => {
    // Remove the "hover-left" class from the "container" element on mouseleave
    container.classList.remove("hover-left");
});

// Add event listeners for mouseenter and mouseleave events on the "right" element
right.addEventListener("mouseenter", () => {
    // Add the "hover-right" class to the "container" element on mouseenter
    container.classList.add("hover-right");
});
//class list is an method
right.addEventListener("mouseleave", () => {
    // Remove the "hover-right" class from the "container" element on mouseleave
    container.classList.remove("hover-right");
});


