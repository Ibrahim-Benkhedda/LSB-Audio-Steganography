import wave

class LSBAudioSteganography:
    """
    A class to implement LSB (Least Significant Bit) audio steganography.
    
    This class provides methods to encode a secret message into an audio file
    and decode it from the audio file using the LSB technique.
    
    Attributes:
        filepath (str): The path to the audio file for steganography.
        frame_bytes (bytearray): The byte array of the audio frames.
        params (tuple): Parameters of the audio file.
    """

    def __init__(self, filepath):
        """
        Initializes the LSBAudioSteganography class with the given audio file.
        
        Paramters:
            filepath (str): The path to the audio file.
        """
        self.filepath = filepath
        self.frame_bytes = None
        self.read_audio_file()

    def read_audio_file(self):
        """
        Reads the audio file and stores its frames in a byte array.
        """
        
        # open the audio file and read frames
        with wave.open(self.filepath, 'rb') as audio_file:
            # convert audio frames to a mutable byte array
            self.frame_bytes = bytearray(list(audio_file.readframes(audio_file.getnframes())))
            # store audio file parameters
            self.params = audio_file.getparams()

    def write_audio_file(self, output_filepath, audio_data):
        """
        writes modified audio data to a new file.
        
        Paramters:
            output_filepath (str): Path to the output audio file.
            audio_data (bytes): Modified audio data to be written.
        """

        # create the output file and write the modified frames
        with wave.open(output_filepath, 'wb') as out_file:
            out_file.setparams(self.params)
            out_file.writeframes(audio_data)

    @staticmethod
    def message_to_bits(message):
        """
        converts a text message to a list of bits.
        
        Parameters:
            message (str): The text message to convert.
            
        Returns:
            list: A list of bits representing the message.
        """

        # Convert each character to its ASCII binary representation
        return [bit for char in message for bit in bin(ord(char))[2:].zfill(8)]

    @staticmethod
    def bits_to_message(bits):
        """
        converts a list of bits back to a text message.
        
        Parameters:
            bits (list): The list of bits to convert.
            
        Returns:
            str: The decoded text message.
        """
        message = ""
        # convert each 8-bit chunk back to a character
        for i in range(0, len(bits), 8):
            byte_as_str = ''.join(str(bit) for bit in bits[i:i+8])
            message += chr(int(byte_as_str, 2))

        return message