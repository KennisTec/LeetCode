class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):


    def addTwoNumbers(self, l1, l2):        
        totalSum = 0
        carryNumber = 0
        res = None
        prev = None
        
        while l1 is not None or l2 is not None:
            totalSum = carryNumber + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carryNumber = (1 if totalSum >= 10 else 0)
            totalSum = totalSum % 10
            temp = ListNode(totalSum)
            if res is None:
                res = temp
            else:
                prev.next = temp
            prev = temp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carryNumber > 0 :
            temp.next = ListNode(carryNumber)

        return res

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

# Utility function to print the list


def printList(n):
    while n:
        print(n.val, end = ' ')
        n = n.next
    print()


# Driver Code
if __name__ == "__main__":

    arr1 = [2,4,9] #[7, 5, 9, 4, 6] 942
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)
    print("First list is", end = " ")
    printList(LL1.head)

    arr2 = [5,6,4,9] #[8, 4] 9465 + 942
    LL2 = LinkedList()
    for i in arr2:
        LL2.insert(i)
    print("Second list is", end = " ")
    printList(LL2.head)

    # Function Call
    res = Solution()
    res = Solution().addTwoNumbers(LL1.head, LL2.head)
    print("Resultant list is", end = " ")
    printList(res)
    # values = Solution()
    # print(values.addTwoNumbers([0],[0]))
    # print(values.addTwoNumbers([0],[0]))
    # print(values.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))

    # print(9999+ 9999999)

