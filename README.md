# Savior
EcoSavior is a Django website that allows users to report pollution in coasts, jungles, and other environments. Our goal is to help users identify and locate pollution so that it can be cleaned up and the environment can be restored. Whether you're an individual, a community, or an organization, EcoSavior provides a platform for reporting and tracking pollution in a simple and efficient manner.

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

![tg_image_2129009688](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/d81d32e3-5db7-4462-bae6-c90675d0bb0d)
![Screenshot 2023-06-08 at 11-30-25 دریابان خانه](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/4a83065f-5825-4168-a2b5-b23d3db59b00)
![Screenshot 2023-06-08 at 11-30-52 دریابان ورود](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/e0b242cd-7997-4991-a82b-37369ba0c3ae)
![Screenshot 2023-06-08 at 11-31-01 دریابان ثبت نام](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/0110a45d-73b1-42ac-b6de-2bac0a34cf14)
![Screenshot 2023-06-08 at 11-31-28 دریابان محیط کاربری](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/f7994b67-7870-4594-bd68-dbbefcf5e559)
![Screenshot 2023-06-08 at 11-31-39 دریابان پروفایل کاربری mohammadkhalaj8](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/caae0337-5369-4c11-b0c6-fa3dfa86e3ea)
![Screenshot 2023-06-08 at 11-31-47 دریابان لیست مکان های آلوده](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/677766ef-51af-4670-bee9-f24e907836a7)
![Screenshot 2023-06-08 at 11-32-03 دریابان محل آلودگی](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/d447f1c1-ebe9-4835-a4f0-f1f7c47e894e)
![Screenshot 2023-06-08 at 11-32-39 دریابان گزارش مکان های آلوده](https://github.com/mohamadkhalaj/EcoSavior/assets/62938359/eb95eb8b-331d-4682-9a8b-4721005600bc)


# Get Involved
At EcoSavior, we believe that everyone can make a difference in protecting our environment. By reporting pollution and working together to clean it up, we can create a cleaner, healthier planet for ourselves and future generations. Join our community today and make a positive impact on the world around you!
