document.addEventListener("DOMContentLoaded", () => {
    // connect to web socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // when connected, configure buttons, when click button, send result to server
    socket.on('connect', () => {
        document.querySelectorAll("button").forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection': selection});
            };
        });
    });

    // when vote total updated and broadcast by server, update vote totals
    socket.on('vote totals', data => {
        document.querySelector('#yes').innerHTML = data.yes;
        document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    });
});