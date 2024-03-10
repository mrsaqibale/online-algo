def check_value(value):
    state = '0'
    regular_exp = "aa*b*"
    if value[0] == 'a':
        state1 =  '1'
        state1 = state1*(len(value) - 1)
        state = state + state1 
        return state, regular_exp
    else:
        return "false", regular_exp
