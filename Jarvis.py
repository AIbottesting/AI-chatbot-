#importing libraries
import speech_recognition as sr
import pyttsx3
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import random

#initializing the engine
engine = pyttsx3.init()

#setting Jarvis's voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Create a class for the AI
class AI_Friend:
    # Initialize the AI with a corpus of text
    def __init__(self, corpus):
        self.corpus = corpus
        self.words = word_tokenize(self.corpus)
        self.sentences = sent_tokenize(self.corpus)
        self.word_freq = nltk.FreqDist(self.words)
        self.word_features = list(self.word_freq.keys())
    
    # Train the AI on new text
def train(self, new_text):
    self.words.extend(word_tokenize(new_text))
    self.sentences.extend(sent_tokenize(new_text))
    self.word_freq = nltk.FreqDist(self.words)
    self.word_features = list(self.word_freq.keys())
    
#defining the function that will be used to recognize speech
def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

# try recognizing the speech in the recording
# if a RequestError or UnknownValueError exception is caught,
#     update the response object accordingly
try:
    response["transcription"] = recognizer.recognize_google(audio)
except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"
except sr.UnknownValueError:
    # speech was unintelligible
    response["error"] = "Unable to recognize speech"

# return the response object
print(response)

#defining the function that will be used to scan documents
def scan_documents(folder):
    #get all the files in the folder
    files = os.listdir(folder)
    #initialize a string to store all the text
    text = ""
    #iterate through all the files
    for file in files:
        #open the file
        f = open(os.path.join(folder, file), "r")
        #read the content
        content = f.read()
        #add the content to the text
        text += content
        #close the file
        f.close()
    #return the text
    return text

#defining the main function
def main():
    #initialize the recognizer
    recognizer = sr.Recognizer()
#initialize the microphone
microphone = sr.Microphone()
#initialize the AI
ai = AI_Friend("")
#scan the documents
text = scan_documents("C:/Users/Mlaptop/Documents/Jarvis Training")
#train the AI
ai.train(text)
#announce Jarvis
engine.say("Hello Sir, how can I help you?")
engine.runAndWait()
#listen for commands
while True:
    #listen for the command
    command = recognize_speech_from_mic(recognizer, microphone)
    #if the command is recognized
    if command["transcription"]:
        #if the command is "scan documents"
        if command["transcription"] == "scan documents":
            #scan the documents
            text = scan_documents("C:/Users/Mlaptop/Documents/Jarvis Training")
            #train the AI
            ai.train(text)
        #if the command is "Jarvis"
        elif command["transcription"] == "Jarvis":
            #generate a response
            response = ai.gener
#say the response
engine.say(response)
engine.runAndWait()			