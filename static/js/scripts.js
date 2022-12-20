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
})
