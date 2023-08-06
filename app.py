# app.py
import subprocess
import os
import streamlit as st

def run_disk_scheduler(N, input_data):
    command = ['./disk_scheduler.exe', str(N), 'input.txt']
    result = subprocess.run(command, input=input_data, capture_output=True, text=True)
    return result.stdout

def main():
    st.title('Disk Scheduler Web App')
    st.write('Upload a text file containing the disk scheduling input data.')
    st.write('The format should be: "time cylinder" with each request on a separate line.')
    uploaded_file = st.file_uploader('Upload File', type=['txt'])

    if uploaded_file is not None:
        input_data = uploaded_file.getvalue()
        input_str = input_data.decode()
        # Get the number of requests (N) from the number of lines in the uploaded file
        num_requests = input_str.count('\n') + 1
        result = run_disk_scheduler(num_requests, input_str)
        st.header('Disk Scheduler Result')
        st.code(result, language='text')
        
if __name__ == '__main__':
    main()
