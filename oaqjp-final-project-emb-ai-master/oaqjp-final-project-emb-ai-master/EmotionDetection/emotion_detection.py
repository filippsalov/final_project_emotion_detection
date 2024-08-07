import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze  }}

    #Value being returned
    text = requests.post(url, json = myobj, headers=header)
    formatted_text = json.loads(text.text)

    # Assuming 'emotionPredictions' is a list of dictionaries
    emotion_predictions = formatted_text['emotionPredictions'][0]  # Access the first element
    # Emotion scores
    anger_score = emotion_predictions['emotion']['anger']
    disgust_score = emotion_predictions['emotion']['disgust']
    fear_score = emotion_predictions['emotion']['fear']
    joy_score = emotion_predictions['emotion']['joy']
    sadness_score = emotion_predictions['emotion']['sadness']
    # Dominant emotion
    dominant_emotion = ''
    dominant_score = 0
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    for emotion in emotions:
        if emotion_predictions['emotion'][emotion] > dominant_score:
            dominant_emotion = emotion
            dominant_score = emotion_predictions['emotion'][emotion]
    # Returning the value
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}