```cmake
# 设置Qt安装目录
set(CMAKE_PREFIX_PATH /home/panocom/Qt/5.15.2/gcc_64)

# 配置Qt
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

# 添加Qt模块
find_package(QT NAMES Qt6 Qt5 COMPONENTS Core Quick REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Quick REQUIRED)

# 配置属性
target_compile_definitions(dataApiTest
    PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
    
# 增加依赖库
target_link_libraries(dataApiTest
    PRIVATE Qt${QT_VERSION_MAJOR}::Core
    Qt${QT_VERSION_MAJOR}::Quick)
    
# 配置程序
if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(dataApiTest
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
        )
    # Define target properties for Android with Qt 6 as:
    #    set_property(TARGET dataApiTest APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
    #                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
    # For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(dataApiTest SHARED
            ${PROJECT_SOURCES}
            )
        # Define properties for Android with Qt 5 after find_package() calls as:
        #    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(dataApiTest
            ${PROJECT_SOURCES}
            )
    endif()
endif()
```

