import moviepy.editor as mp        #pip install moviepy

conversion = mp.VideoFileClip("filename.mp4")
#mention file name here, Note: - file should be already present in the same project directory

audio = conversion.audio   #convertiing it into Audio

audio.write_audiofile("filename.mp3")#Give anyname to Audio file you want

print("Task completed")