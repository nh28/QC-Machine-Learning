from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from joblib import dump, load

class Model:
    def __init__(self, X, y):
        """
        Initialize a new instance of Model.

        Parameters:
        X: The input as a dataframe.
        y: The output as a dataframe.
        """
        self.X = X
        self.y = y

    def create_model(self, version):
        """
        Create, train, and test a random forest model.

        Parameters:
        None
        """
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        # Instantiate Random Forest classifier with desired parameters
        rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

        # Train the Random Forest model
        rf_classifier.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = rf_classifier.predict(X_test)

        # Evaluate model performance
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)

        precision = precision_score(y_test, y_pred)
        print("Precision:", precision)

        dump(rf_classifier, 'SOG_model_' + str(version) + '.joblib')

    @staticmethod
    def predict_data(X, version):
        """
        Predict the accuracy of the data based on the SOG model.

        Parameters:
        X: The input data to predict accuracy for.
        """
        model = load('SOG_model_' + str(version) + '.joblib')
        return model.predict(X)