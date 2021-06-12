import os
from dotenv import load_dotenv
import requests

def get_url(token , data):
    '''
    Parameter:
    token: The API key 
    data: The uploaded file object
    Return:
    url: A url to the uploaded file 
    '''
    headers = {'authorization':token}
    response = requests.post('https://api.assemblyai.com/v2/upload' , 
                            headers=headers, 
                            data=data)
    url = response.json()['upload_url']
    print('Uploaded FIle and got temporary Url to file')
    return url

    def get_transcribe_id(token, url):
        '''
        Parameter:
        token:The API Key
        url: Url to uploaded file
        Return Value:
        id: The transcribe id of the file
        '''
        endpoint = 'https://api.assemblyai.com/v2/transcript'
        json = {
            'audio_url':url
        }
        headers = {
            "authorization":token, 
            "content-type":'application/json'
        }
        response = requests.post(endpoint , json=json , headers=headers)
        id = response.json()['id']
        print("Made request and file is currently queued")
        return id

    def get_text(token , transcribe_id):
        '''
        Parameter:
        token: The API Key
        transcribe_id: The ID of the file to be transcribed
        Return Value:
        result: The response object in JSON format
        '''
        endpoint = f"https://api.assemblyai.com/v2/transcript/{transcribe_id}"
        headers = {
            "authorization": token
        }
        result = requests.get(endpoint ,headers=headers).json()
        return result