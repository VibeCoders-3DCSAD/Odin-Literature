---
conversion_metadata:
  converted_at: "2026-07-22T13:26:08Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ghonaim & El-Sharawy.pdf"
  source_pdf_sha256: "b458e4cdcf67395272dd6ad896d550b6cd037c31f0fcb4ce6dcd08a81fe83978"
  page_count: 13
  markdown_char_count: 125361
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Theoretical and Applied Research, 2025, Vol. 4, No. 2, 840-852

International Journal of Theoretical and Applied Research (IJTAR) 
ISSN: 2812-5878

Homepage: https://ijtar.journals.ekb.eg

Original article  
An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network

Wafaa A. Ghonaim*, Enas E. El-Sharawy

Mathematics Department, Computer Science Division, Faculty of Science, Al-Azhar University (Girls), Cairo 11651, 
Egypt. 
ARTICLE INFO

ABSTRACT

Received   02/10/2025 
Revised     16/11/2025 
Accepted   20/11/2025

Keywords

Budget managemen 
Mobile application 
Artificial intelligence  
Recurrent neural network

Budgeting is important for both people and businesses to manage their finances, save, 
stay out of debt, and be ready for financial emergencies. This paper aims to propose an 
intelligent mobile application to reduce financial risks and support better ways of saving 
and investing through intelligent budgeting. A lot of budgeting applications lacked Arabic 
language support and AI-based forecasting capabilities. This gap is addressed by the de-
velopment of an application that supports English and Arabic speakers through a Recurrent 
Neural Network (RNN) for enhanced financial and management capabilities. The model 
was trained on a real-world financial dataset, preprocessing it, and transforming its data. 
The results demonstrated that the model was highly accurate in the classification of finan-
cial  transactions  based  on  the  level  of  risk.  The  application  was  tested  on  new  data;  it 
reached an overall accuracy of 97.45%. Precision, recall, and F1 measures are all higher 
than 0.97 for each of the risk categories: low, medium, and high. These results validate the 
reliability of the system, particularly in detecting critical low- and high-risk behaviors, and 
its capacity to help users make safer and more informed decisions regarding their finances.

Graphical abstract

1.  Introduction

Budgeting skills should be applied to individuals and 
families so that everyone can manage their finances effec-
tively.  These  skills  demand  much  discipline  and  self-

awareness, and without these skills, the  person may face 
some financial difficulties, which in the long run may in-
fluence the quality of life and achievement of their dreams. 
The  economic  challenges  today  are  very  different,  and

∗ Corresponding author

E-mail address: dr.wafaaghonaim@azhar.edu.eg

DOI: 10.21608/IJTAR.2025.427658.1148

---

<!-- PAGE 2 -->

Ghonaim et al.

needs  are  growing  in  the  modern  world.  People  require 
smart and effective ways and means to manage the availa-
ble resources to provide a secure and strong financial foun-
dation  [1].  The  reality  of  life  is  that  living  has  become 
costly, and the economic stresses call for people to learn 
how to manage their scarce resources. All budgeting skills 
are no longer considered luxuries but a necessity for living 
a  comfortable  and  secure  future  life.  Personal  attributes 
such as financial literacy, mental budgeting, and self-con-
trol  are  good  in  that  they  create  a  link  between  achieve-
ments in the workplace. A study suggests that people with 
high financial literacy have better financial health than oth-
ers. In other words, understanding the basic aspects of fi-
nances, personal planning, saving, and investing can help 
enhance one’s finances [2]. Budgeting has undergone sig-
nificant changes over the years with the  advancement of 
technology. Traditionally, budgeting began with a hierar-
chical  process  based  on  top-down  instructions,  which 
made  it  difficult  to  adapt  to  changes.  Technological  ad-
vancements have brought about many changes in budget 
management,  with  many  software  solutions  being  intro-
duced  to  plan,  predict  financial  crises,  and  evaluate  user 
spending [3].

This paper proposes a budget management mobile appli-
cation  based  on  a  Recurrent  Neural  Network  (RNN), 
which belongs to a family of neural architectures specifi-
cally designed for sequential and temporal data processing. 
Despite their usefulness in areas such as RNNs are charac-
terized  by  recurrent  connections  that  enable  information 
from previous time steps to influence current outputs, al-
lowing the model to capture contextual and time-depend-
ent patterns effectively [4]. Although RNNs have proven 
effective in domains such as natural language processing, 
speech modelling, and time-series forecasting, they often 
face  training  challenges,  particularly  vanishing  and  ex-
ploding gradient problems [5, 6]. To address these limita-
tions,  advanced  architectures  such  as  Long  Short-Term 
Memory  (LSTM)  [7]  and  Gated  Recurrent  Units  (GRU) 
[8] have been developed. These architectures enhance the 
network’s ability to learn and retain long-term dependen-
cies, often outperforming traditional RNNs in practical ap-
plications [6]. The proposed mobile application enables us-
ers to manage their finances intelligently through a user-
friendly  and  intuitive  interface.  It  provides  multiple  ser-
vices,  including recording expenditures across categories 
such  as  necessities,  loans,  and  discretionary  spending 
within a monthly adjustable budget. The application tracks 
both daily and monthly expenditures across all categories 
and generates detailed reports that help users monitor their 
financial status and spending patterns. One of the most im-
portant tools provided in the application is the opportunity 
to analyze spending data and even foresee the potential cri-
ses  that  might  occur due  to  spending and changes  in  in-
come. Thus, the proposed Budget Management Applica-
tion  serves  as  a  comprehensive,  user-oriented  tool  de-
signed to  help  individuals enhance their budgeting skills 
and  financial  awareness.  By  integrating intelligent,  tech-
nology-driven  solutions,  the  system  empowers  users  to 
build long-term financial literacy and make informed, sus-
tainable  financial  decisions.  These  features  make  the

841

application a reliable and effective partner in achieving fi-
nancial stability and long-term economic well-being.

Many  applications  can  help  with  money  management, 
but  there  is  no  comprehensive  application  that  provides 
several important features. It’s crucial to develop a com-
prehensive application that is equipped with the latest tech-
nologies and offers various languages to engage with var-
ious segments. For example, most of them are not in Ara-
bic. This requires the urgency of developing an Arabic-lan-
guage application with extensive customization options to 
accommodate  various  cultures  and  lifestyles.  Although 
there are a few applications that use AI to predict financial 
crises or their imminence, they do not offer personal plans 
and purchase recommendations that fit the user's  budget, 
nor do they provide the user with an alert when the trans-
action exceeds the budget, nor give a retirement financial 
plan. Thus, this is a very serious gap as it is challenging for 
users to reach their financial objectives in a way that works 
for them. This suggests that these features were not given 
enough consideration when  earlier  applications  were  de-
veloped. Therefore, this project proposes a solution by de-
veloping a new application that combines the features from 
earlier versions with several fundamental features in each 
application  to  give  users  the  best  possible  assistance  in 
managing their financial affairs and reaching their finan-
cial objectives. The remainder of this paper is structured as 
follows: Section 2 presents many different budget manage-
ment applications and papers. Section 3 proposes the ar-
chitecture  of  the  proposed  application.  In  Section  4,  we 
present the experimental results and discussion of the pro-
posed  application.  Finally,  Section  5  provides  a  conclu-
sion.

2.  Related works

In this section, the literature review will be presented. It 
is based on two main categories:  Research papers and ap-
plication papers, as shown in Fig. 1.

Fig. 1. Literature Review Taxonomy

2.1 Research Papers

In  [9]  involved  a  methodology  was  involved  that  ana-
lyzed  current  financial  industry  practices  and  targeted

---

<!-- PAGE 3 -->

842 
customers  to  understand  spending  patterns  with  reduced 
spending.  It  is  helpful  for  those  building  systems  or  im-
proving  financial  decision-making  methods.  It  tries  to 
solve the problem of poor financial management and plan-
ning, lack of knowledge, and inaccurate expense tracking. 
The  authors use knowledge and technology to develop a 
financial management tool that provides clients with criti-
cal insights, financial plans, and monthly income and ex-
pense analysis. In [10] solved the problem of how artificial 
intelligence  can  assist  in  improving  the  allocation  of  the 
public budget. The technology that the authors applied is 
the employment of a hybrid AI approach involving a mul-
tilayer perception and multi-objective genetic algorithm to 
analyze the  effects of various public spending categories 
on  inflation,  GDP,  and  income  inequality.  It  uses  real-
world economic data to predict the outcome of scenarios 
that result from different budget allocations.

In [11] authors focused on considering the problem of 
predicting  fiscal  crises  and  the  limitations  of  traditional 
econometric  models  in  accurately  forecasting  such  rare 
events.  The  main  method  proposed  is  applying  machine 
learning  models:  random  forest,  gradient  boosted  trees, 
and elastic net, through which the investigator investigates 
the  interactions  of  the  economic,  political,  and  demo-
graphic  predictors  while  addressing  overfitting  through 
out-of-sample validation and data pooling.  In the study of 
[12]  authors  discussed  applying  machine  learning  tech-
niques  to  improve  financial  forecasting  and  planning. 
Much focus has gone to supervised learning in predicting 
financial outcomes based on historical data; unsupervised 
learning, mainly for pattern recognition; and reinforcement 
learning,  especially  for  adaptive  financial  decision-mak-
ing. It was found that machine learning is good at finding 
patterns in financial data, but it struggles to explain why 
those patterns happen, which is important for making de-
cisions.

In [13] authors focused on considering the problem of 
forecasting stock price movements within the LQ45 finan-
cial sector index and the limitations of traditional forecast-
ing models in capturing the highly dynamic and nonlinear 
nature of financial markets. The main results of this paper 
show  that  the  LSTM-based  approach  significantly  im-
proves the forecasting accuracy, especially for BBCA and 
BMRI stocks, which showed the lowest mean relative ab-
solute  error  (MAPE)  values,  while  other  stocks  showed 
reasonable forecasting results.

2.2 Application Papers

In [14] authors tried to solve the problem of people's poor 
personal  financial  planning  that  leads  to  an  inability  to 
meet  needs.  The  authors  use  existing  technology-based 
methods  to  create  a  mobile-based  application  called 
Money Empire. Money Empire has many features that dis-
tinguish it which are it is a mobile app-based smart assis-
tant for personal finance management. This application au-
tomates finance management by extracting transaction de-
tails from banking SMS alerts and expense details from in-
voices.  In  [15]  authors  solve  the  problem  of  people's

International Journal of Theoretical and Applied Research, 2025, 4(2) 
inability to manage money properly and not understanding 
the financial risks that a person may face due  to making 
some wrong decisions. The authors used existing technol-
ogy-based approaches, such as Google Cloud Vision API 
and  One  Signal  API,  and  integrated  them  into  a  mobile-
based application called Manage on Money. The applica-
tion received great satisfaction, which helped users man-
age money.

In [16] authors discussed the problem for people who do 
not  have  enough  financial  knowledge  to  manage  their 
money and track their daily income. The authors used the 
iterative development methodology, Android Studio to de-
sign the application interfaces, and Firebase for the data-
base.  The project  was  developed  with  an  object-oriented 
approach.  The  application  manages  money  and  analyzes 
cash flow effectively. The main results of this paper are an 
application that manages money, analyzes cash flow effec-
tively, helps users enter and track their spending, and cre-
ates financial plans for retirement and others. In [17] au-
thors developed a mobile application for personal finances, 
offering a set of services for budget tracking, income and 
expense management, and report generation. The authors 
used technologies like Java, Gradle 8, and Microsoft SQL 
to  create  an  Android  application,  validated  through  beta 
testing with real users, including those with visual impair-
ments. As a result, a mobile application was developed that 
offers a user-friendly interface and useful functionalities. 
In [18], the author’s aimed to create and show a prototype 
for  a  mobile  application  that  would  manage  personal  fi-
nances, with an emphasis on goal setting, needs organiza-
tion, and budgeting. The procedure was broken down into 
two phases: content realization, which realized all the fea-
ture lists and specifications from the first phase, and con-
cept formulation, which resulted in an application design 
with a set of needs and features. Consequently, two outputs 
were generated from the work: use case and class diagrams 
from the Content Realization phase and a feature list from 
the  Concept  Formulation  phase  that  included  Getting 
Started, Details for Every Function, Goal Setting, Budget-
ing, Organize Needs, Type of Expense, Indicator for Budg-
eting, Transaction History, and Reminder.

In [19], the authors developed the Cash Save app as an 
effective way to manage money, using a prototyping ap-
proach with continuous improvements based on user feed-
back. The app passed 78% of the test cases, demonstrating 
its  overall  efficiency,  but  it  faced  challenges  such  as  the 
history tracking feature failing in some cases, requiring ad-
ditional improvements. In [20] authors developed an An-
droid application for personal finance management, specif-
ically targeted at students. They used the Waterfall Model 
to design the application, which tracked, categorized, and 
generated  expense  reports  with  customizable  daily, 
weekly, and monthly options. The application effectively 
met its intended purpose, but the limitations of the Water-
fall Model, particularly its lack of adaptability, were noted. 
Iterative  methods  were  suggested  to  improve  flexibility 
during the development process. Compared to similar ap-
simplicity  while 
plications,

this  one  emphasized

---

<!-- PAGE 4 -->

Ghonaim et al.

integrating AI-driven financial advice to provide personal-
ized recommendations. In [21] identified a challenge was 
identified in managing personal finances in today's digital 
world,  where  using  multiple  accounts  and  traditional  re-
cording methods can increase financial stress. To address 
this  issue,  they  introduced  MyFinanceAI,  an  intelligent 
system that combines deep neural networks, reinforcement 
learning, and advanced AI technologies. The system fea-
tures a secure data collection layer, a financial pattern anal-
ysis engine, and predictive models for analyzing time se-
ries data. It provides personalized recommendations with 
40 % more accuracy thanks to its intelligent recommenda-
tion  engine.  The  research  showed  that  MyFinanceAI  re-
duced financial stress by 43% and increased monthly sav-
ings by 22%. Additionally, 78% of users achieved their fi-
nancial goals for debt reduction and savings, and expense 
projection accuracy improved by 30%.

2.3 Applications with Arabic Interfaces

The Wafeer application [22] is an application that helps 
people  make  decisions  on  budget  and  save  money  and 
eliminate wastage and other expenses that are not neces-
sary. A mobile application that can work on Android and 
iOS. The main techniques and methodology applied to pro-
vide several services such as Expense tracking, preparing 
a personal budget, Expense analysis, and financial alerts, 
Daily, monthly, and yearly analysis of operations, Chart of 
spending rate for 6 months and specific periods in the ap-
plication, make statistics on your categories and purchases 
through stores, Savings goals are determined by the per-
son.

In the Wise Budget application [23], which is an appli-
cation that helps people to effectively monitor their spend-
ing and optimize savings. Available on both Android and 
iOS, it provides a lot of features It contains comprehensive 
budget management, as it requires entering the monthly in-
come to determine a budget, accurately tracking expenses 
and  financial  reports  by  providing  illustrative  charts and 
tables, The ability to add debts or loans to the application 
to  facilitate  budget  management,  Payments  are  entered 
manually and no pictures or invoices are inserted. In the 
Wallet  app  [24],  an  app  designed  to  help  users  monitor 
their  income,  expenses,  and  budgets  to  improve  their  fi-
nancial  management,  it  offers  features  such  as  financial 
data  categorization, graphical reports, manual data  entry, 
and bank synchronization. The app relies on features that 
make tracking expenses easy, helping users adopt better fi-
nancial habits. However, the app requires time-consuming 
manual entries and does not provide personalized financial 
guidance. Additionally, its analytical features are consid-
ered too simple for experienced users.

The  Amwaly  application  [25]  is  an  application  that 
helps people solve several problems, such as the ability to 
organize  personal  money,  monitoring  spending  and  en-
couraging savings available on Android and iOS. The main 
techniques and methodologies are applied to provide sev-
eral services. Among the advantages provided by the ap-
plication  are  entering  income  and  determining  expenses

843

and  debts,  if  any,  and  then  dividing  the  expenses  into 
monthly  requirements,  daily  and  monthly  expense  keep-
ing, offering notification of payment days and due charges, 
displaying financial reports to clarify spending habits, and 
analyzing  the  budget.  In  the  Masareef  application  [26], 
which is an application that manages money through budg-
eting, account synchronization, and spending tracking, the 
application  integrates  with  bank  accounts,  e-wallets,  and 
cryptocurrencies,  allowing  users  to  categorize  expenses 
and generate detailed and accurate reports. It also relies on 
manual data entry to categorize expenses and prepare re-
ports, but some advanced features require a premium sub-
scription  to  access  them.  It  is  available  on  smartphones 
only  and  provides  periodic  updates  to  improve  perfor-
mance  and  increase  efficiency.  The  application  has  re-
ceived positive reviews due to its comprehensive features 
that  help  users  improve  their  budget  and  increase  their 
awareness of their spending patterns.

In the money lover application [27], which is an appli-
cation that helps users to easily keep track of their finances, 
it is available on both Android and IOS. The application 
provides several different methods and features, including 
an easy way to track the user's money, detailed reports, a 
clear interface, customizable categories, automatic bill re-
minders,  debt  management,  multi-currency  support,  a 
built-in calculator, and more. The Money manager appli-
cation [28] is an application that solves the problem of the 
complication 
ac-
counts(budget). Available on both Android and iOS, it pro-
vides a lot of features like the ability for the user to enter 
her/his monthly income and calculate his/her expenses in 
various branches. The application is very good, and the in-
terfaces are user-friendly. In contrast to “Hassalah”. The 
money  manager  application  only  provides  the  ability  to 
record his/her purchases in an orderly manner without cre-
ating a budget.

of  managing

household

the

2.4 Applications without Arabic Interfaces

In  Mobil’s  applications  [29],  it  is  an  application  that 
helps people track expenses and maintain steady savings. 
It is available both for Android and iOS and provides many 
features such as adding accounts and credit cards, creating 
a  monthly  plan,  having  a  category  to  organize  expenses, 
adding payment or purchase operations manually, encour-
aging monthly savings, and providing illustrations of cate-
gories.  The  application received  a  high  rating  due  to  the 
features it offers. In GoodBudget application [30] which is 
employing  the  digital  version  of  envelope  budgeting 
through  the  GoodBudget  application  to  handle  their 
money. Users can distribute their income across separate 
expenditure categories through this application without re-
lying  on  cash  payments  and  access  their  budgets  every-
where because they can synchronize their content between 
their different devices. Nevertheless, manual financial ex-
pense input in the free version is time-intensive for users 
who are looking for a free application. The application pro-
vides an intuitive interface that leads users to control their 
financial choices. However, the proposed application ex-
tends  its  capabilities  by  implementing  alert  notifications

---

<!-- PAGE 5 -->

844 
when  the  user  is  close  to  exceeding  their  budget  and 
providing a personalized plan.

In the Moneon application [31], which is an application 
that helps users manage their personal finances, it is avail-
able on Android with iOS. The application provides sev-
eral different methods and features that serve the user in 
reaching  and  achieving  goals,  including  providing  per-
sonal  finance  management,  unlamented  numbers  of  wal-
lets,  full  control  over  categories/subcategories  creation, 
and much more. The application is very good, and it has an 
iOS 10 interface designed according to Apple’s guidelines. 
In the money flow application [32], which is an application 
that helps users to keep track of their expenses and income, 
it is available on Android with iOS. The application pro-
vides several different methods and features that serve the 
user in reaching and achieving goals, including quick and 
easy  adding  of  transactions,  customizable  accounts  and 
categories,  Synchronization  between  devices  and  adding 
goals and planning the budget, and more. The money man-
ager application [33] is an application that solves the prob-
lem of keeping track of users' budgets, finances and keep-
ing the money under control. Available on both Android 
and iOS, it provides a lot of features like payment remind-
ers, detailed reports, a clear interface, customizable cate-
gories,  helps  the  user  to  make  a  budget,  multi-currency 
support, and more. The Spendee application [34], which is 
an application to help users manage their money and track 
their spending, offers a simple interface that allows for cat-
egorizing  expenses,  generating  accurate  reports,  and  set-
ting reminders. The app relies on easy-to-use tools to facil-
itate personal money management, giving users a clearer 
view  of  their  spending  habits  and  helping  them  improve 
their  financial  management.  However,  the  app  is  only 
available on iOS, and it is noted that it lacks the advanced 
features needed for professional financial management or 
business  use.  In  Paymaster  application  [35],  which  is  an 
application that helps people manage their financial affairs 
and maintain their monthly budget, was available on An-
droid and iOS, the application provided several different 
methods and features that serve the user in reaching and 
achieving  goals,  such  as  computing  the  monthly  install-
ments or splitting the expenditure, they will notify you for 
payment dates and upcoming bills, preparing the daily and 
monthly  budget,  provided  accurate  analyses  and  details 
about spending through graphs and reports, there are some 
negatives such as manual entry of bills, a difficult interface 
for the user, the application received a high rating due to 
features.  In the Money application in [36], the application 
helps the users to keep track of their finances, it is available 
on Android with iOS. The application provides several dif-
ferent methods and features that serve the user in reaching 
and achieving goals, including a quick and effortless way 
to plan your income and expenses, tracking debts and sav-
ings, synchronization to track your finances across all your 
devices, and more. In the Buddy application [37], which is 
designed to simplify both individual budget management 
and  group  finances  by  providing  tools  for  budget  setup, 
spending  monitoring,  and  shared  fund  tracking.  Despite 
being easy to use and showing financial transactions, the

International Journal of Theoretical and Applied Research, 2025, 4(2) 
application  doesn’t  provide  alert  notifications  when  the 
user is close to exceeding the budget, nor offer any enter-
tainment ideas. The proposed application focuses specifi-
cally  on  budgeting  duties  through  personalized  financial 
plans for the user and real-time notification systems that 
maintain user financial stability.

2.5 Budget Mobile Applications Comparison

Table 1 shows the comparison between the reviewed ap-
plications (presented in Sections 2.3 and 2.4) and our pro-
posed application in terms of features and other aspects. To 
address the gap highlighted in previous works, a compara-
tive analysis was conducted between the proposed applica-
tion and existing budget management applications as pre-
sented in Table 1. The proposed system stands out in terms 
of functionality, intelligence, and user personalization. Un-
like  most  existing  apps  that  offer  basic  expense  tracking 
and  budgeting,  our  application  integrates  advanced  AI 
techniques,  specifically  an  RNN  to  predict  financial  risk 
and provide personalized financial plans. Also, it supports 
both Arabic and non-Arabic users. Additionally, our sys-
tem offers unique features such as real-time alert notifica-
tions, retirement financial planning, entertainment recom-
mendations based on budget, and a smart wishlist system. 
Furthermore, our app enables multilateral shared budgets, 
which is rarely supported elsewhere. Overall, the proposed 
application  provides  a  more  comprehensive,  intelligent, 
and culturally inclusive solution for modern financial man-
agement.

3.  Methodology 
3.1 Design of the Proposed System

The design phase translates requirements into a blueprint 
for implementation. Key design components include three 
main parts: the architecture model, data preprocessing, and 
interface design.

3.1.1 Architecture Model   
The  architecture  based  on  RNN,  specifically  imple-
mented a bi- directional LSTM network of two hidden lay-
ers, each with 128 units followed by a fully connected out-
put layer with a sofmax activation function for 3 class clas-
sification task (low/medium/high risk), the used activation 
function in hidden layer is RELU, the model was trained 
using Adam optimize and learning rate is 0.001, batch size 
is 64, and the number of epochs is equal to 50. It describes 
how a software system is structured and organized. Archi-
tectural design involves decisions about the type of appli-
cation, system distribution, and architectural styles. Archi-
tecture  is  often  documented  from  multiple  perspectives, 
such  as  conceptual,  logical,  process,  and  development 
views  .The  following  explains  the  architecture  model  of 
the proposed application, as shown in Fig. 2. 
•  The  system  architecture  is  best  described  as  Client-
Server, serverless functions, or a microservice  for AI 
processing.

•  Client: A mobile application built using React Native 
with  Expo.  This  client handles  the  user  interface  and 
user interactions.

---

<!-- PAGE 6 -->

Ghonaim et al.

•  Backend (Database): Cloud Firestore (Firebase) acts as 
the primary backend, managing data storage, real-time 
synchronization, and user authentication.

•  Backend  (AI  Processing):  A  separate  component  de-
veloped in Python handles AI-based tasks like financial 
risk  prediction  and  personalized  recommendations. 
This could be deployed as cloud functions or a micro 
service that interacts with Firestore. There are numer-
ous advantages of utilizing Python, where it is far less 
complicated because its interface is a legacy software 
written in various languages like C, C++, and others. 
Also, Python was initially made so that it could be ex-
tended using compiled code to increase its efficiency. 
•  The  React  Native/Expo  app  communicates  directly 
with  Firestore  for  most  data  operations  (CRUD).  For 
AI-driven  insights,  the  app  might  trigger  a  Python 
backend  service  (e.g.,  via  HTTPS  requests  or  cloud 
function triggers), which processes data from Firestore 
and potentially writes results  back or returns them to 
the app, it enables real-time data synchronization that 
ensures data stays up to date between different devices, 
as it provides safe authentication in addition to allow-
ing  efficient  tracking  of  user  transactions  and  budget 
records.

3.1.2 Data Preprocessing

Preprocessing  is  an  essential  step  in  data  analysis,  and 
machine learning is data preprocessing. It requires convert-
that  are 
ing  unstructured  datasets

formats

into

845

standardized, clean, and appropriate for modeling. Prepro-
cessing  guarantees  that  downstream  algorithms  can  effi-
ciently  learn  from  the  data  by  resolving  problems  like 
missing values, inconsistent formats, and incorrect entries. 
Even the most advanced models are likely to yield false or 
deceptive  results  in  the  absence  of  strong  preprocessing. 
Imputation of missing values, scaling or normalization of 
numerical features, categorical variable encoding, and data 
restructuring  for  model  compatibility  are  examples  of 
common preprocessing tasks.

Fig. 2. Architecture Diagram

Table 1. The comparison between the reviewed applications and our proposed application

Data Cleaning: A crucial preprocessing step in any data 
science or machine learning project is data cleaning. Due

to a variety of data sources and collection techniques, raw 
datasets  frequently  include  formatting  errors,  missing

---

<!-- PAGE 7 -->

International Journal of Theoretical and Applied Research, 2025, 4(2) 
crisis prediction. The design offers an easy-to-use interface 
that facilitates effective financial control for users.

846 
values, duplicate records, inconsistencies, or irrelevant in-
formation. By resolving such problems and converting the 
data into an accurate and structured format, data cleaning 
aims to improve the dataset's quality, consistency, and de-
pendability. Clean data guarantees that the inputs used in 
downstream analysis, visualizations, and predictive mod-
els are reliable and significant. Ignoring this step may lead 
to  inaccurate  insights  and  subpar  model  performance. 
Thus, data cleaning is a fundamental step that directly af-
fects  the  efficacy  and  legitimacy  of  the  entire  analytical 
process, rather than merely being a preparatory task.

Standardize  Column  Names: By  changing  column 
names to lowercase and applying underscores (_) as sepa-
rators, they are standardized to a uniform format. Columns 
in the code are made more readable and accessible by this 
method (e.g., Client_Id turns into client_id),

Rename  key  Linking  Columns: The  key  linking  col-
umns, such as id in the user data and client_id in the trans-
action  data,  are  renamed  to  a  consistent  name,  user_id. 
This guarantees a correct connection between the datasets 
and smooth merging, therefore  facilitating accurate  table 
joining.

Parse  Date/Time  Columns: Date  columns  are  parsed 
into date-time objects in Python, therefore enabling time-
based  analysis.  Invalid  date  formats  are  handled by  con-
verting them to NaT (Not a Time), which indicates missing 
or invalid dates. This makes it possible to increase.

Clean  Monetary  String  Columns:  Commas  used  to 
group  digits,  parentheses  ()  that  contain  negative  values, 
and currency symbols like $ are all removed from mone-
tary  columns  that  contain  financial  amounts.  After  that, 
these columns are transformed into numeric types (float, 
for  example).  Unconvertible  values  are  changed  to  NaN 
(Not a Number), which denotes inaccurate or missing in-
formation.

Risk Label Construction (Low / Medium / High): Be-
cause the original Kaggle dataset did not include risk la-
bels, we created them through a clear and replicable scor-
ing method. Each transaction was evaluated using practical 
financial indicators such as the user’s spending relative to 
income, existing debt pressure, the frequency and timing 
of  transactions,  the  type  of  purchase,  and  whether  the 
spending  exceeded  the  planned  budget.  These  factors 
helped reflect whether a transaction suggested stable or po-
tentially risky financial behavior. After calculating a com-
bined score for each case, we applied simple thresholds to 
classify  transactions  into  three  levels:  low,  medium,  or 
high  risk,  so  the  labeling  process  remained  transparent, 
grounded in real financial patterns, and easy to reproduce.

3.1.3 Interface Design

In the budget management proposed application, the  in-
terfaces  were  designed by  using  Figma, where a  focus on 
providing  a  smooth  and  professional  user  experience. 
More  than  27  interfaces  were  designed,  covering  all  the 
features of the app, from registration and login to expense 
management,  financial  recommendations,  and  financial

Log  In  and  Sign-up  Interfaces:  as  shown  in  Fig.  3. 
These interfaces represent the basic registration (Sign up), 
login in the proposed application. The Sign-Up interface 
includes entering user information to create a new account. 
The Log In interface allows entering an email and a pass-
word.

Profile Page and Edit Profile:  The profile interface dis-
plays basic user information, with a red “Edit Profile” but-
ton.  The  page  also  contains  several  options,  such  as 
“Transactions”,  “Debt/Loan,”  and  language  change  but-
tons  (Arabic  /  English),  allowing  the  user  to  switch  be-
tween languages easily. As for the edit profile interface, it 
contains  user  information  fields  with  a  “Save”  button  to 
save the changes, as shown in Fig. 4.

Fig. 3. Sign UP and Log in Interfaces

Fig. 4. Profile Page Interface

Report Interfaces: These interfaces represent the man-
agement of financial accounts and monthly reports, which 
the user can access through the menu bar at the bottom of 
the page user can add new account, as shown in Fig. 5.

Budget  Interfaces:  These  interfaces  represent  the 
budget  management  pages  (My  Budget)  in  the  proposed 
application, where the user can easily control their money 
and track their spending, and add a new budget, as shown 
in Fig. 6.

3.2 Implementation phase

The implementation phase involves the practical devel-
opment  of  the  proposed  application  using  selected  tools, 
technologies,  and  methodologies  to  achieve  the  defined

---

<!-- PAGE 8 -->

Ghonaim et al.

functional and non-functional requirements. Below is a de-
tailed breakdown of the implementation process. For pro-
gramming  Language  &  Tools,  the  following  tools  and 
technologies are planned for the development of the pro-
posed application:

Frontend Development:

React  Native:  Framework  for  building  cross-platform 
mobile  applications  using  JavaScript/TypeScript.  Expo 
Toolset and platform built around React Native to stream-
line development, building, and deployment.

Backend Development  :

Python is selected for implementing the AI-driven com-
ponents of the application, including financial  crisis pre-
diction  and  personalized  recommendations  [48].    Rich 
Ecosystem: Libraries like TensorFlow/Keras (for building 
Recurrent  Neural  Networks)  and  scikit-learn  streamline 
proposed model development.

3.3 The proposed system

The transaction type and category were used as the input 
features, while the day of the month, time between trans-
actions,  and  transaction  sequence  order  were  normalized 
and fed into the RNN to capture the sequence of financial 
activities.  The  proposed  application  combines  back-end 
development using a Python Flask API with front-end de-
velopment  using  a  React  Native  mobile  application.  To 
provide real-time spending risk predictions, the API com-
bines a pre-trained machine learning model, encapsulates 
business  logic,  and  coordinates  data  persistence  in  Fire-
store.

3.3.1 Backend Development  
The  backend  architecture  of  the  proposed  application 
was developed using Python and the Flask framework. It 
provides a connection point for the user interface, the da-
tabase, and the AI model. The backend acquires applica-
tion transaction data to perform required feature engineer-
ing  before  providing  input  to  the  trained  model  to  make 
financial risk predictions. The results are then stored in a 
Firestore database and returned to the application interface 
for display to the user. This architecture provides an effi-
cient  and  secure  API  that  enables  the  system  to  operate 
smoothly and provide accurate predictions in real time.

Firebase  Firestore:  In  the  application,  Firebase  Fire-
store is used as a cloud database where all the user data is 
stored in an organized, flexible, and automated way. The 
data in Firestore is split up into multiple main collections, 
with each collection containing documents  that represent 
various data entities.

Users: This collection includes basic user information, 
including name, email, age, and annual income. This data 
is used to build a personal budget and analyze risks. This 
data is entered and saved in the Fire Store when the user 
registers from the sign-up page.

Transactions:  This  collection  stores  all  the  financial 
transactions that the user has made, either expenses or in-
come.  Each  document  contains  the  type,  amount,  date,

associated account, and category. New transactions can be 
added from the Add page.

847

Fig. 5. Report interface and Add Account Interface

Fig. 6. My Budget Interface and add a new Budget in-
terface

Budget:  This  collection  stores  the  budget  amount  for 
each category, such as food, entertainment, and transpor-
tation etc. The data is later used by comparing the actual 
spending against the amount specified.

Loan and Debt: These two collections contain debts and 
loans, and store the other party’s name, amount, due date, 
and payment status. A new loan or debt is added from the 
Add Loan and Add Debit pages, and this data is used to 
track due and expected payments.

Account:  This  collection  represents  all  the  accounts 
owned by the user and contains the account name and ac-
count amount. A new account can be added from the Add 
Account page.

Recurring Transactions: This collection is used to save 
recurring  transactions  such  as  subscriptions  or  monthly 
payments, for easy addition or late.

Wishlist:  This  collection  contains  the  user’s  wish  list. 
Every  item  has  the  name,  brand,  price, priority,  and ful-
filled/not  fulfilled  completion  status.  New  items  can  be 
added from the add item page.

Financial Risk Prediction:  This collection records the 
results of the smart analysis of each transaction based on 
the artificial intelligence model, and contains the risk level 
(low, medium, high) and the probability of each.

Firebase Authentication: Helped to offer a secure and 
simple  sign-in  and  sign-out  system  to  users.  It  signs  in

---

<!-- PAGE 9 -->

848 
using email & password and saves login details, including 
login time and last login time.

International Journal of Theoretical and Applied Research, 2025, 4(2) 
essential tasks are executed, including saving transactions 
or adding accounts. These kinds of confirmations are visi-
ble to users in the form of alerts/pop-ups to reassure them.

3.3.2 Model Integration  
After the neural network model was trained and saved, it 
was  deployed  in  the  application  using  a  backend  frame-
work built with Flask. When a user adds a transaction in 
the app, the backend receives this data and saves it to the 
cloud database (Firestore). It then collects all the users’ re-
cent transactions for the current month and tries to find a 
monthly budget. If no budget has been set before, the sys-
tem  automatically  calculates  one  based  on  the  user’s  in-
come.  This  data  is  then  passed  to  a  special  feature-engi-
neering module that turns it into numbers the  model can 
understand,  just  like  the  ones  used  during  training.  The 
backend loads the trained model, the scaler (which keeps 
number ranges consistent), and a list of the features to ex-
pect. The features are sent to the model, which returns the 
predicted financial risk level (low, medium, or high). If the 
transaction is an income, the risk is always set to “Low” 
automatically.  The  feedback  from  the  AI  model  is  dis-
played  in  the  app  immediately  and  gets  saved  to  the  FI-
NANCIAL_RISK_PREDICTION.  For  the  integration  to 
start, the required Python libraries and packages were in-
stalled from the requirements text file. This file contains 
all that is needed to make the AI model work. For example, 
Flask is used to build the API, which will connect the app 
to the model, while Flask-CORS enables safe communica-
tion of different domains (app to backend in our case). Ten-
sorFlow ensures that there are necessary tools to load and 
run the trained neural network. Scikit-learn is used for jobs 
such as data pre-processing and model support utility. Pan-
das and NumPy help deal with data and work on it.

3.3.3 Fronted Development  
The front end of the proposed application was developed 
using  React  Native  with  Expo,  enabling  cross-platform 
functionality  for  both  Android  and  iOS  using  a  single 
codebase. The primary objective was to create an interface 
that is clean, intuitive, bilingual (Arabic and English), and 
responsive to real-time financial data from the backend AI 
system.

React Native is an open-source framework developed by 
Meta (formerly Facebook) that allows developers to build 
mobile  applications  using  JavaScript  and  React.  Unlike 
traditional mobile app development approaches (which use 
Java/Kotlin for Android and Swift/Objective-C for iOS), 
React Native enables cross-platform development—write 
once, run on both platforms.

Main  Interfaces:  The  proposed  application  contains 
several core interfaces that will assist the user in managing 
his  /  her  finances  effectively.  These  screens  cover  such 
main functions as adding transactions, managing budgets, 
as well as setting financial goals.

Error Handling: The proposed application includes rel-
evant error handling to guide users better while navigating 
the app. Validation on mandatory fields is carried out, and 
alerts come with pertinent information for users when se-
lected actions fail.

Confirmation & Success Feedback: The proposed ap-
plication  provides  users  with  simple  notifications  once

3.4 Model Performance

The  performance  of  the  proposed  application  is  meas-
ured based on Precision, Recall, F1-score, and accuracy.  
•  Precision was calculated as the number of true posi-
tives  divided  by  the  sum  of  true  positives  and  false 
positives: 
•  Precision =

TruePositives

TruePositives+FalsePositives

•  Recall was computed by dividing true positives by the

sum of true positives and false negatives:

Recall =

TruePositives
TruePositives + FalseNegatives

•  F1-score, which balances precision and recall, was cal-

culated as:

F1 = 2 ×

Precision × Recall
Precision + Recall

•  The accuracy score represents the proportion of correct

predictions out of all predictions:

Accuracy =

Correct Predictions
Total Predictions

These formulas helped ensure the evaluation was both 
quantitative  and  interpretable,  providing  meaningful  in-
sights into model behavior across risk levels.

●  Stability / Error Rate: How frequently do users encoun-
ter bugs or crashes? The aim is to minimize technical 
errors.

●  Data  Security:  (Implicit  Requirement)  Is  user  data 
stored and handled securely within Firestore and during 
API interactions?

4. Experimental Results 
4.1 Dataset Description

The main data source used for this project was the Trans-
actions Fraud Datasets published on Kaggle [38]. This da-
taset contains two tables: the transaction table and the us-
er's table. The transactions table, with 1,048,576 real finan-
cial  transactions  that  contain  the  transaction  details  like 
date, amount, client_id, etc. The users table contains per-
sonal and financial information about 2,000 users, like age, 
yearly income and total debt. The dataset was divided into 
70% training, 15% validation, and 15% testing sets. Alt-
hough  the  original  purpose  of  this  dataset  was  to  detect 
fraud,  it  was  used  in  this  paper  to  design  an  intelligent 
model capable of assessing the financial risk level of each 
transaction  based  on  user  behavior.  The  dataset  includes 
transaction  details  about  amounts,  transaction  type,  and 
payment methods, along with information about users such 
as age, gender, income status, and debt data. The selected 
dataset was useful for building predictive models because 
it  contained  extensive,  analyzable  features  that  reflected 
actual financial behavior patterns. Testing software is an

---

<!-- PAGE 10 -->

Ghonaim et al.

essential task in software engineering that guarantees good 
quality  and  reliable  applications.  Functional  Testing: 
Functional  testing  was  used  to  ensure  all  the  features 
worked based on the requirements specifications. User reg-
istration, login attempts, adding accounts, adding a budget, 
risk alert, and notification were verified. All core function-
ality was evaluated, including:  The following table shows 
examples of test cases used during functional testing.

4.2 Prediction Model Results

To assess the model’s ability to predict spending risk lev-
els, a separate set of unseen financial transactions was used 
to replicate  a  real-world application. The results indicate 
that the model performs with high reliability, particularly 
in  detecting  low  and  high-risk  behaviors,  giving  users 
greater confidence in managing their finances. Its sensitiv-
ity to medium-risk patterns is solid, though slightly more 
variable, reflecting the nuanced nature of such behaviors. 
Table 2 presents a summary of core performance metrics, 
including precision, recall, and F1-score. As illustrated in 
Table 3, the confusion matrix highlights how closely the 
model’s predictions aligned with actual outcomes. The ma-
jority  of  predictions  in  each  category,  especially  “Low” 
and “High,”  were correct, while slight overlaps occurred 
within  the  “Medium”  category.  Meanwhile,  these  results 
confirm that the model not only offers reliable classifica-
tions but also serves as a strong foundation for continuous 
improvement and refinement in risk assessment.

4.3 Application Testing Case

Functional  testing  was  used  to  ensure  all  the  features 
worked based on the requirements specifications. User reg-
istration, login attempts, adding accounts, adding a budget, 
risk alert, and notification were verified. All core function-
ality  was  evaluated,  including:  The  following  Table  4 
shows examples of test cases used during functional test-
ing. For the proposed application, all the results were good 
and reflect the app's success. The app was tested with test 
cases,  including  the  most  important  features,  such  as

Table 4.  Functional Testin

849

registering a new account, adding a new transaction, add-
ing a budget, adding accounts, and more. The application 
passed  all  these  tests  without  errors,  which  indicates  the 
stability of the application and its ease of use.

Table 2. Classification Report

Risk 
Level

Low

Medium

High 
Macro 
Avg. 
Weighted 
Avg.

Preci-
sion

0.97

0.97

0.98

0.97

Re-
call

0.97

0.97

0.98

F1-
Score

0.97

0.97

0.98

Support

588,091

619,864

723,206

0.97

0.97

1,931,161

0.97

0.97

0.97

1,931,161

Table 3. Confusion Matrix

Actual Low

Actual Me-
dium   
Actual High

Predicted 
Low

Predicted 
Medium

Predicted 
High

569,272

7,300

11,519

16,331

603,108

425

2,112

11,596

709,498

All of this confirms that the application is a useful tool in 
the daily lives of users. The prediction model's outcomes 
show a real technical victory, but they also represent a sig-
nificant  human  step  toward  empowering  consumers  to 
make  better  financial decisions.  When  evaluated  on  new 
data,  the  model  attained  an  overall  accuracy  of  97.45%, 
demonstrating its robustness and high potential for practi-
cal use. Precision, recall, and F1 measures across all risk 
categories  (low,  medium,  and  high)  outperformed  0.97, 
confirming  the  model's  ability  to  accurately  detect  ex-
penditure patterns.

Test case 
ID

Scenario

Input/Test Steps

Expected Output

Status

Actual Output

TC-1

New Registra-
tion

TC-2

Log in

1. Open the app 
2. Press “sign up.” 
3. Enter all information 
4. Press “Sign up.”

1. Open the app 
2. Press “Log in.” 
3. Enter Email and pass-

word

4. Press “Login”

User Register success-
fully stores all the user 
information in the da-
tabase, and the user is 
redirected to the login 
interface.

The user logs in, and 
the user is redirected 
to the Home(profile) 
interface.

Pass

Pass

As expected,

TC-3

Failed login

Email and password

1. Enter an incorrect

2. Press “Login”

An error message pops 
up on the screen.

Pass

---

<!-- PAGE 11 -->

850

International Journal of Theoretical and Applied Research, 2025, 4(2)

1. Go to the report inter-

face

TC-4

Add a new ac-
count

2. Press “add account.” 
3. Enter all the required

TC-5

Add new 
budget

TC-6

Add new 
Transaction

information 
4. Press “save” 
1. Go to the “My

Budget “interface 
2. Enter the month and 
assign a budget for 
each category 
3. Press “save” 
1. Go to the “Add” in-

terface

2. Enter all the required

information 
3. Press “save”

1. Go to the “Add” in-

terface

The account is created 
message and saves the 
info into the database.

Pass

The Budget is created 
message and saves the 
info into the database.

Pass

The Transaction is cre-
ated message and the 
info is saved into the 
database.

Pass

TC-7

Financial alert 
(high)

2. Enter a high amount 
3. Enter all the required

An alert will pop up.

Pass

information 
4. Press “save”

1. Go to the “Add” in-

terface

2. Enter a reasonable

amount

3. Enter all the required

information 
4. Press “save” 
1. Go to the “Add” in-

terface

2. Enter a small amount 
3. Enter all the required

information 
4. Press “save” 
1. Go to the “Wishlist”

interface

2. Press the money-

shaped button at the 
top of the page

TC-8

Financial alert 
(medium)

TC-9

Financial alert 
(Low)

Pass

Suggestions of 
what to buy 
from the wish 
list items

A medium alert will 
pop up.

Pass

No pop-ups, but it will 
be added to the notifi-
cation interface.

Pass

The suggestion will 
pop up.

Pass

5. Conclusion, recommendations and future work

The proposed application aimed to develop a bilingual 
smart budget management mobile application designed 
to enhance personal financial planning through artificial 
intelligence  and  address  a critical  gap  in  the  market. It 
supports Arabic and English users by offering an acces-
sible  interface  and  advanced  features  such  as  expense 
tracking, debt management, budget monitoring, and AI-
powered  financial  risk  prediction.  The development  of 
the  lifecycle,  covering  requirements  gathering,  system 
design,  implementation,  and  testing,  the  application 
demonstrated both functional completeness and high us-
ability. The proposed application achieved 97.45% accu-
racy  in  classifying  financial  transactions  by  risk  level 
(low, medium, high), enabling real-time alerts that em-
power users to make informed decisions and avoid finan-
cial stress.

Although  the  proposed  application  achieved  its  in-
tended goals, there remain valuable directions for future 
improvement and expansion.

New  Features:  Future  versions  of  the  app  could  in-

clude: 
•

Integration with online payment systems to automate 
financial tracking and improve convenience.

•  Entertainment  recommendations  that  fit  within  the

user’s available budget.

•  Joint/multilateral  budget  sharing,  allowing  families 
or groups to collaboratively manage shared expenses.

1.  Scalability:  Expanding  the  proposed  application  to 
support  multiple  currencies  and  regional  tax  struc-
tures could enable its adoption beyond the initial tar-
get  audience.  Moreover,  developing  a  web-based 
companion interface could improve accessibility.

2.  Technological Enhancements:

•  Bank account synchronization would allow real-time

financial data import, reducing manual entry.

•  Blockchain  integration  could  improve  transaction 
transparency,  data  integrity,  and  traceability  in 
budget  management  processes,  thereby  enhancing 
the  overall  accountability  and  security  of  financial 
operations.

•  Advanced AI techniques, such as generative AI or re-
inforcement  learning,  can  improve  personalization 
and forecasting accuracy.

---

<!-- PAGE 12 -->

Ghonaim et al. 
3.  Deployment: Publishing the proposed application on 
the App Store and Google Play is a necessary next 
step. This will require addressing platform-specific 
requirements,

4.  Ensuring  security  compliance  and  setting  up  user

support systems.

References 
1.  Gorshkova  NV,  Mytareva  LA,  Perekrestova  LV, 
Glushchenko AV, Fisher OV. System of family budg-
eting as a methodological basis for personal accounting 
and  guarantee  for  growth  of  financial  literacy  of  the 
Russians.  Mediterranean  Journal  of  Social  Sciences,. 
2015; 
https://doi.org/ 
6(5): 
10.5901/mjss.2015.v6n5p413

413-422.

2.  Bai  R.  Impact  of  financial  literacy,  mental  budgeting 
and self-control on financial wellbeing: Mediating im-
pact of investment decision making. PLOS ONE. 2023; 
18(11): e0294466. 
 https://doi.org/10.1371/journal.pone.0294466

3.  Sonjaya Y. Exploring the Evolution of Budgeting Prac-
tices  from  Traditional  to  Technology.  Advances  in 
Management  &  Financial  Reporting  Research.  2024; 
2(1): 36–45. 
https://doi.org/10.60079/amfr.v2i1.265

4.  “Recurrent  neural  network,”  Wikipedia.  [Online]. 
https://en.wikipedia.org/wiki/Recur-

Available: 
rent_neural_network. [Accessed 19 Sept. 2025].

5.  Pascanu R, Mikolov T, Bengio Y. On the difficulty of 
training recurrent neural networks. In: Proceedings of 
the 30th International Conference on Machine Learn-
ing  (ICML  ’13).  Atlanta  (GA),  USA;  2013.  1310–
1318. 
https://proceedings.mlr.press/v28/pascanu13.html 
6.  Noh S-H. Analysis of gradient vanishing of RNNs and 
performance comparison of standard RNN, LSTM, and 
GRU. Information. 2021; 12(11): 442. 
doi:10.3390/info12110442

7.  Hochreiter  S,  Schmidhuber  J.  Long  short-term 
memory.  Neural  Comput.  1997;  9(8):  1735-1780. 
doi:10.1162/neco.1997.9.8.1735

8.  Cho K, van Merrienboer B, Gulcehre C, Bahdanau D, 
Bougares  F,  Schwenk  H,  Bengio  Y.  Learning  phrase 
representations using RNN encoder–decoder for statis-
tical machine translation. In: Proceedings of the 2014 
Conference  on  Empirical  Methods  in  Natural  Lan-
(EMNLP);  2014.  1724-1734. 
guage  Processing 
doi:10.3115/v1/D14-117

9.  Bohora  A.  Money  alignment:  Helping  people  make 
smart money decisions. NYU SPS Applied Analytics 
Laboratory; 2023. Available from: 
http://hdl.handle.net/2451/6953

10. Valle-Cruz  D,  Fernandez-Cortez  V,  Gil-Garcia  JR. 
From  E-budgeting  to  smart  budgeting:  Exploring  the 
potential of artificial intelligence in government deci-
sion-making  for  resource  allocation.  Gov  Inf  Q. 
2022;39(1):101644. doi:10.1016/j.giq.2021.101644 
11. Hellwig K-P. Predicting fiscal crises: A machine learn-
ing  approach.  SSRN  Electron  J.  2021.  https://pa-
pers.ssrn.com/sol3/papers.cfm?abstract_id=3828232 
12. Wasserbacher H, Spindler M. Machine learning for fi-
nancial  forecasting,  planning  and  analysis:  recent

851

5.  Extended Applications: The core architecture of the 
proposed  application  could  be  adapted  for  broader 
use cases such as small business budgeting, commu-
nity saving circles, or educational tools promoting fi-
nancial literacy among students.

and

pitfalls.  Digital  Finance.

developments 
2021;4(1):63–88. doi:10.1007/s42521-021-00046-2 
13. Hansun S, Young JC. Predicting LQ45 financial sector 
indices  using  RNN-LSTM.  Journal  of  Big  Data,. 
2021;8:104. doi:10.1186/s40537-021-00495-x

14. Balathas M, Ganeshalingam S, Segar A, Vallaven Y, 
Siriwardana S. Money Empire: Intelligent Assistant for 
Personal  Finance  Management.  International  Journal 
for  Research  in  Applied  Science  and  Engineering 
Technology 2022; 10(XI): 454–461. doi:10.22214/ijra-
set.2022.47229.

15.  Saputra KD, Setiawan K, Suryani D, Purnama Y. Mo-
bile  financial  management  application  using  Google 
Cloud Vision API. Procedia Computer Science. 2019; 
157:596–604. doi:10.1016/j.procs.2019.09.019.

16.  Ngoh GJ, Darman R. MyMoney: Money Management 
and Tracking Application. Applied Information Tech-
nology  And  Computer  Science.  2022;  3(2):  442-459. 
doi:10.30880/aitcs.2022.03.02.029.

17.  Stefanov T, Stefanova M, Varbanova S, Temelkov S. 
Personal  Finance  Management  Application.  TEM 
Journal. 2024;13(3):2066–2075. 
doi:10.18421/TEM133-34.

18.  Makalew BA. Android Based Personal Finance Man-
agement  Application:  Design  and  Development. 
EMACS  (Engineering,  Mathematics  and  Computer 
Science) Journal. 2022; 4(1): 5–9.  
doi:10.21512/emacsjournal.v4i1.8085.

19.  Wong  CK,  Mohb  Salleh  MN.  Personal  Finance  and 
Budgeting Mobile Application, “CashSave”. Appl Inf 
Technol  Comput  Sci.  2023;  4(1):  1372-1387. 
https://publisher.uthm.edu.my/periodicals/in-
dex.php/aitcs/article/view/7621

20.  Pandey A, Tripathi A, Chauhan M. Design and Imple-
mentation  of  Expense  Management  Mobile  Applica-
tion. ISAR J Sci Technol. 2024;2(4):22. 
https://isarpublisher.com/backend/public/assets/arti-
cles/1714135412-ISARJST-412024FT-GP.pdf

21. Talasila  SD.  AI-Driven  Personal  Finance  Manage-
ment: Revolutionizing Budgeting and Financial Plan-
ning.  International  Journal  of  Engineering  and  Tech-
nology Research. 2024;11(7):397–403. 
https://www.irjet.net/archives/V11/i7/IR-
JET-V11I755.pdf

22. "Wafir,"  Apple  App  Store,  [Online].  Available: 
[Ac-

https://apps.apple.com/sa/app/id1552797940. 
cessed 16 9 2024].

23. "Spending Tracker - Wise Budget," Apple App Store, 
[Online].https://apps.apple.com/sa/app/spending-
tracker-wise-budget/id6444917344.  [Accessed  19  9 
2024].

24. "Wallet,"  Apple  App  Store,  [Online].  Available: 
https://apps.apple.com/sa/app/wallet.[Accessed  15  9 
2024].

---

<!-- PAGE 13 -->

International Journal of Theoretical and Applied Research, 2025, 4(2)

852 
25. "Amwaly,"  Apple  App  Store,  [Online].  Available: 
https://apps.apple.com/sa/app/amwaly. [Accessed 16 9 
2024].

26. "Masareef,"  Apple  App  Store,  [Online].  Available: 
[Accessed

https://apps.apple.com/app/id463676434. 
17 9 2024].

27. "Money Lover - Expense Manager," Apple App Store,

[Online]. Available:  
https://apps.apple.com/sa/app/money-lover-expense-
manager/id486312413. [Accessed 20 9 2024].

https://apps.apple.com/sa/app/spending-tracker-
money-flow/id900890647. [Accessed 18 9 2024]. 
33. "Money  Manager  -  Expense  Tracker,"  Apple  App

Store, [Online]. Available: 
https://apps.apple.com/sa/app/money-manager-ex-
pense-tracker/id1510997753. [Accessed 19 9 2024]. 
34. "Spendee Money & Budget Planner," Apple App Store,

[Online]. Available: 
https://apps.apple.com/app/id635861140. 
19 9 2024].

[Accessed

28. "Money  Manager  -  Expense  &  Budget,"  Apple  App

35.  "PayMaster  -  My  Spending  Tracker,"  Apple  App

Store, [Online]. Available: 
https://apps.apple.com/sa/app/money-manager-ex-
pense-budget/id560481810. [Accessed 18 9 2024]. 
29. "Mobills  -  Budget  Planner,"  Apple  App  Store,

[Online]. Available: 
https://apps.apple.com/sa/app/mobills-budget-plan-
ner/id921838244?l=ar. [Accessed 15 9 2024].

30. "Goodbudget  -  Budget  Planner,"  Apple  App  Store,

[Online]. Available: 
https://apps.apple.com/sa/app/goodbudget-budget-
planner/id471112395. [Accessed 12 9 2024].

31. "Moneon - My Budget & Expenses," Apple App Store,

[Online]. Available: 
https://apps.apple.com/sa/app/moneon-my-budgetex-
penses/id906363437?l=ar. [Accessed 18 9 2024]. 
32. "Spending Tracker - Money Flow," Apple App Store,

[Online]. Available:

Store, [Online]. Available:  
https://apps.apple.com/sa/app/paymaster-my-spend-
ing-tracker/id1462048413. [Accessed 19 9 2024]. 
36.  "1Money  -  Expense  Tracker,"  Apple  App  Store,

[Online]. Available: 
 https://apps.apple.com/sa/app/1money-expense-
tracker/id1623655243?l=ar. [Accessed 19 9 2024]. 
37.  "Buddy Money - Budget Planner," Apple App Store,

[Online]. Available: 
https://apps.apple.com/sa/app/buddy-money-budget-
planner/id936422955. [Accessed 19 9 2024].

38.  ComputingVictor.  Financial  Transactions  Dataset: 
Analytics  [dataset  on  the  Internet].  Kaggle;  undated 
[Accessed 
from: 
https://www.kaggle.com/…

2024].  Available

14

5

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Theoretical and Applied Research, 2025, Vol. 4, No. 2, 840-852
International Journal of Theoretical and Applied Research (IJTAR)
ISSN: 2812-5878
Homepage: https://ijtar.journals.ekb.eg
Original article
An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network
Wafaa A. Ghonaim*, Enas E. El-Sharawy
Mathematics Department, Computer Science Division, Faculty of Science, Al-Azhar University (Girls), Cairo 11651,
Egypt.
ARTICLE INFO ABSTRACT
Received 02/10/2025 Budgeting is important for both people and businesses to manage their finances, save,
Revised 16/11/2025 stay out of debt, and be ready for financial emergencies. This paper aims to propose an
Accepted 20/11/2025 intelligent mobile application to reduce financial risks and support better ways of saving
and investing through intelligent budgeting. A lot of budgeting applications lacked Arabic
Keywords language support and AI-based forecasting capabilities. This gap is addressed by the de-
velopment of an application that supports English and Arabic speakers through a Recurrent
Budget managemen
Neural Network (RNN) for enhanced financial and management capabilities. The model
Mobile application
was trained on a real-world financial dataset, preprocessing it, and transforming its data.
Artificial intelligence
Recurrent neural network The results demonstrated that the model was highly accurate in the classification of finan-
cial transactions based on the level of risk. The application was tested on new data; it
reached an overall accuracy of 97.45%. Precision, recall, and F1 measures are all higher
than 0.97 for each of the risk categories: low, medium, and high. These results validate the
reliability of the system, particularly in detecting critical low- and high-risk behaviors, and
its capacity to help users make safer and more informed decisions regarding their finances.
Graphical abstract
1. Introduction awareness, and without these skills, the person may face
Budgeting skills should be applied to individuals and some financial difficulties, which in the long run may in-
families so that everyone can manage their finances effec- fluence the quality of life and achievement of their dreams.
tively. These skills demand much discipline and self- The economic challenges today are very different, and
∗ Corresponding author
E-mail address: dr.wafaaghonaim@azhar.edu.eg
DOI: 10.21608/IJTAR.2025.427658.1148

Ghonaim et al. 841
needs are growing in the modern world. People require application a reliable and effective partner in achieving fi-
smart and effective ways and means to manage the availa- nancial stability and long-term economic well-being.
ble resources to provide a secure and strong financial foun-
dation [1]. The reality of life is that living has become Many applications can help with money management,
costly, and the economic stresses call for people to learn but there is no comprehensive application that provides
how to manage their scarce resources. All budgeting skills several important features. It’s crucial to develop a com-
are no longer considered luxuries but a necessity for living prehensive application that is equipped with the latest tech-
a comfortable and secure future life. Personal attributes nologies and offers various languages to engage with var-
such as financial literacy, mental budgeting, and self-con- ious segments. For example, most of them are not in Ara-
trol are good in that they create a link between achieve- bic. This requires the urgency of developing an Arabic-lan-
ments in the workplace. A study suggests that people with guage application with extensive customization options to
high financial literacy have better financial health than oth- accommodate various cultures and lifestyles. Although
ers. In other words, understanding the basic aspects of fi- there are a few applications that use AI to predict financial
nances, personal planning, saving, and investing can help crises or their imminence, they do not offer personal plans
enhance one’s finances [2]. Budgeting has undergone sig- and purchase recommendations that fit the user's budget,
nificant changes over the years with the advancement of nor do they provide the user with an alert when the trans-
technology. Traditionally, budgeting began with a hierar- action exceeds the budget, nor give a retirement financial
chical process based on top-down instructions, which plan. Thus, this is a very serious gap as it is challenging for
made it difficult to adapt to changes. Technological ad- users to reach their financial objectives in a way that works
vancements have brought about many changes in budget for them. This suggests that these features were not given
management, with many software solutions being intro- enough consideration when earlier applications were de-
duced to plan, predict financial crises, and evaluate user veloped. Therefore, this project proposes a solution by de-
spending [3]. veloping a new application that combines the features from
This paper proposes a budget management mobile appli- earlier versions with several fundamental features in each
cation based on a Recurrent Neural Network (RNN), application to give users the best possible assistance in
which belongs to a family of neural architectures specifi- managing their financial affairs and reaching their finan-
cally designed for sequential and temporal data processing. cial objectives. The remainder of this paper is structured as
Despite their usefulness in areas such as RNNs are charac- follows: Section 2 presents many different budget manage-
terized by recurrent connections that enable information ment applications and papers. Section 3 proposes the ar-
from previous time steps to influence current outputs, al- chitecture of the proposed application. In Section 4, we
lowing the model to capture contextual and time-depend- present the experimental results and discussion of the pro-
ent patterns effectively [4]. Although RNNs have proven posed application. Finally, Section 5 provides a conclu-
effective in domains such as natural language processing, sion.
speech modelling, and time-series forecasting, they often
face training challenges, particularly vanishing and ex- 2. Related works
ploding gradient problems [5, 6]. To address these limita- In this section, the literature review will be presented. It
tions, advanced architectures such as Long Short-Term is based on two main categories: Research papers and ap-
Memory (LSTM) [7] and Gated Recurrent Units (GRU) plication papers, as shown in Fig. 1.
[8] have been developed. These architectures enhance the
network’s ability to learn and retain long-term dependen-
cies, often outperforming traditional RNNs in practical ap-
plications [6]. The proposed mobile application enables us-
ers to manage their finances intelligently through a user-
friendly and intuitive interface. It provides multiple ser-
vices, including recording expenditures across categories
such as necessities, loans, and discretionary spending
within a monthly adjustable budget. The application tracks
both daily and monthly expenditures across all categories
and generates detailed reports that help users monitor their
financial status and spending patterns. One of the most im-
portant tools provided in the application is the opportunity
to analyze spending data and even foresee the potential cri-
ses that might occur due to spending and changes in in-
come. Thus, the proposed Budget Management Applica-
tion serves as a comprehensive, user-oriented tool de-
signed to help individuals enhance their budgeting skills Fig. 1. Literature Review Taxonomy
and financial awareness. By integrating intelligent, tech-
nology-driven solutions, the system empowers users to 2.1 Research Papers
build long-term financial literacy and make informed, sus- In [9] involved a methodology was involved that ana-
tainable financial decisions. These features make the lyzed current financial industry practices and targeted

842 International Journal of Theoretical and Applied Research, 2025, 4(2)
customers to understand spending patterns with reduced inability to manage money properly and not understanding
spending. It is helpful for those building systems or im- the financial risks that a person may face due to making
proving financial decision-making methods. It tries to some wrong decisions. The authors used existing technol-
solve the problem of poor financial management and plan- ogy-based approaches, such as Google Cloud Vision API
ning, lack of knowledge, and inaccurate expense tracking. and One Signal API, and integrated them into a mobile-
The authors use knowledge and technology to develop a based application called Manage on Money. The applica-
financial management tool that provides clients with criti- tion received great satisfaction, which helped users man-
cal insights, financial plans, and monthly income and ex- age money.
pense analysis. In [10] solved the problem of how artificial
intelligence can assist in improving the allocation of the In [16] authors discussed the problem for people who do
public budget. The technology that the authors applied is not have enough financial knowledge to manage their
the employment of a hybrid AI approach involving a mul- money and track their daily income. The authors used the
tilayer perception and multi-objective genetic algorithm to iterative development methodology, Android Studio to de-
analyze the effects of various public spending categories sign the application interfaces, and Firebase for the data-
on inflation, GDP, and income inequality. It uses real- base. The project was developed with an object-oriented
world economic data to predict the outcome of scenarios approach. The application manages money and analyzes
that result from different budget allocations. cash flow effectively. The main results of this paper are an
application that manages money, analyzes cash flow effec-
In [11] authors focused on considering the problem of tively, helps users enter and track their spending, and cre-
predicting fiscal crises and the limitations of traditional ates financial plans for retirement and others. In [17] au-
econometric models in accurately forecasting such rare thors developed a mobile application for personal finances,
events. The main method proposed is applying machine offering a set of services for budget tracking, income and
learning models: random forest, gradient boosted trees, expense management, and report generation. The authors
and elastic net, through which the investigator investigates used technologies like Java, Gradle 8, and Microsoft SQL
the interactions of the economic, political, and demo- to create an Android application, validated through beta
graphic predictors while addressing overfitting through testing with real users, including those with visual impair-
out-of-sample validation and data pooling. In the study of ments. As a result, a mobile application was developed that
[12] authors discussed applying machine learning tech- offers a user-friendly interface and useful functionalities.
niques to improve financial forecasting and planning. In [18], the author’s aimed to create and show a prototype
Much focus has gone to supervised learning in predicting for a mobile application that would manage personal fi-
financial outcomes based on historical data; unsupervised nances, with an emphasis on goal setting, needs organiza-
learning, mainly for pattern recognition; and reinforcement tion, and budgeting. The procedure was broken down into
learning, especially for adaptive financial decision-mak- two phases: content realization, which realized all the fea-
ing. It was found that machine learning is good at finding ture lists and specifications from the first phase, and con-
patterns in financial data, but it struggles to explain why cept formulation, which resulted in an application design
those patterns happen, which is important for making de- with a set of needs and features. Consequently, two outputs
cisions. were generated from the work: use case and class diagrams
from the Content Realization phase and a feature list from
In [13] authors focused on considering the problem of the Concept Formulation phase that included Getting
forecasting stock price movements within the LQ45 finan- Started, Details for Every Function, Goal Setting, Budget-
cial sector index and the limitations of traditional forecast- ing, Organize Needs, Type of Expense, Indicator for Budg-
ing models in capturing the highly dynamic and nonlinear eting, Transaction History, and Reminder.
nature of financial markets. The main results of this paper
show that the LSTM-based approach significantly im- In [19], the authors developed the Cash Save app as an
proves the forecasting accuracy, especially for BBCA and effective way to manage money, using a prototyping ap-
BMRI stocks, which showed the lowest mean relative ab- proach with continuous improvements based on user feed-
solute error (MAPE) values, while other stocks showed back. The app passed 78% of the test cases, demonstrating
reasonable forecasting results. its overall efficiency, but it faced challenges such as the
history tracking feature failing in some cases, requiring ad-
2.2 Application Papers ditional improvements. In [20] authors developed an An-
In [14] authors tried to solve the problem of people's poor droid application for personal finance management, specif-
personal financial planning that leads to an inability to ically targeted at students. They used the Waterfall Model
meet needs. The authors use existing technology-based to design the application, which tracked, categorized, and
methods to create a mobile-based application called generated expense reports with customizable daily,
Money Empire. Money Empire has many features that dis- weekly, and monthly options. The application effectively
tinguish it which are it is a mobile app-based smart assis- met its intended purpose, but the limitations of the Water-
tant for personal finance management. This application au- fall Model, particularly its lack of adaptability, were noted.
tomates finance management by extracting transaction de- Iterative methods were suggested to improve flexibility
tails from banking SMS alerts and expense details from in- during the development process. Compared to similar ap-
voices. In [15] authors solve the problem of people's plications, this one emphasized simplicity while

Ghonaim et al. 843
integrating AI-driven financial advice to provide personal- and debts, if any, and then dividing the expenses into
ized recommendations. In [21] identified a challenge was monthly requirements, daily and monthly expense keep-
identified in managing personal finances in today's digital ing, offering notification of payment days and due charges,
world, where using multiple accounts and traditional re- displaying financial reports to clarify spending habits, and
cording methods can increase financial stress. To address analyzing the budget. In the Masareef application [26],
this issue, they introduced MyFinanceAI, an intelligent which is an application that manages money through budg-
system that combines deep neural networks, reinforcement eting, account synchronization, and spending tracking, the
learning, and advanced AI technologies. The system fea- application integrates with bank accounts, e-wallets, and
tures a secure data collection layer, a financial pattern anal- cryptocurrencies, allowing users to categorize expenses
ysis engine, and predictive models for analyzing time se- and generate detailed and accurate reports. It also relies on
ries data. It provides personalized recommendations with manual data entry to categorize expenses and prepare re-
40 % more accuracy thanks to its intelligent recommenda- ports, but some advanced features require a premium sub-
tion engine. The research showed that MyFinanceAI re- scription to access them. It is available on smartphones
duced financial stress by 43% and increased monthly sav- only and provides periodic updates to improve perfor-
ings by 22%. Additionally, 78% of users achieved their fi- mance and increase efficiency. The application has re-
nancial goals for debt reduction and savings, and expense ceived positive reviews due to its comprehensive features
projection accuracy improved by 30%. that help users improve their budget and increase their
awareness of their spending patterns.
2.3 Applications with Arabic Interfaces
The Wafeer application [22] is an application that helps In the money lover application [27], which is an appli-
people make decisions on budget and save money and cation that helps users to easily keep track of their finances,
eliminate wastage and other expenses that are not neces- it is available on both Android and IOS. The application
sary. A mobile application that can work on Android and provides several different methods and features, including
iOS. The main techniques and methodology applied to pro- an easy way to track the user's money, detailed reports, a
vide several services such as Expense tracking, preparing clear interface, customizable categories, automatic bill re-
a personal budget, Expense analysis, and financial alerts, minders, debt management, multi-currency support, a
Daily, monthly, and yearly analysis of operations, Chart of built-in calculator, and more. The Money manager appli-
spending rate for 6 months and specific periods in the ap- cation [28] is an application that solves the problem of the
plication, make statistics on your categories and purchases complication of managing the household ac-
through stores, Savings goals are determined by the per- counts(budget). Available on both Android and iOS, it pro-
son. vides a lot of features like the ability for the user to enter
her/his monthly income and calculate his/her expenses in
In the Wise Budget application [23], which is an appli- various branches. The application is very good, and the in-
cation that helps people to effectively monitor their spend- terfaces are user-friendly. In contrast to “Hassalah”. The
ing and optimize savings. Available on both Android and money manager application only provides the ability to
iOS, it provides a lot of features It contains comprehensive record his/her purchases in an orderly manner without cre-
budget management, as it requires entering the monthly in- ating a budget.
come to determine a budget, accurately tracking expenses
and financial reports by providing illustrative charts and 2.4 Applications without Arabic Interfaces
tables, The ability to add debts or loans to the application In Mobil’s applications [29], it is an application that
to facilitate budget management, Payments are entered helps people track expenses and maintain steady savings.
manually and no pictures or invoices are inserted. In the It is available both for Android and iOS and provides many
Wallet app [24], an app designed to help users monitor features such as adding accounts and credit cards, creating
their income, expenses, and budgets to improve their fi- a monthly plan, having a category to organize expenses,
nancial management, it offers features such as financial adding payment or purchase operations manually, encour-
data categorization, graphical reports, manual data entry, aging monthly savings, and providing illustrations of cate-
and bank synchronization. The app relies on features that gories. The application received a high rating due to the
make tracking expenses easy, helping users adopt better fi- features it offers. In GoodBudget application [30] which is
nancial habits. However, the app requires time-consuming employing the digital version of envelope budgeting
manual entries and does not provide personalized financial through the GoodBudget application to handle their
guidance. Additionally, its analytical features are consid- money. Users can distribute their income across separate
ered too simple for experienced users. expenditure categories through this application without re-
lying on cash payments and access their budgets every-
The Amwaly application [25] is an application that where because they can synchronize their content between
helps people solve several problems, such as the ability to their different devices. Nevertheless, manual financial ex-
organize personal money, monitoring spending and en- pense input in the free version is time-intensive for users
couraging savings available on Android and iOS. The main who are looking for a free application. The application pro-
techniques and methodologies are applied to provide sev- vides an intuitive interface that leads users to control their
eral services. Among the advantages provided by the ap- financial choices. However, the proposed application ex-
plication are entering income and determining expenses tends its capabilities by implementing alert notifications

844 International Journal of Theoretical and Applied Research, 2025, 4(2)
when the user is close to exceeding their budget and application doesn’t provide alert notifications when the
providing a personalized plan. user is close to exceeding the budget, nor offer any enter-
tainment ideas. The proposed application focuses specifi-
In the Moneon application [31], which is an application cally on budgeting duties through personalized financial
that helps users manage their personal finances, it is avail- plans for the user and real-time notification systems that
able on Android with iOS. The application provides sev- maintain user financial stability.
eral different methods and features that serve the user in
reaching and achieving goals, including providing per- 2.5 Budget Mobile Applications Comparison
sonal finance management, unlamented numbers of wal- Table 1 shows the comparison between the reviewed ap-
lets, full control over categories/subcategories creation, plications (presented in Sections 2.3 and 2.4) and our pro-
and much more. The application is very good, and it has an posed application in terms of features and other aspects. To
iOS 10 interface designed according to Apple’s guidelines. address the gap highlighted in previous works, a compara-
In the money flow application [32], which is an application tive analysis was conducted between the proposed applica-
that helps users to keep track of their expenses and income, tion and existing budget management applications as pre-
it is available on Android with iOS. The application pro- sented in Table 1. The proposed system stands out in terms
vides several different methods and features that serve the of functionality, intelligence, and user personalization. Un-
user in reaching and achieving goals, including quick and like most existing apps that offer basic expense tracking
easy adding of transactions, customizable accounts and and budgeting, our application integrates advanced AI
categories, Synchronization between devices and adding techniques, specifically an RNN to predict financial risk
goals and planning the budget, and more. The money man- and provide personalized financial plans. Also, it supports
ager application [33] is an application that solves the prob- both Arabic and non-Arabic users. Additionally, our sys-
lem of keeping track of users' budgets, finances and keep- tem offers unique features such as real-time alert notifica-
ing the money under control. Available on both Android tions, retirement financial planning, entertainment recom-
and iOS, it provides a lot of features like payment remind- mendations based on budget, and a smart wishlist system.
ers, detailed reports, a clear interface, customizable cate- Furthermore, our app enables multilateral shared budgets,
gories, helps the user to make a budget, multi-currency which is rarely supported elsewhere. Overall, the proposed
support, and more. The Spendee application [34], which is application provides a more comprehensive, intelligent,
an application to help users manage their money and track and culturally inclusive solution for modern financial man-
their spending, offers a simple interface that allows for cat- agement.
egorizing expenses, generating accurate reports, and set-
ting reminders. The app relies on easy-to-use tools to facil- 3. Methodology
itate personal money management, giving users a clearer 3.1 Design of the Proposed System
view of their spending habits and helping them improve The design phase translates requirements into a blueprint
their financial management. However, the app is only for implementation. Key design components include three
available on iOS, and it is noted that it lacks the advanced main parts: the architecture model, data preprocessing, and
features needed for professional financial management or interface design.
business use. In Paymaster application [35], which is an
application that helps people manage their financial affairs 3.1.1 Architecture Model
and maintain their monthly budget, was available on An- The architecture based on RNN, specifically imple-
droid and iOS, the application provided several different mented a bi- directional LSTM network of two hidden lay-
methods and features that serve the user in reaching and ers, each with 128 units followed by a fully connected out-
achieving goals, such as computing the monthly install- put layer with a sofmax activation function for 3 class clas-
ments or splitting the expenditure, they will notify you for sification task (low/medium/high risk), the used activation
payment dates and upcoming bills, preparing the daily and function in hidden layer is RELU, the model was trained
monthly budget, provided accurate analyses and details using Adam optimize and learning rate is 0.001, batch size
about spending through graphs and reports, there are some is 64, and the number of epochs is equal to 50. It describes
negatives such as manual entry of bills, a difficult interface how a software system is structured and organized. Archi-
for the user, the application received a high rating due to tectural design involves decisions about the type of appli-
features. In the Money application in [36], the application cation, system distribution, and architectural styles. Archi-
helps the users to keep track of their finances, it is available tecture is often documented from multiple perspectives,
on Android with iOS. The application provides several dif- such as conceptual, logical, process, and development
ferent methods and features that serve the user in reaching views .The following explains the architecture model of
and achieving goals, including a quick and effortless way the proposed application, as shown in Fig. 2.
to plan your income and expenses, tracking debts and sav- • The system architecture is best described as Client-
ings, synchronization to track your finances across all your Server, serverless functions, or a microservice for AI
devices, and more. In the Buddy application [37], which is processing.
designed to simplify both individual budget management • Client: A mobile application built using React Native
and group finances by providing tools for budget setup, with Expo. This client handles the user interface and
spending monitoring, and shared fund tracking. Despite user interactions.
being easy to use and showing financial transactions, the

Ghonaim et al. 845
• Backend (Database): Cloud Firestore (Firebase) acts as standardized, clean, and appropriate for modeling. Prepro-
the primary backend, managing data storage, real-time cessing guarantees that downstream algorithms can effi-
synchronization, and user authentication. ciently learn from the data by resolving problems like
• Backend (AI Processing): A separate component de- missing values, inconsistent formats, and incorrect entries.
veloped in Python handles AI-based tasks like financial Even the most advanced models are likely to yield false or
risk prediction and personalized recommendations. deceptive results in the absence of strong preprocessing.
This could be deployed as cloud functions or a micro Imputation of missing values, scaling or normalization of
service that interacts with Firestore. There are numer- numerical features, categorical variable encoding, and data
ous advantages of utilizing Python, where it is far less restructuring for model compatibility are examples of
complicated because its interface is a legacy software common preprocessing tasks.
written in various languages like C, C++, and others.
Also, Python was initially made so that it could be ex-
tended using compiled code to increase its efficiency.
• The React Native/Expo app communicates directly
with Firestore for most data operations (CRUD). For
AI-driven insights, the app might trigger a Python
backend service (e.g., via HTTPS requests or cloud
function triggers), which processes data from Firestore
and potentially writes results back or returns them to
the app, it enables real-time data synchronization that
ensures data stays up to date between different devices,
as it provides safe authentication in addition to allow-
ing efficient tracking of user transactions and budget
records.
3.1.2 Data Preprocessing
Preprocessing is an essential step in data analysis, and
Fig. 2. Architecture Diagram
machine learning is data preprocessing. It requires convert-
ing unstructured datasets into formats that are
Table 1. The comparison between the reviewed applications and our proposed application
Data Cleaning: A crucial preprocessing step in any data to a variety of data sources and collection techniques, raw
science or machine learning project is data cleaning. Due datasets frequently include formatting errors, missing

846 International Journal of Theoretical and Applied Research, 2025, 4(2)
values, duplicate records, inconsistencies, or irrelevant in- crisis prediction. The design offers an easy-to-use interface
formation. By resolving such problems and converting the that facilitates effective financial control for users.
data into an accurate and structured format, data cleaning
aims to improve the dataset's quality, consistency, and de- Log In and Sign-up Interfaces: as shown in Fig. 3.
pendability. Clean data guarantees that the inputs used in These interfaces represent the basic registration (Sign up),
downstream analysis, visualizations, and predictive mod- login in the proposed application. The Sign-Up interface
els are reliable and significant. Ignoring this step may lead includes entering user information to create a new account.
to inaccurate insights and subpar model performance. The Log In interface allows entering an email and a pass-
Thus, data cleaning is a fundamental step that directly af- word.
fects the efficacy and legitimacy of the entire analytical
process, rather than merely being a preparatory task. Profile Page and Edit Profile: The profile interface dis-
plays basic user information, with a red “Edit Profile” but-
Standardize Column Names: By changing column ton. The page also contains several options, such as
names to lowercase and applying underscores (_) as sepa- “Transactions”, “Debt/Loan,” and language change but-
rators, they are standardized to a uniform format. Columns tons (Arabic / English), allowing the user to switch be-
in the code are made more readable and accessible by this tween languages easily. As for the edit profile interface, it
method (e.g., Client_Id turns into client_id), contains user information fields with a “Save” button to
save the changes, as shown in Fig. 4.
Rename key Linking Columns: The key linking col-
umns, such as id in the user data and client_id in the trans-
action data, are renamed to a consistent name, user_id.
This guarantees a correct connection between the datasets
and smooth merging, therefore facilitating accurate table
joining.
Parse Date/Time Columns: Date columns are parsed
into date-time objects in Python, therefore enabling time-
based analysis. Invalid date formats are handled by con-
verting them to NaT (Not a Time), which indicates missing
or invalid dates. This makes it possible to increase.
Clean Monetary String Columns: Commas used to
group digits, parentheses () that contain negative values, Fig. 3. Sign UP and Log in Interfaces
and currency symbols like $ are all removed from mone-
tary columns that contain financial amounts. After that,
these columns are transformed into numeric types (float,
for example). Unconvertible values are changed to NaN
(Not a Number), which denotes inaccurate or missing in-
formation.
Risk Label Construction (Low / Medium / High): Be-
cause the original Kaggle dataset did not include risk la-
bels, we created them through a clear and replicable scor-
ing method. Each transaction was evaluated using practical
financial indicators such as the user’s spending relative to
income, existing debt pressure, the frequency and timing
of transactions, the type of purchase, and whether the Fig. 4. Profile Page Interface
spending exceeded the planned budget. These factors
helped reflect whether a transaction suggested stable or po- Report Interfaces: These interfaces represent the man-
tentially risky financial behavior. After calculating a com- agement of financial accounts and monthly reports, which
bined score for each case, we applied simple thresholds to the user can access through the menu bar at the bottom of
classify transactions into three levels: low, medium, or the page user can add new account, as shown in Fig. 5.
high risk, so the labeling process remained transparent,
grounded in real financial patterns, and easy to reproduce. Budget Interfaces: These interfaces represent the
budget management pages (My Budget) in the proposed
3.1.3 Interface Design application, where the user can easily control their money
In the budget management proposed application, the in- and track their spending, and add a new budget, as shown
terfaces were designed by using Figma, where a focus on in Fig. 6.
providing a smooth and professional user experience.
More than 27 interfaces were designed, covering all the 3.2 Implementation phase
features of the app, from registration and login to expense The implementation phase involves the practical devel-
management, financial recommendations, and financial opment of the proposed application using selected tools,
technologies, and methodologies to achieve the defined

Ghonaim et al. 847
functional and non-functional requirements. Below is a de- associated account, and category. New transactions can be
tailed breakdown of the implementation process. For pro- added from the Add page.
gramming Language & Tools, the following tools and
technologies are planned for the development of the pro-
posed application:
Frontend Development:
React Native: Framework for building cross-platform
mobile applications using JavaScript/TypeScript. Expo
Toolset and platform built around React Native to stream-
line development, building, and deployment.
Backend Development :
Python is selected for implementing the AI-driven com-
ponents of the application, including financial crisis pre- Fig. 5. Report interface and Add Account Interface
diction and personalized recommendations [48]. Rich
Ecosystem: Libraries like TensorFlow/Keras (for building
Recurrent Neural Networks) and scikit-learn streamline
proposed model development.
3.3 The proposed system
The transaction type and category were used as the input
features, while the day of the month, time between trans-
actions, and transaction sequence order were normalized
and fed into the RNN to capture the sequence of financial
activities. The proposed application combines back-end
development using a Python Flask API with front-end de-
velopment using a React Native mobile application. To
provide real-time spending risk predictions, the API com- Fig. 6. My Budget Interface and add a new Budget in-
bines a pre-trained machine learning model, encapsulates terface
business logic, and coordinates data persistence in Fire-
store. Budget: This collection stores the budget amount for
each category, such as food, entertainment, and transpor-
3.3.1 Backend Development tation etc. The data is later used by comparing the actual
The backend architecture of the proposed application spending against the amount specified.
was developed using Python and the Flask framework. It
provides a connection point for the user interface, the da- Loan and Debt: These two collections contain debts and
tabase, and the AI model. The backend acquires applica- loans, and store the other party’s name, amount, due date,
tion transaction data to perform required feature engineer- and payment status. A new loan or debt is added from the
ing before providing input to the trained model to make Add Loan and Add Debit pages, and this data is used to
financial risk predictions. The results are then stored in a track due and expected payments.
Firestore database and returned to the application interface
for display to the user. This architecture provides an effi- Account: This collection represents all the accounts
cient and secure API that enables the system to operate owned by the user and contains the account name and ac-
smoothly and provide accurate predictions in real time. count amount. A new account can be added from the Add
Account page.
Firebase Firestore: In the application, Firebase Fire-
store is used as a cloud database where all the user data is Recurring Transactions: This collection is used to save
stored in an organized, flexible, and automated way. The recurring transactions such as subscriptions or monthly
data in Firestore is split up into multiple main collections, payments, for easy addition or late.
with each collection containing documents that represent
various data entities. Wishlist: This collection contains the user’s wish list.
Every item has the name, brand, price, priority, and ful-
Users: This collection includes basic user information, filled/not fulfilled completion status. New items can be
including name, email, age, and annual income. This data added from the add item page.
is used to build a personal budget and analyze risks. This
data is entered and saved in the Fire Store when the user Financial Risk Prediction: This collection records the
registers from the sign-up page. results of the smart analysis of each transaction based on
the artificial intelligence model, and contains the risk level
Transactions: This collection stores all the financial (low, medium, high) and the probability of each.
transactions that the user has made, either expenses or in-
come. Each document contains the type, amount, date, Firebase Authentication: Helped to offer a secure and
simple sign-in and sign-out system to users. It signs in

848 International Journal of Theoretical and Applied Research, 2025, 4(2)
using email & password and saves login details, including essential tasks are executed, including saving transactions
login time and last login time. or adding accounts. These kinds of confirmations are visi-
ble to users in the form of alerts/pop-ups to reassure them.
3.3.2 Model Integration
After the neural network model was trained and saved, it 3.4 Model Performance
was deployed in the application using a backend frame- The performance of the proposed application is meas-
work built with Flask. When a user adds a transaction in ured based on Precision, Recall, F1-score, and accuracy.
the app, the backend receives this data and saves it to the • Precision was calculated as the number of true posi-
cloud database (Firestore). It then collects all the users’ re- tives divided by the sum of true positives and false
cent transactions for the current month and tries to find a positives:
monthly budget. If no budget has been set before, the sys- TruePositives
• Precision=
tem automatically calculates one based on the user’s in- TruePositives+FalsePositives
come. This data is then passed to a special feature-engi-
neering module that turns it into numbers the model can • Recall was computed by dividing true positives by the
understand, just like the ones used during training. The sum of true positives and false negatives:
backend loads the trained model, the scaler (which keeps
TruePositives
number ranges consistent), and a list of the features to ex-
Recall=
pect. The features are sent to the model, which returns the TruePositives+FalseNegatives
predicted financial risk level (low, medium, or high). If the
transaction is an income, the risk is always set to “Low” • F1-score, which balances precision and recall, was cal-
automatically. The feedback from the AI model is dis- culated as:
played in the app immediately and gets saved to the FI-
NANCIAL_RISK_PREDICTION. For the integration to Precision×Recall
F1=2×
start, the required Python libraries and packages were in- Precision+Recall
stalled from the requirements text file. This file contains
all that is needed to make the AI model work. For example, • The accuracy score represents the proportion of correct
Flask is used to build the API, which will connect the app predictions out of all predictions:
to the model, while Flask-CORS enables safe communica-
tion of different domains (app to backend in our case). Ten- Correct Predictions
Accuracy=
sorFlow ensures that there are necessary tools to load and Total Predictions
run the trained neural network. Scikit-learn is used for jobs
such as data pre-processing and model support utility. Pan- These formulas helped ensure the evaluation was both
das and NumPy help deal with data and work on it. quantitative and interpretable, providing meaningful in-
sights into model behavior across risk levels.
3.3.3 Fronted Development
The front end of the proposed application was developed ● Stability / Error Rate: How frequently do users encoun-
using React Native with Expo, enabling cross-platform ter bugs or crashes? The aim is to minimize technical
functionality for both Android and iOS using a single errors.
codebase. The primary objective was to create an interface ● Data Security: (Implicit Requirement) Is user data
that is clean, intuitive, bilingual (Arabic and English), and stored and handled securely within Firestore and during
responsive to real-time financial data from the backend AI API interactions?
system.
React Native is an open-source framework developed by 4. Experimental Results
Meta (formerly Facebook) that allows developers to build 4.1 Dataset Description
mobile applications using JavaScript and React. Unlike The main data source used for this project was the Trans-
traditional mobile app development approaches (which use actions Fraud Datasets published on Kaggle [38]. This da-
Java/Kotlin for Android and Swift/Objective-C for iOS), taset contains two tables: the transaction table and the us-
React Native enables cross-platform development—write er's table. The transactions table, with 1,048,576 real finan-
once, run on both platforms. cial transactions that contain the transaction details like
date, amount, client_id, etc. The users table contains per-
Main Interfaces: The proposed application contains
sonal and financial information about 2,000 users, like age,
several core interfaces that will assist the user in managing
yearly income and total debt. The dataset was divided into
his / her finances effectively. These screens cover such
70% training, 15% validation, and 15% testing sets. Alt-
main functions as adding transactions, managing budgets,
hough the original purpose of this dataset was to detect
as well as setting financial goals.
fraud, it was used in this paper to design an intelligent
model capable of assessing the financial risk level of each
Error Handling: The proposed application includes rel-
transaction based on user behavior. The dataset includes
evant error handling to guide users better while navigating
transaction details about amounts, transaction type, and
the app. Validation on mandatory fields is carried out, and
payment methods, along with information about users such
alerts come with pertinent information for users when se-
as age, gender, income status, and debt data. The selected
lected actions fail.
dataset was useful for building predictive models because
it contained extensive, analyzable features that reflected
Confirmation & Success Feedback: The proposed ap-
actual financial behavior patterns. Testing software is an
plication provides users with simple notifications once

| Ghonaim et al.  |     |     |     |     |     |     | 849  |
| --------------- | --- | --- | --- | --- | --- | --- | ---- |
essential task in software engineering that guarantees good  registering a new account, adding a new transaction, add-
quality  and  reliable  applications.  Functional  Testing:  ing a budget, adding accounts, and more. The application
Functional testing was used to ensure all the features  passed all these tests without errors, which indicates the
worked based on the requirements specifications. User reg- stability of the application and its ease of use.
| istration, login attempts, adding accounts, adding a budget,  |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
risk alert, and notification were verified. All core function- Table 2. Classification Report
ality was evaluated, including:  The following table shows
|     |     |     |     | Risk  | Preci- Re- | F1- |     |
| --- | --- | --- | --- | ----- | ---------- | --- | --- |
examples of test cases used during functional testing.  Support
|     |     |     |     | Level  | sion  call  | Score  |     |
| --- | --- | --- | --- | ------ | ----------- | ------ | --- |

4.2 Prediction Model Results
|     |     |     |     | Low  | 0.97  0.97  | 0.97  | 588,091  |
| --- | --- | --- | --- | ---- | ----------- | ----- | -------- |
To assess the model’s ability to predict spending risk lev-
els, a separate set of unseen financial transactions was used  Medium  0.97  0.97  0.97  619,864
to replicate a real-world application. The results indicate
|     |     |     |     | High  | 0.98  0.98  | 0.98  | 723,206  |
| --- | --- | --- | --- | ----- | ----------- | ----- | -------- |
that the model performs with high reliability, particularly
Macro
in detecting low and high-risk behaviors, giving users  0.97  0.97  0.97  1,931,161
Avg.
greater confidence in managing their finances. Its sensitiv-
| ity to medium-risk patterns is solid, though slightly more  |     |     |     | Weighted  |             |       |            |
| ----------------------------------------------------------- | --- | --- | --- | --------- | ----------- | ----- | ---------- |
|                                                             |     |     |     |           | 0.97  0.97  | 0.97  | 1,931,161  |
Avg.
variable, reflecting the nuanced nature of such behaviors.

Table 2 presents a summary of core performance metrics,
including precision, recall, and F1-score. As illustrated in  Table 3. Confusion Matrix
|                                                           |     |     |     |     | Predicted  | Predicted  | Predicted  |
| --------------------------------------------------------- | --- | --- | --- | --- | ---------- | ---------- | ---------- |
| Table 3, the confusion matrix highlights how closely the  |     |     |     |     |            |            |            |
|                                                           |     |     |     |     | Low        | Medium     | High       |
model’s predictions aligned with actual outcomes. The ma-
| jority of predictions in each category, especially “Low”  |     |     |     | Actual Low  |          |        |         |
| --------------------------------------------------------- | --- | --- | --- | ----------- | -------- | ------ | ------- |
|                                                           |     |     |     |             | 569,272  | 7,300  | 11,519  |
and “High,” were correct, while slight overlaps occurred
Actual Me-
within the “Medium” category. Meanwhile, these results  16,331  603,108  425
dium
confirm that the model not only offers reliable classifica-
Actual High
tions but also serves as a strong foundation for continuous  2,112  11,596  709,498
| improvement and refinement in risk assessment.  |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
  All of this confirms that the application is a useful tool in
4.3 Application Testing Case  the daily lives of users. The prediction model's outcomes
Functional testing was used to ensure all the features  show a real technical victory, but they also represent a sig-
worked based on the requirements specifications. User reg- nificant human step toward empowering consumers to
istration, login attempts, adding accounts, adding a budget,  make better financial decisions. When evaluated on new
risk alert, and notification were verified. All core function-
data, the model attained an overall accuracy of 97.45%,
ality was evaluated, including:  The following Table 4  demonstrating its robustness and high potential for practi-
shows examples of test cases used during functional test- cal use. Precision, recall, and F1 measures across all risk
ing. For the proposed application, all the results were good  categories (low, medium, and high) outperformed 0.97,
and reflect the app's success. The app was tested with test  confirming the model's ability to accurately detect ex-
cases,  including  the  most  important  features,  such  as  penditure patterns.

Table 4.  Functional Testin
Test case
|     | Scenario  | Input/Test Steps  | Expected Output  |     | Status  |                |     |
| --- | --------- | ----------------- | ---------------- | --- | ------- | -------------- | --- |
| ID  |           |                   |                  |     |         | Actual Output  |     |

User Register success-
|       |               | 1. Open the app           | fully stores all the user  |     |       |     |     |
| ----- | ------------- | ------------------------- | -------------------------- | --- | ----- | --- | --- |
|       | New Registra- | 2. Press “sign up.”       | information in the da-     |     |       |     |     |
| TC-1  |               |                           |                            |     | Pass  |     |     |
|       | tion          | 3. Enter all information  | tabase, and the user is    |     |       |     |     |
|       |               | 4. Press “Sign up.”       | redirected to the login    |     |       |     |     |
interface.
1. Open the app
The user logs in, and
2. Press “Log in.”
the user is redirected
| TC-2  | Log in  | 3. Enter Email and pass- |     |     | Pass  | As expected,  |     |
| ----- | ------- | ------------------------ | --- | --- | ----- | ------------- | --- |
to the Home(profile)
word
interface.
4. Press “Login”
1. Enter an incorrect
An error message pops
| TC-3  | Failed login  | Email and password  |     |     | Pass  |     |     |
| ----- | ------------- | ------------------- | --- | --- | ----- | --- | --- |
up on the screen.
2. Press “Login”

850 International Journal of Theoretical and Applied Research, 2025, 4(2)
1. Go to the report inter-
face
The account is created
Add a new ac- 2. Press “add account.”
TC-4 message and saves the Pass
count 3. Enter all the required
info into the database.
information
4. Press “save”
1. Go to the “My
Budget “interface
The Budget is created
Add new 2. Enter the month and
TC-5 message and saves the Pass
budget assign a budget for
info into the database.
each category
3. Press “save”
1. Go to the “Add” in-
The Transaction is cre-
terface
Add new ated message and the
TC-6 2. Enter all the required Pass
Transaction info is saved into the
information
database.
3. Press “save”
1. Go to the “Add” in-
terface
Financial alert 2. Enter a high amount
TC-7 An alert will pop up. Pass
(high) 3. Enter all the required
information
4. Press “save”
1. Go to the “Add” in-
terface
2. Enter a reasonable
Financial alert A medium alert will
TC-8 amount Pass
(medium) pop up.
3. Enter all the required
information
4. Press “save”
1. Go to the “Add” in-
terface
No pop-ups, but it will
Financial alert 2. Enter a small amount
TC-9 be added to the notifi- Pass
(Low) 3. Enter all the required
cation interface.
information
4. Press “save”
1. Go to the “Wishlist”
Suggestions of
interface
what to buy The suggestion will
Pass 2. Press the money- Pass
from the wish pop up.
shaped button at the
list items
top of the page
5. Conclusion, recommendations and future work
The proposed application aimed to develop a bilingual • Entertainment recommendations that fit within the
smart budget management mobile application designed user’s available budget.
to enhance personal financial planning through artificial • Joint/multilateral budget sharing, allowing families
intelligence and address a critical gap in the market. It or groups to collaboratively manage shared expenses.
supports Arabic and English users by offering an acces-
1. Scalability: Expanding the proposed application to
sible interface and advanced features such as expense
support multiple currencies and regional tax struc-
tracking, debt management, budget monitoring, and AI-
tures could enable its adoption beyond the initial tar-
powered financial risk prediction. The development of
get audience. Moreover, developing a web-based
the lifecycle, covering requirements gathering, system
companion interface could improve accessibility.
design, implementation, and testing, the application
demonstrated both functional completeness and high us-
2. Technological Enhancements:
ability. The proposed application achieved 97.45% accu-
racy in classifying financial transactions by risk level • Bank account synchronization would allow real-time
(low, medium, high), enabling real-time alerts that em- financial data import, reducing manual entry.
power users to make informed decisions and avoid finan- • Blockchain integration could improve transaction
cial stress. transparency, data integrity, and traceability in
Although the proposed application achieved its in- budget management processes, thereby enhancing
tended goals, there remain valuable directions for future the overall accountability and security of financial
improvement and expansion. operations.
New Features: Future versions of the app could in- • Advanced AI techniques, such as generative AI or re-
clude: inforcement learning, can improve personalization
• Integration with online payment systems to automate and forecasting accuracy.
financial tracking and improve convenience.

Ghonaim et al. 851
3. Deployment: Publishing the proposed application on 5. Extended Applications: The core architecture of the
the App Store and Google Play is a necessary next proposed application could be adapted for broader
step. This will require addressing platform-specific use cases such as small business budgeting, commu-
requirements, nity saving circles, or educational tools promoting fi-
4. Ensuring security compliance and setting up user nancial literacy among students.
support systems.
References
1. Gorshkova NV, Mytareva LA, Perekrestova LV, developments and pitfalls. Digital Finance.
Glushchenko AV, Fisher OV. System of family budg- 2021;4(1):63–88. doi:10.1007/s42521-021-00046-2
eting as a methodological basis for personal accounting 13. Hansun S, Young JC. Predicting LQ45 financial sector
and guarantee for growth of financial literacy of the indices using RNN-LSTM. Journal of Big Data,.
Russians. Mediterranean Journal of Social Sciences,. 2021;8:104. doi:10.1186/s40537-021-00495-x
2015; 6(5): 413-422. https://doi.org/ 14. Balathas M, Ganeshalingam S, Segar A, Vallaven Y,
10.5901/mjss.2015.v6n5p413 Siriwardana S. Money Empire: Intelligent Assistant for
2. Bai R. Impact of financial literacy, mental budgeting Personal Finance Management. International Journal
and self-control on financial wellbeing: Mediating im- for Research in Applied Science and Engineering
pact of investment decision making. PLOS ONE. 2023; Technology 2022; 10(XI): 454–461. doi:10.22214/ijra-
18(11): e0294466. set.2022.47229.
https://doi.org/10.1371/journal.pone.0294466 15. Saputra KD, Setiawan K, Suryani D, Purnama Y. Mo-
3. Sonjaya Y. Exploring the Evolution of Budgeting Prac- bile financial management application using Google
tices from Traditional to Technology. Advances in Cloud Vision API. Procedia Computer Science. 2019;
Management & Financial Reporting Research. 2024; 157:596–604. doi:10.1016/j.procs.2019.09.019.
2(1): 36–45. 16. Ngoh GJ, Darman R. MyMoney: Money Management
https://doi.org/10.60079/amfr.v2i1.265 and Tracking Application. Applied Information Tech-
4. “Recurrent neural network,” Wikipedia. [Online]. nology And Computer Science. 2022; 3(2): 442-459.
Available: https://en.wikipedia.org/wiki/Recur- doi:10.30880/aitcs.2022.03.02.029.
rent_neural_network. [Accessed 19 Sept. 2025]. 17. Stefanov T, Stefanova M, Varbanova S, Temelkov S.
5. Pascanu R, Mikolov T, Bengio Y. On the difficulty of Personal Finance Management Application. TEM
training recurrent neural networks. In: Proceedings of Journal. 2024;13(3):2066–2075.
the 30th International Conference on Machine Learn- doi:10.18421/TEM133-34.
ing (ICML ’13). Atlanta (GA), USA; 2013. 1310– 18. Makalew BA. Android Based Personal Finance Man-
1318. agement Application: Design and Development.
https://proceedings.mlr.press/v28/pascanu13.html EMACS (Engineering, Mathematics and Computer
6. Noh S-H. Analysis of gradient vanishing of RNNs and Science) Journal. 2022; 4(1): 5–9.
performance comparison of standard RNN, LSTM, and doi:10.21512/emacsjournal.v4i1.8085.
GRU. Information. 2021; 12(11): 442. 19. Wong CK, Mohb Salleh MN. Personal Finance and
doi:10.3390/info12110442 Budgeting Mobile Application, “CashSave”. Appl Inf
7. Hochreiter S, Schmidhuber J. Long short-term Technol Comput Sci. 2023; 4(1): 1372-1387.
memory. Neural Comput. 1997; 9(8): 1735-1780. https://publisher.uthm.edu.my/periodicals/in-
doi:10.1162/neco.1997.9.8.1735 dex.php/aitcs/article/view/7621
8. Cho K, van Merrienboer B, Gulcehre C, Bahdanau D, 20. Pandey A, Tripathi A, Chauhan M. Design and Imple-
Bougares F, Schwenk H, Bengio Y. Learning phrase mentation of Expense Management Mobile Applica-
representations using RNN encoder–decoder for statis- tion. ISAR J Sci Technol. 2024;2(4):22.
tical machine translation. In: Proceedings of the 2014 https://isarpublisher.com/backend/public/assets/arti-
Conference on Empirical Methods in Natural Lan- cles/1714135412-ISARJST-412024FT-GP.pdf
guage Processing (EMNLP); 2014. 1724-1734. 21. Talasila SD. AI-Driven Personal Finance Manage-
doi:10.3115/v1/D14-117 ment: Revolutionizing Budgeting and Financial Plan-
9. Bohora A. Money alignment: Helping people make ning. International Journal of Engineering and Tech-
smart money decisions. NYU SPS Applied Analytics nology Research. 2024;11(7):397–403.
Laboratory; 2023. Available from: https://www.irjet.net/archives/V11/i7/IR-
http://hdl.handle.net/2451/6953 JET-V11I755.pdf
10. Valle-Cruz D, Fernandez-Cortez V, Gil-Garcia JR. 22. "Wafir," Apple App Store, [Online]. Available:
From E-budgeting to smart budgeting: Exploring the https://apps.apple.com/sa/app/id1552797940. [Ac-
potential of artificial intelligence in government deci- cessed 16 9 2024].
sion-making for resource allocation. Gov Inf Q. 23. "Spending Tracker - Wise Budget," Apple App Store,
2022;39(1):101644. doi:10.1016/j.giq.2021.101644 [Online].https://apps.apple.com/sa/app/spending-
11. Hellwig K-P. Predicting fiscal crises: A machine learn- tracker-wise-budget/id6444917344. [Accessed 19 9
ing approach. SSRN Electron J. 2021. https://pa- 2024].
pers.ssrn.com/sol3/papers.cfm?abstract_id=3828232 24. "Wallet," Apple App Store, [Online]. Available:
12. Wasserbacher H, Spindler M. Machine learning for fi- https://apps.apple.com/sa/app/wallet.[Accessed 15 9
nancial forecasting, planning and analysis: recent 2024].

852 International Journal of Theoretical and Applied Research, 2025, 4(2)
25. "Amwaly," Apple App Store, [Online]. Available: https://apps.apple.com/sa/app/spending-tracker-
https://apps.apple.com/sa/app/amwaly. [Accessed 16 9 money-flow/id900890647. [Accessed 18 9 2024].
2024]. 33. "Money Manager - Expense Tracker," Apple App
26. "Masareef," Apple App Store, [Online]. Available: Store, [Online]. Available:
https://apps.apple.com/app/id463676434. [Accessed https://apps.apple.com/sa/app/money-manager-ex-
17 9 2024]. pense-tracker/id1510997753. [Accessed 19 9 2024].
27. "Money Lover - Expense Manager," Apple App Store, 34. "Spendee Money & Budget Planner," Apple App Store,
[Online]. Available: [Online]. Available:
https://apps.apple.com/sa/app/money-lover-expense- https://apps.apple.com/app/id635861140. [Accessed
manager/id486312413. [Accessed 20 9 2024]. 19 9 2024].
28. "Money Manager - Expense & Budget," Apple App 35. "PayMaster - My Spending Tracker," Apple App
Store, [Online]. Available: Store, [Online]. Available:
https://apps.apple.com/sa/app/money-manager-ex- https://apps.apple.com/sa/app/paymaster-my-spend-
pense-budget/id560481810. [Accessed 18 9 2024]. ing-tracker/id1462048413. [Accessed 19 9 2024].
29. "Mobills - Budget Planner," Apple App Store, 36. "1Money - Expense Tracker," Apple App Store,
[Online]. Available: [Online]. Available:
https://apps.apple.com/sa/app/mobills-budget-plan- https://apps.apple.com/sa/app/1money-expense-
ner/id921838244?l=ar. [Accessed 15 9 2024]. tracker/id1623655243?l=ar. [Accessed 19 9 2024].
30. "Goodbudget - Budget Planner," Apple App Store, 37. "Buddy Money - Budget Planner," Apple App Store,
[Online]. Available: [Online]. Available:
https://apps.apple.com/sa/app/goodbudget-budget- https://apps.apple.com/sa/app/buddy-money-budget-
planner/id471112395. [Accessed 12 9 2024]. planner/id936422955. [Accessed 19 9 2024].
31. "Moneon - My Budget & Expenses," Apple App Store, 38. ComputingVictor. Financial Transactions Dataset:
[Online]. Available: Analytics [dataset on the Internet]. Kaggle; undated
https://apps.apple.com/sa/app/moneon-my-budgetex- [Accessed 14 5 2024]. Available from:
penses/id906363437?l=ar. [Accessed 18 9 2024]. https://www.kaggle.com/…
32. "Spending Tracker - Money Flow," Apple App Store,
[Online]. Available: