'''
INPUT
jack and jill went up and down to get water
OUTPUT
jill and jack went down and up to get water
'''

sample_input = 'jack and jill went up and down to get water'
sample_input = list(sample_input.split())
temp = sample_input[0]
sample_input[0] = sample_input[2]
sample_input[2] = temp
temp = sample_input[4]
sample_input[4] = sample_input[6]
sample_input[6] = temp
print(sample_input)
