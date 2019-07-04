"""
147. Insertion Sort List

Sort a linked list using insertion sort.

Input: 4->2->1->3
Output: 1->2->3->4


Input: -1->5->3->4->0
Output: -1->0->3->4->5

result:

Runtime: 1616 ms, faster than 44.36% of Python3 online submissions for Insertion Sort List.
Memory Usage: 15.1 MB, less than 46.25% of Python3 online submissions for Insertion Sort List.



"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    @staticmethod
    def construct(data_list):
        head = ListNode(data_list[0])
        rail = head
        for d in data_list[1:]:
            node = ListNode(d)
            rail.next = node
            rail = rail.next
        rail.next = None
        return head

    def __str__(self):
        data_list = []
        h = self
        while h is not None:
            data_list.append(h.val)
            h = h.next
        return(str(data_list))

class Solution:
    def _insert(self, sorted_list:ListNode, data):
        head = sorted_list
        if data.val <= head.val:
            data.next = head
            sorted_list = data
            return sorted_list
        head_next = head.next
        while head_next is not None:
            if head_next.val >= data.val:
                data.next, head.next = head_next, data
                break
            else:
                head = head_next
                head_next = head.next
        if head_next is None:
            head.next = data
            
        return sorted_list

    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        sorted_list, head = head, head.next
        sorted_list.next = None
        while head is not None:
            #print(head)
            #print(sorted_list)
            data, head = head, head.next
            data.next = None
            sorted_list = self._insert(sorted_list, data)
            del data
        return sorted_list

def main():
    s = Solution()
    input_data = [
        # ListNode.construct([4,2,1,3]),
        ListNode.construct([-1,5,3,4,0])
    ]
    for data in input_data:
        print(s.insertionSortList(data))


if __name__=="__main__":
    main()
