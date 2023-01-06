document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded");
    let menu_button = document.getElementById("menu-toggle");
    let menu_list = document.getElementById("navbarSupportedContent");
    let copyright_text = document.getElementById("copyright");

    // Menu button toggle
    menu_button.addEventListener("click", () => {
        console.log("menu button clicked")
        menu_list.classList.toggle("collapse");
    });

    // update copyright date
    copyright_text.innerText = new Date().getFullYear();

    // For dropdown list under bookings
    // $('.collapse').collapse()

    // CLose any alerts after 3000 Mseconds 
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
})
