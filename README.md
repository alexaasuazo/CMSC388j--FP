# CMSC388j--FP
This final project is based off of project 4. It maintains all the same functionalities but also allows logged in users to reply to reviews that other users have made. 

Only logged in users are allowed to review movies and reply to other users reviews. 

Forms user:
1.) Reply to review form: Takes in the review id that the user is replying to, the content of the reply and a submit field to allow a user to submit a reply to someone elses specific review.
2.) Login form: Allows users to login to their account.
3.) Registration form: Allows a user to create a new account, as long as the username is not already taken and the email address a valid format.
4.) Movie review form: Allows a logged in user to submit a review on the movie_details page for that specific movie.

Blueprints:
1.) Movies blueprint which has movie_detail, reply_to_review, etc. routes.
2.) Users blueprint which has registration, login, etc. routes.

Database:
In the MonogDB, stored and retreived values include movie reviews, user information (username, password, email), user replies and review IDs to allow users to reply to specific reviews.
