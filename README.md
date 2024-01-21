# Overview 
This project implements pseudorandom LSB (Least Significant Bit) audio steganography in Python,
enabling secure and undetectable embedding of secret messages in audio files. By leveraging pseudorandom number generation for message embedding,
it enhances the security and minimizes the detectability of the encoded data.

# Features
**Pseudorandom LSB Encoding**: Secret messages are encoded into audio files with LSB modification at pseudorandom indices.
**Secure Decoding**: Messages are extracted using the same pseudorandom pattern as in encoding, requiring the original seed.
**Enhanced Security**: Seed-based pseudorandom sequences create unique encoding patterns.
**Compatibility**: Works with various audio formats supported by Python's **wave** module.


# Components
**LSBAudioSteganography**: Base class for audio processing and bit manipulation.
**LSBAudioEncoder**: Subclass for message encoding using pseudorandom LSB.
**LSBAudioDecoder**: Subclass for message decoding, matching the encoding pattern.
