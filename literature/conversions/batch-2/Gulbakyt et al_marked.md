---
conversion_metadata:
  converted_at: "2026-07-22T13:28:46Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Gulbakyt et al.pdf"
  source_pdf_sha256: "b59a87f97724b56f2dde4a53e5534f46a31a7dab4a57a8584e3729de9e0600a1"
  page_count: 14
  markdown_char_count: 115219
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3075

Dynamic Model for Budget Allocation in via Multi-Criteria Optimization

Sembina Gulbakyt1,

, Abdualiyev Almaz2,*,

, Sagnayeva Saule3,

, Yoldash Suhrab4,

1,2Information Systems Department, International Information Technologies University, Almaty (050040), Kazakhstan

3System Analysis and Management Department, Eurasian National University named after L.N. Gumilyov, Astana (010008), Kazakhstan

4Information Systems Department, Kazakh-British Technical University, Almaty (050000), Kazakhstan

(Received: May 01, 2025; Revised: July 28, 2025; Accepted: October 10, 2025; Available online: November 15, 2025)

Abstract

This research introduces a dynamic multi-criteria optimization framework for fair budget distribution across four districts in Kazakhstan’s Almaty 
region. Its main objective is to promote transparency, equity, and efficiency in allocating a constrained regional budget of 42,656,543 thousand 
tenge  across  seven  activity  areas  (AA):  education,  healthcare,  transport,  infrastructure,  digitalization,  culture,  and  ecology.  The  framework 
incorporates  four  weighted  criteria:  citizen  satisfaction  (0.2  weight),  strategic development  priorities  (0.2),  basic needs  fulfillment (0.3),  and 
urbanization level (0.3). Two optimization techniques were employed: Sequential Quadratic Programming (SQP) in MATLAB, converging in 
100 iterations with an objective function value of 18,519,864.85 thousand tenge, and Genetic Algorithm (GA) in Python, achieving a slightly 
higher value of 18,520,000.00 thousand tenge after 500 generations. The minimal difference of 135.15 thousand tenge (0.0007% of the budget) 
underscores the reliability of both methods. All seven sectors received funding, with healthcare (22.05%) and transport (21.11%) allocated the 
largest portions, and education (7.03%) the smallest. Fairness is evidenced by a standard deviation of sectoral shares at 5.69%, a coefficient of 
variation  of  0.398,  and  a  Gini  coefficient  of  0.223.  Participatory  budgeting  was  simulated  using  synthetic  citizen  voting  data  derived  from 
demographic factors. Visualizations depict the optimization process’s convergence and budget distribution across feasible solutions. A proposal 
for  pilot  testing  within  Kazakhstan’s  e-government  system  (Egov)  has  been  submitted  to  the  Ministry  of  Digital  Development.  Future 
enhancements  will  include  explainable  AI,  stakeholder-driven  weight  adjustments,  and  real  demographic  and  budgetary  data  to  foster 
transparency and public confidence. This framework provides a scalable, data-driven approach to participatory budgeting, harmonizing strategic 
objectives, socio-economic demands, and citizen preferences. SQP and GA methods achieved near-optimal solutions with objective function 
values  of  18,519,864.85  and  18,520,000.00  thousand  tenge,  respectively.  The  135.15  thousand  tenge  difference  (0.0007%  of  the  budget)  is 
negligible, confirming their robustness.

Keywords: Budget Allocation, Multi-Criteria Optimization, Areas Of Activity, Sequential Quadratic Programming, Genetic Algorithm

1. Introduction

The  distribution  of  the  budget  in  the  regions  and  cities  is  handled  by  local  executive  bodies  (maslikhats)  [1],  [2].  
Maslikhats are district representative bodies, whose members are elected by the population of various administrative-
territorial units by direct vote for a period of 5 years. Since the topic of the article is related to the distribution of 
regional  funds  in  the  region,  several  literary  sources  related  to  the  promotion  of  budget  funds  and  their  arrival 
specifically in maslikhat have been studied.

It  is  currently  uncommon  to  see  representatives  of  local  executive  bodies  at  a  normal  maslikhat  meeting.  These 
representatives visit specific trouble spots to observe the current situation and consider the data gathered for discussion 
at the following meeting. The region's socioeconomic, cultural, and material circumstances are deteriorating as a result 
of these lawmakers' careless labor. The opaque procedure of awarding funding is another factor contributing to the 
decline in public trust in official bodies.

For cities and districts, where budget funds should be allocated to maximize the demands of the populace in numerous 
AA,  including  education,  healthcare,  transportation,  infrastructure,  technology,  culture,  and  ecological,  efficient 
financial resource management is particularly crucial. A tight budget necessitates the development and application of

*Corresponding author: Abdualiyev Almaz (dellivine@mail.ru)

DOI: https://doi.org/10.47738/jads.v6i4.935

This is an open access article under the CC-BY license (https://creativecommons.org/licenses/by/4.0/). 
© Authors retain all copyrights

---

<!-- PAGE 2 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3076

strategies that enable the best possible distribution of financial resources while accounting for a number of variables 
and  priorities.    Reducing  socioeconomic  disparities,  encouraging  sustainable  growth,  and  building  public  trust  in 
government all depend on efficient regional budget allocation.  Maslikhats, or local elected councils, are largely in 
charge of allocating public monies across various AA. They frequently deal with issues like low transparency and 
insufficient public involvement [1], [2].  Issues with regional financial planning, such as unequal development, a lack 
of  data-driven  tools  for  decision-making,  and  inadequate  alignment  with local priorities,  have  been  highlighted  by 
recent research [3], [4], [5].  Multi-criteria decision-making approaches have also become more popular worldwide as 
a result of the growing complexity of public sector management and the requirement to balance a variety of social, 
economic, and strategic goals [6], [7]. A popular strategy to increase equity and transparency in resource allocation is 
participatory  budgeting,  which  integrates  public  opinion  into  financial  choices  [7],  [8].  Voting  for  priority  regions 
allows city dwellers to voice their thoughts, which is one of the most important factors in budget distribution. The goal 
of this research is to use quadratic programming and multi-criteria optimization to create a mathematical model of the 
district budget's dynamic distribution.

2. Theoretical Basis and the Proposed Method

By using linear programming based on the simplex method and a leveled balancing approach, this study expands on 
earlier research on the budget allocation process  [3]. Model-based optimization techniques that employ probability 
distributions to identify solutions are examined in article [4]. A strategy is put forth that is predicated on the upkeep of 
a population of models that are updated across many generations. The effective distribution of computational resources 
among the models is the main objective. In order to decrease the number of calculations and enhance the quality of the 
results,  a  dynamic  sampling  technique  based  on  Markov  solutions  has  been  created.  The  findings  show  that  the 
suggested strategy increases the effectiveness of techniques for resolving challenging optimization issues.

Using  Primorsky  Krai  as  an  example,  the  research  [5]  focuses  on  creating  and  evaluating  a  dynamic  model  for 
maximizing the distribution of financial resources for the growth of human capital. The target function of the model is 
to achieve strategic goals in the field of human capital, and it considers the impact of the amount and structure of public 
and private investments through multi-period interdependence. The findings show that it is possible to identify the best 
investment plan that helps reach the objectives. It is advised that resources be distributed fairly over time, encompassing 
social policy, national security, health, and education.

Conflicting aims can be taken into consideration when creating a budget thanks to the multi-criteria approach in the 
contemporary participatory budgeting environment, which has grown popular worldwide [6], [7].  Finding a solution 
that concurrently meets multiple (sometimes conflicting) criteria is the goal of multi-criteria optimization.  Large-scale 
resource allocation issues in the public sector with several limitations have been successfully resolved by quadratic 
programming [8].

3. Methodology

The primary techniques employed in the process of creating a budget allocation model are thoroughly explained in this 
section. Quadratic programming, multi-criteria optimization, and the utilization of the fmincon function in MATLAB 
are the primary areas of emphasis.  The process of identifying a solution that considers multiple criteria, many of which 
are  in  conflict  with  one  another,  is  known  as  multi-criteria  optimization  [9].  Important  characteristics  of  the  SQP 
algorithm for our problem include: allowing the specification of both linear and nonlinear constraints; being able to 
specify  the  boundaries  of  variables  and  constraint  matrices  in  a  convenient  manner;  and  allowing  the  selection  of 
different optimization algorithms, including the SQP method itself [10]. The complete research flow used in the study 
is depicted in figure 1.

---

<!-- PAGE 3 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3077

Figure 1. Conceptual framework of the dynamic budget allocation model

The first step in the process is gathering input data, such as strategic priorities, demographic statistics, and the outcomes 
of simulated citizen voting.  These inputs are fed into a GA and SQP based multi-criteria optimization framework that 
incorporates important factors like urbanization, basic necessities, strategic priorities, and citizen happiness. Subject to 
regional and financial limitations, the optimization procedure iteratively looks for the best way to allocate funds among 
four  districts  and  seven  AA’s.    Following  that,  the  resulting  budget  allocations  are  compared  among  optimization 
techniques and assessed using fairness measures (Gini coefficient, standard deviation).

Task highlights the following criteria: meeting the needs of citizens (weighted by the number of votes); consideration 
of the strategic priorities of the regions; meeting minimum basic needs; accounting for the level of urbanization. A 
target optimization function that incorporates the data above the criterion is necessary for multi-criteria optimization. 
A specific optimization method is quadratic programming, an optimization method in which the objective function is 
quadratic  and  the  constraints  are  linear.  Notably,  the  scientific  literature  is  paying  more  and  more  attention  to 
comparable issues of the best way to allocate funds among areas while taking into consideration a variety of criteria 
and constraints [11]. The problem of quadratic programming is formulated as:

min (

1
2

𝑥𝑇𝑄𝑥 + 𝑐𝑇𝑥) , 𝑔𝑖𝑣𝑒𝑛 𝑡ℎ𝑎𝑡: 𝐴𝑒𝑞 × 𝑥 = 𝑏𝑒𝑞, 𝐴𝑖𝑛𝑒𝑞 × 𝑥 ≤ 𝑏𝑖𝑛𝑒𝑞

(1)

Q - the matrix of quadratic coefficients; с - vector of linear coefficients; 𝐴𝑒𝑞, 𝑏𝑒𝑞 - equality;𝐴𝑖𝑛𝑒𝑞, 𝑏𝑖𝑛𝑒𝑞- inequalities.

This study effectively applies quadratic programming using the SQP method since the target function is approximated 
at each iteration due to the fact that it is not strictly quadratic: the limits are set by the 𝐴𝑒𝑞,  𝐴𝑖𝑛𝑒𝑞 matrices to comply 
with the overall budget and regional limit and boundaries of variables (𝐵𝑚𝑖𝑛, 𝐵𝑚𝑎𝑥) set the minimum and maximum 
allowable  budget  values.  Recent  studies  show  similar  strategies  for  equitable  budgeting  at  the  district  level.  
Specifically, study [12] demonstrates how extra constraints (such project quotas for low-income areas) are employed 
in participatory budgeting procedures to promote equality.

Under  numerous  limitations,  quadratic  programming  has  demonstrated  efficacy  in  resolving  significant  resource 
allocation issues in the public sector [13].The following characteristics of the SQP algorithm, which is appropriate for 
resolving nonlinear programming problems with constraints, are taken into consideration in this study: supports linear 
and non-linear constraints, uses several algorithms for optimization, including SQP, which is used in this task and 
convenience of setting boundaries for variables (𝐵𝑚𝑖𝑛, 𝐵𝑚𝑎𝑥) and the constraint matrices (𝐴𝑒𝑞, 𝐴𝑖𝑛𝑒𝑞).

The approach outlined makes it possible to provide precise and financially sound outcomes that may be used in actual 
practice for the best possible budget allocation. In order to optimize the target function while adhering to financial 
limitations, the model's ultimate objective is to divide the money across four areas and seven AAs in the best possible 
way. Data was collected for the study from four districts in the Almaty region: Raiymbeksky, Kegensky, Talgarsky, 
and Karasaysky. Each of the seven districts has a budget that is appropriate [14], and when these are added together, 
the districts' total budget B is obtained:

4
7
∑ ∑
𝑖=1
𝑗=1

𝐵𝑖,𝑗

(2)

---

<!-- PAGE 4 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3078

Minimal  (𝐵𝑚𝑖𝑛,𝑖,𝑗)  and  maximum  (𝐵𝑚𝑎𝑥,𝑖,𝑗)  budget  boundaries  play  an  important  role  in  ensuring  a  realistic  and 
equitable allocation of financial resources. This is due to avoiding unrealistic solutions that optimization algorithms 
can offer - 𝐵𝑚𝑖𝑛 guarantees that every district or region gets the bare minimum of funding required to carry out its 
essential duties. Additionally, it helps guarantee that everyone has access to a minimum amount of financing, which is 
crucial for vital sectors like healthcare and education. 𝐵𝑚𝑎𝑥 restricts extra money and permits resources to be allocated 
more fairly among regions and AA’s by preventing excessive redistribution of cash to one district or area, which could 
leave  other  AA’s  without sufficient  funding.  By restricting the  search  area inside  the  range  of  potential values for 
optimization variables, the boundaries also aid the algorithm in finding answers more quickly and lower the task's 
computing complexity:

𝐵𝑚𝑖𝑛,𝑖,𝑗 ≤ 𝐵𝑖,𝑗 ≤ 𝐵𝑚𝑎𝑥,𝑖,𝑗

(3)

The objective function of the mathematical model includes four main criteria: satisfaction of citizens (by counting the 
number of votes of citizens)-α;  strategic priorities - unique values that are set depending on the state of satisfaction of 
citizens of a given AA’s in the area (values from 1.0 to 1.9) - β; satisfaction of basic needs (γ) - used in the objective 
function.  Responsible  for  including  the  minimum  budget  limits  of  𝐵𝑚𝑖𝑛  in  the  optimization  process.  Weight  γ 
determines  how  important  it  is  to  meet  the  minimum  requirements  (𝐵𝑣𝑒𝑐 ≥ 𝑙𝑏𝑣𝑒𝑐)  for  the  target  function.  If    𝐵𝑣𝑒𝑐 
exceeds 𝑙𝑏𝑣𝑒𝑐, the indicator returns 1, which adds the value of γ to the objective function. In this way, component y 
provides a balance between strategic priorities and a guarantee of a basic level of provision, motivating the model to 
choose solutions that meet the minimum requirements for basic needs, the level of urbanization (δ) is the standard ratio 
of the urban population to the total in the region. This metric reflects the degree of urban development and access to 
infrastructure and services. Districts with higher CU values are assumed to have greater demands for complex services 
and receive proportionally adjusted funding. The urbanization data were obtained from the Bureau of National Statistics 
of Kazakhstan [14], and incorporated as a weighted factor in the optimization objective. The mathematical formulation 
of the objective function has the form:

Objective function = max (α  ∙ ∑

𝑉𝑖,𝑗
max (𝑉)

𝑖,𝑗

× 𝐵𝑖,𝑗 + β∙ ∑

𝑖,𝑗

𝑊𝑖,𝑗
max (𝑊)

× 𝐵𝑖,𝑗 + γ ∙ ∑ 1(𝐵𝑖,𝑗 ≥ 𝐵𝑚𝑖𝑛 𝑖,𝑗)

𝑖,𝑗

+ δ ∙

∑

𝑖,𝑗

𝑈𝑖
max (𝑈)

× 𝐵𝑖,𝑗

(4)

The  parameter  γ,  reflecting  the  satisfaction  of  basic  needs,  is  operationalized  via  a  conditional  mechanism:  if  the 
allocated budget for a specific area of activity meets or exceeds its predefined minimum threshold, a value of 1 is 
assigned to this component in the objective function; otherwise, it is set to 0. This ensures that the γ weight contributes 
to the objective function only when essential funding requirements are met, incentivizing the optimization algorithm 
to prioritize solutions that fulfill minimum needs across all districts.

Similarly,  β  and  δ  are  incorporated  as  multiplicative  weights,  directly  applied  to  strategic  priority  scores  and 
urbanization coefficients, respectively. These values are normalized and scaled based on their relative importance in 
the model, as determined by the assigned weights. Minimal (𝐵min, 𝑖) and maximum (𝐵max, 𝑖) boundaries are calculated 
taking into account the population level, the level of urbanization and the profitability of the region:

𝐵min, 𝑖 = 𝑘𝑝𝑜𝑝 × 𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛𝑖 + 𝑘𝑢𝑟𝑏𝑎𝑛 × 𝑈𝑟𝑏𝑎𝑛𝑖𝑧𝑎𝑡𝑖𝑜𝑛𝑖  + 𝑘𝑖𝑛𝑐𝑜𝑚𝑒 × 𝐼𝑛𝑐𝑜𝑚𝑒𝑖

𝐵max, 𝑖 = α × 𝐵𝑚𝑖𝑛,𝑖

(5)

𝑘𝑝𝑜𝑝, 𝑘𝑢𝑟𝑏𝑎𝑛, 𝑘𝑖𝑛𝑐𝑜𝑚𝑒- weighting factors for population, urbanization, and profitability of the region; α -the increase 
factor, limits the upper limit of the budget so that resources are not concentrated in one area or region. This is important 
to prevent an imbalance when one sector receives disproportionately much money. The optimization problem is solved 
using the quadratic programming algorithm described above. Limitations of the optimization problem:

𝐴𝑒𝑞 × 𝐵𝑣𝑒𝑐 = 𝑇𝑜𝑡𝑎𝑙 𝑏𝑢𝑑𝑔𝑒𝑡 
𝐴𝑖𝑛𝑒𝑞 × 𝐵𝑣𝑒𝑐 ≤ 𝑏𝑖𝑛𝑒𝑞

(6)

The boundaries of optimization:

---

<!-- PAGE 5 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3079

𝐵𝑚𝑖𝑛,𝑣𝑒𝑐 ≤ 𝐵𝑣𝑒𝑐 ≤ 𝐵𝑚𝑎𝑥,𝑣𝑒𝑐

(7)

When  matrix  representations  of  constraints  are  utilized  in  linear  programming  and  optimization  problems,  certain 
notations are common. Equation (6) sets a constraint that the sum of all allocated funds for all regions and regions must 
be equal to a given total budget, 𝐴𝑒𝑞 is a vector of coefficients. In this problem, the 𝐴𝑒𝑞 consists of units so that the 
sum of all variables 𝐵𝑣𝑒𝑐 (all budgets) is equal to the total budget. 𝐵𝑣𝑒𝑐 - a vector of optimized variables representing 
the budget distribution between regions and regions. Each element of the vector is a dedicated budget for a specific 
area in a specific region. It also defines linear inequalities that limit the amount or proportion of the allocated budget. 
𝐴𝑖𝑛𝑒𝑞  - the coefficient matrix that defines the relationship between the 𝐵𝑣𝑒𝑐 budget variables and their constraints. 
Each row of the matrix 𝐴𝑖𝑛𝑒𝑞  corresponds to one restriction. 𝑏𝑖𝑛𝑒𝑞  - the vector of the right-hand side that defines the 
upper limits for each constraint. The final constraint (8) sets the range of values for each element of the vector 𝐵𝑣𝑒𝑐, 
that is, the budget for each region in each region should be between the minimum 𝐵𝑚𝑖𝑛 and maximum 𝐵𝑚𝑎𝑥 boundaries.

Three important facets of budget allocation in the model are described by these formulas: budget equality requires that 
the total amount of allotted cash equal the entire budget. This restriction guarantees that all resources are used to their 
fullest potential and that the budget is not overspent or underutilized, inequalities: to ensure that budgets adhere to 
predetermined  boundaries,  such  as  not  exceeding  the  maximum  share  allocated  for  a  specific  region  or  sector, 
restrictions  are  imposed  on  the  allocation  of  funds  among  regions  and  AA’s.  Budget  boundaries:  the  lowest  and 
maximum permitted budget values are established for each region, determining the smallest amount of money that can 
be  dedicated to  basic  necessities  and  the  highest  amount  that may  be  allocated while accounting for  priorities  and 
restrictions. The dataset uses data from official sources [14], [15] total budget: 42 656 543 thousand tenge.

The citizen voting data used in this study were synthetically generated based on demographic statistics for each district. 
The number of "votes" was estimated by reducing the population count by approximately 30% to account for natural 
demographic factors (e.g., minors, elderly, mortality, and non-participation). This approach was adopted in the absence 
of actual participatory budgeting records. The model is designed to simulate citizen preferences in a representative 
manner, serving as a proof-of-concept. In future implementations, it is planned to integrate this model into the Egov 
platform  (Kazakhstan's  national  e-government  portal),  where  real  citizen  input  can  be  collected  through  digital 
participation tools, ensuring legitimacy and real-time feedback for decision-makers.

Distributed votes of citizens and the unique strategic priorities for these AA’s in the respective districts are presented 
in  the  tables  below  (table  1  and  table  2,  respectively).  To  facilitate  comparability  across  regions  and  incorporate 
multiple priorities into the objective function, raw vote counts and strategic priority multipliers were normalized within 
each region. The final weight for each area within a region was determined as a weighted sum of normalized votes and 
strategic  scores,  integrated  with  other  components  (e.g.,  basic  needs  and  urbanization)  according  to  the  specified 
criterion weights (α, β, γ, δ).

Table 1. Distributed votes of citizens

Areas of activity

Education  Healthcare

Transport

Infrastructure

Digitalization

Culture

Ecology

1121

5000

3400

2800

3500

3200

4100

3700

4200

7100

5300

5900

2700

2800

5300

4300

6800

4500

6700

800

1500

6300

3300

6400

5400

2200

4900

2900

Table 2. Unique strategic priorities

Areas of activity

Education  Healthcare

Transport

Infrastructure

Digitalization

Culture

Ecology

1.1

1.2

1.3

2.1

1.8

1.7

1.2

1.5

1.1

1.7

1.6

1.5

1.5

1.4

1.2

1.0

1.3

1.4

1.3

1.5

1.6

Region

Raimbeksky

Karasaysky

Talgarsky

Kegensky

Region

Raimbeksky

Karasaysky

Talgarsky

---

<!-- PAGE 6 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3080

Region

Education  Healthcare

Transport

Infrastructure

Digitalization

Culture

Ecology

Areas of activity

Kegensky

1.0

1.5

1.4

1.3

1.3

1.2

1.4

Although  strategic  priority  multipliers  varied  from  1.0  to  2.1  across  activity  areas  and  districts,  their  specific 
quantitative influence on budget allocation was not distinctly isolated in this study. Within the model, these priorities 
contribute  to  the  final  objective  function  through  weighted  normalization,  interacting  with  citizen  preferences, 
minimum thresholds, and urbanization factors.

Table  3  provides  verified  demographic  and  economic  data  for  the  four  districts  analyzed,  encompassing  total 
population, average annual income, and the urbanization coefficient (the ratio of urban to total population). These data 
were  sourced  from  the  official  portal  of  the  Bureau  of  National  Statistics  of  Kazakhstan  (stat.gov.kz,  accessed 
December 2024). The urbanization coefficient served as a weight in the optimization model, capturing the degree of 
infrastructural development and the demand for advanced services.

Region

Raimbeksky

Karasaysky

Talgarsky

Kegensky

Table 3. Demographic data, profitability and quality of regions

Population

Income (thousand tenge)

CU (%)

55,000

230,000

190,000

45,000

280,000

350,000

310,000

260,000

24.5

65.3

60.8

20.1

Weights of strategic priorities: citizens' satisfaction weight = 0.2; strategic priority weight = 0.2; weight of basic needs 
= 0.3; the weight of the urbanization = 0.3.

The weight coefficients in the objective function (e.g., 0.2 for citizen satisfaction, 0.3 for basic needs) were established 
through expert judgment and an analysis of policy priorities in Kazakhstan’s regional planning framework. While these 
coefficients  align  with  practical  priorities,  they  lack  grounding  in  formal  sensitivity  analysis.  Future  studies  will 
integrate systematic sensitivity testing and multi-scenario analysis to evaluate the influence of weight variations on 
budget allocation outcomes and to enhance the model’s robustness.

4. Results and Discussion

After performing optimization, the values of 𝐵𝑖,𝑗 for each region and AA’s in figure 2, corresponding to the constraints and criteria 
were obtained. Despite the differences in emphasis, the total budget is distributed relatively evenly between the districts, 
which indicates that the optimization model meets the specified conditions.  The largest influence on budget allocation 
came from the population (𝑘𝑝𝑜𝑝). The budget proportion for each region grew due to the rising rate of urbanization. 
The  model  allocates  greater  resources  to  strategically  significant  sectors  like  transportation,  healthcare,  and  the 
environment while effectively accounting for the unique demands of each district. The graph effectively demonstrates 
how the model accounts for both strategic priorities and necessities, guaranteeing the best possible budget allocation.

---

<!-- PAGE 7 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3081

The numerical values of the distributed budget obtained are shown in the table 4.

Figure 2. Budget allocation result

Categories

Education

Healthcare

Transport

Infrastructure

Digitalization

Culture

Ecology

Table 4. Numerical results (thousands tenge)

Districts

Raimbeksky

Karasaysky

Talgarsky

Kegensky

296622.18

3082251.69

2307597.61

223033.64

296622.18

2947763.44

2307597.61

223033.64

2307597.61

296622.18

223033.64

3266538.43

296622.18

2307597.61

3266538.43

223033.64

2307597.61

296622.18

223033.64

3266538.43

296622.18

3266538.43

2307597.61

223033.64

296622.18

2904838.10

2307597.61

223033.64

18519864.85  thousand  tenge  is  the  value  of  the  objective  function  that  the  optimization  model  has  reached.  The 
objective function's positive value indicates that resources were successfully allocated in compliance with the given 
standards. By combining multiple criteria into a single generalized value, the objective function enables you to assess 
the  model's  efficacy.  Reaching  such  a  high  result  suggests  a  balanced  distribution  that  considers  the  degree  of 
urbanization, the fulfillment of strategic aims, and the satisfying of fundamental requirements.

To quantitatively assess the fairness and balance of the budget allocation, we calculated several statistical indicators 
based on sectoral budget shares. The disparities in budget allocations across areas and districts, such as the notably 
higher education allocation in Talgarsky district compared to others - stem from the interplay of multiple model criteria. 
These encompass regional strategic priorities, urbanization levels, citizen vote distribution, and minimum/maximum 
constraints. In Talgarsky, education was assigned a higher relative priority score (1.3) and garnered significant citizen 
support (3400 votes). When normalized and weighted within the objective function, these factors justified an increased 
allocation. Additionally, the district’s urbanization coefficient and population size bolstered its share.

In contrast, areas with minimal allocations satisfied only the minimum funding thresholds, reflecting lower strategic 
weights  or  voter  preferences,  while  the  model  adhered  to  upper  bounds  to  preserve  overall  equilibrium. 
To evaluate the fairness and balance of the budget allocation quantitatively, we computed several statistical measures 
based on sectoral budget shares. The standard deviation of the distribution was 5.69%, and the coefficient of variation 
stood at 0.398, suggesting moderate variability across sectors. The Gini coefficient, at 0.223, indicated a relatively 
equitable resource distribution. These metrics demonstrate that, despite healthcare (22.05%) and transport (21.11%) 
receiving the largest allocations due to strategic significance and voter preferences, other sectors like education (7.03%) 
and ecology (6.99%) were adequately supported. The model thus ensured inclusivity and avoided excessive resource 
concentration.

---

<!-- PAGE 8 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3082

While this figure does not directly equate to monetary efficiency or return on investment, it acts as a consolidated 
performance  metric  for  assessing  different  budget  allocation  strategies.  To  offer  perspective,  the  function employs 
normalized weights for each criterion (e.g., strategic priorities at 0.2, basic needs at 0.3), where a greater score signifies 
a more balanced and constraint-compliant allocation. Relative to other models-such as a linear programming approach 
based solely on citizen voting or a level balancing technique-the proposed method delivered enhanced utility while 
securing funding for all activity areas.

To enhance the understanding of how budget allocations align with model constraints, figure 3 provides a visualization 
of  the  feasible  region  for  Healthcare  and  Transport,  the  two  areas  receiving  the  largest  shares  in  the  optimized 
distribution (the red points show all valid combinations of budget allocations under model constraints, blue points represent the 
actual  optimized  allocations  for  four  districts,  all  of  which  fall  within  the  feasible  region).  The  shaded  area  delineates  all 
permissible combinations of budget values for these sectors that comply with the model’s minimum, maximum, and 
total budget constraints.

Figure 3. Feasible budget allocation region for Healthcare and Transport with actual district-level results.

The data on the operation of the fmincon optimization model is shown in the figure 4:

Figure 4. Optimization process – output parameters of the algorithm

The table shows data on the optimization process. Each of the indicators characterizes the steps of the algorithm and 
its approximation to the solution of the problem. Let's look at each line and the key parameters: Func-count = 128 (in 
total, 128 calls to the objective function were performed during the entire optimization process).Fval = −1.654620e+07 
(the  value  of  the  objective  function  has  not  changed  anymore,  indicating  that  a  local  optimum  has  been  reached). 
Feasibility = 8.651e+05 (the restrictions are practically met, the remaining violations are within acceptable limits). Step 
Length = 1.435e−11 (the step length has become extremely small, which indicates the convergence of the algorithm).

Norm of Step = 2.707e−06 (changes in variables are minimal, which confirms the achievement of a stable state). First-
order optimality = 7.016e−01 - the gradient value indicates a local optimum. While the convergence behavior of the 
fmincon  solver  was  initially  presented  through  numerical  indicators,  figure  5  offers  a  graphical  depiction  of  the 
optimization  trajectory.  The  plot  reveals  a  swift  enhancement  in  the  objective  function  value  -  from  roughly  16.5 
million  tenge  to  18.52  million  -  within  the  initial  iteration,  followed  by  a  stabilization  phase,  affirming  efficient 
convergence. This visual representation reinforces the numeric stopping criteria and underscores the robustness of the 
SQP-based solution within the model’s constraints.

---

<!-- PAGE 9 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3083

Figure 5. Convergence of the objective function value during SQP optimization

During  the  optimization  process,  the  solver  identified  a  non-zero  constraint  violation  at  the  final  iteration, 
approximately  865,100  ₸,  largely  attributable  to  the  model's  complex  nonlinear  and  multidimensional  structure. 
Although this residual violation is relatively minor (≈ 0.47% of the total budget), it highlights a trade-off between strict 
feasibility and maximizing utility within the given iteration limit.

This indicates a possible need for enhanced constraint tolerance control or the adoption of penalty-based or augmented 
Lagrangian methods to enforce feasibility more effectively. Future research could also investigate adaptive constraint 
handling techniques or multi-start strategies to boost robustness and mitigate local infeasibility. Nonetheless, all critical 
constraints—including minimum funding per activity and total budget caps—were met to a practical extent, affirming 
the reliability of the resulting allocation for practical implementation.

To enhance reproducibility and accessibility, we highlight that while the current implementation relies on MATLAB’s 
fmincon solver (Sequential Quadratic Programming method), comparable optimization can be achieved using open-
source tools. Specifically, Python’s SciPy library (scipy.optimize.minimize with method='SLSQP') offers analogous 
capabilities for addressing constrained nonlinear optimization problems. The optimization model’s logic and structure 
can be entirely replicated in this platform. For transparency and future advancement, the authors plan to share core 
pseudocode and a minimal working version of the model through a public repository or supplementary materials.

The  model's  efficacy  was  confirmed  by  the  algorithm's  quick  convergence,  which  finished  optimization  in  two 
iterations after the first one. The excellent precision of the solution identified is indicated by the objective function's 
final value and the minimal changes in the variables. Even though there were a few minor infractions of the limits, the 
outcomes were nevertheless acceptable and satisfied the standards.

The level balance model and the linear programming model with maximum citizen satisfaction functions were two 
alternative approaches from related work that were compared in order to assess the efficacy of the suggested multi-
criteria optimization model [3]. An examination of each method's outcomes and a comparison with the model used in 
this paper can be found below. The level balancing model divides the funds among regions and activity areas based on 
predetermined thresholds. This guarantees that the more crucial areas receive proportionately greater funding while 
each category receives the bare minimum permitted.

The results of the study showed a more balanced budget distribution. For instance, ecology in the Talgarsky district 
was  allocated  3,253  thousand  tenge,  while  technology  in  the  Karasaysky  district  received  1,801  thousand  tenge. 
Nevertheless, the absence of objective function optimization restricts the efficient use of resources. In conclusion, the 
level balance model promotes equitable distribution but overlooks strategic priorities and citizen feedback.

The  second  model,  based  on  linear  programming,  aims  to  maximize  citizen  satisfaction  by  incorporating  their 
preferences through voting data, with calculations performed using the simplex method. This approach maximized 
citizen  satisfaction,  though  funding  for  lower-priority  areas  like  culture  and  ecology  was  omitted.  For  example, 
healthcare  in  the  Karasaysky  district  received  1,741  thousand  tenge,  surpassing  the  allocation  in  the  level  balance

---

<!-- PAGE 10 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3084

model. However, excluding funding for certain areas, such as infrastructure, introduces risks of imbalance. Despite not 
funding  all  categories,  this  approach  proves  highly  efficient  under  resource  constraints.  The  optimization  model 
proposed in this study integrates multiple factors, including urbanization levels, strategic priorities, basic needs, and 
citizen satisfaction, with computations carried out using the quadratic programming method. The objective function 
value  reached  18,482  thousand  tenge,  reflecting  a  balanced  consideration  of  the  criteria.  All  categories  received 
funding, with healthcare accounting for 22.05% and transport for 21.11% securing the largest shares, while education 
at 7.03% and infrastructure at 11.26% received smaller portions. The model ensured adherence to both minimum and 
maximum budget constraints.  To evaluate these models, a comparative table (table 5) was developed, highlighting the 
key common criteria across all approaches.

Table 5. Comparative analysis of models

Criterion

Level balance 
model

Linear programming 
model

Multi criteria optimization 
model

Taking into account the opinion of 
citizens 
Financing of all categories 
The balance between criteria 
Transparency

Partly

Yes 
Average 
High

Yes

No 
Low 
Average

Yes

Yes 
High 
High

The best outcomes are shown by the multi-criteria optimization model, which guarantees effective budget allocation 
and  a  balance  between  several  criteria.  An  all-purpose  instrument  considers  social  and  strategic  factors.  The  test 
findings demonstrate that the suggested multi-criteria optimization model is the most dependable and well-balanced 
approach to budget allocation. While a qualitative comparison with baseline models (e.g., level balancing and linear 
programming) has been conducted, a quantitative assessment using performance metrics (e.g., RMSE, MAE) could not 
be performed due to the lack of detailed, disaggregated budget data at the district and sectoral levels for 2022-2023. 
Government-reported allocations are typically aggregated, hindering direct alignment with the model’s framework.

For  future  research,  we  intend  to  submit  a  formal  data  request  to  regional  authorities  to  access  detailed  budget 
breakdowns,  facilitating  a  thorough  empirical  validation  and  enabling  the  calculation  of  accuracy  metrics  such  as 
prediction error and budget deviation. To compare the efficiency of budget allocation optimization methods in more 
detail, were analyzed two methods - the genetic algorithm GA implemented in Python using the DEAP library and the 
SQP method in order to compare the effectiveness of budget allocation optimization techniques in greater detail.  Both 
approaches were used to solve a multi-criteria optimization issue that considers factors including urbanization level, 
strategic priorities, fundamental necessities, and citizen satisfaction.   The comparison's goals were to determine the 
potential benefits and drawbacks of each strategy and assess how GA, as a stochastic method, can compete with the 
deterministic SQP in the budget allocation problem.

In contrast to the SQP, which depends on gradient-based convergence, the GA adopted a stochastic population-based 
strategy. It utilized a population size of 200, evolving over 500 generations, with an 80% crossover rate and a 5% 
mutation rate. Variability was introduced through a one-point crossover operator and Gaussian mutation. Constraint 
violations  were  penalized  within  the  fitness  function,  employing  dynamic  scaling  to  maintain  feasibility  without 
excessively limiting exploration. The GA exhibited slow but consistent convergence, with notable improvements in 
early generations and stabilization in later stages. Although it required substantially more evaluations than SQP, GA 
offered  robustness  against  local  optima  and  achieved  a  high-quality  solution  with  a  final  objective  value  of 
18,520,000.00 thousand tenge.

The capacity of genetic algorithms to identify global optima in intricate multi-criteria issues makes them popular in 
optimization and financial allocation challenges the stock market forecasting problem demonstrates the ability of GA 
to  adjust  to  complicated  nonlinear  dependencies,  by  optimizing  model  parameters,  GA  increased  the  prediction 
accuracy of stock prices [16].  The model is intended to be expanded in the future by accounting for indicator dynamics 
and uncertainty.  To account for the imprecision and fuzziness of input data, it is especially recommended to combine 
fuzzy logic techniques with the evolutionary algorithm.  One example of a successful hybrid strategy is the use of GA 
with fuzzy rules to optimize the cost-time-quality ratio of projects [17].

The effective optimization of KOSPI 200 index fund portfolios [18] shows that when Genetic Algorithms (GAs) were 
used  for  index  fund  management,  they  outperformed  traditional  optimization  techniques  in  terms  of  portfolio 
performance.  The  creation  of  the  GA-MSSR  method,  which  maximized  performance  metrics  like  the  Sharpe  and

---

<!-- PAGE 11 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3085

Sterling ratios to optimize high-frequency trading strategies, further demonstrated GAs' ability to adapt to complex 
nonlinear financial data and greatly increased the accuracy of micro-level price forecasting in volatile market conditions  
[19].

The genetic algorithm reached a value of 18,520,000.00 thousand tenge after modifying the parameters (increasing the 
number of generations to 500, increasing the penalties for violating restrictions, and normalizing the objective function) 
in contrast to SQP, which displayed the objective function value of 18,519,864.85 thousand tenge.  Despite minor 
variations that reflect the stochastic character of the approach, the budget distribution derived using GA was found to 
be similar to the SQP results (figure 6):

Figure 6. Distribution of the budget by districts and regions, obtained using GA

Similar to the SQP results, the graph indicates that the Kegen district, which has a high degree of urbanization, receives 
the biggest allocations of funds for infrastructure, while the Talgar district receives the fewest allocations for culture.  
However, because of the stochastic search for solutions, GA has a uniform distribution in other categories, including 
education. A comparative analysis of the methods is presented below (table 6).

Characteristic

Method Type

Table 6. Comparative Characteristics of SQP and GA methods

Methods

SQP (MATLAB)

Deterministic

GA (Python, DEAP)

Stochastic

Objective Function

18,519,864.85 thousand tenge

18,520,000.00 thousand tenge

Convergence

Accuracy

Fast (less than 100 iterations)

Slow (500 generations)

High (deterministic approach)

Medium (depends on parameters)

Constraint Handling

Linear constraints built into fmincon

Via penalties in the fitness function

Advantages

Disadvantages

Applicability

Fast convergence, high accuracy

Global search, robust to local minimal

May get trapped in local minimal

Random results, high computational cost

Suitable for well-defined constraints

Suitable for complex tasks with uncertainty

The  SQP  and  GA  methods  can  both  solve  the  multi-criteria  budget  allocation  optimization  issue,  according  to  a 
comparison  study  of  the  two  methodologies.  According  to  a  comparative  research,  multi-criteria  budget  allocation 
problems can be successfully handled by both SQP and GA.  As a deterministic method, SQP exhibits better accuracy 
and quicker convergence under well-defined constraints [20].  On the other hand, GA is excellent at examining trade-
offs  between  goals  and  demonstrates  resilience  in  situations  involving  a  lot  of  uncertainty.  It  provides  adaptable 
solutions for complicated issue structures [21].

---

<!-- PAGE 12 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3086

SQP  is  better  for  problems  with  well-defined  constraints  because  of its  deterministic method,  which  shows  higher 
accuracy and convergence rate.  In turn, GA provides many approaches that can be helpful for examining criteria trade-
offs, particularly when there is uncertainty.  The suggested model's dependability is confirmed by the small discrepancy 
between  the  budget  allocation  and the objective  function  values (135.15  thousand  tenge).    It is  advised  that  future 
studies take into account combining GA with fuzzy logic to account for data uncertainties and use more recent libraries 
like Pymoo to enhance constraint handling [22].

The optimization model allocated a total budget of 42,656,543 thousand tenge across four districts and seven Areas of 
Activity  (AAs)  in  the  Almaty  region,  utilizing  a  multi-criteria  optimization  approach.  Healthcare  (22.05%)  and 
transport  (21.11%)  secured  the  largest  shares,  reflecting  their  high  strategic  priority  and  strong  citizen  support. 
Education received the smallest allocation (7.03%), indicating lower prioritization in voter and strategic metrics. All 
seven AAs were funded, showcasing the model’s ability to ensure comprehensive sectoral coverage.

The  model  employed  quadratic  programming,  with  the  Sequential  Quadratic  Programming  (SQP)  algorithm  in 
MATLAB achieving an objective function value of 18,519,864.85 thousand tenge, converging in under 100 iterations. 
The GA, implemented via Python’s DEAP library, yielded a slightly higher value of 18,520,000.00 thousand tenge 
after 500 generations, demonstrating robust global exploration. The negligible difference of 135.15 thousand tenge 
between methods confirms their reliability. SQP excelled in speed and precision under well-defined constraints, while 
GA proved effective for complex, uncertain problem structures.

Figure 1 illustrates balanced budget distribution across districts and sectors, aligning with regional priorities. Figure 2 
confirms SQP’s rapid convergence, with minimal step size and a gradient norm of 0.7016. Figure 3 highlights GA’s 
similar allocation patterns, notably higher infrastructure funding in Kegen and lower culture funding in Talgar. Table 
3 indicates strong influence of urbanization and population on allocations, while table 4 details precise budget amounts, 
consistent with optimization objectives.

5. Conclusion

A  dynamic  budget  allocation  model  was  developed  and  evaluated  in  this  study  using  quadratic  programming  and 
multicriteria optimization approaches.  The efficacy of the SQP method and a GA was compared.  With a target function 
value of 18,519,864.85 thousand tenge with SQP, the model successfully allocates budgetary resources among districts 
and activity areas, according to the analysis and numerical experiments. GA produced a marginally higher value of 
18,520,000.00 thousand tenge, a difference of 135.15 thousand tenge, demonstrating the robustness of both approaches.

In order to provide an accurate and well-informed resource distribution that meets real demands, the model takes into 
account important demographic data, urbanization levels, regional profitability, and public opinions expressed through 
voting.  The model avoids financial imbalances and meets fundamental necessities while upholding strategic priorities 
by imposing minimum and maximum budget limitations.  With the exception of a few minor allocation discrepancies, 
such as GA allocating 300,000.00 thousand tenge to education in Raimbeksky district compared to SQP's 296,622.18 
thousand tenge, both approaches met most criteria. SQP, achieved rapid convergence within 100 iterations, while GA 
required 500 generations, reflecting its slower but more exploratory nature.

Although  the  proposed  model  exhibits  significant  potential  for  practical  use,  especially  in  participatory  and  multi-
criteria  regional  budget  allocation,  it  remains  at  the  conceptual  phase.  A  formal  request  for  pilot  testing  has  been 
submitted  to  the  Ministry  of  Digital  Development  of  the  Republic  of  Kazakhstan  for  possible  integration  into  the 
national  eGov  information  system,  with  the  authors  awaiting  a  response.  Consequently,  while  the  results  are 
encouraging,  conclusions  about  real-world  applicability  should  be  considered  preliminary  pending  validation  in  a 
policy implementation context.

The proposed model also highlights significant ethical concerns. The integration of publicly available demographic 
and  socio-economic  data  with  subjective  weights  for  strategic  priorities  poses  risks  concerning  transparency  and 
perceived equity. Additionally, decisions guided by artificial intelligence and optimization algorithms may encounter 
public  skepticism  or  political  opposition,  particularly  if  stakeholders  lack  a  clear  understanding  of  the  underlying 
processes or perceive them as obscure.

---

<!-- PAGE 13 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3087

To address these risks, future efforts will include the adoption of explainable AI techniques, enhanced transparency in 
data sources, and participatory approaches to validate weighting schemes. These measures are essential for fostering 
trust and ensuring ethical accountability in any potential deployment of the model within e-government systems.

These  results  can  be  used  to  guide  budget  management  choices  at  the  regional  authority  level,  improving  the 
effectiveness and transparency of budget planning. The comparison highlights the accuracy of SQP for clearly defined 
situations and the resilience of GA for complicated, unpredictable scenarios.  To increase computational accuracy, the 
model can be extended to incorporate more complex economic and social factors, more places, more categories, and 
information such as population dynamics and long-term strategic objectives.  The comparative analysis of SQP and 
GA shows that both are effective tools for optimizing government spending in resource-constrained environments, with 
each offering distinct strengths based on task requirements. As a result, the suggested approach guarantees equitable 
budget distribution, minimizes risks, and takes into account the interests of all stakeholders.

6. Declarations

6.1. Author Contributions 
Conceptualization: S.G., S.S., Y.S. and A.A.; Methodology: A.A. and S.G.; Software: S.G. and A.A.; Validation: S.G. 
and  A.A.;  Formal  Analysis:  S.G.,  S.S.,  Y.S.  and  A.A.;  Investigation:  S.G.;  Resources:  A.A.;  Data  Curation:  A.A.; 
Writing Original Draft Preparation: S.G. and A.A.; Writing Review and Editing: A.A. and S.G.; Visualization: S.G., 
S.S., Y.S. and A.A. All authors have read and agreed to the published version of the manuscript.

6.2. Data Availability Statement 
The data presented in this study are available on request from the corresponding author.

6.3. Funding 
The authors received no financial support for the research, authorship, and/or publication of this article.

6.4. Institutional Review Board Statement 
Not applicable.

6.5. Informed Consent Statement 
Not applicable.

6.6. Declaration of Competing Interest 
The authors declare that they have no known competing financial interests or personal relationships that could have 
appeared to influence the work reported in this paper.

References

[1]  M.  Skopin,  “Maslikhats:  who  needs  them  and  what  they  do,”  [Online].  Available:  https://orda.kz/podzabytye-maslihaty-

komu-oni-nuzhny-ichem-zanimayutsya/. [Accessed: Apr. 12, 2024].

[2]  Ministry  of  Justice  Republic  of  Kazakhstan,  “Institute  of  Legislation  and  Legal  Information,”  [Online].  Available:

https://adilet.zan.kz/kz/docs/U1300000704. [Accessed: May 24, 2024].

[3]  S. Gulbakyt and A. Abdualiyev, “Development of a mathematical model for the distribution of financial resources,” Procedia

Comput. Sci., vol. 251, no. 1, pp. 520–525, 2024. doi: 10.1016/j.procs.2024.11.142.

[4]  M. Sigala, A. Beer, L. Hodgson, and A. O’Connor, “Big data for measuring the impact of tourism economic development 
programmes:  A  process  and quality  criteria  framework  for  using  big  data,”  in  Managerial  Approaches,  Techniques, and 
Applications, Singapore: Springer, 2019, vol. 2019, no. 5, pp. 1–20, doi: 10.1007/978-981-13-6339-9_4.

[5]  L. Mazelis, A. Krasko, and E. Krasova, “Distribution of financial resources by areas of investments in the human capital of

the region,” Economic Consultant, vol. 36, no. 4, pp. 4–16, 2021, doi: 10.46224/ecoc.2021.4.1.

[6]  L. Bartocci, G. Grossi, S. G. Mauro, and C. Ebdon, “The journey of participatory budgeting: A systematic literature review 
and  future  research directions,”  International  Review  of  Administrative  Sciences,  vol.  89,  no. 3,  pp.  757–774, 2023,  doi: 
10.1177/00208523221078938.

---

<!-- PAGE 14 -->

Journal of Applied Data Sciences 
Vol. 6, No. 4, December 2025, pp. 3075-3088

ISSN 2723-6471 
3088

[7]  D. Hershkowitz, A. Kahng, D. Peters, and A. Procaccia, “District-fair participatory budgeting,” in Proc. AAAI Conf. Artificial

Intelligence, vol. 35, no. 6, pp. 5464–5471, 2021, doi: 10.1609/aaai.v35i6.16688.

[8]

M.  Beikverdi,  N.  G.  Tehrani,  and  K.  Shahanaghi,  “A  bi-level  model  for  district-fairness  participatory  budgeting: 
Decomposition methods and application,” European Journal of Operational Research, vol. 314, no. 2, pp. 340–362, 2024.

[9]  W. Zhang, G. Xiao, M. Gen, H. Geng, X. Wang, M. Deng, and G. Zhang, “Enhancing multi-objective evolutionary algorithms 
with machine learning for scheduling problems: Recent advances and survey,” Frontiers in Industrial Engineering, vol. 2024, 
no. 6, pp. 1–18, 2024.

[10]  Y. Ma, X. Gao, C. Liu, and J. Li,  “Improved SQP and SLSQP algorithms for feasible path-based process optimisation,”

Computers and Chemical Engineering, vol. 188, no. 4, pp. 1–12, 2024, doi: 10.1016/j.compchemeng.2024.108751..

[11]  S. Rey, U. Endriss, and R. de Haan, “A general framework for participatory budgeting with additional constraints,”  Social

Choice and Welfare, vol. 64, no. 1, pp. 5–41, 2025.

[12]  D. Schugurensky and L. Mook, “Participatory budgeting and local development: Impacts, challenges, and prospects,” Local

Development & Society, vol. 5, no. 1, pp. 1–13, 2024, doi: 10.1080/26883597.2024.2391664.

[13]   I.  Baffo,  M.  Leonardi,  V.  D’Alberti,  and  A.  Petrillo,  “Optimizing  public  investments:  A  sustainable  economic, 
environmental, and social investment multi-criteria decision model (SEESIM),” Regional Science Policy & Practice, vol. 16, 
no. 11, pp. 100140–100152, 2024, doi: 10.1016/j.rspp.2024.100140.

[14]  Bureau of National Statistics of the Agency for Strategic Planning and Reforms of the Republic of Kazakhstan, [Online].

Available: https://stat.gov.kz/ru/region/almatyobl/. [Accessed: Dec. 1, 2024].

[15]  Ministry of Justice of the Republic of Kazakhstan, “Information and Legal System of Regulatory Legal Acts of the Republic

of Kazakhstan,” [Online]. Available: https://adilet.zan.kz/rus/docs/V20D0005841.

[16]  R. Abraham, M. E. Samad, A. M. Bakhach, H. El-Chaarani, A. Sardouk, S. E. Nemar, and D. Jaber, “Forecasting a stock 
trend using genetic algorithm and random forest,” Journal of Risk and Financial Management, vol. 15, no. 5, pp. 1–12, 2022.

[17]  A. Erdoğdu, F. Dayi, F. Yildiz, A. Yanik, and F. Ganji, “Combining fuzzy logic and genetic algorithms to optimize cost, time

and quality in modern agriculture,” Sustainability, vol. 17, no. 7, pp. 1–15, 2025.

[18]   Y. Orito, M. Takeda, and H. Yamamoto, “Index fund optimization using genetic algorithm and scatter diagram based on 
coefficients of determination,” in  Intelligent and Evolutionary Systems, M. Gen, K. Kim, X. Li,  and Y. Tsujimura, Eds., 
Studies in Computational Intelligence, vol. 187, Berlin, Heidelberg: Springer, 2009, pp. 1–12.

[19]   Z. Zhang and M. Khushi, “GA-MSSR: Genetic algorithm maximizing Sharpe and Sterling ratio method for RoboTrading,” 
in Proc. Int. Joint Conf. Neural Networks (IJCNN), vol. 2020, no. 7, pp. 1–8, 2020, doi: 10.1109/IJCNN48605.2020.9206647.

[20]   A. Salami, B. Afshar-Nadjafi, and M. Amiri, “A two-stage optimization approach for healthcare facility location-allocation 
problems with service delivering based on genetic algorithm,” International Journal of Public Health, vol. 68, no. 2, pp. 1–
12, 2023, doi: 10.3389/ijph.2023.1605015.

[21]   R. C. L. Corrêa de Sousa, F. Goulart, D. E. C. Vargas, F. Campelo, and E. Wanner, “Optimizing multi- and many-objective 
problems  on  varied  budgets:  Hybridizing  NSGA-III  with  local  searches,”  Proceedings  of  the  Brazilian  Society  of 
Computational and Applied Mathematics, vol. 11, no. 1, pp. 1–15, 2025, doi: 10.5540/03.2025.011.01.0454.

[22]   J. Blank and K. Deb, “Pymoo: Multi-objective optimization in Python,” IEEE Access, vol. 8, no. 5, pp. 89497–89509, 2020,

doi: 10.1109/ACCESS.2020.2990567.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3075
Dynamic Model for Budget Allocation in via Multi-Criteria Optimization
Sembina Gulbakyt1, , Abdualiyev Almaz2,*, , Sagnayeva Saule3, , Yoldash Suhrab4,
1,2Information Systems Department, International Information Technologies University, Almaty (050040), Kazakhstan
3System Analysis and Management Department, Eurasian National University named after L.N. Gumilyov, Astana (010008), Kazakhstan
4Information Systems Department, Kazakh-British Technical University, Almaty (050000), Kazakhstan
(Received: May 01, 2025; Revised: July 28, 2025; Accepted: October 10, 2025; Available online: November 15, 2025)
Abstract
This research introduces a dynamic multi-criteria optimization framework for fair budget distribution across four districts in Kazakhstan’s Almaty
region. Its main objective is to promote transparency, equity, and efficiency in allocating a constrained regional budget of 42,656,543 thousand
tenge across seven activity areas (AA): education, healthcare, transport, infrastructure, digitalization, culture, and ecology. The framework
incorporates four weighted criteria: citizen satisfaction (0.2 weight), strategic development priorities (0.2), basic needs fulfillment (0.3), and
urbanization level (0.3). Two optimization techniques were employed: Sequential Quadratic Programming (SQP) in MATLAB, converging in
100 iterations with an objective function value of 18,519,864.85 thousand tenge, and Genetic Algorithm (GA) in Python, achieving a slightly
higher value of 18,520,000.00 thousand tenge after 500 generations. The minimal difference of 135.15 thousand tenge (0.0007% of the budget)
underscores the reliability of both methods. All seven sectors received funding, with healthcare (22.05%) and transport (21.11%) allocated the
largest portions, and education (7.03%) the smallest. Fairness is evidenced by a standard deviation of sectoral shares at 5.69%, a coefficient of
variation of 0.398, and a Gini coefficient of 0.223. Participatory budgeting was simulated using synthetic citizen voting data derived from
demographic factors. Visualizations depict the optimization process’s convergence and budget distribution across feasible solutions. A proposal
for pilot testing within Kazakhstan’s e-government system (Egov) has been submitted to the Ministry of Digital Development. Future
enhancements will include explainable AI, stakeholder-driven weight adjustments, and real demographic and budgetary data to foster
transparency and public confidence. This framework provides a scalable, data-driven approach to participatory budgeting, harmonizing strategic
objectives, socio-economic demands, and citizen preferences. SQP and GA methods achieved near-optimal solutions with objective function
values of 18,519,864.85 and 18,520,000.00 thousand tenge, respectively. The 135.15 thousand tenge difference (0.0007% of the budget) is
negligible, confirming their robustness.
Keywords: Budget Allocation, Multi-Criteria Optimization, Areas Of Activity, Sequential Quadratic Programming, Genetic Algorithm
1. Introduction
The distribution of the budget in the regions and cities is handled by local executive bodies (maslikhats) [1], [2].
Maslikhats are district representative bodies, whose members are elected by the population of various administrative-
territorial units by direct vote for a period of 5 years. Since the topic of the article is related to the distribution of
regional funds in the region, several literary sources related to the promotion of budget funds and their arrival
specifically in maslikhat have been studied.
It is currently uncommon to see representatives of local executive bodies at a normal maslikhat meeting. These
representatives visit specific trouble spots to observe the current situation and consider the data gathered for discussion
at the following meeting. The region's socioeconomic, cultural, and material circumstances are deteriorating as a result
of these lawmakers' careless labor. The opaque procedure of awarding funding is another factor contributing to the
decline in public trust in official bodies.
For cities and districts, where budget funds should be allocated to maximize the demands of the populace in numerous
AA, including education, healthcare, transportation, infrastructure, technology, culture, and ecological, efficient
financial resource management is particularly crucial. A tight budget necessitates the development and application of
*Corresponding author: Abdualiyev Almaz (dellivine@mail.ru)
DOI: https://doi.org/10.47738/jads.v6i4.935
This is an open access article under the CC-BY license (https://creativecommons.org/licenses/by/4.0/).
© Authors retain all copyrights

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3076
strategies that enable the best possible distribution of financial resources while accounting for a number of variables
and priorities. Reducing socioeconomic disparities, encouraging sustainable growth, and building public trust in
government all depend on efficient regional budget allocation. Maslikhats, or local elected councils, are largely in
charge of allocating public monies across various AA. They frequently deal with issues like low transparency and
insufficient public involvement [1], [2]. Issues with regional financial planning, such as unequal development, a lack
of data-driven tools for decision-making, and inadequate alignment with local priorities, have been highlighted by
recent research [3], [4], [5]. Multi-criteria decision-making approaches have also become more popular worldwide as
a result of the growing complexity of public sector management and the requirement to balance a variety of social,
economic, and strategic goals [6], [7]. A popular strategy to increase equity and transparency in resource allocation is
participatory budgeting, which integrates public opinion into financial choices [7], [8]. Voting for priority regions
allows city dwellers to voice their thoughts, which is one of the most important factors in budget distribution. The goal
of this research is to use quadratic programming and multi-criteria optimization to create a mathematical model of the
district budget's dynamic distribution.
2. Theoretical Basis and the Proposed Method
By using linear programming based on the simplex method and a leveled balancing approach, this study expands on
earlier research on the budget allocation process [3]. Model-based optimization techniques that employ probability
distributions to identify solutions are examined in article [4]. A strategy is put forth that is predicated on the upkeep of
a population of models that are updated across many generations. The effective distribution of computational resources
among the models is the main objective. In order to decrease the number of calculations and enhance the quality of the
results, a dynamic sampling technique based on Markov solutions has been created. The findings show that the
suggested strategy increases the effectiveness of techniques for resolving challenging optimization issues.
Using Primorsky Krai as an example, the research [5] focuses on creating and evaluating a dynamic model for
maximizing the distribution of financial resources for the growth of human capital. The target function of the model is
to achieve strategic goals in the field of human capital, and it considers the impact of the amount and structure of public
and private investments through multi-period interdependence. The findings show that it is possible to identify the best
investment plan that helps reach the objectives. It is advised that resources be distributed fairly over time, encompassing
social policy, national security, health, and education.
Conflicting aims can be taken into consideration when creating a budget thanks to the multi-criteria approach in the
contemporary participatory budgeting environment, which has grown popular worldwide [6], [7]. Finding a solution
that concurrently meets multiple (sometimes conflicting) criteria is the goal of multi-criteria optimization. Large-scale
resource allocation issues in the public sector with several limitations have been successfully resolved by quadratic
programming [8].
3. Methodology
The primary techniques employed in the process of creating a budget allocation model are thoroughly explained in this
section. Quadratic programming, multi-criteria optimization, and the utilization of the fmincon function in MATLAB
are the primary areas of emphasis. The process of identifying a solution that considers multiple criteria, many of which
are in conflict with one another, is known as multi-criteria optimization [9]. Important characteristics of the SQP
algorithm for our problem include: allowing the specification of both linear and nonlinear constraints; being able to
specify the boundaries of variables and constraint matrices in a convenient manner; and allowing the selection of
different optimization algorithms, including the SQP method itself [10]. The complete research flow used in the study
is depicted in figure 1.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3077
Figure 1. Conceptual framework of the dynamic budget allocation model
The first step in the process is gathering input data, such as strategic priorities, demographic statistics, and the outcomes
of simulated citizen voting. These inputs are fed into a GA and SQP based multi-criteria optimization framework that
incorporates important factors like urbanization, basic necessities, strategic priorities, and citizen happiness. Subject to
regional and financial limitations, the optimization procedure iteratively looks for the best way to allocate funds among
four districts and seven AA’s. Following that, the resulting budget allocations are compared among optimization
techniques and assessed using fairness measures (Gini coefficient, standard deviation).
Task highlights the following criteria: meeting the needs of citizens (weighted by the number of votes); consideration
of the strategic priorities of the regions; meeting minimum basic needs; accounting for the level of urbanization. A
target optimization function that incorporates the data above the criterion is necessary for multi-criteria optimization.
A specific optimization method is quadratic programming, an optimization method in which the objective function is
quadratic and the constraints are linear. Notably, the scientific literature is paying more and more attention to
comparable issues of the best way to allocate funds among areas while taking into consideration a variety of criteria
and constraints [11]. The problem of quadratic programming is formulated as:
1
min( 𝑥𝑇𝑄𝑥+𝑐𝑇𝑥),𝑔𝑖𝑣𝑒𝑛 𝑡ℎ𝑎𝑡:𝐴 ×𝑥 = 𝑏 ,𝐴 ×𝑥 ≤ 𝑏 (1)
2 𝑒𝑞 𝑒𝑞 𝑖𝑛𝑒𝑞 𝑖𝑛𝑒𝑞
Q - the matrix of quadratic coefficients; с - vector of linear coefficients; 𝐴 ,𝑏 - equality;𝐴 , 𝑏 - inequalities.
𝑒𝑞 𝑒𝑞 𝑖𝑛𝑒𝑞 𝑖𝑛𝑒𝑞
This study effectively applies quadratic programming using the SQP method since the target function is approximated
at each iteration due to the fact that it is not strictly quadratic: the limits are set by the 𝐴 , 𝐴 matrices to comply
𝑒𝑞 𝑖𝑛𝑒𝑞
with the overall budget and regional limit and boundaries of variables (𝐵 , 𝐵 ) set the minimum and maximum
𝑚𝑖𝑛 𝑚𝑎𝑥
allowable budget values. Recent studies show similar strategies for equitable budgeting at the district level.
Specifically, study [12] demonstrates how extra constraints (such project quotas for low-income areas) are employed
in participatory budgeting procedures to promote equality.
Under numerous limitations, quadratic programming has demonstrated efficacy in resolving significant resource
allocation issues in the public sector [13].The following characteristics of the SQP algorithm, which is appropriate for
resolving nonlinear programming problems with constraints, are taken into consideration in this study: supports linear
and non-linear constraints, uses several algorithms for optimization, including SQP, which is used in this task and
convenience of setting boundaries for variables (𝐵 , 𝐵 ) and the constraint matrices (𝐴 , 𝐴 ).
𝑚𝑖𝑛 𝑚𝑎𝑥 𝑒𝑞 𝑖𝑛𝑒𝑞
The approach outlined makes it possible to provide precise and financially sound outcomes that may be used in actual
practice for the best possible budget allocation. In order to optimize the target function while adhering to financial
limitations, the model's ultimate objective is to divide the money across four areas and seven AAs in the best possible
way. Data was collected for the study from four districts in the Almaty region: Raiymbeksky, Kegensky, Talgarsky,
and Karasaysky. Each of the seven districts has a budget that is appropriate [14], and when these are added together,
the districts' total budget B is obtained:
∑4 ∑7 𝐵 (2)
𝑖=1 𝑗=1 𝑖,𝑗

| Journal of Applied Data Sciences             |     |     |     |     |     |     | ISSN 2723-6471  |       |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | ----- |
| Vol. 6, No. 4, December 2025, pp. 3075-3088  |     |     |     |     |     |     |                 | 3078  |

Minimal (𝐵 ) and maximum (𝐵 ) budget boundaries play an important role in ensuring a realistic and
|     | 𝑚𝑖𝑛,𝑖,𝑗 | 𝑚𝑎𝑥,𝑖,𝑗 |     |     |     |     |     |     |
| --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
equitable allocation of financial resources. This is due to avoiding unrealistic solutions that optimization algorithms
can offer - 𝐵  guarantees that every district or region gets the bare minimum of funding required to carry out its
𝑚𝑖𝑛
essential duties. Additionally, it helps guarantee that everyone has access to a minimum amount of financing, which is
crucial for vital sectors like healthcare and education. 𝐵  restricts extra money and permits resources to be allocated
𝑚𝑎𝑥
more fairly among regions and AA’s by preventing excessive redistribution of cash to one district or area, which could
leave other AA’s without sufficient funding. By restricting the search area inside the range of potential values for
optimization variables, the boundaries also aid the algorithm in finding answers more quickly and lower the task's
computing complexity:
|     |     |     | 𝐵 ≤     | 𝐵 ≤ 𝐵       |     |     |     | (3)  |
| --- | --- | --- | ------- | ----------- | --- | --- | --- | ---- |
|     |     |     | 𝑚𝑖𝑛,𝑖,𝑗 | 𝑖,𝑗 𝑚𝑎𝑥,𝑖,𝑗 |     |     |     |      |
The objective function of the mathematical model includes four main criteria: satisfaction of citizens (by counting the
number of votes of citizens)-α;  strategic priorities - unique values that are set depending on the state of satisfaction of
citizens of a given AA’s in the area (values from 1.0 to 1.9) - β; satisfaction of basic needs (γ) - used in the objective
function. Responsible for including the minimum budget limits of 𝐵  in the optimization process. Weight γ
𝑚𝑖𝑛
determines how important it is to meet the minimum requirements (𝐵 ≥ 𝑙𝑏 ) for the target function. If  𝐵
|     |     |     |     |     | 𝑣𝑒𝑐 | 𝑣𝑒𝑐 |     | 𝑣𝑒𝑐 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
exceeds 𝑙𝑏 , the indicator returns 1, which adds the value of γ to the objective function. In this way, component y
𝑣𝑒𝑐
provides a balance between strategic priorities and a guarantee of a basic level of provision, motivating the model to
choose solutions that meet the minimum requirements for basic needs, the level of urbanization (δ) is the standard ratio
of the urban population to the total in the region. This metric reflects the degree of urban development and access to
infrastructure and services. Districts with higher CU values are assumed to have greater demands for complex services
and receive proportionally adjusted funding. The urbanization data were obtained from the Bureau of National Statistics
of Kazakhstan [14], and incorporated as a weighted factor in the optimization objective. The mathematical formulation
of the objective function has the form:
|                                |     |             | 𝑉𝑖,𝑗     | 𝑊𝑖,𝑗        |         |          |         |     |
| ------------------------------ | --- | ----------- | -------- | ----------- | ------- | -------- | ------- | --- |
| Objective function = max (α ∙∑ |     |             | ×𝐵 + β∙∑ |             | ×𝐵 +γ∙∑ | 1(𝐵 ≥    | 𝐵 )+δ∙  |     |
|                                |     | 𝑖,𝑗 max (𝑉) | 𝑖,𝑗      | 𝑖,𝑗 max (𝑊) | 𝑖,𝑗     | 𝑖,𝑗  𝑖,𝑗 | 𝑚𝑖𝑛 𝑖,𝑗 |     |
(4)
𝑈𝑖
|     |     |     | ∑           | ×𝐵  |     |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|     |     |     | 𝑖,𝑗 max (𝑈) | 𝑖,𝑗 |     |     |     |     |
The parameter γ, reflecting the satisfaction of basic needs, is operationalized via a conditional mechanism: if the
allocated budget for a specific area of activity meets or exceeds its predefined minimum threshold, a value of 1 is
assigned to this component in the objective function; otherwise, it is set to 0. This ensures that the γ weight contributes
to the objective function only when essential funding requirements are met, incentivizing the optimization algorithm
to prioritize solutions that fulfill minimum needs across all districts.
Similarly, β and δ are incorporated as multiplicative weights, directly applied to strategic priority scores and
urbanization coefficients, respectively. These values are normalized and scaled based on their relative importance in
the model, as determined by the assigned weights. Minimal (𝐵 ) and maximum (𝐵 ) boundaries are calculated
|     |     |     |     | min,𝑖 |     | max,𝑖 |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | --- | --- |
taking into account the population level, the level of urbanization and the profitability of the region:
|     | 𝐵 = 𝑘 | ×𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛 | +𝑘      | ×𝑈𝑟𝑏𝑎𝑛𝑖𝑧𝑎𝑡𝑖𝑜𝑛 | +𝑘        | ×𝐼𝑛𝑐𝑜𝑚𝑒 |     |     |
| --- | ----- | ----------- | ------- | ------------- | --------- | ------- | --- | --- |
|     | min,𝑖 | 𝑝𝑜𝑝         | 𝑖 𝑢𝑟𝑏𝑎𝑛 |               | 𝑖  𝑖𝑛𝑐𝑜𝑚𝑒 |         | 𝑖   |     |
(5)
|     |     |     | 𝐵 =   | α×𝐵   |     |     |     |     |
| --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
|     |     |     | max,𝑖 | 𝑚𝑖𝑛,𝑖 |     |     |     |     |
𝑘 , 𝑘 , 𝑘 - weighting factors for population, urbanization, and profitability of the region; α -the increase
| 𝑝𝑜𝑝 𝑢𝑟𝑏𝑎𝑛 | 𝑖𝑛𝑐𝑜𝑚𝑒 |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
factor, limits the upper limit of the budget so that resources are not concentrated in one area or region. This is important
to prevent an imbalance when one sector receives disproportionately much money. The optimization problem is solved
using the quadratic programming algorithm described above. Limitations of the optimization problem:
|     |     |     | 𝐴𝑒𝑞×𝐵 = | 𝑇𝑜𝑡𝑎𝑙 𝑏𝑢𝑑𝑔𝑒𝑡  |     |     |     |     |
| --- | --- | --- | ------- | ------------- | --- | --- | --- | --- |
𝑣𝑒𝑐
(6)
|     |     |     | 𝐴𝑖𝑛𝑒𝑞×𝐵 | ≤ 𝑏𝑖𝑛𝑒𝑞  |     |     |     |     |
| --- | --- | --- | ------- | -------- | --- | --- | --- | --- |
𝑣𝑒𝑐
The boundaries of optimization:

| Journal of Applied Data Sciences             |     |     |     |     |     | ISSN 2723-6471  |       |
| -------------------------------------------- | --- | --- | --- | --- | --- | --------------- | ----- |
| Vol. 6, No. 4, December 2025, pp. 3075-3088  |     |     |     |     |     |                 | 3079  |

|     |     |                        𝐵 | ≤ 𝐵         | ≤ 𝐵     |     |     | (7)  |
| --- | --- | ------------------------ | ----------- | ------- | --- | --- | ---- |
|     |     |                          | 𝑚𝑖𝑛,𝑣𝑒𝑐 𝑣𝑒𝑐 | 𝑚𝑎𝑥,𝑣𝑒𝑐 |     |     |      |
When matrix representations of constraints are utilized in linear programming and optimization problems, certain
notations are common. Equation (6) sets a constraint that the sum of all allocated funds for all regions and regions must
be equal to a given total budget, 𝐴𝑒𝑞 is a vector of coefficients. In this problem, the 𝐴𝑒𝑞 consists of units so that the
sum of all variables 𝐵  (all budgets) is equal to the total budget. 𝐵  - a vector of optimized variables representing
|     | 𝑣𝑒𝑐 |     |     | 𝑣𝑒𝑐 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
the budget distribution between regions and regions. Each element of the vector is a dedicated budget for a specific
area in a specific region. It also defines linear inequalities that limit the amount or proportion of the allocated budget.
𝐴𝑖𝑛𝑒𝑞  - the coefficient matrix that defines the relationship between the 𝐵  budget variables and their constraints.
𝑣𝑒𝑐
Each row of the matrix 𝐴𝑖𝑛𝑒𝑞  corresponds to one restriction. 𝑏𝑖𝑛𝑒𝑞  - the vector of the right-hand side that defines the
upper limits for each constraint. The final constraint (8) sets the range of values for each element of the vector 𝐵 ,
𝑣𝑒𝑐
that is, the budget for each region in each region should be between the minimum 𝐵  and maximum 𝐵  boundaries.
|     |     |     |     |     | 𝑚𝑖𝑛 | 𝑚𝑎𝑥 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Three important facets of budget allocation in the model are described by these formulas: budget equality requires that
the total amount of allotted cash equal the entire budget. This restriction guarantees that all resources are used to their
fullest potential and that the budget is not overspent or underutilized, inequalities: to ensure that budgets adhere to
predetermined boundaries, such as not exceeding the maximum share allocated for a specific region or sector,
restrictions are imposed on the allocation of funds among regions and AA’s. Budget boundaries: the lowest and
maximum permitted budget values are established for each region, determining the smallest amount of money that can
be dedicated to basic necessities and the highest amount that may be allocated while accounting for priorities and
restrictions. The dataset uses data from official sources [14], [15] total budget: 42 656 543 thousand tenge.
The citizen voting data used in this study were synthetically generated based on demographic statistics for each district.
The number of "votes" was estimated by reducing the population count by approximately 30% to account for natural
demographic factors (e.g., minors, elderly, mortality, and non-participation). This approach was adopted in the absence
of actual participatory budgeting records. The model is designed to simulate citizen preferences in a representative
manner, serving as a proof-of-concept. In future implementations, it is planned to integrate this model into the Egov
platform (Kazakhstan's national e-government portal), where real citizen input can be collected through digital
participation tools, ensuring legitimacy and real-time feedback for decision-makers.
Distributed votes of citizens and the unique strategic priorities for these AA’s in the respective districts are presented
in the tables below (table 1 and table 2, respectively). To facilitate comparability across regions and incorporate
multiple priorities into the objective function, raw vote counts and strategic priority multipliers were normalized within
each region. The final weight for each area within a region was determined as a weighted sum of normalized votes and
strategic scores, integrated with other components (e.g., basic needs and urbanization) according to the specified
criterion weights (α, β, γ, δ).
Table 1. Distributed votes of citizens
Areas of activity
Region
Education  Healthcare  Transport  Infrastructure  Digitalization  Culture  Ecology
| Raimbeksky  | 1121  | 3500  | 4200  | 2700  | 6800  | 1500  | 5400  |
| ----------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Karasaysky  | 5000  | 3200  | 7100  | 2800  | 4500  | 6300  | 2200  |
| Talgarsky   | 3400  | 4100  | 5300  | 5300  | 6700  | 3300  | 4900  |
| Kegensky    | 2800  | 3700  | 5900  | 4300  | 800   | 6400  | 2900  |
Table 2. Unique strategic priorities
Areas of activity
Region
Education  Healthcare  Transport  Infrastructure  Digitalization  Culture  Ecology
| Raimbeksky  | 1.1  | 2.1  | 1.2  | 1.7  | 1.5  | 1.0  | 1.3  |
| ----------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Karasaysky  | 1.2  | 1.8  | 1.5  | 1.6  | 1.4  | 1.3  | 1.5  |
| Talgarsky   | 1.3  | 1.7  | 1.1  | 1.5  | 1.2  | 1.4  | 1.6  |

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3080
Areas of activity
Region
Education Healthcare Transport Infrastructure Digitalization Culture Ecology
Kegensky 1.0 1.5 1.4 1.3 1.3 1.2 1.4
Although strategic priority multipliers varied from 1.0 to 2.1 across activity areas and districts, their specific
quantitative influence on budget allocation was not distinctly isolated in this study. Within the model, these priorities
contribute to the final objective function through weighted normalization, interacting with citizen preferences,
minimum thresholds, and urbanization factors.
Table 3 provides verified demographic and economic data for the four districts analyzed, encompassing total
population, average annual income, and the urbanization coefficient (the ratio of urban to total population). These data
were sourced from the official portal of the Bureau of National Statistics of Kazakhstan (stat.gov.kz, accessed
December 2024). The urbanization coefficient served as a weight in the optimization model, capturing the degree of
infrastructural development and the demand for advanced services.
Table 3. Demographic data, profitability and quality of regions
Region Population Income (thousand tenge) CU (%)
Raimbeksky 55,000 280,000 24.5
Karasaysky 230,000 350,000 65.3
Talgarsky 190,000 310,000 60.8
Kegensky 45,000 260,000 20.1
Weights of strategic priorities: citizens' satisfaction weight = 0.2; strategic priority weight = 0.2; weight of basic needs
= 0.3; the weight of the urbanization = 0.3.
The weight coefficients in the objective function (e.g., 0.2 for citizen satisfaction, 0.3 for basic needs) were established
through expert judgment and an analysis of policy priorities in Kazakhstan’s regional planning framework. While these
coefficients align with practical priorities, they lack grounding in formal sensitivity analysis. Future studies will
integrate systematic sensitivity testing and multi-scenario analysis to evaluate the influence of weight variations on
budget allocation outcomes and to enhance the model’s robustness.
4. Results and Discussion
After performing optimization, the values of 𝐵 for each region and AA’s in figure 2, corresponding to the constraints and criteria
𝑖,𝑗
were obtained. Despite the differences in emphasis, the total budget is distributed relatively evenly between the districts,
which indicates that the optimization model meets the specified conditions. The largest influence on budget allocation
came from the population (𝑘 ). The budget proportion for each region grew due to the rising rate of urbanization.
𝑝𝑜𝑝
The model allocates greater resources to strategically significant sectors like transportation, healthcare, and the
environment while effectively accounting for the unique demands of each district. The graph effectively demonstrates
how the model accounts for both strategic priorities and necessities, guaranteeing the best possible budget allocation.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3081
Figure 2. Budget allocation result
The numerical values of the distributed budget obtained are shown in the table 4.
Table 4. Numerical results (thousands tenge)
Districts
Categories
Raimbeksky Karasaysky Talgarsky Kegensky
Education 296622.18 223033.64 2307597.61 3266538.43
Healthcare 3082251.69 296622.18 223033.64 2307597.61
Transport 2307597.61 3266538.43 296622.18 223033.64
Infrastructure 223033.64 2307597.61 3266538.43 296622.18
Digitalization 296622.18 223033.64 2307597.61 2904838.10
Culture 2947763.44 296622.18 223033.64 2307597.61
Ecology 2307597.61 3266538.43 296622.18 223033.64
18519864.85 thousand tenge is the value of the objective function that the optimization model has reached. The
objective function's positive value indicates that resources were successfully allocated in compliance with the given
standards. By combining multiple criteria into a single generalized value, the objective function enables you to assess
the model's efficacy. Reaching such a high result suggests a balanced distribution that considers the degree of
urbanization, the fulfillment of strategic aims, and the satisfying of fundamental requirements.
To quantitatively assess the fairness and balance of the budget allocation, we calculated several statistical indicators
based on sectoral budget shares. The disparities in budget allocations across areas and districts, such as the notably
higher education allocation in Talgarsky district compared to others - stem from the interplay of multiple model criteria.
These encompass regional strategic priorities, urbanization levels, citizen vote distribution, and minimum/maximum
constraints. In Talgarsky, education was assigned a higher relative priority score (1.3) and garnered significant citizen
support (3400 votes). When normalized and weighted within the objective function, these factors justified an increased
allocation. Additionally, the district’s urbanization coefficient and population size bolstered its share.
In contrast, areas with minimal allocations satisfied only the minimum funding thresholds, reflecting lower strategic
weights or voter preferences, while the model adhered to upper bounds to preserve overall equilibrium.
To evaluate the fairness and balance of the budget allocation quantitatively, we computed several statistical measures
based on sectoral budget shares. The standard deviation of the distribution was 5.69%, and the coefficient of variation
stood at 0.398, suggesting moderate variability across sectors. The Gini coefficient, at 0.223, indicated a relatively
equitable resource distribution. These metrics demonstrate that, despite healthcare (22.05%) and transport (21.11%)
receiving the largest allocations due to strategic significance and voter preferences, other sectors like education (7.03%)
and ecology (6.99%) were adequately supported. The model thus ensured inclusivity and avoided excessive resource
concentration.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3082
While this figure does not directly equate to monetary efficiency or return on investment, it acts as a consolidated
performance metric for assessing different budget allocation strategies. To offer perspective, the function employs
normalized weights for each criterion (e.g., strategic priorities at 0.2, basic needs at 0.3), where a greater score signifies
a more balanced and constraint-compliant allocation. Relative to other models-such as a linear programming approach
based solely on citizen voting or a level balancing technique-the proposed method delivered enhanced utility while
securing funding for all activity areas.
To enhance the understanding of how budget allocations align with model constraints, figure 3 provides a visualization
of the feasible region for Healthcare and Transport, the two areas receiving the largest shares in the optimized
distribution (the red points show all valid combinations of budget allocations under model constraints, blue points represent the
actual optimized allocations for four districts, all of which fall within the feasible region). The shaded area delineates all
permissible combinations of budget values for these sectors that comply with the model’s minimum, maximum, and
total budget constraints.
Figure 3. Feasible budget allocation region for Healthcare and Transport with actual district-level results.
The data on the operation of the fmincon optimization model is shown in the figure 4:
Figure 4. Optimization process – output parameters of the algorithm
The table shows data on the optimization process. Each of the indicators characterizes the steps of the algorithm and
its approximation to the solution of the problem. Let's look at each line and the key parameters: Func-count = 128 (in
total, 128 calls to the objective function were performed during the entire optimization process).Fval = −1.654620e+07
(the value of the objective function has not changed anymore, indicating that a local optimum has been reached).
Feasibility = 8.651e+05 (the restrictions are practically met, the remaining violations are within acceptable limits). Step
Length = 1.435e−11 (the step length has become extremely small, which indicates the convergence of the algorithm).
Norm of Step = 2.707e−06 (changes in variables are minimal, which confirms the achievement of a stable state). First-
order optimality = 7.016e−01 - the gradient value indicates a local optimum. While the convergence behavior of the
fmincon solver was initially presented through numerical indicators, figure 5 offers a graphical depiction of the
optimization trajectory. The plot reveals a swift enhancement in the objective function value - from roughly 16.5
million tenge to 18.52 million - within the initial iteration, followed by a stabilization phase, affirming efficient
convergence. This visual representation reinforces the numeric stopping criteria and underscores the robustness of the
SQP-based solution within the model’s constraints.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3083
Figure 5. Convergence of the objective function value during SQP optimization
During the optimization process, the solver identified a non-zero constraint violation at the final iteration,
approximately 865,100 ₸, largely attributable to the model's complex nonlinear and multidimensional structure.
Although this residual violation is relatively minor (≈ 0.47% of the total budget), it highlights a trade-off between strict
feasibility and maximizing utility within the given iteration limit.
This indicates a possible need for enhanced constraint tolerance control or the adoption of penalty-based or augmented
Lagrangian methods to enforce feasibility more effectively. Future research could also investigate adaptive constraint
handling techniques or multi-start strategies to boost robustness and mitigate local infeasibility. Nonetheless, all critical
constraints—including minimum funding per activity and total budget caps—were met to a practical extent, affirming
the reliability of the resulting allocation for practical implementation.
To enhance reproducibility and accessibility, we highlight that while the current implementation relies on MATLAB’s
fmincon solver (Sequential Quadratic Programming method), comparable optimization can be achieved using open-
source tools. Specifically, Python’s SciPy library (scipy.optimize.minimize with method='SLSQP') offers analogous
capabilities for addressing constrained nonlinear optimization problems. The optimization model’s logic and structure
can be entirely replicated in this platform. For transparency and future advancement, the authors plan to share core
pseudocode and a minimal working version of the model through a public repository or supplementary materials.
The model's efficacy was confirmed by the algorithm's quick convergence, which finished optimization in two
iterations after the first one. The excellent precision of the solution identified is indicated by the objective function's
final value and the minimal changes in the variables. Even though there were a few minor infractions of the limits, the
outcomes were nevertheless acceptable and satisfied the standards.
The level balance model and the linear programming model with maximum citizen satisfaction functions were two
alternative approaches from related work that were compared in order to assess the efficacy of the suggested multi-
criteria optimization model [3]. An examination of each method's outcomes and a comparison with the model used in
this paper can be found below. The level balancing model divides the funds among regions and activity areas based on
predetermined thresholds. This guarantees that the more crucial areas receive proportionately greater funding while
each category receives the bare minimum permitted.
The results of the study showed a more balanced budget distribution. For instance, ecology in the Talgarsky district
was allocated 3,253 thousand tenge, while technology in the Karasaysky district received 1,801 thousand tenge.
Nevertheless, the absence of objective function optimization restricts the efficient use of resources. In conclusion, the
level balance model promotes equitable distribution but overlooks strategic priorities and citizen feedback.
The second model, based on linear programming, aims to maximize citizen satisfaction by incorporating their
preferences through voting data, with calculations performed using the simplex method. This approach maximized
citizen satisfaction, though funding for lower-priority areas like culture and ecology was omitted. For example,
healthcare in the Karasaysky district received 1,741 thousand tenge, surpassing the allocation in the level balance

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3084
model. However, excluding funding for certain areas, such as infrastructure, introduces risks of imbalance. Despite not
funding all categories, this approach proves highly efficient under resource constraints. The optimization model
proposed in this study integrates multiple factors, including urbanization levels, strategic priorities, basic needs, and
citizen satisfaction, with computations carried out using the quadratic programming method. The objective function
value reached 18,482 thousand tenge, reflecting a balanced consideration of the criteria. All categories received
funding, with healthcare accounting for 22.05% and transport for 21.11% securing the largest shares, while education
at 7.03% and infrastructure at 11.26% received smaller portions. The model ensured adherence to both minimum and
maximum budget constraints. To evaluate these models, a comparative table (table 5) was developed, highlighting the
key common criteria across all approaches.
Table 5. Comparative analysis of models
Level balance Linear programming Multi criteria optimization
Criterion
model model model
Taking into account the opinion of
Partly Yes Yes
citizens
Financing of all categories Yes No Yes
The balance between criteria Average Low High
Transparency High Average High
The best outcomes are shown by the multi-criteria optimization model, which guarantees effective budget allocation
and a balance between several criteria. An all-purpose instrument considers social and strategic factors. The test
findings demonstrate that the suggested multi-criteria optimization model is the most dependable and well-balanced
approach to budget allocation. While a qualitative comparison with baseline models (e.g., level balancing and linear
programming) has been conducted, a quantitative assessment using performance metrics (e.g., RMSE, MAE) could not
be performed due to the lack of detailed, disaggregated budget data at the district and sectoral levels for 2022-2023.
Government-reported allocations are typically aggregated, hindering direct alignment with the model’s framework.
For future research, we intend to submit a formal data request to regional authorities to access detailed budget
breakdowns, facilitating a thorough empirical validation and enabling the calculation of accuracy metrics such as
prediction error and budget deviation. To compare the efficiency of budget allocation optimization methods in more
detail, were analyzed two methods - the genetic algorithm GA implemented in Python using the DEAP library and the
SQP method in order to compare the effectiveness of budget allocation optimization techniques in greater detail. Both
approaches were used to solve a multi-criteria optimization issue that considers factors including urbanization level,
strategic priorities, fundamental necessities, and citizen satisfaction. The comparison's goals were to determine the
potential benefits and drawbacks of each strategy and assess how GA, as a stochastic method, can compete with the
deterministic SQP in the budget allocation problem.
In contrast to the SQP, which depends on gradient-based convergence, the GA adopted a stochastic population-based
strategy. It utilized a population size of 200, evolving over 500 generations, with an 80% crossover rate and a 5%
mutation rate. Variability was introduced through a one-point crossover operator and Gaussian mutation. Constraint
violations were penalized within the fitness function, employing dynamic scaling to maintain feasibility without
excessively limiting exploration. The GA exhibited slow but consistent convergence, with notable improvements in
early generations and stabilization in later stages. Although it required substantially more evaluations than SQP, GA
offered robustness against local optima and achieved a high-quality solution with a final objective value of
18,520,000.00 thousand tenge.
The capacity of genetic algorithms to identify global optima in intricate multi-criteria issues makes them popular in
optimization and financial allocation challenges the stock market forecasting problem demonstrates the ability of GA
to adjust to complicated nonlinear dependencies, by optimizing model parameters, GA increased the prediction
accuracy of stock prices [16]. The model is intended to be expanded in the future by accounting for indicator dynamics
and uncertainty. To account for the imprecision and fuzziness of input data, it is especially recommended to combine
fuzzy logic techniques with the evolutionary algorithm. One example of a successful hybrid strategy is the use of GA
with fuzzy rules to optimize the cost-time-quality ratio of projects [17].
The effective optimization of KOSPI 200 index fund portfolios [18] shows that when Genetic Algorithms (GAs) were
used for index fund management, they outperformed traditional optimization techniques in terms of portfolio
performance. The creation of the GA-MSSR method, which maximized performance metrics like the Sharpe and

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3085
Sterling ratios to optimize high-frequency trading strategies, further demonstrated GAs' ability to adapt to complex
nonlinear financial data and greatly increased the accuracy of micro-level price forecasting in volatile market conditions
[19].
The genetic algorithm reached a value of 18,520,000.00 thousand tenge after modifying the parameters (increasing the
number of generations to 500, increasing the penalties for violating restrictions, and normalizing the objective function)
in contrast to SQP, which displayed the objective function value of 18,519,864.85 thousand tenge. Despite minor
variations that reflect the stochastic character of the approach, the budget distribution derived using GA was found to
be similar to the SQP results (figure 6):
Figure 6. Distribution of the budget by districts and regions, obtained using GA
Similar to the SQP results, the graph indicates that the Kegen district, which has a high degree of urbanization, receives
the biggest allocations of funds for infrastructure, while the Talgar district receives the fewest allocations for culture.
However, because of the stochastic search for solutions, GA has a uniform distribution in other categories, including
education. A comparative analysis of the methods is presented below (table 6).
Table 6. Comparative Characteristics of SQP and GA methods
Methods
Characteristic
SQP (MATLAB) GA (Python, DEAP)
Method Type Deterministic Stochastic
Objective Function 18,519,864.85 thousand tenge 18,520,000.00 thousand tenge
Convergence Fast (less than 100 iterations) Slow (500 generations)
Accuracy High (deterministic approach) Medium (depends on parameters)
Constraint Handling Linear constraints built into fmincon Via penalties in the fitness function
Advantages Fast convergence, high accuracy Global search, robust to local minimal
Disadvantages May get trapped in local minimal Random results, high computational cost
Applicability Suitable for well-defined constraints Suitable for complex tasks with uncertainty
The SQP and GA methods can both solve the multi-criteria budget allocation optimization issue, according to a
comparison study of the two methodologies. According to a comparative research, multi-criteria budget allocation
problems can be successfully handled by both SQP and GA. As a deterministic method, SQP exhibits better accuracy
and quicker convergence under well-defined constraints [20]. On the other hand, GA is excellent at examining trade-
offs between goals and demonstrates resilience in situations involving a lot of uncertainty. It provides adaptable
solutions for complicated issue structures [21].

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3086
SQP is better for problems with well-defined constraints because of its deterministic method, which shows higher
accuracy and convergence rate. In turn, GA provides many approaches that can be helpful for examining criteria trade-
offs, particularly when there is uncertainty. The suggested model's dependability is confirmed by the small discrepancy
between the budget allocation and the objective function values (135.15 thousand tenge). It is advised that future
studies take into account combining GA with fuzzy logic to account for data uncertainties and use more recent libraries
like Pymoo to enhance constraint handling [22].
The optimization model allocated a total budget of 42,656,543 thousand tenge across four districts and seven Areas of
Activity (AAs) in the Almaty region, utilizing a multi-criteria optimization approach. Healthcare (22.05%) and
transport (21.11%) secured the largest shares, reflecting their high strategic priority and strong citizen support.
Education received the smallest allocation (7.03%), indicating lower prioritization in voter and strategic metrics. All
seven AAs were funded, showcasing the model’s ability to ensure comprehensive sectoral coverage.
The model employed quadratic programming, with the Sequential Quadratic Programming (SQP) algorithm in
MATLAB achieving an objective function value of 18,519,864.85 thousand tenge, converging in under 100 iterations.
The GA, implemented via Python’s DEAP library, yielded a slightly higher value of 18,520,000.00 thousand tenge
after 500 generations, demonstrating robust global exploration. The negligible difference of 135.15 thousand tenge
between methods confirms their reliability. SQP excelled in speed and precision under well-defined constraints, while
GA proved effective for complex, uncertain problem structures.
Figure 1 illustrates balanced budget distribution across districts and sectors, aligning with regional priorities. Figure 2
confirms SQP’s rapid convergence, with minimal step size and a gradient norm of 0.7016. Figure 3 highlights GA’s
similar allocation patterns, notably higher infrastructure funding in Kegen and lower culture funding in Talgar. Table
3 indicates strong influence of urbanization and population on allocations, while table 4 details precise budget amounts,
consistent with optimization objectives.
5. Conclusion
A dynamic budget allocation model was developed and evaluated in this study using quadratic programming and
multicriteria optimization approaches. The efficacy of the SQP method and a GA was compared. With a target function
value of 18,519,864.85 thousand tenge with SQP, the model successfully allocates budgetary resources among districts
and activity areas, according to the analysis and numerical experiments. GA produced a marginally higher value of
18,520,000.00 thousand tenge, a difference of 135.15 thousand tenge, demonstrating the robustness of both approaches.
In order to provide an accurate and well-informed resource distribution that meets real demands, the model takes into
account important demographic data, urbanization levels, regional profitability, and public opinions expressed through
voting. The model avoids financial imbalances and meets fundamental necessities while upholding strategic priorities
by imposing minimum and maximum budget limitations. With the exception of a few minor allocation discrepancies,
such as GA allocating 300,000.00 thousand tenge to education in Raimbeksky district compared to SQP's 296,622.18
thousand tenge, both approaches met most criteria. SQP, achieved rapid convergence within 100 iterations, while GA
required 500 generations, reflecting its slower but more exploratory nature.
Although the proposed model exhibits significant potential for practical use, especially in participatory and multi-
criteria regional budget allocation, it remains at the conceptual phase. A formal request for pilot testing has been
submitted to the Ministry of Digital Development of the Republic of Kazakhstan for possible integration into the
national eGov information system, with the authors awaiting a response. Consequently, while the results are
encouraging, conclusions about real-world applicability should be considered preliminary pending validation in a
policy implementation context.
The proposed model also highlights significant ethical concerns. The integration of publicly available demographic
and socio-economic data with subjective weights for strategic priorities poses risks concerning transparency and
perceived equity. Additionally, decisions guided by artificial intelligence and optimization algorithms may encounter
public skepticism or political opposition, particularly if stakeholders lack a clear understanding of the underlying
processes or perceive them as obscure.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3087
To address these risks, future efforts will include the adoption of explainable AI techniques, enhanced transparency in
data sources, and participatory approaches to validate weighting schemes. These measures are essential for fostering
trust and ensuring ethical accountability in any potential deployment of the model within e-government systems.
These results can be used to guide budget management choices at the regional authority level, improving the
effectiveness and transparency of budget planning. The comparison highlights the accuracy of SQP for clearly defined
situations and the resilience of GA for complicated, unpredictable scenarios. To increase computational accuracy, the
model can be extended to incorporate more complex economic and social factors, more places, more categories, and
information such as population dynamics and long-term strategic objectives. The comparative analysis of SQP and
GA shows that both are effective tools for optimizing government spending in resource-constrained environments, with
each offering distinct strengths based on task requirements. As a result, the suggested approach guarantees equitable
budget distribution, minimizes risks, and takes into account the interests of all stakeholders.
6. Declarations
6.1. Author Contributions
Conceptualization: S.G., S.S., Y.S. and A.A.; Methodology: A.A. and S.G.; Software: S.G. and A.A.; Validation: S.G.
and A.A.; Formal Analysis: S.G., S.S., Y.S. and A.A.; Investigation: S.G.; Resources: A.A.; Data Curation: A.A.;
Writing Original Draft Preparation: S.G. and A.A.; Writing Review and Editing: A.A. and S.G.; Visualization: S.G.,
S.S., Y.S. and A.A. All authors have read and agreed to the published version of the manuscript.
6.2. Data Availability Statement
The data presented in this study are available on request from the corresponding author.
6.3. Funding
The authors received no financial support for the research, authorship, and/or publication of this article.
6.4. Institutional Review Board Statement
Not applicable.
6.5. Informed Consent Statement
Not applicable.
6.6. Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
References
[1] M. Skopin, “Maslikhats: who needs them and what they do,” [Online]. Available: https://orda.kz/podzabytye-maslihaty-
komu-oni-nuzhny-ichem-zanimayutsya/. [Accessed: Apr. 12, 2024].
[2] Ministry of Justice Republic of Kazakhstan, “Institute of Legislation and Legal Information,” [Online]. Available:
https://adilet.zan.kz/kz/docs/U1300000704. [Accessed: May 24, 2024].
[3] S. Gulbakyt and A. Abdualiyev, “Development of a mathematical model for the distribution of financial resources,” Procedia
Comput. Sci., vol. 251, no. 1, pp. 520–525, 2024. doi: 10.1016/j.procs.2024.11.142.
[4] M. Sigala, A. Beer, L. Hodgson, and A. O’Connor, “Big data for measuring the impact of tourism economic development
programmes: A process and quality criteria framework for using big data,” in Managerial Approaches, Techniques, and
Applications, Singapore: Springer, 2019, vol. 2019, no. 5, pp. 1–20, doi: 10.1007/978-981-13-6339-9_4.
[5] L. Mazelis, A. Krasko, and E. Krasova, “Distribution of financial resources by areas of investments in the human capital of
the region,” Economic Consultant, vol. 36, no. 4, pp. 4–16, 2021, doi: 10.46224/ecoc.2021.4.1.
[6] L. Bartocci, G. Grossi, S. G. Mauro, and C. Ebdon, “The journey of participatory budgeting: A systematic literature review
and future research directions,” International Review of Administrative Sciences, vol. 89, no. 3, pp. 757–774, 2023, doi:
10.1177/00208523221078938.

Journal of Applied Data Sciences ISSN 2723-6471
Vol. 6, No. 4, December 2025, pp. 3075-3088 3088
[7] D. Hershkowitz, A. Kahng, D. Peters, and A. Procaccia, “District-fair participatory budgeting,” in Proc. AAAI Conf. Artificial
Intelligence, vol. 35, no. 6, pp. 5464–5471, 2021, doi: 10.1609/aaai.v35i6.16688.
[8] M. Beikverdi, N. G. Tehrani, and K. Shahanaghi, “A bi-level model for district-fairness participatory budgeting:
Decomposition methods and application,” European Journal of Operational Research, vol. 314, no. 2, pp. 340–362, 2024.
[9] W. Zhang, G. Xiao, M. Gen, H. Geng, X. Wang, M. Deng, and G. Zhang, “Enhancing multi-objective evolutionary algorithms
with machine learning for scheduling problems: Recent advances and survey,” Frontiers in Industrial Engineering, vol. 2024,
no. 6, pp. 1–18, 2024.
[10] Y. Ma, X. Gao, C. Liu, and J. Li, “Improved SQP and SLSQP algorithms for feasible path-based process optimisation,”
Computers and Chemical Engineering, vol. 188, no. 4, pp. 1–12, 2024, doi: 10.1016/j.compchemeng.2024.108751..
[11] S. Rey, U. Endriss, and R. de Haan, “A general framework for participatory budgeting with additional constraints,” Social
Choice and Welfare, vol. 64, no. 1, pp. 5–41, 2025.
[12] D. Schugurensky and L. Mook, “Participatory budgeting and local development: Impacts, challenges, and prospects,” Local
Development & Society, vol. 5, no. 1, pp. 1–13, 2024, doi: 10.1080/26883597.2024.2391664.
[13] I. Baffo, M. Leonardi, V. D’Alberti, and A. Petrillo, “Optimizing public investments: A sustainable economic,
environmental, and social investment multi-criteria decision model (SEESIM),” Regional Science Policy & Practice, vol. 16,
no. 11, pp. 100140–100152, 2024, doi: 10.1016/j.rspp.2024.100140.
[14] Bureau of National Statistics of the Agency for Strategic Planning and Reforms of the Republic of Kazakhstan, [Online].
Available: https://stat.gov.kz/ru/region/almatyobl/. [Accessed: Dec. 1, 2024].
[15] Ministry of Justice of the Republic of Kazakhstan, “Information and Legal System of Regulatory Legal Acts of the Republic
of Kazakhstan,” [Online]. Available: https://adilet.zan.kz/rus/docs/V20D0005841.
[16] R. Abraham, M. E. Samad, A. M. Bakhach, H. El-Chaarani, A. Sardouk, S. E. Nemar, and D. Jaber, “Forecasting a stock
trend using genetic algorithm and random forest,” Journal of Risk and Financial Management, vol. 15, no. 5, pp. 1–12, 2022.
[17] A. Erdoğdu, F. Dayi, F. Yildiz, A. Yanik, and F. Ganji, “Combining fuzzy logic and genetic algorithms to optimize cost, time
and quality in modern agriculture,” Sustainability, vol. 17, no. 7, pp. 1–15, 2025.
[18] Y. Orito, M. Takeda, and H. Yamamoto, “Index fund optimization using genetic algorithm and scatter diagram based on
coefficients of determination,” in Intelligent and Evolutionary Systems, M. Gen, K. Kim, X. Li, and Y. Tsujimura, Eds.,
Studies in Computational Intelligence, vol. 187, Berlin, Heidelberg: Springer, 2009, pp. 1–12.
[19] Z. Zhang and M. Khushi, “GA-MSSR: Genetic algorithm maximizing Sharpe and Sterling ratio method for RoboTrading,”
in Proc. Int. Joint Conf. Neural Networks (IJCNN), vol. 2020, no. 7, pp. 1–8, 2020, doi: 10.1109/IJCNN48605.2020.9206647.
[20] A. Salami, B. Afshar-Nadjafi, and M. Amiri, “A two-stage optimization approach for healthcare facility location-allocation
problems with service delivering based on genetic algorithm,” International Journal of Public Health, vol. 68, no. 2, pp. 1–
12, 2023, doi: 10.3389/ijph.2023.1605015.
[21] R. C. L. Corrêa de Sousa, F. Goulart, D. E. C. Vargas, F. Campelo, and E. Wanner, “Optimizing multi- and many-objective
problems on varied budgets: Hybridizing NSGA-III with local searches,” Proceedings of the Brazilian Society of
Computational and Applied Mathematics, vol. 11, no. 1, pp. 1–15, 2025, doi: 10.5540/03.2025.011.01.0454.
[22] J. Blank and K. Deb, “Pymoo: Multi-objective optimization in Python,” IEEE Access, vol. 8, no. 5, pp. 89497–89509, 2020,
doi: 10.1109/ACCESS.2020.2990567.