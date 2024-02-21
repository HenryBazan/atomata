from graphviz import Digraph

# Create a new directed graph for the DFA
dot = Digraph(comment='DFA for Id')

# Add states
dot.node('S', 'Start')
dot.node('A', 'A-Z|a-z')
dot.node('F', 'Follow', shape='doublecircle')

# Add transitions
# Transition from Start to A-Z|a-z on alphabet letters
for letter in (chr(i) for i in range(65, 91)):  # A-Z
    dot.edge('S', 'A', label=letter)
for letter in (chr(i) for i in range(97, 123)):  # a-z
    dot.edge('S', 'A', label=letter)

# Transition from A-Z|a-z to Follow on all valid characters
all_characters = [chr(i) for i in range(48, 58)]  # 0-9
all_characters.extend([chr(i) for i in range(65, 91)])  # A-Z
all_characters.extend([chr(i) for i in range(97, 123)])  # a-z

for char in all_characters:
    dot.edge('A', 'F', label=char)
    dot.edge('F', 'F', label=char)  # Loop back to itself on all valid characters

# Render and display the graph
dot.render('/mnt/data/dfa_diagram', view=True, format='png')

'/mnt/data/dfa_diagram.png'
