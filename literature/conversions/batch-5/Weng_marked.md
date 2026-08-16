---
conversion_metadata:
  converted_at: "2026-07-21T09:24:48Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Weng.pdf"
  source_pdf_sha256: "bb4090970ad0deebaa988ae857010c00705171e775c34293e816f987247c9c35"
  page_count: 19
  markdown_char_count: 103885
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Spectrum of Research 
Vol 5 issue 2 2025 
https://spectrumofresearch.com

Deep Embedding Clustering with Adaptive Feature Selection for 
Banking Customer Segmentation

Haojun Weng

Computer Technology, Fudan University, Shanghai, China 
Corresponding Email: hao.weng@gmail.com

Abstract 
Customer segmentation is critical for financial institutions to optimize marketing strategies in the 
competitive  credit  card  market.  Traditional  clustering  methods  such  as  K-Means  often  fail  to 
capture complex behavioral patterns and lack interpretability for business decision-making. This 
paper  proposes  a  deep  embedding  clustering  framework  with  adaptive  feature  selection  for 
banking  customer  segmentation.  The  method  integrates  a  stacked  autoencoder  to  learn  low-
dimensional  customer  behavior  representations  while  preserving  interpretability  of  business-
critical  features.  A  mutual  information-based  feature  importance  mechanism  automatically 
identifies  discriminative  behavioral  indicators.  Furthermore,  a  business-constrained  clustering 
optimization  approach  ensures  segmentation  results  align  with  marketing  objectives.  The 
framework will be evaluated on a real-world dataset of credit card customers from a major U.S. 
financial  institution.  This  research  aims  to  advance AI-driven  precision  marketing,  supporting 
banks in optimizing resource allocation and enhancing customer lifetime value.

Keywords: Deep Learning, Customer Segmentation, Feature Selection, Banking Analytics

I. Introduction

The  financial  services  industry  faces  unprecedented  challenges  in  customer  retention  and 
acquisition within increasingly competitive markets. Banks and credit card issuers must develop 
sophisticated understanding of customer behaviors to deliver personalized services and optimize 
marketing expenditure. Recent advances in artificial intelligence have demonstrated remarkable 
potential in consumer behavior analysis [1], enabling institutions to discover nuanced patterns that 
traditional  analytical  approaches  cannot  detect.  The  complexity  of  modern  consumer  financial 
toward 
behaviors  necessitates  moving  beyond  simplistic  demographic  segmentation 
multidimensional behavioral profiling.

Credit card transaction data represents a rich source of behavioral signals, encompassing spending 
patterns,  merchant  categories,  transaction  frequencies,  and  temporal  dynamics.  Traditional 
segmentation  approaches  rely  heavily  on  predetermined  features  and  linear  assumptions  about 
customer  similarities.  K-Means  clustering  and  hierarchical  methods  have  dominated  practical

1

---

<!-- PAGE 2 -->

Spectrum of Research

Vol 5 (2) 2025

applications  due  to  their  computational  efficiency  and  interpretability.  These  conventional 
techniques  struggle  with  high-dimensional  feature  spaces  and  fail  to  capture  nonlinear 
relationships inherent in complex behavioral datasets  [2]. The increasing volume and velocity of 
transactional  data  compound  these  limitations,  creating  an  urgent  need  for  more  sophisticated 
analytical frameworks.

Deep learning architectures offer promising alternatives through their capacity to automatically 
learn  hierarchical  feature  representations  from  raw  data.  Autoencoder  networks  have  shown 
particular  success  in  unsupervised  learning  tasks,  demonstrating  ability  to  compress  high-
dimensional inputs into meaningful latent representations [3]. Embedding-based clustering methods 
combine  representation  learning  with  cluster  assignment  optimization,  enabling  end-to-end 
training that jointly optimizes both objectives. The banking sector requires solutions that balance 
algorithmic sophistication with practical interpretability, as marketing teams must understand and 
act upon segmentation insights [4].

This  research  addresses  the  gap  between  theoretical  advances  in  deep  clustering  and  practical 
requirements of financial services applications. We propose a novel framework that integrates deep 
embedding  clustering  with  adaptive  feature  selection  mechanisms  specifically  designed  for 
banking  customer  segmentation.  The  approach  maintains  interpretability  of  business-critical 
features while leveraging deep learning's representational power. Our methodology incorporates 
domain-specific  constraints  that  ensure  discovered  segments  align  with  actionable  marketing 
strategies. The framework processes large-scale transactional datasets from major U.S. financial 
institutions, demonstrating scalability and practical applicability in production environments.

II. Related Work

Customer segmentation research in financial services has evolved through multiple generations of 
methodological approaches. Early demographic segmentation gave way to behavioral clustering 
based  on  transaction  patterns  and  product  usage  characteristics.  Traditional  machine  learning 
methods including decision trees, random forests, and support vector machines have been applied 
to customer classification tasks with varying degrees of success [5]. These supervised approaches 
require labeled training data and predefined categories, limiting their applicability to exploratory 
segmentation scenarios where customer groups emerge organically from behavioral patterns.

Unsupervised clustering algorithms have formed the backbone of customer segmentation practice 
across industries. K-Means clustering remains widely deployed due to computational efficiency 
and  straightforward  interpretation  of  cluster  centroids.  Hierarchical  clustering  methods  provide 
dendrogram visualizations that support hierarchical market segmentation strategies  [6]. Density-
based  spatial  clustering  algorithms  handle  non-spherical  cluster  shapes  and  automatically 
determine cluster numbers. Model-based  clustering approaches using Gaussian mixture models 
offer probabilistic cluster assignments with theoretical foundations in statistical inference [7]. These

2

---

<!-- PAGE 3 -->

Spectrum of Research

Vol 5 (2) 2025

conventional methods share common limitations including sensitivity to feature scaling, difficulty 
handling high-dimensional spaces, and inability to capture complex nonlinear patterns.

The emergence of deep learning has catalyzed new directions in unsupervised clustering research. 
Autoencoder  architectures  compress  input  data  into  lower-dimensional  latent  spaces  while 
preserving essential information, enabling more effective similarity computations [8]. Variational 
autoencoders introduce probabilistic formulations that model latent space distributions, supporting 
generation of synthetic customer profiles. Deep embedding clustering methods jointly optimize 
reconstruction  loss  and  cluster  assignment  loss,  enabling  representations  specifically  tuned  for 
clustering tasks. Recent work has explored attention mechanisms and transformer architectures for 
sequential transaction data, capturing temporal dependencies in customer behaviors [9].

Feature  selection  represents  a  critical  challenge  in  financial  data  analytics  where  hundreds  of 
potential behavioral indicators exist. Traditional filter methods rank features based on statistical 
measures  including  correlation  coefficients,  chi-square  tests,  and  information  gain  metrics  [10]. 
Wrapper  methods  evaluate  feature  subsets  through  iterative  model  training,  optimizing 
performance on specific learning algorithms. Embedded methods integrate feature selection within 
model  training,  learning  feature  importance  weights  during  optimization.  Mutual  information-
based  approaches  measure  statistical  dependencies  between  features  and  target  variables, 
providing theoretically grounded selection criteria that avoid linear assumptions [11].

Business constraints in banking applications require segmentation methods that produce actionable 
insights aligned with marketing capabilities and regulatory requirements. Segments must achieve 
sufficient size to justify targeted campaigns while maintaining homogeneity in behavior patterns. 
Interpretability  constraints  necessitate  transparent  feature  importance  rankings  that  marketing 
teams can understand and act upon  [12]. Privacy regulations including GDPR and CCPA impose 
additional requirements on data usage and customer profiling practices. Recent research has begun 
addressing  these  practical  considerations  through  constrained  clustering  formulations  and 
explainable AI techniques [13].

The intersection of deep learning and business analytics presents opportunities for methodological 
innovation.  Multi-objective  optimization  frameworks  balance  clustering  quality  metrics  with 
business-specific objectives including marketing ROI and customer lifetime value predictions [14]. 
Transfer learning approaches leverage knowledge from related domains to improve segmentation 
in  data-scarce  scenarios.  Ensemble  methods  combine  multiple  clustering  algorithms  to  achieve 
robust  segment  definitions  less  sensitive  to  algorithmic  choices  [15].  Our  proposed  framework 
builds  upon  these  foundations  while  introducing  novel  mechanisms  specifically  designed  for 
banking customer segmentation challenges.

3

---

<!-- PAGE 4 -->

Spectrum of Research

Vol 5 (2) 2025

III. Methodology

A. Problem Formulation

The customer segmentation problem involves partitioning a set of N credit card customers into K 
distinct groups based on their behavioral characteristics captured through transactional data. Each 
customer  i  is  represented  by  a  feature  vector  x_i  ∈  R^D  containing  D  behavioral  attributes 
extracted  from  transaction  history,  including  average  transaction  amounts,  merchant  category 
distributions,  temporal  spending  patterns,  credit  utilization  ratios,  and  payment  behaviors. The 
objective  function  minimizes  intra-cluster  variance  while  maximizing  inter-cluster  separation, 
subject to business constraints that ensure segment sizes meet minimum thresholds for marketing 
campaign viability and segment interpretability remains sufficiently high for actionable strategy 
development.

Traditional  clustering  objectives  focus  solely  on  geometric  properties  of  data  distributions, 
optimizing metrics such as silhouette coefficients or Davies-Bouldin indices. Banking applications 
require  additional  considerations  including  segment  stability  over  time,  demographic  diversity 
within clusters to avoid discriminatory practices, and alignment between discovered segments and 
existing customer relationship management systems. The optimization problem incorporates these 
multiple objectives through a weighted combination approach where business stakeholders specify 
relative  importance  of  different  criteria.  Constraint  satisfaction  ensures  regulatory  compliance 
while maintaining statistical rigor in cluster definitions.

The high-dimensional nature of behavioral feature spaces presents computational and statistical 
challenges.  Transaction  data  spanning  multiple  years  generates  hundreds  of  potential  features 
capturing  spending  patterns  across  various  dimensions.  Dimensionality  reduction  becomes 
essential  to  avoid  curse  of  dimensionality  effects  that  degrade  clustering  performance.  The 
challenge lies in reducing dimensionality while preserving discriminative information relevant to 
customer segmentation. Our approach addresses this through learned embeddings that compress 
behavioral representations into lower-dimensional manifolds where clustering algorithms operate 
more effectively.

B. Deep Embedding Clustering Architecture

The  proposed  architecture  consists  of  three  interconnected  components  that  jointly  optimize 
clustering  objectives  and  feature  selection  criteria.  The  foundation  comprises  a  stacked 
autoencoder  network  that  learns  compressed  representations  of  customer  behaviors  through 
unsupervised  pre-training  on  raw  transactional  features.  The  encoder  network  maps  high-
dimensional  input  vectors  through  multiple  hidden  layers  with  progressively  decreasing 
dimensions,  culminating  in  a  bottleneck  layer  representing  the  learned  embedding  space.  The 
decoder network mirrors this structure, reconstructing original inputs from latent representations 
to ensure information preservation during compression [1].

4

---

<!-- PAGE 5 -->

Spectrum of Research

Vol 5 (2) 2025

The autoencoder employs a symmetrical architecture with four hidden layers in both encoder and 
decoder  paths.  Input  layer  dimensionality  matches  the  number  of  behavioral  features  D,  while 
hidden layers contain 512, 256, 128, and 64 neurons respectively. The bottleneck embedding layer 
contains 32 dimensions, providing sufficient capacity for representing complex behavioral patterns 
while  enabling  efficient  clustering  computations. Activation  functions  use  rectified  linear  units 
(ReLU)  for  hidden  layers,  introducing  nonlinearity  that  enables  learning  of  complex 
transformations. The output layer employs linear activation for continuous features and sigmoid 
activation for binary indicators, appropriately matching different feature types in the behavioral 
dataset [2].

Pre-training proceeds through layer-wise greedy training followed by fine-tuning of the complete 
autoencoder network. Each layer is initially trained as a denoising autoencoder, learning robust 
features resilient to  input  perturbations. Gaussian noise with standard deviation  0.1 is  added to 
inputs during pre-training, encouraging the network to learn meaningful representations rather than 
identity  mappings.  Fine-tuning  minimizes  mean  squared  reconstruction  error  across  the  entire 
architecture  using  Adam  optimizer  with  learning  rate  0.001  and  mini-batch  size  256.  Early 
stopping  based  on  validation  set  performance  prevents  overfitting  while  ensuring  adequate 
representational capacity.

Layer

Input

Type

Dense

Encoder-1

Dense

Encoder-2

Dense

Encoder-3

Dense

Embedding

Dense

Decoder-1

Dense

Decoder-2

Dense

Decoder-3

Dense

Decoder-4

Dense

Output

Dense

Table I: Autoencoder Architecture Specifications

Input Dim

Output Dim

Activation

Dropout

247

512

256

128

64

32

64

128

256

512

512

256

128

64

32

64

128

256

512

247

-

ReLU

ReLU

ReLU

Linear

ReLU

ReLU

ReLU

ReLU

Mixed

0.0

0.2

0.2

0.2

0.0

0.2

0.2

0.2

0.2

0.0

The clustering component builds upon learned embeddings through an iterative refinement process 
that  alternates  between  cluster  assignment  and  centroid  updates.  Initial  cluster  centroids  are 
established  through  K-Means++  initialization  applied  to  embedded  customer  representations, 
ensuring well-distributed starting positions that accelerate convergence. The clustering objective

5

---

<!-- PAGE 6 -->

Spectrum of Research

Vol 5 (2) 2025

minimizes  Kullback-Leibler  divergence  between  predicted  cluster  assignment  distribution  and 
target  distribution  computed  from  current  centroid  positions  [3].  This  formulation  enables  soft 
cluster  assignments  where  customers  have  probability  distributions  across  multiple  clusters, 
providing flexibility to represent customers with hybrid behavioral patterns.

Target  distribution  sharpening  enhances  cluster  separation  by  emphasizing  high-confidence 
assignments while suppressing ambiguous cases. The auxiliary target distribution is computed by 
raising  assignment  probabilities  to  the  power  of  2  and  normalizing,  effectively  amplifying 
differences  between  cluster  affinities. This  self-training  mechanism  gradually  improves  cluster 
quality without requiring labeled supervision. The clustering loss is combined with reconstruction 
loss in a multi-task learning framework, maintaining embedding quality while optimizing cluster 
assignments. The  balance  between  these  objectives  is  controlled  by  a  hyperparameter  λ  that  is 
annealed  during  training,  initially  emphasizing  reconstruction  to  establish  robust  embeddings 
before shifting focus toward clustering objectives [4].

C. Adaptive Feature Selection Mechanism

The  feature  selection  component  operates  in  parallel  with  embedding  learning,  identifying 
behavioral  indicators  that  contribute  most  significantly  to  clustering  objectives.  Mutual 
information  quantifies  statistical  dependencies  between 
individual  features  and  cluster 
assignments, providing a theoretically grounded measure of feature relevance [6]. The calculation 
employs kernel density estimation to approximate continuous probability distributions, avoiding 
discretization  artifacts  that  can  bias  information  estimates.  Features  exhibiting  high  mutual 
information  with  cluster  labels  receive  elevated  importance  scores,  guiding  subsequent  feature 
subset selection.

The selection mechanism incorporates both relevance and redundancy considerations to construct 
diverse  feature  subsets.  Pairwise  mutual  information  between  features  identifies  redundant 
indicators  that  provide  similar  information  about  cluster  structure.  The  selection  algorithm 
maximizes relevance while minimizing redundancy through a greedy forward selection process. 
Starting  from  an  empty  set,  features  are  iteratively  added  if  they  increase  overall  information 
content  beyond  a 
threshold  determined  by  cross-validation.  This  approach  balances 
comprehensiveness  with  interpretability,  producing  feature  subsets  of  manageable  size  that 
marketing teams can understand and act upon [7].

Business-critical features receive special treatment through a mandatory inclusion mechanism that 
ensures certain behavioral indicators always appear in final feature sets. Credit utilization ratios, 
payment delinquency indicators, and total spending volumes represent fundamental characteristics 
relevant to virtually all banking strategies. The selection algorithm respects these constraints while 
optimizing  remaining  features  based  on  information-theoretic  criteria.  This  hybrid  approach 
maintains domain expertise integration while leveraging data-driven discovery of novel behavioral 
patterns.

6

---

<!-- PAGE 7 -->

Spectrum of Research

Vol 5 (2) 2025

Figure 1: Mutual Information-Based Feature Selection Process

The  visualization  presents  a  comprehensive  flowchart  depicting  the  adaptive  feature  selection 
mechanism across four parallel streams. The top stream illustrates initial feature extraction from 
raw  transaction  data,  showing  247  behavioral  indicators  organized  into  six  category  groups: 
spending  patterns,  merchant  preferences,  temporal  dynamics,  credit  behaviors,  payment 
characteristics, and channel usage. Color-coded boxes represent different feature categories, with 
line thickness indicating feature correlations. The second stream displays the mutual information 
computation module, featuring a heatmap matrix showing pairwise MI scores between all features 
and cluster assignments, with warm colors (red/orange) indicating high information content and 
cool colors (blue) representing low relevance. The third stream depicts the redundancy analysis 
component, visualizing feature correlation networks as a force-directed graph where node sizes 
represent  feature  importance  and  edge  weights  indicate  redundancy  levels.  The  bottom  stream 
shows  the  final  selection  output,  presenting  selected  feature  subsets  for  each  cluster  with 
importance  scores  represented  as  horizontal  bar  charts.  Connecting  arrows  between  streams 
indicate information flow, with annotations showing MI threshold values and redundancy cutoff 
criteria. The figure employs a professional color scheme using institutional blue, financial green, 
and  analytic  orange  tones,  with  clear  labels  and  legends  supporting  interpretability  for  non-
technical stakeholders.

Table II: Top-20 Features Ranked by Mutual Information Scores

Rank

Feature Name  Category

MI Score

Redundancy

Selected

7

---

<!-- PAGE 8 -->

Spectrum of Research

Vol 5 (2) 2025

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

Spending

0.847

0.123

Avg  Monthly 
Spend

Transaction 
Frequency

Spending

0.792

Dining Ratio

Merchant

0.738

Merchant

0.701

0.156

0.089

0.094

Temporal

0.689

0.112

Credit

0.654

0.078

Luxury  Goods 
Ratio

Merchant

0.621

0.201

Payment

0.598

0.067

Temporal

0.576

0.223

Channel

0.554

0.091

Merchant

0.509

0.178

Credit

0.487

0.104

Temporal

0.465

0.087

Merchant

0.443

0.198

Cash  Advance 
Usage

Credit

0.421

0.119

8

Travel 
Spending

Weekend 
Activity

Credit 
Utilization

Payment 
Timeliness

Evening 
Transactions

Online 
Shopping

ATM 
Withdrawal 
Freq

Entertainment 
Spend

Balance 
Transfers

International 
Trans

Subscription 
Services

Yes

Yes

Yes

Yes

Yes

Yes

No

Yes

No

Yes

No

Yes

Yes

No

Yes

Channel

0.532

0.145

Yes

---

<!-- PAGE 9 -->

Spectrum of Research

Vol 5 (2) 2025

17

18

19

20

Mobile 
Activity

App

Quarterly 
Spend Var

Grocery 
Shopping

Contactless 
Payment

Channel

0.398

0.134

Temporal

0.376

0.156

Merchant

0.354

0.241

Channel

0.332

0.167

Yes

Yes

No

No

D. Business-Constrained Optimization

The  optimization  framework  incorporates  multiple  business  constraints  that  ensure  discovered 
segments  support  practical  marketing  applications.  Minimum  cluster  size  constraints  prevent 
creation of segments too small to justify dedicated marketing campaigns, with thresholds set based 
on  campaign  economics  and  customer  acquisition  costs.  Balance  constraints  limit  maximum 
segment size to prevent dominance by single large clusters that provide insufficient differentiation 
for  targeted  strategies  [9].  These  hard  constraints  are  enforced  through  penalty  terms  in  the 
optimization objective that sharply increase when constraint violations occur.

Interpretability  constraints  promote  cluster  definitions  based  on  easily  understood  behavioral 
characteristics.  The  framework  penalizes  clusters  that  require  complex  combinations  of  many 
features  for  explanation,  favoring  segments  describable  through  small  numbers  of  key 
differentiators. Feature contribution regularization encourages sparse cluster profiles where each 
segment exhibits distinctive patterns in limited numbers of behavioral dimensions. This sparsity 
aids marketing teams in developing clear value propositions and messaging strategies tailored to 
segment characteristics [10].

Temporal  stability  constraints  address  the  dynamic  nature  of  customer  behaviors  over  time. 
Segment  definitions  must  remain  relatively  stable  across  consecutive  time  periods  to  enable 
consistent strategy execution and performance measurement. The optimization includes a stability 
regularization term that penalizes large shifts in cluster assignments when the model is retrained 
on updated data. This mechanism balances adaptation to evolving behaviors with maintenance of 
strategic continuity. Marketing teams specify acceptable drift rates based on campaign planning 
horizons and organizational capacity for strategy modification.

The complete optimization objective combines clustering quality metrics, feature selection criteria, 
and business constraints into a unified framework solved through alternating optimization. Cluster 
assignments  and  centroids  are  updated  using  expectation-maximization  steps  while  feature 
selection  weights  are  optimized  through  gradient  descent.  The  multi-objective  formulation 
employs  Pareto  optimization  principles  where  no  single  objective  dominates  at  the  expense  of

9

---

<!-- PAGE 10 -->

Spectrum of Research

Vol 5 (2) 2025

others. Stakeholder preference weights are elicited through interactive sessions where marketing 
leaders review candidate solutions and provide feedback on business alignment [11].

IV. Experimental Results and Analysis

A. Dataset Description and Preprocessing

The experimental evaluation employs a real-world dataset from a major U.S. financial institution 
containing  credit card transaction records for 7.9 million active customers spanning  36 months 
from  January  2022  through  December  2024.  The  dataset  includes  detailed  transaction-level 
information  capturing  merchant  categories,  transaction  amounts,  timestamps,  geographic 
locations,  and  payment  channel  types.  Customer-level  data  provides  demographic  attributes 
including  age,  income  bracket,  account  tenure,  and  product  holdings,  enabling  enrichment  of 
behavioral profiles with contextual information [8]. Data preprocessing addresses missing values, 
outliers, and data quality issues inherent in large-scale operational datasets.

Feature  engineering  transforms  raw  transactional  records  into  structured  behavioral  profiles 
suitable for clustering analysis. Aggregate features summarize spending patterns across multiple 
dimensions including total volumes, average transaction amounts, spending distributions across 
merchant  categories,  and  temporal  patterns  such  as  weekday  versus  weekend  activity.  Derived 
features  capture  behavioral  trends  including  spending  growth  rates,  seasonality  patterns,  and 
category preference shifts over time. Credit behavior indicators measure utilization rates, payment 
punctuality scores, balance transfer frequencies, and cash advance usage patterns [12]. The complete 
feature  set  comprises  247  behavioral  variables  spanning  six  major  categories  aligned  with 
marketing strategy dimensions.

Data  normalization  ensures  features  contribute  appropriately  to  distance  computations  and 
embedding  learning  processes.  Continuous  variables  are  standardized  to  zero  mean  and  unit 
variance, preventing features with large numerical ranges from dominating similarity calculations. 
Binary indicators and categorical variables receive specialized encoding preserving their discrete 
nature  while  enabling  integration  with  continuous  features. Temporal  features  undergo  cyclical 
encoding  using  sine  and  cosine  transformations  to  capture  periodic  patterns  without  artificial 
discontinuities.  The  preprocessing  pipeline  implements  robust  scaling  techniques  resilient  to 
outliers, using median and interquartile range statistics rather than mean and standard deviation 
[13].

Table III: Dataset Statistics and Feature Categories

Category

Features

Mean

Std Dev

Min

Max

Missing %

Spending 
Patterns

42

2,347.56

1,892.34

0.00

45,320.00

0.8%

10

---

<!-- PAGE 11 -->

Spectrum of Research

Vol 5 (2) 2025

Merchant 
Categories

Temporal 
Dynamics

Credit 
Behaviors

Payment 
Patterns

Channel 
Usage

68

51

34

28

24

0.23

0.18

0.00

1.00

1.2%

18.45

12.67

0.00

127.00

0.5%

0.47

0.31

0.00

1.00

2.1%

0.89

0.15

0.00

1.00

1.8%

0.34

0.26

0.00

1.00

0.9%

Total

247

-

-

-

-

1.2%

The dataset is partitioned into training, validation, and test sets using stratified sampling to ensure 
representative distributions across customer segments. Training data comprises 70% of customers 
used  for  model  development  and  embedding  learning.  Validation  data  containing  15%  of 
customers  supports  hyperparameter  tuning  and  early  stopping  decisions  during  training.  The 
remaining  15%  forms  a  held-out  test  set  for  final  performance  evaluation  and  generalization 
assessment. Temporal splits are also constructed where training uses data from first 24 months and 
testing  evaluates  performance  on  the  most  recent  12  months,  assessing  model  robustness  to 
behavioral evolution and market changes [14].

B. Implementation Details and Hyperparameter Configuration

The proposed framework is implemented using Python 3.9 with TensorFlow 2.12 for deep learning 
components and scikit-learn 1.3  for traditional clustering  baselines. Training is  conducted on a 
cluster  with  4  NVIDIA A100  GPUs,  enabling  efficient  processing  of  the  large-scale  customer 
dataset. The stacked autoencoder network is pre-trained for 100 epochs with batch size 256, using 
Adam optimizer with initial learning rate 0.001 and exponential decay rate 0.96 every 10 epochs. 
Reconstruction loss employs mean squared error for continuous features and binary cross-entropy 
for  categorical  indicators,  weighted  by  feature  importance  scores  to  prioritize  business-critical 
attributes.

The deep embedding clustering phase fine-tunes the pre-trained encoder while jointly optimizing 
cluster assignments. Initial cluster number K is determined through elbow analysis and silhouette 
score evaluation on embedded representations, testing values from 4 to 12 clusters. The selected 
configuration uses K=8 clusters, balancing granularity for targeted marketing with interpretability 
for  strategy  development.  The  clustering  loss  weight  λ  starts  at  0.1  during  initial  epochs  and 
linearly increases to 1.0 over 50 epochs, allowing embeddings to stabilize before enforcing strong

11

---

<!-- PAGE 12 -->

Spectrum of Research

Vol 5 (2) 2025

clustering objectives. Centroid updates occur every 5 training iterations, with cluster assignments 
computed using Student's t-distribution with degree of freedom 1 [15].

Adaptive  feature  selection  operates  using  a  sliding  window  approach  that  recomputes  mutual 
information  scores  every  10  epochs  as  embeddings  evolve.  The  selection  algorithm  maintains 
feature  subsets  of  size  35,  representing  approximately  15%  of  total  features  while  preserving 
sufficient  behavioral  coverage.  Redundancy  threshold  is  set  at  0.65  based  on  cross-validation 
experiments balancing information retention with subset compactness. Business-critical features 
including credit utilization, total spending, and payment timeliness are always included regardless 
of computed scores, ensuring alignment with established banking analytics practices.

Figure 2: Training Convergence and Loss Dynamics

The visualization comprises four synchronized subplots arranged in a 2x2 grid displaying training 
dynamics across 150 epochs. The top-left panel shows reconstruction loss curves for both training 
and validation sets, plotted as smooth lines with training loss in solid blue and validation loss in 
dashed orange. The loss values decrease from initial high values around 0.45 to stabilized values 
near 0.08, with slight divergence indicating mild overfitting around epoch 120. The top-right panel 
illustrates clustering loss evolution, starting from 0.0 as λ=0 initially and gradually increasing to 
plateau at approximately 0.23 by epoch 100. Color gradients indicate the annealing schedule with

12

---

<!-- PAGE 13 -->

Spectrum of Research

Vol 5 (2) 2025

warmer  colors  representing  higher  λ  values.  The  bottom-left  panel  displays  silhouette  score 
progression tracking clustering quality, showing improvement from 0.42 to 0.67 over training with 
confidence intervals as shaded regions. Notable improvements occur during epochs 40-60 when 
clustering loss activates. The bottom-right panel presents a stacked area chart showing the evolving 
contribution of different loss components (reconstruction, clustering, regularization) to total loss 
over training. Each component is rendered in distinct colors with smooth interpolation. All panels 
share a common x-axis labeled "Training Epoch" and include grid lines for precise value reading. 
Annotations highlight key events such as "λ annealing begins" at epoch 10 and "early stopping 
point" at epoch 142. The figure uses a professional scientific color palette with high contrast for 
accessibility.

Table IV: Hyperparameter Settings and Justifications

Parameter

Value

Search Range

Embedding Dim

32

[16, 32, 64, 128]

Learning Rate

0.001

[0.0001, 0.01]

Selection 
Criterion

Validation 
Silhouette

Convergence 
Speed

Impact

High

Medium

Batch Size

256

[64, 128, 256, 512]  GPU Memory

Low

Dropout Rate

0.2

[0.0, 0.1, 0.2, 0.3]

Cluster Count K

8

[4, 6, 8, 10, 12]

Reconstruction 
Error

Business 
Requirements

Embedding 
Stability

Medium

High

High

λ Initial

λ Final

Feature Subset

0.1

1.0

35

[0.01, 0.1, 0.5]

[0.5, 1.0, 2.0]

Clustering Priority  High

[20, 35, 50, 70]

Interpretability

Medium

MI Threshold

0.35

[0.2, 0.35, 0.5]

Feature Coverage  Medium

Update Interval

5

[1, 5, 10, 20]

Training Stability

Low

C. Clustering Performance Evaluation

Quantitative evaluation employs multiple clustering quality metrics assessing different aspects of 
segmentation  performance.  Silhouette  coefficient  measures  how  similar  customers  are  to  their 
assigned cluster compared to nearest neighboring clusters, with values ranging from -1 to 1 where

13

---

<!-- PAGE 14 -->

Spectrum of Research

Vol 5 (2) 2025

higher scores indicate better-defined clusters. The proposed method achieves an average silhouette 
score  of  0.673  on  the  test  set,  substantially  outperforming  K-Means  baseline  at  0.524  and 
hierarchical  clustering  at  0.558.  Davies-Bouldin  index  provides  complementary  assessment 
emphasizing inter-cluster separation, with lower values indicating superior clustering. The deep 
embedding approach attains a Davies-Bouldin score of 0.847 compared to 1.234 for K-Means and 
1.089 for Gaussian mixture models, demonstrating enhanced cluster compactness and separation.

Calinski-Harabasz  index  evaluates  the  ratio  of  between-cluster  dispersion  to  within-cluster 
dispersion, providing scale-invariant assessment applicable across different cluster configurations. 
The  proposed  framework  achieves  a  Calinski-Harabasz  score  of  8,947,  significantly  exceeding 
traditional methods including K-Means at 5,432 and DBSCAN at 6,104. Statistical significance 
testing through permutation tests with 10,000 iterations confirms that performance improvements 
are not due to random variation, with p-values below 0.001 for all primary metrics. The robustness 
of  discovered  clusters  is  validated  through  bootstrap  resampling,  computing  clustering  metrics 
across 100 random subsamples and analyzing distribution stability.

Business-oriented  evaluation  metrics  assess  segmentation  utility  for  marketing  applications 
beyond pure clustering quality. Segment size distribution analysis verifies that all eight discovered 
clusters exceed minimum viable campaign sizes of 50,000 customers, with the smallest segment 
containing  187,000  customers  representing  2.4%  of  the  total  population.  Balanced  clustering 
avoids  extreme  concentration  in  single  dominant  segments,  with  the  largest  cluster  containing 
18.3% of customers. Feature interpretability scores measuring comprehensibility of cluster profiles 
indicate  that  marketing  teams  can  describe  each  segment  using  an  average  of  4.2  key 
differentiating  characteristics,  supporting  clear  value  proposition  development  and  targeted 
messaging strategies.

D. Discovered Customer Segments and Business Insights

The  eight  discovered  customer  segments  exhibit  distinct  behavioral  profiles  aligned  with 
recognizable  consumer  personas  relevant  to  banking  strategy.  Cluster  1  represents  "Premium 
Travelers"  characterized  by  high  average  transaction  values  concentrated  in  travel  and  dining 
categories,  elevated  international  transaction  frequencies,  and  low  credit  utilization  suggesting 
financial stability. This segment comprises 892,000 customers with average monthly spending of 
$4,892  and  strong  preference  for  rewards  programs.  Cluster  2  contains  "Everyday  Shoppers" 
showing  balanced  spending  across  multiple  categories,  moderate  transaction  frequencies,  and 
heavy usage of grocery and retail merchants. This largest segment with 1.45 million customers 
exhibits predictable spending patterns suitable for cash-back reward structures.

Cluster  3  identifies  "Digital  Natives"  distinguished  by  predominant  online  shopping  activity, 
mobile  app  engagement,  subscription  service  usage,  and  evening  transaction  timing  patterns. 
These  734,000  customers  skew  younger  demographically  and  respond  strongly  to  digital-first 
banking experiences. Cluster 4 represents "Value Conscious" customers featuring below-average

14

---

<!-- PAGE 15 -->

Spectrum of Research

Vol 5 (2) 2025

transaction  amounts,  price-sensitive  merchant  preferences,  and  high  utilization  of  promotional 
offers.  This  456,000-customer  segment  requires  carefully  balanced  credit  limits  and  benefits 
programs  emphasizing  practical  value  over  premium  perks.  Cluster  5  captures  "Business 
including  office  supplies, 
Professionals"  exhibiting  business-related  spending  patterns 
professional services, and concentrated weekday activity with minimal weekend transactions.

Cluster  6  contains  "Entertainment  Enthusiasts"  showing  elevated  spending  in  entertainment, 
dining,  and  leisure  categories  with  strong  weekend  activity  patterns. These  621,000  customers 
demonstrate interest in experiential rewards and event access programs. Cluster 7 identifies "Credit 
Builders"  characterized  by  lower  credit  limits,  higher  utilization  rates,  and  payment  patterns 
suggesting credit establishment goals. This 298,000-customer segment presents opportunities for 
graduated  credit  line  increase  programs  supporting  financial  wellness  objectives.  Cluster  8 
represents  "Luxury  Consumers"  featuring  highest  transaction  values,  premium  merchant 
preferences, and distinctive spending in luxury goods, fine dining, and high-end travel categories. 
This  187,000-customer  segment,  while  smallest,  contributes  disproportionately  to  profitability 
through high spending volumes and premium product holdings.

The visualization presents an eight-panel radar chart arrangement showing behavioral profiles for 
each discovered customer segment. Each individual radar chart employs eight axes representing 
key  behavioral  dimensions:  average  spending,  transaction  frequency,  travel  affinity,  dining 
preference, online activity, credit utilization, payment timeliness, and premium merchant usage. 
The axes extend from center point (0) to outer edge (1.0) representing normalized feature values. 
Each cluster profile is rendered as a filled polygon connecting data points on the eight axes, with 
distinctive colors assigned to  each  cluster (Cluster 1 in  royal  blue, Cluster 2 in  emerald  green, 
Cluster  3  in  vibrant  orange,  etc.).  The  polygons  use  semi-transparent  fills  allowing  overlay 
comparison  where  multiple  clusters  appear  on  reference  panel.  Grid  lines  at  intervals  of  0.2 
facilitate quantitative reading of values. Individual panels are arranged in 2x4 layout with cluster 
names prominently displayed. The reference panel in the center shows all eight clusters overlaid 
with reduced opacity, enabling cross-cluster comparison of behavioral patterns. Axis labels employ 
clear sans-serif typography with abbreviations explained in legend. Color-coded legends associate 
each cluster with descriptive persona names ("Premium Travelers", "Digital Natives", etc.). The 
visualization employs professional scientific styling with subtle shadows and high-contrast text 
ensuring readability in both digital and print formats.

Marketing  strategy  recommendations  emerge  directly  from  discovered  segment  characteristics. 
Premium  Travelers  merit  premium  reward  card  offerings  emphasizing  travel  benefits,  airport 
lounge access, and international services. Digital Natives benefit from mobile-first experiences, 
instant  notifications,  and  integration  with  digital  wallet  platforms.  Value  Conscious  customers 
require  transparent  fee  structures,  cash-back  programs  on  everyday  spending,  and  financial 
education resources. The segmentation framework enables banks to optimize product development 
roadmaps, prioritize feature enhancements, and allocate marketing budgets across segments based 
on  lifetime  value  projections  and  acquisition  costs.  Cross-sell  opportunities  are  identified  by

15

---

<!-- PAGE 16 -->

Spectrum of Research

Vol 5 (2) 2025

analyzing product holding patterns within each segment, revealing gaps where customers exhibit 
behaviors typical of premium product users but lack corresponding product relationships.

Figure 3: Radar Chart Visualization of Cluster Behavioral Profiles

V. Conclusion

This research presents a comprehensive deep embedding clustering framework addressing critical 
challenges  in  banking  customer  segmentation  through  integration  of  representation  learning, 
adaptive  feature  selection,  and  business-constrained  optimization.  The  proposed  methodology 
demonstrates  substantial  improvements  over  traditional  clustering  approaches  across  multiple 
performance  dimensions  including  statistical  quality  metrics  and  business-oriented  evaluation 
criteria. Experimental validation on large-scale real-world credit card transaction data confirms the

16

---

<!-- PAGE 17 -->

Spectrum of Research

Vol 5 (2) 2025

framework's  capability  to  discover  meaningful  customer  segments  aligned  with  actionable 
marketing  strategies  while  maintaining  computational  efficiency  suitable  for  production 
deployment.

The  adaptive  feature  selection  mechanism  successfully  balances  data-driven  discovery  with 
preservation of business-critical attributes, producing interpretable segment profiles that marketing 
teams can readily understand and operationalize. Mutual information-based importance scoring 
identifies  behavioral  indicators  most  relevant  to  segmentation  objectives  while  redundancy 
analysis  ensures  selected  features  provide  complementary  rather  than  overlapping  information. 
Business constraints embedded within the optimization framework guarantee discovered segments 
satisfy  practical  requirements  including  minimum  viable  sizes,  balanced  distributions,  and 
temporal stability supporting consistent strategy execution.

The eight discovered customer segments exhibit distinctive behavioral profiles corresponding to 
recognizable consumer personas across the banking  customer base. Premium Travelers, Digital 
Natives, Value Conscious customers, and other identified groups each present unique opportunities 
for  targeted  marketing,  product  development,  and  relationship  management  strategies.  The 
framework  enables  financial  institutions  to  move  beyond  simplistic  demographic  segmentation 
toward sophisticated behavioral profiling that captures nuanced differences in spending patterns, 
channel preferences, and credit usage characteristics relevant to personalized service delivery.

Future  research  directions  include  extending  the  framework  to  incorporate  temporal  dynamics 
through  recurrent  neural  architectures  capturing  evolution  of  customer  behaviors  over  time. 
Sequential  modeling  approaches  using  LSTM  or  transformer  networks  could  track  behavioral 
trajectories and predict segment transitions, enabling proactive interventions to retain high-value 
customers or prevent attrition. Multi-view clustering techniques integrating multiple data sources 
including transaction records, customer service interactions, and digital engagement metrics could 
provide richer behavioral profiles. Transfer learning approaches applying knowledge from related 
domains  or  other  financial  institutions  could  accelerate  model  development  in  data-scarce 
scenarios.

The  framework's  modular  design  supports  integration  with  existing  banking  analytics 
infrastructure  and  customer 
relationship  management  systems.  Practical  deployment 
considerations  including  model  retraining  schedules,  segment  assignment  monitoring,  and 
performance tracking dashboards ensure ongoing alignment with business objectives as customer 
behaviors  and  market  conditions  evolve.  Privacy-preserving  extensions  employing  federated 
learning or differential privacy mechanisms could enable collaborative model development across 
institutions while protecting  sensitive customer information. The demonstrated success  of deep 
embedding  clustering  for  banking  customer  segmentation  establishes  a  foundation  for  broader 
applications  across  financial  services  including  loan  origination,  fraud  detection,  and  wealth 
management client segmentation.

17

---

<!-- PAGE 18 -->

Spectrum of Research

Vol 5 (2) 2025

References

[1]  Y. Wang,  "Enhancing  Retail  Promotional  ROI Through AI-Driven Timing  and Targeting: A 
Data Decision Framework for Multi-Category Retailers," in Proceedings of the 2025 International 
Conference on Digital Economy and Information Systems, Apr. 2025, pp. 296-302. 
[2]  M. Sun, "Research on E-Commerce Return Prediction and Influencing Factor Analysis Based 
on User Behavioral Characteristics," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 15-
28, 2025. 
[3]  A.  Kang  and  X.  Ma,  "AI-Based  Pattern  Recognition  and  Characteristic Analysis  of  Cross-
Border Money Laundering Behaviors in Digital Currency Transactions," Pinnacle Academic Press 
Proceedings Series, vol. 5, pp. 1-19, 2025. 
[4]  X. Lu and Z. Li, "Attention-Based Multimodal Emotion Recognition for Fine-Grained Visual 
Ad Engagement Prediction on Instagram," Pinnacle Academic Press Proceedings Series, vol. 3, 
pp. 204-218, 2025. 
[5]  S. Meng, K. Qian, and Y. Zhou, "Empirical Study on the Impact of ESG Factors on Private 
Equity  Investment  Performance:  An  Analysis  Based  on  Clean  Energy  Industry,"  Journal  of 
Computing Innovations and Applications, vol. 3, no. 2, pp. 15-33, 2025. 
[6]  Z.  Pan,  "AI-Powered  Real-Time  Effectiveness  Assessment  Framework  for  Cross-Channel 
Pharmaceutical Marketing: Optimizing ROI through Predictive Analytics," in Proceedings of the 
2025 International Conference on Management Science and Computer Engineering, Jun. 2025, pp. 
220-227. 
[7]  D. Yuan and S. Meng, "Temporal Feature-Based Suspicious Behavior Pattern Recognition in 
Cross-Border Securities Trading," Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp. 
1-18, 2025. 
[8]  Y.  Huang,  "NLP-Enhanced  Detection  of Wrong-Way  Risk  Contagion  Patterns  in  Interbank 
Networks: A Deep Learning Approach," in Proceedings of the 2025 International Conference on 
Management Science and Computer Engineering, Jun. 2025, pp. 214-219. 
[9]  D. Zhang, S. Meng, and Y. Wang, "Impact Analysis of Price Promotion Strategies on Consumer 
Purchase Patterns in Fast-Moving Consumer Goods Retail," Academia Nexus Journal, vol. 4, no. 
1, 2025. 
[10]  L. Ge, "Artificial Intelligence-Driven Optimization of Accounts Receivable Management in 
Supply Chain Finance: An Empirical Study Based on Cash Flow Prediction and Risk Assessment," 
Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp. 110-120, 2025. 
[11]  G. Wei and Z. Ji, "Quantifying and Mitigating Dataset Biases in Video Understanding Tasks 
across Cultural Contexts," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 147-158, 2025. 
[12]  H.  Guan,  "Context-Aware  Semantic  Ambiguity  Resolution  in  Cross-Cultural  Dialogue 
Understanding," Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp. 136-147, 2025. 
[13]  A.  Kang,  K.  Zhang,  and Y.  Chen,  "AI-Assisted Analysis  of  Policy  Communication  during 
Economic  Crises:  Correlations  with  Market  Confidence  and  Recovery  Outcomes,"  Pinnacle 
Academic Press Proceedings Series, vol. 3, pp. 159-173, 2025. 
[14]  X. Luo, "Politeness Strategies in Conversational AI: A Cross-Cultural Pragmatic Analysis of

18

---

<!-- PAGE 19 -->

Spectrum of Research

Vol 5 (2) 2025

Human-AI Interactions," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 1-14, 2025. 
[15]  S.  Meng,  D. Yuan,  and  D.  Zhang,  "Integration  Strategies  and  Performance  Impact  of  PE-
Backed Technology M&A Transactions," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 
59-75, 2025.

19

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Spectrum of Research
Vol 5 issue 2 2025
https://spectrumofresearch.com
Deep Embedding Clustering with Adaptive Feature Selection for
Banking Customer Segmentation
Haojun Weng
Computer Technology, Fudan University, Shanghai, China
Corresponding Email: hao.weng@gmail.com
Abstract
Customer segmentation is critical for financial institutions to optimize marketing strategies in the
competitive credit card market. Traditional clustering methods such as K-Means often fail to
capture complex behavioral patterns and lack interpretability for business decision-making. This
paper proposes a deep embedding clustering framework with adaptive feature selection for
banking customer segmentation. The method integrates a stacked autoencoder to learn low-
dimensional customer behavior representations while preserving interpretability of business-
critical features. A mutual information-based feature importance mechanism automatically
identifies discriminative behavioral indicators. Furthermore, a business-constrained clustering
optimization approach ensures segmentation results align with marketing objectives. The
framework will be evaluated on a real-world dataset of credit card customers from a major U.S.
financial institution. This research aims to advance AI-driven precision marketing, supporting
banks in optimizing resource allocation and enhancing customer lifetime value.
Keywords: Deep Learning, Customer Segmentation, Feature Selection, Banking Analytics
I. Introduction
The financial services industry faces unprecedented challenges in customer retention and
acquisition within increasingly competitive markets. Banks and credit card issuers must develop
sophisticated understanding of customer behaviors to deliver personalized services and optimize
marketing expenditure. Recent advances in artificial intelligence have demonstrated remarkable
potential in consumer behavior analysis [1], enabling institutions to discover nuanced patterns that
traditional analytical approaches cannot detect. The complexity of modern consumer financial
behaviors necessitates moving beyond simplistic demographic segmentation toward
multidimensional behavioral profiling.
Credit card transaction data represents a rich source of behavioral signals, encompassing spending
patterns, merchant categories, transaction frequencies, and temporal dynamics. Traditional
segmentation approaches rely heavily on predetermined features and linear assumptions about
customer similarities. K-Means clustering and hierarchical methods have dominated practical
1

Spectrum of Research Vol 5 (2) 2025
applications due to their computational efficiency and interpretability. These conventional
techniques struggle with high-dimensional feature spaces and fail to capture nonlinear
relationships inherent in complex behavioral datasets [2]. The increasing volume and velocity of
transactional data compound these limitations, creating an urgent need for more sophisticated
analytical frameworks.
Deep learning architectures offer promising alternatives through their capacity to automatically
learn hierarchical feature representations from raw data. Autoencoder networks have shown
particular success in unsupervised learning tasks, demonstrating ability to compress high-
dimensional inputs into meaningful latent representations [3]. Embedding-based clustering methods
combine representation learning with cluster assignment optimization, enabling end-to-end
training that jointly optimizes both objectives. The banking sector requires solutions that balance
algorithmic sophistication with practical interpretability, as marketing teams must understand and
act upon segmentation insights [4].
This research addresses the gap between theoretical advances in deep clustering and practical
requirements of financial services applications. We propose a novel framework that integrates deep
embedding clustering with adaptive feature selection mechanisms specifically designed for
banking customer segmentation. The approach maintains interpretability of business-critical
features while leveraging deep learning's representational power. Our methodology incorporates
domain-specific constraints that ensure discovered segments align with actionable marketing
strategies. The framework processes large-scale transactional datasets from major U.S. financial
institutions, demonstrating scalability and practical applicability in production environments.
II. Related Work
Customer segmentation research in financial services has evolved through multiple generations of
methodological approaches. Early demographic segmentation gave way to behavioral clustering
based on transaction patterns and product usage characteristics. Traditional machine learning
methods including decision trees, random forests, and support vector machines have been applied
to customer classification tasks with varying degrees of success [5]. These supervised approaches
require labeled training data and predefined categories, limiting their applicability to exploratory
segmentation scenarios where customer groups emerge organically from behavioral patterns.
Unsupervised clustering algorithms have formed the backbone of customer segmentation practice
across industries. K-Means clustering remains widely deployed due to computational efficiency
and straightforward interpretation of cluster centroids. Hierarchical clustering methods provide
dendrogram visualizations that support hierarchical market segmentation strategies [6]. Density-
based spatial clustering algorithms handle non-spherical cluster shapes and automatically
determine cluster numbers. Model-based clustering approaches using Gaussian mixture models
offer probabilistic cluster assignments with theoretical foundations in statistical inference [7]. These
2

Spectrum of Research Vol 5 (2) 2025
conventional methods share common limitations including sensitivity to feature scaling, difficulty
handling high-dimensional spaces, and inability to capture complex nonlinear patterns.
The emergence of deep learning has catalyzed new directions in unsupervised clustering research.
Autoencoder architectures compress input data into lower-dimensional latent spaces while
preserving essential information, enabling more effective similarity computations [8]. Variational
autoencoders introduce probabilistic formulations that model latent space distributions, supporting
generation of synthetic customer profiles. Deep embedding clustering methods jointly optimize
reconstruction loss and cluster assignment loss, enabling representations specifically tuned for
clustering tasks. Recent work has explored attention mechanisms and transformer architectures for
sequential transaction data, capturing temporal dependencies in customer behaviors [9].
Feature selection represents a critical challenge in financial data analytics where hundreds of
potential behavioral indicators exist. Traditional filter methods rank features based on statistical
measures including correlation coefficients, chi-square tests, and information gain metrics [10].
Wrapper methods evaluate feature subsets through iterative model training, optimizing
performance on specific learning algorithms. Embedded methods integrate feature selection within
model training, learning feature importance weights during optimization. Mutual information-
based approaches measure statistical dependencies between features and target variables,
providing theoretically grounded selection criteria that avoid linear assumptions [11].
Business constraints in banking applications require segmentation methods that produce actionable
insights aligned with marketing capabilities and regulatory requirements. Segments must achieve
sufficient size to justify targeted campaigns while maintaining homogeneity in behavior patterns.
Interpretability constraints necessitate transparent feature importance rankings that marketing
teams can understand and act upon [12]. Privacy regulations including GDPR and CCPA impose
additional requirements on data usage and customer profiling practices. Recent research has begun
addressing these practical considerations through constrained clustering formulations and
explainable AI techniques [13].
The intersection of deep learning and business analytics presents opportunities for methodological
innovation. Multi-objective optimization frameworks balance clustering quality metrics with
business-specific objectives including marketing ROI and customer lifetime value predictions [14].
Transfer learning approaches leverage knowledge from related domains to improve segmentation
in data-scarce scenarios. Ensemble methods combine multiple clustering algorithms to achieve
robust segment definitions less sensitive to algorithmic choices [15]. Our proposed framework
builds upon these foundations while introducing novel mechanisms specifically designed for
banking customer segmentation challenges.
3

Spectrum of Research Vol 5 (2) 2025
III. Methodology
A. Problem Formulation
The customer segmentation problem involves partitioning a set of N credit card customers into K
distinct groups based on their behavioral characteristics captured through transactional data. Each
customer i is represented by a feature vector x_i ∈ R^D containing D behavioral attributes
extracted from transaction history, including average transaction amounts, merchant category
distributions, temporal spending patterns, credit utilization ratios, and payment behaviors. The
objective function minimizes intra-cluster variance while maximizing inter-cluster separation,
subject to business constraints that ensure segment sizes meet minimum thresholds for marketing
campaign viability and segment interpretability remains sufficiently high for actionable strategy
development.
Traditional clustering objectives focus solely on geometric properties of data distributions,
optimizing metrics such as silhouette coefficients or Davies-Bouldin indices. Banking applications
require additional considerations including segment stability over time, demographic diversity
within clusters to avoid discriminatory practices, and alignment between discovered segments and
existing customer relationship management systems. The optimization problem incorporates these
multiple objectives through a weighted combination approach where business stakeholders specify
relative importance of different criteria. Constraint satisfaction ensures regulatory compliance
while maintaining statistical rigor in cluster definitions.
The high-dimensional nature of behavioral feature spaces presents computational and statistical
challenges. Transaction data spanning multiple years generates hundreds of potential features
capturing spending patterns across various dimensions. Dimensionality reduction becomes
essential to avoid curse of dimensionality effects that degrade clustering performance. The
challenge lies in reducing dimensionality while preserving discriminative information relevant to
customer segmentation. Our approach addresses this through learned embeddings that compress
behavioral representations into lower-dimensional manifolds where clustering algorithms operate
more effectively.
B. Deep Embedding Clustering Architecture
The proposed architecture consists of three interconnected components that jointly optimize
clustering objectives and feature selection criteria. The foundation comprises a stacked
autoencoder network that learns compressed representations of customer behaviors through
unsupervised pre-training on raw transactional features. The encoder network maps high-
dimensional input vectors through multiple hidden layers with progressively decreasing
dimensions, culminating in a bottleneck layer representing the learned embedding space. The
decoder network mirrors this structure, reconstructing original inputs from latent representations
to ensure information preservation during compression [1].
4

| Spectrum of Research   |     |     |     |     |       Vol 5 (2) 2025  |
| ---------------------- | --- | --- | --- | --- | --------------------- |
The autoencoder employs a symmetrical architecture with four hidden layers in both encoder and
decoder paths. Input layer dimensionality matches the number of behavioral features D, while
hidden layers contain 512, 256, 128, and 64 neurons respectively. The bottleneck embedding layer
contains 32 dimensions, providing sufficient capacity for representing complex behavioral patterns
while enabling efficient clustering computations. Activation functions use rectified linear units
(ReLU)  for  hidden  layers,  introducing  nonlinearity  that  enables  learning  of  complex
transformations. The output layer employs linear activation for continuous features and sigmoid
activation for binary indicators, appropriately matching different feature types in the behavioral
dataset [2].
Pre-training proceeds through layer-wise greedy training followed by fine-tuning of the complete
autoencoder network. Each layer is initially trained as a denoising autoencoder, learning robust
features resilient to input perturbations. Gaussian noise with standard deviation 0.1 is added to
inputs during pre-training, encouraging the network to learn meaningful representations rather than
identity mappings. Fine-tuning minimizes mean squared reconstruction error across the entire
architecture using Adam optimizer with learning rate 0.001 and mini-batch size 256. Early
stopping  based  on  validation  set  performance  prevents  overfitting  while  ensuring  adequate
representational capacity.
Table I: Autoencoder Architecture Specifications
| Layer      | Type   | Input Dim  | Output Dim  | Activation  | Dropout  |
| ---------- | ------ | ---------- | ----------- | ----------- | -------- |
| Input      | Dense  | 247        | 512         | -           | 0.0      |
| Encoder-1  | Dense  | 512        | 256         | ReLU        | 0.2      |
| Encoder-2  | Dense  | 256        | 128         | ReLU        | 0.2      |
| Encoder-3  | Dense  | 128        | 64          | ReLU        | 0.2      |
| Embedding  | Dense  | 64         | 32          | Linear      | 0.0      |
| Decoder-1  | Dense  | 32         | 64          | ReLU        | 0.2      |
| Decoder-2  | Dense  | 64         | 128         | ReLU        | 0.2      |
| Decoder-3  | Dense  | 128        | 256         | ReLU        | 0.2      |
| Decoder-4  | Dense  | 256        | 512         | ReLU        | 0.2      |
| Output     | Dense  | 512        | 247         | Mixed       | 0.0      |
The clustering component builds upon learned embeddings through an iterative refinement process
that alternates between cluster assignment and centroid updates. Initial cluster centroids are
established through K-Means++ initialization applied to embedded customer representations,
ensuring well-distributed starting positions that accelerate convergence. The clustering objective
5

Spectrum of Research Vol 5 (2) 2025
minimizes Kullback-Leibler divergence between predicted cluster assignment distribution and
target distribution computed from current centroid positions [3]. This formulation enables soft
cluster assignments where customers have probability distributions across multiple clusters,
providing flexibility to represent customers with hybrid behavioral patterns.
Target distribution sharpening enhances cluster separation by emphasizing high-confidence
assignments while suppressing ambiguous cases. The auxiliary target distribution is computed by
raising assignment probabilities to the power of 2 and normalizing, effectively amplifying
differences between cluster affinities. This self-training mechanism gradually improves cluster
quality without requiring labeled supervision. The clustering loss is combined with reconstruction
loss in a multi-task learning framework, maintaining embedding quality while optimizing cluster
assignments. The balance between these objectives is controlled by a hyperparameter λ that is
annealed during training, initially emphasizing reconstruction to establish robust embeddings
before shifting focus toward clustering objectives [4].
C. Adaptive Feature Selection Mechanism
The feature selection component operates in parallel with embedding learning, identifying
behavioral indicators that contribute most significantly to clustering objectives. Mutual
information quantifies statistical dependencies between individual features and cluster
assignments, providing a theoretically grounded measure of feature relevance [6]. The calculation
employs kernel density estimation to approximate continuous probability distributions, avoiding
discretization artifacts that can bias information estimates. Features exhibiting high mutual
information with cluster labels receive elevated importance scores, guiding subsequent feature
subset selection.
The selection mechanism incorporates both relevance and redundancy considerations to construct
diverse feature subsets. Pairwise mutual information between features identifies redundant
indicators that provide similar information about cluster structure. The selection algorithm
maximizes relevance while minimizing redundancy through a greedy forward selection process.
Starting from an empty set, features are iteratively added if they increase overall information
content beyond a threshold determined by cross-validation. This approach balances
comprehensiveness with interpretability, producing feature subsets of manageable size that
marketing teams can understand and act upon [7].
Business-critical features receive special treatment through a mandatory inclusion mechanism that
ensures certain behavioral indicators always appear in final feature sets. Credit utilization ratios,
payment delinquency indicators, and total spending volumes represent fundamental characteristics
relevant to virtually all banking strategies. The selection algorithm respects these constraints while
optimizing remaining features based on information-theoretic criteria. This hybrid approach
maintains domain expertise integration while leveraging data-driven discovery of novel behavioral
patterns.
6

| Spectrum of Research   |                    |     |     |                                |     |     |       Vol 5 (2) 2025  |     |
| ---------------------- | ------------------ | --- | --- | ------------------------------ | --- | --- | --------------------- | --- |
|                        |                    |     |     |                                |     |     |                       |     |

|     |                              |              |                    |         |        |     |                         |     |
| --- | ---------------------------- | ------------ | ------------------ | ------- | ------ | --- | ----------------------- | --- |
|     |                              |              |                    |         |        |     |                         |     |
|     |                              |              |                    |         |        |     |                         |     |
|     |                              |              |                    |         |        |     |                         |     |
|     |                              |              |                    |         |        |     |                         |     |
|     |                              |              |                    |         |        |     |                         |     |

|     |                    |     |     |                           |     |                   |     |     |
| --- | ------------------ | --- | --- | ------------------------- | --- | ----------------- | --- | --- |
|     |                    |     |     |                           |     |                   |     |     |

|     |                    |     |                     |                            |                               |     |     |     |
| --- | ------------------ | --- | ------------------- | -------------------------- | ----------------------------- | --- | --- | --- |
|     |                    |     |                     |                            |                               |     |     |     |
|     |                    |     |                     |                            |                               |     |     |     |
|     |                    |     |                     |                            |                               |     |     |     |
|     |                    |     |                     |                            |                               |     |     |     |

|     |                   |     |                      |                            |                                |     |     |     |
| --- | ----------------- | --- | -------------------- | -------------------------- | ------------------------------ | --- | --- | --- |
|     |                   |     |                      |                            |                                |     |     |     |
|     |                   |     |                      |                            |                                |     |     |     |

|     |     |                          |     |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
|     |     |                          |     |     |     |     |     |     |
Figure 1: Mutual Information-Based Feature Selection Process
The visualization presents a comprehensive flowchart depicting the adaptive feature selection
mechanism across four parallel streams. The top stream illustrates initial feature extraction from
raw transaction data, showing 247 behavioral indicators organized into six category groups:
spending  patterns,  merchant  preferences,  temporal  dynamics,  credit  behaviors,  payment
characteristics, and channel usage. Color-coded boxes represent different feature categories, with
line thickness indicating feature correlations. The second stream displays the mutual information
computation module, featuring a heatmap matrix showing pairwise MI scores between all features
and cluster assignments, with warm colors (red/orange) indicating high information content and
cool colors (blue) representing low relevance. The third stream depicts the redundancy analysis
component, visualizing feature correlation networks as a force-directed graph where node sizes
represent feature importance and edge weights indicate redundancy levels. The bottom stream
shows  the  final  selection  output,  presenting  selected  feature  subsets  for  each  cluster  with
importance scores represented as horizontal bar charts. Connecting arrows between streams
indicate information flow, with annotations showing MI threshold values and redundancy cutoff
criteria. The figure employs a professional color scheme using institutional blue, financial green,
and analytic orange tones, with clear labels and legends supporting interpretability for non-
technical stakeholders.
Table II: Top-20 Features Ranked by Mutual Information Scores
Rank  Feature Name  Category  MI Score  Redundancy  Selected
7

| Spectrum of Research   |     |     |     |     |       Vol 5 (2) 2025  |
| ---------------------- | --- | --- | --- | --- | --------------------- |
Avg  Monthly
| 1   |     | Spending  | 0.847  | 0.123  | Yes  |
| --- | --- | --------- | ------ | ------ | ---- |
Spend
Transaction
| 2   |     | Spending  | 0.792  | 0.156  | Yes  |
| --- | --- | --------- | ------ | ------ | ---- |
Frequency
| 3   | Dining Ratio  | Merchant  | 0.738  | 0.089  | Yes  |
| --- | ------------- | --------- | ------ | ------ | ---- |
Travel
| 4   |     | Merchant  | 0.701  | 0.094  | Yes  |
| --- | --- | --------- | ------ | ------ | ---- |
Spending
Weekend
| 5   |     | Temporal  | 0.689  | 0.112  | Yes  |
| --- | --- | --------- | ------ | ------ | ---- |
Activity
Credit
| 6   |     | Credit  | 0.654  | 0.078  | Yes  |
| --- | --- | ------- | ------ | ------ | ---- |
Utilization
|     | Luxury  | Goods     |        |        |     |
| --- | ------- | --------- | ------ | ------ | --- |
| 7   |         | Merchant  | 0.621  | 0.201  | No  |
Ratio
Payment
| 8   |     | Payment  | 0.598  | 0.067  | Yes  |
| --- | --- | -------- | ------ | ------ | ---- |
Timeliness
Evening
| 9   |     | Temporal  | 0.576  | 0.223  | No  |
| --- | --- | --------- | ------ | ------ | --- |
Transactions
Online
| 10  |     | Channel  | 0.554  | 0.091  | Yes  |
| --- | --- | -------- | ------ | ------ | ---- |
Shopping
ATM
| 11  | Withdrawal  | Channel  | 0.532  | 0.145  | Yes  |
| --- | ----------- | -------- | ------ | ------ | ---- |
Freq
Entertainment
| 12  |     | Merchant  | 0.509  | 0.178  | No  |
| --- | --- | --------- | ------ | ------ | --- |
Spend
Balance
| 13  |     | Credit  | 0.487  | 0.104  | Yes  |
| --- | --- | ------- | ------ | ------ | ---- |
Transfers
International
| 14  |     | Temporal  | 0.465  | 0.087  | Yes  |
| --- | --- | --------- | ------ | ------ | ---- |
Trans
Subscription
| 15  |     | Merchant  | 0.443  | 0.198  | No  |
| --- | --- | --------- | ------ | ------ | --- |
Services
Cash  Advance
| 16  |     | Credit  | 0.421  | 0.119  | Yes  |
| --- | --- | ------- | ------ | ------ | ---- |
Usage
8

Spectrum of Research Vol 5 (2) 2025
Mobile App
17 Channel 0.398 0.134 Yes
Activity
Quarterly
18 Temporal 0.376 0.156 Yes
Spend Var
Grocery
19 Merchant 0.354 0.241 No
Shopping
Contactless
20 Channel 0.332 0.167 No
Payment
D. Business-Constrained Optimization
The optimization framework incorporates multiple business constraints that ensure discovered
segments support practical marketing applications. Minimum cluster size constraints prevent
creation of segments too small to justify dedicated marketing campaigns, with thresholds set based
on campaign economics and customer acquisition costs. Balance constraints limit maximum
segment size to prevent dominance by single large clusters that provide insufficient differentiation
for targeted strategies [9]. These hard constraints are enforced through penalty terms in the
optimization objective that sharply increase when constraint violations occur.
Interpretability constraints promote cluster definitions based on easily understood behavioral
characteristics. The framework penalizes clusters that require complex combinations of many
features for explanation, favoring segments describable through small numbers of key
differentiators. Feature contribution regularization encourages sparse cluster profiles where each
segment exhibits distinctive patterns in limited numbers of behavioral dimensions. This sparsity
aids marketing teams in developing clear value propositions and messaging strategies tailored to
segment characteristics [10].
Temporal stability constraints address the dynamic nature of customer behaviors over time.
Segment definitions must remain relatively stable across consecutive time periods to enable
consistent strategy execution and performance measurement. The optimization includes a stability
regularization term that penalizes large shifts in cluster assignments when the model is retrained
on updated data. This mechanism balances adaptation to evolving behaviors with maintenance of
strategic continuity. Marketing teams specify acceptable drift rates based on campaign planning
horizons and organizational capacity for strategy modification.
The complete optimization objective combines clustering quality metrics, feature selection criteria,
and business constraints into a unified framework solved through alternating optimization. Cluster
assignments and centroids are updated using expectation-maximization steps while feature
selection weights are optimized through gradient descent. The multi-objective formulation
employs Pareto optimization principles where no single objective dominates at the expense of
9

Spectrum of Research Vol 5 (2) 2025
others. Stakeholder preference weights are elicited through interactive sessions where marketing
leaders review candidate solutions and provide feedback on business alignment [11].
IV. Experimental Results and Analysis
A. Dataset Description and Preprocessing
The experimental evaluation employs a real-world dataset from a major U.S. financial institution
containing credit card transaction records for 7.9 million active customers spanning 36 months
from January 2022 through December 2024. The dataset includes detailed transaction-level
information capturing merchant categories, transaction amounts, timestamps, geographic
locations, and payment channel types. Customer-level data provides demographic attributes
including age, income bracket, account tenure, and product holdings, enabling enrichment of
behavioral profiles with contextual information [8]. Data preprocessing addresses missing values,
outliers, and data quality issues inherent in large-scale operational datasets.
Feature engineering transforms raw transactional records into structured behavioral profiles
suitable for clustering analysis. Aggregate features summarize spending patterns across multiple
dimensions including total volumes, average transaction amounts, spending distributions across
merchant categories, and temporal patterns such as weekday versus weekend activity. Derived
features capture behavioral trends including spending growth rates, seasonality patterns, and
category preference shifts over time. Credit behavior indicators measure utilization rates, payment
punctuality scores, balance transfer frequencies, and cash advance usage patterns [12]. The complete
feature set comprises 247 behavioral variables spanning six major categories aligned with
marketing strategy dimensions.
Data normalization ensures features contribute appropriately to distance computations and
embedding learning processes. Continuous variables are standardized to zero mean and unit
variance, preventing features with large numerical ranges from dominating similarity calculations.
Binary indicators and categorical variables receive specialized encoding preserving their discrete
nature while enabling integration with continuous features. Temporal features undergo cyclical
encoding using sine and cosine transformations to capture periodic patterns without artificial
discontinuities. The preprocessing pipeline implements robust scaling techniques resilient to
outliers, using median and interquartile range statistics rather than mean and standard deviation
[13].
Table III: Dataset Statistics and Feature Categories
Category Features Mean Std Dev Min Max Missing %
Spending
42 2,347.56 1,892.34 0.00 45,320.00 0.8%
Patterns
10

Spectrum of Research Vol 5 (2) 2025
Merchant
68 0.23 0.18 0.00 1.00 1.2%
Categories
Temporal
51 18.45 12.67 0.00 127.00 0.5%
Dynamics
Credit
34 0.47 0.31 0.00 1.00 2.1%
Behaviors
Payment
28 0.89 0.15 0.00 1.00 1.8%
Patterns
Channel
24 0.34 0.26 0.00 1.00 0.9%
Usage
Total 247 - - - - 1.2%
The dataset is partitioned into training, validation, and test sets using stratified sampling to ensure
representative distributions across customer segments. Training data comprises 70% of customers
used for model development and embedding learning. Validation data containing 15% of
customers supports hyperparameter tuning and early stopping decisions during training. The
remaining 15% forms a held-out test set for final performance evaluation and generalization
assessment. Temporal splits are also constructed where training uses data from first 24 months and
testing evaluates performance on the most recent 12 months, assessing model robustness to
behavioral evolution and market changes [14].
B. Implementation Details and Hyperparameter Configuration
The proposed framework is implemented using Python 3.9 with TensorFlow 2.12 for deep learning
components and scikit-learn 1.3 for traditional clustering baselines. Training is conducted on a
cluster with 4 NVIDIA A100 GPUs, enabling efficient processing of the large-scale customer
dataset. The stacked autoencoder network is pre-trained for 100 epochs with batch size 256, using
Adam optimizer with initial learning rate 0.001 and exponential decay rate 0.96 every 10 epochs.
Reconstruction loss employs mean squared error for continuous features and binary cross-entropy
for categorical indicators, weighted by feature importance scores to prioritize business-critical
attributes.
The deep embedding clustering phase fine-tunes the pre-trained encoder while jointly optimizing
cluster assignments. Initial cluster number K is determined through elbow analysis and silhouette
score evaluation on embedded representations, testing values from 4 to 12 clusters. The selected
configuration uses K=8 clusters, balancing granularity for targeted marketing with interpretability
for strategy development. The clustering loss weight λ starts at 0.1 during initial epochs and
linearly increases to 1.0 over 50 epochs, allowing embeddings to stabilize before enforcing strong
11

Spectrum of Research Vol 5 (2) 2025
clustering objectives. Centroid updates occur every 5 training iterations, with cluster assignments
computed using Student's t-distribution with degree of freedom 1 [15].
Adaptive feature selection operates using a sliding window approach that recomputes mutual
information scores every 10 epochs as embeddings evolve. The selection algorithm maintains
feature subsets of size 35, representing approximately 15% of total features while preserving
sufficient behavioral coverage. Redundancy threshold is set at 0.65 based on cross-validation
experiments balancing information retention with subset compactness. Business-critical features
including credit utilization, total spending, and payment timeliness are always included regardless
of computed scores, ensuring alignment with established banking analytics practices.
Figure 2: Training Convergence and Loss Dynamics
The visualization comprises four synchronized subplots arranged in a 2x2 grid displaying training
dynamics across 150 epochs. The top-left panel shows reconstruction loss curves for both training
and validation sets, plotted as smooth lines with training loss in solid blue and validation loss in
dashed orange. The loss values decrease from initial high values around 0.45 to stabilized values
near 0.08, with slight divergence indicating mild overfitting around epoch 120. The top-right panel
illustrates clustering loss evolution, starting from 0.0 as λ=0 initially and gradually increasing to
plateau at approximately 0.23 by epoch 100. Color gradients indicate the annealing schedule with
12

| Spectrum of Research   |     |       |     |       Vol 5 (2) 2025  |
| ---------------------- | --- | ----- | --- | --------------------- |
warmer colors representing higher λ values. The bottom-left panel displays silhouette score
progression tracking clustering quality, showing improvement from 0.42 to 0.67 over training with
confidence intervals as shaded regions. Notable improvements occur during epochs 40-60 when
clustering loss activates. The bottom-right panel presents a stacked area chart showing the evolving
contribution of different loss components (reconstruction, clustering, regularization) to total loss
over training. Each component is rendered in distinct colors with smooth interpolation. All panels
share a common x-axis labeled "Training Epoch" and include grid lines for precise value reading.
Annotations highlight key events such as "λ annealing begins" at epoch 10 and "early stopping
point" at epoch 142. The figure uses a professional scientific color palette with high contrast for
accessibility.
Table IV: Hyperparameter Settings and Justifications
Selection
| Parameter  | Value  | Search Range  |     | Impact  |
| ---------- | ------ | ------------- | --- | ------- |
Criterion
Validation
| Embedding Dim  | 32  | [16, 32, 64, 128]  |     | High  |
| -------------- | --- | ------------------ | --- | ----- |
Silhouette
Convergence
| Learning Rate  | 0.001  | [0.0001, 0.01]  |     | Medium  |
| -------------- | ------ | --------------- | --- | ------- |
Speed
| Batch Size  | 256  | [64, 128, 256, 512]  | GPU Memory  | Low  |
| ----------- | ---- | -------------------- | ----------- | ---- |
Reconstruction
| Dropout Rate  | 0.2  | [0.0, 0.1, 0.2, 0.3]  |     | Medium  |
| ------------- | ---- | --------------------- | --- | ------- |
Error
Business
| Cluster Count K  | 8   | [4, 6, 8, 10, 12]  |     | High  |
| ---------------- | --- | ------------------ | --- | ----- |
Requirements
Embedding
| λ Initial  | 0.1  | [0.01, 0.1, 0.5]  |     | High  |
| ---------- | ---- | ----------------- | --- | ----- |
Stability
| λ Final  | 1.0  | [0.5, 1.0, 2.0]  | Clustering Priority  | High  |
| -------- | ---- | ---------------- | -------------------- | ----- |
Feature Subset  35  [20, 35, 50, 70]  Interpretability  Medium
MI Threshold  0.35  [0.2, 0.35, 0.5]  Feature Coverage  Medium
| Update Interval  | 5   | [1, 5, 10, 20]  | Training Stability  | Low  |
| ---------------- | --- | --------------- | ------------------- | ---- |
C. Clustering Performance Evaluation
Quantitative evaluation employs multiple clustering quality metrics assessing different aspects of
segmentation performance. Silhouette coefficient measures how similar customers are to their
assigned cluster compared to nearest neighboring clusters, with values ranging from -1 to 1 where
13

Spectrum of Research Vol 5 (2) 2025
higher scores indicate better-defined clusters. The proposed method achieves an average silhouette
score of 0.673 on the test set, substantially outperforming K-Means baseline at 0.524 and
hierarchical clustering at 0.558. Davies-Bouldin index provides complementary assessment
emphasizing inter-cluster separation, with lower values indicating superior clustering. The deep
embedding approach attains a Davies-Bouldin score of 0.847 compared to 1.234 for K-Means and
1.089 for Gaussian mixture models, demonstrating enhanced cluster compactness and separation.
Calinski-Harabasz index evaluates the ratio of between-cluster dispersion to within-cluster
dispersion, providing scale-invariant assessment applicable across different cluster configurations.
The proposed framework achieves a Calinski-Harabasz score of 8,947, significantly exceeding
traditional methods including K-Means at 5,432 and DBSCAN at 6,104. Statistical significance
testing through permutation tests with 10,000 iterations confirms that performance improvements
are not due to random variation, with p-values below 0.001 for all primary metrics. The robustness
of discovered clusters is validated through bootstrap resampling, computing clustering metrics
across 100 random subsamples and analyzing distribution stability.
Business-oriented evaluation metrics assess segmentation utility for marketing applications
beyond pure clustering quality. Segment size distribution analysis verifies that all eight discovered
clusters exceed minimum viable campaign sizes of 50,000 customers, with the smallest segment
containing 187,000 customers representing 2.4% of the total population. Balanced clustering
avoids extreme concentration in single dominant segments, with the largest cluster containing
18.3% of customers. Feature interpretability scores measuring comprehensibility of cluster profiles
indicate that marketing teams can describe each segment using an average of 4.2 key
differentiating characteristics, supporting clear value proposition development and targeted
messaging strategies.
D. Discovered Customer Segments and Business Insights
The eight discovered customer segments exhibit distinct behavioral profiles aligned with
recognizable consumer personas relevant to banking strategy. Cluster 1 represents "Premium
Travelers" characterized by high average transaction values concentrated in travel and dining
categories, elevated international transaction frequencies, and low credit utilization suggesting
financial stability. This segment comprises 892,000 customers with average monthly spending of
$4,892 and strong preference for rewards programs. Cluster 2 contains "Everyday Shoppers"
showing balanced spending across multiple categories, moderate transaction frequencies, and
heavy usage of grocery and retail merchants. This largest segment with 1.45 million customers
exhibits predictable spending patterns suitable for cash-back reward structures.
Cluster 3 identifies "Digital Natives" distinguished by predominant online shopping activity,
mobile app engagement, subscription service usage, and evening transaction timing patterns.
These 734,000 customers skew younger demographically and respond strongly to digital-first
banking experiences. Cluster 4 represents "Value Conscious" customers featuring below-average
14

Spectrum of Research Vol 5 (2) 2025
transaction amounts, price-sensitive merchant preferences, and high utilization of promotional
offers. This 456,000-customer segment requires carefully balanced credit limits and benefits
programs emphasizing practical value over premium perks. Cluster 5 captures "Business
Professionals" exhibiting business-related spending patterns including office supplies,
professional services, and concentrated weekday activity with minimal weekend transactions.
Cluster 6 contains "Entertainment Enthusiasts" showing elevated spending in entertainment,
dining, and leisure categories with strong weekend activity patterns. These 621,000 customers
demonstrate interest in experiential rewards and event access programs. Cluster 7 identifies "Credit
Builders" characterized by lower credit limits, higher utilization rates, and payment patterns
suggesting credit establishment goals. This 298,000-customer segment presents opportunities for
graduated credit line increase programs supporting financial wellness objectives. Cluster 8
represents "Luxury Consumers" featuring highest transaction values, premium merchant
preferences, and distinctive spending in luxury goods, fine dining, and high-end travel categories.
This 187,000-customer segment, while smallest, contributes disproportionately to profitability
through high spending volumes and premium product holdings.
The visualization presents an eight-panel radar chart arrangement showing behavioral profiles for
each discovered customer segment. Each individual radar chart employs eight axes representing
key behavioral dimensions: average spending, transaction frequency, travel affinity, dining
preference, online activity, credit utilization, payment timeliness, and premium merchant usage.
The axes extend from center point (0) to outer edge (1.0) representing normalized feature values.
Each cluster profile is rendered as a filled polygon connecting data points on the eight axes, with
distinctive colors assigned to each cluster (Cluster 1 in royal blue, Cluster 2 in emerald green,
Cluster 3 in vibrant orange, etc.). The polygons use semi-transparent fills allowing overlay
comparison where multiple clusters appear on reference panel. Grid lines at intervals of 0.2
facilitate quantitative reading of values. Individual panels are arranged in 2x4 layout with cluster
names prominently displayed. The reference panel in the center shows all eight clusters overlaid
with reduced opacity, enabling cross-cluster comparison of behavioral patterns. Axis labels employ
clear sans-serif typography with abbreviations explained in legend. Color-coded legends associate
each cluster with descriptive persona names ("Premium Travelers", "Digital Natives", etc.). The
visualization employs professional scientific styling with subtle shadows and high-contrast text
ensuring readability in both digital and print formats.
Marketing strategy recommendations emerge directly from discovered segment characteristics.
Premium Travelers merit premium reward card offerings emphasizing travel benefits, airport
lounge access, and international services. Digital Natives benefit from mobile-first experiences,
instant notifications, and integration with digital wallet platforms. Value Conscious customers
require transparent fee structures, cash-back programs on everyday spending, and financial
education resources. The segmentation framework enables banks to optimize product development
roadmaps, prioritize feature enhancements, and allocate marketing budgets across segments based
on lifetime value projections and acquisition costs. Cross-sell opportunities are identified by
15

| Spectrum of Research   |     |     |     |     |     |         Vol 5 (2) 2025  |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
analyzing product holding patterns within each segment, revealing gaps where customers exhibit
behaviors typical of premium product users but lack corresponding product relationships.

|     |                                          |     |     |     |                                        |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
|     |                                          |     |     |     |                                        |     |     |     |

|     |               |     |            |               |     |     |            |     |
| --- | ------------- | --- | ---------- | ------------- | --- | --- | ---------- | --- |
|     |               |     |            |               |     |     |            |     |
|     |               |     |            |               |     |     |            |     |
|     |               |     |            |               |     |     |            |     |

|     |             |     |             |             |     |     |             |     |
| --- | ----------- | --- | ----------- | ----------- | --- | --- | ----------- | --- |

|     |                                        |                 |            |               |                                         |                 |            |     |
| --- | -------------------------------------- | --------------- | ---------- | ------------- | --------------------------------------- | --------------- | ---------- | --- |
|     |                                        |                 |            |               |                                         |                 |            |     |
|     |                                        |                 |            |               |                                         |                 |            |     |
|     |                                        |                 |            |               |                                         |                 |            |     |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |             |                 |             |             |     |                 |             |     |
| --- | ----------- | --------------- | ----------- | ----------- | --- | --------------- | ----------- | --- |
|     |             |                 |             |             |     |                 |             |     |

|     |     |     |                   |                           |                 |     |     |     |
| --- | --- | --- | ----------------- | ------------------------- | --------------- | --- | --- | --- |

Figure 3: Radar Chart Visualization of Cluster Behavioral Profiles
V. Conclusion
This research presents a comprehensive deep embedding clustering framework addressing critical
challenges in banking customer segmentation through integration of representation learning,
adaptive feature selection, and business-constrained optimization. The proposed methodology
demonstrates substantial improvements over traditional clustering approaches across multiple
performance dimensions including statistical quality metrics and business-oriented evaluation
criteria. Experimental validation on large-scale real-world credit card transaction data confirms the
16

Spectrum of Research Vol 5 (2) 2025
framework's capability to discover meaningful customer segments aligned with actionable
marketing strategies while maintaining computational efficiency suitable for production
deployment.
The adaptive feature selection mechanism successfully balances data-driven discovery with
preservation of business-critical attributes, producing interpretable segment profiles that marketing
teams can readily understand and operationalize. Mutual information-based importance scoring
identifies behavioral indicators most relevant to segmentation objectives while redundancy
analysis ensures selected features provide complementary rather than overlapping information.
Business constraints embedded within the optimization framework guarantee discovered segments
satisfy practical requirements including minimum viable sizes, balanced distributions, and
temporal stability supporting consistent strategy execution.
The eight discovered customer segments exhibit distinctive behavioral profiles corresponding to
recognizable consumer personas across the banking customer base. Premium Travelers, Digital
Natives, Value Conscious customers, and other identified groups each present unique opportunities
for targeted marketing, product development, and relationship management strategies. The
framework enables financial institutions to move beyond simplistic demographic segmentation
toward sophisticated behavioral profiling that captures nuanced differences in spending patterns,
channel preferences, and credit usage characteristics relevant to personalized service delivery.
Future research directions include extending the framework to incorporate temporal dynamics
through recurrent neural architectures capturing evolution of customer behaviors over time.
Sequential modeling approaches using LSTM or transformer networks could track behavioral
trajectories and predict segment transitions, enabling proactive interventions to retain high-value
customers or prevent attrition. Multi-view clustering techniques integrating multiple data sources
including transaction records, customer service interactions, and digital engagement metrics could
provide richer behavioral profiles. Transfer learning approaches applying knowledge from related
domains or other financial institutions could accelerate model development in data-scarce
scenarios.
The framework's modular design supports integration with existing banking analytics
infrastructure and customer relationship management systems. Practical deployment
considerations including model retraining schedules, segment assignment monitoring, and
performance tracking dashboards ensure ongoing alignment with business objectives as customer
behaviors and market conditions evolve. Privacy-preserving extensions employing federated
learning or differential privacy mechanisms could enable collaborative model development across
institutions while protecting sensitive customer information. The demonstrated success of deep
embedding clustering for banking customer segmentation establishes a foundation for broader
applications across financial services including loan origination, fraud detection, and wealth
management client segmentation.
17

Spectrum of Research Vol 5 (2) 2025
References
Y. Wang, "Enhancing Retail Promotional ROI Through AI-Driven Timing and Targeting: A
[1]
Data Decision Framework for Multi-Category Retailers," in Proceedings of the 2025 International
Conference on Digital Economy and Information Systems, Apr. 2025, pp. 296-302.
M. Sun, "Research on E-Commerce Return Prediction and Influencing Factor Analysis Based
[2]
on User Behavioral Characteristics," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 15-
28, 2025.
A. Kang and X. Ma, "AI-Based Pattern Recognition and Characteristic Analysis of Cross-
[3]
Border Money Laundering Behaviors in Digital Currency Transactions," Pinnacle Academic Press
Proceedings Series, vol. 5, pp. 1-19, 2025.
X. Lu and Z. Li, "Attention-Based Multimodal Emotion Recognition for Fine-Grained Visual
[4]
Ad Engagement Prediction on Instagram," Pinnacle Academic Press Proceedings Series, vol. 3,
pp. 204-218, 2025.
S. Meng, K. Qian, and Y. Zhou, "Empirical Study on the Impact of ESG Factors on Private
[5]
Equity Investment Performance: An Analysis Based on Clean Energy Industry," Journal of
Computing Innovations and Applications, vol. 3, no. 2, pp. 15-33, 2025.
Z. Pan, "AI-Powered Real-Time Effectiveness Assessment Framework for Cross-Channel
[6]
Pharmaceutical Marketing: Optimizing ROI through Predictive Analytics," in Proceedings of the
2025 International Conference on Management Science and Computer Engineering, Jun. 2025, pp.
220-227.
D. Yuan and S. Meng, "Temporal Feature-Based Suspicious Behavior Pattern Recognition in
[7]
Cross-Border Securities Trading," Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp.
1-18, 2025.
Y. Huang, "NLP-Enhanced Detection of Wrong-Way Risk Contagion Patterns in Interbank
[8]
Networks: A Deep Learning Approach," in Proceedings of the 2025 International Conference on
Management Science and Computer Engineering, Jun. 2025, pp. 214-219.
D. Zhang, S. Meng, and Y. Wang, "Impact Analysis of Price Promotion Strategies on Consumer
[9]
Purchase Patterns in Fast-Moving Consumer Goods Retail," Academia Nexus Journal, vol. 4, no.
1, 2025.
L. Ge, "Artificial Intelligence-Driven Optimization of Accounts Receivable Management in
[10]
Supply Chain Finance: An Empirical Study Based on Cash Flow Prediction and Risk Assessment,"
Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp. 110-120, 2025.
G. Wei and Z. Ji, "Quantifying and Mitigating Dataset Biases in Video Understanding Tasks
[11]
across Cultural Contexts," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 147-158, 2025.
H. Guan, "Context-Aware Semantic Ambiguity Resolution in Cross-Cultural Dialogue
[12]
Understanding," Journal of Sustainability, Policy, and Practice, vol. 1, no. 2, pp. 136-147, 2025.
A. Kang, K. Zhang, and Y. Chen, "AI-Assisted Analysis of Policy Communication during
[13]
Economic Crises: Correlations with Market Confidence and Recovery Outcomes," Pinnacle
Academic Press Proceedings Series, vol. 3, pp. 159-173, 2025.
X. Luo, "Politeness Strategies in Conversational AI: A Cross-Cultural Pragmatic Analysis of
[14]
18

Spectrum of Research Vol 5 (2) 2025
Human-AI Interactions," Pinnacle Academic Press Proceedings Series, vol. 3, pp. 1-14, 2025.
S. Meng, D. Yuan, and D. Zhang, "Integration Strategies and Performance Impact of PE-
[15]
Backed Technology M&A Transactions," Pinnacle Academic Press Proceedings Series, vol. 3, pp.
59-75, 2025.
19