// render contents of new page in main view
function load_page(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        const res = request.responseText;
        document.querySelector('#body').innerHTML = res;
    };

    // push state to URL
    document.title = name;
    history.pushState(null, name, name);

    request.send();
};