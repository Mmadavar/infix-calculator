# DO NOT modify this class
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data value of the node
        self.next = None  # Points to the next node in the linked list
    
    def __str__(self):
        return "Node({})".format(self.data)  # Return string representation of the node

    __repr__ = __str__ #Uses the same string representation for the node when printing or debugging
                          




    
#=============================================== Part I ==============================================

class Stack:
    """
    >>> x = Stack()
    >>> x.isEmpty()
    True
    >>> len(x)
    0
    >>> x.peek()
    >>> x.pop()
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.isEmpty()
    False
    >>> len(x)
    1
    >>> x.peek()
    2
    >>> x.pop()
    2
    >>> x
    Top: None
    Stack: 
    >>> x.push(2)
    >>> x.push(4)
    >>> x.push(6)
    >>> x.isEmpty()
    False
    >>> len(x)
    3
    >>> x
    Top: Node(6)
    Stack: 6 <= 4 <= 2
    >>> x.peek()
    6
    >>> x.pop()
    6
    """

    # DO NOT modify this method
    # constructor method for stack class so method is called when an instance of stack class is created
    def __init__(self):
        self.top = None
    
    # DO NOT modify this method
    # string representation method for the stack class 
    #It iterates over all the elements of the stack, starting from the 'top', and returns a string representing the stack.
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.data))
            temp=temp.next
        out=' <= '.join(out)
        return ('Top: {}\nStack: {}'.format(self.top,out))

    # DO NOT modify this method
    # This is the representation method for the Stack class. It is called by built-in functions 
    # and operators that need a string representation of the object for debugging, such as the 'repr()' function.
    # Here, it is set to be the same as the string representation method '__str__'.
    __repr__=__str__


    

    def isEmpty(self):
        ## YOUR CODE STARTS HERE
        # Here I see to check if this is empty or not and return it.
        return self.top == None

    
    def __len__(self): 
        ## YOUR CODE STARTS HERE
        # Here I create a counter variable set to 0 to iterate through a while loop
        # set current to self.top
        # I run the while loop for current and then i say count += 1 to iterate through each
        # element and then I set current to current.next to represent the next element
        # all the way until there's no elements to refer to
        # then I return count.
        count = 0
        current = self.top
        while current:

            count += 1
            current = current.next
        return count


    def push(self, data):
        ## YOUR CODE STARTS HERE
        # I create a variable for self.top
        # then I set self.top to the node(data)
        # then self.top.next is not top1
        top1 = self.top

        self.top = Node(data)

        self.top.next = top1
           
     
    def pop(self):
        ## YOUR CODE STARTS HERE
        #Here I say if it's empty then return None
        # if it's not then I have a variable representing self.top
        # then I reference self.top to self.top.next and that allows me
        # to delete self.top and then I return the top.data
        if self.isEmpty():
            return None
        top = self.top
        self.top = self.top.next
        return top.data

        
    def peek(self):
        ## YOUR CODE STARTS HERE
        # Here if the stack is empty then I return none
        # if not then I create a variable peek 1 to reference self.top.data
        # and then I return peek1
        if self.isEmpty():
            return None
        peek1 = self.top.data
        return peek1
        


    

#=============================================== Part II==============================================


class Calculator:

    # DO NOT modify this member
    priority = { '+':1, '-':1, '*':2, '/':2, '^':3 } # Here I have a dictionary with operators that have priority levels
    
    # DO NOT modify this method
    # Here I create an instance of the calculator class
    # It initializes the private instance variable '__expr' to None. This variable is intended to hold an 
    # expression that the calculator will work with.
    def __init__(self):
        self.__expr = None

        
    # DO NOT modify this method
    #property decorator to create a getter method for the '__expr' variable. 
    @property
    def expr(self):
        return self.__expr


    # DO NOT modify this method
    @expr.setter
    def expr(self, new_expr):
        if isinstance(new_expr, str) and self._validate(new_expr):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

        


        
    def _isNumber(self, token):
        """
        >>> x=Calculator()
        >>> x._isNumber('5')
        True
        >>> x._isNumber('+5')
        True
        >>> x._isNumber('-5')
        True
        >>> x._isNumber('5.')
        True
        >>> x._isNumber('-5.')
        True
        >>> x._isNumber('+5.')
        True
        >>> x._isNumber('0.5')
        True
        >>> x._isNumber('-0.5')
        True
        >>> x._isNumber('.5')
        True
        >>> x._isNumber('-.5')
        True
        >>> x._isNumber(' 4.560 ')
        True
        >>> x._isNumber('4 56')
        False
        >>> x._isNumber('4.56a')
        False
        >>> x._isNumber('-4.56a')
        False
        >>> x._isNumber('4.5a6')
        False
        """
        ## YOUR CODE STARTS HERE
        # Here I use a try/except statement and for the try statement I see if the string can be converted to a float point number
        # If it does then I return true and if not I go to the except statement and return false
        try:
            if str(float(token)):
                return True
        except:
            return False

    # function to test for parentheses
    def is_well_formed(self, expr):
        stack = []
        for token in expr.split():
            if token.isdigit():
                continue
            elif token == '(':
                stack.append(token)
            elif token == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack



        
    def _validate(self, expr):
        """
        >>> x=Calculator(); x._validate('2 ^ 4')
        True
        >>> x=Calculator(); x._validate('2')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
        True
        >>> x=Calculator(); x._validate('2 * 5.34 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('2.1 * 5 + 3 ^ 2 + 1 + 4')
        True
        >>> x=Calculator(); x._validate('( 2.5 )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 ) )')
        True
        >>> x=Calculator(); x._validate ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
        True
        >>> x=Calculator(); x._validate ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
        True
        >>> x=Calculator(); x._validate ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
        True
        >>> x=Calculator(); x._validate('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
        True
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ + -2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2 * 5 + 3 ^ - 2 + 1 + 4')
        False
        >>> x = Calculator(); x._validate('2    5')
        False
        >>> x = Calculator(); x._validate('25 +')
        False
        """
        ## YOUR CODE STARTS HERE
        
        # check for unsupported operators
        expr = expr.strip()
        # check if the first or last element is an operator
        operators = "+-*/^"
        if expr.split(" ")[-1] in operators or expr.split(" ")[0] in operators:
            return False

        supported_operators = "+-*/^()"
        for char in expr.split(" "):
            if char not in supported_operators and not any(i.isdigit() for i in char):
                return False

        # check for consecutive operators
        operators = "+-*/^"
        prev = ""
        for char in expr.split(" "):
            if char in operators and prev in operators:
                return False
            prev = char

        # check if we have parentheses issues like ) 1 + 2 (
        if not self.is_well_formed(expr):
            return False


        # check for unbalanced parentheses
        if expr.count("(") != expr.count(")"):
            return False

        # check for implicit multiplication
        operators = "+-*/"
        for i in range(len(expr) - 1):
            if expr[i].isdigit() and expr[i+1] == "(":
                return False
            elif expr[i] == ")" and expr[i+1].isdigit():
                return False
            elif expr[i] == "(" and expr[i+1].isdigit() and expr[i+4] == ")" and expr[i+5] == ")":
                return False

        return True




    # self.__expr must be a valid expression
    # validity of self.__expr is checked when calling the property method @expr.setter
    # - see @expr.setter for detail
    def _getPostfix(self):
        """
        Required: _getPostfix must create and use a Stack for expression processing
        >>> x=Calculator()
        >>> x.expr = '2 ^ 4'; x._getPostfix()
        '2.0 4.0 ^'
        >>> x.expr = '2'; x._getPostfix()
        '2.0'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4.45'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
        >>> x.expr ='2 * 5.34 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '2.1 * 5 + 3 ^ 2 + 1 + 4'; x._getPostfix()
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x.expr = '( 2.5 )'; x._getPostfix()
        '2.5'
        >>> x.expr = '( ( 2 ) )'; x._getPostfix()
        '2.0'
        >>> x.expr = '2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )'; x._getPostfix()
        '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x.expr = '( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )'; x._getPostfix()
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        """

        ## YOUR CODE STARTS HERE
        token = list(self.__expr.strip().split())
        result = []
        ratorStack = Stack()  # must use ratorStack to get a postfix expression of self.__expr 
        for i in token: # run the for loop for i in each token which gives us a list for the infix expression
            if i != '(' and i != ')' and i != '^' and i != '+' and i != '-' and i != '*' and i != '/':
                result.append(str(float(i)))  # token is converted to a string which represents the floating point number and append it to the list
            elif i == '(': # Here for the elif statement if i == '(' then I push that same '(' to the stack
                ratorStack.push('(')
            elif i == ')':
                while ratorStack.peek() != '(': # Here while the top part of the stack is not equal to '('
                    result.append(ratorStack.pop()) # Then what I do is pop that from the stack and append that to the list 
                ratorStack.pop() # and then I go out of the while loop and pop it from the stack
            # Here for the elif  statement we check if the token is one of the operators 
            elif i == '*' or i == '/' or i == '+' or i == '-':
                while not ratorStack.isEmpty(): #Here while the stack is not empty 
                    if ratorStack.top.data != '(' and self.priority[ratorStack.peek()] >= self.priority[i]: # we see if the the top of the stack is not equal to '(' and the top part of the stack has a higher or equal precedence to the token
                        result.append(ratorStack.pop()) # here I pop the stack and append it to the list
                    else:
                        break
                ratorStack.push(i) # Here push the token to the stack
            # Here for the elif statement if the '^' operator is here
            elif i == '^':
                while not ratorStack.isEmpty(): # we say while the stack is not empty
                    if ratorStack.peek() != '(' and self.priority[ratorStack.peek()] > self.priority[i]:
                        result.append(ratorStack.pop()) # Here I pop the stack and append it to the list
                    else:
                        break
                ratorStack.push(i) # push the token to the stack 
            else: # or else return none
                return None
        # Here while the stack is not empty I pop the operator from the stack and append it to the list
        while not ratorStack.isEmpty():
            result.append(ratorStack.pop())
        # Then I return the string that i get and I join the list and I use the space in the string as a separator
        return ' '.join(result)


    


    # This property method must
    # 1. converts self.__expr to a postfix expression by calling self._getPostfix
    # 2. use a stack to compute the final result of the postfix expression
    @property
    def value(self):
        '''
        >>> x=Calculator()
        >>> x.expr = '4 + 3 - 2'; x.value
        5.0
        >>> x.expr = '-2 + 3.5'; x.value
        1.5
        >>> x.expr = '4 + 3.65 - 2 / 2'; x.value
        6.65
        >>> x.expr = '23 / 12 - 223 + 5.25 * 4 * 3423'; x.value
        71661.91666666667
        >>> x.expr = ' 2 - 3 * 4'; x.value
        -10.0
        >>> x.expr = '7 ^ 2 ^ 3'; x.value
        5764801.0
        >>> x.expr = ' 3 * ( ( ( 10 - 2 * 3 ) ) )'; x.value
        12.0
        >>> x.expr = '8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3'; x.value
        28.6
        >>> x.expr = '2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4'; x.value
        -2.0
        >>> x.expr = ' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2'; x.value
        1442.7777777777778
        '''

        if not isinstance(self.__expr, str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # must use calcStack to compute the expression

        ## YOUR CODE STARTS HERE
        # here I have the list of tokens from the postfix
        token = list(self._getPostfix().split())
        for i in token:
            if i != '(' and i != ')' and i != '^' and i != '+' and i != '-' and i != '*' and i != '/':# Here to see if i is a number
                calcStack.push(float(i)) #if it is then push it to the stack with a float equivalent
            else:
                op_2 = calcStack.pop() #pop the stack
                op_1 = calcStack.pop() #pop the stack
                if i == '+': # in the token if there's a + sign then add op_1 and op_2
                    calcStack.push(op_1 + op_2)
                if i == '-': # in the token if there's a - sign then subtract op_1 and op_2
                    calcStack.push(op_1 - op_2)
                if i == '*': # if there's a / sign then divide op_1 and op_2
                    calcStack.push(op_1 * op_2)
                if i == '/': # if there's a * sign then multiply op_1 and op_2
                    calcStack.push(op_1 / op_2)
                if i == '^':# then square op_1 and op_2
                    calcStack.push(op_1 ** op_2)
                
        # if the length of Calcstack is exactly one item
        # then I use a return statement and pop the stack
        if len(calcStack) == 1:
            return calcStack.pop()
        # if the length is not equal then return none
        else:
            return None





    
if __name__ == '__main__':
    import doctest
    
    ## Uncomment this line if you want to run doctest by function.
    ## Replace get_words with the name of the function you want to run
    #doctest.run_docstring_examples(Calculator._validate, globals(), verbose=True, name='hw5')

    ## Uncomment this line if you want to run the docstring
    ## in all functions
    doctest.testmod()











        



    

