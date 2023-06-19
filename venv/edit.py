import numpy as np
from gtts import gTTS
from pydub import AudioSegment
import librosa
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter

def convertir_texto_audio(texto, nombre_archivo):
    tts = gTTS(texto, lang="es")  # Configura el idioma deseado

    tts.save(nombre_archivo)
    print(f"Archivo de audio generado: {nombre_archivo}")

    # Cargar el archivo de audio original
    audio = AudioSegment.from_file(nombre_archivo, format="mp3")

    # Modificar el tono del audio (bajar una octava)
    samples = audio.get_array_of_samples()
    framerate = audio.frame_rate
    samples = np.array(samples)

    samples_pitch_shifted = librosa.effects.pitch_shift(samples.astype(float), sr=framerate, n_steps=-5)
    samples_pitch_shifted = np.array(samples_pitch_shifted, dtype=np.int16)

    audio_modificado = AudioSegment(
        samples_pitch_shifted.tobytes(),
        frame_rate=framerate,
        channels=audio.channels,
        sample_width=audio.sample_width
    )

    # Ajustar la velocidad del audio (ritmo)
    audio_modificado.export("temp_audio.wav", format="wav")

    with WavReader("temp_audio.wav") as reader:
        with WavWriter("salida_modificado.wav", reader.channels, reader.samplerate) as writer:
            phasevocoder(reader.channels, speed=1).run(reader, writer)

    audio_modificado = AudioSegment.from_wav("salida_modificado.wav")

    # Aumentar el volumen del audio modificado en 6 dB
    audio_modificado = audio_modificado.apply_gain(15)

    # Guardar el audio modificado, cambiar a audio_modificado si queremos modificar la voz
    nombre_archivo_modificado = "salida_modificado.mp3"
    audio.export(nombre_archivo_modificado, format="mp3")

    print(f"Se ha generado el archivo de audio modificado '{nombre_archivo_modificado}'.")

#convertir_texto_audio("hola que tal jajajaj", "salida.mp3")