CMAKE_PREFIX_PATH的作用是提供一个根目录供FIND_XXX()命令在其中查找相应的文件

工程中加入Qt
- CMakeLists文件中直接指定
```cmake
set(CMAKE_PREFIX_PATH /home/panocom/Qt/5.15.2/gcc_64)  
set(CMAKE_INCLUDE_CURRENT_DIR ON)  
set(CMAKE_AUTOUIC ON)  
set(CMAKE_AUTOMOC ON)  
set(CMAKE_AUTORCC ON)
```
- 编译时指定：cmake -DCMAKE_PREFIX_PATH=/home/panocom/Qt/5.15.2/gcc_64