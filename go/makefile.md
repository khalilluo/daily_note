含一定复杂度的软件工程，基本上都是先编译 A，再依赖 B，再编译 C…，最后才执行构建

如果每次都人为编排，又或是每新来一个同事就问你项目 D 怎么构建、重新构建需要注意什么…等等情况，岂不是要崩溃？

我们常常会在开源项目中发现 Makefile，你是否有过疑问？

## 怎么解决

## Make

### 是什么

Make 是一个构建自动化工具，会在当前目录下寻找 Makefile 或 makefile 文件。如果存在，会依据 Makefile 的**构建规则**去完成构建

当然了，实际上 Makefile 内都是你根据 make 语法规则，自己编写的特定 Shell 命令等

它是一个工具，规则也很简单。在支持的范围内，编译 A， 依赖 B，再编译 C，完全没问题

### 规则

Makefile 由多条规则组成，每条规则都以一个 target（目标）开头，后跟一个 : 冒号，冒号后是这一个目标的 prerequisites（前置条件）

紧接着新的一行，必须以一个 tab 作为开头，后面跟随 command（命令），也就是你希望这一个 target 所执行的构建命令

```makefile
[target] ... : [prerequisites] ...
<tab>[command]
    ...
    ...
```

- target：一个目标代表一条规则，可以是一个或多个文件名。也可以是某个操作的名字（标签），称为**伪目标（phony）**
- prerequisites：前置条件，这一项是**可选参数**。通常是多个文件名、伪目标。它的作用是 target 是否需要重新构建的标准，如果前置条件不存在或有过更新（文件的最后一次修改时间）则认为 target 需要重新构建
- command：构建这一个 target 的具体命令集

### 简单的例子

本文将以 [go-gin-example](https://github.com/EDDYCJY/go-gin-example) 去编写 Makefile 文件，请跨入 make 的大门

#### 分析

在编写 Makefile 前，需要先分析构建先后顺序、依赖项，需要解决的问题等

#### 编写

```makefile
.PHONY: build clean tool lint help
all: build
build:
    go build -v .
tool:
    go tool vet . |& grep -v vendor; true
    gofmt -w .
lint:
    golint ./...
clean:
    rm -rf go-gin-example
    go clean -i .
help:
    @echo "make: compile packages and dependencies"
    @echo "make tool: run specified go tool"
    @echo "make lint: golint ./..."
    @echo "make clean: remove object files and cached files"
```

1、在上述文件中，使用了 `.PHONY`，其作用是声明 build / clean / tool / lint / help 为**伪目标**，声明为伪目标会怎么样呢？

- 声明为伪目标后：在执行对应的命令时，make 就不会去检查是否存在 build / clean / tool / lint / help 其对应的文件，而是每次都会运行标签对应的命令
- 若不声明：恰好存在对应的文件，则 make 将会认为 xx 文件已存在，没有重新构建的必要了

2、这块比较简单，在命令行执行即可看见效果，实现了以下功能：

1. make: make 就是 make all
2. make build: 编译当前项目的包和依赖项
3. make tool: 运行指定的 Go 工具集
4. make lint: golint 一下
5. make clean: 删除对象文件和缓存文件
6. make help: help

#### 为什么会打印执行的命令

如果你实际操作过，可能会有疑问。明明只是执行命令，为什么会打印到标准输出上了？

##### 原因

make 默认会打印每条命令，再执行。这个行为被定义为**回声**

##### 解决

可以在对应命令前加上 @，可指定该命令不被打印到标准输出上

```makefile
build:    @go build -v .
```

