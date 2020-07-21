import os
from flask import *
import speech_recognition as sr

from converter import *
from VideoGenerater import *


app = Flask(__name__)
input_string = ""
isl_string = ""


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speechConverter')
def speechConverter():
    p = os.path.dirname(os.path.abspath(__file__))
    p=p+r"\static\result.mp4"
    if(os.path.exists(p)):
        os.remove(p)
    else:
        print("no result.mp4 available")
    r = sr.Recognizer()
    with sr.Microphone() as source:   
        r.adjust_for_ambient_noise(source)
        print("Say:")
        audio = r.listen(source)
        input_string = r.recognize_google(audio)
        print(input_string)
        isl_string_data = englishToISLConverter(input_string)
        print("\n\n")
        videoGenerater(isl_string_data['pre_process_string'])
        fileGenerater(input_string, isl_string_data['isl_text_string'])
    return "Nothing"
    








if __name__ == '__main__':
   app.run()