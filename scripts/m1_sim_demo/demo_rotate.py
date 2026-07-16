import sys
import os
# 获取当前demo文件所在文件夹路径
current_dir = os.path.dirname(__file__)
# 拼接出scripts文件夹完整路径
scripts_path = os.path.join(current_dir, "..")
# 将scripts文件夹加入Python搜索路径
sys.path.append(scripts_path)
from m1_api import DroneController
import time

if __name__ == "__main__":
    drone = DroneController()
    try:
        drone.connect()
        drone.takeoff()
        time.sleep(1)
        drone.rotate(90)
        time.sleep(1)
        drone.rotate(-90)
        time.sleep(1)
        drone.land()
    except Exception as e:
        print("程序异常：", e)
    finally:
        drone.close()
