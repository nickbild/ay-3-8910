import gi_sound
import time


def main():
    sound = gi_sound.GiSound(8, 10, 12, 16, 18, 22, 24, 26, 36, 38, 40)
    
    sound.set_mixer(1, 1, 0, 0, 0 ,0)
    sound.set_volume(1, 1, 0)
    
    for i in range(4096):
        sound.set_tone_A(i)
        sound.set_tone_B(4095-i)
        time.sleep(0.001)
    
    sound.volume_off()

    return


if __name__ == "__main__":
    main()
