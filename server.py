''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
# Import the emotion_detection function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the dictionary with emotions.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    # Create str with emotions for answer without dominant emotion
    items = []
    for k, v in response.items():
        if k != 'dominant_emotion':
            items.append(f"'{k}': {v}")
    emotions_str = ", ".join(items[:-1]) + " and " + items[-1]
    # Find dominant emotion
    dominant = response['dominant_emotion']
    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
