import math

def create_command_line_graph(f, x_min, x_max, y_min, y_max):
    max_label_len = max(len(str(x_max)), len(str(y_max)), len(str(x_min)), len(str(y_min)))
    axis_width = max_label_len + 1
    for y in range(y_max, y_min-1, -1):
        line = ""
        for x in range(x_min, x_max+1):
            if y == round(f(x)):
                line += "o".center(axis_width)
            elif y == 0 and x != 0:
                line += "—".center(axis_width)
            elif x == 0 and y != 0:
                line += "|".center(axis_width)
            elif x == 0 and y == 0:
                line += "+".center(axis_width)
            else:
                line += " ".center(axis_width)
        print(line)

def my_function(x):
    return 3*x**2/math.pi*x

x_min = -30
x_max = 30
y_min = -30
y_max = 30

create_command_line_graph(my_function, x_min, x_max, y_min, y_max)
