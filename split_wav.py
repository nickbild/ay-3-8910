from pydub import AudioSegment

# Original wav is 2075 ms.
for t1 in range(0, 2070, 30):
    t2 = t1 + 30

    newAudio = AudioSegment.from_wav("greetings_mono.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export("audio_target/greetings_{0}-{1}.wav".format(t1, t2), format="wav")
    