# Django Student Portal

![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/1f5a3a96-2e65-459a-b9e0-49de9e9a4afc)

This is a simple Django-based CRUD (Create, Read, Update, Delete) operation system for managing student records. The portal allows users to register new students, view registered students, update student details, and delete student records.

## Features
- **Student Registration**: Register new students by providing basic details like ID, Name, Email, and Contact Number.
- **View Students**: View a list of all registered students.
- **Update Student Details**: Edit or update existing student records.
- **Delete Students**: Remove a student's record from the system.

## Technologies Used
- **Django**: Web framework for building the application.
- **HTML/CSS**: Frontend for styling and user interaction.
- **MySQL**: MySQL database used by Django (you can switch to others like Postgresql if needed). 
## Requirements
- Python 3.x
- Django 3.x or above

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-student-portal.git
    ```

2. Navigate into the project directory:

    ```bash
    cd django-student-portal
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the admin panel (optional):

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your browser and go to `http://127.0.0.1:8000/` to access the student portal.

## License
This project is open-source and available under the [MIT License](LICENSE).
