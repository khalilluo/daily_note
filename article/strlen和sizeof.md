char str[20]="0123456789";
int a=strlen(str); //a=10; >>>> strlen 计算字符串的长度，以结束符 0x00 为字符串结束。
int b=sizeof(str); //而b=20; >>>> sizeof 计算的则是分配的数组 str[20] 所占的内存空间的大小，不受里面存储的内容改变。

上面是对静态数组处理的结果，如果是对指针，结果就不一样了

char* ss = "0123456789";
sizeof(ss) 结果 4 ＝＝＝》ss是指向[字符串常量](https://www.baidu.com/s?wd=字符串常量&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的字符指针，sizeof 获得的是一个指针的之所占的空间,应该是

长整型的，所以是4
sizeof(*ss) 结果 1 ＝＝＝》*ss是第一个字符 其实就是获得了字符串的第一位'0' 所占的内存空间，是char类

型的，占了 1 位

strlen(ss)= 10 >>>> 如果要获得这个字符串的长度，则一定要使用 strlen