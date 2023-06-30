# Import necessary libraries
import openai
import os
import streamlit as st
import qrcode

# Load your OpenAI API key from your local `.env` file
openai.api_key = "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"

# Add a title and a brief description
st.title("📜 IA Bíblica")
st.markdown("""
Este aplicativo usa o modelo GPT-3.5-turbo-16k da OpenAI para oferecer conselhos e ensinamentos com base na Bíblia.

Você pode usar esse programa para buscar entendimento sobre passagens bíblicas, aprender mais sobre as escrituras, buscar conselhos espirituais, e muito mais.

Basta digitar a sua pergunta ou tópico de interesse, e então clique em 'Gerar'.
""")

# Obtenha a entrada do usuário para o item 1
question = st.text_area("Qual é a sua pergunta ou tópico de interesse?")

# Definir a mensagem do sistema
system_message = f"""
Olá, sou um assistente virtual treinado para oferecer conselhos e ensinamentos com base na Bíblia e em diferentes religiões do mundo. Estou aqui para ajudar você a entender melhor questões espirituais. Então, você gostaria de discutir sobre "{question}"?
"""

# Gerar a resposta
if 'generated_message' not in st.session_state:
    st.session_state.generated_message = ""

# List of keywords related to the Bible and religion
keywords = ['Deus', 'Jesus', 'Bíblia', 'cristão', 'cristianismo', 'fé', 'igreja', 'religião', 'orar', 'oração', 'espírito', 'santo', 'divino', 'biblical', 'heaven', 'hell', 'apostle', 'disciple']

if st.button('Gerar'):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
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

# Generate the QR code

# Generate the QR code
input_data = "00020126580014br.gov.bcb.pix01360e48f310-f553-478e-99ca-2969866ca19a5204000053039865802BR5924Felipe de Oliveira Silva6008Brasilia62080504mpda6304B474"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,
    border=4,
)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image
img.save('qrcode.png')

# Display the QR code at the end of your app
st.markdown("""
## Pronto para elevar a experiência de aprendizado espiritual de sua congregação?
Se você está encantado com o que a IA Bíblica pode fazer, imagine o impacto que ela terá em sua igreja. Este aplicativo não é apenas uma ferramenta educativa, é uma plataforma que inspira, orienta e ajuda a esclarecer questões teológicas complexas, baseando-se na Bíblia. Fale conosco para saber mais sobre como adquirir.
""")

st.markdown("Para mais informações visite o nosso site: ")

st.markdown("""
### Siga nas redes sociais

<p align="left"> 
<a href="https://www.instagram.com/felipesilva.tech/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" />
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.youtube.com/@felipesilvatech" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/youtube.svg" width="32" height="32" /></a> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://twitter.com/fsilvatech" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/twitter.svg" width="32" height="32"/> 
</p>
""", unsafe_allow_html=True)

