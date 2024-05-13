import json
import numpy as np
import cv2
import librosa
import numpy as np
import matplotlib.pyplot as plt
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)
mate=load_json('/home/ubuntu/demos/multimodal_demo/others/ESC_zero_shot.json')
for line in mate:
    idx=line['questionId']
    wav_path=f'/home/ubuntu/demos/multimodal_demo/others/ESC-50-master/audio/{idx}.wav'

    y, sr = librosa.load(wav_path)
    D = np.abs(librosa.stft(y)) ** 2  # stft频谱
    S = librosa.feature.melspectrogram(S=D)  # 使用stft频谱求Mel频谱

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                            y_axis='mel', fmax=8000, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    plt.savefig(f'/home/ubuntu/demos/multimodal_demo/others/wav_img/{idx}.jpg')

