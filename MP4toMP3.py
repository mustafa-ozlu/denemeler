#from email.mime import audio
import moviepy
import moviepy.editor

video=moviepy.editor.VideoFileClip("film.mp4")
audio=video.audio
audio.write_audiofile("audio.mp3")
