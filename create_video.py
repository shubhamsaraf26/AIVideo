from moviepy import ImageClip, AudioFileClip

audio = AudioFileClip("voice.mp3")

image = (
    ImageClip("image.png")
    .with_duration(audio.duration)
    .resized(height=1280)   # ✅ MoviePy 2.x
)

video = image.with_audio(audio)

video.write_videofile(
    "final_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)
