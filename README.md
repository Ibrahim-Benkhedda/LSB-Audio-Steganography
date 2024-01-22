# Overview 
This project implements pseudorandom LSB (Least Significant Bit) audio steganography in Python,
enabling secure and undetectable embedding of secret messages in audio files. By leveraging pseudorandom number generation for message embedding,
it enhances the security and minimizes the detectability of the encoded data.

# Features
- **Pseudorandom LSB Encoding**: Secret messages are encoded into audio files with LSB modification at pseudorandom indices.
- **Secure Decoding**: Messages are extracted using the same pseudorandom pattern as in encoding, requiring the original seed.
- **Enhanced Security**: Seed-based pseudorandom sequences create unique encoding patterns.
- **Compatibility**: Works with various audio formats supported by Python's **wave** module.


# Components
- **LSBAudioSteganography**: Base class for audio processing and bit manipulation.
- **LSBAudioEncoder**: Subclass for message encoding using pseudorandom LSB.
- **LSBAudioDecoder**: Subclass for message decoding, matching the encoding pattern.

# Usage 
```python
from lsb_encoder import LSBAudioEncoder
from lsb_decoder import LSBAudioDecoder

secret_message = "I would tell you a UDP joke, but you might not get it."
audio_filepath = "example_audio.wav"
output_audio_filepath = "embedded_audio.wav"

# For Encoding
encoder = LSBAudioEncoder(audio_filepath)
encoder.encode(secret_message, 42, output_audio_filepath)

# For Decoding
decoder = LSBAudioDecoder(output_audio_filepath)
decoded_message = decoder.decode(42, len(secret_message))
print("Decoded message:", decoded_message)
```

# Dependencies
This project relies on the following external libraries:

- **wave** - Standard Python library for reading and writing WAV files.
- **numpy** (version 1.19 or later) - Used for mathematical operations on audio data.

# Acknowledgement
LSB implementation was inspired from [article](https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3).


