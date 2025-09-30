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
import json
from openai import OpenAI  # pyright: ignore[reportMissingImports]


cliente_openai = OpenAI(
    base_url = 'http://127.0.0.1:1234/v1',
    api_key = 'lm-studio'
)

lista_dicionarios = []

for resenha in extract_list_txt:
    response_llm = cliente_openai.chat.completions.create(
        model='google/gemma-3-1b',
        messages=[
            {
                'role': 'user',
                'content': f'''
    Você receberá UMA resenha no formato:

    <ID_DO_USUARIO>$<NOME_DO_USUARIO>$<RESENHA>

    Sua tarefa é transformar essa entrada em UM dicionário JSON no formato:

    {{
    "usuario": {{
        "id": "ID",
        "nome": "Nome do usuário"
    }},
    "resenha": {{
        "original": "texto original em qualquer idioma",
        "pt_br": "tradução para português"
    }},
    "classificacao": "Positiva | Negativa | Neutra"
    }}

    ### Regras:
    - Retorne SOMENTE JSON válido, sem explicações, sem markdown, sem texto extra.
    - Se o texto contiver caracteres especiais, mantenha-os.
    - A tradução ("pt_br") deve ser fiel ao sentido do texto original.
    - A classificação deve ser EXATAMENTE uma destas strings: "Positiva", "Negativa", "Neutra".

    ### Exemplos:

    Entrada:
    53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la dernière mise à jour a tout gâché. Elle a tout oublié.

    Saída:
    {{
    "usuario": {{
        "id": "53409593",
        "nome": "Safoan Riyad"
    }},
    "resenha": {{
        "original": "J'aimais bien ChatGPT. Mais la dernière mise à jour a tout gâché. Elle a tout oublié.",
        "pt_br": "Eu gostava do ChatGPT. Mas a última atualização estragou tudo. Ele esqueceu de tudo."
    }},
    "classificacao": "Negativa"
    }}

    Entrada:
    4549594$Shahidatun jannat$Wonderful app..i just aastonished.. love this app..

    Saída:
    {{
    "usuario": {{
        "id": "4549594",
        "nome": "Shahidatun jannat"
    }},
    "resenha": {{
        "original": "Wonderful app..i just aastonished.. love this app..",
        "pt_br": "Aplicativo maravilhoso.. fiquei impressionada.. adorei este app.."
    }},
    "classificacao": "Positiva"
    }}

    Agora processe a seguinte resenha:
    {resenha}

    '''
            }
        ],
        temperature=0.0,
    )

    resposta_texto = response_llm.choices[0].message.content.replace('```json', '').replace('```', '').strip()

    dicionario = json.loads(resposta_texto)
    lista_dicionarios.append(dicionario)

# print(f"\nTotal de resenhas processadas: {len(lista_dicionarios)}")
# print("\nPrimeira resenha:")
# print(lista_dicionarios[0])




