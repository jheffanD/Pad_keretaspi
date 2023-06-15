import random
import tkinter as tk
from tkinter import messagebox
from collections import Counter
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self):
        self.data = []

    def generate_data(self, num):
        self.data = [random.randint(0, 20) for _ in range(num)]

    def display_data(self):
        print("Data:")
        print(self.data)

    def get_top_10_data(self):
        counter = Counter(self.data)
        top_10 = counter.most_common(10)
        return top_10

    def display_graph(self, option):
        if option == 1:
            self.display_most_common_graph()
        elif option == 2:
            self.display_random_graph()

    def display_most_common_graph(self):
        top_10 = self.get_top_10_data()
        labels, values = zip(*top_10)
        plt.bar(labels, values)
        plt.xlabel('Data')
        plt.ylabel('Frequency')
        plt.title('Top 10 Most Common Data')
        plt.show()

    def display_random_graph(self):
        random_10 = random.sample(self.data, 10)
        plt.bar(range(10), random_10)
        plt.xlabel('Index')
        plt.ylabel('Data')
        plt.title('Random 10 Data')
        plt.show()


def get_user_input(message):
    return input(message)


def get_validated_input(message):
    while True:
        user_input = get_user_input(message)
        if user_input.lower() == 'x':
            return 'x'
        try:
            num = int(user_input)
            if 0 < num <= 1000:
                return num
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a number or 'X'.")


def show_graph_options(data_processor):
    root = tk.Tk()
    root.withdraw()

    option = messagebox.askquestion("Graph Options", "Choose the graph display option.\n\n"
                                                    "Option 1: Top 10 Most Common Data\n"
                                                    "Option 2: Random 10 Data\n\n"
                                                    "Do you want to continue?", icon='question')

    if option == 'yes':
        data_processor.display_graph(1)
    else:
        data_processor.display_graph(2)

    root.mainloop()


def main():
    data_processor = DataProcessor()

    while True:
        num = get_validated_input("Enter the number of data to generate (1-1000), or 'X' to exit: ")
        if num == 'x':
            break

        data_processor.generate_data(num)
        data_processor.display_data()
        show_graph_options(data_processor)


if __name__ == '__main__':
    main()
