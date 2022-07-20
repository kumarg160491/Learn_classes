'''
INPUT
guvi geeks
OUTPUT
GuviGeeks
'''

sample_input = 'guvi geeks'
sample_input = (sample_input.split(" "))
print(sample_input)

for i in sample_input:
    print("".join(i.capitalize()), end="")
