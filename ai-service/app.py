# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# @app.get("/predict")
# def predict():
#     return {"message": "AI Model Response"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5000)
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your AI models here (example for emotion recognition)
# emotion_model = tf.keras.models.load_model('model/emotion_model.h5')

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    try:
        data = request.json
        # image_data = preprocess(data['image'])
        # prediction = emotion_model.predict(image_data)
        # For now, return mock data
        return jsonify({
            'emotion': 'happy',
            'confidence': 0.85
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)