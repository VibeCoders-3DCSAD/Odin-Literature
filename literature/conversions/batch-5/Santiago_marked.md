---
conversion_metadata:
  converted_at: "2026-07-21T08:34:18Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Santiago.pdf"
  source_pdf_sha256: "2b2a11d464f6b8e87a0ece76135ba2777612b1038ee90a11a9d443769b178196"
  page_count: 10
  markdown_char_count: 143900
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

DOI: http://dx.doi.org/10.26483/ijarcs.v16i3.7256

Volume 16, No. 3, May-June 2025

ISSN No. 0976-5697

International Journal of Advanced Research in Computer Science

RESEARCH PAPER

Available Online at www.ijarcs.info

BUDGET AND FINANCIAL MANAGEMENT INFORMATION SYSTEM FOR 
PUBLIC ELEMENTARY SCHOOLS: ANALYTICS AND PREDICTIVE INSIGHTS 
FOR MOOE ALLOCATION USING LINEAR REGRESSION

Santiago, Rose Lyn T.  
College of Computer Studies 
Laguna State Polytechnic University 
Sta. Cruz, Laguna, Philippines

Villarica, Mia V.

College of Computer Studies 
Laguna State Polytechnic University 
Sta. Cruz, Laguna, Philippines

Bernardino, Mark P.  
College of Computer Studies 
Laguna State Polytechnic University 
Sta. Cruz, Laguna, Philippines

Abstract: Public elementary schools in the Philippines face persistent challenges in managing their financial resources, primarily due to reliance 
on manual processes that are prone to errors, inefficiencies, and a lack of transparency. To address these concerns, this study developed a Budget 
and Financial Management Information System (BFMIS) tailored to the operational needs of public elementary schools. The system integrates 
Artificial  Intelligence  (AI)  and  linear  regression  analytics  to  automate  budget  planning,  optimize  the  allocation  of  Maintenance  and  Other 
Operating  Expenses  (MOOE),  and  enhance  financial  reporting.  Using  Agile  methodology,  the  system  was  designed  with  a  user-centered 
approach  and  developed  through  iterative  cycles  involving  continuous  stakeholder  feedback.  Core  features  include  modules  for  budget 
allocation,  expenditure  tracking,  predictive  budgeting,  and  automated  report  generation  in  compliance  with  the  Department  of  Education 
(DepEd) financial policies. The system underwent black-box testing and was evaluated against ISO/IEC 25010 (software quality) and ISO 27001 
(information security) standards. Furthermore, User Acceptance Testing (UAT) was conducted using the Technology Acceptance Model (TAM) 
to assess perceived usefulness, ease of use, and user satisfaction among school administrators, financial officers, and DepEd auditors. Results 
showed  that  BFMIS  significantly  improved  accuracy  in  budget  forecasting,  enhanced  accountability  through  audit  trails  and  real-time 
dashboards,  and  facilitated  informed  financial  decision-making.  The  integration  of  predictive  analytics  reduced  human  error  and  supported 
proactive  planning  and  equitable  resource  utilization.  This  research  contributes  a  scalable,  AI-driven  solution  for  improving  financial 
management processes in the Philippine public education sector.

Keywords: BFMIS, Public Elementary Schools, Predictive Analytics, MOOE, Agile, Linear Regression, Black box, TAM

I.

INTRODUCTION

Public  elementary  schools  in  the  Philippines  face 
major challenges in managing their financial resources due to 
the absence of a dedicated financial management system.     
Current  manual  processes  often  lead  to  errors,  inconsistent 
records, and difficult 
y  in  tracking  expenditures,  which 
compromises  transparency,  accountability,  and  compliance 
with government regulations.

To  address  these  issues,  the  researcher  proposes  a 
Budget  and  Financial  Management  Information  System 
powered  by  Artificial  Intelligence  (AI).  This  system  will 
streamline  financial  processes  by  enabling  efficient  data 
creation,  storage,  organization,  and  analysis.  AI  features  will 
provide  real-time  analytics,  predictive  insights  using  linear 
regression,  and  data-driven  recommendations 
to  support 
informed decision-making.

Designed  as  a  user-friendly  and  secure  Knowledge 
Management  System  (KMS),  the  proposed  solution  aims  to 
enhance financial planning, optimize resource use, and ensure 
compliance.  Ultimately,  it  empowers  schools  with  the  tools 
needed for sustainable and transparent financial management.

A.  Research Problem 
The  study  aimed  to  answer  the  following  key  research 
questions: 
1.  What  are  the  financial  management  challenges  currently 
faced by public elementary schools? 
2. How can a Budget and Financial Management Information 
System  improve  the  efficiency  of  budget  allocation  and 
expenditure tracking? 
3.  In  what  ways  can  the  proposed  system  enhance  financial 
transparency, accountability, and compliance with government 
regulations? 
4. What are the key features and functionalities required for an 
effective  financial  management  system  tailored  to  public 
elementary schools.

II.  RESEARCH OBJECTIVES

This  study  aims  to  develop  a  Budget  and  Financial 
Management Information System (BFMIS) tailored for public 
elementary  schools.  The  system  integrates  linear  regression 
analytics  to  optimize  MOOE  allocation  based  on  historical 
spending  patterns.  It  enhances  expenditure  tracking  through 
real-time  monitoring,  ensures  compliance  with  DepEd  Order

© 2024-2027, IJARCS All Rights Reserved

128

---

<!-- PAGE 2 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

No. 60, s. 2016, and promotes transparency and accountability 
through  dashboards  and  audit  trails.  Designed  to  minimize 
manual  errors  and  support  data-driven  decision-making, 
BFMIS  provides  predictive  insights  and  automates  financial 
reporting, ultimately improving school resource utilization and 
educational outcomes.

A.  Specific Objectives  
1. Design and develop an AI-driven BFMIS integrating linear 
regression  to  automate  budget  creation,  optimize  MOOE 
allocation, and streamline expenditure tracking. 
2.    Incorporate  AI-based  reporting  to  generate  real-time 
financial  reports  aligned  with  DepEd  policies,  automating 
submission  of  expenditure 
logs,  variance  analyses,  and 
compliance reports. 
3.  Validate  the  system  through  black-box  testing  and  pilot 
implementation in selected schools, assessing compliance with 
ISO/IEC  25010  and  ISO  27001  and  addressing  MOOE 
allocation inefficiencies. 
4.  Assess  user  acceptance  using  the  Technology  Acceptance 
Model 
testing  with  school 
administrators, financial officers, and auditors. 
5. Develop an implementation plan detailing stakeholder roles, 
training,  timelines,  and  risk  mitigation  to  ensure  successful 
and sustainable BFMIS adoption in public elementary schools. 
B. Theoretical Framework

through  structured

(TAM)

Fig. 1, Agile Software Development (Agile Alliance, 
2001)  flexibility  is  especially  valuable  in  public  school 
financial management, where compliance with Department of 
Education (DepEd) policies and the need for transparency are 
critical,  and  policies  may  change  during  development.  The 
approach  enables  easy  adaptation  to  new  guidelines  or 
stakeholder requests without disrupting the project. Agile also 
emphasizes collaboration, involving school administrators and 
auditors  in  regular  reviews  to  ensure  the  system  meets 
transparency and accountability standards.

Continuous testing and automated validation at every 
stage  help  catch  errors  early,  ensuring  accuracy  in  financial 
data.  Agile  prioritizes  high-impact  features,  optimizing 
resource  use  and  delivering  a  reliable  system  faster.  Regular 
retrospective  meetings  drive  ongoing  improvement,  keeping 
the  BFMIS  sustainable  and  responsive  to  changing  needs. 
Overall,  Agile  enables  the  development  of  a  system  that 
streamlines  budget  management,  supports  informed  financial 
decisions,  and  ensures  regulatory  compliance  for  public 
schools.

Figure 1. Agile Software Development Cycle 
Source: https://www.wrike.com/agile-guide/agile-development-life-cycle/

B.  Conceptual Framework

Fig.  2,  conceptual  framework  of  (BFMIS)  follows  a 
structured  Input-Process-Output  model.  It  begins  with  the 
Input  phase,  where  administrators  enter  budget  data, 
expenditures,  and  user  roles.  The  Process  phase  involves 
storing  and  organizing  data  using  a  relational  database,  with 
AI-driven  linear  regression  analyzing  financial  patterns  to 
support  decision-making.  In  the  Output  phase,  the  system 
generates  financial  reports  and  predictive  insights,  offering 
clear  overviews  of  fund  utilization  and  recommendations  for 
future  allocations.  Overall,  BFMIS  enhances  transparency, 
accuracy, and efficiency in public school finances.

Figure 2. Conceptual Framework of the BFMIS

C.  Scope and Limitations of the Study

This study presents the development of a Budget and 
Financial  Management  Information  System  (BFMIS)  for 
public  elementary  schools,  functioning  as  a  Knowledge 
Management  System  (KMS)  integrated  with  AI.  The  system 
streamlines  budget  allocation,  expenditure 
tracking,  and 
financial reporting through key features like linear regression-
based  analytics,  real-time  reporting,  and  role-based  access 
control. While it enhances transparency and decision-making, 
limitations include dependency on accurate data input, lack of 
cloud  support,  basic  security,  and  manual  updates  for  policy 
improved 
changes.  The  system 
accountability and future advancements in AI and scalability.

lays  a  foundation  for

D.  Significance of the Study 
This  study

introduces  a  Budget  and  Financial 
Management  Information  System  (BFMIS)  that  leverages 
automation  and  AI  to  improve  school  financial  processes. 
Using a relational database and linear regression analytics, the 
system  ensures  organized 
records,  accurate 
expenditure  tracking,  and  predictive  insights.  It  simplifies

financial

© 2024-2027, IJARCS All Rights Reserved

129

---

<!-- PAGE 3 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

for  compliance  and

reporting 
reduces  manual  errors. 
Administrators gain better budget oversight, teachers and staff 
access  real-time  data  for  planning,  and  government  agencies 
reports.  Ultimately,  BFMIS  enhances 
receive  accurate 
transparency, 
allocation, 
accountability, 
contributing to improved educational outcomes.

resource

and

III.  RELATED LITERATURE

Budget  and

financial  management

information 
systems are crucial for optimizing resource allocation in public 
elementary  schools,  particularly  concerning  the  Maintenance 
and  Other  Operating  Expenses  (MOOE).  These  system  helps 
to ensure that funds are used effectively to support educational 
goals and improve school operations.

A.  Budget Allocation 
Effective  budget  allocation  is  central  to  school  management. 
As highlighted by Amado et al. (2025), involving stakeholders 
like parents and teachers in budgeting leads to better resource 
use and alignment with school needs. Strategic investments in 
technology  and  instructional  materials,  noted  by  Hargreaves 
and  Fullan  (2015),  enhance  teaching  quality  and  motivate 
teachers.  Beronibla  (2024)  emphasizes  transparency  through 
inclusive  budgeting  and  monitoring  systems,  with  regular 
audits to maintain financial integrity.

B.  Maintenance and Other Operating Expenses  (MOOE)

In the Philippine context, the Maintenance and Other 
Operating Expenses (MOOE) are central to school operations. 
These  government-allocated  funds  cover  basic  expenses  such 
as utilities and minor repairs. DepEd Orders No. 13, s. 2016, 
and  No.  122,  s.  2017,  provide  guidelines  on  the  use  and 
reporting  of  MOOE,  ensuring  that  school  heads  practice 
responsible  spending  and  maintain  financial  transparency. 
However, schools often face shortages in covering even basic 
needs,  prompting  calls  for  increased  budget  support  and 
capacity  building  for  school  heads  (Almazan,  2023).  Despite 
these  constraints,  the  proper  use  of  MOOE  significantly 
contributes  to  daily  operations,  teacher  development,  and 
student welfare (Gaspar et al., 2022).

C.  Annual Procurement Plan

Another  critical  component  of  financial  planning  is 
the  Annual  Procurement  Plan  (APP).  Mandated  under  RA 
9184,  the  APP  ensures  that  all  procurement  activities  are 
properly  planned,  aligned  with 
institutional  goals,  and 
included  in  the  approved  budget.  In  public  schools,  it 
consolidates  procurement  needs  and  supports  the  Annual 
Implementation  Plan  (AIP).  It  serves  as  a  control  mechanism 
for fiscal discipline and compliance, requiring approval by the 
school  head  and  consistency  with  government  standards.  The 
APP  enhances 
in  resource 
utilization,  as  highlighted  by  Beronibla  (2024),  and  reflects 
international  best  practices  in  strategic  procurement  planning 
(Office of Procurement Regulation, 2021).

transparency  and  efficiency

D.  Annual Implementation Plan

The Annual Implementation Plan (AIP) is a key tool 
for school-based management, translating long-term goals into 
yearly  actions.  In  the  Philippines,  DepEd  mandates  the  AIP 
(DepEd  Order  No.  44,  s.  2015),  which  outlines  programs, 
budgets,  and  timelines  for  the  fiscal  year.  It  is  developed

collaboratively  by  school  leaders  and  stakeholders  to  align 
resources with school needs (DM No. 004, s. 2023). 
Globally,  similar  plans  like  Victoria,  Australia’s  AIP  link 
strategic  goals  with  clear  targets  and  funding  (Department  of 
Education  Victoria,  2020).  The  AIP  supports  transparency, 
accountability,  and  shared  governance 
regular 
monitoring and evaluation, fostering continuous improvement 
(Smith & Jones, 2019).

through

E.  AI in Predictive Analytics and Financial Management

Advancements  in  Artificial  Intelligence  (AI)  have 
significantly influenced financial forecasting and management. 
AI 
technologies,  particularly  predictive  analytics,  use 
sophisticated  algorithms  and  machine  learning  to  identify 
complex  patterns  within  large  datasets,  far  beyond  the 
capabilities  of  traditional  linear  forecasting  methods.  As 
described by Faheem et al. (2024), AI allows financial analysts 
to  incorporate  a  wide  array  of  data  sources,  including  social 
media  sentiment  and  macroeconomic  indicators,  to  generate 
real-time, adaptable insights.

F.  Linear Regression 
Linear

is  a

regression

fundamental  predictive 
analytics tool that forecasts outcomes like budget needs based 
on historical data (IBM). It estimates a best-fit linear equation 
to  reveal  trends  and  relationships,  aiding  decision-makers  in 
predicting  future  results.  Roustaei  (2024)  highlights 
its 
effectiveness  in  identifying  patterns,  especially  with  limited 
data.  Wasserbacher  and  Spindler  (2022)  note  that  digital 
financial systems and data analytics further strengthen the use 
of regression models for financial planning and analysis.

G.  Black Box Testing

Fig.  3,  Black  box  testing  evaluates  a  system’s 
behavior  based  on  inputs  and  expected  outputs  without 
considering  internal  code,  making  it  ideal  for  validating 
functionality,  security,  and  role-based  access  in  financial 
systems  (Byol  &  Foygel,  2023).  Sun  and  Li  (2023)  applied 
black  box  testing  to  a  Family  Financial  Management  System 
to verify user authentication and data integrity, highlighting its 
importance  in  securing  financial  operations.  Pressman  and 
Maxim  (2014)  stress  that  black  box  testing  from  a  user’s 
perspective  efficiently  detects  functional  errors  and  input 
issues, recommending multiple test cases per module to ensure 
reliability.  For  systems 
the  Budget  and  Financial 
Management  Information System  (BFMIS), black box testing 
is crucial for validating critical features such as financial data 
accuracy and access control.

like

Figure 3. Black Box Testing Model 
Source: https://www.testbirds.com/en/blog/black-box-testing-enhancing-user-
experience/

H.  Technology Acceptance Model (TAM) 
Venkatesh  and  Davis  (2000)  expanded  TAM  by  including 
social  influence  and  cognitive  factors,  showing  that  user

© 2024-2027, IJARCS All Rights Reserved

130

---

<!-- PAGE 4 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

acceptance evolves with experience. Delima and Tejero (2022) 
found  that  perceived  usefulness  and  ease  of  use  significantly 
impact satisfaction among school financial managers. Sun and 
Li  (2023)  confirmed  TAM’s  relevance  by  highlighting  the 
need for security, data integrity, and role-based access to build 
user  trust.  Byol  and  Foygel  (2023)  emphasized  that  positive 
perceptions driven by intuitive dashboards and secure features 
increase long-term adoption, particularly for sensitive financial 
systems.

I.  Synthesis

The literature highlights the vital  role of Budget  and 
Financial  Management  Information  Systems  (BFMIS)  in 
improving resource allocation and transparency, especially for 
managing  Maintenance  and  Other  Operating  Expenses 
(MOOE)  in  public  elementary  schools.  Technology-enabled 
budgeting  supports  accurate  expenditure  tracking,  regulatory 
compliance, and alignment with educational goals.

Challenges  include  limited  digital  tools  and  reliance 
on  manual  processes,  as  noted  by  Upadhyaya  (2016)  and 
Zuhro et al. (2024), who stress the need for infrastructure and 
training to maximize system benefits. School-based budgeting 
frameworks  (Demas  &  Arcia,  2015)  promote  autonomy  and 
accountability but financial transparency remains hindered by 
budget  constraints  and  inadequate  training  (Almazan,  2023; 
Gaspar et al., 2022).

AI-driven predictive budgeting, supported by Faheem 
et  al.  (2024)  and  Harshitha  et  al.  (2025),  along  with  linear 
regression models (Roustaei, 2024; Wasserbacher & Spindler, 
2022), enhances forecasting and financial planning. Black box 
testing is critical  for ensuring system  reliability, security, and 
usability, as emphasized by Byol and Foygel (2023), Sun and 
Li (2023), and Pressman and Maxim (2014).

(TAM), 
The  Technology  Acceptance  Model 
originally from Davis (1989) and expanded by Venkatesh and 
Davis  (2000),  offers  a  framework  for  understanding  user 
adoption  based  on  perceived  usefulness  and  ease  of  use. 
Studies  like  Delima  and  Tejero  (2022)  confirm  TAM’s 
effectiveness in school financial systems.

Overall,  the  literature  supports  BFMIS  development 
to  overcome  manual  inefficiencies,  meet  compliance,  and 
provide  predictive  insights.  Integrating  AI,  rigorous  testing, 
and  user-focused  design  ensures  a  reliable,  accepted  system 
that enhances financial transparency in education.

IV.  METHODOLOGY

This  chapter  explains  the  methods  and  procedures 
used  in  the  development  and  evaluation  of  the  Budget  and 
Financial  Management  Information  System  (BFMIS).  It 
the  research  design,  population  and  sampling 
outlines 
techniques, data collection instruments, validation procedures, 
statistical treatments, project design, development model, and t

he testing and evaluation process.

A.  Research Design

This  study  employed  a  descriptive-developmental 
research design. The descriptive part analyzed  current  budget 
and financial management practices, focusing on Maintenance 
and Other Operating Expenses (MOOE) in  public elementary 
schools.  The  developmental  aspect  involved  designing  and 
implementing 
the  Budget  and  Financial  Management 
Information  System  (BFMIS),  integrating  AI—specifically 
linear regression—to enhance predictive budget forecasting.

The  population  included  school  heads,  financial 
officers, and DepEd auditors from  selected public elementary 
schools under Laguna’s Schools Division Office. A purposive 
sample of at least 30 participants directly involved in financial 
management was selected.

Data  collection  combined  document  analysis, 
interviews,  and  surveys.  Documents  from  Pook  Elementary 
School  (2022–2024  MOOE  records)  were  gathered  and 
cleaned  for  system 
interviews  with 
administrators and financial officers identified challenges and 
system  needs.  Surveys,  based  on  the  Technology  Acceptance 
Model (TAM), were conducted during user acceptance testing 
to  evaluate  system  usability,  features,  and  user  attitudes 
toward the BFMIS.

testing.  Structured

Table  1  presents  the  TAM-based  questionnaire  used 
in  User  Acceptance  Testing  (UAT),  assessing  quality  factors, 
perceived  ease  of  use,  perceived  usefulness,  system  features, 
and  user  satisfaction.The  questionnaire  was  validated  by 
information  systems  experts  to  ensure  clarity  and  relevance, 
with  their  feedback  incorporated  for  refinement.Survey  data 
were  analyzed  using  descriptive  statistics 
(frequencies, 
percentages, means, standard deviations). Regression analysis 
tested  the  AI  component’s  accuracy  in  forecasting  MOOE 
allocation.  TAM  constructs  were  quantitatively  evaluated  to 
measure system acceptance and user behavior.

Table 1. Sample Technology Acceptance Model (TAM)

Questionnaire Structure

Criteria

Sample Question Item

Scale

Quality Factors

“The system provides correct 
and accurate results in 
displaying real-time data 
comparing budget allocations 
versus actual expenses.”

1 
(Strongly 
Disagree) 
– 5 
(Strongly 
Agree)

Perceived Ease of Use

“The system is easy to 
navigate.”

Perceived Usefulness

“The system enhances 
transparency in financial 
reports.”

System Features and 
Functionality

“The dashboard provides 
relevant and clear financial 
insights.”

User Satisfaction and 
Acceptance

“I am satisfied with the 
system's performance.”

1 – 5

1 – 5

1 – 5

1 – 5

The  system  development  followed  Fig.  4  Agile 
Development  Methodology,  chosen  for  its  iterative,  flexible 
approach suited to the dynamic financial management needs of 
public  schools  allowing  frequent  collaboration  and  feedback 
from  stakeholders 
including  school  principals,  financial 
officers,  and  DepEd  auditors.  Each  development  sprint 
included  planning,  designing,  building,  and  testing  essential 
functionalities,  prioritizing 
and 
predictive analytics capabilities.

compliance,

accuracy,

The  Budget  and  Financial  Management  Information 
System  (BFMIS)  was  developed  using  several  key  software 
tools  are  XAMPP  provides  a  local  server  environment  with 
Apache, MySQL, and PHP for development and testing. PHP

© 2024-2027, IJARCS All Rights Reserved

131

---

<!-- PAGE 5 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

handled  dynamic  web  pages,  user  authentication,  and 
budget/expense  tracking.  MySQL  served  as  the  relational 
database  for  secure  and  efficient  data  management.  Dompdf 
enabled PDF report generation for easy sharing and archiving. 
PhpSpreadsheet  allowed  exporting  reports 
to  Excel  for 
detailed  analysis.  Python  was  used  for  predictive  analytics, 
applying  linear  regression  for  budget  forecasting.  Scikit-learn 
built  and  validated  the  regression  models.  JSON  facilitated 
data  exchange  between  Python  analytics  and  the  PHP  front-
end  for  dynamic  visualization.  These  tools  were  chosen  for 
their  reliability,  integration  ease,  open-source  nature,  and 
alignment with the Agile development approach.

Prediction 
Module

User 
Management

Security 
Testing

Total

TC037

TC023–
TC025

TC026–
TC028

TC033–
TC035

—

•  Usability Testing

3

3

3

37

Yes

Yes

Yes

—

the

User

analysis

interface

assessments

with 
administrators  ensure  accessibility  and  ease  of  use 
(Nielsen, 1994), while compliance validation verifies 
that  automated  reports  adhere  to  DepEd  financial 
regulations  (Department  of  Education,  2023).  Pilot 
implementation  involves  real-world  deployment  in 
selected  schools  to  test  system  functionality  and 
reliability  (Pressman  &  Maxim,  2020),  followed  by 
feedback 
collection  of 
through 
stakeholder  input  for  system  improvements  (Patton, 
2015).  ISO  compliance  testing  validates  the  system 
against  ISO/IEC  25010  (software  quality)  and  ISO 
27001  (security)  standards  (ISO,  2011;  ISO,  2013). 
User  Acceptance  Testing  (UAT)  uses  surveys  and 
interviews  guided  by  the  Technology  Acceptance 
intentions  and 
Model 
to  assess  user 
satisfaction 
complemented  by 
quantitative  analysis  through  statistical  review  of 
UAT data to derive actionable insights (Field, 2018). 
Finally,  implementation  planning  develops  a  phased 
rollout 
full 
deployment,  training,  stakeholder  roles,  and  risk 
management  aligned  with  ISO  standards  (Kerzner, 
2017).

including  pilot

(Davis,  1989),

roadmap

(TAM)

stages,

ensure

Together,

these  methods

the 
development of a robust, user-friendly, and compliant 
financial  management 
improves 
budgeting,  transparency,  and  efficiency  in  public 
elementary  schools,  supporting  predictive  budget 
planning aligned with  the schools’ improvement  and 
procurement plans.

system

that

V.  RESULTS AND DISCUSSIONS

This  chapter  presents  the  presentation,  analysis  and 
discussions  based  on  the  methods  employed  to  achieve  the 
study's objectives. The presentation is structured according to 
the specific research objectives and includes a comprehensive 
explanation  of  the  system’s  design,  the  integration  of  linear 
regression analytics, and the results of multiple testing phases. 
It  also  highlights  how  the  predictive  model  supports  budget 
allocation  optimization,  how  the  system  automates  financial 
reporting aligned with DepEd policies, and how it performs in 
terms of usability, functionality, and user acceptance.

The  Budget  and  Financial  Information  System 
(BFMIS)  was  developed  using  user-centered  and  AI-driven 
linear  regression  analytics  that  automate  budget  creation, 
optimize MOOE allocation, and track expenditures.

Figure 4. Agile Software Development Methodology Model 
Source:https://www.geeksforgeeks.org/software-engineering-agile-software-
development/

B.

Testing and Evaluation Procedure

•  Black-Box Testing

Employed  to  test  inputs  and  outputs  without 
exposing  system  logic,  using  equivalence  partitioning  to 
ensure  system  robustness.  Table  2  summarizes  the  Black 
Box testing conducted on key system functions, evaluating 
performance  based  on  functional  requirements  without 
examining  internal  code,  following  the  3–5  test  case 
guideline  (Pressman  &  Maxim,  2014)  for  balanced 
coverage  and  efficiency.  Testing  covered  modules 
according to complexity, criticality, and coverage.

Table 2. Black Box Test Case Table

Function / 
Module

Test Case IDs

No. of Test 
Cases

Aligned with 
3–5 Rule

Login 
Functionality

Role-Based 
Access 
Control

Dashboard 
Overview

Budget 
Management

Expense 
Management

Report 
Generation

TC001–
TC003, 
TC029, 
TC030

TC004, 
TC005, 
TC027

TC006–
TC010

TC011–
TC015, 
TC031

TC016–
TC020, 
TC032

TC021–
TC022,

5

3

5

6

6

3

Yes

Yes

Yes

Slightly 
exceeds (✓ 
critical 
module)

Slightly 
exceeds (✓ 
related 
module)

Yes

© 2024-2027, IJARCS All Rights Reserved

132

---

<!-- PAGE 6 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Fig. 5 presents the BFMIS dashboard, providing real-
time  insights  into  a  school’s  financial  status.  It  enhances 
transparency  through  live  data  access,  summary  reports,  and 
audit logs. Predictive analytics aid budget planning, supporting 
findings by Martinez and Reyes (2021). Audit logs and access 
controls  promote  accountability,  aligning  with  Byol  and 
insights.  Automated 
Foygel’s 
reporting ensures timely compliance, as highlighted by Ali  et 
al. (2022 ).

fraud  prevention

(2023)

Figure 7. View Expense Entries Page

Figure  8  showcases  BFMIS’s  predictive  insight 
feature, which uses linear regression to analyze historical data 
and  recommend  future  budget  allocations.  By  comparing 
predicted (green) and actual (blue) values, the system enables 
data-driven  decisions  that  enhance  MOOE  planning  and 
resource optimization.

Key  benefits  include  smart  recommendations  that 
automatically suggest budget allocations based on trends, such 
as  rising  utility  or  material  costs,  reducing  guesswork 
(Alvarado  &  Reyes,  2021);  misalignment  detection  that 
highlights  discrepancies  between  planned  and  predicted 
spending  for  timely  adjustments  (Caballero  et  al.,  2020); 
proactive planning that empowers administrators to anticipate 
and respond to funding needs in evolving areas (Lee & Santos, 
2022); evidence-based decisions that support budget proposals 
with data-backed insights (Delos Reyes & Bautista, 2023); and 
user-friendly  visuals  featuring  color-coded,  intuitive  charts 
improve  accessibility  even  for  non-technical  users 
that 
(Tolentino  &  Uy,  2021).  Overall,  this  feature  transforms 
BFMIS  into  a  practical  AI-powered  tool  for  transparent, 
efficient, and strategic school budgeting.

Figure 5. BFMIS Dashboard

Fig.  6  displays  the  BFMIS  Add  Budget  page,  where 
users  input  project-specific  budget  details  such  as  category, 
amount,  and  fiscal  year.  Designed  for  school  administrators 
and finance officers, the interface supports accurate, real-time 
data entry and easy updates. Its user-friendly layout enhances 
adoption  and  reduces  errors  (Hussein  et  al.,  2022).  By 
replacing  manual  methods,  it  improves  data  consistency  and 
compliance  (Abubakar  &  Sulaiman,  2021)  while  supporting 
better 
in  public 
education (Delos Santos & Gomez, 2023).

financial  planning  and  accountability

Figure 6. BFMIS Add Budget Page

Fig.  7  shows  the  View  Expense  Entries  module  of 
BFMIS, which provides a clear summary of recorded expenses 
by project and fiscal year. It displays key details like category, 
budget,  actual spending, percentage used, and  remarks. Users 
can  filter,  update,  or  delete  entries,  with  color-coded 
percentages  aiding  quick  assessment.  Designed  for  usability 
and transparency (Hussein et al., 2022), the module promotes 
accurate  expense  tracking,  reduces  errors,  and  aligns  with 
DepEd  financial  guidelines  for  better  accountability  and 
MOOE management.

Figure 8. MOOE Prediction Page

Figure  9  presents  the  BFMIS  Budget  and  Expense 
Report  page,  summarizing  allocations,  actual  spending,  and 
utilization  rates  across  MOOE  categories  from  January  1  to 
May  15,  2025.  This  real-time  report  supports  accountability 
and  informed  decision-making  by  showing  how  funds  are 
being used.

The  report

includes  columns  for  School  Year, 
Category,  Allocated  Budget,  Total  Expenses,  and  % 
Utilization.  For  instance,  100%  spending  in  the  Graduation 
Program  reflects  full  budget  use,  while  mid-range  figures  in 
other programs indicate ongoing or scheduled disbursements.

The  %  Utilization  metric—calculated  by  dividing 
expenses  by  the  budget—offers  a  quick  view  of  financial 
efficiency,  helping  identify  over-  or  under-utilized  funds. 
Automated calculations and clear visualizations reduce manual 
errors and promote transparency.

© 2024-2027, IJARCS All Rights Reserved

133

---

<!-- PAGE 7 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Aligned with studies on digital finance tools (Gao et 
al.,  2021;  Tolentino  &  Uy,  2021),  this  page  enhances  budget 
tracking,  enables  timely  reallocations,  and  strengthens  school 
financial governance.

Report

Auto-

DomPDF,

All users

Generator

generates

PhpSpreadshe

PDF/Excel

et

reports

Figure  10  presents  the  comparison  of  current-year 
budget  allocations  and  the  system’s  predicted  values  for  the 
next cycle. Notable increases were observed in categories like 
Electricity  (+9.83%)  and  Fidelity  Bond  (+66.67%)  due  to 
historical  spending  trends  and  prior  underestimations.  ICT 
Program  predictions  showed  minimal  variance,  indicating 
stable  expenditure.  Table  4  details  these  results,  including 
absolute  differences  and  percentage  changes,  confirming  the 
accuracy of the Linear Regression model.

Figure 10. Actual vs. Predicted MOOE Allocations per Category

To  evaluate  the  model’s  reliability,  the  following 
regression metrics such as Mean Absolute Error (MAE), Root 
Mean Square Error (RMSE) and R² Score were computed.

The results presented in Table 4 shows that the model 
maintains  high  predictive  accuracy,  with  an  R²  value  of 
92.81%,  indicating  that  most  of  the  variance  in  the  target 
budget  can  be  explained  by  historical  data.  After  generating 
the  predictions,  the  system  automatically  populates  MOOE 
expenditure  logs,  variance  analysis  reports,  and  DepEd-
compliant  financial  summaries,  all  downloadable  in  PDF  and 
Excel  formats  as  shown  in  Figure  9.  This  feature  aligns  with 
reporting  standards  required  by  DepEd  and  significantly 
reduces manual report generation time.

Table 4: Regression Model Performance

Figure 9. Budget and Expense Report Page

Table  3  outlines  the  core  functional  modules  of  the 
BFMIS,  each  addressing  key  financial  management  needs  in 
public  schools  while  promoting  automation  and  data-driven 
decision-making.  Budget  Allocation  Module,  built  with  PHP 
and  MySQL,  this  module  allows  structured  input  and  secure 
storage  of  MOOE  data,  enhancing  accuracy  and  accessibility 
(Abubakar  &  Sulaiman,  2021).  AI-Powered  Prediction 
Module, developed in Python using Scikit-learn, it uses linear 
regression to  forecast future budget  needs, enabling proactive 
and strategic planning (Delos Santos & Gomez, 2023). Budget 
Visualization Module uses Chart.js and JSON to display real-
time  comparisons  of  planned  vs.  actual  spending,  supporting 
transparency  and  informed  decision-making  (Hussein  et  al., 
2022).  Automated  Reporting  Module,  generates  PDF  and 
Excel  reports via DomPDF and PhpSpreadsheet,  streamlining 
compliance  and  reducing  manual  work  (Ramírez-Alujas  & 
Dassen,  2020).  Together,  these  modules  demonstrate  how 
transparency,  efficiency,  and 
BFMIS  enhances  financial 
responsiveness in public elementary schools.

To address  Objective No. 2, BFMIS includes an AI-
driven  reporting  module  that  applies  Linear  Regression  to 
forecast  future  MOOE  allocations.  This  machine  learning 
method  analyzes  historical  spending 
to  predict 
category-wise  budget  needs  for  the  next  fiscal  year.  As 
supported  by  Widanaputra  et  al.  (2022),  linear  regression  is 
effective  for  educational  budget  forecasting,  enabling  data-
driven and proactive financial planning.

trends

Table 3: Core Features of the Developed BFMIS

Module

Description

Key

Technologies

Stakeholders

Benefitted

Budget

Inputs and

PHP, MySQL

School Heads,

Metric

Value

Interpretation

Allocation

categorizes

Finance

MOOE

AI-Powered

Predicts next

Python,

School Heads,

Prediction

year’s budget

Scikit-learn

Finance

via Linear

Regression

Monitors

actual vs.

planned

Expenditure

Tracker

Chart.js,

School Heads,

JSON

Finan

ce, DepEd,

Stakeholders

Mean Absolute 
Error (MAE)

₱1,532.75

Indicates low average error 
between predicted and actual 
values.

Root Mean 
Square Error 
(RMSE)

₱2,126.84

Confirms minimal large 
prediction errors, enhancing 
reliability.

R² Score

0.9281

High explanatory power—
92.81% of variance is 
accounted for by the model.

© 2024-2027, IJARCS All Rights Reserved

134

---

<!-- PAGE 8 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Black-box  testing  involved  37  test  cases  (TC001–
TC037)  assessing  core  modules,  user  access,  validation, 
responsiveness,  and  security.  Conducted  by  IT  professionals 
and  developers,  results  showed  strong  compliance,  with  most 
testers  reporting  full  success.  Only  one  tester  reported  four 
failures  related  to  UI  responsiveness  (TC010),  missing  field 
validation (TC012), incorrect feedback for over-budget entries 
(TC017), and display issues when the budget is zero (TC020). 
Additional  issues  included  input  sanitization  vulnerabilities 
(TC030),  UI  inconsistencies  across  roles,  and  acceptance  of 
invalid  numeric  data.  These  align  with  prior  studies 
emphasizing strong input validation and consistent UI design. 
Despite  minor  issues,  the  system  showed  no  major  bugs  or 
crashes,  confirming  it  is  functionally  complete  and  ready  for 
deployment  with  slight  improvements  in  validation  and  UI 
responsiveness.

•  User Feedback and Observations

“The  system  works  as  intended  and  performs  in  accordance 
with  its  expected  features.  It  passed  all  necessary  functional 
tests,  making  it  suitable  and  ready  for  deployment.  The 
interface is user-friendly, easy to navigate, and responds well 
to defined inputs.“

The  evaluation  of  user  acceptance  and  behavioral 
intention to use the (BFMIS) was conducted using the (TAM) 
through structured (UAT) with school administrators, financial 
officers,  and  DepEd  auditors, 
focusing  on  perceived 
usefulness,  perceived  ease  of  use,  and  attitude  toward  using 
the system.

(BFMIS)

Information  System

As  shown  in  Table  5,  the  Budget  and  Financial 
Management 
received 
consistently  high  ratings  across  all  quality  dimensions  based 
on  user  evaluations.  Users  strongly  agreed  on  the  system's 
accuracy,  functionality,  and  security,  with  the  highest  rating 
given  to  secure  access  and  user  role  management  (Mean  = 
4.70), affirming the system’s reliability in protecting sensitive 
financial data (Byol & Foygel, 2023). They found the system 
easy  to  navigate,  input  data,  and  retrieve  reports  (Weighted 
Mean  =  4.61),  reflecting  its  high  usability  and  user-friendly 
interface  design  (Hussein  et  al.,  2022).  Respondents  also 
acknowledged  the  system’s  role  in  enhancing  transparency, 
efficiency,  and  decision-making 
in  budget  management 
(Weighted  Mean  =  4.51),  consistent  with  findings  from 
Delima and Tejero (2022). Key features such as the dashboard, 
AI  predictions,  and  policy  compliance  were  positively 
received, with  dashboard clarity rated highest (Mean = 4.67), 
supporting  better  financial  insights  (Tolentino  &  Uy,  2021). 
Additionally,  users  expressed  high  satisfaction  and  a  strong 
likelihood of regular use (Weighted Mean = 4.51), indicating 
readiness  for  adoption  and  long-term  integration,  in  line  with 
the  Technology  Acceptance  Model  (Venkatesh  &  Davis, 
2000).  The  low  standard  deviation  across  all  categories 
(ranging  from  0.47  to  0.62)  signals  consistent  agreement 
among  respondents,  validating  the  system’s  effectiveness, 
trustworthiness, and alignment with user needs.

Table 5. Summary of Evaluation Results for the Budget and Financial 
Management Information System (BFMIS)

Dimension

Highest-Rated 
Criterion

Mea
n

Weighte
d Mean

Verbal 
Interpret
ation

System

Secure user role &

4.70

4.62

Strongly

Quality

password 
protection

Ease of Use

Ease of retrieving 
reports and data

4.63

4.61

Perceived 
Usefulness

Enhances 
transparency in 
financial reports

4.67

4.51

4.67

4.51

Agree

Strongly 
Agree

Strongly 
Agree

Strongly 
Agree

System 
Features & 
Functionalit
y

Dashboard 
provides relevant 
and clear financial 
insights

User 
Satisfaction 
& 
Acceptance

Likely to use the 
system regularly 
and satisfied with 
performance

4.53

4.51

Strongly 
Agree

In  Fig.  11,  Implementation  Plan,  the  BFMIS  is 
recommended to be implemented from June 2025 to December 
2026  through  a  phased  rollout  to  ensure  readiness,  training, 
and  policy  alignment.  Phase  1  (June–July  2025)  focuses  on 
system finalization, stakeholder consultation, and pilot school 
selection.  Phase  2  (July–August  2025)  involves  creating 
training  materials  and  conducting  sessions  to  build  user 
capacity.  In  Phase  3  (August–October  2025),  the  system  will 
go 
in  pilot  schools,  with  ongoing  feedback  and 
adjustments  based  on  monitoring.  Phase  4  (October  2025–
the  refined  system  deployed 
February  2026)  will  see 
nationwide,  supported  by  policy  integration  and  helpdesk 
activation. Finally, Phase 5 (January–December 2026) ensures 
sustainability  through  continuous  updates,  integration  with 
DepEd  systems  (BEIS  and  EMIS),  and  a  full  impact 
assessment to guide long-term adoption.

live

Figure 11. BFMIS Phased Implementation Plan

As  shown  in  Table  6,  the  Risk  Mitigation  Strategies 
ensures  a  structured,  scalable,  and  user-centered  approach  to 
transforming  financial  management  in  public  elementary 
schools.  These  mitigation  strategies  reflect  a  comprehensive 
approach  to  implementation  planning,  incorporating  both 
technical  safeguards  and  user-centered  practices  in  line  with 
global standards for ICT deployment in education (UNESCO, 
2022).

© 2024-2027, IJARCS All Rights Reserved

135

---

<!-- PAGE 9 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Table 6. Risk Mitigation Strategies

Identified Risk

Mitigation Plan

Resistance to change

Early orientation and stakeholder 
engagement

Low digital literacy in 
some schools

Tiered training support and digital 
mentoring

Data privacy and system 
breaches

Secure role-based access and 
encryption protocols

Budget inaccuracies or 
prediction discrepancies

Continuous model validation and 
override options

Network or device 
incompatibility

Offline-first design and minimum 
hardware specs

VI.  SUMMARY, CONCLUSIONS, AND 
RECOMMENDATIONS

A.  Summary

The  BFMIS  was  designed

to  address  manual 
inefficiencies in budgeting by offering digital, AI-driven tools 
for  transparency  and  decision-making.  The  system’s  core 
modules  are  the  Budget  Allocation  Module,  which  facilitates 
structured input of MOOE items based on specific categories. 
AI-Powered  Prediction  Module 
that  utilizes  a  Linear 
Regression algorithm to estimate future MOOE allocations.

The  model  achieved  the  accuracy  of  R²  =  0.9281, 
Mean Absolute Error (MAE) = ₱1,532.75, Root Mean Square 
Error (RMSE) = ₱2,126.84. Expenditure Tracker displays real-
time  spending  versus  planned  allocation  using  dynamic 
summaries  and  tables,  and  the  Automated  Reporting  Module 
generates  DepEd-compliant  PDF  and  Excel  reports  for  easier 
audit and submission. 
A total of 37 black-box test cases were conducted to validate 
functionality,  usability,  data  accuracy,  and  security,  all  of 
which were passed successfully.

The  User  Acceptance  Evaluation  shows  that  users 
highly  rated  BFMIS  across  five  key  areas  on  a  5-point  scale: 
System Quality (4.47), Ease of Use (4.46), Usefulness (4.37), 
Features (4.37), and Satisfaction (4.37). These scores indicate 
the  system  is  reliable,  easy  to  use,  valuable,  well-equipped, 
and well-liked, suggesting strong user approval  and readiness 
for adoption.

To support deployment, a five-phase implementation 
plan was proposed: pre-implementation, training, pilot rollout, 
full  deployment,  and  sustainability.  Risk  mitigation  strategies 
were  included  to  address  issues  such  as  digital  skill  gaps, 
system  resistance,  forecasting  challenges,  and  cybersecurity 
concerns.

B.  Conclusions

The  BFMIS  successfully  achieved  its  goals,  offering  a 
reliable  digital  solution  that  automates  budgeting,  improves 
accuracy,  and  promotes  financial  accountability.  Its  use  of 
Linear  Regression  enhanced  the  predictive  quality  of  MOOE 
forecasts, while the system's user interface, role-based access, 
and real-time data display supported positive user experiences. 
All  modules  performed  as  expected  based  on  testing. 
While  minor  improvements  in  UI  responsiveness  and  input 
validation  were  noted,  the  system  is  technically  robust  and 
ready for implementation.

The  implementation  framework  ensures  scalability  and 
regulatory  compliance.  Its  phased  structure  and  risk  controls 
promote a smooth, sustainable rollout.

C.  Recommendations

To support the broader deployment and sustainability 
of  the  BFMIS,  it  is  recommended  that  the  Department  of 
Education  (DepEd)  formally  adopt  and  integrate  the  system 
the  national  school  budgeting  framework.  Regular 
into 
the 
training  sessions  should  be  conducted  alongside 
establishment  of  a  dedicated  help  desk  to  provide  technical 
support and ensure us 
er  proficiency.  Quarterly  updates 
must  be  implemented  to  maintain  system  security  and  the 
accuracy of AI-powered forecasts.

Future  development  should  ensure  integration  with 
existing  DepEd  platforms  such  as  BEIS  and  EMIS  to 
streamline  data  flow  and  reduce  redundancy.  Expanded  pilot 
implementations  across  schools  with  varying  ICT  capacities 
are  encouraged  to  evaluate  system  adaptability  in  diverse 
contexts.  Within  12  months  of  deployment,  a  comprehensive 
impact  assessment  should  be  conducted  to  evaluate  system 
performance, user satisfaction, and improvements in financial 
accuracy.

Lastly, continuous risk monitoring must be embedded 
into  system  operations  to  address  emerging  challenges  and 
ensure long-term success. Regular assessments and mitigation 
strategies  will  help  sustain  BFMIS  effectiveness  and 
institutional trust.

VII.  ACKNOWLEDGMENT

First and foremost, I would like to extend my gratitude to the  
Almighty God for giving me the strength and perseverance to 
make it through this journey. His guidance helped me through 
every challenge. To my parents Cenon and Merly Santiago,  for 
love and support. To my siblings, Eric, Erwin and Mercy, thank 
you  for  always  being  there  with  love,  encouragement,  and 
guidance.  Dr.  Mario  R.  Briones,  the  University  President  of 
Laguna  State  Polytechnic  University  under  his  leadership  and 
support.  Dr.  Mia  V.  Villarica,  the  Associate  Dean  of  the 
College  of  Computer  Studies  –  Santa  Cruz  Campus,  the 
researcher’s  thesis  adviser  for  guidance  and  support  in  the 
study.  Mr.  Mark  P.  Bernardino,  the  Subject  Specialist  of  the 
College of Computer Studies, for the professional guidance and 
support.Ms. Maria Laureen B. Miranda, the Technical Editor of 
the College of Computer Studies and Research Coordinator for 
the valuable guidance and support in the study. Mr. Jhon Jhon 
P.  Zotomayor,  for  patiently  checking  the  grammar  of  the 
manuscript.  Mr.  Edward  S.  Flores,  the  Statistician,  for  his 
expertise.  Lastly,  the  researcher  is  deeply  grateful  to  the 
College  of  Computer  Studies  faculty  member  for  their 
invaluable knowledge and insightful guidance.

VIII.  REFERENCES

[1]  Abubakar, M., & Sulaiman, A. (2021). Manual vs. digital 
record 
institutions.  Journal  of  Public

budgeting:  Comparative  study  on 
accuracy 
Administration and Finance, 9(2), 45–59.

in  public

financial

[2]  Ali,  M.,  Reyes,  G.,  &  Martinez,  F.  (2022).  Automated 
reporting  and  policy  compliance  in  public  education.

© 2024-2027, IJARCS All Rights Reserved

136

---

<!-- PAGE 10 -->

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

International  Journal  of  Educational  Technology,  14(3), 
88–95.

[3]  Almazan,  J.  (2023).  MOOE  budget  challenges

Philippine  public 
Educational Management, 7(1), 22–31.

schools.  Philippine

in 
Journal  of

[4]  Amado,  R.,  Dela  Cruz,  N.,  &  Villanueva,  P.  (2025). 
in  school  management:  A 
Participatory  budgeting 
stakeholder approach. Journal of Educational Governance, 
5(1), 13–21.

[5]  Beronibla,  C.  (2024).  Promoting  transparency  through 
inclusive budgeting. Journal of School Financial Planning, 
6(2), 39–47.

[6]  Beronibla,  C.  (2024).  Promoting  transparency  through 
inclusive budgeting. Journal of School Financial Planning, 
6(2), 39–47.

[7]  Caballero,  S.,  Torres,  L.,  &  Ramos,  J.  (2020).  Detection 
of  budget  misalignments  in  educational  finance.  Journal 
of Educational Finance, 12(2), 119–126.

[8]  Davis, F. D. (1989). Perceived usefulness, perceived ease 
of  use,  and  user  acceptance  of  information  technology. 
MIS Quarterly, 13(3), 319–340.

[9]  Delima,  A.,  &  Tejero,  M.  (2022).  User  satisfaction  and 
system usability in school financial management systems. 
Philippine Journal of Educational ICT, 10(1), 24–35. 
[10]  Delos  Reyes,  L.,  &  Bautista,  R.  (2023).  Evidence-based 
budgeting  in  Philippine  schools.  Journal  of  Education 
Policy and Management, 7(1), 58–66.

[11]  Delos Santos, K., & Gomez, R. (2023). Forecasting tools 
in  school  financial  planning.  Education  and  Technology 
Journal, 8(4), 77–85.

[12]  Demas,  A.,  &  Arcia,  G.  (2015).  What  matters  most  for 
school autonomy and accountability? A framework paper. 
World Bank.

[13]  Department  of  Education  Victoria.  (2020).  Annual 
requirements.

implementation  plan:  Guidelines  and 
Melbourne: Department of Education.

[21]  Lee,  D.,  &  Santos,  M.  (2022).  Proactive  financial 
planning  in  public  institutions.  Fiscal  Planning  Journal, 
14(1), 31–40.

[22]  Martinez,  E.,  &  Reyes,  J.  (2021).  Use  of  predictive 
analytics  in  school  budget  planning.  Journal  of  Smart 
Education, 5(1), 48–56.

[23]  Office  of  Procurement  Regulation.

(2021).  Public

procurement best practices. https://oprtt.org

[24]  Pressman,  R.  S.,  &  Maxim,  B.  R.  (2014).  Software 
(8th  ed.).

engineering:  A  practitioner’s  approach 
McGraw-Hill Education.

[25]  Ramírez-Alujas,  Á.,  &  Dassen,  N.  (2020).  Public  sector 
Inter-American 
and  open  government.

innovation 
Development Bank.

[26]  Roustaei, M. (2024). Predictive modeling using linear

regression for limited data. Financial Analytics Journal, 
8(1), 44–52.

[27]  Smith, A., & Jones, P. (2019). Monitoring and evaluating 
school implementation plans. International Journal of 
Education Management, 10(4), 55–63.

[28]  Sun, L., & Li, J. (2023). Black box testing in family 
financial systems. Journal of Information Security & 
Testing, 9(2), 72–80.

[29]  Tolentino, A., & Uy, M. (2021). Effective financial

visualization for school reporting. Philippine Journal of 
Educational Innovation, 4(3), 67–74.

[30]  Tsakiridis,  L.,  Petrova,  N.,  &  Campos,  M.  (2023).  Data 
integration  between  MySQL  and  Python  for  educational 
analytics. Journal of Data Engineering in Education, 7(2), 
93–101.

[31]  UNESCO.  (2022).  ICT  in  education:  Guidelines  for 
national  policy  and  implementation.  United  Nations 
Educational, Scientific and Cultural Organization. 
[32]  Upadhyaya, R. (2016). Challenges in financial digital 
transformation in education. Journal of Educational 
Finance Reform, 2(2), 22–29.

[14]  Faheem, M., Abdullah, R., & Zhang, Y. (2024). The role 
of  AI  in  predictive  analytics  for  finance.  International 
Journal of Artificial Intelligence Applications, 16(2), 34–
43.

[33]  Venkatesh, V., & Davis, F. D. (2000). A theoretical

extension of the Technology Acceptance Model: Four 
longitudinal field studies. Management Science, 46(2), 
186–204.

[15]  Gao,  Y.,  Lin,  X.,  &  Hu,  M.  (2021).  Digital  financial 
management  in  public  schools.  Journal  of  Educational 
Innovation and Finance, 9(3), 92–100.

[16]  Gaspar, R., De Luna, A., & Borja, K. (2022). The role of 
MOOE  in  student  welfare  and  teacher  development. 
Philippine Journal of Basic Education, 11(1), 17–27. 
[17]  Harshitha,  S.,  Anand,  D.,  &  Mehta,  V.  (2025).  AI-based 
budgeting systems in  education:  A  review. Journal  of  AI 
in Education, 5(2), 59–67.

[18]  Hargreaves, A., & Fullan, M. (2015). Professional capital: 
Transforming teaching in every school. Teachers College 
Press.

[19]  Hussein,  R.,  Alonto,  F.,  &  De  Guzman,  L.  (2022). 
Evaluating  financial  systems'  interface  design  in  public 
education. Journal of ICT in Public Sector, 6(3), 101–109. 
[20]  IBM.  (n.d.).  What  is  linear  regression?.  IBM  Knowledge 
Center. https://www.ibm.com/topics/linear-regression

[34]  Wang, Y., Liu, Q., & Zhao, H. (2020). SQLFlow: 
Building predictive pipelines with SQL and AI 
integration. Proceedings of the IEEE Data Science 
Conference, 89–97.

[35]  Wasserbacher,  M.,  &  Spindler,  M.  (2022).  Applying 
regression models in  digital financial systems. Journal  of 
Computational Finance, 12(1), 25–36.

[36]  Widanaputra,  A.,  Santosa,  D.,  &  Aisyah,  N.  (2022). 
Forecasting  educational  budgets  using  linear  regression. 
Journal of Education Finance and Analytics, 5(3), 34–45.

[37]  Zuhro,  S.,  Kurniawan,  A.,  &  Prasetya,  T.  (2024). 
Overcoming 
financial 
in 
digitization. Journal  of Educational  Transformation, 8(1), 
13–22.

school-based

barriers

© 2024-2027, IJARCS All Rights Reserved

137

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

DOI: http://dx.doi.org/10.26483/ijarcs.v16i3.7256
ISSN No. 0976-5697
Volume 16, No. 3, May-June 2025
International Journal of Advanced Research in Computer Science
RESEARCH PAPER
Available Online at www.ijarcs.info
BUDGET AND FINANCIAL MANAGEMENT INFORMATION SYSTEM FOR
PUBLIC ELEMENTARY SCHOOLS: ANALYTICS AND PREDICTIVE INSIGHTS
FOR MOOE ALLOCATION USING LINEAR REGRESSION
Santiago, Rose Lyn T. Villarica, Mia V.
College of Computer Studies College of Computer Studies
Laguna State Polytechnic University Laguna State Polytechnic University
Sta. Cruz, Laguna, Philippines Sta. Cruz, Laguna, Philippines
Bernardino, Mark P.
College of Computer Studies
Laguna State Polytechnic University
Sta. Cruz, Laguna, Philippines
Abstract: Public elementary schools in the Philippines face persistent challenges in managing their financial resources, primarily due to reliance
on manual processes that are prone to errors, inefficiencies, and a lack of transparency. To address these concerns, this study developed a Budget
and Financial Management Information System (BFMIS) tailored to the operational needs of public elementary schools. The system integrates
Artificial Intelligence (AI) and linear regression analytics to automate budget planning, optimize the allocation of Maintenance and Other
Operating Expenses (MOOE), and enhance financial reporting. Using Agile methodology, the system was designed with a user-centered
approach and developed through iterative cycles involving continuous stakeholder feedback. Core features include modules for budget
allocation, expenditure tracking, predictive budgeting, and automated report generation in compliance with the Department of Education
(DepEd) financial policies. The system underwent black-box testing and was evaluated against ISO/IEC 25010 (software quality) and ISO 27001
(information security) standards. Furthermore, User Acceptance Testing (UAT) was conducted using the Technology Acceptance Model (TAM)
to assess perceived usefulness, ease of use, and user satisfaction among school administrators, financial officers, and DepEd auditors. Results
showed that BFMIS significantly improved accuracy in budget forecasting, enhanced accountability through audit trails and real-time
dashboards, and facilitated informed financial decision-making. The integration of predictive analytics reduced human error and supported
proactive planning and equitable resource utilization. This research contributes a scalable, AI-driven solution for improving financial
management processes in the Philippine public education sector.
Keywords: BFMIS, Public Elementary Schools, Predictive Analytics, MOOE, Agile, Linear Regression, Black box, TAM
A. Research Problem
I. INTRODUCTION
The study aimed to answer the following key research
Public elementary schools in the Philippines face questions:
major challenges in managing their financial resources due to 1. What are the financial management challenges currently
the absence of a dedicated financial management system. faced by public elementary schools?
Current manual processes often lead to errors, inconsistent 2. How can a Budget and Financial Management Information
records, and difficult y in tracking expenditures, which System improve the efficiency of budget allocation and
compromises transparency, accountability, and compliance expenditure tracking?
with government regulations. 3. In what ways can the proposed system enhance financial
To address these issues, the researcher proposes a transparency, accountability, and compliance with government
Budget and Financial Management Information System regulations?
powered by Artificial Intelligence (AI). This system will 4. What are the key features and functionalities required for an
streamline financial processes by enabling efficient data effective financial management system tailored to public
creation, storage, organization, and analysis. AI features will elementary schools.
provide real-time analytics, predictive insights using linear
regression, and data-driven recommendations to support II. RESEARCH OBJECTIVES
informed decision-making.
Designed as a user-friendly and secure Knowledge This study aims to develop a Budget and Financial
Management System (KMS), the proposed solution aims to Management Information System (BFMIS) tailored for public
enhance financial planning, optimize resource use, and ensure elementary schools. The system integrates linear regression
compliance. Ultimately, it empowers schools with the tools analytics to optimize MOOE allocation based on historical
needed for sustainable and transparent financial management. spending patterns. It enhances expenditure tracking through
real-time monitoring, ensures compliance with DepEd Order
© 2024-2027, IJARCS All Rights Reserved 128

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

No. 60, s. 2016, and promotes transparency and accountability
through dashboards and audit trails. Designed to minimize
| manual  | errors  and  support  | data-driven  |     | decision-making,  |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------------- | ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BFMIS provides predictive insights and automates financial
reporting, ultimately improving school resource utilization and
educational outcomes.
A.  Specific Objectives
1. Design and develop an AI-driven BFMIS integrating linear
| regression  | to  automate  | budget  | creation,  | optimize  |     | MOOE  |     |     |     |     |     |     |     |     |     |
| ----------- | ------------- | ------- | ---------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allocation, and streamline expenditure tracking.
| 2.    Incorporate  | AI-based          | reporting  |           | to  generate  | real-time   |      |     |     |     |     |     |     |     |     |     |
| ------------------ | ----------------- | ---------- | --------- | ------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| financial          | reports  aligned  | with       | DepEd     | policies,     | automating  |      |     |     |     |     |     |     |     |     |     |
| submission         | of  expenditure   | logs,      | variance  |               | analyses,   | and  |     |     |     |     |     |     |     |     |     |
compliance reports.
3. Validate the system through black-box testing and pilot
implementation in selected schools, assessing compliance with
| ISO/IEC  | 25010  and  ISO  | 27001  | and  | addressing  |     | MOOE  |     |     |     |     |     |     |     |     |     |
| -------- | ---------------- | ------ | ---- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

allocation inefficiencies.  Figure 1. Agile Software Development Cycle
4. Assess user acceptance using the Technology Acceptance  Source: https://www.wrike.com/agile-guide/agile-development-life-cycle/
| Model  | (TAM)  through  | structured  |     | testing  | with  | school  |     |                       |     |     |     |     |     |     |     |
| ------ | --------------- | ----------- | --- | -------- | ----- | ------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
|        |                 |             |     |          |       |         | B.  | Conceptual Framework  |     |     |     |     |     |     |     |
administrators, financial officers, and auditors.
Fig. 2, conceptual framework of (BFMIS) follows a
5. Develop an implementation plan detailing stakeholder roles,
|     |     |     |     |     |     |     | structured  |     | Input-Process-Output  |     | model.  |     | It  begins  | with  | the  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------------- | --- | ------- | --- | ----------- | ----- | ---- |
training, timelines, and risk mitigation to ensure successful
|     |     |     |     |     |     |     | Input  | phase,  | where  | administrators  |     | enter  | budget  |     | data,  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------ | --------------- | --- | ------ | ------- | --- | ------ |
and sustainable BFMIS adoption in public elementary schools.
|     |     |     |     |     |     |     | expenditures,  |     | and  | user  roles.  | The  | Process  | phase  | involves  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------------- | ---- | -------- | ------ | --------- | --- |
B. Theoretical Framework
storing and organizing data using a relational database, with
Fig. 1, Agile Software Development (Agile Alliance,
|                     |                 |     |           |     |         |         | AI-driven  | linear            |     | regression  | analyzing  | financial  |         | patterns  | to      |
| ------------------- | --------------- | --- | --------- | --- | ------- | ------- | ---------- | ----------------- | --- | ----------- | ---------- | ---------- | ------- | --------- | ------- |
| 2001)  flexibility  | is  especially  |     | valuable  | in  | public  | school  |            |                   |     |             |            |            |         |           |         |
|                     |                 |     |           |     |         |         | support    | decision-making.  |     |             | In  the    | Output     | phase,  | the       | system  |
financial management, where compliance with Department of
generates financial reports and predictive insights, offering
Education (DepEd) policies and the need for transparency are
clear overviews of fund utilization and recommendations for
critical, and policies may change during development. The
approach  enables  easy  adaptation  to  new  guidelines  or  future  allocations.  Overall,  BFMIS  enhances  transparency,
accuracy, and efficiency in public school finances.
stakeholder requests without disrupting the project. Agile also

emphasizes collaboration, involving school administrators and
| auditors  | in  regular  reviews  | to  | ensure  | the  | system  | meets  |     |     |     |     |     |     |     |     |     |
| --------- | --------------------- | --- | ------- | ---- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transparency and accountability standards.
Continuous testing and automated validation at every
stage help catch errors early, ensuring accuracy in financial
| data.  Agile  | prioritizes  | high-impact  |     | features,  | optimizing  |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ------------ | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resource use and delivering a reliable system faster. Regular
retrospective meetings drive ongoing improvement, keeping

| the  BFMIS  | sustainable  | and  responsive  |     | to  changing  |     | needs.  |     |     |     |     |     |     |     |     |     |
| ----------- | ------------ | ---------------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 2. Conceptual Framework of the BFMIS
| Overall,  | Agile  enables  | the  development  |     | of  | a  system  | that  |     |                                     |     |     |     |     |     |     |     |
| --------- | --------------- | ----------------- | --- | --- | ---------- | ----- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |                 |                   |     |     |            |       | C.  | Scope and Limitations of the Study  |     |     |     |     |     |     |     |
streamlines budget management, supports informed financial
decisions,  and  ensures  regulatory  compliance  for  public  This study presents the development of a Budget and
|     |     |     |     |     |     |     | Financial  | Management  |     | Information  |     | System  |     | (BFMIS)  | for  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------ | --- | ------- | --- | -------- | ---- |
schools.
|     |     |     |     |     |     |     | public  | elementary  |     | schools,  | functioning  |     | as  a  | Knowledge  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --------- | ------------ | --- | ------ | ---------- | --- |

Management System (KMS) integrated with AI. The system
|     |     |     |     |     |     |     | streamlines  |     | budget  | allocation,  | expenditure  |     | tracking,  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------------ | ------------ | --- | ---------- | --- | ---- |
financial reporting through key features like linear regression-
|     |     |     |     |     |     |     | based  | analytics,  |     | real-time  | reporting,  | and  | role-based  |     | access  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---------- | ----------- | ---- | ----------- | --- | ------- |
control. While it enhances transparency and decision-making,
limitations include dependency on accurate data input, lack of
cloud support, basic security, and manual updates for policy
|     |     |     |     |     |     |     | changes.  | The  | system  | lays  | a   | foundation  | for  | improved  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------- | ----- | --- | ----------- | ---- | --------- | --- |
accountability and future advancements in AI and scalability.
|     |     |     |     |     |     |     | D.          | Significance of the Study  |              |              |         |            |            |             |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------------------- | ------------ | ------------ | ------- | ---------- | ---------- | ----------- | --- |
|     |     |     |     |     |     |     |             | This                       | study        | introduces   |         | a  Budget  | and        | Financial   |     |
|     |     |     |     |     |     |     | Management  |                            | Information  |              | System  | (BFMIS)    | that       | leverages   |     |
|     |     |     |     |     |     |     | automation  |                            | and  AI      | to  improve  | school  |            | financial  | processes.  |     |
Using a relational database and linear regression analytics, the
|     |     |     |     |     |     |     | system       | ensures  |            | organized  | financial   |            | records,  | accurate        |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ---------- | ---------- | ----------- | ---------- | --------- | --------------- | --- |
|     |     |     |     |     |     |     | expenditure  |          | tracking,  | and        | predictive  | insights.  |           | It  simplifies  |     |
129
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137
reporting for compliance and reduces manual errors. collaboratively by school leaders and stakeholders to align
Administrators gain better budget oversight, teachers and staff resources with school needs (DM No. 004, s. 2023).
access real-time data for planning, and government agencies Globally, similar plans like Victoria, Australia’s AIP link
receive accurate reports. Ultimately, BFMIS enhances strategic goals with clear targets and funding (Department of
transparency, accountability, and resource allocation, Education Victoria, 2020). The AIP supports transparency,
contributing to improved educational outcomes. accountability, and shared governance through regular
monitoring and evaluation, fostering continuous improvement
III. RELATED LITERATURE (Smith & Jones, 2019).
Budget and financial management information
systems are crucial for optimizing resource allocation in public E. AI in Predictive Analytics and Financial Management
elementary schools, particularly concerning the Maintenance Advancements in Artificial Intelligence (AI) have
and Other Operating Expenses (MOOE). These system helps significantly influenced financial forecasting and management.
to ensure that funds are used effectively to support educational AI technologies, particularly predictive analytics, use
goals and improve school operations. sophisticated algorithms and machine learning to identify
complex patterns within large datasets, far beyond the
capabilities of traditional linear forecasting methods. As
A. Budget Allocation
described by Faheem et al. (2024), AI allows financial analysts
Effective budget allocation is central to school management. to incorporate a wide array of data sources, including social
As highlighted by Amado et al. (2025), involving stakeholders media sentiment and macroeconomic indicators, to generate
like parents and teachers in budgeting leads to better resource real-time, adaptable insights.
use and alignment with school needs. Strategic investments in
technology and instructional materials, noted by Hargreaves F. Linear Regression
and Fullan (2015), enhance teaching quality and motivate Linear regression is a fundamental predictive
teachers. Beronibla (2024) emphasizes transparency through analytics tool that forecasts outcomes like budget needs based
inclusive budgeting and monitoring systems, with regular on historical data (IBM). It estimates a best-fit linear equation
audits to maintain financial integrity. to reveal trends and relationships, aiding decision-makers in
predicting future results. Roustaei (2024) highlights its
B. Maintenance and Other Operating Expenses (MOOE)
effectiveness in identifying patterns, especially with limited
In the Philippine context, the Maintenance and Other data. Wasserbacher and Spindler (2022) note that digital
Operating Expenses (MOOE) are central to school operations. financial systems and data analytics further strengthen the use
These government-allocated funds cover basic expenses such of regression models for financial planning and analysis.
as utilities and minor repairs. DepEd Orders No. 13, s. 2016,
and No. 122, s. 2017, provide guidelines on the use and G. Black Box Testing
reporting of MOOE, ensuring that school heads practice Fig. 3, Black box testing evaluates a system’s
responsible spending and maintain financial transparency. behavior based on inputs and expected outputs without
However, schools often face shortages in covering even basic considering internal code, making it ideal for validating
needs, prompting calls for increased budget support and functionality, security, and role-based access in financial
capacity building for school heads (Almazan, 2023). Despite systems (Byol & Foygel, 2023). Sun and Li (2023) applied
these constraints, the proper use of MOOE significantly black box testing to a Family Financial Management System
contributes to daily operations, teacher development, and to verify user authentication and data integrity, highlighting its
student welfare (Gaspar et al., 2022). importance in securing financial operations. Pressman and
Maxim (2014) stress that black box testing from a user’s
C. Annual Procurement Plan
perspective efficiently detects functional errors and input
Another critical component of financial planning is issues, recommending multiple test cases per module to ensure
the Annual Procurement Plan (APP). Mandated under RA reliability. For systems like the Budget and Financial
9184, the APP ensures that all procurement activities are Management Information System (BFMIS), black box testing
properly planned, aligned with institutional goals, and is crucial for validating critical features such as financial data
included in the approved budget. In public schools, it accuracy and access control.
consolidates procurement needs and supports the Annual
Implementation Plan (AIP). It serves as a control mechanism
for fiscal discipline and compliance, requiring approval by the
school head and consistency with government standards. The
APP enhances transparency and efficiency in resource
utilization, as highlighted by Beronibla (2024), and reflects
international best practices in strategic procurement planning
(Office of Procurement Regulation, 2021).
D. Annual Implementation Plan Figure 3. Black Box Testing Model
Source: https://www.testbirds.com/en/blog/black-box-testing-enhancing-user-
The Annual Implementation Plan (AIP) is a key tool experience/
for school-based management, translating long-term goals into
H. Technology Acceptance Model (TAM)
yearly actions. In the Philippines, DepEd mandates the AIP
(DepEd Order No. 44, s. 2015), which outlines programs, Venkatesh and Davis (2000) expanded TAM by including
budgets, and timelines for the fiscal year. It is developed social influence and cognitive factors, showing that user
© 2024-2027, IJARCS All Rights Reserved 130

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

acceptance evolves with experience. Delima and Tejero (2022)  The  population  included  school  heads,  financial
found that perceived usefulness and ease of use significantly  officers, and DepEd auditors from selected public elementary
impact satisfaction among school financial managers. Sun and  schools under Laguna’s Schools Division Office. A purposive
Li (2023) confirmed TAM’s relevance by highlighting the  sample of at least 30 participants directly involved in financial
need for security, data integrity, and role-based access to build  management was selected.
user trust. Byol and Foygel (2023) emphasized that positive  Data  collection  combined  document  analysis,
perceptions driven by intuitive dashboards and secure features  interviews, and surveys. Documents from Pook Elementary
increase long-term adoption, particularly for sensitive financial  School  (2022–2024  MOOE  records)  were  gathered  and
systems.  cleaned  for  system  testing.  Structured  interviews  with
administrators and financial officers identified challenges and
I.  Synthesis
system needs. Surveys, based on the Technology Acceptance
The literature highlights the vital role of Budget and
Model (TAM), were conducted during user acceptance testing
Financial  Management  Information  Systems  (BFMIS)  in  to  evaluate  system  usability,  features,  and  user  attitudes
improving resource allocation and transparency, especially for
toward the BFMIS.
| managing  | Maintenance  | and  | Other  | Operating  | Expenses  |     |     |     |     |     |     |     |     |
| --------- | ------------ | ---- | ------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 1 presents the TAM-based questionnaire used
(MOOE) in public elementary schools. Technology-enabled  in User Acceptance Testing (UAT), assessing quality factors,
budgeting supports accurate expenditure tracking, regulatory  perceived ease of use, perceived usefulness, system features,
compliance, and alignment with educational goals.
|     |     |     |     |     |     |     | and  user  satisfaction.The  |     |     | questionnaire  |     | was  | validated  by  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | -------------- | --- | ---- | -------------- |
Challenges include limited digital tools and reliance  information systems experts to ensure clarity and relevance,
on  manual  processes,  as  noted  by  Upadhyaya  (2016)  and  with their feedback incorporated for refinement.Survey data
Zuhro et al. (2024), who stress the need for infrastructure and
|     |     |     |     |     |     |     | were  analyzed  | using  | descriptive  |     | statistics  |     | (frequencies,  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------ | --- | ----------- | --- | -------------- |
training to maximize system benefits. School-based budgeting
percentages, means, standard deviations). Regression analysis
frameworks (Demas & Arcia, 2015) promote autonomy and  tested the AI component’s accuracy in forecasting MOOE
accountability but financial transparency remains hindered by
allocation. TAM constructs were quantitatively evaluated to
budget constraints and inadequate training (Almazan, 2023;
measure system acceptance and user behavior.
| Gaspar et al., 2022).  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AI-driven predictive budgeting, supported by Faheem  Table 1. Sample Technology Acceptance Model (TAM)
et al. (2024) and Harshitha et al. (2025), along with linear  Questionnaire Structure

regression models (Roustaei, 2024; Wasserbacher & Spindler,
|     |     |     |     |     |     |     | Criteria  |     | Sample Question Item  |     |     |     | Scale  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------------- | --- | --- | --- | ------ |
2022), enhances forecasting and financial planning. Black box
testing is critical for ensuring system reliability, security, and
usability, as emphasized by Byol and Foygel (2023), Sun and  Quality Factors  “The system provides correct  1
|     |     |     |     |     |     |     |     |     | and accurate results in  |     |     |     | (Strongly  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | ---------- |
Li (2023), and Pressman and Maxim (2014).  displaying real-time data  Disagree)
The  Technology  Acceptance  Model  (TAM),  comparing budget allocations  – 5
originally from Davis (1989) and expanded by Venkatesh and  versus actual expenses.”  (Strongly
Agree)
| Davis  (2000),  | offers     | a  framework  |             | for  | understanding  | user      |     |     |     |     |     |     |     |
| --------------- | ---------- | ------------- | ----------- | ---- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| adoption        | based  on  | perceived     | usefulness  |      | and  ease      | of  use.  |     |     |     |     |     |     |     |
Studies  like  Delima  and  Tejero  (2022)  confirm  TAM’s  Perceived Ease of Use  “The system is easy to  1 – 5
navigate.”
effectiveness in school financial systems.
Overall, the literature supports BFMIS development
|               |         |                  |     |       |              |      | Perceived Usefulness  |     | “The system enhances  |     |     |     | 1 – 5  |
| ------------- | ------- | ---------------- | --- | ----- | ------------ | ---- | --------------------- | --- | --------------------- | --- | --- | --- | ------ |
| to  overcome  | manual  | inefficiencies,  |     | meet  | compliance,  | and  |                       |     |                       |     |     |     |        |
transparency in financial
provide predictive insights. Integrating AI, rigorous testing,
reports.”
and user-focused design ensures a reliable, accepted system
that enhances financial transparency in education.
|     |      |              |     |     |     |     | System Features and  |     | “The dashboard provides       |             |     |     | 1 – 5  |
| --- | ---- | ------------ | --- | --- | --- | --- | -------------------- | --- | ----------------------------- | ----------- | --- | --- | ------ |
|     |      |              |     |     |     |     | Functionality        |     | relevant and clear financial  |             |     |     |        |
|     | IV.  | METHODOLOGY  |     |     |     |     |                      |     |                               | insights.”  |     |     |        |
This chapter explains the methods and procedures  User Satisfaction and  “I am satisfied with the  1 – 5
used in the development and evaluation of the Budget and  Acceptance  system's performance.”
| Financial  | Management  | Information  |     | System  | (BFMIS).  | It  |     |     |     |     |     |     |     |
| ---------- | ----------- | ------------ | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |

| outlines  | the  research  | design,  |     | population  | and  | sampling  |     |     |     |     |     |     |     |
| --------- | -------------- | -------- | --- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
techniques, data collection instruments, validation procedures,  The  system  development  followed  Fig.  4  Agile
statistical treatments, project design, development model, and t Development Methodology, chosen for its iterative, flexible
  he testing and evaluation process.  approach suited to the dynamic financial management needs of
public schools allowing frequent collaboration and feedback
A.  Research Design
|     |     |     |     |     |     |     | from  stakeholders  |     | including  | school  | principals,  |     | financial  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ---------- | ------- | ------------ | --- | ---------- |
This  study  employed  a  descriptive-developmental  officers,  and  DepEd  auditors.  Each  development  sprint
research design. The descriptive part analyzed current budget  included planning, designing, building, and testing essential
and financial management practices, focusing on Maintenance
|     |     |     |     |     |     |     | functionalities,  | prioritizing  |     | compliance,  |     | accuracy,  | and  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------- | --- | ------------ | --- | ---------- | ---- |
and Other Operating Expenses (MOOE) in public elementary  predictive analytics capabilities.
schools. The developmental aspect involved designing and  The Budget and Financial Management Information
| implementing  | the  | Budget  | and  | Financial  | Management  |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
System (BFMIS) was developed using several key software
Information  System  (BFMIS),  integrating  AI—specifically  tools are XAMPP provides a local server environment with
linear regression—to enhance predictive budget forecasting.  Apache, MySQL, and PHP for development and testing. PHP
131
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

handled  dynamic  web  pages,  user  authentication,  and    TC037
| budget/expense  | tracking.  | MySQL  |     | served  | as  | the  relational  |     |     |     |     |     |     |     |     |     |
| --------------- | ---------- | ------ | --- | ------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
database for secure and efficient data management. Dompdf
|     |     |     |     |     |     |     |     | Prediction  |     | TC023– |     | 3   |     | Yes  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --- | --- | --- | ---- | --- |
enabled PDF report generation for easy sharing and archiving.  Module  TC025

| PhpSpreadsheet  | allowed  |     | exporting  | reports  | to  | Excel  | for  |     |     |     |     |     |     |     |     |
| --------------- | -------- | --- | ---------- | -------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
detailed analysis. Python was used for predictive analytics,  User  TC026– 3  Yes
applying linear regression for budget forecasting. Scikit-learn  Management  TC028

built and validated the regression models. JSON facilitated
|     |     |     |     |     |     |     |     | Security  |     | TC033– |     | 3   |     | Yes  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --- | --- | --- | ---- | --- |
data exchange between Python analytics and the PHP front-
|     |     |     |     |     |     |     |     | Testing  |     | TC035  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- |
end for dynamic visualization. These tools were chosen for
|                      |              |     |        |              |     |          |      | Total  |     | —   |     | 37  |     | —   |     |
| -------------------- | ------------ | --- | ------ | ------------ | --- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| their  reliability,  | integration  |     | ease,  | open-source  |     | nature,  | and  |        |     |     |     |     |     |     |     |
alignment with the Agile development approach.

•  Usability Testing
|     |     |     |     |     |     |     |     |     |     | User  | interface  |     | assessments  |     | with  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------------ | --- | ----- |
administrators ensure accessibility and ease of use
(Nielsen, 1994), while compliance validation verifies
|     |     |     |     |     |     |     |     |     | that  | automated  | reports  | adhere  | to  DepEd  |     | financial  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | -------- | ------- | ---------- | --- | ---------- |
regulations (Department of Education, 2023). Pilot
|     |     |     |     |     |     |     |     |     | implementation  |          | involves  | real-world    |                | deployment  | in   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | --------- | ------------- | -------------- | ----------- | ---- |
|     |     |     |     |     |     |     |     |     | selected        | schools  | to        | test  system  | functionality  |             | and  |
reliability (Pressman & Maxim, 2020), followed by
|     |     |     |     |     |     |     |     |     | feedback  | analysis  |     | through  | the  | collection  | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | ---- | ----------- | --- |

stakeholder input for system improvements (Patton,
Figure 4. Agile Software Development Methodology Model
2015). ISO compliance testing validates the system
Source:https://www.geeksforgeeks.org/software-engineering-agile-software-
development/  against ISO/IEC 25010 (software quality) and ISO
|     |     |     |     |     |     |     |     |     | 27001 (security) standards (ISO, 2011; ISO, 2013).  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
User Acceptance Testing (UAT) uses surveys and
B.   Testing and Evaluation Procedure
|     |     |     |     |     |     |     |     |     | interviews  | guided  | by  | the  | Technology  | Acceptance  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ---- | ----------- | ----------- | --- |
•  Black-Box Testing
|     |     |     |     |     |     |     |     |     | Model  | (TAM)  | to  | assess  | user  | intentions  | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ------- | ----- | ----------- | ---- |
Employed  to  test  inputs  and  outputs  without  satisfaction  (Davis,  1989),  complemented  by
exposing system logic, using equivalence partitioning to  quantitative  analysis  through  statistical  review  of
ensure system robustness. Table 2 summarizes the Black
UAT data to derive actionable insights (Field, 2018).
Box testing conducted on key system functions, evaluating
Finally, implementation planning develops a phased
performance  based  on  functional  requirements  without  rollout  roadmap  including  pilot  stages,  full
| examining  | internal   | code,  | following  |        | the  3–5  | test           | case  |     |              |     |            |              |     |         |            |
| ---------- | ---------- | ------ | ---------- | ------ | --------- | -------------- | ----- | --- | ------------ | --- | ---------- | ------------ | --- | ------- | ---------- |
|            |            |        |            |        |           |                |       |     | deployment,  |     | training,  | stakeholder  |     | roles,  | and  risk  |
| guideline  | (Pressman  | &      | Maxim,     | 2014)  |           | for  balanced  |       |     |              |     |            |              |     |         |            |
management aligned with ISO standards (Kerzner,
| coverage  | and  | efficiency.  | Testing  |     | covered  | modules  |     |     | 2017).  |     |     |     |     |     |     |
| --------- | ---- | ------------ | -------- | --- | -------- | -------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
according to complexity, criticality, and coverage.  Together,  these  methods  ensure  the

development of a robust, user-friendly, and compliant
Table 2. Black Box Test Case Table  financial  management  system  that  improves

|             |                |     |              |        |               |           |     |     | budgeting,  |     | transparency,  | and         | efficiency  | in  | public  |
| ----------- | -------------- | --- | ------------ | ------ | ------------- | --------- | --- | --- | ----------- | --- | -------------- | ----------- | ----------- | --- | ------- |
| Function /  | Test Case IDs  |     | No. of Test  |        | Aligned with  |           |     |     |             |     |                |             |             |     |         |
|             |                |     |              |        |               |           |     |     | elementary  |     | schools,       | supporting  | predictive  |     | budget  |
| Module      |                |     |              | Cases  |               | 3–5 Rule  |     |     |             |     |                |             |             |     |         |
planning aligned with the schools’ improvement and
procurement plans.
| Login          | TC001–  |     |     | 5   |     | Yes  |     |     |     |     |                          |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
| Functionality  | TC003,  |     |     |     |     |      |     |     |     |     |                          |     |     |     |     |
|                |         |     |     |     |     |      |     |     |     | V.  | RESULTS AND DISCUSSIONS  |     |     |     |     |
TC029,
TC030
This chapter presents the presentation, analysis and
Role-Based  TC004,  3  Yes  discussions based on the methods employed to achieve the
| Access  | TC005,  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
study's objectives. The presentation is structured according to
| Control  | TC027  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the specific research objectives and includes a comprehensive
Dashboard  TC006– 5  Yes  explanation of the system’s design, the integration of linear
| Overview  | TC010  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regression analytics, and the results of multiple testing phases.

It also highlights how the predictive model supports budget
| Budget  | TC011– |     |     | 6   |     | Slightly  |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allocation optimization, how the system automates financial
| Management  | TC015,  |     |     |     | exceeds (✓  |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TC031  reporting aligned with DepEd policies, and how it performs in
critical
|     |     |     |     |     |     | module)  |     | terms of usability, functionality, and user acceptance.  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Expense  TC016– 6  Slightly  The  Budget  and  Financial  Information  System
Management  TC020,  exceeds (✓  (BFMIS) was developed using user-centered and AI-driven
TC032  related  linear  regression  analytics  that  automate  budget  creation,
module)
optimize MOOE allocation, and track expenditures.
| Report  | TC021– |     |     | 3   |     | Yes  |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Generation  | TC022,  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
132
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Fig. 5 presents the BFMIS dashboard, providing real-
| time  insights  | into  a  school’s  | financial  | status.  | It  enhances  |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------ | ---------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transparency through live data access, summary reports, and
audit logs. Predictive analytics aid budget planning, supporting
findings by Martinez and Reyes (2021). Audit logs and access
| controls  promote  | accountability,  |             | aligning   | with  Byol  | and  |     |     |     |     |     |     |     |     |     |
| ------------------ | ---------------- | ----------- | ---------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foygel’s           | (2023)  fraud    | prevention  | insights.  | Automated   |      |     |     |     |     |     |     |     |     |     |
reporting ensures timely compliance, as highlighted by Ali et

al. (2022 ).

Figure 7. View Expense Entries Page

|     |     |     |     |     |     |     | Figure  | 8   | showcases  |     | BFMIS’s  | predictive  |     | insight  |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- | --- | -------- | ----------- | --- | -------- |
feature, which uses linear regression to analyze historical data
|     |     |     |     |     |     | and  | recommend  | future  |     | budget  | allocations.  |     | By  comparing  |     |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | ------- | --- | ------- | ------------- | --- | -------------- | --- |
predicted (green) and actual (blue) values, the system enables
|     |     |     |     |     |     | data-driven  |     | decisions  | that  | enhance  |     | MOOE  | planning  | and  |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----- | -------- | --- | ----- | --------- | ---- |
resource optimization.
|     |     |     |     |     |     |     | Key  | benefits  | include  |     | smart  | recommendations  |     | that  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | -------- | --- | ------ | ---------------- | --- | ----- |
automatically suggest budget allocations based on trends, such
|     |     |     |     |     |     | as  | rising  | utility  | or  material  |     | costs,  | reducing  | guesswork  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------- | --- | ------- | --------- | ---------- | --- |

|     |     |     |     |     |     | (Alvarado  |     | &  Reyes,  | 2021);  |     | misalignment  |     | detection  | that  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------- | --- | ------------- | --- | ---------- | ----- |
Figure 5. BFMIS Dashboard
|     |     |     |     |     |     | highlights  |     | discrepancies  |     | between  | planned  |     | and  | predicted  |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | -------- | -------- | --- | ---- | ---------- |

|     |     |     |     |     |     | spending  |     | for  timely  | adjustments  |     | (Caballero  |     | et  al.,  | 2020);  |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | ------------ | --- | ----------- | --- | --------- | ------- |
Fig. 6 displays the BFMIS Add Budget page, where
proactive planning that empowers administrators to anticipate
users input project-specific budget details such as category,
amount, and fiscal year. Designed for school administrators  and respond to funding needs in evolving areas (Lee & Santos,
2022); evidence-based decisions that support budget proposals
and finance officers, the interface supports accurate, real-time
with data-backed insights (Delos Reyes & Bautista, 2023); and
data entry and easy updates. Its user-friendly layout enhances
adoption  and  reduces  errors  (Hussein  et  al.,  2022).  By  user-friendly  visuals  featuring  color-coded,  intuitive  charts
|     |     |     |     |     |     | that  | improve  | accessibility  |     | even  | for  | non-technical  |     | users  |
| --- | --- | --- | --- | --- | --- | ----- | -------- | -------------- | --- | ----- | ---- | -------------- | --- | ------ |
replacing manual methods, it improves data consistency and
|     |     |     |     |     |     | (Tolentino  |     | &  Uy,  | 2021).  | Overall,  | this  | feature  | transforms  |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------- | --------- | ----- | -------- | ----------- | --- |
compliance (Abubakar & Sulaiman, 2021) while supporting
better  financial  planning  and  accountability  in  public  BFMIS  into  a  practical  AI-powered  tool  for  transparent,
education (Delos Santos & Gomez, 2023).    efficient, and strategic school budgeting.

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 6. BFMIS Add Budget Page
|                                                  |     |     |     |     |     |     |     | Figure 8. MOOE Prediction Page  |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
| Fig. 7 shows the View Expense Entries module of  |     |     |     |     |     |     |     |                                 |     |     |     |     |     |     |
Figure 9 presents the BFMIS Budget and Expense
BFMIS, which provides a clear summary of recorded expenses
Report page, summarizing allocations, actual spending, and
by project and fiscal year. It displays key details like category,
utilization rates across MOOE categories from January 1 to
budget, actual spending, percentage used, and remarks. Users
can  filter,  update,  or  delete  entries,  with  color-coded  May 15, 2025. This real-time report supports accountability
|     |     |     |     |     |     | and  | informed  | decision-making  |     |     | by  showing  |     | how  | funds  are  |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ---------------- | --- | --- | ------------ | --- | ---- | ----------- |
percentages aiding quick assessment. Designed for usability
being used.
and transparency (Hussein et al., 2022), the module promotes
accurate  expense  tracking,  reduces  errors,  and  aligns  with  The  report  includes  columns  for  School  Year,
|                   |             |              |                 |     |      | Category,  |     | Allocated  | Budget,  |     | Total  | Expenses,  |     | and  %  |
| ----------------- | ----------- | ------------ | --------------- | --- | ---- | ---------- | --- | ---------- | -------- | --- | ------ | ---------- | --- | ------- |
| DepEd  financial  | guidelines  | for  better  | accountability  |     | and  |            |     |            |          |     |        |            |     |         |
Utilization. For instance, 100% spending in the Graduation
MOOE management.
Program reflects full budget use, while mid-range figures in

other programs indicate ongoing or scheduled disbursements.
|     |     |     |     |     |     |              | The  | %  Utilization      |           | metric—calculated  |           |                 | by  | dividing   |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------------- | --------- | ------------------ | --------- | --------------- | --- | ---------- |
|     |     |     |     |     |     | expenses     | by   | the  budget—offers  |           |                    | a  quick  | view            | of  | financial  |
|     |     |     |     |     |     | efficiency,  |      | helping             | identify  | over-              | or        | under-utilized  |     | funds.     |
Automated calculations and clear visualizations reduce manual
errors and promote transparency.
133
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Aligned with studies on digital finance tools (Gao et  Report  Auto- DomPDF,  All users
al., 2021; Tolentino & Uy, 2021), this page enhances budget
|     |     |     |     |     |     |     | Generator  | generates  |     | PhpSpreadshe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------ | --- | --- | --- |
tracking, enables timely reallocations, and strengthens school
|     |     |     |     |     |     |     |     | PDF/Excel  |     | et  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
financial governance.
|     |     |     |     |     |     |     |     | reports  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |          |     |     |     |     |     |

Figure 10 presents the comparison of current-year
budget allocations and the system’s predicted values for the
next cycle. Notable increases were observed in categories like
|     |     |     |     |     |     |     | Electricity           | (+9.83%)  | and     | Fidelity    | Bond  (+66.67%)           |             | due  to  |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --------- | ------- | ----------- | ------------------------- | ----------- | -------- |
|     |     |     |     |     |     |     | historical            | spending  | trends  | and         | prior  underestimations.  |             | ICT      |
|     |     |     |     |     |     |     | Program  predictions  |           | showed  | minimal     | variance,                 | indicating  |          |
|     |     |     |     |     |     |     | stable  expenditure.  |           | Table   | 4  details  | these  results,           | including   |          |

absolute differences and percentage changes, confirming the

Figure 9. Budget and Expense Report Page  accuracy of the Linear Regression model.
|     | Table 3 outlines the core functional modules of the  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BFMIS, each addressing key financial management needs in
public schools while promoting automation and data-driven
decision-making. Budget Allocation Module, built with PHP
and MySQL, this module allows structured input and secure
storage of MOOE data, enhancing accuracy and accessibility
| (Abubakar  | &   | Sulaiman,  | 2021).  | AI-Powered  |     | Prediction  |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Module, developed in Python using Scikit-learn, it uses linear
regression to forecast future budget needs, enabling proactive
and strategic planning (Delos Santos & Gomez, 2023). Budget
Visualization Module uses Chart.js and JSON to display real-
time comparisons of planned vs. actual spending, supporting
transparency and informed decision-making (Hussein et al.,
| 2022).  | Automated  | Reporting  | Module,  |     | generates  | PDF  and  |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | -------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |

Excel reports via DomPDF and PhpSpreadsheet, streamlining

| compliance and reducing  |     |     | manual  | work (Ramírez-Alujas &  |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 10. Actual vs. Predicted MOOE Allocations per Category

| Dassen,  | 2020).  | Together,  | these  | modules  | demonstrate  | how  |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | ------ | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
To evaluate the model’s reliability, the following
| BFMIS  | enhances  | financial  | transparency,  |     | efficiency,  | and  |     |     |     |     |     |     |     |
| ------ | --------- | ---------- | -------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
responsiveness in public elementary schools.  regression metrics such as Mean Absolute Error (MAE), Root
Mean Square Error (RMSE) and R² Score were computed.
To address Objective No. 2, BFMIS includes an AI-
The results presented in Table 4 shows that the model
| driven  reporting  |         | module  | that  applies  | Linear  | Regression  | to        |            |                   |     |            |           |            |     |
| ------------------ | ------- | ------- | -------------- | ------- | ----------- | --------- | ---------- | ----------------- | --- | ---------- | --------- | ---------- | --- |
|                    |         |         |                |         |             |           | maintains  | high  predictive  |     | accuracy,  | with  an  | R²  value  | of  |
| forecast           | future  | MOOE    | allocations.   | This    | machine     | learning  |            |                   |     |            |           |            |     |
92.81%, indicating that most of the variance in the target
| method  | analyzes  | historical  | spending  |     | trends  | to  predict  |     |     |     |     |     |     |     |
| ------- | --------- | ----------- | --------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
budget can be explained by historical data. After generating
| category-wise  | budget  | needs  | for  | the  next  | fiscal  | year.  As  |     |     |     |     |     |     |     |
| -------------- | ------- | ------ | ---- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
the predictions, the system automatically populates MOOE
supported by Widanaputra et al. (2022), linear regression is
effective for educational budget forecasting, enabling data- expenditure  logs,  variance  analysis  reports,  and  DepEd-
compliant financial summaries, all downloadable in PDF and
driven and proactive financial planning.
Excel formats as shown in Figure 9. This feature aligns with

Table 3: Core Features of the Developed BFMIS  reporting  standards  required  by  DepEd  and  significantly
|     |     |     |     |     |     |     | reduces manual report generation time.  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |

| Module  |     | Description  |     | Key  | Stakeholders  |     |     |     |     |     |     |     |     |
| ------- | --- | ------------ | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 4: Regression Model Performance
Benefitted
|             |     |              | Technologies  |     |                |     |                |     |            |     |                              |     |     |
| ----------- | --- | ------------ | ------------- | --- | -------------- | --- | -------------- | --- | ---------- | --- | ---------------------------- | --- | --- |
|             |     |              |               |     |                |     | Metric         |     | Value      |     | Interpretation               |     |     |
| Budget      |     | Inputs and   | PHP, MySQL    |     | School Heads,  |     |                |     |            |     |                              |     |     |
| Allocation  |     | categorizes  |               |     | Finance        |     |                |     |            |     |                              |     |     |
|             |     |              |               |     |                |     | Mean Absolute  |     | ₱1,532.75  |     | Indicates low average error  |     |     |
MOOE
|     |     |     |     |     |     |     | Error (MAE)  |     |     |     | between predicted and actual  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ----------------------------- | --- | --- |
values.
| AI-Powered   |     | Predicts next  | Python,       |       | School Heads,   |        |               |     |            |     |                               |     |     |
| ------------ | --- | -------------- | ------------- | ----- | --------------- | ------ | ------------- | --- | ---------- | --- | ----------------------------- | --- | --- |
| Prediction   |     | year’s budget  | Scikit-learn  |       | Finance         |        |               |     |            |     |                               |     |     |
|              |     | via Linear     |               |       |                 |        | Root Mean     |     | ₱2,126.84  |     | Confirms minimal large        |     |     |
|              |     |                |               |       |                 |        | Square Error  |     |            |     | prediction errors, enhancing  |     |     |
|              |     | Regression     |               |       |                 |        | (RMSE)        |     |            |     | reliability.                  |     |     |
| Expenditure  |     | Monitors       | Chart.js,     |       | School Heads,   |        |               |     |            |     |                               |     |     |
|              |     |                |               |       |                 |        | R² Score      |     | 0.9281     |     | High explanatory power—       |     |     |
| Tracker      |     | actual vs.     |               | JSON  |                 | Finan  |               |     |            |     | 92.81% of variance is         |     |     |
|              |     | planned        |               |       | ce, DepEd,      |        |               |     |            |     | accounted for by the model.   |     |     |
Stakeholders
134
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

|     |                                                  |     |     |     |     |     |     |     | Quality  | password    |     |     | Agree  |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --- | ------ |
|     | Black-box testing involved 37 test cases (TC001– |     |     |     |     |     |     |     |          | protection  |     |     |        |
TC037)  assessing  core  modules,  user  access,  validation,
|     |     |     |     |     |     |     |     |     | Ease of Use  | Ease of retrieving  | 4.63  4.61  |     | Strongly  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | ----------- | --- | --------- |
responsiveness, and security. Conducted by IT professionals
|     |     |     |     |     |     |     |     |     |     | reports and data  |     |     | Agree  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------ |
and developers, results showed strong compliance, with most

testers reporting full success. Only one tester reported four
failures related to UI responsiveness (TC010), missing field  Perceived  Enhances  4.67  4.51  Strongly
|     |     |     |     |     |     |     |     |     | Usefulness  | transparency in  |     |     | Agree  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | --- | --- | ------ |
validation (TC012), incorrect feedback for over-budget entries  financial reports
(TC017), and display issues when the budget is zero (TC020).
| Additional  |     | issues included input sanitization  |     |     |     |     | vulnerabilities  |     |             |                    |             |     |           |
| ----------- | --- | ----------------------------------- | --- | --- | --- | --- | ---------------- | --- | ----------- | ------------------ | ----------- | --- | --------- |
|             |     |                                     |     |     |     |     |                  |     | System      | Dashboard          | 4.67  4.51  |     | Strongly  |
|             |     |                                     |     |     |     |     |                  |     | Features &  | provides relevant  |             |     | Agree     |
(TC030), UI inconsistencies across roles, and acceptance of
|          |          |     |               |     |        |       |        |          | Functionalit | and clear financial  |     |     |     |
| -------- | -------- | --- | ------------- | --- | ------ | ----- | ------ | -------- | ------------ | -------------------- | --- | --- | --- |
| invalid  | numeric  |     | data.  These  |     | align  | with  | prior  | studies  |              |                      |     |     |     |
|          |          |     |               |     |        |       |        |          | y            | insights             |     |     |     |
emphasizing strong input validation and consistent UI design.

Despite minor issues, the system showed no major bugs or  User  Likely to use the  4.53  4.51  Strongly
crashes, confirming it is functionally complete and ready for  Satisfaction  system regularly  Agree
deployment with slight improvements in validation and UI  &  and satisfied with
| responsiveness.  |                                    |     |     |     |     |     |     |     | Acceptance  | performance  |     |     |     |
| ---------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --- | --- |
|                  | •  User Feedback and Observations  |     |     |     |     |     |     |     |             |              |     |     |     |
“The system works as intended and performs in accordance  In  Fig.  11,  Implementation  Plan,  the  BFMIS  is
with its expected features. It passed all necessary functional  recommended to be implemented from June 2025 to December
2026 through a phased rollout to ensure readiness, training,
| tests,  | making  | it  | suitable  | and  ready  | for  | deployment.  |     | The  |     |     |     |     |     |
| ------- | ------- | --- | --------- | ----------- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- |
interface is user-friendly, easy to navigate, and responds well  and policy alignment. Phase 1 (June–July 2025) focuses on
to defined inputs.“  system finalization, stakeholder consultation, and pilot school
|     |     |     |     |     |     |     |     |     | selection.  | Phase  2  (July–August  | 2025)  | involves  | creating  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------- | ------ | --------- | --------- |
The evaluation of user acceptance and behavioral
intention to use the (BFMIS) was conducted using the (TAM)  training  materials  and  conducting  sessions  to  build  user
through structured (UAT) with school administrators, financial  capacity. In Phase 3 (August–October 2025), the system will
|            |     |             |            |     |           |     |                |     | go  live  | in  pilot  schools,  | with  ongoing  | feedback  | and  |
| ---------- | --- | ----------- | ---------- | --- | --------- | --- | -------------- | --- | --------- | -------------------- | -------------- | --------- | ---- |
| officers,  |     | and  DepEd  | auditors,  |     | focusing  |     | on  perceived  |     |           |                      |                |           |      |
usefulness, perceived ease of use, and attitude toward using  adjustments based on monitoring. Phase 4 (October 2025–
the system.  February  2026)  will  see  the  refined  system  deployed
  nationwide,  supported  by  policy  integration  and  helpdesk
As  shown  in  Table  5,  the  Budget  and  Financial  activation. Finally, Phase 5 (January–December 2026) ensures
Management  Information  System  (BFMIS)  received  sustainability  through  continuous  updates,  integration  with
consistently high ratings across all quality dimensions based  DepEd  systems  (BEIS  and  EMIS),  and  a  full  impact
assessment to guide long-term adoption.
on user evaluations. Users strongly agreed on the system's
| accuracy, functionality, and security, with the highest rating  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
given to secure access and user role management (Mean =
4.70), affirming the system’s reliability in protecting sensitive
financial data (Byol & Foygel, 2023). They found the system
easy to navigate, input data, and retrieve reports (Weighted
Mean = 4.61), reflecting its high usability and user-friendly
| interface  | design  |     | (Hussein  | et  al.,  | 2022).  | Respondents  |     | also  |     |     |     |     |     |
| ---------- | ------- | --- | --------- | --------- | ------- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
acknowledged the system’s role in enhancing transparency,
| efficiency,  |     | and   | decision-making  |             | in  | budget  | management  |       |     |     |     |     |     |
| ------------ | --- | ----- | ---------------- | ----------- | --- | ------- | ----------- | ----- | --- | --- | --- | --- | --- |
| (Weighted    |     | Mean  | =  4.51),        | consistent  |     | with    | findings    | from  |     |     |     |     |     |
Delima and Tejero (2022). Key features such as the dashboard,
| AI  | predictions,  |     | and  policy  | compliance  |     | were  | positively  |     |     |     |     |     |     |
| --- | ------------- | --- | ------------ | ----------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
received, with dashboard clarity rated highest (Mean = 4.67),
supporting better financial insights (Tolentino & Uy, 2021).
Additionally, users expressed high satisfaction and a strong
likelihood of regular use (Weighted Mean = 4.51), indicating

| readiness for adoption and long-term integration, in line with  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the  Technology  Acceptance  Model  (Venkatesh  &  Davis,  Figure 11. BFMIS Phased Implementation Plan
2000).  The  low  standard  deviation  across  all  categories
As shown in Table 6, the Risk Mitigation Strategies
| (ranging  | from  | 0.47  | to  0.62)  | signals  | consistent  |     | agreement  |     |     |     |     |     |     |
| --------- | ----- | ----- | ---------- | -------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
ensures a structured, scalable, and user-centered approach to
| among  | respondents,  |     | validating  |     | the  system’s  |     | effectiveness,  |     |     |     |     |     |     |
| ------ | ------------- | --- | ----------- | --- | -------------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
trustworthiness, and alignment with user needs.  transforming  financial  management  in  public  elementary
schools. These mitigation strategies reflect a comprehensive

|     |     |     |     |     |     |     |     |     | approach  | to  implementation  | planning,  | incorporating  | both  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | ---------- | -------------- | ----- |
Table 5. Summary of Evaluation Results for the Budget and Financial
Management Information System (BFMIS)  technical safeguards and user-centered practices in line with
|            |     |                     |            |       |            |       |           |     | global standards for ICT deployment in education (UNESCO,  |     |     |     |     |
| ---------- | --- | ------------------- | ---------- | ----- | ---------- | ----- | --------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
| Dimension  |     | Highest-Rated       |            | Mea   | Weighte    |       | Verbal    |     | 2022).                                                     |     |     |     |     |
|            |     |                     | Criterion  |       | n  d Mean  |       | Interpret |     |                                                            |     |     |     |     |
|            |     |                     |            |       |            |       | ation     |     |                                                            |     |     |     |     |
| System     |     | Secure user role &  |            | 4.70  |            | 4.62  | Strongly  |     |                                                            |     |     |     |     |
135
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137

Table 6. Risk Mitigation Strategies  The  implementation  framework  ensures  scalability  and

regulatory compliance. Its phased structure and risk controls
Identified Risk  Mitigation Plan  promote a smooth, sustainable rollout.
| Resistance to change  |     |     |     | Early orientation and stakeholder  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
engagement
|                          |     |     |     |                                      |     |     |     | C.  Recommendations  |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ------------------------------------ | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| Low digital literacy in  |     |     |     | Tiered training support and digital  |     |     |     |                      |     |     |     |     |     |     |     |
To support the broader deployment and sustainability
|     | some schools  |     |     |     | mentoring  |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of the BFMIS, it is recommended that the Department of
| Data privacy and system  |     |     |     | Secure role-based access and  |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Education (DepEd) formally adopt and integrate the system
|     | breaches  |     |     | encryption protocols  |     |     |     |            |           |         |     |            |             |     |          |
| --- | --------- | --- | --- | --------------------- | --- | --- | --- | ---------- | --------- | ------- | --- | ---------- | ----------- | --- | -------- |
|     |           |     |     |                       |     |     |     | into  the  | national  | school  |     | budgeting  | framework.  |     | Regular  |
Budget inaccuracies or  Continuous model validation and  training  sessions  should  be  conducted  alongside  the
prediction discrepancies  override options  establishment of a dedicated help desk to provide technical
| Network or device  |                  |     |     | Offline-first design and minimum  |     |     |     |                        |     |     |     |               |            |     |          |
| ------------------ | ---------------- | --- | --- | --------------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | ------------- | ---------- | --- | -------- |
|                    |                  |     |     |                                   |     |     |     | support and ensure us  |     |     | er  | proficiency.  | Quarterly  |     | updates  |
|                    | incompatibility  |     |     | hardware specs                    |     |     |     |                        |     |     |     |               |            |     |          |
must be implemented to maintain system security and the
|     |     |     |     |     |     |     |     | accuracy of AI-powered forecasts.  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Future development should ensure integration with
|     | VI.  | SUMMARY, CONCLUSIONS, AND  |     |     |     |     |     |           |        |            |     |       |           |      |           |
| --- | ---- | -------------------------- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | --- | ----- | --------- | ---- | --------- |
|     |      |                            |     |     |     |     |     | existing  | DepEd  | platforms  |     | such  | as  BEIS  | and  | EMIS  to  |
RECOMMENDATIONS
streamline data flow and reduce redundancy. Expanded pilot
implementations across schools with varying ICT capacities
A.  Summary    are  encouraged  to  evaluate  system  adaptability  in  diverse
contexts. Within 12 months of deployment, a comprehensive
|     | The  | BFMIS  | was  | designed  | to  address  | manual  |     |     |     |     |     |     |     |     |     |
| --- | ---- | ------ | ---- | --------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
impact assessment should be conducted to evaluate system
inefficiencies in budgeting by offering digital, AI-driven tools
for  transparency  and  decision-making.  The  system’s  core  performance, user satisfaction, and improvements in financial
accuracy.
modules are the Budget Allocation Module, which facilitates
Lastly, continuous risk monitoring must be embedded
structured input of MOOE items based on specific categories.
AI-Powered  Prediction  Module  that  utilizes  a  Linear  into system operations to address emerging challenges and
ensure long-term success. Regular assessments and mitigation
Regression algorithm to estimate future MOOE allocations.
|     |     |     |     |     |     |     |     | strategies  | will  | help  | sustain  | BFMIS  | effectiveness  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | -------- | ------ | -------------- | --- | ---- |
The model achieved the accuracy of R² = 0.9281,
Mean Absolute Error (MAE) = ₱1,532.75, Root Mean Square  institutional trust.
Error (RMSE) = ₱2,126.84. Expenditure Tracker displays real-
|       |           |         |          |             |        |          |     |     |     | VII.  | ACKNOWLEDGMENT  |     |     |     |     |
| ----- | --------- | ------- | -------- | ----------- | ------ | -------- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- |
| time  | spending  | versus  | planned  | allocation  | using  | dynamic  |     |     |     |       |                 |     |     |     |     |
summaries and tables, and the Automated Reporting Module
generates DepEd-compliant PDF and Excel reports for easier
  First and foremost, I would like to extend my gratitude to the
audit and submission.  Almighty God for giving me the strength and perseverance to
A total of 37 black-box test cases were conducted to validate
make it through this journey. His guidance helped me through
| functionality,  |     | usability,  | data  | accuracy,  | and  security,  |     | all  of  |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | ----- | ---------- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
every challenge. To my parents Cenon and Merly Santiago,  for
which were passed successfully.  love and support. To my siblings, Eric, Erwin and Mercy, thank
The User Acceptance Evaluation shows that users
you for always being there with love, encouragement, and
highly rated BFMIS across five key areas on a 5-point scale:
guidance. Dr. Mario R. Briones, the University President of
System Quality (4.47), Ease of Use (4.46), Usefulness (4.37),  Laguna State Polytechnic University under his leadership and
Features (4.37), and Satisfaction (4.37). These scores indicate
|     |     |     |     |     |     |     |     | support.  | Dr.  Mia  | V.  | Villarica,  | the  | Associate  | Dean  | of  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ----------- | ---- | ---------- | ----- | -------- |
the system is reliable, easy to use, valuable, well-equipped,
|     |     |     |     |     |     |     |     | College  | of  Computer  |     | Studies  | –  Santa  | Cruz  | Campus,  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | -------- | --------- | ----- | -------- | ---- |
and well-liked, suggesting strong user approval and readiness
researcher’s thesis adviser for guidance and support in the
for adoption.  study. Mr. Mark P. Bernardino, the Subject Specialist of the
To support deployment, a five-phase implementation
College of Computer Studies, for the professional guidance and
plan was proposed: pre-implementation, training, pilot rollout,
support.Ms. Maria Laureen B. Miranda, the Technical Editor of
full deployment, and sustainability. Risk mitigation strategies  the College of Computer Studies and Research Coordinator for
were included to address issues such as digital skill gaps,
the valuable guidance and support in the study. Mr. Jhon Jhon
system resistance, forecasting challenges, and cybersecurity
|     |     |     |     |     |     |     |     | P.  Zotomayor,  |     | for  patiently  |     | checking  | the  | grammar  | of  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | --------- | ---- | -------- | -------- |
concerns.  manuscript.  Mr. Edward S.  Flores,  the Statistician, for  his

|     |     |     |     |     |     |     |     | expertise.  | Lastly,  | the  | researcher  | is  | deeply  | grateful  | to  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---- | ----------- | --- | ------- | --------- | -------- |
B.  Conclusions  College  of  Computer  Studies  faculty  member  for  their
invaluable knowledge and insightful guidance.
| The BFMIS successfully achieved its goals, offering  |     |     |     |     |     |     | a   |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reliable digital solution that automates budgeting, improves
accuracy, and promotes financial accountability. Its use of  VIII.  REFERENCES
Linear Regression enhanced the predictive quality of MOOE
forecasts, while the system's user interface, role-based access,

and real-time data display supported positive user experiences.  [1]  Abubakar, M., & Sulaiman, A. (2021). Manual vs. digital
All  modules  performed  as  expected  based  on  testing.  budgeting:  Comparative  study  on  financial  record
While minor improvements in UI responsiveness and input  accuracy  in  public  institutions.  Journal  of  Public
Administration and Finance, 9(2), 45–59.
validation were noted, the system is technically robust and
Ali, M., Reyes, G., & Martinez, F. (2022). Automated
| ready for implementation.  |     |     |     |     |     |     |     | [2]        |     |              |             |     |     |         |             |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | ----------- | --- | --- | ------- | ----------- |
|                            |     |     |     |     |     |     |     | reporting  |     | and  policy  | compliance  |     | in  | public  | education.  |
136
| © 2024-2027, IJARCS All Rights Reserved      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Santiago, Rose Lyn T. et al, International Journal of Advanced Research in Computer Science, 16 (3), May-June 2025, 128-137
International Journal of Educational Technology, 14(3), [21] Lee, D., & Santos, M. (2022). Proactive financial
88–95. planning in public institutions. Fiscal Planning Journal,
[3] Almazan, J. (2023). MOOE budget challenges in 14(1), 31–40.
Philippine public schools. Philippine Journal of [22] Martinez, E., & Reyes, J. (2021). Use of predictive
Educational Management, 7(1), 22–31. analytics in school budget planning. Journal of Smart
[4] Amado, R., Dela Cruz, N., & Villanueva, P. (2025). Education, 5(1), 48–56.
Participatory budgeting in school management: A [23] Office of Procurement Regulation. (2021). Public
stakeholder approach. Journal of Educational Governance, procurement best practices. https://oprtt.org
5(1), 13–21. [24] Pressman, R. S., & Maxim, B. R. (2014). Software
[5] Beronibla, C. (2024). Promoting transparency through engineering: A practitioner’s approach (8th ed.).
inclusive budgeting. Journal of School Financial Planning, McGraw-Hill Education.
6(2), 39–47. [25] Ramírez-Alujas, Á., & Dassen, N. (2020). Public sector
[6] Beronibla, C. (2024). Promoting transparency through innovation and open government. Inter-American
inclusive budgeting. Journal of School Financial Planning, Development Bank.
6(2), 39–47.
[26] Roustaei, M. (2024). Predictive modeling using linear
[7] Caballero, S., Torres, L., & Ramos, J. (2020). Detection regression for limited data. Financial Analytics Journal,
of budget misalignments in educational finance. Journal 8(1), 44–52.
of Educational Finance, 12(2), 119–126. [27] Smith, A., & Jones, P. (2019). Monitoring and evaluating
[8] Davis, F. D. (1989). Perceived usefulness, perceived ease school implementation plans. International Journal of
of use, and user acceptance of information technology. Education Management, 10(4), 55–63.
MIS Quarterly, 13(3), 319–340. [28] Sun, L., & Li, J. (2023). Black box testing in family
[9] Delima, A., & Tejero, M. (2022). User satisfaction and financial systems. Journal of Information Security &
system usability in school financial management systems. Testing, 9(2), 72–80.
Philippine Journal of Educational ICT, 10(1), 24–35. [29] Tolentino, A., & Uy, M. (2021). Effective financial
[10] Delos Reyes, L., & Bautista, R. (2023). Evidence-based visualization for school reporting. Philippine Journal of
budgeting in Philippine schools. Journal of Education Educational Innovation, 4(3), 67–74.
Policy and Management, 7(1), 58–66. [30] Tsakiridis, L., Petrova, N., & Campos, M. (2023). Data
[11] Delos Santos, K., & Gomez, R. (2023). Forecasting tools integration between MySQL and Python for educational
in school financial planning. Education and Technology analytics. Journal of Data Engineering in Education, 7(2),
Journal, 8(4), 77–85. 93–101.
[12] Demas, A., & Arcia, G. (2015). What matters most for [31] UNESCO. (2022). ICT in education: Guidelines for
school autonomy and accountability? A framework paper. national policy and implementation. United Nations
World Bank. Educational, Scientific and Cultural Organization.
[13] Department of Education Victoria. (2020). Annual [32] Upadhyaya, R. (2016). Challenges in financial digital
implementation plan: Guidelines and requirements. transformation in education. Journal of Educational
Melbourne: Department of Education. Finance Reform, 2(2), 22–29.
[14] Faheem, M., Abdullah, R., & Zhang, Y. (2024). The role [33] Venkatesh, V., & Davis, F. D. (2000). A theoretical
of AI in predictive analytics for finance. International extension of the Technology Acceptance Model: Four
Journal of Artificial Intelligence Applications, 16(2), 34– longitudinal field studies. Management Science, 46(2),
43. 186–204.
[15] Gao, Y., Lin, X., & Hu, M. (2021). Digital financial [34] Wang, Y., Liu, Q., & Zhao, H. (2020). SQLFlow:
management in public schools. Journal of Educational Building predictive pipelines with SQL and AI
Innovation and Finance, 9(3), 92–100. integration. Proceedings of the IEEE Data Science
[16] Gaspar, R., De Luna, A., & Borja, K. (2022). The role of Conference, 89–97.
MOOE in student welfare and teacher development. [35] Wasserbacher, M., & Spindler, M. (2022). Applying
Philippine Journal of Basic Education, 11(1), 17–27. regression models in digital financial systems. Journal of
[17] Harshitha, S., Anand, D., & Mehta, V. (2025). AI-based Computational Finance, 12(1), 25–36.
budgeting systems in education: A review. Journal of AI [36] Widanaputra, A., Santosa, D., & Aisyah, N. (2022).
in Education, 5(2), 59–67. Forecasting educational budgets using linear regression.
[18] Hargreaves, A., & Fullan, M. (2015). Professional capital: Journal of Education Finance and Analytics, 5(3), 34–45.
Transforming teaching in every school. Teachers College [37] Zuhro, S., Kurniawan, A., & Prasetya, T. (2024).
Press. Overcoming barriers in school-based financial
[19] Hussein, R., Alonto, F., & De Guzman, L. (2022). digitization. Journal of Educational Transformation, 8(1),
13–22.
Evaluating financial systems' interface design in public
education. Journal of ICT in Public Sector, 6(3), 101–109.
[20] IBM. (n.d.). What is linear regression?. IBM Knowledge
Center. https://www.ibm.com/topics/linear-regression
© 2024-2027, IJARCS All Rights Reserved 137