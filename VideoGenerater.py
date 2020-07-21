from moviepy.editor import *
import json

def videoGenerater(isl_string):
    clips = []
    # print(isl_string)
    l = isl_string.split()
    for i in l:
        clips.append(VideoFileClip("static/"+i+".mp4"))
    clips.append(VideoFileClip("static/isl.mp4"))
    result = concatenate_videoclips(clips)
    result.write_videofile("static/result.mp4")


def fileGenerater(englishString, islString):
    f = open("static/data.txt", "w")
    f.seek(0)
    f.truncate()
    data = {"input": englishString, "output": islString}
    data = json.dumps(data)
    f.write(str(data))
    f.close()