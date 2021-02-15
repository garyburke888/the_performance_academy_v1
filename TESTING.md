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

## 3. Test Booking/Classes Page

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
Besides running through the extensive test cycles documented above the URL from the Heroku deployment was shared with friends, family and one currently running performing arts school. As a result, the following features were suggested / requested and could be implemented in future versions;
-   Ability to update quantity on side drawer bag.
-   Ability to click to view next/previous blog post from blog detail page.
-   Ability to actually add user profile images, so they show up in the Boards app for example.

# Django Testing
In total, 32 Django test were written and implemented - solely for the 'Articles' and 'Boards' apps. These tests are listed below.

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
-   Webhooks from Stripe not working, this is despite payments being sent to Stripe without issue. Many attempts to resolve this issue, including contacting CodeInstitute tutor support were made, to no avail. Error code - 405 (Method Not Allowed) remains.

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