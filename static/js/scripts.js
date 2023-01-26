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
        let deleteTableButton = document.getElementById("delete-table-button");
        let deleteBookingButton = document.getElementById("delete-booking-button");
        let bookingButton = document.getElementById("booking-button");

        // Set all the buttons to not visible
        deleteTableButton.style.display = "none";
        deleteMenuButton.style.display = "none";
        deleteBookingButton.style.display = "none";
        bookingButton.style.display = "none";

        if (buttonClicked.value === "delete-table") {

            deleteTableButton.style.display = "block"
            modelHeading.innerText = `Confirm table deletion`;
            modelBody.innerText = `Please confirm you want to delete this table, once deleted this can not be undone, 
                                    this will also delete all bookings for this table.`;
        } else if (buttonClicked.value === "delete-menu-item") {

            deleteMenuButton.style.display = "block"
            modelHeading.innerText = `Confirm menu item deletion`;
            modelBody.innerText = `Please confirm you want to delete this Menu item, once deleted this can not be undone.`;
        } else if (buttonClicked.value === "delete-booking") {

            deleteBookingButton.style.display = "block"
            modelHeading.innerText = `Confirm booking deletion`;
            modelBody.innerText = `Please confirm you want to delete this booking, once deleted this can not be undone.`;
        } else if (buttonClicked.value === "submit-booking") {

            bookingButton.style.display = "block";
            form = bookingButton.form;
            number_of_guests = form.elements["number_of_guests"].value;
            booking_date_month = form.elements["booking_date_month"].value;
            booking_date_day = form.elements["booking_date_day"].value;
            booking_date_year = form.elements["booking_date_year"].value;
            booking_time = form.elements["booking_time"].value;
            modelHeading.innerText = `Confirm booking`;
            modelBody.innerText = `For ${number_of_guests} People
                                    On: ${booking_date_month}/${booking_date_day}/${booking_date_year} 
                                    At: ${booking_time}`;
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
