def f(x,indent=0):
    print_with_indent(indent, 'f(x = {})'.format(x))
    indent += 1
    if x > 0:
        try:
            print_with_indent(indent,'try')
            return f(x-1,indent+1)
        except ZeroDivisionError:
            print_with_indent(indent,'except')
        finally:
            print_with_indent(indent,'finally')
    else:
        print_with_indent(indent,'1 / ' + str(x))
        return 1 / x

def print_with_indent(indent,s):
    print('|  ' * indent  + s)

try:
    f(3)
except ZeroDivisionError:
    print('outer try')
