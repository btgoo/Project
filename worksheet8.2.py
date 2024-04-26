import matplotlib.pyplot as plt

def main():
    line1x = [10, 20, 30]
    line1y = [20, 40, 10]
    line2x = [10, 20, 30]
    line2y = [40, 10, 30]
    plt.plot(line1x, line1y, linewidth=3, label='Line 1', color='b')
    plt.plot(line2x, line2y, linewidth=5, label='Line 2', color='r')
    plt.title('Two or more line with different widths and colors with suitable legends')
    plt.xlabel('x - axis')
    plt.ylabel('y - label')
    plt.legend(loc='upper right')
    plt.show()

main()