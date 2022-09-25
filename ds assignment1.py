class Node:
    def __init__(self, s, x):
        self.age = 0
        self.name = ""
        self.next = None
        self.prev = None

        self.name = s
        self.age = x
        self.prev = None
        self.next = None

def main():
    father = Node("VIJAY YADAV", 51)
    mother = Node("SAVITRI DEVI", 44)
    brother = Node("VISHAL YADAV", 26)
    sister = Node("SANDHYA YADAV", 23)
    myself = Node("VISHWAJEET YADAV", 18)

    head = father

    father.prev = None
    father.next = mother
    mother.prev = father
    mother.next = brother
    brother.prev = mother
    brother.next = sister
    sister.prev = mother
    sister.next = myself
    myself.prev = sister
    myself.next = None

    Globals.printdll(head)


class Globals:

    def printdll(head):
        while head is not None:
            print(head.name, end = '')
            print("-", end = '')
            print(head.age, end = '')
            print("     ", end = '')
            head = head.next

if __name__ == "__main__":
    main()
