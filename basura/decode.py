class BinaryCode:
    def decode(self, message):
        tp = []
        tp.append(self.case0(message))
        tp.append(self.case1(message))
    def case0(self,message):
        p = []
        p.count = len(message)
        init = 0
        p[0] = init 
        p[1] = int(message[0] - p[0])
        for i in range(1,len(message)-1):
            r = int(message[i]-(p[i-1]+p[i]))
            if r == 0 or r == 1:
                p[i+1] = r
            else:
                return tuple("NONE")
        fin = int(message[-1]) -( p[-1] +p[-2])
        if fin == 0 or fin == 1:
            return tuple(str(p))
        else:
            return tuple("NONE")
    def case1(self,message):
        p = []
        init = 1
        p[0] = init 
        p[1] = int(message[0] - p[0])
        for i in range(1,len(message)-1):
            r = int(message[i]-(p[i-1]+p[i]))
            if r == 0 or r == 1:
                p[i+1] = r
            else:
                return tuple("NONE")
        fin = int(message[-1]) -( p[-1] +p[-2])
        if fin == 0 or fin == 1:
            return tuple(str(p))
        else:
            return tuple("NONE")   

bin = BinaryCode()
print(bin.decode("11"))    