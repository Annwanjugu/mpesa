class Human:
    def James(self):
        print("i can walk")

    def tom(self):
        print("can run")
#
# hh = Human()
# print(hh.James())
# print(hh.tom())

class Racoon(Human):
    def racoon(self):
        print("can smile")

JJ =  Racoon()
print(JJ.racoon())
print(JJ.James())
print(JJ.tom())
cc = JJ.racoon+JJ.James+JJ.tom
print(cc)