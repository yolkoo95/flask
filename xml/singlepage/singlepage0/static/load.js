// render contents of new page in main view
function load_page(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        const res = request.responseText;
        document.querySelector('#body').innerHTML = res;
    };

    request.send();
};