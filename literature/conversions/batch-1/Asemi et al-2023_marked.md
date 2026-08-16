---
conversion_metadata:
  converted_at: "2026-07-22T12:01:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Asemi et al-2023.pdf"
  source_pdf_sha256: "98e424cb9847499cdc458e670c5664289956079598983a093fcabd2595024c9a"
  page_count: 27
  markdown_char_count: 134632
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Asemi et al. Journal of Big Data           (2023) 10:87  
https://doi.org/10.1186/s40537-023-00784-7

Journal of Big Data

RESEARCH

Open Access

Adaptive neuro-fuzzy inference system 
for customizing investment type based 
on the potential investors’ demographics 
and feedback

Asefeh Asemi1, Adeleh Asemi2 and Andrea Ko3*

*Correspondence:   
andrea.ko@uni-corvinus.hu

1 Doctoral School of Economics, 
Business, and Informatics, 
Institute of Data Analytics 
and Information Systems, 
Corvinus University of Budapest, 
Budapest, Hungary
2 Department of Software 
Engineering, Faculty 
of Computer Science 
and Information Technology, 
Universiti Malaya, Kuala Lumpur, 
Malaysia
3 Corvinus University 
of Budapest, Budapest, Hungary

Abstract 
The proposed model is an adaptive neuro-fuzzy inference recommender system that 
utilizes customer investment service feedback and fuzzy neural inference solutions 
to generate personalized investment recommendations. The model is designed to 
support the investment process for the customers and takes into consideration seven 
factors to implement the proposed investment system model through the customer or 
potential investor data set. These include demographic data and investment type. The 
model is divided into three main phases: data gathering, data analysis, and decision-
making. In the data gathering phase, initial data is collected through a web-based 
platform, and in the data analysis phase, the potential investors’ demographic crite-
ria are extracted and grouped, and the types of investments are then clustered. The 
output obtained is transferred to the ANFIS layer, and investment-type recommenda-
tions are extracted for each group of potential investors. Investor feedback is received 
to improve and develop the system. JMP and MATLAB are used to propose the model, 
which serves as a framework for investment recommender systems. It demonstrates 
how to use this framework to offer pertinent and precise recommendations for the 
best sort of investment type to potential and present investors by combining the 
expertise of the experts and the demographic information of potential investors. 
Overall, this paper provides a new, novel model for investment recommender systems, 
which can assist investment companies, individual investors, and fund managers in 
their investment decisions.

Keywords:  “Adaptive Neuro-Fuzzy Inference System”, “ANFIS”, “Recommender System”, 
“Demographic Data”, “Investment Type”, “Investment Product”, “Potential Investors”, 
“Investor Feedback”, “Investment Service”

Introduction

One  of  the  most  important  sources  for  understanding  a  company’s  past,  present,  and 
future  is  customer  demographic  data  and  statistics. These  facts  and  figures  are  crucial 
in  recommender  systems  as  they  help  the  user  receive  personalized  and  relevant  rec-
ommendations.  This  is  particularly  important  as  Kanaujia  and  his  colleagues  have

© The Author(s) 2023. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits 
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original 
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third 
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate-
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// 
creat iveco mmons. org/ licen ses/ by/4. 0/.

---

<!-- PAGE 2 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 2 of 27

highlighted that recommender systems should be tailored to meet the specific needs of 
clients  [17].  In  order  to  address  this  issue,  this  study  proposes  a  novel  business  model 
for  an  investment  recommender  system  that  utilizes  adaptive  neural  fuzzy  inference 
(ANFIS) to suggest the appropriate type of investment based on the demographic data 
collected from potential investors. This data is categorized and analyzed using machine 
learning  techniques,  serving  as  the  system  input,  and  the  system  output  is  the  recom-
mended type of investment for the individual investor.

Theoretical framework

This research includes several concepts. These ideas encompass investor and potential 
investor,  demographics  of  potential  investors,  investment,  recommender  systems  for 
investments, and machine learning. The customer and the investor in this study are the 
same. The following list summarizes the theoretical underpinnings:

Investor and potential investors

An investor is typically someone who invests money to gain a profit or an edge in some-
thing  (Cambridge  Dictionary).  Anyone  who  purchases  services  or  investment  goods 
from an investment company qualifies as an investor on their behalf. The investor could 
be a legitimate source or a real individual. From the perspective of a business, a poten-
tial investor is someone or something that is in talks with the business about funding. 
Potential investors in this study are different people who respond to “Investment Ques-
tionnaire”  questions.  These  persons  may  not  all  be  active  investors.  A  community  or 
organization’s members can generally be thought of as potential investors. In this case, 
a  person  rather  than  an  organization  is  the  potential  investor,  and  the  current  study 
is  based  on  data  from  respondents  to  the  “Investment  Questionnaire”  regarding  their 
demographics. Typically, when making an investment decision, an investor seeks advice. 
Professional  investors  attempt  to  speak  with  subject-matter  specialists  in  addition  to 
gathering the information they need before making an investment. It goes without say-
ing that a person’s demographic and behavioral traits will influence how they learn about 
investments and consult with others. People who influence an investor’s decisions fre-
quently have a variety of professional interests. Potential investors have various invest-
ment  requirements  depending  on  their  demographics.  As  a  result,  they  select  various 
forms  of  investments.  For  instance,  the  most  crucial  criteria  in  selecting  the  sort  of 
investment may be income, savings, and employment.

Potential investors’ demographic

Demography,  as  defined  by  Merriam-Webster  [21],  is  “the  statistical  study  of  human 
populations, particularly with regard to size and density, distribution, and vital statistics” 
in sociology. In the context of customer demographics, this refers to certain statistical 
information  about  individuals,  such  as  their  identity  information,  gender,  age,  marital 
status, and education level. This data can also include spatial information, such as mail-
ing addresses. According to Onsgard [22], other relevant consumer demographic infor-
mation  includes  buyer  types,  purchase  objectives,  and  information  about  the  buyer’s 
lifestyle. When making decisions to improve the service or product offered by an invest-
ment company, it is crucial to consider the demographic profile of potential investors.

---

<!-- PAGE 3 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 3 of 27

Factors such as age, gender, occupation, educational attainment, field of study, domicile, 
place  of  employment,  and  other  pertinent  personal  data  can  provide  valuable  insight 
into how investors and potential investors use and evaluate the company’s services and 
products. This understanding can also help predict the behavior of current and potential 
customers. Intelligent recommender systems can be an effective tool in this prediction 
and  direction.  These  systems  can  establish  membership  functions  for  investment-type 
memberships and membership functions related to customer demographics. Addition-
ally, the expertise of experts can be utilized to add additional rules based on their knowl-
edge, resulting in more personalized recommendations tailored to the needs of the user. 
Overall, considering customer demographics is an important aspect of decision-making 
for  investment  companies,  as  it  can  provide  valuable  insights  into  how  customers  use 
and evaluate the company’s services and products.

Investment

To  invest  is  to  set  aside  money  with  the  hope  of  gaining  something  later.  According 
to  finance  2020,  the  advantage  of  investment  is  referred  to  as  a  return  on  investment 
(“Investment”). All stocks, bonds, options, derivatives, and other financial instruments 
that investors invest money in with the aim of making a profit are collectively referred to 
as “investment products” [9]. The process of modifying assets over the short, medium, or 
long term might be included in an investment. For example, the effectiveness of this pro-
cedure may be determined by sales, revenue from dividends, income from apartments, 
etc.,  or  a  mix  of  other  approaches.  The  return  could  potentially  include  gains  from 
foreign  investments  or  losses  because  of  changes  in  foreign  exchange  rates.  Typically, 
investors want higher returns on riskier bets. A low-risk investment often yields a low 
return as well. Like excessive risk, excessive returns are also present. Any financial coun-
seling, investment management, or other related activities are referred to as "investment 
services.” The FCA Handbook states that any service relating to a financial instrument 
may be provided, such as receiving and transmitting orders about one or more financial 
instruments, carrying out orders for clients, engaging in trading for one’s own account, 
managing a portfolio, issuing personal recommendations, underwriting financial instru-
ments and/or placing them on a firm commitment basis, placing financial instruments 
without a firm commitment basis, etc. The investment products included in this study’s 
investment types were listed stock mutual funds, voluntary pension funds, government 
securities, and bonds, as well as other financial products.

Investment recommender systems

According  to  Burke  [7],  recommender  systems  are  software  tools  that  employ  various 
methods  to  offer  advice  to  users  based  on  their  interests.  As  stated  by  Resnick  et  al. 
[28] and Resnick & Varian [29], these recommendations are highly relevant to a specific 
user’s interests. Liang [20] also notes that recommender systems play the role of decision 
support, making recommendations based on the outcomes of examining user behavior. 
Asemi  and  Ko  [4]  note  that  customers  may  receive  specific  offers  from  recommender 
systems based on their needs. This is why it is important to not treat users as a separate 
class  when  integrating  recommender  systems  into  information  systems.  In  investment 
recommender systems, both the investor and the investment service or product must be

---

<!-- PAGE 4 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 4 of 27

considered.  By  identifying  advanced  communication  patterns  between  the  two  parties 
and enhancing the system, the degree to which the system’s recommendations match the 
customer’s needs is successfully increased. According to the proposals made, these kinds 
of technologies ought to be able to boost the company’s profitability. It is even possible 
to  build  a  comparison  capability  for  the  system  to  compare  the  feedback  given  in  the 
context of the system’s ideas regarding the types of suggested investments based on cus-
tomer input to predict. This may be determined by investor or client needs.

Machine learning

One of the subfields of artificial intelligence is machine learning, where the performance 
and capability of the system are improved depending on previous results [12]. Machine 
learning  aims  to  provide  computers  with  the  ability  to  learn  on  their  own  by  utilizing 
available  data  and  generating  precise  predictions  [1].  The  primary  benefit  of  machine 
learning  is  its  capacity  for  learning  from  data,  which  is  absent  from  many  traditional 
databases  [37].  Artificial  intelligence,  natural  language  processing,  data  mining,  math-
ematics,  statistics,  computer  science,  and  deep  learning  are  the  primary  fields  associ-
ated  with  machine  learning  (Sarkar,  Bali  &  Sharma,  [30]).  There  are  various  machine 
learning tasks, such as feature engineering for dimensionality reduction, association rule 
learning,  data  clustering,  regression  analysis,  classification  analysis,  and  deep  learning 
techniques [31]. Supervised learning, unsupervised learning, semi-supervised learning, 
and reinforcement learning are the four categories of machine learning based on their 
intended use [6, 31]. In this study, unsupervised learning was employed. The challenge 
in  unsupervised  learning  is  to  uncover  a  hidden  structure  in  a  collection  of  unlabeled 
data (Agrawal et al., 2005). In this type of learning, the only information present is the 
data itself, which is used to group similar concepts together. Unlabeled data is used in 
the  system’s  learning  process,  and  each  category’s  notions  are  distinct  from  those  of 
other  categories.  One  unsupervised  machine  learning  technique  is  clustering,  where 
categories  are  not  predetermined  and  it  is  also  unclear  which  category  is  categorized 
in  accordance  with  which  feature.  Numerous  clustering  techniques  exist,  such  as  the 
k-means clustering method and hierarchical clustering (Han, Kamber & Pei, [13]). A set 
of  data  is  clustered  into  groups  that  share  the  greatest  characteristics.  Clustering  is  a 
frequent descriptive technique for locating homogeneous groupings of objects based on 
their characteristics. Groups may overlap or be isolated. Data without tags are analyzed 
via clustering, which divides them into groups based on the maximization of similarity 
within groups and the minimization of similarity between groups (Agrawal et al., 2005).

Literature review

The  research  of  this  study  builds  upon  the  foundation  of  previous  studies  that  have 
explored  the  use  of  recommender  systems  in  the  field  of  investment.  Several  studies 
have been conducted in this area. Paranjape-Voditel and Umesh [23] proposed a stock 
market  portfolio  recommender  system  based  on  association  rules  that  analyzes  inven-
tory records and makes stock portfolio recommendations. Kanaujia et al. [17] proposed 
using Apache Hadoop and Apache Mahout as a common filtering-based recommenda-
tion  device  for  financial  analysis  based  on  savings,  costs,  and  investments.  Hernández 
et al. [14] evaluated the state of financial technology and proposed a social computing

---

<!-- PAGE 5 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 5 of 27

platform  built  on  virtual  organizations  that  enable  users  to  gain  more  experience  in 
movements  related  to  the  financing  of  recommendations.  Tejeda-Lorente  et  al.  [35] 
proposed a recommender system that considers various factors, such as current yields, 
historical performance, and industry-wide diversity while being aware of the risks con-
nected with hedge funds. Faridniya and Faridniya (2019) used data envelopment analysis 
to  present  a  model  for  resource  allocation  and  investment  type  selection,  focusing  on 
the Social Security Organization (SSO) in Iran as a case study. Tarnowska et al. [34] cre-
ated a recommender system to increase customer loyalty, which considers various issues 
such as assisting managers in recognizing strategic moves in their choices. Sulistiyo and 
Mahpudin  [33]  looked  at  how  demographics  affected  the  type  of  investments  people 
made, using amateur golfers in Karawang City as a sample. Casuat et al. [8] developed an 
expert-based system for improving students’ employability using fuzzy logic techniques. 
The  proposed  system  uses  the  concept  of  fuzzy  membership  degree,  and  it  considers 
both qualitative and quantitative data while making recommendations. Patro et al. [25] 
presented  a  knowledge-based  preference  learning  model  for  a  recommender  system 
using an adaptive neuro-fuzzy inference system. The paper presents a new approach to 
recommending products to customers by utilizing their preferences and past purchases. 
Kovacs, Ko, and Asemi [4] explored the investment patterns of potential retail banking 
customers using a two-stage cluster analysis to determine the best method for identify-
ing the customer groups that are most likely to use a bank. Asemi and Ko [4] presented 
a  novel  combined  business  recommender  system  model  using  customer  investment 
service  feedback.  The  main  objective  of  this  type  of  system  is  to  provide  information 
about the products or services that are like those purchased by customers so they can 
make  an  informed  decision.  Sharma  et  al.  [32]  aimed  to  build  a  recommender  system 
for  the  cold  start  in  social  media,  which  means  when  the  user  has  not  made  any  pre-
vious  purchase  yet.  They  focused  on  building  a  demographic  profile-building  tool  to 
identify potential customers. Yassine et al. [36] focused on the intelligent recommender 
system using unsupervised machine learning techniques and demographic attributes of 
users as input data. Paryudi et al. [24] discussed the performance of a personality-based 
recommender system for fashion with demographic data-based personality prediction. 
The study evaluated the effectiveness of this technique in predicting fashion preferences 
based  on  personality  traits.  Fuzzy  logic,  a  new  and  advanced  method  of  reasoning,  is 
used in this study to solve the problem of incompleteness in classical logic. It has been 
applied  to  many  fields  such  as  engineering,  management,  economics,  etc.  There  has 
been  a  significant  amount  of  research  conducted  in  the  field  of  recommender  systems 
for  investments.  However,  many  of  these  studies  focus  on  specific  areas  such  as  stock 
market  portfolios,  hedge  funds,  or  resource  allocation.  It  is  clear  from  the  aforemen-
tioned studies that there is a significant amount of research that has been conducted on 
the  topic  of  recommender  systems  and  expert-based  systems.  However,  none  of  these 
studies have specifically focused on developing a recommender system for the type or 
product of investment based on the demographics of potential investors using ANFIS. 
The new model introduced in this study aims to address this gap in the literature. This 
ANFIS-based investment recommender system evaluates the potential investor’s demo-
graphic information and, using a combination of professional judgments, suggests which 
investment type is best for each customer demographic. This study generates rules using

---

<!-- PAGE 6 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 6 of 27

an intelligent fuzzy framework, and based on the advice of experts, membership func-
tions  can  also  be  improved  during  the  rule-generation  process.  Therefore,  it  fills  the 
gap in the literature that few studies have used the ANFIS technique and demographic 
information  to  recommend  the  investment  types.  Overall,  this  study  makes  a  valuable 
contribution to the field by providing a new and innovative approach to the problem of 
investment recommendations.

Methods

In  this  study,  both  quantitative  and  qualitative  methods  were  employed  to  present  a 
new model for an investment recommender system. The model fuses previously learned 
information  with  fresh  concepts  and  utilizes  fuzzy  inference  logic  and  machine  learn-
ing  techniques  to  implement  its  methods.  One  specific  technique  used  is  clustering, 
where a portion of the data was clustered using the JMP clustering toolbox to categorize 
prospective  investors’  preferred  investment  types  and  products. The  simplest  machine 
learning algorithm without supervision, K-Means clustering, was used in this study. The 
number k represents the clusters in this type of clustering and each data point’s cluster 
is determined based on its distance from a cluster. Centroids were kept as small as pos-
sible in this study, leading to the identification of three clusters for different investment 
types. Furthermore, the Adaptive Neuro-Fuzzy Inference System (ANFIS) was employed 
in this study. Jung first presented this system in 1993 (Jung, 1993), and its primary ben-
efit  is  how  it  simplifies  the  establishment  of  logical  judgment  [3].  ANFIS  is  based  on 
the  Sugeno  fuzzy  inference  system,  which  operates  using  “IF–THEN”  logic.  The  input 
membership functions serve as the foundation for the rules generated by the system, and 
the architecture of a FIS consists of three components: fuzzy rules, membership func-
tions, and an output generation reasoning process. During the machine learning stage, 
the  data  is  trained  using  the  ANFIS  network  and  the  output  of  the  system’s  previous 
operation serves as the system’s input. To determine the input and output of the ANFIS 
system, the study includes processing and preparation of the data. Based on ratings for 
various investment types, the recommender system suggests a final output, suggesting a 
specific type of investment to a group of potential investors. During the generation stage 
of fuzzy rules in the ANFIS system, two categories of rules are taken into consideration. 
The system generates a set of rules that are used to predict the type of investment based 
on  customer  demographic  groups.  The  rules  that  system  experts  develop  for  invest-
ment systems are based on input from experts in investment science and feedback from 
investors. To gather this feedback, a feedback form can be set up with two general ques-
tions:  a  closed-ended  question  and  an  open-ended  question.  For  example,  the  closed-
ended  question  could  ask  investors  whether  the  system’s  suggestions  align  with  their 
requirements  and  offer options for a response such as “it somewhat corresponds,” “it’s 
not entirely unrelated,” or “it has no connection at all.” The open-ended question could 
request additional feedback on the effectiveness of the system, allowing for the identi-
fication  of  weak  recommendations  and  mistakes  through  responses.  System-generated 
rules are then supplemented by manually created rules and rules based on professional 
knowledge  to  make  the  system  more  efficient.  The  conceptual  phases  of  the  research, 
including the use of a portion of the Portfolio Investment Questionnaire to define vari-
ables, are outlined in Table 1. The questionnaire is available in the Hungarian language

---

<!-- PAGE 7 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 7 of 27

Table 1  Conceptual stages of research

Conceptual stages of research

Data Collection Tool

Input

Online Questionnaire
Data Collection

Investment Type Data

Machine learning

Investment Type Clustering(JMP)

Output

Input

Intelligent Neuro-Fuzzy 
technique

Investment Types Clusters

Investment Types Clusters
Demographic Data Groups

ANFIS
(Hybrid learning algorithm)
Expert knowledge intervention

Output

Investment Type’s Recommendations
Investors Feedback

on  the  website  https:// www. portf olio. hu/ befek tetesi- kerdo iv/? page=1.  The  research  is 
conducted using a completed dataset, which has been exported based on the answers to 
the Portfolio Investment Questionnaire. According to the Worldbank.org (2020), portfo-
lio investment refers to a variety of securities, including stocks, bonds, and other invest-
ment  vehicles.  A  diversified  portfolio  reduces  the  risk  of  potential  loss  if  one  or  more 
investments perform worse than anticipated (“Portfolio Investment,” 2019).

1542 responses from an online survey conducted in 2019 were included in the analysis 
for the study entitled “Project 2018–1.3.1-VKE-2018–00007.” The survey was conducted 
in Hungarian and the researchers were given permission to use the data for additional 
research and publications as per the Consortia agreement point 6.2 of the project (refer 
to  Attachment  1  for  details).  The  data  used  in  this  study  were  selected  based  on  the 
study’s objectives and included information on the respondents’ demographics and the 
type of investment they had previously made. The data was first translated into English 
and underwent thorough cleaning before being imported into JMP for investment type 
clustering and MATLAB version R2022b for ANFIS analysis. The data here don’t need 
to be analyzed frequently. The data is only analyzed (training fetching rules from data) 
once. Then the created rules will be applied to any new set of inputs. Therefore, the com-
putational time is considered one time.

The proposed investment recommender system model

The model of the investment recommender system is based on ANFIS, as was already 
mentioned,  and  it  is  used  to  present  recommendations  regarding  the  type  of  invest-
ment. The investment type cluster advises using demographic information on customer 
groups. Several stages are considered in the outlined model.

•  Data Gathering and Processing: The first stage of the model involves gathering, stor-
ing, and preliminary processing of data. This includes acquiring demographic infor-
mation on customer groups and investment types, as well as any other relevant data 
that may be used in the model.

---

<!-- PAGE 8 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 8 of 27

•  Machine  Learning  Technique  Stage:  In  the  second  stage,  the  model  uses  machine 
learning  techniques  to  classify  and  cluster  the  data.  This  includes  establishing  two 
categories of information about customer groups and investment-type clusters using 
demographic data.

•  ANFIS  System  Implementation:  The  third  stage  involves  implementing  the  ANFIS 
system to analyze the data and make recommendations. This step uses the classifica-
tion  and  clustering  of  data  from  the  previous  stage  to  generate  investment-related 
advice.

•  Decision  Phase:  The  final  stage  of  the  model  is  the  decision  phase,  where  the  cus-
tomer receives the system’s recommendations through applications. The customer is 
also given a survey form to provide feedback on the system’s performance.

•  Iterative Improvements: The model’s cycle is repeated by using customer feedback to 
improve recommendations and fix any system flaws that may have been identified. 
The  proposed  model’s  structure  is  shown  in  Fig.  1  and  is  broken  down  into  these 
detailed steps to assist in the investment recommendations process.

The  proposed  model’s  structure  is  broken  down  into  the  following  details  to  help

with investment recommendations.

Fig. 1  A Recommender System Model for Investment Type based on the Potential Investors’ Demographic

---

<!-- PAGE 9 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 9 of 27

Data acquisition and processing layer

Data  from  prospective  investors  is  gathered  by  this  layer.  Potential  investors’  demo-
graphic information includes their gender, age, level of education, place of residence, 
job title, and income. Certain investment products, such as mutual funds, voluntary 
pension funds, securities, government bonds, and other financial products, are asso-
ciated with investment type data. A web-based questionnaire is used to gather demo-
graphic  information  as  well  as  investment-related  data.  After  initial  processing  and 
cleaning, the collected data is moved to the following layer.

Data storage and protection layer

This  layer  is  responsible  for  storing  and  protecting  the  data  processed  in  the  previ-
ous  step.  In  this  layer,  the  data  can  be  updated  in  real-time  or  in  batches.  Cloud  or 
database storage is an option. Data reconfiguration and data backup are done in this 
layer Additionally, data archiving, data auditing, and versioning are done in this layer 
as well.

Machine learning layer

This layer oversees grouping information about the type of investment. This layer cre-
ates three clusters from the data related to the type of investment using data mining 
and machine learning algorithms. The data is prepared in this layer and then sent to 
the ANFIS layer after being received from the previous layer. Three categories of clus-
ters  are  established  for  the  type  of  investment  regarding  it.  Unsupervised  machine 
learning  methods  are  used  for  this.  For  customer  groups,  six  categories  of  demo-
graphic data that fall under those six categories have been examined.

ANFIS deployment layer

The  ANFIS  deployment  layer,  based  on  the  Sugeno  fuzzy  model,  uses  six  categories 
of demographic information about potential investors as inputs and suggests invest-
ment  types  using  three  clusters  of  investment  types  as  outputs. The  input  of  invest-
ment experts and their specialized knowledge is used to enhance the system and add 
rules.  The  ANFIS  system  consists  of  several  layers,  including  fuzzification,  implica-
tion  rules,  normalization,  defuzzification,  integration,  and  output  presentation.  The 
first  layer  directs  input  signals  to  the  subsequent  layers,  with  the  fuzzy  rule  layer 
being the second layer and the normalization layer being the third. The fourth layer, 
the propagation layer, receives the first input signals, while the fifth layer, the output 
layer, transforms the fuzzy output into numerical output and aggregates the results. 
The final layer, the sixth layer, presents the recommended investment type to the cli-
ent through appropriate applications.

Application layer

In  this  layer,  the  application  offers  suggestions  to  the  client  from  the  layer  before. 
These  recommendations  are  related  to  the  type  of  investment,  and  for  a  particu-
lar  group  of  clients,  a  cluster  of  the  type  of  investment  is  considered.  Using  the 
application  that  is  installed  on  the  suitable  device,  the  investor  can  receive  system

---

<!-- PAGE 10 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 10 of 27

recommendations  in  his  or  her  profile.  The  investor  provides  his  system  with  feed-
back in this layer. Potential flaws in earlier layers are fixed and the system is improved 
based on investor feedback.

Experiments and results

There  are  three  parts  to  this  section.  On  the  basis  of  the  responses  from  prospective 
investors, the first section deals with the data clustering of various investment types. The 
second section discusses the ANFIS’s description of its demographic data. The third sec-
tion discusses the ANFIS’s inputs and outputs.

Clustering data related to investment types

The  data  was  grouped  according  to  the  investment  types  or  products  that  potential 
investors  used,  in  order  to  implement  the  proposed  investment  recommender  system 
first. The following steps involve clustering data using JMP software for this purpose:

Figure  2  illustrates  how  data  is  imported  into  JMP  to  cluster  the  various  investment 
types that potential investors use. Investment type is a topic covered by questions P24–
P27. Listed stock mutual funds, voluntary pension funds, government securities/bonds, 
and other financial products were included in the data on investment type.

The  questionnaire’s  questions  about  the  different  types  of  investments  are  listed  in 
Table 2. The potential investors’ responses were coded and transformed into numerical 
data  based  on  their  responses,  allowing  MATLAB  and  JMP  to  analyze  them.  Figure  3 
displays the JMP preparation data for K-Means clustering.

The K-Means technique in JMP is used in Fig. 4 to cluster the investment type into 
three clusters. It is 2038 in each row. Iterative clustering using the K-Means method is 
displayed in JMP in Fig. 5. The first cluster has a count of 592, the second has a count 
of 406, and the third has a count of 340, according to the cluster summary. Each K is 
now the nucleus of its respective cluster. JMP assigns data points to the closest cluster

Fig. 2  Import data to JMP to cluster used investment types by potential investors

---

<!-- PAGE 11 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 11 of 27

Table 2  Questions and answers for investment type

Question

Answers

Answer code

P24 Which of the following invest-
ment products do you think is 
right for you? (Multiple answers 
marked)

Listed stock/equity, Mutual 
fund, Voluntary pension fund, 
Government securities, and Other 
financial products

Based on the answers given to the 
question, there were 31 different 
combinations of answers. which 
was coded from 1 to 31

P25 Have you had a stock market 
investment in the last 3 years?

P26 If so, do you regularly monitor/
follow the performance of the 
stock?

P27 Do you have a government bond

investment?

Yes
No

Yes
No

Yes
No

1
2

1
2

1
2

Fig. 3  Preparing data to cluster by K-Means technique in JMP

Fig. 4  Clustering data in three clusters by K-Means technique in JMP

---

<!-- PAGE 12 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 12 of 27

Fig. 5  Iterative Clustering by K Means technique in JMP

center. Until the data points stay in their cluster, the nearest center is assigned to each 
data  point  4  times.  K-Means  are  updated  when  new  data  is  added  to  the  dataset  in 
real-time, and the clusters are updated as a result.

The optimal number of clusters can be determined using elbow curves and silhou-
ette plots. The elbow curve method is useful in identifying the point where increas-
ing the number of clusters no longer significantly reduces the within-cluster sum of 
squares.  On  the  other  hand,  silhouette  plots  provide  additional  information  by  cal-
culating  the  average  silhouette  width  for  each  cluster  and  indicating  the  degree  of 
separation between clusters. After clustering, potential investors are grouped into dif-
ferent categories. The results obtained from these groups are then used as metrics for 
the ANFIS model to make investment recommendations.

To  determine  the  optimal  number  of  clusters  for  the  investment  type  cluster,  the 
K-Means algorithm is employed, clustering the data for each value of k and calculat-
ing the Sum of Squared Errors (SSE) for each k. These SSE values are plotted against 
k to generate the Elbow curve and identify the point where the SSE starts to level off, 
which can indicate the optimal number of clusters. Additionally, the Silhouette score 
is calculated for each k, measuring how well each data point fits into its assigned clus-
ter compared to other clusters. The Silhouette scores are plotted against k to identify 
the  value  of  k  that  maximizes  the  Silhouette  score,  which  can  also  provide  insight 
into  the  optimal  number  of  clusters.  Prior  to  clustering,  it  is  essential  to  preprocess

---

<!-- PAGE 13 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 13 of 27

Fig. 6  Sorting by clusters in JMP

Fig. 7  Scatterplot for the investment type’s clusters in JMP

the data and remove any missing values. The script used for this analysis is written in 
Python and designed to run in JMP.

---

<!-- PAGE 14 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 14 of 27

JMP’s  cluster  sorting  is  shown  in  Fig.  6.  Based  on  the  cluster,  each  row’s  distance  is

indicated. The scatterplot for the investment-type clusters in JMP is displayed in Fig. 7.

Demographic ANFIS

The  questionnaire  contained  some  questions  that  measured  data  related  to  the  demo-
graphic.  The  respondents  were  questioned  about  the  demographic  data  in  six  ways 
(inputs  1–6).  This  data  sought  to  identify  the  respondents’  demographics  and  their 
choice  of  investment  strategy.  Their  responses  help  us  better  understand  how  demo-
graphics  and  financial  attitudes  are  related,  and  ultimately  how  these  factors  influence 
the choice of investment type/product.

Demographic ANFIS inputs & output

The gender of the potential investors is related to input 1 (gender) with 2 MFs. Option 
1 is considered for MF1, and Option 2 is considered for MF2. The age of the respond-
ents is indicated by the three MFs in input 2 (age). For MF1, option 1 "15–34 years old," 
option 2 "35–54 years old," and option 3 "55–79 years old" are all taken into consider-
ation.  The  location  of  the  potential  investors’  homes  is  indicated  by  input  3  (location) 
with 2 MFs. Budapest, option 1, is considered for MF1, and "other location," option 2, is 
considered for MF2. The level of education of potential investors is reflected in input 4 
(education) with 4 MFs. Option 1 "College or university economics" is taken into consid-
eration for MF1, Option 2 "College or university non-economics" is taken into consider-
ation for MF2, Option 3 "Postgraduate" is taken into consideration for MF3, and Option 
4 "Other" is taken into consideration for MF4. Input 5 (job) with 9 MFs is related to the 
job of the potential investor. Employee middle management, option 1, is considered for 
MF1. Option 2, "Small-medium business," is considered for MF2. Option 3, "Graduate 
freelance," is considered for MF3. Option 4 for MF4, "Employed lower manager," is taken 
into  consideration.  Option  5  for  MF5,  "Subordinate  intellectual  worker,"  Option  6  for 
MF6, "Skilled Worker," Option 7 for MF7, "Employed Senior Management," Option 8 for 
MF8, "Micro or Self-Employed," and Option 9 for MF9 are also taken into consideration. 
The monthly income of the potential investors is represented by input 6 (income), which 
has three MF. For MF1, option 1 of "Under 200,000 HUF," option 2 of "200,000–349,999 
HUF," and option 3 of "Above 350,000 HUF," are taken into consideration (Table 3).

Three clusters were included in one output that was defined for the investment type/
product (investment type). Listed stock mutual funds, voluntary pension funds, govern-
ment securities/bonds, and other financial products were included in the data on invest-
ment type.

Proposition of demographicanfis

Based  on  input  membership  functions,  the  "IF–THEN"  rules  govern  how  the  ANFIS 
functions (MFs). A FIS’s architecture is divided into three sections. Fuzzy rules make up 
the first part, MFs make up the second, and the reasoning process that produces the out-
put makes up the third. Four inputs and one output, each with three membership func-
tions, make up the financial ANFIS. The maximum and minimum membership functions 
for each input were one and zero, respectively. Data processing in MATLAB was done 
using a fuzzy logic toolbox. A fuzzy toolbox of MATLAB is used for this purpose in six

---

<!-- PAGE 15 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 15 of 27

Table 3  MFs of the Demographic ANFIS inputs

Input1

Input2

Input3

Input4

Input5

Input6

MFs

MF1

MF2

MFs

MF1

MF2

MF3

MFs

MF1

MF2

MFs

MF1

MF2

MF3

MF4

MFs

MF1

MF2

MF3

MF4

MF5

MF6

MF7

MF8

MF9

MFs

MF1

MF2

MF3

Gender

Male

Female

Age/year

15–34

35–54

55–79

Location

Budapest

Other

Education

College or university economics

College or university non-economics

Postgraduate

Other

Job

Employee middle management

Small medium business

Graduate freelance

Employed lower manager

Subordinate intellectual worker

Skilled worker

Employed senior management

Micro or self-employed

Other

Income/HUF

Under 200,000

200,000–349999

Above 350,000

Frequency

1307

191

Frequency

359

387

100

Frequency

784

704

Frequency

564

596

73

278

Frequency

231

115

69

138

659

51

67

88

80

Frequency

1385

104

7

fundamental fuzzy function steps to implement Demographic ANFIS: Data import, FIS 
design, data loading, FIS creation, FIS training, and FIS testing.

Figure  8  displays  the  imported  data  in  MATLAB,  which  consists  of  7  columns,  6  of 
which are related to the potential investors’ demographics. The final column relates to 
clusters  of  the  investing  kind.  The  inputs  and  output  for  the  Demographic  ANFIS  are 
indicated in the fuzzy function. A new FIS with demographics and a Sugeno-type design. 
Figure 9 depicts the DemographicANFIS system’s layout and characteristics.

A sample of the MFs in DemographicANFIS is shown in Fig. 10. This graph displays 
the  total  number  of  MFs.  The  MFs  can  be  edited  and  are  of  the  gaussmfs  kind.  Out-
put MF kind is regarded as constant. Additionally, 1542 train data pairs are taken into 
consideration. In this case, aggregation is max while the implication is considered min. 
Aggregation is the process of combining all fuzzy sets that represent each rule’s outputs 
into a single set. For each output variable, this aggregation takes place just once before 
the final defuzzification stage.

The loaded data for the subsequent data training and testing steps is shown in Fig. 11. 
A grid partition is taken into consideration for the new FIS’s training data. Additionally, 
the method’s optimization is regarded as a hybrid with epochs 3 and error tolerance 0.

---

<!-- PAGE 16 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 16 of 27

Fig. 8  Imported data to MATLAB to implement Demographic ANFIS

Fig. 9  Designing DemographicANFIS

Then a new FIS called the DemographicANFIS was created (Fig. 12).
Figure  13  shows  that  the  DemographicANFIS  network  is  trained.  The  Gauss-
ian  functions  are  used  for  each  input  during  the  training  procedure. The  number  of 
inputs is considered six for demographic groups, and the number of outputs is con-
sidered  one  for  investment  types.  The  FIS  training  method  is  a  hybrid  with  three 
epochs. Epoch 3: error = 0.8668.

---

<!-- PAGE 17 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 17 of 27

Fig. 10  A sample of membership Functions in DemographicANFIS

Fig. 11  Loaded Data to Train in DemographicANFIS

Fig. 12  Generated new FIS (DemographicANFIS)

---

<!-- PAGE 18 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 18 of 27

Fig. 13  Training DemographicANFIS

Fig. 14  Testing DemographicANFIS

Figure 14 displays the DemographicANFIS under test. 0.86683 is the average testing 
error. In Fig. 15, a portion of the rule viewer is displayed. The open system of the Demo-
graphicANFIS is depicted in this figure. There are 101 plot points and 1296 rules.

Figure 16 displays a portion of the system’s rules in verbose format. Depending on the 
opinions  of  the  experts  and  the  feedback  from  the  investors,  the  rules  may  be  added, 
modified, or removed. The importance of this possibility for recommender systems.

The  relationship  between  the  demographic  factors  influencing  investment  type  is 
established  by  the  implemented  DemographicANFIS  System.  The  three-dimensional 
graphs that illustrated how two inputs at once affected the type of investment are shown 
in Fig. 17a–f. Summary information about the deployed DemographicANFIS system is 
provided below:

---

<!-- PAGE 19 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 19 of 27

Fig. 15  The rule viewer of the opened DemographicANFIS system

Fig. 16  A part of the rules in implemented DemographicANFIS system

---

<!-- PAGE 20 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 20 of 27

Fig. 17  Effectiveness of the relations of each pair of inputs on investment type cluster

---

<!-- PAGE 21 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 21 of 27

Figure 18 depicts the DemographicANFIS’s organizational structure as the proposed

investment recommender system.

---

<!-- PAGE 22 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 22 of 27

Fig. 18  Structure of DemographicANFIS (investment recommender system)

Discussion

The aim of this study is to design a novel model for investment recommender systems 
that utilize demographic and investment preference data of potential investors. To pro-
vide guidance and support the investor’s choice, the model employs a fuzzy neural infer-
ence solution and investment type selection. Seven group agents were considered in the 
design of the investment recommender system. The ANFIS system categorizes custom-
ers based on six demographic traits using six input factors. The output of the ANFIS sys-
tem, which corresponds to three clusters of investment types, is referred to as a factor.

The  first  cluster  of  investment  types  comprises  a  significant  number  of  respondents 
with a total of 592 individuals. This cluster was given the top ranking and includes gov-
ernment securities, mutual funds, and listed stock/equity as the best investment options. 
These individuals have not made any stock market investments in the previous 3 years 
and did not regularly monitor or follow the stock’s performance. Many of them did not 
own  any  government  bonds.  The  second  cluster,  which  includes  406  respondents,  is 
in  second  place.  The  appropriate  investment  products  for  this  cluster  are  listed  stock/
equity, mutual funds, voluntary pension funds, and government securities. These indi-
viduals have invested in the stock market within the last 3 years and regularly kept an 
eye  on  and  followed  the  stock’s  performance.  Many  of  them  had  investments  in  gov-
ernment bonds. The third cluster, with 340 respondents, is in third place. The appropri-
ate investment products for this cluster are listed stock/equity, voluntary pension funds, 
and government securities. These individuals made an investment in the stock market in 
the previous 3 years and regularly checked in on and followed the stock’s performance. 
However, many of them had no investment in government bonds.

The  results  indicate  that  each  cluster’s  respondents  shared  specific  character-
istics  and  investment  preferences,  providing  valuable  insights  for  an  investment

---

<!-- PAGE 23 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 23 of 27

recommendation.  The  results  show  that  a  DemographicANFIS  investment  recom-
mender system was created using 2647 nodes. This system consists of a total of 1365 
parameters,  with  1296  being  linear  and  69  non-linear.  Machine  learning  techniques 
were  utilized  to  generate  1542  training  data  pairs  for  the  system.  The  system  ulti-
mately produced 1296 fuzzy rules for investment recommendations. In order to fully 
assess the effectiveness of the system, it is important for users to test it in real-world 
settings.  As  users  interact  with  the  system,  new  fuzzy  rules  can  be  generated  using 
feedback  from  potential  or  actual  investors  and  expert  knowledge.  One  example  of 
how the first rule in the system was generated and interpreted is provided:

The  nonlinear  monolithic  graphs  in  Fig.  17a–f  present  investment-type  recommen-
dations  based  on  a  pair  of  demographic  factors,  with  the  membership  points  of  the 
investment-type clusters represented on the z-axis. The x-axis and y-axis represent the 
membership points of the demographic characteristics of a cluster of investment types. 
For  example,  Fig.  17a  illustrates  the  respondents’  membership  in  investment  types 
according  to  their  gender  and  income.  It  shows  that  as  income  increases,  more  men 
become investors, with potential investors with monthly incomes below 100,000 forints 
primarily in the second type of investment cluster and those with monthly incomes of 
more  than  500,000  forints  primarily  in  the  third  type  of  investment  cluster.  Similarly, 
Fig. 17b shows that potential investors around the age of 45 with a monthly income of 
fewer than 100,000 forints are in the third cluster of the investment type, while those of 
the same age with a monthly income of about 300,000 forints are in the second cluster. 
Figure 17c demonstrates that potential investors living in Budapest and earning less than 
HUF 100,000 per month belong to the third investment type cluster, while those living 
elsewhere  and  earning  roughly  HUF  300,000  per  month  belong  to  the  second  invest-
ment cluster. Figure 17e illustrates that potential investors in the third cluster of invest-
ment  type  have  a  middle  manager  job  and  make  less  than  100,000  forints  per  month. 
Figure  17f  shows  that  the  first  cluster  of  investment  types  includes  potential  investors 
with  postgraduate  degrees  and  lower  manager  jobs,  while  the  third  cluster  of  invest-
ment  types  includes  potential  investors  who  hold  lower  manager  jobs  but  have  a  col-
lege or university degree. Figure 17d illustrates that potential investors with any level of 
education and a monthly income of more than 500,000 forints are assigned to the first 
cluster of investment type. Overall, these graphs suggest that different demographic fac-
tors and characteristics can influence an individual’s investment preferences and recom-
mendations. These clusters of investment types can be used to guide potential investors 
in selecting investment products such as government securities, mutual funds, stocks/
shares on stock exchanges, and voluntary pension funds.

---

<!-- PAGE 24 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 24 of 27

In comparison, previous research in the field of investment recommender systems has 
focused on various aspects to improve the accuracy and relevance of investment recom-
mendations. One study proposed a system to improve customer loyalty, while another 
proposed a model based on unique hedge funds that consider multiple factors such as 
modern-day  yields  and  historic  performance.  Another  proposed  system  incorporates 
the  use  of  agents  and  an  algorithm  to  improve  the  accuracy  of  the  recommender  sys-
tem.  Some  studies  focused  on  improving  customer  loyalty  and  utilizing  various  fac-
tors,  such  as  modern-day  yields,  historic  performance,  and  diversification  by  industry. 
Another proposed system incorporates the use of agents and an algorithm to improve 
the  accuracy  of  the  recommender  system,  while  another  proposed  model  is  based  on 
association rule mining. However, this study differs in its focus on utilizing demographic 
information  and  investment  preferences  to  generate  personalized  recommendations 
for  potential  investors  and  making  use  of  the  ANFIS  system  for  grouping  and  analyz-
ing  data.  Paranjape-Voditel  and  Umesh  [23]  proposed  a  recommender  system  based 
on association rule mining. Tejeda-Lorente et al. [35] proposed a recommender system 
that  relates  to  unique  hedge  funds  that  consider  multiple  factors,  such  as  modern-day 
yields, historic performance, and diversification by industry. Hernández et al. [14] pro-
posed  a  system  that  incorporates  the  use  of  agents  and  an  algorithm  to  improve  the 
accuracy of the recommender system. Tarnowska et al. [34] presented a recommender 
system for improving customer loyalty. Kovács, Ko, and Asemi [18] examined the use of 
a two-stage clustering method for identifying the investment patterns of potential retail 
banking  customers.  The  study  uses  a  combination  of  neural-network-based  Kohonen 
self-organizing maps (SOMs) and hierarchical clustering to analyze data from an online 
investment survey. The research found that by using this method, investment patterns 
could  be  identified,  and  customer  clusters  could  be  described  based  on  their  invest-
ment preferences and current financial assets. The study also found that the customers 
had  different  perceptions  of  different  financial  instruments  and  portfolios,  which  sug-
gested that different communication strategies might be required for different types of 
investment products. Additionally, it highlighted that risk and yield were perceived dif-
ferently  when  considering  financial  stability.  Overall,  the  study  contributes  to  the  field 
by demonstrating the benefits of using a two-stage clustering method, which allows for 
the simultaneous use of both categorical and numerical variables, in identifying invest-
ment patterns of retail banking customers. This can help in improving marketing policy 
and strategic planning in the retail banking industry. The literature review of Asemi and 
Ko  [4]  examines  the  current  state  of  investment  recommender  systems  and  the  use  of 
customer investment service feedback to improve the accuracy and relevance of invest-
ment recommendations. The authors propose a new business model for an investment 
recommender  system  that  utilizes  fuzzy  neural  inference  solutions  and  customized 
investment  services.  The  authors’  proposed  model  is  based  on  the  ANFIS  system  and 
is designed to support investment companies, individual investors, and fund managers 
in  their  investment  decisions.  The  model  identifies  seven  group  factors  to  implement 
the proposed investment system model through the customer or potential investor data 
set. These  include  demographic  data,  personality  traits,  investor  attitudes  toward  digi-
tal solutions, investor current financial status and savings, investor awareness of poten-
tial risks, and investor financial plan information. Overall, the proposed business model

---

<!-- PAGE 25 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 25 of 27

aims to improve the accuracy and relevance of investment recommendations by utilizing 
customer investment service feedback and fuzzy neural inference solutions. The litera-
ture review highlights the lack of similar models in the field and the potential benefits of 
the  proposed  model  for  investment  companies,  individual  investors,  and  fund  manag-
ers. This paper differs from these previous studies in its utilization of customer invest-
ment  service  feedback  and  fuzzy  neural  inference  solutions  to  generate  personalized 
investment  recommendations.  Moreover,  the  authors  use  the  ANFIS  system,  which  is 
a combination of the neural network and fuzzy logic, to group and analyze data which 
is something that the previous papers have not proposed. Additionally, the authors have 
considered a more comprehensive set of factors, including demographic data which can 
influence the investor’s decision-making process and make the recommendations more 
personalized. This system has several innovations The role of potential investors is the 
subject  of  its  first  innovation.  that  the  model’s  initial  inputs  are  gathered  from  regular 
users who are thought of as potential investors. The second novel aspect of this research 
is  the  proposed  ANFIS  system’s  reliance  on  professional  knowledge.  This  implies  that 
investment experts can add rules to this system in addition to those that are intelligently 
generated by it. This study’s third innovation is based on getting feedback. Investors and 
experts  both  provide  feedback,  and  the  system  can  be  improved  as  a  result.  The  pro-
posed system’s ability to operate based on erroneous or incomplete data is another inno-
vation. Most information systems must deal with this issue.

Conclusion

In conclusion, this research suggested an automated recommender system to give inves-
tors investment-related suggestions. These suggestions are based on information about 
the  investors’  demographics.  The  system  is  built  on  a  novel,  intelligent  methodology 
that  makes  use  of  ANFIS  and  six  demographic  factors.  Additionally,  this  system  oper-
ates with partial data. Based on comments made by investors using the system, it is also 
possible to put expert judgments into practice. According to the findings, the suggested 
system is a solid method for making recommendations regarding the kind of investment 
or investment products based on demographic traits.

What  matters  is  that  two  categories  of  new  rules  for  the  proposed  investment  rec-
ommender system are defined by investment experts using their knowledge. When an 
expert decides that it is necessary to eliminate one or more variables from a generated 
rule, that rule falls under a certain category. As a result, the expert can modify one or 
more of the six variables in each rule the system generates and produce a new rule. Rules 
that are not produced by the system fall into the second category. Not all the rules that 
can be created based on the available variables are necessarily generated by the proposed 
investment  recommender  system.  As  previously  mentioned,  this  system  may  function 
using  fuzzy  logic  and  incomplete  or  inaccurate  data.  Consequently,  a  new  rule  that 
incorporates all the variables and is not currently generated by the system can be added 
to it based on feedback from investors who use the system and the opinions of experts.

This  system  attempts  to  address  the  issue  of  incomplete  or  inaccurate  data  by  using 
the function described for it. One of the system’s drawbacks is that it only takes poten-
tial  investors’  demographic  information  into  account.  As  system  inputs,  these  data 
are  also  constrained  to  six  variables.  Another  drawback  is  that  only  a  few  investment

---

<!-- PAGE 26 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 26 of 27

types are clustered together and viewed as the system’s output. Naturally, the rules pro-
duced by the system will alter as the characteristics of potential investors are changed 
as  inputs  and  as  investment  types  are  altered  as  an  output  of  the  system.  Other  traits 
of potential investors may be considered as system inputs in the future. Additionally, it 
is recommended that experts conduct future research in intelligently producing knowl-
edge-based  rules  so  that  these  rules  can  be  intelligently  added  to  the  system  based  on 
experts’ judgment.
Acknowledgements
We would like to thank Ms. Asefeh Asemi from Khurzouk Municipality in interpretation of some parts of primer data that 
were gathered from customers.

Author contributions
Asefeh Asemi acted as the main researcher, Adeleh Asemi provided guidance as the research advisor, and Andrea Ko 
served as the research supervisor. All authors read and approved the final manuscript.

Funding
Open access funding provided by Corvinus University of Budapest.

Availability of data and materials
Original data was collected in partnership with the Corvinus University of Budapest, the Dorsum company, and the 
Portfolio in the 1.3.1-VKE-2018–00007 project in the Hungarian language. According to the consortium agreement and 
the head of the project’s consent, project data can be used for additional research and publications by the authors. The 
authors translated, cleaned, and prepared it for this research. New data available at Asemi, Asefeh (2022), “Data for Adap-
tive Neuro-Fuzzy Inference System for Customizing Investment Type based on the Potential Investors’ Demographics”, 
Mendeley Data, V1, https:// doi. org/ 10. 17632/ 93dmw j5yhk.1

Declarations

Ethics approval and consent to participate
This article does not contain any studies with human or animal participants performed by any of the authors.

Consent for publication
Not applicable

Competing interests
Work at the Corvinus University of Budapest helped design and develop the survey in conjunction with commercial 
companies (Dorsum and Portfolio).

Received: 5 April 2022   Accepted: 17 May 2023

References
 1.  Alpaydin, E. (2020). Introduction to Machine Learning (Fourth ed.). MIT. pp. xix, 1–3, 13–18. ISBN 978–0262043793.
 2.  Asemi, A. (2022), Data for Adaptive Neuro-Fuzzy Inference System for Customizing Investment Type based on the

Potential Investors’ Demographics, Mendeley Data, V1, https:// doi. org/ 10. 17632/ 93dmw j5yhk.1

3.  Asemi A, Asemi A. Intelligent MCDM method for supplier selection under fuzzy environment. Int J Inf Sci Manag

(IJISM). 2014;12(2):33–40.

4.  Asemi, A. & Ko, A. (2021). A Novel Combined Business Recommender System Model Using Customer Investment

Service Feedback. Proceeding of the 34th Bled eConference, June 27–30, 2021, Bled, Slovenia

5.  Asemi A, Salim SSB, Shahamiri SR, Asemi A, Houshangi N. Adaptive neuro-fuzzy inference system for evaluating dys-
arthric automatic speech recognition (ASR) systems: a case study on MVML-based ASR. Soft Comput. 2019;23:3529–
44. https:// doi. org/ 10. 1007/ s00500- 018- 3013-4.

6.  Baştanlar Y, Ozuysal M. Introduction to machine learning. Methods Mol Biol. 2014;1107:105–28. https:// doi. org/ 10.

1007/ 978-1- 62703- 748-8_7.

7.  Burke R. Hybrid web recommender systems. In: Brusilovsky P, Kobsa A, Nejdl W, editors. The Adaptive Web. Berlin/

Heidelberg: Springer; 2007.

8.  Casuat, C. D., Sadhiqin Mohd Isira, A., Festijo, E. D., Sarraga Alon, A., Mindoro, J. N., & Susa, J. A. B. (2020). A Develop-

ment of Fuzzy Logic Expert-Based Recommender System for Improving Students’Employability. 2020 11th IEEE 
Control and System Graduate Research Colloquium (ICSGRC), 59–62. https:// doi. org/ 10. 1109/ ICSGR C49013. 2020. 
92325 43

9.  Chen, J. (2020). Investment Product. Reviewed by Gordon Scott, In Investopedia.Com. https:// www. inves toped ia.

com/ terms/i/ inves tment- produ ct. asp Accessed 20 April 2020.

10.  Faridniya A, Faridnia M. Providing a model for allocating resources and choosing investment type using Data Envel-

opment Analysis (DEA) (Case Study: Social Security Organization). J Adv Pharm Edu Res. 2019;9(S2):112–24.

---

<!-- PAGE 27 -->

Asemi et al. Journal of Big Data           (2023) 10:87

Page 27 of 27

11.  Financial Conduct Authority (FCA) Handbook. (2022). investment service—FCA Handbook. Handbook.Fca.Org.Uk.

https:// www. handb ook. fca. org. uk/ handb ook/ gloss ary/ G603. html

12.  Garbade, D. M. J. (2021, April 19). Clearing the Confusion: AI vs Machine Learning vs Deep Learning Differences.

Medium. https:// towar dsdat ascie nce. com/ clear ing- the- confu sion- ai- vs- machi ne- learn ing- vs- deep- learn ing- diffe 
rences- fce69 b21d5 eb

13.  Han J, Kamber M, Pei J. Data mining: concepts and techniques. Amsterdam: Elsevier; 2012.
 14.  Hernández E, Sittón I, Rodríguez S, Gil AB, García RJ. An investment recommender multi-agent system in financial 
technology. In: Graña M, López-Guede JM, Etxaniz O, Herrero Á, Sáez JA, Quintián H, Corchado E, editors. Interna-
tional Joint Conference SOCO’18-CISIS’18-ICEUTE’18. Cham: Springer International Publishing; 2019.
Investment. (2020). In Wikipedia. https:// en. wikip edia. org/w/ index. php? title
Accessed from 20 April 2020.

Inves tment & oldid

95135 1513

15.

=

=

16.  Jang JR. ANFIS: adaptive-network-based fuzzy inference system. IEEE Trans Syst Man Cybern. 1993;23(3):665–85.

https:// doi. org/ 10. 1109/ 21. 256541.

17.  Kanaujia PKM, Manjusha P, Siddharth SR. A framework for development of recommender system for financial data

analysis. Int J Inform Eng Electron Bus. 2017;9(5):18–27.

18.  Kovács T, Ko A, Asemi A. Exploration of the investment patterns of potential retail banking customers using two-

stage cluster analysis. J Big Data. 2021;8(1):141. https:// doi. org/ 10. 1186/ s40537- 021- 00529-4.

19.  Law Insider Inc. (2022). Potential Investor Definition. In lawinsider.com. https:// www. lawin sider. com/ dicti onary/

poten tial- inves tor Accessed from 3 Apr 2022.

20.  Liang TP. Recommendation systems for decision support: an editorial introduction. Decis Support Syst.

2008;45(3):385–6. https:// doi. org/ 10. 1016/j. dss. 2007. 05. 003.

21.  Merriam-Webster. (2022). Demography. In the Merriam-Webster.com dictionary. https:// www. merri am- webst er.

com/ dicti onary/ demog raphy Accessed from 3 Apr 2022.

22.  Onsgard, K. (2019). What Are Customer Demographics—& Why Are They Vital For Marketing? https:// www. tower

data. com/ blog/ what- is- custo mer- demog raphic- data

23.  Paranjape-Voditel P, Umesh D. A stock market portfolio recommender system based on association rule mining.

Appl Soft Comput. 2013;13(2):1055–63.

24.  Paryudi I, Ashari A, Mustofa K. The performance of personality-based recommender system for fashion with demo-

graphic data-based personality prediction. Int J Adv Comput Sci Appl. 2022;13(1):360–8.

25.  Patro SGK, Mishra BK, Panda SK, Kumar R, Long HV, Tuan TM. Knowledge-based preference learning model for

recommender system using adaptive neuro-fuzzy inference system. J Intell Fuzzy Syst. 2020;39(3):4651–65. https:// 
doi. org/ 10. 3233/ JIFS- 200595.

26.  Portfolio Investment, net (BoP, current US$)|Data. (2018). https:// data. world bank. org/ indic ator/ BN. KLT. PTXL. CD

Accessed from18 Apr 2020.

27.  Portfolio investment. (2019). In Wikipedia. https:// en. wikip edia. org/w/ index. php? title

91836 2764

Portf olio_ inves tment & oldid

=

=

28.  Resnick, P., Iacovou, N., Suchak, M., Bergstrom, P., Riedl, J.: Grouplens (1994). Open architecture for collaborative filter-

ing of netnews. In: Proceedings ACM Conference on Computer-Supported Cooperative Work, pp. 175–186

29.  Resnick P, Varian HR. Recommender systems. Commun ACM. 1997;40(3):56–8.
 30.  Sarkar, D., Bali, R., Sharma, T. (2018) Machine Learning Basics. In: Practical Machine Learning with Python. Apress,

Berkeley, CA. Available at: https:// doi. org/ 10. 1007/ 978-1- 4842- 3207- 14

31.  Sarker IH. Machine learning: Algorithms, real-world applications, and research directions. SN Comput Sci.

2021;2(3):1–21. https:// doi. org/ 10. 1007/ s42979- 021- 00592-x.

32.  Sharma M, Pant B, Singh V. Demographic profile building for cold start in recommender system: a social media

fusion approach. Mater Today-Proc. 2021;46:11208–12. https:// doi. org/ 10. 1016/j. matpr. 2021. 02. 428.

33.  Sulistiyo H, Mahpudin E. Demographic analysis for the selection of an investment type for amateur golfers. In: Hurri-
yati R, Tjahjono B, Yamamoto I, Rahayu A, Abdullah AG, Danuwijaya AA, editors. Advances in Business, Management, 
and Entrepreneurship. Boca Raton: CRC Press; 2020.

34.  Tarnowska K, Ras ZW, Daniel L. Recommender system for improving customer loyalty. Cham: Springer International

Publishing; 2020.

35.  Tejeda-Lorente Á, Bernabé-Moreno J, Herce-Zelaya J, Porcel C, Herrera-Viedma E. A risk-aware fuzzy linguistic

knowledge-based recommender system for hedge funds. Procedia Comput Sci. 2019;162:916.

36.  Yassine A, Mohamed L, Al Achhab M. Intelligent recommender system based on unsupervised machine learning

and demographic attributes. Simul Model Prac Theory. 2021;107:102198. https:// doi. org/ 10. 1016/j. simpat. 2020. 
102198.

37.  Zou B, You J, Wang Q, Wen X, Jia L. Survey on learnable databases: a machine learning perspective. Big Data Res.

2022;27:100304. https:// doi. org/ 10. 1016/j. bdr. 2021. 100304.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Asemi et al. Journal of Big Data (2023) 10:87 Journal of Big Data
https://doi.org/10.1186/s40537-023-00784-7
RESEARCH Open Access
Adaptive neuro-fuzzy inference system
for customizing investment type based
on the potential investors’ demographics
and feedback
Asefeh Asemi1, Adeleh Asemi2 and Andrea Ko3*
*Correspondence:
Abstract
andrea.ko@uni-corvinus.hu
1 Doctoral School of Economics, The proposed model is an adaptive neuro-fuzzy inference recommender system that
Business, and Informatics, utilizes customer investment service feedback and fuzzy neural inference solutions
Institute of Data Analytics to generate personalized investment recommendations. The model is designed to
and Information Systems,
support the investment process for the customers and takes into consideration seven
Corvinus University of Budapest,
Budapest, Hungary factors to implement the proposed investment system model through the customer or
2 Department of Software potential investor data set. These include demographic data and investment type. The
Engineering, Faculty
model is divided into three main phases: data gathering, data analysis, and decision-
of Computer Science
and Information Technology, making. In the data gathering phase, initial data is collected through a web-based
Universiti Malaya, Kuala Lumpur, platform, and in the data analysis phase, the potential investors’ demographic crite-
Malaysia
3 Corvinus University ria are extracted and grouped, and the types of investments are then clustered. The
of Budapest, Budapest, Hungary output obtained is transferred to the ANFIS layer, and investment-type recommenda-
tions are extracted for each group of potential investors. Investor feedback is received
to improve and develop the system. JMP and MATLAB are used to propose the model,
which serves as a framework for investment recommender systems. It demonstrates
how to use this framework to offer pertinent and precise recommendations for the
best sort of investment type to potential and present investors by combining the
expertise of the experts and the demographic information of potential investors.
Overall, this paper provides a new, novel model for investment recommender systems,
which can assist investment companies, individual investors, and fund managers in
their investment decisions.
Keywords: “Adaptive Neuro-Fuzzy Inference System”, “ANFIS”, “Recommender System”,
“Demographic Data”, “Investment Type”, “Investment Product”, “Potential Investors”,
“Investor Feedback”, “Investment Service”
Introduction
One of the most important sources for understanding a company’s past, present, and
future is customer demographic data and statistics. These facts and figures are crucial
in recommender systems as they help the user receive personalized and relevant rec-
ommendations. This is particularly important as Kanaujia and his colleagues have
© The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate-
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creat iveco mmons. org/ licen ses/ by/4. 0/.

Asemi et al. Journal of Big Data (2023) 10:87 Page 2 of 27
highlighted that recommender systems should be tailored to meet the specific needs of
clients [17]. In order to address this issue, this study proposes a novel business model
for an investment recommender system that utilizes adaptive neural fuzzy inference
(ANFIS) to suggest the appropriate type of investment based on the demographic data
collected from potential investors. This data is categorized and analyzed using machine
learning techniques, serving as the system input, and the system output is the recom-
mended type of investment for the individual investor.
Theoretical framework
This research includes several concepts. These ideas encompass investor and potential
investor, demographics of potential investors, investment, recommender systems for
investments, and machine learning. The customer and the investor in this study are the
same. The following list summarizes the theoretical underpinnings:
Investor and potential investors
An investor is typically someone who invests money to gain a profit or an edge in some-
thing (Cambridge Dictionary). Anyone who purchases services or investment goods
from an investment company qualifies as an investor on their behalf. The investor could
be a legitimate source or a real individual. From the perspective of a business, a poten-
tial investor is someone or something that is in talks with the business about funding.
Potential investors in this study are different people who respond to “Investment Ques-
tionnaire” questions. These persons may not all be active investors. A community or
organization’s members can generally be thought of as potential investors. In this case,
a person rather than an organization is the potential investor, and the current study
is based on data from respondents to the “Investment Questionnaire” regarding their
demographics. Typically, when making an investment decision, an investor seeks advice.
Professional investors attempt to speak with subject-matter specialists in addition to
gathering the information they need before making an investment. It goes without say-
ing that a person’s demographic and behavioral traits will influence how they learn about
investments and consult with others. People who influence an investor’s decisions fre-
quently have a variety of professional interests. Potential investors have various invest-
ment requirements depending on their demographics. As a result, they select various
forms of investments. For instance, the most crucial criteria in selecting the sort of
investment may be income, savings, and employment.
Potential investors’ demographic
Demography, as defined by Merriam-Webster [21], is “the statistical study of human
populations, particularly with regard to size and density, distribution, and vital statistics”
in sociology. In the context of customer demographics, this refers to certain statistical
information about individuals, such as their identity information, gender, age, marital
status, and education level. This data can also include spatial information, such as mail-
ing addresses. According to Onsgard [22], other relevant consumer demographic infor-
mation includes buyer types, purchase objectives, and information about the buyer’s
lifestyle. When making decisions to improve the service or product offered by an invest-
ment company, it is crucial to consider the demographic profile of potential investors.

A semi et al. Journal of Big Data (2023) 10:87 Page 3 of 27
Factors such as age, gender, occupation, educational attainment, field of study, domicile,
place of employment, and other pertinent personal data can provide valuable insight
into how investors and potential investors use and evaluate the company’s services and
products. This understanding can also help predict the behavior of current and potential
customers. Intelligent recommender systems can be an effective tool in this prediction
and direction. These systems can establish membership functions for investment-type
memberships and membership functions related to customer demographics. Addition-
ally, the expertise of experts can be utilized to add additional rules based on their knowl-
edge, resulting in more personalized recommendations tailored to the needs of the user.
Overall, considering customer demographics is an important aspect of decision-making
for investment companies, as it can provide valuable insights into how customers use
and evaluate the company’s services and products.
Investment
To invest is to set aside money with the hope of gaining something later. According
to finance 2020, the advantage of investment is referred to as a return on investment
(“Investment”). All stocks, bonds, options, derivatives, and other financial instruments
that investors invest money in with the aim of making a profit are collectively referred to
as “investment products” [9]. The process of modifying assets over the short, medium, or
long term might be included in an investment. For example, the effectiveness of this pro-
cedure may be determined by sales, revenue from dividends, income from apartments,
etc., or a mix of other approaches. The return could potentially include gains from
foreign investments or losses because of changes in foreign exchange rates. Typically,
investors want higher returns on riskier bets. A low-risk investment often yields a low
return as well. Like excessive risk, excessive returns are also present. Any financial coun-
seling, investment management, or other related activities are referred to as "investment
services.” The FCA Handbook states that any service relating to a financial instrument
may be provided, such as receiving and transmitting orders about one or more financial
instruments, carrying out orders for clients, engaging in trading for one’s own account,
managing a portfolio, issuing personal recommendations, underwriting financial instru-
ments and/or placing them on a firm commitment basis, placing financial instruments
without a firm commitment basis, etc. The investment products included in this study’s
investment types were listed stock mutual funds, voluntary pension funds, government
securities, and bonds, as well as other financial products.
Investment recommender systems
According to Burke [7], recommender systems are software tools that employ various
methods to offer advice to users based on their interests. As stated by Resnick et al.
[28] and Resnick & Varian [29], these recommendations are highly relevant to a specific
user’s interests. Liang [20] also notes that recommender systems play the role of decision
support, making recommendations based on the outcomes of examining user behavior.
Asemi and Ko [4] note that customers may receive specific offers from recommender
systems based on their needs. This is why it is important to not treat users as a separate
class when integrating recommender systems into information systems. In investment
recommender systems, both the investor and the investment service or product must be

Asemi et al. Journal of Big Data (2023) 10:87 Page 4 of 27
considered. By identifying advanced communication patterns between the two parties
and enhancing the system, the degree to which the system’s recommendations match the
customer’s needs is successfully increased. According to the proposals made, these kinds
of technologies ought to be able to boost the company’s profitability. It is even possible
to build a comparison capability for the system to compare the feedback given in the
context of the system’s ideas regarding the types of suggested investments based on cus-
tomer input to predict. This may be determined by investor or client needs.
Machine learning
One of the subfields of artificial intelligence is machine learning, where the performance
and capability of the system are improved depending on previous results [12]. Machine
learning aims to provide computers with the ability to learn on their own by utilizing
available data and generating precise predictions [1]. The primary benefit of machine
learning is its capacity for learning from data, which is absent from many traditional
databases [37]. Artificial intelligence, natural language processing, data mining, math-
ematics, statistics, computer science, and deep learning are the primary fields associ-
ated with machine learning (Sarkar, Bali & Sharma, [30]). There are various machine
learning tasks, such as feature engineering for dimensionality reduction, association rule
learning, data clustering, regression analysis, classification analysis, and deep learning
techniques [31]. Supervised learning, unsupervised learning, semi-supervised learning,
and reinforcement learning are the four categories of machine learning based on their
intended use [6, 31]. In this study, unsupervised learning was employed. The challenge
in unsupervised learning is to uncover a hidden structure in a collection of unlabeled
data (Agrawal et al., 2005). In this type of learning, the only information present is the
data itself, which is used to group similar concepts together. Unlabeled data is used in
the system’s learning process, and each category’s notions are distinct from those of
other categories. One unsupervised machine learning technique is clustering, where
categories are not predetermined and it is also unclear which category is categorized
in accordance with which feature. Numerous clustering techniques exist, such as the
k-means clustering method and hierarchical clustering (Han, Kamber & Pei, [13]). A set
of data is clustered into groups that share the greatest characteristics. Clustering is a
frequent descriptive technique for locating homogeneous groupings of objects based on
their characteristics. Groups may overlap or be isolated. Data without tags are analyzed
via clustering, which divides them into groups based on the maximization of similarity
within groups and the minimization of similarity between groups (Agrawal et al., 2005).
Literature review
The research of this study builds upon the foundation of previous studies that have
explored the use of recommender systems in the field of investment. Several studies
have been conducted in this area. Paranjape-Voditel and Umesh [23] proposed a stock
market portfolio recommender system based on association rules that analyzes inven-
tory records and makes stock portfolio recommendations. Kanaujia et al. [17] proposed
using Apache Hadoop and Apache Mahout as a common filtering-based recommenda-
tion device for financial analysis based on savings, costs, and investments. Hernández
et al. [14] evaluated the state of financial technology and proposed a social computing

A semi et al. Journal of Big Data (2023) 10:87 Page 5 of 27
platform built on virtual organizations that enable users to gain more experience in
movements related to the financing of recommendations. Tejeda-Lorente et al. [35]
proposed a recommender system that considers various factors, such as current yields,
historical performance, and industry-wide diversity while being aware of the risks con-
nected with hedge funds. Faridniya and Faridniya (2019) used data envelopment analysis
to present a model for resource allocation and investment type selection, focusing on
the Social Security Organization (SSO) in Iran as a case study. Tarnowska et al. [34] cre-
ated a recommender system to increase customer loyalty, which considers various issues
such as assisting managers in recognizing strategic moves in their choices. Sulistiyo and
Mahpudin [33] looked at how demographics affected the type of investments people
made, using amateur golfers in Karawang City as a sample. Casuat et al. [8] developed an
expert-based system for improving students’ employability using fuzzy logic techniques.
The proposed system uses the concept of fuzzy membership degree, and it considers
both qualitative and quantitative data while making recommendations. Patro et al. [25]
presented a knowledge-based preference learning model for a recommender system
using an adaptive neuro-fuzzy inference system. The paper presents a new approach to
recommending products to customers by utilizing their preferences and past purchases.
Kovacs, Ko, and Asemi [4] explored the investment patterns of potential retail banking
customers using a two-stage cluster analysis to determine the best method for identify-
ing the customer groups that are most likely to use a bank. Asemi and Ko [4] presented
a novel combined business recommender system model using customer investment
service feedback. The main objective of this type of system is to provide information
about the products or services that are like those purchased by customers so they can
make an informed decision. Sharma et al. [32] aimed to build a recommender system
for the cold start in social media, which means when the user has not made any pre-
vious purchase yet. They focused on building a demographic profile-building tool to
identify potential customers. Yassine et al. [36] focused on the intelligent recommender
system using unsupervised machine learning techniques and demographic attributes of
users as input data. Paryudi et al. [24] discussed the performance of a personality-based
recommender system for fashion with demographic data-based personality prediction.
The study evaluated the effectiveness of this technique in predicting fashion preferences
based on personality traits. Fuzzy logic, a new and advanced method of reasoning, is
used in this study to solve the problem of incompleteness in classical logic. It has been
applied to many fields such as engineering, management, economics, etc. There has
been a significant amount of research conducted in the field of recommender systems
for investments. However, many of these studies focus on specific areas such as stock
market portfolios, hedge funds, or resource allocation. It is clear from the aforemen-
tioned studies that there is a significant amount of research that has been conducted on
the topic of recommender systems and expert-based systems. However, none of these
studies have specifically focused on developing a recommender system for the type or
product of investment based on the demographics of potential investors using ANFIS.
The new model introduced in this study aims to address this gap in the literature. This
ANFIS-based investment recommender system evaluates the potential investor’s demo-
graphic information and, using a combination of professional judgments, suggests which
investment type is best for each customer demographic. This study generates rules using

Asemi et al. Journal of Big Data (2023) 10:87 Page 6 of 27
an intelligent fuzzy framework, and based on the advice of experts, membership func-
tions can also be improved during the rule-generation process. Therefore, it fills the
gap in the literature that few studies have used the ANFIS technique and demographic
information to recommend the investment types. Overall, this study makes a valuable
contribution to the field by providing a new and innovative approach to the problem of
investment recommendations.
Methods
In this study, both quantitative and qualitative methods were employed to present a
new model for an investment recommender system. The model fuses previously learned
information with fresh concepts and utilizes fuzzy inference logic and machine learn-
ing techniques to implement its methods. One specific technique used is clustering,
where a portion of the data was clustered using the JMP clustering toolbox to categorize
prospective investors’ preferred investment types and products. The simplest machine
learning algorithm without supervision, K-Means clustering, was used in this study. The
number k represents the clusters in this type of clustering and each data point’s cluster
is determined based on its distance from a cluster. Centroids were kept as small as pos-
sible in this study, leading to the identification of three clusters for different investment
types. Furthermore, the Adaptive Neuro-Fuzzy Inference System (ANFIS) was employed
in this study. Jung first presented this system in 1993 (Jung, 1993), and its primary ben-
efit is how it simplifies the establishment of logical judgment [3]. ANFIS is based on
the Sugeno fuzzy inference system, which operates using “IF–THEN” logic. The input
membership functions serve as the foundation for the rules generated by the system, and
the architecture of a FIS consists of three components: fuzzy rules, membership func-
tions, and an output generation reasoning process. During the machine learning stage,
the data is trained using the ANFIS network and the output of the system’s previous
operation serves as the system’s input. To determine the input and output of the ANFIS
system, the study includes processing and preparation of the data. Based on ratings for
various investment types, the recommender system suggests a final output, suggesting a
specific type of investment to a group of potential investors. During the generation stage
of fuzzy rules in the ANFIS system, two categories of rules are taken into consideration.
The system generates a set of rules that are used to predict the type of investment based
on customer demographic groups. The rules that system experts develop for invest-
ment systems are based on input from experts in investment science and feedback from
investors. To gather this feedback, a feedback form can be set up with two general ques-
tions: a closed-ended question and an open-ended question. For example, the closed-
ended question could ask investors whether the system’s suggestions align with their
requirements and offer options for a response such as “it somewhat corresponds,” “it’s
not entirely unrelated,” or “it has no connection at all.” The open-ended question could
request additional feedback on the effectiveness of the system, allowing for the identi-
fication of weak recommendations and mistakes through responses. System-generated
rules are then supplemented by manually created rules and rules based on professional
knowledge to make the system more efficient. The conceptual phases of the research,
including the use of a portion of the Portfolio Investment Questionnaire to define vari-
ables, are outlined in Table 1. The questionnaire is available in the Hungarian language

A semi et al. Journal of Big Data (2023) 10:87 Page 7 of 27
Table 1 Conceptual stages of research
Conceptual stages of research
Data Collection Tool Online Questionnaire
Data Collection
Input Investment Type Data
Machine learning Investment Type Clustering(JMP)
Output Investment Types Clusters
Input Investment Types Clusters
Demographic Data Groups
Intelligent Neuro-Fuzzy ANFIS
technique (Hybrid learning algorithm)
Expert knowledge intervention
Output Investment Type’s Recommendations
Investors Feedback
on the website https:// www. portf olio. hu/ befek tetesi- kerdo iv/? page 1. The research is
=
conducted using a completed dataset, which has been exported based on the answers to
the Portfolio Investment Questionnaire. According to the Worldbank.org (2020), portfo-
lio investment refers to a variety of securities, including stocks, bonds, and other invest-
ment vehicles. A diversified portfolio reduces the risk of potential loss if one or more
investments perform worse than anticipated (“Portfolio Investment,” 2019).
1542 responses from an online survey conducted in 2019 were included in the analysis
for the study entitled “Project 2018–1.3.1-VKE-2018–00007.” The survey was conducted
in Hungarian and the researchers were given permission to use the data for additional
research and publications as per the Consortia agreement point 6.2 of the project (refer
to Attachment 1 for details). The data used in this study were selected based on the
study’s objectives and included information on the respondents’ demographics and the
type of investment they had previously made. The data was first translated into English
and underwent thorough cleaning before being imported into JMP for investment type
clustering and MATLAB version R2022b for ANFIS analysis. The data here don’t need
to be analyzed frequently. The data is only analyzed (training fetching rules from data)
once. Then the created rules will be applied to any new set of inputs. Therefore, the com-
putational time is considered one time.
The proposed investment recommender system model
The model of the investment recommender system is based on ANFIS, as was already
mentioned, and it is used to present recommendations regarding the type of invest-
ment. The investment type cluster advises using demographic information on customer
groups. Several stages are considered in the outlined model.
• Data Gathering and Processing: The first stage of the model involves gathering, stor-
ing, and preliminary processing of data. This includes acquiring demographic infor-
mation on customer groups and investment types, as well as any other relevant data
that may be used in the model.

Asemi et al. Journal of Big Data (2023) 10:87 Page 8 of 27
• Machine Learning Technique Stage: In the second stage, the model uses machine
learning techniques to classify and cluster the data. This includes establishing two
categories of information about customer groups and investment-type clusters using
demographic data.
• ANFIS System Implementation: The third stage involves implementing the ANFIS
system to analyze the data and make recommendations. This step uses the classifica-
tion and clustering of data from the previous stage to generate investment-related
advice.
• Decision Phase: The final stage of the model is the decision phase, where the cus-
tomer receives the system’s recommendations through applications. The customer is
also given a survey form to provide feedback on the system’s performance.
• Iterative Improvements: The model’s cycle is repeated by using customer feedback to
improve recommendations and fix any system flaws that may have been identified.
The proposed model’s structure is shown in Fig. 1 and is broken down into these
detailed steps to assist in the investment recommendations process.
The proposed model’s structure is broken down into the following details to help
with investment recommendations.
Fig. 1 A Recommender System Model for Investment Type based on the Potential Investors’ Demographic

A semi et al. Journal of Big Data (2023) 10:87 Page 9 of 27
Data acquisition and processing layer
Data from prospective investors is gathered by this layer. Potential investors’ demo-
graphic information includes their gender, age, level of education, place of residence,
job title, and income. Certain investment products, such as mutual funds, voluntary
pension funds, securities, government bonds, and other financial products, are asso-
ciated with investment type data. A web-based questionnaire is used to gather demo-
graphic information as well as investment-related data. After initial processing and
cleaning, the collected data is moved to the following layer.
Data storage and protection layer
This layer is responsible for storing and protecting the data processed in the previ-
ous step. In this layer, the data can be updated in real-time or in batches. Cloud or
database storage is an option. Data reconfiguration and data backup are done in this
layer Additionally, data archiving, data auditing, and versioning are done in this layer
as well.
Machine learning layer
This layer oversees grouping information about the type of investment. This layer cre-
ates three clusters from the data related to the type of investment using data mining
and machine learning algorithms. The data is prepared in this layer and then sent to
the ANFIS layer after being received from the previous layer. Three categories of clus-
ters are established for the type of investment regarding it. Unsupervised machine
learning methods are used for this. For customer groups, six categories of demo-
graphic data that fall under those six categories have been examined.
ANFIS deployment layer
The ANFIS deployment layer, based on the Sugeno fuzzy model, uses six categories
of demographic information about potential investors as inputs and suggests invest-
ment types using three clusters of investment types as outputs. The input of invest-
ment experts and their specialized knowledge is used to enhance the system and add
rules. The ANFIS system consists of several layers, including fuzzification, implica-
tion rules, normalization, defuzzification, integration, and output presentation. The
first layer directs input signals to the subsequent layers, with the fuzzy rule layer
being the second layer and the normalization layer being the third. The fourth layer,
the propagation layer, receives the first input signals, while the fifth layer, the output
layer, transforms the fuzzy output into numerical output and aggregates the results.
The final layer, the sixth layer, presents the recommended investment type to the cli-
ent through appropriate applications.
Application layer
In this layer, the application offers suggestions to the client from the layer before.
These recommendations are related to the type of investment, and for a particu-
lar group of clients, a cluster of the type of investment is considered. Using the
application that is installed on the suitable device, the investor can receive system

Asemi et al. Journal of Big Data (2023) 10:87 Page 10 of 27
recommendations in his or her profile. The investor provides his system with feed-
back in this layer. Potential flaws in earlier layers are fixed and the system is improved
based on investor feedback.
Experiments and results
There are three parts to this section. On the basis of the responses from prospective
investors, the first section deals with the data clustering of various investment types. The
second section discusses the ANFIS’s description of its demographic data. The third sec-
tion discusses the ANFIS’s inputs and outputs.
Clustering data related to investment types
The data was grouped according to the investment types or products that potential
investors used, in order to implement the proposed investment recommender system
first. The following steps involve clustering data using JMP software for this purpose:
Figure 2 illustrates how data is imported into JMP to cluster the various investment
types that potential investors use. Investment type is a topic covered by questions P24–
P27. Listed stock mutual funds, voluntary pension funds, government securities/bonds,
and other financial products were included in the data on investment type.
The questionnaire’s questions about the different types of investments are listed in
Table 2. The potential investors’ responses were coded and transformed into numerical
data based on their responses, allowing MATLAB and JMP to analyze them. Figure 3
displays the JMP preparation data for K-Means clustering.
The K-Means technique in JMP is used in Fig. 4 to cluster the investment type into
three clusters. It is 2038 in each row. Iterative clustering using the K-Means method is
displayed in JMP in Fig. 5. The first cluster has a count of 592, the second has a count
of 406, and the third has a count of 340, according to the cluster summary. Each K is
now the nucleus of its respective cluster. JMP assigns data points to the closest cluster
Fig. 2 Import data to JMP to cluster used investment types by potential investors

A  semi et al. Journal of Big Data           (2023) 10:87  Page 11 of 27
Table 2 Questions and answers for investment type
| Question | Answers | Answer code |
| -------- | ------- | ----------- |
P24 Which of the following invest- Listed stock/equity, Mutual  Based on the answers given to the
ment products do you think is  fund, Voluntary pension fund,  question, there were 31 different
right for you? (Multiple answers  Government securities, and Other  combinations of answers. which
| marked)                              | financial products | was coded from 1 to 31 |
| ------------------------------------ | ------------------ | ---------------------- |
| P25 Have you had a stock market      | Yes                | 1                      |
| investment in the last 3 years?      | No                 | 2                      |
| P26 If so, do you regularly monitor/ | Yes                | 1                      |
| follow the performance of the        | No                 | 2                      |
stock?
| P27 Do you have a government bond  | Yes | 1   |
| ---------------------------------- | --- | --- |
| investment?                        | No  | 2   |
Fig. 3 Preparing data to cluster by K-Means technique in JMP
Fig. 4 Clustering data in three clusters by K-Means technique in JMP

Asemi et al. Journal of Big Data (2023) 10:87 Page 12 of 27
Fig. 5 Iterative Clustering by K Means technique in JMP
center. Until the data points stay in their cluster, the nearest center is assigned to each
data point 4 times. K-Means are updated when new data is added to the dataset in
real-time, and the clusters are updated as a result.
The optimal number of clusters can be determined using elbow curves and silhou-
ette plots. The elbow curve method is useful in identifying the point where increas-
ing the number of clusters no longer significantly reduces the within-cluster sum of
squares. On the other hand, silhouette plots provide additional information by cal-
culating the average silhouette width for each cluster and indicating the degree of
separation between clusters. After clustering, potential investors are grouped into dif-
ferent categories. The results obtained from these groups are then used as metrics for
the ANFIS model to make investment recommendations.
To determine the optimal number of clusters for the investment type cluster, the
K-Means algorithm is employed, clustering the data for each value of k and calculat-
ing the Sum of Squared Errors (SSE) for each k. These SSE values are plotted against
k to generate the Elbow curve and identify the point where the SSE starts to level off,
which can indicate the optimal number of clusters. Additionally, the Silhouette score
is calculated for each k, measuring how well each data point fits into its assigned clus-
ter compared to other clusters. The Silhouette scores are plotted against k to identify
the value of k that maximizes the Silhouette score, which can also provide insight
into the optimal number of clusters. Prior to clustering, it is essential to preprocess

A semi et al. Journal of Big Data (2023) 10:87 Page 13 of 27
Fig. 6 Sorting by clusters in JMP
Fig. 7 Scatterplot for the investment type’s clusters in JMP
the data and remove any missing values. The script used for this analysis is written in
Python and designed to run in JMP.

Asemi et al. Journal of Big Data (2023) 10:87 Page 14 of 27
JMP’s cluster sorting is shown in Fig. 6. Based on the cluster, each row’s distance is
indicated. The scatterplot for the investment-type clusters in JMP is displayed in Fig. 7.
Demographic ANFIS
The questionnaire contained some questions that measured data related to the demo-
graphic. The respondents were questioned about the demographic data in six ways
(inputs 1–6). This data sought to identify the respondents’ demographics and their
choice of investment strategy. Their responses help us better understand how demo-
graphics and financial attitudes are related, and ultimately how these factors influence
the choice of investment type/product.
Demographic ANFIS inputs & output
The gender of the potential investors is related to input 1 (gender) with 2 MFs. Option
1 is considered for MF1, and Option 2 is considered for MF2. The age of the respond-
ents is indicated by the three MFs in input 2 (age). For MF1, option 1 "15–34 years old,"
option 2 "35–54 years old," and option 3 "55–79 years old" are all taken into consider-
ation. The location of the potential investors’ homes is indicated by input 3 (location)
with 2 MFs. Budapest, option 1, is considered for MF1, and "other location," option 2, is
considered for MF2. The level of education of potential investors is reflected in input 4
(education) with 4 MFs. Option 1 "College or university economics" is taken into consid-
eration for MF1, Option 2 "College or university non-economics" is taken into consider-
ation for MF2, Option 3 "Postgraduate" is taken into consideration for MF3, and Option
4 "Other" is taken into consideration for MF4. Input 5 (job) with 9 MFs is related to the
job of the potential investor. Employee middle management, option 1, is considered for
MF1. Option 2, "Small-medium business," is considered for MF2. Option 3, "Graduate
freelance," is considered for MF3. Option 4 for MF4, "Employed lower manager," is taken
into consideration. Option 5 for MF5, "Subordinate intellectual worker," Option 6 for
MF6, "Skilled Worker," Option 7 for MF7, "Employed Senior Management," Option 8 for
MF8, "Micro or Self-Employed," and Option 9 for MF9 are also taken into consideration.
The monthly income of the potential investors is represented by input 6 (income), which
has three MF. For MF1, option 1 of "Under 200,000 HUF," option 2 of "200,000–349,999
HUF," and option 3 of "Above 350,000 HUF," are taken into consideration (Table 3).
Three clusters were included in one output that was defined for the investment type/
product (investment type). Listed stock mutual funds, voluntary pension funds, govern-
ment securities/bonds, and other financial products were included in the data on invest-
ment type.
Proposition of demographicanfis
Based on input membership functions, the "IF–THEN" rules govern how the ANFIS
functions (MFs). A FIS’s architecture is divided into three sections. Fuzzy rules make up
the first part, MFs make up the second, and the reasoning process that produces the out-
put makes up the third. Four inputs and one output, each with three membership func-
tions, make up the financial ANFIS. The maximum and minimum membership functions
for each input were one and zero, respectively. Data processing in MATLAB was done
using a fuzzy logic toolbox. A fuzzy toolbox of MATLAB is used for this purpose in six

A  semi et al. Journal of Big Data           (2023) 10:87  Page 15 of 27
Table 3 MFs of the Demographic ANFIS inputs
|        | MFs | Gender                              | Frequency |
| ------ | --- | ----------------------------------- | --------- |
| Input1 | MF1 | Male                                | 1307      |
|        | MF2 | Female                              | 191       |
| Input2 | MFs | Age/year                            | Frequency |
|        | MF1 | 15–34                               | 359       |
|        | MF2 | 35–54                               | 387       |
|        | MF3 | 55–79                               | 100       |
| Input3 | MFs | Location                            | Frequency |
|        | MF1 | Budapest                            | 784       |
|        | MF2 | Other                               | 704       |
| Input4 | MFs | Education                           | Frequency |
|        | MF1 | College or university economics     | 564       |
|        | MF2 | College or university non-economics | 596       |
|        | MF3 | Postgraduate                        | 73        |
|        | MF4 | Other                               | 278       |
| Input5 | MFs | Job                                 | Frequency |
|        | MF1 | Employee middle management          | 231       |
|        | MF2 | Small medium business               | 115       |
|        | MF3 | Graduate freelance                  | 69        |
|        | MF4 | Employed lower manager              | 138       |
|        | MF5 | Subordinate intellectual worker     | 659       |
|        | MF6 | Skilled worker                      | 51        |
|        | MF7 | Employed senior management          | 67        |
|        | MF8 | Micro or self-employed              | 88        |
|        | MF9 | Other                               | 80        |
| Input6 | MFs | Income/HUF                          | Frequency |
|        | MF1 | Under 200,000                       | 1385      |
|        | MF2 | 200,000–349999                      | 104       |
|        | MF3 | Above 350,000                       | 7         |
fundamental fuzzy function steps to implement Demographic ANFIS: Data import, FIS
design, data loading, FIS creation, FIS training, and FIS testing.
Figure 8 displays the imported data in MATLAB, which consists of 7 columns, 6 of
which are related to the potential investors’ demographics. The final column relates to
clusters of the investing kind. The inputs and output for the Demographic ANFIS are
indicated in the fuzzy function. A new FIS with demographics and a Sugeno-type design.
Figure 9 depicts the DemographicANFIS system’s layout and characteristics.
A sample of the MFs in DemographicANFIS is shown in Fig. 10. This graph displays
the total number of MFs. The MFs can be edited and are of the gaussmfs kind. Out-
put MF kind is regarded as constant. Additionally, 1542 train data pairs are taken into
consideration. In this case, aggregation is max while the implication is considered min.
Aggregation is the process of combining all fuzzy sets that represent each rule’s outputs
into a single set. For each output variable, this aggregation takes place just once before
the final defuzzification stage.
The loaded data for the subsequent data training and testing steps is shown in Fig. 11.
A grid partition is taken into consideration for the new FIS’s training data. Additionally,
the method’s optimization is regarded as a hybrid with epochs 3 and error tolerance 0.

Asemi et al. Journal of Big Data (2023) 10:87 Page 16 of 27
Fig. 8 Imported data to MATLAB to implement Demographic ANFIS
Fig. 9 Designing DemographicANFIS
Then a new FIS called the DemographicANFIS was created (Fig. 12).
Figure 13 shows that the DemographicANFIS network is trained. The Gauss-
ian functions are used for each input during the training procedure. The number of
inputs is considered six for demographic groups, and the number of outputs is con-
sidered one for investment types. The FIS training method is a hybrid with three
epochs. Epoch 3: error 0.8668.
=

A semi et al. Journal of Big Data (2023) 10:87 Page 17 of 27
Fig. 10 A sample of membership Functions in DemographicANFIS
Fig. 11 Loaded Data to Train in DemographicANFIS
Fig. 12 Generated new FIS (DemographicANFIS)

Asemi et al. Journal of Big Data (2023) 10:87 Page 18 of 27
Fig. 13 Training DemographicANFIS
Fig. 14 Testing DemographicANFIS
Figure 14 displays the DemographicANFIS under test. 0.86683 is the average testing
error. In Fig. 15, a portion of the rule viewer is displayed. The open system of the Demo-
graphicANFIS is depicted in this figure. There are 101 plot points and 1296 rules.
Figure 16 displays a portion of the system’s rules in verbose format. Depending on the
opinions of the experts and the feedback from the investors, the rules may be added,
modified, or removed. The importance of this possibility for recommender systems.
The relationship between the demographic factors influencing investment type is
established by the implemented DemographicANFIS System. The three-dimensional
graphs that illustrated how two inputs at once affected the type of investment are shown
in Fig. 17a–f. Summary information about the deployed DemographicANFIS system is
provided below:

A semi et al. Journal of Big Data (2023) 10:87 Page 19 of 27
Fig. 15 The rule viewer of the opened DemographicANFIS system
Fig. 16 A part of the rules in implemented DemographicANFIS system

Asemi et al. Journal of Big Data (2023) 10:87 Page 20 of 27
Fig. 17 Effectiveness of the relations of each pair of inputs on investment type cluster

A semi et al. Journal of Big Data (2023) 10:87 Page 21 of 27
Figure 18 depicts the DemographicANFIS’s organizational structure as the proposed
investment recommender system.

Asemi et al. Journal of Big Data (2023) 10:87 Page 22 of 27
Fig. 18 Structure of DemographicANFIS (investment recommender system)
Discussion
The aim of this study is to design a novel model for investment recommender systems
that utilize demographic and investment preference data of potential investors. To pro-
vide guidance and support the investor’s choice, the model employs a fuzzy neural infer-
ence solution and investment type selection. Seven group agents were considered in the
design of the investment recommender system. The ANFIS system categorizes custom-
ers based on six demographic traits using six input factors. The output of the ANFIS sys-
tem, which corresponds to three clusters of investment types, is referred to as a factor.
The first cluster of investment types comprises a significant number of respondents
with a total of 592 individuals. This cluster was given the top ranking and includes gov-
ernment securities, mutual funds, and listed stock/equity as the best investment options.
These individuals have not made any stock market investments in the previous 3 years
and did not regularly monitor or follow the stock’s performance. Many of them did not
own any government bonds. The second cluster, which includes 406 respondents, is
in second place. The appropriate investment products for this cluster are listed stock/
equity, mutual funds, voluntary pension funds, and government securities. These indi-
viduals have invested in the stock market within the last 3 years and regularly kept an
eye on and followed the stock’s performance. Many of them had investments in gov-
ernment bonds. The third cluster, with 340 respondents, is in third place. The appropri-
ate investment products for this cluster are listed stock/equity, voluntary pension funds,
and government securities. These individuals made an investment in the stock market in
the previous 3 years and regularly checked in on and followed the stock’s performance.
However, many of them had no investment in government bonds.
The results indicate that each cluster’s respondents shared specific character-
istics and investment preferences, providing valuable insights for an investment

A semi et al. Journal of Big Data (2023) 10:87 Page 23 of 27
recommendation. The results show that a DemographicANFIS investment recom-
mender system was created using 2647 nodes. This system consists of a total of 1365
parameters, with 1296 being linear and 69 non-linear. Machine learning techniques
were utilized to generate 1542 training data pairs for the system. The system ulti-
mately produced 1296 fuzzy rules for investment recommendations. In order to fully
assess the effectiveness of the system, it is important for users to test it in real-world
settings. As users interact with the system, new fuzzy rules can be generated using
feedback from potential or actual investors and expert knowledge. One example of
how the first rule in the system was generated and interpreted is provided:
The nonlinear monolithic graphs in Fig. 17a–f present investment-type recommen-
dations based on a pair of demographic factors, with the membership points of the
investment-type clusters represented on the z-axis. The x-axis and y-axis represent the
membership points of the demographic characteristics of a cluster of investment types.
For example, Fig. 17a illustrates the respondents’ membership in investment types
according to their gender and income. It shows that as income increases, more men
become investors, with potential investors with monthly incomes below 100,000 forints
primarily in the second type of investment cluster and those with monthly incomes of
more than 500,000 forints primarily in the third type of investment cluster. Similarly,
Fig. 17b shows that potential investors around the age of 45 with a monthly income of
fewer than 100,000 forints are in the third cluster of the investment type, while those of
the same age with a monthly income of about 300,000 forints are in the second cluster.
Figure 17c demonstrates that potential investors living in Budapest and earning less than
HUF 100,000 per month belong to the third investment type cluster, while those living
elsewhere and earning roughly HUF 300,000 per month belong to the second invest-
ment cluster. Figure 17e illustrates that potential investors in the third cluster of invest-
ment type have a middle manager job and make less than 100,000 forints per month.
Figure 17f shows that the first cluster of investment types includes potential investors
with postgraduate degrees and lower manager jobs, while the third cluster of invest-
ment types includes potential investors who hold lower manager jobs but have a col-
lege or university degree. Figure 17d illustrates that potential investors with any level of
education and a monthly income of more than 500,000 forints are assigned to the first
cluster of investment type. Overall, these graphs suggest that different demographic fac-
tors and characteristics can influence an individual’s investment preferences and recom-
mendations. These clusters of investment types can be used to guide potential investors
in selecting investment products such as government securities, mutual funds, stocks/
shares on stock exchanges, and voluntary pension funds.

Asemi et al. Journal of Big Data (2023) 10:87 Page 24 of 27
In comparison, previous research in the field of investment recommender systems has
focused on various aspects to improve the accuracy and relevance of investment recom-
mendations. One study proposed a system to improve customer loyalty, while another
proposed a model based on unique hedge funds that consider multiple factors such as
modern-day yields and historic performance. Another proposed system incorporates
the use of agents and an algorithm to improve the accuracy of the recommender sys-
tem. Some studies focused on improving customer loyalty and utilizing various fac-
tors, such as modern-day yields, historic performance, and diversification by industry.
Another proposed system incorporates the use of agents and an algorithm to improve
the accuracy of the recommender system, while another proposed model is based on
association rule mining. However, this study differs in its focus on utilizing demographic
information and investment preferences to generate personalized recommendations
for potential investors and making use of the ANFIS system for grouping and analyz-
ing data. Paranjape-Voditel and Umesh [23] proposed a recommender system based
on association rule mining. Tejeda-Lorente et al. [35] proposed a recommender system
that relates to unique hedge funds that consider multiple factors, such as modern-day
yields, historic performance, and diversification by industry. Hernández et al. [14] pro-
posed a system that incorporates the use of agents and an algorithm to improve the
accuracy of the recommender system. Tarnowska et al. [34] presented a recommender
system for improving customer loyalty. Kovács, Ko, and Asemi [18] examined the use of
a two-stage clustering method for identifying the investment patterns of potential retail
banking customers. The study uses a combination of neural-network-based Kohonen
self-organizing maps (SOMs) and hierarchical clustering to analyze data from an online
investment survey. The research found that by using this method, investment patterns
could be identified, and customer clusters could be described based on their invest-
ment preferences and current financial assets. The study also found that the customers
had different perceptions of different financial instruments and portfolios, which sug-
gested that different communication strategies might be required for different types of
investment products. Additionally, it highlighted that risk and yield were perceived dif-
ferently when considering financial stability. Overall, the study contributes to the field
by demonstrating the benefits of using a two-stage clustering method, which allows for
the simultaneous use of both categorical and numerical variables, in identifying invest-
ment patterns of retail banking customers. This can help in improving marketing policy
and strategic planning in the retail banking industry. The literature review of Asemi and
Ko [4] examines the current state of investment recommender systems and the use of
customer investment service feedback to improve the accuracy and relevance of invest-
ment recommendations. The authors propose a new business model for an investment
recommender system that utilizes fuzzy neural inference solutions and customized
investment services. The authors’ proposed model is based on the ANFIS system and
is designed to support investment companies, individual investors, and fund managers
in their investment decisions. The model identifies seven group factors to implement
the proposed investment system model through the customer or potential investor data
set. These include demographic data, personality traits, investor attitudes toward digi-
tal solutions, investor current financial status and savings, investor awareness of poten-
tial risks, and investor financial plan information. Overall, the proposed business model

A semi et al. Journal of Big Data (2023) 10:87 Page 25 of 27
aims to improve the accuracy and relevance of investment recommendations by utilizing
customer investment service feedback and fuzzy neural inference solutions. The litera-
ture review highlights the lack of similar models in the field and the potential benefits of
the proposed model for investment companies, individual investors, and fund manag-
ers. This paper differs from these previous studies in its utilization of customer invest-
ment service feedback and fuzzy neural inference solutions to generate personalized
investment recommendations. Moreover, the authors use the ANFIS system, which is
a combination of the neural network and fuzzy logic, to group and analyze data which
is something that the previous papers have not proposed. Additionally, the authors have
considered a more comprehensive set of factors, including demographic data which can
influence the investor’s decision-making process and make the recommendations more
personalized. This system has several innovations The role of potential investors is the
subject of its first innovation. that the model’s initial inputs are gathered from regular
users who are thought of as potential investors. The second novel aspect of this research
is the proposed ANFIS system’s reliance on professional knowledge. This implies that
investment experts can add rules to this system in addition to those that are intelligently
generated by it. This study’s third innovation is based on getting feedback. Investors and
experts both provide feedback, and the system can be improved as a result. The pro-
posed system’s ability to operate based on erroneous or incomplete data is another inno-
vation. Most information systems must deal with this issue.
Conclusion
In conclusion, this research suggested an automated recommender system to give inves-
tors investment-related suggestions. These suggestions are based on information about
the investors’ demographics. The system is built on a novel, intelligent methodology
that makes use of ANFIS and six demographic factors. Additionally, this system oper-
ates with partial data. Based on comments made by investors using the system, it is also
possible to put expert judgments into practice. According to the findings, the suggested
system is a solid method for making recommendations regarding the kind of investment
or investment products based on demographic traits.
What matters is that two categories of new rules for the proposed investment rec-
ommender system are defined by investment experts using their knowledge. When an
expert decides that it is necessary to eliminate one or more variables from a generated
rule, that rule falls under a certain category. As a result, the expert can modify one or
more of the six variables in each rule the system generates and produce a new rule. Rules
that are not produced by the system fall into the second category. Not all the rules that
can be created based on the available variables are necessarily generated by the proposed
investment recommender system. As previously mentioned, this system may function
using fuzzy logic and incomplete or inaccurate data. Consequently, a new rule that
incorporates all the variables and is not currently generated by the system can be added
to it based on feedback from investors who use the system and the opinions of experts.
This system attempts to address the issue of incomplete or inaccurate data by using
the function described for it. One of the system’s drawbacks is that it only takes poten-
tial investors’ demographic information into account. As system inputs, these data
are also constrained to six variables. Another drawback is that only a few investment

Asemi et al. Journal of Big Data (2023) 10:87 Page 26 of 27
types are clustered together and viewed as the system’s output. Naturally, the rules pro-
duced by the system will alter as the characteristics of potential investors are changed
as inputs and as investment types are altered as an output of the system. Other traits
of potential investors may be considered as system inputs in the future. Additionally, it
is recommended that experts conduct future research in intelligently producing knowl-
edge-based rules so that these rules can be intelligently added to the system based on
experts’ judgment.
Acknowledgements
We would like to thank Ms. Asefeh Asemi from Khurzouk Municipality in interpretation of some parts of primer data that
were gathered from customers.
Author contributions
Asefeh Asemi acted as the main researcher, Adeleh Asemi provided guidance as the research advisor, and Andrea Ko
served as the research supervisor. All authors read and approved the final manuscript.
Funding
Open access funding provided by Corvinus University of Budapest.
Availability of data and materials
Original data was collected in partnership with the Corvinus University of Budapest, the Dorsum company, and the
Portfolio in the 1.3.1-VKE-2018–00007 project in the Hungarian language. According to the consortium agreement and
the head of the project’s consent, project data can be used for additional research and publications by the authors. The
authors translated, cleaned, and prepared it for this research. New data available at Asemi, Asefeh (2022), “Data for Adap-
tive Neuro-Fuzzy Inference System for Customizing Investment Type based on the Potential Investors’ Demographics”,
Mendeley Data, V1, https:// doi. org/ 10. 17632/ 93dmw j5yhk.1
Declarations
Ethics approval and consent to participate
This article does not contain any studies with human or animal participants performed by any of the authors.
Consent for publication
Not applicable
Competing interests
Work at the Corvinus University of Budapest helped design and develop the survey in conjunction with commercial
companies (Dorsum and Portfolio).
Received: 5 April 2022 Accepted: 17 May 2023
References
1. Alpaydin, E. (2020). Introduction to Machine Learning (Fourth ed.). MIT. pp. xix, 1–3, 13–18. ISBN 978–0262043793.
2. Asemi, A. (2022), Data for Adaptive Neuro-Fuzzy Inference System for Customizing Investment Type based on the
Potential Investors’ Demographics, Mendeley Data, V1, https:// doi. org/ 10. 17632/ 93dmw j5yhk.1
3. Asemi A, Asemi A. Intelligent MCDM method for supplier selection under fuzzy environment. Int J Inf Sci Manag
(IJISM). 2014;12(2):33–40.
4. Asemi, A. & Ko, A. (2021). A Novel Combined Business Recommender System Model Using Customer Investment
Service Feedback. Proceeding of the 34th Bled eConference, June 27–30, 2021, Bled, Slovenia
5. Asemi A, Salim SSB, Shahamiri SR, Asemi A, Houshangi N. Adaptive neuro-fuzzy inference system for evaluating dys-
arthric automatic speech recognition (ASR) systems: a case study on MVML-based ASR. Soft Comput. 2019;23:3529–
44. https:// doi. org/ 10. 1007/ s00500- 018- 3013-4.
6. Baştanlar Y, Ozuysal M. Introduction to machine learning. Methods Mol Biol. 2014;1107:105–28. https:// doi. org/ 10.
1007/ 978-1- 62703- 748-8_7.
7. Burke R. Hybrid web recommender systems. In: Brusilovsky P, Kobsa A, Nejdl W, editors. The Adaptive Web. Berlin/
Heidelberg: Springer; 2007.
8. Casuat, C. D., Sadhiqin Mohd Isira, A., Festijo, E. D., Sarraga Alon, A., Mindoro, J. N., & Susa, J. A. B. (2020). A Develop-
ment of Fuzzy Logic Expert-Based Recommender System for Improving Students’Employability. 2020 11th IEEE
Control and System Graduate Research Colloquium (ICSGRC), 59–62. https:// doi. org/ 10. 1109/ ICSGR C49013. 2020.
92325 43
9. Chen, J. (2020). Investment Product. Reviewed by Gordon Scott, In Investopedia.Com. https:// www. inves toped ia.
com/ terms/i/ inves tment- produ ct. asp Accessed 20 April 2020.
10. Faridniya A, Faridnia M. Providing a model for allocating resources and choosing investment type using Data Envel-
opment Analysis (DEA) (Case Study: Social Security Organization). J Adv Pharm Edu Res. 2019;9(S2):112–24.

A semi et al. Journal of Big Data (2023) 10:87 Page 27 of 27
11. Financial Conduct Authority (FCA) Handbook. (2022). investment service—FCA Handbook. Handbook.Fca.Org.Uk.
https:// www. handb ook. fca. org. uk/ handb ook/ gloss ary/ G603. html
12. Garbade, D. M. J. (2021, April 19). Clearing the Confusion: AI vs Machine Learning vs Deep Learning Differences.
Medium. https:// towar dsdat ascie nce. com/ clear ing- the- confu sion- ai- vs- machi ne- learn ing- vs- deep- learn ing- diffe
rences- fce69 b21d5 eb
13. Han J, Kamber M, Pei J. Data mining: concepts and techniques. Amsterdam: Elsevier; 2012.
14. Hernández E, Sittón I, Rodríguez S, Gil AB, García RJ. An investment recommender multi-agent system in financial
technology. In: Graña M, López-Guede JM, Etxaniz O, Herrero Á, Sáez JA, Quintián H, Corchado E, editors. Interna-
tional Joint Conference SOCO’18-CISIS’18-ICEUTE’18. Cham: Springer International Publishing; 2019.
15. Investment. (2020). In Wikipedia. https:// en. wikip edia. org/w/ index. php? title Inves tment & oldid 95135 1513
= =
Accessed from 20 April 2020.
16. Jang JR. ANFIS: adaptive-network-based fuzzy inference system. IEEE Trans Syst Man Cybern. 1993;23(3):665–85.
https:// doi. org/ 10. 1109/ 21. 256541.
17. Kanaujia PKM, Manjusha P, Siddharth SR. A framework for development of recommender system for financial data
analysis. Int J Inform Eng Electron Bus. 2017;9(5):18–27.
18. Kovács T, Ko A, Asemi A. Exploration of the investment patterns of potential retail banking customers using two-
stage cluster analysis. J Big Data. 2021;8(1):141. https:// doi. org/ 10. 1186/ s40537- 021- 00529-4.
19. Law Insider Inc. (2022). Potential Investor Definition. In lawinsider.com. https:// www. lawin sider. com/ dicti onary/
poten tial- inves tor Accessed from 3 Apr 2022.
20. Liang TP. Recommendation systems for decision support: an editorial introduction. Decis Support Syst.
2008;45(3):385–6. https:// doi. org/ 10. 1016/j. dss. 2007. 05. 003.
21. Merriam-Webster. (2022). Demography. In the Merriam-Webster.com dictionary. https:// www. merri am- webst er.
com/ dicti onary/ demog raphy Accessed from 3 Apr 2022.
22. Onsgard, K. (2019). What Are Customer Demographics—& Why Are They Vital For Marketing? https:// www. tower
data. com/ blog/ what- is- custo mer- demog raphic- data
23. Paranjape-Voditel P, Umesh D. A stock market portfolio recommender system based on association rule mining.
Appl Soft Comput. 2013;13(2):1055–63.
24. Paryudi I, Ashari A, Mustofa K. The performance of personality-based recommender system for fashion with demo-
graphic data-based personality prediction. Int J Adv Comput Sci Appl. 2022;13(1):360–8.
25. Patro SGK, Mishra BK, Panda SK, Kumar R, Long HV, Tuan TM. Knowledge-based preference learning model for
recommender system using adaptive neuro-fuzzy inference system. J Intell Fuzzy Syst. 2020;39(3):4651–65. https://
doi. org/ 10. 3233/ JIFS- 200595.
26. Portfolio Investment, net (BoP, current US$)|Data. (2018). https:// data. world bank. org/ indic ator/ BN. KLT. PTXL. CD
Accessed from18 Apr 2020.
27. Portfolio investment. (2019). In Wikipedia. https:// en. wikip edia. org/w/ index. php? title Portf olio_ inves tment & oldid
= =
91836 2764
28. Resnick, P., Iacovou, N., Suchak, M., Bergstrom, P., Riedl, J.: Grouplens (1994). Open architecture for collaborative filter-
ing of netnews. In: Proceedings ACM Conference on Computer-Supported Cooperative Work, pp. 175–186
29. Resnick P, Varian HR. Recommender systems. Commun ACM. 1997;40(3):56–8.
30. Sarkar, D., Bali, R., Sharma, T. (2018) Machine Learning Basics. In: Practical Machine Learning with Python. Apress,
Berkeley, CA. Available at: https:// doi. org/ 10. 1007/ 978-1- 4842- 3207- 14
31. Sarker IH. Machine learning: Algorithms, real-world applications, and research directions. SN Comput Sci.
2021;2(3):1–21. https:// doi. org/ 10. 1007/ s42979- 021- 00592-x.
32. Sharma M, Pant B, Singh V. Demographic profile building for cold start in recommender system: a social media
fusion approach. Mater Today-Proc. 2021;46:11208–12. https:// doi. org/ 10. 1016/j. matpr. 2021. 02. 428.
33. Sulistiyo H, Mahpudin E. Demographic analysis for the selection of an investment type for amateur golfers. In: Hurri-
yati R, Tjahjono B, Yamamoto I, Rahayu A, Abdullah AG, Danuwijaya AA, editors. Advances in Business, Management,
and Entrepreneurship. Boca Raton: CRC Press; 2020.
34. Tarnowska K, Ras ZW, Daniel L. Recommender system for improving customer loyalty. Cham: Springer International
Publishing; 2020.
35. Tejeda-Lorente Á, Bernabé-Moreno J, Herce-Zelaya J, Porcel C, Herrera-Viedma E. A risk-aware fuzzy linguistic
knowledge-based recommender system for hedge funds. Procedia Comput Sci. 2019;162:916.
36. Yassine A, Mohamed L, Al Achhab M. Intelligent recommender system based on unsupervised machine learning
and demographic attributes. Simul Model Prac Theory. 2021;107:102198. https:// doi. org/ 10. 1016/j. simpat. 2020.
102198.
37. Zou B, You J, Wang Q, Wen X, Jia L. Survey on learnable databases: a machine learning perspective. Big Data Res.
2022;27:100304. https:// doi. org/ 10. 1016/j. bdr. 2021. 100304.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.