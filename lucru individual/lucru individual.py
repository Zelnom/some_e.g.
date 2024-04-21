class Robot():
    garantie = 10
    number_of_robots = 0
    def __init__(self, nume, serial_number, hardware, software, age, sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.age = age
        self.sleep = sleep
        Robot.number_of_robots += 1

    def turn_on(self):
        if self.sleep == False:
            return f"{self.nume} is already running"
        else:
            self.sleep = False
            return f"{self.nume} turned on"
    def end_of_life(self):
        if self.age > self.garantie:
            print(f"{self.nume} is end of life")
        else:
            print(f"{self.nume} has {self.garantie - self.age} years till end of life")

r1 = Robot("John", "12333", "i5", "Python", "11", "True")

r1.turn_on()
# print(help(Robot))

print(r1.sleep)