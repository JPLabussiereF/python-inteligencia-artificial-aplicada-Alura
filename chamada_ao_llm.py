from openai import OpenAI  # pyright: ignore[reportMissingImports]

cliente_openai = OpenAI(
    base_url = 'http://127.0.0.1:1234/v1',
    api_key = 'lm-studio'
)

response_llm = cliente_openai.chat.completions.create(
    model='google/gemma-3-1b',
    messages=[
        {
            'role': 'system', 
            'content': 'O seu nome é "EBinh.ia"! Um assistente de IA da empresa "Elétrica Bahiana" que fala português do brasil.' 
        },
        {
            'role': 'user',
            'content': 'Quem é você, poderia se apresentar para mim?'
        }
    ],
    temperature=1.0,
    
)

print(response_llm.choices[0].message.content)