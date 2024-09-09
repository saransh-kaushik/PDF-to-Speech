import tkinter as tk
from tkinter import filedialog, messagebox
from functions import extract_text_from_pdf, save_text_to_file, text_to_speech

def select_pdf_and_convert():
    # Open file dialog to select PDF
    pdf_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF File"
    )
    
    if not pdf_path:
        return

    # Define output paths
    text_output_path = "output.txt"

    try:
        # Extract text from the selected PDF
        text = extract_text_from_pdf(pdf_path)
        save_text_to_file(text, text_output_path)
        
        # Convert text to speech
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        speech_rate = 150  # Adjust this value as needed
        text_to_speech(text_output_path, voice_id=voice_id, rate=speech_rate)
        
        messagebox.showinfo("Success", f"Text extracted and converted to speech successfully.\nOutput saved to {text_output_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    root.title("PDF to Speech Converter")
    root.geometry("300x150")

    button = tk.Button(root, text="Select PDF and Convert to Speech", command=select_pdf_and_convert)
    button.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()


