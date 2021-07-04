from gi_sound import GiSound
import time
import sounddevice as sd
from scipy.io.wavfile import write
import os
import sys


def record_wav(wav_output_filename):
    fs = 44100
    seconds = 0.03

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write(wav_output_filename, fs, myrecording)

    return


def main():
    sound = GiSound(8, 10, 12, 16, 18, 22, 24, 26, 36, 38, 40)

    sound.set_mixer(1, 1, 1, 0, 0 ,0)
    sound.set_volume(3, 3, 3)
    
    noise = int(sys.argv[1])
    if noise > 0:
        sound.set_mixer(1, 1, 1, 1, 1 ,1)
        sound.set_noise(noise)
    for tone in range(4096):
        sound.set_tone(tone, tone, tone)
        time.sleep(0.005)
        record_wav("audio_library/{1}/tone-{0}_noise-{1}.wav".format(tone, noise))
        time.sleep(0.032)
    
    sound.volume_off()

    return


if __name__ == "__main__":
    main()