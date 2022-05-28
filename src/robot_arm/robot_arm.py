from time import sleep
from pyfirmata import Arduino, util, SERVO, PWM

class RobotArm:
    def __init__(self) -> None:
        # Arduino config
        try:
            print("Connect to Arduino One, Wait please...!")
            self.board = Arduino("COM3")
            sleep(3)
            print("Connected...") 
        except:
            print("Error connection...")


    def connection(self):
        #base hombros brazos muñeca pinzas
        #
        # Available Pins
        # 1  2  3  4  5  6  7  8
        # 3, 4, 5, 6, 7, 8, 9, 10
        # Pinzas
        self.board.digital[9].mode = SERVO
        self.board.digital[9].write(20)

        # Muñeca
        self.board.digital[8].mode = SERVO
        self.board.digital[8].write(5)
        
        # Brazos
        self.board.digital[6].mode = SERVO
        self.board.digital[7].mode = SERVO
        self.board.digital[7].write(90)

        # Hombros
        self.board.digital[4].mode = SERVO
        self.board.digital[4].write(110)

        self.board.digital[5].mode = SERVO        
        self.board.digital[5].write(110)

        # Base
        self.board.digital[3].mode = SERVO



    def move_base(self, position: int):        
        self.board.digital[3].write(position)
        print(f"base {position}")


    def move_shoulders(self, position: int):
        self.board.digital[4].write(position)        
        self.board.digital[5].write(position)        
        print(f"Shoulders {position}")


    def move_arm_botton(self, position: int):
        self.board.digital[6].write(position)
        print(f"Arm bottom {position}")


    def move_arm_top(self, position: int):
        self.board.digital[7].write(position)
        print(f"Arm top {position}")


    def move_arm_wrist(self, position: int):
        self.board.digital[8].write(position)
        print(f"Wrist  {position}")


    def move_arm_gripper(self, position):
        self.board.digital[9].write(position)
        print(f"Gripper  {position}")
