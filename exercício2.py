print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
def fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if fibonacci(num):
    print(num, " pertence.")
else:
    print(num, " não pertence.")
