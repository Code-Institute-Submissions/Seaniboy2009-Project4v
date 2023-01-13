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

    // Close any alerts after 3000 Mseconds 
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

    $('#confirmModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var recipient = button.data('whatever') // Extract info from data-* attributes

        console.log(button.value)

        var modal = $(this)
        modal.find('.modal-title').text('New message to ' + recipient)
        modal.find('.modal-body input').val(recipient)
      })
})
