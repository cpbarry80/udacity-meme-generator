# Meme Generator Overview
this project pulls text from a pdf, csv, docx, and txt files and uses that text in conjuction with an image to create a meme. default behavior is a random selection of the already provided images and qoutes. there are command line args as well as a flask web app to access this. 

## Setup
pip install -r requirements.txt
note `pdftotext` needs to be installed seperatley too but the exe is already included in the project root here
once you do those two things run app.py and then navigate to /127.0.0.1:5000/

### Quote Engine Module
This parses the aforementioned file types and creates a qoute model for those which is really just a strucutured way of showing a qoute clearly with the context (body) and the author. 

### Meme Generator Module
This puts the qoute on the image to create the meme
