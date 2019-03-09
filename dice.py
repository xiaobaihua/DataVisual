import random

import pygal


class Dice:
    def __init__(self, face_sum=6):
        self.face_sum = face_sum
        self.dice_list = list(range(self.face_sum + 1))
        self.value_list = []
        self.result_list = []

    def roll_value(self, roll_sum=500):
        for i in range(roll_sum):
            self.value_list.append(random.choice(self.dice_list))
        return self.value_list

    def get_value_list(self):
        self.roll_value()

        for i in range(7):
            j = self.value_list.count(i)
            self.result_list.append(j)

        return self.result_list


dice = Dice(6)

result_list = dice.get_value_list()

line_chart = pygal.Bar()
line_chart.x_labels = range(7)

line_chart.add('嘻嘻', result_list)

line_chart.render_to_file('123.svg')
