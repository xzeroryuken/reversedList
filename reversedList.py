    def reverseList(self, head):
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def reversedList(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        new_head = ListNode(None)
        curr = new_head
        while stack:
            node = stack.pop()
            curr.next = node
            curr = curr.next
        curr.next = None
        return new_head.next
