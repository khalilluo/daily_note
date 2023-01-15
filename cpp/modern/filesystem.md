### 常用类
path类：说白了该类只是对字符串（路径）进行一些处理，这也是文件系统的基石。
directory_entry 类：功如其名，文件入口，这个类才真正接触文件。 
directory_iterator 类：获取文件系统目录中文件的迭代器容器，其元素为 directory_entry对象（可用于遍历目录）
file_status 类：用于获取和修改文件（或目录）的属性（需要了解C++11的强枚举类型（即枚举类））

```c++

std::filesystem::path str("C:\\Windows");  
if (!std::filesystem::exists(str))    //必须先检测目录是否存在才能使用文件入口.  
    return;  
  
std::filesystem::directory_entry entry(str);      //文件入口  
if (entry.status().type() == std::filesystem::file_type::directory)    //这里用了C++11的强枚举类型  
    std::cout << "该路径是一个目录" << std::endl;  
std::filesystem::directory_iterator list1(str);            //文件入口容器  
for (auto& it:list1) {  
    std::cout << it.path().filename() << std::endl;        //通过文件入口（it）获取path对象，再得到path对象的文件名，将之输出  
    std::cout << it.last_write_time().time_since_epoch()<< std::endl; 
}
    
```