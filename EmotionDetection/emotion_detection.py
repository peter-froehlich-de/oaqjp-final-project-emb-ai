import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = my_obj, headers=header)  
    if response.status_code == 200:
        response_json = json.loads(response.text)
        emotions = response_json["emotionPredictions"][0]["emotion"]
        # Find the dominant emotion
        max_score = 0 # Highest score of an emotion
        dominant_emotion = None
        for emotion in emotions:
            if emotions[emotion] > max_score:
                max_score = emotions[emotion]
                dominant_emotion = emotion
        emotions['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotions = {}
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            emotions[emotion] = None
    return emotions

