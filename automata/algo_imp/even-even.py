value = input("enter the string : ")
state = '0'
fstate = '0'
for n in value:
    # on state 0 if read a or read b 
    if state=='0' and n == 'a':
        state = '1'
        fstate = fstate + state
    elif state == '0' and n == 'b':
        state = '2'
        fstate = fstate + state 

    # on state 1 if read a or read b 
    elif state == '1' and n == 'a':
        state = '0'
        fstate = fstate + state 
    elif state == '1' and n == 'b':
        state = '3'
        fstate = fstate + state 

    # on state 2 if read a or read b 
    elif state == '2' and n == 'a':
        state = '3'
        fstate = fstate + state 
    elif state == '2' and n == 'b':
        state = '0'
        fstate = fstate + state 

    # on state 3 if read a or read b 
    elif state == '3' and n == 'a':
        state = '2'
        fstate = fstate + state 
    elif state == '3' and n == 'b':
        state = '1'
        fstate = fstate + state 
    else:
        fstate = 'states are invalid'


print(fstate)