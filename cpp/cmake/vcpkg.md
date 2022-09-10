## Clion

设置->构建、执行、部署->CMake选项

```cmake
-DCMAKE_TOOLCHAIN_FILE=[vcpkg root]/scripts/buildsystems/vcpkg.cmake
```

这样就可以使用vcpkg安装的库了

```
findPacket()
```


注意设置CMAKE_TOOLCHAIN_FILE后CMAKE_PREFIX_PATH会有对应的属性，如果需要设置后者则需要将之前的属性添加回去
```cmake
set(CMAKE_PREFIX_PATH &{CMAKE_PREFIX_PATH} C:\\Qt\\5.15.2\\msvc2019_64 )

# 注意打印看看是否设置成功，工具链的设置是否又被覆盖了

```