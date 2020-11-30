# Timely-Care Website

---

### Contents:

 - [Description](#description)
 - [UX](#ux)
 - [Features](#features)
 - [Technologies Used](#technologies-used)
 - [Testing](#testing)
 - [Deployment](#deployment)
 - [Credits](#credits)
---

## Description

For the 3rd project I have created a website for a buissness idea which I came up with and is not yet an actual buissness, the name is unique and inspiration was taken from a relative who is studying to be a hairdresser and I thought about a home visit hari and beauty service which they could use once they have their qualification. 

If this was representing a functioning buissness it would be useful as it would allow customers who are unfit medically or elderly who would usually have difficulties travelling outside their homes to get their haircut or makeup/nails done. they can search through the variety of services available to them and book at a convenient time/place for them. Recently due to the new social disctances measures of covid this could be even more useful with hairdressers becoming overcrowded and some people unwilling to travel this provides a great alternative as we are still allowed maxium 6 persons in a house. Also proffesionals can get in touch to request work from the contact form.

---

## UX

---

As this website is potentially designed for elderly customers the UX is very simple and easy to navigate with consistent themes and forms throughout and only a few different links to make it as simple as possible for elderly people to use. However it is also full of colourful pictures and bright backgrounds to keep it easy on the eyes. 

User stories:
 - I am an eldery lady who cannot travel far from home and am in need of a cut and blow dry.
 - I am planning my own wedding and want to have a proffesional style my hair and do my makeup on my wedding day as well as my bridesmaids but need them to travel to the destination of my wedding.
 - I am a proffesional looking for freelance work which is flexible around my normal work hours to earn extra money.
 - I recently injured my leg and am unable to visit a hairdresser but as I am not able to move from bed for a long time my hair needs a cut and wash.

---

## Features

### Existing Features

 - Contact form is implemented to allow users to reach out with any questions they have about our services and for proffesionals to contact us about working freelance for us.
 - A list of all the available services are viewable to customers with Prices.
 - There is a admin login and registration function.
 - Ability for admins to view/edit/delete services directly from the website.
 - Admins can view their schedules to see all of their appointments including customer details, time and place.

### Feaatures left to impend

 - Customers are unable to pay for their services through the website as I have not covered this detail instead using this current website payments would need to be made at the appointment, however this is definetly something which should be added if this were to be used in the real world
 - The Footer is very basic but as Timely-Care has no socials I have only left social Icons rather than Social links in the Footer.
 - Correct details for the address and phone number I created an email so that the contact form would function but the address and phone number is fictional.
 - As it were to create a new user the Website owner would require a software developer to add one, I did not want to leave a register form in the website as this would be unsafe because anyone could create a user and alter the website.
 - A functioning profile page for the admin is not properly completed and must be completed in the future.
---

## Technologies Used

 - JQuerry - The project uses JQuerry to simplify DOM manipulation.
 - mail.js - The project uses mail.js for a fully functioning contact form.
 - Flask - The project uses flask app to render templates, login functionality and session.
 - JSON - This was used to simplify data storage in js.
 - bson.objectid - This was used to aid in the edit/add/remove functions for services.
 - Boostrap4 - Used to add icons, buttons, format contact forms, responsive web design and background colours.
 - Mongodb - This is where all of the data collections are stored for users, services, and bookings.
 - Pymongo - This was used to help read the data from Mongodb in the python script run.py.
 - werkzeug.security - This was used to ensure secure passwords are developed when creating a new admin user.

---

## Testing

Contact form: - Go to the "Contact Us" page.
              - Try to submit the empty form and verify that an error message about the required fields appears.
              - Try to submit the form with an invalid email address and verify that a relevant error message appears.
              - Try to submit the form with an invalid email address and verify that a relevant error message appears.
              - Try to submit the form with all inputs valid and verify that a success message appears.

Booking form: - Go to the "Booking" page.
              - Try to submit the empty form and verify that an error message about the required fields appears.
              - Try to submit the form with an invalid Service and verify that a relevant error message appears.
              - Try to submit the form with an invalid only empty time or date that a relevant error message appears.
              - Try to submit the form with all inputs valid and verify that a success message appears.

Register User: - Add register.html to navbar.
     - Go to register.html
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with an invalid password and verify that a relevant error message appears.
     - Type valid username and password.
     - Click 'Add user' - If success you would be taken to the index.html page and session=user would be in session, if not various errors could happen.
     - To fix any errors check run.py and links in the register form from register.html and try again.

Login User: - Add admin_login.html to navbar.
     - Go to admin_login.html.
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with an invalid password or username and verify that a relevant error message appears.
     - Type username and password created from register.html.
     - Click 'Login' - If success you would be taken to the index.html page and session=user would be in session, if not various errors could happen.
     - To fix any errors check run.py and links in the register form from register.html and try again.

Schedule: - Add services.html to navbar (view only if session.user active).
     - Create a booking through the booking.html page
     - Login using the admin_login.html page
     - Go to schedule.html and see if the booking shows up.

Add Services: - Login as a admin.
     - Go to 'Edit Services' page 
     - Click 'Add new service'
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with valid only one field empty and verify that a relevant error message appears.
     - Try to submit the form with valid fields and verify that the new service appears under the 'Services' Page.

Edit Services: - Login as a admin.
     - Go to 'Edit Services' page 
     - Click 'Edit service' on a existing card
     - Try to submit the form with empty fields and verify that a relevant error message appears.
     - Try to submit the form with valid only one field empty and verify that a relevant error message appears.
     - Try to submit the form with valid fields and verify that the edited service appears under the 'Services' Page.

Delete Services: - Login as a admin.
     - Go to 'Edit Services' page 
     - Click 'Delete service' on a existing card.
     - Verify that the deleted service no longer appears under the 'Services' Page.
---

## Deployment

The website was written in gitpod and deployed through github repositories using regular git commits from the command terminal in gitpod. It is run using Flask

There is no differences between the deployed version and deployment version.

---

## Credits

### content:
 - All information in the site is completely original and no text is copied, prices for services were taken as an average from many other hairdressers and beauty shops from existing knowledge.

### media:
 - https://colorlib.com/wp/free-booking-form-templates/
 - https://codepen.io/salahuddin/pen/LOmWpg
 - https://colorlib.com/wp/template/login-form-v1/
 - https://wordpress.org/plugins/admin-custom-login/
 - https://colorlib.com/wp/free-html5-contact-form-templates/
 - https://getbootstrap.com/docs/4.0/components/forms/
 - https://gijgo.com/datetimepicker/configuration/datepicker
 - https://mdbootstrap.com/docs/jquery/javascript/collapse/
 - images from free stockpile.
