target_link_libraries的时候填写库名称或者文件名称

DCMAKE_TOOLCHAIN_FILE cmake的packet目录

### CMake增加版本(源码使用cmake变量)

1. target_compile_definitions(${PROJECT_NAME}  PRIVATE PRODUCTION_VERSION="01.01.01" )
2. add_definitions( -DPRODUCTION_VERSION="01.01.01")
3. cmake .. -DCMAKE_CXX_FLAGS="-DEX3"

