from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import messagebox

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter text")
        return

    try:
        tts = gTTS(text=text, lang="en", slow=False)
        audio_file = "speech.mp3"
        tts.save(audio_file)
        messagebox.showinfo("Success", "Speech saved successfully! Click 'Play' to hear it.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def play_audio():
    try:
        playsound("speech.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to play audio: {e}")

# GUI Setup
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("400x300")
root.configure(bg="#2C3E50")

tk.Label(root, text="Enter Text:", font=("Arial", 12),fg="white",bg="#2C3E50").pack(pady=5)

text_entry = tk.Text(root, height=5, width=40,bg="#ECF0F1",fg="black")
text_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Speech", command=text_to_speech, font=("Arial", 12),bg="#3498DB",fg="white")
convert_button.pack(pady=5)

play_button = tk.Button(root, text="Play", command=play_audio, font=("Arial", 12),bg="#2ECC71",fg="white")
play_button.pack(pady=5)

root.mainloop()