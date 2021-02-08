# The Performance Academy
![The Performance Academy Responsive Design](/static/images/erisk_multi.png)

[View the live site here.](http://flask-risk-manager-project.herokuapp.com/)

**The Performance Academy** is an eCommerce website for a performing arts school that offers different types of classes for all ages. The site allows users to search for classes, book and pay (via Stripe) for them and register for an account.

## User Experience (UX)

### User stories
-   #### Viewing & Navigation
    1. As a customer, I want to see a list of classes so that I can choose the one(s) I want.
    2. As a customer, I want to view more details about a class, such as the description, price, day/time availabilit and teacher so that I can better understand what the class has to offer.
    3. As a customer, I want to be offered a discount for spending more money so that I can feel like I'm getting something extra.
    4. As a customer, I want to see the contents of my shopping bag at any point so that I can keep track of what I'm spending.
-   #### Registration & User Accounts
    1. As a site user, I want to register for an account so that I can view/edit my user profile and personal information.
    2. As a site user, I want to login/logout with ease, so that I can access my account quickly.
    3. As a site user, I want to reset my password if need be, so that I can keep my account secure.
    4. As a site user, I want to receive a confirmation email when I register.
-   #### Sorting & Searching
    1. As a customer, I want to sort the list of available classes so that I can easily identify classes that suit my needs.
    2. As a customer, I want to search for classes or key words so that I can esasily find the class I want.
    3. As a customer, I want to see different categories so that I can find what's available in my style.
-   #### Purchasing & Checkout
    1. As a customer, I want to request my day preference for a specific class so that I can fit it into my own schedule.
    2. As a customer, I want to view the classes in my bag at any given time so that I can identify the total cost of my booking and what exactly I am booking.
    3. As a customer, I want to adjust the quantity of individual items in my bag so that I can make changes before I checkout.
    4. As a customer, I want to easily enter my billing and payment information so that I can checkout quickly.
    5. As a customer, I want to see a success message and order summary after I checkout so that I can verify that I haven't made any mistakes.
    6. As a customer, I want to recieve and email confirmation after I checkout so that I can save it for future reference.
-   #### Community
    1. As a site user, I want to view the schools blog so that I can read interesting articles about the performing arts.
    2. As a site user, I want to join discussions with other users on the schools forum so that I can be part of a like-minded community.
-   #### Admin & Site Management
    1. As the site owner, I want to add a class so that I can offer new classes to customers.
    2. As the site owner, I want to edit/update a current class so that I can keep the class list up-to-date.
    3. As the site owner, I want to delete a class, so that I can remove classes that are no longer running.
    4. As the site owner, I want to write blog posts and make them availble for site users to read.
    5. As the site owner, I want to moderate the forum and have control over users and user posts.

### Design
-   #### Colour Scheme
    -   The site uses a dark theme, mainly black backgrounds and white text, making use of Bootstrap info style buttons.
-   #### Typography
    -   Roboto 2.0 is used across the site.
-   #### Imagery
    -   The site features one main image on the homepage and each class has its own representitive image, which shows the class title on hover.
    -   Site images are stored...

### Wireframes
Here are the designs I made for the site:
-   [Index page on desktop](/media/tpa_wf1.jpg)
-   [Classes page on desktop](/media/tpa_wf2.jpg)
-   [Index, Classes and Class Detail pages on smartphones](/media/tpa_wf3.jpg)
-   [Shopping Bag popup, Checkout and Checkout Success pages on smartphones](/media/tpa_wf4.jpg)
-   [Blog, Boards and Profile pages on smartphones](/media/tpa_wf5.jpg)
-   [Board Posts and Board Reply/Add page on tablets](/media/tpa_wf6.jpg)
-   [Add/Edit Class and Sign Out pages on tablets](/media/tpa_wf7.jpg)
-   [DB Entity Relationship Diagram](/media/erd_tpa.jpg)

## Features

### Visible to all users
-   **Index page** - Upon entering the site the user is greeted by the main nav, a discount banner, a large performing arts background image, a 'New Term Now Enroling' statement and a call-to-action button.
-   **Main Nav Menu** - The main menu (collapsed on mobile devices) features dropdown lists where the user can select classes and categories as follows;
    -   Classes by age, price, category or all classes.
    -   Singing classes in the following categories: Rock/Pop, Opera/Classical, Musical Theatre or all singing.
    -   Dancing classes in the following categories: Ballet, Hip Hop, Tap, Ballroom, Musical Theatre or all dancing.
    -   Acting classes in the following categories: Stage, Screen, Improv, Musical Theatre or all acting.
    -   Instrument classes in the following categories: Piano, Guitar, Bass Guitar, Drums, Ukulele or all instruments.
-   **Mian Nav Search Box** - Always visible. Searches class names and descriptions using Django models object 'Q' to handle the users query in the database.
-   **Main Nav Account** - Always visible dropdown menu to register or login.
-   **Main Nav Shopping Bag** - Always visible link to the session users shopping bag, which also contains the current total cost of items in the bag.
-   **Discount Banner** - Always visible to remind users they can recieve a discount by booking more than 1 class.
-   **Classes page** - This is main page of the site which features a list of available classes displayed in bootstrap cards. The list of classes can be sorted directly from the 'sort by...' dropdown which includes age (youngest-oldest/oldest-youngest), price (low-high/high-low), name (a-z/z-a) or category (a-z/z-a). When a user selects a certain category or group of categories ('All Singing' for example) from the main menu, all classes in that category / those categories will be listed on the classes page, with an array of bootstrap badges displaying on top which are also quick links to categories themselves. Click on the image of any class to see further details about that class.
-   **Class Detail page** - The class detail page contains more information about a given class, such as a full description, the teacher, what day it takes place etc. It also allows the user to add the class to their shopping bag. Some classes take place on weekdays ('Junior Voice' for example) and with this in mind the user can select their preferred day (Monday-Friday). This function is disabled for classes that take place only on one day. The user can click a button to add an item to their bag or keep shopping. If the user adds an item to their bag, a success message pops up with a summary of the bag contents and a link to go to checkout. This popup also features a discount reminder (if the user has only bought one class they will see a message stating 'Add 1 more class to get a 10% discount!') unless the user has already added more than one item to their bag, in this case the reminder will not show up.
-   **Shopping Bag page** - The user can at any point click on the 'bag' link in the main nav to see a full, detailed list of their items. From here the user can update their bag by removing items or increasing the quantity of items. They can also click a button to go to checkout or keep shopping. Again, this page features a discount reminder (if the user has only bought one class they will see a message stating 'You could get a 10% discount by adding 1 more class!') unless the user has already added more than one item to their bag, in this case the reminder will not show up.
-   **Checkout page** - The user will be prompted to enter their contact details, billing information and credit card number into the checkout form and see a summary of their order. The user will have the option to 'Create an account' or 'Login' to save this information on their profile. They will also have the option to complete order or adjust bag with buttons at the bottom of the page. If the user leaves a mandatory field (denoted by *) blank, they will be prompted to 'please fill out this field'. If the user enters an invalid card number, they will recieve an on-screen message stating the same.
-   **Checkout Success page** - If a user makes a successful transaction they are taken to the checkout success page which features a popup success message (with order number), their full order information and a message stating that a confirmation email has been sent to the email they submitted on the checkout form.
-   **Boards page** - This page features a simple bootstrap table with a list of the current discussion boards (as created by the superuser), their title (a clickable link to go to that board and see a list of topics) how many posts & topics they each contain and when the last post was made on that board (a clickable link to go to that post).
-   **Topics page (Boards)** - Each board contains a topics page, which is a simple bootstrap table containing all the topics under that board heading. The user will see topic title (a clickable link to go to that discussion topic), the name of the user who started the topic, how many replies it has received, how many views it has received and when it was last updated. There is also a button to allow registered users to add a new topic. If a non-registered user clicks this button, they will be prompted to login or register.
-   **Topic Posts page (Boards)** - Each topic contains a posts page, which is a list (in descending chronological order) of replies to that topic. There is a button to allow registered users to reply. If a non-registered user clicks this button, they will be prompted to login or register.
-   **Blog page** - This page features a list of blog posts (as made by the superuser) laid out as bootstrap cards. Each card features an image, post title, article and 'posted by' information. Blog articles are truncated and a read more link has been added which takes the user to the 'Blog Detail' page.
-   **Blog Detail page** - This page features the full article of any blog post, and allows the user to link back tot the main blog by way of a button link.
-   **Register / Sign Up page** - This page allows users to register with a simple form requesting the users email address, username and password. It allows allows the user to return to the login page if they are already registered.
-   **Login / Sign In page** - Allows already registed users to sign in with their username and password. Allows users to go to the register page if they are not yet registered, prompting them to sign up. Features a 'remember me' checkbox, telling the browser to save a cookie so that if the user closes out the window for the site without signing out, the next time they go back, they will be signed back in automatically.

### Visible to registered users
-   **Profile page** - This page features the username and 'billing details' (if they have been saved). It also features an order history.
-   **Edit Post page (Boards)** - Allows a registered user to edit any post they have made, featuring a simple 'message' input field and a 'save changes' button.
-   **New Topic page (Boards)** - Allows a registered user to add a new topic to a board, features a 'subject' input field, 'message' input field and a 'post' button.
-   **Reply Topic page (Boards)** - Allows a registered user to post a reply on any topic, features a simple 'message' input field and a 'post a reply' button.

### Visible to superuser (admin)
-   **Add Class page** - An 'add class' link appears in the 'account' dropdown menu item allowing the superuser to add a new class by way of a form. The form features a dropdown selection of categories and input fields for sku, name, description, day information, price, age, setting (group/solo), teacher, term and image.
-   **Edit/Delete (Class)** - If superuser is logged in, edit and delete links appear on each class card and on the class detail page for quick access to these functions.
-   **Edit Class page** - Features the same form as the 'add class' page but is pre-populated with the current information about a given class.
-   **Add Article page** - An 'post to blog' link appears in the 'account' dropdown menu item allowing superuser to add a new article to the blog by way of a form featuring author, title, body, date and image input fields.
-   **Edit/Delete (Article)** - If superuser is logged in, edit and delete links appear on each blog detail page for quick access to these functions.
-   **Edit Article page** - Features the same form as the 'add article' page but is pre-populated with the current information of that particluar blog artice.
-   **Delete Board / Topic / Post** - If superuser is logged in, a delete link appears beside each board, topic and post in the boards app for quick access to this function and to enable proper moderation.

## Technologies Used

### Languages
-   [HTML](https://www.w3schools.com/html/)
-   [CSS](https://www.w3schools.com/css/)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs
-   [Django](https://www.djangoproject.com/)
    - Django was used to develop the site.
-   [SQLite](https://www.sqlite.org/)
    - SQLite (database engine used by default with Django)
-   [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used to help with design, layout and responsiveness.
-   [Font Awesome](https://fontawesome.com/)
    - Font Awesome icons are used throughout the app.
-   [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub & Heroku.
-   [GitHub](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

## Testing

### Django Testing
-   **Articles App** - Django tests were written and implemented for the forms, models and views files in the Articles app.
-   **Boards App** - Django tests were written and implemented to test the boards, edit post, new topic, posts, reply topic and topics views in the Boards app.

### Defensive Design Testing
-   As detailed above all features have been designed with the consideration to the session user to manage the user actions and visibility.
-   Navigation menu items have been restricted based on session user.

### Code Validators
-   [W3C HTML validator](https://validator.w3.org/) to validate HTML code.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
-   [PEP8 online check](http://pep8online.com/) to review Python code for PEP8 requirements.
-   [Pylint](https://www.pylint.org/) to analyse and validate Python code.

### Testing User Stories from User Experience (UX) Section
-   

### Site UI/UX & Browser Compatibility Testing
-   Manual testing was carried out on this site by the developer's family members to review the UX and site responsivness.
-   Chrome dev tools were used to review responsivness on multiple devices;
    - Moto G4
    - Galaxy S5
    - Pixel 2/2 XL
    - iPhone 5/5E/6/7/8/8+/X
    - iPad/Pro
    - Surface Duo
    - Galaxy Fold
- Cross browser testing was also attempted on Chrome, Opera, Edge, Firefox and Safari.
- Chrome Lighthouse report shows site is highly responsive (insert image)

### Known Bugs
-   Webhooks from Stripe not working, despite efforts to remedy, a 401 error remains, though payment information can be sent to Stripe without issue.

## Deployment
This project was created using Github. From there I used Gitpod to write my code. Then I used commits to git followed by pushes to my GitHub repository. I've deployed this project to Heroku. For deployment on Heroku I've used the following steps;
-   Within the Heroku dashboard, click 'new' app.
-   Give it a name and select the 'region' closest to you.
-   Under 'resources' seacrh postgres and select 'Heroku Postgres'.
-   Slect the 'free' plan.
-   Return to GitPod and do 'pip3 install dj_database_url' followed by 'pip3 install psycopg2-binary'.
-   Freeze these requirments with the 'pip3 freeze > requirements.txt' command.
-   In settings.py, import dj_database_url.
-   Copy database url from Heroku settings (under config vars) and paste in into settings.py - instead of the current settings for database.
-   Migrate these changes with the 'python3 manage.py migrate' command.
-   Run 'python3 manage.py loaddata xxx' command for each fixtures, filling in each fixture name where the xxx is, in the correct order.
-   Run 'python3 manage.py createsuperuser' command and follow the prompts.
-   Remove Heroku database url from setting.py and create 'if statement' for database depending on where the site is running.
-   Run 'pip3 install gunicorn' which will act as the new webserver.
-   Run 'pip3 freeze > requirements.txt' again.
-   Create 'Procfile' to tell Heroku to create a web dyno, which will run gunicorn and serve our django app.
-   Log into Heroku from the command line using 'heroku login -i' and then entering requested credentials.
-   Run 'heroku config:set DISABLE_COLLECTSTATIC=1' command so that static files won't be colleted when we deploy.
-   Add Heroku link to 'allowed' hosts in settings.py.
-   

## Credits

### Tutorials
-   This app was built in conjunction with The Code Institute 'Full Stack Frameworks With Django' module.
-   [Tutorial 1](https://www.pythonistaplanet.com/how-to-create-blog-using-django/) - used to help create the 'Blog' app.
-   [Tutorial 2](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html) - used to help create the 'Boards' app.

### Code & Content
-   [Am I Responsive?](http://ami.responsivedesign.is/) - Used to obtain main README image of site on various screens.

### Acknowledgements
-   Mentor - Gerry McBride
-   Tutor Support - Code Institute
-   Developer - Gary Burke