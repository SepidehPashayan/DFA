import os
from shutil import which
from graphviz import Digraph

os.environ["PATH"] +=os.pathsep + r"C:\Program Files\Graphviz\bin"

if which("dot") is None:
    raise RuntimeError()

dot=Digraph()

dot.node("A",shape="circle")
dot.node("B",shape="circle")
dot.node("C",shape="circle")
dot.node("D",shape="circle")
dot.node("E",shape="circle")
dot.node("H",shape="circle")
dot.node("F",shape="doublecircle")
dot.node("G",shape="doublecircle")

dot.edge("A","B",label="1")
dot.edge("A","H",label="0")
dot.edge("B","A",label="1")
dot.edge("B","H",label="0")
dot.edge("H","C",label="1")
dot.edge("H","C",label="0")
dot.edge("C","F",label="1")
dot.edge("C","E",label="0")
dot.edge("E","G",label="1")
dot.edge("E","F",label="0")
dot.edge("D","F",label="1")
dot.edge("D","E",label="0")
dot.edge("F","F",label="1")
dot.edge("F","F",label="0")
dot.edge("G","F",label="1")
dot.edge("G","G",label="0")

file_path = dot.render("dfa_test",format="png",cleanup=False)

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