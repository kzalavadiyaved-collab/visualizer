import os
import matplotlib.pyplot as plt
import pandas as pd


class SalesDataAnalyzer:

    def __init__(self):
        self.df = None
        self.last_fig = None

    def load_dataset(self):
        print("\n== Load Dataset ==")
        path = input(
            "Enter the path of the dataset (CSV file): "
        ).strip()
        try:
            self.df = pd.read_csv(path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading file: {e}")

    def explore_data(self):
        if self.df is None:
            print("Please load a dataset first!")
            return

        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print(self.df.head())
        elif choice == "2":
            print(self.df.tail())
        elif choice == "3":
            print(list(self.df.columns))
        elif choice == "4":
            print(self.df.dtypes)
        elif choice == "5":
            print(self.df.info())
        else:
            print("Invalid choice!")

    def dataframe_operations(self):
        if self.df is None:
            print("Please load a dataset first!")
            return

        print("\n== Perform DataFrame Operations ==")
        print("1. Add/Perform Mathematical Operations")
        print("2. Filter Data")
        print("3. Sort Data")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            col = input("Enter numerical column name: ")
            op = input("Enter operation (+, -, *, /): ")
            val = float(input("Enter value: "))
            if op == "+":
                print(self.df[col] + val)
            elif op == "-":
                print(self.df[col] - val)
            elif op == "*":
                print(self.df[col] * val)
            elif op == "/":
                print(self.df[col] / val)
        elif choice == "2":
            col = input("Enter column to filter: ")
            val = input("Enter value to match: ")
            print(self.df[self.df[col].astype(str) == val])
        elif choice == "3":
            col = input("Enter column to sort by: ")
            print(self.df.sort_values(by=col))

    def handle_missing_data(self):
        if self.df is None:
            print("Please load a dataset first!")
            return

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            null_data = self.df[self.df.isnull().any(axis=1)]
            if null_data.empty:
                print("No missing values found in the dataset!")
            else:
                print(null_data)
        elif choice == "2":
            num_cols = self.df.select_dtypes(include=["number"]).columns
            self.df[num_cols] = self.df[num_cols].fillna(
                self.df[num_cols].mean()
            )
            print("Filled missing numerical values with mean!")
        elif choice == "3":
            self.df.dropna(inplace=True)
            print("Dropped rows with missing values!")
        elif choice == "4":
            val = input("Enter value to replace NaNs with: ")
            self.df.fillna(val, inplace=True)
            print(f"Replaced missing values with {val}!")

    def generate_descriptive_stats(self):
        if self.df is None:
            print("Please load a dataset first!")
            return
        print("\n== Descriptive Statistics ==")
        print(self.df.describe(include="all"))

    def data_visualization(self):
        if self.df is None:
            print("Please load a dataset first!")
            return

        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        choice = input("Enter your choice: ").strip()
        fig, ax = plt.subplots()

        if choice == "3":
            print("\n== Scatter Plot ==")
            x_col = input("Enter x-axis column name: ").strip()
            y_col = input("Enter y-axis column name: ").strip()
            print("Generating scatter plot...")
            ax.scatter(self.df[x_col], self.df[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} vs {x_col}")
            print("Scatter plot displayed successfully!")
        elif choice == "1":
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            ax.bar(self.df[x_col], self.df[y_col])
        elif choice == "2":
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            ax.plot(self.df[x_col], self.df[y_col])
        elif choice == "4":
            col = input("Enter column name for Pie Chart: ")
            ax.pie(
                self.df[col].value_counts(),
                labels=self.df[col].value_counts().index,
                autopct="%1.1f%%",
            )
        elif choice == "5":
            col = input("Enter column name for Histogram: ")
            ax.hist(self.df[col])
        elif choice == "6":
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            ax.stackplot(self.df[x_col], self.df[y_col])

        self.last_fig = fig
        plt.show()

    def save_visualization(self):
        if self.last_fig is None:
            print("No visualization found to save!")
            return

        print("\n== Save Visualization ==")
        filename = input(
            "Enter file name to save the plot (e.g., scatter_plot.png): "
        ).strip()
        self.last_fig.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")

    def run(self):
        while True:
            print("\n========== Data Analysis & Visualization Program ==========")
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("===========================================================")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.load_dataset()
            elif choice == "2":
                self.explore_data()
            elif choice == "3":
                self.dataframe_operations()
            elif choice == "4":
                self.handle_missing_data()
            elif choice == "5":
                self.generate_descriptive_stats()
            elif choice == "6":
                self.data_visualization()
            elif choice == "7":
                self.save_visualization()
            elif choice == "8":
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.run()
