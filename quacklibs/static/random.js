function random_redirect(links) {
    function random(links) {
        var number = Math.floor(Math.random() * links.length);
        return links[number];
    }
    document.addEventListener("DOMContentLoaded", function() {
        start = document.querySelector(".start");
        start.onclick = function() {
            let link = random(links);
            window.location.href = link;
        };
    });
}
