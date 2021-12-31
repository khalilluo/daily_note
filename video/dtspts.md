 DTS、PTS 是用于指导播放端的行为，但它们是在编码的时候由编码器生成的

当视频流中没有 B 帧时，通常 DTS 和 PTS 的顺序是一致的

要实现音视频同步，通常需要选择一个参考时钟，参考时钟上的时间是线性递增的，编码音视频流时依据参考时钟上的时间给每帧数据打上时间戳。在播放时，读取数据帧上的时间戳，同时参考当前参考时钟上的时间来安排播放。这里的说的时间戳就是我们前面说的 PTS。实践中，我们可以选择：同步视频到音频、同步音频到视频、同步音频和视频到外部时钟

如果你是把1秒分成90000份，每一个刻度就是1/90000秒，此时的time_base={1，90000}。 
所谓时间基表示的就是每个刻度是多少秒 
pts的值就是占多少个时间刻度（占多少个格子）。它的单位不是秒，而是时间刻度。只有pts加上time_base两者同时在一起，才能表达出时间是多少

在ffmpeg中。av_q2d(time_base)=每个刻度是多少秒 ，此时你应该不难理解 **pts*av_q2d(time_base)才是帧的显示时间戳**



## why

下面理解时间基的转换，为什么要有时间基转换。 
首先，不同的封装格式，timebase是不一样的。另外，整个转码过程，不同的数据状态对应的时间基也不一致。拿mpegts封装格式25fps来说（只说视频，音频大致一样，但也略有不同）。**非压缩**时候的数据（即YUV或者其它），在ffmpeg中对应的结构体为AVFrame,它的时间基为AVCodecContext 的time_base ,AVRational{1,25}。 
**压缩后**的数据（对应的结构体为AVPacket）对应的时间基为AVStream的time_base，AVRational{1,90000}。 
因为数据状态不同，时间基不一样，所以我们必须转换，在1/25时间刻度下占10格，在1/90000下是占多少格。这就是pts的转换。

根据pts来计算一桢在整个视频中的时间位置： 
timestamp(秒) = pts * av_q2d(stream->time_base)

duration和pts单位一样，duration表示当前帧的持续时间占多少格。或者理解是两帧的间隔时间是占多少格。一定要理解单位。 
pts：格子数 
av_q2d(st->time_base): 秒/格

**计算视频长度：** 
time(秒) = st->duration * av_q2d(st->time_base)

ffmpeg内部的时间与标准的时间转换方法： 
ffmpeg内部的时间戳 = AV_TIME_BASE * time(秒) 
AV_TIME_BASE_Q=1/AV_TIME_BASE

av_rescale_q(int64_t a, AVRational bq, AVRational cq)函数 
这个函数的作用是计算a*bq / cq来把时间戳从一个时间基调整到另外一个时间基。在进行时间基转换的时候，应该首先这个函数，因为它可以避免溢出的情况发生。 
函数表示在bq下的占a个格子，在cq下是多少。

**关于音频pts的计算：** 
音频sample_rate:samples per second，即采样率，表示每秒采集多少采样点。 
比如44100HZ，就是一秒采集44100个sample. 
即每个sample的时间是1/44100秒

一个音频帧的AVFrame有nb_samples个sample，所以一个AVFrame耗时是nb_samples*（1/44100）秒 
即标准时间下duration_s=nb_samples*（1/44100）秒， 
转换成AVStream时间基下 
duration=duration_s / av_q2d(st->time_base) 
基于st->time_base的num值一般等于采样率,所以duration=nb_samples. 
pts=n*duration=n*nb_samples

### 流媒体相关

RTSP中没有dts和pts？有的，如果保存的话需要根据差值重新变化pts和dts，否则播放可能异常（从获取流到开始保存那一帧的时间将被计算进去）

