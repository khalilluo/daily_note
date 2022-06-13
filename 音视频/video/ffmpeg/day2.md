```C++
// 原寻找流方式
for (i = 0; i < pFormatCtx->nb_streams; i++) {
	if (pFormatCtx->streams[i]->codec->codec_type == AVMEDIA_TYPE_VIDEO) {
		videoStream = i;
	}
}
// 新查找流方式
int  streamIndex = av_find_best_stream(pFormatCtx, AVMEDIA_TYPE_VIDEO, -1, -1, NULL, 0);
if (AVERROR_STREAM_NOT_FOUND == streamIndex){
    // 没找到流
}



// 1、 AVFormatContent有解码器上下文
pCodecCtx = pFormatCtx->streams[videoStream]->codec;
pCodec = avcodec_find_decoder(pCodecCtx->codec_id);

// 2、也可以自行分配解码器上下文
pCodecCtx  = avcodec_alloc_context3(pCodec);

// 根据流参数设置解码器上下文
ret = avcodec_parameters_to_context(pCodecCtx, pFormatCtx->streams[videoStream]->codecpar);


///打开解码器
if (avcodec_open2(pCodecCtx, pCodec, NULL) < 0) {
	printf("Could not open codec.\n");
	return;
}
```


获取特定编码格式下每个像素占的bit

```c++
int perPixel = av_get_bits_per_pixel(av_pix_fmt_desc_get(pCodecCtx->pix_fmt));
```

