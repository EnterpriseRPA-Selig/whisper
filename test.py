import whisper
import torch
import datetime

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = whisper.load_model("base.en", device = "cpu")
result = model.transcribe("news_3mins.mp3")
strAppendTitle = str("\n===== Processed at "+ datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " =====\n")
print(strAppendTitle)
print(result["text"])
with open("output.txt", "a") as outputFile:
    outputFile.write(str(strAppendTitle))
    outputFile.write(str(result["text"]))