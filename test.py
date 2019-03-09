import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
squares = [1, 4, 9, 16, 25, 36, 49]
input_value = [1, 2, 3, 4, 5, 6, 7]
plt.plot(input_value, squares, linewidth=3)

plt.title("哈哈~", fontsize=30)
plt.xlabel("姓名", fontsize=15)
plt.ylabel("年龄", fontsize=15)

plt.tick_params(axis='both', labelsize=10)
plt.show()


