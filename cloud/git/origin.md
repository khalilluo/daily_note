你的代码库 (repository) 可以存放在你的电脑里，同时你也可以把代码库托管到 Github 的服务器上。

在默认情况下，origin 指向的就是你本地的代码库托管在 Github 上的版本。

我们假设你首先在 github 上创建了一个 Repository，叫做 repository，假设你的 Github ID 是 user1, 这个时候指向你的代码库的链接是

`   https://github.com/user1/repository  `

如果你在 terminal 里输入

`   git clone https://github.com/user1/repository     `

那么 git 就会在本地拷贝一份托管在 github 上的代码库

这个时候你 cd 到 repository

然后输入

`` `   git remote -v  登录后复制   `     ``

你会看到控制台输出
```
origin https://github.com/user1/repository.git (fetch) origin https://github.com/user1/repository.git (push)     
```

也就是说 git 为你默认创建了一个指向远端代码库的 origin（因为你是从这个地址 clone 下来的）

再假设现在有一个用户 user2 fork 了你个 repository，那么他的代码库链接就是这个样子

```
https://github.com/user2/repository
``` 

如果他也照着这个 clone 一把，然后在他的控制台里输入

```
git remote -v
```

他会看的的就是

```
origin https://github.com/user2/repository.git (fetch) origin https://github.com/user2/repository.git (push) 
```

可以看的 origin 指向的位置是 user2 的的远程代码库

这个时候，如果 user2 想加一个远程指向你的代码库，他可以在控制台输入

```
git remote add upstream https://github.com/user1/repository.git
```

然后再输入一遍 git remote -v

输出结果就会变为

``` shell
origin https://github.com/user2/repository.git (fetch) 
origin https://github.com/user2/repository.git (push) 
upstream https://github.com/user1/repository.git (push) 
upstream https://github.com/user1/repository.git (push)

```

增加了指向 user1 代码库的 upstream，也就是之前对指向位置的命名。

总结来讲，顾名思义，origin 就是一个名字，它是在你 clone 一个托管在 Github 上代码库时，git 为你默认创建的指向这个远程代码库的标签