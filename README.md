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
![f](https://user-images.githubusercontent.com/99824151/212527517-95a70e89-8469-46c8-80c5-ba021f400bb8.png)


*  it should look like this:


![d](https://user-images.githubusercontent.com/99824151/212527532-b2563526-be82-4cf7-b06f-8d075cd33caa.png)

* Copy the password and paste at **EMAIL_HOST_PASSWORD** in .env file
* Now run the server 
```
python manage.py runserver
``` 
or
```
python-3 manage.py runserver
```
* Open the link generated  in terminal in your browser
# Project Demonstrationg 

![a](https://user-images.githubusercontent.com/99824151/212527394-2d08ed6f-e2f1-42f7-b1e3-c52daca9ed78.png)
![b](https://user-images.githubusercontent.com/99824151/212527452-3815f5fc-a0f5-4aa2-bdf0-600fc0931475.png)
![c](https://user-images.githubusercontent.com/99824151/212527483-2fef81b3-0756-4b3a-b047-9d1f6d49b6a4.png)
![e](https://user-images.githubusercontent.com/99824151/212527567-34e6227d-a9c8-4318-91f6-f85df22c46dc.png)

