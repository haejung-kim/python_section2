from matplotlib import pyplot as plt

data = [11,12,13,14,15]
catagories = ['label1','label2','label3','label4','label5']

plt.axis('equal')    # 이것을 안하며 타원임

# plt.pie(data)  : label 없이
plt.pie(data, labels=catagories)  # 옆에 설명
plt.legend(catagories)   #legend(전체 label)
plt.title('matplotlib')

plt.show()
