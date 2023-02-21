#superclas

class A:
    #public data member
    var1 = none

    #protected data member
    _var2 = None

    #private data member
    __var3 = None

    #costructor
    def __int__(self,var1,var2,var3):
        self.var1 = var1
        self.var2 = var2
        self.__var3 = var3

    #public member functio
    def displayPublicMembers(self):
        #accessing public data members
        print("Public Data Member: ",self.var1)

    #protected member functio
    def _displayProtectedMembers(self):
        #accessing protected data members
        print("Protected Data Member: ",self._var2)

    #private member functio
    def __displayPrivateMembers(self):
        #accessing private data members
        print("Private Data Member: ",self.__var3)

    #public member function

    def accessPrivateMembers(self):
        #accessing private meember function
        self.__displayPrivateMember()


#derived class
class B(A):

    #constructor
def __init__(self,var1,var2,var3):
    A.__init__(self,var1,var2,var3)

    #public member function
    def accessProtectedMembers(self):
        #accessing protected member functions of super clas
        self._displayProtectedMembers()

#creating objects of the drived class
obj = B("Pub_Red","Pro_White","Private_Green")

#calling public member function of the derived class