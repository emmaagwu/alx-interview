#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    i = 0
    n = len(data)

    while i < n:
        byte = data[i]

        # Determine the number of bytes in the UTF-8 character
        if byte & 0b10000000 == 0:
            num_bytes = 1
        elif byte & 0b11100000 == 0b11000000:
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False

        # Check if there are enough bytes left
        if i + num_bytes > n:
            return False

        # Verify the continuation bytes
        for j in range(1, num_bytes):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False

        # Move to the next character
        i += num_bytes

    return True
