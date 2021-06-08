# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        out = l1
        out_root = out
        flag = 0
        while l1 is not None or l2 is not None or flag:
            v = flag
            if l1 is not None:
                v += l1.val
                l1 = l1.next
            if l2 is not None:
                v += l2.val
                l2 = l2.next

            flag, v = v//10, v%10

            if out is None:
                out_para.next = ListNode(v)
                out_para = out_para.next
                out = out_para.next
            else:

                out.val = v 
                out_para = out
                out = out.next
            
        return out_root 

def construct_link(val_list):
    root = None
    cur_p = root
    for v in val_list:
        node = ListNode(v)
        if root is None:
            root = node
            cur_p = node
        else:
            cur_p.next = node
            cur_p = node
    return root

def decode_link(root):
    val = []
    while root is not None:
        val.append(root.val)
        root = root.next
    return val

if __name__=="__main__":
    val1 = [9,9,9,9,9,9,9]
    val2 = [9,9,9,9]
    l1, l2 = construct_link(val1), construct_link(val2)
    s = Solution()
    rtn = s.addTwoNumbers(l1, l2)
    print(decode_link(rtn))
    
