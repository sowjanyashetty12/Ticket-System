
**Ticket Management System**

A Django-based application to manage support tickets, allowing users to register, login, add new tickets, update ticket details, and delete resolved tickets.


## Features

- User Authentication: User registration and login functionality.
- CRUD Operations: Full Create, Read, Update, Delete operations for tickets.
- User Interface: Simple and user-friendly interface for managing tickets.



## Tech Stack

**Backend**: Django, Python

**Frontend**: HTML, CSS, JavaScript

**Database**: SQLite

**Version Control**: Git


## Installation

Clone this repository
```bash
  https://github.com/sowjanyashetty12/Ticket-System
  cd ticketsys
```
Activate Virtual Environment
```bash
 source venv/bin/activate  
```
Install the required packages
```bash
pip install -r requirements.txt  
```
Apply Migrations
```bash
python manage.py migrate
```
Create Super User
```bash
python manage.py createsuperuser

```
Run the developement Server
```bash
python manage.py runserver

```
## Endpoints

1 : Register: Visit /register to create a new user account.

2 : Login: Visit /login to log into your account.
  
  Login required for below endpoints

3:  Add Ticket: Visit /createrecord to add new ticket

4: Update Ticket: Visit /updaterecord/<ticket_id> to update the    ticket details

5:View Ticket: Visit /viewrecord/<ticket_id> to view ticket details

6: Delete Ticket : Visit /deletercord/<ticket_id> to delete the ticket


