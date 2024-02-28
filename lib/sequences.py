#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < length:
        num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(num)
        
    print(fibonacci_sequence[:length])
   
print_fibonacci(10)    
pass