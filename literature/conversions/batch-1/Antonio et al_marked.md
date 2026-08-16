---
conversion_metadata:
  converted_at: "2026-07-22T11:57:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Antonio et al.pdf"
  source_pdf_sha256: "cea527d6e61e5e688c8c1deb44bb7d39c0bbbe0d35567ac2e655ccbb5a91830a"
  page_count: 30
  markdown_char_count: 218035
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Antonio et al. Financial Innovation           (2024) 10:94  
https://doi.org/10.1186/s40854-024-00625-3

Financial Innovation

RESEARCH

Open Access

Examining user behavior with machine 
learning for effective mobile peer-to-peer 
payment adoption

Blanco‑Oliver Antonio1*, Lara‑Rubio Juan2, Irimia‑Diéguez Ana1 and Liébana‑Cabanillas Francisco3

*Correspondence:   
aj_blanco@us.es

1 Department of Financial 
Economics and Operations 
Management, University 
of Seville, Seville, Av. Ramón y 
Cajal, 1, 41018 Seville, Spain
2 Department of Finance, 
University of Granada, Granada, 
Spain
3 Department of Marketing 
and Market Research, University 
of Granada, Granada, Spain

Abstract 
Disruptive innovations caused by FinTech (i.e., technology‑assisted customized financial 
services) have brought digital peer‑to‑peer (P2P) payments to the fore. In this chal‑
lenging environment and based on theories about customer behavior in response 
to technological innovations, this paper identifies the drivers of consumer adoption 
of mobile P2P payments and develops a machine learning model to predict the use 
of this thriving payment option. To do so, we use a unique data set with information 
from 701 participants (observations) who completed a questionnaire about the adop‑
tion of Bizum, a leading mobile P2P platform worldwide. The respondent profile 
was the average Spanish citizen within the framework of European culture and lifestyle. 
We document (in this order of priority) the usefulness of mobile P2P payments, influ‑
ence of peers and other social groups such as friends, family, and colleagues on indi‑
vidual behavior (that is, subjective norms), perceived trust, and enjoyment of the user 
experience within the digital context and how those attributes better classify (poten‑
tial) users of mobile P2P payments. We also find that nonparametric approaches based 
on machine learning algorithms outperform traditional parametric methods. Finally, 
our results show that feature selection based on random forest, such as the Boruta 
procedure, as a preprocessing technique substantially increases prediction perfor‑
mance while reducing noise, redundancy of the resulting model, and computational 
costs. The main limitation of this research is that it only has a place within the socio‑
cultural and institutional framework of the Spanish population. It is therefore desirable 
to replicate this study by surveying people from other countries to analyze the effects 
of the institutional environment on the adoption of mobile P2P payments.

Keywords:  Boruta, Feature selection, Mobile, P2P, Payment, Random forest

JEL Classification:  C45, C53, G17, G28, F65

Introduction

The financial services industry has recently been forced to adopt technological changes 
to innovate its processes and products (Frame et al. 2018; Kou et al. 2021). As a result, 
a  set  of  technology-assisted  customized  financial  services  (FinTech)  has  arisen  in 
the  banking  market  (Thakor  2020).  Prominent  among  them  are  nonintermediated

© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits 
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original 
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third 
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate‑
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by/4.0/.

---

<!-- PAGE 2 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 2 of 30

peer-to-peer  (P2P)  transactions  based  on  digital  infrastructures,  such  as  lending  and 
payments. Indeed, mobile P2P payments are a business vector with deeper market pen-
etration (Abdullah and Naved Khan 2021) and have experienced an extraordinary boom, 
particularly  since  the  beginning  of  the  COVID-19  pandemic  (Higueras-Castillo  et  al. 
2023).  It  should  be  noted  that  mobile  P2P  payments  constitute  a  real  threat  to  tradi-
tional payment methods and were born from a need to break the domination of cash and 
credit  card  payments  for  common  day-to-day  purchases  (Belanche  et  al.  2022;  Insider 
Intelligence  2022).  Mobile  P2P  payments  have  emerged  as  a  singular  digital  payment 
system  and  are  simpler,  faster,  more  convenient,  usually  cost-free,  and  feature  a  social 
component  that  other  (digital  and  not  digital)  systems  lack  (Li  et  al.  2021;  Nasir  et  al. 
2020, 2021).

Given that mobile P2P payments are a disruptive innovation in the financial services 
sector,  previous  research  has  focused  on  identifying  the  factors  determining  their  use 
(Leong et al. 2022). In practice, financial entities drive change by fostering digital pay-
ments among customers. Thus, they need to know the attributes that explain customary 
resistance to change and the barriers to using new technologies and transferring know-
how  (Irimia-Diéguez  et  al.  2023).  In  this  vein,  Liébana-Cabanillas  et  al.  (2021)  showed 
that  the  precursors  and  barriers  to  using  P2P  payments  differ  from  those  of  mobile-
based payment methods, calling for further research.

Therefore, the key research question that this paper aims to shed light on is the drivers 
and barriers that foster the adoption of mobile P2P payments between banking custom-
ers (Shaikh et al. 2023). Accordingly, the main objective of this paper is to analyze factors 
that  determine  customers’  adoption  of  mobile  P2P  payments.  Our  contribution  lies  in 
finding the key variables that allow banking customers to be classified as users (or non-
users) of mobile P2P payments. To this end, we compare traditional parametric statisti-
cal techniques with a set of nonparametric approaches based on machine learning (ML) 
methods oriented to classification problems. These learning algorithms are the founda-
tions of data mining and big data current trending topics in the financial innovation field 
and  are  considered  to  be  a  crucial  part  of  a  wider  research  area  known  as  Knowledge 
Discovery from Data, which focuses on identifying patterns in data sets (Nguyen et al. 
2022).

It is worth highlighting, as one of the core strengths of the present study, the use of a 
unique  data  set  with  information  from  701  individuals  (observations)  who  were  asked 
about the use of mobile P2P payments; namely, the use of Bizum, one of the leading and 
pioneering mobile P2P payment applications worldwide, whose success is comparable to 
Venmo in the USA (Acker and Murthy 2020).

This paper contributes to the FinTech and ML literature in two ways. Practically, our 
findings have significant implications for banks with a high interest in precisely knowing 
the factors that impact the intent to use mobile P2P payment services to (i) create more 
customized  products  and  services  to  satisfy  the  needs  of  their  customers  to  a  greater 
extent and (ii) properly plan their business, human resource, and marketing strategies. 
One  of  the  key  points  of  this  research  is  the  sample,  which  is  built  on  a  survey  con-
ducted with users of the mobile P2P payment platform Bizum. We highlight that one of 
the main variables explaining the adoption of Bizum as a mobile P2P payment is its full 
connection and integration with traditional financial players. In other words, given that

---

<!-- PAGE 3 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 3 of 30

Bizum is a bank-based platform with a largely predefined bank–customer relationship, it 
has benefited from its deep market penetration into the traditional banking industry to 
create new business relationships and become a trustworthy and massively used mobile 
P2P payment platform. Indeed, this, together with the development of technology allow-
ing the widespread use of smartphones, is a primary factor explaining the strong expan-
sion and adoption of Bizum as a mobile P2P payment method.

Theoretically,  our  framework  employs  the  most  relevant  models  from  technology 
acceptance  theories.  We  use  variables  from  the  theory  of  reasoned  action  from  Fish-
bein  and  Ajzen  (1977),  technology  acceptance  model  (TAM)  from  Davis  et  al.  (1989), 
theory  of  planned  behavior  from  Ajzen  (1991),  extended  TAM,  namely  TAM  2  from 
Venkatesh and Davis (2000) and TAM 3 from Venkatesh and Bala (2008), unified theory 
of acceptance and use of technology (UTAUT) from Venkatesh et al. (2003), UTAUT2 
from  Venkatesh  et  al.  (2012),  and  mobile  payment  technology  acceptance  model  from 
Liébana-Cabanillas  et  al.  (2014).  Empirically,  we  follow  Witten  and  Frank  (2005),  who 
suggest  implementing  various  statistical  languages  and  search  procedures  that  serve 
some problems well and others badly, an added motivation for more carefully construct-
ing and comparing alternative ML techniques. In addition, the first preselection of inde-
pendent variables is applied by combining Boruta and Gini index procedures to obtain 
a  more  parsimonious  model.  Thus,  the  comparison  of  different  ML  techniques  in  the 
field  of  user  adoption  of  mobile  P2P  payments  constitutes  the  second  contribution  of 
this study.

The  rest  of  this  paper  is  structured  as  follows.  "Theoretical  background"  section 
describes the dataset and the learning machine models used in this research. "Methodol-
ogy" section presents the empirical results, "Results" section contains the discussion, and 
"Discussion" section sets out the conclusions, implications, and areas for future research.

Theoretical background
Evolution of payment systems

New  payment  systems  have  emerged  from  advancements  in  information  and  commu-
nication  technology  for  financial  transactions  between  businesses  and  their  custom-
ers.  Specifically,  these  systems  arise  as  a  means  of  addressing  certain  issues  associated 
with handling physical money (Tamayo 1999), the need to reduce the cost of money and 
existing  payment  methods,  providing  flexibility  for  small  purchases  and  instant  pay-
ments, enhancing security and protection against fraud and other forms of crime, and 
the rise of e-commerce on the Internet and online payments.

Consequently, the financial sector is undergoing a profound transformation where tra-
ditional payment systems relying on cash are being replaced by electronic payment sys-
tems (see Fig. 1). According to a recent study by the European Central Bank (2022), the 
total number of noncash payment transactions in the euro area, encompassing all types 
of payment services, increased by 12.5% compared to the previous year, reaching 114.2 
billion  transactions,  with  a  total  amount  increase  of  18.6%  to  197  trillion  euros.  Card 
payments  accounted  for  49%  of  the  total  transactions,  transfers  represented  22%,  and 
direct debits represented 20%.

In addition to this trend, the extensive use of technologies such as mobile phones has 
also  brought  about  significant  changes  in  user  payment  behaviors  (Liébana-Cabanillas

---

<!-- PAGE 4 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 4 of 30

Fig. 1  Classification of payment systems.  Source: Own elaboration based on Huang (2021)

et al. 2022a). Current mobile payment solutions are based on the technological develop-
ment of smartphones, enabling the creation of payment applications that can be used in 
various ways for conducting payment transactions with a mobile device (Liébana-Caba-
nillas et al. 2017). The classification of mobile payments evolves from the use of smart-
phones at the point of sale, where they are used to perform economic transactions for 
purchasing products or services and even function as a point-of-sale terminal for cus-
tomers. Second, mobile phones can serve as a standard payment platform, offering vari-
ous functionalities such as executing payments and sending money. Third, these phones 
can be used as a payment channel through the user’s telecommunications operator, with 
whom they have a contracted phone line.

Finally,  closed-loop  payments  refer  to  mobile  applications  specifically  developed  for 
a  particular  store  or  brand,  where  the  mobile  phone  functions  not  only  as  a  payment 
option  within  that  store  but  also  includes  additional  payment-related  services  such  as 
promotional notifications, loyalty programs, and discount coupons.

Previous research on mobile payment adoption

Since  the  seminal  work  of  Dahlberg  et  al.  (2008)  on  mobile  payment  systems,  various 
authors  have  analyzed  the  field  of  mobile  payments  up  to  the  present  day  (Liébana-
Cabanillas et al. 2022b; Migliore et al. 2022). Dennehy and Sammon (2015) concluded 
that research on mobile payments is a well-established area that will continue to receive 
increased attention from various disciplines in the coming years, recognizing the poten-
tial and enrichment of mobile payment services as their adoption becomes increasingly 
imperative.  To  date,  customer  adoption  continues  to  be  of  interest  to  many  research-
ers, but the focus remains on investigating adoption in specific countries separately, with 
less attention given to comparing survey results across multiple countries and examin-
ing their differences. More recently, authors such as Abdullah and Naved Khan (2021), 
Tounekti et al. (2022), and Panetta et al. (2023) have proposed bibliometric reviews that 
highlight the importance of this current and future research topic. Furthermore, recent 
studies  on  adoption  have  specifically  examined  technology,  security,  and  architecture.

---

<!-- PAGE 5 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 5 of 30

Table 1  Recent research on mobile payment adoption

References

Theory

Results

Patil et al. (2017)

Extended UTAUT

Jun et al. (2018)

VAM

Moorthy et al. (2020)

UTAUT2

Liébana‑Cabanillas et al. (2019) Mixed model

Flavián et al. (2020)

Extended TAM

The results revealed that performance expectancy and 
perceived usefulness, followed by perceived ease of use, 
are the factors influencing consumers’ positive behav‑
ioural intention towards mobile payment services, while 
perceived risk emerges as the main inhibitor

Compatibility, simplicity, and economic value have an 
impact on users’ perceived value and the perceived 
value has an impact on the intention of continued use of 
mobile payments

The study revealed that performance expectancy, facili‑
tating conditions, hedonic motivation, and perceived 
security are significant in mobile payment adoption. 
However, effort expectancy and social influence are not 
significant

The results show that satisfaction, service quality, effort 
expectancy, and perceived risk are determining factors 
of the continuance intention to use mobile payment 
applications

The results showed that mindfulness, perceived ease of 
use, perceived usefulness, subjective norms, and attitude 
have a significant influence on mobile payment use 
intention

Wu et al. (2021)

UTAUT2

+

ITM

+

TTF The study found that initial trust, performance expec‑
tancy, effort expectancy, facilitating conditions, price 
value, task technology fit, and initial trust have significant 
effects on use intention

Rafdinal and Senalasari (2021)

Extended TAM

Türker et al. (2022)

Extended TAM

Migliore et al. (2022)

UTAUT2

+

IRT

Bailey et al. (2022)

UTAUT2

Liébana‑Cabanillas et al. (2022a) Extended TAM

Technology Readiness Index constructs affect perceived 
usefulness and perceived ease of use, except for discom‑
fort which has no significant effect on the perceived use‑
fulness. In addition, attitude is influenced by two main 
TAM variables: perceived usefulness and perceived ease 
of use. Meanwhile, the intention to use mobile payment 
applications is influenced by attitude

Perceived usefulness, trust and compatibility positively 
and significantly affect IU, while PS has a negative and 
significant impact

The proposed theoretical model identified performance 
expectancy, social influence, facilitating conditions, 
hedonic motivations, and effort expectancy as significant 
antecedents of the intended use of mobile payment

Performance expectancy, social influence, bank trust, 
confidence in MP system and consumer innovativeness 
all impact consumers’ MP use intention; and use inten‑
tion impacts MP behaviour

The results revealed that, of the three proposed ante‑
cedents, perceived usefulness is the most important, 
followed by attitude and perceived security

Source: TAM (technology acceptance model), UTAUT (unified theory of acceptance and use of technology), ITM (initial trust 
model), TTF (task technology fit), Value-based adoption model (VAM) and IRT (innovation resistance theory)

Table 1 summarizes recent research that has analyzed the adoption of mobile payment 
systems.

Peer‑to‑peer mobile payment system: Bizum

P2P  payments  are  peer-to-peer  applications  that  facilitate  the  immediate  transfer 
of  mobile  money  transactions  anywhere.  Furthermore,  this  type  of  payment,  which 
was  previously  widespread  in  the  private  sphere,  is  also  starting  to  extend  into  the 
commercial  realm  for  making  purchases  at  physical  establishments.  An  increasing

---

<!-- PAGE 6 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 6 of 30

number of consumers are using P2P payment apps to pay for their purchases at retail 
stores. This trend is driven by the growing acceptance of P2P payments by merchants 
(Visconti-Caparrós et al. 2022).

One pioneering P2P payment system in Europe is Bizum, which is known for its origin 
and comparative competitiveness. It offers its users three major advantages: (i) immedi-
acy, as transferred funds reach recipients’ bank accounts within seconds; (ii) universality, 
as customers do not need to switch financial institutions, and the system is connected 
to all participating banks; and (iii) user-friendliness, as it allows users to make payments 
between individuals as well as at physical and online stores.

In addition, its operation is straightforward: to send money, the Bizum user selects a 
contact from their mobile phone lists and sets the desired transfer amount. The sender’s 
bank then sends a code to their mobile phone, which the user enters into the app, and 
the recipient immediately receives the money in their linked bank account.

Bizum is supported by all Spanish banks, with an option for each e-banking applica-
tion, and it is used by more than 21 million active users (nearly 50% of the Spanish popu-
lation), having a historical track record of 1,362 million transactions and more than EUR 
70.5 million transferred since its launch in 2016 (Bizum 2022). Bizum can be considered 
a transversal payment method because its customer profile includes people of any age, 
educational level, and socioeconomic class (Belanche et al. 2022).

Considering  this  review  of  the  adoption  of  mobile  payment  systems  in  general,  and 
P2P systems in particular, as well as in line with our objectives, the current research pro-
poses an improvement in the analysis techniques that may determine the variables that 
foster the intention to use P2P payment systems through the application of different sta-
tistical languages combining Boruta and Gini index procedures to obtain a more parsi-
monious model.

Machine learning and mobile payments

Comparative analysis of key machine learning techniques

ML  is  a  part  of  artificial  intelligence  that,  by  compiling  statistical  algorithms  and  sys-
tems,  demonstrates  intelligence  to  interpret  external  data  correctly  and  subsequently 
make  decisions  (Davenport  et  al.  2020).  In  essence,  ML  models  seek  to  learn  relation-
ships and patterns from a given dataset, and therefore, they can be used to solve both 
predictive and classification/categorization problems (Bishop 2006).

ML is emerging in parallel with the development of computational science and data-
driven  business  management  (Sheth  and  Kellstadt  2021).  This  is  why,  in  recent  years, 
numerous  ML-based  intelligent  systems  have  been  massively  penetrating  our  business 
and personal lives (known as the Internet of Things, IoT) (Kaplan and Haenlein 2019). 
Indeed, ML shows a much greater performance in high-dimensional data environments, 
where  variable  interactions  and  nonlinear  relationships  often  arise,  and  automatized 
recurrent decisions are required (Vanini et al. 2023). Accordingly, ML algorithms have 
been successfully applied in many fields, such as banking, to decide whether to approve 
or  reject  a  loan  application  (Alonso-Robisco  and  Carbó-Martínez  2022),  and  in  engi-
neering for structural design (Thai 2022).

One  of  the  pioneering  ML  models  that  have  subsequently  reached  a  remarkable 
expansion and relevance is artificial neural networks (ANNs). ANNs attempt to emulate

---

<!-- PAGE 7 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 7 of 30

human brain functioning by creating a set of interconnected nodes (artificial neurons) 
placed on several layers that reason in a network architecture (Selvamuthu et al. 2019). 
Among  the  most  used  neural  networks  in  business  research  is  the  multilayer  percep-
tron  (MLP)  (Vellido  et  al.  1999),  whose  main  theoretical  advantage  is  that  of  support-
ing  the  fulfillment  of  the  universal  approximate  property  (Bishop  2006).  Nevertheless, 
in  recent  years,  complex  ANN  architectures  have  emerged,  namely  deep  ANNs  (e.g., 
convolutional ANNs), which already excel in human performance in some environments 
(Madani et al. 2018).

Despite their advantages, the main limitation of ANNs is their black-box nature, which 
jeopardizes  the  interpretation  of  results  and  the  importance,  effects,  and  relationships 
between the variables. ANNs have a high computational cost to tune the training param-
eters, which lengthens the time required to design the topology of the optimal network.

At  the  beginning  of  the  current  century,  ensemble  methods  emerged,  whose  main 
ground is that the nature of a phenomenon is captured to a greater extent by combining 
several alternative methods that are subsequently synthesized by a sole optimal model. 
That is, ensemble algorithms benefit from the strengths of different models without con-
ducting a biased model preselection. Within the ensemble-based approach, two primary 
methods emerge: bagging and boosting models.

First,  the  bagging  algorithm  proposed  by  Breiman  (1996)  fits  the  same  underlying 
algorithm  to  each  training  step,  creating  a  final  prediction  that  is  the  average  of  each 
bootstrap prediction. Given a classification model, bagging draws B independent sam-
ples with a replacement from the available training set (bootstrap samples), fits a model 
to each bootstrap sample, and finally aggregates the B models by majority voting. Since 
the final prediction is always a pondered result of several bootstrap fits, bagging power-
fully decreases the model variance and biases, leading to a model with higher generaliza-
tion ability without overfitting problems (Schapire et al. 1998).

This advantage allows bagging to be successfully applied to generate other ML mod-
els. In this vein, when bagging is applied to a tree-based method, this results in a model 
called random forests (RF), which is one of the most relevant ML techniques (Breiman 
2001). RF is an ML method based on the building and combination of a large set of trees. 
The main strength of RF is that in each split, a random subset of predictors is consid-
ered, increasing the probability of weak predictors being selected and thereby reducing 
bias in the model. Otherwise, stronger predictors would be used by many trees as a first 
split. To do so, it randomly selects the variables to split the dataset and create each node 
while each tree grows from a bootstrap sample of the training dataset.

The growing interest in the use of RFs is also due to their capacity to rank predictor 
variables  according to their importance in explaining the studied phenomenon (Fried-
man  et  al.  2000).  That  is,  unlike  most  ML  methods  that  have  a  black-box  nature,  RF 
shows  how  each  variable  influences  the  understanding  of  the  analyzed  event.  Indeed, 
this  is  the  procedure  employed  in  this  study  to  select  the  most  relevant  variables  (see 
"Feature selection results" section). Moreover, other positive aspects of this method are 
that  it  does  not  generally  overfit  and  that  Bayes  consistency  is  obtained  with  a  simple 
version of RF (Breiman 2001).

Note that RF can be considered an improved version of the classification and regres-
sion trees (CART) approach. In this vein, RF randomly selects the variables to split the

---

<!-- PAGE 8 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 8 of 30

dataset  and  creates  each  node  while  each  tree  grows  from  a  bootstrap  sample  of  the 
training  dataset.  Thus,  it  does  not  fail  as  CART,  as  the  main  disadvantage  lies  in  that 
a change in a higher-level node, by the domino effect, can lead to completely different 
trees. In other words, the performance of the CART is strongly dependent on the stop-
ping criteria implemented because this model is developed using binary recursive par-
titioning, which is an iterative procedure of splitting the dataset until reaching the final 
nodes.  Of  course,  CART  also  has  advantages.  Indeed,  Breiman  (2001)  considers  that 
CART  is  the  model  with  easier  understanding  and  interpretation.  Further,  CART  also 
assumes nonlinear relationships between variables and higher-order interactions (Boul-
esteix et al. 2015).

Second, unlike bagging, boosting trains models sequentially by analyzing the predic-
tion  errors,  which  results  in  a  powerful  improvement  of  the  classifiers  (Freund  1995). 
AdaBoost is the most relevant model within this approach. AdaBoost assigns increasing 
weights  to  observations  that  are  incorrectly  classified  in  the  last  iteration  of  the  clas-
sifier.  Consequently,  the  subsequent  iterations  will  focus  on  correctly  classifying  these 
observations,  which  ultimately  will  minimize  the  prediction  errors.  In  this  paper,  we 
implement  Adaboost  as  well  as  Binominal  Boosting  and  L2  Boosting.  Other  boosting 
algorithms related to additive basis expansion were developed by Friedman et al. (2000).
Finally, support vector machine (SVM) is a powerful technique mainly used for binary 
classification problems, although it can also be applied to multiclass classifications that 
build a hyperplane to separate the observations of different classes. To do so, the SVM 
uses support vectors that are data falling closest to the hyperplane. Although SVM usu-
ally  generates  low  misclassification  errors  and  can  function  well  in  environments  with 
high-dimensional  data,  it  has  a  high  operational  cost  in  terms  of  time  consumption. 
Moreover,  sometimes  SVM  works  with  a  nonoptimal  function,  which  undermines  its 
performance.

User behavior prediction

Behavior analysis was introduced in 1953 by Skinner (1953) and focused on analyzing 
human  behavior  from  a  psychological  perspective.  However,  technological  advance-
ments  have  allowed  massive  data  processing  and  the  powerful  development  of  data 
mining and ML algorithms that have been increasingly applied to explore human behav-
ior,  biasing  behavior  analysis  toward  the  computational  science  area.  Indeed,  behavior 
analysis is currently called behavioral analytics (Cao et al. 2015), whose aim is to model 
human behavior by understanding the past to predict its future, and thus create business 
strategies using statistical and ML approaches (Martín et al. 2021).

From  the  beginning,  these  analyses  essentially  address  how  individuals  interact  and 
the role that they play by acting as a group (collaboration-competition) as well as indi-
vidually  (routines–attitudes–intentions).  However,  the  study  of  human  behavior  is  not 
altruistic. Rather, there is a strong economic interest that companies are trying to exploit 
to  increase  their  market  share,  brand,  and  products-services  positioning  and,  ulti-
mately, their profits. For this reason, currently, this discipline is closely connected to the 
economy  and  organizational  management  and  is  encompassed  in  the  field  called  user

---

<!-- PAGE 9 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 9 of 30

behavior analysis, which comes together with human behavior ML techniques and busi-
ness decision-making (LeCun et al. 2015; Cui et al. 2016).

In practice, ML has been successfully employed in different domains related to disrup-
tive  innovations  and  marketing,  such  as  the  recommendation  of  products  to  potential 
customers (Hagenauer and Helbich 2017) or the estimation of consumer preferences for 
technology products (Guo et al. 2021).

Particularly relevant is the use of ML in P2P finance (also known as Internet or Digital 
Finance), which mainly operates through the Internet; therefore, a large amount of data 
must  be  processed  before  decision-making  (Wu  et  al.  2018).  As  suggested  by  Gomber 
et al. (2017), digital finance is a new form of finance based on third-party payment, cloud 
computing,  big  data,  social  networks,  and  e-commerce  platforms  to  obtain  financing 
and credit as well as to make payments and other financial transactions. In this challeng-
ing  environment,  ML  can  collect  new  data,  update  the  model,  and  provide  an  output, 
thus adapting to rapidly evolving environments, such as economic patterns and shocks.

Indeed, ML is being effectively used to explore the factors that influence users’ digital 
finance behavior (Xiong et al. 2022). Authentication technology, the nonrepudiation of 
transactions, privacy protection, data integrity, and user trust have a significant impact 
on users’ Internet finance behavior.

Focusing on e-payment users, Bajari et al. (2015) suggested that ML techniques out-
perform  discrete  choice  models,  which  have  been  the  referenced  statistical  methods 
used to analyze consumers’ preferences and adoption of means of payments and other 
digital  financial  services  (Hernández-Murillo  et  al.  2010).  As  pointed  out  by  Cui  et  al. 
(2016),  ML  is  a  powerful  methodological  approach  that  promises  to  generate  new 
insights  into  payment  behavior.  In  this  sense,  Lee  et  al.  (2020)  used  a  two-stage  anal-
ysis  by  employing  Partial  Least  Squares  and  subsequently  an  artificial  neural  network 
to  explore  the  antecedents  that  affect  users’  behavioral  intention  to  use  wearable  pay-
ments. Also, Aslam et al. (2022), using SVM, studied the users´ behavioral factors that 
explain  the  adoption  of  mobile  payments.  They  found  perceived  value  to  be  the  most 
important predictor of usage behavior. Even, users´ behavior with mobile payments has 
been employed as a driver to forecast, through ML, stores’ total customer flows (Ma and 
Fildes 2020).

To  the  best  of  the  authors´  knowledge,  only  the  above  few  research  articles  analyze 
the  users´  behavior  regarding  digital  payments;  therefore,  more  empirical  evidence  is 
needed. This is not surprising given that mobile payment applications are not yet widely 
used  by  the  population,  and  more  importantly,  there  is  very  little  leading  e-payment 
software that massively operates in a country (as does happen with Bizum). Therefore, 
it is not possible to question users about the behavioral factors that lead them to adopt 
these mobile payments. This reinforces the findings of the present study.

Methodology

In  this  study,  we  use  a  primary  source  of  data  obtained  from  a  survey  of  701  Spanish 
smartphone users who are considered potential users of mobile P2P payment systems. 
All the users who participated in the survey had experience using their cell phones for 
commercial activities, either for shopping or payments. The profile of the respondents 
was  that  of  an  average  Spanish  citizen  having  their  place  in  the  European  culture  and

---

<!-- PAGE 10 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 10 of 30

lifestyle framework. To collect the data, nonprobability snowball sampling was employed 
through a mailing list and social networks. Although simple random sampling is the best 
sampling method, many empirical studies published in high-impact journals have used a 
snowball method when collecting data (Belanche et al. 2022; Huang et al. 2019).

The  questionnaire  included  items  to  measure  the  variables  defined  in  Table  2.  The 
items  were  selected  through  a  review  of  the  relevant  literature,  adapting  the  origi-
nal scales to the nature of the research. The participants expressed their attitudes on a 
seven-point Likert scale (1: strongly disagree; 7: strongly agree). The questionnaire was 
developed using a multi-item approach, where three or more items measured each latent 
variable.  This  is  a  common  procedure  in  the  field  of  marketing  research.  Appendix  1 
provides the questionnaire used in the study for reference.

The dependent variable is a dummy variable with a null value (0) in the case of a mer-
chant not having a mobile payment system available and a value of one (1) in the case of 
these payment systems being available to customers, according to the following:

Yit

=

1 use mobile payment system
0 does not use mobile payment system

To  execute  this  research,  we  will  classify  the  independent  variables  used  in  two  cat-
egories.  We  established  a  group  of  behavioral  variables  related  to  the  main  theories 
concerning  the  adoption  of  technologies  (perceived  ease  of  use,  perceived  risk,  trust, 
personal innovativeness, subjective norms, perceived enjoyment, loyalty to the banking 
brand, and perceived quality) and a second group of variables linked to the demographic 
classification of potential users of the payment system (gender and age).

Regarding  the  first  group  of  variables,  the  classic  scientific  literature  has  developed 
multiple theories that have analyzed the behavior of individuals despite innovation. In 
recent  years,  some  authors  have  applied  these  theories  to  the  field  of  mobile  and  P2P 
payments  (Upadhyay  et  al.  2022;  Belanche  et  al.  2022).  Table  2  describes  the  variables 
used and the sources employed for their definition.

Table 2  Variables and theoretical background

Variable

Ease of use

Perceived risk

Perceived Trust

Definition

Individuals’ perception that the use of a given sys‑
tem is effortless and/or uncomplicated

A combination of uncertainty plus seriousness of 
outcome involved

Psychological state reflecting favourable expecta‑
tions about the intentions and behaviour of others

Source

Davis (1989)

Singh and Sirdeshmukh (2000)

Personal Innovation

Willingness to try out new information technologies Agarwal and Prasad (1998a)

Subjective norms

Perceived enjoyment

Expectation that the social environment influences 
the decisions of potential users

Pleasure derived from the use of a particular infor‑
mation technology

Fishbein and Ajzen (1975)

Kalinic et al. (2019)

Loyalty to the bank brand Reinforcement of users’ intentions based on the

Lewis and Soureli (2006)

Perceived quality

previous experience of each user

Users’ subjective comparison between the quality 
of service desired and the quality of service actually 
received

Gefen et al. (2003)

---

<!-- PAGE 11 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 11 of 30

The  second  block  of  variables  refers  to  the  gender  and  age  of  potential  users  of  the 
proposed payment system. Therefore, our study includes the same categories used by the 
Spanish National Employment Institute in its statistical reports to classify a population.

Results
Feature selection results

We  performed  two  preprocessing  procedures  because,  as  supported  by  Chen  et  al. 
(2020),  their  use  substantially  improves  the  prediction  result.  First,  all  predictor  vari-
ables were standardized into the [0,1] interval to align the dimensionality of predictors 
and dependent (dummy) variables. Second, given that we have high-dimensional data in 
terms of the number of features (forty-two independent variables, see Table 3), it is nec-
essary to apply a procedure to reduce the complexity of the model by capturing only the 
most relevant inputs. The inclusion of many predictors in a model to solve a classifica-
tion problem has severe theoretical disadvantages such as: (i) overfitting, (ii) correlation 
problems,  (iii)  difficulty  in  interpreting  results,  and  (iv)  a  slower  training  process.  The 
idea is to reduce the noise and redundancy in the final model. Indeed, the principle of 
parsimony states that the best statistical model has fewer parameters (variables) and less 
dimensionality (Arora and Kaur 2020; Speiser et al. 2019).

Consequently, we performed a procedure to select the most relevant predictors. This 
minimizes the complexity of our model and accelerates its training, as well as improves 
the  robustness  of  performance  measurements,  in  terms  of  higher  accuracy  or  lower 
errors,  due  to  the  booster  of  the  generalization  capacity  of  a  classifier.  Dewi  (2019) 
indicated  that  the  feature  selection  (FS)  of  the  procedure  enables  reducing  the  origi-
nal features of a dataset to a smaller one while preserving the relevant information and 
rejecting redundant information. As Chen et al. (2020) sustain, FS crucially impacts the 
performance of the classification model. Indeed, FS is considered more important than 
designing the prediction model.

Following  Chen  et  al.  (2020),  we  implement  the  random  forest  (RF)  algorithm  as 
a  method  to  select  the  most  relevant  feature  from  the  data.  Unlike  other  parametric 
techniques grounded in subset selection, such as logistic regression (LR) with forward 
or backward procedures, RF is a nonparametric method based on supervised ML that 
incorporates  two  procedures  to  select  the  most  important  variables:  (i)  the  package 
varImp() of R, where the mean decrease of the Gini index is calculated, and (ii) Boruta 
(Fahimifar et al. 2022).

The package varImp() of R is implemented after running the RF model. This is a post-
estimation procedure applied to each tree obtained and consists of calculating the pre-
diction  accuracy  and  subsequently  permuting  each  predictor  variable.  Afterward,  the 
difference between the two accuracies is averaged over all the trees normalized by the 
SE. The package provides two measures of importance for each predictor, disaggregating 
the results by outcome class (1, when Bizum is adopted, and 0 otherwise). The first of 
these metrics indicates the decrease, on average, in accuracy when a variable is removed. 
The  second  measure  provides  the  reduction  of  the  Gini  impurity  when  a  variable  is 
chosen to split a node. It should be noted that the sample used to calculate the impor-
tance of each variable is the out-of-sample data that was not used during tree construc-
tion. The recommendation is to analyze both measures together because this enables a

---

<!-- PAGE 12 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 12 of 30

Table 3  Feature selection (FS) under random forest approach

Boruta procedure

Variables Mean

importance

Median 
importance

Min. 
importance

Max. 
importance

Gini index procedure

Norm hits

Decision

Variables Mean

PU2

PU4

PU1

SN4

TR2

PU3

SN3

PENJ2

TR5

PENJ3

PENJ1

TR3

SN2

PII1

QUAL3

PII2

TR4

QUAL2

SN1

QUAL7

PII3

QUAL4

TR1

PII4

PEOU1

QUAL6

PR1

QUAL5

PR4

PR2

PEOU4

QUAL1

PEOU2

LOY1

PEOU5

PR3

LOY4

LOY3

LOY2

AGE

GENDER

PEOU3

16.35

16.34

13.23

13.06

12.67

12.50

12.50

12.31

11.77

11.76

11.44

10.98

10.73

10.53

10.15

10.01

16.25

16.39

13.21

12.97

12.78

12.49

12.44

12.20

11.70

11.77

11.43

11.00

10.72

10.50

10.15

10.08

9.89

9.74

8.90

7.55

7.50

7.46

7.18

6.86

6.21

4.92

4.91

4.84

4.74

4.54

4.24

4.22

3.98

3.94

3.86

3.46

3.05

2.97

2.86

0.61

0.63

1.04

−

−

−

9.90

9.81

8.90

7.55

7.54

7.40

7.21

6.84

6.20

4.87

4.89

4.89

4.80

4.59

4.11

4.23

3.92

3.94

3.97

3.41

3.14

2.97

2.88

0.71

0.96

1.05

−

−

−

15.01

14.53

11.50

11.56

10.72

10.84

10.97

10.98

10.18

10.29

9.93

9.23

9.22

8.62

7.83

8.16

8.58

7.06

7.33

5.40

5.15

5.74

5.57

5.49

3.64

3.03

2.62

2.72

2.37

1.81

2.32

2.23

1.34

1.43

1.00

0.04

0.05

1.08

0.63

1.45

2.29

2.18

−

−

−

−

−

17.72

17.62

15.33

14.55

13.89

14.26

14.53

14.10

13.33

13.13

12.73

12.40

12.43

12.41

11.91

11.42

11.31

11.84

11.38

9.39

9.44

9.00

9.00

8.37

8.35

7.41

6.71

6.70

6.81

6.60

6.11

5.85

6.36

6.88

6.17

5.35

5.28

4.83

5.16

0.90

2.50

1.10

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

1.00

0.99

1.00

1.00

0.99

0.98

0.94

0.90

0.94

0.91

0.90

0.85

0.87

0.82

0.80

0.76

0.68

0.57

0.57

0.52

0.00

0.00

0.00

Confirmed

Confirmed

Confirmed

Confirmed

PU2

PU4

SN3

PU3

Confirmed

PENJ1

Confirmed

Confirmed

Confirmed

SN4

SN2

PU1

Confirmed PENJ2

Confirmed TR2

Confirmed

TR5

Confirmed

PENJ3

Confirmed

PII1

Confirmed

QUAL3

Confirmed

QUAL2

Confirmed

Confirmed

Confirmed

Confirmed

TR3

SN1

TR4

PII2

Confirmed

QUAL4

Confirmed

AGE

Confirmed

QUAL7

Confirmed

TR1

Confirmed

PEOU1

Confirmed

Confirmed

Confirmed

Confirmed

Confirmed

PII3

PR4

PII4

PR1

PR2

Confirmed

QUAL6

Confirmed

PR3

Confirmed

QUAL1

Confirmed

QUAL5

Confirmed

PEOU4

Confirmed

Confirmed

Tentative

Tentative

Tentative

Rejected

Rejected

LOY1

LOY4

PEOU2

PEOU5

LOY3

LOY2

GENERO

Rejected

PEOU3

decrease 
Gini

11.29

10.98

10.51

10.39

9.88

9.66

8.87

8.85

8.72

8.23

8.03

7.37

7.31

6.91

6.68

6.65

6.59

6.56

6.13

5.85

5.76

5.55

5.33

5.01

4.69

4.66

4.55

4.44

4.30

4.20

4.13

4.06

4.02

3.96

3.94

3.92

3.79

3.69

3.67

3.60

1.71

0.24

The variables in bold were not included in the model

comparison of the importance ranking of each one. However, their main disadvantage is 
that they may overstate the importance of the correlated variables.

To benchmark with respect to FS, we also implemented the Boruta algorithm that 
enables  ranking  the  predictor  variables  based  on  their  significance  (default  values 
for p value = 0.01 and maxRun = 100). One of the most important advantages of the

---

<!-- PAGE 13 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 13 of 30

use  of  Boruta  is  that  it  provides  a  classification  of  the  variables  in  three  groups:  (i) 
confirmed, for those significant variables (the most relevant); (ii) tentative, for those 
variables that may be selected, but which have less importance; and (iii) rejected, for 
those variables that the method considers are not to be included.

The  results  of  the  FS  analysis  are  depicted  in  Table  3  (graphically  also  in  Fig.  2).  As 
shown here, the two FS procedures employed (Boruta and the Gini index) match most of 
the rankings performed, especially in the first variables, i.e., the variables with the high-
est classification of importance.

Unlike  the  Gini  index,  one  of  the  main  advantages  of  the  Boruta  procedure  is  that 
it enables knowing which variable must be included in the model. However, as can be 
observed  in  Table  3,  the  Boruta  procedure  considers  that  the  entire  list  of  variables 
should be introduced into the model because they have a high importance level. There-
fore, it is not operational from a computational viewpoint. Consequently, to increase the 
selection capacity of the FS procedures, we only select, from the ten first variables, the 
variables matching the two criteria (Boruta and the Gini index).

Eight  of  the  ten  first  variables  are  the  most  relevant  under  both  FS  criteria  (see 
Table 3); thus, these variables will be included in our classification model. It should be 
noted  that  with  this  procedure,  we  are  dramatically  reducing  the  number  of  variables 
that will be introduced into our model, considering only eight (i.e., only 19.04% of the 
information  contained  in  the  original  dataset)  from  forty-two  variables.  This  selection 
of the data’s critical features reduces the noise and redundancy of the final model and 
improves its interpretation while decreasing the computational costs.

Despite  the  advantages  of  the  Boruta  and  Gini  index  procedures  shown  above, 
the main disadvantage of both procedures is that they do not consider the potential

Fig. 2  The important measure for each variable using Boruta

---

<!-- PAGE 14 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 14 of 30

multicollinearity  problems  that  may  arise  between  the  resulting  explanatory  varia-
bles. Indeed, multicollinearity problems remain understudied in the environment of 
AI and ML algorithms, although it is one of the most important aspects to consider 
in an econometric model (Chan et al. 2022). However, unlike what is often claimed, 
correlation does not necessarily mean multicollinearity as they are not the same, and 
thus multicollinearity problems cannot be analyzed by using the correlation matrix, 
but  by  using  the  Variation  Inflation  Factor  (VIF)  (Chan  et  al.  2022).  The  variable 
PU2 has the maximum VIF value (6.548), which confirms the lack of multicollinear-
ity problems (note that although there is no strict threshold for VIF to confirm the 
presence  of  multicollinearity,  there  is  a  wide  consensus  in  the  previous  research  to 
consider that a VIF of 10 or higher often indicates multicollinearity (Weisberg 2005). 
Additionally, as a robustness check, we also implement the forward stepwise logistic 
regression as a parametric alternative approach to select the most relevant variables. 
Here we obtain only four resulting variables (PU2, SN3, TR5, and PENJ3), of which 
three match those obtained in the Boruta and Gini index procedures (our results, in 
terms of the nonparametric techniques based on ML outperform the classical LDA 
and LR, remain unaltered by applying the Boruta, Gini index, and forward stepwise 
logistic regression).

From  a  theoretical  point  of  view,  FS  analysis  suggests  that  the  variables  correspond-
ing to usefulness, subjective usage norms, trust, and perceived enjoyment have a strong 
influence on the intention to use mobile payment systems and media.

Specifically,  our  results  suggest  that  the  usefulness  of  mobile  payment  media  (PU1, 
PU2, PU3, and PU4) is a strong explanatory factor in their usage intention, which is an 
advance  over  the  previous  literature  (Bhattacherjee  and  Premkumar  2004).  This  pos-
its  the  concept  of  perceived  usefulness  to  understand  changes  in  beliefs  and  attitudes 
toward information technology use.

Second, moving on to personal innovation in the information technology domain, two 
subjective customer profile variables (SN3 and SN4) show high explanatory and predic-
tive power for the intention to use mobile payment methods (Agarwal and Prasad 1998a; 
Taylor and Todd 1995).

Turning to variables related to perceived trust in mobile payment systems, in line with 
Ba  and  Pavlou  (2002),  our  results  identify  a  strong  link  between  bank  customers’  per-
ceived trustworthiness in the mobile payment medium (TR2) and their direct intention 
to use.

Furthermore, our findings represent an advance over the previous literature regarding 
the variable related to the perceived enjoyment of using online payment systems (Agar-
wal and Karahanna 2000; Rouibah et al. 2016), as our results identify a significant rela-
tionship  between  the  perceived  enjoyment  of  using  a  mobile  payment  means  and  the 
intention to continue using this technology (PENJ3). To better illustrate the discrimina-
tory power of the RF model after applying the FS procedure, we present the area under 
the  ROC  curve  (AUC)  in  Fig.  3.  AUC  is  calculated  by  plotting  the  true  positive  rate 
against the false positive rate at various threshold settings. Indeed, AUC can be defined 
as a tradeoff between sensitivity and specificity, given that an increase in sensitivity will 
cause a reduction in specificity. The model will have a greater classification power when 
the curve is closer to the upper left corner. Similarly, Fig. 4 shows the out-of-bag (OOB)

---

<!-- PAGE 15 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 15 of 30

Fig. 3  Area under ROC curve for random forest (AUC)

Fig. 4  The Out‑Of‑Bag (OOB) error for final random forest model

error,  which  can  be  defined  as  the  average  error  using  predictions  from  trees  that  are 
not  contained  in  their  respective  bootstrap  sample.  OOB  is  used  to  fit  the  classifica-
tion  power  of  the  RF  model  while  it  is  being  trained.  As  depicted  in  Fig.  4,  the  OOB

---

<!-- PAGE 16 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 16 of 30

drastically decreases (i.e., the model increases its fitting) after the first 150 trees, oscillat-
ing steadily from them.

Validation measures

The performance of each model is evaluated using different accuracy measurements 
on the results obtained for each method on the out-of-sample. In binary classification 
problems, two relevant metrics arise sensitivity and specificity. On the one hand, sen-
sitivity measures the probability that the model classifies a Bizum user as a real user 
of  Bizum.  In  other  words,  sensitivity  measures  the  model’s  ability  to  detect  Bizum 
usage in its presence. Conversely, specificity measures the probability that the model 
classifies a real Bizum nonuser as a Bizum nonuser. That is, specificity measures the 
ability  of  the  model  to  exclude  the  use  of  Bizum  when  it  is  lacking.  Sensitivity  and 
specificity are defined as follows:

Sensitivity

TP

=

TP

FN ;

+

Speciﬁcity

TN

=

TN

FP

+

where

TP = True  Positive,  the  number  of  positive  cases  (not  adopting  mobile  P2P  pay-

ment) that are correctly identified as positive,

TN = True Negative, the number of negative cases (adopt mobile P2P payment) that

are correctly identified as negative cases,

FN = False Negative, the number of positive cases (not adopt mobile P2P payment)

that are misclassified as negative cases (adopt mobile P2P payment),

FP = False Positive, the number of negative cases (adopt mobile P2P payment) that

are incorrectly identified as positive cases (not adopt mobile P2P payment).

Following  Petropoulos  et  al.  (2020),  we  built  several  performance  measurements 
based on sensitivity and specificity to overcome the limitations of traditional accuracy 
metrics based only on the overall predictive ability. In this vein, we calculate the fol-
lowing measures:

•  G-mean: The geometric mean G-mean is the product of sensitivity and specificity. 
This metric illustrates the balance between the classification performances of the 
majority and minority classes.

G

=

Sensitivity

Speciﬁcity

·

(cid:31)

A  poor  performance  in  predicting  positive  cases  will  lead  to  a  low  G-mean  value, 
even if the negative cases are correctly classified by the algorithm.

•  LR: The negative likelihood ratio is the ratio between the probability of predicting 
a  case  as  negative  when  it  is  positive  and  the  probability  of  predicting  a  case  as 
negative when it is actually negative.

LR

=

1

Sensitivity

−
Speciﬁcity

A lower negative likelihood ratio signifies better performance in negative cases. This 
is the main point of interest in this study as we model bank failures.

---

<!-- PAGE 17 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 17 of 30

•  DP: Discriminant power is a measurement that sums up sensitivity and specificity.

DP

=

√3
π

log

(cid:31)

Sensitivity

1

(cid:30)

−

Sensitivity

+

(cid:29)

log

Speciﬁcity

1

(cid:30)

−

Speciﬁcity

(cid:29)(cid:28)

The algorithm distinguishes between positive and negative cases for DP values greater 
than 3.

•  BA:  Balanced  accuracy  is  the  average  of  Sensitivity  and  Specificity.  If  the  classifier 
performs  equally  well  on  either  class,  this  term  lowers  the  conventional  accuracy 
measure.

BA

=

1
2

(cid:31)

Sensitivity

Speciﬁcity

+

(cid:30)

In contrast, if the conventional accuracy is high simply because the classifier takes advan-
tage of a good prediction on the majority class, the balanced accuracy will decrease, thus 
signaling  any  performance  issues.  That  is,  BA  does  not  disregard  the  accuracy  of  the 
model in the minority class (i.e., adopt Bizum in our case).

•  Youden’s  γ:  Youden’s  index  is  a  linear  transformation  of  the  mean  sensitivity  and

specificity; consequently, it is difficult to interpret.

γ

=

Sensitivity

1

−

−

Speciﬁcity

(cid:30)
As a general rule, a higher value of Youden’s γ signifies a better ability of the algorithm to 
avoid misclassification of the population.

(cid:31)

•  WBA1: A weighted balance accuracy measure that weighs specificity more than sen-

sitivity (75%/25%).

•  WBA2:  A  weighted  balance  accuracy  measure  that  weighs  sensitivity  more  than

specificity (75%/25%).

Alternatively, we also calculate the AUC, which can be defined as the probability that the 
classifier will rank a randomly chosen positive instance higher than a randomly chosen 
negative instance. The value of AUC varies between 0.50 and 1, being accepted by the 
researcher that a value above 0.80 denotes a high performance.

Finally, to facilitate the interpretation of the results, we build a metric, the Global Per-
formance Index (GPI), which summarizes the results of the previous performance meas-
urements.  We  define  GPI  as  the  arithmetic  average  of  all  previous  metrics,  except  for 
Type I and II errors, because they are complementary ratios to specificity and sensitivity. 
Moreover, given that a model obtains a better performance with lower values of LR, this 
metric subtracts in the following expression:

GPI

=

AUC

+

Accuracy ratio

Sensitivity

+

Speciﬁcity

+

+

Gmean
11

−

LR

+

DP

+

BA

+

Youden′s

+

WBA1

WBA2

+

Results

The  final  sample,  after  eliminating  questionnaires  that  were  completed  too  quickly  or 
exceeded the recommended time, amounted to 701 participants, of whom 46.22% were 
male and 53.78% were female. 42.37% were between 18 and 24 years old, 51.21% were

---

<!-- PAGE 18 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 18 of 30

between  25  and  44  years  old,  and  6.28%  were  over  44  years  old.  Of  these,  4.28%  had 
doctoral  studies,  49.93%  had  university  studies,  26.68%  had  secondary  school  studies, 
15.83% had primary school studies, and the remaining 3.28% had no studies at all. The 
number of invalid questionnaires rejected was only 13; thus, the valid response rate was 
98%.

Table 4 summarizes the results in terms of performance metrics in the test set. This 
shows that there is not a unique model that obtains the best performance in terms of all 
metrics. However, our results demonstrate that nonparametric techniques based on ML 
often  outperform  classical  LDA  and  LR.  In  particular,  we  find  that  binomial  boosting, 
MLP4, and L2 boosting are the models that obtain the best performance in terms of GPI. 
Specifically,  binomial  boosting  obtains  the  best  GPI  score  with  a  value  of  0.6859,  fol-
lowed by MLP 4 and L2 boosting, which reach GPIs of 0.6613 and 0.6609, respectively. 
In  contrast,  the  two  models  based  on  classification  trees,  CART  and  CTBag,  obtained 
the worst performance in terms of GPI.

Since the AUC is based on conceptual and methodological foundations different from 
the rest of the metrics, which, as previously argued, are based on specificity and sensi-
tivity (complementary measurements of type I error and type II error, respectively), we 
analyze this metric in more detail. In this sense, our findings show that the methods with 
the highest AUC values are the neuronal network (MLP 1 and MLP 2), followed closely 
by SVM and L2 boosting. In the same way as the GPI, CART, and CTBag are the two 
underperforming methods in terms of AUC.

When comparing the performance of the models built using all the variables for the 
models that apply FS to reduce the dimensionality of the data, our results suggest that 
the performance increases when FS is used. More importantly, we find that the increase 
in the performance of implementing FS remains unaltered for all the methods in terms 
of all the performance metrics.

Discussion
Theoretical implications

Our empirical research has two relevant results. First, related to the classification accu-
racy of methods, our findings suggest that using FS analysis as a preprocessing technique 
substantially  improves  prediction  performance  while  reducing  the  noise  and  redun-
dancy of the resulting model and the computational costs of its implementation due to 
lower data dimensionality. All of this definitively improves the theoretical interpretation 
of the final model and allows analysis of how each independent variable contributes to 
explicating and predicting the use of mobile P2P payments. We also find that there is not 
a unique method that outperforms in terms of all metrics, but it is demonstrated that, 
in general, nonparametric techniques based on ML outperform classical LDA and LR. 
Thus, the results show that binomial boosting, MLP4, and L2 boosting are the models 
that obtain the best performance according to the Global Performance Index (GPI).

Second,  from  a  theoretical  point  of  view,  we  document  that  (in  this  order  of  prior-
ity)  the  usefulness  of  mobile  P2P  payments,  the  influence  of  peers  and  other  social 
groups  such  as  friends,  family,  and  colleagues  on  an  individual’s  behavior  (i.e.,  subjec-
tive norms), and the perceived trust and enjoyment of the user experience in the digital

---

<!-- PAGE 19 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 19 of 30

I

P
G

2
A
B
W

1
A
B
W

ϓ
s
’
n
e
d
u
o
Y

A
B

P
D

‑
R
L

n
a
e
m
G

‑

y
t
i
c
fi
i
c
e
p
S

y
t
i
v
i
t
i
s
n
e
S

r
o
r
r
e
I
I
e
p
y
T

r
o
r
r
e
I
e
p
y
T

y
c
a
r
u
c
c
a
t
s
e
T

C
U
A

l

e
p
m
a
s
‑
f
o
‑
t
u
o
n

i

s
t
l
u
s
e
r
e
c
n
a
m
r
o

f
r
e
P

4
e
l
b
a
T

l

n
o
i
t
c
e
e
s
e
r
u
t
a
e
f

m
o
r
f
g
n
i
t
l
u
s
e
r

l

s
e
b
a
i
r
a
v
t
n
e
d
n
e
p
e
d
n

i

e
h
t
g
n
i
s
u
y
B

.

A

l

e
n
a
P

8
9
5
6
0

.

5
6
4
6
0

.

0
1
6
6
0

.

6
3
5
6
0

.

7
3
5
6
0

.

3
1
6
6
0

.

7
0
6
6
0

.

4
7
2
6
0

.

6
3
1
6
0

.

8
9
5
6
0

.

4
6
5
6
0

.

9
5
8
6
0

.

9
0
6
6
0

.

8
2
3
6
0

.

4
0
5
6
0

.

8
8
5
6
0

.

2
6
6
6
0

.

9
1
8
6
0

.

4
7
8
6
0

.

5
8
6
6
0

.

9
7
2
6
0

.

9
2
8
6
0

.

9
2
8
6
0

.

5
9
7
6
0

.

4
9
7
6
0

.

6
3
9
7
0

.

2
4
7
7
0

.

0
5
8
7
0

.

7
1
8
7
0

.

7
1
8
7
0

.

7
0
8
7
0

.

3
9
8
7
0

.

7
3
8
7
0

.

7
6
5
7
0

.

7
0
8
7
0

.

7
5
8
7
0

.

6
8
7
6
0

.

0
5
8
7
0

.

0
9
5
7
0

.

0
6
8
7
0

.

3
9
8
7
0

.

9
6
9
7
0

.

2
9
9
7
0

.

9
3
9
7
0

.

0
4
8
7
0

.

4
0
5
7
0

.

9
4
9
7
0

.

2
9
9
7
0

.

0
4
5
7
0

.

0
1
7
6
0

.

5
4
6
7
0

.

9
6
6
7
0

.

2
9
7
7
0

.

4
9
6
7
0

.

4
9
6
7
0

.

6
6
8
7
0

.

9
1
7
7
0

.

9
4
3
7
0

.

7
4
3
7
0

.

6
6
8
7
0

.

2
6
7
7
0

.

1
4
8
8
0

.

2
9
7
7
0

.

8
1
6
7
0

.

0
2
6
7
0

.

9
1
7
7
0

.

4
4
7
7
0

.

5
1
0
8
0

.

0
6
2
8
0

.

4
6
9
7
0

.

5
6
7
7
0

.

8
8
0
8
0

.

5
1
0
8
0

.

8
7
4
8
0

.

5
1
8
8
0

.

1
8
5
5
0

.

0
1
4
5
0

.

2
4
6
5
0

.

1
1
5
5
0

.

1
1
5
5
0

.

3
7
6
5
0

.

2
1
6
5
0

.

6
8
1
5
0

.

4
1
9
4
0

.

3
7
6
5
0

.

9
1
6
5
0

.

6
2
6
5
0

.

2
4
6
5
0

.

8
0
2
5
0

.

0
8
4
5
0

.

2
1
6
5
0

.

3
1
7
5
0

.

6
0
0
6
0

.

9
9
1
6
0

.

4
0
8
5
0

.

9
6
2
5
0

.

7
3
0
6
0

.

6
0
0
6
0

.

8
1
0
6
0

.

5
2
5
5
0

.

1
9
7
7
0

.

5
0
7
7
0

.

1
2
8
7
0

.

6
5
7
7
0

.

6
5
7
7
0

.

7
3
8
7
0

.

6
0
8
7
0

.

3
9
5
7
0

.

7
5
4
7
0

.

7
3
8
7
0

.

0
1
8
7
0

.

3
1
8
7
0

.

1
2
8
7
0

.

4
0
6
7
0

.

0
4
7
7
0

.

6
0
8
7
0

.

7
5
8
7
0

.

3
0
0
8
0

.

0
0
1
8
0

.

2
0
9
7
0

.

5
3
6
7
0

.

9
1
0
8
0

.

3
0
0
8
0

.

9
0
0
8
0

.

3
6
7
7
0

.

3
7
0
6
0

.

2
0
8
5
0

.

1
2
1
6
0

.

4
4
9
5
0

.

4
4
9
5
0

.

5
6
1
6
0

.

2
9
0
6
0

.

2
9
5
5
0

.

8
6
1
5
0

.

5
6
1
6
0

.

2
9
0
6
0

.

2
6
0
1
1

.

1
2
1
6
0

.

1
3
5
5
0

.

0
2
9
5
0

.

2
9
0
6
0

.

5
4
2
6
0

.

8
4
6
6
0

.

8
0
0
7
0

.

8
5
3
6
0

.

7
3
6
5
0

.

5
0
7
6
0

.

8
4
6
6
0

.

3
3
2
7
0

.

3
6
9
0
1

.

9
5
5
2
0

.

1
1
9
2
0

.

2
3
7
2
0

.

9
7
7
2
0

.

9
7
7
2
0

.

4
1
8
2
0

.

7
4
6
2
0

.

1
0
7
2
0

.

0
1
2
3
0

.

4
1
8
2
0

.

6
1
7
2
0

.

9
9
2
4
0

.

2
3
7
2
0

.

6
7
1
3
0

.

3
9
6
2
0

.

7
4
6
2
0

.

4
1
5
2
0

.

7
1
5
2
0

.

9
3
6
2
0

.

9
6
7
2
0

.

6
2
3
3
0

.

0
0
6
2
0

.

7
1
5
2
0

.

4
7
2
3
0

.

1
0
4
4
0

.

4
6
7
6
0

.

3
7
8
7
0

.

3
6
0
8
0

.

6
3
9
5
0

.

8
6
9
7
0

.

3
6
5
6
0

.

4
2
7
2
0

.

5
8
7
7
0

.

5
0
7
7
0

.

1
2
8
7
0

.

5
5
7
7
0

.

5
5
7
7
0

.

6
3
8
7
0

.

4
0
8
7
0

.

7
7
5
7
0

.

4
5
4
7
0

.

6
3
8
7
0

.

9
0
8
7
0

.

8
3
5
7
0

.

1
2
8
7
0

.

4
0
6
7
0

.

6
3
7
7
0

.

4
0
8
7
0

.

3
5
8
7
0

.

3
0
0
8
0

.

3
9
0
8
0

.

1
0
9
7
0

.

0
3
6
7
0

.

7
1
0
8
0

.

3
0
0
8
0

.

4
5
9
7
0

.

1
7
4
7
0

.

6
6
9
7
0

.

0
0
5
7
0

.

2
3
6
7
0

.

3
6
7
7
0

.

2
3
6
7
0

.

2
3
6
7
0

.

5
9
8
7
0

.

2
3
6
7
0

.

5
0
1
7
0

.

7
3
2
7
0

.

5
9
8
7
0

.

4
1
7
7
0

.

8
6
8
9
0

.

3
6
7
7
0

.

2
3
6
7
0

.

0
0
5
7
0

.

2
3
6
7
0

.

2
3
6
7
0

.

6
2
0
8
0

.

1
2
4
8
0

.

6
2
0
8
0

.

5
9
8
7
0

.

8
5
1
8
0

.

6
2
0
8
0

.

7
4
9
8
0

.

8
6
8
9
0

.

8
5
1
8
0

.

1
8
0
8
0

.

8
7
7
7
0

.

9
7
8
7
0

.

9
7
8
7
0

.

9
7
8
7
0

.

8
7
7
7
0

.

0
8
9
7
0

.

1
8
0
8
0

.

7
7
6
7
0

.

8
7
7
7
0

.

5
0
9
7
0

.

8
5
7
5
0

.

9
7
8
7
0

.

6
7
5
7
0

.

0
8
9
7
0

.

0
8
9
7
0

.

1
8
0
8
0

.

0
8
9
7
0

.

8
7
7
7
0

.

8
7
7
7
0

.

4
7
3
7
0

.

9
7
8
7
0

.

0
8
9
7
0

.

1
7
0
7
0

.

7
5
6
5
0

.

8
7
7
7
0

.

9
1
9
1
0

.

2
2
2
2
0

.

1
2
1
2
0

.

1
2
1
2
0

.

1
2
1
2
0

.

2
2
2
2
0

.

0
2
0
2
0

.

9
1
9
1
0

.

3
2
3
2
0

.

2
2
2
2
0

.

5
9
0
2
0

.

2
4
2
4
0

.

1
2
1
2
0

.

4
2
4
2
0

.

0
2
0
2
0

.

0
2
0
2
0

.

9
1
9
1
0

.

0
2
0
2
0

.

2
2
2
2
0

.

2
2
2
2
0

.

6
2
6
2
0

.

1
2
1
2
0

.

0
2
0
2
0

.

9
2
9
2
0

.

3
4
3
4
0

.

2
2
2
2
0

.

0
0
5
2
0

.

8
6
3
2
0

.

7
3
2
2
0

.

8
6
3
2
0

.

8
6
3
2
0

.

5
0
1
2
0

.

8
6
3
2
0

.

5
9
8
2
0

.

3
6
7
2
0

.

5
0
1
2
0

.

6
8
2
2
0

.

2
3
1
0
0

.

7
3
2
2
0

.

8
6
3
2
0

.

0
0
5
2
0

.

8
6
3
2
0

.

8
6
3
2
0

.

4
7
9
1
0

.

9
7
5
1
0

.

4
7
9
1
0

.

5
0
1
2
0

.

2
4
8
1
0

.

4
7
9
1
0

.

3
5
0
1
0

.

2
3
1
0
0

.

2
4
8
1
0

.

9
2
8
7
0

.

4
1
7
7
0

.

9
2
8
7
0

.

1
7
7
7
0

.

1
7
7
7
0

.

9
2
8
7
0

.

9
2
8
7
0

.

7
5
6
7
0

.

6
8
4
7
0

.

9
2
8
7
0

.

9
2
8
7
0

.

3
4
5
7
0

.

9
2
8
7
0

.

1
1
9
8
0

.

0
7
8
8
0

.

5
2
9
8
0

.

7
1
9
8
0

.

9
2
9
8
0

.

4
7
8
8
0

.

7
5
9
8
0

.

2
4
7
7
0

.

5
0
4
8
0

.

2
0
7
8
0

.

0
2
5
8
0

.

4
1
9
8
0

.

7
1
9
8
0

.

A
D
L

R
L

1
P
L
M

2
P
L
M

3
P
L
M

4
P
L
M

M
V
S

T
R
A
C

t
s
o
o
B
a
d
A

g
a
B
T
C

F
R

g
n
i
t
s
o
o
B

l

i

a
m
o
n
B

i

g
n
i
t
s
o
o
B
2
L

l

s
e
b
a
i
r
a
v
t
n
e
d
n
e
p
e
d
n

i

e
h
t

l
l

a
g
n
i
s
u
y
B

.

B

l

e
n
a
P

0
0
6
7
0

.

1
7
7
7
0

.

9
2
8
7
0

.

6
8
8
7
0

.

0
0
0
8
0

.

7
5
0
8
0

.

6
8
8
7
0

.

0
0
6
7
0

.

0
0
0
8
0

.

0
0
0
8
0

.

6
8
8
7
0

.

6
8
4
7
0

.

3
4
9
7
0

.

6
2
8
8
0

.

5
3
6
8
0

.

3
5
7
8
0

.

4
1
8
8
0

.

3
5
8
8
0

.

8
9
3
8
0

.

6
4
8
8
0

.

8
8
0
8
0

.

0
7
8
8
0

.

9
6
9
8
0

.

8
7
8
8
0

.

8
7
8
8
0

.

9
7
8
8
0

.

A
D
L

R
L

1
P
L
M

2
P
L
M

3
P
L
M

4
P
L
M

M
V
S

T
R
A
C

t
s
o
o
B
a
d
A

g
a
B
T
C

F
R

g
n
i
t
s
o
o
B

l

i

a
m
o
n
B

i

g
n
i
t
s
o
o
B
2
L

---

<!-- PAGE 20 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 20 of 30

context are the attributes that classify the (potential) users of mobile P2P payments with 
greater ability.

The major importance of usefulness in the intention to use this P2P payment service 
may be mainly based on the number of current users (approximately half of the popu-
lation of Spain). This networking effect is crucial to the success of the service because 
the  application  must  be  used  by  both  the  sender  and  receiver.  In  addition,  adequate 
resources or support are essential for users to perceive the usefulness of the service and 
even directly influence the intention of use. Subjective Norms, as the following signifi-
cant factor on the intention to use the service, show that the information that users share 
about their experience when using the P2P payment service influences the intention of 
other users due to the social requirements of these services. This fact is highly relevant 
for  those  companies  that  provide  these  payment  services  since  their  plans  of  action 
should focus on developing word-of-mouth strategies and attempting to encourage cur-
rent  clients  to  directly  recommend  the  service.  Our  results  also  show  that  perceived 
trust and enjoyment significantly affect the intention to use P2P payment services. This 
finding implies that service providers corroborate the need to develop P2P payment ser-
vices that may be easy to use, secure, and attractive to consumers.

The future landscape of the payment sector will be promising for financial entities and 
FinTech organizations that are open to change, innovation, and forward-thinking. These 
players  need  to  rapidly  accelerate  their  transformation  efforts  to  address  unmet  cus-
tomer demands and plug the gaps. In this vein, our findings are novel and useful for both 
traditional  and  new  financial  intermediaries,  businesses,  customers,  and  other  stake-
holders  that  are  part  of  financial  systems,  such  as  policymakers  and  regulators.  More 
importantly,  our  findings  could  be  of  interest  to  financial  institutions  to  define  ad  hoc 
financial services customized for their target market.

From a theoretical perspective, our results support the necessity of implementing sta-
tistical procedures to reduce the complexity of the data. Boruta and Gini algorithms are 
preferable methods because both are based on the nonlinearity performed by Random 
Forest, one of the most advanced current ML methods.

Practical implications

From a managerial standpoint, our research findings provide valuable insights for service 
providers in the mobile P2P payments industry. To effectively promote the adoption and 
usage of their platforms, providers must prioritize enhancing usability and user experi-
ence. This can be achieved by streamlining the payment process, simplifying user inter-
faces, and ensuring smooth and intuitive navigation. By focusing on subjective norms, 
providers can tap into the power of social influence, leveraging the positive perceptions 
and recommendations of existing users to attract new users. Implementing strategies to 
encourage word-of-mouth marketing, such as referral programs or incentives for users 
who refer others to the service, can be an effective approach to expanding user adoption.
Building  trust  is  another  critical  aspect  of  driving  the  adoption  of  mobile  P2P  pay-
ments.  Service  providers  should  prioritize  security  measures  and  communicate  them 
transparently to users. Highlighting the safety of transactions, data protection protocols, 
and robust authentication methods can help alleviate concerns and increase users’ trust 
in  the  platform.  In  addition,  incorporating  features  that  enhance  user  enjoyment  and

---

<!-- PAGE 21 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 21 of 30

engagement,  such  as  personalized  experiences,  rewards,  or  gamification  elements,  can 
contribute to positive user perception and encourage continued usage.

Beyond  the  immediate  managerial  implications,  our  research  findings  have  broader 
societal  and  economic  implications.  Promoting  the  adoption  of  mobile  P2P  payments 
can contribute to financial inclusion, particularly for marginalized populations, such as 
the young, the unemployed, and those with limited access to traditional banking services 
in  rural  areas.  By  providing  these  individuals  with  convenient  and  accessible  payment 
solutions, barriers to financial participation can be reduced, enabling them to engage in 
economic activities, make transactions, and manage their finances more effectively. This, 
in turn, can lead to increased economic empowerment, poverty reduction, and overall 
societal development.

Furthermore, from a macroeconomic perspective, higher adoption of mobile P2P pay-
ments can lead to increased financial stability. By reducing the reliance on cash transac-
tions and expanding digital payment options, the risks associated with handling physical 
currency, such as theft or counterfeiting, can be mitigated. Additionally, the digitization 
of  payments  enables  better  tracking  and  monitoring  of  financial  flows,  contributing  to 
enhanced  transparency  and  accountability  within  the  financial  system.  This  improved 
oversight  can  help  prevent  illicit  activities,  such  as  money  laundering  and  tax  evasion 
while facilitating more efficient financial regulations and policy implementations.

In conclusion, the implications of our research emphasize the importance of prioritiz-
ing usability, trust, and enjoyment in mobile P2P payment services. By addressing these 
factors and promoting the adoption of mobile P2P payments, service providers can not 
only  drive  their  business  success  but  also  contribute  to  financial  inclusion,  economic 
development, and financial stability at both the individual and societal levels.

Limitations and avenues for future research

Despite the valuable insights gained from this study, it is important to acknowledge its 
limitations, which open up avenues for future research. First, enhancing the dataset by 
incorporating additional information, such as users’ training in new technologies, edu-
cational background, and risk aversion, would provide valuable control and moderating 
variables to deepen our understanding of the factors influencing the use of mobile P2P 
payments.  This  could  shed  light  on  how  these  individual  characteristics  interact  with 
other factors and impact adoption.

Second, obtaining data on the average size of digital payment transactions would allow 
for an analysis of how users’ risk aversion influences their adoption of mobile P2P pay-
ments.  Examining  whether  risk-averse  individuals  are  more  or  less  likely  to  engage  in 
larger transactions through these payment methods could provide valuable insights into 
the relationship between risk perception and usage behavior.

Third,  replicating  this  study  by  surveying  individuals  from  different  countries  would 
enable an analysis of the effects of institutional frameworks on the adoption of mobile 
P2P  payments.  Comparing  adoption  patterns  across  countries  with  varying  regulatory 
environments and financial infrastructures could reveal the influence of these contextual 
factors on user behavior.

Finally,  it  is  important  to  address  the  limitations  associated  with  the  sample  selec-
tion process, specifically the use of a nonprobability snowball sampling method. Future

---

<!-- PAGE 22 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 22 of 30

research  should  consider  employing  alternative  sampling  techniques,  such  as  simple 
random  sampling  or  quota  sampling,  to  ensure  a  more  representative  and  generaliza-
ble sample. This would enhance the external validity of the findings and provide a more 
comprehensive understanding of the factors influencing mobile P2P payment adoption 
across diverse populations.

By addressing these limitations and pursuing further research in these areas, we can 
gain a more nuanced understanding of the adoption and usage of mobile P2P payments, 
leading to more effective strategies for service providers and policymakers in driving the 
growth and acceptance of these payment methods. Another limitation of ML is that it 
includes suitable choices from manifold implementation options, bias and drift in data, 
and the mitigation of black-box properties.

Conclusion

In the current era of increasing digitalization and massive use of FinTech services, digi-
tal P2P payments are being strongly extended as the preferred payment option, mainly 
among the young. The rise in P2P payments has been enhanced by the explosion of sure 
mobile  payment  applications  as  well  as  the  COVID-19  pandemic,  which  has  dramati-
cally limited cash payments to prevent transmission of the virus. Of course, the need to 
align  individuals´  behaviors  with  the  Sustainable  Development  Goals  also  requires  the 
boosting  of  digital  P2P  payments  as  a  way  to  increase  the  financial  inclusion  of  many 
individuals  excluded  from  traditional  financial  banking  services  (Danisman  and  Tarazi 
2020). Indeed, banks and other financial players are currently playing a relevant role in 
developing innovative payment services where P2P payments are becoming widespread. 
Thus, it is crucial to examine the factors that determine customers’ adoption of mobile 
P2P payments to exploit their potential.

This study explores the drivers of mobile P2P adoption by using ML to predict usage 
among FinTech disruptions in financial services. Our main conclusion is that ML must 
be applied by banks and other financial intermediaries to predict their customers’ adop-
tion of mobile/digital P2P payments. Indeed, to the authors’ knowledge, this approach 
has not yet been employed in this field of research. In addition, our findings emphasize 
the  relevance  of  usefulness,  subjective  norms,  trust,  and  user  enjoyment  in  classifying 
potential mobile P2P users.

Appendix 1: constructs and measurement items

Perceived ease of use (Venkatesh and Bala 2008)

•  Interaction with the system does not require great effort.
•  Interaction with the system is straightforward.
•  It’s easy to get the system to do what I want.
•  The system is useful for making small payments.
•  In general, the system is easy to use.

---

<!-- PAGE 23 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 23 of 30

Perceived risk of peer-to-peer mobile payment system (Jarvenpaa et  al. 2000; Wake-

field and Whitten 2006)

•  Other people can get information about my online transactions if I use this tool.
•  There  is  a  high  potential  for  money  wasted  if  I  make  purchases  on  the  internet/

social networks using this tool.

•  There is significant risk in making purchases on the internet/social networks using

this tool.

•  I think that making purchases on the internet/social networks with this tool is a

risky choice.

Perceived  usefulness  of  peer-to-peer  mobile  payment  systems  (Bhattacherjee  and

Premkumar 2004)

•  Peer-to-peer mobile payment systems are useful payment methods.
•  Using peer-to-peer mobile payment systems makes it easier to handle payments.
•  Peer-to-peer mobile payment systems allow quick use of mobile applications.
•  In general, peer-to-peer mobile payment systems could be useful for me.

Perceived trust of peer-to-peer mobile payment system (Pavlou 2002)

•  I believe the peer-to-peer mobile payment system will keep its promises and com-

mitments.

•  The peer-to-peer mobile payment system is trustworthy.
•  I would describe peer-to-peer mobile payment system as honest.
•  I believe the peer-to-peer mobile payment system is responsible.
•  In general, I trust the peer-to-peer mobile payment system.

Personal  innovativeness  in  information  technology  (Agarwal  and  Prasad  1998a;

Ramos-de-Luna et al. 2016)

•  If I find out about new information technology, I seek ways to experience it.
•  I am usually one of the first among my colleagues/peers to explore new informa-

tion technology.

•  In general, I am reluctant to try new information technologies.
•  I like to try new information technologies.

Subjective norms (Taylor and Todd 1995; Agarwal and Prasad 1998b)

•  The  people  whose  opinions  I  value  would  approve  of  me  using  peer-to-peer

mobile payment system.

•  Most of the people I have in mind think that I should use a peer-to-peer mobile

payment system.

•  They expect me to use a peer-to-peer mobile payment system.
•  The  people  who  are  close  to  me  would  agree  with  me  in  using  a  peer-to-peer

mobile payment system.

---

<!-- PAGE 24 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 24 of 30

Perceived  enjoyment  of  the  peer-to-peer  mobile  payment  system  (Agarwal  and

Karahanna 2000; Rouibah et al. 2016)

•  I have fun interacting with this peer-to-peer mobile payment system.
•  Using this peer-to-peer mobile payment system provides me with a lot of enjoyment.
•  I enjoy using this peer-to-peer mobile payment system.

Loyalty to the bank brand (Gözükara and Çolakoğlu 2016)

•  I will not buy other brands if this brand is available at the store.
•  I consider myself loyal to this brand.
•  This brand would be my first choice.
•  I rarely switch from this brand just to try something different.

Perceived quality (Lai et al. 2007)

•  When peer-to-peer mobile payment systems promise they will do something, they

do.

•  I consider peer-to-peer mobile payment systems to be dependable.
•  Peer-to-peer mobile payment systems provide the services they promise when they

are supposed to.

•  Peer-to-peer mobile payment systems accurately maintain the statement.
•  It is easy to obtain related service information.
•  It feels safe to do business with the company.
•  The statement is clear and ease to understand.

Appendix 2: criteria for the implementation of algorithms
Linear and quadratic discriminant analysis

We  select  the  threshold  pc  in  the  grill  (0.01,  0.02,  …,  0.99),  choosing  that  value  which 
minimises  the  classification  error  in  a  tenfold  cross-validation.  We  obtained  the  value 
0.42.  LDA  was  fitted  with  R  function  lda  (Venables  and  Ripley  2002)  available  in  the 
MASS library.

Additionally,  we  also  compute  the  quadratic  discrimination  analysis  (QDA)  that 
assumes  that  the  covariance  matrices  are  not  equal.  For  this,  we  use  the  function  qda 
from the MASS library (Venables and Ripley 2002). In this case, the cut point obtained 
was 0.43.

Logistic regression

We  use  the  step.glm  function  in  R  (Venables  and  Ripley  2002),  which  strives  to  com-
pute the maximum likelihood estimators of the n + 1 parameters by means of an iterative 
weighted  least  squares  (IWLS)  algorithm,  applied  under  a  forward  sequential  method 
based on the Akaike Information Criterion (AIC). The optimal cut-off is searched for in 
the grid (0.01, 0.02, …, 0.99), selecting the value minimising the tenfold validation error, 
obtaining 0.46.

---

<!-- PAGE 25 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 25 of 30

Multilayer perceptron

The size of the hidden layer (H) and the decay parameter (k) are fitted by implementing a 
tenfold cross-validation optimisation in a grid defined as {1, 2, …, 40} and {0, 0.01, 0.05, 
0.10, …, 2}, respectively. Accordingly, the output of an MLP from a vector of inputs given 
by

can be calculated by the following expression:

x1, . . . , xp

(cid:31)

(cid:30)
W0 +

g

y
ˆ

=



H

p

Whg



v0h +

�h
1
=



�j
1
=

vihxj

1, 2, 3, . . . , H


vih, i


0, 1, 2, . . . , p, h

where 
tions between the p-sized input and the hidden layer, and 
synaptic weights for the connections between the hidden nodes and the output node.


  is  the  synaptic  weights  for  the  connec-
 is the

0, 1, 2, . . . , H

vh, h

=

=

=

(cid:31)

(cid:30)

(cid:31)

(cid:30)

We  use  the  function  nnet  from  R  (Venables  and  Ripley  2002),  which  employs  the 
Broyden–Fletcher–Goldfarb–Shanno  (BFGS)  pathway,  a  quasi-Newton  procedure  that 
seeks to minimise an error criterion which allows a decay term k intending to avoid over-
fitting problems. As shown by Hastie et al. (2009), for classification problems an appro-
priate error function is conditional maximum likelihood (or entropy), that together with 
the BFGS procedure solves the problem defined as:

min
W

n

i
(cid:31)i
=

where Wi(i

=

yiln

yi
ˆ

+

1

−

yi

ln

1

yi
− ˆ

k

+

(cid:30)

(cid:30)
1, . . . , M) is the be the vector of all the M coefficients of the net.

(cid:29)(cid:29)

(cid:29)

(cid:30)

M

W 2
i

(cid:28)

i
(cid:31)i
=

(cid:27)

Support vector machine

Mathematically, SVM can be defined by n training vectors {(Xi,yi)}, i = 1,2,...,n, where the 
multi-dimensional vectors Xi contain the predictor features and the n labels yi
1, 1
} 
identify  the  class  of  each  vector.  In  accordance  with  Meyer  (2012),  we  use  Radial 
Basis Gaussian function kernel function from the library e1071 (Dimitriadou et al. 2022):

∈ {−

(u, v)

K

=

=

θ

u
|

−

−

2

v

|

exp

(cid:31)

(cid:30)

where  the  quadratic  programming  problem  is  solved  implementing  the  following 
procedure:

min
w,b,δ

1
2

wt w

C

+

n

δi

yi
δi

wt ω(Xi)
0, i

=

(cid:30)
≥

(cid:31)i
1
=
≥

b
1
+
1, 2, . . . , n
(cid:29)

δi

−

Given  that  the  selection  of  the  parameters  C  and  θ  impact  powerfully  on  the  per-
formance  of  the  model,  we  apply  a  grid  search  through  the  tenfold  cross-validation 
approach in the set {1, 10, 20, 30, 40, …, 1000} and {0.10, 0.15, 0.20, …, 0.90}, respectively, 
by using the function tune.svm in the library e1071.

---

<!-- PAGE 26 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 26 of 30

Classification trees

We employ the rpart package to build CART, which uses the Gini index as an impurity 
measure  to  split  the  dataset.  To  avoid  the  overfitting  problem  and  in  accordance  with 
Maindonald and Braun (2003), we apply the one-standard-deviation rule to determine 
the number of terminal nodes.

Bagging

We aggregate the B models by majority voting. To compute bagged tree models (CTBag) 
we use the package ipred (Peters and Hothorn 2016). To do so, we consider two values 
for B, 50 and 100, selecting the one minimising the tenfold cross-validation classification 
error.

Random forest

To implement this ensemble method, we use the package randomForest (Liaw and Wie-
ner 2022). The number of variables were randomly selected through a tenfold cross-vali-
dation search around the default value (mtry = square root of the number of predictors), 
namely from mtry − 3 to mtry + 3.

Boosting

AdaBoost, Binominal Boosting, and L2 Boosting were performed by using the function 
glmboost,  mboost  library  (Hothorn  et  al.  2022).  To  fit  the  number  of  iterations  (m)  of 
each  model  we  perform  a  tenfold  cross-validation  search  of  the  value  minimising  the 
empirical loss, from 1 to 3000.

This library considers the problem of estimating a real-valued function:

f ∗(

)

·

=

argf (

·

) min E

ρ

Y , f (X)

(cid:30)
where ρ is a loss function. We assume n training vectors 
ing selected a base procedure, the generic functional gradient descent algorithm is:
(cid:31)

, i
(cid:30)

1, 2, . . . , n, and hav-

Xi, yi

(cid:29)(cid:28)

=

(cid:31)

) with an offset value. Set m

0.

=

1.  Initialise  ˆf [0](
·
2.  Increase m by 1. Evaluate at  ˆf [m
∂
∂f

= ˆf [m

= −

Y , f

Ui

ρ

f

−

1](Xi), i

=

1, . . . , n

(cid:31)

(cid:30)(cid:29)
(cid:29)
(cid:29)

).

3.  Fit the base procedure to predict {

ing  ˆ

g [m](
4.  Update  ˆf [m](
5.  Iterate steps 2–4 until some stopping value M.

= ˆf [m

g [m](
ˆ

1](

+

=

).

−

v

)

)

·

·

·

·

Ui, i

1, . . . , n

1](Xi) the negative gradient of the loss function:

−

Xi, −
} from 
(cid:31)

i

=

1, . . . , n

, obtain-

(cid:30)

=

We  use  m

1  since,  as  shown  Bühlman  and  Hothorn  (2007),  a  small  value  for  the 
step-length factor does not affect the stability of the model. According to Bühlman and 
Hothorn (2007), we use three main methods of boosting procedures to select other ele-
ments of this algorithm. All of them share the base procedure: select the best variable

---

<!-- PAGE 27 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 27 of 30

in  a simple  linear  model in the sense of ordinary least squares fitting. The final model 
ˆf [m](

) is a linear combination of the input variables.

·

Abbreviations:
P2P 
LDA 
LR 
IWLS 
AIC 
MLP 
SVM 
CART  
CTBag 
RF 
FS 
AUC  
OOB 
GPI 
SDG

Peer‑to‑peer
 Linear discriminant analysis
 Logistic regression
 Iterative weighted least squares
 Akaike information criterion
 Multilayer perceptron
 Support vector machine
 Classification and regression tree
 Bagged tree model
 Random forests
 Feature selection
 Area under the ROC curve
 Out‑of‑bag
 Global performance index
 Sustainable development goals

Acknowledgements
Not applicable.

Author contributions
ABO: data collecting, methodology, and implementation of algorithms. JLR: conceptualization and original draft. AID: 
writing and editing. FLC: conceptualization, theoretical framework and positioned our research. All authors read and 
approved the final manuscript.

Funding
Not applicable.

Availability of data and materials
The datasets used and analysed during the current study are available from the corresponding author on reasonable 
request.

Declarations

Competing interests
The authors declare that they have no competing interests.

Received: 24 January 2023   Accepted: 2 February 2024

References
Abdullah S, Naved Khan M (2021) Determining mobile payment adoption: a systematic literature search and bibliometric

analysis. Cogent Bus Manag 8(1):1893245

Acker A, Murthy D (2020) What is Venmo? A descriptive analysis of social features in the mobile payment platform. Telem

Inform 52:101429

Agarwal R, Karahanna E (2000) Time flies when you’re having fun: cognitive absorption and beliefs about information

technology usage. MIS Q 24(4):665–694

Agarwal R, Prasad J (1998a) A conceptual and operational definition of personal innovativeness in the domain of infor‑

mation technology. Inf Syst Res 9(2):204–215

Agarwal R, Prasad J (1998b) The antecedents and consequents of user perceptions in information technology adoption.

Decis Support Syst 22(1):15–29

Ajzen I (1991) The theory of planned behaviour. Organ Behav Hum Decis Process 50:179–211
Alonso Robisco A, Carbó Martínez JM (2022) Measuring the model risk‑adjusted performance of machine learning algo‑

rithms in credit default prediction. Financ Innov 8:70. https:// doi. org/ 10. 1186/ s40854‑ 022‑ 00366‑1

Arora N, Kaur PD (2020) A Bolasso based consistent feature selection enabled random forest classification algorithm: an

application to credit risk assessment. Appl Soft Comput 86:105936. https:// doi. org/ 10. 1016/j. asoc. 2019. 105936

Aslam F, Awan TM, Fatima T (2022) Classification of m‑payment users’ behavior using machine learning models. J Financ

Serv Mark 27:264–275. https:// doi. org/ 10. 1057/ s41264‑ 021‑ 00114‑z

Ba S, Pavlou P (2002) Evidence of trust building technology in electronic markets: price premiums and buyer behavior.

MIS Q 26:243–268. https:// doi. org/ 10. 2307/ 41323 32

Bailey AA, Bonifield CM, Arias A, Villegas J (2022) Mobile payment adoption in Latin America. J Serv Mark 36(8):1058–1075
Bajari P, Nekipelov D, Ryan SP, Yang M (2015) Machine learning methods for demand estimation. Am Econ Rev

105(5):481–485

---

<!-- PAGE 28 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 28 of 30

Belanche D, Guinalíu M, Albás P (2022) Customer adoption of P2P mobile payment systems: the role of perceived risk.

Telemat Inform 72:101851. https:// doi. org/ 10. 1016/j. tele. 2022. 101851

Bhattacherjee A, Premkumar G (2004) Understanding changes in belief and attitude toward information technology

usage: a theoretical model and longitudinal test. MIS Q 28(2):229–254
Bishop CM (2006) Pattern recognition and machine learning. Springer, Berlin
Bizum (2022) https:// bizum. es/ datos/. Accessed 21 Mar 2022
Boulesteix AL, Janitza S, Hapfelmeier A, Van Steen K, Strobl C (2015) Letter to the editor: on the term “interaction” and

related phrases in the literature on random forests. Brief Bioinform 16(2):338–345

Breiman L (1996) Bagging predictors. Mach Learn 24:123–140. https:// doi. org/ 10. 1007/ BF000 58655
Breiman L (2001) Random forests. Mach Learn 45(1):5–32
Bühlman P, Hothorn T (2007) Boosting algorithms: regularization, prediction and model fitting. Stat Sci 22:477–505
Cao L, Philip SY, Kumar V (2015) Nonoccurring behavior analytics: a new area. IEEE Intell Syst 30(6):4–11
Chan JY, Leow SM, Bea KT, Cheng WK, Phoong SW, Hong ZW, Chen YL (2022) Mitigating the multicollinearity problem 
and its machine learning approach: a review. Mathematics 10(8):1283. https:// doi. org/ 10. 3390/ math1 00812 83
Chen RC, Dewi C, Huang SW, Caraka RE (2020) Selecting critical features for data classification based on machine learning

methods. J Big Data. https:// doi. org/ 10. 1186/ s40537‑ 020‑ 00327‑4

Cui G, Wong ML, Lui HK (2016) Machine learning for direct marketing response models: Bayesian networks with evolu‑

tionary programming. Manag Sci 52(4):597–612

Dahlberg T, Mallat N, Ondrus J, Zmijewska A (2008) Past, present and future of mobile payments research: a literature

review. Electron Commer Res Appl 7(2):165–181

Danisman GO, Tarazi A (2020) Financial inclusion and bank stability: evidence from Europe. Eur J Finance 26(18):1842–

1855. https:// doi. org/ 10. 1080/ 13518 47X. 2020. 17829 58

Davenport T, Guha A, Grewal D, Bressgott T (2020) How artificial intelligence will change the future of marketing. J Acad

Mark Sci 48(1):24–42. https:// doi. org/ 10. 1007/ s11747‑ 019‑ 00696‑0

Davis FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Q

13:319–340

Davis FD, Bagozzi RP, Warshaw PR (1989) User acceptance of computer technology: a comparison of two theoretical

models. Manag Sci 35(8):982–1003

Dennehy D, Sammon D (2015) Trends in mobile payments research: a literature review. J Innov Manag 3(1):49–61
Dewi C (2019) Random forest and support vector machine on features selection for regression analysis. Int J Innov Com‑

put Inf Control 15(6):2027–2037

Dimitriadou E, Hornik K, Leisch F, Meyer D, Weingessel D (2022) e1071: misc functions of the department of statistics

(e1071) TU Wien. R package version 1.6. https:// cran.r‑ proje ct. org/ web/ packa ges/ e1071/ index. html

European Central Bank (2022) Estadísticas sobre pagos: 2021. www. bce. es
Fahimifar S, Mousavi K, Mozaffari F, Ausloos M (2022) Identification of the most important external features of highly cited 
scholarly papers through 3 (i.e., Ridge, Lasso, and Boruta) feature selection data mining methods. Qual Quant. 
https:// doi. org/ 10. 1007/ s11135‑ 022‑ 01480‑z

Fishbein M, Ajzen I (1975) Belief attitude, intention, and behavior: an introduction to theory and research. Reading,

Addison‑Wesley, M.A.

Fishbein M, Ajzen I (1977) Belief, attitude, intention and behavior: an introduction to theory and research. Philos Rhetor

10(2):130–132

Flavián C, Guinaliu M, Lu Y (2020) Mobile payments adoption–introducing mindfulness to better understand consumer

behavior. Int J Bank Mark 38(7):1575–1599

Frame WS, Wall LD, White LJ (2018) Technological change and financial innovation in banking: some implications for

fintech. FRB Atlanta, working paper no. 2018‑11

Freund Y (1995) Boosting a weak learning algorithm by majority. Inf Comput 121(2):256–285
Friedman J, Hastie T, Tibshirani R (2000) Additive logistic regression: a statistical view of boosting (with discussion). Ann

Stat 28:337–407

Gomber P, Koch JA, Siering M (2017) Digital finance and FinTech: current research and future research directions. J Bus

Econ 87:537–580. https:// doi. org/ 10. 1007/ s11573‑ 017‑ 0852‑x

Gefen D, Karahanna E, Straub DW (2003) Trust and TAM in online shopping: an integrated model. MIS Quart 27(1):51–90
Gözükara İ, Çolakoğlu N (2016) A research on generation Y students: brand innovation, brand trust and brand loyalty. Int

J Bus Manag Econ Res 7(2):603–611

Guo M, Zhang Q, Liao X, Chen FY, Zeng DD (2021) A hybrid machine learning framework for analyzing human decision‑
making through learning preferences. Omega 101:102263. https:// doi. org/ 10. 1016/j. omega. 2020. 102263
Hagenauer J, Helbich MA (2017) Comparative study of machine learning classifiers for modeling travel mode choice.

Expert Syst Appl 78:273–282

Hastie T, Tibshirani R, Friedman J (2009) The elements of statistical learning: data mining, inference, and prediction.

Springer, New York

Hernández‑Murillo R, Llobet G, Fuentes R (2010) Strategic online banking adoption. J Bank Finance 34(7):1650–1663
Higueras‑Castillo E, Liébana‑Cabanillas FJ, Villarejo‑Ramos ÁF (2023) Intention to use e‑commerce vs physical shopping.

Difference between consumers in the post‑COVID era. J Bus Res 157:113622

Hothorn T, Bühlmann P, Kneib T, Schmid M, Hofner B (2022) mboost: model‑based boosting. R package version 2.1‑2.

https:// cran.r‑ proje ct. org/ web/ packa ges/ mboost/ mboost. pdf

Huang Y (2021) Retail fintech payments: facts, benefits, challenges, and policies
Huang D, Liu X, Lai D, Li Z (2019) Users and non‑users of P2P accommodation: differences in perceived risks and behavio‑

ral intentions. J Hosp Tour Technol 10(3):369–382

Insider Intelligence (2022) The payment industry’s biggest trends in 2022—and the pandemic’s impact on digitization in

the payments landscape. https:// www. busin essin sider. com/ payme nts‑ ecosy stem‑ report. Accessed 21 Mar 2022

Irimia‑Diéguez A, Velicia‑Martín F, Aguayo‑Camacho M (2023) Predicting Fintech innovation adoption: the mediator role

of social norms and attitudes. Financ Innov. https:// doi. org/ 10. 1186/ s40854‑ 022‑ 00434‑6

---

<!-- PAGE 29 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 29 of 30

Jarvenpaa SL, Tractinsky N, Vitale M (2000) Consumer trust in an internet store information technology and management.

J Inf Syst 12(1):41–48

Jun J, Cho I, Park H (2018) Factors influencing continued use of mobile easy payment service: an empirical investigation.

Total Qual Manag Bus Excell 29(9–10):1043–1057

Kalinic Z, Marinkovic V, Molinillo S, Liébana‑Cabanillas F (2019) A multi‑analytical approach to peer‑topeer mobile pay‑
ment acceptance prediction. J Retail Consum Serv 49:143–153. https:// doi. org/ 10. 1016/j. jretc onser. 2019. 03. 016
Kaplan A, Haenlein M (2019) Siri, Siri, in my hand: Who’s the fairest in the land? On the interpretations, illustrations, and 
implications of artificial intelligence. Bus Horiz 62(1):15–25. https:// doi. org/ 10. 1016/j. bushor. 2018. 08. 004
Kou G, Olgu Akdeniz Ö, Dinçer H, Yüksel S (2021) Fintech investments in European banks: a hybrid IT2 fuzzy multidimen‑

sional decision‑making approach. Financ Innov 7(1):1–28

Lai F, Hutchinson J, Li D, Bai C (2007) An empirical assessment and application of SERVQUAL in mainland China’s mobile

communications industry. Int J Qual Reliab Manag 24(3):244–262

LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521:436–444. https:// doi. org/ 10. 1038/ natur e14539
Lee VH, Hew JJ, Leong LY, Tan GWH, Ooi KB (2020) Wearable payment: a deep learning‑based dual‑stage SEM‑ANN analy‑

sis. Expert Syst Appl 157:113477. https:// doi. org/ 10. 1016/j. eswa. 2020. 113477

Leong LY, Hew JJ, Wong LW, Lin B (2022) The past and beyond of mobile payment research: a development of the mobile

payment framework. Internet Res 32(6):1757–1782

Lewis BR, Soureli M (2006) The antecedents of consumer loyalty in retail banking. J Consum Behav 5(1):15–31
Li L, Freeman G, Wohn DY (2021) The Interplay of financial exchanges and offline interpersonal relationships through

digital peer‑to‑peer payments. Telemat Inform. https:// doi. org/ 10. 1016/j. tele. 2021. 101671

Liaw A, Wiener M (2022) Classification and regression by random forest. R News 2:18–22
Liébana‑Cabanillas F, Sánchez‑Fernández J, Muñoz‑Leiva F (2014) Role of gender on acceptance of mobile payment. Ind

Manag Data Syst 114(2):220–240

Liébana‑Cabanillas F, Ramos de Luna I, Montoro‑Ríos F (2017) Intention to use new mobile payment systems: a compara‑

tive analysis of SMS and NFC payments. Econ Res‑Ekonomska Istraživanja 30(1):892–910

Liébana‑Cabanillas F, Molinillo S, Ruiz‑Montañez M (2019) To use or not to use, that is the question: analysis of the deter‑

mining factors for using NFC mobile payment systems in public transportation. Technol Forecast Soc Change 
139:266–276

Liébana‑Cabanillas F, Singh N, Kalinic Z, Carvajal‑Trujillo E (2021) Examining the determinants of continuance intention

to use and the moderating effect of the gender and age of users of NFC mobile payments: a multi‑analytical 
approach. Inf Technol Manag 22:133–161. https:// doi. org/ 10. 1007/ s10799‑ 021‑ 00328‑6

Liébana‑Cabanillas F, Kalinic Z, Luna IRD, Marinkovic V (2022a) A holistic analysis of near field communication mobile pay‑

ments: an empirical analysis. Int J Mob Commun 20(6):703–726

Liébana‑Cabanillas F, Muñoz‑Leiva F, Molinillo S, Higueras‑Castillo E (2022b) Do biometric payment systems work during

the COVID‑19 pandemic? Insights from the Spanish users’ viewpoint. Financ Innov 8(1):1–25

Ma S, Fildes R (2020) Forecasting third‑party mobile payments with implications for customer flow prediction. Int J Fore‑

cast 36(3):739–760. https:// doi. org/ 10. 1016/j. ijfor ecast. 2019. 08. 012

Madani A, Ong JR, Tibrewal A, Mofrad MR (2018) Deep echocardiography: data‑efficient supervised and semi‑supervised 
deep learning towards automated diagnosis of cardiac disease. Npj Digit Med 1:59. https:// doi. org/ 10. 1038/ 
s41746‑ 018‑ 0065‑x

Maindonald J, Braun J (2003) Data analysis and graphics using R. An examplebased approach. Cambridge University

Press, Cambridge, Cambridge

Martín A, Fernández‑Isabel A, Martín de Diego I, Beltrán M (2021) A survey for user behavior analysis based on machine 
learning techniques: current models and applications. Appl Intell 51:6029–6055. https:// doi. org/ 10. 1007/ 
s10489‑ 020‑ 02160‑x

Meyer D (2012) Support vector machines. The interface to libsvm in packagee 1071. Available at svmdoc.pdf
Migliore G, Wagner R, Cechella FS, Liébana‑Cabanillas F (2022) Antecedents to the adoption of mobile payment in China

and Italy: an integration of UTAUT2 and innovation resistance theory. Inf Syst Front 24:1–24

Moorthy K, Chun T’ing L, Chea Yee K, Wen Huey A, Joe In L, Chyi Feng P, Jia Yi T (2020) What drives the adoption of mobile

payment? A Malaysian perspective. Int J Finance Econ 25(3):349–364

Nasir A, Shaukat K, Khan KI, Hameed IA, Alam TM, Luo S (2020) What is core and what future holds for blockchain tech‑

nologies and cryptocurrencies: a bibliometric analysis. IEEE Access 9:989–1004

Nasir A, Shaukat K, Iqbal Khan K, Hameed A, I., Alam, T. M., & Luo, S. (2021) Trends and directions of financial technology

(Fintech) in society and environment: a bibliometric study. Appl Sci 11(21):10353

Nguyen DK, Sermpinis G, Stasinakis C (2022) Big data, artificial intelligence and machine learning: a transformative sym‑

biosis in favour of financial technology. Eur Financ Manag. https:// doi. org/ 10. 1111/ eufm. 12365

Panetta IC, Leo S, Delle Foglie A (2023) The development of digital payments–past, present, and future–from the litera‑

ture. Res Int Bus Finance 64:101855

Patil PP, Dwivedi YK, Rana NP (2017) Digital payments adoption: an analysis of literature. Conference on e‑Business,

e‑Services and e‑Society. Springer, Cham, pp 61–70

Pavlou PA (2002) Institution‑based trust in interorganizational exchange relationships: the role of online B2B market‑

places on trust formation. J Strateg Inf Syst 11(3–4):215–243

Peters A, Hothorn T (2016) Improved predictive models by indirect classification and bagging for classification, regression

and survival problems as well as resampling based estimators of prediction error. https:// cran.r‑ proje ct. org/ web/ 
packa ges/ ipred/ index. html

Petropoulos A, Siakoulis V, Stavroulakis E, Vlachogiannakis NE (2020) Predicting bank insolvencies using machine learning

techniques. Int J Forecast 36(3):1092–1113. https:// doi. org/ 10. 1016/j. ijfor ecast. 2019. 11. 005

Rafdinal W, Senalasari W (2021) Predicting the adoption of mobile payment applications during the COVID‑19 pandemic.

Int J Bank Mark 39(6):984–1002

Ramos‑de‑Luna I, Montoro‑Ríos F, Liébana‑Cabanillas F (2016) Determinants of the intention to use NFC technology as a

payment system: an acceptance model approach. IseB 14(2):293–314

---

<!-- PAGE 30 -->

Antonio et al. Financial Innovation           (2024) 10:94

Page 30 of 30

Rouibah K, Lowry PB, Hwang Y (2016) The effects of perceived enjoyment and perceived risks on trust formation and 
intentions to use online payment systems: new perspectives from an Arab country. Electron Commer Res Appl 
19:33–43. https:// doi. org/ 10. 1016/j. elerap. 2016. 07. 001

Schapire RE, Freund Y, Bartlett P, Lee WS (1998) Boosting the margin: a new explanation for the effectiveness of voting

methods. Ann Stat 26(5):1651–1686

Selvamuthu D, Kumar V, Mishra A (2019) Indian stock market prediction using artificial neural networks on tick data.

Financ Innov 5:16. https:// doi. org/ 10. 1186/ s40854‑ 019‑ 0131‑7

Shaikh A, Liébana‑Cabanillas F, Glavee‑Geo R (2023) Factors inhibiting the adoption intention of digital payment plat‑

forms. In: Responsible finance and digitalization. Routledge, pp 140–154

Sheth J, Kellstadt CH (2021) Next frontiers of research in data driven marketing: Will techniques keep up with data tsu‑

nami? J Bus Res 125:780–784. https:// doi. org/ 10. 1016/j. jbusr es. 2020. 04. 050

Singh J, Sirdeshmukh D (2000) Agency and trust mechanisms in consumer satisfaction and loyalty judgments. J Acad

Mark Sci 28:150–167. https:// doi. org/ 10. 1177/ 00920 70300 281014

Skinner BF (1953) Science and human behavior. Simon and Schuster, New York, p 92904
Speiser JL, Miller ME, Tooze J, Ip E (2019) A comparison of random forest variable selection methods for classification

prediction modeling. Expert Syst Appl 134:93–101. https:// doi. org/ 10. 1016/j. eswa. 2019. 05. 028

Tamayo B (1999) Nuevos campos para la innovación: Internet y el comercio electrónico de bienes y servicios. Recuper‑

ado de www. navac tiva. com/ es/ desca rgas/ pdf/ atic/ cotec. pdf

Taylor S, Todd PA (1995) Understanding information technology usage: a test of competing models. Inf Syst Res

6(2):144–176

Thai HT (2022) Machine learning for structural engineering: a state‑of‑the‑art review. Structures 38:448–491. https:// doi.

org/ 10. 1016/j. istruc. 2022. 02. 003

Thakor AV (2020) Fintech and banking: What do we know? J Financ Intermed 41:100883
Tounekti O, Ruiz‑Martínez A, Skarmeta Gomez AF (2022) Research in electronic and mobile payment systems: a biblio‑

metric analysis. Sustainability 14(13):7661

Türker C, Altay BC, Okumuş A (2022) Understanding user acceptance of QR code mobile payment systems in Turkey: an

extended TAM. Technol Forecast Soc Change 184:121968

Upadhyay N, Upadhyay S, Abed SS, Dwivedi YK (2022) Consumer adoption of mobile payment services during COVID‑19:

extending meta‑UTAUT with perceived severity and self‑efficacy. Int J Bank Mark 40(5):960–991

Vanini P, Rossi S, Zvizdic E, Domenig T (2023) Online payment fraud: from anomaly detection to risk management. Financ

Innov 9:66. https:// doi. org/ 10. 1186/ s40854‑ 023‑ 00470‑w

Vellido A, Lisboa PJG, Vaughan J (1999) Neural networks in business: a survey of applications (1992–1998). Expert Syst

Appl 17:51–70. https:// doi. org/ 10. 1016/ S0957‑ 4174(99) 00016‑0

Venables WN, Ripley BD (2002) Modern applied statistics with S, 4th edn. Springer, New York, NY
Venkatesh V, Bala H (2008) Technology acceptance model 3 and a research agenda on interventions. Decis Sci

39(2):273–315

Venkatesh V, Davis FD (2000) A theoretical extension of the technology acceptance model: four longitudinal field studies.

Manag Sci 46(2):186–204

Venkatesh V, Morris MG, Davis GB, Davis FD (2003) User acceptance of information technology: toward a unified view.

MIS Q 27:425–478

Venkatesh V, Thong J, Xu X (2012) Consumer acceptance and use of information technology: extending the unified

theory of acceptance and use of technology. MIS Q 36(1):157–178

Visconti‑Caparrós JM, Campos‑Blázquez JR (2022) The development of alternate payment methods and their impact on

customer behavior: the Bizum case in Spain. Technol Forecast Soc Change 175:121330

Wakefield RL, Whitten D (2006) Examining user perceptions of third‑party organizations credibility and trust in an

e‑retailer. J Organ End User Comput (JOEUC) 18(2):1–19
Weisberg S (2005) Applied linear regression, vol 528. Wiley, Hoboken
Witten IH, Frank E (2005) Data mining: practical machine learning tools and techniques, 2nd edn. Morgan Kaufmann

Publishers, Massachusetts

Wu R‑Z, Lee J‑H, Tian X‑F (2021) Determinants of the intention to use cross‑border mobile payments in Korea among

Chinese tourists: An integrated perspective of UTAUT2 with TTF and ITM. J Theor Appl Electron Commer Res 
16(5):1537–1556

Wu Y, Zhang W, Shen J, Mo Z, Peng Y (2018) Smart city with Chinese characteristics against the background of big data:

idea, action and risk. J Clean Prod 173:60–66

Xiong T, Ma Z, Li Z, Dai J (2022) The analysis of influence mechanism for internet financial fraud identification and user

behavior based on machine learning approaches. Int J Syst Assur Eng Manag 13(3):996–1007. https:// doi. org/ 10. 
1007/ s13198‑ 021‑ 01181‑0

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Antonio et al. Financial Innovation (2024) 10:94 Financial Innovation
https://doi.org/10.1186/s40854-024-00625-3
RESEARCH Open Access
Examining user behavior with machine
learning for effective mobile peer-to-peer
payment adoption
Blanco‑Oliver Antonio1*, Lara‑Rubio Juan2, Irimia‑Diéguez Ana1 and Liébana‑Cabanillas Francisco3
*Correspondence:
Abstract
aj_blanco@us.es
Disruptive innovations caused by FinTech (i.e., technology‑assisted customized financial
1 Department of Financial
Economics and Operations services) have brought digital peer‑to‑peer (P2P) payments to the fore. In this chal‑
Management, University lenging environment and based on theories about customer behavior in response
of Seville, Seville, Av. Ramón y
to technological innovations, this paper identifies the drivers of consumer adoption
Cajal, 1, 41018 Seville, Spain
2 Department of Finance, of mobile P2P payments and develops a machine learning model to predict the use
University of Granada, Granada, of this thriving payment option. To do so, we use a unique data set with information
Spain
from 701 participants (observations) who completed a questionnaire about the adop‑
3 Department of Marketing
and Market Research, University tion of Bizum, a leading mobile P2P platform worldwide. The respondent profile
of Granada, Granada, Spain was the average Spanish citizen within the framework of European culture and lifestyle.
We document (in this order of priority) the usefulness of mobile P2P payments, influ‑
ence of peers and other social groups such as friends, family, and colleagues on indi‑
vidual behavior (that is, subjective norms), perceived trust, and enjoyment of the user
experience within the digital context and how those attributes better classify (poten‑
tial) users of mobile P2P payments. We also find that nonparametric approaches based
on machine learning algorithms outperform traditional parametric methods. Finally,
our results show that feature selection based on random forest, such as the Boruta
procedure, as a preprocessing technique substantially increases prediction perfor‑
mance while reducing noise, redundancy of the resulting model, and computational
costs. The main limitation of this research is that it only has a place within the socio‑
cultural and institutional framework of the Spanish population. It is therefore desirable
to replicate this study by surveying people from other countries to analyze the effects
of the institutional environment on the adoption of mobile P2P payments.
Keywords: Boruta, Feature selection, Mobile, P2P, Payment, Random forest
JEL Classification: C45, C53, G17, G28, F65
Introduction
The financial services industry has recently been forced to adopt technological changes
to innovate its processes and products (Frame et al. 2018; Kou et al. 2021). As a result,
a set of technology-assisted customized financial services (FinTech) has arisen in
the banking market (Thakor 2020). Prominent among them are nonintermediated
© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate‑
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by/4.0/.

Antonio et al. Financial Innovation (2024) 10:94 Page 2 of 30
peer-to-peer (P2P) transactions based on digital infrastructures, such as lending and
payments. Indeed, mobile P2P payments are a business vector with deeper market pen-
etration (Abdullah and Naved Khan 2021) and have experienced an extraordinary boom,
particularly since the beginning of the COVID-19 pandemic (Higueras-Castillo et al.
2023). It should be noted that mobile P2P payments constitute a real threat to tradi-
tional payment methods and were born from a need to break the domination of cash and
credit card payments for common day-to-day purchases (Belanche et al. 2022; Insider
Intelligence 2022). Mobile P2P payments have emerged as a singular digital payment
system and are simpler, faster, more convenient, usually cost-free, and feature a social
component that other (digital and not digital) systems lack (Li et al. 2021; Nasir et al.
2020, 2021).
Given that mobile P2P payments are a disruptive innovation in the financial services
sector, previous research has focused on identifying the factors determining their use
(Leong et al. 2022). In practice, financial entities drive change by fostering digital pay-
ments among customers. Thus, they need to know the attributes that explain customary
resistance to change and the barriers to using new technologies and transferring know-
how (Irimia-Diéguez et al. 2023). In this vein, Liébana-Cabanillas et al. (2021) showed
that the precursors and barriers to using P2P payments differ from those of mobile-
based payment methods, calling for further research.
Therefore, the key research question that this paper aims to shed light on is the drivers
and barriers that foster the adoption of mobile P2P payments between banking custom-
ers (Shaikh et al. 2023). Accordingly, the main objective of this paper is to analyze factors
that determine customers’ adoption of mobile P2P payments. Our contribution lies in
finding the key variables that allow banking customers to be classified as users (or non-
users) of mobile P2P payments. To this end, we compare traditional parametric statisti-
cal techniques with a set of nonparametric approaches based on machine learning (ML)
methods oriented to classification problems. These learning algorithms are the founda-
tions of data mining and big data current trending topics in the financial innovation field
and are considered to be a crucial part of a wider research area known as Knowledge
Discovery from Data, which focuses on identifying patterns in data sets (Nguyen et al.
2022).
It is worth highlighting, as one of the core strengths of the present study, the use of a
unique data set with information from 701 individuals (observations) who were asked
about the use of mobile P2P payments; namely, the use of Bizum, one of the leading and
pioneering mobile P2P payment applications worldwide, whose success is comparable to
Venmo in the USA (Acker and Murthy 2020).
This paper contributes to the FinTech and ML literature in two ways. Practically, our
findings have significant implications for banks with a high interest in precisely knowing
the factors that impact the intent to use mobile P2P payment services to (i) create more
customized products and services to satisfy the needs of their customers to a greater
extent and (ii) properly plan their business, human resource, and marketing strategies.
One of the key points of this research is the sample, which is built on a survey con-
ducted with users of the mobile P2P payment platform Bizum. We highlight that one of
the main variables explaining the adoption of Bizum as a mobile P2P payment is its full
connection and integration with traditional financial players. In other words, given that

A ntonio et al. Financial Innovation (2024) 10:94 Page 3 of 30
Bizum is a bank-based platform with a largely predefined bank–customer relationship, it
has benefited from its deep market penetration into the traditional banking industry to
create new business relationships and become a trustworthy and massively used mobile
P2P payment platform. Indeed, this, together with the development of technology allow-
ing the widespread use of smartphones, is a primary factor explaining the strong expan-
sion and adoption of Bizum as a mobile P2P payment method.
Theoretically, our framework employs the most relevant models from technology
acceptance theories. We use variables from the theory of reasoned action from Fish-
bein and Ajzen (1977), technology acceptance model (TAM) from Davis et al. (1989),
theory of planned behavior from Ajzen (1991), extended TAM, namely TAM 2 from
Venkatesh and Davis (2000) and TAM 3 from Venkatesh and Bala (2008), unified theory
of acceptance and use of technology (UTAUT) from Venkatesh et al. (2003), UTAUT2
from Venkatesh et al. (2012), and mobile payment technology acceptance model from
Liébana-Cabanillas et al. (2014). Empirically, we follow Witten and Frank (2005), who
suggest implementing various statistical languages and search procedures that serve
some problems well and others badly, an added motivation for more carefully construct-
ing and comparing alternative ML techniques. In addition, the first preselection of inde-
pendent variables is applied by combining Boruta and Gini index procedures to obtain
a more parsimonious model. Thus, the comparison of different ML techniques in the
field of user adoption of mobile P2P payments constitutes the second contribution of
this study.
The rest of this paper is structured as follows. "Theoretical background" section
describes the dataset and the learning machine models used in this research. "Methodol-
ogy" section presents the empirical results, "Results" section contains the discussion, and
"Discussion" section sets out the conclusions, implications, and areas for future research.
Theoretical background
Evolution of payment systems
New payment systems have emerged from advancements in information and commu-
nication technology for financial transactions between businesses and their custom-
ers. Specifically, these systems arise as a means of addressing certain issues associated
with handling physical money (Tamayo 1999), the need to reduce the cost of money and
existing payment methods, providing flexibility for small purchases and instant pay-
ments, enhancing security and protection against fraud and other forms of crime, and
the rise of e-commerce on the Internet and online payments.
Consequently, the financial sector is undergoing a profound transformation where tra-
ditional payment systems relying on cash are being replaced by electronic payment sys-
tems (see Fig. 1). According to a recent study by the European Central Bank (2022), the
total number of noncash payment transactions in the euro area, encompassing all types
of payment services, increased by 12.5% compared to the previous year, reaching 114.2
billion transactions, with a total amount increase of 18.6% to 197 trillion euros. Card
payments accounted for 49% of the total transactions, transfers represented 22%, and
direct debits represented 20%.
In addition to this trend, the extensive use of technologies such as mobile phones has
also brought about significant changes in user payment behaviors (Liébana-Cabanillas

Antonio et al. Financial Innovation (2024) 10:94 Page 4 of 30
Fig. 1 Classification of payment systems. Source: Own elaboration based on Huang (2021)
et al. 2022a). Current mobile payment solutions are based on the technological develop-
ment of smartphones, enabling the creation of payment applications that can be used in
various ways for conducting payment transactions with a mobile device (Liébana-Caba-
nillas et al. 2017). The classification of mobile payments evolves from the use of smart-
phones at the point of sale, where they are used to perform economic transactions for
purchasing products or services and even function as a point-of-sale terminal for cus-
tomers. Second, mobile phones can serve as a standard payment platform, offering vari-
ous functionalities such as executing payments and sending money. Third, these phones
can be used as a payment channel through the user’s telecommunications operator, with
whom they have a contracted phone line.
Finally, closed-loop payments refer to mobile applications specifically developed for
a particular store or brand, where the mobile phone functions not only as a payment
option within that store but also includes additional payment-related services such as
promotional notifications, loyalty programs, and discount coupons.
Previous research on mobile payment adoption
Since the seminal work of Dahlberg et al. (2008) on mobile payment systems, various
authors have analyzed the field of mobile payments up to the present day (Liébana-
Cabanillas et al. 2022b; Migliore et al. 2022). Dennehy and Sammon (2015) concluded
that research on mobile payments is a well-established area that will continue to receive
increased attention from various disciplines in the coming years, recognizing the poten-
tial and enrichment of mobile payment services as their adoption becomes increasingly
imperative. To date, customer adoption continues to be of interest to many research-
ers, but the focus remains on investigating adoption in specific countries separately, with
less attention given to comparing survey results across multiple countries and examin-
ing their differences. More recently, authors such as Abdullah and Naved Khan (2021),
Tounekti et al. (2022), and Panetta et al. (2023) have proposed bibliometric reviews that
highlight the importance of this current and future research topic. Furthermore, recent
studies on adoption have specifically examined technology, security, and architecture.

A ntonio et al. Financial Innovation (2024) 10:94 Page 5 of 30
Table 1 Recent research on mobile payment adoption
References Theory Results
Patil et al. (2017) Extended UTAUT The results revealed that performance expectancy and
perceived usefulness, followed by perceived ease of use,
are the factors influencing consumers’ positive behav‑
ioural intention towards mobile payment services, while
perceived risk emerges as the main inhibitor
Jun et al. (2018) VAM Compatibility, simplicity, and economic value have an
impact on users’ perceived value and the perceived
value has an impact on the intention of continued use of
mobile payments
Moorthy et al. (2020) UTAUT2 The study revealed that performance expectancy, facili‑
tating conditions, hedonic motivation, and perceived
security are significant in mobile payment adoption.
However, effort expectancy and social influence are not
significant
Liébana‑Cabanillas et al. (2019) Mixed model The results show that satisfaction, service quality, effort
expectancy, and perceived risk are determining factors
of the continuance intention to use mobile payment
applications
Flavián et al. (2020) Extended TAM The results showed that mindfulness, perceived ease of
use, perceived usefulness, subjective norms, and attitude
have a significant influence on mobile payment use
intention
Wu et al. (2021) UTAUT2 ITM TTF The study found that initial trust, performance expec‑
+ +
tancy, effort expectancy, facilitating conditions, price
value, task technology fit, and initial trust have significant
effects on use intention
Rafdinal and Senalasari (2021) Extended TAM Technology Readiness Index constructs affect perceived
usefulness and perceived ease of use, except for discom‑
fort which has no significant effect on the perceived use‑
fulness. In addition, attitude is influenced by two main
TAM variables: perceived usefulness and perceived ease
of use. Meanwhile, the intention to use mobile payment
applications is influenced by attitude
Türker et al. (2022) Extended TAM Perceived usefulness, trust and compatibility positively
and significantly affect IU, while PS has a negative and
significant impact
Migliore et al. (2022) UTAUT2 IRT The proposed theoretical model identified performance
+
expectancy, social influence, facilitating conditions,
hedonic motivations, and effort expectancy as significant
antecedents of the intended use of mobile payment
Bailey et al. (2022) UTAUT2 Performance expectancy, social influence, bank trust,
confidence in MP system and consumer innovativeness
all impact consumers’ MP use intention; and use inten‑
tion impacts MP behaviour
Liébana‑Cabanillas et al. (2022a) Extended TAM The results revealed that, of the three proposed ante‑
cedents, perceived usefulness is the most important,
followed by attitude and perceived security
Source: TAM (technology acceptance model), UTAUT (unified theory of acceptance and use of technology), ITM (initial trust
model), TTF (task technology fit), Value-based adoption model (VAM) and IRT (innovation resistance theory)
Table 1 summarizes recent research that has analyzed the adoption of mobile payment
systems.
Peer‑to‑peer mobile payment system: Bizum
P2P payments are peer-to-peer applications that facilitate the immediate transfer
of mobile money transactions anywhere. Furthermore, this type of payment, which
was previously widespread in the private sphere, is also starting to extend into the
commercial realm for making purchases at physical establishments. An increasing

Antonio et al. Financial Innovation (2024) 10:94 Page 6 of 30
number of consumers are using P2P payment apps to pay for their purchases at retail
stores. This trend is driven by the growing acceptance of P2P payments by merchants
(Visconti-Caparrós et al. 2022).
One pioneering P2P payment system in Europe is Bizum, which is known for its origin
and comparative competitiveness. It offers its users three major advantages: (i) immedi-
acy, as transferred funds reach recipients’ bank accounts within seconds; (ii) universality,
as customers do not need to switch financial institutions, and the system is connected
to all participating banks; and (iii) user-friendliness, as it allows users to make payments
between individuals as well as at physical and online stores.
In addition, its operation is straightforward: to send money, the Bizum user selects a
contact from their mobile phone lists and sets the desired transfer amount. The sender’s
bank then sends a code to their mobile phone, which the user enters into the app, and
the recipient immediately receives the money in their linked bank account.
Bizum is supported by all Spanish banks, with an option for each e-banking applica-
tion, and it is used by more than 21 million active users (nearly 50% of the Spanish popu-
lation), having a historical track record of 1,362 million transactions and more than EUR
70.5 million transferred since its launch in 2016 (Bizum 2022). Bizum can be considered
a transversal payment method because its customer profile includes people of any age,
educational level, and socioeconomic class (Belanche et al. 2022).
Considering this review of the adoption of mobile payment systems in general, and
P2P systems in particular, as well as in line with our objectives, the current research pro-
poses an improvement in the analysis techniques that may determine the variables that
foster the intention to use P2P payment systems through the application of different sta-
tistical languages combining Boruta and Gini index procedures to obtain a more parsi-
monious model.
Machine learning and mobile payments
Comparative analysis of key machine learning techniques
ML is a part of artificial intelligence that, by compiling statistical algorithms and sys-
tems, demonstrates intelligence to interpret external data correctly and subsequently
make decisions (Davenport et al. 2020). In essence, ML models seek to learn relation-
ships and patterns from a given dataset, and therefore, they can be used to solve both
predictive and classification/categorization problems (Bishop 2006).
ML is emerging in parallel with the development of computational science and data-
driven business management (Sheth and Kellstadt 2021). This is why, in recent years,
numerous ML-based intelligent systems have been massively penetrating our business
and personal lives (known as the Internet of Things, IoT) (Kaplan and Haenlein 2019).
Indeed, ML shows a much greater performance in high-dimensional data environments,
where variable interactions and nonlinear relationships often arise, and automatized
recurrent decisions are required (Vanini et al. 2023). Accordingly, ML algorithms have
been successfully applied in many fields, such as banking, to decide whether to approve
or reject a loan application (Alonso-Robisco and Carbó-Martínez 2022), and in engi-
neering for structural design (Thai 2022).
One of the pioneering ML models that have subsequently reached a remarkable
expansion and relevance is artificial neural networks (ANNs). ANNs attempt to emulate

A ntonio et al. Financial Innovation (2024) 10:94 Page 7 of 30
human brain functioning by creating a set of interconnected nodes (artificial neurons)
placed on several layers that reason in a network architecture (Selvamuthu et al. 2019).
Among the most used neural networks in business research is the multilayer percep-
tron (MLP) (Vellido et al. 1999), whose main theoretical advantage is that of support-
ing the fulfillment of the universal approximate property (Bishop 2006). Nevertheless,
in recent years, complex ANN architectures have emerged, namely deep ANNs (e.g.,
convolutional ANNs), which already excel in human performance in some environments
(Madani et al. 2018).
Despite their advantages, the main limitation of ANNs is their black-box nature, which
jeopardizes the interpretation of results and the importance, effects, and relationships
between the variables. ANNs have a high computational cost to tune the training param-
eters, which lengthens the time required to design the topology of the optimal network.
At the beginning of the current century, ensemble methods emerged, whose main
ground is that the nature of a phenomenon is captured to a greater extent by combining
several alternative methods that are subsequently synthesized by a sole optimal model.
That is, ensemble algorithms benefit from the strengths of different models without con-
ducting a biased model preselection. Within the ensemble-based approach, two primary
methods emerge: bagging and boosting models.
First, the bagging algorithm proposed by Breiman (1996) fits the same underlying
algorithm to each training step, creating a final prediction that is the average of each
bootstrap prediction. Given a classification model, bagging draws B independent sam-
ples with a replacement from the available training set (bootstrap samples), fits a model
to each bootstrap sample, and finally aggregates the B models by majority voting. Since
the final prediction is always a pondered result of several bootstrap fits, bagging power-
fully decreases the model variance and biases, leading to a model with higher generaliza-
tion ability without overfitting problems (Schapire et al. 1998).
This advantage allows bagging to be successfully applied to generate other ML mod-
els. In this vein, when bagging is applied to a tree-based method, this results in a model
called random forests (RF), which is one of the most relevant ML techniques (Breiman
2001). RF is an ML method based on the building and combination of a large set of trees.
The main strength of RF is that in each split, a random subset of predictors is consid-
ered, increasing the probability of weak predictors being selected and thereby reducing
bias in the model. Otherwise, stronger predictors would be used by many trees as a first
split. To do so, it randomly selects the variables to split the dataset and create each node
while each tree grows from a bootstrap sample of the training dataset.
The growing interest in the use of RFs is also due to their capacity to rank predictor
variables according to their importance in explaining the studied phenomenon (Fried-
man et al. 2000). That is, unlike most ML methods that have a black-box nature, RF
shows how each variable influences the understanding of the analyzed event. Indeed,
this is the procedure employed in this study to select the most relevant variables (see
"Feature selection results" section). Moreover, other positive aspects of this method are
that it does not generally overfit and that Bayes consistency is obtained with a simple
version of RF (Breiman 2001).
Note that RF can be considered an improved version of the classification and regres-
sion trees (CART) approach. In this vein, RF randomly selects the variables to split the

Antonio et al. Financial Innovation (2024) 10:94 Page 8 of 30
dataset and creates each node while each tree grows from a bootstrap sample of the
training dataset. Thus, it does not fail as CART, as the main disadvantage lies in that
a change in a higher-level node, by the domino effect, can lead to completely different
trees. In other words, the performance of the CART is strongly dependent on the stop-
ping criteria implemented because this model is developed using binary recursive par-
titioning, which is an iterative procedure of splitting the dataset until reaching the final
nodes. Of course, CART also has advantages. Indeed, Breiman (2001) considers that
CART is the model with easier understanding and interpretation. Further, CART also
assumes nonlinear relationships between variables and higher-order interactions (Boul-
esteix et al. 2015).
Second, unlike bagging, boosting trains models sequentially by analyzing the predic-
tion errors, which results in a powerful improvement of the classifiers (Freund 1995).
AdaBoost is the most relevant model within this approach. AdaBoost assigns increasing
weights to observations that are incorrectly classified in the last iteration of the clas-
sifier. Consequently, the subsequent iterations will focus on correctly classifying these
observations, which ultimately will minimize the prediction errors. In this paper, we
implement Adaboost as well as Binominal Boosting and L2 Boosting. Other boosting
algorithms related to additive basis expansion were developed by Friedman et al. (2000).
Finally, support vector machine (SVM) is a powerful technique mainly used for binary
classification problems, although it can also be applied to multiclass classifications that
build a hyperplane to separate the observations of different classes. To do so, the SVM
uses support vectors that are data falling closest to the hyperplane. Although SVM usu-
ally generates low misclassification errors and can function well in environments with
high-dimensional data, it has a high operational cost in terms of time consumption.
Moreover, sometimes SVM works with a nonoptimal function, which undermines its
performance.
User behavior prediction
Behavior analysis was introduced in 1953 by Skinner (1953) and focused on analyzing
human behavior from a psychological perspective. However, technological advance-
ments have allowed massive data processing and the powerful development of data
mining and ML algorithms that have been increasingly applied to explore human behav-
ior, biasing behavior analysis toward the computational science area. Indeed, behavior
analysis is currently called behavioral analytics (Cao et al. 2015), whose aim is to model
human behavior by understanding the past to predict its future, and thus create business
strategies using statistical and ML approaches (Martín et al. 2021).
From the beginning, these analyses essentially address how individuals interact and
the role that they play by acting as a group (collaboration-competition) as well as indi-
vidually (routines–attitudes–intentions). However, the study of human behavior is not
altruistic. Rather, there is a strong economic interest that companies are trying to exploit
to increase their market share, brand, and products-services positioning and, ulti-
mately, their profits. For this reason, currently, this discipline is closely connected to the
economy and organizational management and is encompassed in the field called user

A ntonio et al. Financial Innovation (2024) 10:94 Page 9 of 30
behavior analysis, which comes together with human behavior ML techniques and busi-
ness decision-making (LeCun et al. 2015; Cui et al. 2016).
In practice, ML has been successfully employed in different domains related to disrup-
tive innovations and marketing, such as the recommendation of products to potential
customers (Hagenauer and Helbich 2017) or the estimation of consumer preferences for
technology products (Guo et al. 2021).
Particularly relevant is the use of ML in P2P finance (also known as Internet or Digital
Finance), which mainly operates through the Internet; therefore, a large amount of data
must be processed before decision-making (Wu et al. 2018). As suggested by Gomber
et al. (2017), digital finance is a new form of finance based on third-party payment, cloud
computing, big data, social networks, and e-commerce platforms to obtain financing
and credit as well as to make payments and other financial transactions. In this challeng-
ing environment, ML can collect new data, update the model, and provide an output,
thus adapting to rapidly evolving environments, such as economic patterns and shocks.
Indeed, ML is being effectively used to explore the factors that influence users’ digital
finance behavior (Xiong et al. 2022). Authentication technology, the nonrepudiation of
transactions, privacy protection, data integrity, and user trust have a significant impact
on users’ Internet finance behavior.
Focusing on e-payment users, Bajari et al. (2015) suggested that ML techniques out-
perform discrete choice models, which have been the referenced statistical methods
used to analyze consumers’ preferences and adoption of means of payments and other
digital financial services (Hernández-Murillo et al. 2010). As pointed out by Cui et al.
(2016), ML is a powerful methodological approach that promises to generate new
insights into payment behavior. In this sense, Lee et al. (2020) used a two-stage anal-
ysis by employing Partial Least Squares and subsequently an artificial neural network
to explore the antecedents that affect users’ behavioral intention to use wearable pay-
ments. Also, Aslam et al. (2022), using SVM, studied the users´ behavioral factors that
explain the adoption of mobile payments. They found perceived value to be the most
important predictor of usage behavior. Even, users´ behavior with mobile payments has
been employed as a driver to forecast, through ML, stores’ total customer flows (Ma and
Fildes 2020).
To the best of the authors´ knowledge, only the above few research articles analyze
the users´ behavior regarding digital payments; therefore, more empirical evidence is
needed. This is not surprising given that mobile payment applications are not yet widely
used by the population, and more importantly, there is very little leading e-payment
software that massively operates in a country (as does happen with Bizum). Therefore,
it is not possible to question users about the behavioral factors that lead them to adopt
these mobile payments. This reinforces the findings of the present study.
Methodology
In this study, we use a primary source of data obtained from a survey of 701 Spanish
smartphone users who are considered potential users of mobile P2P payment systems.
All the users who participated in the survey had experience using their cell phones for
commercial activities, either for shopping or payments. The profile of the respondents
was that of an average Spanish citizen having their place in the European culture and

Antonio et al. Financial Innovation (2024) 10:94 Page 10 of 30
lifestyle framework. To collect the data, nonprobability snowball sampling was employed
through a mailing list and social networks. Although simple random sampling is the best
sampling method, many empirical studies published in high-impact journals have used a
snowball method when collecting data (Belanche et al. 2022; Huang et al. 2019).
The questionnaire included items to measure the variables defined in Table 2. The
items were selected through a review of the relevant literature, adapting the origi-
nal scales to the nature of the research. The participants expressed their attitudes on a
seven-point Likert scale (1: strongly disagree; 7: strongly agree). The questionnaire was
developed using a multi-item approach, where three or more items measured each latent
variable. This is a common procedure in the field of marketing research. Appendix 1
provides the questionnaire used in the study for reference.
The dependent variable is a dummy variable with a null value (0) in the case of a mer-
chant not having a mobile payment system available and a value of one (1) in the case of
these payment systems being available to customers, according to the following:
1 use mobilepaymentsystem
Y
it = 0 does notusemobilepaymentsystem
To execute this research, we will classify the independent variables used in two cat-
egories. We established a group of behavioral variables related to the main theories
concerning the adoption of technologies (perceived ease of use, perceived risk, trust,
personal innovativeness, subjective norms, perceived enjoyment, loyalty to the banking
brand, and perceived quality) and a second group of variables linked to the demographic
classification of potential users of the payment system (gender and age).
Regarding the first group of variables, the classic scientific literature has developed
multiple theories that have analyzed the behavior of individuals despite innovation. In
recent years, some authors have applied these theories to the field of mobile and P2P
payments (Upadhyay et al. 2022; Belanche et al. 2022). Table 2 describes the variables
used and the sources employed for their definition.
Table 2 Variables and theoretical background
Variable Definition Source
Ease of use Individuals’ perception that the use of a given sys‑ Davis (1989)
tem is effortless and/or uncomplicated
Perceived risk A combination of uncertainty plus seriousness of
outcome involved
Perceived Trust Psychological state reflecting favourable expecta‑ Singh and Sirdeshmukh (2000)
tions about the intentions and behaviour of others
Personal Innovation Willingness to try out new information technologies Agarwal and Prasad (1998a)
Subjective norms Expectation that the social environment influences Fishbein and Ajzen (1975)
the decisions of potential users
Perceived enjoyment Pleasure derived from the use of a particular infor‑ Kalinic et al. (2019)
mation technology
Loyalty to the bank brand Reinforcement of users’ intentions based on the Lewis and Soureli (2006)
previous experience of each user
Perceived quality Users’ subjective comparison between the quality Gefen et al. (2003)
of service desired and the quality of service actually
received

A ntonio et al. Financial Innovation (2024) 10:94 Page 11 of 30
The second block of variables refers to the gender and age of potential users of the
proposed payment system. Therefore, our study includes the same categories used by the
Spanish National Employment Institute in its statistical reports to classify a population.
Results
Feature selection results
We performed two preprocessing procedures because, as supported by Chen et al.
(2020), their use substantially improves the prediction result. First, all predictor vari-
ables were standardized into the [0,1] interval to align the dimensionality of predictors
and dependent (dummy) variables. Second, given that we have high-dimensional data in
terms of the number of features (forty-two independent variables, see Table 3), it is nec-
essary to apply a procedure to reduce the complexity of the model by capturing only the
most relevant inputs. The inclusion of many predictors in a model to solve a classifica-
tion problem has severe theoretical disadvantages such as: (i) overfitting, (ii) correlation
problems, (iii) difficulty in interpreting results, and (iv) a slower training process. The
idea is to reduce the noise and redundancy in the final model. Indeed, the principle of
parsimony states that the best statistical model has fewer parameters (variables) and less
dimensionality (Arora and Kaur 2020; Speiser et al. 2019).
Consequently, we performed a procedure to select the most relevant predictors. This
minimizes the complexity of our model and accelerates its training, as well as improves
the robustness of performance measurements, in terms of higher accuracy or lower
errors, due to the booster of the generalization capacity of a classifier. Dewi (2019)
indicated that the feature selection (FS) of the procedure enables reducing the origi-
nal features of a dataset to a smaller one while preserving the relevant information and
rejecting redundant information. As Chen et al. (2020) sustain, FS crucially impacts the
performance of the classification model. Indeed, FS is considered more important than
designing the prediction model.
Following Chen et al. (2020), we implement the random forest (RF) algorithm as
a method to select the most relevant feature from the data. Unlike other parametric
techniques grounded in subset selection, such as logistic regression (LR) with forward
or backward procedures, RF is a nonparametric method based on supervised ML that
incorporates two procedures to select the most important variables: (i) the package
varImp() of R, where the mean decrease of the Gini index is calculated, and (ii) Boruta
(Fahimifar et al. 2022).
The package varImp() of R is implemented after running the RF model. This is a post-
estimation procedure applied to each tree obtained and consists of calculating the pre-
diction accuracy and subsequently permuting each predictor variable. Afterward, the
difference between the two accuracies is averaged over all the trees normalized by the
SE. The package provides two measures of importance for each predictor, disaggregating
the results by outcome class (1, when Bizum is adopted, and 0 otherwise). The first of
these metrics indicates the decrease, on average, in accuracy when a variable is removed.
The second measure provides the reduction of the Gini impurity when a variable is
chosen to split a node. It should be noted that the sample used to calculate the impor-
tance of each variable is the out-of-sample data that was not used during tree construc-
tion. The recommendation is to analyze both measures together because this enables a

Antonio et al. Financial Innovation           (2024) 10:94  Page 12 of 30
Table 3 Feature selection (FS) under random forest approach
| Boruta procedure |     |     | Gini index procedure |     |
| ---------------- | --- | --- | -------------------- | --- |
Variables Mean  Median  Min.  Max.  Norm hits Decision Variables Mean
| importance | importance importance | importance |     | decrease  |
| ---------- | --------------------- | ---------- | --- | --------- |
Gini
| PU2 16.35   | 16.25 15.01 | 17.72 1.00 | Confirmed PU2   | 11.29 |
| ----------- | ----------- | ---------- | --------------- | ----- |
| PU4 16.34   | 16.39 14.53 | 17.62 1.00 | Confirmed PU4   | 10.98 |
| PU1 13.23   | 13.21 11.50 | 15.33 1.00 | Confirmed SN3   | 10.51 |
| SN4 13.06   | 12.97 11.56 | 14.55 1.00 | Confirmed PU3   | 10.39 |
| TR2 12.67   | 12.78 10.72 | 13.89 1.00 | Confirmed PENJ1 | 9.88  |
| PU3 12.50   | 12.49 10.84 | 14.26 1.00 | Confirmed SN4   | 9.66  |
| SN3 12.50   | 12.44 10.97 | 14.53 1.00 | Confirmed SN2   | 8.87  |
| PENJ2 12.31 | 12.20 10.98 | 14.10 1.00 | Confirmed PU1   | 8.85  |
| TR5 11.77   | 11.70 10.18 | 13.33 1.00 | Confirmed PENJ2 | 8.72  |
| PENJ3 11.76 | 11.77 10.29 | 13.13 1.00 | Confirmed TR2   | 8.23  |
| PENJ1 11.44 | 11.43 9.93  | 12.73 1.00 | Confirmed TR5   | 8.03  |
| TR3 10.98   | 11.00 9.23  | 12.40 1.00 | Confirmed PENJ3 | 7.37  |
| SN2 10.73   | 10.72 9.22  | 12.43 1.00 | Confirmed PII1  | 7.31  |
| PII1 10.53  | 10.50 8.62  | 12.41 1.00 | Confirmed QUAL3 | 6.91  |
| QUAL3 10.15 | 10.15 7.83  | 11.91 1.00 | Confirmed QUAL2 | 6.68  |
| PII2 10.01  | 10.08 8.16  | 11.42 1.00 | Confirmed TR3   | 6.65  |
| TR4 9.89    | 9.90 8.58   | 11.31 1.00 | Confirmed SN1   | 6.59  |
| QUAL2 9.74  | 9.81 7.06   | 11.84 1.00 | Confirmed TR4   | 6.56  |
| SN1 8.90    | 8.90 7.33   | 11.38 1.00 | Confirmed PII2  | 6.13  |
| QUAL7 7.55  | 7.55 5.40   | 9.39 1.00  | Confirmed QUAL4 | 5.85  |
| PII3 7.50   | 7.54 5.15   | 9.44 0.99  | Confirmed AGE   | 5.76  |
| QUAL4 7.46  | 7.40 5.74   | 9.00 1.00  | Confirmed QUAL7 | 5.55  |
| TR1 7.18    | 7.21 5.57   | 9.00 1.00  | Confirmed TR1   | 5.33  |
| PII4 6.86   | 6.84 5.49   | 8.37 0.99  | Confirmed PEOU1 | 5.01  |
| PEOU1 6.21  | 6.20 3.64   | 8.35 0.98  | Confirmed PII3  | 4.69  |
| QUAL6 4.92  | 4.87 3.03   | 7.41 0.94  | Confirmed PR4   | 4.66  |
| PR1 4.91    | 4.89 2.62   | 6.71 0.90  | Confirmed PII4  | 4.55  |
| QUAL5 4.84  | 4.89 2.72   | 6.70 0.94  | Confirmed PR1   | 4.44  |
| PR4 4.74    | 4.80 2.37   | 6.81 0.91  | Confirmed PR2   | 4.30  |
| PR2 4.54    | 4.59 1.81   | 6.60 0.90  | Confirmed QUAL6 | 4.20  |
| PEOU4 4.24  | 4.11 2.32   | 6.11 0.85  | Confirmed PR3   | 4.13  |
| QUAL1 4.22  | 4.23 2.23   | 5.85 0.87  | Confirmed QUAL1 | 4.06  |
| PEOU2 3.98  | 3.92 1.34   | 6.36 0.82  | Confirmed QUAL5 | 4.02  |
| LOY1 3.94   | 3.94 1.43   | 6.88 0.80  | Confirmed PEOU4 | 3.96  |
| PEOU5 3.86  | 3.97 1.00   | 6.17 0.76  | Confirmed LOY1  | 3.94  |
| PR3 3.46    | 3.41  0.04  | 5.35 0.68  | Confirmed LOY4  | 3.92  |
−
| LOY4 3.05 | 3.14  0.05 | 5.28 0.57 | Tentative PEOU2 | 3.79 |
| --------- | ---------- | --------- | --------------- | ---- |
−
| LOY3 2.97 | 2.97 1.08   | 4.83 0.57 | Tentative PEOU5 | 3.69 |
| --------- | ----------- | --------- | --------------- | ---- |
| LOY2 2.86 | 2.88 0.63   | 5.16 0.52 | Tentative LOY3  | 3.67 |
| AGE  0.61 |  0.71  1.45 | 0.90 0.00 | Rejected LOY2   | 3.60 |
− − −
| GENDER  0.63 |  0.96  2.29 | 2.50 0.00 | Rejected GENERO | 1.71 |
| ------------ | ----------- | --------- | --------------- | ---- |
− − −
| PEOU3  1.04 |  1.05  2.18 | 1.10 0.00 | Rejected PEOU3 | 0.24 |
| ----------- | ----------- | --------- | -------------- | ---- |
− − −
The variables in bold were not included in the model
comparison of the importance ranking of each one. However, their main disadvantage is
that they may overstate the importance of the correlated variables.
To benchmark with respect to FS, we also implemented the Boruta algorithm that
enables ranking the predictor variables based on their significance (default values
for p value   0.01 and maxRun   100). One of the most important advantages of the
| =   | =   |     |     |     |
| --- | --- | --- | --- | --- |

A ntonio et al. Financial Innovation (2024) 10:94 Page 13 of 30
use of Boruta is that it provides a classification of the variables in three groups: (i)
confirmed, for those significant variables (the most relevant); (ii) tentative, for those
variables that may be selected, but which have less importance; and (iii) rejected, for
those variables that the method considers are not to be included.
The results of the FS analysis are depicted in Table 3 (graphically also in Fig. 2). As
shown here, the two FS procedures employed (Boruta and the Gini index) match most of
the rankings performed, especially in the first variables, i.e., the variables with the high-
est classification of importance.
Unlike the Gini index, one of the main advantages of the Boruta procedure is that
it enables knowing which variable must be included in the model. However, as can be
observed in Table 3, the Boruta procedure considers that the entire list of variables
should be introduced into the model because they have a high importance level. There-
fore, it is not operational from a computational viewpoint. Consequently, to increase the
selection capacity of the FS procedures, we only select, from the ten first variables, the
variables matching the two criteria (Boruta and the Gini index).
Eight of the ten first variables are the most relevant under both FS criteria (see
Table 3); thus, these variables will be included in our classification model. It should be
noted that with this procedure, we are dramatically reducing the number of variables
that will be introduced into our model, considering only eight (i.e., only 19.04% of the
information contained in the original dataset) from forty-two variables. This selection
of the data’s critical features reduces the noise and redundancy of the final model and
improves its interpretation while decreasing the computational costs.
Despite the advantages of the Boruta and Gini index procedures shown above,
the main disadvantage of both procedures is that they do not consider the potential
Fig. 2 The important measure for each variable using Boruta

Antonio et al. Financial Innovation (2024) 10:94 Page 14 of 30
multicollinearity problems that may arise between the resulting explanatory varia-
bles. Indeed, multicollinearity problems remain understudied in the environment of
AI and ML algorithms, although it is one of the most important aspects to consider
in an econometric model (Chan et al. 2022). However, unlike what is often claimed,
correlation does not necessarily mean multicollinearity as they are not the same, and
thus multicollinearity problems cannot be analyzed by using the correlation matrix,
but by using the Variation Inflation Factor (VIF) (Chan et al. 2022). The variable
PU2 has the maximum VIF value (6.548), which confirms the lack of multicollinear-
ity problems (note that although there is no strict threshold for VIF to confirm the
presence of multicollinearity, there is a wide consensus in the previous research to
consider that a VIF of 10 or higher often indicates multicollinearity (Weisberg 2005).
Additionally, as a robustness check, we also implement the forward stepwise logistic
regression as a parametric alternative approach to select the most relevant variables.
Here we obtain only four resulting variables (PU2, SN3, TR5, and PENJ3), of which
three match those obtained in the Boruta and Gini index procedures (our results, in
terms of the nonparametric techniques based on ML outperform the classical LDA
and LR, remain unaltered by applying the Boruta, Gini index, and forward stepwise
logistic regression).
From a theoretical point of view, FS analysis suggests that the variables correspond-
ing to usefulness, subjective usage norms, trust, and perceived enjoyment have a strong
influence on the intention to use mobile payment systems and media.
Specifically, our results suggest that the usefulness of mobile payment media (PU1,
PU2, PU3, and PU4) is a strong explanatory factor in their usage intention, which is an
advance over the previous literature (Bhattacherjee and Premkumar 2004). This pos-
its the concept of perceived usefulness to understand changes in beliefs and attitudes
toward information technology use.
Second, moving on to personal innovation in the information technology domain, two
subjective customer profile variables (SN3 and SN4) show high explanatory and predic-
tive power for the intention to use mobile payment methods (Agarwal and Prasad 1998a;
Taylor and Todd 1995).
Turning to variables related to perceived trust in mobile payment systems, in line with
Ba and Pavlou (2002), our results identify a strong link between bank customers’ per-
ceived trustworthiness in the mobile payment medium (TR2) and their direct intention
to use.
Furthermore, our findings represent an advance over the previous literature regarding
the variable related to the perceived enjoyment of using online payment systems (Agar-
wal and Karahanna 2000; Rouibah et al. 2016), as our results identify a significant rela-
tionship between the perceived enjoyment of using a mobile payment means and the
intention to continue using this technology (PENJ3). To better illustrate the discrimina-
tory power of the RF model after applying the FS procedure, we present the area under
the ROC curve (AUC) in Fig. 3. AUC is calculated by plotting the true positive rate
against the false positive rate at various threshold settings. Indeed, AUC can be defined
as a tradeoff between sensitivity and specificity, given that an increase in sensitivity will
cause a reduction in specificity. The model will have a greater classification power when
the curve is closer to the upper left corner. Similarly, Fig. 4 shows the out-of-bag (OOB)

A ntonio et al. Financial Innovation (2024) 10:94 Page 15 of 30
Fig. 3 Area under ROC curve for random forest (AUC)
Fig. 4 The Out‑Of‑Bag (OOB) error for final random forest model
error, which can be defined as the average error using predictions from trees that are
not contained in their respective bootstrap sample. OOB is used to fit the classifica-
tion power of the RF model while it is being trained. As depicted in Fig. 4, the OOB

Antonio et al. Financial Innovation (2024) 10:94 Page 16 of 30
drastically decreases (i.e., the model increases its fitting) after the first 150 trees, oscillat-
ing steadily from them.
Validation measures
The performance of each model is evaluated using different accuracy measurements
on the results obtained for each method on the out-of-sample. In binary classification
problems, two relevant metrics arise sensitivity and specificity. On the one hand, sen-
sitivity measures the probability that the model classifies a Bizum user as a real user
of Bizum. In other words, sensitivity measures the model’s ability to detect Bizum
usage in its presence. Conversely, specificity measures the probability that the model
classifies a real Bizum nonuser as a Bizum nonuser. That is, specificity measures the
ability of the model to exclude the use of Bizum when it is lacking. Sensitivity and
specificity are defined as follows:
TP TN
Sensitivity Specificity
= TP FN; = TN FP
+ +
where
TP True Positive, the number of positive cases (not adopting mobile P2P pay-
=
ment) that are correctly identified as positive,
TN True Negative, the number of negative cases (adopt mobile P2P payment) that
=
are correctly identified as negative cases,
FN False Negative, the number of positive cases (not adopt mobile P2P payment)
=
that are misclassified as negative cases (adopt mobile P2P payment),
FP False Positive, the number of negative cases (adopt mobile P2P payment) that
=
are incorrectly identified as positive cases (not adopt mobile P2P payment).
Following Petropoulos et al. (2020), we built several performance measurements
based on sensitivity and specificity to overcome the limitations of traditional accuracy
metrics based only on the overall predictive ability. In this vein, we calculate the fol-
lowing measures:
• G-mean: The geometric mean G-mean is the product of sensitivity and specificity.
This metric illustrates the balance between the classification performances of the
majority and minority classes.
G Sensitivity Specificity
= ·
(cid:31)
A poor performance in predicting positive cases will lead to a low G-mean value,
even if the negative cases are correctly classified by the algorithm.
• LR: The negative likelihood ratio is the ratio between the probability of predicting
a case as negative when it is positive and the probability of predicting a case as
negative when it is actually negative.
1 Sensitivity
LR −
= Specificity
A lower negative likelihood ratio signifies better performance in negative cases. This
is the main point of interest in this study as we model bank failures.

A  ntonio et al. Financial Innovation           (2024) 10:94  Page 17 of 30
•  DP: Discriminant power is a measurement that sums up sensitivity and specificity.
|     | √3  | Sensitivity         | Specificity         |                  |     |
| --- | --- | ------------------- | ------------------- | ---------------- | --- |
|     | DP  | log                 | log                 |                  |     |
|     | = π | 1 Sensitivity       | + 1                 | Specificity      |     |
|     |     | (cid:31) (cid:30) − | (cid:29) (cid:30) − | (cid:29)(cid:28) |     |
The algorithm distinguishes between positive and negative cases for DP values greater
than 3.
•  BA: Balanced accuracy is the average of Sensitivity and Specificity. If the classifier
performs equally well on either class, this term lowers the conventional accuracy
measure.
1
|     | BA       | Sensitivity Specificity |          |     |     |
| --- | -------- | ----------------------- | -------- | --- | --- |
|     | = 2      | +                       |          |     |     |
|     | (cid:31) |                         | (cid:30) |     |     |
In contrast, if the conventional accuracy is high simply because the classifier takes advan-
tage of a good prediction on the majority class, the balanced accuracy will decrease, thus
signaling any performance issues. That is, BA does not disregard the accuracy of the
model in the minority class (i.e., adopt Bizum in our case).
•  Youden’s γ: Youden’s index is a linear transformation of the mean sensitivity and
specificity; consequently, it is difficult to interpret.
γ
|     | Sensitivity | 1 Specificity |          |     |     |
| --- | ----------- | ------------- | -------- | --- | --- |
|     | =           | − −           |          |     |     |
|     |             | (cid:31)      | (cid:30) |     |     |
As a general rule, a higher value of Youden’s γ signifies a better ability of the algorithm to
avoid misclassification of the population.
•  WBA1: A weighted balance accuracy measure that weighs specificity more than sen-
sitivity (75%/25%).
•  WBA2: A weighted balance accuracy measure that weighs sensitivity more than
specificity (75%/25%).
Alternatively, we also calculate the AUC, which can be defined as the probability that the
classifier will rank a randomly chosen positive instance higher than a randomly chosen
negative instance. The value of AUC varies between 0.50 and 1, being accepted by the
researcher that a value above 0.80 denotes a high performance.
Finally, to facilitate the interpretation of the results, we build a metric, the Global Per-
formance Index (GPI), which summarizes the results of the previous performance meas-
urements. We define GPI as the arithmetic average of all previous metrics, except for
Type I and II errors, because they are complementary ratios to specificity and sensitivity.
Moreover, given that a model obtains a better performance with lower values of LR, this
metric subtracts in the following expression:
| AUC | Accuracyratio | Sensitivity Specificity | Gmean LR | DP BA Youden′s | WBA1 WBA2 |
| --- | ------------- | ----------------------- | -------- | -------------- | --------- |
| GPI | +             | + +                     | + −      | + + +          | + +       |
| =   |               |                         | 11       |                |           |
Results
The final sample, after eliminating questionnaires that were completed too quickly or
exceeded the recommended time, amounted to 701 participants, of whom 46.22% were
male and 53.78% were female. 42.37% were between 18 and 24 years old, 51.21% were

Antonio et al. Financial Innovation (2024) 10:94 Page 18 of 30
between 25 and 44 years old, and 6.28% were over 44 years old. Of these, 4.28% had
doctoral studies, 49.93% had university studies, 26.68% had secondary school studies,
15.83% had primary school studies, and the remaining 3.28% had no studies at all. The
number of invalid questionnaires rejected was only 13; thus, the valid response rate was
98%.
Table 4 summarizes the results in terms of performance metrics in the test set. This
shows that there is not a unique model that obtains the best performance in terms of all
metrics. However, our results demonstrate that nonparametric techniques based on ML
often outperform classical LDA and LR. In particular, we find that binomial boosting,
MLP4, and L2 boosting are the models that obtain the best performance in terms of GPI.
Specifically, binomial boosting obtains the best GPI score with a value of 0.6859, fol-
lowed by MLP 4 and L2 boosting, which reach GPIs of 0.6613 and 0.6609, respectively.
In contrast, the two models based on classification trees, CART and CTBag, obtained
the worst performance in terms of GPI.
Since the AUC is based on conceptual and methodological foundations different from
the rest of the metrics, which, as previously argued, are based on specificity and sensi-
tivity (complementary measurements of type I error and type II error, respectively), we
analyze this metric in more detail. In this sense, our findings show that the methods with
the highest AUC values are the neuronal network (MLP 1 and MLP 2), followed closely
by SVM and L2 boosting. In the same way as the GPI, CART, and CTBag are the two
underperforming methods in terms of AUC.
When comparing the performance of the models built using all the variables for the
models that apply FS to reduce the dimensionality of the data, our results suggest that
the performance increases when FS is used. More importantly, we find that the increase
in the performance of implementing FS remains unaltered for all the methods in terms
of all the performance metrics.
Discussion
Theoretical implications
Our empirical research has two relevant results. First, related to the classification accu-
racy of methods, our findings suggest that using FS analysis as a preprocessing technique
substantially improves prediction performance while reducing the noise and redun-
dancy of the resulting model and the computational costs of its implementation due to
lower data dimensionality. All of this definitively improves the theoretical interpretation
of the final model and allows analysis of how each independent variable contributes to
explicating and predicting the use of mobile P2P payments. We also find that there is not
a unique method that outperforms in terms of all metrics, but it is demonstrated that,
in general, nonparametric techniques based on ML outperform classical LDA and LR.
Thus, the results show that binomial boosting, MLP4, and L2 boosting are the models
that obtain the best performance according to the Global Performance Index (GPI).
Second, from a theoretical point of view, we document that (in this order of prior-
ity) the usefulness of mobile P2P payments, the influence of peers and other social
groups such as friends, family, and colleagues on an individual’s behavior (i.e., subjec-
tive norms), and the perceived trust and enjoyment of the user experience in the digital

A  ntonio et al. Financial Innovation           (2024) 10:94  Page 19 of 30
| 8956.0 5646.0 0166.0 6356.0 | 7356.0 3166.0 7066.0 4726.0 | 6316.0 8956.0 4656.0 9586.0 9066.0 | 8236.0 4056.0 8856.0 2666.0 9186.0 | 4786.0 5866.0 9726.0 | 9286.0 9286.0 5976.0 4976.0 4676.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
IPG
|     |     |     | 3987.0 9697.0 2997.0 | 9397.0 0487.0 4057.0 | 9497.0 2997.0 0457.0 0176.0 |
| --- | --- | --- | -------------------- | -------------------- | --------------------------- |
2ABW 6397.0 2477.0 0587.0 7187.0 7187.0 7087.0 3987.0 7387.0 7657.0 7087.0 7587.0 6876.0 0587.0 0957.0 0687.0 3787.0
1ABW 5467.0 9667.0 2977.0 4967.0 4967.0 6687.0 9177.0 9437.0 7437.0 6687.0 2677.0 1488.0 2977.0 8167.0 0267.0 9177.0 4477.0 5108.0 0628.0 4697.0 5677.0 8808.0 5108.0 8748.0 5188.0 3608.0
ϓ s’neduoY
| 1855.0 0145.0 2465.0 1155.0 | 1155.0 3765.0 2165.0 6815.0 | 4194.0 3765.0 9165.0 6265.0 2465.0 | 8025.0 0845.0 2165.0 3175.0 6006.0 | 9916.0 4085.0 9625.0 | 7306.0 6006.0 8106.0 5255.0 6395.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
| 1977.0 5077.0 1287.0 6577.0 | 6577.0 7387.0 6087.0 3957.0 | 7547.0 7387.0 0187.0 3187.0 1287.0 | 4067.0 0477.0 6087.0 7587.0 3008.0 | 0018.0 2097.0 5367.0 | 9108.0 3008.0 9008.0 3677.0 8697.0 |
AB
| 3706.0 2085.0 1216.0 4495.0 | 4495.0 5616.0 2906.0 2955.0 | 8615.0 5616.0 2906.0 2601.1 1216.0 | 1355.0 0295.0 2906.0 5426.0 8466.0 | 8007.0 8536.0 7365.0 | 5076.0 8466.0 3327.0 3690.1 3656.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
PD
| 9552.0 1192.0 2372.0 9772.0 | 9772.0 4182.0 7462.0 1072.0 | 0123.0 4182.0 6172.0 9924.0 2372.0 | 6713.0 3962.0 7462.0 4152.0 7152.0 | 9362.0 9672.0 6233.0 | 0062.0 7152.0 4723.0 1044.0 4272.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
‑RL
naem‑G
| 5877.0 5077.0 1287.0 5577.0 | 5577.0 6387.0 4087.0 7757.0 | 4547.0 6387.0 9087.0 8357.0 1287.0 | 4067.0 6377.0 4087.0 3587.0 3008.0 | 3908.0 1097.0 0367.0 | 7108.0 3008.0 4597.0 1747.0 6697.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
yticfiicepS
| 0057.0 2367.0 3677.0 2367.0 | 2367.0 5987.0 2367.0 5017.0 | 7327.0 5987.0 4177.0 8689.0 3677.0 | 2367.0 0057.0 2367.0 2367.0 6208.0 | 1248.0 6208.0 5987.0 | 8518.0 6208.0 7498.0 8689.0 8518.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
ytivitisneS
| 1808.0 8777.0 9787.0 9787.0 | 9787.0 8777.0 0897.0 1808.0 | 7767.0 8777.0 5097.0 8575.0 9787.0 | 6757.0 0897.0 0897.0 1808.0 0897.0 | 8777.0 8777.0 4737.0 | 9787.0 0897.0 1707.0 7565.0 8777.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
rorre II epyT
| 9191.0 2222.0 1212.0 1212.0 | 1212.0 2222.0 0202.0 9191.0 | 3232.0 2222.0 5902.0 2424.0 1212.0 | 4242.0 0202.0 0202.0 9191.0 0202.0 | 2222.0 2222.0 6262.0 | 1212.0 0202.0 9292.0 3434.0 2222.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
rorre I epyT noitceles erutaef morf gnitluser selbairav tnednepedni eht gnisu yB .A lenaP
| 0052.0 8632.0 7322.0 8632.0 | 8632.0 5012.0 8632.0 5982.0 | 3672.0 5012.0 6822.0 2310.0 7322.0 | 8632.0 0052.0 8632.0 8632.0 4791.0 | 9751.0 4791.0 5012.0 | 2481.0 4791.0 3501.0 2310.0 2481.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- | -------------------- | ---------------------------------- |
elpmas‑fo‑tuo ni stluser ecnamrofreP 4 elbaT
ycarucca tseT
| 9287.0 4177.0 9287.0 1777.0 | 1777.0 9287.0 9287.0 7567.0 | 6847.0 9287.0 9287.0 3457.0 9287.0 | selbairav tnednepedni eht lla gnisu yB .B lenaP 0067.0 1777.0 9287.0 6887.0 0008.0 | 7508.0 6887.0 0067.0 | 0008.0 0008.0 6887.0 6847.0 3497.0 |
| --------------------------- | --------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------- | -------------------- | ---------------------------------- |
| 1198.0 0788.0 5298.0 7198.0 | 9298.0 4788.0 7598.0 2477.0 | 5048.0 2078.0 0258.0 4198.0 7198.0 | 6288.0 5368.0 3578.0 4188.0 3588.0                                                 | 8938.0 6488.0 8808.0 | 0788.0 9698.0 8788.0 8788.0 9788.0 |
 CUA
|     |     | gnitsooB laimoniB |     |     | gnitsooB laimoniB |
| --- | --- | ----------------- | --- | --- | ----------------- |
|     |     | gnitsooB 2L       |     |     | gnitsooB 2L       |
tsooBadA
tsooBadA
|           |                     | gaBTC |                |                | gaBTC |
| --------- | ------------------- | ----- | -------------- | -------------- | ----- |
| 1PLM 2PLM | 3PLM 4PLM MVS  TRAC |       | 1PLM 2PLM 3PLM | 4PLM MVS  TRAC |       |
| ADL       |                     |       | ADL            |                | FR    |
| RL        |                     | FR    | RL             |                |       |

Antonio et al. Financial Innovation (2024) 10:94 Page 20 of 30
context are the attributes that classify the (potential) users of mobile P2P payments with
greater ability.
The major importance of usefulness in the intention to use this P2P payment service
may be mainly based on the number of current users (approximately half of the popu-
lation of Spain). This networking effect is crucial to the success of the service because
the application must be used by both the sender and receiver. In addition, adequate
resources or support are essential for users to perceive the usefulness of the service and
even directly influence the intention of use. Subjective Norms, as the following signifi-
cant factor on the intention to use the service, show that the information that users share
about their experience when using the P2P payment service influences the intention of
other users due to the social requirements of these services. This fact is highly relevant
for those companies that provide these payment services since their plans of action
should focus on developing word-of-mouth strategies and attempting to encourage cur-
rent clients to directly recommend the service. Our results also show that perceived
trust and enjoyment significantly affect the intention to use P2P payment services. This
finding implies that service providers corroborate the need to develop P2P payment ser-
vices that may be easy to use, secure, and attractive to consumers.
The future landscape of the payment sector will be promising for financial entities and
FinTech organizations that are open to change, innovation, and forward-thinking. These
players need to rapidly accelerate their transformation efforts to address unmet cus-
tomer demands and plug the gaps. In this vein, our findings are novel and useful for both
traditional and new financial intermediaries, businesses, customers, and other stake-
holders that are part of financial systems, such as policymakers and regulators. More
importantly, our findings could be of interest to financial institutions to define ad hoc
financial services customized for their target market.
From a theoretical perspective, our results support the necessity of implementing sta-
tistical procedures to reduce the complexity of the data. Boruta and Gini algorithms are
preferable methods because both are based on the nonlinearity performed by Random
Forest, one of the most advanced current ML methods.
Practical implications
From a managerial standpoint, our research findings provide valuable insights for service
providers in the mobile P2P payments industry. To effectively promote the adoption and
usage of their platforms, providers must prioritize enhancing usability and user experi-
ence. This can be achieved by streamlining the payment process, simplifying user inter-
faces, and ensuring smooth and intuitive navigation. By focusing on subjective norms,
providers can tap into the power of social influence, leveraging the positive perceptions
and recommendations of existing users to attract new users. Implementing strategies to
encourage word-of-mouth marketing, such as referral programs or incentives for users
who refer others to the service, can be an effective approach to expanding user adoption.
Building trust is another critical aspect of driving the adoption of mobile P2P pay-
ments. Service providers should prioritize security measures and communicate them
transparently to users. Highlighting the safety of transactions, data protection protocols,
and robust authentication methods can help alleviate concerns and increase users’ trust
in the platform. In addition, incorporating features that enhance user enjoyment and

A ntonio et al. Financial Innovation (2024) 10:94 Page 21 of 30
engagement, such as personalized experiences, rewards, or gamification elements, can
contribute to positive user perception and encourage continued usage.
Beyond the immediate managerial implications, our research findings have broader
societal and economic implications. Promoting the adoption of mobile P2P payments
can contribute to financial inclusion, particularly for marginalized populations, such as
the young, the unemployed, and those with limited access to traditional banking services
in rural areas. By providing these individuals with convenient and accessible payment
solutions, barriers to financial participation can be reduced, enabling them to engage in
economic activities, make transactions, and manage their finances more effectively. This,
in turn, can lead to increased economic empowerment, poverty reduction, and overall
societal development.
Furthermore, from a macroeconomic perspective, higher adoption of mobile P2P pay-
ments can lead to increased financial stability. By reducing the reliance on cash transac-
tions and expanding digital payment options, the risks associated with handling physical
currency, such as theft or counterfeiting, can be mitigated. Additionally, the digitization
of payments enables better tracking and monitoring of financial flows, contributing to
enhanced transparency and accountability within the financial system. This improved
oversight can help prevent illicit activities, such as money laundering and tax evasion
while facilitating more efficient financial regulations and policy implementations.
In conclusion, the implications of our research emphasize the importance of prioritiz-
ing usability, trust, and enjoyment in mobile P2P payment services. By addressing these
factors and promoting the adoption of mobile P2P payments, service providers can not
only drive their business success but also contribute to financial inclusion, economic
development, and financial stability at both the individual and societal levels.
Limitations and avenues for future research
Despite the valuable insights gained from this study, it is important to acknowledge its
limitations, which open up avenues for future research. First, enhancing the dataset by
incorporating additional information, such as users’ training in new technologies, edu-
cational background, and risk aversion, would provide valuable control and moderating
variables to deepen our understanding of the factors influencing the use of mobile P2P
payments. This could shed light on how these individual characteristics interact with
other factors and impact adoption.
Second, obtaining data on the average size of digital payment transactions would allow
for an analysis of how users’ risk aversion influences their adoption of mobile P2P pay-
ments. Examining whether risk-averse individuals are more or less likely to engage in
larger transactions through these payment methods could provide valuable insights into
the relationship between risk perception and usage behavior.
Third, replicating this study by surveying individuals from different countries would
enable an analysis of the effects of institutional frameworks on the adoption of mobile
P2P payments. Comparing adoption patterns across countries with varying regulatory
environments and financial infrastructures could reveal the influence of these contextual
factors on user behavior.
Finally, it is important to address the limitations associated with the sample selec-
tion process, specifically the use of a nonprobability snowball sampling method. Future

Antonio et al. Financial Innovation (2024) 10:94 Page 22 of 30
research should consider employing alternative sampling techniques, such as simple
random sampling or quota sampling, to ensure a more representative and generaliza-
ble sample. This would enhance the external validity of the findings and provide a more
comprehensive understanding of the factors influencing mobile P2P payment adoption
across diverse populations.
By addressing these limitations and pursuing further research in these areas, we can
gain a more nuanced understanding of the adoption and usage of mobile P2P payments,
leading to more effective strategies for service providers and policymakers in driving the
growth and acceptance of these payment methods. Another limitation of ML is that it
includes suitable choices from manifold implementation options, bias and drift in data,
and the mitigation of black-box properties.
Conclusion
In the current era of increasing digitalization and massive use of FinTech services, digi-
tal P2P payments are being strongly extended as the preferred payment option, mainly
among the young. The rise in P2P payments has been enhanced by the explosion of sure
mobile payment applications as well as the COVID-19 pandemic, which has dramati-
cally limited cash payments to prevent transmission of the virus. Of course, the need to
align individuals´ behaviors with the Sustainable Development Goals also requires the
boosting of digital P2P payments as a way to increase the financial inclusion of many
individuals excluded from traditional financial banking services (Danisman and Tarazi
2020). Indeed, banks and other financial players are currently playing a relevant role in
developing innovative payment services where P2P payments are becoming widespread.
Thus, it is crucial to examine the factors that determine customers’ adoption of mobile
P2P payments to exploit their potential.
This study explores the drivers of mobile P2P adoption by using ML to predict usage
among FinTech disruptions in financial services. Our main conclusion is that ML must
be applied by banks and other financial intermediaries to predict their customers’ adop-
tion of mobile/digital P2P payments. Indeed, to the authors’ knowledge, this approach
has not yet been employed in this field of research. In addition, our findings emphasize
the relevance of usefulness, subjective norms, trust, and user enjoyment in classifying
potential mobile P2P users.
Appendix 1: constructs and measurement items
Perceived ease of use (Venkatesh and Bala 2008)
• Interaction with the system does not require great effort.
• Interaction with the system is straightforward.
• It’s easy to get the system to do what I want.
• The system is useful for making small payments.
• In general, the system is easy to use.

A ntonio et al. Financial Innovation (2024) 10:94 Page 23 of 30
Perceived risk of peer-to-peer mobile payment system (Jarvenpaa et al. 2000; Wake-
field and Whitten 2006)
• Other people can get information about my online transactions if I use this tool.
• There is a high potential for money wasted if I make purchases on the internet/
social networks using this tool.
• There is significant risk in making purchases on the internet/social networks using
this tool.
• I think that making purchases on the internet/social networks with this tool is a
risky choice.
Perceived usefulness of peer-to-peer mobile payment systems (Bhattacherjee and
Premkumar 2004)
• Peer-to-peer mobile payment systems are useful payment methods.
• Using peer-to-peer mobile payment systems makes it easier to handle payments.
• Peer-to-peer mobile payment systems allow quick use of mobile applications.
• In general, peer-to-peer mobile payment systems could be useful for me.
Perceived trust of peer-to-peer mobile payment system (Pavlou 2002)
• I believe the peer-to-peer mobile payment system will keep its promises and com-
mitments.
• The peer-to-peer mobile payment system is trustworthy.
• I would describe peer-to-peer mobile payment system as honest.
• I believe the peer-to-peer mobile payment system is responsible.
• In general, I trust the peer-to-peer mobile payment system.
Personal innovativeness in information technology (Agarwal and Prasad 1998a;
Ramos-de-Luna et al. 2016)
• If I find out about new information technology, I seek ways to experience it.
• I am usually one of the first among my colleagues/peers to explore new informa-
tion technology.
• In general, I am reluctant to try new information technologies.
• I like to try new information technologies.
Subjective norms (Taylor and Todd 1995; Agarwal and Prasad 1998b)
• The people whose opinions I value would approve of me using peer-to-peer
mobile payment system.
• Most of the people I have in mind think that I should use a peer-to-peer mobile
payment system.
• They expect me to use a peer-to-peer mobile payment system.
• The people who are close to me would agree with me in using a peer-to-peer
mobile payment system.

Antonio et al. Financial Innovation (2024) 10:94 Page 24 of 30
Perceived enjoyment of the peer-to-peer mobile payment system (Agarwal and
Karahanna 2000; Rouibah et al. 2016)
• I have fun interacting with this peer-to-peer mobile payment system.
• Using this peer-to-peer mobile payment system provides me with a lot of enjoyment.
• I enjoy using this peer-to-peer mobile payment system.
Loyalty to the bank brand (Gözükara and Çolakoğlu 2016)
• I will not buy other brands if this brand is available at the store.
• I consider myself loyal to this brand.
• This brand would be my first choice.
• I rarely switch from this brand just to try something different.
Perceived quality (Lai et al. 2007)
• When peer-to-peer mobile payment systems promise they will do something, they
do.
• I consider peer-to-peer mobile payment systems to be dependable.
• Peer-to-peer mobile payment systems provide the services they promise when they
are supposed to.
• Peer-to-peer mobile payment systems accurately maintain the statement.
• It is easy to obtain related service information.
• It feels safe to do business with the company.
• The statement is clear and ease to understand.
Appendix 2: criteria for the implementation of algorithms
Linear and quadratic discriminant analysis
We select the threshold p in the grill (0.01, 0.02, …, 0.99), choosing that value which
c
minimises the classification error in a tenfold cross-validation. We obtained the value
0.42. LDA was fitted with R function lda (Venables and Ripley 2002) available in the
MASS library.
Additionally, we also compute the quadratic discrimination analysis (QDA) that
assumes that the covariance matrices are not equal. For this, we use the function qda
from the MASS library (Venables and Ripley 2002). In this case, the cut point obtained
was 0.43.
Logistic regression
We use the step.glm function in R (Venables and Ripley 2002), which strives to com-
pute the maximum likelihood estimators of the n 1 parameters by means of an iterative
+
weighted least squares (IWLS) algorithm, applied under a forward sequential method
based on the Akaike Information Criterion (AIC). The optimal cut-off is searched for in
the grid (0.01, 0.02, …, 0.99), selecting the value minimising the tenfold validation error,
obtaining 0.46.

A  ntonio et al. Financial Innovation           (2024) 10:94  Page 25 of 30
Multilayer perceptron
The size of the hidden layer (H) and the decay parameter (k) are fitted by implementing a
tenfold cross-validation optimisation in a grid defined as {1, 2, …, 40} and {0, 0.01, 0.05,
0.10, …, 2}, respectively. Accordingly, the output of an MLP from a vector of inputs given
by x ,...,x
| 1        | p        |  can be calculated by the following expression: |            |        |                                          |
| -------- | -------- | ----------------------------------------------- | ---------- | ------ | ---------------------------------------- |
| (cid:31) | (cid:30) |                                                 |            |        |                                          |
|          |          | H                                               |            | p      |                                          |
| y        | g W      | 0                                               | W h g v 0h | v ih x | j                                        |
| ˆ        | =       | +                                               |  +        |        |                                        |
|          |          | �= h 1                                          |            | �= j 1 |                                          |
|          |         |                                                 |           |        |                                        |
|          | v ,i     | 0,1,2,...,p,h                                   | 1,2,3,     | ...,H  |                                          |
| where    | ih =     |                                                 | =          |        |  is the synaptic weights for the connec- |
tions b(cid:31)etween the p-sized input and the hidde(cid:30)n layer, and  v ,h 0,1,2, ...,H  is the
h =
synaptic weights for the connections between the hidden no(cid:31)des and the output no(cid:30)de.
We use the function nnet from R (Venables and Ripley 2002), which employs the
Broyden–Fletcher–Goldfarb–Shanno (BFGS) pathway, a quasi-Newton procedure that
seeks to minimise an error criterion which allows a decay term k intending to avoid over-
fitting problems. As shown by Hastie et al. (2009), for classification problems an appro-
priate error function is conditional maximum likelihood (or entropy), that together with
the BFGS procedure solves the problem defined as:
|         | n             |          |                                                             |                  | M                 |
| ------- | ------------- | -------- | ----------------------------------------------------------- | ---------------- | ----------------- |
| min     |               | ylny     | 1 y ln                                                      | 1 y              | k W2              |
|         |               | i ˆ i +  | − i                                                         | −ˆ i             | + i               |
|         | W             |          |                                                             |                  | (cid:28) (cid:27) |
|         | (cid:31)= i i |          |                                                             |                  | (cid:31)= i i     |
|         | (cid:30)      |          | (cid:30) (cid:29) (cid:30)                                  | (cid:29)(cid:29) |                   |
| where W | i (i          | 1,...,M) |  is the be the vector of all the M coefficients of the net. |                  |                   |
=
Support vector machine
Mathematically, SVM can be defined by n training vectors {(X,y)}, i  i i  1,2,...,n, where the
=
multi-dimensional vectors X contain the predictor features and the n labels y 1,1
i i ∈{− }
identify the class of each vector. In accordance with Meyer (2012), we use Radial
Basis Gaussian function kernel function from the library e1071 (Dimitriadou et al. 2022):
2
| K   | (u,v) | exp      | θ u v   |          |     |
| --- | ----- | -------- | ------- | -------- | --- |
|     | =     | =        | − | − | |          |     |
|     |       | (cid:31) |         | (cid:30) |     |
where  the  quadratic  programming  problem  is  solved  implementing  the  following
procedure:
n
1
| min | wtw | C   | δ   |     |     |
| --- | --- | --- | --- | --- | --- |
|     | 2   | +   | i   |     |     |
w,b,δ
i 1
(cid:31)=
| y   | wtω(X)    | b         | 1 δ |     |     |
| --- | --------- | --------- | --- | --- | --- |
|     | i         | i         | i   |     |     |
|     |           | + ≥       | −   |     |     |
| δ   | 0,i       | 1,2,...,n |     |     |     |
|     | i(cid:30) | (cid:29)  |     |     |     |
|     | ≥ =       |           |     |     |     |
Given that the selection of the parameters C and  θ  impact powerfully on the per-
formance of the model, we apply a grid search through the tenfold cross-validation
approach in the set {1, 10, 20, 30, 40, …, 1000} and {0.10, 0.15, 0.20, …, 0.90}, respectively,
by using the function tune.svm in the library e1071.

Antonio et al. Financial Innovation           (2024) 10:94  Page 26 of 30
Classification trees
We employ the rpart package to build CART, which uses the Gini index as an impurity
measure to split the dataset. To avoid the overfitting problem and in accordance with
Maindonald and Braun (2003), we apply the one-standard-deviation rule to determine
the number of terminal nodes.
Bagging
We aggregate the B models by majority voting. To compute bagged tree models (CTBag)
we use the package ipred (Peters and Hothorn 2016). To do so, we consider two values
for B, 50 and 100, selecting the one minimising the tenfold cross-validation classification
error.
Random forest
To implement this ensemble method, we use the package randomForest (Liaw and Wie-
ner 2022). The number of variables were randomly selected through a tenfold cross-vali-
dation search around the default value (mtry  =  square root of the number of predictors),
| namely from mtry  |     |  3 to mtry  |  3. |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- | --- |
|                   |     | −           | +   |     |     |     |
Boosting
AdaBoost, Binominal Boosting, and L2 Boosting were performed by using the function
glmboost, mboost library (Hothorn et al. 2022). To fit the number of iterations (m) of
each model we perform a tenfold cross-validation search of the value minimising the
empirical loss, from 1 to 3000.
This library considers the problem of estimating a real-valued function:
|        | ()                                                 |          | ρ Y,f(X)                           |     |                               |     |
| ------ | -------------------------------------------------- | -------- | ---------------------------------- | --- | ----------------------------- | --- |
|        | f ∗ arg                                            | f() minE |                                    |     |                               |     |
|        | · =                                                | ·        |                                    |     |                               |     |
|        |                                                    |          | (cid:31) (cid:30) (cid:29)(cid:28) |     |                               |     |
|        | ρ                                                  |          |                                    |     | X ,y  , i 1,2,...,n, and hav- |     |
| where  |  is a loss function. We assume n training vectors  |          |                                    |     | i i                           |     |
=
ing selected a base procedure, the generic functional grad(cid:31)ient d(cid:30)escent algorithm is:
[0](
| 1. Initialise f |     | ) with an offset value. Set m |     | 0.  |     |     |
| --------------- | --- | ----------------------------- | --- | --- | --- | --- |
|                 |     | ˆ ·                           |     | =   |     |     |
2. Increase m by 1. Evaluate at f [m 1](X ) the negative gradient of the loss function:
|     |        |       | ˆ −      | i       |     |     |
| --- | ------ | ----- | -------- | ------- | --- | --- |
|     |        | ∂     | 1](Xi),i |         |     |     |
|     | U      | ρ Y,f | f f [m   | 1,...,n |     |     |
|     | i =−∂f |       | = ˆ −    | =       |     |     |
(cid:29)
(cid:31) (cid:30)(cid:29)
(cid:29)
|     |     |     | U   | ,i 1,...,n | X i 1,...,n |     |
| --- | --- | --- | --- | ---------- | ----------- | --- |
3. Fit the base procedure to predict  { i = }  from  i, − =  , obtain-
|             | ing g [m]( | ).      |          |     |          |          |
| ----------- | ---------- | ------- | -------- | --- | -------- | -------- |
|             | ˆ ·        |         |          |     | (cid:31) | (cid:30) |
|             |            | [m]( [m | 1]( [m]( |     |          |          |
| 4. Update f |            | ) f     | − ) vg   | ).  |          |          |
|             | ˆ          | · = ˆ   | · + ˆ    | ·   |          |          |
5. Iterate steps 2–4 until some stopping value M.
We use m 1 since, as shown Bühlman and Hothorn (2007), a small value for the
=
step-length factor does not affect the stability of the model. According to Bühlman and
Hothorn (2007), we use three main methods of boosting procedures to select other ele-
ments of this algorithm. All of them share the base procedure: select the best variable

A ntonio et al. Financial Innovation (2024) 10:94 Page 27 of 30
in a simple linear model in the sense of ordinary least squares fitting. The final model
f ˆ [m]( · ) is a linear combination of the input variables.
Abbreviations:
P2P Peer‑to‑peer
LDA Linear discriminant analysis
LR Logistic regression
IWLS Iterative weighted least squares
AIC Akaike information criterion
MLP Multilayer perceptron
SVM Support vector machine
CART Classification and regression tree
CTBag Bagged tree model
RF Random forests
FS Feature selection
AUC Area under the ROC curve
OOB Out‑of‑bag
GPI Global performance index
SDG Sustainable development goals
Acknowledgements
Not applicable.
Author contributions
ABO: data collecting, methodology, and implementation of algorithms. JLR: conceptualization and original draft. AID:
writing and editing. FLC: conceptualization, theoretical framework and positioned our research. All authors read and
approved the final manuscript.
Funding
Not applicable.
Availability of data and materials
The datasets used and analysed during the current study are available from the corresponding author on reasonable
request.
Declarations
Competing interests
The authors declare that they have no competing interests.
Received: 24 January 2023 Accepted: 2 February 2024
References
Abdullah S, Naved Khan M (2021) Determining mobile payment adoption: a systematic literature search and bibliometric
analysis. Cogent Bus Manag 8(1):1893245
Acker A, Murthy D (2020) What is Venmo? A descriptive analysis of social features in the mobile payment platform. Telem
Inform 52:101429
Agarwal R, Karahanna E (2000) Time flies when you’re having fun: cognitive absorption and beliefs about information
technology usage. MIS Q 24(4):665–694
Agarwal R, Prasad J (1998a) A conceptual and operational definition of personal innovativeness in the domain of infor‑
mation technology. Inf Syst Res 9(2):204–215
Agarwal R, Prasad J (1998b) The antecedents and consequents of user perceptions in information technology adoption.
Decis Support Syst 22(1):15–29
Ajzen I (1991) The theory of planned behaviour. Organ Behav Hum Decis Process 50:179–211
Alonso Robisco A, Carbó Martínez JM (2022) Measuring the model risk‑adjusted performance of machine learning algo‑
rithms in credit default prediction. Financ Innov 8:70. https:// doi. org/ 10. 1186/ s40854‑ 022‑ 00366‑1
Arora N, Kaur PD (2020) A Bolasso based consistent feature selection enabled random forest classification algorithm: an
application to credit risk assessment. Appl Soft Comput 86:105936. https:// doi. org/ 10. 1016/j. asoc. 2019. 105936
Aslam F, Awan TM, Fatima T (2022) Classification of m‑payment users’ behavior using machine learning models. J Financ
Serv Mark 27:264–275. https:// doi. org/ 10. 1057/ s41264‑ 021‑ 00114‑z
Ba S, Pavlou P (2002) Evidence of trust building technology in electronic markets: price premiums and buyer behavior.
MIS Q 26:243–268. https:// doi. org/ 10. 2307/ 41323 32
Bailey AA, Bonifield CM, Arias A, Villegas J (2022) Mobile payment adoption in Latin America. J Serv Mark 36(8):1058–1075
Bajari P, Nekipelov D, Ryan SP, Yang M (2015) Machine learning methods for demand estimation. Am Econ Rev
105(5):481–485

Antonio et al. Financial Innovation (2024) 10:94 Page 28 of 30
Belanche D, Guinalíu M, Albás P (2022) Customer adoption of P2P mobile payment systems: the role of perceived risk.
Telemat Inform 72:101851. https:// doi. org/ 10. 1016/j. tele. 2022. 101851
Bhattacherjee A, Premkumar G (2004) Understanding changes in belief and attitude toward information technology
usage: a theoretical model and longitudinal test. MIS Q 28(2):229–254
Bishop CM (2006) Pattern recognition and machine learning. Springer, Berlin
Bizum (2022) https:// bizum. es/ datos/. Accessed 21 Mar 2022
Boulesteix AL, Janitza S, Hapfelmeier A, Van Steen K, Strobl C (2015) Letter to the editor: on the term “interaction” and
related phrases in the literature on random forests. Brief Bioinform 16(2):338–345
Breiman L (1996) Bagging predictors. Mach Learn 24:123–140. https:// doi. org/ 10. 1007/ BF000 58655
Breiman L (2001) Random forests. Mach Learn 45(1):5–32
Bühlman P, Hothorn T (2007) Boosting algorithms: regularization, prediction and model fitting. Stat Sci 22:477–505
Cao L, Philip SY, Kumar V (2015) Nonoccurring behavior analytics: a new area. IEEE Intell Syst 30(6):4–11
Chan JY, Leow SM, Bea KT, Cheng WK, Phoong SW, Hong ZW, Chen YL (2022) Mitigating the multicollinearity problem
and its machine learning approach: a review. Mathematics 10(8):1283. https:// doi. org/ 10. 3390/ math1 00812 83
Chen RC, Dewi C, Huang SW, Caraka RE (2020) Selecting critical features for data classification based on machine learning
methods. J Big Data. https:// doi. org/ 10. 1186/ s40537‑ 020‑ 00327‑4
Cui G, Wong ML, Lui HK (2016) Machine learning for direct marketing response models: Bayesian networks with evolu‑
tionary programming. Manag Sci 52(4):597–612
Dahlberg T, Mallat N, Ondrus J, Zmijewska A (2008) Past, present and future of mobile payments research: a literature
review. Electron Commer Res Appl 7(2):165–181
Danisman GO, Tarazi A (2020) Financial inclusion and bank stability: evidence from Europe. Eur J Finance 26(18):1842–
1855. https:// doi. org/ 10. 1080/ 13518 47X. 2020. 17829 58
Davenport T, Guha A, Grewal D, Bressgott T (2020) How artificial intelligence will change the future of marketing. J Acad
Mark Sci 48(1):24–42. https:// doi. org/ 10. 1007/ s11747‑ 019‑ 00696‑0
Davis FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Q
13:319–340
Davis FD, Bagozzi RP, Warshaw PR (1989) User acceptance of computer technology: a comparison of two theoretical
models. Manag Sci 35(8):982–1003
Dennehy D, Sammon D (2015) Trends in mobile payments research: a literature review. J Innov Manag 3(1):49–61
Dewi C (2019) Random forest and support vector machine on features selection for regression analysis. Int J Innov Com‑
put Inf Control 15(6):2027–2037
Dimitriadou E, Hornik K, Leisch F, Meyer D, Weingessel D (2022) e1071: misc functions of the department of statistics
(e1071) TU Wien. R package version 1.6. https:// cran.r‑ proje ct. org/ web/ packa ges/ e1071/ index. html
European Central Bank (2022) Estadísticas sobre pagos: 2021. www. bce. es
Fahimifar S, Mousavi K, Mozaffari F, Ausloos M (2022) Identification of the most important external features of highly cited
scholarly papers through 3 (i.e., Ridge, Lasso, and Boruta) feature selection data mining methods. Qual Quant.
https:// doi. org/ 10. 1007/ s11135‑ 022‑ 01480‑z
Fishbein M, Ajzen I (1975) Belief attitude, intention, and behavior: an introduction to theory and research. Reading,
Addison‑Wesley, M.A.
Fishbein M, Ajzen I (1977) Belief, attitude, intention and behavior: an introduction to theory and research. Philos Rhetor
10(2):130–132
Flavián C, Guinaliu M, Lu Y (2020) Mobile payments adoption–introducing mindfulness to better understand consumer
behavior. Int J Bank Mark 38(7):1575–1599
Frame WS, Wall LD, White LJ (2018) Technological change and financial innovation in banking: some implications for
fintech. FRB Atlanta, working paper no. 2018‑11
Freund Y (1995) Boosting a weak learning algorithm by majority. Inf Comput 121(2):256–285
Friedman J, Hastie T, Tibshirani R (2000) Additive logistic regression: a statistical view of boosting (with discussion). Ann
Stat 28:337–407
Gomber P, Koch JA, Siering M (2017) Digital finance and FinTech: current research and future research directions. J Bus
Econ 87:537–580. https:// doi. org/ 10. 1007/ s11573‑ 017‑ 0852‑x
Gefen D, Karahanna E, Straub DW (2003) Trust and TAM in online shopping: an integrated model. MIS Quart 27(1):51–90
Gözükara İ, Çolakoğlu N (2016) A research on generation Y students: brand innovation, brand trust and brand loyalty. Int
J Bus Manag Econ Res 7(2):603–611
Guo M, Zhang Q, Liao X, Chen FY, Zeng DD (2021) A hybrid machine learning framework for analyzing human decision‑
making through learning preferences. Omega 101:102263. https:// doi. org/ 10. 1016/j. omega. 2020. 102263
Hagenauer J, Helbich MA (2017) Comparative study of machine learning classifiers for modeling travel mode choice.
Expert Syst Appl 78:273–282
Hastie T, Tibshirani R, Friedman J (2009) The elements of statistical learning: data mining, inference, and prediction.
Springer, New York
Hernández‑Murillo R, Llobet G, Fuentes R (2010) Strategic online banking adoption. J Bank Finance 34(7):1650–1663
Higueras‑Castillo E, Liébana‑Cabanillas FJ, Villarejo‑Ramos ÁF (2023) Intention to use e‑commerce vs physical shopping.
Difference between consumers in the post‑COVID era. J Bus Res 157:113622
Hothorn T, Bühlmann P, Kneib T, Schmid M, Hofner B (2022) mboost: model‑based boosting. R package version 2.1‑2.
https:// cran.r‑ proje ct. org/ web/ packa ges/ mboost/ mboost. pdf
Huang Y (2021) Retail fintech payments: facts, benefits, challenges, and policies
Huang D, Liu X, Lai D, Li Z (2019) Users and non‑users of P2P accommodation: differences in perceived risks and behavio‑
ral intentions. J Hosp Tour Technol 10(3):369–382
Insider Intelligence (2022) The payment industry’s biggest trends in 2022—and the pandemic’s impact on digitization in
the payments landscape. https:// www. busin essin sider. com/ payme nts‑ ecosy stem‑ report. Accessed 21 Mar 2022
Irimia‑Diéguez A, Velicia‑Martín F, Aguayo‑Camacho M (2023) Predicting Fintech innovation adoption: the mediator role
of social norms and attitudes. Financ Innov. https:// doi. org/ 10. 1186/ s40854‑ 022‑0 0434‑6

A ntonio et al. Financial Innovation (2024) 10:94 Page 29 of 30
Jarvenpaa SL, Tractinsky N, Vitale M (2000) Consumer trust in an internet store information technology and management.
J Inf Syst 12(1):41–48
Jun J, Cho I, Park H (2018) Factors influencing continued use of mobile easy payment service: an empirical investigation.
Total Qual Manag Bus Excell 29(9–10):1043–1057
Kalinic Z, Marinkovic V, Molinillo S, Liébana‑Cabanillas F (2019) A multi‑analytical approach to peer‑topeer mobile pay‑
ment acceptance prediction. J Retail Consum Serv 49:143–153. https:// doi. org/ 10. 1016/j. jretc onser. 2019. 03. 016
Kaplan A, Haenlein M (2019) Siri, Siri, in my hand: Who’s the fairest in the land? On the interpretations, illustrations, and
implications of artificial intelligence. Bus Horiz 62(1):15–25. https:// doi. org/ 10. 1016/j. bushor. 2018. 08. 004
Kou G, Olgu Akdeniz Ö, Dinçer H, Yüksel S (2021) Fintech investments in European banks: a hybrid IT2 fuzzy multidimen‑
sional decision‑making approach. Financ Innov 7(1):1–28
Lai F, Hutchinson J, Li D, Bai C (2007) An empirical assessment and application of SERVQUAL in mainland China’s mobile
communications industry. Int J Qual Reliab Manag 24(3):244–262
LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521:436–444. https:// doi. org/ 10. 1038/ natur e14539
Lee VH, Hew JJ, Leong LY, Tan GWH, Ooi KB (2020) Wearable payment: a deep learning‑based dual‑stage SEM‑ANN analy‑
sis. Expert Syst Appl 157:113477. https:// doi. org/ 10. 1016/j. eswa. 2020. 113477
Leong LY, Hew JJ, Wong LW, Lin B (2022) The past and beyond of mobile payment research: a development of the mobile
payment framework. Internet Res 32(6):1757–1782
Lewis BR, Soureli M (2006) The antecedents of consumer loyalty in retail banking. J Consum Behav 5(1):15–31
Li L, Freeman G, Wohn DY (2021) The Interplay of financial exchanges and offline interpersonal relationships through
digital peer‑to‑peer payments. Telemat Inform. https:// doi. org/ 10. 1016/j. tele. 2021. 101671
Liaw A, Wiener M (2022) Classification and regression by random forest. R News 2:18–22
Liébana‑Cabanillas F, Sánchez‑Fernández J, Muñoz‑Leiva F (2014) Role of gender on acceptance of mobile payment. Ind
Manag Data Syst 114(2):220–240
Liébana‑Cabanillas F, Ramos de Luna I, Montoro‑Ríos F (2017) Intention to use new mobile payment systems: a compara‑
tive analysis of SMS and NFC payments. Econ Res‑Ekonomska Istraživanja 30(1):892–910
Liébana‑Cabanillas F, Molinillo S, Ruiz‑Montañez M (2019) To use or not to use, that is the question: analysis of the deter‑
mining factors for using NFC mobile payment systems in public transportation. Technol Forecast Soc Change
139:266–276
Liébana‑Cabanillas F, Singh N, Kalinic Z, Carvajal‑Trujillo E (2021) Examining the determinants of continuance intention
to use and the moderating effect of the gender and age of users of NFC mobile payments: a multi‑analytical
approach. Inf Technol Manag 22:133–161. https:// doi. org/ 10. 1007/ s10799‑ 021‑ 00328‑6
Liébana‑Cabanillas F, Kalinic Z, Luna IRD, Marinkovic V (2022a) A holistic analysis of near field communication mobile pay‑
ments: an empirical analysis. Int J Mob Commun 20(6):703–726
Liébana‑Cabanillas F, Muñoz‑Leiva F, Molinillo S, Higueras‑Castillo E (2022b) Do biometric payment systems work during
the COVID‑19 pandemic? Insights from the Spanish users’ viewpoint. Financ Innov 8(1):1–25
Ma S, Fildes R (2020) Forecasting third‑party mobile payments with implications for customer flow prediction. Int J Fore‑
cast 36(3):739–760. https:// doi. org/ 10. 1016/j. ijfor ecast. 2019. 08. 012
Madani A, Ong JR, Tibrewal A, Mofrad MR (2018) Deep echocardiography: data‑efficient supervised and semi‑supervised
deep learning towards automated diagnosis of cardiac disease. Npj Digit Med 1:59. https:// doi. org/ 10. 1038/
s41746‑ 018‑ 0065‑x
Maindonald J, Braun J (2003) Data analysis and graphics using R. An examplebased approach. Cambridge University
Press, Cambridge, Cambridge
Martín A, Fernández‑Isabel A, Martín de Diego I, Beltrán M (2021) A survey for user behavior analysis based on machine
learning techniques: current models and applications. Appl Intell 51:6029–6055. https:// doi. org/ 10. 1007/
s10489‑ 020‑ 02160‑x
Meyer D (2012) Support vector machines. The interface to libsvm in packagee 1071. Available at svmdoc.pdf
Migliore G, Wagner R, Cechella FS, Liébana‑Cabanillas F (2022) Antecedents to the adoption of mobile payment in China
and Italy: an integration of UTAUT2 and innovation resistance theory. Inf Syst Front 24:1–24
Moorthy K, Chun T’ing L, Chea Yee K, Wen Huey A, Joe In L, Chyi Feng P, Jia Yi T (2020) What drives the adoption of mobile
payment? A Malaysian perspective. Int J Finance Econ 25(3):349–364
Nasir A, Shaukat K, Khan KI, Hameed IA, Alam TM, Luo S (2020) What is core and what future holds for blockchain tech‑
nologies and cryptocurrencies: a bibliometric analysis. IEEE Access 9:989–1004
Nasir A, Shaukat K, Iqbal Khan K, Hameed A, I., Alam, T. M., & Luo, S. (2021) Trends and directions of financial technology
(Fintech) in society and environment: a bibliometric study. Appl Sci 11(21):10353
Nguyen DK, Sermpinis G, Stasinakis C (2022) Big data, artificial intelligence and machine learning: a transformative sym‑
biosis in favour of financial technology. Eur Financ Manag. https:// doi. org/ 10. 1111/ eufm. 12365
Panetta IC, Leo S, Delle Foglie A (2023) The development of digital payments–past, present, and future–from the litera‑
ture. Res Int Bus Finance 64:101855
Patil PP, Dwivedi YK, Rana NP (2017) Digital payments adoption: an analysis of literature. Conference on e‑Business,
e‑Services and e‑Society. Springer, Cham, pp 61–70
Pavlou PA (2002) Institution‑based trust in interorganizational exchange relationships: the role of online B2B market‑
places on trust formation. J Strateg Inf Syst 11(3–4):215–243
Peters A, Hothorn T (2016) Improved predictive models by indirect classification and bagging for classification, regression
and survival problems as well as resampling based estimators of prediction error. https:// cran.r‑ proje ct. org/ web/
packa ges/ ipred/ index. html
Petropoulos A, Siakoulis V, Stavroulakis E, Vlachogiannakis NE (2020) Predicting bank insolvencies using machine learning
techniques. Int J Forecast 36(3):1092–1113. https:// doi. org/ 10. 1016/j. ijfor ecast. 2019. 11. 005
Rafdinal W, Senalasari W (2021) Predicting the adoption of mobile payment applications during the COVID‑19 pandemic.
Int J Bank Mark 39(6):984–1002
Ramos‑de‑Luna I, Montoro‑Ríos F, Liébana‑Cabanillas F (2016) Determinants of the intention to use NFC technology as a
payment system: an acceptance model approach. IseB 14(2):293–314

Antonio et al. Financial Innovation (2024) 10:94 Page 30 of 30
Rouibah K, Lowry PB, Hwang Y (2016) The effects of perceived enjoyment and perceived risks on trust formation and
intentions to use online payment systems: new perspectives from an Arab country. Electron Commer Res Appl
19:33–43. https:// doi. org/ 10. 1016/j. elerap. 2016. 07. 001
Schapire RE, Freund Y, Bartlett P, Lee WS (1998) Boosting the margin: a new explanation for the effectiveness of voting
methods. Ann Stat 26(5):1651–1686
Selvamuthu D, Kumar V, Mishra A (2019) Indian stock market prediction using artificial neural networks on tick data.
Financ Innov 5:16. https:// doi. org/ 10. 1186/ s40854‑ 019‑ 0131‑7
Shaikh A, Liébana‑Cabanillas F, Glavee‑Geo R (2023) Factors inhibiting the adoption intention of digital payment plat‑
forms. In: Responsible finance and digitalization. Routledge, pp 140–154
Sheth J, Kellstadt CH (2021) Next frontiers of research in data driven marketing: Will techniques keep up with data tsu‑
nami? J Bus Res 125:780–784. https:// doi. org/ 10. 1016/j. jbusr es. 2020. 04. 050
Singh J, Sirdeshmukh D (2000) Agency and trust mechanisms in consumer satisfaction and loyalty judgments. J Acad
Mark Sci 28:150–167. https:// doi. org/ 10. 1177/ 00920 70300 281014
Skinner BF (1953) Science and human behavior. Simon and Schuster, New York, p 92904
Speiser JL, Miller ME, Tooze J, Ip E (2019) A comparison of random forest variable selection methods for classification
prediction modeling. Expert Syst Appl 134:93–101. https:// doi. org/ 10. 1016/j. eswa. 2019. 05. 028
Tamayo B (1999) Nuevos campos para la innovación: Internet y el comercio electrónico de bienes y servicios. Recuper‑
ado de www. navac tiva. com/ es/ desca rgas/ pdf/ atic/ cotec. pdf
Taylor S, Todd PA (1995) Understanding information technology usage: a test of competing models. Inf Syst Res
6(2):144–176
Thai HT (2022) Machine learning for structural engineering: a state‑of‑the‑art review. Structures 38:448–491. https:// doi.
org/ 10. 1016/j. istruc.2 022. 02. 003
Thakor AV (2020) Fintech and banking: What do we know? J Financ Intermed 41:100883
Tounekti O, Ruiz‑Martínez A, Skarmeta Gomez AF (2022) Research in electronic and mobile payment systems: a biblio‑
metric analysis. Sustainability 14(13):7661
Türker C, Altay BC, Okumuş A (2022) Understanding user acceptance of QR code mobile payment systems in Turkey: an
extended TAM. Technol Forecast Soc Change 184:121968
Upadhyay N, Upadhyay S, Abed SS, Dwivedi YK (2022) Consumer adoption of mobile payment services during COVID‑19:
extending meta‑UTAUT with perceived severity and self‑efficacy. Int J Bank Mark 40(5):960–991
Vanini P, Rossi S, Zvizdic E, Domenig T (2023) Online payment fraud: from anomaly detection to risk management. Financ
Innov 9:66. https:// doi. org/ 10. 1186/ s40854‑ 023‑ 00470‑w
Vellido A, Lisboa PJG, Vaughan J (1999) Neural networks in business: a survey of applications (1992–1998). Expert Syst
Appl 17:51–70. https:// doi. org/ 10. 1016/ S0957‑ 4174(99) 00016‑0
Venables WN, Ripley BD (2002) Modern applied statistics with S, 4th edn. Springer, New York, NY
Venkatesh V, Bala H (2008) Technology acceptance model 3 and a research agenda on interventions. Decis Sci
39(2):273–315
Venkatesh V, Davis FD (2000) A theoretical extension of the technology acceptance model: four longitudinal field studies.
Manag Sci 46(2):186–204
Venkatesh V, Morris MG, Davis GB, Davis FD (2003) User acceptance of information technology: toward a unified view.
MIS Q 27:425–478
Venkatesh V, Thong J, Xu X (2012) Consumer acceptance and use of information technology: extending the unified
theory of acceptance and use of technology. MIS Q 36(1):157–178
Visconti‑Caparrós JM, Campos‑Blázquez JR (2022) The development of alternate payment methods and their impact on
customer behavior: the Bizum case in Spain. Technol Forecast Soc Change 175:121330
Wakefield RL, Whitten D (2006) Examining user perceptions of third‑party organizations credibility and trust in an
e‑retailer. J Organ End User Comput (JOEUC) 18(2):1–19
Weisberg S (2005) Applied linear regression, vol 528. Wiley, Hoboken
Witten IH, Frank E (2005) Data mining: practical machine learning tools and techniques, 2nd edn. Morgan Kaufmann
Publishers, Massachusetts
Wu R‑Z, Lee J‑H, Tian X‑F (2021) Determinants of the intention to use cross‑border mobile payments in Korea among
Chinese tourists: An integrated perspective of UTAUT2 with TTF and ITM. J Theor Appl Electron Commer Res
16(5):1537–1556
Wu Y, Zhang W, Shen J, Mo Z, Peng Y (2018) Smart city with Chinese characteristics against the background of big data:
idea, action and risk. J Clean Prod 173:60–66
Xiong T, Ma Z, Li Z, Dai J (2022) The analysis of influence mechanism for internet financial fraud identification and user
behavior based on machine learning approaches. Int J Syst Assur Eng Manag 13(3):996–1007. https:// doi. org/ 10.
1007/ s13198‑ 021‑ 01181‑0
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.