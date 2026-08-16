---
conversion_metadata:
  converted_at: "2026-07-21T09:02:50Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Tonati et al.pdf"
  source_pdf_sha256: "668e711e3992230ebf4e17e8be69261573fba42fc3b7a63e107823278dd717eb"
  page_count: 27
  markdown_char_count: 164603
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Machine Learning (2025) 114:230
https://doi.org/10.1007/s10994-025-06880-4

Counterfactual ensembles for interpretable churn prediction: 
from real-world to privacy-preserving synthetic data

Samuele Tonati1,2 · Marzio Di Vece1,3 · Fosca Giannotti1 · Roberto Pellungrini1

Received: 23 April 2025 / Revised: 16 July 2025 / Accepted: 25 August 2025 / 
Published online: 15 September 2025
© The Author(s) 2025

Abstract
Counterfactual  explanations  identify  minimal  input  changes  needed  to  alter  a  machine 
learning model’s prediction, offering actionable insights in tasks like churn analysis. How-
ever, existing methods often produce counterfactuals that vary in quality, coherence, and 
plausibility, limiting their practical value. We propose an ensemble evaluation framework 
that integrates multiple generation techniques and ranks their outputs using a tunable scor-
ing  function  balancing  multiple  relevant  metrics.  Our  approach  addresses  two  key  de-
ployment scenarios: (i) in-house churn analysis, where decision-makers can interactively 
adjust  scoring  weights  for  tailored,  user-driven  explanations;  and  (ii)  outsourced  churn 
prediction, where counterfactuals must be generated on synthetic data to preserve privacy 
while  remaining  representative  of  real  cases.  Experiments  on  benchmark  churn  datasets 
demonstrate  that  our  ensemble  approach  improves  the  consistency,  interpretability,  and 
utility of counterfactuals across both real and synthetic settings, supporting more reliable 
and privacy-aware decision-making.

Keywords  Explainable AI · Counterfactual explanations · Churn analysis

Editors: Riccardo Guidotti, Anna Monreale, Dino Pedreschi.

Roberto Pellungrini

roberto.pellungrini@sns.it

Samuele Tonati
samuele.tonati@sns.it

Marzio Di Vece
marzio.divece@sns.it

Fosca Giannotti
fosca.giannotti@sns.it

1 
Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pisa, Italy
2  University of Pisa, Lungarno Antonio Pacinotti 43, 56126 Pisa, Italy
3

IMT School for Advanced Studies, Piazza San Francesco 19, 55100 Lucca, Italy

1 3

---

<!-- PAGE 2 -->

230  Page 2 of 27

1  Introduction

Customer  churn,  the  decision  by  clients  to  terminate  a  service,  is  a  pervasive  and  costly 
issue in many industries, particularly those offering subscription-based or contract-driven 
services. Identifying which customers are likely to churn is only the first step; businesses 
must also understand the underlying reasons behind customer attrition and how to intervene 
effectively. This makes churn analysis not just a predictive task, but a high-stakes decision-
making problem where interpretability and actionable insights are essential.

In  this  context,  Explainable  Artificial  Intelligence  (XAI)  has  emerged  as  a  powerful 
approach  to  bridge  the  gap  between  model  accuracy  and  human  understanding.  While 
machine learning (ML) models have demonstrated high performance in predicting churn, 
their increasing complexity often comes at the cost of transparency. As a result, many mod-
els become opaque to  the practitioners  who  rely on  them, creating  significant barriers to 
trust, accountability, and regulatory compliance (Ali et al., 2023). These concerns are espe-
cially  pressing  in  domains  like  churn  analysis,  where  decisions  directly  affects  customer 
engagement strategies and, ultimately, revenue.

XAI methods, and counterfactual explanations in particular, offer an intuitive and legally 
relevant1 solution (Bodria et al., 2023). By identifying the minimal changes in input fea-
tures required to flip a model’s prediction, counterfactual explanations support contrastive 
reasoning–answering the question: “What would need to change in a customer’s profile to 
prevent churn?” This form of explanation is not only intuitive but aligns with emerging legal 
requirements, such as those established under the GDPR2 and the AI Act3, concerning the 
right to explanation and transparency (Stepin et al., 2021; Guidotti, 2022). In the context 
of churn analysis, counterfactuals provide actionable recommendations that help retention 
officers develop personalized intervention strategies (Geiler et al., 2022; Joy et al., 2024).

However, the quality of counterfactuals can vary significantly across different generation 
techniques, with each method optimizing for different properties such as sparsity, plausibil-
ity, or diversity (Nauta et al., 2023). This heterogeneity poses a challenge when integrating 
XAI into practical churn workflows, especially in the absence of a standardized evaluation 
methodology tailored to the domain.

To address this challenge, we propose an ensemble evaluation framework specifically 
designed for churn prediction. Our framework integrates multiple counterfactual generation 
methods and ranks the resulting explanations using a dynamic, customizable scoring func-
tion. This function balances key counterfactual properties–proximity, sparsity, plausibility, 
and diversity–to surface the most relevant and realistic explanations with minimal compu-
tational overhead (Guidotti & Ruggieri, 2021). This design empowers practitioners to tailor 
explanations  to  the  specific  demands  of  churn  analysis,  where  certain  properties  such  as 
feasibility and minimality are particularly crucial.

Our approach supports two primary operational scenarios. In the first, churn analysis is 
conducted in-house, and the interpretability interface enables user-driven exploration. By 
tuning the scoring function, decision makers can prioritize explanation characteristics that 
align  with  business  goals,  facilitating  targeted,  customer-specific  interventions  based  on

1 For Reference see GDPR articles 12-15 and 22.
2 See previous footnote.
3 For Reference see AI Act articles 13, 50 regarding transparency provisions for high-risk system providers 
and deployers and Article 86 regarding the right to explanation for individual decision-making.

---

<!-- PAGE 3 -->

Page 3 of 27  230

model output. In the second scenario, the prediction of churn is outsourced to third-party 
providers4. These services can include machine learning-based churn prediction, analysis 
of explanations, and intervention strategy design. In such cases, privacy considerations pre-
vent the direct sharing of real customer data. To overcome this constraint, we extend our 
framework to operate in privacy-preserving settings by employing synthetic datasets that 
retain the statistical properties of real data while eliminating personally identifiable infor-
mation (Qian et al., 2024). While generally faithful to the real counterpart, synthetic data 
do not guarantee faithful counterfactuals. To ensure that synthetic counterfactuals remain 
aligned  with  their  real-data  counterparts,  we  introduce  an  optimization  strategy  for  our 
ensemble method that minimizes the Kullback-Leibler (KL) divergence between the distri-
butions of selected counterfactuals from real and synthetic sources. This alignment ensures 
that  third  parties  receive  explanations  that  are  both  representative  of  real  situations  and 
privacy-compliant.

We validate our ensemble framework using four publicly available churn datasets, dem-
onstrating that it improves the robustness, interpretability, and practical utility of counter-
factual  explanations.  Our  results  show  that  the  method  is  effective  in  both  in-house  and 
privacy-sensitive  scenarios,  supporting  trustworthy,  human-centered  decision  making  in 
customer retention workflows.

1.1  Contributions

This work makes the following key contributions:

● Domain-specific ensemble evaluation framework: We introduce an ensemble-based 
framework  for  evaluating  and  selecting  counterfactual  explanations  tailored  to  churn 
prediction, integrating multiple generation methods and ranking them using a scoring 
function.

● Customizable multi-criteria selection: The scoring function balances proximity, spar-
sity, plausibility, and diversity, enabling practitioners to adapt the evaluation process to 
domain-specific needs.

● Support  for  user-driven  counterfactual  exploration:  In  the  in-house  setting,  our 
framework allows interactive control over explanation generation, supporting interpret-
able, client-specific interventions.

● Privacy-preserving explanation generation with distributional alignment: For the 
outsourced prediction of churn, we enable the use of synthetic data to protect personal 
information  while  ensuring  the  fidelity  of  the  explanation.  This  is  achieved  through 
a  KL-divergence-based  optimization  strategy  that  aligns  the  distributions  of  real  and 
synthetic counterfactuals.

● Comprehensive empirical validation: We validate the approach in four public churn 
datasets, showing improved robustness, interpretability, and compliance with privacy in 
both internal and external deployment settings.

4 Outsourcing Churn Analysis and Retention is a common practice. Companies specialized in Churn Analyt-
ics include InfoSysBPM, iQor and Konsyg, etc.

---

<!-- PAGE 4 -->

230  Page 4 of 27

2  Related works

Early research on churn modeling has primarily emphasized predictive accuracy, employ-
ing a range of supervised and unsupervised learning methods to analyze customer behavior, 
transaction histories, and demographic variables (Burez & Poel, 2008; Maldonado et al., 
2020; De Bock & De Caigny, 2021; Adhikary & Gupta, 2020). These models often perform 
well  in  identifying  likely  churners,  but  their  complexity  tends  to  obscure  the  underlying 
decision logic, limiting their usefulness in real-world retention strategies (Dong et al., 2018; 
Mishra & Reddy, 2017; Petkovski et al., 2016).

To address the interpretability gap, counterfactual explanations have emerged as a prom-
ising post-hoc approach within Explainable AI (XAI). These methods identify the minimal 
changes needed in a feature vector to alter a model’s decision (Bodria et al., 2023). Although 
similar in structure to adversarial examples, counterfactuals are intended for human con-
sumption and emphasize informative properties such as proximity, sparsity, plausibility, and 
diversity (Freiesleben, 2022; Guidotti, 2022).

Counterfactual reasoning is especially well-suited to personalized decision-making con-
texts, including churn management, as it allows businesses to identify individual-level inter-
ventions that may prevent customer loss (Lemon & Verhoef, 2016; Tung, 2024). However, 
most XAI applications in churn analysis have relied on feature importance techniques, such 
as SHAP or LIME (Joy et al., 2024; Theodoridis & Tsadiras, 2022; Xiong et al., 2023), with 
relatively few studies exploring the use of counterfactuals for this domain.

From  a  methodological  standpoint,  optimization-based  approaches  to  counterfactual 
generation are well-established (Carrizosa et al., 2024; Kanamori et al., 2021; Tan et al., 
2021). However, existing studies typically focus on single-instance generation and do not 
consider ensemble-based selection strategies. To the best of our knowledge, no prior work 
has systematically applied ensemble evaluation of counterfactuals to churn prediction.

Privacy for churn prediction and analysis has been a focus of several works. In the article 
by Coimbra et al. (2024), edge computing is used to process data for Churn analysis locally, 
without  transmitting  users  data. A  similar  approach  is  adopted  by  Huh  and  Lee  (2024), 
where privacy is guaranteed via Federated Learning, specifically in the telecommunication 
sector. In both these works, the focus is in avoiding data transmission between nodes, thus 
preventing sensible information from being shared outside of the first-party managing the 
churn prediction. This suggests, as it happens in many practical cases, that churn prediction 
is either performed directly by the data owner or, in case of outsourcing, is performed using 
synthetic data, generated to replicate the statistical properties of real datasets while obfus-
cating personal identifiers (Assefa et al., 2020). Empirical evidence from domains such as 
healthcare suggests that models trained on synthetic data can yield comparable performance 
to those trained on real-world data (Rankin et al., 2020). Moreover, synthetic data genera-
tion is increasingly being combined with differential privacy guarantees to enhance protec-
tion without compromising utility (Bellovin et al., 2019). Hyrup et al. (2025) provides a 
comprehensive overview of privacy-preserving techniques for synthetic data in the context 
of health related data. Although a different domain, it still provides a good base to under-
stand how synthetic data can be used to enhance privacy in any data analysis or machine 
learning process. The protection offered by synthetic data can still however be foiled, as 
proved by Ganev and De Cristofaro (2025). In this work, the authors devise an attack model 
that  leverages  the  weaknesses  of  distance  based  privacy  metrics  to  foil  the  protection  of

---

<!-- PAGE 5 -->

synthetic data. However, the adversarial model adopted in the paper assumes a worst-case 
scenario analysis, thus requiring the leaking of a lot of different data and parameters in order 
to be effective.

Page 5 of 27  230

3  Problem definition

3.1  Background

Churn prevention encompasses all the actions that a company puts into place to prevent the 
loss of customers. The first and most important part of any churn prevention strategy lies in 
detecting which customers will likely interrupt their relationship with the company, given 
their current status. A churn officer has then the duty of interacting with these customers in 
order to find possible actions to prevent them from churning. This task can be modeled as 
a binary classification task (Geiler et al., 2022) where a machine learning model is used to 
predict which customers are the ones likely to churn.

Rd  where  each  customer  is  represented  by  a  d 
Formally,  given  a  feature  space 
dimensional vector x = (x1, . . . , xn)
 where 1 indicates 
 and a label space 
a  customer  churning  and  0  a  customer  not  churning,  we  assume  to  observe  a  dataset  of

X ⊆
∈ X

0, 1

=

Y

{

}

=
N  i.i.d  samples 
fier) is a function f :
minimization.

D

(xi, yi)

{
X → Y

iid
∼

N
i=0
}
 usually trained over a training set

P (x, y) over

X × Y

. A  churn  predictor  (or  classi-
Dtrain via empirical risk

In this context, counterfactual explanations are extremely useful from a business’ per-
spective: firstly, counterfactual explanations help identify the minimal changes x needed to 
retain a customer; for example, if the model indicates that a customer is likely to churn, a 
counterfactual explanation might reveal that offering a small discount, offering a particular 
product or improving service quality could change the prediction to retention. This allows 
businesses to implement precise interventions that are cost-effective and efficient. Secondly, 
the  interpretability  offered  by  counterfactual  explanations  builds  trust  among  business 
stakeholders. Unlike explanatory methods that might provide abstract or general insights, 
such as in the case of global explanations, counterfactuals show specific scenarios and out-
comes, making it easier for non-technical stakeholders to understand and trust the model’s 
recommendations. This trust is vital in securing support and commitment from stakehold-
ers for data-driven strategies and ensuring their successful implementation. Counterfactual 
explanations have not been explored as a solution for the problem of specific optimization 
strategies in churn prevention (Joy et al., 2024; Theodoridis & Tsadiras, 2022; Xiong et al., 
2023).

Formally, given an instance x and the corresponding churn prediction f (x) = y a coun-
terfactual explanation for x is a point x′ such that f (x′) = y′ with y
= y′, i.e. the classifier’s 
output flips from its original prediction from y to y′. To find a minimal counterfactual, given 
a distance d(x, x∗), we can solve the optimization problem:

x′ = arg min
x∗
= f (x′)

s.t. f (x)

d(x, x∗)

(1)

---

<!-- PAGE 6 -->

230  Page 6 of 27

where  d(x, x∗)  is  commonly  chosen  to  be  the  (L1)  or  (L2)-norm.  Many  counterfactual 
explanation  methods.  However,  depending  on  what  counterfactual  method  one  chooses 
(Guidotti,  2022),  the  explanations  obtained  may  rely  on  specific  optimization  strategies 
that  are  variations  or  approximations  of  formulation  1  and  therefore  explore  only  some 
particular aspect of the importance of a churn officer. Moreover, many counterfactual meth-
ods  produce  multiple  counterfactual  instances  for  any  given  x.  We  can  therefore  define 
X ′ =
 as the set of valid counterfactuals produced by any method for instance 
x.

x′1, . . . , x′v}

{

3.2  k-CEM: counterfactual ensemble method

To tackle similar problems, Guidotti et al. (Guidotti & Ruggieri, 2021) proposed an ensem-
ble method that leverages the strengths of multiple counterfactual explainers to cover a set 
of desirable properties, such as minimality, actionability, stability, diversity, plausibility, and 
discriminative power. Their approach demonstrates the efficacy of boosting weak explainers 
into a powerful ensemble that is both model-agnostic and data-agnostic, capable of handling 
various data types including tabular data, images, and time series.

Building upon this idea, we propose an ensemble approach that operates ex-post as an 
evaluation and selection mechanism, called k-CEM. Our method is designed to identify the 
optimal set of counterfactual examples by employing a linear combination score of various 
metrics, that reflect on the possible aspects that a churn officer would explore in a churn pre-
diction model. In contrast to the ensemble proposed by Guidotti and Ruggieri (2021), which 
combines results through a diversity-driven selection function, our framework introduces a 
more nuanced selection score. This approach not only refines the selection process but also 
ensures that the chosen counterfactuals align closely with the desired properties - thereby 
improving the interpretability and reliability of the explanations provided – and that can be 
aptly tweaked by practitioners to give more emphasis to a specific metric. Churn analysis, 
however, is often outsourced to specialized organizations. In such circumstances, privacy 
concerns often demand the use of protection mechanism, such as for example the use of 
synthetic data. Synthetic data can be shared outside the organization for analysis (Hyrup et 
al., 2025). However, while synthetic data is generated from real data and therefore similar 
in general properties, it usually provides less accurate models and far less reliable explana-
tions. This means that third-party churn analysts cannot devise realistic customer retention 
strategies based on these explanations. Thanks to the selection function that we devise, it is 
possible to use k-CEM to improve churn prediction procedure in such a privacy-aware set-
ting by providing a tool to interact with outsource churn analysts without compromising the 
quality of the explanations. To do this, we can exploit the selection function on synthetic data 
with a KL-minimization strategy (Section 3.4) to find the best parameters to produce expla-
nations that are as close as possible to realistic explanations on real data. Let us define set of 
x′. With 
counterfactual explanation methods as E =
slight abuse of notation, we indicate with E(f, x, y′) =
. Our 
proposal is to score the counterfactual explanations produced by an ensemble of counterfac-
tual methods E using evaluation metrics that align with desired properties in the context of 
Churn analysis. The pseudocode of our approach is given in Algorithm 1.

where ei : (f, x, y′)
e1(f, x, y′), . . . , eq(f, x, y′)

e1, . . . , eq}
{

→

}

{

---

<!-- PAGE 7 -->

Page 7 of 27  230

Algorithm 1  k-CEM: k-Counterfactual Ensemble Method

For  any  given  instance,  once  a  set  of  valid  counterfactual  is  obtained,  k-CEM  allows 
the user to define a selection score (Section 3.3) and weights of a set of metrics M. The 
priority of each metric is user-defined, therefore the user is able to modify the scores and 
interact  with  the  explanations,  without  having  to  recompute  them.  This  point  is  crucial, 
and is the reason for the ensemble of methods E: by increasing the number and diversity of 
counterfactuals, the selection phase of k-CEM is able to exploit the representativeness of 
the counterfactual set X ′ without overloading the user with information, presenting a set of 
explanations that answer specific user needs as defined by the metrics M. The set of parame-
ters wi is main"handle"that a user can leverage to interact with k-CEM, modifying priorities 
of metrics and exploring the space of explanations. We remark that all the explanations in 
k-CEM are valid, local explanations. While global or group-level counterfactuals (Warren 
et al., 2024) offer scalability and coherence, our method deliberately adheres to instance-
specific counterfactuals to guarantee perfect validity and actionability in a customer-reten-
tion  context.  Group  explanations  risk  diluting  personalized  recommendations–potentially 
yielding  suggestions  that  are  suboptimal  or  invalid  for  individuals  at  the  periphery  of  a 
heterogeneous  subgroup.  With  our  method,  we  ensure  semantic  consistency  and  predic-
tive fidelity, while remaining compatible with privacy-preserving techniques (e.g., synthetic 
data) to safeguard confidentiality without compromising the precision of each explanation. 
The framework in which k-CEM is applied is described in Fig 1. We envision k-CEM to be 
at the center of two possible usage settings: first-party churn analysis or third-party churn 
analysis.

---

<!-- PAGE 8 -->

230  Page 8 of 27

Fig. 1  Churn analysis and explanation workflow with k-CEM

– First-party In first-party mode, k-CEM can be used by an organization internal per-
sonnel to perform in-house churn analysis, based on machine learning models trained 
directly  on  the  data  gathered  and  managed  by  the  organization.  In  this  scenario,  the 
selection score of k-CEM allows the internal churn manager to interact with the expla-
nations, modifying the selection score (Section 3.3) to obtain the explanation that best 
suit the needs of the organization. This allows the churn manager to develop personal-
ized intervention strategies by interacting with k-CEM at a reduced computational cost.
 – Third-party In third-party mode, k-CEM can be used to interact with an external ana-
lyst that can devise an intervention strategy based on shared synthetic data. The orga-
nization needs only to share the synthetic dataset and the specifics of k-CEM, i.e., the 
set of metrics of interest, to the third-party analyst. The analyst will then find the best 
machine learning model to predict churn on the synthetic data and use k-CEM to explain 
such a model. The organization can then use the model and explanations provided by 
the external analyst to adjust k-CEM via KL-minimization strategy (Section 3.4) to find 
a set of parameters that can provide realistic explanations for the synthetic data. There-
fore the external analyst can build an intervention strategy based on such explanations, 
without ever accessing real data or real explanations.

In the following we are going to define the selection scores (Section 3.3) and KL-minimi-
zation strategy (Section 3.4) needed to make k-CEM function in the framework we devised, 
and we will provide the relevant counterfactual methods E and metrics M relevant to churn 
prediction (Section 3.6)

---

<!-- PAGE 9 -->

Page 9 of 27  230

3.3  Selection scores

In this work, we propose two distinct strategies for combining evaluation metrics: a linear 
selection score and a hierarchical selection score, as detailed below. The specific metrics 
and counterfactual generators underlying these scores are introduced in later sections, where 
they are defined in accordance with the application context.

3.3.1  Linear selection score

The selection score of each counterfactual explanation can be computed as a weighted lin-
ear combination of chosen metrics mi, which are defined so that a lower value indicates a 
higher counterfactual performance. This formulation allows a flexible synthesis of the most 
relevant aspects of counterfactual explanations based on application-specific priorities.

Formally, the score is defined as:

Linear Score =

wimi

M

|

|

i
∑

(2)

where wi are user-defined non-negative weights summing to 1, mi represents the i-th cho-
sen counterfactual metric and |M| is the number of the considered metrics. The final set of 
counterfactual explanations is obtained by ranking candidates according to their selection 
score in ascending order and selecting the top k instances, thus prioritizing explanations that 
best align with the weighted optimization criteria.

3.3.2  Hierarchical selection score

In addition to the linear combination, we propose a hierarchical selection score designed 
to prioritize metrics sequentially based on their relative importance. Rather than comput-
ing a single composite score by summing weighted metric values, our hierarchical proce-
dure operates in two distinct phases: allocation and refinement. Let M denote the number 
of  evaluation  metrics, 
  the  set  of  candidate  counterfactuals,  and  k  the  total  number  of 
explanations  to  select.We  assume  normalized  weights  wi  for  each  metric  mi,  such  that

D

M
i=1 wi = 1. For each metric, we then apply a ranking-based selection:
|

|

∑

Si = Top(ki,

D

, metrici)

(3)

where  Top(ki,
wi⌋
k
ki =

⌊

·

D

, mi)  returns  the  ki  candidates  from

. We aggregate these sets:

=

S

M

|

|

i=1
∪

Si,

that  optimize  metrici,  and

D

(4)

Because each metric draws from the same pool 
 may exceed k. To 
meet the overall budget, we apply a refinement step. We order the aggregated set according

, overlaps can occur:

|S|

D

---

<!-- PAGE 10 -->

230  Page 10 of 27

to the primary (highest-weight) metric, breaking ties by the next metric in weight order, and 
truncate to the top-k instances. This ensures that any over-selection is resolved by prioritiz-
ing the most important metric, then the next, and so on.

3.3.3  Comparison of scores

∑

The  Linear  selection  scores  pools  all  metrics  at  once  into  a  continuous  score 
s(x) =
i wimi(x)  and  selects  the  top-k  by  that  score.  In  contrast,  our  hierarchical 
approach discretizes the weight budget into per-metric quotas and enforces a minimal rep-
resentation from each metric before considering composite performance. If a single weight 
wj > 0.5,  the  hierarchical  method  reserves 
  slots  exclusively  based  on  metric  j, 
⌊
guaranteeing that at least half the explanations excel in that metric. In a pure linear score, 
setting wj = 0.5 similarly emphasizes j, but does not enforce a minimum count–other met-
rics  could  crowd  out  metric  j  if  their  combined  scores  exceed  those  of  metric-j-focused 
instances. The  hierarchical allocation and  refinement  scheme  thus  provides  interpretable, 
controllable guarantees on per-metric representation, complementing the more fluid trade-
offs of linear combination.

0.5k

⌋

3.4  KL divergence minimization for parameter tuning

In privacy-preserving settings, particularly when churn analysis is outsourced and real data 
cannot be directly used, it’s essential that synthetic counterfactual explanations closely mir-
ror those derived from real data. To address this challenge, we introduce a parameter tuning 
procedure based on minimizing the Kullback–Leibler (KL) divergence between the feature 
distributions of the real and synthetic counterfactual ensembles. Formally, we measure the 
distance between the feature distributions on real (
) datasets using the 
average Kullback-Leibler (KL) divergence:

) and synthetic (

R

S

¯DKL(

) =

S ∥ R

1
n

n

i=1
∑

DKL(Qi ∥

Pi)

(5)

where n is the number of features considered, and Qi, Pi denote the empirical distributions 
of the i-th feature in the synthetic and real counterfactual datasets, respectively. For con-
tinuous variables, Pi and Qi are estimated via histogram binning, with the number of bins 
determined by Sturges’ rule to balance bias and variance. In this minimization, we jointly 
wS1 , wS2 , wS3 , wS4 }
optimize  the  weight  vectors  w
, 
{
which govern the selection score functions for the real and synthetic datasets, respectively. 
Alternatively, one may fix w
, 
thereby  preserving  user-driven  interpretability  in  the  real  counterfactuals  while  allowing 
for privacy-preserving adaptation in the synthetic ones. However, to avoid overcomplicat-
. The 
ing the narrative, we focus in this work on the joint optimization of both w
optimization problem is formulated as:

according to user-defined preferences and optimize only w

wR1 , wR2 , wR3 , wR4 }
{

and  w

and w

=

=

R

R

R

S

S

S

min
,w
w
S
R

¯DKL (

(w

)

S

S

∥ R

(w

)) ,

R

(6)

---

<!-- PAGE 11 -->

Page 11 of 27  230

S

R

S

R

(w

(w

∑

) and

) denote the distributions of features of the counterfactuals selected 
where 
by the respective weight configurations. We solve this problem using a constrained optimi-
zation framework based on trust-region methods, which balance local model fidelity and 
global convergence guarantees. The optimization is performed under the normalization con-
i wi = 1  for  each  weight  vector,  ensuring  interpretability  and  comparability  of 
straint 
the resulting scores. To enhance robustness and mitigate sensitivity to local minima inher-
ent in the non-convex landscape of  ¯DKL, the optimization is repeated over 100 indepen-
dent random initializations. In each trial, the trust-region algorithm iteratively adjusts the 
weights within adaptive neighborhoods, progressively refining the solution toward a local 
minimum. The  final  parameter  configuration  is  selected  as  the  one  yielding  the  minimal 
KL divergence across all runs. This procedure provides a principled approach to calibrate 
the evaluation metrics, aligning synthetic data-driven counterfactual explanations with their 
real-data counterparts.

3.5  Coherence assessment via cluster-based distribution alignment

While the KL minimization procedure can be applied to the whole population of counterfac-
tuals generated (in both real and synthetic data), counterfactuals in churn analysis are often 
used to interpret individual behavior and devise client-retention strategies.

In light of this, we build upon the KL Divergence minimization framework introduced 
in Section 3.4, and we develop a cluster-based evaluation framework to assess the coher-
ence of counterfactual explanations derived from real and synthetic datasets. The procedure 
begins  by  partitioning  both  real  and  synthetic  datasets  into  distinct  subgroups  based  on 
observable behavioral patterns (e.g., the actual churn outcome). This stratification ensures 
that subsequent analyses are performed on contextually analogous subsets, thereby enabling 
fair  comparisons  between  the  two  data  modalities. Within  each  behavioral  subgroup,  we 
apply the K-Means clustering algorithm to independently group the real and synthetic indi-
viduals  into  five  clusters. These  clusters  serve  as  the  basis  for  forming  initial  baskets  of 
counterfactual  explanations.  Counterfactual  explanations  are  computed  for  each  cluster 
(real  and  synthetic)  and  KL  Divergence  minimization  is  performed  to  identify,  for  each 
pair of synthetic and real counterfactual baskets, the counterfactual explanations that are 
most similar in terms of their feature distributions. Subsequently, we quantify the coherence 
between the real and synthetic counterfactuals by comparing the clusters of data points and 
their respective counterfactual baskets. Two key measurements are obtained: the average 
Euclidean distance among the selected couples of synthetic and real counterfactual explana-
tions (counterfactual-basket distance), and the Euclidean distance between the centroids of 
the corresponding synthetic and real clusters of individuals (centroid distance). By jointly 
analyzing these distances, we derive a nuanced metric of alignment wherein lower coun-
terfactual-basket distances, combined with smaller centroid separations, indicate a higher 
degree of coherence. A schematization of this procedure can be found in Fig. 2.

3.6  Relevant generator and metrics for churn analysis

For  the  implementation  of  our  Counterfactual  Ensemble  Method,  we  choose  four  differ-
ent  counterfactual  generation  methods  that,  in  our  opinion,  condense  the  most  diverse 
approaches to the generation of synthetic counterfactual explanations.

---

<!-- PAGE 12 -->

230  Page 12 of 27

Fig.  2  Bipartite  network  illustrating  potential  matches  between  baskets  of  counterfactuals  from  real 
and  synthetic  datasets.  Each  node  aggregates  counterfactual  explanations  derived  from  clustered  indi-
viduals, and the matching is assessed using the average Euclidean distance dij  across all counterfactual 
components

● DiCE perturbs input features within the decision boundaries of the model, utilizing a 
genetic algorithm to create multiple instances that lead to different predictions (Sharma 
et al., 2020). It generates diverse counterfactual examples solving an optimization prob-
lem that balances properties of proximity and diversity.

● Growing Spheres (GS) uses a sphere-growing algorithm to iteratively explore the fea-
ture space around a given instance (Laugel et al., 2019). In our approach, we slightly 
modify GS to return the best k instances instead of just one, ranking them based on L2 
proximity to the original instance.

● CFRL is a model-agnostic counterfactual generation method that uses reinforcement 
learning (Samoilescu et al., 2021) to train a generative model to produce counterfactual 
explanations.

● T-LACE  is  a  counterfactual  explanation  method  that  constructs  a  transparent  latent 
space using a linear transformation where also the original prediction of the model is 
added, ensuring that similar records in the latent space have similar features and predic-
tions (Bodria et al., 2022). Counterfactuals are then searched in the latent space decom-
posing contributions from each feature to identify a prediction direction.

The scoring function of the counterfactual ensemble constitutes the central component of 
our framework. It is grounded in properties that correspond to the practical considerations 
a  churn  analyst  must  address  to  mitigate  the  risk  of  customer  attrition. When  applied  to 
alternative tabular data domains, such as credit risk assessment, this approach necessitates 
the selection of domain-specific metrics and their appropriate contextualization. In the fol-
lowing,  we  detail  the  metrics  adopted  in  the  churn  prediction  setting  and  elucidate  their 
intended roles.

---

<!-- PAGE 13 -->

Page 13 of 27  230

3.6.1  Proximity measures

How minimal are the changes required to retain potentially churning customers? Proxim-
ity measures indicate close counterfactuals. Proximity (also known as minimality (Byrne, 
2019))  is  a  fundamental  property  of  counterfactual  explanations.  We  choose  an  average 
proximity  measure  using  a  geometric  mean  that  combines  various  normalized  proximity 
measures. The geometric mean prevents skewing by outliers, ensuring equal contribution 
from all proximity measures. The individual proximity metrics we use are:

Euclidean Distance (L2 norm) measures the overall difference in feature values:

ProximityL2 =

h

m

−
m

i

√

(x′i −

cont
∑
∈

xi)2 +

h
m

j
cat
∑
∈

δ(x′j, xj)

Manhattan Distance (L1 norm) measures the sum of absolute differences:

ProximityL1 =

h

m

−
m

x′i −

|

xi|

+

h
m

δ(x′j, xj)

j
cat
∑
∈

i

cont
∑
∈

Maximum Absolute Difference L

norm measures the maximum element-wise abso-

lute difference:

∞

ProximityL

∞

= max

h

m

−
m

(

max
i
∈

cont |

x′i −

,

xi|

h
m

max
j
cat
∈

δ(x′j, xj)

)

Here, m is the total number of features, h the number of categorical features, cont continu-
= xj and 0 otherwise (Ham-
ous features, cat categorical features, and δ(x′j, xj) is 1 if x′j ̸
ming distance).

3.6.2  Plausibility measure

Is the counterfactual explanation similar to a non-churning customer in the data and thus 
justifiable to the customer? Plausibility indicates counterfactuals that have close examples 
in the original dataset.

∈

The  plausibility  measure  (also  known  as  feasibility  (Artelt  et  al.,  2021))  assesses  the 
degree of plausibility or soundness of the counterfactual instances (X ′) with respect to the 
instances in the original dataset to explain. Specifically, it calculates the minimum distance 
X ′ from its closest instance in the original data. To compute the plausibility 
of each x′
measure we build a KDTree (Maneewongvatana & Mount, 1999) on the Xtest dataset to 
efficiently find the nearest neighbors, then we query the KDTree to find the nearest neighbor 
in Xtest for each instance in the set of counterfactual instances and we calculate the dis-
tance between each x′ and its closest instance in Xtest. The use of a KDTree for computing 
the plausibility measure is motivated by the need to efficiently find the nearest neighbors 
of counterfactual instances within the dataset Xtest. KDTree provides logarithmic search 
time complexity for nearest neighbor queries, making it more scalable compared to linear 
search methods, which have linear time complexity. Efficiency is crucial when the number

---

<!-- PAGE 14 -->

230  Page 14 of 27

of  instances  in  Xtest  is  large,  a  common  situation  for  real-world  applications  like  churn 
analysis. Plausibility is represented as the euclidean distance of x′ from its closest instance 
in the Xtest population. A comparison between KDTree and the brute-force distance com-
putation  method  is  provided  in  the  supplementary  material,  demonstrating  the  efficiency 
benefits of the KDTree approach, maintaining high output accuracy.

3.6.3  Sparsity measure

Does the counterfactual explanation modify as few features as possible, thus making the 
required changes easier for the churn officer to propose? Sparsity indicates counterfactuals 
that touch the least amount of features.

Sparsity  (Guidotti,  2022)  is  computed  as  the  fraction  of  differing  features  to  the  total

number of features n:

Sparsity =

3.6.4  Diversity measure

n

i=1(x′i ̸
n

∑

= xi)

(7)

The counterfactuals produced do provide different courses of action for the churn officer? 
Diversity indicates that the explanations produced have enough variety for the churn officer 
to act on.

The  diversity  measure  (Mothilal  et  al.,  2020)  quantifies  the  dissimilarity  or  variation 
within groups defined by the generation source. It is calculated as the mean of distances 
between pairs of instances within each group.

Diversity =

1
N

N

i=1
∑

1
ni(ni −

1)

=k
∑j

d(xj, xk)

(8)

where N is the total number of groups - i.e. sets of counterfactuals for a given instance to 
explain -, ni is the number of instances in group i, and d(xj, xk) is the distance between 
instance j and instance k within the same group.

4  Experiments

For our experiments, we used four public datasets specifically focused on the churn clas-
sification problem. The"Credit Card Bank Churn", dataset5 includes 10000 credit card user 
records with 18 features to predict if a customer will stop using the bank’s credit card ser-
vices (0.19 ratio of churners). The"E-commerce Dataset"6contains 5,630 customer records 
with  20  features,  collected  from  a  leading  online  retailer.  It  is  used  to  predict  customer 
churn, enabling targeted retention efforts through promotional offers (0.20 ratio of churn-

5 https://www .kaggle.com /datasets/a nwarsan/ credit-card-bank-churn
6 https://www .kaggle.com /datasets/a nkitverm a2010/ecom merce-custo mer-churn-a nalysis- and-prediction

---

<!-- PAGE 15 -->

Page 15 of 27  230

ers). The"Iranian Churn Dataset"7 contains 3,150 records and provides telecommunications 
customer  data  from  Iran  with  13  features  used  to  analyze  churn  behavior  (0.18  ratio  of 
churners) in the telecom industry. The"Telco Customer Churn"dataset8 contains information 
on 7,043 customers of a telecom provider, including service usage patterns, billing informa-
tion, and demographic attributes. The dataset features a binary churn label and a churn rate 
of approximately 0.27, making it suitable for evaluating counterfactual explanations in real-
world customer retention scenarios.

We start by identifying which model to explain. We compare the performance of Light 
Gradient  Boosting  Machine  (LightGBM)(Ke  et  al.,  2017),  XGBoost  (Chen  &  Guestrin, 
2016), Random Forest (Breiman, 2001), and Multilayer Perceptron (MLP). Our focus is on 
the explanation methodology, more so than on the task, we therefore chose models that are 
commonly used for the task and easily applied (Geiler et al., 2022). To fine-tune the models, 
we  conducted  a  randomized  grid  search  with  5-fold  cross-validation,  optimizing  for  the 
ROC AUC score and we accounted for class imbalance penalizing errors on the minority 
class proportionally during training.

In Table 1 the comparison is displayed across datasets for F1-Score and Matthews Corre-
lation Coefficient (MCC) measures. The LightGBM outperforms or at least performs as well 
as the XGBoost in the datasets under analysis while the Random Forest and MLP slightly 
underperforms. These results lead us to establish the LightGBM as the model of interest for 
the following counterfactual explanations.

4.1  Interactivity of the counterfactual ensemble for real data

We analyze the behavior of the ensemble selection framework under different configura-
tions of both the linear and hierarchical scoring functions. Our objective is to understand if 
counterfactuals produced with the ensemble are aligned with practitioner-defined priorities 
and if the ensemble enables users to meaningfully interact with explanations. Our analysis 
focuses on two key experimental axes: (i) variation in the weight configurations assigned 
to the evaluation metrics, and (ii) stratification based on prediction confidence thresholds. 
We want, in other words, to verify if our method is responsive with respect to the possible

Table 1  Model  Performance  on  Churn  Datasets.  The  number  of  instances  is  referred  to  the  test  set  only. 
LightGBM tends to perform better, while XGBoost and Random Forest display similar performances, and 
MLP consistently underperforms
Churn Dataset
Card Churn

Test Instances
2026

Metric
F1 Score
MCC
F1 Score
MCC
F1 Score
MCC
F1 Score
MCC

LGB
0.87
0.79
0.95
0.90
0.90
0.87
0.71
0.61

XGB
0.86
0.78
0.89
0.78
0.88
0.74
0.72
0.63

RF
0.80
0.73
0.91
0.86
0.88
0.85
0.72
0.63

MLP
0.73
0.58
0.81
0.61
0.79
0.65
0.70
0.59

E-com Churn

Iranian Churn

755

630

Telco Churn

1408

7 https://arc hive.ics.uc i.edu/datas et/563/i ranian+churn+dataset
8 https:   //communi ty. ibm .com/comm unit y/ user/busin essan alyti  cs/blo gs/ st even  -m ac ko/20 19/07/11 /telc o-cus-
tomer-churn-1113

---

<!-- PAGE 16 -->

230  Page 16 of 27

choices of a potential user, i.e., how interactive is the basket of counterfactuals produced by 
the ensemble.

We begin by examining the effect of different weight allocations in the score function. 
Specifically, we consider five configurations: one with equal weighting across all four met-
rics (wi = 0.25), and four imbalanced settings in which a single metric receives a dominant 
weight of 0.5, while the remaining three metrics are equally assigned a weight of 0.1667. 
For each configuration, we compute the selection score of every counterfactual generated 
by the ensemble and rank them accordingly. The top k = 5 counterfactuals are then selected 
for each instance and algorithm.

Figure 3 displays the proportion of counterfactuals originating from each method–DiCE, 
T-LACE, GS, and CFRL–that are selected under different weight configurations for four 
benchmark  churn  datasets  and  for  both  the  linear  and  hierarchical  selection  scores.  The 
ensemble exhibits strong adaptability. T-LACE is consistently favored in both the Credit 
Card Churn and E-commerce Churn datasets, regardless of the emphasized metric. In con-
trast,  DiCE  emerges  as  the  top-performing  generator  in  the  Iranian  Churn  dataset,  while 
CFRL dominates in the Telco dataset. These results confirm that the quality of counterfac-
tual explanations varies significantly across methods and datasets, reinforcing the need for 
an ensemble approach that can dynamically tailor its selections based on user-defined priori-
ties. In contrast, the hierarchical evaluation function demonstrates a pronounced impact of 
user-specified parameter interactions. Across all datasets, no single counterfactual genera-
tor exhibits consistent dominance. Instead, the interplay between evaluation metrics yields 
dynamic selection patterns: for example, in the Credit Card Churn dataset, a more balanced 
selection is displayed. The hierarchical approach shows no stable trend, with the top-ranked 
counterfactuals shifting markedly as the weights change, illustrating that the hierarchical 
approach  facilitates  a  more  nuanced  and  adaptive  assessment  of  counterfactual  quality.

Fig. 3  Proportion of top-ranked counterfactuals selected by the ensemble across four datasets under dif-
ferent weight configurations: a) Credit Card Churn, b) E-commerce Churn, c) Iranian Churn, and d) Telco 
Churn. The x-axis indicates the metric with the highest weight. In the linear evaluation (top panel), DiCE 
dominates in a) and c), T-LACE in b), and CFRL in d). The hierarchical evaluation (bottom panel) is 
highly sensitive to parameter changes, underscoring the impact of user-defined interactions

---

<!-- PAGE 17 -->

Page 17 of 27  230

Moreover, we highlight that the hierarchical evaluation function is more intuitive in its for-
mulation for a human, as it can be simply designed as a set of priorities.

To further investigate the relationship between counterfactual selection and data point 
characteristics, we stratify the candidate counterfactuals into three bins according to their 
predicted probability for the target class: [0.5, 0.7), [0.7, 0.9), and [0.9, 1.0]. This confidence 
interval reflects the certainty of the black-box model in assigning the counterfactual to the 
opposite class of the original instance. For each confidence bin and weight configuration, we 
rerank the counterfactuals using the linear score and retain the top five per instance. Figure 4 
illustrates the proportion of selected counterfactuals for each generation method under this 
joint stratification.

Using the linear selection score, the figure reveals complementary insights. In the Credit 
Card dataset, T-LACE maintains a consistent advantage across all confidence levels, indi-
cating  its  robustness  to  prediction  certainty,  whereas  in  the  E-commerce  dataset  as  the 
threshold  increases,  patterns  vary  significantly.  In  the  Iranian  and  Telco  Churn  datasets, 
DiCE-generated  counterfactuals  not  only  dominate  overall,  but  are  increasingly  selected 
as prediction confidence rises, suggesting that DiCE yields more reliable, high-confidence 
explanations in these contexts. In contrast, GS and CFRL are more frequently selected at

Fig. 4  Proportion of top-ranked counterfactuals stratified by prediction probability thresholds and weight 
configurations across datasets: a) Credit Card Churn, b) E-commerce Churn, c) Iranian Churn, and d) 
Telco Churn. DiCE remains dominant in a) and c) at higher confidence thresholds. T-LACE is consis-
tently favored in b). CFRL is selected more frequently in d) when confidence is low, but this preference 
diminishes at higher thresholds

---

<!-- PAGE 18 -->

230  Page 18 of 27

lower  confidence  thresholds,  highlighting  their  relevance  to  generate  exploratory  or  less 
decisive alternatives. Interestingly, in the Telco Churn dataset, CFRL predominates only at 
lower confidence thresholds but is progressively supplanted by other methods as the thresh-
old increases. The results for the hierarchical selection score are provided in the Supplemen-
tary Information Fig.4 and are omitted here for length limits.

4.2  Comparison of synthetic and real counterfactual ensembles via KL divergence 
minimization

To  minimize  KL  divergence  between  real  and  synthetic  counterfactuals,  we  first 
selected  a  suitable  synthetic  data  generator.  We  evaluated  four  state-of-the-art  methods–
CTGAN (Xu et al., 2019), GaussianCopula (Patki et al., 2016), TVAE (Xu et al., 2019), 
and CopulaGAN(Patki et al., 2016)–on our four churn datasets using default parameters. 
The data quality was assessed with the SDV library, which computes two indicators: Col-
umn Shapes (measuring how well each column’s marginal distribution is preserved via the 
Kolmogorov–Smirnov  statistic  for  numerical/DateTime  columns  and  total  variation  dis-
tance for boolean/categorical ones) and Column Pair Trends (evaluating the preservation 
of relationships between columns using correlation similarity for numerical/DateTime pairs 
and contingency similarity for boolean/categorical pairs, with numerical data binned when 
paired with categorical data). The overall quality score is the average of these two metrics, 
bounded between 0 and 1. As shown in Table 2, CTGAN achieved the highest average qual-
ity score (0.87) compared to GaussianCopula (0.83), TVAE (0.79), and CopulaGAN (0.83); 
hence, CTGAN was chosen for all subsequent experiments.

Once a proper synthetic data generator is chosen, we can further assess the fidelity of our 
ensemble counterfactual explanations by comparing those generated on synthetic data (via 
CTGAN) to those derived from real data. In privacy-preserving scenarios, it is essential that 
the synthetic ensemble reliably approximates the characteristics of the real-data ensemble. 
To  quantify  this  alignment,  we  measure  the  average  KL  divergence,  ¯DKL,  between  the 
feature  distributions  computed  on  the  entire  population  of  real  and  synthetic  counterfac-
tuals.  For  each  dataset,  we  construct  ensembles  of  counterfactual  explanations  using  the 
linear selection score (as defined in Sec. 3.3.1). To mitigate sensitivity to initialization and 
ensure the robustness of the solution, the optimization problem formulated in Section 3.4 
is solved over 100 independent runs using trust-region methods. This procedure yields the 
optimal weight parameters for both the real (wR) and synthetic (wS) ensembles that mini-
mize  ¯DKL. While the hierarchical function achieves  increased levels  of interactivity,  the 
linear selection score guarantees lower level of KL Divergence (see Supplementary Mate-
rial  Tab.1).  Figure  5  compares  the  membership  ratios  for  real  and  synthetic  counterfac-
tual explanations under two evaluation strategies, linear (top row) and hierarchical (bottom 
row), after KL divergence minimization. Under the linear selection score, the composition 
of synthetic ensembles closely aligns with that of the real ensembles in three out of four

Table 2  Quality scores for 
synthetic data across different 
generation methods. CTGAN 
outperforms the other methods, 
achieving the highest average 
score, and is thus chosen for 
further analysis

CTGAN
Dataset
Credit
0.85
E-com 0.92
0.88
Iranian
0.91
Telco
0.89
Average

GaussianCopula
0.80
0.86
0.86
0.82
0.84

TVAE
0.76
0.83
0.94
0.72
0.81

CopulaGAN
0.81
0.86
0.85
0.80
0.83

---

<!-- PAGE 19 -->

Page 19 of 27  230

Fig. 5  Comparative analysis of membership ratios for real and synthetic datasets across evaluation meth-
ods (Linear and Hierarchical) following KL Divergence minimization. The top row illustrates member-
ship ratios for real and synthetic counterfactuals under linear evaluation, while the bottom row represents 
hierarchical evaluation. Each panel corresponds to a specific dataset (Credit, E-com, Iranian, Telco), with 
bars  indicating  membership  ratios  for  different  models.  Solid  bars  represent  real  counterfactuals,  and 
hatched bars denote synthetic counterfactuals. The x-axis is sorted in descending order of membership 
ratios for real datasets

datasets: T-LACE dominates for Credit, DiCE for Iranian, and CFRL for Telco. The only 
exception is the E-com dataset, where T-LACE dominates in the real ensemble, while DiCE 
prevails in the synthetic one. A similar pattern emerges under the hierarchical evaluation, 
though the dominant method varies across datasets: CFRL leads in Credit and Iranian, while 
DiCE dominates in Telco. Again, E-com presents a notable discrepancy–DiCE is the most 
represented method in the real ensemble, whereas CFRL dominates in the synthetic coun-
terpart.  These  findings  suggest  that  the  choice  of  selection  score  significantly  influences 
counterfactual selection, enabling finer control over user-defined priorities. Furthermore, in 
a subset of datasets, we observe shifts in method composition between real and synthetic 
ensembles even when the evaluation criterion remains fixed.

4.3  Alignment between SHAP and counterfactual ensemble

The purpose of this experiment is to evaluate whether the ensemble method for generat-
ing counterfactual explanations effectively captures the key features that drive the model’s 
decision-making process. Figure 6 presents a combined heatmap reporting Kendall’s Tau 
correlation coefficients between the ranking of SHAP feature importances and the ranking 
of the most frequently changed features in the counterfactual explanations. In this heatmap, 
each row represents a different ensemble configuration of the linear selection score, encom-
passing several user-defined weight combinations as well as a configuration optimized via 
KL divergence minimization, while the columns correspond to the four benchmark churn 
datasets, with real data denoted by

and CTGAN-generated (synthetic) data by

.

SHAP values, computed as the mean absolute Shapley values (Lundberg & Lee, 2017), 
quantify each feature’s contribution to the model’s output. In contrast, the ranking based on 
feature change frequencies reflects how often a feature is altered in the counterfactual expla-

R

S

---

<!-- PAGE 20 -->

230  Page 20 of 27

Fig.  6  Combined  Kendall-Tau  heatmap  comparing  SHAP  rank  correlations  between  individual  coun-
terfactual  methods  and  ensemble  configurations  across  real  and  synthetic  datasets.  Columns  alternate 
between real (denoted as 
) data for each dataset. Higher correlation values 
indicate  greater  alignment  of  ensemble-selected  counterfactuals  with  SHAP-based  feature  importance 
rankings

) and synthetic (denoted as

R

S

nations. A higher Kendall’s Tau coefficient indicates a stronger alignment between these two 
rankings,  suggesting  that  the  counterfactual  generation  method  effectively  identifies  and 
prioritizes features that are critical to the model’s decision-making process. The heatmap 
uses a coolwarm color scale, with red tones representing strong positive correlations and 
blue tones indicating weak or negative correlations. Importantly, our results indicate that for 
each dataset there is always at least one ensemble configuration capable of maintaining high 
correlations with the SHAP feature relevance–even when a single method is predominant, 
an appropriately weighted ensemble can achieve comparable performance. For example, in 
the Credit Churn dataset, an ensemble configuration emphasizing diversity achieves a cor-
relation of approximately 0.16 on the real data, compared to a maximum correlation of 0.26 
achieved  by  GS.  In  the  synthetic  Credit  dataset,  the  configuration  emphasizing  diversity 
achieves a correlation of approximately 0.15 while individual generators such as CFRL and 
GS achieve a correlation of 0.35 and 0.18, respectively. Similar trends are observed across 
the remaining datasets.

4.4  Relationship between cluster similarity and counterfactual ensembles

We  want  to  understand  if  our  KL  minimization methodology  can  help  the  user  in  devis-
ing realistic, population-specific strategies on synthetic data, which resemble the ones that 
would have been obtained from real data. To do so, we adopt the evaluation design that we 
introduced in Section 3.5. This analysis investigates the relationship between data similarity 
and the consistency of counterfactual behavior in both real and synthetic domains. First, we 
partitioned our datasets by label (churner versus non-churner) and applied K-Means clus-
tering with K = 5, as determined by the Elbow Method (see Fig. 5 in the Supplementary 
material) independently to both real and synthetic data. Building on the findings in Sec. 4.2, 
we computed weight vectors that minimize the KL divergence for each combination of real 
and synthetic clusters and used these weights to select the ensemble with the linear selec-
tion score (the same results for the hierarchical selection score are in the Supplementary

---

<!-- PAGE 21 -->

Page 21 of 27  230

−

Material Fig. 6). Subsequently, for each cluster, we computed the delta (X ′
X) between 
the ensemble of counterfactuals X ′ and the original input data X. The Euclidean distance 
between the real and synthetic counterfactual deltas was then measured in order to assess 
whether clusters that are closer in the feature space yield more similar counterfactual behav-
ior. In essence, our goal was to determine if structural similarity in the underlying data cor-
responds to greater consistency in the resulting counterfactual ensembles. Figure 7 presents 
a scatter plot where each point represents a pair of matched clusters. The x-axis denotes the 
Euclidean  distance  between  cluster  centroids,  while  the  y-axis  shows  the  Euclidean  dis-
tance between the corresponding counterfactual deltas. Our hypothesis was that increased 
separation between clusters would be reflected by larger differences between the ensemble 
outputs, thereby confirming a correlation between the structural similarity of clusters and 
the consistency of their counterfactual explanations. As illustrated in Fig. 7, the data reveal 
a significant statistical correlation between the Euclidean distance of cluster centroids and 
that of the counterfactual ensembles for E-com dataset churners, Iranian dataset non-churn-
ers, Iranian dataset churners, and Telco dataset non-churners. In other words, clusters that 
are  further  apart  in  feature  space  tend  to  produce  counterfactual  ensembles  that  diverge 
more substantially.

4.5  Qualitative evaluation of explanations

Figure 8 highlights the flexibility offered by our counterfactual generation method, allowing 
users to steer the explanations toward different intervention strategies depending on their 
needs. In the top-left panel, the sparse counterfactuals demonstrate how minimal and con-
centrated edits on a few features can produce actionable alternatives with limited resources, 
ideal when straightforward and somewhat inexepensive interventions are desired. In con-
trast, the top-right panel shows diverse counterfactuals that explore a broader set of changes 
across multiple features, giving users a wider range of distinct options to consider and gain 
more knowledge on the user profile leading to churning. The bottom-left panel emphasizes 
counterfactuals that remain very close to the original instance, reflecting scenarios where 
subtle, incremental adjustments are preferred to minimize the effort or risk associated with

Fig. 7  Relationship between Euclidean distances of clusters of real and synthetic data and euclidean dis-
tances of ensembles counterparts

---

<!-- PAGE 22 -->

230  Page 22 of 27

Fig.  8  Visual  comparison  of  two  counterfactual  strategies  from  the  E-commerce  Churn  dataset:  Top 
Left (green) shows sparse explanations with minimal feature edits to reverse the churn prediction, while 
Top  Right  (orange)  emphasizes  diversity  with  varied  and  broader  changes  across  multiple  features. 
The sparse counterfactual Bottom Left (blue) prioritizes proximity by making small, focused changes, 
whereas  the  counterfactuals  in  (Bottom  Right  (pink)  favors  plausibility,  offering  realistic  and  varied 
alternatives across multiple features

change.  Meanwhile,  the  bottom-right  panel  displays  counterfactuals  prioritizing  realistic, 
coherent edits across the feature space, illustrating how the method can suggest alternatives 
that align with practical, plausible scenarios for churn retention strategies.

Overall, the figure demonstrates how our approach supports a wide range of intervention 
styles, from minimal and focused to varied and realistic, by enabling users to adjust their 
priorities according to their specific constraints or preferences. This flexibility ensures that 
stakeholders can generate explanations best suited to their operational context, empower-
ing them with control over the balance between the metrics when designing counterfactual 
strategies.

---

<!-- PAGE 23 -->

Page 23 of 27  230

5  Conclusion

In  this  study,  we  introduced  a  novel  counterfactual  ensemble  selection  framework  that 
leverages multiple counterfactual generation techniques and evaluates their outputs based 
on a flexible and customizable scoring function. By combining these metrics through both 
linear and hierarchical evaluation strategies, our approach enables the selection of counter-
factuals based on user preferences that aim to be more flexible and adaptable to the churn 
prevention task. Our method fosters interactivity with explanations and human oversight, 
providing different avenues of intervention. We further tailor our methodology in the con-
text of synthetic data sharing for churn analysis, formulating an optimization problem that 
minimizes the KL divergence between the distributions of counterfactuals derived from real 
and synthetic data. This divergence minimization procedure serves as a tool to align syn-
thetic explanations with their real-data counterparts, thus enhancing the trustworthiness of 
models deployed in privacy-sensitive contexts such as churn analysis. Although we adopted 
LightGBM as the primary predictive model in our experiments due to its strong empirical 
performance and relevance in real-world tabular data tasks such as churn prediction, our 
framework remains inherently model-agnostic. The choice of LightGBM was driven by its 
balance of accuracy, efficiency, and practical relevance, as confirmed by domain experts. 
However, the counterfactual explanation generators we employ are model-agnostic, and our 
approach is fully compatible with more complex or less interpretable models, such as neural 
networks. While  our  method  shows  strong  results,  there  are  limitations  to  this  approach, 
mainly concerning the quality of the generated synthetic data. Another limitation may lie in 
the ability of non-technical users to navigate through the options offered by the ensemble, 
which require knowledge of the metrics and their impact on the output to be successfully 
tweaked. Further research should focus on enhancing the properties of the ensemble, incor-
porating new task-specific metrics tailored to the prediction challenge at hand. An additional 
direction for future work is to investigate whether this ensemble-based framework can be 
adapted from tabular data to more complex types of data, such as images. While the general 
idea of combining multiple counterfactual generation methods with flexible evaluation met-
rics remains valid, applying it to images could introduce significant challenges due to the 
high dimensionality and the absence of clearly defined features. Typically, generating coun-
terfactuals for images requires advanced generative models to produce realistic and mean-
ingful outputs, and defining clear, interpretable evaluation metrics becomes more difficult. 
However, by working in latent spaces and using perceptual or task-specific similarity mea-
sures, a similar ensemble approach could be developed to allow users to interactively select 
counterfactuals based on their preferences, making the method applicable to a wider range 
of data types. Finally, explainability methods are traditionally evaluated both quantitatively 
and qualitatively. Therefore, a rigorous user study aimed at experts in churn management 
would help us investigate some crucial issues in the implementation of our system: first, a 
user study would help us in understanding how to better communicate the explanations pro-
vided by the ensemble to the churn expert. Secondly, it would help us in investigating how 
a user would interact with the selection functions for the ensemble, and the effects of such 
changes in the interaction with the system.

Supplementary Information  The online version contains supplementary material available at  h t t p s : / / d o i . o r g 
/ 1 0 . 1 0 0 7 / s 1 0 9 9 4 - 0 2 5 - 0 6 8 8 0 - 4     .

---

<!-- PAGE 24 -->

230  Page 24 of 27

Acknowledgements  SoBigData.it receives funding from European Union – NextGenerationEU – National 
Recovery  and  Resilience  Plan  (Piano  Nazionale  di  Ripresa  e  Resilienza,  PNRR)  –  Project:  “SoBigData.
it – Strengthening the Italian RI for Social Mining and Big Data Analytics” – Prot. IR0000013 – Avviso n. 
3264 del 28/12/2021. This work has been also supported by the PNRR-M4C2-Investimento 1.3, Partenariato 
Esteso PE00000013-“FAIR-Future Artificial Intelligence Research”-Spoke 1 “Human-centered AI”, funded 
by the European Commission under the NextGeneration EU programme. MDV also acknowledges support 
by the European Community programme under the funding schemes: ERC-2018-ADG G.A. 834756 “XAI: 
Science and technology for the eXplanation of AI decision making.” This work was also funded by the Euro-
pean Union under Grant Agreement no. 101120763 - TANGO. Views and opinions expressed are however 
those of the author(s) only and do not necessarily reflect those of the European Union or the European Health 
and Digital Executive Agency (HaDEA). Neither the European Union nor the granting authority can be held 
responsible for them.

Author contributions  Conceptualization: R.P., M.V.; Methodology: R.P., M.V., S.M.; Formal analysis and 
investigation: R.P., M.V., S.M.; Writing - original draft preparation: R.P., M.V., S.M.; Writing - review and 
editing: R.P., M.V. F.G.; Funding acquisition: F.G.; Resources: F.G.; Supervision: R.P., F.G.; Software: M.V., 
S.M.;

Funding  Open access funding provided by Scuola Normale Superiore within the CRUI-CARE Agreement.

Data availability  The code, datasets, and models used in this study are available on GitHub:  C o u n t e r f a c t u 
a l   E n s e m b l e s   f o r   I n t e r p r e t a b l e   C h u r n   P r e d i c t i o n :   F r o m   R e a l - W o r l d   t o   P r i v a c y - P r e s e r v i n g   S y n t h e t i c   D a t a .

Declarations

Conflict of interest  The authors declare no competing interests.

Ethical approval and consent to participate  Not Applicable.

Consent for publication  Not Applicable.

Open  Access    This  article  is  licensed  under  a  Creative  Commons Attribution  4.0  International  License, 
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as 
you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons 
licence,  and  indicate  if  changes  were  made.  The  images  or  other  third  party  material  in  this  article  are 
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. 
If material is not included in the article’s Creative Commons licence and your intended use is not permitted 
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the 
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Adhikary, D. D., & Gupta, D. (2020). Applying over 100 classifiers for churn prediction in telecom compa-
nies. Multimedia Tools and Applications, 80, 1–22. https://doi.org/10.1007/s11042-020-09658-z
Ali, S., Abuhmed, T., El-Sappagh, S., Muhammad, K., Alonso-Moral, J. M., Confalonieri, R., Guidotti, R., 
Del Ser, J., Díaz-Rodríguez, N., & Herrera, F. (2023). Explainable artificial intelligence (XAI): What 
we know and what is left to attain trustworthy artificial intelligence. Information Fusion, 99, Article 
101805. https://doi.org/10.1016/j.inffus.2023.101805

Artelt, A., Vaquet, V., Velioglu, R., Hinder, F., Brinkrolf, J., Schilling, M., & Hammer, B. (2021). Evaluating 
robustness of counterfactual explanations. In: Proceedings of the 2021 IEEE Symposium on Computa-
tional Intelligence (SSCI), pp. 01–09 .  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / S S  C I 5 0 4  5 1 . 2 0 2  1 . 9 6  6 0 0 5 8

---

<!-- PAGE 25 -->

Page 25 of 27  230

Assefa, S., Dervovic, D., Mahfouz, M., Tillman, R., Reddy, P., & Veloso, M. (2020). Generating synthetic data 
in finance: opportunities, challenges and pitfalls. In: Proceedings of the 2020 International Conference 
on Artificial Intelligence and Data Science (ICAID), pp. 1–8 . https://doi.org/10.1145/3383455.3422554
Bellovin, S. M., Bonastia, R. M., Honig, A., Jones, J. R., & Stransky, E. (2019). Privacy and Synthetic Data-
sets. Stanford Law School, Center for Internet and Society. Working Paper .  h t t p s :  / / l a w  . s t a n f  o r d .  e d u / w  
p - c o n  t e n t / u  p l o a  d s / 2 0  1 9 / 0 1  / B e l l o  v i n _  2 0 1 9 0 1 2 9 . p d f

Bodria, F., Giannotti, F., Guidotti, R., & Naretto, F. (2023). Benchmarking and survey of explanation meth-
ods for black box models. Data Mining and Knowledge Discovery, 37, 1719–1778.  h t t p s : / / d o i . o r g / 1 0 . 
1 0 0 7 / s 1 0 6 1 8 - 0 2 3 - 0 0 9 3 3 - 9

Bodria, F., Guidotti, R., Giannotti, F., & Pedreschi, D. (2022). Transparent latent space counterfactual expla-
nations for tabular data. In: 2022 IEEE International Conference on Data Science and Advanced Analyt-
ics (DSAA), pp. 1–10 .  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / D S  A A 5 4 3  8 5 . 2 0 2  2 . 1 0  0 3 2 4 0 7

Breiman, L. (2001). Random forests. Machine Learning, 45, 5–32. https://doi.org/10.1023/A:1010950718922
Burez, J., & Poel, D. (2008). Handling class imbalance in customer churn prediction. Expert Systems with

Applications, 36, 4626–4636. https://doi.org/10.1016/j.eswa.2008.05.027

Byrne, R. (2019). Counterfactuals in explainable artificial intelligence (xai): Evidence from human reason-
ing. In: Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI), pp. 
6276–6282 . https://doi.org/10.24963/ijcai.2019/876

Carrizosa, E., Ramírez-Ayerbe, J., & Romero Morales, D. (2024). Mathematical optimization modelling for 
group counterfactual explanations. European Journal of Operational Research.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 
6 / j . e j o r . 2 0 2 4 . 0 1 . 0 0 2

Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd ACM 
SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794 .  h t t p s : / / d 
o i . o r g / 1 0 . 1 1 4 5 / 2 9 3 9 6 7 2 . 2 9 3 9 7 8 5

Coimbra, G. T., Santos, V. H. R., Maia, P. A., Silva, L. O., Souza, R. P., Silva, F. A., & Silva, T. R. M. B. 
(2024).  Cancel: A  feature  engineering  method  for  churn  prediction  in  a  privacy-preserving  context. 
Journal of Internet Services and Applications, 15(1), 438–449. https://doi.org/10.5753/jisa.2024.3874

De Bock, K., & De Caigny, A. (2021). Spline-rule ensemble classifiers with structured sparsity regularization 
for interpretable customer churn modeling. Decision Support Systems, 150, Article 113523.  h t t p s : / / d o i 
. o r g / 1 0 . 1 0 1 6 / j . d s s . 2 0 2 1 . 1 1 3 5 2 3

Dong, R., Su, F., Yang, S., Cheng, X., & Chen, W. (2018). Customer churn analysis for telecom operators 
based on svm. In: Proceedings of the 2018 International Conference on Artificial Intelligence and Big 
Data (ICAIBD) . https://doi.org/10.1007/978-981-10-7521-6_39

Freiesleben, T. (2022). The intriguing relation between counterfactual explanations and adversarial exam-

ples. Minds and Machines, 33. https://doi.org/10.1007/s11023-021-09580-9

Ganev, G., & De Cristofaro, E. (2025). The inadequacy of similarity-based privacy metrics: Privacy attacks 
against “truly anonymous” synthetic datasets. In: 2025 IEEE Symposium on Security and Privacy (SP), 
pp. 4007–4025. IEEE Computer Society, Los Alamitos, CA, USA .  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / S P 6 1 1 5 7 . 2 0 
2 5 . 0 0 2 1 8     .  h t t p s :  / / d o i  . i e e e c  o m p u  t e r s o  c i e t y  . o r g / 1  0 . 1 1  0 9 / S P 6 1 1 5 7 . 2 0 2 5 . 0 0 2 1 8

Geiler, L., Affeldt, S., & Nadif, M. (2022). A survey on machine learning methods for churn prediction. Inter-
national Journal of Data Science and Analytics, 14, 1–26. https://doi.org/10.1007/s41060-022-00312-5
Guidotti, R. (2022). Counterfactual explanations and how to find them: Literature review and benchmarking.

Data Mining and Knowledge Discovery, 38, 1–55. https://doi.org/10.1007/s10618-022-00831-6

Guidotti, R., & Ruggieri, S. (2021). Ensemble of counterfactual explainers. In: Explainable AI: Interpreting,

Explaining and Visualizing Deep Learning, . https://doi.org/10.1007/978-3-030-88942-5_28

Huh,  J.,  &  Lee,  W.  (2024).  Privacy-preserving  consumer  churn  prediction  in  telecommunication  through 
federated machine learning. In: 2024 IEEE International Conference on Big Data and Smart Computing 
(BigComp), pp. 355–356 .  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / B i  g C o m p  6 0 7 1 1 .  2 0 2 4  . 0 0 0 6 6

Hyrup, T., Lautrup, A. D., Zimek, A., & Schneider-Kamp, P. (2025). A systematic review of privacy-preserv-
ing techniques for synthetic tabular health data. Discover Data, 3(1), 5.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 4 2 4 
8 - 0 2 5 - 0 0 0 2 2 - w

Joy, U. G., Hoque, K. E., Nazim Uddin, M., Chowdhury, L., & Park, S.-B. (2024). A big data-driven hybrid 
model  for  enhancing  streaming  service  customer  retention  through  churn  prediction  integrated  with 
explainable AI. IEEE Access, 12, 69130–69150. https://doi.org/10.1109/ACCESS.2024.3401247

---

<!-- PAGE 26 -->

230  Page 26 of 27

Kanamori, K., Takagi, T., Kobayashi, K., Ike, Y., Uemura, K., & Arimura, H. (2021). Ordered counterfactual 
explanation  by  mixed-integer  linear  optimization.  Proceedings  of  the AAAI  Conference  on Artificial 
Intelligence, 35, 11564–11574. https://doi.org/10.1609/aaai.v35i13.17376

Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T.-Y. (2017). Lightgbm: A highly 
efficient gradient boosting decision tree. In: Proceedings of the 31st International Conference on Neural 
Information Processing Systems (NeurIPS 2017), pp. 3146–3154

Laugel, T., Lesot, M.-J., Marsala, C., Renard, X., & Detyniecki, M. (2019). The dangers of post-hoc interpret-
ability: Unjustified counterfactual explanations. In: Proceedings of the 28th International Joint Confer-
ence on Artificial Intelligence (IJCAI), pp. 2801–2807 . https://doi.org/10.24963/ijcai.2019/388

Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout the customer journey.

Journal of Marketing, 80(6), 69–96. https://doi.org/10.1509/jm.15.0420

Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. In: Proceedings of 
the 31st International Conference on Neural Information Processing Systems. NIPS’17, pp. 4768–4777. 
Curran Associates Inc., Red Hook, NY, USA

Maldonado, S., López, J., & Vairetti, C. (2020). Profit-based churn prediction based on minimax probability 
machines. European Journal of Operational Research, 284(1), 273–284.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e j o 
r . 2 0 1 9 . 1 2 . 0 0 7

Maneewongvatana, S., & Mount, D. M. (1999). Analysis of approximate nearest neighbor searching with

clustered point sets . arXiv:abs/cs/9901013

Mishra, A., & Reddy, U. S. (2017). A comparative study of customer churn prediction in telecom industry 
using ensemble based classifiers. In: 2017 International Conference on Intelligent Computing and Con-
trol (ICICI), pp. 721–725 . https://doi.org/10.1109/ICICI.2017.8365230

Mothilal, R. K., Sharma, A., & Tan, C. (2020). Explaining machine learning classifiers through diverse coun-
terfactual explanations. In: Proceedings of the 2020 Conference on Fairness, Accountability, and Trans-
parency. FAT* ’20, pp. 607–617. Association for Computing Machinery, New York, NY, USA .  h t t p s : / / 
d o i . o r g / 1 0 . 1 1 4 5 / 3 3 5 1 0 9 5 . 3 3 7 2 8 5 0

Nauta, M., Trienes, J., Pathak, S., Nguyen, E., Peters, M., Schmitt, Y., Schlötterer, J., Van Keulen, M., & 
Seifert, C. (2023). From anecdotal evidence to quantitative evaluation methods: A systematic review 
on evaluating explainable ai. Acm Computing Surveys, 55(13s), 1–42. https://doi.org/10.1145/3583558
Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The synthetic data vault. In: 2016 IEEE International 
Conference on Data Science and Advanced Analytics (DSAA), pp. 399–410 .  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / 
D S A A . 2 0 1 6 . 4 9

Petkovski, A., Risteska Stojkoska, B., Trivodaliev, K., & Kalajdziski, S. (2016). Analysis of churn prediction: 
A case study on telecommunication services in macedonia. In: 2016 24th Telecommunications Forum 
(TELFOR), pp. 1–4 . https://doi.org/10.1109/TELFOR.2016.7818903

Qian, Z., Callender, T., Cebere, B., Janes, S. M., Navani, N., & Schaar, M. (2024). Synthetic data for privacy-
preserving clinical risk prediction. Scientific Reports, 14(1), 25676.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 
4 - 7 2 8 9 4 - y

Rankin, D. R., Black, M., Bond, R., Wallace, J., Mulvenna, M., & Epelde, G. (2020). Reliability of super-
vised machine learning using synthetic data in health care: Model to preserve privacy for data sharing. 
JMIR Medical Informatics, 8(7), Article 18910. https://doi.org/10.2196/18910

Samoilescu, R.-F., Looveren, A. V., & Klaise, J. (2021). Model-agnostic and Scalable Counterfactual Expla-

nations via Reinforcement Learning . arxiv:abs/2106.02597

Sharma, S., Henderson, J., & Ghosh, J. (2020). Certifai: A common framework to provide explanations and 
analyse the fairness and robustness of black-box models. In: Proceedings of the AAAI/ACM Confer-
ence on AI, Ethics, and Society. AIES ’20, pp. 166–172. Association for Computing Machinery, New 
York, NY, USA . https://doi.org/10.1145/3375627.3375812

Stepin, I., Alonso, J., Catala, A., & Pereira-Farina, M. (2021). A survey of contrastive and counterfactual 
explanation generation methods for explainable artificial intelligence. IEEE Access, 9, 11974–12001. 
https://doi.org/10.1109/ACCESS.2021.3051315

Tan, J., Xu, S., Ge, Y., Li, Y., Chen, X., & Zhang, Y. (2021). Counterfactual explainable recommendation. In: 
Proceedings of the 30th ACM International Conference on Information and Knowledge Management 
(CIKM), pp. 1784–1793 . https://doi.org/10.1145/3459637.3482420

---

<!-- PAGE 27 -->

Page 27 of 27  230

Theodoridis, G., & Tsadiras, A. (2022). Applying machine learning techniques to predict and explain sub-
scriber  churn  of  an  online  drug  information  platform.  Neural  Computing  and  Applications,  34(22), 
19501–19514. https://doi.org/10.1007/s00521-022-07603-9

Tung, T.  (2024).  Unlocking  the  ai-powered  customer  experience:  Personalized  service,  enhanced  engage-
ment,  and  data-driven  strategies  for  e-commerce  applications.  Journal  of  Infrastructure,  Policy  and 
Development 8, 4970 https://doi.org/10.24294/jipd.v8i7.4970

Warren, G., Delaney, E., Guéret, C., & Keane, M. T. (2024). Explaining multiple instances counterfactually:user 
tests of group-counterfactuals for XAI. In: ICCBR. Lecture Notes in Computer Science, vol. 14775, pp. 
206–222. Springer, ???

Xiong, Y., Tao, J., Zhao, S., Wu, R., Shen, X., Lyu, T., Fan, C., Hu, Z., Zhao, S., & Pan, G. (2023). Explain-
able AI  for  cheating  detection  and  churn  prediction  in  online  games.  IEEE  Transactions  on  Games, 
15(2), 242–251. https://doi.org/10.1109/TG.2022.3173399

Xu,  L.,  Skoularidou,  M.,  Cuesta-Infante, A.,  &  Veeramachaneni,  K.  (2019).  Modeling  tabular  data  using 
conditional gan. In: Neural Information Processing Systems .  h t t p s :  / / a p i  . s e m a n  t i c s  c h o l a  r . o r g  / C o r p u  s I 
D :  1 9 5 7 6 7 0 6 4

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Machine Learning (2025) 114:230
https://doi.org/10.1007/s10994-025-06880-4
Counterfactual ensembles for interpretable churn prediction:
from real-world to privacy-preserving synthetic data
Samuele Tonati1,2 · Marzio Di Vece1,3 · Fosca Giannotti1 · Roberto Pellungrini1
Received: 23 April 2025 / Revised: 16 July 2025 / Accepted: 25 August 2025 /
Published online: 15 September 2025
© The Author(s) 2025
Abstract
Counterfactual explanations identify minimal input changes needed to alter a machine
learning model’s prediction, offering actionable insights in tasks like churn analysis. How-
ever, existing methods often produce counterfactuals that vary in quality, coherence, and
plausibility, limiting their practical value. We propose an ensemble evaluation framework
that integrates multiple generation techniques and ranks their outputs using a tunable scor-
ing function balancing multiple relevant metrics. Our approach addresses two key de-
ployment scenarios: (i) in-house churn analysis, where decision-makers can interactively
adjust scoring weights for tailored, user-driven explanations; and (ii) outsourced churn
prediction, where counterfactuals must be generated on synthetic data to preserve privacy
while remaining representative of real cases. Experiments on benchmark churn datasets
demonstrate that our ensemble approach improves the consistency, interpretability, and
utility of counterfactuals across both real and synthetic settings, supporting more reliable
and privacy-aware decision-making.
Keywords Explainable AI · Counterfactual explanations · Churn analysis
Editors: Riccardo Guidotti, Anna Monreale, Dino Pedreschi.
Roberto Pellungrini
roberto.pellungrini@sns.it
Samuele Tonati
samuele.tonati@sns.it
Marzio Di Vece
marzio.divece@sns.it
Fosca Giannotti
fosca.giannotti@sns.it
1 Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pisa, Italy
2 University of Pisa, Lungarno Antonio Pacinotti 43, 56126 Pisa, Italy
3 IMT School for Advanced Studies, Piazza San Francesco 19, 55100 Lucca, Italy
1 3

230 Page 2 of 27 Machine Learning (2025) 114:230
1 Introduction
Customer churn, the decision by clients to terminate a service, is a pervasive and costly
issue in many industries, particularly those offering subscription-based or contract-driven
services. Identifying which customers are likely to churn is only the first step; businesses
must also understand the underlying reasons behind customer attrition and how to intervene
effectively. This makes churn analysis not just a predictive task, but a high-stakes decision-
making problem where interpretability and actionable insights are essential.
In this context, Explainable Artificial Intelligence (XAI) has emerged as a powerful
approach to bridge the gap between model accuracy and human understanding. While
machine learning (ML) models have demonstrated high performance in predicting churn,
their increasing complexity often comes at the cost of transparency. As a result, many mod-
els become opaque to the practitioners who rely on them, creating significant barriers to
trust, accountability, and regulatory compliance (Ali et al., 2023). These concerns are espe-
cially pressing in domains like churn analysis, where decisions directly affects customer
engagement strategies and, ultimately, revenue.
XAI methods, and counterfactual explanations in particular, offer an intuitive and legally
relevant1 solution (Bodria et al., 2023). By identifying the minimal changes in input fea-
tures required to flip a model’s prediction, counterfactual explanations support contrastive
reasoning–answering the question: “What would need to change in a customer’s profile to
prevent churn?” This form of explanation is not only intuitive but aligns with emerging legal
requirements, such as those established under the GDPR2 and the AI Act3, concerning the
right to explanation and transparency (Stepin et al., 2021; Guidotti, 2022). In the context
of churn analysis, counterfactuals provide actionable recommendations that help retention
officers develop personalized intervention strategies (Geiler et al., 2022; Joy et al., 2024).
However, the quality of counterfactuals can vary significantly across different generation
techniques, with each method optimizing for different properties such as sparsity, plausibil-
ity, or diversity (Nauta et al., 2023). This heterogeneity poses a challenge when integrating
XAI into practical churn workflows, especially in the absence of a standardized evaluation
methodology tailored to the domain.
To address this challenge, we propose an ensemble evaluation framework specifically
designed for churn prediction. Our framework integrates multiple counterfactual generation
methods and ranks the resulting explanations using a dynamic, customizable scoring func-
tion. This function balances key counterfactual properties–proximity, sparsity, plausibility,
and diversity–to surface the most relevant and realistic explanations with minimal compu-
tational overhead (Guidotti & Ruggieri, 2021). This design empowers practitioners to tailor
explanations to the specific demands of churn analysis, where certain properties such as
feasibility and minimality are particularly crucial.
Our approach supports two primary operational scenarios. In the first, churn analysis is
conducted in-house, and the interpretability interface enables user-driven exploration. By
tuning the scoring function, decision makers can prioritize explanation characteristics that
align with business goals, facilitating targeted, customer-specific interventions based on
1 For Reference see GDPR articles 12-15 and 22.
2 See previous footnote.
3 For Reference see AI Act articles 13, 50 regarding transparency provisions for high-risk system providers
and deployers and Article 86 regarding the right to explanation for individual decision-making.
1 3

Machine Learning (2025) 114:230 Page 3 of 27 230
model output. In the second scenario, the prediction of churn is outsourced to third-party
providers4. These services can include machine learning-based churn prediction, analysis
of explanations, and intervention strategy design. In such cases, privacy considerations pre-
vent the direct sharing of real customer data. To overcome this constraint, we extend our
framework to operate in privacy-preserving settings by employing synthetic datasets that
retain the statistical properties of real data while eliminating personally identifiable infor-
mation (Qian et al., 2024). While generally faithful to the real counterpart, synthetic data
do not guarantee faithful counterfactuals. To ensure that synthetic counterfactuals remain
aligned with their real-data counterparts, we introduce an optimization strategy for our
ensemble method that minimizes the Kullback-Leibler (KL) divergence between the distri-
butions of selected counterfactuals from real and synthetic sources. This alignment ensures
that third parties receive explanations that are both representative of real situations and
privacy-compliant.
We validate our ensemble framework using four publicly available churn datasets, dem-
onstrating that it improves the robustness, interpretability, and practical utility of counter-
factual explanations. Our results show that the method is effective in both in-house and
privacy-sensitive scenarios, supporting trustworthy, human-centered decision making in
customer retention workflows.
1.1 Contributions
This work makes the following key contributions:
● Domain-specific ensemble evaluation framework: We introduce an ensemble-based
framework for evaluating and selecting counterfactual explanations tailored to churn
prediction, integrating multiple generation methods and ranking them using a scoring
function.
● Customizable multi-criteria selection: The scoring function balances proximity, spar-
sity, plausibility, and diversity, enabling practitioners to adapt the evaluation process to
domain-specific needs.
● Support for user-driven counterfactual exploration: In the in-house setting, our
framework allows interactive control over explanation generation, supporting interpret-
able, client-specific interventions.
● Privacy-preserving explanation generation with distributional alignment: For the
outsourced prediction of churn, we enable the use of synthetic data to protect personal
information while ensuring the fidelity of the explanation. This is achieved through
a KL-divergence-based optimization strategy that aligns the distributions of real and
synthetic counterfactuals.
● Comprehensive empirical validation: We validate the approach in four public churn
datasets, showing improved robustness, interpretability, and compliance with privacy in
both internal and external deployment settings.
4 Outsourcing Churn Analysis and Retention is a common practice. Companies specialized in Churn Analyt-
ics include InfoSysBPM, iQor and Konsyg, etc.
1 3

230 Page 4 of 27 Machine Learning (2025) 114:230
2 Related works
Early research on churn modeling has primarily emphasized predictive accuracy, employ-
ing a range of supervised and unsupervised learning methods to analyze customer behavior,
transaction histories, and demographic variables (Burez & Poel, 2008; Maldonado et al.,
2020; De Bock & De Caigny, 2021; Adhikary & Gupta, 2020). These models often perform
well in identifying likely churners, but their complexity tends to obscure the underlying
decision logic, limiting their usefulness in real-world retention strategies (Dong et al., 2018;
Mishra & Reddy, 2017; Petkovski et al., 2016).
To address the interpretability gap, counterfactual explanations have emerged as a prom-
ising post-hoc approach within Explainable AI (XAI). These methods identify the minimal
changes needed in a feature vector to alter a model’s decision (Bodria et al., 2023). Although
similar in structure to adversarial examples, counterfactuals are intended for human con-
sumption and emphasize informative properties such as proximity, sparsity, plausibility, and
diversity (Freiesleben, 2022; Guidotti, 2022).
Counterfactual reasoning is especially well-suited to personalized decision-making con-
texts, including churn management, as it allows businesses to identify individual-level inter-
ventions that may prevent customer loss (Lemon & Verhoef, 2016; Tung, 2024). However,
most XAI applications in churn analysis have relied on feature importance techniques, such
as SHAP or LIME (Joy et al., 2024; Theodoridis & Tsadiras, 2022; Xiong et al., 2023), with
relatively few studies exploring the use of counterfactuals for this domain.
From a methodological standpoint, optimization-based approaches to counterfactual
generation are well-established (Carrizosa et al., 2024; Kanamori et al., 2021; Tan et al.,
2021). However, existing studies typically focus on single-instance generation and do not
consider ensemble-based selection strategies. To the best of our knowledge, no prior work
has systematically applied ensemble evaluation of counterfactuals to churn prediction.
Privacy for churn prediction and analysis has been a focus of several works. In the article
by Coimbra et al. (2024), edge computing is used to process data for Churn analysis locally,
without transmitting users data. A similar approach is adopted by Huh and Lee (2024),
where privacy is guaranteed via Federated Learning, specifically in the telecommunication
sector. In both these works, the focus is in avoiding data transmission between nodes, thus
preventing sensible information from being shared outside of the first-party managing the
churn prediction. This suggests, as it happens in many practical cases, that churn prediction
is either performed directly by the data owner or, in case of outsourcing, is performed using
synthetic data, generated to replicate the statistical properties of real datasets while obfus-
cating personal identifiers (Assefa et al., 2020). Empirical evidence from domains such as
healthcare suggests that models trained on synthetic data can yield comparable performance
to those trained on real-world data (Rankin et al., 2020). Moreover, synthetic data genera-
tion is increasingly being combined with differential privacy guarantees to enhance protec-
tion without compromising utility (Bellovin et al., 2019). Hyrup et al. (2025) provides a
comprehensive overview of privacy-preserving techniques for synthetic data in the context
of health related data. Although a different domain, it still provides a good base to under-
stand how synthetic data can be used to enhance privacy in any data analysis or machine
learning process. The protection offered by synthetic data can still however be foiled, as
proved by Ganev and De Cristofaro (2025). In this work, the authors devise an attack model
that leverages the weaknesses of distance based privacy metrics to foil the protection of
1 3

Machine Learning (2025) 114:230 Page 5 of 27 230
synthetic data. However, the adversarial model adopted in the paper assumes a worst-case
scenario analysis, thus requiring the leaking of a lot of different data and parameters in order
to be effective.
3 Problem definition
3.1 Background
Churn prevention encompasses all the actions that a company puts into place to prevent the
loss of customers. The first and most important part of any churn prevention strategy lies in
detecting which customers will likely interrupt their relationship with the company, given
their current status. A churn officer has then the duty of interacting with these customers in
order to find possible actions to prevent them from churning. This task can be modeled as
a binary classification task (Geiler et al., 2022) where a machine learning model is used to
predict which customers are the ones likely to churn.
Formally, given a feature space Rd where each customer is represented by a d
X ⊆
dimensional vector x=(x 1 ,...,x n ) ∈X and a label space Y = { 0,1 } where 1 indicates
a customer churning and 0 a customer not churning, we assume to observe a dataset of
N i.i.d samples D = { (x i ,y i ) } N i=0 i ∼ id P(x,y) over X ×Y . A churn predictor (or classi-
fier) is a function f : usually trained over a training set train via empirical risk
X →Y D
minimization.
In this context, counterfactual explanations are extremely useful from a business’ per-
spective: firstly, counterfactual explanations help identify the minimal changes x needed to
retain a customer; for example, if the model indicates that a customer is likely to churn, a
counterfactual explanation might reveal that offering a small discount, offering a particular
product or improving service quality could change the prediction to retention. This allows
businesses to implement precise interventions that are cost-effective and efficient. Secondly,
the interpretability offered by counterfactual explanations builds trust among business
stakeholders. Unlike explanatory methods that might provide abstract or general insights,
such as in the case of global explanations, counterfactuals show specific scenarios and out-
comes, making it easier for non-technical stakeholders to understand and trust the model’s
recommendations. This trust is vital in securing support and commitment from stakehold-
ers for data-driven strategies and ensuring their successful implementation. Counterfactual
explanations have not been explored as a solution for the problem of specific optimization
strategies in churn prevention (Joy et al., 2024; Theodoridis & Tsadiras, 2022; Xiong et al.,
2023).
Formally, given an instance x and the corresponding churn prediction f(x)=y a coun-
terfactual explanation for x is a point x ′ such that f(x ′)=y ′ with y=y ′, i.e. the classifier’s
̸
output flips from its original prediction from y to y ′. To find a minimal counterfactual, given
a distance d(x,x ∗), we can solve the optimization problem:
x′ = argmind(x,x∗)
x∗ (1)
s.t. f(x)=f(x′)
̸
1 3

230 Page 6 of 27 Machine Learning (2025) 114:230
where d(x,x ∗) is commonly chosen to be the (L
1
) or (L
2
)-norm. Many counterfactual
explanation methods. However, depending on what counterfactual method one chooses
(Guidotti, 2022), the explanations obtained may rely on specific optimization strategies
that are variations or approximations of formulation 1 and therefore explore only some
particular aspect of the importance of a churn officer. Moreover, many counterfactual meth-
ods produce multiple counterfactual instances for any given x. We can therefore define
X ′ =
{
x ′1 ,...,x ′v} as the set of valid counterfactuals produced by any method for instance
x.
3.2 k-CEM: counterfactual ensemble method
To tackle similar problems, Guidotti et al. (Guidotti & Ruggieri, 2021) proposed an ensem-
ble method that leverages the strengths of multiple counterfactual explainers to cover a set
of desirable properties, such as minimality, actionability, stability, diversity, plausibility, and
discriminative power. Their approach demonstrates the efficacy of boosting weak explainers
into a powerful ensemble that is both model-agnostic and data-agnostic, capable of handling
various data types including tabular data, images, and time series.
Building upon this idea, we propose an ensemble approach that operates ex-post as an
evaluation and selection mechanism, called k-CEM. Our method is designed to identify the
optimal set of counterfactual examples by employing a linear combination score of various
metrics, that reflect on the possible aspects that a churn officer would explore in a churn pre-
diction model. In contrast to the ensemble proposed by Guidotti and Ruggieri (2021), which
combines results through a diversity-driven selection function, our framework introduces a
more nuanced selection score. This approach not only refines the selection process but also
ensures that the chosen counterfactuals align closely with the desired properties - thereby
improving the interpretability and reliability of the explanations provided – and that can be
aptly tweaked by practitioners to give more emphasis to a specific metric. Churn analysis,
however, is often outsourced to specialized organizations. In such circumstances, privacy
concerns often demand the use of protection mechanism, such as for example the use of
synthetic data. Synthetic data can be shared outside the organization for analysis (Hyrup et
al., 2025). However, while synthetic data is generated from real data and therefore similar
in general properties, it usually provides less accurate models and far less reliable explana-
tions. This means that third-party churn analysts cannot devise realistic customer retention
strategies based on these explanations. Thanks to the selection function that we devise, it is
possible to use k-CEM to improve churn prediction procedure in such a privacy-aware set-
ting by providing a tool to interact with outsource churn analysts without compromising the
quality of the explanations. To do this, we can exploit the selection function on synthetic data
with a KL-minimization strategy (Section 3.4) to find the best parameters to produce expla-
nations that are as close as possible to realistic explanations on real data. Let us define set of
counterfactual explanation methods as E = { e 1 ,...,e q } where e i :(f,x,y ′) → x ′. With
slight abuse of notation, we indicate with E(f,x,y ′)= { e 1 (f,x,y ′),...,e q (f,x,y ′) } . Our
proposal is to score the counterfactual explanations produced by an ensemble of counterfac-
tual methods E using evaluation metrics that align with desired properties in the context of
Churn analysis. The pseudocode of our approach is given in Algorithm 1.
1 3

Machine Learning (2025) 114:230 Page 7 of 27 230
Algorithm 1 k-CEM: k-Counterfactual Ensemble Method
For any given instance, once a set of valid counterfactual is obtained, k-CEM allows
the user to define a selection score (Section 3.3) and weights of a set of metrics M. The
priority of each metric is user-defined, therefore the user is able to modify the scores and
interact with the explanations, without having to recompute them. This point is crucial,
and is the reason for the ensemble of methods E: by increasing the number and diversity of
counterfactuals, the selection phase of k-CEM is able to exploit the representativeness of
the counterfactual set X ′ without overloading the user with information, presenting a set of
explanations that answer specific user needs as defined by the metrics M. The set of parame-
ters w i is main"handle"that a user can leverage to interact with k-CEM, modifying priorities
of metrics and exploring the space of explanations. We remark that all the explanations in
k-CEM are valid, local explanations. While global or group-level counterfactuals (Warren
et al., 2024) offer scalability and coherence, our method deliberately adheres to instance-
specific counterfactuals to guarantee perfect validity and actionability in a customer-reten-
tion context. Group explanations risk diluting personalized recommendations–potentially
yielding suggestions that are suboptimal or invalid for individuals at the periphery of a
heterogeneous subgroup. With our method, we ensure semantic consistency and predic-
tive fidelity, while remaining compatible with privacy-preserving techniques (e.g., synthetic
data) to safeguard confidentiality without compromising the precision of each explanation.
The framework in which k-CEM is applied is described in Fig 1. We envision k-CEM to be
at the center of two possible usage settings: first-party churn analysis or third-party churn
analysis.
1 3

230 Page 8 of 27 Machine Learning (2025) 114:230
Fig. 1 Churn analysis and explanation workflow with k-CEM
– First-party In first-party mode, k-CEM can be used by an organization internal per-
sonnel to perform in-house churn analysis, based on machine learning models trained
directly on the data gathered and managed by the organization. In this scenario, the
selection score of k-CEM allows the internal churn manager to interact with the expla-
nations, modifying the selection score (Section 3.3) to obtain the explanation that best
suit the needs of the organization. This allows the churn manager to develop personal-
ized intervention strategies by interacting with k-CEM at a reduced computational cost.
– Third-party In third-party mode, k-CEM can be used to interact with an external ana-
lyst that can devise an intervention strategy based on shared synthetic data. The orga-
nization needs only to share the synthetic dataset and the specifics of k-CEM, i.e., the
set of metrics of interest, to the third-party analyst. The analyst will then find the best
machine learning model to predict churn on the synthetic data and use k-CEM to explain
such a model. The organization can then use the model and explanations provided by
the external analyst to adjust k-CEM via KL-minimization strategy (Section 3.4) to find
a set of parameters that can provide realistic explanations for the synthetic data. There-
fore the external analyst can build an intervention strategy based on such explanations,
without ever accessing real data or real explanations.
In the following we are going to define the selection scores (Section 3.3) and KL-minimi-
zation strategy (Section 3.4) needed to make k-CEM function in the framework we devised,
and we will provide the relevant counterfactual methods E and metrics M relevant to churn
prediction (Section 3.6)
1 3

Machine Learning (2025) 114:230 Page 9 of 27 230
3.3 Selection scores
In this work, we propose two distinct strategies for combining evaluation metrics: a linear
selection score and a hierarchical selection score, as detailed below. The specific metrics
and counterfactual generators underlying these scores are introduced in later sections, where
they are defined in accordance with the application context.
3.3.1 Linear selection score
The selection score of each counterfactual explanation can be computed as a weighted lin-
ear combination of chosen metrics m i, which are defined so that a lower value indicates a
higher counterfactual performance. This formulation allows a flexible synthesis of the most
relevant aspects of counterfactual explanations based on application-specific priorities.
Formally, the score is defined as:
M
| |
Linear Score= w i m i (2)
i
∑
where w i are user-defined non-negative weights summing to 1, m i represents the i-th cho-
sen counterfactual metric and |M| is the number of the considered metrics. The final set of
counterfactual explanations is obtained by ranking candidates according to their selection
score in ascending order and selecting the top k instances, thus prioritizing explanations that
best align with the weighted optimization criteria.
3.3.2 Hierarchical selection score
In addition to the linear combination, we propose a hierarchical selection score designed
to prioritize metrics sequentially based on their relative importance. Rather than comput-
ing a single composite score by summing weighted metric values, our hierarchical proce-
dure operates in two distinct phases: allocation and refinement. Let M denote the number
of evaluation metrics, the set of candidate counterfactuals, and k the total number of
D
explanations to select.We assume normalized weights w i for each metric m i, such that
i | M =1 |w i =1. For each metric, we then apply a ranking-based selection:
∑
i =Top(k i , ,metrici ) (3)
S D
where Top(k i , ,m i ) returns the k i candidates from that optimize metrici, and
D D
k i = k w i . We aggregate these sets:
⌊ · ⌋
M
| |
= , (4)
i
S S
i=1
∪
Because each metric draws from the same pool , overlaps can occur: may exceed k. To
D |S|
meet the overall budget, we apply a refinement step. We order the aggregated set according
1 3

| 230  Page 10 of 27 |     |     |     | Machine Learning (2025) 114:230 |     |     |
| ------------------ | --- | --- | --- | ------------------------------- | --- | --- |
to the primary (highest-weight) metric, breaking ties by the next metric in weight order, and
truncate to the top-k instances. This ensures that any over-selection is resolved by prioritiz-
ing the most important metric, then the next, and so on.
3.3.3  Comparison of scores
The  Linear  selection  scores  pools  all  metrics  at  once  into  a  continuous  score
s(x)= w i m i (x) and selects the top-k by that score. In contrast, our hierarchical
i
approach discretizes the weight budget into per-metric quotas and enforces a minimal rep-
∑
resentation from each metric before considering composite performance. If a single weight
w j >0.5, the hierarchical method reserves  0.5k  slots exclusively based on metric j,
|     |     |     | ⌊   | ⌋   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
guaranteeing that at least half the explanations excel in that metric. In a pure linear score,
setting w j =0.5 similarly emphasizes j, but does not enforce a minimum count–other met-
rics could crowd out metric j if their combined scores exceed those of metric-j-focused
instances. The hierarchical allocation and refinement scheme thus provides interpretable,
controllable guarantees on per-metric representation, complementing the more fluid trade-
offs of linear combination.
3.4  KL divergence minimization for parameter tuning
In privacy-preserving settings, particularly when churn analysis is outsourced and real data
cannot be directly used, it’s essential that synthetic counterfactual explanations closely mir-
ror those derived from real data. To address this challenge, we introduce a parameter tuning
procedure based on minimizing the Kullback–Leibler (KL) divergence between the feature
distributions of the real and synthetic counterfactual ensembles. Formally, we measure the
distance between the feature distributions on real ( ) and synthetic ( ) datasets using the
|     |     |     |     | R   | S   |     |
| --- | --- | --- | --- | --- | --- | --- |
average Kullback-Leibler (KL) divergence:
n
1
|     | D¯ ( | )=  | D   | (Q P )  |     |     |
| --- | ---- | --- | --- | ------- | --- | --- |
|     | KL   |     | KL  | i i     |     | (5) |
|     | S    | ∥R  | n   | ∥       |     |     |
|     |      |     | i=1 |         |     |     |
∑
where n is the number of features considered, and Q i, P i denote the empirical distributions
of the i-th feature in the synthetic and real counterfactual datasets, respectively. For con-
tinuous variables, P i and Q i are estimated via histogram binning, with the number of bins
determined by Sturges’ rule to balance bias and variance. In this minimization, we jointly
optimize the weight vectors w = w ,w ,w ,w  and w = w ,w ,w ,w ,
|     |     | {   | 1R 2R | 3R 4R } | { 1S 2S | 3S 4S } |
| --- | --- | --- | ----- | ------- | ------- | ------- |
|     |     | R   |       |         | S       |         |
which govern the selection score functions for the real and synthetic datasets, respectively.
Alternatively, one may fix w  according to user-defined preferences and optimize only w ,
thereby preserving user-driven interpretability in the real counterfactuals while allowing  R S
for privacy-preserving adaptation in the synthetic ones. However, to avoid overcomplicat-
ing the narrative, we focus in this work on the joint optimization of both w  and w . The
|     |     |     |     |     | R   | S   |
| --- | --- | --- | --- | --- | --- | --- |
optimization problem is formulated as:
|     | m i   | n D¯ ( | (w ) | (w )), |     |     |
| --- | ----- | ------ | ---- | ------ | --- | --- |
|     |       | KL     | S ∥R |        |     | (6) |
|     | w , w |        | S    | R      |     |     |
R S
1 3

Machine Learning (2025) 114:230 Page 11 of 27 230
where (w ) and (w ) denote the distributions of features of the counterfactuals selected
S S R R
by the respective weight configurations. We solve this problem using a constrained optimi-
zation framework based on trust-region methods, which balance local model fidelity and
global convergence guarantees. The optimization is performed under the normalization con-
straint i w i =1 for each weight vector, ensuring interpretability and comparability of
the resulting scores. To enhance robustness and mitigate sensitivity to local minima inher-
ent in t ∑ he non-convex landscape of D¯ , the optimization is repeated over 100 indepen-
KL
dent random initializations. In each trial, the trust-region algorithm iteratively adjusts the
weights within adaptive neighborhoods, progressively refining the solution toward a local
minimum. The final parameter configuration is selected as the one yielding the minimal
KL divergence across all runs. This procedure provides a principled approach to calibrate
the evaluation metrics, aligning synthetic data-driven counterfactual explanations with their
real-data counterparts.
3.5 Coherence assessment via cluster-based distribution alignment
While the KL minimization procedure can be applied to the whole population of counterfac-
tuals generated (in both real and synthetic data), counterfactuals in churn analysis are often
used to interpret individual behavior and devise client-retention strategies.
In light of this, we build upon the KL Divergence minimization framework introduced
in Section 3.4, and we develop a cluster-based evaluation framework to assess the coher-
ence of counterfactual explanations derived from real and synthetic datasets. The procedure
begins by partitioning both real and synthetic datasets into distinct subgroups based on
observable behavioral patterns (e.g., the actual churn outcome). This stratification ensures
that subsequent analyses are performed on contextually analogous subsets, thereby enabling
fair comparisons between the two data modalities. Within each behavioral subgroup, we
apply the K-Means clustering algorithm to independently group the real and synthetic indi-
viduals into five clusters. These clusters serve as the basis for forming initial baskets of
counterfactual explanations. Counterfactual explanations are computed for each cluster
(real and synthetic) and KL Divergence minimization is performed to identify, for each
pair of synthetic and real counterfactual baskets, the counterfactual explanations that are
most similar in terms of their feature distributions. Subsequently, we quantify the coherence
between the real and synthetic counterfactuals by comparing the clusters of data points and
their respective counterfactual baskets. Two key measurements are obtained: the average
Euclidean distance among the selected couples of synthetic and real counterfactual explana-
tions (counterfactual-basket distance), and the Euclidean distance between the centroids of
the corresponding synthetic and real clusters of individuals (centroid distance). By jointly
analyzing these distances, we derive a nuanced metric of alignment wherein lower coun-
terfactual-basket distances, combined with smaller centroid separations, indicate a higher
degree of coherence. A schematization of this procedure can be found in Fig. 2.
3.6 Relevant generator and metrics for churn analysis
For the implementation of our Counterfactual Ensemble Method, we choose four differ-
ent counterfactual generation methods that, in our opinion, condense the most diverse
approaches to the generation of synthetic counterfactual explanations.
1 3

230 Page 12 of 27 Machine Learning (2025) 114:230
Fig. 2 Bipartite network illustrating potential matches between baskets of counterfactuals from real
and synthetic datasets. Each node aggregates counterfactual explanations derived from clustered indi-
viduals, and the matching is assessed using the average Euclidean distance dij across all counterfactual
components
● DiCE perturbs input features within the decision boundaries of the model, utilizing a
genetic algorithm to create multiple instances that lead to different predictions (Sharma
et al., 2020). It generates diverse counterfactual examples solving an optimization prob-
lem that balances properties of proximity and diversity.
● Growing Spheres (GS) uses a sphere-growing algorithm to iteratively explore the fea-
ture space around a given instance (Laugel et al., 2019). In our approach, we slightly
modify GS to return the best k instances instead of just one, ranking them based on L
2
proximity to the original instance.
● CFRL is a model-agnostic counterfactual generation method that uses reinforcement
learning (Samoilescu et al., 2021) to train a generative model to produce counterfactual
explanations.
● T-LACE is a counterfactual explanation method that constructs a transparent latent
space using a linear transformation where also the original prediction of the model is
added, ensuring that similar records in the latent space have similar features and predic-
tions (Bodria et al., 2022). Counterfactuals are then searched in the latent space decom-
posing contributions from each feature to identify a prediction direction.
The scoring function of the counterfactual ensemble constitutes the central component of
our framework. It is grounded in properties that correspond to the practical considerations
a churn analyst must address to mitigate the risk of customer attrition. When applied to
alternative tabular data domains, such as credit risk assessment, this approach necessitates
the selection of domain-specific metrics and their appropriate contextualization. In the fol-
lowing, we detail the metrics adopted in the churn prediction setting and elucidate their
intended roles.
1 3

| Machine Learning (2025) 114:230 |     |     |     |     |     |     | Page 13 of 27  | 230 |
| ------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- |
3.6.1  Proximity measures
How minimal are the changes required to retain potentially churning customers? Proxim-
ity measures indicate close counterfactuals. Proximity (also known as minimality (Byrne,
2019)) is a fundamental property of counterfactual explanations. We choose an average
proximity measure using a geometric mean that combines various normalized proximity
measures. The geometric mean prevents skewing by outliers, ensuring equal contribution
from all proximity measures. The individual proximity metrics we use are:
Euclidean Distance (L  norm) measures the overall difference in feature values:
2
|     |           |     | m h |      | h   |     |      |     |
| --- | --------- | --- | --- | ---- | --- | --- | ---- | --- |
|     | Proximity | =   | −   | (x x | )2+ | δ(x | ,x ) |     |
|     |           | L2  | m   | ′i−  | i m |     | ′j j |     |
√
|     |     |     |     | i ∈∑ cont |     | j ∑∈ cat |     |     |
| --- | --- | --- | --- | --------- | --- | -------- | --- | --- |
Manhattan Distance (L  norm) measures the sum of absolute differences:
1
|     |           |     | m h |           | h   |        |        |     |
| --- | --------- | --- | --- | --------- | --- | ------ | ------ | --- |
|     | Proximity |     | = − | x′i− x    | i + | δ(x′j  | ,x j ) |     |
|     |           | L1  | m   | |         | | m |        |        |     |
|     |           |     |     | i ∈∑ cont | j   | ∑∈ cat |        |     |
Maximum Absolute Difference L  norm measures the maximum element-wise abso-
∞
lute difference:
|     |           |        | m   | h         | h    |       |     |     |
| --- | --------- | ------ | --- | --------- | ---- | ----- | --- | --- |
|     |           |        |     | x′i−      | x ,  | δ(x′j | ,x  |     |
|     | Proximity | L =max | −   | m a x     | i    | m a x | j ) |     |
|     |           | ∞      | m   | i c o nt| | | mj | c a t |     |     |
|     |           |        | (   | ∈         |      | ∈     | )   |     |
Here, m is the total number of features, h the number of categorical features, cont continu-
ous features, cat categorical features, and δ(x ,x ) is 1 if x =x j and 0 otherwise (Ham-
|     |     |     |     | ′j j |     | ′j ̸ |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
ming distance).
3.6.2  Plausibility measure
Is the counterfactual explanation similar to a non-churning customer in the data and thus
justifiable to the customer? Plausibility indicates counterfactuals that have close examples
in the original dataset.
The plausibility measure (also known as feasibility (Artelt et al., 2021)) assesses the
degree of plausibility or soundness of the counterfactual instances (X ′) with respect to the
instances in the original dataset to explain. Specifically, it calculates the minimum distance
of each x ′ X ′ from its closest instance in the original data. To compute the plausibility
∈
measure we build a KDTree (Maneewongvatana & Mount, 1999) on the X  dataset to
test
efficiently find the nearest neighbors, then we query the KDTree to find the nearest neighbor
in X test  for each instance in the set of counterfactual instances and we calculate the dis-
tance between each x ′ and its closest instance in X . The use of a KDTree for computing
test
the plausibility measure is motivated by the need to efficiently find the nearest neighbors
of counterfactual instances within the dataset X . KDTree provides logarithmic search
test
time complexity for nearest neighbor queries, making it more scalable compared to linear
search methods, which have linear time complexity. Efficiency is crucial when the number
1 3

230 Page 14 of 27 Machine Learning (2025) 114:230
of instances in X is large, a common situation for real-world applications like churn
test
analysis. Plausibility is represented as the euclidean distance of x ′ from its closest instance
in the X population. A comparison between KDTree and the brute-force distance com-
test
putation method is provided in the supplementary material, demonstrating the efficiency
benefits of the KDTree approach, maintaining high output accuracy.
3.6.3 Sparsity measure
Does the counterfactual explanation modify as few features as possible, thus making the
required changes easier for the churn officer to propose? Sparsity indicates counterfactuals
that touch the least amount of features.
Sparsity (Guidotti, 2022) is computed as the fraction of differing features to the total
number of features n:
Sparsity= n i=1 (x ′i ̸ =x i ) (7)
n
∑
3.6.4 Diversity measure
The counterfactuals produced do provide different courses of action for the churn officer?
Diversity indicates that the explanations produced have enough variety for the churn officer
to act on.
The diversity measure (Mothilal et al., 2020) quantifies the dissimilarity or variation
within groups defined by the generation source. It is calculated as the mean of distances
between pairs of instances within each group.
N
1 1
Diversity= N n (n 1) d(x j ,x k ) (8)
i i
∑
i=1 −
∑
j
̸
=k
where N is the total number of groups - i.e. sets of counterfactuals for a given instance to
explain -, n i is the number of instances in group i, and d(x j ,x k ) is the distance between
instance j and instance k within the same group.
4 Experiments
For our experiments, we used four public datasets specifically focused on the churn clas-
sification problem. The"Credit Card Bank Churn", dataset5 includes 10000 credit card user
records with 18 features to predict if a customer will stop using the bank’s credit card ser-
vices (0.19 ratio of churners). The"E-commerce Dataset"6contains 5,630 customer records
with 20 features, collected from a leading online retailer. It is used to predict customer
churn, enabling targeted retention efforts through promotional offers (0.20 ratio of churn-
5 https://www .kaggle.com/ datasets/an warsan/ credit-card-bank-churn
6 https://www .kaggle.com/ datasets/an kitverma 2010/ecomm erce-custom er-churn-an alysis- and-prediction
1 3

| Machine Learning (2025) 114:230 |     |     |     | Page 15 of 27  | 230 |
| ------------------------------- | --- | --- | --- | -------------- | --- |
ers). The"Iranian Churn Dataset"7 contains 3,150 records and provides telecommunications
customer data from Iran with 13 features used to analyze churn behavior (0.18 ratio of
churners) in the telecom industry. The"Telco Customer Churn"dataset8 contains information
on 7,043 customers of a telecom provider, including service usage patterns, billing informa-
tion, and demographic attributes. The dataset features a binary churn label and a churn rate
of approximately 0.27, making it suitable for evaluating counterfactual explanations in real-
world customer retention scenarios.
We start by identifying which model to explain. We compare the performance of Light
Gradient Boosting Machine (LightGBM)(Ke et al., 2017), XGBoost (Chen & Guestrin,
2016), Random Forest (Breiman, 2001), and Multilayer Perceptron (MLP). Our focus is on
the explanation methodology, more so than on the task, we therefore chose models that are
commonly used for the task and easily applied (Geiler et al., 2022). To fine-tune the models,
we conducted a randomized grid search with 5-fold cross-validation, optimizing for the
ROC AUC score and we accounted for class imbalance penalizing errors on the minority
class proportionally during training.
In Table 1 the comparison is displayed across datasets for F1-Score and Matthews Corre-
lation Coefficient (MCC) measures. The LightGBM outperforms or at least performs as well
as the XGBoost in the datasets under analysis while the Random Forest and MLP slightly
underperforms. These results lead us to establish the LightGBM as the model of interest for
the following counterfactual explanations.
4.1  Interactivity of the counterfactual ensemble for real data
We analyze the behavior of the ensemble selection framework under different configura-
tions of both the linear and hierarchical scoring functions. Our objective is to understand if
counterfactuals produced with the ensemble are aligned with practitioner-defined priorities
and if the ensemble enables users to meaningfully interact with explanations. Our analysis
focuses on two key experimental axes: (i) variation in the weight configurations assigned
to the evaluation metrics, and (ii) stratification based on prediction confidence thresholds.
We want, in other words, to verify if our method is responsive with respect to the possible
Table 1 Model Performance on Churn Datasets. The number of instances is referred to the test set only.
LightGBM tends to perform better, while XGBoost and Random Forest display similar performances, and
MLP consistently underperforms
| Churn Dataset | Test Instances | Metric   | LGB XGB   | RF   | MLP  |
| ------------- | -------------- | -------- | --------- | ---- | ---- |
| Card Churn    | 2026           | F1 Score | 0.87 0.86 | 0.80 | 0.73 |
|               |                | MCC      | 0.79 0.78 | 0.73 | 0.58 |
| E-com Churn   | 755            | F1 Score | 0.95 0.89 | 0.91 | 0.81 |
|               |                | MCC      | 0.90 0.78 | 0.86 | 0.61 |
| Iranian Churn | 630            | F1 Score | 0.90 0.88 | 0.88 | 0.79 |
|               |                | MCC      | 0.87 0.74 | 0.85 | 0.65 |
| Telco Churn   | 1408           | F1 Score | 0.71 0.72 | 0.72 | 0.70 |
|               |                | MCC      | 0.61 0.63 | 0.63 | 0.59 |
7 https://arch ive.ics.uci .edu/datase t/563/ir anian+churn+dataset
8 https:   //communi ty. ibm .com/comm unit y/ user/busin essan alyti  cs/blo gs/ st even  -m ac ko/20 19/07/11 /telc o-cus-
tomer-churn-1113
1 3

230 Page 16 of 27 Machine Learning (2025) 114:230
choices of a potential user, i.e., how interactive is the basket of counterfactuals produced by
the ensemble.
We begin by examining the effect of different weight allocations in the score function.
Specifically, we consider five configurations: one with equal weighting across all four met-
rics (w i =0.25), and four imbalanced settings in which a single metric receives a dominant
weight of 0.5, while the remaining three metrics are equally assigned a weight of 0.1667.
For each configuration, we compute the selection score of every counterfactual generated
by the ensemble and rank them accordingly. The top k=5 counterfactuals are then selected
for each instance and algorithm.
Figure 3 displays the proportion of counterfactuals originating from each method–DiCE,
T-LACE, GS, and CFRL–that are selected under different weight configurations for four
benchmark churn datasets and for both the linear and hierarchical selection scores. The
ensemble exhibits strong adaptability. T-LACE is consistently favored in both the Credit
Card Churn and E-commerce Churn datasets, regardless of the emphasized metric. In con-
trast, DiCE emerges as the top-performing generator in the Iranian Churn dataset, while
CFRL dominates in the Telco dataset. These results confirm that the quality of counterfac-
tual explanations varies significantly across methods and datasets, reinforcing the need for
an ensemble approach that can dynamically tailor its selections based on user-defined priori-
ties. In contrast, the hierarchical evaluation function demonstrates a pronounced impact of
user-specified parameter interactions. Across all datasets, no single counterfactual genera-
tor exhibits consistent dominance. Instead, the interplay between evaluation metrics yields
dynamic selection patterns: for example, in the Credit Card Churn dataset, a more balanced
selection is displayed. The hierarchical approach shows no stable trend, with the top-ranked
counterfactuals shifting markedly as the weights change, illustrating that the hierarchical
approach facilitates a more nuanced and adaptive assessment of counterfactual quality.
Fig. 3 Proportion of top-ranked counterfactuals selected by the ensemble across four datasets under dif-
ferent weight configurations: a) Credit Card Churn, b) E-commerce Churn, c) Iranian Churn, and d) Telco
Churn. The x-axis indicates the metric with the highest weight. In the linear evaluation (top panel), DiCE
dominates in a) and c), T-LACE in b), and CFRL in d). The hierarchical evaluation (bottom panel) is
highly sensitive to parameter changes, underscoring the impact of user-defined interactions
1 3

Machine Learning (2025) 114:230 Page 17 of 27 230
Moreover, we highlight that the hierarchical evaluation function is more intuitive in its for-
mulation for a human, as it can be simply designed as a set of priorities.
To further investigate the relationship between counterfactual selection and data point
characteristics, we stratify the candidate counterfactuals into three bins according to their
predicted probability for the target class: [0.5, 0.7), [0.7, 0.9), and [0.9, 1.0]. This confidence
interval reflects the certainty of the black-box model in assigning the counterfactual to the
opposite class of the original instance. For each confidence bin and weight configuration, we
rerank the counterfactuals using the linear score and retain the top five per instance. Figure 4
illustrates the proportion of selected counterfactuals for each generation method under this
joint stratification.
Using the linear selection score, the figure reveals complementary insights. In the Credit
Card dataset, T-LACE maintains a consistent advantage across all confidence levels, indi-
cating its robustness to prediction certainty, whereas in the E-commerce dataset as the
threshold increases, patterns vary significantly. In the Iranian and Telco Churn datasets,
DiCE-generated counterfactuals not only dominate overall, but are increasingly selected
as prediction confidence rises, suggesting that DiCE yields more reliable, high-confidence
explanations in these contexts. In contrast, GS and CFRL are more frequently selected at
Fig. 4 Proportion of top-ranked counterfactuals stratified by prediction probability thresholds and weight
configurations across datasets: a) Credit Card Churn, b) E-commerce Churn, c) Iranian Churn, and d)
Telco Churn. DiCE remains dominant in a) and c) at higher confidence thresholds. T-LACE is consis-
tently favored in b). CFRL is selected more frequently in d) when confidence is low, but this preference
diminishes at higher thresholds
1 3

230 Page 18 of 27 Machine Learning (2025) 114:230
lower confidence thresholds, highlighting their relevance to generate exploratory or less
decisive alternatives. Interestingly, in the Telco Churn dataset, CFRL predominates only at
lower confidence thresholds but is progressively supplanted by other methods as the thresh-
old increases. The results for the hierarchical selection score are provided in the Supplemen-
tary Information Fig.4 and are omitted here for length limits.
4.2 Comparison of synthetic and real counterfactual ensembles via KL divergence
minimization
To minimize KL divergence between real and synthetic counterfactuals, we first
selected a suitable synthetic data generator. We evaluated four state-of-the-art methods–
CTGAN (Xu et al., 2019), GaussianCopula (Patki et al., 2016), TVAE (Xu et al., 2019),
and CopulaGAN(Patki et al., 2016)–on our four churn datasets using default parameters.
The data quality was assessed with the SDV library, which computes two indicators: Col-
umn Shapes (measuring how well each column’s marginal distribution is preserved via the
Kolmogorov–Smirnov statistic for numerical/DateTime columns and total variation dis-
tance for boolean/categorical ones) and Column Pair Trends (evaluating the preservation
of relationships between columns using correlation similarity for numerical/DateTime pairs
and contingency similarity for boolean/categorical pairs, with numerical data binned when
paired with categorical data). The overall quality score is the average of these two metrics,
bounded between 0 and 1. As shown in Table 2, CTGAN achieved the highest average qual-
ity score (0.87) compared to GaussianCopula (0.83), TVAE (0.79), and CopulaGAN (0.83);
hence, CTGAN was chosen for all subsequent experiments.
Once a proper synthetic data generator is chosen, we can further assess the fidelity of our
ensemble counterfactual explanations by comparing those generated on synthetic data (via
CTGAN) to those derived from real data. In privacy-preserving scenarios, it is essential that
the synthetic ensemble reliably approximates the characteristics of the real-data ensemble.
To quantify this alignment, we measure the average KL divergence, D¯ KL, between the
feature distributions computed on the entire population of real and synthetic counterfac-
tuals. For each dataset, we construct ensembles of counterfactual explanations using the
linear selection score (as defined in Sec. 3.3.1). To mitigate sensitivity to initialization and
ensure the robustness of the solution, the optimization problem formulated in Section 3.4
is solved over 100 independent runs using trust-region methods. This procedure yields the
optimal weight parameters for both the real (w R) and synthetic (w S) ensembles that mini-
mize D¯ . While the hierarchical function achieves increased levels of interactivity, the
KL
linear selection score guarantees lower level of KL Divergence (see Supplementary Mate-
rial Tab.1). Figure 5 compares the membership ratios for real and synthetic counterfac-
tual explanations under two evaluation strategies, linear (top row) and hierarchical (bottom
row), after KL divergence minimization. Under the linear selection score, the composition
of synthetic ensembles closely aligns with that of the real ensembles in three out of four
Table 2 Quality scores for Dataset CTGAN GaussianCopula TVAE CopulaGAN
synthetic data across different
Credit 0.85 0.80 0.76 0.81
generation methods. CTGAN
outperforms the other methods, E-com 0.92 0.86 0.83 0.86
achieving the highest average Iranian 0.88 0.86 0.94 0.85
score, and is thus chosen for Telco 0.91 0.82 0.72 0.80
further analysis
Average 0.89 0.84 0.81 0.83
1 3

Machine Learning (2025) 114:230 Page 19 of 27 230
Fig. 5 Comparative analysis of membership ratios for real and synthetic datasets across evaluation meth-
ods (Linear and Hierarchical) following KL Divergence minimization. The top row illustrates member-
ship ratios for real and synthetic counterfactuals under linear evaluation, while the bottom row represents
hierarchical evaluation. Each panel corresponds to a specific dataset (Credit, E-com, Iranian, Telco), with
bars indicating membership ratios for different models. Solid bars represent real counterfactuals, and
hatched bars denote synthetic counterfactuals. The x-axis is sorted in descending order of membership
ratios for real datasets
datasets: T-LACE dominates for Credit, DiCE for Iranian, and CFRL for Telco. The only
exception is the E-com dataset, where T-LACE dominates in the real ensemble, while DiCE
prevails in the synthetic one. A similar pattern emerges under the hierarchical evaluation,
though the dominant method varies across datasets: CFRL leads in Credit and Iranian, while
DiCE dominates in Telco. Again, E-com presents a notable discrepancy–DiCE is the most
represented method in the real ensemble, whereas CFRL dominates in the synthetic coun-
terpart. These findings suggest that the choice of selection score significantly influences
counterfactual selection, enabling finer control over user-defined priorities. Furthermore, in
a subset of datasets, we observe shifts in method composition between real and synthetic
ensembles even when the evaluation criterion remains fixed.
4.3 Alignment between SHAP and counterfactual ensemble
The purpose of this experiment is to evaluate whether the ensemble method for generat-
ing counterfactual explanations effectively captures the key features that drive the model’s
decision-making process. Figure 6 presents a combined heatmap reporting Kendall’s Tau
correlation coefficients between the ranking of SHAP feature importances and the ranking
of the most frequently changed features in the counterfactual explanations. In this heatmap,
each row represents a different ensemble configuration of the linear selection score, encom-
passing several user-defined weight combinations as well as a configuration optimized via
KL divergence minimization, while the columns correspond to the four benchmark churn
datasets, with real data denoted by and CTGAN-generated (synthetic) data by .
R S
SHAP values, computed as the mean absolute Shapley values (Lundberg & Lee, 2017),
quantify each feature’s contribution to the model’s output. In contrast, the ranking based on
feature change frequencies reflects how often a feature is altered in the counterfactual expla-
1 3

230 Page 20 of 27 Machine Learning (2025) 114:230
Fig. 6 Combined Kendall-Tau heatmap comparing SHAP rank correlations between individual coun-
terfactual methods and ensemble configurations across real and synthetic datasets. Columns alternate
between real (denoted as ) and synthetic (denoted as ) data for each dataset. Higher correlation values
R S
indicate greater alignment of ensemble-selected counterfactuals with SHAP-based feature importance
rankings
nations. A higher Kendall’s Tau coefficient indicates a stronger alignment between these two
rankings, suggesting that the counterfactual generation method effectively identifies and
prioritizes features that are critical to the model’s decision-making process. The heatmap
uses a coolwarm color scale, with red tones representing strong positive correlations and
blue tones indicating weak or negative correlations. Importantly, our results indicate that for
each dataset there is always at least one ensemble configuration capable of maintaining high
correlations with the SHAP feature relevance–even when a single method is predominant,
an appropriately weighted ensemble can achieve comparable performance. For example, in
the Credit Churn dataset, an ensemble configuration emphasizing diversity achieves a cor-
relation of approximately 0.16 on the real data, compared to a maximum correlation of 0.26
achieved by GS. In the synthetic Credit dataset, the configuration emphasizing diversity
achieves a correlation of approximately 0.15 while individual generators such as CFRL and
GS achieve a correlation of 0.35 and 0.18, respectively. Similar trends are observed across
the remaining datasets.
4.4 Relationship between cluster similarity and counterfactual ensembles
We want to understand if our KL minimization methodology can help the user in devis-
ing realistic, population-specific strategies on synthetic data, which resemble the ones that
would have been obtained from real data. To do so, we adopt the evaluation design that we
introduced in Section 3.5. This analysis investigates the relationship between data similarity
and the consistency of counterfactual behavior in both real and synthetic domains. First, we
partitioned our datasets by label (churner versus non-churner) and applied K-Means clus-
tering with K =5, as determined by the Elbow Method (see Fig. 5 in the Supplementary
material) independently to both real and synthetic data. Building on the findings in Sec. 4.2,
we computed weight vectors that minimize the KL divergence for each combination of real
and synthetic clusters and used these weights to select the ensemble with the linear selec-
tion score (the same results for the hierarchical selection score are in the Supplementary
1 3

Machine Learning (2025) 114:230 Page 21 of 27 230
Material Fig. 6). Subsequently, for each cluster, we computed the delta (X ′ X) between
−
the ensemble of counterfactuals X ′ and the original input data X. The Euclidean distance
between the real and synthetic counterfactual deltas was then measured in order to assess
whether clusters that are closer in the feature space yield more similar counterfactual behav-
ior. In essence, our goal was to determine if structural similarity in the underlying data cor-
responds to greater consistency in the resulting counterfactual ensembles. Figure 7 presents
a scatter plot where each point represents a pair of matched clusters. The x-axis denotes the
Euclidean distance between cluster centroids, while the y-axis shows the Euclidean dis-
tance between the corresponding counterfactual deltas. Our hypothesis was that increased
separation between clusters would be reflected by larger differences between the ensemble
outputs, thereby confirming a correlation between the structural similarity of clusters and
the consistency of their counterfactual explanations. As illustrated in Fig. 7, the data reveal
a significant statistical correlation between the Euclidean distance of cluster centroids and
that of the counterfactual ensembles for E-com dataset churners, Iranian dataset non-churn-
ers, Iranian dataset churners, and Telco dataset non-churners. In other words, clusters that
are further apart in feature space tend to produce counterfactual ensembles that diverge
more substantially.
4.5 Qualitative evaluation of explanations
Figure 8 highlights the flexibility offered by our counterfactual generation method, allowing
users to steer the explanations toward different intervention strategies depending on their
needs. In the top-left panel, the sparse counterfactuals demonstrate how minimal and con-
centrated edits on a few features can produce actionable alternatives with limited resources,
ideal when straightforward and somewhat inexepensive interventions are desired. In con-
trast, the top-right panel shows diverse counterfactuals that explore a broader set of changes
across multiple features, giving users a wider range of distinct options to consider and gain
more knowledge on the user profile leading to churning. The bottom-left panel emphasizes
counterfactuals that remain very close to the original instance, reflecting scenarios where
subtle, incremental adjustments are preferred to minimize the effort or risk associated with
Fig. 7 Relationship between Euclidean distances of clusters of real and synthetic data and euclidean dis-
tances of ensembles counterparts
1 3

230 Page 22 of 27 Machine Learning (2025) 114:230
Fig. 8 Visual comparison of two counterfactual strategies from the E-commerce Churn dataset: Top
Left (green) shows sparse explanations with minimal feature edits to reverse the churn prediction, while
Top Right (orange) emphasizes diversity with varied and broader changes across multiple features.
The sparse counterfactual Bottom Left (blue) prioritizes proximity by making small, focused changes,
whereas the counterfactuals in (Bottom Right (pink) favors plausibility, offering realistic and varied
alternatives across multiple features
change. Meanwhile, the bottom-right panel displays counterfactuals prioritizing realistic,
coherent edits across the feature space, illustrating how the method can suggest alternatives
that align with practical, plausible scenarios for churn retention strategies.
Overall, the figure demonstrates how our approach supports a wide range of intervention
styles, from minimal and focused to varied and realistic, by enabling users to adjust their
priorities according to their specific constraints or preferences. This flexibility ensures that
stakeholders can generate explanations best suited to their operational context, empower-
ing them with control over the balance between the metrics when designing counterfactual
strategies.
1 3

Machine Learning (2025) 114:230 Page 23 of 27 230
5 Conclusion
In this study, we introduced a novel counterfactual ensemble selection framework that
leverages multiple counterfactual generation techniques and evaluates their outputs based
on a flexible and customizable scoring function. By combining these metrics through both
linear and hierarchical evaluation strategies, our approach enables the selection of counter-
factuals based on user preferences that aim to be more flexible and adaptable to the churn
prevention task. Our method fosters interactivity with explanations and human oversight,
providing different avenues of intervention. We further tailor our methodology in the con-
text of synthetic data sharing for churn analysis, formulating an optimization problem that
minimizes the KL divergence between the distributions of counterfactuals derived from real
and synthetic data. This divergence minimization procedure serves as a tool to align syn-
thetic explanations with their real-data counterparts, thus enhancing the trustworthiness of
models deployed in privacy-sensitive contexts such as churn analysis. Although we adopted
LightGBM as the primary predictive model in our experiments due to its strong empirical
performance and relevance in real-world tabular data tasks such as churn prediction, our
framework remains inherently model-agnostic. The choice of LightGBM was driven by its
balance of accuracy, efficiency, and practical relevance, as confirmed by domain experts.
However, the counterfactual explanation generators we employ are model-agnostic, and our
approach is fully compatible with more complex or less interpretable models, such as neural
networks. While our method shows strong results, there are limitations to this approach,
mainly concerning the quality of the generated synthetic data. Another limitation may lie in
the ability of non-technical users to navigate through the options offered by the ensemble,
which require knowledge of the metrics and their impact on the output to be successfully
tweaked. Further research should focus on enhancing the properties of the ensemble, incor-
porating new task-specific metrics tailored to the prediction challenge at hand. An additional
direction for future work is to investigate whether this ensemble-based framework can be
adapted from tabular data to more complex types of data, such as images. While the general
idea of combining multiple counterfactual generation methods with flexible evaluation met-
rics remains valid, applying it to images could introduce significant challenges due to the
high dimensionality and the absence of clearly defined features. Typically, generating coun-
terfactuals for images requires advanced generative models to produce realistic and mean-
ingful outputs, and defining clear, interpretable evaluation metrics becomes more difficult.
However, by working in latent spaces and using perceptual or task-specific similarity mea-
sures, a similar ensemble approach could be developed to allow users to interactively select
counterfactuals based on their preferences, making the method applicable to a wider range
of data types. Finally, explainability methods are traditionally evaluated both quantitatively
and qualitatively. Therefore, a rigorous user study aimed at experts in churn management
would help us investigate some crucial issues in the implementation of our system: first, a
user study would help us in understanding how to better communicate the explanations pro-
vided by the ensemble to the churn expert. Secondly, it would help us in investigating how
a user would interact with the selection functions for the ensemble, and the effects of such
changes in the interaction with the system.
Supplementary Information The online version contains supplementary material available at h t t p s : / / d oi . o r g
/ 1 0 . 1 0 0 7 / s 1 0 9 9 4 - 0 2 5 - 0 6 8 8 0 - 4 .
1 3

230 Page 24 of 27 Machine Learning (2025) 114:230
Acknowledgements SoBigData.it receives funding from European Union – NextGenerationEU – National
Recovery and Resilience Plan (Piano Nazionale di Ripresa e Resilienza, PNRR) – Project: “SoBigData.
it – Strengthening the Italian RI for Social Mining and Big Data Analytics” – Prot. IR0000013 – Avviso n.
3264 del 28/12/2021. This work has been also supported by the PNRR-M4C2-Investimento 1.3, Partenariato
Esteso PE00000013-“FAIR-Future Artificial Intelligence Research”-Spoke 1 “Human-centered AI”, funded
by the European Commission under the NextGeneration EU programme. MDV also acknowledges support
by the European Community programme under the funding schemes: ERC-2018-ADG G.A. 834756 “XAI:
Science and technology for the eXplanation of AI decision making.” This work was also funded by the Euro-
pean Union under Grant Agreement no. 101120763 - TANGO. Views and opinions expressed are however
those of the author(s) only and do not necessarily reflect those of the European Union or the European Health
and Digital Executive Agency (HaDEA). Neither the European Union nor the granting authority can be held
responsible for them.
Author contributions Conceptualization: R.P., M.V.; Methodology: R.P., M.V., S.M.; Formal analysis and
investigation: R.P., M.V., S.M.; Writing - original draft preparation: R.P., M.V., S.M.; Writing - review and
editing: R.P., M.V. F.G.; Funding acquisition: F.G.; Resources: F.G.; Supervision: R.P., F.G.; Software: M.V.,
S.M.;
Funding Open access funding provided by Scuola Normale Superiore within the CRUI-CARE Agreement.
Data availability The code, datasets, and models used in this study are available on GitHub: C o u n t e r f a c t u
a l E n s e m b l e s f o r I n t e r p r e t a b l e C h u r n P r e d i c t i o n : F r o m R e a l - W o r l d t o P r i v a c y - P r e s e r v i n g S y n t h e t i c D a t a .
Declarations
Conflict of interest The authors declare no competing interests.
Ethical approval and consent to participate Not Applicable.
Consent for publication Not Applicable.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as
you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons
licence, and indicate if changes were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material.
If material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Adhikary, D. D., & Gupta, D. (2020). Applying over 100 classifiers for churn prediction in telecom compa-
nies. Multimedia Tools and Applications, 80, 1–22. https://doi.org/10.1007/s11042-020-09658-z
Ali, S., Abuhmed, T., El-Sappagh, S., Muhammad, K., Alonso-Moral, J. M., Confalonieri, R., Guidotti, R.,
Del Ser, J., Díaz-Rodríguez, N., & Herrera, F. (2023). Explainable artificial intelligence (XAI): What
we know and what is left to attain trustworthy artificial intelligence. Information Fusion, 99, Article
101805. https://doi.org/10.1016/j.inffus.2023.101805
Artelt, A., Vaquet, V., Velioglu, R., Hinder, F., Brinkrolf, J., Schilling, M., & Hammer, B. (2021). Evaluating
robustness of counterfactual explanations. In: Proceedings of the 2021 IEEE Symposium on Computa-
tional Intelligence (SSCI), pp. 01–09 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / S S C I 5 0 4 5 1 . 2 0 2 1 . 9 6 6 0 0 5 8
1 3

Machine Learning (2025) 114:230 Page 25 of 27 230
Assefa, S., Dervovic, D., Mahfouz, M., Tillman, R., Reddy, P., & Veloso, M. (2020). Generating synthetic data
in finance: opportunities, challenges and pitfalls. In: Proceedings of the 2020 International Conference
on Artificial Intelligence and Data Science (ICAID), pp. 1–8 . https://doi.org/10.1145/3383455.3422554
Bellovin, S. M., Bonastia, R. M., Honig, A., Jones, J. R., & Stransky, E. (2019). Privacy and Synthetic Data-
sets. Stanford Law School, Center for Internet and Society. Working Paper . h t t p s : / / l a w . s t a n f o r d . e d u / w
p - c o n t e n t / u p l o a d s / 2 0 1 9 / 0 1 / B e l l o v i n _ 2 0 1 9 0 1 2 9 . p d f
Bodria, F., Giannotti, F., Guidotti, R., & Naretto, F. (2023). Benchmarking and survey of explanation meth-
ods for black box models. Data Mining and Knowledge Discovery, 37, 1719–1778. h t t p s : / / d o i . o r g / 1 0 .
1 0 0 7 / s 1 0 6 1 8 - 0 2 3 - 0 0 9 3 3 - 9
Bodria, F., Guidotti, R., Giannotti, F., & Pedreschi, D. (2022). Transparent latent space counterfactual expla-
nations for tabular data. In: 2022 IEEE International Conference on Data Science and Advanced Analyt-
ics (DSAA), pp. 1–10 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / D S A A 5 4 3 8 5 . 2 0 2 2 . 1 0 0 3 2 4 0 7
Breiman, L. (2001). Random forests. Machine Learning, 45, 5–32. https://doi.org/10.1023/A:1010950718922
Burez, J., & Poel, D. (2008). Handling class imbalance in customer churn prediction. Expert Systems with
Applications, 36, 4626–4636. https://doi.org/10.1016/j.eswa.2008.05.027
Byrne, R. (2019). Counterfactuals in explainable artificial intelligence (xai): Evidence from human reason-
ing. In: Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI), pp.
6276–6282 . https://doi.org/10.24963/ijcai.2019/876
Carrizosa, E., Ramírez-Ayerbe, J., & Romero Morales, D. (2024). Mathematical optimization modelling for
group counterfactual explanations. European Journal of Operational Research. h t t p s : / / d o i . o r g / 1 0 . 1 0 1
6 / j . e j o r . 2 0 2 4 . 0 1 . 0 0 2
Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794 . h t t p s : / / d
o i . o r g / 1 0 . 1 1 4 5 / 2 9 3 9 6 7 2 . 2 9 3 9 7 8 5
Coimbra, G. T., Santos, V. H. R., Maia, P. A., Silva, L. O., Souza, R. P., Silva, F. A., & Silva, T. R. M. B.
(2024). Cancel: A feature engineering method for churn prediction in a privacy-preserving context.
Journal of Internet Services and Applications, 15(1), 438–449. https://doi.org/10.5753/jisa.2024.3874
De Bock, K., & De Caigny, A. (2021). Spline-rule ensemble classifiers with structured sparsity regularization
for interpretable customer churn modeling. Decision Support Systems, 150, Article 113523. h t t p s : / / d o i
. o r g / 1 0 . 1 0 1 6 / j . d s s . 2 0 2 1 . 1 1 3 5 2 3
Dong, R., Su, F., Yang, S., Cheng, X., & Chen, W. (2018). Customer churn analysis for telecom operators
based on svm. In: Proceedings of the 2018 International Conference on Artificial Intelligence and Big
Data (ICAIBD) . https://doi.org/10.1007/978-981-10-7521-6_39
Freiesleben, T. (2022). The intriguing relation between counterfactual explanations and adversarial exam-
ples. Minds and Machines, 33. https://doi.org/10.1007/s11023-021-09580-9
Ganev, G., & De Cristofaro, E. (2025). The inadequacy of similarity-based privacy metrics: Privacy attacks
against “truly anonymous” synthetic datasets. In: 2025 IEEE Symposium on Security and Privacy (SP),
pp. 4007–4025. IEEE Computer Society, Los Alamitos, CA, USA . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / S P 6 1 1 5 7 . 2 0
2 5 . 0 0 2 1 8 . h t t p s : / / d oi . i e e e c o m p u t e r s o c i e t y . o r g / 1 0 . 1 1 0 9 / S P 6 1 1 5 7 . 2 0 2 5 . 0 0 2 1 8
Geiler, L., Affeldt, S., & Nadif, M. (2022). A survey on machine learning methods for churn prediction. Inter-
national Journal of Data Science and Analytics, 14, 1–26. https://doi.org/10.1007/s41060-022-00312-5
Guidotti, R. (2022). Counterfactual explanations and how to find them: Literature review and benchmarking.
Data Mining and Knowledge Discovery, 38, 1–55. https://doi.org/10.1007/s10618-022-00831-6
Guidotti, R., & Ruggieri, S. (2021). Ensemble of counterfactual explainers. In: Explainable AI: Interpreting,
Explaining and Visualizing Deep Learning, . https://doi.org/10.1007/978-3-030-88942-5_28
Huh, J., & Lee, W. (2024). Privacy-preserving consumer churn prediction in telecommunication through
federated machine learning. In: 2024 IEEE International Conference on Big Data and Smart Computing
(BigComp), pp. 355–356 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / B i g C o m p 6 0 7 1 1 . 2 0 2 4 . 0 0 0 6 6
Hyrup, T., Lautrup, A. D., Zimek, A., & Schneider-Kamp, P. (2025). A systematic review of privacy-preserv-
ing techniques for synthetic tabular health data. Discover Data, 3(1), 5. h t t p s : / / d oi . o r g / 1 0 . 1 0 0 7 / s 4 4 2 4
8 - 0 2 5 - 0 0 0 2 2 - w
Joy, U. G., Hoque, K. E., Nazim Uddin, M., Chowdhury, L., & Park, S.-B. (2024). A big data-driven hybrid
model for enhancing streaming service customer retention through churn prediction integrated with
explainable AI. IEEE Access, 12, 69130–69150. https://doi.org/10.1109/ACCESS.2024.3401247
1 3

230 Page 26 of 27 Machine Learning (2025) 114:230
Kanamori, K., Takagi, T., Kobayashi, K., Ike, Y., Uemura, K., & Arimura, H. (2021). Ordered counterfactual
explanation by mixed-integer linear optimization. Proceedings of the AAAI Conference on Artificial
Intelligence, 35, 11564–11574. https://doi.org/10.1609/aaai.v35i13.17376
Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T.-Y. (2017). Lightgbm: A highly
efficient gradient boosting decision tree. In: Proceedings of the 31st International Conference on Neural
Information Processing Systems (NeurIPS 2017), pp. 3146–3154
Laugel, T., Lesot, M.-J., Marsala, C., Renard, X., & Detyniecki, M. (2019). The dangers of post-hoc interpret-
ability: Unjustified counterfactual explanations. In: Proceedings of the 28th International Joint Confer-
ence on Artificial Intelligence (IJCAI), pp. 2801–2807 . https://doi.org/10.24963/ijcai.2019/388
Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout the customer journey.
Journal of Marketing, 80(6), 69–96. https://doi.org/10.1509/jm.15.0420
Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. In: Proceedings of
the 31st International Conference on Neural Information Processing Systems. NIPS’17, pp. 4768–4777.
Curran Associates Inc., Red Hook, NY, USA
Maldonado, S., López, J., & Vairetti, C. (2020). Profit-based churn prediction based on minimax probability
machines. European Journal of Operational Research, 284(1), 273–284. h t t p s : / / d oi . o r g / 1 0 . 1 0 1 6 / j . e j o
r . 2 0 1 9 . 1 2 . 0 0 7
Maneewongvatana, S., & Mount, D. M. (1999). Analysis of approximate nearest neighbor searching with
clustered point sets . arXiv:abs/cs/9901013
Mishra, A., & Reddy, U. S. (2017). A comparative study of customer churn prediction in telecom industry
using ensemble based classifiers. In: 2017 International Conference on Intelligent Computing and Con-
trol (ICICI), pp. 721–725 . https://doi.org/10.1109/ICICI.2017.8365230
Mothilal, R. K., Sharma, A., & Tan, C. (2020). Explaining machine learning classifiers through diverse coun-
terfactual explanations. In: Proceedings of the 2020 Conference on Fairness, Accountability, and Trans-
parency. FAT* ’20, pp. 607–617. Association for Computing Machinery, New York, NY, USA . h t t p s : / /
d o i . o r g / 1 0 . 1 1 4 5 / 3 3 5 1 0 9 5 . 3 3 7 2 8 5 0
Nauta, M., Trienes, J., Pathak, S., Nguyen, E., Peters, M., Schmitt, Y., Schlötterer, J., Van Keulen, M., &
Seifert, C. (2023). From anecdotal evidence to quantitative evaluation methods: A systematic review
on evaluating explainable ai. Acm Computing Surveys, 55(13s), 1–42. https://doi.org/10.1145/3583558
Patki, N., Wedge, R., & Veeramachaneni, K. (2016). The synthetic data vault. In: 2016 IEEE International
Conference on Data Science and Advanced Analytics (DSAA), pp. 399–410 . h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 /
D S A A . 2 0 1 6 . 4 9
Petkovski, A., Risteska Stojkoska, B., Trivodaliev, K., & Kalajdziski, S. (2016). Analysis of churn prediction:
A case study on telecommunication services in macedonia. In: 2016 24th Telecommunications Forum
(TELFOR), pp. 1–4 . https://doi.org/10.1109/TELFOR.2016.7818903
Qian, Z., Callender, T., Cebere, B., Janes, S. M., Navani, N., & Schaar, M. (2024). Synthetic data for privacy-
preserving clinical risk prediction. Scientific Reports, 14(1), 25676. h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2
4 - 7 2 8 9 4 - y
Rankin, D. R., Black, M., Bond, R., Wallace, J., Mulvenna, M., & Epelde, G. (2020). Reliability of super-
vised machine learning using synthetic data in health care: Model to preserve privacy for data sharing.
JMIR Medical Informatics, 8(7), Article 18910. https://doi.org/10.2196/18910
Samoilescu, R.-F., Looveren, A. V., & Klaise, J. (2021). Model-agnostic and Scalable Counterfactual Expla-
nations via Reinforcement Learning . arxiv:abs/2106.02597
Sharma, S., Henderson, J., & Ghosh, J. (2020). Certifai: A common framework to provide explanations and
analyse the fairness and robustness of black-box models. In: Proceedings of the AAAI/ACM Confer-
ence on AI, Ethics, and Society. AIES ’20, pp. 166–172. Association for Computing Machinery, New
York, NY, USA . https://doi.org/10.1145/3375627.3375812
Stepin, I., Alonso, J., Catala, A., & Pereira-Farina, M. (2021). A survey of contrastive and counterfactual
explanation generation methods for explainable artificial intelligence. IEEE Access, 9, 11974–12001.
https://doi.org/10.1109/ACCESS.2021.3051315
Tan, J., Xu, S., Ge, Y., Li, Y., Chen, X., & Zhang, Y. (2021). Counterfactual explainable recommendation. In:
Proceedings of the 30th ACM International Conference on Information and Knowledge Management
(CIKM), pp. 1784–1793 . https://doi.org/10.1145/3459637.3482420
1 3

Machine Learning (2025) 114:230 Page 27 of 27 230
Theodoridis, G., & Tsadiras, A. (2022). Applying machine learning techniques to predict and explain sub-
scriber churn of an online drug information platform. Neural Computing and Applications, 34(22),
19501–19514. https://doi.org/10.1007/s00521-022-07603-9
Tung, T. (2024). Unlocking the ai-powered customer experience: Personalized service, enhanced engage-
ment, and data-driven strategies for e-commerce applications. Journal of Infrastructure, Policy and
Development 8, 4970 https://doi.org/10.24294/jipd.v8i7.4970
Warren, G., Delaney, E., Guéret, C., & Keane, M. T. (2024). Explaining multiple instances counterfactually:user
tests of group-counterfactuals for XAI. In: ICCBR. Lecture Notes in Computer Science, vol. 14775, pp.
206–222. Springer, ???
Xiong, Y., Tao, J., Zhao, S., Wu, R., Shen, X., Lyu, T., Fan, C., Hu, Z., Zhao, S., & Pan, G. (2023). Explain-
able AI for cheating detection and churn prediction in online games. IEEE Transactions on Games,
15(2), 242–251. https://doi.org/10.1109/TG.2022.3173399
Xu, L., Skoularidou, M., Cuesta-Infante, A., & Veeramachaneni, K. (2019). Modeling tabular data using
conditional gan. In: Neural Information Processing Systems . h t t p s : / / a p i . s e m a n t i c s c h o l a r . o r g / C o r p u s I
D : 1 9 5 7 6 7 0 6 4
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
1 3