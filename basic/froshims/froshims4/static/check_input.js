
document.querySelector('form').onsubmit = function() {
    if (!document.querySelector('input').value) {
        alert('You must provide your name');
        return false;
    }
    if (!document.querySelector('select').value) {
        alert('You must provide your dorm');
        return false;
    }

    return true;
}