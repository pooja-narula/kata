import re
def extract_num(s):
    r=re.findall('[\\d]+(?:[,]\\d+)?(?:[.]\\d+)?',s)
    num="".join(r).split(",")
    return "".join(num) if len(r) else 0
def add_num(inp, delim) :
    numList=inp.split(delim)
    result = list(map(lambda s: float(extract_num(s.strip())), numList))
    s=sum(result)
    return int(s) if int(s)==s else s

if __name__=="__main__":
    inp=input()
    add_num(inp,"+")
