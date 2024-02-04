#!/usr/bin/env python3

# python -c "import segmentation as s; s.test()"
# python -c "import segmentation as s; s.test(thresh=.5,show_plots=True,debug=True)"
#

import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc

# Assuming t_statistic_values and p_values are lists of your t-statistics and p-values
t_statistic_values = [3.006, 3.730, 3.834, 3.751, 3.672, 3.715, 3.846]
p_values = [0.00287, 0.000229, 0.000154, 0.000212, 0.000285, 0.000243, 0.000148]

precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

# Calculate the area under the precision-recall curve
area_under_curve = auc(recall, precision)

# Plot the precision-recall curve
plt.plot(recall, precision, label=f'AUC-PR = {area_under_curve:.2f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()