# 🔗 Simple URL Shortener

A simple and efficient URL Shortener web application that converts long URLs into short, easy-to-share links.

## 📌 About the Project

The **Simple URL Shortener** is a backend-focused web application designed to generate short URLs from long URLs. When users access the generated short URL, they are automatically redirected to the original URL.

This project demonstrates fundamental backend development concepts such as URL processing, routing, unique short-link generation, and HTTP redirection.

## 🚀 Features

* 🔗 Convert long URLs into short URLs
* ⚡ Generate unique short links
* 🔄 Redirect short URLs to the original URLs
* 🖥️ Simple and user-friendly interface
* 📦 Lightweight and easy to run
* 🛠️ Demonstrates basic backend development concepts

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **SQLite** / Database
* **Git & GitHub**

## 📂 Project Structure

```text
simple_url_shortener/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── database/
    └── database.db
```

> The exact structure may vary depending on your project files.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/simple_url_shortener.git
```

### 2. Navigate to the project folder

```bash
cd simple_url_shortener
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

Go to:

```text
http://127.0.0.1:5000/
```

## 💡 How It Works

1. User enters a long URL.
2. The application validates the URL.
3. A unique short identifier is generated.
4. The short URL is stored in the database.
5. The user receives the shortened URL.
6. When the short URL is opened, the application redirects the user to the original URL.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Backend development using Python
* Flask routing and request handling
* URL shortening logic
* Database integration
* HTTP redirection
* Building and testing web applications
* Using Git and GitHub for version control

## 🔮 Future Enhancements

* User authentication
* Custom short URLs
* URL expiration
* Click tracking and analytics
* QR code generation
* REST API integration
* Improved UI/UX

## 👨‍💻 Author

**Shaik Tabrez**

B.Tech — Artificial Intelligence & Machine Learning

---

