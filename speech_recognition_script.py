import speech_recognition as sr
from pydub import AudioSegment


if __name__ == "__main__":
    # Load the OGG file
    audio_file = AudioSegment.from_file("test-audio.ogg", format="ogg")

    # Export the audio as a WAV file
    wav_file = "audio.wav"
    audio_file.export(wav_file, format="wav")

    # Initialize the speech recognition engine
    recognizer = sr.Recognizer()

    # Load the WAV file
    with sr.AudioFile(wav_file) as source:
        # Read the audio data from the file
        audio = recognizer.record(source)

        # Perform speech recognition
        text = recognizer.recognize_google(audio, language="uk-UA")

        # Print the recognized text
        print(text)


