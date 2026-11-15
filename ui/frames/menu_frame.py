import tkinter as tk

# Класс главного меню, объектом является само окно главного меню
class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        
        tk.Label(self, text="Главное меню", font=("Arial", 18)).pack(pady=20)
        
        tk.Button(self, text="Добавить деньги", width=25,
                  command=lambda: self.controller.show_frame("AddMoneyFrame")).pack(pady=5)
        tk.Button(self, text="Изменить проценты", width=25,
                  command=lambda: self.controller.show_frame("ChangeProcentFrame")).pack(pady=5)
        tk.Button(self, text="Посмотреть баланс", width=25,
                  command=lambda: self.controller.show_frame("SeeBalanceFrame")).pack(pady=5)