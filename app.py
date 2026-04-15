from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    system = "You are a helpful tutor."

    if "notes" in question.lower():
        system = "Create short study notes with bullet points."

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    return jsonify({"answer": answer})


@app.route("/")
def home():
    return "Backend is running 🚀"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
