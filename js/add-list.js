const add = document.querySelectorAll(".js-add-element");
const list = document.querySelectorAll(".js-list");
const input = document.querySelectorAll(".js-input");
const deleteButton = document.querySelectorAll(".js-delete");
let item = document.querySelectorAll(".js-item");

add.forEach(function (element, key) {
    element.addEventListener("click", createElement.bind(null, key));
});

function createElement(key) {
    const inputValue = input[key].value;
    if (inputValue === "") {
        alert("Please enter a value");
    } else {
        const newElement = document.createElement("li");
        newElement.classList.add("form__item");
        newElement.classList.add("js-item");

        const deleteButton = document.createElement("span");
        const content = document.createElement("span");
        deleteButton.textContent = "❌";
        content.textContent = inputValue;
        content.classList.add("form__element");
        deleteButton.classList.add("form__delete");
        deleteButton.classList.add("js-delete");

        newElement.appendChild(content);
        newElement.appendChild(deleteButton);
        list[key].appendChild(newElement);
        input[key].value = "";
        deleteButton.addEventListener("click", deleteItem);
    }
}

function deleteItem(e) {
    e.target.parentNode.remove();
}
