// Get the DOM elements
const modalBG = document.querySelector(".js-modal-bg");
const modal = document.querySelector(".js-modal");
const modalClose = document.querySelector(".js-modal-close");
const modalInput = document.querySelector(".js-modal-input");

// Add the modal
modalInput.addEventListener("click", (e) => {
	e.preventDefault();
	modal.classList.add("modal--active");
	modalBG.classList.add("modal-bg--active");
});

// Remove the modal
modalClose.addEventListener("click", (e) => {
	e.preventDefault();
	modal.classList.remove("modal--active");
	modalBG.classList.remove("modal-bg--active");
});
