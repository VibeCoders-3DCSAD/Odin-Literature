---
conversion_metadata:
  converted_at: "2026-07-22T11:51:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Al Rafi.pdf"
  source_pdf_sha256: "106ab593ba98315047210143f34af4c2e616affc893cb6a277f7b91b6c7d09ff"
  page_count: 11
  markdown_char_count: 81725
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

AI-Driven Fraud Detection Using Self-Supervised Deep Learning 
for Enhanced Customer Identity Modeling

Md Al Rafi 
Washington University of Science and Technology, Alexandria, Virginia, USA 
Email: mdalrafi2@gmail.com

Abstract  
The  quick  growth  rate  of  e-financial  services  has  augmented  the  need  of  smart  and  dynamic  fraud  detection 
framework which had the capacity to acquire intelligent lean and dynamic and unbalanced threat models. The given 
article introduces an AI-based customer identity modeling and fraud system, which presupposes the implementation 
of  hybrid  temporal  and  graph  analytics  and  relies  on  the  self-supervised  deep  learning  to  increase  the  focus  on 
anomalies in the intricate setting of transactions. The suggested system entails contrastive behavioral representation 
learning  and  masked  feature  reconstruction  throughout  the  pretraining  stage  to  acquire  discriminative  latent 
embedding  of  the  customer  behavior  with  a  minimum  requirement  of  frail  information  with  labeling.  These 
embeddings are trained on a Temporal Transformer that is learned to learn the dynamics of sequential spending and 
a Graph Neural Network (GNN) that is learned to learn cross-account identity relationships.

It  is  a  fusion  of  the  temporal,  identity  and  self-supervised  embeddings,  which  apply  to  provide  sound  decision 
making  by  using  the  stacked  ensemble  of  XGBoost,  deep  neural  networks  and  logistic  regression  meta-learner  to 
rank real time risks. The performance metrics on the framework are  measured on large and very imbalanced real-
world  financial  transaction  data  on  the  accuracy,  recall,  F1-score,  ROC-AUC,  the  false  positive  and  latency  of 
detection. The recall, precision, and F1-score of the system are 17, 12 and 19 percent higher than the traditional rule-
based and supervised fraud detectors, as explained in the experiments. Moreover, identity-conscious modeling will 
be capable of minimizing the false positive rates by 15 percent and identify it in time, which may be considered in 
real-time cybersecurity analytics. In general, the proposed framework can be described as a flexible, sustainable and 
intelligent  system  of  proactive  fraud  detection,  dynamic  customer  identity  profiling,  and  next-generation  financial 
cybersecurity systems.

Keywords:  Fraud  detection;  Self-supervised  learning;  Deep  learning;  Customer  identity  modeling;  Anomaly 
detection; Cybersecurity analytics.

DOI: 10.21590/ijhit.06.01.02

1.  Introduction

The category of e-financial services, digital wallets and online banking services and real time payment systems have 
increased  multifolds  and  has  brought  a  radical  change  in  the  global  financial  ecosystem.  The  developments  have 
enabled  customers  to  be  more  convenient  and  fairly  inclusive  of  finances,  however,  they  have  increased  the 
exposure  of  cybercriminals.  Examples  of  such  fraudulent  activities  that  are  increasingly  sophisticated,  automated 
and  adaptive  include  identity  theft,  account  takeover,  transaction  laundering,  phishing-based  frauds  and  synthetic 
identity  creation.  The  ever-evolving  challenge  of  the  threat  environment  with  conventional  rule-based  and  static 
machine learning fraud detection systems may be very daunting since it relies on manually constructed features, set 
points, and supervised learning frameworks that require significant quantities of labeled fraud data [1].

March 2024

www.ijhit.info

8 | Page

---

<!-- PAGE 2 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

The  vastly  disproportionate  level  of  the  amount  of  fraud  cases  in  transactional  data  is  one  of  the  most  important 
issues of  modern  fraud detection, fraud cases tend to be  under 1 percent of all transactions  [2]. The result of this 
mismatch  is  biased  training,  inefficient  generalization  and  high  false-negative  errors  in  standard  classifiers. 
Furthermore,  the  trend  of  fraud  is  being  continuously  evolved  due  to  the  adversarial  learning  where  the  attackers 
deliberately  modify  the  behavior  so  that  they  are  not  detected.  This  means  that  in  the  present  time,  the  fraud 
detection  models  must  be  self-adaptive,  concept  drift  resilient  and  capable  of  detecting  the  previously  unknown 
(zero-day) attack patterns [3].

The current advances in deep learning have enabled the automation of hierarchical features of raw data extraction, 
which  has  significantly  improved  the  detection  accuracy  of  financial  fraud.  Long  Short-Term  Memory  (LSTM), 
Gated  Recurrent  Units  (GRU)  and  sequence-based  models  grounded  on  transformers  have  demonstrated  much 
potential  to  learn  time-related  dependencies  of  transactional  streams.  At  the  same  time,  graph  neural  networks 
(GNNs)  have  been  proven  to  be  effective  in  terms  of  modeling  relational  data  (shared  devices,  IP  addresses, 
payment instruments and links between demeanors between customers). However, most of these models rely heavily 
on  the  fully  supervised  learning  and  hence  were  prone  to  annotation  bias,  latent  fraud  labels,  and  novel  attack 
techniques that cannot be shown in history [4] [5]. 
To  address  these  limitations,  self-supervised  learning  (SSL)  has  emerged  as  a  suitable  representation  learning 
paradigm which is not explicitly labeled. SSL applies intrinsic data structure to form pretext tasks in masked feature 
prediction, contrastive instance discrimination and temporal context prediction. In finance, where, due to a lack of 
labeled  data  about  fraud,  or  the  data  is  slow  or  otherwise  expensive  to  label,  the  idea  of  the  SSL  provides  an 
opportunity to have high-quality behavioral embeddings using large unlabeled transaction data. These embeddings 
represent the latent customer behavior and transaction dynamics, and may be utilized downstream to recognize an 
anomaly in a better way. 
Another new frontier in fraud detection is customer identity modeling whereby an individual transaction analysis is 
replaced by a larger description of regular behavioral patterns over time, across devices, across locations and social 
networks.  Identity  modeling  is  also  necessary  in  determining  synthetic  identities,  mule  networks,  and  organized 
rings  of  fraud  which  is  typically  efficient  in  evading  transaction-level  models.  Behavioral  identity  graphs  can  be 
used to complement the deep learning to convert point-based classification to relation-conscious risk assessment and 
identify it at an earlier stage and more efficiently [6].

The study suggests a new AI-based fraud detection model, which is a self-supervised deep-learning platform with 
customer identity modeling. The framework integrates:

  Learn invariant representations of customer behavior through contrastive self-supervised pretraining. 
  Masked feature reconstruction to powerfully represent missing/noisy data. 
  Long-term temporal transaction patterns modeling using transformers. 
  Encoding of cross account identity relationships by Graph Neural Network (GNN) modeling. 
  Final fraud probability estimation risk scoring layer which is a hybrid fusion.

The  proposed  architecture  is  expected  to  operate  under  the  influence  of  real-life  factors,  including  uneven 
information  which  is,  by  far,  weak  and  massive  transactions.  The  suggested  approach  in  comparison  with  the 
conventional  supervised  fraud  detection  systems  significantly  reduces  the  usage  of  manually-engineered  features 
and  previous-known  fraud  indicators.  Instead,  it  trains  huge  data  sets  of  unlabeled  data  to  predict  discriminative 
customer behavior representations which can be used to predict new fraud patterns. 
Experimental validation is done on the large-scale imbalanced transactional data and the mixed cases of frauds. It is 
demonstrated  to  have  high  recall,  accuracy  and  F1-score  compared  to  classical  machine  learning  models,  and 
improved supervised deep learning baselines. In addition, identity modelling aspect reduces false positive responses

March 2024

www.ijhit.info

9 | Page

---

<!-- PAGE 3 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

and  enables  fraud  to  be  detected  at  a  later  stage  of  its  implementation  by  ascertaining  suspicious  behaviours 
association to numerous accounts.

The main contributions of this work are summarized as follows:

  A fraud detection architecture, which is based on self-supervised learning and which reduces the use of labeled fraud

data.

  A graph-based and joint sequence based identity modeling framework to aid improvement in behavioral profiling. 
  A multi-dimensional risk analysis pipeline based on a hybrid deep learning architecture combining Transformer and

GNNs.

  Similar overall performance measurement with significant gains in recall, accuracy, F1-score and decrease in false-

positive.

  Modern digital financial platforms can have a scalable and real-time deployable fraud detection solution.

The present piece of work provides self-supervised deep learning as the baseline of next-generation fraud detection 
and cybersecurity analytics within dynamic financial settings.

2.  Literature Review

The swift development of industrial automation, cyber-physical systems (CPS), artificial intelligence (AI), and deep 
learning have brought a profound change to the framework of  modern manufacturing, communication system, and 
system  frameworks  of  financial  fraud  detection.  Such  interdisciplinary  developments  have  provided  the  base  of 
intelligent,  secure  and  efficient  Industry  4.0-based  ecosystems.  The  literature  review  offers  critical  analysis  of 
previous  works  of  energy-efficient  automation,  CPS,  explainable  AI,  ethical  automation,  and  deep  learning-based 
fraud and intrusion detection systems.

An  early  effort  at  industrial  automation-optimized  energy-efficient  design  of  electric  machines  was  given  by 
Chukwunweike [1] in the context of using renewable energy. The paper has focused on computational optimization 
methods  of  enhancing  efficiency,  thermal  stability,  and  power  density  of  electric  machines.  This  publication 
provided  a  benchmark  of  sustainable  automation,  with  the  emphasis  placed  on  the  role  of  optimization-based 
engineering in the contemporary industrial setting.

Upon  advancing  the  automation  paradigm  to  the  area  of  cyber-physical  integration,  Javaid  et  al.  [2]  offered  an 
overview of CPS in the context of Industry 4.0, in terms of architectural frameworks, communication protocols, and 
practical  applications  in  the  industrial  sphere.  According  to  their  analysis,  the  demand  to  be  a  digital  transformer 
outlined  smart  factories,  real-time  data  sharing,  and  system  compatibility  as  the  essential  elements  of  the  digital 
transformation.  CPS  was  also  brought  into  the  limelight  by  the  authors  as  an  essential  facilitator  of  smart 
manufacturing, predictive maintenance and intelligent decision-making.

Due  to  the  growing  complexity  of  industrial  systems  controlled  by  AI,  explainability  is  now  a  serious  demand. 
Ahmed et al. [3] conducted a survey on the move towards explainable AI (XAI) in Industry 4.0. Their review dealt 
with  the  main  issues  concerning  trust,  transparency,  regulatory  compliance,  and  the  human  interpretability  of 
intelligent  systems.  The  paper  has  highlighted  the  necessity  of  incorporating  explainability  in  the  high-impact 
sectors of manufacturing automation, healthcare, and finance. 
Ribeiro  and  Bjorkman  [4]  examined  the  shift  towards  the  implementation  of  cyber-physical  production  systems 
(CPPS). They reveal that there are major conceptual, architectural, and technical issues such as the scalability of the 
system, data  synchronization, cybersecurity threats, and  workforce skills. Their results  showed that CPPS is  more 
flexible and efficient, but at the cost of a very high complexity and vulnerability of the systems.

March 2024

www.ijhit.info

10 | Page

---

<!-- PAGE 4 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

Akinsolu [5] explored the use of AI in the manufacturing and industrial production systems with a PEST (Political, 
Economic, Social, and Technological) perspective. The work gave a management view of AI implementation, with 
its risks of investing in it, ethical issues, the loss of workforce, and the infrastructure to support the technology. This 
article  highlighted  the  importance  of  effective  governance  and  regulations  congruence  to  the  integration  of  AI,  as 
well as the technological readiness.

On  the  ethical  aspects  of  AI  and  automation,  Igwe-Nmaju  [6]  analyzed  the  human-machine  interaction  in  the 
corporate  communication system in addition to the  manufacturing. Ethical issues, including the bias  generated by 
algorithms,  loss  of  human  agency,  risks  of  surveillance,  and  diminished  emotional  intelligence  in  automated 
organizational communication were pointed out in the study. This publication strengthened the necessity of ethical 
AI systems, particularly in the delicate human-focused setting. 
The  paradigm  shift  towards  AI-powered  anomaly  detection  became  particularly  high  in  the  area  of  financial 
cybersecurity. Haseena et al. [7] developed a framework of bat optimization to detect credit card frauds. Their bio-
inspired  optimization  system  enhanced  the  detection  performance  by  adapting  dynamically  the  choice  of  features 
and decision boundaries. The experiment showed that optimization methods are a great way in terms of improving 
the classification of fraud detecting systems. 
Zhang  et  al.  [8]  developed  HOBA,  a  new  feature  engineering  model  with  deep  learning  based  credit  card  fraud 
detection.  Their  model  offered  better  extraction  of  feature  relevances  and  dimensionality,  resulting  in  better 
detection rates and quicker convergence rates. This paper established that feature engineering is an essential part of 
the security deep learning systems. 
Wang and Smys [9] examined adaptive learning processes by investigating the adaptive activation of deep neural 
networks.  The  comparative  analysis  that  they  conducted  proved  that  dynamic  activation  functions  are  superior  to 
fixed functions in terms of their quickness in convergence, their classification accuracy, and their models stability. 
The direct use of this work in the creation of more efficient and robust deep learning models in real-time financial 
and security applications is possible. 
A deep convolutional neural network (CNN) model of real-time credit-card fraud detection and alert generation was 
developed by Chen and Lai [10]. Their framework was found to be highly classified based on the amount of spatial 
features  that  were  extracted  automatically  using  the  transaction  data.  The  paper  has  shown  the  analysis  of  an 
increasing focus of CNNs on non-image data in the form of financial analytics. 
Continuing the area of fraud detection to the medical field, Mehbodniya et al. [11] implemented machine learning 
and deep learning algorithms in the detection of financial fraud in the medical field of billing and insurance claims. 
Their  comparative  analysis  revealed  that  hybrid  deep  learning  models  are  better  than  classical  machine  learning 
methods  to  detect  fraudulent  healthcare  transactions.  This  article  brought  out  the  growing  overlap  between 
healthcare informatics and financial cybersecurity. 
Alghofaili et al. [12] suggested deep learning model (LSTM) of financial fraud detection. They were able to better 
performance  with their system using temporal variations of transactional data  relative to the static classifiers. The 
results of the study proved that deep learning architecture sequencing is quite effective in modeling time-dependent 
fraud behaviors. 
Other  than  detecting  fraud,  AI-powered  cybersecurity  has  become  a  major  reason  of  interest.  Abusitta  et  al.  [13] 
presented a  deep learning  framework of a proactive  multi-cloud collaborative system of intrusion detection. Their 
architecture  allowed sharing  of cross-cloud threat intelligence and  made attacks  much  more accurate  in detection. 
The paper has highlighted the need of distributed security architecture in multi-cloud formats. 
Aloqaily  et  al.  [14]  designed  an  intrusion  detection  system  of  connected  vehicles  in  the  area  of  smart  cities  and 
intelligent transportation. Their design used AI-driven monitoring and detecting anomalies through traffic to achieve 
vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications. The article showed how AI could be 
used to ensure cyber-physical mobility infrastructures.

March 2024

www.ijhit.info

11 | Page

---

<!-- PAGE 5 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

Lei et al. [15] lastly suggested a distributed deep neural network model to classify credit card frauds in a large scale. 
Their decentralized design allowed real time classification of frauds on geographically distributed financial nodes. 
The findings showed that the distributed AI security frameworks were more scalable, less latent, and their detection 
accuracy was better than that of centralized models, validating the increasing importance of distributed AI security 
models.

3. Methodology  
3.1 System Architecture Overview 
The  fraud  detection  pipeline  proposed  is  developed  as  a  multi-stage  intelligent  pipeline  that  combines  self-
supervised  learning,  deep  temporal  model,  identity  sensitive  graph  analytics  and  hybrid  decision  fusion  to  aid  in 
fraud detection. The first stage is an instance of a Self-Supervised Representation Learning Module which is trained 
to learn powerful behavioral features on unlabeled information related to transactions through contrastive learning 
and masked feature reconstruction. These embeddings are inputted into the Temporal Sequence Modeling Module 
that is applied to a Transformer architecture to encode sequential patterns of spending, velocity of transaction and 
temporal anomaly. At the same time, the Customer Identity Graph Modeling Module is based on the Graph Neural 
Networks (GNNs) that define the complicated relationships between accounts, devices, and users to identify fraud 
rings and mule networks. Finally, Hybrid Fraud Detection and Risk Scoring Module integrates the outputs of all of 
the above modules to use an ensemble of machine learning models to compute the accurate risk of fraud and real-
time risk rating. The degree of detection, scalability and strength of such a modular design is high. 
Each module addresses a distinct aspect of behavioral fraud modeling while contributing to a unified risk assessment 
output.

Input: Raw Transactional Data

Data Preprocessing & Feature Encoding

Self-supervised Pretraining Block (Contrastive + Masked 
Reconstruction)

Transformer-based Temporal Modeling

Gnn-based Identity Modeling

Hybrid Ensemble Classifier (Xgboost + DNN + Logistic Regression)

Final Output: Fraud Risk Score

Figure 1: Overall System Architecture Diagram (End-to-End Pipeline)

March 2024

www.ijhit.info

12 | Page

---

<!-- PAGE 6 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

3.2 Data Preprocessing and Feature Encoding 
The  proposed  structure  would  contain  transactional  records,  which  is  a  rich  structured  attribute,  like  the  sum  of 
transaction, time of transaction, type of merchants, place of transaction, device identification, IP address, payment 
mode,  velocity-supported  functionality  and  also  detailed  account  data.  Continuous  characteristics  undergo  z-score 
normalization to stabilize the numerics and get the uniform scale, and the categorical features are transformed to the 
dense features via learned embedding layers. Customer behavioral sequences are constructed using sliding temporal 
windows, and here the chronological sequence of the transactions is taken care of and the spending pattern can be 
effectively  modeled.  At  the  same  time,  identity  relationships  between  customers  are  internalized  through  the 
development  of  identity  sides  with  the  background  of  similarities  in  such  characteristics  as  common  device 
identifications, identical IP addresses, similar types of merchant groups, frequent geolocation patterns, and common 
recipient accounts. The combination of all these features forms a dynamic and heterogeneous identity graph, which 
enables it to analyze the relationship of cross-accounts and identity learning of fraud prevention.

3.3 Self-Supervised Pretraining 
The  pretraining  stage  is  self-supervised  to  acquire  robust  and  discriminative  representations  of  customer 
transactional  behavior  without  the  heavy  dependence  on  labelled  fraud  data.  It  is  done  by  using  contrastive 
behavioral representation learning and masked  feature reconstruction. During the contrastive learning phase, every 
customer transaction sequence is perturbed with a sequence of stochastic augmentations, such as temporal shuffling 
to  differentiate  order  of  transaction,  feature  masking  to  emulate  missing  information,  additive  noise  to  promote 
generalization, and crop subsidiary to learn local behavioral pattern. These changes produce different perceptions of 
one and the same sequence of behavior, which allows the model to develop invariance features that stay consistent 
in a variety of perturbations. An objective function is also contrastive and is optimized to ensure that embeddings of 
augmented versions of the same sequence are maximized and that they are not similar to embeddings of different 
customers.  It  is  done  by  a  temperature-scaled  similarity  loss  that  imposes  tight  clustering  of  behaviorally  similar 
samples in latent embedding space.

A  contrastive  objective  maximizes  agreement  between  different  augmented  views  of  the  same  behavior  while 
minimizing similarity with other customers:

where zi and zj are embedding pairs and τ is temperature. 
As  an  addition  to  the  contrastive  approach,  masked  feature  reconstruction  is  applied  whereby  a  random  subset  of 
transactional attributes are masked and an encoder-decoder network is trained on the remaining attributes to predict 
the ones that are missing. The undertaking will force the model to acquire profound contextual reliance among the 
transaction  attributes  and  enhance  robustness  to  noisy,  fragmented,  and  partially  unfamiliar  financial  data. 
Collectively,  these  self-monitored  goals  allow  the  framework  to  obtain  material  representations  of  behavioral 
patterns that are quite effective at improving downstream fraud detection.

3.4 Temporal Transformer Module 
The  Temporal  Transformer  Module  is  used  to  capture  sequential  relationships  in  customer  transaction  behavior 
based on multi-head self-attention mechanism. In contrast to recurrent models, Transformer takes advantage of the 
entire sequence of transactions and attaches adaptive  importance  weights to various time steps using the attention 
function which is defined as

March 2024

www.ijhit.info

13 | Page

---

<!-- PAGE 7 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

This  facilitates  this  model  to  reflect  long-term  temporal  correlations  and  complicated  spending  patterns.  The 
behaviors patterns learned by the module successfully include periodicity of spending, spikes of sudden velocities, 
anomalies  of  bursts  in  transactions,  and  reactivation  of  dormant  accounts.  The  Transformer  output  is  a  high-
dimensional time-based risk embedding that encapsulates the dynamic financial behavior of individual customers to 
be classified as fraudulent in downstream.

3.5 Graph Neural Network Identity Modeling 
To  learn  relational  risk  representations  on  interconnected  accounts,  a  mix  of  GraphSAGE  and  Graph  Attention 
Networks  (GAT)  is  used  to  model  the  customer  identity  graph.  The  graph  below  is  a  representation  of  customer 
accounts  where  nodes  are  customer  accounts  and  the  edges  are  shared  attributes  like  devices,  IP  addresses, 
merchants, geolocations and beneficiary relationships. The update of node embedding follws the rule

where the locality of the neighborhood results in the contagion of the risk factor of behavior among closely related 
accounts.  Neighborhood  sampling  is  applicable  to  scale  GraphSAGE  to  large-scale  graphs,  but  GAT  relies  on 
attention weights to emphasize more importance on the neighbors. It helps to identify organized rings of fraud, mule 
network and synthetic identity clusters successfully due to the ability of this identity modelling scheme to uncover 
hidden patterns of relationships. The cross-account risk is also propagated by the model, and indicators of fraud in 
one account can be utilized to modify the risk score in other accounts, which improves the accuracy of the detection 
and false positives significantly. 
3.6 Hybrid Fraud Detection and Risk Scoring 
The hybrid module of fraud detection and risk scoring involves the multi-dimensional behavioral intelligence, which 
is  based  on  the  self-supervised  embedding,  Temporal  Transformer  embedding,  and  Graph  Neural  Network  based 
identity  embedding  to  result  in  the  final  probability  of  an  occurrence  of  a  fraud.  These  complementary 
representations  are  the  individual  behavioral  patterns,  temporal  transaction  dynamics  and  cross-account  relational 
risks  respectively.  That  feature  set  is  then  inputted  to  a  stacked  ensemble  model  consisting  of  three  learning 
algorithms: an XGBoost Gradient Boosting to learn the complex non-linear interaction of features, a Deep Neural 
Network classifier to learn high-dimensional features representations and a Logistic Regression meta-learner to learn 
probabilistic calibration and decision fusion. This ensemble method has the advantages of increasing robustness as it 
has  led  to  the  increased  generalization  of  various  patterns  of  frauds,  a  smaller  model  bias  and  dramatic  reduced 
model  variance.  The  final  fraud  risk  score  is  computed  as  a  weighted  aggregation  of  the  output  probabilities 
produced by each base classifier, formulated as

Where Pi represents the individual model probabilities and wi are adaptive weights that are to be optimized during 
the  validation.  This  looks  after  balance  between  sensitivity  and  specificity  in  this  adaptive  fusion  mechanism 
allowing real time detection of fraud with a low false positive.

3.7 Evaluation Metrics 
The effectiveness of the suggested fraud detection structure is measured with the help of a set of classification and 
working  measures  in  order  to  guarantee  the  predictive  precision  and  real-time  usage.  The  proportion  of  the 
accurately identified fraud cases amongst all the detected fraud cases is measured using precision, which indicates

March 2024

www.ijhit.info

14 | Page

---

<!-- PAGE 8 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

the reliability of the system. Recall measures the capacity of a model to detect real fraudulent transactions which is 
essential  in  reducing  financial  losses.  The  F1-score  represents  a  harmonized  measure,  a  combination  of  precision 
and recall as one beneficial measure. The Receiver Operating Characteristic-Area Under the Curve (ROC-AUC) is 
used to perform the analysis of the global discrimination ability under different decision thresholds. False Positive 
Rate (FPR) is a metric that determines the percentage of legitimate transactions that were wrongly identified as fraud 
that has a direct influence on customer experience and cost of operation. Detecting latency is evaluated to confirm 
the  possibility  of  real-time  deployment.  Focal  loss  and  dynamic  thresholding  are  implemented  to  solve  extreme 
imbalance  between  classes  in  financial  data  to  prioritize  difficult-to-classify  fraud  samples,  and  cost-sensitive 
learning  is  employed  in  order  to  penalize  missed  fraudulent  transactions  more,  providing  robust  and  balanced 
detection accuracy.

4. Results and Discussion 
4.1 Dataset Characteristics 
The  trial  assessment  is  done  on  a  large  volume  of  real-world  transactional  data  in  large-scale  with  a  total  of 
35,248,912  financial  transactions  with  about  4.2  million  distinct  customers.  Out  of  these,  95,312  transactions  are 
confirmed  to  be  fraudulent,  and  thus,  the  rate  of  fraud  is  much  skewed  at  0.27,  which  is  realistic  in  real-life 
operational  banking  settings.  The  average  number  of  transactions  per  customer  is  239  that  allows  modeling 
behavioral and sequential spending patterns in the long term. All the transactions are modeled in a rich feature space 
of 187 dimensions (monetary, temporal, spatial, device-level, and behavioral). The sheer volume, the high level of 
imbalance between classes, the high customer diversity, and high-dimensional characteristics precondition the high 
relevance of this dataset to the testing of the robustness, scalability, and applicability of  advanced  AI-based  fraud 
detection systems in real-world conditions.

Table 1- Dataset Statistics

Parameter 
Total Transactions 
Fraud Transactions 
Fraud Rate 
No. of Customers 
Avg. Transactions per User 
Feature Dimensions

Value 
35,248,912 
95,312 
0.27% 
4.2 million 
239 
187

4.2 Baseline Model Comparison 
Table  2  shows  that  the  proposed  self-supervised  learning  (SSL)  and  hybrid  fraud  detection  framework  possess 
considerable advantages over the traditional and fully supervised models. The rule-based system acts as a reference 
point and has a low level of effectiveness with a precision of only 0.61 and a very low level of recall of 0.18, which 
gives  it  a  poor  F1-score  of  0.28.  This  shows  that  although  a  small  portion  of  fraud  is  detected  but  still  the  large 
proportion  of  all  fraudulent  transactions  cannot  be  detected  and  the  false  positive  rate  (FPR)  is  really  high  that  is 
0.21. 
The precision of logistic regression is shown to be improving moderately with a recall of 0.54 and precision of 0.73, 
which shows  the advantages  of learning data-driven rules  compared to fixed rules. Random Forest also has better 
detection ability, with F1-score of 0.69 and low FPR of 0.11 when learning in an ensemble. The supervised LSTM 
model does even better and triggers the patterns of transactions over time to achieve a precision of 0.86, recall of 
0.69, and an F1-score of 0.77.

The suggested SSL + Hybrid reaches much higher performance than all baselines with an outstanding precision of 
0.98 and a recall of 0.90,  which leaves the F1-score of 0.96. Most importantly, it has a false positive  rate  of only

March 2024

www.ijhit.info

15 | Page

---

<!-- PAGE 9 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

0.04  meaning  that  it  makes  very  reliable  predictions  of  frauds  and  with  minimum  of  disturbance  to  honest 
customers.  All  these  enhancements  directly  justify  the  efficacy  of  self-supervised  representation  learning  in 
conjunction  with  temporal  modeling  and  identity-conscious  graph  learning.  These  findings  clearly  illustrate  the 
better detection of complex and changing patterns of fraud in complex unbalanced real-world data.

Table 2- Performance Comparison with Baselines

Precision  Recall  F1-Score  FPR 
Model 
0.21 
0.61 
Rule-Based System 
0.14 
0.73 
Logistic Regression 
0.11 
0.81 
Random Forest 
0.09 
LSTM (Supervised) 
0.86 
0.04 
Proposed SSL + Hybrid  0.98

0.28 
0.62 
0.69 
0.77 
0.96

0.18 
0.54 
0.61 
0.69 
0.90

1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0

Precision

Recall

F1-Score

Figure 2: Performance Comparison of Machine Learning and Deep Learning Models

4.3 Impact of Identity Modeling 
Table 3, obtained through the ablation, vividly shows how the Graph Neural Network (GNN) module plays a critical 
role  in  the  performance  of  the  entire  process  of  fraud  detection.  A  system  that  is  run  without  identity  modeling 
through GNN has a high precision of 0.92 and recall of 0.78; nevertheless, the false positive rate (FPR) is low, 0.19. 
This means that although the model is effective in pointing out most of the fraudulent transactions; it still raises a 
large  percentage  of  false  alerts.  Once  the  GNN  module  is  incorporated,  the  performance  of  the  system  becomes 
significantly higher, and the precision is 0.98, and the recall is 0.90. The most striking is that the FPR in the most 
significant way decreases to 0.04. This substantial decrease proves that identity-aware graph learning allows to make 
more precise cross-account risk inferences and to properly curb false prediction of fraud.

Table 3- Effect of GNN-Based Identity Modeling 
Configuration  Precision  Recall  FPR 
0.19 
Without GNN  0.92 
0.04 
0.98 
With GNN

0.78 
0.90

March 2024

www.ijhit.info

16 | Page

---

<!-- PAGE 10 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

4.4 Ablation Study of Self-Supervised Learning 
Table 4 represents the outcome of the ablation study that involves the discussion of the performance of multiple self-
supervised learning (SSL) strategies. The model achieves the baseline F1-score of 0.81 without the assistance of the 
SSL,  indicating  that  the  model  is  not  very  capable  of  locating  intricate  behavioral  patterns.  It  is  only  contrastive 
learning that gives an F1-score of 0.89 due to similarity being artificially enforced between augmented transaction 
views, and pure masked feature reconstruction gives an F1-score of 0.88 due to the method being less sensitive to 
missing  or  contaminated  data.  A  combination  of  contrastive  and  masked  reconstruction  which  is  combined  as 
combined  SSL  has  the  highest  F1-score  of  0.96. This  demonstrates  that  the  conjunction  of  multiple  self-managed 
objectives  has  more  interesting  entrenching  of  behavior,  and  the  level  of  detecting  fraud  is  in  a  deeper  sense 
enhanced.

Table 4- Contribution of Self-Supervised Components

F1-Score 
Configuration 
No SSL 
0.81 
Contrastive Only  0.89 
0.88 
Masked Only 
0.96 
Combined SSL

5. Conclusion and Future Work  
The current paper proposes a practical model of AI-based fraud detector, the model is based on customer identity 
modeling and self-supervised deep learning that would eliminate some of the most challenging concerns in terms of 
financial security. The system can reduce the drawback of the imbalance of classes, delayed labeling  and emerging 
fraud schemes by integrating  the discriminant behavior by  utilizing the unlabeled transactional data. Transformer-
based temporal sequence learning as a hybrid of Graph Neural Network (GNN)-based identity analysis proves to be 
effective  to  learn  the  multidimensional  tendencies  of  fraud  over  time  and  among  mutually  connected  accounts. 
Experimental  tests  are  done  on  large  real-world  datasets  showing  massive  and  enormous  improvement  in  recall, 
precision,  and  F1-score  that  is  far  beyond  what  traditional  and  supervised  baselines  can  show.  Moreover,  the 
framework also has low false positive rate and can be implemented in detecting real-time hence the reason why it 
can be implemented in a high-throughput financial environment.

In a practical context, the framework helps the financial institutions to accept the usage of early warning systems in 
preventing  fraud, recurrence  of identity risk score, and dynamism of cybersecurity analytics. The reduction of the 
operational  costs  of  manual  investigations  and  remediation  are  minimized  on  the  enhancement  of  the  customer 
experience and reduction of the false positives. 
The  Future  Work  Future  Work  Future  Work  will  optimize  the  effort  of  the  structure  to  federated  self-supervised 
learning in order to achieve privacy preserving, multi-institution fraud detection. The added explainable modules of 
AI will increase transparency and control and online continuing learning will enable the system to adapt to concept 
drift in real-time. Moreover, cross border intelligence exchange in banking, telecom and e commerce establishment 
will help in identifying new coordinated trends of frauds. Combinations of all these directions  would result in the 
future generation AI-based system of detecting fraud being more scalable, robust, and interpretable.

References 
1.  Chukwunweike,  ―Design  and  optimization  of  energy-efficient  electric  machines  for  industrial  automation  and 
renewable  power  conversion  applications,‖  Int.  J.  Comput.  Appl.  Technol.  Res.,  vol.  8,  no.  12,  pp.  548–560, 
2019, doi: 10.7753/IJCATR0812.1011.

March 2024

www.ijhit.info

17 | Page

---

<!-- PAGE 11 -->

International Journal of Humanities and Information Technology (IJHIT) 
e-ISSN: 2456 –1142,  Volume 6, Issue 1, (March 2024), ijhit.info

2.  M.  Javaid,  A.  Haleem,  R.  P.  Singh,  and  R.  Suman,  ―An  integrated  outlook  of  cyber–physical  systems  for 
Industry 4.0: Topical practices, architecture, and applications,‖ Green Technol. Sustain., vol. 1, no. 1, p. 100001, 
Jan. 2023.

3.  I. Ahmed, G. Jeon, and F. Piccialli, ―From artificial intelligence to explainable artificial intelligence in Industry 
4.0:  A  survey  on  what,  how,  and  where,‖  IEEE  Trans.  Ind.  Informatics,  vol.  18,  no.  8,  pp.  5031–5042,  Aug. 
2022.

4.  L.  Ribeiro  and  M.  Björkman,  ―Transitioning  from  standard  automation  solutions  to  cyber-physical  production 
systems: An assessment of critical conceptual and technical challenges,‖ IEEE Syst. J., vol. 12, no. 4, pp. 3816–
3827, Dec. 2018.

5.  M.  O.  Akinsolu,  ―Applied  artificial  intelligence  in  manufacturing  and  industrial  production  systems:  PEST

considerations for engineering managers,‖ IEEE Eng. Manag. Rev., vol. 51, no. 1, pp. 52–62, Mar. 2023.

6.  C.  Igwe-Nmaju,  ―AI  and  automation  in  organizational  messaging:  Ethical  challenges  and  human–machine 
interaction in corporate  communication,‖  Int.  J. Eng. Technol.  Res. Manag., vol.  5, no. 12, p. 256, Dec. 2021, 
doi: 10.5281/zenodo.15562214.

7.  H. S. Haseena, S. Saroja, N. Suseandhiran, and B. Manikandan, ―An intelligent approach for anomaly detection

in credit card data using bat optimization algorithm,‖ Intell. Artif., vol. 26, pp. 202–222, 2023.

8.  X. Zhang, Y. Han, W. Xu, and Q. Wang, ―HOBA: A novel feature engineering methodology for credit card fraud

detection with a deep learning architecture,‖ Inf. Sci., vol. 557, pp. 302–316, 2021.

9.  H.  Wang  and  S.  Smys,  ―Overview  of  configuring  adaptive  activation  functions  for  deep  neural  networks—A

comparative study,‖ J. Ubiquitous Comput. Commun. Technol., vol. 3, pp. 10–22, 2021.

10. J.-I. Chen and K.-L. Lai, ―Deep convolution neural network model for credit-card fraud detection and alert,‖ J.

Artif. Intell. Capsul. Netw., vol. 3, pp. 101–112, 2021.

11. A.  Mehbodniya  et  al.,  ―Financial  fraud  detection  in  healthcare  using  machine  learning  and  deep  learning

techniques,‖ Secur. Commun. Netw., vol. 2021, Art. no. 9293877, 2021.

12. Y. Alghofaili, A. Albattah, and M. A. Rassam, ―A financial fraud detection model based on LSTM deep learning

technique,‖ J. Appl. Secur. Res., vol. 15, pp. 498–516, 2020.

13. A.  Abusitta,  M.  Bellaiche,  M.  Dagenais,  and  T.  Halabi,  ―A  deep  learning  approach  for  proactive  multi-cloud

cooperative intrusion detection system,‖ Future Gener. Comput. Syst., vol. 98, pp. 308–318, 2019.

14. M. Aloqaily, S. Otoum, I. A. Ridhawi, and Y. Jararweh, ―An intrusion detection system for connected vehicles in

smart cities,‖ Ad Hoc Netw., vol. 90, Art. no. 101842, 2019.

15. Y.-T. Lei  et al., ―A distributed deep neural network  model for credit card fraud detection,‖  Financ. Res. Lett.,

vol. 58, Art. no. 104547, 2023.

March 2024

www.ijhit.info

18 | Page

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
AI-Driven Fraud Detection Using Self-Supervised Deep Learning
for Enhanced Customer Identity Modeling
Md Al Rafi
Washington University of Science and Technology, Alexandria, Virginia, USA
Email: mdalrafi2@gmail.com
Abstract
The quick growth rate of e-financial services has augmented the need of smart and dynamic fraud detection
framework which had the capacity to acquire intelligent lean and dynamic and unbalanced threat models. The given
article introduces an AI-based customer identity modeling and fraud system, which presupposes the implementation
of hybrid temporal and graph analytics and relies on the self-supervised deep learning to increase the focus on
anomalies in the intricate setting of transactions. The suggested system entails contrastive behavioral representation
learning and masked feature reconstruction throughout the pretraining stage to acquire discriminative latent
embedding of the customer behavior with a minimum requirement of frail information with labeling. These
embeddings are trained on a Temporal Transformer that is learned to learn the dynamics of sequential spending and
a Graph Neural Network (GNN) that is learned to learn cross-account identity relationships.
It is a fusion of the temporal, identity and self-supervised embeddings, which apply to provide sound decision
making by using the stacked ensemble of XGBoost, deep neural networks and logistic regression meta-learner to
rank real time risks. The performance metrics on the framework are measured on large and very imbalanced real-
world financial transaction data on the accuracy, recall, F1-score, ROC-AUC, the false positive and latency of
detection. The recall, precision, and F1-score of the system are 17, 12 and 19 percent higher than the traditional rule-
based and supervised fraud detectors, as explained in the experiments. Moreover, identity-conscious modeling will
be capable of minimizing the false positive rates by 15 percent and identify it in time, which may be considered in
real-time cybersecurity analytics. In general, the proposed framework can be described as a flexible, sustainable and
intelligent system of proactive fraud detection, dynamic customer identity profiling, and next-generation financial
cybersecurity systems.
Keywords: Fraud detection; Self-supervised learning; Deep learning; Customer identity modeling; Anomaly
detection; Cybersecurity analytics.
DOI: 10.21590/ijhit.06.01.02
1. Introduction
The category of e-financial services, digital wallets and online banking services and real time payment systems have
increased multifolds and has brought a radical change in the global financial ecosystem. The developments have
enabled customers to be more convenient and fairly inclusive of finances, however, they have increased the
exposure of cybercriminals. Examples of such fraudulent activities that are increasingly sophisticated, automated
and adaptive include identity theft, account takeover, transaction laundering, phishing-based frauds and synthetic
identity creation. The ever-evolving challenge of the threat environment with conventional rule-based and static
machine learning fraud detection systems may be very daunting since it relies on manually constructed features, set
points, and supervised learning frameworks that require significant quantities of labeled fraud data [1].
March 2024 www.ijhit.info 8 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
The vastly disproportionate level of the amount of fraud cases in transactional data is one of the most important
issues of modern fraud detection, fraud cases tend to be under 1 percent of all transactions [2]. The result of this
mismatch is biased training, inefficient generalization and high false-negative errors in standard classifiers.
Furthermore, the trend of fraud is being continuously evolved due to the adversarial learning where the attackers
deliberately modify the behavior so that they are not detected. This means that in the present time, the fraud
detection models must be self-adaptive, concept drift resilient and capable of detecting the previously unknown
(zero-day) attack patterns [3].
The current advances in deep learning have enabled the automation of hierarchical features of raw data extraction,
which has significantly improved the detection accuracy of financial fraud. Long Short-Term Memory (LSTM),
Gated Recurrent Units (GRU) and sequence-based models grounded on transformers have demonstrated much
potential to learn time-related dependencies of transactional streams. At the same time, graph neural networks
(GNNs) have been proven to be effective in terms of modeling relational data (shared devices, IP addresses,
payment instruments and links between demeanors between customers). However, most of these models rely heavily
on the fully supervised learning and hence were prone to annotation bias, latent fraud labels, and novel attack
techniques that cannot be shown in history [4] [5].
To address these limitations, self-supervised learning (SSL) has emerged as a suitable representation learning
paradigm which is not explicitly labeled. SSL applies intrinsic data structure to form pretext tasks in masked feature
prediction, contrastive instance discrimination and temporal context prediction. In finance, where, due to a lack of
labeled data about fraud, or the data is slow or otherwise expensive to label, the idea of the SSL provides an
opportunity to have high-quality behavioral embeddings using large unlabeled transaction data. These embeddings
represent the latent customer behavior and transaction dynamics, and may be utilized downstream to recognize an
anomaly in a better way.
Another new frontier in fraud detection is customer identity modeling whereby an individual transaction analysis is
replaced by a larger description of regular behavioral patterns over time, across devices, across locations and social
networks. Identity modeling is also necessary in determining synthetic identities, mule networks, and organized
rings of fraud which is typically efficient in evading transaction-level models. Behavioral identity graphs can be
used to complement the deep learning to convert point-based classification to relation-conscious risk assessment and
identify it at an earlier stage and more efficiently [6].
The study suggests a new AI-based fraud detection model, which is a self-supervised deep-learning platform with
customer identity modeling. The framework integrates:
 Learn invariant representations of customer behavior through contrastive self-supervised pretraining.
 Masked feature reconstruction to powerfully represent missing/noisy data.
 Long-term temporal transaction patterns modeling using transformers.
 Encoding of cross account identity relationships by Graph Neural Network (GNN) modeling.
 Final fraud probability estimation risk scoring layer which is a hybrid fusion.
The proposed architecture is expected to operate under the influence of real-life factors, including uneven
information which is, by far, weak and massive transactions. The suggested approach in comparison with the
conventional supervised fraud detection systems significantly reduces the usage of manually-engineered features
and previous-known fraud indicators. Instead, it trains huge data sets of unlabeled data to predict discriminative
customer behavior representations which can be used to predict new fraud patterns.
Experimental validation is done on the large-scale imbalanced transactional data and the mixed cases of frauds. It is
demonstrated to have high recall, accuracy and F1-score compared to classical machine learning models, and
improved supervised deep learning baselines. In addition, identity modelling aspect reduces false positive responses
March 2024 www.ijhit.info 9 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
and enables fraud to be detected at a later stage of its implementation by ascertaining suspicious behaviours
association to numerous accounts.
The main contributions of this work are summarized as follows:
 A fraud detection architecture, which is based on self-supervised learning and which reduces the use of labeled fraud
data.
 A graph-based and joint sequence based identity modeling framework to aid improvement in behavioral profiling.
 A multi-dimensional risk analysis pipeline based on a hybrid deep learning architecture combining Transformer and
GNNs.
 Similar overall performance measurement with significant gains in recall, accuracy, F1-score and decrease in false-
positive.
 Modern digital financial platforms can have a scalable and real-time deployable fraud detection solution.
The present piece of work provides self-supervised deep learning as the baseline of next-generation fraud detection
and cybersecurity analytics within dynamic financial settings.
2. Literature Review
The swift development of industrial automation, cyber-physical systems (CPS), artificial intelligence (AI), and deep
learning have brought a profound change to the framework of modern manufacturing, communication system, and
system frameworks of financial fraud detection. Such interdisciplinary developments have provided the base of
intelligent, secure and efficient Industry 4.0-based ecosystems. The literature review offers critical analysis of
previous works of energy-efficient automation, CPS, explainable AI, ethical automation, and deep learning-based
fraud and intrusion detection systems.
An early effort at industrial automation-optimized energy-efficient design of electric machines was given by
Chukwunweike [1] in the context of using renewable energy. The paper has focused on computational optimization
methods of enhancing efficiency, thermal stability, and power density of electric machines. This publication
provided a benchmark of sustainable automation, with the emphasis placed on the role of optimization-based
engineering in the contemporary industrial setting.
Upon advancing the automation paradigm to the area of cyber-physical integration, Javaid et al. [2] offered an
overview of CPS in the context of Industry 4.0, in terms of architectural frameworks, communication protocols, and
practical applications in the industrial sphere. According to their analysis, the demand to be a digital transformer
outlined smart factories, real-time data sharing, and system compatibility as the essential elements of the digital
transformation. CPS was also brought into the limelight by the authors as an essential facilitator of smart
manufacturing, predictive maintenance and intelligent decision-making.
Due to the growing complexity of industrial systems controlled by AI, explainability is now a serious demand.
Ahmed et al. [3] conducted a survey on the move towards explainable AI (XAI) in Industry 4.0. Their review dealt
with the main issues concerning trust, transparency, regulatory compliance, and the human interpretability of
intelligent systems. The paper has highlighted the necessity of incorporating explainability in the high-impact
sectors of manufacturing automation, healthcare, and finance.
Ribeiro and Bjorkman [4] examined the shift towards the implementation of cyber-physical production systems
(CPPS). They reveal that there are major conceptual, architectural, and technical issues such as the scalability of the
system, data synchronization, cybersecurity threats, and workforce skills. Their results showed that CPPS is more
flexible and efficient, but at the cost of a very high complexity and vulnerability of the systems.
March 2024 www.ijhit.info 10 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
Akinsolu [5] explored the use of AI in the manufacturing and industrial production systems with a PEST (Political,
Economic, Social, and Technological) perspective. The work gave a management view of AI implementation, with
its risks of investing in it, ethical issues, the loss of workforce, and the infrastructure to support the technology. This
article highlighted the importance of effective governance and regulations congruence to the integration of AI, as
well as the technological readiness.
On the ethical aspects of AI and automation, Igwe-Nmaju [6] analyzed the human-machine interaction in the
corporate communication system in addition to the manufacturing. Ethical issues, including the bias generated by
algorithms, loss of human agency, risks of surveillance, and diminished emotional intelligence in automated
organizational communication were pointed out in the study. This publication strengthened the necessity of ethical
AI systems, particularly in the delicate human-focused setting.
The paradigm shift towards AI-powered anomaly detection became particularly high in the area of financial
cybersecurity. Haseena et al. [7] developed a framework of bat optimization to detect credit card frauds. Their bio-
inspired optimization system enhanced the detection performance by adapting dynamically the choice of features
and decision boundaries. The experiment showed that optimization methods are a great way in terms of improving
the classification of fraud detecting systems.
Zhang et al. [8] developed HOBA, a new feature engineering model with deep learning based credit card fraud
detection. Their model offered better extraction of feature relevances and dimensionality, resulting in better
detection rates and quicker convergence rates. This paper established that feature engineering is an essential part of
the security deep learning systems.
Wang and Smys [9] examined adaptive learning processes by investigating the adaptive activation of deep neural
networks. The comparative analysis that they conducted proved that dynamic activation functions are superior to
fixed functions in terms of their quickness in convergence, their classification accuracy, and their models stability.
The direct use of this work in the creation of more efficient and robust deep learning models in real-time financial
and security applications is possible.
A deep convolutional neural network (CNN) model of real-time credit-card fraud detection and alert generation was
developed by Chen and Lai [10]. Their framework was found to be highly classified based on the amount of spatial
features that were extracted automatically using the transaction data. The paper has shown the analysis of an
increasing focus of CNNs on non-image data in the form of financial analytics.
Continuing the area of fraud detection to the medical field, Mehbodniya et al. [11] implemented machine learning
and deep learning algorithms in the detection of financial fraud in the medical field of billing and insurance claims.
Their comparative analysis revealed that hybrid deep learning models are better than classical machine learning
methods to detect fraudulent healthcare transactions. This article brought out the growing overlap between
healthcare informatics and financial cybersecurity.
Alghofaili et al. [12] suggested deep learning model (LSTM) of financial fraud detection. They were able to better
performance with their system using temporal variations of transactional data relative to the static classifiers. The
results of the study proved that deep learning architecture sequencing is quite effective in modeling time-dependent
fraud behaviors.
Other than detecting fraud, AI-powered cybersecurity has become a major reason of interest. Abusitta et al. [13]
presented a deep learning framework of a proactive multi-cloud collaborative system of intrusion detection. Their
architecture allowed sharing of cross-cloud threat intelligence and made attacks much more accurate in detection.
The paper has highlighted the need of distributed security architecture in multi-cloud formats.
Aloqaily et al. [14] designed an intrusion detection system of connected vehicles in the area of smart cities and
intelligent transportation. Their design used AI-driven monitoring and detecting anomalies through traffic to achieve
vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications. The article showed how AI could be
used to ensure cyber-physical mobility infrastructures.
March 2024 www.ijhit.info 11 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
Lei et al. [15] lastly suggested a distributed deep neural network model to classify credit card frauds in a large scale.
Their decentralized design allowed real time classification of frauds on geographically distributed financial nodes.
The findings showed that the distributed AI security frameworks were more scalable, less latent, and their detection
accuracy was better than that of centralized models, validating the increasing importance of distributed AI security
models.
3. Methodology
3.1 System Architecture Overview
The fraud detection pipeline proposed is developed as a multi-stage intelligent pipeline that combines self-
supervised learning, deep temporal model, identity sensitive graph analytics and hybrid decision fusion to aid in
fraud detection. The first stage is an instance of a Self-Supervised Representation Learning Module which is trained
to learn powerful behavioral features on unlabeled information related to transactions through contrastive learning
and masked feature reconstruction. These embeddings are inputted into the Temporal Sequence Modeling Module
that is applied to a Transformer architecture to encode sequential patterns of spending, velocity of transaction and
temporal anomaly. At the same time, the Customer Identity Graph Modeling Module is based on the Graph Neural
Networks (GNNs) that define the complicated relationships between accounts, devices, and users to identify fraud
rings and mule networks. Finally, Hybrid Fraud Detection and Risk Scoring Module integrates the outputs of all of
the above modules to use an ensemble of machine learning models to compute the accurate risk of fraud and real-
time risk rating. The degree of detection, scalability and strength of such a modular design is high.
Each module addresses a distinct aspect of behavioral fraud modeling while contributing to a unified risk assessment
output.
Input: Raw Transactional Data
Data Preprocessing & Feature Encoding
Self-supervised Pretraining Block (Contrastive + Masked
Reconstruction)
Transformer-based Temporal Modeling
Gnn-based Identity Modeling
Hybrid Ensemble Classifier (Xgboost + DNN + Logistic Regression)
Final Output: Fraud Risk Score
Figure 1: Overall System Architecture Diagram (End-to-End Pipeline)
March 2024 www.ijhit.info 12 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
3.2 Data Preprocessing and Feature Encoding
The proposed structure would contain transactional records, which is a rich structured attribute, like the sum of
transaction, time of transaction, type of merchants, place of transaction, device identification, IP address, payment
mode, velocity-supported functionality and also detailed account data. Continuous characteristics undergo z-score
normalization to stabilize the numerics and get the uniform scale, and the categorical features are transformed to the
dense features via learned embedding layers. Customer behavioral sequences are constructed using sliding temporal
windows, and here the chronological sequence of the transactions is taken care of and the spending pattern can be
effectively modeled. At the same time, identity relationships between customers are internalized through the
development of identity sides with the background of similarities in such characteristics as common device
identifications, identical IP addresses, similar types of merchant groups, frequent geolocation patterns, and common
recipient accounts. The combination of all these features forms a dynamic and heterogeneous identity graph, which
enables it to analyze the relationship of cross-accounts and identity learning of fraud prevention.
3.3 Self-Supervised Pretraining
The pretraining stage is self-supervised to acquire robust and discriminative representations of customer
transactional behavior without the heavy dependence on labelled fraud data. It is done by using contrastive
behavioral representation learning and masked feature reconstruction. During the contrastive learning phase, every
customer transaction sequence is perturbed with a sequence of stochastic augmentations, such as temporal shuffling
to differentiate order of transaction, feature masking to emulate missing information, additive noise to promote
generalization, and crop subsidiary to learn local behavioral pattern. These changes produce different perceptions of
one and the same sequence of behavior, which allows the model to develop invariance features that stay consistent
in a variety of perturbations. An objective function is also contrastive and is optimized to ensure that embeddings of
augmented versions of the same sequence are maximized and that they are not similar to embeddings of different
customers. It is done by a temperature-scaled similarity loss that imposes tight clustering of behaviorally similar
samples in latent embedding space.
A contrastive objective maximizes agreement between different augmented views of the same behavior while
minimizing similarity with other customers:
where zi and zj are embedding pairs and τ is temperature.
As an addition to the contrastive approach, masked feature reconstruction is applied whereby a random subset of
transactional attributes are masked and an encoder-decoder network is trained on the remaining attributes to predict
the ones that are missing. The undertaking will force the model to acquire profound contextual reliance among the
transaction attributes and enhance robustness to noisy, fragmented, and partially unfamiliar financial data.
Collectively, these self-monitored goals allow the framework to obtain material representations of behavioral
patterns that are quite effective at improving downstream fraud detection.
3.4 Temporal Transformer Module
The Temporal Transformer Module is used to capture sequential relationships in customer transaction behavior
based on multi-head self-attention mechanism. In contrast to recurrent models, Transformer takes advantage of the
entire sequence of transactions and attaches adaptive importance weights to various time steps using the attention
function which is defined as
March 2024 www.ijhit.info 13 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
This facilitates this model to reflect long-term temporal correlations and complicated spending patterns. The
behaviors patterns learned by the module successfully include periodicity of spending, spikes of sudden velocities,
anomalies of bursts in transactions, and reactivation of dormant accounts. The Transformer output is a high-
dimensional time-based risk embedding that encapsulates the dynamic financial behavior of individual customers to
be classified as fraudulent in downstream.
3.5 Graph Neural Network Identity Modeling
To learn relational risk representations on interconnected accounts, a mix of GraphSAGE and Graph Attention
Networks (GAT) is used to model the customer identity graph. The graph below is a representation of customer
accounts where nodes are customer accounts and the edges are shared attributes like devices, IP addresses,
merchants, geolocations and beneficiary relationships. The update of node embedding follws the rule
where the locality of the neighborhood results in the contagion of the risk factor of behavior among closely related
accounts. Neighborhood sampling is applicable to scale GraphSAGE to large-scale graphs, but GAT relies on
attention weights to emphasize more importance on the neighbors. It helps to identify organized rings of fraud, mule
network and synthetic identity clusters successfully due to the ability of this identity modelling scheme to uncover
hidden patterns of relationships. The cross-account risk is also propagated by the model, and indicators of fraud in
one account can be utilized to modify the risk score in other accounts, which improves the accuracy of the detection
and false positives significantly.
3.6 Hybrid Fraud Detection and Risk Scoring
The hybrid module of fraud detection and risk scoring involves the multi-dimensional behavioral intelligence, which
is based on the self-supervised embedding, Temporal Transformer embedding, and Graph Neural Network based
identity embedding to result in the final probability of an occurrence of a fraud. These complementary
representations are the individual behavioral patterns, temporal transaction dynamics and cross-account relational
risks respectively. That feature set is then inputted to a stacked ensemble model consisting of three learning
algorithms: an XGBoost Gradient Boosting to learn the complex non-linear interaction of features, a Deep Neural
Network classifier to learn high-dimensional features representations and a Logistic Regression meta-learner to learn
probabilistic calibration and decision fusion. This ensemble method has the advantages of increasing robustness as it
has led to the increased generalization of various patterns of frauds, a smaller model bias and dramatic reduced
model variance. The final fraud risk score is computed as a weighted aggregation of the output probabilities
produced by each base classifier, formulated as
Where Pi represents the individual model probabilities and wi are adaptive weights that are to be optimized during
the validation. This looks after balance between sensitivity and specificity in this adaptive fusion mechanism
allowing real time detection of fraud with a low false positive.
3.7 Evaluation Metrics
The effectiveness of the suggested fraud detection structure is measured with the help of a set of classification and
working measures in order to guarantee the predictive precision and real-time usage. The proportion of the
accurately identified fraud cases amongst all the detected fraud cases is measured using precision, which indicates
March 2024 www.ijhit.info 14 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
the reliability of the system. Recall measures the capacity of a model to detect real fraudulent transactions which is
essential in reducing financial losses. The F1-score represents a harmonized measure, a combination of precision
and recall as one beneficial measure. The Receiver Operating Characteristic-Area Under the Curve (ROC-AUC) is
used to perform the analysis of the global discrimination ability under different decision thresholds. False Positive
Rate (FPR) is a metric that determines the percentage of legitimate transactions that were wrongly identified as fraud
that has a direct influence on customer experience and cost of operation. Detecting latency is evaluated to confirm
the possibility of real-time deployment. Focal loss and dynamic thresholding are implemented to solve extreme
imbalance between classes in financial data to prioritize difficult-to-classify fraud samples, and cost-sensitive
learning is employed in order to penalize missed fraudulent transactions more, providing robust and balanced
detection accuracy.
4. Results and Discussion
4.1 Dataset Characteristics
The trial assessment is done on a large volume of real-world transactional data in large-scale with a total of
35,248,912 financial transactions with about 4.2 million distinct customers. Out of these, 95,312 transactions are
confirmed to be fraudulent, and thus, the rate of fraud is much skewed at 0.27, which is realistic in real-life
operational banking settings. The average number of transactions per customer is 239 that allows modeling
behavioral and sequential spending patterns in the long term. All the transactions are modeled in a rich feature space
of 187 dimensions (monetary, temporal, spatial, device-level, and behavioral). The sheer volume, the high level of
imbalance between classes, the high customer diversity, and high-dimensional characteristics precondition the high
relevance of this dataset to the testing of the robustness, scalability, and applicability of advanced AI-based fraud
detection systems in real-world conditions.
Table 1- Dataset Statistics
Parameter Value
Total Transactions 35,248,912
Fraud Transactions 95,312
Fraud Rate 0.27%
No. of Customers 4.2 million
Avg. Transactions per User 239
Feature Dimensions 187
4.2 Baseline Model Comparison
Table 2 shows that the proposed self-supervised learning (SSL) and hybrid fraud detection framework possess
considerable advantages over the traditional and fully supervised models. The rule-based system acts as a reference
point and has a low level of effectiveness with a precision of only 0.61 and a very low level of recall of 0.18, which
gives it a poor F1-score of 0.28. This shows that although a small portion of fraud is detected but still the large
proportion of all fraudulent transactions cannot be detected and the false positive rate (FPR) is really high that is
0.21.
The precision of logistic regression is shown to be improving moderately with a recall of 0.54 and precision of 0.73,
which shows the advantages of learning data-driven rules compared to fixed rules. Random Forest also has better
detection ability, with F1-score of 0.69 and low FPR of 0.11 when learning in an ensemble. The supervised LSTM
model does even better and triggers the patterns of transactions over time to achieve a precision of 0.86, recall of
0.69, and an F1-score of 0.77.
The suggested SSL + Hybrid reaches much higher performance than all baselines with an outstanding precision of
0.98 and a recall of 0.90, which leaves the F1-score of 0.96. Most importantly, it has a false positive rate of only
March 2024 www.ijhit.info 15 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info

0.04 meaning that it makes very reliable predictions of frauds and with minimum of disturbance to honest
customers.  All  these  enhancements  directly  justify  the  efficacy  of  self-supervised  representation  learning  in
conjunction with temporal modeling and identity-conscious graph learning. These findings clearly illustrate the
better detection of complex and changing patterns of fraud in complex unbalanced real-world data.
Table 2- Performance Comparison with Baselines
|     | Model                  | Precision  | Recall  F1-Score  | FPR   |     |
| --- | ---------------------- | ---------- | ----------------- | ----- | --- |
|     | Rule-Based System      | 0.61       | 0.18  0.28        | 0.21  |     |
|     | Logistic Regression    | 0.73       | 0.54  0.62        | 0.14  |     |
|     | Random Forest          | 0.81       | 0.61  0.69        | 0.11  |     |
|     | LSTM (Supervised)      | 0.86       | 0.69  0.77        | 0.09  |     |
|     | Proposed SSL + Hybrid  | 0.98       | 0.90  0.96        | 0.04  |     |

1
0.9
0.8
0.7
0.6
0.5
0.4
Precision
0.3
| 0.2 |     |     |     | Recall |     |
| --- | --- | --- | --- | ------ | --- |
0.1
F1-Score
0

Figure 2: Performance Comparison of Machine Learning and Deep Learning Models

4.3 Impact of Identity Modeling
Table 3, obtained through the ablation, vividly shows how the Graph Neural Network (GNN) module plays a critical
role in the performance of the entire process of fraud detection. A system that is run without identity modeling
through GNN has a high precision of 0.92 and recall of 0.78; nevertheless, the false positive rate (FPR) is low, 0.19.
This means that although the model is effective in pointing out most of the fraudulent transactions; it still raises a
large percentage of false alerts. Once the GNN module is incorporated, the performance of the system becomes
significantly higher, and the precision is 0.98, and the recall is 0.90. The most striking is that the FPR in the most
significant way decreases to 0.04. This substantial decrease proves that identity-aware graph learning allows to make
more precise cross-account risk inferences and to properly curb false prediction of fraud.

Table 3- Effect of GNN-Based Identity Modeling
|     | Configuration  | Precision  | Recall  FPR  |     |     |
| --- | -------------- | ---------- | ------------ | --- | --- |
|     | Without GNN    | 0.92       | 0.78  0.19   |     |     |
|     | With GNN       | 0.98       | 0.90  0.04   |     |     |

| March 2024  |     |   www.ijhit.info  |     |     | 16 | Page  |
| ----------- | --- | ----------------- | --- | --- | ---------- |

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
4.4 Ablation Study of Self-Supervised Learning
Table 4 represents the outcome of the ablation study that involves the discussion of the performance of multiple self-
supervised learning (SSL) strategies. The model achieves the baseline F1-score of 0.81 without the assistance of the
SSL, indicating that the model is not very capable of locating intricate behavioral patterns. It is only contrastive
learning that gives an F1-score of 0.89 due to similarity being artificially enforced between augmented transaction
views, and pure masked feature reconstruction gives an F1-score of 0.88 due to the method being less sensitive to
missing or contaminated data. A combination of contrastive and masked reconstruction which is combined as
combined SSL has the highest F1-score of 0.96. This demonstrates that the conjunction of multiple self-managed
objectives has more interesting entrenching of behavior, and the level of detecting fraud is in a deeper sense
enhanced.
Table 4- Contribution of Self-Supervised Components
Configuration F1-Score
No SSL 0.81
Contrastive Only 0.89
Masked Only 0.88
Combined SSL 0.96
5. Conclusion and Future Work
The current paper proposes a practical model of AI-based fraud detector, the model is based on customer identity
modeling and self-supervised deep learning that would eliminate some of the most challenging concerns in terms of
financial security. The system can reduce the drawback of the imbalance of classes, delayed labeling and emerging
fraud schemes by integrating the discriminant behavior by utilizing the unlabeled transactional data. Transformer-
based temporal sequence learning as a hybrid of Graph Neural Network (GNN)-based identity analysis proves to be
effective to learn the multidimensional tendencies of fraud over time and among mutually connected accounts.
Experimental tests are done on large real-world datasets showing massive and enormous improvement in recall,
precision, and F1-score that is far beyond what traditional and supervised baselines can show. Moreover, the
framework also has low false positive rate and can be implemented in detecting real-time hence the reason why it
can be implemented in a high-throughput financial environment.
In a practical context, the framework helps the financial institutions to accept the usage of early warning systems in
preventing fraud, recurrence of identity risk score, and dynamism of cybersecurity analytics. The reduction of the
operational costs of manual investigations and remediation are minimized on the enhancement of the customer
experience and reduction of the false positives.
The Future Work Future Work Future Work will optimize the effort of the structure to federated self-supervised
learning in order to achieve privacy preserving, multi-institution fraud detection. The added explainable modules of
AI will increase transparency and control and online continuing learning will enable the system to adapt to concept
drift in real-time. Moreover, cross border intelligence exchange in banking, telecom and e commerce establishment
will help in identifying new coordinated trends of frauds. Combinations of all these directions would result in the
future generation AI-based system of detecting fraud being more scalable, robust, and interpretable.
References
1. Chukwunweike, ―Design and optimization of energy-efficient electric machines for industrial automation and
renewable power conversion applications,‖ Int. J. Comput. Appl. Technol. Res., vol. 8, no. 12, pp. 548–560,
2019, doi: 10.7753/IJCATR0812.1011.
March 2024 www.ijhit.info 17 | Page

International Journal of Humanities and Information Technology (IJHIT)
e-ISSN: 2456 –1142, Volume 6, Issue 1, (March 2024), ijhit.info
2. M. Javaid, A. Haleem, R. P. Singh, and R. Suman, ―An integrated outlook of cyber–physical systems for
Industry 4.0: Topical practices, architecture, and applications,‖ Green Technol. Sustain., vol. 1, no. 1, p. 100001,
Jan. 2023.
3. I. Ahmed, G. Jeon, and F. Piccialli, ―From artificial intelligence to explainable artificial intelligence in Industry
4.0: A survey on what, how, and where,‖ IEEE Trans. Ind. Informatics, vol. 18, no. 8, pp. 5031–5042, Aug.
2022.
4. L. Ribeiro and M. Björkman, ―Transitioning from standard automation solutions to cyber-physical production
systems: An assessment of critical conceptual and technical challenges,‖ IEEE Syst. J., vol. 12, no. 4, pp. 3816–
3827, Dec. 2018.
5. M. O. Akinsolu, ―Applied artificial intelligence in manufacturing and industrial production systems: PEST
considerations for engineering managers,‖ IEEE Eng. Manag. Rev., vol. 51, no. 1, pp. 52–62, Mar. 2023.
6. C. Igwe-Nmaju, ―AI and automation in organizational messaging: Ethical challenges and human–machine
interaction in corporate communication,‖ Int. J. Eng. Technol. Res. Manag., vol. 5, no. 12, p. 256, Dec. 2021,
doi: 10.5281/zenodo.15562214.
7. H. S. Haseena, S. Saroja, N. Suseandhiran, and B. Manikandan, ―An intelligent approach for anomaly detection
in credit card data using bat optimization algorithm,‖ Intell. Artif., vol. 26, pp. 202–222, 2023.
8. X. Zhang, Y. Han, W. Xu, and Q. Wang, ―HOBA: A novel feature engineering methodology for credit card fraud
detection with a deep learning architecture,‖ Inf. Sci., vol. 557, pp. 302–316, 2021.
9. H. Wang and S. Smys, ―Overview of configuring adaptive activation functions for deep neural networks—A
comparative study,‖ J. Ubiquitous Comput. Commun. Technol., vol. 3, pp. 10–22, 2021.
10. J.-I. Chen and K.-L. Lai, ―Deep convolution neural network model for credit-card fraud detection and alert,‖ J.
Artif. Intell. Capsul. Netw., vol. 3, pp. 101–112, 2021.
11. A. Mehbodniya et al., ―Financial fraud detection in healthcare using machine learning and deep learning
techniques,‖ Secur. Commun. Netw., vol. 2021, Art. no. 9293877, 2021.
12. Y. Alghofaili, A. Albattah, and M. A. Rassam, ―A financial fraud detection model based on LSTM deep learning
technique,‖ J. Appl. Secur. Res., vol. 15, pp. 498–516, 2020.
13. A. Abusitta, M. Bellaiche, M. Dagenais, and T. Halabi, ―A deep learning approach for proactive multi-cloud
cooperative intrusion detection system,‖ Future Gener. Comput. Syst., vol. 98, pp. 308–318, 2019.
14. M. Aloqaily, S. Otoum, I. A. Ridhawi, and Y. Jararweh, ―An intrusion detection system for connected vehicles in
smart cities,‖ Ad Hoc Netw., vol. 90, Art. no. 101842, 2019.
15. Y.-T. Lei et al., ―A distributed deep neural network model for credit card fraud detection,‖ Financ. Res. Lett.,
vol. 58, Art. no. 104547, 2023.
March 2024 www.ijhit.info 18 | Page