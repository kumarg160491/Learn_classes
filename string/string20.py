'''
INPUT
Hi how are you
OUTPUT
Hi woh era you
'''

sample_input = 'Hi how are you'
sample_input = list(sample_input.split())
print(sample_input)
temp = [sample_input[0]]
for i in range(1, len(sample_input) - 1):
    val = sample_input[i][::-1]
    temp.append(val)
temp.append(sample_input[-1])
print(" ".join(temp))
