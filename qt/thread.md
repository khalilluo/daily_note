```cpp

// 在thread2Obj中connect,区别是有没有this
connect(thread1Obj1, &Thread1Obj1::signal, [this]{
	// do something
	// 此处是thread1
})

connect(thread1Obj1, &Thread1Obj1::signal, this, [this]{
	// do something
	// 此处是thread2
})
```

