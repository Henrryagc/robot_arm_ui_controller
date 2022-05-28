import tkinter as tk
import src.ui.ui_commands as uic


class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #self.pack()
        # Initialize ARM and Connection
        uic.init_arm()
        self.title = tk.Label(container, text="Controladores para Servos")
        self.title.pack()

        # Pinzas
        self.init_gripper(container)

        # Muñeca
        self.init_wrist(container)

        # Brazos        
        self.init_arm_top(container)
        self.init_arm_bottom(container)
        
        # Hombros
        self.init_shoulders(container)

        # Base 
        self.init_base(container)


    def init_gripper(self, master):
        self.title = tk.Label(master, text="Pinzas")
        self.title.pack()
        self.gripper_arm = tk.Scale(master, from_= 20, to=60, orient=tk.HORIZONTAL, command=uic.gripper)
        self.gripper_arm.pack()


    def init_wrist(self, master):
        self.title = tk.Label(master, text="Muñeca")
        self.title.pack()
        self.wrist_arm = tk.Scale(master, from_= 5, to=180, orient=tk.HORIZONTAL, command=uic.wrist)
        self.wrist_arm.pack()


    def init_arm_top(self, master):
        self.title = tk.Label(master, text="Brazo Arriba")
        self.title.pack()
        self.arms_arm = tk.Scale(master, from_= 0, to=180, orient=tk.HORIZONTAL, command=uic.arm_top)
        self.arms_arm.pack()


    def init_arm_bottom(self, master):
        self.title = tk.Label(master, text="Brazo Abajo")
        self.title.pack()
        self.arms_arm = tk.Scale(master, from_= 0, to=180, orient=tk.HORIZONTAL, command=uic.arm_bottom)
        self.arms_arm.pack()


    def init_shoulders(self, master):
        self.title = tk.Label(master, text="Hombros")
        self.title.pack()
        self.shoulders_arm = tk.Scale(master, from_= 20, to=180, orient=tk.HORIZONTAL, command=uic.shoulders)
        self.shoulders_arm.pack()


    def init_base(self, master):
        self.title = tk.Label(master, text="Base")
        self.title.pack()
        self.base_arm = tk.Scale(master, from_= 0, to=180, orient=tk.HORIZONTAL, command=uic.base)
        self.base_arm.pack()



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Robot App')
        self.geometry('300x500')
        #self.configure(bg='red')

