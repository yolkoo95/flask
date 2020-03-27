document.addEventListener("DOMContentLoaded", () => {
    // connect to web socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // when connected, configure buttons
    socket.on('connect', () => {
        document.querySelectorAll("button").forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection': selection});
            };
        });
    });

    // when a new vote announced, add to the unordered list
    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector("#votes").append(li);
    });
});