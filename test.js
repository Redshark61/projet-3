const list = document.querySelectorAll("#doctors option");
const inputCities = document.querySelector("input[list='doctors']");
const inputAdress = document.querySelector("input#street");
const loading = document.querySelector(".loading");

inputCities.addEventListener("keyup", function (e) {
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

// add event listener to input on enter key
inputAdress.addEventListener("keyup", async function (e) {
    if (e.keyCode === 13) {
        // Cancel the default action, if needed
        e.preventDefault();
        // Trigger the button element with a click
        loading.classList.add("active");
        await validate();
        loading.classList.remove("active");
        loading.classList.add("done");
    }
});

async function validate() {
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

        postcode = await getPostCode();

        const url = `https://api-adresse.data.gouv.fr/search/?q=${value}&postcode=${postcode}&limit=1`;
        fetch(url)
            .then((response) => response.json())
            .then((data) => {
                const p = document.createElement("p");
                let properties = data.features[0].properties;
                p.innerHTML = properties.name + "</p><br/>" + properties.city + "</p><br/>" + url;
                document.body.appendChild(p);
                resolve();
            });
    });
}

function getPostCode() {
    // convert the city name to postcode

    return new Promise((resolve) => {
        const http2 = new XMLHttpRequest();
        const url2 =
            "https://raw.githubusercontent.com/Rudloff/french-postal-codes-api/master/insee.csv";
        http2.open("GET", url2);
        http2.send();

        http2.onreadystatechange = (e) => {
            if (http2.readyState === 4 && http2.status === 200) {
                const data = http2.responseText;
                const lines = data.split("\n");
                lines.forEach(function (line) {
                    const columns = line.split(";");
                    if (columns[0].toLowerCase() === inputCities.value.toLowerCase()) {
                        postcode = columns[1];
                        console.log("postcode " + postcode);
                        resolve(postcode);
                    }
                });
            }
        };
    });
}
