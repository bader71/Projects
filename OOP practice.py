import numpy as np
import matplotlib.pyplot as plt

class Robots():

    def Tom(self):
        us_list = []
        promt_user1= input("Hello there, my name is Tom, what's your name? ")
        print("Nice to meet you,", promt_user1.upper())
        op = input("what can i help you with? addition, mean, Max, Min")
        if op.lower() == "addition":
            while True:
                add = input("please put the numbers you want to add together, when you're done type done: ")
                try:
                    val = int(add)
                    us_list.append(val)
                    print(us_list)
                except ValueError:
                    break
            np_us_list = np.array(us_list)
            print("Your total is:", np_us_list.sum())
        elif op.lower() == "mean":
            while True:
                mean = input("please put the numbers you want to add together, when you're done type done: ")
                try:
                    val = int(mean)
                    us_list.append(val)
                    print(us_list)
                except ValueError:
                    break
            np_us_list = np.array(us_list)
            print("Your mean is:", np_us_list.mean())
        elif op.lower() == "max":
            while True:
                max_ = input("please put the numbers you want to add together, when you're done type done: ")
                try:
                    val = int(max_)
                    us_list.append(val)
                    print(us_list)
                except ValueError:
                    break
            np_us_list = np.array(us_list)
            print("Your max is:", np_us_list.max())
        elif op.lower() == "min":
            while True:
                min_ = input("please put the numbers you want to add together, when you're done type done: ")
                try:
                    val = int(min_)
                    us_list.append(val)
                    print(us_list)
                except ValueError:
                    break
            np_us_list = np.array(us_list)
            print("Your min is:", np_us_list.min())


    def Jerry(self):
        x_values = []
        y_values = []
        promt_user2 = input("Hello there, my name is Tom, what's your name? ")
        print("Nice to meet you,", promt_user2.upper())
        while True:
            x_data = input("Please put your X data: ")
            try:
                x_val = int(x_data)
                x_values.append(x_val)
                print(x_values)
            except ValueError:
                break
        np_x_values = np.array(x_values)
        print("Your X data is", np_x_values)
        while True:
            y_data = input("Please input you Y data: ")
            try:
                y_val = int(y_data)
                y_values.append(y_val)
                print(y_values)
            except ValueError:
                break
        np_y_values = np.array(y_values)
        print("Your Y data is", np_y_values)
        plt.plot(np_x_values, np_y_values)
        plt.show()




x = Robots()
choice = input("Who do you wanna talk to? Tom or Jerry?")
if choice.lower() == "tom":
        x.Tom()
elif choice.lower() == "jerry":
    x.Jerry()