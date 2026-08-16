---
conversion_metadata:
  converted_at: "2026-07-22T12:53:53Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Chen & Tan.pdf"
  source_pdf_sha256: "2679ce41b30a33fcdc01b858e609033bbb7f888d8e85c5f3c7b6aca85a33c241"
  page_count: 6
  markdown_char_count: 50947
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

LSTM-Based Consumer Behavior Prediction Model Research

Shuhan Chen∗
Guanghua School of Management
Peking University
Beijing, China
jincyisme@163.com

Abstract
This paper proposes a consumer behavior prediction model based
on Long Short-Term Memory (LSTM) networks to accurately pre-
dict consumer purchasing behavior and preference trends in e-
commerce environments. We construct a multi-dimensional fea-
ture dataset from large-scale consumer historical data contain-
ing user characteristics, product attributes, and temporal patterns.
The model employs a bidirectional LSTM architecture integrated
with self-attention mechanisms for enhanced feature extraction.
The architecture comprises six core components: an input em-
bedding layer transforming 128-dimensional sparse features into
256-dimensional dense representations, bidirectional LSTM layers
with 512 hidden units utilizing gating mechanisms for temporal
dependency modeling, a self-attention layer with adaptive tempo-
ral weighting (𝛼t = softmax(et)), adaptive dropout regularization
(scheduled 0.5→0.3), fully connected layers for feature aggregation,
and a softmax output layer for five-class purchase intention predic-
tion. The model contains approximately 2.1 million trainable param-
eters and is optimized through end-to-end backpropagation with
Adam optimizer, weighted cross-entropy loss, L2 regularization
(𝜆 =0.001), gradient clipping (threshold 1.0), and cosine annealing
learning rate scheduling. Data preprocessing employs distributed
computing frameworks achieving 300% efficiency improvement
with 30-day sliding windows and 50% overlap. Experimental eval-
uation on 500,000 users with over 80 million interaction records
demonstrates superior performance compared to traditional ma-
chine learning methods and basic neural networks, achieving 94.2%
accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score. Statisti-
cal significance testing (p<0.001) confirms performance improve-
ments across diverse user segments: high-frequency users (96.1%
accuracy), new users (91.8% accuracy), and high-value customers
(96.7% accuracy). This model provides effective computational sup-
port for personalized recommendations, intelligent inventory man-
agement, and precision marketing on e-commerce platforms.

CCS Concepts
• Computing methodologies; • Artificial intelligence; • Ma-
chine learning; • Machine learning approaches; • Neural net-
works; • Information systems; • Information systems appli-
cations; • Data mining;; • Decision support systems; • Data

∗Corresponding author

This work is licensed under a Creative Commons Attribution 4.0 International License.
DECS 2025, Wuhan, China
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1951-6/2025/10
https://doi.org/10.1145/3785706.3785906

Wenci Tan
Gezhi Future Research Institute
Beijing, China
twwwwc@sina.com

analytics; • Applied computing; • Electronic commerce; •
Operations research.;

Keywords
Consumer behavior prediction, Long Short-Term Memory net-
works, Deep learning, E-commerce, Personalized recommendation

ACM Reference Format:
Shuhan Chen and Wenci Tan. 2025. LSTM-Based Consumer Behavior
Prediction Model Research. In 2025 2nd International Conference on Digital
Economy and Computer Science (DECS 2025), October 17–19, 2025, Wuhan,
China. ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/3785706.
3785906

With the rapid development of e-commerce and the increasing
complexity of consumer digital behavior, accurately predicting con-
sumer behavior has become a key factor in enhancing business com-
petitiveness. The current global e-commerce market has reached
trillions of dollars in scale, with personalized recommendation sys-
tems contributing over 35% of sales revenue through algorithmic fil-
tering and collaborative learning techniques. Traditional consumer
behavior analysis methods primarily rely on statistical models and
simple machine learning algorithms, such as linear regression, deci-
sion trees, and support vector machines [8], which exhibit obvious
limitations when processing large-scale, multi-dimensional con-
sumer data, particularly in capturing temporal features and complex
dependency relationships in high-dimensional feature spaces.

Deep learning technologies have achieved significant progress
across various computational domains through GPU-accelerated
parallel processing. Liu et al. [2] proposed a hybrid YOLO-UNet3D
framework for automated protein particle annotation using convo-
lutional neural networks, demonstrating deep learning advantages
in complex data processing. Xu et al. [3] developed a multi-strategy
enhanced secret bird optimization algorithm implementing adap-
tive parameter tuning, providing new insights for optimization
problems. These studies indicate that deep learning and intelligent
optimization algorithms have tremendous potential in handling
complex pattern recognition through hierarchical feature learning
[4, 5].

Long Short-Term Memory (LSTM) networks, as an advanced re-
current neural network architecture, effectively solve the gradient
vanishing problem through unique gating mechanisms including
forget gates, input gates, and output gates, excelling in process-
ing sequential data and capturing long-term dependencies through
cell state memory mechanisms. Related research shows that deep
learning-based methods have achieved breakthrough progress in
multiple domains through end-to-end training, such as supply chain
logistics scheduling optimization [6], IoT sensor networks with dis-
tributed edge computing [7], and text summarization generation
using transformer architectures [9]. Yang et al. [10] proposed a

---

<!-- PAGE 2 -->

DECS 2025, October 17–19, 2025, Wuhan, China

Shuhan Chen and Wenci Tan

Table 1: Dataset Characteristics.

Feature Category

Number of
Features

Data Type

User Demographics
Product Attributes
Behavioral Sequences
Temporal Features
Interaction History

8
25
45
12
38

Categorical/Numerical
Categorical/Numerical
Sequential
Numerical
Sequential/Numerical

large language model-based web attack detection method incorpo-
rating attention mechanisms and multi-layer perceptrons, proving
deep learning effectiveness in complex pattern recognition tasks.

This research constructs an LSTM-based consumer behavior pre-
diction model, combining self-attention mechanisms and multi-
layer bidirectional architecture with backpropagation training,
drawing on advanced concepts from bio-inspired hybrid path plan-
ning [1] and multi-scale feature aggregation using hierarchical
neural networks [5]. Through distributed computing frameworks
and parallel data processing of consumers’ historical behavioral
data, we achieve precise prediction of future purchasing behavior,
providing scientific basis for intelligent operations, personalized
recommendations, and precision marketing on e-commerce plat-
forms.

1 Methods
1.1 Data Preprocessing and Feature Engineering
This study employs real consumer data from a major e-commerce
platform with over 150 million monthly active users across clothing,
electronics, and home goods categories. The dataset contains behav-
ioral records of 500,000 users over 12 months, totaling more than 80
million interaction data points encompassing browsing, searching,
cart additions, and purchases. Data preprocessing utilizes Apache
Spark distributed computing framework with parallel processing
across 16 worker nodes, implementing missing value imputation
through iterative algorithms and outlier detection using statistical
Z-score and IQR methods with automated threshold adjustment. As
shown in Table 1, the raw data contains multi-dimensional features
with 87% data coverage, ensuring training effectiveness through
comprehensive data validation pipelines.

Feature engineering employs automated extraction algorithms
and parallel processing pipelines. User behavioral sequences
include click streams with timestamp encoding, session-based
browsing duration metrics, and frequency-based purchase patterns
through sliding window aggregation. Product preference features
utilize collaborative filtering and matrix factorization from histori-
cal purchase matrices. Temporal features capture cyclical patterns
through discrete Fourier transforms and seasonal decomposition
algorithms. The final 128-dimensional feature vector comprises
behavioral sequences (45D), product attributes (25D), temporal fea-
tures (12D), user demographics (8D), and interaction history (38D).
Sequence segmentation uses 30-day sliding windows with 50% over-
lap through parallel batch processing, generating training samples
with maintained temporal consistency.

The distributed computing framework implements memory-
optimized data structures and cache management, achieving 300%
processing efficiency improvement through CPU parallelization
and vectorized operations. Figure 1 illustrates the complete pre-
processing workflow with automated data quality monitoring and
real-time processing capabilities.

1.2 Data Preprocessing and Feature Engineering
The LSTM model adopts a multi-layer bidirectional architecture
with six main components: input embedding layer, bidirectional
LSTM layer, attention mechanism layer, dropout layer, fully con-
nected layer, and output layer. The input embedding layer converts
high-dimensional sparse features into 256-dimensional dense vec-
tors. The bidirectional LSTM core consists of forward and backward
LSTM units with 512 hidden units each, using gating mechanisms
to selectively process information and solve long-term dependency
problems. A dropout layer (rate 0.3) prevents overfitting. Figure
2 illustrates the network architecture and data flow. The model
uses end-to-end training with backpropagation, employs softmax
activation for multi-class prediction across five purchase intention
levels (Very Low to Very High), and contains approximately 2.1
million parameters.

1.3 Model Optimization Strategies
To enhance predictive performance and generalization capability,
this study employs multiple advanced optimization strategies. First,
a self-attention mechanism calculates importance weights for each
time step through learned weight matrices and neural network en-
ergy scoring. The attention layer uses multi-head architecture with
8 attention heads and 64-dimensional key-value pairs, improving
key feature identification accuracy by 12.5%.

Second, gradient clipping prevents gradient explosion by con-
straining gradient norms to threshold 1.0 using L2 norm clipping.
The Adam optimizer implements momentum-based adaptive learn-
ing rates with beta1=0.9, beta2=0.999, and epsilon=1e-8. Learn-
ing rate scheduling employs cosine annealing with warm restarts,
where the learning rate starts at 0.001 and follows a cosine decay
curve throughout training to a minimum value of 0.0001. This
approach enables the model to escape local minima through peri-
odic learning rate increases while maintaining overall convergence
stability.

Training configuration optimizes computational efficiency:
batch size 128 balances GPU memory utilization and convergence
speed, maximum epochs 100 with early stopping patience of 10
iterations. The loss function combines weighted cross-entropy
addressing class imbalance through inverse frequency weighting
and L2 regularization with coefficient 0.001 applied to all trainable
parameters.

Data augmentation enhances robustness through temporal jit-
tering with 5% time shift variance, Gaussian noise injection with
standard deviation 0.01, and sliding window sampling with 15-day
stride intervals. This increases training samples by 200% while
preserving temporal dependencies.

The architecture implements Xavier uniform initialization for
weight matrices and batch normalization between LSTM layers for

---

<!-- PAGE 3 -->

LSTM-Based Consumer Behavior Prediction Model Research

DECS 2025, October 17–19, 2025, Wuhan, China

Figure 1: Data Preprocessing Workflow.

Figure 2: LSTM Model Architecture.

training stability. To optimize regularization throughout the train-
ing process, an adaptive dropout scheduling strategy is employed:
the dropout rate begins at 0.5 during the initial 30 epochs to provide
strong regularization against overfitting, then linearly decreases
to 0.3 and remains at this value for the remaining training epochs.
This scheduled approach allows the model to learn robust feature
representations early in training while enabling fine-grained pa-
rameter tuning in later stages. The dropout is applied after the
bidirectional LSTM layers and before the fully connected layers to
prevent co-adaptation of hidden units. Memory optimization uses
gradient accumulation over 4 mini-batches and mixed-precision

training with FP16 computation, reducing memory footprint by
40% while maintaining numerical stability.

To address the critical challenge of training stability and conver-
gence efficiency, we implemented carefully designed scheduling
strategies for both learning rate and dropout regularization. For
learning rate optimization, we adopted a cosine annealing schedule
rather than conventional step-wise or exponential decay meth-
ods. The learning rate follows a smooth cosine curve from the
initial value of 0.001 to the minimum value of 0.0001 over the
entire training process. This approach offers several advantages:
first, the gradual and continuous decay pattern prevents abrupt

---

<!-- PAGE 4 -->

DECS 2025, October 17–19, 2025, Wuhan, China

Shuhan Chen and Wenci Tan

changes in gradient magnitudes that could destabilize training; sec-
ond, the cosine function naturally provides faster decay in early
epochs when coarse adjustments are beneficial, and slower decay
in later epochs to enable fine-tuning; third, unlike exponential
decay which requires manual tuning of decay intervals, cosine an-
nealing provides a mathematically principled schedule that adapts
automatically to the total training duration. For dropout regular-
ization, we employed an adaptive scheduling strategy to balance
overfitting prevention and model capacity utilization throughout
training. The dropout rate begins at 0.5 during the initial 30 epochs,
providing strong regularization when the model parameters are
randomly initialized and most susceptible to overfitting on training
data. After epoch 30, the dropout rate linearly decreases to 0.3
over the next 20 epochs, and remains fixed at 0.3 for all subsequent
training. This design rationale is grounded in the observation that
early-stage training benefits from aggressive regularization to learn
generalizable feature representations, while later-stage training
requires reduced regularization to allow the model to fully exploit
its capacity for capturing subtle patterns in consumer behavior
sequences. The dropout layers are strategically positioned after the
bidirectional LSTM outputs and before the fully connected layers,
ensuring regularization is applied to the most parameter-rich com-
ponents while preserving the temporal information flow within
the recurrent layers. These scheduling strategies were validated
through ablation experiments: models using fixed learning rates or
fixed dropout rates showed 2.3-4.7% lower accuracy and exhibited
either premature convergence or training instability, confirming
the necessity of our adaptive approach.

2 Experiments
2.1 Experimental Setup and Evaluation Metrics
The experimental environment was configured with Ubuntu 20.04
system, Python 3.8, TensorFlow 2.6 deep learning framework, us-
ing NVIDIA RTX 3080 GPU (24GB memory) for model training,
complemented by Intel Xeon E5-2680 v4 processor and 64GB DDR4
memory to ensure sufficient computational resources. The dataset
was randomly divided into training set (350,000 samples), validation
set (100,000 samples), and test set (50,000 samples) in a 7:2:1 ratio,
with stratified sampling to ensure balanced distribution of differ-
ent category samples across sets, avoiding the impact of class bias
on model evaluation. To comprehensively evaluate model perfor-
mance, this study selected Accuracy, Precision, Recall, and F1-score
as primary evaluation metrics, which can reflect the model’s pre-
dictive capabilities from different perspectives. Accuracy measures
the proportion of correctly predicted samples, precision reflects
the proportion of true positives among predicted positives, recall
represents the proportion of true positives that were correctly pre-
dicted, and F1-score is the harmonic mean of precision and recall,
providing comprehensive model performance evaluation. Addi-
tionally, 10-fold cross-validation was employed to ensure result
reliability and stability, with each experiment repeated 5 times and
averaged to reduce the impact of random factors. Furthermore,
AUC-ROC area under the curve and confusion matrices were cal-
culated to further analyze model performance differences across
different categories.

Table 2: Model Performance Comparison.

Model

Accuracy Precision

Recall

F1-Score

Logistic
Regression
Random
Forest
SVM
Basic RNN
Standard
LSTM
Proposed
LSTM

0.782

0.835

0.798
0.856
0.912

0.942

0.756

0.821

0.789
0.842
0.903

0.938

0.798

0.776

0.849

0.835

0.807
0.871
0.921

0.798
0.856
0.912

0.947

0.942

Table 2 presents detailed comparison results of different models
across various metrics, including traditional machine learning meth-
ods (logistic regression, random forest, support vector machine),
basic neural network models (basic RNN, standard LSTM), and the
improved LSTM model proposed in this study. Experimental re-
sults demonstrate that the LSTM model proposed in this research
significantly outperforms comparison methods across all evalua-
tion metrics, achieving an accuracy of 94.235%, representing a 3.0
percentage point improvement over the best baseline model (stan-
dard LSTM) and an average improvement of 10.7 percentage points
over traditional machine learning methods. Statistical significance
testing (p<0.001) indicates that these performance improvements
are statistically significant.

2.2 Model Performance Analysis
The LSTM model demonstrates excellent performance in consumer
behavior prediction tasks. Figure 3 shows training loss curves, re-
vealing rapid convergence and good stability. The proposed LSTM
model achieves convergence around the 25th epoch, while tradi-
tional methods like logistic regression and SVM converge slowly
with higher final losses. Compared to traditional machine learning
methods, the LSTM model’s accuracy improved by 16.2%, benefit-
ing from powerful sequential modeling and long-term dependency
capture. The model excels in handling complex user behavior pat-
terns, particularly purchase cyclicity, seasonal preferences, and
cross-category behaviors.

Table 3 demonstrates excellent generalization capability across
user groups. High-frequency users achieve the highest accuracy
(96.1%) due to stable patterns and abundant data. For challenging
new users, the model achieves 91.8% accuracy with 23.6% improve-
ment over traditional methods by utilizing short-term behavioral
features and similar user patterns. High-value customers with
complex behaviors reach 96.7% accuracy, proving the model’s supe-
riority in handling complex decision-making.

2.3 Feature Importance and Model

Interpretation

This study reveals the model’s internal working principles through
attention weight analysis and feature importance assessment. Fig-
ure 4 displays attention mechanism weight distribution for 15 key

---

<!-- PAGE 5 -->

LSTM-Based Consumer Behavior Prediction Model Research

DECS 2025, October 17–19, 2025, Wuhan, China

Figure 3: Training Loss Curves Comparison.

Table 3: Performance Analysis by User Groups.

User Group

Sample Size

LSTM Accuracy

Traditional ML Accuracy

Improvement

High-frequency Users
Medium-frequency
Users
Low-frequency Users
New Users
High-value Customers

15,420
28,670

18,230
12,890
8,560

0.961
0.935

0.923
0.918
0.967

0.798
0.821

0.775
0.743
0.812

20.430%
13.890%

19.100%
23.560%
19.090%

Table 4: Feature Importance Ranking.

Rank

Feature Name

Importance Score

Feature Type

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

Purchase Frequency Sequence
Product Browsing Duration
Price Sensitivity Index
Category Preference History
Seasonal Purchase Pattern
Cart Addition Frequency
User Age Group
Time Since Last Purchase
Average Order Value
Brand Loyalty Score

0.187
0.156
0.142
0.123
0.108
0.095
0.078
0.067
0.058
0.052

Behavioral
Behavioral
Preference
Behavioral
Temporal
Behavioral
Demographic
Temporal
Economic
Preference

features within a 30-day window. Key patterns include: obvious re-
cency bias with higher weights for recent 7-day behaviors (recency
bias ratio 1.847), behavioral features (purchase frequency, browsing
duration) receiving higher weights than demographic features, and
seasonal preferences showing increased weights at specific time
points like holidays.

Analysis identifies key influencing factors: purchase frequency
(0.187), browsing duration (0.156), price sensitivity (0.142), and

seasonal preferences (0.108). Table 4 presents the complete fea-
ture importance ranking with detailed scores and feature types.
These findings align with consumer behavior theory, validating the
model’s practical significance.

Behavioral features dominate (cumulative score 0.521), proving
more predictive than demographic features. Ablation experiments
confirm removing any Top-5 feature causes 3.2 percentage point
performance decrease. SHAP analysis shows positive values for

---

<!-- PAGE 6 -->

DECS 2025, October 17–19, 2025, Wuhan, China

Shuhan Chen and Wenci Tan

Figure 4: Attention Weight Visualization.

purchase frequency and browsing duration in high-intention users.
Error analysis reveals improvement needs for impulsive purchasing,
external event-driven consumption, and early adopter behaviors.

3 Conclusion
This study successfully constructed an LSTM-based consumer be-
havior prediction model, effectively improving prediction accu-
racy and generalization capability through deep learning technol-
ogy. Experimental results validate the significant advantages of
LSTM networks in processing consumer behavior sequential data,
with the model achieving 94.235% accuracy, representing a 3.0 per-
centage point improvement over the best baseline model and an
average improvement of 10.7 percentage points over traditional
machine learning methods. Through introducing self-attention
mechanisms and optimized multi-layer bidirectional architecture,
the model precisely captures temporal features and long-term de-
pendencies of user behavior, providing strong technical support for
e-commerce platforms’ personalized recommendations, intelligent
inventory management, and precision marketing strategies. Future
research directions include integrating external environmental fac-
tors, exploring multimodal data fusion technologies, developing
lightweight model architectures for real-time prediction, and con-
structing dynamic model update mechanisms to ensure sustained
prediction performance stability.

References
[1] Yuan F, Lin Z, Tian Z, et al. Bio-inspired hybrid path planning for efficient and
smooth robotic navigation: F. Yuan et al[J]. International Journal of Intelligent
Robotics and Applications, 2025: 1-31.

[2] Liu Z, Yuan C, Zhang Z, et al. A hybrid YOLO-UNet3D framework for automated
protein particle annotation in Cryo-ET images[J]. Scientific Reports, 2025, 15(1):
25033.

[3] Xu L, Yuan C, Jiang Z. Multi-strategy enhanced secret bird optimization algorithm
for solving obstacle avoidance path planning for mobile robots[J]. Mathematics,
2025, 13(5): 717.

[4] Xiao N, Yuan C H, Pei Y T, et al. A study of artificial intelligence in writing
assessment for secondary school students: a comparative analysis based on the
GPT-4 and human raters[J]. Educational Studies, 2025: 1-23.

[5] Cui, J., & Yuan, C. (2025). Multi-scale feature aggregation with hierarchical
semantics and uncertainty assessment: enabling high-accuracy visual retrieval.
The Journal of Supercomputing, 81(10), 1-26.

[6] Wang Y, Zhang H, Yuan C, et al. An efficient scheduling method in supply chain

logistics based on network flow[J]. Processes, 2025, 13(4): 969.

[7] Liu, Z., Chen, P., Wang, Z., Ala, A., & Pethuraj, M. S. (2024). OpHSS: Optimized
pH Sensing Synergy Alignment in IoT Backbone Networks for Precision Farming.
IEEE Sensors Journal, 24(24), 20910-20920.

[8] Wang, Zongshan, et al. ”Energy Efficient Cluster Based Routing Protocol for
WSN Using Firefly Algorithm and Ant Colony Optimization.” Wireless Personal
Communications (2022): 1-34.

[9] Yang, J., Qin, H., Sun, Y., Wang, H., Khan, A. A., Por, L. Y., & Alizadehsani, R.
(2025). A generative adversarial network-based extractive text summarization
using transductive and reinforcement learning. IEEE Access, 9.

[10] Yang, J., Wu, Y., Yuan, Y., Xue, H., Bourouis, S., & Mahmoud, … (2025). LLM-AE-
MP: Web attack detection using a large language model with autoencoder and
multilayer perceptron. Expert Systems with Applications, 12.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

LSTM-Based Consumer Behavior Prediction Model Research
∗
ShuhanChen WenciTan
GuanghuaSchoolofManagement GezhiFutureResearchInstitute
PekingUniversity Beijing,China
Beijing,China twwwwc@sina.com
jincyisme@163.com
Abstract analytics; • Applied computing; • Electronic commerce; •
Thispaperproposesaconsumerbehaviorpredictionmodelbased Operationsresearch.;
onLongShort-TermMemory(LSTM)networkstoaccuratelypre-
Keywords
dict consumer purchasing behavior and preference trends in e-
commerceenvironments. Weconstructamulti-dimensionalfea- Consumer behavior prediction, Long Short-Term Memory net-
ture dataset from large-scale consumer historical data contain- works,Deeplearning,E-commerce,Personalizedrecommendation
ingusercharacteristics,productattributes,andtemporalpatterns.
ACMReferenceFormat:
ThemodelemploysabidirectionalLSTMarchitectureintegrated ShuhanChenandWenciTan. 2025. LSTM-BasedConsumerBehavior
withself-attentionmechanismsforenhancedfeatureextraction. PredictionModelResearch.In20252ndInternationalConferenceonDigital
The architecture comprises six core components: an input em- EconomyandComputerScience(DECS2025),October17–19,2025,Wuhan,
beddinglayertransforming128-dimensionalsparsefeaturesinto China.ACM,NewYork,NY,USA,6pages.https://doi.org/10.1145/3785706.
256-dimensionaldenserepresentations,bidirectionalLSTMlayers 3785906
with512hiddenunitsutilizinggatingmechanismsfortemporal
With the rapid development of e-commerce and the increasing
dependencymodeling,aself-attentionlayerwithadaptivetempo-
complexityofconsumerdigitalbehavior,accuratelypredictingcon-
ralweighting(𝛼t=softmax(et)),adaptivedropoutregularization
sumerbehaviorhasbecomeakeyfactorinenhancingbusinesscom-
(scheduled0.5→0.3),fullyconnectedlayersforfeatureaggregation,
petitiveness.Thecurrentglobale-commercemarkethasreached
andasoftmaxoutputlayerforfive-classpurchaseintentionpredic-
trillionsofdollarsinscale,withpersonalizedrecommendationsys-
tion.Themodelcontainsapproximately2.1milliontrainableparam-
temscontributingover35%ofsalesrevenuethroughalgorithmicfil-
etersandisoptimizedthroughend-to-endbackpropagationwith
teringandcollaborativelearningtechniques.Traditionalconsumer
Adamoptimizer, weightedcross-entropyloss, L2regularization
behavioranalysismethodsprimarilyrelyonstatisticalmodelsand
(𝜆=0.001),gradientclipping(threshold1.0),andcosineannealing
simplemachinelearningalgorithms,suchaslinearregression,deci-
learningratescheduling. Datapreprocessingemploysdistributed
siontrees,andsupportvectormachines[8],whichexhibitobvious
computingframeworksachieving300%efficiencyimprovement
limitationswhenprocessinglarge-scale,multi-dimensionalcon-
with30-dayslidingwindowsand50%overlap.Experimentaleval-
sumerdata,particularlyincapturingtemporalfeaturesandcomplex
uationon500,000userswithover80millioninteractionrecords
dependencyrelationshipsinhigh-dimensionalfeaturespaces.
demonstratessuperiorperformancecomparedtotraditionalma-
Deeplearningtechnologieshaveachievedsignificantprogress
chinelearningmethodsandbasicneuralnetworks,achieving94.2%
acrossvariouscomputationaldomainsthroughGPU-accelerated
accuracy,93.8%precision,94.7%recall,and94.2%F1-score.Statisti-
parallelprocessing. Liuetal. [2]proposedahybridYOLO-UNet3D
calsignificancetesting(p<0.001)confirmsperformanceimprove-
frameworkforautomatedproteinparticleannotationusingconvo-
mentsacrossdiverseusersegments:high-frequencyusers(96.1%
lutionalneuralnetworks,demonstratingdeeplearningadvantages
accuracy),newusers(91.8%accuracy),andhigh-valuecustomers
incomplexdataprocessing.Xuetal.[3]developedamulti-strategy
(96.7%accuracy).Thismodelprovideseffectivecomputationalsup-
enhancedsecretbirdoptimizationalgorithmimplementingadap-
portforpersonalizedrecommendations,intelligentinventoryman-
tive parameter tuning, providing new insights for optimization
agement,andprecisionmarketingone-commerceplatforms.
problems.Thesestudiesindicatethatdeeplearningandintelligent
optimizationalgorithmshavetremendouspotentialinhandling
CCSConcepts
complexpatternrecognitionthroughhierarchicalfeaturelearning
•Computingmethodologies;•Artificialintelligence;•Ma- [4,5].
chinelearning;•Machinelearningapproaches;•Neuralnet- LongShort-TermMemory(LSTM)networks,asanadvancedre-
works;•Informationsystems;•Informationsystemsappli- currentneuralnetworkarchitecture,effectivelysolvethegradient
cations;•Datamining;;•Decisionsupportsystems;•Data vanishingproblemthroughuniquegatingmechanismsincluding
forgetgates,inputgates,andoutputgates,excellinginprocess-
∗Correspondingauthor
ingsequentialdataandcapturinglong-termdependenciesthrough
cellstatememorymechanisms.Relatedresearchshowsthatdeep
learning-basedmethodshaveachievedbreakthroughprogressin
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. multipledomainsthroughend-to-endtraining,suchassupplychain
DECS2025,Wuhan,China logisticsschedulingoptimization[6],IoTsensornetworkswithdis-
©2025Copyrightheldbytheowner/author(s).
tributededgecomputing[7],andtextsummarizationgeneration
ACMISBN979-8-4007-1951-6/2025/10
https://doi.org/10.1145/3785706.3785906 usingtransformerarchitectures[9]. Yangetal. [10]proposeda
1265

DECS2025,October17–19,2025,Wuhan,China ShuhanChenandWenciTan
Table1:DatasetCharacteristics. The distributed computing framework implements memory-
optimizeddatastructuresandcachemanagement,achieving300%
FeatureCategory Numberof DataType processingefficiencyimprovementthroughCPUparallelization
Features andvectorizedoperations. Figure1illustratesthecompletepre-
processingworkflowwithautomateddataqualitymonitoringand
UserDemographics 8 Categorical/Numerical
real-timeprocessingcapabilities.
ProductAttributes 25 Categorical/Numerical
BehavioralSequences 45 Sequential
TemporalFeatures 12 Numerical 1.2 DataPreprocessingandFeatureEngineering
InteractionHistory 38 Sequential/Numerical
TheLSTMmodeladoptsamulti-layerbidirectionalarchitecture
withsixmaincomponents: inputembeddinglayer,bidirectional
LSTMlayer,attentionmechanismlayer,dropoutlayer,fullycon-
largelanguagemodel-basedwebattackdetectionmethodincorpo- nectedlayer,andoutputlayer.Theinputembeddinglayerconverts
ratingattentionmechanismsandmulti-layerperceptrons,proving high-dimensionalsparsefeaturesinto256-dimensionaldensevec-
deeplearningeffectivenessincomplexpatternrecognitiontasks. tors.ThebidirectionalLSTMcoreconsistsofforwardandbackward
ThisresearchconstructsanLSTM-basedconsumerbehaviorpre- LSTMunitswith512hiddenunitseach,usinggatingmechanisms
diction model, combining self-attention mechanisms and multi- toselectivelyprocessinformationandsolvelong-termdependency
layer bidirectional architecture with backpropagation training, problems. Adropoutlayer(rate0.3)preventsoverfitting. Figure
drawingonadvancedconceptsfrombio-inspiredhybridpathplan- 2illustratesthenetworkarchitectureanddataflow. Themodel
ning [1] and multi-scale feature aggregation using hierarchical usesend-to-endtrainingwithbackpropagation,employssoftmax
neuralnetworks[5]. Throughdistributedcomputingframeworks activationformulti-classpredictionacrossfivepurchaseintention
andparalleldataprocessingofconsumers’historicalbehavioral levels(VeryLowtoVeryHigh),andcontainsapproximately2.1
data,weachieveprecisepredictionoffuturepurchasingbehavior, millionparameters.
providingscientificbasisforintelligentoperations,personalized
recommendations,andprecisionmarketingone-commerceplat-
1.3 ModelOptimizationStrategies
forms.
Toenhancepredictiveperformanceandgeneralizationcapability,
1 Methods thisstudyemploysmultipleadvancedoptimizationstrategies.First,
aself-attentionmechanismcalculatesimportanceweightsforeach
1.1 DataPreprocessingandFeatureEngineering
timestepthroughlearnedweightmatricesandneuralnetworken-
Thisstudyemploysrealconsumerdatafromamajore-commerce ergyscoring.Theattentionlayerusesmulti-headarchitecturewith
platformwithover150millionmonthlyactiveusersacrossclothing, 8attentionheadsand64-dimensionalkey-valuepairs,improving
electronics,andhomegoodscategories.Thedatasetcontainsbehav- keyfeatureidentificationaccuracyby12.5%.
ioralrecordsof500,000usersover12months,totalingmorethan80 Second,gradientclippingpreventsgradientexplosionbycon-
millioninteractiondatapointsencompassingbrowsing,searching, straininggradientnormstothreshold1.0usingL2normclipping.
cartadditions,andpurchases.DatapreprocessingutilizesApache TheAdamoptimizerimplementsmomentum-basedadaptivelearn-
Sparkdistributedcomputingframeworkwithparallelprocessing ingrateswithbeta1=0.9,beta2=0.999,andepsilon=1e-8. Learn-
across16workernodes,implementingmissingvalueimputation ingrateschedulingemployscosineannealingwithwarmrestarts,
throughiterativealgorithmsandoutlierdetectionusingstatistical wherethelearningratestartsat0.001andfollowsacosinedecay
Z-scoreandIQRmethodswithautomatedthresholdadjustment.As curve throughout training to a minimum value of 0.0001. This
showninTable1,therawdatacontainsmulti-dimensionalfeatures approachenablesthemodeltoescapelocalminimathroughperi-
with87%datacoverage,ensuringtrainingeffectivenessthrough odiclearningrateincreaseswhilemaintainingoverallconvergence
comprehensivedatavalidationpipelines. stability.
Featureengineeringemploysautomatedextractionalgorithms Training configuration optimizes computational efficiency:
and parallel processing pipelines. User behavioral sequences batchsize128balancesGPUmemoryutilizationandconvergence
include click streams with timestamp encoding, session-based speed,maximumepochs100withearlystoppingpatienceof10
browsingdurationmetrics,andfrequency-basedpurchasepatterns iterations. The loss function combines weighted cross-entropy
throughslidingwindowaggregation.Productpreferencefeatures addressingclassimbalancethroughinversefrequencyweighting
utilizecollaborativefilteringandmatrixfactorizationfromhistori- andL2regularizationwithcoefficient0.001appliedtoalltrainable
calpurchasematrices.Temporalfeaturescapturecyclicalpatterns parameters.
throughdiscreteFouriertransformsandseasonaldecomposition Dataaugmentationenhancesrobustnessthroughtemporaljit-
algorithms. Thefinal128-dimensionalfeaturevectorcomprises teringwith5%timeshiftvariance,Gaussiannoiseinjectionwith
behavioralsequences(45D),productattributes(25D),temporalfea- standarddeviation0.01,andslidingwindowsamplingwith15-day
tures(12D),userdemographics(8D),andinteractionhistory(38D). stride intervals. This increases training samples by 200% while
Sequencesegmentationuses30-dayslidingwindowswith50%over- preservingtemporaldependencies.
lapthroughparallelbatchprocessing,generatingtrainingsamples ThearchitectureimplementsXavieruniforminitializationfor
withmaintainedtemporalconsistency. weightmatricesandbatchnormalizationbetweenLSTMlayersfor
1266

LSTM-BasedConsumerBehaviorPredictionModelResearch DECS2025,October17–19,2025,Wuhan,China
Figure1:DataPreprocessingWorkflow.
Figure2:LSTMModelArchitecture.
trainingstability.Tooptimizeregularizationthroughoutthetrain- trainingwithFP16computation,reducingmemoryfootprintby
ingprocess,anadaptivedropoutschedulingstrategyisemployed: 40%whilemaintainingnumericalstability.
thedropoutratebeginsat0.5duringtheinitial30epochstoprovide Toaddressthecriticalchallengeoftrainingstabilityandconver-
strongregularizationagainstoverfitting,thenlinearlydecreases genceefficiency,weimplementedcarefullydesignedscheduling
to0.3andremainsatthisvaluefortheremainingtrainingepochs. strategiesforbothlearningrateanddropoutregularization. For
Thisscheduledapproachallowsthemodeltolearnrobustfeature learningrateoptimization,weadoptedacosineannealingschedule
representationsearlyintrainingwhileenablingfine-grainedpa- rather than conventional step-wise or exponential decay meth-
rametertuninginlaterstages. Thedropoutisappliedafterthe ods. The learning rate followsa smooth cosine curve fromthe
bidirectionalLSTMlayersandbeforethefullyconnectedlayersto initial value of 0.001 to the minimum value of 0.0001 over the
preventco-adaptationofhiddenunits. Memoryoptimizationuses entiretrainingprocess. Thisapproachoffersseveraladvantages:
gradientaccumulationover4mini-batchesandmixed-precision first,thegradualandcontinuousdecaypatternpreventsabrupt
1267

| DECS2025,October17–19,2025,Wuhan,China |     |     |     |     |     | ShuhanChenandWenciTan |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --------------------- | --- |
changesingradientmagnitudesthatcoulddestabilizetraining;sec- Table2:ModelPerformanceComparison.
ond,thecosinefunctionnaturallyprovidesfasterdecayinearly
epochswhencoarseadjustmentsarebeneficial,andslowerdecay Model Accuracy Precision Recall F1-Score
| in later epochs | to enable fine-tuning; | third, unlike | exponential |          |             |             |     |
| --------------- | ---------------------- | ------------- | ----------- | -------- | ----------- | ----------- | --- |
|                 |                        |               |             | Logistic | 0.782 0.756 | 0.798 0.776 |     |
decaywhichrequiresmanualtuningofdecayintervals,cosinean-
Regression
nealingprovidesamathematicallyprincipledschedulethatadapts
|     |     |     |     | Random | 0.835 0.821 | 0.849 0.835 |     |
| --- | --- | --- | --- | ------ | ----------- | ----------- | --- |
automaticallytothetotaltrainingduration.Fordropoutregular-
Forest
ization,weemployedanadaptiveschedulingstrategytobalance
|     |     |     |     | SVM | 0.798 0.789 | 0.807 0.798 |     |
| --- | --- | --- | --- | --- | ----------- | ----------- | --- |
overfittingpreventionandmodelcapacityutilizationthroughout
|     |     |     |     | BasicRNN | 0.856 0.842 | 0.871 0.856 |     |
| --- | --- | --- | --- | -------- | ----------- | ----------- | --- |
training.Thedropoutratebeginsat0.5duringtheinitial30epochs,
|     |     |     |     | Standard | 0.912 0.903 | 0.921 0.912 |     |
| --- | --- | --- | --- | -------- | ----------- | ----------- | --- |
providingstrongregularizationwhenthemodelparametersare
| randomlyinitializedandmostsusceptibletooverfittingontraining |                                      |     |     | LSTM     |             |             |     |
| ------------------------------------------------------------ | ------------------------------------ | --- | --- | -------- | ----------- | ----------- | --- |
|                                                              |                                      |     |     | Proposed | 0.942 0.938 | 0.947 0.942 |     |
| data. Afterepoch30,                                          | thedropoutratelinearlydecreasesto0.3 |     |     |          |             |             |     |
LSTM
overthenext20epochs,andremainsfixedat0.3forallsubsequent
training.Thisdesignrationaleisgroundedintheobservationthat
early-stagetrainingbenefitsfromaggressiveregularizationtolearn
| generalizablefeaturerepresentations, |     | whilelater-stagetraining |     |     |     |     |     |
| ------------------------------------ | --- | ------------------------ | --- | --- | --- | --- | --- |
Table2presentsdetailedcomparisonresultsofdifferentmodels
requiresreducedregularizationtoallowthemodeltofullyexploit acrossvariousmetrics,includingtraditionalmachinelearningmeth-
itscapacityforcapturingsubtlepatternsinconsumerbehavior ods(logisticregression,randomforest,supportvectormachine),
sequences.Thedropoutlayersarestrategicallypositionedafterthe basicneuralnetworkmodels(basicRNN,standardLSTM),andthe
bidirectionalLSTMoutputsandbeforethefullyconnectedlayers, improvedLSTMmodelproposedinthisstudy. Experimentalre-
ensuringregularizationisappliedtothemostparameter-richcom-
sultsdemonstratethattheLSTMmodelproposedinthisresearch
ponentswhilepreservingthetemporalinformationflowwithin significantlyoutperformscomparisonmethodsacrossallevalua-
therecurrentlayers. Theseschedulingstrategieswerevalidated tionmetrics,achievinganaccuracyof94.235%,representinga3.0
throughablationexperiments:modelsusingfixedlearningratesor percentagepointimprovementoverthebestbaselinemodel(stan-
fixeddropoutratesshowed2.3-4.7%loweraccuracyandexhibited dardLSTM)andanaverageimprovementof10.7percentagepoints
eitherprematureconvergenceortraininginstability,confirming
overtraditionalmachinelearningmethods.Statisticalsignificance
thenecessityofouradaptiveapproach. testing(p<0.001)indicatesthattheseperformanceimprovements
arestatisticallysignificant.
2.2 ModelPerformanceAnalysis
2 Experiments
TheLSTMmodeldemonstratesexcellentperformanceinconsumer
2.1 ExperimentalSetupandEvaluationMetrics
behaviorpredictiontasks.Figure3showstraininglosscurves,re-
TheexperimentalenvironmentwasconfiguredwithUbuntu20.04
vealingrapidconvergenceandgoodstability.TheproposedLSTM
system,Python3.8,TensorFlow2.6deeplearningframework,us-
modelachievesconvergencearoundthe25thepoch,whiletradi-
ingNVIDIARTX3080GPU(24GBmemory)formodeltraining,
tionalmethodslikelogisticregressionandSVMconvergeslowly
complementedbyIntelXeonE5-2680v4processorand64GBDDR4
|     |     |     |     | withhigherfinallosses. | Comparedtotraditionalmachinelearning |     |     |
| --- | --- | --- | --- | ---------------------- | ------------------------------------ | --- | --- |
memorytoensuresufficientcomputationalresources.Thedataset
methods,theLSTMmodel’saccuracyimprovedby16.2%,benefit-
wasrandomlydividedintotrainingset(350,000samples),validation
ingfrompowerfulsequentialmodelingandlong-termdependency
set(100,000samples),andtestset(50,000samples)ina7:2:1ratio,
capture. Themodelexcelsinhandlingcomplexuserbehaviorpat-
withstratifiedsamplingtoensurebalanceddistributionofdiffer-
|     |     |     |     | terns, particularly | purchase cyclicity, | seasonal preferences, | and |
| --- | --- | --- | --- | ------------------- | ------------------- | --------------------- | --- |
entcategorysamplesacrosssets,avoidingtheimpactofclassbias
cross-categorybehaviors.
| onmodelevaluation. | Tocomprehensivelyevaluatemodelperfor- |     |     |     |     |     |     |
| ------------------ | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Table3demonstratesexcellentgeneralizationcapabilityacross
mance,thisstudyselectedAccuracy,Precision,Recall,andF1-score
|     |     |     |     | usergroups. | High-frequencyusersachievethehighestaccuracy |     |     |
| --- | --- | --- | --- | ----------- | -------------------------------------------- | --- | --- |
asprimaryevaluationmetrics,whichcanreflectthemodel’spre-
(96.1%)duetostablepatternsandabundantdata.Forchallenging
| dictivecapabilitiesfromdifferentperspectives. |     | Accuracymeasures |     |     |     |     |     |
| --------------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |
newusers,themodelachieves91.8%accuracywith23.6%improve-
theproportionofcorrectlypredictedsamples,precisionreflects
mentovertraditionalmethodsbyutilizingshort-termbehavioral
theproportionoftruepositivesamongpredictedpositives,recall
|     |     |     |     | features | and similar user patterns. | High-value customers | with |
| --- | --- | --- | --- | -------- | -------------------------- | -------------------- | ---- |
representstheproportionoftruepositivesthatwerecorrectlypre-
complexbehaviorsreach96.7%accuracy,provingthemodel’ssupe-
dicted,andF1-scoreistheharmonicmeanofprecisionandrecall,
riorityinhandlingcomplexdecision-making.
| providingcomprehensivemodelperformanceevaluation. |     |     | Addi- |     |     |     |     |
| ------------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- |
tionally,10-foldcross-validationwasemployedtoensureresult
2.3 FeatureImportanceandModel
reliabilityandstability,witheachexperimentrepeated5timesand
Interpretation
| averagedtoreducetheimpactofrandomfactors. |     |     | Furthermore, |     |     |     |     |
| ----------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- |
AUC-ROCareaunderthecurveandconfusionmatriceswerecal- Thisstudyrevealsthemodel’sinternalworkingprinciplesthrough
culatedtofurtheranalyzemodelperformancedifferencesacross attentionweightanalysisandfeatureimportanceassessment. Fig-
differentcategories. ure4displaysattentionmechanismweightdistributionfor15key
1268

LSTM-BasedConsumerBehaviorPredictionModelResearch DECS2025,October17–19,2025,Wuhan,China
Figure3:TrainingLossCurvesComparison.
Table3:PerformanceAnalysisbyUserGroups.
UserGroup SampleSize LSTMAccuracy TraditionalMLAccuracy Improvement
| High-frequencyUsers | 15,420 | 0.961 | 0.798 | 20.430% |
| ------------------- | ------ | ----- | ----- | ------- |
| Medium-frequency    | 28,670 | 0.935 | 0.821 | 13.890% |
Users
| Low-frequencyUsers  | 18,230 | 0.923 | 0.775 | 19.100% |
| ------------------- | ------ | ----- | ----- | ------- |
| NewUsers            | 12,890 | 0.918 | 0.743 | 23.560% |
| High-valueCustomers | 8,560  | 0.967 | 0.812 | 19.090% |
Table4:FeatureImportanceRanking.
| Rank |                           | FeatureName | ImportanceScore | FeatureType |
| ---- | ------------------------- | ----------- | --------------- | ----------- |
| 1    | PurchaseFrequencySequence |             | 0.187           | Behavioral  |
| 2    | ProductBrowsingDuration   |             | 0.156           | Behavioral  |
| 3    | PriceSensitivityIndex     |             | 0.142           | Preference  |
| 4    | CategoryPreferenceHistory |             | 0.123           | Behavioral  |
| 5    | SeasonalPurchasePattern   |             | 0.108           | Temporal    |
| 6    | CartAdditionFrequency     |             | 0.095           | Behavioral  |
| 7    | UserAgeGroup              |             | 0.078           | Demographic |
| 8    | TimeSinceLastPurchase     |             | 0.067           | Temporal    |
| 9    | AverageOrderValue         |             | 0.058           | Economic    |
| 10   | BrandLoyaltyScore         |             | 0.052           | Preference  |
featureswithina30-daywindow.Keypatternsinclude:obviousre- seasonalpreferences(0.108). Table4presentsthecompletefea-
cencybiaswithhigherweightsforrecent7-daybehaviors(recency tureimportancerankingwithdetailedscoresandfeaturetypes.
biasratio1.847),behavioralfeatures(purchasefrequency,browsing Thesefindingsalignwithconsumerbehaviortheory,validatingthe
duration)receivinghigherweightsthandemographicfeatures,and model’spracticalsignificance.
seasonalpreferencesshowingincreasedweightsatspecifictime Behavioralfeaturesdominate(cumulativescore0.521),proving
pointslikeholidays. morepredictivethandemographicfeatures.Ablationexperiments
Analysisidentifieskeyinfluencingfactors:purchasefrequency confirmremovinganyTop-5featurecauses3.2percentagepoint
(0.187), browsing duration (0.156), price sensitivity (0.142), and performancedecrease. SHAPanalysisshowspositivevaluesfor
1269

DECS2025,October17–19,2025,Wuhan,China ShuhanChenandWenciTan
Figure4:AttentionWeightVisualization.
purchasefrequencyandbrowsingdurationinhigh-intentionusers. References
Erroranalysisrevealsimprovementneedsforimpulsivepurchasing, [1] YuanF,LinZ,TianZ,etal.Bio-inspiredhybridpathplanningforefficientand
externalevent-drivenconsumption,andearlyadopterbehaviors. smoothroboticnavigation:F.Yuanetal[J].InternationalJournalofIntelligent
RoboticsandApplications,2025:1-31.
[2] LiuZ,YuanC,ZhangZ,etal.AhybridYOLO-UNet3Dframeworkforautomated
3 Conclusion proteinparticleannotationinCryo-ETimages[J].ScientificReports,2025,15(1):
25033.
ThisstudysuccessfullyconstructedanLSTM-basedconsumerbe- [3] XuL,YuanC,JiangZ.Multi-strategyenhancedsecretbirdoptimizationalgorithm
havior prediction model, effectively improving prediction accu- forsolvingobstacleavoidancepathplanningformobilerobots[J].Mathematics,
2025,13(5):717.
racyandgeneralizationcapabilitythroughdeeplearningtechnol-
[4] XiaoN,YuanCH,PeiYT,etal.Astudyofartificialintelligenceinwriting
ogy. Experimentalresultsvalidatethesignificantadvantagesof assessmentforsecondaryschoolstudents:acomparativeanalysisbasedonthe
LSTMnetworksinprocessingconsumerbehaviorsequentialdata, GPT-4andhumanraters[J].EducationalStudies,2025:1-23.
[5] Cui,J.,&Yuan,C.(2025).Multi-scalefeatureaggregationwithhierarchical
withthemodelachieving94.235%accuracy,representinga3.0per- semanticsanduncertaintyassessment:enablinghigh-accuracyvisualretrieval.
centagepointimprovementoverthebestbaselinemodelandan TheJournalofSupercomputing,81(10),1-26.
[6] WangY,ZhangH,YuanC,etal.Anefficientschedulingmethodinsupplychain
averageimprovementof10.7percentagepointsovertraditional
logisticsbasedonnetworkflow[J].Processes,2025,13(4):969.
machine learning methods. Through introducing self-attention [7] Liu,Z.,Chen,P.,Wang,Z.,Ala,A.,&Pethuraj,M.S.(2024).OpHSS:Optimized
mechanismsandoptimizedmulti-layerbidirectionalarchitecture, pHSensingSynergyAlignmentinIoTBackboneNetworksforPrecisionFarming.
IEEESensorsJournal,24(24),20910-20920.
themodelpreciselycapturestemporalfeaturesandlong-termde-
[8] Wang,Zongshan,etal.”EnergyEfficientClusterBasedRoutingProtocolfor
pendenciesofuserbehavior,providingstrongtechnicalsupportfor WSNUsingFireflyAlgorithmandAntColonyOptimization.”WirelessPersonal
e-commerceplatforms’personalizedrecommendations,intelligent Communications(2022):1-34.
[9] Yang,J.,Qin,H.,Sun,Y.,Wang,H.,Khan,A.A.,Por,L.Y.,&Alizadehsani,R.
inventorymanagement,andprecisionmarketingstrategies.Future (2025).Agenerativeadversarialnetwork-basedextractivetextsummarization
researchdirectionsincludeintegratingexternalenvironmentalfac- usingtransductiveandreinforcementlearning.IEEEAccess,9.
[10] Yang,J.,Wu,Y.,Yuan,Y.,Xue,H.,Bourouis,S.,&Mahmoud,…(2025).LLM-AE-
tors,exploringmultimodaldatafusiontechnologies,developing
MP:Webattackdetectionusingalargelanguagemodelwithautoencoderand
lightweightmodelarchitecturesforreal-timeprediction,andcon- multilayerperceptron.ExpertSystemswithApplications,12.
structingdynamicmodelupdatemechanismstoensuresustained
predictionperformancestability.
1270