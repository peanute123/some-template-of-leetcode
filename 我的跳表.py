import random
class ListNode:
    def __init__(self,v):
        self.val = v
        self.prev = None
        self.next = None
        self.up = None
        self.down = None
class Skiplist: 
    def __init__(self): 
        node4 = ListNode(-1)
        node3 = ListNode(-1);node4.down =node3;node3.up =node4
        node2 = ListNode(-1);node3.down =node2;node2.up =node3
        node1 = ListNode(-1);node2.down =node1;node1.up =node2
        self.level4 = node4
        self.level3 = node3
        self.level2 = node2
        self.level1 = node1
    def search(self, target: int) -> bool:
        return self._search_node(target).val == target 
    def _search_node(self, target: int) :
        head4 = self.level4 
        while head4.next is not None and head4.next.val<= target:
            head4 = head4.next
        if head4.val == target: return head4.down.down.down
        head3 = head4.down
        while head3.next is not None and head3.next.val<= target:
            head3 = head3.next
        if head3.val == target: return head3.down.down
        head2 = head3.down    
        while head2.next is not None and head2.next.val<= target:
            head2 = head2.next
        if head2.val == target: return head2.down
        head1 = head2.down  
        while head1.next is not None and head1.next.val<= target:
            head1 = head1.next 
        return head1

    # def _first_node(self, num: int) -> None:
    #     node4 = ListNode(num)
    #     node3 = ListNode(num);node4.down =node3;node3.up =node4
    #     node2 = ListNode(num);node3.down =node2;node2.up =node3
    #     node1 = ListNode(num);node2.down =node1;node1.up =node2
    #     self.level4.next = node4;node4.prev=self.level4
    #     self.level3.next = node3;node3.prev=self.level3
    #     self.level2.next = node2;node2.prev=self.level2
    #     self.level1.next = node1;node1.prev=self.level1
    def add(self, num: int) -> None:
        # if self.level1.next is None:
        #     self._first_node( num);return

        head4 = self.level4 
        while head4.next is not None and head4.next.val<= num:
            head4 = head4.next
        head3 = head4.down
        while head3.next is not None and head3.next.val<= num:
            head3 = head3.next
        head2 = head3.down    
        while head2.next is not None and head2.next.val<= num:
            head2 = head2.next
        head1 = head2.down  
        while head1.next is not None and head1.next.val<= num:
            head1 = head1.next
        node1 = ListNode(num)
        node1.next = head1.next
        if head1.next is not None:
             head1.next.prev = node1
        head1.next = node1 ; node1.prev = head1
        if random.random()<0.5:  
            node2  = ListNode(num)
            node1.up = node2;node2.down = node1
            node2.next = head2.next 
            if head2.next is not None:
                head2.next.prev = node2
            head2.next = node2 ; node2.prev = head2
            if random.random()<0.5: 
              node3  = ListNode(num)
              node2.up = node3;node3.down = node2
              node3.next = head3.next 
              if head3.next is not None:
                  head3.next.prev = node3
              head3.next = node3 ; node3.prev = head3
              if random.random()<0.5: 
                node4  = ListNode(num)
                node3.up = node4;node4.down = node3
                node4.next = head4.next 
                if head4.next is not None:
                    head4.next.prev = node4
                head4.next = node4 ; node4.prev = head4

    def erase(self, num: int) -> bool:
        node = self._search_node(num)
        if node is None:return False
        if node.val != num: return False
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        while node.up is not None:
            node = node.up 
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
        return True

 