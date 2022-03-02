"""
https://rosalind.info/problems/fib/
"""
from src.utils import io

def general_fibonacci(input_string):
    n, k = map(lambda x: int(x), input_string.split(" "))
    generations = [1,1]
    if n > 2:
        for _ in range(3, n+1):
            generations.append(generations[-1]+ k * generations[-2])
    return [str(generations[n-1])] 
    

if __name__ == "__main__":

    data, filename =  io.read_data("fibd")
    #data = ["5 3"]
    solution = general_fibonacci(data[0])
    io.write_data(solution=solution, filename=filename)