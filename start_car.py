from ps4_ctrl_car import PS4Controller
if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
