import numpy as np

from sklearn.metrics import roc_auc_score

def get_binary_classification_eval(y, y_hat):

    get_fc = lambda x: float(np.count_nonzero(x))
    p = get_fc(y > 0)
    p_hat = get_fc(y_hat > 0)
    n = get_fc(y < 0)
    n_hat = get_fc(y_hat < 0)
    tp = get_fc(np.logical_and(y_hat == y, y_hat > 0))
    tn = get_fc(np.logical_and(y_hat == y, y_hat < 0))
    accuracy = (tp + tn) / y.shape[0]
    sensitivity = tp / p
    specificity = tn / n
    precision = 1 if p_hat == 0 else tp / p_hat
    f1 = 0 if precision + sensitivity == 0 else \
        2 * precision * sensitivity / (precision + sensitivity)
    auroc = roc_auc_score(y, y_hat)

    return {
        'accuracy': accuracy,
        'sensitivity': sensitivity,
        'specificity': specificity,
        'precision': precision,
        'f1': f1,
        'auroc': auroc}
