Personal Productivity Assistant Chatbot

A simple AI-based chatbot built using Python, Rasa NLU, Flask, and scikit-learn.
It can understand basic user queries and respond with predefined intents such as greetings, notes, reminders, FAQs, and simple task-related replies.

📌 Overview

This project demonstrates how NLP and machine learning can be used to build a lightweight conversational assistant.
The chatbot uses:

Rasa NLU for intent classification

scikit-learn for training a simple ML pipeline

Flask for backend API and routing

HTML templates for a basic web chat interface

The project is kept minimal for easy understanding and can be extended further.

📁 Project Structure
├── app.py               # Flask backend
├── model.pkl            # ML model (if included)
├── templates/           # HTML UI
│   └── index.html
├── env/                 # Virtual environment files
└── README.md

⚙️ How to Run

Create or activate your virtual environment

Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open in browser:

http://localhost:5000

💡 Features

Simple user-friendly chat interface

Basic intent detection

Lightweight ML model using scikit-learn

Easy-to-understand code structure

Can be extended with more intents and responses

🔧 Technologies Used

Python

Flask

Rasa NLU

scikit-learn

HTML/CSS

📝 Notes

This is a basic version intended for learning and demonstration.

You can add more intents, training data, and conversation rules based on your needs.
