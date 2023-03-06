"""
@Date:        2023/2/6 下午2:07
@Author:      wyj
@FileName:    check_file_change.py
@Description: None
"""
import shutil
import time


def get_md5():
    import hashlib

    with open(filename, "rb") as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    return file_md5


if __name__ == "__main__":
    """
    nohup python3 check_file_change.py &
    """
    last_md5 = ""
    while True:
        filename = (
            "/home/wyj/PycharmProjects/file/change/__init__.py"
        )
        target_filename = "/home/wyj/test-file/test.py"
        exec_result_file = "/opt/check_file.txt"
        now_md5 = get_md5()
        if last_md5 != now_md5:
            last_md5 = now_md5
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"{now_time} File has changed!")
            shutil.copy(filename, target_filename)
            with open(exec_result_file, "a+") as erf:
                erf.write(f"{now_time} File has changed!\n")
        else:
            print("Success")
        time.sleep(5)
