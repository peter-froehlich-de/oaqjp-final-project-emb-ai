from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    answer = f"For the given statement, the system response is "
    for emotion in ['anger', 'disgust', 'fear']:
        answer += f"'{emotion}': {response[emotion]}, "
    answer += f"'joy': {response['joy']} and "
    answer += f"'sadness': {response['sadness']}. "
    answer += f"The dominant emotion is <b>{response['dominant_emotion']}.</b>"

    return answer


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
