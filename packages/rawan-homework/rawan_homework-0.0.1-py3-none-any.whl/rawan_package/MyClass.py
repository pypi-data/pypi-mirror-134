import numpy as np
class MyClass:
    def __init__(self, lst=[]):
        if type(lst)
        self.lst = lst.copy()
    
    def return_max(self):
        return max(self.lst)
    
    def return_min(self):
        return min(self.lst)
    
    def return_max_squared(self):
        return max(self.lst)**2
    
    def return_length(self):
        return len(self.lst)
    
    def return_positive_sum(self):
        pos_sum=0
        for e in self.lst:
            if e>0:
                pos_sum+=e
        return pos_sum
    
    def return_negative_count(self):
        neg_cnt=0
        for e in self.lst:
            if e<0:
                neg_cnt+=1
        return neg_cnt
    
    def add_element(self, e):
        self.lst.append(e)
    
    def remove_last_element(self):
        x = self.lst.pop()
        return x
    