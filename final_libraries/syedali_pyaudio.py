def play_all():
    # create an audio object
    pya = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = pya.open(
                format = pyaudio.paInt16,
                channels = 1,
                rate = np.int16(np.round(orig_rate)),
                output = True)

    # read data (based on the chunk size)
    audata = orig_au.astype(np.int16).tostring()
    stream.write(audata)

    # cleanup stuff.
    stream.close()    
    pya.terminate() 