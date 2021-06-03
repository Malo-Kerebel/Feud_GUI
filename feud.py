# import modules
import tkinter as tk
import csv


def show(i):
    global ses_score
    global ans_bt
    global answer

    answer.append(tk.Label(ws, text=question[i][j-1].replace('_', ' ')
                           + "      " + question[i][j]))
    answer[-1].place(x=length // 3 + (length // 6) * ((i-1) // 5),
                     y=45 + ((i-1) % 5) * 20)
    ans_bt[i-1].destroy()
    ses_score += int(question[i][j])
    show_score(ses_score)


def show_score(ses_score):
    global ses_score_lb

    try:
        ses_score_lb.destroy()
    except BaseException:
        1 + 1

    ses_score_lb = tk.Label(ws, text=str(ses_score), bg=bgcolour)
    ses_score_lb.place(x=length // 2, y=30, anchor="center")


def add_right():
    global ses_score
    global right_score
    global right_score_lb
    global add_right_bt
    global add_left_bt

    try:
        add_right_bt.destroy()
        add_left_bt.destroy()
    except BaseException:
        1 + 1

    try:
        right_score_lb.destroy()
    except BaseException:
        1 + 1

    right_score += ses_score
    right_score_lb = tk.Label(ws, text=str(right_score), pady=10, bg=bgcolour)
    right_score_lb.place(x=length - 40, y=50, anchor="center")


def add_left():
    global ses_score
    global left_score
    global left_score_lb
    global add_left_bt
    global add_right_bt

    try:
        add_left_bt.destroy()
        add_right_bt.destroy()
    except BaseException:
        1 + 1

    try:
        left_score_lb.destroy()
    except BaseException:
        1 + 1

    left_score += ses_score

    left_score_lb = tk.Label(ws, text=str(left_score), pady=10, bg=bgcolour)
    left_score_lb.place(x=40, y=50, anchor="center")


def add_error():
    global C
    global error
    global error_bt
    global img

    filename = tk.PhotoImage(file="strike.png")
    img = C.create_image(error * 50 + 50, 25, anchor="center", image=filename)

    img = tk.Label(image=filename)
    img.image = filename

    error += 1

    if error == 3:
        try:
            error_bt.destroy()
        except BaseException:
            1 + 1


def show_question():
    global j
    global ans_bt
    global answer
    global ses_score
    global question_lb
    global ses_score_lb
    global left_score
    global right_score
    global left_score_lb
    global right_score_lb
    global right_lb
    global left_lb
    global add_right_bt
    global add_left_bt
    global nex
    global C
    global error_bt
    global error

    ses_score = 0

    j += 2

    error = 0

    length_cv = 200
    height_cv = 50

    # label & Entry boxes territory
    try:
        sta.destroy()
        title.destroy()
    except BaseException:
        1 + 1

    try:
        left_lb.destroy()
        left_score_lb.destroy()
        right_lb.destroy()
        right_score_lb.destroy()
    except BaseException:
        1 + 1

    try:
        nex.destroy()
    except BaseException:
        1 + 1

    try:
        ses_score_lb.destroy()
    except BaseException:
        1 + 1

    try:
        question_lb.destroy()
        for i in ans_bt:
            i.destroy()
        for i in answer:
            i.destroy()
    except BaseException:
        1 + 1

    try:
        add_left_bt.destroy()
        add_right_bt.destroy()
    except BaseException:
        1 + 1

    try:
        C.destroy()
    except BaseException:
        1 + 1

    try:
        error_bt.destroy()
    except BaseException:
        1 + 1

    if j > len(question[:][0]):
        if left_score > right_score:
            tk.Label(ws,
                     text="Félicitation, " + Left_team + " gagne",
                     font=("Arial", 40),
                     bg=bgcolour
                     ).place(x=length // 2,
                             y=height // 2,
                             anchor="center")
        elif left_score < right_score:
            tk.Label(ws,
                     text="Félicitation, " + Right_team + " gagne",
                     font=("Arial", 40),
                     bg=bgcolour
                     ).place(x=length // 2,
                             y=height // 2,
                             anchor="center")
        else:
            tk.Label(ws,
                     text="Égalité",
                     font=("Arial", 40),
                     bg=bgcolour
                     ).place(x=length // 2,
                             y=height // 2,
                             anchor="center")
        return

    left_lb = tk.Label(ws, text="Team Left", pady=15, padx=15, bg=bgcolour)
    right_lb = tk.Label(ws, text="Team Right", pady=15, padx=15, bg=bgcolour)

    left_lb.place(x=40, y=25, anchor="center")
    right_lb.place(x=length - 40, y=25, anchor="center")

    question_lb = tk.Label(ws, text=question[0][j-1].replace("_", ' '),
                           pady=15, padx=10, bg=bgcolour)

    left_score_lb = tk.Label(ws, text=str(left_score), pady=10, bg=bgcolour)
    right_score_lb = tk.Label(ws, text=str(right_score), pady=10, bg=bgcolour)

    ans_bt = []
    answer = []

    i = 1
    try:
        while question[i][j] != '':
            ans_bt.append(tk.Button(ws,
                                    text=str(i),
                                    command=lambda s=i: show(s)))
            ans_bt[i-1].place(x=length // 3 + (length // 6) * ((i-1) // 5),
                              y=45 + ((i-1) % 5) * 20)
            i += 1
    except BaseException:
        1 + 1

    question_lb.place(x=length // 2, y=10, anchor="center")
    left_score_lb.place(x=40, y=50, anchor="center")
    right_score_lb.place(x=length - 40, y=50, anchor="center")
    show_score(ses_score)

    nex = tk.Button(ws,
                    text="Prochaine question",
                    command=lambda: show_question())
    nex.place(x=length - 10, y=height - 10, anchor="se")

    add_left_bt = tk.Button(ws, text=Left_team + " gagne", command=add_left)
    add_left_bt.place(x=20, y=height // 3, anchor="w")

    add_right_bt = tk.Button(ws, text=Right_team + " gagne", command=add_right)
    add_right_bt.place(x=length - 20, y=height // 3, anchor="e")

    error_bt = tk.Button(ws, text="Erreur", command=add_error)
    error_bt.place(x=length // 2, y=9 * height // 10, anchor="center")

    length_cv = 200
    height_cv = 50

    error = 0

    C = tk.Canvas(ws, bg=bgcolour, height=height_cv, width=length_cv,
                  borderwidth=0, highlightthickness=0)
    C.place(x=length // 2 - length_cv // 2, y=4 * height // 5)


f = open("question.csv")
reader = csv.reader(f)
question = list(reader)

left_score = 0
right_score = 0

Left_team = "Équipe gauche"
Right_team = "Équipe droite"

bgcolour = "#55AACC"

# configure workspace
ws = tk.Tk()
ws.title("Family Feud")
length = 1080
height = 720
ws.geometry(str(length) + 'x' + str(height))
ws.configure(bg=bgcolour)

j = -1

title = tk.Label(ws, text="Une famille en Or", font=("Arial", 40), bg=bgcolour)
title.place(x=length // 2, y=height // 3, anchor="center")

sta = tk.Button(ws, text="Démarrer", command=lambda: show_question())
sta.place(x=length // 2, y=2 * height // 3, anchor="center")

# infinite loop
ws.mainloop()
