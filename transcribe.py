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
        '''

        pass
