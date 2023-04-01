from matplotlib import pyplot as plt
from typing import List


def simple_data_visualization_line_graph() -> None:
    """Create a simple line chart"""
    years: List[int] = [1950, 1960, 1970, 1980, 1990, 2021, 2023]
    gdp: List[float] = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    plt.title("Nominal GDP")

    plt.ylabel("BI $")
    plt.xlabel("Years")
    plt.show()


def simple_data_visualization_bar_graph() -> None:
    """Create a simple line chart"""
    movies: List[str] = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars: List[int] = [5, 11, 3, 8, 10]

    plt.bar(movies, num_oscars)
    plt.ylabel("# Awards")
    plt.xlabel("Movies")
    plt.title("Movies and Awards")
    plt.show()


def simple_data_visualization_scatter_chart() -> None:
    """To see 2 data sets"""
    friends: List[int] = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes: List[int] = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels: List[chr] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(
            label,
            xy=(friend_count, minute_count),
            xytext=(5, -5),
            textcoords='offset points'
        )

    plt.title("Daily minutes vs number of friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spend")
    plt.show()



if __name__ == '__main__':
    # simple_data_visualization_line_graph()
    # simple_data_visualization_bar_graph()
    simple_data_visualization_scatter_chart()