import streamlit as st
import graphviz

class DFA:
    def __init__(self):
        self.state = {"A", "B", "C", "D", "E", "F", "G", "H"}
        self.alphabet = {"0", "1"}
        self.start = "A"
        self.final = {"F", "G"}
        self.transition = {
            ("A", "1"): "B", ("A", "0"): "H",
            ("B", "1"): "A", ("B", "0"): "H",
            ("H", "1"): "C", ("H", "0"): "C",
            ("C", "1"): "F", ("C", "0"): "E",
            ("E", "1"): "G", ("E", "0"): "F",
            ("D", "1"): "F", ("D", "0"): "E",
            ("F", "1"): "F", ("F", "0"): "F",
            ("G", "1"): "F", ("G", "0"): "G",
        }

    def process(self, input_s):
        path = []
        s = self.start
        for x in input_s:
            path.append((s, x))
            if (s, x) in self.transition:
                s = self.transition[(s, x)]
            else:
                path.append(("Invalid", x))
                break
        path.append((s, ""))
        return path, s in self.final

dfa = DFA()

st.title("DFA Simulator")

input_str = st.text_input("Enter your string:", "")

if input_str:
    path, accepted = dfa.process(input_str)
    st.write("✅ Accepted!" if accepted else "❌ Rejected!")

    dot = graphviz.Digraph()

    for state in dfa.state:
        shape = "doublecircle" if state in dfa.final else "circle"
        dot.node(state, shape=shape)

    dot.node("", shape="none")
    dot.edge("", dfa.start)

    for (src, symbol), dst in dfa.transition.items():
        color = "red" if (src, symbol) in path else "black"
        dot.edge(src, dst, label=symbol, color=color)

    st.graphviz_chart(dot)