import os

from cobol_parser import read_cobol_file
from llm_translator import translate_cobol_to_python


def convert_program(input_file):

    print("Reading COBOL program...")

    cobol_code = read_cobol_file(input_file)

    print("Sending to AI for conversion...")

    python_code = translate_cobol_to_python(cobol_code)

    output_file = input_file.replace(".cbl", ".py")

    output_path = os.path.join("output", output_file)

    with open(output_path, "w") as f:
        f.write(python_code)

    print("Python program generated:")
    print(output_path)


def main():

    cobol_program = "sample_cobol/customer_batch.cbl"

    convert_program(cobol_program)


if __name__ == "__main__":
    main()
