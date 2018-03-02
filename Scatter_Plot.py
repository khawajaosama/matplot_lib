from matplotlib import pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
plt.axis([58,74,80,240])
plt.title("Daily Minutes vs. Number of Friends")

plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
for label,friend,minute in zip(labels,friends,minutes):
    plt.annotate(label,xy=(friend,minute), xytext=(5,-4), textcoords='offset points')


plt.show()