import sys

# if we pass in arg , we print it or else print please pass an argument

if len(sys.argv) > 1:
    print('This is the argument u passed {}'.format(sys.argv[1]))
else:
    print('please pass an argument')
