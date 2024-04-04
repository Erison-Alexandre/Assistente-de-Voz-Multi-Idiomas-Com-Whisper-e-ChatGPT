# Projeto Conversando Por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e Python



## Gravação do áudio utilizando as libs pyaudio e wave

Implementamos uma solução que permite capturar o áudio do usuário diretamente no navegador por meio das bibliotecas pyaudio e wave, conectando essas ferramentas para Gravação do áudio direto do microfone.

## Reconhecimento de Fala com Whisper

Utilizando o avançado modelo de reconhecimento de fala Whisper e a API do ChatGPT, ambos da OpenAI, nossa solução é capaz de entender uma pergunta feita por voz e respondê-la de forma inteligente. Além disso, pra fechar com chave de ouro, ainda usamos o Google Text-To-Speech (gTTS) para sintetizar a resposta do ChatGPT em voz.

## Integração com a API do ChatGPT

Aqui, nos aprofundamos em como o ChatGPT entende as requisições dos usuários e oferece respostas rápidas e relevantes, abrindo portas para inúmeras possibilidades no desenvolvimento de assistentes de voz e outras aplicações baseadas em linguagem natural; 

## Sintetizando a Resposta do ChatGPT Como Voz (gTTS)

Usando o gTTS, uma biblioteca em Python que utiliza a API de Text-to-Speech do Google, sintetizamos o texto em voz. Nesta etapa, aprendemos como utilizar o gTTS para converter as respostas em texto geradas pelo ChatGPT em áudio no idioma escolhido. Isso envolve a seleção da voz e velocidade de fala ideais para proporcionar uma experiência de comunicação natural e envolvente. Ao dominar esta etapa, fomos capazes de dar vida às respostas do ChatGPT, permitindo uma comunicação por voz do início ao fim da nossa solução, completando uma experiência de usuário fluida e linear.