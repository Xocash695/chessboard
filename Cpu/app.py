from flask import Flask, request, jsonify
from start import *
import tempfile
import os
from os import environ as env
from newai import cleanup

from dotenv import load_dotenv, find_dotenv




app = Flask(__name__)


@app.route('/upload', methods=['POST'])

def upload_image():
    try:
        print("Request data:", request.data)
        print("Request form:", request.form)
        print("Request files:", request.files)

        # Check if the post request has the file part
        if 'file' not in request.files:
            print("No file part")
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            print("No selected file")
            return jsonify({'error': 'No selected file'})

        temp_filename = os.path.join(tempfile.gettempdir(), file.filename)
        file.save(temp_filename)
        
        # Process the image (you may want to do more meaningful processing here)
        # img = Image.open(file)
        # img.show()
 

        output = start(temp_filename)
        print(output)
        return jsonify(output)
    except Exception as e:
        print(f"Error in /upload: {e}")
        return jsonify({'error': 'Internal server error'})


@app.route('/gamestat', methods=['POST'])

def gamestat():
    # Get the form data from the request

    # gameid = request.form.get('gameid', '')
    # Access specific form fields
    gamestats = request.form.get('reset', '')
    iswhite = request.form.get('iswhite', '')

    
    if gamestats.upper() == 'TRUE': 
        print("RESETTING")
        if iswhite.upper() == 'TRUE':
            value = reset_board(True)
            print("AI playing as White")
            return value
        else:
            reset_board(False)
            print("Resetted board")
            return "Resetted Board"
    # Do something with the form data (e.g., print it)
   
    
    # Return a response
    

if __name__ == '__main__':
    cleanup()
    app.run(host='0.0.0.0', port=9081)
