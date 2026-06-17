MultiClassPredict
=================

A FAIR Machine Learning Framework for Benchmarking, Feature Selection, and Hyperparameter Optimization of Machine Learning Models for 
Multiomics Data in Galaxy

Input
=====
The tool requires following inputs :

- Feature matrix file (required)
  - Tab-separated file.
  - Formatted with features as columns and samples as rows.
  
- Target file (required)
  - Tab-separated file
  - Must contain a column named either: target or Sample_Condition

- Feature counts (k) (required)
  - Comma-separated list of numbers specifying how many top features to evaluate (e.g., 10,50,100).
  
- Number of seeds (n) (default = 2)

- Dataset label (required)
  - A user-defined label for the experiment
  - Used only for storing results (not for modeling logic).
    
- Model type (required)
  - rf (RandomForest)
  - xgb (XGBoost)
  - etc (ExtraTreesClassifier)
  - lgbm (LightGBM)
  - tabpfn (TabPFN model)
    
- Sampling strategy (required)
  - No Sampling
  - Random OverSampling
  - SMOTE
  - Random UnderSampling
  - NearMiss (v1)
  - NearMiss (v2)
  - NearMiss (v3)
    
- Grid Search (optional)
  - Enables hyperparameter optimization
  - Can substantially increase runtime

Output
======
The tool creates following output files : 

  - MultiClass Metric score
    - This is the main output file depicting different classification metric scores.
    - For each seed, feature count (k), class (or class pair), and evaluation type (OvR/OvO), it reports::
      - ROC AUC – class separation ability
      - PR AUC – precision-recall performance
      - Precision
      - Recall
      - F1 Score
      - MCC (balanced classification metric)
    - It also includes Macro averages across all classes.

  - Diagnostic Plots
    - A PNG file showing pairwise class comparisons.
    - For every class pair, it contains:
      - ROC curve
      - Precision–Recall curve
      - Predicted probability histogram
    - This helps visually assess how well the model distinguishes between classes.

  - performance per feature plots
    - This plot answers :
      "How does model performance change as I increase the number of selected features?"
    - A PNG file showing model performance across different numbers of selected features (k).
    - It plots:
      - ROC AUC
      - PR AUC
    - for:
      - One-vs-Rest (OvR)
      - One-vs-One (OvO)
    - This helps identify the optimal number of features and compare performance across classes.
      

        
