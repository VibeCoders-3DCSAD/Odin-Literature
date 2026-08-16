---
conversion_metadata:
  converted_at: "2026-07-22T12:58:59Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Chowdhury T. et al.pdf"
  source_pdf_sha256: "1c744971743ae7dcf82650d46709f64de00262fadb7fc0043716f53732b3699d"
  page_count: 20
  markdown_char_count: 201830
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Computers in Human Behavior Reports 21 (2026) 100926

Contents lists available at ScienceDirect

Computers in Human Behavior Reports

journal homepage: www.sciencedirect.com/journal/computers-in-human-behavior-reports

Modeling financial literacy through explainable machine learning and 
behavioral segmentation in emerging economies

Tawhid Ahmed Chowdhury a, Md Ariful Haque Chowdhury a,*, Md Tahidur Rahman a,  
Iftakhar Ahmed b, Nabila Ahmed b, Md Azizul Islam Tuhin b, Abdulla Al Kafy c
a Department of Business Administration, Bangladesh Army International University of Science and Technology (BAIUST), Cumilla, 3501, Bangladesh
b University of Liberal Arts Bangladesh, Dhaka, Bangladesh
c Department of Urban and Regional Planning, Rajshahi University of Engineering and Technology (RUET), Rajshahi, 6204, Bangladesh

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Financial literacy
Machine learning
Behavioral segmentation
Digital inclusion
Emerging economies

Digital  financial  services are  changing  how people  behave  financially but  understanding  how  individuals use 
financial  technology  remains  limited  in  emerging  economies.  This  study  investigates  financial  literacy  and 
technology-driven financial behavior using machine learning analysis of 1067 adults in Bangladesh. Traditional 
demographic methods fail to capture the complexity of digital financial behavior, which hampers the design of 
effective interventions. By applying Random Forest, XGBoost, and k-means clustering validated with a silhouette 
score of 0.42, Davies-Bouldin Index of 1.08, and Calinski-Harabasz Index of 287.3, we achieved moderate pre-
dictive performance with an F1-score of 0.52, a 58 % improvement over random guessing, and gained important 
insights  into  technology-influenced  financial  behavior.  SHAP  analysis  identified  institutional  trust,  digital 
comfort, and income as key predictors, with trust showing an importance value of 0.18 compared to education at 
0.09, challenging typical demographic assumptions. Three distinct behavioral groups emerged: Digitally Literate 
Planners (34 % of the sample, average financial knowledge 7.8/10), Informally Active but Underskilled (41 %, 
knowledge 5.4/10), and Digitally Excluded Traditionalists (25 %, knowledge 3.1/10). Results show that rural 
users had 7.3 % higher financial literacy than urban users, while formal education did not significantly impact 
literacy  levels.  Weak  correlations  between  financial  knowledge  and  actual  behaviors,  with  coefficients  below 
0.10,  suggest  that  understanding  alone  does  not  lead  to  effective  financial  practices.  The  findings  provide 
frameworks  for  tailored  interventions  based  on  behavioral  types  instead  of  stereotypes,  including  resource 
allocation  of  60  %  for  support,  30  %  for  transitional  programs,  and  10  %  for  advanced  services,  to  improve 
intervention effectiveness for diverse users in developing economies.

1. Introduction

Financial literacy is crucial for economic well-being worldwide, but 
traditional assessment methods often overlook many of its aspects and 
fail to provide valuable insights for targeted actions (Lusardi & Messy, 
2023; Lusardi &  Streeter, 2023). People with higher financial literacy 
tend  to  achieve  better  financial  results,  including  saving  more,  man-
aging debt more effectively, preparing better for retirement, and being 
more resilient to economic shocks. As financial products become more 
complex  and  innovative,  the  ability  to  understand  financial  ideas,

compare options, and navigate systems has become crucial for economic 
participation and success. The importance of financial literacy is espe-
cially  clear  in  developing  countries,  where  rapid  digital  changes  are 
expanding access to financial services but also creating new challenges 
for people with limited experience in formal financial systems (Choung 
et al., 2023; Clark et al., 2025). Mobile banking, digital payments, and 
fintech are transforming financial environments in emerging markets; 
however,  these  technological  advances  do  not  automatically  improve 
financial skills unless they are backed by basic understanding, proper 
institutional  support,  and  user  trust  in  digital  platforms  (Widyastuti

* Corresponding author. Department of Business Administration, Bangladesh Army International University of Science and Technology (BAIUST), Cumilla, 3501,

Bangladesh.

E-mail  addresses:  tawhidchowdhury166@gmail.com (T.A.  Chowdhury),  arifcubaiust@gmail.com,  ariful.dba@baiust.ac.bd (M.A.H.  Chowdhury),  tahidur. 
ais2004@gmail.com (M.T.  Rahman),  Iftakhar92@gmail.com (I.  Ahmed),  nabila0892@gmail.com (N.  Ahmed),  md.azizulislamtuhin@gmail.com (M.A.I.  Tuhin), 
abdulla-al.kafy@localpathways.org (A.A. Kafy).

https://doi.org/10.1016/j.chbr.2025.100926
Received 25 August 2025; Received in revised form 29 December 2025; Accepted 30 December 2025  
Available online 30 December 2025 
2451-9588/© 2026 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- 
nc-nd/4.0/ ).

---

<!-- PAGE 2 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

et al., 2024; Adel, 2024). The digital financial gap is not just about access 
to  technology,  but  also  about  fundamental  gaps  in  knowledge,  skills, 
trust, and confidence needed to navigate increasingly complex financial 
systems safely and effectively (Koskelainen et al., 2023). In Bangladesh, 
where mobile financial services are rapidly growing alongside ongoing 
financial  exclusion,  understanding  the  complex  links  between  de-
mographic  traits,  digital  access,  and  financial  literacy  has  become 
crucial for shaping policy and designing effective interventions (Hossain 
et al., 2020; Khalily, 2008). Despite notable progress in adopting mobile 
financial services, significant gaps remain in individuals' ability to use 
digital financial tools effectively and securely. This issue is especially 
troubling  because  simply  having  access  to  digital  platforms  does  not 
guarantee proper usage without basic knowledge of financial concepts 
and  trust  in  institutions  (Choung  et  al.,  2023).  The  lack  of  financial 
education is even more evident in rural and semi-urban areas, where 
infrastructural  challenges  and  informational  gaps  continue  to  hinder 
financial  empowerment.  Addressing  these  issues  requires  innovative 
approaches  to  assess  financial  literacy  and  create  interventions  that 
consider  Bangladesh's  unique  socioeconomic  and  technological  envi-
ronment (Arora & Sarker, 2025; Khalily, 2008; Rabeta & Sumi, 2023).
Traditional  financial  literacy  research  in  developing  countries  has 
mainly depended on descriptive surveys and simple regression models, 
focusing mostly on demographic factors like age, education, and income 
(Zaimovic et al., 2023). These traditional methods, while offering useful 
initial  insights,  have  clear  limitations  in  capturing  the  complex, 
non-linear,  and  multidimensional  relationships  that  shape  financial 
behavior  in  fast-changing  digital  environments  (Singh  et  al.,  2020). 
Recent  research  has  started  using  machine  learning  (ML)  mod-
els—including  Random  Forest,  XGBoost,  and  LightGBM—to  improve 
prediction  accuracy,  classification,  and  understanding  of  important 
features  in  complex  socioeconomic  data  (Garson,  2021;  Imani  et  al., 
2025).  These  advanced  methods  provide  distinct  benefits  that  suit 
financial  literacy  studies  in  diverse  populations.  ML  algorithms  are 
especially  good  at  identifying  non-linear  relationships  and  threshold 
effects  in  financial  behavior,  automatically  detecting  complex  in-
teractions between variables without needing to specify every possible 
relationship  beforehand,  accommodating  population  differences 
through  natural  behavioral  segmentation,  and  offering  clear  insights 
through  explainable AI  tools  like  SHAP  values  that policymakers  and 
practitioners can easily understand and use (Jarupunphol et al., 2024; 
Yang & Xie, 2025). Research shows that combining clustering methods 
with supervised ML can greatly improve prediction accuracy in social 
science studies, and ensemble techniques like XGBoost tend to outper-
form traditional models in predicting human capital readiness in rural 
areas (Jarupunphol et al., 2024; Yang & Xie, 2025).

Theoretical frameworks surrounding financial literacy have evolved 
considerably from simple knowledge-based ideas to include behavioral 
insights and digital aspects. Instead of viewing literacy as just a binary or 
scalar variable, modern scholars see it as a multidimensional concept 
that  involves  cognitive  understanding,  behavioral  actions,  emotional 
attitudes, and the ability to adapt to different contexts (Bayakhmetova 
et al., 2025; Koskelainen et al., 2023). This view is based on behavioral 
finance  theory,  which  highlights  that  financial behavior  is  influenced 
not only by rational calculation but also by cognitive biases, heuristics, 
and  emotional  factors  that  systematically  affect  choices  even  among 
knowledgeable  people  (Chawla  et  al.,  2020;  Singh  et  al.,  2020).  The 
term “financial aliteracy” refers to situations where individuals greatly 
overestimate their financial skills, which can lead to risky or irrational 
financial decisions. This issue is especially important in digital settings 
where superficial access to tools like mobile banking apps does not al-
ways  mean  proficient  use  (Chawla  et  al.,  2020;  Clark  et  al.,  2025). 
Research  shows  that  financial  behavior  mainly  mediates  the  link  be-
tween  financial  knowledge  and  perceived  wellbeing,  highlighting  the 
need for behaviorally based measurement frameworks that go beyond 
just  testing  knowledge  (Sabri  et  al.,  2022).  The  financial  capability 
approach expands this view by defining financial wellbeing as requiring

both  ability—knowledge  and  skills—and  opportunity—access  to  suit-
able  financial  services  and  institutional  support—to  reach  desired 
financial results (Koskelainen et al., 2023; Zaimovic et al., 2023).

Comparative  research  across  various  cultural  settings  consistently 
indicates that digital financial literacy is often a more reliable predictor 
of  sound  financial  behavior  than  traditional  literacy  measures  alone 
(Choung  et  al.,  2023;  Widyastuti  et  al.,  2024).  In  Bangladesh,  where 
women's  access  to  financial  services  is  frequently  mediated  through 
family or spousal networks, understanding these dynamics is essential 
for creating truly inclusive interventions (Khalily, 2008). The sociocul-
tural and gendered aspects of financial literacy have gained increasing 
attention,  with  studies  documenting  ongoing  gender  gaps  driven  by 
complex factors such as social norms, confidence differences, and dis-
parities in educational exposure (Haag & Brahm, 2025; Roshid & Le Ha, 
2024).  Evidence  from  around  the  world  consistently  shows  a  strong 
positive link between financial literacy and better financial behaviors, 
with those possessing higher financial knowledge more likely to engage 
in  long-term  planning,  responsible  borrowing,  and  regular  savings 
(Lusardi  &  Messy,  2023;  Rabeta  &  Sumi,  2023;  Sabri  et  al.,  2022). 
Recent  studies  also  reveal  that  both  digital  and  traditional  financial 
literacy  positively  impact  financial  well-being  in  emerging  markets, 
emphasizing  the  need  for  comprehensive  literacy  assessments  that 
consider multiple aspects of financial capability (Kamble et al., 2024). 
Together,  behavioral  finance  theory  and  the  financial  capability 
approach provide the conceptual foundation for this study's clustering 
and predictive modeling strategy.

Despite expanding access to digital financial tools across Bangladesh 
and increasing recognition of financial literacy's importance, significant 
gaps  remain  in  both  understanding  and  methodological  approaches. 
Financial  literacy  is  still  underexplored  among  socioeconomically 
vulnerable  groups  in  Bangladesh  and  similar  developing  countries, 
especially affecting low-income communities, rural residents, and un-
dereducated  populations  (Hossain  et  al.,  2020;  Kamble  et  al.,  2024; 
Rabeta  &  Sumi,  2023).  Most  notably,  few  studies  have  used  ML  ap-
proaches specifically designed to address socio-demographic differences 
within  Bangladesh's  developing  economy  context.  Moreover,  existing 
research  rarely  employs  advanced  analytics  to  systematically  map 
financial literacy across behavioral groups or to offer personalized in-
sights for targeted intervention strategies. The literature does not thor-
oughly  investigate  gendered  and  rural-urban  digital  divides  using 
predictive  analytics,  which  could  help  inform  targeted  interventions 
instead of generic population-level programs. Additionally, most studies 
do  not  apply  explainable  AI  techniques  that  translate  complex  algo-
rithmic  results  into  transparent,  policy-relevant  insights  that  practi-
tioners and policymakers can effectively use in resource-limited settings. 
This  highlights  a  significant  gap,  given  the  potential  for  AI-powered 
frameworks to model financial literacy not just as an outcome variable 
but as a complex interplay of socio-economic, behavioral, and digital 
factors.

This study addresses these gaps by developing and evaluating a ML 
framework to predict financial literacy levels among Bangladeshi adults. 
It examines how socioeconomic, demographic, and behavioral factors 
influence financial capability within the context of an emerging econ-
omy characterized by diverse educational backgrounds, varying income 
levels, and differential access to digital financial services. The research 
integrates behavioral clustering with supervised ML to identify natural 
population  segments  while  ensuring  interpretability  through  SHAP 
analysis. This approach represents an innovative methodological com-
bination of unsupervised and supervised learning techniques within the 
context of financial literacy in Bangladesh. By analyzing gendered pat-
terns,  rural-urban  differences,  and  educational  effects  using  compre-
hensive  primary  data,  the  study  offers  actionable  frameworks  for 
targeted interventions based on behavioral typologies rather than de-
mographic  stereotypes.  The  theoretical  contribution  conceptualizes 
financial literacy as a dynamic, multidimensional construct shaped by 
digital behavior patterns, contextual factors, and institutional trust. This

2

---

<!-- PAGE 3 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

work  advances  perspectives  in  behavioral  finance  that  emphasize  the 
knowledge-behavior  gap  in  financial  decision-making  (Koskelainen 
et al., 2023; Zaimovic et al., 2023).

The  primary  aim  of  this  study  is  to  develop  and  systematically 
evaluate a predictive ML framework designed to assess financial literacy 
levels among adults in Bangladesh. The specific objectives encompass: 
identifying key socio-demographic and digital access variables that in-
fluence financial literacy within the Bangladeshi context through feature 
importance  analysis  and  explainable  AI  techniques;  implementing 
advanced ML models—namely, Random Forest, XGBoost, and Decision 
Tree—to classify financial literacy with superior predictive accuracy and 
interpretability  in  comparison  to  conventional  regression  methods; 
analyzing  behavioral  clusters  via  unsupervised  learning  to  identify 
distinct population segments that support targeted financial education 
initiatives beyond traditional demographic classifications; and investi-
gating the correlations between financial knowledge and actual finan-
cial behaviors to enhance both theoretical understanding and practical 
intervention  strategies. This research  makes methodological  contribu-
tions by incorporating explainable AI models in a domain traditionally 
dominated  by  static  regression  analyses  and  descriptive  survey  sum-
maries  (Garson,  2021);  conceptual  contributions  by  framing  financial 
literacy as a complex function of interconnected variables influenced by 
digital  transformation  and  institutional  contexts  (Koskelainen  et  al., 
2023;  Zaimovic  et  al.,  2023);  and  practical  contributions  by  offering 
actionable  insights  for  financial  educators,  policymakers,  and  service 
providers  aiming  to  optimize  educational  content  and  intervention 
strategies  for  Bangladesh's  diverse  population  segments  characterized 
by varying levels of formal education, digital access, and engagement 
with formal financial institutions.

2. Materials and methods

2.1. Study design and sampling

This  research  employed  a  cross-sectional,  quantitative  design 
combining primary data collection through structured surveys with ML- 
based predictive modeling to evaluate financial literacy among adults in 
Bangladesh.  The  study  was  conducted  from  March  to  June  2024  and 
targeted  adults  aged  18–60  with  access  to  digital  platforms  across 
diverse  geographic  and  socioeconomic  backgrounds.  This  approach 
improves on traditional correlation-based financial literacy studies by 
integrating robust survey methods with computational analytics to un-
cover complex, nonlinear relationships between socioeconomic factors 
and financial outcomes that standard regression models often overlook 
(Imani  et  al.,  2025;  Singh  et  al.,  2020).  The  framework  followed  a 
step-by-step  process  involving  primary  data  collection  via  online  sur-
veys,  thorough  data  preprocessing  and  feature  engineering,  develop-
ment  and  assessment  of  supervised  ML  models,  and  unsupervised 
behavioral clustering for population segmentation. This setup enables 
both predictive modeling and natural behavioral segmentation, which 
traditional  statistical  methods  often  miss,  particularly  in  the  diverse 
populations typical of developing economies (Yang & Xie, 2025). Fig. 1
presents  the  complete  methodological  workflow  outlining  key  stages 
from study design to policy implications.

A stratified random sampling technique was used with proportional 
allocation  based  on  Bangladesh's  documented  urban-rural  population 
split,  maintaining  a  45:55  urban-rural  ratio  to  ensure  representation 
across key demographic groups. The target group included adults aged 
18–60 with digital access, aligning with the focus on individuals who 
could  benefit  from  existing  and  emerging  digital  financial  services. 
Sample  size  was  determined  through  statistical  power  analysis

Fig. 1. Methodological workflow outlining key stages from study design to policy implications in the financial literacy analysis.

3

---

<!-- PAGE 4 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

conducted beforehand using G*Power 3.1 software for logistic regres-
sion with three predictor categories. The parameters included an alpha 
significance  level  of  0.05,  a  power  of  0.80,  and  a  medium  effect  size 
corresponding to an odds ratio of 1.5. This analysis showed that at least 
786 participants were needed to detect significant effects with enough 
statistical power. The actual sample of 1067 valid responses surpassed 
this  minimum  by  35.7  %,  ensuring  sufficient  power  for  multivariate 
analysis. For ML purposes, the common guideline of at least ten obser-
vations  per  predictor  variable  was  met  given  the  28  predictors  used, 
resulting in about 38 observations per variable—well above the mini-
mum—and  providing  enough  data  for  training  and  testing  models 
without overfitting concerns. The digital-only survey method was cho-
sen  for  its  practical  advantages  in  reaching  geographically  dispersed 
populations,  cost-effectiveness  within  the  research  budget,  and  its 
alignment with the study's focus on digitally accessible groups who are 
the primary users of mobile financial services. During the March–June 
2024  data  collection  period,  digital  outreach  was  the  most  feasible 
method  given  the  rising  rates  of  mobile  and  internet  use  across 
Bangladesh.  However,  this  approach  has  limitations,  such  as  digital 
exclusion,  since  the  most  financially  vulnerable  individuals  without 
reliable internet access might be underrepresented, potentially biasing 
results toward more digitally engaged groups.

2.2. Data collection and survey instrument

This  study  involved  collecting  original  primary  data  rather  than 
extracting  it  from  existing  databases  or  doing  secondary  analysis  of 
previously gathered datasets. All data was directly gathered from Ban-
gladeshi  respondents  using  a  custom-designed  survey  instrument 
administered  online  during  the  designated  study  period.  Choosing  to 
collect primary data was methodologically crucial to ensure the ques-
tions  were  suitable  for  Bangladesh's  specific  financial  environment, 
including mobile money services like bKash and Nagad, informal sav-
ings groups, and rural cooperative banking practices. Data quality was 
preserved  through  multiple  validation  steps,  such  as  response  time 
monitoring with surveys completed in less than 8 min flagged for re-
view,  attention  check  questions  embedded  throughout  the  survey, 
logical consistency checks comparing related responses, and IP address 
verification  to  prevent  duplicate  submissions.  The  questionnaire  was 
created  specifically  for  this  research,  guided  by  the  internationally 
recognized OECD/INFE financial literacy assessment framework, while 
extensively  adapting  content  to  match  Bangladesh's  unique  financial 
context  (OECD,  2022).  The  final  survey  included  30  items  across  six 
domains:  demographics  (6  items  including  age,  gender,  education, 
employment, income, location), digital access and usage (5 items such as 
smartphone  ownership,  internet  connectivity,  mobile  banking  apps, 
payment  frequency,  trust),  financial  knowledge  (10  items  on  interest 
calculations, inflation, risk diversification, investment basics, insurance 
fundamentals),  behavioral  traits  (4  items  regarding  savings  habits, 
budgeting,  borrowing,  planning),  attitudinal  dimensions  (3  items  on 
decision  confidence,  institutional  trust,  perceived  security),  and 
resource access (2 items about financial education sources and advice 
availability). The instrument was thoroughly validated through internal 
reliability checks using Cronbach's alpha for all subdomains, with results 
showing excellent consistency above 0.82, construct validity confirmed 
through  exploratory  factor  analysis  with  proper  factor  loadings,  pilot 
testing  with  30  participants  representing  diverse  demographics,  and 
expert  review  by  financial  literacy  researchers  and  practitioners  in 
Bangladesh (Garson, 2021; Koskelainen et al., 2023).

2.3. Data preprocessing and variable operationalization

Prior  to  model  development,  the  collected  dataset  underwent 
comprehensive  preprocessing  procedures  designed  to  ensure  optimal 
data  quality  for  ML  applications.  All  categorical  features  were  trans-
formed  using  one-hot  encoding,  and  numerical  variables  were

normalized using Min-Max scaling (0–1 range) to ensure comparability 
across measurement units. Missing data were minimal across the data-
set,  affecting  less  than  1.2  %  of  total  responses,  and  were  addressed 
using median imputation for numerical variables and mode imputation 
for  categorical  variables.  Feature  engineering  played  a  vital  role  in 
enhancing the predictive capacity of ML models by capturing intricate 
relationships that extend beyond simple variable effects. Several inter-
action  terms  were  developed  based  on  Bangladesh-specific  financial 
behavior patterns: income × digital access (technology adoption across 
economic strata), education × age (generational differences in financial 
capability),  gender  × household  decision-making  roles  (cultural  in-
fluences  on  financial  authority),  and  urban-rural  residence  × digital 
comfort (geographic variations in technology adoption). The dependent 
variable,  financial  literacy  level,  was  operationalized  through  a  com-
posite  scoring  approach  integrating  multiple  assessment  dimensions 
(Lusardi & Streeter, 2023; Sabri et al., 2022). The composite score was 
derived  from  ten  core  assessment  items  reflecting  three  pivotal  di-
mensions: objective financial knowledge, including interest calculation 
skills,  inflation  comprehension,  and  risk  diversification  concepts; 
applied financial behaviors, such as budgeting practices, saving habits, 
and 
financial 
decision-making  capabilities,  including  investment  choices  and  insur-
ance  utilization  patterns.  Individual  item  scores  were  weighted  in 
accordance  with  established  financial  literacy  assessment  protocols 
based on OECD guidelines, with scores aggregated to produce compre-
hensive literacy scores ranging from 0 to 10 (OECD, 2022). These scores 
were subsequently classified into three ordinal categories—Low, Mod-
erate,  and  High  literacy—using  tertile-based  classification  to  ensure 
balanced  class  representation  for  ML  applications,  yielding  approxi-
mately 33 % classified as Low literacy, 52 % as Moderate literacy, and 
15 % as High literacy.

decision-making

borrowing

processes;

and

2.4. ML model development

Three  supervised  learning  classifiers  were  strategically  selected 
based  on  empirical  benchmarking  studies  in  financial  behavior 
modeling: Random Forest, XGBoost, and Decision Tree. The criteria for 
model  selection  prioritized  predictive  accuracy  and  F1-score,  which 
balances  precision  and  recall,  particularly  important  for  imbalanced 
datasets.  Model  interpretability  was  also  a  key  consideration,  as  it  is 
crucial  for  policy-relevant  applications  (Garson,  2021;  Kelly  &  Xiu, 
2023). Random Forest was chosen for its robust handling of categorical 
variables,  resistance  to  overfitting  through  ensemble  averaging,  and 
ability  to  provide  reliable  feature  importance  rankings  (Suarez-Lledo 
and  Alvarez-Galvez,  2019).  XGBoost  was  included  based  on  research 
demonstrating  its  superior  performance  in  predicting  human  capital 
readiness in  rural communities  and  other socioeconomic  outcomes  in 
developing  countries  (Jarupunphol  et  al.,  2024).  Decision  Tree  was 
incorporated to provide high interpretability through transparent deci-
sion rules that policymakers can easily understand and implement.

The dataset was systematically divided using stratified sampling into 
a training set comprising 70 % of the data, a validation set comprising 
10 % of the data for hyperparameter tuning, and a testing set comprising 
20 % of the data reserved for the final unbiased performance evaluation. 
Stratified  sampling  ensured  that  the  class  distribution  was  preserved 
across all three partitions. Hyperparameter optimization was conducted 
through  a  comprehensive  grid  search  combined  with  5-fold  cross- 
validation  to  identify  optimal  configurations  while  preventing  over-
fitting. For Random Forest, the grid search explored n_estimators values 
of 100, 200, and 300; max_depth values of 10, 20, 30, and None; and 
min_samples_split  values  of  2,  5,  and  10.  For  XGBoost,  explored  pa-
rameters included learning_rate values of 0.01, 0.05, and 0.1; max_depth 
values of 3, 5, and 7; and n_estimators values of 100, 200, and 300. For 
Decision Tree, max_depths of 5, 10, 15, and 20 were evaluated, along 
with min_samples_split values of 2, 5, 10, and 20.

Class  imbalance,  particularly  the  underrepresentation  of  high-

4

---

<!-- PAGE 5 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

literacy individuals at 15 % of the sample, was systematically addressed 
through resampling techniques applied exclusively to the training data. 
Synthetic Minority Over-sampling Technique (SMOTE) was employed to 
generate  synthetic  examples  of  minority  classes  by  interpolating  be-
tween existing minority class observations in feature space (Imani et al., 
2025).  Additionally,  Adaptive  Synthetic  (ADASYN)  sampling  was 
applied,  which  generates  synthetic  samples  with  density  distribution 
according to learning difficulty. These techniques improved class bal-
ance in the training set to approximately 30-40-30 distribution across 
low, moderate, and high literacy classes, while maintaining the original 
test set distribution for realistic performance evaluation.

Feature  importance  analysis  utilized  both  traditional  Gini  impor-
tance  metrics  provided  by  tree-based  algorithms  and  SHAP  (SHapley 
Additive  exPlanations)  values  to  provide  complementary  perspectives 
on feature contributions (Crompton and Burke, 2023). SHAP analysis, 
grounded in cooperative game theory, assigns each feature an impor-
tance  value  for  individual  predictions  by  calculating  the  marginal 
contribution  of  each  feature  across  all  possible  feature  combinations. 
SHAP  visualizations  included  summary  plots  showing  global  feature 
importance  rankings,  dependence  plots  illustrating  relationships  be-
tween  individual  features  and  predictions,  interaction  plots  revealing 
compound  effects  between  variable  pairs,  and  force  plots  explaining 
individual predictions. This explainability framework transformed ab-
stract algorithmic outputs into concrete, actionable insights regarding 
determinants of financial literacy.

2.5. Behavioral clustering analysis

Unsupervised learning utilizing k-means clustering was employed to 
identify natural population segments based on behavioral patterns and 
financial characteristics rather than predefined demographic categories. 
The optimal number of clusters was determined through three comple-
mentary  approaches. Firstly, the  elbow  method  examined the  within- 
cluster sum of squares (WCSS) across k values from 2 to 8, identifying 
the point where the marginal reduction in WCSS diminishes. Secondly, 
silhouette  analysis  evaluated  cluster  cohesion  and  separation  by 
measuring the similarity of each observation to its own cluster compared 
to  other  clusters.  Thirdly,  the  gap  statistic  compared  within-cluster 
dispersion  to  the  expected  values  under  a  null  distribution  of  data 
with no inherent clustering structure. These three methods converged on 
k equals 3 as the optimal choice, supported by a silhouette score of 0.42, 
indicating reasonable cluster separation, where values above 0.4 suggest 
meaningful  structure.  Additionally,  the  Davies-Bouldin  Index  of  1.08 
indicates good clustering quality, as lower values below 1.5 are deemed 
acceptable, while the Calinski-Harabasz Index of 287.3 signifies well- 
defined  clusters,  with  higher  values  reflecting  greater  separation 
among them.

K-means  implementation  employed  the  k-means++ initialization 
algorithm to optimize centroid selection, which probabilistically choo-
ses  initial  centroids  that  are  distant  from  each  other  to  enhance 
convergence speed and solution quality. The algorithm was configured 
with a maximum of 300 iterations, a convergence criterion of 1e-4 based 
on  centroid  movement  threshold,  and  10  random  initializations  with 
different starting points to ensure the identification of the global opti-
mum.  Hierarchical  clustering  with  Ward  linkage  was  conducted  as  a 
validation  step,  producing  dendrograms  that  corroborated  similar 
segment  structures  with  three-cluster  solutions  demonstrating  clear 
separation.  Principal  Component  Analysis  (PCA)  was  subsequently 
applied to the clustered data, reducing dimensionality while maintain-
ing  85  %  of  the  variance,  thereby  facilitating  visualization  of  cluster 
separation in two-dimensional space and confirming distinct population 
segments.

2.6. Model evaluation and ethical considerations

The performance of the model was assessed using multiple metrics

appropriate  for  multi-class  classification  problems.  Overall  accuracy 
determined  the  proportion  of  correct  classifications  across  all  classes. 
Precision, recall, and F1-score were computed for each class individually 
and subsequently macro-averaged across classes to assign equal signif-
icance to each category, irrespective of sample size. The F1-score sig-
nifies  the  harmonic  mean  of  precision  and  recall,  offering  a  singular 
metric that balances these concerns and proves especially valuable for 
datasets  exhibiting  class  imbalance.  The  Area  Under  the  Receiver 
Operating Characteristic Curve (AUC-ROC) was calculated employing a 
one-vs-rest  approach suitable  for  multi-class  problems,  measuring the 
model's capability to distinguish between classes across various decision 
thresholds. Confusion matrices provided detailed insights into misclas-
sification  patterns,  indicating  which  classes  were  most  frequently 
confused. All aforementioned performance metrics were derived from 
the held-out test set, which was excluded from the model training and 
hyperparameter tuning processes, thereby ensuring an unbiased evalu-
ation of the model's generalization capacity.

Prior to data collection, comprehensive ethical clearance was gran-
ted  by  the  Bangladesh  Army  International  University  of  Science  and 
Technology  Ethics  Review  Board  under  approval  number  2024-0102. 
Participation  was  entirely  voluntary,  with  no  remuneration  or  in-
centives  offered.  Digital  informed  consent  was  obtained  from  all  re-
spondents at the survey's outset, including explicit explanations of the 
study's purpose, data utilization, confidentiality measures, and the right 
to  withdraw.  Data  anonymization  procedures  were  implemented  to 
ensure that no personally identifiable information was retained within 
the analytical dataset. All survey responses were assigned anonymous 
identification codes, with any identifiable data promptly separated from 
response  data  and  destroyed  following  data  collection.  Results  were 
reported in aggregate form, with minimum cell sizes of ten observations 
to  prevent  individual  identification.  Data  security  was  maintained 
through  encrypted  storage,  with  access  limited  solely  to  authorized 
members of the research team.

3. Results

The results explore financial literacy patterns, modeling results, and 
behavioral segments from 1067 responses in Bangladesh. They aim to 
map literacy across demographics, identify predictors via ML, classify 
behavioral groups, and examine links between demographics and liter-
acy. The findings challenge assumptions and offer insights for targeted 
interventions. The sample was 53 % male and 47 % female, reflecting 
Bangladesh's demographics and cultural factors affecting participation.

3.1. Financial literacy distributions across demographic groups

The  geographic  analysis  revealed  counterintuitive  patterns  chal-
lenging  urban-centric  policy  assumptions.  Fig.  2 shows  rural  partici-
pants marginally surpassed urban residents in financial literacy (rural 
mean: 5.73; urban mean: 5.34). Although this difference was not sta-
tistically  significant  (F(1,  1065)  = 2.31,  p  = 0.13,  η2  = 0.002),  the 
consistent  pattern  suggests  that  informal  financial  knowledge  trans-
mission  in  rural  communities—through  cooperative  savings  groups, 
agricultural  credit  associations,  and 
traditional  financial  net-
works—may  be  more  effective  than  previously  acknowledged.  This 
finding  indicates  that  policy  interventions  should  recognize  existing 
informal  financial  capabilities  rather  than  presuming  knowledge 
deficiencies.

Educational  attainment  analysis  revealed  patterns  that  complicate 
traditional human capital theories. Figs. 3 and 4 show financial literacy 
score distributions across educational levels. No significant differences 
emerged in average scores (primary: 5.48, SD = 1.82; secondary: 5.52, 
SD  = 1.76;  higher  secondary:  5.61,  SD  = 1.79;  graduate:  5.68,  SD  =
1.73;  F(3,  1063)  = 0.74,  p  = 0.59,  η2  = 0.002).  However,  higher 
educational attainment was associated with more consistent scores, with 
the  interquartile  range  narrowing  from  3.2  points  (primary)  to  2.1

5

---

<!-- PAGE 6 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

compared to means of 5.23 (SD = 1.91) for primary education, 5.41 (SD 
= 1.82) for secondary education, and 5.68 (SD = 1.76) for higher sec-
ondary education. Two-way ANOVA confirmed a significant interaction 
effect for women (F(3, 499) = 4.83, p = 0.003, η2 = 0.028), suggesting 
that women derive greater financial literacy benefits from tertiary ed-
ucation compared to lower educational levels. This pattern may reflect 
cultural factors that limit women's access to informal financial learning 
opportunities,  making  formal  education  a  more  critical  pathway  for 
female financial capability development. In contrast, male participants 
displayed relatively consistent literacy performance across all education 
levels, with means ranging from 5.62 (SD = 1.75) for primary education 
to  5.74  (SD  = 1.71)  for  graduate  education,  showing  no  statistically 
significant  variation  (F(3,  562)  = 0.91,  p  = 0.44,  η2  = 0.005).  This 
pattern  indicates  that  men  may  acquire  financial  knowledge  through 
diverse  pathways  beyond  formal  education,  possibly  including  work-
place  exposure,  business  activities,  and  social  networks  that  provide 
financial  learning  opportunities  regardless  of  educational  credentials. 
The gender-education interactions revealed in Fig. 5 highlight the need 
for  differentiated  intervention  approaches  that  account  for  varying 
pathways to financial literacy development.

3.2. Relationships between financial knowledge, behavior, and 
demographics

Correlation analysis between financial knowledge assessments and 
behavioral  indicators  revealed  weak  associations  that  challenge  con-
ventional assumptions about the relationship between knowledge and 
behavior in financial literacy research and program development. Fig. 6
shows  a  comprehensive  correlation  matrix  indicating  that  the  ten 
financial  knowledge  questions—covering  topics  like  interest  calcula-
tions,  inflation  understanding,  risk  diversification,  investment  basics, 
borrowing decisions, insurance concepts, budgeting principles, savings 
strategies, emergency planning, and retirement preparation—exhibited 
weak individual correlations with behavioral indicators such as actual 
savings  practices,  budgeting  behaviors,  and  emergency  fund  manage-
ment. The absolute  values of  the correlation  coefficients ranged  from 
0.02 to 0.09, with none reaching statistical significance at the 0.05 level.

Fig. 2. Financial literacy scores by region.

points  (graduate  education).  This  suggests  education  may  influence 
consistency  of  financial  knowledge  application  rather  than  overall 
capability, and that practical financial knowledge in Bangladesh may be 
acquired  through  multiple  pathways,  including  family  transmission, 
community networks, and workplace experience.

Gender-education interaction analysis revealed more nuanced pat-
terns  that  inform  targeted  intervention  design  and  highlight  the 
complexity  of demographic influences on financial literacy outcomes. 
Fig.  5 presents  a  rose  diagram  illustrating  these  interaction  effects, 
demonstrating that among female respondents, financial literacy scores 
peaked at the graduate education level with a mean of 6.12 (SD = 1.54),

Fig. 3. Literacy distribution by education level with no significant differences.

6

---

<!-- PAGE 7 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 4. Density of literacy scores across education groups.

Fig. 5. Gender–education interaction effects on financial literacy.

This  suggests  that  having  theoretical  financial  knowledge  does  not 
automatically lead to practical financial actions, supporting views that 
highlight  the  importance  of  experiential  learning,  behavioral  rein-
forcement, and contextual factors in financial education programs. The 
strongest relationships appeared between investment confidence mea-
sures  and  specific  knowledge  questions  about  risk  assessment  and 
diversification principles, with a correlation coefficient of 0.23 (95 % CI 
[0.17, 0.29], p < 0.001). This indicates partial alignment between un-
derstanding and confidence in specific financial areas. Still, these cor-
relations  are  modest,  implying  that  confidence  in  financial  decision- 
making  is  influenced  by  factors  beyond  simply  acquiring  knowledge, 
such as prior experience with financial institutions, social support net-
works, cultural attitudes toward risk, and perceived access to reliable 
financial services.

Fig. 7 delineates the demographic similarity analysis, offering valu-
able insights into the relative significance of various personal charac-
teristics in predicting financial literacy outcomes. The analysis reveals 
that education level and employment status exhibit the highest associ-
ations with financial literacy classification, each with similarity scores of 
approximately  36.86  %,  thereby  affirming  their  relevance.  However,

these relationships are moderate rather than deterministic. Age recorded 
a similarity score of 24.32 %, and marital status 18.47 %, suggesting 
moderate influence levels and emphasizing the importance of consid-
ering life stage contexts and family responsibilities within financial lit-
eracy  initiatives,  rather  than  relying  solely  on  static  demographic 
attributes. Gender demonstrated the lowest similarity score at 12.15 %, 
indicating minimal direct association with literacy outcomes when other 
factors  are  controlled.  The  analysis  underscores  that  multiple  factors 
collectively influence financial literacy outcomes, with no singular de-
mographic  characteristic  emerging  as  a  dependable  predictor.  Addi-
tionally, the combined effect of various demographic variables accounts 
for only a moderate proportion of variance in literacy classifications.

Fig.  8 depicts  the  intricate  relationship  between  age  and  monthly 
income through a hexbin scatter plot that illustrates clustering patterns 
with significant implications for targeting financial inclusion initiatives. 
While the overall Pearson correlation between age and income was weak 
(r = 0.01, p = 0.89), the visualization exposes distinct clustering pat-
terns  among  individuals  aged  25–45  earning  between  20,000–30,000 
Bangladeshi Taka monthly, with this cluster comprising approximately 
38  %  of  the  total  sample.  These  income-age  clusters  may  represent

7

---

<!-- PAGE 8 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 6. Correlation matrix of knowledge and behavior indicators.

Bangladesh's emerging working-class segment, whose financial literacy 
development  is  likely  influenced  by  factors  such  as  access  to  digital 
technology, employment stability, exposure to formal financial services 
through  workplace  benefits,  and  integration  within  urban  banking 
infrastructure. The clustering patterns indicate that age-income combi-
nations may provide more insightful information for targeting purposes 
than  either  variable  alone,  thereby  presenting  opportunities  for  the 
development  of  segment-specific  interventions  that  consider  the  joint 
distribution of these demographic attributes.

3.3. ML model performance and feature importance

Three  supervised  learning  models—Random  Forest,  XGBoost,  and 
Decision  Tree—were  systematically  trained  and  evaluated  to  predict 
financial literacy classifications. Performance assessment was conducted 
on an independent holdout test set comprising 20 % of the sample to 
ensure an unbiased evaluation of their generalization capabilities. Fig. 9
shows comprehensive performance metrics across all three classifiers, 
with XGBoost achieving superior overall performance F1-score of 0.52 
and an AUC-ROC of 0.527—marginally outperforming Random Forest, 
which had F1-score of 0.50 and an AUC-ROC of 0.514, and significantly 
outperforming Decision Tree, which had F1-score of 0.47 and an AUC- 
ROC of 0.496. Overall accuracy ranged from 51 % for Decision Tree to 
54  %  for  XGBoost.  Although  these  performance  levels  seem  modest, 
context is important: XGBoost's F1-score represents a 58 % improvement 
over random classification baseline (0.33), class imbalance (High liter-
acy:  15  %)  poses  inherent  prediction  challenges,  and  social  science

behavioral prediction typically yields F1-scores between 0.45 and 0.65. 
Beyond predictive accuracy, these models are valuable for identifying 
feature  relationships  and  offering  interpretable  insights  for  policy 
development.

Fig.  10 shows  confusion  matrix  analysis  for  the  Random  Forest 
model,  highlighting  challenges  in  classifying  individuals  across  three 
literacy  categories.  The  model  achieved  53  %  accuracy  for  Moderate 
literacy, likely due to larger sample size and clearer traits. Low literacy 
accuracy  was  47  %,  while  High  literacy  was  only  10  %.  The  matrix 
shows  62  %  of  actual  High  literacy  individuals  were  misclassified  as 
Moderate,  indicating  difficulty  distinguishing  them  with  current  vari-
ables. Similarly, 38 % of Low literacy were misclassified as Moderate. 
These patterns suggest the difficulty in identifying high literacy may be 
due  to  its  rarity,  subtle  differences  requiring  better  measurement,  or 
unmeasured  variables.  Improving  methods  could  involve  ensemble 
strategies,  cost-sensitive  learning,  or  feature  engineering  to  better 
discriminate the High literacy category.

Fig. 11 presents SHAP analysis providing crucial insights into feature 
importance. Monthly income emerged as the strongest predictor (SHAP: 
0.31),  followed  by  trust  in  banking  institutions  (0.18),  age  (0.14), 
sources of financial education (0.12), and digital comfort (0.11). Edu-
cation level showed limited importance (0.09), reaffirming that formal 
education  plays  a  surprisingly  limited  predictive  role,  while  gender 
exhibited  minimal  direct  capacity  (0.06).  The  prominence  of  institu-
tional  trust  as  the  second-strongest  predictor  underscores  the  impor-
tance of cultivating confidence in formal financial systems, suggesting 
that  enhancing  banking  accessibility  and  institutional  transparency

8

---

<!-- PAGE 9 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 7. Demographic similarity scores relative to literacy classification.

could substantially advance literacy outcomes.

individuals  with  very  high

Fig. 12 illustrates the interaction analysis among age, income, and 
predicted  literacy  through  a  three-dimensional  visualization,  which 
unveils complex relationships with significant implications for targeting 
strategies.  The  analysis  indicates  that  individuals  aged  35–50  with 
moderate  income  levels  (20,000–30,000  BDT  monthly)  exhibit  the 
highest  predicted  literacy  probabilities,  exceeding  0.65  for  this  de-
mographic  segment.  Conversely,  younger  individuals  under  30  with 
lower incomes below 15,000 BDT monthly demonstrate predicted lit-
eracy  probabilities below 0.35, indicating higher risks of low literacy 
classification.  Middle-aged 
incomes 
exceeding  40,000  BDT  also  display  elevated  literacy  predictions,  sur-
passing  0.60.  This  pattern  likely  reflects  various  underlying  factors, 
including limited financial exposure among young adults who have had 
fewer opportunities to acquire practical experience, restricted access to 
digital  financial  services  due  to  economic  constraints  that  hinder 
meaningful engagement with formal financial systems, fewer opportu-
nities for practical financial experience among younger populations who 
have  yet  to  navigate  major  life  financial  decisions,  and  potential 
exclusion  from  formal  financial  systems  that  offer  learning  opportu-
nities. The interactions between age and income suggest the necessity 
for targeted interventions that address both economic limitations and 
experiential  learning  opportunities  for  younger,  economically  disad-
vantaged demographic segments.

3.4. Behavioral segmentation and population clustering

Unsupervised  learning  techniques,  including  K-Means  clustering, 
effectively  identified  three  coherent  behavioral  segments  within  the

population of Bangladesh, thereby offering actionable frameworks for 
the design of targeted interventions. The clustering analysis was vali-
dated through multiple metrics: a silhouette score of 0.42, indicating a 
reasonable  degree  of  cluster  separation,  as  values  above  0.4  suggest 
meaningful  structural  delineation;  a  Davies-Bouldin  Index  of  1.08, 
indicating  good  clustering  quality,  with  lower  values  representing 
better-defined  clusters;  and  a  Calinski-Harabasz  Index  of  287.3, 
demonstrating  well-defined  clusters,  with  higher  values  indicating 
greater separation between clusters relative to within-cluster dispersion. 
Fig.  13 presents  comprehensive  behavioral  profiles  across  the  three 
identified  clusters,  revealing  distinct  patterns  in  financial  behaviors, 
digital  engagement,  and  institutional  relationships,  rather  than  tradi-
tional demographic categories. Fig. 14 complements these profiles by 
comparing  behavioral  strengths  across  clusters,  highlighting  relative 
capabilities  in  savings,  digital  engagement,  and  formal  banking 
utilization.

Cluster 1, called “Informally Active but Underskilled,” makes up 41 
% of participants (n = 437). It shows a mixed profile—strong in budg-
eting but weaker in emergency preparedness, formal financial services, 
and  advanced  planning.  As  shown  in  Fig.  14,  this  group  has  a  72  % 
budgeting  rate,  but  only  31  %  maintain  emergency  funds.  Digital 
banking usage is at 56 %, with 68 % feeling uncomfortable with digital 
tools. Formal banking use stands at 43 %, and their average financial 
knowledge  score  is  5.4  out  of  10  (SD  = 1.6).  Interestingly,  67  % 
participate in informal savings groups like samitis or ROSCAs, and 81 % 
mainly rely on family advice for financial decisions, highlighting strong 
informal networks. Demographically, 48 % have secondary education, 
58 % live in rural areas, and the average age is 34 years (SD = 9.1). The 
average monthly income is 22,000 BDT (SD = 8600), about the national

9

---

<!-- PAGE 10 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 8. Age–income distribution of respondents with clustered density.

Fig. 9. Model performance metrics across three classifiers.

median.  This  group  demonstrates  practical  skills  through  community 
networks and traditional systems but could benefit from support to ac-
cess and use formal financial services and digital platforms effectively. 
It's a transitional group that would thrive with bridge programs linking 
informal  practices  to  formal  services,  simple  digital  tools  with  good 
support,  and  community-based  financial  education  respecting  and 
building on existing strengths.

Cluster 2, known as “Digitally Excluded Traditionalists,” includes 25

%  of  respondents  (n  = 267)  and  faces  some  significant  challenges  in 
various areas of financial capability, as shown in Fig. 14. This group has 
a savings rate of just 28 %, a mean financial knowledge score of 3.1 out 
of 10 (SD = 1.8), which is well below the overall average. Their emer-
gency fund maintenance stands at 19 %, digital banking usage is only 15 
%,  and  a  large  89  %  report  feeling  only  minimally  comfortable  with 
digital tools. Ownership of formal banking accounts is at 21 %, with just 
12  %  using  these  accounts  regularly.  Their  average  trust  score  in

10

---

<!-- PAGE 11 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 10. Misclassification patterns by literacy level.

institutions is 1.9 out of 5, indicating some level of mistrust or skepti-
cism  towards  formal  financial  institutions.  Despite  these  hurdles,  this 
group relies heavily on informal financial channels: 73 % borrow from 
informal lenders, 58 % rely solely on cash transactions, 91 % receive 
financial support from family during tough times, and 65 % depend on 
community  reciprocity  systems.  Demographically,  this  cluster  mostly 
consists  of  individuals  with  primary  education  or  less  (78  %),  many 
living in rural areas (78 %), with an average age of 42 years (SD = 10.8). 
Their  average  monthly  income  is  15,000  BDT  (SD  = 6200),  which  is 
below  the  national  median.  To  support  this  group,  targeted  in-
terventions that combine basic financial education with digital literacy 
development are essential. These efforts can help them better integrate 
into the growing formal financial services and digital payment systems. 
Yet, it's equally important to recognize and respect their resilience-many 
rely  on  strong  family  bonds  and  community  networks-so  these  tradi-
tional  strengths  should  be  incorporated  into  intervention  strategies 
rather than replaced.

Fig. 15 illustrates a Principal Component Analysis (PCA) visualiza-
tion  of  three  behavioral  clusters  within  a  reduced  two-dimensional 
space,  confirming  their  distinctiveness  while  indicating  some  overlap 
between  Clusters  1  and  2,  which  suggests  partial  behavioral  conver-
gence. The initial two principal components account for 68 % of the total 
variance: PC1, explaining 42 % of the variance, predominantly reflects 
digital engagement and integration into formal financial systems; PC2, 
capturing  26  %  of  the  variance,  pertains  to  financial  knowledge  and 
planning sophistication. The pronounced separation of Cluster 0 from 
the other segments in the upper-right quadrant affirms its classification 
as  a  distinct  behavioral  type  with  substantially  different  intervention 
requirements and market opportunities. The overlap observed between 
Clusters 1 and 2 in the middle-left region may be attributable to shared 
educational  backgrounds,  geographic  characteristics,  cultural  in-
fluences,  or  transitional  states  wherein  individuals  evolve  between 
behavioral  patterns  over  time.  This  visualization  offers  significant  in-
sights  for  program  development,  indicating  that  interventions  should 
consider potential movement between segments and facilitate pathways

for  progression  from  lower  to  higher  capability  clusters,  rather  than 
perceiving segments as permanently fixed categories.

Table 1 presents comprehensive behavioral profiles and intervention 
recommendations  for  each  of  the  three  clusters,  synthesizing  de-
mographic characteristics, financial behaviors, digital engagement pat-
terns,  and  institutional  relationships  alongside  specific  intervention 
strategies,  delivery  channels,  resource  allocation  guidance,  and  ex-
pected timelines for capability development. The clustering analysis has 
important implications for financial service providers and policymakers. 
Cluster 0 represents a market-ready segment that could adopt sophisti-
cated financial products and services with minimal educational support. 
Cluster 1 represents a bridge segment that requires targeted support to 
transition  from  informal  to  formal  financial  systems  but  possesses 
foundational capabilities that facilitate this transition. Cluster 2 repre-
sents a development priority requiring comprehensive support but also 
significant potential for impact through well-designed interventions.

3.5. Financial pathway analysis and behavioral flow patterns

Sankey  diagram  analysis  revealed  multi-step  pathways  linking 
location, education, and financial literacy to outcomes like emergency 
fund ownership and savings frequency. Fig. 16 shows that rural residents 
have higher emergency fund rates (34 %) than urban residents (28 %), 
challenging  assumptions  about  rural  financial  vulnerability.  Among 
highly literate rural residents, 67 % maintain emergency funds versus 
52  %  of  urban  counterparts.  This  suggests  rural  networks  and 
community-based  mechanisms  may  be  more  effective  for  emergency 
preparedness than urban financial services. The rural advantage likely 
stems  from  stronger  community  support  (78  %  vs.  54  %),  income 
volatility, cultural emphasis on security, and informal insurance outside 
formal systems.

Fig. 17 shows pathways from formal education to literacy and sav-
ings, confirming high financial literacy often follows graduate education 
and links with active savings. Among those with graduate education, 58 
% have high or moderate literacy versus 42 % with primary education.

11

---

<!-- PAGE 12 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 11. Top predictors of financial literacy from SHAP analysis.

Also, 72 % of graduates save monthly or more, compared to 48 % with 
primary education. However, some with limited education develop good 
savings  habits  through  alternative  pathways,  with  23  %  of  primary- 
educated being high literacy and saving 68 % monthly, similar to 71 
%  among  graduate  moderate  literacy  individuals.  These  pathways 
highlight  multiple  routes  to  financial  capability,  suggesting  in-
terventions should cater to diverse learning approaches. Figs. 16 and 17
provide  frameworks  for  designing  targeted  support  to  boost  financial 
capability. Table 2 summarizes the seven key findings from this analysis, 
including  statistical  evidence  and  implications  for  policy  design  and 
intervention strategies. The table offers an integrated view of how de-
mographic  patterns,  knowledge-behavior  links,  predictive  modeling 
insights, and behavioral segmentation work together to inform targeted 
intervention strategies for Bangladesh's diverse population segments.

4. Discussion

4.1. Reconsidering demographic assumptions in financial literacy

The lack of significant differences across demographic groups chal-
lenges assumptions about financial literacy determinants. While inter-
national studies emphasize education, urban residence, and male gender 
as  key  factors  (Lusardi  &  Messy,  2023;  Zaimovic  et  al.,  2023),  our

12

findings in Bangladesh show more complex patterns. Rural respondents 
scored slightly higher, with rural scores 7.3 % above urban, though not 
statistically significant, and minimal gender disparities suggest informal 
financial learning plays a bigger role than assumed. Community-based 
initiatives, informal  savings groups, and  local financial practices  may 
provide practical education, especially in rural areas with stronger social 
capital—78  %  of  rural  residents  reported  reliable  support  during 
financial emergencies versus 54 % in urban areas—and seasonal income 
management  needs.  These  practices  include  rotating  savings  and 
informal  insurance.  However,  since  data  collection  was  digital-only, 
marginalized populations without internet access may be underrepre-
sented, potentially biasing results. The minimal impact of formal edu-
cation on financial literacy, with ANOVA results showing no significant 
differences  across  levels  and  effect  sizes  of  only  0.2  %,  challenges 
traditional human capital theories (Bayakhmetova et al., 2025; Koske-
lainen  et  al.,  2023).  This  aligns  with  behavioral  finance,  which  em-
phasizes that knowledge doesn't automatically lead to effective financial 
behavior, highlighting that interventions focusing solely on knowledge 
may  have  limited  impact  (Sabri  et  al.,  2022).  The  findings  support 
experiential 
over 
classroom-based instruction. Density distributions indicate higher edu-
cation correlates with more consistent literacy, suggesting formal edu-
influences  knowledge  application  reliability  rather  than 
cation

reinforcement

behavioral

learning

and

---

<!-- PAGE 13 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 12. Interaction effects of age and income on predicted literacy.

Fig. 13. Financial behavior profiles across respondent clusters.

capability  alone.  Educational  efforts  should  focus  on  developing 
consistent  application  through  practice and  feedback,  not just knowl-
edge acquisition.

4.2. The knowledge-behavior gap and behavioral economics insights

Weak correlations between financial knowledge and behavior, with 
coefficients below 0.10 and no significance, highlight a key finding with 
implications  for  financial  education  based  on  behavioral  economics. 
This reflects bounded rationality—people make decisions with limited

13

---

<!-- PAGE 14 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 14. Behavioral strengths comparison across clusters.

Fig. 15. Principal component view of behavioral clusters.

14

---

<!-- PAGE 15 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Table 1 
Behavioral  profiles  of  three  population  clusters  identified  through  k-means 
clustering with cluster-specific intervention recommendations, delivery mech-
anisms, and resource allocation guidance. Values represent percentages unless 
otherwise noted. BDT = Bangladeshi Taka.

Cluster 0: 
Digitally Literate 
Planners

Cluster 1: 
Informally Active 
but Under skilled

Cluster 2: 
Digitally Excluded 
Traditionalists

34 % (n = 363)

41 % (n = 437)

25 % (n = 267)

Characteristic

Sample

proportion

Financial

knowledge
Savings behavior

Emergency

preparedness

Digital

Mean: 7.8/10 
(SD = 1.2)
87 % regular 
savers
78 % maintain 
funds (>3 
months)
• 94 % use

engagement

mobile banking

• 89 % trust

digital services

Formal banking

• 91 % regular

Informal

networks

Demographics

Primary needs

Intervention

type

Delivery

channels

Resource

allocation

Expected 
timeline

Implementation

partners

users

• Trust score:

4.2/5

Low reliance

• 62 % tertiary 
education
• 71 % urban
• Mean age: 37
• Income: 35,000

BDT

• Advanced 
products
• Investment 
education

• Sophisticated 
financial tools
• Robo-advisory

services
• Advanced 
investment 
platforms

• Mobile apps
• Web platforms
• Fintech

partnerships

• 10 % of

intervention 
budget
• (minimal 
support 
needed)
• Immediate 
engagement 
with advanced 
products

• Private sector

(banks, 
fintechs)
• Investment

firms

Mean: 5.4/10 
(SD = 1.6)
72 % maintain 
budgets
31 % maintain 
funds

• 56 % use 
mobile 
banking
• 68 % low

digital comfort

43 % regular 
users

Mean: 3.1/10 (SD =
1.8)
28 % regular savers

19 % maintain funds

• 15 % use mobile

banking

• 89 % low digital

comfort

21 % have accounts, 
12 % use regularly 
Trust score: 1.9/5

• 67 % in

• 73 % use informal

savings groups
• 81 % rely on 
family advice

• 48 %

secondary 
education
• 58 % rural
• Mean age: 34
• Income:

22,000 BDT

• Bridge to

formal systems

• Emergency 
preparedness
• Digital literacy
• Simplified 
banking 
products
• Transitional 
programs

lenders

• 91 % rely on 
family support
• 71 % primary or

less

• 78 % rural
• Mean age: 42
• Income: 15,000

BDT

• Basic financial

literacy

• Digital training
• Trust building

• Basic banking 
onboarding

• In-person training
• Agent banking

models

• Digital literacy

• Trust-building

training
• Community-

based 
education
• Community

centers

• Microfinance 
meetings
• Simplified 
mobile apps
• Cooperative 
gatherings

• 30 % of

intervention 
budget

• (transitional 
support)

• 12–18 months 
for formal 
system 
integration

• NGOs +

Private sector 
partnerships
• Microfinance 
institutions

programs

• Village meetings
• Trusted local

agents

• Face-to-face 
support
• Agricultural 
cooperatives

• 60 % of

intervention 
budget

• (comprehensive

support)

• 24–36 months for 
basic capability 
development

• Government +

NGOs

• Community 
organizations
• Agent banking

networks

15

Table 1 (continued )

Characteristic

Cluster 0: 
Digitally Literate 
Planners

Cluster 1: 
Informally Active 
but Under skilled

Cluster 2: 
Digitally Excluded 
Traditionalists

Success metrics

• Product

adoption rates

• Investment 
portfolio 
diversity
• Advanced

• Formal 
account 
opening
• Emergency

fund 
establishment

• Basic account 
ownership

• Institutional trust 
improvement
• Savings initiation

service usage

• Digital

transaction 
frequency

resources,  incomplete  info,  and  time—so  even  with  financial  knowl-
edge,  they  may  not  apply  it  consistently  (Chawla  et  al.,  2020;  Singh 
et al., 2020). Consequently, interventions should simplify decisions and 
include  support  tools,  not  just  increase  knowledge.  The  challenge  in 
translating knowledge into savings behavior, especially due to present 
bias—overvaluing immediate rewards—shows people understand sav-
ings'  importance  but  fail  to  act.  Effective  strategies  should  include 
commitment  devices,  mental  accounting,  and  default  enrollment  to 
leverage inertia and promote beneficial behaviors (Sultana et al., 2025). 
Trust  in  banking  was  the  second-strongest  predictor,  with  a  SHAP 
importance  of  0.18,  compared  to  education  at  0.09,  highlighting 
financial  self-efficacy—confidence  in  executing  financial  behaviors. 
Knowledge raises awareness, but self-efficacy influences success belief 
(Lusardi  &  Streeter,  2023).  Financial  programs  should  include 
confidence-building  with  mastery  experiences,  peer  models,  and  sup-
portive  environments  that  reduce  anxiety  and  foster  skills.  Trust  in 
banks and microfinance institutions is crucial, as they serve as literacy 
educators.  Enhancing  transparency  with  clear  fees,  contracts,  and 
complaint  channels  could  improve  literacy  more  than  traditional 
financial education, which often overlooks trust barriers.

4.3. ML insights and methodological contributions

The  modest  predictive  performance  of  ML  models,  with  XGBoost 
achieving an F1-score of 0.52, representing a 58 % improvement over 
the random classification baseline of 0.33, highlights both the promise 
and limitations of AI-based financial profiling. While the F1-score may 
seem modest in absolute terms, it reflects broader challenges in applying 
predictive models to social data, such as class imbalance—where high- 
literacy  cases  make  up  only  15  %—latent  variables  not  captured  in 
surveys,  and  measurement  noise  from  self-reported  behaviors  (Imani 
et al., 2025). Nonetheless, these models' value extends beyond predic-
tive accuracy to their interpretability and ability to uncover actionable 
insights. SHAP value analysis provided transparent feature importance 
rankings, showing that income, digital access, trust in banks, and sour-
ces  of  financial  education  are  the  most  critical  predictors,  consistent 
with  growing  literature  emphasizing  that  behavioral  and  structural 
variables—such as perceived security, usability, and institutional cred-
ibility—are  just  as  important  as  formal  education  or  income  levels 
(Garson,  2021;  Singh  et  al.,  2020).  The  3D  SHAP  interaction  plots 
showed  that  middle-aged  individuals  (35–50)  with  moderate  income 
(20,000–30,000 BDT) and digital access had predicted literacy proba-
bilities over 0.65. This group often demonstrates digital adaptability and 
financial responsibility, making them ideal for fintech education efforts 
(Jarupunphol  et al., 2024). SHAP analysis  improves  stakeholder trust 
and makes findings accessible to policymakers, educators, and NGOs for 
targeted  interventions  based  on  transparent  insights  rather  than 
black-box models. The study shows ML can be responsibly used in social 
sciences  with  explainability  techniques  that  ensure  transparency  and 
leverage  computational  strengths  for  pattern  detection  (Yang  &  Xie, 
2025).

---

<!-- PAGE 16 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 16. Pathway from region to literacy to emergency fund ownership.

4.4. Behavioral segmentation within financial capability frameworks

The three-cluster behavioral segmentation identified through unsu-
pervised  learning  can  be  meaningfully  aligned  within  established 
financial capability frameworks while enhancing these frameworks with 
empirical insights from Bangladesh's context. The World Bank's financial 
capability approach emphasizes that effective financial behavior results 
from both ability, which  includes knowledge and skills, and opportu-
nity, which involves access to suitable financial services and supportive 
institutional  environments.  Our  behavioral  clusters  illustrate  this 
framework: Cluster 0 demonstrating high ability with financial knowl-
edge scores of 7.8 out of 10, combined with high opportunity reflected in 
94  %  digital  banking  usage  and  89  %  institutional  trust;  Cluster  1 
showing moderate ability through informal learning mechanisms, with 
72 % maintaining budgets but limited opportunity due to weak formal 
system  integration,  with  only  43  %  using  formal  banking  and  68  % 
reporting  low  digital  comfort;  and  Cluster  2  facing  both  ability  con-
straints, with knowledge scores of just 3.1 out of 10, and opportunity 
constraints, with 15 % digital banking usage and trust scores of 1.9 out 
of  5.  This  operationalization  illustrates  that  capability  constraints  in 
Cluster  1  are  primarily  opportunity  deficits  rather  than  ability  gaps, 
indicating  that  interventions  should  focus  on  improving  access  and 
building 
than  solely  addressing  knowledge  gaps 
(Koskelainen et al., 2023; Zaimovic et al., 2023).

trust  rather

The  OECD  defines  financial  literacy  as  encompassing  knowledge, 
behaviors,  and  attitudes  across  key  areas,  including  money  manage-
ment,  planning,  risk  management,  and  navigating  the  financial  land-
scape  (OECD,  2022).  Our  behavioral  analysis  shows  that  these 
dimensions do not develop evenly across populations: Cluster 1 exhibits 
behavioral  activity,  with  72  %  budgeting,  but  has  only  moderate 
knowledge  scores  of  5.4  out  of  10,  while  Cluster  2  shows  low  trust, 
scoring  1.9  out  of  5,  which  limits  both  knowledge  acquisition  and

behavioral  implementation.  This  uneven  development  indicates  that 
traditional  models  assuming  simultaneous  growth  in  knowledge, 
behavior, and attitudes may not fully capture capability development 
where informal and formal systems coexist. The behavioral segmenta-
tion broadens existing frameworks by showing that pathways to finan-
cial  capability  are  multiple  and  nonlinear,  rather  than  progressing 
uniformly from low to high. Cluster 1, characterized by strong informal 
capabilities—67  %  participating  in  savings  groups—yet  weak  formal 
integration,  illustrates  that  individuals  can  have  substantial  financial 
skills  through  traditional  systems,  even  if  they  appear  to  have  low 
capability  based  on  assessments  focused  on  formal  financial  system 
interaction (Kamble et al., 2024). This suggests that capability frame-
works should explicitly recognize multiple parallel routes to financial 
well-being  instead  of  assuming  a  single  developmental  path  from 
informal to formal system engagement.

4.5. Gender, intersectionality, and inclusive design

Average  literacy  scores  showed  minimal  gender  differences,  with 
men scoring 5.58 and women 5.52, less than 1.1 % apart. However, the 
distribution of  literacy  outcomes and  interaction  effects  revealed  pat-
terns for intervention. Women benefited more from tertiary education, 
with an F-statistic of 4.83 and p-value of 0.003, versus men's F of 0.91 
and  p  of  0.44.  This  suggests  women  face  greater  barriers  to  informal 
financial  learning  due  to  cultural  constraints  limiting  workplace, 
networking,  and  social  interactions  where  financial  knowledge  is 
shared. Formal education is thus key for women's financial development 
(Basha et al., 2025; Haag & Brahm, 2025; Khalily, 2008). Interventions 
should target women's specific challenges, such as limited mobility in 
conservative  communities,  caregiving  burdens  restricting  evening  or 
distant programs, and time constraints from household and work duties. 
Voice-based or vernacular mobile interfaces could enhance inclusivity

16

---

<!-- PAGE 17 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Fig. 17. Flow from education to literacy to saving frequency.

for  gender-diverse  or  low-literacy  users  facing  barriers  to  text-based 
digital  financial  services  (Choung  et  al.,  2023;  Widyastuti  et  al., 
2024). Inclusive design is vital, improving usability to boost adoption, 
retention, impact, and market reach for financial providers.

4.6. Digital inclusion and technology-mediated financial behavior

The  prominence  of  digital  comfort  and  institutional  trust  as  key 
predictors, with combined SHAP importance of 0.29 exceeding educa-
tion's importance of 0.09, emphasizes that successful financial technol-
ogy adoption must address both technical and psychological barriers. In 
Bangladesh, the digital divide extends beyond access to include comfort, 
confidence, and trust in digital platforms, with 68 % of Cluster 1 and 89 
% of Cluster 2 reporting low digital comfort despite some level of digital 
access. This pattern aligns with research showing that digital financial 
literacy  is  a  more  reliable  predictor  of  good  financial  behavior  than 
traditional literacy measures alone, indicating that interventions should 
combine  digital  skill  development  with  financial  education  (Choung 
et al., 2023; Widyastuti et al., 2024). The finding that rural users show 
higher  financial  literacy  despite  lower  digital  access  challenges  the 
assumption that urban living automatically grants digital advantages, 
suggesting  that  community-based  informal  learning  mechanisms  in 
rural  areas  may  effectively  share  digital  financial  skills  through  peer 
networks  and  social  learning  even  without  formal  training  programs 
(Clark et al., 2025).

4.7. Implications for policy and practice

Findings  from  this  study  highlight  several  key  areas  for  policy 
innovation  and  private  sector  involvement.  First,  financial  literacy 
programs  should  be  tailored  to  behavioral  groups  identified  through 
segmentation analysis, with evidence-based strategies designed to meet

each group's specific needs and abilities. Cluster 2, which makes up 25 % 
of the population with average knowledge scores of 3.1 out of 10 and 
trust  scores  of  1.9  out  of  5,  would  benefit  from  analog-first  training 
delivered through community partnerships such as village councils and 
agricultural  cooperatives.  Meanwhile,  Cluster  0,  accounting  for  34  % 
with knowledge scores of 7.8 out of 10, could engage in advanced digital 
investment simulations and robo-advisory services developed by fintech 
companies (Choung et al., 2023). Resource allocation should align with 
each  segment's  needs,  with  approximately  60  %  of  intervention  re-
sources allocated to Cluster 2's comprehensive support, 30 % to Cluster 
1's bridge programs connecting informal and formal systems, and 10 % 
to Cluster 0's minimal support requirements. This segmentation strategy 
allows both public and private stakeholders to better allocate resources 
and maximize impact by focusing on targeted interventions that address 
specific capability gaps rather than generic programs assuming uniform 
needs.  Trust  in  financial  institutions  is  the  second-strongest  predictor 
after income, highlighting the need for transparent, accessible banking 
services, especially for marginalized groups. Providers can boost trust by 
simplifying documentation, clarifying fees, and offering dedicated sup-
port,  fostering  inclusion  and  loyalty  (Lusardi  &  Streeter,  2023).  The 
correlation between trust and literacy (0.18) shows banks should act as 
literacy educators, influencing financial capability. Programs targeting 
trust  deficits,  like  those  with  low  trust  scores  of  1.9  out  of  5,  may 
improve literacy more effectively than purely knowledge-based methods 
that overlook institutional barriers. Third, mobile internet, smartphone 
literacy, and app usability are essential for effective financial education, 
as  digital  platforms  increasingly  mediate  transactions.  Public-private 
partnerships  between  network  providers,  device  manufacturers,  and 
financial institutions can offer bundled solutions that improve connec-
tivity,  skills,  and  financial  capabilities  (Widyastuti  et  al.,  2024;  Amit 
et al., 2024). These models align commercial and development goals, 
especially  with  supportive  regulations  offering  incentives  like  tax

17

---

<!-- PAGE 18 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Table 2 
Summary of key empirical findings with statistical evidence and policy impli-
cations. Abbreviations: F=F-statistic, p = p-value, η2 = effect size, r = correla-
tion, SHAP = importance, DB = Davies-Bouldin, CH=Calinski-Harabasz.

Finding

Statistical Evidence

Rural literacy 
advantage

Rural mean: 5.73 vs Urban: 
5.34<br>F(1,1065) = 2.31, p =
0.13, η2 = 0.002<br>7.3 % 
higher rural scores

Education 
minimal 
impact

F(3,1063) = 0.74, p = 0.59, η2 =
0.002<br>No significant 
differences across primary, 
secondary, higher secondary, 
graduate

Knowledge- 
behavior 
disconnect

All correlations |r|<0.10, p >
0.05<br>Strongest: r = 0.23 
(investment confidence)

Institutional

trust 
paramount

SHAP importance: Trust = 0.18 
vs Education = 0.09<br > 2nd 
strongest predictor after income

Gender-

education 
interaction

Women: F(3,499) = 4.83, p =
0.003<br>Men: F(3,562) =
0.91, p = 0.44

Three

behavioral 
segments

Silhouette = 0.42, DB = 1.08, 
CH = 287.3<br>Cluster 0: 34 
%, Cluster 1: 41 %, Cluster 2: 25 
%

ML modest but 
meaningful

XGBoost F1 = 0.52, baseline =
0.33<br>58 % improvement 
over random

Implication for Policy/ 
Practice

Design interventions 
building on existing rural 
informal networks 
(cooperative savings groups, 
ROSCAs) rather than 
assuming deficits. Urban 
programs should emphasize 
emergency preparedness 
where rural populations 
show strength.
Prioritize experiential 
learning and community- 
based education over 
classroom instruction. 
Practical application 
opportunities may be more 
effective than theoretical 
knowledge transmission.
Programs must address 
behavioral barriers (present 
bias, bounded rationality), 
confidence building, and 
institutional access—not 
just information provision.
Trust-building through 
transparent fees, responsive 
service, and simplified 
documentation is 
foundational. Banks are 
literacy educators, not just 
service providers.
Women benefit significantly 
more from tertiary 
education. Targeted 
education programs for 
women with lower formal 
education critical for gender 
equity.
Differentiated interventions 
based on behavioral 
typology, not demographics. 
Resource allocation: 60 % to 
Cluster 2, 30 % to Cluster 1, 
10 % to Cluster 0.
Despite modest absolute 
performance, models reveal 
actionable insights through 
SHAP analysis. Value lies in 
interpretability and feature 
importance, not just 
prediction accuracy.

benefits.  Fourth,  financial  education  content  should  be  localized  to 
Bangladesh's context, gender-sensitive, and tailored to address behav-
ioral barriers such as present bias and self-efficacy, not just information 
gaps (Bhuiyan et al., 2025). Schools, NGOs, and financial institutions 
should  co-develop  adaptable  materials  tested  across  demographics, 
combining academic rigor, community reach, and technological capa-
bilities (Haag & Brahm, 2025; Rabeta & Sumi, 2023).

4.8. Limitations and future research directions

Despite  its  contributions,  this  study  has  limitations.  Self-reported 
behavior may suffer from social desirability bias, overestimating posi-
tive behaviors like savings and underestimating negative ones like debt, 
and recall bias, leading to inaccurate retrospective reports (Bertola and 
Lo  Prete,  2025).  An  online-only  survey  excludes  the  most  digitally 
excluded,  often  the  most  vulnerable,  potentially  overestimating

18

financial literacy by missing those without internet access. Cluster 2, at 
25 % of respondents but only 15 % digital banking usage, indicates the 
truly excluded may have even lower financial skills. The cross-sectional 
design  limits  causal  inferences  about  whether  institutional  trust  in-
fluences literacy or vice versa. Longitudinal studies over 24–36 months 
could identify  triggers for development and  causal mechanisms using 
fixed-effects or difference-in-differences methods. The modest F1-score 
of  0.52  suggests  other  variables  beyond  the  survey  items  could 
improve  the  model.  Unmeasured  psychological  traits  like  financial 
anxiety,  risk  tolerance,  and  locus  of  control  likely  influence  literacy 
outcomes  (Chawla  et  al.,  2020).  Social  network  factors,  such  as  peer 
financial behaviors and community norms, may also affect literacy but 
were not measured. Cultural bias is a limitation; despite adaptation, the 
survey may reflect Western financial concepts not fully suited to Ban-
gladesh's context, where informal systems prevail. Intersectionality gaps 
exist because the analysis treated demographic factors independently, 
failing  to  consider  how  multiple  marginalized  identities,  like  rural, 
low-education women, experience compounded disadvantages.

Future  research  should  explore  multiple  avenues  to  address  these 
limitations. Incorporating objective behavioral data from mobile money 
platforms,  linking  survey  responses  with  actual  transaction  histories, 
would validate self-reported behaviors and mitigate measurement error 
concerns.  Longitudinal  studies  tracking  individuals  over  time  would 
allow  for  causal  inference  and  insights  into  literacy  development  tra-
jectories, including identifying transitions between behavioral clusters. 
Conducting randomized controlled trials that compare cluster-specific 
interventions  with  generic  programs  would  demonstrate the  practical 
benefits  of  behavioral  segmentation  for  enhancing  intervention  effec-
tiveness. Cross-cultural validation by applying the framework in other 
South Asian contexts such as India, Pakistan, Nepal, and Sri Lanka would 
determine whether patterns are generalizable or specific to certain set-
tings. Adding psychographic measures like personality traits, financial 
anxiety, and risk tolerance could explore whether psychological factors 
improve  predictive  accuracy  beyond  demographics  and  behavior. 
Finally,  analyzing  algorithmic  fairness  across  demographic  groups 
would assess if ML models produce biased predictions, leading to the 
development  of  fairness-aware  models  that  incorporate  fairness  con-
straints to prevent unequal error rates across protected groups (Imani 
et al., 2025; Mustafa et al., 2024).

5. Conclusion

This  study  analyzed  financial  literacy  among  1067  adults  in 
Bangladesh  using  ML  and  behavioral  clustering  methods,  producing 
findings that challenge traditional views on financial skill development 
in  emerging  economies.  Three  key  empirical  contributions  emerged. 
First, rural participants slightly outperformed urban residents by 7.3 %, 
and formal education showed no significant effect on literacy outcomes, 
suggesting that informal knowledge transfer through cooperative sav-
ings groups, agricultural credit associations, and community networks 
may be more effective than previously acknowledged. Second, ML-based 
SHAP  analysis  identified  institutional  trust  (importance  value:  0.18), 
digital  comfort,  and  income  as  substantially  stronger  predictors  than 
traditional demographic factors such as education (0.09), while weak 
correlations  between  financial  knowledge  and  actual  behaviors  (r  <
0.10)  challenge  models  that  assume  knowledge  deficits  cause  low 
financial  literacy.  Third,  behavioral  clustering  revealed  three  distinct 
population  segments:  Digitally  Literate  Planners  (34  %,  mean  knowl-
edge score: 7.8/10), Informally Active but Underskilled individuals (41 
%, score: 5.4/10), and Digitally Excluded Traditionalists (25 %, score: 
3.1/10, trust: 1.9/5). These findings advance theoretical understanding 
in several ways. The prominence of institutional trust over formal edu-
cation  as  a  predictor  extends  behavioral  finance  theory  by  demon-
strating  that  confidence  in  financial  systems,  rather  than  knowledge 
acquisition alone, shapes financial capability in contexts where formal 
and  informal  systems  coexist.  The  identification  of  a  knowledge-

---

<!-- PAGE 19 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

behavior gap supports perspectives emphasizing that financial literacy 
interventions must address behavioral barriers including present bias, 
bounded rationality, and self-efficacy rather than simply providing in-
formation.  Furthermore,  the  behavioral  segmentation  approach  oper-
ationalizes the financial capability framework by showing that ability 
constraints  and  opportunity  constraints  vary  independently  across 
population segments, requiring differentiated intervention strategies.

The practical implications for policy and financial service providers 
are substantial. The behavioral segmentation framework recommends 
allocating approximately 60 % to comprehensive support for Digitally 
Excluded Traditionalists, 30 % to transitional bridge programs for the 
Informally Active segment, and 10 % to advanced product development 
targeting Digitally Literate Planners. Financial institutions should pri-
oritize  trust-building  through  transparent  fees,  simplified  documenta-
tion, and responsive service, recognizing their role as literacy educators 
rather  than  solely  service  providers.  The  SHAP-based  explainable  AI 
framework offers practitioners a replicable approach to translate algo-
intervention 
rithmic  outputs 
strategies.

into  actionable,

segment-specific

Future research should address current limitations and build upon 
this work. Long-term studies spanning 24–36 months could help clarify 
causal relationships in behavior and skill development. Using objective 
mobile money data would verify self-reports and minimize bias. Ran-
domized controlled trials comparing targeted cluster interventions with 
generic  programs  would  demonstrate  the  benefits  of  segmentation. 
Cross-cultural  validation  in  South  Asian  countries  such  as  India, 
Pakistan, Nepal, and Sri Lanka would evaluate the framework's overall 
applicability.  Future  research  should  also  incorporate  psychographic 
variables like financial anxiety, risk tolerance, and locus of control to 
enhance  prediction  accuracy.  Investigating  algorithmic  fairness  and 
bias-aware  ML  models  would  help  prevent  inequalities.  This  study 
provides a foundation for computational financial literacy by illustrating 
the potential of ML and behavioral clustering, emphasizing the impor-
tance of addressing methodological and cultural challenges.

measures, and their right to withdraw at any time.

Declaration of generative AI and AI-assisted technologies in the 
writing process

During the preparation of this work, the authors used Copilot and 
Claude to improve the readability and language of the manuscript. After 
using these tools/services, the authors reviewed and edited the content 
as needed and take full responsibility for the content of the published 
article.

Funding

This  research  did  not  receive  any  specific  grant  from  funding

agencies in the public, commercial, or not-for-profit sectors.

Declaration of competing interest

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

Acknowledgements

The authors would like to thank all survey respondents who partic-
ipated  in  this  study  and  contributed  their  time  and  insights  to  this 
research.

Data availability

The data that support the findings of this study are available from the 
corresponding author upon reasonable request. The data are not pub-
licly available due to privacy restrictions as  they contain information 
that could compromise the privacy of research participants.

CRediT authorship contribution statement

References

Tawhid Ahmed Chowdhury: Writing –  review &  editing, Valida-
tion,  Supervision,  Methodology,  Investigation,  Formal  analysis,  Data 
curation. Md Ariful Haque Chowdhury: Writing –  review &  editing, 
Writing  –  original  draft,  Visualization,  Validation,  Supervision,  Soft-
ware,  Resources,  Project  administration,  Methodology,  Investigation, 
Funding acquisition, Formal analysis, Data curation, Conceptualization. 
Md Tahidur Rahman: Writing – review & editing, Validation, Software, 
Project  administration,  Methodology,  Funding  acquisition,  Data  cura-
tion. Iftakhar Ahmed: Writing – review & editing, Validation, Software, 
Project  administration,  Investigation,  Formal  analysis,  Data  curation. 
Nabila  Ahmed:  Writing  –  review  &  editing,  Visualization,  Software, 
Project  administration,  Investigation,  Formal  analysis,  Data  curation. 
Md Azizul Islam Tuhin: Writing – review & editing, Validation, Soft-
ware, Project administration, Investigation, Data curation. Abdulla Al 
Kafy: Writing – review & editing, Validation, Software, Project admin-
istration, Methodology, Formal analysis, Data curation.

Ethics approval statement

This  study  was  approved  by  the  Bangladesh  Army  International 
University of Science and Technology Ethics Review Board (Approval 
Number:  2024-0102;  Approval  Date:  February  2024).  All  procedures 
performed  in  this  study  involving  human  participants  were  in  accor-
dance with the ethical standards of the institutional research committee 
and with the 1964 Helsinki Declaration and its later amendments. Dig-
ital  informed  consent  was  obtained  from  all  individual  participants 
included  in  the  study  prior  to  survey  completion.  Participation  was 
entirely voluntary with no remuneration offered, and respondents were 
informed  of  the  study's  purpose,  data  utilization,  confidentiality

Adel, N. (2024). The impact of digital literacy and technology adoption on financial 
inclusion in Africa, Asia, and Latin America. Heliyon, 10(24), Article e40951. 
https://doi.org/10.1016/j.heliyon.2024.e40951

Amit, S., Levermore, R., & Kafy, A. Al (2024). Reimagining entrepreneurship by utilizing 
venture dynamics in sharing economy: Evaluating the symbiosis of macro and micro 
factors for sustainable capital flows in developing markets. Business Strategy & 
Development, 7(3). https://doi.org/10.1002/bsd2.417

Arora, R., & Sarker, T. (2025). Financing of sustainable development goals (SDGs) challenges

and opportunities.

Basha, S. A., Bennasr, H., & Goaied, M. (2025). Culture, financial literacy, and leverage of 
small firms. Research in International Business and Finance, 75, Article 102759. 
https://doi.org/10.1016/j.ribaf.2025.102759

Bayakhmetova, A., Rudenko, L., Krylova, L., Suleimenova, B., Niyazbekova, S., &

Nurpeisova, A. (2025). Artificial intelligence in financial behavior: Bibliometric 
ideas and new opportunities. Journal of Risk and Financial Management, 18(3). 
https://doi.org/10.3390/jrfm18030159

Bertola, G., & Lo Prete, A. (2025). Who prefers guessing to admitting they don't know? 
Measurement error in financial literacy surveys. Journal of Economic Behavior & 
Organization, 233. https://doi.org/10.1016/j.jebo.2025.107003

Bhuiyan, M. R. I., Husain, T., Islam, S., & Amin, A. (2025). Exploring the prospective 
influence of artificial intelligence on the health sector in Bangladesh: A study on 
awareness, perception and adoption. Health Education. https://doi.org/10.1108/HE- 
10-2024-0125

Chawla, I., Bartholomae, S., & Svec, J. (2020). Knowledge self-awareness, financial

behavior, and economic pressure.

Choung, Y., Chatterjee, S., & Pak, T. Y. (2023). Digital financial literacy and financial 
well-being. Finance Research Letters, 58. https://doi.org/10.1016/j.frl.2023.104438
Clark, R. L., Lin, C., Lusardi, A., Mitchell, O. S., & Sticha, A. (2025). Evaluating the effects 
of a low-cost, online financial education program. Journal of Economic Behavior & 
Organization, 232, Article 106952. https://doi.org/10.1016/j.jebo.2025.106952
Crompton, H., & Burke, D. (2023). Artificial intelligence in higher education: The state of 
the field. International Journal of Educational Technology in Higher Education, 20(1). 
https://doi.org/10.1186/s41239-023-00392-8

Garson, G. D. (2021). Data analytics for the social sciences. Routledge. https://doi.org/

10.4324/9781003109396

Haag, L., & Brahm, T. (2025). The gender gap in economic and financial literacy: A

review and research agenda. International Journal of Consumer Studies, 49(2). https:// 
doi.org/10.1111/ijcs.70031. John Wiley and Sons Inc.

19

---

<!-- PAGE 20 -->

T.A. Chowdhury et al.

Computers in Human Behavior Reports 21 (2026) 100926

Hossain, M. M., Ibrahim, Y., & Uddin, M. M. (2020). Finance, financial literacy and small 
firm financial growth in Bangladesh: The effectiveness of government support. 
Journal of Small Business and Entrepreneurship, 1–26. https://doi.org/10.1080/ 
08276331.2020.1793097

Imani, M., Beikmohammadi, A., & Arabnia, H. R. (2025). Comprehensive analysis of

random forest and XGBoost performance with SMOTE, ADASYN, and GNUS under 
varying imbalance levels. Technologies, 13(3). https://doi.org/10.3390/ 
technologies13030088

Jarupunphol, P., Buathong, W., Kuptabut, S., & Sudjarid, W. (2024). Assessing decision 
tree, random forest, and XGBoost models for human capital readiness predictions in 
low-income areas. Multidisciplinary Science Journal, 7(6), Article 2025296. https:// 
doi.org/10.31893/multiscience.2025296

OECD. (2022). Policy handbook on financial education in the workplace. https://doi.

org/10.1787/b211112e-en.

Rabeta, M., & Sumi, M. S. S. (2023). Impact of financial literacy on financial behaviour: 
Based on the evidence from the middle-class of Bangladesh. Research Journal of 
Finance and Accounting. https://doi.org/10.7176/rjfa/14-18-03

Roshid, M. M., & Le Ha, P. (2024). Medium of education and the politics of distraction in 
school education in Bangladesh. Current Issues in Language Planning. https://doi.org/ 
10.1080/14664208.2024.2368381

Sabri, M. F., Wahab, R., Mahdzan, N. S., Magli, A. S., & Rahim, H. A. (2022). Mediating

effect of financial behaviour on the relationship between perceived financial 
wellbeing and its factors among low-income young adults in Malaysia. Frontiers in 
Psychology, 13. https://doi.org/10.3389/fpsyg.2022.858630

Kamble, P. A., Mehta, A., & Rani, N. (2024). Financial inclusion and digital financial

Singh, G., Garg, V., & Tiwari, P. (2020). Application of artificial intelligence on

literacy: Do they matter for financial well-being? Social Indicators Research, 171(3), 
777–807. https://doi.org/10.1007/s11205-023-03264-w

Kelly, B. T., & Xiu, D. (2023). Financial machine learning.
Khalily, M. A. B. (2008). ADBI working paper series FINANCIAL INCLUSION. FINANCIAL 
REGULATION, AND EDUCATION IN BANGLADESH Asian Development Bank 
Institute. https://www.adb.org/publications/financial-inclusion-financial-regulati 
on-and-education-.

Koskelainen, T., Kalmi, P., Scornavacca, E., & Vartiainen, T. (2023). Financial literacy in 
the digital age—A research agenda. Journal of Consumer Affairs, 57(1), 507–528. 
https://doi.org/10.1111/joca.12510

Lusardi, A., & Messy, F.-A. (2023). The importance of financial literacy and its impact on 
financial wellbeing. Journal of Financial Literacy and Wellbeing, 1(1), 1–11. https:// 
doi.org/10.1017/flw.2023.8

Lusardi, A., & Streeter, J. L. (2023). Financial literacy and financial well-being: Evidence 
from the US. Journal of Financial Literacy and Wellbeing, 1(2), 169–198. https://doi. 
org/10.1017/flw.2023.13

Mustafa, M. Y., Tlili, A., Lampropoulos, G., Huang, R., Jandri´c, P., Zhao, J., Salha, S.,

Xu, L., Panda, S., Kinshuk, L´opez-Pernas, S., & Saqr, M. (2024). A systematic review 
of literature reviews on artificial intelligence in education (AIED): A roadmap to a 
future research agenda. Smart Learning Environments, 11(Issue 1). https://doi.org/ 
10.1186/s40561-024-00350-5. Springer.

behavioral finance. Studies in Computational Intelligence, 863(SCI), 342–353. https:// 
doi.org/10.1007/978-3-030-34152-7_26

Suarez-Lledo, V., & Alvarez-Galvez, J. (2019). A random forest approach to study social

determinants of depression: Turning the black box into a white box in social 
sciences. https://www.researchgate.net/publication/340279716.

Sultana, R., Chowdhury, M. A. H., Chowdhury, T. A., Tazminur, S., Ahmed, I.,

Ahmed, N., Baky, A. Al, Shahriar, A., & Kafy, A. Al (2025). Bridging business strategy 
and educational development: Private sector engagement and value creation 
framework for sustainable e-learning models in emerging markets. Business Strategy 
& Development, 8(1). https://doi.org/10.1002/bsd2.70098

Widyastuti, U., Respati, D. K., Dewi, V. I., & Soma, A. M. (2024). The nexus of digital 
financial inclusion, digital financial literacy and demographic factors: Lesson from 
Indonesia. Cogent Business & Management, 11(1). https://doi.org/10.1080/ 
23311975.2024.2322778

Yang, B., & Xie, X. (2025). Analyzing and predicting global happiness index via

integrated multilayer clustering and machine learning models. https://doi.org 
/10.1371/journal.pone.0322287.

Zaimovic, A., Torlakovic, A., Arnaut-Berilo, A., Zaimovic, T., Dedovic, L., & Nuhic

Meskovic, M. (2023). Mapping financial literacy: A systematic literature review of 
determinants and recent trends. Sustainability, 15(Issue 12). https://doi.org/ 
10.3390/su15129358. Multidisciplinary Digital Publishing Institute (MDPI).

20

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Computers in Human Behavior Reports 21 (2026) 100926
Contents lists available at ScienceDirect
Computers in Human Behavior Reports
journal homepage: www.sciencedirect.com/journal/computers-in-human-behavior-reports
Modeling financial literacy through explainable machine learning and
behavioral segmentation in emerging economies
Tawhid Ahmed Chowdhurya, Md Ariful Haque Chowdhurya,*, Md Tahidur Rahmana,
Iftakhar Ahmedb, Nabila Ahmedb, Md Azizul Islam Tuhinb, Abdulla Al Kafyc
aDepartment of Business Administration, Bangladesh Army International University of Science and Technology (BAIUST), Cumilla, 3501, Bangladesh
bUniversity of Liberal Arts Bangladesh, Dhaka, Bangladesh
cDepartment of Urban and Regional Planning, Rajshahi University of Engineering and Technology (RUET), Rajshahi, 6204, Bangladesh
A R T I C L E I N F O A B S T R A C T
Keywords: Digital financial services are changing how people behave financially but understanding how individuals use
Financial literacy financial technology remains limited in emerging economies. This study investigates financial literacy and
Machine learning technology-driven financial behavior using machine learning analysis of 1067 adults in Bangladesh. Traditional
Behavioral segmentation
demographic methods fail to capture the complexity of digital financial behavior, which hampers the design of
Digital inclusion
effective interventions. By applying Random Forest, XGBoost, and k-means clustering validated with a silhouette
Emerging economies
score of 0.42, Davies-Bouldin Index of 1.08, and Calinski-Harabasz Index of 287.3, we achieved moderate pre-
dictive performance with an F1-score of 0.52, a 58 % improvement over random guessing, and gained important
insights into technology-influenced financial behavior. SHAP analysis identified institutional trust, digital
comfort, and income as key predictors, with trust showing an importance value of 0.18 compared to education at
0.09, challenging typical demographic assumptions. Three distinct behavioral groups emerged: Digitally Literate
Planners (34 % of the sample, average financial knowledge 7.8/10), Informally Active but Underskilled (41 %,
knowledge 5.4/10), and Digitally Excluded Traditionalists (25 %, knowledge 3.1/10). Results show that rural
users had 7.3 % higher financial literacy than urban users, while formal education did not significantly impact
literacy levels. Weak correlations between financial knowledge and actual behaviors, with coefficients below
0.10, suggest that understanding alone does not lead to effective financial practices. The findings provide
frameworks for tailored interventions based on behavioral types instead of stereotypes, including resource
allocation of 60 % for support, 30 % for transitional programs, and 10 % for advanced services, to improve
intervention effectiveness for diverse users in developing economies.
1. Introduction compare options, and navigate systems has become crucial for economic
participation and success. The importance of financial literacy is espe-
Financial literacy is crucial for economic well-being worldwide, but cially clear in developing countries, where rapid digital changes are
traditional assessment methods often overlook many of its aspects and expanding access to financial services but also creating new challenges
fail to provide valuable insights for targeted actions (Lusardi & Messy, for people with limited experience in formal financial systems (Choung
2023; Lusardi & Streeter, 2023). People with higher financial literacy et al., 2023; Clark et al., 2025). Mobile banking, digital payments, and
tend to achieve better financial results, including saving more, man- fintech are transforming financial environments in emerging markets;
aging debt more effectively, preparing better for retirement, and being however, these technological advances do not automatically improve
more resilient to economic shocks. As financial products become more financial skills unless they are backed by basic understanding, proper
complex and innovative, the ability to understand financial ideas, institutional support, and user trust in digital platforms (Widyastuti
* Corresponding author. Department of Business Administration, Bangladesh Army International University of Science and Technology (BAIUST), Cumilla, 3501,
Bangladesh.
E-mail addresses: tawhidchowdhury166@gmail.com (T.A. Chowdhury), arifcubaiust@gmail.com, ariful.dba@baiust.ac.bd (M.A.H. Chowdhury), tahidur.
ais2004@gmail.com (M.T. Rahman), Iftakhar92@gmail.com (I. Ahmed), nabila0892@gmail.com (N. Ahmed), md.azizulislamtuhin@gmail.com (M.A.I. Tuhin),
abdulla-al.kafy@localpathways.org(A.A. Kafy).
https://doi.org/10.1016/j.chbr.2025.100926
Received 25 August 2025; Received in revised form 29 December 2025; Accepted 30 December 2025
Available online 30 December 2025
2451-9588/© 2026 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
et al., 2024; Adel, 2024). The digital financial gap is not just about access both ability—knowledge and skills—and opportunity—access to suit-
to technology, but also about fundamental gaps in knowledge, skills, able financial services and institutional support—to reach desired
trust, and confidence needed to navigate increasingly complex financial financial results (Koskelainen et al., 2023; Zaimovic et al., 2023).
systems safely and effectively (Koskelainen et al., 2023). In Bangladesh, Comparative research across various cultural settings consistently
where mobile financial services are rapidly growing alongside ongoing indicates that digital financial literacy is often a more reliable predictor
financial exclusion, understanding the complex links between de- of sound financial behavior than traditional literacy measures alone
mographic traits, digital access, and financial literacy has become (Choung et al., 2023; Widyastuti et al., 2024). In Bangladesh, where
crucial for shaping policy and designing effective interventions (Hossain women's access to financial services is frequently mediated through
et al., 2020; Khalily, 2008). Despite notable progress in adopting mobile family or spousal networks, understanding these dynamics is essential
financial services, significant gaps remain in individuals' ability to use for creating truly inclusive interventions (Khalily, 2008). The sociocul-
digital financial tools effectively and securely. This issue is especially tural and gendered aspects of financial literacy have gained increasing
troubling because simply having access to digital platforms does not attention, with studies documenting ongoing gender gaps driven by
guarantee proper usage without basic knowledge of financial concepts complex factors such as social norms, confidence differences, and dis-
and trust in institutions (Choung et al., 2023). The lack of financial parities in educational exposure (Haag & Brahm, 2025; Roshid & Le Ha,
education is even more evident in rural and semi-urban areas, where 2024). Evidence from around the world consistently shows a strong
infrastructural challenges and informational gaps continue to hinder positive link between financial literacy and better financial behaviors,
financial empowerment. Addressing these issues requires innovative with those possessing higher financial knowledge more likely to engage
approaches to assess financial literacy and create interventions that in long-term planning, responsible borrowing, and regular savings
consider Bangladesh's unique socioeconomic and technological envi- (Lusardi & Messy, 2023; Rabeta & Sumi, 2023; Sabri et al., 2022).
ronment (Arora & Sarker, 2025; Khalily, 2008; Rabeta & Sumi, 2023). Recent studies also reveal that both digital and traditional financial
Traditional financial literacy research in developing countries has literacy positively impact financial well-being in emerging markets,
mainly depended on descriptive surveys and simple regression models, emphasizing the need for comprehensive literacy assessments that
focusing mostly on demographic factors like age, education, and income consider multiple aspects of financial capability (Kamble et al., 2024).
(Zaimovic et al., 2023). These traditional methods, while offering useful Together, behavioral finance theory and the financial capability
initial insights, have clear limitations in capturing the complex, approach provide the conceptual foundation for this study's clustering
non-linear, and multidimensional relationships that shape financial and predictive modeling strategy.
behavior in fast-changing digital environments (Singh et al., 2020). Despite expanding access to digital financial tools across Bangladesh
Recent research has started using machine learning (ML) mod- and increasing recognition of financial literacy's importance, significant
els—including Random Forest, XGBoost, and LightGBM—to improve gaps remain in both understanding and methodological approaches.
prediction accuracy, classification, and understanding of important Financial literacy is still underexplored among socioeconomically
features in complex socioeconomic data (Garson, 2021; Imani et al., vulnerable groups in Bangladesh and similar developing countries,
2025). These advanced methods provide distinct benefits that suit especially affecting low-income communities, rural residents, and un-
financial literacy studies in diverse populations. ML algorithms are dereducated populations (Hossain et al., 2020; Kamble et al., 2024;
especially good at identifying non-linear relationships and threshold Rabeta & Sumi, 2023). Most notably, few studies have used ML ap-
effects in financial behavior, automatically detecting complex in- proaches specifically designed to address socio-demographic differences
teractions between variables without needing to specify every possible within Bangladesh's developing economy context. Moreover, existing
relationship beforehand, accommodating population differences research rarely employs advanced analytics to systematically map
through natural behavioral segmentation, and offering clear insights financial literacy across behavioral groups or to offer personalized in-
through explainable AI tools like SHAP values that policymakers and sights for targeted intervention strategies. The literature does not thor-
practitioners can easily understand and use (Jarupunphol et al., 2024; oughly investigate gendered and rural-urban digital divides using
Yang & Xie, 2025). Research shows that combining clustering methods predictive analytics, which could help inform targeted interventions
with supervised ML can greatly improve prediction accuracy in social instead of generic population-level programs. Additionally, most studies
science studies, and ensemble techniques like XGBoost tend to outper- do not apply explainable AI techniques that translate complex algo-
form traditional models in predicting human capital readiness in rural rithmic results into transparent, policy-relevant insights that practi-
areas (Jarupunphol et al., 2024; Yang & Xie, 2025). tioners and policymakers can effectively use in resource-limited settings.
Theoretical frameworks surrounding financial literacy have evolved This highlights a significant gap, given the potential for AI-powered
considerably from simple knowledge-based ideas to include behavioral frameworks to model financial literacy not just as an outcome variable
insights and digital aspects. Instead of viewing literacy as just a binary or but as a complex interplay of socio-economic, behavioral, and digital
scalar variable, modern scholars see it as a multidimensional concept factors.
that involves cognitive understanding, behavioral actions, emotional This study addresses these gaps by developing and evaluating a ML
attitudes, and the ability to adapt to different contexts (Bayakhmetova framework to predict financial literacy levels among Bangladeshi adults.
et al., 2025; Koskelainen et al., 2023). This view is based on behavioral It examines how socioeconomic, demographic, and behavioral factors
finance theory, which highlights that financial behavior is influenced influence financial capability within the context of an emerging econ-
not only by rational calculation but also by cognitive biases, heuristics, omy characterized by diverse educational backgrounds, varying income
and emotional factors that systematically affect choices even among levels, and differential access to digital financial services. The research
knowledgeable people (Chawla et al., 2020; Singh et al., 2020). The integrates behavioral clustering with supervised ML to identify natural
term “financial aliteracy” refers to situations where individuals greatly population segments while ensuring interpretability through SHAP
overestimate their financial skills, which can lead to risky or irrational analysis. This approach represents an innovative methodological com-
financial decisions. This issue is especially important in digital settings bination of unsupervised and supervised learning techniques within the
where superficial access to tools like mobile banking apps does not al- context of financial literacy in Bangladesh. By analyzing gendered pat-
ways mean proficient use (Chawla et al., 2020; Clark et al., 2025). terns, rural-urban differences, and educational effects using compre-
Research shows that financial behavior mainly mediates the link be- hensive primary data, the study offers actionable frameworks for
tween financial knowledge and perceived wellbeing, highlighting the targeted interventions based on behavioral typologies rather than de-
need for behaviorally based measurement frameworks that go beyond mographic stereotypes. The theoretical contribution conceptualizes
just testing knowledge (Sabri et al., 2022). The financial capability financial literacy as a dynamic, multidimensional construct shaped by
approach expands this view by defining financial wellbeing as requiring digital behavior patterns, contextual factors, and institutional trust. This
2

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
work advances perspectives in behavioral finance that emphasize the 2. Materials and methods
knowledge-behavior gap in financial decision-making (Koskelainen
et al., 2023; Zaimovic et al., 2023). 2.1. Study design and sampling
The primary aim of this study is to develop and systematically
evaluate a predictive ML framework designed to assess financial literacy This research employed a cross-sectional, quantitative design
levels among adults in Bangladesh. The specific objectives encompass: combining primary data collection through structured surveys with ML-
identifying key socio-demographic and digital access variables that in- based predictive modeling to evaluate financial literacy among adults in
fluence financial literacy within the Bangladeshi context through feature Bangladesh. The study was conducted from March to June 2024 and
importance analysis and explainable AI techniques; implementing targeted adults aged 18–60 with access to digital platforms across
advanced ML models—namely, Random Forest, XGBoost, and Decision diverse geographic and socioeconomic backgrounds. This approach
Tree—to classify financial literacy with superior predictive accuracy and improves on traditional correlation-based financial literacy studies by
interpretability in comparison to conventional regression methods; integrating robust survey methods with computational analytics to un-
analyzing behavioral clusters via unsupervised learning to identify cover complex, nonlinear relationships between socioeconomic factors
distinct population segments that support targeted financial education and financial outcomes that standard regression models often overlook
initiatives beyond traditional demographic classifications; and investi- (Imani et al., 2025; Singh et al., 2020). The framework followed a
gating the correlations between financial knowledge and actual finan- step-by-step process involving primary data collection via online sur-
cial behaviors to enhance both theoretical understanding and practical veys, thorough data preprocessing and feature engineering, develop-
intervention strategies. This research makes methodological contribu- ment and assessment of supervised ML models, and unsupervised
tions by incorporating explainable AI models in a domain traditionally behavioral clustering for population segmentation. This setup enables
dominated by static regression analyses and descriptive survey sum- both predictive modeling and natural behavioral segmentation, which
maries (Garson, 2021); conceptual contributions by framing financial traditional statistical methods often miss, particularly in the diverse
literacy as a complex function of interconnected variables influenced by populations typical of developing economies (Yang & Xie, 2025). Fig. 1
digital transformation and institutional contexts (Koskelainen et al., presents the complete methodological workflow outlining key stages
2023; Zaimovic et al., 2023); and practical contributions by offering from study design to policy implications.
actionable insights for financial educators, policymakers, and service A stratified random sampling technique was used with proportional
providers aiming to optimize educational content and intervention allocation based on Bangladesh's documented urban-rural population
strategies for Bangladesh's diverse population segments characterized split, maintaining a 45:55 urban-rural ratio to ensure representation
by varying levels of formal education, digital access, and engagement across key demographic groups. The target group included adults aged
with formal financial institutions. 18–60 with digital access, aligning with the focus on individuals who
could benefit from existing and emerging digital financial services.
Sample size was determined through statistical power analysis
Fig. 1. Methodological workflow outlining key stages from study design to policy implications in the financial literacy analysis.
3

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
conducted beforehand using G*Power 3.1 software for logistic regres- normalized using Min-Max scaling (0–1 range) to ensure comparability
sion with three predictor categories. The parameters included an alpha across measurement units. Missing data were minimal across the data-
significance level of 0.05, a power of 0.80, and a medium effect size set, affecting less than 1.2 % of total responses, and were addressed
corresponding to an odds ratio of 1.5. This analysis showed that at least using median imputation for numerical variables and mode imputation
786 participants were needed to detect significant effects with enough for categorical variables. Feature engineering played a vital role in
statistical power. The actual sample of 1067 valid responses surpassed enhancing the predictive capacity of ML models by capturing intricate
this minimum by 35.7 %, ensuring sufficient power for multivariate relationships that extend beyond simple variable effects. Several inter-
analysis. For ML purposes, the common guideline of at least ten obser- action terms were developed based on Bangladesh-specific financial
vations per predictor variable was met given the 28 predictors used, behavior patterns: income ×digital access (technology adoption across
resulting in about 38 observations per variable—well above the mini- economic strata), education ×age (generational differences in financial
mum—and providing enough data for training and testing models capability), gender × household decision-making roles (cultural in-
without overfitting concerns. The digital-only survey method was cho- fluences on financial authority), and urban-rural residence × digital
sen for its practical advantages in reaching geographically dispersed comfort (geographic variations in technology adoption). The dependent
populations, cost-effectiveness within the research budget, and its variable, financial literacy level, was operationalized through a com-
alignment with the study's focus on digitally accessible groups who are posite scoring approach integrating multiple assessment dimensions
the primary users of mobile financial services. During the March–June (Lusardi & Streeter, 2023; Sabri et al., 2022). The composite score was
2024 data collection period, digital outreach was the most feasible derived from ten core assessment items reflecting three pivotal di-
method given the rising rates of mobile and internet use across mensions: objective financial knowledge, including interest calculation
Bangladesh. However, this approach has limitations, such as digital skills, inflation comprehension, and risk diversification concepts;
exclusion, since the most financially vulnerable individuals without applied financial behaviors, such as budgeting practices, saving habits,
reliable internet access might be underrepresented, potentially biasing and borrowing decision-making processes; and financial
results toward more digitally engaged groups. decision-making capabilities, including investment choices and insur-
ance utilization patterns. Individual item scores were weighted in
2.2. Data collection and survey instrument accordance with established financial literacy assessment protocols
based on OECD guidelines, with scores aggregated to produce compre-
This study involved collecting original primary data rather than hensive literacy scores ranging from 0 to 10 (OECD, 2022). These scores
extracting it from existing databases or doing secondary analysis of were subsequently classified into three ordinal categories—Low, Mod-
previously gathered datasets. All data was directly gathered from Ban- erate, and High literacy—using tertile-based classification to ensure
gladeshi respondents using a custom-designed survey instrument balanced class representation for ML applications, yielding approxi-
administered online during the designated study period. Choosing to mately 33 % classified as Low literacy, 52 % as Moderate literacy, and
collect primary data was methodologically crucial to ensure the ques- 15 % as High literacy.
tions were suitable for Bangladesh's specific financial environment,
including mobile money services like bKash and Nagad, informal sav- 2.4. ML model development
ings groups, and rural cooperative banking practices. Data quality was
preserved through multiple validation steps, such as response time Three supervised learning classifiers were strategically selected
monitoring with surveys completed in less than 8 min flagged for re- based on empirical benchmarking studies in financial behavior
view, attention check questions embedded throughout the survey, modeling: Random Forest, XGBoost, and Decision Tree. The criteria for
logical consistency checks comparing related responses, and IP address model selection prioritized predictive accuracy and F1-score, which
verification to prevent duplicate submissions. The questionnaire was balances precision and recall, particularly important for imbalanced
created specifically for this research, guided by the internationally datasets. Model interpretability was also a key consideration, as it is
recognized OECD/INFE financial literacy assessment framework, while crucial for policy-relevant applications (Garson, 2021; Kelly & Xiu,
extensively adapting content to match Bangladesh's unique financial 2023). Random Forest was chosen for its robust handling of categorical
context (OECD, 2022). The final survey included 30 items across six variables, resistance to overfitting through ensemble averaging, and
domains: demographics (6 items including age, gender, education, ability to provide reliable feature importance rankings (Suarez-Lledo
employment, income, location), digital access and usage (5 items such as and Alvarez-Galvez, 2019). XGBoost was included based on research
smartphone ownership, internet connectivity, mobile banking apps, demonstrating its superior performance in predicting human capital
payment frequency, trust), financial knowledge (10 items on interest readiness in rural communities and other socioeconomic outcomes in
calculations, inflation, risk diversification, investment basics, insurance developing countries (Jarupunphol et al., 2024). Decision Tree was
fundamentals), behavioral traits (4 items regarding savings habits, incorporated to provide high interpretability through transparent deci-
budgeting, borrowing, planning), attitudinal dimensions (3 items on sion rules that policymakers can easily understand and implement.
decision confidence, institutional trust, perceived security), and The dataset was systematically divided using stratified sampling into
resource access (2 items about financial education sources and advice a training set comprising 70 % of the data, a validation set comprising
availability). The instrument was thoroughly validated through internal 10 % of the data for hyperparameter tuning, and a testing set comprising
reliability checks using Cronbach's alpha for all subdomains, with results 20 % of the data reserved for the final unbiased performance evaluation.
showing excellent consistency above 0.82, construct validity confirmed Stratified sampling ensured that the class distribution was preserved
through exploratory factor analysis with proper factor loadings, pilot across all three partitions. Hyperparameter optimization was conducted
testing with 30 participants representing diverse demographics, and through a comprehensive grid search combined with 5-fold cross-
expert review by financial literacy researchers and practitioners in validation to identify optimal configurations while preventing over-
Bangladesh (Garson, 2021; Koskelainen et al., 2023). fitting. For Random Forest, the grid search explored n_estimators values
of 100, 200, and 300; max_depth values of 10, 20, 30, and None; and
2.3. Data preprocessing and variable operationalization min_samples_split values of 2, 5, and 10. For XGBoost, explored pa-
rameters included learning_rate values of 0.01, 0.05, and 0.1; max_depth
Prior to model development, the collected dataset underwent values of 3, 5, and 7; and n_estimators values of 100, 200, and 300. For
comprehensive preprocessing procedures designed to ensure optimal Decision Tree, max_depths of 5, 10, 15, and 20 were evaluated, along
data quality for ML applications. All categorical features were trans- with min_samples_split values of 2, 5, 10, and 20.
formed using one-hot encoding, and numerical variables were Class imbalance, particularly the underrepresentation of high-
4

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
literacy individuals at 15 % of the sample, was systematically addressed appropriate for multi-class classification problems. Overall accuracy
through resampling techniques applied exclusively to the training data. determined the proportion of correct classifications across all classes.
Synthetic Minority Over-sampling Technique (SMOTE) was employed to Precision, recall, and F1-score were computed for each class individually
generate synthetic examples of minority classes by interpolating be- and subsequently macro-averaged across classes to assign equal signif-
tween existing minority class observations in feature space (Imani et al., icance to each category, irrespective of sample size. The F1-score sig-
2025). Additionally, Adaptive Synthetic (ADASYN) sampling was nifies the harmonic mean of precision and recall, offering a singular
applied, which generates synthetic samples with density distribution metric that balances these concerns and proves especially valuable for
according to learning difficulty. These techniques improved class bal- datasets exhibiting class imbalance. The Area Under the Receiver
ance in the training set to approximately 30-40-30 distribution across Operating Characteristic Curve (AUC-ROC) was calculated employing a
low, moderate, and high literacy classes, while maintaining the original one-vs-rest approach suitable for multi-class problems, measuring the
test set distribution for realistic performance evaluation. model's capability to distinguish between classes across various decision
Feature importance analysis utilized both traditional Gini impor- thresholds. Confusion matrices provided detailed insights into misclas-
tance metrics provided by tree-based algorithms and SHAP (SHapley sification patterns, indicating which classes were most frequently
Additive exPlanations) values to provide complementary perspectives confused. All aforementioned performance metrics were derived from
on feature contributions (Crompton and Burke, 2023). SHAP analysis, the held-out test set, which was excluded from the model training and
grounded in cooperative game theory, assigns each feature an impor- hyperparameter tuning processes, thereby ensuring an unbiased evalu-
tance value for individual predictions by calculating the marginal ation of the model's generalization capacity.
contribution of each feature across all possible feature combinations. Prior to data collection, comprehensive ethical clearance was gran-
SHAP visualizations included summary plots showing global feature ted by the Bangladesh Army International University of Science and
importance rankings, dependence plots illustrating relationships be- Technology Ethics Review Board under approval number 2024-0102.
tween individual features and predictions, interaction plots revealing Participation was entirely voluntary, with no remuneration or in-
compound effects between variable pairs, and force plots explaining centives offered. Digital informed consent was obtained from all re-
individual predictions. This explainability framework transformed ab- spondents at the survey's outset, including explicit explanations of the
stract algorithmic outputs into concrete, actionable insights regarding study's purpose, data utilization, confidentiality measures, and the right
determinants of financial literacy. to withdraw. Data anonymization procedures were implemented to
ensure that no personally identifiable information was retained within
2.5. Behavioral clustering analysis the analytical dataset. All survey responses were assigned anonymous
identification codes, with any identifiable data promptly separated from
Unsupervised learning utilizing k-means clustering was employed to response data and destroyed following data collection. Results were
identify natural population segments based on behavioral patterns and reported in aggregate form, with minimum cell sizes of ten observations
financial characteristics rather than predefined demographic categories. to prevent individual identification. Data security was maintained
The optimal number of clusters was determined through three comple- through encrypted storage, with access limited solely to authorized
mentary approaches. Firstly, the elbow method examined the within- members of the research team.
cluster sum of squares (WCSS) across k values from 2 to 8, identifying
the point where the marginal reduction in WCSS diminishes. Secondly, 3. Results
silhouette analysis evaluated cluster cohesion and separation by
measuring the similarity of each observation to its own cluster compared The results explore financial literacy patterns, modeling results, and
to other clusters. Thirdly, the gap statistic compared within-cluster behavioral segments from 1067 responses in Bangladesh. They aim to
dispersion to the expected values under a null distribution of data map literacy across demographics, identify predictors via ML, classify
with no inherent clustering structure. These three methods converged on behavioral groups, and examine links between demographics and liter-
k equals 3 as the optimal choice, supported by a silhouette score of 0.42, acy. The findings challenge assumptions and offer insights for targeted
indicating reasonable cluster separation, where values above 0.4 suggest interventions. The sample was 53 % male and 47 % female, reflecting
meaningful structure. Additionally, the Davies-Bouldin Index of 1.08 Bangladesh's demographics and cultural factors affecting participation.
indicates good clustering quality, as lower values below 1.5 are deemed
acceptable, while the Calinski-Harabasz Index of 287.3 signifies well- 3.1. Financial literacy distributions across demographic groups
defined clusters, with higher values reflecting greater separation
among them. The geographic analysis revealed counterintuitive patterns chal-
K-means implementation employed the k-means++ initialization lenging urban-centric policy assumptions. Fig. 2 shows rural partici-
algorithm to optimize centroid selection, which probabilistically choo- pants marginally surpassed urban residents in financial literacy (rural
ses initial centroids that are distant from each other to enhance mean: 5.73; urban mean: 5.34). Although this difference was not sta-
convergence speed and solution quality. The algorithm was configured tistically significant (F(1, 1065) = 2.31, p = 0.13, η2 = 0.002), the
with a maximum of 300 iterations, a convergence criterion of 1e-4 based consistent pattern suggests that informal financial knowledge trans-
on centroid movement threshold, and 10 random initializations with mission in rural communities—through cooperative savings groups,
different starting points to ensure the identification of the global opti- agricultural credit associations, and traditional financial net-
mum. Hierarchical clustering with Ward linkage was conducted as a works—may be more effective than previously acknowledged. This
validation step, producing dendrograms that corroborated similar finding indicates that policy interventions should recognize existing
segment structures with three-cluster solutions demonstrating clear informal financial capabilities rather than presuming knowledge
separation. Principal Component Analysis (PCA) was subsequently deficiencies.
applied to the clustered data, reducing dimensionality while maintain- Educational attainment analysis revealed patterns that complicate
ing 85 % of the variance, thereby facilitating visualization of cluster traditional human capital theories. Figs. 3 and 4show financial literacy
separation in two-dimensional space and confirming distinct population score distributions across educational levels. No significant differences
segments. emerged in average scores (primary: 5.48, SD =1.82; secondary: 5.52,
SD = 1.76; higher secondary: 5.61, SD = 1.79; graduate: 5.68, SD =
2.6. Model evaluation and ethical considerations 1.73; F(3, 1063) = 0.74, p = 0.59, η2 = 0.002). However, higher
educational attainment was associated with more consistent scores, with
The performance of the model was assessed using multiple metrics the interquartile range narrowing from 3.2 points (primary) to 2.1
5

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
compared to means of 5.23 (SD =1.91) for primary education, 5.41 (SD
=1.82) for secondary education, and 5.68 (SD =1.76) for higher sec-
ondary education. Two-way ANOVA confirmed a significant interaction
effect for women (F(3, 499) =4.83, p =0.003, η2 =0.028), suggesting
that women derive greater financial literacy benefits from tertiary ed-
ucation compared to lower educational levels. This pattern may reflect
cultural factors that limit women's access to informal financial learning
opportunities, making formal education a more critical pathway for
female financial capability development. In contrast, male participants
displayed relatively consistent literacy performance across all education
levels, with means ranging from 5.62 (SD =1.75) for primary education
to 5.74 (SD = 1.71) for graduate education, showing no statistically
significant variation (F(3, 562) = 0.91, p = 0.44, η2 = 0.005). This
pattern indicates that men may acquire financial knowledge through
diverse pathways beyond formal education, possibly including work-
place exposure, business activities, and social networks that provide
financial learning opportunities regardless of educational credentials.
The gender-education interactions revealed in Fig. 5highlight the need
for differentiated intervention approaches that account for varying
pathways to financial literacy development.
3.2. Relationships between financial knowledge, behavior, and
demographics
Fig. 2. Financial literacy scores by region. Correlation analysis between financial knowledge assessments and
behavioral indicators revealed weak associations that challenge con-
points (graduate education). This suggests education may influence ventional assumptions about the relationship between knowledge and
consistency of financial knowledge application rather than overall behavior in financial literacy research and program development. Fig. 6
capability, and that practical financial knowledge in Bangladesh may be shows a comprehensive correlation matrix indicating that the ten
acquired through multiple pathways, including family transmission, financial knowledge questions—covering topics like interest calcula-
community networks, and workplace experience. tions, inflation understanding, risk diversification, investment basics,
Gender-education interaction analysis revealed more nuanced pat- borrowing decisions, insurance concepts, budgeting principles, savings
terns that inform targeted intervention design and highlight the strategies, emergency planning, and retirement preparation—exhibited
complexity of demographic influences on financial literacy outcomes. weak individual correlations with behavioral indicators such as actual
Fig. 5 presents a rose diagram illustrating these interaction effects, savings practices, budgeting behaviors, and emergency fund manage-
demonstrating that among female respondents, financial literacy scores ment. The absolute values of the correlation coefficients ranged from
peaked at the graduate education level with a mean of 6.12 (SD =1.54), 0.02 to 0.09, with none reaching statistical significance at the 0.05 level.
Fig. 3. Literacy distribution by education level with no significant differences.
6

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 4. Density of literacy scores across education groups.
Fig. 5. Gender–education interaction effects on financial literacy.
This suggests that having theoretical financial knowledge does not these relationships are moderate rather than deterministic. Age recorded
automatically lead to practical financial actions, supporting views that a similarity score of 24.32 %, and marital status 18.47 %, suggesting
highlight the importance of experiential learning, behavioral rein- moderate influence levels and emphasizing the importance of consid-
forcement, and contextual factors in financial education programs. The ering life stage contexts and family responsibilities within financial lit-
strongest relationships appeared between investment confidence mea- eracy initiatives, rather than relying solely on static demographic
sures and specific knowledge questions about risk assessment and attributes. Gender demonstrated the lowest similarity score at 12.15 %,
diversification principles, with a correlation coefficient of 0.23 (95 % CI indicating minimal direct association with literacy outcomes when other
[0.17, 0.29], p <0.001). This indicates partial alignment between un- factors are controlled. The analysis underscores that multiple factors
derstanding and confidence in specific financial areas. Still, these cor- collectively influence financial literacy outcomes, with no singular de-
relations are modest, implying that confidence in financial decision- mographic characteristic emerging as a dependable predictor. Addi-
making is influenced by factors beyond simply acquiring knowledge, tionally, the combined effect of various demographic variables accounts
such as prior experience with financial institutions, social support net- for only a moderate proportion of variance in literacy classifications.
works, cultural attitudes toward risk, and perceived access to reliable Fig. 8 depicts the intricate relationship between age and monthly
financial services. income through a hexbin scatter plot that illustrates clustering patterns
Fig. 7delineates the demographic similarity analysis, offering valu- with significant implications for targeting financial inclusion initiatives.
able insights into the relative significance of various personal charac- While the overall Pearson correlation between age and income was weak
teristics in predicting financial literacy outcomes. The analysis reveals (r =0.01, p =0.89), the visualization exposes distinct clustering pat-
that education level and employment status exhibit the highest associ- terns among individuals aged 25–45 earning between 20,000–30,000
ations with financial literacy classification, each with similarity scores of Bangladeshi Taka monthly, with this cluster comprising approximately
approximately 36.86 %, thereby affirming their relevance. However, 38 % of the total sample. These income-age clusters may represent
7

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 6. Correlation matrix of knowledge and behavior indicators.
Bangladesh's emerging working-class segment, whose financial literacy behavioral prediction typically yields F1-scores between 0.45 and 0.65.
development is likely influenced by factors such as access to digital Beyond predictive accuracy, these models are valuable for identifying
technology, employment stability, exposure to formal financial services feature relationships and offering interpretable insights for policy
through workplace benefits, and integration within urban banking development.
infrastructure. The clustering patterns indicate that age-income combi- Fig. 10 shows confusion matrix analysis for the Random Forest
nations may provide more insightful information for targeting purposes model, highlighting challenges in classifying individuals across three
than either variable alone, thereby presenting opportunities for the literacy categories. The model achieved 53 % accuracy for Moderate
development of segment-specific interventions that consider the joint literacy, likely due to larger sample size and clearer traits. Low literacy
distribution of these demographic attributes. accuracy was 47 %, while High literacy was only 10 %. The matrix
shows 62 % of actual High literacy individuals were misclassified as
Moderate, indicating difficulty distinguishing them with current vari-
3.3. ML model performance and feature importance
ables. Similarly, 38 % of Low literacy were misclassified as Moderate.
These patterns suggest the difficulty in identifying high literacy may be
Three supervised learning models—Random Forest, XGBoost, and
due to its rarity, subtle differences requiring better measurement, or
Decision Tree—were systematically trained and evaluated to predict
unmeasured variables. Improving methods could involve ensemble
financial literacy classifications. Performance assessment was conducted
strategies, cost-sensitive learning, or feature engineering to better
on an independent holdout test set comprising 20 % of the sample to
discriminate the High literacy category.
ensure an unbiased evaluation of their generalization capabilities. Fig. 9
Fig. 11presents SHAP analysis providing crucial insights into feature
shows comprehensive performance metrics across all three classifiers,
importance. Monthly income emerged as the strongest predictor (SHAP:
with XGBoost achieving superior overall performance F1-score of 0.52
0.31), followed by trust in banking institutions (0.18), age (0.14),
and an AUC-ROC of 0.527—marginally outperforming Random Forest,
sources of financial education (0.12), and digital comfort (0.11). Edu-
which had F1-score of 0.50 and an AUC-ROC of 0.514, and significantly
cation level showed limited importance (0.09), reaffirming that formal
outperforming Decision Tree, which had F1-score of 0.47 and an AUC-
education plays a surprisingly limited predictive role, while gender
ROC of 0.496. Overall accuracy ranged from 51 % for Decision Tree to
exhibited minimal direct capacity (0.06). The prominence of institu-
54 % for XGBoost. Although these performance levels seem modest,
tional trust as the second-strongest predictor underscores the impor-
context is important: XGBoost's F1-score represents a 58 % improvement
tance of cultivating confidence in formal financial systems, suggesting
over random classification baseline (0.33), class imbalance (High liter-
that enhancing banking accessibility and institutional transparency
acy: 15 %) poses inherent prediction challenges, and social science
8

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 7. Demographic similarity scores relative to literacy classification.
could substantially advance literacy outcomes. population of Bangladesh, thereby offering actionable frameworks for
Fig. 12illustrates the interaction analysis among age, income, and the design of targeted interventions. The clustering analysis was vali-
predicted literacy through a three-dimensional visualization, which dated through multiple metrics: a silhouette score of 0.42, indicating a
unveils complex relationships with significant implications for targeting reasonable degree of cluster separation, as values above 0.4 suggest
strategies. The analysis indicates that individuals aged 35–50 with meaningful structural delineation; a Davies-Bouldin Index of 1.08,
moderate income levels (20,000–30,000 BDT monthly) exhibit the indicating good clustering quality, with lower values representing
highest predicted literacy probabilities, exceeding 0.65 for this de- better-defined clusters; and a Calinski-Harabasz Index of 287.3,
mographic segment. Conversely, younger individuals under 30 with demonstrating well-defined clusters, with higher values indicating
lower incomes below 15,000 BDT monthly demonstrate predicted lit- greater separation between clusters relative to within-cluster dispersion.
eracy probabilities below 0.35, indicating higher risks of low literacy Fig. 13 presents comprehensive behavioral profiles across the three
classification. Middle-aged individuals with very high incomes identified clusters, revealing distinct patterns in financial behaviors,
exceeding 40,000 BDT also display elevated literacy predictions, sur- digital engagement, and institutional relationships, rather than tradi-
passing 0.60. This pattern likely reflects various underlying factors, tional demographic categories. Fig. 14 complements these profiles by
including limited financial exposure among young adults who have had comparing behavioral strengths across clusters, highlighting relative
fewer opportunities to acquire practical experience, restricted access to capabilities in savings, digital engagement, and formal banking
digital financial services due to economic constraints that hinder utilization.
meaningful engagement with formal financial systems, fewer opportu- Cluster 1, called “Informally Active but Underskilled,” makes up 41
nities for practical financial experience among younger populations who % of participants (n =437). It shows a mixed profile—strong in budg-
have yet to navigate major life financial decisions, and potential eting but weaker in emergency preparedness, formal financial services,
exclusion from formal financial systems that offer learning opportu- and advanced planning. As shown in Fig. 14, this group has a 72 %
nities. The interactions between age and income suggest the necessity budgeting rate, but only 31 % maintain emergency funds. Digital
for targeted interventions that address both economic limitations and banking usage is at 56 %, with 68 % feeling uncomfortable with digital
experiential learning opportunities for younger, economically disad- tools. Formal banking use stands at 43 %, and their average financial
vantaged demographic segments. knowledge score is 5.4 out of 10 (SD = 1.6). Interestingly, 67 %
participate in informal savings groups like samitis or ROSCAs, and 81 %
mainly rely on family advice for financial decisions, highlighting strong
3.4. Behavioral segmentation and population clustering informal networks. Demographically, 48 % have secondary education,
58 % live in rural areas, and the average age is 34 years (SD =9.1). The
Unsupervised learning techniques, including K-Means clustering, average monthly income is 22,000 BDT (SD =8600), about the national
effectively identified three coherent behavioral segments within the
9

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 8. Age–income distribution of respondents with clustered density.
Fig. 9. Model performance metrics across three classifiers.
median. This group demonstrates practical skills through community % of respondents (n = 267) and faces some significant challenges in
networks and traditional systems but could benefit from support to ac- various areas of financial capability, as shown in Fig. 14. This group has
cess and use formal financial services and digital platforms effectively. a savings rate of just 28 %, a mean financial knowledge score of 3.1 out
It's a transitional group that would thrive with bridge programs linking of 10 (SD =1.8), which is well below the overall average. Their emer-
informal practices to formal services, simple digital tools with good gency fund maintenance stands at 19 %, digital banking usage is only 15
support, and community-based financial education respecting and %, and a large 89 % report feeling only minimally comfortable with
building on existing strengths. digital tools. Ownership of formal banking accounts is at 21 %, with just
Cluster 2, known as “Digitally Excluded Traditionalists,” includes 25 12 % using these accounts regularly. Their average trust score in
10

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 10. Misclassification patterns by literacy level.
institutions is 1.9 out of 5, indicating some level of mistrust or skepti- for progression from lower to higher capability clusters, rather than
cism towards formal financial institutions. Despite these hurdles, this perceiving segments as permanently fixed categories.
group relies heavily on informal financial channels: 73 % borrow from Table 1presents comprehensive behavioral profiles and intervention
informal lenders, 58 % rely solely on cash transactions, 91 % receive recommendations for each of the three clusters, synthesizing de-
financial support from family during tough times, and 65 % depend on mographic characteristics, financial behaviors, digital engagement pat-
community reciprocity systems. Demographically, this cluster mostly terns, and institutional relationships alongside specific intervention
consists of individuals with primary education or less (78 %), many strategies, delivery channels, resource allocation guidance, and ex-
living in rural areas (78 %), with an average age of 42 years (SD =10.8). pected timelines for capability development. The clustering analysis has
Their average monthly income is 15,000 BDT (SD = 6200), which is important implications for financial service providers and policymakers.
below the national median. To support this group, targeted in- Cluster 0 represents a market-ready segment that could adopt sophisti-
terventions that combine basic financial education with digital literacy cated financial products and services with minimal educational support.
development are essential. These efforts can help them better integrate Cluster 1 represents a bridge segment that requires targeted support to
into the growing formal financial services and digital payment systems. transition from informal to formal financial systems but possesses
Yet, it's equally important to recognize and respect their resilience-many foundational capabilities that facilitate this transition. Cluster 2 repre-
rely on strong family bonds and community networks-so these tradi- sents a development priority requiring comprehensive support but also
tional strengths should be incorporated into intervention strategies significant potential for impact through well-designed interventions.
rather than replaced.
Fig. 15illustrates a Principal Component Analysis (PCA) visualiza-
3.5. Financial pathway analysis and behavioral flow patterns
tion of three behavioral clusters within a reduced two-dimensional
space, confirming their distinctiveness while indicating some overlap
Sankey diagram analysis revealed multi-step pathways linking
between Clusters 1 and 2, which suggests partial behavioral conver-
location, education, and financial literacy to outcomes like emergency
gence. The initial two principal components account for 68 % of the total
fund ownership and savings frequency. Fig. 16shows that rural residents
variance: PC1, explaining 42 % of the variance, predominantly reflects
have higher emergency fund rates (34 %) than urban residents (28 %),
digital engagement and integration into formal financial systems; PC2,
challenging assumptions about rural financial vulnerability. Among
capturing 26 % of the variance, pertains to financial knowledge and
highly literate rural residents, 67 % maintain emergency funds versus
planning sophistication. The pronounced separation of Cluster 0 from
52 % of urban counterparts. This suggests rural networks and
the other segments in the upper-right quadrant affirms its classification
community-based mechanisms may be more effective for emergency
as a distinct behavioral type with substantially different intervention
preparedness than urban financial services. The rural advantage likely
requirements and market opportunities. The overlap observed between
stems from stronger community support (78 % vs. 54 %), income
Clusters 1 and 2 in the middle-left region may be attributable to shared
volatility, cultural emphasis on security, and informal insurance outside
educational backgrounds, geographic characteristics, cultural in-
formal systems.
fluences, or transitional states wherein individuals evolve between
Fig. 17shows pathways from formal education to literacy and sav-
behavioral patterns over time. This visualization offers significant in-
ings, confirming high financial literacy often follows graduate education
sights for program development, indicating that interventions should
and links with active savings. Among those with graduate education, 58
consider potential movement between segments and facilitate pathways
% have high or moderate literacy versus 42 % with primary education.
11

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 11. Top predictors of financial literacy from SHAP analysis.
Also, 72 % of graduates save monthly or more, compared to 48 % with findings in Bangladesh show more complex patterns. Rural respondents
primary education. However, some with limited education develop good scored slightly higher, with rural scores 7.3 % above urban, though not
savings habits through alternative pathways, with 23 % of primary- statistically significant, and minimal gender disparities suggest informal
educated being high literacy and saving 68 % monthly, similar to 71 financial learning plays a bigger role than assumed. Community-based
% among graduate moderate literacy individuals. These pathways initiatives, informal savings groups, and local financial practices may
highlight multiple routes to financial capability, suggesting in- provide practical education, especially in rural areas with stronger social
terventions should cater to diverse learning approaches. Figs. 16 and 17 capital—78 % of rural residents reported reliable support during
provide frameworks for designing targeted support to boost financial financial emergencies versus 54 % in urban areas—and seasonal income
capability. Table 2summarizes the seven key findings from this analysis, management needs. These practices include rotating savings and
including statistical evidence and implications for policy design and informal insurance. However, since data collection was digital-only,
intervention strategies. The table offers an integrated view of how de- marginalized populations without internet access may be underrepre-
mographic patterns, knowledge-behavior links, predictive modeling sented, potentially biasing results. The minimal impact of formal edu-
insights, and behavioral segmentation work together to inform targeted cation on financial literacy, with ANOVA results showing no significant
intervention strategies for Bangladesh's diverse population segments. differences across levels and effect sizes of only 0.2 %, challenges
traditional human capital theories (Bayakhmetova et al., 2025; Koske-
4. Discussion lainen et al., 2023). This aligns with behavioral finance, which em-
phasizes that knowledge doesn't automatically lead to effective financial
4.1. Reconsidering demographic assumptions in financial literacy behavior, highlighting that interventions focusing solely on knowledge
may have limited impact (Sabri et al., 2022). The findings support
The lack of significant differences across demographic groups chal- experiential learning and behavioral reinforcement over
lenges assumptions about financial literacy determinants. While inter- classroom-based instruction. Density distributions indicate higher edu-
national studies emphasize education, urban residence, and male gender cation correlates with more consistent literacy, suggesting formal edu-
as key factors (Lusardi & Messy, 2023; Zaimovic et al., 2023), our cation influences knowledge application reliability rather than
12

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 12. Interaction effects of age and income on predicted literacy.
Fig. 13. Financial behavior profiles across respondent clusters.
capability alone. Educational efforts should focus on developing 4.2. The knowledge-behavior gap and behavioral economics insights
consistent application through practice and feedback, not just knowl-
edge acquisition. Weak correlations between financial knowledge and behavior, with
coefficients below 0.10 and no significance, highlight a key finding with
implications for financial education based on behavioral economics.
This reflects bounded rationality—people make decisions with limited
13

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 14. Behavioral strengths comparison across clusters.
Fig. 15. Principal component view of behavioral clusters.
14

T.A. Chowdhury et al.                                                                                                                                                                   C  o  m  p  u  t e r  s   i n    H  u  m   a n    B  e  h a  v  i o r    R  e p  o  r t s 21 (2026) 100926
| Table 1  |     |     |     | Table 1 (continued) |     |     |     |     |
| -------- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
Behavioral profiles of three population clusters identified through k-means
|     |     |     |     | Characteristic  | Cluster 0:  | Cluster 1:  | Cluster 2:  |     |
| --- | --- | --- | --- | --------------- | ----------- | ----------- | ----------- | --- |
clustering with cluster-specific intervention recommendations, delivery mech-
|     |     |     |     |     | Digitally Literate  | Informally Active  | Digitally Excluded  |     |
| --- | --- | --- | --- | --- | ------------------- | ------------------ | ------------------- | --- |
anisms, and resource allocation guidance. Values represent percentages unless
|     |     |     |     |     | Planners  | but Under skilled  | Traditionalists |     |
| --- | --- | --- | --- | --- | --------- | ------------------ | --------------- | --- |
otherwise noted. BDT =Bangladeshi Taka.
|     |     |     |     | Success metrics | • Product  | • Formal  | • Basic account  |     |
| --- | --- | --- | --- | --------------- | ---------- | --------- | ---------------- | --- |
Characteristic Cluster 0:  Cluster 1:  Cluster 2:  adoption rates account  ownership
|     |     |     |     |     | •   |     | •   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Digitally Literate  Informally Active  Digitally Excluded  Investment  opening Institutional trust
Planners but Under skilled Traditionalists portfolio  • Emergency  improvement
|                  |               |               |                    |     | d i v e r si t y | f u n d           | • Savings initiation |     |
| ---------------- | ------------- | ------------- | ------------------ | --- | ---------------- | ----------------- | -------------------- | --- |
| Sample           | 34 % (n =363) | 41 % (n =437) | 25 % (n =267)      |     | •                |                   |                      |     |
|                  |               |               |                    |     | A d v a n c e d  | e st a b lishment |                      |     |
| p ro p o r t ion |               |               |                    |     | service usage    | • Digital         |                      |     |
| Fin a n ci a l   | Mean: 7.8/10  | Mean: 5.4/10  | Mean: 3.1/10 (SD = |     |                  |                   |                      |     |
transaction
| knowledge | (SD =1.2) | (SD =1.6) | 1.8) |     |     |     |     |     |
| --------- | --------- | --------- | ---- | --- | --- | --- | --- | --- |
frequency
| Savings behavior | 87 % regular   | 72 % maintain  | 28 % regular savers |     |     |     |     |     |
| ---------------- | -------------- | -------------- | ------------------- | --- | --- | --- | --- | --- |
|                  | savers         | budgets        |                     |     |     |     |     |     |
| Emergency        | 78 % maintain  | 31 % maintain  | 19 % maintain funds |     |     |     |     |     |
resources, incomplete info, and time—so even with financial knowl-
| preparedness | funds (>3  | funds |     |     |     |     |     |     |
| ------------ | ---------- | ----- | --- | --- | --- | --- | --- | --- |
edge, they may not apply it consistently (Chawla et al., 2020; Singh
months)
Digital  • 94 % use  • 56 % use  • 15 % use mobile  et al., 2020). Consequently, interventions should simplify decisions and
engagement mobile banking mobile  banking include support tools, not just increase knowledge. The challenge in
|     | •   |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
89 % trust  banking 89 % low digital  translating knowledge into savings behavior, especially due to present
|     | digital services | • 68 % low  | comfort |     |     |     |     |     |
| --- | ---------------- | ----------- | ------- | --- | --- | --- | --- | --- |
bias—overvaluing immediate rewards—shows people understand sav-
digital comfort
Formal banking • 91 % regular  43 % regular  21 % have accounts,  ings' importance but fail to act. Effective strategies should include
users users 12 % use regularly  commitment devices, mental accounting, and default enrollment to
|     | • Trust score:  |     | Trust score: 1.9/5 |     |     |     |     |     |
| --- | --------------- | --- | ------------------ | --- | --- | --- | --- | --- |
leverage inertia and promote beneficial behaviors (Sultana et al., 2025).
4.2/5
• • Trust in banking was the second-strongest predictor, with a SHAP
| Informal  | Low reliance | 67 % in  | 73 % use informal  |     |     |     |     |     |
| --------- | ------------ | -------- | ------------------ | --- | --- | --- | --- | --- |
networks savings groups lenders importance of 0.18, compared to education at 0.09, highlighting
• 81 % rely on  • 91 % rely on  financial self-efficacy—confidence in executing financial behaviors.
family advice family support Knowledge raises awareness, but self-efficacy influences success belief
|     | •   | •   | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Demographics 62 % tertiary  48 %  71 % primary or  (Lusardi  &  Streeter,  2023).  Financial  programs  should  include
|     | education | secondary  | less |     |     |     |     |     |
| --- | --------- | ---------- | ---- | --- | --- | --- | --- | --- |
confidence-building with mastery experiences, peer models, and sup-
|     | • 71 % urban | education | • 78 % rural |     |     |     |     |     |
| --- | ------------ | --------- | ------------ | --- | --- | --- | --- | --- |
|     | •            | •         | •            |     |     |     |     |     |
Mean age: 37 58 % rural Mean age: 42 portive environments that reduce anxiety and foster skills. Trust in
|     | • Income: 35,000  | • Mean age: 34 | • Income: 15,000  |     |     |     |     |     |
| --- | ----------------- | -------------- | ----------------- | --- | --- | --- | --- | --- |
banks and microfinance institutions is crucial, as they serve as literacy
|     | BDT | • Income:  | BDT |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
educators. Enhancing transparency with clear fees, contracts, and
22,000 BDT
• • • complaint  channels  could  improve  literacy  more  than  traditional
| Primary needs | Advanced  | Bridge to  | Basic financial  |     |     |     |     |     |
| ------------- | --------- | ---------- | ---------------- | --- | --- | --- | --- | --- |
products formal systems literacy financial education, which often overlooks trust barriers.
|     | • Investment  | • Emergency  | • Digital training |     |     |     |     |     |
| --- | ------------- | ------------ | ------------------ | --- | --- | --- | --- | --- |
•
education preparedness Trust building 4.3. ML insights and methodological contributions
• Digital literacy
| Intervention  | • Sophisticated  | • Simplified  | • Basic banking  |     |     |     |     |     |
| ------------- | ---------------- | ------------- | ---------------- | --- | --- | --- | --- | --- |
The modest predictive performance of ML models, with XGBoost
| type | financial tools | banking  | onboarding |     |     |     |     |     |
| ---- | --------------- | -------- | ---------- | --- | --- | --- | --- | --- |
• • achieving an F1-score of 0.52, representing a 58 % improvement over
|     | Robo-advisory  | products | In-person training |     |     |     |     |     |
| --- | -------------- | -------- | ------------------ | --- | --- | --- | --- | --- |
services • Transitional  • Agent banking  the random classification baseline of 0.33, highlights both the promise
|     | • Advanced  | programs | models |     |     |     |     |     |
| --- | ----------- | -------- | ------ | --- | --- | --- | --- | --- |
• • and limitations of AI-based financial profiling. While the F1-score may
|     | investment  | Digital literacy  | Trust-building  |     |     |     |     |     |
| --- | ----------- | ----------------- | --------------- | --- | --- | --- | --- | --- |
platforms training programs seem modest in absolute terms, it reflects broader challenges in applying
predictive models to social data, such as class imbalance—where high-
• Community-
literacy cases make up only 15 %—latent variables not captured in
based
education surveys, and measurement noise from self-reported behaviors (Imani
| Delivery  | • Mobile apps | • Community  | • Village meetings |     |     |     |     |     |
| --------- | ------------- | ------------ | ------------------ | --- | --- | --- | --- | --- |
et al., 2025). Nonetheless, these models' value extends beyond predic-
| channels | • Web platforms | centers | • Trusted local  |     |     |     |     |     |
| -------- | --------------- | ------- | ---------------- | --- | --- | --- | --- | --- |
• • tive accuracy to their interpretability and ability to uncover actionable
|     | Fintech  | Microfinance  | agents |     |     |     |     |     |
| --- | -------- | ------------- | ------ | --- | --- | --- | --- | --- |
partnerships meetings • Face-to-face  insights. SHAP value analysis provided transparent feature importance
• Simplified  support rankings, showing that income, digital access, trust in banks, and sour-
•
mobile apps Agricultural  ces of financial education are the most critical predictors, consistent
•
Cooperative  cooperatives with growing literature emphasizing that behavioral and structural
gatherings
variables—such as perceived security, usability, and institutional cred-
| Resource  | • 10 % of  | • 30 % of  | • 60 % of  |     |     |     |     |     |
| --------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- |
ibility—are just as important as formal education or income levels
| allocation | intervention  | intervention  | intervention  |     |     |     |     |     |
| ---------- | ------------- | ------------- | ------------- | --- | --- | --- | --- | --- |
|            | budget        | budget        | budget        |     |     |     |     |     |
(Garson, 2021; Singh et al., 2020). The 3D SHAP interaction plots
|     | • (minimal  | • (transitional  | • (comprehensive  |     |     |     |     |     |
| --- | ----------- | ---------------- | ----------------- | --- | --- | --- | --- | --- |
showed that middle-aged individuals (35–50) with moderate income
|     | support  | support) | support) |     |     |     |     |     |
| --- | -------- | -------- | -------- | --- | --- | --- | --- | --- |
(20,000–30,000 BDT) and digital access had predicted literacy proba-
needed)
Expected  • Immediate  • 12–18 months  • 24–36 months for  bilities over 0.65. This group often demonstrates digital adaptability and
timeline engagement  for formal  basic capability  financial responsibility, making them ideal for fintech education efforts
with advanced  system  development (Jarupunphol et al., 2024). SHAP analysis improves stakeholder trust
|     | products | integration |     |     |     |     |     |     |
| --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
and makes findings accessible to policymakers, educators, and NGOs for
| Implementation  | • Private sector  | • NGOs +        | • Government + |                          |        |                  |                   |       |
| --------------- | ----------------- | --------------- | -------------- | ------------------------ | ------ | ---------------- | ----------------- | ----- |
|                 |                   |                 |                | targeted  interventions  | based  | on  transparent  | insights  rather  | than  |
| partners        | (banks,           | Private sector  | NGOs           |                          |        |                  |                   |       |
• black-box models. The study shows ML can be responsibly used in social
|     | fintechs)     | partnerships    | Community     |     |     |     |     |     |
| --- | ------------- | --------------- | ------------- | --- | --- | --- | --- | --- |
|     | • Investment  | • Microfinance  | organizations |     |     |     |     |     |
sciences with explainability techniques that ensure transparency and
firms institutions • Agent banking  leverage computational strengths for pattern detection (Yang & Xie,
networks
2025).
15

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 16. Pathway from region to literacy to emergency fund ownership.
4.4. Behavioral segmentation within financial capability frameworks behavioral implementation. This uneven development indicates that
traditional models assuming simultaneous growth in knowledge,
The three-cluster behavioral segmentation identified through unsu- behavior, and attitudes may not fully capture capability development
pervised learning can be meaningfully aligned within established where informal and formal systems coexist. The behavioral segmenta-
financial capability frameworks while enhancing these frameworks with tion broadens existing frameworks by showing that pathways to finan-
empirical insights from Bangladesh's context. The World Bank's financial cial capability are multiple and nonlinear, rather than progressing
capability approach emphasizes that effective financial behavior results uniformly from low to high. Cluster 1, characterized by strong informal
from both ability, which includes knowledge and skills, and opportu- capabilities—67 % participating in savings groups—yet weak formal
nity, which involves access to suitable financial services and supportive integration, illustrates that individuals can have substantial financial
institutional environments. Our behavioral clusters illustrate this skills through traditional systems, even if they appear to have low
framework: Cluster 0 demonstrating high ability with financial knowl- capability based on assessments focused on formal financial system
edge scores of 7.8 out of 10, combined with high opportunity reflected in interaction (Kamble et al., 2024). This suggests that capability frame-
94 % digital banking usage and 89 % institutional trust; Cluster 1 works should explicitly recognize multiple parallel routes to financial
showing moderate ability through informal learning mechanisms, with well-being instead of assuming a single developmental path from
72 % maintaining budgets but limited opportunity due to weak formal informal to formal system engagement.
system integration, with only 43 % using formal banking and 68 %
reporting low digital comfort; and Cluster 2 facing both ability con-
4.5. Gender, intersectionality, and inclusive design
straints, with knowledge scores of just 3.1 out of 10, and opportunity
constraints, with 15 % digital banking usage and trust scores of 1.9 out
Average literacy scores showed minimal gender differences, with
of 5. This operationalization illustrates that capability constraints in
men scoring 5.58 and women 5.52, less than 1.1 % apart. However, the
Cluster 1 are primarily opportunity deficits rather than ability gaps,
distribution of literacy outcomes and interaction effects revealed pat-
indicating that interventions should focus on improving access and
terns for intervention. Women benefited more from tertiary education,
building trust rather than solely addressing knowledge gaps
with an F-statistic of 4.83 and p-value of 0.003, versus men's F of 0.91
(Koskelainen et al., 2023; Zaimovic et al., 2023).
and p of 0.44. This suggests women face greater barriers to informal
The OECD defines financial literacy as encompassing knowledge,
financial learning due to cultural constraints limiting workplace,
behaviors, and attitudes across key areas, including money manage-
networking, and social interactions where financial knowledge is
ment, planning, risk management, and navigating the financial land-
shared. Formal education is thus key for women's financial development
scape (OECD, 2022). Our behavioral analysis shows that these
(Basha et al., 2025; Haag & Brahm, 2025; Khalily, 2008). Interventions
dimensions do not develop evenly across populations: Cluster 1 exhibits
should target women's specific challenges, such as limited mobility in
behavioral activity, with 72 % budgeting, but has only moderate
conservative communities, caregiving burdens restricting evening or
knowledge scores of 5.4 out of 10, while Cluster 2 shows low trust,
distant programs, and time constraints from household and work duties.
scoring 1.9 out of 5, which limits both knowledge acquisition and
Voice-based or vernacular mobile interfaces could enhance inclusivity
16

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Fig. 17. Flow from education to literacy to saving frequency.
for gender-diverse or low-literacy users facing barriers to text-based each group's specific needs and abilities. Cluster 2, which makes up 25 %
digital financial services (Choung et al., 2023; Widyastuti et al., of the population with average knowledge scores of 3.1 out of 10 and
2024). Inclusive design is vital, improving usability to boost adoption, trust scores of 1.9 out of 5, would benefit from analog-first training
retention, impact, and market reach for financial providers. delivered through community partnerships such as village councils and
agricultural cooperatives. Meanwhile, Cluster 0, accounting for 34 %
4.6. Digital inclusion and technology-mediated financial behavior with knowledge scores of 7.8 out of 10, could engage in advanced digital
investment simulations and robo-advisory services developed by fintech
The prominence of digital comfort and institutional trust as key companies (Choung et al., 2023). Resource allocation should align with
predictors, with combined SHAP importance of 0.29 exceeding educa- each segment's needs, with approximately 60 % of intervention re-
tion's importance of 0.09, emphasizes that successful financial technol- sources allocated to Cluster 2's comprehensive support, 30 % to Cluster
ogy adoption must address both technical and psychological barriers. In 1's bridge programs connecting informal and formal systems, and 10 %
Bangladesh, the digital divide extends beyond access to include comfort, to Cluster 0's minimal support requirements. This segmentation strategy
confidence, and trust in digital platforms, with 68 % of Cluster 1 and 89 allows both public and private stakeholders to better allocate resources
% of Cluster 2 reporting low digital comfort despite some level of digital and maximize impact by focusing on targeted interventions that address
access. This pattern aligns with research showing that digital financial specific capability gaps rather than generic programs assuming uniform
literacy is a more reliable predictor of good financial behavior than needs. Trust in financial institutions is the second-strongest predictor
traditional literacy measures alone, indicating that interventions should after income, highlighting the need for transparent, accessible banking
combine digital skill development with financial education (Choung services, especially for marginalized groups. Providers can boost trust by
et al., 2023; Widyastuti et al., 2024). The finding that rural users show simplifying documentation, clarifying fees, and offering dedicated sup-
higher financial literacy despite lower digital access challenges the port, fostering inclusion and loyalty (Lusardi & Streeter, 2023). The
assumption that urban living automatically grants digital advantages, correlation between trust and literacy (0.18) shows banks should act as
suggesting that community-based informal learning mechanisms in literacy educators, influencing financial capability. Programs targeting
rural areas may effectively share digital financial skills through peer trust deficits, like those with low trust scores of 1.9 out of 5, may
networks and social learning even without formal training programs improve literacy more effectively than purely knowledge-based methods
(Clark et al., 2025). that overlook institutional barriers. Third, mobile internet, smartphone
literacy, and app usability are essential for effective financial education,
as digital platforms increasingly mediate transactions. Public-private
4.7. Implications for policy and practice
partnerships between network providers, device manufacturers, and
financial institutions can offer bundled solutions that improve connec-
Findings from this study highlight several key areas for policy
tivity, skills, and financial capabilities (Widyastuti et al., 2024; Amit
innovation and private sector involvement. First, financial literacy
et al., 2024). These models align commercial and development goals,
programs should be tailored to behavioral groups identified through
especially with supportive regulations offering incentives like tax
segmentation analysis, with evidence-based strategies designed to meet
17

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Table 2 financial literacy by missing those without internet access. Cluster 2, at
Summary of key empirical findings with statistical evidence and policy impli- 25 % of respondents but only 15 % digital banking usage, indicates the
cations. Abbreviations: F=F-statistic, p =p-value, η2 =effect size, r =correla- truly excluded may have even lower financial skills. The cross-sectional
tion, SHAP =importance, DB =Davies-Bouldin, CH=Calinski-Harabasz. design limits causal inferences about whether institutional trust in-
Finding Statistical Evidence Implication for Policy/ fluences literacy or vice versa. Longitudinal studies over 24–36 months
Practice could identify triggers for development and causal mechanisms using
Rural literacy Rural mean: 5.73 vs Urban: Design interventions fixed-effects or difference-in-differences methods. The modest F1-score
advantage 5.34<br>F(1,1065) =2.31, p = building on existing rural of 0.52 suggests other variables beyond the survey items could
0.13, η2 =0.002<br>7.3 % informal networks improve the model. Unmeasured psychological traits like financial
higher rural scores (cooperative savings groups,
anxiety, risk tolerance, and locus of control likely influence literacy
ROSCAs) rather than
assuming deficits. Urban outcomes (Chawla et al., 2020). Social network factors, such as peer
programs should emphasize financial behaviors and community norms, may also affect literacy but
emergency preparedness were not measured. Cultural bias is a limitation; despite adaptation, the
where rural populations survey may reflect Western financial concepts not fully suited to Ban-
show strength.
Education F(3,1063) =0.74, p =0.59, η2 = Prioritize experiential gladesh's context, where informal systems prevail. Intersectionality gaps
minimal 0.002<br>No significant learning and community- exist because the analysis treated demographic factors independently,
impact differences across primary, based education over failing to consider how multiple marginalized identities, like rural,
secondary, higher secondary, classroom instruction. low-education women, experience compounded disadvantages.
graduate Practical application
Future research should explore multiple avenues to address these
opportunities may be more
limitations. Incorporating objective behavioral data from mobile money
effective than theoretical
knowledge transmission. platforms, linking survey responses with actual transaction histories,
Knowledge- All correlations |r|<0.10, p > Programs must address would validate self-reported behaviors and mitigate measurement error
behavior 0.05<br>Strongest: r =0.23 behavioral barriers (present concerns. Longitudinal studies tracking individuals over time would
disconnect (investment confidence) bias, bounded rationality),
allow for causal inference and insights into literacy development tra-
confidence building, and
institutional access—not jectories, including identifying transitions between behavioral clusters.
just information provision. Conducting randomized controlled trials that compare cluster-specific
Institutional SHAP importance: Trust =0.18 Trust-building through interventions with generic programs would demonstrate the practical
trust vs Education =0.09<br >2nd transparent fees, responsive
benefits of behavioral segmentation for enhancing intervention effec-
paramount strongest predictor after income service, and simplified
tiveness. Cross-cultural validation by applying the framework in other
documentation is
foundational. Banks are South Asian contexts such as India, Pakistan, Nepal, and Sri Lanka would
literacy educators, not just determine whether patterns are generalizable or specific to certain set-
service providers. tings. Adding psychographic measures like personality traits, financial
Gender- Women: F(3,499) =4.83, p = Women benefit significantly
education 0.003<br>Men: F(3,562) = more from tertiary anxiety, and risk tolerance could explore whether psychological factors
interaction 0.91, p =0.44 education. Targeted improve predictive accuracy beyond demographics and behavior.
education programs for Finally, analyzing algorithmic fairness across demographic groups
women with lower formal would assess if ML models produce biased predictions, leading to the
education critical for gender
development of fairness-aware models that incorporate fairness con-
equity.
Three Silhouette =0.42, DB =1.08, Differentiated interventions straints to prevent unequal error rates across protected groups (Imani
behavioral CH =287.3<br>Cluster 0: 34 based on behavioral et al., 2025; Mustafa et al., 2024).
segments %, Cluster 1: 41 %, Cluster 2: 25 typology, not demographics.
% Resource allocation: 60 % to
5. Conclusion
Cluster 2, 30 % to Cluster 1,
10 % to Cluster 0.
ML modest but XGBoost F1 =0.52, baseline = Despite modest absolute This study analyzed financial literacy among 1067 adults in
meaningful 0.33<br>58 % improvement performance, models reveal Bangladesh using ML and behavioral clustering methods, producing
over random actionable insights through findings that challenge traditional views on financial skill development
SHAP analysis. Value lies in
in emerging economies. Three key empirical contributions emerged.
interpretability and feature
importance, not just First, rural participants slightly outperformed urban residents by 7.3 %,
prediction accuracy. and formal education showed no significant effect on literacy outcomes,
suggesting that informal knowledge transfer through cooperative sav-
ings groups, agricultural credit associations, and community networks
benefits. Fourth, financial education content should be localized to
may be more effective than previously acknowledged. Second, ML-based
Bangladesh's context, gender-sensitive, and tailored to address behav-
SHAP analysis identified institutional trust (importance value: 0.18),
ioral barriers such as present bias and self-efficacy, not just information
digital comfort, and income as substantially stronger predictors than
gaps (Bhuiyan et al., 2025). Schools, NGOs, and financial institutions
traditional demographic factors such as education (0.09), while weak
should co-develop adaptable materials tested across demographics, correlations between financial knowledge and actual behaviors (r <
combining academic rigor, community reach, and technological capa-
0.10) challenge models that assume knowledge deficits cause low
bilities (Haag & Brahm, 2025; Rabeta & Sumi, 2023).
financial literacy. Third, behavioral clustering revealed three distinct
population segments: Digitally Literate Planners (34 %, mean knowl-
4.8. Limitations and future research directions edge score: 7.8/10), Informally Active but Underskilled individuals (41
%, score: 5.4/10), and Digitally Excluded Traditionalists (25 %, score:
Despite its contributions, this study has limitations. Self-reported 3.1/10, trust: 1.9/5). These findings advance theoretical understanding
behavior may suffer from social desirability bias, overestimating posi- in several ways. The prominence of institutional trust over formal edu-
tive behaviors like savings and underestimating negative ones like debt, cation as a predictor extends behavioral finance theory by demon-
and recall bias, leading to inaccurate retrospective reports (Bertola and strating that confidence in financial systems, rather than knowledge
Lo Prete, 2025). An online-only survey excludes the most digitally acquisition alone, shapes financial capability in contexts where formal
excluded, often the most vulnerable, potentially overestimating and informal systems coexist. The identification of a knowledge-
18

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
behavior gap supports perspectives emphasizing that financial literacy measures, and their right to withdraw at any time.
interventions must address behavioral barriers including present bias,
bounded rationality, and self-efficacy rather than simply providing in- Declaration of generative AI and AI-assisted technologies in the
formation. Furthermore, the behavioral segmentation approach oper- writing process
ationalizes the financial capability framework by showing that ability
constraints and opportunity constraints vary independently across During the preparation of this work, the authors used Copilot and
population segments, requiring differentiated intervention strategies. Claude to improve the readability and language of the manuscript. After
The practical implications for policy and financial service providers using these tools/services, the authors reviewed and edited the content
are substantial. The behavioral segmentation framework recommends as needed and take full responsibility for the content of the published
allocating approximately 60 % to comprehensive support for Digitally article.
Excluded Traditionalists, 30 % to transitional bridge programs for the
Informally Active segment, and 10 % to advanced product development Funding
targeting Digitally Literate Planners. Financial institutions should pri-
oritize trust-building through transparent fees, simplified documenta- This research did not receive any specific grant from funding
tion, and responsive service, recognizing their role as literacy educators agencies in the public, commercial, or not-for-profit sectors.
rather than solely service providers. The SHAP-based explainable AI
framework offers practitioners a replicable approach to translate algo- Declaration of competing interest
rithmic outputs into actionable, segment-specific intervention
strategies. The authors declare that they have no known competing financial
Future research should address current limitations and build upon interests or personal relationships that could have appeared to influence
this work. Long-term studies spanning 24–36 months could help clarify the work reported in this paper.
causal relationships in behavior and skill development. Using objective
mobile money data would verify self-reports and minimize bias. Ran- Acknowledgements
domized controlled trials comparing targeted cluster interventions with
generic programs would demonstrate the benefits of segmentation. The authors would like to thank all survey respondents who partic-
Cross-cultural validation in South Asian countries such as India, ipated in this study and contributed their time and insights to this
Pakistan, Nepal, and Sri Lanka would evaluate the framework's overall research.
applicability. Future research should also incorporate psychographic
variables like financial anxiety, risk tolerance, and locus of control to Data availability
enhance prediction accuracy. Investigating algorithmic fairness and
bias-aware ML models would help prevent inequalities. This study The data that support the findings of this study are available from the
provides a foundation for computational financial literacy by illustrating corresponding author upon reasonable request. The data are not pub-
the potential of ML and behavioral clustering, emphasizing the impor- licly available due to privacy restrictions as they contain information
tance of addressing methodological and cultural challenges. that could compromise the privacy of research participants.
CRediT authorship contribution statement References
Tawhid Ahmed Chowdhury: Writing – review & editing, Valida- Adel, N. (2024). The impact of digital literacy and technology adoption on financial
inclusion in Africa, Asia, and Latin America. Heliyon, 10(24), Article e40951.
tion, Supervision, Methodology, Investigation, Formal analysis, Data
https://doi.org/10.1016/j.heliyon.2024.e40951
curation. Md Ariful Haque Chowdhury: Writing – review & editing, Amit, S., Levermore, R., & Kafy, A. Al (2024). Reimagining entrepreneurship by utilizing
Writing – original draft, Visualization, Validation, Supervision, Soft- venture dynamics in sharing economy: Evaluating the symbiosis of macro and micro
ware, Resources, Project administration, Methodology, Investigation, factors for sustainable capital flows in developing markets. Business Strategy &
Development, 7(3). https://doi.org/10.1002/bsd2.417
Funding acquisition, Formal analysis, Data curation, Conceptualization. Arora, R., & Sarker, T. (2025). Financing of sustainable development goals (SDGs) challenges
Md Tahidur Rahman: Writing – review & editing, Validation, Software, and opportunities.
Project administration, Methodology, Funding acquisition, Data cura- Basha, S. A., Bennasr, H., & Goaied, M. (2025). Culture, financial literacy, and leverage of
tion. Iftakhar Ahmed: Writing – review & editing, Validation, Software, small firms. Research in International Business and Finance, 75, Article 102759.
https://doi.org/10.1016/j.ribaf.2025.102759
Project administration, Investigation, Formal analysis, Data curation. Bayakhmetova, A., Rudenko, L., Krylova, L., Suleimenova, B., Niyazbekova, S., &
Nabila Ahmed: Writing – review & editing, Visualization, Software, Nurpeisova, A. (2025). Artificial intelligence in financial behavior: Bibliometric
ideas and new opportunities. Journal of Risk and Financial Management, 18(3).
Project administration, Investigation, Formal analysis, Data curation.
https://doi.org/10.3390/jrfm18030159
Md Azizul Islam Tuhin: Writing – review & editing, Validation, Soft- Bertola, G., & Lo Prete, A. (2025). Who prefers guessing to admitting they don't know?
ware, Project administration, Investigation, Data curation. Abdulla Al Measurement error in financial literacy surveys. Journal of Economic Behavior &
Kafy: Writing – review & editing, Validation, Software, Project admin- Organization, 233. https://doi.org/10.1016/j.jebo.2025.107003
Bhuiyan, M. R. I., Husain, T., Islam, S., & Amin, A. (2025). Exploring the prospective
istration, Methodology, Formal analysis, Data curation. influence of artificial intelligence on the health sector in Bangladesh: A study on
awareness, perception and adoption. Health Education. https://doi.org/10.1108/HE-
10-2024-0125
Ethics approval statement
Chawla, I., Bartholomae, S., & Svec, J. (2020). Knowledge self-awareness, financial
behavior, and economic pressure.
This study was approved by the Bangladesh Army International Choung, Y., Chatterjee, S., & Pak, T. Y. (2023). Digital financial literacy and financial
well-being. Finance Research Letters, 58. https://doi.org/10.1016/j.frl.2023.104438
University of Science and Technology Ethics Review Board (Approval
Clark, R. L., Lin, C., Lusardi, A., Mitchell, O. S., & Sticha, A. (2025). Evaluating the effects
Number: 2024-0102; Approval Date: February 2024). All procedures of a low-cost, online financial education program. Journal of Economic Behavior &
performed in this study involving human participants were in accor- Organization, 232, Article 106952. https://doi.org/10.1016/j.jebo.2025.106952
dance with the ethical standards of the institutional research committee Crompton, H., & Burke, D. (2023). Artificial intelligence in higher education: The state of
the field. International Journal of Educational Technology in Higher Education, 20(1).
and with the 1964 Helsinki Declaration and its later amendments. Dig- https://doi.org/10.1186/s41239-023-00392-8
ital informed consent was obtained from all individual participants Garson, G. D. (2021). Data analytics for the social sciences. Routledge. https://doi.org/
included in the study prior to survey completion. Participation was 10.4324/9781003109396
Haag, L., & Brahm, T. (2025). The gender gap in economic and financial literacy: A
entirely voluntary with no remuneration offered, and respondents were
review and research agenda. International Journal of Consumer Studies, 49(2). https://
informed of the study's purpose, data utilization, confidentiality doi.org/10.1111/ijcs.70031. John Wiley and Sons Inc.
19

T.A. Chowdhury et al. C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 21 (2026) 100926
Hossain, M. M., Ibrahim, Y., & Uddin, M. M. (2020). Finance, financial literacy and small OECD. (2022). Policy handbook on financial education in the workplace. https://doi.
firm financial growth in Bangladesh: The effectiveness of government support. org/10.1787/b211112e-en.
Journal of Small Business and Entrepreneurship, 1–26. https://doi.org/10.1080/ Rabeta, M., & Sumi, M. S. S. (2023). Impact of financial literacy on financial behaviour:
08276331.2020.1793097 Based on the evidence from the middle-class of Bangladesh. Research Journal of
Imani, M., Beikmohammadi, A., & Arabnia, H. R. (2025). Comprehensive analysis of Finance and Accounting. https://doi.org/10.7176/rjfa/14-18-03
random forest and XGBoost performance with SMOTE, ADASYN, and GNUS under Roshid, M. M., & Le Ha, P. (2024). Medium of education and the politics of distraction in
varying imbalance levels. Technologies, 13(3). https://doi.org/10.3390/ school education in Bangladesh. Current Issues in Language Planning. https://doi.org/
technologies13030088 10.1080/14664208.2024.2368381
Jarupunphol, P., Buathong, W., Kuptabut, S., & Sudjarid, W. (2024). Assessing decision Sabri, M. F., Wahab, R., Mahdzan, N. S., Magli, A. S., & Rahim, H. A. (2022). Mediating
tree, random forest, and XGBoost models for human capital readiness predictions in effect of financial behaviour on the relationship between perceived financial
low-income areas. Multidisciplinary Science Journal, 7(6), Article 2025296. https:// wellbeing and its factors among low-income young adults in Malaysia. Frontiers in
doi.org/10.31893/multiscience.2025296 Psychology, 13. https://doi.org/10.3389/fpsyg.2022.858630
Kamble, P. A., Mehta, A., & Rani, N. (2024). Financial inclusion and digital financial Singh, G., Garg, V., & Tiwari, P. (2020). Application of artificial intelligence on
literacy: Do they matter for financial well-being? Social Indicators Research, 171(3), behavioral finance. Studies in Computational Intelligence, 863(SCI), 342–353. https://
777–807. https://doi.org/10.1007/s11205-023-03264-w doi.org/10.1007/978-3-030-34152-7_26
Kelly, B. T., & Xiu, D. (2023). Financial machine learning. Suarez-Lledo, V., & Alvarez-Galvez, J. (2019). A random forest approach to study social
Khalily, M. A. B. (2008). ADBI working paper series FINANCIAL INCLUSION. FINANCIAL determinants of depression: Turning the black box into a white box in social
REGULATION, AND EDUCATION IN BANGLADESH Asian Development Bank sciences. https://www.researchgate.net/publication/340279716.
Institute. https://www.adb.org/publications/financial-inclusion-financial-regulati Sultana, R., Chowdhury, M. A. H., Chowdhury, T. A., Tazminur, S., Ahmed, I.,
on-and-education-. Ahmed, N., Baky, A. Al, Shahriar, A., & Kafy, A. Al (2025). Bridging business strategy
Koskelainen, T., Kalmi, P., Scornavacca, E., & Vartiainen, T. (2023). Financial literacy in and educational development: Private sector engagement and value creation
the digital age—A research agenda. Journal of Consumer Affairs, 57(1), 507–528. framework for sustainable e-learning models in emerging markets. Business Strategy
https://doi.org/10.1111/joca.12510 & Development, 8(1). https://doi.org/10.1002/bsd2.70098
Lusardi, A., & Messy, F.-A. (2023). The importance of financial literacy and its impact on Widyastuti, U., Respati, D. K., Dewi, V. I., & Soma, A. M. (2024). The nexus of digital
financial wellbeing. Journal of Financial Literacy and Wellbeing, 1(1), 1–11. https:// financial inclusion, digital financial literacy and demographic factors: Lesson from
doi.org/10.1017/flw.2023.8 Indonesia. Cogent Business & Management, 11(1). https://doi.org/10.1080/
Lusardi, A., & Streeter, J. L. (2023). Financial literacy and financial well-being: Evidence 23311975.2024.2322778
from the US. Journal of Financial Literacy and Wellbeing, 1(2), 169–198. https://doi. Yang, B., & Xie, X. (2025). Analyzing and predicting global happiness index via
org/10.1017/flw.2023.13 integrated multilayer clustering and machine learning models. https://doi.org
Mustafa, M. Y., Tlili, A., Lampropoulos, G., Huang, R., Jandri´c, P., Zhao, J., Salha, S., /10.1371/journal.pone.0322287.
Xu, L., Panda, S., Kinshuk, Lo´pez-Pernas, S., & Saqr, M. (2024). A systematic review Zaimovic, A., Torlakovic, A., Arnaut-Berilo, A., Zaimovic, T., Dedovic, L., & Nuhic
of literature reviews on artificial intelligence in education (AIED): A roadmap to a Meskovic, M. (2023). Mapping financial literacy: A systematic literature review of
future research agenda. Smart Learning Environments, 11(Issue 1). https://doi.org/ determinants and recent trends. Sustainability, 15(Issue 12). https://doi.org/
10.1186/s40561-024-00350-5. Springer. 10.3390/su15129358. Multidisciplinary Digital Publishing Institute (MDPI).
20