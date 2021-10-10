
# class Dad:
#     basketball =6

# class Son(Dad):
#     dance =1
#     basketball = 9
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"

# class Grandson(Son):
#     dance =6
#     guitar = 1

#     def isdance(self):
#         return f"Jackson yeah!" \
#             f"Yes I dance very awesomely {self.dance} no of times"

# darry = Dad()
# larry = Son()
# harry = Grandson()

# print(harry.guitar)

# # electronic device
# # pocket gadget
# # phone

class Electronic_device():
    power_source = "Alternating current or Direct Current"
    use = "Automates works and make the work very faster and efficient"
    start = "It is a kind of device which uses"
   
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}"

class Pocket_gadget(Electronic_device):
    power_source = "Direct current"
    addon_features = "It is portable and looks super awesome"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}"

class Phone(Pocket_gadget):
    use = "Its main feature is calling other person's phone to talk"
    
    def printdetails(self):
        return f"{self.start} {self.power_source} and {self.use}, {self.addon_features}"


Electronic_device_computer = Electronic_device()
Pocket_gadget_MiBrand = Pocket_gadget()
Phone_Redmi = Phone()


print("\n")
print(Electronic_device_computer.printdetails())
print("\n")
print(Pocket_gadget_MiBrand.printdetails())
print("\n")
print(Phone_Redmi.printdetails())
print("\n")