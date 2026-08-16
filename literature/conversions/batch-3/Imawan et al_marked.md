---
conversion_metadata:
  converted_at: "2026-07-21T13:35:31Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Imawan et al.pdf"
  source_pdf_sha256: "b9575f1a3e520e6c963a5b14eb11d1b92ee5309133ad41c89fd7889cb746851c"
  page_count: 26
  markdown_char_count: 150001
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Hypermedia & Technology-Enhanced Learning 
Vol. 3, No. 1, February (2025), Pages 64–89 
e-ISSN: 2985–9166 |       10.58536/j-hytel.166

RESEARCH ARTICLE

| 64 |

Enhancing Financial Literacy in Young Adults: An Android-Based Personal

Finance Management Tool

Riswandha Imawan1* 
Milakis3

, Mykhailo Dumchykov4

, Wahyu Permana Putra1

, Rabee Alqahtani2

, Emmanouil D.

1 Faculty of Engineering, Universitas Negeri Padang, Padang, Indonesia  
2 School of Education, University of Wollongong, NSW 2500, Australia  
3 Department of Education Sciences, European University Cyprus, Engomi, Cyprus  
4 Sumy State University, Sumy, Ukraine

*Corresponding Author: r1smawan024@gmail.com

This article 
contributes to:

ABSTRACT

This study details the design, development, and evaluation of an Android-based personal finance 
management  application  tailored  for  young  adults  in  higher  education.  Addressing  unique 
financial  challenges  such  as  limited  experience  and  fluctuating  income,  the  application 
incorporates features like income tracking, expense monitoring, budgeting, and financial goal 
setting. Developed using the Waterfall model, the application includes secure login systems, 
intuitive  transaction  management,  customizable  goals,  budget  projections,  and  automated 
notifications to encourage financial discipline. Usability evaluations using a 5-point Likert scale 
with 50 users revealed an overall satisfaction score of 4.6/5, rated 'Excellent.' Users praised the 
intuitive design, accurate tracking, and motivational reminders, while also suggesting additional 
customization  and  deeper  financial  analysis  for  future  updates.  This  study  demonstrates  the 
potential of targeted digital tools to foster financial literacy and resilience, offering evidence that 
personalized technology can significantly improve financial behaviors in young adults. Future 
research  will  explore  enhanced  customization  and  AI-driven  features  to  further  refine  the 
application’s impact.

KEYWORDS

Personal financial management; mobile app; financial habits; young adults; higher education

Received: Nov. 07, 2024; Revised: Dec. 10, 2024; Accepted: Dec. 25, 2024; Published Online: Jan. 27, 2025

How to cite: Imawan, R., Putra, W. P., Alqahtani, R., Milakis, E. D., & Dumchykov, M. (2025). Enhancing 
Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool. Journal of Hypermedia 
& Technology-Enhanced Learning, 3(1), 64-89. https://doi.org/10.58536/j-hytel.166

Published by Sagamedia Teknologi Nusantara 
© The Author(s) 2025| This is an open-access article under the CC BY 4.0 license.

1. INTRODUCTION

The rapid advancement of digital technology has transformed modern life, bringing both opportunities 
and  challenges  across  various  sectors,  particularly  in  personal  finance  [1],  [2],  [3].  Personal  finance

Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 2 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

management  has  become  critical,  especially  for  young  adults  facing  unique  financial  challenges  in 
today’s  economy.  Financial  literacy  and  responsible  financial  behavior  are  increasingly  important, 
especially after the pandemic’s economic impact [4], [5]. As of December 2021, Indonesians aged 19-
34 accounted for 63% of online loan users, according to the Financial Services Authority of Indonesia 
(OJK), with a significant concentration in urban areas. This demographic, composed mainly of students 
and early-career individuals, is vulnerable to financial mismanagement due to limited experience and 
guidance  in  financial  decision-making  [6],  [7].  A  survey  among  Informatics  Education  students  at 
Universitas Negeri Padang highlighted this issue, showing that fewer than 50% consistently recorded 
their  finances,  just  20%  regularly  reviewed  income  and  expenses,  and  merely  40%  adhered  to  a 
monthly budget.

Despite increasing awareness of the importance of financial literacy,  there remains a practical gap  in 
using tools tailored to engage and empower young adults in managing their finances effectively. Many 
existing financial management tools are designed for a general audience, often overlooking the unique 
needs and behaviors of younger users, who are more inclined toward interactive, mobile-first solutions 
[8], [9]. Although prior studies have established the importance of financial literacy, few have explored 
how  a  targeted  mobile  application  can  directly  influence  and  improve  financial  habits  among  young 
Indonesian adults [10], [11].

Addressing this gap is crucial since financial behaviors established in early adulthood have significant 
long-term implications. The prevalence of high online loan usage among young Indonesians highlights 
an  urgent  need  for  tools  that  encourage  responsible  financial  habits  [12],  [13].  Without  timely 
intervention, financial literacy deficits may perpetuate a cycle of debt and instability. By providing a 
mobile solution that promotes consistent financial tracking and budgeting, this study  intends to instill 
positive financial behaviors early on, establishing a foundation for financial resilience.

This study aims to develop an Android-based personal finance management application tailored to the 
needs  of  young  adults,  equipped  with  features  for  tracking  income,  setting  budgets,  monitoring 
expenses, and establishing financial goals. It further evaluates the application’s usability and its impact 
on  users’  financial  behaviors,  focusing  on  fostering  consistent  engagement  and  improving  financial 
literacy. The research questions guiding this study are as follows:

1)  How  effective  is  an  Android-based  personal  financial  management  application  in  improving  the

financial habits of young adults in higher education?

2)  To  what  extent  can  regular  engagement  with  the  application  enhance  financial  literacy  and

contribute to long-term financial resilience among users?

3)  Which  features  most  effectively  promote  consistent  financial  management  behaviors,  such  as

budgeting, expense tracking, and goal setting?

Proactive and practical steps are necessary to prevent younger generations from falling into financial 
difficulties.  A  foundational  strategy  for  improving  financial  literacy  is  consistently  recording  and 
managing personal finances [14]. This practice helps individuals align their spending habits with their 
needs,  plans,  and  goals.  Effective  personal  financial  management  hinges  on  strategically  allocating 
income  across  expenses,  savings,  and  investments  [15].  Individuals  bear  responsibility  for  managing 
their finances as a critical aspect of daily life, which can yield positive outcomes, particularly in curbing 
excessive consumerism [16].

Moreover, financial management is a vital 21st-century skill, resting on four pillars: income, expenses, 
savings, and planning. Healthy finances result from sustainable and deliberate money management [17]. 
To address this challenge, fostering financial habits requires tools that are both accessible and easy to

| 65 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 3 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

maintain. Research underscores that mobile phones—used frequently in daily life—are ideal platforms 
for  cultivating  such  habits  [18],  [19],  [20].  By  leveraging  this  technology,  the  proposed  application 
serves as a platform to reinforce consistent financial tracking and reflection.

This  research  addresses  a  critical  gap  by  targeting  younger  demographics  with  a  customized  digital 
solution for personal finance management. The study contributes to advancing financial literacy as a 
fundamental 21st-century competency through practical implementation and evaluation. By integrating 
goal-setting  frameworks,  automated  reminders,  and  an  intuitive  interface,  the  application  offers  a 
holistic  approach  to  nurturing  healthier  financial  habits  and  mitigating  financial  instability  among 
Indonesia’s young adults.

2. METHODS

systematic  progression

This  research  employed  the  Waterfall  model,  a  structured  software  development  methodology,  to 
sequential  phases:  requirements  analysis,  design, 
ensure 
implementation, testing, and deployment [21], [22], [23]. This approach enabled organized execution 
and thorough validation at each stage, minimizing iterative backtracking and ensuring alignment with 
user needs [24], [25]. The methodology’s stages are illustrated in Figure 1.

through

Figure 1. Phases of the waterfall model

The  Waterfall  model  was  chosen  for  its  linear,  phase-gated  structure,  which  ensured  systematic 
validation of user requirements before advancing to design and coding. This minimized scope creep and 
aligned with the study’s focus on replicable, structured development for academic evaluation.

2.1. Requirements Analysis

The initial phase focused on mapping user behaviors and needs through interviews and surveys targeting 
young adults in higher education. The goal was to identify core financial management processes and 
translate them into application features that promote engagement and financial literacy. Key processes 
observed in user workflows are summarized in Table 1.

| 66 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 4 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Table 1. Key financial management processes identified through requirements analysis

No.

Process

Activity

1

2

3

Income Tracking

Expense Tracking

Budget Projection

Users  record  income  received  in  financial  journals,  mobile 
notes, or calculators. 
Users record expenses incurred, often using financial journals, 
mobile notes, or calculators. 
Users  use  financial  journals,  mobile  notes,  or  calculators  to 
record and plan anticipated expenses.

Actor

Individual

Individual

Individual

This  analysis  led  to  identifying  additional  requirements  to  enhance  the  application's  usability  and 
functionality.  These  enhancements  addressed  everyday  financial  management  needs,  making  the 
application more intuitive and adaptable to user preferences. The additional requirements are outlined 
Table 2, which details each feature’s purpose and contribution to an improved user experience.

Table 2. Additional requirements for enhanced usability and functionality

No.

1

Feature(s)

Process(es)

Income/Expense 
Data Tracking

Users record the amount of income/expense received. This recording is 
typically conducted in financial journals, on mobile notes, or using calculators.

Users can categorize the entered data, classifying income/expense by type, 
method of acquisition, and other relevant factors.

Users may also attach notes to each entry detailing aspects such as the source of 
income/expense, method of acquisition, and other pertinent information.

2

Financial Goal Data 
Tracking

Users can input data related to their financial goals, adjusting target amounts and 
timeframes according to their capacity.

Users receive progress updates on their financial goals based on their transaction 
history.

Users are provided with information and recommendations on optimal saving 
amounts to reach their financial goals effectively.

3

Budget Projection 
Tracking

Users can input data for monthly budget projections based on their monthly 
income and expenses.

Users receive budget information aligned with their historical financial reports.

4

Financial Reports

Users can access a summary of expenses and income based on the data they 
enter.

2.2. Design

2.2.1. Flowchart

A  flowchart  is  a  structured  diagram  that  uses  standardized  symbols  to  visually  represent  systematic 
procedures  for  completing  a  process  [26].  It  depicts  workflows  through  symbols  such  as  rectangles 
(process steps), diamonds (decision points), and arrows (directionality) [27]. Figure 2 illustrates the 
system flow of the financial management application, outlining the user journey from initial login to 
feature interaction.

| 67 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 5 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Figure 2. Application flowchart

When users launch the application, they are presented with a login screen requiring email and password 
entry  to  access  their  financial  data.  Unregistered  users  must  complete  a  registration  process  before 
proceeding.  Upon  successful  authentication,  users  reach  the  homepage,  where  they  can  navigate 
features including expense tracking, income recording, financial goal-setting, budget projections, and 
financial  reports.  Each  feature  incorporates  guided  input  and  output  steps  to  streamline  user 
interaction.  After  completing  a  task,  users  may  either  explore  additional  features  or  exit  the 
application.

2.2.2. Activity Diagram

The  activity  diagram  models  the  dynamic  flow  of  system  activities,  emphasizing  the  sequence  and 
interaction of user actions [28]. Figure 3 depicts activity diagrams for the home and login functions, 
capturing initial user engagement and authentication workflows.

▪  Login  Activity  Diagram:  Details  the  authentication  process,  including  registration,

credential validation, and error handling for incorrect inputs.

▪  Home Activity Diagram: Represents the central interface users navigate to core features. 
Transitions between activities (e.g., moving from expense tracking to budget projections) are 
mapped to reflect user pathways.

| 68 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 6 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

(a)

(b)

Figure 3. Activity diagram: (a) Home; (b) Login

Figure 4 presents activity diagrams for income/expense tracking and financial goal management:

▪

Income/Expense  Tracking:  Outlines  the workflow  for  inputting  transactions,  including 
steps  for  categorization  (e.g.,  type,  payment  method),  adding  contextual  notes,  and  saving 
records. Decision points validate data completeness (e.g., mandatory amount fields).

▪  Financial Goal Management: Models setting, adjusting, and tracking goals. Users define 
targets (amount, deadline), receive progress updates, and can modify goals based on changing 
circumstances.

(b) 
Figure 4. Activity diagram: (a) Income/expense tracking; (b) Financial goal

(a)

| 69 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 7 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

(a)

(b)

Figure 5. Activity diagram: (a) Budget projecting; (b) Financial report

Additionally,  Figure  5  displays  the  activity  diagrams  for  the  budget  projecting  and  financial  report 
features. In the budget projecting activity diagram, users input and adjust their monthly projections as 
needed. The financial report activity diagram gives users an overview of their recorded financial data, 
enabling them to review and analyze their income, expenses, and budget alignment.

2.3. Implementation

The application was developed using Laravel (backend) and Flutter (frontend), ensuring secure data 
handling  and  cross-platform  compatibility.  Laravel’s  MVC  architecture  facilitated  RESTful  API 
development,  while  Flutter’s  widget-based  framework  enabled  a  responsive  UI  across  Android  and 
iOS. Key modules were implemented as follows:

2.3.1. Login Module

The module securely manages user access to the application by providing fields for users to enter their 
email  and  password,  with  data  encrypted  using  industry-standard  security  protocols  to  protect 
credentials.  If  users  forget  their  password,  they  can  reset  it  through  a  secure  process  that  sends  a 
verification code to their registered email. Additionally, the login process validates input formats, such 
as correct email format and minimum password length, to ensure data integrity and enhance security.

2.3.2. Income/Expense Tracking Module

input

This module allows users to record their income and expenses with tools for categorization and detailed 
‘Rent,’ 
tracking.  Users  can 
‘Entertainment’),  and  add  custom  notes  to  specify  details  such  as  income  sources  or  reasons  for 
expenses. The system enables users to edit or delete records, ensuring accuracy and flexibility in their 
financial tracking. Transactions are stored in a local SQLite database, providing quick access and offline 
functionality, with options for cloud storage synchronization.

transaction  amounts,  assign  categories  (e.g.,

‘Food,’

| 70 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 8 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

2.3.3. Financial Goal Module

The financial goal module supports users in setting and tracking financial goals, such as saving for a 
purchase  or  building  an  emergency  fund.  Users  can  define  specific  goals  with  target  amounts  and 
deadlines,  and  the  application  tracks  progress  toward  these  goals  based  on  recorded  income  and 
expenses.  This  module  includes  a  progress  bar  that  visually  represents  the  percentage  of  the  target 
achieved, and users receive updates as they get closer to their goals. The module also includes a feature 
that allows users to adjust goals, enabling them to modify target amounts or deadlines as their needs 
change. Additionally, it provides personalized saving recommendations based on analyzing the user’s 
financial data, suggesting realistic saving amounts to help users reach their goals on schedule.

2.3.4. Budget Projection Module

This  module  enables  users  to  set  and  monitor  monthly  budgets  across  various  categories,  such  as 
“Housing,”  “Utilities,”  “Entertainment,”  and  “Savings.”  Users  can  input  specific  budget  amounts  for 
each category and set durations to apply a budget across multiple months. The module compares user 
expenditures with the set budget, providing visual indicators (e.g., color-coded progress bars) to show 
users if they are within or exceeding their budget. If users exceed their budget, the system displays 
alerts  encouraging  budget  adjustments.  The  budget  data  integrates  with  historical  financial  reports, 
allowing users to compare current and past spending habits, which helps refine future budgets.

2.3.5. Notification Module

The notification module enhances user engagement by providing regular reminders to update financial 
data and review goals. This flexible module allowed users to set notification preferences such as daily 
or weekly reminders. Notifications encourage users to record their expenses, check their budgets, and 
update  their  progress  on  financial  goals.  The  reminders  use  Android’s  built-in  notification  service, 
ensuring they appear even when the application is closed, thus supporting consistent financial tracking 
and habit formation. The application sends custom alerts to users when they are close to reaching a 
financial goal or approaching a budget limit.

2.4. Testing

We  conducted  black-box  testing  to  evaluate  the  application’s  functionality  from  an  end-user 
perspective,  ensuring  it  met  performance  standards without  inspecting  the  internal  code  [29],  [30]. 
This approach allowed us to test each feature for usability, reliability, and accurate functionality based 
on expected outcomes. The testing procedure was structured to verify alignment with the application’s 
requirements,  focusing  on  key  modules,  including  login,  income/expense  tracking,  goal  setting, 
budget projection, financial reporting, and notifications.

Through  black-box  testing,  we  validated  the  application’s  robustness  using  scenarios  representing 
typical  user  interactions.  This  approach  accurately  assessed  the  application’s  performance  and  user 
experience, with detailed outcomes in the results section. As shown in Table 3, the testing covered 
each primary module, focusing on specific aspects of functionality essential to providing a seamless user 
experience.

| 71 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 9 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Table 3. Testing modules and evaluation focus

No.

Module

1

Login Page

2  Home Page

Focus of Evaluation

Secure access, user credential validation, and “forgot password” 
functionality.

Accessibility to all features, navigation between modules, and accuracy of 
financial summaries.

3

4

5

6

Income/Expense Tracking  Accuracy of data entry, categorization, and record deletion

functionalities.

Financial Goal

Goal setting, progress tracking, and goal adjustment capabilities.

Budget Projection

Financial Report

Accuracy in budget setting, monitoring, and alerts when exceeding 
budgets.

Accuracy of data display, summarization of income, expenses, and budget 
alignment.

7  Notification

Consistency of reminders, notification customization, and functionality 
when the application is inactive.

2.5. Deployment

In  the  deployment  phase,  the  application  was  evaluated  directly  with  a  selected  group  of  end  users 
representing  the  target  audience.  This  process  aimed  to  gather  preliminary  feedback  on  the 
application’s functionality, usability, and user satisfaction before its official release. An evaluation was 
conducted  in  a  beta  testing  format,  involving  users  who  matched  the  target  profile  (aged  19-34, 
students or individuals requiring personal financial management).

2.5.1. Direct User Evaluation Process

We randomly selected 50 university students within the target age range  who met personal finance 
management criteria. Each student received a detailed explanation of the research goals, participant 
rights, and data privacy policies. Participation was voluntary, with an option to withdraw at any time. 
After providing informed consent, students accessed the application and received brief training on key 
features,  including  income  tracking,  goal  setting,  and  budget  projection.  Over  a  two-week  testing 
period, participants used various Android devices commonly used by the target demographic, including 
Samsung, Xiaomi, and Oppo models running Android 10 or later. At the end of the period, participants 
completed  a  survey  about  their  experience.  All  data  collected  was  anonymized  and  used  solely  to 
improve the application.

2.5.2. Evaluation Instrument

The evaluation instrument consisted of a survey based on a 1-5 Likert scale to measure users’ responses 
to each evaluation aspect. This instrument covered the following evaluation aspects and indicators, as 
shown in Table 4.

| 72 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 10 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Table 4. Evaluation aspects and key indicators

No.

Aspect

Code

Key Indicators

1  Usability

2  User

Satisfaction

3

Functionality

I am satisfied with this application’s income/expense tracking function.

USA1  The application is easy to use, even for first-time users. 
USA2  Navigation between features in the application is easy to understand. 
USA3  The application’s interface design makes it easy for users to access features. 
USS1 
USS2  The budget projection feature aligns with my financial management needs. 
USS3  The reminder notifications help me stay consistent in tracking my finances. 
FUN1  This application accurately records and displays my financial data. 
FUN2  Each available feature functions as described and meets my expectations. 
FUN3

I  have  encountered  no  issues  or  errors  when  using  the  application’s  main 
features.

4

Engagement

ENG1  This application helps me stay more organized in daily financial management. 
ENG2 
ENG3  The  features  provided  motivate  me  to  track  and  manage  my  finances  more

I am likely to continue using this application routinely over the long term.

effectively.

5  Design

Satisfaction

DES1  The visual design of this application is attractive and comfortable to view. 
DES2  The layout of features in the application makes it easy to find the information I

need.

6

Feedback for 
Improvement

DES3  The color scheme and visual elements help clarify each feature’s function. 
FEI1  The application would benefit from additional customization options for budget

or financial categories. 
I want a more detailed financial trend analysis feature to help evaluate expenses. 
FEI2 
FEI3  Adding options for notification timing would be very helpful in aligning with

my schedule.

2.5.3. Data Analysis

We analyzed the data collected from the evaluation survey to identify the application’s strengths and 
areas for improvement based on end-user feedback. The analysis centered on calculating average scores 
for  each  evaluation  aspect,  which  were  then  categorized  to  provide  a  comprehensive  view  of  the 
application’s performance across key dimensions. This approach allowed us to highlight specific areas 
where  the  application  met  or  exceeded  expectations  and  pinpoint  aspects  that  could  benefit  from 
targeted enhancements.

We recorded each user’s response on a 1-5 Likert scale for every indicator, and average scores were 
calculated across all responses. This average score represented the application’s performance on each 
specific  indicator  within  an  evaluation  aspect.  For  each  evaluation  aspect,  the  average  scores  of  all 
indicators  were  then  summed  and  divided  by  the  number  of  indicators  to  obtain  an  aspect  score 
(Equation  1).  This  score  provided  an  overall  measure  of  the  application’s  performance  within  each 
aspect.

𝐴𝑠𝑝𝑒𝑐𝑡 𝑆𝑐𝑜𝑟𝑒 =

∑(𝐼𝑛𝑑𝑖𝑐𝑎𝑡𝑜𝑟𝑠 𝑆𝑐𝑜𝑟𝑒𝑠)
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐼𝑛𝑑𝑖𝑐𝑎𝑡𝑜𝑟𝑠

(1)

| 73 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 11 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

The overall application score was calculated by averaging the aspect scores from each evaluation aspect, 
as  shown  in  Equation  2,  to  represent  the  application’s  general  performance  across  all  aspects.  This 
overall application score provided a single value summarizing the application’s effectiveness and user 
satisfaction.

𝑂𝑣𝑒𝑟𝑎𝑙𝑙 𝐴𝑝𝑝𝑙𝑖𝑐𝑎𝑡𝑖𝑜𝑛 𝑆𝑐𝑜𝑟𝑒 =

∑(𝐴𝑠𝑝𝑒𝑐𝑡𝑠 𝑆𝑐𝑜𝑟𝑒𝑠)
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐴𝑠𝑝𝑒𝑐𝑡𝑠

(2)

Table 5 shows the scoring categories for aspect evaluations, providing qualitative interpretations based 
on score ranges. These categories included excellent (4.21  - 5.00), good (3.41  - 4.20), fair (2.61  - 
3.40), poor (1.81 - 2.60), and very poor (1.00 - 1.80), allowing each score to be easily interpreted 
based on user expectations.

Table 5. Aspect scores and categories

Score Range

Category

Interpretation

4.21 - 5.00

Excellent

The application fully meets user expectations in this aspect.

3.41 - 4.20

Good

The  application  performs  well  in  this  aspect  but  may  benefit  from  minor 
improvements.

2.61 - 3.40

Fair

The  application  meets  some  expectations  but  has  areas  that  require 
improvement.

1.81 - 2.60

Poor

The application does not meet most user expectations and requires significant 
improvement.

1.00 - 1.80

Very Poor

The  application  fails  to  meet  user  expectations  in  this  aspect.  Significant 
changes are needed.

The final analysis included reporting each aspect’s score and category along with the overall application 
score to provide a comprehensive view of the application’s performance. High scores (excellent, good) 
indicated  strengths  in  areas  that  met  or  exceeded  user  expectations,  while  moderate  scores  (fair) 
suggested  areas  needing  targeted  improvements.  Lower  scores  (poor,  very  poor)  highlighted  critical 
weaknesses  requiring  significant  adjustments.  This  structured  analysis  yielded  actionable  insights  for 
future  development,  helping  prioritize  improvements  based  on  user  needs  and  aligning  further 
development to enhance user satisfaction and functionality.

3. RESULTS

The results are presented following each stage of the development process, as outlined in the methods 
section. This approach explains how the application’s features were implemented, tested, and refined 
based on user feedback.

3.1. Application Development Results

The development phase focused on creating a usable, secure, functional personal financial management 
application. The final product incorporated the following key features:

| 74 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 12 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.1.1. Login Page

The login page, developed based on initial design requirements, provides a secure and user-friendly 
interface.  It  features  encrypted  password  storage  to  protect  user  credentials,  while  the  “forgot 
password” option offers a streamlined recovery process for users who may have misplaced their login 
details. As shown in Figure 6, the login page includes fields for email and password entry, guiding users 
through secure access to the application. Additionally, the application stores users’ financial data and 
records  securely in  the database, allowing  seamless  retrieval  upon login.  Once logged  in,  users  can 
access the full range of personal financial management features the application provides, establishing a 
straightforward and secure entry point.

Figure 6. Login page display

3.1.2. Home Page

After a successful login, users are directed to the home page, which functions as the main dashboard of 
the application. This interface organizes access to all core features, including expense tracking, income 
recording,  financial  goals,  budget  projection,  and  financial  reporting.  As  shown  in  Figure  7(a),  the 
home  page  layout  is  designed  to  ensure  that  users  can  quickly  navigate  between  different  modules 
without  confusion,  enhancing  the  application’s  usability.  The  structured  and  intuitive  design  allows 
users  to  seamlessly  interact  with  all  features,  promoting  a  cohesive  experience  that  makes  personal 
financial management straightforward and accessible.

3.1.3. Income/Expense Tracking

The income/expense tracking module was developed to enable users to record and categorize their 
financial transactions accurately. This feature enables users to input details for income and expenses, 
organize transactions by category, and edit or delete records as necessary, as illustrated in Figure 7(b). 
The application helps users maintain accuracy and stay on top of their financial data by supporting these 
actions. This module gives users clear insights into their spending patterns and income sources, which 
are fundamental for effective financial planning and control.

| 75 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 13 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

(a)

(b)

Figure 7. (a) Home page display; (b) Income/expense tracking display

3.1.4. Financial Goals

The financial goals module allows users to actively manage and track their financial objectives. As shown 
in Figure 8(a), users can create categories for specific goals, such as saving for emergencies, vacation 
planning, or future investments, allowing them to organize and prioritize their goals more effectively. 
The system updates users on their progress by tracking saved or invested amounts over time, fostering 
a sense of achievement as they work toward their targets. Furthermore, if users need to adjust their 
goals to align with changing financial circumstances, they can modify or remove goals as needed. This 
feature  motivates  users  to  focus  on  their  objectives  while  offering  flexibility  to  adapt  to  personal 
financial shifts.

3.1.5. Budget Projection

The budget projection feature enables users to set up monthly or custom plans based on their financial 
needs. When accessing this page, shown in Figure 8(b), users can input specific details such as budget 
name, category, duration, and amount. This feature helps users track and manage their budgets per 
their spending habits. Users can use the delete function to remove incorrect data if an error occurs, 
ensuring  that  their  projections  remain  accurate  and  tailored  to  their  preferences.  This  flexible  and 
customizable  approach  to  budgeting  helps  users  gain  better  control  over  their  financial  resources, 
promoting thoughtful and organized spending.

3.1.6. Financial Reports

The financial report module consolidates all user data, providing comprehensive income, expenses, and 
budget adherence summaries. As shown in  Figure 9(a), this feature displays the user-defined budget 
alongside a detailed history of financial entries. By offering insights into spending patterns and income 
trends, the report helps users make informed financial decisions. This feature highlights areas whe re 
adjustments may be needed and enables users to plan strategically for future goals, making it a valuable 
tool for sustained financial health and accountability.

| 76 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 14 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.1.7. Notification Reminder

The  notification  reminder  feature  is  essential  in  promoting  consistent  user  engagement  with  the 
application. As depicted in Figure 9(b), this feature sends periodic reminders, encouraging users to log 
financial activities regularly. By fostering a habit of consistent tracking, the notification system aims to 
help users develop a comprehensive understanding of their financial status over time. This awareness 
enables them to make more deliberate choices regarding expenses and savings, supporting responsible 
and strategic financial behavior in line with their objectives.

(a)

(b)

Figure 8. (a) Financial goal display; (b) Budget projection display

(a)

(b)

Figure 9. (a) Financial report; (b) Notification reminder display

| 77 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 15 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.2. Application Testing Results

Each  core  module  of  the  application  was  subjected  to  black-box  testing,  which  confirmed  the 
functionality, reliability, and user experience aspects. Below are the results for each module:

3.2.1. Login Page Test

The  login  page  was  tested  to  confirm  that  it  provides  secure  access,  validates  user  credentials,  and 
supports the “forgot password” function. As shown in  Table 6, the application successfully displayed 
the login interface, validated correct input, and directed users to the homepage upon successful login.

Table 6. Login page test result

No.

Scenario

Test Case

Test Output

1

Login as a user

Click on the login button.

2

3

Accessing 
application 
features

Click on the various buttons 
available on the homepage.

Logging into the 
application

Enter the username and 
password to log in.

4  User forgets 
password

Click on the “Forgot your 
password?” button.

The application displays the login 
page, where users can enter their 
username and password. A button is 
also available for users who have 
forgotten their password. 
Each button clicked takes the user to 
the corresponding feature or 
functionality as designed in the 
application. 
Users with registered accounts can 
successfully log in and access the 
application’s features. 
The user is redirected to the password 
recovery page, and the system sends a 
verification code to the user’s 
registered email address.

Result

Valid

Valid

Valid

Valid

3.2.2. Home Page Test

Testing  on  the  home  page  confirmed  access  to  all  features,  smooth  navigation  between  different 
modules, and accurate display of financial summaries. Users can view and select various features from 
the dashboard, as detailed in Table 7.

Table 7. Home page test result

No.

Scenario

Test Case

Test Output

1

2

3

Users access the 
system after 
logging in 
Viewing financial 
summary in detail

Accessing 
application features

After logging in, the user 
enters the system to view 
their financial summary. 
The user clicks on the 
displayed financial 
summary. 
The user clicks on various 
features available in the 
application.

The application displays a financial 
summary based on the features 
provided. 
The user can view a detailed and 
comprehensive financial summary 
within the application. 
The user selects and uses each feature 
according to its intended purpose and 
functionality.

Result

Valid

Valid

Valid

| 78 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 16 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.2.3. Income/Expense Tracking Test

The  Income/expense  tracking  module  was  tested  for  data  entry,  categorization,  and  deletion 
functionalities. As illustrated in  Table 8, users could successfully enter and manage income/expense 
transactions with accurate categorization and record management.

Table 8. Income/expense tracking test

No.

Scenario

Test Case

Test Output

1

2

Accessing the 
income/expense 
tracking page 
after login 
Entering 
income/expense 
transaction data

3  Deleting incorrect

income/expense 
transaction data 
Viewing income 
transaction data

4

After logging in, the user 
navigates to the 
income/expense tracking 
page. 
The user clicks on the 
income/expense data input 
option displayed on the page. 
The user deletes an 
incorrectly entered 
income/expense entry. 
The user views the previously 
entered income/expense 
data.

The application displays a summary of 
the user’s recorded income/expense.

The user can enter and record 
income/expense data into the 
application. 
The user can remove the incorrect 
income/expense data, ensuring 
accuracy in the recorded transactions. 
The user can review all 
income/expense data entered into the 
application.

Result

Valid

Valid

Valid

Valid

3.2.4. Financial Goal Test

The financial goal module testing confirmed that users could set, track, and update their financial goals. 
Users received progress updates and were able to adjust their goals as needed, which aligns with the 
intended design (refer to Table 9 for detailed results).

Table 9. Financial goal test result

No.

Scenario

Test Case

Test Output

1

2

3

Accessing the 
financial goal 
page after login

After logging in, the user 
navigates to the financial goal 
page.

Entering financial 
goal data

The user clicks on the financial 
goal input option displayed on 
the page.

Deleting 
incorrect financial 
goal data

The user deletes an incorrectly 
entered financial goal entry.

The application displays a summary 
of the user’s financial goals and 
progress toward each goal. Options 
are available for adding or removing 
goal progress. 
Users can enter data for a financial 
goal, including the target and 
progress tracking, allowing them to 
record and monitor their goals 
within the application. 
The user can successfully remove 
incorrect financial goal data, ensuring 
accurate tracking of their goals.

Result

Valid

Valid

Valid

3.2.5. Budget Projection Test

Budget  projection  functionality  was  evaluated  for  accuracy  in  setting  and  monitoring  budgets.  The 
system successfully displayed alerts when expenditures exceeded the budget, and users could view and 
modify their budget projections. Detailed results are shown in Table 10.

| 79 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 17 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Table 10. Budget projection test result

No.

Scenario

Test Case

Test Output

1

2

Accessing the 
budget projecting 
page after login

After logging in, the user 
navigates to the budget 
projecting page.

Entering budget 
projection data

The user clicks on the 
budget projection input 
option displayed on the 
page.

3  Deleting incorrect 
budget projection 
data

The user deletes an 
incorrectly entered budget 
projection entry.

The application displays a summary of 
the user’s budgets, including a 
comparison between actual expenses 
and the set budget. 
The user can successfully enter budget 
data, including the budget amount and 
duration, allowing for effectively 
tracking and managing expenses against 
the set budget. 
The user can remove incorrect budget 
data, ensuring accurate budget records 
within the application.

Result

Valid

Valid

Valid

3.2.6. Financial Report Test

The financial report feature was validated for accurate data display, summarizing income, expenses, 
and budget alignment. As shown in Table 11, the report provided users with a comprehensive overview 
of their financial data, supporting better financial decision-making.

Table 11. Financial report test result

No.

Scenario

Test Case

Test Output

1

Accessing the 
financial report page 
after login

2  Displaying financial 
data based on a 
specific budget

After logging in, the user 
navigates to the financial 
report page. 
The user clicks on a specific 
budget or goal displayed on 
the page.

The  application  displays  a  financial 
summary, including the user’s budgets 
and financial goals. 
The user can view detailed financial data 
related to  the selected budget  or  goal, 
allowing them to analyze their financial 
information effectively.

Result

Valid

Valid

3.2.7. Notification Test

The  Notification  module  was  tested  to  ensure  consistent  reminders  and  customizable  notification 
settings.  Users  received  timely  notifications,  as  intended,  even  when  the  application  was  inactive. 
Results are detailed in Table 12.

Table 12. Notification test result

No.

Scenario

Test Case

Test Output

1

2

The user exits the 
application 
temporarily

After entering the data, the 
user exits the application 
because they have finished.

The user clicks on the 
notification provided.

The reminded user 
performs the 
logging action by 
clicking on the 
notification.

After a while, the application displays 
a notification reminder feature to the 
user after the user has finished using 
the application. 
The user can log in, access the 
application’s features, and start 
recording financial transactions 
immediately.

Result

Valid

Valid

| 80 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 18 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.3. Direct User Evaluation Results

The application was evaluated  by  50  users  representing  the  target  demographic  to  gather  feedback. 
Table  13  summarizes  the  average  scores  for  each  evaluation  aspect  based  on  the  Likert  scale,  with 
categories to interpret user satisfaction levels. Each aspect highlights user feedback on the application’s 
performance, functionality, and design elements.

Table 13. Evaluation scores by aspect

No.

Evaluation Aspect

Indicator

% (Tot.)

% (Tot.)

% (Tot.)

% (Tot.)

% (Tot.)

Rated 5

Rated 4

Rated 3

Rated 2

Rated 1

1

Usability

USA1

72% (36)

18% (9)

8% (4)

2% (1)

0% (0)

2

User Satisfaction

USA2

66% (33)

22% (11)

12% (6)

0% (0)

0% (0)

USA3

76% (38)

16% (8)

6% (3)

2% (1)

0% (0)

USS1

USS2

USS3

74% (37)

22% (11)

4% (2)

0% (0)

0% (0)

66% (33)

28% (14)

6% (3)

0% (0)

0% (0)

70% (35)

22% (11)

6% (3)

2% (1)

0% (0)

3

Functionality

FUN1

72% (36)

16% (8)

8% (4)

4% (2)

0% (0)

FUN2

62% (31)

24% (12)

12% (6)

2% (1)

0% (0)

FUN3

66% (33)

24% (12)

6% (3)

4% (2)

0% (0)

4

Engagement

ENG1

68% (34)

20% (10)

10% (5)

2% (1)

0% (0)

5

Design Satisfaction

6

Feedback for Improvement

ENG2

78% (39)

18% (9)

4% (2)

0% (0)

0% (0)

ENG3

76% (38)

20% (10)

4% (2)

0% (0)

0% (0)

DES1

DES2

DES3

FEI1

FEI2

FEI3

74% (37)

18% (9)

6% (3)

2% (1)

0% (0)

70% (35)

24% (12)

4% (2)

2% (1)

0% (0)

64% (32)

22% (11)

10% (5)

4% (2)

0% (0)

78% (39)

20% (10)

2% (1)

0% (0)

0% (0)

68% (34)

24% (12)

8% (4)

0% (0)

0% (0)

66% (33)

26% (13)

6% (3)

2% (1)

0% (0)

The overall application score was calculated by averaging the scores from each evaluation aspect, as 
depicted in Figure 10. This score reflects the application’s comprehensive performance across usability, 
functionality,  and  satisfaction  metrics.  With  an  average  score  of  4.60,  the  application  achieved  an 
Excellent rating, indicating high user satisfaction and effective alignment with target user needs. This 
result  suggests  that,  while  the  application  meets  expectations  in  most  areas,  future  updates  could 
address specific user requests for customization and financial analysis tools, further enhancing the user 
experience.

| 81 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 19 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

4.80
4.75
4.70
4.65
4.60
4.55
4.50
4.45
4.40
4.35
4.30

4.70

4.66

4.60

4.54

4.60 4.60

4.56

4.74

4.72

4.76

4.54

4.52

4.46

4.64

4.62

4.60

4.56

4.46

1
A
S
U

2
A
S
U

3
A
S
U

1
S
S
U

2
S
S
U

3
S
S
U

1
N
U
F

2
N
U
F

3
N
U
F

1
G
N
E

2
G
N
E

3
G
N
E

1
S
E
D

2
S
E
D

3
S
E
D

1
I
E
F

2
I
E
F

3
I
E
F

Usability

User Satisfaction

Functionality

Engagement

Design
Satisfaction

Feedback for
Improvement

1

2

3

4

5

6

Figure 10. The average score for the evaluation aspect

4. DISCUSSION

This study developed and evaluated an Android-based personal finance management application to meet 
young  adults’  financial  literacy  and  management  needs.  Through  a  focus  on  usability,  engagement, 
functionality, and user satisfaction, the results indicate that the application successfully addresses many 
financial management challenges young adults encounter. The findings also suggest potential areas for 
refinement that could further enhance the application’s effectiveness in promoting responsible financial 
habits.

The  study’s  first  objective  was  to  assess  how  effectively  the  application  improved  users’  financial 
management behaviors. With over 90% of users rating it at (4) four or above on the Likert scale, the 
high usability ratings indicate that the application’s design was intuitive and accessible, even for those 
with  minimal  experience  in  financial  tracking.  Usability  is  critical  in  fostering  consistent  usage,  as 
applications that are easy to navigate and visually appealing are more likely to be used regularly. The 
positive user feedback on core features such as expense tracking and budget projections supports this, 
suggesting that users found the application useful and practical for their daily financial activities.

Notably, features like income and expense tracking were highly rated in functionality and satisfaction, 
underscoring their value in enhancing users’ awareness of their spending habits. Encouraging users to 
categorize and analyze their expenses, the application promotes mindful spending, a behavior crucial 
for long-term financial stability. However, while most users engaged consistently with these features, 
some  desired  more  personalized  options,  such  as  customized  budget  categories  and  detailed 
expenditure analysis. These suggestions align with prior studies indicating that personalized financial 
tools can improve engagement by making users feel more connected to their financial data [31], [32].

The  second  research  question  focused  on  whether  regular  engagement  with  the  application  could 
enhance  users’  financial  literacy  and  contribute  to  long-term  financial  resilience.  The  engagement 
scores indicate that the application succeeded in motivating users to track their finances consistently, 
with  a  significant  proportion  of  reporting  plans  to  continue  using  the  app.  This  regular  interaction

| 82 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 20 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

reinforces positive financial habits and increases financial literacy by exposing users to daily spending 
and saving decisions.

The findings suggest that the application’s design elements, such as progress bars for financial goals and 
notification  reminders,  were  important  in  maintaining  user  engagement.  This  aligns  with  behavior 
change theory, which posits that timely reminders and visible progress indicators can reinforce positive 
habits by making achievements tangible [33], [34]. Users specifically mentioned that the visual tracking 
of financial goals motivated them to set and work toward achievable financial objectives, demonstrating 
the application’s potential to foster a proactive approach to financial planning. While notifications were 
generally well-received, some users expressed interest in more customizable reminder options, such 
as  setting  personalized  alert  times.  Incorporating  such  feedback  could  enhance  user  engagement  by 
providing a tailored experience that aligns with individual schedules, which has been shown to increase 
the likelihood of habit formation in digital applications [35], [36], [37].

The  study  also  sought  to  identify  which  features  most  effectively  encouraged  consistent  financial 
management behaviors. Based on user feedback, features such as income and expense tracking, budget 
projections, and financial goal setting were the most impactful. These features align closely with the 
primary  behaviors associated  with  financial  responsibility:  tracking,  planning, and  setting achievable 
financial targets. In particular, the financial goal-setting feature was instrumental in helping users focus 
on  saving  for  specific  objectives.  This  functionality  resonates  with  the  concept  of  “goal-oriented 
behavior,”  which  research  indicates  can  lead  to  increased  motivation  and  better  long-term  financial 
outcomes [38], [39]. By enabling users to break down their financial goals into manageable steps, the 
application helps build confidence and competence in managing money, which are critical to financial 
resilience.

However, some users noted that while the budget projection feature was helpful, it could be further 
improved by allowing for more nuanced budget categories. Additionally, users suggested incorporating 
a more comprehensive financial report that could offer  insights into spending trends over time. Such 
enhancements  would provide  users with a  deeper  understanding  of  their  financial  patterns and help 
them make more informed decisions, a need highlighted by various studies on digital finance tools [40], 
[41], [42]. Integrating these improvements in future updates would likely enhance the application’s role 
as  an  educational  tool  for  financial  literacy.  This  application’s  success  in  engaging  young  adults 
underscores the broader potential for mobile solutions to influence financial behavior. Digital platforms 
are  uniquely  positioned  to  reach  young  users  who  are  comfortable  with  technology  but  may  lack 
financial literacy. By offering an accessible and engaging tool, the application supports the development 
of financial skills essential for navigating complex economic environments.

The  findings  suggest  that,  beyond  practical  utility,  financial  applications  should  emphasize 
personalization and adaptability to cater to individual financial needs and schedules. As young adults 
transition through various life stages, their financial priorities shift; thus, applications that adapt to these 
changes can sustain users’ financial journeys. Moreover, this study highlights the importance of user-
centered design in financial applications, as it significantly impacts engagement and satisfaction. Future 
research could explore the longitudinal impact of consistent app use on financial literacy, particularly 
concerning  debt  reduction,  savings  growth,  and  investment  behavior.  While  the  study  achieved  its 
objectives, it is important to recognize certain limitations. The relatively short evaluation period may 
not fully capture the application’s impact on long-term financial habits. Additionally, while the sample 
was representative of the target demographic, a more extensive and diverse user base would provide a 
broader perspective on user needs and preferences. Future studies could include longitudinal research 
to assess the sustained impact of the application on financial literacy and behavior change.

| 83 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 21 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Furthermore,  implementing  user  feedback  for  added  features,  such  as  trend  analysis  and  advanced 
customization  options,  could  enhance  the  application’s  value.  Expanding  the  application’s  scope  to 
include educational content on financial literacy topics may also increase its impact by providing users 
with  practical  tools  and  theoretical  knowledge.  Given  the  rapid  evolution  of  financial  technology, 
integrating  adaptive  AI  algorithms  to  offer  personalized  financial  advice  could  be  a  promising  future 
direction.

5. CONCLUSION

This  study  successfully  developed  and  evaluated  an  Android-based  personal  finance  management 
application specifically designed for young adults, focusing on usability, engagement, and functionality. 
The application aimed to address its target audience’s specific financial management needs by providing 
tools for tracking income and expense, budget projection, and setting financial goals. Through direct user 
evaluations, the findings revealed high levels of user satisfaction across these core features, indicating that 
the  application  effectively  supports  users  in  managing  their  finances  and  developing  positive  financial 
habits.  Key  outcomes  showed  that  the  application’s  user-friendly  design,  interactive  features,  and 
reminder notifications were essential in encouraging consistent engagement with financial management. 
Features such as financial goal tracking and budget projection fostered mindful spending and motivated 
users  to  set  and  work  toward  achievable  financial  goals,  an  essential  aspect  of  financial  responsibility. 
Despite  these  successes,  feedback  suggested  room  for  improvement.  Users  expressed  interest  in 
additional customization options, such as personalized budget categories and a more detailed analysis of 
spending  trends.  Future  updates  could  also  incorporate  AI-driven  recommendations,  offering  users 
personalized  financial  insights  based  on  spending  behavior,  further  enhancing  the  application's 
functionality. Implementing these features could make the application even more responsive to individual 
user  needs  and  preferences.  Overall,  the  application  demonstrates  significant  potential  to  enhance 
financial  literacy  and  behavior  among  young  adults.  By  offering  an  accessible,  adaptable  platform  for 
personal  finance  management,  this  application  contributes  significantly  to  efforts  toward  improving 
financial resilience in the digital age. Future research could explore the long-term effects of regular app 
usage on financial behavior, including savings growth, debt reduction, and investment practices.

DECLARATIONS

Author Contributions

Riswandha Imawan: Conceptualization, Methodology, Software, Data curation, Writing  - Original 
Draft. Wahyu Permana Putra: Visualization, Writing - Review & Editing. Rabee Alqahtani: Formal 
analysis, Writing - Review & Editing. Emmanouil D. Milakis: Validation, Formal analysis, Writing - 
Review & Editing. Mykhailo Dumchykov: Formal analysis, Writing - Review & Editing. All authors 
have read and approved the final version of this manuscript.

Acknowledgments

The authors wish to express their gratitude to all individuals and organizations that contributed to the 
successful  development  of  this  study.  We  sincerely  thank  the  Faculty  of  Engineering  at  Universitas 
Negeri  Padang  for  their  support  and  resources,  which  were  essential  in  facilitating  this  research. 
Additionally, we acknowledge the invaluable feedback provided by the 50 end-users who participated 
in the testing phase; their insights have significantly contributed to refining the application to  better 
meet the needs of young adults in personal financial management. Finally, we thank our colleagues and 
advisors whose guidance and expertise helped shape this study.

| 84 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 22 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Funding

The authors declare that this research received no external funding.

Competing Interests

The authors declare no competing interests.

Generative AI and AI-Assisted Technologies Statement

The  author(s)  declare  that  no  generative  AI  or  AI-assisted  technologies  were  used  to  prepare  this 
manuscript. All content was created, reviewed, and edited manually by the author(s), who take full 
responsibility for the accuracy and integrity of the manuscript.

REFERENCES

[1]

[2]

T. Koskelainen, P. Kalmi, E. Scornavacca, and T. Vartiainen, “Financial literacy in the digital age—
A  research  agenda,”  Journal  of  Consumer  Affairs,  vol.  57,  no.  1,  pp.  507–528,  Jan.  2023,  doi: 
10.1111/JOCA.12510. 
P. K. Ozili, “Impact of digital finance on financial inclusion and stability,” Borsa Istanbul Review, vol. 
18, no. 4, pp. 329–340, Dec. 2018, doi: 10.1016/J.BIR.2017.12.003.

[3]  A.  Lo  Prete,  “Digital  and  financial  literacy  as  determinants  of  digital  payments  and  personal

finance,” Econ Lett, vol. 213, p. 110378, Apr. 2022, doi: 10.1016/J.ECONLET.2022.110378.

[4]  A.  K.  Khetan  et  al.,  “Variations  in  the  financial  impact  of  the  COVID-19  pandemic  across  5 
continents: A cross-sectional, individual level analysis,” EClinicalMedicine, vol. 44, p. 101284, Feb. 
2022, doi: 10.1016/J.ECLINM.2022.101284.

[5]  M. Nicola et al., “The socio-economic implications of the coronavirus pandemic (COVID-19): A

review,” Int J Surg, vol. 78, p. 185, Jun. 2020, doi: 10.1016/J.IJSU.2020.04.018.

[6]  A.  Lusardi  and  F.-A.  Messy,  “The  importance  of  financial  literacy  and  its  impact  on  financial 
wellbeing,”  Journal  of  Financial  Literacy  and  Wellbeing,  vol.  1,  no.  1,  pp.  1–11,  Apr.  2023,  doi: 
10.1017/FLW.2023.8. 
J. Voßemer, M. Gebel, O. Nizalova, and O. Nikolaieva, “The effect of an early-career involuntary 
job loss on later life health in Europe,” Adv Life Course Res, vol. 35, pp. 69–76, Mar. 2018, doi: 
10.1016/J.ALCR.2018.01.001.

[7]

[8]  A. Save, “Marketing in a mobile-first world: Tackling the why and the how,” Journal of Direct, Data 
Jan.  2014,  doi:

and  Digital  Marketing  Practice,  vol.  15,  no.  3,  pp.  202–212, 
10.1057/DDDMP.2014.8.

[9]  M. Jones et al., “Beyond ‘yesterday’s tomorrow’: future-focused mobile interaction design by and 
for  emergent  users,”  Pers  Ubiquitous  Comput,  vol.  21,  no.  1,  pp.  157–171,  Feb.  2017,  doi: 
10.1007/S00779-016-0982-0.

[10]  L. Stocchi, N. Pourazad, N. Michaelidou, A. Tanusondjaja, and P. Harrigan, “Marketing research 
on Mobile apps: past, present and future,” J Acad Mark Sci, vol. 50, no. 2, pp. 195–225, Mar. 2022, 
doi: 10.1007/S11747-021-00815-W.

[11]  P. Bitrián, I. Buil, and S. Catalán, “Enhancing user engagement: The role of gamification in mobile 
apps,” J Bus Res, vol. 132, pp. 170–185, Aug. 2021, doi: 10.1016/J.JBUSRES.2021.04.028. 
I. Y. Irma, E. sudrajat, N. A. Rachman, and B. Rifai, “The effect of financial literacy on online

[12]

| 85 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 23 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

loans and its impact on poverty,” International Journal of Applied Finance and Business Studies, vol. 11, 
no. 2, pp. 146–154, Sep. 2023, doi: 10.35335/IJAFIBS.V11I2.109.

[13]  W. Puspitasari, “The Effect of Online Loans on the Millennial Generation:  A Systematic Literature 
Review (SLR),” International Journal of Economics Development Research (IJEDR), vol. 5, no. 3, pp. 
2426–2442, Sep. 2024, doi: 10.37385/IJEDR.V5I3.6047.

[14]  K. Czech, L. Ochnio, M. Wielechowski, and S. Zabolotnyy, “Financial Literacy: Identification of 
the Challenges, Needs, and Difficulties among Adults Living in Rural Areas,” Agriculture, vol. 14, 
no. 10, p. 1705, Sep. 2024, doi: 10.3390/AGRICULTURE14101705.

[15]  A. Lusardi, “Financial literacy and the need for financial education: evidence and implications,” 
Swiss Journal of Economics and Statistics, vol. 155, no. 1, pp. 1–8, Jan. 2019, doi: 10.1186/S41937-
019-0027-5.

[16]  V. Leone and P. Thompson, “Financial literacy and advice perceptions among UK higher education 
students:  an  ethnicity  tale?,”  Rev  Econ  Househ,  vol.  22,  no.  2,  pp.  709–781,  Jun.  2024,  doi: 
10.1007/S11150-023-09667-5.

[17]  H. Purnomo, M. Marsely, W. F. Lestari, O. Aryadewa, and F. Z. F. Oktavia, “Eksplorasi Aplikasi 
Pencatatan Keuangan Pribadi Berbasis Android,” Seminar Nasional Gabungan Bidang Sosial - Polinema, 
pp. 145–151, 2021.

[18]  M. C. Mason, G. Zamparo, A. Marini, and N. Ameen, “Glued to your phone? Generation Z’s 
smartphone addiction and online compulsive buying,” Comput Human Behav, vol. 136, p. 107404, 
Nov. 2022, doi: 10.1016/J.CHB.2022.107404. 
J. C. Wang, C. Y. Hsieh, and S. H. Kung, “The impact of smartphone use on learning effectiveness: 
A case study of primary school students,” Educ Inf Technol (Dordr), vol. 28, no. 6, pp. 6287–6320, 
Jun. 2023, doi: 10.1007/S10639-022-11430-9.

[19]

[20]  M. Bauer et al., “Smartphones in mental health: a critical review of background issues, current 
status and future concerns,” International Journal of Bipolar Disorders, vol. 8, no. 1, pp. 1–19, Jan. 
2020, doi: 10.1186/S40345-019-0164-X.

[21]  K. Petersen, C. Wohlin, and D. Baca, “The Waterfall Model in Large-Scale Development,” Lecture 
Notes  in  Business  Information  Processing,  vol.  32,  pp.  386–400,  2009,  doi:  10.1007/978-3-642-
02152-7_29.

[22]  S. Liu, “The Software Development Process,” Formal Engineering for Industrial Software Development,

pp. 235–260, 2004, doi: 10.1007/978-3-662-07287-5_14.

[23]  K. Chari and M. Agrawal, “Impact of incorrect and new requirements on waterfall software project 
outcomes,” Empir Softw Eng, vol. 23, no. 1, pp. 165–185, Feb. 2018, doi: 10.1007/S10664-017-
9506-4.

[24]  M. Bolung and H. R. K. Tampangela, “Analisa Penggunaan Metodologi Pengembangan Perangkat

Lunak,” Jurnal ELTIKOM, vol. 1, no. 1, pp. 1–10, 2017, doi: 10.31961/eltikom.v1i1.1.

[25]  N. Hidayati, “Penggunaan Metode Waterfall Dalam Rancang Bangun Sistem Informasi Penjualan,”

Generation Journal, vol. 3, no. 1, pp. 1–10, 2019.

[26]  T. Yokoyama, H. B. Axelsen, and R. Glück, “Fundamentals of reversible flowchart languages,”

Theor Comput Sci, vol. 611, pp. 87–115, Jan. 2016, doi: 10.1016/J.TCS.2015.07.046.

[27]  H. R. Hiremath and M. J. Skibniewski, “Object-oriented modeling of construction processes by 
unified  modeling  language,”  Autom  Constr,  vol.  13,  no.  4,  pp.  447–468,  Jul.  2004,  doi: 
10.1016/J.AUTCON.2003.09.011.

[28]  L.  Hakim  and  M.  S.  Mardiyamto,  “Relational  Database  Structure  and  Operations  Engineering

| 86 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 24 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Using Class  Diagram  and  Activity Diagram,”  Jurnal  Teknik  Informatika,  Sistem  Infomasi  dan  Teknik 
Industri, vol. 1, no. 1, pp. 109–113, 2018.

[29]  A.  Roman,  “Black-Box  Testing  Techniques,”  A  Study Guide  to  the  ISTQB®  Foundation Level  2018

Syllabus, pp. 25–60, 2018, doi: 10.1007/978-3-319-98740-8_4.

[31]

[30]  R. Fogler, I. Cohen, and D. Peled, “Accelerating Black Box Testing with Light-Weight Learning,” 
Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes 
in Bioinformatics), vol. 13872, pp. 103–120, 2023, doi: 10.1007/978-3-031-32157-3_6. 
I. H. Sarker, “Machine Learning: Algorithms, Real-World Applications and Research Directions,” 
SN Comput Sci, vol. 2, no. 3, pp. 1–21, May 2021, doi: 10.1007/S42979-021-00592-X. 
[32]  A. S. Ferdous, H. S. Akareem, M. Viswanathan, L. D. Hollebeek, and A. Ringer, “Boosting app-
based  mobile  financial  services  engagement  in  B2B  subsistence  marketplaces:  The  roles  of 
marketing strategy and app design,” Industrial Marketing Management, vol. 119, pp. 147–161, May 
2024, doi: 10.1016/J.INDMARMAN.2024.04.014.

[33]  C. Zhang, D. Lakens, and W. A. I. Jsselsteijn, “Theory Integration for Lifestyle Behavior Change 
in the Digital Age: An Adaptive Decision-Making Framework,” J Med Internet Res, vol. 23, no. 4, 
p. e17127, Apr. 2021, doi: 10.2196/17127.

[34]  R. Davis, R. Campbell, Z. Hildon, L. Hobbs, and S. Michie, “Theories of behaviour and behaviour 
change across the social and behavioural sciences: a scoping review,” Health Psychol Rev, vol. 9, no. 
3, p. 323, Aug. 2014, doi: 10.1080/17437199.2014.941722.

[35]  K. Agrawal, S. Athey, A. Kanodia, and E. Palikot, “Digital interventions and habit formation in 
educational  technology,”  Papers,  2024,  Accessed:  Nov.  07,  2024.  [Online].  Available: 
https://ideas.repec.org/p/arx/papers/2310.10850.html

[36]  Y.  Zhu,  Y.  Long,  H.  Wang,  K.  P.  Lee,  L.  Zhang,  and  S.  J.  Wang,  “Digital  Behavior  Change 
Intervention Designs for Habit Formation: Systematic Review,” J Med Internet Res, vol. 26, no. 1, 
p. e54375, May 2024, doi: 10.2196/54375.

[37]  B. Gardner, A. L. Rebar, and P. Lally, “How does habit form? Guidelines for tracking real-world 
habit formation,” Cogent Psychol, vol. 9, no. 1, Dec. 2022, doi: 10.1080/23311908.2022.2041277. 
[38]  B. Hommel, “GOALIATH: a theory of goal-directed behavior,” Psychol Res, vol. 86, no. 4, pp.

1054–1077, Jun. 2022, doi: 10.1007/S00426-021-01563-W.

[39]  H.  Wang,  J.  Yang,  and  P.  Li,  “How  and  when  goal-oriented  self-regulation  improves  college 
students’ wellbeing: A weekly diary study,” Current Psychology, vol. 41, no. 11, pp. 7532–7543, 
Nov. 2022, doi: 10.1007/S12144-020-01288-W.

[40]  W.  Dafri  and  R.  Al-Qaruty,  “Challenges  and  opportunities  to  enhance  digital  financial 
transformation in crisis management,” Social Sciences & Humanities Open, vol. 8, no. 1, p. 100662, 
Jan. 2023, doi: 10.1016/J.SSAHO.2023.100662.

[41]  W. Xu, D. Hu, K. R. Lang, and J. L. Zhao, “Blockchain and digital finance,” Financial Innovation,

vol. 8, no. 1, pp. 1–4, Dec. 2022, doi: 10.1186/S40854-022-00420-Y.

[42]  C.  M.  Malladi,  R.  K.  Soni,  and  S.  Srinivasan,  “Digital  financial  inclusion:  next  frontiers—
challenges and opportunities,” CSI Transactions on ICT, vol. 9, no. 2, pp. 127–134, Aug. 2021, doi: 
10.1007/S40012-021-00328-5.

| 87 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 25 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

This  article  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License,  which  permits  use,  sharing, 
adaptation, distribution, and reproduction in any medium or format, provided that appropriate credit is given to the original author(s) and 
the source, a link to the Creative Commons license is provided, and any modifications are indicated. Unless otherwise specified in a credit line, 
this article’s images or other third-party material are included under the Creative Commons license. If certain material is not covered by the 
article’s Creative Commons license and its intended use is not permitted by statutory regulation or exceeds the allowed usage, permission must 
be obtained directly from the copyright holder. http://creativecommons.org/licenses/by/4.0/.

AUTHOR BIOGRAPHIES

Riswandha  Imawan  holds  a  Bachelor’s  in  Informatics  Engineering  Education 
from  the  Faculty  of  Engineering,  Universitas  Negeri  Padang,  Indonesia.  His 
primary areas of interest include networking systems and application development. 
Riswandha  has  actively  contributed  to  various  software  development  and 
networking projects, focusing on scalable and efficient technological solutions. His 
current work centers on creating software that addresses specific challenges, aiming 
to foster problem-solving through technological integration.

Wahyu  Permana  Putra  holds  a  bachelor’s  degree  in  informatics  engineering 
education from Universitas Negeri Padang and is preparing to complete a master’s 
degree.  As  a  practitioner,  he  focuses  on  software  development  and  informatics 
education,  utilizing  technology  to  improve  educational  methods.  His  recent 
projects emphasize integrating advanced technology to foster a more efficient and 
accessible learning environment.

Rabee  Alqahtani,  a  distinguished  academic  at  the  University  of  Wollongong, 
brings over 20 years of expertise in education with a focus on gifted education and 
artificial  intelligence.  With  an  extensive  publication  record,  his  work  primarily 
addresses  the  needs  of  gifted  learners  and  educational  technology.  His  research 
focuses on informatics education, vocational training, and technological innovation. 
His  contributions  strive  to  cultivate  a  more  adaptable  and  skilled  workforce 
prepared for the demands of a dynamic, tech-driven world.

Emmanouil D. Milakis is a Ph.D. candidate in Education Sciences at European 
University Cyprus and a Special Education IT Instructor at the School of Vocational 
Training  for  People  with  Disabilities  of  Athens.  With  extensive  experience  in 
teaching IT across diverse vocational settings, his current research focuses on Gifted 
STEAM  education.  His  work  aims  to  enhance  cognitive  development  and  social 
inclusion  for  students  with  diverse  needs,  leveraging  technology  to  create  more 
accessible, engaging, and effective educational experiences.

| 88 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

---

<!-- PAGE 26 -->

Journal of Hypermedia & Technology-Enhanced Learning  
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

Mykhailo Dumchykov is a lecturer at Sumy State University, Ukraine. He has 
over six years of experience in vocational education and specializes in cybercrime. 
He has published extensively in the fields of information crime and cybercrime. His 
current  research  is  focused  on  crime  in  the  digital  environment.  Mykhailo 
Dumchykov’s research contributions aim to develop methodologies for combating 
crime in cyberspace, drawing on the experience of leading nations worldwide.

Publisher’s  and  Journal’s  Note  Sagamedia  Teknologi  Nusantara,  as  the  publisher  and  editor  of  the  Journal  of  Hypermedia  & 
Technology-Enhanced Learning (J-HyTEL), upholds the highest ethical standards in academic publishing. The journal remains neutral with 
regard to jurisdictional claims in published maps and institutional affiliations. Authors are fully responsible for the originality, accuracy, and 
integrity of their work. Post-publication ethical concerns will be addressed through corrections, clarifications, or retractions as necessary. The 
content of this publication has not been approved by the United Nations and does not reflect the views of the United Nations or its officials or 
Member States. https://www.un.org/sustainabledevelopment

| 89 | https://doi.org/10.58536/j-hytel.166  
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | 64 |
e-ISSN: 2985–9166 | 10.58536/j-hytel.166
RESEARCH ARTICLE
Enhancing Financial Literacy in Young Adults: An Android-Based Personal
Finance Management Tool
Riswandha Imawan1* , Wahyu Permana Putra1 , Rabee Alqahtani2 , Emmanouil D.
Milakis3 , Mykhailo Dumchykov4
1 Faculty of Engineering, Universitas Negeri Padang, Padang, Indonesia
2 School of Education, University of Wollongong, NSW 2500, Australia
3 Department of Education Sciences, European University Cyprus, Engomi, Cyprus
4 Sumy State University, Sumy, Ukraine
*Corresponding Author: r1smawan024@gmail.com
This article ABSTRACT
contributes to:
This study details the design, development, and evaluation of an Android-based personal finance
management application tailored for young adults in higher education. Addressing unique
financial challenges such as limited experience and fluctuating income, the application
incorporates features like income tracking, expense monitoring, budgeting, and financial goal
setting. Developed using the Waterfall model, the application includes secure login systems,
intuitive transaction management, customizable goals, budget projections, and automated
notifications to encourage financial discipline. Usability evaluations using a 5-point Likert scale
with 50 users revealed an overall satisfaction score of 4.6/5, rated 'Excellent.' Users praised the
intuitive design, accurate tracking, and motivational reminders, while also suggesting additional
customization and deeper financial analysis for future updates. This study demonstrates the
potential of targeted digital tools to foster financial literacy and resilience, offering evidence that
personalized technology can significantly improve financial behaviors in young adults. Future
research will explore enhanced customization and AI-driven features to further refine the
application’s impact.
KEYWORDS
Personal financial management; mobile app; financial habits; young adults; higher education
Received: Nov. 07, 2024; Revised: Dec. 10, 2024; Accepted: Dec. 25, 2024; Published Online: Jan. 27, 2025
How to cite: Imawan, R., Putra, W. P., Alqahtani, R., Milakis, E. D., & Dumchykov, M. (2025). Enhancing
Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool. Journal of Hypermedia
& Technology-Enhanced Learning, 3(1), 64-89. https://doi.org/10.58536/j-hytel.166
Published by Sagamedia Teknologi Nusantara
© The Author(s) 2025| This is an open-access article under the CC BY 4.0 license.
1. INTRODUCTION
The rapid advancement of digital technology has transformed modern life, bringing both opportunities
and challenges across various sectors, particularly in personal finance [1], [2], [3]. Personal finance
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
management has become critical, especially for young adults facing unique financial challenges in
today’s economy. Financial literacy and responsible financial behavior are increasingly important,
especially after the pandemic’s economic impact [4], [5]. As of December 2021, Indonesians aged 19-
34 accounted for 63% of online loan users, according to the Financial Services Authority of Indonesia
(OJK), with a significant concentration in urban areas. This demographic, composed mainly of students
and early-career individuals, is vulnerable to financial mismanagement due to limited experience and
guidance in financial decision-making [6], [7]. A survey among Informatics Education students at
Universitas Negeri Padang highlighted this issue, showing that fewer than 50% consistently recorded
their finances, just 20% regularly reviewed income and expenses, and merely 40% adhered to a
monthly budget.
Despite increasing awareness of the importance of financial literacy, there remains a practical gap in
using tools tailored to engage and empower young adults in managing their finances effectively. Many
existing financial management tools are designed for a general audience, often overlooking the unique
needs and behaviors of younger users, who are more inclined toward interactive, mobile-first solutions
[8], [9]. Although prior studies have established the importance of financial literacy, few have explored
how a targeted mobile application can directly influence and improve financial habits among young
Indonesian adults [10], [11].
Addressing this gap is crucial since financial behaviors established in early adulthood have significant
long-term implications. The prevalence of high online loan usage among young Indonesians highlights
an urgent need for tools that encourage responsible financial habits [12], [13]. Without timely
intervention, financial literacy deficits may perpetuate a cycle of debt and instability. By providing a
mobile solution that promotes consistent financial tracking and budgeting, this study intends to instill
positive financial behaviors early on, establishing a foundation for financial resilience.
This study aims to develop an Android-based personal finance management application tailored to the
needs of young adults, equipped with features for tracking income, setting budgets, monitoring
expenses, and establishing financial goals. It further evaluates the application’s usability and its impact
on users’ financial behaviors, focusing on fostering consistent engagement and improving financial
literacy. The research questions guiding this study are as follows:
1) How effective is an Android-based personal financial management application in improving the
financial habits of young adults in higher education?
2) To what extent can regular engagement with the application enhance financial literacy and
contribute to long-term financial resilience among users?
3) Which features most effectively promote consistent financial management behaviors, such as
budgeting, expense tracking, and goal setting?
Proactive and practical steps are necessary to prevent younger generations from falling into financial
difficulties. A foundational strategy for improving financial literacy is consistently recording and
managing personal finances [14]. This practice helps individuals align their spending habits with their
needs, plans, and goals. Effective personal financial management hinges on strategically allocating
income across expenses, savings, and investments [15]. Individuals bear responsibility for managing
their finances as a critical aspect of daily life, which can yield positive outcomes, particularly in curbing
excessive consumerism [16].
Moreover, financial management is a vital 21st-century skill, resting on four pillars: income, expenses,
savings, and planning. Healthy finances result from sustainable and deliberate money management [17].
To address this challenge, fostering financial habits requires tools that are both accessible and easy to
| 65 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
maintain. Research underscores that mobile phones—used frequently in daily life—are ideal platforms
for cultivating such habits [18], [19], [20]. By leveraging this technology, the proposed application
serves as a platform to reinforce consistent financial tracking and reflection.
This research addresses a critical gap by targeting younger demographics with a customized digital
solution for personal finance management. The study contributes to advancing financial literacy as a
fundamental 21st-century competency through practical implementation and evaluation. By integrating
goal-setting frameworks, automated reminders, and an intuitive interface, the application offers a
holistic approach to nurturing healthier financial habits and mitigating financial instability among
Indonesia’s young adults.
2. METHODS
This research employed the Waterfall model, a structured software development methodology, to
ensure systematic progression through sequential phases: requirements analysis, design,
implementation, testing, and deployment [21], [22], [23]. This approach enabled organized execution
and thorough validation at each stage, minimizing iterative backtracking and ensuring alignment with
user needs [24], [25]. The methodology’s stages are illustrated in Figure 1.
Figure 1. Phases of the waterfall model
The Waterfall model was chosen for its linear, phase-gated structure, which ensured systematic
validation of user requirements before advancing to design and coding. This minimized scope creep and
aligned with the study’s focus on replicable, structured development for academic evaluation.
2.1. Requirements Analysis
The initial phase focused on mapping user behaviors and needs through interviews and surveys targeting
young adults in higher education. The goal was to identify core financial management processes and
translate them into application features that promote engagement and financial literacy. Key processes
observed in user workflows are summarized in Table 1.
| 66 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Table 1. Key financial management processes identified through requirements analysis
No. Process Activity Actor
1 Income Tracking Users record income received in financial journals, mobile Individual
notes, or calculators.
2 Expense Tracking Users record expenses incurred, often using financial journals, Individual
mobile notes, or calculators.
3 Budget Projection Users use financial journals, mobile notes, or calculators to Individual
record and plan anticipated expenses.
This analysis led to identifying additional requirements to enhance the application's usability and
functionality. These enhancements addressed everyday financial management needs, making the
application more intuitive and adaptable to user preferences. The additional requirements are outlined
Table 2, which details each feature’s purpose and contribution to an improved user experience.
Table 2. Additional requirements for enhanced usability and functionality
No. Feature(s) Process(es)
1 Income/Expense Users record the amount of income/expense received. This recording is
Data Tracking typically conducted in financial journals, on mobile notes, or using calculators.
Users can categorize the entered data, classifying income/expense by type,
method of acquisition, and other relevant factors.
Users may also attach notes to each entry detailing aspects such as the source of
income/expense, method of acquisition, and other pertinent information.
2 Financial Goal Data Users can input data related to their financial goals, adjusting target amounts and
Tracking timeframes according to their capacity.
Users receive progress updates on their financial goals based on their transaction
history.
Users are provided with information and recommendations on optimal saving
amounts to reach their financial goals effectively.
3 Budget Projection Users can input data for monthly budget projections based on their monthly
Tracking income and expenses.
Users receive budget information aligned with their historical financial reports.
4 Financial Reports Users can access a summary of expenses and income based on the data they
enter.
2.2. Design
2.2.1. Flowchart
A flowchart is a structured diagram that uses standardized symbols to visually represent systematic
procedures for completing a process [26]. It depicts workflows through symbols such as rectangles
(process steps), diamonds (decision points), and arrows (directionality) [27]. Figure 2 illustrates the
system flow of the financial management application, outlining the user journey from initial login to
feature interaction.
| 67 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Figure 2. Application flowchart
When users launch the application, they are presented with a login screen requiring email and password
entry to access their financial data. Unregistered users must complete a registration process before
proceeding. Upon successful authentication, users reach the homepage, where they can navigate
features including expense tracking, income recording, financial goal-setting, budget projections, and
financial reports. Each feature incorporates guided input and output steps to streamline user
interaction. After completing a task, users may either explore additional features or exit the
application.
2.2.2. Activity Diagram
The activity diagram models the dynamic flow of system activities, emphasizing the sequence and
interaction of user actions [28]. Figure 3 depicts activity diagrams for the home and login functions,
capturing initial user engagement and authentication workflows.
▪ Login Activity Diagram: Details the authentication process, including registration,
credential validation, and error handling for incorrect inputs.
▪ Home Activity Diagram: Represents the central interface users navigate to core features.
Transitions between activities (e.g., moving from expense tracking to budget projections) are
mapped to reflect user pathways.
| 68 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
(a) (b)
Figure 3. Activity diagram: (a) Home; (b) Login
Figure 4 presents activity diagrams for income/expense tracking and financial goal management:
▪ Income/Expense Tracking: Outlines the workflow for inputting transactions, including
steps for categorization (e.g., type, payment method), adding contextual notes, and saving
records. Decision points validate data completeness (e.g., mandatory amount fields).
▪ Financial Goal Management: Models setting, adjusting, and tracking goals. Users define
targets (amount, deadline), receive progress updates, and can modify goals based on changing
circumstances.
(a) (b)
Figure 4. Activity diagram: (a) Income/expense tracking; (b) Financial goal
| 69 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
(a) (b)
Figure 5. Activity diagram: (a) Budget projecting; (b) Financial report
Additionally, Figure 5 displays the activity diagrams for the budget projecting and financial report
features. In the budget projecting activity diagram, users input and adjust their monthly projections as
needed. The financial report activity diagram gives users an overview of their recorded financial data,
enabling them to review and analyze their income, expenses, and budget alignment.
2.3. Implementation
The application was developed using Laravel (backend) and Flutter (frontend), ensuring secure data
handling and cross-platform compatibility. Laravel’s MVC architecture facilitated RESTful API
development, while Flutter’s widget-based framework enabled a responsive UI across Android and
iOS. Key modules were implemented as follows:
2.3.1. Login Module
The module securely manages user access to the application by providing fields for users to enter their
email and password, with data encrypted using industry-standard security protocols to protect
credentials. If users forget their password, they can reset it through a secure process that sends a
verification code to their registered email. Additionally, the login process validates input formats, such
as correct email format and minimum password length, to ensure data integrity and enhance security.
2.3.2. Income/Expense Tracking Module
This module allows users to record their income and expenses with tools for categorization and detailed
tracking. Users can input transaction amounts, assign categories (e.g., ‘Food,’ ‘Rent,’
‘Entertainment’), and add custom notes to specify details such as income sources or reasons for
expenses. The system enables users to edit or delete records, ensuring accuracy and flexibility in their
financial tracking. Transactions are stored in a local SQLite database, providing quick access and offline
functionality, with options for cloud storage synchronization.
| 70 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
2.3.3. Financial Goal Module
The financial goal module supports users in setting and tracking financial goals, such as saving for a
purchase or building an emergency fund. Users can define specific goals with target amounts and
deadlines, and the application tracks progress toward these goals based on recorded income and
expenses. This module includes a progress bar that visually represents the percentage of the target
achieved, and users receive updates as they get closer to their goals. The module also includes a feature
that allows users to adjust goals, enabling them to modify target amounts or deadlines as their needs
change. Additionally, it provides personalized saving recommendations based on analyzing the user’s
financial data, suggesting realistic saving amounts to help users reach their goals on schedule.
2.3.4. Budget Projection Module
This module enables users to set and monitor monthly budgets across various categories, such as
“Housing,” “Utilities,” “Entertainment,” and “Savings.” Users can input specific budget amounts for
each category and set durations to apply a budget across multiple months. The module compares user
expenditures with the set budget, providing visual indicators (e.g., color-coded progress bars) to show
users if they are within or exceeding their budget. If users exceed their budget, the system displays
alerts encouraging budget adjustments. The budget data integrates with historical financial reports,
allowing users to compare current and past spending habits, which helps refine future budgets.
2.3.5. Notification Module
The notification module enhances user engagement by providing regular reminders to update financial
data and review goals. This flexible module allowed users to set notification preferences such as daily
or weekly reminders. Notifications encourage users to record their expenses, check their budgets, and
update their progress on financial goals. The reminders use Android’s built-in notification service,
ensuring they appear even when the application is closed, thus supporting consistent financial tracking
and habit formation. The application sends custom alerts to users when they are close to reaching a
financial goal or approaching a budget limit.
2.4. Testing
We conducted black-box testing to evaluate the application’s functionality from an end-user
perspective, ensuring it met performance standards without inspecting the internal code [29], [30].
This approach allowed us to test each feature for usability, reliability, and accurate functionality based
on expected outcomes. The testing procedure was structured to verify alignment with the application’s
requirements, focusing on key modules, including login, income/expense tracking, goal setting,
budget projection, financial reporting, and notifications.
Through black-box testing, we validated the application’s robustness using scenarios representing
typical user interactions. This approach accurately assessed the application’s performance and user
experience, with detailed outcomes in the results section. As shown in Table 3, the testing covered
each primary module, focusing on specific aspects of functionality essential to providing a seamless user
experience.
| 71 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Table 3. Testing modules and evaluation focus
No. Module Focus of Evaluation
1 Login Page Secure access, user credential validation, and “forgot password”
functionality.
2 Home Page Accessibility to all features, navigation between modules, and accuracy of
financial summaries.
3 Income/Expense Tracking Accuracy of data entry, categorization, and record deletion
functionalities.
4 Financial Goal Goal setting, progress tracking, and goal adjustment capabilities.
5 Budget Projection Accuracy in budget setting, monitoring, and alerts when exceeding
budgets.
6 Financial Report Accuracy of data display, summarization of income, expenses, and budget
alignment.
7 Notification Consistency of reminders, notification customization, and functionality
when the application is inactive.
2.5. Deployment
In the deployment phase, the application was evaluated directly with a selected group of end users
representing the target audience. This process aimed to gather preliminary feedback on the
application’s functionality, usability, and user satisfaction before its official release. An evaluation was
conducted in a beta testing format, involving users who matched the target profile (aged 19-34,
students or individuals requiring personal financial management).
2.5.1. Direct User Evaluation Process
We randomly selected 50 university students within the target age range who met personal finance
management criteria. Each student received a detailed explanation of the research goals, participant
rights, and data privacy policies. Participation was voluntary, with an option to withdraw at any time.
After providing informed consent, students accessed the application and received brief training on key
features, including income tracking, goal setting, and budget projection. Over a two-week testing
period, participants used various Android devices commonly used by the target demographic, including
Samsung, Xiaomi, and Oppo models running Android 10 or later. At the end of the period, participants
completed a survey about their experience. All data collected was anonymized and used solely to
improve the application.
2.5.2. Evaluation Instrument
The evaluation instrument consisted of a survey based on a 1-5 Likert scale to measure users’ responses
to each evaluation aspect. This instrument covered the following evaluation aspects and indicators, as
shown in Table 4.
| 72 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Table 4. Evaluation aspects and key indicators
No. Aspect Code Key Indicators
1 Usability USA1 The application is easy to use, even for first-time users.
USA2 Navigation between features in the application is easy to understand.
USA3 The application’s interface design makes it easy for users to access features.
2 User USS1 I am satisfied with this application’s income/expense tracking function.
Satisfaction
USS2 The budget projection feature aligns with my financial management needs.
USS3 The reminder notifications help me stay consistent in tracking my finances.
3 Functionality FUN1 This application accurately records and displays my financial data.
FUN2 Each available feature functions as described and meets my expectations.
FUN3 I have encountered no issues or errors when using the application’s main
features.
4 Engagement ENG1 This application helps me stay more organized in daily financial management.
ENG2 I am likely to continue using this application routinely over the long term.
ENG3 The features provided motivate me to track and manage my finances more
effectively.
5 Design DES1 The visual design of this application is attractive and comfortable to view.
Satisfaction
DES2 The layout of features in the application makes it easy to find the information I
need.
DES3 The color scheme and visual elements help clarify each feature’s function.
6 Feedback for FEI1 The application would benefit from additional customization options for budget
Improvement or financial categories.
FEI2 I want a more detailed financial trend analysis feature to help evaluate expenses.
FEI3 Adding options for notification timing would be very helpful in aligning with
my schedule.
2.5.3. Data Analysis
We analyzed the data collected from the evaluation survey to identify the application’s strengths and
areas for improvement based on end-user feedback. The analysis centered on calculating average scores
for each evaluation aspect, which were then categorized to provide a comprehensive view of the
application’s performance across key dimensions. This approach allowed us to highlight specific areas
where the application met or exceeded expectations and pinpoint aspects that could benefit from
targeted enhancements.
We recorded each user’s response on a 1-5 Likert scale for every indicator, and average scores were
calculated across all responses. This average score represented the application’s performance on each
specific indicator within an evaluation aspect. For each evaluation aspect, the average scores of all
indicators were then summed and divided by the number of indicators to obtain an aspect score
(Equation 1). This score provided an overall measure of the application’s performance within each
aspect.
∑(𝐼𝑛𝑑𝑖𝑐𝑎𝑡𝑜𝑟𝑠 𝑆𝑐𝑜𝑟𝑒𝑠)
𝐴𝑠𝑝𝑒𝑐𝑡 𝑆𝑐𝑜𝑟𝑒= (1)
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐼𝑛𝑑𝑖𝑐𝑎𝑡𝑜𝑟𝑠
| 73 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
The overall application score was calculated by averaging the aspect scores from each evaluation aspect,
as shown in Equation 2, to represent the application’s general performance across all aspects. This
overall application score provided a single value summarizing the application’s effectiveness and user
satisfaction.
∑(𝐴𝑠𝑝𝑒𝑐𝑡𝑠 𝑆𝑐𝑜𝑟𝑒𝑠)
𝑂𝑣𝑒𝑟𝑎𝑙𝑙 𝐴𝑝𝑝𝑙𝑖𝑐𝑎𝑡𝑖𝑜𝑛 𝑆𝑐𝑜𝑟𝑒= (2)
𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐴𝑠𝑝𝑒𝑐𝑡𝑠
Table 5 shows the scoring categories for aspect evaluations, providing qualitative interpretations based
on score ranges. These categories included excellent (4.21 - 5.00), good (3.41 - 4.20), fair (2.61 -
3.40), poor (1.81 - 2.60), and very poor (1.00 - 1.80), allowing each score to be easily interpreted
based on user expectations.
Table 5. Aspect scores and categories
Score Range Category Interpretation
4.21 - 5.00 Excellent The application fully meets user expectations in this aspect.
3.41 - 4.20 Good The application performs well in this aspect but may benefit from minor
improvements.
2.61 - 3.40 Fair The application meets some expectations but has areas that require
improvement.
1.81 - 2.60 Poor The application does not meet most user expectations and requires significant
improvement.
1.00 - 1.80 Very Poor The application fails to meet user expectations in this aspect. Significant
changes are needed.
The final analysis included reporting each aspect’s score and category along with the overall application
score to provide a comprehensive view of the application’s performance. High scores (excellent, good)
indicated strengths in areas that met or exceeded user expectations, while moderate scores (fair)
suggested areas needing targeted improvements. Lower scores (poor, very poor) highlighted critical
weaknesses requiring significant adjustments. This structured analysis yielded actionable insights for
future development, helping prioritize improvements based on user needs and aligning further
development to enhance user satisfaction and functionality.
3. RESULTS
The results are presented following each stage of the development process, as outlined in the methods
section. This approach explains how the application’s features were implemented, tested, and refined
based on user feedback.
3.1. Application Development Results
The development phase focused on creating a usable, secure, functional personal financial management
application. The final product incorporated the following key features:
| 74 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
3.1.1. Login Page
The login page, developed based on initial design requirements, provides a secure and user-friendly
interface. It features encrypted password storage to protect user credentials, while the “forgot
password” option offers a streamlined recovery process for users who may have misplaced their login
details. As shown in Figure 6, the login page includes fields for email and password entry, guiding users
through secure access to the application. Additionally, the application stores users’ financial data and
records securely in the database, allowing seamless retrieval upon login. Once logged in, users can
access the full range of personal financial management features the application provides, establishing a
straightforward and secure entry point.
Figure 6. Login page display
3.1.2. Home Page
After a successful login, users are directed to the home page, which functions as the main dashboard of
the application. This interface organizes access to all core features, including expense tracking, income
recording, financial goals, budget projection, and financial reporting. As shown in Figure 7(a), the
home page layout is designed to ensure that users can quickly navigate between different modules
without confusion, enhancing the application’s usability. The structured and intuitive design allows
users to seamlessly interact with all features, promoting a cohesive experience that makes personal
financial management straightforward and accessible.
3.1.3. Income/Expense Tracking
The income/expense tracking module was developed to enable users to record and categorize their
financial transactions accurately. This feature enables users to input details for income and expenses,
organize transactions by category, and edit or delete records as necessary, as illustrated in Figure 7(b).
The application helps users maintain accuracy and stay on top of their financial data by supporting these
actions. This module gives users clear insights into their spending patterns and income sources, which
are fundamental for effective financial planning and control.
| 75 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
(a) (b)
Figure 7. (a) Home page display; (b) Income/expense tracking display
3.1.4. Financial Goals
The financial goals module allows users to actively manage and track their financial objectives. As shown
in Figure 8(a), users can create categories for specific goals, such as saving for emergencies, vacation
planning, or future investments, allowing them to organize and prioritize their goals more effectively.
The system updates users on their progress by tracking saved or invested amounts over time, fostering
a sense of achievement as they work toward their targets. Furthermore, if users need to adjust their
goals to align with changing financial circumstances, they can modify or remove goals as needed. This
feature motivates users to focus on their objectives while offering flexibility to adapt to personal
financial shifts.
3.1.5. Budget Projection
The budget projection feature enables users to set up monthly or custom plans based on their financial
needs. When accessing this page, shown in Figure 8(b), users can input specific details such as budget
name, category, duration, and amount. This feature helps users track and manage their budgets per
their spending habits. Users can use the delete function to remove incorrect data if an error occurs,
ensuring that their projections remain accurate and tailored to their preferences. This flexible and
customizable approach to budgeting helps users gain better control over their financial resources,
promoting thoughtful and organized spending.
3.1.6. Financial Reports
The financial report module consolidates all user data, providing comprehensive income, expenses, and
budget adherence summaries. As shown in Figure 9(a), this feature displays the user-defined budget
alongside a detailed history of financial entries. By offering insights into spending patterns and income
trends, the report helps users make informed financial decisions. This feature highlights areas where
adjustments may be needed and enables users to plan strategically for future goals, making it a valuable
tool for sustained financial health and accountability.
| 76 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
3.1.7. Notification Reminder
The notification reminder feature is essential in promoting consistent user engagement with the
application. As depicted in Figure 9(b), this feature sends periodic reminders, encouraging users to log
financial activities regularly. By fostering a habit of consistent tracking, the notification system aims to
help users develop a comprehensive understanding of their financial status over time. This awareness
enables them to make more deliberate choices regarding expenses and savings, supporting responsible
and strategic financial behavior in line with their objectives.
(a) (b)
Figure 8. (a) Financial goal display; (b) Budget projection display
(a) (b)
Figure 9. (a) Financial report; (b) Notification reminder display
| 77 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
3.2. Application Testing Results
Each core module of the application was subjected to black-box testing, which confirmed the
functionality, reliability, and user experience aspects. Below are the results for each module:
3.2.1. Login Page Test
The login page was tested to confirm that it provides secure access, validates user credentials, and
supports the “forgot password” function. As shown in Table 6, the application successfully displayed
the login interface, validated correct input, and directed users to the homepage upon successful login.
Table 6. Login page test result
No. Scenario Test Case Test Output Result
1 Login as a user Click on the login button. The application displays the login Valid
page, where users can enter their
username and password. A button is
also available for users who have
forgotten their password.
2 Accessing Click on the various buttons Each button clicked takes the user to Valid
application available on the homepage. the corresponding feature or
features functionality as designed in the
application.
3 Logging into the Enter the username and Users with registered accounts can Valid
application password to log in. successfully log in and access the
application’s features.
4 User forgets Click on the “Forgot your The user is redirected to the password Valid
password password?” button. recovery page, and the system sends a
verification code to the user’s
registered email address.
3.2.2. Home Page Test
Testing on the home page confirmed access to all features, smooth navigation between different
modules, and accurate display of financial summaries. Users can view and select various features from
the dashboard, as detailed in Table 7.
Table 7. Home page test result
No. Scenario Test Case Test Output Result
1 Users access the After logging in, the user The application displays a financial Valid
system after enters the system to view summary based on the features
logging in their financial summary. provided.
2 Viewing financial The user clicks on the The user can view a detailed and Valid
summary in detail displayed financial comprehensive financial summary
summary. within the application.
3 Accessing The user clicks on various The user selects and uses each feature Valid
application features features available in the according to its intended purpose and
application. functionality.
| 78 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
3.2.3. Income/Expense Tracking Test
The Income/expense tracking module was tested for data entry, categorization, and deletion
functionalities. As illustrated in Table 8, users could successfully enter and manage income/expense
transactions with accurate categorization and record management.
Table 8. Income/expense tracking test
No. Scenario Test Case Test Output Result
1 Accessing the After logging in, the user The application displays a summary of Valid
income/expense navigates to the the user’s recorded income/expense.
tracking page income/expense tracking
after login page.
2 Entering The user clicks on the The user can enter and record Valid
income/expense income/expense data input income/expense data into the
transaction data option displayed on the page. application.
3 Deleting incorrect The user deletes an The user can remove the incorrect Valid
income/expense incorrectly entered income/expense data, ensuring
transaction data income/expense entry. accuracy in the recorded transactions.
4 Viewing income The user views the previously The user can review all Valid
transaction data entered income/expense income/expense data entered into the
data. application.
3.2.4. Financial Goal Test
The financial goal module testing confirmed that users could set, track, and update their financial goals.
Users received progress updates and were able to adjust their goals as needed, which aligns with the
intended design (refer to Table 9 for detailed results).
Table 9. Financial goal test result
No. Scenario Test Case Test Output Result
1 Accessing the After logging in, the user The application displays a summary Valid
financial goal navigates to the financial goal of the user’s financial goals and
page after login page. progress toward each goal. Options
are available for adding or removing
goal progress.
2 Entering financial The user clicks on the financial Users can enter data for a financial Valid
goal data goal input option displayed on goal, including the target and
the page. progress tracking, allowing them to
record and monitor their goals
within the application.
3 Deleting The user deletes an incorrectly The user can successfully remove Valid
incorrect financial entered financial goal entry. incorrect financial goal data, ensuring
goal data accurate tracking of their goals.
3.2.5. Budget Projection Test
Budget projection functionality was evaluated for accuracy in setting and monitoring budgets. The
system successfully displayed alerts when expenditures exceeded the budget, and users could view and
modify their budget projections. Detailed results are shown in Table 10.
| 79 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Table 10. Budget projection test result
No. Scenario Test Case Test Output Result
1 Accessing the After logging in, the user The application displays a summary of Valid
budget projecting navigates to the budget the user’s budgets, including a
page after login projecting page. comparison between actual expenses
and the set budget.
2 Entering budget The user clicks on the The user can successfully enter budget Valid
projection data budget projection input data, including the budget amount and
option displayed on the duration, allowing for effectively
page. tracking and managing expenses against
the set budget.
3 Deleting incorrect The user deletes an The user can remove incorrect budget Valid
budget projection incorrectly entered budget data, ensuring accurate budget records
data projection entry. within the application.
3.2.6. Financial Report Test
The financial report feature was validated for accurate data display, summarizing income, expenses,
and budget alignment. As shown in Table 11, the report provided users with a comprehensive overview
of their financial data, supporting better financial decision-making.
Table 11. Financial report test result
No. Scenario Test Case Test Output Result
1 Accessing the After logging in, the user The application displays a financial Valid
financial report page navigates to the financial summary, including the user’s budgets
after login report page. and financial goals.
2 Displaying financial The user clicks on a specific The user can view detailed financial data Valid
data based on a budget or goal displayed on related to the selected budget or goal,
specific budget the page. allowing them to analyze their financial
information effectively.
3.2.7. Notification Test
The Notification module was tested to ensure consistent reminders and customizable notification
settings. Users received timely notifications, as intended, even when the application was inactive.
Results are detailed in Table 12.
Table 12. Notification test result
No. Scenario Test Case Test Output Result
1 The user exits the After entering the data, the After a while, the application displays Valid
application user exits the application a notification reminder feature to the
temporarily because they have finished. user after the user has finished using
the application.
2 The reminded user The user clicks on the The user can log in, access the Valid
performs the notification provided. application’s features, and start
logging action by recording financial transactions
clicking on the immediately.
notification.
| 80 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166

3.3. Direct User Evaluation Results
The application was evaluated by 50 users representing the target demographic to gather feedback.
Table 13 summarizes the average scores for each evaluation aspect based on the Likert scale, with
categories to interpret user satisfaction levels. Each aspect highlights user feedback on the application’s
performance, functionality, and design elements.
Table 13. Evaluation scores by aspect
|      |                    |            | % (Tot.)  | % (Tot.)  | % (Tot.)  | % (Tot.)  | % (Tot.)  |
| ---- | ------------------ | ---------- | --------- | --------- | --------- | --------- | --------- |
| No.  | Evaluation Aspect  | Indicator  |           |           |           |           |           |
|      |                    |            | Rated 5   | Rated 4   | Rated 3   | Rated 2   | Rated 1   |
1  Usability  USA1  72% (36)  18% (9)  8% (4)  2% (1)  0% (0)
|      |     | USA2  | 66% (33)  | 22% (11)  | 12% (6)  | 0% (0)  | 0% (0)  |
| ---- | --- | ----- | --------- | --------- | -------- | ------- | ------- |

|     |     | USA3  | 76% (38)  | 16% (8)  | 6% (3)  | 2% (1)  | 0% (0)  |
| --- | --- | ----- | --------- | -------- | ------- | ------- | ------- |
2  User Satisfaction  USS1  74% (37)  22% (11)  4% (2)  0% (0)  0% (0)
|      |     | USS2  | 66% (33)  | 28% (14)  | 6% (3)  | 0% (0)  | 0% (0)  |
| ---- | --- | ----- | --------- | --------- | ------- | ------- | ------- |

|     |     | USS3  | 70% (35)  | 22% (11)  | 6% (3)  | 2% (1)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | ------- | ------- | ------- |
3  Functionality  FUN1  72% (36)  16% (8)  8% (4)  4% (2)  0% (0)
|      |     | FUN2  | 62% (31)  | 24% (12)  | 12% (6)  | 2% (1)  | 0% (0)  |
| ---- | --- | ----- | --------- | --------- | -------- | ------- | ------- |

|     |     | FUN3  | 66% (33)  | 24% (12)  | 6% (3)  | 4% (2)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | ------- | ------- | ------- |
4  Engagement  ENG1  68% (34)  20% (10)  10% (5)  2% (1)  0% (0)
|      |     | ENG2  | 78% (39)  | 18% (9)  | 4% (2)  | 0% (0)  | 0% (0)  |
| ---- | --- | ----- | --------- | -------- | ------- | ------- | ------- |

|     |     | ENG3  | 76% (38)  | 20% (10)  | 4% (2)  | 0% (0)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | ------- | ------- | ------- |

5  Design Satisfaction  DES1  74% (37)  18% (9)  6% (3)  2% (1)  0% (0)
|      |     | DES2  | 70% (35)  | 24% (12)  | 4% (2)  | 2% (1)  | 0% (0)  |
| ---- | --- | ----- | --------- | --------- | ------- | ------- | ------- |

|     |     | DES3  | 64% (32)  | 22% (11)  | 10% (5)  | 4% (2)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | -------- | ------- | ------- |
6  Feedback for Improvement  FEI1  78% (39)  20% (10)  2% (1)  0% (0)  0% (0)
|     |     | FEI2  | 68% (34)  | 24% (12)  | 8% (4)  | 0% (0)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | ------- | ------- | ------- |

|     |     | FEI3  | 66% (33)  | 26% (13)  | 6% (3)  | 2% (1)  | 0% (0)  |
| --- | --- | ----- | --------- | --------- | ------- | ------- | ------- |
The overall application score was calculated by averaging the scores from each evaluation aspect, as
depicted in Figure 10. This score reflects the application’s comprehensive performance across usability,
functionality, and satisfaction metrics. With an average score of 4.60, the application achieved an
Excellent rating, indicating high user satisfaction and effective alignment with target user needs. This
result suggests that, while the application meets expectations in most areas, future updates could
address specific user requests for customization and financial analysis tools, further enhancing the user
experience.

| 81 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
4.80
4.75
4.76
4.70 4.74
4.72
4.65 4.70
4.66
4.60 4.64
4.62
4.55 4.60 4.60 4.60 4.60
4.56 4.56
4.50 4.54 4.54
4.52
4.45
4.46 4.46
4.40
4.35
4.30
1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3
A
S U
A
S U
A
S U
S
S U
S
S U
S
S U
N
U
N
U
N
U
G
N
G
N
G
N
S
E D
S
E D
S
E D
IE
F
IE
F
IE
F
F F F E E E
Usability User Satisfaction Functionality Engagement Design Feedback for
Satisfaction Improvement
1 2 3 4 5 6
Figure 10. The average score for the evaluation aspect
4. DISCUSSION
This study developed and evaluated an Android-based personal finance management application to meet
young adults’ financial literacy and management needs. Through a focus on usability, engagement,
functionality, and user satisfaction, the results indicate that the application successfully addresses many
financial management challenges young adults encounter. The findings also suggest potential areas for
refinement that could further enhance the application’s effectiveness in promoting responsible financial
habits.
The study’s first objective was to assess how effectively the application improved users’ financial
management behaviors. With over 90% of users rating it at (4) four or above on the Likert scale, the
high usability ratings indicate that the application’s design was intuitive and accessible, even for those
with minimal experience in financial tracking. Usability is critical in fostering consistent usage, as
applications that are easy to navigate and visually appealing are more likely to be used regularly. The
positive user feedback on core features such as expense tracking and budget projections supports this,
suggesting that users found the application useful and practical for their daily financial activities.
Notably, features like income and expense tracking were highly rated in functionality and satisfaction,
underscoring their value in enhancing users’ awareness of their spending habits. Encouraging users to
categorize and analyze their expenses, the application promotes mindful spending, a behavior crucial
for long-term financial stability. However, while most users engaged consistently with these features,
some desired more personalized options, such as customized budget categories and detailed
expenditure analysis. These suggestions align with prior studies indicating that personalized financial
tools can improve engagement by making users feel more connected to their financial data [31], [32].
The second research question focused on whether regular engagement with the application could
enhance users’ financial literacy and contribute to long-term financial resilience. The engagement
scores indicate that the application succeeded in motivating users to track their finances consistently,
with a significant proportion of reporting plans to continue using the app. This regular interaction
| 82 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
reinforces positive financial habits and increases financial literacy by exposing users to daily spending
and saving decisions.
The findings suggest that the application’s design elements, such as progress bars for financial goals and
notification reminders, were important in maintaining user engagement. This aligns with behavior
change theory, which posits that timely reminders and visible progress indicators can reinforce positive
habits by making achievements tangible [33], [34]. Users specifically mentioned that the visual tracking
of financial goals motivated them to set and work toward achievable financial objectives, demonstrating
the application’s potential to foster a proactive approach to financial planning. While notifications were
generally well-received, some users expressed interest in more customizable reminder options, such
as setting personalized alert times. Incorporating such feedback could enhance user engagement by
providing a tailored experience that aligns with individual schedules, which has been shown to increase
the likelihood of habit formation in digital applications [35], [36], [37].
The study also sought to identify which features most effectively encouraged consistent financial
management behaviors. Based on user feedback, features such as income and expense tracking, budget
projections, and financial goal setting were the most impactful. These features align closely with the
primary behaviors associated with financial responsibility: tracking, planning, and setting achievable
financial targets. In particular, the financial goal-setting feature was instrumental in helping users focus
on saving for specific objectives. This functionality resonates with the concept of “goal-oriented
behavior,” which research indicates can lead to increased motivation and better long-term financial
outcomes [38], [39]. By enabling users to break down their financial goals into manageable steps, the
application helps build confidence and competence in managing money, which are critical to financial
resilience.
However, some users noted that while the budget projection feature was helpful, it could be further
improved by allowing for more nuanced budget categories. Additionally, users suggested incorporating
a more comprehensive financial report that could offer insights into spending trends over time. Such
enhancements would provide users with a deeper understanding of their financial patterns and help
them make more informed decisions, a need highlighted by various studies on digital finance tools [40],
[41], [42]. Integrating these improvements in future updates would likely enhance the application’s role
as an educational tool for financial literacy. This application’s success in engaging young adults
underscores the broader potential for mobile solutions to influence financial behavior. Digital platforms
are uniquely positioned to reach young users who are comfortable with technology but may lack
financial literacy. By offering an accessible and engaging tool, the application supports the development
of financial skills essential for navigating complex economic environments.
The findings suggest that, beyond practical utility, financial applications should emphasize
personalization and adaptability to cater to individual financial needs and schedules. As young adults
transition through various life stages, their financial priorities shift; thus, applications that adapt to these
changes can sustain users’ financial journeys. Moreover, this study highlights the importance of user-
centered design in financial applications, as it significantly impacts engagement and satisfaction. Future
research could explore the longitudinal impact of consistent app use on financial literacy, particularly
concerning debt reduction, savings growth, and investment behavior. While the study achieved its
objectives, it is important to recognize certain limitations. The relatively short evaluation period may
not fully capture the application’s impact on long-term financial habits. Additionally, while the sample
was representative of the target demographic, a more extensive and diverse user base would provide a
broader perspective on user needs and preferences. Future studies could include longitudinal research
to assess the sustained impact of the application on financial literacy and behavior change.
| 83 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Furthermore, implementing user feedback for added features, such as trend analysis and advanced
customization options, could enhance the application’s value. Expanding the application’s scope to
include educational content on financial literacy topics may also increase its impact by providing users
with practical tools and theoretical knowledge. Given the rapid evolution of financial technology,
integrating adaptive AI algorithms to offer personalized financial advice could be a promising future
direction.
5. CONCLUSION
This study successfully developed and evaluated an Android-based personal finance management
application specifically designed for young adults, focusing on usability, engagement, and functionality.
The application aimed to address its target audience’s specific financial management needs by providing
tools for tracking income and expense, budget projection, and setting financial goals. Through direct user
evaluations, the findings revealed high levels of user satisfaction across these core features, indicating that
the application effectively supports users in managing their finances and developing positive financial
habits. Key outcomes showed that the application’s user-friendly design, interactive features, and
reminder notifications were essential in encouraging consistent engagement with financial management.
Features such as financial goal tracking and budget projection fostered mindful spending and motivated
users to set and work toward achievable financial goals, an essential aspect of financial responsibility.
Despite these successes, feedback suggested room for improvement. Users expressed interest in
additional customization options, such as personalized budget categories and a more detailed analysis of
spending trends. Future updates could also incorporate AI-driven recommendations, offering users
personalized financial insights based on spending behavior, further enhancing the application's
functionality. Implementing these features could make the application even more responsive to individual
user needs and preferences. Overall, the application demonstrates significant potential to enhance
financial literacy and behavior among young adults. By offering an accessible, adaptable platform for
personal finance management, this application contributes significantly to efforts toward improving
financial resilience in the digital age. Future research could explore the long-term effects of regular app
usage on financial behavior, including savings growth, debt reduction, and investment practices.
DECLARATIONS
Author Contributions
Riswandha Imawan: Conceptualization, Methodology, Software, Data curation, Writing - Original
Draft. Wahyu Permana Putra: Visualization, Writing - Review & Editing. Rabee Alqahtani: Formal
analysis, Writing - Review & Editing. Emmanouil D. Milakis: Validation, Formal analysis, Writing -
Review & Editing. Mykhailo Dumchykov: Formal analysis, Writing - Review & Editing. All authors
have read and approved the final version of this manuscript.
Acknowledgments
The authors wish to express their gratitude to all individuals and organizations that contributed to the
successful development of this study. We sincerely thank the Faculty of Engineering at Universitas
Negeri Padang for their support and resources, which were essential in facilitating this research.
Additionally, we acknowledge the invaluable feedback provided by the 50 end-users who participated
in the testing phase; their insights have significantly contributed to refining the application to better
meet the needs of young adults in personal financial management. Finally, we thank our colleagues and
advisors whose guidance and expertise helped shape this study.
| 84 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Funding
The authors declare that this research received no external funding.
Competing Interests
The authors declare no competing interests.
Generative AI and AI-Assisted Technologies Statement
The author(s) declare that no generative AI or AI-assisted technologies were used to prepare this
manuscript. All content was created, reviewed, and edited manually by the author(s), who take full
responsibility for the accuracy and integrity of the manuscript.
REFERENCES
[1] T. Koskelainen, P. Kalmi, E. Scornavacca, and T. Vartiainen, “Financial literacy in the digital age—
A research agenda,” Journal of Consumer Affairs, vol. 57, no. 1, pp. 507–528, Jan. 2023, doi:
10.1111/JOCA.12510.
[2] P. K. Ozili, “Impact of digital finance on financial inclusion and stability,” Borsa Istanbul Review, vol.
18, no. 4, pp. 329–340, Dec. 2018, doi: 10.1016/J.BIR.2017.12.003.
[3] A. Lo Prete, “Digital and financial literacy as determinants of digital payments and personal
finance,” Econ Lett, vol. 213, p. 110378, Apr. 2022, doi: 10.1016/J.ECONLET.2022.110378.
[4] A. K. Khetan et al., “Variations in the financial impact of the COVID-19 pandemic across 5
continents: A cross-sectional, individual level analysis,” EClinicalMedicine, vol. 44, p. 101284, Feb.
2022, doi: 10.1016/J.ECLINM.2022.101284.
[5] M. Nicola et al., “The socio-economic implications of the coronavirus pandemic (COVID-19): A
review,” Int J Surg, vol. 78, p. 185, Jun. 2020, doi: 10.1016/J.IJSU.2020.04.018.
[6] A. Lusardi and F.-A. Messy, “The importance of financial literacy and its impact on financial
wellbeing,” Journal of Financial Literacy and Wellbeing, vol. 1, no. 1, pp. 1–11, Apr. 2023, doi:
10.1017/FLW.2023.8.
[7] J. Voßemer, M. Gebel, O. Nizalova, and O. Nikolaieva, “The effect of an early-career involuntary
job loss on later life health in Europe,” Adv Life Course Res, vol. 35, pp. 69–76, Mar. 2018, doi:
10.1016/J.ALCR.2018.01.001.
[8] A. Save, “Marketing in a mobile-first world: Tackling the why and the how,” Journal of Direct, Data
and Digital Marketing Practice, vol. 15, no. 3, pp. 202–212, Jan. 2014, doi:
10.1057/DDDMP.2014.8.
[9] M. Jones et al., “Beyond ‘yesterday’s tomorrow’: future-focused mobile interaction design by and
for emergent users,” Pers Ubiquitous Comput, vol. 21, no. 1, pp. 157–171, Feb. 2017, doi:
10.1007/S00779-016-0982-0.
[10] L. Stocchi, N. Pourazad, N. Michaelidou, A. Tanusondjaja, and P. Harrigan, “Marketing research
on Mobile apps: past, present and future,” J Acad Mark Sci, vol. 50, no. 2, pp. 195–225, Mar. 2022,
doi: 10.1007/S11747-021-00815-W.
[11] P. Bitrián, I. Buil, and S. Catalán, “Enhancing user engagement: The role of gamification in mobile
apps,” J Bus Res, vol. 132, pp. 170–185, Aug. 2021, doi: 10.1016/J.JBUSRES.2021.04.028.
[12] I. Y. Irma, E. sudrajat, N. A. Rachman, and B. Rifai, “The effect of financial literacy on online
| 85 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
loans and its impact on poverty,” International Journal of Applied Finance and Business Studies, vol. 11,
no. 2, pp. 146–154, Sep. 2023, doi: 10.35335/IJAFIBS.V11I2.109.
[13] W. Puspitasari, “The Effect of Online Loans on the Millennial Generation: A Systematic Literature
Review (SLR),” International Journal of Economics Development Research (IJEDR), vol. 5, no. 3, pp.
2426–2442, Sep. 2024, doi: 10.37385/IJEDR.V5I3.6047.
[14] K. Czech, L. Ochnio, M. Wielechowski, and S. Zabolotnyy, “Financial Literacy: Identification of
the Challenges, Needs, and Difficulties among Adults Living in Rural Areas,” Agriculture, vol. 14,
no. 10, p. 1705, Sep. 2024, doi: 10.3390/AGRICULTURE14101705.
[15] A. Lusardi, “Financial literacy and the need for financial education: evidence and implications,”
Swiss Journal of Economics and Statistics, vol. 155, no. 1, pp. 1–8, Jan. 2019, doi: 10.1186/S41937-
019-0027-5.
[16] V. Leone and P. Thompson, “Financial literacy and advice perceptions among UK higher education
students: an ethnicity tale?,” Rev Econ Househ, vol. 22, no. 2, pp. 709–781, Jun. 2024, doi:
10.1007/S11150-023-09667-5.
[17] H. Purnomo, M. Marsely, W. F. Lestari, O. Aryadewa, and F. Z. F. Oktavia, “Eksplorasi Aplikasi
Pencatatan Keuangan Pribadi Berbasis Android,” Seminar Nasional Gabungan Bidang Sosial - Polinema,
pp. 145–151, 2021.
[18] M. C. Mason, G. Zamparo, A. Marini, and N. Ameen, “Glued to your phone? Generation Z’s
smartphone addiction and online compulsive buying,” Comput Human Behav, vol. 136, p. 107404,
Nov. 2022, doi: 10.1016/J.CHB.2022.107404.
[19] J. C. Wang, C. Y. Hsieh, and S. H. Kung, “The impact of smartphone use on learning effectiveness:
A case study of primary school students,” Educ Inf Technol (Dordr), vol. 28, no. 6, pp. 6287–6320,
Jun. 2023, doi: 10.1007/S10639-022-11430-9.
[20] M. Bauer et al., “Smartphones in mental health: a critical review of background issues, current
status and future concerns,” International Journal of Bipolar Disorders, vol. 8, no. 1, pp. 1–19, Jan.
2020, doi: 10.1186/S40345-019-0164-X.
[21] K. Petersen, C. Wohlin, and D. Baca, “The Waterfall Model in Large-Scale Development,” Lecture
Notes in Business Information Processing, vol. 32, pp. 386–400, 2009, doi: 10.1007/978-3-642-
02152-7_29.
[22] S. Liu, “The Software Development Process,” Formal Engineering for Industrial Software Development,
pp. 235–260, 2004, doi: 10.1007/978-3-662-07287-5_14.
[23] K. Chari and M. Agrawal, “Impact of incorrect and new requirements on waterfall software project
outcomes,” Empir Softw Eng, vol. 23, no. 1, pp. 165–185, Feb. 2018, doi: 10.1007/S10664-017-
9506-4.
[24] M. Bolung and H. R. K. Tampangela, “Analisa Penggunaan Metodologi Pengembangan Perangkat
Lunak,” Jurnal ELTIKOM, vol. 1, no. 1, pp. 1–10, 2017, doi: 10.31961/eltikom.v1i1.1.
[25] N. Hidayati, “Penggunaan Metode Waterfall Dalam Rancang Bangun Sistem Informasi Penjualan,”
Generation Journal, vol. 3, no. 1, pp. 1–10, 2019.
[26] T. Yokoyama, H. B. Axelsen, and R. Glück, “Fundamentals of reversible flowchart languages,”
Theor Comput Sci, vol. 611, pp. 87–115, Jan. 2016, doi: 10.1016/J.TCS.2015.07.046.
[27] H. R. Hiremath and M. J. Skibniewski, “Object-oriented modeling of construction processes by
unified modeling language,” Autom Constr, vol. 13, no. 4, pp. 447–468, Jul. 2004, doi:
10.1016/J.AUTCON.2003.09.011.
[28] L. Hakim and M. S. Mardiyamto, “Relational Database Structure and Operations Engineering
| 86 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Using Class Diagram and Activity Diagram,” Jurnal Teknik Informatika, Sistem Infomasi dan Teknik
Industri, vol. 1, no. 1, pp. 109–113, 2018.
[29] A. Roman, “Black-Box Testing Techniques,” A Study Guide to the ISTQB® Foundation Level 2018
Syllabus, pp. 25–60, 2018, doi: 10.1007/978-3-319-98740-8_4.
[30] R. Fogler, I. Cohen, and D. Peled, “Accelerating Black Box Testing with Light-Weight Learning,”
Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes
in Bioinformatics), vol. 13872, pp. 103–120, 2023, doi: 10.1007/978-3-031-32157-3_6.
[31] I. H. Sarker, “Machine Learning: Algorithms, Real-World Applications and Research Directions,”
SN Comput Sci, vol. 2, no. 3, pp. 1–21, May 2021, doi: 10.1007/S42979-021-00592-X.
[32] A. S. Ferdous, H. S. Akareem, M. Viswanathan, L. D. Hollebeek, and A. Ringer, “Boosting app-
based mobile financial services engagement in B2B subsistence marketplaces: The roles of
marketing strategy and app design,” Industrial Marketing Management, vol. 119, pp. 147–161, May
2024, doi: 10.1016/J.INDMARMAN.2024.04.014.
[33] C. Zhang, D. Lakens, and W. A. I. Jsselsteijn, “Theory Integration for Lifestyle Behavior Change
in the Digital Age: An Adaptive Decision-Making Framework,” J Med Internet Res, vol. 23, no. 4,
p. e17127, Apr. 2021, doi: 10.2196/17127.
[34] R. Davis, R. Campbell, Z. Hildon, L. Hobbs, and S. Michie, “Theories of behaviour and behaviour
change across the social and behavioural sciences: a scoping review,” Health Psychol Rev, vol. 9, no.
3, p. 323, Aug. 2014, doi: 10.1080/17437199.2014.941722.
[35] K. Agrawal, S. Athey, A. Kanodia, and E. Palikot, “Digital interventions and habit formation in
educational technology,” Papers, 2024, Accessed: Nov. 07, 2024. [Online]. Available:
https://ideas.repec.org/p/arx/papers/2310.10850.html
[36] Y. Zhu, Y. Long, H. Wang, K. P. Lee, L. Zhang, and S. J. Wang, “Digital Behavior Change
Intervention Designs for Habit Formation: Systematic Review,” J Med Internet Res, vol. 26, no. 1,
p. e54375, May 2024, doi: 10.2196/54375.
[37] B. Gardner, A. L. Rebar, and P. Lally, “How does habit form? Guidelines for tracking real-world
habit formation,” Cogent Psychol, vol. 9, no. 1, Dec. 2022, doi: 10.1080/23311908.2022.2041277.
[38] B. Hommel, “GOALIATH: a theory of goal-directed behavior,” Psychol Res, vol. 86, no. 4, pp.
1054–1077, Jun. 2022, doi: 10.1007/S00426-021-01563-W.
[39] H. Wang, J. Yang, and P. Li, “How and when goal-oriented self-regulation improves college
students’ wellbeing: A weekly diary study,” Current Psychology, vol. 41, no. 11, pp. 7532–7543,
Nov. 2022, doi: 10.1007/S12144-020-01288-W.
[40] W. Dafri and R. Al-Qaruty, “Challenges and opportunities to enhance digital financial
transformation in crisis management,” Social Sciences & Humanities Open, vol. 8, no. 1, p. 100662,
Jan. 2023, doi: 10.1016/J.SSAHO.2023.100662.
[41] W. Xu, D. Hu, K. R. Lang, and J. L. Zhao, “Blockchain and digital finance,” Financial Innovation,
vol. 8, no. 1, pp. 1–4, Dec. 2022, doi: 10.1186/S40854-022-00420-Y.
[42] C. M. Malladi, R. K. Soni, and S. Srinivasan, “Digital financial inclusion: next frontiers—
challenges and opportunities,” CSI Transactions on ICT, vol. 9, no. 2, pp. 127–134, Aug. 2021, doi:
10.1007/S40012-021-00328-5.
| 87 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution, and reproduction in any medium or format, provided that appropriate credit is given to the original author(s) and
the source, a link to the Creative Commons license is provided, and any modifications are indicated. Unless otherwise specified in a credit line,
this article’s images or other third-party material are included under the Creative Commons license. If certain material is not covered by the
article’s Creative Commons license and its intended use is not permitted by statutory regulation or exceeds the allowed usage, permission must
be obtained directly from the copyright holder. http://creativecommons.org/licenses/by/4.0/.
AUTHOR BIOGRAPHIES
Riswandha Imawan holds a Bachelor’s in Informatics Engineering Education
from the Faculty of Engineering, Universitas Negeri Padang, Indonesia. His
primary areas of interest include networking systems and application development.
Riswandha has actively contributed to various software development and
networking projects, focusing on scalable and efficient technological solutions. His
current work centers on creating software that addresses specific challenges, aiming
to foster problem-solving through technological integration.
Wahyu Permana Putra holds a bachelor’s degree in informatics engineering
education from Universitas Negeri Padang and is preparing to complete a master’s
degree. As a practitioner, he focuses on software development and informatics
education, utilizing technology to improve educational methods. His recent
projects emphasize integrating advanced technology to foster a more efficient and
accessible learning environment.
Rabee Alqahtani, a distinguished academic at the University of Wollongong,
brings over 20 years of expertise in education with a focus on gifted education and
artificial intelligence. With an extensive publication record, his work primarily
addresses the needs of gifted learners and educational technology. His research
focuses on informatics education, vocational training, and technological innovation.
His contributions strive to cultivate a more adaptable and skilled workforce
prepared for the demands of a dynamic, tech-driven world.
Emmanouil D. Milakis is a Ph.D. candidate in Education Sciences at European
University Cyprus and a Special Education IT Instructor at the School of Vocational
Training for People with Disabilities of Athens. With extensive experience in
teaching IT across diverse vocational settings, his current research focuses on Gifted
STEAM education. His work aims to enhance cognitive development and social
inclusion for students with diverse needs, leveraging technology to create more
accessible, engaging, and effective educational experiences.
| 88 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)

Journal of Hypermedia & Technology-Enhanced Learning
Vol. 3, No. 1, February (2025), Pages 64–89 | e-ISSN: 2985–9166
Mykhailo Dumchykov is a lecturer at Sumy State University, Ukraine. He has
over six years of experience in vocational education and specializes in cybercrime.
He has published extensively in the fields of information crime and cybercrime. His
current research is focused on crime in the digital environment. Mykhailo
Dumchykov’s research contributions aim to develop methodologies for combating
crime in cyberspace, drawing on the experience of leading nations worldwide.
Publisher’s and Journal’s Note Sagamedia Teknologi Nusantara, as the publisher and editor of the Journal of Hypermedia &
Technology-Enhanced Learning (J-HyTEL), upholds the highest ethical standards in academic publishing. The journal remains neutral with
regard to jurisdictional claims in published maps and institutional affiliations. Authors are fully responsible for the originality, accuracy, and
integrity of their work. Post-publication ethical concerns will be addressed through corrections, clarifications, or retractions as necessary. The
content of this publication has not been approved by the United Nations and does not reflect the views of the United Nations or its officials or
Member States. https://www.un.org/sustainabledevelopment
| 89 | https://doi.org/10.58536/j-hytel.166
Enhancing Financial Literacy in Young Adults: An Android-Based Personal … (Riswandha Imawan et al., 2025)