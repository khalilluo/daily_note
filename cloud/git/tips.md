### 单次重复输密码

输入  git config --global credential.helper store
再操作一次git pull，然后它会提示你输入账号密码，这一次之后就不需要再次输入密码了


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

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

### gitpush提示鉴权失败

settings->developer settings->personanl access tokens -> generate new tokens 

#### window和linux文件格式
```shell

# AutoCRLF
# 提交时转换为LF，检出时转换为CRLF
git config --global core.autocrlf true
# 提交时转换为LF，检出时不转换
git config --global core.autocrlf input
# 提交检出均不转换
git config --global core.autocrlf false

# SafeCRLF
# 拒绝提交包含混合换行符的文件
git config --global core.safecrlf true
# 允许提交包含混合换行符的文件
git config --global core.safecrlf false
# 提交包含混合换行符的文件时给出警告
git config --global core.safecrlf warn

```

