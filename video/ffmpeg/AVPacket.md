AVPacket表示解复用之后，解码之前的数据。对于视频（Video）来说，AVPacket通常包含一个压缩的Frame，而音频（Audio）则有可能包含多个压缩的Frame

推荐在栈上分配？

```C++
// 压缩编码的数据。
// 例如对于H.264来说。1个AVPacket的data通常对应一个NAL。
// 注意：在这里只是对应，而不是一模一样。
// 他们之间有微小的差别：使用FFMPEG类库分离出多媒体文件中的H.264码流。
// 因此在使用FFMPEG进行视音频处理的时候，常常可以将得到的AVPacket的data数据直接写成文件，
// 从而得到视音频的码流文件。
uint8_t *data; // 指向保存压缩数据的指针，这就是AVPacket实际的数据。

int   size； 		// data的大小
int64_t pts； 		// 显示时间戳
int64_t dts； 		// 解码时间戳
int stream_index； 	// 标识该AVPacket所属的视频/音频流。
    
AVPacketSideData *side_data 	// 容器提供的一些附加数据
AVBufferRef *buf 				// 是AVBufferRef类型的指针，用来管理data指针引用的数据缓存的，其使用在后面介绍。
```

```c++
av_read_frame() // 从上下文获取一个包，必须使用av_packet_unref（av_free_packet）释放内容，否则内存泄漏

//AVPacket如果是指针需要先用av_packet_alloc申请空间，但不包含data内容

av_init_packet()//初始化AVPacket部分属性，但data仍没有内容

av_new_packet(pkg, size) //申请size大小的内存空间到data

av_packet_clone(500) // (av_packet_alloc()+av_packet_ref())
```

### AVPacket中的内存管理

AVPacket实际上可用看作一个容器，它本身并不包含压缩的媒体数据，而是通过data指针引用数据的缓存空间。所以将一个Packet作为参数传递的时候，妖就要根据具体的需要，对data引用的这部分数据缓存空间进行特殊的处理。当从一个Packet去创建另一个Packet的时候，有两种情况：

- 两个Packet的data引用的是同一数据缓存空间，这时候要注意数据缓存空间的释放问题
- 两个Packet的data引用不同的数据缓存空间，每个Packet都有数据缓存空间的copy。

第二种情况，数据空间的管理比较简单，但是数据实际上有多个copy造成内存空间的浪费。所以要根据具体的需要，来选择到底是两个Packet共享一个数据缓存空间，还是每个Packet拥有自己独自的缓存空间。
对于多个Packet共享同一个缓存空间，FFmpeg使用的**引用计数的机制（reference-count）**。当有新的Packet引用共享的缓存空间时，就将引用计数+1；当释放了引用共享空间的Packet，就将引用计数-1；引用计数为0时，就释放掉引用的缓存空间。
AVPacket中的`AVBufferRef *buf;`就是用来管理这个引用计数的，`AVBufferRef`的声明如下：

```c++
typedef struct AVBufferRef {
    AVBuffer *buffer;
    /**
     * The data buffer. It is considered writable if and only if
     * this is the only reference to the buffer, in which case
     * av_buffer_is_writable() returns 1.
     */
    uint8_t *data;
    /**
     * Size of data in bytes.
     */
    int      size;
} AVBufferRef;  
```

在AVPacket中使用`AVBufferRef`有两个函数：`av_packet_ref`和`av_packet_unref`。

- av_packet_ref

```c++
int av_packet_ref(AVPacket *dst, const AVPacket *src)
```

创建一个`src->data`的新的引用计数。如果src已经设置了引用计数发（src->buffer不为空），则直接将其引用计数+1；如果src没有设置引用计数（src->buffer为空），则为dst创建一个新的引用计数buf，并复制`src->data`到`buf->buffer`中。最后，复制src的其他字段到dst中。

- av_packet_unref

```c++
void av_packet_unref(AVPacket *pkt)
```

将缓存空间的引用计数-1，并将Packet中的其他字段设为初始值。如果引用计数为0，自动的释放缓存空间。
**所以，有两个Packet共享同一个数据缓存空间的时候可用这么做**

```c++
av_read_frame(pFormatCtx, &packet)  // 读取Packet
av_packet_ref(&dst,&packet) // dst packet共享同一个数据缓存空间
...
av_packet_unref(&dst); 
```

下一小节简单的介绍下AVPacket相关的函数，并介绍如何在传递Packet的时候，复制一个独立的数据缓存空间的copy，每个Packet都拥有自己独立的数据缓存空间。

### AVPacket 相关函数介绍

操作AVPacket的函数大约有30个，主要可以分为：AVPacket的创建初始化、AVPacket中的data数据管理（clone，free，copy等）、AVPacket中的side_data数据管理。
AVPacket的创建有很多种，而由于Packet中的数据是通过data引用的，从一个Packet来创建另一个Packet有多种方法。

- `av_read_frame` 这个是比较常见的了，从媒体流中读取帧填充到填充到Packet的数据缓存空间。如果`Packet->buf`为空，则Packet的数据缓存空间会在下次调用`av_read_frame`的时候失效。这也就是为何在[FFmpeg3：播放音频](http://www.cnblogs.com/wangguchangqing/p/5788805.html)中，从流中读取到Packet的时，在将该Packet插入队列时，要调用`av_dup_avpacket`重新复制一份缓存数据。（`av_dup_avpacket`函数已废弃，后面会介绍）
- `av_packet_alloc` 创建一个AVPacket，将其字段设为默认值（data为空，没有数据缓存空间）。
- `av_packet_free` 释放使用`av_packet_alloc`创建的AVPacket，如果该Packet有引用计数（packet->buf不为空），则先调用`av_packet_unref(&packet)`。
- `av_packet_clone` 其功能是 `av_packet_alloc` + `av_packet_ref`
- `av_init_packet` 初始化packet的值为默认值，该函数不会影响data引用的数据缓存空间和size，需要单独处理。
- `av_new_packet` `av_init_packet`的增强版，不但会初始化字段，还为data分配了存储空间。
- `av_copy_packet` 复制一个新的packet，包括数据缓存。
- `av_packet_from_data` 初始化一个引用计数的packet，并指定了其数据缓存。
- `av_grow_packet`和 `av_shrink_packet` 增大或者减小Packet->data指向的数据缓存。

就罗列这么多吧，剩下的没提到的基本都是和side_data相关的一些函数，和data的比较类似。
最后介绍下已经废弃的两个函数 `av_dup_packet`和`av_free_packet`。
`av_dup_packet` 是复制src->data引用的数据缓存，赋值给dst。也就是创建两个独立packet，这个功能现在可用使用函数`av_packet_ref`来代替。
`av_free_packet` 释放packet，包括其data引用的数据缓存，现在可以使用`av_packet_unref`代替。

### AVPacket队列

在[FFmpeg3：播放音频](http://www.cnblogs.com/wangguchangqing/p/5788805.html)中，使用了AVPacket队列来缓存从流中读取的帧数据。这就涉及到多次的AVPacket的传递，从流中读取Packet插入队列；从队列中取出Packet进行解码；以及一些中间变量。由于Dranger教程中使用的已经废弃的API，在参照官方文档进行修改的时候就出现了内存读写的异常。下面就播放音频的教程中的AVPacket队列实现，分析下在AVPacket作为参数传递的过程中，应该如何更好的管理其data引用的缓存空间。

- 从流中读取AVPacket插入队列

```c++
    AVPacket packet;
    while (av_read_frame(pFormatCtx, &packet) >= 0)
    {
        if (packet.stream_index == audioStream)
            packet_queue_put(&audioq, &packet);
        else
            //av_free_packet(&packet);
            av_packet_unref(&packet);
    } 
```

如果是音频流则将读到Packet调用`packet_queue_put`插入到队列，如果不是音频流则调用`av_packet_unref`释放已读取到的AVPacket数据。
下面代码是`packet_queue_put`中将Packet放入到一个新建的队列节点的代码片段

```
    AVPacketList *pktl;
    //if (av_dup_packet(pkt) < 0)
        //return -1;
    pktl = (AVPacketList*)av_malloc(sizeof(AVPacketList));
    if (!pktl)
        return -1;
    if (av_packet_ref(&pktl->pkt, pkt) < 0)
        return -1;
    //pktl->pkt = *pkt;
    pktl->next = nullptr;  
```

注意，在调用`packet_queue_put`时传递的是指针，也就是形参pkt和实参packet中的data引用的是同一个数据缓存。但是在循环调用`av_read_frame`的时候，会将packet中的data释放掉，以便于读取下一个帧数据。
所以就需要对data引用的数据缓存进行处理，保证在读取下一个帧数据的时候，其data引用的数据空间没有被释放。有两种方法，复制一份data引用的数据缓存或者给data引用的缓存空间加一个引用计数。
注释掉的部分是使用已废弃的API`av_dup_packet`，该函数将pkt中data引用的数据缓存复制一份给队列节点中的AVPacket。
添加引用计数的方法则是调用`av_apcket_ref`将data引用的数据缓存的引用计数+1，这样其就不会被释放掉。

- 从队列中取出AVPacket

```c++
 //*pkt = pktl->pkt;
 if (av_packet_ref(pkt, &pktl->pkt) < 0)
 {
      ret = 0;
      break;
 }  
```

注释掉的代码仍然是两个packet引用了同一个缓存空间，这样在一个使用完成释放掉缓存的时候，会造成另一个访问错误。所以扔给调用`av_packet_ref`将其引用计数+1，这样在释放其中一个packet的时候其引用的数据缓存就不会被释放掉，知道两个packet都被释放。
