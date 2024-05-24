class Inset():
    def __init__(self) -> None:
        self.my_list = []
        
    def insert(self, element):
        if not self.member(element):
            self.my_list.append(element)
        else:
            print(f"Element {element} already added!")
        
    def member(self, element):
        if element in self.my_list:
            return True
        return False

    def remove(self, element):
        if element in self.my_list:
            raise ValueError("ვერ ვიპოვნე")
        
        self.my_list.remove(element)
        
    
    def __str__(self) -> str:
        self.my_list.sort()
        
        return "".join(map(str, self.my_list))
    
inset = Inset()

inset.insert(5)
inset.insert(6)
inset.insert(8)
inset.insert(1)
print(inset)
inset.remove(5)
inset.remove(5)
print(inset)
