"""
This module provides a Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    This function receives text from the HTML interface and runs
    emotion detection on it using the emotion_detector() function.
    The output shows the scores for various emotions and the dominant emotion.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page
    over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
