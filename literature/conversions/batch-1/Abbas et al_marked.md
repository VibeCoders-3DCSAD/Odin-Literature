---
conversion_metadata:
  converted_at: "2026-07-22T11:43:45Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Abbas et al.pdf"
  source_pdf_sha256: "6ace4e147d64f0381f155f499dfe467218e3cc40cdc65448a6945d8ecd07c15d"
  page_count: 12
  markdown_char_count: 112810
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

SN Computer Science           (2025) 6:674  
https://doi.org/10.1007/s42979-025-04214-8

ORIGINAL RESEARCH

Machine Learning‑Based Analysis of Technology Acceptance 
in FinTech: A Behavioral Study Using Digital Wallet Data

Sayyed Khawar Abbas1

· Muzzammil Hussain2 · Yagya Nath Rimal3

Received: 17 June 2025 / Accepted: 11 July 2025 
© The Author(s) 2025

Abstract
The rapid growth of FinTech services, particularly robo-advisors, has transformed how individuals engage with digital 
financial platforms. Understanding the behavioral drivers of technology acceptance in this context is critical for enhancing 
adoption and designing more effective user experiences. This study investigates whether user-level behavioral and trans-
actional data can be leveraged to predict technology acceptance, operationalized through daily app usage. Grounded in the 
Technology Acceptance Model (TAM) and Unified Theory of Acceptance and Use of Technology (UTAUT), the study 
uses behavioral proxies such as customer satisfaction, loyalty points, and lifetime value to reflect constructs like perceived 
usefulness, performance expectancy, and facilitating conditions. Using a real-world dataset of 7000 FinTech users sourced 
from Kaggle, we applied four machine learning algorithms, Logistic Regression, Support Vector Machine, Random Forest, 
and XGBoost, to classify users into high and low acceptance categories. Results revealed that ensemble models, particularly 
XGBoost, outperformed linear classifiers, achieving moderate improvements in precision and recall for the high-acceptance 
class. However, overall predictive performance remained constrained by class imbalance and overlapping behavioral patterns. 
These findings suggest that while machine learning can reveal patterns linked to technology acceptance, predictive preci-
sion remains limited without richer temporal and psychographic features. The study contributes to the evolving discourse 
on FinTech adoption by offering a data-driven lens to complement intention-based models and inform adaptive engagement 
strategies.

Keywords  FinTech · Robo-advisors · Technology acceptance · Machine learning · Behavioral prediction · User 
engagement · XGBoost · Random forest · Digital financial services · Imbalanced classification

*  Sayyed Khawar Abbas

sayyedkhawar.abbas@uni-corvinus.hu; 
Sayyedkhawarabbas@gmail.com

Muzzammil Hussain 
  Muzzammil.hussain@kfupm.edu.sa

Yagya Nath Rimal

Rimal.yagya@gmail.com

1

Institute of Data Analytics and Information Systems, 
Department of Information Systems, Corvinus University 
of Budapest, 8 Fovam Ter, Budapest 1093, Hungary

2

Interdisciplinary Research Center for Finance and Digital 
Economy, KBS, KFUPM, Dhahran, Saudi Arabia
3  Faculty of Science and Technology, Pokhara University,

Pokhara, Nepal

Introduction

The advancement of financial technology (FinTech) has sig-
nificantly reshaped the global financial landscape by enhanc-
ing the accessibility, efficiency, and personalization of finan-
cial services. A notable innovation within this domain is 
the rise of robo-advisors, automated digital platforms that 
use algorithms and artificial intelligence to provide invest-
ment advice and portfolio management with minimal human 
supervision [1]. These systems have gained increasing atten-
tion for their potential to democratize financial planning and 
deliver scalable, cost-effective solutions to a broad base of 
users.

Despite  their  rapid  proliferation,  the  acceptance  of 
robo-advisors among users remains inconsistent [2], often 
influenced  by  complex  behavioral,  economic,  and  tech-
nological factors. Understanding what drives or hinders 
user  acceptance  is  critical  for  both  FinTech  developers

---

<!-- PAGE 2 -->

674

Page 2 of 12

SN Computer Science           (2025) 6:674

and policymakers, particularly as digital financial services 
continue to expand into diverse markets and demographic 
segments. Traditional approaches to measuring technol-
ogy acceptance have relied primarily on models such as 
the Technology Acceptance Model (TAM) or the Unified 
Theory of Acceptance and Use of Technology (UTAUT), 
typically evaluated through structured surveys [3]. However, 
these models may not fully capture real-time behavioral data 
and actual engagement patterns that are now increasingly 
available through digital platforms [4].

This study addresses this limitation by leveraging a real-
world dataset from Kaggle, which includes detailed behavio-
ral and transactional data from 7000 users of a digital wallet 
platform. To operationalize technology acceptance in this 
context, daily app usage is used as a behavioral proxy for 
high technology adoption [5]. The study then applies a com-
parative machine learning framework using Logistic Regres-
sion, Support Vector Machine (SVM), Random Forest, and 
XGBoost to classify users based on their likelihood of high 
technology acceptance [6].

The primary aim of this research is twofold:

1)  To evaluate the predictive capacity of multiple machine 
learning algorithms in modeling technology acceptance 
based on digital behavioral data; and

2)  To identify the most influential features, such as cus-
tomer satisfaction, loyalty points, and lifetime value 
(LTV), that correlate with increased engagement and 
adoption.

The contributions of this study are as follows:

•  It  provides  a  data-driven  perspective  on  technology 
acceptance using real transactional and engagement data 
rather than theoretical survey constructs.

•  It presents a comparative performance analysis of widely 
used machine learning models in the context of imbal-
anced classification tasks.

•  It highlights key behavioral and transactional predictors 
of FinTech technology acceptance, with implications for 
targeted design, personalization, and customer retention 
strategies.

Despite  valuable  insights  from  TAM,  UTAUT,  and 
related  models,  most  existing  studies  rely  on  structured 
surveys and intention-based indicators. These approaches, 
while theoretically robust, may not fully reflect real-world 
engagement, often suffering from self-reporting bias and 
lack of contextual nuance. This creates a critical research 
gap: limited empirical evidence exists on how actual behav-
ioral data, particularly transactional, usage, and support 
interactions, map onto technology acceptance in FinTech. 
Our study addresses this gap by leveraging a large-scale,

real-world dataset and applying machine learning models 
to detect behavioral signals of adoption. By framing daily 
app usage as a proxy for sustained technology acceptance 
and linking behavioral variables to theoretical constructs, the 
study contributes both methodologically and theoretically to 
the FinTech adoption literature. It offers a novel perspective 
that complements traditional perceptual frameworks with 
predictive insights rooted in real user behavior.

This article is structured as follows. Sect. "Literature 
Review" presents a review of the relevant literature on Fin-
Tech adoption and machine learning applications in behav-
ioral prediction. Sect. "Methodology" describes the dataset, 
preprocessing steps, and machine learning methodologies 
employed. Sect. "Results" discusses the results of the model 
evaluation and feature importance analysis. Sect. "Discus-
sion" interprets these findings and explores their implica-
tions, while Sect. "Conclusion" concludes the paper with a 
summary and directions for future research.

Literature Review

The  accelerating  digitalization  of  financial  services  has 
reshaped the dynamics of consumer interaction with tech-
nology, giving rise to the widespread deployment of robo-
advisors and other AI-enabled financial tools. Understanding 
how users engage with such systems has become a crucial 
research focus, intersecting domains such as technology 
acceptance, behavioral finance, and machine learning. This 
section provides an overview of key theoretical frameworks, 
empirical findings on FinTech adoption, and recent method-
ological advances leveraging machine learning in behavioral 
prediction tasks.

Theoretical Models of Technology Acceptance

The literature on user acceptance of technology is deeply 
rooted in psychological and behavioral theories. The Tech-
nology Acceptance Model (TAM) introduced by Davis [7], 
remains one of the most widely cited frameworks, positing 
that perceived usefulness and perceived ease of use directly 
influence an individual’s behavioral intention to use a tech-
nology. Subsequent models, such as TAM2, TAM3, and 
the Unified Theory of Acceptance and Use of Technology 
(UTAUT) [8], have extended this foundation by incorporat-
ing variables such as social influence, facilitating conditions, 
hedonic motivation, and price value.

In financial services, these models have been adapted to 
assess acceptance of internet banking, mobile payment apps, 
and recently, robo-advisors [9]. However, such models often 
rely on cross-sectional survey data, which may be suscepti-
ble to self-reporting biases and may not adequately capture 
actual user behavior over time.

---

<!-- PAGE 3 -->

SN Computer Science           (2025) 6:674

Page 3 of 12

674

FinTech and Robo‑Advisor Adoption

Recent studies have explored the factors influencing the 
adoption of robo-advisors, highlighting constructs such as 
trust, transparency, algorithm aversion, and financial literacy 
[10]. Zhang, et al. [2] found that perceived competence and 
benevolence of the algorithm significantly impact users’ 
willingness to adopt robo-advisory services. Similarly, Aw, 
et al. [11] emphasized the moderating role of digital finan-
cial literacy in shaping robo-advisor usage.

Despite the growing body of work, there is a scarcity 
of research using behavioral datasets to infer adoption pat-
terns [12]. Most existing studies depend on hypothetical 
scenarios or intention-based measurements, limiting their 
external validity. Moreover, limited effort has been made to 
operationalize technology acceptance through actual usage 
metrics, such as frequency of app interaction, transactional 
depth, and engagement behavior, which are more reflective 
of real-world acceptance [13].

Machine Learning in FinTech and Behavioral 
Modeling

Machine learning (ML) offers a powerful set of tools for 
modeling behavioral outcomes in complex, high-dimen-
sional environments, making it particularly suitable for Fin-
Tech applications. Prior research has successfully employed 
ML techniques for credit scoring, fraud detection, and churn 
prediction [14]. In the domain of customer behavior mod-
eling, classifiers such as Random Forest, Support Vector 
Machines (SVM), and Gradient Boosting (XGBoost) have 
been applied to detect risk profiles, segment users, and opti-
mize marketing strategies [15].

However, the application of ML in the context of technol-
ogy acceptance, particularly in the FinTech domain, remains 
limited. While ML has been used in recommender systems 
and digital personalization [16], few studies have attempted 
to use it to predict technology adoption based on rich behav-
ioral datasets. Moreover, the challenge of class imbalance in 
such predictive tasks, where the number of high-engagement 
or early-adopter users is often relatively low, has been insuf-
ficiently addressed in most empirical studies [17].

Research Gap and Contribution

Drawing from the aforementioned literature, a clear gap 
emerges in the empirical study of real behavioral signals of 
technology acceptance in FinTech [16, 18]. While theoreti-
cal models provide foundational insights, and survey-based 
studies offer perceptual understandings, the predictive mod-
eling of technology adoption using machine learning and 
real-world behavioral data remains underexplored.

This study aims to fill this gap by:

•  Using a publicly available FinTech behavioral dataset that 
captures a wide range of transactional and engagement 
variables.

•  Operationalizing technology acceptance through daily

app usage, a tangible behavioral proxy.

•  Applying and comparing the performance of Logistic 
Regression,  SVM,  Random  Forest,  and  XGBoost  to 
model this binary classification task.

•  Evaluating feature importance and model interpretability

to provide actionable insights for practitioners.

By doing so, this research bridges the theoretical and 
data-driven approaches, offering a novel methodological 
contribution to the field of FinTech adoption and presenting 
practical implications for robo-advisor design, targeting, and 
personalization strategies.

Methodology

This study adopts a structured, data-driven methodology to 
examine the behavioral dimensions of technology accept-
ance in FinTech, using machine learning techniques applied 
to real-world customer engagement data from south Asia. 
The analysis is based on the Digital Wallet LTV Dataset,1 
a publicly available dataset sourced from Kaggle, which 
comprises 7,000 user-level records and 20 features. These 
include demographic attributes (such as age, location, and 
income level), transactional indicators (including total trans-
actions, average and maximum transaction value), behav-
ioral metrics (such as app usage frequency, loyalty points, 
referral count), and outcome variables such as Customer Sat-
isfaction Score and Customer Lifetime Value (LTV). The 
breadth and granularity of the dataset make it well-suited 
for modeling technology adoption behavior within a digital 
financial context.

We  operationalized  technology  acceptance  using  the 
App_Usage_Frequency feature, categorizing daily users as 
'high acceptance' and weekly/monthly users as 'low accept-
ance.' While binary classification simplifies complex behav-
ior, daily usage offers a concrete behavioral proxy reflecting 
sustained engagement. We acknowledge that this operation-
alization does not capture cognitive or affective components 
of  technology  acceptance  (e.g.,  perceived  usefulness  or 
trust), and suggest future work explore multi-level or con-
tinuous measures of engagement.

The data preprocessing phase involved multiple steps 
to ensure model readiness and integrity. First, all records 
were  verified  to  be  free  of  missing  values.  Categorical

1  https:// www. kaggle. com/ datas ets/ harun rai/ finte ch- custo mer- life-  
time- value- ltv- datas et

---

<!-- PAGE 4 -->

674

Page 4 of 12

SN Computer Science           (2025) 6:674

variables such as location, income level, and preferred pay-
ment method were transformed into numeric form using 
label encoding. Redundant identifiers such as customer ID 
were removed, and all numerical variables were standard-
ized using z-score normalization to mitigate scale-related 
biases during training. The final feature matrix included 18 
independent variables. Class imbalance was identified in the 
target variable, with approximately 33.5% of users labeled 
as high acceptance. Although no oversampling or under-
sampling techniques were applied at this stage, performance 
metrics were selected to account for imbalance effects during 
evaluation. To address the class imbalance (approximately 
33.5% high-acceptance users), we applied for the Synthetic 
Minority Oversampling Technique (SMOTE) during train-
ing.  SMOTE  generates  synthetic  samples  of  the  minor-
ity class, enabling the models to better learn the decision 
boundaries. Models were retrained using SMOTE-applied 
training sets, and performance was re-evaluated. As detailed 
in Sect. "Results", this led to measurable improvements in 
F1-score and recall for the minority class, particularly in 
ensemble models.

Four  machine  learning  algorithms  were  employed  to 
model the classification task: Logistic Regression, Support 
Vector Machine (SVM), Random Forest, and Extreme Gra-
dient Boosting (XGBoost) [19]. Logistic Regression served 
as a baseline model due to its interpretability and wide-
spread use in binary classification. SVM was included for 
its robustness in high-dimensional spaces and capacity for 
non-linear separation. Random Forest and XGBoost, both 
tree-based ensemble methods, were chosen for their abil-
ity to model complex feature interactions, handle heteroge-
neous data types, and provide built-in measures of feature 
importance. All models were implemented in Python using 
the scikit-learn and xgboost libraries. The dataset was par-
titioned using an 80/20 train-test split, with stratified sam-
pling employed to maintain class proportions across both 
sets. Hyperparameters were optimized through grid search 
and cross-validation to enhance generalizability.

Model  performance  was  evaluated  using  a  compre-
hensive set of metrics. These included accuracy to gauge 
overall predictive success; precision, recall, and F1-score 
to provide class-specific insights; and the area under the 
Receiver Operating Characteristic (ROC AUC) to assess the 
discriminative power of the classifiers. Confusion matrices 
were used to analyze error types, while probabilistic out-
puts were assessed using Mean Absolute Error (MAE) and 
Root Mean Square Error (RMSE) as secondary evaluation 
measures. These metrics collectively provided a nuanced 
understanding of model strengths and limitations, especially 
in the presence of class imbalance.

To  enhance  the  interpretability  of  results,  especially 
given the increasing emphasis on explainable artificial intel-
ligence (XAI) in FinTech applications, feature importance

Table 1   Machine learning model performance metrics

Model

Accuracy ROC 
AUC

Precision
(high)

Recall 
(high)

F1-score
(high)

Logistic
Regres-
sion
SVM
Random
Forest
XGBoost

0.665

0.514

0.00

0.00

0.00

0.665
0.665

0.507
0.496

0.00
0.50

0.615

0.519

0.34

0.00
0.03

0.16

0.00
0.06

0.22

was analyzed using both model-specific and model-agnostic 
methods. The Random Forest and XGBoost models gener-
ated intrinsic importance scores for each variable, indicat-
ing their relative contribution to predictive performance. In 
addition, SHapley Additive exPlanations (SHAP) values 
were computed to offer both local and global interpretability, 
revealing how specific features influenced individual predic-
tions and overall model behavior. This was complemented 
by rich visual diagnostics, including 3D scatter plots to 
capture multivariate interactions, dimensionality reduction 
techniques such as t-SNE and Principal Component Analy-
sis (PCA) for visualizing data clusters, and ROC/precision-
recall curves to assess threshold sensitivity.

All experiments were conducted in a Jupyter Notebook 
environment using Python 3.11. The computational pipe-
line  was  built  with  standard  libraries  including  pandas, 
numpy, matplotlib, seaborn, shap, and plotly. The full code 
and supporting visualizations are available upon request to 
promote transparency and reproducibility. Ethical considera-
tions were observed throughout the study, with the dataset 
fully anonymized and publicly accessible, thereby ensuring 
compliance with data protection norms. This methodological 
approach not only supports the robust modeling of behav-
ioral technology acceptance but also provides a replicable 
framework for future FinTech research focused on real-world 
engagement signals.

Results

The objective of this study was to assess the effectiveness of 
various machine learning models in predicting high levels 
of technology acceptance—measured via daily app usage—
among FinTech users. This section presents the compara-
tive performance of four classification algorithms: Logistic 
Regression, Support Vector Machine (SVM), Random For-
est, and XGBoost. The models were evaluated on several key 
metrics including overall accuracy, ROC AUC score, and 
class-specific precision, recall, and F1-score, with a particu-
lar emphasis on their ability to detect users exhibiting high 
technology acceptance behavior.

---

<!-- PAGE 5 -->

SN Computer Science           (2025) 6:674

Page 5 of 12

674

A  summary  of  model  performance  is  presented  in 
Table 1. While all four classifiers achieved similar accuracy 
levels, approximately 66.5%, the ROC AUC scores, which 
offer a more nuanced view in the presence of class imbal-
ance, were modest across all models. XGBoost demonstrated 
the highest ROC AUC at 0.519, followed closely by Logis-
tic Regression at 0.514. SVM and Random Forest lagged 
slightly behind, indicating limited capability of all models 
in separating high and low technology acceptance classes 
based on the available features.

Although accuracy remained consistent across models, 
the deeper class-level analysis reveals a stark contrast in how 
well each classifier handled the minority class, users with 
high technology acceptance. Logistic Regression and SVM, 
both linear models, completely failed to identify this group, 
yielding zero precision, recall, and F1-score, consistency can 
be found [20]. This suggests an inherent limitation in their 
ability to model the complex, nonlinear relationships likely 
present in the behavioral features.

In contrast, the ensemble models, Random Forest and 
XGBoost, offered significantly better insight into this minor-
ity class. Random Forest achieved a high precision of 0.50, 
indicating that when it predicted a user as a high-accept-
ance case [21], it was often correct. However, its recall of 
just 0.03 signals an extremely high false-negative rate [22], 
meaning it failed to identify the vast majority of actual daily 
users. XGBoost, on the other hand, demonstrated a more 
balanced performance with precision at 0.34 and recall at 
0.16, producing the highest F1-score of 0.22 among all mod-
els for this class. While this still reflects a limited ability 
to detect high-tech-acceptance users, it marks a significant 
improvement over linear method.

After  applying  SMOTE  to  the  training  data,  model 
performance on the minority class improved. XGBoost’s 
F1-score increased from 0.22 to 0.36, and Random Forest’s 
F1-score improved to 0.28. Recall for XGBoost rose from 
0.16 to 0.27, showing a more balanced identification of high-
acceptance users.

These results are visually summarized in Fig. 1, which 
compares the accuracy and ROC AUC of all models. The 
graph illustrates that despite similar surface-level perfor-
mance (accuracy), the underlying discriminatory power, rep-
resented by ROC AUC, is weak, hovering close to 0.5, which 
reflects near-random classification. The comparatively better 
performance of XGBoost points to its capability in handling 
feature interaction and minor class signals more effectively 
than its counterparts.

To further evaluate classifier performance, especially 
given the class imbalance in the dataset, we examined both 
the Precision–Recall (PR) curves and the Receiver Operat-
ing Characteristic (ROC) curves for each model, as shown 
in  Fig.  1.  The  left  panel  of  the  figure  illustrates  the  PR 
curves, which are particularly informative for imbalanced 
classification tasks as they emphasize the models' ability to 
identify positive class instances (i.e., users with high tech-
nology acceptance). While all models exhibited relatively 
low precision across most recall thresholds, the Random 
Forest (AP = 0.345) and XGBoost (AP = 0.343) classifiers 
demonstrated marginally superior performance compared 
to Logistic Regression and SVM, whose average precision 
scores were 0.338 and 0.333, respectively.

The right panel of Fig. 2 presents the ROC curves for all 
models. In this visualization, XGBoost attained the highest 
area under the curve (AUC = 0.519), followed closely by

Fig. 1   Precision–Recall  (left)  and  ROC  Curves  (right)  for  four  clas-
sification  models  (Logistic  Regression,  SVM,  Random  Forest,  and 
XGBoost). Average Precision (AP) and AUC values are shown in the

legends. Curves indicate limited model discrimination, with ensemble 
models  slightly  outperforming  linear  classifiers  in  identifying  high 
technology acceptance users

---

<!-- PAGE 6 -->

674

Page 6 of 12

SN Computer Science           (2025) 6:674

Fig. 2   PCA results showing: (left) 3D projection of users colored by tech acceptance, (center) explained variance by components, and (right) key 
feature loadings across PC1–PC3. LTV, Total Spent, and Satisfaction Score show strong influence on PC1

Logistic Regression (AUC = 0.514), while Random Forest 
(AUC = 0.496) and SVM (AUC = 0.507) remained close 
to the diagonal line representing random guessing. These 
results reinforce the earlier finding that although the models 
offer some degree of predictive capability, their overall abil-
ity to differentiate between high and low engagement users 
remains limited. Notably, the ROC curves suggest very mod-
est true positive rate improvements over chance, emphasiz-
ing the challenge of modeling real-world FinTech behavior 
through static transactional features alone.

To explore latent structure in the data and assess whether 
linear combinations of features could reveal distinguishable 
clusters of technology acceptance, a Principal Component 
Analysis (PCA) was conducted. Figure 2 presents a three-
panel summary of the PCA results. The left panel shows 
a 3D projection of the data using the first three principal 
components, with points colored by technology acceptance 
status (red for high acceptance, blue for low). Although no 
clear separation is observed, subtle patterns in spatial dis-
tribution suggest that certain combinations of variables may 
partially differentiate user classes.

The middle panel displays the variance explained by each 
principal component. The first component (PC1) accounts 
for approximately 21.4% of the total variance, followed by 
PC2 (8.2%) and PC3 (5.97%), indicating that the first three 
components together capture about 35.6% of the total infor-
mation. While this level of variance is moderate, it does 
provide a reduced yet informative basis for visual explora-
tion and downstream modeling.

The rightmost panel presents the feature loadings for 
each of the three components. Variables such as Customer 
Lifetime Value (LTV), Total Spent, Customer Satisfaction 
Score, and Average Transaction Value contributed strongly 
to PC1[23], confirming their relevance in capturing behav-
ioral intensity. PC2 was more influenced by features like

Total Transactions and Issue Resolution Time [24], while 
PC3 showed moderate contributions from Support Tickets 
Raised and Loyalty Points Earned [25]. These insights rein-
force the notion that while a few behavioral features carry 
strong signals, the variance is distributed across multiple 
dimensions, and no single component dominates the repre-
sentation space.

To further interpret model performance and understand 
feature contributions to predictions, we conducted several 
advanced machine learning analyses, presented in Fig. 3. 
The upper left panel shows the validation curve for the Ran-
dom Forest model with varying numbers of estimators [26]. 
As expected, training accuracy remains near perfect across 
all values, while validation accuracy plateaus at around 
66.5%, suggesting the model is not overfitting but also lim-
ited in learnable signal from the data.

The upper right panel compares the feature importance 
scores of Random Forest and XGBoost models. Features 
such as LTV, Customer Satisfaction Score, and Issue Resolu-
tion Time consistently ranked highest in both models [27], 
reinforcing earlier findings about the influence of financial 
value and service experience on daily usage behavior. Other 
important features include Support Tickets Raised, Pre-
ferred Payment Method, and Referral Count [28], pointing 
to behavioral and interaction-based drivers of engagement.
The lower left panel presents the distribution of predicted 
probabilities from the Random Forest model [26]. Predic-
tions for both high and low tech acceptance classes cluster 
near the middle, indicating that the model often expresses 
uncertainty. The significant overlap between classes suggests 
that the available features only weakly separate user groups, 
which aligns with the modest precision-recall performance 
seen earlier.

Finally, the bottom right panel shows the calibration 
curves for both Random Forest and XGBoost models [29].

---

<!-- PAGE 7 -->

SN Computer Science           (2025) 6:674

Page 7 of 12

674

Fig. 3   Model diagnostics: (top left) Random Forest validation curve, (top right) feature importance comparison, (bottom left) predicted probabil-
ity distribution, and (bottom right) calibration curves for Random Forest and XGBoost

A perfectly calibrated model would align with the diago-
nal reference line. Here, both models deviate from ideal 
calibration, particularly in mid-probability ranges, imply-
ing that predicted probabilities may not reliably reflect 
true class membership likelihood. Nonetheless, calibration 
remains within a tolerable range for exploratory decision-
support purposes.

From an interpretive standpoint, these findings partially 
support the research hypothesis. Machine learning mod-
els, particularly ensemble methods, can identify signals of 
high technology acceptance using behavioral and transac-
tional data. However, the overall results suggest that the 
differentiation between high and low adoption users is 
nuanced and potentially entangled in subtle behavioral 
patterns not fully captured by the available features. The 
weak recall scores highlight that many daily users exhibit

similar surface behavior to weekly or monthly users, com-
plicating prediction.

Furthermore, the limited success of even advanced classi-
fiers suggests that class imbalance, feature overlap, and lack 
of temporal behavioral features pose significant challenges 
[30]. The outcome indicates a need for incorporating richer 
behavioral dynamics, such as session timing, transaction 
sequences, or real-time feedback, to improve model robust-
ness. Additionally, deploying resampling methods (e.g., 
SMOTE), cost-sensitive learning, or hybrid approaches com-
bining rules with statistical learning could further strengthen 
predictive power in future work.

In summary, while Random Forest and XGBoost show 
some promise in identifying FinTech users likely to adopt 
robo-advisory platforms based on engagement behavior, 
the difficulty in reliably distinguishing these users from

---

<!-- PAGE 8 -->

674

Page 8 of 12

SN Computer Science           (2025) 6:674

less engaged ones points to the complexity of behavioral 
acceptance as a predictive task. The subsequent section will 
explore which specific features drove the models' predic-
tions and how they can inform FinTech product design and 
personalization strategies.

Discussion

The findings of this study offer important insights into the 
viability and limitations of using behavioral and transac-
tional  data  to  model  technology  acceptance  in  FinTech 
platforms,  particularly  in  the  context  of  robo-advisory 
adoption. While the research was guided by the hypothesis 
that machine learning techniques could effectively differ-
entiate high-engagement users (i.e., daily app users) from 
less engaged ones, the results reveal a more nuanced reality. 
Although ensemble methods such as Random Forest and 
XGBoost performed relatively better than linear models, 
their discriminatory power, particularly in identifying users 
with high technology acceptance, remained limited.

Our findings regarding behavioral predictors such as Cus-
tomer Satisfaction Score, Lifetime Value (LTV), and Loy-
alty Points Earned align with several perceptual constructs 
highlighted in the literature. For instance, Zhang et al. [31] 
emphasized the role of algorithmic competence and benevo-
lence in shaping trust, while Chen et al. [32] linked trust 
and loyalty to the continued use of robo-advisory services 
[33, 34]. In our case, satisfaction and LTV likely serve as 
behavioral proxies for perceived usefulness and performance 
expectancy, constructs central to TAM and UTAUT. Loy-
alty points and referral behaviors may correspond to hedonic 
motivation and social influence, respectively. This empirical 
support suggests that behavioral signals can serve as indirect 
validations of established psychological constructs, though 
the correspondence is not always one-to-one.

Notably, several key behavioral features such as Cus-
tomer Satisfaction Score, Lifetime Value, and Loyalty Points 
Earned map closely to constructs from TAM and UTAUT 
models. For instance, satisfaction and LTV align with 'per-
ceived usefulness' and 'performance expectancy,' while sup-
port resolution may relate to 'facilitating conditions.' This 
theoretical alignment reinforces the behavioral validity of 
our feature selection and supports deeper integration of data-
driven models with psychological theories of technology 
acceptance.

However, the divergence between our machine learn-
ing models’ modest recall rates and the strong associations 
found in perception-based studies invites critical reflection. 
One plausible explanation is that ML models, particularly 
those based on static transactional features, lack the con-
textual richness of perceptual constructs such as trust, per-
ceived risk, or financial anxiety. While users may report

high trust in robo-advisors in surveys, their behavioral data 
may not reflect this sentiment due to external constraints or 
situational factors (e.g., financial goals, income variability). 
This disconnect underlines the limits of behavioral proxies 
and suggests that psychographic and contextual variables 
are indispensable for capturing the full adoption spectrum.
One of the most critical observations is that Logistic 
Regression and Support Vector Machines failed entirely to 
classify high-acceptance users, highlighting the insufficiency 
of linear decision boundaries in capturing complex behavio-
ral dynamics. This aligns with prior research indicating that 
financial behaviors, such as digital adoption and investment 
decisions, often exhibit nonlinear interactions influenced by 
multi-layered socio-demographic, psychological, and behav-
ioral factors [35, 36]. The modest performance of Random 
Forest and XGBoost, where precision and recall improved 
but remained well below acceptable thresholds, suggests that 
while richer models can begin to decode patterns of engage-
ment, the overlap in behavioral signals between high and low 
adoption groups presents a persistent challenge.

These results partially confirm the central hypothesis of 
this study, that machine learning can uncover probabilistic 
signals of technology acceptance, but the prediction task is 
inherently difficult due to the class imbalance, limited proxy 
variables, and lack of temporal context. For example, while 
features like Customer Satisfaction Score, LTV, and Loyalty 
Points Earned were found to be influential, their distributions 
often overlapped significantly across both classes, undermin-
ing classification certainty. Moreover, the binary operation-
alization of technology acceptance, although grounded in 
behavioral frequency, likely fails to capture the full spectrum 
of user attitudes, intentions, and constraints that influence 
digital platform engagement.

The findings further highlight the need for advanced fea-
ture engineering and modeling strategies. Given the limited 
recall achieved by all models for the high acceptance class, 
future research should consider incorporating time-series 
features (e.g., user activity over time), contextual metadata 
(e.g., promotional campaigns or app interface changes), or 
external behavioral drivers (e.g., economic conditions or 
peer influence). Additionally, addressing class imbalance 
through oversampling techniques such as SMOTE, or by 
applying cost-sensitive learning, may enable models to place 
greater emphasis on minority class predictions.

From a practical standpoint, the study’s insights are rel-
evant for FinTech product managers and developers. The 
finding  that  satisfaction  and  loyalty-related  metrics  are 
among the most influential predictors suggests that improv-
ing resolution times, reward systems, and user experience 
design could be effective levers to increase daily usage and 
long-term adoption of robo-advisory services. Furthermore, 
the difficulty encountered by even advanced models in clas-
sifying high-adoption users reinforces the importance of

---

<!-- PAGE 9 -->

SN Computer Science           (2025) 6:674

Page 9 of 12

674

multi-modal personalization strategies, which go beyond 
transactional patterns to include psychographic profiling, 
dynamic behavioral cues, and interactive feedback loops.

In  comparison  with  previous  literature,  this  study 
advances the field by employing a behaviorally-grounded 
and data-driven approach to technology acceptance, con-
trasting with most earlier works that rely heavily on percep-
tual survey data and structural equation modeling [37, 38]. 
By focusing on actual user engagement metrics, this research 
contributes a fresh methodological perspective that comple-
ments existing theoretical models like TAM and UTAUT 
with empirical predictive insights.

Despite these contributions, the study is not without limi-
tations. The use of a single dataset limits generalizability, 
and the absence of temporal and psychological variables 
constrains the depth of behavioral modeling. Additionally, 
while machine learning offers powerful tools for classifica-
tion, it does not inherently address causality, and interpret-
ability remains a challenge, particularly in black-box models 
like XGBoost.

The  observed  discrepancy,  where  features  like  LTV 
and satisfaction show high importance, yet models exhibit 
low  recall,  mirrors  theoretical  expectations  from  TAM 
and UTAUT. These models posit that while performance 
expectancy and facilitating conditions are important, actual 
adoption is mediated by intention and moderated by per-
sonal and environmental variables. Our findings suggest 
that while behavioral indicators provide partial signals, they 
are insufficient without accounting for the user’s internal

decision-making process or surrounding ecosystem. There-
fore, weak recall may not indicate model failure, but rather 
the complexity of behavioral manifestation that lacks visible 
differentiation in transactional data. To further clarify how 
our dataset operationalizes theoretical constructs from TAM 
and UTAUT, Table 2 provides a comparative summary of 
key constructs, their proxy variables, empirical results, and 
corresponding interpretations.

In conclusion, this study underscores the potential of 
machine learning in enhancing our understanding of Fin-
Tech user behavior, but also reveals critical areas for meth-
odological refinement. The ability to predict technology 
acceptance behaviorally is possible, but only to a limited 
extent, when relying solely on transactional and static user 
data. To move toward more reliable and actionable models, 
future research should integrate longitudinal behavioral data, 
hybrid modeling techniques, and cross-disciplinary insights 
from behavioral economics, human–computer interaction, 
and digital psychology.

This study contributes to theoretical discourse by offering 
an empirical, data-driven lens through which to examine and 
potentially refine constructs from TAM and UTAUT. While 
these models traditionally rely on perceptual or intention-
based inputs, our ML-based behavioral approach reveals 
the extent to which such constructs manifest in real-world 
engagement patterns. The moderate alignment of satisfaction 
and LTV with perceived usefulness and facilitating condi-
tions demonstrates the potential of behavioral modeling to 
supplement traditional frameworks. Moreover, the study

Table 2   Comparative table: theoretical constructs, data representation, and empirical insights

Construct (from
TAM/UTAUT)

Repre-
sented in 
dataset

Proxy variable used

Empirical finding

Interpretation and implication

Perceived usefulness

Yes

Customer satisfaction score

High feature importance

Aligns with TAM; satisfaction reflects 
system value contributing to frequent 
usage

Performance expectancy Yes

Lifetime value (LTV)

High feature importance

Suggests users adopt when longterm

Facilitating conditions

Partially

Hedonic motivation

Partially

Issue resolution
time, support tickets
Loyalty points, referral count

financial benefit is evident

Moderate importance

Indicates support access influences adop-
tion, but not strongly predictive alone
Moderate to low importance These engagement incentives influence 
behavior but do not fully differentiate 
high-use users

Social influence

No

Not available

Not tested

Trust and
competence
Digital literacy

Behavioral intention

Indirect

Satisfaction score (proxy), LTV Suggested through impor-

tance of satisfaction

No

No

Not available

Not tested

Not available

Not applicable

Missing from dataset; future studies 
should include peer or community 
influence variables

Implied link between good experience 
and trust, but not directly measured
Important perceptual driver in literature;

absence limits generalizability
Study focused on actual behavior,

not intention. Supports shift toward 
behavior-centric models

---

<!-- PAGE 10 -->

674

Page 10 of 12

SN Computer Science           (2025) 6:674

underscores the importance of transitioning from intention-
centric models to outcome-oriented behavioral analysis, 
especially  as  granular  usage  data  becomes  increasingly 
available in FinTech platforms.

Conclusion

This study set out to explore whether machine learning algo-
rithms can effectively predict behavioral technology accept-
ance among FinTech users, using real-world transactional 
and engagement data. By framing daily app usage as a proxy 
for high technology acceptance, and applying four differ-
ent classifiers—Logistic Regression, SVM, Random Forest, 
and XGBoost—the research aimed to uncover the predictive 
power of user behavior patterns in the adoption of robo-
advisory platforms. The results offer partial validation of this 
objective. While ensemble methods like Random Forest and 
XGBoost demonstrated better discriminatory performance 
compared to linear models, their overall ability to detect 
high-tech-acceptance users was limited, as evidenced by low 
recall and modest AUC scores. These findings reveal that 
while behavioral features contain signals of engagement, 
the distinction between high and low adopters is subtle and 
non-trivial to model.

While the inclusion of SMOTE improved classification of 
high-engagement users, challenges remain. This reinforces 
that behavioral data alone may not be sufficient for robust 
prediction without temporal depth or psychographic inputs. 
Our findings are promising but exploratory, and further vali-
dation is necessary before real-world deployment.

The study provides several important practical implica-
tions for FinTech companies and digital product managers. 
Firstly, features related to customer satisfaction, loyalty pro-
grams, and spending patterns emerged as significant predic-
tors, underscoring the value of customer experience design 
in promoting sustained app engagement. Companies aiming 
to increase robo-advisor adoption should consider investing 
in features that personalize user journeys, reward engage-
ment, and resolve issues efficiently. Secondly, the difficulty 
encountered by machine learning models in reliably identi-
fying high-engagement users points to the need for real-time 
behavioral tracking, psychographic profiling, and adaptive 
interfaces that respond dynamically to user patterns. Incor-
porating these elements could enhance user trust, retention, 
and ultimately, technology acceptance.

Despite its contributions, this study has several limita-

tions that must be acknowledged:

•  Single source and cross-sectional dataset: The analysis 
relies on one dataset from a single platform, which lim-
its the generalizability of findings across regions, demo-
graphics, and types of FinTech services.

•  Behavioral proxy constraints: While daily app usage is a 
practical measure of engagement, it may not fully capture 
deeper cognitive and emotional dimensions of technol-
ogy acceptance such as trust, perceived usefulness, or 
risk aversion.

•  Use of only static features: The model applies static snap-
shot data without incorporating temporal or sequential 
behavioral patterns. These patterns are often critical for 
capturing evolving user behavior and engagement trends.
•  Missing psychographic variables: Factors such as finan-
cial goals, personality traits, or digital literacy levels, 
which often moderate technology adoption, are not pre-
sent in the dataset. This limits interpretability.

•  Class imbalance issue: The relatively small proportion 
of high-acceptance users posed challenges for predictive 
performance, especially in recall metrics, despite apply-
ing techniques like SMOTE.

•  Lack of causal explanation: The machine learning mod-
els used in this study focus on pattern detection and do 
not support causal inference. As a result, it is difficult 
to determine the underlying mechanisms that drive user 
adoption.

These  limitations  highlight  the  importance  of  future 
research using longitudinal data, psychographic profiling, 
temporal behavior logs, and hybrid modeling frameworks 
that combine machine learning with theoretical or rule-
based systems. Such multimodal approaches can improve 
both predictive performance and theoretical understanding 
of FinTech adoption.

These limitations open several promising avenues for 
future research. First, future studies should consider longi-
tudinal data that tracks user interactions over time, enabling 
more robust modeling of behavioral change and technol-
ogy internalization. Second, incorporating hybrid modeling 
frameworks that combine machine learning with rule-based 
or fuzzy logic systems could enhance prediction in ambigu-
ous  or  overlapping  user  groups.  Third,  addressing  class 
imbalance using advanced techniques such as ensemble 
bagging, cost-sensitive learning, or generative oversampling 
(e.g., SMOTE, ADASYN) could improve minority class 
detection. Lastly, future work should incorporate qualita-
tive variables, such as digital literacy, perceived risk, and 
financial goals, which may help contextualize engagement 
patterns in more meaningful ways.

In conclusion, this research offers a novel, data-driven 
perspective on technology acceptance in FinTech, bridging 
the gap between behavioral modeling and predictive analyt-
ics. While machine learning shows promise in identifying 
patterns of engagement, its limitations remind us that tech-
nology adoption remains a complex human phenomenon, 
influenced by not only usage metrics but also psychological, 
social, and contextual factors. Understanding and embracing

---

<!-- PAGE 11 -->

SN Computer Science           (2025) 6:674

Page 11 of 12

674

this complexity will be key to building more inclusive, intel-
ligent, and user-centered financial technologies in the future.

Author Contributions  Sayyed Khawar Abbas contributed to conceptu-
alization, methodology, supervision, writing of the original draft, and 
critical review and editing. Muzzammil Hussain contributed to data 
curation, formal analysis, visualization, and manuscript review and 
editing. Yagya Nath Rimal contributed to software implementation, 
model validation, investigation, and manuscript review and editing.

Funding  Open access funding provided by Corvinus University of 
Budapest.

Data Availability  The data will be provided on request.

Declarations

Conflict  of  interest  All  authors  certify  that  they  have  no  conflict  of 
interest.

Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

1.  Barile D, Secundo G, Bussoli C, Exploring artificial intelligence 
robo-advisor in banking industry: a platform model. Manag Decis 
(2024).

2.  Zhang L, Pentina I, Fan Y. Who do you choose? comparing per-
ceptions of human vs robo-advisor in the context of financial ser-
vices. J Serv Mark. 2021;35(5):634–46.

3.  Abbas SK, Kő A, Szabó Z. B2B financial sector behavior con-
cerning cognitive chatbots. personalized contextual chatbots in 
financial sector. In: 2023 14th IEEE international conference on 
cognitive infocommunications (CogInfoCom). IEEE; 2023. p. 
000085–90.

4.  Theodorakopoulos  L,  Theodoropoulou  A.  Leveraging  big 
data analytics for understanding consumer behavior in digital 
marketing:  a  systematic  review.  Hum  Behav  Emerg  Technol. 
2024;2024(1):3641502.

5.  Jeyaraj A, Dwivedi YK, Venkatesh V. Intention in information 
systems adoption and use: current state and research directions, 
vol. 73. Elsevier; 2023. p. 102680.

6.  Sun  J,  et  al.  Prediction  of  toc  content  in  organic-rich  shale 
using machine learning algorithms: comparative study of ran-
dom  forest,  support  vector  machine,  and  Xgboost.  Energies. 
2023;16(10):4159.

7.  Davis FD. Technology acceptance model: TAM. Al-Suqri, MN,

Al-Aufi, AS: Inf Seek Behav Technol Adopt. 1989;205(219):5.

8.  Williams MD, Rana NP, Dwivedi YK. The unified theory of 
acceptance and use of technology (UTAUT): a literature review. 
J Enterp Inf Manag. 2015;28(3):443–88.

9.  Cheng Y-M. How can robo-advisors retain end-users? Identifying 
the formation of an integrated post-adoption model. J Enterp Inf 
Manag. 2023;36(1):91–122.

10.  Chen Y, Aw EC-X, Tan GW-H. Financial empowerment through 
robo-advisors: understanding the keys to trust and loyalty. Ind 
Manag Data Syst. 2025;125(6):2178–205.

11.  Aw EC-X, Zha T, Chuah SH-W. My new financial companion! 
non-linear understanding of robo-advisory service acceptance. 
Serv Ind J. 2023;43(3–4):185–212.

12.  Sundaram  A,  Gonçalves  J,  Ghorbani  A,  Verma  T.  Network 
dynamics of solar PV adoption: reconsidering flat tax-credits 
and influencer seeding for inclusive renewable energy access in 
Albany county, New York. Energy Res Soc Sci. 2024;112:103518.
 13.  Lin K-Y, Huang TK. Shopping in the digital world: how aug-
mented reality mobile applications trigger customer engagement. 
Technol Soc. 2024;77:102540.

14.  Manzoor  A,  Qureshi  MA,  Kidney  E,  Longo  L.  A  review  on 
machine learning methods for customer churn prediction and 
recommendations  for  business  practitioners.  IEEE  Access. 
2024;12:70434–63.

15.  Selvalakshmi V, Sree TMU, Saranya S, Devi AU, Basha MSA. 
Enhancing  customer  personality  prediction  using  advanced 
machine learning techniques and data balancing strategies: a 
comprehensive approach to addressing imbalanced datasets in 
marketing analytics. In: 2025 international conference on intelli-
gent systems and computational networks (ICISCN). IEEE; 2025. 
p. 1–7.

16.  Singh S, Sahni MM, Kovid RK. What drives FinTech adoption? a 
multi-method evaluation using an adapted technology acceptance 
model. Manag Decis. 2020;58(8):1675–97.

17.  Barjak F, Lindeque J, Koch J, Soland M. Segmenting household 
electricity customers with quantitative and qualitative approaches. 
Renew Sustain Energy Rev. 2022;157:112014.

18.  Roh T, Yang YS, Xiao S, Park BI. What makes consumers trust 
and adopt fintech? an empirical investigation in China. Electron 
Commer Res. 2024;24(1):3–35.

19.  Kavzoglu  T,  Teke  A.  Predictive  performances  of  ensemble 
machine learning algorithms in landslide susceptibility map-
ping using random forest, extreme gradient boosting (XGBoost) 
and  natural  gradient  boosting  (NGBoost).  Arab  J  Sci  Eng. 
2022;47(6):7367–85.

20.  DeVries Z, et al. Using a national surgical database to predict 
complications following posterior lumbar surgery and compar-
ing the area under the curve and F1-score for the assessment of 
prognostic capability. Spine J. 2021;21(7):1135–42.

21.  Singha S, Pasupuleti S, Singha SS, Singh R, Kumar S. Prediction 
of groundwater quality using efficient machine learning technique. 
Chemosphere. 2021;276:130265.

22.  Kumaravel A, Vijayan T. Comparing cost sensitive classifiers 
by the false-positive to false-negative ratio in diagnostic studies. 
Expert Syst Appl. 2023;227:120303.

23.  Ali N, Shabn OS. Customer lifetime value (CLV) insights for stra-
tegic marketing success and its impact on organizational financial 
performance. Cogent Bus Manag. 2024;11(1):2361321.

24.  Zemin G, et al. MIRRIFT: Multimodal image rotation and resolu-
tion invariant feature transformation. IEEE Trans Geosci Remote 
Sens. 2025. https:// doi. org/ 10. 1109/ TGRS. 2025. 35546 42.
 25.  Won D, Lee C. What influences season ticket holders’ satisfaction 
and renewal intention? the role of season ticket service quality. 
Manag Sport Leisure. 2024;29(4):572–90.

26.  Barreñada L, Dhiman P, Timmerman D, Boulesteix A-L, Van 
Calster B. Understanding overfitting in random forest for prob-
ability estimation: a visualization and simulation study. Diagn 
Progn Res. 2024;8(1):14.

---

<!-- PAGE 12 -->

674

Page 12 of 12

SN Computer Science           (2025) 6:674

27.  Ehsani F, Hosseini M. Customer churn analysis using feature 
optimization methods and tree-based classifiers. J Serv Mark. 
2025;39(1):20–35.

28.  Fry J, Fuller-Love N, Owen R. VIP/Hospitality event packages: 
using online reviews to improve the ticket purchase journey map. 
Event Manag. 2024. https:// doi. org/ 10. 3727/ 15259 9525X 17367 
48490 6390.

29.  Duan C, et al. A combination of XGBoost and neural network in 
LIBS spectrum processing for precise determination of critical 
elements in 620 iron ore samples of various origins. Spectrochim 
Acta, Part B. 2024;221:107056.

30.  Altalhan M, Algarni A, Alouane MT-H. Imbalanced data problem 
in machine learning: a review. IEEE Access. 2025;13:13686–99.
 31.  Zhang C, Bengio S, Hardt M, Recht B, Vinyals O. Understanding 
deep learning (still) requires rethinking generalization. Commun 
ACM. 2021;64(3):107–15.

32.  Pan Y, Chen H. Securing customer loyalty in the highly competi-
tive chinese hospitality market: an examination of the influence 
of sustainability, service quality, and brand equity. J Qual Assur 
Hosp Tour. 2025. https:// doi. org/ 10. 1080/ 15280 08X. 2025. 24602 
02.

33.  Abbas SK, Szabó Z, Kő A. Robo-advisors in fintech-challenges

and solutions. Acta Polytech Hung. 2025;22(6):131–51.

34.  Abbas SK. AI meets finance: the rise of AI-powered Robo-advi-

sors. J Electr Syst. 2024;20(11):1011–6.

35.  Belanche D, Casaló LV, Flavián C. Artificial Intelligence in Fin-
Tech: understanding robo-advisors adoption among customers. 
Ind Manag Data Syst. 2019;119(7):1411–30.

36.  Jünger  M,  Mietzner  M.  Banking  goes  digital:  the  adoption 
of FinTech services by German households. Financ Res Lett. 
2020;34:101260.

37.  Mantello P, Ho M-T, Nguyen M-H, Vuong Q-H. Machines that 
feel: behavioral determinants of attitude towards affect recognition 
technology—upgrading technology acceptance theory with the 
mindsponge model. Hum Soc Sci Commun. 2023;10(1):1–16.

38.  Szukits Á. The illusion of data-driven decision making–The medi-
ating effect of digital orientation and controllers’ added value in 
explaining organizational implications of advanced analytics. J 
Manag Control. 2022;33(3):403–46.

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to 
jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

SN Computer Science           (2025) 6:674
https://doi.org/10.1007/s42979-025-04214-8

ORIGINAL RESEARCH

Machine Learning‑Based Analysis of Technology Acceptance
in FinTech: A Behavioral Study Using Digital Wallet Data

Sayyed Khawar Abbas1

 · Muzzammil Hussain2 · Yagya Nath Rimal3

Received: 17 June 2025 / Accepted: 11 July 2025
© The Author(s) 2025

Abstract
The rapid growth of FinTech services, particularly robo-advisors, has transformed how individuals engage with digital
financial platforms. Understanding the behavioral drivers of technology acceptance in this context is critical for enhancing
adoption and designing more effective user experiences. This study investigates whether user-level behavioral and trans-
actional data can be leveraged to predict technology acceptance, operationalized through daily app usage. Grounded in the
Technology Acceptance Model (TAM) and Unified Theory of Acceptance and Use of Technology (UTAUT), the study
uses behavioral proxies such as customer satisfaction, loyalty points, and lifetime value to reflect constructs like perceived
usefulness, performance expectancy, and facilitating conditions. Using a real-world dataset of 7000 FinTech users sourced
from Kaggle, we applied four machine learning algorithms, Logistic Regression, Support Vector Machine, Random Forest,
and XGBoost, to classify users into high and low acceptance categories. Results revealed that ensemble models, particularly
XGBoost, outperformed linear classifiers, achieving moderate improvements in precision and recall for the high-acceptance
class. However, overall predictive performance remained constrained by class imbalance and overlapping behavioral patterns.
These findings suggest that while machine learning can reveal patterns linked to technology acceptance, predictive preci-
sion remains limited without richer temporal and psychographic features. The study contributes to the evolving discourse
on FinTech adoption by offering a data-driven lens to complement intention-based models and inform adaptive engagement
strategies.

Keywords  FinTech · Robo-advisors · Technology acceptance · Machine learning · Behavioral prediction · User
engagement · XGBoost · Random forest · Digital financial services · Imbalanced classification

 *  Sayyed Khawar Abbas

sayyedkhawar.abbas@uni-corvinus.hu;
Sayyedkhawarabbas@gmail.com

  Muzzammil Hussain
  Muzzammil.hussain@kfupm.edu.sa

  Yagya Nath Rimal

Rimal.yagya@gmail.com

1

Institute of Data Analytics and Information Systems,
Department of Information Systems, Corvinus University
of Budapest, 8 Fovam Ter, Budapest 1093, Hungary

2

Interdisciplinary Research Center for Finance and Digital
Economy, KBS, KFUPM, Dhahran, Saudi Arabia
3  Faculty of Science and Technology, Pokhara University,

Pokhara, Nepal

Introduction

The advancement of financial technology (FinTech) has sig-
nificantly reshaped the global financial landscape by enhanc-
ing the accessibility, efficiency, and personalization of finan-
cial services. A notable innovation within this domain is
the rise of robo-advisors, automated digital platforms that
use algorithms and artificial intelligence to provide invest-
ment advice and portfolio management with minimal human
supervision [1]. These systems have gained increasing atten-
tion for their potential to democratize financial planning and
deliver scalable, cost-effective solutions to a broad base of
users.

Despite  their  rapid  proliferation,  the  acceptance  of
robo-advisors among users remains inconsistent [2], often
influenced  by  complex  behavioral,  economic,  and  tech-
nological factors. Understanding what drives or hinders
user  acceptance  is  critical  for  both  FinTech  developers

Vol.:(0123456789)SN Computer Science

  674

Page 2 of 12

SN Computer Science           (2025) 6:674

and policymakers, particularly as digital financial services
continue to expand into diverse markets and demographic
segments. Traditional approaches to measuring technol-
ogy acceptance have relied primarily on models such as
the Technology Acceptance Model (TAM) or the Unified
Theory of Acceptance and Use of Technology (UTAUT),
typically evaluated through structured surveys [3]. However,
these models may not fully capture real-time behavioral data
and actual engagement patterns that are now increasingly
available through digital platforms [4].

This study addresses this limitation by leveraging a real-
world dataset from Kaggle, which includes detailed behavio-
ral and transactional data from 7000 users of a digital wallet
platform. To operationalize technology acceptance in this
context, daily app usage is used as a behavioral proxy for
high technology adoption [5]. The study then applies a com-
parative machine learning framework using Logistic Regres-
sion, Support Vector Machine (SVM), Random Forest, and
XGBoost to classify users based on their likelihood of high
technology acceptance [6].

The primary aim of this research is twofold:

1)  To evaluate the predictive capacity of multiple machine
learning algorithms in modeling technology acceptance
based on digital behavioral data; and

2)  To identify the most influential features, such as cus-
tomer satisfaction, loyalty points, and lifetime value
(LTV), that correlate with increased engagement and
adoption.

The contributions of this study are as follows:

•  It  provides  a  data-driven  perspective  on  technology
acceptance using real transactional and engagement data
rather than theoretical survey constructs.

•  It presents a comparative performance analysis of widely
used machine learning models in the context of imbal-
anced classification tasks.

•  It highlights key behavioral and transactional predictors
of FinTech technology acceptance, with implications for
targeted design, personalization, and customer retention
strategies.

Despite  valuable  insights  from  TAM,  UTAUT,  and
related  models,  most  existing  studies  rely  on  structured
surveys and intention-based indicators. These approaches,
while theoretically robust, may not fully reflect real-world
engagement, often suffering from self-reporting bias and
lack of contextual nuance. This creates a critical research
gap: limited empirical evidence exists on how actual behav-
ioral data, particularly transactional, usage, and support
interactions, map onto technology acceptance in FinTech.
Our study addresses this gap by leveraging a large-scale,

real-world dataset and applying machine learning models
to detect behavioral signals of adoption. By framing daily
app usage as a proxy for sustained technology acceptance
and linking behavioral variables to theoretical constructs, the
study contributes both methodologically and theoretically to
the FinTech adoption literature. It offers a novel perspective
that complements traditional perceptual frameworks with
predictive insights rooted in real user behavior.

This article is structured as follows. Sect. "Literature
Review" presents a review of the relevant literature on Fin-
Tech adoption and machine learning applications in behav-
ioral prediction. Sect. "Methodology" describes the dataset,
preprocessing steps, and machine learning methodologies
employed. Sect. "Results" discusses the results of the model
evaluation and feature importance analysis. Sect. "Discus-
sion" interprets these findings and explores their implica-
tions, while Sect. "Conclusion" concludes the paper with a
summary and directions for future research.

Literature Review

The  accelerating  digitalization  of  financial  services  has
reshaped the dynamics of consumer interaction with tech-
nology, giving rise to the widespread deployment of robo-
advisors and other AI-enabled financial tools. Understanding
how users engage with such systems has become a crucial
research focus, intersecting domains such as technology
acceptance, behavioral finance, and machine learning. This
section provides an overview of key theoretical frameworks,
empirical findings on FinTech adoption, and recent method-
ological advances leveraging machine learning in behavioral
prediction tasks.

Theoretical Models of Technology Acceptance

The literature on user acceptance of technology is deeply
rooted in psychological and behavioral theories. The Tech-
nology Acceptance Model (TAM) introduced by Davis [7],
remains one of the most widely cited frameworks, positing
that perceived usefulness and perceived ease of use directly
influence an individual’s behavioral intention to use a tech-
nology. Subsequent models, such as TAM2, TAM3, and
the Unified Theory of Acceptance and Use of Technology
(UTAUT) [8], have extended this foundation by incorporat-
ing variables such as social influence, facilitating conditions,
hedonic motivation, and price value.

In financial services, these models have been adapted to
assess acceptance of internet banking, mobile payment apps,
and recently, robo-advisors [9]. However, such models often
rely on cross-sectional survey data, which may be suscepti-
ble to self-reporting biases and may not adequately capture
actual user behavior over time.

SN Computer Science
SN Computer Science           (2025) 6:674

Page 3 of 12

  674

FinTech and Robo‑Advisor Adoption

Recent studies have explored the factors influencing the
adoption of robo-advisors, highlighting constructs such as
trust, transparency, algorithm aversion, and financial literacy
[10]. Zhang, et al. [2] found that perceived competence and
benevolence of the algorithm significantly impact users’
willingness to adopt robo-advisory services. Similarly, Aw,
et al. [11] emphasized the moderating role of digital finan-
cial literacy in shaping robo-advisor usage.

Despite the growing body of work, there is a scarcity
of research using behavioral datasets to infer adoption pat-
terns [12]. Most existing studies depend on hypothetical
scenarios or intention-based measurements, limiting their
external validity. Moreover, limited effort has been made to
operationalize technology acceptance through actual usage
metrics, such as frequency of app interaction, transactional
depth, and engagement behavior, which are more reflective
of real-world acceptance [13].

Machine Learning in FinTech and Behavioral
Modeling

Machine learning (ML) offers a powerful set of tools for
modeling behavioral outcomes in complex, high-dimen-
sional environments, making it particularly suitable for Fin-
Tech applications. Prior research has successfully employed
ML techniques for credit scoring, fraud detection, and churn
prediction [14]. In the domain of customer behavior mod-
eling, classifiers such as Random Forest, Support Vector
Machines (SVM), and Gradient Boosting (XGBoost) have
been applied to detect risk profiles, segment users, and opti-
mize marketing strategies [15].

However, the application of ML in the context of technol-
ogy acceptance, particularly in the FinTech domain, remains
limited. While ML has been used in recommender systems
and digital personalization [16], few studies have attempted
to use it to predict technology adoption based on rich behav-
ioral datasets. Moreover, the challenge of class imbalance in
such predictive tasks, where the number of high-engagement
or early-adopter users is often relatively low, has been insuf-
ficiently addressed in most empirical studies [17].

Research Gap and Contribution

Drawing from the aforementioned literature, a clear gap
emerges in the empirical study of real behavioral signals of
technology acceptance in FinTech [16, 18]. While theoreti-
cal models provide foundational insights, and survey-based
studies offer perceptual understandings, the predictive mod-
eling of technology adoption using machine learning and
real-world behavioral data remains underexplored.

This study aims to fill this gap by:

•  Using a publicly available FinTech behavioral dataset that
captures a wide range of transactional and engagement
variables.

•  Operationalizing technology acceptance through daily

app usage, a tangible behavioral proxy.

•  Applying and comparing the performance of Logistic
Regression,  SVM,  Random  Forest,  and  XGBoost  to
model this binary classification task.

•  Evaluating feature importance and model interpretability

to provide actionable insights for practitioners.

By doing so, this research bridges the theoretical and
data-driven approaches, offering a novel methodological
contribution to the field of FinTech adoption and presenting
practical implications for robo-advisor design, targeting, and
personalization strategies.

Methodology

This study adopts a structured, data-driven methodology to
examine the behavioral dimensions of technology accept-
ance in FinTech, using machine learning techniques applied
to real-world customer engagement data from south Asia.
The analysis is based on the Digital Wallet LTV Dataset,1
a publicly available dataset sourced from Kaggle, which
comprises 7,000 user-level records and 20 features. These
include demographic attributes (such as age, location, and
income level), transactional indicators (including total trans-
actions, average and maximum transaction value), behav-
ioral metrics (such as app usage frequency, loyalty points,
referral count), and outcome variables such as Customer Sat-
isfaction Score and Customer Lifetime Value (LTV). The
breadth and granularity of the dataset make it well-suited
for modeling technology adoption behavior within a digital
financial context.

We  operationalized  technology  acceptance  using  the
App_Usage_Frequency feature, categorizing daily users as
'high acceptance' and weekly/monthly users as 'low accept-
ance.' While binary classification simplifies complex behav-
ior, daily usage offers a concrete behavioral proxy reflecting
sustained engagement. We acknowledge that this operation-
alization does not capture cognitive or affective components
of  technology  acceptance  (e.g.,  perceived  usefulness  or
trust), and suggest future work explore multi-level or con-
tinuous measures of engagement.

The data preprocessing phase involved multiple steps
to ensure model readiness and integrity. First, all records
were  verified  to  be  free  of  missing  values.  Categorical

1  https:// www. kaggle. com/ datas ets/ harun rai/ finte ch- custo mer- life-
time- value- ltv- datas et

SN Computer Science  674

Page 4 of 12

SN Computer Science           (2025) 6:674

variables such as location, income level, and preferred pay-
ment method were transformed into numeric form using
label encoding. Redundant identifiers such as customer ID
were removed, and all numerical variables were standard-
ized using z-score normalization to mitigate scale-related
biases during training. The final feature matrix included 18
independent variables. Class imbalance was identified in the
target variable, with approximately 33.5% of users labeled
as high acceptance. Although no oversampling or under-
sampling techniques were applied at this stage, performance
metrics were selected to account for imbalance effects during
evaluation. To address the class imbalance (approximately
33.5% high-acceptance users), we applied for the Synthetic
Minority Oversampling Technique (SMOTE) during train-
ing.  SMOTE  generates  synthetic  samples  of  the  minor-
ity class, enabling the models to better learn the decision
boundaries. Models were retrained using SMOTE-applied
training sets, and performance was re-evaluated. As detailed
in Sect. "Results", this led to measurable improvements in
F1-score and recall for the minority class, particularly in
ensemble models.

Four  machine  learning  algorithms  were  employed  to
model the classification task: Logistic Regression, Support
Vector Machine (SVM), Random Forest, and Extreme Gra-
dient Boosting (XGBoost) [19]. Logistic Regression served
as a baseline model due to its interpretability and wide-
spread use in binary classification. SVM was included for
its robustness in high-dimensional spaces and capacity for
non-linear separation. Random Forest and XGBoost, both
tree-based ensemble methods, were chosen for their abil-
ity to model complex feature interactions, handle heteroge-
neous data types, and provide built-in measures of feature
importance. All models were implemented in Python using
the scikit-learn and xgboost libraries. The dataset was par-
titioned using an 80/20 train-test split, with stratified sam-
pling employed to maintain class proportions across both
sets. Hyperparameters were optimized through grid search
and cross-validation to enhance generalizability.

Model  performance  was  evaluated  using  a  compre-
hensive set of metrics. These included accuracy to gauge
overall predictive success; precision, recall, and F1-score
to provide class-specific insights; and the area under the
Receiver Operating Characteristic (ROC AUC) to assess the
discriminative power of the classifiers. Confusion matrices
were used to analyze error types, while probabilistic out-
puts were assessed using Mean Absolute Error (MAE) and
Root Mean Square Error (RMSE) as secondary evaluation
measures. These metrics collectively provided a nuanced
understanding of model strengths and limitations, especially
in the presence of class imbalance.

To  enhance  the  interpretability  of  results,  especially
given the increasing emphasis on explainable artificial intel-
ligence (XAI) in FinTech applications, feature importance

Table 1   Machine learning model performance metrics

Model

Accuracy ROC
AUC

Precision
(high)

Recall
(high)

F1-score
(high)

Logistic
Regres-
sion
SVM
Random
Forest
XGBoost

0.665

0.514

0.00

0.00

0.00

0.665
0.665

0.507
0.496

0.00
0.50

0.615

0.519

0.34

0.00
0.03

0.16

0.00
0.06

0.22

was analyzed using both model-specific and model-agnostic
methods. The Random Forest and XGBoost models gener-
ated intrinsic importance scores for each variable, indicat-
ing their relative contribution to predictive performance. In
addition, SHapley Additive exPlanations (SHAP) values
were computed to offer both local and global interpretability,
revealing how specific features influenced individual predic-
tions and overall model behavior. This was complemented
by rich visual diagnostics, including 3D scatter plots to
capture multivariate interactions, dimensionality reduction
techniques such as t-SNE and Principal Component Analy-
sis (PCA) for visualizing data clusters, and ROC/precision-
recall curves to assess threshold sensitivity.

All experiments were conducted in a Jupyter Notebook
environment using Python 3.11. The computational pipe-
line  was  built  with  standard  libraries  including  pandas,
numpy, matplotlib, seaborn, shap, and plotly. The full code
and supporting visualizations are available upon request to
promote transparency and reproducibility. Ethical considera-
tions were observed throughout the study, with the dataset
fully anonymized and publicly accessible, thereby ensuring
compliance with data protection norms. This methodological
approach not only supports the robust modeling of behav-
ioral technology acceptance but also provides a replicable
framework for future FinTech research focused on real-world
engagement signals.

Results

The objective of this study was to assess the effectiveness of
various machine learning models in predicting high levels
of technology acceptance—measured via daily app usage—
among FinTech users. This section presents the compara-
tive performance of four classification algorithms: Logistic
Regression, Support Vector Machine (SVM), Random For-
est, and XGBoost. The models were evaluated on several key
metrics including overall accuracy, ROC AUC score, and
class-specific precision, recall, and F1-score, with a particu-
lar emphasis on their ability to detect users exhibiting high
technology acceptance behavior.

SN Computer Science
SN Computer Science           (2025) 6:674

Page 5 of 12

  674

A  summary  of  model  performance  is  presented  in
Table 1. While all four classifiers achieved similar accuracy
levels, approximately 66.5%, the ROC AUC scores, which
offer a more nuanced view in the presence of class imbal-
ance, were modest across all models. XGBoost demonstrated
the highest ROC AUC at 0.519, followed closely by Logis-
tic Regression at 0.514. SVM and Random Forest lagged
slightly behind, indicating limited capability of all models
in separating high and low technology acceptance classes
based on the available features.

Although accuracy remained consistent across models,
the deeper class-level analysis reveals a stark contrast in how
well each classifier handled the minority class, users with
high technology acceptance. Logistic Regression and SVM,
both linear models, completely failed to identify this group,
yielding zero precision, recall, and F1-score, consistency can
be found [20]. This suggests an inherent limitation in their
ability to model the complex, nonlinear relationships likely
present in the behavioral features.

In contrast, the ensemble models, Random Forest and
XGBoost, offered significantly better insight into this minor-
ity class. Random Forest achieved a high precision of 0.50,
indicating that when it predicted a user as a high-accept-
ance case [21], it was often correct. However, its recall of
just 0.03 signals an extremely high false-negative rate [22],
meaning it failed to identify the vast majority of actual daily
users. XGBoost, on the other hand, demonstrated a more
balanced performance with precision at 0.34 and recall at
0.16, producing the highest F1-score of 0.22 among all mod-
els for this class. While this still reflects a limited ability
to detect high-tech-acceptance users, it marks a significant
improvement over linear method.

After  applying  SMOTE  to  the  training  data,  model
performance on the minority class improved. XGBoost’s
F1-score increased from 0.22 to 0.36, and Random Forest’s
F1-score improved to 0.28. Recall for XGBoost rose from
0.16 to 0.27, showing a more balanced identification of high-
acceptance users.

These results are visually summarized in Fig. 1, which
compares the accuracy and ROC AUC of all models. The
graph illustrates that despite similar surface-level perfor-
mance (accuracy), the underlying discriminatory power, rep-
resented by ROC AUC, is weak, hovering close to 0.5, which
reflects near-random classification. The comparatively better
performance of XGBoost points to its capability in handling
feature interaction and minor class signals more effectively
than its counterparts.

To further evaluate classifier performance, especially
given the class imbalance in the dataset, we examined both
the Precision–Recall (PR) curves and the Receiver Operat-
ing Characteristic (ROC) curves for each model, as shown
in  Fig.  1.  The  left  panel  of  the  figure  illustrates  the  PR
curves, which are particularly informative for imbalanced
classification tasks as they emphasize the models' ability to
identify positive class instances (i.e., users with high tech-
nology acceptance). While all models exhibited relatively
low precision across most recall thresholds, the Random
Forest (AP = 0.345) and XGBoost (AP = 0.343) classifiers
demonstrated marginally superior performance compared
to Logistic Regression and SVM, whose average precision
scores were 0.338 and 0.333, respectively.

The right panel of Fig. 2 presents the ROC curves for all
models. In this visualization, XGBoost attained the highest
area under the curve (AUC = 0.519), followed closely by

Fig. 1   Precision–Recall  (left)  and  ROC  Curves  (right)  for  four  clas-
sification  models  (Logistic  Regression,  SVM,  Random  Forest,  and
XGBoost). Average Precision (AP) and AUC values are shown in the

legends. Curves indicate limited model discrimination, with ensemble
models  slightly  outperforming  linear  classifiers  in  identifying  high
technology acceptance users

SN Computer Science  674

Page 6 of 12

SN Computer Science           (2025) 6:674

Fig. 2   PCA results showing: (left) 3D projection of users colored by tech acceptance, (center) explained variance by components, and (right) key
feature loadings across PC1–PC3. LTV, Total Spent, and Satisfaction Score show strong influence on PC1

Logistic Regression (AUC = 0.514), while Random Forest
(AUC = 0.496) and SVM (AUC = 0.507) remained close
to the diagonal line representing random guessing. These
results reinforce the earlier finding that although the models
offer some degree of predictive capability, their overall abil-
ity to differentiate between high and low engagement users
remains limited. Notably, the ROC curves suggest very mod-
est true positive rate improvements over chance, emphasiz-
ing the challenge of modeling real-world FinTech behavior
through static transactional features alone.

To explore latent structure in the data and assess whether
linear combinations of features could reveal distinguishable
clusters of technology acceptance, a Principal Component
Analysis (PCA) was conducted. Figure 2 presents a three-
panel summary of the PCA results. The left panel shows
a 3D projection of the data using the first three principal
components, with points colored by technology acceptance
status (red for high acceptance, blue for low). Although no
clear separation is observed, subtle patterns in spatial dis-
tribution suggest that certain combinations of variables may
partially differentiate user classes.

The middle panel displays the variance explained by each
principal component. The first component (PC1) accounts
for approximately 21.4% of the total variance, followed by
PC2 (8.2%) and PC3 (5.97%), indicating that the first three
components together capture about 35.6% of the total infor-
mation. While this level of variance is moderate, it does
provide a reduced yet informative basis for visual explora-
tion and downstream modeling.

The rightmost panel presents the feature loadings for
each of the three components. Variables such as Customer
Lifetime Value (LTV), Total Spent, Customer Satisfaction
Score, and Average Transaction Value contributed strongly
to PC1[23], confirming their relevance in capturing behav-
ioral intensity. PC2 was more influenced by features like

Total Transactions and Issue Resolution Time [24], while
PC3 showed moderate contributions from Support Tickets
Raised and Loyalty Points Earned [25]. These insights rein-
force the notion that while a few behavioral features carry
strong signals, the variance is distributed across multiple
dimensions, and no single component dominates the repre-
sentation space.

To further interpret model performance and understand
feature contributions to predictions, we conducted several
advanced machine learning analyses, presented in Fig. 3.
The upper left panel shows the validation curve for the Ran-
dom Forest model with varying numbers of estimators [26].
As expected, training accuracy remains near perfect across
all values, while validation accuracy plateaus at around
66.5%, suggesting the model is not overfitting but also lim-
ited in learnable signal from the data.

The upper right panel compares the feature importance
scores of Random Forest and XGBoost models. Features
such as LTV, Customer Satisfaction Score, and Issue Resolu-
tion Time consistently ranked highest in both models [27],
reinforcing earlier findings about the influence of financial
value and service experience on daily usage behavior. Other
important features include Support Tickets Raised, Pre-
ferred Payment Method, and Referral Count [28], pointing
to behavioral and interaction-based drivers of engagement.
The lower left panel presents the distribution of predicted
probabilities from the Random Forest model [26]. Predic-
tions for both high and low tech acceptance classes cluster
near the middle, indicating that the model often expresses
uncertainty. The significant overlap between classes suggests
that the available features only weakly separate user groups,
which aligns with the modest precision-recall performance
seen earlier.

Finally, the bottom right panel shows the calibration
curves for both Random Forest and XGBoost models [29].

SN Computer Science
SN Computer Science           (2025) 6:674

Page 7 of 12

  674

Fig. 3   Model diagnostics: (top left) Random Forest validation curve, (top right) feature importance comparison, (bottom left) predicted probabil-
ity distribution, and (bottom right) calibration curves for Random Forest and XGBoost

A perfectly calibrated model would align with the diago-
nal reference line. Here, both models deviate from ideal
calibration, particularly in mid-probability ranges, imply-
ing that predicted probabilities may not reliably reflect
true class membership likelihood. Nonetheless, calibration
remains within a tolerable range for exploratory decision-
support purposes.

From an interpretive standpoint, these findings partially
support the research hypothesis. Machine learning mod-
els, particularly ensemble methods, can identify signals of
high technology acceptance using behavioral and transac-
tional data. However, the overall results suggest that the
differentiation between high and low adoption users is
nuanced and potentially entangled in subtle behavioral
patterns not fully captured by the available features. The
weak recall scores highlight that many daily users exhibit

similar surface behavior to weekly or monthly users, com-
plicating prediction.

Furthermore, the limited success of even advanced classi-
fiers suggests that class imbalance, feature overlap, and lack
of temporal behavioral features pose significant challenges
[30]. The outcome indicates a need for incorporating richer
behavioral dynamics, such as session timing, transaction
sequences, or real-time feedback, to improve model robust-
ness. Additionally, deploying resampling methods (e.g.,
SMOTE), cost-sensitive learning, or hybrid approaches com-
bining rules with statistical learning could further strengthen
predictive power in future work.

In summary, while Random Forest and XGBoost show
some promise in identifying FinTech users likely to adopt
robo-advisory platforms based on engagement behavior,
the difficulty in reliably distinguishing these users from

SN Computer Science  674

Page 8 of 12

SN Computer Science           (2025) 6:674

less engaged ones points to the complexity of behavioral
acceptance as a predictive task. The subsequent section will
explore which specific features drove the models' predic-
tions and how they can inform FinTech product design and
personalization strategies.

Discussion

The findings of this study offer important insights into the
viability and limitations of using behavioral and transac-
tional  data  to  model  technology  acceptance  in  FinTech
platforms,  particularly  in  the  context  of  robo-advisory
adoption. While the research was guided by the hypothesis
that machine learning techniques could effectively differ-
entiate high-engagement users (i.e., daily app users) from
less engaged ones, the results reveal a more nuanced reality.
Although ensemble methods such as Random Forest and
XGBoost performed relatively better than linear models,
their discriminatory power, particularly in identifying users
with high technology acceptance, remained limited.

Our findings regarding behavioral predictors such as Cus-
tomer Satisfaction Score, Lifetime Value (LTV), and Loy-
alty Points Earned align with several perceptual constructs
highlighted in the literature. For instance, Zhang et al. [31]
emphasized the role of algorithmic competence and benevo-
lence in shaping trust, while Chen et al. [32] linked trust
and loyalty to the continued use of robo-advisory services
[33, 34]. In our case, satisfaction and LTV likely serve as
behavioral proxies for perceived usefulness and performance
expectancy, constructs central to TAM and UTAUT. Loy-
alty points and referral behaviors may correspond to hedonic
motivation and social influence, respectively. This empirical
support suggests that behavioral signals can serve as indirect
validations of established psychological constructs, though
the correspondence is not always one-to-one.

Notably, several key behavioral features such as Cus-
tomer Satisfaction Score, Lifetime Value, and Loyalty Points
Earned map closely to constructs from TAM and UTAUT
models. For instance, satisfaction and LTV align with 'per-
ceived usefulness' and 'performance expectancy,' while sup-
port resolution may relate to 'facilitating conditions.' This
theoretical alignment reinforces the behavioral validity of
our feature selection and supports deeper integration of data-
driven models with psychological theories of technology
acceptance.

However, the divergence between our machine learn-
ing models’ modest recall rates and the strong associations
found in perception-based studies invites critical reflection.
One plausible explanation is that ML models, particularly
those based on static transactional features, lack the con-
textual richness of perceptual constructs such as trust, per-
ceived risk, or financial anxiety. While users may report

high trust in robo-advisors in surveys, their behavioral data
may not reflect this sentiment due to external constraints or
situational factors (e.g., financial goals, income variability).
This disconnect underlines the limits of behavioral proxies
and suggests that psychographic and contextual variables
are indispensable for capturing the full adoption spectrum.
One of the most critical observations is that Logistic
Regression and Support Vector Machines failed entirely to
classify high-acceptance users, highlighting the insufficiency
of linear decision boundaries in capturing complex behavio-
ral dynamics. This aligns with prior research indicating that
financial behaviors, such as digital adoption and investment
decisions, often exhibit nonlinear interactions influenced by
multi-layered socio-demographic, psychological, and behav-
ioral factors [35, 36]. The modest performance of Random
Forest and XGBoost, where precision and recall improved
but remained well below acceptable thresholds, suggests that
while richer models can begin to decode patterns of engage-
ment, the overlap in behavioral signals between high and low
adoption groups presents a persistent challenge.

These results partially confirm the central hypothesis of
this study, that machine learning can uncover probabilistic
signals of technology acceptance, but the prediction task is
inherently difficult due to the class imbalance, limited proxy
variables, and lack of temporal context. For example, while
features like Customer Satisfaction Score, LTV, and Loyalty
Points Earned were found to be influential, their distributions
often overlapped significantly across both classes, undermin-
ing classification certainty. Moreover, the binary operation-
alization of technology acceptance, although grounded in
behavioral frequency, likely fails to capture the full spectrum
of user attitudes, intentions, and constraints that influence
digital platform engagement.

The findings further highlight the need for advanced fea-
ture engineering and modeling strategies. Given the limited
recall achieved by all models for the high acceptance class,
future research should consider incorporating time-series
features (e.g., user activity over time), contextual metadata
(e.g., promotional campaigns or app interface changes), or
external behavioral drivers (e.g., economic conditions or
peer influence). Additionally, addressing class imbalance
through oversampling techniques such as SMOTE, or by
applying cost-sensitive learning, may enable models to place
greater emphasis on minority class predictions.

From a practical standpoint, the study’s insights are rel-
evant for FinTech product managers and developers. The
finding  that  satisfaction  and  loyalty-related  metrics  are
among the most influential predictors suggests that improv-
ing resolution times, reward systems, and user experience
design could be effective levers to increase daily usage and
long-term adoption of robo-advisory services. Furthermore,
the difficulty encountered by even advanced models in clas-
sifying high-adoption users reinforces the importance of

SN Computer Science
SN Computer Science           (2025) 6:674

Page 9 of 12

  674

multi-modal personalization strategies, which go beyond
transactional patterns to include psychographic profiling,
dynamic behavioral cues, and interactive feedback loops.

In  comparison  with  previous  literature,  this  study
advances the field by employing a behaviorally-grounded
and data-driven approach to technology acceptance, con-
trasting with most earlier works that rely heavily on percep-
tual survey data and structural equation modeling [37, 38].
By focusing on actual user engagement metrics, this research
contributes a fresh methodological perspective that comple-
ments existing theoretical models like TAM and UTAUT
with empirical predictive insights.

Despite these contributions, the study is not without limi-
tations. The use of a single dataset limits generalizability,
and the absence of temporal and psychological variables
constrains the depth of behavioral modeling. Additionally,
while machine learning offers powerful tools for classifica-
tion, it does not inherently address causality, and interpret-
ability remains a challenge, particularly in black-box models
like XGBoost.

The  observed  discrepancy,  where  features  like  LTV
and satisfaction show high importance, yet models exhibit
low  recall,  mirrors  theoretical  expectations  from  TAM
and UTAUT. These models posit that while performance
expectancy and facilitating conditions are important, actual
adoption is mediated by intention and moderated by per-
sonal and environmental variables. Our findings suggest
that while behavioral indicators provide partial signals, they
are insufficient without accounting for the user’s internal

decision-making process or surrounding ecosystem. There-
fore, weak recall may not indicate model failure, but rather
the complexity of behavioral manifestation that lacks visible
differentiation in transactional data. To further clarify how
our dataset operationalizes theoretical constructs from TAM
and UTAUT, Table 2 provides a comparative summary of
key constructs, their proxy variables, empirical results, and
corresponding interpretations.

In conclusion, this study underscores the potential of
machine learning in enhancing our understanding of Fin-
Tech user behavior, but also reveals critical areas for meth-
odological refinement. The ability to predict technology
acceptance behaviorally is possible, but only to a limited
extent, when relying solely on transactional and static user
data. To move toward more reliable and actionable models,
future research should integrate longitudinal behavioral data,
hybrid modeling techniques, and cross-disciplinary insights
from behavioral economics, human–computer interaction,
and digital psychology.

This study contributes to theoretical discourse by offering
an empirical, data-driven lens through which to examine and
potentially refine constructs from TAM and UTAUT. While
these models traditionally rely on perceptual or intention-
based inputs, our ML-based behavioral approach reveals
the extent to which such constructs manifest in real-world
engagement patterns. The moderate alignment of satisfaction
and LTV with perceived usefulness and facilitating condi-
tions demonstrates the potential of behavioral modeling to
supplement traditional frameworks. Moreover, the study

Table 2   Comparative table: theoretical constructs, data representation, and empirical insights

Construct (from
TAM/UTAUT)

Repre-
sented in
dataset

Proxy variable used

Empirical finding

Interpretation and implication

Perceived usefulness

Yes

Customer satisfaction score

High feature importance

Aligns with TAM; satisfaction reflects
system value contributing to frequent
usage

Performance expectancy Yes

Lifetime value (LTV)

High feature importance

Suggests users adopt when longterm

Facilitating conditions

Partially

Hedonic motivation

Partially

Issue resolution
time, support tickets
Loyalty points, referral count

financial benefit is evident

Moderate importance

Indicates support access influences adop-
tion, but not strongly predictive alone
Moderate to low importance These engagement incentives influence
behavior but do not fully differentiate
high-use users

Social influence

No

Not available

Not tested

Trust and
competence
Digital literacy

Behavioral intention

Indirect

Satisfaction score (proxy), LTV Suggested through impor-

tance of satisfaction

No

No

Not available

Not tested

Not available

Not applicable

Missing from dataset; future studies
should include peer or community
influence variables

Implied link between good experience
and trust, but not directly measured
Important perceptual driver in literature;

absence limits generalizability
Study focused on actual behavior,

not intention. Supports shift toward
behavior-centric models

SN Computer Science  674

Page 10 of 12

SN Computer Science           (2025) 6:674

underscores the importance of transitioning from intention-
centric models to outcome-oriented behavioral analysis,
especially  as  granular  usage  data  becomes  increasingly
available in FinTech platforms.

Conclusion

This study set out to explore whether machine learning algo-
rithms can effectively predict behavioral technology accept-
ance among FinTech users, using real-world transactional
and engagement data. By framing daily app usage as a proxy
for high technology acceptance, and applying four differ-
ent classifiers—Logistic Regression, SVM, Random Forest,
and XGBoost—the research aimed to uncover the predictive
power of user behavior patterns in the adoption of robo-
advisory platforms. The results offer partial validation of this
objective. While ensemble methods like Random Forest and
XGBoost demonstrated better discriminatory performance
compared to linear models, their overall ability to detect
high-tech-acceptance users was limited, as evidenced by low
recall and modest AUC scores. These findings reveal that
while behavioral features contain signals of engagement,
the distinction between high and low adopters is subtle and
non-trivial to model.

While the inclusion of SMOTE improved classification of
high-engagement users, challenges remain. This reinforces
that behavioral data alone may not be sufficient for robust
prediction without temporal depth or psychographic inputs.
Our findings are promising but exploratory, and further vali-
dation is necessary before real-world deployment.

The study provides several important practical implica-
tions for FinTech companies and digital product managers.
Firstly, features related to customer satisfaction, loyalty pro-
grams, and spending patterns emerged as significant predic-
tors, underscoring the value of customer experience design
in promoting sustained app engagement. Companies aiming
to increase robo-advisor adoption should consider investing
in features that personalize user journeys, reward engage-
ment, and resolve issues efficiently. Secondly, the difficulty
encountered by machine learning models in reliably identi-
fying high-engagement users points to the need for real-time
behavioral tracking, psychographic profiling, and adaptive
interfaces that respond dynamically to user patterns. Incor-
porating these elements could enhance user trust, retention,
and ultimately, technology acceptance.

Despite its contributions, this study has several limita-

tions that must be acknowledged:

•  Single source and cross-sectional dataset: The analysis
relies on one dataset from a single platform, which lim-
its the generalizability of findings across regions, demo-
graphics, and types of FinTech services.

•  Behavioral proxy constraints: While daily app usage is a
practical measure of engagement, it may not fully capture
deeper cognitive and emotional dimensions of technol-
ogy acceptance such as trust, perceived usefulness, or
risk aversion.

•  Use of only static features: The model applies static snap-
shot data without incorporating temporal or sequential
behavioral patterns. These patterns are often critical for
capturing evolving user behavior and engagement trends.
•  Missing psychographic variables: Factors such as finan-
cial goals, personality traits, or digital literacy levels,
which often moderate technology adoption, are not pre-
sent in the dataset. This limits interpretability.

•  Class imbalance issue: The relatively small proportion
of high-acceptance users posed challenges for predictive
performance, especially in recall metrics, despite apply-
ing techniques like SMOTE.

•  Lack of causal explanation: The machine learning mod-
els used in this study focus on pattern detection and do
not support causal inference. As a result, it is difficult
to determine the underlying mechanisms that drive user
adoption.

These  limitations  highlight  the  importance  of  future
research using longitudinal data, psychographic profiling,
temporal behavior logs, and hybrid modeling frameworks
that combine machine learning with theoretical or rule-
based systems. Such multimodal approaches can improve
both predictive performance and theoretical understanding
of FinTech adoption.

These limitations open several promising avenues for
future research. First, future studies should consider longi-
tudinal data that tracks user interactions over time, enabling
more robust modeling of behavioral change and technol-
ogy internalization. Second, incorporating hybrid modeling
frameworks that combine machine learning with rule-based
or fuzzy logic systems could enhance prediction in ambigu-
ous  or  overlapping  user  groups.  Third,  addressing  class
imbalance using advanced techniques such as ensemble
bagging, cost-sensitive learning, or generative oversampling
(e.g., SMOTE, ADASYN) could improve minority class
detection. Lastly, future work should incorporate qualita-
tive variables, such as digital literacy, perceived risk, and
financial goals, which may help contextualize engagement
patterns in more meaningful ways.

In conclusion, this research offers a novel, data-driven
perspective on technology acceptance in FinTech, bridging
the gap between behavioral modeling and predictive analyt-
ics. While machine learning shows promise in identifying
patterns of engagement, its limitations remind us that tech-
nology adoption remains a complex human phenomenon,
influenced by not only usage metrics but also psychological,
social, and contextual factors. Understanding and embracing

SN Computer Science
SN Computer Science           (2025) 6:674

Page 11 of 12

  674

this complexity will be key to building more inclusive, intel-
ligent, and user-centered financial technologies in the future.

Author Contributions  Sayyed Khawar Abbas contributed to conceptu-
alization, methodology, supervision, writing of the original draft, and
critical review and editing. Muzzammil Hussain contributed to data
curation, formal analysis, visualization, and manuscript review and
editing. Yagya Nath Rimal contributed to software implementation,
model validation, investigation, and manuscript review and editing.

Funding  Open access funding provided by Corvinus University of
Budapest.

Data Availability  The data will be provided on request.

Declarations

Conflict  of  interest  All  authors  certify  that  they  have  no  conflict  of
interest.

Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

  1.  Barile D, Secundo G, Bussoli C, Exploring artificial intelligence
robo-advisor in banking industry: a platform model. Manag Decis
(2024).

  2.  Zhang L, Pentina I, Fan Y. Who do you choose? comparing per-
ceptions of human vs robo-advisor in the context of financial ser-
vices. J Serv Mark. 2021;35(5):634–46.

  3.  Abbas SK, Kő A, Szabó Z. B2B financial sector behavior con-
cerning cognitive chatbots. personalized contextual chatbots in
financial sector. In: 2023 14th IEEE international conference on
cognitive infocommunications (CogInfoCom). IEEE; 2023. p.
000085–90.

  4.  Theodorakopoulos  L,  Theodoropoulou  A.  Leveraging  big
data analytics for understanding consumer behavior in digital
marketing:  a  systematic  review.  Hum  Behav  Emerg  Technol.
2024;2024(1):3641502.

  5.  Jeyaraj A, Dwivedi YK, Venkatesh V. Intention in information
systems adoption and use: current state and research directions,
vol. 73. Elsevier; 2023. p. 102680.

  6.  Sun  J,  et  al.  Prediction  of  toc  content  in  organic-rich  shale
using machine learning algorithms: comparative study of ran-
dom  forest,  support  vector  machine,  and  Xgboost.  Energies.
2023;16(10):4159.

  7.  Davis FD. Technology acceptance model: TAM. Al-Suqri, MN,

Al-Aufi, AS: Inf Seek Behav Technol Adopt. 1989;205(219):5.

  8.  Williams MD, Rana NP, Dwivedi YK. The unified theory of
acceptance and use of technology (UTAUT): a literature review.
J Enterp Inf Manag. 2015;28(3):443–88.

  9.  Cheng Y-M. How can robo-advisors retain end-users? Identifying
the formation of an integrated post-adoption model. J Enterp Inf
Manag. 2023;36(1):91–122.

 10.  Chen Y, Aw EC-X, Tan GW-H. Financial empowerment through
robo-advisors: understanding the keys to trust and loyalty. Ind
Manag Data Syst. 2025;125(6):2178–205.

 11.  Aw EC-X, Zha T, Chuah SH-W. My new financial companion!
non-linear understanding of robo-advisory service acceptance.
Serv Ind J. 2023;43(3–4):185–212.

 12.  Sundaram  A,  Gonçalves  J,  Ghorbani  A,  Verma  T.  Network
dynamics of solar PV adoption: reconsidering flat tax-credits
and influencer seeding for inclusive renewable energy access in
Albany county, New York. Energy Res Soc Sci. 2024;112:103518.
 13.  Lin K-Y, Huang TK. Shopping in the digital world: how aug-
mented reality mobile applications trigger customer engagement.
Technol Soc. 2024;77:102540.

 14.  Manzoor  A,  Qureshi  MA,  Kidney  E,  Longo  L.  A  review  on
machine learning methods for customer churn prediction and
recommendations  for  business  practitioners.  IEEE  Access.
2024;12:70434–63.

 15.  Selvalakshmi V, Sree TMU, Saranya S, Devi AU, Basha MSA.
Enhancing  customer  personality  prediction  using  advanced
machine learning techniques and data balancing strategies: a
comprehensive approach to addressing imbalanced datasets in
marketing analytics. In: 2025 international conference on intelli-
gent systems and computational networks (ICISCN). IEEE; 2025.
p. 1–7.

 16.  Singh S, Sahni MM, Kovid RK. What drives FinTech adoption? a
multi-method evaluation using an adapted technology acceptance
model. Manag Decis. 2020;58(8):1675–97.

 17.  Barjak F, Lindeque J, Koch J, Soland M. Segmenting household
electricity customers with quantitative and qualitative approaches.
Renew Sustain Energy Rev. 2022;157:112014.

 18.  Roh T, Yang YS, Xiao S, Park BI. What makes consumers trust
and adopt fintech? an empirical investigation in China. Electron
Commer Res. 2024;24(1):3–35.

 19.  Kavzoglu  T,  Teke  A.  Predictive  performances  of  ensemble
machine learning algorithms in landslide susceptibility map-
ping using random forest, extreme gradient boosting (XGBoost)
and  natural  gradient  boosting  (NGBoost).  Arab  J  Sci  Eng.
2022;47(6):7367–85.

 20.  DeVries Z, et al. Using a national surgical database to predict
complications following posterior lumbar surgery and compar-
ing the area under the curve and F1-score for the assessment of
prognostic capability. Spine J. 2021;21(7):1135–42.

 21.  Singha S, Pasupuleti S, Singha SS, Singh R, Kumar S. Prediction
of groundwater quality using efficient machine learning technique.
Chemosphere. 2021;276:130265.

 22.  Kumaravel A, Vijayan T. Comparing cost sensitive classifiers
by the false-positive to false-negative ratio in diagnostic studies.
Expert Syst Appl. 2023;227:120303.

 23.  Ali N, Shabn OS. Customer lifetime value (CLV) insights for stra-
tegic marketing success and its impact on organizational financial
performance. Cogent Bus Manag. 2024;11(1):2361321.

 24.  Zemin G, et al. MIRRIFT: Multimodal image rotation and resolu-
tion invariant feature transformation. IEEE Trans Geosci Remote
Sens. 2025. https:// doi. org/ 10. 1109/ TGRS. 2025. 35546 42.
 25.  Won D, Lee C. What influences season ticket holders’ satisfaction
and renewal intention? the role of season ticket service quality.
Manag Sport Leisure. 2024;29(4):572–90.

 26.  Barreñada L, Dhiman P, Timmerman D, Boulesteix A-L, Van
Calster B. Understanding overfitting in random forest for prob-
ability estimation: a visualization and simulation study. Diagn
Progn Res. 2024;8(1):14.

SN Computer Science  674

Page 12 of 12

SN Computer Science           (2025) 6:674

 27.  Ehsani F, Hosseini M. Customer churn analysis using feature
optimization methods and tree-based classifiers. J Serv Mark.
2025;39(1):20–35.

 28.  Fry J, Fuller-Love N, Owen R. VIP/Hospitality event packages:
using online reviews to improve the ticket purchase journey map.
Event Manag. 2024. https:// doi. org/ 10. 3727/ 15259 9525X 17367
48490 6390.

 29.  Duan C, et al. A combination of XGBoost and neural network in
LIBS spectrum processing for precise determination of critical
elements in 620 iron ore samples of various origins. Spectrochim
Acta, Part B. 2024;221:107056.

 30.  Altalhan M, Algarni A, Alouane MT-H. Imbalanced data problem
in machine learning: a review. IEEE Access. 2025;13:13686–99.
 31.  Zhang C, Bengio S, Hardt M, Recht B, Vinyals O. Understanding
deep learning (still) requires rethinking generalization. Commun
ACM. 2021;64(3):107–15.

 32.  Pan Y, Chen H. Securing customer loyalty in the highly competi-
tive chinese hospitality market: an examination of the influence
of sustainability, service quality, and brand equity. J Qual Assur
Hosp Tour. 2025. https:// doi. org/ 10. 1080/ 15280 08X. 2025. 24602
02.

 33.  Abbas SK, Szabó Z, Kő A. Robo-advisors in fintech-challenges

and solutions. Acta Polytech Hung. 2025;22(6):131–51.

 34.  Abbas SK. AI meets finance: the rise of AI-powered Robo-advi-

sors. J Electr Syst. 2024;20(11):1011–6.

 35.  Belanche D, Casaló LV, Flavián C. Artificial Intelligence in Fin-
Tech: understanding robo-advisors adoption among customers.
Ind Manag Data Syst. 2019;119(7):1411–30.

 36.  Jünger  M,  Mietzner  M.  Banking  goes  digital:  the  adoption
of FinTech services by German households. Financ Res Lett.
2020;34:101260.

 37.  Mantello P, Ho M-T, Nguyen M-H, Vuong Q-H. Machines that
feel: behavioral determinants of attitude towards affect recognition
technology—upgrading technology acceptance theory with the
mindsponge model. Hum Soc Sci Commun. 2023;10(1):1–16.

 38.  Szukits Á. The illusion of data-driven decision making–The medi-
ating effect of digital orientation and controllers’ added value in
explaining organizational implications of advanced analytics. J
Manag Control. 2022;33(3):403–46.

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to
jurisdictional claims in published maps and institutional affiliations.

SN Computer Science
