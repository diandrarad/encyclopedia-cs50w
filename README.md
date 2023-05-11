# Django Wikipedia-like Online Encyclopedia

### [Video Demo](https://youtu.be/izhDUeQ85_A)

## Description
This is a Wikipedia-like online encyclopedia project built using Django. It allows users to create, edit, and search for encyclopedia entries. Entries are written in Markdown and converted to HTML using the python-markdown2 package.

## Overview
The project has the following features:

- Entry Page: Visiting /wiki/TITLE displays the contents of the encyclopedia entry. If an entry does not exist, an error page is displayed.
- Index Page: Lists all encyclopedia entries. Clicking on an entry takes the user to that entry’s page.
- Search: Allows the user to search for an encyclopedia entry. If the entry exists, the user is redirected to that entry’s page. If not, a search results page is displayed.
- New Page: Allows the user to create a new encyclopedia entry.
- Edit Page: Allows the user to edit an existing encyclopedia entry.
- Random Page: Takes the user to a random encyclopedia entry.

## Technologies
The project is built using the Django framework, Python programming language, and the python-markdown2 package.

## Functionality
- util.py: Contains utility functions for loading and saving encyclopedia entries.
- views.py: Contains the views for the web application.
- templates: Contains the HTML templates for the web application.

## How to Use
- Clone the project from Github
Install the requirements using pip
- Run the server using python manage.py runserver
- Access the web application on a browser at http://localhost:8000/

## Credits
This project was completed as part of the CS50 Web Programming with Python and Javascript course. The project specifications and instructions were provided by Harvard University. The "Page Not Found" template used in this project was sourced from freefrontend.com (https://freefrontend.com/html-css-404-page-templates/).
