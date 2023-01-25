import openai

texto = "qual a formula fisica da agua?"
#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Voce poderia me responder esta pergunta: " + texto,
    max_tokens=2000,
    echo=True,
    best_of=5,
    temperature=1,
    n=1,
    )
print(response.choices[0].text)