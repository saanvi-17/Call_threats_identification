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
	import speech_recognition as sr           
-	used for speech recognition

	from googletrans import Translator        
-	For translation

	import re             
-	for regular expressions 

	import nltk                               
-	for natural language processing

	from nltk.tokenize import word_tokenize   
-	 to tokenize a string 

	import spacy                             
-	 for stopwords

	import pandas as pd        
-	for data analysis

	import smtplib   
-	sending email

	from email.message import EmailMessage

	from flask import Flask, render_template, url_for, flash, request, redirect, send_from_directory

	import os

	from werkzeug.utils import secure_filename
