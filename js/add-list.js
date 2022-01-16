const add = document.querySelectorAll(".js-add-element");
const list = document.querySelectorAll(".js-list");
const input = document.querySelectorAll(".js-input");
const deleteButton = document.querySelectorAll(".js-delete");
const item = document.querySelectorAll(".js-item");

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
        deleteButton.addEventListener("click", deleteItem.bind(null, key));
    }
}

deleteButton.forEach(function (element, key) {
    element.addEventListener("click", deleteItem.bind(null, key));
});

function deleteItem(key) {
    list[key].removeChild(item[key]);
}
