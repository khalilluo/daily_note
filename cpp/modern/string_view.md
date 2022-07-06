#### string_view

std::string_view是C++ 17标准中新加入的类，正如其名，它提供一个字符串的视图，即可以通过这个类以各种方法“观测”字符串，但不允许修改字符串。由于它只读的特性，它并不真正持有这个字符串的拷贝，而是与相对应的字符串共享这一空间。即——构造时不发生字符串的复制。同时，你也可以自由的移动这个视图，移动视图并不会移动原定的字符串。

正因这些特性，当你不需要改变字符串时，应当抛弃原来使用的const string而采用新的string_view，这样可以避免多余的字符串拷贝

```cpp
// using namespace std;
string_view sv("123456789", 5);

// 支持Range-based for
for (auto i : sv) {
    cout << i << ' ';
}
// 支持begin/end, cbegin/cend, rbegin/rend, crbegin/crend迭代器
for (auto it = sv.crbegin(); it != sv.crend(); ++it) {
    cout << *it << ' ';
}

cout << sv.at(0) << ' ' << sv[1]; // 输出指定位置上的字符
cout << sv.front();  // 输出首位字符
cout << sv.back();   // 输出末位字符
cout << sv.size() << ' ' << sv.length(); // 输出视图中的字符串长度
cout << sv.data();   // 输出字符串存储的位置
cout << sv.empty();  // 输出字符串是否为空
cout << sv.substr(0, 2); // 输出字符串的子串(用法与string的一致)

string_view sv2("12345");
cout << (sv == sv2 ? "true" : "false"); // 支持同string一样的各种比较符号


string_view sv3("123456789");
sv3.remove_suffix(1);    // 现在sv3中为：12345678, sv3的大小为8
sv3.remove_prefix(2);    // 现在sv3中为: 345678, sv3的大小为6
```

注意对象的生命周期

```cpp
std::string_view getView() {
    char ar[] = "Example";
    return { ar };
}

std::string getString() {
    char ar[] = "Example";
    return { ar };
}


int main(int argc, char *argv[])
{
    auto && v = getView();		// v 是空的，变量已经删除，右值引用也无法延长
    auto && s = getString();	// 可以正常延长生命周期
    std::cout << v << std::endl;
    std::cout << s << std::endl;
    return 0;
}
```

#### 便利性

在string_view面世之前，一个接受const char*的函数， 加入想要传入string， 还需要把string使用c_str()转换才行。而现在，string_view可以完全兼容两者

```c++
void f1(const string& str) { …… } // C++17以前
void f2(string_view sv) { …… } // C++17以后

const char* s = "1234567890abcdefghijklmn";

f1(s); // 会创建临时的string，发生内存的分配和拷贝
f2(s); // 不会发生内存分配
```



#### 陷阱

1.string_view并没有尾0 （'\0），所以在输出的时候，要注意边界。
 2.因为string_view并不拷贝内存，所以要特别注意它所指向的字符串的生命周期。string_view指向的字符串，不能再string_view死亡之前被回收。

```cpp
string replace_post(string_view src, string_view new_post)
{
    auto pos = src.find(".") + 1;
    // 取出点及点之前的全部字符，string_view的substr会返回一个string_view对象，所以要取data()赋值给string对象
    string_view sv1 = src.substr(0, pos); // substr能正确返回字符串
    string s1 = sv1.data(); 
    cout << "sv1 = " << sv1 << ", s1=" << s1 << endl;
	// 输出 sv1 = abcdefg., s1=abcdefg.xxx   因为data返回的指针没有尾0
    return s1 + new_post.data();
}



int main(int argc, char *argv[])
{
    string sss =  "abcdefg.xxx";
    string_view sv = sss;
    string s = replace_post(sv, "yyy");

    cout << sv << " after replaced : " << s << endl;
    return 0;
}

// 输出 abcdefg.xxx after replaced : abcdefg.xxxyyy
```



#### O(n) versus O(1)

std::string 和 std::string_view 都有 substr 方法, std::string 的 substr 方法返回的是字符串的子串,而 std::string_view 的 substr 返回的则是字符串子串的"视图".听上去似乎两个方法功能上比较相似,但他们之间有一个非常大的差别: **std::string::substr 是线性复杂度, std::string_view::substr 则是常数复杂度**.这意味着 std::string::substr 方法的性能取决于字符串的长度,而std::string_view::substr 的性能并不受字符串长度的影响.