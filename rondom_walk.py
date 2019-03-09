from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_list = [0]
        self.y_list = [0]

        self.walk()

    def walk(self):

        while len(self.x_list) < self.num_points:
            # 方向
            x_direction = choice([1, -1])
            # 距离
            x_distance = choice([0, 1, 2, 3, 4])
            # 在哪个方向走多少距离
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 如果原地踏步
            if y_step != 0 or x_step != 0:
                x_site = self.x_list[-1] + x_step
                y_site = self.y_list[-1] + y_step

                self.x_list.append(x_site)
                self.y_list.append(y_site)
            else:
                continue
