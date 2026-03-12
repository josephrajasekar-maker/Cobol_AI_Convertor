def read_cobol_file(path):

    with open(path) as f:
        code = f.read()

    return code


def split_into_sections(cobol_code):

    sections = {}

    current = "GLOBAL"
    sections[current] = []

    for line in cobol_code.split("\n"):

        line_upper = line.upper()

        if "PROCEDURE DIVISION" in line_upper:
            current = "PROCEDURE"
            sections[current] = []

        elif "DATA DIVISION" in line_upper:
            current = "DATA"
            sections[current] = []

        sections[current].append(line)

    return sections
