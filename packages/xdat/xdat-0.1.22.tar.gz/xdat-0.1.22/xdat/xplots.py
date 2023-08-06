import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from ds_utils.metrics import plot_confusion_matrix as _plot_confusion_matrix, visualize_accuracy_grouped_by_probability
from . import xproblem, xpd


def plot_feature_importances(folds, title=''):
    df = xproblem.calc_feature_importances(folds, flat=True)
    if df is None:
        return

    fis = df.groupby('feature_name')['feature_importance'].mean()
    df = xpd.x_sort_on_lookup(df, 'feature_name', fis, ascending=True)
    sns.catplot(data=df, y='feature_name', x='feature_importance')
    plt.xlim([0, None])
    if title:
        plt.title(title)

    plt.tight_layout()
    plt.show()

    return


def plot_roc_curve(y_true, y_score):
    auc = metrics.roc_auc_score(y_true, y_score)
    fper, tper, thresholds = metrics.roc_curve(y_true, y_score)
    plt.plot(fper, tper, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve (AUC={auc:.3f})')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_confusion_matrix(y_true, y_pred, labels=None):
    labels = labels or sorted(y_true.unique())
    _plot_confusion_matrix(y_true, y_pred, labels=labels)
    plt.tight_layout()
    plt.show()
