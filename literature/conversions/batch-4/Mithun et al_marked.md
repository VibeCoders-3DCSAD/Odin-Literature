---
conversion_metadata:
  converted_at: "2026-07-21T07:34:21Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Mithun et al.pdf"
  source_pdf_sha256: "b5ab2be5b650e389fd8511500c0d8bb71a542fd7b4fa51f4ce2b11ba34274c91"
  page_count: 29
  markdown_char_count: 212525
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Informatics and Data Science Research 
ISSN 2997-3961 (Online) 
Vol. 2, No. 10, Oct 2025,  
Available online at: https://scientificbulletin.com/index.php/IJIDSR

Developing AI-Powered Credit Scoring Models Leveraging 
Alternative Data for Financially Underserved US Small 
Businesses

Md Manarat Uddin Mithun  
Master of Science in Business Analytics, Trine University, USA

Sakhawat Hussain Tanim  
Master of Science in Technology Project Management, Illinois State University, USA

Rahanuma Tarannum 
Masters in Information Technology, Arkansas Tech University, USA

Article information:  
Manuscript received: 4 Aug 2025; Accepted: 10 Sep 2025; Published: 18 Oct 2025

Abstract:  In  the  modern  dynamically  changing  financial  landscape  where  people 
more  and  more  often  are  illegible  with  traditional  credit  scoring  systems,  traditional 
credit scoring systems are in many cases ineffective to capture the credit worthiness of 
the underserved small business borrowers- especially those who do not have lengthy 
credit histories or traditional documentation. In their study, the authors focus on how 
to  develop  and  implement  the  artificial  intelligence  (AI)-based  credit  scoring  models, 
which  can  solve  these  shortcomings  by  utilizing  alternative  sources  of  data.  The 
objective  is  to  improve  the  accuracy,  diversity  and  equity  of  lending  decisions  to 
marginalized  business  owners  of  small  firms  that  are  usually  underrepresented  in 
regular  financial  services.  Using  a  large  scale  data  containing  demographic,  financial, 
employment,  and  behavioral  characteristics,  this  study  will  utilize  enhanced  machine 
learning technologies with the help of gradient boosting and decision tree methods to 
assess  borrower  risk  of  default  based  on  a  multidimensional  applicative  nature.  The 
parameters  namely  education  level,  marital  status,  bracket  of  income  and  job  tenure 
are examined to reveal how they impact their viability of loan default. Those findings 
display  specific  trends:  the  more  highly  educated  individuals  the  longer  their 
employment  term,  and  the  stable  marriage  status,  the  less  likely  they  are  to  default, 
which proves the predictive qualities of using non-traditional factors to evaluate credit 
risks.  The  results  of  this  study  add  to  a  more  inclusive  credit  assessment  system 
because  they  indicate  that  the  alternative  data  points  can  be  used  to  reliably  predict 
credit worthiness. This study highlights the possibility of AI underpinning data-driven, 
fair  lending  platforms  and  decreasing  financial  exclusion.  In  addition,  it  promotes 
responsible AI, which entails that algorithmic decisions are explainable, ethical and do 
not  produce  systemic  bias.  This  study  would  contribute  to  the  discussion  of  financial 
inclusion  by  presenting  a  solution  that  gives  leeway  to  financial institutions,  financial 
innovators, and policymakers. Extending credit to small businesses increases revenue 
by  providing  lenders  with  different  data  options  informed  by  AI-driven  models  to 
recognize deserving credit applicants that may otherwise have been turned away. This 
increases  the  flow  of  capital  not  only,  but  enhances  growth  at  the  grassroots  level- 
which works in line with wider agendas of sustainable and inclusive financial growth.

---

<!-- PAGE 2 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

59

Keywords: Artificial Intelligence, Credit Scoring, Financial Inclusion, Small Business

Lending, Loan Default Prediction and Alternative Data Analytics.

I. Introduction

A. Background

The  importance  of  small  businesses  on  the  economy  of  the  United  States  cannot  be 
underestimated as they make up over 99 percent of all businesses and account nearly half for 
the  workforce  that  the  private  sector  comprises.  They  are  powerful  motivators  and  spur 
innovation,  employment  and  economic  resiliency  at  the  local  level.  Mainstream  credit 
systems  are  under-servicing  many  small  businesses,  especially  new,  minority-owned,  or 
located in low-income regions despite it being an important source of financial  liquidity to 
the businesses. Common financial institutions tend to consider them high-weighted because 
they  do  not  have  enough  credit  histories,  unreliable  income  stream,  or  lack  of  collateral. 
Such companies therefore have challenges in acquiring cheap financing which can be used 
to  increase  their  operations,  make  investments  to  freshen  up  to  new  technology  or  sustain 
themselves during economic adversities [1]. In most incidences, these businesses are funded 
through personal savings, informal lending or expensive short term loans, which may further 
add  to  such  asset  fragility.  The  financing  ecosystem  that  exists  is  not  supportive  of 
entrepreneurs working in arrangements that are not within the standard financial systems to 
the  degree  needed.  The  pursuit  of  the  structural  biases  in  lending  systems  has  increased 
disparities  on  access  to  capital  with  a  disproportionate  hit  on  women,  immigrants  and 
minority-owned  businesses  [2].  The  current  COVID-19  pandemic  demonstrated  the 
existence  of  these  disparities  since  numerous  underserved  businesses  could  not  access 
emergency funding because of the existing old or strict credit evaluation procedures. In this 
regard,  credit  assessment  models  in  credit  are  required  urgently  in  the  form  of  innovation 
and  inclusiveness  to  bridge  the  gap.  With  a  reconsideration  of  creditworthiness  evaluation 
methods, especially with the adoption of technology and alternative data, financial inclusion, 
entrepreneurship,  and  more  equitable  economic  development  within  the  small  business 
ecosystem of the United States can be achieved.

B. Drawbacks of the Traditional Credit Scoring

The  existing  world  of  credit  assessment  is  dominated  by  such  traditional  credit  scoring 
systems  as  FICO  and  Vantage  Score.  These  models  are  mainly  used  to  determine  credit 
worthiness of an individual or business depending on structured financial information, such 
as credit history repayment performance, amount of outstanding credit, the length of time in 
credit, the types of credits taken and any recent credit searches incurred [3]. Although such 
criteria work very well to assess the borrowers with known credit status, they are inadequate 
in  assessing  small  companies,  particularly  young  companies,  and  those  who  are  informal. 
Small businesses are not separating personal and business finances, do not pledge collateral 
or operate on a cash basis, and find it hard to produce such standardized data as traditional 
models  would  need  [4].  The  entrepreneurs  with  no  or  thin  credit  files  are  not  usually 
unjustly pinned, but they may still have a high repayment capacity or a steady business but 
the  traditional  model  does  not  see  it.  These  models  are  even  unacquainted  with  small 
business  operations  like  seasonal  income,  contract  based  work,  or  informal  credit 
relationships.  The  end  result  of  this  exclusionary  structure  is  that  underserved  business 
applicants  face  high  rejection  rates,  creating  financial  biases  deep  rooted  in  the  origin  or 
design of the scoring mechanism. Traditional scoring systems are often static and backward 
looking which does not offer much latitude to use near real-time or behavioral information

---

<!-- PAGE 3 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

60

that can be used to gain a more accurate picture of credit risk [5]. The dependence on strict 
parameters  opens  to  bias,  since  the  inhabitants  of  a  particular  group  (age  demographic  or 
income  level)  are  systematically  underrepresented  in  the  data  sets  against  which  these 
models are trained. These constraints reinforce the necessity of changing to more dynamic, 
inclusive, and contextualized manners of credit assessment that are able to help the variety 
of realities that U.S. small businesses seek refuge in.

C. Emergence of the Alternative Data in Finance

Upraising inequalities, the financial sector has availed over to alternative data as a source of 
information  to  quantitate  creditworthiness  especially  of  the  under-served  people  and 
businesses  by  the  classical  mechanisms  [6].  Alternative  data  can  be  described  as  non-
traditional measures of financial activity and soundness such as payment trends of rents and 
utilities,  cell  phone  use,  social  media  use,  online  shopping  habits,  history  of  business 
transactions,  and  work  or  academic  history.  These  pieces  of  information  give  a  fuller  and 
more comprehensive picture of the capacity and willingness of a borrower to pay off loans. 
Informal  small  businesses  and  those  that  thrive  on  gig  work,  or  those  that  cannot  access 
mainstream  financial  services,  alternative  data  therefore  provides  an  effective  means  to 
verify  their  credit  card  without  the  need  to  base  this  on  a  long  credit  history  or  collateral. 
Alternative data exploitation can make credit analysis less lagging and more segmented to 
reflect  more  appropriately  borrower  behavior  or  market  fluctuations  [7].  Advances  in 
technologies of aggregating data and open banking systems allow more efficient collection, 
processing,  and  securing  of  such  data  with  minimal  compliance  risk.  Increased  Approval 
Rates  and  Decreased  Default  Risk  among  under-served  communities  financial  institutions 
and  fintech  companies  have  started  to  include  alternative  data  to  calculate  their  risk  of 
borrowers,  bringing  more  of  them  access  to  credit  and  leading  to  lower  default  rates. 
Privacy, data quality, and algorithmic fairness should be considered in regard to the adoption 
of alternative data, as communication was perceived as a possible downfall of this potential 
[8].  The  systematic  application  of  alternative  data  sources  holds  the  great  promise  to  be  a 
democratizing force in enhancing access to credit and inclusive growth in the small business 
community in the United States.

D. The role of Artificial Intelligence

Artificial  Intelligence  (AI)  has  become  an  impressive  theme  throughout  the  financial 
industry, especially as the markets relate to risk management planning, fraud identification, 
and  customer  segmentation.  Within  credit  scoring,  AI  (and  Machine  Learning  (ML),  in 
general) allows us  to  come up with  new models  which are capable not  only  of processing 
large amounts of both structured and unstructured data but of detecting complex trends and 
efficiently  predicting  the  outcome,  in  comparison  to  the  traditional  ones. Contrary  to  rule-
based systems, AI models can learn using historical data in order to dynamically respond to 
changing behavior among borrowers and market conditions [9]. This is what qualifies them 
to  be  specifically  suitable  to  incorporate  alternative  sources  of  data,  like  the  employment 
history, the trend of transactions or even behavioral  sensations by digital platforms. Based 
on  these  data  inputs,  AI  driven  credit  scoring  algorithms  will  be  able  to  produce  more 
comprehensive, real-time, and contextualized  risk scores.  In the case of  underserved small 
businesses, these systems provide an opportunity to be judged fairly- not just based on strict 
credit scores, but on a wider set of variables that show better predictive abilities. Explainable 
AI approaches such as SHAP (SHapley Additive explanations) can be used to interpret the 
decision-making  process  of  the  model  and  be  transparent  and  compliant  with  regulation. 
Such  interpretability  is  needed  to  satisfy  stakeholders  with  increased  trust  in  terms  to 
minimize possible biased models [10]. Banks applied with the AI in credit scoring indicate 
better loan approvals, reduced default loans and better customer interaction. Deploying AI in 
a responsible way needs to deal with ethical implications of data privacy, data fairness, and

---

<!-- PAGE 4 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

61

algorithmic responsibility. When applied properly, AI can transform the credit systems into 
more  inclusive,  quantitatively-based,  and  adapted  to  peculiarities  of  the  microenterprises 
financial realities in the United States.

E. Research Problem

The access to credit by small businesses in the United States has remained a systemic issue 
among  under-resourced  small  business  owners  since  they  are  serviced  by  none  of  the 
traditional  credit  rating  systems  [11].  These  models  tend  to  dissociate  non-traditional 
borrowers  or  borrowers  with  limited  financial  histories,  thus  barring  equal  access  to 
financial applications and potential prosperity. Even though there is a range of different data 
and AI capabilities, credit scoring models that are robust, scale, and explainable to the needs 
of  the  small  business  borrowers  are  not  available.  This  study  aims  to  address  that  gap  by 
creating AI-driven credit scoring models that use alternative data to better predict the risk of 
loan  defaults,  increase  financial  inclusion,  and  enable  lenders  to  implement  more  accurate 
and equitable decisions.

F. Research Objective

The purpose of this  study is  to  generate AI-assisted credit scoring models  with  alternative 
data on underserved small businesses in the United States.

➢  To evaluate shortcomings of conventional credit scoring systems.

➢  As an inquiry into the possibility of using alternative data in calculating credit risks.

➢  To implement machine learning to cash loan default prediction.

➢  To measure the model performance on their accuracy and interpretability.

➢  To increase access to credit by businesses which have not got a good financial history.

➢  In  the  form  of  giving  something  back  to  society  to  ensure  that  it  is  beneficial  in

providing ethical, inclusive financial technology tools.

G. Research Questions

This  study  estimates  the  most  important  questions  regarding  AI-based  credit  scores  and 
alternative data:

1.  What  does  it  mean  to  exclude  small  businesses  when  it  comes  to  accessing  finances

through the models of a traditional credit process?

2.  Does alternative data help to increase loan default prediction accuracy?

3.  Which is the AI model that offers maximum discrimination and interpretability?

H. Significance of Study

This study is important in terms of financial inclusion and the role of artificial intelligence 
(AI) in credit risk assessment, which is rapidly expanding [12]. Conventional credit scoring 
models do not always reveal the maximum potential of the owners of small businesses who 
are not  always  served or adequately banked. This study shores up a major loophole in  the 
present-day  loaning  paradigm  by  creating  AI-based  credit  score  models  using  alternative 
data, including education status, marital status, levels of income, and repayment history. The 
results  would  provide  an  avenue  to  the  more  realistic,  fairer,  more  individualized,  credit 
assessment.  Not  only  does  this  create  a  more  likely  avenue  of  loan  approvals  to  small 
businesses that show no formal history of credit it lessens risk to the lenders as the capability 
to predict loan defaults is improved. In addition, the demographic and behavioral data helps 
to  minimize  systematic  biases  inherent  to  conventional  scoring  models  driving  a  more 
equitable financial ecosystem. The findings of the research enable the financial institutions

---

<!-- PAGE 5 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

62

to offer credit facilities to the high potential borrowers whose services have until then been 
out  of  reach  of  mainstream  credit  availability  [13].  Finally,  the  study  facilitates  economic 
growth since it allows small companies to obtain capital they require to develop, innovate, 
and hire new workers--and establish a new precedent on AI in financial services.

II. Literature Review

A. Traditional models of Credit Scoring: History and Constraints

The conventional credit scoring has always depended on the structured financial indicators 
in  determining  the  creditworthiness  of  a  borrower.  Some  of  the  important  considerations 
made  by  the  models  e.g.  FICO  and  Vantage  Score  are  payment  history,  amounts  owed, 
length  of  credit  history,  type  of  credit  used  and  new  credit  inquiries  [14].  The  models  are 
highly  widely  written  and  implemented  in  their  simplicity  and  scalability  and  their 
productiveness in high income lending markets that are structured. Their relevance to small 
enterprises  including  those  with  little  or  no  formal  credit  engagement  is  being  challenged 
more and more. A number of micro and start up business ventures are conducted informally 
with no distinct line between personal and business finances [15]. Therefore, they might not 
have  a  credit  record  to  the  signals  that  drive  the  conventional  scoring  systems.  Recent 
research  points  to  deficiency  of  such  models  in  capturing  real-life  business  environments 
especially  among  the  women/minority-owned  businesses  which  may  not  access  formal 
financial services. Critics claim that credit scoring is historical and that it is always late and 
reactionary,  is  mostly  dependent  on  past  records  and  does  not  take  cues  on  changing 
financial  behavior.  Various  documents  have  mentioned  that  these  systems  have  the 
socioeconomic  bias  system  at  their  core,  which  has  led  to  the  unfair  concentration  of 
borrowers of underserved groups. These are giving rise to  researchers and institutions that 
are  pursuing  more  holistic  credit  assessment  systems  that  look  into  the  future  [16].  As  a 
reaction  to  this,  a  growing  literature  is  devoted  to  improving  or  superseding  these  models 
with machine learning based systems that are capable of working with both structured and 
unstructured  information.  Although  regulatory  compliance  and  protecting  against  risks  is 
advantageous,  traditional  credit  scores  are  not  flexible  or  inclusive  enough  to  support  the 
financing  of  various  small  business  borrowers  and,  therefore,  innovation  in  the  segment 
would be necessary.

B. Evolution of Alternative Data in the Financial Services

The  concept  of  alternative  data  has  attracted  more  attention  over  the  past  several  years 
because of its potential to resolve the discriminatory aspects of the traditional credit scoring 
systems.  Alternative  data  can  be  defined  as  data  not  covered  by  conventional  financial 
accounting,  such  as:  payment  of  utilities,  history  of  rental  property,  use  of  social  media, 
behavior in online e-commerce stores and use of mobile phones.  The World Bank and the 
International Finance Corporation have found out that using alternative data when analyzing 
credit  risks  allows  enhancing  access  to  finance  by  a  large  margin,  particularly  in  the 
underserved population. Led by financial technology (fintech) companies, digital footprints 
are helping to fill information gaps and enable the borrowers who would otherwise be under 
financial  radar  (known  as  the  credit  invisible)  to  be  evaluated.  Alternative  data  has  been 
proved as predictive in academic research. As part of an illustration, research has affirmed 
that  paying  bills  on  rent  and  utility  on  time  are  good  indicators  of  financial  responsibility 
[17].  Other  scholars  have  tested  whether  mobile  wallet  usage,  geolocation  tendencies,  and 
even psychometric data, could serve to signal reliable creditworthiness. The following types 
of data sources  provide  a more detailed picture of a borrower in  terms  of his/her financial 
life,  stability,  and  personality.  In  a  growing  economy,  in  a  gig  economy  type  of  business 
model, the use of alternative data has been proven to be an invaluable addition to inclusive 
credit  assessment.  There  is  still  apprehension  about  the  quality  of  data,  standardization  of

---

<!-- PAGE 6 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

63

data  and  confidentiality.  There  is  no  regulation  on  the  use  of  alternative  data,  which  can 
cause both ethical and legal issues. Its strategic application in credit scoring has been on the 
increase largely due to the technological gains made in big data processing, API and cloud 
computing.  Literature  continues  to  provide  importance  over  the  use  of  alternative  data, 
exemplifying the democratizing of financial services amongst small businesses which do not 
have access to formal banking infrastructure.

C. Credit Risk Assessment with Machine Learning

Machine Learning (ML) techniques have been very useful in developing credit risk models 
and  presenting  new  features  to  these  models  such  as  the  capability  to  learn  non-trivial 
patterns in data, dynamic update capabilities, and non-linear relationships between variables. 
The Logistic Regression, Decision Trees, Random Forest, Gradient Boosting Machines, and 
Neural  Networks  are  four  other  algorithms  that  have  been  used  extensively  both 
theoretically  and  practically.  Such  models  have  exhibited  a  very  high  success  rate  as 
compared to  the use of  classical  methods of statistics  in  situations  where data is  large and 
wide [18]. A key benefit of ML is that it can consume and process alternative data sources in 
addition  to  traditional  metrics  and,  therefore,  produce  more  informative  insights  that  can 
result  in  more  individualized  risk  assessments.  Comparative  studies  that  have  been  done 
concerning ML models and the conventional credit scoring systems have all concluded that 
this  former  has  a  higher  accuracy,  low  false-positive  rates,  and  better  borrower  risk 
segmentation  [19].  The  Random  Forests  and  the  Gradient  Boosting  have  proven  to  be  the 
best  at  uncovering  loan  defaults  in  imbalanced  data.  In  addition,  methods  such  as  cross-
validation,  hyper  parameter  optimization,  and  ensemble  methods  have  been  employed  to 
maximize model performance in terms of robustness and generalization. Less interpretable 
Deep  learning  techniques  have  been  used  in  large  scale  lending  settings  with  potentially 
complex data about individual borrowers. Among the major criticisms of machine learning 
applied  to  credit  scoring  is  the  fact  that  many  machine  learning  models  are  considered  a 
black-box;  it  is  unknown  exactly  how  they  work.  Strict  regulatory  agencies  like  the 
Consumer Financial Protection Bureau (CFPB) insist on transparency and explain ability in 
credit made decisions. Due to this, interpretable ML techniques explain ability frameworks 
such  as  SHAP  (SHapley  Additive  Explanations)  and  LIME  (Local  Interpretable  Model-
Agnostic Explanations) received attention in recently published literature. On the whole, ML 
integration has made credit risk models to be more precise, customizable, and all-inclusive, 
particularly when dealing with non-traditional borrowers.

D. Small Business Credit Scoring using AI

Data scarcity, heterogeneity of business, and volatility in operations pose unique difficulties 
to  the  creation  of  credit  risk  models  in  small  business  lending.  These  businesses  are 
classically erroneously tabulated because they do not have regular documents or revenues; 
or, because of a lack of collateral [20]. As a result, researchers, and practitioners are paying 
an increasing amount of attention to AI-powered credit scoring along the lines that will be 
subjected 
to  different  small  business  finance  peculiarities.  Such  AI  models  can 
accommodate  more  input  variables  such  as  transactional  information,  cash  flow  trends, 
industry-specifics,  and  socio-psychological  indicators,  which  enables  them  to  have  a  more 
comprehensive indication of business credit-worthiness [21]. The latest studies have pointed 
to the favorability of AI models that minimize credit exclusion and improve credit approvals 
of  underserved  small  businesses.  To  illustrate,  fintech  marketplaces  like  Kabbage  and 
OnDeck  have  implemented  AI  to  automatically  evaluate  risk  using  indicators  of  business 
performance  in  real  time.  The  models  go  not  only  beyond  static  credit  history  to  include 
dynamics such as point-of-sale, online reviews, supply chain activities and so on. Scholarly 
research substantiates the idea that the AI models can better the historical scoring systems in 
small  business  scenarios  in  terms  of  providing  access  to  granular  segmentation,  consistent

---

<!-- PAGE 7 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

64

model updating, and increased processing speed. There continue to be issues around model 
validation, data privacy, and fairness. The small businesses are cautious about the way their 
data is gathered and utilized and Lenders need to ensure that they do not introduce implicit 
bias into models [22]. Regulative and ethical systems are hence essential in the process of 
implementing  AI.  All  in  all,  the  existing  literature  substantiates  the  promises  of  AI-based 
credit  scoring  as  a  channel  to  the  establishment  of  equitable,  data-driven  lending  to  small 
businesses that cannot be missed in a traditional approach.

E. Financial Inclusion and the Under-Served Market

Financial  inclusion  means  the  prevention  and  parity  of  the  chances  to  use  the  financial 
services.  The  reports  produced  by  the  international  authority  bodies,  like  the  World  Bank, 
IMF and the Federal Reserve, indicate that millions of small enterprises in the United States 
have  been  left  behind  in  the  major  financial  institutions  [23].  This  ostracizing  is  due  to 
stringent credit standards, geographical inaccessibility, cultural and linguistic difference and 
absence of institutional relationships in banking. Such elements affect the businesses owned 
by  women,  minorities,  and  those  located  in  rural  areas;  commonly  known  as  the  credit 
invisible. Controlling studies have the capacity to verify that increased accessibility to credit 
has the effect of increasing the business survival level, employment and economic strength. 
Other  credit  scoring  options  such  as  AI-  and  alternative  data-driven  ones  are  increasingly 
being seen as vehicles of financial inclusion. Such models allow new entrants into the credit 
system  without  undermining  risk  standards  since  redefining  [24].  Some  case  studies  even 
attract  a  success  story  whereby  smaller businesses were  able to finance loans available on 
mobile  transaction  records  or  peer  ratings  as  opposed  to  the  traditional  credit  files.  In 
addition, a recent state of the literature focuses on the fact that inclusive credit models are 
not just socially beneficial, but commercially beneficial as they identify a huge underserved 
market. Responsibility has to balance inclusion [25]. There exists the possibility that a badly 
formed  design  should  result  in  excessive  indebtedness  or  discriminatory  behavior. 
Therefore, scholars attach great significance to the concept of fairness audits, transparency, 
and  user  education  as  part  of  any  financial  inclusion  plan.  The  literature  argument  that 
modern, responsible use of AI-driven  credit scoring  has the potential to  even the financial 
playing field  in  the U.S.  small  business  market  and create a more just economy  is  hard to 
refute.

F. Empirical Study

The  article  by  Richa  Lomas  and  Reeta  called  AI-Driven  FinTech  Solutions  to  Financial 
Inclusion: A Study on Empowerment of MSME Sector empirically discusses the value of AI 
technologies  in  ensuring  financial  inclusion,  especially  to  the  Micro,  Small,  and  Medium 
Enterprises  (MSMEs),  which  have  little  access  to  formal  banking  systems.  The  research 
reveals  how  the  AI-driven  FinTech  platforms  use  machine  learning,  analytics  of  data,  and 
alternative  data  sources  to  improve  credit  evaluation,  risk  analytics  and  personalisation  of 
their services to the MSMEs. The AI systems will offer more comprehensive, equitable, and 
reachable financial solutions since they address the shortfalls of conventional credit scoring 
systems, including the lack of formal credit histories. The paper presents some of the major 
advantages including enhanced availability of cheap credit, enhanced efficiency, and growth 
of  operations  to  unserved  areas  [1].  It  recognizes  the  existence  of  vital  challenges  such  as 
data  privacy  issues,  adherence  to  regulations,  and  digital  literacy  gap  among  owners  of 
MSMEs.  The  empirical  evidence  can  be  viewed  as  the  premise  behind  this  study,  which 
promotes the adoption of AI-driven credit scoring solutions to help small business borrowers 
and  achieve  inclusive  economic  development.  The  article  is  a  good  source  of  reference  in 
appreciating  the  practical  effect  of  AI  among  the  underserved  participants  in  the  financial 
ecosystem.

---

<!-- PAGE 8 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

65

In  the  article  by  Ga  Young  Jang,  Hyoung  Goo  Kang,  James  Park,  and  Hyung-Suk  Choi 
titled  AI-Driven  Credit  Scoring  and  Market  Transformation:  How  ACSS  Reshapes  SME 
Financing,  Firm  Strategy,  and  Regulatory  Boundaries,  the  authors  argue  an  empirical  case 
regarding the remaking of the market by alternative credit scoring systems (ACSS), driven 
by AI and big data, which have provided the potential to transform the funding structure of 
small  and  medium-sized  enterprise  (SMEs).  The  paper  examines  the  use  of  ACSS  by 
platform  companies  to  succeed  within  harsh  regulatory  frameworks  deploying  credit  in 
underbanked  small  and  medium-sized  enterprises  and  driving  inclusive  financial  systems. 
These systems use non-traditional data points and AI algorithms to provide better estimates 
of creditworthiness,  and  as a  result even businesses  with  little historical  financial data can 
take out external capital to drive growth [2]. The study brings out the instrumental usage of 
the platform companies as the driver of the regulatory reforms and competitive redrawing of 
industry  borders.  The  present  research  is  supported  by  these  empirical  findings,  which 
proved the necessity of introducing AI-based credit models because they not only optimize 
the  SME  financing  process  but  become  drivers  of  market  and  regulatory  changes  in  the 
entire  National  Market.  The  article  is  a  good  resource  to  the  policymakers,  financial 
institutions  and  developers  of  technology  who  aim  at  attaining  a  balance  between 
innovation, management of risk, and economic inclusion. It supports the significance of AI 
in supporting the sustainable empowerment of the SME and creating a financial system that 
is more favorable to the equal importance of human beings.

In  the  article,  The  Role  of  Data  Analytics  in  Enhancing  Financial  Inclusion  in  Emerging 
Economies by Oluwabusayo Adijat Bello, the author highlights the role that data analytics 
can play in reducing the gap between financial inclusions across emerging economies. Using 
alternative data sources to detect underbanked populations such as mobile usage patterns and 
online payments habits, financial institutions are able to detect them better, optimize credit 
scoring and organize financial services to a wider range of socioeconomic needs. The study 
is  specifically  applicable  to  the  present  study  in  terms  of  disclosing  the  benefits  of  data-
driven  approaches  to  fostering  inclusivity  by  breaking  the  existing  structural  boundaries 
such as remote geographical location and the absence of an established formal credit profile. 
The examples of effective implementations,  described by Bello, such as Kenya M-Pesa or 
the  Indian  Aadhaar-enabled  digital  lending  provide  a  tangible  example  of  what  analytics-
driven  innovation  is.  The  paper  discusses  such  essential  dilemmas  as  data  privacy, 
regulatory restrictions, and infrastructure shortages that have to  be negotiated to  guarantee 
sensible  and  sound  deployment  [3].  The  combination  of  upcoming  technologies  like  AI, 
blockchain, and IoT reflects a vision of the blueprint of an inclusive financial ecosystem in 
the  future.  In  general,  the  insights  that  Bello  presents  in  his  work  help  to  understand  how 
data analytics allows institutions to create fairer financial systems, which is compatible with 
the larger initiative to decrease poverty and achieve sustainable development.

The  article  by  Elijah  Nguyen,  The  Role  of  Big Data  and  AI  in  Real-Time  Credit  Scoring, 
provides an in-depth investigation of the changes that the modern financial system faces due 
to  the  advent  of  new  technologies,  especially  those  related  to  real-time  credit  scoring. 
Nguyen  stresses  that  the  current  systems  of  credit  scorecards,  e.g.,  based  on  FICO  scores, 
are insufficient in assessing people or SMEs with no formal credits. With input of big data 
sources, such  as  online  behavior, digital transaction  history, and other alternative financial 
measurement  sources,  AI-based  models  can  provide  more  rapid  and  comprehensive  credit 
ratings.  Such  models  especially  that  based  on  machine  learning,  further  improve  risk 
prediction  accuracy  and  the  models  self-improve  themselves  using  iterative  learning. 
Notably, the article falls in line with the stated goals of this study by showing how big data 
and  AI  have  already  managed  to  fill  historical  inclusion  gaps  in  the  world  of  finance  [4]. 
Nguyen critically brings up some of the ethical and regulatory issues that are associated with

---

<!-- PAGE 9 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

66

the  implementation  of  AI  within  financial  decision-making  including  privacy  of  data, 
fairness of algorithms, and transparency of models. His observations serve as an appropriate 
background  to  the  idea  of  how  the  use  of  advanced  analytics  tools  can  transform  credit 
access  of  the  marginalized  group  enabling  as  well  to  draw  attention  to  the  necessity  of 
responsible  innovation.  This  piece  of  work  makes  a  significant  contribution  to  continued 
scholarly and practice-related discourse concerning the usage of technology to create more 
equitable, efficient and speedier credit systems around the world.

In  the  chapter  FinTech  and  Artificial  Intelligence  to  Sustainable  Development  by  David 
Mhlanga,  the  nexus  of  financial  innovation  and  alleviation  policy  from  the  prism  of  the 
United Nations Sustainable Development Goals (SDGs), namely SDG 1: ending poverty, is 
revealed. Mhlanga gives an emphasis on how FinTech and artificial intelligence (AI) may be 
critical  towards  the  achievement  of  inclusive  growth  and  economic  empowerment  in 
developing  region.  Using  the  capabilities  of  an  AI-enabled  tool,  the  chapter  explains  the 
means in which underserved populations can receive greater access to financial services and 
such  financial  tools  as  digital  wallets,  microloans,  and  mobile  banking  applications.  It  is 
important  to  note  that  these  technologies  have  encouraged  not  only  a  diminution  of  the 
drawbacks attached to the traditional banking system, namely the physical distance involved 
and the bureaucratic red tapes, but simplified the process of sending aid and raising financial 
literacy [5]. The chapter questions how, with the incorporation of AI FinTech solutions, real-
time  credit  evaluation  and  fraud  detection  will  be  possible  making  lenders  comfortable 
funding  small  and  mediocre  enterprises  (SMEs)  which  are  the  key  to  the  local  economic 
growth.  In such innovations,  FinTech acts  as a source of employment, wealth-distribution, 
and social mobility. Mhlanga seeks long-term cooperation with governments, companies in 
the  field  of  technology,  and  global  organizations  to  introduce  these  technologies  in  a 
controlled,  ethical,  secure,  and  inclusive  way.  His  perspectives  give  formidable  theoretical 
and practical support to how AI-based financial systems can eliminate poverty and promote 
sustainable development.

III. Dataset

A. Screenshot of Dataset

---

<!-- PAGE 10 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

67

B. Dataset Overview

The data used in the study is a multidimensional and exhaustive set that entails credit risk 
scoring  with  particular  emphasis  on  small  businesses  borrowers’  loan  lending  model.  It 
embraces  a  wide  array  of  variables  that  cross  economic,  demographic,  and  behavioral 
variables  that  are  linked  with  creditworthiness  and  default-risk.  The  most  important 
characteristics of the data will be the age of the borrower, gender, education level, marital 
status,  employment  types,  annual  income,  and  amount  of  loan,  interest  rate,  length  of  the 
loan,  credit  history  status,  the  number  of  previous  defaults,  and  the  current  default  status. 
The  sample  size  in  the  dataset  is  thousands,  which  will  guarantee  a  good  number  of 
observations  to  be  used  to  train  the  models,  validate,  and  evaluate  the  performance.  It  is 
realistic in terms of diversity in borrowers as it includes both the traditionally employed and 
self-employed  individuals,  a  broad  range  of  the  various  income  brackets  and  educational 
levels. Data structure is clean, well-labelled and can be used in machine learning tasks, and 
the minimal  missing values with  the existence of categorical  variables which are correctly 
encoded [65]. The selection of each variable was made in a way that they could be relevant 
to modeling of credit risk and statistical methods of normalization and correlation analysis 
were  used  to  analyze  data  distribution  and  important  predictive  characteristics.  Using 
Tableau and Python allowed determining the important trends as well, high default rates on 
specific  levels  of  education  or  employment  status  or  having  an  uneven  distribution  of 
income  among  the  types  of  the  borrowers.  Such  an  inclusion  of  the  defaulted  and  non-
defaulted  cases  was  used  to  construct  balanced  predictive  models  and  evaluate  bounded 
classification  accuracy  in  the  research.  The  richness  and  relevance  of  the  dataset  not  only 
facilitated the construction of rigorous algorithmic models, but potentially rich insights with 
regard to socioeconomic trends on the loan repayment behaviors. It is thus especially useful 
in  the  development  of  inclusive  credit  scoring  models  that  will  be  sensitive  to  the  lived 
experience of underserved borrowers.

IV. Methodology

This  study  used  a  quantitative  research  method,  through  AI  and  machine  learning 
application,  to  investigate  the  tendency  of  loan  defaults  by  small  business  loan  recipients. 
The data follows a credible financial database whose data were preprocessed to deal with the 
missing data, categorical variable encoding, and normalization of numerical variables [26]. 
Decision tree, logistic regression, and random forest are predictive models that were trained 
and  validated  in  their  support  of  assessing  default  risk.  Tableau  and  Python  are  data 
visualization tools that were applied to find a relationship amongst the variables; education, 
marital  status,  employment  and  income.  To  determine  whether  model  performance  was 
robust  and  predictively  fair,  accuracy,  precision,  recall  and  F1-score  were  used  to  assess 
performance.

A. Research Design

The research employed in this study is of a quantitative exploratory design to investigate the 
interaction  between  credit  scores,  default  rates  and  interest  rate  distributions.  The  ultimate 
goal  is  to  uncover  quantifiable  trends  and  information  with  guided  data  found  on  lending 
websites [27]. Quantitative research can easily be analyzed due to statistical analysis, and it 
is thus easy to establish relationships, trends, and differences in variables like credit scores, 
annual  income,  loan  amounts  and  the  interest  rate.  The  exploratory  aspect  enables  one  to 
complete  the  study  in  the  locations  where  there  is  little  research  or  pre-determined 
hypotheses  to  find  the  unknown  or  unexpected  connections  in  the  data.  This  study  design 
was especially appropriate since the research not only aimed at testing theories, but it aimed 
at creating other ideas. Using this methodology we can investigate various aspects that shape 
the behavior of the borrower and the consequences of a loan [28]. These data were analyzed

---

<!-- PAGE 11 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

68

with data visualization, statistical description, and correlation. Combination of tools such as 
Python,  Excel,  and  Tableau  was  applied  so  as  to  improve  the  strength  of  the  approach. 
Python allowed the extensive numerical analysis, whereas Tableau provided the possibility 
of pattern identification by visualization. Excel provided the chance to manage the primary 
data and conduct rapid reviews. All in all, the design is clear, objective and replicable. The 
structure can be used in future predictive modeling or machine learning related to financial 
decision-making as it has a solid base.

B. Data Collection

This study used data on a publicly available lending dataset, entailing detailed information 
of  borrowers  (credit  scores  and  interest  rates,  annual  income,  loan  amounts,  co-signer 
information,  and  the  purpose  of  loans).  This  information  consists  of  thousands  of  loan 
application data, which provides a sample of different loan applicant profiles and risk. The 
process  of  collection  commenced  with  the  importation  of  the  data  to  the  Microsoft  Excel 
program  to  observe  the  structures,  degree  of  completeness  and  simple  formatting.  This 
permits preliminary cleaning- elimination of doubles, resolution to missing values, and input 
of  inconsistent  entries  [29].  Then,  the  cleaned  data  was  sent  to  Python  and  Tableau  and  a 
more  in-depth  analysis  was  done.  Advanced  filtering,  transformation,  and  exploration  of 
data  were  carried  out  in  Python  through  libraries  such  as  Pandas.  Interactive  visual 
dashboards capable of absorbing more patterns  were  created on Tableau. All  records were 
reviewed with the aim of ensuring that they fell within the objectives of the study, especially 
the attributes such as credit score grouping, default record and the loan classification [30]. 
The data further got arranged in a way that they could be subdivided, i.e., evaluation could 
be performed between loans with or without a co-signer or how the effect of income level on 
interest  level  worked.  The  data  collection  protocol  focused  on  reliability,  reproducibility, 
and moral responsibility since all the information was anonymized and applied to academic 
learning and analytical aspects only.

C. Data Preprocessing

Preprocessing of the data helped to verify the quality, consistency, and relevance of the data 
that  was  to  be  analyzed.  The  first  one  was  locating  and  manipulating  data  that  was  not 
present. Null values in unimportant fields were dropped, whereas the missing/ invalid values 
in important/ key variables like the credit score and interest rate were not dropped to retain 
large  missing  value  entries  [31].  Outliers,  i.e.,  unrealistic  amount  of  income  or  loan  being 
negative would skew any result of the analysis, were removed from the dataset. In python, 
pandas  and  NumPy  were  used  to  do  preprocessing,  in  which  normalization  and  encoding 
transformation  were  performed.  Categorical  fields  such  as  the  loan  purpose  were 
transformed to numbers using label encoding that allowed the correlation to be determined. 
Credit scores became categorized into ranges such as Poor, Fair, Good, and Excellent) that 
could easily be visualized and contrasted. Likewise, the annual income was segmented into 
brackets to find out patterns among income brackets. In Tableau, it used calculated fields in 
order to segment and aggregate variables in the form of visual grouping. They filtered and 
sorted  the  data  so  that  data  that  was  not  relevant  such  as  business  loans  or  missing 
applications  were  missing  [32].  Preprocessing  procedures  made  the  data  to  be  correct, 
complete  and  fit  to  further  statistical  and  graphic  analysis.  This  intense  procedure  gave  a 
good  basis  to  develop  insights  and  recognize  the  trends  and  reduce  errors  during  later 
development of results interpretation.

D. Analysis Techniques and Tools.

The  study  involved  the combination  of  Excel,  Python,  and  Tableau  to  process  and  thus  to 
visualize the dataset. All the tools had their own contribution to the purposes of the research. 
The first step was the importation of data and generation of summary statistics with the help

---

<!-- PAGE 12 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

69

of Excel in order to obtain quick visualizations [33]. It enabled rudimentary sorting, filtering 
and  producing  pivot  tables  in  order  to  determine  distributions  by  borrower  category.  The 
deeper analysis engine was python. The data was investigated via the correlation matrices, 
regression functions, and clustering operations with the use of libraries, Pandas, Matplotlib, 
and  Seaborn.  As  an  example,  a  correlation  heatmap  was  made  to  comprehend  the 
interconnection  of  interest  rate  and  credit  score  with  line  plots  demonstrating  directional 
movement among brackets of scores [34]. The discussions about default rates in dependence 
on income and the co-signer presence exist with the help of Seaborn which helped to create 
thoughtful  scatter  plots.  Dashboards  that  were  visually  intense  were  developed  through 
Tableau. Using a drag-and-drop with an intuitive interface, Tableau allowed dynamic filters 
and  dashboard  designs  that  could  display  the  variations  in  the  interest  rates,  loan  purpose 
and the risk profiles of the borrowers. It was able to provide depth and clarity in the analysis 
due  to  integration  of  these  tools.  It  gave  us  the  possibility  to  analyze  raw  data  multi-
dimensionally,  synthesizing  numbers,  statistics,  and  graphical  views.  This  mix-up  of  tools 
increased the interpretability and reliability of the final finding of the research.

E. Data Visualization Method

Data  visualization  systematically  entered  into  a  central  aspect  of  this  research  because  the 
insights  of  the  large  sets  of  data  were  translated  into  meaningful  patterns  and  trends  [35]. 
With  Tableau,  different  types  of  analysis  were  visualized  to  help  in  analysis  such  as  bar 
graphs,  scatter  plots,  lines  graphs,  and  histograms.  The  intended  goal  behind  the 
visualization  strategy  was  to  ease  the  comprehension  of  complex  relationships  especially 
one  that  involved  multivariate  such  as  credit  score,  default  rate  and  interest  rate  [36].  The 
credit scores were entered in categories and colored to show how various brackets affected 
interest  rates  and  the  chances  of  getting  loans  based  on  them.  The  existence  of  the 
correlations between default rates and co-signer  status  or income level  was pointed out  by 
scatter plots. The line graphs presented the trend of the decrease or increase in the interest 
rates on the basis of credit score band. The usage of interactive filters on Tableau dashboard 
enabled adding the option to narrow down on a specific subgroup of individuals having co-
signers or a loan purpose. Such dynamic graphics were complemented by Matplotlib-based 
and Seaborn-based plots generated in  Python,  in particular regression lines and correlation 
matrices [37]. The visualization plan did not only add beauty to the visualization of data but 
made  it  easy  to  interpret.  It  allowed  readers  and  stakeholders  to  get  the  essential  insights 
without spending a lot of time working through the data presented in raw numerical forms. 
There was an emphasis of insights and relationships when using the visualization approach 
as it enhanced the presentation and impact of the research.

F. Ethical consideration and limitations

Ethical  integrity  was  a paramount utmost  requirement that took  priority in  this research in 
handling and analysis of data. Any data employed was anonymized and obtained through a 
publicly available database, so that no personal identifiers were in the data. The research did 
not involve any discriminatory profiling because the variables used were only numeric and 
categorical  and  did  not  include  the  concept  of  profiling  using  different  factors  like  color, 
religion,  etc.  As  to  limitations,  the  data  represent  the  history  of  trends,  and  it  might  not 
measure both the current shifts in the economy and the new lending policy alterations [38]. 
Variables such as employment history of the borrowers or macro-economic factors have not 
been discussed that could come into play in risk assessment of credit. It is restrictive in the 
sense  that  the  data  used  is  not  dynamic;  in  other  words,  it  is  not  updated  in  real  time. 
Nevertheless,  the  limitations  notwithstanding,  the  methodology  used  retains  its  value  and 
applicability when it comes to underlying ideas and can be used on the basis of more recent, 
and comprehensive data.

---

<!-- PAGE 13 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

70

V. Result

The findings of this study present important findings regarding lending patterns of this group 
of small business borrowers with focus on the demographic and socio-economic factors. The 
borrowers of lesser education status, single and with less job tenure had higher probability of 
defaulting [39]. In the visual analysis, it was stressed that employment type, income level, 
and  repayment  behavior  were  strongly  associated  with  each  other.  The  results  affirm  the 
successfulness  of  AI-amplified  credit  models  incorporating  variations  of  non-conventional 
information inputs. With these insights, it allows lenders to make a better assessment of risk 
and support financial inclusion by financing the small firms, which fall through the cracks of 
the traditional credit scoring model.

A. Default Rates Analysis by Employment Type

Figure 1: This image displays the average default rate per employment type according to 
four employment categories

Examining the relationship between employment type and default risk is important to ensure 
the  inclusiveness  of  credit  scoring  models,  particularly  among  the  small  business  owners 
that are underserved financially.  As shown in  Figure 1, the average percentages of default 
occurred in four types of employment which included Full-time, Part-time, Self-employed, 
and  Unemployed.  This  observation  proves  in  the  analysis  that  the  employment  status  can 
determine  and  contribute  to  the  credit  risk  greatly,  explaining  why  artificial  intelligence-
enabled credit score systems  need to  consider other employment-related  assets. As seen in 
the  chart,  the  highest  average  level  of  default  is  among  unemployed  people,  amounting  to 
that of 0.14. Understandably, this is the case given that unstable income has a direct impact 
on the capabilities of an individual to repay debt. Close behind are part-time workers with an 
above average default rate of around 0.12 that has been attributed to the instability of their 
income  and  earning  potential  in  comparison  to  the  full  time  parties.  Interestingly,  self-
employed  people  have  relatively  high  default  rates  (~0.115)  indicating  that  despite  having 
income  streams,  the  volatility  and  unreliability  of  entrepreneurship  may  affect  their  credit

---

<!-- PAGE 14 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

71

worthiness.  The  average  default  rate  is  the  lowest  among  full-time  employees  but  a  little 
more than 0.10. This means they are in more secure financial status and stability that makes 
them reliable lending in the eyes of lenders. This reflection makes it clear that the tendency 
toward  binary  measures  of  employment  obscures  the  issue  and  instead  there  is  a  need  to 
examine the quality of employment, stability of incoming, and the kind of self-employment 
[40]. The use of such granular data by AI models allows a better separation of risk profiles 
and  a  decreased  level  of  bias  against  self-employed  or  informally  employed  people.  This 
further confirms why alternative data plays a vital role in making credit more democratic by 
paying  attention  to  the  idiosyncratic  financial  circumstances  of  small  business  owners  of 
varied employment statuses.

B. Credit Score Analysis by Marital Status

Figure 2: This image displays the mean score of credit rating according to marital status 
based upon three specific categories

Figure  2  shows  the  mean  credit  score  divided  by  marital  status  with  three  attributes  as 
Divorced,  Married  and  Single.  In  both  conventional  and  alternative  credit  ratings,  credit 
score  is  an  important  parameter  that  highlights  the  capacity  and  the  possibility  that  an 
individual is best able and most likely to repay the money borrowed. The knowledge about 
the effect  of marital  status on credit scores may  help  to  optimize AI-related credit scoring 
algorithms  and  the  identification  of  possible  culturally-based  biases  of  credit  scores 
analytical tools. The chart shows that there is a slight difference in the means of the average 
credit scores of the three marital statuses where divorced people have the highest mean score 
of  about  574.8,  followed  by  married  (about  574.2)  and  single  (573.6).  Although  the 
difference  is  somewhat  minimal,  the  persistence  of  better  credit  scores  of  divorced  and 
married  people  based  on  current  trends  over  single  people  might  be  an  indication  of  the 
stabilization effect of joint financial commitments or long-term financial behavior developed 
within  a  marriage.  Therefore,  one  should  remember  that  marital  status  can  be  used  as  a 
proxy  indicator  of  other  financial  variables  like  there  may  be  two  incomes  of  households, 
two  credit  accounts,  or  varied  amounts  of  debt  accrued  by  individuals.  The  behavioral

---

<!-- PAGE 15 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

72

patterns represented by these nuances may not be obvious in the conventional frameworks 
but  may  be  more  effectively  measured  with  the  help  of  the  AI-powered  solutions  that 
evaluate a wider range of the behavioral and transactional data. In the small business lending 
point  of  view,  particularly  with  reference  to  the  low-end  financially  underserved  groups, 
extreme dependency on a marital status when making credit decisions can continue to cause 
inequitable  discriminations.  Consequently,  marital  status  should  be  added  to  the  list  of 
contextual aspects of the AI models but should be mixed with alternative data that is more 
dynamic  to  achieve  a  more  fair  and  precise  scoring  [41].  This  number  supports  the 
importance of thoughtful design of the AI models in which parameters such as marital status 
are computed with a combination of other signals and not individually.

C. Average Income Distribution by Income Bin and its Analysis

Figure 3: This image represents average income over income bins of increasing income, 
up to 150K from 10K

Figure 3 shows the mean income by the different income bins, which provides a micro level 
look  at  income  distribution  among  people  within  the  dataset.  The  horizontal  axis  provides 
the  segmented  delivery  of  income  (bins)  between  $10K,  up  to  150K,  whereas  the  vertical 
one indicates the average income on the same receiving scale. The graph shows that there is 
a definite and linear upward slope on the level of income which implies that the data is well-
organized and distributed equally among the classes in terms of the economy. The income 
levels  start  with  a  minimum  of  around  15260  dollars  and  they  progress  to  around  149834 
dollars representing the whole picture of economic diversity- through low income earners to 
high  earners.  To  come  up  with  inclusive  AI-powered  credit  scoring  models,  especially  in 
underserved small enterprises in the U.S., this type of distribution is critical since it prevents 
the training data set to be biased in favor of a specific economic segment. One important fact 
that can be observed in this figure is that the increment in income is predictable and there are 
no  inscrutable  outliers  or  noise  in  the  data  of  the  income.  Income  is  one  of  the  basic 
determinants of the ability to repay loans in the case of small businesses in terms of building 
a model of credit. The use of income alone is always misleading; this is particularly relevant

---

<!-- PAGE 16 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

73

in  the  case  of  individuals  who  are  self-employed  or  micro-entrepreneurs  because  their 
income  might  not  be  constant  but  steady  in  a  long-lasting  period.  Consequently,  this 
visualization supports the idea that to improve the ability to assess the financial stability of 
people  whose  incomes  are  not  steady  to  formal  data,  it  is  important  to  use  nontraditional 
indicators,  which  can  be  transaction  history,  digital  activity,  or  payment  of  utilities,  that 
would  be  more  relevant  to  the  financial  trustworthiness  of  people  with  irregular  formal 
income. Figure 3 evidences the argument in the paper that, as critical as income may be, it 
must be put into perspective with  other wider behavioral  information  to achieve equitable, 
more accurate AI-powered credit scoring.

D. Average Loan Amount, and Defaults by Loan Purpose Analysis

Figure 4: This image presents a comparison of the mean loan and the defaults with 
different loan

Figure  4  is  the  comparative  study  of  average  loan  amount  and  number  of  defaults  with 
respect  to  various  loan  purposes,  which  are  Auto,  Business,  Education,  Home  and  Other. 
The blue bars show the average of loan amount given per purpose whereas the orange bars 
show  the  amount  of  defaults  given.  This  two-visualization  gives  insights  on  lending 
behavior  or  default  risks  according  to  different  classifications  of  financing.  Based  on  the 
chart, it is noted that the average loan amounts tend to remain basically the same across the 
types of loans regardless  of the intended use of $127,000 which implies standardized loan 
offering  regardless  of  the  type  of  loan  sought.  The  differences  in  absolute  height  of  the 
default rates are more discreet though meaningful in respect to the context. Business loans 
and auto loans have a little more default numbers than other types of loans such as education 
loans or home loans. This would be due to the nature of the business of smaller companies 
which  tends  to  be  susceptible  to  any  changes  in  the  market,  minimal  cash  reserves,  or 
unstable sources of income [42]. On the same note, auto loans might cater to a more diverse 
group  of  people  on  credit,  such  as  those  of  low  credit  rating.  Education  and  home  loans, 
have much lower default rates perhaps due to the fact that these types of loans are usually 
linked  to  longer  term  investments  and,  perhaps,  a  more  strict  vetting  process,  or

---

<!-- PAGE 17 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

74

collateralizing.  The  rest,  labeled  as  other,  does  not  have  its  name  defined  but  is  in  the 
moderate  range  in  terms  of  the  amount  of  loan  and  the  number  of  defaults.  Using  this 
visualization,  one  can  emphasize  the  role  of  loan  purpose  as  a  predictive  element  in  AI-
enhanced credit scoring systems. Knowledge of the risk behavior of select loan purposes can 
greatly  enhance  the  default  prediction  model  and  allow  the  lending  programs  to  be 
customized to suit the underserved areas of small business. 
E. Evaluation of Marital Status by Average Debt to Income Ratio

Figure 5: This image presents the mean debt-compared to-income proportion by marital 
status 
The  average  Debt  to  Income  (DTI)  ratio  is  displayed  as  per  each  marital  status,  namely, 
Divorced,  Married,  and  Single  which  are  presented  in  Figure  5.  DTI  ratio  is  a  significant 
financial  measure  which  is  applicable  in  credit  scoring  and  loan  underwriting  because  it 
shows  the  ability  of  a  borrower  to  repay  his  monthly  debts  based  on  his  income.  A  thus 
lower DTI is usually the sign of healthier financial stability and less chances of default. The 
average of the DTI ratios of all incarnations of marital status are quite near to each other as 
depicted in the chart: it is between approximately 0.499 and 0.501, thus indicating a slight 
difference  in  financial  leverage  among  members  of  the  different  demographic  groupings. 
Between the labels, married people have the highest average of DTI ratio, which is slightly 
over  0.501  followed  by  single  and  divorced.  The  low  difference  between  the  three  groups 
means  that  maybe  marital  status  is  not  a  strong  discriminator  of  the  DTI  behavior  in  the 
dataset. Nevertheless, even minor variations in DTI may make physical implications when it 
is scaled to a large scale credit modeling. In this case, married people could have a higher 
financial  liability  because  of  joint  liabilities  i.e.  mortgages,  family  costs,  and  hence  their 
debts  could  be  more  but  their  income  otherwise  could  be  the  same  or  higher.  Conversely, 
divorced  persons  could  have  gone  through  a  reorganization  of  their  finances  after  divorce 
that could decrease their debts or distribute them. The use of marital status DTI in AI-based 
credit  scores  can  be  used  to  provide  more  individual  and  equitable  experiences.  This  is 
consistent  with  the  purpose  of  the  study  of  finding  inclusive  models  describing  their  data 
points in a more subtle way of focusing on alternative data besides the conventional credit 
history.

---

<!-- PAGE 18 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

75

F. Defaults by Education and Marital Status Analysis

Figure 6: The image illustrates how the defaults are distributed according to education 
and marital status

The focus on the demographics of loan defaults has found its expression in the figure of 6 
that contains the detailed breakdown of loan defaults by education level  and marital status 
providing  important  information  on  the  impact  of  demographics  on  the  behavior  of 
borrowers in terms of credit. Education levels in the graph have been grouped under High 
School, Bachelor, Master and PHD and the marital statuses under the categories Divorced, 
Married and single. As it can be recognized, high school completions, particularly those who 
had  become  single  or  divorced,  are  the  biggest  source  of  defaults,  and  this  signifies  the 
increased risk of lending credits to individuals with low levels of schooling. Conversely, the 
rate of defaults is significantly lower among those with Bachelor and Master degree levels 
thus giving a positive relationship between higher education and being more responsible in 
handling their money. The group that shows the lowest rates of defaults is the group that has 
PhDs, especially in the age category of married and divorced, to prove the point that senior 
levels  of  education  lead  to  improved  repayments  dependability.  In  all  categories  of 
education, the single individuals always have the highest default rate whereas the divorced 
people  will  have  higher  default  than  the  married  borrowers,  and  there  may  be  several 
reasons  as  to  why  the  married  ones  have  lower  rates  of  defaulting  such  as  they  have  the 
mutual income or they are more economical. The given demographic trends are necessary to 
optimize  the  AI-based  credit  scoring  system,  and,  particularly,  focus  the  latter  on  small 
business borrowers in the underserved segment. Incorporation of features like education and 
marital  status  not  only  increases  the  effectiveness  of  prediction,  but  directly  helps  achieve 
more inclusive and equal lending frameworks [43]. With the acknowledged mixed impact of 
education  and  personal  stability,  the  financial  institutions  will  be  able  to  understand  the 
reliability of borrowers better than the standard metrics of credit levels. This method ushers 
in smarter, fairer and more personified decision-making on credit, leading to wider access to 
credit options.

---

<!-- PAGE 19 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

76

G. Comparing Total Loan Amount based on Loan Purpose and Co-Signer Status

Figure 7: This image demonstrates the cumulative value of loans by purpose of the loan 
and co-signer status

Total amount of the loans disbursed during the year with regard to different loan purposes 
broken  based  on  the  presence  or  absence  of  co-signers  is  presented  in  figure  7.  Instead  of 
providing sub-categorization under each section, the chart contains five labels that are Auto, 
Business,  Education,  Home  and  Other  with  further  inclusion  of  information  whether  a  co-
signer  was  involved  or  not.  In  all  types  of  loans,  the  bars  demonstrate  similar  total  loan 
amounts irrespective of whether a co-signer is present or not hence suggesting that co-signer 
does not greatly change the amount of credit granted in totality. Particularly, the total loan 
amounts  are  rather  stable  with  an  average  of  around  3  billion  dollars  in  both  of  the 
categories. Such uniformity indicates that lenders disperse huge loans at an egalitarian level 
irrespective of the dependency of the borrower to have a co-signer. There is a slight pattern 
to note when comparing the heights of the bars, loan amounts are in fact a little bit higher in 
some of the categories that involve a co-signer, as in the case of Business and Home loans. 
This  can  be  seen  as  a  sign  that  a  co-signer  can  only  give  a  slight  advantage  in  terms  of 
access  to  larger amounts of loan, perhaps because of a perceived higher  credit-worthiness. 
The conclusions are useful with respect to developing credit scoring models powered by AI 
[44]..  Adding  the  co-signer  status  as  a  feature  could  increase  the  accuracy  of  predicting 
whether a person will be approved or not in the case of loan applications that are on the edge 
of  being  approved  and  on  the  edge  of  being  rejected.  The  availability  of  an  option  of  co-
signing the loan may therefore play an important  role in  loan approvals  and loan  amounts 
among small businesses especially when it comes to underserved small business groups with 
limited  credit  histories.  This  evaluation  proves  the  benefit  of  more  subtle  credit  modeling 
that  can  interpret  borrower  profiles  beyond  the  mainstream  usage  measures-  which  jives 
with the objectives of inclusive and alternative-data AI-based credit systems.

---

<!-- PAGE 20 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

77

H. Loan Purpose and Co-Signer Status Default Rate Analysis

Figure 8: This image illustrates the defaults according to the purpose of the loan and the 
availability of the co-signer

Fig. 8 shows, by loan purpose and status with a co-signer, the impact of credit score and of 
default risk on interest rate distribution. On the chart, the average default rates are compared 
between  the  corresponding  types  of  loans  (Auto,  Business,  Education,  Home,  Other)  with 
those borrowers who have co-signer and those without. Among the major emerging trends, 
the backing of a co-signer has its defaulting in all loan applications. Lending under the label 
of business and auto loans in the category of No Co-Signer has the worst average defaults-
more than 13 percent-conveying the caution that lenders witness when the borrower has no 
second  line  of  financial  support.  On  the  other  hand,  borrowers  who  have  a  co-signer  are 
likely to exhibit less of default rates especially under categories of home and education loans 
with  averages  as  little  as  around  10%.  This  trend  suggests  that  co-signing  does  not  only 
strengthen a borrower in terms of credit worthiness to the lender, but leads to less potential 
defaults,  which  was  likely  to  be  instigated  by  shared  responsibility  or  better  financial 
sobriety.  Under  a  modeling  angle,  this  number  lends  significant  thrust  to  the  idea  of 
including  co-signer  status  as  a  predictive  parameter  in  AI-driven  credit  rating  models.  It 
suggests  that  the  other  data  input  loan  purpose  provides  effective  segmentation  in  the 
prediction of risks, especially on segments that are financially underserved and therefore the 
co-signers  present  more  frequently  because  of  thin-file.  The  results  emphasize  the 
significance of the alternative attributes--namely loan purpose and co-signer presence--in the 
construction of inclusive, correct credit models [45]. The lenders will be better able to fine-
tune  their  interest  rates  or  even  decision-making  levels  appropriately  using  these  risk-
segmented information.

VI. Discussion and Analysis

A. Effect of Alternative Data on accuracy of credit score

The adoption of the addition of alternative data in credit scoring has been finding substantial

---

<!-- PAGE 21 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

78

changes  in  the  way  traditional  lending  was  done.  Alternative  data  are  non-traditional 
indicators in the form of utility payments, rental history, mobile phone usage, e-commerce 
activity, and social media behavior [46]. These data points give a further understanding of 
how the borrower is behaving, particularly individuals and small businesses which have thin 
or  no  credit  files.  Such  a  shift  is  particularly  relevant  to  the  US  small  businesses.  Most 
entrepreneurs conduct  their businesses in  cash markets  or where there are no conventional 
financial  footprints.  Through  alternative  data,  the  lenders  will  be  able  to  create  a  holistic 
profile  of  creditworthiness  that  does  not  live  within  the  constraints  of  FICO  scores  or 
historical  loan  defaults.  The  results  of  this  study  indicate  that  small  businesses  that  use 
alternative data analytics were provided with better  interest rates and accessibility to loans 
especially among the businesses that have never defaulted or those with more positive and 
reliable behavior patterns online. This implies that the alternative data will not only promote 
scoring  accuracy  but  it  will  democratize  financial  inclusion  [47].  It  minimizes  the 
probability  of  false  negatives  of  credit  evaluation-those  who  might  be  creditworthy  are 
locked  out  because  of  the  absence  of  a  long  credit  history  in  the  economic  environment. 
There is the need to ascertain that the data employed is pertinent, precise, and proportionate 
to  a  forecast  of  the  loan  performance.  The  lenders  have  to  justify  the  fit  between  the 
alternative  data  variables  that  they  choose  and  repayment  behaviors.  With  a  careful 
implementation, alternative data can decrease the risk of defaults, improve portfolio quality, 
and widen the scope of lending activities to a wider section of people.

B. Mitigation of Loan Default Risk by Co-signers

The  availability  of  co-signer  has  become  the  decisive  measure  in  ensuring  default 
inquisitiveness  will occur among  the small  business  borrowers. As  reflected in  the results, 
co-signer  guaranteed  loans  had  a  lesser  average  default  rate  when  comparing  different 
purposes  of  loans  [48].  The  trend  underscores  how  co-signers  are  useful  in  boosting  the 
credibility  of  the  borrower,  and  thus,  dispels  the  lenders  fears  of  the  likelihood  of  paying 
them off. In special industries such as the Home and Auto, which require massive capital, 
the co-signers are quite crucial in raising the eligibility and credibility of the borrowers. The 
presence of co-signers means two layers of safety nets, that a person is not only a financial 
backer  but  a  person  of  social  responsibility.  This  tends  to  make  borrowers  pay  more 
responsibly as they are aware that they may spoil the credit status of another person. On the 
part  of  the  lender,  the  presence  of  a  co-signer  would  help  in  diversifying  the  risk,  hence 
rendering  loan  portfolios  to  be  a  bit  stronger  particularly  in  an  unstable  economic  set  up. 
Interestingly,  the  chart  used  in  Figure  8  reveals  that  despite  high-risk  segments  such  as 
Business and Education, the average default rating comes down when there is a presence of 
a co-signer. This supports the argument that co-signers stabilize in the case of both types of 
loans  [49].  The  input  of  the  co-signers  should  be  questioned  under  equity.  Although  they 
decrease  the  risk,  excessive  dependence  on  co-signers  can  deprive  the  underprivileged 
borrowers  whose  networks  are  underdeveloped.  Co-signers  are  not  only  a  risk  reduction 
mechanism; they allow wider participation in financial transactions. The policymakers and 
lenders ought to consider rewarding the co-signed loan contracts by putting a lower charge 
on it or flexible terms due to the security it offers the lending environment.

C. Effect of Purpose of Loan on the Probability of default

The purpose of the loan has  a strong impact  on  the possibilities of default because not  all 
sectors are equal in financial conduct, capital requirements and risk level. Unlike the Auto 
loan and Home loan, Business loans are generally characterized by high rates of default, as 
shown in Figure 8; they prove unpredictable when considering the co-signer status (Figure 
8). Such differences indicate that these types of loans which already have always been used 
differently  add  to  the  level  of  risk  within  borrowers  in  different  ways.  Business  lending 
loans, especially those of the small and medium scale establishments (SMEs), are those with

---

<!-- PAGE 22 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

79

uncertain income generators, market risks, and operational risks. This uncertainty forms the 
reason why default rates are high, especially in the situation where borrowers have no ample 
financial background or securities. Auto loans are in general less in size, secured by tangible 
assets,  and  related  to  critical  mobility  needs-and  thus  are  less  risky  in  terms  of  repayment 
behavior. On the same note, Home loans tend to be high amounts and long term, thus people 
tend  to  be  more  committed  to  repayments.  It  is  indicated  in  the  findings  that  loans  to 
Education  possess  a  moderate  level  of  default  [50].  They  can  show  postponed  repayment 
capacity, when the borrowers depend on future time incomes and forecasts over the present 
ones.  Miscellaneous  loans  reportedly  had  varied  patterns  and  this  emphasizes  the  need  to 
have  better  credit  categorization  and  profiling  in  order  to  strengthen  the  miscellaneous 
groups. Lenders will need to pursue dynamic risk-pricing policies on a per-type basis. With 
high-risk  products  such  as  business  loans,  it  could  be  possible  to  introduce  more  flexible 
repayment  patterns,  financial  literacy  or  part  guarantees  that  help  counter  the  risk  [51]. 
Conversely,  the  low-risk  loans  may  be  automated  and  AI-based  that  will  help  to  lower 
operational costs and can increase access. The purpose of a loan must be a major factor of 
credit evaluation whereby not only the interest rates, but the loan approval system and post 
loan support frameworks must be affected.

D. Impact of Credit Score and Default History on the Distribution of Interest Rates

Credit  score  and  default  history  has  been  among  the  most  influential  variables  in  how 
interest  rate  is  distributed  across  types  of  loans. High  credit  score  borrowers  who  have  no 
defaults  in  their  records  generally  receive  lower  interest  rates  and  those  with  a  history  of 
default  or  low  scores  find  that  their  interest  rates  are  high  or  worse  still  deny  them  loans 
[52]. The findings in Figure 8 affirm this conventional tendency but denote delicate trends 
once crossed with the existence of a co-signer and the purpose of a loan. Under the No Co-
signer  category,  high  average  default  rates  are  encountered  by  borrowers  on  all  types  of 
loans and consequently increase the interest  rate distribution on a wider fate biased on the 
higher  side.  This  implies  that  the  credit  scoring  models  are  stricter  with  unassisted 
borrowers. On the other hand, the Yes Co-signer group has a generally better credit rating, 
which leads  to  better distribution of rates, which is  even in  the previously  riskier business 
lending.  The  variance  of  default  distribution  of  loans  of  various  types  point  out  that 
consistent  consumer  credit  facility  borrowers  have  much  easier  interest  rates  to  forecast. 
There is larger variance in the case of individuals who may show erratic behavior in terms of 
credit, or who have defaulted in the past and thus the risk uncertainty factor must be priced 
in by the lender. The possibility of including both AI and machine learning when modeling 
credit  risks  has  the  potential  to  reflect  these  differences  better  and  offer  more  reasonable 
interest  rates  [53].  Typical  models  impose  too  high  expectations  when  it  comes  to  small 
offences whereas one powered by AI has the ability to take into consideration surroundings 
information  and  behavior  patterns  which  then  help  in  making  adjustments  to  the 
computation of rates. The credit score and history of defaults by a borrower remains to be 
quite  effective  indicators  of  the  interest  rate  decision  and  data  analytics  advancements  are 
making this as fair and data-driven as possible.

E. Neutral Lending Policies, and the Connection with Default Rates

The  momentum  of  gender  neutral  lending  has  been  driven  by  the  efforts  of  financial 
institutions  to  become  accessible  and  non-depredatory.  This  research  did  not  observe  any 
significant  changes  in  default  rates  due  to  gender  when  compared  with  other  explanatory 
factors such as loan purpose, co-signers and credit history were held constant. It implies that 
the  modern  credit  models  start  to  pay  more  attention  to  measurable  financial  behavior 
instead of relying on unfounded demographic stereotypes and are inching towards achieving 
fair lending. The absence of a bias in the default rates means that there is no discrimination 
against male and female borrowers provided that risk-adjusted conditions are laid down. But

---

<!-- PAGE 23 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

80

one  should  take  a  wider  scope  into  consideration  [54].  Although  the  default  risk  can  be 
considered gender-neutral, the provision of loans, the mean size of loans granted, and rates 
of  interest  charged  can  still  represent  the  systemic  inequality.  An  example  is  that  female 
entrepreneurs  have  frequently  stated  that  they  have  to  submit  more  paperwork  or  get  a 
tougher review during underwriting. The combination of gender and other socio-economic 
variables like education, the level of income, and residency status can add to disadvantages. 
Such  factors  are  typically  not  directly  included  into  default  statistics  but  can  affect  access 
and  terms  in  a  more  subtle  way.  Consequently,  subsequent  models  should  carry  on  with 
ensuring that the metric of fairness is incorporated throughout the applications processing to 
approval  and  rate-setting  [55].  Credit  judgments  conducted  by  AI  represent  a  chance  to 
strengthen gender neutral lending because it pays attention to behavioral, transactional, and 
performance  data.  Such  models  need  to  incorporate  bias  detection  algorithms  and  fairness 
audits to eliminate discrimination that may not be executed intentionally [56]. Although this 
study  shows  that  gender  is  not  directly  proportional  to  the  default  likelihood,  it  is  upon 
financial  institutions  to  actively  update  and  improve  gender  equity  throughout  the  lending 
process lifecycle in order to maintain long-lasting inclusion and confidence.

F. Predictive loan risk modeling with AI

Predictive  analytics  in  lending  has  been  transformed  by  Artificial  Intelligence  (AI),  which 
allows  setting  up  more  granular  and  accurate  judgments  regarding  loan  default  risk. 
Analyzing large streams  of data that contain not only  typical  financial indicators but  other 
behavioral  signals,  AI  models  can  identify  patterns  and  trends  and  reveal  correlations  that 
would otherwise be invisible to the traditional tools [57]. This research paper contributes to 
the  relevance  of  AI,  especially  when  it  comes  to  the  scope  of  bias  reduction  and  better 
predictive outcomes in the loans assessment of small businesses. Machine learning, as one 
of the AI algorithms, can update with changes in the patterns and behaviors of the borrower, 
macro economy, and risks characteristic of the industry. In the case study of understanding 
the dataset used in this research, AI would be able to know that Business loans on Default 
with  no  co-signer  and  low  historical  credit  activity  were  at  the  greatest  risk  and  the  Auto 
loans  on  Default  that  had  co-signer  were  most  likely  to  be  at  low  default  rate  [58].  The 
insights  can enable the lenders to  better calibrate their approval  rules, assignment of rates, 
and efforts to alleviate risk. Risk scores can be updated real-time and dynamically based on 
continuously learning new repayment behaviors  as  AI does, making the  credit models and 
repayment behavior more responsive to present realities of the borrowers [59]. This is unlike 
the stagnant scoring systems that are based on old dated, or narrow data. Furthermore, AI-
based applications aid in the process of customer segmentation, evaluation of risks assessed 
on  the  basis  of  clusters,  and  even  suggestions  of  financial  products  that  would  suit  the 
profiles of borrowers. Ethics should inform the use of Artificial Intelligence. It is important 
to have transparency, explain ability of models, and prevention of discriminatory outcomes. 
Regulators  pay  more  attention  to  the  need  to  make  sure  that  AI  in  lending  is  consolidated 
with fairness and accountability principles [60]. AI would have an effective tool to increase 
credit  scoring  accuracy,  financial  access,  and  to  mitigate  systemic  risk  thus  making  it  the 
foundation of modern and evidential lending practices.

VII. Future Work

With  financial  institutions  turning  toward  data-based  methods  to  address  both  credit  risk 
management  and  lending  strategy  optimization,  the  present  work  leaves  open  a  range  of 
avenues  to  explore  in  the  future  [61].  Although  this  work  forms  important  basis  on  the 
influence  of  the  credit  scores  and  default  probabilities  on  the  distribution  of  interest  rates 
across different loan purposes and to different types of borrowers including co-signers, the 
future work will add to this work by addition of a greater level of variables, a higher level of 
predictive  models,  and  real-time  integration  of  data.  A  potentially  beneficial  avenue  is  the

---

<!-- PAGE 24 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

81

use  of  machine  learning  algorithms  that  will  help  credit  score  and  optimize  interest  rates 
[62]. Random forests, gradient boosting, and neural networks might be used to improve the 
accuracy of default prediction relative to the conventional regression analysis. Such models 
are  able  to  reproduce  non-  linear  association  between  profiles  of  borrowers  and  the 
likelihood of defaulting which can provide a more tailored rate of interest and can enhance 
financial inclusion. The other area that can be explored in future is the inclusion of temporal 
and behavioral data. Through the analysis of longitudinal data able to trace the modification 
of  the  borrower  behavior  throughout  time  such  as  changes  in  payments,  alterations  in 
income, in the future, it is possible to consider the dynamic character of creditworthiness and 
its  influence  on  interest  rate  structure.  This  would  enable  lenders  to  change  their  credit 
models  in  near  real-time.  To  discuss  how  the  character  of  lending  activity  may  vary 
regionally or in age, geographical and demographical divisions may be added. Segmentation 
of this nature would give banks and policymakers more depth in terms of actual context so 
that  lending  policies  could  be  equitable  across  all  populations.  Research  can  further  be 
applied  in  policies  as  an  extension,  like  the  impact  of  co-signer  policies  and  financial 
regulations  on  risk-sharing  and  default  probabilities  [63].  Incorporation  of  regulatory 
changes or macro-economic indicators such as inflation or unemployment rates may produce 
more  generous  risk  measurement.  Finally,  live  dashboards  and  visualization  tools  can  be 
considered to make decision-making quick and convenient among financial analysts and the 
borrowers.  Devices,  fueled  by  Tableau  or  Power  BI,  might  simplify  the  language  of  a 
complicated  risk  policy  and  allow  to  create  an  understandable,  transparent,  and  trusted 
interpretation of the lending process. Advanced financial models of risk are more inclusive, 
dynamic,  and  technologically  advanced  than  before  and  are  based  on  the  findings  of  this 
research [64]. Further building on such findings by enhancing multidisciplinary approaches 
and  new  developments  in  technology  will  enhance  the  credit  scoring  models  and  provide 
responsible, fair lending practices in the growing digital economy.

VIII. Conclusion

This  study  has  examined  the  complexities  of  the  relationships  involving  credit  scores, 
default  rates,  distributions  of  interest  rates,  and  related  borrower  qualities  on  a  wealthy 
lending  dataset.  With  the  thorough  approaches  to  data  analysis  and  visualization  using 
Python, Excel, and Tableau, the study revealed meaningful tendencies that may have various 
cost-effective implications to the credit risk analysis and financial decision-making of loans-
related practice. The key findings indicate that interest rates largely depend on credit scores, 
where  the  individuals  with  higher  marks  are  always  offered  better  quotations.  Borrowers 
who  had  a  co-signer  had  fewer  defaults  indicating  that  lenders  felt  safer  with  the  extra 
sources of capital of the debtor. The analysis indicated that the impact of annual income and 
amount  of  loan  on  interest  rates  and  the  remaining  possibility  to  default  with  loan  is 
significant,  which  underlines  the  necessity  of  broad-based  risk  assessment.  This  study 
revealed  the  significance  of  data-based  credit  scoring  with  the  example  of  using  a 
combination  of  different  characteristics  of  borrowers  to  achieve  improved  risk  forecasting 
and a more justifying lending policy in terms of providing lenders. The visualizations gave a 
straightforward  and  easily  comprehended  explanation  to  these  complicated  financial  ties, 
which  raised  the  prospect  of  direct  application  in  the  workplace  lending  settings. 
Notwithstanding  its  merits,  the  study  had  its  limitations  such  as  employing  historical, 
stagnant  data,  and  lack  of  macroeconomic  variables  i.e.  unemployment  rates  or  inflation, 
which  might  affect  the  behavior  of  borrowers.  The  emerging  knowledge  will  serve  as  an 
excellent basis of future study and development of credit analytics. The importance of credit 
scores and related variables in determining the outcome of loans highlighted in this region 
will aid both academic and industry stakeholders in understanding how data can be used to 
make more transparent and fairer lending practices. Financial technology is developing, and

---

<!-- PAGE 25 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

82

as such, incorporation of such machine learning models with a powerful data source such as 
this  can  be  used  to  improve  predictive  accuracy  and  accordingly  facilitate  inclusive  credit 
systems.

IX. References:

1.  Lomas,  R.  (2024,  December).  AI-Driven  FinTech  Solutions  for  Financial  Inclusion:  A 
Study  on  MSME  Sector  Empowerment.  In  2024  1st  International  Conference  on 
Advances  in  Computing,  Communication and Networking (ICAC2N) (pp. 1887-1891). 
IEEE.

2.  Jang, G. Y., Kang, H. G., Park, J., & Choi, H. S. (2023). AI-Driven Credit Scoring and 
Market  Transformation:  How  ACSS  Reshapes  SME  Financing,  Firm  Strategy,  and 
Regulatory Boundaries. In Posted on Google Scholar by the AI and Finance Conference 
after the presentation with the previous title," Unveiling the Imoact of Alternative Credit 
Scoring Systems on Small and Medium-sized Enterprises.

3.  Bello,  O.  A.  (2024).  The  role  of  data  analytics  in  enhancing  financial  inclusion  in 
emerging  economies.  International  Journal  of  Developing  and  Emerging  Economies, 
11(3), 90-112.

4.  Nguyen, E. (2024). The Role of Big Data and AI in Real-Time Credit Scoring.

5.  Mhlanga, D. (2023). FinTech and Artificial Intelligence in addressing poverty,  towards 
sustainable  development.  In  FinTech  and  artificial 
intelligence  for  sustainable 
development:  The  role  of  smart  technologies  in  achieving  development  goals  (pp.  89-
117). Cham: Springer Nature Switzerland.

6.  Nuka,  T.  F.,  &  Ogunola,  A.  A.  (2024).  AI  and  machine  learning  as  tools  for  financial 
inclusion: challenges and opportunities in credit scoring. International Journal of Science 
and Research Archive, 13(2), 1052-1067.

7.  Adewale, G. T., Umavezi, J. U., & Olukoya, O. (2022). Innovations in Lending-Focused

FinTech: Leveraging AI to Transform Credit Accessibility and Risk Assessment.

8.  Ajuwon,  A.,  Oladuji,  T.  J.,  Akintobi,  A.  O.,  &  Onifade,  O.  (2024).  A  Model  for 
Financial Automation in Developing Economies: Integrating AI with Payment Systems 
and Credit Scoring Tools.

9.  Okunola,  A.,  &  Ahsun,  A.  (2022).  Leveraging  Big  Data  Analytics  and  AI  for 
in  Underserved

Personalized  Financial  Product  Design  and  Risk  Assessment 
Populations.

10. Adewuyi,  A.,  Ajuwon,  A.,  Oladuji,  T.  J.,  &  Akintobi,  A.  O.  (2023).  Advances  in 
Financial Inclusion Models: Expanding Access to Credit through AI and Data Analytics. 
International  Journal  of  Advanced  Multidisciplinary  Research  and  Studies,  3(6),  1827-
1842.

11. Omokhoa,  H.  E.,  Odionu,  C.  S.,  Azubuike,  C.  H.  I.  M.  A.,  &  Sule,  A.  K.  (2024). 
Leveraging  AI  and  technology  to  optimize  financial  management  and  operations  in 
microfinance institutions and SMEs. IRE Journals, 8(6), 676.

12. Shittu,  A.  K.  (2022).  Advances  in  AI-driven  credit  risk  models  for  financial  services 
International  Journal  of  Multidisciplinary  Research  and  Growth

optimization. 
Evaluation, 3(1), 660-676.

13. Omogbeme, A. O., Phil-Ugochukwu, A. I., Nwabufo, I. J., & Onyebuchi, J. (2024). The 
role of artificial intelligence in enhancing financial inclusion: A review of its impact on 
financial  services  for  the  unbanked  population  in  the  United  States.  World  Journal  of

---

<!-- PAGE 26 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

83

Advanced Research and Reviews, 23(2), 2184-2192.

14. Avevor,  M.,  Attionu,  G.  T.,  Osahor,  D.,  Azonuche,  T.,  &  Tawo,  O.  (2023).  Beyond 
funding:  rethinking  small  business  administration  strategies  and  public-private 
partnerships for minority-owned business resilience (AI, FinTech, and Policy Synergy).

15. Hamzat,  L.  (2023).  Real-Time  Financial  Resilience  and  Debt  Optimization  for 
Entrepreneurs:  Tackling  Debt  Management  as  a  Financial  Health  Pandemic  and 
Empowering Small Business Growth Through Early Detection of Financial Distress and 
Effortless Capital Management.

16. Balaji,  K.  (2024).  Harnessing  AI  for  financial  innovations:  Pioneering  the  future  of 
financial services. In Modern Management Science Practices in the Age of AI (pp. 91-
122). IGI Global.

17. Xiong,  H.,  Carton,  F.,  &  McCarthy,  J.  B.  (2024,  October).  AI-Powered  Financial 
Services:  A  Value  Co-creation  Model.  In  International  Workshop  on  Enterprise 
Applications, Markets and Services in the Finance Industry (pp. 18-31). Cham: Springer 
Nature Switzerland.

18. Taneja,  B.  (2024).  Financial  Innovations  in  FinTech:  Unleashing  the  Power  of 
in  Firm  Financing  and  Investment  Strategies.  In 
for  Promoting  Financial  Literacy  and

Embedded  Finance  and  AI 
Contemporary  Research  and  Practices 
Sustainability (pp. 208-232). IGI Global.

19. Adhikari, P., Hamal, P., & Jnr, F. B. (2024). The role of fintech in US entrepreneurship: 
How AI is shaping the future of financial services. International Journal of Science and 
Research Archive, 13(02), 1673-1693.

20. How, M. L., Cheah, S. M., Chan, Y. J., Khor, A. C., & Say, E. M. P. (2023). Artificial 
Intelligence  for  Advancing  Sustainable  Development  Goals  (SDGs):  An  Inclusive 
Democratized  Low-Code  Approach.  In  The  Ethics  of  Artificial  Intelligence  for  the 
Sustainable Development Goals (pp. 145-165). Cham: Springer International Publishing.

21. Kowsar, M. M., & Mohna, H. A. (2023). American Journal of Interdisciplinary Studies.

22. Piao, J., Wang, K. P., & Weng, D. (2024). US Banks' Artificial Intelligence and Small 
Business Lending: Evidence from the Census Bureau's Technology Survey. Available at 
SSRN 5016585.

23. Heidari, A. (2023). The Role of Artificial Intelligence in Modern Finance. Available at

SSRN 5127689.

24. Challoumis, C. (2024). Ai’s role in the cycle of money. In XIX International Scientific

Conference. London. Great Britain (pp. 1003-1035).

25. Aria,  J.,  Diego,  C.,  Jose,  D.,  &  Ok,  E.  (2024).  Machine  Learning  in  Credit  Risk

Management: Evaluating the Role of AI and Blockchain.

26. Chukwuma-Eke, E. C., Attipoe, V., Lawal, C. I., Friday, S. C., Isibor, N. J., & Akintobi, 
A.  O.  (2024).  Promoting  financial  inclusion  through  energy  financing  for  underserved 
communities:  A  sustainable  business  model.  International  Journal  of  Multidisciplinary 
Research and Growth Evaluation, 5(1), 1699-1707.

27. Nwachukwu,  G.  (2024).  Enhancing  credit  risk  management  through  revalidation  and 
accuracy  in  financial  data:  The  impact  of  credit  history  assessment  on  procedural 
financing. International Journal of Research Publication and Reviews, 5(11), 631-644.

28. Alonge, E. O., Eyo-Udo, N. L., Ubanadu, B. C., Daraojimba, A.  I., Balogun, E. D., & 
Ogunsola, K. O. (2024). Developing an Advanced Machine Learning Decision-Making

---

<!-- PAGE 27 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

84

Model  for  Banking:  Balancing  Risk,  Speed,  and  Precision  in  Credit  Assessments. 
Journal details pending.

29. Singhania,  D.,  Tanty,  G.,  &  Srivastava,  A.  (2024).  Empowering  Rural  Jharkhand: 
Adoption  of  Artificial  Intelligence  for  Digital  Financial  Inclusion.  In  Blockchain’s 
Transformative Potential of Financial Technology for Sustainable Futures (pp. 123-134). 
Cham: Springer Nature Switzerland.

30. Olanrewaju,  A. G.,  Inegbedion,  E., Olukotun,  I.  F., &  Atimango, K.  (2024). AI-driven 
healthcare  financial  models:  Ethical  frameworks  for  balancing  profit  and  access  in 
precision medicine in the US.

31. Ziemba,  E.  W.,  Duong,  C.  D.,  Ejdys,  J.,  Gonzalez-Perez,  M.  A.,  Kazlauskaitė,  R., 
Korzynski,  P.,  ...  &  Wach,  K.  (2024).  Leveraging  artificial  intelligence  to  meet  the 
sustainable development goals. Journal of Economics and Management, 46, 508-583.

32. Adenekan,  T.  K.  (2022).  The  Digital  Path  to  Financial  Inclusion:  Data  Engineering

Strategies for Equitable Banking.

33. Ojonugwa,  B.  M.,  Adanigbo,  O.  S.,  Ogunwale,  B.,  &  Ochefu,  A.  (2024).  Impact 
Investing  and  AI:  Advancing  Developmental  Goals  through  Data-Driven  Investment 
Strategies.

34. Kouam, A. W. F. (2024). The Impact of Artificial Intelligence on Fintech Innovation and

Financial Inclusion: A Global Perspective.

35. Paleti, S. (2023). Transforming Money Transfers and Financial Inclusion: The Impact of 
AI-Powered  Risk  Mitigation  and  Deep  Learning-Based  Fraud  Prevention  in  Cross-
Border Transactions. Available at SSRN 5158588.

36. Yu,  P.,  Wong,  S.  K.,  &  Prabhakar,  A.  C.  (Eds.).  (2024).  AI  Strategies  for  Social

Entrepreneurship and Sustainable Economic Development. IGI Global.

37. Liu, Y., Li, X., & Zheng, Z. (2024). Smart natural disaster relief: Assisting victims with

artificial intelligence in lending. Information Systems Research, 35(2), 489-504.

38. Mbuguah, S. M., & Gichuki, D. K. (2024, November). Leveraging Emerging Trends for 
Technological  Advancement  in  Africa.  In  2024  4th  International  Multidisciplinary 
Information Technology and Engineering Conference (IMITEC) (pp. 1-11). IEEE.

39. Ok, E., Aria, J., Jose, D., & Diego, C. (2024). Transforming Credit Risk Mitigation: The

Role of AI, Blockchain, and Predictive Analytics.

40. Adewale, T. T., Olorunyomi, T. D., & Odonkor, T. N. (2023). Big data-driven financial 
analysis:  A  new  paradigm  for  strategic  insights  and  decision-making.  Journal  of 
Financial Innovation and Analytics, 1(1), 1-15.

41. Shah,  S.  (2024).  Financial  inclusion  and  digital  banking:  Current  trends  and  future

directions. Premier Journal of Business and Management, 1.

42. Palakurti, N. R. (2024). The Intersection of Information Technology, Financial Services, 
and  Risk  Management,  Including  AI  And  Ml  Innovations.  International  Journal  of 
Computer Engineering And Technology (IJCET), 15(4).

43. Zoey,  A.,  Aria,  D.,  Oscar,  A.,  Marek,  M.,  Julia,  Z.,  Cora,  L.,  &  Ok,  E.  (2024). 
Blockchain  and  AI  in  Financial  Risk  Management:  A  Machine  Learning  Approach  to 
Credit Risk Mitigation. Journal of Financial Technology, 15(4), 201-214.

44. Chadha,  P.,  Gera,  R.,  Khera,  G.  S.,  &  Sharma,  M.  (2023).  Challenges  of  Artificial 
Intelligence  Adoption  for  Financial  Inclusion.  In  Artificial  Intelligence,  Fintech,  and

---

<!-- PAGE 28 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

85

Financial Inclusion (pp. 135-160). CRC Press.

45. Gera, R., Chadha, P., Saxena, A., & Dixit, S. (2023). A scientometric and bibliometric 
review  of  impacts  and  application  of  artificial  intelligence  and  fintech  for  financial 
inclusion. In Artificial Intelligence, Fintech, and Financial Inclusion (pp. 82-111). CRC 
Press.

46. Attah,  R.  U.,  Garba,  B.  M.  P.,  Gil-Ozoudeh,  I.,  &  Iwuanyanwu,  O.  (2024).  Corporate 
banking  strategies  and  financial  services  innovation:  Conceptual  analysis  for  driving 
corporate growth and market expansion. Int J Eng Res Dev, 20(11), 1339-49.

47. Sanyaolu,  T.  O.,  Adeleke,  A.  G.,  Efunniyi,  C.  P.,  Akwawa,  L.  A.,  &  Azubuko,  C.  F. 
(2024).  The  role  of  business  analysts  in  driving  financial  inclusion  through  product 
innovation. Finance & Accounting Research Journal P-ISSN, 1555-1581.

48. Xiong, H., Carton, F., & McCarthy, J. B. (2022). Data Science for Financial Inclusion: a

value co-creation model for balanced benefits.

49. El Hajj, M., & Hammoud, J. (2023). Unveiling the influence of artificial intelligence and 
machine learning on financial markets: A comprehensive analysis of AI applications in 
trading,  risk  management,  and  financial  operations.  Journal  of  Risk  and  Financial 
Management, 16(10), 434.

50. Abu Jamie, N. H., Abu-Jamie, T. N., & Al-Absy, M. S. M. (2024). Advances in AI and 
Their Effects on Finance and Economic Analysis. The AI Revolution: Driving Business 
Innovation and Research: Volume 1, 507-523.

51. Channe, P. S. (2024). The  Impact  of AI on Economic Forecasting and Policy-Making: 
Opportunities  and  Challenges  for  Future  Economic  Stability  and  Growth.  York 
University.

52. Rajenthran,  G.  (2024).  Financial  Frontiers:  How  Generative  AI  Is  Shaping  the  Fintech 
Industry. In Generative AI for Transformational Management (pp. 161-192). IGI Global.

53. Owoade, S. J., Uzoka, A., Akerele, J. I., & Ojukwu, P. U. (2024). Enhancing financial 
portfolio management with predictive analytics and scalable data modeling techniques. 
International Journal of Applied Research in Social Sciences, 6(11), 2678-2690.

54. Omopariola,  B.  J.  (2023).  Decentralized  energy  investment:  Leveraging  public-private 
partnerships  and  digital  financial  instruments  to  overcome  grid  instability  in  the  US. 
World Journal of Advanced Research and Reviews, 20(03), 2178-2196.

55. Maleh,  Y.,  Zhang,  J.,  &  Hansali,  A.  (Eds.).  (2024).  Advances  in  emerging  financial

technology and digital money. CRC Press.

56. Meera, K. L., & Seshanna, S. (2023). AI and Machine Learning as Drivers of Change in

the Financial Industry. Journal of Financial Innovation, 51(3), 190-215.

57. Lim, T. (2024). Environmental, social, and governance (ESG) and artificial intelligence 
in finance: State-of-the-art and research takeaways. Artificial Intelligence Review, 57(4), 
76.

58. Subramaniam,  Y.,  Loganathan,  N.,  Khan,  F.  N.  H.  T.,  &  Subramaniam,  T.  (2024). 
Exploring  the  Impact  of  Artificial  Intelligence  on  Financial  Inclusion:  Cross-Country 
Analysis. Social Indicators Research, 1-18.

59. Fiorillo, L., & Mehta, V. (2024). Accelerating editorial processes in scientific journals:

Leveraging AI for rapid manuscript review. Oral Oncology Reports, 10, 100511.

60. Tyagi, A. K. (2024). Modern Banking and. Convergence of Technology and Operations

---

<!-- PAGE 29 -->

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

86

Management in Modern Businesses, 141.

61. Sehgal,  M.  I.  (2023).  Digital  Finance  Strategies  and  Their  Role  in  Transforming 
Financial  Management.  Digital  Transform  Management:  Em  Technologic  Innovations 
for Orga, 57.

62. Mousa,  S.  (2024).  Unleashing  the  Potential  of  Industry  4.0  for  Financial  Inclusion.  In 
Financial  Inclusion,  Sustainability,  and  the  Influence  of  Religion  and  Technology  (pp. 
253-285). IGI Global Scientific Publishing.

63. Bhavana, K. V., Koduri, H., Ariwa, E., & Vishwa, K. D. (2023). Artificial intelligence 
and Fintech industry—The metaverse adoption. The business of the metaverse, 199-215.

64. Packin,  N.  G.,  &  Lev‐Aretz,  Y.  (2024).  Decentralized  credit  scoring:  Black  box  3.0.

American Business Law Journal, 61(2), 91-111.

65. Datasheet Link:https://www.kaggle.com/datasets/nikhil1e9/loan-default

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Informatics and Data Science Research
ISSN 2997-3961 (Online)
Vol. 2, No. 10, Oct 2025,
Available online at: https://scientificbulletin.com/index.php/IJIDSR

Developing AI-Powered Credit Scoring Models Leveraging
Alternative Data for Financially Underserved US Small
Businesses

Md Manarat Uddin Mithun
Master of Science in Business Analytics, Trine University, USA

Sakhawat Hussain Tanim
Master of Science in Technology Project Management, Illinois State University, USA

Rahanuma Tarannum
Masters in Information Technology, Arkansas Tech University, USA

Article information:
Manuscript received: 4 Aug 2025; Accepted: 10 Sep 2025; Published: 18 Oct 2025

Abstract:  In  the  modern  dynamically  changing  financial  landscape  where  people
more  and  more  often  are  illegible  with  traditional  credit  scoring  systems,  traditional
credit scoring systems are in many cases ineffective to capture the credit worthiness of
the underserved small business borrowers- especially those who do not have lengthy
credit histories or traditional documentation. In their study, the authors focus on how
to  develop  and  implement  the  artificial  intelligence  (AI)-based  credit  scoring  models,
which  can  solve  these  shortcomings  by  utilizing  alternative  sources  of  data.  The
objective  is  to  improve  the  accuracy,  diversity  and  equity  of  lending  decisions  to
marginalized  business  owners  of  small  firms  that  are  usually  underrepresented  in
regular  financial  services.  Using  a  large  scale  data  containing  demographic,  financial,
employment,  and  behavioral  characteristics,  this  study  will  utilize  enhanced  machine
learning technologies with the help of gradient boosting and decision tree methods to
assess  borrower  risk  of  default  based  on  a  multidimensional  applicative  nature.  The
parameters  namely  education  level,  marital  status,  bracket  of  income  and  job  tenure
are examined to reveal how they impact their viability of loan default. Those findings
display  specific  trends:  the  more  highly  educated  individuals  the  longer  their
employment  term,  and  the  stable  marriage  status,  the  less  likely  they  are  to  default,
which proves the predictive qualities of using non-traditional factors to evaluate credit
risks.  The  results  of  this  study  add  to  a  more  inclusive  credit  assessment  system
because  they  indicate  that  the  alternative  data  points  can  be  used  to  reliably  predict
credit worthiness. This study highlights the possibility of AI underpinning data-driven,
fair  lending  platforms  and  decreasing  financial  exclusion.  In  addition,  it  promotes
responsible AI, which entails that algorithmic decisions are explainable, ethical and do
not  produce  systemic  bias.  This  study  would  contribute  to  the  discussion  of  financial
inclusion  by  presenting  a  solution  that  gives  leeway  to  financial institutions,  financial
innovators, and policymakers. Extending credit to small businesses increases revenue
by  providing  lenders  with  different  data  options  informed  by  AI-driven  models  to
recognize deserving credit applicants that may otherwise have been turned away. This
increases  the  flow  of  capital  not  only,  but  enhances  growth  at  the  grassroots  level-
which works in line with wider agendas of sustainable and inclusive financial growth.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

59

Keywords: Artificial Intelligence, Credit Scoring, Financial Inclusion, Small Business

Lending, Loan Default Prediction and Alternative Data Analytics.

I. Introduction

A. Background

The  importance  of  small  businesses  on  the  economy  of  the  United  States  cannot  be
underestimated as they make up over 99 percent of all businesses and account nearly half for
the  workforce  that  the  private  sector  comprises.  They  are  powerful  motivators  and  spur
innovation,  employment  and  economic  resiliency  at  the  local  level.  Mainstream  credit
systems  are  under-servicing  many  small  businesses,  especially  new,  minority-owned,  or
located in low-income regions despite it being an important source of financial  liquidity to
the businesses. Common financial institutions tend to consider them high-weighted because
they  do  not  have  enough  credit  histories,  unreliable  income  stream,  or  lack  of  collateral.
Such companies therefore have challenges in acquiring cheap financing which can be used
to  increase  their  operations,  make  investments  to  freshen  up  to  new  technology  or  sustain
themselves during economic adversities [1]. In most incidences, these businesses are funded
through personal savings, informal lending or expensive short term loans, which may further
add  to  such  asset  fragility.  The  financing  ecosystem  that  exists  is  not  supportive  of
entrepreneurs working in arrangements that are not within the standard financial systems to
the  degree  needed.  The  pursuit  of  the  structural  biases  in  lending  systems  has  increased
disparities  on  access  to  capital  with  a  disproportionate  hit  on  women,  immigrants  and
minority-owned  businesses  [2].  The  current  COVID-19  pandemic  demonstrated  the
existence  of  these  disparities  since  numerous  underserved  businesses  could  not  access
emergency funding because of the existing old or strict credit evaluation procedures. In this
regard,  credit  assessment  models  in  credit  are  required  urgently  in  the  form  of  innovation
and  inclusiveness  to  bridge  the  gap.  With  a  reconsideration  of  creditworthiness  evaluation
methods, especially with the adoption of technology and alternative data, financial inclusion,
entrepreneurship,  and  more  equitable  economic  development  within  the  small  business
ecosystem of the United States can be achieved.

B. Drawbacks of the Traditional Credit Scoring

The  existing  world  of  credit  assessment  is  dominated  by  such  traditional  credit  scoring
systems  as  FICO  and  Vantage  Score.  These  models  are  mainly  used  to  determine  credit
worthiness of an individual or business depending on structured financial information, such
as credit history repayment performance, amount of outstanding credit, the length of time in
credit, the types of credits taken and any recent credit searches incurred [3]. Although such
criteria work very well to assess the borrowers with known credit status, they are inadequate
in  assessing  small  companies,  particularly  young  companies,  and  those  who  are  informal.
Small businesses are not separating personal and business finances, do not pledge collateral
or operate on a cash basis, and find it hard to produce such standardized data as traditional
models  would  need  [4].  The  entrepreneurs  with  no  or  thin  credit  files  are  not  usually
unjustly pinned, but they may still have a high repayment capacity or a steady business but
the  traditional  model  does  not  see  it.  These  models  are  even  unacquainted  with  small
business  operations  like  seasonal  income,  contract  based  work,  or  informal  credit
relationships.  The  end  result  of  this  exclusionary  structure  is  that  underserved  business
applicants  face  high  rejection  rates,  creating  financial  biases  deep  rooted  in  the  origin  or
design of the scoring mechanism. Traditional scoring systems are often static and backward
looking which does not offer much latitude to use near real-time or behavioral information

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

60

that can be used to gain a more accurate picture of credit risk [5]. The dependence on strict
parameters  opens  to  bias,  since  the  inhabitants  of  a  particular  group  (age  demographic  or
income  level)  are  systematically  underrepresented  in  the  data  sets  against  which  these
models are trained. These constraints reinforce the necessity of changing to more dynamic,
inclusive, and contextualized manners of credit assessment that are able to help the variety
of realities that U.S. small businesses seek refuge in.

C. Emergence of the Alternative Data in Finance

Upraising inequalities, the financial sector has availed over to alternative data as a source of
information  to  quantitate  creditworthiness  especially  of  the  under-served  people  and
businesses  by  the  classical  mechanisms  [6].  Alternative  data  can  be  described  as  non-
traditional measures of financial activity and soundness such as payment trends of rents and
utilities,  cell  phone  use,  social  media  use,  online  shopping  habits,  history  of  business
transactions,  and  work  or  academic  history.  These  pieces  of  information  give  a  fuller  and
more comprehensive picture of the capacity and willingness of a borrower to pay off loans.
Informal  small  businesses  and  those  that  thrive  on  gig  work,  or  those  that  cannot  access
mainstream  financial  services,  alternative  data  therefore  provides  an  effective  means  to
verify  their  credit  card  without  the  need  to  base  this  on  a  long  credit  history  or  collateral.
Alternative data exploitation can make credit analysis less lagging and more segmented to
reflect  more  appropriately  borrower  behavior  or  market  fluctuations  [7].  Advances  in
technologies of aggregating data and open banking systems allow more efficient collection,
processing,  and  securing  of  such  data  with  minimal  compliance  risk.  Increased  Approval
Rates  and  Decreased  Default  Risk  among  under-served  communities  financial  institutions
and  fintech  companies  have  started  to  include  alternative  data  to  calculate  their  risk  of
borrowers,  bringing  more  of  them  access  to  credit  and  leading  to  lower  default  rates.
Privacy, data quality, and algorithmic fairness should be considered in regard to the adoption
of alternative data, as communication was perceived as a possible downfall of this potential
[8].  The  systematic  application  of  alternative  data  sources  holds  the  great  promise  to  be  a
democratizing force in enhancing access to credit and inclusive growth in the small business
community in the United States.

D. The role of Artificial Intelligence

Artificial  Intelligence  (AI)  has  become  an  impressive  theme  throughout  the  financial
industry, especially as the markets relate to risk management planning, fraud identification,
and  customer  segmentation.  Within  credit  scoring,  AI  (and  Machine  Learning  (ML),  in
general) allows us  to  come up with  new models  which are capable not  only  of processing
large amounts of both structured and unstructured data but of detecting complex trends and
efficiently  predicting  the  outcome,  in  comparison  to  the  traditional  ones. Contrary  to  rule-
based systems, AI models can learn using historical data in order to dynamically respond to
changing behavior among borrowers and market conditions [9]. This is what qualifies them
to  be  specifically  suitable  to  incorporate  alternative  sources  of  data,  like  the  employment
history, the trend of transactions or even behavioral  sensations by digital platforms. Based
on  these  data  inputs,  AI  driven  credit  scoring  algorithms  will  be  able  to  produce  more
comprehensive, real-time, and contextualized  risk scores.  In the case of  underserved small
businesses, these systems provide an opportunity to be judged fairly- not just based on strict
credit scores, but on a wider set of variables that show better predictive abilities. Explainable
AI approaches such as SHAP (SHapley Additive explanations) can be used to interpret the
decision-making  process  of  the  model  and  be  transparent  and  compliant  with  regulation.
Such  interpretability  is  needed  to  satisfy  stakeholders  with  increased  trust  in  terms  to
minimize possible biased models [10]. Banks applied with the AI in credit scoring indicate
better loan approvals, reduced default loans and better customer interaction. Deploying AI in
a responsible way needs to deal with ethical implications of data privacy, data fairness, and

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

61

algorithmic responsibility. When applied properly, AI can transform the credit systems into
more  inclusive,  quantitatively-based,  and  adapted  to  peculiarities  of  the  microenterprises
financial realities in the United States.

E. Research Problem

The access to credit by small businesses in the United States has remained a systemic issue
among  under-resourced  small  business  owners  since  they  are  serviced  by  none  of  the
traditional  credit  rating  systems  [11].  These  models  tend  to  dissociate  non-traditional
borrowers  or  borrowers  with  limited  financial  histories,  thus  barring  equal  access  to
financial applications and potential prosperity. Even though there is a range of different data
and AI capabilities, credit scoring models that are robust, scale, and explainable to the needs
of  the  small  business  borrowers  are  not  available.  This  study  aims  to  address  that  gap  by
creating AI-driven credit scoring models that use alternative data to better predict the risk of
loan  defaults,  increase  financial  inclusion,  and  enable  lenders  to  implement  more  accurate
and equitable decisions.

F. Research Objective

The purpose of this  study is  to  generate AI-assisted credit scoring models  with  alternative
data on underserved small businesses in the United States.

➢  To evaluate shortcomings of conventional credit scoring systems.

➢  As an inquiry into the possibility of using alternative data in calculating credit risks.

➢  To implement machine learning to cash loan default prediction.

➢  To measure the model performance on their accuracy and interpretability.

➢  To increase access to credit by businesses which have not got a good financial history.

➢  In  the  form  of  giving  something  back  to  society  to  ensure  that  it  is  beneficial  in

providing ethical, inclusive financial technology tools.

G. Research Questions

This  study  estimates  the  most  important  questions  regarding  AI-based  credit  scores  and
alternative data:

1.  What  does  it  mean  to  exclude  small  businesses  when  it  comes  to  accessing  finances

through the models of a traditional credit process?

2.  Does alternative data help to increase loan default prediction accuracy?

3.  Which is the AI model that offers maximum discrimination and interpretability?

H. Significance of Study

This study is important in terms of financial inclusion and the role of artificial intelligence
(AI) in credit risk assessment, which is rapidly expanding [12]. Conventional credit scoring
models do not always reveal the maximum potential of the owners of small businesses who
are not  always  served or adequately banked. This study shores up a major loophole in  the
present-day  loaning  paradigm  by  creating  AI-based  credit  score  models  using  alternative
data, including education status, marital status, levels of income, and repayment history. The
results  would  provide  an  avenue  to  the  more  realistic,  fairer,  more  individualized,  credit
assessment.  Not  only  does  this  create  a  more  likely  avenue  of  loan  approvals  to  small
businesses that show no formal history of credit it lessens risk to the lenders as the capability
to predict loan defaults is improved. In addition, the demographic and behavioral data helps
to  minimize  systematic  biases  inherent  to  conventional  scoring  models  driving  a  more
equitable financial ecosystem. The findings of the research enable the financial institutions

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

62

to offer credit facilities to the high potential borrowers whose services have until then been
out  of  reach  of  mainstream  credit  availability  [13].  Finally,  the  study  facilitates  economic
growth since it allows small companies to obtain capital they require to develop, innovate,
and hire new workers--and establish a new precedent on AI in financial services.

II. Literature Review

A. Traditional models of Credit Scoring: History and Constraints

The conventional credit scoring has always depended on the structured financial indicators
in  determining  the  creditworthiness  of  a  borrower.  Some  of  the  important  considerations
made  by  the  models  e.g.  FICO  and  Vantage  Score  are  payment  history,  amounts  owed,
length  of  credit  history,  type  of  credit  used  and  new  credit  inquiries  [14].  The  models  are
highly  widely  written  and  implemented  in  their  simplicity  and  scalability  and  their
productiveness in high income lending markets that are structured. Their relevance to small
enterprises  including  those  with  little  or  no  formal  credit  engagement  is  being  challenged
more and more. A number of micro and start up business ventures are conducted informally
with no distinct line between personal and business finances [15]. Therefore, they might not
have  a  credit  record  to  the  signals  that  drive  the  conventional  scoring  systems.  Recent
research  points  to  deficiency  of  such  models  in  capturing  real-life  business  environments
especially  among  the  women/minority-owned  businesses  which  may  not  access  formal
financial services. Critics claim that credit scoring is historical and that it is always late and
reactionary,  is  mostly  dependent  on  past  records  and  does  not  take  cues  on  changing
financial  behavior.  Various  documents  have  mentioned  that  these  systems  have  the
socioeconomic  bias  system  at  their  core,  which  has  led  to  the  unfair  concentration  of
borrowers of underserved groups. These are giving rise to  researchers and institutions that
are  pursuing  more  holistic  credit  assessment  systems  that  look  into  the  future  [16].  As  a
reaction  to  this,  a  growing  literature  is  devoted  to  improving  or  superseding  these  models
with machine learning based systems that are capable of working with both structured and
unstructured  information.  Although  regulatory  compliance  and  protecting  against  risks  is
advantageous,  traditional  credit  scores  are  not  flexible  or  inclusive  enough  to  support  the
financing  of  various  small  business  borrowers  and,  therefore,  innovation  in  the  segment
would be necessary.

B. Evolution of Alternative Data in the Financial Services

The  concept  of  alternative  data  has  attracted  more  attention  over  the  past  several  years
because of its potential to resolve the discriminatory aspects of the traditional credit scoring
systems.  Alternative  data  can  be  defined  as  data  not  covered  by  conventional  financial
accounting,  such  as:  payment  of  utilities,  history  of  rental  property,  use  of  social  media,
behavior in online e-commerce stores and use of mobile phones.  The World Bank and the
International Finance Corporation have found out that using alternative data when analyzing
credit  risks  allows  enhancing  access  to  finance  by  a  large  margin,  particularly  in  the
underserved population. Led by financial technology (fintech) companies, digital footprints
are helping to fill information gaps and enable the borrowers who would otherwise be under
financial  radar  (known  as  the  credit  invisible)  to  be  evaluated.  Alternative  data  has  been
proved as predictive in academic research. As part of an illustration, research has affirmed
that  paying  bills  on  rent  and  utility  on  time  are  good  indicators  of  financial  responsibility
[17].  Other  scholars  have  tested  whether  mobile  wallet  usage,  geolocation  tendencies,  and
even psychometric data, could serve to signal reliable creditworthiness. The following types
of data sources  provide  a more detailed picture of a borrower in  terms  of his/her financial
life,  stability,  and  personality.  In  a  growing  economy,  in  a  gig  economy  type  of  business
model, the use of alternative data has been proven to be an invaluable addition to inclusive
credit  assessment.  There  is  still  apprehension  about  the  quality  of  data,  standardization  of

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

63

data  and  confidentiality.  There  is  no  regulation  on  the  use  of  alternative  data,  which  can
cause both ethical and legal issues. Its strategic application in credit scoring has been on the
increase largely due to the technological gains made in big data processing, API and cloud
computing.  Literature  continues  to  provide  importance  over  the  use  of  alternative  data,
exemplifying the democratizing of financial services amongst small businesses which do not
have access to formal banking infrastructure.

C. Credit Risk Assessment with Machine Learning

Machine Learning (ML) techniques have been very useful in developing credit risk models
and  presenting  new  features  to  these  models  such  as  the  capability  to  learn  non-trivial
patterns in data, dynamic update capabilities, and non-linear relationships between variables.
The Logistic Regression, Decision Trees, Random Forest, Gradient Boosting Machines, and
Neural  Networks  are  four  other  algorithms  that  have  been  used  extensively  both
theoretically  and  practically.  Such  models  have  exhibited  a  very  high  success  rate  as
compared to  the use of  classical  methods of statistics  in  situations  where data is  large and
wide [18]. A key benefit of ML is that it can consume and process alternative data sources in
addition  to  traditional  metrics  and,  therefore,  produce  more  informative  insights  that  can
result  in  more  individualized  risk  assessments.  Comparative  studies  that  have  been  done
concerning ML models and the conventional credit scoring systems have all concluded that
this  former  has  a  higher  accuracy,  low  false-positive  rates,  and  better  borrower  risk
segmentation  [19].  The  Random  Forests  and  the  Gradient  Boosting  have  proven  to  be  the
best  at  uncovering  loan  defaults  in  imbalanced  data.  In  addition,  methods  such  as  cross-
validation,  hyper  parameter  optimization,  and  ensemble  methods  have  been  employed  to
maximize model performance in terms of robustness and generalization. Less interpretable
Deep  learning  techniques  have  been  used  in  large  scale  lending  settings  with  potentially
complex data about individual borrowers. Among the major criticisms of machine learning
applied  to  credit  scoring  is  the  fact  that  many  machine  learning  models  are  considered  a
black-box;  it  is  unknown  exactly  how  they  work.  Strict  regulatory  agencies  like  the
Consumer Financial Protection Bureau (CFPB) insist on transparency and explain ability in
credit made decisions. Due to this, interpretable ML techniques explain ability frameworks
such  as  SHAP  (SHapley  Additive  Explanations)  and  LIME  (Local  Interpretable  Model-
Agnostic Explanations) received attention in recently published literature. On the whole, ML
integration has made credit risk models to be more precise, customizable, and all-inclusive,
particularly when dealing with non-traditional borrowers.

D. Small Business Credit Scoring using AI

Data scarcity, heterogeneity of business, and volatility in operations pose unique difficulties
to  the  creation  of  credit  risk  models  in  small  business  lending.  These  businesses  are
classically erroneously tabulated because they do not have regular documents or revenues;
or, because of a lack of collateral [20]. As a result, researchers, and practitioners are paying
an increasing amount of attention to AI-powered credit scoring along the lines that will be
subjected
to  different  small  business  finance  peculiarities.  Such  AI  models  can
accommodate  more  input  variables  such  as  transactional  information,  cash  flow  trends,
industry-specifics,  and  socio-psychological  indicators,  which  enables  them  to  have  a  more
comprehensive indication of business credit-worthiness [21]. The latest studies have pointed
to the favorability of AI models that minimize credit exclusion and improve credit approvals
of  underserved  small  businesses.  To  illustrate,  fintech  marketplaces  like  Kabbage  and
OnDeck  have  implemented  AI  to  automatically  evaluate  risk  using  indicators  of  business
performance  in  real  time.  The  models  go  not  only  beyond  static  credit  history  to  include
dynamics such as point-of-sale, online reviews, supply chain activities and so on. Scholarly
research substantiates the idea that the AI models can better the historical scoring systems in
small  business  scenarios  in  terms  of  providing  access  to  granular  segmentation,  consistent

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

64

model updating, and increased processing speed. There continue to be issues around model
validation, data privacy, and fairness. The small businesses are cautious about the way their
data is gathered and utilized and Lenders need to ensure that they do not introduce implicit
bias into models [22]. Regulative and ethical systems are hence essential in the process of
implementing  AI.  All  in  all,  the  existing  literature  substantiates  the  promises  of  AI-based
credit  scoring  as  a  channel  to  the  establishment  of  equitable,  data-driven  lending  to  small
businesses that cannot be missed in a traditional approach.

E. Financial Inclusion and the Under-Served Market

Financial  inclusion  means  the  prevention  and  parity  of  the  chances  to  use  the  financial
services.  The  reports  produced  by  the  international  authority  bodies,  like  the  World  Bank,
IMF and the Federal Reserve, indicate that millions of small enterprises in the United States
have  been  left  behind  in  the  major  financial  institutions  [23].  This  ostracizing  is  due  to
stringent credit standards, geographical inaccessibility, cultural and linguistic difference and
absence of institutional relationships in banking. Such elements affect the businesses owned
by  women,  minorities,  and  those  located  in  rural  areas;  commonly  known  as  the  credit
invisible. Controlling studies have the capacity to verify that increased accessibility to credit
has the effect of increasing the business survival level, employment and economic strength.
Other  credit  scoring  options  such  as  AI-  and  alternative  data-driven  ones  are  increasingly
being seen as vehicles of financial inclusion. Such models allow new entrants into the credit
system  without  undermining  risk  standards  since  redefining  [24].  Some  case  studies  even
attract  a  success  story  whereby  smaller businesses were  able to finance loans available on
mobile  transaction  records  or  peer  ratings  as  opposed  to  the  traditional  credit  files.  In
addition, a recent state of the literature focuses on the fact that inclusive credit models are
not just socially beneficial, but commercially beneficial as they identify a huge underserved
market. Responsibility has to balance inclusion [25]. There exists the possibility that a badly
formed  design  should  result  in  excessive  indebtedness  or  discriminatory  behavior.
Therefore, scholars attach great significance to the concept of fairness audits, transparency,
and  user  education  as  part  of  any  financial  inclusion  plan.  The  literature  argument  that
modern, responsible use of AI-driven  credit scoring  has the potential to  even the financial
playing field  in  the U.S.  small  business  market  and create a more just economy  is  hard to
refute.

F. Empirical Study

The  article  by  Richa  Lomas  and  Reeta  called  AI-Driven  FinTech  Solutions  to  Financial
Inclusion: A Study on Empowerment of MSME Sector empirically discusses the value of AI
technologies  in  ensuring  financial  inclusion,  especially  to  the  Micro,  Small,  and  Medium
Enterprises  (MSMEs),  which  have  little  access  to  formal  banking  systems.  The  research
reveals  how  the  AI-driven  FinTech  platforms  use  machine  learning,  analytics  of  data,  and
alternative  data  sources  to  improve  credit  evaluation,  risk  analytics  and  personalisation  of
their services to the MSMEs. The AI systems will offer more comprehensive, equitable, and
reachable financial solutions since they address the shortfalls of conventional credit scoring
systems, including the lack of formal credit histories. The paper presents some of the major
advantages including enhanced availability of cheap credit, enhanced efficiency, and growth
of  operations  to  unserved  areas  [1].  It  recognizes  the  existence  of  vital  challenges  such  as
data  privacy  issues,  adherence  to  regulations,  and  digital  literacy  gap  among  owners  of
MSMEs.  The  empirical  evidence  can  be  viewed  as  the  premise  behind  this  study,  which
promotes the adoption of AI-driven credit scoring solutions to help small business borrowers
and  achieve  inclusive  economic  development.  The  article  is  a  good  source  of  reference  in
appreciating  the  practical  effect  of  AI  among  the  underserved  participants  in  the  financial
ecosystem.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

65

In  the  article  by  Ga  Young  Jang,  Hyoung  Goo  Kang,  James  Park,  and  Hyung-Suk  Choi
titled  AI-Driven  Credit  Scoring  and  Market  Transformation:  How  ACSS  Reshapes  SME
Financing,  Firm  Strategy,  and  Regulatory  Boundaries,  the  authors  argue  an  empirical  case
regarding the remaking of the market by alternative credit scoring systems (ACSS), driven
by AI and big data, which have provided the potential to transform the funding structure of
small  and  medium-sized  enterprise  (SMEs).  The  paper  examines  the  use  of  ACSS  by
platform  companies  to  succeed  within  harsh  regulatory  frameworks  deploying  credit  in
underbanked  small  and  medium-sized  enterprises  and  driving  inclusive  financial  systems.
These systems use non-traditional data points and AI algorithms to provide better estimates
of creditworthiness,  and  as a  result even businesses  with  little historical  financial data can
take out external capital to drive growth [2]. The study brings out the instrumental usage of
the platform companies as the driver of the regulatory reforms and competitive redrawing of
industry  borders.  The  present  research  is  supported  by  these  empirical  findings,  which
proved the necessity of introducing AI-based credit models because they not only optimize
the  SME  financing  process  but  become  drivers  of  market  and  regulatory  changes  in  the
entire  National  Market.  The  article  is  a  good  resource  to  the  policymakers,  financial
institutions  and  developers  of  technology  who  aim  at  attaining  a  balance  between
innovation, management of risk, and economic inclusion. It supports the significance of AI
in supporting the sustainable empowerment of the SME and creating a financial system that
is more favorable to the equal importance of human beings.

In  the  article,  The  Role  of  Data  Analytics  in  Enhancing  Financial  Inclusion  in  Emerging
Economies by Oluwabusayo Adijat Bello, the author highlights the role that data analytics
can play in reducing the gap between financial inclusions across emerging economies. Using
alternative data sources to detect underbanked populations such as mobile usage patterns and
online payments habits, financial institutions are able to detect them better, optimize credit
scoring and organize financial services to a wider range of socioeconomic needs. The study
is  specifically  applicable  to  the  present  study  in  terms  of  disclosing  the  benefits  of  data-
driven  approaches  to  fostering  inclusivity  by  breaking  the  existing  structural  boundaries
such as remote geographical location and the absence of an established formal credit profile.
The examples of effective implementations,  described by Bello, such as Kenya M-Pesa or
the  Indian  Aadhaar-enabled  digital  lending  provide  a  tangible  example  of  what  analytics-
driven  innovation  is.  The  paper  discusses  such  essential  dilemmas  as  data  privacy,
regulatory restrictions, and infrastructure shortages that have to  be negotiated to  guarantee
sensible  and  sound  deployment  [3].  The  combination  of  upcoming  technologies  like  AI,
blockchain, and IoT reflects a vision of the blueprint of an inclusive financial ecosystem in
the  future.  In  general,  the  insights  that  Bello  presents  in  his  work  help  to  understand  how
data analytics allows institutions to create fairer financial systems, which is compatible with
the larger initiative to decrease poverty and achieve sustainable development.

The  article  by  Elijah  Nguyen,  The  Role  of  Big Data  and  AI  in  Real-Time  Credit  Scoring,
provides an in-depth investigation of the changes that the modern financial system faces due
to  the  advent  of  new  technologies,  especially  those  related  to  real-time  credit  scoring.
Nguyen  stresses  that  the  current  systems  of  credit  scorecards,  e.g.,  based  on  FICO  scores,
are insufficient in assessing people or SMEs with no formal credits. With input of big data
sources, such  as  online  behavior, digital transaction  history, and other alternative financial
measurement  sources,  AI-based  models  can  provide  more  rapid  and  comprehensive  credit
ratings.  Such  models  especially  that  based  on  machine  learning,  further  improve  risk
prediction  accuracy  and  the  models  self-improve  themselves  using  iterative  learning.
Notably, the article falls in line with the stated goals of this study by showing how big data
and  AI  have  already  managed  to  fill  historical  inclusion  gaps  in  the  world  of  finance  [4].
Nguyen critically brings up some of the ethical and regulatory issues that are associated with

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

66

the  implementation  of  AI  within  financial  decision-making  including  privacy  of  data,
fairness of algorithms, and transparency of models. His observations serve as an appropriate
background  to  the  idea  of  how  the  use  of  advanced  analytics  tools  can  transform  credit
access  of  the  marginalized  group  enabling  as  well  to  draw  attention  to  the  necessity  of
responsible  innovation.  This  piece  of  work  makes  a  significant  contribution  to  continued
scholarly and practice-related discourse concerning the usage of technology to create more
equitable, efficient and speedier credit systems around the world.

In  the  chapter  FinTech  and  Artificial  Intelligence  to  Sustainable  Development  by  David
Mhlanga,  the  nexus  of  financial  innovation  and  alleviation  policy  from  the  prism  of  the
United Nations Sustainable Development Goals (SDGs), namely SDG 1: ending poverty, is
revealed. Mhlanga gives an emphasis on how FinTech and artificial intelligence (AI) may be
critical  towards  the  achievement  of  inclusive  growth  and  economic  empowerment  in
developing  region.  Using  the  capabilities  of  an  AI-enabled  tool,  the  chapter  explains  the
means in which underserved populations can receive greater access to financial services and
such  financial  tools  as  digital  wallets,  microloans,  and  mobile  banking  applications.  It  is
important  to  note  that  these  technologies  have  encouraged  not  only  a  diminution  of  the
drawbacks attached to the traditional banking system, namely the physical distance involved
and the bureaucratic red tapes, but simplified the process of sending aid and raising financial
literacy [5]. The chapter questions how, with the incorporation of AI FinTech solutions, real-
time  credit  evaluation  and  fraud  detection  will  be  possible  making  lenders  comfortable
funding  small  and  mediocre  enterprises  (SMEs)  which  are  the  key  to  the  local  economic
growth.  In such innovations,  FinTech acts  as a source of employment, wealth-distribution,
and social mobility. Mhlanga seeks long-term cooperation with governments, companies in
the  field  of  technology,  and  global  organizations  to  introduce  these  technologies  in  a
controlled,  ethical,  secure,  and  inclusive  way.  His  perspectives  give  formidable  theoretical
and practical support to how AI-based financial systems can eliminate poverty and promote
sustainable development.

III. Dataset

A. Screenshot of Dataset

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

67

B. Dataset Overview

The data used in the study is a multidimensional and exhaustive set that entails credit risk
scoring  with  particular  emphasis  on  small  businesses  borrowers’  loan  lending  model.  It
embraces  a  wide  array  of  variables  that  cross  economic,  demographic,  and  behavioral
variables  that  are  linked  with  creditworthiness  and  default-risk.  The  most  important
characteristics of the data will be the age of the borrower, gender, education level, marital
status,  employment  types,  annual  income,  and  amount  of  loan,  interest  rate,  length  of  the
loan,  credit  history  status,  the  number  of  previous  defaults,  and  the  current  default  status.
The  sample  size  in  the  dataset  is  thousands,  which  will  guarantee  a  good  number  of
observations  to  be  used  to  train  the  models,  validate,  and  evaluate  the  performance.  It  is
realistic in terms of diversity in borrowers as it includes both the traditionally employed and
self-employed  individuals,  a  broad  range  of  the  various  income  brackets  and  educational
levels. Data structure is clean, well-labelled and can be used in machine learning tasks, and
the minimal  missing values with  the existence of categorical  variables which are correctly
encoded [65]. The selection of each variable was made in a way that they could be relevant
to modeling of credit risk and statistical methods of normalization and correlation analysis
were  used  to  analyze  data  distribution  and  important  predictive  characteristics.  Using
Tableau and Python allowed determining the important trends as well, high default rates on
specific  levels  of  education  or  employment  status  or  having  an  uneven  distribution  of
income  among  the  types  of  the  borrowers.  Such  an  inclusion  of  the  defaulted  and  non-
defaulted  cases  was  used  to  construct  balanced  predictive  models  and  evaluate  bounded
classification  accuracy  in  the  research.  The  richness  and  relevance  of  the  dataset  not  only
facilitated the construction of rigorous algorithmic models, but potentially rich insights with
regard to socioeconomic trends on the loan repayment behaviors. It is thus especially useful
in  the  development  of  inclusive  credit  scoring  models  that  will  be  sensitive  to  the  lived
experience of underserved borrowers.

IV. Methodology

This  study  used  a  quantitative  research  method,  through  AI  and  machine  learning
application,  to  investigate  the  tendency  of  loan  defaults  by  small  business  loan  recipients.
The data follows a credible financial database whose data were preprocessed to deal with the
missing data, categorical variable encoding, and normalization of numerical variables [26].
Decision tree, logistic regression, and random forest are predictive models that were trained
and  validated  in  their  support  of  assessing  default  risk.  Tableau  and  Python  are  data
visualization tools that were applied to find a relationship amongst the variables; education,
marital  status,  employment  and  income.  To  determine  whether  model  performance  was
robust  and  predictively  fair,  accuracy,  precision,  recall  and  F1-score  were  used  to  assess
performance.

A. Research Design

The research employed in this study is of a quantitative exploratory design to investigate the
interaction  between  credit  scores,  default  rates  and  interest  rate  distributions.  The  ultimate
goal  is  to  uncover  quantifiable  trends  and  information  with  guided  data  found  on  lending
websites [27]. Quantitative research can easily be analyzed due to statistical analysis, and it
is thus easy to establish relationships, trends, and differences in variables like credit scores,
annual  income,  loan  amounts  and  the  interest  rate.  The  exploratory  aspect  enables  one  to
complete  the  study  in  the  locations  where  there  is  little  research  or  pre-determined
hypotheses  to  find  the  unknown  or  unexpected  connections  in  the  data.  This  study  design
was especially appropriate since the research not only aimed at testing theories, but it aimed
at creating other ideas. Using this methodology we can investigate various aspects that shape
the behavior of the borrower and the consequences of a loan [28]. These data were analyzed

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

68

with data visualization, statistical description, and correlation. Combination of tools such as
Python,  Excel,  and  Tableau  was  applied  so  as  to  improve  the  strength  of  the  approach.
Python allowed the extensive numerical analysis, whereas Tableau provided the possibility
of pattern identification by visualization. Excel provided the chance to manage the primary
data and conduct rapid reviews. All in all, the design is clear, objective and replicable. The
structure can be used in future predictive modeling or machine learning related to financial
decision-making as it has a solid base.

B. Data Collection

This study used data on a publicly available lending dataset, entailing detailed information
of  borrowers  (credit  scores  and  interest  rates,  annual  income,  loan  amounts,  co-signer
information,  and  the  purpose  of  loans).  This  information  consists  of  thousands  of  loan
application data, which provides a sample of different loan applicant profiles and risk. The
process  of  collection  commenced  with  the  importation  of  the  data  to  the  Microsoft  Excel
program  to  observe  the  structures,  degree  of  completeness  and  simple  formatting.  This
permits preliminary cleaning- elimination of doubles, resolution to missing values, and input
of  inconsistent  entries  [29].  Then,  the  cleaned  data  was  sent  to  Python  and  Tableau  and  a
more  in-depth  analysis  was  done.  Advanced  filtering,  transformation,  and  exploration  of
data  were  carried  out  in  Python  through  libraries  such  as  Pandas.  Interactive  visual
dashboards capable of absorbing more patterns  were  created on Tableau. All  records were
reviewed with the aim of ensuring that they fell within the objectives of the study, especially
the attributes such as credit score grouping, default record and the loan classification [30].
The data further got arranged in a way that they could be subdivided, i.e., evaluation could
be performed between loans with or without a co-signer or how the effect of income level on
interest  level  worked.  The  data  collection  protocol  focused  on  reliability,  reproducibility,
and moral responsibility since all the information was anonymized and applied to academic
learning and analytical aspects only.

C. Data Preprocessing

Preprocessing of the data helped to verify the quality, consistency, and relevance of the data
that  was  to  be  analyzed.  The  first  one  was  locating  and  manipulating  data  that  was  not
present. Null values in unimportant fields were dropped, whereas the missing/ invalid values
in important/ key variables like the credit score and interest rate were not dropped to retain
large  missing  value  entries  [31].  Outliers,  i.e.,  unrealistic  amount  of  income  or  loan  being
negative would skew any result of the analysis, were removed from the dataset. In python,
pandas  and  NumPy  were  used  to  do  preprocessing,  in  which  normalization  and  encoding
transformation  were  performed.  Categorical  fields  such  as  the  loan  purpose  were
transformed to numbers using label encoding that allowed the correlation to be determined.
Credit scores became categorized into ranges such as Poor, Fair, Good, and Excellent) that
could easily be visualized and contrasted. Likewise, the annual income was segmented into
brackets to find out patterns among income brackets. In Tableau, it used calculated fields in
order to segment and aggregate variables in the form of visual grouping. They filtered and
sorted  the  data  so  that  data  that  was  not  relevant  such  as  business  loans  or  missing
applications  were  missing  [32].  Preprocessing  procedures  made  the  data  to  be  correct,
complete  and  fit  to  further  statistical  and  graphic  analysis.  This  intense  procedure  gave  a
good  basis  to  develop  insights  and  recognize  the  trends  and  reduce  errors  during  later
development of results interpretation.

D. Analysis Techniques and Tools.

The  study  involved  the combination  of  Excel,  Python,  and  Tableau  to  process  and  thus  to
visualize the dataset. All the tools had their own contribution to the purposes of the research.
The first step was the importation of data and generation of summary statistics with the help

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

69

of Excel in order to obtain quick visualizations [33]. It enabled rudimentary sorting, filtering
and  producing  pivot  tables  in  order  to  determine  distributions  by  borrower  category.  The
deeper analysis engine was python. The data was investigated via the correlation matrices,
regression functions, and clustering operations with the use of libraries, Pandas, Matplotlib,
and  Seaborn.  As  an  example,  a  correlation  heatmap  was  made  to  comprehend  the
interconnection  of  interest  rate  and  credit  score  with  line  plots  demonstrating  directional
movement among brackets of scores [34]. The discussions about default rates in dependence
on income and the co-signer presence exist with the help of Seaborn which helped to create
thoughtful  scatter  plots.  Dashboards  that  were  visually  intense  were  developed  through
Tableau. Using a drag-and-drop with an intuitive interface, Tableau allowed dynamic filters
and  dashboard  designs  that  could  display  the  variations  in  the  interest  rates,  loan  purpose
and the risk profiles of the borrowers. It was able to provide depth and clarity in the analysis
due  to  integration  of  these  tools.  It  gave  us  the  possibility  to  analyze  raw  data  multi-
dimensionally,  synthesizing  numbers,  statistics,  and  graphical  views.  This  mix-up  of  tools
increased the interpretability and reliability of the final finding of the research.

E. Data Visualization Method

Data  visualization  systematically  entered  into  a  central  aspect  of  this  research  because  the
insights  of  the  large  sets  of  data  were  translated  into  meaningful  patterns  and  trends  [35].
With  Tableau,  different  types  of  analysis  were  visualized  to  help  in  analysis  such  as  bar
graphs,  scatter  plots,  lines  graphs,  and  histograms.  The  intended  goal  behind  the
visualization  strategy  was  to  ease  the  comprehension  of  complex  relationships  especially
one  that  involved  multivariate  such  as  credit  score,  default  rate  and  interest  rate  [36].  The
credit scores were entered in categories and colored to show how various brackets affected
interest  rates  and  the  chances  of  getting  loans  based  on  them.  The  existence  of  the
correlations between default rates and co-signer  status  or income level  was pointed out  by
scatter plots. The line graphs presented the trend of the decrease or increase in the interest
rates on the basis of credit score band. The usage of interactive filters on Tableau dashboard
enabled adding the option to narrow down on a specific subgroup of individuals having co-
signers or a loan purpose. Such dynamic graphics were complemented by Matplotlib-based
and Seaborn-based plots generated in  Python,  in particular regression lines and correlation
matrices [37]. The visualization plan did not only add beauty to the visualization of data but
made  it  easy  to  interpret.  It  allowed  readers  and  stakeholders  to  get  the  essential  insights
without spending a lot of time working through the data presented in raw numerical forms.
There was an emphasis of insights and relationships when using the visualization approach
as it enhanced the presentation and impact of the research.

F. Ethical consideration and limitations

Ethical  integrity  was  a paramount utmost  requirement that took  priority in  this research in
handling and analysis of data. Any data employed was anonymized and obtained through a
publicly available database, so that no personal identifiers were in the data. The research did
not involve any discriminatory profiling because the variables used were only numeric and
categorical  and  did  not  include  the  concept  of  profiling  using  different  factors  like  color,
religion,  etc.  As  to  limitations,  the  data  represent  the  history  of  trends,  and  it  might  not
measure both the current shifts in the economy and the new lending policy alterations [38].
Variables such as employment history of the borrowers or macro-economic factors have not
been discussed that could come into play in risk assessment of credit. It is restrictive in the
sense  that  the  data  used  is  not  dynamic;  in  other  words,  it  is  not  updated  in  real  time.
Nevertheless,  the  limitations  notwithstanding,  the  methodology  used  retains  its  value  and
applicability when it comes to underlying ideas and can be used on the basis of more recent,
and comprehensive data.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

70

V. Result

The findings of this study present important findings regarding lending patterns of this group
of small business borrowers with focus on the demographic and socio-economic factors. The
borrowers of lesser education status, single and with less job tenure had higher probability of
defaulting [39]. In the visual analysis, it was stressed that employment type, income level,
and  repayment  behavior  were  strongly  associated  with  each  other.  The  results  affirm  the
successfulness  of  AI-amplified  credit  models  incorporating  variations  of  non-conventional
information inputs. With these insights, it allows lenders to make a better assessment of risk
and support financial inclusion by financing the small firms, which fall through the cracks of
the traditional credit scoring model.

A. Default Rates Analysis by Employment Type

Figure 1: This image displays the average default rate per employment type according to
four employment categories

Examining the relationship between employment type and default risk is important to ensure
the  inclusiveness  of  credit  scoring  models,  particularly  among  the  small  business  owners
that are underserved financially.  As shown in  Figure 1, the average percentages of default
occurred in four types of employment which included Full-time, Part-time, Self-employed,
and  Unemployed.  This  observation  proves  in  the  analysis  that  the  employment  status  can
determine  and  contribute  to  the  credit  risk  greatly,  explaining  why  artificial  intelligence-
enabled credit score systems  need to  consider other employment-related  assets. As seen in
the  chart,  the  highest  average  level  of  default  is  among  unemployed  people,  amounting  to
that of 0.14. Understandably, this is the case given that unstable income has a direct impact
on the capabilities of an individual to repay debt. Close behind are part-time workers with an
above average default rate of around 0.12 that has been attributed to the instability of their
income  and  earning  potential  in  comparison  to  the  full  time  parties.  Interestingly,  self-
employed  people  have  relatively  high  default  rates  (~0.115)  indicating  that  despite  having
income  streams,  the  volatility  and  unreliability  of  entrepreneurship  may  affect  their  credit

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

71

worthiness.  The  average  default  rate  is  the  lowest  among  full-time  employees  but  a  little
more than 0.10. This means they are in more secure financial status and stability that makes
them reliable lending in the eyes of lenders. This reflection makes it clear that the tendency
toward  binary  measures  of  employment  obscures  the  issue  and  instead  there  is  a  need  to
examine the quality of employment, stability of incoming, and the kind of self-employment
[40]. The use of such granular data by AI models allows a better separation of risk profiles
and  a  decreased  level  of  bias  against  self-employed  or  informally  employed  people.  This
further confirms why alternative data plays a vital role in making credit more democratic by
paying  attention  to  the  idiosyncratic  financial  circumstances  of  small  business  owners  of
varied employment statuses.

B. Credit Score Analysis by Marital Status

Figure 2: This image displays the mean score of credit rating according to marital status
based upon three specific categories

Figure  2  shows  the  mean  credit  score  divided  by  marital  status  with  three  attributes  as
Divorced,  Married  and  Single.  In  both  conventional  and  alternative  credit  ratings,  credit
score  is  an  important  parameter  that  highlights  the  capacity  and  the  possibility  that  an
individual is best able and most likely to repay the money borrowed. The knowledge about
the effect  of marital  status on credit scores may  help  to  optimize AI-related credit scoring
algorithms  and  the  identification  of  possible  culturally-based  biases  of  credit  scores
analytical tools. The chart shows that there is a slight difference in the means of the average
credit scores of the three marital statuses where divorced people have the highest mean score
of  about  574.8,  followed  by  married  (about  574.2)  and  single  (573.6).  Although  the
difference  is  somewhat  minimal,  the  persistence  of  better  credit  scores  of  divorced  and
married  people  based  on  current  trends  over  single  people  might  be  an  indication  of  the
stabilization effect of joint financial commitments or long-term financial behavior developed
within  a  marriage.  Therefore,  one  should  remember  that  marital  status  can  be  used  as  a
proxy  indicator  of  other  financial  variables  like  there  may  be  two  incomes  of  households,
two  credit  accounts,  or  varied  amounts  of  debt  accrued  by  individuals.  The  behavioral

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

72

patterns represented by these nuances may not be obvious in the conventional frameworks
but  may  be  more  effectively  measured  with  the  help  of  the  AI-powered  solutions  that
evaluate a wider range of the behavioral and transactional data. In the small business lending
point  of  view,  particularly  with  reference  to  the  low-end  financially  underserved  groups,
extreme dependency on a marital status when making credit decisions can continue to cause
inequitable  discriminations.  Consequently,  marital  status  should  be  added  to  the  list  of
contextual aspects of the AI models but should be mixed with alternative data that is more
dynamic  to  achieve  a  more  fair  and  precise  scoring  [41].  This  number  supports  the
importance of thoughtful design of the AI models in which parameters such as marital status
are computed with a combination of other signals and not individually.

C. Average Income Distribution by Income Bin and its Analysis

Figure 3: This image represents average income over income bins of increasing income,
up to 150K from 10K

Figure 3 shows the mean income by the different income bins, which provides a micro level
look  at  income  distribution  among  people  within  the  dataset.  The  horizontal  axis  provides
the  segmented  delivery  of  income  (bins)  between  $10K,  up  to  150K,  whereas  the  vertical
one indicates the average income on the same receiving scale. The graph shows that there is
a definite and linear upward slope on the level of income which implies that the data is well-
organized and distributed equally among the classes in terms of the economy. The income
levels  start  with  a  minimum  of  around  15260  dollars  and  they  progress  to  around  149834
dollars representing the whole picture of economic diversity- through low income earners to
high  earners.  To  come  up  with  inclusive  AI-powered  credit  scoring  models,  especially  in
underserved small enterprises in the U.S., this type of distribution is critical since it prevents
the training data set to be biased in favor of a specific economic segment. One important fact
that can be observed in this figure is that the increment in income is predictable and there are
no  inscrutable  outliers  or  noise  in  the  data  of  the  income.  Income  is  one  of  the  basic
determinants of the ability to repay loans in the case of small businesses in terms of building
a model of credit. The use of income alone is always misleading; this is particularly relevant

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

73

in  the  case  of  individuals  who  are  self-employed  or  micro-entrepreneurs  because  their
income  might  not  be  constant  but  steady  in  a  long-lasting  period.  Consequently,  this
visualization supports the idea that to improve the ability to assess the financial stability of
people  whose  incomes  are  not  steady  to  formal  data,  it  is  important  to  use  nontraditional
indicators,  which  can  be  transaction  history,  digital  activity,  or  payment  of  utilities,  that
would  be  more  relevant  to  the  financial  trustworthiness  of  people  with  irregular  formal
income. Figure 3 evidences the argument in the paper that, as critical as income may be, it
must be put into perspective with  other wider behavioral  information  to achieve equitable,
more accurate AI-powered credit scoring.

D. Average Loan Amount, and Defaults by Loan Purpose Analysis

Figure 4: This image presents a comparison of the mean loan and the defaults with
different loan

Figure  4  is  the  comparative  study  of  average  loan  amount  and  number  of  defaults  with
respect  to  various  loan  purposes,  which  are  Auto,  Business,  Education,  Home  and  Other.
The blue bars show the average of loan amount given per purpose whereas the orange bars
show  the  amount  of  defaults  given.  This  two-visualization  gives  insights  on  lending
behavior  or  default  risks  according  to  different  classifications  of  financing.  Based  on  the
chart, it is noted that the average loan amounts tend to remain basically the same across the
types of loans regardless  of the intended use of $127,000 which implies standardized loan
offering  regardless  of  the  type  of  loan  sought.  The  differences  in  absolute  height  of  the
default rates are more discreet though meaningful in respect to the context. Business loans
and auto loans have a little more default numbers than other types of loans such as education
loans or home loans. This would be due to the nature of the business of smaller companies
which  tends  to  be  susceptible  to  any  changes  in  the  market,  minimal  cash  reserves,  or
unstable sources of income [42]. On the same note, auto loans might cater to a more diverse
group  of  people  on  credit,  such  as  those  of  low  credit  rating.  Education  and  home  loans,
have much lower default rates perhaps due to the fact that these types of loans are usually
linked  to  longer  term  investments  and,  perhaps,  a  more  strict  vetting  process,  or

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

74

collateralizing.  The  rest,  labeled  as  other,  does  not  have  its  name  defined  but  is  in  the
moderate  range  in  terms  of  the  amount  of  loan  and  the  number  of  defaults.  Using  this
visualization,  one  can  emphasize  the  role  of  loan  purpose  as  a  predictive  element  in  AI-
enhanced credit scoring systems. Knowledge of the risk behavior of select loan purposes can
greatly  enhance  the  default  prediction  model  and  allow  the  lending  programs  to  be
customized to suit the underserved areas of small business.
E. Evaluation of Marital Status by Average Debt to Income Ratio

Figure 5: This image presents the mean debt-compared to-income proportion by marital
status
The  average  Debt  to  Income  (DTI)  ratio  is  displayed  as  per  each  marital  status,  namely,
Divorced,  Married,  and  Single  which  are  presented  in  Figure  5.  DTI  ratio  is  a  significant
financial  measure  which  is  applicable  in  credit  scoring  and  loan  underwriting  because  it
shows  the  ability  of  a  borrower  to  repay  his  monthly  debts  based  on  his  income.  A  thus
lower DTI is usually the sign of healthier financial stability and less chances of default. The
average of the DTI ratios of all incarnations of marital status are quite near to each other as
depicted in the chart: it is between approximately 0.499 and 0.501, thus indicating a slight
difference  in  financial  leverage  among  members  of  the  different  demographic  groupings.
Between the labels, married people have the highest average of DTI ratio, which is slightly
over  0.501  followed  by  single  and  divorced.  The  low  difference  between  the  three  groups
means  that  maybe  marital  status  is  not  a  strong  discriminator  of  the  DTI  behavior  in  the
dataset. Nevertheless, even minor variations in DTI may make physical implications when it
is scaled to a large scale credit modeling. In this case, married people could have a higher
financial  liability  because  of  joint  liabilities  i.e.  mortgages,  family  costs,  and  hence  their
debts  could  be  more  but  their  income  otherwise  could  be  the  same  or  higher.  Conversely,
divorced  persons  could  have  gone  through  a  reorganization  of  their  finances  after  divorce
that could decrease their debts or distribute them. The use of marital status DTI in AI-based
credit  scores  can  be  used  to  provide  more  individual  and  equitable  experiences.  This  is
consistent  with  the  purpose  of  the  study  of  finding  inclusive  models  describing  their  data
points in a more subtle way of focusing on alternative data besides the conventional credit
history.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

75

F. Defaults by Education and Marital Status Analysis

Figure 6: The image illustrates how the defaults are distributed according to education
and marital status

The focus on the demographics of loan defaults has found its expression in the figure of 6
that contains the detailed breakdown of loan defaults by education level  and marital status
providing  important  information  on  the  impact  of  demographics  on  the  behavior  of
borrowers in terms of credit. Education levels in the graph have been grouped under High
School, Bachelor, Master and PHD and the marital statuses under the categories Divorced,
Married and single. As it can be recognized, high school completions, particularly those who
had  become  single  or  divorced,  are  the  biggest  source  of  defaults,  and  this  signifies  the
increased risk of lending credits to individuals with low levels of schooling. Conversely, the
rate of defaults is significantly lower among those with Bachelor and Master degree levels
thus giving a positive relationship between higher education and being more responsible in
handling their money. The group that shows the lowest rates of defaults is the group that has
PhDs, especially in the age category of married and divorced, to prove the point that senior
levels  of  education  lead  to  improved  repayments  dependability.  In  all  categories  of
education, the single individuals always have the highest default rate whereas the divorced
people  will  have  higher  default  than  the  married  borrowers,  and  there  may  be  several
reasons  as  to  why  the  married  ones  have  lower  rates  of  defaulting  such  as  they  have  the
mutual income or they are more economical. The given demographic trends are necessary to
optimize  the  AI-based  credit  scoring  system,  and,  particularly,  focus  the  latter  on  small
business borrowers in the underserved segment. Incorporation of features like education and
marital  status  not  only  increases  the  effectiveness  of  prediction,  but  directly  helps  achieve
more inclusive and equal lending frameworks [43]. With the acknowledged mixed impact of
education  and  personal  stability,  the  financial  institutions  will  be  able  to  understand  the
reliability of borrowers better than the standard metrics of credit levels. This method ushers
in smarter, fairer and more personified decision-making on credit, leading to wider access to
credit options.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

76

G. Comparing Total Loan Amount based on Loan Purpose and Co-Signer Status

Figure 7: This image demonstrates the cumulative value of loans by purpose of the loan
and co-signer status

Total amount of the loans disbursed during the year with regard to different loan purposes
broken  based  on  the  presence  or  absence  of  co-signers  is  presented  in  figure  7.  Instead  of
providing sub-categorization under each section, the chart contains five labels that are Auto,
Business,  Education,  Home  and  Other  with  further  inclusion  of  information  whether  a  co-
signer  was  involved  or  not.  In  all  types  of  loans,  the  bars  demonstrate  similar  total  loan
amounts irrespective of whether a co-signer is present or not hence suggesting that co-signer
does not greatly change the amount of credit granted in totality. Particularly, the total loan
amounts  are  rather  stable  with  an  average  of  around  3  billion  dollars  in  both  of  the
categories. Such uniformity indicates that lenders disperse huge loans at an egalitarian level
irrespective of the dependency of the borrower to have a co-signer. There is a slight pattern
to note when comparing the heights of the bars, loan amounts are in fact a little bit higher in
some of the categories that involve a co-signer, as in the case of Business and Home loans.
This  can  be  seen  as  a  sign  that  a  co-signer  can  only  give  a  slight  advantage  in  terms  of
access  to  larger amounts of loan, perhaps because of a perceived higher  credit-worthiness.
The conclusions are useful with respect to developing credit scoring models powered by AI
[44]..  Adding  the  co-signer  status  as  a  feature  could  increase  the  accuracy  of  predicting
whether a person will be approved or not in the case of loan applications that are on the edge
of  being  approved  and  on  the  edge  of  being  rejected.  The  availability  of  an  option  of  co-
signing the loan may therefore play an important  role in  loan approvals  and loan  amounts
among small businesses especially when it comes to underserved small business groups with
limited  credit  histories.  This  evaluation  proves  the  benefit  of  more  subtle  credit  modeling
that  can  interpret  borrower  profiles  beyond  the  mainstream  usage  measures-  which  jives
with the objectives of inclusive and alternative-data AI-based credit systems.

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

77

H. Loan Purpose and Co-Signer Status Default Rate Analysis

Figure 8: This image illustrates the defaults according to the purpose of the loan and the
availability of the co-signer

Fig. 8 shows, by loan purpose and status with a co-signer, the impact of credit score and of
default risk on interest rate distribution. On the chart, the average default rates are compared
between  the  corresponding  types  of  loans  (Auto,  Business,  Education,  Home,  Other)  with
those borrowers who have co-signer and those without. Among the major emerging trends,
the backing of a co-signer has its defaulting in all loan applications. Lending under the label
of business and auto loans in the category of No Co-Signer has the worst average defaults-
more than 13 percent-conveying the caution that lenders witness when the borrower has no
second  line  of  financial  support.  On  the  other  hand,  borrowers  who  have  a  co-signer  are
likely to exhibit less of default rates especially under categories of home and education loans
with  averages  as  little  as  around  10%.  This  trend  suggests  that  co-signing  does  not  only
strengthen a borrower in terms of credit worthiness to the lender, but leads to less potential
defaults,  which  was  likely  to  be  instigated  by  shared  responsibility  or  better  financial
sobriety.  Under  a  modeling  angle,  this  number  lends  significant  thrust  to  the  idea  of
including  co-signer  status  as  a  predictive  parameter  in  AI-driven  credit  rating  models.  It
suggests  that  the  other  data  input  loan  purpose  provides  effective  segmentation  in  the
prediction of risks, especially on segments that are financially underserved and therefore the
co-signers  present  more  frequently  because  of  thin-file.  The  results  emphasize  the
significance of the alternative attributes--namely loan purpose and co-signer presence--in the
construction of inclusive, correct credit models [45]. The lenders will be better able to fine-
tune  their  interest  rates  or  even  decision-making  levels  appropriately  using  these  risk-
segmented information.

VI. Discussion and Analysis

A. Effect of Alternative Data on accuracy of credit score

The adoption of the addition of alternative data in credit scoring has been finding substantial

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

78

changes  in  the  way  traditional  lending  was  done.  Alternative  data  are  non-traditional
indicators in the form of utility payments, rental history, mobile phone usage, e-commerce
activity, and social media behavior [46]. These data points give a further understanding of
how the borrower is behaving, particularly individuals and small businesses which have thin
or  no  credit  files.  Such  a  shift  is  particularly  relevant  to  the  US  small  businesses.  Most
entrepreneurs conduct  their businesses in  cash markets  or where there are no conventional
financial  footprints.  Through  alternative  data,  the  lenders  will  be  able  to  create  a  holistic
profile  of  creditworthiness  that  does  not  live  within  the  constraints  of  FICO  scores  or
historical  loan  defaults.  The  results  of  this  study  indicate  that  small  businesses  that  use
alternative data analytics were provided with better  interest rates and accessibility to loans
especially among the businesses that have never defaulted or those with more positive and
reliable behavior patterns online. This implies that the alternative data will not only promote
scoring  accuracy  but  it  will  democratize  financial  inclusion  [47].  It  minimizes  the
probability  of  false  negatives  of  credit  evaluation-those  who  might  be  creditworthy  are
locked  out  because  of  the  absence  of  a  long  credit  history  in  the  economic  environment.
There is the need to ascertain that the data employed is pertinent, precise, and proportionate
to  a  forecast  of  the  loan  performance.  The  lenders  have  to  justify  the  fit  between  the
alternative  data  variables  that  they  choose  and  repayment  behaviors.  With  a  careful
implementation, alternative data can decrease the risk of defaults, improve portfolio quality,
and widen the scope of lending activities to a wider section of people.

B. Mitigation of Loan Default Risk by Co-signers

The  availability  of  co-signer  has  become  the  decisive  measure  in  ensuring  default
inquisitiveness  will occur among  the small  business  borrowers. As  reflected in  the results,
co-signer  guaranteed  loans  had  a  lesser  average  default  rate  when  comparing  different
purposes  of  loans  [48].  The  trend  underscores  how  co-signers  are  useful  in  boosting  the
credibility  of  the  borrower,  and  thus,  dispels  the  lenders  fears  of  the  likelihood  of  paying
them off. In special industries such as the Home and Auto, which require massive capital,
the co-signers are quite crucial in raising the eligibility and credibility of the borrowers. The
presence of co-signers means two layers of safety nets, that a person is not only a financial
backer  but  a  person  of  social  responsibility.  This  tends  to  make  borrowers  pay  more
responsibly as they are aware that they may spoil the credit status of another person. On the
part  of  the  lender,  the  presence  of  a  co-signer  would  help  in  diversifying  the  risk,  hence
rendering  loan  portfolios  to  be  a  bit  stronger  particularly  in  an  unstable  economic  set  up.
Interestingly,  the  chart  used  in  Figure  8  reveals  that  despite  high-risk  segments  such  as
Business and Education, the average default rating comes down when there is a presence of
a co-signer. This supports the argument that co-signers stabilize in the case of both types of
loans  [49].  The  input  of  the  co-signers  should  be  questioned  under  equity.  Although  they
decrease  the  risk,  excessive  dependence  on  co-signers  can  deprive  the  underprivileged
borrowers  whose  networks  are  underdeveloped.  Co-signers  are  not  only  a  risk  reduction
mechanism; they allow wider participation in financial transactions. The policymakers and
lenders ought to consider rewarding the co-signed loan contracts by putting a lower charge
on it or flexible terms due to the security it offers the lending environment.

C. Effect of Purpose of Loan on the Probability of default

The purpose of the loan has  a strong impact  on  the possibilities of default because not  all
sectors are equal in financial conduct, capital requirements and risk level. Unlike the Auto
loan and Home loan, Business loans are generally characterized by high rates of default, as
shown in Figure 8; they prove unpredictable when considering the co-signer status (Figure
8). Such differences indicate that these types of loans which already have always been used
differently  add  to  the  level  of  risk  within  borrowers  in  different  ways.  Business  lending
loans, especially those of the small and medium scale establishments (SMEs), are those with

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

79

uncertain income generators, market risks, and operational risks. This uncertainty forms the
reason why default rates are high, especially in the situation where borrowers have no ample
financial background or securities. Auto loans are in general less in size, secured by tangible
assets,  and  related  to  critical  mobility  needs-and  thus  are  less  risky  in  terms  of  repayment
behavior. On the same note, Home loans tend to be high amounts and long term, thus people
tend  to  be  more  committed  to  repayments.  It  is  indicated  in  the  findings  that  loans  to
Education  possess  a  moderate  level  of  default  [50].  They  can  show  postponed  repayment
capacity, when the borrowers depend on future time incomes and forecasts over the present
ones.  Miscellaneous  loans  reportedly  had  varied  patterns  and  this  emphasizes  the  need  to
have  better  credit  categorization  and  profiling  in  order  to  strengthen  the  miscellaneous
groups. Lenders will need to pursue dynamic risk-pricing policies on a per-type basis. With
high-risk  products  such  as  business  loans,  it  could  be  possible  to  introduce  more  flexible
repayment  patterns,  financial  literacy  or  part  guarantees  that  help  counter  the  risk  [51].
Conversely,  the  low-risk  loans  may  be  automated  and  AI-based  that  will  help  to  lower
operational costs and can increase access. The purpose of a loan must be a major factor of
credit evaluation whereby not only the interest rates, but the loan approval system and post
loan support frameworks must be affected.

D. Impact of Credit Score and Default History on the Distribution of Interest Rates

Credit  score  and  default  history  has  been  among  the  most  influential  variables  in  how
interest  rate  is  distributed  across  types  of  loans. High  credit  score  borrowers  who  have  no
defaults  in  their  records  generally  receive  lower  interest  rates  and  those  with  a  history  of
default  or  low  scores  find  that  their  interest  rates  are  high  or  worse  still  deny  them  loans
[52]. The findings in Figure 8 affirm this conventional tendency but denote delicate trends
once crossed with the existence of a co-signer and the purpose of a loan. Under the No Co-
signer  category,  high  average  default  rates  are  encountered  by  borrowers  on  all  types  of
loans and consequently increase the interest  rate distribution on a wider fate biased on the
higher  side.  This  implies  that  the  credit  scoring  models  are  stricter  with  unassisted
borrowers. On the other hand, the Yes Co-signer group has a generally better credit rating,
which leads  to  better distribution of rates, which is  even in  the previously  riskier business
lending.  The  variance  of  default  distribution  of  loans  of  various  types  point  out  that
consistent  consumer  credit  facility  borrowers  have  much  easier  interest  rates  to  forecast.
There is larger variance in the case of individuals who may show erratic behavior in terms of
credit, or who have defaulted in the past and thus the risk uncertainty factor must be priced
in by the lender. The possibility of including both AI and machine learning when modeling
credit  risks  has  the  potential  to  reflect  these  differences  better  and  offer  more  reasonable
interest  rates  [53].  Typical  models  impose  too  high  expectations  when  it  comes  to  small
offences whereas one powered by AI has the ability to take into consideration surroundings
information  and  behavior  patterns  which  then  help  in  making  adjustments  to  the
computation of rates. The credit score and history of defaults by a borrower remains to be
quite  effective  indicators  of  the  interest  rate  decision  and  data  analytics  advancements  are
making this as fair and data-driven as possible.

E. Neutral Lending Policies, and the Connection with Default Rates

The  momentum  of  gender  neutral  lending  has  been  driven  by  the  efforts  of  financial
institutions  to  become  accessible  and  non-depredatory.  This  research  did  not  observe  any
significant  changes  in  default  rates  due  to  gender  when  compared  with  other  explanatory
factors such as loan purpose, co-signers and credit history were held constant. It implies that
the  modern  credit  models  start  to  pay  more  attention  to  measurable  financial  behavior
instead of relying on unfounded demographic stereotypes and are inching towards achieving
fair lending. The absence of a bias in the default rates means that there is no discrimination
against male and female borrowers provided that risk-adjusted conditions are laid down. But

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

80

one  should  take  a  wider  scope  into  consideration  [54].  Although  the  default  risk  can  be
considered gender-neutral, the provision of loans, the mean size of loans granted, and rates
of  interest  charged  can  still  represent  the  systemic  inequality.  An  example  is  that  female
entrepreneurs  have  frequently  stated  that  they  have  to  submit  more  paperwork  or  get  a
tougher review during underwriting. The combination of gender and other socio-economic
variables like education, the level of income, and residency status can add to disadvantages.
Such  factors  are  typically  not  directly  included  into  default  statistics  but  can  affect  access
and  terms  in  a  more  subtle  way.  Consequently,  subsequent  models  should  carry  on  with
ensuring that the metric of fairness is incorporated throughout the applications processing to
approval  and  rate-setting  [55].  Credit  judgments  conducted  by  AI  represent  a  chance  to
strengthen gender neutral lending because it pays attention to behavioral, transactional, and
performance  data.  Such  models  need  to  incorporate  bias  detection  algorithms  and  fairness
audits to eliminate discrimination that may not be executed intentionally [56]. Although this
study  shows  that  gender  is  not  directly  proportional  to  the  default  likelihood,  it  is  upon
financial  institutions  to  actively  update  and  improve  gender  equity  throughout  the  lending
process lifecycle in order to maintain long-lasting inclusion and confidence.

F. Predictive loan risk modeling with AI

Predictive  analytics  in  lending  has  been  transformed  by  Artificial  Intelligence  (AI),  which
allows  setting  up  more  granular  and  accurate  judgments  regarding  loan  default  risk.
Analyzing large streams  of data that contain not only  typical  financial indicators but  other
behavioral  signals,  AI  models  can  identify  patterns  and  trends  and  reveal  correlations  that
would otherwise be invisible to the traditional tools [57]. This research paper contributes to
the  relevance  of  AI,  especially  when  it  comes  to  the  scope  of  bias  reduction  and  better
predictive outcomes in the loans assessment of small businesses. Machine learning, as one
of the AI algorithms, can update with changes in the patterns and behaviors of the borrower,
macro economy, and risks characteristic of the industry. In the case study of understanding
the dataset used in this research, AI would be able to know that Business loans on Default
with  no  co-signer  and  low  historical  credit  activity  were  at  the  greatest  risk  and  the  Auto
loans  on  Default  that  had  co-signer  were  most  likely  to  be  at  low  default  rate  [58].  The
insights  can enable the lenders to  better calibrate their approval  rules, assignment of rates,
and efforts to alleviate risk. Risk scores can be updated real-time and dynamically based on
continuously learning new repayment behaviors  as  AI does, making the  credit models and
repayment behavior more responsive to present realities of the borrowers [59]. This is unlike
the stagnant scoring systems that are based on old dated, or narrow data. Furthermore, AI-
based applications aid in the process of customer segmentation, evaluation of risks assessed
on  the  basis  of  clusters,  and  even  suggestions  of  financial  products  that  would  suit  the
profiles of borrowers. Ethics should inform the use of Artificial Intelligence. It is important
to have transparency, explain ability of models, and prevention of discriminatory outcomes.
Regulators  pay  more  attention  to  the  need  to  make  sure  that  AI  in  lending  is  consolidated
with fairness and accountability principles [60]. AI would have an effective tool to increase
credit  scoring  accuracy,  financial  access,  and  to  mitigate  systemic  risk  thus  making  it  the
foundation of modern and evidential lending practices.

VII. Future Work

With  financial  institutions  turning  toward  data-based  methods  to  address  both  credit  risk
management  and  lending  strategy  optimization,  the  present  work  leaves  open  a  range  of
avenues  to  explore  in  the  future  [61].  Although  this  work  forms  important  basis  on  the
influence  of  the  credit  scores  and  default  probabilities  on  the  distribution  of  interest  rates
across different loan purposes and to different types of borrowers including co-signers, the
future work will add to this work by addition of a greater level of variables, a higher level of
predictive  models,  and  real-time  integration  of  data.  A  potentially  beneficial  avenue  is  the

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

81

use  of  machine  learning  algorithms  that  will  help  credit  score  and  optimize  interest  rates
[62]. Random forests, gradient boosting, and neural networks might be used to improve the
accuracy of default prediction relative to the conventional regression analysis. Such models
are  able  to  reproduce  non-  linear  association  between  profiles  of  borrowers  and  the
likelihood of defaulting which can provide a more tailored rate of interest and can enhance
financial inclusion. The other area that can be explored in future is the inclusion of temporal
and behavioral data. Through the analysis of longitudinal data able to trace the modification
of  the  borrower  behavior  throughout  time  such  as  changes  in  payments,  alterations  in
income, in the future, it is possible to consider the dynamic character of creditworthiness and
its  influence  on  interest  rate  structure.  This  would  enable  lenders  to  change  their  credit
models  in  near  real-time.  To  discuss  how  the  character  of  lending  activity  may  vary
regionally or in age, geographical and demographical divisions may be added. Segmentation
of this nature would give banks and policymakers more depth in terms of actual context so
that  lending  policies  could  be  equitable  across  all  populations.  Research  can  further  be
applied  in  policies  as  an  extension,  like  the  impact  of  co-signer  policies  and  financial
regulations  on  risk-sharing  and  default  probabilities  [63].  Incorporation  of  regulatory
changes or macro-economic indicators such as inflation or unemployment rates may produce
more  generous  risk  measurement.  Finally,  live  dashboards  and  visualization  tools  can  be
considered to make decision-making quick and convenient among financial analysts and the
borrowers.  Devices,  fueled  by  Tableau  or  Power  BI,  might  simplify  the  language  of  a
complicated  risk  policy  and  allow  to  create  an  understandable,  transparent,  and  trusted
interpretation of the lending process. Advanced financial models of risk are more inclusive,
dynamic,  and  technologically  advanced  than  before  and  are  based  on  the  findings  of  this
research [64]. Further building on such findings by enhancing multidisciplinary approaches
and  new  developments  in  technology  will  enhance  the  credit  scoring  models  and  provide
responsible, fair lending practices in the growing digital economy.

VIII. Conclusion

This  study  has  examined  the  complexities  of  the  relationships  involving  credit  scores,
default  rates,  distributions  of  interest  rates,  and  related  borrower  qualities  on  a  wealthy
lending  dataset.  With  the  thorough  approaches  to  data  analysis  and  visualization  using
Python, Excel, and Tableau, the study revealed meaningful tendencies that may have various
cost-effective implications to the credit risk analysis and financial decision-making of loans-
related practice. The key findings indicate that interest rates largely depend on credit scores,
where  the  individuals  with  higher  marks  are  always  offered  better  quotations.  Borrowers
who  had  a  co-signer  had  fewer  defaults  indicating  that  lenders  felt  safer  with  the  extra
sources of capital of the debtor. The analysis indicated that the impact of annual income and
amount  of  loan  on  interest  rates  and  the  remaining  possibility  to  default  with  loan  is
significant,  which  underlines  the  necessity  of  broad-based  risk  assessment.  This  study
revealed  the  significance  of  data-based  credit  scoring  with  the  example  of  using  a
combination  of  different  characteristics  of  borrowers  to  achieve  improved  risk  forecasting
and a more justifying lending policy in terms of providing lenders. The visualizations gave a
straightforward  and  easily  comprehended  explanation  to  these  complicated  financial  ties,
which  raised  the  prospect  of  direct  application  in  the  workplace  lending  settings.
Notwithstanding  its  merits,  the  study  had  its  limitations  such  as  employing  historical,
stagnant  data,  and  lack  of  macroeconomic  variables  i.e.  unemployment  rates  or  inflation,
which  might  affect  the  behavior  of  borrowers.  The  emerging  knowledge  will  serve  as  an
excellent basis of future study and development of credit analytics. The importance of credit
scores and related variables in determining the outcome of loans highlighted in this region
will aid both academic and industry stakeholders in understanding how data can be used to
make more transparent and fairer lending practices. Financial technology is developing, and

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

82

as such, incorporation of such machine learning models with a powerful data source such as
this  can  be  used  to  improve  predictive  accuracy  and  accordingly  facilitate  inclusive  credit
systems.

IX. References:

1.  Lomas,  R.  (2024,  December).  AI-Driven  FinTech  Solutions  for  Financial  Inclusion:  A
Study  on  MSME  Sector  Empowerment.  In  2024  1st  International  Conference  on
Advances  in  Computing,  Communication and Networking (ICAC2N) (pp. 1887-1891).
IEEE.

2.  Jang, G. Y., Kang, H. G., Park, J., & Choi, H. S. (2023). AI-Driven Credit Scoring and
Market  Transformation:  How  ACSS  Reshapes  SME  Financing,  Firm  Strategy,  and
Regulatory Boundaries. In Posted on Google Scholar by the AI and Finance Conference
after the presentation with the previous title," Unveiling the Imoact of Alternative Credit
Scoring Systems on Small and Medium-sized Enterprises.

3.  Bello,  O.  A.  (2024).  The  role  of  data  analytics  in  enhancing  financial  inclusion  in
emerging  economies.  International  Journal  of  Developing  and  Emerging  Economies,
11(3), 90-112.

4.  Nguyen, E. (2024). The Role of Big Data and AI in Real-Time Credit Scoring.

5.  Mhlanga, D. (2023). FinTech and Artificial Intelligence in addressing poverty,  towards
sustainable  development.  In  FinTech  and  artificial
intelligence  for  sustainable
development:  The  role  of  smart  technologies  in  achieving  development  goals  (pp.  89-
117). Cham: Springer Nature Switzerland.

6.  Nuka,  T.  F.,  &  Ogunola,  A.  A.  (2024).  AI  and  machine  learning  as  tools  for  financial
inclusion: challenges and opportunities in credit scoring. International Journal of Science
and Research Archive, 13(2), 1052-1067.

7.  Adewale, G. T., Umavezi, J. U., & Olukoya, O. (2022). Innovations in Lending-Focused

FinTech: Leveraging AI to Transform Credit Accessibility and Risk Assessment.

8.  Ajuwon,  A.,  Oladuji,  T.  J.,  Akintobi,  A.  O.,  &  Onifade,  O.  (2024).  A  Model  for
Financial Automation in Developing Economies: Integrating AI with Payment Systems
and Credit Scoring Tools.

9.  Okunola,  A.,  &  Ahsun,  A.  (2022).  Leveraging  Big  Data  Analytics  and  AI  for
in  Underserved

Personalized  Financial  Product  Design  and  Risk  Assessment
Populations.

10. Adewuyi,  A.,  Ajuwon,  A.,  Oladuji,  T.  J.,  &  Akintobi,  A.  O.  (2023).  Advances  in
Financial Inclusion Models: Expanding Access to Credit through AI and Data Analytics.
International  Journal  of  Advanced  Multidisciplinary  Research  and  Studies,  3(6),  1827-
1842.

11. Omokhoa,  H.  E.,  Odionu,  C.  S.,  Azubuike,  C.  H.  I.  M.  A.,  &  Sule,  A.  K.  (2024).
Leveraging  AI  and  technology  to  optimize  financial  management  and  operations  in
microfinance institutions and SMEs. IRE Journals, 8(6), 676.

12. Shittu,  A.  K.  (2022).  Advances  in  AI-driven  credit  risk  models  for  financial  services
International  Journal  of  Multidisciplinary  Research  and  Growth

optimization.
Evaluation, 3(1), 660-676.

13. Omogbeme, A. O., Phil-Ugochukwu, A. I., Nwabufo, I. J., & Onyebuchi, J. (2024). The
role of artificial intelligence in enhancing financial inclusion: A review of its impact on
financial  services  for  the  unbanked  population  in  the  United  States.  World  Journal  of

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

83

Advanced Research and Reviews, 23(2), 2184-2192.

14. Avevor,  M.,  Attionu,  G.  T.,  Osahor,  D.,  Azonuche,  T.,  &  Tawo,  O.  (2023).  Beyond
funding:  rethinking  small  business  administration  strategies  and  public-private
partnerships for minority-owned business resilience (AI, FinTech, and Policy Synergy).

15. Hamzat,  L.  (2023).  Real-Time  Financial  Resilience  and  Debt  Optimization  for
Entrepreneurs:  Tackling  Debt  Management  as  a  Financial  Health  Pandemic  and
Empowering Small Business Growth Through Early Detection of Financial Distress and
Effortless Capital Management.

16. Balaji,  K.  (2024).  Harnessing  AI  for  financial  innovations:  Pioneering  the  future  of
financial services. In Modern Management Science Practices in the Age of AI (pp. 91-
122). IGI Global.

17. Xiong,  H.,  Carton,  F.,  &  McCarthy,  J.  B.  (2024,  October).  AI-Powered  Financial
Services:  A  Value  Co-creation  Model.  In  International  Workshop  on  Enterprise
Applications, Markets and Services in the Finance Industry (pp. 18-31). Cham: Springer
Nature Switzerland.

18. Taneja,  B.  (2024).  Financial  Innovations  in  FinTech:  Unleashing  the  Power  of
in  Firm  Financing  and  Investment  Strategies.  In
for  Promoting  Financial  Literacy  and

Embedded  Finance  and  AI
Contemporary  Research  and  Practices
Sustainability (pp. 208-232). IGI Global.

19. Adhikari, P., Hamal, P., & Jnr, F. B. (2024). The role of fintech in US entrepreneurship:
How AI is shaping the future of financial services. International Journal of Science and
Research Archive, 13(02), 1673-1693.

20. How, M. L., Cheah, S. M., Chan, Y. J., Khor, A. C., & Say, E. M. P. (2023). Artificial
Intelligence  for  Advancing  Sustainable  Development  Goals  (SDGs):  An  Inclusive
Democratized  Low-Code  Approach.  In  The  Ethics  of  Artificial  Intelligence  for  the
Sustainable Development Goals (pp. 145-165). Cham: Springer International Publishing.

21. Kowsar, M. M., & Mohna, H. A. (2023). American Journal of Interdisciplinary Studies.

22. Piao, J., Wang, K. P., & Weng, D. (2024). US Banks' Artificial Intelligence and Small
Business Lending: Evidence from the Census Bureau's Technology Survey. Available at
SSRN 5016585.

23. Heidari, A. (2023). The Role of Artificial Intelligence in Modern Finance. Available at

SSRN 5127689.

24. Challoumis, C. (2024). Ai’s role in the cycle of money. In XIX International Scientific

Conference. London. Great Britain (pp. 1003-1035).

25. Aria,  J.,  Diego,  C.,  Jose,  D.,  &  Ok,  E.  (2024).  Machine  Learning  in  Credit  Risk

Management: Evaluating the Role of AI and Blockchain.

26. Chukwuma-Eke, E. C., Attipoe, V., Lawal, C. I., Friday, S. C., Isibor, N. J., & Akintobi,
A.  O.  (2024).  Promoting  financial  inclusion  through  energy  financing  for  underserved
communities:  A  sustainable  business  model.  International  Journal  of  Multidisciplinary
Research and Growth Evaluation, 5(1), 1699-1707.

27. Nwachukwu,  G.  (2024).  Enhancing  credit  risk  management  through  revalidation  and
accuracy  in  financial  data:  The  impact  of  credit  history  assessment  on  procedural
financing. International Journal of Research Publication and Reviews, 5(11), 631-644.

28. Alonge, E. O., Eyo-Udo, N. L., Ubanadu, B. C., Daraojimba, A.  I., Balogun, E. D., &
Ogunsola, K. O. (2024). Developing an Advanced Machine Learning Decision-Making

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

84

Model  for  Banking:  Balancing  Risk,  Speed,  and  Precision  in  Credit  Assessments.
Journal details pending.

29. Singhania,  D.,  Tanty,  G.,  &  Srivastava,  A.  (2024).  Empowering  Rural  Jharkhand:
Adoption  of  Artificial  Intelligence  for  Digital  Financial  Inclusion.  In  Blockchain’s
Transformative Potential of Financial Technology for Sustainable Futures (pp. 123-134).
Cham: Springer Nature Switzerland.

30. Olanrewaju,  A. G.,  Inegbedion,  E., Olukotun,  I.  F., &  Atimango, K.  (2024). AI-driven
healthcare  financial  models:  Ethical  frameworks  for  balancing  profit  and  access  in
precision medicine in the US.

31. Ziemba,  E.  W.,  Duong,  C.  D.,  Ejdys,  J.,  Gonzalez-Perez,  M.  A.,  Kazlauskaitė,  R.,
Korzynski,  P.,  ...  &  Wach,  K.  (2024).  Leveraging  artificial  intelligence  to  meet  the
sustainable development goals. Journal of Economics and Management, 46, 508-583.

32. Adenekan,  T.  K.  (2022).  The  Digital  Path  to  Financial  Inclusion:  Data  Engineering

Strategies for Equitable Banking.

33. Ojonugwa,  B.  M.,  Adanigbo,  O.  S.,  Ogunwale,  B.,  &  Ochefu,  A.  (2024).  Impact
Investing  and  AI:  Advancing  Developmental  Goals  through  Data-Driven  Investment
Strategies.

34. Kouam, A. W. F. (2024). The Impact of Artificial Intelligence on Fintech Innovation and

Financial Inclusion: A Global Perspective.

35. Paleti, S. (2023). Transforming Money Transfers and Financial Inclusion: The Impact of
AI-Powered  Risk  Mitigation  and  Deep  Learning-Based  Fraud  Prevention  in  Cross-
Border Transactions. Available at SSRN 5158588.

36. Yu,  P.,  Wong,  S.  K.,  &  Prabhakar,  A.  C.  (Eds.).  (2024).  AI  Strategies  for  Social

Entrepreneurship and Sustainable Economic Development. IGI Global.

37. Liu, Y., Li, X., & Zheng, Z. (2024). Smart natural disaster relief: Assisting victims with

artificial intelligence in lending. Information Systems Research, 35(2), 489-504.

38. Mbuguah, S. M., & Gichuki, D. K. (2024, November). Leveraging Emerging Trends for
Technological  Advancement  in  Africa.  In  2024  4th  International  Multidisciplinary
Information Technology and Engineering Conference (IMITEC) (pp. 1-11). IEEE.

39. Ok, E., Aria, J., Jose, D., & Diego, C. (2024). Transforming Credit Risk Mitigation: The

Role of AI, Blockchain, and Predictive Analytics.

40. Adewale, T. T., Olorunyomi, T. D., & Odonkor, T. N. (2023). Big data-driven financial
analysis:  A  new  paradigm  for  strategic  insights  and  decision-making.  Journal  of
Financial Innovation and Analytics, 1(1), 1-15.

41. Shah,  S.  (2024).  Financial  inclusion  and  digital  banking:  Current  trends  and  future

directions. Premier Journal of Business and Management, 1.

42. Palakurti, N. R. (2024). The Intersection of Information Technology, Financial Services,
and  Risk  Management,  Including  AI  And  Ml  Innovations.  International  Journal  of
Computer Engineering And Technology (IJCET), 15(4).

43. Zoey,  A.,  Aria,  D.,  Oscar,  A.,  Marek,  M.,  Julia,  Z.,  Cora,  L.,  &  Ok,  E.  (2024).
Blockchain  and  AI  in  Financial  Risk  Management:  A  Machine  Learning  Approach  to
Credit Risk Mitigation. Journal of Financial Technology, 15(4), 201-214.

44. Chadha,  P.,  Gera,  R.,  Khera,  G.  S.,  &  Sharma,  M.  (2023).  Challenges  of  Artificial
Intelligence  Adoption  for  Financial  Inclusion.  In  Artificial  Intelligence,  Fintech,  and

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

85

Financial Inclusion (pp. 135-160). CRC Press.

45. Gera, R., Chadha, P., Saxena, A., & Dixit, S. (2023). A scientometric and bibliometric
review  of  impacts  and  application  of  artificial  intelligence  and  fintech  for  financial
inclusion. In Artificial Intelligence, Fintech, and Financial Inclusion (pp. 82-111). CRC
Press.

46. Attah,  R.  U.,  Garba,  B.  M.  P.,  Gil-Ozoudeh,  I.,  &  Iwuanyanwu,  O.  (2024).  Corporate
banking  strategies  and  financial  services  innovation:  Conceptual  analysis  for  driving
corporate growth and market expansion. Int J Eng Res Dev, 20(11), 1339-49.

47. Sanyaolu,  T.  O.,  Adeleke,  A.  G.,  Efunniyi,  C.  P.,  Akwawa,  L.  A.,  &  Azubuko,  C.  F.
(2024).  The  role  of  business  analysts  in  driving  financial  inclusion  through  product
innovation. Finance & Accounting Research Journal P-ISSN, 1555-1581.

48. Xiong, H., Carton, F., & McCarthy, J. B. (2022). Data Science for Financial Inclusion: a

value co-creation model for balanced benefits.

49. El Hajj, M., & Hammoud, J. (2023). Unveiling the influence of artificial intelligence and
machine learning on financial markets: A comprehensive analysis of AI applications in
trading,  risk  management,  and  financial  operations.  Journal  of  Risk  and  Financial
Management, 16(10), 434.

50. Abu Jamie, N. H., Abu-Jamie, T. N., & Al-Absy, M. S. M. (2024). Advances in AI and
Their Effects on Finance and Economic Analysis. The AI Revolution: Driving Business
Innovation and Research: Volume 1, 507-523.

51. Channe, P. S. (2024). The  Impact  of AI on Economic Forecasting and Policy-Making:
Opportunities  and  Challenges  for  Future  Economic  Stability  and  Growth.  York
University.

52. Rajenthran,  G.  (2024).  Financial  Frontiers:  How  Generative  AI  Is  Shaping  the  Fintech
Industry. In Generative AI for Transformational Management (pp. 161-192). IGI Global.

53. Owoade, S. J., Uzoka, A., Akerele, J. I., & Ojukwu, P. U. (2024). Enhancing financial
portfolio management with predictive analytics and scalable data modeling techniques.
International Journal of Applied Research in Social Sciences, 6(11), 2678-2690.

54. Omopariola,  B.  J.  (2023).  Decentralized  energy  investment:  Leveraging  public-private
partnerships  and  digital  financial  instruments  to  overcome  grid  instability  in  the  US.
World Journal of Advanced Research and Reviews, 20(03), 2178-2196.

55. Maleh,  Y.,  Zhang,  J.,  &  Hansali,  A.  (Eds.).  (2024).  Advances  in  emerging  financial

technology and digital money. CRC Press.

56. Meera, K. L., & Seshanna, S. (2023). AI and Machine Learning as Drivers of Change in

the Financial Industry. Journal of Financial Innovation, 51(3), 190-215.

57. Lim, T. (2024). Environmental, social, and governance (ESG) and artificial intelligence
in finance: State-of-the-art and research takeaways. Artificial Intelligence Review, 57(4),
76.

58. Subramaniam,  Y.,  Loganathan,  N.,  Khan,  F.  N.  H.  T.,  &  Subramaniam,  T.  (2024).
Exploring  the  Impact  of  Artificial  Intelligence  on  Financial  Inclusion:  Cross-Country
Analysis. Social Indicators Research, 1-18.

59. Fiorillo, L., & Mehta, V. (2024). Accelerating editorial processes in scientific journals:

Leveraging AI for rapid manuscript review. Oral Oncology Reports, 10, 100511.

60. Tyagi, A. K. (2024). Modern Banking and. Convergence of Technology and Operations

Vol 2|No 10 (2025):  International Journal of Informatics and Data Science Research

86

Management in Modern Businesses, 141.

61. Sehgal,  M.  I.  (2023).  Digital  Finance  Strategies  and  Their  Role  in  Transforming
Financial  Management.  Digital  Transform  Management:  Em  Technologic  Innovations
for Orga, 57.

62. Mousa,  S.  (2024).  Unleashing  the  Potential  of  Industry  4.0  for  Financial  Inclusion.  In
Financial  Inclusion,  Sustainability,  and  the  Influence  of  Religion  and  Technology  (pp.
253-285). IGI Global Scientific Publishing.

63. Bhavana, K. V., Koduri, H., Ariwa, E., & Vishwa, K. D. (2023). Artificial intelligence
and Fintech industry—The metaverse adoption. The business of the metaverse, 199-215.

64. Packin,  N.  G.,  &  Lev‐Aretz,  Y.  (2024).  Decentralized  credit  scoring:  Black  box  3.0.

American Business Law Journal, 61(2), 91-111.

65. Datasheet Link:https://www.kaggle.com/datasets/nikhil1e9/loan-default

