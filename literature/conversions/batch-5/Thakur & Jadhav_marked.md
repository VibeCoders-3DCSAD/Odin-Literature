---
conversion_metadata:
  converted_at: "2026-07-21T08:58:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Thakur & Jadhav.pdf"
  source_pdf_sha256: "3acc1e20f775556b4e811d13c8c7c4d49401d4365b1411787a21accc11b39696"
  page_count: 11
  markdown_char_count: 87689
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

Sigma Journal of Engineering and Natural Sciences
Web page info: https://sigma.yildiz.edu.tr
DOI: 10.14744/sigma.2025.00119

Research Article

Expense tracker management system using machine learning

Rishiraj Singh THAKUR1

, Akshay JADHAV1,*

1Department of Computer Science and Engineering, Manipal University Jaipur, Jaipur, 303007, India

ARTICLE INFO

Article history
Received: 28 May 2024 
Revised: 05 August 2024 
Accepted: 22 August 2024

Keywords:
Ensemble Learning; Expense 
Tracker System; Machine 
Learning; Regression

ABSTRACT

The transition from “Income and Expense Tracker” to “Expense Tracker Management Sys-
tem” marks a strategic evolution in financial management tools. This shift underscores a more 
focused  approach  towards  efficiently  tracking  and  managing  expenses.  While  the  former 
emphasized both income and expenses, the latter places a heightened emphasis on expense 
management specifically. This refined system aims to streamline expense tracking processes, 
offering users a robust platform to meticulously monitor and analyze their spending habits. 
Through customizable features, intuitive interfaces, and comprehensive reporting functional-
ities, the “Expense Tracker Management System” empowers users to take full control of their 
finances,  fostering  greater  financial  awareness  and  facilitating  smarter  spending  decisions 
which makes it better than the existing state-of-the-art. The article also emphasizes predicting 
future  expenses  based  on  prior  experience  of  the  user,  using  machine  learning  techniques. 
Different  machine  learning  techniques  are  used  for  prediction  purposes  such  as  multi-lay-
er perceptron, extreme gradient boosting, support vector machine and ensemble techniques 
such as bagging, boosting. Extreme Boost (XGBoost) outperforms other individual models 
with highest R-square value and voting ensemble regressor outperforms ensemble techniques 
with highest R-square value of 78.11% and lowest relative absolute error of 0.6121.

Cite this article as: Thakur RS, Jadhav A. Expense tracker management system using machine 
learning. Sigma J Eng Nat Sci 2025;43(4):1265−1275.

INTRODUCTION

Introducing

the  “Expense  Tracker  Management 
System,”  a  cutting-edge  solution  designed  to  revolution-
ize  the  way  individuals  track  and  manage  their  expenses 
in today’s fast-paced world. Since the dawn of civilization, 
economic  transactions  have  been  a  fundamental  aspect 
of  human  existence,  evolving  into  an  indispensable  com-
ponent  of  daily  life.  With  most  individuals  operating  on 
fixed  incomes,  effective  budgeting  becomes  paramount,

necessitating  the  meticulous  tracking  of  expenditures  to 
ensure financial stability.

Traditionally, expense tracking involved laborious man-
ual methods, such as recording transactions with pen and 
paper.  However,  the  proliferation  of  electronic  devices, 
notably smartphones and computers, has ushered in a new 
era of convenience and efficiency. Today, a myriad of soft-
ware applications exists to assist users in monitoring their 
daily expenses, providing invaluable insights into spending 
habits and ensuring adherence to budgetary constraints.

*Corresponding author.
*E-mail address: akshay.jadhav@jaipur.manipal.edu, akshay15jadhav93@gmail.com

This paper was recommended for publication in revised form by 
Editor-in-Chief Ahmet Selim Dalkilic

Published by Yıldız Technical University Press, İstanbul, Turkey
© Author. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-nc/4.0/).

---

<!-- PAGE 2 -->

1266

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

Despite  the  availability  of  expense  tracking  apps,  many 
still rely on manual input systems, which can be time-con-
suming  and  prone  to  error.  Recognizing  this  challenge,  we 
propose  an  innovative  approach  to  expense  management 
that leverages automation to streamline the process. Our sys-
tem aims to offer users a seamless and efficient experience, 
allowing  them  to  input,  track,  and  monitor  their  expenses 
with  ease.  At  the  heart  of  our  solution  lies  the  concept  of 
automation,  which  eliminates  the  need  for  manual  data 
entry and significantly reduces the time and effort required 
to manage expenses. By harnessing the power of technology, 
users can effortlessly stay on top of their finances, ensuring 
that expenditures remain within budgetary limits.

The  “Expense  Tracker  Management  System”  offers 
a  comprehensive  suite  of  features  designed  to  meet  the 
diverse  needs  of  users.  From  categorizing  expenses  into 
predefined  categories  such  as  food,  entertainment,  trans-
portation,  education,  health,  and  clothing  to  generating 
detailed reports of spending patterns, our system provides 
users  with  invaluable  insights  into  their  financial  health. 
Furthermore, our system incorporates predictive analytics 
capabilities, allowing users to forecast their monthly bud-
gets  with  precision.  By  analyzing  past  spending  patterns 
and income trends, the system can generate accurate pro-
jections,  empowering  users  to  make  informed  financial 
decisions and avoid budgetary pitfalls.

In  addition  to  its  predictive  capabilities,  the  “Expense 
Tracker  Management  System”  also  offers  real-time  notifi-
cations and alerts to keep users informed about their finan-
cial status. Whether it’s a reminder to pay bills or a warning 
that expenses are approaching budgetary limits, our system 
ensures  that  users  always  stay  proactive  and  in  control  of 
their finances.

Overall,  the  “Expense  Tracker  Management  System” 
represents a paradigm shift in the way individuals approach 
expense  tracking  and  management.  Our  platform  is 
designed  to  offer  users  a  customized  experience  through 
a  personalized  dashboard,  enabling  seamless  financial 
management.
•  Personalized  Dashboard:  Our  platform  features  a  per-
sonalized  dashboard,  eliminating  the  need  for  generic 
interfaces. This dashboard is uniquely crafted to adapt 
to individual financial needs and preferences, providing 
users with a comprehensive overview of their financial 
status briefly.

•  Advanced Expense Categorization: Simplifying expense 
tracking is at the core of our platform’s functionalities. 
With our advanced categorization feature, users benefit 
from intelligent expense management capabilities. This 
system efficiently categorizes expenses, facilitating eas-
ier tracking and analysis of spending habits.
Intelligent Alerts and Notifications: Ensuring users stay 
informed  and  in  control  is  paramount.  Our  platform 
incorporates intelligent alerts and notifications to keep 
users updated on significant financial events, impend-
ing bill payments, and deviations in spending patterns.

•

This  proactive  approach  ensures  users  remain  vigilant 
and responsive to their financial circumstances.
The  article  delves  into  how  machine  learning  tech-
niques are leveraged to predict future expenses based on 
the prior experiences of users. This involves analyzing past 
spending patterns and behaviors to forecast future finan-
cial  needs  and  trends.  In  recent  years,  machine  learning 
(ML) has experienced significant growth and has demon-
strated  its  potential  across  a  wide  array  of  applications. 
This expansion is driven by the ability of ML algorithms to 
process vast amounts of data and extract meaningful pat-
terns,  leading  to  smarter,  more  efficient,  and  innovative 
solutions across various fields. By leveraging these diverse 
machine  learning  techniques,  financial  institutions  and 
services can offer more accurate and personalized expense 
predictions.  This  helps  users  manage  their  finances  bet-
ter, anticipate future spending needs, and make informed 
financial decisions.

Let’s  review  the  existing  methods  and  analyses  previ-
ously conducted in this domain. The article examines some 
of these prior works and identifies the limitations that our 
work  aims  to  address.  The  state-of-the-art  description  of 
existing work is discussed in Table 1.

The rest of the article is organized as follows: after dis-
cussing introduction and literature review, which provides 
insight  of  the  existing  expense  tracker  management  sys-
tem, Section 2 provides information on the dataset utilized 
for  experimentation,  along  with  description  of  machine 
learning  models.  Section  3  discusses  the  proposed  work. 
Section 4 illustrates results and outcomes in terms of eval-
uation metrics and web application design. Finally, section 
5 discusses concluding remarks and recommendations for 
future work.

MATERIALS AND METHODS

The  section  discusses  the  details  of  dataset  utilized  in 
our  experiment,  along  with  different  machine  learning 
models applied to predict expenses.

Dataset Description

The “Daily Household Transactions” [16] file contains 
information  about  the  virtual  transactions  people  make 
every  day.  This  information  includes  information  about 
the  products  purchased,  the  price  used  for  each  product, 
the date and time of each transaction, the payment for each 
transaction,  and  the  location  of  each  document  (debit/
income). Data can be used to analyze purchasing behavior 
and financial management, estimate expenses, and develop 
savings  strategies  and  budgets.  This  data  is  ideal  for  data 
analysis and machine learning and can be used to train pre-
dictive models and make decisions from the data. The data-
set attributes are as follows.
•  Date: The date and time of the transaction
•  Mode: The payment method used for the transaction

---

<!-- PAGE 3 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

1267

Table 1. A state-of-the-art description on existing work

Reference Area of focus

Dataset

Parameter

Limitation

Expense Tracking 
Application

Amount

N/A

Categories, Date,

·  Manual input required for adding expenses.

Expense Tracking 
Application

N/A

Expense History, View 
Analytics, PDF Reports

·

Limited categories available for tracking 
expenses.

•  Limited platform availability (Android only).

•  Data compatibility concerns

•  Dependency on internet for updates

Expense Tracking 
Application

N/A

Email Verification, 
Analysis, Prediction

•  Not suitable for complex data analysis, only

suitable for simple daily expenses.

Expense Tracking,

Financial Analysis,

Income 
Records

Budget Planning

Application Features N/A

Application Features N/A

Expense Tracking 
Application

N/A

Mobile Application 
Development

N/A

User Experience

Online Income and 
Expense Tracker

N/A

Income and expense 
daily tracker system

N/A

Spending, Income,

•  Relies on user-entered data.

Trends

Registration, Sign-in, 
Categorization, Graphs

Registration, Income/ 
Expense, Views, Export

Expense amount, date, 
category, merchant, notes, 
optional parameters

Income, Expense Limits, 
Savings, Interface, etc.

•  Time-consuming manual entry

•  Lack of automatic reminders for daily

expenditure.

•  Limited data analysis capabilities.

•

Suitable for basic expenses

•  User adaptation and learning curve,

accessibility for diverse user demographics, 
effectiveness of reminder system

Spending, Income,

•  Lack of Mobile Application

Categories, Date,

•  Limited Integration with Financial

Amount

Registration, Income/
Expense, Email 
Verification, Analysis

Institutions

•  Dependence on Manual Data Entry

•  Requested in table form

Expense Tracker: 
Window Application

N/A

Expense Monitoring,

•  Platform limitation

Window application

•  Manual Entry

Expense 
Management System

N/A

AI based application, 
expense monitoring

•  No automation in expense tracking.

•  Recommendations depends heavily on 
the accuracy of user-provided data and 
thresholds.

Expense Tracker 
Application

Firebase as 
online dataset 
for messages.

Using Naïve Bayes to detect 
bank messages.

•  Manual expenses entry.

•  No automation in expense tracking.

•  Limited features

•  No automation in expense tracking.

Expenses Tracker 
App

N/A

Flutter framework which 
comprises expense entry, 
monthly budget setting

Income and Expense 
Tracker

N/A

Add income and expense, 
add category, export files

•  Limited platform availability (Android only).

•  Manual Entry

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

[11]

[12]

[13]

[14]

[15]

---

<!-- PAGE 4 -->

1268

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

•  Category:  Transactions  are  grouped

into  various

categories

•  Subcategory: Categories are further divided into subcat-

egories of transactions

•  Note: A short description of the transaction
•  Amount: The transaction amounts
•

Income/Expense:  Indicates  whether  the  transaction  is 
an expense or income.

•  Currency:  All  transactions  are  recorded  in  the  official

currency of India

Machine Learning Models

Nowadays, machine learning has potential applications 
which  continues  to  evolve  and  expand  into  new  various 
areas  such  as  healthcare,  finance,  industry  etc.  By  lever-
aging vast amounts of data and advanced algorithms, ML 
enables  smarter,  more  efficient,  and  innovative  solutions 
across various fields [17].
•  Extreme Gradient Boosting (XGBoost): XGBoost is an 
efficient version of the gradient boosting algorithm. It 
creates  a  sequential  decision  tree,  where  each  subse-
quent  tree  corrects  the  mistakes  of  the  previous  ones. 
Known for its efficiency and effectiveness. XGBoost is 
widely  used  in  many  machine-learning  fields  such  as 
classification, regression, and ranking. Each tree is built 
using a random subset of features, and predictions from 
individual trees are combined through voting or averag-
ing to make the final prediction.

•  Random  Forest  (RF):  is  an  ensemble  learning  method 
that  combines  multiple  decision  trees  to  improve  the 
predictive accuracy and robustness of a model. Random 
forests  are  valuable  for  their  robustness  against  overfit-
ting and their suitability for classification and regression 
problems. The hyperplane that best separates the classes. 
•  SVM  (Support  Vector  Machine):  SVM,  which  allows 
the separation of classes, is useful in large areas and in 
cases  where  the  number  of  features  is  larger  than  the 
sample. It finds application in classification and rework-
ing, especially in cases where classes are separated. Hide 
and reveal layers.

•  Multi-Layer Perceptron (MLP): MLP is trained using a 
regression model that adjusts the weights of neurons to 
reduce the error between predictions and actual results. 
MLP is known for its ability to learn nonlinear relation-
ships  and  is  often  used  in  tasks  such  as  classification, 
regression, and pattern recognition.

•  K-Nearest  Neighbors  (KNN):  It  predicts  the  class  of 
data  points  by  identifying  the  class  of  most  of  their 
nearest neighbors (for classification) or by the average 
value of its neighbor (for regression). The performance 
of KNN depends on the distance measure choice and k 
value. Each classification is determined by the value of 
the selected item, creating a tree-like structure.

•  Decision Tree (DT): Decision trees are easy to interpret 
and visualize and are useful for understanding the deci-
sion-making process. However, they are easy to overfit,

especially  for  complex  data  that  can  be  resolved  with 
techniques such as pruning and integration.

•  Extra  Tree  (ET):  ET  is  an  ensemble  learning  method 
that  aggregates  the  predictions  of  multiple  de-cor-
related decision trees collected in a “forest” to improve 
the predictive accuracy and control overfitting. Unlike 
Random  Forest,  which  selects  optimal  cut-points  for 
splits, Extra Trees split nodes using random cut-points 
for  each  feature,  which  introduces  more  randomness 
into the model.

•  Categorical  Boosting  (CatBoost):  CatBoost  incorpo-
rates advanced techniques like ordered boosting, which 
improves  training  speed  and  reduces  overfitting.  Its 
strength  lies  in  its  robustness,  ease  of  use,  and  ability 
to  deliver  high-quality  predictions  on  a  wide  range  of 
datasets without extensive hyperparameter tuning.

Ensemble Learning Models

Ensemble  learning  [18,  19]  is  a  technique  in  machine 
learning where we combine the predictions of several dif-
ferent models to make a stronger and more accurate model 
than any individual model. By pooling together predictions 
from diverse models, ensemble learning helps to reduce the 
weaknesses  of  individual  models  while  maximizing  their 
strengths, resulting in better overall performance [20].
•  Bagging:  Involves  training  multiple  instances  of  the 
same  base  model  on  different  subsets  of  the  training 
data and averaging their predictions.

•  Boosting: Builds a strong learner by sequentially train-
ing  multiple  weak  learners,  where  each  subsequent 
learner  focuses  more  on  the  misclassified  instances 
from the previous learners.

•  Stacking: Involves training multiple base models and then 
using a meta-model to combine their predictions, treating 
the predictions of base models as additional features.
•  Voting: Combines the predictions of multiple models by 
aggregating their individual predictions using a simple 
voting mechanism (e.g., majority vote for classification 
or averaging for regression).

•  Blending: Blending is like stacking, but it uses a holdout 
set (a part of the training set) to generate predictions for 
the  training  set  of  the  meta-model.  This  can  be  more 
robust  than  voting  or  a  single  layer  of  models  since  it 
incorporates multiple stages of learning and validation.

PROPOSED WORK

The  section  discusses  the  proposed  work  in  terms  of 
data  preparation  phase  and  regression  phase.  The  “Daily 
Household  Transaction”  dataset  is  pre-processed  to  apply 
machine  learning  models  for  training  and  predicting 
expenses.  The  data  preprocessing  is  divided  into  multiple 
steps;  the  first  step  is  normalization  using  MinMax  scal-
ing  technique  which  scales  each  feature  to  a  given  range, 
between 0 and 1 [21]. This scaling is useful when you want 
all features to be on a similar scale, which can improve the

---

<!-- PAGE 5 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

1269

Error, Mean Square Error and Relative absolute error. These 
are  the  common  parameters  used  in  regression  analysis. 
They  provide  different  perspectives  on  how  well  a  model 
is performing.

R-squared (R2) value

Also  known  as  the  coefficient  of  determination, 
R-squared measures the proportion of the variance in the 
dependent  variable  (target)  that  is  predictable  from  the 
independent variables (features). Higher R-squared scores 
(closer to 1) indicate better model fit.

(1)

where,  SSres  and  SStot  the  sum  of  the  squared  differences 
between the observed values and the predicted values, and 
the  sum  of  the  squared  differences  between  the  observed 
values and the mean of the observed values respectively.

Mean absolute error (MAE)

This metric quantifies the average magnitude of errors 
between  predicted  and  actual  values.  Lower  MAE  values 
indicate better model performance.

(2)

where,  n  is  the  number  of  observations,  yi  is  the  actual 
value, and ŷi is the predicted value.

Mean square error (MSE)

MSE measures the average of the squares of the errors 
that  is,  the  average  squared  difference  between  the  actual 
values and the predicted values.

(3)

where,  n  is  the  number  of  observations,  yi  is  the  actual 
value, and ŷi is the predicted value.

Relative absolute error (RAE)

RAE measures the total absolute error as a proportion 
of the total absolute error of a simple predictor, such as the 
mean of the actual values. It provides a normalized measure 
of prediction accuracy.

(4)

where, n is the number of observations, yi is the actual value, 
 is the mean of actual value. 
ŷi is the predicted value, and 
The R-square value provides an indication of how well 
the model’s predictions match the actual data. MAE mea-
sures the average magnitude of errors in a set of predic-
tions.  Relative  absolute  error  is  particularly  useful  when

Figure  1.  Data  Transformation,  distribution  of 
(1+amount).

log

performance  of  many  machine  learning  algorithms.  In 
second  step  is  transformation  of  amount  attribute  using 
‘log1p’ function. The log1p function computes the natural 
logarithm of ‘1 + x’, which is useful for transforming data 
(amount in our case) that may contain zero or small posi-
tive values as shown in Figure 1.

Lastly, the third step in data preprocessing is vectorizer 
process  using  ‘TfidfVectorizer  (min_df=3)’,  it  transforms 
text data into numerical values based on the term frequen-
cy-inverse document frequency (TF-IDF) statistic, param-
eter ‘min_df =3’ specifies that only terms (words or tokens; 
in our case ‘Mode’, ‘Category’,’ Subcategory’, ‘Note’, ‘Income/
Expense’)  that  appear  in  at  least  three  documents  will  be 
considered, reducing noise and dimensionality. By convert-
ing the text data into TF-IDF vectors, it transforms the text 
into a numerical format that can be fed into algorithms.

After  successful  preprocessing,  the  dataset  is  divided 
into the ratio of 70:30, where 70% is used for training and 
30% is used for testing purposes. The next phase is regres-
sion phase, the training data and testing data is fed to mul-
tiple  machine  learning  models  and  predictions  are  made, 
evaluated using two regression metrics; r-squared value and 
mean absolute error.

RESULTS AND DISCUSSION

The  section  discusses  the  evaluation  parameters  used 
in the experiment, along with a description, results of the 
machine  learning  model.  The  section  also  showcases  the 
web  application  description  and  screenshots  of  the  web 
application for better understanding.

Evaluation Parameters

The results of the Expense Tracker Management System 
are evaluated in terms of R-squared value, Mean Absolute

---

<!-- PAGE 6 -->

1270

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

comparing different models. Mean square error is a pre-
ferred metric for optimizing and assessing model fitness, 
also  offers  an  absolute  measure  of  predictive  accuracy. 
The  performance  of  the  different  machine  learning  and 
ensemble  models  is  evaluated  over  these  metrics  and  is 
shown in Table 2.

The  results  in  Table  2  showcase  the  performance  of 
individual machine learning models and ensemble learn-
ing  techniques.  The  parameter  tuning  process  for  the 
selected  machine  learning  models  involves  identifying 
key  hyperparameters  such  as  learning  rate  for  XGBoost 
or number of neighbors for KNN, by using Hit and Trial 
method.  The  models  are  evaluated  based  on  perfor-
mance  metrics  such  as  R-squared  and  Mean  Absolute 
Error  through  cross-validation  to  prevent  overfitting. 
The  best-performing  hyperparameters  are  selected  and 
validated  on  a  test  set  to  ensure  that  improvements  are 
generalizable to new data. The performance of XGBoost 
technique  outperforms  other  individual  machine  learn-
ing  models  with  a  highest  r-square  value  of  77.89,  while 
Voting Ensemble Regressor outperforms individual mod-
els and other ensemble approaches with highest r-square 
value of 78.11 and lowest relative absolute error of 0.1765. 
As  r-square  value  is  a  useful  metric  for  evaluating  the 
explanatory power of a model, it does not always provide a 
complete picture of model performance. Since there is no 
more  difference  in  the  r-square  value  of  models  because 
of characteristics of the dataset, as the distribution of the 
variables and the nature of their relationships, explaining 
the same amount of variance. RAE stands out be the decid-
ing factor in our approach as the RAE of voting ensemble 
regressor is lowest.

Web Application Development

The  application  development  for  expense  tracking 
involves  ensuring  seamless  user  experience  by  incorpo-
rating features such as income and expense limits, savings 
tracking,  and  intuitive  interfaces.  The  effectiveness  of  the 
reminder system is crucial for user engagement and adher-
ence to budgeting goals. A user-friendly design reduces the 
learning curve, making the app accessible to diverse demo-
graphics. The framework behind the application develop-
ment is described below.

Backend Development

•  Django (Python): Django is chosen for its robust frame-
work and extensive built-in features, which streamline 
the development process.
ü  Django’s  Built-in  Authentication:  Implement  role-
based access control (RBAC) using Django’s authen-
tication system.

ü  Django Paginator Class: Implement server-side pag-

ination for efficient data management.

ü  Django  Admin  Customization:  Customize  the

Django Admin interface for better usability.
•  Database:  PostgreSQL  is  selected  for  its  reliability, 
robustness,  and  support  for  complex  queries  and 
transactions.

Frontend Development
•  HTML, CSS, JavaScript
•  Ajax: Use jQuery for making asynchronous requests to

the server.
ü  JavaScript  and  Django:  Develop  Ajax-based  search 
functionality for querying the database in real-time.

Table 2. Performance of machine learning models

Model

R-squared(R2) value

Mean absolute error Mean square error Relative absolute error

Individual models

XGBoost

Random forest

SVM

MLP

KNN

Decision tree

Extra tree

CatBoost

Ensemble Models

Bagging

Boosting

Stacking

Voting

Blending

77.89

77.02

72.41

74.81

69.58

70.89

75.68

76.02

76.34

75.89

73.56

78.11

74.37

0.6324

0.6150

0.6943

0.6439

0.6956

0.6701

0.6107

0.7020

0.6217

0.6208

0.6613

0.6121

0.6731

0.9399

0.9773

1.1734

1.0716

1.2937

1.2378

1.0344

1.0199

-

-

1.0604

0.9648

1.0439

0.1919

0.1919

0.1919

0.1919

0.1919

0.1919

0.1919

0.1919

0.1835

0.1852

0.1939

0.1765

0.1909

---

<!-- PAGE 7 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

1271

ü  Chart.js: Use JavaScript charting libraries to display

data visually on the frontend.

•  Client-side Validation: Implement client-side validation 
using JavaScript and the jQuery Validation library.
•  Server-side Validation: Utilize Django form validation.

Key Components

1.  User  Authentication  and  Security:  Utilize  Django’s 
built-in authentication for user registration, login, and 
role-based access control (RBAC).

2.  Expense  Tracking:  Allow  users  to  manually  enter

expenses via forms.

3.  Expense  Categorization:  Predefined  Categories  which 
provide categories such as food, transportation, enter-
tainment,  and  utilities.  Also,  custom  categories  which 
allow users to create custom categories.

4.  Analytics and Reporting

ü  Visual  Reports:  Generate  visual  reports  using

JavaScript charting libraries like Chart.js.

ü  Predictive  Analytics:  Implement  machine  learning

models for expense prediction.

ü  Budget Forecasting: Offer monthly budget forecasts

and highlight potential overspending areas.

Application Description

in  Django

The  section  provides  the  screenshots  of  the  appli-
cation and its working in the form of description. User 
authentication 
involves  configuring  the 
built-in authentication system, creating login views and 
templates,  and  managing  user  sessions  using  functions 
like `login()` and `logout()`. User authorization utilizes 
Django’s permissions system, where permissions can be 
defined at the model level and enforced using decorators 
like `@login_required` to restrict access to views based 
on authentication status. Customization can be done by 
creating custom authentication backends or user models 
to suit specific requirements, the login page is shown in 
Figure 2.

Figure 2. Login page.

The  expense  tracker  management  system  provides  a 
detailed expense summary that offers users a comprehen-
sive view of their financial activity. The summary includes 
the total expenses for a selected period, along with a break-
down by categories such as food, transportation, and enter-
tainment,  visualized  through  pie  or  bar  charts  as  shown 
in  Figure  3.  Monthly  spending  trends  are  depicted  using 
line charts, highlighting patterns and significant variances. 
Detailed transaction lists are available for review, showing 
individual expenses with dates, amounts, and descriptions. 
Users can also see their top expenses, compare their actual 
spending against budget limits with progress bars, and view 
predictive analytics for future expenses. Additionally, a sav-
ings overview indicates the total savings achieved, helping 
users monitor their financial goals effectively. To enhance 
financial management, the system allows users to create and 
manage custom expense categories, provides expense fore-
casting  through  advanced  algorithms,  and  tracks  income 
sources alongside expenses for a complete financial picture.
The income summary in the expense tracker manage-
ment system offers  users a clear and  detailed  overview  of 
their  earnings  over  a  specified  period  as  shown  in  Figure 
4.  It  includes  the  total  income  received,  broken  down  by 
sources  such  as  salary,  freelance  work,  and  other  income 
streams. This breakdown is visualized through charts like

Figure 3. Expense summary.

---

<!-- PAGE 8 -->

1272

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

Figure 4. Income summary.

pie charts or bar graphs for easy analysis. Monthly income 
trends are displayed using line charts, helping users iden-
tify  patterns  and  variations  in  their  earnings.  A  detailed 
list  of  income  transactions  is  provided,  showing  dates, 
amounts,  and  sources,  enabling  users  to  verify  and  track 
their  earnings  accurately.  The  summary  also  compares 
actual income against projected income targets, highlight-
ing any discrepancies. Overall, the Income Summary helps 
users  understand  their  financial  inflows,  track  perfor-
mance against income goals, and plan for future financial 
stability.  Additionally,  users  can  set  and  monitor  income 
goals,  and  the  system  offers  projections  based  on  histori-
cal data and trends. The Income Summary integrates with 
other  financial  reports  to  provide  a  comprehensive  view 
of  overall  financial  health.  Overall,  the  Income  Summary 
helps users understand their financial inflows, track perfor-
mance against income goals, and plan for future financial 
stability, ultimately aiding in better budgeting and financial 
decision-making.

Expense  entry  in  the  expense  tracker  management 
system  involves  creating  a  model  to  represent  individual 
expenses, including fields such as the amount, description, 
date, and category as depicted in Figure 5. Users can input 
their  expenses  through  a  form  or  API  endpoint,  which

validates the data and saves it to the database. Additionally, 
expense  entry  functionalities  may  include  the  ability  to 
view,  update,  and  delete  existing  expenses  and  features 
like  filtering  and  sorting  to  analyze  spending  patterns. 
Additionally, expense entry functionalities include the abil-
ity to view, update, and delete  existing expenses,  and fea-
tures like filtering and sorting to analyze spending patterns. 
Users  can  categorize  expenses  for  more  detailed  tracking 
and  apply  tags  for  specific  projects  or  events.  The  system 
also provides tools to generate expense reports and visual-
ize spending trends over time.

The income entry feature in the expense tracker man-
agement system enables users to easily record and manage 
their  earnings.  Users  can  input  details  such  as  the  date, 
source,  amount,  and  mode  of  payment  for  each  income 
entry,  ensuring  accurate  and  comprehensive  financial 
records as shown in Figure 6. They can also add descrip-
tions and categorize their income to facilitate better track-
ing  and  analysis.  Additionally,  the  system  allows  users  to 
mark  certain  income  entries  as  recurring,  automating 
future  entries  and  saving  time.  Once  entered,  the  income 
details are saved and displayed in the income summary and 
transaction list, where users can view, edit, or delete entries 
as  needed.  This  streamlined  process  helps  users  maintain

Figure 5. Expense entry.

---

<!-- PAGE 9 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

1273

Figure 6. Income entry.

an  accurate  overview  of  their  financial  inflows,  aiding  in 
budgeting and financial planning.

Expense categorization in the expense tracker manage-
ment system allows users to classify their expenses into pre-
defined categories for better organization and analysis. This 
involves  creating  a  model  for  expense  categories,  which 
typically includes fields like name, description, and possi-
bly a color or icon for visual distinction such as in Figure 7, 
it indicates shopping, food, rent and other. Users can assign 
categories  to  their  expenses  either  manually  or  through 
automated rules. The system may provide features for man-
aging categories, such as adding, editing, or deleting them, 
as well as reporting functionalities to track spending across 
different categories over time.

Figure 8 depicts the search and filter capabilities in the 
debt tracking system allow customers to effectively and effi-
ciently identify their debts based on specific criteria. This 
includes using features that allow users to search for debt 
using keywords or phrases, filter debt by attributes such as 
date, category, price or description, and combine multiple

filters to narrow down. The system may provide user inter-
faces such as a search bar, drop-down menu, or date picker 
to  facilitate  filter  selection.  Additionally,  advanced  filter 
options such as sorting by relevance or custom filter presets 
can improve user experience and productivity.

Application Benefits

Our  application  outperforms  other  applications  from 
the  state-of-the-art  discussed  in  the  literature.  Here  are 
some points which outstand our application.
•  Advanced  Analytics  and  Prediction:  Existing  systems 
often provide basic data analysis and are limited to sim-
ple  expense  tracking.  Our  system  leverages  machine 
learning  for  advanced  analytics  and  precise  expense 
predictions,  offering  users  a  deeper  understanding  of 
their financial patterns.

•  Customizable  Reporting:  Earlier  solutions  often  offer 
limited  customization  for  financial  reports  and  cat-
egories.  Our  system  provides  extensive  options  for

Figure 7. Expense categorization.

---

<!-- PAGE 10 -->

1274

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

Figure 8. Search and filtering.

customizing categories, reports, and catering to diverse 
user needs and preferences.

•

•  User-Friendly Design: Older systems might have com-
plex interfaces. Our application features a simple, intui-
tive design, making it easy for users to navigate and use 
effectively.
Interactive  Dashboards:  Existing  solutions  might  offer 
static  reports.  Our  system  features  interactive  dash-
boards  that  allow  users  to  explore  their  financial  data 
through dynamic charts and graphs.
Our proposed ML based Expense Tracker Management 
System  helps 
individuals  and  organizations  manage 
finances by using machine learning to predict and analyze 
expenses. Its features offer valuable insights into spending 
patterns,  benefiting  personal  finance  enthusiasts,  small 
businesses,  and  financial  advisors  by  improving  budget-
ing and financial planning. The findings from the Expense 
Tracker  Management  System  demonstrate  its  effective-
ness  in  predicting  and  analyzing  expenses  using  machine 
learning. These insights are valuable for a broad audience, 
including  individuals  managing  personal  finances  and 
small businesses optimizing budgets.

CONCLUSION

Expense  Tracker  Management  System  provides  indi-
viduals  and  businesses  with  effective  solutions  to  track, 
analyze, and manage their spending through intuitive and 
powerful features such as categorization, fundraising, and 
advertising recommendations to present to users. Financial 
gaining control over their situation improving health clean 
budgeting  and  decisions  access  across  multiple  devices 
and improving accountability and transparency, especially 
in  an  environment  where  many  people  can  integrate  and

share  future  expenses  transactions  can  include  scanning 
of  receipts  and  instant  integration  with  bank  accounts 
Features such as syncing and spend-based personal finan-
cial advice are used as important tools to promote financial 
literacy,  budgeting,  and  overall  health  for  individuals  and 
organizations.

To conclude, various machine learning techniques and 
ensemble methods like bagging, boosting, stacking, voting, 
and  blending  are  employed  for  prediction.  Among  these, 
XGBoost achieves R-squared value of 77.89%, the highest 
compared  to  other  individual  models,  while  the  voting 
ensemble regressor surpasses other ensemble methods with 
the highest R-squared value of 78.11% and the lowest rela-
tive absolute error of 0.6121. The proposed approach helps 
to forecast future expenses by analyzing users’ past spend-
ing  patterns  and  behaviors.  By  leveraging  historical  data, 
these methods provide valuable insights into future finan-
cial needs and trends of any individual or business.

The

future  evolution  of

the  Expense  Tracker 
Management System holds promise for even greater inno-
vation  and  impact.  Potential  enhancements  may  include 
integration  with  emerging  technologies  such  as  advanced 
artificial  intelligence  and  machine  learning,  enabling  pre-
dictive  analytics  for  personalized  financial  insights  and 
automated  expense  categorization.  We  aim  to  enhance 
application functionality and user experience by incorpo-
rating  automated  transaction  tracking,  cloud-based  data 
synchronization,  multi-language  support,  and  AI-driven 
recommendations. We also aim in developing a dataset for 
expense tracker system to ensure that the dataset captures 
distinct and meaningful patterns, leading to better perfor-
mance and more reliable predictions.

---

<!-- PAGE 11 -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025

1275

AUTHORSHIP CONTRIBUTIONS

Authors equally contributed to this work.

DATA AVAILABILITY STATEMENT

The  authors  confirm  that  the  data  that  supports  the 
findings of this study are available within the article. Raw 
data that support the finding of this study are available from 
the corresponding author, upon reasonable request.

CONFLICT OF INTEREST

The  author  declared  no  potential  conflicts  of  interest 
with respect to the research, authorship, and/or publication 
of this article.

ETHICS

There are no ethical issues with the publication of this

manuscript.

STATEMENT ON THE USE OF ARTIFICIAL 
INTELLIGENCE

Artificial  intelligence  was  not  used  in  the  preparation

of the article.

REFERENCES

[1]

Jadhav  NJ,  Chakor  RV,  Gun-jal  TM,  Pawar  DD. 
Expense  tracker.  Int  Res  J  Modernization  Eng 
Technol Sci 2022;4:2582–5208.

[2]  Masendu  TR,  Tripath  AM.  Daily  Expense  Tracker.

Int J Res Eng Sci Manag 2022;5:90–92.

[3]  Thomas P, Lekshmi, Mahalekshmi. Expense tracker. 
Int J Adv Res Sci Commun Technol 2020;9:4. 
  [4]  Cabañero RA. Design and Development of Expense 
Management System using CodeIgniter Framework. 
Int  J  Adv  Res  Sci  Commun  Technol  2023;29:929–
935. [CrossRef]

[5]  Garg A, Goel M, Mittal S, Singh S. Expense Tracker. 
Int  J  Res  Appl  Sci  Eng  Technol  2023;9:1067–1070. 
[CrossRef]
Sakthivel  M,  Roshini  P,  Roja  K,  Maha  Lakshmi  P, 
Keerthi  V.  Personal  Expense  Tracker  Application. 
Int J Res Appl Sci Eng Technol 2023;8:2031–2038.

[6]

[7]  Noorsumar  MH,  Supalkar  SS,  Singh  H,  Udeshi 
TU.  Expense  Tracker.  Int  Res  J  Eng  Technol 
2023;11:195-201.

[8]  Patil  P,  Ahmed  MM,  Kamble  R,  Gaikwad  N. 
Personal  Expenses  Tracker.  Int  J  Res  Publ  Rev 
2023;4:4357–4359.

[10]

[9]  Chandini  S,  Poojitha  T,  Ranjith  D,  Mohammed 
Akram  VJ,  Vani  MS,  Rajyalakshmi  V.  Online 
Income and Expense Tracker. Int Res J Eng Technol 
2019;6:11110.
Saravade PS, Molak PR, Jadhav BS, Khare KP, Lokare 
SM. Income and expense daıly tracker system. Int J 
Innovations Eng Res Technol 2023;11:86–89.
[11]  Gupta  H,  Singh  AP,  Kumar  N,  Blessy  JA.  Expense 
Tracker:  A  Smart  Approach  to  Track  Everyday 
Expense. EasyChair Preprint 2020;4809.
Johri  E,  Desai  P,  Soni  P,  Jain  H,  Sanganeria  N. 
Expense  Management  System.  In:  2023  4th  IEEE 
Global Conference for Advancement in Technology 
(GCAT); 2023. p. 1–6. [CrossRef]

[12]

[13]  Thakare  R,  Thakare  N,  Sangtani  R,  Bondre  S, 
Manekar A. Expense tracker application using naive 
bayes. Int J Recent Eng Sci 2023;10:50–56. [CrossRef]

[14]  Laishram  C.  Design  and  Development  of  an 
Expenses Tracker App using the Flutter Framework. 
Amity J Comput Sci 2023;7:2.

[15]  Thanapal P, Patel MY, Raj TL, Kumar JS. Income and 
expense tracker. Indian J Sci Technol 2015;8(Suppl 
2):118–122. [CrossRef]

[16]  Daily  Transactions  Dataset.  Kaggle  2024.  Available 
at:  https://www.kaggle.com/datasets/prasad22/dai-
ly-transactions-dataset Accessed July 21, 2025.
[17]  Doan  T,  Kalita  J.  Selecting  machine  learning  algo-
rithms  using  regression  models.  In:  2015  IEEE 
International Conference on Data Mining Workshop 
(ICDMW); 2015. p. 1498–1505. [CrossRef]

[18]  Aldave R, Dussault JP. Systematic ensemble learning 
for regression. arXiv preprint 2014;1403.7267.
[19]  Mienye  ID,  Sun  Y.  A  survey  of  ensemble  learning: 
Concepts,  algorithms,  applications,  and  prospects. 
IEEE Access 2022;10:99129–99149. [CrossRef]
[20]  Odegua  R.  An  empirical  study  of  ensemble  tech-
niques  (bagging,  boosting,  and  stacking).  In:  Proc 
Conf: Deep Learn IndabaXAt; 2019.
Jadhav A, Dhaulakhandi D, Shandilya SK, Malviya 
L,  Mewada  A.  Data  transformation:  A  preprocess-
ing stage in machine learning regression problems. 
In:  Artificial  Intelligence  Techniques  in  Power 
Systems Operations and Analysis; 2023. p. 183–194. 
Auerbach Publications. [CrossRef]

[21]

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
Sigma Journal of Engineering and Natural Sciences
Web page info: https://sigma.yildiz.edu.tr
DOI: 10.14744/sigma.2025.00119
Research Article
Expense tracker management system using machine learning
Rishiraj Singh THAKUR1 , Akshay JADHAV1,*
1Department of Computer Science and Engineering, Manipal University Jaipur, Jaipur, 303007, India
ARTICLE INFO
ABSTRACT
Article history
Received: 28 May 2024 The transition from “Income and Expense Tracker” to “Expense Tracker Management Sys-
Revised: 05 August 2024 tem” marks a strategic evolution in financial management tools. This shift underscores a more
Accepted: 22 August 2024 focused approach towards efficiently tracking and managing expenses. While the former
emphasized both income and expenses, the latter places a heightened emphasis on expense
Keywords: management specifically. This refined system aims to streamline expense tracking processes,
Ensemble Learning; Expense offering users a robust platform to meticulously monitor and analyze their spending habits.
Tracker System; Machine Through customizable features, intuitive interfaces, and comprehensive reporting functional-
Learning; Regression ities, the “Expense Tracker Management System” empowers users to take full control of their
finances, fostering greater financial awareness and facilitating smarter spending decisions
which makes it better than the existing state-of-the-art. The article also emphasizes predicting
future expenses based on prior experience of the user, using machine learning techniques.
Different machine learning techniques are used for prediction purposes such as multi-lay-
er perceptron, extreme gradient boosting, support vector machine and ensemble techniques
such as bagging, boosting. Extreme Boost (XGBoost) outperforms other individual models
with highest R-square value and voting ensemble regressor outperforms ensemble techniques
with highest R-square value of 78.11% and lowest relative absolute error of 0.6121.
Cite this article as: Thakur RS, Jadhav A. Expense tracker management system using machine
learning. Sigma J Eng Nat Sci 2025;43(4):1265−1275.
INTRODUCTION necessitating the meticulous tracking of expenditures to
ensure financial stability.
Introducing the “Expense Tracker Management
Traditionally, expense tracking involved laborious man-
System,” a cutting-edge solution designed to revolution-
ual methods, such as recording transactions with pen and
ize the way individuals track and manage their expenses
paper. However, the proliferation of electronic devices,
in today’s fast-paced world. Since the dawn of civilization,
notably smartphones and computers, has ushered in a new
economic transactions have been a fundamental aspect era of convenience and efficiency. Today, a myriad of soft-
of human existence, evolving into an indispensable com- ware applications exists to assist users in monitoring their
ponent of daily life. With most individuals operating on daily expenses, providing invaluable insights into spending
fixed incomes, effective budgeting becomes paramount, habits and ensuring adherence to budgetary constraints.
*Corresponding author.
*E-mail address: akshay.jadhav@jaipur.manipal.edu, akshay15jadhav93@gmail.com
This paper was recommended for publication in revised form by
Editor-in-Chief Ahmet Selim Dalkilic
Published by Yıldız Technical University Press, İstanbul, Turkey
© Author. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-nc/4.0/).

1266 Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
Despite the availability of expense tracking apps, many This proactive approach ensures users remain vigilant
still rely on manual input systems, which can be time-con- and responsive to their financial circumstances.
suming and prone to error. Recognizing this challenge, we The article delves into how machine learning tech-
propose an innovative approach to expense management niques are leveraged to predict future expenses based on
that leverages automation to streamline the process. Our sys- the prior experiences of users. This involves analyzing past
tem aims to offer users a seamless and efficient experience, spending patterns and behaviors to forecast future finan-
allowing them to input, track, and monitor their expenses cial needs and trends. In recent years, machine learning
with ease. At the heart of our solution lies the concept of (ML) has experienced significant growth and has demon-
automation, which eliminates the need for manual data strated its potential across a wide array of applications.
entry and significantly reduces the time and effort required This expansion is driven by the ability of ML algorithms to
to manage expenses. By harnessing the power of technology, process vast amounts of data and extract meaningful pat-
users can effortlessly stay on top of their finances, ensuring
terns, leading to smarter, more efficient, and innovative
that expenditures remain within budgetary limits.
solutions across various fields. By leveraging these diverse
The “Expense Tracker Management System” offers
machine learning techniques, financial institutions and
a comprehensive suite of features designed to meet the
services can offer more accurate and personalized expense
diverse needs of users. From categorizing expenses into
predictions. This helps users manage their finances bet-
predefined categories such as food, entertainment, trans-
ter, anticipate future spending needs, and make informed
portation, education, health, and clothing to generating
financial decisions.
detailed reports of spending patterns, our system provides
Let’s review the existing methods and analyses previ-
users with invaluable insights into their financial health.
ously conducted in this domain. The article examines some
Furthermore, our system incorporates predictive analytics
of these prior works and identifies the limitations that our
capabilities, allowing users to forecast their monthly bud-
work aims to address. The state-of-the-art description of
gets with precision. By analyzing past spending patterns
existing work is discussed in Table 1.
and income trends, the system can generate accurate pro-
The rest of the article is organized as follows: after dis-
jections, empowering users to make informed financial
cussing introduction and literature review, which provides
decisions and avoid budgetary pitfalls.
insight of the existing expense tracker management sys-
In addition to its predictive capabilities, the “Expense
tem, Section 2 provides information on the dataset utilized
Tracker Management System” also offers real-time notifi-
for experimentation, along with description of machine
cations and alerts to keep users informed about their finan-
learning models. Section 3 discusses the proposed work.
cial status. Whether it’s a reminder to pay bills or a warning
Section 4 illustrates results and outcomes in terms of eval-
that expenses are approaching budgetary limits, our system
ensures that users always stay proactive and in control of uation metrics and web application design. Finally, section
their finances. 5 discusses concluding remarks and recommendations for
Overall, the “Expense Tracker Management System” future work.
represents a paradigm shift in the way individuals approach
expense tracking and management. Our platform is MATERIALS AND METHODS
designed to offer users a customized experience through
a personalized dashboard, enabling seamless financial The section discusses the details of dataset utilized in
management. our experiment, along with different machine learning
• Personalized Dashboard: Our platform features a per- models applied to predict expenses.
sonalized dashboard, eliminating the need for generic
Dataset Description
interfaces. This dashboard is uniquely crafted to adapt
The “Daily Household Transactions” [16] file contains
to individual financial needs and preferences, providing
information about the virtual transactions people make
users with a comprehensive overview of their financial
every day. This information includes information about
status briefly.
the products purchased, the price used for each product,
• Advanced Expense Categorization: Simplifying expense
tracking is at the core of our platform’s functionalities. the date and time of each transaction, the payment for each
With our advanced categorization feature, users benefit transaction, and the location of each document (debit/
from intelligent expense management capabilities. This income). Data can be used to analyze purchasing behavior
system efficiently categorizes expenses, facilitating eas- and financial management, estimate expenses, and develop
ier tracking and analysis of spending habits. savings strategies and budgets. This data is ideal for data
• Intelligent Alerts and Notifications: Ensuring users stay analysis and machine learning and can be used to train pre-
informed and in control is paramount. Our platform dictive models and make decisions from the data. The data-
incorporates intelligent alerts and notifications to keep set attributes are as follows.
users updated on significant financial events, impend- • Date: The date and time of the transaction
ing bill payments, and deviations in spending patterns. • Mode: The payment method used for the transaction

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025 1267
Table 1. A state-of-the-art description on existing work
| Reference | Area of focus | Dataset | Parameter | Limitation |
| --------- | ------------- | ------- | --------- | ---------- |
[1] Expense Tracking  N/A Categories, Date,  ·  Manual input required for adding expenses.
Application
|     |     |     | Amount | ·  Limited categories available for tracking  |
| --- | --- | --- | ------ | --------------------------------------------- |
expenses.
[2] Expense Tracking  N/A Expense History, View  •  Limited platform availability (Android only).
|     | Application |     | Analytics, PDF Reports |     |
| --- | ----------- | --- | ---------------------- | --- |
•  Data compatibility concerns
•  Dependency on internet for updates
[3] Expense Tracking  N/A Email Verification,  •  Not suitable for complex data analysis, only
Application Analysis, Prediction suitable for simple daily expenses.
[4] Expense Tracking, Income  Spending, Income,  •  Relies on user-entered data.
|     | Financial Analysis, | Records | Trends |     |
| --- | ------------------- | ------- | ------ | --- |
Budget Planning
[5] Application Features N/A Registration, Sign-in,  •  Time-consuming manual entry
Categorization, Graphs
[6] Application Features N/A Registration, Income/  •  Lack of automatic reminders for daily
|     |     |     | Expense, Views, Export | expenditure. |
| --- | --- | --- | ---------------------- | ------------ |
[7] Expense Tracking  N/A Expense amount, date,  •  Limited data analysis capabilities.
|     | Application |     | category, merchant, notes,  |     |
| --- | ----------- | --- | --------------------------- | --- |
•  Suitable for basic expenses
optional parameters
[8] Mobile Application  N/A Income, Expense Limits,  •  User adaptation and learning curve,
Development Savings, Interface, etc. accessibility for diverse user demographics,
effectiveness of reminder system
User Experience
[9] Online Income and  N/A Spending, Income,  •  Lack of Mobile Application
Expense Tracker Categories, Date,  •  Limited Integration with Financial
|     |     |     | Amount | Institutions |
| --- | --- | --- | ------ | ------------ |
[10] Income and expense  N/A Registration, Income/ •  Dependence on Manual Data Entry
|     | daily tracker system |     | Expense, Email  |     |
| --- | -------------------- | --- | --------------- | --- |
•  Requested in table form
Verification, Analysis
[11] Expense Tracker:  N/A Expense Monitoring, •  Platform limitation
Window Application
|     |     |     | Window application | •  Manual Entry |
| --- | --- | --- | ------------------ | --------------- |
•  No automation in expense tracking.
[12] Expense  N/A AI based application,  •  Recommendations depends heavily on
Management System expense monitoring the accuracy of user-provided data and
thresholds.
[13] Expense Tracker  Firebase as  Using Naïve Bayes to detect  •  Manual expenses entry.
|     | Application | online dataset  | bank messages. |     |
| --- | ----------- | --------------- | -------------- | --- |
•  No automation in expense tracking.
for messages.
•  Limited features
[14] Expenses Tracker  N/A Flutter framework which  •  No automation in expense tracking.
|     | App |     | comprises expense entry,  |     |
| --- | --- | --- | ------------------------- | --- |
monthly budget setting
[15] Income and Expense  N/A Add income and expense,  •  Limited platform availability (Android only).
|     | Tracker |     | add category, export files |     |
| --- | ------- | --- | -------------------------- | --- |
•  Manual Entry

1268 Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
• Category: Transactions are grouped into various especially for complex data that can be resolved with
categories techniques such as pruning and integration.
• Subcategory: Categories are further divided into subcat- • Extra Tree (ET): ET is an ensemble learning method
egories of transactions that aggregates the predictions of multiple de-cor-
• Note: A short description of the transaction related decision trees collected in a “forest” to improve
• Amount: The transaction amounts the predictive accuracy and control overfitting. Unlike
• Income/Expense: Indicates whether the transaction is Random Forest, which selects optimal cut-points for
an expense or income. splits, Extra Trees split nodes using random cut-points
• Currency: All transactions are recorded in the official for each feature, which introduces more randomness
currency of India into the model.
• Categorical Boosting (CatBoost): CatBoost incorpo-
Machine Learning Models
rates advanced techniques like ordered boosting, which
Nowadays, machine learning has potential applications
improves training speed and reduces overfitting. Its
which continues to evolve and expand into new various
strength lies in its robustness, ease of use, and ability
areas such as healthcare, finance, industry etc. By lever-
to deliver high-quality predictions on a wide range of
aging vast amounts of data and advanced algorithms, ML
datasets without extensive hyperparameter tuning.
enables smarter, more efficient, and innovative solutions
across various fields [17]. Ensemble Learning Models
• Extreme Gradient Boosting (XGBoost): XGBoost is an Ensemble learning [18, 19] is a technique in machine
efficient version of the gradient boosting algorithm. It learning where we combine the predictions of several dif-
creates a sequential decision tree, where each subse- ferent models to make a stronger and more accurate model
quent tree corrects the mistakes of the previous ones. than any individual model. By pooling together predictions
Known for its efficiency and effectiveness. XGBoost is from diverse models, ensemble learning helps to reduce the
widely used in many machine-learning fields such as weaknesses of individual models while maximizing their
classification, regression, and ranking. Each tree is built strengths, resulting in better overall performance [20].
using a random subset of features, and predictions from • Bagging: Involves training multiple instances of the
individual trees are combined through voting or averag- same base model on different subsets of the training
ing to make the final prediction. data and averaging their predictions.
• Random Forest (RF): is an ensemble learning method • Boosting: Builds a strong learner by sequentially train-
that combines multiple decision trees to improve the ing multiple weak learners, where each subsequent
predictive accuracy and robustness of a model. Random learner focuses more on the misclassified instances
forests are valuable for their robustness against overfit- from the previous learners.
ting and their suitability for classification and regression • Stacking: Involves training multiple base models and then
problems. The hyperplane that best separates the classes. using a meta-model to combine their predictions, treating
• SVM (Support Vector Machine): SVM, which allows the predictions of base models as additional features.
the separation of classes, is useful in large areas and in • Voting: Combines the predictions of multiple models by
cases where the number of features is larger than the aggregating their individual predictions using a simple
sample. It finds application in classification and rework- voting mechanism (e.g., majority vote for classification
ing, especially in cases where classes are separated. Hide or averaging for regression).
and reveal layers. • Blending: Blending is like stacking, but it uses a holdout
• Multi-Layer Perceptron (MLP): MLP is trained using a set (a part of the training set) to generate predictions for
regression model that adjusts the weights of neurons to the training set of the meta-model. This can be more
reduce the error between predictions and actual results. robust than voting or a single layer of models since it
MLP is known for its ability to learn nonlinear relation- incorporates multiple stages of learning and validation.
ships and is often used in tasks such as classification,
regression, and pattern recognition.
PROPOSED WORK
• K-Nearest Neighbors (KNN): It predicts the class of
data points by identifying the class of most of their The section discusses the proposed work in terms of
nearest neighbors (for classification) or by the average data preparation phase and regression phase. The “Daily
value of its neighbor (for regression). The performance Household Transaction” dataset is pre-processed to apply
of KNN depends on the distance measure choice and k machine learning models for training and predicting
value. Each classification is determined by the value of expenses. The data preprocessing is divided into multiple
the selected item, creating a tree-like structure. steps; the first step is normalization using MinMax scal-
• Decision Tree (DT): Decision trees are easy to interpret ing technique which scales each feature to a given range,
and visualize and are useful for understanding the deci- between 0 and 1 [21]. This scaling is useful when you want
sion-making process. However, they are easy to overfit, all features to be on a similar scale, which can improve the

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025 1269
Error, Mean Square Error and Relative absolute error. These
are the common parameters used in regression analysis.
They provide different perspectives on how well a model
is performing.
R-squared (R2) value
Also known as the coefficient of determination,
R-squared measures the proportion of the variance in the
dependent variable (target) that is predictable from the
independent variables (features). Higher R-squared scores
(closer to 1) indicate better model fit.
(1)
where, SS and SS the sum of the squared differences
res tot
between the observed values and the predicted values, and
Figure 1. Data Transformation, distribution of log
the sum of the squared differences between the observed
(1+amount).
values and the mean of the observed values respectively.
Mean absolute error (MAE)
performance of many machine learning algorithms. In This metric quantifies the average magnitude of errors
second step is transformation of amount attribute using between predicted and actual values. Lower MAE values
‘log1p’ function. The log1p function computes the natural indicate better model performance.
logarithm of ‘1 + x’, which is useful for transforming data
(amount in our case) that may contain zero or small posi-
(2)
tive values as shown in Figure 1.
Lastly, the third step in data preprocessing is vectorizer
where, n is the number of observations, y is the actual
process using ‘TfidfVectorizer (min_df=3)’, it transforms i
value, and ŷ is the predicted value.
text data into numerical values based on the term frequen- i
cy-inverse document frequency (TF-IDF) statistic, param-
Mean square error (MSE)
eter ‘min_df =3’ specifies that only terms (words or tokens;
MSE measures the average of the squares of the errors
in our case ‘Mode’, ‘Category’,’ Subcategory’, ‘Note’, ‘Income/
that is, the average squared difference between the actual
Expense’) that appear in at least three documents will be
values and the predicted values.
considered, reducing noise and dimensionality. By convert-
ing the text data into TF-IDF vectors, it transforms the text
(3)
into a numerical format that can be fed into algorithms.
After successful preprocessing, the dataset is divided
into the ratio of 70:30, where 70% is used for training and where, n is the number of observations, y is the actual
i
30% is used for testing purposes. The next phase is regres- value, and ŷ is the predicted value.
i
sion phase, the training data and testing data is fed to mul-
tiple machine learning models and predictions are made, Relative absolute error (RAE)
evaluated using two regression metrics; r-squared value and RAE measures the total absolute error as a proportion
mean absolute error. of the total absolute error of a simple predictor, such as the
mean of the actual values. It provides a normalized measure
of prediction accuracy.
RESULTS AND DISCUSSION
The section discusses the evaluation parameters used
(4)
in the experiment, along with a description, results of the
machine learning model. The section also showcases the
web application description and screenshots of the web where, n is the number of observations, y i is the actual value,
application for better understanding. ŷ i is the predicted value, and is the mean of actual value.
The R-square value provides an indication of how well
Evaluation Parameters the model’s predictions match the actual data. MAE mea-
The results of the Expense Tracker Management System sures the average magnitude of errors in a set of predic-
are evaluated in terms of R-squared value, Mean Absolute tions. Relative absolute error is particularly useful when

1270 Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
comparing different models. Mean square error is a pre- Web Application Development
ferred metric for optimizing and assessing model fitness,  The  application  development  for  expense  tracking
also offers an absolute measure of predictive accuracy.  involves ensuring seamless user experience by incorpo-
The performance of the different machine learning and  rating features such as income and expense limits, savings
ensemble models is evaluated over these metrics and is  tracking, and intuitive interfaces. The effectiveness of the
shown in Table 2. reminder system is crucial for user engagement and adher-
The results in Table 2 showcase the performance of  ence to budgeting goals. A user-friendly design reduces the
individual machine learning models and ensemble learn- learning curve, making the app accessible to diverse demo-
ing techniques. The parameter tuning process for the  graphics. The framework behind the application develop-
selected machine learning models involves identifying  ment is described below.
key hyperparameters such as learning rate for XGBoost
or number of neighbors for KNN, by using Hit and Trial  Backend Development
method.  The  models  are  evaluated  based  on  perfor- •  Django (Python): Django is chosen for its robust frame-
mance metrics such as R-squared and Mean Absolute  work and extensive built-in features, which streamline
Error  through  cross-validation  to  prevent  overfitting.  the development process.
The best-performing hyperparameters are selected and  ü  Django’s Built-in Authentication: Implement role-
validated on a test set to ensure that improvements are  based access control (RBAC) using Django’s authen-
generalizable to new data. The performance of XGBoost  tication system.
technique outperforms other individual machine learn- ü  Django Paginator Class: Implement server-side pag-
ing models with a highest r-square value of 77.89, while  ination for efficient data management.
Voting Ensemble Regressor outperforms individual mod- ü  Django  Admin  Customization:  Customize  the
els and other ensemble approaches with highest r-square  Django Admin interface for better usability.
value of 78.11 and lowest relative absolute error of 0.1765.  •  Database:  PostgreSQL  is  selected  for  its  reliability,
As r-square value is a useful metric for evaluating the  robustness,  and  support  for  complex  queries  and
explanatory power of a model, it does not always provide a  transactions.
complete picture of model performance. Since there is no
more difference in the r-square value of models because  Frontend Development
of characteristics of the dataset, as the distribution of the  •  HTML, CSS, JavaScript
variables and the nature of their relationships, explaining  •  Ajax: Use jQuery for making asynchronous requests to
the same amount of variance. RAE stands out be the decid- the server.
ing factor in our approach as the RAE of voting ensemble  ü  JavaScript and Django: Develop Ajax-based search
regressor is lowest. functionality for querying the database in real-time.
Table 2. Performance of machine learning models
Model R-squared(R2) value Mean absolute error Mean square error Relative absolute error
Individual models
| XGBoost       | 77.89 | 0.6324 | 0.9399 | 0.1919 |
| ------------- | ----- | ------ | ------ | ------ |
| Random forest | 77.02 | 0.6150 | 0.9773 | 0.1919 |
| SVM           | 72.41 | 0.6943 | 1.1734 | 0.1919 |
| MLP           | 74.81 | 0.6439 | 1.0716 | 0.1919 |
| KNN           | 69.58 | 0.6956 | 1.2937 | 0.1919 |
| Decision tree | 70.89 | 0.6701 | 1.2378 | 0.1919 |
| Extra tree    | 75.68 | 0.6107 | 1.0344 | 0.1919 |
| CatBoost      | 76.02 | 0.7020 | 1.0199 | 0.1919 |
Ensemble Models
| Bagging  | 76.34 | 0.6217 | -      | 0.1835 |
| -------- | ----- | ------ | ------ | ------ |
| Boosting | 75.89 | 0.6208 | -      | 0.1852 |
| Stacking | 73.56 | 0.6613 | 1.0604 | 0.1939 |
| Voting   | 78.11 | 0.6121 | 0.9648 | 0.1765 |
| Blending | 74.37 | 0.6731 | 1.0439 | 0.1909 |

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025 1271
ü Chart.js: Use JavaScript charting libraries to display
data visually on the frontend.
• Client-side Validation: Implement client-side validation
using JavaScript and the jQuery Validation library.
• Server-side Validation: Utilize Django form validation.
Key Components
1. User Authentication and Security: Utilize Django’s
built-in authentication for user registration, login, and
role-based access control (RBAC).
2. Expense Tracking: Allow users to manually enter Figure 2. Login page.
expenses via forms.
3. Expense Categorization: Predefined Categories which
provide categories such as food, transportation, enter- The expense tracker management system provides a
tainment, and utilities. Also, custom categories which detailed expense summary that offers users a comprehen-
allow users to create custom categories. sive view of their financial activity. The summary includes
4. Analytics and Reporting the total expenses for a selected period, along with a break-
ü Visual Reports: Generate visual reports using down by categories such as food, transportation, and enter-
JavaScript charting libraries like Chart.js. tainment, visualized through pie or bar charts as shown
ü Predictive Analytics: Implement machine learning in Figure 3. Monthly spending trends are depicted using
models for expense prediction. line charts, highlighting patterns and significant variances.
ü Budget Forecasting: Offer monthly budget forecasts Detailed transaction lists are available for review, showing
and highlight potential overspending areas. individual expenses with dates, amounts, and descriptions.
Users can also see their top expenses, compare their actual
Application Description
spending against budget limits with progress bars, and view
The section provides the screenshots of the appli- predictive analytics for future expenses. Additionally, a sav-
cation and its working in the form of description. User ings overview indicates the total savings achieved, helping
authentication in Django involves configuring the users monitor their financial goals effectively. To enhance
built-in authentication system, creating login views and financial management, the system allows users to create and
templates, and managing user sessions using functions manage custom expense categories, provides expense fore-
like `login()` and `logout()`. User authorization utilizes casting through advanced algorithms, and tracks income
Django’s permissions system, where permissions can be sources alongside expenses for a complete financial picture.
defined at the model level and enforced using decorators The income summary in the expense tracker manage-
like `@login_required` to restrict access to views based ment system offers users a clear and detailed overview of
on authentication status. Customization can be done by their earnings over a specified period as shown in Figure
creating custom authentication backends or user models 4. It includes the total income received, broken down by
to suit specific requirements, the login page is shown in sources such as salary, freelance work, and other income
Figure 2. streams. This breakdown is visualized through charts like
Figure 3. Expense summary.

1272 Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
Figure 4. Income summary.
pie charts or bar graphs for easy analysis. Monthly income validates the data and saves it to the database. Additionally,
trends are displayed using line charts, helping users iden- expense entry functionalities may include the ability to
tify patterns and variations in their earnings. A detailed view, update, and delete existing expenses and features
list of income transactions is provided, showing dates, like filtering and sorting to analyze spending patterns.
amounts, and sources, enabling users to verify and track Additionally, expense entry functionalities include the abil-
their earnings accurately. The summary also compares ity to view, update, and delete existing expenses, and fea-
actual income against projected income targets, highlight- tures like filtering and sorting to analyze spending patterns.
ing any discrepancies. Overall, the Income Summary helps Users can categorize expenses for more detailed tracking
users understand their financial inflows, track perfor- and apply tags for specific projects or events. The system
mance against income goals, and plan for future financial also provides tools to generate expense reports and visual-
stability. Additionally, users can set and monitor income ize spending trends over time.
goals, and the system offers projections based on histori- The income entry feature in the expense tracker man-
cal data and trends. The Income Summary integrates with agement system enables users to easily record and manage
other financial reports to provide a comprehensive view their earnings. Users can input details such as the date,
of overall financial health. Overall, the Income Summary source, amount, and mode of payment for each income
helps users understand their financial inflows, track perfor- entry, ensuring accurate and comprehensive financial
mance against income goals, and plan for future financial records as shown in Figure 6. They can also add descrip-
stability, ultimately aiding in better budgeting and financial tions and categorize their income to facilitate better track-
decision-making. ing and analysis. Additionally, the system allows users to
Expense entry in the expense tracker management mark certain income entries as recurring, automating
system involves creating a model to represent individual future entries and saving time. Once entered, the income
expenses, including fields such as the amount, description, details are saved and displayed in the income summary and
date, and category as depicted in Figure 5. Users can input transaction list, where users can view, edit, or delete entries
their expenses through a form or API endpoint, which as needed. This streamlined process helps users maintain
Figure 5. Expense entry.

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025 1273
Figure 6. Income entry.
an accurate overview of their financial inflows, aiding in filters to narrow down. The system may provide user inter-
budgeting and financial planning. faces such as a search bar, drop-down menu, or date picker
Expense categorization in the expense tracker manage- to facilitate filter selection. Additionally, advanced filter
ment system allows users to classify their expenses into pre- options such as sorting by relevance or custom filter presets
defined categories for better organization and analysis. This
can improve user experience and productivity.
involves creating a model for expense categories, which
typically includes fields like name, description, and possi- Application Benefits
bly a color or icon for visual distinction such as in Figure 7, Our application outperforms other applications from
it indicates shopping, food, rent and other. Users can assign the state-of-the-art discussed in the literature. Here are
categories to their expenses either manually or through
some points which outstand our application.
automated rules. The system may provide features for man-
• Advanced Analytics and Prediction: Existing systems
aging categories, such as adding, editing, or deleting them,
often provide basic data analysis and are limited to sim-
as well as reporting functionalities to track spending across
ple expense tracking. Our system leverages machine
different categories over time.
learning for advanced analytics and precise expense
Figure 8 depicts the search and filter capabilities in the
predictions, offering users a deeper understanding of
debt tracking system allow customers to effectively and effi-
their financial patterns.
ciently identify their debts based on specific criteria. This
includes using features that allow users to search for debt • Customizable Reporting: Earlier solutions often offer
using keywords or phrases, filter debt by attributes such as limited customization for financial reports and cat-
date, category, price or description, and combine multiple egories. Our system provides extensive options for
Figure 7. Expense categorization.

1274 Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025
Figure 8. Search and filtering.
customizing categories, reports, and catering to diverse share future expenses transactions can include scanning
user needs and preferences. of receipts and instant integration with bank accounts
• User-Friendly Design: Older systems might have com- Features such as syncing and spend-based personal finan-
plex interfaces. Our application features a simple, intui- cial advice are used as important tools to promote financial
tive design, making it easy for users to navigate and use
literacy, budgeting, and overall health for individuals and
effectively.
organizations.
• Interactive Dashboards: Existing solutions might offer
To conclude, various machine learning techniques and
static reports. Our system features interactive dash-
ensemble methods like bagging, boosting, stacking, voting,
boards that allow users to explore their financial data
and blending are employed for prediction. Among these,
through dynamic charts and graphs.
XGBoost achieves R-squared value of 77.89%, the highest
Our proposed ML based Expense Tracker Management
compared to other individual models, while the voting
System helps individuals and organizations manage
ensemble regressor surpasses other ensemble methods with
finances by using machine learning to predict and analyze
expenses. Its features offer valuable insights into spending the highest R-squared value of 78.11% and the lowest rela-
patterns, benefiting personal finance enthusiasts, small tive absolute error of 0.6121. The proposed approach helps
businesses, and financial advisors by improving budget- to forecast future expenses by analyzing users’ past spend-
ing and financial planning. The findings from the Expense ing patterns and behaviors. By leveraging historical data,
Tracker Management System demonstrate its effective- these methods provide valuable insights into future finan-
ness in predicting and analyzing expenses using machine cial needs and trends of any individual or business.
learning. These insights are valuable for a broad audience, The future evolution of the Expense Tracker
including individuals managing personal finances and Management System holds promise for even greater inno-
small businesses optimizing budgets.
vation and impact. Potential enhancements may include
integration with emerging technologies such as advanced
CONCLUSION artificial intelligence and machine learning, enabling pre-
dictive analytics for personalized financial insights and
Expense Tracker Management System provides indi-
automated expense categorization. We aim to enhance
viduals and businesses with effective solutions to track,
application functionality and user experience by incorpo-
analyze, and manage their spending through intuitive and
rating automated transaction tracking, cloud-based data
powerful features such as categorization, fundraising, and
synchronization, multi-language support, and AI-driven
advertising recommendations to present to users. Financial
gaining control over their situation improving health clean recommendations. We also aim in developing a dataset for
budgeting and decisions access across multiple devices expense tracker system to ensure that the dataset captures
and improving accountability and transparency, especially distinct and meaningful patterns, leading to better perfor-
in an environment where many people can integrate and mance and more reliable predictions.

Sigma J Eng Nat Sci, Vol. 43, No. 4, pp. 1265−1275, August, 2025 1275
AUTHORSHIP CONTRIBUTIONS
|     |     |     |  [8]  | Patil     | P,  Ahmed  | MM,  Kamble  |      | R,  Gaikwad   | N.   |
| --- | --- | --- | ----- | --------- | ---------- | ------------ | ---- | ------------- | ---- |
|     |     |     |       | Personal  | Expenses   | Tracker.     | Int  | J  Res  Publ  | Rev  |
Authors equally contributed to this work.
2023;4:4357–4359.
|     |     |     |  [9]  | Chandini  | S,  | Poojitha  T,  | Ranjith  | D,  Mohammed  |     |
| --- | --- | --- | ----- | --------- | --- | ------------- | -------- | ------------- | --- |
DATA AVAILABILITY STATEMENT
|     |     |     |     | Akram  | VJ,  Vani  | MS,  Rajyalakshmi  |     | V.  | Online  |
| --- | --- | --- | --- | ------ | ---------- | ------------------ | --- | --- | ------- |
The authors confirm that the data that supports the  Income and Expense Tracker. Int Res J Eng Technol
findings of this study are available within the article. Raw  2019;6:11110.
data that support the finding of this study are available from  [10]  Saravade PS, Molak PR, Jadhav BS, Khare KP, Lokare
the corresponding author, upon reasonable request. SM. Income and expense daıly tracker system. Int J
Innovations Eng Res Technol 2023;11:86–89.
CONFLICT OF INTEREST [11]  Gupta H, Singh AP, Kumar N, Blessy JA. Expense
|     |     |     |     | Tracker:  | A  Smart  | Approach  | to  | Track  Everyday  |     |
| --- | --- | --- | --- | --------- | --------- | --------- | --- | ---------------- | --- |
The author declared no potential conflicts of interest
Expense. EasyChair Preprint 2020;4809.
with respect to the research, authorship, and/or publication
|     |     |     | [12]  | Johri E, Desai P, Soni P, Jain H, Sanganeria N.  |     |     |     |     |     |
| --- | --- | --- | ----- | ------------------------------------------------ | --- | --- | --- | --- | --- |
of this article.
Expense Management System. In: 2023 4th IEEE
Global Conference for Advancement in Technology
ETHICS
(GCAT); 2023. p. 1–6. [CrossRef]
There are no ethical issues with the publication of this  [13]  Thakare  R,  Thakare  N,  Sangtani  R,  Bondre  S,
manuscript. Manekar A. Expense tracker application using naive
bayes. Int J Recent Eng Sci 2023;10:50–56. [CrossRef]
STATEMENT ON THE USE OF ARTIFICIAL  [14]  Laishram  C.  Design  and  Development  of  an
INTELLIGENCE Expenses Tracker App using the Flutter Framework.
Amity J Comput Sci 2023;7:2.
Artificial intelligence was not used in the preparation
|     |     |     | [15]  | Thanapal P, Patel MY, Raj TL, Kumar JS. Income and  |     |     |     |     |     |
| --- | --- | --- | ----- | --------------------------------------------------- | --- | --- | --- | --- | --- |
of the article.
expense tracker. Indian J Sci Technol 2015;8(Suppl
2):118–122. [CrossRef]
REFERENCES [16]  Daily Transactions Dataset. Kaggle 2024. Available
|     |     |     |     | at:  https://www.kaggle.com/datasets/prasad22/dai- |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
 [1]  Jadhav NJ, Chakor RV, Gun-jal TM, Pawar DD.
ly-transactions-dataset Accessed July 21, 2025.
| Expense  tracker.  | Int  Res  J  Modernization  | Eng  |       |                                                    |     |     |     |     |     |
| ------------------ | --------------------------- | ---- | ----- | -------------------------------------------------- | --- | --- | --- | --- | --- |
|                    |                             |      | [17]  | Doan T, Kalita J. Selecting machine learning algo- |     |     |     |     |     |
Technol Sci 2022;4:2582–5208.
|     |     |     |     | rithms  | using  | regression  models.  |     | In:  2015  | IEEE  |
| --- | --- | --- | --- | ------- | ------ | -------------------- | --- | ---------- | ----- |
 [2]  Masendu TR, Tripath AM. Daily Expense Tracker.
International Conference on Data Mining Workshop
Int J Res Eng Sci Manag 2022;5:90–92.
(ICDMW); 2015. p. 1498–1505. [CrossRef]
 [3]  Thomas P, Lekshmi, Mahalekshmi. Expense tracker.
|     |     |     | [18]  | Aldave R, Dussault JP. Systematic ensemble learning  |     |     |     |     |     |
| --- | --- | --- | ----- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
Int J Adv Res Sci Commun Technol 2020;9:4.
 [4]  Cabañero RA. Design and Development of Expense  for regression. arXiv preprint 2014;1403.7267.
|     |     |     | [19]  | Mienye ID, Sun Y. A survey of ensemble learning:  |     |     |     |     |     |
| --- | --- | --- | ----- | ------------------------------------------------- | --- | --- | --- | --- | --- |
Management System using CodeIgniter Framework.
Int J Adv Res Sci Commun Technol 2023;29:929– Concepts, algorithms, applications, and prospects.
IEEE Access 2022;10:99129–99149. [CrossRef]
935. [CrossRef]
 [5]  Garg A, Goel M, Mittal S, Singh S. Expense Tracker.  [20]  Odegua R. An empirical study of ensemble tech-
niques (bagging, boosting, and stacking). In: Proc
Int J Res Appl Sci Eng Technol 2023;9:1067–1070.
| [CrossRef] |     |     |     | Conf: Deep Learn IndabaXAt; 2019. |     |     |     |     |     |
| ---------- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
 [6]  Sakthivel M, Roshini P, Roja K, Maha Lakshmi P,  [21]  Jadhav A, Dhaulakhandi D, Shandilya SK, Malviya
Keerthi V. Personal Expense Tracker Application.  L, Mewada A. Data transformation: A preprocess-
Int J Res Appl Sci Eng Technol 2023;8:2031–2038. ing stage in machine learning regression problems.
 [7]  Noorsumar  MH,  Supalkar  SS,  Singh  H,  Udeshi  In:  Artificial  Intelligence  Techniques  in  Power
TU.  Expense  Tracker.  Int  Res  J  Eng  Technol  Systems Operations and Analysis; 2023. p. 183–194.
| 2023;11:195-201. |     |     |     | Auerbach Publications. [CrossRef] |     |     |     |     |     |
| ---------------- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |