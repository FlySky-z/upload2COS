# upload2COS

用于将文件上传至腾讯云（qcloud）的对象存储（COS），使用Python语言完成。

# 简介

> 项目基于腾讯云提供的PythonSDK接口编写。

# 使用

## Release
下载地址：https://github.com/FlySky-z/upload2COS/releases/tag/V1.0


## 源码安装
### 1. 安装PythonSDK
```bash
pip install -U cos-python-sdk-v5
```

### 2. 配置文件

#### Example（For Release）

```bash
."D:\\Drive\COSupload.exe" -b "xxx-1231231231" -i "ABCDEFGHIJKLMNOPQ" -k "ABCDEFGHIJKLMNOPQRST" -cp "img/" -r "ap-chengdu" -lp
```
参数解释：
* `-b` （必填）表示存储桶名称；
* `-i` （必填）表示SECRET_ID，为腾讯云的API密钥ID；
* `-k` （必填）表示SECRET_KEY，为腾讯云API密钥KEY；
* `-r` （必填）表示存储桶地区；
* `-cp` 指定所上传的图片位于存储桶内的目录（如果为根目录则无需填写）；
* `-lp` （放置最后）指定本地图片的路径。


### 3. 各参数说明

* 对于`Release`文件，则可以在命令行通过`-h`参数查询各参数；
* 对于源码可以通过`python main.py -h`查询各参数。

```
usage: main.py [-h] -bucket_name BUCKET_NAME -secret_id SECRET_ID -secret_key SECRET_KEY -region REGION -local_path LOCAL_PATH [LOCAL_PATH ...] [-cos_path COS_PATH]
               [-use_CDN USE_CDN] [-token TOKEN] [-scheme SCHEME] [-max_thread MAX_THREAD] [-log LOG]

For uploading files to Tencent Cloud COS.

optional arguments:
  -h, --help            show this help message and exit
  -bucket_name BUCKET_NAME, -b BUCKET_NAME
                        bucket_name, COS bucketName.
  -secret_id SECRET_ID, -i SECRET_ID
                        secret_id, The project identification ID owned by the developer is used for identity authentication and can be obtained on the API key management page.
  -secret_key SECRET_KEY, -k SECRET_KEY
                        secret_key, The project identity key owned by the developer can be obtained on the API key management page.
  -region REGION, -r REGION
                        region, COS bucket region.
  -local_path LOCAL_PATH [LOCAL_PATH ...], -lp LOCAL_PATH [LOCAL_PATH ...]
                        local_path, Local file storage path, Usually put the parameter at the end.
  -cos_path COS_PATH, -cp COS_PATH
                        cos_path, COS file storage path, default is 'root path'.
  -use_CDN USE_CDN, -c USE_CDN
                        Optional, If you use CDN to accelerate. This will return Default CDN acceleration domain name, default is 'False'
  -token TOKEN, -t TOKEN
                        Optional, If you use a temporary key, you need to pass in the Token, default is 'None'.
  -scheme SCHEME, -s SCHEME
                        Optional, Specify to use the http/https protocol to access COS, default is 'https'
  -max_thread MAX_THREAD, -m MAX_THREAD
                        Optional, Upload use max thread, default is '5'.
  -log LOG, -l LOG      Optional, Whether to display the log, default is 'False'.
```


