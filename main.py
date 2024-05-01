import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct ",
                                    "What's another state name ?").title()


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        anam = turtle.Turtle()
        anam.hideturtle()
        anam.penup()
        state_date = data[data.state == answer_state]
        anam.goto(int(state_date.x), int(state_date.y))
        anam.write(state_date.state.item())








