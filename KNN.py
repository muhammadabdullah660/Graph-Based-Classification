from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from graph import returnTravel, returnFashion, returnDisease, graphToVector, graphsToVectors

travelList = returnTravel()
fashionList = returnFashion()
diseaseList = returnDisease()
docs = travelList + fashionList + diseaseList
labels = ['travel'] * len(travelList) + ['fashion'] * len(fashionList) + ['disease'] * len(diseaseList)

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

# Calculate precision, recall, F1-score
precision, recall, f1_score, _ = precision_recall_fscore_support(y_test, predictions, average='weighted')

# Print precision, recall, and F1-score
print("Precision: ", int(precision*100))
print("Recall: ", int(recall*100))
print("F1-score: ", int(f1_score*100))

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Import libraries for plotting (assuming you don't have them already)
import matplotlib.pyplot as plt

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.colorbar()

# Set labels for each axis
classes = ['travel', 'fashion', 'disease']  # Assuming these are your class labels
plt.xticks(range(len(classes)), classes, rotation=45)
plt.yticks(range(len(classes)), classes)

# Add text labels to each cell of the confusion matrix
thresh = cm.max() / 2.0
for i in range(len(cm)):
  for j in range(len(cm)):
    plt.text(j, i, cm[i, j], ha="center", va="center",
             color="white" if cm[i, j] > thresh else "black")

# Set labels for title and axes
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')

# Show the confusion matrix plot
plt.tight_layout()
plt.show()
