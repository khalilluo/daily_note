
```shell

#!/bin/bash

# 循环执行
echo "What is your favourite OS?"
select name in "Linux" "Windows" "Mac OS" "UNIX" "[Android](http://c.biancheng.net/android/)"
do
    echo $name
done
echo "You have selected $name"

# 每次循环时 select 都会要求用户输入菜单编号，并使用环境变量 PS3 的值作为提示符，PS3 的默认值为`#?`，修改 PS3 的值就可以修改提示符
PS3="请选择：(1-6):"  
select MENU in  "asd" "2" "中文" "asdf" "更多发生过" 退出 ;do  
case $REPLY in  
1)  
        Master_Change_config  
        ;;  
2)  
        create_Replication_user  
        ;;  
3)  
        Backup  
        ;;  
4)  
        Slave_Change_config  
        ;;  
5)  
        master_check  
        ;;  
6)  
        exit  
esac  
done
```