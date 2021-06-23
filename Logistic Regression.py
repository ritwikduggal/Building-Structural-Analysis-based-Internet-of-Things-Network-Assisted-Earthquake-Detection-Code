import csv
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, plot_confusion_matrix

'''declaring SVM model'''
model = LogisticRegression()

'''Extracting data from csv file'''
with open("Data set/Data.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:6]],
            "label": int(row[6])
        })

'''dividing data into training and testing set'''
holdout = int(0.50*len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[:holdout]

X_training = [row["evidence"] for row in training]
Y_training = [row["label"] for row in training]

'''fiting training data into model'''
model.fit(X_training, Y_training)

X_testing = [row["evidence"] for row in testing]
Y_testing = [row["label"] for row in testing]

'''predicting testing data'''
predictions = model.predict(X_testing)

correct = 0
incorrect = 0
total = 0

'''calculating accuracy manually'''
for actual, predicted in zip(Y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1
print("Model: SVM")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100*correct/total:.4f}%")

'''plotting roc curve'''
y_pred1 = model.decision_function(X_testing)

lr_fpr, lr_tpr, threshold1 = roc_curve(Y_testing, y_pred1)
auc_lr = auc(lr_fpr, lr_tpr)

plt.figure(figsize=(5, 5), dpi=100)
plt.plot(lr_fpr, lr_tpr, linestyle='-', label='LR (auc = %0.4f)' % auc_lr)

plt.xlabel('False Positive Rate -->', weight='bold')
plt.ylabel('True Positive Rate -->', weight='bold')
ax = plt.gca()
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)

plt.legend()

plt.show()

'''plotting confusion matrix'''
disp = plot_confusion_matrix(model, X_testing, Y_testing, cmap=plt.cm.Blues, normalize=None)
disp.ax_.set_title("Confusion matrix")

print("Confusion matrix")
print(disp.confusion_matrix)

plt.show()