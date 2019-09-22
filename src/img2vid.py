import os
from PIL import Image


def img2Video(imgPath, audioPath, rgbColor, opacity, outPath):
    img = Image.open(imgPath)
    rgba = rgbColor + (opacity,)
    overlay = Image.new('RGBA', (img.size), rgba)
    img.paste(overlay, (0, 0), overlay)
    temp = imgPath.split(".")
    print(temp)
    out = temp[0] + "_temp.jpg"
    print(out)
    img.save(out)

    print("Converting \"{0}\" to \"{1}\"  ...".format(out, outPath))
    command = "ffmpeg -loop 1 -y -i " + out + " -i " + audioPath + " -c:v libx264 -shortest -pix_fmt yuv420p " + outPath
    #command2 = "ffmpeg -i " + outPath + " -f lavfi -i " + color=s=1280x720:c=red + " -filter_complex " + " blend=shortest=1:all_mode=overlay:all_opacity=0.7" + output.mp4

    try:
        os.system(command)
        print("Done...")

        #print("Adding Color overlay to the video.....")
        #print(command2)
        #print("Done updating images....")

    except:
        print("Unable to run FFmpeg. Make sure FFmpeg is installed and added to environment variable...")
        exit()


def combineVideos(listOfVideos, outputPath):
    vid = ''
    filter = ''
    count = -1
    for i in listOfVideos:
        count += 1
        vid = vid + " -i " + i
        filter = filter + "[{0}:v:0] [{1}:a:0] ".format(count, count)
    filter = filter + "concat=n=" + str(count + 1) + ":v=1:a=1 [v] [a]"

    command = "ffmpeg -y" + vid + " -filter_complex \"" + filter + "\" -map \"[v]\" -map \"[a]\" " + outputPath
    print(command)
    try:
        os.system(command)
        print("Combined...")
    except:
        print("Unable to run FFmpeg. Make sure FFmpeg is installed and added to environment variable...")
        exit()


if __name__ == '__main__':
    dataPath = os.path.join(os.getcwd(), "Data")
    imgPath = os.path.join(dataPath, "img.jpg")
    audioPath = os.path.join(dataPath, "test.mp3")
    output = os.path.join(dataPath, "out.mp4")
    duration = 30
    img2Video(imgPath, audioPath, (250, 13, 13), 100, output)
    outpath = os.path.join(dataPath, "outfile.mp4")
    combineVideos([os.path.join(dataPath, "out.mp4"), os.path.join(dataPath, "out2.mp4"), os.path.join(dataPath, "out3.mp4")], outpath)