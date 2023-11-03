
def solution(n):
    pattern = ''
    for i in range(n * 2):
        row = i
        if i < n:
            pass
        else:
            row = n *2 - i - 1 #Devolverlo
        u = ""
        for j in range(n):
            letter_index = max(0, row-j) #Determina despues si al valor ascii se le agrega o no, ya que puede ser 0
            ascii_value = 65+n-row-1+letter_index #Genera el valor del char que se agregara
            u += chr(ascii_value)
        if i == n*2-1:
            pattern += u+''.join(reversed(u))
        else:
            pattern += u+''.join(reversed(u)) + '\n'
    print(pattern)

solution(3)