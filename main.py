import pyttsx3
import os
import openai

openai.organization = 'org-yourorganizationid'
openai.api_key_path = '/path/to/your/apikey.txt'  # Set the path to your API key file

completion = openai.Completion()

def Reply(question):
    prompt = f'Gustavo: \n{question}\nJARVIS: '
    response = completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Gustavo'], max_tokens=200)
    answer = response.choices[0].text.strip()
    print(prompt)
    return answer

""" SPEAKING RATE """
engine = pyttsx3.init()  # object creation
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 155)  # setting up new voice rate


def speak(text):  # allows AI to speak from computer speakers
    engine.say(text)
    engine.runAndWait()

speak("Hello World")

if __name__ == '__main__':
    while True:
        userQuestion = input("Enter a question: ")
        query = Reply(userQuestion)
        print(query)
        speak(query)
        if 'bye' in query:  # If the AI finds 'bye' in the question, then the program will stop
            break
