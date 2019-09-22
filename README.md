# brain-change-proj1

## Project Structure:
1. main.py : Code for the application
2. xlsx.py : Contains code to parse excel sheets
3. img2vid.py : Contains code to convert images to video and other necessary functions
4. polly.py : Contains code to communicate with Amazon Polly

## Dependencies
Make sure FFmpeg is installed and added to Environment Variables.
(https://ffmpeg.org/download.html)

## To Use:
To set up the necessary development environment:
1. Install Python3.
2. Make sure to install FFmpeg and add it to environment variables.
3. Download this project and go to its directory.
4. Run "pip install -r requirements.txt".
5. Add your AWS credentials key in the "/src/.aws-cred/credentials" file.(Just replace the required fields, leave others unchanged.)
6. Run main.py by typing "python main.py"
7. Dialog box fo selecting excel sheet appears. Select an xlsx file. (Make sure all images and text files mentioned in the excel sheet are in the same folder as the excel file itself)
8. Wait for process to complete.

<b>NOTE: Make sure to enter your aws "credentials" in "./src/.aws-credentials/credentials".</b>
