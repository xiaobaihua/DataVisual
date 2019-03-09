import matplotlib.pyplot as plt

from rondom_walk import RandomWalk

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def test1():
    plt.scatter(2, 4, s=50)
    plt.title("123", fontsize=20)

    plt.xlabel('哈哈', fontsize=20)
    plt.ylabel('嘻嘻', fontsize=20)

    plt.tick_params(axis='both', labelsize=10)

    plt.show()


def test2():
    # 自动计算数据
    value = list(range(1, 10001))
    square_value = [x**2 for x in value]

    plt.scatter(value, square_value, s=10)

    plt.xlabel('123', fontsize=10)
    plt.ylabel('321', fontsize=10)

    plt.tick_params(axis='both', labelsize=20)

    plt.show()


def test3():
    # 删除轮廓
    value = list(range(1, 10001))
    square_value = [x**2 for x in value]

    plt.scatter(value, square_value, edgecolors='none', s=10)

    plt.xlabel('123', fontsize=10)
    plt.ylabel('321', fontsize=10)

    plt.tick_params(axis='both', labelsize=20)

    plt.show()


def test4():
    # 改变颜色
    value = list(range(1, 10001))
    square_value = [x**2 for x in value]

    plt.scatter(value, square_value, c=(1, 1, 0), edgecolors='none', s=10)

    plt.xlabel('123', fontsize=10)
    plt.ylabel('321', fontsize=10)

    plt.tick_params(axis='both', labelsize=20)

    plt.show()


def test5():
    # 使用colormap来映射数据大小, 体现为颜色深度
    value = list(range(1, 10001))
    square_value = [x**2 for x in value]

    plt.scatter(value, square_value, c=square_value, cmap='Reds', edgecolors='none', s=10)

    plt.xlabel('123', fontsize=10)
    plt.ylabel('321', fontsize=10)

    plt.tick_params(axis='both', labelsize=20)

    plt.show()


def test6():
    rw = RandomWalk()

    plt.scatter(rw.x_list, rw.y_list, linewidths=1)

    plt.xlabel('123', fontsize=20)

    plt.show()


test6()
