from m1_api import DroneController
import time

if __name__ == "__main__":
    print("===== M1 完整飞行闭环测试 =====")
    drone = DroneController()
    try:
        drone.connect()
        drone.takeoff()
        time.sleep(1)
        drone.move("forward", 40)
        time.sleep(1)
        drone.rotate(180)
        time.sleep(1)
        drone.capture_image()
        time.sleep(1)
        drone.land()
    except Exception as e:
        print("飞行流程异常：", e)
    finally:
        drone.close()
