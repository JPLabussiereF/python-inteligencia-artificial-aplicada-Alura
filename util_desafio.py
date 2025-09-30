
import json
from openai import OpenAI  # pyright: ignore[reportMissingImports]


cliente_openai = OpenAI(
    base_url = 'http://127.0.0.1:1234/v1',
    api_key = 'lm-studio'
)

def recebe_linha_retorna_json(linha):
    lista_dicionarios = []

for resenha in extract_list_txt:
    response_llm = cliente_openai.chat.completions.create(
        model='google/gemma-3-1b',
        messages=[
            {
                'role': 'system',
                'content': '''
                Você é um especialista em análise de dados e conversão de dados para JSON.
                Você recebera uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
                Responda extamente o que o usuário pedir 
                '''
            },
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