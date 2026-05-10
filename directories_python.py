class employee:
    def __init__(self, name, age):
        self._name=name
        self._age=age
    def accessmeetingroom(self):
        print("access meeting room")
    
    def accesskitchen(self):
        print("access kitchen")
    
    def accesspersonaloffice(self):
        print("access personal office")
    
class advemployee(employee):
    
    def __init__(self, buisnessnumber, *args, **kwargs):
        self._buisnessnumber=buisnessnumber
        super().__init__(*args, **kwargs)
    def accessprivatemeetingroom(self):
        print("access private meeting room")


advancedemployee= advemployee(7891, "John", 28)
print(advancedemployee._age)
print(advancedemployee._buisnessnumber)

