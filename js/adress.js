const inputCities = document.querySelector(".js-input-cities");
const inputAdress = document.querySelector(".js-input-address");
const loading = document.querySelector(".loading");

// const url = "https://raw.githubusercontent.com/Rudloff/french-postal-codes-api/master/insee.csv";
// const http = new XMLHttpRequest();
// http.open("GET", url);
// http.send();

// http.onreadystatechange = (e) => {
//     if (http.readyState === 4 && http.status === 200) {
//         const data = http.responseText;
//         const lines = data.split("\n");
//         const list = document.querySelector("datalist");
//         lines.forEach(function (line) {
//             const columns = line.split(";");
//             const option = document.createElement("option");
//             option.value = columns[0];
//             option.textContent = columns[1];
//             list.appendChild(option);
//         });
//     }
// };

// const line = (async () => {
//     return getCities();
// })();
getCities().then((value) => {
    inputAdress.line = value;
});

// add event listener to input on enter key
inputAdress.addEventListener("keyup", async function (e) {
    if (e.keyCode === 13) {
        // Cancel the default action, if needed
        e.preventDefault();
        // Trigger the button element with a click
        loading.classList.add("active");
        await validate(e.currentTarget.line);
        loading.classList.remove("active");
        loading.classList.add("done");
    }
});

async function validate(lines) {
    return new Promise(async (resolve) => {
        // replace spaces with +
        value = inputAdress.value.replace(/\s/g, "+");
        // replace apostrophes with +
        value = value.replace(/'/g, "+");
        // replace accents with non-accented letters
        value = value.replace(/[àáâãäå]/g, "a");
        value = value.replace(/[ç]/g, "c");
        value = value.replace(/[éèêë]/g, "e");
        value = value.replace(/[îï]/g, "i");
        value = value.replace(/[ôö]/g, "o");
        value = value.replace(/[ùûü]/g, "u");

        // console.log(lines);
        postcode = getPostCode(lines);
        console.log(postcode);

        const url = `https://api-adresse.data.gouv.fr/search/?q=${value}&postcode=${postcode}&limit=1`;
        fetch(url)
            .then((response) => response.json())
            .then((data) => {
                const p = document.createElement("p");
                // console.log(url);
                // console.log(data.features);
                let properties = data.features[0].properties;
                p.innerHTML = properties.name + "</p><br/>" + properties.city + "</p><br/>" + url;
                document.body.appendChild(p);
                resolve();
            });
    });
}

function getPostCode(lines) {
    let postcode = 0;
    lines.forEach(function (line) {
        const columns = line.split(";");
        if (columns[0].toLowerCase() === inputCities.value.toLowerCase()) {
            postcode = columns[1];
            console.log("postcode " + postcode);
            return;
        }
    });
    return postcode;
}

async function getCities() {
    const url =
        "https://raw.githubusercontent.com/Rudloff/french-postal-codes-api/master/insee.csv";

    return new Promise(async (resolve) => {
        fetch(url)
            .then((response) => response.text())
            .then((data) => {
                const lines = data.split("\n");
                const list = document.querySelector("datalist");
                lines.forEach(function (line) {
                    const columns = line.split(";");
                    const option = document.createElement("option");
                    option.value = columns[0];
                    option.textContent = columns[1];
                    list.appendChild(option);
                });
                resolve(lines);
            });
    });
}
