import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# Define the file path
CSV_FILE = './dataset/process_data.csv'

MIN_DATASET_SIZE = 100
R_STATE = 42

class BadDecisionTree:
    def __init__(self, df: pd.DataFrame):
        self.best_model = None
        self.model: DecisionTreeClassifier = DecisionTreeClassifier(random_state=R_STATE)
        self.hyperparams: dict = {
            'max_depth': np.arange(1, 10, dtype=int),
            'min_samples_leaf': np.arange(1, 50, dtype=int),
            'min_samples_split': np.arange(2, 10, dtype=int),
            'criterion': ["gini", "entropy", "log_loss"],
            'splitter': ["best", "random"],
            'class_weight': ["balanced", None],
            'ccp_alpha': np.linspace(0, 0.1, 50)   # 100 values between 0 and 1
        }


        self.init_data: pd.DataFrame = df
        
        self.data: pd.DataFrame = self.init_data.sample(frac=0.75, random_state=R_STATE)
        self.test_data: pd.DataFrame = self.init_data.drop(self.data.index)

        self.best_score: float = 0.0
        
        if self.data.shape[0] < MIN_DATASET_SIZE:
            self._data_augment()

        self.X_train = self.data.drop('Sandbox Score', axis=1)
        self.y_train = self.data['Sandbox Score']        
        
        self.X_test = self.test_data.drop('Sandbox Score', axis=1)
        self.y_test = self.test_data['Sandbox Score']

    def _data_augment(self) -> None:
        self.data = self.data.sample(n=MIN_DATASET_SIZE, replace=True)

    def tune_hyperparameters(self) -> None:
        # Number of iteration for RandomizedSearchCV
        n_iter_search = 5000
        
        # Setting up the Randomized Search with cross validation
        self.best_model = RandomizedSearchCV(self.model, param_distributions=self.hyperparams,
                                             n_iter=n_iter_search, cv=5, scoring='accuracy', random_state=R_STATE)

        self.best_model.fit(self.X_train, self.y_train)
        self.best_score = self.best_model.best_score_
        return self.best_model.best_params_

    def visualize_tree(self, filename: str):
        # Check if best_model is not None and if it's been fit
        if self.best_model and hasattr(self.best_model, 'best_estimator_'):
            plt.figure(figsize=(10, 6), dpi=100)  # increase figure size and dpi

            # Use plot_tree from sklearn.tree to visualize the tree
            plot_tree(self.best_model.best_estimator_,
                      feature_names=self.X_train.columns,
                      class_names=True,
                      rounded=True,
                      fontsize=8,
                      filled=True)

            # Save the tree
            plt.savefig(filename)
        else:
            print("The model has not been created or fitted yet")


if __name__ == "__main__":

    # Read the CSV into a DataFrame
    data = pd.read_csv(CSV_FILE)

    BadTree = BadDecisionTree(data)

    # Print hyperparameters
    print("\n\nTraining BadTree:")
    print(BadTree.tune_hyperparameters())

    # Define the data and the column names
    data = [[140, 70, 2]]  # The data inside two brackets makes it a 2D list which represents one row and three columns
    columns = ['Process Count', 'Process Count/User', 'User Count']
    test_frame = pd.DataFrame(data, columns=columns)

    badtrer_predict_test = BadTree.best_model.predict(BadTree.X_test)
    badtree_acc = accuracy_score(badtrer_predict_test, BadTree.y_test) 

    # Make a prediction on our novel test frame
    print(f'BadTree accuracy       : {badtree_acc * 100:.2f}%\n')


    # Visualize and save the decision tree
    BadTree.visualize_tree("badtree.png")
