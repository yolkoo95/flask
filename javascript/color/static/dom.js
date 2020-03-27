document.addEventListener("DOMContentLoaded", () => {
    // only keyword "function" will make "this" work
    document.querySelector("#color-change").onchange = function() {
        document.querySelector("#hello").style.color = this.value;
    }
})