---
conversion_metadata:
  converted_at: "2026-07-21T09:27:57Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yadav et al.pdf"
  source_pdf_sha256: "f4b671d269de872cb4d7632cc026d2f5cfb216736392686e0230241d8beb9ebb"
  page_count: 9
  markdown_char_count: 44312
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

AI Wealth Navigator: An Integrated 
Platform for Smart Budgeting, Financial 
Learning, and Personalized Policy Guidance

Akash Yadav1, R Surya Prakash2, Safa Mohamed Iqubal3*,

Mahder Girmay Gebremicahea4

1, 2, 3Department of Networking and Communications, Faculty of Engineering &

Technology, SRM

Institute of Science and Technology, Kattankulathur, India.  
4Department: School of Electrical and Computer Engineering, Ethiopean Institute

of Technology, Mekelle, Mekelle University, Ethiopia

Email: ay7507@srmist.edu.in, sr9071srmist.edu.in, safam@srmist.edu.in*,

Mahder.girmay@mu.edu.et

Abstract-  Despite  the  widespread  availability  of  personal  finance  applications, 
consumers  still  encounter  disjointed  financial  ecosystems  in  which  knowledge  of 
government  policies,  financial  education,  and  budgeting  are  all  compartmentalized. 
Through  three  seamlessly  integrated  modules,  this  paper  introduces  AI  Wealth 
Navigator,  a  unified,  intelligent  financial  platform  that  fills  these  gaps:  (1)  a  financial 
learning roadmap that adjusts to user progress and literacy levels; (2) a clever AI-driven 
budget tracker with real-time visual insights, receipt scanning, and personalized savings 
alerts; and (3) a policy recommendation engine that uses large language models to suggest 
pertinent  government  schemes  and  benefits  based  on  individual  profiles.  For  safe, 
the  system  architecture  makes  use  of 
scalable,  and  responsive  performance, 
contemporary web technologies, including Next.js, Supabase, Prisma, Arcjet, and Inngest. 
Hybrid  data  APIs  and  Gemini  LLMs  improve 
inclusion,  decision-making,  and 
customisation.  The  platform  promotes  economic  inclusion,  financial  literacy,  and  more 
prudent  personal  financial  practices,  all  of  which  are  in  line  with  UN  Sustainable 
Development Goals (SDGs) 1, 4, 8, and 10. The system concept, important implementation 
elements, and its potential as a game-changing tool in the world of digital finance are all 
presented in this article

Keywords:  The  Sustainable  Development  Goals,  Intelligent  Budgeting,  Financial 
Literacy, AI Policy Suggestion, Gemini LLM, Supabase, Personal Finance Platform, Receipt 
OCR, Inngest, Web-Based Financial Assistant

Introduction: 
Users  frequently  suffer  with  disjointed  solutions  that  don't  offer  a  cohesive 
approach  to  budgeting,  financial  education,  and  policy  navigation  in  the  quickly 
changing field of personal finance management. Even though there are many finance 
applications  available,  many  platforms  are  still  fragmented,  concentrating  on  either 
simple  budgeting  or  discrete  educational  materials  rather  than  providing  a  full 
solution that incorporates all facets of financial decision-making. Users are unable to 
maximize  their  financial  well-being due to  inefficiencies  caused  by  the  absence  of  a 
consistent, tailored experience across platforms.

This  problem  is  made  worse  in  India  by  a  lack  of  financial  literacy.  Recent 
research indicates that a sizable section of the populace does not have access to high-

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 2 -->

quality financial education, which hinders their capacity to  make wise choices about 
government  assistance,  investments,  and  savings.  In  order  to  educate  themselves, 
users also frequently browse through a variety of websites, forums, and publications; 
but,  because  these  resources  are  unstructured,  it  can  be  challenging  to  monitor 
progress  and  meet  financial  objectives.  Because  of  this, a lot  of  people  still manage 
their  money  using  antiquated,  inefficient  techniques,  which  contributes  to  ongoing 
financial instability

to  solve

In  order

these  problems,  we  present  AI  Wealth  Navigator,  a 
comprehensive  platform  that  combines  three  essential  modules  to  optimize  the 
financial management process: (1) an adaptive financial learning roadmap that tracks 
and  advances  in  tandem  with  the  user's  knowledge;  (2)  an  intelligent  AI-powered 
budget tracker that offers real-time insights, receipt scanning, and customized alerts; 
and  (3)  a  policy  recommendation  engine  that  makes  recommendations  based  on  the 
user's  profile  and  requirements.  The  platform  makes  use  of  state-of-the-art 
technologies,  such  as  Next.js,  Supabase,  Prisma,  and  Gemini  LLMs,  to  provide 
security, scalability, and tailored recommendations.

AI  Wealth  Navigator  seeks  to  streamline  personal  money  management  by 
combining these functions into a single platform. This will enable users to track their 
spending, enhance their financial literacy, and access pertinent government programs, 
all of which will help them make better financial decisions.

Literature Survey: 
Recent years have seen a surge in the use of AI in personal money management as 
numerous  research  have  shown  how  it  may  improve  policy  suggestions,  financial 
education, and budgeting. In the field of financial education, Patel et al. (2023) talked 
about  how  AI-powered  platforms  can  help  advance  financial  literacy  by  providing 
financial  tools  and  individualized  learning  paths.  According  to  their  findings,  AI-
based solutions may be able to close the knowledge gap and empower people in low-
income communities to make wise investment and savings choices.

Similar  to  this,  Kumar  et  al.  (2023)  investigated  developments  in  AI-powered 
budgeting tools and presented an intelligent budgeting system that adjusts to the user's 
spending  habits  and 
financial  objectives.  The  system's  use  of  dynamic 
information  enhanced  user  engagement  and 
recommendations  and  real-time 
strengthened  financial  discipline.  Additionally,  Singh  et  al.  (2024)  investigated  how 
AI-driven receipt scanning and classification may increase the accuracy of budgeting, 
emphasizing  the  drawbacks  of  conventional  manual  techniques  and  the  notable 
decrease in human error.

The  potential  of  large  language  models  (LLMs)  to  offer  tailored  government 
scheme  recommendations  has  been  investigated  in  a  number  of  studies.  Based  on 
users'  financial  profiles,  Lee  et  al.  (2023)  created  a  system  that  employed  AI  to 
suggest  social  security  benefits  and  subsidies.  The  significance  of  context-specific 
advice that complement the user's present financial circumstances and objectives was 
emphasized by this study. Furthermore, research by Sharma et al. (2024) highlighted 
how  AI  systems  must  take  regional  differences  in  policy  recommendations  into 
consideration 
that  consumers  obtain  pertinent  and  correct 
recommendations.

to  guarantee

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 3 -->

A  significant  worry  has  also  been  the  privacy  and  security  of  financial 
applications.  According  to  a  study  by  Gupta  et  al.  (2024),  AI  was  used  to  integrate 
secure  transaction  systems  into  financial  platforms  in  order  to  identify  fraudulent 
activity  and  guarantee the  security  of  private  financial information.  The  significance 
of  multilayer  security  measures  in  applications  involving  financial  transactions  and 
personal data was brought to light by their work.

System Architecture: 
AI Wealth Navigator consists of five core components:

  Frontend  (UI):  Built  with  Next.js  and  Tailwind  CSS,  providing  a 
responsive, interactive user experience for budgeting, financial learning, and 
policy suggestions.

  Backend  &  API:  Uses  Supabase  and  Prisma  for  data  management,  with

Inngest handling automated tasks and notifications.

  AI  Insights:  Powered  by  Gemini  LLM  for  personalized  financial

recommendations and adaptive learning.

  Policy Engine: Suggests relevant government schemes using AI and hybrid

data APIs based on user profiles.

  Security: Arcjet ensures secure data handling and transaction encryption.

Scalability and maintainability are guaranteed by the architecture's modular design, 
which  allows  each  component  to  handle  various  platform  functions  independently. 
This  division  makes  the  system  adaptable,  allowing  for  future  enhancements  to 
financial  services,  security  protocols,  or  AI  models  without  compromising  system 
speed.

Architecture

’Fig 1.1 System Layered

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 4 -->

Fig 1.2 Architecture diagram

Methodology: 
4.1  Financial  Data  Collection:  Supabase-integrated  secure  APIs  are  used  to 
collect user financial data, such as transaction history and spending trends. To protect 
privacy, data is anonymised before being saved for processing and suggestions in the 
future.

4.2  AI-Driven  Budgeting  and  Recommendations:  The  platform  offers  tailored 
financial  advice  through  the  Gemini  LLM  API.  By  analysing  their  spending  habits 
and  offering  personalized  investment  plans,  savings  advice,  and  budgeting  insights, 
the  AI  adjusts  to  consumers'  financial  behaviours.  Real-time  data  and  personal 
financial objectives are the main topics of the prompts.

4.3  Policy  Recommendation  Engine:  The  system  connects  consumers  with 
pertinent  government  programs,  tax  breaks,  and  subsidies  by  utilizing  hybrid  data 
APIs. The suggestions are dynamic and customized based on the geographic location 
and financial profile of each user.

4.4 Frontend Interface: The Next.js frontend displays interactive dashboards and

real-time financial insights. It includes the following interface functionality

  Visual spending analytics

  Budget Tracking Tools

  Responsive design for mobile and desktop use

  Dark/light mode toggle

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 5 -->

4.5 Sequence Diagram:

Evaluation: 
5.1  System  Performance  Evaluation:  A  number  of  measures  are  used  to  assess

Fig 1.3 Sequence Diagram

the system's performance:

  Response  Time:  Average

financial 
recommendations  and  policy  suggestions.  The  platform  aims  to  respond 
within 2-3 seconds after user input.

for  generating

response

time

  Token Efficiency: To make sure the AI provides pertinent insights quickly 
and  without  requiring  too  much  computation,  the  Gemini  LLM  API  tracks 
the token usage for each interaction. This is quantified in terms of response 
length,  which  fluctuates  according to  the  financial inquiry  and the intricacy 
of user input.

5.2  Human  Evaluation:  Fifty  users  were  polled  to  assess  the  platform's 
effectiveness in terms of recommendations' personalization, relevancy, and empathy. 
The average rating was:

  Budgeting Insights: 4.8/5

  Policy Recommendations: 4.7/5

  Learning Roadmap: 4.6/5

The  platform's  capacity  to  provide  tailored  budgeting  guidance,  pertinent  policy 
recommendations, and unambiguous financial education were recognized by users as 
its  most  important  characteristics.  Higher  evaluations  were  frequently  attributed  to 
cultural relevance and actionable ideas

5.3  Security  and  Privacy  Evaluation:  Assessment:  To  guarantee  the  privacy  of 
user  data,  security  protocols  were  examined. The  platform transmits  and  stores  data 
using  end-to-end  encryption.  Arcjet  was  used  to  identify  any  security  risks  and

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 6 -->

prevent unwanted access, guaranteeing that private financial information was handled 
securely.

Novelty and Uniqueness: 
The  primary  innovation  of  AI  Wealth  Navigator  is  the  integration  of  three 
historically  distinct  financial  domains—financial  education,  policy  suggestion, 
and  budget  tracking—into  a  unified,  context-aware  platform  driven  by  AI. 
Although  the majority  of  personal  finance  applications are excellent  at  one  area, 
like  tracking  investments  or  managing  expenses,  they  frequently  overlook  the 
significance  of  financial  literacy  and  having  access  to  specialized  government 
assistance  services.  AI  Wealth  Navigator  fills  this  crucial  void  by  providing  a 
comprehensive ecosystem intended to empower people financially.

The platform's clever application of Gemini LLMs, which dynamically produce 
tailored insights and useful suggestions, is what makes it unique. The LLM adjusts 
its  answers  according  to  users'  spending  patterns,  financial  objectives,  reading 
level,  and  demographic  information,  in  contrast  to  traditional  systems  that  use 
static  financial  principles.  For  example,  advanced  users  gain  from  sophisticated 
analysis and investment methods, while those with little financial expertise receive 
simplified, instructional solutions.

The  policy  recommendation  engine  is  another  significant  innovation.  It  uses 
real-time  user  profiling  and  hybrid  API  integration  to  classify  and  recommend 
government programs, tax breaks, and subsidies. Beyond simple eligibility checks, 
this  module  provides  information  on how,  why,  and  when to  apply  according  on 
the  user's  age,  occupation,  family  history,  and  income  bracket.  The  engine 
functions as a personal advisor integrated into the financial workflow, in contrast 
to general policy directories.

Additionally,  the  platform  offers  a  Financial  Literacy  Progress  Tracker  that 
makes  use  of  adaptive  roadmaps  and  gamified  modules.  Users  are  now  led 
through  a  carefully  chosen, trackable  learning route rather than having to  search 
through  numerous  websites,  blogs,  or  Reddit  communities.  The  poor  financial 
literacy  rates  in  places  like  India,  where  it  is  still  difficult  to  obtain  trustworthy 
and organized financial information, are immediately addressed by this feature.

Integrating  Arcjet,  which  offers  rate  restriction  and  sophisticated  threat 
prevention at the API layer, strengthens security and dependability. When used in 
conjunction  with  Inngest  for  automated  background  functions  such  as  learning 
progress  updates  and  monthly  budget  resets,  the  system  guarantees  real-time 
responsiveness without sacrificing speed.

the

Through

integration  of

learning,  intelligent  budgeting,  and  policy 
suggestions into a single, adaptable ecosystem, the AI Wealth Navigator platform 
presents  a  cohesive,  intelligent  approach  to  personal  finance.  The  AI  Receipt 
Scanner,  a  specially  designed,  AI-powered 
that  outperforms 
conventional OCR modules, is one of its primary inventions. It accurately captures

technology

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 7 -->

a  variety  of  receipt  forms,  including  GPay  transactions  and  paper  bills,  and 
automatically converts them into structured transaction logs, greatly reducing false 
positives and negatives in comparison to standard OCRs. This increases adoption 
by  doing  away  with  manual  entry.  In  addition  to  contextual  insights  enabled  by 
Gemini  and  customized  policy  recommendations  based  on  user  portfolios,  the 
platform  guarantees  a  smooth,  data-driven,  and  human-centered  financial 
experience

than  merely  another  financial

In conclusion, AI Wealth Navigator is a context-aware, AI-enhanced financial 
tutor  rather 
instrument.  It  combines  safe 
infrastructure,  adaptive  education,  localized  policy  knowledge,  and  intelligent 
automation  in  a  way  that  is  unique  and  supports  both  personal  financial 
development and more general objectives of economic inclusion.

Results and Discussion: 
In  tests  conducted  in  the  real  world,  the  AI  Wealth  Navigator  showed  excellent 
usability.  Users  valued  the  platform's  smooth  integration  of  financial  education, 
policy  recommendations,  and  budgeting,  which  eliminated  the  need  to  manage 
several apps or websites. The Gemini LLM provided context-aware insights including 
spending  patterns  and  customized  saving  advice,  while  the  OCR-powered  receipt 
scanner achieved 94% accuracy on both digital and physical receipts. The success of 
the policy recommendation module is demonstrated by the fact that more than 70% of 
users  found  previously  unheard-of  government  programs  that  were  customized  for 
their  profiles.  Arcjet  blocked  all  simulated  security  risks,  and  Inngest  handled 
automated  duties  effectively,  ensuring  seamless  performance.  The  reliance  on  full 
user profiles for policy matching and sporadic OCR errors were minor drawbacks.

Fig 1.4 Dashboard

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 8 -->

Fig 1.5 Transaction Page with Scanner

Fig 1.6 Learning Modules

Fig 1.7 Policy Suggestion

Conclusion and Future Work: 
The  potential  of  combining  policy  recommendations,  smart  budgeting,  and 
financial  education  into  a  unified,  AI-powered  ecosystem  is  demonstrated  by  AI 
Wealth  Navigator.  The  platform  offers  real-time  policy  recommendations,  adaptive 
learning,  and  personalized  financial  insights  through  a  modular  design  and  the 
integration  of  refined  large  language  models—all  inside  a  safe  and  user-friendly 
interface.

Future enhancements include:

  Support for regional languages to promote accessibility

  Predictive financial planning using behavioural data

  Offline support via open-source LLMs like Mistral

References:

[1]  N  Sunayana,  N.  Ravikumar,  and  B.  L.  Gururaja,  “Fintech:  A  Model  for  Financial  Inclusion  of 
Sustainable  Economic  Development  of  Vishwakarma  Community  in  India,” 2022  9th  International 
Conference on Computing for Sustainable Global Development (INDIACom),  pp. 1526–1530, Feb. 2024, 
doi: https://doi.org/10.23919/indiacom61295.2024.10498449.

[2]  G.  U.  Ebirim,  N.  L.  Ndubuisi,  I.  F.  Unigwe,  O.  F.  Asuzu,  O.  A.  Adelekan,  and  K.  F.  Awonuga, 
“Financial  literacy  and  community  empowerment:  A  review  of  volunteer  accounting  initiatives  in  low-
income areas,” International Journal of Science and Research Archive, vol. 11, no. 1, pp. 975–985, 2024, 
doi: https://doi.org/10.30574/ijsra.2024.11.1.0135.

Electronic copy available at: https://ssrn.com/abstract=5854302

---

<!-- PAGE 9 -->

[3]  H.  Liu,  “Research  on  Financial  Budget  Management  System  Based  on  Particle  Swarm 
Optimization,” 2022  2nd  International  Conference  on  Networking,  Communications  and  Information 
Technology 
doi: 
390, 
https://doi.org/10.1109/netcit57419.2022.00108.

(NetCIT),

432–435,

2022,

Dec.

vol.

pp.

[4]  “IEEE FINANCE OPERATIONS MANUAL (FOM)  V.48 Includes approved  changes through 19 
November  2018  INTRODUCTION  FOM.1  -FINANCIAL  STABILITY  FOM.2  -ANNUAL  AND 
INTERIM  REPORTING  REQUIREMENTS  FOM.3  -ASSET/LIABILITY  MANAGEMENT  FOM.4  -
RESERVES FOM.5 -INSURANCE COVERAGE FOM.6 -BUSINESS EXPENSE REPORTING FOM.7 -
FUND-RAISING:  GRANTS  AND  CONTRIBUTIONS  FOM.8  -CONTRACT  APPROVAL  FOM.9  -
SALES  REBATES  TO  ORGANIZATIONAL  UNITS.”  Accessed:  Apr.  28,  2025.  [Online].  Available: 
https://events.ieee.org/wp-content/uploads/financial-ops-manual.pdf.

[5]  O.  Maslova,  L.  Klein,  D.  Dabernat,  A.  Benoit,  and  P.  Lambert,  “Receipt  automatic  reader,” 2019 
(CBMI),  Sep.  2019,  doi:

Indexing

International  Conference  on  Content-Based  Multimedia 
https://doi.org/10.1109/cbmi.2019.8877407

[6]  “Mobile  Bookkeeper:  Personal  Financial  Management  Application  with  Receipt  Scanner  Using 
Optical  Character  Recognition  |  IEEE  Conference  Publication  |  IEEE  Xplore,” ieeexplore.ieee.org. 
https://ieeexplore.ieee.org/document/9638794

[7]  Rizlene  Raoui-Outach,  C.  Million-Rousseau,  A.  Benoit,  and  P.  Lambert,  “Deep  learning  for 
automatic sale receipt understanding,” HAL (Le Centre pour la Communication Scientifique Directe), Nov. 
2020, doi: https://doi.org/10.1109/ipta.2017.8310088.

[8]  Sahil  Shelke,  Manish  Shingre,  Sahaya  Lebisha,  and  S.  Shaikh,  “Smart  BAT  -  Smart  Budget

Analyzer and Tracker,” Oct. 2023, doi: https://doi.org/10.1109/icacta58201.2023.10392452.

[9]  “TrackEZ  Expense  Tracker  |  IEEE  Conference  Publication  |  IEEE  Xplore,” ieeexplore.ieee.org.

https://ieeexplore.ieee.org/abstract/document/1017073.

[10]  A.  Tamizhselvi,  M.  Anbu,  and  K.  R.  Radhakrishnan,  “Financial  and  Individual  Future  Expense 
Prediction  Based  on  Frequent  Patterns  Using  Micro  Services,” 2022  Third  International  Conference  on 
Intelligent Computing Instrumentation and Control Technologies (ICICICT), pp. 532–536, Aug. 2022, doi: 
https://doi.org/10.1109/icicict54557.2022.9917982.

[11]  E.  R.  Larrocha et  al.,  “Resources  and  new  educational  modules  for  Sustainable  Finantial 
Literacy,” 2021 World Engineering Education Forum/Global Engineering Deans Council (WEEF/GEDC), 
pp. 545–549, Nov. 2021, doi: https://doi.org/10.1109/weef/gedc53299.2021.9657313.

[12]  N.  Kaur,  M.  Gupta,  S.  Saha,  S.  Manallack,  and  P.  Gupta,  “Financial  Literacy  through

Gamification,” Feb. 2024, doi: https://doi.org/10.1109/iciptm59628.2024.10563365.

[13]  R.  S.  Gautam,  A.  Rawal,  and  S.  Rastogi,  “Financial  Literacy  and  Its  Impact  on  Sustainable 
doi: 
Subscribers

as  Moderator,”  Oct.

India  Using

Internet

2022,

of

Development 
https://doi.org/10.1109/sibf56821.2022.9939760.

[14]  S.  Rani,  “The  Impact  of  Financial  Literacy  on  Financial  Well-Being:  The  Meditational  Role  of

Personal Finance Management,” Sep. 2023, doi: https://doi.org/10.1109/ic3i59117.2023.10397970.

[15]  R.  Islam  and  I.  Ahmed,  “Gemini-the  most  powerful  LLM:  Myth  or  Truth,”  May  2024,  doi:

https://doi.org/10.1109/ictc61510.2024.10602253

Electronic copy available at: https://ssrn.com/abstract=5854302

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

AI Wealth Navigator: An Integrated
Platform for Smart Budgeting, Financial
Learning, and Personalized Policy Guidance

Akash Yadav1, R Surya Prakash2, Safa Mohamed Iqubal3*,

Mahder Girmay Gebremicahea4

1, 2, 3Department of Networking and Communications, Faculty of Engineering &

Technology, SRM

Institute of Science and Technology, Kattankulathur, India.
4Department: School of Electrical and Computer Engineering, Ethiopean Institute

of Technology, Mekelle, Mekelle University, Ethiopia

Email: ay7507@srmist.edu.in, sr9071srmist.edu.in, safam@srmist.edu.in*,

Mahder.girmay@mu.edu.et

Abstract-  Despite  the  widespread  availability  of  personal  finance  applications,
consumers  still  encounter  disjointed  financial  ecosystems  in  which  knowledge  of
government  policies,  financial  education,  and  budgeting  are  all  compartmentalized.
Through  three  seamlessly  integrated  modules,  this  paper  introduces  AI  Wealth
Navigator,  a  unified,  intelligent  financial  platform  that  fills  these  gaps:  (1)  a  financial
learning roadmap that adjusts to user progress and literacy levels; (2) a clever AI-driven
budget tracker with real-time visual insights, receipt scanning, and personalized savings
alerts; and (3) a policy recommendation engine that uses large language models to suggest
pertinent  government  schemes  and  benefits  based  on  individual  profiles.  For  safe,
the  system  architecture  makes  use  of
scalable,  and  responsive  performance,
contemporary web technologies, including Next.js, Supabase, Prisma, Arcjet, and Inngest.
Hybrid  data  APIs  and  Gemini  LLMs  improve
inclusion,  decision-making,  and
customisation.  The  platform  promotes  economic  inclusion,  financial  literacy,  and  more
prudent  personal  financial  practices,  all  of  which  are  in  line  with  UN  Sustainable
Development Goals (SDGs) 1, 4, 8, and 10. The system concept, important implementation
elements, and its potential as a game-changing tool in the world of digital finance are all
presented in this article

Keywords:  The  Sustainable  Development  Goals,  Intelligent  Budgeting,  Financial
Literacy, AI Policy Suggestion, Gemini LLM, Supabase, Personal Finance Platform, Receipt
OCR, Inngest, Web-Based Financial Assistant

Introduction:
Users  frequently  suffer  with  disjointed  solutions  that  don't  offer  a  cohesive
approach  to  budgeting,  financial  education,  and  policy  navigation  in  the  quickly
changing field of personal finance management. Even though there are many finance
applications  available,  many  platforms  are  still  fragmented,  concentrating  on  either
simple  budgeting  or  discrete  educational  materials  rather  than  providing  a  full
solution that incorporates all facets of financial decision-making. Users are unable to
maximize  their  financial  well-being due to  inefficiencies  caused  by  the  absence  of  a
consistent, tailored experience across platforms.

This  problem  is  made  worse  in  India  by  a  lack  of  financial  literacy.  Recent
research indicates that a sizable section of the populace does not have access to high-

Electronic copy available at: https://ssrn.com/abstract=5854302

quality financial education, which hinders their capacity to  make wise choices about
government  assistance,  investments,  and  savings.  In  order  to  educate  themselves,
users also frequently browse through a variety of websites, forums, and publications;
but,  because  these  resources  are  unstructured,  it  can  be  challenging  to  monitor
progress  and  meet  financial  objectives.  Because  of  this, a lot  of  people  still manage
their  money  using  antiquated,  inefficient  techniques,  which  contributes  to  ongoing
financial instability

to  solve

In  order

these  problems,  we  present  AI  Wealth  Navigator,  a
comprehensive  platform  that  combines  three  essential  modules  to  optimize  the
financial management process: (1) an adaptive financial learning roadmap that tracks
and  advances  in  tandem  with  the  user's  knowledge;  (2)  an  intelligent  AI-powered
budget tracker that offers real-time insights, receipt scanning, and customized alerts;
and  (3)  a  policy  recommendation  engine  that  makes  recommendations  based  on  the
user's  profile  and  requirements.  The  platform  makes  use  of  state-of-the-art
technologies,  such  as  Next.js,  Supabase,  Prisma,  and  Gemini  LLMs,  to  provide
security, scalability, and tailored recommendations.

AI  Wealth  Navigator  seeks  to  streamline  personal  money  management  by
combining these functions into a single platform. This will enable users to track their
spending, enhance their financial literacy, and access pertinent government programs,
all of which will help them make better financial decisions.

Literature Survey:
Recent years have seen a surge in the use of AI in personal money management as
numerous  research  have  shown  how  it  may  improve  policy  suggestions,  financial
education, and budgeting. In the field of financial education, Patel et al. (2023) talked
about  how  AI-powered  platforms  can  help  advance  financial  literacy  by  providing
financial  tools  and  individualized  learning  paths.  According  to  their  findings,  AI-
based solutions may be able to close the knowledge gap and empower people in low-
income communities to make wise investment and savings choices.

Similar  to  this,  Kumar  et  al.  (2023)  investigated  developments  in  AI-powered
budgeting tools and presented an intelligent budgeting system that adjusts to the user's
spending  habits  and
financial  objectives.  The  system's  use  of  dynamic
information  enhanced  user  engagement  and
recommendations  and  real-time
strengthened  financial  discipline.  Additionally,  Singh  et  al.  (2024)  investigated  how
AI-driven receipt scanning and classification may increase the accuracy of budgeting,
emphasizing  the  drawbacks  of  conventional  manual  techniques  and  the  notable
decrease in human error.

The  potential  of  large  language  models  (LLMs)  to  offer  tailored  government
scheme  recommendations  has  been  investigated  in  a  number  of  studies.  Based  on
users'  financial  profiles,  Lee  et  al.  (2023)  created  a  system  that  employed  AI  to
suggest  social  security  benefits  and  subsidies.  The  significance  of  context-specific
advice that complement the user's present financial circumstances and objectives was
emphasized by this study. Furthermore, research by Sharma et al. (2024) highlighted
how  AI  systems  must  take  regional  differences  in  policy  recommendations  into
consideration
that  consumers  obtain  pertinent  and  correct
recommendations.

to  guarantee

Electronic copy available at: https://ssrn.com/abstract=5854302

A  significant  worry  has  also  been  the  privacy  and  security  of  financial
applications.  According  to  a  study  by  Gupta  et  al.  (2024),  AI  was  used  to  integrate
secure  transaction  systems  into  financial  platforms  in  order  to  identify  fraudulent
activity  and  guarantee the  security  of  private  financial information.  The  significance
of  multilayer  security  measures  in  applications  involving  financial  transactions  and
personal data was brought to light by their work.

System Architecture:
AI Wealth Navigator consists of five core components:

  Frontend  (UI):  Built  with  Next.js  and  Tailwind  CSS,  providing  a
responsive, interactive user experience for budgeting, financial learning, and
policy suggestions.

  Backend  &  API:  Uses  Supabase  and  Prisma  for  data  management,  with

Inngest handling automated tasks and notifications.

  AI  Insights:  Powered  by  Gemini  LLM  for  personalized  financial

recommendations and adaptive learning.

  Policy Engine: Suggests relevant government schemes using AI and hybrid

data APIs based on user profiles.

  Security: Arcjet ensures secure data handling and transaction encryption.

Scalability and maintainability are guaranteed by the architecture's modular design,
which  allows  each  component  to  handle  various  platform  functions  independently.
This  division  makes  the  system  adaptable,  allowing  for  future  enhancements  to
financial  services,  security  protocols,  or  AI  models  without  compromising  system
speed.

Architecture

’Fig 1.1 System Layered

Electronic copy available at: https://ssrn.com/abstract=5854302

Fig 1.2 Architecture diagram

Methodology:
4.1  Financial  Data  Collection:  Supabase-integrated  secure  APIs  are  used  to
collect user financial data, such as transaction history and spending trends. To protect
privacy, data is anonymised before being saved for processing and suggestions in the
future.

4.2  AI-Driven  Budgeting  and  Recommendations:  The  platform  offers  tailored
financial  advice  through  the  Gemini  LLM  API.  By  analysing  their  spending  habits
and  offering  personalized  investment  plans,  savings  advice,  and  budgeting  insights,
the  AI  adjusts  to  consumers'  financial  behaviours.  Real-time  data  and  personal
financial objectives are the main topics of the prompts.

4.3  Policy  Recommendation  Engine:  The  system  connects  consumers  with
pertinent  government  programs,  tax  breaks,  and  subsidies  by  utilizing  hybrid  data
APIs. The suggestions are dynamic and customized based on the geographic location
and financial profile of each user.

4.4 Frontend Interface: The Next.js frontend displays interactive dashboards and

real-time financial insights. It includes the following interface functionality

  Visual spending analytics

  Budget Tracking Tools

  Responsive design for mobile and desktop use

  Dark/light mode toggle

Electronic copy available at: https://ssrn.com/abstract=5854302

4.5 Sequence Diagram:

Evaluation:
5.1  System  Performance  Evaluation:  A  number  of  measures  are  used  to  assess

Fig 1.3 Sequence Diagram

the system's performance:

  Response  Time:  Average

financial
recommendations  and  policy  suggestions.  The  platform  aims  to  respond
within 2-3 seconds after user input.

for  generating

response

time

  Token Efficiency: To make sure the AI provides pertinent insights quickly
and  without  requiring  too  much  computation,  the  Gemini  LLM  API  tracks
the token usage for each interaction. This is quantified in terms of response
length,  which  fluctuates  according to  the  financial inquiry  and the intricacy
of user input.

5.2  Human  Evaluation:  Fifty  users  were  polled  to  assess  the  platform's
effectiveness in terms of recommendations' personalization, relevancy, and empathy.
The average rating was:

  Budgeting Insights: 4.8/5

  Policy Recommendations: 4.7/5

  Learning Roadmap: 4.6/5

The  platform's  capacity  to  provide  tailored  budgeting  guidance,  pertinent  policy
recommendations, and unambiguous financial education were recognized by users as
its  most  important  characteristics.  Higher  evaluations  were  frequently  attributed  to
cultural relevance and actionable ideas

5.3  Security  and  Privacy  Evaluation:  Assessment:  To  guarantee  the  privacy  of
user  data,  security  protocols  were  examined. The  platform transmits  and  stores  data
using  end-to-end  encryption.  Arcjet  was  used  to  identify  any  security  risks  and

Electronic copy available at: https://ssrn.com/abstract=5854302

prevent unwanted access, guaranteeing that private financial information was handled
securely.

Novelty and Uniqueness:
The  primary  innovation  of  AI  Wealth  Navigator  is  the  integration  of  three
historically  distinct  financial  domains—financial  education,  policy  suggestion,
and  budget  tracking—into  a  unified,  context-aware  platform  driven  by  AI.
Although  the majority  of  personal  finance  applications are excellent  at  one  area,
like  tracking  investments  or  managing  expenses,  they  frequently  overlook  the
significance  of  financial  literacy  and  having  access  to  specialized  government
assistance  services.  AI  Wealth  Navigator  fills  this  crucial  void  by  providing  a
comprehensive ecosystem intended to empower people financially.

The platform's clever application of Gemini LLMs, which dynamically produce
tailored insights and useful suggestions, is what makes it unique. The LLM adjusts
its  answers  according  to  users'  spending  patterns,  financial  objectives,  reading
level,  and  demographic  information,  in  contrast  to  traditional  systems  that  use
static  financial  principles.  For  example,  advanced  users  gain  from  sophisticated
analysis and investment methods, while those with little financial expertise receive
simplified, instructional solutions.

The  policy  recommendation  engine  is  another  significant  innovation.  It  uses
real-time  user  profiling  and  hybrid  API  integration  to  classify  and  recommend
government programs, tax breaks, and subsidies. Beyond simple eligibility checks,
this  module  provides  information  on how,  why,  and  when to  apply  according  on
the  user's  age,  occupation,  family  history,  and  income  bracket.  The  engine
functions as a personal advisor integrated into the financial workflow, in contrast
to general policy directories.

Additionally,  the  platform  offers  a  Financial  Literacy  Progress  Tracker  that
makes  use  of  adaptive  roadmaps  and  gamified  modules.  Users  are  now  led
through  a  carefully  chosen, trackable  learning route rather than having to  search
through  numerous  websites,  blogs,  or  Reddit  communities.  The  poor  financial
literacy  rates  in  places  like  India,  where  it  is  still  difficult  to  obtain  trustworthy
and organized financial information, are immediately addressed by this feature.

Integrating  Arcjet,  which  offers  rate  restriction  and  sophisticated  threat
prevention at the API layer, strengthens security and dependability. When used in
conjunction  with  Inngest  for  automated  background  functions  such  as  learning
progress  updates  and  monthly  budget  resets,  the  system  guarantees  real-time
responsiveness without sacrificing speed.

the

Through

integration  of

learning,  intelligent  budgeting,  and  policy
suggestions into a single, adaptable ecosystem, the AI Wealth Navigator platform
presents  a  cohesive,  intelligent  approach  to  personal  finance.  The  AI  Receipt
Scanner,  a  specially  designed,  AI-powered
that  outperforms
conventional OCR modules, is one of its primary inventions. It accurately captures

technology

Electronic copy available at: https://ssrn.com/abstract=5854302

a  variety  of  receipt  forms,  including  GPay  transactions  and  paper  bills,  and
automatically converts them into structured transaction logs, greatly reducing false
positives and negatives in comparison to standard OCRs. This increases adoption
by  doing  away  with  manual  entry.  In  addition  to  contextual  insights  enabled  by
Gemini  and  customized  policy  recommendations  based  on  user  portfolios,  the
platform  guarantees  a  smooth,  data-driven,  and  human-centered  financial
experience

than  merely  another  financial

In conclusion, AI Wealth Navigator is a context-aware, AI-enhanced financial
tutor  rather
instrument.  It  combines  safe
infrastructure,  adaptive  education,  localized  policy  knowledge,  and  intelligent
automation  in  a  way  that  is  unique  and  supports  both  personal  financial
development and more general objectives of economic inclusion.

Results and Discussion:
In  tests  conducted  in  the  real  world,  the  AI  Wealth  Navigator  showed  excellent
usability.  Users  valued  the  platform's  smooth  integration  of  financial  education,
policy  recommendations,  and  budgeting,  which  eliminated  the  need  to  manage
several apps or websites. The Gemini LLM provided context-aware insights including
spending  patterns  and  customized  saving  advice,  while  the  OCR-powered  receipt
scanner achieved 94% accuracy on both digital and physical receipts. The success of
the policy recommendation module is demonstrated by the fact that more than 70% of
users  found  previously  unheard-of  government  programs  that  were  customized  for
their  profiles.  Arcjet  blocked  all  simulated  security  risks,  and  Inngest  handled
automated  duties  effectively,  ensuring  seamless  performance.  The  reliance  on  full
user profiles for policy matching and sporadic OCR errors were minor drawbacks.

Fig 1.4 Dashboard

Electronic copy available at: https://ssrn.com/abstract=5854302

Fig 1.5 Transaction Page with Scanner

Fig 1.6 Learning Modules

Fig 1.7 Policy Suggestion

Conclusion and Future Work:
The  potential  of  combining  policy  recommendations,  smart  budgeting,  and
financial  education  into  a  unified,  AI-powered  ecosystem  is  demonstrated  by  AI
Wealth  Navigator.  The  platform  offers  real-time  policy  recommendations,  adaptive
learning,  and  personalized  financial  insights  through  a  modular  design  and  the
integration  of  refined  large  language  models—all  inside  a  safe  and  user-friendly
interface.

Future enhancements include:

  Support for regional languages to promote accessibility

  Predictive financial planning using behavioural data

  Offline support via open-source LLMs like Mistral

References:

[1]  N  Sunayana,  N.  Ravikumar,  and  B.  L.  Gururaja,  “Fintech:  A  Model  for  Financial  Inclusion  of
Sustainable  Economic  Development  of  Vishwakarma  Community  in  India,” 2022  9th  International
Conference on Computing for Sustainable Global Development (INDIACom),  pp. 1526–1530, Feb. 2024,
doi: https://doi.org/10.23919/indiacom61295.2024.10498449.

[2]  G.  U.  Ebirim,  N.  L.  Ndubuisi,  I.  F.  Unigwe,  O.  F.  Asuzu,  O.  A.  Adelekan,  and  K.  F.  Awonuga,
“Financial  literacy  and  community  empowerment:  A  review  of  volunteer  accounting  initiatives  in  low-
income areas,” International Journal of Science and Research Archive, vol. 11, no. 1, pp. 975–985, 2024,
doi: https://doi.org/10.30574/ijsra.2024.11.1.0135.

Electronic copy available at: https://ssrn.com/abstract=5854302

[3]  H.  Liu,  “Research  on  Financial  Budget  Management  System  Based  on  Particle  Swarm
Optimization,” 2022  2nd  International  Conference  on  Networking,  Communications  and  Information
Technology
doi:
390,
https://doi.org/10.1109/netcit57419.2022.00108.

(NetCIT),

432–435,

2022,

Dec.

vol.

pp.

[4]  “IEEE FINANCE OPERATIONS MANUAL (FOM)  V.48 Includes approved  changes through 19
November  2018  INTRODUCTION  FOM.1  -FINANCIAL  STABILITY  FOM.2  -ANNUAL  AND
INTERIM  REPORTING  REQUIREMENTS  FOM.3  -ASSET/LIABILITY  MANAGEMENT  FOM.4  -
RESERVES FOM.5 -INSURANCE COVERAGE FOM.6 -BUSINESS EXPENSE REPORTING FOM.7 -
FUND-RAISING:  GRANTS  AND  CONTRIBUTIONS  FOM.8  -CONTRACT  APPROVAL  FOM.9  -
SALES  REBATES  TO  ORGANIZATIONAL  UNITS.”  Accessed:  Apr.  28,  2025.  [Online].  Available:
https://events.ieee.org/wp-content/uploads/financial-ops-manual.pdf.

[5]  O.  Maslova,  L.  Klein,  D.  Dabernat,  A.  Benoit,  and  P.  Lambert,  “Receipt  automatic  reader,” 2019
(CBMI),  Sep.  2019,  doi:

Indexing

International  Conference  on  Content-Based  Multimedia
https://doi.org/10.1109/cbmi.2019.8877407

[6]  “Mobile  Bookkeeper:  Personal  Financial  Management  Application  with  Receipt  Scanner  Using
Optical  Character  Recognition  |  IEEE  Conference  Publication  |  IEEE  Xplore,” ieeexplore.ieee.org.
https://ieeexplore.ieee.org/document/9638794

[7]  Rizlene  Raoui-Outach,  C.  Million-Rousseau,  A.  Benoit,  and  P.  Lambert,  “Deep  learning  for
automatic sale receipt understanding,” HAL (Le Centre pour la Communication Scientifique Directe), Nov.
2020, doi: https://doi.org/10.1109/ipta.2017.8310088.

[8]  Sahil  Shelke,  Manish  Shingre,  Sahaya  Lebisha,  and  S.  Shaikh,  “Smart  BAT  -  Smart  Budget

Analyzer and Tracker,” Oct. 2023, doi: https://doi.org/10.1109/icacta58201.2023.10392452.

[9]  “TrackEZ  Expense  Tracker  |  IEEE  Conference  Publication  |  IEEE  Xplore,” ieeexplore.ieee.org.

https://ieeexplore.ieee.org/abstract/document/1017073.

[10]  A.  Tamizhselvi,  M.  Anbu,  and  K.  R.  Radhakrishnan,  “Financial  and  Individual  Future  Expense
Prediction  Based  on  Frequent  Patterns  Using  Micro  Services,” 2022  Third  International  Conference  on
Intelligent Computing Instrumentation and Control Technologies (ICICICT), pp. 532–536, Aug. 2022, doi:
https://doi.org/10.1109/icicict54557.2022.9917982.

[11]  E.  R.  Larrocha et  al.,  “Resources  and  new  educational  modules  for  Sustainable  Finantial
Literacy,” 2021 World Engineering Education Forum/Global Engineering Deans Council (WEEF/GEDC),
pp. 545–549, Nov. 2021, doi: https://doi.org/10.1109/weef/gedc53299.2021.9657313.

[12]  N.  Kaur,  M.  Gupta,  S.  Saha,  S.  Manallack,  and  P.  Gupta,  “Financial  Literacy  through

Gamification,” Feb. 2024, doi: https://doi.org/10.1109/iciptm59628.2024.10563365.

[13]  R.  S.  Gautam,  A.  Rawal,  and  S.  Rastogi,  “Financial  Literacy  and  Its  Impact  on  Sustainable
doi:
Subscribers

as  Moderator,”  Oct.

India  Using

Internet

2022,

of

Development
https://doi.org/10.1109/sibf56821.2022.9939760.

[14]  S.  Rani,  “The  Impact  of  Financial  Literacy  on  Financial  Well-Being:  The  Meditational  Role  of

Personal Finance Management,” Sep. 2023, doi: https://doi.org/10.1109/ic3i59117.2023.10397970.

[15]  R.  Islam  and  I.  Ahmed,  “Gemini-the  most  powerful  LLM:  Myth  or  Truth,”  May  2024,  doi:

https://doi.org/10.1109/ictc61510.2024.10602253

Electronic copy available at: https://ssrn.com/abstract=5854302

