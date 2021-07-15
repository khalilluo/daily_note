# 生成访问代码

将proto.exe、helloworld.proto、grpc_cpp_plugin.exe拷贝到一个文件夹中，grpc_cpp_plugin.exe是gRPC的protoc插件，生成方法参考上文。

创建一个bat文件，包含以下命令：

```
protoc.exe -I=. --grpc_out=. --plugin=protoc-gen-grpc=.\grpc_cpp_plugin.exe helloworld.proto
protoc.exe -I=. --cpp_out=. helloworld.proto
```

生成了两套文件

```
hellowworld.pb.h 声明生成的消息类的头文件
hellowworld.pb.cc  包含消息类的实现
hellowworld.grpc.pb.h 声明你生成的服务类的头文件
hellowworld.grpc.pb.cc 包含服务类的实现
```