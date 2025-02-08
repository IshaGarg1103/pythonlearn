from Chef import Chef

class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes Orange chicken")
        super().make_special_dish() #calls the parent class
    def make_fried_rice(self):
        print("The chef makes fried rice")