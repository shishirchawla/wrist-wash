import sys
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
import matplotlib
import pylab as plt
import itertools
import numpy as np

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
  """
  This function prints and plots the confusion matrix.
  Normalization can be applied by setting `normalize=True`.
  """
  if normalize:
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    print("Normalized confusion matrix")
  else:
    print('Confusion matrix, without normalization')

  plt.imshow(cm, interpolation='nearest', cmap=cmap)
  plt.title(title)
  plt.colorbar()
  tick_marks = np.arange(len(classes))
  plt.xticks(tick_marks, classes, rotation=45)
  plt.yticks(tick_marks, classes)

  fmt = '.1f' if normalize else 'd'
  thresh = cm.max() / 2.
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
  plt.ylabel('True label')
  plt.xlabel('Predicted label')

if __name__ == '__main__':
  if len(sys.argv) > 2:
    predfile = sys.argv[1]
    truthfile = sys.argv[2]
  else:
    print 'predfile and truthfile required'
    sys.exit()

#  label_map = {"activity1":"Step 1",
#  "activity2":"Step 2", "activity3":"Step 3", "activity4":"Step 4",
#  "activity5":"Step 5", "activity6":"Step 6", "activity7":"Step 7",
#  "activity8":"Step 8", "activity9":"Step 9", "activity10":"Step 10",
#  "activity11":"Step 11", "activity12":"Step 12", "activity13":"Step 13",
#  "activity14":"Step 14", "activity15":"Step 15", "activity16":"Step 16"}
  label_map = {"activity4":"Step 1",
  "activity5":"Step 2", "activity6":"Step 3", "activity7":"Step 4",
  "activity8":"Step 5", "activity9":"Step 6", "activity10":"Step 7",
  "activity11":"Step 8", "activity12":"Step 9", "activity13":"Step 10",
  "activity14":"Step 11", "activity15":"Step 12", "activity16":"Step 13"}

  label_map_values = ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5",
    "Step 6", "Step 7", "Step 8", "Step 9", "Step 10",
    "Step 11", "Step 12", "Step 13"]

  y_truth = []
  y_pred = []
  with open(truthfile) as f:
    for line in f:
      y_truth.append(label_map[line.strip().lower()])
  with open(predfile) as f:
    for line in f:
      y_pred.append(label_map[line.strip().lower()])

  cm = confusion_matrix(y_truth, y_pred, labels=label_map_values)
  f1w = f1_score(y_truth, y_pred, average="weighted")
  f1m = f1_score(y_truth, y_pred, average="macro")
  accuracy = accuracy_score(y_truth, y_pred)

  print 'Accuracy:', accuracy, 'F1 (weighted):', f1w, 'F1 (macro):', f1m
  print 'Confusion matrix:\n', cm

  if len(sys.argv) > 3:
    plotmatrix = sys.argv[3]
    if plotmatrix == '1':
      plt.figure()
      plot_confusion_matrix(cm, label_map_values, normalize=True)
      plt.show()

