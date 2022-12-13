#let's see if I did this right...

import numpy
import matplotlib

from sklearn.datasets import load_digits

digits_data = load_digits()

digits_data.data.shape

import matplotlib.pyplot as plt

plt.matshow(digits_data.images[0])
plt.show()

plt.gray()
plt.matshow(digits_data.images[0])
plt.show()

digits_data.images[0]

images = list(zip(digits_data.images, digits_data.target))

plt.figure(figsize=(4,4))

for i, (image, label) in enumerate(images[:10]):
	#initializing subplot of 3x5
	plt.subplot(3,5, i+1)
	#display images in the subplots
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	#set title for each subplot
	plt.title("Training: %i" % label)
plt.show()

#get the total number of samples
img_samples = len(digits_data.images)

#get the handwritten images
img = digits_data.images.reshape(img_samples, -1)

#get the target labels
labels = digits_data.target

from sklearn import svm
classify = svm.SVC(gamma=0.001)

#flatten sample images are stored in img variable
img_half = img[:img_samples // 2]
#target labels are stored in labels variable
labels_half = labels[:img_samples // 2]

classify.fit(img_half, labels_half)

labels_expected = digits_data.target[img_samples // 2:]
img_predicted = classify.predict(img[img_samples // 2:])

images_predictions = list(zip(digits_data.images[img_samples // 2:], img_predicted))

for i, (image, predict) in enumerate(images_predictions[:10]):
	#initialize the subplot of size 3x5
	plt.subplot(3,5, i+1)
	#turn of the axis values (the labels for each value in x and y axis)
	plt.axis('off')
	#display the predicted images in the subplot
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	#set the title for each subplot in the main plot
	plt.title("Predict: %i" % predict)
plt.show()

from sklearn import metrics

print("Classification Report %s:\n%s\n"
      % (classify, metrics.classification_report(labels_expected, img_predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(labels_expected, img_predicted))




