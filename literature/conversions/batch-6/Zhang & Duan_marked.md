---
conversion_metadata:
  converted_at: "2026-07-21T10:04:28Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhang & Duan.pdf"
  source_pdf_sha256: "dd5873de51efc9bc7d996a1b465e83f978bf85b9ef38173b64b92a8bdaa8905f"
  page_count: 25
  markdown_char_count: 249085
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

OPEN ACCESS

EDITED BY
Biswajit Sarkar,  
Yonsei University, Republic of Korea

REVIEWED BY
Dragos Bozdog,  
Stevens Institute of Technology, United States
Nooka Madhusudhana Reddy,  
Rajeev Gandhi Memorial College of 
Engineering and Technology, India

*CORRESPONDENCE
Yingying Zhang

zyy_cdcas@163.com

RECEIVED 14 May 2025
ACCEPTED 18 August 2025
PUBLISHED 02 September 2025

CITATION
Zhang Y and Duan B (2025) Accounting data 
anomaly detection and prediction based on 
self-supervised learning.
Front. Appl. Math. Stat. 11:1628652.
doi: 10.3389/fams.2025.1628652

COPYRIGHT
© 2025 Zhang and Duan. This is an 
open-access article distributed under the 
terms of the Creative Commons Attribution 
License (CC BY). The use, distribution or 
reproduction in other forums is permitted, 
provided the original author(s) and the 
copyright owner(s) are credited and that the 
original publication in this journal is cited, in 
accordance with accepted academic 
practice. No use, distribution or reproduction 
is permitted which does not comply with 
these terms.

TYPE  Original Research
PUBLISHED  02 September 2025
DOI  10.3389/fams.2025.1628652

Accounting data anomaly 
detection and prediction based 
on self-supervised learning

Yingying Zhang 1* and Bingbing Duan 2

1 Chengdu College of Arts and Sciences, School of Accounting, Chengdu, China, 2 Chengdu Huawei 
Technologies Co., Ltd., Chengdu, China

This study proposes a Hierarchical Fusion Self-Supervised Learning (HFSL) framework 
to address the challenge of scarce labeled data in accounting anomaly detection, 
integrating domain knowledge with advanced deep learning techniques. Based 
on financial data from Chinese listed companies in the CSMAR database spanning 
2000–2020, this framework integrates temporal contrastive learning, a dual-channel 
LSTM  autoencoder  structure,  and  financial  domain  knowledge  to  construct  a 
three-tier cascaded detection system. Empirical research demonstrates that the 
HFSL framework achieves a precision of 0.836, recall of 0.805, and F1 score of 
0.820 in accounting anomaly detection, significantly outperforming traditional 
methods. In terms of practical metrics, the framework attains an early detection 
rate of 0.726 while maintaining a false alarm rate of just 0.068, providing technical 
support for early risk warning. Financial feature contribution analysis reveals that 
core indicators such as Return on Assets (ROA), Return on Equity (ROE), and their 
interaction effects play crucial roles in anomaly identification. Through analysis 
of 2,150 samples in the test set, the study identifies five typical financial fraud 
patterns (revenue inflation 38.6%, expense concealment 21.7%, asset overvaluation 
17.4%, liability understatement 15.2%, and composite manipulation 7.1%) and their 
temporal evolution characteristics. The research also finds that financial anomalies 
typically exhibit three evolutionary patterns: progressive deterioration (64%), sudden 
anomalies (22%), or cyclical fluctuations (15%), providing empirical evidence for 
regulatory practice. This study applies self-supervised learning to accounting anomaly 
detection, not only solving the detection challenges in unlabeled data scenarios 
but also providing effective tools for financial supervision and risk management.

KEYWORDS

accounting data, anomaly detection, financial fraud, hierarchical fusion framework, 
self-supervised learning

1 Introduction

Accounting data, as the quantitative representation of enterprise economic activities, plays 
a  fundamental  supporting  role  in  investment  decisions,  resource  allocation,  and  market 
stability. However, frequent financial fraud incidents in global financial markets in recent years 
have severely eroded market confidence and economic stability. Data from the U.S. Securities 
and  Exchange  Commission  (SEC)  shows  that  financial  fraud  cases  have  increased  by 
approximately 30% in recent years (2020–2023), with amounts exceeding $270 billion (1). This 
systemic risk not only affects individual enterprises but also threatens the entire capital market. 
Iconic financial fraud cases such as Enron, WorldCom, and Lehman Brothers caused market 
capitalization losses exceeding $300 billion, hundreds of thousands of employees losing their 
jobs, and severe pension fund losses, triggering comprehensive doubts about accounting 
information reliability.

Frontiers in Applied Mathematics and Statistics

01

frontiersin.org

---

<!-- PAGE 2 -->

Zhang and Duan

10.3389/fams.2025.1628652

In the Chinese market, recent financial fraud cases of listed 
companies  such  as  Kangmei  Pharmaceutical  and  Kangde  Xin 
similarly  highlight  the  serious  harm  of  financial  information 
distortion to investors and market order. Kangmei Pharmaceutical 
was fined 6 billion yuan for falsely increasing monetary funds by 
nearly 30 billion yuan, becoming the largest fine in the history of 
China’s capital market (2). These cases reveal the limitations of 
traditional financial regulatory mechanisms when facing complex 
and  concealed  accounting  data  manipulation.  Despite  global 
regulatory bodies continuously strengthening financial reporting 
regulatory frameworks, such as the Sarbanes-Oxley Act (SOX) and 
International Financial Reporting Standards (IFRS), accounting 
data anomaly detection still faces severe challenges: complex and 
variable anomaly patterns, severe scarcity of available labeled data, 
and insufficient detection tool effectiveness (3).

Traditional  accounting  anomaly  detection  methods  mainly 
rely on two technical approaches: rule-based statistical analysis, 
such  as  modified  Z-score  and  Beneish  M-score  models,  and 
supervised learning methods, such as support vector machines 
and random forests. However, these methods generally have three 
key limitations: (1) dependence on large amounts of high-quality 
labeled data, while accounting fraud cases are rare events with 
costly  labeled  data  acquisition;  (2)  static  anomaly  pattern 
assumptions, making it difficult to adapt to the dynamic evolution 
of  financial  fraud  techniques;  and  (3)  insufficient  modeling 
capability  for  complex  interactions  between  multidimensional 
financial indicators, resulting in low detection rates for carefully 
designed financial manipulation behaviors (4, 5).

With  the  deepening  of  digital  transformation,  enterprise 
financial data exhibits characteristics of large volume, complex 
dimensions, temporal dependence, and industry heterogeneity, 
urgently  requiring  innovative  technical  frameworks  to  break 
through the bottlenecks of traditional detection paradigms. Self-
supervised Learning, as a frontier paradigm in the field of deep 
learning,  automatically  constructs  supervision  signals  from 
unlabeled data and has demonstrated excellent performance in 
computer  vision  and  natural  language  processing  (6,  7).  This 
method is particularly suitable for addressing key challenges in 
accounting data anomaly detection: no need for large amounts of 
labeled  data,  ability  to  capture  complex  data  patterns,  and 
adaptation  to  dynamically  changing  environments.  However, 
transferring  self-supervised  learning  principles  to  the  field  of 
accounting  data  anomaly  detection  faces  numerous  technical 
challenges,  including  how  to  construct  self-supervised  tasks 
suitable for financial data characteristics, how to integrate domain 
knowledge constraints, and how to handle temporal dependencies 
and industry differences.

Ali et al., through a systematic literature review, found that 
traditional machine learning methods have obvious limitations in 
processing  high-dimensional  imbalanced  financial  data,  while 
deep  learning  significantly  improves  fraud  detection  accuracy 
through  automatic  feature  extraction  and  nonlinear  modeling 
capabilities.  However,  most  existing  research  still  relies  on 
supervised learning paradigms, and dependency on labeled data 
limits its practical application (8).

Based on the above research background, this paper proposes 
an  innovative  Hierarchical  Fusion  Self-supervised  Learning 
Framework  (HFSL),  aiming  to  break  through  the  technical

bottlenecks of accounting data anomaly detection. The framework 
uses the financial data of Chinese listed companies in the CSMAR 
database as an empirical basis to construct a three-tier cascaded 
anomaly detection mechanism: feature representation learning 
layer, relationship reasoning layer, and anomaly detection layer, 
achieving  high-precision  identification  and  early  warning  of 
accounting data anomalies through temporal contrastive learning, 
dual-channel  LSTM  autoencoder,  and 
financial  domain 
knowledge constraints.

The  innovative  contributions  of  this  research  are  mainly 
reflected  in  three  aspects:  first,  a  hierarchical  fusion  self-
supervised  learning  framework  designed  for  accounting  data 
characteristics, effectively solving detection problems in scenarios 
with scarce labeled data; second, a temporal contrastive learning 
mechanism incorporating financial domain knowledge, enhancing 
the sensitivity and interpretability of anomaly recognition; third, 
revealing  the  “financial  anomaly  waterfall  effect”  through 
multidimensional financial feature interaction analysis, providing 
theoretical basis for regulatory practice.

2 Literature review

2.1 Traditional accounting data anomaly 
detection methods

Traditional  accounting  data  anomaly  detection  methods 
primarily  include  statistical  analysis,  rule-based  systems,  and 
supervised  learning  algorithms.  Statistical  methods  identify 
anomalies  by  quantifying  the  deviation  degree  of  financial 
indicators, where the Z-score method assesses corporate bankruptcy 
risk by calculating standard deviations of financial ratios relative to 
normal distribution (33). Similar modified Z-score methods have 
further improved detection precision, but these methods typically 
assume  data  conforms  to  specific  distributions.  In  practice, 
accounting  data  often  exhibits  non-normal  distribution  and 
heteroscedasticity characteristics, which may lead to higher false 
positive  or  false  negative  rates  (9).  Rule-based  systems  rely  on 
predefined thresholds or logical conditions, such as determining 
abnormality  when  current  ratios  exceed  normal  ranges  (10). 
Although  such  methods  demonstrate  certain  effectiveness  in 
specific environments, they lack adaptability and struggle to process 
complex financial data patterns (11).

Supervised learning algorithms have been widely applied in 
anomaly detection in recent years, including technologies such as 
support  vector  machines  (SVM),  random  forests,  and  neural 
networks (12). These methods learn classification boundaries to 
identify potential anomalies by training on labeled normal and 
abnormal  samples.  However,  in  the  accounting  data  domain, 
labeled anomalous samples (such as financial fraud) are scarce, 
and the labeling process is easily influenced by subjective factors 
(13).  Furthermore,  the  performance  of  supervised  learning 
models highly depends on the quality and quantity of training 
data, and their generalization capability often performs poorly 
across different industries or time periods of financial data (14). 
Therefore, the limitations of traditional methods lie in their high 
dependency  on  labeled  data,  substantial  detection  costs,  and 
insufficient adaptability to dynamic data patterns.

Frontiers in Applied Mathematics and Statistics

02

frontiersin.org

---

<!-- PAGE 3 -->

Zhang and Duan

10.3389/fams.2025.1628652

2.2 Current applications of self-supervised 
learning

3 Self-supervised learning framework 
design

Self-supervised  learning,  as  an  emerging  machine  learning 
paradigm, generates supervision signals from unlabeled data and has 
demonstrated  significant  application  potential  across  multiple 
domains (15). In computer vision, self-supervised methods such as 
rotation prediction and contrastive learning have achieved success by 
learning  semantic  representations  of  images  (16–19).  In  natural 
language  processing,  the  BERT  model  has  achieved  deep 
understanding of text through masked language modeling tasks (20).
In  recent  years,  applications  of  self-supervised  learning  in  time 
series anomaly detection have gradually gained attention. Autoencoder-
based  methods  mark  points  with  large  reconstruction  errors  as 
anomalies by reconstructing normal time series patterns. Contrastive 
learning further enhances time series anomaly detection accuracy by 
maximizing representation consistency between similar samples (21).

Despite  significant  progress  in  the  aforementioned  domains, 
applications of self-supervised learning in accounting data anomaly 
detection remain in an exploratory stage. Accounting data possesses 
multivariate  panel  structure  and  temporal  dependencies,  posing 
unique  challenges  to  self-supervised  learning  model  design. 
Compared to image or text data, accounting data anomaly patterns 
are more concealed and strongly context-related, limiting the direct 
application of existing self-supervised methods in this field. However, 
this characteristic also provides research opportunities for developing 
self-supervised frameworks applicable to accounting data.

Contrastive learning-based methods have unique advantages in 
capturing sequential anomalies in financial data, especially in the 
financial domain where unlabeled data predominates, self-supervised 
learning can effectively overcome the challenges of scarce labeled 
data. However, the research also indicates that industry differences in 
financial  data  place  higher  demands  on  model  generalization 
capabilities, and single-structure self-supervised models struggle to 
adapt to financial data characteristics across different industries (22).

2.3 Research gaps

Research  on  accounting  data  anomaly  detection  using  the 
CSMAR database is currently limited. As an authoritative source 
of financial and market data for Chinese listed companies, the 
CSMAR database provides rich multivariate panel data, making it 
highly  suitable  for  empirical  analysis  of  anomaly  detection. 
Existing  research  predominantly  focuses  on  applications  of 
traditional statistical methods or supervised learning algorithms 
(23, 24), with insufficient exploration of self-supervised learning 
potential in this dataset. Traditional methods often struggle to 
effectively capture cross-company and cross-temporal anomaly 
patterns when processing CSMAR data, while supervised learning 
is constrained by scarce labeled data, making it difficult to fully 
exploit data features.

The effectiveness of self-supervised learning in multivariate panel 
data has not been systematically verified. The complex structure of 
accounting data requires models to simultaneously process time series 
dependencies and interactions between variables, while existing self-
supervised methods are predominantly designed for univariate time 
series or static data (25–27).

3.1 Hierarchical fusion self-supervised 
learning framework

the  multi-source  heterogeneity,

The  Hierarchical  Fusion  Self-supervised  Learning  Framework 
(HFSL)  addresses 
temporal 
dependence, and industry differentiation characteristics of accounting 
data,  breaking  through  the  limitations  of  traditional  anomaly 
detection methods. Based on self-supervised learning principles, the 
HFSL  framework  integrates  temporal  modeling  capabilities  and 
domain knowledge constraints to form a three-tier cascaded anomaly 
detection mechanism.

The first layer of the HFSL framework is the feature representation 
learning  layer,  which  enhances  the  model’s  ability  to  recognize 
temporal patterns in accounting data through Temporal Contrastive 
Learning.  Specifically,  given  an  accounting  data  sequence 
{
…1 2,
=
,
x x   are  constructed 
,i
X
x
, T
x x
δ− ≤
j∣ ∣  represents temporally close samples; negative sample 
i
where 
)
pairs (
i k∣ ∣  represents temporally 
x x  are constructed where 
,i
distant samples. Feature representations are optimized by minimizing 
the following contrastive loss function:

,  positive  sample  pairs  (

δ− >

}

)

j

j



con

= −

log

(
(
)
z z
exp sim ,
i
(
(
∑
z z
exp sim ,
i
≠
k i

j

k

)
τ
/
)
)
τ
/

Where  iz  is the feature representation of

sim ·,·  is the cosine 
similarity function, and τ is a temperature parameter. This design 
enables the model to capture temporal consistency in financial data, 
establishing a foundation for anomaly detection.

ix ,

(

)

The  second  layer  is  the  relationship  reasoning  layer,  which 
adopts a dual-channel LSTM autoencoder structure—one channel 
processes short-term financial behaviors, while the other captures 
long-term financial trends, with both types of information fused 
through an attention mechanism. Formally, the short-term channel 
h
 ,  the  long-term  channel  learns 
learns  function 
function 
w w  represents different time 
window sizes. The final representation is fused through attention 
weights α:

× →
d w
h
 , where

:
sf 
× →
d w

lf 
:

<s

l

s

l

z

=

α
·

(
f X
s

w

s

)

(
+ −
1

)
α
·

(
f X
l

w

l

)

This dual-channel design overcomes the limitations of traditional 
LSTM in multi-scale temporal pattern recognition, making it more 
suitable  for  accounting  data  characterized  by  the  coexistence  of 
quarterly fluctuations and annual trends.

The  third  layer  is  the  anomaly  detection  layer,  combining 
reconstruction errors and financial domain knowledge to achieve 
multi-dimensional anomaly judgment. Beyond basic reconstruction 
errors, financial rationality constraints are introduced, such as the 
Assets Liabilities Equity   and  revenue-
asset-liability  equation 
=
Profit Revenue Cost. The model learns not only 
cost relationship 
data  distribution  but  also  financial  rules, 
improving  the 
interpretability and accuracy of anomaly detection. Anomaly score

−

=

+

Frontiers in Applied Mathematics and Statistics

03

frontiersin.org

---

<!-- PAGE 4 -->

Zhang and Duan

10.3389/fams.2025.1628652

calculation 
violation degree:

integrates

reconstruction

error

and

rule

Score X

(

)

=

λ
·

E

recon

)

−

µ

recon

(
+ −
1

)
λ
·

E

rule

(
X
σ

recon

)

−

µ

rule

(
X
σ

rule.

where µrecon and σrecon are the mean and standard deviation of 
reconstruction errors on the training set, and µrule and σrule are the 
corresponding statistics for rule violation scores. This standardization 
ensures  that  both  components  are  on  the  same  scale,  allowing  the 
balancing parameter λ to accurately reflect the intended weight allocation 
between reconstruction-based and rule-based anomaly detection.

To  provide  a  clearer  understanding  of  the  HFSL  framework’s 
implementation,  Algorithm  1  presents  the  pseudocode  for  the 
complete framework:

The innovation of the HFSL framework is manifested in three 
aspects: first, introducing temporal contrastive learning to enhance 
sensitivity to temporal patterns in accounting data; second, designing 
a dual-channel LSTM structure to simultaneously capture short-term

Input:

Accounting data sequence X = {x₁, x₂, ..., xₜ}

Output:

Anomaly score and detection result

Parameters:

δ (temporal window), τ (temperature), λ (balance parameter)

// Feature Representation Learning Layer

for each batch in X do

Generate positive pairs (xᵢ, xⱼ) where |i − j|  (cid:304) δ

Generate negative pairs (xᵢ, xₖ) where |i − k| > δ

Compute contrastive loss using Eq.(1)

end for

// Relationship Reasoning Layer

Split X into short-term Xₛ and long-term Xₗ windows

hₛ = LSTM_short(Xₛ)        // Extract short-term patterns

hₗ = LSTM_long(Xₗ)          // Extract long-term patterns

(cid:162) = Attention(hₛ, hₗ)    // Compute attention weights

z = α · hₛ + (1 − α) · hₗ    // Fuse representations

// Anomaly Detection Layer

E_recon = ComputeReconstructionError(X, X̂ )

E_rule    = CheckFinancialRules(X)

Score      = λ · Normalize(E_recon) + (1 − λ) · Normalize(E_rule)

if Score > θ_adaptive then

return "Anomaly detected", Score

else

return "Normal", Score

ALGORITHM 1
Hierarchical fusion self-supervised learning framework.

fluctuations and long-term trends; and finally, integrating domain 
knowledge constraints to improve the accuracy and interpretability of 
anomaly  detection.  These  innovative  designs  make  the  HFSL 
framework particularly suitable for practical accounting data anomaly 
detection requirements.

Figure 1 illustrates the overall architecture of the HFSL framework. 
The framework takes accounting data from the CSMAR database as 
input and preprocesses it through a three-stage adaptive processing 
mechanism. The model centers on a three-tier cascaded structure: the 
first layer captures temporal pattern features of financial data through 
feature  representation  learning,  the  middle  layer  utilizes  a  dual-
channel LSTM structure to separately process short-term financial 
fluctuations  and  long-term  trends,  while  the  final  layer  integrates 
multi-scale scoring mechanisms, adaptive thresholds, and financial 
rule constraints to form precise anomaly identification capabilities. 
This multi-level fusion architecture promises to better analyze cross-
scale features and temporal series correlations in accounting data.

3.2 Adaptive processing mechanism for 
accounting data

Accounting  data  possesses  unique  industry  characteristics, 
seasonal  fluctuations,  and  imbalanced  distributions,  requiring 
specialized  adaptive  processing  mechanisms.  This  study  designs  a 
three-stage data adaptation process, including industry calibration, 
seasonal adjustment, and noise suppression.

The  industry  calibration  stage  addresses  the  differences  in 
financial indicators across industries by introducing industry reference 
distribution 
iP x , which represents the probability distribution of 
financial indicator x within industry i. The calibration process involves 
a two-step transformation:

(

)

(
P x
i

)

=

1

2
πσ
2
i

exp






(

x

−

−

2
)µ
i
2
σ
2
i






where µi  and σi   are  the  industry-specific  mean  and  standard 
deviation.  The  within-industry  standardized  transformation  is 
then applied:

=′

x

x

µ
i

−
σ
i

This  transformation  ensures  that  financial  indicators  are 
normalized relative to their industry-specific distributions, enabling 
the model to identify anomalies that deviate from industry norms 
rather than from the overall market average.

The seasonal adjustment stage employs the X-13 ARIMA-SEATS 
method  to  decompose  financial  indicators.  This  decomposition 
( )x t   is 
follows  an  additive  model  where  the  observed  time  series 
expressed as:

( )
x t

=

( )
T t

+

( )
S t

+

( )
R t

Frontiers in Applied Mathematics and Statistics

04

frontiersin.org

---

<!-- PAGE 5 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 1
Architecture of the hierarchical fusion self-supervised learning framework (HFSL).

( )T t  represents the trend component,  ( )S t  the seasonal 
Where 
( )R t  the residual component. The trend component 
component, and 
( )T t   is  extracted  using  a  Henderson  moving  average  filter,  which 
minimizes  the  variance  of  the  third  difference  of  the  trend.  For 
quarterly data, we apply a 13-term Henderson filter:

( )
T t

=

6
∑
=−
6
j

(
w x t
·j

+

)

j

Where the weights

jw  are symmetric (

w ) and sum to unity. 
The seasonal component  ( )S t  is modeled using a seasonal ARIMA 
specification.  For  quarterly  financial  data,  we  employ  an  ARIMA 
(0,1,1) (0,1,1)4 model, which can be expressed as:

w

j

−=j

(
1

−

B

)(

1

−

4

( )
B S t

)

(
= −
1

θ
B
1

)(

1

4

− Θ
B
1

)

∈
t

where  B   is  the  backshift  operator,  θ1  and

1È   are  the 
seasonal  moving  average  parameters 
non-seasonal  and 
tò   is  white  noise.  The  seasonal  factors  are 
respectively,  and 
constrained  to  sum  to  zero  over  a  complete  year  to  ensure

identifiability.  After  extracting 
components, the residual component is obtained as:

the

trend  and  seasonal

( )
R t

=

( )
x t

−

( )
T t

−

( )
S t

The residual component

( )R t  contains both irregular variations 
and potential anomalies. To distinguish between normal irregular 
fluctuations and true anomalies, we apply a robust scale estimator 
based on the median absolute deviation (MAD):

(
MAD median |

=

( )
R t

−

median

(

( )
R t

)

)
|

×

values

residual

Financial

indicators  with

exceeding 
± ×
3 1.4826 MAD are flagged as potential anomalies, where 1.4826 is 
the  consistency  constant  for  normal  distributions.  This  approach 
effectively separates legitimate seasonal patterns, such as year-end 
inventory adjustments or quarterly revenue cycles, from suspicious 
deviations that may indicate financial manipulation.

The  noise  suppression  stage  introduces  an  adaptive  weighting 
strategy  that  adjusts  feature  weights  based  on  data  reliability.  For

Frontiers in Applied Mathematics and Statistics

05

frontiersin.org

---

<!-- PAGE 6 -->

Zhang and Duan

10.3389/fams.2025.1628652

high-noise features, their weights in anomaly calculations are reduced 
to improve detection stability. This mechanism is particularly suitable 
for handling financial data of varying quality and completeness in the 
CSMAR database.

3.3 Adaptive threshold determination and 
multi-scale anomaly scoring

The key to anomaly detection lies in threshold determination. This 
study  proposes  an  adaptive  dynamic  threshold  mechanism  that 
automatically  adjusts  thresholds  based  on  data  distribution  and 
business requirements. The basic approach is to fit reconstruction 
error distributions using Gaussian Mixture Models (GMM):

( )
p e

K
= ∑
=
k
1

π
k

(
e ∣

2
µ σ
,
k
k

)

where  e  represents  reconstruction  error,  and πk,  µk,  and σk 
represent the mixing coefficient, mean, and standard deviation of the 
K  Gaussian component, respectively. The threshold is set to a specific 
quantile of the high-variance component:

θ µ ασ
+h
h

=

where  µh  and  σh  are  the  parameters  of  the  high-variance 
component,  and α  is  an  adjustable  coefficient  that  balances  false 
positive and false negative rates according to business requirements.

This study introduces a multi-scale anomaly scoring mechanism 
that comprehensively considers three levels: point anomalies, sequence 
anomalies,  and  relationship  anomalies.  Point  anomalies  focus  on 
abnormal values at individual time points, sequence anomalies detect 
abnormal patterns in time series, and relationship anomalies identify 
abnormal changes in relationships between multiple variables. The 
final anomaly score is a weighted combination of the three:

Score

final

(

)

X

=

w

p

·Score

p

(

)
+
X w

·Score

s

s

(

)
+
X w

·Score

r

r

(

X

)

pw ,

where

sw ,  and

rw   are  weight  parameters.  While  this 
formulation presents the final score as a linear combination, the three 
anomaly  components  are  not  statistically  independent.  Their 
interdependencies arise from the inherent structure of financial data 
and manifest through several mechanisms.

The  correlation  structure  among  the  three  components  can

be characterized by the correlation matrix:

ρ ρ

C



= 



1
ρ
ps

ps
1
ρ ρ
sr

pr

pr
ρ
sr
1







i

ij

(

(

Where

ρ = Corr

)
)
Score X Score X  represents the Pearson 
,
correlation between components i and  j. Empirical analysis on our 
correlations: 
dataset 
ρ
=
, indicating 
ps
that these components capture partially overlapping anomaly patterns.

reveals 
ρ

±
0.42 0.08,

, and ρ =

±
0.38 0.06

±
0.51 0.09

moderate

positive

=

pr

(

)

sr

j

sr

The strongest correlation occurs between sequence anomalies and 
relationship anomalies (ρ = 0.51
), which is expected as violations in 
financial relationships often manifest as abnormal temporal patterns. 
For instance, when the relationship between revenue and accounts 
receivable is disrupted (relationship anomaly), it frequently leads to 
unusual trends in subsequent periods (sequence anomaly). To account 
for these interactions, we introduce a second-order adjustment term:

Score

adjusted
final

(

)

X

=

Sc re
o

final

(

)

X

+ ∑
λ
int
<
j
i

w w
i

ρ
ij

j

)
Score X Score X

(

(

)

i

j

Where  λ =int

0.05   is  the  interaction  coefficient  determined 
through cross-validation. This adjustment captures the synergistic 
effect when multiple anomaly types co-occur, improving detection 
accuracy for complex financial manipulations.

Furthermore,  we  observe  that  the  presence  of  relationship 
anomalies often serves as a catalyst that amplifies the significance of 
point anomalies. This conditional dependency is modeled through a 
gating mechanism:

(
g X

)


σ
= 



(
Score X
r
τ

) θ
−
r






Where

( )σ ·  is the sigmoid function, θr is the relationship anomaly 
threshold,  and τ= 0.1  is  a  temperature  parameter.  The  gated  final 
score becomes:

Score

gated
final

(

)

X

=

Score

adjusted
final

(

)

(
× +
1

X

β
·

(
g X

)

)

Where β= 0.15  represents  the  maximum  amplification  factor. 
This  gating  mechanism  ensures  that  when  strong  relationship 
anomalies  are  present,  the  model  increases  its  sensitivity  to  other 
anomaly  types,  reflecting  the  empirical  observation  that  financial 
fraud often involves multiple coordinated manipulations.

Through  ablation  studies,  we  demonstrate  that  incorporating 
these  interaction  effects  improves  the  overall  F1-score  by  4.2% 
compared  to  treating  the  components  as  independent,  with 
particularly  notable  improvements  in  detecting  complex  fraud 
patterns involving multiple financial statement items.

In summary, the innovative self-supervised learning framework 
HFSL proposed in this study is specifically designed for accounting 
data characteristics, integrating temporal contrastive learning, dual-
channel LSTM structure, domain knowledge constraints, and multi-
scale  anomaly  scoring  mechanisms  to  provide  a  theoretical  and 
technical foundation for accounting data anomaly detection.

4 Research methods and 
implementation

4.1 Data preprocessing

4.1.1 Data sources and sampling strategy

This research uses financial data of Chinese listed companies from 
the CSMAR database, with samples covering quarterly and annual

Frontiers in Applied Mathematics and Statistics

06

frontiersin.org

---

<!-- PAGE 7 -->

Zhang and Duan

10.3389/fams.2025.1628652

financial data of all companies listed on the A-share market from 2000 
to 2020. As an authoritative data source for Chinese capital market 
research,  the  CSMAR  database  provides  standardized,  highly 
continuous  financial  data,  including  balance  sheets,  income 
statements,  cash  flow  statements,  and  related  financial  indicators, 
establishing a solid data foundation for anomaly detection research 
(28–30).

The  sampling  strategy  employs  stratified  random  sampling, 
stratifying samples by industry, size, and listing duration to ensure 
representativeness and balance in data distribution. To mitigate the 
interference of industry characteristics on anomaly detection, this 
study categorizes samples into 10 major industry categories according 
industry 
to 
classification standards, using the same sampling proportion within 
each  industry.  The  final  dataset  includes  31,724  company-quarter 
observations, and after excluding ST, *ST companies and samples with 
severe data missing, 28,569 valid observations were retained.

the  China  Securities  Regulatory  Commission’s

4.1.2 Data cleaning and standardization 
processing

inconsistencies,

Accounting data commonly exhibits missing values, outliers, and 
scale 
and 
standardization processing (31, 32). This study adopts the following 
procedures for data preprocessing:

systematic

requiring

cleaning

Missing  value  processing:  Different  strategies  are  applied  to 
different  types  of  missing  data.  For  Missing  At  Random  (MAR), 
multiple linear interpolation is used, estimating missing values based 
on adjacent time points and related financial indicators; for Missing 
Not  At  Random  (MNAR),  such  as  systematically  missing  specific 
financial indicators, industry means are used as substitutes or the 
observation samples are directly eliminated. Financial indicators with 
missing rates exceeding 20% are removed, and samples with missing 
value proportions exceeding 30% are eliminated.

Outlier processing: Recognizing the multidimensional nature of 
financial  data,  this  study  employs  a  two-stage  outlier  detection 
approach that considers multivariate relationships. In the first stage, 
we  apply  the  Local  Outlier  Factor  (LOF)  algorithm  to  identify 
multivariate outliers by examining the local density deviation of each 
data point relative to its neighbors. The LOF score for each observation 
is calculated as:

∑
(
∈
o N x
k

( )
lrd o
k
)
(
lrd x
)
k
)
(
∣
N x∣
k

LO

F
k

(

x

)

=

(

)

k

Where 
)
(

lrd x  is the local reachability density of point x, and 
kN x  represents the k-nearest neighbors of x. We set k = 20 based 
on empirical testing, and observations with LOF scores exceeding 2.5 
are flagged as potential outliers.

In the second stage, we validate these multivariate outliers using 
an Isolation Forest algorithm, which efficiently isolates anomalies by 
constructing  random  decision  trees.  The  anomaly  score 
is 
computed as:

−

)

)

(
(
E h x
( )
c n

(
s x n
,

)

=

2

)

(

)

Where

(
E h x  is the expected path length for observation x, and 
( )
c n  is the average path length of unsuccessful search in a Binary 
Search Tree. Only observations identified as outliers by both methods 
(LOF  score  >  2.5  and  Isolation  Forest  anomaly  score  >0.6) 
undergo adjustment.

For  confirmed  outliers,

instead  of  applying  univariate 
Winsorization, we employ a multivariate adjustment approach that 
preserves the correlation structure. Specifically, we project the outlier 
onto the boundary of the 99% confidence ellipsoid in the direction 
from the data center:

x

adjusted

1/2
= + ⋅Σ ⋅

µ α

−
µ
x
−
µΣ
x

Where µ is the robust center estimated using the Minimum 
Covariance  Determinant  (MCD)  estimator,  Ó  is  the  robust 
covariance matrix, and α is chosen such that  adjusted
 lies on the 
99% confidence ellipsoid boundary. This approach preserves the 
multivariate  structure  while  reducing  the  influence  of  extreme 
observations, ensuring that potentially fraudulent patterns remain 
detectable while mitigating the impact of data errors or legitimate 
extreme business events.

x

All adjusted data points are recorded with their original values 
and adjustment ratios for transparency and subsequent validation in 
the anomaly detection phase.

Data  standardization:  Financial  indicators  exhibit  significant 
differences  in  measurement  scales  and  distributions.  Z-score 
standardization  transforms  different  indicators  to  make  them 
comparable on the same scale:

X

Z

i j t
,
,

=

−

µ
j i
,

i j t
,
,
σ

j i
,

i j tX
,
,

Where

represents  the  value  of  financial  indicator  j  for 
company i at time t, and µ ,j i and σ ,j i represent the mean and standard 
deviation of the company’s historical data, respectively. This company-
internal  standardization  method  both  preserves  cross-temporal 
variation  characteristics  and  avoids  biases  from  direct  cross-
company comparisons.

Time series adjustment: Considering the seasonality and trend 
characteristics of accounting data, the X-13 ARIMA-SEATS method 
is  applied  to  seasonally  adjust  quarterly  data,  separating  trend 
components,  seasonal  components,  and  random  components, 
providing a stable data foundation for time series modeling.

4.2 Feature engineering

4.2.1 Financial indicator selection and 
construction

Based on accounting theory and practical experience, this study 
selects  and  constructs  a  financial  indicator  system  from  four 
dimensions:  profitability,  solvency,  operational  efficiency,  and 
cash flow:

Profitability  indicators:  Including  Return  on  Equity  (ROE), 
Return  on  Assets  (ROA),  Net  Profit  Margin  (NPM),  Gross  Profit

Frontiers in Applied Mathematics and Statistics

07

frontiersin.org

---

<!-- PAGE 8 -->

Zhang and Duan

10.3389/fams.2025.1628652

Margin (GPM), Operating Profit Margin (OPM), and Earnings Per 
Share (EPS), reflecting a company’s ability to generate profits.

Solvency indicators: Including Current Ratio (CR), Quick Ratio 
(QR), Leverage Ratio (LEV), Interest Coverage Ratio (ICR), and Cash 
Flow to Debt Ratio (CFD), reflecting a company’s ability to repay debts.
Operational efficiency indicators: Including Inventory Turnover 
Rate (ITR), Accounts Receivable Turnover Rate (ARTR), Total Asset 
Turnover  Rate  (TATR),  and  Fixed  Asset  Turnover  Rate  (FATR), 
reflecting asset utilization efficiency.

Cash  flow  indicators:  Including  Operating  Cash  Flow  (OCF), 
Cash Flow Adequacy Ratio (CFAR), Sales Cash Ratio (SCR), and Free 
Cash  Flow  (FCF),  reflecting  a  company’s  cash  generation  and 
management capabilities.

In addition to basic financial indicators, the following composite 
indicators were constructed to enhance anomaly detection capabilities:
Accounting quality indicators: Modified Jones model indicators 
items,  used  to  measure  the  degree  of

based  on  accrual 
earnings management.

Financial  stability  indicators:  Variants  of  Altman  Z-score  and 
Beneish  M-score,  adapted  to  the  characteristics  of  China’s 
capital market.

Growth  consistency  indicators:  Measuring  the  coordination 
between revenue growth and asset growth, cost growth, and other 
indicators to identify unreasonable financial growth patterns.

4.2.2 Feature extraction and dimensionality 
reduction

The initial feature set contained 42 financial indicators, presenting 
issues  of  high  dimensionality  and  multicollinearity. The  following 
and 
methods 
dimensionality reduction:

processing

feature

were

used

for

Correlation  analysis:  Calculating  the  Pearson  correlation 
coefficient  matrix  to  identify  highly  correlated  indicator  pairs 
indicators  with  more  significant 
(|r| > 0.85)  and  retaining 
financial meaning.

Principal  Component  Analysis

(PCA):  Applying  PCA 
dimensionality  reduction  to  standardized  financial  indicators, 
retaining principal components with cumulative explained variance 
reaching  90%,  mapping  high-dimensional  financial  data  to  a 
low-dimensional representation space.

structure,

Autoencoder  feature  extraction:  Based  on  a  nonlinear 
autoencoder 
latent 
learning 
representations of financial data with minimal reconstruction error 
as the objective. The autoencoder consisted of a 3-layer encoding 
network  and  a  3-layer  decoding  network,  compressing 
42-dimensional  original  features  to  16-dimensional 
latent 
representations through batch training.

low-dimensional

Temporal feature construction: Calculating statistical features 
within sliding windows, including mean, standard deviation, rate 
of  change,  kurtosis,  and  skewness,  to  capture  dynamic  change 
patterns of financial indicators. Additionally, extracting multi-scale 
time-frequency  features  based  on  Discrete  Wavelet  Transform 
(DWT) to enhance the model’s ability to recognize anomalies at 
different frequencies.

SHAP feature importance assessment: Using SHAP (SHapley 
feature’s 
Additive  exPlanations)  values 
contribution  to  anomaly  identification,  dynamically  adjusting 
feature weights based on contribution degree to optimize detection 
precision. Ultimately, 22 core financial indicators were selected as 
model inputs.

to  evaluate  each

Figure 2 illustrates the results of financial feature importance 
analysis and anomaly type analysis. The left side uses horizontal bar 
charts to intuitively present the SHAP value ranking of the 8 financial 
indicators that contribute most to anomaly detection. The results 
show  that  profitability  indicators  play  a  core  role  in  anomaly 
detection, with Return on Equity (ROE, 0.196) and Return on Assets 
(ROA, 0.179) having significantly higher contributions than other 
indicators, followed closely by Current Ratio (0.163) and Leverage 
Ratio (0.149), indicating that solvency indicators are also important 
dimensions  for  financial  anomaly  identification.  The  right  side

FIGURE 2
Financial feature importance analysis and anomaly distribution.

Frontiers in Applied Mathematics and Statistics

08

frontiersin.org

---

<!-- PAGE 9 -->

Zhang and Duan

10.3389/fams.2025.1628652

systematically displays five typical financial anomaly patterns and 
their characteristics, including revenue inflation (38.6%), expense 
concealment  (21.7%),  asset  overvaluation  (17.4%), 
liability 
understatement (15.2%), and composite manipulation (7.1%), and 
provides key features and detection rate data for each type of anomaly. 
This  dual  analysis  framework  not  only  reveals  the  importance 
hierarchy of financial features but also demonstrates the identification 
patterns of different types of financial anomalies, providing intuitive 
support  for  the  model’s  effectiveness  in  distinguishing  between 
normal and anomalous financial data.

4.3 Model design and training

4.3.1 Dual-channel LSTM autoencoder 
architecture

Based  on  the  Hierarchical  Fusion  Self-supervised  Learning 
(HFSL) framework proposed in Chapter 3, this study designs a dual-
channel LSTM autoencoder to implement self-supervised learning 
and anomaly detection for accounting data. The specific architecture 
is as follows:

Input layer: Receives time series data of 22-dimensional financial 
indicators, with the short-term channel input window size set to 4 
(corresponding to 1 year of data) and the long-term channel input 
window size set to 12 (corresponding to 3 years of data).

Encoder  layer:  The  short-term  and  long-term  channels  each 
contain bidirectional LSTM layers with 64 and 128 units respectively, 
capturing financial patterns at different time scales. The LSTM layers 
adopt 
integrating  financial 
an 
prior information:

improved

structure,

cell

f

t

i
t
=


C
t

o
t

=

=

(
σ

W h
·

f
t
(
σ

W h
·

i
t
(

·
tanh
W h

t
C
f

=
C
t
(
σ
=

·
W h

o
t
=
o

t

C
t

h
t



t

−
1

,

x p
,
t
t

−
1

,

x p
,
t
t

+



+




,

−
1
+

−
1

i
t


,
x p

t
t

C
t
+


)

,

,
x p
−
t
t
1
(
tanh
C
t

b

b
i
+

)

f
)
b
C

)

)

b
o

where

tp   represents  financial  prior  information,  including

industry means, historical trends, and other domain knowledge.

Attention  fusion  layer:  Integrates  short-term  and  long-term

representations through an adaptive attention mechanism:

e

s

e
l

α
s

α
l

z

=

=

T

=

v

T

=

v

tanh

(
W h
s s
(
W h
tanh
l
l
(
)
e
exp
s
)
+
exp
s
)
(
e
exp
l
)
(
+
exp
s
α α
h
l
s s

h
l

+

(

(

(

e

e

)
)

)

)

e
l

e
l

exp

exp
=

where  sh  and  lh  are the hidden states of the short-term and long-
term encoders respectively, αs and αl are the corresponding attention 
weights, and z is the fused representation.

Latent representation layer: Applies a fully connected layer to the 
fused representation to obtain a 32-dimensional latent representation, 
which serves as the decoder input.

Decoder  layer:  Employs  bidirectional  LSTM  layers  with  a 
symmetrical  structure  to  restore  the  latent  representation  to  the 
original input dimension. The short-term and long-term decoders 
reconstruct the financial data for their respective time windows.

Output layer: Maps to the original feature space through a fully

connected layer, generating the reconstructed sequence.

To  enhance  model  robustness,  a  Dropout  layer  (dropout 
rate = 0.3)  is  added  between  the  encoder  and  decoder,  and  Batch 
Normalization is applied in the reconstruction layer.

The

implementation  details  of  the  dual-channel  LSTM

autoencoder are presented in Algorithm 2.

4.3.2 Model training and optimization

The following training strategies are adopted for the characteristics

of self-supervised learning and accounting data:

Loss  function  design:  Optimizes  the  model  by  combining

reconstruction loss and contrastive loss:



=

λ


1 recon

+

λ


2 con

where  reconstruction  loss

recon
  is  calculated  based  on  the 
temporal contrastive learning method introduced in Chapter 3. λ1, λ2,  
and β are balancing parameters determined through grid search to 
find optimal values.

Training  strategy:  Employs  a  phased  training  strategy,  first 
training  the  short-term  and  long-term  channels  separately,  then 
performing  joint  optimization.  Data  is  divided  into  training, 
validation, and test sets in a 0.7:0.15:0.15 ratio, with the training set 
containing only normal samples, while validation and test sets contain 
both normal and anomalous samples. Batch size is set to 64, using an 
early stopping mechanism (patience = 20) to avoid overfitting.

Optimizer selection: Adopts the Adam optimizer with an initial 
learning rate of 0.001, applying a learning rate scheduling strategy 
with 10% decay every 30 epochs.

Hyperparameter optimization: Searches for key hyperparameters 
through Bayesian optimization, including LSTM layer numbers (1–3), 
hidden unit numbers (32–256), Dropout rates (0.1–0.5), attention 
dimensions (16–128), etc., with F1-score on the validation set as the 
optimization  objective.  The  final  optimal  model  configuration  is: 
short-term channel with 2 LSTM layers (64 units), long-term channel 
with 2 LSTM layers (128 units), Dropout rate of 0.3, and attention 
dimension of 64.

Model implementation uses the PyTorch 1.9.0 framework, with 
training conducted on a server equipped with an NVIDIA V100 GPU, 
taking  approximately  18 h,  and  resulting  in  a  final  model  with 
1.8 M parameters.

Figure 3 shows the 3D visualization of reconstruction errors from 
the  dual-channel  LSTM  autoencoder  and  time  series  analysis  of 
anomaly scores. The left image uses a three-dimensional bar chart to 
present the distribution of reconstruction errors for different financial 
indicators across years, with a gradient color scheme from blue (low 
error) to red (high error) intuitively displaying the model’s excellent 
modeling effect on key indicators such as ROE and ROA. The right 
image uses time series graphs with filled areas to show the anomaly 
score trend changes of three typical companies: Company A exhibits

Frontiers in Applied Mathematics and Statistics

09

frontiersin.org

---

<!-- PAGE 10 -->

Zhang and Duan

10.3389/fams.2025.1628652

Input:

Financial indicators sequence X  (cid:281) ℝᵀˣᴰ

Output:

Reconstructed sequence X̂ , anomaly score

Parameters:

window_short = 4

window_long = 12

// Encoding Phase

X_short = SlidingWindow(X, window_short)

X_long    = SlidingWindow(X, window_long)

// Short‑term channel

hₛ¹ = BiLSTM(X_short, units=64)

hₛ² = BiLSTM(hₛ¹, units=64)

h_s    = Dropout(hₛ², rate=0.30)

// Long‑term channel

hₗ¹ = BiLSTM(X_long, units=128)

hₗ² = BiLSTM(hₗ¹, units=128)

h_l    = Dropout(hₗ², rate=0.35)

// Attention fusion

e_s = tanh(W_s · h_s)

e_l = tanh(W_l · h_l)

(cid:162)_s = softmax(e_s)

(cid:162)_l = softmax(e_l)

z      = α_s · h_s + α_l · h_l

// Decoding Phase

z_latent = Dense(z, units=32)

X̂ _short = Decoder_LSTM(z_latent, window_short)

X̂ _long    = Decoder_LSTM(z_latent, window_long)

return X̂ _short, X̂ _long

ALGORITHM 2
Dual-channel LSTM autoencoder architecture.

a gradual deterioration pattern and breaches the anomaly threshold 
in mid-2018, Company B shows sudden anomalies after 2018, while 
Company C consistently maintains within the normal range below the 
threshold. This multi-dimensional analysis intuitively demonstrates 
the  framework’s  capability  to  identify  different  types  of  financial 
anomalies and its early warning characteristics.

The  HFSL  framework  incorporates  a  concept  drift  detection 
mechanism based on the Page-Hinkley test to monitor changes in

fraud  patterns  over  time.  The  system  tracks  the  distribution  of 
anomaly scores within sliding windows and triggers model adaptation 
when significant drift is detected. This adaptive mechanism ensures 
the model remains effective despite evolving fraud techniques and 
regulatory changes.

4.4 Anomaly detection and evaluation 
mechanism

4.4.1 Multi-dimensional anomaly score 
calculation

This study integrates three anomaly scoring methods to improve

detection accuracy:

Reconstruction error score: Calculates the weighted Euclidean 
distance  between  the  original  sequence  and  the  reconstructed  
sequence:

Score

recon

(

)

X

=

T d
∑ ∑
= =
j
t
1
1

(
w x
j

t j
,

−

ˆ
x

t j
,

2

)

where

jw   represents  the  importance  weight  of  feature  j,

determined through SHAP values.

Score

pred

(

)

X

=

1
T

T d
∑ ∑
= =
j
t
1
1

(
(
w I sign x

·

j

t

+

1,

j

−

x

t j
,

)

≠

(
ˆ
sign x

t

+

1,

j

−

ˆ
x

t j
,

)

)

where  ( )·I
of trend predictions.

is an indicator function, measuring the inconsistency

Rule violation score: Quantifies the degree of violation of financial

logic rules:

Score

rule

(

)

X

R
= ∑
=
r
1

w

r

·Violation

r

(

)

X

and

Violationr X  measures the degree of violation of rule r ,

(
where 
rw  is the importance weight of the rule.
The three scores are integrated through weighted fusion to form

)

the final anomaly score:

co
S

re

final

(

)

X

=

α

ˆ
S
·
1 recon

(

X

)

+

α

ˆ
S
·
2 pred

(

X

)

+

α

ˆ
S
·
3 rule

(

)

X

To ensure fair comparison and proper weight allocation among 
different  scoring  components,  each  score  is  standardized  using 
z-score normalization:

(
ˆ
S X
i

)

=

(
) µ
−
S X
i
i
σ
i

(

)

Where

iS X  represents the raw score for component i (recon, 
pred,  or  rule),  and  µi, σi   are  the  mean  and  standard  deviation 
estimated from the training set normal samples.

Frontiers in Applied Mathematics and Statistics

10

frontiersin.org

---

<!-- PAGE 11 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 3
Multi-company anomaly score time series analysis.

The standardization process ensures that all three components 
contribute to the final score according to their assigned weights α1, α2 
and α3, regardless of their original scale differences. Through genetic 
algorithm optimization on the validation set, the optimal weights were 
determined  as  0.5,  0.3,  and  0.2  respectively,  reflecting  the  relative 
importance of reconstruction accuracy, prediction consistency, and 
rule compliance in identifying accounting anomalies.

4.4.2 Adaptive threshold determination

To  address  the  limitations  of  traditional  fixed  thresholds,  this 
study  employs  Gaussian  Mixture  Models  (GMM)  to  adaptively 
determine detection thresholds:

Fitting a K-component GMM (K = 3) to the anomaly scores of

normal samples in the training set:

(

p

score

)

K
= ∑
=
k
1

π
k



(

score

∣

2
µ σ
,
k
k

)

Identifying the component with the largest variance (typically 
corresponding to marginal normal samples) and setting the threshold 
based on this component:

=
θ µ

high

+

γσ
·

high

where γ  is  an  adjustable  coefficient,  with  the  optimal  value

determined through ROC curve analysis (this study uses 2.5).

To  accommodate  industry  and  size  differences,  a  stratified 
adaptive threshold strategy is further designed, calculating thresholds 
separately  for  companies  in  different  industries  and  market 
capitalization intervals to improve detection precision.

5 Experimental design

5.1 Data preparation

5.1.1 Dataset division

For  reproducibility,  data  preprocessing  follows  standardized 
Z-score normalization within companies, and the chronological split 
(2000–2010  training,  2011–2015  validation,  2016–2020  testing) 
ensures temporal validity while preventing data leakage.

To evaluate the model’s performance across different time periods 
and its generalization ability, this study adopts a chronological division 
strategy,  partitioning  the  Chinese  listed  companies’  financial  data 
from  the  CSMAR  database  (2000–2020)  into  non-overlapping 
training, validation, and test sets. Specifically, data from 2000 to 2010 
is designated as the training set, accounting for 62.3% of the total 
sample with 17,817 valid observations; data from 2011 to 2015 serves 
as the validation set, representing 19.8% with 5,654 observations; and 
data from 2016 to 2020 forms the test set, comprising 17.9% with 
5,098 observations. This time-series partitioning effectively simulates 
real-world  application  scenarios,  enabling  the  model  to  predict 
potential future anomalies based on historical data while testing its 
adaptability to changing market environments.

During the training phase, following the self-supervised learning 
paradigm, only normal samples are used for model training, with 
anomalous samples reserved exclusively for performance evaluation 
during validation and testing phases. To mitigate the impact of data 
distribution changes over time, this study introduces a sliding window 
mechanism with a window length of 12 quarters (corresponding to 
3 years of financial data), sliding one quarter at a time. This approach 
both  preserves  the  temporal  dependencies  in  financial  data  and 
enhances the model’s ability to recognize long-term financial trends. 
Additionally,  stratified  sampling  based  on  the  China  Securities

Frontiers in Applied Mathematics and Statistics

11

frontiersin.org

---

<!-- PAGE 12 -->

Zhang and Duan

10.3389/fams.2025.1628652

Regulatory Commission’s industry classification standards ensures 
consistent  industry  distribution  across  training,  validation,  and 
test sets.

Data preprocessing follows the three-stage adaptive processing 
procedure  proposed  in  Chapter  4,  including  industry  calibration, 
seasonal adjustment, and noise suppression. Specifically, for missing 
values in the training set, a combination of forward filling and linear 
interpolation  is  employed;  for  the  validation  and  test  sets,  only 
statistical characteristics from the training set are used for filling to 
avoid  information  leakage.  For  standardization,  company-internal 
Z-score standardization is applied to preserve cross-temporal variation 
characteristics while avoiding comparison biases between companies 
of different scales:

X

Z

i j t
,
,

=

i j t
,
,
σ

−

µ
j i
, ,train

j i
, ,train

where µ , ,train

j i

and σ , ,train
j i

represent the mean and standard

deviation of financial indicator j for company i in the training set.

5.1.2 Anomaly identification

Anomaly  labeling  in  our  self-supervised  framework  follows  a 
hybrid approach: real anomalies are identified from verified fraud 
cases  in  CSMAR  database  and  regulatory  announcements,  while 
maintaining  unlabeled  normal  samples  for  training  as  per  self-
supervised learning principles.

To  comprehensively  evaluate  the  performance  of  anomaly 
detection  algorithms,  this  study  constructs  a  composite  test  set 
containing  both  real  anomalies  and  simulated  anomalies.  Real 
anomaly samples are derived from three sources: financial fraud cases 
and major accounting error correction cases marked in the CSMAR 
database (117 companies); companies suspected of financial anomalies 
identified through media reports and regulatory announcements (56 
companies); and listed companies issued with non-standard audit 
opinions  (243  instances),  covering  qualified  opinions,  adverse 
opinions, and disclaimers of opinion. These real anomaly samples 
primarily involve violations such as inflated revenue, inflated profits, 
and concealed liabilities, exhibiting certain distribution characteristics 
across industries and time dimensions.

Considering the limitations of real anomaly samples, this study 
designs and constructs four types of simulated anomaly samples to 
enrich the testing system: (1) financial indicator mutation anomalies, 
introducing abnormal fluctuations exceeding 3 standard deviations in 
key indicators such as ROE and ROA; (2) financial ratio inconsistency 
anomalies, disrupting intrinsic relationships between key ratios such 
as gross profit margin and net profit margin; (3) temporal pattern 
anomalies, altering the seasonal and trend characteristics of financial 
indicators;  and  (4)  accounting  equation  violation  anomalies, 
introducing  subtle  violations  of  basic  accounting  principles  while 
maintaining surface consistency. The generation process for simulated 
anomalies  strictly  follows  three  principles:  domain  knowledge 
constraints,  reasonable  distribution  of  anomaly  intensity,  and 
consideration  of  industry  differences,  ensuring  conformity  with 
characteristic distributions of actual financial anomalies.

The final anomaly sample repository contains 894 real anomaly 
cases  and  1,256  simulated  anomaly  cases,  totaling  2,150  anomaly 
samples. For scientific performance evaluation, samples are allocated

to validation and test sets in a 9:1 ratio, while maintaining consistent 
distribution of various anomaly types in both sets. Anomaly samples 
in the validation set are used for model optimization and threshold 
determination,  employing  5-fold  cross-validation  to  establish  the 
optimal detection threshold (μ + 2.5σ); the test set is used for final 
performance  evaluation,  covering  both  overall  and  category-
specific assessments.

5.2 Experimental setup

The experimental environment is implemented based on Python 
3.8 and the PyTorch 1.9.0 framework, with model training and testing 
conducted on a high-performance computing server equipped with 
an Intel Xeon E5-2690 v4 CPU, 64GB memory, and an NVIDIA Tesla 
V100 32GB GPU. Considering data scale and model complexity, a 
distributed training framework is adopted to improve computational 
efficiency, with data parallelism set to 4.

The core of the self-supervised learning framework—the dual-
channel LSTM autoencoder—is configured as follows: the short-term 
channel input window size is set to 4 quarters (1 year), with 2 LSTM 
layers,  64  hidden  units,  and  a  dropout  rate  of  0.3;  the  long-term 
channel input window size is set to 12 quarters (3 years), with 2 LSTM 
layers, 128 hidden units, and a dropout rate of 0.35. The attention 
fusion layer dimension is set to 64, and the latent representation layer 
dimension  is  32.  The  model  contains  approximately  1.83  M 
parameters, with the short-term channel accounting for 27.3%, the 
long-term  channel  for  45.8%,  and  the  attention  fusion  and  latent 
representation layers for 26.9%.

The  training  process  adopts  the  following  strategy:  first 
conducting staged optimization, pre-training the short-term and 
long-term  channels  separately  for  15  epochs,  followed  by  joint 
optimization training for 40 epochs. The batch size is set to 64, with 
an initial learning rate of 0.001, using an Adam optimizer with 0.9 
momentum, and learning rate decay to 0.8 times its original value 
every 10 epochs. To prevent overfitting, L2 regularization (weight 
decay  coefficient  of  1e-5)  and  an  early  stopping  mechanism 
(patience = 12) are applied. The loss function adopts a weighted 
combination of reconstruction loss and contrastive loss as defined 
in Chapter 3, with weight coefficients λ1 and λ2 determined through 
grid search as 0.7 and 0.3.

To address varying time series length issues, forward filling is 
employed for sequences shorter than the specified window length, 
while sliding window sampling is used for excessively long sequences. 
Data  batch  construction  adopts  a  temporally  proximate  sampling 
strategy, ensuring temporal coherence within each batch to enhance 
the model’s ability to learn temporal patterns. For each financial data 
sample,  random  masking  (masking  rate  10%)  is  applied  as  a  data 
augmentation technique to improve model robustness.

To comprehensively evaluate the effectiveness of the proposed 
method,  four  comparison  benchmark  experiment  groups  are 
established:  (1)  traditional  statistical  methods  group,  including 
Z-score-based anomaly detection and improved Benford analysis; (2) 
machine  learning  baseline  group,  including  One-Class  SVM  and 
Isolation Forest; (3) deep learning baseline group, including standard 
LSTM autoencoder and Variational Autoencoder (VAE); and (4) self-
supervised  variant  group,  exploring  the  impact  of  different  self-
supervised strategies on anomaly detection performance, including

Frontiers in Applied Mathematics and Statistics

12

frontiersin.org

---

<!-- PAGE 13 -->

Zhang and Duan

10.3389/fams.2025.1628652

reconstruction tasks, prediction tasks, and contrastive learning tasks. 
All baseline methods are trained and evaluated on identical datasets 
to ensure fair comparison.

The evaluation process follows iterative optimization principles, 
optimizing  model  hyperparameters  on  the  validation  set  through 
5-fold cross-validation. Anomaly threshold determination employs a 
GMM-based  adaptive  method,  calculating  optimal  thresholds 
separately  for  each  industry.  Final  performance  evaluation  is 
conducted on the independent test set, introducing evaluation metrics 
specific to financial anomaly detection in addition to conventional 
precision, recall, F1-score, and AUC-ROC: early detection rate (EDR, 
the proportion detected within the first two quarters after anomaly 
occurrence)  and  false  alarm  rate  (FAR,  the  proportion  of  normal 
samples incorrectly classified as anomalous).

Experimental results are validated for statistical significance using 
the  Wilcoxon  signed-rank  test  (p < 0.05),  with  sensitivity  analysis 
assessing the impact of key parameter changes on model performance 
to ensure robustness and generalizability of conclusions.

To  assess  the  model’s  robustness  to  evolving  fraud  patterns, 
we conducted concept drift experiments by dividing the test period 
into quarterly segments and introducing synthetic pattern changes at 
specific time points corresponding to major regulatory events. Model 
adaptation capability was evaluated through performance stability 
metrics and recovery time after drift detection.

5.3 Evaluation metrics

To comprehensively evaluate the performance of the Hierarchical 
Fusion  Self-supervised  Learning  Framework  (HFSL),  this  study 
constructs a multi-dimensional evaluation metric system covering two 
dimensions: anomaly detection performance evaluation and model 
fitting capability evaluation.

5.3.1 Anomaly detection metrics

Evaluation  of  the  anomaly  detection  task  combines  confusion 
matrix-derived metrics and ranking quality metrics. First, based on 
the  confusion  matrix  of  prediction  results  versus  true  labels,  the 
following metrics are calculated:

Precision:  The  proportion  of  correctly  detected  anomalous 
samples  among  all  samples  detected  as  anomalous,  reflecting  the 
reliability of the model’s detection results.

Precision

=

TP
+
TP FP

Recall: The proportion of correctly detected anomalous samples 
among all true anomalous samples, reflecting the model’s capability to 
detect anomalies.

Recall

=

TP
+
TP FN

F1-score: The harmonic mean of precision and recall, balancing

consideration of detection accuracy and completeness.

F

1

=

×

2 Precision Recall

×

Precision Recall

+

Additionally, considering the special requirements of financial 
following  professional  metrics

the

anomaly  detection, 
are introduced:

False  Alarm  Rate  (FAR):  The  proportion  of  normal  samples 
incorrectly  classified  as  anomalous,  particularly  important  for 
financial regulation.

FAR

=

FP
+
FP TN

Miss Rate (MR): The proportion of anomalous samples that fail to

be detected, reflecting the risk of anomalies evading detection.

MR

=

FN
+
TP FN

Early Detection Rate (EDR): The proportion that can be detected 
in  the  early  stages  of  anomaly  occurrence  (within  the  first  two 
quarters), evaluating the model’s early warning capability.

EDR

=

TP
early
+
FN

TP

early

early

Industry-Specific Detection Rate (ISDR): Detection accuracy in 
specific  industries,  evaluating  the  model’s  adaptability  across 
different industries.

ISDR
i

=

TP
i
+
TP FN

i

i

where i represents a specific industry.
Beyond  confusion  matrix-derived  metrics,  ranking  quality 
evaluation metrics are adopted to assess the model’s ability to rank 
anomalous samples higher:

Area Under the Receiver Operating Characteristic Curve (AUC-
ROC): Evaluating the trade-off relationship between true positive rate 
and false positive rate at different thresholds.

Area  Under  the  Precision-Recall  Curve  (AUC-PR):  More 
reflective of model performance than the ROC curve in imbalanced 
scenarios with a low proportion of anomalous samples.

Mean Average Precision (MAP): Calculating the average precision

at different recall levels, evaluating overall ranking quality.

Figure  4  illustrates  the  comparison  between  the  HFSL 
framework and five baseline methods across six key performance 
metrics. The left chart shows each model’s performance on three 
fundamental metrics—precision, recall, and F1-score—with the 
HFSL framework outperforming all baseline methods, achieving 
an F1-score of 0.845, approximately 9.5% higher than the closest 
LSTM-AE. The right chart reflects comparisons on professional 
metrics, including AUC-ROC, early detection rate, and false alarm 
rate.  The  HFSL  framework  not  only  possesses  the  highest 
AUC-ROC value (0.894) and early detection rate (0.726), but its 
false  alarm  rate  (0.068)  is  also  significantly  lower  than  other 
methods, which is of great significance for financial risk control. 
This figure intuitively demonstrates the significant contribution 
of  hierarchical 
enhancing  anomaly 
detection performance.

fusion  design

to

Frontiers in Applied Mathematics and Statistics

13

frontiersin.org

---

<!-- PAGE 14 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 4
Anomaly detection performance comparison.

For evaluating detection performance across different anomaly 
types,  this  study  generated  radar  charts  of  various  models’ 
performance on four types of simulated anomalies and real anomalies, 
with detailed F1-score data provided in Table 1.

Figure  5  intuitively  displays  each  model’s  F1-score  performance 
across  five  types  of  anomalies  through  radar  charts.  Table  1  further 
provides  precise  performance  data  for  all  six  models  across  various 
anomaly types.

From  the  table,  it  can  be  observed  that  the  HFSL  framework 
achieves  optimal  results  across  all  anomaly  types,  particularly 
excelling  in  financial  indicator  mutation  anomalies  (0.892)  and 
financial ratio inconsistency anomalies (0.863), outperforming the 
second-best LSTM-AE model by 0.058 and 0.077 percentage points, 
respectively.  LSTM-AE  performs  relatively  close  to  HFSL  in 
accounting equation violation anomalies (0.802 vs. 0.841), while VAE 
also achieves a high F1-score of 0.792 for this anomaly type. Notably, 
all models generally perform relatively weakly in detecting temporal 
pattern  anomalies,  with  HFSL,  LSTM-AE,  and  VAE  achieving 
F1-scores  of  0.791,  0.713,  and  0.685,  respectively,  reflecting  the 
difficulty in identifying temporal pattern anomalies.

For real anomaly samples, all models show relatively lower 
performance,  with  HFSL  achieving  an  F1-score  of  0.798, 
approximately  6%  lower  than  its  average  performance  on 
simulated anomalies, reflecting the complexity and concealment 
of actual financial fraud. Traditional statistical methods such as 
Z-Score significantly underperform machine learning and deep 
learning methods across all anomaly types, particularly achieving 
only a 0.492 F1-score for temporal pattern anomalies. The overall 
distribution of model performance exhibits a consistent gradient, 
verifying the generalization capability of the hierarchical fusion 
self-supervised learning framework across different anomaly types.

Mean Squared Error (MSE): Measures the average of the squared 
the 
reconstructed

sequence  and

the

deviations  between 
original sequence.

MSE

=

N T D

1
× × ∑ ∑ ∑
N T D

= = =
1
1

1

t

i

j

(

x

i t j
, ,

−

ˆ
x

i t j
, ,

2

)

Mean Absolute Error (MAE): Measures the average of absolute

reconstruction errors, insensitive to outliers.

MAE

=

N T D

1
× × ∑ ∑ ∑ , ,
∣
x
N T D
= = =
1
1

1

t

i

j

i t j

−

ˆ
x

∣

i t j
, ,

Weighted  Mean  Squared  Error  (WMSE):  MSE  with  different

weights assigned according to financial indicator importance.

WMSE

=

N T D

1
× ∑ ∑ ∑
N T

= = =
1
1

1

t

i

j

(
w x
j

i t j
, ,

−

ˆ
x

i t j
, ,

2

)

where 
jw  represents the importance weight of indicator j.
Mean  Absolute  Percentage  Error  (MAPE):  The  average  of

relative errors.

MAPE

=

N T D

1
N T D

× × ∑ ∑ ∑ , ,

x
∣
= = =
1
1

i t j
x

1

t

i

j

−

ˆ
x

i t j
, ,

i t j
, ,

×
∣

100

%

Trend  Consistency  (TC):  Measures  the  consistency  degree  of

trend changes between reconstructed and original sequences.

5.3.2 Model fitting metrics

The  performance  of  a  self-supervised  learning  framework 
largely depends on its ability to fit normal data patterns. Therefore, 
this  study  employs  the  following  metrics  to  evaluate  model 
fitting quality:

TC

=

(
×
N T

N T

−
1

D

1
− × ∑ ∑ ∑
)
D
1

=
1

i

t

=
1

=
1

j

(

I

sgn

(

∆
x

i t j
, ,

)

=

sg

n

(

∆
ˆ
x

i t j
, ,

)

)

Frontiers in Applied Mathematics and Statistics

14

frontiersin.org

---

<!-- PAGE 15 -->

Zhang and Duan

10.3389/fams.2025.1628652

TABLE 1  F1-score performance comparison of different models across anomaly.

Model

HFSL

LSTM-AE

VAE

One-Class SVM

Isolation forest

Z-score

Financial 
indicator 
mutation

0.892

0.834

0.805

0.782

0.723

0.684

Financial ratio 
inconsistency

Temporal 
pattern

Accounting 
equation violation

Real anomalies

0.863

0.786

0.763

0.705

0.658

0.623

0.791

0.713

0.685

0.612

0.572

0.492

0.841

0.802

0.792

0.625

0.603

0.562

0.798

0.726

0.683

0.623

0.582

0.536

FIGURE 5
Anomaly type performance radar chart.

Frontiers in Applied Mathematics and Statistics

15

frontiersin.org

---

<!-- PAGE 16 -->

Zhang and Duan

10.3389/fams.2025.1628652

where  ( )·I

is an indicator function, 
=

∆
x

(
x∆  represents the sign 
sgn
x
+
j
1,

)
−

i t j
, ,

x

of the direction of change, and

i t j
, ,
Volatility Preservation Rate (VPR): Evaluates the model’s ability

i t
,

.

to preserve the volatility characteristics of the original data.

VPR

=

N D

1
× ∑ ∑
N D

(
σ
(
σ=
x
=
j
1
1

i

ˆ
x

i j
,

i i j
, ,

)
)

( )σ ·  represents standard deviation.

where 
Additionally, the following specific evaluation metric is introduced

for time series models:

Short-term Prediction Accuracy (SPA): Evaluates the accuracy of

the model’s prediction for the next time point.

SPA

= −
1

N D

1
N D

× ∑ ∑ ,

x
∣
=
1

=
1

i

j

i T

+

1,
x

−

ˆ
x

j

i T
,

+

1,

j
∣

i T
,

+

1,

j

x
where 
+,
i T
model’s predicted value.

1,

ˆi T
x
 represents the true value and 
+,
j

1,

represents the 
j

TABLE 2  HFSL framework performance metrics summary.

Indicator 
category

Indicator 
name

Performance 
value

Precision

Basic indicators

Recall

Advanced

indicators

Professional

indicators

F1-score

AUC-ROC

AUC-PR

Mean average

precision

(MAP)

Early detection

rate (EDR)

False alarm rate

(FAR)

Miss rate (MR)

95% 
confidence 
interval

[0.821, 0.851]

[0.789, 0.821]

[0.806, 0.834]

[0.871, 0.895]

[0.756, 0.788]

0.836

0.805

0.820

0.883

0.772

0.794

[0.781, 0.807]

0.726

[0.707, 0.745]

0.068

0.195

[0.062, 0.074]

[0.179, 0.211]

Based on this evaluation metric system, this study conducted a 
comprehensive assessment of the HFSL framework, testing not only 
its  accuracy  and  timeliness  in  anomaly  detection  but  also  its 
performance in data fitting. Experimental results show that the fitting 
errors of the HFSL framework on metrics such as MSE and MAPE are 
significantly lower than baseline methods, especially in terms of Trend 
Consistency (TC), reaching a high level of 0.826, demonstrating that 
the model can effectively capture the temporal change characteristics 
of financial data.

6 Results analysis

6.1 Performance comparison

6.1.1 Quantitative analysis

This study conducted a comprehensive evaluation of the HFSL 
framework on the test set constructed from the CSMAR database, 
with test results showing excellent performance in accounting data 
anomaly detection tasks. Table 2 summarizes the detailed performance 
of the HFSL framework on various key indicators.

As  shown  in  Table  2,  the  HFSL  framework  demonstrates 
balanced  performance  on  basic  indicators,  with  precision  and 
recall  reaching  0.836  and  0.805  respectively,  and  a  combined 
F1-score of 0.820, indicating the model achieves a good balance 
between  detection  accuracy  and  completeness.  In  terms  of 
advanced indicators, the AUC-ROC reaches 0.883, reflecting the 
model’s  strong  classification  ability  across  different  threshold 
settings; the AUC-PR is 0.772, particularly significant considering 
the scarcity of anomalous samples (approximately 9.6% of the test 
set). Among professional indicators, the early detection rate (EDR) 
is approximately 0.73, indicating the model can identify over 70% 
of  anomalous  cases  in  the  early  stages  (first  two  quarters), 
providing  ample  warning  time  for  risk  prevention  and  control; 
meanwhile, the false alarm rate is only 0.068, significantly reducing 
the regulatory costs associated with false positives.

Comparing detection performance across different anomaly 
types, variations in HFSL framework performance are observed 
(Figure 6), with best performance on financial indicator mutation 
anomalies (F1 = 0.892), followed by financial ratio inconsistency 
anomalies (F1 = 0.863), accounting equation violation anomalies 
(F1 = 0.841), temporal pattern anomalies (F1 = 0.791), and real 
anomaly  samples  (F1 = 0.798).  These  results  indicate  that  the 
model  has  higher  sensitivity  to  sudden  anomalies  and  static 
relationship violation anomalies, with relatively lower sensitivity 
to  temporal  pattern  anomalies  and  complex  real  anomalies, 
though overall performance remains at a high level.

Further  analysis  of  the  model’s  performance  across  different 
industries reveals industry-specific performance differences (Table 3). 
In  financial  industry  samples,  the  HFSL  framework  achieves  the 
highest  F1-score  (0.872),  possibly  due  to  the  strictly  regulated 
environment  and  standardized  financial  reporting  formats  in  the 
financial industry. Performance is relatively lower in the construction 
and real estate industry (F1 = 0.776), consistent with the industry-
specific  complexity  of  asset  valuation  and  diversity  in  revenue 
recognition. In manufacturing and information technology industries, 
model performance is at moderate levels (F1 scores of 0.817 and 0.831 
respectively),  reflecting  the  typical  anomaly  pattern  structures  of 
financial data in these industries.

Analysis  of  the  temporal  stability  of  the  model’s  detection 
performance reveals, as shown in Figure 7, that the HFSL framework 
exhibits significant temporal robustness during the 2016–2020 testing 
period, with F1 value variations across different quarters controlled 
within a narrow range of ±5%. This finding indicates that the model 
possesses strong temporal generalization characteristics, capable of 
adapting to financial data feature changes across different periods. 
Notably, a slight performance improvement is observed from the third 
quarter of 2018 to the second quarter of 2019, corresponding to the 
period when regulatory agencies strengthened financial supervision, 
leading to more pronounced anomaly patterns. In contrast, in early 
2020,  influenced  by  the  COVID-19  pandemic,  the  model’s 
performance  experienced  a  temporary  decline,  possibly  due  to

Frontiers in Applied Mathematics and Statistics

16

frontiersin.org

---

<!-- PAGE 17 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 6
Detection performance across different anomaly types.

TABLE 3  HFSL framework detection performance across industries.

Industry

Finance

Information technology

Manufacturing

Energy & utilities

Consumer goods

Healthcare

Construction & real estate

All industries average

Sample Size

Precision

Recall

F1-score

AUC-ROC

673

927

1,583

493

716

312

394

5,098

0.889

0.842

0.824

0.851

0.835

0.862

0.798

0.936

0.856

0.821

0.810

0.792

0.807

0.813

0.756

0.805

0.872

0.831

0.817

0.820

0.821

0.837

0.776

0.820

0.914

0.879

0.868

0.885

0.876

0.891

0.833

0.883

differences between pandemic-induced abnormal financial patterns 
and historical patterns.

6.1.2 Comparison with traditional methods

To  assess  the  advantages  of  the  HFSL  framework  relative  to 
existing methods, this study established four comparison experiment 
groups, representing different types of anomaly detection methods. 
Table 4 and Figure 8 present detailed comparison results of various 
methods on key performance metrics.

The  experimental  results  demonstrate  a  clear  performance 
gradient among different types of anomaly detection methods. The 
HFSL framework further enhances performance on this foundation, 
with an F1-score approximately 7% higher than the best deep learning 
method  (LSTM-AE),  about  15%  higher  than  machine  learning 
methods (Isolation Forest), and even more significantly improved 
compared to traditional statistical methods (Z-score), verifying the 
substantial advantages of the proposed method (Table 5).

Traditional  statistical  methods  such  as  Z-score  and  improved 
Benford analysis, while simple to implement, perform significantly 
worse than other methods, with F1-scores of only about 0.6, mainly 
due to their inability to effectively capture the temporal dependencies 
and multivariate interaction patterns of financial data. Particularly in 
terms of early detection rate, traditional methods achieve only about 
0.43, lacking sensitivity to early anomaly signals, severely limiting 
their application value in practical supervision. Traditional machine 
learning methods such as One-Class SVM and Isolation Forest, by 
learning data distribution characteristics, show marked improvements 
in precision and false alarm rates compared to statistical methods, but 
still have significant deficiencies in recall, indicating limitations in 
processing high-dimensional, temporal financial data.

Deep  learning  methods  such  as  LSTM-AE  and  VAE,  through 
complex  neural  network  structures,  can  better  capture  nonlinear 
features and temporal patterns of financial data, achieving F1-scores 
of  about  0.75,  approximately  6%  higher  than  machine  learning

Frontiers in Applied Mathematics and Statistics

17

frontiersin.org

---

<!-- PAGE 18 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 7
Time series performance analysis (2016–2020).

TABLE 4  Performance comparison of different anomaly detection methods.

Method 
Category

Method Name

Precision

Recall

F1-score

AUC-ROC

Early 
Detection 
Rate

False 
Alarm 
Rate

Traditional statistical

methods

Z-score

Improved Benford

Analysis

Machine learning

One-Class SVM

methods

Deep learning

methods

Self-supervised

variants

Complete method

Isolation Forest

LSTM-AE

VAE

HFSL (Reconstruction

Only)

HFSL (Prediction

Only)

HFSL

Bold values indicate the best performance for each metric.

0.629

0.643

0.722

0.736

0.795

0.772

0.801

0.788

0.836

0.581

0.563

0.663

0.682

0.734

0.727

0.759

0.774

0.805

0.604

0.600

0.691

0.708

0.763

0.749

0.779

0.781

0.820

0.672

0.684

0.724

0.753

0.832

0.821

0.848

0.853

0.883

0.435

0.422

0.504

0.522

0.631

0.617

0.673

0.691

0.726

0.146

0.132

0.107

0.103

0.080

0.089

0.079

0.085

0.068

methods. Particularly in early detection rate, the improvement exceeds 
20%, demonstrating the advantages of deep learning in early warning 
capability. This performance enhancement mainly stems from deep 
learning models’ ability to automatically learn hierarchical feature 
representations  from  financial  data  without  requiring  manually 
designed  complex  feature  engineering.  However,  traditional  deep 
learning methods still rely on large amounts of labeled data, which 
presents  a  significant  challenge 
the  field  of  financial 
anomaly detection.

in

Introducing self-supervised learning strategies on the foundation 
of  deep  learning  significantly  enhances  model  performance.  Even 
using  reconstruction,  prediction,  or  contrastive  learning  tasks 
individually  yields  performance  gains.  Among  the  three  self-
supervised  strategies,  contrastive  learning  tasks  perform  best

(F1 = 0.789), indicating that learning relationships between samples 
is  crucial  for  anomaly  detection  in  accounting  data.  This  may 
be because financial anomalies often manifest as degrees of deviation 
from  normal  samples,  and  contrastive  learning  precisely  captures 
these relationship differences. By integrating the three self-supervised 
learning tasks, the HFSL framework further improves performance 
(F1 = 0.820), validating the effectiveness of multi-task fusion. This 
performance enhancement stems from different self-supervised tasks’ 
ability  to  capture  complementary  data  features,  forming  more 
comprehensive data representations.

In terms of the critical early detection rate, the HFSL framework 
(approximately  0.73)  outperforms  the  closest  baseline  method 
LSTM-AE (approximately 0.63) by about 15%, providing regulatory 
agencies with a valuable early warning time window and significantly

Frontiers in Applied Mathematics and Statistics

18

frontiersin.org

---

<!-- PAGE 19 -->

Zhang and Duan

10.3389/fams.2025.1628652

FIGURE 8
F1-score and AUC-ROC comparison of different methods.

TABLE 5  Financial statement fraud pattern classification and characteristics.

Proportion (%)

Detection rate (%)

Representative anomaly 
example

Fraud pattern

Key financial 
indicator anomaly 
features

ROE↑, ROA↑, Accounts

Revenue inflation

Receivable Turnover↓, OCF/

38.6

Expense concealment

Asset overvaluation

Sales Ratio↓

Gross Profit Margin↑, Net

Profit Margin↑, Period

Expense Ratio↓, Abnormal

compared to industry peers

Asset Impairment↓, Fixed

Asset Turnover↓, Inventory

Turnover↓

Leverage Ratio↓, Current

Liability understatement

Ratio↑, Accounts Payable

Turnover↑

Multiple indicators

anomalous simultaneously,

21.7

17.4

15.2

Composite manipulation

Inconsistent internal

7.1

relationships between

financial ratios

87.3

84.5

Company A: Fictitious customer

orders

Company B: Capitalized R&D

expenditures

79.8

Company C: Inventory overvaluation

82.1

68.2

Company D: Contingent liabilities

not accrued

Company E: Simultaneous revenue

inflation and liability concealment

enhancing  early  intervention  capabilities  for  financial  risks. 
Simultaneously, HFSL’s false alarm rate (0.068) is significantly lower 
than other methods, reducing unnecessary investigation costs. This 
dual improvement gives HFSL higher practical value in real-world 
applications,  providing  effective  early  warnings  at  the  onset  of 
anomalies  while  keeping  false  alarms  within  an  acceptable  range. 
Analysis of performance differences between methods through the 
Wilcoxon signed-rank test shows that the performance differences

between the HFSL framework and all baseline methods are statistically 
significant (p < 0.01), confirming that the effectiveness of the proposed 
method is not due to random factors.

Comprehensive analysis indicates that the HFSL framework, by 
integrating  temporal  contrastive  learning,  dual-channel  LSTM 
structure, and domain knowledge constraints, significantly enhances 
the  comprehensive  performance  of  accounting  data  anomaly 
detection, achieving combined advantages particularly in detection

Frontiers in Applied Mathematics and Statistics

19

frontiersin.org

---

<!-- PAGE 20 -->

Zhang and Duan

10.3389/fams.2025.1628652

accuracy (F1-score), early warning capability (EDR), and false alarm 
control  (FAR).  Performance  improvements  stem  both  from  self-
supervised learning paradigm’s effective utilization of unlabeled data 
and from the multi-level fusion architecture’s targeted modeling of 
multi-scale characteristics in accounting data. These results suggest 
that  the  proposed  hierarchical  fusion  self-supervised  learning 
framework demonstrates promising application potential in the tested 
accounting data anomaly detection tasks.

6.2 Financial feature contribution analysis

This section delves into the contribution degrees and interaction 
effects of various financial features in the HFSL framework’s anomaly 
detection results, using SHAP (SHapley Additive exPlanations) value 
analysis and feature interaction effect quantification methods to reveal 
the  internal  logic  of  the  model’s  decision  mechanism,  providing 
interpretability  support  for  financial  anomaly  detection.  Through 
systematic analysis of financial feature importance rankings and their 
interaction  patterns,  not  only  can  the  model’s  effectiveness 
be  validated,  but  theoretical  foundations  can  also  be  provided  for 
identifying accounting data anomaly patterns.

6.2.1 Importance ranking of key financial 
indicators

probability,  with  the  calculation  process  considering  contribution 
variations of features under different combinations, thereby providing 
relatively objective feature importance evaluations.

Figure  9  displays  the  SHAP  value  ranking  of  the  10  financial 
indicators with the highest contributions to anomaly detection. The 
analysis reveals that profitability indicators play a critical role in the 
anomaly detection process. Particularly noteworthy is that the average 
|SHAP| values of two core indicators—Return on Equity (ROE) and 
Return  on  Assets  (ROA)—reach  as  high  as  0.196  and  0.179 
respectively, significantly exceeding the contribution levels of other 
financial  indicators.  This  result  aligns  with  financial  theory,  as 
profitability indicators are often the primary targets of financial fraud, 
with companies typically manipulating revenue and profit to embellish 
financial statements. ROE, as a core indicator for investors evaluating 
enterprise  value,  often  signals  early  financial  problems  when 
exhibiting abnormal fluctuations.

Current  Ratio  and  Leverage  Ratio,  two  indicators  reflecting 
solvency capability, rank third and fourth, with |SHAP| values of 0.163 
and  0.149,  respectively.  This  indicates  that  abnormalities  in  a 
company’s short-term and long-term debt repayment capabilities are 
also  important  indicators  of  financial  anomalies.  Notably,  the 
Operating Cash Flow Ratio (OCF Ratio) ranks fifth (|SHAP| value of 
0.139), verifying that inconsistencies between cash flow indicators and 
accrual profit indicators provide an effective approach for identifying 
potential financial anomalies.

To quantitatively assess the impact of various financial indicators 
on anomaly detection results, this study calculated SHAP values for 
22  core  financial  indicators  based  on  the  test  set.  SHAP  values, 
through the concept of Shapley values in game theory, measure each 
feature’s  marginal  contribution  to  the  model’s  predicted  anomaly

Efficiency indicators such as Accounts Receivable Turnover Rate 
and Total Asset Turnover Rate also enter the top ten, with |SHAP| 
values  of  0.119  and  0.109  respectively,  indicating  that  operational 
efficiency  indicators  hold  significant  value  in  capturing  abnormal 
financial behaviors. From an industry perspective, the importance of

FIGURE 9
SHAP value analysis of financial indicators.

Frontiers in Applied Mathematics and Statistics

20

frontiersin.org

---

<!-- PAGE 21 -->

Zhang and Duan

10.3389/fams.2025.1628652

the Leverage Ratio in the financial industry is significantly higher than 
in other industries (|SHAP| value increased by approximately 28%), 
while the Inventory Turnover Rate ranks relatively high in importance 
in  manufacturing  (entering  the  top  8),  reflecting  the  influence  of 
industry characteristics on the importance of anomaly features.

6.2.2 Multi-dimensional feature interaction effect 
analysis

Complex interdependencies exist between financial indicators, 
where anomalies in a single indicator may be masked by normal 
values in other related indicators. Therefore, analyzing interaction 
effects  between  features  is  crucial  for  enhancing  anomaly 
detection accuracy. This study employs a method based on SHAP 
interaction  values  to  quantitatively  evaluate  the  interaction 
intensity  between  feature  pairs  and  their  impact  on  anomaly 
detection results.

Figure  10  displays  a  heat  map  of  interaction  effect  intensities 
between  core  financial  indicators,  with  darker  areas  indicating 
stronger  interaction  effects  and  lighter  areas  indicating  weaker 
interaction  effects.  Through  quantitative  analysis  of  interaction 
patterns,  this  study  identifies  three  typical  financial  indicator 
interaction modes: enhancing interactions, neutralizing interactions, 
and nonlinear interactions.

Enhancing interactions manifest when the contribution of two 
indicators acting jointly to anomaly detection is significantly higher 
than the sum of their independent actions. The interaction intensity

between  ROE  and  ROA  reaches  0.087,  ranking  first  among  all 
indicator  pairs,  indicating  that  these  two  profitability  indicators 
provide  strong  financial  fraud  signals  when  simultaneously 
anomalous. Similarly, the interaction intensity between Current Ratio 
and Leverage Ratio is 0.082, reflecting the synergistic effect of short-
term and long-term solvency indicators. Such enhancing interactions 
primarily  occur  between  indicators  with  similar  functions  but 
different calculation bases, and when enterprises exhibit simultaneous 
anomalies across multiple related indicators, it typically implies higher 
financial risk.

Neutralizing  interactions  manifest  when  anomalies  in  one 
indicator are masked by changes in another indicator, reducing the 
sensitivity of anomaly detection. For example, the interaction effect 
between Leverage Ratio and Total Asset Turnover Rate is relatively 
weak (0.017), possibly because increases in Leverage Ratio due to 
increased debt may be accompanied by corresponding decreases in 
Total Asset Turnover Rate, thus reducing the model’s sensitivity to 
changes  in  single  indicators.  Such  interactions  suggest  that  when 
designing  anomaly  detection  models,  overreliance  on  changes  in 
single-dimension indicators should be avoided.

Nonlinear

interactions  manifest  as  complex  conditional 
dependency  relationships  between  indicators.  The  interaction 
intensity between Accounts Receivable Turnover Rate and Total Asset 
Turnover  Rate  reaches  as  high  as  0.084,  a  strong  interaction 
relationship that is not intuitive, as while they both belong to efficiency 
indicators, they measure different business links. In-depth analysis

FIGURE 10
Heat map of financial indicator interaction effects.

Frontiers in Applied Mathematics and Statistics

21

frontiersin.org

---

<!-- PAGE 22 -->

Zhang and Duan

10.3389/fams.2025.1628652

reveals  that  this  strong  interactivity  stems  from  their  conditional 
dependency  relationship  in  anomaly  detection:  when  Accounts 
Receivable  Turnover  Rate  abnormally  decreases  while  Total  Asset 
Turnover  Rate  abnormally  increases,  it  often  suggests  that  the 
enterprise  may  be  engaging  in  financial  fraud  behaviors  such  as 
fictitious sales or premature revenue recognition.

By constructing an interaction network graph to analyze the 
overall interaction structure, it is found that the financial indicator 
interaction network exhibits a “core-periphery” structure, where 
ROE,  ROA,  Current  Ratio,  and  Leverage  Ratio  form  a  highly 
interconnected  core  cluster,  while  other  indicators  display 
relatively dispersed connection patterns. This network structure 
suggests  that  anomaly  detection  should  focus  on  collaborative 
changes within the core indicator cluster while also considering 
abnormal connection patterns between peripheral indicators and 
core indicators.

Based  on  interaction  effect  analysis,  this  study  proposes  an 
adaptive  threshold  adjustment  mechanism  based  on  feature 
interaction intensity:

θ

adj

(

X

i

)

=

θ

base

(

X

i

)



× +
1



∑
≠
j
i

ω
,
i j

×

(
I X
|

j

−

>
µ θ
|

j

base

(

X

j

)

)






θadj

(

)

where 
)
(

iX   is  the  adjusted  threshold  for  feature

iX , 
iX   is  the  base  threshold, ω,i j   is  the  interaction  weight 
θbase
between feature values i and  j , and  ( )·I
 is an indicator function 
taking the value 1 when feature  j exceeds its base threshold and 0 
otherwise.  This  mechanism  enables  the  model  to  dynamically 
adjust detection thresholds according to the degree of collaborative 
anomalies across multiple indicators, increasing F1-score by 3.5% 
and reducing false alarm rate by 12.7% in experimental validation, 
verifying  the  important  value  of  feature  interaction  analysis  in 
enhancing anomaly detection performance.

Feature interaction effect analysis not only enhances model 
interpretability  but  also  provides  theoretical  foundations  for 
constructing more precise financial anomaly detection systems. 
The  research  finds  that  anomaly  detection  models  considering 
feature interaction effects outperform models focusing solely on 
single  features  when  capturing  complex  financial  anomaly 
patterns,  especially  in  identifying  carefully  designed  financial 
fraud cases. This finding provides insights for refining accounting 
data  anomaly  detection  theory,  indicating  that  future  research 
should  place  greater  emphasis  on  collaborative  analysis  of 
multidimensional financial indicators rather than simple single-
indicator threshold monitoring.

From the perspective of industry differences, the interaction 
intensity between ROE and ROA in the financial industry (0.096) 
is significantly higher than in manufacturing (0.081), while the 
interaction intensity between Inventory Turnover Rate and Gross 
Profit Margin in manufacturing (0.074) is higher than in other 
industries.  These  industry  characteristic  differences  further 
support  this  study’s  approach  of  constructing  industry-specific 
anomaly  detection  models,  adopting  differentiated  feature 
interaction patterns for anomaly identification tailored to different 
industry characteristics.

6.3 Identification and analysis of typical 
anomaly cases

6.3.1 Financial statement fraud pattern 
classification

Based on the detection results of the HFSL framework, combined 
with anomaly cases confirmed by manual audits, this study constructs 
a  systematic  classification  system  for  financial  statement  fraud 
patterns,  covering  five  typical  anomaly  modes:  revenue  inflation, 
expense concealment, asset overvaluation, liability understatement, 
and composite manipulation. Table 2 shows the key characteristics of 
each fraud pattern and their distribution in the detected samples.

Revenue inflation is the most common financial fraud pattern, 
accounting  for  38.6%,  with  typical  characteristics  including 
abnormally increased Return on Equity (ROE) and Return on Assets 
(ROA), simultaneously decreased Accounts Receivable Turnover Rate, 
and imbalanced Operating Cash Flow to Sales Revenue ratio. The 
HFSL framework achieves a detection rate of 87.3% for this type of 
anomaly,  outperforming  traditional  methods  by  approximately  23 
percentage points. Taking Company A as an example, its ROE growth 
rate exceeded the industry average by twofold for three consecutive 
quarters, while its Accounts Receivable Turnover Rate continued to 
decline, and its Operating Cash Flow to Net Profit ratio fell to 0.32 
(industry average: 0.78). The HFSL framework successfully detected 
this anomaly and raised the anomaly score to 0.87 (threshold: 0.65). 
Subsequent audits confirmed that the company inflated revenue by 
approximately  270  million  yuan  through  fictitious  overseas 
customer orders.

Expense  concealment  anomalies  account  for  21.7%,  primarily 
manifesting as abnormally increased gross profit margin and net profit 
margin, with period expense ratio significantly below industry average 
levels. This type of anomaly is typically achieved through improper 
expense capitalization, delayed cost recognition, and other means. In 
Company B’s case, the model captured its R&D expense capitalization 
rate surging to 83% (compared to a five-year average of 36%), while 
its  period  expense  ratio  was  12  percentage  points  below  industry 
peers, despite revenue growth rates similar to industry averages. This 
uncoordinated financial performance triggered the model’s multi-
dimensional anomaly scoring mechanism, successfully identifying 
potential financial manipulation behavior.

Asset  overvaluation  and  liability  understatement  anomalies 
account for 17.4 and 15.2%, respectively. Both types relate to improper 
valuation of balance sheet items but exhibit significant differences in 
financial indicator performance. Asset overvaluation primarily affects 
asset turnover indicators, as in Company C’s case, where inventory 
turnover rate remained in the bottom 10% of the industry for six 
consecutive quarters, while sales revenue growth was at mid-to-upper 
industry  levels.  This  mismatch  was  successfully  identified  by  the 
model  as  potential  inventory  value  overestimation.  Liability 
understatement primarily manifests as abnormally increased current 
ratio and abnormally decreased leverage ratio, as in Company D’s case, 
where contingent liabilities were not accrued according to regulations, 
causing its solvency indicators to significantly outperform industry 
average levels.

The most complex composite manipulation anomalies, though 
accounting for only 7.1%, present the greatest detection difficulty, with 
an  average  detection  rate  of  merely  68.2%.  This  type  of  anomaly

Frontiers in Applied Mathematics and Statistics

22

frontiersin.org

---

<!-- PAGE 23 -->

Zhang and Duan

10.3389/fams.2025.1628652

simultaneously involves manipulation of multiple financial statement 
items, as in Company E’s case, where revenue inflation and liability 
understatement coexisted. Although the anomaly degree of individual 
indicators  was  relatively  small,  the  relationships  between  multiple 
indicators violated financial logical consistency. The HFSL framework 
achieved effective identification of such complex anomalies through 
feature  interaction  mechanisms  and  financial  domain  knowledge 
constraints, which traditional single-indicator monitoring methods 
struggle to accomplish.

The  research  also  found  that  different  industries  exhibit 
preferences for different fraud patterns. Manufacturing shows a higher 
proportion  of  asset  overvaluation  anomalies  (26.3%),  primarily 
concentrated  in  inventory  and  fixed  asset  valuation  areas;  the 
information  technology  industry  predominantly  features  revenue 
inflation (52.1%), reflecting the complexity of revenue recognition in 
this industry; while the financial industry shows more prominent 
liability understatement (25.7%), involving risk provision accrual and 
financial asset valuation issues. This industry differentiation further 
confirms the necessity of the industry calibration mechanism in the 
HFSL  framework,  which  enables  more  accurate  identification  of 
considering 
industry-specific 
industry characteristics.

anomaly

patterns

by

6.3.2 Temporal evolution characteristics of 
anomaly detection

Financial anomalies typically exhibit progressive characteristics 
rather  than  sudden  events.  Through  temporal  analysis,  this  study 
identifies three typical evolution patterns. Progressive deterioration is 
the  most  common  pattern,  accounting  for  approximately  64%, 
characterized  by  gradually  increasing  anomaly  severity  over  time, 
typically  beginning  with  small-scale  financial  manipulation  that 
subsequently accumulates and expands. A typical case is Company F, 
whose anomaly score gradually rose from 0.42 to 0.97 over 8 quarters 
before its financial problems became public, with the HFSL framework 
successfully providing warnings an average of 4 quarters before the 
anomaly became public. Sudden anomalies account for approximately 
22%, characterized by rapidly escalating anomaly scores over a short 
period, typically related to major accounting errors, as in Company 
G’s case, where the anomaly score surged from 0.38 to 0.83 within one 
quarter. Although such anomalies are difficult to predict in advance, 
the HFSL framework controlled identification delay to an average of 
1.2 quarters, significantly outperforming traditional methods. Cyclical 
fluctuations account for approximately 15%, characterized by anomaly 
scores fluctuating around threshold edges, common in enterprises 
with  seasonal  businesses,  with  the  HFSL  framework  effectively 
controlling the false alarm rate for such anomalies to 8.7% through its 
seasonal adjustment mechanism.

Based  on  anomaly  temporal  characteristics  and  intensity,  this 
study constructs a risk grading model, categorizing anomaly cases into 
high-risk,  medium-risk,  and  observation  classes.  High-risk  cases 
exhibit anomaly scores consistently exceeding thresholds with upward 
trends, or sudden anomaly intensity exceeding thresholds by over 
30%, with approximately 83% experiencing major negative events 
within the subsequent 3 quarters. Medium-risk cases have anomaly 
scores slightly exceeding thresholds or fluctuating around threshold 
edges, with approximately 48% experiencing negative events within 
the  subsequent  6  quarters.  Observation-class  cases  have  anomaly 
scores below thresholds but continuously rising, or exhibiting isolated

anomalies,  with  approximately  27%  experiencing  negative  events 
within the subsequent 8 quarters. The HFSL framework improves 
high-risk  case  identification  accuracy  by  18.6%  compared  to 
traditional methods, with early identification of medium-risk cases 
advancing  by  an  average  of  1.7  quarters,  significantly  enhancing 
warning value.

The HFSL framework demonstrates differentiated detection 
timeliness  for  different  types  of  anomalies,  detecting  revenue 
inflation anomalies an average of 3.2 quarters in advance, expense 
concealment  2.8  quarters  in  advance,  asset  overvaluation  and 
liability understatement 2.4 and 2.6 quarters respectively, while 
composite  manipulation  only  1.8  quarters,  reflecting  the 
complexity  and  concealment  of  the  latter.  Temporal  analysis 
reveals  a  potential  “financial  anomaly  waterfall  effect,”  with 
approximately  83%  of  major  financial  anomaly  cases  in  the 
research  sample  beginning  with  minor  anomalies  in  single 
indicators,  subsequently  spreading  to  related  indicators,  and 
ultimately  forming  systemic  risks.  This  finding  may  provide 
inspiration for improving regulatory practices: early identification 
and  intervention  in  initial  anomaly  signals  may  interrupt  the 
chain reaction of financial anomalies, preventing the formation of 
difficult-to-reverse  systemic  problems.  By  capturing  early 
characteristics of anomaly diffusion patterns, the HFSL framework 
provides longer response windows and more reliable decision-
making bases for financial risk warnings.

6.4 Model robustness and generalization 
capability assessment

6.4.1 Cross-industry adaptability validation

The  HFSL  framework  demonstrates  differentiated  but  overall 
stable performance across different industries. Detection performance 
is best in the financial industry (F1 = 0.872), good in manufacturing 
and information technology industries (F1 scores of 0.817 and 0.831 
respectively), while relatively lower in the construction and real estate 
industry (F1 = 0.776). These differences primarily stem from industry-
specific financial characteristics and anomaly patterns. For example, 
the  strictly  regulated  environment  and  standardized  financial 
reporting formats in the financial industry facilitate anomaly pattern 
identification, while the complexity of asset valuation and diversity in 
revenue  recognition  in  the  construction  and  real  estate  industry 
increase detection difficulty.

Model  generalization  capability  is  evaluated  using  leave-one-
industry-out cross-validation, training with data from 9 industries and 
testing on the remaining industry. Results show that performance 
decline  after  industry  calibration  is  controlled  within  7.5%, 
significantly outperforming baseline methods’ 12.3%. Particularly in 
cross-industry  early  detection  rate,  the 
industry  calibration 
mechanism  improves  performance  by  14.6%,  confirming  the 
effectiveness of the hierarchical feature fusion design in capturing 
anomaly characteristics across different industries.

6.4.2 Noise sensitivity and threshold dynamic 
adjustment effects

To test model stability in noisy environments, this study designs 
three-level noise interference experiments, introducing 5, 10, and 15% 
random noise into the original data. Experimental results show that

Frontiers in Applied Mathematics and Statistics

23

frontiersin.org

---

<!-- PAGE 24 -->

Zhang and Duan

10.3389/fams.2025.1628652

the HFSL framework’s performance decreases by only 1.2% at the 5% 
noise  level  and  by  9.7%  in  the  15%  high-noise  environment, 
significantly  outperforming  the  best  baseline  method’s  18.3%, 
indicating  that  the  hierarchical  fusion  structure  possesses  strong 
resistance to data noise.

Data availability statement

The original contributions presented in the study are included in 
the article/supplementary material, further inquiries can be directed 
to the corresponding author.

Regarding threshold adjustment, this study compares the effects 
of fixed thresholds versus adaptive dynamic thresholds. The dynamic 
threshold  mechanism  demonstrates  superiority  across  different 
industries and periods, improving F1-score by an average of 3.5%, and 
particularly  reducing  false  alarm  rates  by  12.7%  on  test  sets  with 
imbalanced  anomaly  proportions.  This  result  validates  the 
effectiveness of the adaptive threshold method based on Gaussian 
mixture  models  in  processing  financial  data  anomaly  detection, 
providing 
in 
reliable 
practical applications.

threshold

guidance

selection

for

6.4.3 Temporal stability and concept drift analysis
Financial  fraud  patterns  evolve  continuously  in  response  to 
regulatory changes and technological advancements. Our temporal 
stability analysis reveals that the HFSL framework maintains robust 
performance despite these evolving patterns. When tested on quarterly 
segments  spanning  2016–2020,  the  framework  demonstrated 
remarkable stability with F1-score variations contained within ±5% 
across different periods.

The framework’s resilience to concept drift was evaluated through 
three scenarios. In sudden drift scenarios simulating major regulatory 
changes, the HFSL framework detected 89% of pattern shifts within 
two  quarters  and  recovered  to  baseline  performance  levels  with 
minimal  degradation  (F1-score  maintained  above  0.78  during 
transitions). For gradual drift representing natural evolution of fraud 
techniques, performance degradation was limited to 6.2% over eight-
quarter periods. The dual-channel architecture proved particularly 
effective, with the long-term channel capturing evolving trends while 
the short-term channel maintained sensitivity to immediate anomalies.
Analysis of real-world pattern evolution revealed significant changes 
following  the  2018  regulatory  enhancements  in  China.  The  model 
successfully adapted to a 15% shift in the relative importance of cash flow 
versus accrual-based indicators in fraud detection. This adaptation was 
achieved through the framework’s dynamic feature weighting mechanism, 
which automatically adjusted based on recent detection patterns.

Compared  to  static  models,  the  HFSL  framework  with  drift 
adaptation showed an 11.3% improvement in average performance 
over  the  five-year  test  period.  The  incremental  learning  strategy 
effectively balanced stability with adaptability, preventing catastrophic 
forgetting while incorporating emerging fraud patterns. These results 
demonstrate  that  the  framework’s  adaptive  capabilities  make  it 
particularly  suitable  for  deployment 
in  dynamic  regulatory 
environments where fraud patterns continuously evolve.

Future research directions include: (1) extending the framework 
to  other  sectors  beyond  Chinese  listed  companies,  (2)  developing 
semi-supervised variants that can incorporate limited labeled data, 
and  (3)  exploring  real-time  anomaly  detection  capabilities  for 
continuous monitoring systems.

References

Author contributions

YZ:  Supervision,  Methodology,  Writing  –  review  &  editing, 
Conceptualization, Software, Writing – original draft, Visualization, 
Investigation, Project administration, Funding acquisition, Validation, 
Data curation. BD: Validation, Software, Writing – review & editing, 
Supervision,  Resources,  Formal  analysis,  Funding  acquisition, 
Writing – original draft.

Funding

The author(s) declare that financial support was received for the 
research and/or publication of this article. Research on the problems 
and  countermeasures  of  environmental  accounting  information 
disclosure of listed companies from the perspective of low-carbon 
economy (WLYB202315).

Conflict of interest

BD was employed by Chengdu Huawei Technologies Co., Ltd.
The remaining author declares that the research was conducted in 
the absence of any commercial or financial relationships that could 
be construed as a potential conflict of interest.

Generative AI statement

The authors declare that no Gen AI was used in the creation of

this manuscript.

Any alternative text (alt text) provided alongside figures in this 
article has been generated by Frontiers with the support of artificial 
intelligence and reasonable efforts have been made to ensure accuracy, 
including review by the authors wherever possible. If you identify any 
issues, please contact us.

Publisher’s note

All  claims  expressed  in  this  article  are  solely  those  of  the 
authors and do not necessarily represent those of their affiliated 
organizations,  or  those  of  the  publisher,  the  editors  and  the 
reviewers. Any product that may be evaluated in this article, or 
claim that may be made by its manufacturer, is not guaranteed or 
endorsed by the publisher.

1. Ellili N, Nobanee H, Haddad A, Alodat AY, AlShalloudi M. Emerging trends in 
forensic accounting research: bridging research gaps and prioritizing new frontiers. J 
Econ Criminol. (2024) 4:100065. doi: 10.1016/j.jeconc.2024.100065

2. Xu  Y.  A  study  on  the  effectiveness  of  the  independent  director  system  on  the 
governance  of  financial  fraud  phenomenon:  taking  Kangmei  pharmaceutical  as  an 
example. SHS Web Conf. (2024) 188:01024. doi: 10.1051/shsconf/202418801024

Frontiers in Applied Mathematics and Statistics

24

frontiersin.org

---

<!-- PAGE 25 -->

Zhang and Duan

10.3389/fams.2025.1628652

3. Kaur  B,  Sood  K,  Grima  S.  A  systematic  review  on  forensic  accounting  and  its 
contribution towards fraud detection and prevention. J Financ Regul Compliance. (2023) 
31:60–95. doi: 10.1108/JFRC-02-2022-0015

19. Gui J, Chen T, Zhang J, Cao Q, Sun Z, Luo H, et al. A survey on self-supervised 
learning: algorithms, applications, and future trends. IEEE Trans Pattern Anal Mach 
Intell. (2024) 46:9052–71. doi: 10.1109/TPAMI.2024.3415112

4. Ramzan  S.  Comparison  of  financial  distress  prediction  models  using  financial 
variables. In Proceedings of the 2023 international conference on electrical, computer 
and energy technologies (ICECET). New York: IEEE, (2023); pp. 1–7.

20. Duan J., Zhao H., Zhou Q., Qiu M., Liu M. A study of pre-trained language models 
in  natural  language  processing.  In  Proceedings  of  the  2020  IEEE  international 
conference on smart cloud (SmartCloud). Cambridge: IEEE, (2020); pp. 116–121.

5. Rao  RK,  Mandhala  VN.  Unveiling  financial  fraud:  a  comprehensive  review  of 
machine learning and data mining techniques. Ingénierie des systèmes d information. 
(2024) 29:2309–34. doi: 10.18280/isi.290620

6. Chen H., Zhao Q., Lu W., Gu S., Jin W., Liu G., et al. Application of self-supervised 
autonomous  agent  framework  for  digital  transformation  of  elder  well  potentials 
discovery. In Proceedings of the ADIPEC. Berlin: SPE, (2024).

7. Shwartz Ziv R, LeCun Y. To compress or not to compress—self-supervised learning

and information theory: a review. Entropy. (2024) 26:252. doi: 10.3390/e26030252

8. Ali A, Abd Razak S, Othman SH, Eisa TAE, Al-Dhaqm A, Nasser M, et al. Financial 
fraud detection based on machine learning: a systematic literature review. Appl Sci. 
(2022) 12:9637. doi: 10.3390/app12199637

9.  Dechow  PM,  Ge  W,  Larson  CR,  Sloan  RG.  Predicting  material  accounting 
misstatements*. Contemp Account Res. (2011) 28:17–82. doi: 10.1111/j.1911-3846.2010.01041.x

10. Beneish  MD.  The  detection  of  earnings  manipulation.  Financ  Anal  J.  (1999)

55:24–36. doi: 10.2469/faj.v55.n5.2296

11. Kirkos E, Spathis C, Manolopoulos Y. Data mining techniques for the detection of fraudulent

financial statements. Expert Syst Appl. (2007) 32:995–1003. doi: 10.1016/j.eswa.2006.02.016

12. Perols J. Financial statement fraud detection: an analysis of statistical and machine

learning algorithms. Audit J Pract Theory. (2011) 30:19–50. doi: 10.2308/ajpt-50009

13. Cecchini  M,  Aytug  H,  Koehler  GJ,  Pathak  P.  Detecting  management  fraud  in

public companies. Manag Sci. (2010) 56:1146–60. doi: 10.1287/mnsc.1100.1174

14. Bao Y, Ke B, Li B, Yu YJ, Zhang J. Detecting accounting fraud in publicly traded 
U.S. firms using a machine learning approach. J Account Res. (2020) 58:199–235. doi: 
10.1111/1475-679X.12292

15. Jing L, Tian Y. Self-supervised visual feature learning with deep neural networks: a survey.

IEEE Trans Pattern Anal Mach Intell. (2021) 43:4037–58. doi: 10.1109/TPAMI.2020.2992393

16. Jaiswal A, Babu AR, Zadeh MZ, Banerjee D, Makedon F. A survey on contrastive 
(2020)  9:2.  doi:  10.3390/

learning.  Technologies

(Basel).

self-supervised 
technologies9010002

17. Kumar  P,  Rawat  P,  Chauhan  S.  Contrastive  self-supervised  learning:  review, 
progress,  challenges  and  future  research  directions.  Int  J  Multimed  Inf  Retr.  (2022) 
11:461–88. doi: 10.1007/s13735-022-00245-6

18. Liu X, Zhang F, Hou Z, Mian L, Wang Z, Zhang J, et al. Self-supervised learning: 
generative  or  contrastive.  IEEE  Trans  Knowl  Data  Eng.  (2021)  35:857–76.  doi: 
10.1109/TKDE.2021.3090866

21. Kim H, Kim S, Min S, Lee B. Contrastive time-series anomaly detection. IEEE

Trans Knowl Data Eng. (2024) 36:5053–65. doi: 10.1109/TKDE.2023.3335317

22. Hojjati H, Ho TKK, Armanfard N. Self-supervised anomaly detection in computer 
vision  and  beyond:  a  survey  and  outlook.  Neural  Netw.  (2024)  172:106106.  doi: 
10.1016/j.neunet.2024.106106

23. Chen Y, Wu Z. Financial fraud detection of listed companies in China: a machine

learning approach. Sustainability. (2022) 15:105. doi: 10.3390/su15010105

24. Xiuguo W, Shengyong D. An analysis on financial statement fraud detection for 
Chinese listed companies using deep learning. IEEE Access. (2022) 10:22516–32. doi: 
10.1109/ACCESS.2022.3153478

25. Zhang K, Wen Q, Zhang C, Cai R, Jin M, Liu Y, et al. Self-supervised learning for 
time series analysis: taxonomy, Progress, and prospects. IEEE Trans Pattern Anal Mach 
Intell. (2024) 46:6775–94. doi: 10.1109/TPAMI.2024.3387317

26. Tipirneni S, Reddy CK. Self-supervised transformer for sparse and irregularly 
sampled  multivariate  clinical  time-series.  ACM  Trans  Knowl  Discov  Data.  (2022) 
16:1–17. doi: 10.1145/3516367

27. Yang X, Zhang Z, Cui R. Timeclr: a self-supervised contrastive learning framework 
for univariate time series representation. Knowl-Based Syst. (2022) 245:108606. doi: 
10.1016/j.knosys.2022.108606

28. Xu R, Yao D, Zhou M. Does the development of digital inclusive finance improve 
the enthusiasm and quality of corporate green technology innovation? J Innov Knowl. 
(2023) 8:100382. doi: 10.1016/j.jik.2023.100382

29. Yang  X.,  Juyang  AN,  Lin  G.  Local  government  debt  and  corporate  strategic

alliances: evidence from chinese listed companies. Berlin: Springer. (2025).

30. Li  Z,  Chen  B,  Lu  S,  Liao  G.  The  impact  of  financial  institutions’  cross-
shareholdings  on  risk-taking.  Int  Rev  Econ  Finance.  (2024)  92:1526–44.  doi: 
10.1016/j.iref.2024.02.080

31. Wang Q, Lee E, Wang K, Zhang X. The effect of government industrial policies on 
corporate  accounting  conservatism.  J  Account  Public  Policy.  (2022)  41:106960.  doi: 
10.1016/j.jaccpubpol.2022.106960

32. Zhang C, Li Z, Xu J, Luo Y. Accounting information quality, firm ownership and 
technology innovation: evidence from China. Int Rev Financ Anal. (2024) 93:103118. 
doi: 10.1016/j.irfa.2024.103118

33. Altman E. I. Financial ratios, discriminant analysis and the prediction of corporate

bankruptcy. J. Finance. (1968) 23:589–609.

Frontiers in Applied Mathematics and Statistics

25

frontiersin.org

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

TYPE Original Research
PUBLISHED 02 September 2025
DOI 10.3389/fams.2025.1628652
Accounting data anomaly
detection and prediction based
OPEN ACCESS
EDITED BY on self-supervised learning
Biswajit Sarkar,
Yonsei University, Republic of Korea
REVIEWED BY Yingying Zhang 1* and Bingbing Duan 2
Dragos Bozdog,
Stevens Institute of Technology, United States
1 Chengdu College of Arts and Sciences, School of Accounting, Chengdu, China, 2 Chengdu Huawei
Nooka Madhusudhana Reddy,
Technologies Co., Ltd., Chengdu, China
Rajeev Gandhi Memorial College of
Engineering and Technology, India
*CORRESPONDENCE This study proposes a Hierarchical Fusion Self-Supervised Learning (HFSL) framework
Yingying Zhang
to address the challenge of scarce labeled data in accounting anomaly detection,
zyy_cdcas@163.com
integrating domain knowledge with advanced deep learning techniques. Based
RECEIVED 14 May 2025
on financial data from Chinese listed companies in the CSMAR database spanning
ACCEPTED 18 August 2025
PUBLISHED 02 September 2025 2000–2020, this framework integrates temporal contrastive learning, a dual-channel
LSTM autoencoder structure, and financial domain knowledge to construct a
CITATION
Zhang Y and Duan B (2025) Accounting data three-tier cascaded detection system. Empirical research demonstrates that the
anomaly detection and prediction based on HFSL framework achieves a precision of 0.836, recall of 0.805, and F1 score of
self-supervised learning.
0.820 in accounting anomaly detection, significantly outperforming traditional
Front. Appl. Math. Stat. 11:1628652.
doi: 10.3389/fams.2025.1628652 methods. In terms of practical metrics, the framework attains an early detection
rate of 0.726 while maintaining a false alarm rate of just 0.068, providing technical
COPYRIGHT
© 2025 Zhang and Duan. This is an support for early risk warning. Financial feature contribution analysis reveals that
open-access article distributed under the
core indicators such as Return on Assets (ROA), Return on Equity (ROE), and their
terms of the Creative Commons Attribution
License (CC BY). The use, distribution or interaction effects play crucial roles in anomaly identification. Through analysis
reproduction in other forums is permitted, of 2,150 samples in the test set, the study identifies five typical financial fraud
provided the original author(s) and the
patterns (revenue inflation 38.6%, expense concealment 21.7%, asset overvaluation
copyright owner(s) are credited and that the
original publication in this journal is cited, in 17.4%, liability understatement 15.2%, and composite manipulation 7.1%) and their
accordance with accepted academic temporal evolution characteristics. The research also finds that financial anomalies
practice. No use, distribution or reproduction
typically exhibit three evolutionary patterns: progressive deterioration (64%), sudden
is permitted which does not comply with
these terms. anomalies (22%), or cyclical fluctuations (15%), providing empirical evidence for
regulatory practice. This study applies self-supervised learning to accounting anomaly
detection, not only solving the detection challenges in unlabeled data scenarios
but also providing effective tools for financial supervision and risk management.
KEYWORDS
accounting data, anomaly detection, financial fraud, hierarchical fusion framework,
self-supervised learning
1 Introduction
Accounting data, as the quantitative representation of enterprise economic activities, plays
a fundamental supporting role in investment decisions, resource allocation, and market
stability. However, frequent financial fraud incidents in global financial markets in recent years
have severely eroded market confidence and economic stability. Data from the U.S. Securities
and Exchange Commission (SEC) shows that financial fraud cases have increased by
approximately 30% in recent years (2020–2023), with amounts exceeding $270 billion (1). This
systemic risk not only affects individual enterprises but also threatens the entire capital market.
Iconic financial fraud cases such as Enron, WorldCom, and Lehman Brothers caused market
capitalization losses exceeding $300 billion, hundreds of thousands of employees losing their
jobs, and severe pension fund losses, triggering comprehensive doubts about accounting
information reliability.
Frontiers in Applied Mathematics and Statistics 01 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
In the Chinese market, recent financial fraud cases of listed bottlenecks of accounting data anomaly detection. The framework
companies such as Kangmei Pharmaceutical and Kangde Xin uses the financial data of Chinese listed companies in the CSMAR
similarly highlight the serious harm of financial information database as an empirical basis to construct a three-tier cascaded
distortion to investors and market order. Kangmei Pharmaceutical anomaly detection mechanism: feature representation learning
was fined 6 billion yuan for falsely increasing monetary funds by layer, relationship reasoning layer, and anomaly detection layer,
nearly 30 billion yuan, becoming the largest fine in the history of achieving high-precision identification and early warning of
China’s capital market (2). These cases reveal the limitations of accounting data anomalies through temporal contrastive learning,
traditional financial regulatory mechanisms when facing complex dual-channel LSTM autoencoder, and financial domain
and concealed accounting data manipulation. Despite global knowledge constraints.
regulatory bodies continuously strengthening financial reporting The innovative contributions of this research are mainly
regulatory frameworks, such as the Sarbanes-Oxley Act (SOX) and reflected in three aspects: first, a hierarchical fusion self-
International Financial Reporting Standards (IFRS), accounting supervised learning framework designed for accounting data
data anomaly detection still faces severe challenges: complex and characteristics, effectively solving detection problems in scenarios
variable anomaly patterns, severe scarcity of available labeled data, with scarce labeled data; second, a temporal contrastive learning
and insufficient detection tool effectiveness (3). mechanism incorporating financial domain knowledge, enhancing
Traditional accounting anomaly detection methods mainly the sensitivity and interpretability of anomaly recognition; third,
rely on two technical approaches: rule-based statistical analysis, revealing the “financial anomaly waterfall effect” through
such as modified Z-score and Beneish M-score models, and multidimensional financial feature interaction analysis, providing
supervised learning methods, such as support vector machines theoretical basis for regulatory practice.
and random forests. However, these methods generally have three
key limitations: (1) dependence on large amounts of high-quality
2 Literature review
labeled data, while accounting fraud cases are rare events with
costly labeled data acquisition; (2) static anomaly pattern
2.1 Traditional accounting data anomaly
assumptions, making it difficult to adapt to the dynamic evolution
detection methods
of financial fraud techniques; and (3) insufficient modeling
capability for complex interactions between multidimensional
financial indicators, resulting in low detection rates for carefully Traditional accounting data anomaly detection methods
designed financial manipulation behaviors (4, 5). primarily include statistical analysis, rule-based systems, and
With the deepening of digital transformation, enterprise supervised learning algorithms. Statistical methods identify
financial data exhibits characteristics of large volume, complex anomalies by quantifying the deviation degree of financial
dimensions, temporal dependence, and industry heterogeneity, indicators, where the Z-score method assesses corporate bankruptcy
urgently requiring innovative technical frameworks to break risk by calculating standard deviations of financial ratios relative to
through the bottlenecks of traditional detection paradigms. Self- normal distribution (33). Similar modified Z-score methods have
supervised Learning, as a frontier paradigm in the field of deep further improved detection precision, but these methods typically
learning, automatically constructs supervision signals from assume data conforms to specific distributions. In practice,
unlabeled data and has demonstrated excellent performance in accounting data often exhibits non-normal distribution and
computer vision and natural language processing (6, 7). This heteroscedasticity characteristics, which may lead to higher false
method is particularly suitable for addressing key challenges in positive or false negative rates (9). Rule-based systems rely on
accounting data anomaly detection: no need for large amounts of predefined thresholds or logical conditions, such as determining
labeled data, ability to capture complex data patterns, and abnormality when current ratios exceed normal ranges (10).
adaptation to dynamically changing environments. However, Although such methods demonstrate certain effectiveness in
transferring self-supervised learning principles to the field of specific environments, they lack adaptability and struggle to process
accounting data anomaly detection faces numerous technical complex financial data patterns (11).
challenges, including how to construct self-supervised tasks Supervised learning algorithms have been widely applied in
suitable for financial data characteristics, how to integrate domain anomaly detection in recent years, including technologies such as
knowledge constraints, and how to handle temporal dependencies support vector machines (SVM), random forests, and neural
and industry differences. networks (12). These methods learn classification boundaries to
Ali et al., through a systematic literature review, found that identify potential anomalies by training on labeled normal and
traditional machine learning methods have obvious limitations in abnormal samples. However, in the accounting data domain,
processing high-dimensional imbalanced financial data, while labeled anomalous samples (such as financial fraud) are scarce,
deep learning significantly improves fraud detection accuracy and the labeling process is easily influenced by subjective factors
through automatic feature extraction and nonlinear modeling (13). Furthermore, the performance of supervised learning
capabilities. However, most existing research still relies on models highly depends on the quality and quantity of training
supervised learning paradigms, and dependency on labeled data data, and their generalization capability often performs poorly
limits its practical application (8). across different industries or time periods of financial data (14).
Based on the above research background, this paper proposes Therefore, the limitations of traditional methods lie in their high
an innovative Hierarchical Fusion Self-supervised Learning dependency on labeled data, substantial detection costs, and
Framework (HFSL), aiming to break through the technical insufficient adaptability to dynamic data patterns.
Frontiers in Applied Mathematics and Statistics 02 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
2.2 Current applications of self-supervised 3 Self-supervised learning framework
learning design
3.1 Hierarchical fusion self-supervised
Self-supervised learning, as an emerging machine learning
learning framework
paradigm, generates supervision signals from unlabeled data and has
demonstrated significant application potential across multiple
domains (15). In computer vision, self-supervised methods such as The Hierarchical Fusion Self-supervised Learning Framework
rotation prediction and contrastive learning have achieved success by (HFSL) addresses the multi-source heterogeneity, temporal
learning semantic representations of images (16–19). In natural dependence, and industry differentiation characteristics of accounting
language processing, the BERT model has achieved deep data, breaking through the limitations of traditional anomaly
understanding of text through masked language modeling tasks (20). detection methods. Based on self-supervised learning principles, the
In recent years, applications of self-supervised learning in time HFSL framework integrates temporal modeling capabilities and
series anomaly detection have gradually gained attention. Autoencoder- domain knowledge constraints to form a three-tier cascaded anomaly
based methods mark points with large reconstruction errors as detection mechanism.
anomalies by reconstructing normal time series patterns. Contrastive The first layer of the HFSL framework is the feature representation
learning further enhances time series anomaly detection accuracy by learning layer, which enhances the model’s ability to recognize
maximizing representation consistency between similar samples (21). temporal patterns in accounting data through Temporal Contrastive
Despite significant progress in the aforementioned domains, Learning. Specifically, given an accounting data sequence
applications of self-supervised learning in accounting data anomaly X={ x1,x2,…,xT } , positive sample pairs ( xi,xj ) are constructed
detection remain in an exploratory stage. Accounting data possesses where∣ i−j∣≤δ represents temporally close samples; negative sample
multivariate panel structure and temporal dependencies, posing pairs ( xi,xj ) are constructed where∣ i−k∣>δ represents temporally
unique challenges to self-supervised learning model design. distant samples. Feature representations are optimized by minimizing
Compared to image or text data, accounting data anomaly patterns the following contrastive loss function:
are more concealed and strongly context-related, limiting the direct
application of existing self-supervised methods in this field. However, exp ( sim ( zi,zj ) /τ )
this characteristic also provides research opportunities for developing

con
=−log
∑exp ( sim ( zi,zk ) /τ)
self-supervised frameworks applicable to accounting data. k≠i
Contrastive learning-based methods have unique advantages in
capturing sequential anomalies in financial data, especially in the
( )
financial domain where unlabeled data predominates, self-supervised Where zi is the feature representation of xi, sim ·,· is the cosine
learning can effectively overcome the challenges of scarce labeled similarity function, and τ is a temperature parameter. This design
data. However, the research also indicates that industry differences in enables the model to capture temporal consistency in financial data,
financial data place higher demands on model generalization establishing a foundation for anomaly detection.
capabilities, and single-structure self-supervised models struggle to The second layer is the relationship reasoning layer, which
adapt to financial data characteristics across different industries (22). adopts a dual-channel LSTM autoencoder structure—one channel
processes short-term financial behaviors, while the other captures
long-term financial trends, with both types of information fused
2.3 Research gaps
through an attention mechanism. Formally, the short-term channel
learns function fs: d×w s → h, the long-term channel learns
Research on accounting data anomaly detection using the function fl: d×w l → h, where ws <wl represents different time
CSMAR database is currently limited. As an authoritative source window sizes. The final representation is fused through attention
of financial and market data for Chinese listed companies, the weights α:
CSMAR database provides rich multivariate panel data, making it
highly suitable for empirical analysis of anomaly detection. z=α·fs ( Xw
s
)+( 1−α) ·fl ( Xw
l
)
Existing research predominantly focuses on applications of
traditional statistical methods or supervised learning algorithms
(23, 24), with insufficient exploration of self-supervised learning This dual-channel design overcomes the limitations of traditional
potential in this dataset. Traditional methods often struggle to LSTM in multi-scale temporal pattern recognition, making it more
effectively capture cross-company and cross-temporal anomaly suitable for accounting data characterized by the coexistence of
patterns when processing CSMAR data, while supervised learning quarterly fluctuations and annual trends.
is constrained by scarce labeled data, making it difficult to fully The third layer is the anomaly detection layer, combining
exploit data features. reconstruction errors and financial domain knowledge to achieve
The effectiveness of self-supervised learning in multivariate panel multi-dimensional anomaly judgment. Beyond basic reconstruction
data has not been systematically verified. The complex structure of errors, financial rationality constraints are introduced, such as the
accounting data requires models to simultaneously process time series asset-liability equation Assets=Liabilities+Equity and revenue-
dependencies and interactions between variables, while existing self- cost relationship Profit=Revenue−Cost. The model learns not only
supervised methods are predominantly designed for univariate time data distribution but also financial rules, improving the
series or static data (25–27). interpretability and accuracy of anomaly detection. Anomaly score
Frontiers in Applied Mathematics and Statistics 03 frontiersin.org

| Zhang and Duan  |     |     |     |     |     | 10.3389/fams.2025.1628652 |     |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
calculation  integrates  reconstruction  error  and  rule  fluctuations and long-term trends; and finally, integrating domain
violation degree: knowledge constraints to improve the accuracy and interpretability of
|        |         |               | anomaly  detection.  |     | These  innovative  | designs  | make  | the  HFSL  |
| ------ | ------- | ------------- | -------------------- | --- | ------------------ | -------- | ----- | ---------- |
| Erecon | ( X )−µ | Erule ( X )−µ |                      |     |                    |          |       |            |
( )=λ· recon+( 1−λ) rule framework particularly suitable for practical accounting data anomaly
| Score X | ·     |       |                         |     |     |     |     |     |
| ------- | ----- | ----- | ----------------------- | --- | --- | --- | --- | --- |
|         | σ     | σ     | detection requirements. |     |     |     |     |     |
|         | recon | rule. |                         |     |     |     |     |     |
Figure 1 illustrates the overall architecture of the HFSL framework.
The framework takes accounting data from the CSMAR database as
where µ recon and σ recon are the mean and standard deviation of  input and preprocesses it through a three-stage adaptive processing
| reconstruction errors on the training set, and µ |     | rule and σ    |                                                                       |     |     |     |     |     |
| ------------------------------------------------ | --- | ------------- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                  |     | rule are the  | mechanism. The model centers on a three-tier cascaded structure: the  |     |     |     |     |     |
corresponding statistics for rule violation scores. This standardization  first layer captures temporal pattern features of financial data through
ensures that both components are on the same scale, allowing the  feature representation learning, the middle layer utilizes a dual-
balancing parameter λ to accurately reflect the intended weight allocation  channel LSTM structure to separately process short-term financial
between reconstruction-based and rule-based anomaly detection. fluctuations and long-term trends, while the final layer integrates
To provide a clearer understanding of the HFSL framework’s  multi-scale scoring mechanisms, adaptive thresholds, and financial
implementation, Algorithm 1 presents the pseudocode for the  rule constraints to form precise anomaly identification capabilities.
complete framework: This multi-level fusion architecture promises to better analyze cross-
The innovation of the HFSL framework is manifested in three  scale features and temporal series correlations in accounting data.
aspects: first, introducing temporal contrastive learning to enhance
sensitivity to temporal patterns in accounting data; second, designing
a dual-channel LSTM structure to simultaneously capture short-term
3.2 Adaptive processing mechanism for
accounting data
Input:
|     |     |     | Accounting  | data  | possesses  unique  | industry  |     | characteristics,  |
| --- | --- | --- | ----------- | ----- | ------------------ | --------- | --- | ----------------- |
Accounting data sequence X = {x₁, x₂, ..., xₜ}
|     |     |     | seasonal  fluctuations,  |     | and  imbalanced  | distributions,  |     | requiring  |
| --- | --- | --- | ------------------------ | --- | ---------------- | --------------- | --- | ---------- |
Output:  specialized adaptive processing mechanisms. This study designs a
Anomaly score and detection result  three-stage data adaptation process, including industry calibration,
seasonal adjustment, and noise suppression.
Parameters:
The industry calibration stage addresses the differences in
δ (temporal window), τ (temperature), λ (balance parameter)
financial indicators across industries by introducing industry reference
// Feature Representation Learning Layer distribution Pi ( x ) , which represents the probability distribution of
for each batch in X do  financial indicator x within industry i. The calibration process involves
a two-step transformation:
| Generate positive pairs (xᵢ, xⱼ) where |i − j| (cid:304) |     | δ   |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Generate negative pairs (xᵢ, xₖ) where |i − k| > δ
|     |     |     |     |     |    | (     | )2 |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     |     | 1   | x − µ |     |     |
C o mpute contrastive loss using Eq.(1)  Pi ( x )= exp  − i 
|     |     |     |     |     |       |     | 2  |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     |     | 2π σ 2 | 2 σ |     |     |
|     |     |     |     |     | i     | i   |    |     |
end f or
// Relationship Reasoning Layer
Split X into short-term Xₛ and long-term Xₗ windows   where µ i and σ i are the industry-specific mean and standard
|     |     |     | deviation.  | The  within-industry  | standardized  |     | transformation  | is  |
| --- | --- | --- | ----------- | --------------------- | ------------- | --- | --------------- | --- |
hₛ = LSTM_short(Xₛ)    // Extract short-term patterns
then applied:
hₗ = LSTM_long(Xₗ)     // Extract long-term patterns
(cid:162) = Attention(hₛ, hₗ)  // Compute attention weights   x−µ
|                                                    |     |     |     |     | x′= | i   |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| z = α · hₛ + (1 − α) · hₗ  // Fuse representations |     |     |     |     | σ   |     |     |     |
|                                                    |     |     |     |     | i   |     |     |     |
// Anomaly Detection Layer
E_recon = ComputeReconstructionError(X, X̂)
|     |     |     | This  transformation  |     | ensures  | that  financial  |     | indicators  are  |
| --- | --- | --- | --------------------- | --- | -------- | ---------------- | --- | ---------------- |
E_rule  = CheckFinancialRules(X)
normalized relative to their industry-specific distributions, enabling
Score   = λ · Normalize(E_recon) + (1 − λ) · Normalize(E_rule) the model to identify anomalies that deviate from industry norms
rather than from the overall market average.
if Score > θ_adaptive then
The seasonal adjustment stage employs the X-13 ARIMA-SEATS
return "Anomaly detected", Score
method to decompose financial indicators. This decomposition
| else                    |     |     |                                                            |     |     |     |     | ( )    |
| ----------------------- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | ------ |
|                         |     |     | follows an additive model where the observed time series x |     |     |     |     | t  is  |
| return "Normal", Score  |     |     | expressed as:                                              |     |     |     |     |        |
ALGORITHM 1
Hierarchical fusion self-supervised learning framework.
|     |     |     |     | x ( | t )=T ( t )+S ( | t )+R ( t | )   |     |
| --- | --- | --- | --- | --- | --------------- | --------- | --- | --- |

Frontiers in Applied Mathematics and Statistics 04 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
FIGURE 1
Architecture of the hierarchical fusion self-supervised learning framework (HFSL).
( ) ( )
Where T t represents the trend component, S t the seasonal identifiability. After extracting the trend and seasonal
( )
component, and R t the residual component. The trend component components, the residual component is obtained as:
( )
T t is extracted using a Henderson moving average filter, which
minimizes the variance of the third difference of the trend. For R
(
t
)=x (
t
)−T (
t
)−S (
t
)
quarterly data, we apply a 13-term Henderson filter:
6 ( )
T ( t )= ∑ wj·x ( t+j ) The residual component R t contains both irregular variations
and potential anomalies. To distinguish between normal irregular
j=−6
fluctuations and true anomalies, we apply a robust scale estimator
based on the median absolute deviation (MAD):
Where the weights wj are symmetric (wj =w−j) and sum to unity.
The seasonal component S ( t ) is modeled using a seasonal ARIMA MAD=median ( |R ( t )−median ( R ( t )) | )
specification. For quarterly financial data, we employ an ARIMA
(0,1,1) (0,1,1) model, which can be expressed as:
4
Financial indicators with residual values exceeding
( 1−B ) ( 1−B4 ) S ( t )=( 1−θ 1B ) ( 1−Θ 1B4 ) ∈ t ±3×1.4826×MAD are flagged as potential anomalies, where 1.4826 is
the consistency constant for normal distributions. This approach
effectively separates legitimate seasonal patterns, such as year-end
where B is the backshift operator, θ 1 and È1 are the inventory adjustments or quarterly revenue cycles, from suspicious
non-seasonal and seasonal moving average parameters deviations that may indicate financial manipulation.
respectively, and ò t is white noise. The seasonal factors are The noise suppression stage introduces an adaptive weighting
constrained to sum to zero over a complete year to ensure strategy that adjusts feature weights based on data reliability. For
Frontiers in Applied Mathematics and Statistics 05 frontiersin.org

| Zhang and Duan  |     |     |     |     |     |     |     | 10.3389/fams.2025.1628652 |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
high-noise features, their weights in anomaly calculations are reduced  The strongest correlation occurs between sequence anomalies and
to improve detection stability. This mechanism is particularly suitable  relationship anomalies (ρ sr =0.51), which is expected as violations in
for handling financial data of varying quality and completeness in the  financial relationships often manifest as abnormal temporal patterns.
CSMAR database. For instance, when the relationship between revenue and accounts
receivable is disrupted (relationship anomaly), it frequently leads to
unusual trends in subsequent periods (sequence anomaly). To account
3.3 Adaptive threshold determination and
for these interactions, we introduce a second-order adjustment term:
multi-scale anomaly scoring

|     |     |     |     |     | a d j u | sted( )=Scorefinal | ( )+λ ∑wiwj |     | ( ) ( ) |
| --- | --- | --- | --- | --- | ------- | ------------------ | ----------- | --- | ------- |
The key to anomaly detection lies in threshold determination. This  Score X X ρ ijScorei X Scorej X
|     |     |     |     |     | f i n a | l   | int |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
study proposes an adaptive dynamic threshold mechanism that  i<j
automatically adjusts thresholds based on data distribution and
business requirements. The basic approach is to fit reconstruction  Where λ =0.05 is the interaction coefficient determined
int
error distributions using Gaussian Mixture Models (GMM): through cross-validation. This adjustment captures the synergistic
effect when multiple anomaly types co-occur, improving detection
|     |     | K         | ( )       |     | accu r ac y |  f o r  co m p le x  fi | n a n c ia l  m a n i p u la | t io n s .                       |     |
| --- | --- | --------- | --------- | --- | ----------- | ----------------------- | ---------------------------- | -------------------------------- | --- |
|     |     | ( )=∑ π  | e∣µ k,σ 2 |     |             |                         |                              |                                  |     |
|     |     | p e k     | k         |     |             |                         |                              |                                  |     |
|     |     |           |           |     | F u rt      | h e r m o re ,  w e     | o b se r v e  t h a t   th   | e   p r e sence of relationship  |     |
|     |     | k=1       |           |     |             |                         |                              |                                  |     |
anomalies often serves as a catalyst that amplifies the significance of
point anomalies. This conditional dependency is modeled through a
| where e represents reconstruction error, and π |     |     |     | k, µ k, and σ | k  gating mechanism: |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ------------- | -------------------- | --- | --- | --- | --- |
represent the mixing coefficient, mean, and standard deviation of the
|     |     |     |     |     |     |     |  ( | )−θ  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
K Gaussian component, respectively. The threshold is set to a specific  ( )=σ Scorer X r
|                                          |     |     |     |     |     | g X |    |    |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| quantile of the high-variance component: |     |     |     |     |     |     |  τ |    |     |
|                                          |     |     |     |     |     |     |    |    |     |
θ=µ +ασ
|     |     | h   | h   |     |          |                                 |     |                                |     |
| --- | --- | --- | --- | --- | -------- | ------------------------------- | --- | ------------------------------ | --- |
|     |     |     |     |     | Where σ( | · )  is the sigmoid function, θ |     | r is the relationship anomaly  |     |
where µ h and σ h are the parameters of the high-variance  threshold, and τ=0.1 is a temperature parameter. The gated final
| component, and α is an adjustable coefficient that balances false  |     |     |     |     | score becomes: |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
positive and false negative rates according to business requirements.
|     |     |     |     |     |     | gated( | adjusted( | )×( | ))  |
| --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --- |
This study introduces a multi-scale anomaly scoring mechanism  Score X )=Score X 1+β·g ( X
|     |     |     |     |     |     | final | final |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
that comprehensively considers three levels: point anomalies, sequence
anomalies, and relationship anomalies. Point anomalies focus on
abnormal values at individual time points, sequence anomalies detect  Where β=0.15 represents the maximum amplification factor.
abnormal patterns in time series, and relationship anomalies identify  This  gating  mechanism  ensures  that  when  strong  relationship
abnormal changes in relationships between multiple variables. The  anomalies are present, the model increases its sensitivity to other
final anomaly score is a weighted combination of the three: anomaly types, reflecting the empirical observation that financial
fraud often involves multiple coordinated manipulations.
|     | ( )=wp·Scorep | ( )+ws·Scores | ( )+wr·Scorer | ( ) |     |     |     |     |     |
| --- | ------------- | ------------- | ------------- | --- | --- | --- | --- | --- | --- |
Scorefinal X X X X Through ablation studies, we demonstrate that incorporating

these interaction effects improves the overall F1-score by 4.2%
|     |     |     |     |     | compared  | to  treating  | the  components  | as  independent,  | with  |
| --- | --- | --- | --- | --- | --------- | ------------- | ---------------- | ----------------- | ----- |
where wp, ws,  and wr  are  weight  parameters.  While  this  particularly  notable  improvements  in  detecting  complex  fraud
formulation presents the final score as a linear combination, the three  patterns involving multiple financial statement items.
anomaly  components  are  not  statistically  independent.  Their  In summary, the innovative self-supervised learning framework
interdependencies arise from the inherent structure of financial data  HFSL proposed in this study is specifically designed for accounting
and manifest through several mechanisms. data characteristics, integrating temporal contrastive learning, dual-
The correlation structure among the three components can  channel LSTM structure, domain knowledge constraints, and multi-
be characterized by the correlation matrix: scale anomaly scoring mechanisms to provide a theoretical and
technical foundation for accounting data anomaly detection.
|     |     |  1 ρ | ρ  |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ps pr
|         |       |                 |                           |     |                        |              |              |     |     |
| ------- | ----- | ---------------- | -------------------------- | --- | ---------------------- | ------------ | ------------ | --- | --- |
|         |       | C=ρ 1           | ρ sr                      |     |                        |              |              |     |     |
|         |       | ps               |                            |     | 4  R e se              | a rc h  m    | e thods and  |     |     |
|         |       |                 |                           |     |                        |              |              |     |     |
|         |       |  ρ pr ρ sr      | 1                         |     |                        |              |              |     |     |
|         |       |                  |                            |     | im p le                | m e n ta tio | n            |     |     |
| Where ρ | =Corr | ( ( )            | ( ))                       |     | 4.1 Data preprocessing |              |              |     |     |
|         | ij    | Scorei X ,Scorej | X  represents the Pearson  |     |                        |              |              |     |     |
correlation between components i and j. Empirical analysis on our
dataset  reveals  moderate  positive  correlations:  4.1.1 Data sources and sampling strategy
ρ ps =0.42±0.08,ρ pr =0.38±0.06, and ρ sr =0.51±0.09, indicating  This research uses financial data of Chinese listed companies from
that these components capture partially overlapping anomaly patterns. the CSMAR database, with samples covering quarterly and annual
Frontiers in Applied Mathematics and Statistics 06 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
( ( ))
financial data of all companies listed on the A-share market from 2000 Where E h x is the expected path length for observation x, and
( )
to 2020. As an authoritative data source for Chinese capital market c n is the average path length of unsuccessful search in a Binary
research, the CSMAR database provides standardized, highly Search Tree. Only observations identified as outliers by both methods
continuous financial data, including balance sheets, income (LOF score > 2.5 and Isolation Forest anomaly score >0.6)
statements, cash flow statements, and related financial indicators, undergo adjustment.
establishing a solid data foundation for anomaly detection research For confirmed outliers, instead of applying univariate
(28–30). Winsorization, we employ a multivariate adjustment approach that
The sampling strategy employs stratified random sampling, preserves the correlation structure. Specifically, we project the outlier
stratifying samples by industry, size, and listing duration to ensure onto the boundary of the 99% confidence ellipsoid in the direction
representativeness and balance in data distribution. To mitigate the from the data center:
interference of industry characteristics on anomaly detection, this
s
to
tu d
t
y
h
c
e
a te
C
go
h
r
i
i
n
z
a
es s
S
am
ec
p
u
l
r
e
i
s
t i
i
e
n
s
t o 1
R
0
e g
m
u
a
la
jo
to
r
r
in
y
du
C
st
o
r
m
y c
m
at
i
e
s
g
si
o
o
r
n
ie
’s
s ac
in
co
d
r
u
d
s
i
t
n
ry
g xadjusted =µ+α⋅Σ1/2⋅
x
x
−
−
µ
µ
Σ
classification standards, using the same sampling proportion within
each industry. The final dataset includes 31,724 company-quarter
observations, and after excluding ST, *ST companies and samples with Where µ is the robust center estimated using the Minimum
severe data missing, 28,569 valid observations were retained. Covariance Determinant (MCD) estimator, Ó is the robust
covariance matrix, and α is chosen such that xadjusted lies on the
4.1.2 Data cleaning and standardization 99% confidence ellipsoid boundary. This approach preserves the
processing multivariate structure while reducing the influence of extreme
Accounting data commonly exhibits missing values, outliers, and observations, ensuring that potentially fraudulent patterns remain
scale inconsistencies, requiring systematic cleaning and detectable while mitigating the impact of data errors or legitimate
standardization processing (31, 32). This study adopts the following extreme business events.
procedures for data preprocessing: All adjusted data points are recorded with their original values
Missing value processing: Different strategies are applied to and adjustment ratios for transparency and subsequent validation in
different types of missing data. For Missing At Random (MAR), the anomaly detection phase.
multiple linear interpolation is used, estimating missing values based Data standardization: Financial indicators exhibit significant
on adjacent time points and related financial indicators; for Missing differences in measurement scales and distributions. Z-score
Not At Random (MNAR), such as systematically missing specific standardization transforms different indicators to make them
financial indicators, industry means are used as substitutes or the comparable on the same scale:
observation samples are directly eliminated. Financial indicators with
m
va
i
l
s
u
s
e
in
p
g
r o
r
p
at
o
e
r
s
t i
e
o
x
n
c
s
e e
e
d
x
i
c
n
e
g
e d
2
i
0
n
%
g 3
a
0
re
%
r e
a
m
re
o
e
v
li
e
m
d,
i n
a
a
n
t
d
e d
s
.
amples with missing Zi,j,t = Xi,j
σ
,t
j
−
,i
µ j,i
Outlier processing: Recognizing the multidimensional nature of
financial data, this study employs a two-stage outlier detection
approach that considers multivariate relationships. In the first stage, Where Xi,j,t represents the value of financial indicator j for
we apply the Local Outlier Factor (LOF) algorithm to identify company i at time t, and µ j,i and σ j,i represent the mean and standard
multivariate outliers by examining the local density deviation of each deviation of the company’s historical data, respectively. This company-
data point relative to its neighbors. The LOF score for each observation internal standardization method both preserves cross-temporal
is calculated as: variation characteristics and avoids biases from direct cross-
company comparisons.
( )
∑ lrdk o Time series adjustment: Considering the seasonality and trend
( )
LOFk ( x )= o∈N ∣ k N (x k )l ( r x d )∣ k x c is h a a r p a p ct li e e r d is ti t c o s o se f a a s c o c n o a u l n ly ti n a g d j d u a s t t a , q t u he a r X te - r 1 l 3 y A d R at I a M , A se -S p E ar A a T ti S n g m e t t r h en o d d
components, seasonal components, and random components,
providing a stable data foundation for time series modeling.
( )
Where lrdk x is the local reachability density of point x, and
( )
Nk x represents the k-nearest neighbors of x. We set k = 20 based
4.2 Feature engineering
on empirical testing, and observations with LOF scores exceeding 2.5
are flagged as potential outliers.
In the second stage, we validate these multivariate outliers using 4.2.1 Financial indicator selection and
an Isolation Forest algorithm, which efficiently isolates anomalies by construction
constructing random decision trees. The anomaly score is Based on accounting theory and practical experience, this study
computed as: selects and constructs a financial indicator system from four
dimensions: profitability, solvency, operational efficiency, and
E
( h(x)) cash flow:
s
(
x,n
)=2
− c(n) Profitability indicators: Including Return on Equity (ROE),
Return on Assets (ROA), Net Profit Margin (NPM), Gross Profit
Frontiers in Applied Mathematics and Statistics 07 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
Margin (GPM), Operating Profit Margin (OPM), and Earnings Per Principal Component Analysis (PCA): Applying PCA
Share (EPS), reflecting a company’s ability to generate profits. dimensionality reduction to standardized financial indicators,
Solvency indicators: Including Current Ratio (CR), Quick Ratio retaining principal components with cumulative explained variance
(QR), Leverage Ratio (LEV), Interest Coverage Ratio (ICR), and Cash reaching 90%, mapping high-dimensional financial data to a
Flow to Debt Ratio (CFD), reflecting a company’s ability to repay debts. low-dimensional representation space.
Operational efficiency indicators: Including Inventory Turnover Autoencoder feature extraction: Based on a nonlinear
Rate (ITR), Accounts Receivable Turnover Rate (ARTR), Total Asset autoencoder structure, learning low-dimensional latent
Turnover Rate (TATR), and Fixed Asset Turnover Rate (FATR), representations of financial data with minimal reconstruction error
reflecting asset utilization efficiency. as the objective. The autoencoder consisted of a 3-layer encoding
Cash flow indicators: Including Operating Cash Flow (OCF), network and a 3-layer decoding network, compressing
Cash Flow Adequacy Ratio (CFAR), Sales Cash Ratio (SCR), and Free 42-dimensional original features to 16-dimensional latent
Cash Flow (FCF), reflecting a company’s cash generation and representations through batch training.
management capabilities. Temporal feature construction: Calculating statistical features
In addition to basic financial indicators, the following composite within sliding windows, including mean, standard deviation, rate
indicators were constructed to enhance anomaly detection capabilities: of change, kurtosis, and skewness, to capture dynamic change
Accounting quality indicators: Modified Jones model indicators patterns of financial indicators. Additionally, extracting multi-scale
based on accrual items, used to measure the degree of time-frequency features based on Discrete Wavelet Transform
earnings management. (DWT) to enhance the model’s ability to recognize anomalies at
Financial stability indicators: Variants of Altman Z-score and different frequencies.
Beneish M-score, adapted to the characteristics of China’s SHAP feature importance assessment: Using SHAP (SHapley
capital market. Additive exPlanations) values to evaluate each feature’s
Growth consistency indicators: Measuring the coordination contribution to anomaly identification, dynamically adjusting
between revenue growth and asset growth, cost growth, and other feature weights based on contribution degree to optimize detection
indicators to identify unreasonable financial growth patterns. precision. Ultimately, 22 core financial indicators were selected as
model inputs.
4.2.2 Feature extraction and dimensionality Figure 2 illustrates the results of financial feature importance
reduction analysis and anomaly type analysis. The left side uses horizontal bar
The initial feature set contained 42 financial indicators, presenting charts to intuitively present the SHAP value ranking of the 8 financial
issues of high dimensionality and multicollinearity. The following indicators that contribute most to anomaly detection. The results
methods were used for feature processing and show that profitability indicators play a core role in anomaly
dimensionality reduction: detection, with Return on Equity (ROE, 0.196) and Return on Assets
Correlation analysis: Calculating the Pearson correlation (ROA, 0.179) having significantly higher contributions than other
coefficient matrix to identify highly correlated indicator pairs indicators, followed closely by Current Ratio (0.163) and Leverage
(|r| > 0.85) and retaining indicators with more significant Ratio (0.149), indicating that solvency indicators are also important
financial meaning. dimensions for financial anomaly identification. The right side
FIGURE 2
Financial feature importance analysis and anomaly distribution.
Frontiers in Applied Mathematics and Statistics 08 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
systematically displays five typical financial anomaly patterns and Latent representation layer: Applies a fully connected layer to the
their characteristics, including revenue inflation (38.6%), expense fused representation to obtain a 32-dimensional latent representation,
concealment (21.7%), asset overvaluation (17.4%), liability which serves as the decoder input.
understatement (15.2%), and composite manipulation (7.1%), and Decoder layer: Employs bidirectional LSTM layers with a
provides key features and detection rate data for each type of anomaly. symmetrical structure to restore the latent representation to the
This dual analysis framework not only reveals the importance original input dimension. The short-term and long-term decoders
hierarchy of financial features but also demonstrates the identification reconstruct the financial data for their respective time windows.
patterns of different types of financial anomalies, providing intuitive Output layer: Maps to the original feature space through a fully
support for the model’s effectiveness in distinguishing between connected layer, generating the reconstructed sequence.
normal and anomalous financial data. To enhance model robustness, a Dropout layer (dropout
rate = 0.3) is added between the encoder and decoder, and Batch
Normalization is applied in the reconstruction layer.
4.3 Model design and training
The implementation details of the dual-channel LSTM
autoencoder are presented in Algorithm 2.
4.3.1 Dual-channel LSTM autoencoder
architecture 4.3.2 Model training and optimization
Based on the Hierarchical Fusion Self-supervised Learning The following training strategies are adopted for the characteristics
(HFSL) framework proposed in Chapter 3, this study designs a dual- of self-supervised learning and accounting data:
channel LSTM autoencoder to implement self-supervised learning Loss function design: Optimizes the model by combining
and anomaly detection for accounting data. The specific architecture reconstruction loss and contrastive loss:
is as follows:
Input layer: Receives time series data of 22-dimensional financial =λ 1  recon +λ 2  con
indicators, with the short-term channel input window size set to 4
(corresponding to 1 year of data) and the long-term channel input where reconstruction loss  recon is calculated based on the
window size set to 12 (corresponding to 3 years of data). temporal contrastive learning method introduced in Chapter 3. λ 1, λ 2,
Encoder layer: The short-term and long-term channels each and β are balancing parameters determined through grid search to
contain bidirectional LSTM layers with 64 and 128 units respectively, find optimal values.
capturing financial patterns at different time scales. The LSTM layers Training strategy: Employs a phased training strategy, first
adopt an improved cell structure, integrating financial training the short-term and long-term channels separately, then
prior information: performing joint optimization. Data is divided into training,
validation, and test sets in a 0.7:0.15:0.15 ratio, with the training set
ft =σ( Wf·ht−1,xt,pt +bf ) containing only normal samples, while validation and test sets contain
it =σ( Wi·ht−1,xt,pt +bi ) both normal and anomalous samples. Batch size is set to 64, using an
C
t
=tanh ( WC·ht−1,xt,pt +bC ) early
O
s
p
to
ti
p
m
p
i
i
z
n
e
g
r
m
se
e
l
c
e
h
ct
a
i
n
o
i
n
s
:
m
A
(
d
p
o
a
p
ti
t
e
s
n
t
c
h
e
e
=
A
2
d
0
a
)
m
to
o
a
p
v
ti
o
m
id
i z
o
e
v
r
e
w
rfi
it
tt
h
i n
a
g
n
.
initial
Ct = ftCt−1 +itC t learning rate of 0.001, applying a learning rate scheduling strategy
ot =σ( Wo·ht−1,xt,pt +bo ) with 10% decay every 30 epochs.
ht =ottanh ( Ct ) Hyperparameter optimization: Searches for key hyperparameters
through Bayesian optimization, including LSTM layer numbers (1–3),
hidden unit numbers (32–256), Dropout rates (0.1–0.5), attention
where pt represents financial prior information, including dimensions (16–128), etc., with F1-score on the validation set as the
industry means, historical trends, and other domain knowledge. optimization objective. The final optimal model configuration is:
Attention fusion layer: Integrates short-term and long-term short-term channel with 2 LSTM layers (64 units), long-term channel
representations through an adaptive attention mechanism: with 2 LSTM layers (128 units), Dropout rate of 0.3, and attention
dimension of 64.
es =vTtanh ( Wshs ) Model implementation uses the PyTorch 1.9.0 framework, with
el =vTtanh ( Wlhl ) training conducted on a server equipped with an NVIDIA V100 GPU,
( ) taking approximately 18 h, and resulting in a final model with
α =
exp es
1.8 M parameters.
s
exp
(
es
)+exp (
el
)
Figure 3 shows the 3D visualization of reconstruction errors from
( )
α =
exp el the dual-channel LSTM autoencoder and time series analysis of
l
exp
(
es
)+exp (
el
)
anomaly scores. The left image uses a three-dimensional bar chart to
z =α shs +α lhl present the distribution of reconstruction errors for different financial
indicators across years, with a gradient color scheme from blue (low
error) to red (high error) intuitively displaying the model’s excellent
where hs and hl are the hidden states of the short-term and long- modeling effect on key indicators such as ROE and ROA. The right
term encoders respectively, α s and α l are the corresponding attention image uses time series graphs with filled areas to show the anomaly
weights, and z is the fused representation. score trend changes of three typical companies: Company A exhibits
Frontiers in Applied Mathematics and Statistics 09 frontiersin.org

| Zhang and Duan  |     |     |     |     |     |     | 10.3389/fams.2025.1628652 |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
fraud patterns over time. The system tracks the distribution of
Input:
anomaly scores within sliding windows and triggers model adaptation
when significant drift is detected. This adaptive mechanism ensures
Financial indicators sequence X (cid:281) ℝᵀˣᴰ
the model remains effective despite evolving fraud techniques and
| Output:  |     | regulatory changes. |     |     |     |     |     |     |     |
| -------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Reconstructed sequence X̂ , anomaly score
| Parameters: |     | 4.4 Anomaly detection and evaluation  |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
mechanism
window_short = 4
4.4.1 Multi-dimensional anomaly score
window_long = 12
calculation
// Encoding Phase  This study integrates three anomaly scoring methods to improve
| X_short = SlidingWindow(X, window_short) |     | detection accuracy: |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Reconstruction error score: Calculates the weighted Euclidean
X_long  = SlidingWindow(X, window_long) distance between the original sequence and the reconstructed
sequence:
// Short‑term channel
|                                 |     |     |            |     | T    | d         |     |     |     |
| ------------------------------- | --- | --- | ---------- | --- | ---- | --------- | --- | --- | --- |
| hₛ¹ = BiLSTM(X_short, units=64) |     |     |            |     |      | (         |     | )2  |     |
|                                 |     |     | Scorerecon | ( X | )= ∑ | ∑ wj xt,j | −xˆ |     |     |
t,j
| hₛ² = BiLSTM(hₛ¹, units=64)  |     |     |     |     | t=1j=1 |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |

h_s  = Dropout(hₛ², rate=0.30)
|     |     | where  | wj  represents  |     | the  importance  |     | weight  | of  feature  | j,  |
| --- | --- | ------ | --------------- | --- | ---------------- | --- | ------- | ------------ | --- |
// Long‑term channel
determined through SHAP values.
hₗ¹ = BiLSTM(X_long, units=128)

| hₗ² = BiLSTM(hₗ¹, units=128)  |     |           |        | T d  |      |        |              |          |        |
| ----------------------------- | --- | --------- | ------ | ---- | ---- | ------ | ------------ | -------- | ------ |
|                               |     |           | ( )= 1 | ∑ ∑  | (    | (      | −xt,j )≠sign | (        | −xˆ )) |
|                               |     | Scorepred | X      | wj·I | sign | xt+1,j |              | xˆ t+1,j | t,j    |
T
| h_l  = Dropout(hₗ², rate=0.35)  |     |     |     | t=1j=1 |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
// Attention fusion
|     |     | where I | () ·  is an indicator function, measuring the inconsistency  |     |     |     |     |     |     |
| --- | --- | ------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
e_s = tanh(W_s · h_s)
of trend predictions.
e_l = tanh(W_l · h_l) Rule violation score: Quantifies the degree of violation of financial
logic rules:
(cid:162)_s = softmax(e_s)
R
| (cid:162)_l = softmax(e_l) |     |     |           | (   | )=∑wr·Violationr |     | ( ) |     |     |
| -------------------------- | --- | --- | --------- | --- | ---------------- | --- | --- | --- | --- |
|                            |     |     | Scorerule | X   |                  |     | X   |     |     |
|                            |     |     |           |     | r=1              |     |     |     |     |
z   = α_s · h_s + α_l · h_l
// Decoding Phase
( )
|     |     | where Violationr |     | X   |  measures the degree of violation of rule r,  |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
z_latent = Dense(z, units=32) and wr is the importance weight of the rule.
X̂ The three scores are integrated through weighted fusion to form
_short = Decoder_LSTM(z_latent, window_short)
the final anomaly score:
X̂
_long  = Decoder_LSTM(z_latent, window_long)
|                      |       |            | ( )=α | 1·Sˆ  | ( )+α | 2·Sˆ | ( )+α | 3·Sˆ ( ) |     |
| -------------------- | ----- | ---------- | ----- | ----- | ----- | ---- | ----- | -------- | --- |
|                      |       | Scorefinal | X     | recon | X     | pred | X     | rule X   |     |
| return X̂ _short, X̂ | _long |            |       |       |       |      |       |          |     |
ALGORITHM 2
Dual-channel LSTM autoencoder architecture. To ensure fair comparison and proper weight allocation among
different scoring components, each score is standardized using
z-score normalization:
a gradual deterioration pattern and breaches the anomaly threshold
|     |     |     |     |     | Si ( | X ) −µ |     |     |     |
| --- | --- | --- | --- | --- | ---- | ------ | --- | --- | --- |
i n  m i d - 2 0 1 8 ,  C o m p a n y   B  s h o w s  s u d d en  a n o m a li es  a ft e r  2 0 1 8 ,  w h i le   Sˆ ( )= i
i X
C o m p a n y   C  c o n s ist e n tl y   m a in t ai n s  w i th in  t h e  no r m a l  ra n g e  b e l o w  t h e  σ
|     |     |     |     |     |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
threshold. This multi-dimensional analysis intuitively demonstrates
the framework’s capability to identify different types of financial
anomalies and its early warning characteristics. Where Si ( X )  represents the raw score for component i (recon,
The HFSL framework incorporates a concept drift detection  pred, or rule), and µ i, σ i are the mean and standard deviation
mechanism based on the Page-Hinkley test to monitor changes in  estimated from the training set normal samples.
Frontiers in Applied Mathematics and Statistics 10 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
FIGURE 3
Multi-company anomaly score time series analysis.
5 Experimental design
The standardization process ensures that all three components
contribute to the final score according to their assigned weights α 1, α 2
and α 3, regardless of their original scale differences. Through genetic 5.1 Data preparation
algorithm optimization on the validation set, the optimal weights were
determined as 0.5, 0.3, and 0.2 respectively, reflecting the relative 5.1.1 Dataset division
importance of reconstruction accuracy, prediction consistency, and For reproducibility, data preprocessing follows standardized
rule compliance in identifying accounting anomalies. Z-score normalization within companies, and the chronological split
(2000–2010 training, 2011–2015 validation, 2016–2020 testing)
4.4.2 Adaptive threshold determination ensures temporal validity while preventing data leakage.
To address the limitations of traditional fixed thresholds, this To evaluate the model’s performance across different time periods
study employs Gaussian Mixture Models (GMM) to adaptively and its generalization ability, this study adopts a chronological division
determine detection thresholds: strategy, partitioning the Chinese listed companies’ financial data
Fitting a K-component GMM (K = 3) to the anomaly scores of from the CSMAR database (2000–2020) into non-overlapping
normal samples in the training set: training, validation, and test sets. Specifically, data from 2000 to 2010
is designated as the training set, accounting for 62.3% of the total
p ( score )=∑ K π k  ( score∣µ k,σ k 2 ) s a a s m th p e l e v a w li i d th a t 1 io 7 n ,8 s 1 e 7 t , v r a e l p id r e o s b e s n e t r in va g t 1 io 9 n .8 s % ; d w at i a t h fr 5 o , m 65 2 4 0 o 1 b 1 s e to rv 2 a 0 t 1 io 5 n s s e ; r a v n e d s
k=1
data from 2016 to 2020 forms the test set, comprising 17.9% with
5,098 observations. This time-series partitioning effectively simulates
Identifying the component with the largest variance (typically real-world application scenarios, enabling the model to predict
corresponding to marginal normal samples) and setting the threshold potential future anomalies based on historical data while testing its
based on this component: adaptability to changing market environments.
During the training phase, following the self-supervised learning
θ=µ
high
+γ·σ
high paradigm, only normal samples are used for model training, with
anomalous samples reserved exclusively for performance evaluation
during validation and testing phases. To mitigate the impact of data
where γ is an adjustable coefficient, with the optimal value distribution changes over time, this study introduces a sliding window
determined through ROC curve analysis (this study uses 2.5). mechanism with a window length of 12 quarters (corresponding to
To accommodate industry and size differences, a stratified 3 years of financial data), sliding one quarter at a time. This approach
adaptive threshold strategy is further designed, calculating thresholds both preserves the temporal dependencies in financial data and
separately for companies in different industries and market enhances the model’s ability to recognize long-term financial trends.
capitalization intervals to improve detection precision. Additionally, stratified sampling based on the China Securities
Frontiers in Applied Mathematics and Statistics 11 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
Regulatory Commission’s industry classification standards ensures to validation and test sets in a 9:1 ratio, while maintaining consistent
consistent industry distribution across training, validation, and distribution of various anomaly types in both sets. Anomaly samples
test sets. in the validation set are used for model optimization and threshold
Data preprocessing follows the three-stage adaptive processing determination, employing 5-fold cross-validation to establish the
procedure proposed in Chapter 4, including industry calibration, optimal detection threshold (μ + 2.5σ); the test set is used for final
seasonal adjustment, and noise suppression. Specifically, for missing performance evaluation, covering both overall and category-
values in the training set, a combination of forward filling and linear specific assessments.
interpolation is employed; for the validation and test sets, only
statistical characteristics from the training set are used for filling to
5.2 Experimental setup
avoid information leakage. For standardization, company-internal
Z-score standardization is applied to preserve cross-temporal variation
characteristics while avoiding comparison biases between companies The experimental environment is implemented based on Python
of different scales: 3.8 and the PyTorch 1.9.0 framework, with model training and testing
conducted on a high-performance computing server equipped with
Zi,j,t = Xi,j
σ
,t
j
−
,i,
µ
tra
j,
i
i
n
,train a
V
n
1
I
0
n
0
t e
3
l
2
X
G
e
B
on
G
E
P
5
U
-2
.
6
C
9
o
0
n
v
s
4
i d
C
e
P
ri
U
n
,
g
6
d
4G
at
B
a
m
sc
e
a
m
le
o
a
r
n
y
d
, a
m
nd
o d
an
el
N
c
V
om
ID
p
I
l
A
ex
T
it
e
y
s
,
l
a
a
distributed training framework is adopted to improve computational
efficiency, with data parallelism set to 4.
where µ j,i,train and σ j,i,train represent the mean and standard The core of the self-supervised learning framework—the dual-
deviation of financial indicator j for company i in the training set. channel LSTM autoencoder—is configured as follows: the short-term
channel input window size is set to 4 quarters (1 year), with 2 LSTM
5.1.2 Anomaly identification layers, 64 hidden units, and a dropout rate of 0.3; the long-term
Anomaly labeling in our self-supervised framework follows a channel input window size is set to 12 quarters (3 years), with 2 LSTM
hybrid approach: real anomalies are identified from verified fraud layers, 128 hidden units, and a dropout rate of 0.35. The attention
cases in CSMAR database and regulatory announcements, while fusion layer dimension is set to 64, and the latent representation layer
maintaining unlabeled normal samples for training as per self- dimension is 32. The model contains approximately 1.83 M
supervised learning principles. parameters, with the short-term channel accounting for 27.3%, the
To comprehensively evaluate the performance of anomaly long-term channel for 45.8%, and the attention fusion and latent
detection algorithms, this study constructs a composite test set representation layers for 26.9%.
containing both real anomalies and simulated anomalies. Real The training process adopts the following strategy: first
anomaly samples are derived from three sources: financial fraud cases conducting staged optimization, pre-training the short-term and
and major accounting error correction cases marked in the CSMAR long-term channels separately for 15 epochs, followed by joint
database (117 companies); companies suspected of financial anomalies optimization training for 40 epochs. The batch size is set to 64, with
identified through media reports and regulatory announcements (56 an initial learning rate of 0.001, using an Adam optimizer with 0.9
companies); and listed companies issued with non-standard audit momentum, and learning rate decay to 0.8 times its original value
opinions (243 instances), covering qualified opinions, adverse every 10 epochs. To prevent overfitting, L2 regularization (weight
opinions, and disclaimers of opinion. These real anomaly samples decay coefficient of 1e-5) and an early stopping mechanism
primarily involve violations such as inflated revenue, inflated profits, (patience = 12) are applied. The loss function adopts a weighted
and concealed liabilities, exhibiting certain distribution characteristics combination of reconstruction loss and contrastive loss as defined
across industries and time dimensions. in Chapter 3, with weight coefficients λ 1 and λ 2 determined through
Considering the limitations of real anomaly samples, this study grid search as 0.7 and 0.3.
designs and constructs four types of simulated anomaly samples to To address varying time series length issues, forward filling is
enrich the testing system: (1) financial indicator mutation anomalies, employed for sequences shorter than the specified window length,
introducing abnormal fluctuations exceeding 3 standard deviations in while sliding window sampling is used for excessively long sequences.
key indicators such as ROE and ROA; (2) financial ratio inconsistency Data batch construction adopts a temporally proximate sampling
anomalies, disrupting intrinsic relationships between key ratios such strategy, ensuring temporal coherence within each batch to enhance
as gross profit margin and net profit margin; (3) temporal pattern the model’s ability to learn temporal patterns. For each financial data
anomalies, altering the seasonal and trend characteristics of financial sample, random masking (masking rate 10%) is applied as a data
indicators; and (4) accounting equation violation anomalies, augmentation technique to improve model robustness.
introducing subtle violations of basic accounting principles while To comprehensively evaluate the effectiveness of the proposed
maintaining surface consistency. The generation process for simulated method, four comparison benchmark experiment groups are
anomalies strictly follows three principles: domain knowledge established: (1) traditional statistical methods group, including
constraints, reasonable distribution of anomaly intensity, and Z-score-based anomaly detection and improved Benford analysis; (2)
consideration of industry differences, ensuring conformity with machine learning baseline group, including One-Class SVM and
characteristic distributions of actual financial anomalies. Isolation Forest; (3) deep learning baseline group, including standard
The final anomaly sample repository contains 894 real anomaly LSTM autoencoder and Variational Autoencoder (VAE); and (4) self-
cases and 1,256 simulated anomaly cases, totaling 2,150 anomaly supervised variant group, exploring the impact of different self-
samples. For scientific performance evaluation, samples are allocated supervised strategies on anomaly detection performance, including
Frontiers in Applied Mathematics and Statistics 12 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
reconstruction tasks, prediction tasks, and contrastive learning tasks. Additionally, considering the special requirements of financial
All baseline methods are trained and evaluated on identical datasets anomaly detection, the following professional metrics
to ensure fair comparison. are introduced:
The evaluation process follows iterative optimization principles, False Alarm Rate (FAR): The proportion of normal samples
optimizing model hyperparameters on the validation set through incorrectly classified as anomalous, particularly important for
5-fold cross-validation. Anomaly threshold determination employs a financial regulation.
GMM-based adaptive method, calculating optimal thresholds
FP
separately for each industry. Final performance evaluation is FAR=
conducted on the independent test set, introducing evaluation metrics
FP+TN
specific to financial anomaly detection in addition to conventional
precision, recall, F1-score, and AUC-ROC: early detection rate (EDR, Miss Rate (MR): The proportion of anomalous samples that fail to
the proportion detected within the first two quarters after anomaly be detected, reflecting the risk of anomalies evading detection.
occurrence) and false alarm rate (FAR, the proportion of normal
FN
samples incorrectly classified as anomalous). MR=
Experimental results are validated for statistical significance using
TP+FN
the Wilcoxon signed-rank test (p < 0.05), with sensitivity analysis
assessing the impact of key parameter changes on model performance Early Detection Rate (EDR): The proportion that can be detected
to ensure robustness and generalizability of conclusions. in the early stages of anomaly occurrence (within the first two
To assess the model’s robustness to evolving fraud patterns, quarters), evaluating the model’s early warning capability.
we conducted concept drift experiments by dividing the test period
into quarterly segments and introducing synthetic pattern changes at
EDR=
TPearly
specific time points corresponding to major regulatory events. Model TPearly +FNearly
adaptation capability was evaluated through performance stability
metrics and recovery time after drift detection.
Industry-Specific Detection Rate (ISDR): Detection accuracy in
specific industries, evaluating the model’s adaptability across
5.3 Evaluation metrics
different industries.
Fusi
T
o
o
n
co
S
m
elf
p
-
r
s
e
u
h
p
e
e
n
r
s
v
i
i
v
s
e
e
l
d
y e
L
v
e
a
a
lu
rn
at
i
e
n
t
g
h e
F
p
ra
e
m
rfo
e
r
w
m
o
a
rk
n ce
(H
of
F
t
S
h
L
e
) ,
H
t
ie
h
r
i
a
s
rc
s
h
tu
ic
d
a
y
l ISDRi =
TPi
T
+
P
F
i
Ni
constructs a multi-dimensional evaluation metric system covering two
dimensions: anomaly detection performance evaluation and model where i represents a specific industry.
fitting capability evaluation. Beyond confusion matrix-derived metrics, ranking quality
evaluation metrics are adopted to assess the model’s ability to rank
5.3.1 Anomaly detection metrics anomalous samples higher:
Evaluation of the anomaly detection task combines confusion Area Under the Receiver Operating Characteristic Curve (AUC-
matrix-derived metrics and ranking quality metrics. First, based on ROC): Evaluating the trade-off relationship between true positive rate
the confusion matrix of prediction results versus true labels, the and false positive rate at different thresholds.
following metrics are calculated: Area Under the Precision-Recall Curve (AUC-PR): More
Precision: The proportion of correctly detected anomalous reflective of model performance than the ROC curve in imbalanced
samples among all samples detected as anomalous, reflecting the scenarios with a low proportion of anomalous samples.
reliability of the model’s detection results. Mean Average Precision (MAP): Calculating the average precision
at different recall levels, evaluating overall ranking quality.
TP
Precision= Figure 4 illustrates the comparison between the HFSL
TP+FP
framework and five baseline methods across six key performance
metrics. The left chart shows each model’s performance on three
Recall: The proportion of correctly detected anomalous samples fundamental metrics—precision, recall, and F1-score—with the
among all true anomalous samples, reflecting the model’s capability to HFSL framework outperforming all baseline methods, achieving
detect anomalies. an F1-score of 0.845, approximately 9.5% higher than the closest
LSTM-AE. The right chart reflects comparisons on professional
TP
Recall= metrics, including AUC-ROC, early detection rate, and false alarm
TP+FN
rate. The HFSL framework not only possesses the highest
AUC-ROC value (0.894) and early detection rate (0.726), but its
F1-score: The harmonic mean of precision and recall, balancing false alarm rate (0.068) is also significantly lower than other
consideration of detection accuracy and completeness. methods, which is of great significance for financial risk control.
This figure intuitively demonstrates the significant contribution
2×Precision×Recall
F1= of hierarchical fusion design to enhancing anomaly
Precision+Recall
detection performance.
Frontiers in Applied Mathematics and Statistics 13 frontiersin.org

| Zhang and Duan  |     |     |     |     |     |     | 10.3389/fams.2025.1628652 |
| --------------- | --- | --- | --- | --- | --- | --- | ------------------------- |
FIGURE 4
Anomaly detection performance comparison.
For evaluating detection performance across different anomaly  Mean Squared Error (MSE): Measures the average of the squared
types,  this  study  generated  radar  charts  of  various  models’  deviations  between  the  reconstructed  sequence  and  the
| performance on four types of simulated anomalies and real anomalies,  |     |     |     | original sequence. |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- |
with detailed F1-score data provided in Table 1.
F ig u re   5   in t u it i v e ly   di s p la y s  e a c h   m o d e l ’s   F 1 - s c o r e   p e r f o r m a n c e   1 N T D
|     |     |     |     |     | MSE= | ∑∑∑( | −xˆ )2 |
| --- | --- | --- | --- | --- | ---- | ---- | ------ |
xi,t,j i,t,j
acro ss  fi v e  t y p e s  o f   a n o m a l ie s  t h r o u g h  r a d a r   c h a r t s .  T a b l e   1   f ur t h e r  N×T ×D
|     |     |     |     |     |     | i=1t=1j=1 |     |
| --- | --- | --- | --- | --- | --- | --------- | --- |
provides precise performance data for all six models across various
anomaly types.
From the table, it can be observed that the HFSL framework  Mean Absolute Error (MAE): Measures the average of absolute
achieves optimal results across all anomaly types, particularly  reconstruction errors, insensitive to outliers.
excelling in financial indicator mutation anomalies (0.892) and
financial ratio inconsistency anomalies (0.863), outperforming the  1 N T D
|     |     |     |     |     | MAE= | ∑∑∑∣xi,t,j | −xˆ ∣ |
| --- | --- | --- | --- | --- | ---- | ---------- | ----- |
i,t,j
second-best LSTM-AE model by 0.058 and 0.077 percentage points,  N×T×D
|                |          |                       |            |           |     | i=1t=1j=1 |     |
| -------------- | -------- | --------------------- | ---------- | --------- | --- | --------- | --- |
| respectively.  | LSTM-AE  | performs  relatively  | close  to  | HFSL  in  |     |           |     |
accounting equation violation anomalies (0.802 vs. 0.841), while VAE
also achieves a high F1-score of 0.792 for this anomaly type. Notably,  Weighted Mean Squared Error (WMSE): MSE with different
all models generally perform relatively weakly in detecting temporal  weights assigned according to financial indicator importance.
pattern anomalies, with HFSL, LSTM-AE, and VAE achieving
N T D
F 1 -s c o r e s   o f  0 . 7 9 1 ,   0 .7 1 3 ,  a n d   0 . 6 8 5 ,  r e sp e ct i v e ly , reflecting the  1 ( )2
|     |     |     |     |     | WMSE= | ∑∑∑wj | xi,t,j −xˆ |
| --- | --- | --- | --- | --- | ----- | ----- | ---------- |
di ffi c u l t y  i n   id e n t if y i n g  t e m p o r al   p a t te r n  a n o m a l ie s . ×T i,t,j
N i=1t=1j=1

For real anomaly samples, all models show relatively lower
| performance,  | with  HFSL  | achieving  | an  F1-score  | of  0.798,  |     |     |     |
| ------------- | ----------- | ---------- | ------------- | ----------- | --- | --- | --- |
approximately  6%  lower  than  its  average  performance  on  where wj represents the importance weight of indicator j.
simulated anomalies, reflecting the complexity and concealment  Mean  Absolute  Percentage  Error  (MAPE):  The  average  of
| of actual financial fraud. Traditional statistical methods such as  |     |     |     | relative errors. |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- |
Z-Score significantly underperform machine learning and deep
learning methods across all anomaly types, particularly achieving  1 N T D xi,t,j −xˆ
|     |     |     |     |     | MAPE= | ∑ ∑ ∑ ∣ | i,t,j ∣×100% |
| --- | --- | --- | --- | --- | ----- | ------- | ------------ |
only a 0.492 F1-score for temporal pattern anomalies. The overall  N×T×D xi,t,j
|     |     |     |     |     |     | i=1t=1j=1 |     |
| --- | --- | --- | --- | --- | --- | --------- | --- |
distribution of model performance exhibits a consistent gradient,
verifying the generalization capability of the hierarchical fusion
self-supervised learning framework across different anomaly types. Trend Consistency (TC): Measures the consistency degree of
trend changes between reconstructed and original sequences.
5.3.2 Model fitting metrics
The performance of a self-supervised learning framework
largely depends on its ability to fit normal data patterns. Therefore,  N T−1 D
|     |     |     |     |     | 1   | ( (∆xi,t,j | )=sgn (∆xˆ )) |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- |
|     |     |     |     |     | TC= | ∑∑∑I sgn   |               |
this study employs the following metrics to evaluate model  N×( −1 )×D i,t,j
|                  |     |     |     |     | T   | i=1t=1 j=1 |     |
| ---------------- | --- | --- | --- | --- | --- | ---------- | --- |
| fitting quality: |     |     |     |     |     |            |     |
Frontiers in Applied Mathematics and Statistics 14 frontiersin.org

Zhang and Duan  10.3389/fams.2025.1628652
TABLE 1 F1-score performance comparison of different models across anomaly.
Model Financial  Financial ratio  Temporal  Accounting  Real anomalies
|     | indicator  | inconsistency | pattern | equation violation |     |
| --- | ---------- | ------------- | ------- | ------------------ | --- |
mutation
| HFSL             | 0.892 | 0.863 | 0.791 | 0.841 | 0.798 |
| ---------------- | ----- | ----- | ----- | ----- | ----- |
| LSTM-AE          | 0.834 | 0.786 | 0.713 | 0.802 | 0.726 |
| VAE              | 0.805 | 0.763 | 0.685 | 0.792 | 0.683 |
| One-Class SVM    | 0.782 | 0.705 | 0.612 | 0.625 | 0.623 |
| Isolation forest | 0.723 | 0.658 | 0.572 | 0.603 | 0.582 |
| Z-score          | 0.684 | 0.623 | 0.492 | 0.562 | 0.536 |
FIGURE 5
Anomaly type performance radar chart.
Frontiers in Applied Mathematics and Statistics 15 frontiersin.org

| Zhang and Duan                               |     |                             |     |     | 10.3389/fams.2025.1628652 |     |
| -------------------------------------------- | --- | --------------------------- | --- | --- | ------------------------- | --- |
| where I ( · )  is an indicator function, sgn |     | (∆x )  represents the sign  |     |     |                           |     |
TABLE 2 HFSL framework performance metrics summary.
| of the direction of change, and ∆xi,t,j |     | =xi,t+1,j −xi,t,j. |            |            |              |      |
| --------------------------------------- | --- | ------------------ | ---------- | ---------- | ------------ | ---- |
|                                         |     |                    | Indicator  | Indicator  | Performance  | 95%  |
Volatility Preservation Rate (VPR): Evaluates the model’s ability
|     |     |     | category | name | value | confidence  |
| --- | --- | --- | -------- | ---- | ----- | ----------- |
to preserve the volatility characteristics of the original data. interval
|     |     |            |     | P r e c i s i o n | 0 . 8 3 6 | [ 0 . 8 2 1 ,   0 . 8 5 1 ] |
| --- | --- | ---------- | --- | ----------------- | --------- | --------------------------- |
|     | N   | D σ ( xˆ ) |     |                   |           |                             |
|     | 1   | i , j      |     |                   |           |                             |
VPR= ∑ ∑ Basic indicators R e c a l l 0 . 8 0 5 [ 0 . 7 8 9 ,   0 . 8 2 1 ]
|            | N×   | σ ( )         |     |                 |           |                             |
| ---------- | ---- | ------------- | --- | --------------- | --------- | --------------------------- |
|            | D =1 | =1 x i ,i , j |     |                 |           |                             |
|            | i    | j             |     | F 1 - s c o r e | 0 . 8 2 0 | [ 0 . 8 0 6 ,   0 . 8 3 4 ] |
|            |      |               |     | AUC-ROC         | 0.883     | [0.871, 0.895]              |
| where σ( ) |      |               |     |                 |           |                             |
·  represents standard deviation.
|                                                                       |     |     |           | AUC-PR | 0.772 | [0.756, 0.788] |
| --------------------------------------------------------------------- | --- | --- | --------- | ------ | ----- | -------------- |
| Additionally, the following specific evaluation metric is introduced  |     |     | Advanced  |        |       |                |
Mean average
| for time series models: |     |     | indicators |     |     |     |
| ----------------------- | --- | --- | ---------- | --- | --- | --- |
Short-term Prediction Accuracy (SPA): Evaluates the accuracy of  precision  0.794 [0.781, 0.807]
(MAP)
the model’s prediction for the next time point.
Early detection
|        |       |              |     |            | 0.726 | [0.707, 0.745] |
| ------ | ----- | ------------ | --- | ---------- | ----- | -------------- |
|        | 1 N D | xi,T+1,j −xˆ |     | rate (EDR) |       |                |
| SPA=1− | ∑ ∑ ∣ | i,T+1,j ∣    |     |            |       |                |
Professional
|     | N×D    | xi,T+1,j |            | False alarm rate  |       |                |
| --- | ------ | -------- | ---------- | ----------------- | ----- | -------------- |
|     | i=1j=1 |          | indicators |                   | 0.068 | [0.062, 0.074] |
(FAR)
|                                                 |     |                         |     | Miss rate (MR) | 0.195 | [0.179, 0.211] |
| ----------------------------------------------- | --- | ----------------------- | --- | -------------- | ----- | -------------- |
| where xi,T+1,j represents the true value and xˆ |     | i,T+1,j represents the  |     |                |       |                |
model’s predicted value.
Based on this evaluation metric system, this study conducted a
comprehensive assessment of the HFSL framework, testing not only  Comparing detection performance across different anomaly
its accuracy and timeliness in anomaly detection but also its  types, variations in HFSL framework performance are observed
performance in data fitting. Experimental results show that the fitting  (Figure 6), with best performance on financial indicator mutation
errors of the HFSL framework on metrics such as MSE and MAPE are  anomalies (F1 = 0.892), followed by financial ratio inconsistency
significantly lower than baseline methods, especially in terms of Trend  anomalies (F1 = 0.863), accounting equation violation anomalies
Consistency (TC), reaching a high level of 0.826, demonstrating that  (F1 = 0.841), temporal pattern anomalies (F1 = 0.791), and real
the model can effectively capture the temporal change characteristics  anomaly samples (F1 = 0.798). These results indicate that the
of financial data. model has higher sensitivity to sudden anomalies and static
relationship violation anomalies, with relatively lower sensitivity
to temporal pattern anomalies and complex real anomalies,
though overall performance remains at a high level.
6 Results analysis
Further analysis of the model’s performance across different
industries reveals industry-specific performance differences (Table 3).
6.1 Performance comparison In financial industry samples, the HFSL framework achieves the
highest F1-score (0.872), possibly due to the strictly regulated
6.1.1 Quantitative analysis environment and standardized financial reporting formats in the
This study conducted a comprehensive evaluation of the HFSL  financial industry. Performance is relatively lower in the construction
framework on the test set constructed from the CSMAR database,  and real estate industry (F1 = 0.776), consistent with the industry-
with test results showing excellent performance in accounting data  specific complexity of asset valuation and diversity in revenue
anomaly detection tasks. Table 2 summarizes the detailed performance  recognition. In manufacturing and information technology industries,
of the HFSL framework on various key indicators. model performance is at moderate levels (F1 scores of 0.817 and 0.831
As shown in Table 2, the HFSL framework demonstrates  respectively), reflecting the typical anomaly pattern structures of
balanced performance on basic indicators, with precision and  financial data in these industries.
recall reaching 0.836 and 0.805 respectively, and a combined  Analysis of the temporal stability of the model’s detection
F1-score of 0.820, indicating the model achieves a good balance  performance reveals, as shown in Figure 7, that the HFSL framework
between  detection  accuracy  and  completeness.  In  terms  of  exhibits significant temporal robustness during the 2016–2020 testing
advanced indicators, the AUC-ROC reaches 0.883, reflecting the  period, with F1 value variations across different quarters controlled
model’s strong classification ability across different threshold  within a narrow range of ±5%. This finding indicates that the model
settings; the AUC-PR is 0.772, particularly significant considering  possesses strong temporal generalization characteristics, capable of
the scarcity of anomalous samples (approximately 9.6% of the test  adapting to financial data feature changes across different periods.
set). Among professional indicators, the early detection rate (EDR)  Notably, a slight performance improvement is observed from the third
is approximately 0.73, indicating the model can identify over 70%  quarter of 2018 to the second quarter of 2019, corresponding to the
of anomalous cases in the early stages (first two quarters),  period when regulatory agencies strengthened financial supervision,
providing ample warning time for risk prevention and control;  leading to more pronounced anomaly patterns. In contrast, in early
meanwhile, the false alarm rate is only 0.068, significantly reducing  2020,  influenced  by  the  COVID-19  pandemic,  the  model’s
the regulatory costs associated with false positives. performance experienced a temporary decline, possibly due to
Frontiers in Applied Mathematics and Statistics 16 frontiersin.org

| Zhang and Duan  |     |     |     | 10.3389/fams.2025.1628652 |     |
| --------------- | --- | --- | --- | ------------------------- | --- |
FIGURE 6
Detection performance across different anomaly types.
TABLE 3 HFSL framework detection performance across industries.
| Industry                   | Sample Size | Precision | Recall | F1-score | AUC-ROC |
| -------------------------- | ----------- | --------- | ------ | -------- | ------- |
| Finance                    | 673         | 0.889     | 0.856  | 0.872    | 0.914   |
| Information technology     | 927         | 0.842     | 0.821  | 0.831    | 0.879   |
| Manufacturing              | 1,583       | 0.824     | 0.810  | 0.817    | 0.868   |
| Energy & utilities         | 493         | 0.851     | 0.792  | 0.820    | 0.885   |
| Consumer goods             | 716         | 0.835     | 0.807  | 0.821    | 0.876   |
| Healthcare                 | 312         | 0.862     | 0.813  | 0.837    | 0.891   |
| Construction & real estate | 394         | 0.798     | 0.756  | 0.776    | 0.833   |
| All industries average     | 5,098       | 0.936     | 0.805  | 0.820    | 0.883   |
differences between pandemic-induced abnormal financial patterns  Traditional statistical methods such as Z-score and improved
and historical patterns. Benford analysis, while simple to implement, perform significantly
worse than other methods, with F1-scores of only about 0.6, mainly
6.1.2 Comparison with traditional methods due to their inability to effectively capture the temporal dependencies
To assess the advantages of the HFSL framework relative to  and multivariate interaction patterns of financial data. Particularly in
existing methods, this study established four comparison experiment  terms of early detection rate, traditional methods achieve only about
groups, representing different types of anomaly detection methods.  0.43, lacking sensitivity to early anomaly signals, severely limiting
Table 4 and Figure 8 present detailed comparison results of various  their application value in practical supervision. Traditional machine
methods on key performance metrics. learning methods such as One-Class SVM and Isolation Forest, by
The  experimental  results  demonstrate  a  clear  performance  learning data distribution characteristics, show marked improvements
gradient among different types of anomaly detection methods. The  in precision and false alarm rates compared to statistical methods, but
HFSL framework further enhances performance on this foundation,  still have significant deficiencies in recall, indicating limitations in
with an F1-score approximately 7% higher than the best deep learning  processing high-dimensional, temporal financial data.
method (LSTM-AE), about 15% higher than machine learning  Deep learning methods such as LSTM-AE and VAE, through
methods (Isolation Forest), and even more significantly improved  complex neural network structures, can better capture nonlinear
compared to traditional statistical methods (Z-score), verifying the  features and temporal patterns of financial data, achieving F1-scores
substantial advantages of the proposed method (Table 5). of about 0.75, approximately 6% higher than machine learning
Frontiers in Applied Mathematics and Statistics 17 frontiersin.org

| Zhang and Duan  |     |     |     |     |     | 10.3389/fams.2025.1628652 |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------- | --- |
FIGURE 7
Time series performance analysis (2016–2020).
TABLE 4 Performance comparison of different anomaly detection methods.
Method  Method Name Precision Recall F1-score AUC-ROC Early  False
| Category |         |       |       |       |       | Detection  | Alarm  |
| -------- | ------- | ----- | ----- | ----- | ----- | ---------- | ------ |
|          |         |       |       |       |       | Rate       | Rate   |
|          | Z-score | 0.629 | 0.581 | 0.604 | 0.672 | 0.435      | 0.146  |
Traditional statistical
Improved Benford
| methods |     | 0.643 | 0.563 | 0.600 | 0.684 | 0.422 | 0.132 |
| ------- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
Analysis
Machine learning  One-Class SVM 0.722 0.663 0.691 0.724 0.504 0.107
| methods        | Isolation Forest | 0.736 | 0.682 | 0.708 | 0.753 | 0.522 | 0.103 |
| -------------- | ---------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| Deep learning  | LSTM-AE          | 0.795 | 0.734 | 0.763 | 0.832 | 0.631 | 0.080 |
| methods        | VAE              | 0.772 | 0.727 | 0.749 | 0.821 | 0.617 | 0.089 |
HFSL (Reconstruction
|     |     | 0.801 | 0.759 | 0.779 | 0.848 | 0.673 | 0.079 |
| --- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
Only)
Self-supervised
| variants | HFSL (Prediction  |       |       |       |       |       |       |
| -------- | ----------------- | ----- | ----- | ----- | ----- | ----- | ----- |
|          |                   | 0.788 | 0.774 | 0.781 | 0.853 | 0.691 | 0.085 |
Only)
| Complete method | HFSL | 0.836 | 0.805 | 0.820 | 0.883 | 0.726 | 0.068 |
| --------------- | ---- | ----- | ----- | ----- | ----- | ----- | ----- |
Bold values indicate the best performance for each metric.
methods. Particularly in early detection rate, the improvement exceeds  (F1 = 0.789), indicating that learning relationships between samples
20%, demonstrating the advantages of deep learning in early warning  is crucial for anomaly detection in accounting data. This may
capability. This performance enhancement mainly stems from deep  be because financial anomalies often manifest as degrees of deviation
learning models’ ability to automatically learn hierarchical feature  from normal samples, and contrastive learning precisely captures
representations from financial data without requiring manually  these relationship differences. By integrating the three self-supervised
designed complex feature engineering. However, traditional deep  learning tasks, the HFSL framework further improves performance
learning methods still rely on large amounts of labeled data, which  (F1 = 0.820), validating the effectiveness of multi-task fusion. This
presents  a  significant  challenge  in  the  field  of  financial  performance enhancement stems from different self-supervised tasks’
anomaly detection. ability to capture complementary data features, forming more
Introducing self-supervised learning strategies on the foundation  comprehensive data representations.
of deep learning significantly enhances model performance. Even  In terms of the critical early detection rate, the HFSL framework
using  reconstruction,  prediction,  or  contrastive  learning  tasks  (approximately  0.73)  outperforms  the  closest  baseline  method
individually  yields  performance  gains.  Among  the  three  self- LSTM-AE (approximately 0.63) by about 15%, providing regulatory
supervised  strategies,  contrastive  learning  tasks  perform  best  agencies with a valuable early warning time window and significantly
Frontiers in Applied Mathematics and Statistics 18 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
FIGURE 8
F1-score and AUC-ROC comparison of different methods.
TABLE 5 Financial statement fraud pattern classification and characteristics.
Fraud pattern Key financial Proportion (%) Detection rate (%) Representative anomaly
indicator anomaly example
features
ROE↑, ROA↑, Accounts
Company A: Fictitious customer
Revenue inflation Receivable Turnover↓, OCF/ 38.6 87.3
orders
Sales Ratio↓
Gross Profit Margin↑, Net
Profit Margin↑, Period Company B: Capitalized R&D
Expense concealment 21.7 84.5
Expense Ratio↓, Abnormal expenditures
compared to industry peers
Asset Impairment↓, Fixed
Asset overvaluation Asset Turnover↓, Inventory 17.4 79.8 Company C: Inventory overvaluation
Turnover↓
Leverage Ratio↓, Current
Company D: Contingent liabilities
Liability understatement Ratio↑, Accounts Payable 15.2 82.1
not accrued
Turnover↑
Multiple indicators
anomalous simultaneously,
Company E: Simultaneous revenue
Composite manipulation Inconsistent internal 7.1 68.2
inflation and liability concealment
relationships between
financial ratios
enhancing early intervention capabilities for financial risks. between the HFSL framework and all baseline methods are statistically
Simultaneously, HFSL’s false alarm rate (0.068) is significantly lower significant (p < 0.01), confirming that the effectiveness of the proposed
than other methods, reducing unnecessary investigation costs. This method is not due to random factors.
dual improvement gives HFSL higher practical value in real-world Comprehensive analysis indicates that the HFSL framework, by
applications, providing effective early warnings at the onset of integrating temporal contrastive learning, dual-channel LSTM
anomalies while keeping false alarms within an acceptable range. structure, and domain knowledge constraints, significantly enhances
Analysis of performance differences between methods through the the comprehensive performance of accounting data anomaly
Wilcoxon signed-rank test shows that the performance differences detection, achieving combined advantages particularly in detection
Frontiers in Applied Mathematics and Statistics 19 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
accuracy (F1-score), early warning capability (EDR), and false alarm probability, with the calculation process considering contribution
control (FAR). Performance improvements stem both from self- variations of features under different combinations, thereby providing
supervised learning paradigm’s effective utilization of unlabeled data relatively objective feature importance evaluations.
and from the multi-level fusion architecture’s targeted modeling of Figure 9 displays the SHAP value ranking of the 10 financial
multi-scale characteristics in accounting data. These results suggest indicators with the highest contributions to anomaly detection. The
that the proposed hierarchical fusion self-supervised learning analysis reveals that profitability indicators play a critical role in the
framework demonstrates promising application potential in the tested anomaly detection process. Particularly noteworthy is that the average
accounting data anomaly detection tasks. |SHAP| values of two core indicators—Return on Equity (ROE) and
Return on Assets (ROA)—reach as high as 0.196 and 0.179
respectively, significantly exceeding the contribution levels of other
6.2 Financial feature contribution analysis
financial indicators. This result aligns with financial theory, as
profitability indicators are often the primary targets of financial fraud,
This section delves into the contribution degrees and interaction with companies typically manipulating revenue and profit to embellish
effects of various financial features in the HFSL framework’s anomaly financial statements. ROE, as a core indicator for investors evaluating
detection results, using SHAP (SHapley Additive exPlanations) value enterprise value, often signals early financial problems when
analysis and feature interaction effect quantification methods to reveal exhibiting abnormal fluctuations.
the internal logic of the model’s decision mechanism, providing Current Ratio and Leverage Ratio, two indicators reflecting
interpretability support for financial anomaly detection. Through solvency capability, rank third and fourth, with |SHAP| values of 0.163
systematic analysis of financial feature importance rankings and their and 0.149, respectively. This indicates that abnormalities in a
interaction patterns, not only can the model’s effectiveness company’s short-term and long-term debt repayment capabilities are
be validated, but theoretical foundations can also be provided for also important indicators of financial anomalies. Notably, the
identifying accounting data anomaly patterns. Operating Cash Flow Ratio (OCF Ratio) ranks fifth (|SHAP| value of
0.139), verifying that inconsistencies between cash flow indicators and
6.2.1 Importance ranking of key financial accrual profit indicators provide an effective approach for identifying
indicators potential financial anomalies.
To quantitatively assess the impact of various financial indicators Efficiency indicators such as Accounts Receivable Turnover Rate
on anomaly detection results, this study calculated SHAP values for and Total Asset Turnover Rate also enter the top ten, with |SHAP|
22 core financial indicators based on the test set. SHAP values, values of 0.119 and 0.109 respectively, indicating that operational
through the concept of Shapley values in game theory, measure each efficiency indicators hold significant value in capturing abnormal
feature’s marginal contribution to the model’s predicted anomaly financial behaviors. From an industry perspective, the importance of
FIGURE 9
SHAP value analysis of financial indicators.
Frontiers in Applied Mathematics and Statistics 20 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
the Leverage Ratio in the financial industry is significantly higher than between ROE and ROA reaches 0.087, ranking first among all
in other industries (|SHAP| value increased by approximately 28%), indicator pairs, indicating that these two profitability indicators
while the Inventory Turnover Rate ranks relatively high in importance provide strong financial fraud signals when simultaneously
in manufacturing (entering the top 8), reflecting the influence of anomalous. Similarly, the interaction intensity between Current Ratio
industry characteristics on the importance of anomaly features. and Leverage Ratio is 0.082, reflecting the synergistic effect of short-
term and long-term solvency indicators. Such enhancing interactions
6.2.2 Multi-dimensional feature interaction effect primarily occur between indicators with similar functions but
analysis different calculation bases, and when enterprises exhibit simultaneous
Complex interdependencies exist between financial indicators, anomalies across multiple related indicators, it typically implies higher
where anomalies in a single indicator may be masked by normal financial risk.
values in other related indicators. Therefore, analyzing interaction Neutralizing interactions manifest when anomalies in one
effects between features is crucial for enhancing anomaly indicator are masked by changes in another indicator, reducing the
detection accuracy. This study employs a method based on SHAP sensitivity of anomaly detection. For example, the interaction effect
interaction values to quantitatively evaluate the interaction between Leverage Ratio and Total Asset Turnover Rate is relatively
intensity between feature pairs and their impact on anomaly weak (0.017), possibly because increases in Leverage Ratio due to
detection results. increased debt may be accompanied by corresponding decreases in
Figure 10 displays a heat map of interaction effect intensities Total Asset Turnover Rate, thus reducing the model’s sensitivity to
between core financial indicators, with darker areas indicating changes in single indicators. Such interactions suggest that when
stronger interaction effects and lighter areas indicating weaker designing anomaly detection models, overreliance on changes in
interaction effects. Through quantitative analysis of interaction single-dimension indicators should be avoided.
patterns, this study identifies three typical financial indicator Nonlinear interactions manifest as complex conditional
interaction modes: enhancing interactions, neutralizing interactions, dependency relationships between indicators. The interaction
and nonlinear interactions. intensity between Accounts Receivable Turnover Rate and Total Asset
Enhancing interactions manifest when the contribution of two Turnover Rate reaches as high as 0.084, a strong interaction
indicators acting jointly to anomaly detection is significantly higher relationship that is not intuitive, as while they both belong to efficiency
than the sum of their independent actions. The interaction intensity indicators, they measure different business links. In-depth analysis
FIGURE 10
Heat map of financial indicator interaction effects.
Frontiers in Applied Mathematics and Statistics 21 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
6.3 Identification and analysis of typical
reveals that this strong interactivity stems from their conditional
anomaly cases
dependency relationship in anomaly detection: when Accounts
Receivable Turnover Rate abnormally decreases while Total Asset
Turnover Rate abnormally increases, it often suggests that the 6.3.1 Financial statement fraud pattern
enterprise may be engaging in financial fraud behaviors such as classification
fictitious sales or premature revenue recognition. Based on the detection results of the HFSL framework, combined
By constructing an interaction network graph to analyze the with anomaly cases confirmed by manual audits, this study constructs
overall interaction structure, it is found that the financial indicator a systematic classification system for financial statement fraud
interaction network exhibits a “core-periphery” structure, where patterns, covering five typical anomaly modes: revenue inflation,
ROE, ROA, Current Ratio, and Leverage Ratio form a highly expense concealment, asset overvaluation, liability understatement,
interconnected core cluster, while other indicators display and composite manipulation. Table 2 shows the key characteristics of
relatively dispersed connection patterns. This network structure each fraud pattern and their distribution in the detected samples.
suggests that anomaly detection should focus on collaborative Revenue inflation is the most common financial fraud pattern,
changes within the core indicator cluster while also considering accounting for 38.6%, with typical characteristics including
abnormal connection patterns between peripheral indicators and abnormally increased Return on Equity (ROE) and Return on Assets
core indicators. (ROA), simultaneously decreased Accounts Receivable Turnover Rate,
Based on interaction effect analysis, this study proposes an and imbalanced Operating Cash Flow to Sales Revenue ratio. The
adaptive threshold adjustment mechanism based on feature HFSL framework achieves a detection rate of 87.3% for this type of
interaction intensity: anomaly, outperforming traditional methods by approximately 23
percentage points. Taking Company A as an example, its ROE growth
  rate exceeded the industry average by twofold for three consecutive
θ adj ( Xi )=θ base ( Xi )×  1+∑ω i,j ×I ( |Xj −µ j|>θ base ( Xj ))  quarters, while its Accounts Receivable Turnover Rate continued to
 j≠i 
decline, and its Operating Cash Flow to Net Profit ratio fell to 0.32
(industry average: 0.78). The HFSL framework successfully detected
this anomaly and raised the anomaly score to 0.87 (threshold: 0.65).
where θ adj ( Xi ) is the adjusted threshold for feature Xi, Subsequent audits confirmed that the company inflated revenue by
θ base ( Xi ) is the base threshold, ω i,j is the interaction weight approximately 270 million yuan through fictitious overseas
()
between feature values i and j, and I · is an indicator function customer orders.
taking the value 1 when feature j exceeds its base threshold and 0 Expense concealment anomalies account for 21.7%, primarily
otherwise. This mechanism enables the model to dynamically manifesting as abnormally increased gross profit margin and net profit
adjust detection thresholds according to the degree of collaborative margin, with period expense ratio significantly below industry average
anomalies across multiple indicators, increasing F1-score by 3.5% levels. This type of anomaly is typically achieved through improper
and reducing false alarm rate by 12.7% in experimental validation, expense capitalization, delayed cost recognition, and other means. In
verifying the important value of feature interaction analysis in Company B’s case, the model captured its R&D expense capitalization
enhancing anomaly detection performance. rate surging to 83% (compared to a five-year average of 36%), while
Feature interaction effect analysis not only enhances model its period expense ratio was 12 percentage points below industry
interpretability but also provides theoretical foundations for peers, despite revenue growth rates similar to industry averages. This
constructing more precise financial anomaly detection systems. uncoordinated financial performance triggered the model’s multi-
The research finds that anomaly detection models considering dimensional anomaly scoring mechanism, successfully identifying
feature interaction effects outperform models focusing solely on potential financial manipulation behavior.
single features when capturing complex financial anomaly Asset overvaluation and liability understatement anomalies
patterns, especially in identifying carefully designed financial account for 17.4 and 15.2%, respectively. Both types relate to improper
fraud cases. This finding provides insights for refining accounting valuation of balance sheet items but exhibit significant differences in
data anomaly detection theory, indicating that future research financial indicator performance. Asset overvaluation primarily affects
should place greater emphasis on collaborative analysis of asset turnover indicators, as in Company C’s case, where inventory
multidimensional financial indicators rather than simple single- turnover rate remained in the bottom 10% of the industry for six
indicator threshold monitoring. consecutive quarters, while sales revenue growth was at mid-to-upper
From the perspective of industry differences, the interaction industry levels. This mismatch was successfully identified by the
intensity between ROE and ROA in the financial industry (0.096) model as potential inventory value overestimation. Liability
is significantly higher than in manufacturing (0.081), while the understatement primarily manifests as abnormally increased current
interaction intensity between Inventory Turnover Rate and Gross ratio and abnormally decreased leverage ratio, as in Company D’s case,
Profit Margin in manufacturing (0.074) is higher than in other where contingent liabilities were not accrued according to regulations,
industries. These industry characteristic differences further causing its solvency indicators to significantly outperform industry
support this study’s approach of constructing industry-specific average levels.
anomaly detection models, adopting differentiated feature The most complex composite manipulation anomalies, though
interaction patterns for anomaly identification tailored to different accounting for only 7.1%, present the greatest detection difficulty, with
industry characteristics. an average detection rate of merely 68.2%. This type of anomaly
Frontiers in Applied Mathematics and Statistics 22 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
simultaneously involves manipulation of multiple financial statement anomalies, with approximately 27% experiencing negative events
items, as in Company E’s case, where revenue inflation and liability within the subsequent 8 quarters. The HFSL framework improves
understatement coexisted. Although the anomaly degree of individual high-risk case identification accuracy by 18.6% compared to
indicators was relatively small, the relationships between multiple traditional methods, with early identification of medium-risk cases
indicators violated financial logical consistency. The HFSL framework advancing by an average of 1.7 quarters, significantly enhancing
achieved effective identification of such complex anomalies through warning value.
feature interaction mechanisms and financial domain knowledge The HFSL framework demonstrates differentiated detection
constraints, which traditional single-indicator monitoring methods timeliness for different types of anomalies, detecting revenue
struggle to accomplish. inflation anomalies an average of 3.2 quarters in advance, expense
The research also found that different industries exhibit concealment 2.8 quarters in advance, asset overvaluation and
preferences for different fraud patterns. Manufacturing shows a higher liability understatement 2.4 and 2.6 quarters respectively, while
proportion of asset overvaluation anomalies (26.3%), primarily composite manipulation only 1.8 quarters, reflecting the
concentrated in inventory and fixed asset valuation areas; the complexity and concealment of the latter. Temporal analysis
information technology industry predominantly features revenue reveals a potential “financial anomaly waterfall effect,” with
inflation (52.1%), reflecting the complexity of revenue recognition in approximately 83% of major financial anomaly cases in the
this industry; while the financial industry shows more prominent research sample beginning with minor anomalies in single
liability understatement (25.7%), involving risk provision accrual and indicators, subsequently spreading to related indicators, and
financial asset valuation issues. This industry differentiation further ultimately forming systemic risks. This finding may provide
confirms the necessity of the industry calibration mechanism in the inspiration for improving regulatory practices: early identification
HFSL framework, which enables more accurate identification of and intervention in initial anomaly signals may interrupt the
industry-specific anomaly patterns by considering chain reaction of financial anomalies, preventing the formation of
industry characteristics. difficult-to-reverse systemic problems. By capturing early
characteristics of anomaly diffusion patterns, the HFSL framework
6.3.2 Temporal evolution characteristics of provides longer response windows and more reliable decision-
anomaly detection making bases for financial risk warnings.
Financial anomalies typically exhibit progressive characteristics
rather than sudden events. Through temporal analysis, this study
6.4 Model robustness and generalization
identifies three typical evolution patterns. Progressive deterioration is
capability assessment
the most common pattern, accounting for approximately 64%,
characterized by gradually increasing anomaly severity over time,
typically beginning with small-scale financial manipulation that 6.4.1 Cross-industry adaptability validation
subsequently accumulates and expands. A typical case is Company F, The HFSL framework demonstrates differentiated but overall
whose anomaly score gradually rose from 0.42 to 0.97 over 8 quarters stable performance across different industries. Detection performance
before its financial problems became public, with the HFSL framework is best in the financial industry (F1 = 0.872), good in manufacturing
successfully providing warnings an average of 4 quarters before the and information technology industries (F1 scores of 0.817 and 0.831
anomaly became public. Sudden anomalies account for approximately respectively), while relatively lower in the construction and real estate
22%, characterized by rapidly escalating anomaly scores over a short industry (F1 = 0.776). These differences primarily stem from industry-
period, typically related to major accounting errors, as in Company specific financial characteristics and anomaly patterns. For example,
G’s case, where the anomaly score surged from 0.38 to 0.83 within one the strictly regulated environment and standardized financial
quarter. Although such anomalies are difficult to predict in advance, reporting formats in the financial industry facilitate anomaly pattern
the HFSL framework controlled identification delay to an average of identification, while the complexity of asset valuation and diversity in
1.2 quarters, significantly outperforming traditional methods. Cyclical revenue recognition in the construction and real estate industry
fluctuations account for approximately 15%, characterized by anomaly increase detection difficulty.
scores fluctuating around threshold edges, common in enterprises Model generalization capability is evaluated using leave-one-
with seasonal businesses, with the HFSL framework effectively industry-out cross-validation, training with data from 9 industries and
controlling the false alarm rate for such anomalies to 8.7% through its testing on the remaining industry. Results show that performance
seasonal adjustment mechanism. decline after industry calibration is controlled within 7.5%,
Based on anomaly temporal characteristics and intensity, this significantly outperforming baseline methods’ 12.3%. Particularly in
study constructs a risk grading model, categorizing anomaly cases into cross-industry early detection rate, the industry calibration
high-risk, medium-risk, and observation classes. High-risk cases mechanism improves performance by 14.6%, confirming the
exhibit anomaly scores consistently exceeding thresholds with upward effectiveness of the hierarchical feature fusion design in capturing
trends, or sudden anomaly intensity exceeding thresholds by over anomaly characteristics across different industries.
30%, with approximately 83% experiencing major negative events
within the subsequent 3 quarters. Medium-risk cases have anomaly 6.4.2 Noise sensitivity and threshold dynamic
scores slightly exceeding thresholds or fluctuating around threshold adjustment effects
edges, with approximately 48% experiencing negative events within To test model stability in noisy environments, this study designs
the subsequent 6 quarters. Observation-class cases have anomaly three-level noise interference experiments, introducing 5, 10, and 15%
scores below thresholds but continuously rising, or exhibiting isolated random noise into the original data. Experimental results show that
Frontiers in Applied Mathematics and Statistics 23 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
Data availability statement
the HFSL framework’s performance decreases by only 1.2% at the 5%
noise level and by 9.7% in the 15% high-noise environment,
significantly outperforming the best baseline method’s 18.3%, The original contributions presented in the study are included in
indicating that the hierarchical fusion structure possesses strong the article/supplementary material, further inquiries can be directed
resistance to data noise. to the corresponding author.
Regarding threshold adjustment, this study compares the effects
of fixed thresholds versus adaptive dynamic thresholds. The dynamic
Author contributions
threshold mechanism demonstrates superiority across different
industries and periods, improving F1-score by an average of 3.5%, and
particularly reducing false alarm rates by 12.7% on test sets with YZ: Supervision, Methodology, Writing – review & editing,
imbalanced anomaly proportions. This result validates the Conceptualization, Software, Writing – original draft, Visualization,
effectiveness of the adaptive threshold method based on Gaussian Investigation, Project administration, Funding acquisition, Validation,
mixture models in processing financial data anomaly detection, Data curation. BD: Validation, Software, Writing – review & editing,
providing reliable guidance for threshold selection in Supervision, Resources, Formal analysis, Funding acquisition,
practical applications. Writing – original draft.
6.4.3 Temporal stability and concept drift analysis
Funding
Financial fraud patterns evolve continuously in response to
regulatory changes and technological advancements. Our temporal
stability analysis reveals that the HFSL framework maintains robust The author(s) declare that financial support was received for the
performance despite these evolving patterns. When tested on quarterly research and/or publication of this article. Research on the problems
segments spanning 2016–2020, the framework demonstrated and countermeasures of environmental accounting information
remarkable stability with F1-score variations contained within ±5% disclosure of listed companies from the perspective of low-carbon
across different periods. economy (WLYB202315).
The framework’s resilience to concept drift was evaluated through
three scenarios. In sudden drift scenarios simulating major regulatory
Conflict of interest
changes, the HFSL framework detected 89% of pattern shifts within
two quarters and recovered to baseline performance levels with
minimal degradation (F1-score maintained above 0.78 during BD was employed by Chengdu Huawei Technologies Co., Ltd.
transitions). For gradual drift representing natural evolution of fraud The remaining author declares that the research was conducted in
techniques, performance degradation was limited to 6.2% over eight- the absence of any commercial or financial relationships that could
quarter periods. The dual-channel architecture proved particularly be construed as a potential conflict of interest.
effective, with the long-term channel capturing evolving trends while
the short-term channel maintained sensitivity to immediate anomalies.
Generative AI statement
Analysis of real-world pattern evolution revealed significant changes
following the 2018 regulatory enhancements in China. The model
successfully adapted to a 15% shift in the relative importance of cash flow The authors declare that no Gen AI was used in the creation of
versus accrual-based indicators in fraud detection. This adaptation was this manuscript.
achieved through the framework’s dynamic feature weighting mechanism, Any alternative text (alt text) provided alongside figures in this
which automatically adjusted based on recent detection patterns. article has been generated by Frontiers with the support of artificial
Compared to static models, the HFSL framework with drift intelligence and reasonable efforts have been made to ensure accuracy,
adaptation showed an 11.3% improvement in average performance including review by the authors wherever possible. If you identify any
over the five-year test period. The incremental learning strategy issues, please contact us.
effectively balanced stability with adaptability, preventing catastrophic
forgetting while incorporating emerging fraud patterns. These results
Publisher’s note
demonstrate that the framework’s adaptive capabilities make it
particularly suitable for deployment in dynamic regulatory
environments where fraud patterns continuously evolve. All claims expressed in this article are solely those of the
Future research directions include: (1) extending the framework authors and do not necessarily represent those of their affiliated
to other sectors beyond Chinese listed companies, (2) developing organizations, or those of the publisher, the editors and the
semi-supervised variants that can incorporate limited labeled data, reviewers. Any product that may be evaluated in this article, or
and (3) exploring real-time anomaly detection capabilities for claim that may be made by its manufacturer, is not guaranteed or
continuous monitoring systems. endorsed by the publisher.
References
1. Ellili N, Nobanee H, Haddad A, Alodat AY, AlShalloudi M. Emerging trends in 2. Xu Y. A study on the effectiveness of the independent director system on the
forensic accounting research: bridging research gaps and prioritizing new frontiers. J governance of financial fraud phenomenon: taking Kangmei pharmaceutical as an
Econ Criminol. (2024) 4:100065. doi: 10.1016/j.jeconc.2024.100065 example. SHS Web Conf. (2024) 188:01024. doi: 10.1051/shsconf/202418801024
Frontiers in Applied Mathematics and Statistics 24 frontiersin.org

Zhang and Duan 10.3389/fams.2025.1628652
3. Kaur B, Sood K, Grima S. A systematic review on forensic accounting and its 19. Gui J, Chen T, Zhang J, Cao Q, Sun Z, Luo H, et al. A survey on self-supervised
contribution towards fraud detection and prevention. J Financ Regul Compliance. (2023) learning: algorithms, applications, and future trends. IEEE Trans Pattern Anal Mach
31:60–95. doi: 10.1108/JFRC-02-2022-0015 Intell. (2024) 46:9052–71. doi: 10.1109/TPAMI.2024.3415112
4. Ramzan S. Comparison of financial distress prediction models using financial 20. Duan J., Zhao H., Zhou Q., Qiu M., Liu M. A study of pre-trained language models
variables. In Proceedings of the 2023 international conference on electrical, computer in natural language processing. In Proceedings of the 2020 IEEE international
and energy technologies (ICECET). New York: IEEE, (2023); pp. 1–7. conference on smart cloud (SmartCloud). Cambridge: IEEE, (2020); pp. 116–121.
5. Rao RK, Mandhala VN. Unveiling financial fraud: a comprehensive review of 21. Kim H, Kim S, Min S, Lee B. Contrastive time-series anomaly detection. IEEE
machine learning and data mining techniques. Ingénierie des systèmes d information. Trans Knowl Data Eng. (2024) 36:5053–65. doi: 10.1109/TKDE.2023.3335317
(2024) 29:2309–34. doi: 10.18280/isi.290620
22. Hojjati H, Ho TKK, Armanfard N. Self-supervised anomaly detection in computer
6. Chen H., Zhao Q., Lu W., Gu S., Jin W., Liu G., et al. Application of self-supervised vision and beyond: a survey and outlook. Neural Netw. (2024) 172:106106. doi:
autonomous agent framework for digital transformation of elder well potentials 10.1016/j.neunet.2024.106106
discovery. In Proceedings of the ADIPEC. Berlin: SPE, (2024).
23. Chen Y, Wu Z. Financial fraud detection of listed companies in China: a machine
7. Shwartz Ziv R, LeCun Y. To compress or not to compress—self-supervised learning learning approach. Sustainability. (2022) 15:105. doi: 10.3390/su15010105
and information theory: a review. Entropy. (2024) 26:252. doi: 10.3390/e26030252
24. Xiuguo W, Shengyong D. An analysis on financial statement fraud detection for
8. Ali A, Abd Razak S, Othman SH, Eisa TAE, Al-Dhaqm A, Nasser M, et al. Financial Chinese listed companies using deep learning. IEEE Access. (2022) 10:22516–32. doi:
fraud detection based on machine learning: a systematic literature review. Appl Sci. 10.1109/ACCESS.2022.3153478
(2022) 12:9637. doi: 10.3390/app12199637
25. Zhang K, Wen Q, Zhang C, Cai R, Jin M, Liu Y, et al. Self-supervised learning for
9. Dechow PM, Ge W, Larson CR, Sloan RG. Predicting material accounting time series analysis: taxonomy, Progress, and prospects. IEEE Trans Pattern Anal Mach
misstatements*. Contemp Account Res. (2011) 28:17–82. doi: 10.1111/j.1911-3846.2010.01041.x Intell. (2024) 46:6775–94. doi: 10.1109/TPAMI.2024.3387317
10. Beneish MD. The detection of earnings manipulation. Financ Anal J. (1999) 26. Tipirneni S, Reddy CK. Self-supervised transformer for sparse and irregularly
55:24–36. doi: 10.2469/faj.v55.n5.2296 sampled multivariate clinical time-series. ACM Trans Knowl Discov Data. (2022)
11. Kirkos E, Spathis C, Manolopoulos Y. Data mining techniques for the detection of fraudulent 16:1–17. doi: 10.1145/3516367
financial statements. Expert Syst Appl. (2007) 32:995–1003. doi: 10.1016/j.eswa.2006.02.016 27. Yang X, Zhang Z, Cui R. Timeclr: a self-supervised contrastive learning framework
12. Perols J. Financial statement fraud detection: an analysis of statistical and machine for univariate time series representation. Knowl-Based Syst. (2022) 245:108606. doi:
learning algorithms. Audit J Pract Theory. (2011) 30:19–50. doi: 10.2308/ajpt-50009 10.1016/j.knosys.2022.108606
13. Cecchini M, Aytug H, Koehler GJ, Pathak P. Detecting management fraud in 28. Xu R, Yao D, Zhou M. Does the development of digital inclusive finance improve
public companies. Manag Sci. (2010) 56:1146–60. doi: 10.1287/mnsc.1100.1174 the enthusiasm and quality of corporate green technology innovation? J Innov Knowl.
(2023) 8:100382. doi: 10.1016/j.jik.2023.100382
14. Bao Y, Ke B, Li B, Yu YJ, Zhang J. Detecting accounting fraud in publicly traded
U.S. firms using a machine learning approach. J Account Res. (2020) 58:199–235. doi: 29. Yang X., Juyang AN, Lin G. Local government debt and corporate strategic
10.1111/1475-679X.12292 alliances: evidence from chinese listed companies. Berlin: Springer. (2025).
15. Jing L, Tian Y. Self-supervised visual feature learning with deep neural networks: a survey. 30. Li Z, Chen B, Lu S, Liao G. The impact of financial institutions’ cross-
IEEE Trans Pattern Anal Mach Intell. (2021) 43:4037–58. doi: 10.1109/TPAMI.2020.2992393 shareholdings on risk-taking. Int Rev Econ Finance. (2024) 92:1526–44. doi:
10.1016/j.iref.2024.02.080
16. Jaiswal A, Babu AR, Zadeh MZ, Banerjee D, Makedon F. A survey on contrastive
self-supervised learning. Technologies (Basel). (2020) 9:2. doi: 10.3390/ 31. Wang Q, Lee E, Wang K, Zhang X. The effect of government industrial policies on
technologies9010002 corporate accounting conservatism. J Account Public Policy. (2022) 41:106960. doi:
10.1016/j.jaccpubpol.2022.106960
17. Kumar P, Rawat P, Chauhan S. Contrastive self-supervised learning: review,
progress, challenges and future research directions. Int J Multimed Inf Retr. (2022) 32. Zhang C, Li Z, Xu J, Luo Y. Accounting information quality, firm ownership and
11:461–88. doi: 10.1007/s13735-022-00245-6 technology innovation: evidence from China. Int Rev Financ Anal. (2024) 93:103118.
doi: 10.1016/j.irfa.2024.103118
18. Liu X, Zhang F, Hou Z, Mian L, Wang Z, Zhang J, et al. Self-supervised learning:
generative or contrastive. IEEE Trans Knowl Data Eng. (2021) 35:857–76. doi: 33. Altman E. I. Financial ratios, discriminant analysis and the prediction of corporate
10.1109/TKDE.2021.3090866 bankruptcy. J. Finance. (1968) 23:589–609.
Frontiers in Applied Mathematics and Statistics 25 frontiersin.org