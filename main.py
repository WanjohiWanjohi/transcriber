import streamlit as st
from transcribe import *
import time
st.header('Transcribe audio file')
fileObject = st.file_uploader(label='Select file to upload')

if fileObject:
    token , t_id = upload_file(fileObject)
    result = {}
    #polling 
    sleep_duration = 1 
    percent_complete = 0
    progress_bar = st.progress(percent_complete)
    st.text('Currently in queue')
    while result.get('status') != 'processing':
        