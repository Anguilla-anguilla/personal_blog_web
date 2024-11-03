# Personal blog

A blog web page built with Django, featuring admin authentication, rich text editing, and simple design.

## Features
- **Rich Text Editing**: Utilizes CKEditor for rich text editing in blog posts.
- **Comments**: Simple comment system.
- **Search**: Efficient search for blog posts.
- **Admin Interface**: Admin interface for managing blog content.
- **Categories**: Customizable categories, that will appear at navigation bar.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**:

```git clone https://github.com/Anguilla-anguilla/personal_blog_web.git```

```cd personal_blog_web```

2. **Create a virtual environment**:

```python -m venv venv```

```source venv/Scripts/activate```

3. **Install dependencies**:

```pip install -r requirements.txt```

4. **Apply migrations**:

```python manage.py migrate```

5. **Create a superuser**:

```python manage.py createsuperuser```

6. **Load initial data (optional)**:

```python manage.py loaddata fixtures.json```

7. **Run the development server**:

```python manage.py runserver```

8. **Access the application**:

Open your browser and go to *http://127.0.0.1:8000/*.

### Usage

#### Admin Interface
- **Access the admin panel**: Go to *http://127.0.0.1:8000/admin/* and log in with your superuser credentials.
- **Manage blog posts**: Create, edit, and delete blog posts from the admin interface.

#### User Interface
- **View blog posts**: Browse through the list of blog posts on the homepage.
- **Read full post**: Click on a blog post to read the full content.

[Project URL](https://roadmap.sh/projects/personal-blog)