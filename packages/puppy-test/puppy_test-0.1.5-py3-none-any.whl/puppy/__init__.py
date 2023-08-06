__version__ = "0.1.5"
__host__ = "http://172.32.4.219/puppy_test"

# __host__="http://r4735hqh7.hn-bkt.clouddn.com"
import os
import warnings
from urllib import request


def to_int(version):
    a = version.replace(".", "")
    return int(a)


def get_server_version() -> str:
    """从服务器取到最新的版本"""
    global __host__
    try:
        puppy_version_url = __host__ + "/version.txt"
        request.urlretrieve(puppy_version_url, "puppy_version.txt")
        with open("puppy_version.txt") as file:
            for line in file.readlines():
                version = line.strip()
        os.remove("puppy_version.txt")
        return version
    except:
        return None


def get_version() -> str:
    """获取当前框架版本"""
    global __version__
    return __version__


def upgrade_puppy_test():
    global __host__
    version = get_server_version()
    filename = "puppy_test-{}-py3-none-any.whl".format(version)
    if version is None:
        return
    puppy_test_url = __host__ + "/{}".format(filename)
    request.urlretrieve(puppy_test_url, filename)
    re = os.system("pip install {}".format(filename))
    os.remove(filename)
    return re


def check_version(version):
    if to_int(version) > to_int(get_version()):
        warnings.warn("puppy_test框架版本落后于脚本版本，请使用puppym upgrade命令升级puppy_test版本！", UserWarning)
    if to_int(version) < to_int(get_version()):
        warnings.warn('puppy_test框架版本高于脚本版本，请使用puppym update命令进行更新！', UserWarning)
