# EcoSavior
At EcoSavior, we're dedicated to promoting sustainable living and environmental awareness. We believe that everyone has the power to make a positive impact on the world around them, and we're here to help you do just that. Our repository provides you with practical solutions for reducing waste, conserving resources, and protecting the environment, from eco-friendly product recommendations to tips and tricks for living sustainably. Whether you're an individual, a business, or a community, we're committed to helping you achieve your sustainability goals. Join us in our mission to create a better, more sustainable future!
# Features
This project offers a range of features to help you report and clean up polluted areas, including:
- A feature to add an image of the polluted area
- The ability to add the location of the polluted area
- The option to select the type of pollution, such as metal, paper, plastic, etc.
- The ability for users to see their report and cleaning history
- The ability for users to see the cleaning history of other users
- An email activation feature to verify users' email addresses
- Captcha for login to ensure security and prevent bot attacks
- A responsive design that adapts to different screen sizes and devices
- An email notification to admins when a contact us message is received from users
- The ability to get users' avatar from Gravatar
- The ability to save user uploaded images in Dropbox

By using EcoSavior to report and clean up polluted areas, you'll be making a positive impact on the environment and helping to protect our planet for future generations.

# Get Involved
At EcoSavior, we're committed to making a positive impact on the environment, and we hope you'll join us in this important mission. We believe that everyone can make a difference, no matter how small their actions may seem. So why not start today? Explore our repository, connect with our community, and see how you can be an EcoSavior!

# Compile
## Step 1
```
mv .env-sample .env
```
## Step 2
### Get API
- SECRET_KEY: This is a variable that's commonly used in Django projects to store a secret key that's used for cryptographic signing, hashing, and other security-related purposes. It should be kept secret and not shared publicly.
- EMAIL_HOST_USER and EMAIL_HOST_PASSWORD: These variables are used to store the username and password, respectively, for the email service that the project uses to send emails. They should be set to the appropriate values for the email service being used.
- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: These variables are used by the Python Social Auth library to authenticate users using their Google account. They should be set to the appropriate values for the Google API credentials being used.
- HCAPTCHA_SITEKEY and HCAPTCHA_SECRET: These variables are used by the hCaptcha service to prevent automated spam and abuse on web forms. They should be set to the appropriate values for the hCaptcha account being used.
- DBX_TOKEN, DBX_APP_KEY, DBX_APP_SECRET, and DBX_REFRESH_TOKEN: These variables are used by the Dropbox API to authenticate and authorize access to a Dropbox account. They should be set to the appropriate values for the Dropbox API credentials being used.

## Step 3
Create a virtual-environment and run below commands:
```
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Step 4
Create a superuser and in admin panel add garbage types.
```
python manage.py createsuperuser
```

# Screenshots
