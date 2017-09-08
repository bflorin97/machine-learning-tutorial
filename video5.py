from scipy.spatial import distance
import random

def euc(a, b):
	return distance.euclidean(a,b)

class ScrappyKNN():
	def fit(self, X_train, Y_train):
		self.X_train = X_train
		self.Y_train = Y_train

	def predict(self, X_test):
		predictions = []

		for row in X_test:
			label = self.closest(row)
			predcitions.append(label)

		return predictions

	def closest(self, row):
		best_dist = euc(row, self.X_train[0])
		best_ind = 0;
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_ind = i
		return self.Y_train[best_ind]


from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
Y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .5)

#from sklearn.neighbors import KNeighborsClassifier


clf = ScrappyKNN()

clf.fit(X_train, Y_train)

predictions = clf.predict(X_test)

print predictions
from sklearn.metrics import accuracy_score
print accuracy_score(Y_test, predictions)
