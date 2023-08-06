def encode_string(bytes_to_encode: bytes) -> str:
    output = ''
    for byte in bytes_to_encode:
        binary_byte = int(str(bin(byte))[2:])
        formuled_byte = int(str(binary_byte * byte) + str(byte) + str(len(str(byte))))
        output += str(formuled_byte)[::-1] + ' '
    return output.strip()


def decode_bytes(string_to_decode: str) -> bytes:
    output = b''
    for byte in str(string_to_decode).split(' '):
        reversed_bytes = byte[::-1]
        if int(reversed_bytes) == 1:
            output += int(0).to_bytes(1, 'little')
        else:
            append_number = str(reversed_bytes)[len(str(reversed_bytes)) - int(str(reversed_bytes[-1])) - 1:len(str(reversed_bytes)) - 1]
            cut_length = len(append_number) + 1
            decoded_bin = str(int(str(reversed_bytes)[0:len(reversed_bytes) - cut_length]) // int(append_number))
            data = int(decoded_bin, 2)
            output += data.to_bytes(1, 'little')
    return output
