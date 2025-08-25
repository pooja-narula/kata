import re

class Kata:
    def extract_num(self, s):
        r=re.findall('[\\d]+(?:[,]\\d+)?(?:[.]\\d+)?',s)
        num="".join(r).split(",")
        return "".join(num) if len(r) else 0
    
    def extract_delim(self, s):
        delims=[]
        delimProvided=re.findall('//(?:[^\\n]*)\n',s)
        # step 4, making delim optional, thereby satisfying all previous steps
        delim=delimProvided[0][2:-1] if len(delimProvided) and len(delimProvided[0])>3 else ","
        # step 8, multiple delimiters [*][+]
        delims=re.findall(r'\[(?:[^\]]*)\]',delim)
        delims=list(map(lambda v: v[1:-1], delims))
        self.delimInpLength = len(delimProvided[0]) if len(delimProvided) else 0
        return delims if len(delims) else [delim] 
    
    def add_num(self, inp) :
        self.inp=inp
        delims = self.extract_delim(inp)
        start = self.delimInpLength
        inp=inp[start:]
        #step 3, treating \n as delim 
        inp=inp.replace('\n',delims[0])
        numList=re.split("["+"".join(delims)+"]",inp)
        #step 5, throw an exception “negatives not allowed”
        if '-' not in delims and len(inp.split("-"))>1:
            negNums=[]
            for numString in numList:
                if '-' in numString:
                    negNums.append(numString.strip().split('-')[1])
            raise Exception('negatives not allowed: -'+ ",-".join(negNums))
        result = list(map(lambda s: float(self.extract_num(s.strip())), numList))
        s=sum(result)
        return int(s) if int(s)==s else s

if __name__=="__main__":
    inp=input()
    print(add_num(inp))
