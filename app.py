

from flask import Flask, render_template, request, jsonify,session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = "sudhiksha"

# ✅ Configure your working Gemini API key
genai.configure(api_key="AIzaSyA_u9hnrvBLvRmFwM6zGURIvkvOpWr1wG0")

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json["message"]

    # Initialize chat history for this session
    if "chat_history" not in session:
        session["chat_history"] = []

    chat_history = session["chat_history"]

    # Reset chat if user types "reset"
    if user_input.lower() == "reset":
        chat_history.clear()
        session["chat_history"] = chat_history  # save empty list
        return jsonify({"reply": "Chat history cleared. Start a new conversation!"})

    # Add user message to chat history
    chat_history.append(f"User: {user_input}")

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        conversation_text = "\n".join(chat_history)
        response = model.generate_content(conversation_text)

        bot_reply = response.text

        # Add bot reply to chat history
        chat_history.append(f"Bot: {bot_reply}")
        session["chat_history"] = chat_history  # save updated history

    except Exception as e:
        bot_reply = "Sorry, I ran into an error: " + str(e)

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
