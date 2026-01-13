from moviepy import ImageClip, AudioFileClip

audio = AudioFileClip("voice.mp3")

image = (
    ImageClip("image.png")
    .with_duration(audio.duration)
    .resize(height=1280)
)

video = image.with_audio(audio)

video.write_videofile(
    "final_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)
