## Code Validation

### HTML
| File Name | File Path | Result | W3C | Comments | Corrected Issues |
|--|--|--|--|--|--|
| base.html | templates/restaurant/index.html + base.html + nav.html + footer.html | PASS | [link](docs/validation/Passbase.png) | See next link for corrected issues | [link](docs/validation/FailBase.png) |
| menu.html | templates/restaurant/menu.html | PASS | [link](docs/validation/Passmenu.png) | NA | NA |
| contact.html | templates/restaurant/contact.html | PASS | [link](docs/validation/Passcontact.png) | See next link for corrected issues | [link](docs/validation/FailContact.png) |
| loginuser.html | templates/restaurant/loginuser.html | PASS | [link](docs/validation/PassLogin.png) | See next link for corrected issues | [link](docs/validation/FailLogin.png) |
| register.html | templates/restaurant/resgister.html | PASS | [link](docs/validation/Pass%20Register.png) | See next link for corrected issues | [link](docs/validation/FailRegister.png) |
| booklist.html | templates/restaurant/resgister.html | PASS | [link](docs/validation/Booklist.png) | NA | NA |
| booking.html | templates/restaurant/booking.html | PASS | [link](docs/validation/PassBooking.png) | NA | NA |
| edituser.html | templates/restaurant/edituser.html | Pass | [link](docs/validation/PassEditUser.png) | See next link for corrected issues | [link](docs/validation/FailEditUser.png) |
| userlist.html | templates/restaurant/userlist.html | Pass | [link](docs/validation/PassUserlist.png) | See next link for corrected issues | [link](docs/validation/FailUserlist.png) |
| userprofile.html | templates/restaurant/userprofile.html | Pass | [link](docs/validation/PassUserProfile.png) | See next link for corrected issues | [link](docs/validation/FailUserProfile.png) |
| 404.html | templates/restaurant/404.html | Pass | [link](docs/validation/Pass404.png) | NA | NA |

### Python

| File Name | File Path | Result | PEP8 |
|--|--|--|--|
| apps.py | mrwrestaurant/admin.py | PASS | [link](docs/validation/app.py.png) |
| forms.py | mrwrestaurant/forms.py | PASS | [link](docs/validation/form.py.png) |
| models.py | mrwrestaurant/models.py | PASS | [link](docs/validation/models.py.png) |
| urls.py | mrwrestaurant/urls.py | PASS | [link](docs/validation/urls.py.png) |
| views.py | mrwrestaurant/admin.py | PASS | [link](docs/validation/views.py.png) |


### Javascript

| File Name | File Path | Result | JsHint |
|--|--|--|--|
| index.js | static/js/index.js | PASS | [link](docs/validation/index.js.png) |
| index.js | templates/restaurant/contact.html | PASS | [link](docs/validation/contact.html.png) |


### CSS

| File Name | File Path | Result | JsHint |
|--|--|--|--|
| style.css | static/css/style.css | PASS | [link](docs/validation/style.css.png) |


## Responsiveness

The website was designed to be fully responsive from the screenwidth 280px above.

| **Browser Tested** | **Actual Result** | **Pass/Fail** |
| ------------------ | ----------------- | ------------- |
| Chrome             | As Expected       | Pass          |
| Firefox            | As Expected       | Pass          |
| Edge               | As Expected       | Pass          |
| Mac OS Safari      | As Expected       | Pass          |
| Safari             | As Expected       | Pass          |


| **Devices Tested** | **Actual Result** | **Pass/Fail** |
|-------------------|-------------------|---------------|
| Iphone SE        | As Expected       | Pass          |
| Iphone XR   | As Expected       | Pass          |
| Iphone 12 pro     | As Expected       | Pass          |
| Pixel 5  | As Expected       | Pass          |
| Samsung Note 20   | As Expected       | Pass          |
| Samsung S21+      | As Expected       | Pass          |
| Samsung Tab S7+   | As Expected       | Pass          |
| iPhone 13 Pro Max | As Expected       | Pass          |
| iPhone 11         | As Expected       | Pass          |
| iPad Pro 12 inch  | As Expected       | Pass          |
| iPad Pro Air       | As Expected       | Pass          |
| Galaxy Fold | As Expected       | Pass          |
| Iphone 5 | As Expected       | Pass          |


### Lighthouse

I've only included lighthouse results for mobile and desktop for the home page as all other pages have above 90% scores.

<details><summary>Results</summary>

- Home Page Desktop

![Lighthouse Desktop](/docs/screenshots/HomepagescoreDesktop.png)

- Home Page Mobile

![Lighthouse Mobile](/docs/screenshots/HomepageMobile.png)



</details>


## Manual User Story Testing

- All requirements for User Stories were met, tested, and behaved as expected before they were marked as done.

- Full CRUD functionality implemented for regular users, they can create, view and delete bookings.
- Regular users can view, edit and delete their profiles.
- Super users can view, edit and delete customer profiles but cannot delete their own profiles.
- Super users can accept or deny bookings.


### Manual testing completed on existing functionalities: 

<details><summary></summary>

|               | Feature Tested      | Expected Result                                                               | Actual Result | Pass/Fail |
| ------------ | ------------------- | ----------------------------------------------------------------------------- | ------------- | --------- |
| Nav Bar      | Responsiveness | Behaves consistently across a wide range of browsers and devices.                | As Expected   | Pass      |
|              | Non-authenticated user      | Only shows menu, contact, and home page to unauthenticated users               | As Expected   | Pass      |
|              | Authenticated admin user         | Only shows booking requests and customer list once authenticated              | As Expected   | Pass      |
|              | Authenticated regular user       | Only shows profile, book a table, and my bookings pages.                          | As Expected   | Pass      |
|              | Logout button       | Login and register button is replaced with logout once the user is authenticated, when pressed the user is redirected to the home page | As Expected   | Pass      |
|              | Username reflected | Username is reflected in nav bar once user is authenticated                    | As Expected   | Pass      |
|              | Hamburger menu       | Hamburger menu across all devices width                                    | As Expected   | Pass      |
|              | Redirect link for logo and title         | Redirects user to home page.                                    | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Index  page   | Responsive Image and text   | Behaves consistently across wide range of browers and devices         | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Menu  page        | Responsive  text   | Behaves consistently across wide range of browers and devices                      | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Contact page  | Responsiveness   | Behaves consistently across wide range of browsers and devices          | As Expected   | Pass      |
|              | Email form | User cannot submit an empty form, users receive an alert once the form is submitted                  | As Expected   | Pass      |
|              | Email form | Admin user correctly received emails.                  | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Profile page  | Shows user info    | Shows username, full name, email and join date                                 | As Expected   | Pass      |
|              | Edit button    | User can view, and edit profile, changes are informed instantly.                                             | As Expected   | Pass      |
|              | Delete          | User can delete the profile and is redirected to log in, user cannot log in with the deleted profile, a new profile is necessary | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Book a table page | Make a reservation  | Users can make a reservation with date and time with a minimum of 1 guest    | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|My bookings page | View reservation  | Users view reservation details ans status(pending, accepted or denied)    | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Booking requests page| Accept or deny bookings  | Admin users can view, accept or deny booking requests, reservation status is updated accordingly    | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Customer list page | Edit or delete  | Admin users can view, edit or delete customer profiles but not their own.   | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|Footer | Responsivess  | Behaves consistently across wide range of browers and devices    | As Expected   | Pass      |
| | Social media links  | Redirect customer to a new page when clicked upon    | As Expected   | Pass      |
|              |       |        |    |      |
|              |       |        |    |      |
|404 page | Any unknown url  | Custom 404 page is displayed with link to home page    | As Expected   | Pass      |

</details>

### Security and authentication

<details><summary></summary>

- If the user is unauthenticated and knows the URL and tries to access restricted information: 

|               | Feature Tested      | Expected Result                                                               | Actual Result | Pass/Fail |
| ------------ | ------------------- | ----------------------------------------------------------------------------- | ------------- | --------- |
| Non authenticated users      | Customer list or profile page  | Non authenticated users are redirected to login page               | As Expected   | Pass      |
|       | Booking requests page  | Users are presented with a server error 500              | As Expected   | Pass      |
|       | Booking page  | Users are presented with a server error 500              | As Expected   | Pass      |
|       | My bookings | Users are presented with a server error 500              | As Expected   | Pass      |


- If the regular user is authenticated and knows the URL and tries to access restricted information: 

|               | Feature Tested      | Expected Result                                                               | Actual Result | Pass/Fail |
| ------------ | ------------------- | ----------------------------------------------------------------------------- | ------------- | --------- |
| Regular authenticated users      | Customer list   | Users are redirected to their own profile               | As Expected   | Pass      |
|       | Booking requests page  | Users are redirected to My Bookings page              | As Expected   | Pass      |
|       | Booking page  | Users are presented with a server error 500              | As Expected   | Pass      |

</details>


## Bugs

|        Bug       | Issue     | Solution  |
| ------------ | ------------------- | ----------------------------------------------------------------------------- | 
| Deployment Bug      | Installed fontawesome was creating issues with Cloudinary  | Removal of Cloudinary from installed apps and requirements.txt              |
| Email form      | Emails were being sent without validation, I tried adding an event listener with prevent.Default() to stop page reload on form submission but addEvenListener was not being recognized in the index.js file. | Due to the page lifecycle I had to insert the event listener via a script tag into the contact.html page, this solved the bug.           | 








