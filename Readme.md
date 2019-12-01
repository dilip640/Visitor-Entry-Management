# Visitor Entry Management Software

The software is designed to keep a proper log of the visiters who visit an office. It notifies the host about the visiters via an e-mail, and the visitor also gets the info about their visit via a SMS and an e-mail.

The problem statement to the content can be found here: https://summergeeks.in/static/assignments/summergeeks%202020%20-%20SDE%20Assignment.pdf


## How to install
 1. Set values of environment variable in `.env` file
 2. Install dependencies from `requirements.txt`

    Required python version is 3.6

    ```$ pip install requirements.txt```
 3. Setup Database and Migrate

    ```$ python manage.py makemigrations```

    ```$ python manage.py migrate```
 4. Run App

    ```$ python manage.py runserver```

## Specifications:

>The web application supports two kinds of users:

* Host
* Visitor

> A host registration is required before any visitor's visit.

> Registration as a host can be facilitated only after a password verification. As for visitor registration, there is no such requirement.

> The host info can be modified later(only after password verification), in case the host changes.

> To avoid accidental checkouts, the checkout process is facilitated by a verification step wherein the user needs to validate the phone number he provided during checkin.

> Upon verification and successful checkout, the user is notified, via a SMS, about his visit.

> Proper messages are displayed in case of validation failures.