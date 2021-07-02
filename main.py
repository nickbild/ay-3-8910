from gi_sound import GiSound
import time
import random


def main():
    sound = GiSound(8, 10, 12, 16, 18, 22, 24, 26, 36, 38, 40)

    sound.set_mixer(1, 0, 0, 0, 0 ,0)
    sound.set_volume(1, 0, 0)
    sound.set_tone_A(100)
    time.sleep(1)

    sound.set_envelope_freq(5000)
    sound.set_envelope_shape(1, 0, 0, 0)
    sound.enable_envelope(1, 0, 0)
    time.sleep(1)

    # sound.set_mixer(1, 1, 1, 0, 0 ,0)
    # sound.set_volume(1, 1, 1)
    
    # for i in range(4096):
    #     sound.set_tone_A(i)
    #     sound.set_tone_B(4095-i)
    #     sound.set_tone_C(random.randint(0, 4095))
    #     time.sleep(0.001)
    
    sound.volume_off()

    return


if __name__ == "__main__":
    main()
