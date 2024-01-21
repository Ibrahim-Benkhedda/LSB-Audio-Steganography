import random
import os
from lsb import LSBAudioSteganography

class LSBAudioEncoder(LSBAudioSteganography):
    """
    A subclass of LSBAudioSteganography to handle the encoding (embedding)
    of a secret message into an audio file using the LSB technique.
    """
    def encode(self, secret_message, seed_value, output_filepath):
        """
        Embeds a secret message into the audio file by altering 
        the least significant bits of the audio data according to a pseudorandom 
        sequence determined by the given seed value.

        Parameters:
            secret_message (str): The secret message to be encoded in the audio file.
            seed_value (int): The seed value for pseudorandom number generation, 
                        used to determine the indices in the audio data, 
                        where the message bits will be embedded.
            output_filepath (str): The path where the modified audio file will be saved.

        """
        # validate the file path
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Input audio file not found.")
        
        # convert the secret message to a list of bits
        message_bits = self.message_to_bits(secret_message)

        # Check if the audio file can hold the message
        if len(message_bits) > len(self.frame_bytes):
            raise ValueError("Secret message is too long for the given audio file.")

        # initialize the pseudorandom number generator with the given seed
        random.seed(seed_value)

        # generate a pseudorandom sequence of unique indices in the audio data
        indices = random.sample(range(len(self.frame_bytes)), len(message_bits))

        # embed each bit of the secret message into the least significant bit
        # of the audio data at the pseudorandomly determined indices
        for index, bit in zip(indices, message_bits):
            self.frame_bytes[index] = (self.frame_bytes[index] & 254) | int(bit)

        # write the modified audio data with the embedded message to the output file
        self.write_audio_file(output_filepath, bytes(self.frame_bytes))