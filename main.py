from tkinter import *
import turtle as t
from turtle import Screen
import time
import random

EXPLANATION_FONT = ("Arial", 30, "normal")
EXPLANATION_ALNMT = "center"
EXPLANATION_COORD = (0, -200)

symbols = {
    "+": "add",
    "-": "subtract",
    "/": "divide",
    "*": "multiply",
    " ": "whitespace",
    "(": "opening parenthesis",
    ")": "closing parenthesis",
    "^": "power"
}


def valid_input_check(users_input):
    valid_numbers = []
    for anum in range(10):
        newnum = str(anum)
        valid_numbers.append(newnum)

    valid_symbols = symbols
    input_to_check = str(users_input)
    for item in input_to_check:
        if item not in valid_symbols and item not in valid_numbers:
            solution_label.config(text="Please type the problem correctly")
            return "FAILED"


def calculate_clicked():
    if len(user_problem.get().split()) == 0:
        solution_label.config(text="Please enter something")
    elif valid_input_check(user_problem.get()) == "FAILED":
        pass
    else:
        main_problem = user_problem.get()
        answer = calculate(main_problem)
        user_problem.delete(0, END)
        user_problem.insert(0, answer)
        solution_label.config(text=f"{main_problem} = {answer}")


def showme_clicked():
    if len(user_problem.get().split()) == 0:
        solution_label.config(text="Please enter something")
    elif valid_input_check(user_problem.get()) == "FAILED":
        pass
    else:
        solution_label.config(text="Thinking...")
        tutor_me(user_problem.get())


def tutor_me(given_problem):
    problem = given_problem.split()
    screen = Screen()

    while len(problem) > 1:
        value1 = int(problem[0])
        value2 = int(problem[2])
        problem_symbol = problem[1]
        values_sum = value1 + value2

        answer = quick_calculate(value1, value2, problem_symbol)

        turtlelist1 = []
        turtlelist2 = []

        explanation = t.Turtle()
        explanation.ht()
        explanation.penup()
        explanation.goto(EXPLANATION_COORD)

        if len(problem) > 3:
            explanation.write(f"{given_problem} is a big problem, so we're going to split it up.",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()

            explanation.write(f"For now, we are just going to work on a small piece of the problem",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()

            explanation.write(f"Let's do {value1} {problem_symbol} {value2}", font=EXPLANATION_FONT,
                              align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()

        # _________________________________________ Set up value1's Turtles ___________________________________________
        x_coord = None
        y_coord = 0

        if value1 >= 10 or value2 >= 10:
            max_xcoord = 250
        else:
            if problem_symbol == "+":
                max_xcoord = (values_sum / 2) * 25
            else:
                max_xcoord = (value1 / 2) * 25

        min_xcoord = max_xcoord * -1

        if x_coord is None:
            x_coord = min_xcoord

        for x in range(value1):
            if x_coord == min_xcoord:
                pass
            elif x_coord >= max_xcoord:
                x_coord = min_xcoord
                y_coord += 50
            numbered_turtle = t.Turtle()
            turtlelist1.append(numbered_turtle)
            turtlelist1[x].shape("turtle")
            turtlelist1[x].color("red")
            turtlelist1[x].penup()
            turtlelist1[x].setheading(90)
            turtlelist1[x].speed(3)
            turtlelist1[x].goto(x_coord, y_coord)
            x_coord += 50

        # _________________________________________ SMALL NUMBER ADDITION _____________________________________________

        if problem_symbol == "+":

            for x in range(value2):
                if x_coord >= max_xcoord:
                    x_coord = min_xcoord
                    y_coord += 50
                numbered_turtle = t.Turtle()
                turtlelist2.append(numbered_turtle)
                turtlelist2[x].shape("turtle")
                turtlelist2[x].color("blue")
                turtlelist2[x].penup()
                turtlelist2[x].setheading(90)
                turtlelist2[x].speed(3)
                turtlelist2[x].goto(x_coord, y_coord)
                turtlelist2[x].st()
                x_coord += 50

            explanation.write(f"We have {value1} Red Turtles, and {value2} Blue Turtles", font=EXPLANATION_FONT,
                              align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()

            explanation.write("Let's make them the same color",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(10)
            explanation.clear()

            for item in turtlelist2:
                item.color("red")

            time.sleep(2)

        # _________________________________________ SMALL NUMBER SUBTRACTION _________________________________________
        elif problem_symbol == "-":
            explanation.write(f"We have {value1} Red Turtles.",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()

            explanation.write(f"Since we are subtracting {value2}, We need to take away {value2} Turtles.",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(5)
            explanation.clear()
            for x in range(value2):
                subtraction_index = -1
                turtlelist1[subtraction_index].ht()
                turtlelist1[subtraction_index].clear()
                turtlelist1.pop(subtraction_index)
                time.sleep(1.5)

        explanation.write("Now we can count our Red turtles.",
                          font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)

        time.sleep(5)
        current_number = 1
        hiddennumber = 0
        hiddennumber2 = 0

        for number in range(answer):
            explanation.clear()

            try:
                new_xcor = turtlelist1[number].xcor()
            except IndexError:
                new_xcor = turtlelist2[hiddennumber].xcor()
                hiddennumber += 1
            try:
                new_ycor = turtlelist1[number].ycor()
            except IndexError:
                new_ycor = turtlelist2[hiddennumber2].ycor()

                hiddennumber2 += 1

            new_ycor -= 35
            explanation.goto(new_xcor, new_ycor)
            explanation.write(f"{current_number}",
                              font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            current_number += 1
            time.sleep(1)
        time.sleep(2)
        explanation.clear()
        explanation.goto(0, -200)
        explanation.write(f"We have {answer} turtles",
                          font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        time.sleep(5)
        explanation.clear()
        explanation.write(f"So our answer is {answer}",
                          font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        time.sleep(5)
        explanation.clear()
        for item in turtlelist1:
            item.ht()
            item.clear()
        for item in turtlelist2:
            item.ht()
            item.clear()
        problem.pop(2)
        problem.pop(1)
        problem[0] = answer

    # screen.exitonclick()


# ________________________ Addition with bigger numbers ____________________________


def get_digit_length(num1, num2, sym):
    num3 = len(str(quick_calculate(num1, num2, sym)))
    num2 = len(str(num2))
    num1 = len(str(num1))
    return max(num1, num2, num3)


def math_table():
    number1 = random.randint(0, 9999)
    number2 = 840
    symbol = "+"

    answer = quick_calculate(number1, number2, symbol)

    tablemaker = t.Turtle()
    tablemaker.width(2)
    tablemaker.ht()
    tablemaker.penup()
    tablescreen = Screen()
    column_colors = ["lightcoral", "lightskyblue", "gold", "palegreen"]
    digits = get_digit_length(number1, number2, symbol)
    rightedge = (digits * 50) / 2
    leftedge = 0 - rightedge
    pen_lineup = rightedge
    y_max_boundary = 100
    horizontal_line_length = (digits + 1) * 50

    for number in range(digits):
        tablemaker.goto(pen_lineup, y_max_boundary)
        if number >= 4:
            tablemaker.fillcolor(column_colors[number - 4])
        else:
            tablemaker.fillcolor(column_colors[number])
        tablemaker.begin_fill()
        tablemaker.setheading(270)
        tablemaker.forward(150)
        tablemaker.setheading(180)
        tablemaker.forward(50)
        tablemaker.setheading(90)
        tablemaker.forward(150)
        tablemaker.setheading(0)
        tablemaker.forward(50)
        tablemaker.end_fill()
        tablemaker.penup()
        pen_lineup -= 50

    pen_lineup = rightedge

    # Create as many columns for every digit + an extra column for the symbol used
    for every_number in range(digits + 2):
        tablemaker.goto(pen_lineup, y_max_boundary)
        tablemaker.setheading(270)
        tablemaker.pendown()
        tablemaker.forward(150)
        tablemaker.penup()
        pen_lineup -= 50

    # Re-align pen for horizontal lines
    pen_lineup = rightedge

    # Draws horizontal lines but makes the solution line slightly thicker
    for number in range(4):
        if number == 2:
            tablemaker.width(5)
        else:
            tablemaker.width(2)

        tablemaker.goto(pen_lineup, y_max_boundary)
        tablemaker.setheading(180)
        tablemaker.pendown()
        tablemaker.forward(horizontal_line_length)
        tablemaker.penup()
        y_max_boundary -= 50
        tablemaker.goto(pen_lineup, y_max_boundary)

    # Writes first 2 Numbers in:
    number1 = str(number1)
    number2 = str(number2)
    answer = str(answer)
    pen_lineup = rightedge - 25
    ypen_lineup = 100 - 45
    for digit in reversed(range(len(number1))):
        tablemaker.goto(pen_lineup, ypen_lineup)
        tablemaker.write(f"{number1[digit]}", font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        pen_lineup -= 50

    pen_lineup = rightedge - 25
    ypen_lineup = 50 - 45
    for digit in reversed(range(len(number2))):
        tablemaker.goto(pen_lineup, ypen_lineup)
        tablemaker.write(f"{number2[digit]}", font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        pen_lineup -= 50

    # Add Symbols in before the solution number:
    tablemaker.goto(leftedge - 25, ypen_lineup)
    tablemaker.write(f"{symbol}", font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)

    # ________ Problem explanation section
    problem_type = symbols[symbol]
    tblexpln = t.Turtle()
    tblexpln.ht()
    tblexpln.penup()
    tblexpln.goto(EXPLANATION_COORD)

    tblexpln.write(f"We need to {problem_type} these numbers step by step first.", font=EXPLANATION_FONT,
                   align=EXPLANATION_ALNMT)
    time.sleep(10)
    tblexpln.clear()

    # Line up pen for solution input
    pen_lineup = rightedge - 25
    ypen_lineup = 0 - 45
    current_column = -1
    
    for i in range(len(answer)):

        if current_column == -1:
            tblexpln.write(f"In the first column, we have {number1[current_column]} {symbol} {number2[current_column]}",
                           font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(10)
            tblexpln.clear()
        else:
            tblexpln.write(f"In the next column, we have {number1[current_column]} {symbol} {number2[current_column]}",
                           font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(10)
            tblexpln.clear()
            
        # Cover problem so other turtle explanation can function, and we can go back to this problem later.
        
        if number1[current_column] == "0" and number2[current_column] == "0":
            tblexpln.write(f"Since we are {symbols[symbol]}ing 0 & 0, the answer is 0!",
                           font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
            time.sleep(10)
            tblexpln.clear()
            
        elif number1[current_column] == "0" or number2[current_column] == "0":
            if symbol != "*" or symbol != "^":
                if number1[current_column] == "0":
                    suppl_value = number2[current_column]
                else:
                    suppl_value = number1[current_column]
                tblexpln.write(f"Whenever you {symbols[symbol]} {suppl_value} to 0, you will always just have "
                               f"{suppl_value}",
                               font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
                time.sleep(10)
                tblexpln.clear()

            elif symbol == "*" or symbol == "^":
                if symbol == "*":
                    suppl_value = 0
                else:
                    suppl_value = 1
                tblexpln.write(
                    f"Whenever you {symbols[symbol]} anything to 0, your answer will always be {suppl_value}",
                    font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
                time.sleep(10)
                tblexpln.clear()
            else:
                cover = t.Turtle()
                covers_screen = t.Screen()
                covers_screen.tracer(0)
                cover.speed(0)
                cover.ht()
                cover.penup()
                cover.goto(1500, 1500)
                cover.fillcolor("white")
                cover.pendown()
                cover.begin_fill()
                for number in range(4):
                    cover.right(90)
                    cover.forward(3000)
                cover.end_fill()
                covers_screen.update()
                covers_screen.tracer(1)
                tutor_me(f"{number1[current_column]} {symbol} {number2[current_column]}")
                cover.clear()

        tblexpln.write(f"So the answer to {number1[current_column]} {symbol} {number2[current_column]} is "
                       f"{answer[current_column]}",
                       font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        time.sleep(10)
        tblexpln.clear()
        tblexpln.write(f"We can add {answer[current_column]} to the column it belongs in now.",
                       font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        time.sleep(10)
        tblexpln.clear()

        tablemaker.goto(pen_lineup, ypen_lineup)
        tablemaker.write(f"{answer[current_column]}", font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
        pen_lineup -= 50
        current_column -= 1

    tblexpln.clear()

    # _____ Add the solution at the bottom

    # pen_lineup = rightedge - 25
    # ypen_lineup = 0 - 45
    # for digit in reversed(range(len(answer[current_column]))):
    #     tablemaker.goto(pen_lineup, ypen_lineup)
    #     tablemaker.write(f"{answer[digit]}", font=EXPLANATION_FONT, align=EXPLANATION_ALNMT)
    #     pen_lineup -= 50

    tablescreen.exitonclick()


# Quick function to get the answer between two numbers
def quick_calculate(num1, num2, sym):
    if sym == "+":
        return num1 + num2
    elif sym == "-":
        return num1 - num2
    elif sym == "*":
        return num1 * num2
    elif sym == "/":
        return num1 / num2
    elif sym == "^":
        return num1 ** 2


def calculate(given_problem):
    # Do a function that calculates the problem and returns the answer
    problem = given_problem.split()

    while len(problem) > 1:
        if problem[1] in symbols:
            value1 = int(problem[0])
            value2 = int(problem[2])
            symbol = problem[1]

            answer = None

            if symbol == "+":
                answer = value1 + value2
            elif symbol == "-":
                answer = value1 - value2
            elif symbol == "*":
                answer = value1 * value2
            elif symbol == "/":
                answer = value1 / value2

            if answer is not None:
                problem[0] = answer
            else:
                solution_label.config(text="Error with your math symbol")

            problem.pop(2)
            problem.pop(1)
    if len(problem) == 1:
        return problem[0]


window = Tk()
window.title("Moonie Math Tutoring")
window.minsize(width=850, height=600)
window.config(padx=100, pady=100)

reminder_label = Label(text="Please put a space between all numbers and symbols!", font=('Ariel', 20, 'bold'))
reminder_label.grid(column=2, row=0)

problem_space_label = Label(text="Type in your math problem:")
problem_space_label.grid(column=2, row=1)

solution_label = Label(text="", font=('Ariel', 20, "bold"))
solution_label.grid(column=2, row=3)

user_problem = Entry(width=100)
user_problem.grid(column=2, row=2)

calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(column=2, row=3, sticky="W")

showme_button = Button(text="Show me how to solve this", command=showme_clicked)
showme_button.grid(column=2, row=3, sticky="E")

testing_button = Button(text="Tester", command=math_table)
testing_button.grid(column=2, row=3)

window.mainloop()
