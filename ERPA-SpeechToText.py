import whisper
import torch

def main(fileName):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = whisper.load_model("base.en", device = "cpu")
    result = model.transcribe(fileName)
    print(result["text"])
    return result["text"]