---
conversion_metadata:
  converted_at: "2026-07-21T14:07:05Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Luong & Xie.pdf"
  source_pdf_sha256: "0eb20ae488844cfbc78e6e0375a08f15c6f91f4fd7235563057479a0eac07928"
  page_count: 20
  markdown_char_count: 175782
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

The Journal of Finance and Data Science 12 (2026) 100195

Contents lists available at ScienceDirect

The Journal of Finance and Data Science

journal homepage: www.keaipublishing.com/en/journals/jfds

Research Article
Explainable ensemble machine learning for financial transaction 
fraud detection: Insights from XGBoost and deep neural networks
Nguyen Duy Anh Luong , Shengkun Xie *
Global Management Studies, Ted Rogers School of Management, Toronto Metropolitan University, 350 Victoria Street, Toronto, ON M5B2K3, 
Canada

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Fraud detection 
Machine learning 
XGBoost
Deep learning 
Ensemble models

1.  Introduction

The rapid digitalization of financial services has enhanced transaction speed and accessibility but 
also amplified exposure to fraud activities that undermine institutional integrity and consumer 
trust. Effective fraud detection requires analytical frameworks that are not only accurate and 
adaptive but also interpretable and compliant with financial regulations. This study develops a 
scalable, explainable machine learning framework for detecting fraud financial transactions using 
a hybrid ensemble of Extreme Gradient Boosting (XGBoost) and Deep Neural Networks (DNN). 
The proposed model integrates transactional, temporal, and identity-linked features to capture 
behavioral and contextual patterns in large-scale, high-frequency data. To address the extreme 
class imbalance inherent in fraud detection, we evaluate multiple strategies including focal loss, 
class weighting, and threshold optimization. Model transparency is enhanced through SHAP-
based interpretability analysis, providing granular insights into the feature interactions driving 
fraud risk. Empirical evaluation on a real-world transaction dataset demonstrates that the hybrid 
ensemble achieves superior detection accuracy and recall relative to baseline models while 
maintaining explainability suitable for regulated financial environments. The results highlight the 
potential of combining interpretable machine learning with adaptive ensemble learning to 
enhance resilience and trustworthiness in modern financial risk management systems.

The rapid digitalization of financial services (Broby, 2021) has fundamentally transformed the way individuals and businesses 
conduct transactions across e-commerce, mobile payments, and on-line banking. While these innovations have enabled unprecedented 
convenience and efficiency, they have also introduced new vulnerabilities, exposing financial systems to increasingly sophisticated 
fraud activities. Credit card fraud, in particular, remains one of the most pervasive and costly financial crimes, causing direct monetary 
losses and eroding public trust in financial institutions (Ding et al., 2025). Accurately identifying fraud is challenging because mali-
cious activities are often concealed within massive streams of legitimate transactions, making traditional detection approaches 
insufficient.

Early fraud detection systems were predominantly rule-based, relying on static thresholds and handcrafted anomaly detection rules 
to flag suspicious transactions (Bolton and Hand, 2002). Although such approaches were initially effective, they fail to adapt to

* Corresponding author. Toronto Metropolitan University, 350 Victoria Street, Toronto, ON M5B2K3,Canada. 1-(416)-9795000.

E-mail addresses: nguyenduyanh.luong@torontomu.ca (N.D. Anh Luong), shengkun.xie@torontomu.ca (S. Xie).
Peer review under the responsibility of KeAi Communications Co., Ltd.

https://doi.org/10.1016/j.jfds.2026.100195
Received 3 November 2025; Received in revised form 29 May 2026; Accepted 2 June 2026
Available online 9 June 2026
2405-9188/© 2026 The Authors. Publishing services by Elsevier B.V. on behalf of KeAi Communications Co. Ltd. This is an open access article under 
the CC BY license (http://creativecommons.org/licenses/by/4.0/).

---

<!-- PAGE 2 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

evolving fraud patterns. Fraudsters continuously modify their tactics, rendering fixed rules obsolete and leading to high false-positive 
rates while allowing genuine fraud cases to go undetected (Ding et al., 2025). These limitations have driven a paradigm shift toward 
machine learning (ML) and deep learning (DL), which can automatically learn complex, non-linear patterns from data, adapt to 
emerging fraud tactics, and uncover relationships that are difficult to model manually (Roseline et al., 2022).

ML has shown particular strength in analyzing large-scale, high-dimensional transaction data (Talukder et al., 2024; Zhang et al., 
2019). Cost-sensitive learning has been proposed to explicitly account for the financial consequences of misclassification, striking a 
balance between minimizing false positives and maximizing fraud detection (Roseline et al., 2022). To address scalability re-
quirements, distributed learning frameworks have been developed to process high-velocity data streams in near real time (Theo-
dorakopoulos et al., 2025). In addition, various algorithms have been explored: support vector machines and neural networks 
effectively capture non-linear relationships, whereas gradient boosting methods such as XGBoost offer robust performance and strong 
predictive accuracy for tabular, structured data (Noviandy et al., 2023).

Despite these advances, fraud detection still faces several challenges. One of the most persistent is the extreme class imbalance 
between legitimate and fraud transactions, where fraud often accounts for less than 1% of all records (Breskuviene and Dzemyda, 
2024). This imbalance biases models toward the majority class and reduces recall for fraud cases, which is particularly costly in 
real-world applications. Existing solutions include active learning to prioritize informative samples (Riskiyadi, 2024), ensemble 
boosting methods tailored to minority classes, and resampling strategies such as SMOTE and undersampling to rebalance the data 
distribution (Ludera, 2021).

Another major challenge is the high dimensionality and structural complexity of financial transaction data, which involve non-
linear feature interactions. Feature engineering has therefore become central to improving model performance, with techniques 
such as time-window aggregation to capture sequential spending behavior (Saputra et al., 2019). Recent research highlights the 
promise of hybrid ML–DL approaches, which combine the predictive power of deep neural networks with the interpretability of 
tree-based models (Gandhar et al., 2024). Advanced feature selection frameworks that integrate statistical and evolutionary methods 
have also been proposed to reduce redundant features, lower computational cost, but retain discriminative power (Siam et al., 2025).
DL has emerged as a dominant paradigm in recent years due to its ability to automatically extract high-level representations from 
raw transaction data (Du et al., 2023; Zioviris et al., 2024). Deep neural networks have been shown to scale well to distributed systems 
and maintain generalization in dynamic environments (Prasad and Srikanth, 2024). Furthermore, their ability to perform anomaly 
detection and representation learning makes them highly effective when fraud patterns evolve over time (Mehbodniya et al., 2021). 
Nevertheless, DL models often require large volumes of labeled data, demand substantial computational resources, and suffer from 
limited interpretability, posing challenges for deployment in highly regulated financial environments (Mienye et al., 2024).

Building on these insights, the present study addresses these gaps through a comprehensive investigation of supervised ML ap-
proaches for fraud detection of financial transactions. Specifically, the study (i) systematically compares seven ML models, including 
logistic regression, random forests, XGBoost, shallow and deep neural networks, and a novel hybrid ensemble; (ii) evaluates imbalance 
handling strategies, such as class weighting, focal loss, and threshold optimization; (iii) incorporates transactional, temporal, and 
identity-linked features to improve contextual predictive power; and (iv) applies SHAP-based interpretability analysis to ensure 
transparency and regulatory compliance. The main contributions of this research are threefold: (1) a detailed characterization of fraud 
patterns across transactional, temporal, and identity dimensions; (2) a hybrid ensemble model integrating Enhanced XGBoost and a 
Deep Neural Network, achieving strong predictive performance on the dataset we consider; and (3) an adaptive evaluation framework 
that integrates model interpretability and dynamic threshold optimization to support practical application in fraud detection systems.

2.  Related work

Research on fraud detection has largely focused on supervised ML approaches, aiming to address the challenges posed by real-
world datasets that are highly imbalanced, high-dimensional, complex and often noisy. Existing studies can be broadly classified 
into four themes: (i) model selection, (ii) imbalance-handling techniques, (iii) feature engineering, and (iv) the integration of identity-
based variables to improve predictive power of the model.

Supervised learning models remain fundamental for most modern fraud detection systems (Bin Sulaiman, Schetinin and Sant, 2022; 
George et al., 2025). These models learn parameters or hyper-parameters from labeled historical data and build the model to predict 
whether new transactions are fraud or legitimate. A notable advancement in this area is the distributed deep neural network (DDNN) 
proposed by Lei et al. (2023), which balances predictive accuracy with user privacy by allowing institutions to train local models and 
share only model parameters with a central server. This federated-style approach not only preserves data confidentiality but also 
improves efficiency through distributed computation, yielding superior accuracy, precision, recall, and F1-scores compared to 
centralized models (Xia and Saha, 2025).

Interpretable models such as decision trees and random forests have also been widely used in fraud detection (Lee et al., 2025; Sun, 
2025; Wajgi et al., 2024).Decision trees are valued for their transparency but are prone to overfitting, whereas random forests mitigate 
this issue through tree aggregation and hyperparameter tuning (Shah and Sharma, 2023). However, both approaches are sensitive to 
severe class imbalance. A comprehensive evaluation of 66 algorithm–resampling combinations by Alfaiz and Fati (2022) highlighted 
that pairing strong classifiers such as CatBoost with effective undersampling methods like AllKNN can achieve state-of-the-art per-
formance in terms of F1-score, recall, and AUC.

Class imbalance remains one of the most critical obstacles in fraud detection (Baisholan et al., 2025; Velarde et al., 2023). When 
fraud cases account for less than 1% of transactions, models are significantly biased toward the majority class, leading to poor recall. 
Numerous resampling and reweighting techniques have been proposed to mitigate this challenge. For example, Alamri and Ykhlef

2

---

<!-- PAGE 3 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

(2024) introduced BCB-SMOTE, a hybrid method combining Tomek links, clustering, and borderline synthetic oversampling, which 
achieved an F1-score of 85.2% while reducing overlap between classes. Similarly, Ileberi et al. (2021) showed that combining SMOTE 
with AdaBoost improved detection rates across classifiers, and Lahbiss and Chtouki (2024) reported that SMOTE-ENN with advanced 
models such as Random Forest and Long Short Term Memory (LSTM) significantly enhanced AUC-ROC. Moreover, Jiao et al. (2022) 
proposed DES-ICD, which integrates adaptive oversampling (AnnSMOTE) with dynamic ensemble selection to handle both class 
imbalance and concept drift. By generating minority samples that reflect new concepts and selecting classifiers based on local 
neighborhood performance, DES-ICD achieved superior accuracy and recall across multiple real and synthetic datasets.These findings 
highlight that careful design of imbalance handling techniques is crucial for achieving high recall without sacrificing precision.

Beyond class imbalance, feature engineering plays a pivotal role in fraud detection (Alamri and Ykhlef, 2024; Sharma et al., 2025). 
The inclusion of behavioral and identity-based attributes has been shown to significantly improve model performance. For instance, 
Shimin et al. (2020) demonstrated that combining financial transaction data with identity-linked features (e.g., device type, email 
domain) significantly enhanced XGBoost's ROC-AUC to 0.942 on the IEEE-CIS dataset. Similarly, Lucas et al. (2019) applied Hidden 
Markov Models to capture sequential spending behavior, which, when combined with Random Forest, improved precision–recall AUC. 
Bahnsen et al. (2016) further extended this line of work by modeling periodic spending patterns with von Mises distributions, yielding 
a 13% reduction in financial losses. These studies collectively underscore that well-designed feature engineering strategies are 
essential for building robust and discriminative fraud detection models.

Ensemble and hybrid learning methods represent a growing trend in fraud detection research. Carcillo et al. (2021) combined 
unsupervised anomaly detection with supervised learning, feeding outlier scores as features into classifiers to enable multi-level 
detection. Dynamic ensemble selection approaches, such as the one proposed by Achakzai and Peng (2023), adaptively choose 
classifiers based on local competence and consistently outperform static ensembles. Hybrid models have also demonstrated promise; 
for example, Jahnavi et al. (2024) combined decision trees with logistic regression to achieve 98.1% accuracy for the data they 
considered, while Chaurasia, Kesharwani, Sharma, Sharma, and Chugh (2024) confirmed that XGBoost paired with data balancing 
strategies offers superior recall in rare-event detection.

Several comparative reviews have synthesized findings across models and datasets. Patel et al. (2024) reported that while deep 
neural networks often achieve the highest accuracy (up to 98.9%), simpler models such as logistic regression and Naive Bayes remain 
competitive due to their interpretability and high efficiency. Similarly, Bhardwaj et al. (2024) found that deep neural networks trained 
using the Adam optimizer reached 99.4% accuracy on the European credit card dataset and were computationally efficient, making 
them well-suited for large-scale data implementation.

Taken together, prior work demonstrates that deep learning and advanced ensemble approaches frequently deliver superior 
predictive performance, yet simpler models retain value for their interpretability, scalability, and ease of application. Despite these 
advances, few studies have simultaneously addressed all major challenges, including class imbalance, feature selection, interpret-
ability, and integration of identity-based features, within a unified framework. This work seeks to close this gap by systematically 
comparing multiple supervised ML models, integrating advanced imbalance handling techniques, and leveraging feature engineering 
to deliver a scalable, interpretable, and robust fraud detection framework.

3.  Materials and methods

This study adopts a systematic and rigorous methodology for evaluating supervised machine learning models in the context of 
financial fraud detection. The proposed framework is explicitly designed to address two major challenges inherent to large-scale 
financial transaction data: high dimensionality and severe class imbalance. The methodological design is organized into four 
sequential phases, data preprocessing, imbalance mitigation, model training with hyperparameter optimization, and post-hoc inter-
pretability analysis. Each phase is implemented to ensure both model robustness and transparency. The following sections provide 
detailed descriptions of the procedures and techniques applied within each phase.

3.1.  Data and its description

The data used in this study is the IEEE-CIS fraud detection dataset, released through a Kaggle competition in collaboration with 
Vesta, a global fraud prevention company. This data reflects real-world e-commerce environments with anonymized transaction and 
identity information, and its very suited for testing algorithms and computational framework designed for fraud detection in financial 
transactions. The training set contains over 590,000 records, of which only about 3.5% are labeled as fraud, while the test set contains 
similar features but does not include fraud labels. The dataset can be downloaded from the official Kaggle competition portal (https:// 
www.kaggle.com/competitions/ieee-fraud-detection/data).

Two main files were provided for both training and test: transaction.csv, which contains transaction-level attributes, and identity. 
csv, which includes device and identity-related variables. These files were merged using the TransactionID field to produce a 
comprehensive view of each transaction. The features can be grouped into several categories, as summarized in Table 1.

Beyond the feature types, it is also important to consider the overall statistical profile of the dataset. Basic descriptive statistics are 
provided in Table 2. The dataset is highly imbalanced, with fraud cases representing only a small fraction of transactions. Transaction 
amounts vary widely, ranging from a few cents to over $10,000, with a median value of approximately $68. Additionally, many 
identity-related fields contain substantial missing values, highlighting the challenges inherent in real-world fraud detection problems.
These characteristics emphasize the dual challenges of extreme class imbalance and data high-dimensionality. These insights

directly informed the preprocessing strategies and modeling decisions described in the following sections.

3

---

<!-- PAGE 4 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Table 1
Summary of feature groups in the IEEE-CIS dataset.

Feature Group
Transaction features 
Card attributes 
Address codes 
Engineered features 
Email domains 
Identity features

Description/Examples
TransactionAmt, TransactionDT, ProductCD
card1–card6 (e.g., card type, issuer, category)
addr1, addr2 (geographic location codes)
C1–C14, D1–D15, V1–V339 (anonymized signals) 
P_emaildomain, R_emaildomain
DeviceType, DeviceInfo, id12–id38 (browser, OS, network)

3.2.  Data preprocessing

The training dataset was constructed by merging transaction dataset and identity dataset on the TransactionID field, thereby 
integrating transaction-level payment attributes with device- and identity-related features. This merging step was crucial to capture 
both behavioral and contextual features that can distinguish fraud from legitimate transactions. To address missing data, categorical 
variables were imputed with the string “missing” so that models could treat absence of information as an additional informative 
category. For numerical attributes, two different strategies were adopted depending on the model type. For tree-based methods such as 
XGBoost and Random Forest, missing values were retained as NaN, allowing these models to handle missingness natively during split 
optimization.

Since neural network models (both ANN and DNN) cannot process missing values directly, for all neural network-based models, 
numerical features with missing values were imputed using the median of each feature computed from the training set. Median 
imputation was chosen due to its robustness to skewed distributions and extreme values, which are common in financial transaction 
data. After imputation, numerical features were standardized using z-score normalization to ensure stable and efficient training of the 
neural networks. This hybrid preprocessing strategy ensures that each model type operates under conditions best suited to its un-
derlying assumptions while maintaining consistency across the experimental pipeline.

Categorical features, including ProductCD, card4, and DeviceType, were transformed using label encoding to convert string cat-
egories into numerical form while preserving their distinct identities. Although more sophisticated encoders (e.g., target or one-hot 
encoding) could be applied, label encoding was selected to maintain consistency across a high-dimensional feature space and 
reduce memory overhead. In addition, a temporal feature, hour_of_day, was derived from the continuous TransactionDT timestamp to 
capture periodic spending behaviors that may indicate fraud, such as late-night or off–hour activity.

Following data preprocessing, the dataset was partitioned into training and validation subsets using an 80/20 stratified split. 
Stratification ensured that the proportion of fraud to legitimate transactions was maintained in both sets, enabling a fair and repre-
sentative evaluation. The computational details of this preprocessing and splitting are presented in Algorithm 1. This approach pre-
served the natural distribution of the data, which is essential for imbalanced classification problems. However, it also retained 
potential noise from weak or redundant features, meaning that subsequent feature selection and model regularization were critical for 
improving robustness.

4

---

<!-- PAGE 5 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Table 2
Descriptive statistics of the IEEE-CIS training dataset.

Statistic
Total records
Fraud proportion
Transaction amount range 
Median transaction amount 
Number of features (after merge)

Value

~590,000
3.5%
$0.01 – $10,000+ 
$68
434

3.3.  Handling class imbalance

Fraud transactions represented only about 3.5% of the dataset, creating a severe class imbalance that posed a significant challenge 
for model training. If left unaddressed, most classifiers would become biased toward predicting the majority class (legitimate trans-
actions), thereby achieving deceptively high accuracy but failing to identify the rare fraud cases that matter most in practice. To 
mitigate this imbalance, cost-sensitive learning approaches were adopted. For gradient boosting models such as XGBoost, the 
parameter value of scale_pos_weight was set to the ratio of majority to minority class instances, thereby instructing the algorithm to 
assign higher importance to fraud cases during training. For neural networks, a focal loss function was used. Unlike traditional cross-
entropy, focal loss dynamically down-weights well-classified examples and focuses learning on harder, misclassified fraud cases. This 
adaptation is particularly effective when fraud behavior exhibits high diversity and overlaps with legitimate transaction patterns. This 
strategy preserved the natural class distribution of the dataset and avoided the introduction of synthetic artifacts, which are often a 
drawback of oversampling or SMOTE-based techniques. However, while cost-sensitive methods improve recall, they may not fully 
resolve imbalance in scenarios where the decision boundary between classes is highly non-linear or overlapping.

3.4.  Machine learning models

In this section, we provide a brief overview of the machine learning models used in this study to ensure the paper remains self-
contained. Five models were selected based on their suitability for handling structured, imbalanced data classification problems
and their diversity in algorithmic approach. Let {x 
is the p-
dimensional feature vector, and y 
i ∈ {0, 1} is the class label of fraud or non-fraud. We first consider Logistic Regression (LR), a linear 
baseline model that estimates the conditional probability of the positive (fraud) class as

i=1 denote a training set of financial transaction data, where x 
i ; y 
i }n

i ∈ ℝ p

i = P(y i = 1|x i ) = σ(w ⊤ x i + b); 
̂y

(1)

where σ(z) =  1
rameters w and b can be estimated using the least squares method or maximum likelihood estimation.

1+e(cid:0) z  is the logistic sigmoid function, and ̂y

i ∈ [0; 1] represents the predicted probability of fraud. The unknown pa-

To capture non-linear patterns, we also apply a Random Forest (RF) model, which is an ensemble of T decision trees {h 
t }T

t=1. Each 
tree is trained on a bootstrap sample of the data with random feature subsampling. The final prediction is the average of individual tree 
predictions of probability,

̂y 
i =

1
T

∑ T

h t (x i );

t=1

where h

t (x

i ) ∈ [0, 1] denotes the probability assigned by tree t.

As a more powerful alternative, XGBoost uses gradient boosting to iteratively construct an additive model,

i = ̂y(t(cid:0) 1) 
̂y(t)

i

+ f t(x i );

where f

t represents the regression tree added at iteration t. The objective function minimized at each step is

∑ n

L (t) =

ℓ(y i ; ̂y(t)

i ) + Ω(f t);

(2)

(3)

(4)

i=1

where ℓ(⋅) is a differentiable loss function, such as logistic loss, and Ω(⋅) is a regularization term penalizing tree complexity to prevent 
overfitting.

We further explore neural network-based approaches. The Artificial Neural Network (ANN) considered here is a shallow feed-
1 ), where ϕ(⋅) is an activa-

forward network with a single hidden layer. For hidden representations computed as h ¼ ϕ(W 
tion function such as ReLU, the predicted probability is given by

i þ b

1 x

i = σ(w⊤ 
̂y

2 h + b 2 ):

(5)

Finally, we utilize a Deep Neural Network (DNN) with L hidden layers. The prediction is expressed as

5

---

<!-- PAGE 6 -->

N.D. Anh Luong, S. Xie

) 
(cid:0) 
f (L) ∘f (L(cid:0) 1) ∘⋯∘f (1) (x i ) 
̂y 
; 
i = σ

The Journal of Finance and Data Science 12 (2026) 100195

(6)

where f (l) 
function defined as follows

(⋅) represents the non-linear transformation at layer l. To address class imbalance, the DNN is trained using the focal loss

L focal = (cid:0)

∑ n

i ) γ 
α(1 (cid:0)  ̂y

y i loĝy

i + (1 (cid:0)  α)̂y γ

i (1 (cid:0)  y i )log(1 (cid:0)  ̂y 
i );

(7)

i=1

where α balances the class weights and γ down-weights well-classified examples, focusing learning on harder cases.

The inclusion of these models provided both breadth and depth in evaluation. Logistic regression offered transparency and 
interpretability, serving as a benchmark for assessing gains from more complex models. Random forests and XGBoost captured non-
linear interactions through ensemble learning, with XGBoost effectively handling imbalance via class weighting. Neural networks 
represented higher-capacity learners: the ANN provided a shallow deep learning baseline, while the DNN leveraged deeper archi-
tectures and focal loss for improved representation learning in imbalanced fraud detection tasks.

To combine the strengths of gradient boosting and deep neural networks, a hybrid ensemble model was constructed using a 
weighted averaging strategy. In this approach, XGBoost and the DNN were trained independently on the same training data, and their 
predicted probabilities were combined using a weighted linear combination. Specifically, the final ensemble prediction is given by

̂y 
i = λ⋅̂yXGB

i + (1 (cid:0)  λ)⋅̂yDNN

i

;

(8)

where ̂y

XGB
i

and ̂y

DNN
i

denote the predicted probabilities from XGBoost and the DNN respectively, and λ is a weighting parameter.

In this hybrid approach, XGBoost contributes structured feature learning and interpretability, while the DNN captures non-linear 
patterns, enabling robust fraud detection in imbalanced and high-dimensional environments. The weights (0.6 for XGBoost, 0.4 for 
DNN) were selected based on validation performance, giving slightly greater influence to XGBoost due to its stability on tabular data 
while still leveraging the DNN's capacity to refine decision boundaries. This weighting scheme produced the best balance between 
recall and precision, ensuring that the ensemble remains both accurate and adaptable for practical deployment.

For further clarification, in Algorithm 2, “tuning the threshold to maximize F1 on (y

val )” refers to selecting an optimal decision 
threshold that converts predicted probabilities into binary labels. Instead of using a fixed threshold (e.g., 0.5), a range of candidate 
thresholds is evaluated, and the one that maximizes the F1-score on the validation set is chosen. This step is particularly important in 
imbalanced settings such as fraud detection, where the default threshold often yields poor recall for the minority class. Optimizing the 
threshold with respect to the F1-score enables a better balance between precision and recall, improving detection performance. 
Importantly, threshold tuning is a post-training calibration step rather than part of model learning. Model parameters are trained 
exclusively on the training set, while the validation set is used only to determine the operating point on the precision–recall curve. No 
parameter updates are performed on the validation data. To limit potential bias, the validation set is strictly separated from training 
data, and the selected threshold is fixed before final evaluation. This practice is standard in imbalanced classification and reflects real-
world deployment, where decision thresholds are calibrated to meet operational objectives. While more conservative approaches (e.g., 
nested cross-validation) could further reduce bias, they are computationally expensive at this scale.

6

---

<!-- PAGE 7 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

3.5.  Model architecture and hyperparameter configuration

The Artificial Neural Network (ANN) model consists of two hidden layers with 128 and 64 neurons, respectively. Both hidden layers 
employ the ReLU activation function, followed by dropout layers with a rate of 0.3 to mitigate overfitting. The output layer contains a 
single neuron with a sigmoid activation function to produce probabilistic predictions for binary classification. The model is trained 
using the Adam optimizer with a learning rate of 0.001 and binary cross-entropy loss. Training is conducted for up to 20 epochs with a 
batch size of 512, and early stopping with a patience of 3 epochs is applied to prevent overfitting.

The Deep Neural Network (DNN) is designed as a deeper architecture with three hidden layers containing 512, 256, and 128 
neurons, respectively. Instead of standard ReLU activation, LeakyReLU is employed to mitigate the “dying ReLU” problem and improve 
gradient propagation in deeper networks. Each hidden layer is followed by batch normalization and dropout with rates of 0.4, 0.4, and 
0.3, respectively, to enhance training stability and generalization. The output layer uses a sigmoid activation function to produce 
probability estimates. The model is trained using the Adam optimizer with a learning rate of 0.001 and focal loss, which is particularly 
effective in handling class imbalance by emphasizing difficult-to-classify samples. Training is performed for up to 20 epochs with a 
batch size of 1024, with early stopping and learning rate reduction applied to improve convergence.

The Random Forest model consists of 100 decision trees with a maximum depth of 15. Class imbalance is handled through built-in 
class weighting, ensuring that minority class samples receive higher importance during training. The model utilizes all available CPU 
cores to improve computational efficiency. The choice of tree depth and number of estimators reflects a balance between model 
expressiveness and overfitting control.

Regularization is incorporated across all models to enhance generalization performance. In the neural network models, dropout is 
used to reduce overfitting by preventing co-adaptation of neurons, while batch normalization stabilizes training and accelerates 
convergence. Class imbalance is addressed through cost-sensitive learning techniques, including class weighting and focal loss, which 
adjust the learning process without modifying the original data distribution. Early stopping is applied to prevent overfitting by halting 
training when validation performance no longer improves.

Regarding activation functions, ReLU is used in the ANN due to its computational efficiency and strong empirical performance. In 
the deeper DNN architecture, LeakyReLU is adopted to avoid inactive neurons and improve gradient flow. The sigmoid activation 
function is used exclusively in the output layer, as it is standard for binary classification tasks and enables probabilistic interpretation 
of predictions.

Hyperparameters were selected based on a combination of prior literature, empirical validation, and computational considerations. 
While systematic hyperparameter tuning methods such as grid search or Bayesian optimization could potentially yield marginal 
performance improvements, these approaches are computationally expensive given the scale and dimensionality of the data. Instead, 
we adopt a pragmatic approach by using well-established configurations and validating them through stratified train-validation splits. 
Furthermore, techniques such as early stopping and adaptive learning rate scheduling provide implicit tuning during training, allowing 
the models to converge to suitable parameter settings efficiently.

3.6.  Experimental design

The methodological framework discussed in the previous sections laid the foundation for a structured experimental design. Having 
defined the preprocessing pipeline, imbalance handling strategies, and predictive models, the next step was to implement these 
methods in a controlled series of experiments. These experiments were carefully structured to test models of varying complexity under 
realistic fraud detection conditions.

3.6.1.  Objectives and rationale

The primary objective of the experiments was to evaluate the effectiveness of various supervised machine learning models for 
detecting fraud transactions using the IEEE-CIS dataset. Three considerations guided the experimental design. First, simple and 
interpretable models were assessed as baseline approaches. Second, ensemble methods, including Random Forest and XGBoost, were 
examined for their ability to improve discrimination under severe class imbalance. Third, deep neural networks and hybrid ensembles 
were investigated to capture non-linear patterns potentially missed by tree-based methods.

This approach reflects the operational priorities of fraud detection, which require a balance between predictive accuracy, inter-
pretability, scalability, and computational efficiency. The experiments followed a staged workflow: dataset preparation and pre-
processing, class imbalance mitigation, evaluation of increasingly complex model families, and performance assessment using metrics 
appropriate for imbalanced classification. The overall workflow and the range of models are illustrated in Fig. 1.

Scalability and computational efficiency were key factors in both model selection and experimental design, given the large scale 
and high dimensionality of the data. These considerations influenced not only which models were evaluated, but also how they were 
configured and compared.

Model selection was guided by the need to balance predictive performance with computational feasibility. Tree-based ensemble 
models such as Random Forest and XGBoost were chosen because they scale efficiently to large tabular datasets and provide strong 
performance with relatively low training complexity. In particular, XGBoost incorporates parallelized tree construction and optimized 
memory usage, making it suitable for high-volume transactional data. Random Forest serves as a computationally efficient baseline, 
enabling comparison with more advanced models while maintaining stable and scalable training behavior.

Deep learning models, including ANN and DNN, were introduced to capture complex non-linear relationships that may not be fully 
exploited by tree-based methods. However, these models are computationally more expensive due to iterative gradient-based

7

---

<!-- PAGE 8 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Fig. 1. Staged workflow of the experimental design, from dataset preparation to evaluation.

Table 3
Comparison of performance metrics due to different imbalance handling strategies.

Method
SMOTE + ensemble
Class weighting þ focal loss (proposed)

ROC-AUC

0.9037
0.9638

PR-AUC

0.6068
0.6582

F1-score

Precision

0.60
0.74

0.73
0.78

Recall

0.51
0.69

optimization and the requirement for feature scaling. To ensure computational efficiency, the neural network architectures were 
constrained in depth and size, and training was controlled using early stopping, batch processing, and learning rate scheduling.

In addition to training efficiency, inference time was explicitly evaluated to assess the suitability of each model for real-time 
deployment. Inference latency was measured as the average prediction time per transaction (milliseconds per transaction) on the 
validation set. This metric is particularly important in fraud detection systems, where models must process large volumes of trans-
actions with minimal delay. The measured inference times for all models are reported in Table 4.

The hybrid ensemble model was explicitly designed to balance scalability and predictive performance. XGBoost contributes effi-
cient feature learning and fast inference, while the DNN enhances predictive capability through non-linear representation learning. 
While neural network models incur higher inference cost due to forward propagation through multiple layers, tree-based models such

Table 4
Comparative performance of models on fraud detection task, including external benchmark and inference time.

Model

Accuracy

Recall

Precision

F1-Score

ROC-AUC

PR-AUC

Inference Time
(ms/transaction)

Logistic regression (LR)
Random forest (RF)
XGBoost (XGB)
Enhanced XGBoost (XGB-adv)
Artificial neural network (ANN)
Deep neural network (DNN)
XGB + DNN ensemble
OLightGBM (Taha and Malebary (2020))

77%
94%
89%
95%
98%
98%
98%
98%

0.69
0.68
0.81
0.83
0.43
0.51
0.69
–

0.18
0.45
0.35
0.55
0.59
0.63
0.74
0.5695

0.7959
0.9122
0.9276
0.9628
0.9160
0.9182
0.9638
0.9288

0.1772
0.5856
0.6187
0.7676
0.6403
0.6582
0.7897
–

0.02
0.15
0.08
0.09
0.25
0.30
0.35
–

0.10
0.33
0.22
0.42
0.91
0.82
0.78
0.97

8

---

<!-- PAGE 9 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

as XGBoost provide lower latency through efficient decision-tree traversal. The hybrid ensemble introduces a modest additional 
overhead by combining predictions from both models, but remains within practical limits for real-time applications.

From an application perspective, these factors are critical. Fraud detection systems must process large volumes of transactions with 
low latency. The inclusion of inference-time evaluation ensures that the proposed approach is not only accurate but also practical for 
deployment in latency-sensitive environments.

3.6.2.  Models under evaluation

Six models, representing distinct methodological families, were selected to evaluate performance across the comparative frame-
work. Traditional baselines and ensemble learners included Logistic Regression as a transparent, low-cost benchmark; Random Forest, 
which captures non-linear interactions and handles missing data effectively; and XGBoost, a gradient boosting algorithm designed for 
high performance on imbalanced data through iterative boosting, regularization, and class weighting. Neural network models 
comprised a shallow ANN to assess whether modest architectures could detect fraud patterns beyond tree-based methods, and a deeper 
DNN with additional hidden layers, dropout regularization, and focal loss to enhance representation and handle class imbalance. Both 
models were trained independently, and their predicted probabilities were combined using a linear weighting scheme. This approach 
avoids the complexity of stacking while still leveraging the complementary strengths of boosting and deep learning models. This 
hybrid integration leveraged both structured feature learning and deep representations, aiming to improve predictive performance in 
real-world fraud detection.

3.6.3.  Evaluation framework

Model evaluation in fraud detection requires careful consideration of extreme class imbalance. Overall accuracy was excluded due 
to its tendency to overstate performance in majority-dominated datasets. Instead, a combination of complementary metrics was 
employed to assess both detection effectiveness and operational impact. Recall (sensitivity) was prioritized to minimize costly false 
negatives, while precision ensured that gains in recall did not lead to excessive false alarms. The F1-score provided a balanced measure 
of this trade-off. Discriminative ability was captured via ROC-AUC, with additional emphasis on PR-AUC, which better reflects per-
formance on the minority (fraud) class. Finally, a cost-sensitive adjustment penalized false negatives more heavily than false positives, 
aligning evaluation with the financial consequences of undetected fraud. This multi-metric framework ensured models were assessed 
for both predictive accuracy and practical utility.

4.  Results

This section integrates both exploratory data analysis and modeling, providing a unified presentation of findings. Exploratory data 
analysis is incorporated directly into the results to illustrate how transaction characteristics and feature distributions inform subse-
quent model performance. The subsections are structured to highlight specific aspects of the data and connect them to fraud detection 
outcomes.

4.1.  Fraud distribution and class imbalance

The first step in characterizing the dataset was to assess the distribution of fraud versus legitimate transactions. Based on the 
processed dataset used in this study, there are 16,530 fraud transactions out of a total of 472,432 records, corresponding to a fraud 
proportion of approximately 3.5%. This value was verified directly from the data as

Fraud Ratio =

∑n

i=1 y i
n

= 16530
472432

≈ 0:035:

Although this level of imbalance is less extreme than in certain real-world financial datasets, it still presents a significant challenge 
for classification models. A naive classifier that always predicts the majority (non-fraud) class would achieve approximately 96.5% 
accuracy, yet it would fail to detect any fraud transactions. This demonstrates that accuracy alone is not an appropriate metric for 
evaluating fraud detection performance. To address this issue, evaluation metrics such as precision, recall, F1-score, ROC-AUC, and 
PR-AUC are used throughout this study, as they better reflect performance on the minority class.

4.2.  Evaluation of class imbalance handling strategies - SMOTE

Class imbalance is a fundamental challenge in fraud detection, where fraud transactions typically constitute only a small fraction of 
the dataset. In this study, we primarily address class imbalance through cost-sensitive learning techniques, including class weighting, 
focal loss, and threshold optimization. To provide a more comprehensive evaluation, we also investigate the effectiveness of the 
Synthetic Minority Over-sampling Technique (SMOTE). SMOTE generates synthetic minority class samples by interpolating between 
existing minority instances, thereby increasing the representation of fraud transactions in the training data. SMOTE was applied to the 
training dataset prior to model fitting. Specifically, a sampling ratio of 0.2 was used, meaning that the minority class was increased to 
20% of the majority class. After applying SMOTE, the augmented dataset was used to train both the XGBoost and deep neural network 
components of the ensemble model, following the same pipeline as the baseline approach.

The results indicate that the proposed cost-sensitive approach significantly outperforms the SMOTE-based model across all eval-
uation metrics. In particular, the proposed method achieves higher ROC-AUC, PR-AUC, and F1-score, demonstrating better overall

9

---

<!-- PAGE 10 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

discrimination and balance between precision and recall. For completeness, we note that generative approaches such as GAN-based 
methods have also been proposed for imbalance handling. However, these methods introduce significant computational complexity 
and are difficult to stabilize in high-dimensional tabular data. Given these challenges, and the strong performance of cost-sensitive 
learning observed in our experiments, we do not pursue GAN-based methods in this study. Overall, the experimental results in 
Table 3 demonstrate that cost-sensitive learning provides a more effective and stable approach to handling class imbalance in the 
dataset compared to SMOTE, making it a more suitable choice for tabular fraud detection tasks.

4.3.  Transaction and product patterns

Fraud activity often manifests through systematic behaviors rather than random noise, making transaction characteristics an 
important source of discriminative features. In particular, monetary value and product type reveal clear differences between fraud and 
legitimate transactions, as illustrated in Fig. 2. Fig. 2a presents the distribution of transaction amounts by class. Fraud activity is 
disproportionately concentrated in very low value transactions, often below 200 USD, which suggests that fraudsters frequently 
conduct small “test” purchases to confirm the validity of stolen credentials before escalating to larger transactions. At the other 
extreme, there is also a visible concentration of fraud in very high value purchases, reflecting opportunistic attempts to maximize 
financial gain once an account has been compromised. Legitimate transactions, by contrast, are more evenly spread across the range 
but cluster most heavily in the mid value segment, particularly below 500 USD, after which their frequency declines sharply. This 
divergence between fraud and legitimate spending behaviors highlights the deliberate strategies used by fraudsters to balance 
concealment and profitability. Fig. 2b shows fraud prevalence across product categories. Fraud rates are highest in category C, fol-
lowed by category S, whereas categories H, R, and especially W exhibit much lower levels of fraud activity. These discrepancies align 
with differences in product risk profiles: categories dominated by digital or card not present transactions are more vulnerable to 
exploitation, while those tied to physical goods or requiring stronger verification demonstrate greater resilience. Incorporating such 
product level distinctions into predictive models provides highly discriminative signals that enhance the effectiveness of both 
ensemble and neural network based approaches to fraud detection.

4.4.  Temporal and geolocation patterns of fraud

Fraud transactions also exhibit systematic temporal and geographical behaviors rather than occurring uniformly across time and 
space. These patterns, summarized in Fig. 3, reveal how fraud risk is influenced by daily cycles, weekly rhythms, and regional contexts. 
Fig. 3a shows fraud distribution across hours of the day. Fraud activity peaks during late-night and early-morning hours, a pattern 
consistent with reduced customer vigilance and lower institutional monitoring during off-peak periods. Fig. 3b presents the distri-
bution of fraud rates by day of the week. The x-axis represents the seven days (Monday to Sunday), obtained by mapping the 
transaction timeline into a weekly cycle using modular arithmetic on the transaction day index. This transformation converts the 
continuous transaction timeline into a categorical representation that captures weekly periodic behavior. The results indicate that 
fraud rates are relatively stable across weekdays, with a slight decrease observed on Fridays and moderate increases during weekends, 
particularly on Saturday and Sunday. This pattern may reflect reduced monitoring and lower operational oversight during weekends, 
as well as increased online transaction activity, which can create more opportunities for fraud behavior. The lower fraud rate on 
Fridays may be associated with more structured transaction patterns and stronger institutional controls during standard business 
periods. While temporal variation exists, fraud is not strongly concentrated on a single day but instead reflects broader behavioral and 
operational dynamics. By explicitly encoding the day-of-week structure, this visualization provides a clearer and more interpretable 
representation of weekly fraud patterns compared to the original sequential time-based plot. Fig. 3c and d highlight geographical 
differences. Fraud rates vary significantly across regions and countries, with certain locations showing disproportionately high 
prevalence. These discrepancies may reflect both differences in fraudster targeting strategies and variability in regional payment

Fig. 2. Fraud patterns across transaction amounts and product categories.

10

---

<!-- PAGE 11 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Fig. 3. Temporal and spatial fraud patterns: (a) hour of day; (b) day of week; (c) region; (d) country.

infrastructures. Such spatial heterogeneity reinforces the value of incorporating geolocation features into fraud detection models, as 
they provide powerful discriminative signals when combined with transaction and identity attributes.

Temporal and geolocation information are explicitly incorporated into the predictive models through feature engineering and 
preprocessing, rather than being used solely for exploratory visualization. Temporal information is derived directly from the Trans-
actionDT variable, which represents the elapsed time since a reference point. From this variable, the hour of the day is constructed as:

(
hour_of_day =

)

TransactionDT 
3600

mod 24:

(9)

This transformation converts raw timestamps into a cyclical daily feature that captures time-of-day fraud patterns observed during

exploratory analysis. The resulting variable is included as a numerical feature in the model input.

Geolocation information is incorporated using the addr1 (region) and addr2 (country) variables provided in the dataset. As these 
variables are categorical, they are encoded using label encoding during preprocessing, where each unique category is mapped to a 
numerical value. This representation enables both tree-based models and neural networks to learn location-specific fraud patterns.

Following feature engineering and encoding, all temporal and geolocation variables are included in the final feature matrix X, 
which is used to train all models in this study, including Random Forest, XGBoost, ANN, DNN, and the hybrid ensemble. Consequently, 
the models are able to directly learn from temporal cycles and geographical risk patterns identified in the data. By incorporating these 
engineered features into the training process, the temporal and spatial patterns discussed in Section 4.3 are not only observed but are 
actively leveraged to improve fraud detection performance.

4.5.  Identity-based feature insights

Identity-related features provide some of the strongest discriminative signals in fraud detection, and Fig. 4 highlights three 
representative patterns. Fig. 4a shows that free email domains are disproportionately associated with fraud activity, whereas insti-
tutional or corporate domains exhibit much lower fraud rates, reflecting fraudsters’ preference for anonymous or disposable services. 
Fig. 4b compares fraud rates across device types, with mobile and tablet transactions showing higher fraud levels than desktop, 
consistent with weaker authentication mechanisms and less reliable device fingerprinting. Fig. 4c illustrates variation by device in-
formation, where certain identifiers appear disproportionately in fraud transactions, suggesting the use of emulated or spoofed devices

11

---

<!-- PAGE 12 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Fig. 4. Identity-based fraud patterns: (a) email domain; (b) device type; (c) device information.

or the systematic reuse of compromised profiles. Together, these findings underscore why identity-linked attributes are heavily 
weighted by both tree-based ensembles and deep learning models in fraud detection.

4.6.  Results of model performance

This section presents a comparative evaluation of all seven machine learning models developed for transaction fraud detection: 
Logistic Regression (LR), Random Forest (RF), XGBoost (XGB), Enhanced XGBoost (XGB-Adv), Artificial Neural Network (ANN), Deep 
Neural Network (DNN), and the XGBoost + DNN Ensemble. Table 4 summarizes the validation performance of all models.

Metrics include ROC-AUC and PR-AUC for ranking capability, as well as accuracy, precision, recall, and F1-score for fraud detection 
effectiveness. In addition, inference time (measured in milliseconds per transaction) is reported to assess computational efficiency in 
real-time deployment scenarios.

The results show a clear performance gap between baseline models and advanced approaches. Logistic Regression suffers from low 
precision (0.10) and F1-score (0.18), making it unsuitable for fraud detection. Random Forest improves on these metrics, reaching an 
F1-score of 0.45, but still falls behind gradient boosting methods in capturing complex relationships in the data. Standard XGBoost 
raises recall to 0.81, boosting fraud capture rates, but precision (0.22) remains low, leading to a higher false-positive rate.

Enhanced XGBoost demonstrates the most significant improvement among single models, delivering the highest recall (0.83) and 
substantially better precision (0.42) than standard XGBoost. This balance results in a higher F1-score (0.55) and strong PR-AUC 
(0.7676), reflecting better performance in the imbalanced fraud detection setting. The improvement can be attributed to careful 
hyperparameter tuning and regularization, which reduce overfitting while improving fraud detection sensitivity. For use cases 
prioritizing maximum fraud capture with acceptable false positives, Enhanced XGBoost is a strong candidate.

The XGB + DNN Ensemble outperforms all other models in overall balance, achieving the highest F1-score (0.74) and PR-AUC 
(0.7897), alongside a high recall (0.69) and precision (0.78). By combining Enhanced XGBoost's structured feature learning with 
the DNN's deep representation capability, the ensemble reduces weaknesses present in each standalone model. This makes it well-
suited for real-world usage, where both detecting fraud and minimizing false positives are critical for efficiency and customer trust.

12

---

<!-- PAGE 13 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

While Table 4 shows that some performance differences (e.g., ROC-AUC of 0.9638 vs. 0.9628) appear small, it is important to 
determine whether these improvements are statistically meaningful and consistent rather than artifacts of a particular train–validation 
split. To address this, additional experiments were conducted using multiple random data partitions. Specifically, the dataset was split 
into training (80%) and validation (20%) sets across three different random seeds, using stratified sampling to preserve the class 
imbalance. For each split, both the Enhanced XGBoost model and the proposed XGB + DNN Ensemble were trained independently and 
evaluated on the corresponding validation set.

The evaluation metric used for comparison is ROC-AUC. Results are summarized as mean ± standard deviation across the three 
runs. The Enhanced XGBoost model achieved an average ROC-AUC of 0.9223 ± 0.0019, while the proposed ensemble achieved 
0.9274 ± 0.0025. The ensemble consistently outperformed the baseline model across all splits. To formally assess whether this 
improvement is statistically significant, a paired t-test was conducted on the ROC-AUC scores obtained from each split. This test is 
appropriate since both models are evaluated on identical validation partitions, enabling a direct paired comparison. The resulting p-
value is 0.0054, which is well below the conventional significance threshold of 0.05, indicating that the improvement is statistically 
significant and unlikely to be due to random variation.

Furthermore, the small standard deviation observed for both models indicates stable performance across different data splits. This 
demonstrates that the results are robust and not sensitive to the specific 80/20 partition of the data, despite the relatively small 
proportion of fraud cases. The overall evaluation procedure follows the training and validation pipeline described in Algorithm 2, 
extended across multiple randomized splits. Overall, these results demonstrate that the proposed XGB + DNN Ensemble provides a 
consistent and statistically significant improvement over the baseline model. While more extensive validation strategies such as k-fold 
cross-validation could further strengthen this analysis, the current findings already provide strong empirical evidence supporting the 
robustness and reliability of the proposed approach.

OLightGBM, an optimized version of the Light Gradient Boosting Machine (LightGBM), proposed by Taha and Malebary (2020), is 
incorporated into the main comparative results (Table 4) to provide a unified and consistent benchmark across all models, rather than 
being presented in a separate subsection. OLightGBM enhances the standard framework through Bayesian-based hyperparameter opti-
mization to automatically tune model parameters and improve predictive performance. LightGBM itself is a gradient boosting algorithm 
based on decision trees, designed for efficiency and scalability. It employs techniques such as gradient-based one-side sampling (GOSS) 
and exclusive feature bundling (EFB) to reduce computational complexity while maintaining high predictive accuracy. The OLightGBM 
approach builds upon this foundation by optimizing hyperparameters governing tree growth and learning dynamics.

The reported results for OLightGBM are taken directly from the original study, where it achieved a ROC-AUC of 0.9288, accuracy of 
98.40% (rounded to 98%), precision of 97.34% (rounded to 0.97), and F1-score of 0.5695. As shown in Table 4, both the Enhanced 
XGBoost and the proposed XGB + DNN Ensemble outperform OLightGBM in terms of ROC-AUC, achieving 0.9628 and 0.9638, 
respectively. This indicates that the proposed models provide improved discriminative capability relative to a strong published 
benchmark.

It is important to note that the OLightGBM results are taken from the original publication and may be based on different datasets, 
preprocessing pipelines, and evaluation protocols. Therefore, this comparison is intended to provide contextual benchmarking rather 
than a strictly controlled experimental comparison. Nevertheless, the results suggest that the proposed models are competitive with, 
and in this case outperform, existing state-of-the-art approaches.

In addition to predictive performance, inference time results reported in Table 4 provide important insights into the computational 
efficiency of each model in real-time deployment scenarios. Tree-based models, particularly XGBoost (0.08 ms/transaction) and 
Enhanced XGBoost (0.09 ms/transaction), achieve low inference latency due to efficient decision-tree traversal, making them highly 
suitable for large-scale, low-latency fraud detection systems. Logistic Regression exhibits the lowest latency overall (0.02 ms/trans-
action), although its predictive performance is substantially weaker.

In contrast, neural network models such as ANN (0.25 ms/transaction) and DNN (0.30 ms/transaction) incur higher inference times 
due to forward propagation through multiple layers. The hybrid XGB + DNN ensemble introduces additional computational overhead 
by combining predictions from both models, resulting in the highest latency (0.35 ms/transaction) among the evaluated approaches.
These results highlight a clear trade-off between predictive performance and computational efficiency. While the proposed 
ensemble achieves the best overall detection performance, its higher latency may limit its applicability in ultra-low-latency envi-
ronments. In such cases, XGBoost provides a strong alternative, offering competitive predictive performance with significantly lower 
inference time, making it particularly attractive for real-time fraud detection systems where rapid decision-making is critical.

4.7.  Comparison with sequential model (LSTM)

To evaluate whether sequence-based modeling improves fraud detection performance, we implemented a Long Short-Term 
Memory (LSTM) network as a representative state-of-the-art temporal model. Fraud detection is often considered inherently 
sequential, as user behavior over time may reveal anomalous patterns. Therefore, incorporating an LSTM provides a meaningful 
benchmark to assess whether modeling temporal dependencies yields performance gains for this dataset.

The LSTM model was trained using sliding-window sequences constructed from the transaction data, with each sequence repre-
senting a short temporal context of transactions. Class imbalance was addressed using a weighted binary cross-entropy loss function to 
ensure that the model does not trivially predict the majority class. However, experimental results demonstrate that the LSTM performs 
substantially worse than the proposed hybrid ensemble model across all evaluation metrics (as shown in Table 5). Specifically, the 
LSTM achieves a ROC-AUC of 0.502, PR-AUC of 0.036, and F1-score of 0.013, indicating near-random classification behavior. In

13

---

<!-- PAGE 14 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

contrast, the proposed XGBoost + DNN ensemble achieves substantially higher performance, with a ROC-AUC of 0.9638, PR-AUC of 
0.6582, and F1-score of 0.74 (see Table 6).

The poor performance of the LSTM can be attributed to the structural characteristics of the IEEE-CIS dataset. Although the dataset 
includes a temporal feature (TransactionDT), it does not provide consistent user-level sequences or long-term behavioral histories. 
Transactions are not reliably grouped by individual users, and temporal ordering alone does not guarantee meaningful sequential 
dependencies. As a result, the constructed sequences lack coherent behavioral patterns, limiting the ability of sequence-based models 
to learn discriminative temporal features. In contrast, the proposed hybrid ensemble model is better aligned with the tabular and high-
dimensional nature of the dataset. XGBoost effectively captures complex feature interactions, handles missing values, and is robust to 
noisy and sparse features commonly found in fraud detection data. The DNN component complements this by learning nonlinear 
representations and capturing higher-order feature interactions. By combining these two models, the ensemble leverages comple-
mentary strengths, resulting in improved generalization and significantly higher predictive performance.

These findings highlight an important insight: model effectiveness is strongly dependent on the underlying data structure. While 
sequence-based models such as LSTM are powerful for tasks with well-defined temporal dependencies, they are less suitable for tabular 
fraud detection datasets with weak or irregular sequential patterns. In such cases, hybrid ensemble approaches provide a more 
effective and practical solution.

4.8.  Comparison with kaggle state-of-the-art

To further evaluate the effectiveness of the proposed model, we compare our results with top-performing solutions from the IEEE-

CIS Kaggle fraud detection competition.

According to the 1st place solution of the IEEE-CIS Kaggle competition (Deotte et al., 2019), the final model was an ensemble of 
gradient boosting algorithms, including XGBoost, LightGBM, and CatBoost, combined with extensive feature engineering, validation 
strategies, and stacking techniques. This approach achieved a private leaderboard ROC-AUC of approximately 0.9459 and a public 
leaderboard score of 0.9677. Similarly, the 5th place solution (H. M. et al., 2019) relied on an ensemble of LightGBM models with 
user-level feature aggregation and achieved a private leaderboard score of 0.9425. These results demonstrate that tree-based ensemble 
methods are consistently effective for this dataset.

In comparison, the proposed hybrid ensemble achieves a ROC-AUC of 0.9638 and F1-score of 0.74, demonstrating competitive 
performance relative to these state-of-the-art solutions. It is important to note that direct comparison with Kaggle leader board results 
is not strictly equivalent, as competition settings involve hidden test sets and more stringent validation protocols. Nevertheless, the 
results indicate that the proposed model achieves strong predictive performance within a standard experimental framework. Unlike 
the Kaggle-winning solutions, which rely heavily on complex feature engineering and dataset-specific techniques, the proposed 
method emphasizes a principled integration of tree-based learning and deep neural networks. This results in a simpler, more repro-
ducible modeling pipeline while maintaining strong predictive performance and interpretability through SHAP-based analysis. 
Interestingly, the observations reported in the Kaggle winning solution further support our findings.

4.9.  ROC and Precision–Recall curve analysis

This section compares four models to evaluate how the proposed approaches perform against strong baselines. Random Forest is 
included as a representative of traditional machine learning methods, while the Deep Neural Network represents deep learning ap-
proaches. These are compared with the Enhanced XGBoost (XGB-Adv) and the XGB + DNN Ensemble, which combine boosting and 
neural networks. This comparison highlights the improvements of the proposed methods over both classical and deep learning models. 
Fig. 6 presents the ROC and Precision–Recall (PR) curves for the four models. Both plots confirm the superior performance of the 
proposed methods over the baselines. In Fig. 5a, the XGB + DNN Ensemble achieved the highest ROC-AUC of 0.9638, followed closely 
by XGB-Adv at 0.9628. Among the baselines, the DNN (0.9182) slightly outperformed the RF (0.9122). The steep initial slope and 
proximity of the proposed models’ curves to the top-left corner illustrate their strong discriminative ability across thresholds. Fig. 5b 
shows the PR curves, which are more informative for imbalanced datasets. The XGB + DNN Ensemble again outperformed all models

Table 5
Performance comparison between LSTM and the proposed ensemble model.

Model

LSTM
XGB + DNN ensemble

ROC-AUC

0.502
0.9638

PR-AUC

0.036
0.6582

F1-score

0.013
0.74

Precision

0.030
0.78

Table 6
Comparison with Kaggle top solutions.

Method
Kaggle 1st place ensemble [46]
Kaggle 5th place LightGBM ensemble [47] 
Proposed XGB þ DNN ensemble

ROC-AUC

0.94–0.95
0.94
0.9638

14

PR-AUC

–
–

0.6582

Recall

0.008
0.69

F1-score

–
–

0.74

---

<!-- PAGE 15 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Fig. 5. ROC and Precision–Recall curve analysis for baseline and proposed models: (a) ROC curves; (b) PR curves.

Fig. 6. Global feature importance–bar plot.

with an Average Precision (AP) of 0.7897, followed by XGB-Adv at 0.7676. Among the baselines, the DNN achieved 0.6403, out-
performing the RF at 0.5856. The proposed models maintain higher precision at varying recall levels, demonstrating superior handling 
of the minority fraud class.

The results demonstrate that while traditional models such as Logistic Regression and Random Forest provide useful baselines, they 
fall short under severe class imbalance. Enhanced XGBoost achieved substantial gains, and the hybrid XGB + DNN Ensemble 
consistently outperformed all other approaches, delivering the highest recall, F1-score, ROC-AUC, and PR-AUC. Exploratory analyses 
further revealed clear fraud patterns across transaction amounts, product categories, temporal cycles, and identity-related features, 
confirming their importance as discriminative signals. Taken together, these findings underscore both the necessity of advanced 
ensemble methods and the value of incorporating domain-specific patterns, providing a comprehensive foundation for fraud detection 
pipelines.

15

---

<!-- PAGE 16 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

4.10.  Results on feature interpretability - SHAP based feature analysis

This section extends the analysis beyond performance metrics to interpret the results and their practical significance. While the 
previous section identified the best-performing models under class imbalance, the focus here is on understanding the mechanisms 
driving their success, the insights provided by key features, and their implications for real-world fraud detection. Interpretability is 
particularly critical in financial applications, where transparency and accountability are required for deployment. To this end, SHAP 
values are computed for the Enhanced XGBoost model, the best-performing single learner, to quantify both global and local feature 
contributions. The analysis is conducted from two complementary perspectives: (i) global feature importance, using mean absolute 
SHAP values to identify the most influential predictors across all transactions, and (ii) local interpretation, using SHAP beeswarm plots 
to examine how feature values, their direction, and distribution influence fraud predictions at the instance level.

4.10.1.  Global feature importance in fraud context

The global SHAP importance plot (Fig. 6) shows that TransactionAmt is the most influential feature, followed by identity-related

features such as card6, C14, C1, and C13, as well as behavioral variables including V70 and V258.

This ranking is consistent with prior fraud detection studies, where transaction amount and identity consistency are primary in-
dicators of fraud. Fraud transactions often occur at extreme values: low-value transactions are used as “test” transactions to validate 
stolen credentials, while high-value transactions reflect attempts to maximize financial gain. Identity-related features capture de-
viations from normal user behavior. In legitimate transactions, these features tend to be stable, whereas fraud introduces anomalies 
such as unusual transaction counts or inconsistent card usage. The importance of these features confirms that fraud detection relies 
heavily on identifying such deviations.

4.10.2.  Local SHAP interpretation and feature effects

The SHAP beeswarm plot shown in Fig. 7 provides detailed transaction-level insights by combining feature values with their 
contributions to model predictions. In the beeswarm plot, the horizontal axis represents SHAP values, indicating the magnitude and 
direction of each feature's contribution. Positive SHAP values increase fraud likelihood, while negative values decrease it. The color 
gradient represents feature values (red = high, blue = low), allowing us to infer whether high or low values of a feature are associated 
with fraud.

For TransactionAmt, high values (red points) are predominantly associated with positive SHAP values, indicating increased fraud 
risk. However, some low values also contribute positively, suggesting that fraud detection captures both high-value exploitation and 
low-value probing behavior. This demonstrates that fraud risk cannot be explained by simple thresholds but depends on contextual

Fig. 7. Local explanation–beeswarm plot.

16

---

<!-- PAGE 17 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

interactions. For card6, distinct clusters of SHAP values indicate that specific categories consistently increase fraud probability. This 
suggests that certain card types or transaction channels are more vulnerable, likely due to differences in authentication mechanisms. 
Features such as C14 and C13 exhibit asymmetric distributions, where extreme values correspond to strong positive SHAP contri-
butions. This indicates that deviations from normal behavioral patterns significantly increase fraud likelihood, providing evidence of 
anomaly-based detection. The V-series features (e.g., V70, V258) show wide and overlapping SHAP distributions, indicating strong 
interaction effects. These features do not act independently but contribute differently depending on the context of other variables. This 
highlights the importance of models capable of capturing non-linear relationships.

4.10.3.  Comparison with random forest

For comparison, the Random Forest feature importance plot (See Fig. 8) shows a broader distribution of influential variables rather 
than dominance by a small subset. Features such as C14 and C13 emerge as the strongest contributors, while transaction-based at-
tributes like TransactionAmt, V258, and V265, along with several V-series variables, also rank highly. This balance indicates that 
Random Forest relies on both identity signals and behavioral transaction features, capturing multiple dimensions of fraud risk. Im-
portances are more evenly spread across categories, suggesting that no single variable alone drives the predictions but rather a 
combination of complementary signals.

While this confirms the relevance of key features, Random Forest importances provide only relative weights and lack the ability to 
explain whether a feature increases or decreases the likelihood of fraud. They also do not account for interactions between features or 
variation across individual cases. These limitations highlight why more interpretable methods such as SHAP are better suited for high-
stakes fraud detection, where fine-grained reasoning and case-level explanations are essential for operational use.

4.10.4.  Consistency with prior literature and novel insights

The SHAP analysis demonstrates strong agreement with prior research in financial fraud detection. Previous studies have identified 
transaction amount, identity consistency, and behavioral irregularities as key indicators of fraud. The prominence of these features in 
our analysis confirms that the proposed models capture established fraud patterns.

At the same time, the results provide additional insights beyond prior work. In particular, the analysis highlights the importance of 
anonymized behavioral features (V-series), which encode latent interaction patterns not directly observable in raw data. These features 
exhibit context-dependent contributions, indicating that fraud detection is driven by interactions rather than isolated feature effects. 
This observation aligns with recent work by (Lin and Gao, 2022), who demonstrate that SHAP-based methods can reveal complex 
relationships between financial features and improve interpretability in fraud detection models.

4.10.5.  Practical implications

The enhanced SHAP interpretation provides actionable insights for real-world fraud detection systems. Financial institutions can 
leverage these findings to combine rule-based detection (e.g., abnormal transaction amounts or identity inconsistencies) with machine 
learning models capable of capturing complex feature interactions. Furthermore, SHAP-based explanations improve transparency by 
providing case-level justifications for predictions. This is critical for regulatory compliance and operational trust in financial 
applications.

Fig. 8. Random forest - top 20 feature importances.

17

---

<!-- PAGE 18 -->

N.D. Anh Luong, S. Xie

5.  Discussions

The Journal of Finance and Data Science 12 (2026) 100195

The results carry direct implications for real-world fraud detection systems, where predictive performance must be balanced with 
operational considerations. Model selection cannot rely solely on ROC-AUC or PR-AUC values; institutions must also consider inter-
pretability, latency, and the trade-off between false positives and false negatives.

While this study demonstrates the effectiveness of advanced ensemble models for fraud detection, several limitations should be 
acknowledged. First, the dataset, although large and representative of real-world payment transactions, is anonymized and lacks 
certain contextual features (e.g., merchant category codes, customer demographics, and real-time session information). The absence of 
these variables restricts the interpretability of fraud patterns and may limit the generalizability of the findings across different financial 
institutions and geographies.

Second, the evaluation was conducted in an offline validation setting. Although metrics such as ROC-AUC and PR-AUC are 
informative, they do not capture all operational trade-offs. Real-world deployment involves latency constraints, streaming data 
pipelines, and integration with fraud investigation teams. These aspects were not simulated in this study, and future research should 
extend validation to production-like environments, including stress testing under high transaction volumes and adversarial attack 
scenarios.

Third, while SHAP provided valuable explainability for tree-based models, interpretability for deep neural networks remains less 
developed. Methods such as LIME or integrated gradients offer partial insights, but their stability and regulatory acceptance are still 
evolving. This creates challenges for deploying complex models in strictly regulated financialdomains where transparency is a non-
negotiable requirement.

A key limitation of this study is that the IEEE-CIS dataset represents a fixed historical snapshot of transaction data. In real-world 
fraud detection systems, transaction patterns and fraud strategies evolve continuously over time, a phenomenon commonly referred to 
as concept drift. This occurs when the underlying data distribution or the relationship between features and the target variable changes, 
often due to adaptive behavior by fraudsters. As fraud detection models are trained on historical data, their performance may degrade 
when deployed in a live environment if the statistical properties of incoming transactions differ from those observed during training. 
For example, fraudsters may shift from low-value probing transactions to more sophisticated attacks involving device spoofing or 
identity obfuscation, rendering previously learned patterns less effective.

While the models proposed in this study demonstrate strong performance under a static evaluation setting, maintaining their 
effectiveness in practice would require continuous monitoring and adaptation. This may involve periodic retraining on recent data, 
online learning strategies, or drift detection mechanisms that trigger model updates when significant distributional changes are 
observed. Furthermore, ensemble approaches such as the proposed XGBoost + DNN model may offer some robustness to moderate drift 
due to their ability to capture complementary patterns. However, they are not inherently immune to concept drift, and their long-term 
performance depends on timely updates and data refresh cycles.

6.  Conclusion

This study addressed the persistent challenge of fraud detection in highly imbalanced financial transaction data by systematically 
comparing traditional, ensemble-based, and deep learning approaches. Through rigorous experimentation, it was demonstrated that 
classical baselines such as Logistic Regression and Random Forest, while interpretable, fail to provide the precision and recall balance 
required for real-world applications. Enhanced XGBoost improved performance by leveraging gradient boosting with advanced 
handling of imbalance, yet it was the proposed hybrid XGB + DNN Ensemble that delivered the most effective and robust results across 
all evaluation metrics. Beyond raw performance scores, the study emphasized the importance of interpretability and operational 
readiness. SHAP-based feature attribution highlighted the central role of transaction amounts, identity-linked attributes, and temporal 
patterns in detecting fraud behavior, underscoring the need for multi-dimensional representations of customer activity.

The hybrid XGB + DNN Ensemble, embedded within a structured and adaptive framework, represents a powerful and practical 
solution for modern fraud detection. By aligning methodological innovation with operational realities, this study demonstrates that 
effective fraud detection requires not only strong algorithms but also transparent, adaptive, and institutionally aligned systems capable 
of withstanding the evolving tactics of financial fraud. Together, these findings advance both academic understanding and practical 
implementation of fraud detection systems. Nevertheless, limitations remain. The anonymized dataset constrained interpretability of 
certain fraud patterns, and evaluation was restricted to offline validation. Addressing these gaps through richer feature sets, real-time 
testing, and advanced learning paradigms such as graph-based or federated learning offers promising directions for future research.

CRediT authorship contribution statement

Nguyen Duy Anh Luong: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, 
Investigation, Formal analysis, Data curation, Conceptualization. Shengkun Xie: Writing – review & editing, Writing – original draft, 
Supervision, Methodology, Funding acquisition, Formal analysis, Conceptualization.

Grant information

This work is funded by Natural Sciences and Engineering Research Council of Canada Discovery Grant.

18

---

<!-- PAGE 19 -->

N.D. Anh Luong, S. Xie

Declaration of competing interest

The Journal of Finance and Data Science 12 (2026) 100195

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to

influence the work reported in this paper.

References

Achakzai, M.A.K., Peng, J., 2023. Detecting financial statement fraud using dynamic ensemble machine learning. Int. Rev. Financ. Anal. 89, 102827.
Alamri, M., Ykhlef, M., 2024. Hybrid feature engineering based on customer spending behavior for credit card anomaly and fraud detection. Electronics 13 (20), 3978. 
Alfaiz, N.S., Fati, S.M., 2022. Enhanced credit card fraud detection model using machine learning. Electronics 11 (4), 662.
Bahnsen, A.C., Aouada, D., Stojanovic, A., Ottersten, B., 2016. Feature engineering strategies for credit card fraud detection. Expert Syst. Appl. 51, 134–142. 
Baisholan, N., Dietz, J.E., Gnatyuk, S., Turdalyuly, M., Matson, E.T., Baisholanova, K., 2025. A systematic review of machine learning in credit card fraud detection

under original class imbalance. Computers 14 (10), 437.

Bhardwaj, K., Kumar, M., Verma, R., Kumar, D., 2024. Machine learning and deep learning for credit card fraud detection: a comparative analysis. In: Proc. 2024 Int.

Conf. Artificial Intelligence and Emerging Technology (Global AI Summit), pp. 131–136.

Bin Sulaiman, R., Schetinin, V., Sant, P., 2022. Review of machine learning approach on credit card fraud detection. Human-Centric Intelligent Systems 2 (1), 55–68. 
Bolton, R.J., Hand, D.J., 2002. Statistical fraud detection: a review. Stat. Sci. 17 (3), 235–255.
Breskuviene, D., Dzemyda, G., 2024. Enhancing credit card fraud detection: highly imbalanced data case. J. Big Data 11 (1), 182.
Broby, D., 2021. Financial technology and the future of banking. Financ. Innov. 7 (1), 47.
Carcillo, F., Le Borgne, Y.-A., Caelen, O., Kessaci, Y., Obl�e, F., Bontempi, G., 2021. Combining unsupervised and supervised learning in credit card fraud detection. Inf.

Chaurasia, S., Kesharwani, S., Sharma, S., Sharma, S., Chugh, B., 2024. Analysis of ensemble machine learning models for fraud detection. In: Proc. 2024 Int. Conf.

Deotte, C., et al., 2019. IEEE-CIS fraud detection: 1st place solution. Kaggle Competition Write-up. https://www.kaggle.com/competitions/ieee-fraud-detection/

Ding, N., Ruan, X., Wang, H., Liu, Y., 2025. Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. Insur.

Sci. 557, 317–331.

Intelligent Systems for Cybersecurity (ISCS), pp. 1–6.

writeups/fraudsquad-1st-place-solution-part-2.

Math. Econ. 120, 51–60.

Du, H., Lv, L., Guo, A., Wang, H., 2023. Autoencoder and LightGBM for credit card fraud detection problems. Symmetry 15 (4), 870.
Gandhar, A., Gupta, K., Pandey, A.K., Raj, D., 2024. Fraud detection using machine learning and deep learning. SN Comput. Sci. 5 (5), 453.
George, M.Z.H., Alam, M.K., Hasan, M.T., 2025. Machine learning for fraud detection in digital banking: a systematic literature review. arXiv preprint arXiv:

2510.05167.

H. M, et al., 2019. IEEE-CIS fraud detection: 5th place solution (Lions). Kaggle Competition Write-up. https://www.kaggle.com/competitions/ieee-fraud-detection/

writeups/lions-5th-place-solution-lions.

Ileberi, E., Sun, Y., Wang, Z., 2021. Performance evaluation of machine learning methods for credit card fraud detection using SMOTE and AdaBoost. IEEE Access 9,

Jahnavi, D., Mona, A., Pulata, S., Sami, S., Vakamullu, B., 2024. Robust hybrid machine learning model for financial fraud detection in credit card transactions. In:

Proc. 2024 2nd Int. Conf. Intelligent Data Communication Technologies and Internet of Things (IDCIoT), pp. 680–686.

Jiao, B., Guo, Y., Gong, D., Chen, Q., 2022. Dynamic ensemble selection for imbalanced data streams with concept drift. IEEE Transact. Neural Networks Learn. Syst.

Lahbiss, M.M., Chtouki, Y., 2024. Credit card fraud detection in imbalanced datasets: a comparative analysis of machine learning techniques. In: Proc. 2024 Int. Conf.

Computer and Applications (ICCA), pp. 1–6.

Lee, C.-W., Fu, M.-W., Wang, C.-C., Azis, M.I., 2025. Evaluating machine learning algorithms for financial fraud detection: insights from Indonesia. Mathematics 13

Lei, Y.-T., Ma, C.-Q., Ren, Y.-S., Chen, X.-Q., Narayan, S., Huynh, A.N.Q., 2023. A distributed deep neural network model for credit card fraud detection. Finance Res.

Lin, K., Gao, Y., 2022. Model interpretability of financial fraud detection by group SHAP. Expert Syst. Appl. 202.
Lucas, Y., Portier, P.-E., Laporte, L., Calabretto, S., Caelen, O., He-Guelton, L., Granitzer, M., 2019. Multiple perspectives HMM-based feature engineering for credit

card fraud detection. In: Proc. 34th ACM/SIGAPP Symposium on Applied Computing, pp. 1359–1361.

Ludera, D.T., 2021. Credit card fraud detection by combining synthetic minority oversampling and edited nearest neighbours. In: Future of Information and

Communication Conference, pp. 735–743.

Mehbodniya, A., Alam, I., Pande, S., Neware, R., Rane, K.P., Shabaz, M., Madhavan, M.V., 2021. [Retracted] financial fraud detection in healthcare using machine

learning and deep learning techniques. Secur. Commun. Network. 2021, 9293877.

Mienye, E., Jere, N., Obaido, G., Mienye, I.D., Aruleba, K., 2024. Deep learning in finance: a survey of applications and techniques. A.I. 5 (4), 2066–2091. 
Noviandy, T.R., Idroes, G.M., Maulana, A., Hardi, I., Ringga, E.S., Idroes, R., 2023. Credit card fraud detection for contemporary financial management using XGBoost-

driven machine learning and data augmentation techniques. Indatu Journal of Management and Accounting 1 (1), 29–35.

Patel, A., Patel, M., Patel, P., 2024. Exploring supervised machine learning techniques for detecting credit card fraud: an investigative review. In: ITM Web of

Conferences, vol. 65, 03006.

Prasad, M., Srikanth, T., 2024. Multi-Entity real-time Fraud Detection System Using Machine Learning: Improving Fraud Detection Efficiency Using FROST-enhanced

Oversampling.

Riskiyadi, M., 2024. Detecting future financial statement fraud using a machine learning model in Indonesia: a comparative study. Asian Rev. Account. 32 (3),

165286–165294.

35 (1), 1278–1291.

(4), 600.

Lett. 58, 104547.

394–422.

Eng. 102, 108132.

20 (7), e0326975.

168.

Roseline, J.F., Naidu, G., Pandi, V.S., Rajasree, S.A., Mageswari, N., 2022. Autonomous credit card fraud detection using machine learning approach. Comput. Electr.

Saputra, A., et al., 2019. Fraud detection using machine learning in e-commerce. Int. J. Adv. Comput. Sci. Appl. 10 (9).
Shah, D., Sharma, L.K., 2023. Credit card fraud detection using decision tree and random forest. In: ITM Web of Conferences, vol. 53, 02012.
Sharma, A., Sharma, S., Malik, A., Sobti, R., Suryana, A., 2025. Dynamic feature engineering for adaptive fraud detection. Eng. Proc. 107 (1), 68.
Shimin, L., Ke, X., Xinye, S., et al., 2020. An XGBoost-based system for financial fraud detection. In: E3S Web of Conferences, vol 214, 02042.
Siam, A.M., Bhowmik, P., Uddin, M.P., 2025. Hybrid feature selection framework for enhanced credit card fraud detection using machine learning models. PLoS One

Sun, J., 2025. Decision tree-based credit card fraud detection system: design and optimization. Economics & Management Information 1–5.
Taha, A.A., Malebary, S., 2020. An intelligent approach to credit card fraud detection using an optimized light gradient boosting machine. IEEE Access 8,

25579–25587.

Talukder, M.A., Khalid, M., Uddin, M.A., 2024. An integrated multi-stage ensemble machine learning model for fraudulent transaction detection. J. Big Data 11 (1),

Theodorakopoulos, L., Theodoropoulou, A., Tsimakis, A., Halkiopoulos, C., 2025. Big data-driven distributed machine learning for scalable credit card fraud detection

using PySpark, XGBoost, and CatBoost. Electronics 14 (9), 1754.

19

---

<!-- PAGE 20 -->

N.D. Anh Luong, S. Xie

The Journal of Finance and Data Science 12 (2026) 100195

Velarde, G., Sudhir, A., Deshmane, S., Deshmunkh, A., Sharma, K., Joshi, V., 2023. Evaluating XGBoost for balanced and imbalanced data: application to fraud

Wajgi, R., Agarkar, H., Patil, R., Rao, H., Petkar, N., 2024. Enhancing credit card transaction fraud detection with random forest and robust scaling. AIP Conf. Proc.

Xia, Z., Saha, S.C., 2025. FinGraphFL: financial graph-based federated learning for enhanced credit card fraud detection. Mathematics 13 (9), 1396.
Zhang, Y.-L., Zhou, J., Zheng, W., Feng, J., Li, L., Liu, Z., et al., 2019. Distributed deep forest and its application to automatic detection of cash-out fraud. ACM Trans.

Zioviris, G., Kolomvatsos, K., Stamoulis, G., 2024. An intelligent sequential fraud detection model based on deep learning. J. Supercomput. 80 (10), 14824–14847.

detection. arXiv preprint arXiv:2303.15218.

3188, 040013.

Intell. Syst. Technol. 10 (5), 1–19.

20

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

TheJournalofFinanceandDataScience12(2026)100195
ContentslistsavailableatScienceDirect
The Journal of Finance and Data Science
journal homepage: www.keaipublishing.com/en/journals/jfds
Research Article
Explainable ensemble machine learning for financial transaction
fraud detection: Insights from XGBoost and deep neural networks
Nguyen Duy Anh Luong , Shengkun Xie *
Global Management Studies, Ted Rogers School of Management, Toronto Metropolitan University, 350 Victoria Street, Toronto, ON M5B2K3,
Canada
A R T I C L E I N F O A B S T R A C T
Keywords: The rapid digitalization of financial services has enhanced transaction speed and accessibility but
Fraud detection also amplified exposure to fraud activities that undermine institutional integrity and consumer
Machine learning trust. Effective fraud detection requires analytical frameworks that are not only accurate and
XGBoost
Deep learning
adaptive butalsoint erpretabl eandco mpliantwit hfi nancialre gulat ions.This studydevel opsa
Ensemble models
sc alable, explainab lem achinel earningfr amework fordetecti ngfr audfi nancial transaction susing
ahybridensembleofExtremeGradientBoosting(XGBoost)andDeepNeuralNetworks(DNN).
Theproposedmodelintegratestransactional,temporal,andidentity-linkedfeaturestocapture
behavioralandcontextualpatternsinlarge-scale,high-frequencydata.Toaddresstheextreme
classimbalanceinherentinfrauddetection,weevaluatemultiplestrategiesincludingfocalloss,
class weighting, and threshold optimization. Model transparency is enhanced through SHAP-
basedinterpretabilityanalysis,providinggranularinsightsintothefeatureinteractionsdriving
fraudrisk.Empiricalevaluationonareal-worldtransactiondatasetdemonstratesthatthehybrid
ensemble achieves superior detection accuracy and recall relative to baseline models while
maintainingexplainabilitysuitableforregulatedfinancialenvironments.Theresultshighlightthe
potential of combining interpretable machine learning with adaptive ensemble learning to
enhanceresilienceandtrustworthinessinmodernfinancialriskmanagementsystems.
1. Introduction
Therapiddigitalizationoffinancialservices(Broby,2021)hasfundamentallytransformedthewayindividualsandbusinesses
conducttransactionsacrosse-commerce,mobilepayments,andon-linebanking.Whiletheseinnovationshaveenabledunprecedented
convenienceandefficiency,theyhavealsointroducednewvulnerabilities,exposingfinancialsystemstoincreasinglysophisticated
fraudactivities.Creditcardfraud,inparticular,remainsoneofthemostpervasiveandcostlyfinancialcrimes,causingdirectmonetary
lossesanderodingpublictrustinfinancialinstitutions(Dingetal.,2025).Accuratelyidentifyingfraudischallengingbecausemali-
cious activities are often concealed within massive streams of legitimate transactions, making traditional detection approaches
insufficient.
Earlyfrauddetectionsystemswerepredominantlyrule-based,relyingonstaticthresholdsandhandcraftedanomalydetectionrules
to flag suspicious transactions (Bolton and Hand, 2002). Although such approaches were initially effective, they fail to adapt to
* Correspondingauthor.TorontoMetropolitanUniversity,350VictoriaStreet,Toronto,ONM5B2K3,Canada.1-(416)-9795000.
E-mailaddresses:nguyenduyanh.luong@torontomu.ca(N.D.AnhLuong),shengkun.xie@torontomu.ca(S.Xie).
PeerreviewundertheresponsibilityofKeAiCommunicationsCo.,Ltd.
https://doi.org/10.1016/j.jfds.2026.100195
Received3November2025;Receivedinrevisedform29May2026;Accepted2June2026
Availableonline9June2026
2405-9188/© 2026 The Authors. Publishing services by Elsevier B.V. on behalf of KeAi Communications Co. Ltd. This is an open access article under
theCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
evolvingfraudpatterns.Fraudsterscontinuouslymodifytheirtactics,renderingfixedrulesobsoleteandleadingtohighfalse-positive
rateswhileallowinggenuinefraudcasestogoundetected(Dingetal.,2025).Theselimitationshavedrivenaparadigmshifttoward
machine learning (ML) and deep learning (DL), which can automatically learn complex, non-linear patterns from data, adapt to
emergingfraudtactics,anduncoverrelationshipsthataredifficulttomodelmanually(Roselineetal.,2022).
MLhasshownparticularstrengthinanalyzinglarge-scale,high-dimensionaltransactiondata(Talukderetal.,2024;Zhangetal.,
2019).Cost-sensitivelearninghasbeenproposedtoexplicitlyaccountforthefinancialconsequencesofmisclassification,strikinga
balance between minimizing false positives and maximizing fraud detection (Roseline et al., 2022). To address scalability re-
quirements, distributed learning frameworks have been developed to process high-velocity data streams in near real time (Theo-
dorakopoulos et al., 2025). In addition, various algorithms have been explored: support vector machines and neural networks
effectivelycapturenon-linearrelationships,whereasgradientboostingmethodssuchasXGBoostofferrobustperformanceandstrong
predictiveaccuracyfortabular,structureddata(Noviandyetal.,2023).
Despitetheseadvances,frauddetectionstillfacesseveralchallenges.Oneofthemostpersistentistheextremeclassimbalance
betweenlegitimateandfraudtransactions,wherefraudoftenaccountsforlessthan1%ofallrecords(BreskuvieneandDzemyda,
2024). This imbalance biases models toward the majority class and reduces recall for fraud cases, which is particularly costly in
real-world applications. Existing solutions include active learning to prioritize informative samples (Riskiyadi, 2024), ensemble
boostingmethodstailoredtominorityclasses,andresamplingstrategiessuchasSMOTEandundersamplingtorebalancethedata
distribution(Ludera,2021).
Anothermajorchallengeisthehighdimensionalityandstructuralcomplexityoffinancialtransactiondata,whichinvolvenon-
linear feature interactions. Feature engineering has therefore become central to improving model performance, with techniques
such as time-window aggregation to capture sequential spending behavior (Saputra et al., 2019). Recent research highlights the
promise of hybrid ML–DL approaches, which combine the predictive power of deep neural networks with the interpretability of
tree-basedmodels(Gandharetal.,2024).Advancedfeatureselectionframeworksthatintegratestatisticalandevolutionarymethods
havealsobeenproposedtoreduceredundantfeatures,lowercomputationalcost,butretaindiscriminativepower(Siametal.,2025).
DLhasemergedasadominantparadigminrecentyearsduetoitsabilitytoautomaticallyextracthigh-levelrepresentationsfrom
rawtransactiondata(Duetal.,2023;Ziovirisetal.,2024).Deepneuralnetworkshavebeenshowntoscalewelltodistributedsystems
andmaintaingeneralizationindynamicenvironments(PrasadandSrikanth,2024).Furthermore,theirabilitytoperformanomaly
detectionandrepresentationlearningmakesthemhighlyeffectivewhenfraudpatternsevolveovertime(Mehbodniyaetal.,2021).
Nevertheless,DLmodelsoftenrequirelargevolumesoflabeleddata,demandsubstantialcomputationalresources,andsufferfrom
limitedinterpretability,posingchallengesfordeploymentinhighlyregulatedfinancialenvironments(Mienyeetal.,2024).
Buildingontheseinsights,thepresentstudyaddressesthesegapsthroughacomprehensiveinvestigationofsupervisedMLap-
proachesforfrauddetectionoffinancialtransactions.Specifically,thestudy(i)systematicallycomparessevenMLmodels,including
logisticregression,randomforests,XGBoost,shallowanddeepneuralnetworks,andanovelhybridensemble;(ii)evaluatesimbalance
handlingstrategies,suchasclassweighting,focalloss,andthresholdoptimization;(iii) incorporatestransactional,temporal, and
identity-linked features to improve contextual predictive power; and (iv) applies SHAP-based interpretability analysis to ensure
transparencyandregulatorycompliance.Themaincontributionsofthisresearcharethreefold:(1)adetailedcharacterizationoffraud
patternsacrosstransactional,temporal,andidentitydimensions;(2)ahybridensemblemodelintegratingEnhancedXGBoostanda
DeepNeuralNetwork,achievingstrongpredictiveperformanceonthedatasetweconsider;and(3)anadaptiveevaluationframework
thatintegratesmodelinterpretabilityanddynamicthresholdoptimizationtosupportpracticalapplicationinfrauddetectionsystems.
2. Relatedwork
ResearchonfrauddetectionhaslargelyfocusedonsupervisedMLapproaches,aimingtoaddressthechallengesposedbyreal-
world datasets that are highly imbalanced, high-dimensional, complex and often noisy. Existing studies can be broadly classified
intofourthemes:(i)modelselection,(ii)imbalance-handlingtechniques,(iii)featureengineering,and(iv)theintegrationofidentity-
basedvariablestoimprovepredictivepowerofthemodel.
Supervisedlearningmodelsremainfundamentalformostmodernfrauddetectionsystems(BinSulaiman,SchetininandSant,2022;
Georgeetal.,2025).Thesemodelslearnparametersorhyper-parametersfromlabeledhistoricaldataandbuildthemodeltopredict
whethernewtransactionsarefraudorlegitimate.Anotableadvancementinthisareaisthedistributeddeepneuralnetwork(DDNN)
proposedbyLeietal.(2023),whichbalancespredictiveaccuracywithuserprivacybyallowinginstitutionstotrainlocalmodelsand
share onlymodelparameterswithacentralserver.Thisfederated-styleapproach notonlypreservesdataconfidentialitybutalso
improves efficiency through distributed computation, yielding superior accuracy, precision, recall, and F1-scores compared to
centralizedmodels(XiaandSaha,2025).
Interpretablemodelssuchasdecisiontreesandrandomforestshavealsobeenwidelyusedinfrauddetection(Leeetal.,2025;Sun,
2025;Wajgietal.,2024).Decisiontreesarevaluedfortheirtransparencybutarepronetooverfitting,whereasrandomforestsmitigate
thisissuethroughtreeaggregationandhyperparametertuning(ShahandSharma,2023).However,bothapproachesaresensitiveto
severe class imbalance. A comprehensive evaluation of 66 algorithm–resampling combinations by Alfaiz and Fati (2022) highlighted
thatpairingstrongclassifierssuchasCatBoostwitheffectiveundersamplingmethodslikeAllKNNcanachievestate-of-the-artper-
formanceintermsofF1-score,recall,andAUC.
Classimbalanceremainsoneofthemostcriticalobstaclesinfrauddetection(Baisholanetal.,2025;Velardeetal.,2023).When
fraudcasesaccountforlessthan1%oftransactions,modelsaresignificantlybiasedtowardthemajorityclass,leadingtopoorrecall.
Numerousresamplingandreweightingtechniqueshavebeenproposedtomitigatethischallenge.Forexample,AlamriandYkhlef
2

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
(2024)introducedBCB-SMOTE,ahybridmethodcombiningTomeklinks,clustering,andborderlinesyntheticoversampling,which
achievedanF1-scoreof85.2%whilereducingoverlapbetweenclasses.Similarly,Ileberietal.(2021)showedthatcombiningSMOTE
withAdaBoostimproveddetectionratesacrossclassifiers,andLahbissandChtouki(2024)reportedthatSMOTE-ENNwithadvanced
modelssuchasRandomForestandLongShortTermMemory(LSTM)significantlyenhancedAUC-ROC.Moreover,Jiaoetal.(2022)
proposed DES-ICD, which integrates adaptive oversampling (AnnSMOTE) with dynamic ensemble selection to handle both class
imbalance and concept drift. By generating minority samples that reflect new concepts and selecting classifiers based on local
neighborhoodperformance,DES-ICDachievedsuperioraccuracyandrecallacrossmultiplerealandsyntheticdatasets.Thesefindings
highlightthatcarefuldesignofimbalancehandlingtechniquesiscrucialforachievinghighrecallwithoutsacrificingprecision.
Beyondclassimbalance,featureengineeringplaysapivotalroleinfrauddetection(AlamriandYkhlef,2024;Sharmaetal.,2025).
Theinclusionofbehavioralandidentity-basedattributeshasbeenshowntosignificantlyimprovemodelperformance.Forinstance,
Shiminetal.(2020)demonstratedthatcombiningfinancialtransactiondatawithidentity-linkedfeatures(e.g.,devicetype,email
domain)significantlyenhancedXGBoost'sROC-AUCto0.942ontheIEEE-CISdataset.Similarly,Lucasetal.(2019)appliedHidden
Markov Models to capture sequential spending behavior, which, when combined with Random Forest, improved precision–recall AUC.
Bahnsenetal.(2016)furtherextendedthislineofworkbymodelingperiodicspendingpatternswithvonMisesdistributions,yielding
a 13% reduction in financial losses. These studies collectively underscore that well-designed feature engineering strategies are
essentialforbuildingrobustanddiscriminativefrauddetectionmodels.
Ensembleandhybridlearningmethodsrepresentagrowingtrendinfrauddetectionresearch.Carcilloetal.(2021)combined
unsupervised anomaly detection with supervised learning, feeding outlier scores as features into classifiers to enable multi-level
detection. Dynamic ensemble selection approaches, such as the one proposed by Achakzai and Peng (2023), adaptively choose
classifiersbasedonlocalcompetenceandconsistentlyoutperformstaticensembles.Hybridmodelshavealsodemonstratedpromise;
for example, Jahnavi et al. (2024) combined decision trees with logistic regression to achieve 98.1% accuracy for the data they
considered,whileChaurasia,Kesharwani,Sharma,Sharma,andChugh(2024)confirmedthatXGBoostpairedwithdatabalancing
strategiesofferssuperiorrecallinrare-eventdetection.
Severalcomparativereviewshavesynthesizedfindingsacrossmodelsanddatasets.Pateletal.(2024)reportedthatwhiledeep
neuralnetworksoftenachievethehighestaccuracy(upto98.9%),simplermodelssuchaslogisticregressionandNaiveBayesremain
competitiveduetotheirinterpretabilityandhighefficiency.Similarly,Bhardwajetal.(2024)foundthatdeepneuralnetworkstrained
usingtheAdamoptimizerreached99.4%accuracyontheEuropeancreditcarddatasetandwerecomputationallyefficient,making
themwell-suitedforlarge-scaledataimplementation.
Taken together, prior work demonstrates that deep learning and advanced ensemble approaches frequently deliver superior
predictiveperformance,yetsimplermodelsretainvaluefortheirinterpretability,scalability,andeaseofapplication.Despitethese
advances,few studieshave simultaneouslyaddressedall major challenges, including classimbalance, feature selection, interpret-
ability,andintegrationofidentity-basedfeatures,withinaunifiedframework.Thisworkseekstoclosethisgapbysystematically
comparingmultiplesupervisedMLmodels,integratingadvancedimbalancehandlingtechniques,andleveragingfeatureengineering
todeliverascalable,interpretable,androbustfrauddetectionframework.
3. Materialsandmethods
Thisstudyadoptsasystematicandrigorousmethodologyforevaluatingsupervisedmachinelearningmodelsinthecontextof
financial fraud detection. The proposed framework is explicitly designed to address two major challenges inherent to large-scale
financial transaction data: high dimensionality and severe class imbalance. The methodological design is organized into four
sequentialphases,datapreprocessing,imbalancemitigation,modeltrainingwithhyperparameteroptimization,andpost-hocinter-
pretabilityanalysis.Eachphaseisimplementedtoensurebothmodelrobustnessandtransparency.Thefollowingsectionsprovide
detaileddescriptionsoftheproceduresandtechniquesappliedwithineachphase.
3.1. Dataanditsdescription
ThedatausedinthisstudyistheIEEE-CISfrauddetectiondataset,releasedthroughaKagglecompetitionincollaborationwith
Vesta,aglobalfraudpreventioncompany.Thisdatareflectsreal-worlde-commerceenvironmentswithanonymizedtransactionand
identityinformation,anditsverysuitedfortestingalgorithmsandcomputationalframeworkdesignedforfrauddetectioninfinancial
transactions.Thetrainingsetcontainsover590,000records,ofwhichonlyabout3.5%arelabeledasfraud,whilethetestsetcontains
similarfeaturesbutdoesnotincludefraudlabels.ThedatasetcanbedownloadedfromtheofficialKagglecompetitionportal(https://
www.kaggle.com/competitions/ieee-fraud-detection/data).
Twomainfileswereprovidedforbothtrainingandtest:transaction.csv,whichcontainstransaction-levelattributes,andidentity.
csv, which includes device and identity-related variables. These files were merged using the TransactionID field to produce a
comprehensiveviewofeachtransaction.Thefeaturescanbegroupedintoseveralcategories,assummarizedinTable1.
Beyondthefeaturetypes,itisalsoimportanttoconsidertheoverallstatisticalprofileofthedataset.Basicdescriptivestatisticsare
providedinTable2.Thedatasetishighlyimbalanced,withfraudcasesrepresentingonlyasmallfractionoftransactions.Transaction
amounts vary widely, ranging from a few cents to over $10,000, with a median value of approximately $68. Additionally, many
identity-relatedfieldscontainsubstantialmissingvalues,highlightingthechallengesinherentinreal-worldfrauddetectionproblems.
These characteristics emphasize the dual challenges of extreme class imbalance and data high-dimensionality. These insights
directlyinformedthepreprocessingstrategiesandmodelingdecisionsdescribedinthefollowingsections.
3

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Table1
SummaryoffeaturegroupsintheIEEE-CISdataset.
Feature Group Description/Examples
Transaction features TransactionAmt, TransactionDT, ProductCD
Card attributes card1–card6 (e.g., card type, issuer, category)
Address codes addr1, addr2 (geographic location codes)
Engineered features C1–C14, D1–D15, V1–V339 (anonymized signals)
Email domains P_emaildomain, R_emaildomain
Identity features DeviceType, DeviceInfo, id12–id38 (browser, OS, network)
3.2. Datapreprocessing
The training dataset was constructed by merging transaction dataset and identity dataset on the TransactionID field, thereby
integratingtransaction-levelpaymentattributeswithdevice-andidentity-relatedfeatures.Thismergingstepwascrucialtocapture
bothbehavioralandcontextualfeaturesthatcandistinguishfraudfromlegitimatetransactions.Toaddressmissingdata,categorical
variables were imputed with the string “missing” so that models could treat absence of information as an additional informative
category.Fornumericalattributes,twodifferentstrategieswereadopteddependingonthemodeltype.Fortree-basedmethodssuchas
XGBoostandRandomForest,missingvalueswereretainedasNaN,allowingthesemodelstohandlemissingnessnativelyduringsplit
optimization.
Sinceneuralnetworkmodels(bothANNandDNN)cannotprocessmissingvaluesdirectly,forallneuralnetwork-basedmodels,
numerical features with missing values were imputed using the median of each feature computed from the training set. Median
imputationwaschosenduetoitsrobustnesstoskeweddistributionsandextremevalues,whicharecommoninfinancialtransaction
data.Afterimputation,numericalfeatureswerestandardizedusingz-scorenormalizationtoensurestableandefficienttrainingofthe
neuralnetworks.Thishybridpreprocessingstrategyensuresthateachmodeltypeoperatesunderconditionsbestsuitedtoitsun-
derlyingassumptionswhilemaintainingconsistencyacrosstheexperimentalpipeline.
Categoricalfeatures,includingProductCD,card4,andDeviceType,weretransformedusinglabelencodingtoconvertstringcat-
egoriesintonumericalformwhilepreservingtheirdistinctidentities.Althoughmoresophisticatedencoders(e.g.,targetorone-hot
encoding) could be applied, label encoding was selected to maintain consistency across a high-dimensional feature space and
reducememoryoverhead.Inaddition,atemporalfeature,hour_of_day,wasderivedfromthecontinuousTransactionDTtimestampto
capture periodic spending behaviors that may indicate fraud, such as late-night or off–hour activity.
Following data preprocessing, the dataset was partitioned into training and validation subsets using an 80/20 stratified split.
Stratificationensuredthattheproportionoffraudtolegitimatetransactionswasmaintainedinbothsets,enablingafairandrepre-
sentativeevaluation.ThecomputationaldetailsofthispreprocessingandsplittingarepresentedinAlgorithm1.Thisapproachpre-
served the natural distribution of the data, which is essential for imbalanced classification problems. However, it also retained
potentialnoisefromweakorredundantfeatures,meaningthatsubsequentfeatureselectionandmodelregularizationwerecriticalfor
improvingrobustness.
4

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Table2
DescriptivestatisticsoftheIEEE-CIStrainingdataset.
Statistic Value
Total records ~590,000
Fraud proportion 3.5%
Transaction amount range $0.01 – $10,000+
Median transaction amount $68
Number of features (after merge) 434
3.3. Handlingclassimbalance
Fraudtransactionsrepresentedonlyabout3.5%ofthedataset,creatingasevereclassimbalancethatposedasignificantchallenge
formodeltraining.Ifleftunaddressed,mostclassifierswouldbecomebiasedtowardpredictingthemajorityclass(legitimatetrans-
actions),thereby achievingdeceptivelyhighaccuracybutfailingtoidentifytherarefraudcasesthat mattermostinpractice.To
mitigate this imbalance, cost-sensitive learning approaches were adopted. For gradient boosting models such as XGBoost, the
parametervalueofscale_pos_weightwassettotheratioofmajoritytominorityclassinstances,therebyinstructingthealgorithmto
assignhigherimportancetofraudcasesduringtraining.Forneuralnetworks,afocallossfunctionwasused.Unliketraditionalcross-
entropy,focallossdynamicallydown-weightswell-classifiedexamplesandfocuseslearningonharder,misclassifiedfraudcases.This
adaptationisparticularlyeffectivewhenfraudbehaviorexhibitshighdiversityandoverlapswithlegitimatetransactionpatterns.This
strategypreservedthenaturalclassdistributionofthedatasetandavoidedtheintroductionofsyntheticartifacts,whichareoftena
drawbackofoversamplingorSMOTE-basedtechniques.However,whilecost-sensitivemethodsimproverecall,theymaynotfully
resolveimbalanceinscenarioswherethedecisionboundarybetweenclassesishighlynon-linearoroverlapping.
3.4. Machinelearningmodels
Inthissection,weprovideabriefoverviewofthemachinelearningmodelsusedinthisstudytoensurethepaperremainsself-
contained. Five models were selected based on their suitability for handling structured, imbalanced data classification problems
and their diversity in algorithmic approach. Let {x i ;y i }n i=1 denote a training set of financial transaction data, where x i ∈ ℝ p is the p-
dimensional feature vector, and y i ∈ {0, 1} is the class label of fraud or non-fraud. We first consider Logistic Regression (LR), a linear
baselinemodelthatestimatestheconditionalprobabilityofthepositive(fraud)classas
̂y i = P(y i = 1|x i ) = σ(w ⊤ x i + b); (1)
where σ(z) = 1+ 1 e(cid:0) z is the logistic sigmoid function, and ̂y i ∈ [0; 1] represents the predicted probability of fraud. The unknown pa-
rameterswandbcanbeestimatedusingtheleastsquaresmethodormaximumlikelihoodestimation.
To capture non-linear patterns, we also apply a Random Forest (RF) model, which is an ensemble of T decision trees {ht }T t=1 . Each
treeistrainedonabootstrapsampleofthedatawithrandomfeaturesubsampling.Thefinalpredictionistheaverageofindividualtree
predictionsofprobability,
1 ∑T
̂y i = T h t (x i ); (2)
t=1
where ht (x i) ∈ [0, 1] denotes the probability assigned by tree t.
Asamorepowerfulalternative,XGBoostusesgradientboostingtoiterativelyconstructanadditivemodel,
̂y( i t)= ̂y( i t(cid:0) 1) + f t (x i ); (3)
whereft representstheregressiontreeaddedatiterationt.Theobjectivefunctionminimizedateachstepis
∑n
L( t) = ℓ(y i ; ̂y( i t)) + Ω(f t ); (4)
i=1
where ℓ(⋅) is a differentiable loss function, such as logistic loss, and Ω(⋅) is a regularization term penalizing tree complexity to prevent
overfitting.
Wefurtherexploreneuralnetwork-basedapproaches.TheArtificialNeuralNetwork(ANN)consideredhereisashallowfeed-
forward network with a single hidden layer. For hidden representations computed as h ¼ ϕ(W1 xi þ b1 ), where ϕ(⋅) is an activa-
tionfunctionsuchasReLU,thepredictedprobabilityisgivenby
̂y i = σ(w⊤ 2 h + b 2 ): (5)
Finally,weutilizeaDeepNeuralNetwork(DNN)withLhiddenlayers.Thepredictionisexpressedas
5

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
(cid:0) )
̂y i = σ f (L) ∘f (L(cid:0) 1) ∘⋯∘f (1) (x i ) ; (6)
where f (l) (⋅) represents the non-linear transformation at layer l. To address class imbalance, the DNN is trained using the focal loss
functiondefinedasfollows
∑n
L f ocal = (cid:0) α(1 (cid:0) ̂y i )γ y i loĝy i + (1 (cid:0) α)̂y γ i (1 (cid:0) y i )log(1 (cid:0) ̂y i ); (7)
i=1
where α balances the class weights and γ down-weights well-classified examples, focusing learning on harder cases.
The inclusion of these models provided both breadth and depth in evaluation. Logistic regression offered transparency and
interpretability,servingasabenchmarkforassessinggainsfrommorecomplexmodels.RandomforestsandXGBoostcapturednon-
linearinteractionsthroughensemblelearning,withXGBoosteffectivelyhandlingimbalanceviaclassweighting.Neuralnetworks
representedhigher-capacitylearners:theANNprovidedashallowdeeplearningbaseline,whiletheDNNleverageddeeperarchi-
tecturesandfocallossforimprovedrepresentationlearninginimbalancedfrauddetectiontasks.
To combine the strengths of gradient boosting and deep neural networks, a hybrid ensemble model was constructed using a
weightedaveragingstrategy.Inthisapproach,XGBoostandtheDNNweretrainedindependentlyonthesametrainingdata,andtheir
predictedprobabilitieswerecombinedusingaweightedlinearcombination.Specifically,thefinalensemblepredictionisgivenby
̂y i = λ⋅̂yX i GB+ (1 (cid:0) λ)⋅̂yD i NN; (8)
where ̂yXGBand ̂yDNNdenote the predicted probabilities from XGBoost and the DNN respectively, and λ is a weighting parameter.
i i
Inthishybridapproach,XGBoostcontributesstructuredfeaturelearningandinterpretability,whiletheDNNcapturesnon-linear
patterns,enablingrobustfrauddetectioninimbalancedandhigh-dimensionalenvironments.Theweights(0.6forXGBoost,0.4for
DNN)wereselectedbasedonvalidationperformance,givingslightlygreaterinfluencetoXGBoostduetoitsstabilityontabulardata
whilestillleveragingtheDNN'scapacitytorefinedecisionboundaries.Thisweightingschemeproducedthebestbalancebetween
recallandprecision,ensuringthattheensembleremainsbothaccurateandadaptableforpracticaldeployment.
For further clarification, in Algorithm 2, “tuning the threshold to maximize F1 on (y val) ” refers to selecting an optimal decision
thresholdthatconvertspredictedprobabilitiesintobinarylabels.Insteadofusingafixedthreshold(e.g.,0.5),arangeofcandidate
thresholdsisevaluated,andtheonethatmaximizestheF1-scoreonthevalidationsetischosen.Thisstepisparticularlyimportantin
imbalancedsettingssuchasfrauddetection,wherethedefaultthresholdoftenyieldspoorrecallfortheminorityclass.Optimizingthe
threshold with respect to the F1-score enables a better balance between precision and recall, improving detection performance.
Importantly,thresholdtuningisapost-trainingcalibrationstepratherthanpartofmodellearning.Modelparametersaretrained
exclusively on the training set, while the validation set is used only to determine the operating point on the precision–recall curve. No
parameterupdatesareperformedonthevalidationdata.Tolimitpotentialbias,thevalidationsetisstrictlyseparatedfromtraining
data,andtheselectedthresholdisfixedbeforefinalevaluation.Thispracticeisstandardinimbalancedclassificationandreflectsreal-
worlddeployment,wheredecisionthresholdsarecalibratedtomeetoperationalobjectives.Whilemoreconservativeapproaches(e.g.,
nestedcross-validation)couldfurtherreducebias,theyarecomputationallyexpensiveatthisscale.
6

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
3.5. Modelarchitectureandhyperparameterconfiguration
TheArtificialNeuralNetwork(ANN)modelconsistsoftwohiddenlayerswith128and64neurons,respectively.Bothhiddenlayers
employtheReLUactivationfunction,followedbydropoutlayerswitharateof0.3tomitigateoverfitting.Theoutputlayercontainsa
singleneuronwithasigmoidactivationfunctiontoproduceprobabilisticpredictionsforbinaryclassification.Themodelistrained
usingtheAdamoptimizerwithalearningrateof0.001andbinarycross-entropyloss.Trainingisconductedforupto20epochswitha
batchsizeof512,andearlystoppingwithapatienceof3epochsisappliedtopreventoverfitting.
The DeepNeural Network (DNN)is designedas a deeperarchitecture withthreehidden layers containing512, 256, and 128
neurons, respectively. Instead of standard ReLU activation, LeakyReLU is employed to mitigate the “dying ReLU” problem and improve
gradientpropagationindeepernetworks.Eachhiddenlayerisfollowedbybatchnormalizationanddropoutwithratesof0.4,0.4,and
0.3,respectively,toenhancetrainingstabilityandgeneralization.Theoutputlayerusesasigmoidactivationfunctiontoproduce
probabilityestimates.ThemodelistrainedusingtheAdamoptimizerwithalearningrateof0.001andfocalloss,whichisparticularly
effectiveinhandlingclassimbalancebyemphasizingdifficult-to-classifysamples.Trainingisperformedforupto20epochswitha
batchsizeof1024,withearlystoppingandlearningratereductionappliedtoimproveconvergence.
TheRandomForestmodelconsistsof100decisiontreeswithamaximumdepthof15.Classimbalanceishandledthroughbuilt-in
classweighting,ensuringthatminorityclasssamplesreceivehigherimportanceduringtraining.ThemodelutilizesallavailableCPU
cores to improve computational efficiency. The choice of tree depth and number of estimators reflects a balance between model
expressivenessandoverfittingcontrol.
Regularizationisincorporatedacrossallmodelstoenhancegeneralizationperformance.Intheneuralnetworkmodels,dropoutis
used to reduce overfitting by preventing co-adaptation of neurons, while batch normalization stabilizes training and accelerates
convergence.Classimbalanceisaddressedthroughcost-sensitivelearningtechniques,includingclassweightingandfocalloss,which
adjustthelearningprocesswithoutmodifyingtheoriginaldatadistribution.Earlystoppingisappliedtopreventoverfittingbyhalting
trainingwhenvalidationperformancenolongerimproves.
Regardingactivationfunctions,ReLUisusedintheANNduetoitscomputationalefficiencyandstrongempiricalperformance.In
thedeeperDNNarchitecture,LeakyReLUisadoptedtoavoidinactiveneuronsandimprovegradientflow.Thesigmoidactivation
functionisusedexclusivelyintheoutputlayer,asitisstandardforbinaryclassificationtasksandenablesprobabilisticinterpretation
ofpredictions.
Hyperparameterswereselectedbasedonacombinationofpriorliterature,empiricalvalidation,andcomputationalconsiderations.
While systematic hyperparameter tuning methods such as grid search or Bayesian optimization could potentially yield marginal
performanceimprovements,theseapproachesarecomputationallyexpensivegiventhescaleanddimensionalityofthedata.Instead,
weadoptapragmaticapproachbyusingwell-establishedconfigurationsandvalidatingthemthroughstratifiedtrain-validationsplits.
Furthermore,techniquessuchasearlystoppingandadaptivelearningrateschedulingprovideimplicittuningduringtraining,allowing
themodelstoconvergetosuitableparametersettingsefficiently.
3.6. Experimentaldesign
Themethodologicalframeworkdiscussedintheprevioussectionslaidthefoundationforastructuredexperimentaldesign.Having
defined the preprocessing pipeline, imbalance handling strategies, and predictive models, the next step was to implement these
methodsinacontrolledseriesofexperiments.Theseexperimentswerecarefullystructuredtotestmodelsofvaryingcomplexityunder
realisticfrauddetectionconditions.
3.6.1. Objectivesandrationale
Theprimaryobjectiveoftheexperimentswastoevaluatetheeffectivenessofvarioussupervisedmachinelearningmodelsfor
detecting fraud transactions using the IEEE-CIS dataset. Three considerations guided the experimental design. First, simple and
interpretablemodelswereassessedasbaselineapproaches.Second,ensemblemethods,includingRandomForestandXGBoost,were
examinedfortheirabilitytoimprovediscriminationundersevereclassimbalance.Third,deepneuralnetworksandhybridensembles
wereinvestigatedtocapturenon-linearpatternspotentiallymissedbytree-basedmethods.
Thisapproachreflectstheoperationalprioritiesoffrauddetection,whichrequireabalancebetweenpredictiveaccuracy,inter-
pretability, scalability, and computational efficiency. The experiments followed a staged workflow: dataset preparation and pre-
processing,classimbalancemitigation,evaluationofincreasinglycomplexmodelfamilies,andperformanceassessmentusingmetrics
appropriateforimbalancedclassification.TheoverallworkflowandtherangeofmodelsareillustratedinFig.1.
Scalabilityandcomputationalefficiencywerekeyfactorsinbothmodelselectionandexperimentaldesign,giventhelargescale
andhighdimensionalityofthedata.Theseconsiderationsinfluencednotonlywhichmodelswereevaluated,butalsohowtheywere
configuredandcompared.
Modelselectionwasguidedbytheneedtobalancepredictiveperformancewithcomputationalfeasibility.Tree-basedensemble
modelssuchasRandomForestandXGBoostwerechosenbecausetheyscaleefficientlytolargetabulardatasetsandprovidestrong
performancewithrelativelylowtrainingcomplexity.Inparticular,XGBoostincorporatesparallelizedtreeconstructionandoptimized
memoryusage,makingitsuitableforhigh-volumetransactionaldata.RandomForestservesasacomputationallyefficientbaseline,
enablingcomparisonwithmoreadvancedmodelswhilemaintainingstableandscalabletrainingbehavior.
Deeplearningmodels,includingANNandDNN,wereintroducedtocapturecomplexnon-linearrelationshipsthatmaynotbefully
exploited by tree-based methods. However, these models are computationally more expensive due to iterative gradient-based
7

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Fig.1. Stagedworkflowoftheexperimentaldesign,fromdatasetpreparationtoevaluation.
Table3
Comparisonofperformancemetricsduetodifferentimbalancehandlingstrategies.
Method ROC-AUC PR-AUC F1-score Precision Recall
SMOTE + ensemble 0.9037 0.6068 0.60 0.73 0.51
Class weighting þ focal loss (proposed) 0.9638 0.6582 0.74 0.78 0.69
optimization and the requirement for feature scaling. To ensure computational efficiency, the neural network architectures were
constrainedindepthandsize,andtrainingwascontrolledusingearlystopping,batchprocessing,andlearningratescheduling.
In addition to training efficiency, inference time was explicitly evaluated to assess the suitability of each model for real-time
deployment.Inferencelatencywasmeasured astheaveragepredictiontimepertransaction(millisecondspertransaction)onthe
validationset.Thismetricisparticularlyimportantinfrauddetectionsystems,wheremodelsmustprocesslargevolumesoftrans-
actionswithminimaldelay.ThemeasuredinferencetimesforallmodelsarereportedinTable4.
Thehybridensemblemodelwasexplicitlydesignedtobalancescalabilityandpredictiveperformance.XGBoostcontributeseffi-
cientfeaturelearningandfastinference,whiletheDNNenhancespredictivecapabilitythroughnon-linearrepresentationlearning.
Whileneuralnetworkmodelsincurhigherinferencecostduetoforwardpropagationthroughmultiplelayers,tree-basedmodelssuch
Table4
Comparativeperformanceofmodelsonfrauddetectiontask,includingexternalbenchmarkandinferencetime.
Model Accuracy Recall Precision F1-Score ROC-AUC PR-AUC InferenceTime
(ms/transaction)
Logistic regression (LR) 77% 0.69 0.10 0.18 0.7959 0.1772 0.02
Random forest (RF) 94% 0.68 0.33 0.45 0.9122 0.5856 0.15
XGBoost (XGB) 89% 0.81 0.22 0.35 0.9276 0.6187 0.08
Enhanced XGBoost (XGB-adv) 95% 0.83 0.42 0.55 0.9628 0.7676 0.09
Artificial neural network (ANN) 98% 0.43 0.91 0.59 0.9160 0.6403 0.25
Deep neural network (DNN) 98% 0.51 0.82 0.63 0.9182 0.6582 0.30
XGB + DNN ensemble 98% 0.69 0.78 0.74 0.9638 0.7897 0.35
OLightGBM (Taha and Malebary (2020)) 98% – 0.97 0.5695 0.9288 – –
8

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
as XGBoost provide lower latency through efficient decision-tree traversal. The hybrid ensemble introduces a modest additional
overheadbycombiningpredictionsfrombothmodels,butremainswithinpracticallimitsforreal-timeapplications.
Fromanapplicationperspective,thesefactorsarecritical.Frauddetectionsystemsmustprocesslargevolumesoftransactionswith
lowlatency.Theinclusionofinference-timeevaluationensuresthattheproposedapproachisnotonlyaccuratebutalsopracticalfor
deploymentinlatency-sensitiveenvironments.
3.6.2. Modelsunderevaluation
Sixmodels,representingdistinctmethodologicalfamilies,wereselectedtoevaluateperformanceacrossthecomparativeframe-
work.TraditionalbaselinesandensemblelearnersincludedLogisticRegressionasatransparent,low-costbenchmark;RandomForest,
whichcapturesnon-linearinteractionsandhandlesmissingdataeffectively;andXGBoost,agradientboostingalgorithmdesignedfor
high performance on imbalanced data through iterative boosting, regularization, and class weighting. Neural network models
comprisedashallowANNtoassesswhethermodestarchitecturescoulddetectfraudpatternsbeyondtree-basedmethods,andadeeper
DNNwithadditionalhiddenlayers,dropoutregularization,andfocallosstoenhancerepresentationandhandleclassimbalance.Both
modelsweretrainedindependently,andtheirpredictedprobabilitieswerecombinedusingalinearweightingscheme.Thisapproach
avoids the complexity of stacking while still leveraging the complementary strengths of boosting and deep learning models. This
hybridintegrationleveragedbothstructuredfeaturelearninganddeeprepresentations,aimingtoimprovepredictiveperformancein
real-worldfrauddetection.
3.6.3. Evaluationframework
Modelevaluationinfrauddetectionrequirescarefulconsiderationofextremeclassimbalance.Overallaccuracywasexcludeddue
to its tendency to overstate performance in majority-dominated datasets. Instead, a combination of complementary metrics was
employedtoassessbothdetectioneffectivenessandoperationalimpact.Recall(sensitivity)wasprioritizedtominimizecostlyfalse
negatives,whileprecisionensuredthatgainsinrecalldidnotleadtoexcessivefalsealarms.TheF1-scoreprovidedabalancedmeasure
ofthistrade-off.DiscriminativeabilitywascapturedviaROC-AUC,withadditionalemphasisonPR-AUC,whichbetterreflectsper-
formanceontheminority(fraud)class.Finally,acost-sensitiveadjustmentpenalizedfalsenegativesmoreheavilythanfalsepositives,
aligningevaluationwiththefinancialconsequencesofundetectedfraud.Thismulti-metricframeworkensuredmodelswereassessed
forbothpredictiveaccuracyandpracticalutility.
4. Results
Thissectionintegratesbothexploratorydataanalysisandmodeling,providingaunifiedpresentationoffindings.Exploratorydata
analysisisincorporateddirectlyintotheresultstoillustratehowtransactioncharacteristicsandfeaturedistributionsinformsubse-
quentmodelperformance.Thesubsectionsarestructuredtohighlightspecificaspectsofthedataandconnectthemtofrauddetection
outcomes.
4.1. Frauddistributionandclassimbalance
The firststepin characterizingthe dataset wasto assessthe distribution offraud versuslegitimatetransactions. Based on the
processeddatasetusedinthisstudy,thereare16,530fraudtransactionsoutofatotalof472,432records,correspondingtoafraud
proportionofapproximately3.5%.Thisvaluewasverifieddirectlyfromthedataas
∑
n y 16530
Fraud Ratio = i=1 i= ≈ 0:035:
n 472432
Althoughthislevelofimbalanceislessextremethanincertainreal-worldfinancialdatasets,itstillpresentsasignificantchallenge
forclassificationmodels.Anaiveclassifierthatalwayspredictsthemajority(non-fraud)classwouldachieveapproximately96.5%
accuracy,yetitwouldfailtodetectanyfraudtransactions.Thisdemonstratesthataccuracyaloneisnotanappropriatemetricfor
evaluatingfrauddetectionperformance.Toaddressthisissue,evaluationmetricssuchasprecision,recall,F1-score,ROC-AUC,and
PR-AUCareusedthroughoutthisstudy,astheybetterreflectperformanceontheminorityclass.
4.2. Evaluationofclassimbalancehandlingstrategies-SMOTE
Classimbalanceisafundamentalchallengeinfrauddetection,wherefraudtransactionstypicallyconstituteonlyasmallfractionof
thedataset.Inthisstudy,weprimarilyaddressclassimbalancethroughcost-sensitivelearningtechniques,includingclassweighting,
focal loss, and threshold optimization. To provide a more comprehensive evaluation, we also investigate the effectiveness of the
SyntheticMinorityOver-samplingTechnique(SMOTE).SMOTEgeneratessyntheticminorityclasssamplesbyinterpolatingbetween
existingminorityinstances,therebyincreasingtherepresentationoffraudtransactionsinthetrainingdata.SMOTEwasappliedtothe
trainingdatasetpriortomodelfitting.Specifically,asamplingratioof0.2wasused,meaningthattheminorityclasswasincreasedto
20%ofthemajorityclass.AfterapplyingSMOTE,theaugmenteddatasetwasusedtotrainboththeXGBoostanddeepneuralnetwork
componentsoftheensemblemodel,followingthesamepipelineasthebaselineapproach.
Theresultsindicatethattheproposedcost-sensitiveapproachsignificantlyoutperformstheSMOTE-basedmodelacrossalleval-
uationmetrics.Inparticular,theproposedmethodachieveshigherROC-AUC,PR-AUC,andF1-score,demonstratingbetteroverall
9

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
discriminationandbalancebetweenprecisionandrecall.Forcompleteness,wenotethatgenerativeapproachessuchasGAN-based
methodshavealsobeenproposedforimbalancehandling.However,thesemethodsintroducesignificantcomputationalcomplexity
andaredifficulttostabilizeinhigh-dimensionaltabulardata.Giventhesechallenges,andthestrongperformanceofcost-sensitive
learning observed in our experiments, we do not pursue GAN-based methods in this study. Overall, the experimental results in
Table3demonstratethatcost-sensitivelearningprovidesamoreeffectiveandstableapproachtohandlingclassimbalanceinthe
datasetcomparedtoSMOTE,makingitamoresuitablechoicefortabularfrauddetectiontasks.
4.3. Transactionandproductpatterns
Fraud activity often manifests through systematic behaviors rather than random noise, making transaction characteristics an
importantsourceofdiscriminativefeatures.Inparticular,monetaryvalueandproducttyperevealcleardifferencesbetweenfraudand
legitimatetransactions, asillustratedinFig. 2.Fig.2a presentsthe distributionoftransaction amountsby class.Fraud activity is
disproportionately concentrated in very low value transactions, often below 200 USD, which suggests that fraudsters frequently
conduct small “test” purchases to confirm the validity of stolen credentials before escalating to larger transactions. At the other
extreme,thereisalsoavisibleconcentrationoffraudinveryhighvaluepurchases,reflectingopportunisticattemptstomaximize
financialgainonceanaccounthasbeencompromised.Legitimatetransactions,bycontrast,aremoreevenlyspreadacrosstherange
butclustermostheavilyinthemidvaluesegment,particularlybelow500USD,afterwhichtheirfrequencydeclinessharply.This
divergence between fraud and legitimate spending behaviors highlights the deliberate strategies used by fraudsters to balance
concealmentandprofitability.Fig.2bshowsfraudprevalenceacrossproductcategories.FraudratesarehighestincategoryC,fol-
lowedbycategoryS,whereascategoriesH,R,andespeciallyWexhibitmuchlowerlevelsoffraudactivity.Thesediscrepanciesalign
with differences in product risk profiles: categories dominated by digital or card not present transactions are more vulnerable to
exploitation,whilethosetiedtophysicalgoodsorrequiringstrongerverificationdemonstrategreaterresilience.Incorporatingsuch
product level distinctions into predictive models provides highly discriminative signals that enhance the effectiveness of both
ensembleandneuralnetworkbasedapproachestofrauddetection.
4.4. Temporalandgeolocationpatternsoffraud
Fraudtransactionsalsoexhibitsystematictemporalandgeographicalbehaviorsratherthanoccurringuniformlyacrosstimeand
space.Thesepatterns,summarizedinFig.3,revealhowfraudriskisinfluencedbydailycycles,weeklyrhythms,andregionalcontexts.
Fig.3ashowsfrauddistributionacrosshoursoftheday.Fraudactivitypeaksduringlate-nightandearly-morninghours,apattern
consistentwithreducedcustomervigilanceandlowerinstitutionalmonitoringduringoff-peakperiods.Fig.3bpresentsthedistri-
bution of fraud rates by day of the week. The x-axis represents the seven days (Monday to Sunday), obtained by mapping the
transactiontimelineintoaweeklycycleusingmodulararithmeticonthetransactiondayindex.Thistransformationconvertsthe
continuoustransactiontimelineintoacategoricalrepresentationthatcapturesweeklyperiodicbehavior.Theresultsindicatethat
fraudratesarerelativelystableacrossweekdays,withaslightdecreaseobservedonFridaysandmoderateincreasesduringweekends,
particularlyonSaturdayandSunday.Thispatternmayreflectreducedmonitoringandloweroperationaloversightduringweekends,
aswellasincreasedonlinetransactionactivity,whichcancreatemoreopportunitiesforfraudbehavior.Thelowerfraudrateon
Fridays may be associated with more structured transaction patterns and stronger institutional controls during standard business
periods.Whiletemporalvariationexists,fraudisnotstronglyconcentratedonasingledaybutinsteadreflectsbroaderbehavioraland
operationaldynamics.Byexplicitlyencodingtheday-of-weekstructure,thisvisualizationprovidesaclearerandmoreinterpretable
representationofweeklyfraudpatternscomparedtotheoriginalsequentialtime-basedplot.Fig.3canddhighlightgeographical
differences. Fraud rates vary significantly across regions and countries, with certain locations showing disproportionately high
prevalence. These discrepancies may reflect both differences in fraudster targeting strategies and variability in regional payment
Fig.2. Fraudpatternsacrosstransactionamountsandproductcategories.
10

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Fig.3. Temporalandspatialfraudpatterns:(a)hourofday;(b)dayofweek;(c)region;(d)country.
infrastructures.Suchspatialheterogeneityreinforcesthevalueofincorporatinggeolocationfeaturesintofrauddetectionmodels,as
theyprovidepowerfuldiscriminativesignalswhencombinedwithtransactionandidentityattributes.
Temporal and geolocation information are explicitly incorporated into the predictive models through feature engineering and
preprocessing,ratherthanbeingusedsolelyforexploratoryvisualization.TemporalinformationisderiveddirectlyfromtheTrans-
actionDTvariable,whichrepresentstheelapsedtimesinceareferencepoint.Fromthisvariable,thehourofthedayisconstructedas:
( )
TransactionDT
hour_of_day = mod 24: (9)
3600
Thistransformationconvertsrawtimestampsintoacyclicaldailyfeaturethatcapturestime-of-dayfraudpatternsobservedduring
exploratoryanalysis.Theresultingvariableisincludedasanumericalfeatureinthemodelinput.
Geolocationinformationisincorporatedusingtheaddr1(region)andaddr2(country)variablesprovidedinthedataset.Asthese
variablesarecategorical,theyareencodedusinglabelencodingduringpreprocessing,whereeachuniquecategoryismappedtoa
numericalvalue.Thisrepresentationenablesbothtree-basedmodelsandneuralnetworkstolearnlocation-specificfraudpatterns.
Followingfeatureengineeringandencoding,alltemporalandgeolocationvariablesareincludedinthefinalfeaturematrixX,
whichisusedtotrainallmodelsinthisstudy,includingRandomForest,XGBoost,ANN,DNN,andthehybridensemble.Consequently,
themodelsareabletodirectlylearnfromtemporalcyclesandgeographicalriskpatternsidentifiedinthedata.Byincorporatingthese
engineeredfeaturesintothetrainingprocess,thetemporalandspatialpatternsdiscussedinSection4.3arenotonlyobservedbutare
activelyleveragedtoimprovefrauddetectionperformance.
4.5. Identity-basedfeatureinsights
Identity-related features provide some of the strongest discriminative signals in fraud detection, and Fig. 4 highlights three
representativepatterns.Fig.4ashowsthatfreeemaildomainsaredisproportionatelyassociatedwithfraudactivity,whereasinsti-
tutional or corporate domains exhibit much lower fraud rates, reflecting fraudsters’ preference for anonymous or disposable services.
Fig. 4b compares fraud rates across device types, with mobile and tablet transactions showing higher fraud levels than desktop,
consistentwithweakerauthenticationmechanismsandlessreliabledevicefingerprinting.Fig.4cillustratesvariationbydevicein-
formation,wherecertainidentifiersappeardisproportionatelyinfraudtransactions,suggestingtheuseofemulatedorspoofeddevices
11

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Fig.4. Identity-basedfraudpatterns:(a)emaildomain;(b)devicetype;(c)deviceinformation.
or the systematic reuse of compromised profiles. Together, these findings underscore why identity-linked attributes are heavily
weightedbybothtree-basedensemblesanddeeplearningmodelsinfrauddetection.
4.6. Resultsofmodelperformance
Thissectionpresentsacomparativeevaluationofallsevenmachinelearningmodelsdevelopedfortransactionfrauddetection:
LogisticRegression(LR),RandomForest(RF),XGBoost(XGB),EnhancedXGBoost(XGB-Adv),ArtificialNeuralNetwork(ANN),Deep
Neural Network (DNN), and the XGBoost + DNN Ensemble. Table 4 summarizes the validation performance of all models.
MetricsincludeROC-AUCandPR-AUCforrankingcapability,aswellasaccuracy,precision,recall,andF1-scoreforfrauddetection
effectiveness.Inaddition,inferencetime(measuredinmillisecondspertransaction)isreportedtoassesscomputationalefficiencyin
real-timedeploymentscenarios.
Theresultsshowaclearperformancegapbetweenbaselinemodelsandadvancedapproaches.LogisticRegressionsuffersfromlow
precision(0.10)andF1-score(0.18),makingitunsuitableforfrauddetection.RandomForestimprovesonthesemetrics,reachingan
F1-scoreof0.45,butstillfallsbehindgradientboostingmethodsincapturingcomplexrelationshipsinthedata.StandardXGBoost
raisesrecallto0.81,boostingfraudcapturerates,butprecision(0.22)remainslow,leadingtoahigherfalse-positiverate.
EnhancedXGBoostdemonstratesthemostsignificantimprovementamongsinglemodels,deliveringthehighestrecall(0.83)and
substantially better precision (0.42) than standard XGBoost. This balance results in a higher F1-score (0.55) and strong PR-AUC
(0.7676), reflecting better performance in the imbalanced fraud detection setting. The improvement can be attributed to careful
hyperparameter tuning and regularization, which reduce overfitting while improving fraud detection sensitivity. For use cases
prioritizingmaximumfraudcapturewithacceptablefalsepositives,EnhancedXGBoostisastrongcandidate.
The XGB + DNN Ensemble outperforms all other models in overall balance, achieving the highest F1-score (0.74) and PR-AUC
(0.7897), alongside a high recall (0.69) and precision (0.78). By combining Enhanced XGBoost's structuredfeature learning with
theDNN'sdeeprepresentationcapability,theensemblereducesweaknessespresentineachstandalonemodel.Thismakesitwell-
suitedforreal-worldusage,wherebothdetectingfraudandminimizingfalsepositivesarecriticalforefficiencyandcustomertrust.
12

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
WhileTable4showsthatsomeperformancedifferences(e.g.,ROC-AUCof0.9638vs.0.9628)appearsmall,itisimportantto
determine whether these improvements are statistically meaningful and consistent rather than artifacts of a particular train–validation
split.Toaddressthis,additionalexperimentswereconductedusingmultiplerandomdatapartitions.Specifically,thedatasetwassplit
intotraining (80%) andvalidation (20%) setsacrossthree differentrandom seeds,using stratifiedsamplingto preservetheclass
imbalance. For each split, both the Enhanced XGBoost model and the proposed XGB + DNN Ensemble were trained independently and
evaluatedonthecorrespondingvalidationset.
The evaluation metric used for comparison is ROC-AUC. Results are summarized as mean ± standard deviation across the three
runs. The Enhanced XGBoost model achieved an average ROC-AUC of 0.9223 ± 0.0019, while the proposed ensemble achieved
0.9274 ± 0.0025. The ensemble consistently outperformed the baseline model across all splits. To formally assess whether this
improvementisstatisticallysignificant,apairedt-testwasconductedontheROC-AUCscoresobtainedfromeachsplit.Thistestis
appropriatesincebothmodelsareevaluatedonidenticalvalidationpartitions,enablingadirectpairedcomparison.Theresultingp-
valueis0.0054,whichiswellbelowtheconventionalsignificancethresholdof0.05,indicatingthattheimprovementisstatistically
significantandunlikelytobeduetorandomvariation.
Furthermore,thesmallstandarddeviationobservedforbothmodelsindicatesstableperformanceacrossdifferentdatasplits.This
demonstrates that the results are robust and not sensitive to the specific 80/20 partition of the data, despite the relatively small
proportionoffraudcases.TheoverallevaluationprocedurefollowsthetrainingandvalidationpipelinedescribedinAlgorithm2,
extended across multiple randomized splits. Overall, these results demonstrate that the proposed XGB + DNN Ensemble provides a
consistentandstatisticallysignificantimprovementoverthebaselinemodel.Whilemoreextensivevalidationstrategiessuchask-fold
cross-validationcouldfurtherstrengthenthisanalysis,thecurrentfindingsalreadyprovidestrongempiricalevidencesupportingthe
robustnessandreliabilityoftheproposedapproach.
OLightGBM,anoptimizedversionoftheLightGradientBoostingMachine(LightGBM),proposedbyTahaandMalebary(2020),is
incorporatedintothemaincomparativeresults(Table4)toprovideaunifiedandconsistentbenchmarkacrossallmodels,ratherthan
beingpresentedinaseparatesubsection.OLightGBMenhancesthestandardframeworkthroughBayesian-basedhyperparameteropti-
mizationtoautomaticallytunemodelparametersandimprovepredictiveperformance.LightGBMitselfisagradientboostingalgorithm
basedondecisiontrees,designedforefficiencyandscalability.Itemploystechniquessuchasgradient-basedone-sidesampling(GOSS)
andexclusivefeaturebundling(EFB)toreducecomputationalcomplexitywhilemaintaininghighpredictiveaccuracy.TheOLightGBM
approachbuildsuponthisfoundationbyoptimizinghyperparametersgoverningtreegrowthandlearningdynamics.
ThereportedresultsforOLightGBMaretakendirectlyfromtheoriginalstudy,whereitachievedaROC-AUCof0.9288,accuracyof
98.40%(roundedto98%),precisionof97.34%(roundedto0.97),andF1-scoreof0.5695.AsshowninTable4,boththeEnhanced
XGBoost and the proposed XGB + DNN Ensemble outperform OLightGBM in terms of ROC-AUC, achieving 0.9628 and 0.9638,
respectively. This indicates that the proposed models provide improved discriminative capability relative to a strong published
benchmark.
ItisimportanttonotethattheOLightGBMresultsaretakenfromtheoriginalpublicationandmaybebasedondifferentdatasets,
preprocessingpipelines,andevaluationprotocols.Therefore,thiscomparisonisintendedtoprovidecontextualbenchmarkingrather
thanastrictlycontrolledexperimentalcomparison.Nevertheless,theresultssuggestthattheproposedmodelsarecompetitivewith,
andinthiscaseoutperform,existingstate-of-the-artapproaches.
Inadditiontopredictiveperformance,inferencetimeresultsreportedinTable4provideimportantinsightsintothecomputational
efficiency of each model in real-time deployment scenarios. Tree-based models, particularly XGBoost (0.08 ms/transaction) and
EnhancedXGBoost(0.09ms/transaction),achievelowinferencelatencyduetoefficientdecision-treetraversal,makingthemhighly
suitableforlarge-scale,low-latencyfrauddetectionsystems.LogisticRegressionexhibitsthelowestlatencyoverall(0.02ms/trans-
action),althoughitspredictiveperformanceissubstantiallyweaker.
Incontrast,neuralnetworkmodelssuchasANN(0.25ms/transaction)andDNN(0.30ms/transaction)incurhigherinferencetimes
due to forward propagation through multiple layers. The hybrid XGB + DNN ensemble introduces additional computational overhead
bycombiningpredictionsfrombothmodels,resultinginthehighestlatency(0.35ms/transaction)amongtheevaluatedapproaches.
These results highlight a clear trade-off between predictive performance and computational efficiency. While the proposed
ensemble achieves the best overall detection performance, its higher latency may limitits applicability in ultra-low-latencyenvi-
ronments.Insuchcases,XGBoostprovidesastrongalternative,offeringcompetitivepredictiveperformancewithsignificantlylower
inferencetime,makingitparticularlyattractiveforreal-timefrauddetectionsystemswhererapiddecision-makingiscritical.
4.7. Comparisonwithsequentialmodel(LSTM)
To evaluate whether sequence-based modeling improves fraud detection performance, we implemented a Long Short-Term
Memory (LSTM) network as a representative state-of-the-art temporal model. Fraud detection is often considered inherently
sequential, as user behavior over time may reveal anomalous patterns. Therefore, incorporating an LSTM provides a meaningful
benchmarktoassesswhethermodelingtemporaldependenciesyieldsperformancegainsforthisdataset.
TheLSTMmodelwastrainedusingsliding-windowsequencesconstructedfromthetransactiondata,witheachsequencerepre-
sentingashorttemporalcontextoftransactions.Classimbalancewasaddressedusingaweightedbinarycross-entropylossfunctionto
ensurethatthemodeldoesnottriviallypredictthemajorityclass.However,experimentalresultsdemonstratethattheLSTMperforms
substantiallyworsethantheproposedhybridensemblemodelacrossallevaluationmetrics(asshowninTable5).Specifically,the
LSTM achievesa ROC-AUC of 0.502,PR-AUC of 0.036, and F1-score of 0.013,indicating near-random classification behavior. In
13

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
contrast, the proposed XGBoost + DNN ensemble achieves substantially higher performance, with a ROC-AUC of 0.9638, PR-AUC of
0.6582,andF1-scoreof0.74(seeTable6).
ThepoorperformanceoftheLSTMcanbeattributedtothestructuralcharacteristicsoftheIEEE-CISdataset.Althoughthedataset
includesatemporalfeature(TransactionDT),itdoesnotprovideconsistentuser-levelsequencesorlong-termbehavioralhistories.
Transactionsarenotreliablygroupedbyindividualusers,andtemporalorderingalonedoesnotguaranteemeaningfulsequential
dependencies.Asaresult,theconstructedsequenceslackcoherentbehavioralpatterns,limitingtheabilityofsequence-basedmodels
tolearndiscriminativetemporalfeatures.Incontrast,theproposedhybridensemblemodelisbetteralignedwiththetabularandhigh-
dimensionalnatureofthedataset.XGBoosteffectivelycapturescomplexfeatureinteractions,handlesmissingvalues,andisrobustto
noisyandsparsefeaturescommonlyfoundinfrauddetectiondata.The DNNcomponentcomplementsthisbylearning nonlinear
representations and capturinghigher-order feature interactions. By combining these twomodels, theensemble leverages comple-
mentarystrengths,resultinginimprovedgeneralizationandsignificantlyhigherpredictiveperformance.
Thesefindingshighlightanimportantinsight:modeleffectivenessisstronglydependentontheunderlyingdatastructure.While
sequence-basedmodelssuchasLSTMarepowerfulfortaskswithwell-definedtemporaldependencies,theyarelesssuitablefortabular
fraud detection datasets with weak or irregular sequential patterns. In such cases, hybrid ensemble approaches provide a more
effectiveandpracticalsolution.
4.8. Comparisonwithkagglestate-of-the-art
Tofurtherevaluatetheeffectivenessoftheproposedmodel,wecompareourresultswithtop-performingsolutionsfromtheIEEE-
CISKagglefrauddetectioncompetition.
Accordingtothe1stplacesolutionoftheIEEE-CISKagglecompetition(Deotteetal.,2019),thefinalmodelwasanensembleof
gradientboostingalgorithms,includingXGBoost,LightGBM,andCatBoost,combinedwithextensivefeatureengineering,validation
strategies,andstackingtechniques.ThisapproachachievedaprivateleaderboardROC-AUCofapproximately0.9459andapublic
leaderboardscoreof0.9677.Similarly,the5thplacesolution(H.M.etal.,2019)reliedonanensembleofLightGBMmodelswith
user-levelfeatureaggregationandachievedaprivateleaderboardscoreof0.9425.Theseresultsdemonstratethattree-basedensemble
methodsareconsistentlyeffectiveforthisdataset.
Incomparison,theproposedhybridensembleachievesaROC-AUCof0.9638andF1-scoreof0.74,demonstratingcompetitive
performancerelativetothesestate-of-the-artsolutions.ItisimportanttonotethatdirectcomparisonwithKaggleleaderboardresults
isnotstrictlyequivalent,ascompetitionsettingsinvolvehiddentestsetsandmorestringentvalidationprotocols.Nevertheless,the
resultsindicatethattheproposedmodelachievesstrongpredictiveperformancewithinastandardexperimentalframework.Unlike
the Kaggle-winning solutions, which rely heavily on complex feature engineering and dataset-specific techniques, the proposed
methodemphasizesaprincipledintegrationoftree-basedlearninganddeepneuralnetworks.Thisresultsinasimpler,morerepro-
ducible modeling pipeline while maintaining strong predictive performance and interpretability through SHAP-based analysis.
Interestingly,theobservationsreportedintheKagglewinningsolutionfurthersupportourfindings.
4.9. ROC and Precision–Recall curve analysis
Thissectioncomparesfourmodelstoevaluatehowtheproposedapproachesperformagainststrongbaselines.RandomForestis
includedasarepresentativeoftraditionalmachinelearningmethods,whiletheDeepNeuralNetworkrepresentsdeeplearningap-
proaches. These are compared with the Enhanced XGBoost (XGB-Adv) and the XGB + DNN Ensemble, which combine boosting and
neuralnetworks.Thiscomparisonhighlightstheimprovementsoftheproposedmethodsoverbothclassicalanddeeplearningmodels.
Fig. 6 presents the ROC and Precision–Recall (PR) curves for the four models. Both plots confirm the superior performance of the
proposed methods over the baselines. In Fig. 5a, the XGB + DNN Ensemble achieved the highest ROC-AUC of 0.9638, followed closely
byXGB-Advat0.9628.Amongthebaselines,theDNN(0.9182)slightlyoutperformedtheRF(0.9122).Thesteepinitialslopeand
proximity of the proposed models’ curves to the top-left corner illustrate their strong discriminative ability across thresholds. Fig. 5b
shows the PR curves, which are more informative for imbalanced datasets. The XGB + DNN Ensemble again outperformed all models
Table5
PerformancecomparisonbetweenLSTMandtheproposedensemblemodel.
Model ROC-AUC PR-AUC F1-score Precision Recall
LSTM 0.502 0.036 0.013 0.030 0.008
XGB + DNN ensemble 0.9638 0.6582 0.74 0.78 0.69
Table6
ComparisonwithKaggletopsolutions.
Method ROC-AUC PR-AUC F1-score
Kaggle 1st place ensemble [46] 0.94–0.95 – –
Kaggle 5th place LightGBM ensemble [47] 0.94 – –
Proposed XGB þ DNN ensemble 0.9638 0.6582 0.74
14

N.D. Anh Luong, S. Xie  The Journal of Finance and Data Science 12 (2026) 100195
|     |     |     |     |     |     |     |     |     |     |     |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
Fig. 5. ROC and Precision–Recall curve analysis for baseline and proposed models: (a) ROC curves; (b) PR curves.
|     |     |     |     |     |      |           |     importance–bar |     |       |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --------- | ------------------ | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     | Fig. | 6. Global | feature            |     | plot. |     |     |     |     |
withanAveragePrecision(AP)of0.7897,followedbyXGB-Advat0.7676.Amongthebaselines,theDNNachieved0.6403,out-
performingtheRFat0.5856.Theproposedmodelsmaintainhigherprecisionatvaryingrecalllevels,demonstratingsuperiorhandling
| oftheminorityfraudclass.   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                            |     |     |     |     |     |     |     |     |     |     |     |     |     |
TheresultsdemonstratethatwhiletraditionalmodelssuchasLogisticRegressionandRandomForestprovideusefulbaselines,they
|     |     |     |     |     |     |     |     |     |     |     |     |  +    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
fall short under severe class imbalance. Enhanced XGBoost achieved substantial gains, and the hybrid XGB DNN Ensemble
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consistentlyoutperformedallotherapproaches,deliveringthehighestrecall,F1-score,ROC-AUC,andPR-AUC.Exploratoryanalyses
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
furtherrevealedclearfraudpatternsacrosstransactionamounts,productcategories,temporalcycles,andidentity-relatedfeatures,
|     |     |     |     |     |     |     |     |     |     |     |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
confirming their importance as discriminative signals. Taken together, these findings underscore both the necessity of advanced
|     |     |     |     |     |     |     |     |     |     |     |     |       |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
ensemblemethodsandthevalueofincorporatingdomain-specificpatterns,providingacomprehensivefoundationforfrauddetection
pipelines.
15

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
4.10. Resultsonfeatureinterpretability-SHAPbasedfeatureanalysis
Thissectionextendstheanalysisbeyondperformancemetricstointerprettheresultsandtheirpracticalsignificance.Whilethe
previoussectionidentifiedthebest-performingmodelsunderclassimbalance,thefocushereisonunderstandingthemechanisms
drivingtheirsuccess,theinsightsprovidedbykeyfeatures,andtheirimplicationsforreal-worldfrauddetection.Interpretabilityis
particularlycriticalinfinancialapplications,wheretransparencyandaccountabilityarerequiredfordeployment.Tothisend,SHAP
valuesarecomputedfortheEnhancedXGBoostmodel,thebest-performingsinglelearner,toquantifybothglobalandlocalfeature
contributions.Theanalysisisconductedfromtwocomplementaryperspectives:(i)globalfeatureimportance,usingmeanabsolute
SHAPvaluestoidentifythemostinfluentialpredictorsacrossalltransactions,and(ii)localinterpretation,usingSHAPbeeswarmplots
toexaminehowfeaturevalues,theirdirection,anddistributioninfluencefraudpredictionsattheinstancelevel.
4.10.1. Globalfeatureimportanceinfraudcontext
TheglobalSHAPimportanceplot(Fig.6)showsthatTransactionAmtisthemostinfluentialfeature,followedbyidentity-related
featuressuchascard6,C14,C1,andC13,aswellasbehavioralvariablesincludingV70andV258.
Thisrankingisconsistentwithpriorfrauddetectionstudies,wheretransactionamountandidentityconsistencyareprimaryin-
dicators of fraud. Fraud transactions often occur at extreme values: low-value transactions are used as “test” transactions to validate
stolen credentials, while high-value transactions reflect attempts to maximize financial gain. Identity-related features capture de-
viationsfromnormaluserbehavior.Inlegitimatetransactions,thesefeaturestendtobestable,whereasfraudintroducesanomalies
suchasunusualtransactioncountsorinconsistentcardusage.Theimportanceofthesefeaturesconfirmsthatfrauddetectionrelies
heavilyonidentifyingsuchdeviations.
4.10.2. LocalSHAPinterpretationandfeatureeffects
The SHAP beeswarm plot shown in Fig. 7 provides detailed transaction-level insights by combining feature values with their
contributionstomodelpredictions.Inthebeeswarmplot,thehorizontalaxisrepresentsSHAPvalues,indicatingthemagnitudeand
directionofeachfeature'scontribution.PositiveSHAPvaluesincreasefraudlikelihood,whilenegativevaluesdecreaseit.Thecolor
gradient represents feature values (red = high, blue = low), allowing us to infer whether high or low values of a feature are associated
withfraud.
ForTransactionAmt,highvalues(redpoints)arepredominantlyassociatedwithpositiveSHAPvalues,indicatingincreasedfraud
risk.However,somelowvaluesalsocontributepositively,suggestingthatfrauddetectioncapturesbothhigh-valueexploitationand
low-valueprobingbehavior.Thisdemonstratesthatfraudriskcannotbeexplainedbysimplethresholdsbutdependsoncontextual
Fig. 7. Local explanation–beeswarm plot.
16

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
interactions.Forcard6,distinctclustersofSHAPvaluesindicatethatspecificcategoriesconsistentlyincreasefraudprobability.This
suggeststhatcertaincardtypesortransactionchannelsaremorevulnerable,likelyduetodifferencesinauthenticationmechanisms.
FeaturessuchasC14andC13exhibitasymmetricdistributions,whereextremevaluescorrespondtostrongpositiveSHAPcontri-
butions.Thisindicatesthatdeviationsfromnormalbehavioralpatternssignificantlyincreasefraudlikelihood,providingevidenceof
anomaly-baseddetection.TheV-seriesfeatures(e.g.,V70,V258)showwideandoverlappingSHAPdistributions,indicatingstrong
interactioneffects.Thesefeaturesdonotactindependentlybutcontributedifferentlydependingonthecontextofothervariables.This
highlightstheimportanceofmodelscapableofcapturingnon-linearrelationships.
4.10.3. Comparisonwithrandomforest
Forcomparison,theRandomForestfeatureimportanceplot(SeeFig.8)showsabroaderdistributionofinfluentialvariablesrather
thandominancebyasmallsubset.FeaturessuchasC14andC13emergeasthestrongestcontributors,whiletransaction-basedat-
tributeslikeTransactionAmt,V258,andV265,alongwithseveralV-seriesvariables,alsorankhighly.Thisbalanceindicatesthat
RandomForestreliesonbothidentitysignalsandbehavioraltransactionfeatures,capturingmultipledimensionsoffraudrisk.Im-
portances are more evenly spread across categories, suggesting that no single variable alone drives the predictions but rather a
combinationofcomplementarysignals.
Whilethisconfirmstherelevanceofkeyfeatures,RandomForestimportancesprovideonlyrelativeweightsandlacktheabilityto
explainwhetherafeatureincreasesordecreasesthelikelihoodoffraud.Theyalsodonotaccountforinteractionsbetweenfeaturesor
variationacrossindividualcases.TheselimitationshighlightwhymoreinterpretablemethodssuchasSHAParebettersuitedforhigh-
stakesfrauddetection,wherefine-grainedreasoningandcase-levelexplanationsareessentialforoperationaluse.
4.10.4. Consistencywithpriorliteratureandnovelinsights
TheSHAPanalysisdemonstratesstrongagreementwithpriorresearchinfinancialfrauddetection.Previousstudieshaveidentified
transactionamount,identityconsistency,andbehavioralirregularitiesaskeyindicatorsoffraud.Theprominenceofthesefeaturesin
ouranalysisconfirmsthattheproposedmodelscaptureestablishedfraudpatterns.
Atthesametime,theresultsprovideadditionalinsightsbeyondpriorwork.Inparticular,theanalysishighlightstheimportanceof
anonymizedbehavioralfeatures(V-series),whichencodelatentinteractionpatternsnotdirectlyobservableinrawdata.Thesefeatures
exhibitcontext-dependentcontributions,indicatingthatfrauddetectionisdrivenbyinteractionsratherthanisolatedfeatureeffects.
Thisobservationalignswithrecentworkby(LinandGao,2022),whodemonstratethatSHAP-basedmethodscanrevealcomplex
relationshipsbetweenfinancialfeaturesandimproveinterpretabilityinfrauddetectionmodels.
4.10.5. Practicalimplications
TheenhancedSHAPinterpretationprovidesactionableinsightsforreal-worldfrauddetectionsystems.Financialinstitutionscan
leveragethesefindingstocombinerule-baseddetection(e.g.,abnormaltransactionamountsoridentityinconsistencies)withmachine
learningmodelscapableofcapturingcomplexfeatureinteractions.Furthermore,SHAP-basedexplanationsimprovetransparencyby
providing case-level justifications for predictions. This is critical for regulatory compliance and operational trust in financial
applications.
Fig.8. Randomforest-top20featureimportances.
17

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
5. Discussions
Theresultscarrydirectimplicationsforreal-worldfrauddetectionsystems,wherepredictiveperformancemustbebalancedwith
operationalconsiderations.ModelselectioncannotrelysolelyonROC-AUCorPR-AUCvalues;institutionsmustalsoconsiderinter-
pretability,latency,andthetrade-offbetweenfalsepositivesandfalsenegatives.
Whilethisstudydemonstratestheeffectivenessofadvancedensemblemodelsforfrauddetection,severallimitationsshouldbe
acknowledged. First, the dataset, although large and representative of real-world payment transactions, is anonymized and lacks
certaincontextualfeatures(e.g.,merchantcategorycodes,customerdemographics,andreal-timesessioninformation).Theabsenceof
thesevariablesrestrictstheinterpretabilityoffraudpatternsandmaylimitthegeneralizabilityofthefindingsacrossdifferentfinancial
institutionsandgeographies.
Second, the evaluation was conducted in an offline validation setting. Although metrics such as ROC-AUC and PR-AUC are
informative, they do not capture all operational trade-offs. Real-world deployment involves latency constraints, streaming data
pipelines,andintegrationwithfraudinvestigationteams.Theseaspectswerenotsimulatedinthisstudy,andfutureresearchshould
extendvalidationtoproduction-likeenvironments,includingstresstestingunderhightransactionvolumesandadversarialattack
scenarios.
Third,whileSHAPprovidedvaluableexplainabilityfortree-basedmodels,interpretabilityfordeepneuralnetworksremainsless
developed.MethodssuchasLIMEorintegratedgradientsofferpartialinsights,buttheirstabilityandregulatoryacceptancearestill
evolving.Thiscreateschallengesfordeployingcomplexmodelsinstrictlyregulatedfinancialdomainswheretransparencyisanon-
negotiablerequirement.
AkeylimitationofthisstudyisthattheIEEE-CISdatasetrepresentsafixedhistoricalsnapshotoftransactiondata.Inreal-world
frauddetectionsystems,transactionpatternsandfraudstrategiesevolvecontinuouslyovertime,aphenomenoncommonlyreferredto
asconceptdrift.Thisoccurswhentheunderlyingdatadistributionortherelationshipbetweenfeaturesandthetargetvariablechanges,
oftenduetoadaptivebehaviorbyfraudsters.Asfrauddetectionmodelsaretrainedonhistoricaldata,theirperformancemaydegrade
whendeployedinaliveenvironmentifthestatisticalpropertiesofincomingtransactionsdifferfromthoseobservedduringtraining.
Forexample,fraudstersmayshiftfromlow-valueprobingtransactionstomoresophisticatedattacksinvolvingdevicespoofingor
identityobfuscation,renderingpreviouslylearnedpatternslesseffective.
While the models proposed in this study demonstrate strong performance under a static evaluation setting, maintaining their
effectivenessinpracticewouldrequirecontinuousmonitoringandadaptation.Thismayinvolveperiodicretrainingonrecentdata,
online learning strategies, or drift detection mechanisms that trigger model updates when significant distributional changes are
observed. Furthermore, ensemble approaches such as the proposed XGBoost + DNN model may offer some robustness to moderate drift
duetotheirabilitytocapturecomplementarypatterns.However,theyarenotinherentlyimmunetoconceptdrift,andtheirlong-term
performancedependsontimelyupdatesanddatarefreshcycles.
6. Conclusion
Thisstudyaddressedthepersistentchallengeoffrauddetectioninhighlyimbalancedfinancialtransactiondatabysystematically
comparingtraditional,ensemble-based,anddeeplearningapproaches.Throughrigorousexperimentation,itwasdemonstratedthat
classicalbaselinessuchasLogisticRegressionandRandomForest,whileinterpretable,failtoprovidetheprecisionandrecallbalance
required for real-world applications. Enhanced XGBoost improved performance by leveraging gradient boosting with advanced
handling of imbalance, yet it was the proposed hybrid XGB + DNN Ensemble that delivered the most effective and robust results across
all evaluation metrics. Beyond raw performance scores, the study emphasized the importance of interpretability and operational
readiness.SHAP-basedfeatureattributionhighlightedthecentralroleoftransactionamounts,identity-linkedattributes,andtemporal
patternsindetectingfraudbehavior,underscoringtheneedformulti-dimensionalrepresentationsofcustomeractivity.
The hybrid XGB + DNN Ensemble, embedded within a structured and adaptive framework, represents a powerful and practical
solutionformodernfrauddetection.Byaligningmethodologicalinnovationwithoperationalrealities,thisstudydemonstratesthat
effectivefrauddetectionrequiresnotonlystrongalgorithmsbutalsotransparent,adaptive,andinstitutionallyalignedsystemscapable
ofwithstandingtheevolvingtacticsoffinancialfraud.Together,thesefindingsadvancebothacademicunderstandingandpractical
implementationoffrauddetectionsystems.Nevertheless,limitationsremain.Theanonymizeddatasetconstrainedinterpretabilityof
certainfraudpatterns,andevaluationwasrestrictedtoofflinevalidation.Addressingthesegapsthroughricherfeaturesets,real-time
testing,andadvancedlearningparadigmssuchasgraph-basedorfederatedlearningofferspromisingdirectionsforfutureresearch.
CRediTauthorshipcontributionstatement
Nguyen Duy Anh Luong: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology,
Investigation, Formal analysis, Data curation, Conceptualization. Shengkun Xie: Writing – review & editing, Writing – original draft,
Supervision,Methodology,Fundingacquisition,Formalanalysis,Conceptualization.
Grantinformation
ThisworkisfundedbyNaturalSciencesandEngineeringResearchCouncilofCanadaDiscoveryGrant.
18

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Declarationofcompetinginterest
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonalrelationshipsthatcouldhaveappearedto
influencetheworkreportedinthispaper.
References
Achakzai, M.A.K., Peng, J., 2023. Detecting financial statement fraud using dynamic ensemble machine learning. Int. Rev. Financ. Anal. 89, 102827.
Alamri, M., Ykhlef, M., 2024. Hybrid feature engineering based on customer spending behavior for credit card anomaly and fraud detection. Electronics 13 (20), 3978.
Alfaiz, N.S., Fati, S.M., 2022. Enhanced credit card fraud detection model using machine learning. Electronics 11 (4), 662.
Bahnsen, A.C., Aouada, D., Stojanovic, A., Ottersten, B., 2016. Feature engineering strategies for credit card fraud detection. Expert Syst. Appl. 51, 134–142.
Baisholan, N., Dietz, J.E., Gnatyuk, S., Turdalyuly, M., Matson, E.T., Baisholanova, K., 2025. A systematic review of machine learning in credit card fraud detection
under original class imbalance. Computers 14 (10), 437.
Bhardwaj, K., Kumar, M., Verma, R., Kumar, D., 2024. Machine learning and deep learning for credit card fraud detection: a comparative analysis. In: Proc. 2024 Int.
Conf. Artificial Intelligence and Emerging Technology (Global AI Summit), pp. 131–136.
Bin Sulaiman, R., Schetinin, V., Sant, P., 2022. Review of machine learning approach on credit card fraud detection. Human-Centric Intelligent Systems 2 (1), 55–68.
Bolton, R.J., Hand, D.J., 2002. Statistical fraud detection: a review. Stat. Sci. 17 (3), 235–255.
Breskuviene, D., Dzemyda, G., 2024. Enhancing credit card fraud detection: highly imbalanced data case. J. Big Data 11 (1), 182.
Broby, D., 2021. Financial technology and the future of banking. Financ. Innov. 7 (1), 47.
Carcillo, F., Le Borgne, Y.-A., Caelen, O., Kessaci, Y., Obl�e, F., Bontempi, G., 2021. Combining unsupervised and supervised learning in credit card fraud detection. Inf.
Sci. 557, 317–331.
Chaurasia, S., Kesharwani, S., Sharma, S., Sharma, S., Chugh, B., 2024. Analysis of ensemble machine learning models for fraud detection. In: Proc. 2024 Int. Conf.
Intelligent Systems for Cybersecurity (ISCS), pp. 1–6.
Deotte, C., et al., 2019. IEEE-CIS fraud detection: 1st place solution. Kaggle Competition Write-up. https://www.kaggle.com/competitions/ieee-fraud-detection/
writeups/fraudsquad-1st-place-solution-part-2.
Ding, N., Ruan, X., Wang, H., Liu, Y., 2025. Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. Insur.
Math. Econ. 120, 51–60.
Du, H., Lv, L., Guo, A., Wang, H., 2023. Autoencoder and LightGBM for credit card fraud detection problems. Symmetry 15 (4), 870.
Gandhar, A., Gupta, K., Pandey, A.K., Raj, D., 2024. Fraud detection using machine learning and deep learning. SN Comput. Sci. 5 (5), 453.
George, M.Z.H., Alam, M.K., Hasan, M.T., 2025. Machine learning for fraud detection in digital banking: a systematic literature review. arXiv preprint arXiv:
2510.05167.
H. M, et al., 2019. IEEE-CIS fraud detection: 5th place solution (Lions). Kaggle Competition Write-up. https://www.kaggle.com/competitions/ieee-fraud-detection/
writeups/lions-5th-place-solution-lions.
Ileberi, E., Sun, Y., Wang, Z., 2021. Performance evaluation of machine learning methods for credit card fraud detection using SMOTE and AdaBoost. IEEE Access 9,
165286–165294.
Jahnavi, D., Mona, A., Pulata, S., Sami, S., Vakamullu, B., 2024. Robust hybrid machine learning model for financial fraud detection in credit card transactions. In:
Proc. 2024 2nd Int. Conf. Intelligent Data Communication Technologies and Internet of Things (IDCIoT), pp. 680–686.
Jiao, B., Guo, Y., Gong, D., Chen, Q., 2022. Dynamic ensemble selection for imbalanced data streams with concept drift. IEEE Transact. Neural Networks Learn. Syst.
35 (1), 1278–1291.
Lahbiss, M.M., Chtouki, Y., 2024. Credit card fraud detection in imbalanced datasets: a comparative analysis of machine learning techniques. In: Proc. 2024 Int. Conf.
Computer and Applications (ICCA), pp. 1–6.
Lee, C.-W., Fu, M.-W., Wang, C.-C., Azis, M.I., 2025. Evaluating machine learning algorithms for financial fraud detection: insights from Indonesia. Mathematics 13
(4), 600.
Lei, Y.-T., Ma, C.-Q., Ren, Y.-S., Chen, X.-Q., Narayan, S., Huynh, A.N.Q., 2023. A distributed deep neural network model for credit card fraud detection. Finance Res.
Lett. 58, 104547.
Lin, K., Gao, Y., 2022. Model interpretability of financial fraud detection by group SHAP. Expert Syst. Appl. 202.
Lucas, Y., Portier, P.-E., Laporte, L., Calabretto, S., Caelen, O., He-Guelton, L., Granitzer, M., 2019. Multiple perspectives HMM-based feature engineering for credit
card fraud detection. In: Proc. 34th ACM/SIGAPP Symposium on Applied Computing, pp. 1359–1361.
Ludera, D.T., 2021. Credit card fraud detection by combining synthetic minority oversampling and edited nearest neighbours. In: Future of Information and
Communication Conference, pp. 735–743.
Mehbodniya, A., Alam, I., Pande, S., Neware, R., Rane, K.P., Shabaz, M., Madhavan, M.V., 2021. [Retracted] financial fraud detection in healthcare using machine
learning and deep learning techniques. Secur. Commun. Network. 2021, 9293877.
Mienye, E., Jere, N., Obaido, G., Mienye, I.D., Aruleba, K., 2024. Deep learning in finance: a survey of applications and techniques. A.I. 5 (4), 2066–2091.
Noviandy, T.R., Idroes, G.M., Maulana, A., Hardi, I., Ringga, E.S., Idroes, R., 2023. Credit card fraud detection for contemporary financial management using XGBoost-
driven machine learning and data augmentation techniques. Indatu Journal of Management and Accounting 1 (1), 29–35.
Patel, A., Patel, M., Patel, P., 2024. Exploring supervised machine learning techniques for detecting credit card fraud: an investigative review. In: ITM Web of
Conferences, vol. 65, 03006.
Prasad, M., Srikanth, T., 2024. Multi-Entity real-time Fraud Detection System Using Machine Learning: Improving Fraud Detection Efficiency Using FROST-enhanced
Oversampling.
Riskiyadi, M., 2024. Detecting future financial statement fraud using a machine learning model in Indonesia: a comparative study. Asian Rev. Account. 32 (3),
394–422.
Roseline, J.F., Naidu, G., Pandi, V.S., Rajasree, S.A., Mageswari, N., 2022. Autonomous credit card fraud detection using machine learning approach. Comput. Electr.
Eng. 102, 108132.
Saputra, A., et al., 2019. Fraud detection using machine learning in e-commerce. Int. J. Adv. Comput. Sci. Appl. 10 (9).
Shah, D., Sharma, L.K., 2023. Credit card fraud detection using decision tree and random forest. In: ITM Web of Conferences, vol. 53, 02012.
Sharma, A., Sharma, S., Malik, A., Sobti, R., Suryana, A., 2025. Dynamic feature engineering for adaptive fraud detection. Eng. Proc. 107 (1), 68.
Shimin, L., Ke, X., Xinye, S., et al., 2020. An XGBoost-based system for financial fraud detection. In: E3S Web of Conferences, vol 214, 02042.
Siam, A.M., Bhowmik, P., Uddin, M.P., 2025. Hybrid feature selection framework for enhanced credit card fraud detection using machine learning models. PLoS One
20 (7), e0326975.
Sun, J., 2025. Decision tree-based credit card fraud detection system: design and optimization. Economics & Management Information 1–5.
Taha, A.A., Malebary, S., 2020. An intelligent approach to credit card fraud detection using an optimized light gradient boosting machine. IEEE Access 8,
25579–25587.
Talukder, M.A., Khalid, M., Uddin, M.A., 2024. An integrated multi-stage ensemble machine learning model for fraudulent transaction detection. J. Big Data 11 (1),
168.
Theodorakopoulos, L., Theodoropoulou, A., Tsimakis, A., Halkiopoulos, C., 2025. Big data-driven distributed machine learning for scalable credit card fraud detection
using PySpark, XGBoost, and CatBoost. Electronics 14 (9), 1754.
19

N.D. Anh Luong, S. Xie The Journal of Finance and Data Science 12 (2026) 100195
Velarde, G., Sudhir, A., Deshmane, S., Deshmunkh, A., Sharma, K., Joshi, V., 2023. Evaluating XGBoost for balanced and imbalanced data: application to fraud
detection. arXiv preprint arXiv:2303.15218.
Wajgi, R., Agarkar, H., Patil, R., Rao, H., Petkar, N., 2024. Enhancing credit card transaction fraud detection with random forest and robust scaling. AIP Conf. Proc.
3188, 040013.
Xia, Z., Saha, S.C., 2025. FinGraphFL: financial graph-based federated learning for enhanced credit card fraud detection. Mathematics 13 (9), 1396.
Zhang, Y.-L., Zhou, J., Zheng, W., Feng, J., Li, L., Liu, Z., et al., 2019. Distributed deep forest and its application to automatic detection of cash-out fraud. ACM Trans.
Intell. Syst. Technol. 10 (5), 1–19.
Zioviris, G., Kolomvatsos, K., Stamoulis, G., 2024. An intelligent sequential fraud detection model based on deep learning. J. Supercomput. 80 (10), 14824–14847.
20