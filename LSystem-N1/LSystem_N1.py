

import turtle
from Gramatica import Gramatica
import canvasvg





def main():
    rule_num = 1
    f = open("LSystemsCode.txt", "r", encoding='utf-8')
    lines = f.readlines()
    gramatica = Gramatica(lines) 

    for regra in gramatica.regra:
        key, value = regra.split("->")
        SYSTEM_RULES[key.strip()] = value.strip()
        rule_num += 1

    axioma = gramatica.axioma
    iterations = gramatica.passos

    model = div(axioma, iterations)

    segment_length = 5  
    alpha_zero = 90
    angulo = gramatica.angulo

    r_turtle = set_turtle(alpha_zero)
    turtle_screen = turtle.Screen()
    turtle_screen.screensize(1500, 1500)
    desenho_1(r_turtle, model[-1], segment_length, angulo,gramatica.alfabeto )
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall("LSystem.svg",ts,None,10,None)

    turtle_screen.exitonclick()


if __name__ == "__main__":
    main()

SYSTEM_RULES = {} 


def divisao(axioma, passos):
    div = [axioma]  
    for _ in range(int(passos)):
        next_seq = div[-1]
        prox_axioma = [regra(char) for char in next_seq]
        div.append(''.join(prox_axioma))
    return div


def regra(sequence):
    if sequencia in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequencia


def desenho_1(turtle, SYSTEM_RULES, seg_length, angulo,alfabeto):
    stack = []
    for command in SYSTEM_RULES:
        turtle.pd()
        if command in alfabeto:
            turtle.forward(seg_length)
        elif command == "f":
            turtle.pu()
            turtle.forward(seg_length)
        elif command == "+":
            turtle.right(float(angulo))
        elif command == "-":
            turtle.left(float(angulo))
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)


def set_turtle(alpha_zero):
    r_turtle = turtle.Turtle()
    r_turtle.screen.title("L-System Derivation")
    r_turtle.speed(0)
    r_turtle.setheading(alpha_zero) 
    return r_turtle

