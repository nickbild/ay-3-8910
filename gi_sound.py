import RPi.GPIO as GPIO
import time


class GiSound:
    def __init__(self, d0, d1, d2, d3, d4, d5, d6, d7, bc1, bdir, reset):
        # Set up GPIO pins.

        # Data bus.
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7

        # Control signals.
        self.bc1 = bc1
        self.bdir = bdir
        self.reset = reset

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.d0, GPIO.OUT)
        GPIO.setup(self.d1, GPIO.OUT)
        GPIO.setup(self.d2, GPIO.OUT)
        GPIO.setup(self.d3, GPIO.OUT)
        GPIO.setup(self.d4, GPIO.OUT)
        GPIO.setup(self.d5, GPIO.OUT)
        GPIO.setup(self.d6, GPIO.OUT)
        GPIO.setup(self.d7, GPIO.OUT)
        GPIO.setup(self.bc1, GPIO.OUT)
        GPIO.setup(self.bdir, GPIO.OUT)
        GPIO.setup(self.reset, GPIO.OUT)

        self.reset_toggle()
        self.set_idle()

        return


    ####
    # CONVENIENCE FUNCTIONS
    ####

    def set_address(self, addr):
        self.set_idle()

        b_str = format(addr, '08b')
        GPIO.output(self.d0, int(b_str[7]))
        GPIO.output(self.d1, int(b_str[6]))
        GPIO.output(self.d2, int(b_str[5]))
        GPIO.output(self.d3, int(b_str[4]))
        GPIO.output(self.d4, int(b_str[3]))
        GPIO.output(self.d5, int(b_str[2]))
        GPIO.output(self.d6, int(b_str[1]))
        GPIO.output(self.d7, int(b_str[0]))

        chan_list = (self.bc1, self.bdir)
        GPIO.output(chan_list, GPIO.HIGH)

        self.set_idle()

        return


    def set_data(self, data):
        self.set_idle()

        b_str = format(data, '08b')
        GPIO.output(self.d0, int(b_str[7]))
        GPIO.output(self.d1, int(b_str[6]))
        GPIO.output(self.d2, int(b_str[5]))
        GPIO.output(self.d3, int(b_str[4]))
        GPIO.output(self.d4, int(b_str[3]))
        GPIO.output(self.d5, int(b_str[2]))
        GPIO.output(self.d6, int(b_str[1]))
        GPIO.output(self.d7, int(b_str[0]))

        GPIO.output(self.bdir, GPIO.HIGH)

        self.set_idle()

        return

    def reset_toggle(self):
        GPIO.output(self.reset, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(self.reset, GPIO.LOW)
        time.sleep(0.25)
        GPIO.output(self.reset, GPIO.HIGH)

        return


    def set_idle(self):
        chan_list = (self.bc1, self.bdir)
        GPIO.output(chan_list, GPIO.LOW)

        return

    
    ####
    # VOLUME
    ####

    def volume_off(self):
        self.set_volume(0, 0, 0)

        return


    def set_volume(self, volumeA, volumeB, volumeC):
        self.set_address(8)  # Channel A
        self.set_data(volumeA)
        self.set_address(9)  # Channel B
        self.set_data(volumeB)
        self.set_address(10) # Channel C
        self.set_data(volumeC)

        return

    
    def enable_envelope(self, chanA, chanB, chanC):
        if chanA == 1:
            self.set_address(8)  # Channel A
            self.set_data(31)
        if chanB == 1:
            self.set_address(9)  # Channel B
            self.set_data(31)
        if chanC == 1:
            self.set_address(10) # Channel C
            self.set_data(31)

        return


    ####
    # TONE
    ####

    # Tone is 0-4095.
    def set_tone_A(self, tone):
        tone_bin = format(tone, '012b')
        coarse = int(tone_bin[0:4], 2)
        fine = int(tone_bin[4:12], 2)

        self.set_address(0)
        self.set_data(fine)
        self.set_address(1)
        self.set_data(coarse)

        return


    # Tone is 0-4095.
    def set_tone_B(self, tone):
        tone_bin = format(tone, '012b')
        coarse = int(tone_bin[0:4], 2)
        fine = int(tone_bin[4:12], 2)

        self.set_address(2)
        self.set_data(fine)
        self.set_address(3)
        self.set_data(coarse)

        return


    # Tone is 0-4095.
    def set_tone_C(self, tone):
        tone_bin = format(tone, '012b')
        coarse = int(tone_bin[0:4], 2)
        fine = int(tone_bin[4:12], 2)

        self.set_address(4)
        self.set_data(fine)
        self.set_address(5)
        self.set_data(coarse)

        return


    def set_tone(self, toneA, toneB, toneC):
        self.set_tone_A(toneA)
        self.set_tone_B(toneB)
        self.set_tone_C(toneC)

        return


    ####
    # MIXER
    ####

    def invert_bits(self, bits):
        inverted = ""

        for b in bits:
            if b == "0":
                inverted += "1"
            else:
                inverted += "0"

        return inverted


    def set_mixer(self, toneA, toneB, toneC, noiseA, noiseB, noiseC):
        mixer_val = "00{}{}{}{}{}{}".format(noiseC, noiseB, noiseA, toneC, toneB, toneA)
        # Enable on low signal.
        mixer_val = int(self.invert_bits(mixer_val), 2)

        self.set_address(7)
        self.set_data(mixer_val)

        return


    ####
    # NOISE
    ####

    # Noise is 0-31.
    def set_noise(self, noise):
        self.set_address(6)
        self.set_data(noise)

        return


    #####
    # ENVELOPE
    ####

    # Frequency is 0-65535.
    def set_envelope_freq(self, freq):
        freq_bin = format(freq, '016b')
        coarse = int(freq_bin[0:8], 2)
        fine = int(freq_bin[8:16], 2)

        self.set_address(11)
        self.set_data(fine)
        self.set_address(12)
        self.set_data(coarse)

        return

    
    def set_envelope_shape(self, cont, attack, alternate, hold):
        shape_val = "{}{}{}{}".format(cont, attack, alternate, hold)
        shape_val = int(shape_val, 2)

        self.set_address(13)
        self.set_data(shape_val)

        return
