"""
Desafio Final (usando uma IDE):
1 - Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python
2 - Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá "usuário", "resenha original", "resenha_pt", "avaliacao" (Positiva, Negativa, Neutra)
3 - Transformar a resposta do modelo em uma lista de dicionários Python
4 - Criar uma função que, dada uma lista de dicionários, percorre a lista faz 2 coisas:
a) conta a quantidade de avaliações positivas, negativas e neutras;
b) une cada item dessa lista em uma variável do tipo string com algum separador.
Ao final, retorna ambas as coisas.
"""

# 1 - Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python
extract_list_txt = []

with open('resenhas_app_chatgpt.txt', 'r', encoding='utf-8') as file:
    for row in file:
        extract_list_txt.append(row.strip())

# print(extract_list_txt)

# 2 - Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá "usuário", "resenha original", "resenha_pt", "avaliacao" (Positiva, Negativa, Neutra)
# 3 - Transformar a resposta do modelo em uma lista de dicionários Python
import json
from util_desafio import recebe_linha_retorna_json  # pyright: ignore[reportMissingImports]

lista_dicionarios = []  

for resenha in extract_list_txt:
    resenha_json = recebe_linha_retorna_json(resenha).replace('```json', '').replace('```', '').strip()
    resenha_dict = json.loads(resenha_json)
    lista_dicionarios.append(resenha_dict)


print(f"\nTotal de resenhas processadas: {len(lista_dicionarios)}")
print("\nPrimeira resenha:")
print(lista_dicionarios[0])

def contador_avaliacoes(lista_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0

    lista_dicionarios_str = []

    for dicionario in lista_dicionarios:
        if dicionario['classificacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['classificacao'] == 'Negativa':
            contador_negativas += 1
        elif dicionario['classificacao'] == 'Neutra':
            contador_neutras += 1

        lista_dicionarios_str.append(dicionario)

    resenhas_unidas = '####'.join(lista_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, resenhas_unidas

contador_positivas, contador_negativas, contador_neutras, resenhas_unidas = contador_avaliacoes(lista_dicionarios)
print(f"Total de avaliações positivas: {contador_positivas}")
print(f"Total de avaliações negativas: {contador_negativas}")
print(f"Total de avaliações neutras: {contador_neutras}")
print(f"Resenhas unidas: {resenhas_unidas}")