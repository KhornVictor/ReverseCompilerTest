hex_digits = "0123456789ABCDEF"

with open("binary.txt", "r") as input_file:
    with open("data/hexadecimal.txt", "w") as output_file:
        for line in input_file:
            binary = line.strip()

            if binary == "":
                continue

            value = 0

            for bit in binary:
                if bit == "0":
                    value = value * 2
                elif bit == "1":
                    value = value * 2 + 1
                else:
                    print("Invalid binary:", binary)
                    continue

            high = value // 16
            low = value % 16

            hexadecimal = hex_digits[high] + hex_digits[low]
            output_file.write(hexadecimal + "\n")

print("Done! Hexadecimal saved to hexadecimal.txt")