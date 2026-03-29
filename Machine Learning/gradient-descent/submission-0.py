class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        #x = x - lr * dx
        x = init
        while iterations:
            dx =  2*x
            x = x - learning_rate*dx
            iterations-=1

        return round(x,5)    


