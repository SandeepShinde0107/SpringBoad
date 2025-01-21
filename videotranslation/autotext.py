import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS

def transcribe_audio(audio_path):
    # Load Whisper model and transcribe audio to text
    model = whisper.load_model("medium")
    result = model.transcribe(audio_path)
    text = result.get('text', "").strip()  # Handle cases where text might not exist
    if not text:
        print("Error: No text was transcribed from the audio.")
        return None
    print("Transcribed text:", text)  # Debugging
    return text

def translate_text(text, target_language="hi"):
    if not text:
        print("Error: No text to translate.")
        return None
    
    try:
        # Use deep-translator for translation
        translated_text = GoogleTranslator(source="auto", target=target_language).translate(text)
        print("Translated text:", translated_text)  # Debugging
        return translated_text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

def text_to_audio(text, audio_output_path, lang="hi"):
    if not text:
        print("Error: No text to convert to audio.")
        return
    
    try:
        # Generate audio using gTTS
        tts = gTTS(text=text, lang=lang)
        tts.save(audio_output_path)
        print(f"Audio saved at: {audio_output_path}")
    except Exception as e:
        print(f"Failed to generate audio: {e}")

def process_audio_translation(video_audio_path, target_language, output_audio_path):
    # Step 1: Transcribe the audio to text
    text = transcribe_audio(video_audio_path)
    if not text:
        return
    
    # Step 2: Translate the text to the target language
    translated_text = translate_text(text, target_language)
    if not translated_text:
        return
    
    # Step 3: Convert translated text back to audio
    text_to_audio(translated_text, output_audio_path, lang=target_language)

# Example usage
video_audio_path = "output_audio1.mp3"  # Input audio file
target_language = "hi"  # Target language code (e.g., "hi" for Hindi, "fr" for French)
output_audio_path = "translated_audio.mp3"  # Output audio file path

process_audio_translation(video_audio_path, target_language, output_audio_path)
