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
        for x in input_s:
            if(s,x) in self.transition:
                s = self.transition[(s,x)]
        return s in self.final
    
dfa = DFA()
input_string = input("please enter the string:").strip()
print(dfa.accept(input_string))