from unittest.main import main


class Stack:

    def __init__(self):
        self.s = []
    
    # Xuat Stack
    def PrintStack(self):
        i=0
        length=len(self.s)
        while (i<length):
            print(self.s[i])
            i+=1

    # Kiem tra Stack rong
    def Is_Empty(self):
        if (len(self.s) !=0):
            return False
        else:
            return True 
    # Them phan tu vao Stack
    def Push(self,key):
        self.s.append(key)

    # Lay phan tu ra khoi Stack
    def Pop(self):
        return self.s.pop()

    # Lay phan tu o Top
    def Top(self):
        if self.Is_Empty(self):
            print(' Stack is Empty')
        else:
            return self.s[-1]


if __name__ == "__main__":
    S=Stack()
    nhap=input()
    n=int(nhap)
    for i in range (0,n):
        temp=input()
        S.Push(temp)
    
    S.PrintStack()