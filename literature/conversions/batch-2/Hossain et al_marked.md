---
conversion_metadata:
  converted_at: "2026-07-22T13:35:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hossain et al.pdf"
  source_pdf_sha256: "d71dd4f06c78c3335c84a1faf80cbe483a76a7f305beac48de3bab48f3d29f6d"
  page_count: 14
  markdown_char_count: 88337
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

Enhancing Credit Scoring with Multimodal Deep Learning: A Hybrid Neural 
Network Approach Using Structured and Unstructured Financial Data

Md Refat Hossain 
Master of Business Administration (MBA), College of Business, Westcliff University, USA

Md Amran Hossen Pabel 
Masters of Science in Business Analytics Wright State University, Ohio, USA

Md Sayem Ul Haque 
MBA in Business Analytics, Gannon University, USA

Md Sayem Khan 
Master of Science in Project Management, Saint Francis College (SFC), Brooklyn, New York, USA

Md Omar Obaid 
Department of Business Analytics, California State Polytechnic University Pomona, CA, USA

Sadia Akter 
Department of Business Administration, International American University, USA

Mousumi Ahmed 
Masters in Public Administration, University of Dhaka, Dhaka, Bangladesh.

ABSTRACT

In  the  evolving  landscape  of  financial  technology,  credit  scoring  systems  must  adapt  to  increasingly  complex  data 
environments to ensure accurate and fair lending decisions. Traditional credit models rely heavily on structured data such 
as income, credit history, and debt ratios, but often fall short in assessing borrowers with limited credit footprints or non-
traditional financial behaviors. This study proposes a hybrid deep neural network (DNN) model that integrates structured 
financial indicators with unstructured textual data—including customer service interactions, financial news,  and social 
media sentiment—to enhance  credit  risk prediction. We collected and preprocessed a multimodal dataset  comprising 
over 100,000 loan profiles, developed a bi-directional LSTM architecture for text processing, and fused it with structured 
data via a deep learning framework. Our model was evaluated against benchmark algorithms including logistic regression, 
random forest, XGBoost, and single-input DNNs. Experimental results show that the hybrid DNN significantly outperforms 
traditional models, achieving an accuracy of 87% and an AUC-ROC of 0.91. These findings underscore the potential of 
multimodal  deep  learning  in  transforming  credit  scoring  systems,  improving  model  precision,  and  expanding  financial 
inclusion.  The  proposed  model  offers  a  scalable  and  robust  framework  for  future  credit  evaluation  tools  in  data-rich 
financial ecosystems.

KEYWORDS

Credit scoring, deep neural networks, unstructured data, financial risk assessment, LSTM, multimodal learning, machine 
learning.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

9

---

<!-- PAGE 2 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

INTRODUCTION 
Credit scoring plays a pivotal role in the financial industry by helping lenders assess the creditworthiness of individuals 
and  businesses.  Traditionally,  credit  scoring  models  have  relied  heavily  on  structured  data  such  as  income  level, 
employment history, credit utilization, and payment history. These models, often built using statistical or classical machine 
learning  algorithms,  provide  a  quantitative  foundation  for  decision-making  in  consumer  and  commercial  lending. 
However, the increasing availability of unstructured data—including textual customer service logs, financial news, and 
social media content—presents new opportunities to enhance risk assessment models.

In recent years, financial institutions have begun exploring the integration of alternative data sources into credit scoring 
mechanisms  to  capture  more  granular  insights  about  borrower  behavior.  This  shift  is  driven  by  the  limitations  of 
conventional  models  in  evaluating  first-time  borrowers,  freelancers,  and  those  lacking  extensive  credit  history. 
Unstructured data, rich in contextual and behavioral cues, can help bridge this gap by providing a more holistic view of an 
individual's financial reliability.

The  advent  of  deep  learning,  particularly  deep  neural  networks  (DNNs),  has  revolutionized  the  ability  to  model  high-
dimensional  and  unstructured  data.  Techniques  such  as  recurrent  neural  networks  (RNNs),  long  short-term  memory 
(LSTM)  networks,  and  transformers  have  enabled  more  accurate  interpretation  of  sequential  and  textual  data.  These 
developments  have  made  it  possible  to  augment  credit  scoring  with  models  that  learn  representations  from  both 
numerical and semantic features, resulting in more comprehensive and dynamic assessments.

In this paper, we propose a hybrid deep learning approach that  combines  structured financial data with unstructured 
textual inputs to improve the performance of credit scoring models. Our goal is to evaluate whether integrating text-based 
information  into  a  deep  neural  network  architecture  can  offer  better  predictive  power  and  reliability  compared  to 
traditional and single-modality models. We benchmark our proposed model against several baseline algorithms, including 
logistic regression, random forest, and XGBoost, as well as models trained exclusively on structured or unstructured data.

Literature Review

Credit  scoring  has  historically  been  dominated  by  statistical  methods,  most  notably  logistic  regression,  due  to  their 
interpretability and ease of deployment in regulatory settings [1]. However, these models often struggle with nonlinear 
patterns and interactions among variables, prompting a transition toward more advanced techniques. Tree-based models 
such as decision trees, random forests, and gradient boosting machines (e.g., XGBoost) have gained popularity for their 
ability to handle complex feature spaces and imbalanced datasets [2].

Deep  learning methods,  though  initially  slow  to  gain traction  in  finance,  are  now  widely  recognized  for  their  superior 
performance  in  pattern  recognition  and  their  ability  to  model  both  structured  and  unstructured  data.  For  instance, 
Malekipirbazari and Aksakalli [3] employed random forest and deep learning to predict peer-to-peer (P2P) loan defaults 
and found that deep neural networks offered significant performance advantages over conventional models. Similarly, 
Xiao  et  al.  [4]  demonstrated  that  deep  learning  models  could  outperform  logistic  regression  in  predicting  credit  card

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

10

---

<!-- PAGE 3 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

defaults, especially when dealing with large-scale transactional data.

Recent  studies  have  also  explored  the  role  of  unstructured  data  in  credit  risk  modeling.  One  notable  approach  by 
Cerchiello et al. [5] used sentiment  analysis on financial news to enhance credit  scoring for firms, while Mai et  al. [6] 
showed  that  incorporating  Twitter  sentiment  could  significantly  improve  bankruptcy  prediction  models.  These  works 
suggest that unstructured data sources contain valuable signals not captured in traditional financial attributes.

The rise of hybrid models that combine structured and unstructured data has further pushed the boundaries of credit 
scoring. Bazarbash [7] from the  International Monetary Fund introduced the concept of "AI-enhanced credit  scoring," 
showing  that  machine  learning  models  integrating  both  structured  data  and  text  narratives  could  reduce  credit 
misclassification errors. Moreover, transformer-based models like BERT have shown promise in extracting context-rich 
features from financial documents and social media, allowing for better risk classification [8].

Despite  the  potential,  challenges  remain  in  aligning  structured  and  unstructured  data,  ensuring  data  quality,  and 
maintaining interpretability for regulatory compliance. Nevertheless, the growing body of evidence indicates that deep 
learning models leveraging multimodal data hold significant promise for the future of credit assessment. Our research 
builds upon these findings by presenting a hybrid deep neural network model and empirically evaluating its efficacy in a 
credit scoring context.

METHODOLOGY

In conducting this study on credit scoring using deep neural networks, our primary objective was to evaluate the feasibility 
and effectiveness of leveraging unstructured data—such as customer service interactions, financial news, and social media 
content—in conjunction with traditional structured data. Our methodology consisted of six key phases: dataset collection, 
data  preprocessing,  feature  extraction, model  development, model  validation,  and model evaluation. Each  phase  was 
designed  to  ensure  methodological  rigor  and  enable  a  comprehensive  exploration  of  deep  learning’s  potential  in 
enhancing credit risk prediction.

Dataset Collection and Dataset Details

We began by collecting datasets that incorporated both structured and unstructured data, thereby enabling a multimodal 
approach to credit scoring. Our core structured data source was the Lending Club’s publicly available loan dataset, which 
provided  essential  information  on  borrower  profiles,  loan  terms,  credit  history,  employment  status,  and  repayment 
behavior. To enrich our structured data, we integrated the “Give Me Some Credit” dataset from Kaggle, which included 
features such as monthly income, number of dependents, and credit card utilization.

To  complement  the  structured  data,  we  gathered  unstructured  data  from  two  major  sources.  First,  we  acquired 
anonymized  customer  interaction  records—including  email  transcripts,  chatbot  exchanges,  and  phone  support 
summaries—through a data-sharing agreement with a mid-sized financial institution. Second, we curated a collection of 
financial news articles from reputable outlets and used the Tweepy API to scrape sentiment-tagged social media posts

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

11

---

<!-- PAGE 4 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

related to personal finance, debt, and credit behavior.

Page No. 09-22

We ensured that all datasets were ethically sourced, anonymized, and stripped of personally identifiable information in 
compliance with data protection regulations such as GDPR and HIPAA. Below is a summary of the datasets used in our 
study:

Table 1: Dataset Details

Dataset Name

Type

Description

Source

Lending Club Loan 
Data

Structured

Borrower  credit  history, 
loan  terms, 
payment status, income, and employment

Lending  Club 
data portal)

(open

Give  Me  Some 
Credit Dataset

Structured

Additional  borrower  financial  details 
(monthly income, dependents, etc.)

Kaggle

Financial 
Institution Logs

Unstructured  Chat, email, and call summaries linked to

loan applications

Partnered 
Institution

Financial

Financial 
Articles

News

Unstructured  News  articles  related  to  credit,  lending,

and financial markets

scraping

Web 
Reuters, Bloomberg

from

Size

~80,000 
records

~15,000 
records

~10,000 
records

~5,000 
articles

Financial

Twitter 
Sentiment

Unstructured  Tweets  with  hashtags  like  #credit,  #loan, 
#debt tagged for sentiment

Tweepy  API,  Twitter 
Academic Access

~30,000 
tweets

These datasets together formed a rich, heterogeneous data environment that enabled us to analyze borrower behavior 
from both quantitative and qualitative perspectives.

Data Preprocessing

Following  collection,  we  conducted  thorough  preprocessing  to  prepare  both  structured  and  unstructured  data  for 
modeling.  For  structured  data,  we  handled  missing  values  using  mean  imputation  for  numerical  variables  and  mode 
imputation  for  categorical  fields.  We  then  normalized  all  continuous  features  using  Min-Max  scaling  to  ensure  that 
variables existed on a uniform scale, which is critical for training neural networks effectively.

For the unstructured textual data, we undertook extensive cleaning. This included the removal of HTML tags, lowercasing, 
punctuation stripping, stopword removal, and lemmatization. We also applied spell correction using TextBlob to further 
improve textual quality. To ensure privacy and compliance, we removed all identifiable information from the texts.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

12

---

<!-- PAGE 5 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

We aligned the  structured and unstructured data by linking each borrower’s structured profile  to corresponding text-
based data through unique identifiers and timestamps. This created a coherent and unified dataset where both forms of 
information were associated at the individual level.

Feature Extraction

For structured data, we selected key financial indicators such as annual income, credit utilization, loan purpose, number 
of credit lines, and past delinquencies. These features were fed directly into a structured-input branch of our deep learning 
model.

For unstructured data, we utilized natural language processing techniques to transform raw text into numerical vectors. 
Initially,  we  employed  pre-trained  GloVe  embeddings  to  convert  text  into  dense  vector  representations  that  capture 
semantic meaning. Each document was tokenized and padded to a uniform length of 200 tokens. We also experimented 
with contextual embeddings using BERT to evaluate whether transformer-based representations improved performance 
over static embeddings.

After  extracting  features  from  both  data  types,  we  concatenated  the  structured  numerical  vectors  with  the  text 
embeddings to create a unified input matrix. This allowed the model to simultaneously learn from financial metrics and 
qualitative text-based signals.

Model Development

To model credit risk using this multimodal data, we developed a deep neural network with two distinct input streams: one 
for structured data and another for unstructured text. We implemented the model using TensorFlow and Keras.

The structured data branch was a feedforward neural network composed of three dense layers with ReLU activations and 
dropout layers (set to 0.3) to prevent overfitting. For unstructured data, we used a bidirectional LSTM (Bi-LSTM) network. 
The LSTM branch began with an embedding layer initialized with GloVe vectors, followed by a Bi-LSTM layer with 128 units 
and a global max-pooling layer.

We merged the outputs from both branches and passed them through two fully connected layers with 128 and 64 neurons, 
respectively, applying ReLU activations. Finally, we added a sigmoid-activated output node to predict the probability of 
loan default. We trained the model using binary cross-entropy as the loss function and the Adam optimizer with a learning 
rate of 0.001. We trained the model for 20 epochs with early stopping to prevent overfitting.

Model Validation

To validate our model, we employed stratified 5-fold cross-validation. This approach ensured that each fold maintained 
the  same  proportion  of  defaulters  and  non-defaulters  as  the  overall  dataset,  thereby  reducing  the  risk  of  biased 
evaluation.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

13

---

<!-- PAGE 6 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

In each fold, we split the data into 80% training and 20% testing sets. We initialized weights at the start of each fold and 
tracked  performance  using  validation  loss  and  accuracy.  We  also  conducted  grid  search  for  hyperparameter  tuning, 
adjusting parameters such as dropout rates, number of LSTM units, batch size, and learning rate.

We tested alternative architectures including GRUs, CNN-LSTM hybrids, and transformer-based models such as BERT with 
dense networks. However, the Bi-LSTM model with structured data fusion offered the best balance between performance 
and computational efficiency.

Model Evaluation

We evaluated our model using standard metrics for binary classification in credit scoring: Accuracy, Precision, Recall, F1-
Score, and AUC-ROC (Area Under the Receiver Operating Characteristic Curve). These metrics were averaged across all 
five folds to ensure robust and generalized performance evaluation.

Our model achieved an average accuracy of 87%, with a precision of 82%, recall of 85%, and an F1-score of 83.5%. The 
AUC-ROC consistently exceeded 0.90, indicating strong discriminatory ability between good and bad credit risks. We also 
examined confusion matrices to assess misclassification patterns and identified that most false negatives were borderline 
risk borrowers.

To further interpret our model, we used SHAP (SHapley Additive exPlanations) to understand which features—whether 
numerical or semantic—had the greatest influence on predictions. SHAP values showed that both credit utilization and 
sentiment-laden text, such as borrower concerns or late payment justifications, were key predictors.

Finally, we benchmarked our DNN model against traditional algorithms including logistic regression, random forest, and 
XGBoost.  While  XGBoost  performed  well  with  structured  data  alone,  our  multimodal  DNN  model  outperformed  it  in 
overall prediction accuracy and interpretability when unstructured data were included.

RESULTS

To  evaluate  the  effectiveness  of  our  proposed  hybrid  deep  neural  network  model  for  credit  scoring,  we  conducted  a 
comprehensive experimental analysis using a combination of structured and unstructured data. We compared our model’s 
performance against a range of established machine learning and deep learning techniques. The evaluation was carried 
out using five key classification metrics: accuracy, precision, recall, F1-score, and the area under the Receiver Operating 
Characteristic curve (AUC-ROC). These metrics provided a holistic view of each model’s predictive capability, particularly 
in distinguishing high-risk borrowers from those likely to repay.

We tested six models in total: logistic regression, random forest, XGBoost, Bi-LSTM using only unstructured text data, a 
deep neural network using only structured numerical data, and our proposed hybrid model combining both structured 
and  unstructured  inputs.  Each  model  was  trained  and  evaluated  using  a  stratified  5-fold  cross-validation  approach  to 
ensure robustness and generalizability of the results.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

14

---

<!-- PAGE 7 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

The performance of all models is summarized in the following table:

Table 2: Model Performance Summary

Model

Accuracy

Precision

Recall

F1-Score

AUC-ROC

Logistic Regression

Random Forest

XGBoost

0.76

0.82

0.85

Bi-LSTM (Text Only)

0.83

DNN (Structured Only)

0.84

Hybrid  DNN  (Structured 
+ Text)

0.87

0.72

0.80

0.83

0.81

0.82

0.82

0.74

0.81

0.84

0.84

0.83

0.85

0.73

0.80

0.83

0.82

0.82

0.78

0.86

0.89

0.88

0.89

0.835

0.91

From this table, it is evident that traditional statistical models such as logistic regression yielded modest performance, 
achieving an accuracy of 76% and an AUC-ROC of 0.78. While logistic regression offers interpretability and simplicity, it 
lacked the flexibility to capture complex, nonlinear relationships present in the data. The random forest model performed 
noticeably better with an accuracy of 82% and an AUC-ROC of 0.86, benefiting from its ensemble learning framework and 
ability to model feature interactions.

XGBoost emerged as one of the strongest performers among the classic machine learning models, reaching an accuracy 
of  85%  and  an  AUC-ROC  of  0.89.  It  outperformed  logistic  regression  and  random  forest  across  all  metrics  due  to  its 
capability to handle class imbalance and penalize misclassifications effectively during training. However, while XGBoost 
achieved  strong  predictive  scores  using  structured  data,  it  was  inherently  limited  in  leveraging  semantic  information 
embedded in unstructured text.

The  Bi-LSTM  model,  which  was  trained  solely  on  unstructured  text  data  such  as  customer  service  logs  and  financial 
sentiment  from  news  and  social  media,  achieved  an  accuracy  of  83%,  a  recall  of  84%,  and  an  AUC-ROC  of  0.88.  This 
performance  validated  our  hypothesis  that  textual  behavioral  signals  contain  critical  predictive 
insights  for 
creditworthiness. Nevertheless, its lack of structured numerical inputs constrained its holistic view of a borrower’s risk 
profile.

Our deep neural network trained exclusively on structured data showed a slightly improved performance over Bi-LSTM, 
with  an  accuracy  of  84%  and  AUC-ROC  of  0.89.  However,  its  lack  of  contextual,  behavioral  data  from  text  made  it 
susceptible to missing nuanced indicators of risk that are not easily quantifiable.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

15

---

<!-- PAGE 8 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

The most notable result came from our proposed Hybrid Deep Neural Network, which fused both structured features and 
unstructured text data into a unified model. This architecture achieved the highest scores across all evaluation metrics, 
including an accuracy of 87%, precision of 82%, recall of 85%, F1-score of 83.5%, and an AUC-ROC of 0.91. These outcomes 
clearly demonstrate the advantage of multimodal input in credit scoring, particularly in improving the recall rate, which is 
vital in correctly identifying high-risk borrowers and preventing potential defaults.

The visualization below illustrates a comparative analysis of all tested models across the five-performance metrics. The 
hybrid  model’s  dominance  is  visually  evident,  with  consistently  higher  scores  across  every  metric  compared  to  the 
alternatives.

Chart 1: comparative analysis of all tested models across the five-performance metrics

This chart highlights how models leveraging unstructured data (Bi-LSTM) or combining it with structured inputs (Hybrid 
DNN) significantly outperform traditional models that rely solely on tabular financial variables. The hybrid model’s ability 
to  synthesize  numerical  trends  with  textual  cues—such  as  borrower  sentiment,  financial  concerns,  or  behavioral 
inconsistencies—enhances its ability to generalize across different borrower profiles and loan scenarios.

From  an  industry  standpoint,  the  implications of  these  results  are  substantial. While models  like  XGBoost  are  already 
widely used in fintech platforms due to their interpretability and efficiency, they lack the capacity to incorporate real-time 
behavioral and sentiment data. Our hybrid DNN, although computationally more demanding, reflects a growing shift in 
industry toward data fusion techniques that provide deeper and more accurate risk assessments. Institutions adopting 
such  models  can  benefit  from  reduced  default  rates,  more  personalized  lending  decisions,  and  enhanced  credit

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

16

---

<!-- PAGE 9 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

accessibility for previously under-evaluated segments of the population.

In conclusion, the  results of our study underscore the  critical role that deep neural networks—and particularly hybrid 
architectures combining multiple data modalities—can play in redefining credit scoring practices. By capturing both the 
quantitative  and  qualitative  dimensions  of  borrower  behavior,  these  models  offer  a  powerful,  scalable,  and  adaptive 
framework that aligns closely with the data-rich, real-time decision environments of modern financial services.

CONCLUSION

This study explored the integration of structured and unstructured data using a hybrid deep neural network approach to 
enhance credit scoring models. Traditional credit scoring systems have long depended on structured financial indicators 
such as income, debt-to-income ratio, and repayment history. While effective in many cases, such models often fall short 
in  evaluating  borrowers  with  limited  credit  histories  or  those  whose  financial  behavior  is  not  fully  captured  through 
conventional  metrics.  Our  research  addressed  this  limitation  by  incorporating  unstructured  data  sources—such  as 
customer service transcripts, financial news articles, and social media sentiment—into a deep learning framework.

Through  extensive  experimentation  and comparative  analysis,  we  demonstrated  that  the  hybrid  deep  neural  network 
model  significantly outperformed  traditional  models  like  logistic  regression,  random  forest,  and even  high-performing 
algorithms  like  XGBoost.  The  hybrid  model  achieved  superior  scores  across  all  major  evaluation  metrics,  including  an 
accuracy of 87% and an AUC-ROC of 0.91, affirming its robustness in capturing both numerical and contextual risk signals.

Importantly, the inclusion of unstructured textual data provided valuable behavioral and sentiment-related insights that 
traditional credit features could not capture alone. This multimodal data fusion approach offers financial institutions a 
more holistic and adaptive tool for credit assessment, particularly in environments where traditional data is sparse or 
insufficient. Moreover, as more customer interactions and financial decisions are digitally recorded, the use of text-based 
analytics in credit scoring will likely become not just beneficial but essential.

Our findings suggest that the future of credit risk modeling lies in the ability to synthesize heterogeneous data sources 
through advanced deep learning architectures. By combining structured financial attributes with unstructured narratives, 
financial  institutions  can  develop  more  accurate,  inclusive,  and  responsive  credit  evaluation  systems.  This  not  only 
improves lending decisions but also supports financial inclusion by enabling access to credit for individuals traditionally 
overlooked by conventional scoring systems.

Moving  forward,  further  research  could  explore  the  interpretability  of  deep  learning  models  in  compliance-focused 
financial  environments,  as  well  as  real-time  deployment  of  such  systems  in  credit  decision  engines.  The  potential 
integration of transformer-based models such as BERT or GPT for dynamic credit risk monitoring also presents a promising 
avenue for future exploration.

Acknowledgement: All the author contributed equally.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

17

---

<!-- PAGE 10 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

REFERENCE

Page No. 09-22

[1]  Hand, D. J., & Henley, W. E. (1997). Statistical classification methods in consumer credit scoring: a review. 
in  Society),  160(3),  523–541.

the  Royal  Statistical  Society:  Series  A

(Statistics

Journal  of 
https://doi.org/10.1111/j.1467-985X.1997.00078.x

[2]  Brown, I., & Mues, C. (2012). An experimental comparison of classification algorithms for imbalanced credit 
3446–3453.

Applications,

Systems

Expert

39(3),

sets.

data

with

scoring 
https://doi.org/10.1016/j.eswa.2011.09.033

[3]  Malekipirbazari,  M.,  &  Aksakalli,  V.  (2015).  Risk  assessment  in  social  lending  via  random  forests.  Expert

Systems with Applications, 42(10), 4621–4631. https://doi.org/10.1016/j.eswa.2015.01.002

[4]  Xiao,  L.,  Hu,  X.,  Yu,  F.  R.,  Xie,  R.,  &  Liu,  Y.  (2020).  Deep  learning  for  the  prediction  of  loan  default:  A 
Innovation,  6(1),  1–22.

learning  approaches.  Financial

traditional  machine

comparison  with 
https://doi.org/10.1186/s40854-020-00191-2

[5]  Cerchiello, P., Nicola, G., & Giudici, P. (2017). Big data analytics for bank customer profiling. Journal of Risk

and Financial Management, 10(1), 6. https://doi.org/10.3390/jrfm10010006

[6]  Mai, F., Shan, Z., Bai, Q., Wang, X. S., & Chiang, R. H. L. (2018). How does social media impact bankruptcy 
555–578.

Quarterly,

Twitter.

42(2),

from

MIS

prediction? 
Evidence 
https://doi.org/10.25300/MISQ/2018/14418

[7]  Bazarbash, M. (2019). FinTech in Financial Inclusion: Machine Learning Applications in Assessing Credit Risk 
Fund.

(IMF 
https://www.imf.org/en/Publications/WP/Issues/2019/06/27/FinTech-in-Financial-Inclusion-Machine-
Learning-Applications-in-Assessing-Credit-Risk-46988

International

Monetary

19/109).

Working

Paper

No.

[8]  Huang, B., & Paul, M. J. (2020). Extracting actionable information from financial documents using BERT. In 
Proceedings of the First Workshop on Financial Technology and Natural Language Processing (pp. 29–34). 
https://doi.org/10.18653/v1/2020.financialnlp-1.4

[9]  Hossain, M. N., Hossain, S., Nath, A., Nath, P. C., Ayub, M. I., Hassan, M. M., ... & Rasel, M. (2024). ENHANCED BANKING 
FRAUD  DETECTION:  A  COMPARATIVE  ANALYSIS  OF  SUPERVISED  MACHINE  LEARNING  ALGORITHMS. American 
Research Index Library, 23-35.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

18

---

<!-- PAGE 11 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

[10]  Uddin, A., Pabel, M. A. H., Alam, M. I., KAMRUZZAMAN, F., Haque, M. S. U., Hosen, M. M., ... & Ghosh, S. K. (2025). 
Advancing  Financial  Risk  Prediction  and  Portfolio  Optimization  Using  Machine  Learning  Techniques. The  American 
Journal of Management and Economics Innovations, 7(01), 5-20.

[11]  Nguyen, Q. G., Nguyen, L. H., Hosen, M. M., Rasel, M., Shorna, J. F., Mia, M. S., & Khan, S. I. (2025). Enhancing Credit 
Risk Management with Machine Learning: A Comparative Study of Predictive Models for Credit Default Prediction. The 
American Journal of Applied sciences, 7(01), 21-30.

[12]  Bhattacharjee, B., Mou, S. N., Hossain, M. S., Rahman, M. K., Hassan, M. M., Rahman, N., ... & Haque, M. S. U. (2024). 
MACHINE  LEARNING  FOR  COST  ESTIMATION  AND  FORECASTING  IN  BANKING:  A  COMPARATIVE  ANALYSIS  OF 
ALGORITHMS. Frontline Marketing,Management and Economics Journal, 4(12), 66-83.

[13]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S. S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative 
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep 
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[14]  Nath, F., Chowdhury, M. O. S., & Rhaman, M. M. (2023). Navigating produced water sustainability in the oil and gas 
sector: A Critical review of reuse challenges, treatment technologies, and prospects ahead. Water, 15(23), 4088.

[15]  PHAN,  H.  T.  N.,  &  AKTER,  A.  (2024).  HYBRID MACHINE  LEARNING  APPROACH FOR  ORAL  CANCER  DIAGNOSIS  AND

CLASSIFICATION USING HISTOPATHOLOGICAL IMAGES. Universal Publication Index e-Library, 63-76.

[16]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S. S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative 
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep 
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[17]  Nath, F., Asish, S., Debi, H. R., Chowdhury, M. O. S., Zamora, Z. J., & Muñoz, S. (2023, August). Predicting hydrocarbon 
production  behavior  in  heterogeneous  reservoir  utilizing  deep  learning  models.  In Unconventional  Resources 
Technology Conference, 13–15 June 2023 (pp. 506-521). Unconventional Resources Technology Conference (URTeC).

[18]  Ahmmed,  M.  J.,  Rahman,  M.  M.,  Das,  A.  C.,  Das,  P.,  Pervin,  T.,  Afrin,  S.,  ...  &  Rahman,  N.  (2024).  COMPARATIVE 
ANALYSIS  OF  MACHINE  LEARNING  ALGORITHMS  FOR  BANKING  FRAUD  DETECTION:  A  STUDY  ON  PERFORMANCE, 
PRECISION, AND REAL-TIME APPLICATION. American Research Index Library, 31-44.

[19]  Akhi, S. S., Shakil, F., Dey, S. K., Tusher, M. I., Kamruzzaman, F., Jamee, S. S., ... & Rahman, N. (2025). Enhancing Banking 
Cybersecurity: An Ensemble-Based Predictive Machine Learning Approach. The American Journal of Engineering and 
Technology, 7(03), 88-97.

[20]  Pabel, M. A. H., Bhattacharjee, B., Dey, S. K., Jamee, S. S., Obaid, M. O., Mia, M. S., ... & Sharif, M. K. (2025). BUSINESS 
ANALYTICS  FOR  CUSTOMER  SEGMENTATION:  A  COMPARATIVE  STUDY  OF  MACHINE  LEARNING  ALGORITHMS  IN 
PERSONALIZED BANKING SERVICES. American Research Index Library, 1-13.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

19

---

<!-- PAGE 12 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

[21]  Siddique, M. T., Jamee, S. S., Sajal, A., Mou, S. N., Mahin, M. R. H., Obaid, M. O., ... & Hasan, M. (2025). Enhancing 
Automated Trading with Sentiment  Analysis: Leveraging Large Language Models for Stock Market Predictions. The 
American Journal of Engineering and Technology, 7(03), 185-195.

[22]  Mohammad Iftekhar Ayub, Biswanath Bhattacharjee, Pinky Akter, Mohammad Nasir Uddin, Arun Kumar Gharami, Md 
Iftakhayrul Islam, Shaidul Islam Suhan, Md Sayem Khan, & Lisa Chambugong. (2025). Deep Learning for Real-Time 
Fraud  Detection:  Enhancing  Credit  Card  Security  in  Banking  Systems. The  American  Journal  of  Engineering  and 
Technology, 7(04), 141–150. https://doi.org/10.37547/tajet/Volume07Issue04-19

[23]  Nguyen, A. T. P., Jewel, R. M., & Akter, A. (2025). Comparative Analysis of Machine Learning Models for Automated 
Skin  Cancer  Detection:  Advancements  in Diagnostic Accuracy  and  AI  Integration. The  American  Journal  of  Medical 
Sciences and Pharmaceutical Research, 7(01), 15-26.

[24]  Nguyen, A. T. P., Shak, M. S., & Al-Imran, M. (2024). ADVANCING EARLY SKIN CANCER DETECTION: A COMPARATIVE 
ANALYSIS  OF  MACHINE  LEARNING  ALGORITHMS  FOR  MELANOMA  DIAGNOSIS  USING  DERMOSCOPIC 
IMAGES. International Journal of Medical Science and Public Health Research, 5(12), 119-133.

[25]  Phan, H. T. N., & Akter, A. (2025). Predicting the Effectiveness of Laser Therapy in Periodontal Diseases Using Machine

Learning Models. The American Journal of Medical Sciences and Pharmaceutical Research, 7(01), 27-37.

[26]  Phan, H. T. N. (2024). EARLY DETECTION OF ORAL DISEASES USING MACHINE LEARNING: A COMPARATIVE STUDY OF 
PREDICTIVE  MODELS  AND  DIAGNOSTIC  ACCURACY. International  Journal  of  Medical  Science  and  Public  Health 
Research, 5(12), 107-118.

[27]  Al Mamun, A., Nath, A., Dey, S. K., Nath, P. C., Rahman, M. M., Shorna, J. F., & Anjum, N. (2025). Real-Time Malware 
Detection in Cloud Infrastructures Using Convolutional Neural Networks: A Deep Learning Framework for Enhanced 
Cybersecurity. The American Journal of Engineering and Technology, 7(03), 252-261.

[28]  Akhi, S. S., Shakil, F., Dey, S. K., Tusher, M. I., Kamruzzaman, F., Jamee, S. S., ... & Rahman, N. (2025). Enhancing Banking 
Cybersecurity: An Ensemble-Based Predictive Machine Learning Approach. The American Journal of Engineering and 
Technology, 7(03), 88-97.

[29]  Mazharul  Islam  Tusher,  “Deep  Learning  Meets  Early  Diagnosis:  A  Hybrid  CNN-DNN  Framework  for  Lung  Cancer

Prediction and Clinical Translation”, ijmsphr, vol. 6, no. 05, pp. 63–72, May 2025.

[30]  Integrating Consumer Sentiment and Deep Learning for GDP Forecasting: A Novel Approach in Financial Industry”., Int

Bus &amp; Eco Adv Jou, vol. 6, no. 05, pp. 90–101, May 2025, doi: 10.55640/business/volume06issue05-05.

[31]  Tamanna Pervin, Sharmin Akter, Sadia Afrin, Md Refat Hossain, MD Sajedul Karim Chy, Sadia Akter, Md Minzamul 
Hasan,  Md  Mafuzur  Rahman,  &  Chowdhury  Amin  Abdullah.  (2025).  A  Hybrid  CNN-LSTM  Approach  for  Detecting

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

20

---

<!-- PAGE 13 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

Anomalous Bank Transactions: Enhancing Financial Fraud Detection Accuracy. The American Journal of Management 
and Economics Innovations, 7(04), 116–123. https://doi.org/10.37547/tajmei/Volume07Issue04-15

[32]  Mohammad Iftekhar Ayub, Biswanath Bhattacharjee, Pinky Akter, Mohammad Nasir Uddin, Arun Kumar Gharami, Md 
Iftakhayrul Islam, Shaidul Islam Suhan, Md Sayem Khan, & Lisa Chambugong. (2025). Deep Learning for Real-Time 
Fraud  Detection:  Enhancing  Credit  Card  Security  in  Banking  Systems. The  American  Journal  of  Engineering  and 
Technology, 7(04), 141–150. https://doi.org/10.37547/tajet/Volume07Issue04-19

[33]  Mazharul Islam Tusher, Han Thi Ngoc Phan, Arjina Akter, Md Rayhan Hassan Mahin, & Estak Ahmed. (2025). A Machine 
Learning Ensemble Approach for Early Detection of Oral Cancer: Integrating Clinical Data and Imaging Analysis in the 
Public  Health. International 
Journal  of  Medical  Science  and  Public  Health  Research, 6(04),  07–15. 
https://doi.org/10.37547/ijmsphr/Volume06Issue04-02

[34]  Safayet Hossain, Ashadujjaman Sajal, Sakib Salam Jamee, Sanjida Akter Tisha, Md Tarake Siddique, Md Omar Obaid, 
MD Sajedul Karim Chy, & Md Sayem Ul Haque. (2025). Comparative Analysis of Machine Learning Models for Credit 
in  Banking  Systems. The  American  Journal  of  Engineering  and  Technology, 7(04),  22–33. 
Risk  Prediction 
https://doi.org/10.37547/tajet/Volume07Issue04-04

[35]  Ayub, M. I., Bhattacharjee, B., Akter, P., Uddin, M. N., Gharami, A. K., Islam, M. I., ... & Chambugong, L. (2025). Deep 
Learning for Real-Time Fraud Detection: Enhancing Credit Card Security in Banking Systems. The American Journal of 
Engineering and Technology, 7(04), 141-150.

[36]  Siddique, M. T., Uddin, M. J., Chambugong, L., Nijhum, A. M., Uddin, M. N., Shahid, R., ... & Ahmed, M. (2025). AI-
Powered  Sentiment  Analytics  in  Banking:  A  BERT  and  LSTM  Perspective. International  Interdisciplinary  Business 
Economics Advancement Journal, 6(05), 135-147.

[37]  Thakur, K., Sayed, M. A., Tisha, S. A., Alam, M. K., Hasan, M. T., Shorna, J. F., ... & Ayon, E. H. (2025). Multimodal 
Deepfake  Detection  Using  Transformer-Based  Large  Language  Models:  A  Path  Toward  Secure  Media  and  Clinical 
Integrity. The American Journal of Engineering and Technology, 7(05), 169-177.

[38]  Al Mamun, A., Nath, A., Dey, S. K., Nath, P. C., Rahman, M. M., Shorna, J. F., & Anjum, N. (2025). Real-Time Malware 
Detection in Cloud Infrastructures Using Convolutional Neural Networks: A Deep Learning Framework for Enhanced 
Cybersecurity. The American Journal of Engineering and Technology, 7(03), 252-261.

[39]  Tusher, M. I., Hasan, M. M., Akter, S., Haider, M., Chy, M. S. K., Akhi, S. S., ... & Shaima, M. (2025). Deep Learning 
for  Lung  Cancer  Prediction  and  Clinical

Meets  Early  Diagnosis:  A  Hybrid  CNN-DNN  Framework 
Translation. International Journal of Medical Science and Public Health Research, 6(05), 63-72.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

21

---

<!-- PAGE 14 -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL 
eISSN: 2375-9615 pISSN: 2375-9607 
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07 
Published 11-07-2025

Page No. 09-22

[40]  Sajal, A., Chy, M. S. K., Jamee, S. S., Uddin, M. N., Khan, M. S., Gharami, A. K., ... & Ahmed, M. (2025). Forecasting Bank 
Profitability  Using  Deep  Learning  and  Macroeconomic  Indicators:  A  Comparative  Model  Study. International 
Interdisciplinary Business Economics Advancement Journal, 6(06), 08-20.

[41]  Paresh Chandra Nath, Md Sajedul Karim Chy, Md Refat Hossain, Md Rashel Miah, Sakib Salam Jamee, Mohammad 
Kawsur Sharif, Md Shakhaowat Hossain, & Mousumi Ahmed. (2025). Comparative Performance of Large Language 
Models  for  Sentiment  Analysis  of  Consumer  Feedback  in  the  Banking  Sector:  Accuracy,  Efficiency,  and  Practical 
Deployment. Frontline 
07–19. 
https://doi.org/10.37547/marketing-fmmej-05-06-02

Journal, 5(06),

Management

Marketing,

Economics

and

[42]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S.  S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative 
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep 
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[43]  Jamee, S. S., Sajal, A., Obaid, M. O., Uddin, M. N., Haque, M. S. U., Gharami, A. K., ... & FARHAN, M. (2025). Integrating 
Consumer Sentiment and Deep Learning for GDP Forecasting: A Novel Approach in Financial Industry. International 
Interdisciplinary Business Economics Advancement Journal, 6(05), 90-101.

[44]  Hossain, S., Sajal, A., Jamee, S. S., Tisha, S. A., Siddique, M. T., Obaid, M. O., ... & Haque, M. S. U. (2025). Comparative 
Analysis  of  Machine  Learning  Models  for  Credit  Risk  Prediction  in  Banking  Systems. The  American  Journal  of 
Engineering and Technology, 7(04), 22-33.

[45]  Pabel,  M.  A.  H.,  Bhattacharjee,  B.,  Dey,  S.  K.,  Jamee,  S.  S.,  Obaid,  M.  O.,  Mia,  M.  S.,  ...  &  Sharif,  M.  K.  BUSINESS 
ANALYTICS  FOR  CUSTOMER  SEGMENTATION:  A  COMPARATIVE  STUDY  OF  MACHINE  LEARNING  ALGORITHMS  IN 
PERSONALIZED BANKING SERVICES.

INTERNATIONAL INTERDISCIPLINARY BUSINESS 
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

22

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

Enhancing Credit Scoring with Multimodal Deep Learning: A Hybrid Neural
Network Approach Using Structured and Unstructured Financial Data

Md Refat Hossain
Master of Business Administration (MBA), College of Business, Westcliff University, USA

Md Amran Hossen Pabel
Masters of Science in Business Analytics Wright State University, Ohio, USA

Md Sayem Ul Haque
MBA in Business Analytics, Gannon University, USA

Md Sayem Khan
Master of Science in Project Management, Saint Francis College (SFC), Brooklyn, New York, USA

Md Omar Obaid
Department of Business Analytics, California State Polytechnic University Pomona, CA, USA

Sadia Akter
Department of Business Administration, International American University, USA

Mousumi Ahmed
Masters in Public Administration, University of Dhaka, Dhaka, Bangladesh.

ABSTRACT

In  the  evolving  landscape  of  financial  technology,  credit  scoring  systems  must  adapt  to  increasingly  complex  data
environments to ensure accurate and fair lending decisions. Traditional credit models rely heavily on structured data such
as income, credit history, and debt ratios, but often fall short in assessing borrowers with limited credit footprints or non-
traditional financial behaviors. This study proposes a hybrid deep neural network (DNN) model that integrates structured
financial indicators with unstructured textual data—including customer service interactions, financial news,  and social
media sentiment—to enhance  credit  risk prediction. We collected and preprocessed a multimodal dataset  comprising
over 100,000 loan profiles, developed a bi-directional LSTM architecture for text processing, and fused it with structured
data via a deep learning framework. Our model was evaluated against benchmark algorithms including logistic regression,
random forest, XGBoost, and single-input DNNs. Experimental results show that the hybrid DNN significantly outperforms
traditional models, achieving an accuracy of 87% and an AUC-ROC of 0.91. These findings underscore the potential of
multimodal  deep  learning  in  transforming  credit  scoring  systems,  improving  model  precision,  and  expanding  financial
inclusion.  The  proposed  model  offers  a  scalable  and  robust  framework  for  future  credit  evaluation  tools  in  data-rich
financial ecosystems.

KEYWORDS

Credit scoring, deep neural networks, unstructured data, financial risk assessment, LSTM, multimodal learning, machine
learning.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

9

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

INTRODUCTION
Credit scoring plays a pivotal role in the financial industry by helping lenders assess the creditworthiness of individuals
and  businesses.  Traditionally,  credit  scoring  models  have  relied  heavily  on  structured  data  such  as  income  level,
employment history, credit utilization, and payment history. These models, often built using statistical or classical machine
learning  algorithms,  provide  a  quantitative  foundation  for  decision-making  in  consumer  and  commercial  lending.
However, the increasing availability of unstructured data—including textual customer service logs, financial news, and
social media content—presents new opportunities to enhance risk assessment models.

In recent years, financial institutions have begun exploring the integration of alternative data sources into credit scoring
mechanisms  to  capture  more  granular  insights  about  borrower  behavior.  This  shift  is  driven  by  the  limitations  of
conventional  models  in  evaluating  first-time  borrowers,  freelancers,  and  those  lacking  extensive  credit  history.
Unstructured data, rich in contextual and behavioral cues, can help bridge this gap by providing a more holistic view of an
individual's financial reliability.

The  advent  of  deep  learning,  particularly  deep  neural  networks  (DNNs),  has  revolutionized  the  ability  to  model  high-
dimensional  and  unstructured  data.  Techniques  such  as  recurrent  neural  networks  (RNNs),  long  short-term  memory
(LSTM)  networks,  and  transformers  have  enabled  more  accurate  interpretation  of  sequential  and  textual  data.  These
developments  have  made  it  possible  to  augment  credit  scoring  with  models  that  learn  representations  from  both
numerical and semantic features, resulting in more comprehensive and dynamic assessments.

In this paper, we propose a hybrid deep learning approach that  combines  structured financial data with unstructured
textual inputs to improve the performance of credit scoring models. Our goal is to evaluate whether integrating text-based
information  into  a  deep  neural  network  architecture  can  offer  better  predictive  power  and  reliability  compared  to
traditional and single-modality models. We benchmark our proposed model against several baseline algorithms, including
logistic regression, random forest, and XGBoost, as well as models trained exclusively on structured or unstructured data.

Literature Review

Credit  scoring  has  historically  been  dominated  by  statistical  methods,  most  notably  logistic  regression,  due  to  their
interpretability and ease of deployment in regulatory settings [1]. However, these models often struggle with nonlinear
patterns and interactions among variables, prompting a transition toward more advanced techniques. Tree-based models
such as decision trees, random forests, and gradient boosting machines (e.g., XGBoost) have gained popularity for their
ability to handle complex feature spaces and imbalanced datasets [2].

Deep  learning methods,  though  initially  slow  to  gain traction  in  finance,  are  now  widely  recognized  for  their  superior
performance  in  pattern  recognition  and  their  ability  to  model  both  structured  and  unstructured  data.  For  instance,
Malekipirbazari and Aksakalli [3] employed random forest and deep learning to predict peer-to-peer (P2P) loan defaults
and found that deep neural networks offered significant performance advantages over conventional models. Similarly,
Xiao  et  al.  [4]  demonstrated  that  deep  learning  models  could  outperform  logistic  regression  in  predicting  credit  card

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

10

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

defaults, especially when dealing with large-scale transactional data.

Recent  studies  have  also  explored  the  role  of  unstructured  data  in  credit  risk  modeling.  One  notable  approach  by
Cerchiello et al. [5] used sentiment  analysis on financial news to enhance credit  scoring for firms, while Mai et  al. [6]
showed  that  incorporating  Twitter  sentiment  could  significantly  improve  bankruptcy  prediction  models.  These  works
suggest that unstructured data sources contain valuable signals not captured in traditional financial attributes.

The rise of hybrid models that combine structured and unstructured data has further pushed the boundaries of credit
scoring. Bazarbash [7] from the  International Monetary Fund introduced the concept of "AI-enhanced credit  scoring,"
showing  that  machine  learning  models  integrating  both  structured  data  and  text  narratives  could  reduce  credit
misclassification errors. Moreover, transformer-based models like BERT have shown promise in extracting context-rich
features from financial documents and social media, allowing for better risk classification [8].

Despite  the  potential,  challenges  remain  in  aligning  structured  and  unstructured  data,  ensuring  data  quality,  and
maintaining interpretability for regulatory compliance. Nevertheless, the growing body of evidence indicates that deep
learning models leveraging multimodal data hold significant promise for the future of credit assessment. Our research
builds upon these findings by presenting a hybrid deep neural network model and empirically evaluating its efficacy in a
credit scoring context.

METHODOLOGY

In conducting this study on credit scoring using deep neural networks, our primary objective was to evaluate the feasibility
and effectiveness of leveraging unstructured data—such as customer service interactions, financial news, and social media
content—in conjunction with traditional structured data. Our methodology consisted of six key phases: dataset collection,
data  preprocessing,  feature  extraction, model  development, model  validation,  and model evaluation. Each  phase  was
designed  to  ensure  methodological  rigor  and  enable  a  comprehensive  exploration  of  deep  learning’s  potential  in
enhancing credit risk prediction.

Dataset Collection and Dataset Details

We began by collecting datasets that incorporated both structured and unstructured data, thereby enabling a multimodal
approach to credit scoring. Our core structured data source was the Lending Club’s publicly available loan dataset, which
provided  essential  information  on  borrower  profiles,  loan  terms,  credit  history,  employment  status,  and  repayment
behavior. To enrich our structured data, we integrated the “Give Me Some Credit” dataset from Kaggle, which included
features such as monthly income, number of dependents, and credit card utilization.

To  complement  the  structured  data,  we  gathered  unstructured  data  from  two  major  sources.  First,  we  acquired
anonymized  customer  interaction  records—including  email  transcripts,  chatbot  exchanges,  and  phone  support
summaries—through a data-sharing agreement with a mid-sized financial institution. Second, we curated a collection of
financial news articles from reputable outlets and used the Tweepy API to scrape sentiment-tagged social media posts

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

11

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

related to personal finance, debt, and credit behavior.

Page No. 09-22

We ensured that all datasets were ethically sourced, anonymized, and stripped of personally identifiable information in
compliance with data protection regulations such as GDPR and HIPAA. Below is a summary of the datasets used in our
study:

Table 1: Dataset Details

Dataset Name

Type

Description

Source

Lending Club Loan
Data

Structured

Borrower  credit  history,
loan  terms,
payment status, income, and employment

Lending  Club
data portal)

(open

Give  Me  Some
Credit Dataset

Structured

Additional  borrower  financial  details
(monthly income, dependents, etc.)

Kaggle

Financial
Institution Logs

Unstructured  Chat, email, and call summaries linked to

loan applications

Partnered
Institution

Financial

Financial
Articles

News

Unstructured  News  articles  related  to  credit,  lending,

and financial markets

scraping

Web
Reuters, Bloomberg

from

Size

~80,000
records

~15,000
records

~10,000
records

~5,000
articles

Financial

Twitter
Sentiment

Unstructured  Tweets  with  hashtags  like  #credit,  #loan,
#debt tagged for sentiment

Tweepy  API,  Twitter
Academic Access

~30,000
tweets

These datasets together formed a rich, heterogeneous data environment that enabled us to analyze borrower behavior
from both quantitative and qualitative perspectives.

Data Preprocessing

Following  collection,  we  conducted  thorough  preprocessing  to  prepare  both  structured  and  unstructured  data  for
modeling.  For  structured  data,  we  handled  missing  values  using  mean  imputation  for  numerical  variables  and  mode
imputation  for  categorical  fields.  We  then  normalized  all  continuous  features  using  Min-Max  scaling  to  ensure  that
variables existed on a uniform scale, which is critical for training neural networks effectively.

For the unstructured textual data, we undertook extensive cleaning. This included the removal of HTML tags, lowercasing,
punctuation stripping, stopword removal, and lemmatization. We also applied spell correction using TextBlob to further
improve textual quality. To ensure privacy and compliance, we removed all identifiable information from the texts.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

12

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

We aligned the  structured and unstructured data by linking each borrower’s structured profile  to corresponding text-
based data through unique identifiers and timestamps. This created a coherent and unified dataset where both forms of
information were associated at the individual level.

Feature Extraction

For structured data, we selected key financial indicators such as annual income, credit utilization, loan purpose, number
of credit lines, and past delinquencies. These features were fed directly into a structured-input branch of our deep learning
model.

For unstructured data, we utilized natural language processing techniques to transform raw text into numerical vectors.
Initially,  we  employed  pre-trained  GloVe  embeddings  to  convert  text  into  dense  vector  representations  that  capture
semantic meaning. Each document was tokenized and padded to a uniform length of 200 tokens. We also experimented
with contextual embeddings using BERT to evaluate whether transformer-based representations improved performance
over static embeddings.

After  extracting  features  from  both  data  types,  we  concatenated  the  structured  numerical  vectors  with  the  text
embeddings to create a unified input matrix. This allowed the model to simultaneously learn from financial metrics and
qualitative text-based signals.

Model Development

To model credit risk using this multimodal data, we developed a deep neural network with two distinct input streams: one
for structured data and another for unstructured text. We implemented the model using TensorFlow and Keras.

The structured data branch was a feedforward neural network composed of three dense layers with ReLU activations and
dropout layers (set to 0.3) to prevent overfitting. For unstructured data, we used a bidirectional LSTM (Bi-LSTM) network.
The LSTM branch began with an embedding layer initialized with GloVe vectors, followed by a Bi-LSTM layer with 128 units
and a global max-pooling layer.

We merged the outputs from both branches and passed them through two fully connected layers with 128 and 64 neurons,
respectively, applying ReLU activations. Finally, we added a sigmoid-activated output node to predict the probability of
loan default. We trained the model using binary cross-entropy as the loss function and the Adam optimizer with a learning
rate of 0.001. We trained the model for 20 epochs with early stopping to prevent overfitting.

Model Validation

To validate our model, we employed stratified 5-fold cross-validation. This approach ensured that each fold maintained
the  same  proportion  of  defaulters  and  non-defaulters  as  the  overall  dataset,  thereby  reducing  the  risk  of  biased
evaluation.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

13

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

In each fold, we split the data into 80% training and 20% testing sets. We initialized weights at the start of each fold and
tracked  performance  using  validation  loss  and  accuracy.  We  also  conducted  grid  search  for  hyperparameter  tuning,
adjusting parameters such as dropout rates, number of LSTM units, batch size, and learning rate.

We tested alternative architectures including GRUs, CNN-LSTM hybrids, and transformer-based models such as BERT with
dense networks. However, the Bi-LSTM model with structured data fusion offered the best balance between performance
and computational efficiency.

Model Evaluation

We evaluated our model using standard metrics for binary classification in credit scoring: Accuracy, Precision, Recall, F1-
Score, and AUC-ROC (Area Under the Receiver Operating Characteristic Curve). These metrics were averaged across all
five folds to ensure robust and generalized performance evaluation.

Our model achieved an average accuracy of 87%, with a precision of 82%, recall of 85%, and an F1-score of 83.5%. The
AUC-ROC consistently exceeded 0.90, indicating strong discriminatory ability between good and bad credit risks. We also
examined confusion matrices to assess misclassification patterns and identified that most false negatives were borderline
risk borrowers.

To further interpret our model, we used SHAP (SHapley Additive exPlanations) to understand which features—whether
numerical or semantic—had the greatest influence on predictions. SHAP values showed that both credit utilization and
sentiment-laden text, such as borrower concerns or late payment justifications, were key predictors.

Finally, we benchmarked our DNN model against traditional algorithms including logistic regression, random forest, and
XGBoost.  While  XGBoost  performed  well  with  structured  data  alone,  our  multimodal  DNN  model  outperformed  it  in
overall prediction accuracy and interpretability when unstructured data were included.

RESULTS

To  evaluate  the  effectiveness  of  our  proposed  hybrid  deep  neural  network  model  for  credit  scoring,  we  conducted  a
comprehensive experimental analysis using a combination of structured and unstructured data. We compared our model’s
performance against a range of established machine learning and deep learning techniques. The evaluation was carried
out using five key classification metrics: accuracy, precision, recall, F1-score, and the area under the Receiver Operating
Characteristic curve (AUC-ROC). These metrics provided a holistic view of each model’s predictive capability, particularly
in distinguishing high-risk borrowers from those likely to repay.

We tested six models in total: logistic regression, random forest, XGBoost, Bi-LSTM using only unstructured text data, a
deep neural network using only structured numerical data, and our proposed hybrid model combining both structured
and  unstructured  inputs.  Each  model  was  trained  and  evaluated  using  a  stratified  5-fold  cross-validation  approach  to
ensure robustness and generalizability of the results.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

14

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

The performance of all models is summarized in the following table:

Table 2: Model Performance Summary

Model

Accuracy

Precision

Recall

F1-Score

AUC-ROC

Logistic Regression

Random Forest

XGBoost

0.76

0.82

0.85

Bi-LSTM (Text Only)

0.83

DNN (Structured Only)

0.84

Hybrid  DNN  (Structured
+ Text)

0.87

0.72

0.80

0.83

0.81

0.82

0.82

0.74

0.81

0.84

0.84

0.83

0.85

0.73

0.80

0.83

0.82

0.82

0.78

0.86

0.89

0.88

0.89

0.835

0.91

From this table, it is evident that traditional statistical models such as logistic regression yielded modest performance,
achieving an accuracy of 76% and an AUC-ROC of 0.78. While logistic regression offers interpretability and simplicity, it
lacked the flexibility to capture complex, nonlinear relationships present in the data. The random forest model performed
noticeably better with an accuracy of 82% and an AUC-ROC of 0.86, benefiting from its ensemble learning framework and
ability to model feature interactions.

XGBoost emerged as one of the strongest performers among the classic machine learning models, reaching an accuracy
of  85%  and  an  AUC-ROC  of  0.89.  It  outperformed  logistic  regression  and  random  forest  across  all  metrics  due  to  its
capability to handle class imbalance and penalize misclassifications effectively during training. However, while XGBoost
achieved  strong  predictive  scores  using  structured  data,  it  was  inherently  limited  in  leveraging  semantic  information
embedded in unstructured text.

The  Bi-LSTM  model,  which  was  trained  solely  on  unstructured  text  data  such  as  customer  service  logs  and  financial
sentiment  from  news  and  social  media,  achieved  an  accuracy  of  83%,  a  recall  of  84%,  and  an  AUC-ROC  of  0.88.  This
performance  validated  our  hypothesis  that  textual  behavioral  signals  contain  critical  predictive
insights  for
creditworthiness. Nevertheless, its lack of structured numerical inputs constrained its holistic view of a borrower’s risk
profile.

Our deep neural network trained exclusively on structured data showed a slightly improved performance over Bi-LSTM,
with  an  accuracy  of  84%  and  AUC-ROC  of  0.89.  However,  its  lack  of  contextual,  behavioral  data  from  text  made  it
susceptible to missing nuanced indicators of risk that are not easily quantifiable.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

15

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

The most notable result came from our proposed Hybrid Deep Neural Network, which fused both structured features and
unstructured text data into a unified model. This architecture achieved the highest scores across all evaluation metrics,
including an accuracy of 87%, precision of 82%, recall of 85%, F1-score of 83.5%, and an AUC-ROC of 0.91. These outcomes
clearly demonstrate the advantage of multimodal input in credit scoring, particularly in improving the recall rate, which is
vital in correctly identifying high-risk borrowers and preventing potential defaults.

The visualization below illustrates a comparative analysis of all tested models across the five-performance metrics. The
hybrid  model’s  dominance  is  visually  evident,  with  consistently  higher  scores  across  every  metric  compared  to  the
alternatives.

Chart 1: comparative analysis of all tested models across the five-performance metrics

This chart highlights how models leveraging unstructured data (Bi-LSTM) or combining it with structured inputs (Hybrid
DNN) significantly outperform traditional models that rely solely on tabular financial variables. The hybrid model’s ability
to  synthesize  numerical  trends  with  textual  cues—such  as  borrower  sentiment,  financial  concerns,  or  behavioral
inconsistencies—enhances its ability to generalize across different borrower profiles and loan scenarios.

From  an  industry  standpoint,  the  implications of  these  results  are  substantial. While models  like  XGBoost  are  already
widely used in fintech platforms due to their interpretability and efficiency, they lack the capacity to incorporate real-time
behavioral and sentiment data. Our hybrid DNN, although computationally more demanding, reflects a growing shift in
industry toward data fusion techniques that provide deeper and more accurate risk assessments. Institutions adopting
such  models  can  benefit  from  reduced  default  rates,  more  personalized  lending  decisions,  and  enhanced  credit

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

16

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

accessibility for previously under-evaluated segments of the population.

In conclusion, the  results of our study underscore the  critical role that deep neural networks—and particularly hybrid
architectures combining multiple data modalities—can play in redefining credit scoring practices. By capturing both the
quantitative  and  qualitative  dimensions  of  borrower  behavior,  these  models  offer  a  powerful,  scalable,  and  adaptive
framework that aligns closely with the data-rich, real-time decision environments of modern financial services.

CONCLUSION

This study explored the integration of structured and unstructured data using a hybrid deep neural network approach to
enhance credit scoring models. Traditional credit scoring systems have long depended on structured financial indicators
such as income, debt-to-income ratio, and repayment history. While effective in many cases, such models often fall short
in  evaluating  borrowers  with  limited  credit  histories  or  those  whose  financial  behavior  is  not  fully  captured  through
conventional  metrics.  Our  research  addressed  this  limitation  by  incorporating  unstructured  data  sources—such  as
customer service transcripts, financial news articles, and social media sentiment—into a deep learning framework.

Through  extensive  experimentation  and comparative  analysis,  we  demonstrated  that  the  hybrid  deep  neural  network
model  significantly outperformed  traditional  models  like  logistic  regression,  random  forest,  and even  high-performing
algorithms  like  XGBoost.  The  hybrid  model  achieved  superior  scores  across  all  major  evaluation  metrics,  including  an
accuracy of 87% and an AUC-ROC of 0.91, affirming its robustness in capturing both numerical and contextual risk signals.

Importantly, the inclusion of unstructured textual data provided valuable behavioral and sentiment-related insights that
traditional credit features could not capture alone. This multimodal data fusion approach offers financial institutions a
more holistic and adaptive tool for credit assessment, particularly in environments where traditional data is sparse or
insufficient. Moreover, as more customer interactions and financial decisions are digitally recorded, the use of text-based
analytics in credit scoring will likely become not just beneficial but essential.

Our findings suggest that the future of credit risk modeling lies in the ability to synthesize heterogeneous data sources
through advanced deep learning architectures. By combining structured financial attributes with unstructured narratives,
financial  institutions  can  develop  more  accurate,  inclusive,  and  responsive  credit  evaluation  systems.  This  not  only
improves lending decisions but also supports financial inclusion by enabling access to credit for individuals traditionally
overlooked by conventional scoring systems.

Moving  forward,  further  research  could  explore  the  interpretability  of  deep  learning  models  in  compliance-focused
financial  environments,  as  well  as  real-time  deployment  of  such  systems  in  credit  decision  engines.  The  potential
integration of transformer-based models such as BERT or GPT for dynamic credit risk monitoring also presents a promising
avenue for future exploration.

Acknowledgement: All the author contributed equally.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

17

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

REFERENCE

Page No. 09-22

[1]  Hand, D. J., & Henley, W. E. (1997). Statistical classification methods in consumer credit scoring: a review.
in  Society),  160(3),  523–541.

the  Royal  Statistical  Society:  Series  A

(Statistics

Journal  of
https://doi.org/10.1111/j.1467-985X.1997.00078.x

[2]  Brown, I., & Mues, C. (2012). An experimental comparison of classification algorithms for imbalanced credit
3446–3453.

Applications,

Systems

Expert

39(3),

sets.

data

with

scoring
https://doi.org/10.1016/j.eswa.2011.09.033

[3]  Malekipirbazari,  M.,  &  Aksakalli,  V.  (2015).  Risk  assessment  in  social  lending  via  random  forests.  Expert

Systems with Applications, 42(10), 4621–4631. https://doi.org/10.1016/j.eswa.2015.01.002

[4]  Xiao,  L.,  Hu,  X.,  Yu,  F.  R.,  Xie,  R.,  &  Liu,  Y.  (2020).  Deep  learning  for  the  prediction  of  loan  default:  A
Innovation,  6(1),  1–22.

learning  approaches.  Financial

traditional  machine

comparison  with
https://doi.org/10.1186/s40854-020-00191-2

[5]  Cerchiello, P., Nicola, G., & Giudici, P. (2017). Big data analytics for bank customer profiling. Journal of Risk

and Financial Management, 10(1), 6. https://doi.org/10.3390/jrfm10010006

[6]  Mai, F., Shan, Z., Bai, Q., Wang, X. S., & Chiang, R. H. L. (2018). How does social media impact bankruptcy
555–578.

Quarterly,

Twitter.

42(2),

from

MIS

prediction?
Evidence
https://doi.org/10.25300/MISQ/2018/14418

[7]  Bazarbash, M. (2019). FinTech in Financial Inclusion: Machine Learning Applications in Assessing Credit Risk
Fund.

(IMF
https://www.imf.org/en/Publications/WP/Issues/2019/06/27/FinTech-in-Financial-Inclusion-Machine-
Learning-Applications-in-Assessing-Credit-Risk-46988

International

Monetary

19/109).

Working

Paper

No.

[8]  Huang, B., & Paul, M. J. (2020). Extracting actionable information from financial documents using BERT. In
Proceedings of the First Workshop on Financial Technology and Natural Language Processing (pp. 29–34).
https://doi.org/10.18653/v1/2020.financialnlp-1.4

[9]  Hossain, M. N., Hossain, S., Nath, A., Nath, P. C., Ayub, M. I., Hassan, M. M., ... & Rasel, M. (2024). ENHANCED BANKING
FRAUD  DETECTION:  A  COMPARATIVE  ANALYSIS  OF  SUPERVISED  MACHINE  LEARNING  ALGORITHMS. American
Research Index Library, 23-35.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

18

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

[10]  Uddin, A., Pabel, M. A. H., Alam, M. I., KAMRUZZAMAN, F., Haque, M. S. U., Hosen, M. M., ... & Ghosh, S. K. (2025).
Advancing  Financial  Risk  Prediction  and  Portfolio  Optimization  Using  Machine  Learning  Techniques. The  American
Journal of Management and Economics Innovations, 7(01), 5-20.

[11]  Nguyen, Q. G., Nguyen, L. H., Hosen, M. M., Rasel, M., Shorna, J. F., Mia, M. S., & Khan, S. I. (2025). Enhancing Credit
Risk Management with Machine Learning: A Comparative Study of Predictive Models for Credit Default Prediction. The
American Journal of Applied sciences, 7(01), 21-30.

[12]  Bhattacharjee, B., Mou, S. N., Hossain, M. S., Rahman, M. K., Hassan, M. M., Rahman, N., ... & Haque, M. S. U. (2024).
MACHINE  LEARNING  FOR  COST  ESTIMATION  AND  FORECASTING  IN  BANKING:  A  COMPARATIVE  ANALYSIS  OF
ALGORITHMS. Frontline Marketing,Management and Economics Journal, 4(12), 66-83.

[13]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S. S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[14]  Nath, F., Chowdhury, M. O. S., & Rhaman, M. M. (2023). Navigating produced water sustainability in the oil and gas
sector: A Critical review of reuse challenges, treatment technologies, and prospects ahead. Water, 15(23), 4088.

[15]  PHAN,  H.  T.  N.,  &  AKTER,  A.  (2024).  HYBRID MACHINE  LEARNING  APPROACH FOR  ORAL  CANCER  DIAGNOSIS  AND

CLASSIFICATION USING HISTOPATHOLOGICAL IMAGES. Universal Publication Index e-Library, 63-76.

[16]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S. S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[17]  Nath, F., Asish, S., Debi, H. R., Chowdhury, M. O. S., Zamora, Z. J., & Muñoz, S. (2023, August). Predicting hydrocarbon
production  behavior  in  heterogeneous  reservoir  utilizing  deep  learning  models.  In Unconventional  Resources
Technology Conference, 13–15 June 2023 (pp. 506-521). Unconventional Resources Technology Conference (URTeC).

[18]  Ahmmed,  M.  J.,  Rahman,  M.  M.,  Das,  A.  C.,  Das,  P.,  Pervin,  T.,  Afrin,  S.,  ...  &  Rahman,  N.  (2024).  COMPARATIVE
ANALYSIS  OF  MACHINE  LEARNING  ALGORITHMS  FOR  BANKING  FRAUD  DETECTION:  A  STUDY  ON  PERFORMANCE,
PRECISION, AND REAL-TIME APPLICATION. American Research Index Library, 31-44.

[19]  Akhi, S. S., Shakil, F., Dey, S. K., Tusher, M. I., Kamruzzaman, F., Jamee, S. S., ... & Rahman, N. (2025). Enhancing Banking
Cybersecurity: An Ensemble-Based Predictive Machine Learning Approach. The American Journal of Engineering and
Technology, 7(03), 88-97.

[20]  Pabel, M. A. H., Bhattacharjee, B., Dey, S. K., Jamee, S. S., Obaid, M. O., Mia, M. S., ... & Sharif, M. K. (2025). BUSINESS
ANALYTICS  FOR  CUSTOMER  SEGMENTATION:  A  COMPARATIVE  STUDY  OF  MACHINE  LEARNING  ALGORITHMS  IN
PERSONALIZED BANKING SERVICES. American Research Index Library, 1-13.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

19

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

[21]  Siddique, M. T., Jamee, S. S., Sajal, A., Mou, S. N., Mahin, M. R. H., Obaid, M. O., ... & Hasan, M. (2025). Enhancing
Automated Trading with Sentiment  Analysis: Leveraging Large Language Models for Stock Market Predictions. The
American Journal of Engineering and Technology, 7(03), 185-195.

[22]  Mohammad Iftekhar Ayub, Biswanath Bhattacharjee, Pinky Akter, Mohammad Nasir Uddin, Arun Kumar Gharami, Md
Iftakhayrul Islam, Shaidul Islam Suhan, Md Sayem Khan, & Lisa Chambugong. (2025). Deep Learning for Real-Time
Fraud  Detection:  Enhancing  Credit  Card  Security  in  Banking  Systems. The  American  Journal  of  Engineering  and
Technology, 7(04), 141–150. https://doi.org/10.37547/tajet/Volume07Issue04-19

[23]  Nguyen, A. T. P., Jewel, R. M., & Akter, A. (2025). Comparative Analysis of Machine Learning Models for Automated
Skin  Cancer  Detection:  Advancements  in Diagnostic Accuracy  and  AI  Integration. The  American  Journal  of  Medical
Sciences and Pharmaceutical Research, 7(01), 15-26.

[24]  Nguyen, A. T. P., Shak, M. S., & Al-Imran, M. (2024). ADVANCING EARLY SKIN CANCER DETECTION: A COMPARATIVE
ANALYSIS  OF  MACHINE  LEARNING  ALGORITHMS  FOR  MELANOMA  DIAGNOSIS  USING  DERMOSCOPIC
IMAGES. International Journal of Medical Science and Public Health Research, 5(12), 119-133.

[25]  Phan, H. T. N., & Akter, A. (2025). Predicting the Effectiveness of Laser Therapy in Periodontal Diseases Using Machine

Learning Models. The American Journal of Medical Sciences and Pharmaceutical Research, 7(01), 27-37.

[26]  Phan, H. T. N. (2024). EARLY DETECTION OF ORAL DISEASES USING MACHINE LEARNING: A COMPARATIVE STUDY OF
PREDICTIVE  MODELS  AND  DIAGNOSTIC  ACCURACY. International  Journal  of  Medical  Science  and  Public  Health
Research, 5(12), 107-118.

[27]  Al Mamun, A., Nath, A., Dey, S. K., Nath, P. C., Rahman, M. M., Shorna, J. F., & Anjum, N. (2025). Real-Time Malware
Detection in Cloud Infrastructures Using Convolutional Neural Networks: A Deep Learning Framework for Enhanced
Cybersecurity. The American Journal of Engineering and Technology, 7(03), 252-261.

[28]  Akhi, S. S., Shakil, F., Dey, S. K., Tusher, M. I., Kamruzzaman, F., Jamee, S. S., ... & Rahman, N. (2025). Enhancing Banking
Cybersecurity: An Ensemble-Based Predictive Machine Learning Approach. The American Journal of Engineering and
Technology, 7(03), 88-97.

[29]  Mazharul  Islam  Tusher,  “Deep  Learning  Meets  Early  Diagnosis:  A  Hybrid  CNN-DNN  Framework  for  Lung  Cancer

Prediction and Clinical Translation”, ijmsphr, vol. 6, no. 05, pp. 63–72, May 2025.

[30]  Integrating Consumer Sentiment and Deep Learning for GDP Forecasting: A Novel Approach in Financial Industry”., Int

Bus &amp; Eco Adv Jou, vol. 6, no. 05, pp. 90–101, May 2025, doi: 10.55640/business/volume06issue05-05.

[31]  Tamanna Pervin, Sharmin Akter, Sadia Afrin, Md Refat Hossain, MD Sajedul Karim Chy, Sadia Akter, Md Minzamul
Hasan,  Md  Mafuzur  Rahman,  &  Chowdhury  Amin  Abdullah.  (2025).  A  Hybrid  CNN-LSTM  Approach  for  Detecting

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

20

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

Anomalous Bank Transactions: Enhancing Financial Fraud Detection Accuracy. The American Journal of Management
and Economics Innovations, 7(04), 116–123. https://doi.org/10.37547/tajmei/Volume07Issue04-15

[32]  Mohammad Iftekhar Ayub, Biswanath Bhattacharjee, Pinky Akter, Mohammad Nasir Uddin, Arun Kumar Gharami, Md
Iftakhayrul Islam, Shaidul Islam Suhan, Md Sayem Khan, & Lisa Chambugong. (2025). Deep Learning for Real-Time
Fraud  Detection:  Enhancing  Credit  Card  Security  in  Banking  Systems. The  American  Journal  of  Engineering  and
Technology, 7(04), 141–150. https://doi.org/10.37547/tajet/Volume07Issue04-19

[33]  Mazharul Islam Tusher, Han Thi Ngoc Phan, Arjina Akter, Md Rayhan Hassan Mahin, & Estak Ahmed. (2025). A Machine
Learning Ensemble Approach for Early Detection of Oral Cancer: Integrating Clinical Data and Imaging Analysis in the
Public  Health. International
Journal  of  Medical  Science  and  Public  Health  Research, 6(04),  07–15.
https://doi.org/10.37547/ijmsphr/Volume06Issue04-02

[34]  Safayet Hossain, Ashadujjaman Sajal, Sakib Salam Jamee, Sanjida Akter Tisha, Md Tarake Siddique, Md Omar Obaid,
MD Sajedul Karim Chy, & Md Sayem Ul Haque. (2025). Comparative Analysis of Machine Learning Models for Credit
in  Banking  Systems. The  American  Journal  of  Engineering  and  Technology, 7(04),  22–33.
Risk  Prediction
https://doi.org/10.37547/tajet/Volume07Issue04-04

[35]  Ayub, M. I., Bhattacharjee, B., Akter, P., Uddin, M. N., Gharami, A. K., Islam, M. I., ... & Chambugong, L. (2025). Deep
Learning for Real-Time Fraud Detection: Enhancing Credit Card Security in Banking Systems. The American Journal of
Engineering and Technology, 7(04), 141-150.

[36]  Siddique, M. T., Uddin, M. J., Chambugong, L., Nijhum, A. M., Uddin, M. N., Shahid, R., ... & Ahmed, M. (2025). AI-
Powered  Sentiment  Analytics  in  Banking:  A  BERT  and  LSTM  Perspective. International  Interdisciplinary  Business
Economics Advancement Journal, 6(05), 135-147.

[37]  Thakur, K., Sayed, M. A., Tisha, S. A., Alam, M. K., Hasan, M. T., Shorna, J. F., ... & Ayon, E. H. (2025). Multimodal
Deepfake  Detection  Using  Transformer-Based  Large  Language  Models:  A  Path  Toward  Secure  Media  and  Clinical
Integrity. The American Journal of Engineering and Technology, 7(05), 169-177.

[38]  Al Mamun, A., Nath, A., Dey, S. K., Nath, P. C., Rahman, M. M., Shorna, J. F., & Anjum, N. (2025). Real-Time Malware
Detection in Cloud Infrastructures Using Convolutional Neural Networks: A Deep Learning Framework for Enhanced
Cybersecurity. The American Journal of Engineering and Technology, 7(03), 252-261.

[39]  Tusher, M. I., Hasan, M. M., Akter, S., Haider, M., Chy, M. S. K., Akhi, S. S., ... & Shaima, M. (2025). Deep Learning
for  Lung  Cancer  Prediction  and  Clinical

Meets  Early  Diagnosis:  A  Hybrid  CNN-DNN  Framework
Translation. International Journal of Medical Science and Public Health Research, 6(05), 63-72.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

21

INTERNATIONAL INTERDISCIPLINARY BUSINESS ECONOMICS ADVANCEMENT JOURNAL
eISSN: 2375-9615 pISSN: 2375-9607
DOI: - https://doi.org/10.55640/business/volume06issue07-02

VOLUME06 ISSUE07
Published 11-07-2025

Page No. 09-22

[40]  Sajal, A., Chy, M. S. K., Jamee, S. S., Uddin, M. N., Khan, M. S., Gharami, A. K., ... & Ahmed, M. (2025). Forecasting Bank
Profitability  Using  Deep  Learning  and  Macroeconomic  Indicators:  A  Comparative  Model  Study. International
Interdisciplinary Business Economics Advancement Journal, 6(06), 08-20.

[41]  Paresh Chandra Nath, Md Sajedul Karim Chy, Md Refat Hossain, Md Rashel Miah, Sakib Salam Jamee, Mohammad
Kawsur Sharif, Md Shakhaowat Hossain, & Mousumi Ahmed. (2025). Comparative Performance of Large Language
Models  for  Sentiment  Analysis  of  Consumer  Feedback  in  the  Banking  Sector:  Accuracy,  Efficiency,  and  Practical
Deployment. Frontline
07–19.
https://doi.org/10.37547/marketing-fmmej-05-06-02

Journal, 5(06),

Management

Marketing,

Economics

and

[42]  Hossain, S., Siddique,  M. T., Hosen, M. M., Jamee,  S.  S., Akter, S., Akter, P., ... &  Khan, M. S. (2025). Comparative
Analysis of Sentiment Analysis Models for Consumer Feedback: Evaluating the Impact of Machine Learning and Deep
Learning Approaches on Business Strategies. Frontline Social Sciences and History Journal, 5(02), 18-29.

[43]  Jamee, S. S., Sajal, A., Obaid, M. O., Uddin, M. N., Haque, M. S. U., Gharami, A. K., ... & FARHAN, M. (2025). Integrating
Consumer Sentiment and Deep Learning for GDP Forecasting: A Novel Approach in Financial Industry. International
Interdisciplinary Business Economics Advancement Journal, 6(05), 90-101.

[44]  Hossain, S., Sajal, A., Jamee, S. S., Tisha, S. A., Siddique, M. T., Obaid, M. O., ... & Haque, M. S. U. (2025). Comparative
Analysis  of  Machine  Learning  Models  for  Credit  Risk  Prediction  in  Banking  Systems. The  American  Journal  of
Engineering and Technology, 7(04), 22-33.

[45]  Pabel,  M.  A.  H.,  Bhattacharjee,  B.,  Dey,  S.  K.,  Jamee,  S.  S.,  Obaid,  M.  O.,  Mia,  M.  S.,  ...  &  Sharif,  M.  K.  BUSINESS
ANALYTICS  FOR  CUSTOMER  SEGMENTATION:  A  COMPARATIVE  STUDY  OF  MACHINE  LEARNING  ALGORITHMS  IN
PERSONALIZED BANKING SERVICES.

INTERNATIONAL INTERDISCIPLINARY BUSINESS
ECONOMICS ADVANCEMENT JOURNAL

https://www.iibajournal.org/index.php/iibeaj

22

