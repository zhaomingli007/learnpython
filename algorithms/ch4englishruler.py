
def draw_lines(length, tick_label=''):
    line = '-'*length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_inteval(length):
    if(length == 0):
        return;
    draw_inteval(length-1)
    draw_lines(length)
    draw_inteval(length-1)

def draw_ruler(length, num_inches):
    draw_lines(length, '0')
    for j in range(1,num_inches+1):
        draw_inteval(length-1)
        draw_lines(length, str(j))


draw_ruler(4,3)
