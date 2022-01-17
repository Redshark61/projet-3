const inputsSecurityCode = document.querySelectorAll(".js-security-code");

inputsSecurityCode.forEach((input) => {
    new Cleave(input, {
        delimiters: ["-", "-", "-", "-", "-", " "],
        blocks: [1, 2, 2, 2, 3, 3, 2],
        numericOnly: true,
    });
});
