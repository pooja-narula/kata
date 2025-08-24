import re
def extract_num(s):
    r=re.findall('[\\d]+(?:[,]\\d+)?(?:[.]\\d+)?',s)
    num="".join(r).split(",")
    return "".join(num) if len(r) else 0
def add_num(inp) :
    delimProvided=re.findall('//(?:[^\\n]*)\n',inp)
    # step 4, making delim optional, thereby satisfying all previous steps
    delim=delimProvided[0][2:-1] if len(delimProvided) and len(delimProvided[0])>3 else ","
    start=len(delimProvided[0]) if len(delimProvided) else 0
    inp=inp[start:]
    #step 3, treating \n as delim 
    inp=inp.replace('\n',delim)
    #step 5, throw an exception “negatives not allowed”
    if delim!='-' and len(inp.split("-"))>1:
        r=list(map(lambda v:v.split(delim)[0],inp.split("-")[1:]))
        raise Exception('negatives not allowed: -'+ ",-".join(r))
    numList=inp.split(delim)
    result = list(map(lambda s: float(extract_num(s.strip())), numList))
    s=sum(result)
    return int(s) if int(s)==s else s

if __name__=="__main__":
    inp=input()
    print(add_num(inp))
