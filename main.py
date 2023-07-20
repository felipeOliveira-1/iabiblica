# Import necessary libraries
import openai
import os
import streamlit as st


# Load your OpenAI API key from your local `.env` file
openai.api_key = "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"

# Add a title and a brief description
st.markdown("""
<a href="https://iabiblica.com.br/">
<img src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=132,h=132,fit=crop/Aq2047MR9ZFejV6k/logo-iab-1-AE0qRkNM04u1E9l8.png" />
</a><br>
""", unsafe_allow_html=True)
st.markdown("""
Este é um aplicativo de teste ALPHA que utiliza o modelo mais avançado de Inteligencia Artificial, capaz de oferecer conhecimento, sabedoria e ensinamentos Bíblicos.

Você pode usar esse programa para buscar entendimento sobre passagens bíblicas, aprender mais sobre as escrituras, buscar direção espiritual e muito mais.

Basta digitar a sua pergunta ou tópico de interesse, e então clique em 'Gerar'.
""")

# Obtenha a entrada do usuário para o item 1
question = st.text_area("Qual é a sua pergunta ou tópico de interesse?")

# Definir a mensagem do sistema
system_message = f"""
Olá, sou um assistente virtual treinado para oferecer conselhos e ensinamentos com base na Bíblia. A versão da Bíblia que utilizo prioritariamente é a King James, mas também utilizo João Ferreira de Almeida (ACF), Nova Versão Internacional (NVI) alem dos três pilares: as Sagradas Escrituras, a Tradição e o Magistério da Igreja Católica. 
Estou aqui para ajudar você a entender melhor questões espirituais tendo como base a bíblia. Então, você gostaria de discutir sobre "{question}"?
"""

# Gerar a resposta
if 'generated_message' not in st.session_state:
    st.session_state.generated_message = ""

# List of keywords related to the Bible and religion
keywords = ['Deus', 'Jesus', 'Bíblia', 'cristão', 'cristianismo', 'fé', 'igreja', 'religião', 'orar', 'oração', 'espírito', 'santo', 'divino', 'biblical', 'heaven', 'hell', 'apostle', 'disciple']

if st.button('Gerar'):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=3500,
        messages=[
            {"role": "system", "content": system_message},
        ]
    )

    generated_message = response['choices'][0]['message']['content']

    # If the generated message does not contain any keyword, return the specified message
    if not any(keyword.lower() in generated_message.lower() for keyword in keywords):
        generated_message = "Essa IA trata somente de questões relacionadas à Bíblia e diferentes religiões do mundo."

    st.session_state.generated_message = generated_message

# Imprimir a resposta gerada
st.text_area("Resposta:", value=st.session_state.generated_message, height=200, max_chars=None, key=None)

st.markdown("""
## Pronto para elevar a experiência de aprendizado espiritual de sua congregação?
Se você está encantado com o que a IA Bíblica pode fazer, imagine o impacto que ela terá em sua igreja. Este aplicativo não é apenas uma ferramenta educativa, é uma plataforma que inspira, orienta e ajuda a esclarecer questões teológicas complexas, baseando-se na Bíblia. Fale conosco para saber mais sobre como adquirir a versão completa.
""")

st.markdown("Para mais informações visite o nosso site: https://iabiblica.com.br/ ")

