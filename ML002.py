<<<<<<< HEAD
# graficos embebidos
%matplotlib inline

# importando pandas, numpy y matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importando los datasets de sklearn
from sklearn import datasets

boston = datasets.load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['TARGET'] = boston.target
boston_df.head() # estructura de nuestro dataset.
=======
import os
import pandas as pd
import cv2

>>>>>>> 5bf2910f8e3dd35788e3eabddaeae51bd0091be9
