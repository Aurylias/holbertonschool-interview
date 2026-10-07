"""Module for checking if the given data represents a valid UTF-8 encoding"""

def validUTF8(data):
    remaining = 0

    for num in data:
        byte = num & 0xFF # 8 least significant bite

        if remaining == 0:
            if byte >> 7 == 0b0:        # 0xxxxxxx -> 1-byte char
                continue
            elif byte >> 5 == 0b110:    # 110xxxxx -> 2-byte char
                remaining = 1
            elif byte >> 4 == 0b1110:   # 1110xxxx -> 3-byte char
                remaining = 2
            elif byte >> 3 == 0b11110:  # 11110xxx -> 4-byte char
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1
    
    return remaining == 0
