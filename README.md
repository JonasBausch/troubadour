# TroubAIdour
An AI assisted collector of your adventures!

## Local Setup
When running the project in PyCharm, either install the below packages via pycharm package manager or via command line.
```commandline
pip install -q git+https://github.com/openai/whisper.git
pip install -q git+https://github.com/pyannote/pyannote-audio
```
The current prototype relies on an mp3 file called `speechtest.mp3`. Modify `main.py` to change file name and number of speakers.

## Credits
* [whisper.ai](https://github.com/openai/whisper)
* [Dwarkesh Patel](https://colab.research.google.com/drive/1V-Bt5Hm2kjaDb4P1RyMSswsDKyrzc2-3?usp=sharing#scrollTo=O0_tup8RAyBy)