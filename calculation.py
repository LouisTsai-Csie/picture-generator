class helper:
    def __init__(self, expression):
        self.expression = expression
        self.num = []
        self.op  = []
    
    def cal(self, op):
        if len(self.num)<2: raise ValueError('Operand number less than two')

        back  = self.num.pop()
        front = self.num.pop()

        if op=='+':
            if len(self.op) and self.op[-1]=='-': self.num.append(front-back)
            else: self.num.append(front+back) 
        elif op=='-':
            if len(self.op) and self.op[-1]=='-': self.num.append(front+back)
            else: self.num.append(front-back)
        elif op=='*':
            if len(self.op) and self.op[-1]=='/': self.num.append(front/back)
            else: self.num.append(front*back)
        elif op=='/':
            if len(self.op) and self.op[-1]=='/': self.num.append(front*back)
            else: self.num.append(front/back)
        else: raise ValueError('Invalid operator')
        return

    def getDigit(self, s):
        result = ''
        for i in range(len(s)):
            if s[i].isdigit(): result += s[i]
            else:
                self.num.append(int(result))
                return i        
        self.num.append(int(result))
        return len(s)
    
    def flash(self):
        while len(self.op):
            op = self.op.pop()
            if op=='(': break
            self.cal(op)
        if len(self.op) and (self.op[-1]=='*' or self.op[-1]=='/'):
            op = self.op.pop()
            self.cal(op) 
        return

    def flatten(self):
        index = 0
        while index<len(self.expression):
            s = self.expression[index]
            if s.isdigit():
                index += self.getDigit(self.expression[index:])
                if len(self.op) and (self.op[-1]=='*' or self.op[-1]=='/'):
                    op = self.op.pop()
                    self.cal(op)
            elif s=='(':
                self.op.append(s)
                index+=1
            elif s==')': 
                self.flash()
                index+=1
            elif s=='+' or s=='-' or s=='*' or s=='/':
                self.op.append(s)
                index+=1
            else: raise ValueError('Invalid string')

    def calculate(self):
        self.flatten()
        self.flash()
        return self.num[-1]


if __name__=='__main__':
    expression = input()
    calculator = helper(expression)
    print(calculator.calculate())

















