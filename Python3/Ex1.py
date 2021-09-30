with open("boke.txt", "w") as out:
    for i in range(10):
        out.write("Ценная информация о Водниках\n")
    out.write("Ну и вот это еще.")

with open("boke.txt", "r") as file:
    for line in file:
        print(line,end='')
