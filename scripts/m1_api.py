import time
import os

# 创建文件夹用于模拟存储拍照图片
if not os.path.exists("capture_img"):
    os.mkdir("capture_img")

class DroneController:
    def __init__(self):
        self.is_connected = False
        print("【模拟】无人机对象初始化完成，模拟IP：192.168.10.1")

    def connect(self):
        """模拟连接无人机"""
        print("【模拟】正在发送连接指令 command ...")
        time.sleep(0.8)
        self.is_connected = True
        print("【模拟】连接成功！无人机就绪")

    def takeoff(self):
        """模拟起飞"""
        if not self.is_connected:
            raise Exception("【连接失败故障】未连接无人机，无法起飞")
        print("【模拟】执行起飞动作")
        time.sleep(1)

    def land(self):
        """模拟降落"""
        if not self.is_connected:
            raise Exception("【连接失败故障】未连接无人机，无法降落")
        print("【模拟】执行降落动作")
        time.sleep(1)

    def move(self, direction, distance):
        """模拟前后左右移动
        direction: forward / back / left / right
        distance: 移动距离 cm
        """
        if not self.is_connected:
            raise Exception("【连接失败故障】未连接无人机，无法移动")
        print(f"【模拟】向{direction}方向移动 {distance} cm")
        time.sleep(0.6)

    def rotate(self, angle):
        """模拟旋转，正数右转，负数左转"""
        if not self.is_connected:
            raise Exception("【连接失败故障】未连接无人机，无法旋转")
        print(f"【模拟】机头旋转 {angle} 度")
        time.sleep(0.6)

    def capture_image(self):
        """模拟拍照，生成空白文件"""
        if not self.is_connected:
            raise Exception("【连接失败故障】未连接无人机，无法拍照")
        import datetime
        img_name = f"capture_img/photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        with open(img_name, "w", encoding="utf-8") as f:
            f.write("模拟拍摄图片文件")
        print(f"【模拟】拍照完成，图片保存路径：{img_name}")

    def emergency_stop(self):
        """模拟紧急停机"""
        print("【模拟】触发紧急停机，电机立刻断电！")

    def close(self):
        """释放资源"""
        if self.is_connected:
            print("【模拟】断开无人机连接，程序结束")
            self.is_connected = False
