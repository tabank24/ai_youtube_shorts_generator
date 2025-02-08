import whisper
import moviepy.editor as mp

def extract_highlights(video_path):
    model = whisper.load_model("base")
    audio = mp.VideoFileClip(video_path).audio.write_audiofile("audio.wav")
    result = model.transcribe("audio.wav")
    print("Transcription:", result["text"])

extract_highlights("example.mp4")
