**防止target和文件名一样**

当我们设置的target和当前目录下的文件名一样的话，target会被忽略，所以，通常，我们把target都用做phony target。



```makefile
# 防止以下target名和外部文件名称或者命令相同
.PHONY: build compile start push
 
# 版本号
VERSION_TAG = 1.7.0
MILESTONE_TAG = Sep.2019
REGISTRY = registry.local
NAME = registry.local/xxx.cn/demo
 
# 源码最后一次提交的commit id，使用commit id可以将docker镜像与提交的代码绑定在一起
COMMIT_ID := $(shell git rev-parse HEAD)
 
# 镜像构建的时间戳
BUILD_TS := $(shell date +'%Y%m%d%H%M%S')
 
# 源码分支
BRANCH_TAG := $(shell git rev-parse --abbrev-ref HEAD)
 
# 镜像版本信息
VERSION := $(VERSION_TAG)-build-$(BRANCH_TAG)-$(BUILD_TS)
 
# 镜像构建信息
BUILD := $(VERSION_TAG)-$(MILESTONE_TAG)-build-$(BUILD_TS)-$(BRANCH_TAG)-$(COMMIT_ID)
 
export GO111MODULE = on
 
# 编译源码
compile:
	go build -p 8 -o demo
 
build: build-version
 
# 默认读取当前目录下的Dockerfile。 --build-arg：给Dockerfile添加参数，BUILD=$(BUILD)中间不能有空格
build-version:
	docker build --build-arg BUILD=$(BUILD) -t $(NAME):$(VERSION) . >/dev/null
 
# docker image 打tag
tag-latest:
	docker tag $(NAME):$(VERSION) $(NAME):latest >/dev/null
 
# push 到镜像仓库
push: build-version tag-latest
	docker push $(NAME):$(VERSION); docker push $(NAME):latest
 
# 运行镜像
start:
	docker run -it --rm $(NAME):$(VERSION) /bin/bash

```


#### 删除指定镜像

``` makefile
DOCKER_IMAGE_NAME = your-docker-image-name

.PHONY: clean

clean:
    @if docker images $(DOCKER_IMAGE_NAME) | awk '{print $$2}' | grep -q -F $(DOCKER_IMAGE_TAG); then \
        docker rmi $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG); \
        echo "Docker image $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) deleted"; \
    else \
        echo "Docker image $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) not found"; \
    fi

```

#### 删除指定镜像版本
``` makefile

IMAGE_NAME = keepalived
IMAGE_VERSION = 0728

.PHONY: check-and-remove-image

check-and-remove-image:
	@if [ "$(shell docker images -q $(IMAGE_NAME):$(IMAGE_VERSION) 2> /dev/null)" != "" ]; then \
		docker rmi -f $(IMAGE_NAME):$(IMAGE_VERSION); \
	fi


```