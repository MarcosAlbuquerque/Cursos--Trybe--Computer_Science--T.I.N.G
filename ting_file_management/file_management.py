import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file) as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("Arquivo %s não encontrado" % (path_file), file=sys.stderr)


"""
[references]
------------
https://www.w3schools.com/python/python_ref_string.asp
https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
"""
