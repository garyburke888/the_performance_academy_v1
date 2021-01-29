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
    -   The site is a a dark theme, mainly black backgrounds and white text, making use of Bootstrap info style buttons.
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
-   **Index page** - Upon entering the site you are greeted by the main nav, a discount banner, a large performing arts background image, a 'New Term Now Enroling' statement and a call-to-action button.
-   **Main Nav Menu** - The main menu (collapsed on mobile devices) features dropdown lists where the user can select classes and categories as follows;
    -   Classes by age, price, category or all classes.
    -   Singing classes in the following categories: Rock/Pop, Opera/Classical, Musical Theatre or all singing.
    -   Dancing classes in the following categories: Ballet, Hip Hop, Tap, Ballroom, Musical Theatre or all dancing.
    -   Acting classes in the following categories: Stage, Screen, Improv, Musical Theatre or all acting.
    -   Instrument classes in the following categories: Piano, Guitar, Bass Guitar, Drums, Ukulele or all instruments.
-   **Mian Nav Search Box** - Always visible, some info on how this works...
-   **Main Nav Account** - Always visible dropdown menu to register or login.
-   **Main Nav Shopping Bag** - Always visible link to the session users shopping bag, which also contains the current total cost of items in the bag.
-   **Discount Banner** - Always visible to remind users they can recieve a discount by booking more than 1 class.
-   **Classes page** - This is main page of the site which features a list of available classes displayed in bootstrap cards. The list of classes can be sorted directly from the 'sort by...' dropdown which includes age (youngest-oldest/oldest-youngest), price (low-high/high-low), name (a-z/z-a) or category (a-z/z-a). When a user selects a certain category or group of categories ('All Singing' for example) from the main menu, all classes in that category / those categories will be listed on the classes page, with an array of bootstrap badges displaying on top which are also quick links to categories themselves. Click on the image of any class to see further details about that class.
-   **Class Detail page** - The class detail page contains more information about a given class, such as a full description, the teacher, what day it takes place etc. It also allows the user to add the class to their shopping bag. Some classes take place on weekdays ('Junior Voice' for example) and with this in mind the user can select their preferred day (Monday-Friday). This function is disabled for classes that take place only on one day. The user can click a button to add an item to their bag or keep shopping. If the user adds an item to their bag, a success message pops up with a summary of the bag contents and a link to go to checkout. This popup also features a discount reminder (if the user has only bought one class they will see a message stating 'Add 1 more class to get a 10% discount!') unless the user has already added more than one item to their bag, in this case the reminder will not show up.
-   **Shopping Bag page** - The user can at any point click on the 'bag' link in the main nav to see a full, detailed list of their items. From here the user can update their bag by removing items or increasing the quantity of items. They can also click a button to go to checkout or keep shopping. Again, this page features a discount reminder (if the user has only bought one class they will see a message stating 'You could get a 10% discount by adding 1 more class!') unless the user has already added more than one item to their bag, in this case the reminder will not show up.
-   **Checkout page** - The user will be prompted to enter their contact details, billing information and credit card number into the checkout form and see a summary of their order. The user will have the option to 'Create an account' or 'Login' to save this information on their profile. They will also have the option to complete order or adjust bag with buttons at the bottom of the page. If the user leaves a mandatory field (denoted by *) blank, they will be prompted to 'please fill out this field'. If the user enters an invalid card number, they will recieve an on-screen message stating the same.
-   **Checkout Success page** - If a user makes a successful transaction they are taken to the checkout success page which features a popup success message (with order number), their full order information and a message stating that a confirmation email has been sent to the email they submitted on the checkout form.
-   **Boards page**
-   **Topics page (Boards)**
-   **Topic Posts page (Boards)**
-   **Blog page**
-   **Blog Detail page**

### Visible to registered users
-   **Profile page**
-   **Edit Post page (Boards)**
-   **New Topic page (Boards)**
-   **Reply Topic page (Boards)**

### Visible to superuser (admin)
-   **Add Class page**
-   **Edit Class page**

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
    - SQLite (databse engine used by default with Django)
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
-   

### Defensive Design Testing
-   As detailed above all features have been designed with the consideration to the session user to manage the user actions and visibility.
-   Navigation menu items have been restricted based on session user.

### Code Validators
-   [W3C HTML validator](https://validator.w3.org/) to validate HTML code.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
-   [PEP8 online check](http://pep8online.com/) to review Python code for PEP8 requirements.
-   [Pylint](https://www.pylint.org/) to analyse and validate Python code.

### Testing User Stories from User Experience (UX) Section

### Site UI/UX & Browser Compatibility Testing
-   Manual testing was carried out on this site by the developers family members to review the UX and site responsivness.
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
-   step 1...

## Credits

### Tutorials
-   This app was built in conjunction with The Code Institute 'Fullstack Frameworks with Django' module.
-   [Tutorial 1](https://www.pythonistaplanet.com/how-to-create-blog-using-django/) - used to help create the 'Blog' app.
-   [Tutorial 2](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html) - used to help create the 'Boards' app.

### Code & Content
-   [Am I Responsive?](http://ami.responsivedesign.is/) - Used to obtain main README image of site on various screens.

### Acknowledgements
-   Mentor - Gerry McBride
-   Tutor Support - Code Institute
-   Developer - Gary Burke