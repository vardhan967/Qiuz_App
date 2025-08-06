# 📚 Quiz_App

A web-based quiz application built using Python and HTML. This app supports audio-based quizzes and stores data in a SQLite database.

---

## 🗂️ Project Structure

### 🔸 Overview (Indented List)

- Quiz_App Project  
&nbsp;&nbsp;&nbsp;&nbsp;- Quiz_App/ – Main Django app folder  
&nbsp;&nbsp;&nbsp;&nbsp;- Quiz_Base/ – Base files or templates for quiz logic/UI  
&nbsp;&nbsp;&nbsp;&nbsp;- Quiz.zip – Zipped version of the project (likely same as above)  
&nbsp;&nbsp;&nbsp;&nbsp;- db.sqlite3 – SQLite database file  
&nbsp;&nbsp;&nbsp;&nbsp;- manage.py – Django management script  
&nbsp;&nbsp;&nbsp;&nbsp;- populate_audio_quiz.py – Script to populate database with audio quizzes  
&nbsp;&nbsp;&nbsp;&nbsp;- requirements.txt – List of Python dependencies

### 🔹 Visual Tree

```
Quiz_App/
├── Quiz_App/                # Main Django app folder
├── Quiz_Base/               # Base files or templates for quiz logic/UI
├── Quiz.zip                 # Zipped version of the project (likely same as above)
├── db.sqlite3               # SQLite database file
├── manage.py                # Django management script
├── populate_audio_quiz.py   # Script to populate database with audio quizzes
└── requirements.txt         # List of Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vardhan967/Quiz_App.git
cd Quiz_App
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. (Optional) Populate the Database

```bash
python populate_audio_quiz.py
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

###🎯 Features
- 🧠 Quiz interface with support for audio-based questions

- 🔊 Audio quiz functionality

- 👤 User authentication (login/logout)

- 📝 User registration

- 💾 SQLite-based storage

- 📂 Django backend architecture

- 📊 Score tracking and quiz submission

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML
- **Database:** SQLite

---

## 📝 To Do

- [ ] Add user authentication
- [ ] Improve UI with CSS or a frontend framework
- [ ] Add scoring and result tracking
- [ ] Deploy to a cloud platform (e.g., Heroku, Render)
- [ ] Add tests and CI/CD workflow

---


## 🙋‍♂️ About Developer

The content and code in this repository are created with ❤️ by **PrakashVardhan**.

You're welcome to **use**, **modify**, and **share** this project freely under the MIT License.  
I believe in open knowledge and learning together – all I ask is that you **give proper credit**.

> 🚀 If you find this project helpful, feel free to ⭐ the repo or mention me when you use it!

Happy Coding! 😊
