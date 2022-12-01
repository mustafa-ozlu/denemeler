import sounddevice
from scipy.io.wavfile import write
fs=44100
second=int(input("Kaç Saniye Kayıt Yapılacak:"))
print("Kayıtta....\n")

record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("KAYIT.wav",fs,record_voice)
print("Kayıt Bitti...\n")