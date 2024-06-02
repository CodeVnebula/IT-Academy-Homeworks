class MyList(list):
    def __init__(self, my_list) -> None:
        self.my_list = my_list
        super().__init__(self.my_list)
    
    def min(self):
        if not self.my_list:
            raise ValueError("List empty")
        return min(self.my_list)
    
    def max(self):
        if not self.my_list:
            raise ValueError("List empty")
        return max(self.my_list)
    
my_list = MyList([1, 2, 3, 5, 7, 0, -4, 4])

print(my_list.max())    # 7
print(my_list.min())    # -4

another_list = MyList([])

print(another_list.min())   # list empty error
print(another_list.max())   # list emtpy error
