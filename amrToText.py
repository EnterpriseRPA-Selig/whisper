import whisper
import torch
import datetime
from pydub import AudioSegment

input_file = input("Enter the input file name (including the extension): ")
output_file = "output.mp3"

sound = AudioSegment.from_file(input_file, format="amr")
sound.export(output_file, format="mp3")
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = whisper.load_model("base.en", device = "cpu")
result = model.transcribe(output_file)
strAppendTitle = str("\n===== Processed at "+ datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " =====\n")
print(strAppendTitle)
print(result["text"])
with open("output.txt", "a") as outputFile:
    outputFile.write(str(strAppendTitle))
    outputFile.write(str(result["text"]))