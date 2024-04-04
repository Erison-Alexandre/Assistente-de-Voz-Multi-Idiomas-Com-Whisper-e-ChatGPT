#importação das bibliotecas
from IPython.display import Audio, display
import whisper
import pyaudio
import wave
import os
import openai
from gtts import  gTTS
from pydub import AudioSegment
from pydub.playback import play


#gravação do áudio utilizando as libs pyaudio e wave

def record_audio(filename, duration=5, channels=1, rate=44100, chunk=1024):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
                        

    print("Gravando...\n")

    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Fim da gravação\n")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    audio_file = AudioSegment.from_wav(filename)
    play(audio_file)

record_audio("audio.wav", duration=5)

#Reconhecimento de Fala com Whisper

print("transcrevendo audio.\n")
language = 'pt'
record_file= "audio.wav"
model = whisper.load_model("small")
result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]
print(transcription)
print("Fim da transcrição\n")

#Integração com a API do ChatGPT

os.environ['CHAVE API'] = 'TODO'
openai.api_key = os.environ.get('OPENAI_API_KEY')
chatgpt_response = response.choices[0].message.content
print(chatgpt_response)

#Sintetizando a Resposta do ChatGPT Como Voz (gTTS)

gtts_object = gTTS(text=chatgpt_response, lang=language, slow=False)
response_audio = "response_audio.wav"
gtts_object.save(response_audio)
display(Audio(response_audio, autoplay=True))