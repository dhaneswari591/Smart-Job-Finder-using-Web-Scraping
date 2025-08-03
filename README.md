# Smart-Job-Finder-using-Web-Scraping
# 💼 Job Scraper Alert System

A Python-based web app that scrapes job listings, matches them with user preferences using NLP (TF-IDF + Cosine Similarity), and sends alerts via email or desktop pop-ups.

## 🚀 Features

* 📝 User input form for job preferences
* 🔍 Job matching using Machine Learning
* 📬 Email alerts using Gmail SMTP
* 🔔 Windows popup alerts
* 📀 Real-time job data (from Kaggle dataset)
* 🌐 Flask-powered web interface

## 📁 Project Structure

```
job-alert-system/
├── app.py                # Flask app
├── job_matcher.py        # Matching logic + email alerts
├── email_alert.py        # Gmail alert system
├── gui_alert.py          # Windows popup alert
├── templates/            # HTML files
├── utils/preprocess.py   # Text preprocessing
├── dataset/              # Kaggle dataset
├── requirements.txt
```

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/job-alert-system.git
cd job-alert-system
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## ✉️ Email Alerts Setup

1. Enable 2FA on your Gmail account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate an app password for “Mail”
4. Replace in `email_alert.py`:

```python
from_email = 'your_email@gmail.com'
from_password = 'your_app_password'
```

## 🧠 Tech Stack

* Python
* Flask
* scikit-learn
* BeautifulSoup
* Selenium (for future scraping)
* win10toast
* Gmail SMTP

## 📂 Dataset Used

* **[JustJoinIt 2021-2023](https://www.kaggle.com/datasets/justjoinit/remote-it-jobs)** from Kaggle

## 🧑‍💻 Author

**Dhaneswari Jogi**
Fresher, CSE Student | Data Analyst & Web Enthusiast
[GitHub](https://github.com/dhaneswari591) | [LinkedIn](https://www.linkedin.com/in/dhaneswari91)
