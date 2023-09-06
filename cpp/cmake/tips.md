变量和option之类的设置，如果不清理cache可能会导致设置失败 ^b607f1


#### 指定目标文件生成的位置  
CMAKE_SOURCE_DIR是CMakelist.txt文件所在目录
set_target_properties(simpleCpp PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)