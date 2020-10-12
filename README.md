# Project: Personal_PM

#### [Project repository link](https://github.com/sergeyuspenskyi/Personal_PM)

#### Summary
Web application that allows general user to view his/her weekly loading per projects and admin to upload excel file with the data that will be shown to a certain user.

#### Planned technology stack: Python, HTML, CSS


### Planned User stories

#### For general user:
1. As a general user I may register by email and login in the system (without password restore fucntion for now).
2. As a logged_in general user I may view my weekly loading for current week on a main page in a simple table.

#### For admin:
1. As an admin I may register by email and login in the system (without password restore fucntion for now).
2. As an admin I may go to main page and upload excel file.


### Planned UI/UX structure

#### For general user:
1. Register page: 
 * two fileds - email and password
 * confirm registration button
2. Login page: 
 * two fileds - email and password
 * login button
3. Main page: 
 * view of table with infomation from excel file (uploaded by admin)
 * logout button

#### For admin:
1. Register page: 
 * two fileds - email and password
 * Confirm registration button
2. Login page: 
 * two fileds - email and password
 * login button
3. Main page: 
 * Upload button - to choose a file from your computer to upload. Only XLSX and XLS types are supported.
 * logout button


### Important requirements

1. The template of excel file should have an agreed structure.
2. The view for each general user will be unique depending and identified by email that was used to log_in.
