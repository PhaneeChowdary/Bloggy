# Bloggy: A Django Blogging Platform
Bloggy is a Django-based blogging application that allows users to create, read, update, and delete posts. It also includes robust user authentication and profile management features, providing a complete platform for bloggers.

## Features
-   **User Authentication:** Secure user registration, login, and logout functionality.
-   **Password Reset:** Allows users to reset their passwords via email.
-   **CRUD Operations for Posts:** Users can Create, Read, Update, and Delete their blog posts.
-   **Post Viewing:** View all posts in a central feed and click to see individual post details.
-   **User Profiles:** Each user has a dedicated profile page displaying their posts and information.
-   **Responsive Design:** The application is designed to work well on various screen sizes.
-   **Static File Management:** Efficiently serves CSS, JavaScript, and images.
-   **Media File Handling:** Supports user-uploaded images for profile pictures and potentially post content.

## Setup and Installation
To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/PhaneeChowdary/Bloggy.git
    cd Bloggy
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Thank you
