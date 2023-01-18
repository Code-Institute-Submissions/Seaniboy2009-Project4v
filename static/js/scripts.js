document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded");
    let menu_button = document.getElementById("menu-toggle");
    let buttons = document.getElementsByTagName("button");
    let menu_list = document.getElementById("navbarSupportedContent");
    let copyright_text = document.getElementById("copyright");

    // Menu button toggle
    menu_button.addEventListener("click", () => {
        console.log("menu button clicked")
        menu_list.classList.toggle("collapse");
    });
    
    // Add event listeners to each button, this is used to change the model text for table, booking and menu item crud
    for (let button of buttons) {
        button.addEventListener("click", (e) => {
            let button = e.target;
            updateModel(button);

            if (button.value == "confirmModalButton") {
                console.log("Model button pressed")
            }
        })};

    // update copyright date
    copyright_text.innerText = new Date().getFullYear();

    // Close any alerts after 3000 Mseconds 
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

    // Update the model depending on what you are deleting, it will hide/unhide the corresponding button
    function updateModel(button) {

        let modelHeading = document.getElementById("confirmModalLabel");
        let modelBody = document.getElementById("confirmModalBody");
        let menuButton = document.getElementById("delete-menu-button");
        let tableButton = document.getElementById("delete-table-button");
        tableButton.style.display = "none"
        menuButton.style.display = "none"

        if (button.value == "delete-table") {

            console.log("delete table called");
            tableButton.style.display = "block"
            modelHeading.innerText = `Confirm table deletion`;
            modelBody.innerText = `Please confirm you want to delete this table, once deleted this can not be undone, this will also delete all bookings for this table.`;
        } else if (button.value == "delete-menu-item") {

            console.log("delete menu item called");
            menuButton.style.display = "block"
            modelHeading.innerText = `Confirm menu item deletion`;
            modelBody.innerText = `Please confirm you want to delete this Menu item, once deleted this can not be undone.`;
        }
    }
})
