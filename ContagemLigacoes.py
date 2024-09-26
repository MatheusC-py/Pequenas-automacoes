def contar_ocorrencias(arquivo, string_busca):
    # Abrir o arquivo em modo de leitura
    with open(arquivo, 'r') as file:
        # Ler o conteúdo do arquivo
        conteudo = file.read()
        # Contar as ocorrências da string
        ocorrencias = conteudo.count(string_busca)
    return ocorrencias

# Exemplo de uso
nome_arquivo = 'TESTE.txt'
string_busca = 'NORMAL'
string_busca2 = 'REDUZIDA'
string_busca3 = 'FLAT'
ocorrencias = contar_ocorrencias(nome_arquivo, string_busca)
ocorrencias2 = contar_ocorrencias(nome_arquivo, string_busca2)
ocorrencias3 = contar_ocorrencias(nome_arquivo, string_busca3)
print(f'A string "{string_busca}" aparece {ocorrencias} vezes no arquivo "{nome_arquivo}".')
print(f'A string "{string_busca2}" aparece {ocorrencias2} vezes no arquivo "{nome_arquivo}".')
print(f'A string "{string_busca3}" aparece {ocorrencias3} vezes no arquivo "{nome_arquivo}".')
print('O total de ligações foi de:', ocorrencias+ocorrencias2+ocorrencias3)