from argparse import ArgumentParser
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import threading
from sys import stdout
import logging
from hashlib import md5
from os import path

parser = ArgumentParser(description='For uploading files to Tencent Cloud COS.')
parser.add_argument("-bucket_name", "-b", required=True, type=str, help="bucket_name, COS bucketName.")
parser.add_argument("-secret_id", "-i", required=True, type=str, help="secret_id, The project identification "
                                                                      "ID owned by the developer is used for "
                                                                      "identity authentication and can be "
                                                                      "obtained on the API key management page.")
parser.add_argument("-secret_key", "-k", required=True, type=str, help="secret_key, The project identity key "
                                                                       "owned by the developer can be obtained "
                                                                       "on the API key management page.")
parser.add_argument("-region", "-r", required=True, type=str, help="region, COS bucket region.")
parser.add_argument("-local_path", "-lp", required=True, nargs="+", help="local_path, Local file storage path, "
                                                                         "Usually put the parameter at the end.")
parser.add_argument("-cos_path", "-cp", required=False, default="", help="cos_path, COS file storage path, "
                                                                         "default is 'root path'.")
parser.add_argument("-use_CDN", "-c", required=False, help="Optional, If you use CDN to "
                                                           "accelerate. This will return Default "
                                                           "CDN acceleration domain name, default "
                                                           "is 'False'")
parser.add_argument("-token", "-t", default=None, help="Optional, If you use a temporary key, you need to "
                                                       "pass in the Token, default is 'None'.")
parser.add_argument("-scheme", "-s", type=str, default="https", help="Optional, Specify to use the http/https "
                                                                     "protocol to access COS, default is 'https'")
parser.add_argument("-max_thread", "-m", required=False, default=5, help="Optional, Upload use max thread, "
                                                                         "default is '5'.")
parser.add_argument("-log", "-l", required=False, default=False, help="Optional, Whether to display the log, "
                                                                      "default is 'False'.")
args = parser.parse_args()

# logging setting
if args.log:
    logging.basicConfig(level=logging.INFO, stream=stdout,
                        format="%(asctime)s %(filename)s > %(message)s", datefmt="%Y/%m/%d %X")
else:
    logging.basicConfig(level=logging.WARNING, stream=stdout,
                        format="%(asctime)s %(filename)s > %(message)s", datefmt="%Y/%m/%d %X")


class Handle(threading.Thread):
    def __init__(self):
        super(Handle, self).__init__()
        self.fpath = None

    def run(self):
        logging.info(f"thread {self.name}, start.")
        while True:
            fpath = get_filepath()
            if not fpath:
                logging.info(f"thread {self.name}, end.")
                return
            else:
                self.fpath = fpath
                url = self.upload2cos()
                logging.info(f"file {self.fpath} url: {url}")
                put_fileURL(fpath, url)

    def get_file(self):
        try:
            with open(self.fpath, "rb") as img:
                imgBytes = img.read()
                return imgBytes
        except:
            return None

    def upload2cos(self):
        fileBytes = self.get_file()
        if not fileBytes:
            return ""
        else:
            fileRawName = path.basename(self.fpath)
            if len(fileRawName.split(".")) > 1:
                fileType = "." + fileRawName.split(".")[-1]
            else:
                fileType = ""
            fileTypeMD5 = md5(fileBytes + fileType.encode("utf-8")).hexdigest()
            logging.debug(f"file {self.fpath} [file+type] MD5: {fileTypeMD5}")
            fileHashName = fileTypeMD5 + fileType
            # try get cosFile message
            checkDic = client.list_objects(
                Bucket=args.bucket_name,
                Prefix="{}{}".format(args.cos_path, fileHashName),
            )
            logging.debug(f"file {self.fpath} COS exist info: {checkDic}")
            contents = checkDic.get("Contents")

            if contents is None:
                uploadDic = client.put_object(
                    Bucket=args.bucket_name,
                    Body=fileBytes,
                    Key="{}{}".format(args.cos_path, fileHashName),
                    StorageClass='STANDARD',
                    EnableMD5=False
                )
                logging.debug(f"file {self.fpath} upload info: {uploadDic}")
            else:
                fileCOSInfo = contents[0]
                cosFileName = path.basename(fileCOSInfo.get("Key"))
                if cosFileName == fileHashName:
                    logging.info(f"file {self.fpath} MD5 same as COS exist")
                else:
                    logging.warning(f"file {self.fpath} , may have been damaged, "
                                    f"that exists in COS but MD5 incorrect.")
                    return "error"
            if args.use_CDN:
                return "https://{}.file.myqcloud.com/{}{}".format(args.bucket_name, args.cos_path,
                                                                  fileHashName)
            else:
                return "https://{}.cos.{}.myqcloud.com/{}{}".format(args.bucket_name, args.region,
                                                                    args.cos_path, fileHashName)


if __name__ == '__main__':
    args = parser.parse_args()
    config = CosConfig(Region=args.region, SecretId=args.secret_id, SecretKey=args.secret_key,
                       Token=args.token, Scheme=args.scheme)
    client = CosS3Client(config)
    logging.info(f"Program parse info: {args}")
    filepath = args.local_path.copy()
    fp_lock = threading.Lock()
    fileURL = {}
    fu_lock = threading.Lock()


    def get_filepath():
        uploadPath = None
        fp_lock.acquire()
        if len(filepath) != 0:
            uploadPath = filepath.pop()
        fp_lock.release()
        return uploadPath


    def put_fileURL(fpath, url):
        fu_lock.acquire()
        fileURL[fpath] = url
        fu_lock.release()


    # create new thread
    thread_list = []
    for i in range(min(len(filepath), args.max_thread)):
        thread = Handle()
        thread.start()
        thread_list.append(thread)

    # wait thread
    for thread in thread_list:
        thread.join()

    # output
    for f in args.local_path:
        print(fileURL[f])
