from calc.util import *

def run():
    while (True) :
        print(' 종료 하려면 0 입력')
        number1 = int(input(' 첫번째 수 : '))
        if ( number1 == 0 ):
            print(' 계산기 종료! ')
            break
        oper = str(input('연산자를 입력하세요! ( +, -, *, / ) : '))
        number2 = int(input(' 두번째 수 : '))

        if ( oper == '+' ):
            res = add( number1, number2 )
        
        elif ( oper == '-' ):
            res = sub( number1, number2 )
        
        elif ( oper == '*' ):
            res = mul( number1, number2 )
        
        elif ( oper == '/' ):
            res = div( number1, number2 )
        else:
            print('{} 연산자 없음'.format(oper))

        print('\n 결과 : {} {} {} = {}'.format(number1, oper, number2, res),'\n--------------------\n')
        
if __name__=="__main__": run()
