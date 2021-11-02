#!/usr/bin/env python3

from array2gif import write_gif  # version: 1.0.4
import librosa  # version: 0.8.1
import numpy  # version: 1.19.5


num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'
red_pixel = [255, 0, 0]
white_pixel = [255, 255, 255]
y, sample_rate = librosa.load("flag.mp3")       # sample rate is 22050 Hz
print(sample_rate)

spectrogram = (                                 # 频谱图
    numpy.around(                               # Number of decimal places to round to (default: 0).
                                                # 此处实际作用 arr&=~1 所有数(bin)末位置零
        librosa.power_to_db(                    # 將功率譜圖（幅度平方）轉換為分貝 (dB) 單位
            librosa.feature.melspectrogram(     # 計算梅爾縮放頻譜圖。
                y,                              # flag.mp3  audio signal
                sample_rate,                    # 22050     sample rate
                n_mels=num_freqs,               # 32        number of mel bins
                n_fft=fft_window_size,          # 2048      FFT window size
                hop_length=frame_step_size,     # 512       hop size
                window=window_function_type     # 'hann'    window function
            )
        )/quantize
    )*quantize
)

gif_data = [
    numpy.kron(         # 兩個數組的 Kronecker 積
        numpy.array(    # 將 numpy.array 轉換為 numpy.ndarray
            [
                [
                    red_pixel
                        if freq % 2 and round(frame[freq // 2]) > threshold
                        else white_pixel    
                        for threshold in list(
                        range(
                            min_db,                     # -60
                            max_db + 1,                 # 30+1=31
                            quantize                    # 2
                        )
                    )[::-1]
                ] for freq in range(num_freqs * 2 + 1)  # 32*2+1=65
            ]
        ),                                              # 这里面是一个frame变成柱状图的样子
        numpy.ones(
            [quantize, quantize, 1]                     # 2*2*1 的三维1.0矩阵: [[[1.]  [1.]] [[1.]  [1.]]]
        )
    ) for frame in spectrogram.transpose()              # 频谱图转置后的每一行(帧)
]

write_gif(
    gif_data,
    'flag.gif',
    fps=sample_rate/frame_step_size,    # 22050/512=43.06640625
)
