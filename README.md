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

## For later
* [AWS EC2 with GPU](https://pyimagesearch.com/2014/10/13/deep-learning-amazon-ec2-gpu-python-nolearn/)
* [How to train ChatGPT with your own data](https://writesonic.com/blog/how-to-train-chatgpt-own-data/#:~:text=In%20order%20to%20import%20your,your%20version%20of%20customizable%20ChatGPT.)
* [MPT-30B](https://huggingface.co/mosaicml/mpt-30b)
* [OpenAI API Overview](https://platform.openai.com/overview)