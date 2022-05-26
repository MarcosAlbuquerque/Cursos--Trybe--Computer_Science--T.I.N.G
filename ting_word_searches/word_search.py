def exists_word(word, instance):
    files_list = instance.queue
    occurrences = list()
    result = dict()
    for file in files_list:
        lines = file["linhas_do_arquivo"]
        for index, line in enumerate(lines):
            if word in line.lower():
                result["arquivo"] = file["nome_do_arquivo"]
                result["palavra"] = word
                occurrences.append({"linha": index + 1})
    result["ocorrencias"] = occurrences
    return [] if result["ocorrencias"] == [] else [result]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
