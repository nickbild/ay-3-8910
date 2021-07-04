# AY-3-8910 Python Library

A Python library to control a General Instrument AY-3-8910 sound generator from a Raspberry Pi.  To demonstrate the abilities of the chip, I used it to synthesize speech.

<p align="center">
<img src="https://raw.githubusercontent.com/nickbild/ay-3-8910/main/media/breadboard_close_sm.jpg">
</p>

## How It Works

### Library

A demonstration of the core functionalities can be found in [main.py](https://github.com/nickbild/ay-3-8910/blob/main/main.py):

```python
# Initialize sound object with pin definition.
sound = GiSound(d0=8, d1=10, d2=12, d3=16, d4=18, d5=22, d6=24, d7=26, bc1=36, bdir=38, reset=40)

# Set mixer; 1=0N, 0=OFF; (toneA, toneB, toneC, noiseA, noiseB, noiseC)
sound.set_mixer(1, 1, 1, 0, 0, 0)
# Set volume; 1=0N, 0=OFF; (volumeA, volumeB, volumeC)
sound.set_volume(1, 1, 1)
    
for i in range(4096):
    # Set tone value, 0-4096; (toneA, toneB, toneC)
    sound.set_tone(i, i+20, i+40)
    time.sleep(0.001)

# Set noise, 0-31.
sound.set_noise(2)
sound.set_mixer(1, 1, 1, 1, 1, 1)

sound.set_tone(200, 200, 200)

# Define an envelope.
sound.set_envelope_freq(10000)              # 0-65535
sound.set_envelope_shape(0, 1, 1, 0)        # 1=0N, 0=OFF; (continue, attack, alternate, hold)
sound.enable_envelope(1, 1, 1)              # 1=0N, 0=OFF; (chanA, chanB, chanC)

time.sleep(2)
    
# Turn off all sound output.
sound.volume_off()
```

Further details are availble in the [library](https://github.com/nickbild/ay-3-8910/blob/main/gi_sound.py).

### Speech Synthesis

I'm sure there are better ways to go about this (e.g. [Software Automatic Mouth](https://en.wikipedia.org/wiki/Software_Automatic_Mouth)), but I don't really understand them, so I said, "Dammit Jim, I'm a hacker, not a linguist" and came up with my own approach.

I first created a [script](https://github.com/nickbild/ay-3-8910/blob/main/create_library.py) that would systematically make each tone/noise combination that the AY-3-8910 can produce, and record each as a .wav file.  Well, not quite everything possible; I only used 1 channel for tones (3 are available), and I didn't use any envelope functionalities.  The number of conditions would have grown exponentialy if I had done so, and I wasn't sure how much would be gained through their use.

Next, I recorded the [target speech](https://github.com/nickbild/ay-3-8910/blob/main/greetings_mono.wav), "Greetings, Professor Falken."  I split this into 30 millisecond segments.  That seemed like a reasonable length to me for a minimal amount of sound that is perceivable, but I am making things up as I go along, so...

After this, I generated spectrgrams for both the library of AY-3-8910 sounds, and the target sound clips.  Finally, I created another [script](https://github.com/nickbild/ay-3-8910/blob/main/compare_spectrograms.py) that compares each target sound to every available library sound, calcuates the mean squared error of the difference, and then reports back the best match (i.e. lowest MSE).

This results in a sequence of tone/noise segments to run sequentially on the AY-3-8910 to reproduce the target speech.  I did that [here](https://github.com/nickbild/ay-3-8910/blob/main/speech.py).  If you don't have an AY-3-8910 sitting around, you can listen to a .wav of the result [here](https://github.com/nickbild/ay-3-8910/blob/main/greetings_synthesized.wav?raw=true).  It's rough to be sure, but it is distinguishable.  And I don't want it to be too good, or it wouldn't be retro enough...at least that is what I like to tell myself.

While this approach only allows the chip to say one phrase, the next step is fairly obvious.  I could take the same approach to generate sequences to reproduce all of the English phonemes.  From there, I could just string together phonemes as needed to syntesize any arbitrary speech.

## Media

Coming soon.

## Bill of Materials

- 1 x Raspberry Pi 400, or similar
- 1 x AY-3-8910 sound generator
- 1 x 3.5mm jack to USB audio adapter
- 1 x Speaker (3.5mm jack input)
- 1 x 2 MHz crystal oscillator
- 1 x TRRS jack breakout board
- 2 x 1 nF capacitor
- 3 x 10K ohm resistor
- 1 x 1K ohm resistor
- 1 x breadboard
- miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
