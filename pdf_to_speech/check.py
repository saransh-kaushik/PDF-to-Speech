import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")

if __name__ == "__main__":
    list_voices()
