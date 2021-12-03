保存一帧YUV420数据

```c++
		while (avcodec_receive_frame(pCodecCtx, &g_frame) == 0)
		 
			uint32_t pitchY = g_frame.linesize[0];
			uint32_t pitchU = g_frame.linesize[1];
			uint32_t pitchV = g_frame.linesize[2];

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
				fwrite(avU, g_frame.width, 1, fp);
				avU += pitchU;
			}

			for (size_t i = 0; i < g_frame.height/2; ++i)
			{
				fwrite(avV, g_frame.width, 1, fp);
				avV += pitchV;
			}
		}
```

