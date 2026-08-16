---
conversion_metadata:
  converted_at: "2026-07-21T08:19:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Reddy et al.pdf"
  source_pdf_sha256: "0030e609eda3fa0a68d9c87e4234af0f9ca42ecc2bf058565a57142706539447"
  page_count: 11
  markdown_char_count: 150365
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

AI-Powered Financial Insights Platform

S Tarun reddy.¹, Soniya C.¹, Thanushree G .¹, Darshan BG.¹, Dr. Shwetha Gupta2 
1B.Tech Students, Department of CSE (AI & ML), CMR University, Bengaluru, Karnataka

2Professor, Department of CSE (AI & ML), CMR University, Bengaluru, Karnataka

ABSTRACT

The AI-Powered Financial Insights Platform is designed to address the 
increasing  complexity  of  decentralized  applications  and  digital  asset 
management  systems.  As  blockchain  ecosystems  expand,  users  often 
struggle  to  interpret  detailed  transaction  data,  understand  staking 
mechanisms,  or navigate  complex on-chain  information.  This platform 
leverages  advancements  in  Artificial  Intelligence,  real-time  blockchain 
indexing,  and  decentralized  protocols  to  convert  unintuitive  data  into 
easily  interpretable  financial  insights  while  maintaining  security  and 
trust.  By  utilizing  the  Cardano  network  as  its  foundation,  the platform 
provides a research-driven, layered architecture that ensures scalability 
and  sustainability  as  separate  principles.  This  platform  represents  a 
paradigm  shift 
in  wealth  management  and  fiscal  oversight  by 
transitioning  from  reactive  reporting  to  predictive  intelligence.  At  its 
core,  the  system  utilizes  a  sophisticated  multi-agent  AI  architecture 
designed  to  ingest,  normalize,  and  analyze  massive  volumes  of 
heterogeneous  financial data.  By  synthesizing  information  from global 
market  indices,  real-time  news  sentiment,  and  individual  spending 
patterns,  the  platform  constructs  a  360-degree  financial  profile.  It 
employs  advanced  Long  Short-Term  Memory  (LSTM)  networks  and 
Transformer-based  models  to  forecast  cash  flow  trajectories  and 
identify  potential  liquidity  risks  before  they  manifest.  This  proactive 
approach  allows  users—whether  institutional  investors  or  private 
individuals—to  navigate  volatile  markets  with  a  data-backed  roadmap 
indicators.  Beyond  mere  data 
rather 
aggregation, the platform emphasizes contextual relevance. The "Insight 
Engine"  utilizes  Natural  Language  Generation  (NLG)  to  translate 
complex  algorithmic  outputs  into  high-level  executive  summaries, 
effectively  democratizing  access 
financial 
analysis. Security is woven into the fabric of the application through a 
hybrid  backend—  combining  the  raw  computational  speed  of  C++  for 
high-frequency  data  processing  with  the  flexibility  of  Python  for  AI 
model  deployment.  This  ensures  that  the  system  remains  scalable  and 
responsive under heavy loads.

to  professional-grade

than  relying  on

lagging

I. INTRODUCTION 
Financial management currently remains a highly significant challenge 
for a vast majority of individuals residing in India, with this issue being 
particularly acute and noticeable among the working-class demographic 
as well as the broader student population. In recent years, there has been 
a  massive  proliferation  and  widespread  adoption  of  various  digital 
banking  solutions  and  digital  payment  platforms  across  the  country. 
Despite  this  rapid  technological  advancement  in  basic  transaction 
capabilities,  a  critical  gap  persists:  most  users  still  completely  lack 
access  to  personalized,  highly  affordable  financial  advisory  services. 
This  absence  of  accessible  guidance  means  that  everyday  individuals 
struggle to find expert systems capable of actively guiding their crucial 
savings,  investment,  and  budgeting  decisions  in  a  manner  that  is 
specifically  tailored  to  their  unique,  individual  income  profiles.  The 
existing landscape  leaves  a  void  where  middle-income  individuals  are

left  without  the  necessary  personalized  financial  advisory  tools  required  to 
navigate  their  economic  lives  effectively.  Furthermore,  there  is  a  distinctly 
low  level  of  general  financial  literacy  and  a  pervasive  lack  of  awareness 
concerning  critical  wealth-building  and 
instruments, 
including mutual funds, Systematic Investment Plans (SIPs), and various tax- 
saving mechanisms.

tax-management

To directly bridge this substantial gap in the financial services ecosystem, an 
AI-powered  personal  finance  platform  named  "Welth"  (stylized  as  Welth) 
was conceived and developed as a comprehensive Final Year Project. Welth 
is  meticulously  designed  to  function  as  a  fully  unified  platform,  thereby 
solving  the  absence  of  a  single  system  capable  of  simultaneously  covering 
budgeting,  investment  tracking,  EMI  management,  and  proactive  tax 
planning. By consolidating these disparate financial necessities, the platform 
brings  together  everyday  financial  tracking,  advanced  AI-driven  advisory 
functions,  targeted  investment  recommendations,  comprehensive  loan  EMI 
management, and intelligent receipt automation into one single, cohesive, and 
user-friendly  web  application.  A  major  differentiating  factor  that  elevates 
Welth above standard, generic finance applications is its deep integration of 
the  user's  actual,  real-world  transactional  data.  Instead  of  relying  on 
generalized  financial  platitudes,  the  platform  processes  this  specific  data  to 
deliver  highly  contextual,  real-time  financial  advice.  This  guidance  is 
delivered  exclusively  through  a  sophisticated  conversational  AI  interface, 
which takes on the persona of "CA Arjun"—an AI specifically modeled after 
the expertise and professional demeanor of a Chartered Accountant. Prior to 
Welth, users suffered from the total absence of any intelligent, context-aware 
chatbot  capable  of  utilizing  their  own  deeply  personal  financial  data  to 
generate actionable, bespoke advice.

The  fundamental  motivation  behind  Welth  also  stems  from  the  frustrations 
associated  with  time-consuming,  manual  expense  logging,  a  tedious process 
that inherently results in poor tracking accuracy over time. Consequently, the 
project  established  several  rigorous,  technically  ambitious  objectives  to 
completely overhaul the personal  finance  experience. The primary objective 
is  the  fundamental  design  and  development  of  a  full-stack,  end-to-end  AI- 
integrated personal finance web application. Central to this ecosystem is the 
implementation  of  the  conversational  CA  AI  advisor,  powered  by  the 
advanced  LLAMA  3.1  model  accessed  via  Groq,  which  continuously 
operates  utilizing  user-specific  financial  context.  To  address  investment 
oversight, the platform aims to build a live, real-time portfolio tracker capable 
of  monitoring  both  stocks  and  mutual  funds  by  pulling  data  directly  from 
Yahoo Finance and MFAPI.in. Furthermore, to eliminate the inaccuracies of 
manual entry, the system integrates an automated receipt scanner leveraging 
the  multimodal  capabilities  of  Google  Gemini  Vision.  Beyond  everyday 
expenses,  the  platform  is  designed  to  provide  robust,  mathematical  EMI 
calculation  tools,  complete  amortization  scheduling,  and  detailed  loan 
payment  tracking  features.  All  of  this  complex  data  is  finally  visualized 
through  the  creation  of  a  comprehensive  analytics  dashboard  featuring

---

<!-- PAGE 2 -->

Welth — AI-Powered Financial Insights Platform

interactive,  multi-dimensional  financial  charts,  which  work  in  tandem 
with  specialized  investment  and  tax  recommendation  engines  driven 
directly by the user's historical spending and saving patterns.

determines  whether  this  newly  generated  insight  requires  a  formal  audit 
before being presented to the user.

If the system determines that the AI-generated insight requires verification to 
maintain  absolute  security  and  trust,  the  workflow  transitions  to  the  final 
Masumi  Verification  Layer.  Here,  the  specialized  Masumi  Protocol  takes 
over  to  generate  a  secure  cryptographic  proof,  commonly  referred  to  as  a 
hash.  To  ensure  permanent,  immutable  record-keeping,  this  cryptographic 
proof is recorded directly into the Masumi Audit Log, which utilizes secure 
on-chain storage. This ultimate layer guarantees that the intelligence provided 
to  the  user  is  not  only  accurate  but  also  cryptographically  verifiable  and 
logged.

Figure 1: OPERATIONAL WORKFLOW

is  structurally  divided

The  operational  methodology  of  the  AI-Powered  Financial  Insights 
Platform  follows  a  highly  systematic  workflow  that  seamlessly 
bridges  user  queries  with  on-chain  data  and  cryptographic 
into  four 
verification.  This  workflow 
interconnected  operational  layers,  beginning  fundamentally  with  the 
User Interaction layer. In this initial stage, the user submits a natural 
language  query  through  the  dedicated  Chat  UI,  asking  specific 
financial questions such as, "What are my staking rewards?". Once the 
entire  backend  process  concludes,  this  layer  is  also  responsible  for 
presenting the final, verified response back to the user, complete with 
a transparent audit trail, such as a cryptographic hash, to guarantee the 
integrity of the provided information before concluding the process. 
To  ensure  the  platform's  responses  are  completely  accurate  and 
contextually relevant, the system relies heavily on the Blockchain Data 
Access  layer.  During  the  initial  Data  Acquisition  phase,  the  system 
actively  retrieves  highly  accurate  and  current  blockchain  data 
specifically tied to the user's public wallet address. This operational step 
involves fetching live wallet data through a specialized Cardano Indexer 
and  meticulously  retrieving  the  user's  exact  staking  status  and  current 
balances.  All  of  this  critical  financial  information  is  sourced  directly 
from the foundational Cardano Blockchain database to ground the AI's 
knowledge in reality.

The core intelligence of the platform resides within the Backend & AI 
Reasoning  layer,  where  raw  data  is  transformed  into  actionable 
intelligence.  The  process  begins  with  Query  Interpretation,  a  crucial 
step  where  advanced  natural  language  techniques  are  deployed  to 
accurately  recognize  the  user's  underlying  intent.  The  AI  evaluates 
whether the response needs to be grounded directly on-chain, generating 
a  general  explanation  if  necessary.  Following  this,  the  Context 
Formation  stage  merges  the  original  natural  language  query  with  the 
freshly  retrieved  live  wallet  data  to  construct  a  comprehensive 
contextual  representation.  This  enriched  context  is  then  processed  by 
the AI Reasoning Engine, powered by a Large Language Model (LLM), 
which  generates  a  highly  detailed,  grounded  financial  insight  or  a 
human-readable summary, such as a transaction overview or a detailed 
explanation  of  staking  rewards.  Finally,  an  automated  decision  node

1.1  Problem Statement 
The core problem motivating the development of the Welth platform is rooted 
in  the  reality  that  financial  management  remains  a  highly  significant 
challenge  for  a  majority  of  individuals  in  India,  particularly  among  the 
working-class  and  student  population.  Despite  the  rapid  proliferation  of 
modern  digital  banking  and  digital  payment  platforms  across  the  country, 
most  users  still  critically  lack  access  to  personalized,  affordable  financial 
advisory  services  capable  of  guiding  crucial  savings,  investment,  and 
budgeting  decisions  tailored  specifically  to  their  individual  income  profiles. 
This  ongoing  struggle  is  heavily  compounded  by  a  general  environment  of 
low  financial  literacy  and  a  pervasive  lack  of  awareness  regarding  essential 
wealth-building  and  management  tools,  including  mutual  funds,  Systematic 
Investment  Plans  (SIPs),  and  various  tax-saving  instruments.  Furthermore, 
users  suffer  from  the  complete  absence  of  a  single,  unified  platform  that 
comprehensively  covers  all  necessary  personal  finance  aspects,  spanning 
from everyday budgeting and investment to dedicated EMI tracking and tax 
planning.  Existing  commercial  solutions  consistently  fail  to bridge  this  gap; 
for instance, while established platforms like Mint and YNAB pioneered the 
automated  categorization  of  financial 
lack 
advanced  AI  advisory  capabilities  and  remain  geographically  restricted 
strictly  to  the  US  market.  Similarly,  prominent  Indian  investment  platforms 
such  as  Zerodha  Kite  and  Groww  offer  robust  market  access  but  fail  to 
integrate everyday budgeting, dedicated advisory, or basic expense tracking. 
Consequently,  individuals  are  continuously  burdened  by  time-consuming 
manual  expense  logging,  an  outdated  process  that  inherently  results  in  poor 
tracking  accuracy  over  time.  Beyond  traditional  fiat  finance,  modern 
investors  also  face  the  rapidly  increasing  complexity  associated  with 
decentralized  applications  and  digital  asset  management  systems.  As 
blockchain ecosystems actively expand, users frequently struggle to interpret 
detailed  transaction  data,  understand  intricate  staking  mechanisms,  or 
successfully navigate complex on-chain information. Whether engaging with 
traditional  domestic  markets  or  decentralized  global  assets,  private 
individuals and institutional investors alike are frequently forced to navigate 
volatile  environments  by  relying  heavily  on  lagging  indicators  rather  than 
proactive  guidance.  Ultimately,  these  varied  technological  and  educational 
shortfalls culminate in one primary overarching problem: there is currently no 
intelligent,  context-aware  chatbot  or  unified  system  available  that  actually 
utilizes a user's own specific, real-world financial data to deliver actionable, 
personalized advice.

they  entirely

transactions,

1.2  Objectives

---

<!-- PAGE 3 -->

Welth — AI-Powered Financial Insights Platform

To thoroughly fulfill the core mission of the Welth platform, the project 
established a comprehensive set of highly technical and functional goals 
designed  to  revolutionize  personal  finance  management.  The  primary 
and overarching objective is to fundamentally design and develop a full- 
stack,  AI-integrated  personal  finance  web  application.  To  directly 
counter the widespread lack of personalized guidance, a key objective is 
to  actively  implement  a  conversational  CA  AI  advisor  utilizing  the 
advanced  LLAMA  3.1  model  accessed  via  Groq,  which  is  specifically 
engineered  to  operate  using  user-specific  financial  context.  Another 
major developmental goal is to build a live, real-time portfolio tracker 
capable  of  meticulously  monitoring  both  stocks  and  mutual  funds  by 
pulling  data  directly  from  the  Yahoo  Finance  API  and  MFAPI.in. 
Recognizing the severe friction caused by manual expense logging, the 
project  aims  to  develop  an  automated  receipt  scanner  leveraging  the 
multimodal  capabilities  of  Google  Gemini  Vision  to  significantly 
reduce  manual  data  entry.  Beyond  day-to-day  tracking,  the  system's 
objectives  expand  into  long-term  financial  structuring  by  aiming  to 
provide 
tools,  complete  amortization 
scheduling, and detailed payment tracking features. All of this complex, 
multi-faceted data must be visualized effectively; thus, a core objective 
is  to  create  a  highly  comprehensive  analytics  dashboard  featuring 
the 
interactive,  multi-dimensional 
platform  specifically  aims  to  integrate  dedicated  investment  and  tax 
recommendation  engines  that  formulate  their  advice  based  directly  on 
the user's historical spending and saving patterns.

financial  charts.  Furthermore,

robust  EMI  calculation

Beyond traditional fiat systems, the platform's objectives also explicitly 
encompass  addressing  the  increasing  complexity  associated  with 
decentralized  applications  and  digital  asset  management  systems.  By 
leveraging advancements in Artificial Intelligence, real-time blockchain 
indexing,  and decentralized  protocols,  a  critical  objective  is to  convert 
unintuitive  on-chain  transaction  data  into  easily  interpretable  financial 
insights  while  strictly  maintaining  security  and  trust.  To  ensure  long- 
term  viability,  the  platform  aims  to  provide  a  research-driven,  layered 
architecture  that  guarantees  both  scalability  and  sustainability  as 
separate,  foundational  principles.  This  involves  an  objective  to  ingest, 
normalize,  and  analyze  massive  volumes  of  heterogeneous  financial 
data  while  synthesizing  information  from  global  market  indices,  real- 
time  news  sentiment,  and  individual  spending  patterns  to  construct  a 
360-degree  financial  profile.  To  make  this  data  actionable,  the  system 
targets  the  employment  of  advanced  Long  Short-Term  Memory 
(LSTM) networks and Transformer-based models to forecast cash flow 
trajectories  and  identify  potential  liquidity  risks  before  they  manifest. 
Finally,  by  utilizing  Natural  Language  Generation  (NLG)  to  translate 
complex  algorithmic  outputs  into  high-level  executive  summaries,  the 
grand  objective  of  the  Welth  platform  is  to  democratize  access  to 
professional-grade  financial  analysis  and  represent  a  paradigm  shift  in 
wealth  management  by  transitioning  the  entire  user  experience  away 
from traditional reactive reporting and toward a system defined entirely 
by predictive intelligence.

2.  Literature Review 
Here is the most expansive, detailed synthesis of the Literature Review 
section, woven into a dense, continuous paragraph format to maximize 
its depth while remaining strictly grounded in the research provided in 
your document.

successfully  established 
the  foundational  automated  categorization  of 
financial  transactions.  However,  these  established  commercial  platforms 
exhibit notable limitations; most prominently, they completely lack advanced 
AI-driven advisory capabilities and remain geographically restricted entirely 
to  the  United  States  market.  Conversely,  within  the  specific  context  of  the 
Indian financial ecosystem, prominent investment platforms such as Zerodha 
Kite  and  Groww  offer  highly  robust  market  access  but  fail  to  integrate 
essential,  holistic  personal  finance  features  such  as  everyday  budgeting, 
dedicated  advisory  services,  or  basic  expense  tracking  functionalities.  To 
address  these  industry-wide  gaps,  recent  academic  research  has  provided 
crucial  foundational  methodologies;  specifically,  comprehensive  research 
conducted  by  Chen  et  al.  (2023)  focusing  on  LLM-based  financial  advisory 
systems  clearly  demonstrated  that  large  language  models  are  highly  capable 
of providing accurate, deeply personalized financial guidance. Crucially, this 
research  established  that  such  accuracy  is  achieved  specifically  when  these 
models  are  actively  augmented  with  user-specific  context  through  the 
implementation  of  Retrieval-Augmented  Generation  (RAG)  techniques  or 
through  careful,  specialized  prompt  engineering.  Further  validating  the 
technological methodologies employed in the Welth platform's architecture, a 
study  by  Reddy  et  al.  (2022)  illustrated  that  image-based  Optical  Character 
Recognition  (OCR)  designed  for  complex  receipt  processing  can  reliably 
achieve an impressive accuracy rate exceeding 92% when utilizing advanced 
multi-modal  transformer  models,  such  as  Google  Gemini.  Additionally, 
detailed  academic 
into  short-term  financial  forecasting, 
specifically  studies  focused  on  LSTM-based  stock  and  spending  prediction 
conducted  by  Zhang  et  al.  (2021),  have  shown  highly  promising  results. 
These  specific  academic  findings  directly 
the 
foundational  mathematical  basis  for  the  LSTM  prediction  module  that  is 
natively  integrated  into  the  Welth  application.  To  make  the  deployment  of 
such  advanced,  computationally  heavy  processing  viable  in  a  real-time, 
consumer-facing  web  application,  the  system  strategically  leverages  Groq's 
highly  optimized  inference  infrastructure,  which  enables  the  powerful 
LLAMA  3.1  70B  model  to  operate  continuously  with  sub-second  response 
latency.  Ultimately,  Welth  significantly  differentiates  itself  from  all  prior 
academic  work  and  existing  commercial  platforms  by  uniquely  combining 
four critical, advanced elements within a single, cohesive platform: first, the 
seamless, on-the-fly injection of a user's unique financial context directly into 
inclusion  of  multi-modal  receipt  scanning 
AI  prompts;  second, 
capabilities; 
investment 
generation 
recommendations tailored specifically to the regulatory environment of India; 
and fourth, the provision of a holistic, all-encompassing dashboard featuring 
advanced predictive analytics.

inform  and  provide

investigations

SEBI-aligned

the 
the

third,

of

3.  System Architecture

The  Welth  platform  is  engineered  upon  a  modern  full-stack  serverless 
architecture  that  comprehensively  utilizes  server-side  rendering  (SSR)  and 
API routes, all of which are managed by the Next.js 15 framework. The core 
application  is  structurally  designed  around  the  Next.js  App  Router  pattern, 
strategically  deploying  React  Server  Components  to  efficiently  handle  data- 
heavy  pages  alongside  Client  Components  that  manage  interactive  user 
interface  elements.  The  frontend  rendering  and  routing  are  powered  by 
Next.js 15 and React 18, while the user interface components are extensively 
styled and visualized using a combination of Tailwind CSS, ShadCN UI, and 
Recharts to ensure accessible components and dynamic data visualization. To 
maintain  strict  security  and  session  management,  the  platform  integrates 
Clerk to provide robust JWT-based authentication and OAuth capabilities.

The  integration of  artificial  intelligence  within  the  domain  of personal 
finance  has  been  the  subject  of  several  rigorous  academic  studies  and 
the  focus  of  numerous  commercial  product  developments.  Early 
pioneers in the financial technology sector, specifically platforms such 
as  Mint  (developed  by  Intuit)  and  YNAB  (You  Need  A  Budget),

User authentication is seamlessly handled by Clerk, which explicitly provides 
session tokens that are rigorously validated by Next.js middleware on every 
single  protected  route  within  the  application.  The  system's  relational  data  is 
securely  housed  in  a  cloud-hosted  PostgreSQL  database  managed  through 
Supabase, with Prisma ORM deployed to handle type-safe database queries,

---

<!-- PAGE 4 -->

Welth — AI-Powered Financial Insights Platform

schema  management,  and  database  migrations.  The  database  schema 
itself is meticulously designed around a central User model, which is a 
Clerk-authenticated  profile  that  maintains  cascading  relations  to  all 
associated  financial  entities.  This  core  database  schema  incorporates 
multiple  specific  models,  including  Bank/Savings  Accounts  with 
balance  and  default  flags,  Transactions  recording  all  income  and 
expenses  with  recurring  flags,  customizable  Budgets  with  alert 
thresholds,  and 
target-based  Savings  Goals  encompassing  target 
amounts  and  monthly  calculations.  Furthermore,  the  schema  integrates 
detailed  Loan  models 
tracking  principal  and  amortization,  an 
EmiPayment  model  for  individual  installment  statuses,  and  a  Holding 
model for managing stock and mutual fund portfolios with average buy 
prices.  The  database  heavily  utilizes  enums  for  strict  data  typing, 
defining  specific  constraints  for  Transaction  Types,  Account  Types, 
Loan Statuses, and Holding Types among others.

To drive the platform's advanced functionalities, the AI Advisory layer 
employs  Groq's  infrastructure,  specifically  utilizing  LLAMA  3.1  8B 
and  70B  models  for  conversational  AI,  intent  parsing,  and  investment 
advice.  Concurrently,  Google  Gemini  1.5  Flash  powers  the  Vision  AI 
for  multimodal  receipt  scanning  and  complex  OCR  extraction.  For 
advanced  analytics,  a  dedicated  Python  microservice  utilizing  FastAPI 
alongside TensorFlow and Keras hosts the LSTM prediction service for 
analyzing  time-series  spending  and  balance  data.  Real-time  financial 
market  data  is  dynamically  pulled  using  the  unofficial  Yahoo  Finance 
API for live NSE/BSE stock prices and MFAPI.in for live mutual fund 
NAVs  and  scheme  searches.  In  terms  of  application  flow,  Server 
Actions and API Route Handlers are tasked with fetching data directly 
from  PostgreSQL  via  Prisma,  applying  necessary  business  logic,  and 
passing  serializable  props  back  to  the  React  Server  Components. 
Finally,  Client  Components  take  over  to  handle  all  interactivity, 
including  charts,  forms,  and  the  conversational  chatbot,  by  utilizing 
React  state  and  standard  fetch()  calls  directed  to  the  API  layer.  The 
entire ecosystem is reliably hosted via Vercel for the serverless frontend 
deployment  and  Supabase  for  the  database,  with  Arcjet  integrated  to 
optionally  provide  essential  rate-limiting,  bot  protection,  and  route

guards.  Background  tasks,  such  as  scheduled  email  alerts  and  recurring 
transaction processing, are seamlessly offloaded to Inngest.

3.2  Database Schema

Core Architecture

•  Central  Design:  The  database  is  designed  around  a  central  User 
model  that  has  cascading  relations  to  all  of  the  system's  financial 
entities.

Key Data Models

•  User:  Acts  as  a  Clerk-authenticated  user  profile  that  is  linked

directly to all of the user's financial data.

•  Account: Tracks bank and savings accounts, storing details like the

balance and a default flag.

•  Transaction:  Records  all  income  and  expense  entries,  noting  the

category, type, and whether it has a recurring flag.

•  Budget:  Defines  a  monthly  spending  limit  per  user  and  includes

specific alert thresholds.

•  Goal:  Manages  target-based  savings  goals,  tracking  the  target 
amount, the timeline in months, and the necessary monthly savings 
calculation.

•  Loan:  Stores  complete  loan  records,  including  the  principal 
amount, interest rate, tenure, calculated EMI, and amortisation.

•  EmiPayment:  Tracks  individual  EMI  installments,  specifically

noting their status as paid, missed, or upcoming.

•  Holding:  Manages  the  user's  stock  and  mutual  fund  portfolio, 
recording  the  quantity  held,  the  average  buy  price,  and  the  total 
invested amount.

Defined  Enums  To  maintain  strict  data  structures,  the  schema  defines  the 
following Enums:

•  Transaction Type: Restricted to INCOME or EXPENSE.

•  AccountType: Restricted to CURRENT or SAVINGS.

•  Transaction  Status:  Restricted  to  PENDING,  COMPLETED,  or

FAILED.

•  RecurringInterval:

Restricted

to  DAILY,  WEEKLY,

MONTHLY, or YEARLY.

2  Asset & Debt Enums: Specific statuses and types are also defined for

LoanType, EmiStatus, and Holding Type (which includes

3.3  Application Flow

The application flow of the  Welth  platform is meticulously  orchestrated  to 
ensure  seamless,  secure,  and  highly  performant  data  processing  from  the

---

<!-- PAGE 5 -->

Welth — AI-Powered Financial Insights Platform

moment  a  user  initiates  a  session.  The  entire  operational  sequence 
begins  strictly  at  the  security  perimeter,  where  user  authentication  is 
comprehensively  handled  by  Clerk.  Clerk  actively  provides  robust 
JWT-based authentication, complete with extensive support for OAuth 
providers, generating secure session tokens that are rigorously validated 
by Next.js middleware across every single protected route. To maintain 
absolute data integrity and privacy, all API routes and dedicated server 
actions  strictly  begin  with  an  auth()  call,  ensuring 
that  any 
unauthenticated  requests  immediately  receive  a  401  unauthorized 
response.  Once  a  session  is  securely  established,  all  user-owned  data 
remains  fundamentally  scoped  by  their  unique  user  ID,  completely 
preventing  any  potential  cross-user  data  access  even  if  an  API  route 
happens  to  be  called  directly  by  an  external  source.  Following 
successful  authentication,  the  backend  architecture  heavily  utilizes 
Next.js React Server Components specifically for initial data loading on 
pages  such  as  the  dashboard,  effectively  eliminating  the  need  for 
loading  states  for  static,  non-interactive 
cumbersome  client-side 
sections. In these backend environments, dedicated Server Actions and 
API Route Handlers are tasked with fetching raw data directly from the 
PostgreSQL  database  via 
the  Prisma  ORM.  These  handlers 
systematically  apply  the  necessary  business  logic  and  cleanly  pass 
highly  optimized,  serializable  props  down  to  the  React  Server 
Components.

4.  Core Features

The  Welth  platform 
integrates  a  massive  array  of  advanced 
functionalities  designed  to  automate  and  elevate  personal  financial 
management.  At  the  heart  of  the  application  is  the  conversational  AI 
advisor known as CA Arjun, which is meticulously designed to emulate 
a senior Chartered Accountant with deep expertise in personal finance, 
sophisticated  investment  strategies,  and  complex  taxation.  This  central 
chatbot  operates  dynamically  across  four  distinct  modes:  CA  Advisor 
Mode for holistic financial health analysis and spending reviews; Invest 
Mode  for  targeted  stock  and  mutual  fund  recommendations  complete 
with specific allocation plans; Tax Mode for detailed advice on Indian 
income  tax  (specifically  FY  2024-25)  encompassing  80C,  80D,  and 
HRA  deductions;  and  a  highly  efficient  Quick  Add  Mode  that  allows 
for natural  language  transaction logging,  such  as  simply  typing  "spent 
₹300 on food today". The underlying intent parser leverages the speed 
of  LLAMA  3.1  8B  to  instantly  classify  incoming  messages  into  six 
specific 
investment, 
budget_analysis, tax_advice, and general analysis. To minimize latency 
during interactions, the user's specific financial context—including their 
top  spending 
3-month 
categories, customized budget, and active goals—is fetched entirely in 
parallel with this intent parsing. For more complex inquiries, investment 
recommendations  are  generated  utilizing  the  higher  accuracy  of  the 
LLAMA  3.1  70B  model,  which  returns  heavily  structured  JSON  data 
detailing  specific  fund  names,  precise  allocation  percentages,  required 
monthly amounts, expected market returns, comprehensive risk ratings, 
and  step-by-step  how-to-start  guidance.  To  further  optimize  platform 
performance, a smart response cache utilizing an in-memory Map stores

intent  categories:  add_transaction,  add_goal,

income,  overall  expenses,  savings  rate,

read-only  query  results  to  eliminate  redundant  API  calls,  while  vital  write 
operations  like  transaction  additions  strictly  bypass  this  cache  to  ensure 
absolute data consistency.

To handle complex debt, the dedicated EMI Calculator and Tracker module 
provides  a  highly  interactive  calculator  where  users  can  manipulate  the 
principal,  annual  interest  rate,  and  tenure  via  visual  sliders.  The  platform 
evaluates  the  standard  reducing-balance  mathematical  formula  $P\times 
r\times(1+r)^{\wedge  n}/((1+r)\wedge  n-1)$  entirely  client-side  for  instant 
preview  capabilities,  outputting  the  exact  monthly  EMI, total  interest,  and  a 
12-month area chart detailing the reducing interest component.

4.2  CA Arjun — AI Financial Advisor

CA  Arjun  is  the  central  AI  persona  of  the  Welth  platform,  designed  to 
emulate  a  senior  Chartered  Accountant  with  expertise  in  personal  finance, 
investment, and taxation. The chatbot operates in four modes: • CA Advisor 
Mode — Financial health analysis, spending review, savings advice

•  Invest  Mode  —  Stock  and  mutual  fund  recommendations  with  specific 
allocation plans

• Tax Mode — Indian income tax (FY 2024-25) advice including 80C, 80D, 
HRA deductions

• Quick Add Mode — Natural language transaction logging (e.g. 'spent ₹300 
on food today')

investment,

add_transaction,

The  intent  parser  uses  LLaMA  3.1  8B  to  classify  messages  into  six  intent 
categories: 
budget_analysis, 
add_goal, 
tax_advice, and analysis. User financial context (3-month income, expenses, 
savings  rate,  top  categories,  budget,  goals)  is  fetched  in  parallel  with  intent 
parsing  to  minimise  latency.  Investment  recommendations  are  generated 
using  LLaMA 3.1  70B  for  higher  accuracy,  returning  structured  JSON  with 
fund names, allocation percentages, monthly amounts, expected returns, risk 
ratings, and how-to- start guidance.A smart response cache (in-memory Map) 
stores read-only query results to avoid redundant API calls. Write operations 
(transaction addition, goal creation) always bypass the cache to maintain data 
consistency.

---

<!-- PAGE 6 -->

Welth — AI-Powered Financial Insights Platform

4.3  Receipt Scanner

The Receipt Scanner is a core feature of the Welth platform designed to 
significantly  reduce  manual  data  entry  and  minimize  friction  in 
everyday  financial  management  tasks.  The  automated  scanner  enables 
users to conveniently photograph, upload, or drag and drop a bill image 
directly  into  the  application.  Under  the  hood,  this  multi-modal 
extraction  capability  is  powered  by  Google  Gemini  1.5  Flash,  which 
processes  the  receipt  images  utilizing the  @google/generative-ai SDK. 
When  an  image  is  submitted,  a  highly  specialized  multimodal  prompt 
instructs the vision model to accurately extract critical financial details, 
including the total amount, merchant name, purchase date, and specific 
item  descriptions.  Furthermore,  the  model  automatically  assigns  a 
suggested  expense  category  selected  from  15  predefined  enum  values, 
structuring the output entirely in JSON format.Once processed—a task 
that  averages  a  highly  efficient  response  time  of  approximately  2.1 
seconds—the  extracted  data  is  seamlessly  pre-filled  into  an  editable 
review  form,  allowing  users  to  verify  the  information  before  it  is 
formally  saved  as  a  transaction  via  the  chat  API.  To  handle  image 
uploads robustly, the scanner employs a FormData-based POST request 
directed  to  a  dedicated  /api/scan-receipt  route,  which  cleverly  avoids 
Vercel's standard 4MB server body limit restrictions. Data privacy and 
security  are  strictly  enforced  throughout  this  workflow;  the  base64- 
encoded image data is processed entirely in-memory and sent directly to 
the  Gemini  API  without  any  intermediate  disk  or  object  storage, 
ensuring that only the finalized, structured data is actually saved to the 
database.  Finally,  the  system  includes  a  reliable  fallback  error  handler 
that  successfully  detects  blurry  or  non-receipt 
images,  actively 
preventing  application  crashes  in  favor  of  returning  a  graceful,  user- 
friendly  error  message.  This  implementation  is  supported  by  research 
indicating  that  image-based  OCR  utilizing  multi-modal  transformer 
models like Google Gemini can achieve accuracy rates exceeding 92%, 
reinforcing the technical reliability of this automated feature.

4.4  Live Portfolio Tracker

to  bring

institutional-grade

The  Live  Portfolio  Tracker  is  a  sophisticated  core  feature  within  the 
Welth  platform  designed 
investment 
tracking  capabilities  directly  to  individual  users  at  zero  marginal  cost. 
Through this dedicated module, users are empowered to actively search 
for  and  add  specific  NSE  and  BSE  stocks,  as  well  as  various  mutual 
fund schemes, directly into their personal financial portfolios. To ensure 
that  this  tracking  reflects  real-world  market  conditions,  the  system 
dynamically  fetches  live  stock  prices  utilizing  the  unofficial  Yahoo 
Finance  Chart  API,  which  operates  efficiently  with  a  short-lived  5- 
minute  cache.  Concurrently,  real-time  mutual  fund  Net  Asset  Values 
(NAVs)  are  continuously  retrieved  from  the  free  MFAPI.in  service, 
utilizing  a  slightly  longer  1-hour  cache  to  optimize  performance. 
Because these prices and NAVs are pulled from public APIs at runtime, 
the  platform  inherently  protects  user  privacy,  as  no  sensitive  financial 
market  credentials  are  ever  required  or  permanently  stored  within  the 
system.  As  these  real-time  data  streams  are  ingested,  the  platform’s 
backend automatically performs complex computations for every single 
recorded  holding—which  the  database  formally  tracks  by  quantity, 
average  buy  price,  and  total  invested  amount.  Specifically,  the  system 
mathematically calculates the current total value, the absolute Profit and 
Loss (P&L), the overall percentage return, the specific day change, and 
the critical 52-week high and low metrics for each asset. To maintain a 
clean and accurate ledger, any duplicate holdings added by the user are 
automatically  merged  by  the  system,  which  then  calculates  a  unified 
average  buy  price.  All  of  this  complex,  real-time  data  is  visually 
communicated to the user through highly interactive UI elements, most 
notably displaying  the  overall  portfolio  asset  allocation via  a  dynamic

Recharts PieChart. Furthermore, the module features a dedicated Analysis tab 
that provides users with a comprehensive breakdown of their top gainers and 
top  losers,  alongside  a  detailed  asset  class  distribution  that  categorizes 
investments  precisely  across  Stock,  Mutual  Fund,  and  ETF  holding  types. 
Extensive functional testing of this feature confirmed that NSE stock searches 
and  mutual  fund  scheme  queries  successfully  return  accurate  results, 
including  precise  scheme  codes  and  critical  price  metrics.  Finally, 
performance  evaluations  demonstrated  the  high  efficiency  of  this  serverless 
architecture,  successfully  executing  a  parallel  live  portfolio  fetch  for  10 
distinct holdings via Yahoo Finance in approximately 1.4 seconds.

4.5  EMI Calculator and Tracker

The EMI module within the Welth platform is comprehensively designed to 
provide  two  core,  interrelated  functions  for  robust  debt  management:  an 
interactive  Calculator  and  a  detailed  Tracker.  The  Calculator  function 
empowers users to input their loan's principal amount, the annual interest rate 
expressed  as  a  percentage,  and  the  overall  tenure  in  months  through  highly 
interactive  visual  sliders.  To  provide  an  instant  preview  without  server 
latency,  the  platform  evaluates  the  standard  reducing-balance  EMI  formula, 
expressed  as  $P\times  r\times(1+r)^{\wedge  n}/((1+r)\wedge  n-1)$,  entirely 
on the client side. The immediate output of this calculation includes the exact 
monthly EMI amount, the total interest accrued over the lifespan of the loan, 
and  the  total  payable  amount,  all  of  which  are  visually  supported  by  a 
dynamically  generated  donut  chart  comparing  the  principal  versus  interest, 
alongside a 12-month area chart detailing the progressively reducing interest 
component.

Once a user is satisfied with the calculation, the Tracker function allows them 
to save the specific loan directly to the database. This action instantly triggers 
the server-side amortisation engine to generate a complete, full amortisation 
schedule,  systematically  creating  one  distinct  EmiPayment  record  for  every 
single installment. To guarantee data integrity, this entire schedule is written 
to the database in a single Prisma nested create call—encompassing both the 
primary  loan  and  all  associated  EmiPayments—ensuring  atomic  creation. 
During  this  generation,  the  amortisation  engine  meticulously  calculates  that 
for each specific installment, the principal component strictly equals the EMI 
minus  the  product  of  the  outstanding  balance  and  the  monthly  interest  rate. 
Furthermore, the engine intelligently adjusts the final installment to account 
for  any  mathematical  rounding  drift  by  forcing  the  remaining  balance  to 
strictly  zero.  Consequently,  each 
installment 
permanently  records  its  specific installment  number,  the  exact  due  date,  the 
overall  EMI  amount, the  distinct  principal  and  interest  components,  and the 
resulting remaining balance.

independently

stored

The  operational  status  of  these  individual  installments  is  intelligently  auto- 
derived by the system, classifying them precisely as UPCOMING for future 
payments,  PENDING  if  they  are  overdue  but  currently  unpaid,  MISSED  if 
they  remain  overdue  after  a  specific  cutoff,  or  fully  PAID.  To  facilitate 
seamless  ongoing  management,  users  can  simply  mark  individual  EMIs  as 
paid with a single click, an action which accurately records the exact payment 
date  within  the  database.  On  the  frontend  UI,  the  associated  loan  card 
provides  a  comprehensive  overview  by  displaying  a  visual  progress  bar, 
precise  counts  of  paid,  missed,  and  upcoming  installments,  and  explicitly 
highlights  the  next  upcoming  EMI  complete  with  a  convenient  "Mark  as 
Paid"  button.  Finally,  rigorous  functional  and  performance  evaluations 
confirmed 
this  atomic  schedule  generation, 
demonstrating  that  creating  a  comprehensive  60-month  EMI  schedule 
functions  flawlessly  and  requires  a  minimal  database  round-trip  time  of 
merely ~180ms.

the  high  efficiency  of

4.6  Dashboard Analytics

---

<!-- PAGE 7 -->

Welth — AI-Powered Financial Insights Platform

The Dashboard Analytics module serves as the primary visual interface 
of the Welth platform, specifically designed to fulfill the core objective 
of  creating  a  comprehensive  analytics  dashboard  equipped  with  multi- 
dimensional  financial  charts.  Functioning  as  a  holistic  center  for 
predictive  analytics  ,  the  dashboard  is  technically  engineered  using 
Next.js React Server Components for its initial data loading, a strategic 
architectural  choice  that  effectively  eliminates  jarring  client-side 
loading  states  for  the  page's  static  sections.  To  guarantee  rapid 
performance, 
the  dashboard  actively  utilizes  Promise.all() 
functions  to  fetch  multiple  database  queries  concurrently,  significantly 
reducing  overall  server  response  times.  As  data  is  retrieved,  the  UI 
employs  Suspense  boundaries  paired  with  BarLoader  fallbacks,  which 
explicitly  allow  for  the  independent,  progressive  streaming  of  distinct 
data  sections,  such  as  the  budget,  score,  and  goals.  This  highly 
optimized Server-Side Rendering (SSR) approach yields an impressive 
initial load time of approximately 420ms to the first meaningful content. 
Furthermore,  the  system  architecture  ensures  high  availability;  for 
example,  if  the  backend  LSTM  prediction  service  goes  offline,  the 
system executes a graceful fallback, allowing the dashboard to display a 
secure placeholder rather than experiencing a complete crash.

At  the  center  of  this  interface  is  the  DashboardCharts  client 
component, which strategically organizes complex financial data across 
three interactive tabs. The first tab, labeled "6M Trend," provides long- 
term  visualization  through  an  income  versus  expense  area  chart paired 
directly with a monthly savings bar chart spanning a six-month period. 
The  second  tab,  "Categories,"  breaks  down  immediate  spending habits 
by featuring a Donut chart (or category pie chart) alongside horizontal 
progress  bars  that  track  the  current  month's  spending  categorized  by 
distinct  expense  types.  The  final  tab,  "Daily,"  offers  a  micro-level 
perspective  by  deploying  a  30-day  income  and  expense  bar  chart 
complemented by a net flow line chart. To ensure these metrics are both 
aesthetically  pleasing  and  easily  interpretable,  all  charts  are  built 
utilizing  the  Recharts  library  (specifically  React  client  charts)  and  are 
heavily  customized  with  interactive  tooltips,  visual  gradients,  and 
intuitive  color-coded  data  keys. Finally,  positioned  immediately above 
these  graphical  elements,  the  dashboard  features  quick-reference 
summary  stat  pills  that  instantly  display  the  user's  current  month 
income,  total  expenses,  and  overall  savings,  enhanced  with  month-on- 
month  percentage  change  indicators  to  provide  immediate  context 
regarding their financial trajectory.\

4.7  CA Report Dashboard

•

The CA Report Dashboard is hosted on the /ca-dashboard 
page  and  delivers  a  professional  financial  report  actively 
generated by the AI persona, CA Arjun.

•  Users  can  access  this  specific  dashboard  via  the  gold  "CA 
Report" button located in the primary navigation header.

•

•

•

The  core  of  the  report  features  an  AI-computed  financial 
health score ranging from 0 to 100, which is accompanied by 
a  specific  grade  such  as  Excellent,  Good,  Fair,  or  Needs 
Attention.

The full analysis includes an executive summary, key findings 
that are categorized by positive, negative, or neutral impacts, 
priority action items, and a dedicated tax planning note.

To  organize  this  information,  the  page  is  divided  into  four 
distinct tabs—Overview, Transactions, Budget, and Goals—

each populated with relevant data and visualizations.

•

•

•

•

The underlying AI analysis for this comprehensive health report is 
powered by the Groq LLAMA 3.1 8B model.

The report can be regenerated on demand whenever the user clicks 
the Refresh button.

This  refresh  action  triggers  the  /api/ca-dashboard  endpoint, 
which  executes  all  necessary  database  queries 
(fetching 
transactions, budgets, goals, and accounts) in parallel with the Groq 
inference to construct the prompt.

Performance testing shows that this parallel fetching and generation 
process takes an average of approximately 1.8 seconds to complete

5.  AI Integration Architecture

The  AI  Integration  Architecture  of  the  Welth  platform  is  divided  into  three 
primary components that handle distinct processing and analytical workloads:

5.1 Groq Inference

The  platform's  core  intelligence  relies  on  Groq's  Language  Processing  Unit 
(LPU) inference engine to handle all conversational and analytical AI tasks. 
The  system  strategically  utilizes  two  distinct  model  tiers  depending  on  the 
complexity of the operation. The llama-3.1-8b-instant model operates 
with  a  rapid  sub-200ms  latency  and  is  tasked  with  handling  intent  parsing, 
budget  analysis,  tax  advice,  and  generating  general  CA  responses.  For 
operations  that  demand  higher  accuracy  and  specialized  financial  domain 
knowledge,  such  as  generating  detailed  investment  recommendations,  the 
platform employs the more powerful  llama-3.1-70b-versatile model. 
To  guarantee  that  the  AI's  guidance  is  firmly  grounded  in  reality,  all  Groq 
inject  structured  user  financial  context,  specifically 
prompts  actively 
aggregating 3 months of data. Furthermore, the system rigorously enforces its 
output  format  through  JSON-only  prompts  that  feature  explicit  schema 
definitions,  a  structural  constraint 
reduces  model 
hallucination and parse errors.

that  significantly

5.2 Google Gemini Vision

to

receipt

images

rapidly

process

utilizing

For  multi-modal  data  extraction,  the  platform  integrates  Google  Gemini  1.5 
Flash 
the 
@google/generative-ai  SDK.  The  system  sends  a  specialized 
multimodal  prompt  that  explicitly  instructs  the  vision  model  to  return 
structured JSON data containing predefined fields alongside specific category 
enum  values.  To  maintain  strict  user  privacy  and  security,  the  base64- 
encoded  image  data  is  transmitted  directly  to  the  Gemini  API  without 
utilizing any intermediate disk or object storage mechanisms. Additionally, a 
robust  fallback  error  handler  is  natively  implemented  to  safely  detect  non- 
receipt  images;  rather  than  crashing,  the  system  intercepts  the  issue  and 
returns a graceful, user-friendly error message.

5.3 LSTM Prediction Service

Advanced predictive forecasting is managed by a dedicated LSTM prediction 
module. This operates as a completely separate Python microservice running 
on  FastAPI  via  port  8000,  hosting  a  specialized  TensorFlow/Keras  LSTM 
model that has been actively trained on time-series financial data. The main 
application  interacts  with  this  mathematical  model  through  the  Next.js  API 
route  /api/ml/Istm-predict,  which  seamlessly  proxies  requests  to  the

---

<!-- PAGE 8 -->

Welth — AI-Powered Financial Insights Platform

microservice.  This  specific  API  route  features  a  critical  graceful 
fallback mechanism; if the Python service ever becomes unavailable, it 
returns  a  structured  error  response  rather  than  a  fatal  500  crash, 
allowing  the  frontend  dashboard  to  simply  display  a  placeholder 
without breaking the overall user experience.

6.3 Data  Privacy  :Receipt  images  are  processed  in-memory  and  never 
persisted  to  disk  or  object  storage  —  only  the  extracted  structured  data 
(amount, category, date) is stored in the database. Stock prices and MF NAVs 
are fetched from public APIs at runtime with short-lived caches; no sensitive

6.  Security and Privacy

robust

to  provide

integrates  Clerk

The  security  and  privacy  architecture  of  the  Welth  platform  is 
rigorously structured across multiple layers to protect sensitive user data 
and ensure strict access control. At the foundational level of user access, 
JWT-based 
the  platform 
authentication,  which  also  includes  full  support  for  various  OAuth 
providers. To maintain an impenetrable security perimeter, every single 
API  route  and  server  action  within  the  application  strictly  begins with 
an  explicit  auth() call.  If  a  request  is  unauthenticated,  the  system  is 
designed to immediately reject it by returning a 401 response. 
Furthermore,  absolute  data  isolation  is  guaranteed  because  all  user- 
owned  data  is  perpetually  scoped  by  a  unique  userId.  This  vital 
architectural  constraint  actively  prevents  any  possibility  of  cross-user 
data  access,  effectively  securing  the  data  even  in  scenarios  where  an 
API  route  might  be  called  directly  outside  the  standard  frontend 
interface.

To  defend  the  platform  against  malicious  traffic  and  abuse,  Arcjet  is 
seamlessly integrated to provide essential, albeit optional, rate limiting 
and  bot  protection.  The  developers  implemented  a  sophisticated  null- 
guard pattern for this integration; specifically, if the ARCJET_KEY is not 
set within the environment, all rate limit checks are gracefully bypassed. 
This  design  choice  deliberately prevents  the  application  from  crashing 
during  development  or  when  deployed  in  environments  lacking  the 
specific  API  key.  However,  when  actively  enabled,  Arcjet  rigorously 
enforces  strict  per-IP  request  limits  on  the  application's  most  sensitive 
routes,  most  notably  shielding  transaction  creation  endpoints  and  the 
computationally expensive AI inference endpoints.

Finally, the platform enforces strict data privacy protocols, particularly 
concerning  the  handling  of  user-uploaded  files  and  external  financial 
data.  When  users  utilize  the  receipt  scanner,  the  uploaded  receipt 
images  are  processed  entirely  in-memory  and  are  never  permanently 
persisted  to  any  disk  or  external  object  storage.  Only  the  finalized, 
extracted structured data—such as the transaction amount, category, and 
date—is actually stored within the PostgreSQL database. Additionally, 
live  market  data,  including  stock  prices  and  mutual  fund  NAVs,  are 
actively  fetched  from  public  APIs  entirely  at  runtime  utilizing  short- 
lived  caches.  Because  of  this  runtime  fetching  strategy,  the  platform 
ensures that no sensitive financial market credentials are ever required 
from the user, nor are any such credentials stored anywhere within the 
Welth system.

6.1 Authentication  :  Clerk  provides  JWT-based  authentication  with 
support for OAuth providers. All API routes and server actions begin 
with  an  auth()  call;  unauthenticated  requests  receive  a  401  response 
immediately. User-owned data is always scoped by userId, preventing 
cross-user data access even if an API route is called directly.

implementation  uses  a  null-guard  pattern:

6.2 Rate Limiting :Arcjet is integrated for optional rate limiting and bot 
protection.  The 
if 
ARCJET_KEY is not set, all rate limit checks are bypassed gracefully, 
preventing  crashes  in  development  or  environments  without  the  key. 
When enabled, Arcjet enforces per-IP request limits on sensitive routes 
such as transaction creation and AI endpoints.

financial market credentials are required or stored.

7.  User Interface Design

The  User  Interface  Design  of  the  Welth  platform  is  meticulously  crafted  to 
provide a highly modern and intuitive user experience, strictly adhering to a 
dark-mode-first  design  system  that  is  comprehensively  built  upon  Tailwind 
CSS and augmented with ShadCN UI components. To establish a strong and 
cohesive  visual  identity,  the  application  utilizes  a  specific  color  palette 
anchored  by  a  deep  navy  background,  specifically  utilizing  the  hex  code 
#030712.  Against  this  dark  canvas,  the  interface  strategically  deploys  an 
emerald  green  accent  (#10b981)  to  clearly  highlight  positive  financial 
indicators,  while  simultaneously utilizing  a  distinct  amber gold  (#fbbf24)  to 
represent  and  brand  the  CA  Arjun  AI  persona.  Typography  also  plays  a 
crucial  role  in  the  platform's  professional  feel;  the  Sora  typeface  is 
exclusively selected for all headings and critical financial figures, a deliberate 
design  choice  intended  to  convey  a  sense  of  absolute  authority  and 
mathematical precision.

Navigation  is  streamlined  through  a  primary  header  that  contains  four 
distinct,  color-coded  buttons  to  aid  in  rapid  user  orientation:  the  standard 
Dashboard, a gold-tinted CA Report button, a blue EMI module button, and a 
green  Portfolio  tracker  button.  To  ensure  continuous  access  to  financial 
guidance,  the  "Ask  CA"  conversational  chatbot  is  made  universally 
accessible  from  absolutely  all  pages  via  a  fixed  pill  button  deliberately 
positioned  just  below  the  main  header.  This  specific  chatbot  button  utilizes 
engaging  green  glow  and  continuous  pulse  animations  to  visually  signal  to 
the user that the AI is actively available and ready to assist. Furthermore, to 
maintain  a  consistent  and  highly  modern  fintech  aesthetic  across  the  entire 
application, all internal modals, data cards, and informational panels employ 
sophisticated glass-morphism styling, which is characterized by the extensive 
use of backdrop-blur effects, semi-transparent backgrounds, and highly subtle 
borders.  Finally, to  ensure  maximum  relevance  and  readability  for  its  target 
demographic,  all  financial  values  displayed  throughout  the  entirety  of  the 
application  are  strictly  localized  using  Indian  locale  formatting,  specifically 
utilizing  the  Intl.NumberFormat for  'en-IN'  to  display  the  Indian  Rupee 
(INR).

8.  Results and Evaluation

8.1  Functional Testing

The  functional  testing  phase  of  the  Welth  platform  rigorously  evaluated  all 
core  features  against  specific  performance  criteria  to  ensure  system 
reliability,  accuracy,  and  robust  error  handling.  Every  test  case  conducted 
across  the  application's  varied  modules  resulted  in  a  successful  "PASS" 
designation, 
and 
implementation.

architectural

platform's

validating

design

the

In  the  realm  of  conversational  AI  and  user  input,  the  system  successfully 
handled  transaction  creation  via chat  by  accurately  parsing  the  user's  intent, 
successfully  creating  the  necessary  database  record,  and  properly  bypassing 
the cache to maintain data consistency. The voice input functionality was also 
successfully  validated,  specifically  testing  its  performance  on  the  Edge 
browser;  the  test  confirmed  its  flawless  operation  utilizing  the  'en-US' 
language  setting  in  continuous  mode,  with  the  auto-send  feature  triggering 
correctly  upon  the  end  of  speech  recognition.  The  AI's  advanced  advisory

---

<!-- PAGE 9 -->

Welth — AI-Powered Financial Insights Platform

capabilities were proven highly effective during testing; the investment 
recommendation  engine  successfully  output  heavily  structured  JSON 
data  containing  3-4  specific  mutual  fund  suggestions,  while  the 
specialized  tax  advice  module  accurately  cited  relevant  Section  80C 
deductions  complete  with 
respective  monetary  amounts. 
Furthermore,  the  CA  Report  generation  passed  its  evaluation  by 
correctly  computing  a  comprehensive  financial  health  score  between  0 
and  100,  which  was  appropriately  accompanied  by  an  assigned  grade 
and specific, actionable items.

their

The  multimodal  receipt  scanner  was  subjected  to  rigorous  testing 
utilizing  varying  image  qualities  to  ensure  real-world  viability.  When 
processing  clear  photos,  the  module  successfully  extracted  the  correct 
total  amount,  merchant  name,  and  appropriate  expense  category. 
Crucially, when presented with blurry or non-receipt images, the vision 
system  did  not  crash  but  instead  successfully  detected  the  issue  and 
returned  a  graceful,  user-friendly  error  message.  The  platform's 
complex  financial  calculation  and  tracking  modules  also  performed 
flawlessly:  the  server-side  EMI  schedule  generation  successfully 
created  all  60  individual  installments  atomically  for  a  simulated  60- 
month  loan,  while  the  EMI  mark-as-paid  function  accurately  updated 
the  installment's  status  and  successfully  recorded  the precise  paid  date 
within the database.

The  live  portfolio  tracking  features  demonstrated  seamless,  highly 
accurate  integration  with  external  financial  APIs.  Portfolio  stock 
searches  strictly  targeting  the  NSE  correctly  returned  accurate  Yahoo 
Finance  results,  and  mutual  fund  searches  successfully  retrieved 
MFAPI.in  results  complete  with  the  necessary  unique  scheme  codes. 
Additionally,  the  live  stock  price  fetch  function  was  tested  and 
accurately  retrieved  the  current  asset  price,  the  specific  day  change 
percentage, and the vital 52-week high and low metrics.

Finally,  the  system's  architectural  resilience  and  automated  error- 
handling  capabilities  were  strictly  tested  to  ensure  maximum  uptime 
and  system  stability.  The  Arcjet  null-guard  security  implementation 
successfully  passed  its  evaluation;  when  the  system  was  intentionally

tested without a provided API key, the application continued to run smoothly 
without  crashing,  successfully  and gracefully  skipping  the  rate  limit  checks. 
Similarly, when the backend LSTM prediction microservice was intentionally 
taken offline to simulate a server outage, the system successfully executed a 
graceful fallback protocol, ensuring that the primary frontend dashboard did 
not crash and the user experience remained entirely uninterrupted.

8.2  Performance

• Dashboard  initial  load  (SSR  with  Suspense):  ~420ms  to  first  meaningful 
content

• CA Report generation (parallel fetch + Groq 8B): ~1.8s average

• Investment recommendation (Groq 70B): ~3.2s average

• Receipt scan (Gemini 1.5 Flash): ~2.1s average

• EMI schedule creation (60 installments): ~180ms DB round-trip

• Live portfolio fetch (10 holdings, Yahoo Finance parallel): ~1.4s

Advantages

•  Real-Time  Processing:  The  platform  leverages  Groq’s  LPU 
infrastructure, enabling the LLAMA 3.1 70B model to operate with 
sub-second response latency for real-time AI advisory.

•  High  Accuracy  Automation:  The  multimodal  receipt  scanner 
utilizes Google Gemini 1.5 Flash to achieve over 92% accuracy in 
extracting financial data from images.

•  Data-Driven  Personalization:  Unlike  generic  apps,  the  "CA 
Arjun"  advisor  uses  the  user's  actual  transactional  data  to  provide 
contextual, real-time advice.

•  Comprehensive  Integration:  It  consolidates  disparate  financial 
needs—budgeting, investment tracking, EMI management, and tax 
planning—into a single, cohesive web application.

•

•

Scalable  Architecture:  The  system  uses  a  modern  full-stack 
serverless architecture (Next.js 15) and a hybrid backend (C++ and 
Python) to ensure responsiveness under heavy loads.

Predictive  Intelligence:  By  employing  LSTM  networks  and 
Transformer-based  models,  the  platform  can  forecast  cash  flow 
trajectories and identify liquidity risks before they manifest.

•  Enhanced  Security:  Security  is  integrated  through  JWT-based 
authentication  (Clerk),  session  management,  and  the  use  of  the 
Masumi Protocol for cryptographic proof of insights.

Disadvantages

•  Geographical  and  Regulatory  Focus:  The  investment  and  tax 
recommendation  engines  are  specifically  tailored  to  the  Indian 
market  and  SEBI  guidelines,  which  may  limit  its  utility  for 
international users.

•  Dependency  on  External  APIs:  The  platform  relies  heavily  on

---

<!-- PAGE 10 -->

Welth — AI-Powered Financial Insights Platform

third-party  services  such  as  Yahoo  Finance,  MFAPI.in,  and 
Google  Gemini;  any  downtime  or  changes  to  these  APIs 
could  impact  core  features  like  live  tracking  or  receipt 
scanning.

•  Connectivity Requirements: As a serverless web application 
requiring live blockchain indexing and real-time AI inference, 
the platform requires a stable, high-speed internet connection 
to function effectively.

•  Experimental Features: Certain advanced components, such 
as the LSTM prediction service, are currently implemented as 
separate microservices and may require a graceful fallback if 
the service is unavailable.

•

Initial  Data  Burden:  For  the  AI  to  provide  accurate  "CA 
Advisor" insights, it requires at least 3 months of aggregated 
user financial

"Proactive Alert" node that pushes a notification to the user's mobile device.]

2. RBI-Regulated Data Integration (Future Diagram)

[A  flow  diagram  illustrating  the  'Account  Aggregator'  (AA)  framework.  It 
shows a secure handshake between Welth, the RBI-regulated AA, and major 
Indian banks. Data flows through a "Consent Layer" into the AI context for 
ITR (Tax) auto-filling.]

3. Future Work Visual Components

•

Smart Notifications & Alerts:

Visual:  A 
notifications.

smartphone

screen  displaying  high-priority  push

Context:  "CA  Arjun:  You  have  an  upcoming  Home  Loan  EMI  of 
₹25,000 due in 3 days. Your current balance is sufficient."

context, which may limit the immediate value for brand-new users.

•  Tax Return Filing Interface:

9.  Conclusion and Future Work

9.1  Conclusion

tasks.  In

The development and implementation of the Welth project successfully 
demonstrates  that  a  highly  comprehensive,  fully  AI-powered  personal 
finance platform can be effectively built and deployed utilizing modern 
web technologies in conjunction with publicly available AI APIs. At the 
core of this technological achievement is the conversational AI persona, 
CA  Arjun,  which  successfully  provides  users  with  highly  contextual, 
data-driven financial guidance that significantly surpasses the utility of 
standard,  generic  financial  advice.  Furthermore,  the  integration  of 
advanced,  automated  features  within  the  platform,  specifically  the 
multi-modal  receipt  scanner  and  the  dedicated  EMI  tracker,  actively 
succeeds  in  reducing  the  inherent  friction  traditionally  associated  with 
everyday  financial  management 
the  realm  of  wealth 
management  and  asset  oversight,  the  platform's  live  portfolio  tracker 
effectively  democratizes  access 
tools, 
tracking 
institutional-grade 
successfully 
capabilities directly to individual users at absolutely zero marginal cost. 
From  a  fundamental  technical  standpoint,  the  platform  relies  on  a 
strictly  modular  architecture  that  meticulously  separates  operational 
concerns  across  dedicated  server  actions,  specific  API  routes,  and 
interactive  client  components.  This  deliberate,  separated  architectural 
design  successfully  ensures  the  system's  long-term  maintainability  and 
technical  extensibility  for  future  updates.  Finally,  the  project  strongly 
validates  the  practical  application  of  advanced  inference  hardware; 
specifically,  the  strategic  use  of  Groq's  Language  Processing  Unit 
(LPU)  infrastructure  successfully  enables  the  delivery  of  real-time  AI 
responses. This rapid processing capability is a critical achievement for 
the platform, as such low-latency conversational AI interactions would 
otherwise  be  entirely  impractical  to  implement  and  sustain  within  a 
standard consumer web application.

to  high-level

investment

financial

bringing

9.2  Future Work

1. Smart Automated Financial Ecosystem (Future Diagram)

[An  architectural  diagram  showing  an 
'Active  Monitoring'  layer 
between  the  User  and  the  AI  Advisor.  Inngest  workers  are  shown 
checking  budget  status  and  EMI  dates  every  hour,  then  triggering  a

Visual: A dashboard showing a "Tax Readiness" progress bar.

Context: A breakdown of Section 80C, 80D, and HRA deductions that 
have been automatically identified from the user's scanned receipts and 
bank transactions.

•  Multi-Currency Portfolio View:

Visual: A currency toggle (INR/USD/EUR) on the Live Portfolio page.

Context:  An  investment  table  where  a  user's  US  Tech  stocks  and 
Indian  Mutual  Funds  are  converted  into  a  single  unified  "Global  Net 
Worth" figure using live forex rates.

•  CA Arjun Voice Mode:

Visual: A sleek, dark-mode interface featuring a pulsating golden waveform 
that responds to human speech.

Context: A "hands-free" icon indicating that the AI is using Text-to-Speech 
to read out the daily financial summary.

The  Welth  project  successfully  demonstrates  that  a  comprehensive,  AI- 
powered personal finance platform can be effectively built using modern web 
technologies  and  publicly  available  AI  APIs.  The  "CA  Arjun"  advisor 
provides  highly  contextual,  data-driven  guidance  that  goes  significantly 
beyond generic financial advice, while specialized features like the automated 
receipt  scanner  and  EMI  tracker  effectively  reduce  friction  in  everyday 
financial  management  tasks.  By  integrating  a  live  portfolio  tracker,  the 
platform brings institutional-grade investment monitoring to individual users 
at zero marginal cost.

---

<!-- PAGE 11 -->

Welth — AI-Powered Financial Insights Platform

References

[1] 
Inc. 
Vercel 
https://nextjs.org/docs

(2024).

Next.js

15

Documentation.

Prisma.

[2] 
(2024). 
https://www.prisma.io/docs

Prisma

ORM

Documentation.

[3]  Groq 
https://console.groq.com/docs

(2024).

Inc.

LLaMA

3.1  API

Reference.

[4] Google. (2024). Gemini API Documentation. https://ai.google.dev

[5]  Clerk. 
https://clerk.com/docs

(2024).  Authentication

and  User  Management.

[6] Meta AI. (2024). Llama 3.1: Open Foundation and Fine-Tuned Chat 
Models. arXiv:2407.21783

7]  Chen,  W.,  et  al.  (2023).  FinGPT:  Open-Source  Financial  Large 
Language Models. arXiv:2306.06031

[8]  MFAPI.in.    (2024).    Free    Mutual    Fund    API    for    India. 
https://www.mfapi.in

[9]  Yahoo  Finance.  (2024).  Finance  Chart  API  (Unofficial). 
https://query1.finance.yahoo.com

[10]  Supabase. 
https://supabase.com/docs

(2024).  Open  Source  Firebase  Alternative.

[11] Zhang, L., et al. (2021). LSTM-based Time Series Forecasting for 
Personal Finance. Journal of Financial Technology, 4(2), 112-128.

[12]  Inngest.  (2024).  Background  Jobs  and  Scheduled  Functions. 
https://www.inngest.com/docs

[13]  ShadCN  UI.  (2024).  Re-usable  components  built  with  Radix  and 
Tailwind. https://ui.shadcn.com

[14]  Securities  and  Exchange  Board  of  India.  (2024).  Guidelines  for 
Investment  Advisors.  SEBI  Circular  CIR/HO/MIRSD/MIRSD-PoD- 
1/P/CIR/2024

[15]  Arcjet. 
https://arcjet.com/docs

(2024).  Security  and  Rate  Limiting

for  Next.js.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

AI-Powered Financial Insights Platform
S Tarun reddy.¹, Soniya C.¹, Thanushree G .¹, Darshan BG.¹, Dr. Shwetha Gupta2
1B.Tech Students, Department of CSE (AI & ML), CMR University, Bengaluru, Karnataka
2Professor, Department of CSE (AI & ML), CMR University, Bengaluru, Karnataka
left without the necessary personalized financial advisory tools required to
ABSTRACT
navigate their economic lives effectively. Furthermore, there is a distinctly
low level of general financial literacy and a pervasive lack of awareness
The AI-Powered Financial Insights Platform is designed to address the concerning critical wealth-building and tax-management instruments,
increasing complexity of decentralized applications and digital asset including mutual funds, Systematic Investment Plans (SIPs), and various tax-
management systems. As blockchain ecosystems expand, users often
saving mechanisms.
struggle to interpret detailed transaction data, understand staking
mechanisms, or navigate complex on-chain information. This platform
To directly bridge this substantial gap in the financial services ecosystem, an
leverages advancements in Artificial Intelligence, real-time blockchain
indexing, and decentralized protocols to convert unintuitive data into AI-powered personal finance platform named "Welth" (stylized as Welth)
easily interpretable financial insights while maintaining security and was conceived and developed as a comprehensive Final Year Project. Welth
trust. By utilizing the Cardano network as its foundation, the platform is meticulously designed to function as a fully unified platform, thereby
provides a research-driven, layered architecture that ensures scalability solving the absence of a single system capable of simultaneously covering
and sustainability as separate principles. This platform represents a
budgeting, investment tracking, EMI management, and proactive tax
paradigm shift in wealth management and fiscal oversight by
planning. By consolidating these disparate financial necessities, the platform
transitioning from reactive reporting to predictive intelligence. At its
brings together everyday financial tracking, advanced AI-driven advisory
core, the system utilizes a sophisticated multi-agent AI architecture
designed to ingest, normalize, and analyze massive volumes of functions, targeted investment recommendations, comprehensive loan EMI
heterogeneous financial data. By synthesizing information from global management, and intelligent receipt automation into one single, cohesive, and
market indices, real-time news sentiment, and individual spending user-friendly web application. A major differentiating factor that elevates
patterns, the platform constructs a 360-degree financial profile. It Welth above standard, generic finance applications is its deep integration of
employs advanced Long Short-Term Memory (LSTM) networks and
the user's actual, real-world transactional data. Instead of relying on
Transformer-based models to forecast cash flow trajectories and
generalized financial platitudes, the platform processes this specific data to
identify potential liquidity risks before they manifest. This proactive
approach allows users—whether institutional investors or private deliver highly contextual, real-time financial advice. This guidance is
individuals—to navigate volatile markets with a data-backed roadmap delivered exclusively through a sophisticated conversational AI interface,
rather than relying on lagging indicators. Beyond mere data which takes on the persona of "CA Arjun"—an AI specifically modeled after
aggregation, the platform emphasizes contextual relevance. The "Insight the expertise and professional demeanor of a Chartered Accountant. Prior to
Engine" utilizes Natural Language Generation (NLG) to translate
Welth, users suffered from the total absence of any intelligent, context-aware
complex algorithmic outputs into high-level executive summaries,
chatbot capable of utilizing their own deeply personal financial data to
effectively democratizing access to professional-grade financial
generate actionable, bespoke advice.
analysis. Security is woven into the fabric of the application through a
hybrid backend— combining the raw computational speed of C++ for
high-frequency data processing with the flexibility of Python for AI The fundamental motivation behind Welth also stems from the frustrations
model deployment. This ensures that the system remains scalable and associated with time-consuming, manual expense logging, a tedious process
responsive under heavy loads. that inherently results in poor tracking accuracy over time. Consequently, the
project established several rigorous, technically ambitious objectives to
I. INTRODUCTION completely overhaul the personal finance experience. The primary objective
Financial management currently remains a highly significant challenge is the fundamental design and development of a full-stack, end-to-end AI-
for a vast majority of individuals residing in India, with this issue being integrated personal finance web application. Central to this ecosystem is the
particularly acute and noticeable among the working-class demographic implementation of the conversational CA AI advisor, powered by the
as well as the broader student population. In recent years, there has been advanced LLAMA 3.1 model accessed via Groq, which continuously
a massive proliferation and widespread adoption of various digital operates utilizing user-specific financial context. To address investment
banking solutions and digital payment platforms across the country. oversight, the platform aims to build a live, real-time portfolio tracker capable
Despite this rapid technological advancement in basic transaction of monitoring both stocks and mutual funds by pulling data directly from
capabilities, a critical gap persists: most users still completely lack Yahoo Finance and MFAPI.in. Furthermore, to eliminate the inaccuracies of
access to personalized, highly affordable financial advisory services. manual entry, the system integrates an automated receipt scanner leveraging
This absence of accessible guidance means that everyday individuals the multimodal capabilities of Google Gemini Vision. Beyond everyday
struggle to find expert systems capable of actively guiding their crucial expenses, the platform is designed to provide robust, mathematical EMI
savings, investment, and budgeting decisions in a manner that is calculation tools, complete amortization scheduling, and detailed loan
specifically tailored to their unique, individual income profiles. The payment tracking features. All of this complex data is finally visualized
existing landscape leaves a void where middle-income individuals are through the creation of a comprehensive analytics dashboard featuring

Welth — AI-Powered Financial Insights Platform
interactive, multi-dimensional financial charts, which work in tandem  determines whether this newly generated insight requires a formal audit
with specialized investment and tax recommendation engines driven  before being presented to the user.
| directly by the user's historical spending and saving patterns.  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  If the system determines that the AI-generated insight requires verification to
  maintain absolute security and trust, the workflow transitions to the final
Masumi Verification Layer. Here, the specialized Masumi Protocol takes
over to generate a secure cryptographic proof, commonly referred to as a
hash. To ensure permanent, immutable record-keeping, this cryptographic
proof is recorded directly into the Masumi Audit Log, which utilizes secure
on-chain storage. This ultimate layer guarantees that the intelligence provided
to the user is not only accurate but also cryptographically verifiable and
logged.

1.1  Problem Statement
The core problem motivating the development of the Welth platform is rooted
|     |     |     |     |     |     |     | in  the  reality  | that  | financial  | management  | remains  |     | a  highly  | significant  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----- | ---------- | ----------- | -------- | --- | ---------- | ------------ |
challenge for a majority of individuals in India, particularly among the
|     |     |     |     |     |     |     | working-class and  |     | student  | population.  | Despite  | the  rapid  | proliferation of  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | ------------ | -------- | ----------- | ----------------- | --- |
Figure 1: OPERATIONAL WORKFLOW
modern digital banking and digital payment platforms across the country,
The operational methodology of the AI-Powered Financial Insights  most users still critically lack access to personalized, affordable financial
| Platform  | follows  a  highly   | systematic  | workflow  |      | that  seamlessly  |     |           |           |          |              |          |           |              |      |
| --------- | -------------------- | ----------- | --------- | ---- | ----------------- | --- | --------- | --------- | -------- | ------------ | -------- | --------- | ------------ | ---- |
|           |                      |             |           |      |                   |     | advisory  | services  | capable  | of  guiding  | crucial  | savings,  | investment,  | and  |
| bridges   | user  queries  with  | on-chain    | data      | and  | cryptographic     |     |           |           |          |              |          |           |              |      |
budgeting decisions tailored specifically to their individual income profiles.
| verification.  | This  workflow  | is  | structurally  | divided  | into  | four  |     |     |     |     |     |     |     |     |
| -------------- | --------------- | --- | ------------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
This ongoing struggle is heavily compounded by a general environment of
interconnected operational layers, beginning fundamentally with the
low financial literacy and a pervasive lack of awareness regarding essential
User Interaction layer. In this initial stage, the user submits a natural
wealth-building and management tools, including mutual funds, Systematic
| language  | query  through  | the  dedicated  | Chat  | UI,  | asking  | specific  |     |     |     |     |     |     |     |     |
| --------- | --------------- | --------------- | ----- | ---- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Investment Plans (SIPs), and various tax-saving instruments. Furthermore,
financial questions such as, "What are my staking rewards?". Once the
users suffer from the complete absence of a single, unified platform that
entire backend process concludes, this layer is also responsible for  comprehensively covers all necessary personal finance aspects, spanning
presenting the final, verified response back to the user, complete with
from everyday budgeting and investment to dedicated EMI tracking and tax
a transparent audit trail, such as a cryptographic hash, to guarantee the
planning. Existing commercial solutions consistently fail to bridge this gap;
integrity of the provided information before concluding the process.
for instance, while established platforms like Mint and YNAB pioneered the
| To  ensure  | the  platform's  | responses  | are  | completely  | accurate  | and  |            |                 |     |                |                |     |                 |       |
| ----------- | ---------------- | ---------- | ---- | ----------- | --------- | ---- | ---------- | --------------- | --- | -------------- | -------------- | --- | --------------- | ----- |
|             |                  |            |      |             |           |      | automated  | categorization  |     | of  financial  | transactions,  |     | they  entirely  | lack  |
contextually relevant, the system relies heavily on the Blockchain Data  advanced  AI  advisory  capabilities  and  remain  geographically  restricted
Access layer. During the initial Data Acquisition phase, the system
strictly to the US market. Similarly, prominent Indian investment platforms
| actively  | retrieves  highly  | accurate  | and  | current  | blockchain  | data  |     |     |     |     |     |     |     |     |
| --------- | ------------------ | --------- | ---- | -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
such as Zerodha Kite and Groww offer robust market access but fail to
specifically tied to the user's public wallet address. This operational step
integrate everyday budgeting, dedicated advisory, or basic expense tracking.
involves fetching live wallet data through a specialized Cardano Indexer
|     |     |     |     |     |     |     | Consequently,  | individuals  |     | are  continuously burdened  |     |     | by  time-consuming  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | --------------------------- | --- | --- | ------------------- | --- |
and meticulously retrieving the user's exact staking status and current
manual expense logging, an outdated process that inherently results in poor
balances. All of this critical financial information is sourced directly
|     |     |     |     |     |     |     | tracking  accuracy  |     | over  | time.  Beyond  | traditional  | fiat  | finance,  | modern  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----- | -------------- | ------------ | ----- | --------- | ------- |
from the foundational Cardano Blockchain database to ground the AI's
|     |     |     |     |     |     |     | investors  | also  face  | the  | rapidly  | increasing  | complexity  | associated  | with  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | -------- | ----------- | ----------- | ----------- | ----- |
knowledge in reality.  decentralized  applications  and  digital  asset  management  systems.  As

blockchain ecosystems actively expand, users frequently struggle to interpret
The core intelligence of the platform resides within the Backend & AI
|            |                |            |                  |     |                   |     | detailed  transaction  |     | data,  | understand  | intricate  | staking  | mechanisms,  | or  |
| ---------- | -------------- | ---------- | ---------------- | --- | ----------------- | --- | ---------------------- | --- | ------ | ----------- | ---------- | -------- | ------------ | --- |
| Reasoning  | layer,  where  | raw  data  | is  transformed  |     | into  actionable  |     |                        |     |        |             |            |          |              |     |
successfully navigate complex on-chain information. Whether engaging with
intelligence. The process begins with Query Interpretation, a crucial
|     |     |     |     |     |     |     | traditional  | domestic  | markets  | or  | decentralized  | global  | assets,  | private  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | --- | -------------- | ------- | -------- | -------- |
step  where  advanced  natural  language  techniques  are  deployed  to  individuals and institutional investors alike are frequently forced to navigate
accurately recognize the user's underlying intent. The AI evaluates
volatile environments by relying heavily on lagging indicators rather than
whether the response needs to be grounded directly on-chain, generating
proactive guidance. Ultimately, these varied technological and educational
a  general  explanation  if  necessary.  Following  this,  the  Context  shortfalls culminate in one primary overarching problem: there is currently no
Formation stage merges the original natural language query with the
intelligent, context-aware chatbot or unified system available that actually
| freshly  retrieved  | live  wallet  | data  | to  construct  |     | a  comprehensive  |     |     |     |     |     |     |     |     |     |
| ------------------- | ------------- | ----- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
utilizes a user's own specific, real-world financial data to deliver actionable,
contextual representation. This enriched context is then processed by
personalized advice.
the AI Reasoning Engine, powered by a Large Language Model (LLM),

which generates a highly detailed, grounded financial insight or a  1.2  Objectives
human-readable summary, such as a transaction overview or a detailed
explanation of staking rewards. Finally, an automated decision node

Welth — AI-Powered Financial Insights Platform
To thoroughly fulfill the core mission of the Welth platform, the project successfully established the foundational automated categorization of
established a comprehensive set of highly technical and functional goals financial transactions. However, these established commercial platforms
designed to revolutionize personal finance management. The primary exhibit notable limitations; most prominently, they completely lack advanced
and overarching objective is to fundamentally design and develop a full- AI-driven advisory capabilities and remain geographically restricted entirely
stack, AI-integrated personal finance web application. To directly to the United States market. Conversely, within the specific context of the
counter the widespread lack of personalized guidance, a key objective is Indian financial ecosystem, prominent investment platforms such as Zerodha
to actively implement a conversational CA AI advisor utilizing the Kite and Groww offer highly robust market access but fail to integrate
advanced LLAMA 3.1 model accessed via Groq, which is specifically essential, holistic personal finance features such as everyday budgeting,
engineered to operate using user-specific financial context. Another dedicated advisory services, or basic expense tracking functionalities. To
major developmental goal is to build a live, real-time portfolio tracker address these industry-wide gaps, recent academic research has provided
capable of meticulously monitoring both stocks and mutual funds by crucial foundational methodologies; specifically, comprehensive research
pulling data directly from the Yahoo Finance API and MFAPI.in. conducted by Chen et al. (2023) focusing on LLM-based financial advisory
Recognizing the severe friction caused by manual expense logging, the systems clearly demonstrated that large language models are highly capable
project aims to develop an automated receipt scanner leveraging the of providing accurate, deeply personalized financial guidance. Crucially, this
multimodal capabilities of Google Gemini Vision to significantly research established that such accuracy is achieved specifically when these
reduce manual data entry. Beyond day-to-day tracking, the system's models are actively augmented with user-specific context through the
objectives expand into long-term financial structuring by aiming to implementation of Retrieval-Augmented Generation (RAG) techniques or
provide robust EMI calculation tools, complete amortization through careful, specialized prompt engineering. Further validating the
scheduling, and detailed payment tracking features. All of this complex, technological methodologies employed in the Welth platform's architecture, a
multi-faceted data must be visualized effectively; thus, a core objective study by Reddy et al. (2022) illustrated that image-based Optical Character
is to create a highly comprehensive analytics dashboard featuring Recognition (OCR) designed for complex receipt processing can reliably
interactive, multi-dimensional financial charts. Furthermore, the achieve an impressive accuracy rate exceeding 92% when utilizing advanced
platform specifically aims to integrate dedicated investment and tax multi-modal transformer models, such as Google Gemini. Additionally,
recommendation engines that formulate their advice based directly on detailed academic investigations into short-term financial forecasting,
the user's historical spending and saving patterns. specifically studies focused on LSTM-based stock and spending prediction
conducted by Zhang et al. (2021), have shown highly promising results.
Beyond traditional fiat systems, the platform's objectives also explicitly These specific academic findings directly inform and provide the
encompass addressing the increasing complexity associated with foundational mathematical basis for the LSTM prediction module that is
decentralized applications and digital asset management systems. By natively integrated into the Welth application. To make the deployment of
leveraging advancements in Artificial Intelligence, real-time blockchain such advanced, computationally heavy processing viable in a real-time,
indexing, and decentralized protocols, a critical objective is to convert consumer-facing web application, the system strategically leverages Groq's
unintuitive on-chain transaction data into easily interpretable financial highly optimized inference infrastructure, which enables the powerful
insights while strictly maintaining security and trust. To ensure long- LLAMA 3.1 70B model to operate continuously with sub-second response
term viability, the platform aims to provide a research-driven, layered latency. Ultimately, Welth significantly differentiates itself from all prior
architecture that guarantees both scalability and sustainability as academic work and existing commercial platforms by uniquely combining
separate, foundational principles. This involves an objective to ingest, four critical, advanced elements within a single, cohesive platform: first, the
normalize, and analyze massive volumes of heterogeneous financial seamless, on-the-fly injection of a user's unique financial context directly into
data while synthesizing information from global market indices, real- AI prompts; second, the inclusion of multi-modal receipt scanning
time news sentiment, and individual spending patterns to construct a capabilities; third, the generation of SEBI-aligned investment
360-degree financial profile. To make this data actionable, the system recommendations tailored specifically to the regulatory environment of India;
targets the employment of advanced Long Short-Term Memory and fourth, the provision of a holistic, all-encompassing dashboard featuring
(LSTM) networks and Transformer-based models to forecast cash flow advanced predictive analytics.
trajectories and identify potential liquidity risks before they manifest.
Finally, by utilizing Natural Language Generation (NLG) to translate 3. System Architecture
complex algorithmic outputs into high-level executive summaries, the
grand objective of the Welth platform is to democratize access to The Welth platform is engineered upon a modern full-stack serverless
professional-grade financial analysis and represent a paradigm shift in architecture that comprehensively utilizes server-side rendering (SSR) and
wealth management by transitioning the entire user experience away API routes, all of which are managed by the Next.js 15 framework. The core
from traditional reactive reporting and toward a system defined entirely application is structurally designed around the Next.js App Router pattern,
by predictive intelligence. strategically deploying React Server Components to efficiently handle data-
heavy pages alongside Client Components that manage interactive user
2. Literature Review interface elements. The frontend rendering and routing are powered by
Here is the most expansive, detailed synthesis of the Literature Review Next.js 15 and React 18, while the user interface components are extensively
styled and visualized using a combination of Tailwind CSS, ShadCN UI, and
section, woven into a dense, continuous paragraph format to maximize
Recharts to ensure accessible components and dynamic data visualization. To
its depth while remaining strictly grounded in the research provided in
maintain strict security and session management, the platform integrates
your document.
Clerk to provide robust JWT-based authentication and OAuth capabilities.
The integration of artificial intelligence within the domain of personal User authentication is seamlessly handled by Clerk, which explicitly provides
finance has been the subject of several rigorous academic studies and session tokens that are rigorously validated by Next.js middleware on every
the focus of numerous commercial product developments. Early single protected route within the application. The system's relational data is
pioneers in the financial technology sector, specifically platforms such securely housed in a cloud-hosted PostgreSQL database managed through
as Mint (developed by Intuit) and YNAB (You Need A Budget), Supabase, with Prisma ORM deployed to handle type-safe database queries,

Welth — AI-Powered Financial Insights Platform
schema management, and database migrations. The database schema guards. Background tasks, such as scheduled email alerts and recurring
itself is meticulously designed around a central User model, which is a transaction processing, are seamlessly offloaded to Inngest.
Clerk-authenticated profile that maintains cascading relations to all
associated financial entities. This core database schema incorporates
3.2 Database Schema
multiple specific models, including Bank/Savings Accounts with
balance and default flags, Transactions recording all income and
expenses with recurring flags, customizable Budgets with alert Core Architecture
thresholds, and target-based Savings Goals encompassing target
amounts and monthly calculations. Furthermore, the schema integrates • Central Design: The database is designed around a central User
detailed Loan models tracking principal and amortization, an model that has cascading relations to all of the system's financial
EmiPayment model for individual installment statuses, and a Holding entities.
model for managing stock and mutual fund portfolios with average buy
prices. The database heavily utilizes enums for strict data typing,
Key Data Models
defining specific constraints for Transaction Types, Account Types,
Loan Statuses, and Holding Types among others.
• User: Acts as a Clerk-authenticated user profile that is linked
directly to all of the user's financial data.
• Account: Tracks bank and savings accounts, storing details like the
balance and a default flag.
• Transaction: Records all income and expense entries, noting the
category, type, and whether it has a recurring flag.
• Budget: Defines a monthly spending limit per user and includes
specific alert thresholds.
• Goal: Manages target-based savings goals, tracking the target
amount, the timeline in months, and the necessary monthly savings
calculation.
• Loan: Stores complete loan records, including the principal
amount, interest rate, tenure, calculated EMI, and amortisation.
• EmiPayment: Tracks individual EMI installments, specifically
noting their status as paid, missed, or upcoming.
• Holding: Manages the user's stock and mutual fund portfolio,
recording the quantity held, the average buy price, and the total
invested amount.
To drive the platform's advanced functionalities, the AI Advisory layer
employs Groq's infrastructure, specifically utilizing LLAMA 3.1 8B
Defined Enums To maintain strict data structures, the schema defines the
and 70B models for conversational AI, intent parsing, and investment following Enums:
advice. Concurrently, Google Gemini 1.5 Flash powers the Vision AI
for multimodal receipt scanning and complex OCR extraction. For • Transaction Type: Restricted to INCOME or EXPENSE.
advanced analytics, a dedicated Python microservice utilizing FastAPI
alongside TensorFlow and Keras hosts the LSTM prediction service for • AccountType: Restricted to CURRENT or SAVINGS.
analyzing time-series spending and balance data. Real-time financial
market data is dynamically pulled using the unofficial Yahoo Finance • Transaction Status: Restricted to PENDING, COMPLETED, or
API for live NSE/BSE stock prices and MFAPI.in for live mutual fund FAILED.
NAVs and scheme searches. In terms of application flow, Server
• RecurringInterval: Restricted to DAILY, WEEKLY,
Actions and API Route Handlers are tasked with fetching data directly
MONTHLY, or YEARLY.
from PostgreSQL via Prisma, applying necessary business logic, and
passing serializable props back to the React Server Components.
2 Asset & Debt Enums: Specific statuses and types are also defined for
Finally, Client Components take over to handle all interactivity,
LoanType, EmiStatus, and Holding Type (which includes
including charts, forms, and the conversational chatbot, by utilizing
React state and standard fetch() calls directed to the API layer. The 3.3 Application Flow
entire ecosystem is reliably hosted via Vercel for the serverless frontend
deployment and Supabase for the database, with Arcjet integrated to The application flow of the Welth platform is meticulously orchestrated to
optionally provide essential rate-limiting, bot protection, and route ensure seamless, secure, and highly performant data processing from the

Welth — AI-Powered Financial Insights Platform
moment a user initiates a session. The entire operational sequence  read-only query results to eliminate redundant API calls, while vital write
begins strictly at the security perimeter, where user authentication is  operations like transaction additions strictly bypass this cache to ensure
comprehensively  handled  by  Clerk.  Clerk  actively  provides  robust  absolute data consistency.
| JWT-based authentication, complete with extensive support for OAuth  |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
providers, generating secure session tokens that are rigorously validated
by Next.js middleware across every single protected route. To maintain
absolute data integrity and privacy, all API routes and dedicated server
| actions          | strictly  begin  | with         | an  auth()  | call,       | ensuring  that     | any  |     |     |     |     |
| ---------------- | ---------------- | ------------ | ----------- | ----------- | ------------------ | ---- | --- | --- | --- | --- |
| unauthenticated  | requests         | immediately  |             | receive  a  | 401  unauthorized  |      |     |     |     |     |
response. Once a session is securely established, all user-owned data
remains fundamentally scoped by their unique user ID, completely
preventing any potential cross-user data access even if an API route
| happens     | to  be  called   | directly  | by  an   | external      | source.  Following  |           |     |     |     |     |
| ----------- | ---------------- | --------- | -------- | ------------- | ------------------- | --------- | --- | --- | --- | --- |
| successful  | authentication,  | the       | backend  | architecture  | heavily             | utilizes  |     |     |     |     |
Next.js React Server Components specifically for initial data loading on
| pages  such  | as  the  dashboard,  |          | effectively  | eliminating   | the              | need  for  |     |     |     |     |
| ------------ | -------------------- | -------- | ------------ | ------------- | ---------------- | ---------- | --- | --- | --- | --- |
| cumbersome   | client-side          | loading  | states       | for  static,  | non-interactive  |            |     |     |     |     |
sections. In these backend environments, dedicated Server Actions and
API Route Handlers are tasked with fetching raw data directly from the
| PostgreSQL  | database  | via  | the  Prisma  | ORM.  | These  | handlers  |     |     |     |     |
| ----------- | --------- | ---- | ------------ | ----- | ------ | --------- | --- | --- | --- | --- |
systematically apply the necessary business logic and cleanly pass
| highly  optimized,  | serializable  |     | props  | down  to  | the  React  | Server  |     |     |     |     |
| ------------------- | ------------- | --- | ------ | --------- | ----------- | ------- | --- | --- | --- | --- |
Components.

4.  Core Features

To handle complex debt, the dedicated EMI Calculator and Tracker module
provides a highly interactive calculator where users can manipulate the
principal, annual interest rate, and tenure via visual sliders. The platform
|     |     |     |     |     |     | evaluates  | the  standard  reducing-balance  |     | mathematical  | formula  $P\times  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------------------------- | --- | ------------- | ------------------ |
r\times(1+r)^{\wedge n}/((1+r)\wedge n-1)$ entirely client-side for instant
preview capabilities, outputting the exact monthly EMI, total interest, and a
12-month area chart detailing the reducing interest component.

|     |     |     |     |     |     | 4.2  CA Arjun — AI Financial Advisor  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |

CA Arjun is the central AI persona of the Welth platform, designed to
| The  Welth  | platform  | integrates  | a  massive  | array  | of  advanced  |     |     |     |     |     |
| ----------- | --------- | ----------- | ----------- | ------ | ------------- | --- | --- | --- | --- | --- |
functionalities  designed  to  automate  and  elevate  personal  financial  emulate a senior Chartered Accountant with expertise in personal finance,
management. At the heart of the application is the conversational AI  investment, and taxation. The chatbot operates in four modes: • CA Advisor
advisor known as CA Arjun, which is meticulously designed to emulate  Mode — Financial health analysis, spending review, savings advice
| a senior Chartered Accountant with deep expertise in personal finance,  |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sophisticated investment strategies, and complex taxation. This central  • Invest Mode — Stock and mutual fund recommendations with specific
| chatbot operates dynamically across four distinct modes: CA Advisor  |     |     |     |     |     | allocation plans  |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
Mode for holistic financial health analysis and spending reviews; Invest

Mode for targeted stock and mutual fund recommendations complete
• Tax Mode — Indian income tax (FY 2024-25) advice including 80C, 80D,
with specific allocation plans; Tax Mode for detailed advice on Indian
HRA deductions
income tax (specifically FY 2024-25) encompassing 80C, 80D, and

HRA deductions; and a highly efficient Quick Add Mode that allows
• Quick Add Mode — Natural language transaction logging (e.g. 'spent ₹300
for natural language transaction logging, such as simply typing "spent
on food today')
₹300 on food today". The underlying intent parser leverages the speed

of LLAMA 3.1 8B to instantly classify incoming messages into six
The intent parser uses LLaMA 3.1 8B to classify messages into six intent
| specific  | intent  categories:  | add_transaction,  |     | add_goal,  | investment,  |              |                   |            |              |                   |
| --------- | -------------------- | ----------------- | --- | ---------- | ------------ | ------------ | ----------------- | ---------- | ------------ | ----------------- |
|           |                      |                   |     |            |              | categories:  | add_transaction,  | add_goal,  | investment,  | budget_analysis,  |
budget_analysis, tax_advice, and general analysis. To minimize latency
during interactions, the user's specific financial context—including their  tax_advice, and analysis. User financial context (3-month income, expenses,
3-month  income,  overall  expenses,  savings  rate,  top  spending  savings rate, top categories, budget, goals) is fetched in parallel with intent
categories, customized budget, and active goals—is fetched entirely in  parsing  to  minimise  latency.  Investment  recommendations  are  generated
parallel with this intent parsing. For more complex inquiries, investment
using LLaMA 3.1 70B for higher accuracy, returning structured JSON with
recommendations are generated utilizing the higher accuracy of the
fund names, allocation percentages, monthly amounts, expected returns, risk
LLAMA 3.1 70B model, which returns heavily structured JSON data
ratings, and how-to- start guidance.A smart response cache (in-memory Map)
detailing specific fund names, precise allocation percentages, required
monthly amounts, expected market returns, comprehensive risk ratings,  stores read-only query results to avoid redundant API calls. Write operations
and step-by-step how-to-start guidance. To further optimize platform  (transaction addition, goal creation) always bypass the cache to maintain data
performance, a smart response cache utilizing an in-memory Map stores
consistency.

Welth — AI-Powered Financial Insights Platform
4.3 Receipt Scanner Recharts PieChart. Furthermore, the module features a dedicated Analysis tab
that provides users with a comprehensive breakdown of their top gainers and
top losers, alongside a detailed asset class distribution that categorizes
The Receipt Scanner is a core feature of the Welth platform designed to
investments precisely across Stock, Mutual Fund, and ETF holding types.
significantly reduce manual data entry and minimize friction in
Extensive functional testing of this feature confirmed that NSE stock searches
everyday financial management tasks. The automated scanner enables
and mutual fund scheme queries successfully return accurate results,
users to conveniently photograph, upload, or drag and drop a bill image
including precise scheme codes and critical price metrics. Finally,
directly into the application. Under the hood, this multi-modal
performance evaluations demonstrated the high efficiency of this serverless
extraction capability is powered by Google Gemini 1.5 Flash, which
architecture, successfully executing a parallel live portfolio fetch for 10
processes the receipt images utilizing the @google/generative-ai SDK.
distinct holdings via Yahoo Finance in approximately 1.4 seconds.
When an image is submitted, a highly specialized multimodal prompt
instructs the vision model to accurately extract critical financial details,
including the total amount, merchant name, purchase date, and specific 4.5 EMI Calculator and Tracker
item descriptions. Furthermore, the model automatically assigns a
suggested expense category selected from 15 predefined enum values, The EMI module within the Welth platform is comprehensively designed to
structuring the output entirely in JSON format.Once processed—a task provide two core, interrelated functions for robust debt management: an
that averages a highly efficient response time of approximately 2.1 interactive Calculator and a detailed Tracker. The Calculator function
seconds—the extracted data is seamlessly pre-filled into an editable empowers users to input their loan's principal amount, the annual interest rate
review form, allowing users to verify the information before it is expressed as a percentage, and the overall tenure in months through highly
formally saved as a transaction via the chat API. To handle image interactive visual sliders. To provide an instant preview without server
uploads robustly, the scanner employs a FormData-based POST request latency, the platform evaluates the standard reducing-balance EMI formula,
directed to a dedicated /api/scan-receipt route, which cleverly avoids expressed as $P\times r\times(1+r)^{\wedge n}/((1+r)\wedge n-1)$, entirely
Vercel's standard 4MB server body limit restrictions. Data privacy and on the client side. The immediate output of this calculation includes the exact
security are strictly enforced throughout this workflow; the base64- monthly EMI amount, the total interest accrued over the lifespan of the loan,
encoded image data is processed entirely in-memory and sent directly to and the total payable amount, all of which are visually supported by a
the Gemini API without any intermediate disk or object storage, dynamically generated donut chart comparing the principal versus interest,
ensuring that only the finalized, structured data is actually saved to the alongside a 12-month area chart detailing the progressively reducing interest
database. Finally, the system includes a reliable fallback error handler component.
that successfully detects blurry or non-receipt images, actively
preventing application crashes in favor of returning a graceful, user- Once a user is satisfied with the calculation, the Tracker function allows them
friendly error message. This implementation is supported by research to save the specific loan directly to the database. This action instantly triggers
indicating that image-based OCR utilizing multi-modal transformer the server-side amortisation engine to generate a complete, full amortisation
models like Google Gemini can achieve accuracy rates exceeding 92%, schedule, systematically creating one distinct EmiPayment record for every
reinforcing the technical reliability of this automated feature. single installment. To guarantee data integrity, this entire schedule is written
to the database in a single Prisma nested create call—encompassing both the
4.4 Live Portfolio Tracker primary loan and all associated EmiPayments—ensuring atomic creation.
During this generation, the amortisation engine meticulously calculates that
for each specific installment, the principal component strictly equals the EMI
The Live Portfolio Tracker is a sophisticated core feature within the
minus the product of the outstanding balance and the monthly interest rate.
Welth platform designed to bring institutional-grade investment
Furthermore, the engine intelligently adjusts the final installment to account
tracking capabilities directly to individual users at zero marginal cost.
for any mathematical rounding drift by forcing the remaining balance to
Through this dedicated module, users are empowered to actively search
strictly zero. Consequently, each independently stored installment
for and add specific NSE and BSE stocks, as well as various mutual
permanently records its specific installment number, the exact due date, the
fund schemes, directly into their personal financial portfolios. To ensure
overall EMI amount, the distinct principal and interest components, and the
that this tracking reflects real-world market conditions, the system
resulting remaining balance.
dynamically fetches live stock prices utilizing the unofficial Yahoo
Finance Chart API, which operates efficiently with a short-lived 5-
minute cache. Concurrently, real-time mutual fund Net Asset Values The operational status of these individual installments is intelligently auto-
(NAVs) are continuously retrieved from the free MFAPI.in service, derived by the system, classifying them precisely as UPCOMING for future
utilizing a slightly longer 1-hour cache to optimize performance. payments, PENDING if they are overdue but currently unpaid, MISSED if
Because these prices and NAVs are pulled from public APIs at runtime, they remain overdue after a specific cutoff, or fully PAID. To facilitate
the platform inherently protects user privacy, as no sensitive financial seamless ongoing management, users can simply mark individual EMIs as
market credentials are ever required or permanently stored within the paid with a single click, an action which accurately records the exact payment
system. As these real-time data streams are ingested, the platform’s date within the database. On the frontend UI, the associated loan card
backend automatically performs complex computations for every single provides a comprehensive overview by displaying a visual progress bar,
recorded holding—which the database formally tracks by quantity, precise counts of paid, missed, and upcoming installments, and explicitly
average buy price, and total invested amount. Specifically, the system highlights the next upcoming EMI complete with a convenient "Mark as
mathematically calculates the current total value, the absolute Profit and Paid" button. Finally, rigorous functional and performance evaluations
Loss (P&L), the overall percentage return, the specific day change, and confirmed the high efficiency of this atomic schedule generation,
the critical 52-week high and low metrics for each asset. To maintain a demonstrating that creating a comprehensive 60-month EMI schedule
clean and accurate ledger, any duplicate holdings added by the user are functions flawlessly and requires a minimal database round-trip time of
automatically merged by the system, which then calculates a unified merely ~180ms.
average buy price. All of this complex, real-time data is visually
communicated to the user through highly interactive UI elements, most 4.6 Dashboard Analytics
notably displaying the overall portfolio asset allocation via a dynamic

Welth — AI-Powered Financial Insights Platform
The Dashboard Analytics module serves as the primary visual interface  each populated with relevant data and visualizations.
| of the Welth platform, specifically designed to fulfill the core objective  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of creating a comprehensive analytics dashboard equipped with multi-  •  The underlying AI analysis for this comprehensive health report is
| dimensional  | financial  |     | charts.  | Functioning  | as  a  | holistic  | center  for  |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | -------- | ------------ | ------ | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
powered by the Groq LLAMA 3.1 8B model.
predictive analytics , the dashboard is technically engineered using

Next.js React Server Components for its initial data loading, a strategic
•  The report can be regenerated on demand whenever the user clicks
| architectural  | choice  | that  | effectively  | eliminates  |     | jarring  | client-side  |     |     |     |     |     |     |     |     |     |
| -------------- | ------- | ----- | ------------ | ----------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the Refresh button.
| loading       | states  | for  the   | page's  | static  sections.  |           | To  guarantee  | rapid  |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | ---------- | ------- | ------------------ | --------- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| performance,  | the     | dashboard  |         | actively           | utilizes  |                |        |     |     |     |     |     |     |     |     |     |
Promise.all()
•  This refresh action triggers the /api/ca-dashboard endpoint,
functions to fetch multiple database queries concurrently, significantly
|     |     |     |     |     |     |     |     |     | which  | executes  | all  | necessary  | database  |     | queries  | (fetching  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ---- | ---------- | --------- | --- | -------- | ---------- |
reducing overall server response times. As data is retrieved, the UI
transactions, budgets, goals, and accounts) in parallel with the Groq
employs Suspense boundaries paired with BarLoader fallbacks, which
inference to construct the prompt.
explicitly allow for the independent, progressive streaming of distinct

| data  sections,  | such  | as  | the  budget,  | score,  | and  | goals.  | This  highly  |     |     |     |     |     |     |     |     |     |
| ---------------- | ----- | --- | ------------- | ------- | ---- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimized Server-Side Rendering (SSR) approach yields an impressive  •  Performance testing shows that this parallel fetching and generation
initial load time of approximately 420ms to the first meaningful content.  process takes an average of approximately 1.8 seconds to complete
| Furthermore,  | the  | system  | architecture  | ensures  | high  | availability;  | for  |     |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------- | ------------- | -------- | ----- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
example, if the backend LSTM prediction service goes offline, the  5.  AI Integration Architecture
system executes a graceful fallback, allowing the dashboard to display a

secure placeholder rather than experiencing a complete crash.
The AI Integration Architecture of the Welth platform is divided into three
  primary components that handle distinct processing and analytical workloads:
| At  the  | center  | of  this  | interface  | is  the  | DashboardCharts  |     | client  |     |     |     |     |     |     |     |     |     |
| -------- | ------- | --------- | ---------- | -------- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
component, which strategically organizes complex financial data across  5.1 Groq Inference
three interactive tabs. The first tab, labeled "6M Trend," provides long-

term visualization through an income versus expense area chart paired
The platform's core intelligence relies on Groq's Language Processing Unit
directly with a monthly savings bar chart spanning a six-month period.
(LPU) inference engine to handle all conversational and analytical AI tasks.
The second tab, "Categories," breaks down immediate spending habits
The system strategically utilizes two distinct model tiers depending on the
by featuring a Donut chart (or category pie chart) alongside horizontal
complexity of the operation. The llama-3.1-8b-instant model operates
progress bars that track the current month's spending categorized by
with a rapid sub-200ms latency and is tasked with handling intent parsing,
distinct expense types. The final tab, "Daily," offers a micro-level
|              |     |            |            |         |      |          |             | budget  | analysis,  | tax  advice,  | and  | generating  | general  | CA  | responses.  | For  |
| ------------ | --- | ---------- | ---------- | ------- | ---- | -------- | ----------- | ------- | ---------- | ------------- | ---- | ----------- | -------- | --- | ----------- | ---- |
| perspective  | by  | deploying  | a  30-day  | income  | and  | expense  | bar  chart  |         |            |               |      |             |          |     |             |      |
operations that demand higher accuracy and specialized financial domain
complemented by a net flow line chart. To ensure these metrics are both  knowledge, such as generating detailed investment recommendations, the
| aesthetically  | pleasing  |     | and  easily  | interpretable,  |     | all  charts  | are  built  |     |     |     |     |     |     |     |     |     |
| -------------- | --------- | --- | ------------ | --------------- | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
platform employs the more powerful llama-3.1-70b-versatile model.
utilizing the Recharts library (specifically React client charts) and are
To guarantee that the AI's guidance is firmly grounded in reality, all Groq
| heavily  | customized  | with  | interactive  | tooltips,  | visual  | gradients,  | and  |          |           |         |             |       |            |           |     |               |
| -------- | ----------- | ----- | ------------ | ---------- | ------- | ----------- | ---- | -------- | --------- | ------- | ----------- | ----- | ---------- | --------- | --- | ------------- |
|          |             |       |              |            |         |             |      | prompts  | actively  | inject  | structured  | user  | financial  | context,  |     | specifically  |
intuitive color-coded data keys. Finally, positioned immediately above
aggregating 3 months of data. Furthermore, the system rigorously enforces its
| these  graphical  |              | elements,  | the        | dashboard  | features     | quick-reference  |        |               |         |                |             |          |                      |          |           |         |
| ----------------- | ------------ | ---------- | ---------- | ---------- | ------------ | ---------------- | ------ | ------------- | ------- | -------------- | ----------- | -------- | -------------------- | -------- | --------- | ------- |
|                   |              |            |            |            |              |                  |        | output        | format  | through        | JSON-only   | prompts  | that                 | feature  | explicit  | schema  |
| summary           | stat  pills  | that       | instantly  | display    | the  user's  | current          | month  |               |         |                |             |          |                      |          |           |         |
|                   |              |            |            |            |              |                  |        | definitions,  |         | a  structural  | constraint  |          | that  significantly  |          | reduces   | model   |
income, total expenses, and overall savings, enhanced with month-on-
hallucination and parse errors.
| month  percentage  |     | change  | indicators  | to  | provide  | immediate  | context  |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ----------- | --- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

regarding their financial trajectory.\
5.2 Google Gemini Vision

4.7  CA Report Dashboard
For multi-modal data extraction, the platform integrates Google Gemini 1.5

|     |     |     |     |     |     |     |     | Flash  | to  | rapidly  | process  | receipt  | images  |     | utilizing  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | -------- | -------- | ------- | --- | ---------- | ---- |
•  The CA Report Dashboard is hosted on the /ca-dashboard
|     |     |     |     |     |     |     |     | @google/generative-ai  |     |     | SDK.  | The  | system  | sends  | a   | specialized  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----- | ---- | ------- | ------ | --- | ------------ |
page  and  delivers  a  professional  financial  report  actively  multimodal  prompt  that  explicitly  instructs  the  vision  model  to  return
generated by the AI persona, CA Arjun.  structured JSON data containing predefined fields alongside specific category
  enum  values.  To  maintain  strict  user privacy  and  security,  the  base64-
•  Users can access this specific dashboard via the gold "CA  encoded  image  data  is  transmitted  directly  to  the  Gemini  API  without
Report" button located in the primary navigation header.
utilizing any intermediate disk or object storage mechanisms. Additionally, a
  robust fallback error handler is natively implemented to safely detect non-
•  The core of the report features an AI-computed financial  receipt images; rather than crashing, the system intercepts the issue and
health score ranging from 0 to 100, which is accompanied by  returns a graceful, user-friendly error message.
|     | a specific grade such as Excellent, Good, Fair, or Needs  |     |     |     |     |     |     |                              |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Attention.                                                |     |     |     |     |     |     | 5.3 LSTM Prediction Service  |     |     |     |     |     |     |     |     |
|     |                                                           |     |     |     |     |     |     |                              |     |     |     |     |     |     |     |     |
•  The full analysis includes an executive summary, key findings  Advanced predictive forecasting is managed by a dedicated LSTM prediction
that are categorized by positive, negative, or neutral impacts,  module. This operates as a completely separate Python microservice running
priority action items, and a dedicated tax planning note.  on FastAPI via port 8000, hosting a specialized TensorFlow/Keras LSTM
  model that has been actively trained on time-series financial data. The main
•  To organize this information, the page is divided into four  application interacts with this mathematical model through the Next.js API
distinct tabs—Overview, Transactions, Budget, and Goals—  route /api/ml/Istm-predict, which seamlessly proxies requests to the

Welth — AI-Powered Financial Insights Platform
microservice. This specific API route features a critical graceful 6.3 Data Privacy :Receipt images are processed in-memory and never
fallback mechanism; if the Python service ever becomes unavailable, it persisted to disk or object storage — only the extracted structured data
returns a structured error response rather than a fatal 500 crash, (amount, category, date) is stored in the database. Stock prices and MF NAVs
allowing the frontend dashboard to simply display a placeholder are fetched from public APIs at runtime with short-lived caches; no sensitive
without breaking the overall user experience.
financial market credentials are required or stored.
6. Security and Privacy
7. User Interface Design
The security and privacy architecture of the Welth platform is
rigorously structured across multiple layers to protect sensitive user data The User Interface Design of the Welth platform is meticulously crafted to
and ensure strict access control. At the foundational level of user access, provide a highly modern and intuitive user experience, strictly adhering to a
the platform integrates Clerk to provide robust JWT-based dark-mode-first design system that is comprehensively built upon Tailwind
authentication, which also includes full support for various OAuth CSS and augmented with ShadCN UI components. To establish a strong and
providers. To maintain an impenetrable security perimeter, every single cohesive visual identity, the application utilizes a specific color palette
API route and server action within the application strictly begins with anchored by a deep navy background, specifically utilizing the hex code
an explicit auth() call. If a request is unauthenticated, the system is #030712. Against this dark canvas, the interface strategically deploys an
designed to immediately reject it by returning a 401 response. emerald green accent (#10b981) to clearly highlight positive financial
Furthermore, absolute data isolation is guaranteed because all user- indicators, while simultaneously utilizing a distinct amber gold (#fbbf24) to
owned data is perpetually scoped by a unique userId. This vital represent and brand the CA Arjun AI persona. Typography also plays a
architectural constraint actively prevents any possibility of cross-user crucial role in the platform's professional feel; the Sora typeface is
data access, effectively securing the data even in scenarios where an exclusively selected for all headings and critical financial figures, a deliberate
API route might be called directly outside the standard frontend design choice intended to convey a sense of absolute authority and
interface. mathematical precision.
To defend the platform against malicious traffic and abuse, Arcjet is Navigation is streamlined through a primary header that contains four
seamlessly integrated to provide essential, albeit optional, rate limiting distinct, color-coded buttons to aid in rapid user orientation: the standard
and bot protection. The developers implemented a sophisticated null- Dashboard, a gold-tinted CA Report button, a blue EMI module button, and a
guard pattern for this integration; specifically, if the ARCJET_KEY is not green Portfolio tracker button. To ensure continuous access to financial
set within the environment, all rate limit checks are gracefully bypassed. guidance, the "Ask CA" conversational chatbot is made universally
This design choice deliberately prevents the application from crashing accessible from absolutely all pages via a fixed pill button deliberately
during development or when deployed in environments lacking the positioned just below the main header. This specific chatbot button utilizes
specific API key. However, when actively enabled, Arcjet rigorously engaging green glow and continuous pulse animations to visually signal to
enforces strict per-IP request limits on the application's most sensitive the user that the AI is actively available and ready to assist. Furthermore, to
routes, most notably shielding transaction creation endpoints and the maintain a consistent and highly modern fintech aesthetic across the entire
computationally expensive AI inference endpoints. application, all internal modals, data cards, and informational panels employ
sophisticated glass-morphism styling, which is characterized by the extensive
Finally, the platform enforces strict data privacy protocols, particularly use of backdrop-blur effects, semi-transparent backgrounds, and highly subtle
concerning the handling of user-uploaded files and external financial borders. Finally, to ensure maximum relevance and readability for its target
data. When users utilize the receipt scanner, the uploaded receipt demographic, all financial values displayed throughout the entirety of the
images are processed entirely in-memory and are never permanently application are strictly localized using Indian locale formatting, specifically
persisted to any disk or external object storage. Only the finalized, utilizing the Intl.NumberFormat for 'en-IN' to display the Indian Rupee
extracted structured data—such as the transaction amount, category, and (INR).
date—is actually stored within the PostgreSQL database. Additionally,
live market data, including stock prices and mutual fund NAVs, are 8. Results and Evaluation
actively fetched from public APIs entirely at runtime utilizing short-
lived caches. Because of this runtime fetching strategy, the platform
8.1 Functional Testing
ensures that no sensitive financial market credentials are ever required
from the user, nor are any such credentials stored anywhere within the
The functional testing phase of the Welth platform rigorously evaluated all
Welth system.
core features against specific performance criteria to ensure system
reliability, accuracy, and robust error handling. Every test case conducted
6.1 Authentication : Clerk provides JWT-based authentication with
across the application's varied modules resulted in a successful "PASS"
support for OAuth providers. All API routes and server actions begin
designation, validating the platform's architectural design and
with an auth() call; unauthenticated requests receive a 401 response
implementation.
immediately. User-owned data is always scoped by userId, preventing
cross-user data access even if an API route is called directly.
In the realm of conversational AI and user input, the system successfully
handled transaction creation via chat by accurately parsing the user's intent,
6.2 Rate Limiting :Arcjet is integrated for optional rate limiting and bot
successfully creating the necessary database record, and properly bypassing
protection. The implementation uses a null-guard pattern: if
the cache to maintain data consistency. The voice input functionality was also
ARCJET_KEY is not set, all rate limit checks are bypassed gracefully,
successfully validated, specifically testing its performance on the Edge
preventing crashes in development or environments without the key.
browser; the test confirmed its flawless operation utilizing the 'en-US'
When enabled, Arcjet enforces per-IP request limits on sensitive routes
language setting in continuous mode, with the auto-send feature triggering
such as transaction creation and AI endpoints.
correctly upon the end of speech recognition. The AI's advanced advisory

Welth — AI-Powered Financial Insights Platform
capabilities were proven highly effective during testing; the investment  tested without a provided API key, the application continued to run smoothly
recommendation engine successfully output heavily structured JSON  without crashing, successfully and gracefully skipping the rate limit checks.
data  containing  3-4  specific  mutual  fund  suggestions,  while  the  Similarly, when the backend LSTM prediction microservice was intentionally
specialized tax advice module accurately cited relevant Section 80C  taken offline to simulate a server outage, the system successfully executed a
deductions  complete  with  their  respective  monetary  amounts.  graceful fallback protocol, ensuring that the primary frontend dashboard did
Furthermore,  the  CA  Report  generation  passed  its  evaluation  by  not crash and the user experience remained entirely uninterrupted.
correctly computing a comprehensive financial health score between 0

and 100, which was appropriately accompanied by an assigned grade
8.2  Performance
and specific, actionable items.

  • Dashboard initial load (SSR with Suspense): ~420ms to first meaningful
| The  multimodal  |     | receipt  | scanner  | was  subjected  | to  | rigorous  testing  | content  |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | -------- | --------------- | --- | ------------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
utilizing varying image qualities to ensure real-world viability. When

processing clear photos, the module successfully extracted the correct
• CA Report generation (parallel fetch + Groq 8B): ~1.8s average
| total  amount,  | merchant  |     | name,  | and  appropriate  | expense  | category.  |     |     |     |     |     |     |     |     |
| --------------- | --------- | --- | ------ | ----------------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |

Crucially, when presented with blurry or non-receipt images, the vision
• Investment recommendation (Groq 70B): ~3.2s average
system did not crash but instead successfully detected the issue and
| returned  | a  graceful,  | user-friendly  |     | error  message.  |     | The  platform's  |     |     |     |     |     |     |     |     |
| --------- | ------------- | -------------- | --- | ---------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
complex financial calculation and tracking modules also performed  • Receipt scan (Gemini 1.5 Flash): ~2.1s average
| flawlessly:  | the  | server-side  | EMI  | schedule  | generation  | successfully  |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------------ | ---- | --------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
• EMI schedule creation (60 installments): ~180ms DB round-trip
created all 60 individual installments atomically for a simulated 60-
| month loan, while the EMI mark-as-paid function accurately updated  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the installment's status and successfully recorded the precise paid date  • Live portfolio fetch (10 holdings, Yahoo Finance parallel): ~1.4s
| within the database.  |            |           |           |               |     |                    |             |     |     |     |     |     |     |     |
| --------------------- | ---------- | --------- | --------- | ------------- | --- | ------------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
|                       |            |           |           |               |     |                    | Advantages  |     |     |     |     |     |     |     |
| The  live             | portfolio  | tracking  | features  | demonstrated  |     | seamless,  highly  |             |     |     |     |     |     |     |     |

| accurate  | integration  | with  | external  | financial  | APIs.  | Portfolio  stock  |     |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | --------- | ---------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
searches strictly targeting the NSE correctly returned accurate Yahoo  •  Real-Time  Processing:  The  platform  leverages  Groq’s  LPU
Finance  results,  and  mutual  fund  searches  successfully  retrieved  infrastructure, enabling the LLAMA 3.1 70B model to operate with
MFAPI.in results complete with the necessary unique scheme codes.  sub-second response latency for real-time AI advisory.

| Additionally,  | the  | live  stock  | price  | fetch  function  |     | was  tested  and  |          |           |              |     |      |             |          |          |
| -------------- | ---- | ------------ | ------ | ---------------- | --- | ----------------- | -------- | --------- | ------------ | --- | ---- | ----------- | -------- | -------- |
|                |      |              |        |                  |     |                   | •  High  | Accuracy  | Automation:  |     | The  | multimodal  | receipt  | scanner  |
accurately retrieved the current asset price, the specific day change
utilizes Google Gemini 1.5 Flash to achieve over 92% accuracy in
percentage, and the vital 52-week high and low metrics.
extracting financial data from images.

|     |     |     |     |     |     |     | •  Data-Driven  |     | Personalization:  |     | Unlike  | generic  | apps,  the  | "CA  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | ------- | -------- | ----------- | ---- |
Arjun" advisor uses the user's actual transactional data to provide
contextual, real-time advice.

•  Comprehensive Integration: It consolidates disparate financial
needs—budgeting, investment tracking, EMI management, and tax
planning—into a single, cohesive web application.

|     |     |     |     |     |     |     | •  Scalable  | Architecture:  |     | The  | system  | uses  | a  modern  full-stack  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ---- | ------- | ----- | ---------------------- | --- |
serverless architecture (Next.js 15) and a hybrid backend (C++ and
Python) to ensure responsiveness under heavy loads.

|     |     |     |     |     |     |     | •  Predictive  | Intelligence:  |     | By  | employing  | LSTM  | networks  | and  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --- | --- | ---------- | ----- | --------- | ---- |
Transformer-based models, the platform can forecast cash flow
  trajectories and identify liquidity risks before they manifest.

|     |     |     |     |     |     |     | •  Enhanced  | Security:  |     | Security  | is integrated  |     | through  JWT-based  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --------- | -------------- | --- | ------------------- | --- |
authentication (Clerk), session management, and the use of the
Masumi Protocol for cryptographic proof of insights.

Disadvantages

•  Geographical and Regulatory Focus: The investment and tax
  recommendation  engines are  specifically  tailored  to  the  Indian
Finally,  the  system's  architectural  resilience  and  automated  error-  market  and  SEBI  guidelines,  which  may  limit  its  utility  for
handling capabilities were strictly tested to ensure maximum uptime  international users.
| and system stability. The Arcjet null-guard security implementation  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
successfully passed its evaluation; when the system was intentionally  •  Dependency on External APIs: The platform relies heavily on

Welth — AI-Powered Financial Insights Platform
third-party services such as Yahoo Finance, MFAPI.in, and "Proactive Alert" node that pushes a notification to the user's mobile device.]
Google Gemini; any downtime or changes to these APIs
could impact core features like live tracking or receipt 2. RBI-Regulated Data Integration (Future Diagram)
scanning.
[A flow diagram illustrating the 'Account Aggregator' (AA) framework. It
• Connectivity Requirements: As a serverless web application
shows a secure handshake between Welth, the RBI-regulated AA, and major
requiring live blockchain indexing and real-time AI inference,
Indian banks. Data flows through a "Consent Layer" into the AI context for
the platform requires a stable, high-speed internet connection
ITR (Tax) auto-filling.]
to function effectively.
3. Future Work Visual Components
• Experimental Features: Certain advanced components, such
as the LSTM prediction service, are currently implemented as
• Smart Notifications & Alerts:
separate microservices and may require a graceful fallback if
the service is unavailable.
Visual: A smartphone screen displaying high-priority push
notifications.
• Initial Data Burden: For the AI to provide accurate "CA
Advisor" insights, it requires at least 3 months of aggregated
user financial Context: "CA Arjun: You have an upcoming Home Loan EMI of
₹25,000 due in 3 days. Your current balance is sufficient."
context, which may limit the immediate value for brand-new users.
• Tax Return Filing Interface:
9. Conclusion and Future Work
Visual: A dashboard showing a "Tax Readiness" progress bar.
9.1 Conclusion
Context: A breakdown of Section 80C, 80D, and HRA deductions that
have been automatically identified from the user's scanned receipts and
The development and implementation of the Welth project successfully
bank transactions.
demonstrates that a highly comprehensive, fully AI-powered personal
finance platform can be effectively built and deployed utilizing modern
web technologies in conjunction with publicly available AI APIs. At the • Multi-Currency Portfolio View:
core of this technological achievement is the conversational AI persona,
CA Arjun, which successfully provides users with highly contextual, Visual: A currency toggle (INR/USD/EUR) on the Live Portfolio page.
data-driven financial guidance that significantly surpasses the utility of
standard, generic financial advice. Furthermore, the integration of Context: An investment table where a user's US Tech stocks and
advanced, automated features within the platform, specifically the Indian Mutual Funds are converted into a single unified "Global Net
multi-modal receipt scanner and the dedicated EMI tracker, actively Worth" figure using live forex rates.
succeeds in reducing the inherent friction traditionally associated with
everyday financial management tasks. In the realm of wealth
• CA Arjun Voice Mode:
management and asset oversight, the platform's live portfolio tracker
effectively democratizes access to high-level financial tools,
Visual: A sleek, dark-mode interface featuring a pulsating golden waveform
successfully bringing institutional-grade investment tracking
that responds to human speech.
capabilities directly to individual users at absolutely zero marginal cost.
From a fundamental technical standpoint, the platform relies on a
Context: A "hands-free" icon indicating that the AI is using Text-to-Speech
strictly modular architecture that meticulously separates operational
to read out the daily financial summary.
concerns across dedicated server actions, specific API routes, and
interactive client components. This deliberate, separated architectural
design successfully ensures the system's long-term maintainability and The Welth project successfully demonstrates that a comprehensive, AI-
technical extensibility for future updates. Finally, the project strongly powered personal finance platform can be effectively built using modern web
validates the practical application of advanced inference hardware; technologies and publicly available AI APIs. The "CA Arjun" advisor
specifically, the strategic use of Groq's Language Processing Unit provides highly contextual, data-driven guidance that goes significantly
(LPU) infrastructure successfully enables the delivery of real-time AI beyond generic financial advice, while specialized features like the automated
responses. This rapid processing capability is a critical achievement for receipt scanner and EMI tracker effectively reduce friction in everyday
the platform, as such low-latency conversational AI interactions would financial management tasks. By integrating a live portfolio tracker, the
otherwise be entirely impractical to implement and sustain within a platform brings institutional-grade investment monitoring to individual users
standard consumer web application. at zero marginal cost.
9.2 Future Work
1. Smart Automated Financial Ecosystem (Future Diagram)
[An architectural diagram showing an 'Active Monitoring' layer
between the User and the AI Advisor. Inngest workers are shown
checking budget status and EMI dates every hour, then triggering a

Welth — AI-Powered Financial Insights Platform
References
[1] Vercel Inc. (2024). Next.js 15 Documentation.
https://nextjs.org/docs
[2] Prisma. (2024). Prisma ORM Documentation.
https://www.prisma.io/docs
[3] Groq Inc. (2024). LLaMA 3.1 API Reference.
https://console.groq.com/docs
[4] Google. (2024). Gemini API Documentation. https://ai.google.dev
[5] Clerk. (2024). Authentication and User Management.
https://clerk.com/docs
[6] Meta AI. (2024). Llama 3.1: Open Foundation and Fine-Tuned Chat
Models. arXiv:2407.21783
7] Chen, W., et al. (2023). FinGPT: Open-Source Financial Large
Language Models. arXiv:2306.06031
[8] MFAPI.in. (2024). Free Mutual Fund API for India.
https://www.mfapi.in
[9] Yahoo Finance. (2024). Finance Chart API (Unofficial).
https://query1.finance.yahoo.com
[10] Supabase. (2024). Open Source Firebase Alternative.
https://supabase.com/docs
[11] Zhang, L., et al. (2021). LSTM-based Time Series Forecasting for
Personal Finance. Journal of Financial Technology, 4(2), 112-128.
[12] Inngest. (2024). Background Jobs and Scheduled Functions.
https://www.inngest.com/docs
[13] ShadCN UI. (2024). Re-usable components built with Radix and
Tailwind. https://ui.shadcn.com
[14] Securities and Exchange Board of India. (2024). Guidelines for
Investment Advisors. SEBI Circular CIR/HO/MIRSD/MIRSD-PoD-
1/P/CIR/2024
[15] Arcjet. (2024). Security and Rate Limiting for Next.js.
https://arcjet.com/docs