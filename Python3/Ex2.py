def write_array(array, flnm):
    if len(array) != 0:
        flnm.write(str(array[0]+'\n'))
        array.pop(0)
        write_array(array, flnm)
    else:
        return(flnm)

s = str(input())
a = s.split(';')

with open("array.txt", 'w') as text:
    write_array(a, text)