### 为什么用它
空间占用少。 
RGB24一帧的大小size＝width×heigth×3 Byte 
RGB32一帧的大小size＝width×heigth×4 Byte 
YUV420一帧的大小size=width×heigth×1.5 Byte (Y占1Byte，UV占0.5Byte)



保存一帧YUV420数据

```c++
		while (avcodec_receive_frame(pCodecCtx, &g_frame) == 0)
		 	// YUV420P，1080P为例，pitchY通常为视频宽度1920，pitchU/pitchV为960
            // 
			uint32_t pitchY = g_frame.linesize[0];	// Y分量的宽度，有时不等于视频宽度，为了对齐？
			uint32_t pitchU = g_frame.linesize[1];	// U分量的宽度
			uint32_t pitchV = g_frame.linesize[2];	// V分量的宽度

			// data是指针数组，每项代表对应的YUV数据地址
			uint8_t* avY = g_frame.data[0];
			uint8_t* avU = g_frame.data[1];
			uint8_t* avV = g_frame.data[2];
			for (size_t i = 0; i < g_frame.height; ++i)
			{
				fwrite(avY, g_frame.width, 1, fp);
				avY += pitchY;
			}
			
			for (size_t i = 0; i < g_frame.height/2; ++i)
			{
                // 为什么不用pitchU做第二个参数？（应该是为了对齐有时分量大于视频宽度，避免多余拷贝）
				fwrite(avU, g_frame.width / 2, 1, fp);
				avU += pitchU;
			}

			for (size_t i = 0; i < g_frame.height/2; ++i)
			{
				fwrite(avV, g_frame.width / 2, 1, fp);
				avV += pitchV;
			}
		}
```

