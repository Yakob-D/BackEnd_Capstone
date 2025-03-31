Event Management API 

Overview

Welcome to my Event Management API! This is a RESTful API designed to help manage events seamlessly. This API allows you to create, view, update, and delete events with ease. It also has user authentication, ensuring that only authorized users can modify events, while anyone can browse the event listings. This API is built using Django rest framework

Key Features

User Authentication: Register, log in, and log out to manage your account securely.
Event Management:
Public Access: Anyone can view the list of events created.
Authenticated Access: Only logged-in users can create, update, or delete events.
Secure Access: Uses token-based authentication to protect modification of events.
Flexible Event Details: Each event includes a title, description, date, location, organizer, capacity, and creation date.
This API is perfect for developers building event management applications, community platforms, or any system that needs to handle event scheduling and user access control.

Getting Started

Prerequisites

To use this API, you’ll need the following tools installed on your system:
Python 3.8 or higher
pip (Python package manager)
A tool like Postman or cURL to make HTTP requests
A database (SQLite is used by default, but you can configure PostgreSQL if preferred)

Setup Instructions

Follow these steps to get the API up and running on your local machine:
Clone the Repository
Download the project files by cloning the repository. Navigate to the project directory.

Install Dependencies

The project includes a requirements.txt file listing all necessary packages. Install them by running:
pip install -r requirements.txt
This will install Django, Django REST Framework, and other dependencies.

Configure the Database

By default, the API uses SQLite, so no extra setup is needed. If you prefer PostgreSQL:
Install PostgreSQL and create a database.
Update the database settings in the project’s settings.py file with your database name, user, and password.

Apply Migrations

Set up the database schema by running:
python manage.py makemigrations
python manage.py migrate

Create a Superuser (Optional)

If you want to access the admin panel to manage users and events, create a superuser account:
python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

Run the Server
Start the development server:
python manage.py runserver
 The API will be available at http://127.0.0.1:8000/. You can now interact with it using a tool like Postman.

Using the API
Base URL
All API endpoints are relative to the base URL:
http://127.0.0.1:8000/

Authentication
This API uses token-based authentication, so you’ll need to register and login to get a token, and include that token in the Authorization header for actions like creating, updating or deleting events.


1. Register a User
Endpoint: /api/user/register/
Method: POST
What It Does: Creates a new user account.
Request Body (JSON):
username: Your desired username.
email: Your email address.
password: Your password (must be at least 8 characters).
Example Request:
{
  "username": "samuel",
  "email": "samuel@gmail.com",
  "password": "123456789"
}
Response:
Success (201 Created): Returns the user’s details, including their ID (e.g., {"id": 1, "username": "samuel", "email": "samuel@gmail.com"}).
Error (400 Bad Request): If the username is taken, you’ll get an error like {"username": ["A user with that username already exists."]}.


2. Log In
Endpoint: /api/user/login/
Method: POST
What It Does: Authenticates a user and returns a token for accessing protected endpoints.
Request Body (JSON):
username: Your username.
password: Your password.
Example Request:
{
  	"username": "abrish",
  	"password": "123456789"
}


Response:
Success (200 OK): Returns a token (e.g., {"token": "your-token-here"}).
Error (400 Bad Request): If credentials are wrong, you’ll get {"detail": "Invalid username or password"}.


3. Log Out
Endpoint: /api/user/logout/
Method: POST
What It Does: removes your token, logging you out.
Headers:
Authorization: Token your-token-here (replace with the token from login).
Request Body: None.
Response:
Success (200 OK): {"message": "Success"}.
Error (400 Bad Request): If the token is missing or invalid, you’ll get an error like {"error": "Token required"} or {"error": "Invalid token"}.
Event Management
Events have the following attributes:
title: The event’s name (max 200 characters).
description: A detailed description of the event.
date: The date and time of the event (in the following format, "2025-04-01T10:00:00Z").
location: Where the event is held (max 200 characters).
organizer: The ID of the user organizing the event (this will be displayed on the register response).
capacity: The maximum number of attendees for the event.
created_date: The date the event was created.
1. List Events (Public Access)
Endpoint: /api/events/
Method: GET
What It Does: Returns a list of all events. Accessible to anyone.
Headers: None.
Response:
Success (200 OK): A list of events, e.g., [{"id": 1, "title": "Test Event", "description": "A test event description", "date": "2025-04-01T10:00:00Z", "location": "Test Location", "organizer": 1, "capacity": 100, "created_date": "2025-03-31"}, ...].


2. Create an Event (Authenticated)
Endpoint: /api/events/create/
Method: POST
What It Does: Creates a new event. You must be logged in.
Headers:
Authorization: Token your-token-here.
Request Body (JSON):
Include all event attributes.
Example Request:
{
  "title": "Meeting",
  "description": "Managers meeting",
  "date": "2025-06-19",
  "location": "Online Zoom",
  "organizer": 5,
  "Capacity": 20,
  "created_date": "2025-09-12"
}
Response:
Success (201 Created): Returns the created event, e.g., {"id": 1, "title": "Test Event", "description": "A test event description", "date": "2025-04-01T10:00:00Z", "location": "Test Location", "organizer": 1, "capacity": 100, "created_date": "2025-03-31"}.
Error (401 Unauthorized): If not logged in, {"detail": "Authentication credentials were not provided."}.

3. Update an Event (Authenticated)
Endpoint: /api/events/update/<id>
Method: PUT
What It Does: Updates an existing event. You must be logged in.
Headers:
Authorization: Token your-token-here.
Request Body (JSON):
Include all event attributes to update the event.
Example Request:
To update event with ID 3, send a PUT request to /api/events/update/3 with:
{
  "title": "Updated Event",
  "description": "Updated description",
  "date": "2025-04-01T10:00:00Z",
  "location": "Updated Location",
  "organizer": 5,
  "capacity": 150,
  "created_date": "2025-03-31"
}
Response:
Success (200 OK): Returns the updated event, e.g., {"id": 1, "title": "Updated Event", "description": "Updated description", "date": "2025-04-01T10:00:00Z", "location": "Updated Location", "organizer": 1, "capacity": 150, "created_date": "2025-03-31"}.
Error (401 Unauthorized): If not logged in, {"detail": "Authentication credentials were not provided."}.

4. Delete an Event (Authenticated)
Endpoint: /api/events/delete/<id>
Method: DELETE
What It Does: Deletes an event. You must be logged in.
Headers:
Authorization: Token your-token-here.
Request Body: None.
Example Request:
To delete an event with ID 1, send a DELETE request to /api/events/delete/1.
Response:
Success (204 No Content): No body returned on successful deletion.
Error (401 Unauthorized): If not logged in, {"detail": "Authentication credentials were not provided."}.

Authentication Flow
To perform actions like creating, updating, or deleting events, follow this flow:
Register: Use the /api/users/register/ endpoint to create an account.
Log In: Use the /api/users/login/ endpoint to get a token.
Use the Token: Include the token in the Authorization header for protected requests.
Log Out: When done, use the /api/users/logout/ endpoint to destroy your token.

Admin Access
If you created a superuser, you can access the Django admin panel to manage users and events:
URL: http://127.0.0.1:8000/admin/
Log in with your superuser credentials.
Use this to view user IDs or manage events directly.

Example Workflow
Here’s how you might use the API to manage an event:
Register a user named "Samuel" using the register endpoint.
Log in with "Samuel" to get a token.
Use the token to create a new event with the create endpoint.
View all events using the list endpoint.
Update the event with new details using the update endpoint.
Delete the event using the delete endpoint.
Log out to invalidate your token.

Troubleshooting
401 Unauthorized: Ensure you’re including the Authorization header with a valid token for protected endpoints.
400 Bad Request: Check your request body for missing or incorrect fields
404 Not Found: Make sure you have a correct endpoint URL and ensure the event ID exists for update/delete requests.
Database Issues: If migrations fail, ensure your database is set up correctly in settings.py.