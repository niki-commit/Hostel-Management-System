# Hostel_Management_System
The aim of the project is to automate the process of traditional Hostel Management System. Students had to go to office room and standing in a queue for hours for room alloting,fee pay etc.They will be able to do all these things by logging into online portal.Students can apply for leave in this portal without standing in a queue for long hours at the time of vacation. Students can see their dues without going to office room.Students can make a complaint if they have any problem like fan not working,LAN not working etc..We can overcome those problems by using this hostel management system.It is a web application. Anyone can use a web browser with an active network connection to access web apps. So, any student can access this by using their login credentials username and password and they can make those things from anywhere.It has many modules like room registration,student information,fee issue,expenses etc,.

This is a web application type project. A web application, unlike computer-based software programs that operate locally on the device’s operating system, is application software that runs on a web server. The user uses a web browser with an active network connection to access web apps.

In this project,I used Python Django for backend,HTML,CSS for front end.User will enter a URL in their browser,that request will go through the internet protocols,to our server,which will then call Django.Django will process the given URL path,and if it matches an URL path we have explicitly stated in the urls.py file,it will call the controller,which will then perform a certain action,such as get an entry from our model (database) and then render a view (HTML/CSS web page).HTML,CSS are used for designing our web pages of our portal.We used SQLite for storing and accessing the database.

## Commands
```bash
pip install -r requirements.txt
py manage.py createsuperuser
py manage.py runserver
```
(enter your username, email, password) after 'py manage.py createsuperuser' command