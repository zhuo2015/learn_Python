#Temperature Convert Between Centigrade and Fahrenheit
var = input('Please enter the value want to convert (eg. 32C or 89F):')

if var[-1] in ['c','C']:
    value = 1.8 * float(var[:-1]) + 32
    print('%sC is %.2fF' % (var[:-1],value))
elif var[-1] in ['F', 'f']:
    value = float(var[:-1])/1.8 - 32
    print('%sF is %.2fC' % (var[:-1],value))
else:
    print('Wrong Format! ')

