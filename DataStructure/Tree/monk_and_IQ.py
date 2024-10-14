class node:
    def __init__(self, x = None, c = None, index = None):
        self.x = [x] if not x else [0]
        self.index = index
        self.c = c
        self.next = None
        self.pri = self.c * sum(self.x)
    
    def addStudent(self, newIQ):
        if self.c >= 2:
            if newIQ > min(self.x):
                self.x.remove(min(self.x))
                self.x.append(newIQ)
        else:
            self.x.append(newIQ)
        
        self.c += 1
    
class priorityQ:
    def __init__(self):
        self.root = None
    
    def addToQ(self, node):
        if not self.root or node.pri > self.root.pri:
            self.root = node
        else:
            temp = self.root
            while temp.next != None and node.pri < temp.next.pri:
                temp = temp.next
            node.next = temp.next
            temp.next = node
    
    def addStudentToC(self, newIQ):
        temp = self.root
        self.root = self.root.next
        temp.addStudent(newIQ)
        self.addToQ(temp)
        return temp.index
    
    def showQ(self):
        temp = self.root
        while not temp:
            print(temp.index, end=' ')
            temp = temp.next
        print()

temp = list(map(int, input().split(' ')))
C, P, N = temp
Ns = list(map(int, input().split(' ')))
Ps = list(map(int, input().split(' ')))
Q = priorityQ()

for i in range(len(Ns)):
    Q.addToQ(node(c = 1, x = Ns[i], index = i + 1))
    Q.showQ()

for i in Ps:
    print(Q.addStudentToC(i), end=' ')