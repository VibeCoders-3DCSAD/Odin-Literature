---
conversion_metadata:
  converted_at: "2026-07-22T13:03:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "D. R. et al.pdf"
  source_pdf_sha256: "b29af8ba647c3ade6dc87ede2440fd90e56c90be9fc4a6f1932da0267e67e399"
  page_count: 9
  markdown_char_count: 68451
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

International Journal of Artificial 
Intelligence and Machine Learning

Publisher's Home Page: https://www.svedbergopen.com/

SvedbergOpen

DISSEMINATION OF  KNOWLEDGE

Research Paper

Open Access

Robust Learning Under Distribution Shifts for Non-Stationary 
Data Environments

Rekha D1 , Shanthi Vairavan², Sunil MP³, Jitendra Kumar Katariya⁴, Swapnil Maheshkumar Parikh⁵, T. 
Shanthi⁶, Shanthi R⁷

1Assistant Professor  Vel Tech Multi Tech Dr.Rangarajan Dr.Sakunthala Engineering College Chennai – 600062 
rekhadharma23@gmail.com 
² Professor, Computer Science, Meenakshi College of Arts and Science, Meenakshi Academy of Higher Education and Research, India 
³ Assistant Professor, Department of Electronics and Communication Engineering, Faculty of Engineering and Technology, JAIN 
(Deemed-to-be University), Bengaluru, Karnataka, India. Email: mp.sunil@jainuniversity.ac.in, ORCID: 0000-0002-7737-4145 
⁴ Assistant Professor, Department of Computer Science & Application, Vivekananda Global University, Jaipur, India. Email: 
jitendra.kumar.katariya@vgu.ac.in, ORCID: 0009-0000-9940-9022 
⁵ Professor, Department of Computer Science and Engineering, Faculty of Engineering and Technology, Parul Institute of 
Technology, Parul University, Vadodara, Gujarat, India. Email: swapnil.parikh17761@paruluniversity.ac.in, ORCID: 0000-0001-
7831-6927 
⁶ Associate Professor, Department of Electronics and Communication Engineering, Sona College of Technology, India. Email: 
shanthi@sonatech.ac.in, ORCID: 0000-0001-8962-5311 
⁷ Assistant Professor, Department of Mathematics, Meenakshi College of Arts and Science, Meenakshi Academy of Higher Education 
and Research, India

Abstract

Keyword: Robust Learning, Distribution Shift, Non-Stationary Data, Concept Drift, Adaptive Learning Systems, Deep Learning

Introduction  
Contemporary ML systems are dynamic and constantly produce data that defies the notion of fixed distribution [1, 
2]. The data properties in non-stationary environments evolve due to the user behavior, the system dynamics, or 
external  forces,  and  thus  learning  becomes  more  complicated  [3].  The  most  important  problems  are  the 
distribution shift whereby training and testing data is not the same [4]. It is concept drift, where there is a shift in 
input-output relations, and domain shift, where there is a shift in input distributions, but the same task is being 
done [5, 6].

These models are primarily trained in a stationary form, without a continuous adaptation process [7, 8]. Thus, the 
performance  is  worse  when  the  distributions  are  varied,  which  leads  to  a  loss  of  accuracy  in  practice  and 
inaccuracy in generalization [9]. This weakness offers the necessity to possess flexible and strong learning systems

Vol.6, No.2s, 2026                                                                                                                                                                            754

---

<!-- PAGE 2 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

that can deal with the shifting flows of information. The best system must be able to recognize the patterns of data 
change,  continuously  update  itself,  and  be  capable  of  maintaining  its  performance  at  all  times  without  full 
retraining [10, 11].

To  alleviate  these  issues,  the  proposed  presents  a  potent  learning  model  in  non-stationary  environments  with 
AHO-InDNN  to  balance  exploration  and  exploitation.  It  is  a  combination  of  the  drift  detection  and  online 
incremental learning to adapt dynamically. An LDP-based optimization strategy increases stability and minimises 
uncertainty.  The key contributions can be summed up as follows:

•  Developed an AHO-InDNN adaptive learning framework integrated with drift detection, online learning,

and incremental updating for non-stationary environments.

•

Introduced an LDP-based parameter optimization strategy to improve robustness, stability, and reliable 
decision-making under dynamic uncertainty.

•  Performed comprehensive evaluation demonstrating superior performance under sudden, gradual, and

recurrent distribution shift scenarios compared with baseline models.

The  remaining  structure  of  this  research  was  as  follows:  Section  2  reviews  the  literature  in  robust  learning  in 
distribution shifts. Section 3 develops the suggested non-stationary data. Section 4 describes the implementation 
and design of the model. Section 5 evaluates results of performance. The section 6 ends with conclusion and future 
research directions.

Literature review 
The concept drift research has been extensively studied in the fields of forecasting, streaming analytics, healthcare, 
and financial systems. Research [12] enhances Photovoltaic (PV) prediction based on adaptive federated learning 
with  dual  drift  detection  and  selective  retraining  with  a  smaller  Root  Mean  Square  Error  (RMSE)  and  faster 
adaptation,  but  was  restricted  by  threshold  tuning  and  poor  real-world  diversity.  Likewise,  the  research  [13] 
compares  several  adaptive  classifiers  in  the  concept  drift  context  based  on  the  scikit-multiflow  framework, 
demonstrating  the  adaptability  of  models  in  a  variety  of  algorithms  though  lacks  real-life  validation  and  more 
rigorous analysis of optimization.

Deep learning-based drift detection was explored in [14] using a DNN combined with an autoencoder (DNN+AE-
DD), where reconstruction error and the 3σ rule are used for drift identification. Despite its sensitivity, it does not 
have  a  good  cross-domain  generalization.  In  network  systems,  [15]  has  used  adaptive  windowing  with  H2M 
networks,  which  are  better  with  respect  to  latency  and  response,  but  it  is  based  on  pre-established  traffic 
assumptions.  In  the  same  vein,  [16]  trained  an  ensemble  variational  autoencoder  with  Kolmogorov-Smirnoff 
testing to detect cloud drift, with high F-scores but high computational and scalability cost. In additional, [17] used 
variational autoencoders with KL-divergence testing to identify abnormal behavior in older adults, with over 91% 
F1-score, but was limited to small sample size and generalizability.

Research Gap  
Although  concept  drift  and  non-stationary  data  management  have  advanced,  current  approaches  are  still 
disjointed, focusing on drift detection, adaptive learning, or optimization individually. Various methods are based 
on threshold-driven mechanisms, minimizing resilience to changing distributions. Some of the models are also less 
adaptable  and  have  poor  generalization  in  the  real  world.  Moreover,  model  uncertainty  and  robustness 
optimization  are  under-explored,  and  certain  methods  are  costly  to  compute  or  may  need  dataset-specific 
optimization. To address these issues, this research proposes a robust framework integrating lightweight drift 
detection with AHO-InDNN for online and incremental learning, enhanced with uncertainty-aware optimization 
and a LDP-based robustness evaluation to improve stability and adaptability.

Problem formulation  
Training  and  testing  data  in  ML  were  assumed  to  share  the  same  underlying  distribution,  represented  as: 
𝑄𝑇𝑟𝑎𝑖𝑛(𝑌, 𝑋) = 𝑄𝑇𝑒𝑠𝑡(𝑌, 𝑋). However, in the dynamic and real-world scenarios the assumption is not always true 
since data distributions evolve with time as customers adjust their behavior, new fraud strategies are invented, 
seasonal spending trends and dynamics of online payments. To give an example, the tendencies of fraud that could 
be  traced  in  the  previous  weeks  may  be  ineffective  now  as  the  fraudsters  are  coming  up  with  other  types  of 
transactions or disguises. This breakdown can be formally stated as: 𝑄𝑇𝑟𝑎𝑖𝑛(𝑌, 𝑋) ≠ 𝑄𝑇𝑒𝑠𝑡(𝑌, 𝑋). Progressive model 
performance deterioration is caused by distributional mismatch. To be more specific, concept drift is change in the 
denote 
conditional distribution between input and output over time: 𝑄(𝑌|𝑋)𝑠 ≠ 𝑄(𝑌|𝑋)𝑠+1. Let 𝐶𝑠 = {(𝑦𝑗, 𝑥𝑗 )}

𝑚

𝑗=1

Vol.6, No.2s, 2026                                                                                                                                                                            755

---

<!-- PAGE 3 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

data  at  time  𝑠,  and  𝑒𝜃  represent  the  model  with  parameters  𝜃𝑠.  The  goal  is  to  minimize  the  expected  loss  in 
moderating  distributions:  𝐾𝑠(𝜃) = 𝔼(𝑌,𝑋)~𝑄𝑠[ℓ(𝑒𝜃(𝑌), 𝑋)].  To  handle  this  dynamic  environment,  the  model  is 
incrementally updated at each time step: 𝜃𝑠+1 = 𝜃𝑠 + ∆𝜃𝑠.  Where ∆𝜃𝑠 is adaptively learned using the drift-directed 
uncertainty estimation-based optimization strategy based on the AHO approach.

Methodology  
The methodology suggests  a solid adaptive learning model of non-stationary data  settings, as demonstrated  in 
Figure 1. It is created to operate on continuous data streams in which distributions can vary because of abrupt, 
gradual or periodic drift. In contrast  to the static models, the framework constantly checks incoming data and 
updates the model to maintain prediction accuracy in the changing conditions.

Figure 1: Proposed Robust Adaptive Learning Framework for Non-Stationary Environments

The model consists of four modules; data input, drift detection, adaptive learning and output prediction. Streaming 
data are preprocessed and analyzed to detect concept drift through statistical and feature changes. After the drift, 
the AHO-InDNN model re-estimates the parameters to learn effectively. Incremental and online learning allows 
constant adaptation without re-training. LDP-based mechanism minimizes the uncertainty and stabilizes updates, 
and distributed learning increases the scalability and computational efficiency of multiple nodes.

Dataset  
The research utilizes PaySim artificial mobile money transaction data in Kaggle 
(https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset), which was developed to 
replicate actual financial transactions without compromising their privacy.  It contains 30 days of sequential 
transaction records (743 time steps) with types including CASH-IN, CASH-OUT, PAYMENT, DEBIT, and 
TRANSFER. Features include transaction amount, time step, anonymized user IDs, and fraud label. It has a time-
series structure that can be used in concept drift analysis, adaptive learning, and fraud detection in the changing 
transaction patterns.

Min-Max Normalization for Scaling Input Data into a Uniform Range

To ensure stable learning and faster convergence, Min–Max normalization is applied to numerical features, scaling 
values into the range [0,1]. This reduces magnitude variation and improves robustness under distribution shifts, 
as expressed in Equation (1).

𝑦′ =

𝑦−𝑦𝑚𝑖𝑛
𝑦𝑚𝑎𝑥−𝑦𝑚𝑖𝑛

(1)

Where 𝑦 is dynamic data patterns as raw transaction feature;  𝑦𝑚𝑖𝑛 observed value as a way to maintain lower-
bound stability; 𝑦𝑚𝑎𝑥 is observed value as a way to maintain scale variation; 𝑦′  prime normalized feature as a way 
to allow robust and drift-resilient learning.

Drift Detection Module for Identifying Concept Drift

Vol.6, No.2s, 2026                                                                                                                                                                            756

---

<!-- PAGE 4 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

The drift detection module of the proposed framework tracks transaction streams to detect changes in the data 
distribution. It initiates a change in the model when a drastic change is detected to reduce the overall cost of the 
computation and to retain the high detection levels. The model includes three types of concept drift, like sudden 
(immediate  adaptation),  gradual  (patterns  change  gradually  as  learning  progresses  slowly),  and  recurrent 
(patterns repeat with the use of historical knowledge). These drifts are due to the rapid change of fraud strategies 
(Table 1), changing user spending behavior, and periodic attack cycles in the fraud detection systems, and adaptive 
learning is a solution to maintain strong performance.

Table 1. Types of Concept Drift and Examples

Drift Type 
Sudden Drift 
Gradual Drift 
Recurrent Drift  Periodic, repeating patterns

Description 
Abrupt change in data distribution 
Slow, continuous changes over time  Slowly changing user spending behavior

Seasonal fraud campaigns

New fraud attack pattern

Real-World Example

Hybrid statistical divergence and mean shift enhance the drift detection by being more sensitive to the changes of 
the distribution and less prone to false positives and stable.

Online & Incremental Learning for Continuous Model Adaptation 
The framework online incremental learning module to revise the model as it notices changes in distribution. The 
model is retrained using the new information received, and is not retrained entirely, which is effective in adapting 
and preserving previously learnt information.  This is the selective means of learning that allows the system to 
optimize its parameters continuously by new streams of data and uncertainty data. This is particularly essential 
in fraud detection, as transaction patterns tend to fluctuate as the attackers change their methods of fraud, as their 
behavior  changes,  and  new  patterns  of  attack  emerge.  The  suggested  approach  allows  constant  adaptation, 
minimizes  the  computational  cost,  and  is  stable  in  non-stationary  conditions.  It  enhances  the  reliability  of 
prediction  and  a  robust  performance  in  dynamic  and  imbalanced  transaction  flows,  which  are  effective  in 
performing real-time fraud detection.

InDNN for Robust Learning under Distribution Shifts 
InDNN  is  designed  to  deal  with  non-stationary  data  situations  that  are  affected  by  concept  drift  and  domain 
variability. It has a three-layer architecture, with input, multiple hidden layers, and output. Unlike standard DNNs, 
InDNN  employs  dynamic  depth  and  neuron  structure  to  be  robust.  It  has  64  input  neurons,  as  many  as  seven 
hidden layers, and 64 output neurons to learn high-dimensional features. A parameter tuning strategy controls 
the hidden neurons in a dynamic manner to prevent overfitting and underfitting. The neuron output is defined as 
(3):

𝑚
𝑚+1 = 𝜎(𝑤) = 𝜎(∑ 𝜔𝑗𝑝
𝑥𝑝

𝑛
𝑗=1

+ 𝜔𝑝

𝑛+1)

(2)

𝑚 represents 
where 𝜎(𝑤) is the activation function, 𝑥𝑝
𝑛+1 denotes bias. The ReLU activation function is employed to ensure efficient gradient propagation 
weights, and 𝜔𝑝
and adaptability under shifting data distributions. To explicitly handle uncertainty caused by distribution shifts, a 
regularized loss function 𝐹(𝜃) is used (3):

𝑚+1 denotes the output of the 𝑝𝑡ℎ neuron in layer 𝑚 + 1, 𝜔𝑗𝑝

𝐹(𝜃) = −

1

𝑀

∑ ∑ 𝑠𝑚𝑝 log 𝑥𝑚𝑝

𝑝𝑚

(3)

where ∑ denotes aggregation over all samples and classes; 𝑠𝑚𝑝 is the true label, log 𝑥𝑚𝑝 is the predicted output, 
𝜃 = {𝜔, 𝑏},  and  𝐹(𝜃)  is  a  robustness  regularization  term  that  mitigates  overfitting  under  drift  conditions.  To 
optimize the parameters efficiently in dynamic environments, an adaptive moment-based gradient optimization 
is employed (4):

𝜃𝑠 = 𝜃𝑠−1−∝

𝛽1𝑚𝑠−1+(1−𝛽1) ∇𝜃𝐹(𝜃𝑠−1)
2
√𝛽2𝑣𝑠−1+(1−𝛽2) ( ∇𝜃𝐹(𝜃𝑠−1))

+𝜖

(4)

Where  𝜃𝑠  updated  parameters,  𝜃𝑠−1  previous  state,  ∝  learning  rate,  𝛽1, 𝛽2  decay  factors,  𝑚𝑠−1,𝑣𝑠−1  gradient 
moments,   ∇𝜃𝐹(𝜃𝑠−1)  current  gradient,  and  𝜖  ensures  stability  under  distribution  shifts.  Dropout  improves 
generalization  under  unseen  shifts,  while  drift-aware  updates  enable  incremental  learning  when  significant 
distribution changes are detected.

Vol.6, No.2s, 2026                                                                                                                                                                            757

---

<!-- PAGE 5 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

AHO for Optimal Parameter Tuning 
The  AHO  method  is  used  in  this  research  to  improve  the  AHO-InDNN  model's  parameter  setting  and  adaptive 
learning in non-stationary situations. AHO balances exploration and exploitation to handle distribution shifts such 
as  concept  drift  and  domain  variability,  inspired  by  the  hunting  behavior  of  archerfish,  where  each  agent 
represents a candidate solution of network parameters, hyperparameters, and adaptation strategies.

•  Population  Initialization:  Initially,  the  population  of  archerfish  is  randomly  generated  within  the

defined search space. The initial position of the 𝑗th archerfish is given as (5):

𝑞(𝑗, 0) = [(𝑞1

𝐾 + 𝜎1(𝑞1

𝑉 − 𝑞1

𝐾)), ⋯ , (𝑞𝑐

𝐾 + 𝜎𝑐(𝑞𝑐

𝑉 − 𝑞𝑐

𝐾))]

(5)

𝑉 
𝐾  and  𝑞𝑐
Where  𝑞(𝑗, 0)  denotes  the  initial  candidate  solution;  𝑗  is  the  archerfish  index;  𝑐  is  dimensionality;  𝑞𝑐
represent  lower  (𝐾)  and  upper  (𝑉)  bounds  of  parameters;  𝜎𝑐 ∈ [0,1] ensures  randomness  for  diversity  and 
robustness under distribution shifts.

•

Shooting  Behavior  (Exploration  Phase):  This  phase  performs  global  search  to  adapt  to  sudden 
distribution changes. The position update is defined as (6):

𝑞(𝑗, 𝑠 + 1) = −(𝑞(𝑗, 𝑠) − 𝑞𝑖𝑛(𝑗, 𝑠)) 𝑓−(‖𝑞𝑖𝑛(𝑗,𝑠)−𝑞(𝑗,𝑠)‖2)2

+ 𝑞(𝑗, 𝑠)

(6)

Where 𝑞(𝑗, 𝑠 + 1) denotes the updated proposed model parameters; 𝑞(𝑗, 𝑠) is the current parameter set of the 𝑗𝑡ℎ 
candidate  model;  𝑞𝑖𝑛(𝑗, 𝑠)  is  the  estimated  optimal  solution  under  distribution  shift;  𝑗 is  candidate  index;  𝑠  is 
iteration; ∥⋅∥2 measures adaptation distance, guiding robust learning.

𝑞𝑖𝑛(𝑗, 𝑠) = 𝑞(𝑗, 𝑠) + (0, ⋯ ,

𝑢2
2g

× sin 2∅ , … , 0) + 𝜖

(7)

In  equation  (7),  𝑞𝑖𝑛(𝑗, 𝑠)  is  the  estimated  optimum  adaptive  solution  in  the  case  of  distribution  shift;  𝑞(𝑗, 𝑠) 
represents the state of the current model; 𝑢2 is the adaptive update strength; 2g is scaling stabilization; 𝜙 is the 
constant parameters; 0 is the uncertainty added to ensure robustness. In this case, 𝜖 is in the range of -0.5 to 0.5, 
which increases uncertainty and noise-resistance in non-stationary data streams.

•

Jumping Behavior (Exploitation Phase): This phase refines solutions for gradual and recurrent shifts. 
The position update is expressed as (8):

𝑞(𝑗, 𝑠 + 1) = −(𝑞(𝑗, 𝑠) − 𝑞𝑖𝑛(𝑗, 𝑠)) 𝑓−(‖𝑞𝑖𝑛(𝑗,𝑠)−𝑞(𝑗,𝑠)‖2)2

+ 𝐾(𝑗, 𝑠)

(8)

𝑞(𝑗, 𝑠 + 1) denotes the updated candidate solution; 𝑞(𝑗, 𝑠) is the current solution; 𝑞𝑖𝑛(𝑗, 𝑠) represents the estimated 
optimal (target) solution; (∥⋅∥2) is the Euclidean norm measuring distance; 𝑓−(‖.‖2)2
 controls convergence; 𝐾(𝑗, 𝑠) 
is the local exploitation component refining parameters under distribution shifts.

𝑞𝑖𝑛(𝑗, 𝑠) = 𝑞(𝑗, 𝑠) + (0, ⋯ ,

𝑢2
2g

× sin 2∅ , … ,

𝑢2
2g

× sin2 ∅ , … , 0) + 𝜖

(9)

In equation (9), 𝑞𝑖𝑛(𝑗, 𝑠) is the estimated configuration of the target that should be followed in adaptation to the 
distribution shift; j is the index of the candidate; 𝑠 is the iteration;  𝑞(𝑗, 𝑠) is the reference state in which to update; 
sin2 ∅  determines the magnitude of the adaptive step; 𝑢2 determines the search intensity; 2𝑔 normalizes scaling; 
0 modulates exploration exploitation; 𝜖 introduces stochastic perturbation for robustness.

•  Lévy Flight Reinitialization: To avoid stagnation, Lévy-based random re-initialization is used (10):

𝑞𝑖𝑛(𝑗, 𝑠) = 𝑞(𝑗, 𝑠) + 𝜎 [𝑢1

𝑞1
(1
𝛽⁄ ), ⋯ , 𝑢𝑐

(1

𝑞𝑐
𝛽⁄ ) ]

(10)

𝑞𝑖𝑛(𝑗, 𝑠)  represents  the  reinitialized  solution  for  escaping  stagnation;  𝑞(𝑗, 𝑠)  is  the  previous  state;  𝜎  controls

𝑞𝑐
𝛽⁄ )  induces Lévy-flight-based step 
perturbation strength; 𝑢1and 𝑢𝑐 scales direction per dimension; 𝑢1
variation; 𝛽 regulates step distribution, enabling long jumps for improved adaptation under dynamic distribution 
shifts, it represent (11):

𝑞1
(1
𝛽⁄ ) and 𝑢𝑐

(1

Vol.6, No.2s, 2026                                                                                                                                                                            758

---

<!-- PAGE 6 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

𝑞𝑗~𝑒𝑚(0,  𝛾2), 𝛾 = (

Γ(𝛽+1)×sin(

𝜋𝛽
)
2

(

𝛽−1
2

)

×𝛽

Γ(

)×2
𝑢𝑗~𝑒𝑚(0,  𝛾́ 2), 𝛾́ = 1

𝛽+1
2

{

1
𝛽

)

, 𝑗𝜖{1, … , 𝑐}

, 𝑗𝜖{1, … , 𝑐}

(11)

where  𝑞𝑗~𝑒𝑚(0,  𝛾2)  produces  Levy-based  directional  components  to  search  in  a  global  scale;  𝑢𝑗~𝑒𝑚(0,  𝛾́ 2) 
provides  stabilized  stepwise  control;  𝑗 ∈ {1, … , 𝑐}  is  the  parameter  index  with  𝑐  total  dimensions;  𝑒𝑚(⋅)  is  the 
Gaussian sampling; 𝛾 and 𝛾́  is calculated using the Gamma function 𝛤(⋅)  and 𝜋𝛽 to control heavy-tailed search; 
𝛾́ = 1  ensures  normalized  variance.  In  general,  the  hybrid  AHO-InDNN  architecture  is  an  integration  of 
metaheuristic optimization with deep neural learning that enhances the parameter tuning, adaptive convergence, 
resistance to drift, and generalized prediction in changing conditions.

LDP for Enhancing Model Stability and Robustness 
LDP  measures  the  probability  of  exceptional  bursts  in  streaming  data  in  financial  systems.  It  differentiates 
between the normal variation, which can be a minor adjustment of a transaction, and the unusual and impactful 
variations (unauthorized transaction). LDP increases model responsiveness to important changes but is stable in 
ordinary behaviour by costing more for the rare patterns. Let {𝑋𝑠}s≥0  denote the incoming data stream. The LDP 
is defined as (12):

lim
𝑠 → ∞

1

𝑠

log 𝑃(𝑋𝑠 𝜖 𝐴) = −

Inf
𝑥𝜖𝐴

𝐼(𝑥)

(12)

Where 𝑠 denotes time in the streaming financial data, 𝑋𝑠 represents transaction stream, and 𝐴 indicates abnormal 
conditions. 𝑃(𝑋𝑠 𝜖 𝐴) denotes the probability of such events. The term 
 captures long-term behavior, while

lim
𝑠 → ∞

log reflects the exponential decay rate. The function 𝐼(𝑥) rarity of fraud behavior, and

represents the minimum

Inf
𝑥𝜖𝐴

deviation  cost,  where  higher  values  indicate  rarer  and  more  significant  distributional  shifts.  LDP  detects  rare 
distributional  shifts  related  to  fraud,  including  abrupt  increases  in  total  transactions  or  abnormal  spending 
behavior, to successfully distinguish between changes in normal/unusual fraud.

Result  
Results from experiments and an analysis of the suggested AHO-InDNN model's performance in non-stationary 
data environments using the Python tool. It evaluates the model’s effectiveness in handling concept drift through 
comparative analysis with baseline methods using standard classification metrics.

Figure 2: Analysis of Data Distribution Shift in Fraud Detection (a) Sudden, (b) Gradual, and (c) Recurrent 
Concept Drift

Figure 2 illustrates how fraud rates change over time under three different concept drift scenarios. In (A) Sudden 
Drift, the fraud rate sharply jumps at a specific point, showing an immediate shift from a low baseline (Concept C₁) 
to  a  higher  fraud  pattern  (Concept  C₂).  In  (B)  Gradual  Drift,  the  change  occurs  gradually  over  time,  the  model 
behavior gradually changes to another concept, and then stabilizes at a higher rate of fraud. In (C) Recurrent Drift, 
the system switches between low and high fraud rate patterns cyclically, with changes being cyclical with past 
ideas reoccurring with time. Combined, these plots illustrate that patterns of real-world fraud can dynamically 
change, and adaptive learning is necessary

Performance Evaluation

Vol.6, No.2s, 2026                                                                                                                                                                            759

---

<!-- PAGE 7 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

Python and standard libraries were used to carry out the experiments. The model has been trained and tested on 
PaySim data, in a simulated non-stationary environment with added distribution shifts. A measure of performance 
was the metrics of classification. The AHO-InDNN was contrasted with K-Nearest Neighbors (KNN) [18], Synthetic 
Minority  Over-Sampling  Technique  Boosting  (SMOTEBoost)  with  cost-sensitive  learning  [19],  and  Multi-Head 
Deep Recurrent Neural Network (MH-DRNN) [20].

To assess the effectiveness of the proposed framework towards detection of strong and adaptable fraud detection 
(Table  2  and  Figure  3)  to  distribution  changes,  the  following  measures  are  applied:  Accuracy,  the  ratio  of  the 
number of transactions correctly classified, is a measure that is used to measure the stability of the model when 
the data distributions change. Precision means how many of the predicted cases of fraud are actually fraudulent, 
decreasing false alarms in dynamic financial environments. Recall is the test that analyzes the identification of 
actual cases of fraud. F1-score is a measure that aims to balance both recall and precision and thus ensures a good 
overall performance.

Table 2: Performance Comparison of Models under Dynamic Distribution Shifts

Model

Accuracy (%)

KNN [18] 
SMOTEBoost + Cost-sensitive [19]  
MH-DRNN [20] 
AHO-InDNN [Proposed]

91.67 
- 
98.5 
98.74

Precision 
(%)  
- 
78 
97 
98.42

Recall (%)

95 
85 
98 
98.52

F1-score 
(%) 
93.33 
81 
97 
98.37

Figure 3:  Recall and F1-score Comparison for Robust Fraud Detection

In this research, AHO-InDNN achieves 98.74%, outperforming KNN and MH-DRNN. The proposed model records 
98.42%, exceeding SMOTEBoost and MH-DRNN. Overall, AHO-InDNN demonstrates strong adaptability, reliability, 
and high fraud detection capability in non-stationary environments.

Discussion  
The suggested AHO-InDNN model identifies abrupt, gradual and repetitive patterns of fraud drift, guaranteeing 
stable, adaptive, and precise outcomes in dynamic and unbalanced financial conditions with constantly changing 
distributions of transactions. Current techniques like KNN [18] are not adaptable because they are based on fixed 
learning, which restricts them in aspects of drift. SMOTEBoost [19] can better deal with class imbalance, yet it 
cannot easily deal with continuous distribution changes. MH-DRNN [20] is also highly sequential, but lacks real-
time adaptability and increased computational complexity in dynamic fraud situations. Conversely, the proposed 
AHO-InDNN  model  obtains  better  results.  This  enhancement  is  supported  through  drift-aware  learning,  online 
incremental, and uncertainty-informed optimization, which provides quick adaptation with a retention of learned 
knowledge. The framework is generally more robust, false detections are minimized, and generalization is better 
in the framework of constantly changing patterns of fraud.

Conclusion  
In the case of real-life financial systems, detecting fraud is difficult because of the ever-evolving behaviors of the 
transactions and the shift in the attack techniques. This study introduced an AHO-InDNN-driven adaptive system 
to deal with sudden, gradual and recurrent concept drift in streaming data by combining drift detection, online 
incremental learning, uncertainty-sensitive adaptation, and LDP-based optimization. Experimental performance

Vol.6, No.2s, 2026                                                                                                                                                                            760

---

<!-- PAGE 8 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

on PaySim data exhibits a high level of performance with 98.74% accuracy, 98.42% precision, 98.52% recall and 
98.37% F1-score and a low number of classification errors in the confusion matrix. The model is always superior 
to  the  existing  methods  and  it  is  very  robust  in  non-stationary  conditions.  The  suggested  solution  needs  to  be 
further elaborated to consider the intricacies of real-life financial systems. Future studies are needed to implement 
in real-time in a distributed environment, simplify lightweight architectures, reduce the cost of computation, scale 
up, and test the framework on actual financial data.

References  
1.  Liu, Z., Lu, J., Xuan, J. and Zhang, G., 2024. Deep reinforcement learning in nonstationary environments with

unknown change points. IEEE transactions on cybernetics, 54(9), pp.5191-5204. 
https://doi.org/10.1109/TCYB.2024.3356981

2.  Wang, T., Li, M., Zheng, R., Cai, C., Lou, Y. and Zhu, S., 2023. Towards continual knowledge transfer in

modeling manufacturing processes under non-stationary data streams: T. Wang et al. Applied Intelligence, 
53(23), pp.29393-29413.  https://doi.org/10.1007/s10489-023-05034-0

3.  Reis, M.J.C.S., 2026. Deep-Learning-Driven Adaptive Filtering for Non-Stationary Signals: Theory and

Simulation. Electronics, 15(2), p.381. https://doi.org/10.3390/electronics15020381

4.  Benatia, M.A., Hafsi, M. and Ayed, S.B., 2025. A continual learning approach for failure prediction under non-

stationary conditions: Application to condition monitoring data streams. Computers & Industrial 
Engineering, 204, p.111049. https://doi.org/10.1016/j.cie.2025.111049

5.  Halstead, B., Koh, Y.S., Riddle, P., Pears, R., Pechenizkiy, M., Bifet, A., Olivares, G. and Coulson, G., 2022.

Analyzing and repairing concept drift adaptation in data stream classification. Machine Learning, 111(10), 
pp.3489-3523. https://doi.org/10.1007/s10994-021-05993-w

6.  Ma, S., Yuan, Z., Wu, Q., Huang, Y., Hu, X., Leung, C.H., Wang, D. and Huang, Z., 2023. Deep into the domain 
shift: Transfer learning through dependence regularization. IEEE Transactions on Neural Networks and 
Learning Systems, 35(10), pp.14409-14423. https://doi.org/10.1109/TNNLS.2023.3279099  
7.  Li, J., Yu, H., Zhang, Z., Luo, X. and Xie, S., 2024. Concept drift adaptation by exploiting drift type. ACM 
Transactions on Knowledge Discovery from Data, 18(4), pp.1-22. https://doi.org/10.1145/3638777  
8.  Wang, M., Yang, N., Gunasinghe, D.H. and Weng, N., 2023. On the robustness of ML-based network intrusion

detection systems: An adversarial and distribution shift perspective. Computers, 12(10), p.209. 
https://doi.org/10.3390/computers12100209

9.  Shaheen, K., Hanif, M.A., Hasan, O. and Shafique, M., 2022. Continual learning for real-world autonomous

systems: Algorithms, challenges and frameworks. Journal of Intelligent & Robotic Systems, 105(1), p.9. 
https://doi.org/10.1007/s10846-022-01603-6

10.  Ghibi, O. and Weyns, D., 2024. Dealing with drift of adaptation spaces in learning-based self-adaptive

systems using lifelong self-adaptation. ACM Transactions on Autonomous and Adaptive Systems, 19(1), 
pp.1-57. https://doi.org/10.1145/3636428

11.  Cano, A. and Krawczyk, B., 2022. ROSE: robust online self-adjusting ensemble for continual learning on

imbalanced drifting data streams. Machine Learning, 111(7), pp.2561-2599. 
https://doi.org/10.1007/s10994-022-06168-x

12.  H. Moayyed, H. Abdeltawab, L. Gomes and Z. Vale, "Adaptive Federated Learning for Robust PV Power 
Forecasting Under Weather-Induced Concept Drift," in IEEE Access, vol. 13, pp. 193356-193376, 2025. 
https://10.1109/ACCESS.2025.3630992

13.  Pereira, E.V. and Da Silva, W.S., 2025. A comparison of approaches for handling concept drifts in data 
processed with machine learning. IEEE Access, 13, https://doi.org/10.1109/ACCESS.2025.3557229  
14.  Desale, K.S. and Shinde, S.V., 2023. Concept drift detection and adaption framework using optimized deep

learning and adaptive sliding window approach. Expert Systems, 40(9), p.e13394. 
https://doi.org/10.3390/app15063056

15.  Yu, X., Ruan, L., Evans, J.S. and Wong, E., 2025. Adaptive windowing-based concept drift detection and

adaptation framework for human-to-machine applications over future communication networks. Journal of 
Optical Communications and Networking, 17(4), pp.338-351. https://doi.org/10.1364/JOCN.538964

16.  Mehmood, T., Latif, S., Latif, R., Majeed, H. and Malik, A.W., 2024. DRIFTNET-EnVACK: adaptive drift

detection in cloud data streams with ensemble variational auto-encoder featuring contextual network. IEEE 
Access, 12, pp.80020-80034. https://doi.org/10.1109/ACCESS.2024.3409433

17.  Friedrich, B., Sawabe, T. and Hein, A., 2023. Unsupervised statistical concept drift detection for behaviour 
abnormality detection. Applied Intelligence, 53(3), pp.2527-2537. https://doi.org/10.1007/s10489-022-
03611-3

18.  Usman, A.U., Abdullahi, S.B., Liping, Y., Alghofaily, B., Almasoud, A.S. and Rehman, A., 2024. Financial fraud 
detection using value-at-risk with machine learning in skewed data. Ieee Access, 12, pp.64285-64299. 
https://doi.org/10.1109/ACCESS.2024.3393154

Vol.6, No.2s, 2026                                                                                                                                                                            761

---

<!-- PAGE 9 -->

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

19.  Al-Daoud, K.I. and Abu-AlSondos, I.A., 2025. Robust AI for financial fraud detection in the GCC: A hybrid

framework for imbalance, drift, and adversarial threats. Journal of Theoretical and Applied Electronic 
Commerce Research, 20(2), p.121. https://doi.org/10.3390/jtaer20020121

20.  Wang, L., 2026. MH-DRNN: An intelligent approach in financial fraud detection and prevention. Systems and

Soft Computing, p.200483. https://doi.org/10.1016/j.sasc.2026.200483

Vol.6, No.2s, 2026                                                                                                                                                                            762

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
International Journal of Artificial
Intelligence and Machine Learning
SvedbergOpen Publisher's Home Page: https://www.svedbergopen.com/
DISSEMINATION OF KNOWLEDGE
Research Paper Open Access
Robust Learning Under Distribution Shifts for Non-Stationary
Data Environments
Rekha D1 , Shanthi Vairavan², Sunil MP³, Jitendra Kumar Katariya⁴, Swapnil Maheshkumar Parikh⁵, T.
Shanthi⁶, Shanthi R⁷
1Assistant Professor Vel Tech Multi Tech Dr.Rangarajan Dr.Sakunthala Engineering College Chennai – 600062
rekhadharma23@gmail.com
² Professor, Computer Science, Meenakshi College of Arts and Science, Meenakshi Academy of Higher Education and Research, India
³ Assistant Professor, Department of Electronics and Communication Engineering, Faculty of Engineering and Technology, JAIN
(Deemed-to-be University), Bengaluru, Karnataka, India. Email: mp.sunil@jainuniversity.ac.in, ORCID: 0000-0002-7737-4145
⁴ Assistant Professor, Department of Computer Science & Application, Vivekananda Global University, Jaipur, India. Email:
jitendra.kumar.katariya@vgu.ac.in, ORCID: 0009-0000-9940-9022
⁵ Professor, Department of Computer Science and Engineering, Faculty of Engineering and Technology, Parul Institute of
Technology, Parul University, Vadodara, Gujarat, India. Email: swapnil.parikh17761@paruluniversity.ac.in, ORCID: 0000-0001-
7831-6927
⁶ Associate Professor, Department of Electronics and Communication Engineering, Sona College of Technology, India. Email:
shanthi@sonatech.ac.in, ORCID: 0000-0001-8962-5311
⁷ Assistant Professor, Department of Mathematics, Meenakshi College of Arts and Science, Meenakshi Academy of Higher Education
and Research, India
Abstract
Keyword: Robust Learning, Distribution Shift, Non-Stationary Data, Concept Drift, Adaptive Learning Systems, Deep Learning
Introduction
Contemporary ML systems are dynamic and constantly produce data that defies the notion of fixed distribution [1,
2]. The data properties in non-stationary environments evolve due to the user behavior, the system dynamics, or
external forces, and thus learning becomes more complicated [3]. The most important problems are the
distribution shift whereby training and testing data is not the same [4]. It is concept drift, where there is a shift in
input-output relations, and domain shift, where there is a shift in input distributions, but the same task is being
done [5, 6].
These models are primarily trained in a stationary form, without a continuous adaptation process [7, 8]. Thus, the
performance is worse when the distributions are varied, which leads to a loss of accuracy in practice and
inaccuracy in generalization [9]. This weakness offers the necessity to possess flexible and strong learning systems
Vol.6, No.2s, 2026 754

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
that can deal with the shifting flows of information. The best system must be able to recognize the patterns of data
change, continuously update itself, and be capable of maintaining its performance at all times without full
retraining [10, 11].
To alleviate these issues, the proposed presents a potent learning model in non-stationary environments with
AHO-InDNN to balance exploration and exploitation. It is a combination of the drift detection and online
incremental learning to adapt dynamically. An LDP-based optimization strategy increases stability and minimises
uncertainty. The key contributions can be summed up as follows:
• Developed an AHO-InDNN adaptive learning framework integrated with drift detection, online learning,
and incremental updating for non-stationary environments.
• Introduced an LDP-based parameter optimization strategy to improve robustness, stability, and reliable
decision-making under dynamic uncertainty.
• Performed comprehensive evaluation demonstrating superior performance under sudden, gradual, and
recurrent distribution shift scenarios compared with baseline models.
The remaining structure of this research was as follows: Section 2 reviews the literature in robust learning in
distribution shifts. Section 3 develops the suggested non-stationary data. Section 4 describes the implementation
and design of the model. Section 5 evaluates results of performance. The section 6 ends with conclusion and future
research directions.
Literature review
The concept drift research has been extensively studied in the fields of forecasting, streaming analytics, healthcare,
and financial systems. Research [12] enhances Photovoltaic (PV) prediction based on adaptive federated learning
with dual drift detection and selective retraining with a smaller Root Mean Square Error (RMSE) and faster
adaptation, but was restricted by threshold tuning and poor real-world diversity. Likewise, the research [13]
compares several adaptive classifiers in the concept drift context based on the scikit-multiflow framework,
demonstrating the adaptability of models in a variety of algorithms though lacks real-life validation and more
rigorous analysis of optimization.
Deep learning-based drift detection was explored in [14] using a DNN combined with an autoencoder (DNN+AE-
DD), where reconstruction error and the 3σ rule are used for drift identification. Despite its sensitivity, it does not
have a good cross-domain generalization. In network systems, [15] has used adaptive windowing with H2M
networks, which are better with respect to latency and response, but it is based on pre-established traffic
assumptions. In the same vein, [16] trained an ensemble variational autoencoder with Kolmogorov-Smirnoff
testing to detect cloud drift, with high F-scores but high computational and scalability cost. In additional, [17] used
variational autoencoders with KL-divergence testing to identify abnormal behavior in older adults, with over 91%
F1-score, but was limited to small sample size and generalizability.
Research Gap
Although concept drift and non-stationary data management have advanced, current approaches are still
disjointed, focusing on drift detection, adaptive learning, or optimization individually. Various methods are based
on threshold-driven mechanisms, minimizing resilience to changing distributions. Some of the models are also less
adaptable and have poor generalization in the real world. Moreover, model uncertainty and robustness
optimization are under-explored, and certain methods are costly to compute or may need dataset-specific
optimization. To address these issues, this research proposes a robust framework integrating lightweight drift
detection with AHO-InDNN for online and incremental learning, enhanced with uncertainty-aware optimization
and a LDP-based robustness evaluation to improve stability and adaptability.
Problem formulation
Training and testing data in ML were assumed to share the same underlying distribution, represented as:
𝑄 (𝑌,𝑋)=𝑄 (𝑌,𝑋). However, in the dynamic and real-world scenarios the assumption is not always true
𝑇𝑟𝑎𝑖𝑛 𝑇𝑒𝑠𝑡
since data distributions evolve with time as customers adjust their behavior, new fraud strategies are invented,
seasonal spending trends and dynamics of online payments. To give an example, the tendencies of fraud that could
be traced in the previous weeks may be ineffective now as the fraudsters are coming up with other types of
transactions or disguises. This breakdown can be formally stated as: 𝑄 (𝑌,𝑋)≠𝑄 (𝑌,𝑋). Progressive model
𝑇𝑟𝑎𝑖𝑛 𝑇𝑒𝑠𝑡
performance deterioration is caused by distributional mismatch. To be more specific, concept drift is change in the
𝑚
conditional distribution between input and output over time: 𝑄(𝑌|𝑋) ≠𝑄(𝑌|𝑋) . Let 𝐶 ={(𝑦 ,𝑥 )} denote
𝑠 𝑠+1 𝑠 𝑗 𝑗 𝑗=1
Vol.6, No.2s, 2026 755

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
data at time 𝑠, and 𝑒 represent the model with parameters 𝜃 . The goal is to minimize the expected loss in
𝜃 𝑠
moderating distributions: 𝐾 (𝜃)=𝔼 [ℓ(𝑒 (𝑌),𝑋)]. To handle this dynamic environment, the model is
𝑠 (𝑌,𝑋)~𝑄𝑠 𝜃
incrementally updated at each time step: 𝜃 =𝜃 +∆𝜃 . Where ∆𝜃 is adaptively learned using the drift-directed
𝑠+1 𝑠 𝑠 𝑠
uncertainty estimation-based optimization strategy based on the AHO approach.
Methodology
The methodology suggests a solid adaptive learning model of non-stationary data settings, as demonstrated in
Figure 1. It is created to operate on continuous data streams in which distributions can vary because of abrupt,
gradual or periodic drift. In contrast to the static models, the framework constantly checks incoming data and
updates the model to maintain prediction accuracy in the changing conditions.
Figure 1: Proposed Robust Adaptive Learning Framework for Non-Stationary Environments
The model consists of four modules; data input, drift detection, adaptive learning and output prediction. Streaming
data are preprocessed and analyzed to detect concept drift through statistical and feature changes. After the drift,
the AHO-InDNN model re-estimates the parameters to learn effectively. Incremental and online learning allows
constant adaptation without re-training. LDP-based mechanism minimizes the uncertainty and stabilizes updates,
and distributed learning increases the scalability and computational efficiency of multiple nodes.
Dataset
The research utilizes PaySim artificial mobile money transaction data in Kaggle
(https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset), which was developed to
replicate actual financial transactions without compromising their privacy. It contains 30 days of sequential
transaction records (743 time steps) with types including CASH-IN, CASH-OUT, PAYMENT, DEBIT, and
TRANSFER. Features include transaction amount, time step, anonymized user IDs, and fraud label. It has a time-
series structure that can be used in concept drift analysis, adaptive learning, and fraud detection in the changing
transaction patterns.
Min-Max Normalization for Scaling Input Data into a Uniform Range
To ensure stable learning and faster convergence, Min–Max normalization is applied to numerical features, scaling
values into the range [0,1]. This reduces magnitude variation and improves robustness under distribution shifts,
as expressed in Equation (1).
𝑦′ = 𝑦−𝑦𝑚𝑖𝑛 (1)
𝑦𝑚𝑎𝑥−𝑦𝑚𝑖𝑛
Where 𝑦 is dynamic data patterns as raw transaction feature; 𝑦 observed value as a way to maintain lower-
𝑚𝑖𝑛
bound stability; 𝑦 is observed value as a way to maintain scale variation; 𝑦′ prime normalized feature as a way
𝑚𝑎𝑥
to allow robust and drift-resilient learning.
Drift Detection Module for Identifying Concept Drift
Vol.6, No.2s, 2026 756

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
The drift detection module of the proposed framework tracks transaction streams to detect changes in the data
distribution. It initiates a change in the model when a drastic change is detected to reduce the overall cost of the
computation and to retain the high detection levels. The model includes three types of concept drift, like sudden
(immediate adaptation), gradual (patterns change gradually as learning progresses slowly), and recurrent
(patterns repeat with the use of historical knowledge). These drifts are due to the rapid change of fraud strategies
(Table 1), changing user spending behavior, and periodic attack cycles in the fraud detection systems, and adaptive
learning is a solution to maintain strong performance.
Table 1. Types of Concept Drift and Examples
Drift Type Description Real-World Example
Sudden Drift Abrupt change in data distribution New fraud attack pattern
Gradual Drift Slow, continuous changes over time Slowly changing user spending behavior
Recurrent Drift Periodic, repeating patterns Seasonal fraud campaigns
Hybrid statistical divergence and mean shift enhance the drift detection by being more sensitive to the changes of
the distribution and less prone to false positives and stable.
Online & Incremental Learning for Continuous Model Adaptation
The framework online incremental learning module to revise the model as it notices changes in distribution. The
model is retrained using the new information received, and is not retrained entirely, which is effective in adapting
and preserving previously learnt information. This is the selective means of learning that allows the system to
optimize its parameters continuously by new streams of data and uncertainty data. This is particularly essential
in fraud detection, as transaction patterns tend to fluctuate as the attackers change their methods of fraud, as their
behavior changes, and new patterns of attack emerge. The suggested approach allows constant adaptation,
minimizes the computational cost, and is stable in non-stationary conditions. It enhances the reliability of
prediction and a robust performance in dynamic and imbalanced transaction flows, which are effective in
performing real-time fraud detection.
InDNN for Robust Learning under Distribution Shifts
InDNN is designed to deal with non-stationary data situations that are affected by concept drift and domain
variability. It has a three-layer architecture, with input, multiple hidden layers, and output. Unlike standard DNNs,
InDNN employs dynamic depth and neuron structure to be robust. It has 64 input neurons, as many as seven
hidden layers, and 64 output neurons to learn high-dimensional features. A parameter tuning strategy controls
the hidden neurons in a dynamic manner to prevent overfitting and underfitting. The neuron output is defined as
(3):
𝑥𝑚+1 =𝜎(𝑤)=𝜎(∑𝑛 𝜔𝑚+𝜔𝑛+1) (2)
𝑝 𝑗=1 𝑗𝑝 𝑝
where 𝜎(𝑤) is the activation function, 𝑥𝑚+1 denotes the output of the 𝑝𝑡ℎ neuron in layer 𝑚+1, 𝜔𝑚 represents
𝑝 𝑗𝑝
weights, and 𝜔𝑛+1 denotes bias. The ReLU activation function is employed to ensure efficient gradient propagation
𝑝
and adaptability under shifting data distributions. To explicitly handle uncertainty caused by distribution shifts, a
regularized loss function 𝐹(𝜃) is used (3):
1
𝐹(𝜃)=− ∑ ∑ 𝑠 log𝑥 (3)
𝑀 𝑚 𝑝 𝑚𝑝 𝑚𝑝
where ∑ denotes aggregation over all samples and classes; 𝑠 is the true label, log𝑥 is the predicted output,
𝑚𝑝 𝑚𝑝
𝜃 ={𝜔,𝑏}, and 𝐹(𝜃) is a robustness regularization term that mitigates overfitting under drift conditions. To
optimize the parameters efficiently in dynamic environments, an adaptive moment-based gradient optimization
is employed (4):
𝜃 =𝜃 −∝
𝛽1𝑚𝑠−1+(1−𝛽1) ∇𝜃𝐹(𝜃𝑠−1)
(4)
𝑠 𝑠−1
√𝛽2𝑣𝑠−1+(1−𝛽2) ( ∇𝜃𝐹(𝜃𝑠−1)) 2 +𝜖
Where 𝜃 updated parameters, 𝜃 previous state, ∝ learning rate, 𝛽 ,𝛽 decay factors, 𝑚 ,𝑣 gradient
𝑠 𝑠−1 1 2 𝑠−1 𝑠−1
moments, ∇ 𝐹(𝜃 ) current gradient, and 𝜖 ensures stability under distribution shifts. Dropout improves
𝜃 𝑠−1
generalization under unseen shifts, while drift-aware updates enable incremental learning when significant
distribution changes are detected.
Vol.6, No.2s, 2026 757

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

AHO for Optimal Parameter Tuning
The AHO method is used in this research to improve the AHO-InDNN model's parameter setting and adaptive
learning in non-stationary situations. AHO balances exploration and exploitation to handle distribution shifts such
as concept drift and domain variability, inspired by the hunting behavior of archerfish, where each agent
represents a candidate solution of network parameters, hyperparameters, and adaptation strategies.
•  Population Initialization: Initially, the population of archerfish is randomly generated within the
defined search space. The initial position of the 𝑗th archerfish is given as (5):
| 𝑞(𝑗,0)=[(𝑞𝐾+𝜎 | (𝑞𝑉−𝑞𝐾)),⋯ | , (𝑞𝐾+𝜎 | (𝑞𝑉−𝑞𝐾))]  |     |     |     | (5)  |
| ------------- | ---------- | ------- | ---------- | --- | --- | --- | ---- |
|               | 1 1 1      | 1       | 𝑐 𝑐        | 𝑐 𝑐 |     |     |      |
Where 𝑞(𝑗,0) denotes the initial candidate solution; 𝑗 is the archerfish index; 𝑐 is dimensionality; 𝑞𝐾 and 𝑞𝑉
𝑐 𝑐
represent lower (𝐾) and upper (𝑉) bounds of parameters; 𝜎 ∈[0,1] ensures randomness for diversity and
𝑐
robustness under distribution shifts.
•  Shooting Behavior (Exploration Phase):  This phase performs global search to adapt to sudden
distribution changes. The position update is defined as (6):
(𝑗,𝑠)) 𝑓−(‖𝑞𝑖𝑛(𝑗,𝑠)−𝑞(𝑗,𝑠)‖2)2
| 𝑞(𝑗,𝑠+1)=−(𝑞(𝑗,𝑠)−𝑞 |     |     |     |     | +𝑞(𝑗,𝑠)  |     | (6)  |
| ------------------- | --- | --- | --- | --- | -------- | --- | ---- |
𝑖𝑛
Where 𝑞(𝑗,𝑠+1) denotes the updated proposed model parameters; 𝑞(𝑗,𝑠) is the current parameter set of the 𝑗𝑡ℎ
candidate model; 𝑞 (𝑗,𝑠) is the estimated optimal solution under distribution shift; 𝑗 is candidate index; 𝑠 is
𝑖𝑛
iteration; ∥⋅∥2 measures adaptation distance, guiding robust learning.
𝑢2
| 𝑞 (𝑗,𝑠)=𝑞(𝑗,𝑠)+(0,⋯, |     | ×sin2∅,…,0)+𝜖  |     |     |     |     | (7)  |
| -------------------- | --- | -------------- | --- | --- | --- | --- | ---- |
𝑖𝑛
2g
In equation (7), 𝑞 (𝑗,𝑠) is the estimated optimum adaptive solution in the case of distribution shift; 𝑞(𝑗,𝑠)
𝑖𝑛
represents the state of the current model; 𝑢2 is the adaptive update strength; 2g is scaling stabilization; 𝜙 is the
constant parameters; 0 is the uncertainty added to ensure robustness. In this case, 𝜖 is in the range of -0.5 to 0.5,
which increases uncertainty and noise-resistance in non-stationary data streams.
•  Jumping Behavior (Exploitation Phase): This phase refines solutions for gradual and recurrent shifts.
The position update is expressed as (8):
(𝑗,𝑠)) 𝑓−(‖𝑞𝑖𝑛(𝑗,𝑠)−𝑞(𝑗,𝑠)‖2)2
| 𝑞(𝑗,𝑠+1)=−(𝑞(𝑗,𝑠)−𝑞 |     |     |     |     | +𝐾(𝑗,𝑠)  |     | (8)  |
| ------------------- | --- | --- | --- | --- | -------- | --- | ---- |
𝑖𝑛
𝑞(𝑗,𝑠+1) denotes the updated candidate solution; 𝑞(𝑗,𝑠) is the current solution; 𝑞 (𝑗,𝑠) represents the estimated
𝑖𝑛
optimal (target) solution; (∥⋅∥2) is the Euclidean norm measuring distance; 𝑓−(‖.‖2)2
 controls convergence; 𝐾(𝑗,𝑠)
is the local exploitation component refining parameters under distribution shifts.
|                      |     | 𝑢2       | 𝑢2               |     |     |     |      |
| -------------------- | --- | -------- | ---------------- | --- | --- | --- | ---- |
| 𝑞 (𝑗,𝑠)=𝑞(𝑗,𝑠)+(0,⋯, |     | ×sin2∅,… | , ×sin2∅,…,0)+𝜖  |     |     |     | (9)  |
| 𝑖𝑛                   |     | 2g       | 2g               |     |     |     |      |
In equation (9), 𝑞 (𝑗,𝑠) is the estimated configuration of the target that should be followed in adaptation to the
𝑖𝑛
distribution shift; j is the index of the candidate; 𝑠 is the iteration;  𝑞(𝑗,𝑠) is the reference state in which to update;
sin2∅  determines the magnitude of the adaptive step; 𝑢2 determines the search intensity; 2𝑔 normalizes scaling;
0 modulates exploration exploitation; 𝜖 introduces stochastic perturbation for robustness.
•  Lévy Flight Reinitialization: To avoid stagnation, Lévy-based random re-initialization is used (10):
𝑞1 𝑞𝑐
(1⁄𝛽),⋯,𝑢 (1⁄𝛽) ]
| 𝑞 (𝑗,𝑠)=𝑞(𝑗,𝑠)+𝜎[𝑢 |     |     |     |     |     |     | (10)  |
| ------------------ | --- | --- | --- | --- | --- | --- | ----- |
| 𝑖𝑛                 |     | 1 𝑐 |     |     |     |     |       |
𝑞 𝑖𝑛 (𝑗,𝑠) represents the reinitialized solution for escaping stagnation; 𝑞(𝑗,𝑠) is the previous state; 𝜎 controls
|                          |                                          |     |     | 𝑞1          | 𝑞𝑐                                     |     |     |
| ------------------------ | ---------------------------------------- | --- | --- | ----------- | -------------------------------------- | --- | --- |
|                          |                                          |     |     | (1⁄𝛽) and 𝑢 | (1⁄𝛽)  induces Lévy-flight-based step  |     |     |
| perturbation strength; 𝑢 | and 𝑢  scales direction per dimension; 𝑢 |     |     |             |                                        |     |     |
| 1                        | 𝑐                                        |     |     | 1           | 𝑐                                      |     |     |
variation; 𝛽 regulates step distribution, enabling long jumps for improved adaptation under dynamic distribution
shifts, it represent (11):
Vol.6, No.2s, 2026                                                                                                                                                                            758

www.svedbergopen.com                            International Journal of Artificial Intelligence and Machine Learning

1
|          |           |             |         | 𝛽          |     |     |         |
| -------- | --------- | ----------- | ------- | ---------- | --- | --- | ------- |
|          |           | Γ(𝛽+1)×sin( | 𝜋𝛽 )    |            |     |     |         |
|          | (0, 𝛾2),𝛾 |             | 2       | ,𝑗𝜖{1,…,𝑐} |     |     |         |
| 𝑞 𝑗 ~𝑒 𝑚 |           | =(          | )       |            |     |     |   (11)  |
|          |           |             | ( 𝛽−1 ) |            |     |     |         |
|          |           | Γ( 𝛽+1 )×2  | 2 ×𝛽    |            |     |     |         |
2

| {   | 𝑢 ~𝑒 (0, 𝛾́2),𝛾́ | =1  |     | ,𝑗𝜖{1,…,𝑐} |     |     |     |
| --- | ---------------- | --- | --- | ---------- | --- | --- | --- |
𝑗 𝑚
where 𝑞 ~𝑒 (0, 𝛾2) produces Levy-based directional components to search in a global scale; 𝑢 ~𝑒 (0, 𝛾́2)
| 𝑗 𝑚 |     |     |     |     |     |     | 𝑗 𝑚 |
| --- | --- | --- | --- | --- | --- | --- | --- |
provides stabilized stepwise control; 𝑗 ∈{1,…,𝑐} is the parameter index with 𝑐 total dimensions; 𝑒 (⋅) is the
𝑚
Gaussian sampling; 𝛾 and 𝛾́ is calculated using the Gamma function 𝛤(⋅)  and 𝜋𝛽 to control heavy-tailed search;
𝛾́ =1  ensures  normalized  variance.  In  general,  the  hybrid  AHO-InDNN  architecture  is  an  integration  of
metaheuristic optimization with deep neural learning that enhances the parameter tuning, adaptive convergence,
resistance to drift, and generalized prediction in changing conditions.
LDP for Enhancing Model Stability and Robustness
LDP measures the probability of exceptional bursts in streaming data in financial systems. It differentiates
between the normal variation, which can be a minor adjustment of a transaction, and the unusual and impactful
variations (unauthorized transaction). LDP increases model responsiveness to important changes but is stable in
ordinary behaviour by costing more for the rare patterns. Let {𝑋𝑠}  denote the incoming data stream. The LDP
s≥0
is defined as (12):
| lim  | 1      |         | Inf   |     |     |     |       |
| ---- | ------ | ------- | ----- | --- | --- | --- | ----- |
|      | log𝑃(𝑋 |  𝜖 𝐴)=− | 𝐼(𝑥)  |     |     |     | (12)  |
| 𝑠→∞𝑠 |        | 𝑠       | 𝑥𝜖𝐴   |     |     |     |       |
Where 𝑠 denotes time in the streaming financial data, 𝑋  represents transaction stream, and 𝐴 indicates abnormal
𝑠
lim
conditions. 𝑃(𝑋  𝜖 𝐴) denotes the probability of such events. The term   captures long-term behavior, while
| 𝑠   |     |     |     |     |     | 𝑠→∞ |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Inf
log reflects the exponential decay rate. The function 𝐼(𝑥) rarity of fraud behavior, and   represents the minimum
𝑥𝜖𝐴
deviation cost, where higher values indicate rarer and more significant distributional shifts. LDP detects rare
distributional shifts related to fraud, including abrupt increases in total transactions or abnormal spending
behavior, to successfully distinguish between changes in normal/unusual fraud.
Result
Results from experiments and an analysis of the suggested AHO-InDNN model's performance in non-stationary
data environments using the Python tool. It evaluates the model’s effectiveness in handling concept drift through
comparative analysis with baseline methods using standard classification metrics.

Figure 2: Analysis of Data Distribution Shift in Fraud Detection (a) Sudden, (b) Gradual, and (c) Recurrent
Concept Drift
Figure 2 illustrates how fraud rates change over time under three different concept drift scenarios. In (A) Sudden
Drift, the fraud rate sharply jumps at a specific point, showing an immediate shift from a low baseline (Concept C₁)
to a higher fraud pattern (Concept C₂). In (B) Gradual Drift, the change occurs gradually over time, the model
behavior gradually changes to another concept, and then stabilizes at a higher rate of fraud. In (C) Recurrent Drift,
the system switches between low and high fraud rate patterns cyclically, with changes being cyclical with past
ideas reoccurring with time. Combined, these plots illustrate that patterns of real-world fraud can dynamically
change, and adaptive learning is necessary
Performance Evaluation
Vol.6, No.2s, 2026                                                                                                                                                                            759

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
Python and standard libraries were used to carry out the experiments. The model has been trained and tested on
PaySim data, in a simulated non-stationary environment with added distribution shifts. A measure of performance
was the metrics of classification. The AHO-InDNN was contrasted with K-Nearest Neighbors (KNN) [18], Synthetic
Minority Over-Sampling Technique Boosting (SMOTEBoost) with cost-sensitive learning [19], and Multi-Head
Deep Recurrent Neural Network (MH-DRNN) [20].
To assess the effectiveness of the proposed framework towards detection of strong and adaptable fraud detection
(Table 2 and Figure 3) to distribution changes, the following measures are applied: Accuracy, the ratio of the
number of transactions correctly classified, is a measure that is used to measure the stability of the model when
the data distributions change. Precision means how many of the predicted cases of fraud are actually fraudulent,
decreasing false alarms in dynamic financial environments. Recall is the test that analyzes the identification of
actual cases of fraud. F1-score is a measure that aims to balance both recall and precision and thus ensures a good
overall performance.
Table 2: Performance Comparison of Models under Dynamic Distribution Shifts
Model Accuracy (%) Precision Recall (%) F1-score
(%) (%)
KNN [18] 91.67 - 95 93.33
SMOTEBoost + Cost-sensitive [19] - 78 85 81
MH-DRNN [20] 98.5 97 98 97
AHO-InDNN [Proposed] 98.74 98.42 98.52 98.37
Figure 3: Recall and F1-score Comparison for Robust Fraud Detection
In this research, AHO-InDNN achieves 98.74%, outperforming KNN and MH-DRNN. The proposed model records
98.42%, exceeding SMOTEBoost and MH-DRNN. Overall, AHO-InDNN demonstrates strong adaptability, reliability,
and high fraud detection capability in non-stationary environments.
Discussion
The suggested AHO-InDNN model identifies abrupt, gradual and repetitive patterns of fraud drift, guaranteeing
stable, adaptive, and precise outcomes in dynamic and unbalanced financial conditions with constantly changing
distributions of transactions. Current techniques like KNN [18] are not adaptable because they are based on fixed
learning, which restricts them in aspects of drift. SMOTEBoost [19] can better deal with class imbalance, yet it
cannot easily deal with continuous distribution changes. MH-DRNN [20] is also highly sequential, but lacks real-
time adaptability and increased computational complexity in dynamic fraud situations. Conversely, the proposed
AHO-InDNN model obtains better results. This enhancement is supported through drift-aware learning, online
incremental, and uncertainty-informed optimization, which provides quick adaptation with a retention of learned
knowledge. The framework is generally more robust, false detections are minimized, and generalization is better
in the framework of constantly changing patterns of fraud.
Conclusion
In the case of real-life financial systems, detecting fraud is difficult because of the ever-evolving behaviors of the
transactions and the shift in the attack techniques. This study introduced an AHO-InDNN-driven adaptive system
to deal with sudden, gradual and recurrent concept drift in streaming data by combining drift detection, online
incremental learning, uncertainty-sensitive adaptation, and LDP-based optimization. Experimental performance
Vol.6, No.2s, 2026 760

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
on PaySim data exhibits a high level of performance with 98.74% accuracy, 98.42% precision, 98.52% recall and
98.37% F1-score and a low number of classification errors in the confusion matrix. The model is always superior
to the existing methods and it is very robust in non-stationary conditions. The suggested solution needs to be
further elaborated to consider the intricacies of real-life financial systems. Future studies are needed to implement
in real-time in a distributed environment, simplify lightweight architectures, reduce the cost of computation, scale
up, and test the framework on actual financial data.
References
1. Liu, Z., Lu, J., Xuan, J. and Zhang, G., 2024. Deep reinforcement learning in nonstationary environments with
unknown change points. IEEE transactions on cybernetics, 54(9), pp.5191-5204.
https://doi.org/10.1109/TCYB.2024.3356981
2. Wang, T., Li, M., Zheng, R., Cai, C., Lou, Y. and Zhu, S., 2023. Towards continual knowledge transfer in
modeling manufacturing processes under non-stationary data streams: T. Wang et al. Applied Intelligence,
53(23), pp.29393-29413. https://doi.org/10.1007/s10489-023-05034-0
3. Reis, M.J.C.S., 2026. Deep-Learning-Driven Adaptive Filtering for Non-Stationary Signals: Theory and
Simulation. Electronics, 15(2), p.381. https://doi.org/10.3390/electronics15020381
4. Benatia, M.A., Hafsi, M. and Ayed, S.B., 2025. A continual learning approach for failure prediction under non-
stationary conditions: Application to condition monitoring data streams. Computers & Industrial
Engineering, 204, p.111049. https://doi.org/10.1016/j.cie.2025.111049
5. Halstead, B., Koh, Y.S., Riddle, P., Pears, R., Pechenizkiy, M., Bifet, A., Olivares, G. and Coulson, G., 2022.
Analyzing and repairing concept drift adaptation in data stream classification. Machine Learning, 111(10),
pp.3489-3523. https://doi.org/10.1007/s10994-021-05993-w
6. Ma, S., Yuan, Z., Wu, Q., Huang, Y., Hu, X., Leung, C.H., Wang, D. and Huang, Z., 2023. Deep into the domain
shift: Transfer learning through dependence regularization. IEEE Transactions on Neural Networks and
Learning Systems, 35(10), pp.14409-14423. https://doi.org/10.1109/TNNLS.2023.3279099
7. Li, J., Yu, H., Zhang, Z., Luo, X. and Xie, S., 2024. Concept drift adaptation by exploiting drift type. ACM
Transactions on Knowledge Discovery from Data, 18(4), pp.1-22. https://doi.org/10.1145/3638777
8. Wang, M., Yang, N., Gunasinghe, D.H. and Weng, N., 2023. On the robustness of ML-based network intrusion
detection systems: An adversarial and distribution shift perspective. Computers, 12(10), p.209.
https://doi.org/10.3390/computers12100209
9. Shaheen, K., Hanif, M.A., Hasan, O. and Shafique, M., 2022. Continual learning for real-world autonomous
systems: Algorithms, challenges and frameworks. Journal of Intelligent & Robotic Systems, 105(1), p.9.
https://doi.org/10.1007/s10846-022-01603-6
10. Ghibi, O. and Weyns, D., 2024. Dealing with drift of adaptation spaces in learning-based self-adaptive
systems using lifelong self-adaptation. ACM Transactions on Autonomous and Adaptive Systems, 19(1),
pp.1-57. https://doi.org/10.1145/3636428
11. Cano, A. and Krawczyk, B., 2022. ROSE: robust online self-adjusting ensemble for continual learning on
imbalanced drifting data streams. Machine Learning, 111(7), pp.2561-2599.
https://doi.org/10.1007/s10994-022-06168-x
12. H. Moayyed, H. Abdeltawab, L. Gomes and Z. Vale, "Adaptive Federated Learning for Robust PV Power
Forecasting Under Weather-Induced Concept Drift," in IEEE Access, vol. 13, pp. 193356-193376, 2025.
https://10.1109/ACCESS.2025.3630992
13. Pereira, E.V. and Da Silva, W.S., 2025. A comparison of approaches for handling concept drifts in data
processed with machine learning. IEEE Access, 13, https://doi.org/10.1109/ACCESS.2025.3557229
14. Desale, K.S. and Shinde, S.V., 2023. Concept drift detection and adaption framework using optimized deep
learning and adaptive sliding window approach. Expert Systems, 40(9), p.e13394.
https://doi.org/10.3390/app15063056
15. Yu, X., Ruan, L., Evans, J.S. and Wong, E., 2025. Adaptive windowing-based concept drift detection and
adaptation framework for human-to-machine applications over future communication networks. Journal of
Optical Communications and Networking, 17(4), pp.338-351. https://doi.org/10.1364/JOCN.538964
16. Mehmood, T., Latif, S., Latif, R., Majeed, H. and Malik, A.W., 2024. DRIFTNET-EnVACK: adaptive drift
detection in cloud data streams with ensemble variational auto-encoder featuring contextual network. IEEE
Access, 12, pp.80020-80034. https://doi.org/10.1109/ACCESS.2024.3409433
17. Friedrich, B., Sawabe, T. and Hein, A., 2023. Unsupervised statistical concept drift detection for behaviour
abnormality detection. Applied Intelligence, 53(3), pp.2527-2537. https://doi.org/10.1007/s10489-022-
03611-3
18. Usman, A.U., Abdullahi, S.B., Liping, Y., Alghofaily, B., Almasoud, A.S. and Rehman, A., 2024. Financial fraud
detection using value-at-risk with machine learning in skewed data. Ieee Access, 12, pp.64285-64299.
https://doi.org/10.1109/ACCESS.2024.3393154
Vol.6, No.2s, 2026 761

www.svedbergopen.com International Journal of Artificial Intelligence and Machine Learning
19. Al-Daoud, K.I. and Abu-AlSondos, I.A., 2025. Robust AI for financial fraud detection in the GCC: A hybrid
framework for imbalance, drift, and adversarial threats. Journal of Theoretical and Applied Electronic
Commerce Research, 20(2), p.121. https://doi.org/10.3390/jtaer20020121
20. Wang, L., 2026. MH-DRNN: An intelligent approach in financial fraud detection and prevention. Systems and
Soft Computing, p.200483. https://doi.org/10.1016/j.sasc.2026.200483
Vol.6, No.2s, 2026 762