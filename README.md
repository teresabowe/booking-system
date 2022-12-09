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

__Database Schema__

There are two custom models in the database schema, a desk model and a bookings model.  The desk model records all of the available desks and meeting rooms.  The bookings model handles the user bookings for the office spaces.  The django-allauth application manages the account registration and authentication so a custom model is not required in this instance.

![Entity Relationship Diagram](/documentation/screenshots/entity-relationship-diagram-bookings.png)

### Surface Design

The overall design aims to present a simple, clean website which demonstrates that the overall purpose is to book office space.  A carousel example template from Bootstrap 4.1 was used as the starting point for developing the templates for the project.

__Colours__

Once the landing page carousel image was chosen, it was uploaded to the Coolers colour palette generator to develop the colour scheme.  This colour scheme was then applied to elements of the landing and bookings pages.

![Coolors Palette](/documentation/screenshots/coolors-palette.png)

__Typography__

The Bootstrap landing page html links directly to the core CSS files. The font family holds several font names so it can act as a fall back system depending on the browser used.  The default font family applied for this website includes the following: 

font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Liberation Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";

__Images__

The office-related images chosen for the website aim to show that there is a wide variety of modern office space types available.  Workers can collaborate in open workspaces, meet in more private settings, and work alone in shared office spaces.  The location-based images show how these office spaces are located close to public transport links and restaurants.

## Features

### Existing Features


### Future Features


## Technologies Used

### Languages

- 

### Frameworks

- 

### Database

- 

### Other

- 

## Testing


### Features Testing

<details>
  <summary></summary>
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
