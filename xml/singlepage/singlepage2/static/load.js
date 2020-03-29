// track back history information when click back button
window.onpopstate = e => {
    const data = e.state;
    document.title = data.title;
    document.querySelector('#body').innerHTML = data.text;
}

// render contents of new page in main view
function load_page(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        const res = request.responseText;
        document.querySelector('#body').innerHTML = res;
    
        // push state to URL
        document.title = name;
        history.pushState({'title': name, 'text': res}, name, name); // also push data that we want to track back
                                                                     // history.pushState(data, title, url)
    };

    request.send();
};