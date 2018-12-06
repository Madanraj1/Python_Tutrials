class Parent:
    parAtt = 100
    
    def __init__(self):
        print("calling parent constructor")
        
    def parentmethod(self):
        print("calling parent method")
        
    def setAttr(self,attr):
        Parent.parAtt = attr
    
    def getAttr(self):
        print("parent Attribute :",Parent.parAtt)
        
class Child(Parent):
    def __init__(self):
        print("calling child constructor")
        
    def childmethod(self):
        print("Calling child method")
        


c = Child()
c.childmethod()
c.parentmethod()
c.setAttr(200)
c.getAttr()