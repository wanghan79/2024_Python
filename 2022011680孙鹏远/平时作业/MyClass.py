class MyClass(object):
    classVar=456

    def __init__(self,index):
        self.memVar=index
        self.memlist=list()
    
    def memberFunc(self): #固定，可变，默认，关键字
        print("a member Func")
    def __privateFunction(self):
        print("a 'private' Func")
    
    def __copy__(self):
        print("a inherate function")
        # super(Myclass,self).__copy__()
    def __str__(self):
        # super().__str__()
        return "MyClass"
    def __del__(self):
        pass
    def __eq__(self,other):
        pass
    def __hash__(self):
        return self.memVar
    
    @staticmethod
    def staticFunc():
        print("a static function")

    @classmethod
    def classFunc(cls):
        print("a class function")


if __name__ == "__main__":
    mc1 =MyClass(1)
    mc2 =MyClass(2)
    # print(MyClass.classVar)
    # print(mc1.memVar)
    # print(mc2.memVar)
    # MyClass.classVar=567
    # print(mc1.classVar)
    # print(mc2.classVar)

    # mc1.memberFunc()
    # mc1.staticFunc()
    # mc1.classFunc()

    # MyClass.memberFunc(mc1) # == mc1.memberFunction()
    # MyClass.staticFunc()

    # mc1 = TestClass{}
    # mc2 = TestClass{}
    aset={mc1,mc2}
    print(mc1.__hash__())
    print(id(mc1))
    print(mc2.__hash__())
    # mc3=mc1
    # print(mc2.__hash__())
    # print(aset)
