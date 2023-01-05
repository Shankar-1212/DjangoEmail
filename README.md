# DjangoEmail
This is a simple project developed using Django framework and it contains the settings required for successfull deployment in localhost.
# Setup
Below are the steps to follow to setup this project locally on your machine
* Clone the project locally on your machine using git clone command
 ``` 
git clone https://github.com/Shankar-1212/DjangoEmail.git
```
* Create and activate a new virtual enviroment.
[Virtual Environment Reference](https://docs.python.org/3/library/venv.html)
* To install dependencies run
 ``` 
 pip install -r requirements.txt
 ```
 * In your terminal execute the following commands to makemigrations and migrate to database
 ```
 python manage.py makemigrations
 ```
 ```
python manage.py migrate
```
* Now open terminal go to the directory which contain    settings . py file
* Make .env file by the following command
```
touch .env
```
* Paste the following contents in the file
```
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=YOUR_MAIL_ADDRESS
EMAIL_HOST_PASSWORD=YOUR_MAIL_PASSWORD
RECIPIENT_ADDRESS=MAIL_ADDRESS
```
**Note**: In env file you have to enter your own generated password and your mail account has **2-Step Verification** turn on. 
* Go to your google account settings and search for App passswords then choose Other(Custom name) give name and click on generate
![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot_20230106_015254.png)

*  it should look like this:


![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot%202023-01-06%20at%2002-10-23%20App%20passwords.png)

* Copy the password and paste at **EMAIL_HOST_PASSWORD** in .enc file
* Now run the server 
```
python manage.py runserver
``` 
or
```
python-3 manage.py runserver
```
* Open the link generated  in terminal in your browser
# Project Demonstration
![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot%202023-01-06%20at%2002-22-48%20Send%20Email.png)
![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot%202023-01-06%20at%2002-25-12%20Send%20Email.png)
![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot%202023-01-06%20at%2002-25-23%20Send%20Email.png)
![alt text](https://github.com/Shankar-1212/DjangoEmail/blob/main/raw/Screenshot%202023-01-06%20at%2002-27-10%20Testing%20-%20shankarbhavani2004%40gmail.com%20-%20Gmail.png) 
