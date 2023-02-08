# importing libraries
import speech_recognition as sr
import pyttsx3
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import random

# initializing the engine
engine = pyttsx3.init()

# setting Jarvis's voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# set the rate of speech
engine.setProperty('rate', 150)

# give the AI program a name 
name = "Jarvis"

# initialize the microphone
microphone = sr.Microphone()
# initialize the AI
ai = AI_Friend("")
# scan the documents
text = scan_documents("C:/Users/Mlaptop/Documents/Jarvis Training")
# train the AI
ai.train(text)
# announce Jarvis
engine.say("Hello Sir, how can I help you?")
engine.runAndWait()
# listen for commands
while True:
    # listen for the command
    command = recognize_speech_from_mic(recognizer, microphone)
    # if the command is recognized
    if command["transcription"]:
        # if the command is "scan documents"
        if command["transcription"] == "scan documents":
            # scan the documents
            text = scan_documents("C:/Users/Mlaptop/Documents/Jarvis Training")
            # train the AI
            ai.train(text)
        # if the command is "Jarvis"
        elif command["transcription"] == "Jarvis":
            # generate a response
            response = ai.gener
# say the response
engine.say(response)
engine.runAndWait()

# defining the function that will be used to recognize speech
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


# defining the function that will be used to scan documents
def scan_documents(folder):
    # get all the files in the folder
    files = os.listdir(folder)
    # initialize a string to store all the text
    text = ""
    # iterate through all the files
    for file in files:
        # open the file
        f = open(os.path.join(folder, file), "r")
        # read the content
        content = f.read()
        # add the content to the text
        text += content
        # close the file
        f.close()
    # return the text
    return text


# defining the main function
def main():
    # initialize the recognizer
    recognizer = sr.Recognizer()


# scanning documents
def scan_documents():
    documents = []
    for document in os.listdir('C:\\Users\\Mlaptop\\Documents\\Jarvis Training'):
        if document.endswith('.txt'):
            documents.append(document)
    return documents


# converting text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# listening to the user
def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try.


# processing audio
try:
    said = r.recognize_google(audio)
except Exception as e:
    print("Exception: " + str(e))

return said.lower()

# main loop
while True:
    text = listen()
    documents = scan_documents()

    # processing the users text 
    if "scan documents" in text:
        for document in documents:
            with open(document, 'r') as file:
                data = file.read()
                nltk.word_tokenize(data)
                speak("Scanning document, " + document)
    elif "hello jarvis" in text:
        speak("Hello Sir, how can I help you?")
    elif "goodbye" in text:
        speak("Goodbye Sir, it was nice talking to you")
        break
    else:
        speak("I'm sorry, I didn't understand that")


# processing user inputs
if text != '':
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    subjects = [word for word, pos in tagged if pos in ['NN', 'NNP']]
    verbs = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]

for subject in subjects:
    for verb in verbs:
        response = subject + " " + verb
        speak(response)


# storing conversation
conversation_log = open("conversation_log.txt", "a+")
conversation_log.write("User: " + text + "\n")
conversation_log.write("Jarvis: " + response + "\n")
conversation_log.close()


# learning from conversation 
with open("conversation_log.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-2:]:
        if "User" in line:
            pattern = re.compile(r'User:(.*)')
            user = pattern.search(line).group(1)
        elif "Jarvis" in line:
            pattern = re.compile(r'Jarvis:(.*)')
            jarvis = pattern.search(line).group(1)
    if user and jarvis:
        learn_from_conversation(user, jarvis)


# function to learn from conversation
def learn_from_conversation(user, jarvis):
    words = nltk.word_tokenize(user)
    tagged = nltk.pos_tag(words)
    subjects = [word for word, pos in tagged if pos in ['NN', 'NNP']]
    verbs = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
    patterns = []

    for subject in subjects:
        for verb in verbs:
            pattern = {'subject': subject, 'verb': verb, 'response': jarvis}
            patterns.append(pattern)

            # write patterns to file 
    with open("patterns.json", "a") as f:
        json.dump(patterns, f)


# function to answer questions
def answer_questions(text):
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    subjects = [word for word, pos in tagged if pos in ['NN', 'NNP']]
    verbs = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
    response = None

    with open("patterns.json", "r") as f:
        patterns = json.load(f)
        for pattern in patterns:
            if pattern['subject'] in subjects and pattern['verb'] in verbs:
                response = pattern['response']
    return response


# asking questions
if response is None:
    speak("I'm sorry, I don't understand")
    question = listen()
    response = answer_questions(question)
    if response is not None:
        speak(response)

# looping the program
while True:
    text = listen()
    response = answer_questions(text)
    if response is not None:
        speak(response)
    else:
        speak("I'm sorry, I don't understand")


# saving conversation
conversation_log = open("conversation_log.txt", "a+")
conversation_log.write("User: " + text + "\n")
conversation_log.write("Jarvis: " + response + "\n")
conversation_log.close()


# learning from conversation 
with open("conversation_log.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-2:]:
        if "User" in line:
            pattern = re.compile(r'User:(.*)')
            user = pattern.search(line).group(1)
        elif "Jarvis" in line:
            pattern = re.compile(r'Jarvis:(.*)')
            jarvis = pattern.search(line).group(1)
    if user and jarvis:
        learn_from_conversation(user, jarvis)
        

# ending the program
if "goodbye" in text:
    speak("Goodbye Sir, it was nice talking to you")
    break

# exiting program
exit()

# finalizing program
speak("Goodbye Sir, it was nice talking to you. Have a nice day!")

# finalizing code
engine.stop()

# program complete
print("Jarvis AI Program is now complete.")

# finalizing code
engine.stop()

