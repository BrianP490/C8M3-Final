import requests
import json

def emotion_detector(text_to_analyse):
    """ Crafts a request to an LLM and parses the response.
    Args:
        text_to_analyse (str): The input string from the client/user.
    Returns:
        output (dict): the dictionary of anger-score pairs and the dominant emotion.
    """ 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }   

    resp = requests.post(URL, json=Input, headers=Headers)

    if resp.status_code == 400:
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        json_resp = json.loads(resp.text)
        emotion_dict = json_resp['emotionPredictions'][0]['emotion']

        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust']
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']

        dominant_emotion_tuple = max(emotion_dict.items(), key=lambda item: item[1])
        dominant_emotion = dominant_emotion_tuple[0]

        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    return output