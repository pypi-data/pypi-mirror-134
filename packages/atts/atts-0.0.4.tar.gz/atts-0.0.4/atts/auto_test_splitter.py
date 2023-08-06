import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import xgboost as xgb
from xgboost import cv

class atts:
    """
    Auto Train Test Split
    Auto train test split with adversarial validation. Use it to get the without data leakage train-test split.
    Parameters
    ----------
    dataset: ATTS Dataset object
    target: Target name in dataset
    start_point: test_size initial value
    end_point : test_size final value
    increase: test_size increase value
    """
    
    def __init__(self, dataset, target, start_point, end_point, increase):
        self.target = target
        self.dataset = dataset
        self.start_point = start_point
        self.end_point = end_point
        self.increase = increase

    def test_size(self): 
      df_drop = self.dataset.drop(columns=self.target)
      scores = np.arange(self.start_point, self.end_point, self.increase)
      size = np.arange(self.start_point, self.end_point, self.increase)
      i = 0
      for s in size:
              X_train, X_test = train_test_split(df_drop, test_size=s, random_state=42, shuffle=True)
              # select only the numerical features
              X_test  = X_test.select_dtypes(include=['number']).copy()
              X_train = X_train.select_dtypes(include=['number']).copy()

              # drop the target column from the training data
              #X_train = X_train.drop(['Survived'], axis=1)

              # add the train/test labels
              X_train["AV_label"] = 0
              X_test["AV_label"]  = 1

              # make one big dataset
              all_data = pd.concat([X_train, X_test], axis=0, ignore_index=True)

              # shuffle
              all_data_shuffled = all_data.sample(frac=1)

              # create our DMatrix (the XGBoost data structure)
              X = all_data_shuffled.drop(['AV_label'], axis=1)
              y = all_data_shuffled['AV_label']
              XGBdata = xgb.DMatrix(data=X,label=y)

              # our XGBoost parameters
              params = {"objective":"binary:logistic",
                        "eval_metric":"logloss",
                        'learning_rate': 0.05,
                        'max_depth': 5, }

              # perform cross validation with XGBoost
              cross_val_results = cv(dtrain=XGBdata, params=params, 
                                    nfold=5, metrics="auc", 
                                    num_boost_round=200,early_stopping_rounds=20,
                                    as_pandas=True)

              # print out the final result
              scores[i] = (cross_val_results["test-auc-mean"]).tail(1)
              i = i+1

      array = np.asarray(scores)
      idx = (np.abs(array - 0.5)).argmin()
      size[idx]
      # assign data of lists.  
      data = {'AUC_Scores':scores, 'Test_Size':size}  
      
      # Creates pandas DataFrame.  
      plot_df = pd.DataFrame(data) 

      return plot_df

    def auc_size_plot(self, figSize):
      plot_df = self.test_size()
      plot_df.sort_values("AUC_Scores", inplace=True)
      plt.figure(figsize=figSize)
      sns.lineplot(data=plot_df, x="Test_Size", y="AUC_Scores").axhline(y = 0.5,  color = 'w', linestyle = '--')
      plt.axhline(y = 0.5, color = 'r', linestyle = 'dashed')
      return plt.show()