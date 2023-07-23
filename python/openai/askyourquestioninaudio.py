#Get the list of models available in open AI
import os
import openai

# This the file got created a a global environment file , where you have to set the API key and org key for your account
import openaienv
openai.organization = openaienv.GLOBAL_ORG_KEY
openai.api_key = openaienv.GLOBAL_API_KEY
#system_prompt = "You are a helpful assistant for the company cloudaigurus. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

system_prompt = "You are a helpful assistant for the company cloudaigurus. Your task is translate the audio."

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 5
 
# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
 
# Record audio for the given number of seconds
sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("C:\\PRODDEV\\projects\\cloudaigurus\\content\\sampleaudios\\recording0.wav", freq, recording)
 
# Convert the NumPy array to audio file
wv.write("C:\\PRODDEV\\projects\\cloudaigurus\\content\\sampleaudios\\recording1.wav", recording, freq, sampwidth=2)

def generate_answer_transcript(temperature, system_prompt, audio_file):
    print(audio_file)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": ""
            },
            {
                "role": "user",
                "content": str(openai.Audio.translate("whisper-1", audio_file))
                #openai.Audio.transcribe(audio_file, "")
            }
        ]
    )
    return response['choices'][0]['message']['content']
sample_audio_file= open("C:\\PRODDEV\\projects\\cloudaigurus\\content\\sampleaudios\\recording0.wav", "rb")

response_text = generate_answer_transcript(0, system_prompt, sample_audio_file)
print("Response is :" + response_text)