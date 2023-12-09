def main():
    # Choose the input filename
    document = 'input.txt'

    # Read the document and get the lines
    lines = read_calibration_document(document)

    # For each line in the document, concatenate the first and last digits
    # to find the calibration value then sum all calibration values
    total = 0
    for line in lines:
        calibration_value = find_calibration_value(line)
        total += calibration_value

    # Print and return the sum of all calibration values
    print(total)

    return total

def read_calibration_document(document):
    with open(document, 'r') as file:
        lines = file.readlines()

    return lines

def find_calibration_value(line):
    spelled_digits = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]

    # Initialize an empty list to store all the digits found
    digits = []

    # Initialize an empty string to store characters
    s = ''

    # For each char of the line
    for char in line:
        # If the character is a digit
        # add it to the digits list and reset the string
        if char.isdigit():
            digits.append(char)
            s = ''

        # If the character is not a digit
        # add it to the temporary string
        else:
            s = ''.join((s, char))

            # If the string contains a spelled digits
            # add its index (which equals its value) to the digits list
            for number in spelled_digits:
                if number in s:
                    index = spelled_digits.index(number)
                    digits.append(str(index))

                    # Reset the string
                    # but keep the last character
                    # as it might be the start of another spelled digit
                    s = number[-1]

    # Concatenate the first and last found digits
    n = digits[0] + digits[-1]

    # Convert the concatenated digits to an integer
    calibration_value = int(n)

    return calibration_value

if __name__ == '__main__':
    main()
