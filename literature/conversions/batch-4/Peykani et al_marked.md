---
conversion_metadata:
  converted_at: "2026-07-21T08:08:58Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Peykani et al.pdf"
  source_pdf_sha256: "f11d77d835f9d4689383d37ee7dfdc83d39e7037ab22cc29a1eabb8b112400ff"
  page_count: 29
  markdown_char_count: 203188
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
Evaluation of Cost-Sensitive Learning Models in Forecasting
Business Failure of Capital Market Firms

Pejman Peykani 1,*
Hamidreza Kamyabfar 2

, Moslem Peymany Foroushany 2, Cristina Tanasescu 3

, Mostafa Sargolzaei 2 and

1 Department of Industrial Engineering, Faculty of Engineering, Khatam University, Tehran 1991633357, Iran
2 Department of Finance and Banking, Faculty of Management and Accounting, Allameh Tabataba’i University,

Tehran 1489684511, Iran; m.peymany@atu.ac.ir (M.P.F.); mostafa.sargolzaei@atu.ac.ir (M.S.);
h.kamyabfar@gmail.com (H.K.)
Faculty of Economic Sciences, Lucian Blaga University of Sibiu, 550324 Sibiu, Romania;
cristina.tanasescu@ulbsibiu.ro

3

* Correspondence: p.peykani@khatam.ac.ir or pejman.peykani@yahoo.com

Abstract: Classifying imbalanced data is a well-known challenge in machine learning. One
of the fields inherently affected by imbalanced data is credit datasets in finance. In this
study, to address this challenge, we employed one of the most recent methods developed
for classifying imbalanced data, CorrOV-CSEn. In addition to the original CorrOV-CSEn
approach, which uses AdaBoost as its base learning method, we also applied Multi-Layer
Perceptron (MLP), random forest, gradient boosted trees, XGBoost, and CatBoost. Our
dataset, sourced from the Iran capital market from 2015 to 2022, utilizes the more general
and accurate term business failure instead of default. Model performance was evaluated
using sensitivity, precision, and F1 score, while their overall performance was compared
using the Friedman–Nemenyi test. The results indicate the high effectiveness of all models
in identifying failing businesses (sensitivity), with CatBoost achieving a sensitivity of 0.909
on the test data. However, all models exhibited relatively low precision.

Keywords: business failure forecasting; imbalanced data; cost-sensitive learning; machine
learning; Multi-Layer Perceptron (MLP); random forest; gradient boosted trees; XGBoost;
CatBoost; AdaBoost

MSC: 62M20; 62P05; 62P20; 68T05; 68T10; 90C90; 91B28

1. Introduction

In recent decades, with advancements in ML algorithms and computational tools, their
experts and
application has garnered significant attention among financial
researchers [1–11]. One of the most critical fields in which they have been applied is
risk management, particularly credit risk management. Many studies have used ML mod-
els to identify firms or customers likely to default compared to others. Machine learning
(ML)-based models offer specific advantages. They require fewer assumptions compared
to traditional models and can process a wider range of data. Unlike traditional models,
which typically rely on accounting or market data [12], ML models incorporate a broader
set of factors, such as cash flow, national governance, and capital structure, making them
more effective in credit assessment [13–16].

While their performance often surpasses that of traditional human-based or structural
models, they encounter some challenges [17–19]. One of these challenges is the structure of

Academic Editor: Raymond Lee

Received: 18 December 2024

Revised: 16 January 2025

Accepted: 21 January 2025

Published: 23 January 2025

Citation: Peykani, P.; Peymany

Foroushany, M.; Tanasescu, C.;

Sargolzaei, M.; Kamyabfar, H.

Evaluation of Cost-Sensitive Learning

Models in Forecasting Business Failure

of Capital Market Firms. Mathematics

2025, 13, 368. https://doi.org/

10.3390/math13030368

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Mathematics 2025, 13, 368

https://doi.org/10.3390/math13030368

---

<!-- PAGE 2 -->

Mathematics 2025, 13, 368

2 of 29

datasets [20]. ML models work with data and are regularly developed to handle balanced
data [21], while in many credit datasets, inherent imbalances exist.

This is logical because defaults are rare occurrences. As it is often stated, machine
learning models are typically designed for balanced datasets. However, in credit risk
management, it is crucial to predict defaulters as accurately as possible due to the high
cost of missing a defaulter in a credit system. This is similar to other challenges, such as
disease detection, where misclassifying a member of the minority class is costlier than
misclassifying a member of the majority class [22,23].

In some studies, to address the performance challenges of ML models, the dataset is
balanced by selecting an equal number of defaulters and non-defaulters. However, this
approach is unrealistic and often results in models with high bias due to the artificially
balanced dataset. In other cases, this imbalance has simply been ignored, resulting in
models that achieve high accuracy but exhibit low sensitivity.

Imbalanced data have an impact on the performance of models, although it may
not be visible initially. For instance, in a hypothetical credit dataset, an ML model might
predict both good and bad payers with the same number of incorrect classifications. In
this case, because of the low number of defaulters, the whole number of payers that their
label predicts correctly is high, and, as a result, the machine learning model reached high
accuracy or even a high AUC score.

However, this undermines the model’s ability to identify defaulters effectively because
even a very small portion of non-defaulter firms, which we defined as the number of falsely
labeled firms in ML model performance, can be a vast majority of defaulter firms, and, as a
result, the model exhibits a poor function in finding the defaulter firms.

This issue is particularly evident in metrics like sensitivity, which are based on defining
defaulted borrowers as positive or negative and measure the rate of identifying each data
label category.

As a result, it is important to note that due to the high number of good payers and
their better identification rate, general metrics like accuracy and AUC may appear high
while sensitivity remains low. This discrepancy can lead to credit disasters, especially
considering the high correlation of defaults.

In response to this challenge, several solutions have been proposed. Some solutions
focus on modifying the data distribution by creating artificial instances or reducing certain
instances. The second brunch emphasizes developing new algorithms that are experts on
learning imbalance data. The third category aims to allocate different weights to different
classes. The last category is referred to as cost-sensitive approaches.

Cost-sensitive approaches are constructed based on real-world outcomes. As a matter
of fact, it is inevitable that when a default occurs after credit risk management predicts that
the firm will not default (false positive), it is more expensive than preventing allocating
capital to a firm that is predicted to default although it will not (false negative).

Many cost-sensitive approaches have been introduced in recent years; however, few
of them have been studied to detect defaulter firms. In this essay, we first review research
on imbalanced datasets and the performance of notable studies in credit prediction using
cost-sensitive ML models. Then, we explore the performance of notable papers in credit
prediction using cost-sensitive machine learning models. Finally, we evaluate the perfor-
mance of one of the most recent cost-sensitive models for imbalanced datasets, as proposed
in work by Devi et al. [24], which combines several decision tree-based models for the
first time.

In this paper, for the first time, Devi et al.’s [24] (CorrOV-CSEn) method is used in
business failure prediction. Additionally, we employ one of the state-of-the-art algorithms
introduced in recent years, CatBoost, in conjunction with a cost-sensitive approach. We

---

<!-- PAGE 3 -->

Mathematics 2025, 13, 368

3 of 29

believe that CatBoost’s ability to prevent overfitting is expected to enhance our model’s
performance. Our third contribution is the use of Iranian capital market firms as our dataset.
The Iranian capital market is one of the oldest in the Middle East and recently was described
by Bloomberg as one of the most “unfamiliar” large capital markets in the world [25].

The remainder of this paper is organized as follows: Section 2 provides a brief review
of methods developed to address imbalanced dataset problems and their applications in
credit risk management. Section 3 details the methodology employed in this study. In
Section 4, the case study—focused on business failure in the Iranian capital market—is
analyzed. Section 5 presents the experimental results, discussing the performance of each
machine learning model. Finally, Section 6 concludes the paper with recommendations for
future research.

2. Literature Review

Our literature review is divided into two parts. The first part addresses previous
work on imbalanced datasets, primarily that developed by computer science scholars. The
second part explores the application of these models in finance, with a focus on credit
risk management.

2.1. Imbalance Datasets Solution

Numerous methods have been proposed to address the issue of imbalanced datasets.
These approaches are generally categorized into three types [26]: (A) data-level (or resam-
pling) methods, (B) algorithm-level methods, and C) cost-sensitive learning, respectively.
Data-level (or resampling) methods address imbalanced datasets by modifying the
structure of the data. This can be achieved through under-sampling, oversampling, or
hybrid resampling methods. In under-sampling, only a subset of the majority class is used
of the majority class are trained. Methods such as Tomek links [27], Kubat and Matwin [28],
Japkowicz [29], Neighborhood Cleaning Rule (NCL) [30], Relevant Information-based
Under Sampling (RIUS) [31], Lee & Seo [32], and EUStack [33] are examples of under-
sampling approaches.

Oversampling methods, on the other hand, involve creating additional copies of the
minority class to balance the training set. Solberg and Solberg [34], WK-SMOTE [35],
MAHAKIL [36], GSMOTE-NFM [37], SMOTEFUN [38], SMOTE-tBPSO-SVM [39], and
Approx—SMOTE [40] are examples of such methods.

Hybrid resampling methods usually combine oversampling and under-sampling. The
Synthetic Minority Oversampling Technique (SMOTE), introduced in 2002 by Chawla
et al. [41], is a widely used hybrid resampling approach. Other hybrid resampling methods
include Ling and Li [42], RFMSE [43], RK-SVM [26], SA-CGAN [44], SMOTified-GAN [45],
and Puri & Gupta [46].

Algorithm-level methods focus on developing algorithms specifically designed to
classify imbalanced data. The RUSBoost algorithm [47], Weighted Ensemble with One-Class
Classification with Over sampling and Instance Selection (WECOI) [48], and Lasso-Logistic
Regression Ensemble [49] are examples of these methods.

Cost-Sensitive Learning addresses misclassification by assigning different costs to
errors. In traditional ML models, misclassifications—such as false negatives (FN) and
false positives (FP)—are often treated equally. However, in reality, the consequences
of these errors can vary significantly, especially in domains like credit classification. In
this context, there is a loss function that considers four possible outcomes in a binary
classification problem, such as distinguishing between defaulters and non-defaulters (or

---

<!-- PAGE 4 -->

Mathematics 2025, 13, 368

4 of 29

1 and 0). The matrix below illustrates the cost matrix used in a regular ML algorithm for
credit classification.

(cid:34)

C(1¸1) = 0 C(1¸0) = 1
C(0¸1) = 1 C(0¸0) = 0

(cid:35)

(1)

In the cost matrix, C(i¸j) represents the cost of labeling an instance X, with an actual
value of j as i. When the instance is correctly labeled, there is no cost. However, for both
types of mislabeling (false positives and false negatives), the cost is typically set to 1.

Cost-Sensitive Learning incorporates the loss function through two main approaches:
direct and indirect. In the direct approach, the loss function influences the training process
itself by adjusting the model based on misclassification costs. In the indirect approach, the
loss function is applied after training, either by modifying decision thresholds or using a
Bayesian decision framework to minimize expected costs [50].

In Cost-Sensitive Learning, different misclassification costs are taken into account. In
real-world scenarios, the cost of a false positive (e.g., incorrectly classifying an unhealthy
firm as healthy) can be significantly different from the cost of a false negative. Misclassifica-
tion costs can be assigned using various approaches. As a result, while traditional machine
learning methods focus on minimizing overall misclassification and maximizing accuracy,
Cost-Sensitive Learning methods aim to minimize the total costs associated with different
types of misclassification errors.

One of the most pioneering cost-sensitive methods was ICET, introduced by Turney in
1995 [51]. It was built on genetic algorithms. Other cost-sensitive models based on decision
trees were introduced by Ling et al. [52] and Drummond and Holte [53].

Some cost-sensitive methods use a threshold probability for algorithms, which pro-
duces probabilities for each instance classification, such as MetaCost [54], CostSensitive-
Classifier [55], Cost-sensitive naïve Bayes [56], and Empirical Thresholding [57].

Khan et al. [58] proposed a cost-sensitive method based on the deep Convolutional
Neural Network that focuses on feature selection. They did not alter data distribution.
Unlike previous models, they set class dependent costs automatically during the learning
procedure. The efficiency of their model has been demonstrated in subsequent works [59].
The Cost-sensitive General Vector Machine (CFGVM) was proposed by Feng et al., which
combines feature selection and GVM [60]. Devi et al. [24], combined AdaBoost ensemble
learning with correlation-based oversampling in their proposed model.

2.2. Imbalanced Learning in Finance

Using machine learning methods in credit risk assessment has already been extensively
explored in the literature. However, the vast majority of these studies have not considered
the imbalanced nature of datasets [22]. Among the notable works in utilizing machine
learning tools for predicting defaults, Khandani et al. [61] evaluated machine learning-based
models for predicting credit card default risk. They employed four classifier thresholds
to classify the data, achieving sensitivity values of 65%, 78%, 83%, and 88% for each
threshold, respectively.

Barboza et al. [62] conducted a comprehensive study examining the credit risk of
North American companies from 1985 to 2013. The dataset included 10,000 companies and
aimed to predict defaults one year in advance. They employed various models, including
support vector machines, bagging, boosting, and random forests and compared these to
statistical models such as discriminant analysis, logistic regression, and neural networks.
Their findings indicated that machine learning models outperformed traditional ones in
predicting corporate defaults by up to 10%, as measured by the ROC score. Notably, the
random forest model demonstrated exceptional accuracy, achieving 87%, which surpassed

---

<!-- PAGE 5 -->

Mathematics 2025, 13, 368

5 of 29

other models. However, the sensitivity of the random forest remained in the range of 0.76
to 0.83.

Yildrim [63] conducted a study to develop two models for predicting corporate de-
faults using a sample of 1 million Turkish companies from 2010 to 2018. The study evaluated
logistic regression, decision tree, random forest, and gradient boosted tree models. The
average AUC scores for these models were 0.76, 0.80, 0.82, and 0.82, respectively. How-
ever, the sensitivity of the three tree-based models was notably low, at 0.15, 0.17, and
0.30, respectively.

In a similar study using the same dataset, Peykani et al. [64] employed two machine
learning models—random forest and gradient boosted trees—to predict business failure
in the Iranian capital market. Both models achieved exceptionally high ROC scores of
0.97. However, their sensitivity for defaulted firms was 0.66 for random forest and 0.77 for
gradient boosted trees.

Chen & Ribeiro [65] combined multiple classifiers, including KNN, support vector
machines, and decision trees, using a consensus approach for bankruptcy prediction.
The dataset consisted of 37 French firms, and the ensemble method aimed to improve
the robustness and accuracy of predictions by integrating results from several machine
learning techniques.

Bahnsen et al. [66] presented a cost-sensitive decision tree algorithm designed to ac-
count for the varying costs associated with different instances by incorporating a cost-based
impurity measure. They introduced a new performance metric called “Saving” to evaluate
model performance. This algorithm is tested on various real-world datasets, including
credit card fraud detection and credit scoring. The results indicate that it outperforms other
methods across all datasets, achieving significant cost savings of up to 71 percent compared
to 32 percent for the benchmark while constructing smaller trees that are faster to build,
requiring only one-fifth of the time needed for traditional decision trees.

Zakaryazad and Duman [67] addressed the challenge of imbalanced data by develop-
ing an Artificial Neural Network (ANN) model optimized to maximize profit rather than
traditional accuracy. Their profit-oriented ANN incorporates a customized penalty func-
tion that assigns variable penalties based on the financial impact of correctly or incorrectly
classifying each instance, modifying the typical sum of squared errors (SSE) function to
weigh misclassifications according to each instance’s profit significance. The findings from
datasets in fraud detection and bank marketing indicate that the ANN and Naïve Bayes
classifier outperform other models.

Xia et al. [68] explored peer-to-peer lending datasets using a cost-sensitive weighted
XGBoost approach. Their study examined both financial and non-financial factors, with the
primary evaluation metric being the annualized rate of return (ARR). The model aimed to
enhance loan evaluation by balancing risks and returns for lenders.

Fiore et al. [69] demonstrated that generative adversarial networks (GANs) can be
employed as an alternative resampling technique to enhance credit card fraud modeling.
Notably, early default has received less attention in the literature.

Papouskova and Hajek [70] proposed a two-stage ensemble learning model to evaluate
default risk in consumer credit, particularly in P2P lending. In the first stage, they employed
heterogeneous classification ensemble models to predict whether a P2P loan would default.
In the second stage, they applied heterogeneous regression ensemble models to estimate
the exposure at default for loans that had defaulted. Their findings demonstrated that
the two-stage method outperformed single-stage approaches, with the ensemble method
achieving greater predictive accuracy compared to traditional credit scoring models. They
employed a diverse range of algorithms, including Decision Tree (C4.5), Logistic Regression,
SVM, random forest, and AdaBoost.

---

<!-- PAGE 6 -->

Mathematics 2025, 13, 368

6 of 29

De Bock et al. [71] addressed uncertainty in misclassification costs for business failure
prediction through a heterogeneous ensemble framework. The model incorporated bag-
ging, random forests, and multi-objective optimization and was evaluated on 21 datasets
spanning various industries. The results highlighted the model’s adaptability to scenarios
involving unknown or dynamic misclassification costs.

Hou et al. [72] proposed an innovative approach to addressing imbalanced data in
credit scoring. Recognizing the limitations of traditional static ensemble methods, they
introduced a dynamic ensemble selection (DES) model specifically designed for imbalanced
classification tasks. The model first applied SMOTE (Synthetic Minority Over-Sampling
Technique) to balance the dataset, thereby creating a more effective candidate classifier pool.
Additionally, they integrated DES-MI, a weighting mechanism that prioritizes minority in-
stances during the evaluation of classifier competence. For further refinement, they applied
META-DES for a comprehensive multi-criteria assessment and used DES-KNN to balance
classifier competence with diversity. Testing on 15 imbalanced datasets demonstrated that
the proposed model outperformed other DES approaches in terms of AUC performance.
Moreover, when evaluated on real P2P loan data, it achieved a lower Type I error rate
compared to XGBoost and LightGBM, highlighting its potential for more accurate credit
risk predictions. This model is particularly valuable for applications where false positives
carry significant financial consequences.

Li et al. [73] applied credit scoring tools to identify high-risk borrowers, including
online loan fraudsters. Using ML-LightGBM, they aimed to more effectively identify early
stage defaulters. To enhance prediction accuracy, the authors incorporated a cost-sensitive
framework into the loss function of the classification model. Tested on a dataset of 1.6
million online loans, their method demonstrated that the cost-sensitive ML-LightGBM
approach outperformed previous models in predictive performance, underscoring its
effectiveness for fraud detection and credit scoring.

Barbaglia et al. [74] investigated default behavior in European residential mortgages
leveraging a dataset of 12 million loans across multiple countries. They modeled loan de-
fault as a function of variables such as borrower profiles, loan characteristics, and regional
economic conditions. By comparing cost-sensitive machine learning algorithms with tradi-
tional logistic regression, they demonstrated that machine learning methods significantly
enhanced prediction accuracy. Their models included gradient boosted trees, XGBoost, and
Logistic Regression. They employed both under-sampling and over-sampling techniques.
Gramegna and Giudici [75] evaluated their model on real-world data from Italian small
and medium enterprises, employing XGBoost with an under-sampling approach. Zou
et al. [76] applied XGBoost with a cost matrix to predict business failures in the Chinese
capital market. They utilized a diverse set of 47 financial ratios as features in their dataset.
The model was compared to various other statistical and machine learning models, and the
results indicated that XGBoost with a cost matrix excelled in minimizing Type II errors.

Chi et al. [77] introduced a novel instance-dependent, misclassification cost-sensitive
algorithm for default prediction. The study proposed two classifiers—misclassification
cost-sensitive Logistic Regression (MCSLR) and misclassification cost-sensitive Neural
Network (MCSNN)—and evaluated their performance by minimizing Type I and Type
II errors, thus improving prediction accuracy in financial decision making. Wang and
Chi [78] utilized a cost-sensitive stacking ensemble learning method to predict financial
distress among 3425 Chinese companies from 2000 to 2020. The study employed statistical
tests, including T-tests and Wilcoxon non-parametric tests, to validate the significance of
differences in financial distress predictions, underscoring the effectiveness of the ensemble
method. Table 1. provides a summary of the discussion in this section.

---

<!-- PAGE 7 -->

Mathematics 2025, 13, 368

7 of 29

Table 1. A summary of the studies conducted.

Year

Research

Method of
Imbalanced Data

Machine Learning Model

Dataset

2013

Chen & Ribeiro [65]

Cost-sensitive

KNN
Support Vector Machines
Decision Trees

Bahnsen [79]

Cost-sensitive

Decision Trees

2015

2016

2017

2017

2019

Zakaryazad and
Duman [67]

Cost-sensitive

Xia et al. [68]

Cost-sensitive

Fiore et al. [69]

Resampling

Papouskova and
Hajek [70]

Cost-sensitive

2020

De Bock et al. [71]

Cost-sensitive

2020

2021

Hou et al. [72]

Resampling

Li et al. [73]

Cost-sensitive

2021

Barbaglia et al. [74]

Cost-sensitive

2021

2022

2022

Gramegna and
Giudici [75]
Zou et al. [76]

Resampling

Cost-sensitive

Chi et al. [77]

Cost-sensitive

ANN

XGBoost

GAN
Decision Tree (C4.5) Logistic
regression
SVM
Random forest AdaBoost
Bagging
Random forests
XGBoost
LightGBM
LightGBM
XGBoost
Gradient Boosted tree
Logistic Regression

XGBoost

XGBoost
Logistic Regression
Neural Network

2024

Wang and Chi [78]

Cost-sensitive

Ensemble learning method

2024

Our Research

Cost-sensitive and
Resampling
(CorrOV-CSEn)

Random forest
Gradient Boosted tree
AdaBoost
XGBoost
CatBoost

37 French firms

Credit card transactions and
customer data

Credit card fraud detection

Two real-world P2P lending
datasets
credit card fraud

P2P lending
consumer loans

21 datasets across various
industries

P2P loan

1.6 million online loans

12 million loans

Italian small and medium
enterprises
Chinese capital market

3425 Chinese companies from
2000 to 2020

Iranian capital market firms

3. Methods
3.1. CorrOV-CSEn

In this study, we employed recently introduced Correlation-based Oversampling
Aided Cost-Sensitive Ensemble learning (CorrOV-CSEn) technique. CorrOV-CSEn inte-
grates two complementary approaches for handling imbalanced datasets. First, it applies
correlation-based oversampling to better prepare the dataset. Then, the prepared data are
used in a cost-sensitive ensemble algorithm, specifically Adaboost in some cases, but also
in combination with other ensemble learning methods. The primary goals of CorrOV-CSEn
are to reduce redundant data generation, prevent overfitting, and improve the classification
accuracy of the minority class. Generally, CorrOV-CSEn follows a two-step process, as
detailed below. Figure 1 describes an overview of the CorrOV-CSEn process.

---

<!-- PAGE 8 -->

Mathematics 2025, 13, 368

8 of 29

Figure 1. Overview of the CorrOV-CSEn process.

3.1.1. Correlation-Based Oversampling

This step enhances the performance of traditional oversampling methods like SMOTE
by incorporating correlation information into the process. Specifically, we employ a Linear
Covariance Matrix (LCM) [80] to determine the optimal level of oversampling. The LCM is
calculated using the following equation:

∑ A =

1
|NN(Xa)|

∑

X∈NN(Xa)

(cid:0)Y − Y(cid:1)(cid:0)Y − Y(cid:1)T

(2)

where

•
•
•
•
•

∑ A represents the Linear Covariance Matrix (LCM);
Xa is a minority class instance;
NN(Xa) denotes the k-nearest neighbors (K-NN) of Xa;
Y is the matrix of K-NN instances of Xa;
Y is the centroid of the Y matrix.

The Linear Covariance Matrix (LCM) is utilized in two critical ways:

• Oversampling rate determination: Higher LCM values, particularly among the K-
NN of the same minority class, indicate stronger correlation and guide a higher
oversampling rate. This strategy reduces variance and generates synthetic instances in
regions with higher minority class correlations, especially near borderline instances.
• Oversampling region optimization: For each minority instance, oversampling is per-
formed only if its LCM with respect to the K-NN of the same class label is greater
than its LCM with instances from other classes. This ensures that synthetic data are
generated in the most relevant regions, enhancing both model robustness and the
quality of the generated samples.

3.1.2. Cost-Sensitive Ensemble Learning

After applying correlation-based oversampling, the prepared data are fed into an
ensemble learning framework. While previous studies, such as those by Devi et al. [24],
used AdaBoost [81], this study, in addition to AdaBoost, explores a broader range of ensem-

---

<!-- PAGE 9 -->

Mathematics 2025, 13, 368

9 of 29

ble methods to assess their performance. These methods include Multi-Layer Perceptron
(MLP), random forest [82], gradient boosted trees [83], XGBoost [84], and CatBoost [85].
Each of these ensemble models is adapted to be cost-sensitive, focusing on minimizing
the misclassification costs associated with the minority class, which is crucial for handling
imbalanced datasets. We describe these methods in detail.

Multi-Layer Perceptron (MLP)

The Multi-Layer Perceptron (MLP) [86], a type of feedforward artificial neural network,
is widely used for both classification and regression tasks due to its flexibility and ability to
model complex, non-linear relationships. The MLP consists of multiple layers of neurons,
where each neuron is connected to the neurons in the subsequent layer through weighted
connections. The learning process involves adjusting these weights to minimize prediction
error. The algorithm’s process can be summarized as follows [87]:

1. An MLP consists of an input layer, one or more hidden layers, and an output layer.
Each layer is composed of several neurons (nodes). If the dataset contains M features,
the input layer will have M neurons. The number of neurons in the hidden layers
can be chosen based on the complexity of the task. Each neuron applies a weighted
sum of inputs followed by a non-linear activation function such as ReLU or sigmoid.
Mathematically, the output of a neuron can be expressed as

z =

M
∑
i=1

wixi + b

where wi are the weights of the connections, xi are the input features, and b is the bias
term. The neuron output after applying the activation function f is

a = f (z)

2.

3.

4.

During forward propagation, inputs pass through the network from the input layer to
the output layer. Each hidden layer neuron processes the weighted sum of inputs and
applies the activation function. The final output layer provides predictions, which
can be either Classification or Regression.
The loss function quantifies the error between the predicted output and the actual
target. For regression, the Mean Squared Error (MSE) is often used.
Backpropagation and Weight Update: The gradient of the loss function is calculated
using the chain rule, and weights are updated using gradient descent.

3.2. Random Forest

The random forest algorithm, introduced by Leo Breiman in 2001 [82], is among the
most widely used and accurate machine learning techniques, including applications in
credit risk management [88–91]. It constructs an ensemble of decision trees by drawing
random subsets from the dataset and combines predictions from multiple “weak” models
to create a robust “strong” model. Based on CART (Classification and Regression Trees),
each tree is independently trained on a bootstrapped sample—a random subset chosen
with replacement. The algorithm’s process can be summarized as follows [92]:

1.

Bootstrap Sampling: For each of the T trees in the forest, a random subset of the data
is drawn with replacement. If there are N total samples, then each tree is built from
a subset Dt of N samples drawn randomly with replacement, resulting in different
training sets for each tree:

Dt = {xi, yi} where i ∈ {1, 2, . . . , N}

(3)

---

<!-- PAGE 10 -->

Mathematics 2025, 13, 368

10 of 29

2.

3.

4.

5.

√

Feature Selection: At each node of the decision tree, a random subset of features
is chosen, typically equal to the square root of the total number of features M in
M). This helps reduce the correlation between trees and
classification tasks (i.e.,
improve model variance. For regression, the number of selected features is often M/3.
This features minimizes correlations among the trees [60].
Splitting Criterion: From the selected subset of features at each node, the feature that
best splits the data is chosen using a splitting criterion, often the Gini index or entropy.
For example, the Gini index G for a split can be calculated as

G = 1 − ∑C

i=1 p2

i

(4)

Building the Forest: Each tree is grown to its full depth without pruning, resulting
in a collection of deep, unpruned trees. By default, 500 trees are built, though this
number can be adjusted for specific applications.
Prediction Aggregation: For classification tasks, the final prediction for each data point
is determined by majority voting across all trees. Let ht(x) represent the prediction of
the t − th tree for a data point x. Then, the final prediction H(x) is given by

H(x) = mode{h1(x), h2(x), . . . , hT(x) }

For regression tasks, the final prediction is the average of all tree outputs:

H(x) =

1
T

∑T

t=1 ht(x)

(5)

(6)

Random sampling and feature selection in random forest reduce the variance of
individual trees while minimizing correlations among them, producing an ensemble with
lower variance and higher accuracy. Each tree in the forest is uncorrelated with the others,
enhancing the model’s robustness.

3.3. Gradient Boosted Trees

Gradient boosted trees (GBT), introduced by Friedman in 2000 [83], extend the boosting
concept to decision trees by building a sequence of models that iteratively minimize errors.
Each model focuses on correcting the errors of its predecessor, creating a strong learner
from a series of weak learners. Unlike bagging, which trains independent models on
random subsets of data (as used in random forest), boosting involves sequential training
where each model improves upon the previous one [93].

Boosting operates on the principle that a robust learning model can be constructed
by combining multiple complementary weak models. Unlike bagging [94], boosting does
not divide the dataset into random subsets. Instead, it assigns higher weights to samples
that were misclassified in previous iterations, refining the model step-by-step. This process
continues until the model achieves a desired level of accuracy or the error is minimized [95].
In GBT, the first decision tree T1(x) is trained on the original target values y. Subse-
quent trees are trained on the residuals (errors) of the preceding models to progressively
reduce the remaining error. For example, if y is the target value, the residuals for the first
tree are calculated as

(1)
i = yi − T1(xi)

r

(7)

In each successive step m, a new tree Tm(x) is trained to predict the residuals from the

prior model. The model update process can be summarized as follows:

---

<!-- PAGE 11 -->

Mathematics 2025, 13, 368

11 of 29

1.

Initialize the model: Start with an initial estimate, often taken as the mean value of
the target variable for regression tasks or a single weak classifier for classification.

F0(x) = argminγ ∑N

i=1 L(yi, γ)

(8)

where L is the loss function, such as squared error for regression or log-loss for
classification.
Iterative Model Updates: For each iteration m = 1, 2, . . . , M:

2.

•

Compute the Residuals: Calculate the residuals r
the current model Fm−1(x):

(m)
i

for each sample based on

(m)
i = −

r

∂L(yi, Fm−1(xi))
∂Fm−1(xi)

(9)

•
Fit a New Tree: Train a new decision tree Tm(x) to predict the residuals r
• Update the Model: Add the new tree to the model with a learning rate η (to

.

(m)
i

control the contribution of each tree), yielding an updated model:

Fm(x) = Fm−1(x) + ηTm(x)

(10)

3.

Final Prediction: After M iterations, the final model FM(x) is an ensemble of the
trees, each adjusted to reduce the error from prior steps. For regression, the final
prediction is

ˆY = FM(x) = F0(x) + ∑M

m=1 ηTm(x)

(11)

The sequential nature of boosting, combined with gradient descent optimization,
allows gradient boosted trees to achieve high accuracy and performance on various datasets.
This algorithm is well-known in credit risk prediction [89].

3.4. XGBoost

XGBoost, introduced by Tianqi Chen in 2016 [84], is an optimized implementation of
gradient boosted trees (GBT) designed to be both efficient and scalable. XGBoost enhances
traditional gradient boosting by adding regularization techniques, tree pruning, and ad-
vanced handling of missing data, making it well-suited for high-dimensional datasets [96].
These improvements help XGBoost achieve high predictive accuracy and robustness while
avoiding overfitting [97].

One of the key differentiators of XGBoost from other GBT methods is its use of both L1
(Lasso) and L2 (Ridge) regularization. These regularization terms penalize the complexity
of the model, ensuring that the final model generalizes well even with large datasets:

1.

Objective Function: The objective of XGBoost is to minimize a regularized loss function
that combines the traditional loss function with regularization terms for complexity
control. For T trees, the objective function Obj is defined as

Obj = ∑N

i=1 L(yi, ˆyi) + ∑T

t=1

Ω( ft)

(12)

where

•

L(yi, ˆyi) is the loss function, such as mean squared error for regression or log-loss
for classification;
• Ω( ft) = YT + 1

j is the regularization term with parameters γ and λ,

j=1 w2

2 λ ∑T
controlling the complexity of each tree.

---

<!-- PAGE 12 -->

Mathematics 2025, 13, 368

12 of 29

2.

Tree Structure and Growth: Each tree in XGBoost is built to minimize the residuals
from the previous trees, following the same general structure as GBT. However,
XGBoost introduces a tree-pruning technique, where trees are pruned based on their
impact on the objective function rather than growing to full depth. The max_depth
parameter controls the maximum depth of each tree, preventing the model from
overfitting by limiting tree complexity.

3. Update Process: In each iteration, the algorithm calculates the best tree structure to
minimize the residuals of the previous ensemble. The updates are computed using
second-order gradients (Hessian) of the loss function, making it more efficient. The
model update at each step t is given by

ˆy

(t)
i = ˆy

(t−1)
i

+ η ft(xi)

(13)

where η is the learning rate and ft(xi) is the output of the t − th tree.

4. Handling Missing Data: XGBoost automatically manages missing data by learning
optimal paths for instances with missing values during training. It assigns missing
values to the most suitable branch, improving model accuracy when dealing with
incomplete datasets.
Final Prediction: The final prediction is an aggregation of all trees, represented as

5.

ˆy = F(xi) = ∑T

t=1 ft(xi)

(14)

where xi represents the input features, and ft(xi) is the output from the t − th tree.
For classification, the final output is often determined by applying a softmax function
to convert the aggregated score to class probabilities.

By integrating these innovations, XGBoost achieves a high degree of accuracy and
efficiency, making it particularly effective for complex tasks such as handling imbalanced
datasets and financial failure prediction [88,89,98,99].

3.5. AdaBoost

Adaboost, short for Adaptive Boosting, is an ensemble learning method designed
to create a strong classifier by combining multiple weak classifiers. The core idea behind
Adaboost, like Boosting, is to iteratively adjust the weights of the training samples, placing
greater emphasis on those that were misclassified in previous rounds. This approach
enhances the overall model’s accuracy by forcing each weak classifier to focus more on
challenging cases.

Initially, Adaboost assigns equal weights to all training sample. In each iteration, it
selects the weak classifier that performs best on the current weighted dataset and updates
the sample weights based on its classification results. Misclassified samples receive higher
weights in the next round, while correctly classified samples are assigned lower weights.
This ensures that previously misclassified samples receive more attention in subsequent
rounds, improving the model’s overall accuracy.

The Adaboost process can be formalized as follows [81]:

1.

Initialize sample weights: Each sample i in the training set receives an initial weight:

where N is the number of training samples.

w

(1)
i =

1
N

(15)

---

<!-- PAGE 13 -->

Mathematics 2025, 13, 368

13 of 29

2.

3.

4.

5.

(17)

(19)

Train a weak classifier: In each round t, a weak classifier ht(x) is trained on the
weighted samples, and its error rate ϵt is calculated as

ϵt = ∑N

i=1 w

(t)
i

.1(ht(xi) ̸= yi)

(16)

Calculate the classifier’s weight: The weight of the weak classifier is determined based
on its accuracy:

at = ln

(cid:19)

(cid:18) 1 − ϵt
ϵt

Update sample weights: Sample weights are updated to reflect the classifier’s perfor-
mance, giving more weight to misclassified samples:

w

(t+1)
i

= w

(t)
i

. exp(at.1(ht(xt) ̸= yi))

(18)

Combine weak classifiers: The final strong classifier H(x) is a weighted sum of all
weak classifiers:

H(x) = sign

(cid:16)∑T

i=1 at.ht(x)

(cid:17)

Through these iterations, Adaboost creates a robust ensemble model capable of general-
izing well across various datasets, improving classification accuracy significantly, especially
for imbalanced datasets.

3.6. CatBoost

CatBoost, introduced by Prokhorenkova et al. in 2018 [100], is a powerful and efficient
implementation of gradient boosted trees (GBT) designed to reduce overfitting and im-
prove predictive accuracy, especially with categorical features. The primary innovation in
CatBoost is the use of ordered boosting, a technique developed by Dorogush et al. [101], to
address the target leakage problem that often arises in standard boosting algorithms. This
feature makes CatBoost particularly effective on small- to medium-sized datasets, where
target leakage can significantly impact model performance.

CatBoost offers several unique improvements over traditional GBT methods [85]:

1.

Ordered Boosting to Avoid Target Leakage: In standard GBT, future data points
might unintentionally influence earlier predictions, leading to target leakage. Ordered
boosting solves this by using a permutation-based scheme, ensuring that only past
information influences each iteration. This ordered approach is particularly useful in
datasets where feature-target relationships are complex and dynamic, and it enhances
CatBoost’s accuracy.

2. Handling of Categorical Variables: CatBoost automatically handles categorical fea-
tures without requiring extensive preprocessing. It converts categorical features into
numeric representations through a series of random permutations, using them to
guide the splitting criteria for each decision tree.

3. Objective Function: CatBoost minimizes a regularized loss function similar to other

boosting methods, but with an emphasis on ordered boosting:

Obj = ∑N

i=1 L(yi. ˆyi) + ∑J

j=1

Ω(cid:0) fj

(cid:1))

(20)

where

ˆyi) is the loss function (e.g., cross-entropy or log-loss for classification

(cid:1) is the regularization term for tree complexity, helping to control overfitting.

•

L(yi,
tasks);
• Ω(cid:0) fj

---

<!-- PAGE 14 -->

Mathematics 2025, 13, 368

14 of 29

4.

Tree Structure and Decision Rule: CatBoost uses binary decision trees as base learners.
For each input xi, the decision tree assigns it to one of the leaf regions Rj based on a
series of splits. The function for each tree can be represented as

H(Xi) = ∑J

j=1 Cj.1x∈Rj

(21)

where

•
•
•

H(Xi) represents the decision function for each sample Xi;
Rj is the disjoint region corresponding to each leaf in the tree;
Cj is the predicted output value for region Rj.

5.

Final Prediction: The final prediction is the aggregation of all the trees in the ensemble.
For a dataset with T trees, the final output Z is given by

Z = F(Xi) = ∑T

t=1 ft(Xi)

(22)

6.

where ft(Xi) is the output of the t − th tree for a given input Xi. For classification, the
model often applies a sigmoid or softmax transformation to convert the output into
class probabilities.
Regularization and Overfitting Prevention: CatBoost uses random permutations when
selecting tree splits, which reduces overfitting and enhances model generalization.
This, combined with ordered boosting, allows CatBoost to outperform traditional GBT
methods on many complex tasks.

CatBoost have been applied in several papers in order to financial failure predic-
tion [102,103], in this article, we applied a dost-sensitive approach toward them for the
first time.

By combining correlation-based oversampling with cost-sensitive ensemble learn-
ing, the CorrOV-CSEn approach minimizes overfitting and significantly enhances the
classification accuracy of the minority class compared to traditional methods.

3.7. Business Failure

In our study, we emphasize the concept of business failure rather than terms like
default or bankruptcy. Business failure refers to a situation where a firm faces signif-
icant challenges in continuing its operations. It is a broader concept than default and
bankruptcy. A firm experiencing business failure is likely to default, which may eventually
lead to bankruptcy if it reaches specific legal thresholds and undergoes the legal process
of resolution.

In countries like Iran, where the government plays a significant role in the econ-
omy [104,105] and the operation of major companies, firms are often prevented from
defaulting and declaring bankruptcy in the capital and debt markets. However, the concept
of business failure provides a valuable perspective for assessing credit risk. Business failure
has been examined in other studies, particularly in relation to macroeconomic conditions.
In Iran’s capital market, business failure is closely associated with “Article 141 of the
Amended Commercial Code.” This regulation requires companies that fall under Article
141 to present a detailed recovery plan. The correlation between Article 141 and business
failure is evident in its focus on both financial losses and the proportion of those losses
relative to the company’s capital. A company falling under Article 141 has accumulated
losses that exceed its equity, meaning its assets have dropped below its liabilities, which
signals potential insolvency.

Figure 2 illustrates the percentage of firms in each year that failed under Article 141 as

a proportion of the total number of firms in that year.

---

<!-- PAGE 15 -->

Mathematics 2025, 13, 368

15 of 29

Figure 2. Percentage of firms failing under Article 141 each year from 2015 to 2022.

3.8. Evaluating Methods

In our research, we utilized ratios derived from the elements of the confusion matrix,
which offers valuable insights into the overall performance of the model. The confusion
matrix is commonly used to assess the performance of binary classification models, where
the aim is to differentiate between failed companies (positive class) and healthy companies
(negative class).

(cid:34)

(cid:35)

TP FN
FP TN

(23)

In the confusion matrix, TP or true positive refers to instances that are actually positive
and were correctly identified by the model. TN or true negative indicates instances that
are actually negative and correctly classified. FP or false positive represents instances that
were predicted as positive but are actually negative, while FN or false negative refers to
positive instances incorrectly classified as negative.

Based on the confusion matrix elements, various ratios are introduced to evaluate the
performance of binary classification models. In this research, we used three key ratios:
recall, precision, and F1 score, which will be explained in order of their significance.

Recall or sensitivity, calculated using Formula (3), measures the model’s success in
identifying failed companies. This metric is considered the most important, as a good credit
model should be able to identify all failing companies and prevent misclassifying them
as healthy.

Sensitivity =

TP
TP + FN

(24)

Precision, calculated using Formula 4, evaluates the accuracy of the model in identify-
ing failing companies. In other words, it indicates the likelihood that a company identified
as failing by the model is indeed failing.

Precision =

TP
TP + FP

(25)

F1 score is a metric used to evaluate binary classification models, especially in cases
where there is an imbalance between the positive and negative classes. The F1 score is the
harmonic mean of precision and recall, calculated using the following formula:

F1 Score =

2 ∗ Precision ∗ Sensitivity
Precision + Sensitivity

(26)

---

<!-- PAGE 16 -->

Mathematics 2025, 13, 368

16 of 29

It balances the two metrics, offering a comprehensive measure of a model’s perfor-
mance by considering both how well the model identifies failed companies (recall) and the
accuracy of those predictions (precision). This score is particularly important when both
false positives and false negatives carry significant costs.

3.9. Statistical Significance Test

We use the Friedman–Nemenyi test to detect significant differences among the models.
This approach is commonly employed in research involving machine learning models,
particularly those related to business failure. The Friedman test is suitable for comparing
three or more groups, especially when the assumption of normality is violated. It extends
the Wilcoxon signed-rank test by incorporating an additional assumption of sphericity [106].
The Friedman statistic is calculated as described by Friedman (1937) [107,108]:

X2

F =

12
nk(k + 1)

∑ R2

i − 3n(k + 1)

(27)

where

•
•
•

n is the number of data sets (blocks);
k is the number of models (groups);
R2

i is the sum of ranks for each model.

H0 is that there is no significance difference between the two models that have been
F crosses the critical value, then H0 is rejected. When H0 is rejected, then

compared, and if X2
the Nemenyi test is used.

4. Case Study

The statistical population of the research comprises all companies in the Iranian capital
market from 2015 to 2022. Each instance represents a firm’s annual information, with
instances labeled as either “defaulted” or “healthy.” In Iran’s economy, the government
prohibits large companies from declaring bankruptcy or default. Consequently, similar to
most credit risk research in Iran, default and bankruptcy are defined based on Article 141
of the proposed amendment to a section of the Commercial Code. According to this article,
if a company loses at least half of its capital due to incurred losses, the board of directors
must promptly convene an extraordinary general meeting of shareholders to decide on the
company’s dissolution or survival. Article 141 effectively identifies conditions indicative of
financial distress, and due to the accessibility of this information, it is used by researchers in
the Iranian capital market. The following section reviews the models employed, detailing
the parameters and calculation methods for each model.

We divided our sample into training and test datasets based on the years. Instances
from 2015 to 2021 were considered as training datasets, and instances from 2021 to 2022
were also considered as training datasets.

In this research, as the focus of our investigation involves companies whose shares
are traded in the capital market, we have made efforts to categorize variables into two
main groups: financial statement-based variables and variables related to the company’s
stock price. These variables are considered the most fundamental information available for
companies in the capital market [109].

Barboza et al. [62] conducted one of the most comprehensive studies investigating
the default risk of companies in the North American capital market from 1985 to 2013.
They employed two research approaches to determine their dataset variables. Firstly, they
utilized the variables of the Altman model [110], a fundamental model designed to estimate
the default risk of companies. Secondly, they also incorporated the variables used by
Carton & Hofer [111], which are based on the growth rate of some fundamental company

---

<!-- PAGE 17 -->

Mathematics 2025, 13, 368

17 of 29

variables [62]. Our features are derived from the balance sheet, which is essential in credit
studies [112].

It is essential to mention that the criterion used in this research for default is not the
actual default but the inclusion in Article 141, which is measured based on the ratio of the
retained earnings to the registered capital of the company. One of the variables used by
Altman (variable X2), representing the ratio of retained earnings to registered capital, is
excluded from the dataset variables list. The reason for excluding Altman’s X2 is that the
default criterion in this study already relies on the same ratio, thus avoiding redundancy
and overlapping metrics. Additionally, one of the Carton & Hofer variables, GE, which
measures the growth in the company employee count, was removed due to the lack of
complete and reliable data.

The variables of the training and test datasets are as follows, as shown in Table 2,

considering the aforementioned points.

Table 2. Features of the dataset and their respective formulas.

Variable

X1
X3
X4
X5
OM
GA
GS
CROE
CPB

Formula

Net Working Capital /Total assets
Earnings be f ore interest and taxes /Total assets
Market value o f share ∗ number o f shares /Total debt
Sales /Total assets
Earnings be f ore intrest and taxes /Sales
Total assetst − Total assetst−1/Total assetst
Salest−Salest−1/Salest−1
ROEt−ROEt−1
Price − to − Bookt−Price − to − Bookt−1

Table 3 shows the statistical description of our training and test data. The table
provides a statistical summary of the training and test datasets, detailing key variables (e.g.,
X1, X3, and X4). Metrics such as the mean, standard deviation, minimum, maximum, and
quartiles offer insights into the distribution of each variable. X4 and GS exhibit considerable
variability, with large standard deviations and extreme maximum values. The training set
shows more stability, while the test set includes outliers, particularly for X4 and GS. These
variations could impact the model’s predictive performance and generalizability.

Table 3. Statistical description of our training and test data.

Training Set

count

mean

std

min

25%

50%

75%

max

Test set

count

mean

std

min

X1

2987

0.083

0.682

−16.681

−0.046

0.145

0.341

0.982

X1

1240

0.224

0.365

X3

2987

0.129

0.182

−2.109

0.026

0.106

0.222

0.842

X3

1240

0.192

0.187

X4

2987

19.821

104.381

0.002

1.339

4.532

13.310

4133.761

X4

1240

1407.757

18,561.378

X5

2987

0.724

0.720

OM

2987

−2.688

129.034

GA

2987

0.374

1.536

GS

2987

349.054

19,013.508

CROE

2987

0.698

8.601

CPB

2987

0.057

3.794

−0.192

−6824.769

−0.786

−203.866

−181.728

−112.889

0.219

0.577

1.001

7.780

X5

1240

0.805

0.787

0.061

0.192

0.463

0.038

0.176

0.429

−0.014

−0.266

−0.077

0.257

0.671

0.143

1.505

0.013

0.124

230.176

68.611

1,039,154.000

190.281

125.772

OM

1240

0.463

4.646

GA

1240

0.581

1.882

GS

1240

0.970

11.161

−27.413

CROE

1240

−0.771

4.969

CPB

1240

−0.111

4.079

−99.452

−129.227

−3.494

−0.781

0.001

−0.579

−18.486

−0.637

---

<!-- PAGE 18 -->

Mathematics 2025, 13, 368

18 of 29

Training Set

25%

50%

75%

max

X1

0.057

0.232

0.402

1.000

Table 3. Cont.

X3

0.061

0.179

0.313

0.838

X4

3.283

7.290

16.479

387,142.019

X5

0.271

0.633

1.132

7.467

OM

0.123

0.286

0.622

GA

0.174

0.366

0.612

GS

0.162

0.479

0.828

159.588

44.695

385.756

CROE

−1.218

−0.173

0.425

32.016

CPB

−0.143

−0.013

0.083

47.076

Table 4 presents skewness and kurtosis values for variables in both the training
and test sets. Skewness measures asymmetry, with values near zero indicating symmetric
distributions. Many variables, especially in the training set (e.g., X1: −10.814, OM: −50.328),
show high positive or negative skewness, indicating significant asymmetry.

Table 4. Skewness and Kurtosis values for variables in total datasets.

Skewness

Kurtosis

Training Set

−10.814
−1.193
25.938
2.584
−50.328
32.133
54.653
1.569
5.855

Test Set

−2.181
−0.008
17.379
2.417
32.369
19.269
33.171
−7.078
−24.427

Training Set

199.295
15.695
897.031
12.077
2629.754
1337.749
2986.988
172.100
725.704

Test Set

17.969
0.939
319.686
10.372
1113.145
426.320
1142.797
136.141
826.716

X1
X3
X4
X5
OM
GA
GS
CROE
CPB

Kurtosis measures the “tailedness” of the distribution. High values, such as GS
(2986.988 in the training set), suggest extreme outliers. The test set generally shows lower
kurtosis, indicating more moderate outliers compared to the training set.

Table 5 shows the correlation matrix among features for both the training and test sets.

Table 5. Correlation matrix among features in the training and test datasets.

Training Set

X1

X3

X4

X5

OM

GA

GS

CROE

CPB

Test set

X1

X3

X4

X5

OM

GA

GS

CROE

CPB

X1

1.000

0.529

0.103

0.097

0.255

0.040

−0.004

−0.173

0.008

X1

1.000

0.445

0.127

0.017

−0.001

−0.046

−0.025

−0.029

0.024

X3

0.529

1.000

0.130

0.281

0.173

0.075

−0.015

−0.139

0.016

X3

0.445

1.000

−0.115

0.321

0.026

−0.003

0.112

−0.045

0.042

X4

0.103

0.130

1.000

−0.032

0.005

0.025

−0.003

0.201

0.002

X4

0.127

−0.115

1.000

−0.086

0.009

−0.028

−0.016

0.012

−0.001

X5

0.097

0.281

−0.032

1.000

0.022

−0.018

−0.016

0.003

0.008

X5

0.017

0.321

−0.086

1.000

−0.049

−0.027

0.009

0.054

0.035

OM

0.255

0.173

0.005

0.022

1.000

0.013

0.000

GA

0.040

0.075

0.025

−0.018

0.013

1.000

0.003

−0.013

−0.242

0.001

OM

−0.001

0.026

0.009

−0.049

1.000

−0.007

−0.001

0.004

−0.008

0.005

GA

−0.046

−0.003

−0.028

−0.027

−0.007

1.000

−0.001

−0.606

−0.023

GS

−0.004

−0.015

−0.003

−0.016

0.000

0.003

1.000

−0.001

−0.003

GS

−0.025

0.112

−0.016

0.009

−0.001

−0.001

1.000

−0.007

0.037

CROE

−0.173

−0.139

0.201

0.003

−0.013

−0.242

−0.001

1.000

0.001

CROE

−0.029

−0.045

0.012

0.054

0.004

−0.606

−0.007

1.000

0.005

CPB

0.008

0.016

0.002

0.008

0.001

0.005

−0.003

0.001

1.000

CPB

0.024

0.042

−0.001

0.035

−0.008

−0.023

0.037

0.005

1.000

---

<!-- PAGE 19 -->

Mathematics 2025, 13, 368

19 of 29

5. Experimental Discussion
5.1. Evaluation Among Models

Table 6 shows the results of applying SMOTE and CorrOV-CSEn across different
machine learning methods. We summarize all the results here and highlight the best result
for each aspect among the models in bold.

Table 6. Performance metrics for different machine learning models.

Model

Sensitivity

Precision

F1 Score

CorrOV-CSEn

Multi-Layer Perceptron (MLP)
Random Forest
Gradient Boosting
XGBoost
AdaBoost
CatBoost

Multi-Layer Perceptron (MLP)
Random Forest
Gradient Boosting
XGBoost
AdaBoost
CatBoost

0.841
0.886
0.795
0.795
0.750
0.909

0.841
0.795
0.727
0.772
0.568
0.750

SMOTE

0.327
0.375
0.443
0.393
0.478
0.201

0.327
0.603
0.603
0.554
0.555
0.717

0.471
0.527
0.569
0.526
0.584
0.329

0.471
0.686
0.660
0.645
0.561
0.733

The performance evaluation of the Multi-Layer Perceptron (MLP), random forest,
gradient boosting, XGBoost, AdaBoost, and CatBoost models reveals significant differences
in their classification accuracy.

CorrOV-CSEn Results:

•

•

• Multi-Layer Perceptron (MLP) shows good sensitivity (0.84). However, it struggles
with precision (0.33), meaning a relatively small proportion of the predicted failure
cases are actual failures. This imbalance results in a moderate F1 score of 0.47.
Random forest demonstrates strong sensitivity (0.89), meaning it effectively detects
failure cases. However, it struggles with precision (0.38), indicating that only a
relatively small portion of the firms predicted as failures are actually failures. This
results in a moderate F1 score of (0.53). On the other hand, when using SMOTE, it
records (0.80) for sensitivity and loses much of its success rate for identifying default
firms. However, precision got better ((0.60) and (0.69)).
Gradient boosting offers balanced performance, with a sensitivity of (0.80) and higher
precision (0.44), resulting in an F1 score of (0.57). This indicates better overall handling
of both false positives and false negatives.
XGBoost performs similarly to gradient boosting, with the same sensitivity (0.80) but
slightly lower precision (0.39), resulting in an F1 score of (0.53). While still robust, it is
slightly outperformed by gradient boosting in terms of precision.
AdaBoost has the lowest sensitivity (0.75) but the highest precision (0.48), resulting in
a competitive F1 score of (0.58). This indicates that while its failure predictions are
more accurate, it misses some failure cases.
CatBoost exhibits the highest sensitivity (0.91) but struggles the most with precision
(0.20), leading to the weakest F1 score (0.33). This suggests that while CatBoost is
highly effective at detecting failures, which is our primary objective, it produces more
false positives.
SMOTE Results:

•

•

•

• Multi-Layer Perceptron (MLP) maintains a similar performance pattern. Sensitivity
remains high at 0.84, effectively capturing failure cases, while precision stays relatively
low at 0.33, indicating that many predicted failure cases were not actual failures.

---

<!-- PAGE 20 -->

Mathematics 2025, 13, 368

20 of 29

•

•

•

•

•

Random forest sensitivity drops to 0.80 while precision improves to 0.60, leading
to an F1 score of 0.69. However, the sensitivity reduction indicates some missed
failure cases.
Gradient boosting shows lower sensitivity (0.73) with a slight precision increase (0.60),
resulting in an F1 score of 0.66, suggesting a modest trade-off.
XGBoost sees a minor decrease in sensitivity (0.77) and an increase in precision (0.55),
with an F1 score of 0.65.
AdaBoost under SMOTE shows a significant drop in sensitivity (0.57) with minimal
gain in precision (0.56), reducing its F1 score to 0.56.
CatBoost improves precision (0.72) but its sensitivity remains lower than CorrOV-CSEn,
with an F1 score of 0.73, showing more balanced results but still lower sensitivity.

These findings reveal that CatBoost reached the highest sensitivity, which is followed
by random forest, Multi-Layer Perceptron (MLP), gradient boosting, XGBoost, and Ad-
aBoost. On the other hand, CatBoost and random forest, despite their high sensitivity,
achieve relatively poor precision and overall effectiveness.

When the SMOTE method is used, XGBoost records the highest sensitivity, followed
by random forest, gradient boosting, CatBoost, and AdaBoost. Meanwhile, CatBoost has
the best precision and F1 score.

CatBoost emerges as the strongest model in terms of sensitivity when combined with
CorrOV-CSEn. This is primarily due to the features of CorrOV-CSEn, where the augmented
data are generated based on correlations, leading to less noisy data being fed into the model.
Additionally, the minority class receives more weight automatically, which is essential in
imbalanced datasets. CatBoost, being highly adaptable to weighted data, can effectively
handle the imbalance and emphasize the minority class.

Furthermore, CatBoost uses a gradient boosting framework with decision trees, lever-
aging the powerful combination of categorical feature processing and boosting to handle
the weight distributions more efficiently. For recall specifically, CorrOV-CSEn generates
data that clarifies the boundary between classes, reducing overlap and thus improving
recall. This characteristic is particularly beneficial for models like CatBoost, which are
well-equipped to learn from complex relationships in the data, including those between
features that are more strongly correlated with default cases.

5.2. Significance Differences

For a more detailed comparison of our models, we divided the dataset into four
subsets. The performance across these subsets reveals notable variations, highlighting the
models’ differing strengths and weaknesses in handling imbalanced data. Table 7 describes
the performance of machine learning models across four datasets.

CatBoost achieves high sensitivity, particularly in Dataset-I (1.00) and Dataset-IV (1.00).
It also performs reasonably well in Dataset-II (0.86) and Dataset-III (0.89), indicating its
effectiveness in identifying positive cases. Gradient boosting and XGBoost demonstrate the
highest and most consistent sensitivity across all datasets, both achieving perfect sensitivity
(1.00) in Dataset-I and Dataset-IV. However, they experience moderate drops in Dataset-II
(0.57 and 0.71, respectively) and Dataset-III (0.56 and 0.67, respectively). Random forest
shows varied sensitivity, excelling in Dataset-I (0.95) and Dataset-IV (0.88) but dropping
significantly in Dataset-II (0.71) and Dataset-III (0.67). The performance of Multi-Layer
Perceptron (MLP), similar to random forest, varies significantly, ranging from 0.84 in
Dataset-II to 0.67 in Dataset-IV. AdaBoost struggles more with sensitivity, particularly
in Dataset-II (0.43) and Dataset-III (0.56), though it performs well in Dataset-I (0.80) and
Dataset-IV (0.88).

---

<!-- PAGE 21 -->

Mathematics 2025, 13, 368

21 of 29

Table 7. Performance comparison of machine learning models across four datasets.

Dataset-I

Dataset-II

Model

Sensitivity

Precision

F1 Score

Sensitivity

Precision

F1 Score

Multi-Layer Perceptron (MLP)

Random Forest

Gradient Boosting

XGBoost

AdaBoost

CatBoost

0.693

0.950

1.000

1.000

0.800

1.000

0.455

0.593

0.666

0.606

0.640

0.339

0.550

0.731

0.800

0.755

0.711

0.506

0.844

0.714

0.571

0.714

0.429

0.857

0.371

0.192

0.500

0.385

0.429

0.188

0.516

0.303

0.533

0.500

0.429

0.308

Model

Sensitivity

Precision

F1 Score

Sensitivity

Precision

F1 Score

Dataset-III

Dataset-IV

Multi-Layer Perceptron (MLP)

Random Forest

Gradient
Boosting

XGBoost

AdaBoost

CatBoost

0.773

0.666

0.556

0.667

0.556

0.889

0.370

0.240

0.227

0.300

0.313

0.138

0.500

0.353

0.323

0.414

0.4

0.239

0.670

0.875

1.000

1.000

0.875

1.000

0.451

0.368

0.444

0.333

0.389

0.116

0.540

0.519

0.615

0.500

0.538

0.208

Gradient boosting delivers solid precision across all datasets, particularly in Dataset-I
(0.67) and Dataset-IV (0.44). XGBoost also performs well in terms of precision, especially in
Dataset-I (0.61), but suffers slightly in Dataset-II (0.38) and Dataset-IV (0.33), indicating a
higher number of false positives in these datasets. Multi-Layer Perceptron (MLP) achieves
a more stable performance, with scores ranging from (0.37) to (0.45) across the four datasets.
Random forest shows a wide range of precision, performing strongly in Dataset-I (0.59) but
struggling significantly in Dataset-II (0.19), Dataset-III (0.24), and Dataset-IV (0.37). This
suggests that while random forest captures positive cases well, it is prone to misclassifying
negative cases as positive. CatBoost exhibits the weakest precision across all datasets, with
values of (0.34) in Dataset-I, (0.19) in Dataset-II, (0.14) in Dataset-III, and (0.12) in Dataset-IV,
indicating consistent difficulty in accurately classifying failure cases and a higher rate
of false positives. AdaBoost generally maintains moderate precision, performing best
in Dataset-I (0.64) but falling to (0.43) in Dataset-II, with consistent but lower results in
Dataset-III and Dataset-IV.

Gradient boosting achieves the highest and most consistent F1 scores, particularly in
Dataset-I (0.80) and Dataset-IV (0.62). XGBoost also performs well, especially in Dataset-I
(0.75), with solid F1 scores in Dataset-III (0.41) and Dataset-IV (0.50). However, its F1
score drops slightly in Dataset-II (0.50). Random forest delivers strong performance in
Dataset-I (0.73) and Dataset-IV (0.52), but its lower F1 scores in Dataset-II (0.30) and Dataset-
III (0.35) highlight its susceptibility to imbalanced class distributions, especially where
precision is low. The Multi-Layer Perceptron (MLP) achieves stable performance, with
scores consistently around (0.50). AdaBoost performs moderately well, with peak F1 scores
in Dataset-I (0.71) and Dataset-IV (0.54), but faces challenges in Dataset-II (0.43) and Dataset-
III (0.40). Despite its high sensitivity, CatBoost suffers the most in terms of F1 score due to
poor precision, which may need tuning for scenarios where precision is more critical. Its F1
scores are (0.51) in Dataset-I, (0.31) in Dataset-II, and (0.21) in Dataset-IV.

We also used the Friedman–Nemenyi test to detect significant differences among
the models. Table 8 shows the results of the Friedman–Nemenyi test for each of the
three scores.

---

<!-- PAGE 22 -->

Mathematics 2025, 13, 368

22 of 29

Table 8. Friedman test results for comparisons among machine learning models.

Friedman Test Statistic

p-value

12.00

0.03479

Precision

Random Forest

Multi-Layer
Perceptron (MLP)

Gradient Boosting

XGBoost

AdaBoost

CatBoost

Random Forest

Multi-Layer Perceptron (MLP)

Gradient Boosting

XGBoost

AdaBoost

CatBoost

-

0.854075

0.635776

0.900000

0.635776

0.744925

0.854075

-

0.900000

0.900000

0.900000

0.136905

Sensitivity

0.635776

0.900000

-

0.900000

0.900000

0.052161

0.900000

0.635776

0.744925

0.900000

0.900000

0.136905

0.900000

0.900000

0.052161

-

0.900000

0.410222

0.900000

-

0.052161

0.410222

0.052161

-

Friedman Test Statistic

p-value 1

10.04

0.07413

No significant difference was found by the Friedman test because the p-value is greater than the significance level of 0.05.

Friedman Test Statistic

p-value 2

10.43

0.06396

F1 Score

1,2 No significant difference was found by the Friedman test because the p-value is greater than the significance
level of 0.05.

Since the p-value is less than 0.05, the Friedman test indicates a significant difference

in sensitivity and precision across the models:

•

• AdaBoost vs. CatBoost: This is the only comparison with a significant difference
(p-value = 0.030), showing that CatBoost performs significantly better than AdaBoost
in terms of sensitivity.
Gradient boosting vs. CatBoost, AdaBoost vs. CatBoost, and MLP vs. CatBoost:
All comparisons show significant differences with p-values of 0.030, indicating that
CatBoost has significantly lower precision compared to gradient boosting, AdaBoost,
and MLP.

All other comparisons have p-values above 0.05, indicating no significant differences

in sensitivity and precision between these models.

5.3. Feature Importance

In the final stage, we present the importance of our feature set across the models used.
Figure 3 illustrates the feature importance in our models. It is clear that X1 has the highest
importance in all models expect MLP. This contrasts with other credit risk studies using the
same feature set in the Iranian capital market [64].

---

<!-- PAGE 23 -->

Mathematics 2025, 13, 368

23 of 29

Figure 3. Feature importance in our machine learning models.

---

<!-- PAGE 24 -->

Mathematics 2025, 13, 368

24 of 29

6. Conclusions

In this study, we employed recently introduced cost-sensitive methods to predict
business failures in the Iranian capital market using five decision tree-based algorithms in
addition to MPL. Our findings demonstrate that all models achieved improved sensitivity
scores through this approach, with CatBoost outperforming the others.

While CatBoost showed clear superiority, there remains a tradeoff between extending
credit to a broader range of customers to maximize revenue and minimizing the risk
of default. Future research could focus on developing models that optimize creditor
profits by balancing revenue generation with risk management rather than solely assessing
default risk.

Additionally, other decision tree-based methods, such as Mondrian Forest, could be
explored in this context. In addition to the models evaluated in this study, it is important
to consider the role of hyperparameter optimization in improving model performance.
While our current work focuses on assessing the effectiveness of various decision tree-
based models, incorporating optimization techniques such as grid search or Bayesian
optimization could lead to even better-performing models.

From a data perspective, incorporating new types of data, including sentiment analysis,
textual data, and political indices, could significantly enhance model performance. This is
especially relevant in countries like Iran, where political and economic conditions play a
crucial role in credit risk management.

Our research focused on the Iran capital market, and due to the unique economic and
political challenges facing the Iranian capital market, these findings might not exactly apply
to other industries or nations, although many developing countries face similar challenges,
like extensive governmental administration, challenges related to market efficiency, and
regulatory frameworks and political instability. It is recommended to consider actual
default instead of failure under Article 141 of the Amended Commercial Code.

Further, it is important to notice that the data analysis results may be affected by the
global economic meltdown caused by the pandemic during the window period. Therefore,
in the upcoming research, it is potential to conduct a sensitivity analysis to compare the
results with the exclusion of the COVID-19 period.

Lastly, there is considerable potential in applying these methods to emerging fields,
such as peer-to-peer (P2P) lending platforms, which have been growing rapidly in Iran in
recent years.

Author Contributions: Conceptualization, P.P., M.P.F., C.T., M.S. and H.K.; methodology, P.P., M.P.F.,
C.T., M.S. and H.K.; software, P.P. and H.K.; validation, P.P., M.P.F., C.T. and H.K.; formal analysis, P.P.,
C.T., M.S. and H.K.; investigation, P.P., M.P.F., C.T. and M.S.; resources, P.P., M.P.F., C.T. and M.S.; data
curation, M.P.F., M.S. and H.K.; writing—original draft preparation, P.P. and H.K.; writing—review
and editing, P.P., M.P.F., C.T., M.S. and H.K.; visualization, P.P., M.S. and H.K.; supervision, P.P., M.P.F.,
C.T. and M.S.; project administration, P.P., C.T. and M.P.F. All authors have read and agreed to the
published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: Data are contained within the article.

Acknowledgments: The authors would like to thank the anonymous reviewers and the editor-in-chief
for their constructive comments and suggestions.

Conflicts of Interest: The authors declare no conflicts of interest.

---

<!-- PAGE 25 -->

Mathematics 2025, 13, 368

References

25 of 29

1.

2.

3.

4.

5.

6.

7.

8.

9.

Usmani, S.; Shamsi, J.A. LSTM based stock prediction using weighted and categorized financial news. PLoS ONE 2023, 18,
e0282234. [CrossRef] [PubMed]
Zhang, Z.; Liu, X.; Niu, H. Financial crisis early warning of Chinese listed companies based on MD&A text-linguistic feature
indicators. PLoS ONE 2023, 18, e0291818. [CrossRef]
Jezeie, F.V.; Sadjadi, S.J.; Makui, A. Constrained portfolio optimization with discrete variables: An algorithmic method based on
dynamic programming. PLoS ONE 2022, 17, e0271811. [CrossRef] [PubMed]
Bi, W.; Zhang, Q. Forecasting mergers and acquisitions failure based on partial-sigmoid neural network and feature selec-tion.
PLoS ONE 2021, 16, e0259575. [CrossRef]
Li, M. Financial investment risk prediction under the application of information interaction Firefly Algorithm combined with
Graph Convolutional Network. PLoS ONE 2023, 18, e0291510. [CrossRef]
Dahal, K.R.; Pokhrel, N.R.; Gaire, S.; Mahatara, S.; Joshi, R.P.; Gupta, A.; Banjade, H.R.; Joshi, J. A comparative study on effect of
news sentiment on stock price prediction with deep learning architecture. PLoS ONE 2023, 18, e0284695. [CrossRef] [PubMed]
Javid, I.; Ghazali, R.; Syed, I.; Zulqarnain, M.; Husaini, N.A. Study on the Pakistan stock market using a new stock crisis prediction
method. PLoS ONE 2022, 17, e0275022. [CrossRef]
Cui, Y.; Liu, L. Investor sentiment-aware prediction model for P2P lending indicators based on LSTM. PLoS ONE 2022, 17,
e0262539. [CrossRef]
Zhu, C.; Liu, X.; Chen, D. Prediction of digital transformation of manufacturing industry based on interpretable machine learning.
PLoS ONE 2024, 19, e0299147. [CrossRef] [PubMed]

10. Khan, A.H.; Shah, A.; Ali, A.; Shahid, R.; Zahid, Z.U.; Sharif, M.U.; Jan, T.; Zafar, M.H. A performance comparison of machine
learning models for stock market prediction with novel investment strategy. PLoS ONE 2023, 18, e0286362. [CrossRef] [PubMed]
11. Wei, X.; Ouyang, H.; Liu, M. Stock index trend prediction based on TabNet feature selection and long short-term memory. PLoS

ONE 2022, 17, e0269195. [CrossRef] [PubMed]

12. Tran, T.; Nguyen, N.H.; Le, B.T.; Vu, N.T.; Vo, D.H. Examining financial distress of the Vietnamese listed firms using accounting-

based models. PLoS ONE 2023, 18, e0284451. [CrossRef] [PubMed]

13. Laghari, F.; Ahmed, F.; López García, M.D.L.N. Cash flow management and its effect on firm performance: Empirical ev-idence

on non-financial firms of China. PLoS ONE 2023, 18, e0287135. [CrossRef] [PubMed]

14. Almustafa, H.; Nguyen, Q.K.; Liu, J.; Dang, V.C. The impact of COVID-19 on firm risk and performance in MENA countries:

Does national governance quality matter? PLoS ONE 2023, 18, e0281148. [CrossRef] [PubMed]

15. Tian, X.; Wang, Y.; Kohar, U.H.A. Capital structure, business model innovation, and firm performance: Evidence from Chinese

16.

listed corporate based on system GMM model. PLoS ONE 2024, 19, e0306054. [CrossRef]
Samour, A.; AlGhazali, A.; Gadoiu, M.; Banuta, M. Capital structure and financial performance of China’s energy industry: What
can we infer from COVID-19? PLoS ONE 2024, 19, e0300936.

17. Berloco, C.; Morales, G.D.F.; Frassineti, D.; Greco, G.; Kumarasinghe, H.; Lamieri, M.; Massaro, E.; Miola, A.; Yang, S. Predicting

corporate credit risk: Network contagion via trade credit. PLoS ONE 2021, 16, e0250115. [CrossRef] [PubMed]

18. Hlongwane, R.; Ramaboa, K.K.K.M.; Mongwe, W. Enhancing credit scoring accuracy with a comprehensive evaluation of

alternative data. PLoS ONE 2024, 19, e0303566. [CrossRef] [PubMed]

19. Ma, Z.; Hou, W.; Zhang, D. A credit risk assessment model of borrowers in P2P lending based on BP neural network. PLoS ONE

2021, 16, e0255216. [CrossRef] [PubMed]

20. Wang, H.; Liu, X. Undersampling bankruptcy prediction: Taiwan bankruptcy data. PLoS ONE 2021, 16, e0254030. [CrossRef]

21.

[PubMed]
Japkowicz, N. Learning from imbalanced data sets: A comparison of various strategies. In AAAI Workshop on Learning from
Imbalanced Data Sets; AAAI Press: Menlo Park, CA, USA, 2000.

22. Groccia, M.C.; Guido, R.; Conforti, D.; Pelaia, C.; Armentaro, G.; Toscani, A.F.; Miceli, S.; Succurro, E.; Hribal, M.L.; Sciacqua, A.
Cost-Sensitive Models to Predict Risk of Cardiovascular Events in Patients with Chronic Heart Failure. Information 2023, 14, 542.
[CrossRef]

23. Natha, P.; RajaRajeswari, P. Advancing Skin Cancer Prediction Using Ensemble Models. Computers 2024, 13, 157. [CrossRef]
24. Devi, D.; Biswas, S.K.; Purkayastha, B. Correlation-based Oversampling aided Cost Sensitive Ensemble learning technique for

Treatment of Class Imbalance. J. Exp. Theor. Artif. Intell. 2022, 34, 143–174. [CrossRef]

25. Alloway, B.T.; Weisenthal, J. What’s Been Happening with the Iranian Stock Market; Bloomberg: New York, NY, USA, 2023.
26. Rawat, S.S.; Mishra, A.K. Review of Methods for Handling Class-Imbalanced in Classification Problems.

arXiv 2022,

arXiv:2211.05456.

27. Tomek, I. Two Modifications of CNN. IEEE Trans. Syst. Man Cybern. 1976, 11, 769–772.
28. Kubat, M.; Matwin, S. Addressing the curse of imbalanced data sets: One-sided sampling. In Proceedings of the Fourteenth

International Conference on Machine Learning, Nashville, TN, USA, 8–12 July 1997.

---

<!-- PAGE 26 -->

Mathematics 2025, 13, 368

26 of 29

29.

Japkowicz, N. The class imbalance problem: Significance and strategies. In Proceedings of the International Conference on
Artificial Intelligence, Las Vegas, NV, USA, 26–29 June 2000.

30. Laurikkala, J. Improving identification of difficult small classes by balancing class distribution. In Proceedings of the Artificial
Intelligence in Medicine: 8th Conference on Artificial Intelligence in Medicine in Europe, AIME 2001, Cascais, Portugal, 1–4 July
2001; Proceedings 8. Springer: Berlin/Heidelberg, Germany, 2001.

31. Hoyos-Osorio, J.; Alvarez-Meza, A.; Daza-Santacoloma, G.; Orozco-Gutierrez, A.; Castellanos-Dominguez, G. Relevant informa-

tion undersampling to support imbalanced data classification. Neurocomputing 2021, 436, 136–146. [CrossRef]

32. Lee, W.; Seo, K. Downsampling for Binary Classification with a Highly Imbalanced Dataset Using Active Learning. Big Data Res.

2022, 28, 100314. [CrossRef]

33. Laveti, R.N.; Mane, A.A.; Pal, S.N. Dynamic Stacked Ensemble with Entropy based Undersampling for the Detection of Fraudulent
Transactions. In Proceedings of the 2021 6th International Conference for Convergence in Technology (I2CT), Maharashtra, India,
2–4 April 2021; pp. 1–7.
Solberg, A.S.; Solberg, R. A large-scale evaluation of features for automatic detection of oil spills in ERS SAR images. In
Proceedings of the IGARSS ’96. 1996 International Geoscience and Remote Sensing Symposium, Lincoln, NB, USA, 21–26 May
1996; pp. 1484–1486.

34.

35. Mathew, J.; Pang, C.K.; Luo, M.; Leong, W.H. Classification of Imbalanced Data by Oversampling in Kernel Space of Support

Vector Machines. IEEE Trans. Neural Networks Learn. Syst. 2017, 29, 4065–4076. [CrossRef] [PubMed]

36. Bennin, K.E.; Keung, J.; Phannachitta, P.; Monden, A.; Mensah, S. MAHAKIL: Diversity Based Oversampling Approach to

Alleviate the Class Imbalance Issue in Software Defect Prediction. IEEE Trans. Softw. Eng. 2017, 44, 534–550. [CrossRef]

37. Cheng, K.; Zhang, C.; Yu, H.; Yang, X.; Zou, H.; Gao, S. Grouped SMOTE With Noise Filtering Mechanism for Classifying

Imbalanced Data. IEEE Access 2019, 7, 170668–170681. [CrossRef]

38. Tarawneh, A.S.; Hassanat, A.B.A.; Almohammadi, K.; Chetverikov, D.; Bellinger, C. SMOTEFUNA: Synthetic Minority Over-

Sampling Technique Based on Furthest Neighbour Algorithm. IEEE Access 2020, 8, 59069–59082. [CrossRef]

39. Almomani, I.; Qaddoura, R.; Habib, M.; Alsoghyer, S.; Al Khayer, A.; Aljarah, I.; Faris, H. Android ransomware detection based
on a hybrid evolutionary approach in the context of highly im-balanced data. IEEE Access 2021, 9, 57674–57691. [CrossRef]
Juez-Gil, M.; Arnaiz-González, Á.; Rodríguez, J.J.; López-Nozal, C.; García-Osorio, C. Approx-SMOTE: Fast SMOTE for Big Data
on Apache Spark. Neurocomputing 2021, 464, 432–437. [CrossRef]

40.

41. Chawla, N.V.; Bowyer, K.W.; Hall, L.O.; Kegelmeyer, W.P. SMOTE: Synthetic Minority Over-sampling Technique. J. Artif. Intell.

Res. 2002, 16, 321–357. [CrossRef]

42. Li, C. Data Mining for Direct Marketing: Problems and Solutions; National Library of Canada= Bibliothèque nationale du Canada:

Ottawa, ON, Canada, 2000.

43. Xu, Z.; Shen, D.; Nie, T.; Kou, Y. A hybrid sampling algorithm combining M-SMOTE and ENN based on Random forest for

medical imbalanced data. J. Biomed. Informatics 2020, 107, 103465. [CrossRef]

44. Dong; Xiao, H.; Dong, Y. SA-CGAN: An oversampling method based on single attribute guided conditional GAN for multi-class

45.

imbalanced learning. Neurocomputing 2022, 472, 326–337. [CrossRef]
Sharma, A.; Singh, P.K.; Chandra, R. SMOTified-GAN for Class Imbalanced Pattern Classification Problems. IEEE Access 2022, 10,
30655–30665. [CrossRef]

46. Puri, A.; Gupta, M.K. Improved Hybrid Bag-Boost Ensemble With K-Means-SMOTE–ENN Technique for Handling Noisy Class

47.

Imbalanced Data. Comput. J. 2021, 65, 124–138. [CrossRef]
Seiffert, C.; Khoshgoftaar, T.M.; Van Hulse, J.; Napolitano, A. RUSBoost: A Hybrid Approach to Alleviating Class Imbalance.
IEEE Trans. Syst. Man Cybern. Part A Syst. Hum. 2009, 40, 185–197. [CrossRef]

48. Czarnowski, I. Weighted Ensemble with one-class Classification and Over-sampling and Instance selection (WECOI): An approach

for learning from imbalanced data streams. J. Comput. Sci. 2022, 61, 101614. [CrossRef]

49. Wang, H.; Xu, Q.; Zhou, L. Large Unbalanced Credit Scoring Using Lasso-Logistic Regression Ensemble. PLoS ONE 2015, 10,

e0117844. [CrossRef] [PubMed]

50. Ariza-Garzón, M.-J.; Arroyo, J.; Segovia-Vargas, M.-J.; Caparrini, A. Profit-sensitive machine learning classification with ex-
planations in credit risk: The case of small businesses in peer-to-peer lending. Electron. Commer. Res. Appl. 2024, 67, 101428.
[CrossRef]

51. Turney, P.D. Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm. J. Artif.

Intell. Res. 1994, 2, 369–409. [CrossRef]

52. Ling, C.X.; Yang, Q.; Wang, J.; Zhang, S. Decision trees with minimal costs. In Proceedings of the Twenty-First International

Conference on Machine Learning, Banff, AB, Canada, 4–8 July 2004.

53. Drummond, C.; Holte, R.C. Exploiting the cost (in) sensitivity of decision tree splitting criteria. In Proceedings of the International

Conference on Machine Learning, Stanford, CA, USA, 29 June 29–2 July 2000.

---

<!-- PAGE 27 -->

Mathematics 2025, 13, 368

27 of 29

54. Domingos, P. Metacost: A general method for making classifiers cost-sensitive. In Proceedings of the Fifth ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining, San Diego, CA, USA, 15–18 August 1999.

55. Witten, I.H.; Frank, E. Data mining: Practical machine learning tools and techniques with Java implementations. Acm Sigmod Rec.

2002, 31, 76–77. [CrossRef]

56. Chai, X.; Deng, L.; Yang, Q.; Ling, C.X. Test-cost sensitive naive bayes classification.

In Proceedings of the Fourth IEEE

57.

International Conference on Data Mining (ICDM’04), Brighton, UK, 1–4 November 2004; IEEE: Piscataway, NJ, USA.
Sheng, V.S.; Ling, C.X. Thresholding for making classifiers cost-sensitive. In Proceedings of the Association for the Advancement
of Artificial Intelligence, Boston, MA, USA, 16–20 July 2006.

58. Khan, S.H.; Hayat, M.; Bennamoun, M.; Sohel, F.A.; Togneri, R. Cost-Sensitive Learning of Deep Feature Representations From

Imbalanced Data. IEEE Trans. Neural Netw. Learn. Syst. 2017, 29, 3573–3587. [CrossRef] [PubMed]

59. Lu, H.; Xu, Y.; Ye, M.; Yan, K.; Gao, Z.; Jin, Q. Learning misclassification costs for imbalanced classification on gene expression

60.

data. BMC Bioinform. 2019, 20, 1–10. [CrossRef] [PubMed]
Feng, F.; Li, K.C.; Shen, J.; Zhou, Q.; Yang, X. Using cost-sensitive learning and feature selection algorithms to improve the
performance of imbalanced clas-sification. IEEE Access 2020, 8, 69979–69996. [CrossRef]

61. Khandani, A.E.; Kim, A.J.; Lo, A.W. Consumer credit-risk models via machine-learning algorithms. J. Bank. Financ. 2010, 34,

2767–2787. [CrossRef]

62. Barboza, F.; Kimura, H.; Altman, E. Machine learning models and bankruptcy prediction. Expert Syst. Appl. 2017, 83, 405–417.

[CrossRef]

63. Yıldırım, M.; Okay, F.Y.; Özdemir, S. Big data analytics for default prediction using graph theory. Expert Syst. Appl. 2021, 176,

114840. [CrossRef]

64. Peykani, P.; Sargolzaei, M.; Sanadgol, N.; Takaloo, A.; Kamyabfar, H. The application of structural and machine learning models
to predict the default risk of listed companies in the Iranian capital market. PLoS ONE 2023, 18, e0292081. [CrossRef] [PubMed]
65. Chen, N.; Ribeiro, B. A consensus approach for combining multiple classifiers in cost-sensitive bankruptcy prediction. In
Proceedings of the Adaptive and Natural Computing Algorithms: 11th International Conference, ICANNGA 2013, Lausanne,
Switzerland, 4–6 April 2013; Proceedings 11. Springer: Berlin/Heidelberg, Germany, 2013.

66. Bahnsen, A.C.; Aouada, D.; Ottersten, B. Example-dependent cost-sensitive decision trees. Expert Syst. Appl. 2015, 42, 6609–6619.

[CrossRef]

67. Zakaryazad, A.; Duman, E. A profit-driven Artificial Neural Network (ANN) with applications to fraud detection and direct

marketing. Neurocomputing 2016, 175, 121–131. [CrossRef]

68. Xia, Y.; Liu, C.; Liu, N. Cost-sensitive boosted tree for loan evaluation in peer-to-peer lending. Electron. Commer. Res. Appl. 2017,

69.

24, 30–49. [CrossRef]
Fiore, U.; De Santis, A.; Perla, F.; Zanetti, P.; Palmieri, F. Using generative adversarial networks for improving classification
effectiveness in credit card fraud detection. Inf. Sci. 2017, 479, 448–455. [CrossRef]

70. Papouskova, M.; Hajek, P. Two-stage consumer credit risk modelling using heterogeneous ensemble learning. Decis. Support Syst.

2019, 118, 33–45. [CrossRef]

71. De Bock, K.W.; Coussement, K.; Lessmann, S. Cost-sensitive business failure prediction when misclassification costs are uncertain:

A heterogeneous ensemble selection approach. Eur. J. Oper. Res. 2020, 285, 612–630. [CrossRef]

72. Hou, W.-H.; Wang, X.-K.; Zhang, H.-Y.; Wang, J.-Q.; Li, L. A novel dynamic ensemble selection classifier for an imbalanced data

set: An application for credit risk assessment. Knowl.-Based Syst. 2020, 208, 106462. [CrossRef]

73. Li, Z.; Zhang, J.; Yao, X.; Kou, G. How to identify early defaults in online lending: A cost-sensitive multi-layer learning framework.

Knowl.-Based Syst. 2021, 221, 106963. [CrossRef]

74. Barbaglia, L.; Manzan, S.; Tosetti, E. Forecasting Loan Default in Europe with Machine Learning. J. Financ. Econ. 2021, 21, 569–596.

[CrossRef]

75. Gramegna, A.; Giudici, P. SHAP and LIME: An Evaluation of Discriminative Power in Credit Risk. Front. Artif. Intell. 2021, 4,

752558. [CrossRef]

76. Zou, Y.; Gao, C.; Gao, H. Business Failure Prediction Based on a Cost-Sensitive Extreme Gradient Boosting Machine. IEEE Access

2022, 10, 42623–42639. [CrossRef]

77. Xing, J.; Chi, G.; Pan, A. Instance-dependent misclassification cost-sensitive learning for default prediction. Res. Int. Bus. Financ.

2024, 69, 102265. [CrossRef]

78. Wang, S.; Chi, G. Cost-sensitive stacking ensemble learning for company financial distress prediction. Expert Syst. Appl. 2024, 255,

124525. [CrossRef]

79. Correa Bahnsen, A.; Aouada, D.; Ottersten, B. Ensemble of Example-Dependent Cost-Sensitive Decision Trees. arXiv 2015,

arXiv:1505.04637.

80. Pandove, D.; Rani, R.; Goel, S. Local graph based correlation clustering. Knowl.-Based Syst. 2017, 138, 155–175. [CrossRef]

---

<!-- PAGE 28 -->

Mathematics 2025, 13, 368

28 of 29

81.

Freund, Y.; Schapire, R.E. A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting. J. Comput.
Syst. Sci. 1997, 55, 119–139. [CrossRef]

82. Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5–32. [CrossRef]
Friedman, J.H. Greedy function approximation: A gradient boosting machine. Ann. Stat. 2001, 29, 1189–1232. [CrossRef]
83.
84. Chen, T.; Guestrin, C. XGBoost: A Scalable Tree Boosting System. In Proceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, 13–17 August 2016; Association for Computing
Machinery: San Francisco, Ca, USA; pp. 785–794.

85. Prokhorenkova, L.; Gusev, G.; Vorobev, A.; Dorogush, A.V.; Gulin, A. CatBoost: Unbiased boosting with categorical features. In
Proceedings of the 32nd International Con-ference on Neural Information Processing Systems, Montréal, Canada, 3–8 December
2018; Curran Associates Inc.: Montréal, QC, Canada; pp. 6639–6649.

86. Rumelhart, D.E.; Hinton, G.E.; Williams, R.J. Learning representations by back-propagating errors. Nature 1986, 323, 533–536.

[CrossRef]

87. Kumar, V.; Kedam, N.; Sharma, K.V.; Mehta, D.J.; Caloiero, T. Advanced Machine Learning Techniques to Improve Hydrological

Prediction: A Comparative Analysis of Streamflow Prediction Models. Water 2023, 15, 2572. [CrossRef]

88. Charoenwong, B.; Reddy, P. Using forensic analytics and machine learning to detect bribe payments in regime-switching

environments: Evidence from the India demonetization. PLoS ONE 2022, 17, e0268965. [CrossRef] [PubMed]

89. Nandi, A.K.; Randhawa, K.K.; Chua, H.S.; Seera, M.; Lim, C.P. Credit card fraud detection using a hierarchical behavior-knowledge

space model. PLoS ONE 2022, 17, e0260579. [CrossRef] [PubMed]

90. Carbo-Valverde, S.; Cuadros-Solas, P.; Rodríguez-Fernández, F. A machine learning approach to the digitalization of bank

customers: Evidence from random and causal forests. PLoS ONE 2020, 15, e0240362. [CrossRef]

91. Hlongwane, R.; Ramabao, K.; Mongwe, W. A novel framework for enhancing transparency in credit scoring: Leveraging Shapley

values for interpretable credit scorecards. PLoS ONE 2024, 19, e0308718. [CrossRef]

92. Quach, A.C. A Extensions and Improvements to Random Forests for Classification; Utah State University: Logan, Utah, 2017.
93. Wyrobek, J.; Kluza, K. Efficiency of Gradient Boosting Decision Trees Technique in Polish Companies’ Bankruptcy Prediction.
In Proceedings of the Information Systems Architecture and Technology: Proceedings of 39th International Conference on
Information Systems Architecture and Technology–ISAT 2018: Part III, Wrocław, Poland, 16–18 September 2019; pp. 24–35.
Freund, Y. Boosting a Weak Learning Algorithm by Majority. Inf. Comput. 1995, 121, 256–285. [CrossRef]

94.
95. Breiman, L. Bagging predictors. Mach. Learn. 1996, 24, 123–140. [CrossRef]
96. Lu, M.; Hou, Q.; Qin, S.; Zhou, L.; Hua, D.; Wang, X.; Cheng, L. A Stacking Ensemble Model of Various Machine Learning Models

for Daily Runoff Forecasting. Water 2023, 15, 1265. [CrossRef]

97. Ainan, U.H.; Por, L.Y.; Chen, Y.-L.; Yang, J.; Ku, C.S. Advancing Bankruptcy Forecasting with Hybrid Machine Learning

Techniques: Insights from an Unbalanced Polish Dataset. IEEE Access 2024, 12, 1. [CrossRef]

98. Aiken, J.M.; De Bin, R.; Hjorth-Jensen, M.; Caballero, M.D. Predicting time to graduation at a large enrollment American university.

PLoS ONE 2020, 15, e0242334. [CrossRef] [PubMed]

99. Du, H.; Lv, L.; Wang, H.; Guo, A. A novel method for detecting credit card fraud problems. PLoS ONE 2024, 19, e0294537.

[CrossRef]

100. Jabeur, S.B.; Gharib, C.; Mefteh-Wali, S.; Arfi, W.B. CatBoost model and artificial intelligence techniques for corporate failure

prediction. Technol. Fore-Cast. Soc. Chang. 2021, 166, 120658. [CrossRef]

101. Dorogush, A.V.; Ershov, V.; Gulin, A. CatBoost: Gradient boosting with categorical features support. arXiv 2018, arXiv:1810.11363.
102. Lu, H.; Hu, X. Enhancing Financial Risk Prediction for Listed Companies: A Catboost-Based Ensemble Learning Approach. J.

Knowl. Econ. 2023, 15, 1–17. [CrossRef]

103. Enkhtuya, T.; Kang, D.K. Bankruptcy Prediction with Explainable Artificial Intelligence for Early-Stage Business Models. Int. J.

Internet Broadcast. Commun. 2023, 15, 58–65.

104. Peykani, P.; Sargolzaei, M.; Botshekan, M.H.; Oprean-Stan, C.; Takaloo, A. Optimization of Asset and Liability Management of

Banks with Minimum Possible Changes. Mathematics 2023, 11, 2761. [CrossRef]

105. Peykani, P.; Sargolzaei, M.; Takaloo, A.; Sanadgol, N. Investigating the monetary policy risk channel based on the dynamic
stochastic general equilibrium model: Empirical evidence from Iran. PLoS ONE 2023, 18, e0291934. [CrossRef] [PubMed]
106. Marino, M.J. Chapter 3—Statistical Analysis in Preclinical Biomedical Research. In Research in the Biomedical Sciences; Williams, M.,

Curtis, M.J., Mullane, K., Eds.; Academic Press: Cambridge, MA, USA, 2018; pp. 107–144.

107. Riffenburgh, R.H. Chapter Summaries. In Statistics in Medicine, 2nd ed.; Riffenburgh, R.H., Ed.; Academic Press: Burlington, MA,

USA, 2006; pp. 533–580.

108. Friedman, M. The Use of Ranks to Avoid the Assumption of Normality Implicit in the Analysis of Variance. J. Am. Stat. Assoc.

1937, 32, 675–701. [CrossRef]

109. Hull, J. Machine Learning in Business: An Introduction to the World of Data Science; Amazon Distribution: London, UK, 2020.

---

<!-- PAGE 29 -->

Mathematics 2025, 13, 368

29 of 29

110. Altman, E.I. Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. J. Financ. 1968, 23, 589–609.

[CrossRef]

111. Carton, R.B.; Hofer, C.W. Measuring Organizational Performance: Metrics for Entrepreneurship and Strategic Management Research;

Edward Elgar Publishing: Cheltenham, UK, 2006.

112. Peykani, P.; Sargolzaei, M.; Takaloo, A.; Valizadeh, S. The Effects of Monetary Policy on Macroeconomic Variables through Credit
and Balance Sheet Channels: A Dynamic Stochastic General Equilibrium Approach. Sustainability 2023, 15, 4409. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
Evaluation of Cost-Sensitive Learning Models in Forecasting
Business Failure of Capital Market Firms
PejmanPeykani1,* ,MoslemPeymanyForoushany2,CristinaTanasescu3 ,MostafaSargolzaei2and
HamidrezaKamyabfar2
1 DepartmentofIndustrialEngineering,FacultyofEngineering,KhatamUniversity,Tehran1991633357,Iran
2 DepartmentofFinanceandBanking,FacultyofManagementandAccounting,AllamehTabataba’iUniversity,
Tehran1489684511,Iran;m.peymany@atu.ac.ir(M.P.F.);mostafa.sargolzaei@atu.ac.ir(M.S.);
h.kamyabfar@gmail.com(H.K.)
3 FacultyofEconomicSciences,LucianBlagaUniversityofSibiu,550324Sibiu,Romania;
cristina.tanasescu@ulbsibiu.ro
* Correspondence:p.peykani@khatam.ac.irorpejman.peykani@yahoo.com
Abstract: Classifyingimbalanceddataisawell-knownchallengeinmachinelearning. One
ofthefieldsinherentlyaffectedbyimbalanceddataiscreditdatasetsinfinance. Inthis
study,toaddressthischallenge,weemployedoneofthemostrecentmethodsdeveloped
forclassifyingimbalanceddata,CorrOV-CSEn. InadditiontotheoriginalCorrOV-CSEn
approach,whichusesAdaBoostasitsbaselearningmethod,wealsoappliedMulti-Layer
Perceptron(MLP),randomforest, gradientboostedtrees, XGBoost, andCatBoost. Our
dataset,sourcedfromtheIrancapitalmarketfrom2015to2022,utilizesthemoregeneral
andaccuratetermbusinessfailureinsteadofdefault. Modelperformancewasevaluated
usingsensitivity,precision,andF1score,whiletheiroverallperformancewascompared
usingtheFriedman–Nemenyitest. Theresultsindicatethehigheffectivenessofallmodels
inidentifyingfailingbusinesses(sensitivity),withCatBoostachievingasensitivityof0.909
onthetestdata. However,allmodelsexhibitedrelativelylowprecision.
Keywords: businessfailureforecasting;imbalanceddata;cost-sensitivelearning;machine
learning;Multi-LayerPerceptron(MLP);randomforest;gradientboostedtrees;XGBoost;
CatBoost;AdaBoost
AcademicEditor:RaymondLee
Received:18December2024
MSC:62M20;62P05;62P20;68T05;68T10;90C90;91B28
Revised:16January2025
Accepted:21January2025
Published:23January2025
Citation: Peykani,P.;Peymany 1. Introduction
Foroushany,M.;Tanasescu,C.;
Sargolzaei,M.;Kamyabfar,H. Inrecentdecades,withadvancementsinMLalgorithmsandcomputationaltools,their
EvaluationofCost-SensitiveLearning application has garnered significant attention among financial experts and
ModelsinForecastingBusinessFailure researchers [1–11]. One of the most critical fields in which they have been applied is
ofCapitalMarketFirms.Mathematics
riskmanagement,particularlycreditriskmanagement. ManystudieshaveusedMLmod-
2025,13,368. https://doi.org/
elstoidentifyfirmsorcustomerslikelytodefaultcomparedtoothers. Machinelearning
10.3390/math13030368
(ML)-basedmodelsofferspecificadvantages. Theyrequirefewerassumptionscompared
Copyright:©2025bytheauthors.
totraditionalmodelsandcanprocessawiderrangeofdata. Unliketraditionalmodels,
LicenseeMDPI,Basel,Switzerland.
whichtypicallyrelyonaccountingormarketdata[12],MLmodelsincorporateabroader
Thisarticleisanopenaccessarticle
setoffactors,suchascashflow,nationalgovernance,andcapitalstructure,makingthem
distributedunderthetermsand
conditionsoftheCreativeCommons moreeffectiveincreditassessment[13–16].
Attribution(CCBY)license Whiletheirperformanceoftensurpassesthatoftraditionalhuman-basedorstructural
(https://creativecommons.org/ models,theyencountersomechallenges[17–19]. Oneofthesechallengesisthestructureof
licenses/by/4.0/).
Mathematics2025,13,368 https://doi.org/10.3390/math13030368

Mathematics2025,13,368 2of29
datasets[20]. MLmodelsworkwithdataandareregularlydevelopedtohandlebalanced
data[21],whileinmanycreditdatasets,inherentimbalancesexist.
Thisislogicalbecausedefaultsarerareoccurrences. Asitisoftenstated, machine
learning models are typically designed for balanced datasets. However, in credit risk
management,itiscrucialtopredictdefaultersasaccuratelyaspossibleduetothehigh
costofmissingadefaulterinacreditsystem. Thisissimilartootherchallenges,suchas
disease detection, where misclassifying a member of the minority class is costlier than
misclassifyingamemberofthemajorityclass[22,23].
Insomestudies,toaddresstheperformancechallengesofMLmodels,thedatasetis
balancedbyselectinganequalnumberofdefaultersandnon-defaulters. However,this
approachisunrealisticandoftenresultsinmodelswithhighbiasduetotheartificially
balanced dataset. In other cases, this imbalance has simply been ignored, resulting in
modelsthatachievehighaccuracybutexhibitlowsensitivity.
Imbalanced data have an impact on the performance of models, although it may
notbevisibleinitially. Forinstance,inahypotheticalcreditdataset,anMLmodelmight
predictbothgoodandbadpayerswiththesamenumberofincorrectclassifications. In
thiscase,becauseofthelownumberofdefaulters,thewholenumberofpayersthattheir
labelpredictscorrectlyishigh,and,asaresult,themachinelearningmodelreachedhigh
accuracyorevenahighAUCscore.
However,thisunderminesthemodel’sabilitytoidentifydefaulterseffectivelybecause
evenaverysmallportionofnon-defaulterfirms,whichwedefinedasthenumberoffalsely
labeledfirmsinMLmodelperformance,canbeavastmajorityofdefaulterfirms,and,asa
result,themodelexhibitsapoorfunctioninfindingthedefaulterfirms.
Thisissueisparticularlyevidentinmetricslikesensitivity,whicharebasedondefining
defaultedborrowersaspositiveornegativeandmeasuretherateofidentifyingeachdata
labelcategory.
Asaresult,itisimportanttonotethatduetothehighnumberofgoodpayersand
theirbetteridentificationrate,generalmetricslikeaccuracyandAUCmayappearhigh
while sensitivity remains low. This discrepancy can lead to credit disasters, especially
consideringthehighcorrelationofdefaults.
Inresponsetothischallenge,severalsolutionshavebeenproposed. Somesolutions
focusonmodifyingthedatadistributionbycreatingartificialinstancesorreducingcertain
instances. Thesecondbrunchemphasizesdevelopingnewalgorithmsthatareexpertson
learningimbalancedata. Thethirdcategoryaimstoallocatedifferentweightstodifferent
classes. Thelastcategoryisreferredtoascost-sensitiveapproaches.
Cost-sensitiveapproachesareconstructedbasedonreal-worldoutcomes. Asamatter
offact,itisinevitablethatwhenadefaultoccursaftercreditriskmanagementpredictsthat
thefirmwillnotdefault(falsepositive),itismoreexpensivethanpreventingallocating
capitaltoafirmthatispredictedtodefaultalthoughitwillnot(falsenegative).
Manycost-sensitiveapproacheshavebeenintroducedinrecentyears;however,few
ofthemhavebeenstudiedtodetectdefaulterfirms. Inthisessay,wefirstreviewresearch
onimbalanceddatasetsandtheperformanceofnotablestudiesincreditpredictionusing
cost-sensitiveMLmodels. Then,weexploretheperformanceofnotablepapersincredit
predictionusingcost-sensitivemachinelearningmodels. Finally,weevaluatetheperfor-
manceofoneofthemostrecentcost-sensitivemodelsforimbalanceddatasets,asproposed
in work by Devi et al. [24], which combines several decision tree-based models for the
firsttime.
Inthispaper,forthefirsttime,Devietal.’s[24](CorrOV-CSEn)methodisusedin
businessfailureprediction. Additionally,weemployoneofthestate-of-the-artalgorithms
introducedinrecentyears,CatBoost,inconjunctionwithacost-sensitiveapproach. We

Mathematics2025,13,368 3of29
believethatCatBoost’sabilitytopreventoverfittingisexpectedtoenhanceourmodel’s
performance.OurthirdcontributionistheuseofIraniancapitalmarketfirmsasourdataset.
TheIraniancapitalmarketisoneoftheoldestintheMiddleEastandrecentlywasdescribed
byBloombergasoneofthemost“unfamiliar”largecapitalmarketsintheworld[25].
Theremainderofthispaperisorganizedasfollows: Section2providesabriefreview
ofmethodsdevelopedtoaddressimbalanceddatasetproblemsandtheirapplicationsin
credit risk management. Section 3 details the methodology employed in this study. In
Section4, thecasestudy—focusedonbusinessfailureintheIraniancapitalmarket—is
analyzed. Section5presentstheexperimentalresults,discussingtheperformanceofeach
machinelearningmodel. Finally,Section6concludesthepaperwithrecommendationsfor
futureresearch.
2. LiteratureReview
Our literature review is divided into two parts. The first part addresses previous
workonimbalanceddatasets,primarilythatdevelopedbycomputersciencescholars. The
second part explores the application of these models in finance, with a focus on credit
riskmanagement.
2.1. ImbalanceDatasetsSolution
Numerousmethodshavebeenproposedtoaddresstheissueofimbalanceddatasets.
Theseapproachesaregenerallycategorizedintothreetypes[26]: (A)data-level(orresam-
pling)methods,(B)algorithm-levelmethods,andC)cost-sensitivelearning,respectively.
Data-level(orresampling)methodsaddressimbalanceddatasetsbymodifyingthe
structure of the data. This can be achieved through under-sampling, oversampling, or
hybridresamplingmethods. Inunder-sampling,onlyasubsetofthemajorityclassisused
ofthemajorityclassaretrained. MethodssuchasTomeklinks[27],KubatandMatwin[28],
Japkowicz [29], Neighborhood Cleaning Rule (NCL) [30], Relevant Information-based
Under Sampling (RIUS) [31], Lee & Seo [32], and EUStack [33] are examples of under-
samplingapproaches.
Oversamplingmethods,ontheotherhand,involvecreatingadditionalcopiesofthe
minority class to balance the training set. Solberg and Solberg [34], WK-SMOTE [35],
MAHAKIL [36], GSMOTE-NFM [37], SMOTEFUN [38], SMOTE-tBPSO-SVM [39], and
Approx—SMOTE[40]areexamplesofsuchmethods.
Hybridresamplingmethodsusuallycombineoversamplingandunder-sampling. The
Synthetic Minority Oversampling Technique (SMOTE), introduced in 2002 by Chawla
etal.[41],isawidelyusedhybridresamplingapproach. Otherhybridresamplingmethods
includeLingandLi[42],RFMSE[43],RK-SVM[26],SA-CGAN[44],SMOTified-GAN[45],
andPuri&Gupta[46].
Algorithm-level methods focus on developing algorithms specifically designed to
classifyimbalanceddata.TheRUSBoostalgorithm[47],WeightedEnsemblewithOne-Class
ClassificationwithOversamplingandInstanceSelection(WECOI)[48],andLasso-Logistic
RegressionEnsemble[49]areexamplesofthesemethods.
Cost-Sensitive Learning addresses misclassification by assigning different costs to
errors. In traditional ML models, misclassifications—such as false negatives (FN) and
false positives (FP)—are often treated equally. However, in reality, the consequences
oftheseerrorscanvarysignificantly, especiallyindomainslikecreditclassification. In
this context, there is a loss function that considers four possible outcomes in a binary
classificationproblem,suchasdistinguishingbetweendefaultersandnon-defaulters(or

Mathematics2025,13,368 4of29
1and0). ThematrixbelowillustratesthecostmatrixusedinaregularMLalgorithmfor
creditclassification.
(cid:34) (cid:35)
C(1¸1) =0 C(1¸0) =1
(1)
C(0¸1) =1 C(0¸0) =0
Inthecostmatrix,C(i¸j)representsthecostoflabelinganinstanceX,withanactual
valueofjasi. Whentheinstanceiscorrectlylabeled,thereisnocost. However,forboth
typesofmislabeling(falsepositivesandfalsenegatives),thecostistypicallysetto1.
Cost-SensitiveLearningincorporatesthelossfunctionthroughtwomainapproaches:
directandindirect. Inthedirectapproach,thelossfunctioninfluencesthetrainingprocess
itselfbyadjustingthemodelbasedonmisclassificationcosts. Intheindirectapproach,the
lossfunctionisappliedaftertraining,eitherbymodifyingdecisionthresholdsorusinga
Bayesiandecisionframeworktominimizeexpectedcosts[50].
InCost-SensitiveLearning,differentmisclassificationcostsaretakenintoaccount. In
real-worldscenarios,thecostofafalsepositive(e.g.,incorrectlyclassifyinganunhealthy
firmashealthy)canbesignificantlydifferentfromthecostofafalsenegative. Misclassifica-
tioncostscanbeassignedusingvariousapproaches. Asaresult,whiletraditionalmachine
learningmethodsfocusonminimizingoverallmisclassificationandmaximizingaccuracy,
Cost-SensitiveLearningmethodsaimtominimizethetotalcostsassociatedwithdifferent
typesofmisclassificationerrors.
Oneofthemostpioneeringcost-sensitivemethodswasICET,introducedbyTurneyin
1995[51]. Itwasbuiltongeneticalgorithms. Othercost-sensitivemodelsbasedondecision
treeswereintroducedbyLingetal.[52]andDrummondandHolte[53].
Somecost-sensitivemethodsuseathresholdprobabilityforalgorithms,whichpro-
ducesprobabilitiesforeachinstanceclassification,suchasMetaCost[54],CostSensitive-
Classifier[55],Cost-sensitivenaïveBayes[56],andEmpiricalThresholding[57].
Khanetal.[58]proposedacost-sensitivemethodbasedonthedeepConvolutional
Neural Network that focuses on feature selection. They did not alter data distribution.
Unlikepreviousmodels,theysetclassdependentcostsautomaticallyduringthelearning
procedure. Theefficiencyoftheirmodelhasbeendemonstratedinsubsequentworks[59].
TheCost-sensitiveGeneralVectorMachine(CFGVM)wasproposedbyFengetal.,which
combinesfeatureselectionandGVM[60]. Devietal.[24],combinedAdaBoostensemble
learningwithcorrelation-basedoversamplingintheirproposedmodel.
2.2. ImbalancedLearninginFinance
Usingmachinelearningmethodsincreditriskassessmenthasalreadybeenextensively
exploredintheliterature. However,thevastmajorityofthesestudieshavenotconsidered
the imbalanced nature of datasets [22]. Among the notable works in utilizing machine
learningtoolsforpredictingdefaults,Khandanietal.[61]evaluatedmachinelearning-based
modelsforpredictingcreditcarddefaultrisk. Theyemployedfourclassifierthresholds
to classify the data, achieving sensitivity values of 65%, 78%, 83%, and 88% for each
threshold,respectively.
Barboza et al. [62] conducted a comprehensive study examining the credit risk of
NorthAmericancompaniesfrom1985to2013. Thedatasetincluded10,000companiesand
aimedtopredictdefaultsoneyearinadvance. Theyemployedvariousmodels,including
supportvectormachines,bagging,boosting,andrandomforestsandcomparedtheseto
statisticalmodelssuchasdiscriminantanalysis,logisticregression,andneuralnetworks.
Theirfindingsindicatedthatmachinelearningmodelsoutperformedtraditionalonesin
predictingcorporatedefaultsbyupto10%,asmeasuredbytheROCscore. Notably,the
randomforestmodeldemonstratedexceptionalaccuracy,achieving87%,whichsurpassed

Mathematics2025,13,368 5of29
othermodels. However,thesensitivityoftherandomforestremainedintherangeof0.76
to0.83.
Yildrim[63]conductedastudytodeveloptwomodelsforpredictingcorporatede-
faultsusingasampleof1millionTurkishcompaniesfrom2010to2018.Thestudyevaluated
logisticregression,decisiontree,randomforest,andgradientboostedtreemodels. The
averageAUCscoresforthesemodelswere0.76,0.80,0.82,and0.82,respectively. How-
ever, the sensitivity of the three tree-based models was notably low, at 0.15, 0.17, and
0.30,respectively.
Inasimilarstudyusingthesamedataset,Peykanietal.[64]employedtwomachine
learningmodels—randomforestandgradientboostedtrees—topredictbusinessfailure
in the Iranian capital market. Both models achieved exceptionally high ROC scores of
0.97. However,theirsensitivityfordefaultedfirmswas0.66forrandomforestand0.77for
gradientboostedtrees.
Chen&Ribeiro[65]combinedmultipleclassifiers,includingKNN,supportvector
machines, and decision trees, using a consensus approach for bankruptcy prediction.
The dataset consisted of 37 French firms, and the ensemble method aimed to improve
therobustnessandaccuracyofpredictionsbyintegratingresultsfromseveralmachine
learningtechniques.
Bahnsenetal.[66]presentedacost-sensitivedecisiontreealgorithmdesignedtoac-
countforthevaryingcostsassociatedwithdifferentinstancesbyincorporatingacost-based
impuritymeasure. Theyintroducedanewperformancemetriccalled“Saving”toevaluate
modelperformance. Thisalgorithm istestedon variousreal-world datasets, including
creditcardfrauddetectionandcreditscoring. Theresultsindicatethatitoutperformsother
methodsacrossalldatasets,achievingsignificantcostsavingsofupto71percentcompared
to32percentforthebenchmarkwhileconstructingsmallertreesthatarefastertobuild,
requiringonlyone-fifthofthetimeneededfortraditionaldecisiontrees.
ZakaryazadandDuman[67]addressedthechallengeofimbalanceddatabydevelop-
inganArtificialNeuralNetwork(ANN)modeloptimizedtomaximizeprofitratherthan
traditionalaccuracy. Theirprofit-orientedANNincorporatesacustomizedpenaltyfunc-
tionthatassignsvariablepenaltiesbasedonthefinancialimpactofcorrectlyorincorrectly
classifyingeachinstance,modifyingthetypicalsumofsquarederrors(SSE)functionto
weighmisclassificationsaccordingtoeachinstance’sprofitsignificance. Thefindingsfrom
datasetsinfrauddetectionandbankmarketingindicatethattheANNandNaïveBayes
classifieroutperformothermodels.
Xiaetal.[68]exploredpeer-to-peerlendingdatasetsusingacost-sensitiveweighted
XGBoostapproach. Theirstudyexaminedbothfinancialandnon-financialfactors,withthe
primaryevaluationmetricbeingtheannualizedrateofreturn(ARR).Themodelaimedto
enhanceloanevaluationbybalancingrisksandreturnsforlenders.
Fioreetal.[69]demonstratedthatgenerativeadversarialnetworks(GANs)canbe
employedasanalternativeresamplingtechniquetoenhancecreditcardfraudmodeling.
Notably,earlydefaulthasreceivedlessattentionintheliterature.
PapouskovaandHajek[70]proposedatwo-stageensemblelearningmodeltoevaluate
defaultriskinconsumercredit,particularlyinP2Plending.Inthefirststage,theyemployed
heterogeneousclassificationensemblemodelstopredictwhetheraP2Ploanwoulddefault.
Inthesecondstage,theyappliedheterogeneousregressionensemblemodelstoestimate
the exposure at default for loans that had defaulted. Their findings demonstrated that
thetwo-stagemethodoutperformedsingle-stageapproaches,withtheensemblemethod
achievinggreaterpredictiveaccuracycomparedtotraditionalcreditscoringmodels. They
employedadiverserangeofalgorithms,includingDecisionTree(C4.5),LogisticRegression,
SVM,randomforest,andAdaBoost.

Mathematics2025,13,368 6of29
DeBocketal.[71]addresseduncertaintyinmisclassificationcostsforbusinessfailure
predictionthroughaheterogeneousensembleframework. Themodelincorporatedbag-
ging,randomforests,andmulti-objectiveoptimizationandwasevaluatedon21datasets
spanningvariousindustries. Theresultshighlightedthemodel’sadaptabilitytoscenarios
involvingunknownordynamicmisclassificationcosts.
Houetal.[72]proposedaninnovativeapproachtoaddressingimbalanceddatain
creditscoring. Recognizingthelimitationsoftraditionalstaticensemblemethods,they
introducedadynamicensembleselection(DES)modelspecificallydesignedforimbalanced
classificationtasks. ThemodelfirstappliedSMOTE(SyntheticMinorityOver-Sampling
Technique)tobalancethedataset,therebycreatingamoreeffectivecandidateclassifierpool.
Additionally,theyintegratedDES-MI,aweightingmechanismthatprioritizesminorityin-
stancesduringtheevaluationofclassifiercompetence. Forfurtherrefinement,theyapplied
META-DESforacomprehensivemulti-criteriaassessmentandusedDES-KNNtobalance
classifiercompetencewithdiversity. Testingon15imbalanceddatasetsdemonstratedthat
theproposedmodeloutperformedotherDESapproachesintermsofAUCperformance.
Moreover, when evaluated on real P2P loan data, it achieved a lower Type I error rate
comparedtoXGBoostandLightGBM,highlightingitspotentialformoreaccuratecredit
riskpredictions. Thismodelisparticularlyvaluableforapplicationswherefalsepositives
carrysignificantfinancialconsequences.
Lietal.[73]appliedcreditscoringtoolstoidentifyhigh-riskborrowers, including
onlineloanfraudsters. UsingML-LightGBM,theyaimedtomoreeffectivelyidentifyearly
stagedefaulters. Toenhancepredictionaccuracy,theauthorsincorporatedacost-sensitive
framework into the loss function of the classification model. Tested on a dataset of 1.6
million online loans, their method demonstrated that the cost-sensitive ML-LightGBM
approach outperformed previous models in predictive performance, underscoring its
effectivenessforfrauddetectionandcreditscoring.
Barbagliaetal.[74]investigateddefaultbehaviorinEuropeanresidentialmortgages
leveragingadatasetof12millionloansacrossmultiplecountries. Theymodeledloande-
faultasafunctionofvariablessuchasborrowerprofiles,loancharacteristics,andregional
economicconditions. Bycomparingcost-sensitivemachinelearningalgorithmswithtradi-
tionallogisticregression,theydemonstratedthatmachinelearningmethodssignificantly
enhancedpredictionaccuracy. Theirmodelsincludedgradientboostedtrees,XGBoost,and
LogisticRegression. Theyemployedbothunder-samplingandover-samplingtechniques.
GramegnaandGiudici[75]evaluatedtheirmodelonreal-worlddatafromItaliansmall
and medium enterprises, employing XGBoost with an under-sampling approach. Zou
etal.[76]appliedXGBoostwithacostmatrixtopredictbusinessfailuresintheChinese
capitalmarket. Theyutilizedadiversesetof47financialratiosasfeaturesintheirdataset.
Themodelwascomparedtovariousotherstatisticalandmachinelearningmodels,andthe
resultsindicatedthatXGBoostwithacostmatrixexcelledinminimizingTypeIIerrors.
Chietal.[77]introducedanovelinstance-dependent,misclassificationcost-sensitive
algorithmfordefaultprediction. Thestudyproposedtwoclassifiers—misclassification
cost-sensitive Logistic Regression (MCSLR) and misclassification cost-sensitive Neural
Network(MCSNN)—andevaluatedtheirperformancebyminimizingTypeIandType
II errors, thus improving prediction accuracy in financial decision making. Wang and
Chi[78]utilizedacost-sensitivestackingensemblelearningmethodtopredictfinancial
distressamong3425Chinesecompaniesfrom2000to2020. Thestudyemployedstatistical
tests,includingT-testsandWilcoxonnon-parametrictests,tovalidatethesignificanceof
differencesinfinancialdistresspredictions,underscoringtheeffectivenessoftheensemble
method. Table1. providesasummaryofthediscussioninthissection.

Mathematics2025,13,368
7of29
Table1.Asummaryofthestudiesconducted.
Methodof
| Year | Research |     |     | MachineLearningModel |     | Dataset |
| ---- | -------- | --- | --- | -------------------- | --- | ------- |
ImbalancedData
KNN
2013 Chen&Ribeiro[65] Cost-sensitive SupportVectorMachines 37Frenchfirms
DecisionTrees
Creditcardtransactionsand
| 2015 | Bahnsen[79] |     | Cost-sensitive |     | DecisionTrees |     |
| ---- | ----------- | --- | -------------- | --- | ------------- | --- |
customerdata
Zakaryazadand
| 2016 |     |     | Cost-sensitive |     | ANN | Creditcardfrauddetection |
| ---- | --- | --- | -------------- | --- | --- | ------------------------ |
Duman[67]
Tworeal-worldP2Plending
| 2017 | Xiaetal. | [68] | Cost-sensitive |     | XGBoost |     |
| ---- | -------- | ---- | -------------- | --- | ------- | --- |
datasets
| 2017 | Fioreetal. | [69] | Resampling |     | GAN | creditcardfraud |
| ---- | ---------- | ---- | ---------- | --- | --- | --------------- |
DecisionTree(C4.5)Logistic
|      | Papouskovaand |     |                |     | regression | P2Plending    |
| ---- | ------------- | --- | -------------- | --- | ---------- | ------------- |
| 2019 |               |     | Cost-sensitive |     |            |               |
|      | Hajek[70]     |     |                |     | SVM        | consumerloans |
RandomforestAdaBoost
|      |             |      |                |               | Bagging | 21datasetsacrossvarious |
| ---- | ----------- | ---- | -------------- | ------------- | ------- | ----------------------- |
| 2020 | DeBocketal. | [71] | Cost-sensitive |               |         |                         |
|      |             |      |                | Randomforests |         | industries              |
XGBoost
| 2020 | Houetal. | [72] | Resampling |     |     | P2Ploan |
| ---- | -------- | ---- | ---------- | --- | --- | ------- |
LightGBM
2021 Lietal. [73] Cost-sensitive LightGBM 1.6milliononlineloans
XGBoost
2021 Barbagliaetal. [74] Cost-sensitive GradientBoostedtree 12millionloans
LogisticRegression
|      | Gramegnaand |     |            |     |         | Italiansmallandmedium |
| ---- | ----------- | --- | ---------- | --- | ------- | --------------------- |
| 2021 |             |     | Resampling |     | XGBoost |                       |
|      | Giudici[75] |     |            |     |         | enterprises           |
2022 Zouetal. [76] Cost-sensitive XGBoost Chinesecapitalmarket
LogisticRegression
| 2022 | Chietal. | [77] | Cost-sensitive |     |     |     |
| ---- | -------- | ---- | -------------- | --- | --- | --- |
NeuralNetwork
3425Chinesecompaniesfrom
| 2024 | WangandChi[78] |     | Cost-sensitive | Ensemblelearningmethod |     |     |
| ---- | -------------- | --- | -------------- | ---------------------- | --- | --- |
2000to2020
Randomforest
|     |     |     | Cost-sensitiveand | GradientBoostedtree |     |     |
| --- | --- | --- | ----------------- | ------------------- | --- | --- |
2024 OurResearch Resampling AdaBoost Iraniancapitalmarketfirms
|     |     |     | (CorrOV-CSEn) |     | XGBoost |     |
| --- | --- | --- | ------------- | --- | ------- | --- |
CatBoost
3. Methods
|     |     | 3.1. | CorrOV-CSEn |     |     |     |
| --- | --- | ---- | ----------- | --- | --- | --- |
In this study, we employed recently introduced Correlation-based Oversampling
AidedCost-SensitiveEnsemblelearning(CorrOV-CSEn)technique. CorrOV-CSEninte-
gratestwocomplementaryapproachesforhandlingimbalanceddatasets. First,itapplies
correlation-basedoversamplingtobetterpreparethedataset. Then,theprepareddataare
usedinacost-sensitiveensemblealgorithm,specificallyAdaboostinsomecases,butalso
incombinationwithotherensemblelearningmethods. TheprimarygoalsofCorrOV-CSEn
aretoreduceredundantdatageneration,preventoverfitting,andimprovetheclassification
accuracy of the minority class. Generally, CorrOV-CSEn follows a two-step process, as
detailedbelow. Figure1describesanoverviewoftheCorrOV-CSEnprocess.

MMatahtehmemataictisc2s 022052,51, 31,33, 6x8 FOR PEER REVIEW 88 ooff2 929
FiFgiugurere1 .1O. Ovverevrvieiwewo offt htheeC CororrOrOVV-C-CSESnEnp rporcoecsess.s.
3.31..11..1.C Coorrrerelalatitoionn-B-BaasesdedO Ovveresrasmampplilningg
TThhisiss tespteepn heannhcaensctehse ptheerf opremrfaonrcmeaonfctera doift iotrnaadliotivoenrasal mopvleirnsgammpetlhinogd smliketehSoMdsO TliEke
bSyMinOcoTrEp obrya itnincgorcpoorrrealtaintigo ncoirnrfeolramtioanti oinnfoinrtmoathtieonp rinoctoe stsh.eS ppreoccifiescsa.l lSyp,ewceifiecmalplylo, wyae eLminpelaory
Cao vLainrieaanrc eCMovaatrriiaxn(cLeC MMa)t[r8i0x] (tLoCdMet)e r[m80i]n teot hdeetoeprtmiminael ltehvee olopftiomvaelr slaemvepl loinf go.vTehresaLmCpMlinisg.
caTlhcue lLaCteMd uiss icnaglctuhleatfeodll ouwsiinngg tehqeu faotliloonw:ing equation:
∑ A = ∑ | 𝐴 NN =1 ( | X (cid:3015)(cid:3015) a (cid:2869) ( ) (cid:3025) |(cid:3276) ∑ )| ∑ X (cid:3025) ∈ ∈ N (cid:3015) N (cid:3015)( ( (cid:3025) X (cid:3276) a ) ) ((cid:0)𝑌 Y − − 𝑌(cid:3364) Y )(cid:1)((cid:0)𝑌 Y − − 𝑌(cid:3364) Y )(cid:3021) (cid:1) T (2 (2 ) )
where
w•h ere∑𝐴 represents the Linear Covariance Matrix (LCM);
• • ∑𝑋A(cid:3028) riesp ar emsiennotrsitthy eclLaisnse ianrstCanovcea;r ianceMatrix(LCM);
• • X𝑁
a
𝑁is(a𝑋 (cid:3028)m) indoernitoytecsl atshse ikn-sntaeanrcees;t neighbors (K-NN) of 𝑋
(cid:3028)
;
• • N𝑌N (isX t
a
h)ed menatortiexs otfh Ke-kN-Nn einarsetastncneesig ohf b𝑋or(cid:3028)s; (K-NN)ofX
a
;
• • Y𝑌(cid:3364) i sitsh tehme caetnritxrooifdK o-fN thNe iYn mstaatnrciexs. ofX ;
a
• YTihset hLeinceeanrt rCooidvaorfitahneceY Mmaattrriixx .(LCM) is utilized in two critical ways:
• Oversampling rate determination: Higher LCM values, particularly among the K-
TheLinearCovarianceMatrix(LCM)isutilizedintwocriticalways:
NN of the same minority class, indicate stronger correlation and guide a higher over-
• Oversampling rate determination: Higher LCM values, particularly among the K-
sampling rate. This strategy reduces variance and generates synthetic instances in
NN of the same minority class, indicate stronger correlation and guide a higher
regions with higher minority class correlations, especially near borderline instances.
• o O ve v r e sa rs m am pl p in l g in r g a t r e e . g T io h n is o s p tr t a im te i g z y at r i e o d n u : c F e o s r v e a a r c ia h n m ce in a o n r d it g y e i n n e s r t a a t n e c s e s , y o n v t e h r e s t a ic m i p n l s i t n a g n c i e s s p i e n r-
regionswithhigherminorityclasscorrelations,especiallynearborderlineinstances.
formed only if its LCM with respect to the K-NN of the same class label is greater
• Oversamplingregionoptimization: Foreachminorityinstance,oversamplingisper-
than its LCM with instances from other classes. This ensures that synthetic data are
formed only if its LCM with respect to the K-NN of the same class label is greater
generated in the most relevant regions, enhancing both model robustness and the
thanitsLCMwithinstancesfromotherclasses. Thisensuresthatsyntheticdataare
quality of the generated samples.
generated in the most relevant regions, enhancing both model robustness and the
qualityofthegeneratedsamples.
3.1.2. Cost-Sensitive Ensemble Learning
After applying correlation-based oversampling, the prepared data are fed into an en-
3.1.2. Cost-SensitiveEnsembleLearning
semble learning framework. While previous studies, such as those by Devi et al. [24], used
After applying correlation-based oversampling, the prepared data are fed into an
AdaBoost [81], this study, in addition to AdaBoost, explores a broader range of ensemble
ensemblelearningframework. Whilepreviousstudies,suchasthosebyDevietal.[24],
methods to assess their performance. These methods include Multi-Layer Perceptron
usedAdaBoost[81],thisstudy,inadditiontoAdaBoost,exploresabroaderrangeofensem-
(MLP), random forest [82], gradient boosted trees [83], XGBoost [84], and CatBoost [85].
Each of these ensemble models is adapted to be cost-sensitive, focusing on minimizing the

Mathematics2025,13,368 9of29
blemethodstoassesstheirperformance. ThesemethodsincludeMulti-LayerPerceptron
(MLP),randomforest[82],gradientboostedtrees[83],XGBoost[84],andCatBoost[85].
Eachoftheseensemblemodelsisadaptedtobecost-sensitive, focusingonminimizing
themisclassificationcostsassociatedwiththeminorityclass,whichiscrucialforhandling
imbalanceddatasets. Wedescribethesemethodsindetail.
Multi-LayerPerceptron(MLP)
TheMulti-LayerPerceptron(MLP)[86],atypeoffeedforwardartificialneuralnetwork,
iswidelyusedforbothclassificationandregressiontasksduetoitsflexibilityandabilityto
modelcomplex,non-linearrelationships. TheMLPconsistsofmultiplelayersofneurons,
whereeachneuronisconnectedtotheneuronsinthesubsequentlayerthroughweighted
connections. Thelearningprocessinvolvesadjustingtheseweightstominimizeprediction
error. Thealgorithm’sprocesscanbesummarizedasfollows[87]:
1. AnMLPconsistsofaninputlayer,oneormorehiddenlayers,andanoutputlayer.
Eachlayeriscomposedofseveralneurons(nodes). Ifthedatasetcontains Mfeatures,
theinputlayerwillhave Mneurons. Thenumberofneuronsinthehiddenlayers
canbechosenbasedonthecomplexityofthetask. Eachneuronappliesaweighted
sumofinputsfollowedbyanon-linearactivationfunctionsuchasReLUorsigmoid.
Mathematically,theoutputofaneuroncanbeexpressedas
M
∑
z = w x +b
i i
i=1
wherew aretheweightsoftheconnections,x aretheinputfeatures,andbisthebias
i i
term. Theneuronoutputafterapplyingtheactivationfunction f is
a = f(z)
2. Duringforwardpropagation,inputspassthroughthenetworkfromtheinputlayerto
theoutputlayer. Eachhiddenlayerneuronprocessestheweightedsumofinputsand
appliestheactivationfunction. Thefinaloutputlayerprovidespredictions,which
canbeeitherClassificationorRegression.
3. Thelossfunctionquantifiestheerrorbetweenthepredictedoutputandtheactual
target. Forregression,theMeanSquaredError(MSE)isoftenused.
4. BackpropagationandWeightUpdate: Thegradientofthelossfunctioniscalculated
usingthechainrule,andweightsareupdatedusinggradientdescent.
3.2. RandomForest
Therandomforestalgorithm,introducedbyLeoBreimanin2001[82],isamongthe
mostwidelyusedandaccuratemachinelearningtechniques, includingapplicationsin
creditriskmanagement[88–91]. Itconstructsanensembleofdecisiontreesbydrawing
randomsubsetsfromthedatasetandcombinespredictionsfrommultiple“weak”models
tocreatearobust“strong”model. BasedonCART(ClassificationandRegressionTrees),
eachtreeisindependentlytrainedonabootstrappedsample—arandomsubsetchosen
withreplacement. Thealgorithm’sprocesscanbesummarizedasfollows[92]:
1. BootstrapSampling: ForeachoftheTtreesintheforest,arandomsubsetofthedata
isdrawnwithreplacement. IfthereareNtotalsamples,theneachtreeisbuiltfrom
asubsetD ofNsamplesdrawnrandomlywithreplacement,resultingindifferent
t
trainingsetsforeachtree:
D = {x, y }wherei ∈ {1, 2, ..., N} (3)
t i i

Mathematics2025,13,368 10of29
2. Feature Selection: At each node of the decision tree, a random subset of features
is chosen, typically equal to the square root of the total number of features M in
√
classificationtasks(i.e., M). Thishelpsreducethecorrelationbetweentreesand
improvemodelvariance. Forregression,thenumberofselectedfeaturesisoftenM/3.
Thisfeaturesminimizescorrelationsamongthetrees[60].
3. SplittingCriterion: Fromtheselectedsubsetoffeaturesateachnode,thefeaturethat
bestsplitsthedataischosenusingasplittingcriterion,oftentheGiniindexorentropy.
Forexample,theGiniindexGforasplitcanbecalculatedas
G =1− ∑C p2 (4)
i=1 i
4. BuildingtheForest: Eachtreeisgrowntoitsfulldepthwithoutpruning,resulting
inacollectionofdeep,unprunedtrees. Bydefault,500treesarebuilt,thoughthis
numbercanbeadjustedforspecificapplications.
5. PredictionAggregation:Forclassificationtasks,thefinalpredictionforeachdatapoint
isdeterminedbymajorityvotingacrossalltrees. Leth (x)representthepredictionof
t
thet−thtreeforadatapointx. Then,thefinalpredictionH(x)isgivenby
H(x) = mode{h (x),h (x),..., h (x)} (5)
1 2 T
Forregressiontasks,thefinalpredictionistheaverageofalltreeoutputs:
1 ∑T
H(x) = h (x) (6)
T t=1 t
Random sampling and feature selection in random forest reduce the variance of
individualtreeswhileminimizingcorrelationsamongthem,producinganensemblewith
lowervarianceandhigheraccuracy. Eachtreeintheforestisuncorrelatedwiththeothers,
enhancingthemodel’srobustness.
3.3. GradientBoostedTrees
Gradientboostedtrees(GBT),introducedbyFriedmanin2000[83],extendtheboosting
concepttodecisiontreesbybuildingasequenceofmodelsthatiterativelyminimizeerrors.
Eachmodelfocusesoncorrectingtheerrorsofitspredecessor,creatingastronglearner
from a series of weak learners. Unlike bagging, which trains independent models on
randomsubsetsofdata(asusedinrandomforest),boostinginvolvessequentialtraining
whereeachmodelimprovesuponthepreviousone[93].
Boostingoperatesontheprinciplethatarobustlearningmodelcanbeconstructed
bycombiningmultiplecomplementaryweakmodels. Unlikebagging[94],boostingdoes
notdividethedatasetintorandomsubsets. Instead,itassignshigherweightstosamples
thatweremisclassifiedinpreviousiterations,refiningthemodelstep-by-step. Thisprocess
continuesuntilthemodelachievesadesiredlevelofaccuracyortheerrorisminimized[95].
InGBT,thefirstdecisiontreeT (x)istrainedontheoriginaltargetvaluesy. Subse-
1
quenttreesaretrainedontheresiduals(errors)oftheprecedingmodelstoprogressively
reducetheremainingerror. Forexample,ifyisthetargetvalue,theresidualsforthefirst
treearecalculatedas
r
(1)
= y −T (x ) (7)
i i 1 i
Ineachsuccessivestepm,anewtreeT (x)istrainedtopredicttheresidualsfromthe
m
priormodel. Themodelupdateprocesscanbesummarizedasfollows:

Mathematics2025,13,368
11of29
1. Initializethemodel: Startwithaninitialestimate,oftentakenasthemeanvalueof
thetargetvariableforregressiontasksorasingleweakclassifierforclassification.
∑N
|     |     | F   | (x) = argmin |     | γ   | L(y | γ)  | (8) |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
|     |     |     | 0            |     | i=1 | i,  |     |     |
where L is the loss function, such as squared error for regression or log-loss for
classification.
|                           |     | Foreachiterationm |     |     | =1, |         | M:  |     |
| ------------------------- | --- | ----------------- | --- | --- | --- | ------- | --- | --- |
| 2. IterativeModelUpdates: |     |                   |     |     |     | 2, ..., |     |     |
(m)
• ComputetheResiduals: Calculatetheresidualsr foreachsamplebasedon
i
| thecurrentmodelF |     |     | (x): |     |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
m−1
|     |     |     | (m) | ∂L(y | i , F | m−1 (x | i )) |     |
| --- | --- | --- | --- | ---- | ----- | ------ | ---- | --- |
|     |     |     | r   | = −  |       |        |      | (9) |
|     |     |     | i   |      | ∂F    | (x )   |      |     |
|     |     |     |     |      | m−1   | i      |      |     |
(m)
• FitaNewTree: TrainanewdecisiontreeT m (x)topredicttheresidualsr .
i
| •   |     |     |     |     |     |     |     | η   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Update the Model: Add the new tree to the model with a learning rate (to
controlthecontributionofeachtree),yieldinganupdatedmodel:
|     |     |     | F (x) | = F | (x)+ηT |     | (x) |      |
| --- | --- | --- | ----- | --- | ------ | --- | --- | ---- |
|     |     |     | m     | m−1 |        | m   |     | (10) |
(x)
3. Final Prediction: After M iterations, the final model F M is an ensemble of the
trees, each adjusted to reduce the error from prior steps. For regression, the final
predictionis
∑M
|     |     | Yˆ = | F (x) = | F (x)+ |     | ηT  | (x) | (11) |
| --- | --- | ---- | ------- | ------ | --- | --- | --- | ---- |
|     |     |      | M       | 0      |     | m=1 | m   |      |
The sequential nature of boosting, combined with gradient descent optimization,
allowsgradientboostedtreestoachievehighaccuracyandperformanceonvariousdatasets.
Thisalgorithmiswell-knownincreditriskprediction[89].
3.4. XGBoost
XGBoost,introducedbyTianqiChenin2016[84],isanoptimizedimplementationof
gradientboostedtrees(GBT)designedtobebothefficientandscalable. XGBoostenhances
traditionalgradientboostingbyaddingregularizationtechniques,treepruning,andad-
vancedhandlingofmissingdata,makingitwell-suitedforhigh-dimensionaldatasets[96].
TheseimprovementshelpXGBoostachievehighpredictiveaccuracyandrobustnesswhile
avoidingoverfitting[97].
OneofthekeydifferentiatorsofXGBoostfromotherGBTmethodsisitsuseofbothL1
(Lasso)andL2(Ridge)regularization. Theseregularizationtermspenalizethecomplexity
ofthemodel,ensuringthatthefinalmodelgeneralizeswellevenwithlargedatasets:
1. ObjectiveFunction:TheobjectiveofXGBoostistominimizearegularizedlossfunction
thatcombinesthetraditionallossfunctionwithregularizationtermsforcomplexity
control. ForTtrees,theobjectivefunctionObjisdefinedas
|     |     |     | = ∑N | L(y, | )+ ∑T | Ω(f | )   |      |
| --- | --- | --- | ---- | ---- | ----- | --- | --- | ---- |
|     |     | Obj |      | i    | yˆ i  |     | t   | (12) |
|     |     |     | i=1  |      |       | t=1 |     |      |
where
• L(y, yˆ )isthelossfunction,suchasmeansquarederrorforregressionorlog-loss
| i   | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
forclassification;
| • Ω(f | ) = YT+ | 1λ∑T | w2                                          |     |     |     |     |     |
| ----- | ------- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- |
| t     |         | j=1  | istheregularizationtermwithparametersγandλ, |     |     |     |     |     |
|       |         | 2    | j                                           |     |     |     |     |     |
controllingthecomplexityofeachtree.

Mathematics2025,13,368 12of29
2. TreeStructureandGrowth: EachtreeinXGBoostisbuilttominimizetheresiduals
from the previous trees, following the same general structure as GBT. However,
XGBoostintroducesatree-pruningtechnique,wheretreesareprunedbasedontheir
impactontheobjectivefunctionratherthangrowingtofulldepth. Themax_depth
parameter controls the maximum depth of each tree, preventing the model from
overfittingbylimitingtreecomplexity.
3. UpdateProcess: Ineachiteration,thealgorithmcalculatesthebesttreestructureto
minimizetheresidualsofthepreviousensemble. Theupdatesarecomputedusing
second-ordergradients(Hessian)ofthelossfunction,makingitmoreefficient. The
modelupdateateachsteptisgivenby
yˆ
(t)
= yˆ
(t−1)
+ηf (x ) (13)
i i t i
whereηisthelearningrateand f (x )istheoutputofthet−thtree.
t i
4. HandlingMissingData: XGBoostautomaticallymanagesmissingdatabylearning
optimalpathsforinstanceswithmissingvaluesduringtraining. Itassignsmissing
valuestothemostsuitablebranch,improvingmodelaccuracywhendealingwith
incompletedatasets.
5. FinalPrediction: Thefinalpredictionisanaggregationofalltrees,representedas
∑T
yˆ = F(x ) = f (x ) (14)
i t=1 t i
where x representstheinputfeatures,and f (x )istheoutputfromthet−thtree.
i t i
Forclassification,thefinaloutputisoftendeterminedbyapplyingasoftmaxfunction
toconverttheaggregatedscoretoclassprobabilities.
Byintegratingtheseinnovations, XGBoostachievesahighdegreeofaccuracyand
efficiency,makingitparticularlyeffectiveforcomplextaskssuchashandlingimbalanced
datasetsandfinancialfailureprediction[88,89,98,99].
3.5. AdaBoost
Adaboost, short for Adaptive Boosting, is an ensemble learning method designed
tocreateastrongclassifierbycombiningmultipleweakclassifiers. Thecoreideabehind
Adaboost,likeBoosting,istoiterativelyadjusttheweightsofthetrainingsamples,placing
greater emphasis on those that were misclassified in previous rounds. This approach
enhancestheoverallmodel’saccuracybyforcingeachweakclassifiertofocusmoreon
challengingcases.
Initially,Adaboostassignsequalweightstoalltrainingsample. Ineachiteration,it
selectstheweakclassifierthatperformsbestonthecurrentweighteddatasetandupdates
thesampleweightsbasedonitsclassificationresults. Misclassifiedsamplesreceivehigher
weightsinthenextround,whilecorrectlyclassifiedsamplesareassignedlowerweights.
Thisensuresthatpreviouslymisclassifiedsamplesreceivemoreattentioninsubsequent
rounds,improvingthemodel’soverallaccuracy.
TheAdaboostprocesscanbeformalizedasfollows[81]:
1. Initializesampleweights: Eachsampleiinthetrainingsetreceivesaninitialweight:
w
(1)
=
1
(15)
i N
whereNisthenumberoftrainingsamples.

Mathematics2025,13,368
13of29
2. Train a weak classifier: In each round t, a weak classifier h (x) is trained on the
t
weightedsamples,anditserrorrateϵ t iscalculatedas
|     | ∑N  | (t)     |          |      |
| --- | --- | ------- | -------- | ---- |
| ϵ = | w   | .1(h (x | ) ̸= y ) | (16) |
| t   | i=1 | i t i   | i        |      |
3. Calculatetheclassifier’sweight:Theweightoftheweakclassifierisdeterminedbased
onitsaccuracy:
|     |     | (cid:18) 1−ϵ (cid:19) |     |     |
| --- | --- | --------------------- | --- | --- |
t
|     | a t =ln |     |     | (17) |
| --- | ------- | --- | --- | ---- |
ϵ
t
4. Updatesampleweights: Sampleweightsareupdatedtoreflecttheclassifier’sperfor-
mance,givingmoreweighttomisclassifiedsamples:
| (t+1) | (t)      |         |           |      |
| ----- | -------- | ------- | --------- | ---- |
| w =   | w .exp(a | .1(h (x | ) ̸= y )) | (18) |
| i     | i        | t t     | t i       |      |
5. Combineweakclassifiers: Thefinalstrongclassifier H(x)isaweightedsumofall
weakclassifiers:
|     |     | (cid:16) | (cid:17) |     |
| --- | --- | -------- | -------- | --- |
∑T
| H(x) | = sign | a .h  | (x) | (19) |
| ---- | ------ | ----- | --- | ---- |
|      |        | i=1 t | t   |      |
Throughtheseiterations,Adaboostcreatesarobustensemblemodelcapableofgeneral-
izingwellacrossvariousdatasets,improvingclassificationaccuracysignificantly,especially
forimbalanceddatasets.
3.6. CatBoost
CatBoost,introducedbyProkhorenkovaetal. in2018[100],isapowerfulandefficient
implementationofgradientboostedtrees(GBT)designedtoreduceoverfittingandim-
provepredictiveaccuracy,especiallywithcategoricalfeatures. Theprimaryinnovationin
CatBoostistheuseoforderedboosting,atechniquedevelopedbyDorogushetal.[101],to
addressthetargetleakageproblemthatoftenarisesinstandardboostingalgorithms. This
featuremakesCatBoostparticularlyeffectiveonsmall-tomedium-sizeddatasets,where
targetleakagecansignificantlyimpactmodelperformance.
CatBoostoffersseveraluniqueimprovementsovertraditionalGBTmethods[85]:
1. Ordered Boosting to Avoid Target Leakage: In standard GBT, future data points
mightunintentionallyinfluenceearlierpredictions,leadingtotargetleakage. Ordered
boostingsolvesthisbyusingapermutation-basedscheme,ensuringthatonlypast
informationinfluenceseachiteration. Thisorderedapproachisparticularlyusefulin
datasetswherefeature-targetrelationshipsarecomplexanddynamic,anditenhances
CatBoost’saccuracy.
2. HandlingofCategoricalVariables: CatBoostautomaticallyhandlescategoricalfea-
tureswithoutrequiringextensivepreprocessing. Itconvertscategoricalfeaturesinto
numeric representations through a series of random permutations, using them to
guidethesplittingcriteriaforeachdecisiontree.
3. ObjectiveFunction: CatBoostminimizesaregularizedlossfunctionsimilartoother
boostingmethods,butwithanemphasisonorderedboosting:
| ∑N    |        | ∑J  | Ω(cid:0) (cid:1) |      |
| ----- | ------ | --- | ---------------- | ---- |
| Obj = | L(y.yˆ | )+  | f )              | (20) |
|       | i=1    | i i | j=1 j            |      |
where
• L(y, yˆ ) is the loss function (e.g., cross-entropy or log-loss for classification
i i
tasks);
Ω(cid:0) (cid:1)
• f istheregularizationtermfortreecomplexity,helpingtocontroloverfitting.
j

Mathematics2025,13,368 14of29
4. TreeStructureandDecisionRule: CatBoostusesbinarydecisiontreesasbaselearners.
Foreachinputx,thedecisiontreeassignsittooneoftheleafregionsR basedona
i j
seriesofsplits. Thefunctionforeachtreecanberepresentedas
∑J
H(X i ) = j=1 C j .1 x∈Rj (21)
where
• H(X)representsthedecisionfunctionforeachsampleX;
i i
• R isthedisjointregioncorrespondingtoeachleafinthetree;
j
• C isthepredictedoutputvalueforregionR .
j j
5. FinalPrediction: Thefinalpredictionistheaggregationofallthetreesintheensemble.
ForadatasetwithTtrees,thefinaloutputZisgivenby
∑T
Z = F(X) = f (X) (22)
i t=1 t i
where f (X)istheoutputofthet−thtreeforagiveninputX. Forclassification,the
t i i
modeloftenappliesasigmoidorsoftmaxtransformationtoconverttheoutputinto
classprobabilities.
6. RegularizationandOverfittingPrevention:CatBoostusesrandompermutationswhen
selectingtreesplits,whichreducesoverfittingandenhancesmodelgeneralization.
This,combinedwithorderedboosting,allowsCatBoosttooutperformtraditionalGBT
methodsonmanycomplextasks.
CatBoost have been applied in several papers in order to financial failure predic-
tion[102,103], inthisarticle, weappliedadost-sensitiveapproachtowardthemforthe
firsttime.
By combining correlation-based oversampling with cost-sensitive ensemble learn-
ing, the CorrOV-CSEn approach minimizes overfitting and significantly enhances the
classificationaccuracyoftheminorityclasscomparedtotraditionalmethods.
3.7. BusinessFailure
In our study, we emphasize the concept of business failure rather than terms like
default or bankruptcy. Business failure refers to a situation where a firm faces signif-
icant challenges in continuing its operations. It is a broader concept than default and
bankruptcy. Afirmexperiencingbusinessfailureislikelytodefault,whichmayeventually
leadtobankruptcyifitreachesspecificlegalthresholdsandundergoesthelegalprocess
ofresolution.
In countries like Iran, where the government plays a significant role in the econ-
omy [104,105] and the operation of major companies, firms are often prevented from
defaultinganddeclaringbankruptcyinthecapitalanddebtmarkets. However,theconcept
ofbusinessfailureprovidesavaluableperspectiveforassessingcreditrisk. Businessfailure
hasbeenexaminedinotherstudies,particularlyinrelationtomacroeconomicconditions.
InIran’scapitalmarket,businessfailureiscloselyassociatedwith“Article141ofthe
AmendedCommercialCode.”ThisregulationrequirescompaniesthatfallunderArticle
141topresentadetailedrecoveryplan. ThecorrelationbetweenArticle141andbusiness
failureisevidentinitsfocusonbothfinanciallossesandtheproportionofthoselosses
relativetothecompany’scapital. AcompanyfallingunderArticle141hasaccumulated
lossesthatexceeditsequity,meaningitsassetshavedroppedbelowitsliabilities,which
signalspotentialinsolvency.
Figure2illustratesthepercentageoffirmsineachyearthatfailedunderArticle141as
aproportionofthetotalnumberoffirmsinthatyear.

Mathematics 2025, 13, x FOR PEER REVIEW 14 of 29
In our study, we emphasize the concept of business failure rather than terms like
default or bankruptcy. Business failure refers to a situation where a firm faces significant
challenges in continuing its operations. It is a broader concept than default and bank-
ruptcy. A firm experiencing business failure is likely to default, which may eventually
lead to bankruptcy if it reaches specific legal thresholds and undergoes the legal process
of resolution.
In countries like Iran, where the government plays a significant role in the economy
[104,105] and the operation of major companies, firms are often prevented from defaulting
and declaring bankruptcy in the capital and debt markets. However, the concept of busi-
ness failure provides a valuable perspective for assessing credit risk. Business failure has
been examined in other studies, particularly in relation to macroeconomic conditions.
In Iran’s capital market, business failure is closely associated with “Article 141 of the
Amended Commercial Code.” This regulation requires companies that fall under Article
141 to present a detailed recovery plan. The correlation between Article 141 and business
failure is evident in its focus on both financial losses and the proportion of those losses
relative to the company’s capital. A company falling under Article 141 has accumulated
losses that exceed its equity, meaning its assets have dropped below its liabilities, which
signals potential insolvency.
Mathematics2025,13,368 Figure 2 illustrates the percentage of firms in each year that failed under Arti1c5leo f12491
as a proportion of the total number of firms in that year.
16
14
12
10
8
6
4
2
0
2015 2016 2017 2018 2019 2020 2021 2022
FFigiguurere2 .2.P Peercrecnentataggeeo offfi firmrmssf afialiilninggu unnddererA Artritcilcele1 41141e aecahchy eyaerarf rformom2 0210515to to2 022022.2.
33.8.8..E EvvaaluluaatitninggM Metehthooddss
InIno ouurrr ereseseaarcrhch,,w weeu utitliilzizeeddr aratitoiossd deerirviveeddf rforommt htheee elelemmeenntstso offt htheec coonnffuussioionnm maattrrixix,,
wwhhicihcho offffeersrsv vaaluluaabblelei ninsisgighhtstsi nintotot htheeo ovverearallllp perefroformrmaannceceo offt htheem mooddele.l.T Thheec oconnfufusisoionn
mmaatrtirxixi sisc coommmmoonnlylyu useseddt otoa asssseesssst htheep peerfroformrmaanncceeo offb bininaaryryc clalassssifiificcaatitoionnm mooddeelsl,s,w whheerere
ththeea iamimis isto tod idffieffreernetniattieatbee btweteweneefna ifleadilecdo mcopmanpiaensi(epso (spitoivsieticvlea scsl)aasns)d ahneda lhtheyalcthoym cpoamnipesa-
(nneiegsa t(inveegcaltaivsse) .class).
(cid:34) (cid:35)
TP FN
FP
(cid:4674)
𝑇𝑃
TN
𝐹𝑁
(cid:4675)
(2(233))
𝐹𝑃 𝑇𝑁
In the confusion matrix, 𝑇𝑃 or true positive refers to instances that are actually pos-
Intheconfusionmatrix,TPortruepositivereferstoinstancesthatareactuallypositive
itive and were correctly identified by the model. 𝑇𝑁 or true negative indicates instances
andwerecorrectlyidentifiedbythemodel. TNortruenegativeindicatesinstancesthat
that are actually negative and correctly classified. 𝐹𝑃 or false positive represents in-
areactuallynegativeandcorrectlyclassified. FPorfalsepositiverepresentsinstancesthat
stances that were predicted as positive but are actually negative, while 𝐹𝑁 or false nega-
werepredictedaspositivebutareactuallynegative,whileFNorfalsenegativerefersto
tive refers to positive instances incorrectly classified as negative.
positiveinstancesincorrectlyclassifiedasnegative.
Basedontheconfusionmatrixelements,variousratiosareintroducedtoevaluatethe
performance of binary classification models. In this research, we used three key ratios:
recall,precision,andF1score,whichwillbeexplainedinorderoftheirsignificance.
Recallorsensitivity,calculatedusingFormula(3),measuresthemodel’ssuccessin
identifyingfailedcompanies. Thismetricisconsideredthemostimportant,asagoodcredit
modelshouldbeabletoidentifyallfailingcompaniesandpreventmisclassifyingthem
ashealthy.
TP
Sensitivity= (24)
TP+FN
Precision,calculatedusingFormula4,evaluatestheaccuracyofthemodelinidentify-
ingfailingcompanies. Inotherwords,itindicatesthelikelihoodthatacompanyidentified
asfailingbythemodelisindeedfailing.
TP
Precision= (25)
TP+FP
F1scoreisametricusedtoevaluatebinaryclassificationmodels,especiallyincases
wherethereisanimbalancebetweenthepositiveandnegativeclasses. TheF1scoreisthe
harmonicmeanofprecisionandrecall,calculatedusingthefollowingformula:
2∗Precision∗Sensitivity
F1Score = (26)
Precision+Sensitivity

Mathematics2025,13,368 16of29
Itbalancesthetwometrics,offeringacomprehensivemeasureofamodel’sperfor-
mancebyconsideringbothhowwellthemodelidentifiesfailedcompanies(recall)andthe
accuracyofthosepredictions(precision). Thisscoreisparticularlyimportantwhenboth
falsepositivesandfalsenegativescarrysignificantcosts.
3.9. StatisticalSignificanceTest
WeusetheFriedman–Nemenyitesttodetectsignificantdifferencesamongthemodels.
This approach is commonly employed in research involving machine learning models,
particularlythoserelatedtobusinessfailure. TheFriedmantestissuitableforcomparing
threeormoregroups,especiallywhentheassumptionofnormalityisviolated. Itextends
theWilcoxonsigned-ranktestbyincorporatinganadditionalassumptionofsphericity[106].
TheFriedmanstatisticiscalculatedasdescribedbyFriedman(1937)[107,108]:
X2 = 12 ∑ R2−3n(k+1) (27)
F nk(k+1) i
where
• nisthenumberofdatasets(blocks);
• k isthenumberofmodels(groups);
• R2isthesumofranksforeachmodel.
i
H isthatthereisnosignificancedifferencebetweenthetwomodelsthathavebeen
0
compared,andifX2 crossesthecriticalvalue,thenH isrejected. WhenH isrejected,then
F 0 0
theNemenyitestisused.
4. CaseStudy
ThestatisticalpopulationoftheresearchcomprisesallcompaniesintheIraniancapital
market from 2015 to 2022. Each instance represents a firm’s annual information, with
instanceslabeledaseither“defaulted”or“healthy.”InIran’seconomy,thegovernment
prohibitslargecompaniesfromdeclaringbankruptcyordefault. Consequently,similarto
mostcreditriskresearchinIran,defaultandbankruptcyaredefinedbasedonArticle141
oftheproposedamendmenttoasectionoftheCommercialCode. Accordingtothisarticle,
ifacompanylosesatleasthalfofitscapitalduetoincurredlosses,theboardofdirectors
mustpromptlyconveneanextraordinarygeneralmeetingofshareholderstodecideonthe
company’sdissolutionorsurvival. Article141effectivelyidentifiesconditionsindicativeof
financialdistress,andduetotheaccessibilityofthisinformation,itisusedbyresearchersin
theIraniancapitalmarket. Thefollowingsectionreviewsthemodelsemployed,detailing
theparametersandcalculationmethodsforeachmodel.
Wedividedoursampleintotrainingandtestdatasetsbasedontheyears. Instances
from2015to2021wereconsideredastrainingdatasets,andinstancesfrom2021to2022
werealsoconsideredastrainingdatasets.
Inthisresearch,asthefocusofourinvestigationinvolvescompanieswhoseshares
are traded in the capital market, we have made efforts to categorize variables into two
maingroups: financialstatement-basedvariablesandvariablesrelatedtothecompany’s
stockprice. Thesevariablesareconsideredthemostfundamentalinformationavailablefor
companiesinthecapitalmarket[109].
Barbozaetal.[62]conductedoneofthemostcomprehensivestudiesinvestigating
the default risk of companies in the North American capital market from 1985 to 2013.
Theyemployedtworesearchapproachestodeterminetheirdatasetvariables. Firstly,they
utilizedthevariablesoftheAltmanmodel[110],afundamentalmodeldesignedtoestimate
the default risk of companies. Secondly, they also incorporated the variables used by
Carton&Hofer[111],whicharebasedonthegrowthrateofsomefundamentalcompany

Mathematics2025,13,368
17of29
variables[62]. Ourfeaturesarederivedfromthebalancesheet,whichisessentialincredit
studies[112].
Itisessentialtomentionthatthecriterionusedinthisresearchfordefaultisnotthe
actualdefaultbuttheinclusioninArticle141,whichismeasuredbasedontheratioofthe
retainedearningstotheregisteredcapitalofthecompany. Oneofthevariablesusedby
Altman(variableX2),representingtheratioofretainedearningstoregisteredcapital,is
excludedfromthedatasetvariableslist. ThereasonforexcludingAltman’sX2isthatthe
defaultcriterioninthisstudyalreadyreliesonthesameratio,thusavoidingredundancy
andoverlappingmetrics. Additionally,oneoftheCarton&Hofervariables,GE,which
measuresthegrowthinthecompanyemployeecount, wasremovedduetothelackof
completeandreliabledata.
The variables of the training and test datasets are as follows, as shown in Table 2,
consideringtheaforementionedpoints.
Table2.Featuresofthedatasetandtheirrespectiveformulas.
|     |     | Variable |     |     |                                             | Formula                      |     |     |
| --- | --- | -------- | --- | --- | ------------------------------------------- | ---------------------------- | --- | --- |
|     |     | X1       |     |     | NetWorkingCapital/Totalassets               |                              |     |     |
|     |     | X3       |     |     | Earningsbeforeinterestandtaxes/Totalassets  |                              |     |     |
|     |     | X4       |     |     | Marketvalueofshare∗numberofshares/Totaldebt |                              |     |     |
|     |     | X5       |     |     |                                             | Sales/Totalassets            |     |     |
|     |     | OM       |     |     | Earningsbeforeintrestandtaxes/Sales         |                              |     |     |
|     |     | GA       |     |     | Totalassetst                                | −Totalassetst−1/Totalassetst |     |     |
|     |     | GS       |     |     |                                             | Salest−Salest−1/Salest−1     |     |     |
|     |     | CROE     |     |     |                                             | ROE t−ROE                    | t−1 |     |
|     |     | CPB      |     |     | Price−to−Book                               | t−Price−to−Book              |     |     |
t−1
Table 3 shows the statistical description of our training and test data. The table
providesastatisticalsummaryofthetrainingandtestdatasets,detailingkeyvariables(e.g.,
X1,X3,andX4). Metricssuchasthemean,standarddeviation,minimum,maximum,and
quartilesofferinsightsintothedistributionofeachvariable.X4andGSexhibitconsiderable
variability,withlargestandarddeviationsandextrememaximumvalues. Thetrainingset
showsmorestability,whilethetestsetincludesoutliers,particularlyforX4andGS.These
variationscouldimpactthemodel’spredictiveperformanceandgeneralizability.
Table3.Statisticaldescriptionofourtrainingandtestdata.
| TrainingSet | X1 X3     | X4   | X5   | OM   | GA   | GS   | CROE | CPB  |
| ----------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| count       | 2987 2987 | 2987 | 2987 | 2987 | 2987 | 2987 | 2987 | 2987 |
−2.688
| mean | 0.083 0.129 | 19.821 | 0.724 |     | 0.374 | 349.054 | 0.698 | 0.057 |
| ---- | ----------- | ------ | ----- | --- | ----- | ------- | ----- | ----- |
std 0.682 0.182 104.381 0.720 129.034 1.536 19,013.508 8.601 3.794
min −16.681 −2.109 0.002 −0.192 −6824.769 −0.786 −203.866 −181.728 −112.889
25% −0.046 0.026 1.339 0.219 0.061 0.038 −0.014 −0.266 −0.077
| 50% | 0.145 0.106 | 4.532  | 0.577 | 0.192 | 0.176 | 0.257 | 0.143 | 0.013 |
| --- | ----------- | ------ | ----- | ----- | ----- | ----- | ----- | ----- |
| 75% | 0.341 0.222 | 13.310 | 1.001 | 0.463 | 0.429 | 0.671 | 1.505 | 0.124 |
max 0.982 0.842 4133.761 7.780 230.176 68.611 1,039,154.000 190.281 125.772
| Testset | X1 X3     | X4   | X5   | OM   | GA   | GS   | CROE | CPB  |
| ------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| count   | 1240 1240 | 1240 | 1240 | 1240 | 1240 | 1240 | 1240 | 1240 |
mean 0.224 0.192 1407.757 0.805 0.463 0.581 0.970 −0.771 −0.111
std 0.365 0.187 18,561.378 0.787 4.646 1.882 11.161 4.969 4.079
min −3.494 −0.781 0.001 −0.579 −18.486 −0.637 −27.413 −99.452 −129.227

Mathematics2025,13,368
18of29
Table3.Cont.
| TrainingSet | X1 X3       | X4     | X5    | OM    | GA    | GS    | CROE   | CPB    |
| ----------- | ----------- | ------ | ----- | ----- | ----- | ----- | ------ | ------ |
| 25%         | 0.057 0.061 | 3.283  | 0.271 | 0.123 | 0.174 | 0.162 | −1.218 | −0.143 |
| 50%         | 0.232 0.179 | 7.290  | 0.633 | 0.286 | 0.366 | 0.479 | −0.173 | −0.013 |
| 75%         | 0.402 0.313 | 16.479 | 1.132 | 0.622 | 0.612 | 0.828 | 0.425  | 0.083  |
max 1.000 0.838 387,142.019 7.467 159.588 44.695 385.756 32.016 47.076
Table 4 presents skewness and kurtosis values for variables in both the training
andtestsets. Skewnessmeasuresasymmetry,withvaluesnearzeroindicatingsymmetric
distributions.Manyvariables,especiallyinthetrainingset(e.g.,X1:−10.814,OM:−50.328),
showhighpositiveornegativeskewness,indicatingsignificantasymmetry.
Table4.SkewnessandKurtosisvaluesforvariablesintotaldatasets.
|     |     |      |             | Skewness |         |             | Kurtosis |          |
| --- | --- | ---- | ----------- | -------- | ------- | ----------- | -------- | -------- |
|     |     |      | TrainingSet |          | TestSet | TrainingSet |          | TestSet  |
|     |     | X1   | −10.814     |          | −2.181  | 199.295     |          | 17.969   |
|     |     | X3   | −1.193      |          | −0.008  | 15.695      |          | 0.939    |
|     |     | X4   | 25.938      |          | 17.379  | 897.031     |          | 319.686  |
|     |     | X5   | 2.584       |          | 2.417   | 12.077      |          | 10.372   |
|     |     | OM   | −50.328     |          | 32.369  | 2629.754    |          | 1113.145 |
|     |     | GA   | 32.133      |          | 19.269  | 1337.749    |          | 426.320  |
|     |     | GS   | 54.653      |          | 33.171  | 2986.988    |          | 1142.797 |
|     |     | CROE | 1.569       |          | −7.078  | 172.100     |          | 136.141  |
|     |     | CPB  | 5.855       |          | −24.427 | 725.704     |          | 826.716  |
Kurtosis measures the “tailedness” of the distribution. High values, such as GS
(2986.988inthetrainingset),suggestextremeoutliers. Thetestsetgenerallyshowslower
kurtosis,indicatingmoremoderateoutlierscomparedtothetrainingset.
Table5showsthecorrelationmatrixamongfeaturesforboththetrainingandtestsets.
Table5.Correlationmatrixamongfeaturesinthetrainingandtestdatasets.
| TrainingSet | X1 X3       | X4     | X5     | OM    | GA     | GS     | CROE   | CPB   |
| ----------- | ----------- | ------ | ------ | ----- | ------ | ------ | ------ | ----- |
| X1          | 1.000 0.529 | 0.103  | 0.097  | 0.255 | 0.040  | −0.004 | −0.173 | 0.008 |
| X3          | 0.529 1.000 | 0.130  | 0.281  | 0.173 | 0.075  | −0.015 | −0.139 | 0.016 |
| X4          | 0.103 0.130 | 1.000  | −0.032 | 0.005 | 0.025  | −0.003 | 0.201  | 0.002 |
|             |             | −0.032 |        |       | −0.018 | −0.016 |        |       |
| X5          | 0.097 0.281 |        | 1.000  | 0.022 |        |        | 0.003  | 0.008 |
−0.013
| OM  | 0.255 0.173 | 0.005 | 0.022  | 1.000 | 0.013 | 0.000 |        | 0.001 |
| --- | ----------- | ----- | ------ | ----- | ----- | ----- | ------ | ----- |
| GA  | 0.040 0.075 | 0.025 | −0.018 | 0.013 | 1.000 | 0.003 | −0.242 | 0.005 |
GS −0.004 −0.015 −0.003 −0.016 0.000 0.003 1.000 −0.001 −0.003
CROE −0.173 −0.139 0.201 0.003 −0.013 −0.242 −0.001 1.000 0.001
| CPB     | 0.008 0.016 | 0.002  | 0.008 | 0.001  | 0.005  | −0.003 | 0.001  | 1.000 |
| ------- | ----------- | ------ | ----- | ------ | ------ | ------ | ------ | ----- |
| Testset | X1 X3       | X4     | X5    | OM     | GA     | GS     | CROE   | CPB   |
|         |             |        |       | −0.001 | −0.046 | −0.025 | −0.029 |       |
| X1      | 1.000 0.445 | 0.127  | 0.017 |        |        |        |        | 0.024 |
| X3      | 0.445 1.000 | −0.115 | 0.321 | 0.026  | −0.003 | 0.112  | −0.045 | 0.042 |
X4 0.127 −0.115 1.000 −0.086 0.009 −0.028 −0.016 0.012 −0.001
| X5  | 0.017 0.321 | −0.086 | 1.000 | −0.049 | −0.027 | 0.009 | 0.054 | 0.035 |
| --- | ----------- | ------ | ----- | ------ | ------ | ----- | ----- | ----- |
OM −0.001 0.026 0.009 −0.049 1.000 −0.007 −0.001 0.004 −0.008
GA −0.046 −0.003 −0.028 −0.027 −0.007 1.000 −0.001 −0.606 −0.023
GS −0.025 0.112 −0.016 0.009 −0.001 −0.001 1.000 −0.007 0.037
|      | −0.029 −0.045 |        |       |        | −0.606 | −0.007 |       |       |
| ---- | ------------- | ------ | ----- | ------ | ------ | ------ | ----- | ----- |
| CROE |               | 0.012  | 0.054 | 0.004  |        |        | 1.000 | 0.005 |
| CPB  | 0.024 0.042   | −0.001 | 0.035 | −0.008 | −0.023 | 0.037  | 0.005 | 1.000 |

Mathematics2025,13,368
19of29
5. ExperimentalDiscussion
5.1. EvaluationAmongModels
Table 6 shows the results of applying SMOTE and CorrOV-CSEn across different
machinelearningmethods. Wesummarizealltheresultshereandhighlightthebestresult
foreachaspectamongthemodelsinbold.
Table6.Performancemetricsfordifferentmachinelearningmodels.
| Model | Sensitivity | Precision | F1Score |
| ----- | ----------- | --------- | ------- |
CorrOV-CSEn
| Multi-LayerPerceptron(MLP) | 0.841 | 0.327 | 0.471 |
| -------------------------- | ----- | ----- | ----- |
| RandomForest               | 0.886 | 0.375 | 0.527 |
| GradientBoosting           | 0.795 | 0.443 | 0.569 |
| XGBoost                    | 0.795 | 0.393 | 0.526 |
| AdaBoost                   | 0.750 | 0.478 | 0.584 |
| CatBoost                   | 0.909 | 0.201 | 0.329 |
SMOTE
| Multi-LayerPerceptron(MLP) | 0.841 | 0.327 | 0.471 |
| -------------------------- | ----- | ----- | ----- |
| RandomForest               | 0.795 | 0.603 | 0.686 |
| GradientBoosting           | 0.727 | 0.603 | 0.660 |
| XGBoost                    | 0.772 | 0.554 | 0.645 |
| AdaBoost                   | 0.568 | 0.555 | 0.561 |
| CatBoost                   | 0.750 | 0.717 | 0.733 |
The performance evaluation of the Multi-Layer Perceptron (MLP), random forest,
gradientboosting,XGBoost,AdaBoost,andCatBoostmodelsrevealssignificantdifferences
intheirclassificationaccuracy. classification accuracy.
  CCoorrrrOOVV--CCSSEEnn RReessuullttss::
  • Multi-LayerPerceptron(MLP)showsgoodsensitivity(0.84). However,itstruggles
withprecision(0.33),meaningarelativelysmallproportionofthepredictedfailure
casesareactualfailures. ThisimbalanceresultsinamoderateF1scoreof0.47.
• Randomforestdemonstratesstrongsensitivity(0.89),meaningiteffectivelydetects
failure cases. However, it struggles with precision (0.38), indicating that only a
relativelysmallportionofthefirmspredictedasfailuresareactuallyfailures. This
resultsinamoderateF1scoreof(0.53). Ontheotherhand,whenusingSMOTE,it
records(0.80)forsensitivityandlosesmuchofitssuccessrateforidentifyingdefault
firms. However,precisiongotbetter((0.60)and(0.69)).
• Gradientboostingoffersbalancedperformance,withasensitivityof(0.80)andhigher
precision(0.44),resultinginanF1scoreof(0.57).Thisindicatesbetteroverallhandling
ofbothfalsepositivesandfalsenegatives.
• XGBoostperformssimilarlytogradientboosting,withthesamesensitivity(0.80)but
slightlylowerprecision(0.39),resultinginanF1scoreof(0.53). Whilestillrobust,itis
slightlyoutperformedbygradientboostingintermsofprecision.
• AdaBoosthasthelowestsensitivity(0.75)butthehighestprecision(0.48),resultingin
acompetitiveF1scoreof(0.58). Thisindicatesthatwhileitsfailurepredictionsare
moreaccurate,itmissessomefailurecases.
• CatBoostexhibitsthehighestsensitivity(0.91)butstrugglesthemostwithprecision
(0.20), leadingtotheweakestF1score(0.33). ThissuggeststhatwhileCatBoostis
highlyeffectiveatdetectingfailures,whichisourprimaryobjective,itproducesmore
cflaalssseifipcoastiitoivne asc.curacy.
  CSoMrrOOTVE-CRSesEunl tRs:esults:
  • Multi-LayerPerceptron(MLP)maintainsasimilarperformancepattern. Sensitivity
remainshighat0.84,effectivelycapturingfailurecases,whileprecisionstaysrelatively
lowat0.33,indicatingthatmanypredictedfailurecaseswerenotactualfailures.

Mathematics2025,13,368 20of29
• Random forest sensitivity drops to 0.80 while precision improves to 0.60, leading
to an F1 score of 0.69. However, the sensitivity reduction indicates some missed
failurecases.
• Gradientboostingshowslowersensitivity(0.73)withaslightprecisionincrease(0.60),
resultinginanF1scoreof0.66,suggestingamodesttrade-off.
• XGBoostseesaminordecreaseinsensitivity(0.77)andanincreaseinprecision(0.55),
withanF1scoreof0.65.
• AdaBoostunderSMOTEshowsasignificantdropinsensitivity(0.57)withminimal
gaininprecision(0.56),reducingitsF1scoreto0.56.
• CatBoostimprovesprecision(0.72)butitssensitivityremainslowerthanCorrOV-CSEn,
withanF1scoreof0.73,showingmorebalancedresultsbutstilllowersensitivity.
ThesefindingsrevealthatCatBoostreachedthehighestsensitivity,whichisfollowed
byrandomforest,Multi-LayerPerceptron(MLP),gradientboosting,XGBoost,andAd-
aBoost. On the other hand, CatBoost and random forest, despite their high sensitivity,
achieverelativelypoorprecisionandoveralleffectiveness.
WhentheSMOTEmethodisused,XGBoostrecordsthehighestsensitivity,followed
byrandomforest,gradientboosting,CatBoost,andAdaBoost. Meanwhile,CatBoosthas
thebestprecisionandF1score.
CatBoostemergesasthestrongestmodelintermsofsensitivitywhencombinedwith
CorrOV-CSEn. ThisisprimarilyduetothefeaturesofCorrOV-CSEn,wheretheaugmented
dataaregeneratedbasedoncorrelations,leadingtolessnoisydatabeingfedintothemodel.
Additionally,theminorityclassreceivesmoreweightautomatically,whichisessentialin
imbalanceddatasets. CatBoost,beinghighlyadaptabletoweighteddata,caneffectively
handletheimbalanceandemphasizetheminorityclass.
Furthermore,CatBoostusesagradientboostingframeworkwithdecisiontrees,lever-
agingthepowerfulcombinationofcategoricalfeatureprocessingandboostingtohandle
theweightdistributionsmoreefficiently. Forrecallspecifically,CorrOV-CSEngenerates
datathatclarifiestheboundarybetweenclasses, reducingoverlapandthusimproving
recall. This characteristic is particularly beneficial for models like CatBoost, which are
well-equippedtolearnfromcomplexrelationshipsinthedata,includingthosebetween
featuresthataremorestronglycorrelatedwithdefaultcases.
5.2. SignificanceDifferences
For a more detailed comparison of our models, we divided the dataset into four
subsets. Theperformanceacrossthesesubsetsrevealsnotablevariations,highlightingthe
models’differingstrengthsandweaknessesinhandlingimbalanceddata. Table7describes
theperformanceofmachinelearningmodelsacrossfourdatasets.
CatBoostachieveshighsensitivity,particularlyinDataset-I(1.00)andDataset-IV(1.00).
ItalsoperformsreasonablywellinDataset-II(0.86)andDataset-III(0.89),indicatingits
effectivenessinidentifyingpositivecases. GradientboostingandXGBoostdemonstratethe
highestandmostconsistentsensitivityacrossalldatasets,bothachievingperfectsensitivity
(1.00)inDataset-IandDataset-IV.However,theyexperiencemoderatedropsinDataset-II
(0.57and0.71,respectively)andDataset-III(0.56and0.67,respectively). Randomforest
showsvariedsensitivity,excellinginDataset-I(0.95)andDataset-IV(0.88)butdropping
significantlyinDataset-II(0.71)andDataset-III(0.67). TheperformanceofMulti-Layer
Perceptron (MLP), similar to random forest, varies significantly, ranging from 0.84 in
Dataset-II to 0.67 in Dataset-IV. AdaBoost struggles more with sensitivity, particularly
inDataset-II(0.43)andDataset-III(0.56),thoughitperformswellinDataset-I(0.80)and
Dataset-IV(0.88).

Mathematics2025,13,368
21of29
Table7.Performancecomparisonofmachinelearningmodelsacrossfourdatasets.
|     | Dataset-I |     |     |     | Dataset-II |     |
| --- | --------- | --- | --- | --- | ---------- | --- |
Model Sensitivity Precision F1Score Sensitivity Precision F1Score
Multi-LayerPerceptron(MLP) 0.693 0.455 0.550 0.844 0.371 0.516
| RandomForest     | 0.950       | 0.593 | 0.731 | 0.714 | 0.192      | 0.303 |
| ---------------- | ----------- | ----- | ----- | ----- | ---------- | ----- |
| GradientBoosting | 1.000       | 0.666 | 0.800 | 0.571 | 0.500      | 0.533 |
| XGBoost          | 1.000       | 0.606 | 0.755 | 0.714 | 0.385      | 0.500 |
| AdaBoost         | 0.800       | 0.640 | 0.711 | 0.429 | 0.429      | 0.429 |
| CatBoost         | 1.000       | 0.339 | 0.506 | 0.857 | 0.188      | 0.308 |
|                  | Dataset-III |       |       |       | Dataset-IV |       |
Model Sensitivity Precision F1Score Sensitivity Precision F1Score
Multi-LayerPerceptron(MLP) 0.773 0.370 0.500 0.670 0.451 0.540
| RandomForest | 0.666 | 0.240 | 0.353 | 0.875 | 0.368 | 0.519 |
| ------------ | ----- | ----- | ----- | ----- | ----- | ----- |
Gradient
|     | 0.556 | 0.227 | 0.323 | 1.000 | 0.444 | 0.615 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- |
Boosting
| XGBoost  | 0.667 | 0.300 | 0.414 | 1.000 | 0.333 | 0.500 |
| -------- | ----- | ----- | ----- | ----- | ----- | ----- |
| AdaBoost | 0.556 | 0.313 | 0.4   | 0.875 | 0.389 | 0.538 |
| CatBoost | 0.889 | 0.138 | 0.239 | 1.000 | 0.116 | 0.208 |
Gradientboostingdeliverssolidprecisionacrossalldatasets,particularlyinDataset-I
(0.67)andDataset-IV(0.44). XGBoostalsoperformswellintermsofprecision,especiallyin
Dataset-I(0.61),butsuffersslightlyinDataset-II(0.38)andDataset-IV(0.33),indicatinga
highernumberoffalsepositivesinthesedatasets. Multi-LayerPerceptron(MLP)achieves
amorestableperformance,withscoresrangingfrom(0.37)to(0.45)acrossthefourdatasets.
Randomforestshowsawiderangeofprecision,performingstronglyinDataset-I(0.59)but
strugglingsignificantlyinDataset-II(0.19),Dataset-III(0.24),andDataset-IV(0.37). This
suggeststhatwhilerandomforestcapturespositivecaseswell,itispronetomisclassifying
negativecasesaspositive. CatBoostexhibitstheweakestprecisionacrossalldatasets,with
valuesof(0.34)inDataset-I,(0.19)inDataset-II,(0.14)inDataset-III,and(0.12)inDataset-IV,
indicating consistent difficulty in accurately classifying failure cases and a higher rate
of false positives. AdaBoost generally maintains moderate precision, performing best
inDataset-I(0.64)butfallingto(0.43)inDataset-II,withconsistentbutlowerresultsin
Dataset-IIIandDataset-IV.
GradientboostingachievesthehighestandmostconsistentF1scores,particularlyin
Dataset-I(0.80)andDataset-IV(0.62). XGBoostalsoperformswell,especiallyinDataset-I
(0.75), with solid F1 scores in Dataset-III (0.41) and Dataset-IV (0.50). However, its F1
score drops slightly in Dataset-II (0.50). Random forest delivers strong performance in
Dataset-I(0.73)andDataset-IV(0.52),butitslowerF1scoresinDataset-II(0.30)andDataset-
III (0.35) highlight its susceptibility to imbalanced class distributions, especially where
precision is low. The Multi-Layer Perceptron (MLP) achieves stable performance, with
scoresconsistentlyaround(0.50). AdaBoostperformsmoderatelywell,withpeakF1scores
inDataset-I(0.71)andDataset-IV(0.54),butfaceschallengesinDataset-II(0.43)andDataset-
III(0.40). Despiteitshighsensitivity,CatBoostsuffersthemostintermsofF1scoredueto
poorprecision,whichmayneedtuningforscenarioswhereprecisionismorecritical. ItsF1
scoresare(0.51)inDataset-I,(0.31)inDataset-II,and(0.21)inDataset-IV.
We also used the Friedman–Nemenyi test to detect significant differences among
the models. Table 8 shows the results of the Friedman–Nemenyi test for each of the
threescores.

Mathematics2025,13,368
22of29
Table8.Friedmantestresultsforcomparisonsamongmachinelearningmodels.
Precision
| FriedmanTestStatistic | 12.00   |     |     |     |     |     |
| --------------------- | ------- | --- | --- | --- | --- | --- |
| p-value               | 0.03479 |     |     |     |     |     |
Multi-Layer
|     | RandomForest |     | GradientBoosting | XGBoost | AdaBoost | CatBoost |
| --- | ------------ | --- | ---------------- | ------- | -------- | -------- |
Perceptron(MLP)
| RandomForest | -   | 0.854075 | 0.635776 | 0.900000 | 0.635776 | 0.744925 |
| ------------ | --- | -------- | -------- | -------- | -------- | -------- |
Multi-LayerPerceptron(MLP) 0.854075 - 0.900000 0.900000 0.900000 0.136905
GradientBoosting 0.635776 0.900000 - 0.900000 0.900000 0.052161
| XGBoost  | 0.900000 | 0.900000 | 0.900000 | -        | 0.900000 | 0.410222 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| AdaBoost | 0.635776 | 0.900000 | 0.900000 | 0.900000 | -        | 0.052161 |
| CatBoost | 0.744925 | 0.136905 | 0.052161 | 0.410222 | 0.052161 | -        |
Sensitivity
| FriedmanTestStatistic | 10.04 |     |     |     |     |     |
| --------------------- | ----- | --- | --- | --- | --- | --- |
p-value1
0.07413
NosignificantdifferencewasfoundbytheFriedmantestbecausethep-valueisgreaterthanthesignificancelevelof0.05.
F1Score
| FriedmanTestStatistic | 10.43   |     |     |     |     |     |
| --------------------- | ------- | --- | --- | --- | --- | --- |
| p-value2              | 0.06396 |     |     |     |     |     |
1,2NosignificantdifferencewasfoundbytheFriedmantestbecausethep-valueisgreaterthanthesignificance
levelof0.05.
Sincethep-valueislessthan0.05,theFriedmantestindicatesasignificantdifference
insensitivityandprecisionacrossthemodels:
• AdaBoost vs. CatBoost: This is the only comparison with a significant difference
(p-value=0.030),showingthatCatBoostperformssignificantlybetterthanAdaBoost
intermsofsensitivity.
•
Gradient boosting vs. CatBoost, AdaBoost vs. CatBoost, and MLP vs. CatBoost:
Allcomparisonsshowsignificantdifferenceswithp-valuesof0.030,indicatingthat
CatBoosthassignificantlylowerprecisioncomparedtogradientboosting,AdaBoost,
andMLP.
Allothercomparisonshavep-valuesabove0.05,indicatingnosignificantdifferences
insensitivityandprecisionbetweenthesemodels.
5.3. FeatureImportance
Inthefinalstage,wepresenttheimportanceofourfeaturesetacrossthemodelsused.
Figure3illustratesthefeatureimportanceinourmodels. ItisclearthatX1hasthehighest
importanceinallmodelsexpectMLP.Thiscontrastswithothercreditriskstudiesusingthe
samefeaturesetintheIraniancapitalmarket[64].

Mathematics 2025, 13, x FOR PEER REVIEW  22 of 29

Since the p-value is less than 0.05, the Friedman test indicates a significant difference
in sensitivity and precision across the models:
•
AdaBoost vs. CatBoost: This is the only comparison with a significant difference (p-
value = 0.030), showing that CatBoost performs significantly better than AdaBoost in
terms of sensitivity.
•  Gradient boosting vs. CatBoost, AdaBoost vs. CatBoost, and MLP vs. CatBoost: All
comparisons show significant differences with p-values of 0.030, indicating that Cat-
Boost has significantly lower precision compared to gradient boosting, AdaBoost,
and MLP.
All other comparisons have p-values above 0.05, indicating no significant differences
in sensitivity and precision between these models.
5.3. Feature Importance
In the final stage, we present the importance of our feature set across the models
used. Figure 3 illustrates the feature importance in our models. It is clear that X1 has the
Mathematics2025,13,368 highest importance in all models expect MLP. This contrasts with other credit r2i3skof s2t9udies
using the same feature set in the Iranian capital market [64].
|      | RandomForest |     |      |     | XGBoost  |     |     |
| ---- | ------------ | --- | ---- | --- | -------- | --- | --- |
| CPB  |              |     | CPB  |     |          |     |     |
| CROE |              |     | CROE |     |          |     |     |
| GS   |              |     |      | GS  |          |     |     |
| GA   |              |     |      | GA  |          |     |     |
| OM   |              |     |      | OM  |          |     |     |
| X5   |              |     |      | X5  |          |     |     |
| X4   |              |     |      | X4  |          |     |     |
| X3   |              |     |      | X3  |          |     |     |
| X1   |              |     |      | X1  |          |     |     |
| 0    | 0.1          | 0.2 | 0.3  | 0   | 0.1      | 0.2 | 0.3 |

|      | AdaBoost   |     |      |     | CatBoost    |     |     |
| ---- | ---------- | --- | ---- | --- | ----------- | --- | --- |
| CPB  |            |     | CPB  |     |             |     |     |
| CROE |            |     | CROE |     |             |     |     |
| GS   |            |     |      | GS  |             |     |     |
| GA   |            |     |      | GA  |             |     |     |
| OM   |            |     |      | OM  |             |     |     |
| X5   |            |     |      | X5  |             |     |     |
| X4   |            |     |      | X4  |             |     |     |
| X3   |            |     |      | X3  |             |     |     |
| X1   |            |     |      | X1  |             |     |     |
Mathematics 2025, 13, x FOR PEER REVIEW  23 of 29

| 0                | 0.05 0.1 | 0.15 | 0.2  | 0   | 10  | 20  | 30  |
| ---------------- | -------- | ---- | ---- | --- | --- | --- | --- |
|                  |          |      |      |     |     |     |     |
| GradientBoosting |          |      |      |     | MLP |     |     |
| CPB              |          |      | CPB  |     |     |     |     |
| CROE             |          |      | CROE |     |     |     |     |
| GS               |          |      |      | GS  |     |     |     |
| GA               |          |      |      | GA  |     |     |     |

| OM  |         |     | OM  |     |          |      |     |
| --- | ------- | --- | --- | --- | -------- | ---- | --- |
| X5  |         |     |     | X5  |          |      |     |
| X4  |         |     |     | X4  |          |      |     |
| X3  |         |     |     | X3  |          |      |     |
| X1  |         |     |     | X1  |          |      |     |
| 0   | 0.2 0.4 | 0.6 | 0.8 | 0   | 0.05 0.1 | 0.15 | 0.2 |
|     |         |     |     |     |          |      |     |
Figure3.Featureimportanceinourmachinelearningmodels.
Figure 3. Feature importance in our machine learning models.
6. Conclusions
In this study, we employed recently introduced cost-sensitive methods to predict
business failures in the Iranian capital market using five decision tree-based algorithms in
addition to MPL. Our findings demonstrate that all models achieved improved sensitivity
scores through this approach, with CatBoost outperforming the others.
While CatBoost showed clear superiority, there remains a tradeoff between extend-
ing credit to a broader range of customers to maximize revenue and minimizing the risk
of default. Future research could focus on developing models that optimize creditor prof-
its by balancing revenue generation with risk management rather than solely assessing
default risk.
Additionally, other decision tree-based methods, such as Mondrian Forest, could be
explored in this context. In addition to the models evaluated in this study, it is important
to consider the role of hyperparameter optimization in improving model performance.
While our current work focuses on assessing the effectiveness of various decision tree-
based models, incorporating optimization techniques such as grid search or Bayesian op-
timization could lead to even better-performing models.
From a data perspective, incorporating new types of data, including sentiment anal-
ysis, textual data, and political indices, could significantly enhance model performance.
This is especially relevant in countries like Iran, where political and economic conditions
play a crucial role in credit risk management.
Our research focused on the Iran capital market, and due to the unique economic and
political challenges facing the Iranian capital market, these findings might not exactly ap-
ply to other industries or nations, although many developing countries face similar chal-
lenges, like extensive governmental administration, challenges related to market effi-
ciency, and regulatory frameworks and political instability. It is recommended to consider
actual default instead of failure under Article 141 of the Amended Commercial Code.
Further, it is important to notice that the data analysis results may be affected by the
global economic meltdown caused by the pandemic during the window period. There-
fore, in the upcoming research, it is potential to conduct a sensitivity analysis to compare
the results with the exclusion of the COVID-19 period.
Lastly, there is considerable potential in applying these methods to emerging fields,
such as peer-to-peer (P2P) lending platforms, which have been growing rapidly in Iran in
recent years.

Mathematics2025,13,368 24of29
6. Conclusions
In this study, we employed recently introduced cost-sensitive methods to predict
businessfailuresintheIraniancapitalmarketusingfivedecisiontree-basedalgorithmsin
additiontoMPL.Ourfindingsdemonstratethatallmodelsachievedimprovedsensitivity
scoresthroughthisapproach,withCatBoostoutperformingtheothers.
WhileCatBoostshowedclearsuperiority,thereremainsatradeoffbetweenextending
credit to a broader range of customers to maximize revenue and minimizing the risk
of default. Future research could focus on developing models that optimize creditor
profitsbybalancingrevenuegenerationwithriskmanagementratherthansolelyassessing
defaultrisk.
Additionally,otherdecisiontree-basedmethods,suchasMondrianForest,couldbe
exploredinthiscontext. Inadditiontothemodelsevaluatedinthisstudy,itisimportant
to consider the role of hyperparameter optimization in improving model performance.
While our current work focuses on assessing the effectiveness of various decision tree-
based models, incorporating optimization techniques such as grid search or Bayesian
optimizationcouldleadtoevenbetter-performingmodels.
Fromadataperspective,incorporatingnewtypesofdata,includingsentimentanalysis,
textualdata,andpoliticalindices,couldsignificantlyenhancemodelperformance. Thisis
especiallyrelevantincountrieslikeIran,wherepoliticalandeconomicconditionsplaya
crucialroleincreditriskmanagement.
OurresearchfocusedontheIrancapitalmarket,andduetotheuniqueeconomicand
politicalchallengesfacingtheIraniancapitalmarket,thesefindingsmightnotexactlyapply
tootherindustriesornations,althoughmanydevelopingcountriesfacesimilarchallenges,
likeextensivegovernmentaladministration,challengesrelatedtomarketefficiency,and
regulatory frameworks and political instability. It is recommended to consider actual
defaultinsteadoffailureunderArticle141oftheAmendedCommercialCode.
Further,itisimportanttonoticethatthedataanalysisresultsmaybeaffectedbythe
globaleconomicmeltdowncausedbythepandemicduringthewindowperiod. Therefore,
intheupcomingresearch,itispotentialtoconductasensitivityanalysistocomparethe
resultswiththeexclusionoftheCOVID-19period.
Lastly,thereisconsiderablepotentialinapplyingthesemethodstoemergingfields,
suchaspeer-to-peer(P2P)lendingplatforms,whichhavebeengrowingrapidlyinIranin
recentyears.
AuthorContributions:Conceptualization,P.P.,M.P.F.,C.T.,M.S.andH.K.;methodology,P.P.,M.P.F.,
C.T.,M.S.andH.K.;software,P.P.andH.K.;validation,P.P.,M.P.F.,C.T.andH.K.;formalanalysis,P.P.,
C.T.,M.S.andH.K.;investigation,P.P.,M.P.F.,C.T.andM.S.;resources,P.P.,M.P.F.,C.T.andM.S.;data
curation,M.P.F.,M.S.andH.K.;writing—originaldraftpreparation,P.P.andH.K.;writing—review
andediting,P.P.,M.P.F.,C.T.,M.S.andH.K.;visualization,P.P.,M.S.andH.K.;supervision,P.P.,M.P.F.,
C.T.andM.S.;projectadministration,P.P.,C.T.andM.P.F.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Dataarecontainedwithinthearticle.
Acknowledgments:Theauthorswouldliketothanktheanonymousreviewersandtheeditor-in-chief
fortheirconstructivecommentsandsuggestions.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

Mathematics2025,13,368 25of29
References
1. Usmani,S.; Shamsi,J.A.LSTMbasedstockpredictionusingweightedandcategorizedfinancialnews. PLoSONE2023,18,
e0282234.[CrossRef][PubMed]
2. Zhang,Z.;Liu,X.;Niu,H.FinancialcrisisearlywarningofChineselistedcompaniesbasedonMD&Atext-linguisticfeature
indicators.PLoSONE2023,18,e0291818.[CrossRef]
3. Jezeie,F.V.;Sadjadi,S.J.;Makui,A.Constrainedportfoliooptimizationwithdiscretevariables:Analgorithmicmethodbasedon
dynamicprogramming.PLoSONE2022,17,e0271811.[CrossRef][PubMed]
4. Bi,W.;Zhang,Q.Forecastingmergersandacquisitionsfailurebasedonpartial-sigmoidneuralnetworkandfeatureselec-tion.
PLoSONE2021,16,e0259575.[CrossRef]
5. Li,M.FinancialinvestmentriskpredictionundertheapplicationofinformationinteractionFireflyAlgorithmcombinedwith
GraphConvolutionalNetwork.PLoSONE2023,18,e0291510.[CrossRef]
6. Dahal,K.R.;Pokhrel,N.R.;Gaire,S.;Mahatara,S.;Joshi,R.P.;Gupta,A.;Banjade,H.R.;Joshi,J.Acomparativestudyoneffectof
newssentimentonstockpricepredictionwithdeeplearningarchitecture.PLoSONE2023,18,e0284695.[CrossRef][PubMed]
7. Javid,I.;Ghazali,R.;Syed,I.;Zulqarnain,M.;Husaini,N.A.StudyonthePakistanstockmarketusinganewstockcrisisprediction
method.PLoSONE2022,17,e0275022.[CrossRef]
8. Cui, Y.; Liu, L.Investorsentiment-awarepredictionmodelforP2PlendingindicatorsbasedonLSTM.PLoSONE2022, 17,
e0262539.[CrossRef]
9. Zhu,C.;Liu,X.;Chen,D.Predictionofdigitaltransformationofmanufacturingindustrybasedoninterpretablemachinelearning.
PLoSONE2024,19,e0299147.[CrossRef][PubMed]
10. Khan,A.H.;Shah,A.;Ali,A.;Shahid,R.;Zahid,Z.U.;Sharif,M.U.;Jan,T.;Zafar,M.H.Aperformancecomparisonofmachine
learningmodelsforstockmarketpredictionwithnovelinvestmentstrategy.PLoSONE2023,18,e0286362.[CrossRef][PubMed]
11. Wei,X.;Ouyang,H.;Liu,M.StockindextrendpredictionbasedonTabNetfeatureselectionandlongshort-termmemory.PLoS
ONE2022,17,e0269195.[CrossRef][PubMed]
12. Tran,T.;Nguyen,N.H.;Le,B.T.;Vu,N.T.;Vo,D.H.ExaminingfinancialdistressoftheVietnameselistedfirmsusingaccounting-
basedmodels.PLoSONE2023,18,e0284451.[CrossRef][PubMed]
13. Laghari,F.;Ahmed,F.;LópezGarcía,M.D.L.N.Cashflowmanagementanditseffectonfirmperformance:Empiricalev-idence
onnon-financialfirmsofChina.PLoSONE2023,18,e0287135.[CrossRef][PubMed]
14. Almustafa,H.;Nguyen,Q.K.;Liu,J.;Dang,V.C.TheimpactofCOVID-19onfirmriskandperformanceinMENAcountries:
Doesnationalgovernancequalitymatter?PLoSONE2023,18,e0281148.[CrossRef][PubMed]
15. Tian,X.;Wang,Y.;Kohar,U.H.A.Capitalstructure,businessmodelinnovation,andfirmperformance:EvidencefromChinese
listedcorporatebasedonsystemGMMmodel.PLoSONE2024,19,e0306054.[CrossRef]
16. Samour,A.;AlGhazali,A.;Gadoiu,M.;Banuta,M.CapitalstructureandfinancialperformanceofChina’senergyindustry:What
canweinferfromCOVID-19?PLoSONE2024,19,e0300936.
17. Berloco,C.;Morales,G.D.F.;Frassineti,D.;Greco,G.;Kumarasinghe,H.;Lamieri,M.;Massaro,E.;Miola,A.;Yang,S.Predicting
corporatecreditrisk:Networkcontagionviatradecredit.PLoSONE2021,16,e0250115.[CrossRef][PubMed]
18. Hlongwane, R.; Ramaboa, K.K.K.M.; Mongwe, W. Enhancing credit scoring accuracy with a comprehensive evaluation of
alternativedata.PLoSONE2024,19,e0303566.[CrossRef][PubMed]
19. Ma,Z.;Hou,W.;Zhang,D.AcreditriskassessmentmodelofborrowersinP2PlendingbasedonBPneuralnetwork.PLoSONE
2021,16,e0255216.[CrossRef][PubMed]
20. Wang,H.;Liu,X.Undersamplingbankruptcyprediction:Taiwanbankruptcydata.PLoSONE2021,16,e0254030.[CrossRef]
[PubMed]
21. Japkowicz,N.Learningfromimbalanceddatasets: Acomparisonofvariousstrategies. InAAAIWorkshoponLearningfrom
ImbalancedDataSets;AAAIPress:MenloPark,CA,USA,2000.
22. Groccia,M.C.;Guido,R.;Conforti,D.;Pelaia,C.;Armentaro,G.;Toscani,A.F.;Miceli,S.;Succurro,E.;Hribal,M.L.;Sciacqua,A.
Cost-SensitiveModelstoPredictRiskofCardiovascularEventsinPatientswithChronicHeartFailure.Information2023,14,542.
[CrossRef]
23. Natha,P.;RajaRajeswari,P.AdvancingSkinCancerPredictionUsingEnsembleModels.Computers2024,13,157.[CrossRef]
24. Devi,D.;Biswas,S.K.;Purkayastha,B.Correlation-basedOversamplingaidedCostSensitiveEnsemblelearningtechniquefor
TreatmentofClassImbalance.J.Exp.Theor.Artif.Intell.2022,34,143–174.[CrossRef]
25. Alloway,B.T.;Weisenthal,J.What’sBeenHappeningwiththeIranianStockMarket;Bloomberg:NewYork,NY,USA,2023.
26. Rawat, S.S.; Mishra, A.K. Review of Methods for Handling Class-Imbalanced in Classification Problems. arXiv 2022,
arXiv:2211.05456.
27. Tomek,I.TwoModificationsofCNN.IEEETrans.Syst.ManCybern.1976,11,769–772.
28. Kubat,M.;Matwin,S.Addressingthecurseofimbalanceddatasets: One-sidedsampling. InProceedingsoftheFourteenth
InternationalConferenceonMachineLearning,Nashville,TN,USA,8–12July1997.

Mathematics2025,13,368 26of29
29. Japkowicz,N.Theclassimbalanceproblem: Significanceandstrategies. InProceedingsoftheInternationalConferenceon
ArtificialIntelligence,LasVegas,NV,USA,26–29June2000.
30. Laurikkala,J.Improvingidentificationofdifficultsmallclassesbybalancingclassdistribution.InProceedingsoftheArtificial
IntelligenceinMedicine:8thConferenceonArtificialIntelligenceinMedicineinEurope,AIME2001,Cascais,Portugal,1–4July
2001;Proceedings8.Springer:Berlin/Heidelberg,Germany,2001.
31. Hoyos-Osorio,J.;Alvarez-Meza,A.;Daza-Santacoloma,G.;Orozco-Gutierrez,A.;Castellanos-Dominguez,G.Relevantinforma-
tionundersamplingtosupportimbalanceddataclassification.Neurocomputing2021,436,136–146.[CrossRef]
32. Lee,W.;Seo,K.DownsamplingforBinaryClassificationwithaHighlyImbalancedDatasetUsingActiveLearning.BigDataRes.
2022,28,100314.[CrossRef]
33. Laveti,R.N.;Mane,A.A.;Pal,S.N.DynamicStackedEnsemblewithEntropybasedUndersamplingfortheDetectionofFraudulent
Transactions.InProceedingsofthe20216thInternationalConferenceforConvergenceinTechnology(I2CT),Maharashtra,India,
2–4April2021;pp.1–7.
34. Solberg, A.S.; Solberg, R. A large-scale evaluation of features for automatic detection of oil spills in ERS SAR images. In
ProceedingsoftheIGARSS’96.1996InternationalGeoscienceandRemoteSensingSymposium,Lincoln,NB,USA,21–26May
1996;pp.1484–1486.
35. Mathew,J.;Pang,C.K.;Luo,M.;Leong,W.H.ClassificationofImbalancedDatabyOversamplinginKernelSpaceofSupport
VectorMachines.IEEETrans.NeuralNetworksLearn.Syst.2017,29,4065–4076.[CrossRef][PubMed]
36. Bennin, K.E.; Keung, J.; Phannachitta, P.; Monden, A.; Mensah, S.MAHAKIL:DiversityBasedOversamplingApproachto
AlleviatetheClassImbalanceIssueinSoftwareDefectPrediction.IEEETrans.Softw.Eng.2017,44,534–550.[CrossRef]
37. Cheng, K.; Zhang, C.; Yu, H.; Yang, X.; Zou, H.; Gao, S.GroupedSMOTEWithNoiseFilteringMechanismforClassifying
ImbalancedData.IEEEAccess2019,7,170668–170681.[CrossRef]
38. Tarawneh,A.S.;Hassanat,A.B.A.;Almohammadi,K.;Chetverikov,D.;Bellinger,C.SMOTEFUNA:SyntheticMinorityOver-
SamplingTechniqueBasedonFurthestNeighbourAlgorithm.IEEEAccess2020,8,59069–59082.[CrossRef]
39. Almomani,I.;Qaddoura,R.;Habib,M.;Alsoghyer,S.;AlKhayer,A.;Aljarah,I.;Faris,H.Androidransomwaredetectionbased
onahybridevolutionaryapproachinthecontextofhighlyim-balanceddata.IEEEAccess2021,9,57674–57691.[CrossRef]
40. Juez-Gil,M.;Arnaiz-González,Á.;Rodríguez,J.J.;López-Nozal,C.;García-Osorio,C.Approx-SMOTE:FastSMOTEforBigData
onApacheSpark.Neurocomputing2021,464,432–437.[CrossRef]
41. Chawla,N.V.;Bowyer,K.W.;Hall,L.O.;Kegelmeyer,W.P.SMOTE:SyntheticMinorityOver-samplingTechnique.J.Artif.Intell.
Res.2002,16,321–357.[CrossRef]
42. Li,C.DataMiningforDirectMarketing:ProblemsandSolutions;NationalLibraryofCanada=BibliothèquenationaleduCanada:
Ottawa,ON,Canada,2000.
43. Xu,Z.;Shen,D.;Nie,T.;Kou,Y.AhybridsamplingalgorithmcombiningM-SMOTEandENNbasedonRandomforestfor
medicalimbalanceddata.J.Biomed.Informatics2020,107,103465.[CrossRef]
44. Dong;Xiao,H.;Dong,Y.SA-CGAN:AnoversamplingmethodbasedonsingleattributeguidedconditionalGANformulti-class
imbalancedlearning.Neurocomputing2022,472,326–337.[CrossRef]
45. Sharma,A.;Singh,P.K.;Chandra,R.SMOTified-GANforClassImbalancedPatternClassificationProblems.IEEEAccess2022,10,
30655–30665.[CrossRef]
46. Puri,A.;Gupta,M.K.ImprovedHybridBag-BoostEnsembleWithK-Means-SMOTE–ENNTechniqueforHandlingNoisyClass
ImbalancedData.Comput.J.2021,65,124–138.[CrossRef]
47. Seiffert,C.;Khoshgoftaar,T.M.;VanHulse,J.;Napolitano,A.RUSBoost:AHybridApproachtoAlleviatingClassImbalance.
IEEETrans.Syst.ManCybern.PartASyst.Hum.2009,40,185–197.[CrossRef]
48. Czarnowski,I.WeightedEnsemblewithone-classClassificationandOver-samplingandInstanceselection(WECOI):Anapproach
forlearningfromimbalanceddatastreams.J.Comput.Sci.2022,61,101614.[CrossRef]
49. Wang,H.;Xu,Q.;Zhou,L.LargeUnbalancedCreditScoringUsingLasso-LogisticRegressionEnsemble. PLoSONE2015,10,
e0117844.[CrossRef][PubMed]
50. Ariza-Garzón,M.-J.;Arroyo,J.;Segovia-Vargas,M.-J.;Caparrini,A.Profit-sensitivemachinelearningclassificationwithex-
planationsincreditrisk: Thecaseofsmallbusinessesinpeer-to-peerlending. Electron. Commer. Res. Appl. 2024,67,101428.
[CrossRef]
51. Turney,P.D.Cost-SensitiveClassification:EmpiricalEvaluationofaHybridGeneticDecisionTreeInductionAlgorithm.J.Artif.
Intell.Res.1994,2,369–409.[CrossRef]
52. Ling,C.X.;Yang,Q.;Wang,J.;Zhang,S.Decisiontreeswithminimalcosts. InProceedingsoftheTwenty-FirstInternational
ConferenceonMachineLearning,Banff,AB,Canada,4–8July2004.
53. Drummond,C.;Holte,R.C.Exploitingthecost(in)sensitivityofdecisiontreesplittingcriteria.InProceedingsoftheInternational
ConferenceonMachineLearning,Stanford,CA,USA,29June29–2July2000.

Mathematics2025,13,368 27of29
54. Domingos, P.Metacost: Ageneralmethodformakingclassifierscost-sensitive. InProceedingsoftheFifthACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining,SanDiego,CA,USA,15–18August1999.
55. Witten,I.H.;Frank,E.Datamining:PracticalmachinelearningtoolsandtechniqueswithJavaimplementations.AcmSigmodRec.
2002,31,76–77.[CrossRef]
56. Chai, X.; Deng, L.; Yang, Q.; Ling, C.X. Test-cost sensitive naive bayes classification. In Proceedings of the Fourth IEEE
InternationalConferenceonDataMining(ICDM’04),Brighton,UK,1–4November2004;IEEE:Piscataway,NJ,USA.
57. Sheng,V.S.;Ling,C.X.Thresholdingformakingclassifierscost-sensitive.InProceedingsoftheAssociationfortheAdvancement
ofArtificialIntelligence,Boston,MA,USA,16–20July2006.
58. Khan,S.H.;Hayat,M.;Bennamoun,M.;Sohel,F.A.;Togneri,R.Cost-SensitiveLearningofDeepFeatureRepresentationsFrom
ImbalancedData.IEEETrans.NeuralNetw.Learn.Syst.2017,29,3573–3587.[CrossRef][PubMed]
59. Lu,H.;Xu,Y.;Ye,M.;Yan,K.;Gao,Z.;Jin,Q.Learningmisclassificationcostsforimbalancedclassificationongeneexpression
data.BMCBioinform.2019,20,1–10.[CrossRef][PubMed]
60. Feng,F.; Li,K.C.; Shen,J.; Zhou,Q.; Yang,X.Usingcost-sensitivelearningandfeatureselectionalgorithmstoimprovethe
performanceofimbalancedclas-sification.IEEEAccess2020,8,69979–69996.[CrossRef]
61. Khandani,A.E.;Kim,A.J.;Lo,A.W.Consumercredit-riskmodelsviamachine-learningalgorithms. J.Bank. Financ. 2010,34,
2767–2787.[CrossRef]
62. Barboza,F.;Kimura,H.;Altman,E.Machinelearningmodelsandbankruptcyprediction.ExpertSyst.Appl.2017,83,405–417.
[CrossRef]
63. Yıldırım,M.;Okay,F.Y.;Özdemir,S.Bigdataanalyticsfordefaultpredictionusinggraphtheory.ExpertSyst.Appl.2021,176,
114840.[CrossRef]
64. Peykani,P.;Sargolzaei,M.;Sanadgol,N.;Takaloo,A.;Kamyabfar,H.Theapplicationofstructuralandmachinelearningmodels
topredictthedefaultriskoflistedcompaniesintheIraniancapitalmarket.PLoSONE2023,18,e0292081.[CrossRef][PubMed]
65. Chen, N.; Ribeiro, B. A consensus approach for combining multiple classifiers in cost-sensitive bankruptcy prediction. In
ProceedingsoftheAdaptiveandNaturalComputingAlgorithms:11thInternationalConference,ICANNGA2013,Lausanne,
Switzerland,4–6April2013;Proceedings11.Springer:Berlin/Heidelberg,Germany,2013.
66. Bahnsen,A.C.;Aouada,D.;Ottersten,B.Example-dependentcost-sensitivedecisiontrees.ExpertSyst.Appl.2015,42,6609–6619.
[CrossRef]
67. Zakaryazad,A.;Duman,E.Aprofit-drivenArtificialNeuralNetwork(ANN)withapplicationstofrauddetectionanddirect
marketing.Neurocomputing2016,175,121–131.[CrossRef]
68. Xia,Y.;Liu,C.;Liu,N.Cost-sensitiveboostedtreeforloanevaluationinpeer-to-peerlending.Electron.Commer.Res.Appl.2017,
24,30–49.[CrossRef]
69. Fiore,U.;DeSantis,A.;Perla,F.;Zanetti,P.;Palmieri,F.Usinggenerativeadversarialnetworksforimprovingclassification
effectivenessincreditcardfrauddetection.Inf.Sci.2017,479,448–455.[CrossRef]
70. Papouskova,M.;Hajek,P.Two-stageconsumercreditriskmodellingusingheterogeneousensemblelearning.Decis.SupportSyst.
2019,118,33–45.[CrossRef]
71. DeBock,K.W.;Coussement,K.;Lessmann,S.Cost-sensitivebusinessfailurepredictionwhenmisclassificationcostsareuncertain:
Aheterogeneousensembleselectionapproach.Eur.J.Oper.Res.2020,285,612–630.[CrossRef]
72. Hou,W.-H.;Wang,X.-K.;Zhang,H.-Y.;Wang,J.-Q.;Li,L.Anoveldynamicensembleselectionclassifierforanimbalanceddata
set:Anapplicationforcreditriskassessment.Knowl.-BasedSyst.2020,208,106462.[CrossRef]
73. Li,Z.;Zhang,J.;Yao,X.;Kou,G.Howtoidentifyearlydefaultsinonlinelending:Acost-sensitivemulti-layerlearningframework.
Knowl.-BasedSyst.2021,221,106963.[CrossRef]
74. Barbaglia,L.;Manzan,S.;Tosetti,E.ForecastingLoanDefaultinEuropewithMachineLearning.J.Financ.Econ.2021,21,569–596.
[CrossRef]
75. Gramegna,A.;Giudici,P.SHAPandLIME:AnEvaluationofDiscriminativePowerinCreditRisk.Front.Artif.Intell.2021,4,
752558.[CrossRef]
76. Zou,Y.;Gao,C.;Gao,H.BusinessFailurePredictionBasedonaCost-SensitiveExtremeGradientBoostingMachine.IEEEAccess
2022,10,42623–42639.[CrossRef]
77. Xing,J.;Chi,G.;Pan,A.Instance-dependentmisclassificationcost-sensitivelearningfordefaultprediction.Res.Int.Bus.Financ.
2024,69,102265.[CrossRef]
78. Wang,S.;Chi,G.Cost-sensitivestackingensemblelearningforcompanyfinancialdistressprediction.ExpertSyst.Appl.2024,255,
124525.[CrossRef]
79. CorreaBahnsen, A.; Aouada, D.; Ottersten, B.EnsembleofExample-DependentCost-SensitiveDecisionTrees. arXiv2015,
arXiv:1505.04637.
80. Pandove,D.;Rani,R.;Goel,S.Localgraphbasedcorrelationclustering.Knowl.-BasedSyst.2017,138,155–175.[CrossRef]

Mathematics2025,13,368 28of29
81. Freund,Y.;Schapire,R.E.ADecision-TheoreticGeneralizationofOn-LineLearningandanApplicationtoBoosting.J.Comput.
Syst.Sci.1997,55,119–139.[CrossRef]
82. Breiman,L.RandomForests.Mach.Learn.2001,45,5–32.[CrossRef]
83. Friedman,J.H.Greedyfunctionapproximation:Agradientboostingmachine.Ann.Stat.2001,29,1189–1232.[CrossRef]
84. Chen,T.; Guestrin,C.XGBoost: AScalableTreeBoostingSystem. InProceedingsofthe22ndACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August2016;AssociationforComputing
Machinery:SanFrancisco,Ca,USA;pp.785–794.
85. Prokhorenkova,L.;Gusev,G.;Vorobev,A.;Dorogush,A.V.;Gulin,A.CatBoost:Unbiasedboostingwithcategoricalfeatures.In
Proceedingsofthe32ndInternationalCon-ferenceonNeuralInformationProcessingSystems,Montréal,Canada,3–8December
2018;CurranAssociatesInc.:Montréal,QC,Canada;pp.6639–6649.
86. Rumelhart,D.E.;Hinton,G.E.;Williams,R.J.Learningrepresentationsbyback-propagatingerrors.Nature1986,323,533–536.
[CrossRef]
87. Kumar,V.;Kedam,N.;Sharma,K.V.;Mehta,D.J.;Caloiero,T.AdvancedMachineLearningTechniquestoImproveHydrological
Prediction:AComparativeAnalysisofStreamflowPredictionModels.Water2023,15,2572.[CrossRef]
88. Charoenwong, B.; Reddy, P. Using forensic analytics and machine learning to detect bribe payments in regime-switching
environments:EvidencefromtheIndiademonetization.PLoSONE2022,17,e0268965.[CrossRef][PubMed]
89. Nandi,A.K.;Randhawa,K.K.;Chua,H.S.;Seera,M.;Lim,C.P.Creditcardfrauddetectionusingahierarchicalbehavior-knowledge
spacemodel.PLoSONE2022,17,e0260579.[CrossRef][PubMed]
90. Carbo-Valverde, S.; Cuadros-Solas, P.; Rodríguez-Fernández, F. A machine learning approach to the digitalization of bank
customers:Evidencefromrandomandcausalforests.PLoSONE2020,15,e0240362.[CrossRef]
91. Hlongwane,R.;Ramabao,K.;Mongwe,W.Anovelframeworkforenhancingtransparencyincreditscoring:LeveragingShapley
valuesforinterpretablecreditscorecards.PLoSONE2024,19,e0308718.[CrossRef]
92. Quach,A.C.AExtensionsandImprovementstoRandomForestsforClassification;UtahStateUniversity:Logan,Utah,2017.
93. Wyrobek,J.;Kluza,K.EfficiencyofGradientBoostingDecisionTreesTechniqueinPolishCompanies’BankruptcyPrediction.
In Proceedings of the Information Systems Architecture and Technology: Proceedings of 39th International Conference on
InformationSystemsArchitectureandTechnology–ISAT2018:PartIII,Wrocław,Poland,16–18September2019;pp.24–35.
94. Freund,Y.BoostingaWeakLearningAlgorithmbyMajority.Inf.Comput.1995,121,256–285.[CrossRef]
95. Breiman,L.Baggingpredictors.Mach.Learn.1996,24,123–140.[CrossRef]
96. Lu,M.;Hou,Q.;Qin,S.;Zhou,L.;Hua,D.;Wang,X.;Cheng,L.AStackingEnsembleModelofVariousMachineLearningModels
forDailyRunoffForecasting.Water2023,15,1265.[CrossRef]
97. Ainan, U.H.; Por, L.Y.; Chen, Y.-L.; Yang, J.; Ku, C.S. Advancing Bankruptcy Forecasting with Hybrid Machine Learning
Techniques:InsightsfromanUnbalancedPolishDataset.IEEEAccess2024,12,1.[CrossRef]
98. Aiken,J.M.;DeBin,R.;Hjorth-Jensen,M.;Caballero,M.D.PredictingtimetograduationatalargeenrollmentAmericanuniversity.
PLoSONE2020,15,e0242334.[CrossRef][PubMed]
99. Du, H.; Lv, L.; Wang, H.; Guo, A.Anovelmethodfordetectingcreditcardfraudproblems. PLoSONE2024, 19, e0294537.
[CrossRef]
100. Jabeur,S.B.;Gharib,C.;Mefteh-Wali,S.;Arfi,W.B.CatBoostmodelandartificialintelligencetechniquesforcorporatefailure
prediction.Technol.Fore-Cast.Soc.Chang.2021,166,120658.[CrossRef]
101. Dorogush,A.V.;Ershov,V.;Gulin,A.CatBoost:Gradientboostingwithcategoricalfeaturessupport.arXiv2018,arXiv:1810.11363.
102. Lu,H.;Hu,X.EnhancingFinancialRiskPredictionforListedCompanies:ACatboost-BasedEnsembleLearningApproach.J.
Knowl.Econ.2023,15,1–17.[CrossRef]
103. Enkhtuya,T.;Kang,D.K.BankruptcyPredictionwithExplainableArtificialIntelligenceforEarly-StageBusinessModels.Int.J.
InternetBroadcast.Commun.2023,15,58–65.
104. Peykani,P.;Sargolzaei,M.;Botshekan,M.H.;Oprean-Stan,C.;Takaloo,A.OptimizationofAssetandLiabilityManagementof
BankswithMinimumPossibleChanges.Mathematics2023,11,2761.[CrossRef]
105. Peykani,P.;Sargolzaei,M.;Takaloo,A.;Sanadgol,N.Investigatingthemonetarypolicyriskchannelbasedonthedynamic
stochasticgeneralequilibriummodel:EmpiricalevidencefromIran.PLoSONE2023,18,e0291934.[CrossRef][PubMed]
106. Marino,M.J.Chapter3—StatisticalAnalysisinPreclinicalBiomedicalResearch.InResearchintheBiomedicalSciences;Williams,M.,
Curtis,M.J.,Mullane,K.,Eds.;AcademicPress:Cambridge,MA,USA,2018;pp.107–144.
107. Riffenburgh,R.H.ChapterSummaries.InStatisticsinMedicine,2nded.;Riffenburgh,R.H.,Ed.;AcademicPress:Burlington,MA,
USA,2006;pp.533–580.
108. Friedman,M.TheUseofRankstoAvoidtheAssumptionofNormalityImplicitintheAnalysisofVariance.J.Am.Stat.Assoc.
1937,32,675–701.[CrossRef]
109. Hull,J.MachineLearninginBusiness:AnIntroductiontotheWorldofDataScience;AmazonDistribution:London,UK,2020.

Mathematics2025,13,368 29of29
110. Altman,E.I.Financialratios,discriminantanalysisandthepredictionofcorporatebankruptcy. J.Financ. 1968,23,589–609.
[CrossRef]
111. Carton,R.B.;Hofer,C.W.MeasuringOrganizationalPerformance:MetricsforEntrepreneurshipandStrategicManagementResearch;
EdwardElgarPublishing:Cheltenham,UK,2006.
112. Peykani,P.;Sargolzaei,M.;Takaloo,A.;Valizadeh,S.TheEffectsofMonetaryPolicyonMacroeconomicVariablesthroughCredit
andBalanceSheetChannels:ADynamicStochasticGeneralEquilibriumApproach.Sustainability2023,15,4409.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.