from matplotlib import pyplot as plt
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs =[x for x,_ in enumerate(movies)]

plt.bar(xs,num_oscars)

plt.xlabel("Movies")

plt.ylabel("No. of Oscars")

plt.xticks(xs,movies)

plt.show()