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

const http = new XMLHttpRequest();
const url = "https://raw.githubusercontent.com/Rudloff/french-postal-codes-api/master/insee.csv";
http.open("GET", url);
http.send();

http.onreadystatechange = (e) => {
    if (http.readyState === 4 && http.status === 200) {
        const data = http.responseText;
        const lines = data.split("\n");
        const list = document.querySelector("datalist");
        lines.forEach(function (line) {
            const columns = line.split(";");
            const option = document.createElement("option");
            option.value = columns[0];
            option.textContent = columns[1];
            list.appendChild(option);
        });
    }
};
