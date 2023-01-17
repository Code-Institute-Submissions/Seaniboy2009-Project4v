![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Clarks resturant 
## 1. Purpose of the project: 
    - the purpose of the project is to create a fully functionng resturant website with the main part being a booking system so that users can book a table, for admins/staff to also create bookings and update and edit them.
## 2. user stories:
    - as a user i want to view the menu before booking
    - as a user i want to book a table as a guest
    - as a user i want to view by bookings account will be required
    - as a user i want to see my confirmed booking
    - as a admin i want to create and delete tables in the resturant and update the site
    - as a admin i want to be able to view all tables
    - as a admin i want to be able to see all bookings and manage
## 3. Features: 
    - navigation bar
    - Main page with the name of the site/resturant
    - Menu page with a list of starters, mains, sides and deserts 
    - booking page with the option to book a table and if you have an account see your previous/current bookings 
    - login, logou and signup page
    - managemnet/admin page where an admin and create/delete tables, also update or delete bookings
## 4. future features
    - ability for users to update there booking rather than over the phone
    - a UI layout of where the table are in the resturant
    - a reminder function that sends the user an email 1 hour before the booking
## 5. Typography and color scheme
## 6. wireframes
## 7. Technology
## 8. testing
   - 8.1 code validation
   - 8.2 test cases (user story based with screenshots)
   - 8.3 fixed bugs
    - had a hard time trying to implement more than one table booking, the code was fine for any booking with one table, but as soon as there was two tables the    functons where not working, i had to re-do the code a few times
   - 8.4 supported screens and browsers
## 9. Deployment
   - 9.1 Heroku
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
   
- 9.2 via gitpod
   - Deployment from gitpod was done by adding changes to the python3 command line, command to add changes git add ., adds each file to the awating commit, then type in commit -m "changes in here", once i was happy with that i could then push them to github, using git push command, as i set up heroku with auto deploy it would pull the updates sent from github.
## 10. credits

- site layout was taken from https://www.millerandcarter.co.uk/#/
