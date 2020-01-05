from matplotlib import pyplot as plt

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
y2_values = [11,12,13,14,15]

plt.plot(x_values, y_values,)
plt.plot(x_values, y2_values)
# plt.plot(x_values, y_values,'o') -> option(o) 점으로 표현

# x축(xlabel),y축(ylabel),title(제목),legend(주석)
plt.xlabel('axis-x')
plt.ylabel('axis-y')
plt.title('matplotlib')

plt.legend(['test1','test2'])
plt.show()
