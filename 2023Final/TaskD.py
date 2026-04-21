
def sequence(n):
    
    def _seq(n, memo):
        if n in memo:
            return memo[n]
        
        if n == 1:
            return 0
        if n == 2:
            return 1

        
        memo[n] = _seq(n - 1, memo) - (n + 1) * _seq(n - 2, memo)
        
        return memo[n]
    
    return _seq(n, {})

for n in range(1, 21):
    print(sequence(n))

