"""Emotion detection web application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analizer():
    """Analyze emotion from user text."""
    input_text = request.args.get("textToAnalyze")
    response = emotion_detector(input_text)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return response

@app.route("/")
def render_index():
    """Render the main page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
