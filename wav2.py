import wave
import numpy as np
"""
time = np.arange(0, nframes) * (1.0 / framerate)
# 绘制波形
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()
"""
def Resample(input_signal,src_fs,tar_fs=32000):
    dtype = input_signal.dtype
    audio_len = len(input_signal)
    audio_time_max = 1.0*(audio_len-1) / src_fs
    src_time = 1.0 * np.linspace(0,audio_len,audio_len) / src_fs
    tar_time = 1.0 * np.linspace(0,np.int(audio_time_max*tar_fs),np.int(audio_time_max*tar_fs)) / tar_fs
    output_signal = np.interp(tar_time,src_time,input_signal).astype(dtype)
    return output_signal

def readWav(file):
    f = wave.open(file, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]  # 声道数,byte,采样频率,采样点数
    str_data = f.readframes(nframes)
    f.close()

    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = wave_data.reshape(-1, 2).T
    if nchannels==2:
        wave_data = np.average(wave_data, axis=0)
    data = Resample(wave_data, framerate).astype(np.short)

    f = wave.open(r"output.wav", "wb")
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(32000)
    f.writeframes(data.tostring())
    f.close()

readWav("input.wav")

