from .Exceptions import InValidExpression
    # created by G Daniel Vineel

class PostfixExpression(InValidExpression):
    """
    This class is responsible for converting postfix to infix 
    Here ~ can be accepted to take unary negative values

    
    """

    def __init__(self,expression):
        """params : expression <str>"""
        if(not(self.__validateExpression(expression))):
            raise InValidExpression(expression)

    def __validateExpression(self,exp):
        """
        This method validate no special symbol present including "()" except "~"and" "
        """
        specialSymbols=False
        allChars="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM+-*/~ "
        
        isStartedWithOperation=False
        isOperandStarted=False
        for x in exp:

            if(x not in allChars):
                specialSymbols=True
                break
            elif(x in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" and not(isOperandStarted)):
                isOperandStarted=True
            elif(not(isOperandStarted) and x in "-+*/"):
                isStartedWithOperation=True
                break
        self.__setExpression(exp)   
        res=not(specialSymbols)and not(isStartedWithOperation)
        return res
    
    def __setExpression(self,exp):
        """
        This method will set the expression
        params : expression <str>
        """
        self.__expression=exp

    def getExpression(self):
        """This method return the expression"""
        return self.__expression
    
    def replaceExpression(self,exp):
         """This method will replace the existing expression
            params : expression <str>
         """
         if(not(self.__validateExpression(exp))):
            raise InValidExpression(exp)

    def getInfixExpression(self):
        exp=self.getExpression()
        operands=[]
        samePlace=False #used to append the operand if it is more than one
        operationInvalid=False
        for x in exp:
            
            if(x == " "):
                samePlace=False
            elif(x in "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm~"):
                if(samePlace):
                    if(len(operands)>0):
                        operands.append(operands.pop()+x)
                else:
                    operands.append(x)
                samePlace=True
            elif(x in "+-*/"):
                if(len(operands)>=2):
                    two=operands.pop()
                    one=operands.pop()
                    operands.append(f"({one+x+two})")
                else:
                    operationInvalid=True
        return operands[0].replace("~","-")

# a=PostfixExpression(" a b c d -e  f + * * +")
# a=PostfixExpression('an a * b -')
# print(a.getExpression())
# print(a.getInfixExpression())








