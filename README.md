<h1 align="center">Milestone Project 4 - The Hangar</h1>

[Click here to view the live project :link:](https://the-hangar.herokuapp.com/)

The Hangar is a project for an Aircraft Model Store e-commerce website. This e-commerce website was built to all the Aviation lovers, pilots and mechanics that wish to push their dreams to a next level and buy a real flying Aircraft Miniature Model. As a quote widely attributed to da Vinci say "Once you have tasted flight, you will forever walk the earth with your eyes turned skyward, for there you have been, and there you will always long to return."

# Table Of Contents

1. [User Experience (UX)](#user-experience)
    - [User stories](#user-stories)
    - [Design](#design)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4.  [Languages Used](#languages-used)
5.  [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
6.  [Database](#database)
7.  [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Additional Testing](#additional-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
8. [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Stripe and Database](#stripe-and-database)
    - [GitHub](#github-pages)
9. [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

# User Experience

The main intention of this e-commerce store is to be easy for non-computer savy users and users with no web experience to navigate. The website returns a simplistic but realistic design and experience, focusing on what is important: The Aircraft Models.

-   ## User stories

    -   ### First Time Visitor Goals
        1. As a First Time user,  I want to access the website and know what it offers.
        2. As a First Time user, I want to to easily navigate through the website and register my account.
        3. As a First Time user, I want to check all the products section to see all the products the website has to offer.
        4. As a First Time user, I want to filter the products per categories or per types to check the exact types of Aircraft models I am interested in.
        5. As a First Time user, I want to quickly and easily access my current cart to check all the products I have added, their quantity and their price.
        6. As a First Time user, I want to quickly and easily update my current cart by changing the products quantity or deleting a product I don't want anymore.


    -   ### Returning Visitor Goals
        1. As a Returning user, I want to check and sort the aircraft models by their price and see which products are within my budget.
        2. As a Returning user, I want to already use my registered account to login back to the website.
        3. As a Returning user, I want to easily and quickly use the safe checkout method with my previous saved information.
        4. As a Returning user, I want to check my favorite aircraft model types.
    
    - ### Frequent Visitor Goals
        1. As a Frequent user, I want to login back to my account with all the previous information from the last purchases added.
        2. As a Frequent user, I want to quickly view all products in the page and see if there is any new product added.
        3. As a Frequent user, I want to see how much I need to add on my cart in order to not pay shipping.
        4. As a Frequent user, I want to quickly add products to the cart and return to the webstore to add more products to the cart.
        5. As a Frequent user, I want to be able to leave the website but still have my purchase information and cart information saved, so I can return to the cart and still have my products added there.

-   ## Design
    -   ### Colour Scheme

        - I choose and used neutral colors to not deviate the attention from the products. With the white body and the black navigation bar the products page creates a color contrast as the Aircraft Models in different colors grab the attention of the customer.

        - The main colors used were: Black [#000000] and White [#FFFFFF]

    -   ### Typography

        - The font that I choose for the project was the Oxygen font imported from Google Fonts. This font was chosen due to the easy readability and I thought that the font matched in a nice way in what the website had to offer.

        - The font was imported from [Google Fonts](https://fonts.google.com/)

# Features

- **Main top nav bar** - Where users can surf the website and view all category, types, and all the products of the website using the same navigation option.

- **Sort field** - Users can sort all the products by price, name and category by selecting their sort options in the field.

- **Collapsible nav bar** - To help users navigate the website in smaller screens.

- **Quantity update option** - Before and after Users add the product to the cart they can select the product quantity they would like to buy.

- **Toasts messages** - Toasts messages to help maintain the user informed of the actions he has taken or actions that he still is taking while using the website.

- **Session cookie user** - Saves a session cookie so Users don't need to keep login in every time they re-open the website and also keeps their cart information and cart products saved on the cookie in case they need to stop in the middle of the product hunt to do something else.

- **Delivery Information Save** - User can save his delivery information if he wants to purchase new products in the future using the same info.

- **Order History** - Under the user profile page he can check and view information about all his past orders.

# Technologies Used

A brief overview of the languages, frameworks, and other tools I've used on this project:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - Semantic markup language as the shell of the site.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - Cascading Style Sheets as the design of the site.

- [Bootstrap:](https://getbootstrap.com/)
    - Loaded Bootstrap to provide all its pre-built classes, grid and classes functions.

- [JavaScript](https://www.javascript.com)
   - Used to add interactivity to the site.

- [Python](https://pt.wikipedia.org/wiki/Python)
    - Used to build the backend and render the pages.

- [Django](https://www.djangoproject.com/)
    - Django was the backend framework used to handle all backend processes such as interactions with the database, authentication and rendering of HTML templates.

# Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://pt.wikipedia.org/wiki/JavaScript)
-   [Python](https://pt.wikipedia.org/wiki/Python)

# Frameworks Libraries and Programs Used

1. [Bootstrap:](https://getbootstrap.com/)
    - Loaded Bootstrap to provide all its pre-built classes, grid and classes functions.

2. [JavaScript Validator](https://jshint.com)
    - Used to check and validate all JavaScript code to check for any typos or errors.

3. [Google Fonts](https://fonts.google.com/)
    - Google fonts was used to import the Oxygen font.

4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

5. [GitHub](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.

6. [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - Used for testing and fixing website bugs. Also used Google Lighthouse for performance testing.

7. [Google Icons](https://google.github.io/material-design-icons/#icon-font-for-the-web)
    - Google Icons was used on the site to improve visual design.

8. [JQuery](https://jquery.com/)
    - DOM manipulation to initiate the interactive functions from Materialize.

9. [Heroku](https://www.heroku.com/)
    - Enabling this project to be build, run, and operate entirely in the cloud.

10. [Stripe](https://stripe.com/en-ie)
    -  NoSQL database used for the project.

11. [Postgre](https://www.postgresql.org/)
    - PostgreSQL was the database used to store all the models in Heroku on the production environment.

12. [Gitpod](https://www.gitpod.io/)
    - Was the online IDE used to developed the entire project and to push changes and production to GitHub and Heroku.

13. [Markdown](https://pt.wikipedia.org/wiki/Markdown)
    - Was used for this README and to create the table of contents and code blocks.

14. [Fontawesome](https://fontawesome.com/)
    - Was used on the entire website to provide a better UX/UI through the site.

15. [SQLite](https://www.sqlite.org/)
    - The Django SQlite database was used as the database in the development environment

# Testing

- The website was tested in Google Chrome, Microsoft Edge, Mozilla Firefox, both on Windows and Mac OS.

- Through the Console device toolbar it was also tested using the following emulated devices: Moto G4, Galaxy S5, Pixel 2, iPhone 5/SE iPhone 6/7/8, iPhone X, iPad, iPad Pro, Surface Duo.

- Used [Am I Responsive](http://ami.responsivedesign.is/#) for testing different viewports and a [Mockup Generator](http://techsini.com/multi-mockup/index.php) 

- The W3C Markup Validator and W3C CSS Validator Services:

    - [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - Validated all pages HTML by direct input.

    - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - No errors were found.

    - [Web Formatter](https://webformatter.com/) - Was also used for checking for any errors in HTML and CSS.

    - [JavaScript Validator](https://jshint.com) - No errors were found.

    - [PEP8 online check](http://pep8online.com/) - Succesfully passed through the PEP8 validator.

    - [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) - Used to check general performance of the website.

## Database

- Throughout the development of the project I was using  Using Django SQL database SQLite and in Heroku I have used a PostgreSQL database for deployment.

### Product App

`Product` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Product id | id | primary_key=True | AutoField
|Category|category|null=True, blank=True, on_delete=models.SET_NULL|ForeignKey
|Type|type|null=True, blank=True, on_delete=models.SET_NULL|ForeignKey
|Manufacturer|manufacturer|null=True, blank=True, on_delete=models.SET_NULL|ForeignKey
|Name | name | max_length=30 | CharField
|Description | content | blank=False | TextField
|Price | price | max_digits=20, decimal_places=2 | DecimalField
|Image URL| image_url| max_length=1024, null=True, blank=True | URLField
|Image | image | null=True, blank=True | ImageField

`Category` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Category id | id | primary_key=True | AutoField
|Name | name | max_length=50 | CharField
|Friendly Name | friendly_name | max_length=50, null=False, blank=False | CharField

`Manufacturer` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Manufacturer id | id | primary_key=True | AutoField
|Name | name | max_length=50, null=False, blank=False | CharField
|Country | country | max_length=50, null=False, blank=False | CharField

`Type` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Type id | id | primary_key=True | AutoField
|Name | name | max_length=50, null=False, blank=False | CharField
|Friendly Name | friendly_name | max_length=254, null=False, blank=False | CharField
|Thrust | thrust | max_length=30 | CharField


### Checkout App

`Order` model

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order id | id | primary_key=True | AutoField
|Order Number | order_number | max_length=32, null=False, editable=False | CharField
|Full Name | full_name | max_length=50, null=False, blank=False | CharField
|User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True | ForeignKey
|Email | email | max_length=254, null=False, blank=False | EmailField
|Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
|Country | country | null=False, blank=False | CountryField
|Postcode | postcode | max_length=20, null=True, blank=True | CharField
|City | town_or_city | max_length=40, null=False, blank=False | AutoField
|Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
|Street Address 2 | street_address2 | max_length=80, null=False, blank=False | CharField
|County | county | max_length=80, null=True, blank=True | CharField
|Date | date | auto_now_add=True | DateTimeField
|Delivery Cost | delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
|Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Grand Total | grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
|Original Cart | original_cart | null=False, blank=False, default='' | TextField
|Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order id | id | primary_key=True | AutoField
|Order | order | null=False, blank=False, on_delete=models.CASCADE | ForeignKey
|Product | product | null=False, blank=False, on_delete=models.CASCADE | ForeignKey
|Quantity | quantity | null=False, blank=False | IntegerField
|Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

### Profile App

| Name | Database Key | Validation | Field Type|
| :-------------: |:----------------:| :--------------: | :---------: |
|Order id | id | primary_key=True | AutoField
|Order | user | on_delete=models.CASCADE | OneToOneField
|Order | default_phone_number | max_length=20, null=True, blank=True | CharField
|Order | default_country | null=True, blank=True | CountryField
|Order | default_postcode | max_length=20, null=True, blank=True | CharField
|Order | default_town_or_city | max_length=40, null=True, blank=True | CharField
|Order | default_street_address1 | max_length=80, null=True, blank=True | CharField
|Order | default_street_address2 | max_length=80, null=True, blank=True | CharField
|Order | default_county | max_length=80, null=True, blank=True | CharField

## Testing User Stories

-   ### First Time Visitor Goals
    1. As a first time user, entering the site I know by the landing page and by vieweing the "All Products" section that the website sells Aircraft Models.
    2. As a first time user, I can navigate via the top navigation menu to view and filter the products and to also register my account.
    3. As a first time user, I can see the all the products in the website by going to the "All products" section via the top nav bar.
    4. As a first time user, I can filter all the products by their categories or Aircraft types via the top navigation bar to check the products I am most interested in.
    5. As a first time user, I can check my current cart by clicking on the Cart icon on the top menu and check the products I have added with the quantity and price.
    6. As a first time user, I can quickly and easily update my cart information by decreasing/increasing the products quantity and then clicking update or by removing a product I don't want it anymore.

-   ### Returning Visitor Goals
    1. As a returning user, I can check and sort the Aircraft Models by their price by using the Sort Field and selecting the Price sorting options.
    2. As a returning user, I can login back with my registered account from previous sessions.
    3. As a returning user, I can go through the checkout process with my previous information saved there.
    4. As a returning user, I can check my favorite Aircraft Models types by filtering the types I like the most via the top navigation menu.

-   ### Frequent Visitor Goals
    1. As a frequent user, I can login back to my account with all my previous information from past purchases added there and also with the order history.
    2. As a frequent user, I can quickly view all the products by going to "All Products" on the top navigation menu and seeing all the Aircraft Models current in the store.
    3. As a frequent user, I can see a banner message informing if I will have to pay the shipping price with the current cart and products I have added in the cart.
    4. As a frequent user, I can quickly add the products to my cart and return to the store using the "Back to the store" button to view and add any more products to the cart.
    5. As a frequent user, I can leave the website and when I return my session is saved and I can return to vieweing the website and the products without having to login back again and without having to re-add my products to the cart.

## Additional Testing

    All testing performed via the app deployed to Heroku (on the-hangar.herokuapp.com)

-   ### Testing index.html page:

    1. When clicking "Click here to Access" I am succesfully redirected to the webstore page.

    2. Tested that the hero image of the hangar is responsive to the screen size.

-   ### Testing the Products App:

    #### products.html page:
    1. On the /products/ page tested the Sort by option with: Price Ascending, Price Descending, Category Ascending, Category Descending, Name (A-Z), Name (Z-A) and made sure the sorting is working correctly for each sorte option.
    
    2. Tested the "Back to top" Button to make sure it is working.
    
    3. Tested the "Edit" and "Delete" buttons under the products to make sure they are working correctly.

    4. Tested the redirect to the product details page when we click on the product image.

    5. When clicking on the products tags we then filter the products to show all the same tags.

    6. Made sure that the success toast alert appears when a product is added to the cart.

    7. Made sure that all information being picked up from the database is showing correctly on the page.

    8. Made sure that only admins can view the edit and delete button and no unintended user can modify the product by modifying the page URL.

    #### product_detail.html page:

    1. Tested the "Edit" and "Delete" buttons to make sure they are working correctly.

    2. Tested the Increase and Decrease buttons to make sure they were working properly and that the quantity was updating accordingly.

    3. Tested both buttons "Keep Shopping" (Redirects back to /products/ page) and "Add to Cart"(add product to cart) to make sure they are working properly.

    4. Made sure that only admins can view the edit and delete button and no unintended user can modify the product by modifying the page URL.

    #### add_product.html page:

    1. Made sure that while on the adding product management page users can choose the correct selectors for Caregoty, Type and Manufacturer from the database.

    2. Tested both buttons "Cancel" (returns to products page) and "Add product" (to add the product to the database)

    3. Tested adding a test product and made sure the image and all the fiels were created correctly on the database.

    4. Tested the "noimage.jpg" to make sure if a product is added without an image the noimage.jpg appears.

    #### edit_product.html page:

    1. Tested that while clicking on the "Edit" button the user is redirected to the /product/edit/# page and the product information populates the forms.

    2. Tested both buttons "Cancel" (returns to products page) and "Update product" to certify they are working properly and updating the product information.

    3. Tested the toasts alert to make sure they appear to indicate that you are editing a product and also a toast success appears when you have succesfully updated the product.

-   ### Testing the Cart App and also cart.html page :

    1. Tested the Increase/Decrease button and then the "Update" button to make sure the product quantity is changing accordingly as well as the total price.

    2. While Increasing/Decreasing the product quantity and clicking "Update" the Success toast should appear to inform the product quantity was updated accordinly.

    3. Tested the "Remove" button and to confirm the product is removed from the cart.

    4. Tested both the "Keep Shopping" and "Proceed to Checkout" buttons to make sure they are working.

    5. While adding a product under €100 made sure that the yellow banner informing about the free delivery is appearing.

    6. Made sure that all the information is showing correctly like product name, price, quantity, subtotal and grand total.

    6. Made sure that the session cookie is working and that it keeps saved the products inside the cart even if you close and re-open the page.

-   ### Testing checkout app and also checkout.html and checkout_success.html page:

    1. Made sure when clicking on the "Modify Cart" you get back to your cart.

    2. Tested that when you are logged in the form is populated with the User information correctly.

    3. Made sure the order summary displays correctly all the information (product name, quantity and price)

    4. Tested purchasing a product and made sure the order was created succesfully in Stripe.

    5. While clicking on "Complete order" made sure the order was completed and redirected to the checkout_success.html page

    6. On the checkout_success.html page made sure all the order information was displaying correctly and that the success toast pops to confirm the order was processed.

    7. On the checkout_success.html page tested the "Back to store" button to make sure it redirects back to the /products/ page.

    8. Made sure after the order is succesfull that the order now displays in the Order History under the My Profile page.

    9. Tested the webhooks for payment intent succeed and payment intent failed.

    10. Made sure that when the "Save this delivery information to my profile" information is selected the information is indeed saved to the user profile.

-   ### Testing profiles app and profile.html page:
    1. Tested the "Update Information" button to make sure the information is updated correctly on the database.

    2. made sure the Order History is showing all the past order accordingly.

    3. When clicking on the Order History ID made sure the past order details appears and a toast alert pops in to inform the user is viewing a past confirmation order.

-   ### Testing toasts and main-nav.html and mobile-header.html pages:
    1. Tested all the toasts information (error, info, success and warning) throug the website to make sure they are appearing accordingly.

    2. On the toast_success.html made sure the button "View your Cart" shows correctly and redirects to the cart page.

    3. While selecting a product under €100 made sure the yellow bar advising about the free shipping fee appears.

-   ### Testing main navigation and collapsible bar:

    1. On the main top navigation bar tested all the links to make sure they are working properly and also the filters.

    2. On the main top navigation bar tested the Cart and Account icongs to make sure they are working. And while checking the account it is displaying the account options correctly.

    3. Made sure that only admins the product Management option.

    4. Tested the search bar to make sure it is working properly and the page is updating with the correct search query.

    5. On the collapsible bar made sure that all links are working properly.

    6. On the the collapsible bar made sure that the Search, Cart, and My Account are working as expected and that the total cart price is also updated.

## Bugs and Fixes

1. After adding the search functionality every time I was searching for anything it was displaying all the products.
	- 1.1 **Fix:** The indendation of both lines (lines followed below) was wrong. I have to remove one indendation level: 
    ```
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    ```

2. After adding the search functionality for product types the server was running fine and not showing any error, but everytime I selecting the product type like "Jets" on the navbar it wasn't showing anything.
    - 2.1 **Fix:** I have to add a Friendly name to models.py so while selecting the type on navbar would retrieve the type name all in lowercase and show the friendly name with the first letter capitalized.

3. While trying to setup webhook I got a few 401 errors while trying to send a test event to a webhook endpoint. While investigating it better I have found out that this error was related to an Unauthorized request.
    - 3.1 **Fix:** The 8000 port was set to private and while checking Slack I have found out that the 8000 port must be set to public. After changing the 8000 port to public I was still getting a 401 error and this time was due to the URL added in stripe not containing the 8000 port on the URL (https://8000-coffee-mongoose-wi4a85v2.ws-eu18.gitpod.io/checkout/wh/).

4. After I deleted a product on Django Admin panel to perform a test the entire website started returning a 404 with the error message `RelatedObjectDoesNotExist at /admin/login/`
    - 4.1 **Fix:** After trying several times to close and start the python server and also shutting off and opening again the workspace on gitpod I found that the issue was with the session cookies. After clearing all the cookies I manage to see the website again without the products that I have deleted.

5. After deploying to Heroku I was trying to access the Postgres database to create Superuser but it was only accessing the SQLite database.
    - 4.1 **Fix:** After checking with Tutor Support he informed I forgot to add the DATABASE_URL to gitpod vars.

6. After deploying to Amazon S3 bucket the images were not showing.
    - 4.1 **Fix:** After a very detailed check I have found that instead of using `/media/` the images in Amazon S3 bucket were set to /static/media/. After I updated the URL the images appeared again.

# Deployment

## Heroku

The project was deployed on [Heroku](the-hangar.herokuapp.com), the following steps were taken:

1. Created a requirements.txt file by typing: `pip3 freeze --local > requirements.txt` in the terminal.
2. Created a procfile.
3. Logged in to Heroku.
4. Pressed the button "new" and then "create new app".
5. Chose an app name and a region and pressed create app.
6. Went to deployment section.
7. Under deployment method pressed Github.
8. Chose the right repository in the list, pressed search and then connect.
9. Pressed enable automatic deploys under automatic deploys.
10. Click on the find more addons button.
11. Click on the Heroku Postgres button.
12. Click on install Heroku Postgres.
13. Went to settings.
14. Added all the config vars needed for the project.
15. Pressed open app.

## Stripe and Database

The first step after forking or cloning the project would be to install all dependencies needed by the system.
If the project is opened in GitPod the command in the terminal would be: `pip3 install -r requirements.txt`.
If working locally setting up a virtual environment first and after that running the `pip3 install -r requirements.txt` command.

In order for the project to work in a product environment a PostgreSQL database would need to be set up, this process might differ depending upon how you choose to deploy the site but on Heroku you would:
1. Log in to Heroku.
2. From the dashboard click the link to the app.
3. Go to resources.
4. Click on the find more addons button.
5. Click on the Heroku Postgres button.
6. Click on install Heroku Postgres.
7. Choose the Hobby dev free plan and choose your app in the list.
8. Press submit form.

If your using another way of hosting the project include an environment variable called "DATABASE_URL" which only exists in the production environment and create the connection to the database in this section in the settings.py file: if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }

In order for the payment and order system to work a Stripe account needs to be created, with these steps:

1. Go to https://dashboard.stripe.com/register.
2. Enter all details and press create account.
3. Confirm your email address by following the link.
4. Create an account by pressing the top left account button.
5. Write name and press create account.
6. Navigate to developers/webhooks.
7. Click on add endpoint.
8. Enter the base URL of your website plus "/payments/confirmation/" in the URL field.
9. Choose checkout.session.completed in events to send and press add endpoint.
10. Go to developers/webhooks and click on the webhook.
11. Get the webhook signing secret by clicking click to reveal.
12. Get your Stripe API keys from developers/Stripe API
13 Store your webhook signing secret in the variable STRIPE_ENDPOINT_SECRET in settings.py.
14. Store your Stripe API secret_key in the variable STRIPE_TEST_SECRET_KEY in settings.py.
15. Add your publishable key as a string argument to the const stripe = Stripe() object in payments.js

Preferably hide your STRIPE_ENDPOINT_SECRET and STRIPE_TEST_SECRET_KEY values in environment variables if the project is to be publicly displayed.
The same goes for the rest of the settings that needs to be added to setting.py: 

SECRET_KEY : a secret key used to hash passwords etc.
EMAIL_HOST_USER : Gmail account you want to send mails from..
EMAIL_HOST_PASSWORD = App password which can be acquired by setting up two step verification and creating an app password for your Google account
DEFAULT_FROM_EMAIL = same Gmail account.

In development add an environment variable called DEVELOPMENT to use the development database.

## GitHub Pages 

**Under the repository page:**

    1. Click on Settings 
    2. Scroll down to the "GitHub Pages" section 
    3. Select the Source Branch 
    4. Click Save.

- For this project, I have used the cloud-based IDE [Gitpod](https://gitpod.io/) and [GitHub](http://github.com/) as a free git repository hosting.

    1. I started the project by creating a new Repository on GitHub and loading the [Code Institute Gitpod Template](https://github.com/Code-Institute-Org/gitpod-full-template).

    2. Installed the [Gitpod extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) and on my GitHub repo I clicked on the Gitpod button to create a new Master Workspace on GitPod.

    3. After creating the workspace I developed the website using Gitpod and pushing my commits to GitHub using the following commands:
        - `git add "file-name"` - To add a file for staging.
        - `git commit -m "description-of-update"` - To commit.
        - `git push` - To push my commits to GitHub
        - I have also used extra git commands such as: 
        - `python3 -m http.server` - To run a preview of the website on the browser.
        - `git status` - To display the current state of the working directory and the staging area.

## Running locally

1. Go tho this [project repository](https://github.com/MatSim91/Milestone-Project-4-The-Hangar) in GitHub while signed in in your own GitHub account.
2. Click on the dropdown menu Code option.
3. Click on "Open with GitHub Desktop" to clone and open the repository locally.
4. Click on the "Choose" option and navigate to the local path where you want the cloned repository to be.
5. Click "Clone".

- [Click here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories) for more cloning GitHub options.

# Credits

- [Code Institute Course](https://codeinstitute.net/) helping on setuping up the e-commerce store.

- [Font Awesome](https://fontawesome.com/icons) for the huge collection of free icons they offer.

- [Web Formatter](https://webformatter.com/) Used for formatting HTML, CSS and Javascript and also to check for errors.

- [Google Fonts:](https://fonts.google.com/) Thanks to Google for providing this huge amount of free fonts on the site.

- [Bootstrap](https://getbootstrap.com) for the large and free libraries 

- [Pixabay](https://pixabay.com/images/search/hangar/) - Thanks to Pixabay for providing the awesome hero image of The Hangar

## Content

-  The  details and descriptions of the products were taken from [Wikipedia](https://www.wikipedia.org/) and from [Revell](https://www.revell.de/).

## Media

-  The media for the Aircraft Products was taken from a website that sell Aircraft Models: [Revell](https://www.revell.de/).

## Acknowledgements

- My mentor Akshat for all his help and ideas.

- Thanks to the tutors at Code Institute for all help during the course (Especial thanks to Scott for all his help).

- Slack channel help regarding ongoingissues and problem solving ideas.