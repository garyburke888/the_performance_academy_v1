# Introduction
-   All links have been manually tested.
-   Pylint used for static code analysis throughout build.

All the following tests have been implemented and passed. Where errors occured this has been highlighted.

# Manual Test Cycles

## 1. Test Navbar

### General Functionalities
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click every nav item.
4.  Ensure all links work correctly for classes.

### Logged in and non-logged in users see different options
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Check if navbar contains the following;
    -   Logo (with homepage link)
    -   Classes links
    -   Blog link
    -   Boards link
    -   Account icon
    -   Bag icon
    -   Search bar and/or icon
4.  Click account icon and login.
5.  Check the account icon dropdown list and check the following are present;
    -   Add class (for admin only)
    -   Post to blog (for admin only)
    -   My Profile
    -   Log Out

## 2. Test Landing Page
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Check that Classes page is opened by clicking the 'Find a Class' button.

## 3. Test Classes Page

### Class Categories
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Click all sorting options.
5.  Toggle the sort through all options and check that sorting works accordingly;
    -   Age
    -   Price
    -   Name
    -   Category

### Get Class Details
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
6.  New page should open.
7.  Page should contain the following;
    -   Image
    -   Title
    -   Age
    -   Descripton
    -   Teacher
    -   Price
    -   Term length
    -   Category badge(s)
    -   Day preference dropdown (if applicable)
    -   Add to bag button
    -   Keep shopping button
    -   Quantity field

### Test search Function
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Type 'ballet' into the search box and press enter.
4.  All ballet classes should display on the classes page, and nothing else.
5.  Type 'guitar' into the search bar and press enter.
6.  'Guitar' and 'Bass Guitar' classes should display on the classes page.

## 4. Test Shopping Bag

### Check empty bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on bag icon.
4.  Bookings page should open.
5.  Placeholder 'You have no bookings' should be displayed.
6.  'Look again' button link should appear and take you back to all classes.

### Add item to bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Chosen class should be inside the bag view.

### Open Fullpage bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Fullpage bag should open.

### Add two items to bag and check position/order of contents
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Continue shopping by clicking 'x' button at the top.
8.  Bag should close.
9.  Choose another class.
10. Add item to bag.
11. Side drawer bag should open and last added item should be on top.

### Checkout from side drawer bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Click 'secure checkout' button on page.
9.  Checkout page should open.

### Increase quantity in fullpage bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Should be redirected to fullpage bag.
9.  Press '+' button.
10. Click update.
11. Side drawer bag should open and quantity increased by one.

### Decrease quantity in fullpage bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Should be redirected to fullpage bag.
9.  Press '-' button.
10. Click update.
11. Side drawer bag should open and quantity decreased by one.

### Remove item(s) in fullpage bag
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Should be redirected to fullpage bag.
9.  Click remove.
10. Side drawer bag will open and item should be removed from bag (if multiple class categories were in bag).
11. Booking page (empty) should open (if only 1 class category was in bag)

## 5. Checkout

### Checkout anonymous user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click on 'Find a Class'.
4.  Choose any class by clicking the image.
5.  Add item to bag.
6.  Side drawer bag should open.
7.  Click 'go to secure checkout' button on bag.
8.  Should be redirected to fullpage bag.
9.  Click 'secure checkout'.
10. Should be redirected to checkout page.
11. Form for address details & 'Order Summary' should be displayed.
12. Fill in form & use test credit card (4242 4242 4242 4242...)
13. Complete order.
14. Loading animation should be displayed.
15. Checkout success page should be shown.
16. If real email address was used, confirmation email should be recieved.

### Checkout registered user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click account icon and login with user details.
4.  Click on 'Find a Class'.
5.  Choose any class by clicking the image.
6.  Add item to bag.
7.  Side drawer bag should open.
8.  Click 'go to secure checkout' button on bag.
9.  Should be redirected to fullpage bag.
10. Click 'secure checkout'.
11. Should be redirected to checkout page.
12. Form for address details should be prefilled & 'Order Summary' should be displayed.
13. Add test credit card (4242 4242 4242 4242...)
14. Complete order.
15. Loading animation should be displayed.
16. Checkout success page should be shown.
17. If real email address was used, confirmation email should be recieved.

### Discount - correct application
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click account icon and login with user details.
4.  Click on 'Find a Class'.
5.  Choose any class by clicking the image.
6.  Add item to bag.
7.  Side drawer bag should open.
8.  Bag should contain the message 'Add 1 more class to get a 10% discount!'
9.  Close bag and add another item.
10. Side drawer bag should open and not contain discount message.

### Discount - correct amount
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click account icon and login with user details.
4.  Click on 'Find a Class'.
5.  Choose any class by clicking the image.
6.  Add item to bag.
7.  Choose another class and add to bag. (make sure you have at least two items in the bag, as the discount applies to bookings of more than one class).
8.  Grand total should contain a discount of 10%, no matter what classes you have in it.

## 6. Register

### Register
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click Account icon.
4.  Choose 'Register'.
5.  Fill out the form.
6.  Check if confirmation mail was received.
7.  Confirm email.
8.  Login with credentials.

## 7. Registered Users: Useraccount
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Click Account icon.
4.  Select Login.
5.  Should see form.
6.  Enter username and password.
7.  Redirected to home page.

## 8. Site Management

### Class Management
-   Create Class
-   Read Class
-   Update Class
-   Delete Class

### Profile Management
-   Create Profile
-   Read Profile
-   Update Profile
-   Delete Profile

### Blog Management
-   Create Article
-   Read Article
-   Update Article
-   Delete Article

### Boards Management
-   Create Board
-   Read Board
-   Update Board
-   Delete Board

## 9. Blog

### View blog
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Blog' from the main menu.
4.  Blog articles should be visible.
5.  Click 'read more' on any article.
6.  Blog detail page should open.
7.  Full article should be displayed.
8.  Click 'back to blog' button.
9.  Should be taken to main blog page.

## 10. Boards

### View Boards, Topics & Posts
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Boards' from the main menu.
4.  List of boards (in table) should be visible.
5.  Click the title on any Board.
6.  Board page should open, featuring all topics on that board.
7.  Click the title of any Topic.
8.  Topic page should open, featuring all the posts on that topic, in descending chronological order.
9.  Click 'back to all topics' button.
10. Should be taken back to the previous topics page.
11. Click 'back to all boards' button.
12. Should be taken to the main Boards page.

### Post new topic - anonymous user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Boards' from the main menu.
4.  List of boards (in table) should be visible.
5.  Click the title on any Board.
6.  Board page should open, featuring all topics on that board.
7.  Click 'new topic' button.
8.  Should be redirected to login page.

### Post new topic - registered user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Boards' from the main menu.
4.  List of boards (in table) should be visible.
5.  Click the title on any Board.
6.  Board page should open, featuring all topics on that board.
7.  Click 'new topic' button.
8.  New topic page with form should open up.
9.  Enter subject and message, click 'post'.
10. Should be redirected to that topics page.

### Reply to a post topic - anonymous user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Boards' from the main menu.
4.  List of boards (in table) should be visible.
5.  Click the title on any Board.
6.  Board page should open, featuring all topics on that board.
7.  Click the title of any Topic.
8.  Topic page should open, featuring all topics on that topic.
9.  Click 'reply' button.
10. Should be redirected to login page.

### Reply to a post topic - registered user
1.  Open web browser.
2.  Open [The Performance Academy Page](https://the-performance-academy.herokuapp.com/).
3.  Choose 'Boards' from the main menu.
4.  List of boards (in table) should be visible.
5.  Click the title on any Board.
6.  Board page should open, featuring all topics on that board.
7.  Click the title of any Topic.
8.  Topic page should open, featuring all topics on that topic.
9.  Click 'reply' button.
10. Reply page with form should open.
11. Enter message and click 'post a reply'.
12. Should be redirected to that topics page, with all replies visible.

# User Testing

## Testing User Stories from User Experience (UX) Section

### Browsing the Site
As a **site visitor**, I want to...
-   access the site on any device (smartphone, tablet, desktop), so that I am able to visit the site anytime and anywhere.
    -   The following actual devices / device sizes were used for testing the real-world responsiveness; iPhone 7 Plus (Phone), Dell Inspiron 15 (Laptop), Mac Mini, with acer K222HQL monitor (Desktop). Chrome dev tools were used to test tablet screens. Cross browser testing was also attempted on Chrome, Opera, Edge, Firefox and Safari, site works as expected on all.
-   have easy navigation, to quickly solve the reason for my visit.
    -   Main nav is apparant from landing on the site, clear text with dropdowns and Bootstrap info-styled buttons throughout.
-   have information about the brand, to get to know the classes and understand what they entail.
    -   The homepage explains in very few words what the site is, a school that offers classes. Each class then contins more detailed information. The Blog also provides information to users interested in the school and performing arts in general.

### Browsing Classes
As a **site visitor**, I want to...
-   browse classes by category and type, so that I can quickly find what I am looking for.
    -   Class categories are linked directly form the dropdown menu, under classes and class types are actually used as the main nav items themselves.
-   sort classes to adjust the order according to my needs.
    -   Full sorting capabilities are available on the classes page which includes age (youngest-oldest/oldest-youngest), price (low-high/high-low), name (a-z/z-a) or category (a-z/z-a).
-   be able to to search for specific classes, to quickley find what I need.
    -   Users can search directly form the main nav on all screen sizes, the search function will search class titles and descriptions.
-   access class details, to get more information on the class.
    -   Each class card on the classes page features a link to full 'class details'.
-   be able to choose a class, to book according to my needs.
    -   Each class detail page features an 'add to bag' button to allow users to quickley add that item to their bag.
-   read information about performaing arts in general, with a view to exploring new classes / styles.
    -   The site features a Blog, which contains relevant articles as posted by the school admin. It also features Boards which are moderated by admin but are for users to chat to each other, about performing arts related topics.

### Manage Shopping Bag and Make Booking
As a **site visitor**, I want to...
-   see all my items in a shopping bag, so that I have an overview of my potential booking.
    -   When a user adds an item to their bag, a side drawer opens up with a summary of contents, which a user can click and it will take them to the full bag page. This page can also be accessed at any time by the bag icon in the main nav.
-   be able to reduce / increase quantity, so that I can order my prefered amount.
    -   Each class detail page features a quantity form field which can be adjusted to their needs, this also is a feature of the shopping bag page.
-   be able to remove an item from my cart, so that I can manage my shopping bag efficiently.
    -   The shopping bag contains a quick 'remove' link which allows this action.
-   be able to checkout from the cart view, so that I can quickly finish my booking.
    -   The shopping bag page has a 'secure checkout' button link which accomplishes this.
-   be able to pay for a booking by credit card, so that I don't have to deal with an invoice and money transfer.
    -   This site only accepts credit card payments currently, which is filled out on the checkout page.
-   receive a booking confirmation, so that I know my booking was completed.
    -   Booking confirmation emails are sent on checkout success - [checkout/views.py](checkout/views.py)

As a **registered user**, I want to..
-   store my details in my profile, so that I can quickly finish my booking.
    -   If a user is logged in a 'Save this billing information to my profile' checkbox is provided on the checout form, which will save the users billing information to their profile.

### Registration & Useraccount
As a **site visitor**, I want to...
-   be able to sign up to the site, so that I can track bookings and have my data prefilled in the order form.
    -   A standard account icon is used in the main nav as a dropdown to allow new users to 'register'. This takes the user to the sign-up page where the must enter a username, password and email address, and then they will be sent an email asking them to confirm their email address.

As a **registered user**, I want to...
-   be able to login, so that I can access my useraccount.
    -   From the account dropdown icon in the main nav, registered users can click the login link and will be taken to the login page and can login using their username and password.
-   be able to see my order history, so that I know what bookings I've made before.
    -   A registered users order history is available to view on their profile page.
-   manage my personal details, so that I can quickly update my data if something changes.
    -   A registered users billing details can be edited and saved on their progfile page.
-   post new topics and/or replies to the boards section of the site.
    -   You must be a registered user to create a topic or post a reply on a topic in the 'Boards' app. Users will be asked to login/register if they try to do either without registering/logging in.

### Site Management
As a **site owner**, I want to...
-   be able to manage the classes, categories, price and availability, so that I have an overview of all class details.
    -   The 'account' dropdown menu item will display 'add class' and 'post to blog' links for admin only. Edit & delete links will display on class_detail pages for admin only. Edit & delete links will also display on Blog articles for admin only.
-   view customer conversations & comments, so that I can quickly update the site when required.
    -   The 'Boards' app allows users / customers to chat and post about anything - which in turn is moderated and overseen by admin.
-   create, edit or delete articles to post in the blog, for site users to read.
    -   Only admin can post new articles to the Blog, which can be done via a link on the 'account' dropdown main nav item. Edit & delete links appear on each blog_detail page for admin only.
-   create, edit or delete boards, topics and posts in the boards app to maintain proper moderation.
    -   Admin retain full moderation over the 'Boards' app with regards to having the sole ability to delete topics & posts deemed inappropriate. Creating/editing/deleting boards is done by admin through the Django administration site.

Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends, family and one currently running performing arts school. As a result, the following features were suggested / requested and could be implemented in future versions;
-   Ability to update quantity on side drawer bag.
-   Ability to click to view next/previous blog post from blog detail page.
-   Ability to actually add user profile images, so they show up in the Boards app for example.

# Django Testing
In total, 32 passing Django tests were written and implemented - solely for the 'Articles' and 'Boards' apps. These tests are listed below.

## Articles App
-   [Forms](articles/test_forms.py)
-   [Models](articles/test_models.py)
-   [Views](articles/test_views.py)

## Boards App
-   [Boards View](boards/test_boards_view.py)
-   [Edit Post View](boards/test_edit_post_view.py)
-   [New Topic View](boards/test_new_topic_view.py)
-   [Posts View](boards/test_posts_view.py)
-   [Reply Posts View](boards/test_reply_topic_view.py)
-   [Topics View](boards/test_topics_view.py)

# Known Bugs
Webhooks from Stripe are not working, this is despite payments being sent to Stripe without issue. Many attempts to resolve this issue, including contacting Code Institute tutor support were made, to no avail. Error code - 405 (Method Not Allowed) remains.

# Development Issues
-   An attempt was made to use [AWS](https://aws.amazon.com/) to serve static and media files and though this started out successfully, data limits were somehow reached after only 3 days of hosting (under the free plan) and so it was decided to roll back and try another method to serve these files. WhiteNoise is used instead.
-   Midway through development I had to reset migrations because of a change I wanted to make to the database setup and this was done using the following steps;
    1.  ```python3 manage.py makemigrations```
    2.  ```python3 manage.py migrate --fake classes zero (for classes app)```
    3.  ```python3 manage.py showmigrations```
    4.  ```Delete everything from migrations folder apart from __init__.py```
    5.  ```python3 manage.py showmigrations```
    6.  ```python3 manage.py makemigrations```
    7.  ```python3 manage.py migrate --fake-initial```
    8.  ```python3 manage.py showmigrations```

# Code Validators

## [W3C HTML validator](https://validator.w3.org/)
Used to validate HTML code. The following non-critical errors were found;
-   Error: Bad value icon for attribute type on element link: Subtype missing.
-   Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.)
-   Error: Duplicate ID user-options.
-   Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.)
-   Warning: The type attribute is unnecessary for JavaScript resources.
-   Error: The aria-labelledby attribute must point to an element in the same document.

## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
Used to validate CSS code. The following non-critical errors were found, as well as various non-critical warnings.
-   abbr[data-original-title], abbr[title] - Property text-decoration-skip-ink doesn't exist : none
-   .toast - Property backdrop-filter doesn't exist : blur(10px)

## [Pylint](https://www.pylint.org/)
Used to analyse and validate Python code during development.

## [JSLint](https://jslint.com)
All .js files were checked. No issues were found on the JSON files. The stripe_elements .js file was requested to use double quotes instead of single quotes. The countryfield .js file had same request with some undeclared '$' and unexpected 'this' also.

## [Flake8](https://flake8.pycqa.org/en/latest/)
All .py files were checked using Flake8 in the terminal. There are still several 'null=True' and 'line too long' issues, but nothing critical.

# Site UI/UX & Browser Compatibility Testing
-   The following devices / device sizes were used for testing the responsiveness:
    -   iPhone 7 Plus (Phone)
    -   Dell Inspiron 15 (Laptop)
    -   Mac Mini, with acer K222HQL monitor (Desktop)
-   Chrome dev tools were used to review responsivness on multiple devices;
    -   Moto G4
    -   Galaxy S5
    -   Pixel 2/2 XL
    -   iPhone 5/5E/6/7/8/8+/X
    -   iPad/Pro
    -   Surface Duo
    -   Galaxy Fold
-   Cross browser testing was also attempted on Chrome, Opera, Edge, Firefox and Safari, site works as expected on all.
-   Chrome Lighthouse report results [here](media/tpa_measure.pdf)