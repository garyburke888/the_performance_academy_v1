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
-   [Home page on desktop](/media/tpa_wf1.jpg)
-   [Classes page on desktop](/media/tpa_wf2.jpg)
-   [Home, Classes and Class Detail pages on smartphones](/media/tpa_wf3.jpg)
-   [Shopping Bag popup, Checkout and Checkout Success pages on smartphones](/media/tpa_wf4.jpg)
-   [Blog, Boards and Profile pages on smartphones](/media/tpa_wf5.jpg)
-   [Board Posts and Board Reply/Add page on tablets](/media/tpa_wf6.jpg)
-   [Add/Edit Class and Sign Out pages on tablets](/media/tpa_wf7.jpg)
-   [The Performance Academy DB Entity Relationship Diagram](/static/images/erisk_erd.png)

## Features
-   Responsive on all screen sizes.
-   User registration, login/logout, password reset, profile update and billing information storage.
-   Search functionality.
-   Mobile collapse nav bar.
-   Different views for user levels (Admin/User)

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