hex_file: str = "data/hexadecimal.txt"
ascii_file: str = "compare/ascii.csv"
output_file: str = "out/program.py"

ascii_table: dict[str, str] = {}

with open(ascii_file, "r") as file:
    for line in file:
        line: str = line.strip()

        if line == "":
            continue

        parts: list[str] = line.split(",")

        if len(parts) < 3:
            continue

        decimal: str = parts[0]
        hexadecimal: str = parts[1]
        character: str = parts[2]

        ascii_table[hexadecimal.upper()] = character


with open(hex_file, "r") as file:
    hex_data: list[str] = file.readlines()


decoded: str = ""

for line in hex_data:
    hexadecimal: str = line.strip().upper()

    if hexadecimal == "":
        continue

    if hexadecimal in ascii_table:
        character: str = ascii_table[hexadecimal]

        if character == "SPACE":
            character = " "

        decoded += character

    else:
        decoded += "?"


with open(output_file, "w") as file:
    file.write(decoded)


print("Decoding complete!")
print("Saved to:", output_file)