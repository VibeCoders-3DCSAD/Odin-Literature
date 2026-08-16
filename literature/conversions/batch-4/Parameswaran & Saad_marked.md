---
conversion_metadata:
  converted_at: "2026-07-21T08:05:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Parameswaran & Saad.pdf"
  source_pdf_sha256: "b514ea887ee9ba0cea5677e3bd76c6bdfab507dc419a03ebc4c293720c36f252"
  page_count: 19
  markdown_char_count: 86836
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

JOURNAL OF DIGITAL SYSTEM DEVELOPMENT

https://e-journal.uum.edu.my/index.php/jdsd

How to cite this article: 
Parameswaran, S., & Sharhida Zawani Saad (2025). Development and Evaluation of My Money Manager: An Intelligent Mobile 
App for Personalized Financial Insight. Journal of Digital System Development, 3 (2), 123-141. 
https://doi.org/10.32890/jdsd2025.3.2.9

DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN 
INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT

1Sharwin Parameswaran & 2Sharhida Zawani Saad 
1&2School of Computing, Universiti Utara Malaysia, Malaysia

2Corresponding author: sharhida@uum.edu.my

Received: 20/8/2025

Revised: 15/9/2025

Accepted: 24/10/2025

Published: 30/10/2025

ABSTRACT

Personal  finance  management  has  become  increasingly  critical  in  today's  digital  economy,  yet  existing 
mobile  applications  often  lack  the  intelligence  to  provide  personalised  financial  guidance.  This  article 
presents  the  development  of  "My  Money  Manager  Mobile  App,"  an  Android-based  personal  finance 
management  system  that  addresses  current  limitations  through  intelligent  expense  categorisation  and 
personalised financial insights. The application distinguishes between fixed and variable expenses using 
algorithmic analysis and provides tailored savings recommendations based on user spending patterns over 
90  days.  Unlike  existing  solutions  that  offer  generic  financial  advice,  this  system  analyses  individual 
spending  behaviour  to  detect  anomalies  and  provide  dynamic,  evolving  financial  guidance.  The  app 
employs an iterative and incremental development methodology, ensuring continuous improvement based 
on user feedback. Key features include automated expense categorisation, visual representation of financial 
flows, balance tracking, and personalised savings advice. The system addresses significant gaps in current 
personal  finance  applications  by  providing  intelligent  analysis  rather  than  simple  expense  tracking, 
ultimately empowering users to make more informed financial decisions and develop healthier spending 
habits. A usability evaluation involving 35 participants was conducted. The results demonstrate that 71.4% 
of respondents agreed that the financial insights helped guide their financial decision-making. In terms of 
personal finance habits, 74.3% of users reported that the app encouraged them to manage their finances 
more  effectively,  pointing  to  the  usefulness  of  budget  planning  and  savings  recommendations.  The 
strongest validation was observed in income and expense tracking, where 82.8% of respondents confirmed 
that the feature was efficient and reliable in monitoring their daily financial activities.

Keywords:  Expense  categorisation,  financial  behaviour,  financial  literacy,  financial  visualisation, 
spending pattern analysis.

123

---

<!-- PAGE 2 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

INTRODUCTION

In  today's  rapidly  evolving  digital  economy,  effective  personal  finance  management  has  emerged  as  a 
fundamental life skill. The proliferation of mobile technology has created unprecedented opportunities to 
develop sophisticated yet accessible financial management solutions that seamlessly integrate into users' 
daily lives. Mobile financial management applications have become essential tools for promoting financial 
inclusion and literacy, offering users convenient methods to handle their money effectively.

However, despite the growing number of personal finance applications, many fail to meet the sophisticated 
needs  of  modern  users.  Most  existing  applications  treat  financial  management  as  a  one-size-fits-all 
approach, offering generic advice that fails to account for individual spending patterns, financial goals, or 
unique  circumstances.  This  approach  often  results  in  recommendations  that  may  be  irrelevant  or 
counterproductive to users' actual financial situations.

Current  personal  finance  management  applications  present  several  critical  limitations.  Most  existing 
applications lack the intelligence necessary to analyse spending patterns comprehensively or provide truly 
personalised  recommendations.  A  significant  shortcoming  is  the  failure  to  differentiate  between  fixed, 
essential costs, such as rent and loan payments, and variable, discretionary expenses, such as entertainment 
or dining out (Shaikh et al., 2022).

Furthermore,  current  applications  rarely  account  for  abnormal  spending  behaviours,  typically  offering 
static, one-size-fits-all financial recommendations that fail to adapt to changing circumstances (Mijić & 
Ćebić, 2023). Users require more sophisticated systems capable of intelligently recognising patterns and 
providing dynamic insights on effective financial habit adjustment.

LITERATURE REVIEW

The  rise  of  mobile  financial  technologies  has  had  a  profound  impact  on  how  individuals  manage  their 
finances.  These  mobile  apps  now  provide  users  with  instant  access  to  a  range  of  financial  tools,  from 
budgeting and expense monitoring to more advanced financial planning, making it easier for users to make 
better-informed financial decisions. This literature review highlights key research across several areas: the 
influence of mobile financial services on financial behaviour, theoretical models of user acceptance and 
technology adoption, and the features of personal finance apps currently available. Additionally, the review 
explores the role of regional and cultural factors, particularly in Malaysia, in shaping adoption trends, and 
provides a comparative  evaluation  of  leading applications available today. Together, these studies shed 
light  on  the  evolving  landscape  of  mobile  finance  management  and  offer  valuable  insights  for  future 
innovation and user-focused design.

Extensive research has focused on the role of mobile apps in influencing financial decision-making. Carlin 
et  al.  (2022)  found  that  mobile  applications,  by  reducing  barriers  to  accessing  personal  financial  data, 
significantly improved user behaviour, resulting in fewer overdraft fees and better financial management. 
This underscores how mobile apps, by providing real-time financial insights, can empower users to make 
more informed and practical financial choices.

Shaikh et al. (2022) conducted an in-depth review of mobile financial services and identified key drivers 
of adoption, including perceived utility, ease of use, and trustworthiness. Their framework offers essential 
guidance for developing mobile apps that are both user-friendly and tailored to meet the needs of everyday 
consumers.

124

---

<!-- PAGE 3 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

The acceptance of mobile personal finance apps has been analysed through various theoretical lenses. Mijić 
and Ćebić (2023) utilised the UTAUT2 model to identify crucial factors influencing adoption, including 
performance expectancy, effort expectancy, and social influence. These factors are essential for designing 
apps that meet user expectations, fostering higher satisfaction and greater engagement.

Torno  et  al.  (2021)  developed  a  detailed  classification  system  for  mobile  finance  apps,  grouping  them 
based  on  core  functionalities  such  as  budgeting,  expense  tracking,  and  investment  management.  This 
categorisation offers a valuable framework for understanding existing app features and identifying gaps 
that could be addressed in future developments.

Leading applications in the market include YNAB, which stands out for its rules-based budgeting system 
and PocketGuard, which simplifies budget management by automatically categorising recurring expenses 
and  distinguishing  between  fixed  and  variable  costs  (Forbes  Advisor,  2024).  However,  both  apps  face 
challenges such as steep learning curves or reliance on precise categorisation to function optimally.

In addressing the research  gaps  identified  in previous work, the My Money Manager Mobile  App goes 
beyond  basic  expense  tracking  by  offering  personalised  financial  insights  and  detecting  spending 
anomalies based on users’ financial activities and behaviours. This results in generic recommendations for 
reducing  the  likelihood  of  overspending,  debt  accumulation,  and  financial  stress.  Unlike  traditional 
methods and previous approaches to supporting technology adoption, categorisation, and feature analysis, 
the app fills a critical gap for individuals who need comprehensive yet simple financial management tools, 
automating financial analysis and providing insightful visualisations. It is also worth noting that the 90-
day  analysis  feature  provides  actionable  insights  to  optimise  future  spending  and  savings  strategies, 
supporting long-term financial decisions.

PROJECT SIGNIFICANCE

The My Money Manager Mobile App represents a meaningful contribution to the field of digital personal 
finance  tools  by  addressing  key  limitations  in  existing  solutions.  The  application  introduces  advanced, 
user-friendly features that promote informed financial decision-making, financial literacy, and long-term 
planning across four key areas:

The  application  provides  intelligent  financial  analysis  beyond  basic  expense  tracking,  differentiating 
between fixed and variable expenses, detecting spending anomalies, and offering personalised, evolving 
financial insights. This represents a substantial advancement over existing solutions that provide generic 
recommendations.

The  application  significantly  impacts  financial  literacy  by  making  sophisticated  financial  analysis 
accessible to a broad user base. By providing clear, actionable advice and real-time updates, it reduces the 
likelihood of overspending, debt accumulation, and financial stress.

In an increasingly  digital financial  landscape, the application fills a critical gap for individuals needing 
comprehensive yet simple financial management tools. Unlike traditional methods, it automates financial 
analysis and provides insightful visualisations.

The  application's  ability  to  review  financial  trends  over  time  supports  strategic  long-term  financial 
planning. The 90-day analysis feature provides actionable insights to optimise future spending and savings 
strategies.

125

---

<!-- PAGE 4 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

METHODOLOGY

This research employed an iterative and incremental development methodology, following the principles 
of  agile  software  development.  The  methodology  was  selected  for  its  proven  effectiveness  in  mobile 
application development projects, as demonstrated by Abrahamsson  et al. (2017), and for  its alignment 
with user-centred design principles advocated by Norman (2013).

Figure 1

Iterative and Incremental Approach Methodology

The  iterative  and  incremental  approach  ensures  continuous  improvement  through  user  feedback 
integration,  risk  mitigation  through  early  testing,  and  adaptive  development  that  responds  to  changing 
requirements. This methodology is particularly suitable for mobile applications where user experience and 
functionality must be refined through multiple iterations based on real-world usage patterns.

Development Approach 
The  methodology  incorporates  cycles  of  planning,  design,  development,  testing,  and  deployment,  with 
each  cycle  building  upon  previous  stages  to  refine  features,  address  challenges,  and  prioritise 
improvements.  This  approach  follows  the  principles  of  agile  development  and  has  been  successfully 
applied in mobile application development contexts (Abrahamsson et al., 2017).

Phase 1: Initiation and Research 
Comprehensive understanding of user needs through market research, user persona creation, and user story 
development. This phase  employed  user-centred design principles as advocated by Norman (2013) and 
utilised  market  research  methodologies  described  by  Kotler  and  Keller  (2016).  Deliverables  include 
research findings, user personas, and prioritised feature lists based on real-world needs.

Phase 2: Planning and Roadmap Development 
Clear objective establishment, timeline definition, and resource allocation following project management 
best practices outlined by PMI (2017). Detailed roadmap creation with key  milestones, feature backlog 
prioritisation, and sprint planning for meaningful updates, utilising agile planning techniques.

126

---

<!-- PAGE 5 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Phase 3: Design and Prototyping 
Translation  of  conceptual  ideas  into  tangible  interfaces  using  design  thinking  methodology.  UI/UX 
wireframe  development,  user  flow  diagrams,  interactive  prototype  creation,  and  backend  architecture 
planning  with  secure  data  storage  solutions. This  phase  incorporated  mobile-first  design  principles  and 
responsive design methodologies.

Phase 4: Development Iterations 
Iterative sprints focusing on specific feature sets, following Scrum methodology principles (Schwaber & 
Sutherland,  2020).  Initial  development  of  core  features  followed  by  complex  functionalities,  backend 
development  for  data  storage  and  security,  and  visual  component  implementation  using  Android 
development best practices (Meier, 2018).

Phase 5: Testing and Quality Assurance 
Comprehensive testing for reliability and user experience, and incorporating testing methodologies. Unit 
and integration testing, usability testing with user groups following Nielsen's principles (Nielsen, 2012), 
performance testing across devices, and systematic user feedback collection.

Phase 6: Deployment and Maintenance 
Public availability through QR Code that links to Google Drive .apk file, post-launch monitoring through 
analytics,  user  feedback  collection  systems,  and  comprehensive  documentation  following  software 
deployment best practices.

DESIGN AND DEVELOPMENT

The design and development phase focused on creating an intuitive, user-friendly interface that addresses 
the  identified  gaps  in  existing  personal  finance  management  applications.  The  application  architecture 
follows the Model-View-Controller (MVC) pattern, ensuring separation of concerns and maintainability.

User Interface Design 
The user interface design prioritises simplicity, clarity, and efficiency, following material design principles 
for Android applications (Google, 2021). The interface components are organised into distinct functional 
areas, each serving specific user needs and workflows.

127

---

<!-- PAGE 6 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Figure 2

Home Screen / Dashboard Interface

The Home Screen or Dashboard Interface (Figure 2) serves as the central hub of the application, providing 
users with immediate access to their financial overview. The interface features a clean, minimalist design 
with key financial metrics prominently displayed at the top, including current balance, monthly income, 
and expenses. Quick action buttons enable rapid access to core functions such as adding income, recording 
expenses, and setting budgets. The recent transactions section provides a chronological view of the latest 
financial activities, enabling users to review their spending patterns quickly.

Figure 3

Add Income / Expenses Interface

The  Add  Income  and  Add  Expense  Interfaces  (Figure  3)  are  designed  for  efficient  data  entry  with 
streamlined forms featuring intuitive field layouts. Each interface includes an amount input with numerical 
keypad  optimisation,  category  selection  with  predefined  options  and  custom  category  creation,  date

128

---

<!-- PAGE 7 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

selection with calendar integration, and optional note fields for additional context. The forms incorporate 
real-time validation to ensure data accuracy and provide immediate feedback to users as they enter data.

Figure 4

Budget Planning Interface

The Monthly Budget Interface (Figure 4) provides comprehensive budget management capabilities through 
visual progress indicators for each spending category. Users can set spending limits for different categories, 
view  real-time  budget  utilisation  via  colour-coded  progress  bars,  and  receive  alerts  when  approaching 
budget limits. The interface includes  comparative analysis features that show budget performance  over 
time and provide recommendations for budget adjustments based on spending patterns.

Figure 5

Financial Summary Interface

129

---

<!-- PAGE 8 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

The Financial Summary Interface (Figure 5) provides a clear, organised overview of income, expenses, 
and budget entries, organised into three tabs for easy navigation. Each entry is displayed in card format, 
with  key  details  such  as  amount,  category,  payment  method,  and  date,  along  with  icons  for  editing  or 
deleting. Users can sort entries by month, year, or both, with customizable filter options. A detailed pop-
up shows complete transaction information and any attached images. This interface provides users with an 
intuitive and efficient way to manage and review their financial data.

Figure 6

Financial Insights Interface

The  Financial  Insights  Interface  (Figure  6)  transforms  raw  financial  data  into  actionable  intelligence 
through  interactive  charts  and  graphs.  The  screen  features  spending  pattern  analysis  with  categorical 
breakdowns, trend analysis showing spending patterns over time, anomaly detection highlighting unusual 
spending  behaviours,  and  personalised  recommendations  based  on  individual  financial  patterns.  The 
visualisation components utilise responsive design principles to ensure optimal viewing across different 
device sizes.

Financial Insights Calculation 
The  Financial  Insights  Interface  implements  several  key  calculations  to  provide  users  with  meaningful 
financial analysis. All calculations are performed  monthly, with data filtered by the selected month and 
year via the interactive calendar component.

130

---

<!-- PAGE 9 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Core Financial Metrics 
The application calculates five primary financial metrics for the selected month:

Monthly Income Calculation:

Monthly Income = Σ(all income entries for selected month)                                    (1)

Monthly Expenses Calculation:

Monthly Expenses = Σ(all expense entries for selected month)                                (2)

Monthly Savings Calculation:

Monthly Savings = Monthly Income - Monthly Expenses                                          (3)

Income/Expense Ratio Calculation:

Income/Expense Ratio = Monthly Income ÷ Monthly Expenses                             (4)

Budget Status Calculation:

Budget Status = Monthly Budget - Monthly Expenses                                              (5)

Expense Distribution Analysis 
The pie chart visualisation displays expense distribution by category for the selected month:

Category Expense Calculation:

Category Expense = Σ(all expenses for specific category in selected month)       (6)

Category Percentage Calculation:

Category Percentage = (Category Expense ÷ Monthly Expenses) × 100              (7)

The interactive calendar component allows users to navigate between different months and years, with all 
calculations automatically updating based on the selected time period. Users can navigate using the arrow 
keys to select adjacent months or select specific months and years directly in the calendar interface. This 
dynamic  approach  ensures  that  financial  insights  remain  contextually  relevant  to  the  user's  selected 
timeframe, enabling comprehensive month-by-month financial analysis.

RESULTS

This section presents the key findings from the user evaluation of My Money Manager, focusing on four 
main  dimensions:  App  Experience,  Perceived  Ease  of  Use,  Perceived  Usefulness,  and  Perceived 
Acceptance. Data was collected using Likert-scale questionnaires from participants who tested the app's 
core  features  and  interface.  The  aim  was  to  understand  how  users  perceive  the  application's  design, 
functionality, and impact on their financial management routines.

Data  collection  involved  35  participants  interacting  with  the  My  Money  Manager  application  and 
subsequently completing questionnaires that measured their experience across multiple dimensions. The 
evaluation  utilised  a  structured  approach  with  standardised  response  options  ranging  from  "Strongly 
Disagree" to "Strongly Agree" on a six-point Likert scale. This methodology enabled quantitative analysis 
of  user  perceptions  while  providing  insights  into  specific  areas  of  strength  and  opportunities  for 
enhancement.

131

---

<!-- PAGE 10 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Figure 7

What Do You Think About the App Experience?

Figure 7 is based on the question that explores users' first impressions and general experience with the app, 
focusing on interface design, usability, and confidence during use. Most participants responded positively 
to the visual appeal, with many selecting Strongly Agree or Somewhat Agree, indicating that the design is 
well  received.  Likewise,  most  users  found  the  app  user-friendly,  with  straightforward  navigation  and  a 
cohesive interface. The icons and buttons were also rated as intuitive, although a small portion of users felt 
certain symbols could be improved for clarity. However, the ability to complete tasks without help showed 
a more mixed response. While many felt confident, a noticeable portion needed assistance, suggesting a 
need for improved onboarding or help features. Overall, users expressed confidence while using the app, 
though a few indicated uncertainty in specific parts of the interface.

Figure 8

Perceived Ease of Use

Figure 8 is based on the question that assesses how easy it was for users to perform key tasks within the 
app, such as navigation, adding transactions, editing  entries, and understanding financial insights. Most 
users  reported  that  navigating  the  home  screen  and  dashboard  was  Very  Easy  or  Easy,  reflecting  an

132

---

<!-- PAGE 11 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

intuitive  layout. Adding income  or expense  entries also scored highly in  ease  of use, affirming that the 
form  design and category selection process  were user-friendly. Setting a  monthly budget  was similarly 
straightforward for most users, though a few suggested minor improvements to guide users through this 
feature.  Editing  or  deleting  entries  was  generally  manageable,  though  responses  indicated  that  better 
visibility  or  interaction  design  could  further  streamline  the  process.  The  most  variation  appeared  in 
responses to viewing and interpreting financial insights. While many found it easy, some users struggled 
to understand charts and data, suggesting a need for clearer visualisations or explanatory features. Table 1 
summarises the collected responses focusing on Perceived Ease of Use.

Table 1

Responses on Perceived Ease of Use

Statement

Options

Percentage (%)

How easy was it to navigate the home page or the 
dashboard?

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

How easy was it to add an income/expense entry?  Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

How easy was it to set your monthly budget?

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

133

77.1

20.0

2.9

0.0

0.0

0.0

77.1

20.0

2.9

0.0

0.0

0.0

77.1

20.0

2.9

0.0

0.0

0.0

---

<!-- PAGE 12 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

How easy was it to edit/delete an entry?

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

How easy was it to view and understand the 
financial insights?

Figure 9

Perceived Usefulness

60.0

31.4

8.6

0.0

0.0

0.0

37.1

28.6

20.0

14.3

0.0

0.0

Figure 9 illustrates how respondents evaluated the usefulness of the My Money Manager application in 
supporting their financial activities. The results highlight three main features: financial insights, improved 
personal  finance  habits,  and  income  and  expense  tracking.  Most  respondents  (37.1%  strongly  agreed, 
34.3% agreed) indicated that the financial insights helped guide their financial decision-making. However, 
28.6%  marked  'somewhat  agree,'  suggesting  that  the  clarity  or  depth  of  the  charts  and  data  could  be

134

---

<!-- PAGE 13 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

improved.  In  terms  of  personal  finance  habits,  74.3%  of  users  (28.6%  strongly  agreed,  45.7%  agreed) 
reported that the app encouraged them to manage their finances more effectively, pointing to the usefulness 
of budget planning and savings recommendations. The strongest validation was observed in income and 
expense tracking, where 82.8% of respondents (45.7% strongly agreed, 37.1% agreed) confirmed that the 
feature was efficient and reliable in monitoring their daily financial activities. Collectively, these findings 
show that while tracking and habit-building functions were highly valued, financial insights received more 
mixed responses, highlighting an important area for future refinement. Table 2 summarises the collected 
responses focusing on Perceived Usefulness.

Table 2

Responses on Perceived Usefulness

Statement

Options

Percentage (%)

The app helps in managing my income and 
expenses more effectively.

The app improves the way I handle my personal 
finances.

The app provides valuable financial insights that 
help in making better financial decisions.

I can easily track my income and expenses using 
this app.

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

Strongly Agree

Agree

135

31.4

48.6

20.0

0.0

0.0

0.0

28.6

45.7

25.7

0.0

0.0

0.0

37.1

34.3

28.6

0.0

0.0

0.0

45.7

37.1

---

<!-- PAGE 14 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

Strongly Agree

Agree

Somewhat Agree

Somewhat Disagree

Disagree

Strongly Disagree

14.3

2.9

0.0

0.0

37.1

37.1

25.7

0.0

0.0

0.0

The app helps reduce the time I spend managing 
financial matters.

Figure 10

Perceived Acceptance

Figure 10 is based on a question that assesses broader sentiments regarding satisfaction, trust, and the app’s 
perceived reliability. Most users expressed satisfaction with the overall experience and acknowledged the 
app as a valuable personal finance tool. However, responses regarding trust in accuracy and data security 
were more varied. While a majority trusted the app’s tracking capabilities, some expressed mild concern, 
suggesting  that  features  such  as  verification,  data  logs,  or  better  feedback  mechanisms  could  enhance 
transparency. Similarly, although many users believed their financial data was secure, a significant portion 
selected  Somewhat  Agree  or  Somewhat  Disagree,  highlighting  security  as  a  potential  area  for 
improvement. Lastly, the app was generally seen as reliable for planning and tracking finances, though 
strengthening certain features and reinforcing stability could increase user confidence in long-term usage.

136

---

<!-- PAGE 15 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

These results collectively provide a clear picture of My Money Manager’s current performance and user 
perception.  While  overall  feedback  is  encouraging,  particularly  in  areas  like  usability,  tracking,  and 
satisfaction,  the  results  also  reveal  actionable  insights  for  refining  the  user  interface  and  onboarding 
experience, as well as enhancing trust-related aspects such as data security and the clarity of insights.

App Experience

KEY FINDINGS

Referring to Figure 7, the evaluation of overall app experience revealed generally positive responses across 
several interface and usability measures. Visual appeal stood out as a strong point, with 16 users (45.7%) 
strongly agreeing,  6 (17.1%) agreeing, and 11 (31.4%) somewhat agreeing that the layout was visually 
attractive. Only two users (5.7%) marked 'disagree,' suggesting that while many respondents appreciated 
the design, a considerable group found the appearance less appealing, indicating a degree of polarisation 
in design preferences.

User-friendliness received strong support: 19 users (54.3%) strongly agreed and 11 users (31.4%) agreed 
that the app was easy to use, while five users marked somewhat agree, for a 100% positive response rate 
overall.  This  confirms  that  the  navigation,  layout,  and  overall  interface  flow  were  intuitive  to  most 
participants. The clarity  of  icons and buttons also showed favourable  outcomes,  with 15 users (42.9%) 
strongly  agreeing  and  10  users  (28.6%)  agreeing  that  these  interface  elements  were  straightforward  to 
understand.

The most mixed responses were related to task completion independence. Only five users (14.3%) strongly 
agreed that they could complete tasks without help; 4 users agreed; 15 users (42.9%) marked somewhat 
agree;  and  10  users  marked  somewhat  disagree.  Only  one  user  marked  disagree  on  task  completion 
independence. This pattern indicates that while most users could eventually complete tasks, a substantial 
number required guidance, pointing to possible gaps in onboarding or contextual support.

User  confidence  in  using  the  application  was  moderate  to  strong.  A  total  of  10  users  (28.6%)  strongly 
agreed, 13 users (37.1%) agreed, and 11 users (31.4%) marked somewhat agree that they felt confident 
using the app. Only one user disagreed on this. These results suggest that although many respondents felt 
assured in navigating and interacting with the app, further improvements to interface clarity and in-app 
guidance could help build greater confidence across all users.

Perceived Ease of Use

Referring  to  Figure  8,  the  ease-of-use  evaluation  demonstrated  exceptional  performance  across  core 
functionalities. Navigation of the home page and dashboard received outstanding ratings: 26 users (74.3%) 
strongly  agreed,  eight  users  (22.9%)  agreed,  and  one  user  marked  it  somewhat  easy.  This  outcome 
demonstrated 100% positive responses on the navigation ease. This indicates highly successful information 
architecture and navigation design.

Similarly, adding income and expense entries received identical positive ratings: 27 users (77.1%) marked 
strongly agree, and seven users (20%) agreed. In contrast, one user marked somewhat agree, confirming 
that the data entry process is intuitive and efficient. The budget-setting feature also received the same high

137

---

<!-- PAGE 16 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

ratings:  27  users  (77.1%)  marked  strongly  agree,  7  (20%)  agreed,  and  one  marked  somewhat  agree, 
suggesting consistent design quality across core financial management functions.

Editing and deleting entries showed slightly lower but still strong performance: 21 users (60%) strongly 
agreed and 11 users (31.4%) agreed that performing edits and updates were easy, with three users marking 
them somewhat easy, for a 100% positive response rate. While still highly positive, this slight decrease 
suggests minor friction in the editing workflow that could be refined.

The most significant variation  occurred in viewing and understanding financial insights, where 13 users 
(37.1%) strongly agreed it was easy, 10 users (28.6%) agreed, and seven users (20%) marked somewhat 
agree. That said, five users (14.3%) found it somewhat challenging. This represents the lowest performance 
in the ease-of-use category, indicating that data visualisation and insight presentation require enhancement 
to improve insight clarity.

Perceived Usefulness

Referring to Figure 9, the usefulness evaluation revealed strong validation of the application’s core value 
proposition. Management  of income and  expenses received robust endorsement, with 11 users (31.4%) 
strongly  agreeing,  17  users  (48.6%)  agreeing,  and  seven  users  (20%)  somewhat  agreeing  that  the  app 
helped manage finances more effectively, for a 100% positive response rate.

Personal  finance  habit  improvement  showed  similarly  strong  results,  with  10  users  (28.6%)  strongly 
agreeing, 16 users (45.7%) agreeing. Nine users (25.7%) marked 'somewhat agree' that the app improved 
their  financial  management  approach,  resulting  in  a  100%  positive  response,  indicating  a  meaningful 
perceived impact on user behaviour and financial practices.

Financial insights' usefulness received positive but more varied responses, with 13 users (37.1%) strongly 
agreeing, 12 users (34.3%) agreeing, and 10 users (28.6%) marking somewhat agree that insights were 
helpful in decision-making, suggesting that while insights are generally valued, their presentation or depth 
could be enhanced to maximise utility.

Income and expense tracking capability received the highest ratings in this category, with 16 users (45.7%) 
strongly agreeing, 13 users (37.1%) agreeing, and five users (14.3%) somewhat agreeing that it was easy 
to track finances. Time savings in financial management showed strong results: 13 users (37.1%) strongly 
agreed, 13 (37.1%) agreed, and 9 (25.7%) somewhat agreed that the app reduced time spent on financial 
tasks, yielding 100% positive responses on that aspect.

Perceived Acceptance

Referring  to  Figure  10,  the  acceptance  evaluation  revealed  mixed  results  with  both  strengths  and  areas 
requiring attention. Overall satisfaction was high, with 14 users (40%) strongly agreeing, 16 users (45.7%) 
agreeing, and five users (14.3%) somewhat agreeing that they were satisfied with the experience, resulting 
in 100% positive responses and indicating a successful overall user experience.

Users strongly validated the application’s value proposition, with 11 users (31.4%) strongly agreeing, 14 
users  (40%)  agreeing,  and  10  users  (28.6%)  marking  somewhat  agree  that  it  was  a  valuable  personal 
financial tool, resulting in a 100% positive response that confirms market fit and user-need fulfilment.

138

---

<!-- PAGE 17 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

However, trust in accuracy revealed more concerning patterns: 8 users (22.9%) strongly agreed, 11 users 
(31.4%)  agreed,  and  14  users  (40%)  somewhat  agreed  that  they  trusted  the  app’s  accuracy  in  tracking 
financial  data.  Having  said  that,  two  users  (5.7%)  marked  'somewhat  disagree'  on  this  aspect.  This 
distribution suggests moderate confidence levels that could benefit from enhanced security or verification 
features.

The most significant concern emerged in perceptions of data security. Only four users (11.4%) strongly 
agreed, 3 (8.6%) agreed, and 17 (48.6%) somewhat agreed that their financial data was safe and secure. 
However,  11  users  (31.4%)  marked  'somewhat  disagree,'  indicating  a  critical  area  requiring  immediate 
attention through enhanced security features, clearer privacy policies, or improved communication about 
data protection measures. Reliability for financial planning and tracking showed satisfactory results, with 
eight  users  (22.9%)  strongly  agreeing,  15  users  (42.9%)  agreeing,  and  11  users  (31.4%)  somewhat 
agreeing, for a 99.97% positive response rate.

DISCUSSION AND IMPLICATIONS

The evaluation results paint a picture of an application with strong foundational capabilities but specific 
areas  requiring  improvement.  The  exceptionally  positive  responses  to  ease  of  use  for  core  functions 
(navigation,  data  entry,  budget  setting)  demonstrate  successful  user  experience  design  for  primary 
workflows. However, the mixed results in task completion independence and the challenges with financial 
insight comprehension suggest opportunities for enhanced user guidance and data visualisation.

The  strong  results  of  the  usefulness  dimension  validate  the  application's  market  fit  and  core  value 
proposition. Users clearly perceive benefits in financial management efficiency and habit improvement. 
However, the moderate responses to insight usefulness indicate potential for enhanced analytical features 
or improved presentation of financial intelligence.

The  acceptance  dimension  reveals  the  most  critical  areas  for  improvement.  While  satisfaction  and 
perceived value are intense, the concerning results for data security confidence and moderate trust levels 
represent significant barriers to long-term adoption and user retention. These findings suggest prioritising 
security  communication,  implementing  additional  verification  features,  and  enhancing  transparency 
around data handling practices.

Based on these findings, several strategic improvements are recommended:

1.  Enhanced  Onboarding:  Address

the

task  completion

independence  concerns

through

comprehensive onboarding tutorials and contextual help features.

2.  Improved  Data  Visualisation:  Redesign  the  financial  insights  presentation  to  enhance  user

comprehension and utility.

3.  Security Communication: Implement clearer security messaging, privacy policy accessibility, and

potentially additional verification features to build user confidence.

4.  Trust Building Features: Consider implementing data logs, verification mechanisms, or feedback

systems to enhance transparency and trust.

5.  Consistency Optimisation: While core functions perform well, ensure consistent design quality

across all features, particularly in editing workflows.

139

---

<!-- PAGE 18 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

CONCLUSION

The  My  Money  Manager  Mobile  App  marks  a  notable  leap  forward  in  personal  finance  management 
technology,  filling  crucial  gaps  in  existing  tools  with  its  intelligent  expense  categorisation  and  tailored 
financial  insights.  By  distinguishing  between  fixed  and  variable  costs,  identifying  unusual  spending 
patterns, and providing ongoing financial advice, the app enables users to make more strategic, adaptable 
financial decisions.

Through its iterative, user-centred development process, the app has the potential to improve in response 
to user input and evolving needs continuously. Its mobile-first design ensures that even complex financial 
analysis is easily accessible to a wide range of users. With the potential to enhance financial literacy, foster 
long-term  financial  planning,  and  encourage  healthier  financial  habits,  the  app  stands  as  a  powerful 
resource  for  individuals  aiming  to  take  control  of  their  financial  lives.  The  impact  of  this  project  goes 
beyond  individual  use,  contributing  to  broader  goals  of  financial  inclusion  and  education,  while  also 
pushing the boundaries of  mobile finance  management technology. As it continues to  evolve  with user 
feedback and technological advances, the app has the potential to redefine the standards for innovative, 
personalised financial management tools.

The  evaluation  demonstrates a solid foundation  with strong performance  in core functionality and user 
satisfaction. The application successfully delivers on its primary value proposition: simplifying financial 
management and improving users' financial habits. However, the results also highlight  some limitations 
and  potential  improvements  in  specific  areas,  particularly  in  user  guidance,  insight  presentation,  and 
security confidence, which require attention to optimise the user experience and drive long-term adoption. 
As discussed in the previous section, these findings provide a clear roadmap for prioritising development 
efforts to enhance the application's overall effectiveness and user acceptance.

REFERENCES

Abrahamsson,  P.,  Salo,  O.,  Ronkainen,  J.,  &  Warsta,  J.  (2017).  Agile  software  development  methods:

Review and analysis. VTT Publications.

A  complete  guide  to  iterative  and  incremental  development  |  Relia  Software.  (2024,  July  1).

https://reliasoftware.com/blog/iterative-and-incremental-development

Carlin,  B.,  Olafsson,  A.,  &  Pagel,  M.  (2022).  Mobile  apps  and  financial  decision  making.  Review  of

Finance, 27(3), 977–996. https://doi.org/10.1093/rof/rfac040

Forbes  Advisor.

1). 
https://www.forbes.com/advisor/banking/pocketguard-budgeting-app-review/

PocketGuard  Budgeting  App  Review

(2024,  August

2024.

García,  M.  B.  (2021).  Mobile  Bookkeeper:  Personal  Financial  Management  Application  with  Receipt 
Scanner Using Optical Character Recognition. The First Conference on Online Teaching for Mobile 
Education (OT4ME). https://doi.org/10.1109/ot4me53559.2021.9638794

Google. (2021). Material Design Guidelines. Google Inc.

Kotler, P., & Keller, K. L. (2016). Marketing management (15th ed.). Pearson.

140

---

<!-- PAGE 19 -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

Meier, R. (2018). Professional Android (4th ed.). Wrox Press.

Mijić,  M.,  &  Ćebić,  B.  (2023).  Mobile  Applications  for  Personal  Finance  Management:  Technology 
273–295.

Perspective.  Contributions

Accounting,

Finance

and

to

Acceptance 
https://doi.org/10.1007/978-3-031-23269-5_16

Nielsen, J. (2012). Usability engineering. Morgan Kaufmann.

Norman, D. (2013). The design of everyday things: Revised and expanded edition. Basic Books.

PMI. (2017).  A guide to the project management body of knowledge (PMBOK guide) (6th ed.). Project

Management Institute.

Schwaber, K., & Sutherland, J. (2020). The Scrum guide: The definitive guide to scrum. Scrum.org.

Shaikh,  A.  A.,  Alamoudi,  H.,  Alharthi,  M.,  &  Glavee-Geo,  R.  (2022).  Advances  in  mobile  financial 
services:  a  review  of  the  literature  and  future  research  directions.  International  Journal  of  Bank 
Marketing, 41(1). https://doi.org/10.1108/ijbm-06-2021-0230

Torno, A., Werth, O., Nickerson, R. C., Breitner, M. H., & Muntermann, J. (2021). More than Mobile 
Banking  –  A  Taxonomy-based  Analysis  of  Mobile  Personal  Finance  Applications.  Twenty-Fifth 
Pacific Asia Conference on Information Systems (PACIS).

141

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
JOURNAL OF DIGITAL SYSTEM DEVELOPMENT
https://e-journal.uum.edu.my/index.php/jdsd
How to cite this article:
Parameswaran, S., & Sharhida Zawani Saad (2025). Development and Evaluation of My Money Manager: An Intelligent Mobile
App for Personalized Financial Insight. Journal of Digital System Development, 3 (2), 123-141.
https://doi.org/10.32890/jdsd2025.3.2.9
DEVELOPMENT AND EVALUATION OF MY MONEY MANAGER: AN
INTELLIGENT MOBILE APP FOR PERSONALIZED FINANCIAL INSIGHT
1Sharwin Parameswaran & 2Sharhida Zawani Saad
1&2School of Computing, Universiti Utara Malaysia, Malaysia
2Corresponding author: sharhida@uum.edu.my
Received: 20/8/2025 Revised: 15/9/2025 Accepted: 24/10/2025 Published: 30/10/2025
ABSTRACT
Personal finance management has become increasingly critical in today's digital economy, yet existing
mobile applications often lack the intelligence to provide personalised financial guidance. This article
presents the development of "My Money Manager Mobile App," an Android-based personal finance
management system that addresses current limitations through intelligent expense categorisation and
personalised financial insights. The application distinguishes between fixed and variable expenses using
algorithmic analysis and provides tailored savings recommendations based on user spending patterns over
90 days. Unlike existing solutions that offer generic financial advice, this system analyses individual
spending behaviour to detect anomalies and provide dynamic, evolving financial guidance. The app
employs an iterative and incremental development methodology, ensuring continuous improvement based
on user feedback. Key features include automated expense categorisation, visual representation of financial
flows, balance tracking, and personalised savings advice. The system addresses significant gaps in current
personal finance applications by providing intelligent analysis rather than simple expense tracking,
ultimately empowering users to make more informed financial decisions and develop healthier spending
habits. A usability evaluation involving 35 participants was conducted. The results demonstrate that 71.4%
of respondents agreed that the financial insights helped guide their financial decision-making. In terms of
personal finance habits, 74.3% of users reported that the app encouraged them to manage their finances
more effectively, pointing to the usefulness of budget planning and savings recommendations. The
strongest validation was observed in income and expense tracking, where 82.8% of respondents confirmed
that the feature was efficient and reliable in monitoring their daily financial activities.
Keywords: Expense categorisation, financial behaviour, financial literacy, financial visualisation,
spending pattern analysis.
123

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
INTRODUCTION
In today's rapidly evolving digital economy, effective personal finance management has emerged as a
fundamental life skill. The proliferation of mobile technology has created unprecedented opportunities to
develop sophisticated yet accessible financial management solutions that seamlessly integrate into users'
daily lives. Mobile financial management applications have become essential tools for promoting financial
inclusion and literacy, offering users convenient methods to handle their money effectively.
However, despite the growing number of personal finance applications, many fail to meet the sophisticated
needs of modern users. Most existing applications treat financial management as a one-size-fits-all
approach, offering generic advice that fails to account for individual spending patterns, financial goals, or
unique circumstances. This approach often results in recommendations that may be irrelevant or
counterproductive to users' actual financial situations.
Current personal finance management applications present several critical limitations. Most existing
applications lack the intelligence necessary to analyse spending patterns comprehensively or provide truly
personalised recommendations. A significant shortcoming is the failure to differentiate between fixed,
essential costs, such as rent and loan payments, and variable, discretionary expenses, such as entertainment
or dining out (Shaikh et al., 2022).
Furthermore, current applications rarely account for abnormal spending behaviours, typically offering
static, one-size-fits-all financial recommendations that fail to adapt to changing circumstances (Mijić &
Ćebić, 2023). Users require more sophisticated systems capable of intelligently recognising patterns and
providing dynamic insights on effective financial habit adjustment.
LITERATURE REVIEW
The rise of mobile financial technologies has had a profound impact on how individuals manage their
finances. These mobile apps now provide users with instant access to a range of financial tools, from
budgeting and expense monitoring to more advanced financial planning, making it easier for users to make
better-informed financial decisions. This literature review highlights key research across several areas: the
influence of mobile financial services on financial behaviour, theoretical models of user acceptance and
technology adoption, and the features of personal finance apps currently available. Additionally, the review
explores the role of regional and cultural factors, particularly in Malaysia, in shaping adoption trends, and
provides a comparative evaluation of leading applications available today. Together, these studies shed
light on the evolving landscape of mobile finance management and offer valuable insights for future
innovation and user-focused design.
Extensive research has focused on the role of mobile apps in influencing financial decision-making. Carlin
et al. (2022) found that mobile applications, by reducing barriers to accessing personal financial data,
significantly improved user behaviour, resulting in fewer overdraft fees and better financial management.
This underscores how mobile apps, by providing real-time financial insights, can empower users to make
more informed and practical financial choices.
Shaikh et al. (2022) conducted an in-depth review of mobile financial services and identified key drivers
of adoption, including perceived utility, ease of use, and trustworthiness. Their framework offers essential
guidance for developing mobile apps that are both user-friendly and tailored to meet the needs of everyday
consumers.
124

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
The acceptance of mobile personal finance apps has been analysed through various theoretical lenses. Mijić
and Ćebić (2023) utilised the UTAUT2 model to identify crucial factors influencing adoption, including
performance expectancy, effort expectancy, and social influence. These factors are essential for designing
apps that meet user expectations, fostering higher satisfaction and greater engagement.
Torno et al. (2021) developed a detailed classification system for mobile finance apps, grouping them
based on core functionalities such as budgeting, expense tracking, and investment management. This
categorisation offers a valuable framework for understanding existing app features and identifying gaps
that could be addressed in future developments.
Leading applications in the market include YNAB, which stands out for its rules-based budgeting system
and PocketGuard, which simplifies budget management by automatically categorising recurring expenses
and distinguishing between fixed and variable costs (Forbes Advisor, 2024). However, both apps face
challenges such as steep learning curves or reliance on precise categorisation to function optimally.
In addressing the research gaps identified in previous work, the My Money Manager Mobile App goes
beyond basic expense tracking by offering personalised financial insights and detecting spending
anomalies based on users’ financial activities and behaviours. This results in generic recommendations for
reducing the likelihood of overspending, debt accumulation, and financial stress. Unlike traditional
methods and previous approaches to supporting technology adoption, categorisation, and feature analysis,
the app fills a critical gap for individuals who need comprehensive yet simple financial management tools,
automating financial analysis and providing insightful visualisations. It is also worth noting that the 90-
day analysis feature provides actionable insights to optimise future spending and savings strategies,
supporting long-term financial decisions.
PROJECT SIGNIFICANCE
The My Money Manager Mobile App represents a meaningful contribution to the field of digital personal
finance tools by addressing key limitations in existing solutions. The application introduces advanced,
user-friendly features that promote informed financial decision-making, financial literacy, and long-term
planning across four key areas:
The application provides intelligent financial analysis beyond basic expense tracking, differentiating
between fixed and variable expenses, detecting spending anomalies, and offering personalised, evolving
financial insights. This represents a substantial advancement over existing solutions that provide generic
recommendations.
The application significantly impacts financial literacy by making sophisticated financial analysis
accessible to a broad user base. By providing clear, actionable advice and real-time updates, it reduces the
likelihood of overspending, debt accumulation, and financial stress.
In an increasingly digital financial landscape, the application fills a critical gap for individuals needing
comprehensive yet simple financial management tools. Unlike traditional methods, it automates financial
analysis and provides insightful visualisations.
The application's ability to review financial trends over time supports strategic long-term financial
planning. The 90-day analysis feature provides actionable insights to optimise future spending and savings
strategies.
125

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
METHODOLOGY
This research employed an iterative and incremental development methodology, following the principles
of agile software development. The methodology was selected for its proven effectiveness in mobile
application development projects, as demonstrated by Abrahamsson et al. (2017), and for its alignment
with user-centred design principles advocated by Norman (2013).
Figure 1
Iterative and Incremental Approach Methodology
The iterative and incremental approach ensures continuous improvement through user feedback
integration, risk mitigation through early testing, and adaptive development that responds to changing
requirements. This methodology is particularly suitable for mobile applications where user experience and
functionality must be refined through multiple iterations based on real-world usage patterns.
Development Approach
The methodology incorporates cycles of planning, design, development, testing, and deployment, with
each cycle building upon previous stages to refine features, address challenges, and prioritise
improvements. This approach follows the principles of agile development and has been successfully
applied in mobile application development contexts (Abrahamsson et al., 2017).
Phase 1: Initiation and Research
Comprehensive understanding of user needs through market research, user persona creation, and user story
development. This phase employed user-centred design principles as advocated by Norman (2013) and
utilised market research methodologies described by Kotler and Keller (2016). Deliverables include
research findings, user personas, and prioritised feature lists based on real-world needs.
Phase 2: Planning and Roadmap Development
Clear objective establishment, timeline definition, and resource allocation following project management
best practices outlined by PMI (2017). Detailed roadmap creation with key milestones, feature backlog
prioritisation, and sprint planning for meaningful updates, utilising agile planning techniques.
126

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
Phase 3: Design and Prototyping
Translation of conceptual ideas into tangible interfaces using design thinking methodology. UI/UX
wireframe development, user flow diagrams, interactive prototype creation, and backend architecture
planning with secure data storage solutions. This phase incorporated mobile-first design principles and
responsive design methodologies.
Phase 4: Development Iterations
Iterative sprints focusing on specific feature sets, following Scrum methodology principles (Schwaber &
Sutherland, 2020). Initial development of core features followed by complex functionalities, backend
development for data storage and security, and visual component implementation using Android
development best practices (Meier, 2018).
Phase 5: Testing and Quality Assurance
Comprehensive testing for reliability and user experience, and incorporating testing methodologies. Unit
and integration testing, usability testing with user groups following Nielsen's principles (Nielsen, 2012),
performance testing across devices, and systematic user feedback collection.
Phase 6: Deployment and Maintenance
Public availability through QR Code that links to Google Drive .apk file, post-launch monitoring through
analytics, user feedback collection systems, and comprehensive documentation following software
deployment best practices.
DESIGN AND DEVELOPMENT
The design and development phase focused on creating an intuitive, user-friendly interface that addresses
the identified gaps in existing personal finance management applications. The application architecture
follows the Model-View-Controller (MVC) pattern, ensuring separation of concerns and maintainability.
User Interface Design
The user interface design prioritises simplicity, clarity, and efficiency, following material design principles
for Android applications (Google, 2021). The interface components are organised into distinct functional
areas, each serving specific user needs and workflows.
127

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
Figure 2
Home Screen / Dashboard Interface
The Home Screen or Dashboard Interface (Figure 2) serves as the central hub of the application, providing
users with immediate access to their financial overview. The interface features a clean, minimalist design
with key financial metrics prominently displayed at the top, including current balance, monthly income,
and expenses. Quick action buttons enable rapid access to core functions such as adding income, recording
expenses, and setting budgets. The recent transactions section provides a chronological view of the latest
financial activities, enabling users to review their spending patterns quickly.
Figure 3
Add Income / Expenses Interface
The Add Income and Add Expense Interfaces (Figure 3) are designed for efficient data entry with
streamlined forms featuring intuitive field layouts. Each interface includes an amount input with numerical
keypad optimisation, category selection with predefined options and custom category creation, date
128

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
selection with calendar integration, and optional note fields for additional context. The forms incorporate
real-time validation to ensure data accuracy and provide immediate feedback to users as they enter data.
Figure 4
Budget Planning Interface
The Monthly Budget Interface (Figure 4) provides comprehensive budget management capabilities through
visual progress indicators for each spending category. Users can set spending limits for different categories,
view real-time budget utilisation via colour-coded progress bars, and receive alerts when approaching
budget limits. The interface includes comparative analysis features that show budget performance over
time and provide recommendations for budget adjustments based on spending patterns.
Figure 5
Financial Summary Interface
129

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
The Financial Summary Interface (Figure 5) provides a clear, organised overview of income, expenses,
and budget entries, organised into three tabs for easy navigation. Each entry is displayed in card format,
with key details such as amount, category, payment method, and date, along with icons for editing or
deleting. Users can sort entries by month, year, or both, with customizable filter options. A detailed pop-
up shows complete transaction information and any attached images. This interface provides users with an
intuitive and efficient way to manage and review their financial data.
Figure 6
Financial Insights Interface
The Financial Insights Interface (Figure 6) transforms raw financial data into actionable intelligence
through interactive charts and graphs. The screen features spending pattern analysis with categorical
breakdowns, trend analysis showing spending patterns over time, anomaly detection highlighting unusual
spending behaviours, and personalised recommendations based on individual financial patterns. The
visualisation components utilise responsive design principles to ensure optimal viewing across different
device sizes.
Financial Insights Calculation
The Financial Insights Interface implements several key calculations to provide users with meaningful
financial analysis. All calculations are performed monthly, with data filtered by the selected month and
year via the interactive calendar component.
130

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
Core Financial Metrics
The application calculates five primary financial metrics for the selected month:
Monthly Income Calculation:
Monthly Income = Σ(all income entries for selected month) (1)
Monthly Expenses Calculation:
Monthly Expenses = Σ(all expense entries for selected month) (2)
Monthly Savings Calculation:
Monthly Savings = Monthly Income - Monthly Expenses (3)
Income/Expense Ratio Calculation:
Income/Expense Ratio = Monthly Income ÷ Monthly Expenses (4)
Budget Status Calculation:
Budget Status = Monthly Budget - Monthly Expenses (5)
Expense Distribution Analysis
The pie chart visualisation displays expense distribution by category for the selected month:
Category Expense Calculation:
Category Expense = Σ(all expenses for specific category in selected month) (6)
Category Percentage Calculation:
Category Percentage = (Category Expense ÷ Monthly Expenses) × 100 (7)
The interactive calendar component allows users to navigate between different months and years, with all
calculations automatically updating based on the selected time period. Users can navigate using the arrow
keys to select adjacent months or select specific months and years directly in the calendar interface. This
dynamic approach ensures that financial insights remain contextually relevant to the user's selected
timeframe, enabling comprehensive month-by-month financial analysis.
RESULTS
This section presents the key findings from the user evaluation of My Money Manager, focusing on four
main dimensions: App Experience, Perceived Ease of Use, Perceived Usefulness, and Perceived
Acceptance. Data was collected using Likert-scale questionnaires from participants who tested the app's
core features and interface. The aim was to understand how users perceive the application's design,
functionality, and impact on their financial management routines.
Data collection involved 35 participants interacting with the My Money Manager application and
subsequently completing questionnaires that measured their experience across multiple dimensions. The
evaluation utilised a structured approach with standardised response options ranging from "Strongly
Disagree" to "Strongly Agree" on a six-point Likert scale. This methodology enabled quantitative analysis
of user perceptions while providing insights into specific areas of strength and opportunities for
enhancement.
131

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
Figure 7
What Do You Think About the App Experience?
Figure 7 is based on the question that explores users' first impressions and general experience with the app,
focusing on interface design, usability, and confidence during use. Most participants responded positively
to the visual appeal, with many selecting Strongly Agree or Somewhat Agree, indicating that the design is
well received. Likewise, most users found the app user-friendly, with straightforward navigation and a
cohesive interface. The icons and buttons were also rated as intuitive, although a small portion of users felt
certain symbols could be improved for clarity. However, the ability to complete tasks without help showed
a more mixed response. While many felt confident, a noticeable portion needed assistance, suggesting a
need for improved onboarding or help features. Overall, users expressed confidence while using the app,
though a few indicated uncertainty in specific parts of the interface.
Figure 8
Perceived Ease of Use
Figure 8 is based on the question that assesses how easy it was for users to perform key tasks within the
app, such as navigation, adding transactions, editing entries, and understanding financial insights. Most
users reported that navigating the home screen and dashboard was Very Easy or Easy, reflecting an
132

 Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

intuitive layout. Adding income or expense entries also scored highly in ease of use, affirming that the
form design and category selection process were user-friendly. Setting a monthly budget was similarly
straightforward for most users, though a few suggested minor improvements to guide users through this
feature. Editing or deleting entries was generally manageable, though responses indicated that better
visibility or interaction design could further streamline the process. The most variation appeared in
responses to viewing and interpreting financial insights. While many found it easy, some users struggled
to understand charts and data, suggesting a need for clearer visualisations or explanatory features. Table 1
summarises the collected responses focusing on Perceived Ease of Use.

Table 1

Responses on Perceived Ease of Use

| Statement  | Options  | Percentage (%)  |
| ---------- | -------- | --------------- |
How easy was it to navigate the home page or the  Strongly Agree  77.1
dashboard?
|     | Agree              | 20.0  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 2.9   |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
How easy was it to add an income/expense entry?  Strongly Agree  77.1
|     | Agree              | 20.0  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 2.9   |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
How easy was it to set your monthly budget?  Strongly Agree  77.1
|     | Agree              | 20.0  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 2.9   |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
133

 Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

How easy was it to edit/delete an entry?  Strongly Agree  60.0
|     | Agree              | 31.4  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 8.6   |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
How easy was it to view and understand the  Strongly Agree  37.1
financial insights?
|     | Agree              | 28.6  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 20.0  |
|     | Somewhat Disagree  | 14.3  |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
|     |                    |       |
Figure 9

Perceived Usefulness

Figure 9 illustrates how respondents evaluated the usefulness of the My Money Manager application in
supporting their financial activities. The results highlight three main features: financial insights, improved
personal finance habits, and income and expense tracking. Most respondents (37.1% strongly agreed,
34.3% agreed) indicated that the financial insights helped guide their financial decision-making. However,
28.6% marked 'somewhat agree,' suggesting that the clarity or depth of the charts and data could be
134

 Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

improved. In terms of personal finance habits, 74.3% of users (28.6% strongly agreed, 45.7% agreed)
reported that the app encouraged them to manage their finances more effectively, pointing to the usefulness
of budget planning and savings recommendations. The strongest validation was observed in income and
expense tracking, where 82.8% of respondents (45.7% strongly agreed, 37.1% agreed) confirmed that the
feature was efficient and reliable in monitoring their daily financial activities. Collectively, these findings
show that while tracking and habit-building functions were highly valued, financial insights received more
mixed responses, highlighting an important area for future refinement. Table 2 summarises the collected
responses focusing on Perceived Usefulness.

Table 2

Responses on Perceived Usefulness
| Statement  | Options  | Percentage (%)  |
| ---------- | -------- | --------------- |
The app helps in managing my income and  Strongly Agree  31.4
expenses more effectively.
|     | Agree              | 48.6  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 20.0  |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
The app improves the way I handle my personal  Strongly Agree  28.6
finances.
|     | Agree              | 45.7  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 25.7  |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
The app provides valuable financial insights that  Strongly Agree  37.1
help in making better financial decisions.
|     | Agree              | 34.3  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 28.6  |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
I can easily track my income and expenses using  Strongly Agree  45.7
this app.
|     | Agree  | 37.1  |
| --- | ------ | ----- |
135

 Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141

|     | Somewhat Agree     | 14.3  |
| --- | ------------------ | ----- |
|     | Somewhat Disagree  | 2.9   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |
The app helps reduce the time I spend managing  Strongly Agree  37.1
financial matters.
|     | Agree              | 37.1  |
| --- | ------------------ | ----- |
|     | Somewhat Agree     | 25.7  |
|     | Somewhat Disagree  | 0.0   |
|     | Disagree           | 0.0   |
|     | Strongly Disagree  | 0.0   |

|     |     |     |
| --- | --- | --- |
Figure 10

Perceived Acceptance

Figure 10 is based on a question that assesses broader sentiments regarding satisfaction, trust, and the app’s
perceived reliability. Most users expressed satisfaction with the overall experience and acknowledged the
app as a valuable personal finance tool. However, responses regarding trust in accuracy and data security
were more varied. While a majority trusted the app’s tracking capabilities, some expressed mild concern,
suggesting that features such as verification, data logs, or better feedback mechanisms could enhance
transparency. Similarly, although many users believed their financial data was secure, a significant portion
selected  Somewhat  Agree  or  Somewhat  Disagree,  highlighting  security  as  a  potential  area  for
improvement. Lastly, the app was generally seen as reliable for planning and tracking finances, though
strengthening certain features and reinforcing stability could increase user confidence in long-term usage.
136

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
These results collectively provide a clear picture of My Money Manager’s current performance and user
perception. While overall feedback is encouraging, particularly in areas like usability, tracking, and
satisfaction, the results also reveal actionable insights for refining the user interface and onboarding
experience, as well as enhancing trust-related aspects such as data security and the clarity of insights.
KEY FINDINGS
App Experience
Referring to Figure 7, the evaluation of overall app experience revealed generally positive responses across
several interface and usability measures. Visual appeal stood out as a strong point, with 16 users (45.7%)
strongly agreeing, 6 (17.1%) agreeing, and 11 (31.4%) somewhat agreeing that the layout was visually
attractive. Only two users (5.7%) marked 'disagree,' suggesting that while many respondents appreciated
the design, a considerable group found the appearance less appealing, indicating a degree of polarisation
in design preferences.
User-friendliness received strong support: 19 users (54.3%) strongly agreed and 11 users (31.4%) agreed
that the app was easy to use, while five users marked somewhat agree, for a 100% positive response rate
overall. This confirms that the navigation, layout, and overall interface flow were intuitive to most
participants. The clarity of icons and buttons also showed favourable outcomes, with 15 users (42.9%)
strongly agreeing and 10 users (28.6%) agreeing that these interface elements were straightforward to
understand.
The most mixed responses were related to task completion independence. Only five users (14.3%) strongly
agreed that they could complete tasks without help; 4 users agreed; 15 users (42.9%) marked somewhat
agree; and 10 users marked somewhat disagree. Only one user marked disagree on task completion
independence. This pattern indicates that while most users could eventually complete tasks, a substantial
number required guidance, pointing to possible gaps in onboarding or contextual support.
User confidence in using the application was moderate to strong. A total of 10 users (28.6%) strongly
agreed, 13 users (37.1%) agreed, and 11 users (31.4%) marked somewhat agree that they felt confident
using the app. Only one user disagreed on this. These results suggest that although many respondents felt
assured in navigating and interacting with the app, further improvements to interface clarity and in-app
guidance could help build greater confidence across all users.
Perceived Ease of Use
Referring to Figure 8, the ease-of-use evaluation demonstrated exceptional performance across core
functionalities. Navigation of the home page and dashboard received outstanding ratings: 26 users (74.3%)
strongly agreed, eight users (22.9%) agreed, and one user marked it somewhat easy. This outcome
demonstrated 100% positive responses on the navigation ease. This indicates highly successful information
architecture and navigation design.
Similarly, adding income and expense entries received identical positive ratings: 27 users (77.1%) marked
strongly agree, and seven users (20%) agreed. In contrast, one user marked somewhat agree, confirming
that the data entry process is intuitive and efficient. The budget-setting feature also received the same high
137

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
ratings: 27 users (77.1%) marked strongly agree, 7 (20%) agreed, and one marked somewhat agree,
suggesting consistent design quality across core financial management functions.
Editing and deleting entries showed slightly lower but still strong performance: 21 users (60%) strongly
agreed and 11 users (31.4%) agreed that performing edits and updates were easy, with three users marking
them somewhat easy, for a 100% positive response rate. While still highly positive, this slight decrease
suggests minor friction in the editing workflow that could be refined.
The most significant variation occurred in viewing and understanding financial insights, where 13 users
(37.1%) strongly agreed it was easy, 10 users (28.6%) agreed, and seven users (20%) marked somewhat
agree. That said, five users (14.3%) found it somewhat challenging. This represents the lowest performance
in the ease-of-use category, indicating that data visualisation and insight presentation require enhancement
to improve insight clarity.
Perceived Usefulness
Referring to Figure 9, the usefulness evaluation revealed strong validation of the application’s core value
proposition. Management of income and expenses received robust endorsement, with 11 users (31.4%)
strongly agreeing, 17 users (48.6%) agreeing, and seven users (20%) somewhat agreeing that the app
helped manage finances more effectively, for a 100% positive response rate.
Personal finance habit improvement showed similarly strong results, with 10 users (28.6%) strongly
agreeing, 16 users (45.7%) agreeing. Nine users (25.7%) marked 'somewhat agree' that the app improved
their financial management approach, resulting in a 100% positive response, indicating a meaningful
perceived impact on user behaviour and financial practices.
Financial insights' usefulness received positive but more varied responses, with 13 users (37.1%) strongly
agreeing, 12 users (34.3%) agreeing, and 10 users (28.6%) marking somewhat agree that insights were
helpful in decision-making, suggesting that while insights are generally valued, their presentation or depth
could be enhanced to maximise utility.
Income and expense tracking capability received the highest ratings in this category, with 16 users (45.7%)
strongly agreeing, 13 users (37.1%) agreeing, and five users (14.3%) somewhat agreeing that it was easy
to track finances. Time savings in financial management showed strong results: 13 users (37.1%) strongly
agreed, 13 (37.1%) agreed, and 9 (25.7%) somewhat agreed that the app reduced time spent on financial
tasks, yielding 100% positive responses on that aspect.
Perceived Acceptance
Referring to Figure 10, the acceptance evaluation revealed mixed results with both strengths and areas
requiring attention. Overall satisfaction was high, with 14 users (40%) strongly agreeing, 16 users (45.7%)
agreeing, and five users (14.3%) somewhat agreeing that they were satisfied with the experience, resulting
in 100% positive responses and indicating a successful overall user experience.
Users strongly validated the application’s value proposition, with 11 users (31.4%) strongly agreeing, 14
users (40%) agreeing, and 10 users (28.6%) marking somewhat agree that it was a valuable personal
financial tool, resulting in a 100% positive response that confirms market fit and user-need fulfilment.
138

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
However, trust in accuracy revealed more concerning patterns: 8 users (22.9%) strongly agreed, 11 users
(31.4%) agreed, and 14 users (40%) somewhat agreed that they trusted the app’s accuracy in tracking
financial data. Having said that, two users (5.7%) marked 'somewhat disagree' on this aspect. This
distribution suggests moderate confidence levels that could benefit from enhanced security or verification
features.
The most significant concern emerged in perceptions of data security. Only four users (11.4%) strongly
agreed, 3 (8.6%) agreed, and 17 (48.6%) somewhat agreed that their financial data was safe and secure.
However, 11 users (31.4%) marked 'somewhat disagree,' indicating a critical area requiring immediate
attention through enhanced security features, clearer privacy policies, or improved communication about
data protection measures. Reliability for financial planning and tracking showed satisfactory results, with
eight users (22.9%) strongly agreeing, 15 users (42.9%) agreeing, and 11 users (31.4%) somewhat
agreeing, for a 99.97% positive response rate.
DISCUSSION AND IMPLICATIONS
The evaluation results paint a picture of an application with strong foundational capabilities but specific
areas requiring improvement. The exceptionally positive responses to ease of use for core functions
(navigation, data entry, budget setting) demonstrate successful user experience design for primary
workflows. However, the mixed results in task completion independence and the challenges with financial
insight comprehension suggest opportunities for enhanced user guidance and data visualisation.
The strong results of the usefulness dimension validate the application's market fit and core value
proposition. Users clearly perceive benefits in financial management efficiency and habit improvement.
However, the moderate responses to insight usefulness indicate potential for enhanced analytical features
or improved presentation of financial intelligence.
The acceptance dimension reveals the most critical areas for improvement. While satisfaction and
perceived value are intense, the concerning results for data security confidence and moderate trust levels
represent significant barriers to long-term adoption and user retention. These findings suggest prioritising
security communication, implementing additional verification features, and enhancing transparency
around data handling practices.
Based on these findings, several strategic improvements are recommended:
1. Enhanced Onboarding: Address the task completion independence concerns through
comprehensive onboarding tutorials and contextual help features.
2. Improved Data Visualisation: Redesign the financial insights presentation to enhance user
comprehension and utility.
3. Security Communication: Implement clearer security messaging, privacy policy accessibility, and
potentially additional verification features to build user confidence.
4. Trust Building Features: Consider implementing data logs, verification mechanisms, or feedback
systems to enhance transparency and trust.
5. Consistency Optimisation: While core functions perform well, ensure consistent design quality
across all features, particularly in editing workflows.
139

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
CONCLUSION
The My Money Manager Mobile App marks a notable leap forward in personal finance management
technology, filling crucial gaps in existing tools with its intelligent expense categorisation and tailored
financial insights. By distinguishing between fixed and variable costs, identifying unusual spending
patterns, and providing ongoing financial advice, the app enables users to make more strategic, adaptable
financial decisions.
Through its iterative, user-centred development process, the app has the potential to improve in response
to user input and evolving needs continuously. Its mobile-first design ensures that even complex financial
analysis is easily accessible to a wide range of users. With the potential to enhance financial literacy, foster
long-term financial planning, and encourage healthier financial habits, the app stands as a powerful
resource for individuals aiming to take control of their financial lives. The impact of this project goes
beyond individual use, contributing to broader goals of financial inclusion and education, while also
pushing the boundaries of mobile finance management technology. As it continues to evolve with user
feedback and technological advances, the app has the potential to redefine the standards for innovative,
personalised financial management tools.
The evaluation demonstrates a solid foundation with strong performance in core functionality and user
satisfaction. The application successfully delivers on its primary value proposition: simplifying financial
management and improving users' financial habits. However, the results also highlight some limitations
and potential improvements in specific areas, particularly in user guidance, insight presentation, and
security confidence, which require attention to optimise the user experience and drive long-term adoption.
As discussed in the previous section, these findings provide a clear roadmap for prioritising development
efforts to enhance the application's overall effectiveness and user acceptance.
REFERENCES
Abrahamsson, P., Salo, O., Ronkainen, J., & Warsta, J. (2017). Agile software development methods:
Review and analysis. VTT Publications.
A complete guide to iterative and incremental development | Relia Software. (2024, July 1).
https://reliasoftware.com/blog/iterative-and-incremental-development
Carlin, B., Olafsson, A., & Pagel, M. (2022). Mobile apps and financial decision making. Review of
Finance, 27(3), 977–996. https://doi.org/10.1093/rof/rfac040
Forbes Advisor. (2024, August 1). PocketGuard Budgeting App Review 2024.
https://www.forbes.com/advisor/banking/pocketguard-budgeting-app-review/
García, M. B. (2021). Mobile Bookkeeper: Personal Financial Management Application with Receipt
Scanner Using Optical Character Recognition. The First Conference on Online Teaching for Mobile
Education (OT4ME). https://doi.org/10.1109/ot4me53559.2021.9638794
Google. (2021). Material Design Guidelines. Google Inc.
Kotler, P., & Keller, K. L. (2016). Marketing management (15th ed.). Pearson.
140

Journal of Digital System Development: Vol. 3. No. 2 (October) 2025: 123-141
Meier, R. (2018). Professional Android (4th ed.). Wrox Press.
Mijić, M., & Ćebić, B. (2023). Mobile Applications for Personal Finance Management: Technology
Acceptance Perspective. Contributions to Finance and Accounting, 273–295.
https://doi.org/10.1007/978-3-031-23269-5_16
Nielsen, J. (2012). Usability engineering. Morgan Kaufmann.
Norman, D. (2013). The design of everyday things: Revised and expanded edition. Basic Books.
PMI. (2017). A guide to the project management body of knowledge (PMBOK guide) (6th ed.). Project
Management Institute.
Schwaber, K., & Sutherland, J. (2020). The Scrum guide: The definitive guide to scrum. Scrum.org.
Shaikh, A. A., Alamoudi, H., Alharthi, M., & Glavee-Geo, R. (2022). Advances in mobile financial
services: a review of the literature and future research directions. International Journal of Bank
Marketing, 41(1). https://doi.org/10.1108/ijbm-06-2021-0230
Torno, A., Werth, O., Nickerson, R. C., Breitner, M. H., & Muntermann, J. (2021). More than Mobile
Banking – A Taxonomy-based Analysis of Mobile Personal Finance Applications. Twenty-Fifth
Pacific Asia Conference on Information Systems (PACIS).
141