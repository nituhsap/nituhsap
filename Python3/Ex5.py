print("Введите ряд целых чисел, разделенных запятой")
ls = str(input())
a = ls.split(",")

def sumdeviser(ar):
    x = 0
    try:
        if len(a)>1:
            for i in range(len(a)-1):
                x += int(a[i])//int(a[i+1])
                print(x)
        else:
            print("Над единственным числом невозможно провести операцию")
    except ArithmeticError:
        print("Среди чисел есть 0 или нецелочисленное значение, дальнейшее деление невозможно")
    else:
        print("Все отлично.")
    finally:
        print("Возможно, среди чисел были недопустимые,однако вот полученный результат:")
        print(x)

sumdeviser(a)