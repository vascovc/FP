# Exercise 5 on "How to think...", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open("mystery.txt", "r") as ficheiro:
    for a in ficheiro:
        item = a.split()
        if item[0] == "UP":
            t.up()
        elif item[0] == "DOWN":
            t.down()
        else:
            t.goto(int(item[0]),int(item[1]))
turtle.Screen().exitonclick()

"""o programa abre o ficheiro e vai ler cada linha, a.split converte para uma lista
e depois ve se aquele elemente o primeiro se é uma daquelas strings e se for faz
o correspondente. O else faz a conversão para o valor"""
