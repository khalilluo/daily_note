### 创建
```cpp
std::tuple<double, char, std::string> get_student(int id) { 
	// C++11构建tuple的写法 
	if (id == 0) 
		return std::make_tuple(3.8, 'A', "Lisa Simpson"); 
	// C++17提供了更方便的构建tuple的写法 
	if (id == 0) 
		return { 3.8, 'A', "Lisa Simpson" }; 
		
	throw std::invalid_argument("id"); 
}
```

### 访问
```cpp
	auto student0 = get_student(0); 
	
	// 通过下标位置获取tuple中对应的元素 
	std::cout << "ID: 0, " 
		<< "GPA: " << std::get<0>(student0) << ", " 
		<< "grade: " << std::get<1>(student0) << ", " 
		<< "name: " << std::get<2>(student0) << '\n';

	// 通过tie将tuple中的元素解构至多个变量中 
	double gpa1; 
	char grade1; 
	std::string name1; 
		std::tie(gpa1, grade1, name1) = get_student(1); 
		std::cout << "ID: 1, "
			<< "GPA: " << gpa1 << ", " 
			<< "grade: " << grade1 << ", " 
			<< "name: " << name1 << '\n';

	// C++17结构化绑定
	auto [ gpa2, grade2, name2 ] = get_student(2);
```

