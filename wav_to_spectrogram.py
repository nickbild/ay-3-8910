import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import glob
import sys


# Set input/output directories.
audio_dir = sys.argv[1] # "audio_library"
spectrogram_dir = sys.argv[2] # "audio_library_spectrograms"
noise = sys.argv[3]


def graph_spectrogram(wav_file, noise):
    rate, data = wavfile.read("{1}/{2}/{0}".format(wav_file, audio_dir, noise))
    plt.figure(figsize=(1, 1))
    pxx, freqs, bins, im = plt.specgram(x=data, Fs=rate, noverlap=128, NFFT=256)
    plt.axis('off')
    plt.savefig("{1}/{2}/{0}.jpg".format(wav_file, spectrogram_dir, noise), bbox_inches='tight', dpi=100, pad_inches=0)
    plt.close()

    return


def main():
    files = glob.glob("{0}/{1}/*.wav".format(audio_dir, noise))

    for file in files:
        file_only = file.split("/")[-1]
        graph_spectrogram(file_only, noise)

    return


if __name__ == '__main__':
    main()
