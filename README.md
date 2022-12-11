# Office Space Booking - Smithfield Square

This booking site allows registered users to create bookings to secure office space. The user can also view, update and delete their bookings. The user can choose from available office space only. Both desks and meeting rooms are available for booking. The administrator can view, create, update and delete available office space resources.

![Responsive Mockup](/documentation/screenshots/am-i-responsive.png)

The live site is available for use on [Heroku](https://deskbooking.herokuapp.com/).

## UX

### Strategy

__Agile__

This project uses the Agile methodology presented on the GitHub platform. There are seven epics shown as milestones and 14 user stories shown as issues in GitHub. These user stories are split into [three project iterations](https://github.com/teresabowe/booking-system/projects?query=is%3Aopen). The aim is to deliver a usable product at the end of each iteration.

__Project Goal__

The goal of the project is to create a website to allow users to book their desks or meeting rooms in a shared office space. It was inspired as a result of the increasing use of flexible workspaces by companies.

A typical user is someone:

- who is visiting and wishes to understand the purpose of the site, how to register and book a space
- who is registered and wants to book a space in the shared office space
- who is an office manager and wants to manage capacity in the office space
- who is an office manager and wants to manage desks and bookings

Key features identified are:

- Site administration to manage desks and bookings
- User signup and authentication
- Landing page showcasing the office space and facilitating the booking
- User bookings management
- Office manager desk administration and reporting
- User account management

### Scope

The initial scope for this project is documented below in the epics and stories. Each user story has a flag indicating prioritisation and implementation status. There is also a link to each user story in GitHub. The scope at the project planning stage was quite broad and incorporated a user front end for the office manager and additional user profile features. These features are not currently present but will be implemented in future iterations of the project.

__Epics and User Stories__

Epic: Initial Project Setup

User Stories:

- As a developer, I can install Django and support libraries so that I have the appropriate environment ready to be able to proceed with the development (must-have / complete) <a href="https://github.com/teresabowe/booking-system/issues/1" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/1/hovercard">#1</a>
- As a developer, I can create a hosting environment so that I can present the site to the end user (must-have / complete) <a href="https://github.com/teresabowe/booking-system/issues/2" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/2/hovercard">#2</a>

Epic: Setup Site Administration to Manage Desks and Bookings

User Stories:

- As a site administrator, I can CRUD desks so that I can manage site content (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/3" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/3/hovercard">#3</a>
- As a site administrator, I can CRUD bookings so that manage my customer's needs (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/4" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/4/hovercard">#4</a>

Epic: User Authentication

User Stories:

- As a site visitor, I can register on the site so that I can access the site services (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/6" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/6/hovercard">#6</a>
- As a registered user, I can login so that I have access to my content (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/7" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/7/hovercard">#7</a>
- As a registered user, I can logout of my account so that my content is kept secure (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/8" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/8/hovercard">#8</a>

Epic: Create Landing Page

User Story:
As a site visitor, I can access the landing page so that I can understand the purpose of the site and take appropriate actions (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/5" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/5/hovercard">#5</a>

Epic: User Bookings Management

User Story:

- As a registered user I can create, read, update and delete my bookings so that I can maintain an accurate record of my use of the desk space (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/9" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/9/hovercard">#9</a>

Epic: Office Manager Desk Administration and Reporting

User Stories:

- As a registered user with the role of office manager, I can create, read, update and delete desks so that I can keep the site content up to date (could-have/future implementation) <a href="https://github.com/teresabowe/booking-system/issues/11" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/11/hovercard">#11</a>
- As a registered user with the role of office manager, I can create, read, update and delete bookings so that I can keep the site content up to date (could-have/future implementation) <a href="https://github.com/teresabowe/booking-system/issues/10" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/10/hovercard">#10</a>
- As a registered user with the role of office manager, I can run relevant capacity reporting for the office spaces so that I can manage facilities for the site (should-have/future implementation)<a href="https://github.com/teresabowe/booking-system/issues/11" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/11/hovercard">#11</a>

Epic: User Account Management

User Stories:

- As a registered user, I can change my password so that I can login to make bookings (could-have/future implementation) <a href="https://github.com/teresabowe/booking-system/issues/13" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/13/hovercard">#13</a>
- As a registered user, I can edit my user profile so that I can keep my profile up to date (could-have/future implementation) <a href="https://github.com/teresabowe/booking-system/issues/14" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/14/hovercard">#14</a>



### Structure

The website has five user pages currently.  There is a home page that is open to all users both registered and non-registered.  The bookings page can only be accessed by registered users.  Here it is possible to add, update and delete bookings.  There are also registration, login, and logout pages.  

The main flow for the bookings page is shown below.

![Responsive Mockup](/documentation/screenshots/flow-diagram-bookings.png)

### Skeleton

__Wireframes__

The Bootstrap carousel example was considered for use and chosen for use early in the project.  The wireframes were drawn up with some adjustments which include square images underneath the carousel.  The final deployment of the website has centered links on the navigation bar and a user status for login on the right side.  A custom logo was also created for the home page link on the left side of the navigation bar.

![Entity Relationship Diagram](/documentation/screenshots/desktop-wireframe-bookings-home-page.png)
![Entity Relationship Diagram](/documentation/screenshots/desktop-wireframe-bookings-list-page.png)
![Entity Relationship Diagram](/documentation/screenshots/mobile-wireframe-pages.png)

__Database Schema__

There are two custom models in the database schema, a desk model and a bookings model.  The desk model records all of the available desks and meeting rooms.  The bookings model handles the user bookings for the office spaces.  The django-allauth application manages the account registration and authentication so a custom model is not required in this instance.

![Entity Relationship Diagram](/documentation/screenshots/entity-relationship-diagram-bookings.png)

### Surface Design

The overall design aims to present a simple, clean website which demonstrates that the overall purpose is to book office space.  A carousel example template from Bootstrap 4.1 was used as the starting point for developing the templates for the project.

__Colours__

Once the landing page carousel image was chosen, it was uploaded to the Coolers colour palette generator to develop the colour scheme.  This colour scheme was then applied to elements of the landing and booking pages.

![Coolors Palette](/documentation/screenshots/coolors-palette.png)

__Typography__

The Bootstrap landing page html links directly to the core CSS files. The font family holds several font names so it can act as a fall back system depending on the browser used.  The default font family applied for this website includes the following: 

font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Liberation Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";

__Images__

The office-related images chosen for the website aim to show that there is a wide variety of modern office space types available.  Workers can collaborate in open workspaces, meet in more private settings, and work alone in shared office spaces.  The location-based images show how these office spaces are located close to public transport links and restaurants.

## Features

### Existing Features

__Navigation Bar__

The navigation bar is present on all pages.  It remains at the top of the page at all times to allow the user to navigate easily around the site.

Along with being a marketing tool, the company logo serves as a home page link.

![Navigation Bar](/documentation/screenshots/logo.png)

All visitors both registered and unregistered are initially presented with an opportunity to register and login.  The Login button is highlighted in green so there is a clear call to action for registered users to login. The user status on the right side shows a logged-out status.

![Navigation Bar](/documentation/screenshots/logged-out-user.png)

The registered logged-in user is presented with an opportunity to visit the bookings page and logout.  The user status on the right side shows a logged-in status.

![Navigation Bar](/documentation/screenshots/logged-in-user.png)

The mobile view for the navigation bar shows a hamburger menu.

![Mobile Navigation Bar](/documentation/screenshots/mobile-navbar.png)

The dropdown changes depending on whether the user is logged in or logged out.

![Mobile Navigation Bar Logged Out](/documentation/screenshots/mobile-navbar-logged-out.png)

![Mobile Navigation Bar Logged In](/documentation/screenshots/mobile-navbar-logged-in.png)

__Footer__

The footer is present on all pages.  There is an opportunity presented here to call, email, or contact the company on social media platforms.

![Footer](/documentation/screenshots/footer.png)

__Carousel__

There are three slides in the carousel and all have a clear call to action for the user depending on the user's status.  

On slide one, the unregistered or logged-out visitor is presented with an opportunity to login.  The call to action button for login is green.  The user must enter their username and password to login.

![Carousel Slide One](/documentation/screenshots/carousel-slide-1.png)

If the user is unregistered the login page shows a link for the user to register.  

On slide two, all users regardless of their registration status are presented with an opportunity to have a look at the office spaces available.   The options call to action button is green in colour.

![Carousel Slide Two](/documentation/screenshots/carousel-slide-2.png)

If the user is unregistered or logged out the call to action button here will prompt the user to login.

![Logged Out Office Space Options](/documentation/screenshots/logged-out-office-options.png)

If the user is registered and logged in the call to action button here will prompt the user to visit the bookings page.

![Logged In Office Space Options](/documentation/screenshots/logged-in-office-options.png)

On slide three, all users regardless of their registration status are presented with an opportunity to have a look at the location details of the offices and the various transport and dining services close by.   The call to action button for location link is green.

![Carousel Slide Three](/documentation/screenshots/carousel-slide-3.png)

__User Authentication__

To make a booking on the site all users must register on the site.  The user must enter an email address, username, and password to register.

![User Registration](/documentation/screenshots/user-registration.png)

Once the user has registered, a message will confirm registration and logged-in status.

![User Registration Confirmation](/documentation/screenshots/user-registration-confirmation.png)

The navigation bar will also show the logged-in status of the user.

![Logged In User Status](/documentation/screenshots/logged-in-user-status.png)

To login at any time, the user will be prompted to enter a username and password.

![User Login](/documentation/screenshots/user-login.png)

Once the user has logged in, a message will confirm the logged-in status.

![User Login Confirmation](/documentation/screenshots/user-login-confirmation.png)

To logout, the user will be asked to confirm that they wish to logout.

![User Logout](/documentation/screenshots/user-logout.png)

Once the user has logged out, a message will confirm the logged-out status.

![User Logout](/documentation/screenshots/user-logout-confirmation.png)

The navigation bar will also show the logged-out status of the user.

![Logged Out User Status](/documentation/screenshots/logged-out-user-status.png)

__Bookings__

The user must be logged in to access the bookings page.  The page can be opened from the navigation bar.  It is also available on the green call to action button on slide one of the carousel and again if the logged-in user is viewing the office space options on the home page.

The bookings are presented in ascending date order.  There are options to add a booking, edit a booking and delete a booking on this page.  To add a booking the user clicks on the green plus sign beside the add a booking heading.  A booking can be edited by clicking on the pencil-square blue button beside the booking.  A booking can be deleted by clicking on the x-circle button beside the booking.

![Bookings Page](/documentation/screenshots/bookings-page.png)

On the add booking screen, the user must select the booking date and then choose the desk or meeting room they wish to book.  Only available desks and rooms will be shown on the dropdown list.  Multiple bookings are allowed for the same day as a user may wish to book both a desk and a meeting room on the same day.

![Add Booking Page](/documentation/screenshots/add-a-booking.png)

Once the booking is saved, a message will confirm the booking is added.

![Add Booking Confirmation](/documentation/screenshots/add-a-booking-confirmation.png)

When the user selects to edit a booking, they can select the new desk or office from the dropdown menu.  It is also possible to change the date on the booking along with the desk or office.  Once the date is selected, the database is checked for available desks and offices on the date.  The dropdown menu is only presented after this database check is completed.

![Edit Booking](/documentation/screenshots/edit-a-booking.png)

Once the booking is saved, a message will confirm the booking is updated.

![Edit Booking Confirmation](/documentation/screenshots/edit-a-booking-confirmation.png)

To delete a booking on the delete booking screen, the user must click on the confirm button.

![Delete Booking](/documentation/screenshots/delete-a-booking.png)

Once the booking is confirmed for deletion, a message will show that the booking is deleted.

![Delete Booking Confirmation](/documentation/screenshots/delete-a-booking-confirmation.png)


### Future Features

The following features will be delivered in future iterations of the project.

- An office manager capacity reporting tool for the office spaces.

- An office manager desk management front-end.  This would mean that it would be possible for the office manager to create, read, update and delete desks without using the admin panel.

- An office manager bookings management front end.  This involves enhancing the current user front end to handle the management of all user bookings.

- The end user would be able to manage their user profile including changing their password.

## Technologies Used

### Languages

- [Python](https://www.python.org/) 3.2 was used to develop the application backend.  The following are the python modules and packages used in the project:

  - asgiref==3.5.2
  - cloudinary==1.30.0
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2.16
  - django-allauth==0.51.0
  - django-crispy-forms==1.14.0
  - gunicorn==20.1.0
  - oauthlib==3.2.2
  - psycopg2==2.9.5
  - PyJWT==2.6.0
  - python3-openid==3.2.0
  - pytz==2022.6
  - requests-oauthlib==1.3.1
  - sqlparse==0.4.3

- [HTML5](https://html.spec.whatwg.org/multipage/) for front-end development.

- [CSS](https://www.w3.org/Style/CSS/) to style the HTML pages

- [JavaScript](https://www.javascript.com//) no was used to create custom dropdown menus in forms

### Frameworks

- [Django](https://docs.djangoproject.com/en/3.2/) v3.2.16
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) v4.6.2

### Database

- [SQLite](https://www.sqlite.org/index.html) for automated testing locally
- [PostgreSQL](https://www.postgresql.org/)from [ElephantSQL](https://www.elephantsql.com/) for live database

### Other

- [Heroku](https://www.heroku.com/) was used to host the deployed site
- [Cloudinary](https://cloudinary.com/) is hosting the static files
- [Gitpod](https://www.gitpod.io/) VS Code Browser as the IDE/Editor
- [Git](https://git-scm.com/) was used for version control 
- [GitHub](https://github.com/) is the repository for the code
- [Coverage](https://coverage.readthedocs.io/) was used to gauge the effectiveness of tests
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service(Jigsaw)](https://jigsaw.w3.org/css-validator/)
- [PEP8](https://www.python.org/dev/peps/pep-0008/) to validate Python
- [Coolors](https://coolors.co/) generate the colour palette used on the site
- [Balsamiq](https://balsamiq.com/) for developing the wireframes

## Testing

### Automated Testing
<details><summary>Details of automated testing with coverage of 91%.</summary>

To setup the local environment for testing, the following adjustment was made to the settings.py file

![Change settings.py](/documentation/screenshots/settings-py-for-testing.png) 

Also, the following was added to the env.py file:

![Change env.py](/documentation/screenshots/env-py-for-testing.png) 

When not testing, os.environ["DEVELOPMENT"] can be changed back to "False".

The coverage report for automated testing is as follows:

![Coverage Report](/documentation/screenshots/coverage-report.png) 

</details>

### Manual Testing
<details><summary>User Story Testing</summary>

Epic: Setup Site Administration to Manage Desks and Bookings 

To start testing, complete the following steps:
1. Go to the application web page on ** link
2. Select Login from the navigation bar
3. Login in as admin
4. Go to the application web page for the admin ** link

User Story: As a site administrator, I can CRUD desks so that I can manage site content <a href="https://github.com/teresabowe/booking-system/issues/3" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/3/hovercard">#3</a>

**Add a desk**

Testing procedure:
1. Click on the Add button beside Desks
2. Enter the Desk, Floor, and Description
3. Click on the SAVE button

![Add Booking](/documentation/screenshots/site-administration-desk-add.png) 

Expected Result: A new desk is created and is visible on the site administration desk list

Actual Result: A new desk is created and is visible on the site administration desk list

![Add Booking](/documentation/screenshots/site-administration-desk-add-list.png) 

Pass/Fail: Pass

**Update a desk**

Testing procedure:
1. Click on the Desk D3001 from the site administration desk list
2. Change the description from 'Window Desk on 3rd Floor' to 'Window Desk'
3. Click on the SAVE button

![Add Booking](/documentation/screenshots/site-administration-desk-update.png) 

Expected Result: The desk is updated and is visible with the new description on the site administration desk list

Actual Result: The desk is updated and is visible with the new description on the site administration desk list

![Add Booking List](/documentation/screenshots/site-administration-desk-update-list.png) 

Pass/Fail: Pass

**Delete a desk**

Testing procedure:
1. Click on the Desk D3001 from the site administration desk list
2. Click on Delete
3. Confirm deletion

![Delete Booking](/documentation/screenshots/site-administration-desk-delete.png) 
![Delete Booking Confirmation](/documentation/screenshots/site-administration-desk-delete-confirmation.png)

Actual Result: The desk is no longer visible on the site administration desk list

Expected Result: The desk is no longer visible on the site administration desk list

![Delete Booking List](/documentation/screenshots/site-administration-desk-delete-list.png)

Pass/Fail: Pass

**

User Story: As a site administrator, I can CRUD bookings so that manage my customer's needs <a href="https://github.com/teresabowe/booking-system/issues/4" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/4/hovercard">#4</a>

**Add a booking**

Testing procedure:
1. Click on the Add button beside bookings
2. Enter the Desk booking date, Desk, and Desk user
3. Click on the SAVE button

![Delete Booking List](/documentation/screenshots/site-administration-booking-add.png)

Expected Result: A new booking is created and is visible on the site administration desk list

Actual Result: A new booking is created and is visible on the site administration desk list

![Delete Booking List](/documentation/screenshots/site-administration-booking-add-list.png)

Pass/Fail: Pass

**Update a booking**

Testing procedure:
1. Click on the Desk D2004 for 22/12/2022 from the site administration bookings list
2. Change the Desk booking date from 22/12/2022 to 23/12/2022
3. Click on the SAVE button

![Update Booking](/documentation/screenshots/site-administration-booking-update.png)

Expected Result: The updated booking is updated and is visible on the site administration desk list

Actual Result: The updated booking is updated and is visible on the site administration desk list

![Update Booking List](/documentation/screenshots/site-administration-booking-update-list.png)

Pass/Fail: Pass

**Delete a booking**

Testing procedure:
1. Click on the Booking for Desk 2004 from the site administration bookings list
2. Click on Delete
3. Confirm deletion

![Delete Booking](/documentation/screenshots/site-administration-booking-delete.png)
![Delete Booking Confirm](/documentation/screenshots/site-administration-booking-delete-confirm.png)

Expected Result: The booking is no longer visible on the site administration bookings list

Actual Result: The booking is no longer visible on the site administration bookings list

![Delete Booking List](/documentation/screenshots/site-administration-booking-delete-list.png)

Pass/Fail: Pass

Epic: User Authentication

User Story: As a site visitor, I can register on the site so that I can access the site services <a href="https://github.com/teresabowe/booking-system/issues/6" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/6/hovercard">#6</a>

**Register**

Testing procedure:
1. Click on the Register button on the navigation bar
2. Enter the Email address, username, and password twice
3. Click on the Confirm button

Expected Result: 

1. A message is shown to indicate that a confirmation email is sent to the user  
2. A second message is shown to indicate that the newly registered user is also logged in to the site
3. The navigation bar shows the username of the logged-in user
4. The navigation bar Register link on the navigation bar has changed to Bookings
5. The navigation bar Login link on the navigation bar has changed to Logout

Actual Result: 

1. A message is shown to indicate that a confirmation email is sent to the user 
2. A second message is shown to indicate that the newly registered user is also logged in to the site
3. The navigation bar shows the username of the logged-in user
4. The navigation bar Register link on the navigation bar has changed to Bookings
5. The navigation bar Login link on the navigation bar has changed to Logout

Pass/Fail: Pass

User Story: As a registered user, I can login so that I have access to my content <a href="https://github.com/teresabowe/booking-system/issues/7" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/7/hovercard">#7</a>

**Login**

Testing procedure:
1. Click on the Login button on the navigation bar
2. Enter the username and password
3. Click on the Login button

Expected Result: 

1. A message is shown to indicate that the user has successfully signed in 
2. The navigation bar shows the username of the logged-in user
3. The navigation bar Register link on the navigation bar has changed to Bookings
4. The navigation bar Login link on the navigation bar has changed to Logout

Actual Result: 

1. A message is shown to indicate that the user has successfully signed in
2. The navigation bar shows the username of the logged-in user
3. The navigation bar Register link on the navigation bar has changed to Bookings
4. The navigation bar Login link on the navigation bar has changed to Logout

Pass/Fail: Pass

User Story: As a registered user, I can logout of my account so that my content is kept secure <a href="https://github.com/teresabowe/booking-system/issues/8" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/8/hovercard">#8</a>

**Logout**

Testing procedure:
1. Click on the Logout button on the navigation bar
2. Confirm logging out by clicking on the Logout button

Expected Result: 

1. A message is shown to indicate that the user has successfully logged out
2. The navigation bar shows that the user is logged out
3. The navigation bar bookings link on the navigation bar has changed to Register
4. The navigation bar Logout link has changed to Login

Actual Result: 

1. A message is shown to indicate that the user has successfully logged out
2. The navigation bar shows that the user is logged out
3. The navigation bar bookings link on the navigation bar has changed to Register
4. The navigation bar Logout link has changed to Login

Pass/Fail: Pass

Epic: Create Landing Page

User Story: As a site visitor, I can access the landing page so that I can understand the purpose of the site and take appropriate actions <a href="https://github.com/teresabowe/booking-system/issues/5" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/5/hovercard">#5</a>

Testing procedure:
1. Enter the URL for the booking application as https://deskbooking.herokuapp.com/

Expected Result: 

1. The landing page carousel slide 1 hero image text indicates that a workspace can be booked.  
2. A call to action on slide 1 invites the user to Login.  If the user is not registered then there is a link to register from the login page.
3. The landing page carousel slide 2 hero image text indicates that there are private offices and workspaces. 
4. A call to action on slide 2 invites the user to have a further look at the options available.  
5. The landing page carousel slide 3 hero image text and call to action invites the user to learn more about the location.

Actual Result: 

1. The landing page carousel slide 1 hero image text indicates that a workspace can be booked.  
2. A call to action on slide 1 invites the user to Login.  If the user is not registered then there is a link to register from the login page.
3. The landing page carousel slide 2 hero image text indicates that there are private offices and workspaces. 
4. A call to action on slide 2 invites the user to have a further look at the options available.  
5. The landing page carousel slide 3 hero image text and call to action invites the user to learn more about the location.

Pass/Fail: Pass

Epic: User Bookings Management

User Story: As a registered user I can create, read, update and delete my bookings so that I can maintain an accurate record of my use of the desk space (must-have/complete) <a href="https://github.com/teresabowe/booking-system/issues/9" data-hovercard-type="issue" data-hovercard-url="/teresabowe/booking-system/issues/9/hovercard">#9</a>

**Add Booking**

Testing procedure:
1. Select the Login link from the navigation bar
2. Select the Bookings link from the navigation bar
3. Click on the green plus icon beside "Add a Booking"
4. Select a desk booking date and desk
5. Click Save

Expected Result: 

1. A message indicating that the booking is added is shown 
2. The booking detail is now shown on the list of bookings

Actual Result: 

1. A message indicating that the booking is added is shown 
2. The booking detail is now shown on the list of bookings

![Registered User Booking Add](/documentation/screenshots/registered-user-booking-add.png)

Pass/Fail: Pass

**Add Booking**

Testing procedure:
1. Select the Login link from the navigation bar
2. Select the Bookings link from the navigation bar
3. Click on the Edit button which is a pencil-square blue button beside the booking
4. Update the desk booking date or the desk or both
5. Click Save

Expected Result: 

1. A message indicating that the booking is updated is shown 
2. The new booking detail is now shown on the list of bookings

Actual Result: 

1. A message indicating that the booking is updated is shown 
2. The new booking detail is now shown on the list of bookings

Pass/Fail: Pass

**Delete Booking**

Testing procedure:
1. Select the Login link from the navigation bar
2. Select the Bookings link from the navigation bar
3. Click on the Delete button which is a red x-circle button beside the booking
4. Click Confirm

Expected Result: 

1. A message indicating that the booking is deleted is shown 
2. The booking has now been removed from the list of bookings

Actual Result: 

1. A message indicating that the booking is deleted is shown 
2. The booking has now been removed from the list of bookings

Pass/Fail: Pass

</details>

<details><summary>Features Testing</summary>

**Home Page Company Logo**

- When clicked the company logo returns the user to the home page

Testing procedure:
1. From the Bookings page click on the company logo "SmithfieldSquare" on the navigation bar

Expected Result: 

1. The user is returned to the home page

Actual Result: 

1. The user is returned to the home page

Pass/Fail: Pass

**Footer Social Media Links**

- When clicked the social media links take the user to the correct sites

Testing procedure:
1. From the footer click on all of the social media links

Expected Result: 

1. The user is sent to the correct social media page

Actual Result: 

1. The user is sent to the correct social media page

Pass/Fail: Pass

**Footer Email Link**

- When clicked the email link opens a mailto link

Testing procedure:
1. From the footer click on the email address

Expected Result: 

1. The user is directed to the default mailto email provider or receives an "Add an Account" message if no default exists

Actual Result: 

1. The user is directed to the default mailto email provider or receives an "Add an Account" message if no default exists

Pass/Fail: Pass

**Footer Phone Link on Mobile**

- When clicked on a mobile phone the link suggests calling the number listed

Testing procedure:
1. From the footer click on the phone number

Expected Result: 

1. When clicked on a mobile phone the link suggests calling the number listed

Actual Result: 

1. When clicked on a mobile phone the link suggests calling the number listed

Pass/Fail: Pass
Note: This phone link is also available on a desktop.  While it is possible to disable it there may be some users who wish to call by using a phone app such as Meta WhatsApp or Microsoft Phone Link. This has not been tested to date.

**Add Booking Shows Available Desks Only**

- On Add Booking the dropdown menu for desks only shows available desks

Testing procedure:
1. Have a look at the bookings listed on the Bookings page 
2. Take note of a date and desk already booked
3. Click on the green plus icon beside "Add a Booking"
4. Choose the date observed above
5. Click on the Desk dropdown list

Expected Result: 

1. The dropdown list does not show the desk observed above as it is already booked on that date

Actual Result: 

1. The dropdown list does not show the desk observed above as it is already booked on that date

![Registered User Booking Add](/documentation/screenshots/registered-user-booking-list-check-dropdown.png)
![Registered User Booking Add](/documentation/screenshots/registered-user-booking-add-booking-check-dropdown.png)

Pass/Fail: Pass

**Update Booking Shows Available Desks Only**

- On Update Booking the dropdown menu for desks only shows available desks

Testing procedure:
1. Have a look at the bookings listed on the Bookings page 
2. Take note of a date and desk already booked
3. Click on the update button, the pencil-square blue button beside the booking
4. Choose the date observed above
5. Click on the Desk dropdown list

Expected Result: 

1. The dropdown list does not show the desk observed above as it is already booked on that date

Actual Result: 

1. The dropdown list does not show the desk observed above as it is already booked on that date

Pass/Fail: Pass

**Unregistered User Opens Bookings URL**

- An unregistered user is redirected to the Login URL when attempting to browse to the view_bookings URL

Testing procedure:
1. Enter the https://deskbooking.herokuapp.com/view_bookings URL 

Expected Result: 

1. The user is redirected to the Login page

Actual Result: 

1. The user is redirected to the Login page

Pass/Fail: Pass

**Unregistered User Opens an Invalid URL**

- Work in Progress

**Bad Email Address on Registration**

- When a bad Email address is entered the user is prompted to correct it 

Testing procedure:
1. Select Register from the navigation bar
2. Enter an incorrect Email address i.e. exclude the @ or . or both
3. Enter the username
4. Enter the password twice. It must contain at least 8 characters.  It must not be too common.
5. Click Register

Expected Result: 

1. The user is prompted to correct the email address
2. Registration is not completed until the correct format for the email address is entered

Actual Result: 

1. The user is prompted to correct the email address
2. Registration is not completed until the correct format for the email address is entered

Pass/Fail: Pass

**Bad Password on Registration**

- When a bad Email address is entered the user is prompted to correct it 

Testing procedure:
1. Select Register from the navigation bar
2. Enter a correct email address
3. Enter the username
4. Enter an incorrect password i.e. enter less than 8 characters
5. Click Register

Expected Result: 

1. The user is prompted to enter a password with at least 8 characters.
2. Registration is not completed until the correct format for the password is entered

Actual Result: 

1. The user is prompted to enter a password with at least 8 characters.
2. Registration is not completed until the correct format for the password is entered

Pass/Fail: Pass

</details>

<details><summary>Browser Compatibility</summary>

The site was developed using Google Chrome Version 108.0.5359.99 (Official Build) (64-bit).  It was also tested on Microsoft Edge Version 108.0.1462.46 (Official build) (64-bit) and Firefox Browser 107.0.1 (64-bit).  No issues were identified during this testing.

</details>

<details><summary>Responsiveness</summary>

The Chrome Developer Tool was used to check responsiveness as the application was being developed.

The following devices were also used to check responsiveness.

- iPhone 13, iOS Version 16.1.1
- Redmi Note 9, Android Version SP1A.210812.016
- HP Pavillion Laptop Windows 11 Home 21H2 with 15" screen and Acer KG271 27" monitor

As the development progressed, the main responsiveness issues were found with the bookings listings where the information presented forced a slide bar to be inserted on mobile devices.  While the slide bar allowed the user to move the view to the right, it wasn't delivering a professional product.  The solution was to merge two columns of data into one and rename the table titles.

</details>

### Validator Testing

### Bugs and Fixes

## Deployment

<details>
  <summary></summary>

</details>

<details>
  <summary></summary>
</details>

<details>
  <summary></summary>
</details>

<details>
  <summary></summary>
</details>

<details>
  <summary></summary>
</details>

<details>
  <summary></summary>
</details>

## Credits

- Implementing the LoginRequired mixin from [Django Software Foundation](<https://docs.djangoproject.com/en/3.0/topics/auth/default/#the-loginrequired-mixin>).
- Implementing a dependent dropdown list from [Simple is better than complex](<https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html>).  
- Catching an integrity error and showing a customised message from [Stack Overflow](<https://stackoverflow.com/questions/11293380/django-catching-integrity-error-and-showing-a-customized-message-using-template>).

### Content

- Text for workspaces is from [Condeco](<https://www.condecosoftware.com/blog/different-types-of-workspaces/>).
- Text for Dublin Smithfield location is from [Dublin.ie](<https://dublin.ie/live/life-in-dublin/dublin-neighbourhoods/>).
- Text for transport links is from [Dublin.ie](<https://dublin.ie/live/life-in-dublin/getting-around/>).
- Text for Eating and Drinking is from [All The Food](<https://www.allthefood.ie/single-post/2018/09/19/where-to-eat-and-drink-in-smithfieldnking>). 

### Media

__Images__
- [Carousel Image Slide 1](<https://pixabay.com/photos/pneumatic-desk-office-desk-6952958/>) created by reallywellmadedesks - Pixabay.
- [Carousel Image Slide 2](<https://pixabay.com/photos/conference-table-meeting-startup-593355/>) created by StartupStockPhotos - Pixabay.
- [Carousel Image Slide 3](<https://pixabay.com/photos/office-workspace-office-desk-6952950/>) created by reallywellmadedesks - Pixabay.
- [Office Space Image 1](<https://pixabay.com/photos/entrepreneur-startup-start-up-man-593361/>) created by StartupStockPhotos - Pixabay.
- [Office Space Image 1](<https://pixabay.com/photos/meeting-brainstorming-business-594091/>) created by StartupStockPhotos - Pixabay.
- [Office Space Image 1](<https://pixabay.com/photos/office-startup-tables-chairs-room-594119/>) created by StartupStockPhotos - Pixabay.
- [Luas Transport](<https://www.freeimages.com/photo/luas-dublin-4-1446434>) created by energy69 - Freeimages.
- [Whiskey Factory](<https://www.freeimages.com/photo/whiskey-factory-1-1622276>) created by porah - Freeimages.
- [Restaurant Sign](<https://unsplash.com/photos/w5nIrLaq4dg>) created by Naseem Buras - Unsplash.
- Logo image was created on the [Logo](https://logo.com/) website.  

__Icons__
- [Edit Icon](https://icons.getbootstrap.com/icons/pencil-square/) created by Bootstrap.
- [Delete Icon](https://icons.getbootstrap.com/icons/x-circle/) created Bootstrap.
- [Facebook](<https://fontawesome.com/v5/icons/facebook-f?s=solid&f=brands>) created by Font Awesome.
- [Twitter](<https://fontawesome.com/icons/twitter?s=solid&f=brands>) created by Font Awesome.
- [LinkedIn](<https://fontawesome.com/v5/icons/linkedin-in?s=solid&f=brands>) created by Font Awesome.
- [Instagram](<https://fontawesome.com/v5/icons/instagram?s=solid&f=brands>) created by Font Awesome.
