import sys
import bibtexparser as btp
import re
import pathlib as pl

if __name__ == '__main__':
    words_path = pl.Path(sys.argv[0]).parent / "dictionary.txt"

    with open(words_path, "r") as words_file:
        words = [line.rstrip() for line in words_file]

    if len(sys.argv) != 2:
        print("Error: Please provide a single argument: the input_path to the .bib file to fix.")
        exit(1)

    input_path = pl.Path(sys.argv[1])

    output_path = input_path.parent / ("{}_fixed".format(input_path.stem) + input_path.suffix)

    library = btp.parse_file(input_path)

    for entry in library.entries:
        for field in entry.fields:
            if not isinstance(field.value, str):
                continue

            field.value = "{{{}}}".format(field.value)

        if not isinstance(entry.fields_dict["title"].value, str):
            continue

        if "title" not in entry.fields_dict:
            continue

        for word in words:
            entry.fields_dict["title"].value = re.sub(r"((?!\{)" + word + r"(?!\}))|((?<!\{)" + word + r"(?=\}))", "{{{}}}".format(word), entry.fields_dict["title"].value)

    modified: str = btp.writer.write(library, btp.writer.BibtexFormat())

    with open(output_path, "w") as file:
        res: int = file.write(modified)
        print("File written; {}.".format(res))



