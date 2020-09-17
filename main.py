from fileinput import filename

from flask import Flask, render_template, url_for, flash, request, redirect, send_from_directory
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
from googletrans import Translator
import re
import nltk
from nltk.tokenize import word_tokenize
import gensim
from gensim.parsing.preprocessing import STOPWORDS
import pandas as pd
import smtplib
from email.message import EmailMessage

UPLOAD_FOLDER = r"C:\Users\ACER\Desktop\project"
ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1.1 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('home.html', title='Upload New File')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    r = sr.Recognizer()

    with open(filename, "rb") as a:

        file = sr.AudioFile(a)
        with file as source:
            audio = r.record(source)
            
        try:
            recog = r.recognize_wit(audio, key="key")
            audio_text = recog
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError:
            print("Could not request results")

    """# Translation
    translating the audio files to english
    """
    trans = Translator()
    t = trans.translate(recog)
    audio_translate = t.text

    """# Regular expressions
    we are using regular expressions to look for words that could mean there is a threat.
    """

    pattern = re.compile(r"terror+|attack+|fire+|shoot+|bomb+|gun+|revenge+|weapon+|"
                         r"kill+|explode+|murder+|target+|blast+|fight+|destroy+|ruin+|grenade+|death+", re.I,
                         )
    word = re.findall(pattern, audio_translate)
    count = 0
    for match in re.findall(pattern, audio_translate):
        count += 1

    """# removing stopwords
    removing the useless words from the text string by converting the string into tokens and then removing stopwords using spacy library.
    """
    all_stopwords_gensim = STOPWORDS.union(set([".", ","]))
    text_tokens = word_tokenize(audio_translate)
    tokens_without_sw = [
        word for word in text_tokens if not word in all_stopwords_gensim
    ]
    filtered_sentence = (" ").join(tokens_without_sw)
    total_count = len(tokens_without_sw)

    """# frequency
    to find the ratio of the negative words to the total words in order to distinguish between normal and suspicious audios.
    """

    # frequency of negative words
    frequency = ((count / total_count) * 100)

    # """# Sending Email
    # sending an email of the audio which could be a threat to the concerned authorities.
    # """

    if (frequency > 20):
        msg = EmailMessage()
        msg['Subject'] = f'Threat in audio'
        msg['From'] = 'email_id'
        msg['To'] = 'email_id'
        msg.set_content(f'A threat is detected in the audio file: {filename}')
        b = 'A threat is detected in the audio file'

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login('email_id', 'password')

            smtp.send_message(msg)
    else:
        b = 'this is a normal audio with no threat'

    contents = {"Name": filename, "words": word, "message": b, "frequency": frequency}

    return render_template("display.html", contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
