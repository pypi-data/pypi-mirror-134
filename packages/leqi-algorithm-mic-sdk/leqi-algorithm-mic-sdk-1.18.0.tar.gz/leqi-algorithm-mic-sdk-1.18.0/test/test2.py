import time

from algorithm_mic_sdk.algorithms.cutout_and_beauty import CutoutAndBeautyClassic
from algorithm_mic_sdk.auth import ClassicAuthInfo
from algorithm_mic_sdk.tools import FileInfo

host = 'http://nyasu.leqi.us:17013'  # 算法host地址
user_name = 'panso'
password = '0bdca2d8-4a3d-11eb-addb-0242c0a80006'
classic_password = 'rongsuo'
classic_user_name = 'pan'

filename = 'src/证件照/色彩问题.jpeg'  # 需要处理的文件名

file_info = FileInfo.for_file_bytes(open(filename, 'rb').read() + b'5676')
auth_info = ClassicAuthInfo(classic_user_name=classic_user_name, classic_password=classic_password, user_name=user_name,
                            password=password, host=host, gateway_cache=False, extranet=True)
process = 'image/auto-orient,1/format,jpeg'
cutout_and_beauty = CutoutAndBeautyClassic(auth_info, file_info, need_original_background=True)
print(cutout_and_beauty.json)
t0 = time.time()
resp = cutout_and_beauty.synchronous_request(timeout=500)
print(resp.json)
if resp.code == 200:
    for result_im_oss_name in resp.json['result']['result_im_oss_names']:
        print(cutout_and_beauty.get_classic_file_url(result_im_oss_name))
    print(resp.algo_server_timing, time.time() - t0)
