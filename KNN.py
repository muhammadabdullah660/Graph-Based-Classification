from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from graph import returnTravel, returnFashion, returnDisease,graphToVector,graphsToVectors

travelList = returnTravel()
fashionList = returnFashion()
diseaseList = returnDisease()
docs = travelList + fashionList + diseaseList
labels=['travel'] * len(travelList) + ['fashion'] * len(fashionList) + ['disease'] * len(diseaseList)

X_train, X_test, y_train, y_test = train_test_split(docs, labels, test_size=0.2, random_state=76)

# Initialize KNN classifier
X_train = graphsToVectors(X_train)
X_test = graphsToVectors(X_test)

classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
classifier.fit(X_train, y_train)

# Predict on the test set
predictions = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", int(accuracy*100))