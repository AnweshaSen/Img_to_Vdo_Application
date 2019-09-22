import boto3


class AWSPolly:
    credentials = {}
    client = ''

    def __init__(self):
        self.loadCredentials()
        self.createClient()

    def loadCredentials(self):
        try:
            with open('./.aws-cred/credentials', 'r') as f:
                lines = f.readlines()
                print("AWS Credentials File Found...")
                for line in lines:
                    tokens = line.split('=')
                    if len(tokens) > 1:
                        key = tokens[0]
                        value = tokens[1].split('\n')[0]
                        self.credentials[key] = value
        except:
            print("AWS Credentials File not found... Exiting...")
            exit()


    def createClient(self):
        try:
            self.client = boto3.client(
                'polly',
                aws_access_key_id=self.credentials['aws_access_key_id'],
                aws_secret_access_key=self.credentials['aws_secret_access_key'],
                aws_session_token=self.credentials['aws_session_token'],
                region_name=self.credentials['region_name'],
            )
        except:
            print("Invalid AWS credentials... Exiting...")
            exit()

    def file2audio(self, inputfile, outputFileName):
        try:
            txt = ''
            with open(inputfile, 'r') as f:
                txt = txt + f.read()
            print("Content of txt file: ", txt)
            spoken = self.client.synthesize_speech(Text=txt,
                                                   OutputFormat='mp3',
                                                   VoiceId='Emma')
            with open(outputFileName, 'wb') as f:
                f.write(spoken['AudioStream'].read())
        except:
            print("Could not convert {0} to audio for some reason... Sorry...".format(inputfile))

    def tts(self, inputText, outputFileName):
        try:
            spoken = self.client.synthesize_speech(Text=inputText,
                                                   OutputFormat='mp3',
                                                   VoiceId='Emma')
            print(spoken)
            output = './Data/' + outputFileName + '.mp3'
            with open(output, 'wb') as f:
                f.write(spoken['AudioStream'].read())
        except:
            print("Could not convert {0} to audio for some reason... Sorry...".format(inputText))

if __name__ == '__main__':
    polly = AWSPolly()
    polly.tts("hi", "check")