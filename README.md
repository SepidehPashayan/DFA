# 🤖 DFA Simulator

> An interactive Deterministic Finite Automaton (DFA) simulator built with Python and Streamlit.  
> Enter a binary string and watch the automaton trace its path through the state diagram in real time.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔤 String input | Enter any binary string and simulate it instantly |
| ✅ Accept / Reject | Clearly shows whether the input string is accepted or rejected |
| 🗺️ Visual state diagram | Graphviz renders the full DFA graph |
| 🔴 Path highlighting | Traversed transitions are highlighted in red on the diagram |

---

## 🧠 The Automaton

The DFA is hardcoded with the following configuration:

| Property | Value |
|---|---|
| States | `A, B, C, D, E, F, G, H` |
| Alphabet | `{0, 1}` |
| Start state | `A` |
| Accepting states | `F, G` |

### Transition table

| State | `0` | `1` |
|---|---|---|
| A | H | B |
| B | H | A |
| H | C | C |
| C | E | F |
| D | E | F |
| E | F | G |
| F | F | F |
| G | G | F |

---

## 📁 Project Structure

```
dfa-simulator/
└── app.py      # DFA logic + Streamlit UI
```

---

## 🚀 Getting Started

### Install dependencies

```bash
pip install streamlit graphviz
```

> You also need the Graphviz system package:
> - **Windows**: [graphviz.org/download](https://graphviz.org/download/)
> - **macOS**: `brew install graphviz`
> - **Linux**: `sudo apt install graphviz`

### Run the app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥️ Usage

1. Type a binary string (e.g. `1100`, `011`, `101`) into the input field
2. The app shows **✅ Accepted** or **❌ Rejected**
3. The state diagram renders below — transitions taken are highlighted in **red**

---

## 👩‍💻 Author

**Sepideh Pashayan**
