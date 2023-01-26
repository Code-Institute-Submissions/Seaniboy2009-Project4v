## Clarks restaurant  
## 1. Purpose of the project: 
- the purpose of the project is to create a fully functioning restaurant  website with the main 
    part being a booking system so that users can book a table, for admins/staff to also create bookings and update and edit them.
## 2. User stories:
- as a user i want to view the menu before booking
- as a user i want to book a table as a guest
- as a user i want to view by bookings account will be required
- as a user i want to see my confirmed booking
- as a admin i want to create and delete tables in the restaurant and update the site
- as a admin i want to be able to view all tables
- as a admin i want to be able to create new tables
- as a admin i want to be able to delete tables
- as a admin i want to be able to see all bookings and manage
- as a admin i want to be able to create menu items
- as a admin i want to be able to delete menu items
## 3. Features: 
- The booking system needs to have one table created for any bookings to be made, each booking request date and time is checked against the tables bookings, if no bookins then a booking can happen, if one table is booked for the time and date but another is not, a booking can happen, if all tables have a booking for the time and date then no bookings can happen, there is also a check for the date and time slot so users cant book the same time and date regardless of how many tables there are(avoid duplicate bookings)  
- navigation bar
- no login

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/nav_pwjiku.png)

- admin login

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/navfull_q5evlf.png)

- Main page with the name of the site/restaurant

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741247/Wireframe/home1_cb6u5e.png)
![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741247/Wireframe/home2_fsipfe.png)

- Menu page with a list of starters, mains, sides and deserts

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741247/Wireframe/menu_i2svus.png)

- booking page with the option to book a table and if you have an account see your previous/current bookings

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741246/Wireframe/book1_e90voq.png)

- login, logout and sign up page
- management/admin page where an admin and create/delete tables, also update or delete bookings

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741246/Wireframe/management_wfjttr.png)

- Table management, create and delete tables, no bookings can be made without a table created
- Menu item creation and deletion
- bookings edit and deletion

## 4. Future features
- ability for users to update there booking rather than over the phone
- a UI layout of where the table are in the restaurant
- a reminder function that sends the user an email 1 hour before the booking
- ability of the app to combine tables together for larger group size
- users to leave a review on the page
- booking events
- booking as a guest

## 5. Typography and color scheme
- main scheme is black and white

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674741247/Wireframe/home1_cb6u5e.png)

- with green as hyperlinks

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/green_ye0hc8.png)

## 6. Wireframes
- Table class, the booking system works around how many tables there is and if each table is free 
for the time and date that is selected

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673955041/Wireframe/tablelayout_fvmdnk.png)

- interaction of table class and booking class

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674680477/Wireframe/table_booking_relationship_t6uraf.png)

## 7. Technology
- Frameworks
    - Django is the main framework [Django](https://www.djangoproject.com/)
    - Bootstrap for the HTML and CSS [Bootstrap](https://getbootstrap.com/)
- storage
    - cloudinary for media storage [cloudinary](https://cloudinary.com/)
- Database
    - elephantsql for the database [elephantsql](https://customer.elephantsql.com/)

## 8. testing
- code validation
    - CSS validation [CSS](https://jigsaw.w3.org/css-validator/validator)
    - HTML validation [HTML](https://validator.w3.org/)
    - Javascript validation [Javascript](https://pythontutor.com/javascript.html#mode=edit)
    - Python validation using [Python](https://pythontutor.com/python-debugger.html#mode=edit)
    - Spellchecker [Online Spellchecker](https://www.online-spellcheck.com/)

- automation testing
    - 11 tests created

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674475878/Wireframe/tests_v6wwnn.png)

- test cases (user story based)
    - user viewing the menu
        - menu url is available and visible in the navigation bar

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/navfull_q5evlf.png)

- user clicked menu
- user then has a list of starters, mains, sides and deserts

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954942/Wireframe/menu_qay4dp.png)

- user can click to see each item

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131345/Wireframe/menuitem_jn2zju.png)

- user booking a table
    - Booking url is available and visible in the navigation bar
    - user can enter amount of people, date, time, name and email
    - user can then click submit

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954941/Wireframe/booking-loggedout_eekm6l.png)

- user will be told if its booked

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131344/Wireframe/booking_sucess_vq1zsx.png)

- user will be told if it cant book

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131595/Wireframe/party_to_big_ckllme.png)

- user will be told if they have booked for this time/date already

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131344/Wireframe/already_made_booking_ehfsfv.png)

- user viewing  there bookings (Login and active account required)

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954941/Wireframe/booking-loggedin_enhwat.png)

- admin viewing tables (admin account required)
    - management url is available and visible in the navigation bar
    - admin signed in and can see the list of tables that are avalible on the right

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131807/Wireframe/list_of_all_tables_jffzub.png)

- admin viewing the bookings (admin account required)
    - management url is available and visible in the navigation bar
    - admin signs in and can see the tables bookings and can then expand by clicking each table to see the booking

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/manage_bookings_qbcq9i.png)
![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131807/Wireframe/manage_bookings_open_fnuyku.png)

- admin creating a table (admin account required)
    - management url is available and visible in the navigation bar
    - admin can click on create table and fillout the number and select capacity of the table and click submit

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/create_table_lig8ha.png)

- admin deleting a table (admin account required)
    - management url is available and visible in the navigation bar
    - admin can click delete then have a list of avalible tables, select one then click delete again
    - confirmation will popup admin can cancel or delete

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/delete_table_mjylgr.png

- admin updating a booking (admin account required)
    - management url is available and visible in the navigation bar
    - admin can click the table then on the booking update button, then can then change all the values and click update

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/edit_booking_vndjwo.png)

- admin deleting a booking (admin account required)
    - management url is available and visible in the navigation bar
    - admin can click the table then on the delete button of the booking

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131807/Wireframe/manage_bookings_open_fnuyku.png)

- admin creating menu item (admin account required)
    - management url is available and visible in the navigation bar
    - admin can click on create menu item and fillout the details and click submit

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/create_menu_izykm7.png)

- admin deleting menu item(admin account required)
    - management url is available and visible in the navigation bar
    - admin can click delete then have a list of avalible menu items, select one then click delete again
    - confirmation will popup admin can cancel or delete

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1674131806/Wireframe/delete_menu_ircalr.png)


- fixed bugs
    - had a hard time trying to implement more than one table booking, the code was fine for any booking with one table, but as soon as there were two tables the functons where not working, i had to re-do the code a few times

- issues
    - bookings should not be deleted from the Django admin pannel as it will not update the booking amount for the table

- supported screens and browsers
    - tested using a galaxy s10 and s10 plus
    - tested on chrome on windows 10
    - tested on edge on windows 10

## 9. Deployment
   - Heroku
    - Deployment from heroku involved signing up to the site, click create your first app. to deploy my project i went to settings tab, click on add config vars and added the below:
        - API_KEY_KEY
        - API_SECRET_KEY
        - CLOUDINARY_URL
        - CLOUD_NAME_KEY
        - DATABASE_URL
        - DEBUG
        - DEVELOPMENT
        - PORT
        - SECRET_KEY
- once done i then clicked on the deploy tab linked to my github, selected the main branch then deployed, i set this to automatic deploys so when ever i made a change it would do it. New app > settings > config var > build packs > deploy
   
- via gitpod
   - Deployment from gitpod was done by adding changes to the python3 command line.
   - git add .
   - git commit -m "changes in here"
   - git push

## 10. Credits

- site layout was taken from https://www.millerandcarter.co.uk/#/
