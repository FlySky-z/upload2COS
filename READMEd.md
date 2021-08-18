
# A COS service for Typora.

This is a project is a simple COS used for image host.

这是一个简易的图床上传命令行.

## Getting Started

The usage is shown below


<img src="https://flysky-1302120781.file.myqcloud.com/7cdacb47f0487ec96f2cc4140a81024f.gif">


## Prerequisites

What things you need to install the software and how to install them

```
Typora 
```

## Installing

#### MacOS

<img src="https://jarviszuo-tencent-img-1302316844.cos.ap-chengdu.myqcloud.com/img/markdownImg/a91955802fc9ea614a5cca7dbbebd154.png" alt="image-20210819010128371" style="zoom:50%;" />

#### Windows

<img src="https://jarviszuo-tencent-img-1302316844.cos.ap-chengdu.myqcloud.com/img/markdownImg/8f7a074da66deecd32fa089f039c7638.png" alt="image-20210819010242356" style="zoom:50%;" />


## Running the tests

Explain how to run the automated tests for this system

```shell
GOROOT=/Users/jason/go/go1.17 #gosetup
GOPATH=/Users/jason/go #gosetup
/Users/jason/go/go1.17/bin/go test -c -o /private/var/folders/19/1wgy0cwd1pl5jv6typ52w68w0000gn/T/GoLand/___go_test_github_com_Jsoneft_cos_service_client.test github.com/Jsoneft/cos_service/client #gosetup
/Users/jason/go/go1.17/bin/go tool test2json -t /private/var/folders/19/1wgy0cwd1pl5jv6typ52w68w0000gn/T/GoLand/___go_test_github_com_Jsoneft_cos_service_client.test -test.v -test.paniconexit0
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* GO

## Authors

* **Jarvis zuo** - *Initial work* - [Jarvis](https://github.com/jsoneft)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
