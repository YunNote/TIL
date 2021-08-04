# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cl1 = self.listNodeToList(l1)
        cl2 = self.listNodeToList(l2)

        cl1.reverse()
        cl2.reverse()
        cl1 = int("".join(list(map(str, cl1))))
        cl2 = int("".join(list(map(str, cl2))))
        total = cl1 + cl2

        header = None
        link = None

        for x in str(total):
            if header is None:
                header = ListNode(x)
                link = header;
            else:
                link = ListNode(x, link)

        return link

    def listNodeToList(self, ln: ListNode):
        result = []
        currNode = ln;

        while True:
            result.append(currNode.val)
            currNode = currNode.next

            if currNode is None:
                break;

        return result


if __name__ == '__main__':

    Solution().addTwoNumbers(ListNode(2,ListNode(4, ListNode(3))), ListNode(5,ListNode(6, ListNode(4))))

