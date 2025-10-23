from .Exceptions import InValidExpression
    # created by G Daniel Vineel

class InfixExpression(InValidExpression):

    def __init__(self,expression):
        """Params : <str> type (Expression)"""
        if (not(self.__validateExpression(expression))):
            raise InValidExpression(f"{expression} is not valid ")
        
    def replaceExpression(self,expression):
        """It will replace the existing expression"""
        if (not(self.__validateExpression(expression))):
            raise InValidExpression(f"{expression} is not valid ")
        

    def __setExpression(self,expression):
        """set the expression and validate the expression"""
        self.__expression=expression
    
    
    def getExpression(self):
        """returns the expression"""
        return self.__expression

    def __validateExpression(self,exp):

        """
        This method validates the following :
            - Braced Properly 
            - Empty Braces like ()
            - Any special symbols 
            - Double Operators
            - Operand present or not
            - Started with Operator
            - Ending with Operator
            - consider -a as unary values
        returns True if it is satisfy all conditions ,
        returns False if any of the condition not satisfied
        """
        # print(exp)
        isListItemsPresent=False
        list1=["(-(","(+(","(*(","(/("]
        for x in list1:
            if(exp.find(x) > 0):
                isListItemsPresent=True
                return not(isListItemsPresent)
                
     
        lb=rb=0
        bracedProperly=True
        specialCharacter=False
        doubleOperator=False
        isOperandStarted=False
        starting_with_operator=False
        operator=False
        emptyBraces=False
        braceOpened=False
        prev_operator=""
        prev_chr=""
        braceOpenedAdj=False
        newExp=""
        words="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        operators="+-*/()"
        symbol_change=0
        inside_braces=0
        isOperandPresentBefore=False
        for x in exp:
            chr=x
            if(x not in "1234567890-+/*qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM()"):
                specialCharacter=True
                break
            elif(x=="("):
                lb+=1
                operator=False
                braceOpened=True
                braceOpenedAdj=True
                inside_braces+=1
                # if brace opened directly convert it to *
                if(prev_chr in words and len(newExp)>0):
                    chr="*("
                    prev_chr="("
                else:
                    chr="("


            elif(x==")"):
                # print(symbol_change,inside_braces,end=" ")
                
                if(inside_braces>0):
                    inside_braces-=1
                if(inside_braces==0 and symbol_change>0):
                    symbol_change-=1
                
                # print(symbol_change,inside_braces)


                if(braceOpened):
                    emptyBraces=True
                    break
                rb+=1
                braceOpened=False
                braceOpenedAdj=False
           
            else: # ALL Words and Operators excluding ()
                
                braceOpened=False # checking for consequtive closing

                if(not(isOperandStarted) and x in "-"): #only works before any word shows

                        chr="~"
                elif(not(isOperandStarted) and x in "+*/"): #only works before any word shows

                    starting_with_operator=True
                    break


                elif(not(isOperandStarted)):#only works on first word

                    isOperandStarted=True #operand started


                # print(x,braceOpenedAdj,"hello")


                elif(x in "+/*-" and not(operator)):
                    # print(symbol_change,x)
                    operator=True
                    

                    if(symbol_change>0):
                        if(symbol_change%2==0):
                            chr=x
                        else:
                            if(x=='-'):
                                chr="+"
                            elif(x=="+"):
                                chr="-"


                elif(x in "+/*-" and operator):

                
                    if((prev_operator in "-+" and x in "-+/*") or (prev_operator in "/+*" and x in "/*+") ):
                        doubleOperator=True
                        break
                   
                    else:
                        prev_operator=x
                
                else:
                    operator=False


                if(x=="-" and braceOpenedAdj):
                    chr="~"
                    braceOpenedAdj=False
                else:
                    braceOpenedAdj=False


            if(rb>lb):
                bracedProperly=False
                break
            prev_chr=x
            newExp+=chr
        self.__setExpression(newExp)
        
        if(not(bracedProperly) or emptyBraces or specialCharacter or doubleOperator or not(isOperandStarted) or starting_with_operator or operator):
            return False
        return True

        # print(f"\n{x}\nlb\t{lb}\nrb\t{rb}\nbracedProperly\t{bracedProperly}\nemptyBraced\t{emptyBraces}\nspecialCharacters\t{specialCharacter}\ndoubleOperator\t{doubleOperator}\nisOperandStarted\t{isOperandStarted}\nstarted+with_operator\t{starting_with_operator}\noperator-last\t{operator}")



    def getPostfixExpression(self):
        """returns postfix expression"""
       
        exp=(self.getExpression())
  
        exp="("+exp+")"
        # print(exp)
        res=""
        stack1=[]
        for x in exp:

            if (x not in "+-*/()"):
                if(x=="~"):
                    res+="-"
                else:
                    res+=x
            else:
                res+=" "
                if(x=="("):
                    stack1.append(x)
                if(x==")"):
                    for i in range(len(stack1)-1,-1,-1):
                        
                        if(stack1[i]=="("):
                            stack1.pop()
                            break
                        else:
                            res+=stack1.pop()+" "

                elif((x in "/*" and stack1[-1] in "/*")  or (x in "+-" and stack1[-1] in "+-/*") ):
                    res+=stack1.pop()+" "
                    stack1.append(x)
                elif((x in "/*" and stack1[-1] not in "/*")or(x in "+-" and stack1[-1] =="(")):
                    stack1.append(x)
        
        res=res.replace("  "," ")
        
        # print(res)
        return res


# print(InfixExpression("(a*(a))").infixToPostfix())


# work on brace should open before operator like +(),-(),*(),/()
#  *- /-  change the symbols inside braces 