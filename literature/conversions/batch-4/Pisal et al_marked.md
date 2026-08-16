---
conversion_metadata:
  converted_at: "2026-07-21T08:09:42Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Pisal et al.pdf"
  source_pdf_sha256: "161a0b35c6bc25a5aaa1bd5a7dfbf45e380b19981bf9a191e045e52782b6db4c"
  page_count: 23
  markdown_char_count: 204324
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

www.nature.com/scientificreports

An integrated TOPSIS and ARAS 
method multi-criteria decision-
making approach for optimizing 
investment portfolios using 
goal programming and genetic 
algorithm model

Prajwal Pisal1, Kiran Kumar Reddy2, Jaydeep Kishore3, Ram Reddy Jonnalagadda4, 
Manish Kumar5, Gayathri Band6 & B. P. Joshi7

As the portfolio optimization field grows, classical techniques often notoriously find it difficult to 
efficiently model how investors decisions, risk tolerances, and asset attributes intertwine. This paper 
presents an innovation-based hybrid method, where Technique for Order Preference by Similarity to 
Ideal Solution (TOPSIS) combined with Additive Ratio Assessment (ARAS) for multi-criteria decision 
making, Goal Programming (GP) and a Genetic Algorithm (GA) for finding constraints are united. The 
proposed approach enhances the accuracy of ranking and effectiveness of allocation by incorporating 
asset evaluation, characterization of investors and probabilistic construction of portfolios. The system 
is tested in view of various performance implications, using the FAR-Trans dataset, a collection of 
genuine transaction statistics and asset pricing, as well as investor data. The first step involves project 
transaction capacities partitioning and risk categorization to create a bipartite TOPSIS–ARAS scoring 
mechanism. The GP part of the model matches investment decisions to the individual return and risk 
expectations of each investor, and the GA promotes the use of entropy-aware strategies. Important 
performance metrics are a Sharpe Ratio of 2.241, the annualized return of 4.6% and diversification 
score of 0.845. The study also reflects a 0.729 correlation between TOPSIS–ARAS rankings, and GP 
configurations leading to portfolio returns of over 30.0%. The system offers a realistic depiction of the 
behavior of investors, considering several transaction channels and different risk factors as well as 
geographies. The comprehensive integration is very flexible, computationally effective and based on 
realistic investment models while minimizing constraint deviation.

Keywords  Portfolio optimization, Multi-criteria decision-making (MCDM), TOPSIS, ARAS, Goal 
programming (GP), Genetic algorithm (GA), Investment strategies, Risk management

Background and motivation
The current financial environment calls on investors to operate in volatile markets, deal with complex risks and 
align their financial objectives with market constraints. Investors today do not only want the highest possible 
returns.  Models  that  are  based  on  one  objective  frequently  fail  to  respond  to  the  complexity  of  the  modern 
investment  dilemma,  which  is  why  MCDM  frameworks  are  required  to  optimize  portfolios  with  informed

1Department  of  Computer  Science,  California  State  University  (Alumni),  Monterey  Bay,  Seaside,  CA  93955, 
USA.  2Department  of  Computer  Science,  Jawaharlal  Nehru  Technological  University,  Kukatpally,  Hyderabad, 
Telangana 500085, India.  3Department of Artificial Intelligence and Machine Learning, Manipal University Jaipur, 
Jaipur  303007,  India.  4Department  of Computer Science, Osmania University, Amberpet,  Hyderabad, Telangana 
500007, India. 5Department of Electronic and Communication Engineering, Annamalai University, Chidambaram, 
Tamil Nadu 608002, India. 6School of Management, Ramdeobaba University, Nagpur 440013, India. 7Department 
of  Mathematics;  Department  of Computer Science  &  Engineering, Graphic  Era  Hill University,  Bhimtal Campus, 
Bhimtal 263132, India. email: jaydeep.kishore@jaipur.manipal.edu

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

1

---

<!-- PAGE 2 -->

www.nature.com/scientificreports/

choices1,2.  The  TOPSIS  and  ARAS  methods,  of  all  available  MCDM  frameworks3,4,  have  recently  gained 
popularity as options for decision makers. TOPSIS assesses alternatives in relation to how closely they match the 
ideal and anti-ideal situations and has a powerful discrimination ability, even between assets that are similar in 
terms of performance5. Alternatively, ARAS determines rankings by summing normalized performance ratios, 
resulting in a strong algorithm for controlling scaling and zero values6–8.

Conventional portfolio optimization approaches
The  integration  of  TOPSIS  and  ARAS  generates  a  complete  model  that  drastically  enhances  the  robustness 
of  decision-making  processes.  TOPSIS  is  good  at  understanding  faint  differences  among  highly  comparable 
alternatives, whereas ARAS brings stability through additive aggregation. The combination of both techniques 
results in the reduced sensitivity to normalization factors, reduces the number of rank reversals, and produces a 
more reliable initial screening of investment portfolios9–11.

While such MCDM models offer certain advantages, they are primarily confined to the ranking phase and do 
not directly contribute to asset allocation decisions. In the realm of high-stakes portfolio construction, merely 
identifying the top-performing alternatives is inadequate; it is essential to determine the optimal allocation levels 
that satisfy a range of investor-specific constraints. This necessity calls for the application of Goal Programming 
(GP), a mathematical method that models trade-offs among multiple financial objectives, in conjunction with 
Genetic Algorithms (GA), a bio-inspired evolutionary optimization technique proficient in navigating extensive, 
nonlinear, and high-dimensional investment landscapes12–14.

In the dynamic field of financial investment, portfolio optimization involves not only maximizing returns 
but  also  meeting  multiple,  often  conflicting,  investor  objectives15.  These  objectives  encompass  minimizing 
risk, maintaining liquidity, adhering to regulatory constraints, and aligning with investor capacity and sectoral 
preferences.  As  financial  markets  continue  to  evolve,  so  too  must  the  models  that  guide  capital  allocation 
decisions. While traditional portfolio optimization techniques provide a foundational basis, they increasingly 
fall short in addressing the multidimensional nature of real-world investor behavior16.

Conventionally,  two  major  approaches  have  significantly  contributed  to  the  discipline.  Multi-Criteria 
Decision-Making  (MCDM)  structures  and  solutions  from  quantitative  optimization  processes.  MCDM 
methods—such  as  AHP,  TOPSIS,  VIKOR,  ELECTRE,  and  ARAS—are  widely  utilized  to  rank  investment 
options analyzed on the basis of financial indicators such as return, risk, liquidity, and stability17–20.

These approaches21,22 create a clear framework of value judging, including both factual information and the 
investors’ personal views. They continue to be limited in terms of using these frameworks to control real assets 
primarily  because  there  are  no  mechanisms  for  determining  how  much  to  invest  in  each  asset  or  imposing 
limitations  like  budgetary  constraints  or  return  goals.  In  contrast,  models  based  purely  on  optimization,  for 
example, mean–Variance Optimization (Markowitz), Goal Programming (GP), and methods such as Genetic 
Algorithms (GA) are created to numerically optimize returns in terms of risk23–25.

Although they can deliver practical results within certain limitations, these models tend to work independently 
of the investor’s particular goals and behavioral inclinations. In the absence of a formalized system of ranking 
preferences,  these  models  may  allocate  assets  that,  while  theoretically  optimal,  do  not  correspond  to  what 
investors actually want or are willing to tolerate in the form of risk.

The gap between preference modeling and portfolio optimization has created ad hoc solutions that struggle 
to  bring  together  high-quality  decision,  efficient  updating  and  algorithmic  practicality.  The  segregation  of 
asset  choice  and  portfolio  formation  in  real-life  scenarios  is  likely  to  produce  less  than  optimal  investment 
plans,  particularly  in  cases  where  there  are  multiple  objectives  which  include  return,  risk  management,  and 
diversification.

Proposed hybrid framework
To  overcome  these  hurdles,  an  integrated  modular  framework  will  be  proposed  in  this  paper  to  combine 
decision-making systems and optimization subjected to constraints. The essence of this approach is that two-
tier MCDM model is used that is based on TOPSIS when the distances are measured and ARAS when additive 
normalization  is  considered.  This  is  enhanced  by  a  Goal  Programming  (GP)  formulation  with  optimization 
according to the particular constraint parameters of the investors combined with a Genetic Algorithm in order 
to arrive at maximum allocation within the GP defined feasible domain of the solution. This way individual 
preferences  which  are  established  in  investment  decisions  are  customized  and  allocation  of  resources  is 
streamlined to an established set of goals. The model is tested on the FAR-Trans dataset that involves combining 
investor transactions, demographics, pricing, and financial instruments.

It is proposed to make an advanced hybrid method suggesting the integration of TOPSIS, ARAS and goal 
programming and Genetic Algorithms to perform as an optimization technique. This complex model supports 
the concept of prioritized decision making and efficient resource allocation within the conditions of the practical 
circumstances.  The  framework  presents  an  opportunity  of  combining  the  qualitative  decision  making  with 
quantitative optimization that can transcend various market conditions and able to use large sets of data.

Research contribution and scope
Not only is the proposed system as accurate and adjustable as traditional models, or more so, but it also has 
an  adjustable  scale  with  a  more  understandable  design  that  aligns  well  with  the  current  digital  investment 
platforms. This research improves the application of multi-objective portfolio optimization26,27 through the use 
of preference modeling, rule-based decision logic, and evolutionary computation.

Although isolated applications of MCDM techniques and optimization algorithms show success, the field 
of investment portfolio optimization lacks a comprehensive methodology that combines subjective preference 
modeling  and  computational  optimization.  Techniques  such  as  TOPSIS  that  identify  relative  rankings  based

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

2

---

<!-- PAGE 3 -->

www.nature.com/scientificreports/

on  the  closeness  to  a  best  solution,  and  ARAS  that  uses  additive  normalization  to  create  a  balanced  scoring 
system, are constrained in modelling capital allocation or practical limitations without integration. For example, 
sometimes Goal Programming (GP)28,29 or Genetic Algorithms (GA) are used in the optimization of investments, 
but they rarely involve prior decision-preference modeling, which makes them ineffective in dealing with the 
goals of stakeholders30,31.

Taking  this  gap  into  consideration,  there  is  a  critical  need  for  a  strong  methodology  that  combines  the 
decision-making skills of TOPSIS and ARAS with the optimization methods of GP and GA32–35. The absence of 
integration results in the inefficient selection process of assets, poorly optimized allocation plans and inadequate 
adaptability to different multi-objective investment landscapes.

Conventionally, the traditional portfolio optimization models make use of Multi-Criteria Decision-Making 
(MCDM) tools such as TOPSIS or AHP to assess and rank possible investment options. Conversely, they also 
use optimisation techniques like Goal Programming or Genetic Algorithms, and in many cases they use only 
quantitative measures of return and risk in their analysis. Such methods lack the capacity to incorporate opinion 
of investors that is subjective, consider variable restrictions, and reflect dynamic features of feedback.

Its suggested technique integrates the qualitative and the quantitative analysis into a single decision-support 
framework. It is possible to assume that one of the starting points is investor segmentation, which leads to the 
adoption of a two-level TOPSISARAS approach to scoring financial instruments in accordance with the return, 
risk, and liquidity. This is followed with the imposition of constraints on investor specific investments such as 
wanted returns and budget limits via a flexible Goal Programming technique coupled with a Genetic Algorithm 
balancing the entropy and diversification with the optimal allocation. The prevalence of these elements enables 
the given approach to maximize the accuracy, reactiveness, and employability by the different sort of investors.

On the basis of the findings in the earlier limits of the system shown in Fig. 1, the goal of this research is the 
development of a modular framework of portfolio optimisation combining the stages harmoniously. This paper 
proposes the usage of a two-layer MCDM framework that combines ARAS and TOPSIS and thereby introduces 
enhanced performance of this framework. By combining TOPSIS and ARAS, we obtain a multidimensional and 
reliable analysis of possible investments based on such factors as return, risk, and liquidity.

A Goal Programming (GP) model is incorporated into the framework, designed to accurately define investor 
goals and restrictions, so that it would be possible to effectively address multiple objectives at the same time. In 
order to increase the accuracy of allocation decisions, the GP model is supplemented by a Genetic Algorithm, 
which explores the whole feasible space in search of optimal or suboptimal asset weight assignments.

Experimental results validate the superiority of the integrated model: decision accuracy, risk-return ratios, 
and the efficiency of processing are improved as compared to traditional models. In addition, the practical utility 
of the model is tested against standard financial benchmarks, illustrating the model’s ability to adjust to different 
types of investors and changing market environments.

While related works such as Wu et al36,37. and Wang et al38. have applied MCDM and optimization models to 
portfolio selection, this study advances those contributions by integrating complementary MCDM techniques 
(TOPSIS + ARAS), hybridizing deterministic and evolutionary optimizers (GP + GA), and validating the model 
using a behavior-driven dataset. The distinction lies not merely in integration but in the sequential structure and 
investor-specific adaptability of the framework.

Related works
Multi-criteria  decision  models  have  become  indispensable  in  portfolio  selection  because  they  are  needed 
to  address  the  challenges  of  pursuing  conflicting  investment  goals  simultaneously.  The  central  position  of 
procedures such as the Analytic Hierarchy Process (AHP) in the formation of structured decision-making was 
then succeeded by the introduction of improved ranking systems like the TOPSIS, in their work5,39, used an 
AHP–TOPSIS methodology to rank Colombian stock options according to return, risk, and liquidity.

Fig. 1.  Overview of the proposed hybrid investment portfolio optimization model which integrates MCDM, 
Goal programming and genetic algorithm layers.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

3

---

<!-- PAGE 4 -->

www.nature.com/scientificreports/

Moreover,  financial  scenarios  have  used  different  outranking  methods,  including  ELECTRE-TRI  and 
FlowSort, together with AHP and TOPSIS. These models are able to successfully combine investment choices 
in complex preference frameworks because of the results presented by40, so offering useful advice in discrete 
portfolio management.

This topic of research deals with employment and comparison of different Multi-Criteria Decision-Making 
(MCDM) techniques like TOPSIS, VIKOR and COPRAS in general of Tehran Stock Exchange. The paper shows 
that  MCDM  models  are  valuable  flexible  appliances  in  the  Finance  industry  during  decision-making.  ARAS 
method has been commended especially because it is an additive assessment method which enables analysts to 
be able to rate alternatives using standardized scores against best benchmark8,41,42.

The thing is that the separate use of TOPSIS or ARAS still has limitations. It is notable that TOPSIS is very 
sensitive to outliers and normalization and ARAS would not be very effective in finding alternatives that are 
similar  to  one  another.  Combining  these  two  approaches  will  allow  the  decision-makers  to  benefit  from  the 
complementary properties of these techniques: rank stability can be achieved with ARAS due to their linear 
utility  functions,  and  TOPSIS  is  more  powerful  to  differentiate  since  the  distances  between  points  and  ideal 
states are Euclidean. This systematic combination of appraisal each neutralizes the drawbacks of the other two 
approaches  and  strengthens  the  entire  assessment  process  of  making  critical  decisions  at  the  asset-filtering 
level43,44.

Resource allocation or optimization can be considered as one of the important phases of investment planning 
because Multi-Criteria Decision-Making (MCDM) methods45 may facilitate the selection and rankings however 
they do not provide the actual stage of resource allocation. Given the modeled multiple soft and hard constraints 
(return thresholds, risk caps, and so on liquidity quotas), GP provides a powerful framework to model them. 
Chopra  and  Chopra  (2005)  have  shown  the  usefulness  of  GP  in  the  process  of  fitting  the  projects  portfolio 
goals46, by making minimum deviations towards the set priorities. It has turned out to be a strong metaheuristic 
that can explore vast and non-linear financial landscapes, the benefits of which have use been applied in asset 
allocation and risk diversification12.

To  enhance  adaptability  in  uncertain  financial  environments47,48,  introduced  a  hybrid  decision-making 
model that integrates fuzzy MCDM49,50 with multi-objective mathematical optimization. This approach enables 
decision-makers to account for interval uncertainty in input data, thereby improving the robustness of portfolio 
selection  when  precise  values  are  either  unavailable  or  volatile. This  contribution  is  particularly  pertinent  in 
capital markets, where ambiguity in forecasting and the evaluation of subjective criteria often impede decision 
consistency.

While individual methodologies have achieved a certain level of maturity, a significant gap remains in the 
literature, as only a limited number of studies have proposed a comprehensive framework that integrates Multi-
Criteria Decision-Making (MCDM) with both Goal Programming (GP) and Genetic Algorithms (GA). Existing 
approaches often conclude after the decision-ranking phase or proceed with optimization using predetermined 
weights,  without  incorporating  preference  modeling.  Although51  introduced  a  two-phase  MCDM  plus 
optimization model, it did not integrate complementary MCDM methods (e.g., TOPSIS and ARAS) and failed 
to incorporate both deterministic (GP) and stochastic (GA) optimization techniques.

In  a  recent  study51,  utilized  the  Non-Dominated  Sorting  Genetic  Algorithm  III  (NSGA-III)  for  multi-
objective portfolio optimization, focusing on risk-return trade-offs, as well as kurtosis and skewness metrics. 
Their methodology effectively generated Pareto-optimal fronts for complex investment strategies, outperforming 
traditional  mean–variance  models  in  addressing  conflicting  financial  objectives.  However,  the  study  did  not 
incorporate a structured pre-optimization filtering mechanism using preference-based models, such as MCDM, 
which  led  to  an  indiscriminate  search  across  the  entire  portfolio  space  without  strategic  prioritization.  This 
underscores the need for a hybridized approach, wherein qualitative evaluation methods, such as TOPSIS and 
ARAS52,53,  can  serve  as  an  initial  screening  layer,  followed  by  NSGA-III  or  GA-based  optimization  to  refine 
allocation decisions.

This  study  addresses  a  critical  gap  in  the  literature  by  introducing  a  comprehensive  hybrid  model.  The 
suggested  approach  begins  by  taking  an  integrated  TOPSIS-ARAS  MCDM  layer  to  filter  the  portfolios  after 
which this outcome is used as an input to a Goal Programming module that allows taking into consideration the 
objectives, which exist and form of the investor. The final optimization is executed through Genetic Algorithms. 
This  three-tiered  approach  facilitates  scalable,  intelligent,  and  preference-aligned  portfolio  optimization, 
representing a significant advancement over existing fragmented models.

Methodology and mathematical formulation
Figure 2 presents a modular architecture that employs feedback mechanisms to optimize portfolios with multiple 
objectives. The process initiates with the acquisition of raw data on investors and assets from the FAR-Trans 
dataset. Subsequently, the system categorizes investors based on their risk profiles and investment capacities. 
The pre-processing phase includes Z-score normalization, one-hot encoding of categorical data, and time-based 
filtering to establish the decision matrix.

Combining  the  TOPSIS  to  rank  by  distance  with  ARAS  to  provide  ratio  score,  the  MCDM  framework 
acquires the total asset rank within its two-level performance. When assets fail to rank according to the threshold 
specified, there is a need to alter constraints or reweighting of assets. The Goal Programming (GP) model will be 
applied to incorporate the goals the investor has specified especially in terms of returns, risk and budget limits 
on the amount of the assets above the agreed limit. Following this, the Genetic Algorithm (GA) optimization 
module refines position weights via fitness calculations and introduces operators, which are Simulated Binary 
Crossover (SBX), mutation, and seek to maximize the return and prioritize the penalties undertaken.

Optimal sector resultant and balanced weight assignment have a big impact on the final assets allocation. 
These  allocations  are  analyzed  with  the  help  of  such  key  performance  indicators  as  Sharpe  Ratio,  Return  on

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

4

---

<!-- PAGE 5 -->

www.nature.com/scientificreports/

Fig. 2.  Workflow of the proposed hybrid MCDM–GP–GA framework for intelligent portfolio Optimization.

Investment (ROI), Volatility. When original results fail to meet standards, the framework offers the modifications 
via repetition of first steps, i.e. recalculation of MCDM scores or adjustment of constraints, thus, maintaining 
the closed-loop process. The application of this framework results in agile and investor-oriented portfolios that 
display versatility and dependability under differing financial circumstances and guidelines.

As shown in Fig. 2, the MCDM scoring layer outputs a ranked list of assets based on investor preferences, 
which then forms the input set for Goal Programming (GP) and Genetic Algorithm (GA) modules. The flow 
from behavioral data to optimization is thus preserved across all stages.

Dataset overview and preprocessing
This research presents the FAR-Trans dataset54, a publicly available dataset that is specifically intended to support 
research in financial asset recommendation. The Far-Trans dataset includes anonymized retail investor activity, 
comprehensive tracking of asset prices, and profiles of investors, obtained from a leading European financial 
institution for the period January 2018 to November 2022. A systematic preprocessing pipeline was designed, 
which  includes  elimination  of  redundancies,  standardization  of  price  discrepancies  and  harmonization  of 
transaction records. Categorical variables were pre-processed with one-hot encoding, and continuous variables 
were scaled through min–max normalization to be compatible with multiple machine learning techniques. The 
preference  data  of  investors  in  the  form  of  risk  toleration  and  investment  capacity  were  obtained  to  enable 
specific methods of recommendation. Also, the current research evaluates the effectiveness of eleven algorithms 
to recommend financial assets on the dataset.

This study is aimed at coming up with a well-matched product suggestion system on the surety of customer 
finances. The dataset includes customer transaction history and the product details. The categorical columns 
were converted to one-hot encoded format to allow numeric input to be used in machine learning models. To 
put continuous features on the same scale, in terms of importance of all the features, minmax scaling was carried 
out. Moreover, user-item matrix was adapted in the study to explore the preferences and behaviours of users 
thereby helping in creation of customized recommendation strategies.

This paper is related to the investigation of the accuracy of five machine learning techniques in the matter 
of  financial  risk  assessment.  The  data  contains  different  types  of  financial  details,  and  pertinent  customer 
data. Min–max scaling has been done as  an  adjuvenation  process of  the  data to normalize the ranges of the 
independent variables to make the data fit to modeling. The categorical variables were encoded using one-hot 
encoding to make them friendly to the machine learning. These preprocessing steps ensured that the data could 
be used in the machine learning models and therefore gave a more equal chance of evaluating the performance 
of the various approaches in financial risk assessment.

The input data on the MCDM layer was taken out of the FAR-Trans data. These were both categorical and 
numerical variables, including the rate of returns, the standard deviation, the popularity of assets and the score 
of  investor  preferences.  The  decision  matrix  X = [x  ij  ]  with  each  row  corresponding  to  an  alternative  i  and 
each column to a criterion j was constructed. Categorical data were treated by one-hot encoding and numerical 
data by min–max normalization to obtain the range of [0,1]. The TOPSIS and ares based on this process of the 
standardized matrix in the following section.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

5

---

<!-- PAGE 6 -->

www.nature.com/scientificreports/

Multi-criteria decision-making layer: TOPSIS and ARAS
In recent past, portfolio analysis has diversified in its reach by the adoption of multi-criteria aids that increase 
the  investment  selections  as  well  as  their  orientations  favoring  the  investor  interests.  In  determining  stock 
performance  on  risk,  returns,  and  liquidity,  a  meaningful  research  effort  was  employed,  which  involved 
application  of  a  hierarchical  ranking  technique  in  identifying  stock  performance  of  the  same.  The  method 
employed the standardization of financial measures as well as the distance-based assessment to rank investment 
alternatives, a factor that would assist investors in developing areas to make wiser choices.

Researchers  attempted  to  determine  the  best  strategies  to  adopt  in  the  selection  of  stocks  using  additive 
scoring  and  relative  closeness  as  aspects  of  a  comparative  analysis. The  models  were  used  for  the  analysis  of 
a matrix of normalized financial indicators and then the stability of rankings and weight correction based on 
investors’ preferences was assessed. It was discovered that there was great match between the ordering done by 
the models and the historical returns of assets traded in various exchanges.

A later investigation employed a two-staged process that first entailed the evaluation of asset options through 
a normalized multi-criterion scoring process with even weighting factors. The resulting ranked outputs in turn 
guided an optimization module, which showed the relevance of a structured pre-selection in terms of reducing 
computation  needs  and  improving  investment  performance.  Such  implementations  reflect  the  increasing 
adoption of the structured ranking methods in investment decision-making, and, specifically, those involving 
normalized performance indicators, distance metrics, and additive scoring to match investor-specific priorities.
The model for the integration of TOPSIS and ARAS proposed in this paper brings forward a hybrid scoring 
system designed to achieve more robust and stable asset rankings. details the methodology of this integration, 
making the asset ranking process both differentiated and stable, complying with the investors’ preferences. To 
improve methodological transparency and reproducibility, we present the dual-layer MCDM model (TOPSIS 
and ARAS) with clear step-wise computations and variable definitions. Each equation is aligned with the hybrid 
scoring mechanism that guides the portfolio filtering stage. The TOPSIS component emphasizes distance from 
ideal  solutions,  while  ARAS  focuses  on  additive  ratios.  Their  fusion  balances  differentiation  and  stability  in 
portfolio ranking.

Step 1 Normalize the Decision Matrix.
For TOPSIS: Use vector normalization

rT OP SIS
ij

=

xij
m
i=1 x2

ij

where: xij is the original score of the ith alternative on the jth criterion, m is the number of alternatives.

√∑

Result: Scales each criterion vector-wise for fair comparison.
For ARAS: Normalize using additive method

rARAS
ij

=

xij
m
i=1 xij

This method makes each criterion sum to 1, preserving relative proportions.

∑

Step 2 Weighted Normalized Matrix

vT OP SIS
ij

= wj.rT OP SIS
ij

; vARAS
ij

= wj.rARAS
ij

(1)

(2)

(3)

where wj is the weight assigned to the jth criterion based on importance.

Step 3 Identify Ideal Solutions (TOPSIS only).
We determine the Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS) based on the nature of each

criterion. Benefit criteria use maximum values for PIS, whereas cost criteria use minimum values.

Positive Ideal Solution (PIS):

A+ =

{

max(Xij)for beneﬁt, min(Xij) for cost criteria

}

Negative Ideal Solution (NIS):

A− =

{

min(Xij)for beneﬁt, max(Xij) for cost criteria

}

(4)

(5)

Step 4 Compute Separation Measures (TOPSIS).

For each alternative, we compute the Euclidean distance from both PIS and NIS. This quantifies how far each

alternative lies from ideal and non-ideal solutions.

n

s+
i =

s−i =

(vij

−

j )2
v+

(cid:31)
(cid:30)
(cid:30)
(cid:29)

j=1
(cid:28)

n

(vij

−

v−j )2

(cid:31)
(cid:30)
(cid:30)
(cid:29)

j=1
(cid:28)

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

(6)

(7)

6

---

<!-- PAGE 7 -->

www.nature.com/scientificreports/

s+
i  Distance of alternative i from PIS, s−i  Distance of alternative i from NIS.

n is the number of alternatives.
Step 5 Calculate TOPSIS Closeness Coefficient.
The closeness coefficient C T OP SIS

I

reflects the relative nearness of each alternative to the ideal. A higher

coefficient indicates better suitability.

C T OP SIS

I

=

S−i

S+

i −

S−i

(8)

where C T OP SIS
I
Step 6 Compute ARAS Utility Scores:
We compute the ARAS utility score U ARAS

I

∈ [0,1] with higher values indicating better alternatives.

as the ratio of the total weighted performance of an asset to

that of the ideal alternative.

Ideal alternative A0: composed of best values per criterion.
Utility degree of each alternative:

U ARAS

I

=

n

ij

j=1 vARAS
j=0 vARAS

ij

n
∑
∑

(9)

where vARAS

ij

Score of the ideal alternative under ARAS, U ARAS

I

- Higher values indicate better performance.

Clarification on data for TOPSIS and ARAS
The  input  data  for  the  MCDM  process  was  constructed  from  the  FAR-Trans  dataset.  The  dataset  included 
key indicators such as historical return, standard deviation, Sharpe ratio, investment volume, and behavioral 
preference scores. All numerical features were normalized using min–max scaling to the [0,1] range to ensure 
compatibility across both TOPSIS and ARAS methods. Categorical variables were either pre-ranked or encoded 
appropriately prior to inclusion.

Ideal and anti-ideal construction
In the TOPSIS method, the Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS) are constructed for 
each criterion. For benefit criteria (e.g., return, Sharpe ratio), PIS is the maximum value among alternatives; 
for cost criteria (e.g., standard deviation), PIS is the minimum value. These are defined formally in Eqs. (4) and 
(5). The ARAS method, by contrast, constructs an optimal alternative with the best normalized values across all 
criteria as a reference for ratio-based utility scoring.

Interpretation of rankings
The  scores  obtained  from  both  methods—closeness  index  in  TOPSIS  and  utility  index  in  ARAS—are  fused 
using a convex combination (Eq. 10). This combined score ϕi ensures that the final rankings are balanced across 
geometric and additive perspectives, mitigating method-specific biases.

Step 7 Combine TOPSIS and ARAS Scores.
Using a convex combination controlled by parameter

score φI

∈ [0,1] we fuse both scores to derive a final hybrid

∝

φI =

∝ ·

C T OP SIS

i

+ (1

)C ARAS
i

− ∝

(10)

φI Final hybrid score of alternative i.
Where 
Step 8 Rank Alternatives.
All alternatives are ranked based on descending φ I value. The top-ranking assets proceed to the optimization

[0,1] controls weight between the two methods (e.g., α = 0.5: equal fusion).

∝∈

layer.

Mathematical insights for the integrated framework
The final score ϕi (Eq. 10), calculated via a convex combination of the TOPSIS and ARAS scores, is used to rank 
all investment alternatives. The top-N ranked assets are selected and passed as inputs to the Goal Programming 
and Genetic Algorithm stages. This ensures that only alternatives satisfying investor-defined preference filters 
are considered during portfolio optimization. The Hybrid Scoring Mechanism combines TOPSIS (Technique 
for  Order  of  Preference  by  Similarity  to  Ideal  Solution)  and  ARAS  (Additive  Ratio  Assessment)  to  rank 
investment portfolios. This amalgamation kind of model will ensure that we exploit the respective merits of the 
two approaches to overcome their respective demerits. The following is the mathematical form that supports this 
combined scoring mechanism.

1.  Convex Combination Validity

The suggested structure of hybrid scoring mechanism solves the several drawbacks of applying the stand alone 
MCDM methods because it is a combination in a convex form used to combine the two scoring systems-TOPSIS 
and ARAS. TOPSIS is coupled with ARAS to provide a more consistent and stable decision-making framework 
since  the  above  approaches  balance  proximity  of  ideal  solutions  with  the  normalized  additive  performance. 
The convex fusion also ensures that the final score can be any number between 0 and 1 and is interpretable and

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

7

---

<!-- PAGE 8 -->

www.nature.com/scientificreports/

Pareto optimal amongst conflicting objectives. This step will bring a strong interface between the qualitative 
decision making and quantitative optimization and is expected to help filters portfolio candidates on the basis 
of investor interests. The initial mathematical procedure to prove the consistency of the score is to show that the 
total score, which is abbreviated as Phi i, is in the normalized range.

We combine the TOPSIS score (C T OP SIS

I

) and the ARAS score (C ARAS

I

) as a weighted average:

φI =

∝

.C T OP SIS

I

+ (1

)U ARAS
I

− ∝

(11)

where: α is a parameter that controls the relative weight assigned to TOPSIS and ARAS. It lies in the range 0 ≤ 
≤1, C T OP SIS
 is the score from TOPSIS, indicating how close the alternative is to the ideal solution, U ARAS
I
the score from ARAS, indicating how well an alternative rank based on the additive ratio.

I

∝
 is

2.  Pareto Optimality Alignment:

The hybrid approach ensures Pareto optimality by balancing risk and returns without sacrificing one objective 
for the other. In multi-objective optimization, an alternative is Pareto optimal if no other solution can improve 
one objective without worsening another. The hybrid scoring mechanism ensures this by combining the outputs 
of TOPSIS and ARAS, each of which evaluates different aspects of the investment portfolio (e.g., TOPSIS for 
proximity to the ideal, ARAS for stability). By integrating both, the system provides a balanced solution that 
maximizes return while minimizing risk.

The  value  of  the  convex  weight  parameter  α  determines  the  relative  influence  of  the  geometric  scoring 
(TOPSIS)  and  additive  scoring  (ARAS)  components.  While  α = 0.5  represents  an  equal-weighted  fusion,  the 
rationale for this choice is empirically supported. As part of a sensitivity analysis (refer to Online Appendix A), 
we tested α 
 {0.3, 0.5, 0.7} and compared resulting asset rankings using Kendall’s τ coefficient. The stability 
of rankings across these α values validates the selection of α = 0.5, which yielded a τ > 0.89 with both adjacent 
settings, indicating robust and consistent ranking behavior.

∈

Goal programming formulation
In portfolio management, optimization-based allocation strategies often utilize deviation minimization models 
to balance the dual objectives of maximizing returns and minimizing risk. Recent studies have incorporated 
mathematical  programming  formulations  that  prioritize  multiple  financial  objectives  within  investor-defined 
tolerances. One such study introduced a multi-objective framework that encoded investor preferences into a 
constrained programming model, enabling the simultaneous achievement of return expectations and risk limits. 
The model employed deviation variables to quantify the underachievement or overachievement of investment 
goals and ensured feasibility through capital allocation and non-negativity constraints and governed by Eq. (12).

Goal programming model formulation
Objective function

n

Min

(d+

j + d−j )

j=1
∑

(12)

j :  Overachievement  (positive  deviation)  from  target,  d−j :  Underachievement  (negative  deviation)

where:  d+
from target.
Constraints:

1.  Return Constraints:

2.  Risk constraint:

3.  Budget constraint:

4.  Bounds on weights:

n

i=1
∑

xiri + d−1 −

d+
1 = R

∗

n

i=1
∑

xiσi + d−2 −

d+
2 = σ

∗

xi = B

n

i=1
∑

0

xi ≤

1

i

∀

≤

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

8

---

<!-- PAGE 9 -->

www.nature.com/scientificreports/

Variable Definitions:

Allocation weight of asset i
Expected return of asset i
Risk (e.g., standard deviation) of asset i
Target return set by investor
Acceptable risk threshold
Total budget

xi 
ri 
σi 
R∗ 
σ* 
B 
d+
j , d−j :  Positive and negative deviations for each constraint j
Empirical  analysis  proved  that  the  application  of  both  budgetary  controls  and  performance  objectives  in  an 
optimized  allocation  system  was  beneficial.  Disparities  from  established  return-risk  metrics  were  penalized 
thus asset weights became the core decision variables. Minimized cumulative deviation ensured that the final 
allocation honored investor preference and all the relevant legal investment limits. Further work has examined 
the effectiveness of goal-driven approaches, with explicit modeling of objectives which permit variable financial 
constraints.  Such  models  generally  produce  useable  intermediate  allocation  proposals,  which  can  then  be 
optimized with metaheuristic or evolutionary algorithms, thus showing the flexibility of mathematical models to 
hybrid decision-making environments. In compliance with this approach, the goal programming model applies 
a similar methodology, which seeks to minimize the sum of positive and negative variances from return and 
risk benchmarks, established by investors, under the constraints of capital allocation and feasibility. This result 
yields a goal-compliant allocation vector, which can be enhanced by using global optimization algorithms such 
as Genetic Algorithms.

Optimization via genetic algorithm
Genetic Algorithms (GA) were used in an evolutionary context to improve the intermediate allocation vector 
produced by goal programming. Using Genetic Algorithms in financial optimization situations is advantageous 
because they can easily explore large problem spaces and always escape local optima. The approach uses the logic 
of natural selection to iteratively and optimize solutions with respect to a set fitness criterion.

The first population was obtained from the feasible solution space produced by the goal programming model 
while ensuring that all the chromosomes adhered to the capital budget constraints and non-negativity limits. 
Each  genetic  representation  represents  a  possible  investment  portfolio,  and  genes  encode  for  the  allocation 
fraction of a given asset.

The  fitness  function  was  devised  to  optimize  the  equilibrium  between  maximizing  expected  returns  and

imposing penalties for constraint violations. It is formally articulated as:

The GA optimization was conducted with the following parameterized configuration, enabling reproducibility

as shown in Eq. (13):

Fitness =

n

n

xiri

λ

−

xiσi

σ∗

−

(cid:30)
(cid:30)
(cid:30)
(cid:30)
(cid:30)

(cid:30)
(cid:30)
(cid:30)
(cid:30)
(cid:30)

i=1
(cid:31)

i=1
(cid:31)
where xi is the weight of asset i, ri and σi are the return and risk of asset i, respectively, σ∗ is the target portfolio 
risk, λ is a penalty coefficient balancing return vs. constraint deviation.
The sample parameters are:
Population Size: 100.
Crossover Operator: Simulated Binary Crossover (SBX), probability Pc = 0.9
Mutation Operator: Gaussian Mutation with adaptive variance, initial mutation rate Pm = 0.1
Selection Strategy: Tournament selection (size = 3).

(13)

Fitness Function
Penalty Coefficient λ 50 (used to balance risk-return violation)
Termination Condition 100 generations or if best fitness value stagnates for 10 iterations
Resulting Outcome The GA-converged portfolio had a Sharpe Ratio of 2.24, ROI of 4.6%, and budget deviation 
of €36.2M.

To ensure that the selection of the penalty coefficient λ is not arbitrary, we performed a controlled sensitivity 
analysis using λ 
 {10, 25, 50, 100}. For each value, the portfolio’s Sharpe ratio, budget deviation, and constraint 
adherence were evaluated. The setting λ = 50 produced the most stable and high-performing results as shown 
in Table 1 across different investor profiles, offering an optimal balance between return maximization and risk 
deviation control.

∈

In  order  to  justify  the  comparative  advantage  of  the  suggested  TOPSISARASGPGA  framework,  we  have 
benchmarked  the  proposed  framework  to  the  classical  Markowitz  mean  variance  model  and  multi-objective 
evolutionary  approach  like  NSGAIII  and  MOPSO.  To  state  that  a  fair  comparison  was  made,  all  the  models 
were tried with the same datasets, constraints, and performance measures. As is evidenced in Table 1 and radar 
plot in Figure XX, the proposed framework outperformed in Sharpe ratio, ROI and diversification across the 
board as well as being competitive or exceeding in budget ensuring. The proposed method had a more balanced 
performance in all evaluation metrics than when compared with NSGA-III and MOPSO which resulted in a 
trade-off  where  it  performed  well  only  in  one  dimension  at  the  cost  of  the  others.  It  can  be  concluded  that 
the  combination  of  dual-MCDM  ranking  with  genetic  algorithm  and  goal  programming  gives  a  very  strong 
enhancement of the conventional methods as well as the new ones under uniform test conditions.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

9

---

<!-- PAGE 10 -->

www.nature.com/scientificreports/

S. no λ value

Sharpe ratio ROI (%) Budget deviation (€M)

1

2

3

4

10

25

50

100

1.84

2.10

2.24

2.21

4.1

4.4

4.6

4.5

42.0

38.3

36.2

32.8

Table 1.  Sensitivity analysis of bias penalty coefficient (λ). Bold text represents most stable and high 
performing result.

Fig. 3.  Distribution across retail investor activity.

Tournament selection was employed to prioritize individuals with superior fitness levels, while Simulated 
Binary Crossover (SBX) was utilized to facilitate genetic recombination, with a crossover probability set at 0.9. 
Also, Gaussian mutation technique with adaptive mutation rate was used to maintain the population diversity 
and avoid early convergence. The genetic algorithm (GA) activity was terminated either when the number of the 
generations reached a limit fixed at 100 or when the global best fitness variation was less than a predetermined 
threshold within 10 transitions. This stochastic optimization step meant that the optimized portfolio that was 
finally  chosen  not  only  met  the  constraints  stipulated  by  this  investor  in  relation  to  his/her  goals,  but  also 
maximized the performance potential of the filtered asset set. The GA-modulated model was found attentive, 
resilient and of high quality solutions on basis of different investment profiles.

A  step-by-step  traceability  between  Eqs.  (1–10)  and  the  experimental  figures  is  documented  in  Online 
Appendix  A,  supporting  reproducibility  and  interpretability  of  the  proposed  framework.  The  portfolio 
allocation problem addressed in this study involves a nonlinear fitness function with penalty-based constraints 
for investor-specific goals (e.g., risk tolerance, diversification spread, and sectoral balance). These characteristics 
make the solution space non-convex and non-differentiable. Traditional exact methods like linear or quadratic 
programming may struggle with constraint violations and local optima. Therefore, a metaheuristic like Genetic 
Algorithm is preferred, offering robustness and flexibility in navigating the solution space to obtain near-optimal 
portfolios.

Results and discussion
The experimental evaluation of the proposed framework validates the integration of the TOPSIS–ARAS multi-
criteria decision-making model with goal programming and genetic algorithm-based optimization. Each visual 
outcome corresponds to a distinct modeling layer, ranging from investor profiling and asset evaluation to final 
optimization, demonstrating how the hybrid structure effectively translates theoretical constructs into practical 
portfolio allocations.

Investor behavior and initial MCDM screening
Figure 3 illustrates a pronounced bullish inclination, with 59% of 359,128 transactions being purchases. This 
long-term  accumulation  trend  aligns  with  the  model’s  TOPSIS–ARAS-based  initial  scoring,  which  filters  for 
stable, liquid assets—favoring portfolios with buy-side dominance and sustained profitability potential.

Figure 4 illustrates how investor profiles, such as risk tolerance and budget capacity, are parameterized into 
the model. These values are directly mapped into the GP model as constraint targets (e.g., R∗, σ∗, B) and provides 
a  detailed  analysis  of  investor  demographics,  highlighting  the  predominance  of  the  “Mass”  and  “Premium” 
customer  segments.  The  ‘Mass’  and  ‘Premium’  segments  represent  over  80%  of  investor  profiles,  serving  as 
empirical constraints for capital and risk thresholds in GP-based optimization. Customer classes were aligned 
with corresponding risk tolerances and investment capacity bands, which were subsequently utilized in both 
Goal  Programming  (to  ensure  alignment  between  return  and  risk)  and  Genetic  Algorithm  boundaries  (to 
uphold capital feasibility).

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

10

---

<!-- PAGE 11 -->

www.nature.com/scientificreports/

Fig. 4.  Mass and premium investor segments.

Fig. 5.  Capital-based investor stratification.

Figure 4 illustrates that 61% of customers are categorized as 'Mass,' contributing to 55.3% of transactions. 
This segment played a crucial role in budget modeling during the pre-processing phase (Section A), facilitating 
the enforcement of capital-based constraints in GP.

Risk segmentation and constraint vector mapping
The model’s ability to personalize for individual investors is demonstrated in Fig. 5, which indicates that the 
majority of participants fall within the CAP_LT30K tier. Additionally, the intermediate categories (CAP_30K–
80K and CAP_80K–300K) also showed significant activity. This segmentation is consistent with the preprocessing 
strategy described in Sect. 5.A methodology, where capacity-based feature encoding ensures that optimization 
adheres to investor-specific financial constraints.

Figure 5 visualizes how the return and deviation values (extracted from investor and market data) serve as 
inputs  to  the  GP  constraints,  influencing  optimal  allocation  strategies  and  it  substantiates  the  segmentation 
rationale: the CAP_LT30K group predominates. Although premium investors constitute a smaller cohort, they 
account for 55.6% of the total transaction value, underscoring the significance of dual modeling (capacity and 
influence) in preference embedding.

Figure 6 illustrates that “Balanced” and “Income” investors exhibit the highest levels of trading activity. These 
behavioral inputs serve as constraint vectors within the goal programming (GP) layer to minimize return-risk 
deviations for profiles characterized by moderate risk tolerance.

To  ensure  consistent  scoring  of  asset  alternatives  across  multiple  financial  criteria,  the  associated  raw 
indicators were normalized using vector-based (TOPSIS) and additive (ARAS) techniques, as shown in (1) and 
(2), respectively. This transformation supports comparability in the decision matrix prior to scoring and aligns 
directly with the hybrid ranking framework applied downstream.

Figure  7  presents  the  interaction  matrix  that  categorizes  transaction  behavior  by  investor  risk  profiles. 
Balanced and income investors together contributed to over 400,000 transactions, with Balanced profiles alone 
accounting for 243,000 trades in equities. Aggressive investors showed a pronounced preference for high-risk 
stocks,  with  92.6%  of  their  total  trades  directed  toward  equities.  In  contrast,  conservative  investors  leaned 
toward  MTFs  and  Bonds;  however,  52.5%  of  their  activity  still  involved  high-volatility  assets. These  patterns 
were quantitatively integrated into the MCDM framework using the TOPSIS closeness coefficient, calculated 
as per Eq. (8), which measures each asset’s relative proximity to an ideal profile. The resulting scores guided

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

11

---

<!-- PAGE 12 -->

www.nature.com/scientificreports/

Fig. 6.  Behavioral risk tolerance.

Fig. 7.  Preference mapping by investor type.

asset ranking in a behavior-aware manner, validating the effectiveness of the dual-stage TOPSIS–ARAS filtering 
in  aligning  recommendations  with  investor-specific  risk  preferences.  Figures  6  and  7  highlight  the  ranked 
alternatives produced through the hybrid TOPSIS–ARAS scoring. The top-ranked assets from these figures form 
the filtered candidate pool for the GP optimization process.

Based on Table 2, a population of 100 with 100 iterations showed a good trade-off between performance 
and computation cost. No significant improvement was seen beyond 100 iterations, confirming the parameter’s 
suitability. The best fitness plateaued after 80 generations, reflecting the effectiveness of early convergence in the 
optimization process.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

12

---

<!-- PAGE 13 -->

www.nature.com/scientificreports/

S. no Population size Max iterations

Sharpe ratio Convergence iteration Budget deviation (€M)

1

2

3

50

100

100

100

100

200

2.17

2.24

2.24

75

80

100

37.6

36.2

35.9

Table 2.  Genetic algorithm convergence and performance sensitivity with respect to population size and 
iteration count. Bold text represents good trade off between performance and computation cost.

α Pairs

Kendall’s Tau (τ) p-value

0.3 vs 0.5

0.92

0.3 vs 0.7

0.91

0.5 vs 0.7

0.94

0.0001

0.0002

0.0001

Table 3.  Kendall’s τ rank stability across α variations. Due to the presence of the α fusion parameter in all τ 
values, this is confirmed to have a high rank stability even though the parameter has been changed.

We accept that TOPSIS is susceptible to normalization options as well as extreme values. There are two design

elements that will make the proposed framework more robust:

1.  Dual-MCDM Fusion: The asset ranking stage adds scores of closeness in TOPSIS w/ARAS scores utilities 
through convex fusion coefficient, α, can thus obscure any individual method sensitivity to any normality.
 2.  Normalization  Scheme  Selection:  The  TOPSIS  will  be  normalized  using  a  vector  normalization  and  the 
ARAS will be normalized under min–max such that there is comparability of the scales and minimal distor-
tion due to the high magnitude attributes.

The test of sensitivity by changing the values of 2 in [0.3, 0.5, 0.7] and calculating the measure of correlation 
Kendall  2  correlation  of  the  results  of  ranking,  was  done  to  determine  stability.  The  findings  revealed  that 
0.9 > 0  in  each  case  which  is  a  high  rank  stability  even  with  changes  in  the  parameters.  We  also  carried  out 
outlier treatment through winsorizing (trimming to 1st-99th percentile) in pre-processing the data, increasing 
the effect of the extreme values, but not the discarding of important market signals. These results, as Table 3 
indicates, show all the values of τ are above 0.9 which implies that the stability of rank remains very high even 
though the parameters are altered.

The accurateness of the model will be based on the quality and completeness of both transaction data and 
asset attributes as they have the direct impact on the outputs of MCDM ranking, optimization of assets. Several 
safeguards are used in the pre-processing stage in an attempt to minimize data quality problems:

•  Numerical attributes which have missing values are imputed by sector-specific median values, so the relative

performance differences are not lost but the maximum bias is not as severe.

•  The  outlier’s  control  is  carried  out  through  winsorizing  1st  and  99th  percentiles  to  minimize  distortion  in

normalising steps of TOPSIS and ARAS.

•  The portfolios of investors who have not provided complete details are instead matched with the closest pre-
determined category (conservative, balanced, aggressive) using available values so that partial optimization is 
possible even without them but still with useful constraints.

Sensitivity  tests  indicated  that  random  deletions  of  up  to  5%  of  the  attributes  of  assets  or  transaction  logs 
produced  little  impact  over  final  ranks  (Kendall > 0.9),  whereas  greater  disparities  (> 10  percent)  contributed 
to  greater  variations  in  allocation  and  slight  reductions  in  the  Sharpe  ratio.  These  results  point  out  that  the 
framework is robust against moderate data defects and that data validation and enrichment will continue to help 
it make the most accurate decisions.

Asset evaluation, return profiling, and optimization result
Figure  8  demonstrates  a  significant  focus  on  public  securities,  which  constitute  94.7%  of  the  emphasis.  This 
allocation aligns with the ARAS-weighted preference for assets characterized by accessibility and transparency.
Figure 8 demonstrates a significant focus on public securities, which constitute 94.7% of the emphasis. This 
allocation aligns with the ARAS-weighted preference for assets characterized by accessibility and transparency.
The final asset ranking score ϕi, computed through a convex fusion of the TOPSIS closeness coefficient and 
ARAS utility score as formulated in (10), serves as the core input to the GP–GA optimization module. Figure 9 
presents the distribution of return on investment (ROI) across Stocks, Bonds, and MTFs, reflecting the impact 
of this ranking in guiding portfolio decisions. Equities exhibit outlier returns exceeding 80%, particularly within 
GA-optimized allocations favoring risk-tolerant investors. On average, stocks yielded a post-optimization ROI 
of 1.0%, while bonds reflected a marginally negative ROI of –0.017%. This contrast highlights the model’s ability 
to maintain ROI fidelity within defined risk boundaries.

Figure  10  further  explores  sectoral  volatility,  revealing  minimal  dispersion  in  Utilities,  Real  Estate,  and 
Technology sectors, and higher spread in Corporate and Communication Services. The GA module adaptively

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

13

---

<!-- PAGE 14 -->

www.nature.com/scientificreports/

Fig. 8.  Public, private and mutual fund holdings.

Fig. 9.  RoI across instrument types.

Fig. 10.  Risk spread analysis among financial sectors.

prioritized low-volatility sectors for Conservative and Balanced profiles, while selectively incorporating high-
risk sectors for Aggressive investors.

Figures 7 through 9 visualize how the individual MCDM components (TOPSIS and ARAS) and their hybrid 
score ϕi influence the overall ranking of assets. The high-scoring alternatives (based on ϕi) are then selected 
as input for the optimization phase. This shows the exact transformation of input data into actionable ranking 
decisions,  linking  the  investor  preference  matrix  with  actual  allocation  outcomes.  This  approach  enhances 
transparency and avoids black-box decision-making.

Technology  and  Utilities  achieved  optimal  Sharpe  ratios,  reinforcing  the  optimizer’s  capacity  to  balance 
profitability  with  entropy-controlled  diversification.  These  observations  validate  the  effectiveness  of  the 
integrated  scoring  and  optimization  framework  in  translating  investor-defined  constraints  into  robust  asset 
allocations.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

14

---

<!-- PAGE 15 -->

www.nature.com/scientificreports/

Fig. 11.  Asset-level trade-off surface showing normalized return vs. volatility. Color gradient represents 
assigned portfolio weight, with warmer colors indicating higher weight allocations.

Fig. 12.  Top 10 asset allocations across sectors. Financial Services dominates due to high scores in return-risk 
profile and MCDM-based ranking.

Figure 11 presents the scatter distribution of assets selected in the final portfolio, illustrating the trade-off 
surface achieved through Genetic Algorithm optimization. There is a large concentration in the 0- 0.10 volatility 
range which complies with the intent of having portfolio stability and a sizeable upside potential growth. The top 
half presents assets that present a 100% proportional build, this is when the model is sensitive to outliers of high 
returns. The color density will also highlight the asset weight concentration whereby higher-weighted assets will 
be showed both with low volatility and high returns which is due to the objective function driving towards fitness 
of the objective of returns but penalizing against the violation of risk objectives. The high vertical dispersion 
and low horizontal dispersion ensure that the model is highly correlated and Sharpe efficient according to the 
minimum vertical dispersion and minimal horizontal variance thus balancing diversification with profitability. 
It is also mapped on the basis of its regularized return and volatility scores. The color gradient reflects the final 
portfolio weight assigned to the asset, with warmer tones (e.g., green/yellow) indicating higher weights. This 
visualization makes it evident that the portfolio optimization model favors assets that exhibit high return with 
controlled or moderate volatility. Such characteristics reflect the goal programming objective of balancing return 
maximization and risk conformity.

Figure 12 shows the weight distribution among the top 10 selected assets, with “Financial Services” receiving 
the highest allocation. This outcome aligns with the feature-level dominance of this sector across key metrics. 
Specifically, assets in the financial services sector scored highly in the final ranking index ϕi, calculated from the 
hybrid TOPSIS–ARAS fusion (Eq. 10). These assets combined high return values with relatively low standard 
deviation, leading to favourable utility and closeness scores. In accordance with this, Fig. 12 illustrates the most 
significant instruments in the final solution. The Financial Services sector is predominant, with sovereign and 
investment-grade assets from Cyprus and Germany receiving the highest allocations. These assets demonstrate 
high-return,  low-volatility  characteristics  that  are  consistent  with  the  hybrid  scoring  and  optimization 
framework.  The  sectoral  representation  across  Sovereign  and  Corporate  classes  supports  the  diversification 
strategy implemented through entropy constraints, with no asset exceeding a 1.8% allocation—thereby affirming 
the entropy and risk parameters outlined in Section III.C.

The  quantitative  results  presented  in  the  Portfolio  Performance  Metrics  further  corroborate  these 
observations. A Sharpe Ratio of 2.241 demonstrates the framework’s ability to achieve exceptional risk-adjusted 
returns, particularly advantageous for conservative and balanced investors. The portfolio’s annualized return of 
4.6% and volatility of 3.2% align with the dual-objective formulation established during the Goal Programming 
phase.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

15

---

<!-- PAGE 16 -->

www.nature.com/scientificreports/

The diversification score of 0.845, obtained from an analysis of 79 assets across 13 sectors, substantiates the 
effectiveness of entropy control as outlined in Section III.C. Simultaneously, the liquidity measure of 23,493.59, 
although  below  the  benchmark  average,  reflects  a  strategic  asset  selection  approach  and  necessitates  future 
rebalancing  adjustments.  The  TOPSIS–ARAS  correlation  coefficient  of  0.729  indicates  a  strong  concordance 
in  rank,  despite  the  integrated  scoring  model.  Additionally,  the  budget  deviation  of  €36.2  M  highlights  the 
optimizer’s assertive asset inclusion decisions within the framework of global constraints.

The  V1  Portfolio  Metrics  were  obtained  from  a  hold-out  test  set  using  the  final  GP–GA  allocation  logic, 
providing an out-of-sample validation of wealth accumulation. Further validation from the V1 Portfolio Metrics 
indicates that the GP model achieved a 30.0% return with a volatility of only 3.1%, thereby demonstrating near-
perfect constraint satisfaction. The final portfolio consisted of 84 assets distributed across 9 sectors, achieving 
a diversification score of 0.823, which closely resembles that of the primary portfolio. Notably, only 3 of the top 
10 ARAS-ranked assets and none from TOPSIS were included in the final selection, highlighting the model’s 
preference for stochastic GA logic over deterministic rankings in optimizing asset allocation.

The formulation proposed of GP takes into consideration investor-specific objectives and risk tolerance as 
specific parameters, such as goal target return (R ∗), maximum acceptable level of risk (σ∗) budget constraints 
and diversification constraints. These parameters can be determined based on preloaded investor types (e.g., 
conservative, balanced, aggressive), and they are assigned numerical values by using industry standard financial 
planning targets. In order to test the influence of misspecification, we conducted a controlled variation analysis 
to alter both 2 hypothesized misspecification 2 by 10 percent in each condition, holding every other condition 
constant. Findings showed that preferential errors caused small changes in allocations within top-ranked assets 
with implications that moderate preference errors did not render the portfolio to be very sensitive. Conversely, 
when deviations were large (> 20%), more pronounced changes in patterns of allocation were elicited, as they 
were to be expected since these preferences directly affected the performance of optimization. This shows that 
the framework is able to translate subjective intentions of investors on portfolio actions successfully into the 
formulation of portfolio structures with the strength to resist reasonable specification error.

Sensitivity analysis of α for fusion score stability:
To verify the robustness of the asset rankings derived from Eq. (10), a sensitivity analysis was conducted on the 
convex combination weight α. We evaluated three values—α = 0.3, 0.5, and 0.7—and computed the Kendall rank 
correlation coefficient (τ) between each pair of ranked outputs. The resulting τ values were:

τ (0.3, 0.5) = 0.892

τ (0.5, 0.7) = 0.881

τ (0.3, 0.7) = 0.867

These results demonstrate that the ranking outputs are highly consistent across varying α, indicating that the 
model’s ranking logic is not overly sensitive to the selected fusion weight. Therefore, α = 0.5 is both mathematically 
interpretable and empirically stable.

Deployment feasibility and regional insights
Figure  13  elucidates  operational  behavior,  demonstrating  that  Internet  Banking  is  the  predominant  mode, 
accounting for approximately 250,000 transactions, thereby surpassing both Branch and Phone Banking. This 
behavioral pattern suggests that the proposed model is optimally suited for implementation in digital investment 
platforms that provide automated, preference-driven portfolio guidance.

Figure  13  highlights  the  operational  feasibility,  with  64.6%  of  all  transactions  being  executed  via  Internet 
Banking.  This  observation  supports  the  suitability  of  implementing  algorithmic  deployment  through  digital 
recommender platforms.

Fig. 13.  Channel-wise transaction behavior.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

16

---

<!-- PAGE 17 -->

www.nature.com/scientificreports/

Figure 14 illustrates that Greece leads in total portfolio activity, with an estimated €3 billion, followed by 
Germany  and  Luxembourg.  These  insights  are  essential  for  geographic  performance  profiling.  The  MCDM–
GP–GA framework can be effectively adapted to regional investment filters, allowing financial advisors to adjust 
ranking and optimization weights in alignment with country-specific market conditions and investor sentiment.
Figure 14 demonstrates that Greece is responsible for 99.5% of transactions, primarily conducted through 
the XATH exchange. These regional insights have been integrated to support the feasibility of country-specific 
Multi-Criteria Decision-Making (MCDM) scoring in future developments.

In the ‘GP-only’ baseline model, asset allocation is performed using the raw data inputs without filtering or 
scoring; the GP formulation (Section III.D) is solved using a deterministic linear solver (e.g., simplex-based). In 
the ‘MCDM + GP’ model, assets are first ranked using the hybrid scoring mechanism (ϕᵢ), and the top-N are fed 
into the same GP formulation without invoking GA. In the proposed full model, GA is used after GP to explore 
the feasible allocation space more flexibly, optimizing for investor-aligned risk-return profiles.

The  implementation  to  the  current  stage  is  dealing  with  a  single-period  optimization  cycle  although  the 
framework can be easily adjusted to fit dynamic market conditions. Assets rankings within the TOPSIS ARAS 
layer can be recomputed immediately that new market, industry, or macroeconomic data are loaded, and can 
be re-ranked on a periodic or ad-hoc basis. Likewise, the investor profiles, specified by target return (58), risk 
tolerance (59), and other restrictions, could change any time and this would fully or incompletely re-optimize 
the portfolio through the GP/GA module.

In case of high volatility conditions, the model facilitates incremental recalibration of model i.e., only assets 
with a high degree of score change is reprocessed thus cutting down computation time. This design can support 
scheduled rebalancing (e.g., daily, weekly), or dynamic in real time where investments are linked to a live data 
feed in case of a digital investment platform. It is modular in structure so that once the asset evaluation layer 
or set of preferences parameters is updated, the whole system does not need retraining or redesigning but can 
maintain an ongoing operation with a rapid response to the market changes.

Evaluation and analysis
Comparative baselines and ablation study
To  assess  the  efficacy  of  the  proposed  hybrid  model,  we  performed  an  ablation  study  by  comparing  the 
performance  of  various  configurations  through  the  isolation  or  removal  of  specific  components  within  the 
pipeline.

The  aim  of  this  study  was  to  evaluate  the  extent  to  which  each  methodological  component—MCDM 
(TOPSIS + ARAS), Goal Programming (GP), and Genetic Algorithm (GA)—contributes to the overall quality 
of the portfolio.

We established four baseline models, as depicted in Table 4. All baseline models, including NSGA-III, MOPSO, 
and other state-of-the-art techniques, were evaluated using the same dataset (FAR-Trans) and evaluation period. 
Where applicable, parameter settings were aligned with those reported in the original publications to ensure 
fairness. No model was retrained on out-of-sample data to preserve in-sample consistency. To visually reinforce 
the multi-criteria superiority of the proposed hybrid model, a radar plot (Fig. 15) has been added, highlighting 
performance across Sharpe Ratio, ROI, Diversification, and Budget Deviation.

Model A: MCDM-Only (TOPSIS–ARAS)
In this configuration, assets were evaluated utilizing the dual-ranking system, although no optimization layer

was implemented. Portfolios were constructed by allocating equal weights to the top-ranked assets.

Model B: GP-Only (without MCDM or GA)
This  model  employed  a  direct  GP  formulation  on  all  available  assets  without  prior  filtering.  Although 
constraints were adhered to, the absence of a scoring mechanism diminished alignment with investor preferences.

Model C: MCDM + GP (No GA)
In this study, asset ranking was conducted prior to integrating the shortlisted alternatives into the GP model.

The optimization process adhered to constraints, although it did not incorporate evolutionary refinement.

Model D: Full Hybrid (TOPSIS–ARAS + GP + GA)
(Proposed Model)
The  comprehensive  framework  integrates  Multi-Criteria  Decision  Making  (MCDM)  for  asset  selection,

Genetic Programming (GP) for constraint modeling, and Genetic Algorithms (GA) for global optimization.

Fig. 14.  Regional flow of investment activity.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

17

---

<!-- PAGE 18 -->

www.nature.com/scientificreports/

Model

AHP–TOPSIS

ELECTRE–TRI

FlowSort–BWM

Fuzzy-VIKOR

NSGA-III

MOPSO

BWM–ARAS

Deep Learning Forecast + MCDM

Hybrid GRA–TOPSIS

1.45

1.62

1.70

1.78

1.85

1.91

1.96

2.05

2.11

Proposed (TOPSIS–ARAS–GP–GA)

2.24

Sharpe ratio ROI (%) Diversification Budget deviation Reference

3.1

3.4

3.6

3.9

4.1

4.3

4.4

4.5

4.5

4.6

0.68

0.71

0.73

0.74

0.76

0.79

0.80

0.82

0.83

0.845

58.4

48.0

45.1

42.0

41.2

39.0

37.5

36.9

36.5

36.2

5

55

17

56

57

58

15

59

17

Proposed Work

Table 4.  Performance comparison between proposed framework and state-of-the-art portfolio optimization 
techniques. Bold text represents performance of our proposed method.

Fig. 15.  Radar plot comparing the proposed model against NSGA-III and MOPSO across four key portfolio 
metrics. The proposed model demonstrates superior balance across risk-adjusted return, diversification, and 
budget adherence.

Though  the  proposed  TOPSISARASGPGA  framework  incorporates  several  quantitative  techniques,  the 
proposed implementation within an asset management system is meant to reduce operating complexity on the 
part of the end-users. The modularity of its architecture enables the implementation of the individual components 
of the framework; MCDM ranking, goal programming optimization, and genetic algorithm refinement, to be 
the independent service modules in an asset management platform. This division makes it possible to perform 
parallel processing and integration with current decision-support systems.

To portfolio managers who are not well versed in each technique, the process can be represented by a user 
interface that just needs high-level inputs: selection of investor profile, target return, and risk level. Automation 
on the backend performs preprocessing steps, normalization, score fusion, and optimization, and displays result 
in appealing visual aids, including ranked lists of assets to be invested in, allocation charts, and a performance 
dashboard.

These  are  mainly  the  difficulties  of  deployment  (enough  computational  resources  to  support  large-scale 
portfolios, combining the framework with end-of-day market data feeds and model result validation across a 
variety of regulatory scenarios). These are covered using scalable cloud architecture, data pipeline automation 
and  parameter  presets  to  common  types  of  investors. Through  the  integration  of  automated  processing  with 
configurable  preference  entries,  the  methodology  could  be  of  practical  use  to  non-technological  users  even 
though it could still be methodologically intense.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

18

---

<!-- PAGE 19 -->

www.nature.com/scientificreports/

Fig. 16.  Flowchart of the genetic algorithm-based portfolio optimization process. Each portfolio is modeled 
as a chromosome of asset weights and evaluated using a fitness function based on return and risk deviation. 
The algorithm applies tournament selection, sbx crossover, gaussian mutation, and constraint repair to evolve 
optimal portfolio solutions under budget and diversification constraints.

Insights

•  The MCDM-Only configuration demonstrated satisfactory ranking quality; however, it was unable to effec-
tively balance risk and capital distribution, resulting in suboptimal performance in terms of the Sharpe ratio 
and diversification.

•  GP-Only models encountered challenges due to optimization within an expansive, unranked asset pool, fre-
quently  selecting  assets  that  were  technically  optimal  yet  impractical,  such  as  those  with  low  liquidity  or 
misaligned with investor objectives.

•  The integration of Multi-Criteria Decision Making (MCDM) with Goal Programming (GP) enhanced perfor-
mance by facilitating the early elimination of low-quality assets. However, it did not incorporate evolutionary 
fine-tuning.

•  The Full Hybrid model consistently demonstrated superior performance across all metrics, thereby affirming

the effectiveness of the sequential integration of MCDM, GP, and GA.

To  further  validate  the  effectiveness  of  the  proposed  integrated  TOPSIS–ARAS–GP–GA  framework,  we 
compared  it  with  several  state-of-the-art  portfolio  optimization  methodologies  published  between  2021  and 
2025.  As  shown  in  Table  4,  the  proposed  model  achieves  the  highest  Sharpe  Ratio  (2.24),  ROI  (4.6%),  and 
Diversification  Score  (0.845)  while  maintaining  the  lowest  Budget  Deviation  (€36.2  M),  outperforming  all 
referenced models. This comparative evaluation demonstrates the superior balance achieved by the proposed 
hybrid model between risk-adjusted performance and capital allocation feasibility, affirming its viability for real-
world deployment across investor profiles and market conditions.

Although  the  proposed  TOPSIS-ARAS-GP-GA  framework  incorporates  various  sophisticated  methods, 
the  staged  structure  makes  sure  that  the  proposed  framework  is  computationally  tractable.  MCDM  layer 
(TOPSIS + ARAS) acts as a pre-filter, that reduces the number of the passed candidate assets to be considered by 
the optimization stage significantly. Having reduced the search space, the GA component can easily converge 
early on—in tests with a population size of 100, this has occurred well before 80 iterations on average. This speed 
allows scalability up to large scale institution portfolios, and it also facilitates decision making in volatile markets 
in near real time. Furthermore, the modular layout enables parallel computations and re-optimization of any 
affected asset in an incremental way, in order to require no complete recalculation when updating the market.

Genetic algorithm pseudocode and optimization logic
The Genetic Algorithm (GA) functions as the ultimate optimization mechanism within the proposed hybrid 
framework, operating over the feasible solution space generated by the Goal Programming (GP) layer. GA is 
particularly  adept  at  addressing  non-linear,  high-dimensional  portfolio  allocation  challenges  under  multiple 
constraints, including return-risk trade-offs, budget compliance, and sector diversification.

In this model (Fig. 16), each portfolio is represented as a chromosome, with each gene corresponding to 
the  normalized  allocation  weight  of  a  specific  asset.  The  algorithm  iteratively  evolves  a  population  of  these 
chromosomes  across  successive  generations,  optimizing  the  portfolio’s  fitness  by  maximizing  returns  while 
imposing penalties for risk deviation.

Interpretability and explainability of portfolio outcomes
One  of  the  primary  strengths  of  the  proposed  hybrid  framework  is  its  inherent  interpretability,  which  is 
grounded in both the model’s structure and the visualization of its outputs. In contrast to black-box optimization 
techniques, the integration of MCDM scoring, goal-based constraint modeling, and evolutionary search allows 
each  phase  of  the  portfolio  construction  process  to  be  traced,  explained,  and  rationalized  in  alignment  with 
investor objectives.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

19

---

<!-- PAGE 20 -->

www.nature.com/scientificreports/

The  dual-layer  scoring  mechanism  involving  TOPSIS  and  ARAS  provides  transparent  justifications  for 
asset inclusion. TOPSIS ensures differentiation  based  on relative proximity to the ideal return–risk–liquidity 
profile,  while  ARAS  contributes  linear  additive  interpretability.  Assets  selected  for  shortlisting  can  be  traced 
directly to their normalized performance in each criterion, as illustrated in Section IV.C and supported by Fig. 9 
(Profitability by Asset Category) and Fig. 10 (Volatility by Sector).

In the Goal Programming formulation (Section III.C), investor-specific logic is encoded to model return and 
risk targets through the use of deviation variables. Consequently, the optimization outcome transcends a mere 
numerical solution, offering a decision-aware configuration that aligns with investor preferences, as illustrated 
in  Fig.  7  (Risk  Level × Asset  Category  Heatmap)  and  Fig.  12  (Top  10  Assets  in  Final  Portfolio).  These  visual 
representations enable stakeholders to comprehend the rationale underlying asset allocation, sectoral weighting, 
and the trade-offs imposed by budgetary and diversification constraints.

Moreover,  the  Genetic  Algorithm  enhances  interpretability  by  developing  solutions  through  quantifiable 
fitness  scores,  with  intermediate  generations  adhering  to  clearly  defined  rules,  such  as  mutation  limits  and 
sectoral exposure. As illustrated in Fig. 11 (Portfolio Risk–Return Profile), the algorithm’s output resembles the 
shape of an efficient frontier, which can be visually interpreted by both domain experts and end users.

The application of evaluation metrics such as the Sharpe Ratio, budget deviation, and entropy score enhances 
post  hoc  interpretability.  Such  measures  can  be  used  to  convert  intangible  goals  into  quantitative  financial 
measures not only recognizable to investors and analysts but also capable of closing the gap between what a 
model outputs and what it would mean to stakeholders. The proposed system guarantees that it is data-driven, 
transparent in its decisions by keeping a modular structure and by visual diagnostics at every level of ranging, 
constraint modeling and optimization. Such transparency is necessary in environments of digital investment 
where regulatory compliance, user trust and auditability are paramount to deployment of the model.

Limitations and future work
Despite significant advantages in terms of improved decision quality, constrained satisfaction rates, and aligning 
with investor interests, the proposed integrated framework of MCDM-GP-GA approach has some limitations 
that should be observed and expanded by means of the further investigations and development of the system.

Originally, the current model is expected to operate in a single period static optimization. This constrains 
its versatility to situations that entail fluctuation over investor preference as time varies or market data that is 
updated real time. The addition of dynamic rebalancing and multi-period optimization of the portfolio would 
make the model much more applicable to the realities of live financial planning systems and would allow tracking 
the performance much more effectively under time-varying risks.

Secondly, although Genetic Algorithm is good at the search of the search space that is high-dimensional, 
it is time-wasting. Convergence time is dependent  on  the  portfolio size  and  variety of the population which 
can  become  a  bottleneck  under  high-frequency  portfolio  recommendations.  Further  studies  can  involve  the 
combination of hybrid metaheuristics, including the Genetic Algorithm with the Particle Swarm Optimization 
(GA-PSO)  or  the  Ant  Colony  Optimization  (ACO)  in  order  to  reduce  the  computational  overhead  with  a 
retainment of the solution quality.

Thirdly, the existing framework assumes same investor constraints, like stationary budget constraints and 
the  linear  goals  of  the  investors  regarding  returns  and  risks.  In  real-life,  however,  fuzzy,  linguistic,  or  utility 
based preferences of the investor might be included. The model can be improved by integrating the fuzzy Multi 
Criteria Decision Making (MCDM) scoring or multi-utility Goal Programming (GP) as a means of representing 
complexities.

In addition, though, the current version lacks any inclusion of regulatory constraints, transaction costs and 
tax considerations. Integrating these real-world investment factors would enhance the framework’s readiness 
for deployment in regulated environments, such as robo-advisory platforms and institutional portfolio engines.
In conclusion, while the model facilitates visualization for interpretability, a more formal incorporation of 
Explainable AI (XAI) modules—such as SHAP or LIME—could be investigated to offer detailed justification for 
the inclusion and weight assignment of each asset. This approach would not only support regulatory compliance 
but also enhance user trust and system transparency.

Future iterations of this research will seek to address these gaps by developing the framework into a real-time 
adaptive decision-support engine that is aligned with personalized, explainable, and regulation-aware portfolio 
management.

Conclusion
This  study  introduces  an  innovative  hybrid  framework  for  optimizing  investment  portfolios  by  integrating 
Multi-Criteria Decision-Making (MCDM) methods—specifically, TOPSIS and ARAS—with constraint-driven 
Goal  Programming  (GP)  and  evolutionary  Genetic  Algorithms  (GA).  In  contrast  to  traditional  systems  that 
separate decision logic from optimization mechanics, the proposed model consolidates asset ranking, investor 
constraint modeling, and metaheuristic search into a unified, data-driven pipeline.

Utilizing  the  FAR-Trans  dataset,  the  model  underwent  validation  across  diverse  investor  profiles, 
demonstrating enhanced outcomes in terms of risk-adjusted return, diversification, and constraint satisfaction. 
The  application  of  visual  evaluation  metrics,  including  sectoral  volatility  plots,  risk-return  clustering,  and 
allocation  profiles,  augmented  the  interpretability  of  the  results  and  affirmed  the  framework’s  applicability 
in  real-world  scenarios.  While  the  primary  metrics  are  in-sample,  we  also  include  a  limited  out-of-sample 
validation  using  the  V1  portfolio  metrics.  Additional  tests  such  as  walk-forward  validation  are  proposed  for 
future research.

Experimental results indicated the model’s superiority through comparative baselines and ablation studies. 
With the help of the GA module and the dual MCDM layer, portfolio weight was optimized within the feasible

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

20

---

<!-- PAGE 21 -->

www.nature.com/scientificreports/

space of GP to score and filter assets from various perspectives. As a result, the model generated better Sharpe 
ratios, reduced budget variances, and provided more transparent insights than conventional or single-model 
approaches. Finally, this integrated framework brings a modular, scalable and transparent method of portfolio 
construction, effectively bridging investor driven decision models and robust computational optimization.

It  offered  the  TOPSIS-ARAS-GP-GA  framework  in  the  shape  of  multi-criteria/multi-objective  portfolio 
optimization  where  asset  scoring  is  qualitative  whereas  risk-return  optimization  is  quantitative.  The  staged 
design had a good computational efficiency as evidenced by pre-optimization filtering and early convergence 
of the GA which made them scalable to large portfolios. The robustness was established through a-sensitivity 
examination  (Kendall > 0.9)  tests  and  resistance  to  moderate  data  quality  concerns.  Using  benchmarking  on 
Markowitz, NSGA-III, MOPSO, it was found that it was better or equalled in all four measures of Sharpe ratio, 
ROI, diversification, and budget adherence.

Module-based  architecture  and  the  automated  processing  in  the  back  end  made  the  approach  practically 
applicable and available even to non-technical portfolio managers. The system can accomplish fast recalibration, 
as asset scores and investor profiles are refreshed with market data to enable periodic or issue-driven rebalancing. 
All of these features combined can provide stability, flexibility and usability within dynamic asset management 
settings,  though  future  efforts  are  concentrated  on  dynamic  rebalancing  and  hybrid  metaheuristics  to  adapt 
more quickly.

Data availability
The datasets analysed during the current study are available in the following repository:  [   h t t p s : / / d o i . o r g / 1 0 . 5 5 2 
5 / g l a . r e s e a r c h d a t a . 1 6 5 8     ] .

Received: 13 June 2025; Accepted: 25 August 2025

References
  1.  Tan,  T.,  Mills,  G.,  Papadonikolaki,  E.  &  Liu,  Z.  Combining  multi-criteria  decision  making  (MCDM)  methods  with  building

information modelling (BIM): A review. Autom. Constr. 121, 103451 (2021).

2.  Taherdoost,  H.  &  Madanchian,  M.  Multi-criteria  decision  making  (MCDM)  methods  and  concepts.  Encyclopedia  3(1),  77–87

(2023).

3.  Demir,  G.,  Chatterjee,  P.  &  Pamucar,  D.  Sensitivity  analysis  in  multi-criteria  decision  making:  A  state-of-the-art  research

perspective using bibliometric analysis. Expert Syst. Appl. 237, 121660 (2024).

4.  Francis,  &  Thomas,  A.  System  dynamics  modelling  coupled  with  multi-criteria  decision-making  (MCDM)  for  sustainability-

related policy analysis and decision-making in the built environment. Smart Sustain. Built Environ. 12(3), 534–564 (2023).
  5.  Vásquez, J. A., Escobar, J. W. & Manotas, D. F. AHP–TOPSIS methodology for stock portfolio investments. Risks 10(1), 4 (2021).
  6.  Ramón-Canul, L. G. et al. Technique for order of preference by similarity to ideal solution (TOPSIS) method for the generation of

external preference mapping using rapid sensometric techniques. J. Sci. Food Agric. 101(8), 3298–3307 (2021).

7.  Hatefi, S. M., Asadi, H., Shams, G., Tamošaitienė, J. & Turskis, Z. Model for the sustainable material selection by applying integrated

Dempster-Shafer evidence theory and additive ratio assessment (ARAS) method. Sustainability 13(18), 10438 (2021).

8.  Jing, D., Imeni, M., Edalatpanah, S. A., Alburaikan, A. & Khalifa, H. A. E. W. Optimal selection of stock portfolios using multi-

criteria decision-making methods. Mathematics 11(2), 415 (2023).

9.  Meidelfi, D., Idmayanti, R., Maulidani, F., Ilham, M. & Muhlis, F. A. Additive ratio assessment (ARAS) method in the selection of

popular mobile games. Int. J. Adv. Sci. Comput. Eng. 4(1), 56–66 (2022).

10.  Thakkar,  &  Chaudhari,  K.  A  comprehensive  survey  on  portfolio  optimization,  stock  price  and  trend  prediction  using  particle

swarm optimization. Arch. Comput. Methods Eng. 28(4), 2133–2164 (2021).

11.  Faheem, M., Aslam, M. & Kakolu, S. Artificial intelligence in investment portfolio optimization: A comparative study of machine

learning algorithms. Int. J. Sci. Res. Arch. 6(1), 335–342 (2022).

12.  Anadani, I., Sharma, A., Dave, D. &amp; Sharma, A. A genetic algorithm approach for portfolio optimization. In Proceedings of

international conference on data science and applications, 113–124 (Springer, 2023).

13.  Sornette,  D.  &  Lapeyre,  B.  Portfolio  optimization  and  genetic  algorithms,  In:  M.S.  thesis,  Department  of  Economics  Science

(University of Geneva, 1998).

14.  Al  Janabi,  M.  A.  Multivariate  portfolio  optimization  under  illiquid  market  prospects:  A  review  of  theoretical  algorithms  and

practical techniques for liquidity risk management. J. Model. Manag. 16(1), 288–309 (2021).

15.  Du, J. Mean–variance portfolio optimization with deep learning based-forecasts for cointegrated stocks. Expert Syst. Appl. 201,

117005 (2022).

16.  Liagkouras,  K.,  Metaxiotis,  K.  &  Tsihrintzis,  G.  Incorporating  environmental  and  social  considerations  into  the  portfolio

optimization process. Ann. Oper. Res. 316, 1–26 (2022).

17.  Sahoo, S. K. & Goswami, S. S. A comprehensive review of multiple criteria decision-making (MCDM) methods: Advancements,

applications, and future directions. Decis. Making Adv. 1(1), 25–48 (2023).

18.  Więckowski, J. et al. Recent advances in multi-criteria decision analysis: A comprehensive review of applications and trends. Int. J.

Knowl-Based Intell. Eng. Syst. 27(4), 367–393 (2023).

19.  Thakkar, J. J. Multi-Criteria Decision Making Vol. 336 (Springer, 2021). https://doi.org/10.1007/978-981-16-9448-3.
 20.  Singh, R. et al. A historical review and analysis on MOORA and its fuzzy extensions for different applications.  Heliyon 10(3),

e25453 (2024).

21.  Saini, M., Sengupta, E., Singh, M., Singh, H. & Singh, J. Sustainable development goal for quality education (SDG 4): A study on 
SDG 4 to extract the pattern of association among the indicators of SDG 4 employing a genetic algorithm. Educ. Inf. Technol. 28(2), 
2031–2069 (2023).

22.  Papazoglou, G. & Biskas, P. Review and comparison of genetic algorithm and particle swarm optimization in the optimal power

flow problem. Energies 16(3), 1152 (2023).

23.  Foroozandeh, Z., Ramos, S., Soares, J. & Vale, Z. Goal programming approach for energy management of smart building. IEEE

Access 10, 25341–25348 (2022).

24.  Heidari, M. D., Gandasasmita, S., Li, E. & Pelletier, N. Proposing a framework for sustainable feed formulation for laying hens: A

systematic review of recent developments and future directions. J. Cleaner Prod. 288, 125585 (2021).

25.  Mohseny-Tonekabony,  N.,  Sadjadi,  S.  J.,  Mohammadi,  E.,  Tamiz,  M.  &  Jones,  D.  F.  Robust,  extended  goal  programming  with 
uncertainty sets: An application to a multi-objective portfolio selection problem leveraging DEA. Ann. Oper. Res. 346, 1–56 (2024).

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

21

---

<!-- PAGE 22 -->

www.nature.com/scientificreports/

26.  Abadi,  M.  Q.  H.,  Rahmati,  S.,  Sharifi,  A.  &  Ahmadi,  M.  HSSAGA:  Designation  and  scheduling  of  nurses  for  taking  care  of 
COVID-19 patients using novel method of hybrid salp swarm algorithm and genetic algorithm. Appl. Soft Comput. 108, 107449 
(2021).

27.  Ashour, M. A. H., Ahmed, A. A. and Al-dahhan, I. A. H. Minimizing costs of transportation problems using the genetic algorithm. 
In Proceedings of sixth international congress on information and communication technology: ICICT 2021, U.K., vol. 1, 165–173, 
(Springer, 2021).

28.  Colapinto, C. & Mejri, I. The relevance of goal programming for financial portfolio management: A bibliometric and systematic

literature review. Ann. Oper. Res. 346(2), 917–943 (2025).

29.  Akbari, N., Jones, D. & Arabikhan, F. Goal programming models with interval coefficients for the sustainable selection of marine

renewable energy projects in the UK. Eur. J. Oper. Res. 293(2), 748–760 (2021).

30.  D’Agostino, D., Minelli, F. & Minichiello, F. New genetic algorithm-based workflow for multi-objective optimization of Net Zero

Energy Buildings integrating robustness assessment. Energy Build. 284, 112841 (2023).

31.  Chou, J. S. & Chen, K. E. Optimizing investment portfolios with a sequential ensemble of decision tree-based models and the FBI

algorithm for efficient financial analysis. Appl. Soft Comput. 158, 111550 (2024).

32.  Liu,  S.  &  Xiao,  C.  Application  and  comparative  study  of  optimization  algorithms  in  financial  investment  portfolio  problems.

Mobile Inf. Syst. 2021(1), 3462715 (2021).

33.  Montoya, O. D., Grisales-Noreña, L. F. & Perea-Moreno, A. J. Optimal investments in PV sources for grid-connected distribution

networks: An application of the discrete–continuous genetic algorithm. Sustainability 13(24), 13633 (2021).

34.  Razghandi, M., Dehghan, A. & Yousefzadeh, R. Application of particle swarm optimization and genetic algorithm for optimization

of a southern Iranian oilfield. J. Pet. Explor. Prod. Technol. 11, 1781–1796 (2021).

35.  Faridi,  S.,  Madanchi  Zaj,  M.,  Daneshvar,  A.,  Shahverdiani,  S.  &  Rahnamay  Roodposhti,  F.  Portfolio  rebalancing  based  on  a

combined method of ensemble machine learning and genetic algorithm. J. Financ. Report. Account. 21(1), 105–125 (2023).

36.  Wu,  Q.  et  al.  An  integrated  multi-criteria  decision-  making  and  multi-objective  optimization  model  for  socially  responsible

portfolio selection. Technol. Forecast. Soc. Chang. 184, 121977 (2022).

37.  Wu, Q., Liu, X., Qin, J. & Zhou, L. Multi-criteria group decision-making for portfolio allocation with consensus reaching process

under interval type-2 fuzzy environment. Inf. Sci. 570, 668–688 (2021).

38.  Wang, X., Wang, B., Li, T., Li, H. & Watada, J. Multi-criteria fuzzy portfolio selection based on three- way decisions and cumulative

prospect theory. Appl. Soft Comput. 134, 110033 (2023).

39.  Alsanousi, T., Alqahtani, A. Y., Makki, A. A. & Baghdadi, M. A. A hybrid MCDM approach using the BWM and the TOPSIS for a

financial performance-based evaluation of Saudi stocks. Information 15(5), 258 (2024).

40.  Emamat, M. S. M. M., Mota, C. M. D. M., Mehregan, M. R., Sadeghi Moghadam, M. R. & Nemery, P. Using ELECTRE-TRI and

FlowSort methods in a stock portfolio selection context. Financ. Innov. 8(1), 11 (2022).

41.  Amudha,  M.,  Ramachandran,  M.,  Saravanan,  V.,  Anusuya,  P.  &  Gayathri,  R.  A  study  on  TOPSIS  MCDM  techniques  and  its

application. Data Anal. Artif. Intell. 1(1), 09–14 (2021).

42.  Chodha, V., Dubey, R., Kumar, R., Singh, S. & Kaur, S. Selection of industrial arc welding robot with TOPSIS and entropy MCDM

techniques. Mater. Today Proc. 50, 709–715 (2022).

43.  Lin, S. S., Zhou, A. & Shen, S. L. Safety assessment of excavation system via TOPSIS-based MCDM modelling in fuzzy environment.

Appl. Soft Comput. 138, 110206 (2023).

44.  Wang, K., Ying, Z., Goswami, S. S., Yin, Y. & Zhao, Y. Investigating the role of artificial intelligence technologies in the construction 
industry using a Delphi–ANP–TOPSIS hybrid MCDM concept under a fuzzy environment. Sustainability 15(15), 11848 (2023).
 45.  Mogbojuri, A. O. & Olanrewaju, O. A. Goal programming and genetic algorithm in multiple objective optimization model for

project portfolio selection: A review. Niger. J. Technol. 41(5), 862–869 (2022).

46.  Lee, H., Kang, H. Y. & Chen, C. L. Multi-objective assembly line balancing problem with setup times using fuzzy goal programming

and genetic algorithm. Symmetry 13(2), 333 (2021).

47.  Iraj, M. Z. & Doaei, M. A hybrid decision-making model for optimal portfolio selection under interval uncertainty. Iran. J Account.

Audit. Financ. (IJAAF) 8(4), 2717 (2024).

48.  Shih, H. S. & Olson, D. L. TOPSIS and its Extensions: A Distance-Based MCDM Approach Vol. 447 (Springer, 2022).
 49.  Patel, A., Jana, S. & Mahanta, J. Intuitionistic fuzzy EM-SWARA-TOPSIS approach based on new distance measure to assess the

medical waste treatment techniques. Appl. Soft Comput. 144, 110521 (2023).

50.  Sathyan, R., Parthiban, P., Dhanalakshmi, R. & Sachin, M. S. An integrated fuzzy MCDM approach for modelling and prioritising 
the enablers of responsiveness in automotive supply chain using fuzzy DEMATEL, fuzzy AHP and fuzzy TOPSIS. Soft Comput. 
27(1), 257–277 (2023).

51.  Mwamba, J. W. M., Mbucici, L. M. & Mba, J. C. Multi-objective portfolio optimization: An application of the non-dominated

sorting genetic algorithm III. Int. J. Financ. Stud 13(1), 15 (2025).

52.  Chakraborty, S., Chatterjee, P. & Das, P. P. Additive ratio assessment (ARAS) method. In Multi-Criteria Decision-Making Methods

in Manufacturing Environments 171–181 (Apple Academic Press, 2023).

53.  Sihombing, V. et al. Additive ratio assessment (ARAS) method for selecting English course branch locations. Proc. J. Phys. Conf.

Ser. 933(1), 012070 (2021).

54.  Sanz-Cruzado, J., Droukas, N. & McCreadie, R. FAR-Trans: An investment dataset for financial asset recommendation. Preprint at

arXiv:2407.08692. (2024).

55.  Doaei, M., Dehnad, K. & Dehnad, M. A hybrid approach based on multi-criteria decision making and data-driven optimization in

solving portfolio selection problem. Opsearch 62(1), 1–36 (2025).

56.  Hwang, Y., Kong, Y., Zohren, S. & Lee, Y. Decision-informed neural networks with large language model integration for portfolio

optimization. Preprint at arXiv:2502.00828 (2025).

57.  Dominguez,  A.  R.,  Shahzad,  M.  &  Hong,  X.  Multi-hypothesis  prediction  for  portfolio  optimization:  A  structured  ensemble

learning approach to risk diversification. Preprint at arXiv:2501.03919 (2025).

58.  Mwamba, J. W. M., Mbucici, L. M. & Mba, J. C. Multi-objective portfolio optimization: An application of the non-dominated

sorting genetic algorithm III. Int. J. Financial Stud. 13(1), 15 (2025).

59.  Goswami, M., Dey, R. & Singh, A. An integrated TOPSIS-GRA model for sustainable investment selection. J. Clean. Prod. 350,

131528 (2023).

Author contributions
P. P and K.K. focused on the literature review, data processing, and model development. J. K supervised the study, 
while RRJ, MK, GB, and B. P. J. contributed to experimentation, result analysis, writing, and final proofreading.

Funding
Open access funding provided by Manipal University Jaipur. No Funding.

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

22

---

<!-- PAGE 23 -->

www.nature.com/scientificreports/

Declarations

Competing interests
The authors declare no competing interests.

Additional information
Supplementary Information The online version contains supplementary material available at  h t t p s : / / d o i . o r g / 1 
0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 5 - 1 7 6 0 4 - y     .

Correspondence and requests for materials should be addressed to J.K.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.

Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o 
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .

© The Author(s) 2025

Scientific Reports |        (2025) 15:34450

| https://doi.org/10.1038/s41598-025-17604-y

23

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

www.nature.com/scientificreports
OPEN An integrated TOPSIS and ARAS
method multi-criteria decision-
making approach for optimizing
investment portfolios using
goal programming and genetic
algorithm model
Prajwal Pisal1, Kiran Kumar Reddy2, Jaydeep Kishore3, Ram Reddy Jonnalagadda4,
Manish Kumar5, Gayathri Band6 & B. P. Joshi7
As the portfolio optimization field grows, classical techniques often notoriously find it difficult to
efficiently model how investors decisions, risk tolerances, and asset attributes intertwine. This paper
presents an innovation-based hybrid method, where Technique for Order Preference by Similarity to
Ideal Solution (TOPSIS) combined with Additive Ratio Assessment (ARAS) for multi-criteria decision
making, Goal Programming (GP) and a Genetic Algorithm (GA) for finding constraints are united. The
proposed approach enhances the accuracy of ranking and effectiveness of allocation by incorporating
asset evaluation, characterization of investors and probabilistic construction of portfolios. The system
is tested in view of various performance implications, using the FAR-Trans dataset, a collection of
genuine transaction statistics and asset pricing, as well as investor data. The first step involves project
transaction capacities partitioning and risk categorization to create a bipartite TOPSIS–ARAS scoring
mechanism. The GP part of the model matches investment decisions to the individual return and risk
expectations of each investor, and the GA promotes the use of entropy-aware strategies. Important
performance metrics are a Sharpe Ratio of 2.241, the annualized return of 4.6% and diversification
score of 0.845. The study also reflects a 0.729 correlation between TOPSIS–ARAS rankings, and GP
configurations leading to portfolio returns of over 30.0%. The system offers a realistic depiction of the
behavior of investors, considering several transaction channels and different risk factors as well as
geographies. The comprehensive integration is very flexible, computationally effective and based on
realistic investment models while minimizing constraint deviation.
Keywords Portfolio optimization, Multi-criteria decision-making (MCDM), TOPSIS, ARAS, Goal
programming (GP), Genetic algorithm (GA), Investment strategies, Risk management
Background and motivation
The current financial environment calls on investors to operate in volatile markets, deal with complex risks and
align their financial objectives with market constraints. Investors today do not only want the highest possible
returns. Models that are based on one objective frequently fail to respond to the complexity of the modern
investment dilemma, which is why MCDM frameworks are required to optimize portfolios with informed
1Department of Computer Science, California State University (Alumni), Monterey Bay, Seaside, CA 93955,
USA. 2Department of Computer Science, Jawaharlal Nehru Technological University, Kukatpally, Hyderabad,
Telangana 500085, India. 3Department of Artificial Intelligence and Machine Learning, Manipal University Jaipur,
Jaipur 303007, India. 4Department of Computer Science, Osmania University, Amberpet, Hyderabad, Telangana
500007, India. 5Department of Electronic and Communication Engineering, Annamalai University, Chidambaram,
Tamil Nadu 608002, India. 6School of Management, Ramdeobaba University, Nagpur 440013, India. 7Department
of Mathematics; Department of Computer Science & Engineering, Graphic Era Hill University, Bhimtal Campus,
Bhimtal 263132, India. email: jaydeep.kishore@jaipur.manipal.edu
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 1

www.nature.com/scientificreports/
choices1,2. The TOPSIS and ARAS methods, of all available MCDM frameworks3,4, have recently gained
popularity as options for decision makers. TOPSIS assesses alternatives in relation to how closely they match the
ideal and anti-ideal situations and has a powerful discrimination ability, even between assets that are similar in
terms of performance5. Alternatively, ARAS determines rankings by summing normalized performance ratios,
resulting in a strong algorithm for controlling scaling and zero values6–8.
Conventional portfolio optimization approaches
The integration of TOPSIS and ARAS generates a complete model that drastically enhances the robustness
of decision-making processes. TOPSIS is good at understanding faint differences among highly comparable
alternatives, whereas ARAS brings stability through additive aggregation. The combination of both techniques
results in the reduced sensitivity to normalization factors, reduces the number of rank reversals, and produces a
more reliable initial screening of investment portfolios9–11.
While such MCDM models offer certain advantages, they are primarily confined to the ranking phase and do
not directly contribute to asset allocation decisions. In the realm of high-stakes portfolio construction, merely
identifying the top-performing alternatives is inadequate; it is essential to determine the optimal allocation levels
that satisfy a range of investor-specific constraints. This necessity calls for the application of Goal Programming
(GP), a mathematical method that models trade-offs among multiple financial objectives, in conjunction with
Genetic Algorithms (GA), a bio-inspired evolutionary optimization technique proficient in navigating extensive,
nonlinear, and high-dimensional investment landscapes12–14.
In the dynamic field of financial investment, portfolio optimization involves not only maximizing returns
but also meeting multiple, often conflicting, investor objectives15. These objectives encompass minimizing
risk, maintaining liquidity, adhering to regulatory constraints, and aligning with investor capacity and sectoral
preferences. As financial markets continue to evolve, so too must the models that guide capital allocation
decisions. While traditional portfolio optimization techniques provide a foundational basis, they increasingly
fall short in addressing the multidimensional nature of real-world investor behavior16.
Conventionally, two major approaches have significantly contributed to the discipline. Multi-Criteria
Decision-Making (MCDM) structures and solutions from quantitative optimization processes. MCDM
methods—such as AHP, TOPSIS, VIKOR, ELECTRE, and ARAS—are widely utilized to rank investment
options analyzed on the basis of financial indicators such as return, risk, liquidity, and stability17–20.
These approaches21,22 create a clear framework of value judging, including both factual information and the
investors’ personal views. They continue to be limited in terms of using these frameworks to control real assets
primarily because there are no mechanisms for determining how much to invest in each asset or imposing
limitations like budgetary constraints or return goals. In contrast, models based purely on optimization, for
example, mean–Variance Optimization (Markowitz), Goal Programming (GP), and methods such as Genetic
Algorithms (GA) are created to numerically optimize returns in terms of risk23–25.
Although they can deliver practical results within certain limitations, these models tend to work independently
of the investor’s particular goals and behavioral inclinations. In the absence of a formalized system of ranking
preferences, these models may allocate assets that, while theoretically optimal, do not correspond to what
investors actually want or are willing to tolerate in the form of risk.
The gap between preference modeling and portfolio optimization has created ad hoc solutions that struggle
to bring together high-quality decision, efficient updating and algorithmic practicality. The segregation of
asset choice and portfolio formation in real-life scenarios is likely to produce less than optimal investment
plans, particularly in cases where there are multiple objectives which include return, risk management, and
diversification.
Proposed hybrid framework
To overcome these hurdles, an integrated modular framework will be proposed in this paper to combine
decision-making systems and optimization subjected to constraints. The essence of this approach is that two-
tier MCDM model is used that is based on TOPSIS when the distances are measured and ARAS when additive
normalization is considered. This is enhanced by a Goal Programming (GP) formulation with optimization
according to the particular constraint parameters of the investors combined with a Genetic Algorithm in order
to arrive at maximum allocation within the GP defined feasible domain of the solution. This way individual
preferences which are established in investment decisions are customized and allocation of resources is
streamlined to an established set of goals. The model is tested on the FAR-Trans dataset that involves combining
investor transactions, demographics, pricing, and financial instruments.
It is proposed to make an advanced hybrid method suggesting the integration of TOPSIS, ARAS and goal
programming and Genetic Algorithms to perform as an optimization technique. This complex model supports
the concept of prioritized decision making and efficient resource allocation within the conditions of the practical
circumstances. The framework presents an opportunity of combining the qualitative decision making with
quantitative optimization that can transcend various market conditions and able to use large sets of data.
Research contribution and scope
Not only is the proposed system as accurate and adjustable as traditional models, or more so, but it also has
an adjustable scale with a more understandable design that aligns well with the current digital investment
platforms. This research improves the application of multi-objective portfolio optimization26,27 through the use
of preference modeling, rule-based decision logic, and evolutionary computation.
Although isolated applications of MCDM techniques and optimization algorithms show success, the field
of investment portfolio optimization lacks a comprehensive methodology that combines subjective preference
modeling and computational optimization. Techniques such as TOPSIS that identify relative rankings based
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 2

www.nature.com/scientificreports/
on the closeness to a best solution, and ARAS that uses additive normalization to create a balanced scoring
system, are constrained in modelling capital allocation or practical limitations without integration. For example,
sometimes Goal Programming (GP)28,29 or Genetic Algorithms (GA) are used in the optimization of investments,
but they rarely involve prior decision-preference modeling, which makes them ineffective in dealing with the
goals of stakeholders30,31.
Taking this gap into consideration, there is a critical need for a strong methodology that combines the
decision-making skills of TOPSIS and ARAS with the optimization methods of GP and GA32–35. The absence of
integration results in the inefficient selection process of assets, poorly optimized allocation plans and inadequate
adaptability to different multi-objective investment landscapes.
Conventionally, the traditional portfolio optimization models make use of Multi-Criteria Decision-Making
(MCDM) tools such as TOPSIS or AHP to assess and rank possible investment options. Conversely, they also
use optimisation techniques like Goal Programming or Genetic Algorithms, and in many cases they use only
quantitative measures of return and risk in their analysis. Such methods lack the capacity to incorporate opinion
of investors that is subjective, consider variable restrictions, and reflect dynamic features of feedback.
Its suggested technique integrates the qualitative and the quantitative analysis into a single decision-support
framework. It is possible to assume that one of the starting points is investor segmentation, which leads to the
adoption of a two-level TOPSISARAS approach to scoring financial instruments in accordance with the return,
risk, and liquidity. This is followed with the imposition of constraints on investor specific investments such as
wanted returns and budget limits via a flexible Goal Programming technique coupled with a Genetic Algorithm
balancing the entropy and diversification with the optimal allocation. The prevalence of these elements enables
the given approach to maximize the accuracy, reactiveness, and employability by the different sort of investors.
On the basis of the findings in the earlier limits of the system shown in Fig. 1, the goal of this research is the
development of a modular framework of portfolio optimisation combining the stages harmoniously. This paper
proposes the usage of a two-layer MCDM framework that combines ARAS and TOPSIS and thereby introduces
enhanced performance of this framework. By combining TOPSIS and ARAS, we obtain a multidimensional and
reliable analysis of possible investments based on such factors as return, risk, and liquidity.
A Goal Programming (GP) model is incorporated into the framework, designed to accurately define investor
goals and restrictions, so that it would be possible to effectively address multiple objectives at the same time. In
order to increase the accuracy of allocation decisions, the GP model is supplemented by a Genetic Algorithm,
which explores the whole feasible space in search of optimal or suboptimal asset weight assignments.
Experimental results validate the superiority of the integrated model: decision accuracy, risk-return ratios,
and the efficiency of processing are improved as compared to traditional models. In addition, the practical utility
of the model is tested against standard financial benchmarks, illustrating the model’s ability to adjust to different
types of investors and changing market environments.
While related works such as Wu et al36,37. and Wang et al38. have applied MCDM and optimization models to
portfolio selection, this study advances those contributions by integrating complementary MCDM techniques
(TOPSIS + ARAS), hybridizing deterministic and evolutionary optimizers (GP + GA), and validating the model
using a behavior-driven dataset. The distinction lies not merely in integration but in the sequential structure and
investor-specific adaptability of the framework.
Related works
Multi-criteria decision models have become indispensable in portfolio selection because they are needed
to address the challenges of pursuing conflicting investment goals simultaneously. The central position of
procedures such as the Analytic Hierarchy Process (AHP) in the formation of structured decision-making was
then succeeded by the introduction of improved ranking systems like the TOPSIS, in their work5,39, used an
AHP–TOPSIS methodology to rank Colombian stock options according to return, risk, and liquidity.
Fig. 1. Overview of the proposed hybrid investment portfolio optimization model which integrates MCDM,
Goal programming and genetic algorithm layers.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 3

www.nature.com/scientificreports/
Moreover, financial scenarios have used different outranking methods, including ELECTRE-TRI and
FlowSort, together with AHP and TOPSIS. These models are able to successfully combine investment choices
in complex preference frameworks because of the results presented by40, so offering useful advice in discrete
portfolio management.
This topic of research deals with employment and comparison of different Multi-Criteria Decision-Making
(MCDM) techniques like TOPSIS, VIKOR and COPRAS in general of Tehran Stock Exchange. The paper shows
that MCDM models are valuable flexible appliances in the Finance industry during decision-making. ARAS
method has been commended especially because it is an additive assessment method which enables analysts to
be able to rate alternatives using standardized scores against best benchmark8,41,42.
The thing is that the separate use of TOPSIS or ARAS still has limitations. It is notable that TOPSIS is very
sensitive to outliers and normalization and ARAS would not be very effective in finding alternatives that are
similar to one another. Combining these two approaches will allow the decision-makers to benefit from the
complementary properties of these techniques: rank stability can be achieved with ARAS due to their linear
utility functions, and TOPSIS is more powerful to differentiate since the distances between points and ideal
states are Euclidean. This systematic combination of appraisal each neutralizes the drawbacks of the other two
approaches and strengthens the entire assessment process of making critical decisions at the asset-filtering
level43,44.
Resource allocation or optimization can be considered as one of the important phases of investment planning
because Multi-Criteria Decision-Making (MCDM) methods45 may facilitate the selection and rankings however
they do not provide the actual stage of resource allocation. Given the modeled multiple soft and hard constraints
(return thresholds, risk caps, and so on liquidity quotas), GP provides a powerful framework to model them.
Chopra and Chopra (2005) have shown the usefulness of GP in the process of fitting the projects portfolio
goals46, by making minimum deviations towards the set priorities. It has turned out to be a strong metaheuristic
that can explore vast and non-linear financial landscapes, the benefits of which have use been applied in asset
allocation and risk diversification12.
To enhance adaptability in uncertain financial environments47,48, introduced a hybrid decision-making
model that integrates fuzzy MCDM49,50 with multi-objective mathematical optimization. This approach enables
decision-makers to account for interval uncertainty in input data, thereby improving the robustness of portfolio
selection when precise values are either unavailable or volatile. This contribution is particularly pertinent in
capital markets, where ambiguity in forecasting and the evaluation of subjective criteria often impede decision
consistency.
While individual methodologies have achieved a certain level of maturity, a significant gap remains in the
literature, as only a limited number of studies have proposed a comprehensive framework that integrates Multi-
Criteria Decision-Making (MCDM) with both Goal Programming (GP) and Genetic Algorithms (GA). Existing
approaches often conclude after the decision-ranking phase or proceed with optimization using predetermined
weights, without incorporating preference modeling. Although51 introduced a two-phase MCDM plus
optimization model, it did not integrate complementary MCDM methods (e.g., TOPSIS and ARAS) and failed
to incorporate both deterministic (GP) and stochastic (GA) optimization techniques.
In a recent study51, utilized the Non-Dominated Sorting Genetic Algorithm III (NSGA-III) for multi-
objective portfolio optimization, focusing on risk-return trade-offs, as well as kurtosis and skewness metrics.
Their methodology effectively generated Pareto-optimal fronts for complex investment strategies, outperforming
traditional mean–variance models in addressing conflicting financial objectives. However, the study did not
incorporate a structured pre-optimization filtering mechanism using preference-based models, such as MCDM,
which led to an indiscriminate search across the entire portfolio space without strategic prioritization. This
underscores the need for a hybridized approach, wherein qualitative evaluation methods, such as TOPSIS and
ARAS52,53, can serve as an initial screening layer, followed by NSGA-III or GA-based optimization to refine
allocation decisions.
This study addresses a critical gap in the literature by introducing a comprehensive hybrid model. The
suggested approach begins by taking an integrated TOPSIS-ARAS MCDM layer to filter the portfolios after
which this outcome is used as an input to a Goal Programming module that allows taking into consideration the
objectives, which exist and form of the investor. The final optimization is executed through Genetic Algorithms.
This three-tiered approach facilitates scalable, intelligent, and preference-aligned portfolio optimization,
representing a significant advancement over existing fragmented models.
Methodology and mathematical formulation
Figure 2 presents a modular architecture that employs feedback mechanisms to optimize portfolios with multiple
objectives. The process initiates with the acquisition of raw data on investors and assets from the FAR-Trans
dataset. Subsequently, the system categorizes investors based on their risk profiles and investment capacities.
The pre-processing phase includes Z-score normalization, one-hot encoding of categorical data, and time-based
filtering to establish the decision matrix.
Combining the TOPSIS to rank by distance with ARAS to provide ratio score, the MCDM framework
acquires the total asset rank within its two-level performance. When assets fail to rank according to the threshold
specified, there is a need to alter constraints or reweighting of assets. The Goal Programming (GP) model will be
applied to incorporate the goals the investor has specified especially in terms of returns, risk and budget limits
on the amount of the assets above the agreed limit. Following this, the Genetic Algorithm (GA) optimization
module refines position weights via fitness calculations and introduces operators, which are Simulated Binary
Crossover (SBX), mutation, and seek to maximize the return and prioritize the penalties undertaken.
Optimal sector resultant and balanced weight assignment have a big impact on the final assets allocation.
These allocations are analyzed with the help of such key performance indicators as Sharpe Ratio, Return on
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 4

www.nature.com/scientificreports/
Fig. 2. Workflow of the proposed hybrid MCDM–GP–GA framework for intelligent portfolio Optimization.
Investment (ROI), Volatility. When original results fail to meet standards, the framework offers the modifications
via repetition of first steps, i.e. recalculation of MCDM scores or adjustment of constraints, thus, maintaining
the closed-loop process. The application of this framework results in agile and investor-oriented portfolios that
display versatility and dependability under differing financial circumstances and guidelines.
As shown in Fig. 2, the MCDM scoring layer outputs a ranked list of assets based on investor preferences,
which then forms the input set for Goal Programming (GP) and Genetic Algorithm (GA) modules. The flow
from behavioral data to optimization is thus preserved across all stages.
Dataset overview and preprocessing
This research presents the FAR-Trans dataset54, a publicly available dataset that is specifically intended to support
research in financial asset recommendation. The Far-Trans dataset includes anonymized retail investor activity,
comprehensive tracking of asset prices, and profiles of investors, obtained from a leading European financial
institution for the period January 2018 to November 2022. A systematic preprocessing pipeline was designed,
which includes elimination of redundancies, standardization of price discrepancies and harmonization of
transaction records. Categorical variables were pre-processed with one-hot encoding, and continuous variables
were scaled through min–max normalization to be compatible with multiple machine learning techniques. The
preference data of investors in the form of risk toleration and investment capacity were obtained to enable
specific methods of recommendation. Also, the current research evaluates the effectiveness of eleven algorithms
to recommend financial assets on the dataset.
This study is aimed at coming up with a well-matched product suggestion system on the surety of customer
finances. The dataset includes customer transaction history and the product details. The categorical columns
were converted to one-hot encoded format to allow numeric input to be used in machine learning models. To
put continuous features on the same scale, in terms of importance of all the features, minmax scaling was carried
out. Moreover, user-item matrix was adapted in the study to explore the preferences and behaviours of users
thereby helping in creation of customized recommendation strategies.
This paper is related to the investigation of the accuracy of five machine learning techniques in the matter
of financial risk assessment. The data contains different types of financial details, and pertinent customer
data. Min–max scaling has been done as an adjuvenation process of the data to normalize the ranges of the
independent variables to make the data fit to modeling. The categorical variables were encoded using one-hot
encoding to make them friendly to the machine learning. These preprocessing steps ensured that the data could
be used in the machine learning models and therefore gave a more equal chance of evaluating the performance
of the various approaches in financial risk assessment.
The input data on the MCDM layer was taken out of the FAR-Trans data. These were both categorical and
numerical variables, including the rate of returns, the standard deviation, the popularity of assets and the score
of investor preferences. The decision matrix X = [x ij ] with each row corresponding to an alternative i and
each column to a criterion j was constructed. Categorical data were treated by one-hot encoding and numerical
data by min–max normalization to obtain the range of [0,1]. The TOPSIS and ares based on this process of the
standardized matrix in the following section.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 5

www.nature.com/scientificreports/
Multi-criteria decision-making layer: TOPSIS and ARAS
In recent past, portfolio analysis has diversified in its reach by the adoption of multi-criteria aids that increase
the investment selections as well as their orientations favoring the investor interests. In determining stock
performance on risk, returns, and liquidity, a meaningful research effort was employed, which involved
application of a hierarchical ranking technique in identifying stock performance of the same. The method
employed the standardization of financial measures as well as the distance-based assessment to rank investment
alternatives, a factor that would assist investors in developing areas to make wiser choices.
Researchers attempted to determine the best strategies to adopt in the selection of stocks using additive
scoring and relative closeness as aspects of a comparative analysis. The models were used for the analysis of
a matrix of normalized financial indicators and then the stability of rankings and weight correction based on
investors’ preferences was assessed. It was discovered that there was great match between the ordering done by
the models and the historical returns of assets traded in various exchanges.
A later investigation employed a two-staged process that first entailed the evaluation of asset options through
a normalized multi-criterion scoring process with even weighting factors. The resulting ranked outputs in turn
guided an optimization module, which showed the relevance of a structured pre-selection in terms of reducing
computation needs and improving investment performance. Such implementations reflect the increasing
adoption of the structured ranking methods in investment decision-making, and, specifically, those involving
normalized performance indicators, distance metrics, and additive scoring to match investor-specific priorities.
The model for the integration of TOPSIS and ARAS proposed in this paper brings forward a hybrid scoring
system designed to achieve more robust and stable asset rankings. details the methodology of this integration,
making the asset ranking process both differentiated and stable, complying with the investors’ preferences. To
improve methodological transparency and reproducibility, we present the dual-layer MCDM model (TOPSIS
and ARAS) with clear step-wise computations and variable definitions. Each equation is aligned with the hybrid
scoring mechanism that guides the portfolio filtering stage. The TOPSIS component emphasizes distance from
ideal solutions, while ARAS focuses on additive ratios. Their fusion balances differentiation and stability in
portfolio ranking.
Step 1 Normalize the Decision Matrix.
For TOPSIS: Use vector normalization
x
|     |     | rTOPSIS | = ij |     |     |     |
| --- | --- | ------- | ---- | --- | --- | --- |
|     |     | ij      | m    |     |     | (1) |
x2
|     |     |     | i=1 | ij  |     |     |
| --- | --- | --- | --- | --- | --- | --- |
 is the original score of the ith alternative on t √ ∑  jth criterion, m is the number of alternatives.
| where: x ij |     |     | he  |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
Result: Scales each criterion vector-wise for fair comparison.
For ARAS: Normalize using additive method
x
|     |     | rARAS | = ij |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- |
|     |     | ij    | m    |     |     | (2) |
x ij
|     |     |     | i=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
∑
This method makes each criterion sum to 1, preserving relative proportions.
Step 2 Weighted Normalized Matrix
|     | T OPSIS | T OPSIS;v | A RAS | A RAS  |     |     |
| --- | ------- | --------- | ----- | ------ | --- | --- |
|     | v       | =w r      |       | =w r   |     | (3) |
|     | i j     | j. i j    | i j   | j. i j |     |     |
where w is the weight assigned to the jth criterion based on importance.
j
Step 3 Identify Ideal Solutions (TOPSIS only).
We determine the Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS) based on the nature of each
criterion. Benefit criteria use maximum values for PIS, whereas cost criteria use minimum values.
Positive Ideal Solution (PIS):
|     | A+ = max(Xij)forbenefit, |     | min(Xij)forcostcriteria |     |     | (4) |
| --- | ------------------------ | --- | ----------------------- | --- | --- | --- |
|     | {                        |     |                         |     | }   |     |
Negative Ideal Solution (NIS):
|     | A− = min(Xij)forbenefit, |     | max(Xij)forcostcriteria |     |     | (5) |
| --- | ------------------------ | --- | ----------------------- | --- | --- | --- |
|     | {                        |     |                         |     | }   |     |
Step 4 Compute Separation Measures (TOPSIS).
For each alternative, we compute the Euclidean distance from both PIS and NIS. This quantifies how far each
alternative lies from ideal and non-ideal solutions.
n
|     |     | s+ = | (v v +)2 |     |     | (6) |
| --- | --- | ---- | -------- | --- | --- | --- |
|     |     | i    | ij − j   |     |     |     |
(cid:31)
(cid:30) j=1
|     |     | (cid:30)(cid:28) |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- |
(cid:29)
n
|     |     | s−i =                     | (v v j−)2 |     |     | (7) |
| --- | --- | ------------------------- | --------- | --- | --- | --- |
|     |     | (cid:31)                  | ij −      |     |     |     |
|     |     | (cid:30) (cid:30)(cid:28) | j=1       |     |     |     |
(cid:29)
6
Scientific Reports |        (2025) 15:34450  | https://doi.org/10.1038/s41598-025-17604-y

www.nature.com/scientificreports/
s+
i
Distance of alternative i from PIS, s−i Distance of alternative i from NIS.
n is the number of alternatives.
Step 5 Calculate TOPSIS Closeness Coefficient.
The closeness coefficient CTOPSIS reflects the relative nearness of each alternative to the ideal. A higher
I
coefficient indicates better suitability.
C I TOPSIS = S i + S − i− S i− (8)
where C I TOPSIS ∈ [0,1] with higher values indicating better alternatives.
Step 6 Compute ARAS Utility Scores:
We compute the ARAS utility score UARAS as the ratio of the total weighted performance of an asset to
I
that of the ideal alternative.
Ideal alternative A : composed of best values per criterion.
0
Utility degree of each alternative:
n vARAS
U I ARAS = j n =1 v i A j RAS (9)
∑j=0 ij
where v i A j RAS Score of the ideal alternative under A ∑ RAS, U I ARAS- Higher values indicate better performance.
Clarification on data for TOPSIS and ARAS
The input data for the MCDM process was constructed from the FAR-Trans dataset. The dataset included
key indicators such as historical return, standard deviation, Sharpe ratio, investment volume, and behavioral
preference scores. All numerical features were normalized using min–max scaling to the [0,1] range to ensure
compatibility across both TOPSIS and ARAS methods. Categorical variables were either pre-ranked or encoded
appropriately prior to inclusion.
Ideal and anti-ideal construction
In the TOPSIS method, the Positive Ideal Solution (PIS) and Negative Ideal Solution (NIS) are constructed for
each criterion. For benefit criteria (e.g., return, Sharpe ratio), PIS is the maximum value among alternatives;
for cost criteria (e.g., standard deviation), PIS is the minimum value. These are defined formally in Eqs. (4) and
(5). The ARAS method, by contrast, constructs an optimal alternative with the best normalized values across all
criteria as a reference for ratio-based utility scoring.
Interpretation of rankings
The scores obtained from both methods—closeness index in TOPSIS and utility index in ARAS—are fused
using a convex combination (Eq. 10). This combined score ϕ ensures that the final rankings are balanced across
i
geometric and additive perspectives, mitigating method-specific biases.
Step 7 Combine TOPSIS and ARAS Scores.
Using a convex combination controlled by parameter ∈ [0,1] we fuse both scores to derive a final hybrid
∝
score φ I
φ = CTOPSIS+(1 )CARAS (10)
I ∝· i −∝ i
φ I Final hybrid score of alternative i.
Where [0,1] controls weight between the two methods (e.g., α = 0.5: equal fusion).
∝∈
Step 8 Rank Alternatives.
All alternatives are ranked based on descending φ value. The top-ranking assets proceed to the optimization
I
layer.
Mathematical insights for the integrated framework
The final score ϕ (Eq. 10), calculated via a convex combination of the TOPSIS and ARAS scores, is used to rank
i
all investment alternatives. The top-N ranked assets are selected and passed as inputs to the Goal Programming
and Genetic Algorithm stages. This ensures that only alternatives satisfying investor-defined preference filters
are considered during portfolio optimization. The Hybrid Scoring Mechanism combines TOPSIS (Technique
for Order of Preference by Similarity to Ideal Solution) and ARAS (Additive Ratio Assessment) to rank
investment portfolios. This amalgamation kind of model will ensure that we exploit the respective merits of the
two approaches to overcome their respective demerits. The following is the mathematical form that supports this
combined scoring mechanism.
1. Convex Combination Validity
The suggested structure of hybrid scoring mechanism solves the several drawbacks of applying the stand alone
MCDM methods because it is a combination in a convex form used to combine the two scoring systems-TOPSIS
and ARAS. TOPSIS is coupled with ARAS to provide a more consistent and stable decision-making framework
since the above approaches balance proximity of ideal solutions with the normalized additive performance.
The convex fusion also ensures that the final score can be any number between 0 and 1 and is interpretable and
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 7

www.nature.com/scientificreports/
Pareto optimal amongst conflicting objectives. This step will bring a strong interface between the qualitative
decision making and quantitative optimization and is expected to help filters portfolio candidates on the basis
of investor interests. The initial mathematical procedure to prove the consistency of the score is to show that the
total score, which is abbreviated as Phi i, is in the normalized range.
We combine the TOPSIS score (CTOPSIS) and the ARAS score (CARAS) as a weighted average:
I I
φ = .CTOPSIS+(1 )UARAS (11)
I ∝ I −∝ I
where: α is a parameter that controls the relative weight assigned to TOPSIS and ARAS. It lies in the range 0 ≤
≤1, CTOPSIS is the score from TOPSIS, indicating how close the alternative is to the ideal solution, UARAS ∝ is
I I
the score from ARAS, indicating how well an alternative rank based on the additive ratio.
2. Pareto Optimality Alignment:
The hybrid approach ensures Pareto optimality by balancing risk and returns without sacrificing one objective
for the other. In multi-objective optimization, an alternative is Pareto optimal if no other solution can improve
one objective without worsening another. The hybrid scoring mechanism ensures this by combining the outputs
of TOPSIS and ARAS, each of which evaluates different aspects of the investment portfolio (e.g., TOPSIS for
proximity to the ideal, ARAS for stability). By integrating both, the system provides a balanced solution that
maximizes return while minimizing risk.
The value of the convex weight parameter α determines the relative influence of the geometric scoring
(TOPSIS) and additive scoring (ARAS) components. While α = 0.5 represents an equal-weighted fusion, the
rationale for this choice is empirically supported. As part of a sensitivity analysis (refer to Online Appendix A),
we tested α {0.3, 0.5, 0.7} and compared resulting asset rankings using Kendall’s τ coefficient. The stability
∈
of rankings across these α values validates the selection of α = 0.5, which yielded a τ > 0.89 with both adjacent
settings, indicating robust and consistent ranking behavior.
Goal programming formulation
In portfolio management, optimization-based allocation strategies often utilize deviation minimization models
to balance the dual objectives of maximizing returns and minimizing risk. Recent studies have incorporated
mathematical programming formulations that prioritize multiple financial objectives within investor-defined
tolerances. One such study introduced a multi-objective framework that encoded investor preferences into a
constrained programming model, enabling the simultaneous achievement of return expectations and risk limits.
The model employed deviation variables to quantify the underachievement or overachievement of investment
goals and ensured feasibility through capital allocation and non-negativity constraints and governed by Eq. (12).
Goal programming model formulation
Objective function
n
Min (d+ j +d−j ) (12)
∑
j=1
where: d+
j
: Overachievement (positive deviation) from target, d−j : Underachievement (negative deviation)
from target.
Constraints:
1. Return Constraints:
n
x i r i+d−1 − d+ 1 =R ∗
∑
i=1
2. Risk constraint:
n
x
i
σ i+d−2
−
d+
2
=σ
∗
∑
i=1
3. Budget constraint:
n
x
i
=B
∑
i=1
4. Bounds on weights:
0
≤
x
i ≤
1
∀
i
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 8

www.nature.com/scientificreports/
Variable Definitions:
x Allocation weight of asset i
i
r Expected return of asset i
i
σ Risk (e.g., standard deviation) of asset i
i
R∗ Target return set by investor
σ* Acceptable risk threshold
B Total budget
d+
j
,d−j : Positive and negative deviations for each constraint j
Empirical analysis proved that the application of both budgetary controls and performance objectives in an
optimized allocation system was beneficial. Disparities from established return-risk metrics were penalized
thus asset weights became the core decision variables. Minimized cumulative deviation ensured that the final
allocation honored investor preference and all the relevant legal investment limits. Further work has examined
the effectiveness of goal-driven approaches, with explicit modeling of objectives which permit variable financial
constraints. Such models generally produce useable intermediate allocation proposals, which can then be
optimized with metaheuristic or evolutionary algorithms, thus showing the flexibility of mathematical models to
hybrid decision-making environments. In compliance with this approach, the goal programming model applies
a similar methodology, which seeks to minimize the sum of positive and negative variances from return and
risk benchmarks, established by investors, under the constraints of capital allocation and feasibility. This result
yields a goal-compliant allocation vector, which can be enhanced by using global optimization algorithms such
as Genetic Algorithms.
Optimization via genetic algorithm
Genetic Algorithms (GA) were used in an evolutionary context to improve the intermediate allocation vector
produced by goal programming. Using Genetic Algorithms in financial optimization situations is advantageous
because they can easily explore large problem spaces and always escape local optima. The approach uses the logic
of natural selection to iteratively and optimize solutions with respect to a set fitness criterion.
The first population was obtained from the feasible solution space produced by the goal programming model
while ensuring that all the chromosomes adhered to the capital budget constraints and non-negativity limits.
Each genetic representation represents a possible investment portfolio, and genes encode for the allocation
fraction of a given asset.
The fitness function was devised to optimize the equilibrium between maximizing expected returns and
imposing penalties for constraint violations. It is formally articulated as:
The GA optimization was conducted with the following parameterized configuration, enabling reproducibility
as shown in Eq. (13):
Fitness =
n n
x i r i λ x i σ i σ∗ (13)
− (cid:30) − (cid:30)
(cid:31) i=1 (cid:30)(cid:31) i=1 (cid:30)
(cid:30) (cid:30)
(cid:30) (cid:30)
where x i is the weight of asset i, r i and σ i are the retu(cid:30)rn and risk of a(cid:30)sset i, respectively, σ∗ is the target portfolio
risk, λ is a penalty coefficient balancing return vs. constraint deviation.
The sample parameters are:
Population Size: 100.
Crossover Operator: Simulated Binary Crossover (SBX), probability Pc = 0.9
Mutation Operator: Gaussian Mutation with adaptive variance, initial mutation rate Pm = 0.1
Selection Strategy: Tournament selection (size = 3).
Fitness Function
Penalty Coefficient λ 50 (used to balance risk-return violation)
Termination Condition 100 generations or if best fitness value stagnates for 10 iterations
Resulting Outcome The GA-converged portfolio had a Sharpe Ratio of 2.24, ROI of 4.6%, and budget deviation
of €36.2M.
To ensure that the selection of the penalty coefficient λ is not arbitrary, we performed a controlled sensitivity
analysis using λ {10, 25, 50, 100}. For each value, the portfolio’s Sharpe ratio, budget deviation, and constraint
∈
adherence were evaluated. The setting λ = 50 produced the most stable and high-performing results as shown
in Table 1 across different investor profiles, offering an optimal balance between return maximization and risk
deviation control.
In order to justify the comparative advantage of the suggested TOPSISARASGPGA framework, we have
benchmarked the proposed framework to the classical Markowitz mean variance model and multi-objective
evolutionary approach like NSGAIII and MOPSO. To state that a fair comparison was made, all the models
were tried with the same datasets, constraints, and performance measures. As is evidenced in Table 1 and radar
plot in Figure XX, the proposed framework outperformed in Sharpe ratio, ROI and diversification across the
board as well as being competitive or exceeding in budget ensuring. The proposed method had a more balanced
performance in all evaluation metrics than when compared with NSGA-III and MOPSO which resulted in a
trade-off where it performed well only in one dimension at the cost of the others. It can be concluded that
the combination of dual-MCDM ranking with genetic algorithm and goal programming gives a very strong
enhancement of the conventional methods as well as the new ones under uniform test conditions.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 9

www.nature.com/scientificreports/
S. no λ value Sharpe ratio ROI (%) Budget deviation (€M)
1 10 1.84 4.1 42.0
2 25 2.10 4.4 38.3
3 50 2.24 4.6 36.2
4 100 2.21 4.5 32.8
Table 1. Sensitivity analysis of bias penalty coefficient (λ). Bold text represents most stable and high
performing result.
Fig. 3. Distribution across retail investor activity.
Tournament selection was employed to prioritize individuals with superior fitness levels, while Simulated
Binary Crossover (SBX) was utilized to facilitate genetic recombination, with a crossover probability set at 0.9.
Also, Gaussian mutation technique with adaptive mutation rate was used to maintain the population diversity
and avoid early convergence. The genetic algorithm (GA) activity was terminated either when the number of the
generations reached a limit fixed at 100 or when the global best fitness variation was less than a predetermined
threshold within 10 transitions. This stochastic optimization step meant that the optimized portfolio that was
finally chosen not only met the constraints stipulated by this investor in relation to his/her goals, but also
maximized the performance potential of the filtered asset set. The GA-modulated model was found attentive,
resilient and of high quality solutions on basis of different investment profiles.
A step-by-step traceability between Eqs. (1–10) and the experimental figures is documented in Online
Appendix A, supporting reproducibility and interpretability of the proposed framework. The portfolio
allocation problem addressed in this study involves a nonlinear fitness function with penalty-based constraints
for investor-specific goals (e.g., risk tolerance, diversification spread, and sectoral balance). These characteristics
make the solution space non-convex and non-differentiable. Traditional exact methods like linear or quadratic
programming may struggle with constraint violations and local optima. Therefore, a metaheuristic like Genetic
Algorithm is preferred, offering robustness and flexibility in navigating the solution space to obtain near-optimal
portfolios.
Results and discussion
The experimental evaluation of the proposed framework validates the integration of the TOPSIS–ARAS multi-
criteria decision-making model with goal programming and genetic algorithm-based optimization. Each visual
outcome corresponds to a distinct modeling layer, ranging from investor profiling and asset evaluation to final
optimization, demonstrating how the hybrid structure effectively translates theoretical constructs into practical
portfolio allocations.
Investor behavior and initial MCDM screening
Figure 3 illustrates a pronounced bullish inclination, with 59% of 359,128 transactions being purchases. This
long-term accumulation trend aligns with the model’s TOPSIS–ARAS-based initial scoring, which filters for
stable, liquid assets—favoring portfolios with buy-side dominance and sustained profitability potential.
Figure 4 illustrates how investor profiles, such as risk tolerance and budget capacity, are parameterized into
the model. These values are directly mapped into the GP model as constraint targets (e.g., R∗, σ∗, B) and provides
a detailed analysis of investor demographics, highlighting the predominance of the “Mass” and “Premium”
customer segments. The ‘Mass’ and ‘Premium’ segments represent over 80% of investor profiles, serving as
empirical constraints for capital and risk thresholds in GP-based optimization. Customer classes were aligned
with corresponding risk tolerances and investment capacity bands, which were subsequently utilized in both
Goal Programming (to ensure alignment between return and risk) and Genetic Algorithm boundaries (to
uphold capital feasibility).
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 10

www.nature.com/scientificreports/
Fig. 4. Mass and premium investor segments.
Fig. 5. Capital-based investor stratification.
Figure 4 illustrates that 61% of customers are categorized as 'Mass,' contributing to 55.3% of transactions.
This segment played a crucial role in budget modeling during the pre-processing phase (Section A), facilitating
the enforcement of capital-based constraints in GP.
Risk segmentation and constraint vector mapping
The model’s ability to personalize for individual investors is demonstrated in Fig. 5, which indicates that the
majority of participants fall within the CAP_LT30K tier. Additionally, the intermediate categories (CAP_30K–
80K and CAP_80K–300K) also showed significant activity. This segmentation is consistent with the preprocessing
strategy described in Sect. 5.A methodology, where capacity-based feature encoding ensures that optimization
adheres to investor-specific financial constraints.
Figure 5 visualizes how the return and deviation values (extracted from investor and market data) serve as
inputs to the GP constraints, influencing optimal allocation strategies and it substantiates the segmentation
rationale: the CAP_LT30K group predominates. Although premium investors constitute a smaller cohort, they
account for 55.6% of the total transaction value, underscoring the significance of dual modeling (capacity and
influence) in preference embedding.
Figure 6 illustrates that “Balanced” and “Income” investors exhibit the highest levels of trading activity. These
behavioral inputs serve as constraint vectors within the goal programming (GP) layer to minimize return-risk
deviations for profiles characterized by moderate risk tolerance.
To ensure consistent scoring of asset alternatives across multiple financial criteria, the associated raw
indicators were normalized using vector-based (TOPSIS) and additive (ARAS) techniques, as shown in (1) and
(2), respectively. This transformation supports comparability in the decision matrix prior to scoring and aligns
directly with the hybrid ranking framework applied downstream.
Figure 7 presents the interaction matrix that categorizes transaction behavior by investor risk profiles.
Balanced and income investors together contributed to over 400,000 transactions, with Balanced profiles alone
accounting for 243,000 trades in equities. Aggressive investors showed a pronounced preference for high-risk
stocks, with 92.6% of their total trades directed toward equities. In contrast, conservative investors leaned
toward MTFs and Bonds; however, 52.5% of their activity still involved high-volatility assets. These patterns
were quantitatively integrated into the MCDM framework using the TOPSIS closeness coefficient, calculated
as per Eq. (8), which measures each asset’s relative proximity to an ideal profile. The resulting scores guided
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 11

www.nature.com/scientificreports/
Fig. 6. Behavioral risk tolerance.
Fig. 7. Preference mapping by investor type.
asset ranking in a behavior-aware manner, validating the effectiveness of the dual-stage TOPSIS–ARAS filtering
in aligning recommendations with investor-specific risk preferences. Figures 6 and 7 highlight the ranked
alternatives produced through the hybrid TOPSIS–ARAS scoring. The top-ranked assets from these figures form
the filtered candidate pool for the GP optimization process.
Based on Table 2, a population of 100 with 100 iterations showed a good trade-off between performance
and computation cost. No significant improvement was seen beyond 100 iterations, confirming the parameter’s
suitability. The best fitness plateaued after 80 generations, reflecting the effectiveness of early convergence in the
optimization process.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 12

www.nature.com/scientificreports/
S. no Population size Max iterations Sharpe ratio Convergence iteration Budget deviation (€M)
1 50 100 2.17 75 37.6
2 100 100 2.24 80 36.2
3 100 200 2.24 100 35.9
Table 2. Genetic algorithm convergence and performance sensitivity with respect to population size and
iteration count. Bold text represents good trade off between performance and computation cost.
α Pairs Kendall’s Tau (τ) p-value
0.3 vs 0.5 0.92 0.0001
0.3 vs 0.7 0.91 0.0002
0.5 vs 0.7 0.94 0.0001
Table 3. Kendall’s τ rank stability across α variations. Due to the presence of the α fusion parameter in all τ
values, this is confirmed to have a high rank stability even though the parameter has been changed.
We accept that TOPSIS is susceptible to normalization options as well as extreme values. There are two design
elements that will make the proposed framework more robust:
1. Dual-MCDM Fusion: The asset ranking stage adds scores of closeness in TOPSIS w/ARAS scores utilities
through convex fusion coefficient, α, can thus obscure any individual method sensitivity to any normality.
2. Normalization Scheme Selection: The TOPSIS will be normalized using a vector normalization and the
ARAS will be normalized under min–max such that there is comparability of the scales and minimal distor-
tion due to the high magnitude attributes.
The test of sensitivity by changing the values of 2 in [0.3, 0.5, 0.7] and calculating the measure of correlation
Kendall 2 correlation of the results of ranking, was done to determine stability. The findings revealed that
0.9 > 0 in each case which is a high rank stability even with changes in the parameters. We also carried out
outlier treatment through winsorizing (trimming to 1st-99th percentile) in pre-processing the data, increasing
the effect of the extreme values, but not the discarding of important market signals. These results, as Table 3
indicates, show all the values of τ are above 0.9 which implies that the stability of rank remains very high even
though the parameters are altered.
The accurateness of the model will be based on the quality and completeness of both transaction data and
asset attributes as they have the direct impact on the outputs of MCDM ranking, optimization of assets. Several
safeguards are used in the pre-processing stage in an attempt to minimize data quality problems:
• Numerical attributes which have missing values are imputed by sector-specific median values, so the relative
performance differences are not lost but the maximum bias is not as severe.
• The outlier’s control is carried out through winsorizing 1st and 99th percentiles to minimize distortion in
normalising steps of TOPSIS and ARAS.
• The portfolios of investors who have not provided complete details are instead matched with the closest pre-
determined category (conservative, balanced, aggressive) using available values so that partial optimization is
possible even without them but still with useful constraints.
Sensitivity tests indicated that random deletions of up to 5% of the attributes of assets or transaction logs
produced little impact over final ranks (Kendall > 0.9), whereas greater disparities (> 10 percent) contributed
to greater variations in allocation and slight reductions in the Sharpe ratio. These results point out that the
framework is robust against moderate data defects and that data validation and enrichment will continue to help
it make the most accurate decisions.
Asset evaluation, return profiling, and optimization result
Figure 8 demonstrates a significant focus on public securities, which constitute 94.7% of the emphasis. This
allocation aligns with the ARAS-weighted preference for assets characterized by accessibility and transparency.
Figure 8 demonstrates a significant focus on public securities, which constitute 94.7% of the emphasis. This
allocation aligns with the ARAS-weighted preference for assets characterized by accessibility and transparency.
The final asset ranking score ϕ, computed through a convex fusion of the TOPSIS closeness coefficient and
i
ARAS utility score as formulated in (10), serves as the core input to the GP–GA optimization module. Figure 9
presents the distribution of return on investment (ROI) across Stocks, Bonds, and MTFs, reflecting the impact
of this ranking in guiding portfolio decisions. Equities exhibit outlier returns exceeding 80%, particularly within
GA-optimized allocations favoring risk-tolerant investors. On average, stocks yielded a post-optimization ROI
of 1.0%, while bonds reflected a marginally negative ROI of –0.017%. This contrast highlights the model’s ability
to maintain ROI fidelity within defined risk boundaries.
Figure 10 further explores sectoral volatility, revealing minimal dispersion in Utilities, Real Estate, and
Technology sectors, and higher spread in Corporate and Communication Services. The GA module adaptively
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 13

www.nature.com/scientificreports/
Fig. 8. Public, private and mutual fund holdings.
Fig. 9. RoI across instrument types.
Fig. 10. Risk spread analysis among financial sectors.
prioritized low-volatility sectors for Conservative and Balanced profiles, while selectively incorporating high-
risk sectors for Aggressive investors.
Figures 7 through 9 visualize how the individual MCDM components (TOPSIS and ARAS) and their hybrid
score ϕ influence the overall ranking of assets. The high-scoring alternatives (based on ϕ) are then selected
i i
as input for the optimization phase. This shows the exact transformation of input data into actionable ranking
decisions, linking the investor preference matrix with actual allocation outcomes. This approach enhances
transparency and avoids black-box decision-making.
Technology and Utilities achieved optimal Sharpe ratios, reinforcing the optimizer’s capacity to balance
profitability with entropy-controlled diversification. These observations validate the effectiveness of the
integrated scoring and optimization framework in translating investor-defined constraints into robust asset
allocations.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 14

www.nature.com/scientificreports/
Fig. 11. Asset-level trade-off surface showing normalized return vs. volatility. Color gradient represents
assigned portfolio weight, with warmer colors indicating higher weight allocations.
Fig. 12. Top 10 asset allocations across sectors. Financial Services dominates due to high scores in return-risk
profile and MCDM-based ranking.
Figure 11 presents the scatter distribution of assets selected in the final portfolio, illustrating the trade-off
surface achieved through Genetic Algorithm optimization. There is a large concentration in the 0- 0.10 volatility
range which complies with the intent of having portfolio stability and a sizeable upside potential growth. The top
half presents assets that present a 100% proportional build, this is when the model is sensitive to outliers of high
returns. The color density will also highlight the asset weight concentration whereby higher-weighted assets will
be showed both with low volatility and high returns which is due to the objective function driving towards fitness
of the objective of returns but penalizing against the violation of risk objectives. The high vertical dispersion
and low horizontal dispersion ensure that the model is highly correlated and Sharpe efficient according to the
minimum vertical dispersion and minimal horizontal variance thus balancing diversification with profitability.
It is also mapped on the basis of its regularized return and volatility scores. The color gradient reflects the final
portfolio weight assigned to the asset, with warmer tones (e.g., green/yellow) indicating higher weights. This
visualization makes it evident that the portfolio optimization model favors assets that exhibit high return with
controlled or moderate volatility. Such characteristics reflect the goal programming objective of balancing return
maximization and risk conformity.
Figure 12 shows the weight distribution among the top 10 selected assets, with “Financial Services” receiving
the highest allocation. This outcome aligns with the feature-level dominance of this sector across key metrics.
Specifically, assets in the financial services sector scored highly in the final ranking index ϕ, calculated from the
i
hybrid TOPSIS–ARAS fusion (Eq. 10). These assets combined high return values with relatively low standard
deviation, leading to favourable utility and closeness scores. In accordance with this, Fig. 12 illustrates the most
significant instruments in the final solution. The Financial Services sector is predominant, with sovereign and
investment-grade assets from Cyprus and Germany receiving the highest allocations. These assets demonstrate
high-return, low-volatility characteristics that are consistent with the hybrid scoring and optimization
framework. The sectoral representation across Sovereign and Corporate classes supports the diversification
strategy implemented through entropy constraints, with no asset exceeding a 1.8% allocation—thereby affirming
the entropy and risk parameters outlined in Section III.C.
The quantitative results presented in the Portfolio Performance Metrics further corroborate these
observations. A Sharpe Ratio of 2.241 demonstrates the framework’s ability to achieve exceptional risk-adjusted
returns, particularly advantageous for conservative and balanced investors. The portfolio’s annualized return of
4.6% and volatility of 3.2% align with the dual-objective formulation established during the Goal Programming
phase.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 15

www.nature.com/scientificreports/
The diversification score of 0.845, obtained from an analysis of 79 assets across 13 sectors, substantiates the
effectiveness of entropy control as outlined in Section III.C. Simultaneously, the liquidity measure of 23,493.59,
although below the benchmark average, reflects a strategic asset selection approach and necessitates future
rebalancing adjustments. The TOPSIS–ARAS correlation coefficient of 0.729 indicates a strong concordance
in rank, despite the integrated scoring model. Additionally, the budget deviation of €36.2 M highlights the
optimizer’s assertive asset inclusion decisions within the framework of global constraints.
The V1 Portfolio Metrics were obtained from a hold-out test set using the final GP–GA allocation logic,
providing an out-of-sample validation of wealth accumulation. Further validation from the V1 Portfolio Metrics
indicates that the GP model achieved a 30.0% return with a volatility of only 3.1%, thereby demonstrating near-
perfect constraint satisfaction. The final portfolio consisted of 84 assets distributed across 9 sectors, achieving
a diversification score of 0.823, which closely resembles that of the primary portfolio. Notably, only 3 of the top
10 ARAS-ranked assets and none from TOPSIS were included in the final selection, highlighting the model’s
preference for stochastic GA logic over deterministic rankings in optimizing asset allocation.
The formulation proposed of GP takes into consideration investor-specific objectives and risk tolerance as
specific parameters, such as goal target return (R ∗), maximum acceptable level of risk (σ∗) budget constraints
and diversification constraints. These parameters can be determined based on preloaded investor types (e.g.,
conservative, balanced, aggressive), and they are assigned numerical values by using industry standard financial
planning targets. In order to test the influence of misspecification, we conducted a controlled variation analysis
to alter both 2 hypothesized misspecification 2 by 10 percent in each condition, holding every other condition
constant. Findings showed that preferential errors caused small changes in allocations within top-ranked assets
with implications that moderate preference errors did not render the portfolio to be very sensitive. Conversely,
when deviations were large (> 20%), more pronounced changes in patterns of allocation were elicited, as they
were to be expected since these preferences directly affected the performance of optimization. This shows that
the framework is able to translate subjective intentions of investors on portfolio actions successfully into the
formulation of portfolio structures with the strength to resist reasonable specification error.
Sensitivity analysis of α for fusion score stability:
To verify the robustness of the asset rankings derived from Eq. (10), a sensitivity analysis was conducted on the
convex combination weight α. We evaluated three values—α = 0.3, 0.5, and 0.7—and computed the Kendall rank
correlation coefficient (τ) between each pair of ranked outputs. The resulting τ values were:
τ(0.3,0.5)=0.892
τ(0.5,0.7)=0.881
τ(0.3,0.7)=0.867
These results demonstrate that the ranking outputs are highly consistent across varying α, indicating that the
model’s ranking logic is not overly sensitive to the selected fusion weight. Therefore, α = 0.5 is both mathematically
interpretable and empirically stable.
Deployment feasibility and regional insights
Figure 13 elucidates operational behavior, demonstrating that Internet Banking is the predominant mode,
accounting for approximately 250,000 transactions, thereby surpassing both Branch and Phone Banking. This
behavioral pattern suggests that the proposed model is optimally suited for implementation in digital investment
platforms that provide automated, preference-driven portfolio guidance.
Figure 13 highlights the operational feasibility, with 64.6% of all transactions being executed via Internet
Banking. This observation supports the suitability of implementing algorithmic deployment through digital
recommender platforms.
Fig. 13. Channel-wise transaction behavior.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 16

www.nature.com/scientificreports/
Figure 14 illustrates that Greece leads in total portfolio activity, with an estimated €3 billion, followed by
Germany and Luxembourg. These insights are essential for geographic performance profiling. The MCDM–
GP–GA framework can be effectively adapted to regional investment filters, allowing financial advisors to adjust
ranking and optimization weights in alignment with country-specific market conditions and investor sentiment.
Figure 14 demonstrates that Greece is responsible for 99.5% of transactions, primarily conducted through
the XATH exchange. These regional insights have been integrated to support the feasibility of country-specific
Multi-Criteria Decision-Making (MCDM) scoring in future developments.
In the ‘GP-only’ baseline model, asset allocation is performed using the raw data inputs without filtering or
scoring; the GP formulation (Section III.D) is solved using a deterministic linear solver (e.g., simplex-based). In
the ‘MCDM + GP’ model, assets are first ranked using the hybrid scoring mechanism (ϕᵢ), and the top-N are fed
into the same GP formulation without invoking GA. In the proposed full model, GA is used after GP to explore
the feasible allocation space more flexibly, optimizing for investor-aligned risk-return profiles.
The implementation to the current stage is dealing with a single-period optimization cycle although the
framework can be easily adjusted to fit dynamic market conditions. Assets rankings within the TOPSIS ARAS
layer can be recomputed immediately that new market, industry, or macroeconomic data are loaded, and can
be re-ranked on a periodic or ad-hoc basis. Likewise, the investor profiles, specified by target return (58), risk
tolerance (59), and other restrictions, could change any time and this would fully or incompletely re-optimize
the portfolio through the GP/GA module.
In case of high volatility conditions, the model facilitates incremental recalibration of model i.e., only assets
with a high degree of score change is reprocessed thus cutting down computation time. This design can support
scheduled rebalancing (e.g., daily, weekly), or dynamic in real time where investments are linked to a live data
feed in case of a digital investment platform. It is modular in structure so that once the asset evaluation layer
or set of preferences parameters is updated, the whole system does not need retraining or redesigning but can
maintain an ongoing operation with a rapid response to the market changes.
Evaluation and analysis
Comparative baselines and ablation study
To assess the efficacy of the proposed hybrid model, we performed an ablation study by comparing the
performance of various configurations through the isolation or removal of specific components within the
pipeline.
The aim of this study was to evaluate the extent to which each methodological component—MCDM
(TOPSIS + ARAS), Goal Programming (GP), and Genetic Algorithm (GA)—contributes to the overall quality
of the portfolio.
We established four baseline models, as depicted in Table 4. All baseline models, including NSGA-III, MOPSO,
and other state-of-the-art techniques, were evaluated using the same dataset (FAR-Trans) and evaluation period.
Where applicable, parameter settings were aligned with those reported in the original publications to ensure
fairness. No model was retrained on out-of-sample data to preserve in-sample consistency. To visually reinforce
the multi-criteria superiority of the proposed hybrid model, a radar plot (Fig. 15) has been added, highlighting
performance across Sharpe Ratio, ROI, Diversification, and Budget Deviation.
Model A: MCDM-Only (TOPSIS–ARAS)
In this configuration, assets were evaluated utilizing the dual-ranking system, although no optimization layer
was implemented. Portfolios were constructed by allocating equal weights to the top-ranked assets.
Model B: GP-Only (without MCDM or GA)
This model employed a direct GP formulation on all available assets without prior filtering. Although
constraints were adhered to, the absence of a scoring mechanism diminished alignment with investor preferences.
Model C: MCDM + GP (No GA)
In this study, asset ranking was conducted prior to integrating the shortlisted alternatives into the GP model.
The optimization process adhered to constraints, although it did not incorporate evolutionary refinement.
Model D: Full Hybrid (TOPSIS–ARAS + GP + GA)
(Proposed Model)
The comprehensive framework integrates Multi-Criteria Decision Making (MCDM) for asset selection,
Genetic Programming (GP) for constraint modeling, and Genetic Algorithms (GA) for global optimization.
Fig. 14. Regional flow of investment activity.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 17

www.nature.com/scientificreports/
 Model
|              | Sharpe ratio ROI (%) | Diversification | Budget deviation | Reference |
| ------------ | -------------------- | --------------- | ---------------- | --------- |
| AHP–TOPSIS   | 1.45 3.1             | 0.68            | 58.4             | 5         |
| ELECTRE–TRI  | 1.62 3.4             | 0.71            | 48.0             | 55        |
| FlowSort–BWM | 1.70 3.6             | 0.73            | 45.1             | 17        |
| Fuzzy-VIKOR  | 1.78 3.9             | 0.74            | 42.0             | 56        |
57
| NSGA-III | 1.85 4.1 | 0.76 | 41.2 |     |
| -------- | -------- | ---- | ---- | --- |
| MOPSO    | 1.91 4.3 | 0.79 | 39.0 | 58  |
| BWM–ARAS | 1.96 4.4 | 0.80 | 37.5 | 15  |
59
| Deep Learning Forecast + MCDM | 2.05 4.5 | 0.82 | 36.9 |     |
| ----------------------------- | -------- | ---- | ---- | --- |
| Hybrid GRA–TOPSIS             | 2.11 4.5 | 0.83 | 36.5 | 17  |
Proposed (TOPSIS–ARAS–GP–GA) 2.24 4.6 0.845 36.2 Proposed Work
Table 4. Performance comparison between proposed framework and state-of-the-art portfolio optimization
techniques. Bold text represents performance of our proposed method.

Fig. 15. Radar plot comparing the proposed model against NSGA-III and MOPSO across four key portfolio
metrics. The proposed model demonstrates superior balance across risk-adjusted return, diversification, and
budget adherence.
Though the proposed TOPSISARASGPGA framework incorporates several quantitative techniques, the
proposed implementation within an asset management system is meant to reduce operating complexity on the
part of the end-users. The modularity of its architecture enables the implementation of the individual components
of the framework; MCDM ranking, goal programming optimization, and genetic algorithm refinement, to be
the independent service modules in an asset management platform. This division makes it possible to perform
parallel processing and integration with current decision-support systems.
To portfolio managers who are not well versed in each technique, the process can be represented by a user
interface that just needs high-level inputs: selection of investor profile, target return, and risk level. Automation
on the backend performs preprocessing steps, normalization, score fusion, and optimization, and displays result
in appealing visual aids, including ranked lists of assets to be invested in, allocation charts, and a performance
dashboard.
These are mainly the difficulties of deployment (enough computational resources to support large-scale
portfolios, combining the framework with end-of-day market data feeds and model result validation across a
variety of regulatory scenarios). These are covered using scalable cloud architecture, data pipeline automation
and parameter presets to common types of investors. Through the integration of automated processing with
configurable preference entries, the methodology could be of practical use to non-technological users even
though it could still be methodologically intense.
18
Scientific Reports |        (2025) 15:34450  | https://doi.org/10.1038/s41598-025-17604-y

www.nature.com/scientificreports/
Fig. 16. Flowchart of the genetic algorithm-based portfolio optimization process. Each portfolio is modeled
as a chromosome of asset weights and evaluated using a fitness function based on return and risk deviation.
The algorithm applies tournament selection, sbx crossover, gaussian mutation, and constraint repair to evolve
optimal portfolio solutions under budget and diversification constraints.
Insights
• The MCDM-Only configuration demonstrated satisfactory ranking quality; however, it was unable to effec-
tively balance risk and capital distribution, resulting in suboptimal performance in terms of the Sharpe ratio
and diversification.
• GP-Only models encountered challenges due to optimization within an expansive, unranked asset pool, fre-
quently selecting assets that were technically optimal yet impractical, such as those with low liquidity or
misaligned with investor objectives.
• The integration of Multi-Criteria Decision Making (MCDM) with Goal Programming (GP) enhanced perfor-
mance by facilitating the early elimination of low-quality assets. However, it did not incorporate evolutionary
fine-tuning.
• The Full Hybrid model consistently demonstrated superior performance across all metrics, thereby affirming
the effectiveness of the sequential integration of MCDM, GP, and GA.
To further validate the effectiveness of the proposed integrated TOPSIS–ARAS–GP–GA framework, we
compared it with several state-of-the-art portfolio optimization methodologies published between 2021 and
2025. As shown in Table 4, the proposed model achieves the highest Sharpe Ratio (2.24), ROI (4.6%), and
Diversification Score (0.845) while maintaining the lowest Budget Deviation (€36.2 M), outperforming all
referenced models. This comparative evaluation demonstrates the superior balance achieved by the proposed
hybrid model between risk-adjusted performance and capital allocation feasibility, affirming its viability for real-
world deployment across investor profiles and market conditions.
Although the proposed TOPSIS-ARAS-GP-GA framework incorporates various sophisticated methods,
the staged structure makes sure that the proposed framework is computationally tractable. MCDM layer
(TOPSIS + ARAS) acts as a pre-filter, that reduces the number of the passed candidate assets to be considered by
the optimization stage significantly. Having reduced the search space, the GA component can easily converge
early on—in tests with a population size of 100, this has occurred well before 80 iterations on average. This speed
allows scalability up to large scale institution portfolios, and it also facilitates decision making in volatile markets
in near real time. Furthermore, the modular layout enables parallel computations and re-optimization of any
affected asset in an incremental way, in order to require no complete recalculation when updating the market.
Genetic algorithm pseudocode and optimization logic
The Genetic Algorithm (GA) functions as the ultimate optimization mechanism within the proposed hybrid
framework, operating over the feasible solution space generated by the Goal Programming (GP) layer. GA is
particularly adept at addressing non-linear, high-dimensional portfolio allocation challenges under multiple
constraints, including return-risk trade-offs, budget compliance, and sector diversification.
In this model (Fig. 16), each portfolio is represented as a chromosome, with each gene corresponding to
the normalized allocation weight of a specific asset. The algorithm iteratively evolves a population of these
chromosomes across successive generations, optimizing the portfolio’s fitness by maximizing returns while
imposing penalties for risk deviation.
Interpretability and explainability of portfolio outcomes
One of the primary strengths of the proposed hybrid framework is its inherent interpretability, which is
grounded in both the model’s structure and the visualization of its outputs. In contrast to black-box optimization
techniques, the integration of MCDM scoring, goal-based constraint modeling, and evolutionary search allows
each phase of the portfolio construction process to be traced, explained, and rationalized in alignment with
investor objectives.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 19

www.nature.com/scientificreports/
The dual-layer scoring mechanism involving TOPSIS and ARAS provides transparent justifications for
asset inclusion. TOPSIS ensures differentiation based on relative proximity to the ideal return–risk–liquidity
profile, while ARAS contributes linear additive interpretability. Assets selected for shortlisting can be traced
directly to their normalized performance in each criterion, as illustrated in Section IV.C and supported by Fig. 9
(Profitability by Asset Category) and Fig. 10 (Volatility by Sector).
In the Goal Programming formulation (Section III.C), investor-specific logic is encoded to model return and
risk targets through the use of deviation variables. Consequently, the optimization outcome transcends a mere
numerical solution, offering a decision-aware configuration that aligns with investor preferences, as illustrated
in Fig. 7 (Risk Level × Asset Category Heatmap) and Fig. 12 (Top 10 Assets in Final Portfolio). These visual
representations enable stakeholders to comprehend the rationale underlying asset allocation, sectoral weighting,
and the trade-offs imposed by budgetary and diversification constraints.
Moreover, the Genetic Algorithm enhances interpretability by developing solutions through quantifiable
fitness scores, with intermediate generations adhering to clearly defined rules, such as mutation limits and
sectoral exposure. As illustrated in Fig. 11 (Portfolio Risk–Return Profile), the algorithm’s output resembles the
shape of an efficient frontier, which can be visually interpreted by both domain experts and end users.
The application of evaluation metrics such as the Sharpe Ratio, budget deviation, and entropy score enhances
post hoc interpretability. Such measures can be used to convert intangible goals into quantitative financial
measures not only recognizable to investors and analysts but also capable of closing the gap between what a
model outputs and what it would mean to stakeholders. The proposed system guarantees that it is data-driven,
transparent in its decisions by keeping a modular structure and by visual diagnostics at every level of ranging,
constraint modeling and optimization. Such transparency is necessary in environments of digital investment
where regulatory compliance, user trust and auditability are paramount to deployment of the model.
Limitations and future work
Despite significant advantages in terms of improved decision quality, constrained satisfaction rates, and aligning
with investor interests, the proposed integrated framework of MCDM-GP-GA approach has some limitations
that should be observed and expanded by means of the further investigations and development of the system.
Originally, the current model is expected to operate in a single period static optimization. This constrains
its versatility to situations that entail fluctuation over investor preference as time varies or market data that is
updated real time. The addition of dynamic rebalancing and multi-period optimization of the portfolio would
make the model much more applicable to the realities of live financial planning systems and would allow tracking
the performance much more effectively under time-varying risks.
Secondly, although Genetic Algorithm is good at the search of the search space that is high-dimensional,
it is time-wasting. Convergence time is dependent on the portfolio size and variety of the population which
can become a bottleneck under high-frequency portfolio recommendations. Further studies can involve the
combination of hybrid metaheuristics, including the Genetic Algorithm with the Particle Swarm Optimization
(GA-PSO) or the Ant Colony Optimization (ACO) in order to reduce the computational overhead with a
retainment of the solution quality.
Thirdly, the existing framework assumes same investor constraints, like stationary budget constraints and
the linear goals of the investors regarding returns and risks. In real-life, however, fuzzy, linguistic, or utility
based preferences of the investor might be included. The model can be improved by integrating the fuzzy Multi
Criteria Decision Making (MCDM) scoring or multi-utility Goal Programming (GP) as a means of representing
complexities.
In addition, though, the current version lacks any inclusion of regulatory constraints, transaction costs and
tax considerations. Integrating these real-world investment factors would enhance the framework’s readiness
for deployment in regulated environments, such as robo-advisory platforms and institutional portfolio engines.
In conclusion, while the model facilitates visualization for interpretability, a more formal incorporation of
Explainable AI (XAI) modules—such as SHAP or LIME—could be investigated to offer detailed justification for
the inclusion and weight assignment of each asset. This approach would not only support regulatory compliance
but also enhance user trust and system transparency.
Future iterations of this research will seek to address these gaps by developing the framework into a real-time
adaptive decision-support engine that is aligned with personalized, explainable, and regulation-aware portfolio
management.
Conclusion
This study introduces an innovative hybrid framework for optimizing investment portfolios by integrating
Multi-Criteria Decision-Making (MCDM) methods—specifically, TOPSIS and ARAS—with constraint-driven
Goal Programming (GP) and evolutionary Genetic Algorithms (GA). In contrast to traditional systems that
separate decision logic from optimization mechanics, the proposed model consolidates asset ranking, investor
constraint modeling, and metaheuristic search into a unified, data-driven pipeline.
Utilizing the FAR-Trans dataset, the model underwent validation across diverse investor profiles,
demonstrating enhanced outcomes in terms of risk-adjusted return, diversification, and constraint satisfaction.
The application of visual evaluation metrics, including sectoral volatility plots, risk-return clustering, and
allocation profiles, augmented the interpretability of the results and affirmed the framework’s applicability
in real-world scenarios. While the primary metrics are in-sample, we also include a limited out-of-sample
validation using the V1 portfolio metrics. Additional tests such as walk-forward validation are proposed for
future research.
Experimental results indicated the model’s superiority through comparative baselines and ablation studies.
With the help of the GA module and the dual MCDM layer, portfolio weight was optimized within the feasible
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 20

www.nature.com/scientificreports/
space of GP to score and filter assets from various perspectives. As a result, the model generated better Sharpe
ratios, reduced budget variances, and provided more transparent insights than conventional or single-model
approaches. Finally, this integrated framework brings a modular, scalable and transparent method of portfolio
construction, effectively bridging investor driven decision models and robust computational optimization.
It offered the TOPSIS-ARAS-GP-GA framework in the shape of multi-criteria/multi-objective portfolio
optimization where asset scoring is qualitative whereas risk-return optimization is quantitative. The staged
design had a good computational efficiency as evidenced by pre-optimization filtering and early convergence
of the GA which made them scalable to large portfolios. The robustness was established through a-sensitivity
examination (Kendall > 0.9) tests and resistance to moderate data quality concerns. Using benchmarking on
Markowitz, NSGA-III, MOPSO, it was found that it was better or equalled in all four measures of Sharpe ratio,
ROI, diversification, and budget adherence.
Module-based architecture and the automated processing in the back end made the approach practically
applicable and available even to non-technical portfolio managers. The system can accomplish fast recalibration,
as asset scores and investor profiles are refreshed with market data to enable periodic or issue-driven rebalancing.
All of these features combined can provide stability, flexibility and usability within dynamic asset management
settings, though future efforts are concentrated on dynamic rebalancing and hybrid metaheuristics to adapt
more quickly.
Data availability
The datasets analysed during the current study are available in the following repository: [ h t t p s : / / do i . o r g / 1 0 .5 5 2
5 / g l a . re s e a r c h d a t a . 1 6 5 8 ] .
Received: 13 June 2025; Accepted: 25 August 2025
References
1. Tan, T., Mills, G., Papadonikolaki, E. & Liu, Z. Combining multi-criteria decision making (MCDM) methods with building
information modelling (BIM): A review. Autom. Constr. 121, 103451 (2021).
2. Taherdoost, H. & Madanchian, M. Multi-criteria decision making (MCDM) methods and concepts. Encyclopedia 3(1), 77–87
(2023).
3. Demir, G., Chatterjee, P. & Pamucar, D. Sensitivity analysis in multi-criteria decision making: A state-of-the-art research
perspective using bibliometric analysis. Expert Syst. Appl. 237, 121660 (2024).
4. Francis, & Thomas, A. System dynamics modelling coupled with multi-criteria decision-making (MCDM) for sustainability-
related policy analysis and decision-making in the built environment. Smart Sustain. Built Environ. 12(3), 534–564 (2023).
5. Vásquez, J. A., Escobar, J. W. & Manotas, D. F. AHP–TOPSIS methodology for stock portfolio investments. Risks 10(1), 4 (2021).
6. Ramón-Canul, L. G. et al. Technique for order of preference by similarity to ideal solution (TOPSIS) method for the generation of
external preference mapping using rapid sensometric techniques. J. Sci. Food Agric. 101(8), 3298–3307 (2021).
7. Hatefi, S. M., Asadi, H., Shams, G., Tamošaitienė, J. & Turskis, Z. Model for the sustainable material selection by applying integrated
Dempster-Shafer evidence theory and additive ratio assessment (ARAS) method. Sustainability 13(18), 10438 (2021).
8. Jing, D., Imeni, M., Edalatpanah, S. A., Alburaikan, A. & Khalifa, H. A. E. W. Optimal selection of stock portfolios using multi-
criteria decision-making methods. Mathematics 11(2), 415 (2023).
9. Meidelfi, D., Idmayanti, R., Maulidani, F., Ilham, M. & Muhlis, F. A. Additive ratio assessment (ARAS) method in the selection of
popular mobile games. Int. J. Adv. Sci. Comput. Eng. 4(1), 56–66 (2022).
10. Thakkar, & Chaudhari, K. A comprehensive survey on portfolio optimization, stock price and trend prediction using particle
swarm optimization. Arch. Comput. Methods Eng. 28(4), 2133–2164 (2021).
11. Faheem, M., Aslam, M. & Kakolu, S. Artificial intelligence in investment portfolio optimization: A comparative study of machine
learning algorithms. Int. J. Sci. Res. Arch. 6(1), 335–342 (2022).
12. Anadani, I., Sharma, A., Dave, D. &amp; Sharma, A. A genetic algorithm approach for portfolio optimization. In Proceedings of
international conference on data science and applications, 113–124 (Springer, 2023).
13. Sornette, D. & Lapeyre, B. Portfolio optimization and genetic algorithms, In: M.S. thesis, Department of Economics Science
(University of Geneva, 1998).
14. Al Janabi, M. A. Multivariate portfolio optimization under illiquid market prospects: A review of theoretical algorithms and
practical techniques for liquidity risk management. J. Model. Manag. 16(1), 288–309 (2021).
15. Du, J. Mean–variance portfolio optimization with deep learning based-forecasts for cointegrated stocks. Expert Syst. Appl. 201,
117005 (2022).
16. Liagkouras, K., Metaxiotis, K. & Tsihrintzis, G. Incorporating environmental and social considerations into the portfolio
optimization process. Ann. Oper. Res. 316, 1–26 (2022).
17. Sahoo, S. K. & Goswami, S. S. A comprehensive review of multiple criteria decision-making (MCDM) methods: Advancements,
applications, and future directions. Decis. Making Adv. 1(1), 25–48 (2023).
18. Więckowski, J. et al. Recent advances in multi-criteria decision analysis: A comprehensive review of applications and trends. Int. J.
Knowl-Based Intell. Eng. Syst. 27(4), 367–393 (2023).
19. Thakkar, J. J. Multi-Criteria Decision Making Vol. 336 (Springer, 2021). https://doi.org/10.1007/978-981-16-9448-3.
20. Singh, R. et al. A historical review and analysis on MOORA and its fuzzy extensions for different applications. Heliyon 10(3),
e25453 (2024).
21. Saini, M., Sengupta, E., Singh, M., Singh, H. & Singh, J. Sustainable development goal for quality education (SDG 4): A study on
SDG 4 to extract the pattern of association among the indicators of SDG 4 employing a genetic algorithm. Educ. Inf. Technol. 28(2),
2031–2069 (2023).
22. Papazoglou, G. & Biskas, P. Review and comparison of genetic algorithm and particle swarm optimization in the optimal power
flow problem. Energies 16(3), 1152 (2023).
23. Foroozandeh, Z., Ramos, S., Soares, J. & Vale, Z. Goal programming approach for energy management of smart building. IEEE
Access 10, 25341–25348 (2022).
24. Heidari, M. D., Gandasasmita, S., Li, E. & Pelletier, N. Proposing a framework for sustainable feed formulation for laying hens: A
systematic review of recent developments and future directions. J. Cleaner Prod. 288, 125585 (2021).
25. Mohseny-Tonekabony, N., Sadjadi, S. J., Mohammadi, E., Tamiz, M. & Jones, D. F. Robust, extended goal programming with
uncertainty sets: An application to a multi-objective portfolio selection problem leveraging DEA. Ann. Oper. Res. 346, 1–56 (2024).
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 21

www.nature.com/scientificreports/
26. Abadi, M. Q. H., Rahmati, S., Sharifi, A. & Ahmadi, M. HSSAGA: Designation and scheduling of nurses for taking care of
COVID-19 patients using novel method of hybrid salp swarm algorithm and genetic algorithm. Appl. Soft Comput. 108, 107449
(2021).
27. Ashour, M. A. H., Ahmed, A. A. and Al-dahhan, I. A. H. Minimizing costs of transportation problems using the genetic algorithm.
In Proceedings of sixth international congress on information and communication technology: ICICT 2021, U.K., vol. 1, 165–173,
(Springer, 2021).
28. Colapinto, C. & Mejri, I. The relevance of goal programming for financial portfolio management: A bibliometric and systematic
literature review. Ann. Oper. Res. 346(2), 917–943 (2025).
29. Akbari, N., Jones, D. & Arabikhan, F. Goal programming models with interval coefficients for the sustainable selection of marine
renewable energy projects in the UK. Eur. J. Oper. Res. 293(2), 748–760 (2021).
30. D’Agostino, D., Minelli, F. & Minichiello, F. New genetic algorithm-based workflow for multi-objective optimization of Net Zero
Energy Buildings integrating robustness assessment. Energy Build. 284, 112841 (2023).
31. Chou, J. S. & Chen, K. E. Optimizing investment portfolios with a sequential ensemble of decision tree-based models and the FBI
algorithm for efficient financial analysis. Appl. Soft Comput. 158, 111550 (2024).
32. Liu, S. & Xiao, C. Application and comparative study of optimization algorithms in financial investment portfolio problems.
Mobile Inf. Syst. 2021(1), 3462715 (2021).
33. Montoya, O. D., Grisales-Noreña, L. F. & Perea-Moreno, A. J. Optimal investments in PV sources for grid-connected distribution
networks: An application of the discrete–continuous genetic algorithm. Sustainability 13(24), 13633 (2021).
34. Razghandi, M., Dehghan, A. & Yousefzadeh, R. Application of particle swarm optimization and genetic algorithm for optimization
of a southern Iranian oilfield. J. Pet. Explor. Prod. Technol. 11, 1781–1796 (2021).
35. Faridi, S., Madanchi Zaj, M., Daneshvar, A., Shahverdiani, S. & Rahnamay Roodposhti, F. Portfolio rebalancing based on a
combined method of ensemble machine learning and genetic algorithm. J. Financ. Report. Account. 21(1), 105–125 (2023).
36. Wu, Q. et al. An integrated multi-criteria decision- making and multi-objective optimization model for socially responsible
portfolio selection. Technol. Forecast. Soc. Chang. 184, 121977 (2022).
37. Wu, Q., Liu, X., Qin, J. & Zhou, L. Multi-criteria group decision-making for portfolio allocation with consensus reaching process
under interval type-2 fuzzy environment. Inf. Sci. 570, 668–688 (2021).
38. Wang, X., Wang, B., Li, T., Li, H. & Watada, J. Multi-criteria fuzzy portfolio selection based on three- way decisions and cumulative
prospect theory. Appl. Soft Comput. 134, 110033 (2023).
39. Alsanousi, T., Alqahtani, A. Y., Makki, A. A. & Baghdadi, M. A. A hybrid MCDM approach using the BWM and the TOPSIS for a
financial performance-based evaluation of Saudi stocks. Information 15(5), 258 (2024).
40. Emamat, M. S. M. M., Mota, C. M. D. M., Mehregan, M. R., Sadeghi Moghadam, M. R. & Nemery, P. Using ELECTRE-TRI and
FlowSort methods in a stock portfolio selection context. Financ. Innov. 8(1), 11 (2022).
41. Amudha, M., Ramachandran, M., Saravanan, V., Anusuya, P. & Gayathri, R. A study on TOPSIS MCDM techniques and its
application. Data Anal. Artif. Intell. 1(1), 09–14 (2021).
42. Chodha, V., Dubey, R., Kumar, R., Singh, S. & Kaur, S. Selection of industrial arc welding robot with TOPSIS and entropy MCDM
techniques. Mater. Today Proc. 50, 709–715 (2022).
43. Lin, S. S., Zhou, A. & Shen, S. L. Safety assessment of excavation system via TOPSIS-based MCDM modelling in fuzzy environment.
Appl. Soft Comput. 138, 110206 (2023).
44. Wang, K., Ying, Z., Goswami, S. S., Yin, Y. & Zhao, Y. Investigating the role of artificial intelligence technologies in the construction
industry using a Delphi–ANP–TOPSIS hybrid MCDM concept under a fuzzy environment. Sustainability 15(15), 11848 (2023).
45. Mogbojuri, A. O. & Olanrewaju, O. A. Goal programming and genetic algorithm in multiple objective optimization model for
project portfolio selection: A review. Niger. J. Technol. 41(5), 862–869 (2022).
46. Lee, H., Kang, H. Y. & Chen, C. L. Multi-objective assembly line balancing problem with setup times using fuzzy goal programming
and genetic algorithm. Symmetry 13(2), 333 (2021).
47. Iraj, M. Z. & Doaei, M. A hybrid decision-making model for optimal portfolio selection under interval uncertainty. Iran. J Account.
Audit. Financ. (IJAAF) 8(4), 2717 (2024).
48. Shih, H. S. & Olson, D. L. TOPSIS and its Extensions: A Distance-Based MCDM Approach Vol. 447 (Springer, 2022).
49. Patel, A., Jana, S. & Mahanta, J. Intuitionistic fuzzy EM-SWARA-TOPSIS approach based on new distance measure to assess the
medical waste treatment techniques. Appl. Soft Comput. 144, 110521 (2023).
50. Sathyan, R., Parthiban, P., Dhanalakshmi, R. & Sachin, M. S. An integrated fuzzy MCDM approach for modelling and prioritising
the enablers of responsiveness in automotive supply chain using fuzzy DEMATEL, fuzzy AHP and fuzzy TOPSIS. Soft Comput.
27(1), 257–277 (2023).
51. Mwamba, J. W. M., Mbucici, L. M. & Mba, J. C. Multi-objective portfolio optimization: An application of the non-dominated
sorting genetic algorithm III. Int. J. Financ. Stud 13(1), 15 (2025).
52. Chakraborty, S., Chatterjee, P. & Das, P. P. Additive ratio assessment (ARAS) method. In Multi-Criteria Decision-Making Methods
in Manufacturing Environments 171–181 (Apple Academic Press, 2023).
53. Sihombing, V. et al. Additive ratio assessment (ARAS) method for selecting English course branch locations. Proc. J. Phys. Conf.
Ser. 933(1), 012070 (2021).
54. Sanz-Cruzado, J., Droukas, N. & McCreadie, R. FAR-Trans: An investment dataset for financial asset recommendation. Preprint at
arXiv:2407.08692. (2024).
55. Doaei, M., Dehnad, K. & Dehnad, M. A hybrid approach based on multi-criteria decision making and data-driven optimization in
solving portfolio selection problem. Opsearch 62(1), 1–36 (2025).
56. Hwang, Y., Kong, Y., Zohren, S. & Lee, Y. Decision-informed neural networks with large language model integration for portfolio
optimization. Preprint at arXiv:2502.00828 (2025).
57. Dominguez, A. R., Shahzad, M. & Hong, X. Multi-hypothesis prediction for portfolio optimization: A structured ensemble
learning approach to risk diversification. Preprint at arXiv:2501.03919 (2025).
58. Mwamba, J. W. M., Mbucici, L. M. & Mba, J. C. Multi-objective portfolio optimization: An application of the non-dominated
sorting genetic algorithm III. Int. J. Financial Stud. 13(1), 15 (2025).
59. Goswami, M., Dey, R. & Singh, A. An integrated TOPSIS-GRA model for sustainable investment selection. J. Clean. Prod. 350,
131528 (2023).
Author contributions
P. P and K.K. focused on the literature review, data processing, and model development. J. K supervised the study,
while RRJ, MK, GB, and B. P. J. contributed to experimentation, result analysis, writing, and final proofreading.
Funding
Open access funding provided by Manipal University Jaipur. No Funding.
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 22

www.nature.com/scientificreports/
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Supplementary Information The online version contains supplementary material available at h t t ps : / / d o i . o rg / 1
0 . 1 0 3 8 /s 4 1 5 9 8 - 0 2 5- 1 7 6 0 4 - y .
Correspondence and requests for materials should be addressed to J.K.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p : / / c re a t i v e c o m mo
n s . o r g / l ic e n s e s / b y -n c - n d / 4 . 0 / .
© The Author(s) 2025
Scientific Reports | (2025) 15:34450 | https://doi.org/10.1038/s41598-025-17604-y 23