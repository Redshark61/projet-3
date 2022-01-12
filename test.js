const list = document.querySelectorAll("option");
const input = document.querySelector("input");

input.addEventListener("keyup", function (e) {
    const value = e.target.value.toLowerCase();
    list.forEach(function (item) {
        const text = item.textContent.toLowerCase();
        if (text.indexOf(value) > -1) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    });
});
