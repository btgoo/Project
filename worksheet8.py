import matplotlib.pyplot as plt

def main():
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    teams = [0, 1, 2, 3, 4, 5]
    bar_width = 0.75
    plt.xlabel('Football team')
    plt.ylabel('Popularity')
    plt.xticks([0, 1, 2, 3, 4, 5],['Manchester United', 'Liverpool', 'Chelsea', 'Manchester City', 'Arsenal', 'Totenham'])
    plt.bar(teams, popularity, bar_width, color='blue')
    plt.title('Popularity Of Football Team')
    plt.grid(True, color='r')
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle='-.', linewidth='0.5', color='gray')
    plt.show()

    main()
