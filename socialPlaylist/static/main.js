const nav = document.getElementsByClassName('navbar')[0],
    path = window.location.pathname;

if (path === '/') {
    nav.className += ' hidden';
}