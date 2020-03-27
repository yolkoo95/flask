document.addEventListener("DOMContentLoaded", () => {

    document.querySelector("#new-form").onsubmit = () => {
        alert("received");

        // initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector("#currency").value;

        request.open("POST", "/convert");

        // callback function for when request completes
        request.onload = () => {
            // extract JSON data from request
            const data = JSON.parse(request.responseText);

            // update the result div
            if (data.success) {
                const contents = `1 EUR is equal to ${data.rate} ${currency}.`
                document.querySelector("#result").innerHTML = contents;
            }
            else {
                document.querySelector("#result").innerHTML = " Error ";
            }
        };

        // for XML request with POST method, data should be formatted
        const data = new FormData();
        data.append('currency', currency);

        request.send(data);
        
        return false;
    };
});