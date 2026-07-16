from m1_api import DroneController

def test_connect_fail():
    print("===== 测试1：连接失败故障 =====")
    drone = DroneController()
    try:
        drone.connect()
    except Exception as e:
        print("捕获故障：", e)

if __name__ == "__main__":
    test_connect_fail()
