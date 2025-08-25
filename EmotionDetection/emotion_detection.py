# Import the requests library to handle HTTP requests
import requests
# Import the json library
import json


# Define a function named emotion_detector that takes a string input (text_to_analyze)
def emotion_detector(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set the headers required for the API request
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header)
    # Get formatted response using json library
    formatted_response = json.loads(response.text)
    # Get dictionary with emotions from response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Find dominant emotion
    dominant = max(emotions, key=emotions.get)
    # Add dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant
    # Return data in the reqiurement format
    return emotions
