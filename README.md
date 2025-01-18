This is a simple and intuitive To-Do app built with Django, Python and Bootstrap (I used Visual Studio Code). This app allows you to create, update, view and delete tasks, helping you stay organized and manage your tasks effectively.

**Features** 

- User Authentication: Users can register, login, and manage their profiles.

- Task Management: Users can create, update, and delete tasks.

- Task List: View a list of tasks with details such as title, description, and the author of each task.

- CRUD Operations: Full Create, Read, Update, Delete functionality for tasks.

- Responsive Design: Built with Bootstrap for a clean and responsive interface.

The main app (project_app) is built within the virtual environment and it follows Django's MVT architecture:

- Model: Defines the data structure, such as the To_do model for tasks.

- View: Handles the logic and retrieves data from the models. For example, the ToDoListView and ToDoDetailView are class-based views used to display the list of tasks and task details.

- Template: Manages the user interface. The templates include HTML files that are styled with Bootstrap. The templates folder is created inside the project_app folder, so that the views are returning the corresponding templates when the pages are rendered.

**Django Features Used**

- Authentication: The app uses Django's built-in authentication system to manage users, allowing them to register, log in, and log out.

- CRUD Functionality: The app implements CRUD functionality for tasks using Django’s class-based views (CBVs).

- Crispy-Forms: The app uses crispy-forms to render HTML forms with a Bootstrap layout.

- Database: The app uses SQLite as the default database for development.

**Frontend Design**

Bootstrap: The app's interface is built using the Bootstrap framework, ensuring a responsive design that looks good on both mobile and desktop devices.

**Installation**

To get the app up and running locally, follow these steps:

1. Clone the repository

```
git clone https://github.com/your-username/to-do-app.git
cd to-do-app
```

2. Set up a virtual environment

```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply database migrations

```
python manage.py migrate
```

5. Create a superuser to access the Django admin panel. (You can also create some test users through the panel)

```
python manage.py createsuperuser
```

6. Run the development server

```
python manage.py runserver
```

Then, visit http://127.0.0.1:8000 in your browser to view the app.


**Usage**

- Register an account: Users must register to create, update, and delete tasks.

- Login: After registering, log in to access the dashboard.

Manage tasks:

- Create new tasks.

- View task details.

- Update task information.

- Delete tasks when no longer needed.

- Profile: View user information through the profile page.
