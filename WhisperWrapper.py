import whisper as whisper
import datetime
import subprocess
import torch
import wave
import contextlib
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from pyannote.audio import Audio
from pyannote.core import Segment
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding


class WhisperWrapper:
    def __init__(self, model_size):
        self.embedding_model = PretrainedSpeakerEmbedding("speechbrain/spkrec-ecapa-voxceleb", device=torch.device("cpu"))
        self.model = whisper.load_model(model_size)
        self.audio = Audio()

    def transcribe(self, path, num_speakers):
        if path[-3:] != 'wav':
            subprocess.call(['ffmpeg', '-i', path, 'speechtest.wav', '-y'])
            path = 'speechtest.wav'
        result = self.model.transcribe(path)
        segments = result["segments"]
        with contextlib.closing(wave.open(path, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
        embeddings = np.zeros(shape=(len(segments), 192))
        for i, segment in enumerate(segments):
            embeddings[i] = self.segment_embedding(segment, path, duration)
        embeddings = np.nan_to_num(embeddings)
        clustering = AgglomerativeClustering(num_speakers).fit(embeddings)
        labels = clustering.labels_
        for i in range(len(segments)):
            segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)
        f = open("transcript.txt", "w")

        for (i, segment) in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                f.write("\n" + segment["speaker"] + ' ' + str(self.time(segment["start"])) + '\n')
            f.write(segment["text"][1:] + ' ')
        f.close()

    def segment_embedding(self, segment, path, duration):
        start = segment["start"]
        # Whisper overshoots the end timestamp in the last segment
        end = min(duration, segment["end"])
        clip = Segment(start, end)
        waveform, sample_rate = self.audio.crop(path, clip)
        return self.embedding_model(waveform[None])

    @staticmethod
    def time(secs):
        return datetime.timedelta(seconds=round(secs))
