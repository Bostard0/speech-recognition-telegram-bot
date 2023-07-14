import speech_recognition as sr
from pydub import AudioSegment


def audio_to_text(audio):
    audio_file = AudioSegment.from_file(audio, format="ogg")
    wav_file = "audio.wav"
    audio_file.export(wav_file, format="wav")
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="uk-UA")

        return text
