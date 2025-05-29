class DFA:
    def __init__(self):
        self.state = {"A","B","C","D","E","F","G","H"}
        self.alphabet = {"0","1"}
        self.start = "A"
        self.final = {"F","G"}
        self.transition ={
            ("A","1"): "B",
            ("A","0"): "H",
            ("B","1"): "A",
            ("B","0"): "H",
            ("H","1"): "C",
            ("H","0"): "C",
            ("C","1"): "F",
            ("C","0"): "E",
            ("E","1"): "G",
            ("E","0"): "F",
            ("D","1"): "F",
            ("D","0"): "E",
            ("F","1"): "F",
            ("F","0"): "F",
            ("G","1"): "F",
            ("G","0"): "G",
        }
    def accept(self,input_s):
        s = self.start
        path = [s]
        transition = []
        for x in input_s:
            if x not in self.alphabet:
                print("string is not correct!")
                return path,transition
            if(s,x) in self.transition:
                next_s = self.transition[(s,x)]
                transition.append((s,x,next_s))
                s = next_s
                path.append(s)
        return s in self.final
    
dfa = DFA()
input_string = input("please enter the string:").strip()
answer=str(dfa.accept(input_string))
if answer=="True":
    print("Accept")
else :
    print("Reject")