class Matrix:
    def __init__(self, input) -> None:
        if type(input) is list and all((lambda x: x is list, iter(input))):
            self.data = input
            self.shape = (len(self.data), len(self.data[0]))
        elif type(input) is tuple:
            self.shape = input
            self.data = [[0 for _ in range(input[1])] for _ in range(input[0])]
        else:
            raise ValueError("Matrix accept list of list or tuple")

    def T(self):
        self.data = [
            [self.data[i][j] for i in range(self.shape[0])]
            for j in range(self.shape[1])
        ]
        return self

    def __str__(self):
        return f"Matrix({self.data})"
        
    
if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    print(m1.T())    
