from datetime import datetime
from blog import app, db
from blog.models import Comments, Post, User

#Empties the database
with app.app_context():
    db.drop_all()

#Create empty database
    db.create_all()

#Create entry
    user_1 = User(first_name = "juliette", last_name = "radley", email = "julietter@flask.com")

    post_1 = Post(date = datetime.now(), title = "Security", content_summary = "This post discusses security features in relation to Flask. Alongside Flask’s own in-built security, such as SQLAlchemy’s automatic parameterisation of queries, my site has been secured against a range of vulnerabilities. " , 
    
    content = """

This post discusses Flask’s security features. Alongside Flask’s in-built security,
such as SQLAlchemy’s automatic parameterisation of queries, there are additional
security features on my site to protect against a range of vulnerabilities.

As a framework, Flask has many inbuilt functions which are integral to the protection
of this blog and by implementing them, the sites security is significantly improved.
One of the key security features, Flask’s aptly named Flask-Security, is implemented
through each of its inbuilt modules such as its forms. Flask’s-WTForms protects all
form-based posts from CSRF (Cross-Site Request Forgery) attacks (Flask-WTForms
Documentation, 2022). CSRF attacks may occur when the browser requests include
all cookies, which means the site is unable to recognise whether the user request is
legitimately authorised or if the request is falsely authenticated. Flask’s
documentation describes how this framework protects against these attacks through
using “per-session hidden-form-field csrf-tokens” (Flask-WTForms Documentation,
2022), a unique unguessable string enabling Flask to verify that the user is
authenticated. Flask implements this level of security without the need for
configuration. Furthermore, WTForms also has inbuilt validators which provide
functionality to shield from SQL injection.

Another security feature provided by this blog protects Users by password hashing. I
have implemented Grinberg’s (2014, 2018) method for password hashing. Grinberg
uses Werkzeug’s security library to ensure passwords saved in the database are not
stored in plaintext.

Flask also provides protection against Cross Site Scripting (XSS), which is where
arbitrary HTML and Javascript is injected into the site. To protect against this, Flask
uses Jinja2 configured to automatically “escape all values” (Flask Documentation,
2022) unless the system is told to do otherwise. This has the effect of stopping any
XSS problem which could be created in templates.

Whilst Jinja2 is able to defend against XSS attacks by escaping the HTML, it is
unable to stop XSS attribute injections. To enable protection against this potential

attack all Jinja expressions/attributes should be surrounded by either single or
double quotation marks.
    
    
    """, image_file = "image1.jpeg",author_id = 1)

    post_2 = Post(date = datetime.now(), title = "Quality and Usability", content_summary = "This post discusses quality and usability decisions I made when designing this site. Such as designing the navbar, requiring authentication for certain users and the blog’s accessibility.", 
    
    content = 
    
    """ This post discusses quality and usability decisions which were made when designing this site. These illustratively include, designing the navbar, requiring authentication for certain users and the blog’s accessibility.

The blog has a horizontal navbar along the top of the site for the user to quickly navigate across the Flask blog. The navbar sits across the top of each page on the site allowing easy access through a series of buttons to navigate to the home page, registration page, log in to the site. Once logged in, a button will appear on the navbar, allowing the user to log-out of the site. By using Jinja2, and its ability to ‘extend’ the layout of one HTML file, both the navbar which appears on the top of the site and the footer that appears on the bottom is identical and consistent across all of the blog’s pages. These features provide a familiar and consistent set of navigation tools thus allowing the user to be comforted by the consistency of the webpage’s design.  

One usability feature which I implemented, are the buttons for logging out and leaving a comment. This feature only appears when the user is logged in/authenticated. As these features do not show until the user is authenticated there will be no confusion as to which functions can be accessed by guests and ensures only authenticated visitors can leave comments.

I decided to style the blog using ‘Bulma’ (Bulma Documentation, 2022), which helped to give the blog a clean and simple look. The visual stylistic choices implemented by Bulma gives the blog a similar User Interface (UI) and design to many other social media and other sites. Therefore, by using Bulma to style the blog, this should reduce any apprehension a new user may feel when browsing and interacting with an unfamiliar site for the first time. This familiarity will hopefully encourage confidence in the site by having intuitive navigational features.

In choosing the visual appearance of the blog some design choices had to be made and accessibility was considered chosen as the primary driver of design. A key feature was to make the blog using a minimal colour palette to increase the colour contrast between the backgrounds and the text. The choice of visual language ensures the text is visible, easy to read and accessible for all users, including those who may have visual impairments. The colour contrasts on this blog were tested using an online colour contrast checker (Colour Contrast, 2022). 

Finally, one quality issue with this blog that I was unable to resolve was having posts appear on the blog in block text. As they are stored in the database in plaintext, I was unfortunately unable to find a way to add paragraph breaks or line spaces to the text. Therefore, for ease of reading I have also created two static pages where these two posts are displayed with correct paragraph breaks for ease of reading.
 """, image_file= "image2.jpeg", author_id = 1)

    user_2 = User(first_name = "testuser", last_name = "test", email = "testing@flask.com")
    
    comment_1 = Comments(date = datetime.now(), body = "Interesting post!", author_id = 2, post_id = 1)

    comment_2 = Comments(date = datetime.now(), body = "I like this post!", author_id = 2, post_id = 2)




# Add entry to "session"
    db.session.add(user_1)
    db.session.add(post_1)
    db.session.add(user_2)
    db.session.add(comment_1)
    db.session.add(comment_2)
    db.session.add(post_2)
    





    #Commit or save the "session"
    db.session.commit()