class Solution:
    def encode(self, strs: List[str]) -> str:
        op = ""
        for s in strs:
            op += str(len(s))+"#"+s
        return op

    def decode(self, s: str) -> List[str]:
        op=[]
        while s:
            key = s.find("#")
            index = int(s[:key])
            op_string = s[key+1:key+index+1]
            op.append(op_string)
            s = s[key+index+1:]
        return op


        