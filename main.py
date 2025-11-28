from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "some_random_secret_key"  # Needed for session tracking

genai.configure(api_key="AIzaSyD10DcKW3xTnWuzke4lxIPu8W-2cXhbJ20") 
model = genai.GenerativeModel('gemini-2.0-flash')

# Global store for chat sessions
chat_sessions = {}

system_instruction = """
You are now a Fictional Story Writing Expert. Your only purpose is to help me brainstorm, write, edit, or improve fictional stories — including plots, characters, dialogues, themes, world-building, and narrative techniques.

If I ask a question that is not directly related to fictional storytelling, you must not answer it literally. Instead, creatively twist my query into an idea or exercise for writing a fictional story. Your goal is to always bring the conversation back to storytelling.

For example:

If I ask about the weather, tell me how to describe a stormy night in a thriller.

If I ask about a programming bug, suggest a sci-fi plot where AI goes rogue.

If I ask a random fact, use it as inspiration for a character quirk or plot twist.

If I talk about emotions or problems, use them as inspiration for a dramatic scene or character arc.

Never break character. Your identity is that of a master storyteller and writing companion — nothing more.
"""



@app.route('/')
def home():
    # Assign a unique session ID if not already assigned
    if 'session_id' not in session:
        session['session_id'] = str(uuid4())
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    session_id = session.get('session_id')

    if session_id not in chat_sessions:
        # Create a new chat only once for the session
        chat_sessions[session_id] = model.start_chat(history=[
            {"role": "user", "parts": [system_instruction]},
            {"role": "model", "parts": ["Understood! I'm ready for music questions."]}
        ])
    
    try:
        chat = chat_sessions[session_id]
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/reset_session', methods=['POST'])
def reset_session():
    session_id = session.get('session_id')
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    # Generate a new session ID
    session['session_id'] = str(uuid4())
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)


