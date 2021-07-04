from gi_sound import GiSound
import time


def main():
    sound = GiSound(8, 10, 12, 16, 18, 22, 24, 26, 36, 38, 40)

    sound.set_mixer(1, 1, 1, 0, 0 ,0)
    sound.set_volume(1, 1, 1)
    
    for i in range(4096):
        sound.set_tone(i, i+20, i+40)
        time.sleep(0.001)
    
    sound.volume_off()

    return


if __name__ == "__main__":
    main()
