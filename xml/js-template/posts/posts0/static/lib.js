// start with first post and load 20 posts at a time
let counter = 1;
const quantity = 20;

// when to load page
document.addEventListener('DOMContentLoaded', load);
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
}

function load() {
    // set up start and end numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1; 
    
    // get new posts
    const request = new XMLHttpRequest();
    request.open('POST', '/posts')
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        data.forEach(add_post);
    };

    const data = new FormData();
    data.append('start', start);
    data.append('end', end);

    request.send(data);
}

// add new post to html page
function add_post(contents) {
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = contents;

    document.querySelector('#posts').append(post);
}