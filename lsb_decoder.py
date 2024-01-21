import random
import os 
from lsb import LSBAudioSteganography

class LSBAudioDecoder(LSBAudioSteganography):
    """
    A subclass of LSBAudioSteganography to handle the decoding (extraction)
    of a secret message from an audio file using the LSB technique.
    """
    def decode(self, seed_value, message_length):
        """
        decodes the secret message from the audio file by retrieving 
        the least significant bits from the audio data at indices determined by 
        a pseudorandom sequence generated using the given seed value.

        Parameters:
            seed_value (int):The seed value used for pseudorandom number generation.
                            This should be the same seed used in the encoding process.
            message_length (int): The length of the secret message to be decoded.

        Returns:
            str: The decoded secret message.
        """

        # Validate the file path
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Audio file not found.")
          
        # initialize the pseudorandom number generator with the given seed
        random.seed(seed_value)

        if message_length * 8 > len(self.frame_bytes):
            raise ValueError("Message length is too long for the given audio file.")

        # generate the same pseudorandom sequence of indices as used in the encoding
        indices = random.sample(range(len(self.frame_bytes)), message_length * 8)

        # extract the least significant bits from the audio data at the given indices
        extracted_bits = [self.frame_bytes[index] & 1 for index in indices]

        # convert the extracted bits back into the original message
        return self.bits_to_message(extracted_bits)