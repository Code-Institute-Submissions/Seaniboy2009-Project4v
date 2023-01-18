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
- as a admin i want to be able to see all bookings and manage
## 3. Features: 
- navigation bar
- no login

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/nav_pwjiku.png)

- admin login

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/navfull_q5evlf.png)

- Main page with the name of the site/restaurant

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954942/Wireframe/home_ikqjjp.png)

- Menu page with a list of starters, mains, sides and deserts

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954942/Wireframe/menu_qay4dp.png)

- booking page with the option to book a table and if you have an account see your previous/current bookings

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954941/Wireframe/booking-loggedout_eekm6l.png)

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954941/Wireframe/booking-loggedin_enhwat.png)

- login, logout and sign up page
- management/admin page where an admin and create/delete tables, also update or delete bookings

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673954941/Wireframe/management_wwjxda.png)

## 4. Future features
- ability for users to update there booking rather than over the phone
- a UI layout of where the table are in the restaurant
- a reminder function that sends the user an email 1 hour before the booking

## 5. Typography and color scheme
- main scheme is black and white

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/scheme_ymejbb.png)

- with green as hyperlinks

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673958261/Wireframe/green_ye0hc8.png)

## 6. Wireframes
- Table class

![Header](https://res.cloudinary.com/dgj9rjuka/image/upload/v1673955041/Wireframe/tablelayout_fvmdnk.png)

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

- test cases (user story based)
    - user viewing the menu
        - menu url is available and visible in the navigation bar
    - user booking a table
        - menu url is available and visible in the navigation bar
    - user viewing  there bookings (Login and active account required)
        - menu url is available and visible in the navigation bar
    - admin viewing the bookings (Login and active account required)
        - menu url is available and visible in the navigation bar
    - admin creating a table (admin account required)
        - menu url is available and visible in the navigation bar
    - admin deleting a table (admin account required)
        - menu url is available and visible in the navigation bar
    - admin updating a booking (admin account required)
        - menu url is available and visible in the navigation bar
    - admin deleting a booking (admin account required)
        - menu url is available and visible in the navigation bar

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
   - Deployment from gitpod was done by adding changes to the python3 command line, command to add changes git add ., adds each file to the commit, then type in commit -m "changes in here", once i was happy with that i could then push them to github, using git push command, as i set up heroku with auto deploy it would pull the updates sent from github.

## 10. Credits

- site layout was taken from https://www.millerandcarter.co.uk/#/
