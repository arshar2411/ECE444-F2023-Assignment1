class utils():
    def reversed(n: int):
        if type(n) != int:
            raise TypeError("integer inputs only!")
        out = []
        while n:
            out.append(str(n%10))
            n //=10
        return int("".join(out))
    
    def formatter(n: int):
        if type(n) != int:
            raise TypeError("integer inputs only!")
        base_8 = []
        base_2 = []
        x = y = n
        while x:
            base_8.append(str(x%8))
            x //=8
        while y:
            base_2.append(str(y%2))
            y//=2
        return "0o"+"".join(base_2)[::-1], "0b"+"".join(base_8)[::-1]
        
