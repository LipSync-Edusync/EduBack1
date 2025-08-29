import torch
from vakyansh.tts.glow.base import TextToMel, MelToWav
from vakyansh.utils.text import clean_text
import torchaudio
import os

GLOWTTS_PATH = "models/hindi_male/glowtts/hifi-tts_best.pth"
HIFIGAN_PATH = "models/hindi_male/hifigan/g_02500000"
CONFIG_PATH = "models/hindi_male/config.json"

device = "cuda" if torch.cuda.is_available() else "cpu"

text2mel = TextToMel(glow_path=GLOWTTS_PATH, config_path=CONFIG_PATH).to(device).eval()

mel2wav = MelToWav(hifigan_path=HIFIGAN_PATH, config_path=CONFIG_PATH).to(device).eval()

def synthesize(text, output_wav="output.wav"):
    tokens = clean_text(text, language="hi") 

    with torch.no_grad():
        mel = text2mel.generate(tokens.to(device).unsqueeze(0))

        wav = mel2wav.generate(mel)

    torchaudio.save(output_wav, wav.cpu(), 22050)
    print(f"Saved: {output_wav}")