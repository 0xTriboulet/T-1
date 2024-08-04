import pandas as pd

# Define the file path
CSV_FILE = './dataset/process_data.csv'


# BadDecisionTree class contains core functionality
class BadDecisionTree:
    def __init__(self, df: pd.DataFrame):
        self.data: pd.DataFrame = df


if __name__ == "__main__":

    # Read the CSV into a DataFrame
    data = pd.read_csv(CSV_FILE)

    BadTree = BadDecisionTree(data)

    # Print the contents of the DataFrame to the console
    print(BadTree.data)
