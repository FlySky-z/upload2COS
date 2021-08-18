# upload2COS
用于将文件上传至腾讯云（qcloud）的对象存储（COS），使用Python语言完成。

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

## Example

```bash
."D:\\Drive\COSupload.exe" -b "xxx-1231231231" -i "ABCDEFGHIJKLMNOPQ" -k "ABCDEFGHIJKLMNOPQRST" -cp "img/" -r "ap-chengdu" -lp
```
