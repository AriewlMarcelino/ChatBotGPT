#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system('pip install openai')


# In[23]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(model="text-davinci-003",prompt="Você pode explicar o que é um transformers no contexto de NLP?")
print(response.choices[0].text)


# In[20]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(model="text-davinci-003",prompt="Você pode explicar o que é um transformers no contexto de NLP?",max_tokens=1000)
print(response.choices[0].text)


# #modelo de text-davinci-003
# 
# Transformers são redes neurais profundas que foram projetadas para entender o significado de sentenças em línguas naturais. Usando o poder do processamento distribuído, os transformadores aprendem representações ricas e significativas de palavras e frases, permitindo que os algoritmos de NLP aproveitem essas representações mais profundas para sua tarefa. Alguns exemplos de aplicações são tradução automática, classificação de sentimentos e extração de informação.

# # Teste de modelo text-curie-001

# In[26]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(model="text-curie-001",prompt="Você pode explicar o que é um transformers no contexto de NLP?",max_tokens=1000)
print(response.choices[0].text)

#modelo de test-curie-001

Transformers é um filme transmitido periodicamente nos cinemas durante os anos 80 e 90, um sistema de cinema que utiliza imagens de animação feitas para transformá-las em vídeo 3-D. Os transformers impactam a vida dos personagens principalmente quando eles descobrem que eles não são humanos, mas animais escolhidos para combaterem um inimigo criado pelo governo que está associando os transformers à morte. Essa ligação é realize pela mostra de um robot autômato que tem a forma de um insecto.
# # Teste do modelo text-babbage-001

# In[27]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(model="text-babbage-001",prompt="Você pode explicar o que é um transformers no contexto de NLP?",max_tokens=1000)
print(response.choices[0].text)

#modelo de test-babbage-001

A transformer é uma correspondência de dezenas de bits (dimensão diferente de um galáxia) que elemite transformados de uma forma particular. Geralmente, os transformers são usados quando é preciso transformar informações para outras formas, conforme a necessidade. Por exemplo, um transformers é usado para transformar 8 Lambda na informação ASCII.
# # Teste de modelo text-ada-001

# In[29]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(model="text-ada-001",prompt="Você pode explicar o que é um transformers no contexto de NLP?",max_tokens=1000)
print(response.choices[0].text)

# modelo de test-ada-001

Um transfonenciante, outra forma de denominar-se é unguladores.Eles forman uma face gone mothing, lvier obrazy tank ecologically aggressivo, planificada para atravessar as rochas, formando uma fechesinhada de cavidada (ilha de forma horizontal, de fora do formanho normal).Outra facesiana roroxyfed estupor, orientadas para a vista, formandoesporge costas e costeiras.
# # trabalhando com outros atributos:

# In[ ]:


# Temperature=1 => expresa o nivél de criatividade exercida ao GTP 
# n=4 => numero de respostas fornecidas pelo GPT como inico vamos dar


# In[40]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

#Passando para o Openai, o modelo que é o tipo de modelo para o gerenciamento de processamento e o prompt para poder estar perguntado ao GPT:
response = openai.Completion.create(
    # modelo utilizado para o processamento:
    model="text-davinci-003",
    # A pergunta a ser processada:
    prompt="Você pode explicar o que é um transformers no contexto de NLP?",
    # O numero de caracteres a ser passado:
    max_tokens=1000,
    # Nivél de criatividade para a resposta:
    temperature=1,
    # Numeros de respostas
    n = 4
    )

#For para poder percorres as 4 respostas:
for i in range(len(response.choices)):
    print(response.choices[i].text)
    

#### Modelo de resposta com parâmetros "temperature" e 'n':

Transformers são uma arquitetura de aprendizado profundo que usa o Attention em um modelo de linguagem para a transferência de aprendizado de tarefas de processamento de linguagem natural. Os modelos Transformer usam módulos matemáticos chamados 'camadas de atenção' para ajudar o modelo a se concentrar em partes relevantes da entrada de linguagem. Estas camadas usam matrizes à esquerda e à direita para determinar a relação entre as palavras e cada ponto focal. O restante das camadas são usadas para codificar os pontos focais e produzir a saída. Um benefício dos modelos Transformers é que eles são mais versáteis do que outras arquiteturas de aprendizado profundo, pois podem lidar com uma ampla variedade de tarefas de processamento de linguagem natural.


Transformers são modelos de aprendizado profundo de aprendizado por meio de autoatendimento que foram desenvolvidos para melhorar os resultados de tarefas comuns de Processamento de Linguagem Natural (NLP), como parte da frase, o que o usuário está lendo, tradução automática e classificação de sentimentos. Eles utilizam de processos de autoatendimento chamados de células de memória (ex: mecanismos de atenção (attention mechanisms) baseados em camadas). Estas células são responsáveis por armazenar o que o usuário lê e usando mecanismos de atenção, as informações são usadas para ajudar a modelar a saída do processador. Assim, eles permitem a compreensão de linguagem natural mais precisa ao levar em consideração informações do contexto e da estrutura da frase completa.


Transformadores são modelos de aprendizagem profunda que usam um recurso de processamento de linguagem natural chamado autocodificador transferível. Estes modelos consistem em sobreposições hierárquicas de blocos autoencoders que usam atenção multi-tarefa. As sobreposições permitem que os dados de entrada sejam analisados, compreendidos e processados ao mesmo tempo, permitindo que os modelos qualificados e conscientes das representações capturem pontos importantes do texto, tais como entidades, sinônimos e relações entre palavras. Estes modelos são usados ​​para tarefas como classificação de sentimentos, previsão de linguagem, extensão de frase, classificação e muito mais.


Transformers são uma classe de deeplearning mais recente, especialmente bem-sucedida para tarefas de processamento de linguagem natural (NLP). Em vez do uso convencional de camadas convolucionais e recorrentes, os transformers aprendem a entender a linguagem natural através de múltiplos processos de auto-atendimento que se comunicam entre si. Eles utilizam tecnologia de atenção, o que significa que procuram focar sua atenção na parte importante da entrada ao invés de lidar com a entrada como um todo. Isto significa que ao lidar com problemas de linguagem, como tradução, as pessoas podem agora construir redes mais complexas, já que as várias partes do input têm relações entre si que precisam ser entendidas.
# # Fazendo o GPT emitir as resposta com base em um texto:

# In[61]:


import openai

texto = "qual é a diferença entre copywriting e marketing de conteudo"
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


# # trabalhando com contexto em GPT

# In[ ]:


import openai

texto = "qual é a diferença entre copywriting e marketing de conteudo"
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


# # Trabalhando com DALL-E

# In[67]:


import openai

#Vinculando a chave de API com openia:
openai.api_key = "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"

response = openai.Image.create(
    prompt = 'crie uma imagem de um disco voador 3D',
    size = "512x512",
    n=1,
    response_format = "url",

)

print(response["data"][0]["url"])





# # Gerando imagens com DALL-E no Anaconda

# In[69]:


import openai
from io import BytesIO
import requests
from PIL import image

#Vinculando a chave de API com openia:
openai.api_key = "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"

response = openai.Image.create(
    prompt = 'crie uma imagem de um disco voador 3D',
    size = "256x256",
    n=1,
    response_format = "url",

)

response = requests.get(respose["data"][0]["url"])
Image.open(BytesIO(response.content))


# In[ ]:




