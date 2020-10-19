# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.


a, b, = 5, 6

print(f'{a} = {bin(a)}')
print(f'{b} = {bin(b)}')
print('Binary AND is: ', a & b, '=', bin(a & b))
print('Binary OR is: ', a | b, '=',  bin(a | b))
print('Binary XOR is: ', a ^ b, '=',  bin(a ^ b))
print('Binary NOT is: ', ~a, '=',  bin(~a))

print('Move to the right for 2 symbols is: ', a >> 2)
print('Move to the left for 2 symbols is: ', a << 2)
