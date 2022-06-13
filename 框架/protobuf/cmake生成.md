#### 步骤
```cmake
# 找到cmake配置
find_package(Protobuf CONFIG REQUIRED)  
if(Protobuf_FOUND)  
    include_directories(${PROTOBUF_INCLUDE_DIRS})  
    include_directories(${CMAKE_CURRENT_BINARY_DIR})  
    # protoc生成对应的pb文件
    protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS testprotos.proto)  
    message(STATUS "protobuf found ${PROTO_SRCS} head ${PROTO_HDRS}")  
else()  
    message(FATAL_ERROR "protobuf library is needed but cant be found")  
endif()

# 需要搭配以下命令才能生成
add_executable(${PROJECT_NAME} ${PROTO_SRCS} ${PROTO_HDRS})  
target_link_libraries(${PROJECT_NAME} PRIVATE ${PROTOBUF_LIBRARIES})
```