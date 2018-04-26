import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

# ********** Setting *********************
filename = 'weizu1_result.txt'
fpr_thresh = 0.001
# ****************************************


def get_data(filename):
    """get ground truth labels and predicted labels
    The format of each line in result file is [gt_label pred_score image_name]
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    num_items = len(lines)
    data = np.zeros((num_items, 2))
    for i, line in enumerate(lines):
        line = line.split()
        data[i, 0] = float(line[0])
        data[i, 1] = float(line[1])
    return data


def main():
    data = get_data(filename)
    gt_labels = data[:, 0]
    pred_scores = data[:, 1]
    fpr, tpr, threshold = roc_curve(gt_labels, pred_scores)

    idx = np.where(fpr <= fpr_thresh)[0][-1]
    print('threshold:', threshold[idx])

    print("\n\nFPR = {:.3f}, TPR = {:.2f}\n".format(fpr_thresh, tpr[idx]))

    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()


if __name__ == '__main__':
    main()