import math
text_to_format = "Lorem Ipsum..."
print('{:>50}'.format(text_to_format))
print('{:_<50}'.format(text_to_format))
print('{:^50}'.format(text_to_format))
print('{:10.7}'.format(text_to_format))

num_to_format = 0xff
print('{:d}'.format(num_to_format))
print('{:f}'.format(math.pi))
print('{:+d}'.format(num_to_format))
print('{:3.2f}'.format(math.pi))
