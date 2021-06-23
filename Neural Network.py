import csv
import tensorflow as tf
import random
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score

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

evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]

'''dividing data into training and testing set'''
holdout = int(0.50*len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[:holdout]

X_training = [row["evidence"] for row in training]
Y_training = [row["label"] for row in training]
X_testing = [row["evidence"] for row in testing]
Y_testing = [row["label"] for row in testing]

'''declaring CNN model'''
model = tf.keras.models.Sequential()

'''adding layers to the model'''
model.add(tf.keras.layers.Dense(8, input_shape=(6,), activation="relu"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

'''fiting training data into model and running epochs'''
his = model.fit(evidence, labels, epochs=100, batch_size=10)
model.evaluate(X_testing, Y_testing, verbose=2)

yhat_classes = model.predict_classes(X_testing, verbose=0)
yhat_classes = yhat_classes[:, 0]

'''predicting testing data'''
precision = precision_score(Y_testing, yhat_classes)
print('Precision: %0.4f' % precision)

'''plotting accuracy vs epoch graph'''
ax = plt.gca()
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)

plt.plot(his.history['accuracy'])
plt.title('MODEL ACCURACY', weight='bold')
plt.ylabel('Accuracy', weight='bold')
plt.xlabel('Epoch', weight='bold')
plt.show()

'''plotting loss vs epoch graph'''
ax = plt.gca()
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)

plt.plot(his.history['loss'])
plt.title('MODEL LOSS', weight='bold')
plt.ylabel('Loss', weight='bold')
plt.xlabel('Epoch', weight='bold')
plt.show()
