document.addEventListener("DOMContentLoaded", () => {
    let menuButton = document.getElementById("menu-toggle");
    let buttons = document.getElementsByTagName("button");
    let menuList = document.getElementById("navbarSupportedContent");
    let copyrightText = document.getElementById("copyright");

    // Menu button toggle
    menuButton.addEventListener("click", () => {
        menuList.classList.toggle("collapse");
    });

    // Update the model depending on what you are deleting, it will hide/unhide the corresponding button
    function updateModel(buttonClicked) {

        let modelHeading = document.getElementById("confirmModalLabel");
        let modelBody = document.getElementById("confirmModalBody");
        let deleteMenuButton = document.getElementById("delete-menu-button");
        let tableButton = document.getElementById("delete-table-button");
        tableButton.style.display = "none"
        deleteMenuButton.style.display = "none"

        if (buttonClicked.value === "delete-table") {

            tableButton.style.display = "block"
            modelHeading.innerText = `Confirm table deletion`;
            modelBody.innerText = `Please confirm you want to delete this table, once deleted this can not be undone, 
                                    this will also delete all bookings for this table.`;
        } else if (buttonClicked.value === "delete-menu-item") {

            deleteMenuButton.style.display = "block"
            modelHeading.innerText = `Confirm menu item deletion`;
            modelBody.innerText = `Please confirm you want to delete this Menu item, once deleted this can not be undone.`;
        }
    }
    
    // Add event listeners to each button, this is used to change the model text for table, booking and menu item crud
    for (let button of buttons) {
        button.addEventListener("click", (e) => {
            let button = e.target;
            updateModel(button);
        })};

    // update copyright date
    copyrightText.innerText = new Date().getFullYear();

    // Close any alerts after 3000 Mseconds 
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

})
