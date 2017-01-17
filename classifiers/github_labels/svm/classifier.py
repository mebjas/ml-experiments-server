import sys
import pickle
import time
from sklearn import svm
from sklearn.metrics import accuracy_score

sys.path.append("../../../libs")
from dataset import loadData
from datapreprocessing import preprocess

dataset_name = "github-issue-bug-enhancement"
ratio = 50

print ("loading dataset %s from files" % dataset_name)
dataset = loadData(dataset_name, False)
labels = loadData(dataset_name, True)

print ("dataset and labels loaded, splitting using cross_validation")
features_train, features_test, labels_train, labels_test = preprocess(dataset, labels, 1 - (ratio / 100))

# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

print ("training classifier using SVM")
_start = time.time()
clf = svm.SVC()
clf.fit(features_train, labels_train)
_training_time = time.time() - _start
_start = time.time()

print ("predicting test data")
result = clf.predict(features_test)
_prediciton_time = time.time() - _start

print ("training size - %s%%, test size - %s%% on dataset `%s`" % (ratio, 100 - ratio, dataset_name))
print ("Accuracy - %s, Classification Time - %s, Prediciton Time - %s" % (accuracy_score(result, labels_test), _training_time, _prediciton_time))


