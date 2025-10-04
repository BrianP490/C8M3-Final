"""
This Server module to run the emotion detection flask application\

Defines 2 routes:
1. '/' - Renders the index.html page
2. '/emotionDetector' - Receives text input from the user and returns the emotion analysis
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initiate the flask app
app = Flask("Final_Project")

@app.route('/emotionDetector')
def process_emotion():
    """
    This code receives the text from the HTML interface and runs sentiment analysis over it
    using the 'emotion_detector' function. The output is returned in a formatted style.
    Returns:
        response_skeleton (str): Formatted string containing the emotion analysis results.
    """
    # Extract the text from the request object
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the function for processing
    response_dict = emotion_detector(text_to_analyze)

    # Process the response dictionary
    anger_score = response_dict['anger']
    disgust_score = response_dict['disgust']
    fear_score = response_dict['fear']
    joy_score = response_dict['joy']
    sadness_score = response_dict['sadness']
    dominant_emotion = response_dict['dominant_emotion']

    # Create the response to send to the client
    if dominant_emotion is None:
        response_skeleton = "Invalid text! Please try again!"
    else:
        response_skeleton = f"""For the given statement, the system response is 'anger':
        {anger_score},
        'disgust': {disgust_score}, 'fear': {fear_score}, 'joy':
        {joy_score} and 'sadness':
        {sadness_score}. The dominant emotion is {dominant_emotion}."""

    return response_skeleton

@app.route("/")
def render_index_page():
    """
    Initial rendering of the main application using flask.
    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('index.html')

# Run the flask app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
