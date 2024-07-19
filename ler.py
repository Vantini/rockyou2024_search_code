import sys


def search_in_file(file_path, search_term, block_size=1024 * 1024):
    # Abre o arquivo em modo de leitura binária
    with open(file_path, 'rb') as file:
        # Inicializa variáveis para armazenamento de dados
        buffer = b""
        occurrences = 0

        while True:
            # Lê o próximo bloco do arquivo
            block = file.read(block_size)
            if not block:
                break

            # Adiciona o novo bloco ao buffer
            buffer += block

            # Divide o buffer em linhas
            lines = buffer.split(b'\n')

            # Mantém a última linha no buffer (pode ser uma linha incompleta)
            buffer = lines.pop()

            # Procura o termo de pesquisa em cada linha
            for line in lines:
                if search_term.encode() in line:
                    occurrences += 1
                    print(line.decode(errors='ignore'))  # Exibe a linha encontrada

        # Verifica o buffer final
        if search_term.encode() in buffer:
            occurrences += 1
            print(buffer.decode(errors='ignore'))

        print(f"Ocorrências encontradas: {occurrences}")


# Exemplo de uso
file_path = sys.argv[1]
search_term = sys.argv[2]
search_in_file(file_path, search_term)
