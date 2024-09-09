import fitz  # PyMuPDF
import pyttsx3

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text("text")

    return text

def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)



def text_to_speech(text_path, voice_id=None , rate = 150):
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    engine = pyttsx3.init()

    # Set the voice if provided
    if voice_id:
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.id == voice_id:
                engine.setProperty('voice', voice.id)
                break

    # Set the speech rate (words per minute)
    engine.setProperty('rate', rate)

    engine.say(text)
    engine.runAndWait()