# **[Au Revoir Bistrot](#)**  French Restaurant

## **Overview**

Au Revoir Bistrot is a website for a fictional restaurant developed for lurning purposes. The restaurant is located in the center of Paris and offers classic French food.

Developed by Martin Fortuna

## **Project Goals**

As part of my journey as a student of Code Institute, the goal of this project is to demonstrate how I can apply my Bootstrap, Python & Django skills. I've built a fully friendly UX by not using the default built-in Django admin panel for the admin user.

## **User Goals**

-  Login, log-out, and sign-up feature.
-  CRUD feature for regular/admin users.
-  Ability to accept or deny bookings for admin users.
-  Contact Us Page.
-  Easy to read the menu.

## **Agile methodology**

The development phase was applied with Agile methodologies to deliver small features with efficiency and maintain hypothetical business value. User stories were prioritized according to the MoSCoW method to deliver the primarily needed functionalities first.

![Project Kanban](https://github.com/users/MartinFortuna/projects/6/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%2C%22Repository%22%5D)


### **User stories**

- A - As a developer I can correctly set up the basic project as in CI walkthrough so that all the basis is set to start development. 
- B - As a user, I can view the website on different devices so that I can access it anytime.
- C - As a user, I can register,login or logout  on the website so that I can access the  reservations feature.
- D - As a regular user, I can create, view or cancel my reservation so that I can change plans.
- E - As a user, I can choose to view, edit and delete my profile so that correct and erase my information.
- F - As an admin user, I can choose to accept or deny reservation requests so that I do not overbook my restaurant.
- G - As an admin user, I can view, edit or delete my customer list/profile so that manage the customers profiles.
- H - As a developer, I can avoid double bookings so that the restaurant is not spammed.
- I - As a user, I can view a simplistic menu so that I can easily understand the options.
- J - As a user, I can find opening hours and contact information so that I contact the restaurant within business hours.
- K - As a user, I can contact the restaurant by email so that I do not have to call. 
- L - As a developer, I can create a custom 404 page so that the customer has a link to return to the home page.
- M - As a user, I can leave a review so that I can share my experience. 


### **Story Points**

The current capacity is 20 story points per iteration.

- Iteration one : 

 User story ID | Story Point | MoSCoW categorization |
| ---------- |  -----------| ---------- |
| A | 2 | Must-Have |
| B | 2 | Must-Have |
| C | 2 | Must-Have |
| D | 2 | Must-Have |
| E | 2 | Must-Have|
| F | 2 | Must-Have |
| G | 2 | Should-Have |
| H | 0 | Won't-Have |
| I | 2 | Should-Have |
| J | 2 | Should-Have |
| K | 1 | Could-Have |
| L | 2 | Should-Have |
| M | 1 | Could-Have |

Scores:

- Must-Have: 12 story points
- Should-Have: 8 story points
- Could-Have: 2 story points
- Won't-Have: 0 story points


## **Design**

The website is fully responsive and designed with an easy access hamburger menu to make nagivation intuitive, the login button button will be replaced by a login icon so that the device stays reponsive on very small screens. 
As for the colors, I decided to use Bootstrap's dark background along with it's warning yellow across the website for consistency.

### App structure: 

- Non authenticated user Flow:

![Non authenticated user](docs/screenshots/Unauthenticateduser.png)

- Authenticated user Flow:

![Admin user authenticated](docs/screenshots/Adminauthenticated.png)

![Regular user authenticated](docs/screenshots/Regularuserauthenticated.png)


### Wireframes: 

|    Desktop   |    Tablet    |    Mobile    |
|    :----:    |     :----:   |    :----:    |
|[Home Page](docs/screenshots/hompageDesktop.png)|[Home Page](docs/screenshots/homepageIpad.png)|[Home Page](docs/screenshots/homepageMobile.png)|
|[Login](docs/screenshots/loginDesktop.png)|[Same as Desktop](docs/screenshots/loginDesktop.png)|[Same as Desktop](docs/screenshots/loginDesktop.png)|
|[Register](docs/screenshots/Sign-up.png)|[Same as Desktop](docs/screenshots/Sign-up.png)|[Same as Desktop](docs/screenshots/Sign-up.png)|
|[Menu](docs/screenshots/menuDesktop.png)|[Menu](docs/screenshots/menuIpad.png)|[Menu](docs/screenshots/menuMobile.png)|
|[Find us](docs/screenshots/findusDesktop.png)|[Find us](docs/screenshots/findusIpad.png)|[Find us](docs/screenshots/findusMobile.png)|
|[Booking Requests](docs/screenshots/bookingrequestsDesktop.png)|[Same as Desktop](docs//bookingrequestsDesktop.png)|[Same as Desktop](docs/screenshots/bookingrequestsDesktop.png)|
|[Customer List](docs/screenshots/customerlist.png)|[Same as Desktop](docs/screenshots/customerlist.png)|[Same as Desktop](docs/screenshots/customerlist.png)|
|[Profile](docs/screenshots/regularuserprofile.png)|[Same as Desktop](docs/screenshots/regularuserprofile.png)|[Same as Desktop](docs/screenshots/regularuserprofile.png)|
|[Book a table](docs/screenshots/bookatableDesktop.png)|[Same as Desktop](docs/screenshots/bookatableDesktop.png)|[Same as Desktop](docs/screenshots/bookatableDesktop.png)|
|[My Bookings](docs/screenshots/mybookindsDesktop.png)|[Same as Desktop](docs/screenshots/mybookindsDesktop.png)|[Same as Desktop](docs/screenshots/mybookindsDesktop.png)|













