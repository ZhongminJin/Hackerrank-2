def FindMergeNode(headA, headB):
    currentA=headA
    currentB=headB
    while(currentA!=currentB):
        if(currentA.next is None):
            currentA=headB
        else:
            currentA=currentA.next
        
        if(currentB.next is None):
            currentB=headA
        else:
            currentB=currentB.next
    return currentB.data
  
  
  
  
