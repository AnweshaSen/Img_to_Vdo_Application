from polly import AWSPolly
from xlsx import parseXlsx
from img2vid import img2Video, combineVideos
from ui import fileSelector

import os.path
import shutil

def makedir(path):
    if os.path.exists(path):
        return
    os.makedirs(path)

def init():
    pollyObject = AWSPolly()

    sheetPath = fileSelector()
    sheetList = parseXlsx(sheetPath)

    inputDataPath = os.path.dirname(sheetPath)
    inputDataPathContents = os.listdir(inputDataPath)
    # print(inputDataPath)

    outputRootDir = os.path.join(os.getcwd(), "Data")
    outputRootDir = os.path.join(outputRootDir, "OutputVideos")
    makedir(outputRootDir)

    print("Output videos, if any, will be stored in", outputRootDir)

    sheetCount = 0
    for sheet in sheetList:
        sheetCount += 1
        sheetVideosDir = os.path.join(outputRootDir, ("Sheet_" + str(sheetCount)))
        makedir(sheetVideosDir)
        print("===== Processing Sheet Number:", sheetCount, " =====")

        rowNumber = 0
        for row in sheet:
            rowNumber += 1
            print("== Processing row:", rowNumber, " ==")

            tempDir = os.path.join(outputRootDir, "temp")
            makedir(tempDir)

            outputFile = row['outfile']
            inputFileList = row['infile']
            overlay = row['overlay'].split(",")
            transparency = row['trans']
            overlayColor = (int(overlay[0]), int(overlay[1]), int(overlay[2]))
            transparency = 255 * (int(100 - transparency) / 100)
            transparency = int(transparency)


            outputFile = outputFile + '.mp4'
            outputFilePath = os.path.join(sheetVideosDir, outputFile)

            print("    {0} items in row {1}.".format(len(inputFileList), rowNumber))
            itemCount = 0
            partVideoList = []
            for item in inputFileList:
                itemCount += 1
                (img, txt) = item
                print("    Img:", img, "  Txt:", txt, "      PROCESSING...")

                for item in inputDataPathContents:
                    filename = item.split('.')[0]
                    if img == filename:
                        imgPath = item
                    if txt == filename:
                        txtPath = item

                imgPath = os.path.join(inputDataPath, imgPath)
                if not os.path.exists(imgPath):
                    print("XXX  Invalid img path ", imgPath)
                    continue
                txtPath = os.path.join(inputDataPath, txtPath)
                if not os.path.exists(txtPath):
                    print("XXX  Invalid txt path ", txtPath)
                    continue

                outAudioPath = os.path.join(tempDir, ("audiopart" + str(itemCount) + ".mp3"))
                outImgPath = os.path.join(tempDir, img)
                outPartVideoPath = os.path.join(tempDir, ("videopart" + str(itemCount) + ".mp4"))
                shutil.copy(imgPath, outImgPath)
                pollyObject.file2audio(txtPath, outAudioPath)
                print("    Audio file generated:", outAudioPath)
                img2Video(outImgPath, outAudioPath, overlayColor, transparency,outPartVideoPath)
                partVideoList.append(outPartVideoPath)
                print("    == Done...")

            print("    Combining videos...")
            combineVideos(partVideoList, outputFilePath)
            print("    -- ", outputFile, "generated at ", outputFilePath)
            shutil.rmtree(tempDir)

if __name__ == '__main__':
    init()