# AY-3-8910 Python Library

A Python library to control a General Instrument AY-3-8910 sound generator from a Raspberry Pi.  To demonstrate the abilities of the chip, I used it to synthesize speech.

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

### Speech Synthesis

## Media

## Bill of Materials

- 1 x Raspberry Pi 400, or similar
- 1 x AY-3-8910 sound generator
- 1 x 2 MHz crystal oscillator
- 1 x TRRS jack breakout board
- 2 x 1 nF capacitor
- 3 x 10K ohm resistor
- 1 x 1K ohm resistor
- 1 x breadboard
- miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
