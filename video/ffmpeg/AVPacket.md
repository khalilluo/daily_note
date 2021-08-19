```c++
av_read_frame() // 从上下文获取一个包，必须使用av_packet_unref（av_free_packet）释放内容，否则内存泄漏

//AVPacket如果是指针需要先用av_packet_alloc申请空间，但不包含data内容

av_init_packet()//初始化AVPacket部分属性，但data仍没有内容

av_new_packet(pkg, size) //申请size大小的内存空间到data

av_packet_clone(500) // (av_packet_alloc()+av_packet_ref())
```

