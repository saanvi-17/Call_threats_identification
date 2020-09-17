# **Identifying Threats In a Call Recording**
<p>Data science in defence and military organizations plays a huge role in strengthening the security forces of the country. Countries are working on improving their security by using new age weapons and so it’s necessary to invest in virtual security as well. 
  </p>
 
    
 ![Webp net-resizeimage](https://user-images.githubusercontent.com/62648110/93492070-07050900-f928-11ea-9a05-c056064cb731.jpg)    ![Webp net-resizeimage (1)](https://user-images.githubusercontent.com/62648110/93492593-9ad6d500-f928-11ea-84b9-bb728f3e0e39.jpg)
 
 
 
## Aim-
<p>The aim of this project is to identify if a call recording contains a message which could be a threat to the security of our country. By looking at some specific words and their usage in the recording we will decide if the call should be considered as threatening or not. 
  </p>
  <p align="center">
  <img src="https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fcognitiveworld%2Ffiles%2F2018%2F08%2F4-ways-the-global-defense-forces-are-using-AI.jpg" width="300" height="300" /></p>

# Flowchart


![flowchart](https://user-images.githubusercontent.com/62648110/93494666-e8ecd800-f92a-11ea-8f2d-8b44a7338853.png)


# Libraries Used

1. import speech_recognition as sr           
   used for speech recognition

2. from googletrans import Translator        
   For translation

3. import re             
   for regular expressions 

4. import nltk                               
   for natural language processing

5. from nltk.tokenize import word_tokenize   
   to tokenize a string 

6. import spacy                             
	 for stopwords

7. import pandas as pd        
 	 for data analysis

8. import smtplib   
	 sending email

9. from email.message import EmailMessage

10.	from flask import Flask, render_template, url_for, flash, request, redirect, send_from_directory

11. import os

12.	from werkzeug.utils import secure_filename

# Methodology
## Flask
Flask is a web framework. It provides us with tools, libraries and technologies that allows us to build a web application. This web application can be some web pages, a blog and a wiki or go as big as a web-based calendar application or a commercial website.

-	The project has been created using Flask in PyCharm.

-	In our project we have created a template ‘home.html’ which allows the user to upload an audio file of size up to 1MB in .wav format.

-	Then it is checked if the user has uploaded the file according to the requirements. A flash message is displayed when there is no file or wrong file is uploaded.

-	There is another template ‘display.html’ which displays the name of the audio file, the threatening words that are being used, the frequency of the words and whether the  audio is a threat or not.

-	A mail is then sent to the concerned authorities so that they can take necessary action.


## Speech to text
-	In this project we upload an audio file which is in ‘.wav’ format in our user interface. All these audio files are stored in a directory. We have created an API using wit.ai to convert the Hindi audio files to text. 

-	Wit.ai is a natural language processing interface used to turn sentences into structured data. Most important feature of wit.ai is that it is free.   We have used it for speech recognition.

Steps involved to use wit.ai – 

1.	Login to wit.ai using Github or Facebook account.  
2.	Click on ‘+’ sign in Menu Bar and create a new app.
3.	Then go to settings of the app. Under API details, copy the server access token to use it as an API key. 

-	Recognizer class as the name suggests is used to recognize speech.

-	An exception will be thrown if for some reason the API is not called properly or there is some error.

-	After the transcription is done, the text string is stored.

## Translation
-	Googletrans is a library that implemented Google Translate API. We have used this to translate our text strings to English (from Hindi). 

-	The translated text strings are then stored.

## Regular Expression
-	A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.

<p align="center">
<img src="https://user-images.githubusercontent.com/62648110/93500910-594b2780-f932-11ea-92aa-56c7e2d582df.png" width="500" height="300" />
</p>

-	The text obtained from the converted audio will be matched with the help of regular expression to find threatening words (like terrorism, weapons, shoot, kill etc.) and identify if the call is a threat. We use a counter along with this to count the number of matches.

# Stopwords
-	Stopwords are considered as noise in text. Text may contain stopwords like is, an, the etc. Stopwords are removed or excluded from the given text so that more focus can be given to those words which define the meaning of the text. We can create a list of stopwords to filter out the words that we need.

-	We use NLTK to convert the strings to tokens so that each word can be compared individually. 
-	We have used the gensim library which has a list of its own stopwords which can be used to efficiently remove stopwords. 

-	After removing the stopwords we find out the total number of words, tokens and filtered sentences 

 # Frequency
-	We calculate the ratio of the negative words to the total count and then find the frequency of the whole audio file.
-	If the frequency is greater than 20 then it means the message could be a threat and an alert is sent to the concerned authorities and if it is lesser than 20 then no threat is detected.

After calculating the frequency we display the name of the audio file, the threatening words that are being used, the frequency of the words and whether the audio is a threat or not.

# Sending Email
-	An alert will be sent in the form of an E-mail to the concerned authority so that they can check and take necessary action. 
Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers. 
Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP. 

# Screenshots

## Email


![email](https://user-images.githubusercontent.com/62648110/93502376-46395700-f934-11ea-9845-f307b0296219.png)

## Templates

### home.html

![display](https://user-images.githubusercontent.com/62648110/93503636-fbb8da00-f935-11ea-9c38-a7f574ca71fc.png)

### display.html


![home](https://user-images.githubusercontent.com/62648110/93503896-57836300-f936-11ea-8d8a-198ee01b3fac.png)

