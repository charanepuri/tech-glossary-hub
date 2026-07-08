# 📚 Tech Glossary Hub

A modern **Django-powered web application** that helps students, beginners, and developers understand technical concepts through simple definitions, detailed explanations, practical examples, and organized learning categories.

Whether you're learning Programming, Python, Django, JavaScript, React, Databases, or DevOps, Tech Glossary Hub provides an easy-to-navigate platform for exploring essential technical terminology.

---

## 🚀 Live Demo

**Coming Soon**

---

# ✨ Features

- 📚 45+ Technical Glossary Terms
- 📂 7 Learning Categories
- 🔍 Organized Learning Experience
- 📖 Beginner-Friendly Definitions
- 💡 Detailed Explanations
- 💻 Practical Code Examples
- 🎯 Difficulty Levels
- ⭐ Featured Glossary Terms
- 📱 Fully Responsive Design
- ⚡ Dynamic Content with Django ORM
- 🛠 Custom Django Admin Panel
- 🎨 Modern Bootstrap UI

---

# 📂 Categories

- Programming
- Python
- Django
- JavaScript
- React
- Database
- DevOps

---

# 🏗 Project Structure

```text
tech_glossary_hub/
│
├── glossary/
│   ├── migrations/
│   ├── static/
│   │   └── glossary/
│   │       ├── css/
│   │       ├── js/
│   │       └── images/
│   │
│   ├── templates/
│   │   └── glossary/
│   │       ├── partials/
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── category_list.html
│   │       ├── category_detail.html
│   │       ├── glossary_list.html
│   │       └── glossary_detail.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── static/
├── tech_glossary_hub/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- JavaScript

### Backend

- Python
- Django

### Database

- SQLite

### Development Tools

- Git
- GitHub
- VS Code

---

# 🗄 Database Design

## Category Model

| Field       | Type          |
| ----------- | ------------- |
| Name        | CharField     |
| Slug        | SlugField     |
| Description | TextField     |
| Icon        | CharField     |
| Color       | CharField     |
| Created At  | DateTimeField |
| Updated At  | DateTimeField |

---

## GlossaryTerm Model

| Field       | Type          |
| ----------- | ------------- |
| Category    | ForeignKey    |
| Title       | CharField     |
| Slug        | SlugField     |
| Definition  | TextField     |
| Explanation | TextField     |
| Example     | TextField     |
| Difficulty  | CharField     |
| Is Featured | BooleanField  |
| Created At  | DateTimeField |
| Updated At  | DateTimeField |

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/charanepuri/tech-glossary-hub.git
```

```bash
cd tech-glossary-hub
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🎯 Key Features Implemented

- Django Project Setup
- Database Design
- Django Admin Customization
- Dynamic Homepage
- Featured Categories
- Latest Glossary Terms
- Category List
- Category Detail
- Glossary List
- Glossary Detail
- About Page
- Responsive Navigation
- Responsive UI
- Bootstrap Components

---

# 📈 Future Enhancements

- Global Search
- Category Filters
- Difficulty Filters
- Dark Mode
- User Authentication
- Bookmarks
- Related Terms
- Pagination
- Recently Viewed Terms
- Daily Tech Word
- Quiz Module
- Flashcards
- REST API
- PostgreSQL Support
- Docker Deployment

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Django Project Structure
- Django Models
- Django ORM
- Django Templates
- URL Routing
- Django Admin
- Bootstrap UI Development
- Responsive Web Design
- CRUD-Based Data Management
- Git & GitHub Workflow

---

# 👨‍💻 Author

**Charan Teja Epuri**

Aspiring Python Full Stack Developer

- Portfolio(Django): [Link](https://portfolio-site-django.onrender.com)

- GitHub: [Profile](https://github.com/charanepuri)

- Portfolio(React): [Link](https://charan-react-portfolio.vercel.app)

- LinkedIn: [Profile](https://www.linkedin.com/in/charan-teja-972aa9231)

- Portfolio(Flask): [Link](https://flask-developer-dashboard-portfolio.onrender.com)

---

# 📄 License

This project is created for educational and portfolio purposes.
