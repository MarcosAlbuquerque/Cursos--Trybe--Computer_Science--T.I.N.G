import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_description = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    if file_description not in instance.queue:
        instance.enqueue(file_description)

    print(file_description, file=sys.stdout)


def remove(instance):
    if not len(instance):
        print("Não há elementos", file=sys.stdout)
    else:
        print(
            "Arquivo %s removido com sucesso"
            % (instance.dequeue()["nome_do_arquivo"]),
            file=sys.stdout,
        )


def file_metadata(instance, position):
    if position >= len(instance) or position < 0:
        print("Posição inválida", file=sys.stderr)
    else:
        print("%s" % (instance.search(position)), file=sys.stdout)
