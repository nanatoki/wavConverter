import wave

fname = 'ori.wav' # mono
# fname = 'Alesis-Fusion-Pizzicato-Strings-C4.wav' # stereo

waveFile = wave.open(fname, 'r')
#buf = waveFile.readframes(1024)
buf = waveFile.readframes(-1) # 全て読み込む場合


print(buf)
# wavファイルの情報を取得
# チャネル数：monoなら1, stereoなら2, 5.1chなら6(たぶん)
nchannles = waveFile.getnchannels()

# 音声データ1サンプルあたりのバイト数。2なら2bytes(16bit), 3なら24bitなど
samplewidth = waveFile.getsampwidth()

# サンプリング周波数。普通のCDなら44.1k
framerate = waveFile.getframerate()

# 音声のデータ点の数
nframes = waveFile.getnframes()


waveFile.close()
print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)