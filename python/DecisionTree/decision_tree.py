import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Define the file path
CSV_FILE = './dataset/process_data.csv'

MIN_DATASET_SIZE = 50


class BadDecisionTree:
    def __init__(self, df: pd.DataFrame):
        self.best_model = None
        self.model: DecisionTreeClassifier = DecisionTreeClassifier()
        self.hyperparams: dict = {
            'max_depth': np.arange(1, 10).astype(np.uint64),
            'min_samples_leaf': np.arange(1, 50).astype(np.uint64),
            'min_samples_split': np.arange(2, 10).astype(np.uint64),
            'criterion': ["gini", "entropy"],
            'splitter': ["best", "random"],
        }

        self.data = df

        if self.data.shape[0] < MIN_DATASET_SIZE:
            self._data_augment()

        self.X = self.data.drop('Sandbox Score', axis=1)
        self.y = self.data['Sandbox Score']

    def _data_augment(self) -> None:
        self.data = self.data.sample(n=MIN_DATASET_SIZE, replace=True)

    def tune_hyperparameters(self) -> None:
        # Number of iteration for RandomizedSearchCV
        n_iter_search = 20
        # Setting up the Randomized Search with cross validation
        self.best_model = RandomizedSearchCV(self.model, param_distributions=self.hyperparams,
                                             n_iter=n_iter_search, cv=5)

        self.best_model.fit(self.X, self.y)
        return self.best_model.best_params_

    def visualize_tree(self, filename: str):
        # Check if best_model is not None and if it's been fit
        if self.best_model and hasattr(self.best_model, 'best_estimator_'):
            # Initialize the figure size
            plt.figure(figsize=(100, 60), dpi=100)  # increase figure size and dpi
            # Use plot_tree from sklearn.tree to visualize the tree
            plot_tree(self.best_model.best_estimator_,
                      feature_names=self.X.columns,
                      class_names=True,
                      filled=True)
            # Save the tree
            plt.savefig(filename)
        else:
            print("The model has not been created or fitted yet")


if __name__ == "__main__":

    # Read the CSV into a DataFrame
    data = pd.read_csv(CSV_FILE)

    BadTree = BadDecisionTree(data)

    # Print the contents of the DataFrame to the console
    print(BadTree.data)
    print(BadTree.X)
    print(BadTree.y)

    # Print hyperparameters
    print("\n\nTraining BadTree:")
    print(BadTree.tune_hyperparameters())

    # Define the data and the column names
    data = [[140, 70, 2]]  # The data inside two brackets makes it a 2D list which represents one row and three columns
    columns = ['Process Count', 'Process Count/User', 'User Count']

    test_frame = pd.DataFrame(data, columns=columns)

    # Make a prediction on our novel test frame
    print(f'BadTree test frame:\n {test_frame}')
    print(f'BadTree prediction frame: {BadTree.best_model.predict(test_frame)}')

    # Visualize and save the decision tree
    BadTree.visualize_tree("badtree.png")
