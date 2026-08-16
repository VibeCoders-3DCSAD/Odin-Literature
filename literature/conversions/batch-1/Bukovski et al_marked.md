---
conversion_metadata:
  converted_at: "2026-07-22T12:27:26Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bukovski et al.pdf"
  source_pdf_sha256: "9f22333748c3ef89e00d6b73dfaf199b07c42bf9f1cf6b4bf32d7afb8919890d"
  page_count: 49
  markdown_char_count: 219617
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ISSN: 3033-4136

DOI:  https://doi.org/10.17868/strath.00094718

From  Crisis  to  Prosperity:  AI  and 
Open Finance for Holistic Financial 
Health and Smart Future Planning

<

>

FRIL

Financial Regulation Innovation Lab

FinTech 
Scotland®

l

- University 
~ efGlasgow

•

Universityof

Strathclyde 
Glasgow

1

in collaboration with

---

<!-- PAGE 2 -->

From Crisis to Prosperity: AI and Open Finance for 
Holistic Financial Health and Smart Future Planning

Kal Bukovski, Consulting Senior Manager and Director of Academia & Research, Sopra Steria, 
Orchard Brae House, 30 Queensferry Road, Edinburgh EH4 2HS

Dr  Kushagra  Jain,  Professor  Mark  Cummins,  Dr  James  Bowden,  Dr  Godsway  Korku  Tetteh. 
Strathclyde  Business  School,  University  of  Strathclyde,  and  Financial  Regulation  Innovation 
Lab, 199 Cathedral Street, Glasgow, G4 0QU, UK

Zi Khang, MSc student in Mathematical and Computational Finance 2024-2025 – University of 
Oxford’s Mathematical Institute, Wellington Square, Oxford OX1 2JD

12 November 2025

We acknowledge funding from Innovate UK, award number 10055559.

Corresponding authors:

Email: kal.bukovski@soprasteria.com

Email: kushagra.jain@strath.ac.uk

Email: mark.cummins@strath.ac.uk

Email: james.bowden@strath.ac.uk

Email: godsway.tetteh@strath.ac.uk

---

<!-- PAGE 3 -->

Financial Regulation Innovation Lab

Who are we?

The  Financial  Regulation  Innovation Lab  (FRIL)  is  an industry-led  collaborative research and 
innovation programme focused on leveraging new technologies to respond to, shape, and help 
evolve  the  future  regulatory  landscape  in  the  UK  and  globally,  helping  to  create  new 
employment and business opportunities, and enabling the future talent.

FRIL  provides  an  environment  for  participants  to  engage  and  collaborate  on  the  dynamic 
demands of financial regulation, explore, test and experiment with new technologies, build 
confidence in solutions and demonstrate their ability to meet regulatory standards worldwide.

What is Actionable Research?

FRIL will integrate academic research with an industry relevant agenda, focused on enabling 
knowledge on cutting-edge topics such as generative and explainable AI, advanced analytics, 
advanced  computing,  and  earth-intelligent  data  as  applied  to  financial  regulation.  The 
learning  to  produce  a  series  of  papers,  actionable 
approach  fosters  cross  sector 
recommendations and  strategic plans that  can be tested  in the  innovation  environment, in 
collaboration across industry and regulators.

Locally-led Innovation Accelerators delivered in 
partnership with DSIT, Innovate UK and City Regions

Department for 
Science, Innovation 
& Technology

Innovate 
UK

GLASGOW 
CITY  REGION

---

<!-- PAGE 4 -->

FRIL White Paper Series

From Crisis to Prosperity: AI and Open Finance for 
Holistic Financial Health and Smart Future Planning

Kal Bukovski*    Kushagra Jain**    Mark Cummins**

James Bowden**    Godsway Korku Tetteh**    Zi Lin***

* Sopra Steria    ** University of Strathclyde   ***University of Oxford

12 November 2025

Executive Summary

The  financial  services  industry  stands  at  a  critical  inflection  point.  Traditional  credit-score-
centric frameworks, rooted in historical repayment data and broad demographic categories, 
are increasingly incapable of capturing the full spectrum of consumers’ financial health. The 
COVID-19 pandemic, successive cost-of-living crises and wider economic shocks have exposed 
deep  vulnerabilities  in  reactive,  one-dimensional  risk  models.  Consumers  and  institutions 
require  proactive,  resilience-focused  insights  that  span  day-to-day  cashflow  management, 
medium-term debt servicing, and long-term wealth accumulation.

Open Finance - the consent-driven sharing of a comprehensive array of financial data (current 
accounts, mortgages, loans, savings, investments, pensions, insurance, government benefits), 
combined  with  advanced  Artificial  Intelligence  (AI)  and  Machine  Learning  (ML)  techniques, 
offers a transformational route to truly holistic financial health evaluation. By ingesting rich, 
multi-dimensional data and applying explainable models, financial firms can transition from 
static  credit  assessments  to  dynamic,  personalised  guidance  and  recommendation  engines. 
These engines empower consumers to build financial resilience, make informed decisions and 
pursue life goals with confidence.

Building on Sopra Steria and Glasgow University’s joint whitepaper “Consumers at the Heart of 
Innovation: Financial Health Evaluation in the UK Regulatory Landscape” and inspired by R&D 
collaboration between Sopra Steria and Oxford University, this whitepaper:

▪  Examines the scope and expected data architecture of Open Finance, extending from

Open Banking to full-spectrum data sharing.

▪  Presents  a  robust  data  modelling  framework,  encompassing  data  acquisition, 
cleansing,  feature  engineering,  supervised  and  unsupervised  modelling,  scorecard 
design and persona segmentation. It culminates in a composite financial health score 
that blends aspects like credit risk and resilience evaluation.

---

<!-- PAGE 5 -->

▪  Explores  explainability  and  consumer  engagement,  employing  data  science 
techniques  to  ensure  transparency  and  mapping  various  persona  archetypes  to 
tailored, sequential optimisation plans.

▪  Demonstrates  regulatory  alignment,  showing  how  non-product-specific,  persona-
driven guidance and recommendation can fit within the Financial Conduct Authority’s 
(FCA) Advice and Guidance Boundary (FG15/1) and the Consumer Duty framework.

---

<!-- PAGE 6 -->

Table of Contents

1.  Introduction .......................................................................................................................... 1

1.1 Context & motivation - shifting financial landscape ......................................................... 1

1.2 Problem statement .......................................................................................................... 2

1.3 From Open Banking to Open Finance............................................................................... 3

1.4 Defining financial health and resilience ........................................................................... 4

1.5. Industry & Regulatory perspectives ................................................................................ 6

2.  Open Finance: Data integration and customer segmentation ............................................ 9

2.1 The Open Finance data revolution ................................................................................... 9

2.2 Data structures ............................................................................................................... 11

2.4 Advanced customer segmentation through AI-driven analytics .................................... 13

2.5 Privacy-preserving data enhancement ........................................................................... 14

2.6 Regulatory compliance and ethical considerations ........................................................ 15

2.7 Beyond Open Finance: inclusion, smart data and cross-border portability ................... 16

3.  Predictive analytics & cash flow modelling ........................................................................ 17

3.1 Comprehensive data sourcing ........................................................................................ 17

3.2 Dynamic risk assessment and behavioural prediction ................................................... 19

3.3 Feature selection & engineering .................................................................................... 20

3.4 Predictive modelling & clustering .................................................................................. 20

3.5 Model explainability vs performance ............................................................................. 22

3.6 Stochastic modelling and scenario analysis .................................................................... 22

3.7 Adaptation and continuous learning .............................................................................. 24

4.  Smart Personalised Finance Management Framework ..................................................... 25

4.1 Hierarchical financial needs framework ......................................................................... 25

4.2 Sequential optimisation engine architecture ................................................................. 26

4.3 Personalisation and behavioural integration ................................................................. 27

4.4 Continuous improvement and outcome tracking .......................................................... 29

5.  Conclusion ........................................................................................................................... 31

6.  References: ......................................................................................................................... 32

About the Authors .................................................................................................................... 41

---

<!-- PAGE 7 -->

1. Introduction  
1.1 Context & motivation - shifting financial landscape

Over the past decade, digital transformation, fintech innovation and economic volatility have 
radically changed consumers’ financial lives. Typically, traditional credit-scoring frameworks are 
heavily reliant on repayment histories and demographic proxies. These can therefore often fail 
to reflect complex, dynamic realities such as fluctuating gig-economy incomes, irregular self-
employment cashflows or sudden macroeconomic shocks. The COVID-19 pandemic exposed 
the fragility of many households, while the following cost-of-living crises have underscored the 
imperative  for  financial  resilience  –  more  specifically,  the  ability  to  absorb  income  shocks, 
maintain essential spending and avoid harmful debt spirals.

The  financial  sector’s  balance  sheets  as  a  proportion  of  GDP,  and  share  in  economy  value 
added,  have  been  rising  in  many  economies.  From  the  resulting  financial  depth,  such 
“financialisation”  can  boost  growth  and  productivity,  especially  in  developing  countries. 
However, too much of a good thing can be a concern: financial intermediation costs continue 
to rise, calling into question the industry’s efficiency. The relationship between financial depth 
and  productivity  and  growth  is  possibly  U-shaped.  Thus,  it  is  pivotal  to  acknowledge  these 
factors and to question the financial system’s contribution to economy and society [1].

More contemporary evidence casts further scrutiny upon finance’s societal value. Sentiment 
positivity from a huge corpus of finance literature (captured, for example, in multiple languages 
and over multiple decades) has been shown to be positively correlated with financial market 
participation and negatively with income inequality [2],[3]. The former is represented by equity 
percentage of total assets for households (from the Organisation for Economic Co-operation 
and  Development  –  OECD),  total  loans  to  households  and  non-financial  private  sector,  as 
percentages  of  GDP.  The  latter  is  measured  with  national  accounts  data  using  the  Gini 
coefficient, reported by the World Income Inequality Database.

In light of the above, global and UK concerns surrounding the role of such income and wealth 
inequality and concentration merit acknowledgement and consideration, alongside alternate 
solutions such as better corporate and wealth taxation. Specifically, from macroeconomic data 
in  [4],  researchers  investigate  substantial  profit  reductions  for  nations  from  profit  shifting 
strategies of multinational companies to tax havens.

At the same time, rising consumer expectations demand proactive support. Rather than simply 
deciding  on  creditworthiness,  households  seek  insights  into  essential  buffer  levels,  optimal 
long-term  goals 
debt-repayment  strategies,  saving 
(homeownership, education, retirement) and timely nudges when life events (job loss, family 
expansion, rate resets) threaten financial stability.

for  medium-  and

trajectories

Financial Regulation Innovation Lab (FRIL) | 1

---

<!-- PAGE 8 -->

1.2 Problem statement

This  whitepaper  addresses  the  urgent  challenge  of  improving  holistic  financial  health  and 
resilience in an increasingly complex and shifting financial landscape. While traditional financial 
guidance often focuses narrowly on creditworthiness or savings, many consumers still struggle 
to manage everyday finances, absorb shocks and plan effectively for their futures [5],[6]. Our 
work  situates  financial  health  as  a  multi-dimensional  concept,  integrating  spending,  saving, 
borrowing  and  financial  planning,  with  resilience  as  a  cross-cutting  capability  that  supports 
wellbeing through life’s uncertainties.

This approach aligns closely with the FCA’s Advice Guidance Boundary Review (AGBR), which 
explores new regulatory frameworks to better support consumers in making financial decisions 
[7].  The  AGBR  focuses  on  bridging  the  gap  between  generic  guidance  and  full  advice  by 
introducing “targeted support” (see Figure 1) – tailored suggestions developed for groups of 
consumers with similar circumstances, designed to improve access to timely and affordable 
financial help. This emerging model aims to empower more people to navigate pensions and 
investments with confidence, addressing the persistent “advice gap” where only around 8% of 
UK adults currently receive financial advice [8].

Ideally, such targeted support ought to be provided at a minimal cost to vulnerable parties. 
Fairness should be considered for delivery of targeted support to ensure maximal efficacy. For 
instance, AI’s potential in improving learning outcomes and promoting diversity, equity, and 
inclusion should be considered [9]. Further, blended human-AI delivery behoves consideration 
especially for complex problems in the context of targeted support, as research indicates hybrid 
human-AI interaction yields better performance in interactive reasoning tasks, driven by the 
latter’s correct reasoning [10].

Financial Regulation Innovation Lab (FRIL) | 2

---

<!-- PAGE 9 -->

A suite of consumer support options

Personal recommendation boundary

J,

~

INFORMATION/ 
GUIDANCE

Factual information 
and/or generic 
guidance to help a 
consumer understand 
their options but 
without providing 
a view of what the 
consumer should do

QI

....  C: 
:::l 
....  0 
:.:;  :.:; 
VI 
IO 
C:  "O 
0  C: 
u  QI

....  E 
0 
C:  E 
VI  0 
QI  u 
... 
0  QI 
"O 
....  iii 
IO  C: 
.c:  0 
....  VI 
... 
QI 
u  QI 
·s:  Q,

IO

"O 
<(

~ SIMPLIFIED ADVICE

A recommendation of a particular product or 
eourHofactlon a.......t usultableforan 
lncllvldual consumer taking accountofeuentlal 
Information relevant to• single nHd

HOLISTIC ADVICE

A  recommendation of 
a particular product 
or course of action 
assessed as suitable for 
a consumer's overall 
financial situation 
taking account of 
comprehensive 
information about 
their needs and 
circumstances

Figure 1: Consumer Support Options. Source: The FCA's plans to bridge the advice gap - The Lang Cat

Our Smart Personalised Finance Management Framework presents a tangible and actionable 
methodology to tackle this. By integrating Open Finance data, AI and data-driven predictive 
analytics and behavioural insights, our framework can help drive personalised, scalable support 
consistent with the AGBR’s targeted support approach. This can enable firms and innovators to 
provide  meaningful,  timely  financial  guidance  that  helps  consumers  improve  their  financial 
health and resilience sustainably.

1.3 From Open Banking to Open Finance

The EU’s Payment Services Directive 2 (PSD2) and the UK’s Competition and Markets Authority 
(CMA) Open Banking mandate required banks to expose payment-account data and payment-
initiation services via secure Application Programming Interfaces (APIs). Open Banking proved 
a  powerful  opportunity:  fintech  apps  now  offer  budgeting,  expense  categorisation  and 
streamlined credit applications. Yet its scope is limited to current accounts and payment flows, 
leaving mortgages, savings, pensions, investments and insurance data aside.

It is worth noting data breaches and risks on privacy, fraud and exploitation fronts exist from a 
risk perspective: we address these in more depth later in the paper. Another concern is bias or 
misuse of such data. This in turn can result in vulnerable consumer exploitation due to conflicts 
of interest in the use of such data, depending on who is providing targeted support and can 
arise  in  both  human  and  AI  support.  For  example,  contemporary  analysis  on  hotel  pricing 
algorithms  showcases  price  setting  frictions  due  to  adjustment  costs  of  human  decision 
makers,  which  induce  a  conflict  of  interest  with  the  algorithmic  advisor.  Such  costly  price 
adjustments lead to  suboptimal pricing  by human decision makers and  the  losses from  this 
strategic bias can be avoided with a full shift to automated algorithmic pricing [11].

Financial Regulation Innovation Lab (FRIL) | 3

---

<!-- PAGE 10 -->

Open Finance extends the API-driven paradigm to a full spectrum of financial products (see 
Figure 2). Under customer consent, it enables:

•  Credit products: mortgages, personal loans, credit cards. 
•  Savings & investments: deposit accounts, ISAs. 
•  Pensions & retirement products: Defined Contribution (DC) pot valuations, contribution

histories. 
Insurance policies: life, home, auto; coverage, premiums, claims history.

• 
•  Government benefits & incentives: Universal Credit, Child Benefit, pension credit.

This richer dataset allows a truly holistic view of financial health and underpins advanced AI-
driven guidance engines.

BNPL 
~ Fo='oJ 
ld Au.to  Loal'\  GMortgage

%  HELOC

CheckiJ'\9

1=---~1

Figure 2: Open Finance as an extension of Open Banking. Source: How to Survive Open Banking - Fintech Takes

1.4 Defining financial health and resilience

In  our  work,  financial  health  is  considered  not  merely  as  credit  worthiness  but  as  a  multi-
dimensional  construct  combining  ability  to  meet  day-to-day  obligations,  capacity  to  absorb 
shocks, and readiness for future goals. The FCA, in its 2021 guidance, identifies four primary 
drivers of vulnerability: low financial resilience, poor health, recent negative life events and low 
capability.  Of  these,  low  financial  resilience  (the  inability  to  hold  out  against  unexpected 
expenses without falling into difficulty) was the most common, affecting approximately one 
quarter of UK adults in 2022 (12.9 million people) [12].

Financial Regulation Innovation Lab (FRIL) | 4

---

<!-- PAGE 11 -->

Financial health encompasses four pillars [13], [14]:

Pillar

Spend

Save

Borrow

Descriptor 
Covering essential needs without 
overextending. 
Building buffers for planned and 
unplanned events. 
Accessing and managing credit 
sustainably.

Example Financial Products 
Current accounts, credit cards, store 
cards  
Savings and investment accounts, 
ISA 
Credit cards, short term loans, car 
finance and more

Plan

Setting and pursuing financial goals.

Insurance, retirement products

Financial health is not just about having a good credit score or being able to pay the bills  – 
instead, it is about balancing everyday spending, saving for a rainy day, borrowing sensibly, and 
planning ahead for the future. At the heart of all these elements lies financial resilience – the 
capacity to cope when circumstances change unexpectedly.

1 
Spend  less 
than income

3 
Have sufficient 
liquid savings

5 
Have manageable 
debt

7 
Have appropriate 
insurance

2 
Pay  bills 
on time

4 
Confident wil l 
meet long-term 
financial goals

6 
Have a prime 
credit score

8 
Plan  ahead 
financially

Figure 3: Main pillars of Financial Health. Source: What is Financial Health? – Financial Health Network

Financial resilience is the thread running through each pillar of financial health. Being able to 
spend wisely relies on having reserves to fall back on in an emergency. Saving and borrowing 
work best when people can manage cashflow and debt without resorting to costly credit. And 
effective  financial  planning  depends  on  being  prepared  for  both  personal  and  economic 
uncertainties.

Regulators like the FCA increasingly highlight resilience as a key factor in financial vulnerability. 
It is not just about having financial wellbeing at a single point in time but also about sustaining 
that  wellbeing  in  the  face  of  change  –  whether  that  is  an  unexpected  expense,  income 
fluctuation or larger economic shifts.

Financial Regulation Innovation Lab (FRIL) | 5

---

<!-- PAGE 12 -->

Examples of key resilience metrics can be illustrated with the following:

•

Buffer ratios: liquid assets (current + savings) divided by essential monthly outflows.  
Cashflow volatility: the rolling standard deviation of net inflows over recent periods.

• 
•  Debt-service coverage: ratio of income to scheduled debt payments under stress

scenarios.

•  Days-to-buffer-breach: estimated number of days before liquid assets fall below the

minimum required buffer threshold.

Integrating financial resilience into the holistic assessment of financial health provides a more 
dynamic  and  practical  framework.  It  ensures  that  interventions  and  innovations  in  finance 
support  people,  not  only  in  maintaining  financial  wellbeing  today,  but  also  in  adapting  and 
prospering for the future.

As  holistic  financial  data  becomes  central  to  improving  financial  health  and  resilience,  it  is 
crucial  to  use  such  data  ethically  and  avoid  bias  [15],[16].  The  aim  must  be  to  support 
individuals, not to allow firms to benefit at their expense.

1.5. Industry & Regulatory perspectives

Studies on Alternative Credit Scoring and Financial Resilience

Global  institutions  like  the  World  Bank  and  the  International  Monetary  Fund  (IMF)  have 
highlighted the potential of alternative credit scoring methods that go beyond traditional credit 
histories. These approaches often incorporate behavioural indicators, psychometrics and non-
financial  data  to  evaluate  creditworthiness  more  holistically  and  inclusively,  especially  for 
underserved  populations.  For  example,  the  World  Bank’s  Entrepreneurial  Finance  Lab 
developed psychometric credit scoring [17] to better assess small business owners in emerging 
markets, improving access without raising default risk. The IMF has further explored how ML 
and alternative data enhance risk assessment, supporting fairer credit access [18]. Parallel to 
credit scoring innovation, frameworks focused on financial resilience have emerged – such as 
the Financial Health Network’s model that measures individuals’ capacity to absorb shocks and 
manage financial wellbeing over time, moving beyond simple balance sheet assessments [19].

Individual differences that predict success and achievement in all professional domains may 
offer another approach to alternative credit scoring and determining financial resilience. For 
example, grit, defined as perseverance and passion for long-term goals, has been shown to 
account for an average of 4% of the variance in success outcomes, and is highly correlated with 
conscientiousness. It supports the idea that achievement of difficult goals entails the sustained 
and focused application of talent over time [20]. This Grit scale measurement can be achieved 
via Short Grit Scale (Grit–S) [21], an improved version of the original.

Financial Regulation Innovation Lab (FRIL) | 6

---

<!-- PAGE 13 -->

It is important to acknowledge the impact of financial technology, through channels such as 
peer-to-peer lending and “shadow banks”. For instance, research shows that due to the trust-
intensive nature of peer-to-peer lending, borrowers that appear to be more trustworthy have 
higher  probabilities  of  having  loans  funded  [22].  Indeed,  such  borrowers  are  likely  to  have 
better  credit  scores  as  well.  Overall,  impressions  of  trustworthiness  matter  in  financial 
transactions as  they predict the investor’s,  as well  as  the borrower’s, behaviour. Likewise, a 
study on the supply of financial services to small businesses found FinTech is disproportionately 
used in ZIP codes with fewer bank branches, lower incomes and more minority households, 
and  in  industries  with  fewer  banking  relationships  [23].  Further,  its  use  was  also  greater  in 
counties  where  the  economic  effects  of  the  COVID-19  pandemic  were  more  severe  and 
financial services expanded.

FinTech lenders are major suppliers of credit to small businesses and played an important role 
in  the  recovery  from  the  2008  financial  crisis.  Furthermore,  some  argue  that  reduced  bank 
lending did not have substantial effect on employment, wages and new business creation by 
2016, due to its substitution by FinTech lenders [24].

Finally, researchers explore connections between bank capital regulation and the prevalence 
of  lightly  regulated,  often  technology-enabled,  nonbanks  (i.e.  shadow  banks)  in  the  U.S. 
corporate loan market. It is found that at times when capital is scarce, such shadow banks step 
in and provide credit or funding for loans with higher capital requirements, which are offloaded 
by less-capitalised banks subject to Basel III requirements [25].

Regulations and Policy Making

Consumer protection remains a cornerstone of regulatory efforts as financial data sharing and 
AI-based  advisory  tools  expand  [26],  [27].  Sopra  Steria’s  recent  research  emphasises  the 
importance  of  safeguarding  consumer  interests  in  this  evolving  landscape,  highlighting 
transparency,  fairness  and  data  privacy  as  key  enablers  of  trust  [28].  Furthermore,  the  FCA 
(through its AGBR) is actively redefining how financial support is delivered. The AGBR focuses 
on  innovative  regulatory  frameworks  that  enable  “targeted  support”,  offering  tailored 
guidance to groups with shared characteristics, bridging the gap between generic guidance and 
full advice and thus, improving access and outcomes [7], [29]. On the international stage, the 
Organisation  for  Economic  Co-operation  and  Development  (OECD)  advocates  advancing 
financial  literacy  and  inclusion  through  integrated  technology  and  policy  approaches, 
empowering  consumers  globally  [30].  Meanwhile,  Open  Finance  initiatives,  potentially 
accelerated  by  the  forthcoming  Payment  Services  Directive  3  (PSD3)  in  Europe,  seek  to 
standardise and broaden data  sharing  while embedding  strong  consumer  rights protections 
[31].

Financial Regulation Innovation Lab (FRIL) | 7

---

<!-- PAGE 14 -->

Industry Perspectives

Industry stakeholders recognise the transformative power of Open Finance for personalised 
financial  wellness.  Market  reports  observe  a  rising  trend  in  dynamic,  AI-driven  financial 
planning tools, delivering real-time insights and tailored recommendations [32], [33]. Firms like 
Cleo  and  MoneyHub  demonstrate  this  shift  by  integrating  Open  Finance  data  with  ML  to 
enhance budgeting, debt management and forward-looking planning for consumers [34], [35]. 
MoneyHub’s recent expansions (e.g. partnering with Experian to accelerate debt repayment 
[36]  and  with  Pennyworth  to  democratise  financial  planning  [37])  showcase  practical 
deployments  of  personalised  financial  management  at  scale.  Additionally,  AI-driven  digital 
platforms  are  increasingly  engaging  consumers  who  live  paycheck  to  paycheck,  offering 
support customised to their needs [38]. Such initiatives, embedding Open Finance capabilities, 
demonstrate  clear  industry  momentum  toward  closing  the  financial  wellness  gap  and 
promoting resilience.

Contrasting Viewpoints

Despite these advances, persistent concerns exist around data privacy, algorithmic bias, and 
consumer  trust  [39].  The  aggregation  of  personal  financial  data  raises  risks  of  misuse  and 
unintended  discrimination  unless  managed  through  ethical  AI  frameworks  and  transparent 
governance  [40].  Consumer  scepticism  toward  data  sharing  further  challenges  adoption, 
underscoring the need for clear communication and robust protections to build confidence in 
emerging financial tools.

Financial Regulation Innovation Lab (FRIL) | 8

---

<!-- PAGE 15 -->

2. Open Finance: Data integration and customer

segmentation

The transition from traditional banking to Open Finance represents one of the most significant 
paradigm  shifts in the financial services industry  [12]. This  evolution moves far beyond the 
foundational  concepts  of  Open  Banking  to  encompass  a  comprehensive  ecosystem  that 
integrates  diverse  financial  data  sources  including  mortgages,  insurance,  investments, 
pensions and government incentives into a unified analytical framework.

2.1 The Open Finance data revolution

Open Finance fundamentally transforms how financial institutions access and utilise customer 
data. Traditional banking systems operated in silos, with each institution maintaining isolated 
datasets that provided only fragmented views of customer financial health. The Open Finance 
framework will break down these barriers through consent-based APIs and trusted third-party 
frameworks,  enabling  the  creation  of  comprehensive  financial  profiles  that  span  multiple 
institutions and product categories [41].

The scope of data available through Open Finance extends significantly beyond transactional 
information. Modern implementations can capture income patterns, expenditure categories, 
debt  obligations  across  multiple  products,  savings  behaviours,  pension  contributions, 
insurance  coverage  details  and  participation  in  government  financial  incentives  such  as 
Individual  Savings  Accounts  (ISAs).  This  rich  data  environment  can  also  incorporate  event-
driven disclosures that capture life-changing events, dependency changes and employment 
transitions that significantly impact financial circumstances [42].

Category

Credit Products

Savings & Investments

Pensions & Retirement

Insurance

Government Benefits & 
Incentives

Examples / Data Types

Mortgages: outstanding balances, amortisation schedules, 
rate resets. 
Personal loans & credit cards: credit limits, utilisation, 
minimum payments. 
Deposit accounts & ISAs: balances, interest rates, 
contribution histories. 
Brokerage accounts: holdings, asset valuations, transaction 
histories. 
Defined-contribution pots, contribution rates, projected 
retirement income. 
Policy details, coverage limits, premium schedules, claims 
records. 
Universal Credit, Child Benefit, Pension Credit, ISA 
allowances, tax relief data.

Financial Regulation Innovation Lab (FRIL) | 9

---

<!-- PAGE 16 -->

Credit Products

Open  Finance  is  reshaping  access  to  credit  information  by  enabling  lenders  to  supplement 
traditional bureau data with  live  account-level  insights [43]. The democratisation  of  data  is 
lowering  entry  barriers  for  fintechs,  encouraging  competition  and  innovation  in  consumer 
lending  [44].  At  the  same  time,  consumers’  credit  product  usage  is  diversifying,  with  many 
households managing a mix of mortgages, loans and revolving credit [45].

▪  Mortgages:  Data  on  outstanding  balances,  amortisation  schedules  and  rate  resets  is 
gathered via the FCA’s Mortgage Lending and Administration Return (MLAR), submitted 
quarterly by mortgage lenders in the UK [46]. Such integration supports both lenders and 
regulators in monitoring repayment risks and borrower resilience.

▪  Personal  Loans  &  Credit  Cards:  Open  Banking  is  already  deployed  to  improve  lending 
decisions by giving providers real-time access to loan affordability, credit limits, utilisation 
and minimum repayment histories. This dynamic visibility allows for more accurate credit 
risk profiling and prevents overextension.

Savings & Investments

Open Finance expands beyond transactional accounts into the broader realm of wealth and 
asset management [42],[47].

▪  Deposit Accounts & ISAs: Access to balances, accrued interest, and contribution histories

provides a dynamic view of liquidity and savings capacity.

▪  Brokerage  Accounts:  With  Open  Finance  frameworks,  historical  data  on  investment 
holdings  and  valuations  can  be  made  portable  across  platforms,  enhancing  consumer 
choice and advisory services.

Pensions & Retirement

Pensions are among the most significant assets for many households, yet they are traditionally 
fragmented and opaque. For example, as an individual’s employment changes, their pension 
providers may do as well. For an individual, these changes can be unclear and difficult to track.  
Structured  access  to  defined-contribution  pots  and  retirement  income  projections  is 
highlighted  in  [47],  [48].  This  shift  would  allow  individuals  to  view  contribution  rates, 
investment  performance  and  projected  retirement  income  in  one  place,  significantly 
improving retirement planning.

Insurance

Insurance data remains at an early stage in the Open Finance journey. Future phases outlined 
by  the  OBIE  envision  access  to  policy  details,  coverage  limits,  premium  schedules,  claims 
records  and others [42].  Incorporating  such datasets into financial health models  can allow 
consumers  to  understand  their  protection  gaps,  while  enabling  insurers  to  personalise 
offerings based on holistic financial profiles.

Financial Regulation Innovation Lab (FRIL) | 10

---

<!-- PAGE 17 -->

Government Benefits & Incentives

A forward-looking extension of Open Finance lies in the integration of government benefits 
and tax-related incentives. Universal Credit, Child Benefit, Pension Credit, ISA allowances and 
tax  reliefs  all  play  a  material  role  in  financial  wellbeing.  Incorporating  such  data  into  Open 
Finance ecosystems would give households comprehensive visibility of their entitlements and 
improve the ability of financial advisors and digital tools to deliver tailored guidance [47].

2.2 Data structures

The technical infrastructure supporting Open Finance relies on standardised data schemas and 
temporal  structuring1  approaches  [32],[49].  Account-customer  relationships  are  mapped 
through  sophisticated  data  models  that  maintain  event  timeline  tagging  and  spending 
categorisation systems. These structures enable both time-series analysis and static attribute 
analysis for demographic and behavioural segmentation [41]. Integration with external data 
sources, including census data, house price indices, and regional deprivation indices, further 
enriches the analytical potential of Open Finance datasets.

Designing  the  data  architecture2  compatible  with  Open  Finance  involves  careful  schematic 
structuring to accommodate data streams from multiple financial products. This may involve 
relational  or  graph-based  schemas3  (see  Figure  4)  that  associate  customers  with  multiple 
account entities spanning different providers and product types. Each account is tagged with 
a timeline of events (e.g. transactions, contributions, expenditure, and facilitating temporal 
structuring).  Transactions  and  financial  behaviours  are  categorised  hierarchically  to  reflect 
spending  patterns  (for  example  rent,  discretionary  spending,  utilities),  debt  servicing,  and 
income sources.

1 Temporal data is information that involves time – data points that have timestamps or durations, such as records 
of  events,  changes,  or  states  occurring  at  different  moments.  Read  more:  Three  Aspects  of  Temporal  Data  - 
DATAVERSITY

2 Data Architecture – a blueprint for how data is collected, stored, managed and used. Read more: What Is a Data 
Architecture? | IBM

3 Relational schemas organise data into tables with rows and columns, while graph-based schemas connect data 
like a web of relationships using nodes and links (like social networks). Read more: What is A Graph Database? A 
Beginner's Guide | DataCamp

Financial Regulation Innovation Lab (FRIL) | 11

---

<!-- PAGE 18 -->

GRAPH DB

RELATIONAL DB

8  RESIDESAT  8

Customer  - - - -+

Location

\

f

f

8

- -DE_LIVE_ RS _

\ 
_ 8

PRODUCT

CUSTOMER

I

ORDER

..

..

I

I 
I

SUPPLIER

LOCATION

..

Figure 4: Graph vs Relational schema. Source: Graph Database vs Relational Database

Temporal  structuring  is  fundamental  to  capturing  both  static  attributes  (e.g.  date  of  birth, 
region, occupation) and evolving time-series data, such as monthly cash flows or investment 
portfolio  valuations  [49].  This  dual  approach  supports  both  cross-sectional  snapshots  and 
trend-based analyses, enabling dynamic risk scoring and forecasting.

Integration  with  external  data  sources  augments  the  internal  financial  dataset.  Linking  to 
census data, house price indices (HPIs), regional deprivation indices or labour market statistics 
enriches demographic and behavioural context. Such linkages improve accuracy where data 
gaps  exist,  enhance  segmentation  models  and  enable  robust  benchmarking  against 
population-level trends.

2.3 Data sharing mechanisms

Central to Open Finance’s architecture are consent-based APIs, which empower consumers to 
authorise  specific  data  access  between  financial  institutions  and  authorised  third  party 
providers (TPPs).

TPPs  operate  as  intermediaries  facilitating  data  aggregation  and  service  delivery  across 
multiple financial institutions, giving consumers a consolidated financial view beyond siloed 
accounts.  Their  role  is  critical  for  seamless  data  ingestion  and  delivering  personalised 
recommendations. By leveraging secure APIs and consent arrangement platforms, TPPs enable 
customers to benefit from comprehensive insights without compromising data security.

In  summary,  this  framework  of  consent-driven  APIs,  robust  regulatory  support  and  trusted 
intermediaries lays the foundation for Open Finance to deliver holistic financial management 
and proactive future planning.

Financial Regulation Innovation Lab (FRIL) | 12

---

<!-- PAGE 19 -->

2.4 Advanced customer segmentation through AI-driven analytics

The wealth of data available through Open Finance will enable unprecedented sophistication 
in customer segmentation approaches. Traditional demographic segmentation based on age, 
income, geography etc will be superseded by behavioural and financial health-based clustering 
methodologies that provide much more actionable insights for financial service providers [41], 
[50].

identify  patterns

leverage  ML  techniques  to

Modern  segmentation  approaches 
in 
transactional  data  that  reveal  spending  periodicities,  savings  capacity  assessments  and 
predictive indicators of future financial behaviour. These algorithms can detect subtle patterns 
such  as  seasonal  spending  variations,  response  to  economic  shocks,  and  propensity  for 
financial product adoption that would be impossible to identify through traditional analytical 
methods [41]. It is important to note that ML techniques can perform better than traditional 
economic  forecasting  methods  in  many  settings  and  are  especially  useful  when  financial 
markets are uncertain or behave  in non-linear ways. With proper tuning and testing, these 
models  can  offer  clearer  and  more  accurate  predictions.  However,  in  some  cases,  simpler 
models like factor models work just as well or even better, especially when the data is stable 
and the relationships are mostly linear. Not every ML application improves results, and overly 
complex models can perform worse if not carefully managed. The key is to use ML when it 
adds real value, while still keeping traditional models as strong benchmarks. More in-depth 
scientific discussion can be found in [51] and [52].

The  implementation  of  clustering  techniques  such  as  K-means,  DBSCAN  and  hierarchical 
clustering on Open Finance data reveals distinct customer archetypes that align with different 
financial health profiles and advisory needs. Sopra Steria & Oxford University’s collaborative 
research  demonstrates  that  effective  clustering  can  identify  groups  such  as  "Emerging 
Professionals  with  Debt",  "Disciplined  Debt  Navigators",  "Established  and  Secure 
Homeowners",  "Vulnerable  and  Delinquent  Renters"  and  others,  each  requiring  tailored 
financial guidance strategies [53].

Advanced clustering methodologies incorporate both demographic features and behavioural 
indicators  derived  from  transaction  analysis.  Financial  prudence  scores,  debt  management 
patterns, discretionary spending volatility and investment allocation preferences all contribute 
to  more  nuanced  customer  understanding.  These  multidimensional  approaches  enable 
financial  institutions  to  move  beyond  simple  income-based  categorisation  toward  truly 
personalised service delivery [54].

Financial Regulation Innovation Lab (FRIL) | 13

---

<!-- PAGE 20 -->

2.5 Privacy-preserving data enhancement

The  sensitive  nature  of  financial  data  requires 
sophisticated approaches to data privacy and often the 
use  of  synthetic  data  generation  for  development. 
Privacy-preserving 
those 
regulatory 
compliant  with  GDPR 
frameworks,  are  essential  for  enabling  innovation 
while protecting customer interests [55],[56].

techniques,  particularly

and  other

Synthetic  data  generation  techniques  using  advanced 
ML models, including Generative Adversarial Networks 
(GANs)4  and  Variational  Autoencoders  (VAEs)5  (see 
Figure  5),  enable  the  creation  of  realistic  financial 
datasets that maintain statistical properties of original 
data while eliminating direct personal identifiers. These 
for  model 
approaches  are  particularly  valuable 
development, testing and research collaboration [57].

VAE:  Variational autoencoders

Encoder

Latent space

(x,y)

z

GAN:  Generative adversarial networks

♦ }

Decoder

(x,y)

Empirical data 
distribution

( 11~%

:  Real 
:  or 
:  fake?

■ ♦ }

Gaussian 
noise

Generator  Synthetic data  Discriminator

Figure 5: Technical schematic representations of 
VAEs and GANs. Source: Chemistry Europe

imputation  methods,  e.g.  Bayesian

inference6  approaches,  provide  robust 
Statistical 
frameworks  for  enhancing  existing  datasets  with  additional  demographic  and  behavioural 
attributes. These techniques leverage publicly available distributional data from sources such 
as  the  Office  for  National  Statistics  (ONS)  to  enrich  synthetic  datasets  while  maintaining 
realistic correlation structures between variables [53]. The implementation of diverse privacy 
techniques ensures that synthetic data generation processes provide mathematically rigorous 
privacy guarantees. These approaches inject  carefully  calibrated  noise  into data generation 
processes to prevent individual record identification while preserving overall dataset utility for 
analytical purposes [55].

4 Generative Adversarial Networks (GANs) are a type of AI that generates new, realistic data, like images or music, 
by pitting two neural networks against each other in an iterative competitive game. One network ("generator") 
creates fake data, while the other ("discriminator") tries to tell the difference between the fake data and the real 
data it was trained on. Read more: Generative Adversarial Networks Explained | AWS

5 Variational Autoencoders (VAEs) are AI models that learn to generate new, similar data like images or text by 
understanding the underlying "rules" or patterns in existing data. They contain an encoder that maps input data 
to a "fuzzy" representation and a decoder that takes a sample from this space and reconstructs new, similar data. 
Read more: What is a Variational Autoencoder? | IBM

6 Bayesian inference is a learning technique that uses probabilities to define and reason about our beliefs. Read 
more: Bayesian inference | Introduction with explained examples

Financial Regulation Innovation Lab (FRIL) | 14

---

<!-- PAGE 21 -->

2.6 Regulatory compliance and ethical considerations

Open  Finance  implementation  must  navigate  complex  regulatory  landscapes  that  balance 
innovation enablement with consumer protection. The Data (Use and Access) Bill and evolving 
regulatory guidance from the FCA provide frameworks for responsible data utilisation while 
encouraging technological advancement [58]. Consent-based data sharing mechanisms ensure 
that  customers  maintain  control  over  their  financial  information  while  enabling  them  to 
benefit from improved service personalisation. These frameworks require clear transparency 
about data usage purposes, retention periods and sharing arrangements with third parties.

The  role  of  intermediaries  and  trusted  third  parties  becomes  crucial  in  maintaining  data 
security and privacy while enabling innovation. These entities must demonstrate robust data 
governance  and  cybersecurity  capabilities  as  well  as  compliance  with  evolving  regulatory 
requirements [59].

Ethical  considerations  extend  beyond  regulatory  compliance  to  encompass  fairness, 
transparency  and  inclusivity  in  algorithmic  decision-making.  Open  Finance  systems  must 
actively  address  potential  biases  in  data  collection  and  model  development,  to  ensure 
unbiased outcomes across different customer segments [Error! Reference source not found.]. 
Bias can arise from incomplete, imbalanced or historically skewed data. If left unchecked, it 
risks entrenching inequalities rather than reducing them. Literature emphasises the need for 
ongoing checks, transparent algorithms and active human oversight to ensure fair outcomes 
in financial decision-making [61], [62], [63].

Ethical  frameworks  should  always  be  incorporated  to  prioritise  consumers’  financial  health 
over  business  opportunity  identification.  Recommendations  focus  on  improving  customer 
financial  health  and  resilience  rather  than  product  sales  or  revenue  optimisation.  Such  a 
customer-centric approach builds trust and supports long-term relationship development.

Transparency and explainability requirements demand that consumers understand the basis 
for  recommendations  and  can  see  how  their  specific  circumstances  influence  the  guidance 
provided.  Explainable  AI  techniques  (e.g.  SHAP7)  bring 
life  and  deliver 
recommendation  rationales  [64].  Proper  use  of  data  means  prioritising  positive  impact  on 
people’s financial wellbeing, with fairness and transparency at the core. This approach builds 
trust  in  technology  and  ensures  that  advancements  serve  everyone,  not  just  financial 
institutions.

insights  to

7 SHAP - (SHapley Additive exPlanations) is a game theoretic approach to explain the output of any ML model. 
Read more: An introduction to explainable AI with Shapley values — SHAP

Financial Regulation Innovation Lab (FRIL) | 15

---

<!-- PAGE 22 -->

2.7 Beyond Open Finance: inclusion, smart data and cross-border portability

While this paper places primary emphasis on Open Finance, it is important to recognise that 
financial health is not defined solely within the boundaries of formal financial products. Hence, 
Open Finance may not go far enough in addressing the full  spectrum of financial inclusion. 
Smart Data and Open Data initiatives, such as those being advanced under the UK Smart Data 
schemes  [65],  can  enrich  the  picture,  particularly  for  those  without  bank  accounts  or  who 
interact only minimally with financial products (e.g. those who hold only a single basic bank 
account with no available credit facilities). Utility bills, rent records, mobile phone usage and 
other non-financial sources can provide crucial signals of discipline and resilience. In practice, 
this  broader  approach  can  help  ensure  that  individuals  who  are  financially  inactive, 
underserved or “off-grid” are brought into the fold, as a key part of inclusion efforts.

To  ensure  inclusion,  modelling  frameworks  should  anticipate  dedicated  clusters  for  the 
“financially invisible”. These individuals may not receive highly tailored recommendations due 
to  limited  data,  but  they  can  still  benefit  from  generalised,  yet  actionable,  advice  that 
safeguards against exclusion. By recognising varied levels of data richness, personalised and 
group-based advice can be delivered at scale, ensuring that the benefits of financial technology 
reach  as  many  people  as  possible.  This  addresses  social  equity  and  supports  smarter  risk 
management.

Looking beyond national boundaries, financial health frameworks (when built on verifiable and 
transferable data) hold promises for supporting mobility across borders. The ability to ‘carry’ 
one’s  credit  score,  resilience  metric  or  financial  health  indicators  internationally  could 
empower individuals to access fair financial products wherever they choose to live or work, 
removing a longstanding barrier for those relocating. With initiatives such as PSD3 in Europe 
[66], which aims to expand and harmonise access to financial data across borders, there is an 
opportunity  to  embed  verification  and  interoperability  mechanisms  into  Open  Finance 
architectures.  Such  portability  would  generate  Pareto-optimal8  benefits:  consumers  retain 
recognition of their financial discipline internationally, while institutions reduce onboarding 
risks and open new opportunities for responsible growth.

8  Pareto  optimality  (efficiency)  describes  a  situation  where  resources  are  allocated  in  the  best  possible  way, 
making it impossible to improve one person's situation without negatively affecting another. Read more: Pareto 
Efficiency Examples and Production Possibility Frontier

Financial Regulation Innovation Lab (FRIL) | 16

---

<!-- PAGE 23 -->

3.  Predictive analytics & cash flow modelling  
The  foundation  of  effective  financial  guidance  and  tailored  recommendations  in  the  Open 
Finance era rests on sophisticated cash flow modelling capabilities that can accurately predict 
and  analyse  individual  customer  financial  trajectories.  These  modelling  approaches  must 
capture the complexity of modern financial lives, whilst providing actionable insights for both 
short-term stability optimisation and long-term wealth building strategies.

3.1 Comprehensive data sourcing

Effective  modelling  requires  robust  and  comprehensive  data  sourcing  that  reflects  the 
complexity of modern personal finance.

•  Open Finance Data: Core financial data is aggregated from multiple providers within the 
Open  Finance  ecosystem.  Collectively,  these  datasets  offer  an  extensive  view  of 
consumers’  financial  positions  and  behaviours,  surpassing  the  limited  scope  of  Open 
Banking transactional data. Note: cash transactions outside the digital ecosystem cannot 
be tracked and hence, cannot form part of data-driven predictive modelling.

•  Consumer-Disclosed  Information: Supplementary  data  directly  reported  by  consumers 
plays a crucial role. Such event-driven disclosures provide critical context for adaptive and 
personalised modelling.

•  Publicly Available Data: External datasets enrich individual financial profiles by embedding 
them within broader socio-economic frameworks. Integrating external data informs risk 
assessments and ensures models account for environmental variables affecting financial 
resilience.

Furthermore,  modern  cash  flow  modelling  extends  far  beyond  simple  income-expense 
calculations  to  encompass  a  holistic  view  of  financial  health  that  includes  housing  costs, 
essential  expenditures,  debt  service  obligations,  discretionary  spending  patterns  and 
allocation  toward  savings  and  investments.  This  comprehensive  approach  recognises  that 
financial health cannot be assessed through any single metric but requires integrated analysis 
of multiple financial dimensions [67], [68]. 
--- ---

Housing  cost  modelling,  for  example,  must  account  for  regional  variations,  tenure  types 
(rental,  mortgage,  owned  outright)  and  the  relationship  between  housing  expenses  and 
income levels across different demographics. Research demonstrates significant variation in 
housing  cost  ratios  based  on  regional  economic  conditions  [69],[70],  with  London  and 
Southeast England showing markedly different patterns compared to other UK regions (see 
Figure 6). Wealth and assets concentration in these regions plays a key role.

Financial Regulation Innovation Lab (FRIL) | 17

---

<!-- PAGE 24 -->

I 
26

I 
73

£, 000s

121  170  222  263

Bel~

Figure 6: Wealth & Assets Medians – 2018-2020.  
Source: Distribution of individual total wealth in Great Britain - Office for National Statistics

Essential expenditure modelling beyond housing presents additional complexity, as spending 
on food, transportation, and utilities varies not only with income levels but also with regional 
cost  structures  and  individual  lifestyle  choices.  Advanced  modelling  approaches  use 
Iterative  Proportional  Fitting9,  Propensity  Score  Matching10,  and 
techniques 
Counterfactual  Identification11  to  generate  realistic  joint  distributions  that  respect  both 
regional and income-based marginal constraints while introducing appropriate stochasticity to 
capture individual variation.

like

Debt service modelling requires sophisticated understanding of different credit product types, 
interest  rate  structures,  payment  timing  patterns  etc.  The  framework  must  distinguish 
between  revolving  credit  (credit  cards,  overdrafts)  where  payment  obligations  vary  with 
utilisation and fixed credit products (personal loans, mortgages) with predetermined payment 
schedules.  Integration of  late payment patterns and  associated penalty  structures provides 
crucial insights into financial stress indicators.

9 Iterative Proportional Fitting techniques – mathematical methods that adjust a dataset, such as a table of data, 
to make its row and column totals match a known set of target marginal totals from a different source. Read 
more: Iterative Proportional Fitting | TF Resource

10 Propensity score matching (PSM) – statistical method used in observational studies to reduce selection bias 
when estimating the effect of a treatment. Read more: Understanding the Propensity Score: A Guide to Reducing 
Bias | DataCamp

11 Counterfactuals help to identify which aspects of the input data are most influential in the model's decisions, 
aiding  in  model  debugging,  fairness  analysis  and  improving  model  performance.  Read  more:  Counterfactual 
Explanations: The What-Ifs of AI Decision Making

Financial Regulation Innovation Lab (FRIL) | 18

---

<!-- PAGE 25 -->

3.2 Dynamic risk assessment and behavioural prediction

Advanced cash flow modelling incorporates predictive analytics capabilities that can anticipate 
future financial stress, identify emerging opportunities for financial improvement and adapt 
recommendations based on changing circumstances. These capabilities rely on ML techniques 
that can identify subtle patterns in financial behaviour that precede significant financial events 
[50], [71]. 
--- ---

Transaction  pattern  analysis  reveals  cyclicality  in  financial  behaviour  that  can  inform  both 
short-term  cash  flow  forecasting  and  long-term  financial  planning.  Algorithms  capable  of 
detecting spending seasonality, income volatility and irregular financial  events enable more 
accurate prediction of future cash flow challenges and opportunities [41].

Behavioural risk assessment leverages advanced analytics to ultimately identify early warning 
indicators of financial distress. These may include increasing credit utilisation rates, growing 
payment  delays,  changes  in  discretionary  spending  patterns  or  shifts  in  savings  allocation 
behaviours. ML models trained on historical patterns can identify customers at risk of financial 
difficulty with sufficient advance warning to enable proactive intervention.

Such  models  may  also  add  potential  monitoring  benefits  in  other  contexts.  For  example, 
undiagnosed memory disorders in early stages impact a broad range of financial outcomes, 
such as: credit card account payment delinquency and amount of delinquent balance, credit 
utilisation among credit card account holders, mortgage delinquency and delinquent balance 
amount,  and  credit  scores.  These  effects  are  seen  across  seniors  in  single  and  coupled 
households, racial/ethnic minorities and non-minorities, and older adults living in areas with 
higher  and  lower  education  levels  [72].  Clinically  informed  lead  indicators  of  dementia, 
extended to include money management difficulty (which emerges as the most important lead 
indicator), can inform a high-performance AI model to predict a clinical diagnosis [73]. Armed 
with  this  knowledge,  financial  institutions  can  enhance  their  protection  of  vulnerable 
customers with dementia and, potentially, inform the intergenerational transfer of financial 
control. Likewise, mergers of large regional banks leading to branch closures and tighter credit 
constraints in counties harm the mental health of lower-income individuals [74]. Conversely, 
regulatory  reforms  that  improved  credit  conditions  reduced  mental  depression,  boosted 
labour  market  outcomes,  eased  access  to  mortgage  debt,  and  reduced  the  ranks  of  the 
“unbanked”  [74].  Lastly,  permissive  laws  deputising  financial  professionals  to  screen  for 
misbehaviour  without  providing  explicit  incentives  are  shown  to  result  in  fewer  reports  of 
abuse by financial professionals and, separately, in financial crimes against the elderly, with a 
stronger  impact  for  isolated  elders  [75].  This  showcases  how  financial  professionals  can 
prevent financial fraud and combat social problems, an important contribution of finance to 
society.

Financial Regulation Innovation Lab (FRIL) | 19

---

<!-- PAGE 26 -->

3.3 Feature selection & engineering

Identifying  the  most  explanatory  variables  essential  for  accurate  predictions  and  insightful 
customer  segmentation  involves  multiple  analytical  techniques,  alongside  careful  ethical 
considerations.

In order to extract data features that capture both the static attributes and dynamic financial 
behaviours driving individual financial health and trajectories, the following techniques can 
be used:

Technique

Description

Correlation Analysis & Mutual Information

Chi-squared Binning

Principal Component Analysis (PCA)

Stepwise Regression

LASSO Regression

Time-Based Feature Engineering

Permutation Feature Importance

Measures linear and non-linear relationships between features 
and target variables.

Evaluates categorical variables’ predictive power and enables 
effective discretisation.

Reduces dimensionality by extracting orthogonal components 
explaining variance.

Iteratively adds or removes features to find the best predictive 
subset. 
LASSO (Least Absolute Shrinkage and Selection Operator) uses 
regularisation to penalise less important features, promoting 
model sparsity. 
Creates temporal variables such as spending volatility, seasonal 
trends, late payment counts.

Measures a feature's importance by calculating the decrease in a 
model's performance after shuffling the feature's values.

In addition, the following ethical considerations must be embedded in the data processing:

•  Protected Characteristics: Features relating to sensitive personal attributes, including but 
not limited to race, gender, disabilities etc. Their inclusion requires clear justification and 
transparency, to avoid bias and discrimination.

•  Fairness Constraints: The modelling framework should apply fairness-aware principles to 
ensure that selected features do not inadvertently conserve historical biases or result in 
unfair  outcomes  for  protected  groups  [76],  [77],  [78].  Continuous  monitoring  and 
adjustment are required to uphold ethical standards in financial decision-making.

3.4 Predictive modelling & clustering

Building on carefully engineered features, a suite of AI/ML models can be utilised to generate 
personalised financial health scores, and customer segmentation.

Financial Regulation Innovation Lab (FRIL) | 20

---

<!-- PAGE 27 -->

Model Type

Examples

Purpose & Characteristics

Logistic Regression

N/A

Baseline model for binary classification, valued for 
interpretability.

Ensemble Learning 
Methods

XGBoost, LightGBM, 
Random Forest

Handles complex relationships, reduces overfitting, suitable for 
classification and regression.

Neural Networks

LSTM

Unsupervised 
Learning

Reinforcement 
Learning

k-means, DBSCAN, SOMs

Q-Learning, Deep Q-
Networks (DQN), Proximal 
Policy Optimisation

General-to-Specific 
(GETS) Modelling

Autometrics, Hendry’s 
Classical, Dynamic GETS 
Models

Captures temporal dependencies and seasonality in sequential 
financial data.

Identifies clusters or segments within customer data for 
personalised insights.

Enables dynamic planning and real-time adaptive 
recommendations, based on feedback.

Used for variable selection by starting with a general model and 
simplifying it step-by-step. Retains only statistically significant 
variables, ensuring models are both data-driven and 
economically meaningful. Helps identify key determinants in 
large datasets while avoiding overfitting.

Typical Model Outputs:

•  Financial  Health  Scorecard: A  composite  metric  that  provides  a  holistic  measure  of  an 
individual’s current financial health and risk exposure. It reflects cashflow stability, debt 
management, sustainable growth in savings & investment and others.

•  Resilience  Index: This  index  quantifies  an  individual’s  capacity  to  withstand  adverse 
macroeconomic shocks, incorporating scenario analysis informed by economic indicators 
such  as  unemployment  rates,  inflation  levels  and  housing  market  trends.  Monte  Carlo 
simulations12 and stochastic modelling techniques can be used to achieve this.

•  Clustering Results: Customer clusters derived from unsupervised methods identify typical 
financial  personas  and  segments,  informing  tailored  recommendation  strategies  and 
product  offerings.  Clustering  outcomes  are  usually  validated  via  silhouette  scores13  and 
external benchmarking. Other methods that may be considered within this context include 
Linear Discriminant Analysis14 and Support Vector Machines15.

12  Monte  Carlo  simulations  -  computational  method  that  uses  repeated  random  sampling  to  generate  a 
distribution of potential outcomes for an uncertain event or process. Read more: Monte Carlo Simulation: What 
It Is, How It Works, History, 4 Key Steps

13 Silhouette score - a metric used to evaluate the quality of clustering in unsupervised machine learning. The 
silhouette score assesses both cohesion (how similar a point is to its own cluster) and separation (how dissimilar 
a point is to neighboring clusters).

14 Linear Discriminant Analysis – a supervised ML technique used for dimensionality reduction and classification 
by finding a linear combination of features that maximizes the separability between known classes. Read more: 
What Is Linear Discriminant Analysis? | IBM

15  Support  Vector  Machine  -  a  supervised  ML  algorithm  that  finds  the  best  line  or  "hyperplane"  to  separate 
different classes of data. Read more: What Is Support Vector Machine? | IBM

Financial Regulation Innovation Lab (FRIL) | 21

---

<!-- PAGE 28 -->

3.5 Model explainability vs performance

The  success  of  AI-driven  financial  models  rests  on  balancing  predictive  performance  with 
interpretability.  While  high  predictive  accuracy  metrics  (such  as Precision, Recall, F1  Score, 
in  classifying  or  forecasting  financial 
and Log-loss)  demonstrate  model  effectiveness 
behaviours (e.g. probability of default or cash flow stability), these alone are insufficient for 
transparent customer engagement and regulatory compliance.

•  Precision quantifies the correctness of positive predictions (in our case correctly

identifying at-risk customers).

•  Recall captures the model’s ability to detect all relevant positive cases.

•  F1 Score harmonises precision and recall into a single metric.

•

Log-loss evaluates the confidence of probabilistic predictions, penalising overconfident 
errors.

Other measures for practical applicability and predictive power such as proportion of variation 
(R2), Mean Squared Error, Root Mean Squared Error, Mean Absolute Error, other loss functions 
(e.g. quasi-likelihood function, asymmetric loss function) and more [79],[80],[81].

In financial health contexts, where trust and accountability are most important, explainable AI 
(XAI) techniques such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable 
Model-agnostic  Explanations)  play  a  pivotal  role.  These  tools  dissect  complex  AI  models  to 
provide:

•  Data  feature-level  insights  showing  how  individual  inputs  (such  as  income  volatility,

discretionary spend etc) influence predictions.

•

Local explanations that clarify a specific decision for an individual customer, essential for 
personalised recommendations.

There is a trade-off between interpretability and predictive power. Simpler models like logistic 
regression offer clear rationales but may miss compound patterns, while complex ensembles 
or neural networks may capture deeper relationships at the cost of harder interpretability. This 
paper acknowledges the trade-off at a high level - detailed exploration is reserved for works 
focused on AI fairness and regulatory explainability.

3.6 Stochastic modelling and scenario analysis

The inherent uncertainty in financial planning requires stochastic modelling approaches that 
can capture the range of possible financial outcomes and their associated probabilities. Monte-
Carlo  simulation  techniques  enable  comprehensive  scenario  analysis  that  accounts  for 
variability in income, expenses, investment returns etc.

Investment  modelling  incorporates  sophisticated  stochastic  processes  including  Geometric 
Brownian Motion16 (see Figure 7) for risky asset evolution and deterministic modelling for risk-

16 Geometric Brownian Motion – a mathematical model used to describe asset prices such as stocks, that follow 
a pattern of random (but generally upward) movement. A key feature is that the asset's value cannot go below

Financial Regulation Innovation Lab (FRIL) | 22

---

<!-- PAGE 29 -->

free  savings  growth.  These  approaches  account  for  market  volatility  and  risk  tolerance 
preferences.

Figure 7: Geometric Brownian Motion Simulation. Source: Montecarlo simulation for Geometric Brownian 
Motion

Wealth  accumulation  trajectories  are  widely  held  to  be  based  upon  either  S-shaped  or 
inverted-L shaped  curves shown below for the  relationship of  income today  and tomorrow 
(and by extension wealth as a function of income) [82] – see Figure 8.

Figure 8: The S-Shape Curve and the Poverty Trap (left); the Inverted L-Shape: No Poverty Trap (right). Source: 
[82]

Age groups and income-based risk appetite modelling recognises that appropriate investment 
allocation  varies  significantly  across  different  life  stages  and  wealth  levels.  Glide  path

zero, and its changes are proportional to its current price. Read more: How to use Monte Carlo simulation 
with GBM

Financial Regulation Innovation Lab (FRIL) | 23

---

<!-- PAGE 30 -->

methodologies can adjust risk exposure based on time horizon and financial capacity, ensuring 
that investment recommendations remain appropriate as circumstances change.

Scenario analysis capabilities enable exploration of various "what-if" situations including job 
loss, health events, housing market changes, economic recession scenarios and so on. These 
analyses help customers understand the resilience of their financial plans and identify areas 
where additional protection or flexibility might be beneficial [83],[84].

3.7 Adaptation and continuous learning

Modern cash flow modelling systems must provide real-time adaptation capabilities that can 
respond immediately to changing financial circumstances. This requires regular data refresh 
capabilities  that  can  incorporate  new  transaction  information,  economic  data  updates  and 
customer-reported life changes into ongoing financial assessments [71]. As discussed earlier 
in this paper, potential non-financial benefits can result from this approach, e.g. diagnosing 
memory  disorders,  mild  cognitive  impairment,  dementia,  mental  health  deterioration  and 
others [72],[73],[74].

ML models enable continuous improvement in prediction accuracy through ongoing training 
on new data patterns [50]. These systems can identify shifts in customer behaviour, adapt to 
changing economic conditions, and refine their understanding of the relationships between 
different financial variables over time.

The  integration of feedback loops from  customer interactions and outcomes  (see  Figure  9) 
enables  model  validation  and  improvement  [41].  When  customers  report  satisfaction  with 
recommendations,  experience  financial  improvements  or  deteriorations,  this  information 
feeds back into model refinement processes.

Figure 9: An example of continuous feedback loop structure. Source: Zeda.io

Financial Regulation Innovation Lab (FRIL) | 24

---

<!-- PAGE 31 -->

4.  Smart Personalised Finance Management Framework  
The  culmination  of  Open  Finance  data  integration  and  sophisticated  cash  flow  modelling 
enables the development of comprehensive smart personalised finance management systems 
that can provide tailored, actionable financial guidance and recommendations at scale. These 
systems  must  balance  automated  efficiency  with  personalised  relevance  while  maintaining 
regulatory compliance and ethical standards.

4.1 Hierarchical financial needs framework

Effective  personalised  financial  management  recognises  that  financial  needs  exist  in  a 
hierarchical  structure,  similar  to  Maslow's  hierarchy  of  human  needs  (see  Figure  10).  This 
framework  prioritises  fundamental  financial  stability  before  progressing  to  more  advanced 
wealth optimisation objectives [85],[86],[87].

The  foundational  level  focuses  on  basic  financial  survival  through  cash  flow  stability 
optimisation.  Customers  experiencing  negative  cash  flow  or  inadequate  emergency  savings 
require immediate attention to essential expense management, income stabilisation and basic 
safety  net  establishment.  This  level  corresponds  to  the  physiological  and  safety  needs  in 
Maslow's hierarchy and must be addressed before any higher-level financial planning can be 
effective [85].

The second level addresses financial security through debt management and risk mitigation. 
Once  basic  cash  flow  stability  is  achieved,  attention  turns  to  managing  debt  service  ratios, 
eliminating high-interest debt, and establishing appropriate insurance coverage [86]. This level 
provides the foundation for more advanced financial planning by eliminating major financial 
vulnerabilities.

The third level focuses on financial independence through strategic wealth accumulation. With 
stability  and  security  established,  customers  can  pursue  long-term  wealth  building  through 
investment  optimisation,  tax  planning  and  goal-based  savings  strategies  [87].  This  level 
corresponds to self-esteem and belonging needs as customers work toward financial goals that 
enable lifestyle choices and social participation.

The highest level encompasses financial self-actualisation through legacy planning and value-
aligned  financial  strategies.  This  includes  estate  planning,  charitable  giving  and  investment 
approaches that reflect personal values and long-term societal impact.

Financial Regulation Innovation Lab (FRIL) | 25

---

<!-- PAGE 32 -->

Figure 10: Application of Maslow’s theory in a financial needs’ context.  
Source: Visualizing the Hierarchy of Financial Needs

4.2 Sequential optimisation engine architecture

The  implementation  of  hierarchical  financial  guidance  requires  sophisticated  sequential 
optimisation engines that  can  systematically address financial needs in appropriate priority 
order while avoiding premature advancement to higher-level objectives before foundational 
needs are met.

Layer 1 optimisation focuses exclusively on cash flow stability and emergency fund adequacy. 
The  system  evaluates  current  cash  flow  patterns,  identifies  potential  expense  reductions 
through  discretionary  spending  optimisation  and  essential  expense  rebudgeting,  and 
calculates feasible timelines for emergency fund accumulation. For young renters, this may 
include recommendations for temporary housing arrangement changes to dramatically reduce 
housing costs.

Financial Regulation Innovation Lab (FRIL) | 26

---

<!-- PAGE 33 -->

The optimisation engine incorporates constraint handling that recognises practical limitations 
on expense reduction while identifying all feasible improvement strategies. If cash flow cannot 
be  made  positive  through  reasonable  expense  modifications,  the  system  provides 
income 
recommendations  about  the  need  for  professional  financial  counselling  or 
enhancement strategies.

of

service

payment

Layer  2  optimisation  addresses  debt 
management 
ratio 
and 
optimisation only after Layer 1 stability 
layer  prioritises 
is  achieved.  This 
elimination 
arrears, 
reduction of high-interest debt balances 
and  optimisation  of  debt  service  ratios 
to  sustainable 
levels.  The  system 
calculates  optimal  debt  paydown 
strategies  that  balance  interest  cost 
minimisation 
flow 
with 
sustainability.

cash

Advanced  debt  optimisation 
incorporates  understanding  of  different  debt  product 
characteristics,  interest  rate  structures,  and  penalty  mechanisms.  The  system  can  identify 
optimal  balance  transfer  opportunities,  refinancing  possibilities,  and  payment  timing 
strategies that minimise total debt service costs while maintaining financial stability [88].

Layer 3 optimisation addresses wealth maximisation and goal achievement once both stability 
and debt management objectives are met. This layer incorporates sophisticated goal-based 
financial  planning 
including  housing  deposit  accumulation,  retirement  planning  and 
investment portfolio  optimisation.  Relevant economic aspects  of wealth accumulation  over 
time are examined thoroughly in [82],[89].

4.3 Personalisation and behavioural integration

Drawing  from  Sopra  Steria’s  Research  &  Development  work,  smart  personalised  finance 
management  synthesises  clustering-driven  persona  construction  with  a  hierarchical 
optimisation engine to tailor financial recommendations precisely.

Persona Construction

Clustering  analysis  has  identified  eight  distinct  customer  segments  (personas),  revealing 
heterogeneous financial conditions and behaviours:

•  Emerging Professionals with Debt: Young renters in professional roles, facing moderate

incomes but significant debt burdens and arrears risks.

Financial Regulation Innovation Lab (FRIL) | 27

---

<!-- PAGE 34 -->

•  Disciplined Debt Navigators: Financially responsible professionals adept at managing debt

and sustaining healthy cash flows.

•  Established and Secure Homeowners: Mature homeowners with stable incomes, robust

savings and strong financial discipline.

•  Vulnerable  and  Delinquent  Renters: Low-income  young  renters  burdened  by  high

financial distress and poor payment behaviours.

•  Affluent and Prudent Investors: High earners focused on wealth accumulation, investing

strategically.

•  Struggling to Start: Entry-level earners with low income and minimal savings, vulnerable

to shocks despite good payment discipline.

•  Steady  and  Responsible  Managers: Balanced  demographic  with  solid  surplus  and

moderate liabilities; exemplary payment records.

•  Crisis-Prone and Underbanked: Younger renters with persistent negative cash flow, low

savings, and limited credit access.

Defining  such  personas  enables  contextualisation  of  recommendations  and  establishes 
communication frameworks aligned with customer needs and motivational factors.

Effective personalised financial management must account for individual behavioural patterns, 
risk preferences and life circumstances that influence financial decision-making effectiveness. 
This  requires  integration  of  behavioural  finance  principles  with  technical  optimisation 
capabilities [90],[91]. For example, modelling the optimal illiquidity levels for retirement saving 
based on present  bias [92]. This research  shows the  relationship with present bias  impacts 
these levels via early pre-retirement withdrawal penalties from mandatory savings accounts, 
illustrating how a social planner would set up a simple socially optimal pension scheme. Their 
very simple mechanisms provide good welfare approximations to arbitrarily complex, optimal 
mechanisms.

Other sources investigate saving goals’ effectiveness in increasing individuals' savings from a 
fintech app’s data, finding that setting soft goals (whereby individuals face no penalties when 
deviating from their plan) causally increases individuals' savings rate [93]. Increased savings 
within the app are not at the cost of reduced savings outside the app, and soft goal setting is 
especially effective for those in the population at greater risk of under-saving. Soft goals could 
thus be deployed to help low-income individuals, who are arguably among those who could 
benefit  from  such  fintech  solutions  the  most,  and  are  also  more  scalable  and  easier  to 
administer compared to their counterpart hard goals, especially in real-life settings [93].

Other studies explore welfare consequences of retirement plan automatic enrolment policies, 
for example in [94]. At 43 to 48 months of tenure, their experimental policy raises cumulative 
contributions to such plans by 4.1% of first-year annualised salary. However, they find little 
evidence  that  auto-enrolment 
increases  financial  distress,  which  holds  even  among 
subpopulations  very  likely  to  have  large  auto-enrolment  effects  on  plan  contributions. 
Automatic  enrolment  has  a  precisely  estimated  zero  effect  on  credit  scores,  no  significant

Financial Regulation Innovation Lab (FRIL) | 28

---

<!-- PAGE 35 -->

effect on debt excluding auto loans and first mortgages and no significant positive effects on a 
range  of  measures  of  adverse  credit  outcomes,  with  the  exception  of  first-mortgage 
foreclosures.

Some researchers find that offering consumers the opportunity to adopt increased retirement 
saving behaviour immediately and then, only if they decline, inviting them to adopt it later (i.e. 
offering  “sequential  pre-commitment”)  increases  inferred  urgency,  predicting  greater 
adoption [95],[96].

Lastly, various nudge interventions for increased retirement saving merit consideration. These 
alter people’s decisions without coercion or significant changes to economic incentives and 
include especially efficacious variations like fresh start nudging and semi-automated nudging. 
Moreover,  they  compare  favourably  with  traditional  interventions/policy  tools  such  as  tax 
incentives and other financial inducements, even without restricting the menu of options and 
without altering financial incentives [97],[98].

Customer  segmentation  insights  derived  from  clustering  analysis  inform  personalisation 
strategies  that  recognise  different  customer  archetypes  require  different  communication 
approaches,  recommendation  timing  and  motivational  frameworks.  "Disciplined  Debt 
long-term  planning 
Navigators"  respond  well  to  detailed  analytical 
frameworks,  while  "Vulnerable  and  Delinquent  Renters"  require  more  immediate,  practical 
guidance with simplified decision frameworks.

information  and

Behavioural consistency modelling recognises that financial improvement requires sustainable 
behaviour change rather than short-term sacrifice. The system incorporates understanding of 
customer  spending  patterns,  seasonal  variations  and  discretionary  spending  preferences  to 
develop realistic improvement strategies that can be maintained over time [41].

Risk appetite integration ensures that investment and planning recommendations align with 
individual comfort levels and life circumstances. For instance, income-level considerations and 
personal risk tolerance assessments combine to generate investment allocations that balance 
growth potential with downside protection.

4.4 Continuous improvement and outcome tracking

Advanced  personalised  finance  management  systems  incorporate  comprehensive  feedback 
mechanisms  that  enable  continuous  improvement  in  recommendation  effectiveness  and 
customer  outcome  optimisation.  These  systems  must  track  customer  financial  health 
improvements, recommendation adoption rates, and long-term financial trajectory changes 
[41].

Performance monitoring is needed to track key metrics including emergency fund adequacy, 
debt  service  ratio  improvements,  investment  goal  progress  and  overall  financial  stress 
reduction.  These  metrics  provide  objective  measures  of  system  effectiveness  and  identify 
areas requiring refinement.

Financial Regulation Innovation Lab (FRIL) | 29

---

<!-- PAGE 36 -->

Customer  satisfaction  integration  ensures  that  technical  optimisation  aligns  with  customer 
experience  and perceived  value  [90]. Feedback mechanisms capture  customer preferences, 
communication effectiveness, and recommendation relevance to guide system enhancement.

The  integration  of  macroeconomic  monitoring  enables  system  adaptation  to  changing 
economic  conditions  and  regulatory  frameworks  [99].  This  ensures  that  recommendations 
remain relevant and effective across different economic scenarios.

Through a comprehensive framework, smart personalised finance management systems can 
deliver significant value to customers while maintaining operational efficiency and regulatory 
compliance,  ultimately  democratising  access  to  sophisticated  financial  guidance  previously 
available only to high-net-worth individuals.

Financial Regulation Innovation Lab (FRIL) | 30

---

<!-- PAGE 37 -->

5. Conclusion

The convergence of AI and Open Finance marks a fundamental shift in how financial health is 
understood, measured and supported. This whitepaper has demonstrated that moving beyond 
legacy,  credit-score-centric  systems  is  no  longer  simply  an  innovation  opportunity,  but  a 
necessity.  Recent  economic  shocks,  widening 
inequalities  and  changing  consumer 
expectations demand data-driven financial  modelling that  is  inclusive and  focused on  long-
term resilience.

Open  Finance  will  provide  the  infrastructure  to  enable  this  transformation  by  facilitating 
secure,  consent-driven  access  to  a  far  broader  range  of  financial  data.  Combined  with 
advanced AI and machine learning techniques, such as predictive cashflow modelling, persona-
based optimisation and explainable analytics – this data becomes the foundation for intelligent 
financial guidance. Rather than relying on retrospective assessments, financial institutions can 
offer proactive support: anticipating risk, identifying opportunity and tailoring interventions to 
individual circumstances.

However, technology alone is not sufficient. Ethical data stewardship, fairness, transparency 
and regulatory compliance must remain central. The FCA’s Advice Guidance Boundary Review 
and  Consumer  Duty  framework  show  that  innovation  and  consumer  protection  are  not 
mutually  exclusive but mutually  reinforcing.  Responsible AI, anchored in  explainability, bias 
mitigation and privacy safeguards, ensures these advances enhance trust rather than diminish 
it.

This transformation enables financial institutions to evolve from product providers to long-
term  financial  partners  –  supporting  everyday  budgeting,  responsible  borrowing,  future 
planning  and  improved  financial  wellbeing.  Consumers,  in  turn,  can  gain  access  to 
personalised,  non-product-specific  guidance  that  empowers  informed  decision-making  and 
strengthens resilience through life’s uncertainties.

As  Open  Finance  infrastructure  matures  in  future,  continued  collaboration  between 
policymakers, regulators, academia, industry and technology providers will be crucial. Those 
who act early – investing in data capabilities, ethical AI and human-centric design, will define 
a  more  inclusive  and  trustworthy  financial  ecosystem.  Out  of  crisis  arises  opportunity:  a 
pathway towards prosperity built on transparency, accountability and holistic financial health 
evaluation.

Financial Regulation Innovation Lab (FRIL) | 31

---

<!-- PAGE 38 -->

6. References

1.  Haldane, A.G., Aikman, D., Kapadia, S. and Hinterschweiger, M., 2017. Rethinking 
financial stability. Peterson Institute for International Economics, October 12th, 
mimeo. 
Web Access

2.  Jha, M., Liu, H. and Manela, A., 2025. Does finance benefit society? A language

embedding approach. The Review of Financial Studies, p.hhaf012. 
Web Access

3.  Alvaredo, F., Chancel, L., Piketty, T., Saez, E. and Zucman, G., 2017. Global inequality 
dynamics: New findings from WID. world. American Economic Review, 107(5), 
pp.404-409. 
Web Access

4.  Tørsløv, T., Wier, L. and Zucman, G., 2023. The missing profits of nations. The Review

of Economic Studies, 90(3), pp.1499-1534.  
Web Access

5.  Retail Economics, 2022. The Big Squeeze: Pressure on consumer finances, rising

inflation & money management. 
Web Access

6.  Bell, J., Jurgenson, J., Warmath, D., 2025. The Role of Objective Financial Situation and 
Psychological Outlook in the Relationship Between Personal Life Shocks and Financial 
Well-Being. Journal of Consumer Behaviour 24: 632-654. 
Web Access

7.  Thinks Insights & Strategy and Financial Conduct Authority (FCA), 2025. Advice

Guidance Boundary Review: Retail Investments Consumer Research. 
Web Access

8.  Carbon Financial, 2025. Bridging the advice gap: why only 8% of UK adults seek

financial guidance. 
Web Access

9.  Bao, L., Huang, D. and Lin, C., 2024. Can artificial intelligence improve gender

equality? Evidence from a natural experiment. Management Science. 
Web Access

10. Bayer, R.C. and Renou, L., 2024. Interacting with Man or Machine: When Do Humans

Reason Better?. Management Science. 
Web Access

11. Garcia, D., Tolvanen, J. and Wagner, A.K., 2024. Strategic responses to algorithmic

recommendations: evidence from hotel pricing. Management Science. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 32

---

<!-- PAGE 39 -->

12. Bukovski, K., Cepkauskaite, A., Shaikh, S., Finch, J. & Otioma, C., 2025. Consumers at 
the heart of innovation: Financial health evaluation in the UK regulatory landscape. 
Web Access

13. NASA Federal Credit Union, 2024. The four pillars of financial health.

Web Access

14. Financial Health Network, 2025. FinHealth Standards.

Web Access

15. Bartlett, R., Morse, A., Stanton, R. and Wallace, N., 2022. Consumer-lending

discrimination in the FinTech Era. Journal of Financial Economics, 143(1), pp.30-56. 
Web Access

16. Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T. and Walther, A., 2022. Predictably 
unequal? The effects of machine learning on credit markets. The Journal of Finance, 
77(1), pp.5-47. 
Web Access

17. Arráiz, I., Stucchi, R., Bruhn, M., 2015. Psychometrics as a tool to improve screening

and access to credit. World Bank Policy Research Working Paper 7506. 
Web Access

18. Sahay, R., Eriksson von Allmen, U., Lahreche, A., Khera, P., Ogawa, S., Bazarbash, M.

and Beaton, K., 2020. The Promise of Fintech: Financial Inclusion in the Post COVID-19 
Era. IMF Departmental Paper 20/009. 
Web Access

19. Dunn, A., Celik, N., Warren, A., Chege, W. - Financial Health Network, 2022. 2022 U.S.

Trends Report: Landmark changes in Americans’ financial health. 
Web Access

20. Duckworth, A.L., Peterson, C., Matthews, M.D. and Kelly, D.R., 2007. Grit:

perseverance and passion for long-term goals. Journal of Personality and Social 
Psychology, 92(6), p.1087. 
Web Access

21. Duckworth, A.L. and Quinn, P.D., 2009. Development and validation of the Short Grit

Scale (GRIT–S). Journal of Personality Assessment, 91(2), pp.166-174. 
Web Access

22. Duarte, J., Siegel, S. and Young, L., 2012. Trust and credit: The role of appearance in

peer-to-peer lending. The Review of Financial Studies, 25(8), pp.2455-2484. 
Web Access

23. Erel, I. and Liebersohn, J., 2022. Can FinTech reduce disparities in access to finance? 
Evidence from the Paycheck Protection Program. Journal of Financial Economics,

Financial Regulation Innovation Lab (FRIL) | 33

---

<!-- PAGE 40 -->

146(1), pp.90-118. 
Web Access

24. Gopal, M. and Schnabl, P., 2022. The rise of finance companies and fintech lenders in

small business lending. The Review of Financial Studies, 35(11), pp.4859-4901. 
Web Access

25. Irani, R.M., Iyer, R., Meisenzahl, R.R. and Peydro, J.L., 2021. The rise of shadow

banking: Evidence from capital regulation. The Review of Financial Studies, 34(5), 
pp.2181-2235. 
Web Access

26. Rossi, A.G. and Utkus, S., 2024. The diversification and welfare effects of robo-

advising. Journal of Financial Economics, 157, p.103869. 
Web Access

27. Cao, S., Jiang, W., Wang, J. and Yang, B., 2024. From man vs. machine to man+ 
machine: The art and AI of stock analyses. Journal of Financial Economics, 160, 
p.103910. 
Web Access

28. Sopra Steria, 2025. Digital Banking Experience Report (DBX) - Financial Well-Being as a

Key Differentiator in Banking. 
Web Access

29. Baird, G., Reed, J. - Farrer & Co., 2025. The advice-guidance boundary review: The

new targeted support regime. 
Web Access

30. OECD, 2023. Open Finance policy considerations, OECD Business and Finance Policy

Papers, OECD Publishing. 
Web Access

31. Lessar, S., Plant, S., Kiers, A., Rennie, C., Milner, H. - DLA Piper, 2023. The European

Commission’s proposal for Payment Services Directive 3 (PSD3). 
Web Access

32. Financial Conduct Authority (FCA), 2025. Open finance sprint: Outcomes report.

Web Access

33. The Business Research Company, 2025. Global Artificial Intelligence AI In Financial

Wellness Growth Drivers 2025, Forecast To 2034. 
Web Access

34. Standard Life, 2023. Standard Life partners with Moneyhub to integrate Open Finance

functionality. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 34

---

<!-- PAGE 41 -->

35. Ozone API, 2024. How Open Finance is revolutionising financial management for

young adults. 
Web Access

36. Moneyhub, 2025. Moneyhub extends partnership with Experian to help people pay

debt faster. 
Web Access

37. The Power 50, 2022. Moneyhub joins forces with Pennyworth to democratise

financial planning. 
Web Access

38. Standard Life, 2025. Finance for all the family: Standard Life launches digital coaching

platform to support key life moments. 
Web Access

39. Bank of England, 2024. Artificial intelligence in UK financial services - 2024.

Web Access

40. Delev, Z. - GDPR Local, 2024. The future of Finance: Adapting to AI and data privacy

laws. 
Web Access

41. Coinscrap Finance, 2025. Customer segmentation in banking: AI revolutionizes

clustering. 
Web Access

42. Open Banking Limited, 2023. From Open Banking to Open Finance and beyond.

Web Access

43. Morgan, K. - Plaid, 2022. Innovating in the UK's credit information market - how Open

Banking can help and why it matters. 
Web Access

44. Babina, T., Bahaj, S., Buchak, G., De Marco, F., Foulis, A., Gornall, W., Mazzola, F., Yu, 
T. - Bank of England, 2024. Customer data access and fintech entry: Early evidence 
from Open Banking. Staff Working Paper No. 1059 
Web Access

45. Financial Conduct Authority (FCA), 2025. Financial Lives Survey 2024: Credit and loans

– Selected findings. 
Web Access

46. Financial Conduct Authority (FCA), 2025. Mortgage lending statistics.

Web Access

47. Centre for Finance, Innovation and Technology (CFIT), 2024. Embracing the UK’s Open

Finance opportunity. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 35

---

<!-- PAGE 42 -->

48. Open Banking Limited. Open Finance.

Web Access

49. Cambridge Centre for Alternative Finance (CCAF), 2024. The global state of Open

Banking and Open Finance. Cambridge: Cambridge Centre for Alternative Finance, 
Cambridge Judge Business School, University of Cambridge. 
Web Access

50. Fariha, N., Khan, M. N. M., Hossain, M. I., Reza, S. A., Bortty, J. C., Sultana, K. S., Islam 
Jawad, M. S., Safat, S., Ahad, M. A. & Begum, M., 2025. Advanced fraud detection 
using machine learning models: enhancing financial transaction security. 
Web Access

51. Goulet Coulombe, P., Leroux, M., Stevanovic, D. and Surprenant, S., 2022. How is 
machine learning useful for macroeconomic forecasting?. Journal of Applied 
Econometrics, 37(5), pp.920-964. 
Web Access

52. Gu, S., Kelly, B. and Xiu, D., 2020. Empirical asset pricing via machine learning. The

Review of Financial Studies, 33(5), pp.2223-2273. 
Web Access

53. Lin Zi, Bukovski, K., Journey C., 2025. Smart Personalised Finance. MSc Dissertation in 
collaboration between Sopra Steria and University of Oxford’s Mathematical Institute 
(Mathematical and Computational Finance MSc).

54. Matellio, 2024. Customer segmentation analytics in banking: Unlocking Insights for

Enhanced Decision-Making. 
Web Access

55. Selvaraj, A., Sivathapandi, P., Namperumal, G., 2022. Privacy-Preserving Synthetic

Data Generation in Financial Services: Implementing Differential Privacy in AI-Driven 
Data Synthesis for Regulatory Compliance. Journal of Artificial Intelligence Research 
Vol. 2 No. 1. 
Web Access

56. Berry, M. L. - EM360Tech, 2025. Is Synthetic Data GDPR-Compliant? What Security

and Privacy Leaders Need to Know  
Web Access

57. Financial Conduct Authority (FCA), 2024. Using synthetic data in financial services.

The Synthetic Data Expert Group. 
Web Access

58. Financial Conduct Authority (FCA), 2023. Exploring synthetic data validation: Privacy,

utility and fidelity. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 36

---

<!-- PAGE 43 -->

59. Centre for Data Ethics and Innovation, 2021. Unlocking the value of data: Exploring

the role of data intermediaries.  
Web Access

60. Mirzoev, V. and Machado, M.R., 2025. The impact of synthetic data augmentation on

algorithmic bias in credit risk assessment. University of Twente. 
Web Access

61. Bailey, K. - Corporate Finance Institute. The ethics of AI in finance: How to detect and

prevent bias. 
Web Access

62. Bogiatzis-Gibbons, D., Charles, L., Dewing, H., Gretschel, C., Jomy, M., Reid, A., Slack, 
R. - Financial Conduct Authority (FCA), 2024. A literature review on bias in supervised 
machine learning. 
Web Access

63. Turner Lee, N., Resnick, P. and Barton, G. - Brookings, 2019. Algorithmic bias

detection and mitigation: Best practices and policies to reduce consumer harms. 
Web Access

64. Irons, A., Bukovski, K., 2024. Intelligent financial health evaluation. MSc Dissertation 
in collaboration between Sopra Steria and University of Oxford’s Mathematical 
Institute (Mathematical and Computational Finance MSc).

65. Department for Business and Trade (UK Government), 2024. The Smart Data

roadmap: Action the government is taking in 2024 to 2025. 
Web Access

66. Finexer, 2025. PSD3: All you need to know in 2025.

Web Access

67. Bentleys, 2025. How to improve cash flow: Best strategies for business success.

Web Access

68. Treelife, 2024. Cash Flow Optimization – Meaning, Techniques, Forecasting.

Web Access

69. HM Land Registry and Office for National Statistics (ONS), 2025. UK House Price

Index: May 2025 summary. 
Web Access

70. Office for National Statistics (ONS), 2025. Private rent and house prices, UK: July 2025.

Web Access

71. Tookitaki, 2025. Smarter Surveillance: How Machine Learning Is Transforming

Transaction Monitoring. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 37

---

<!-- PAGE 44 -->

72. Gresenz, C.R., Mitchell, J.M., Rodriguez, B., Turner, R.S. and Van der Klaauw, W., 
2025. The financial consequences of undiagnosed memory disorders. Journal of 
Financial Economics, 172, 104149. 
Web Access

73. Agarwal, S. and Muckley, C.B., 2025. Money management difficulty, customer 
protection and the detection of early-stage dementia. Michael J. Brennan Irish 
Finance Working Paper Series Research Paper, (24-4). 
Web Access

74. Hu, Q., Levine, R., Lin, C. and Tai, M., 2024. Credit Market Conditions and Mental

Health. Management Science, 71(3), pp.1967-1987. 
Web Access

75. Carlin, B., Umar, T. and Yi, H., 2023. Deputizing financial institutions to fight elder

abuse. Journal of Financial Economics, 149(3), pp.557-577. 
Web Access

76. de Souza Santos, R., Fronchetti, F., Freire, S. and Spinola, R., 2025. Software fairness 
debt: Building a research agenda for addressing bias in AI systems. ACM Transactions 
on Software Engineering and Methodology, 34(5), pp.1-21. 
Web Access

77. Das, A., Uddin, G., Chowdhury, S., Akhond, M.R. and Hemmati, H., 2025. Applications 
and Challenges of Fairness APIs in Machine Learning Software. ACM Transactions on 
Software Engineering and Methodology. 
Web Access

78. Chen, Z., Zhang, J.M., Hort, M., Harman, M. and Sarro, F., 2022. Fairness testing: A 
comprehensive survey and analysis of trends. ACM Transactions on Software 
Engineering and Methodology, 33(5), pp.1-59. 
Web Access

79. Conlon, T., Cotter, J. and Kynigakis, I., 2025. Asset allocation with factor-based

covariance matrices. European Journal of Operational Research, 325(1), pp.189-203. 
Web Access

80. Goulet Coulombe, P., Leroux, M., Stevanovic, D. and Surprenant, S., 2022. How is 
machine learning useful for macroeconomic forecasting?. Journal of Applied 
Econometrics, 37(5), pp.920-964. 
Web Access

81. Giglio, S., Kelly, B. and Xiu, D., 2022. Factor models, machine learning, and asset

pricing. Annual Review of Financial Economics, 14(1), pp.337-368. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 38

---

<!-- PAGE 45 -->

82. Duflo, E. and Banerjee, A., 2011. Poor economics (Vol. 619). New York: PublicAffairs.

& parts of chapters 6-9 (insurance, lending, saving and business for the poor, 
microcredit.) 
Web Access

83. Holistique Training, 2023. Optimising cash flow: Strategies For Financial Stability.

Web Access

84. KPMG. Cash flow forecasting and stabilisation.

Web Access

85. McBride, J. - Stewardship Wealth Advisors, 2021. The financial needs hierarchy.

Web Access

86. Carbonaro, C. - Ashton Thomas Private Wealth, 2024. How Maslow’s pyramid

intersects with the financial planning pyramid. 
Web Access

87. Chen, O., 2024. Maslow’s hierarchy of needs and money.

Web Access

88. Hamzat, L., 2025. Real-Time Financial Resilience and Debt Optimization for

Entrepreneurs: Tackling Debt Management as a Financial Health Pandemic and 
Empowering Small Business Growth Through Early Detection of Financial Distress and 
Effortless Capital Management. International Journal of Research Publication and 
Reviews, Vol 02, Issue 05, pp 202-223 
Web Access

89. Banerjee, A.V. and Duflo, E., 2019. Good economics for hard times. PublicAffairs.

Web Access

90. Kaur, J. - Akira AI, 2024. Financial Robo-Advisory: Harnessing Agentic AI.

Web Access

91. Kashyap, A., 2025. AI-driven financial advisory: The rise of robo-advisors.

Web Access

92. Beshears, J., Choi, J.J., Clayton, C., Harris, C., Laibson, D. and Madrian, B.C., 2025.

Optimal illiquidity. Journal of Financial Economics, 165, p.103996. 
Web Access

93. Gargano, A. and Rossi, A.G., 2024. Goal setting and saving in the fintech era. The

Journal of Finance, 79(3), pp.1931-1976. 
Web Access

94. Beshears, J., Choi, J.J., Laibson, D., Madrian, B.C. and Skimmyhorn, W.L., 2022.

Borrowing to save? The impact of automatic enrollment on debt. The Journal of 
Finance, 77(1), pp.403-447. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 39

---

<!-- PAGE 46 -->

95. Reiff, J., Dai, H., Beshears, J., Milkman, K.L. and Benartzi, S., 2023. Save more today or

tomorrow: the role of urgency in precommitment design. Journal of Marketing 
Research, 60(6), pp.1095-1113. 
Web Access

96. Benartzi, S., Beshears, J., Milkman, K.L., Sunstein, C.R., Thaler, R.H., Shankar, M.,

Tucker-Ray, W., Congdon, W.J. and Galing, S., 2017. Should governments invest more 
in nudging?. Psychological Science, 28(8), pp.1041-1055. 
Web Access

97. Beshears, J., Dai, H., Milkman, K.L. and Benartzi, S., 2021. Using fresh starts to nudge

increased retirement savings. Organizational Behavior and Human Decision 
Processes, 167, pp.72-87. 
Web Access

98. Beshears, J. and Kosowsky, H., 2020. Nudging: Progress to date and future directions.

Organizational behavior and human decision processes, 161, pp.3-19. 
Web Access

99. Bank of England, 2023. Financial Stability in Focus: The FPC’s approach to assessing

risks in market-based finance. 
Web Access

Financial Regulation Innovation Lab (FRIL) | 40

---

<!-- PAGE 47 -->

About the Authors

Kal  Bukovski  is  Consulting  Senior  Manager  and  Director  of  Academia  & 
Research  at  Sopra  Steria.  He  specialises  in  the  financial  services  domain, 
driving transformative projects and data-driven excellence. With expertise in 
analytics,  data  science,  business  intelligence  and  data  visualisation,  he 
supports clients in making strategic decisions and gaining a competitive edge 
in  this  dynamic,  regulated  domain.  Kal 
leads  business  projects  and 
collaborations  with  Academia,  fostering  innovation,  compliance  and  data-
driven  storytelling.  His  main  areas  of  expertise  are  regulatory  modelling,  credit  risk,  consumers’ 
financial health, scorecards, pricing and others, enhancing risk management and customer experience 
for sustained success.

interests

Dr Kushagra Jain is a Research Associate at the Financial Regulation Innovation Lab 
(FRIL),  Strathclyde  Business  School.  His  research 
include  artificial 
intelligence,  machine  learning,  financial/regulatory  technology,  textual  analysis, 
international  finance  and  risk  management,  among  others.  He  is  a  recipient  of 
doctoral  scholarships  from  the  Financial  Mathematics  and  Computation  Cluster 
(FMCC),  Science  Foundation  Ireland  (SFI),  Higher  Education  Authority  (HEA)  and 
Michael  Smurfit  Graduate  Business  School,  University  College  Dublin  (UCD). 
Previously, he worked within wealth management and as a statutory auditor. He is 
due to complete his doctoral studies in Finance from UCD in 2023, and obtained his MSc in Finance 
from UCD, his Accounting Technician accreditation from the Institute of Chartered Accountants of India 
and his undergraduate degree from Bangalore University. He is a FMCC Database Management Group 
Data  Manager,  Research  Assistant,  PhD  Representative  and  Teaching  Assistant  for  undergraduate, 
graduate and MBA programmes.

Professor  Mark  Cummins  is  Professor  of  Financial  Technology  at  the 
Strathclyde  Business  School,  University  of  Strathclyde,  where  he  leads  the 
FinTech  Cluster  as  part  of  the  university’s  Technology  and  Innovation  Zone 
leadership and connection into the Glasgow City Innovation District. As part of 
this role, he is driving collaboration between the FinTech Cluster and the other 
strategic clusters identified by the University of Strathclyde, in particular the 
Space, Quantum and Industrial Informatics Clusters. Professor Cummins is the 
lead investigator at the University of Strathclyde on the newly funded (via UK 
Government and Glasgow City Council) Financial Regulation Innovation Lab initiative, a novel industry 
project under the leadership of FinTech Scotland and in collaboration with the University of Glasgow. 
He previously held the posts of Professor of Finance at the Dublin City University (DCU) Business School 
and Director of the Irish Institute of Digital Business. Professor Cummins has research interests in the 
following areas: financial technology (FinTech), with particular interest in Explainable AI and Generative 
AI; quantitative finance; energy and commodity finance; sustainable finance; model risk management. 
Professor Cummins has over 50 publication outputs. He has published in leading international discipline 
journals such  as: European  Journal of Operational Research;  Journal of Money, Credit and Banking; 
Journal  of  Banking  and  Finance;  Journal  of  Financial  Markets;  Journal  of  Empirical  Finance;  and 
International Review of Financial Analysis. Professor Cummins is co-editor of the open access Palgrave 
title  Disrupting Finance:  Fintech and Strategy in the 21st Century.  He  is  also co-author of the Wiley 
Finance  title  Handbook  of  Multi-Commodity  Markets  and  Products:  Structuring,  Trading  and  Risk 
Management.

Financial Regulation Innovation Lab (FRIL) | 41

---

<!-- PAGE 48 -->

Dr James Bowden is Senior Lecturer in Financial Technology at Strathclyde Business 
School, University of Strathclyde, where he is the programme director of the MSc 
Financial  Technology. Prior to this, he gained experience  as  a Knowledge Transfer 
Partnership (KTP) Associate at Bangor Business School, and he has previous industry 
experience  within  the  global  financial  index  team  at  FTSE  Russell.  Dr  Bowden’s 
research  focusses  on  different  areas  of  financial  technology  (FinTech),  and  his 
published  work  involves  the  application  of  text  analysis  algorithms  to  financial 
disclosures, news reporting, and social media. More recently he has been working on 
projects incorporating audio analysis into existing financial text analysis models and investigating the 
use cases of satellite imagery for the purpose of corporate environmental monitoring. Dr Bowden has 
published in respected international journals, such as the European Journal of Finance, the Journal of 
Comparative Economics, and the Journal of International Financial Markets, Institutions and Money. 
He has also contributed chapters to books including “Disruptive Technology in Banking and Finance”, 
published by Palgrave Macmillan. His commentary on financial events has previously been published in 
The  Conversation  UK,  the  World  Economic  Forum,  MarketWatch  and  Business  Insider,  and  he  has 
appeared  on  international  TV  stations  to  discuss  financial  innovations  such  as  non-fungible  tokens 
(NFTs).

Dr  Godsway  Korku  Tetteh  is  a  Knowledge  Exchange  Associate  at  the  Fraser  of 
Allander  Institute  where  he  conducts  economic  evaluation  of  public  sector 
programmes  and  projects.  Previously,  he  worked  for  the  Financial  Regulation 
Innovation Lab as a Research Associate at the University of Strathclyde. His research 
explores the impact of digital technologies and financial innovation (FinTech) on 
welfare  and  private  sector  development.  In  addition  to  research,  he  has  active 
engagement with the policy community. He worked with the Cambridge Centre for Alternative Finance 
to build the capacity of regulators and policymakers from across the globe in FinTech and regulatory 
innovation. He shares his research insights with international development organisations. Godsway has 
recently served as a panellist during the 3rd International Conference for Alternative Finance Research 
to  discuss  alternative  finance  and  financial  inclusion.  He  has  a  Ph.D.  in  Economics  from  Maastricht 
University  and  published  in  reputable  journals  such  as  Small  Business  Economics  and  World 
Development.

Jackie  (Zi  Khang)  Lin  holds  an  MSc  in  Mathematical  and  Computational  Finance 
from  the  University  of  Oxford,  graduating  with  Distinction  in  2025.  For  his 
dissertation,  he  developed  a  proof-of-concept  data  pipeline  that  processes  raw, 
granular  datasets  and  applies  Bayesian  imputation  to  infer  demographic  labels, 
followed  by  clustering  techniques  to  identify  distinct  customer  groups  for 
personalised financial insights. Before his MSc, Jackie earned a BA in Mathematics 
from the University of Cambridge. He brings five years of experience in the asset 
management industry, having served as a fixed income reserves portfolio manager at the Central Bank 
of Malaysia. He is also a CFA charter holder. Jackie is currently working at a hedge fund in London.

Financial Regulation Innovation Lab (FRIL) | 42

---

<!-- PAGE 49 -->

Get in touch

FRIL@FinTechScotland.com

Financial Regulation Innovation Lab (FRIL) | 43

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ISSN: 3033-4136
  DOI:  https://doi.org/10.17868/strath.00094718
|       |         |                  |          |
| ----- | ------- | ---------------- | -------- |
| From  | Crisis  | to  Prosperity:  | AI  and  |
<  >
Open Finance for Holistic Financial
Health and Smart Future Planning
FRIL
Financial Regulation Innovation Lab
University
FinTech  Universityof
l  -
Strathclyde
|            |     | efGlasgow  | •   |
| ---------- | --- | ---------- | --- |
| Scotland®  |     | ~          |     |
Glasgow
 in collaboration with
1

From Crisis to Prosperity: AI and Open Finance for
Holistic Financial Health and Smart Future Planning
Kal Bukovski, Consulting Senior Manager and Director of Academia & Research, Sopra Steria,
Orchard Brae House, 30 Queensferry Road, Edinburgh EH4 2HS
Dr Kushagra Jain, Professor Mark Cummins, Dr James Bowden, Dr Godsway Korku Tetteh.
Strathclyde Business School, University of Strathclyde, and Financial Regulation Innovation
Lab, 199 Cathedral Street, Glasgow, G4 0QU, UK
Zi Khang, MSc student in Mathematical and Computational Finance 2024-2025 – University of
Oxford’s Mathematical Institute, Wellington Square, Oxford OX1 2JD
12 November 2025
We acknowledge funding from Innovate UK, award number 10055559.
Corresponding authors:
Email: kal.bukovski@soprasteria.com
Email: kushagra.jain@strath.ac.uk
Email: mark.cummins@strath.ac.uk
Email: james.bowden@strath.ac.uk
Email: godsway.tetteh@strath.ac.uk

Financial Regulation Innovation Lab
Who are we?
The Financial Regulation Innovation Lab (FRIL) is an industry-led collaborative research and
innovation programme focused on leveraging new technologies to respond to, shape, and help
evolve the future regulatory landscape in the UK and globally, helping to create new
employment and business opportunities, and enabling the future talent.
FRIL provides an environment for participants to engage and collaborate on the dynamic
demands of financial regulation, explore, test and experiment with new technologies, build
confidence in solutions and demonstrate their ability to meet regulatory standards worldwide.
What is Actionable Research?
FRIL will integrate academic research with an industry relevant agenda, focused on enabling
knowledge on cutting-edge topics such as generative and explainable AI, advanced analytics,
advanced computing, and earth-intelligent data as applied to financial regulation. The
approach fosters cross sector learning to produce a series of papers, actionable
recommendations and strategic plans that can be tested in the innovation environment, in
collaboration across industry and regulators.
Locally-led Innovation Accelerators delivered in
partnership with DSIT, Innovate UK and City Regions
Innovate
Department for GLASGOW
Science, Innovation UK CITY REGION
& Technology

FRIL White Paper Series
From Crisis to Prosperity: AI and Open Finance for
Holistic Financial Health and Smart Future Planning
Kal Bukovski* Kushagra Jain** Mark Cummins**
James Bowden** Godsway Korku Tetteh** Zi Lin***
* Sopra Steria ** University of Strathclyde ***University of Oxford
12 November 2025
Executive Summary
The financial services industry stands at a critical inflection point. Traditional credit-score-
centric frameworks, rooted in historical repayment data and broad demographic categories,
are increasingly incapable of capturing the full spectrum of consumers’ financial health. The
COVID-19 pandemic, successive cost-of-living crises and wider economic shocks have exposed
deep vulnerabilities in reactive, one-dimensional risk models. Consumers and institutions
require proactive, resilience-focused insights that span day-to-day cashflow management,
medium-term debt servicing, and long-term wealth accumulation.
Open Finance - the consent-driven sharing of a comprehensive array of financial data (current
accounts, mortgages, loans, savings, investments, pensions, insurance, government benefits),
combined with advanced Artificial Intelligence (AI) and Machine Learning (ML) techniques,
offers a transformational route to truly holistic financial health evaluation. By ingesting rich,
multi-dimensional data and applying explainable models, financial firms can transition from
static credit assessments to dynamic, personalised guidance and recommendation engines.
These engines empower consumers to build financial resilience, make informed decisions and
pursue life goals with confidence.
Building on Sopra Steria and Glasgow University’s joint whitepaper “Consumers at the Heart of
Innovation: Financial Health Evaluation in the UK Regulatory Landscape” and inspired by R&D
collaboration between Sopra Steria and Oxford University, this whitepaper:
▪ Examines the scope and expected data architecture of Open Finance, extending from
Open Banking to full-spectrum data sharing.
▪ Presents a robust data modelling framework, encompassing data acquisition,
cleansing, feature engineering, supervised and unsupervised modelling, scorecard
design and persona segmentation. It culminates in a composite financial health score
that blends aspects like credit risk and resilience evaluation.

▪ Explores explainability and consumer engagement, employing data science
techniques to ensure transparency and mapping various persona archetypes to
tailored, sequential optimisation plans.
▪ Demonstrates regulatory alignment, showing how non-product-specific, persona-
driven guidance and recommendation can fit within the Financial Conduct Authority’s
(FCA) Advice and Guidance Boundary (FG15/1) and the Consumer Duty framework.

Table of Contents
1. Introduction .......................................................................................................................... 1
1.1 Context & motivation - shifting financial landscape ......................................................... 1
1.2 Problem statement .......................................................................................................... 2
1.3 From Open Banking to Open Finance............................................................................... 3
1.4 Defining financial health and resilience ........................................................................... 4
1.5. Industry & Regulatory perspectives ................................................................................ 6
2. Open Finance: Data integration and customer segmentation ............................................ 9
2.1 The Open Finance data revolution ................................................................................... 9
2.2 Data structures ............................................................................................................... 11
2.4 Advanced customer segmentation through AI-driven analytics .................................... 13
2.5 Privacy-preserving data enhancement ........................................................................... 14
2.6 Regulatory compliance and ethical considerations ........................................................ 15
2.7 Beyond Open Finance: inclusion, smart data and cross-border portability ................... 16
3. Predictive analytics & cash flow modelling ........................................................................ 17
3.1 Comprehensive data sourcing ........................................................................................ 17
3.2 Dynamic risk assessment and behavioural prediction ................................................... 19
3.3 Feature selection & engineering .................................................................................... 20
3.4 Predictive modelling & clustering .................................................................................. 20
3.5 Model explainability vs performance ............................................................................. 22
3.6 Stochastic modelling and scenario analysis .................................................................... 22
3.7 Adaptation and continuous learning .............................................................................. 24
4. Smart Personalised Finance Management Framework ..................................................... 25
4.1 Hierarchical financial needs framework ......................................................................... 25
4.2 Sequential optimisation engine architecture ................................................................. 26
4.3 Personalisation and behavioural integration ................................................................. 27
4.4 Continuous improvement and outcome tracking .......................................................... 29
5. Conclusion ........................................................................................................................... 31
6. References: ......................................................................................................................... 32
About the Authors .................................................................................................................... 41

1. Introduction
1.1 Context & motivation - shifting financial landscape
Over the past decade, digital transformation, fintech innovation and economic volatility have
radically changed consumers’ financial lives. Typically, traditional credit-scoring frameworks are
heavily reliant on repayment histories and demographic proxies. These can therefore often fail
to reflect complex, dynamic realities such as fluctuating gig-economy incomes, irregular self-
employment cashflows or sudden macroeconomic shocks. The COVID-19 pandemic exposed
the fragility of many households, while the following cost-of-living crises have underscored the
imperative for financial resilience – more specifically, the ability to absorb income shocks,
maintain essential spending and avoid harmful debt spirals.
The financial sector’s balance sheets as a proportion of GDP, and share in economy value
added, have been rising in many economies. From the resulting financial depth, such
“financialisation” can boost growth and productivity, especially in developing countries.
However, too much of a good thing can be a concern: financial intermediation costs continue
to rise, calling into question the industry’s efficiency. The relationship between financial depth
and productivity and growth is possibly U-shaped. Thus, it is pivotal to acknowledge these
factors and to question the financial system’s contribution to economy and society [1].
More contemporary evidence casts further scrutiny upon finance’s societal value. Sentiment
positivity from a huge corpus of finance literature (captured, for example, in multiple languages
and over multiple decades) has been shown to be positively correlated with financial market
participation and negatively with income inequality [2],[3]. The former is represented by equity
percentage of total assets for households (from the Organisation for Economic Co-operation
and Development – OECD), total loans to households and non-financial private sector, as
percentages of GDP. The latter is measured with national accounts data using the Gini
coefficient, reported by the World Income Inequality Database.
In light of the above, global and UK concerns surrounding the role of such income and wealth
inequality and concentration merit acknowledgement and consideration, alongside alternate
solutions such as better corporate and wealth taxation. Specifically, from macroeconomic data
in [4], researchers investigate substantial profit reductions for nations from profit shifting
strategies of multinational companies to tax havens.
At the same time, rising consumer expectations demand proactive support. Rather than simply
deciding on creditworthiness, households seek insights into essential buffer levels, optimal
debt-repayment strategies, saving trajectories for medium- and long-term goals
(homeownership, education, retirement) and timely nudges when life events (job loss, family
expansion, rate resets) threaten financial stability.
Financial Regulation Innovation Lab (FRIL) | 1

1.2 Problem statement
This whitepaper addresses the urgent challenge of improving holistic financial health and
resilience in an increasingly complex and shifting financial landscape. While traditional financial
guidance often focuses narrowly on creditworthiness or savings, many consumers still struggle
to manage everyday finances, absorb shocks and plan effectively for their futures [5],[6]. Our
work situates financial health as a multi-dimensional concept, integrating spending, saving,
borrowing and financial planning, with resilience as a cross-cutting capability that supports
wellbeing through life’s uncertainties.
This approach aligns closely with the FCA’s Advice Guidance Boundary Review (AGBR), which
explores new regulatory frameworks to better support consumers in making financial decisions
[7]. The AGBR focuses on bridging the gap between generic guidance and full advice by
introducing “targeted support” (see Figure 1) – tailored suggestions developed for groups of
consumers with similar circumstances, designed to improve access to timely and affordable
financial help. This emerging model aims to empower more people to navigate pensions and
investments with confidence, addressing the persistent “advice gap” where only around 8% of
UK adults currently receive financial advice [8].
Ideally, such targeted support ought to be provided at a minimal cost to vulnerable parties.
Fairness should be considered for delivery of targeted support to ensure maximal efficacy. For
instance, AI’s potential in improving learning outcomes and promoting diversity, equity, and
inclusion should be considered [9]. Further, blended human-AI delivery behoves consideration
especially for complex problems in the context of targeted support, as research indicates hybrid
human-AI interaction yields better performance in interactive reasoning tasks, driven by the
latter’s correct reasoning [10].
Financial Regulation Innovation Lab (FRIL) | 2

A suite of consumer support options
Personal recommendation boundary
J,
~
.Q...I
:::l  C:
....  0
:.:; :.:;
| INFORMATION/  | VI   I O  |     |     |     |     | HOLISTIC ADVICE  |
| ------------- | --------- | --- | --- | --- | --- | ---------------- |
C :   " O
| GUIDANCE  | .u 0      C :   |     |     |     |     |                      |
| --------- | --------------- | --- | --- | --- | --- | -------------------- |
|           | ... Q I         |     |     |     |     | A recommendation of  |
E
| Factual information  | 0   E  |     |     |     |     | a particular product  |
| -------------------- | ------ | --- | --- | --- | --- | --------------------- |
C:
a n d /o r  g e n e ri c   VI   0   o r  c o u r s e   o f  a c ti o n
Q I  u
gu i d an c e  t o  h e l p  a  0   . Q.. I    ass e s s e d   a s  s u i ta b l e  f or
~
|                      | "..O..   iii  |     |                    |     |     | a consumer's overall  |
| -------------------- | ------------- | --- | ------------------ | --- | --- | --------------------- |
| consumer understand  |               |     | SIMPLIFIED ADVICE  |     |     |                       |
..cI O .:.     C :
| their options but  | . . 0..     |     |     |     |     | financial situation  |
| ------------------ | ----------- | --- | --- | --- | --- | -------------------- |
VI
| without providing  | Q I   |     |     |     |     | taking account of  |
| ------------------ | ----- | --- | --- | --- | --- | ------------------ |
·su :    Q I  A recommendation ofa  particular product or
| a view of what the  | Q,       |                  |                       |                          |                     | comprehensive      |
| ------------------- | -------- | ---------------- | --------------------- | ------------------------ | ------------------- | ------------------ |
|                     | "O   IO  | e o u r H        | o f a c t lo n  a . . | . . . . .t  u s u lt a b | l e f o r a n       |                    |
| consumer should do  | < (      |                  |                       |                          |                     | information about  |
|                     |          | lnc l lv ld u al |  c o n s u m e r  t a | k i n g  a c c ou n t    | o f e u e n t l al  |                    |
their needs and
Information relevant to• single nHd
circumstances

Figure 1: Consumer Support Options. Source: The FCA's plans to bridge the advice gap - The Lang Cat
Our Smart Personalised Finance Management Framework presents a tangible and actionable
methodology to tackle this. By integrating Open Finance data, AI and data-driven predictive
analytics and behavioural insights, our framework can help drive personalised, scalable support
consistent with the AGBR’s targeted support approach. This can enable firms and innovators to
provide meaningful, timely financial guidance that helps consumers improve their financial
health and resilience sustainably.
1.3 From Open Banking to Open Finance
The EU’s Payment Services Directive 2 (PSD2) and the UK’s Competition and Markets Authority
(CMA) Open Banking mandate required banks to expose payment-account data and payment-
initiation services via secure Application Programming Interfaces (APIs). Open Banking proved
a  powerful  opportunity:  fintech  apps  now  offer  budgeting,  expense  categorisation  and
streamlined credit applications. Yet its scope is limited to current accounts and payment flows,
leaving mortgages, savings, pensions, investments and insurance data aside.
It is worth noting data breaches and risks on privacy, fraud and exploitation fronts exist from a
risk perspective: we address these in more depth later in the paper. Another concern is bias or
misuse of such data. This in turn can result in vulnerable consumer exploitation due to conflicts
of interest in the use of such data, depending on who is providing targeted support and can
arise in both human and AI support. For example, contemporary analysis on hotel pricing
algorithms showcases price setting frictions due to adjustment costs of human decision
makers, which induce a conflict of interest with the algorithmic advisor. Such costly price
adjustments lead to suboptimal pricing by human decision makers and the losses from this
strategic bias can be avoided with a full shift to automated algorithmic pricing [11].
Financial Regulation Innovation Lab (FRIL) | 3

Open Finance extends the API-driven paradigm to a full spectrum of financial products (see
Figure 2). Under customer consent, it enables:
• Credit products: mortgages, personal loans, credit cards.
• Savings & investments: deposit accounts, ISAs.
• Pensions & retirement products: Defined Contribution (DC) pot valuations, contribution
histories.
• Insurance policies: life, home, auto; coverage, premiums, claims history.
• Government benefits & incentives: Universal Credit, Child Benefit, pension credit.
This richer dataset allows a truly holistic view of financial health and underpins advanced AI-
driven guidance engines.
BNPL
~ Fo='oJ
ld
GMortgage
Au.to Loal'\
% HELOC
CheckiJ'\9
1=---~1
Figure 2: Open Finance as an extension of Open Banking. Source: How to Survive Open Banking - Fintech Takes
1.4 Defining financial health and resilience
In our work, financial health is considered not merely as credit worthiness but as a multi-
dimensional construct combining ability to meet day-to-day obligations, capacity to absorb
shocks, and readiness for future goals. The FCA, in its 2021 guidance, identifies four primary
drivers of vulnerability: low financial resilience, poor health, recent negative life events and low
capability. Of these, low financial resilience (the inability to hold out against unexpected
expenses without falling into difficulty) was the most common, affecting approximately one
quarter of UK adults in 2022 (12.9 million people) [12].
Financial Regulation Innovation Lab (FRIL) | 4

Financial health encompasses four pillars [13], [14]:
| Pillar  | Descriptor  |     | Example Financial Products  |     |
| ------- | ----------- | --- | --------------------------- | --- |
Covering essential needs without  Current accounts, credit cards, store
Spend
|     | overextending.  |     | cards   |     |
| --- | --------------- | --- | ------- | --- |
Building buffers for planned and  Savings and investment accounts,
Save
|     | unplanned events.  |     | ISA  |     |
| --- | ------------------ | --- | ---- | --- |
Accessing and managing credit  Credit cards, short term loans, car
Borrow
|     | sustainably.  |     | finance and more  |     |
| --- | ------------- | --- | ----------------- | --- |
Plan  Setting and pursuing financial goals.  Insurance, retirement products

Financial health is not just about having a good credit score or being able to pay the bills –
instead, it is about balancing everyday spending, saving for a rainy day, borrowing sensibly, and
planning ahead for the future. At the heart of all these elements lies financial resilience – the
capacity to cope when circumstances change unexpectedly.
|     | 1            | 3                | 5                | 7                 |
| --- | ------------ | ---------------- | ---------------- | ----------------- |
|     | Spend less   | Have sufficient  | Have manageable  | Have appropriate  |
|     | than income  | liquid savings   | debt             | insurance         |
|     | 2            | 4                | 6                | 8                 |
|     | Pay bills    | Confident will   | Have a prime     | Plan ahead        |
|     | on time      | meet long-term   | credit score     | financially       |
financial goals

Figure 3: Main pillars of Financial Health. Source: What is Financial Health? – Financial Health Network
Financial resilience is the thread running through each pillar of financial health. Being able to
spend wisely relies on having reserves to fall back on in an emergency. Saving and borrowing
work best when people can manage cashflow and debt without resorting to costly credit. And
effective financial planning depends on being prepared for both personal and economic
uncertainties.
Regulators like the FCA increasingly highlight resilience as a key factor in financial vulnerability.
It is not just about having financial wellbeing at a single point in time but also about sustaining
that wellbeing in the face of change – whether that is an unexpected expense, income
fluctuation or larger economic shifts.

Financial Regulation Innovation Lab (FRIL) | 5

Examples of key resilience metrics can be illustrated with the following:
• Buffer ratios: liquid assets (current + savings) divided by essential monthly outflows.
• Cashflow volatility: the rolling standard deviation of net inflows over recent periods.
• Debt-service coverage: ratio of income to scheduled debt payments under stress
scenarios.
• Days-to-buffer-breach: estimated number of days before liquid assets fall below the
minimum required buffer threshold.
Integrating financial resilience into the holistic assessment of financial health provides a more
dynamic and practical framework. It ensures that interventions and innovations in finance
support people, not only in maintaining financial wellbeing today, but also in adapting and
prospering for the future.
As holistic financial data becomes central to improving financial health and resilience, it is
crucial to use such data ethically and avoid bias [15],[16]. The aim must be to support
individuals, not to allow firms to benefit at their expense.
1.5. Industry & Regulatory perspectives
Studies on Alternative Credit Scoring and Financial Resilience
Global institutions like the World Bank and the International Monetary Fund (IMF) have
highlighted the potential of alternative credit scoring methods that go beyond traditional credit
histories. These approaches often incorporate behavioural indicators, psychometrics and non-
financial data to evaluate creditworthiness more holistically and inclusively, especially for
underserved populations. For example, the World Bank’s Entrepreneurial Finance Lab
developed psychometric credit scoring [17] to better assess small business owners in emerging
markets, improving access without raising default risk. The IMF has further explored how ML
and alternative data enhance risk assessment, supporting fairer credit access [18]. Parallel to
credit scoring innovation, frameworks focused on financial resilience have emerged – such as
the Financial Health Network’s model that measures individuals’ capacity to absorb shocks and
manage financial wellbeing over time, moving beyond simple balance sheet assessments [19].
Individual differences that predict success and achievement in all professional domains may
offer another approach to alternative credit scoring and determining financial resilience. For
example, grit, defined as perseverance and passion for long-term goals, has been shown to
account for an average of 4% of the variance in success outcomes, and is highly correlated with
conscientiousness. It supports the idea that achievement of difficult goals entails the sustained
and focused application of talent over time [20]. This Grit scale measurement can be achieved
via Short Grit Scale (Grit–S) [21], an improved version of the original.
Financial Regulation Innovation Lab (FRIL) | 6

It is important to acknowledge the impact of financial technology, through channels such as
peer-to-peer lending and “shadow banks”. For instance, research shows that due to the trust-
intensive nature of peer-to-peer lending, borrowers that appear to be more trustworthy have
higher probabilities of having loans funded [22]. Indeed, such borrowers are likely to have
better credit scores as well. Overall, impressions of trustworthiness matter in financial
transactions as they predict the investor’s, as well as the borrower’s, behaviour. Likewise, a
study on the supply of financial services to small businesses found FinTech is disproportionately
used in ZIP codes with fewer bank branches, lower incomes and more minority households,
and in industries with fewer banking relationships [23]. Further, its use was also greater in
counties where the economic effects of the COVID-19 pandemic were more severe and
financial services expanded.
FinTech lenders are major suppliers of credit to small businesses and played an important role
in the recovery from the 2008 financial crisis. Furthermore, some argue that reduced bank
lending did not have substantial effect on employment, wages and new business creation by
2016, due to its substitution by FinTech lenders [24].
Finally, researchers explore connections between bank capital regulation and the prevalence
of lightly regulated, often technology-enabled, nonbanks (i.e. shadow banks) in the U.S.
corporate loan market. It is found that at times when capital is scarce, such shadow banks step
in and provide credit or funding for loans with higher capital requirements, which are offloaded
by less-capitalised banks subject to Basel III requirements [25].
Regulations and Policy Making
Consumer protection remains a cornerstone of regulatory efforts as financial data sharing and
AI-based advisory tools expand [26], [27]. Sopra Steria’s recent research emphasises the
importance of safeguarding consumer interests in this evolving landscape, highlighting
transparency, fairness and data privacy as key enablers of trust [28]. Furthermore, the FCA
(through its AGBR) is actively redefining how financial support is delivered. The AGBR focuses
on innovative regulatory frameworks that enable “targeted support”, offering tailored
guidance to groups with shared characteristics, bridging the gap between generic guidance and
full advice and thus, improving access and outcomes [7], [29]. On the international stage, the
Organisation for Economic Co-operation and Development (OECD) advocates advancing
financial literacy and inclusion through integrated technology and policy approaches,
empowering consumers globally [30]. Meanwhile, Open Finance initiatives, potentially
accelerated by the forthcoming Payment Services Directive 3 (PSD3) in Europe, seek to
standardise and broaden data sharing while embedding strong consumer rights protections
[31].
Financial Regulation Innovation Lab (FRIL) | 7

Industry Perspectives
Industry stakeholders recognise the transformative power of Open Finance for personalised
financial wellness. Market reports observe a rising trend in dynamic, AI-driven financial
planning tools, delivering real-time insights and tailored recommendations [32], [33]. Firms like
Cleo and MoneyHub demonstrate this shift by integrating Open Finance data with ML to
enhance budgeting, debt management and forward-looking planning for consumers [34], [35].
MoneyHub’s recent expansions (e.g. partnering with Experian to accelerate debt repayment
[36] and with Pennyworth to democratise financial planning [37]) showcase practical
deployments of personalised financial management at scale. Additionally, AI-driven digital
platforms are increasingly engaging consumers who live paycheck to paycheck, offering
support customised to their needs [38]. Such initiatives, embedding Open Finance capabilities,
demonstrate clear industry momentum toward closing the financial wellness gap and
promoting resilience.
Contrasting Viewpoints
Despite these advances, persistent concerns exist around data privacy, algorithmic bias, and
consumer trust [39]. The aggregation of personal financial data raises risks of misuse and
unintended discrimination unless managed through ethical AI frameworks and transparent
governance [40]. Consumer scepticism toward data sharing further challenges adoption,
underscoring the need for clear communication and robust protections to build confidence in
emerging financial tools.
Financial Regulation Innovation Lab (FRIL) | 8

2. Open Finance: Data integration and customer
segmentation
The transition from traditional banking to Open Finance represents one of the most significant
paradigm shifts in the financial services industry [12]. This evolution moves far beyond the
foundational concepts of Open Banking to encompass a comprehensive ecosystem that
integrates diverse financial data sources including mortgages, insurance, investments,
pensions and government incentives into a unified analytical framework.
2.1 The Open Finance data revolution
Open Finance fundamentally transforms how financial institutions access and utilise customer
data. Traditional banking systems operated in silos, with each institution maintaining isolated
datasets that provided only fragmented views of customer financial health. The Open Finance
framework will break down these barriers through consent-based APIs and trusted third-party
frameworks, enabling the creation of comprehensive financial profiles that span multiple
institutions and product categories [41].
The scope of data available through Open Finance extends significantly beyond transactional
information. Modern implementations can capture income patterns, expenditure categories,
debt obligations across multiple products, savings behaviours, pension contributions,
insurance coverage details and participation in government financial incentives such as
Individual Savings Accounts (ISAs). This rich data environment can also incorporate event-
driven disclosures that capture life-changing events, dependency changes and employment
transitions that significantly impact financial circumstances [42].
Category Examples / Data Types
Credit Products Mortgages: outstanding balances, amortisation schedules,
rate resets.
Personal loans & credit cards: credit limits, utilisation,
minimum payments.
Savings & Investments Deposit accounts & ISAs: balances, interest rates,
contribution histories.
Brokerage accounts: holdings, asset valuations, transaction
histories.
Pensions & Retirement Defined-contribution pots, contribution rates, projected
retirement income.
Insurance Policy details, coverage limits, premium schedules, claims
records.
Government Benefits & Universal Credit, Child Benefit, Pension Credit, ISA
Incentives allowances, tax relief data.
Financial Regulation Innovation Lab (FRIL) | 9

Credit Products
Open Finance is reshaping access to credit information by enabling lenders to supplement
traditional bureau data with live account-level insights [43]. The democratisation of data is
lowering entry barriers for fintechs, encouraging competition and innovation in consumer
lending [44]. At the same time, consumers’ credit product usage is diversifying, with many
households managing a mix of mortgages, loans and revolving credit [45].
▪ Mortgages: Data on outstanding balances, amortisation schedules and rate resets is
gathered via the FCA’s Mortgage Lending and Administration Return (MLAR), submitted
quarterly by mortgage lenders in the UK [46]. Such integration supports both lenders and
regulators in monitoring repayment risks and borrower resilience.
▪ Personal Loans & Credit Cards: Open Banking is already deployed to improve lending
decisions by giving providers real-time access to loan affordability, credit limits, utilisation
and minimum repayment histories. This dynamic visibility allows for more accurate credit
risk profiling and prevents overextension.
Savings & Investments
Open Finance expands beyond transactional accounts into the broader realm of wealth and
asset management [42],[47].
▪ Deposit Accounts & ISAs: Access to balances, accrued interest, and contribution histories
provides a dynamic view of liquidity and savings capacity.
▪ Brokerage Accounts: With Open Finance frameworks, historical data on investment
holdings and valuations can be made portable across platforms, enhancing consumer
choice and advisory services.
Pensions & Retirement
Pensions are among the most significant assets for many households, yet they are traditionally
fragmented and opaque. For example, as an individual’s employment changes, their pension
providers may do as well. For an individual, these changes can be unclear and difficult to track.
Structured access to defined-contribution pots and retirement income projections is
highlighted in [47], [48]. This shift would allow individuals to view contribution rates,
investment performance and projected retirement income in one place, significantly
improving retirement planning.
Insurance
Insurance data remains at an early stage in the Open Finance journey. Future phases outlined
by the OBIE envision access to policy details, coverage limits, premium schedules, claims
records and others [42]. Incorporating such datasets into financial health models can allow
consumers to understand their protection gaps, while enabling insurers to personalise
offerings based on holistic financial profiles.
Financial Regulation Innovation Lab (FRIL) | 10

Government Benefits & Incentives
A forward-looking extension of Open Finance lies in the integration of government benefits
and tax-related incentives. Universal Credit, Child Benefit, Pension Credit, ISA allowances and
tax reliefs all play a material role in financial wellbeing. Incorporating such data into Open
Finance ecosystems would give households comprehensive visibility of their entitlements and
improve the ability of financial advisors and digital tools to deliver tailored guidance [47].
2.2 Data structures
The technical infrastructure supporting Open Finance relies on standardised data schemas and
temporal structuring1 approaches [32],[49]. Account-customer relationships are mapped
through sophisticated data models that maintain event timeline tagging and spending
categorisation systems. These structures enable both time-series analysis and static attribute
analysis for demographic and behavioural segmentation [41]. Integration with external data
sources, including census data, house price indices, and regional deprivation indices, further
enriches the analytical potential of Open Finance datasets.
Designing the data architecture2 compatible with Open Finance involves careful schematic
structuring to accommodate data streams from multiple financial products. This may involve
relational or graph-based schemas3 (see Figure 4) that associate customers with multiple
account entities spanning different providers and product types. Each account is tagged with
a timeline of events (e.g. transactions, contributions, expenditure, and facilitating temporal
structuring). Transactions and financial behaviours are categorised hierarchically to reflect
spending patterns (for example rent, discretionary spending, utilities), debt servicing, and
income sources.
1 Temporal data is information that involves time – data points that have timestamps or durations, such as records
of events, changes, or states occurring at different moments. Read more: Three Aspects of Temporal Data -
DATAVERSITY
2 Data Architecture – a blueprint for how data is collected, stored, managed and used. Read more: What Is a Data
Architecture? | IBM
3 Relational schemas organise data into tables with rows and columns, while graph-based schemas connect data
like a web of relationships using nodes and links (like social networks). Read more: What is A Graph Database? A
Beginner's Guide | DataCamp
Financial Regulation Innovation Lab (FRIL) | 11

GRAPH DB RELATIONAL DB
8
8
PRODUCT CUSTOMER
Customer --RESID-ESAT- + Location
..
\ f I
I
OR.D.E R
I
I
f \
8
SUPPLIER LOCATION
8 --DE_LIV_ER_S _ ..
Figure 4: Graph vs Relational schema. Source: Graph Database vs Relational Database
Temporal structuring is fundamental to capturing both static attributes (e.g. date of birth,
region, occupation) and evolving time-series data, such as monthly cash flows or investment
portfolio valuations [49]. This dual approach supports both cross-sectional snapshots and
trend-based analyses, enabling dynamic risk scoring and forecasting.
Integration with external data sources augments the internal financial dataset. Linking to
census data, house price indices (HPIs), regional deprivation indices or labour market statistics
enriches demographic and behavioural context. Such linkages improve accuracy where data
gaps exist, enhance segmentation models and enable robust benchmarking against
population-level trends.
2.3 Data sharing mechanisms
Central to Open Finance’s architecture are consent-based APIs, which empower consumers to
authorise specific data access between financial institutions and authorised third party
providers (TPPs).
TPPs operate as intermediaries facilitating data aggregation and service delivery across
multiple financial institutions, giving consumers a consolidated financial view beyond siloed
accounts. Their role is critical for seamless data ingestion and delivering personalised
recommendations. By leveraging secure APIs and consent arrangement platforms, TPPs enable
customers to benefit from comprehensive insights without compromising data security.
In summary, this framework of consent-driven APIs, robust regulatory support and trusted
intermediaries lays the foundation for Open Finance to deliver holistic financial management
and proactive future planning.
Financial Regulation Innovation Lab (FRIL) | 12

2.4 Advanced customer segmentation through AI-driven analytics
The wealth of data available through Open Finance will enable unprecedented sophistication
in customer segmentation approaches. Traditional demographic segmentation based on age,
income, geography etc will be superseded by behavioural and financial health-based clustering
methodologies that provide much more actionable insights for financial service providers [41],
[50].
Modern segmentation approaches leverage ML techniques to identify patterns in
transactional data that reveal spending periodicities, savings capacity assessments and
predictive indicators of future financial behaviour. These algorithms can detect subtle patterns
such as seasonal spending variations, response to economic shocks, and propensity for
financial product adoption that would be impossible to identify through traditional analytical
methods [41]. It is important to note that ML techniques can perform better than traditional
economic forecasting methods in many settings and are especially useful when financial
markets are uncertain or behave in non-linear ways. With proper tuning and testing, these
models can offer clearer and more accurate predictions. However, in some cases, simpler
models like factor models work just as well or even better, especially when the data is stable
and the relationships are mostly linear. Not every ML application improves results, and overly
complex models can perform worse if not carefully managed. The key is to use ML when it
adds real value, while still keeping traditional models as strong benchmarks. More in-depth
scientific discussion can be found in [51] and [52].
The implementation of clustering techniques such as K-means, DBSCAN and hierarchical
clustering on Open Finance data reveals distinct customer archetypes that align with different
financial health profiles and advisory needs. Sopra Steria & Oxford University’s collaborative
research demonstrates that effective clustering can identify groups such as "Emerging
Professionals with Debt", "Disciplined Debt Navigators", "Established and Secure
Homeowners", "Vulnerable and Delinquent Renters" and others, each requiring tailored
financial guidance strategies [53].
Advanced clustering methodologies incorporate both demographic features and behavioural
indicators derived from transaction analysis. Financial prudence scores, debt management
patterns, discretionary spending volatility and investment allocation preferences all contribute
to more nuanced customer understanding. These multidimensional approaches enable
financial institutions to move beyond simple income-based categorisation toward truly
personalised service delivery [54].
Financial Regulation Innovation Lab (FRIL) | 13

2.5 Privacy-preserving data enhancement
| The  sensitive  |     | nature  | of  financial  |     | data  requires  |     |     |     |
| --------------- | --- | ------- | -------------- | --- | --------------- | --- | --- | --- |
VAE:  Variational autoencoders
sophisticated approaches to data privacy and often the
| use  of             | synthetic  | data  generation  |      | for           | development.  |                        |          |        |
| ------------------- | ---------- | ----------------- | ---- | ------------- | ------------- | ---------------------- | -------- | ------ |
|                     |            |                   |      |               |               |                        | ♦        | }      |
| Privacy-preserving  |            | techniques,       |      | particularly  | those         |                        |          |        |
| compliant           | with       | GDPR              | and  | other         | regulatory    |                        |          |        |
|                     |            |                   |      |               |               | Encoder  Latent space  | Decoder  |        |
| frameworks,         | are        | essential         | for  | enabling      | innovation    |                        |          |        |
|                     |            |                   |      |               |               | (x,y)                  | z        | (x,y)  |
while protecting customer interests [55],[56].
|     |     |     |     |     |     | GAN:  Generative adversarial networks  |     | Empirical data  |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --------------- |
distribution
Synthetic data generation techniques using advanced
( 11~%
ML models, including Generative Adversarial Networks
|     |     |     |     |     |     | ■ ♦ | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(GANs)4  and  Variational  Autoencoders  (VAEs)5  (see  : Real
:  or
: fake?
| Figure                                                     | 5),  enable  | the  creation  |     | of  realistic  | financial  |           |     |     |
| ---------------------------------------------------------- | ------------ | -------------- | --- | -------------- | ---------- | --------- | --- | --- |
| datasets that maintain statistical properties of original  |              |                |     |                |            | Gaussian  |     |     |
Generator Synthetic data Discriminator
noise
data while eliminating direct personal identifiers. These
Figure 5: Technical schematic representations of
approaches  are  particularly  valuable  for  model  VAEs and GANs. Source: Chemistry Europe
development, testing and research collaboration [57].
Statistical  imputation  methods,  e.g.  Bayesian  inference6  approaches,  provide  robust
frameworks for enhancing existing datasets with additional demographic and behavioural
attributes. These techniques leverage publicly available distributional data from sources such
as the Office for National Statistics (ONS) to enrich synthetic datasets while maintaining
realistic correlation structures between variables [53]. The implementation of diverse privacy
techniques ensures that synthetic data generation processes provide mathematically rigorous
privacy guarantees. These approaches inject carefully calibrated noise into data generation
processes to prevent individual record identification while preserving overall dataset utility for
analytical purposes [55].

4 Generative Adversarial Networks (GANs) are a type of AI that generates new, realistic data, like images or music,
by pitting two neural networks against each other in an iterative competitive game. One network ("generator")
creates fake data, while the other ("discriminator") tries to tell the difference between the fake data and the real
data it was trained on. Read more: Generative Adversarial Networks Explained | AWS
5 Variational Autoencoders (VAEs) are AI models that learn to generate new, similar data like images or text by
understanding the underlying "rules" or patterns in existing data. They contain an encoder that maps input data
to a "fuzzy" representation and a decoder that takes a sample from this space and reconstructs new, similar data.
Read more: What is a Variational Autoencoder? | IBM
6 Bayesian inference is a learning technique that uses probabilities to define and reason about our beliefs. Read
more: Bayesian inference | Introduction with explained examples
Financial Regulation Innovation Lab (FRIL) | 14

2.6 Regulatory compliance and ethical considerations
Open Finance implementation must navigate complex regulatory landscapes that balance
innovation enablement with consumer protection. The Data (Use and Access) Bill and evolving
regulatory guidance from the FCA provide frameworks for responsible data utilisation while
encouraging technological advancement [58]. Consent-based data sharing mechanisms ensure
that customers maintain control over their financial information while enabling them to
benefit from improved service personalisation. These frameworks require clear transparency
about data usage purposes, retention periods and sharing arrangements with third parties.
The role of intermediaries and trusted third parties becomes crucial in maintaining data
security and privacy while enabling innovation. These entities must demonstrate robust data
governance and cybersecurity capabilities as well as compliance with evolving regulatory
requirements [59].
Ethical considerations extend beyond regulatory compliance to encompass fairness,
transparency and inclusivity in algorithmic decision-making. Open Finance systems must
actively address potential biases in data collection and model development, to ensure
unbiased outcomes across different customer segments [Error! Reference source not found.].
Bias can arise from incomplete, imbalanced or historically skewed data. If left unchecked, it
risks entrenching inequalities rather than reducing them. Literature emphasises the need for
ongoing checks, transparent algorithms and active human oversight to ensure fair outcomes
in financial decision-making [61], [62], [63].
Ethical frameworks should always be incorporated to prioritise consumers’ financial health
over business opportunity identification. Recommendations focus on improving customer
financial health and resilience rather than product sales or revenue optimisation. Such a
customer-centric approach builds trust and supports long-term relationship development.
Transparency and explainability requirements demand that consumers understand the basis
for recommendations and can see how their specific circumstances influence the guidance
provided. Explainable AI techniques (e.g. SHAP7) bring insights to life and deliver
recommendation rationales [64]. Proper use of data means prioritising positive impact on
people’s financial wellbeing, with fairness and transparency at the core. This approach builds
trust in technology and ensures that advancements serve everyone, not just financial
institutions.
7 SHAP - (SHapley Additive exPlanations) is a game theoretic approach to explain the output of any ML model.
Read more: An introduction to explainable AI with Shapley values — SHAP
Financial Regulation Innovation Lab (FRIL) | 15

2.7 Beyond Open Finance: inclusion, smart data and cross-border portability
While this paper places primary emphasis on Open Finance, it is important to recognise that
financial health is not defined solely within the boundaries of formal financial products. Hence,
Open Finance may not go far enough in addressing the full spectrum of financial inclusion.
Smart Data and Open Data initiatives, such as those being advanced under the UK Smart Data
schemes [65], can enrich the picture, particularly for those without bank accounts or who
interact only minimally with financial products (e.g. those who hold only a single basic bank
account with no available credit facilities). Utility bills, rent records, mobile phone usage and
other non-financial sources can provide crucial signals of discipline and resilience. In practice,
this broader approach can help ensure that individuals who are financially inactive,
underserved or “off-grid” are brought into the fold, as a key part of inclusion efforts.
To ensure inclusion, modelling frameworks should anticipate dedicated clusters for the
“financially invisible”. These individuals may not receive highly tailored recommendations due
to limited data, but they can still benefit from generalised, yet actionable, advice that
safeguards against exclusion. By recognising varied levels of data richness, personalised and
group-based advice can be delivered at scale, ensuring that the benefits of financial technology
reach as many people as possible. This addresses social equity and supports smarter risk
management.
Looking beyond national boundaries, financial health frameworks (when built on verifiable and
transferable data) hold promises for supporting mobility across borders. The ability to ‘carry’
one’s credit score, resilience metric or financial health indicators internationally could
empower individuals to access fair financial products wherever they choose to live or work,
removing a longstanding barrier for those relocating. With initiatives such as PSD3 in Europe
[66], which aims to expand and harmonise access to financial data across borders, there is an
opportunity to embed verification and interoperability mechanisms into Open Finance
architectures. Such portability would generate Pareto-optimal8 benefits: consumers retain
recognition of their financial discipline internationally, while institutions reduce onboarding
risks and open new opportunities for responsible growth.
8 Pareto optimality (efficiency) describes a situation where resources are allocated in the best possible way,
making it impossible to improve one person's situation without negatively affecting another. Read more: Pareto
Efficiency Examples and Production Possibility Frontier
Financial Regulation Innovation Lab (FRIL) | 16

3. Predictive analytics & cash flow modelling
The foundation of effective financial guidance and tailored recommendations in the Open
Finance era rests on sophisticated cash flow modelling capabilities that can accurately predict
and analyse individual customer financial trajectories. These modelling approaches must
capture the complexity of modern financial lives, whilst providing actionable insights for both
short-term stability optimisation and long-term wealth building strategies.
3.1 Comprehensive data sourcing
Effective modelling requires robust and comprehensive data sourcing that reflects the
complexity of modern personal finance.
• Open Finance Data: Core financial data is aggregated from multiple providers within the
Open Finance ecosystem. Collectively, these datasets offer an extensive view of
consumers’ financial positions and behaviours, surpassing the limited scope of Open
Banking transactional data. Note: cash transactions outside the digital ecosystem cannot
be tracked and hence, cannot form part of data-driven predictive modelling.
• Consumer-Disclosed Information: Supplementary data directly reported by consumers
plays a crucial role. Such event-driven disclosures provide critical context for adaptive and
personalised modelling.
• Publicly Available Data: External datasets enrich individual financial profiles by embedding
them within broader socio-economic frameworks. Integrating external data informs risk
assessments and ensures models account for environmental variables affecting financial
resilience.
Furthermore, modern cash flow modelling extends far beyond simple income-expense
calculations to encompass a holistic view of financial health that includes housing costs,
essential expenditures, debt service obligations, discretionary spending patterns and
allocation toward savings and investments. This comprehensive approach recognises that
financial health cannot be assessed through any single metric but requires integrated analysis
of multiple financial dimensions [67], [68].
--- ---
Housing cost modelling, for example, must account for regional variations, tenure types
(rental, mortgage, owned outright) and the relationship between housing expenses and
income levels across different demographics. Research demonstrates significant variation in
housing cost ratios based on regional economic conditions [69],[70], with London and
Southeast England showing markedly different patterns compared to other UK regions (see
Figure 6). Wealth and assets concentration in these regions plays a key role.
Financial Regulation Innovation Lab (FRIL) | 17

I I
26 73 121 170 222 263
£,000s
Bel~
Figure 6: Wealth & Assets Medians – 2018-2020.
Source: Distribution of individual total wealth in Great Britain - Office for National Statistics
Essential expenditure modelling beyond housing presents additional complexity, as spending
on food, transportation, and utilities varies not only with income levels but also with regional
cost structures and individual lifestyle choices. Advanced modelling approaches use
techniques like Iterative Proportional Fitting9, Propensity Score Matching10, and
Counterfactual Identification11 to generate realistic joint distributions that respect both
regional and income-based marginal constraints while introducing appropriate stochasticity to
capture individual variation.
Debt service modelling requires sophisticated understanding of different credit product types,
interest rate structures, payment timing patterns etc. The framework must distinguish
between revolving credit (credit cards, overdrafts) where payment obligations vary with
utilisation and fixed credit products (personal loans, mortgages) with predetermined payment
schedules. Integration of late payment patterns and associated penalty structures provides
crucial insights into financial stress indicators.
9 Iterative Proportional Fitting techniques – mathematical methods that adjust a dataset, such as a table of data,
to make its row and column totals match a known set of target marginal totals from a different source. Read
more: Iterative Proportional Fitting | TF Resource
10 Propensity score matching (PSM) – statistical method used in observational studies to reduce selection bias
when estimating the effect of a treatment. Read more: Understanding the Propensity Score: A Guide to Reducing
Bias | DataCamp
11 Counterfactuals help to identify which aspects of the input data are most influential in the model's decisions,
aiding in model debugging, fairness analysis and improving model performance. Read more: Counterfactual
Explanations: The What-Ifs of AI Decision Making
Financial Regulation Innovation Lab (FRIL) | 18

3.2 Dynamic risk assessment and behavioural prediction
Advanced cash flow modelling incorporates predictive analytics capabilities that can anticipate
future financial stress, identify emerging opportunities for financial improvement and adapt
recommendations based on changing circumstances. These capabilities rely on ML techniques
that can identify subtle patterns in financial behaviour that precede significant financial events
[50], [71].
--- ---
Transaction pattern analysis reveals cyclicality in financial behaviour that can inform both
short-term cash flow forecasting and long-term financial planning. Algorithms capable of
detecting spending seasonality, income volatility and irregular financial events enable more
accurate prediction of future cash flow challenges and opportunities [41].
Behavioural risk assessment leverages advanced analytics to ultimately identify early warning
indicators of financial distress. These may include increasing credit utilisation rates, growing
payment delays, changes in discretionary spending patterns or shifts in savings allocation
behaviours. ML models trained on historical patterns can identify customers at risk of financial
difficulty with sufficient advance warning to enable proactive intervention.
Such models may also add potential monitoring benefits in other contexts. For example,
undiagnosed memory disorders in early stages impact a broad range of financial outcomes,
such as: credit card account payment delinquency and amount of delinquent balance, credit
utilisation among credit card account holders, mortgage delinquency and delinquent balance
amount, and credit scores. These effects are seen across seniors in single and coupled
households, racial/ethnic minorities and non-minorities, and older adults living in areas with
higher and lower education levels [72]. Clinically informed lead indicators of dementia,
extended to include money management difficulty (which emerges as the most important lead
indicator), can inform a high-performance AI model to predict a clinical diagnosis [73]. Armed
with this knowledge, financial institutions can enhance their protection of vulnerable
customers with dementia and, potentially, inform the intergenerational transfer of financial
control. Likewise, mergers of large regional banks leading to branch closures and tighter credit
constraints in counties harm the mental health of lower-income individuals [74]. Conversely,
regulatory reforms that improved credit conditions reduced mental depression, boosted
labour market outcomes, eased access to mortgage debt, and reduced the ranks of the
“unbanked” [74]. Lastly, permissive laws deputising financial professionals to screen for
misbehaviour without providing explicit incentives are shown to result in fewer reports of
abuse by financial professionals and, separately, in financial crimes against the elderly, with a
stronger impact for isolated elders [75]. This showcases how financial professionals can
prevent financial fraud and combat social problems, an important contribution of finance to
society.
Financial Regulation Innovation Lab (FRIL) | 19

3.3 Feature selection & engineering
Identifying the most explanatory variables essential for accurate predictions and insightful
customer segmentation involves multiple analytical techniques, alongside careful ethical
considerations.
In order to extract data features that capture both the static attributes and dynamic financial
behaviours driving individual financial health and trajectories, the following techniques can
be used:
Technique Description
Measures linear and non-linear relationships between features
Correlation Analysis & Mutual Information
and target variables.
Evaluates categorical variables’ predictive power and enables
Chi-squared Binning
effective discretisation.
Reduces dimensionality by extracting orthogonal components
Principal Component Analysis (PCA)
explaining variance.
Iteratively adds or removes features to find the best predictive
Stepwise Regression
subset.
LASSO (Least Absolute Shrinkage and Selection Operator) uses
LASSO Regression regularisation to penalise less important features, promoting
model sparsity.
Creates temporal variables such as spending volatility, seasonal
Time-Based Feature Engineering
trends, late payment counts.
Measures a feature's importance by calculating the decrease in a
Permutation Feature Importance
model's performance after shuffling the feature's values.
In addition, the following ethical considerations must be embedded in the data processing:
• Protected Characteristics: Features relating to sensitive personal attributes, including but
not limited to race, gender, disabilities etc. Their inclusion requires clear justification and
transparency, to avoid bias and discrimination.
• Fairness Constraints: The modelling framework should apply fairness-aware principles to
ensure that selected features do not inadvertently conserve historical biases or result in
unfair outcomes for protected groups [76], [77], [78]. Continuous monitoring and
adjustment are required to uphold ethical standards in financial decision-making.
3.4 Predictive modelling & clustering
Building on carefully engineered features, a suite of AI/ML models can be utilised to generate
personalised financial health scores, and customer segmentation.
Financial Regulation Innovation Lab (FRIL) | 20

Model Type Examples Purpose & Characteristics
Baseline model for binary classification, valued for
Logistic Regression N/A
interpretability.
Ensemble Learning XGBoost, LightGBM, Handles complex relationships, reduces overfitting, suitable for
Methods Random Forest classification and regression.
Captures temporal dependencies and seasonality in sequential
Neural Networks LSTM
financial data.
Unsupervised Identifies clusters or segments within customer data for
k-means, DBSCAN, SOMs
Learning personalised insights.
Q-Learning, Deep Q-
Reinforcement Enables dynamic planning and real-time adaptive
Networks (DQN), Proximal
Learning recommendations, based on feedback.
Policy Optimisation
Used for variable selection by starting with a general model and
Autometrics, Hendry’s simplifying it step-by-step. Retains only statistically significant
General-to-Specific
Classical, Dynamic GETS variables, ensuring models are both data-driven and
(GETS) Modelling
Models economically meaningful. Helps identify key determinants in
large datasets while avoiding overfitting.
Typical Model Outputs:
• Financial Health Scorecard: A composite metric that provides a holistic measure of an
individual’s current financial health and risk exposure. It reflects cashflow stability, debt
management, sustainable growth in savings & investment and others.
• Resilience Index: This index quantifies an individual’s capacity to withstand adverse
macroeconomic shocks, incorporating scenario analysis informed by economic indicators
such as unemployment rates, inflation levels and housing market trends. Monte Carlo
simulations12 and stochastic modelling techniques can be used to achieve this.
• Clustering Results: Customer clusters derived from unsupervised methods identify typical
financial personas and segments, informing tailored recommendation strategies and
product offerings. Clustering outcomes are usually validated via silhouette scores13 and
external benchmarking. Other methods that may be considered within this context include
Linear Discriminant Analysis14 and Support Vector Machines15.
12 Monte Carlo simulations - computational method that uses repeated random sampling to generate a
distribution of potential outcomes for an uncertain event or process. Read more: Monte Carlo Simulation: What
It Is, How It Works, History, 4 Key Steps
13 Silhouette score - a metric used to evaluate the quality of clustering in unsupervised machine learning. The
silhouette score assesses both cohesion (how similar a point is to its own cluster) and separation (how dissimilar
a point is to neighboring clusters).
14 Linear Discriminant Analysis – a supervised ML technique used for dimensionality reduction and classification
by finding a linear combination of features that maximizes the separability between known classes. Read more:
What Is Linear Discriminant Analysis? | IBM
15 Support Vector Machine - a supervised ML algorithm that finds the best line or "hyperplane" to separate
different classes of data. Read more: What Is Support Vector Machine? | IBM
Financial Regulation Innovation Lab (FRIL) | 21

3.5 Model explainability vs performance
The success of AI-driven financial models rests on balancing predictive performance with
interpretability. While high predictive accuracy metrics (such as Precision, Recall, F1 Score,
and Log-loss) demonstrate model effectiveness in classifying or forecasting financial
behaviours (e.g. probability of default or cash flow stability), these alone are insufficient for
transparent customer engagement and regulatory compliance.
• Precision quantifies the correctness of positive predictions (in our case correctly
identifying at-risk customers).
• Recall captures the model’s ability to detect all relevant positive cases.
• F1 Score harmonises precision and recall into a single metric.
• Log-loss evaluates the confidence of probabilistic predictions, penalising overconfident
errors.
Other measures for practical applicability and predictive power such as proportion of variation
(R2), Mean Squared Error, Root Mean Squared Error, Mean Absolute Error, other loss functions
(e.g. quasi-likelihood function, asymmetric loss function) and more [79],[80],[81].
In financial health contexts, where trust and accountability are most important, explainable AI
(XAI) techniques such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable
Model-agnostic Explanations) play a pivotal role. These tools dissect complex AI models to
provide:
• Data feature-level insights showing how individual inputs (such as income volatility,
discretionary spend etc) influence predictions.
• Local explanations that clarify a specific decision for an individual customer, essential for
personalised recommendations.
There is a trade-off between interpretability and predictive power. Simpler models like logistic
regression offer clear rationales but may miss compound patterns, while complex ensembles
or neural networks may capture deeper relationships at the cost of harder interpretability. This
paper acknowledges the trade-off at a high level - detailed exploration is reserved for works
focused on AI fairness and regulatory explainability.
3.6 Stochastic modelling and scenario analysis
The inherent uncertainty in financial planning requires stochastic modelling approaches that
can capture the range of possible financial outcomes and their associated probabilities. Monte-
Carlo simulation techniques enable comprehensive scenario analysis that accounts for
variability in income, expenses, investment returns etc.
Investment modelling incorporates sophisticated stochastic processes including Geometric
Brownian Motion16 (see Figure 7) for risky asset evolution and deterministic modelling for risk-
16 Geometric Brownian Motion – a mathematical model used to describe asset prices such as stocks, that follow
a pattern of random (but generally upward) movement. A key feature is that the asset's value cannot go below
Financial Regulation Innovation Lab (FRIL) | 22

free savings growth. These approaches account for market volatility and risk tolerance
preferences.
Figure 7: Geometric Brownian Motion Simulation. Source: Montecarlo simulation for Geometric Brownian
Motion
Wealth accumulation trajectories are widely held to be based upon either S-shaped or
inverted-L shaped curves shown below for the relationship of income today and tomorrow
(and by extension wealth as a function of income) [82] – see Figure 8.
Figure 8: The S-Shape Curve and the Poverty Trap (left); the Inverted L-Shape: No Poverty Trap (right). Source:
[82]
Age groups and income-based risk appetite modelling recognises that appropriate investment
allocation varies significantly across different life stages and wealth levels. Glide path
zero, and its changes are proportional to its current price. Read more: How to use Monte Carlo simulation
with GBM
Financial Regulation Innovation Lab (FRIL) | 23

methodologies can adjust risk exposure based on time horizon and financial capacity, ensuring
that investment recommendations remain appropriate as circumstances change.
Scenario analysis capabilities enable exploration of various "what-if" situations including job
loss, health events, housing market changes, economic recession scenarios and so on. These
analyses help customers understand the resilience of their financial plans and identify areas
where additional protection or flexibility might be beneficial [83],[84].
3.7 Adaptation and continuous learning
Modern cash flow modelling systems must provide real-time adaptation capabilities that can
respond immediately to changing financial circumstances. This requires regular data refresh
capabilities that can incorporate new transaction information, economic data updates and
customer-reported life changes into ongoing financial assessments [71]. As discussed earlier
in this paper, potential non-financial benefits can result from this approach, e.g. diagnosing
memory disorders, mild cognitive impairment, dementia, mental health deterioration and
others [72],[73],[74].
ML models enable continuous improvement in prediction accuracy through ongoing training
on new data patterns [50]. These systems can identify shifts in customer behaviour, adapt to
changing economic conditions, and refine their understanding of the relationships between
different financial variables over time.
The integration of feedback loops from customer interactions and outcomes (see Figure 9)
enables model validation and improvement [41]. When customers report satisfaction with
recommendations, experience financial improvements or deteriorations, this information
feeds back into model refinement processes.
Figure 9: An example of continuous feedback loop structure. Source: Zeda.io
Financial Regulation Innovation Lab (FRIL) | 24

4. Smart Personalised Finance Management Framework
The culmination of Open Finance data integration and sophisticated cash flow modelling
enables the development of comprehensive smart personalised finance management systems
that can provide tailored, actionable financial guidance and recommendations at scale. These
systems must balance automated efficiency with personalised relevance while maintaining
regulatory compliance and ethical standards.
4.1 Hierarchical financial needs framework
Effective personalised financial management recognises that financial needs exist in a
hierarchical structure, similar to Maslow's hierarchy of human needs (see Figure 10). This
framework prioritises fundamental financial stability before progressing to more advanced
wealth optimisation objectives [85],[86],[87].
The foundational level focuses on basic financial survival through cash flow stability
optimisation. Customers experiencing negative cash flow or inadequate emergency savings
require immediate attention to essential expense management, income stabilisation and basic
safety net establishment. This level corresponds to the physiological and safety needs in
Maslow's hierarchy and must be addressed before any higher-level financial planning can be
effective [85].
The second level addresses financial security through debt management and risk mitigation.
Once basic cash flow stability is achieved, attention turns to managing debt service ratios,
eliminating high-interest debt, and establishing appropriate insurance coverage [86]. This level
provides the foundation for more advanced financial planning by eliminating major financial
vulnerabilities.
The third level focuses on financial independence through strategic wealth accumulation. With
stability and security established, customers can pursue long-term wealth building through
investment optimisation, tax planning and goal-based savings strategies [87]. This level
corresponds to self-esteem and belonging needs as customers work toward financial goals that
enable lifestyle choices and social participation.
The highest level encompasses financial self-actualisation through legacy planning and value-
aligned financial strategies. This includes estate planning, charitable giving and investment
approaches that reflect personal values and long-term societal impact.
Financial Regulation Innovation Lab (FRIL) | 25

Figure 10: Application of Maslow’s theory in a financial needs’ context.
Source: Visualizing the Hierarchy of Financial Needs
4.2 Sequential optimisation engine architecture
The implementation of hierarchical financial guidance requires sophisticated sequential
optimisation engines that can systematically address financial needs in appropriate priority
order while avoiding premature advancement to higher-level objectives before foundational
needs are met.
Layer 1 optimisation focuses exclusively on cash flow stability and emergency fund adequacy.
The system evaluates current cash flow patterns, identifies potential expense reductions
through discretionary spending optimisation and essential expense rebudgeting, and
calculates feasible timelines for emergency fund accumulation. For young renters, this may
include recommendations for temporary housing arrangement changes to dramatically reduce
housing costs.
Financial Regulation Innovation Lab (FRIL) | 26

The optimisation engine incorporates constraint handling that recognises practical limitations
on expense reduction while identifying all feasible improvement strategies. If cash flow cannot
be made positive through reasonable expense modifications, the system provides
recommendations about the need for professional financial counselling or income
enhancement strategies.
Layer 2 optimisation addresses debt
management and service ratio
optimisation only after Layer 1 stability
is achieved. This layer prioritises
elimination of payment arrears,
reduction of high-interest debt balances
and optimisation of debt service ratios
to sustainable levels. The system
calculates optimal debt paydown
strategies that balance interest cost
minimisation with cash flow
sustainability.
Advanced debt optimisation incorporates understanding of different debt product
characteristics, interest rate structures, and penalty mechanisms. The system can identify
optimal balance transfer opportunities, refinancing possibilities, and payment timing
strategies that minimise total debt service costs while maintaining financial stability [88].
Layer 3 optimisation addresses wealth maximisation and goal achievement once both stability
and debt management objectives are met. This layer incorporates sophisticated goal-based
financial planning including housing deposit accumulation, retirement planning and
investment portfolio optimisation. Relevant economic aspects of wealth accumulation over
time are examined thoroughly in [82],[89].
4.3 Personalisation and behavioural integration
Drawing from Sopra Steria’s Research & Development work, smart personalised finance
management synthesises clustering-driven persona construction with a hierarchical
optimisation engine to tailor financial recommendations precisely.
Persona Construction
Clustering analysis has identified eight distinct customer segments (personas), revealing
heterogeneous financial conditions and behaviours:
• Emerging Professionals with Debt: Young renters in professional roles, facing moderate
incomes but significant debt burdens and arrears risks.
Financial Regulation Innovation Lab (FRIL) | 27

• Disciplined Debt Navigators: Financially responsible professionals adept at managing debt
and sustaining healthy cash flows.
• Established and Secure Homeowners: Mature homeowners with stable incomes, robust
savings and strong financial discipline.
• Vulnerable and Delinquent Renters: Low-income young renters burdened by high
financial distress and poor payment behaviours.
• Affluent and Prudent Investors: High earners focused on wealth accumulation, investing
strategically.
• Struggling to Start: Entry-level earners with low income and minimal savings, vulnerable
to shocks despite good payment discipline.
• Steady and Responsible Managers: Balanced demographic with solid surplus and
moderate liabilities; exemplary payment records.
• Crisis-Prone and Underbanked: Younger renters with persistent negative cash flow, low
savings, and limited credit access.
Defining such personas enables contextualisation of recommendations and establishes
communication frameworks aligned with customer needs and motivational factors.
Effective personalised financial management must account for individual behavioural patterns,
risk preferences and life circumstances that influence financial decision-making effectiveness.
This requires integration of behavioural finance principles with technical optimisation
capabilities [90],[91]. For example, modelling the optimal illiquidity levels for retirement saving
based on present bias [92]. This research shows the relationship with present bias impacts
these levels via early pre-retirement withdrawal penalties from mandatory savings accounts,
illustrating how a social planner would set up a simple socially optimal pension scheme. Their
very simple mechanisms provide good welfare approximations to arbitrarily complex, optimal
mechanisms.
Other sources investigate saving goals’ effectiveness in increasing individuals' savings from a
fintech app’s data, finding that setting soft goals (whereby individuals face no penalties when
deviating from their plan) causally increases individuals' savings rate [93]. Increased savings
within the app are not at the cost of reduced savings outside the app, and soft goal setting is
especially effective for those in the population at greater risk of under-saving. Soft goals could
thus be deployed to help low-income individuals, who are arguably among those who could
benefit from such fintech solutions the most, and are also more scalable and easier to
administer compared to their counterpart hard goals, especially in real-life settings [93].
Other studies explore welfare consequences of retirement plan automatic enrolment policies,
for example in [94]. At 43 to 48 months of tenure, their experimental policy raises cumulative
contributions to such plans by 4.1% of first-year annualised salary. However, they find little
evidence that auto-enrolment increases financial distress, which holds even among
subpopulations very likely to have large auto-enrolment effects on plan contributions.
Automatic enrolment has a precisely estimated zero effect on credit scores, no significant
Financial Regulation Innovation Lab (FRIL) | 28

effect on debt excluding auto loans and first mortgages and no significant positive effects on a
range of measures of adverse credit outcomes, with the exception of first-mortgage
foreclosures.
Some researchers find that offering consumers the opportunity to adopt increased retirement
saving behaviour immediately and then, only if they decline, inviting them to adopt it later (i.e.
offering “sequential pre-commitment”) increases inferred urgency, predicting greater
adoption [95],[96].
Lastly, various nudge interventions for increased retirement saving merit consideration. These
alter people’s decisions without coercion or significant changes to economic incentives and
include especially efficacious variations like fresh start nudging and semi-automated nudging.
Moreover, they compare favourably with traditional interventions/policy tools such as tax
incentives and other financial inducements, even without restricting the menu of options and
without altering financial incentives [97],[98].
Customer segmentation insights derived from clustering analysis inform personalisation
strategies that recognise different customer archetypes require different communication
approaches, recommendation timing and motivational frameworks. "Disciplined Debt
Navigators" respond well to detailed analytical information and long-term planning
frameworks, while "Vulnerable and Delinquent Renters" require more immediate, practical
guidance with simplified decision frameworks.
Behavioural consistency modelling recognises that financial improvement requires sustainable
behaviour change rather than short-term sacrifice. The system incorporates understanding of
customer spending patterns, seasonal variations and discretionary spending preferences to
develop realistic improvement strategies that can be maintained over time [41].
Risk appetite integration ensures that investment and planning recommendations align with
individual comfort levels and life circumstances. For instance, income-level considerations and
personal risk tolerance assessments combine to generate investment allocations that balance
growth potential with downside protection.
4.4 Continuous improvement and outcome tracking
Advanced personalised finance management systems incorporate comprehensive feedback
mechanisms that enable continuous improvement in recommendation effectiveness and
customer outcome optimisation. These systems must track customer financial health
improvements, recommendation adoption rates, and long-term financial trajectory changes
[41].
Performance monitoring is needed to track key metrics including emergency fund adequacy,
debt service ratio improvements, investment goal progress and overall financial stress
reduction. These metrics provide objective measures of system effectiveness and identify
areas requiring refinement.
Financial Regulation Innovation Lab (FRIL) | 29

Customer satisfaction integration ensures that technical optimisation aligns with customer
experience and perceived value [90]. Feedback mechanisms capture customer preferences,
communication effectiveness, and recommendation relevance to guide system enhancement.
The integration of macroeconomic monitoring enables system adaptation to changing
economic conditions and regulatory frameworks [99]. This ensures that recommendations
remain relevant and effective across different economic scenarios.
Through a comprehensive framework, smart personalised finance management systems can
deliver significant value to customers while maintaining operational efficiency and regulatory
compliance, ultimately democratising access to sophisticated financial guidance previously
available only to high-net-worth individuals.
Financial Regulation Innovation Lab (FRIL) | 30

5. Conclusion
The convergence of AI and Open Finance marks a fundamental shift in how financial health is
understood, measured and supported. This whitepaper has demonstrated that moving beyond
legacy, credit-score-centric systems is no longer simply an innovation opportunity, but a
necessity. Recent economic shocks, widening inequalities and changing consumer
expectations demand data-driven financial modelling that is inclusive and focused on long-
term resilience.
Open Finance will provide the infrastructure to enable this transformation by facilitating
secure, consent-driven access to a far broader range of financial data. Combined with
advanced AI and machine learning techniques, such as predictive cashflow modelling, persona-
based optimisation and explainable analytics – this data becomes the foundation for intelligent
financial guidance. Rather than relying on retrospective assessments, financial institutions can
offer proactive support: anticipating risk, identifying opportunity and tailoring interventions to
individual circumstances.
However, technology alone is not sufficient. Ethical data stewardship, fairness, transparency
and regulatory compliance must remain central. The FCA’s Advice Guidance Boundary Review
and Consumer Duty framework show that innovation and consumer protection are not
mutually exclusive but mutually reinforcing. Responsible AI, anchored in explainability, bias
mitigation and privacy safeguards, ensures these advances enhance trust rather than diminish
it.
This transformation enables financial institutions to evolve from product providers to long-
term financial partners – supporting everyday budgeting, responsible borrowing, future
planning and improved financial wellbeing. Consumers, in turn, can gain access to
personalised, non-product-specific guidance that empowers informed decision-making and
strengthens resilience through life’s uncertainties.
As Open Finance infrastructure matures in future, continued collaboration between
policymakers, regulators, academia, industry and technology providers will be crucial. Those
who act early – investing in data capabilities, ethical AI and human-centric design, will define
a more inclusive and trustworthy financial ecosystem. Out of crisis arises opportunity: a
pathway towards prosperity built on transparency, accountability and holistic financial health
evaluation.
Financial Regulation Innovation Lab (FRIL) | 31

6. References
1. Haldane, A.G., Aikman, D., Kapadia, S. and Hinterschweiger, M., 2017. Rethinking
financial stability. Peterson Institute for International Economics, October 12th,
mimeo.
Web Access
2. Jha, M., Liu, H. and Manela, A., 2025. Does finance benefit society? A language
embedding approach. The Review of Financial Studies, p.hhaf012.
Web Access
3. Alvaredo, F., Chancel, L., Piketty, T., Saez, E. and Zucman, G., 2017. Global inequality
dynamics: New findings from WID. world. American Economic Review, 107(5),
pp.404-409.
Web Access
4. Tørsløv, T., Wier, L. and Zucman, G., 2023. The missing profits of nations. The Review
of Economic Studies, 90(3), pp.1499-1534.
Web Access
5. Retail Economics, 2022. The Big Squeeze: Pressure on consumer finances, rising
inflation & money management.
Web Access
6. Bell, J., Jurgenson, J., Warmath, D., 2025. The Role of Objective Financial Situation and
Psychological Outlook in the Relationship Between Personal Life Shocks and Financial
Well-Being. Journal of Consumer Behaviour 24: 632-654.
Web Access
7. Thinks Insights & Strategy and Financial Conduct Authority (FCA), 2025. Advice
Guidance Boundary Review: Retail Investments Consumer Research.
Web Access
8. Carbon Financial, 2025. Bridging the advice gap: why only 8% of UK adults seek
financial guidance.
Web Access
9. Bao, L., Huang, D. and Lin, C., 2024. Can artificial intelligence improve gender
equality? Evidence from a natural experiment. Management Science.
Web Access
10. Bayer, R.C. and Renou, L., 2024. Interacting with Man or Machine: When Do Humans
Reason Better?. Management Science.
Web Access
11. Garcia, D., Tolvanen, J. and Wagner, A.K., 2024. Strategic responses to algorithmic
recommendations: evidence from hotel pricing. Management Science.
Web Access
Financial Regulation Innovation Lab (FRIL) | 32

12. Bukovski, K., Cepkauskaite, A., Shaikh, S., Finch, J. & Otioma, C., 2025. Consumers at
the heart of innovation: Financial health evaluation in the UK regulatory landscape.
Web Access
13. NASA Federal Credit Union, 2024. The four pillars of financial health.
Web Access
14. Financial Health Network, 2025. FinHealth Standards.
Web Access
15. Bartlett, R., Morse, A., Stanton, R. and Wallace, N., 2022. Consumer-lending
discrimination in the FinTech Era. Journal of Financial Economics, 143(1), pp.30-56.
Web Access
16. Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T. and Walther, A., 2022. Predictably
unequal? The effects of machine learning on credit markets. The Journal of Finance,
77(1), pp.5-47.
Web Access
17. Arráiz, I., Stucchi, R., Bruhn, M., 2015. Psychometrics as a tool to improve screening
and access to credit. World Bank Policy Research Working Paper 7506.
Web Access
18. Sahay, R., Eriksson von Allmen, U., Lahreche, A., Khera, P., Ogawa, S., Bazarbash, M.
and Beaton, K., 2020. The Promise of Fintech: Financial Inclusion in the Post COVID-19
Era. IMF Departmental Paper 20/009.
Web Access
19. Dunn, A., Celik, N., Warren, A., Chege, W. - Financial Health Network, 2022. 2022 U.S.
Trends Report: Landmark changes in Americans’ financial health.
Web Access
20. Duckworth, A.L., Peterson, C., Matthews, M.D. and Kelly, D.R., 2007. Grit:
perseverance and passion for long-term goals. Journal of Personality and Social
Psychology, 92(6), p.1087.
Web Access
21. Duckworth, A.L. and Quinn, P.D., 2009. Development and validation of the Short Grit
Scale (GRIT–S). Journal of Personality Assessment, 91(2), pp.166-174.
Web Access
22. Duarte, J., Siegel, S. and Young, L., 2012. Trust and credit: The role of appearance in
peer-to-peer lending. The Review of Financial Studies, 25(8), pp.2455-2484.
Web Access
23. Erel, I. and Liebersohn, J., 2022. Can FinTech reduce disparities in access to finance?
Evidence from the Paycheck Protection Program. Journal of Financial Economics,
Financial Regulation Innovation Lab (FRIL) | 33

146(1), pp.90-118.
Web Access
24. Gopal, M. and Schnabl, P., 2022. The rise of finance companies and fintech lenders in
small business lending. The Review of Financial Studies, 35(11), pp.4859-4901.
Web Access
25. Irani, R.M., Iyer, R., Meisenzahl, R.R. and Peydro, J.L., 2021. The rise of shadow
banking: Evidence from capital regulation. The Review of Financial Studies, 34(5),
pp.2181-2235.
Web Access
26. Rossi, A.G. and Utkus, S., 2024. The diversification and welfare effects of robo-
advising. Journal of Financial Economics, 157, p.103869.
Web Access
27. Cao, S., Jiang, W., Wang, J. and Yang, B., 2024. From man vs. machine to man+
machine: The art and AI of stock analyses. Journal of Financial Economics, 160,
p.103910.
Web Access
28. Sopra Steria, 2025. Digital Banking Experience Report (DBX) - Financial Well-Being as a
Key Differentiator in Banking.
Web Access
29. Baird, G., Reed, J. - Farrer & Co., 2025. The advice-guidance boundary review: The
new targeted support regime.
Web Access
30. OECD, 2023. Open Finance policy considerations, OECD Business and Finance Policy
Papers, OECD Publishing.
Web Access
31. Lessar, S., Plant, S., Kiers, A., Rennie, C., Milner, H. - DLA Piper, 2023. The European
Commission’s proposal for Payment Services Directive 3 (PSD3).
Web Access
32. Financial Conduct Authority (FCA), 2025. Open finance sprint: Outcomes report.
Web Access
33. The Business Research Company, 2025. Global Artificial Intelligence AI In Financial
Wellness Growth Drivers 2025, Forecast To 2034.
Web Access
34. Standard Life, 2023. Standard Life partners with Moneyhub to integrate Open Finance
functionality.
Web Access
Financial Regulation Innovation Lab (FRIL) | 34

35. Ozone API, 2024. How Open Finance is revolutionising financial management for
young adults.
Web Access
36. Moneyhub, 2025. Moneyhub extends partnership with Experian to help people pay
debt faster.
Web Access
37. The Power 50, 2022. Moneyhub joins forces with Pennyworth to democratise
financial planning.
Web Access
38. Standard Life, 2025. Finance for all the family: Standard Life launches digital coaching
platform to support key life moments.
Web Access
39. Bank of England, 2024. Artificial intelligence in UK financial services - 2024.
Web Access
40. Delev, Z. - GDPR Local, 2024. The future of Finance: Adapting to AI and data privacy
laws.
Web Access
41. Coinscrap Finance, 2025. Customer segmentation in banking: AI revolutionizes
clustering.
Web Access
42. Open Banking Limited, 2023. From Open Banking to Open Finance and beyond.
Web Access
43. Morgan, K. - Plaid, 2022. Innovating in the UK's credit information market - how Open
Banking can help and why it matters.
Web Access
44. Babina, T., Bahaj, S., Buchak, G., De Marco, F., Foulis, A., Gornall, W., Mazzola, F., Yu,
T. - Bank of England, 2024. Customer data access and fintech entry: Early evidence
from Open Banking. Staff Working Paper No. 1059
Web Access
45. Financial Conduct Authority (FCA), 2025. Financial Lives Survey 2024: Credit and loans
– Selected findings.
Web Access
46. Financial Conduct Authority (FCA), 2025. Mortgage lending statistics.
Web Access
47. Centre for Finance, Innovation and Technology (CFIT), 2024. Embracing the UK’s Open
Finance opportunity.
Web Access
Financial Regulation Innovation Lab (FRIL) | 35

48. Open Banking Limited. Open Finance.
Web Access
49. Cambridge Centre for Alternative Finance (CCAF), 2024. The global state of Open
Banking and Open Finance. Cambridge: Cambridge Centre for Alternative Finance,
Cambridge Judge Business School, University of Cambridge.
Web Access
50. Fariha, N., Khan, M. N. M., Hossain, M. I., Reza, S. A., Bortty, J. C., Sultana, K. S., Islam
Jawad, M. S., Safat, S., Ahad, M. A. & Begum, M., 2025. Advanced fraud detection
using machine learning models: enhancing financial transaction security.
Web Access
51. Goulet Coulombe, P., Leroux, M., Stevanovic, D. and Surprenant, S., 2022. How is
machine learning useful for macroeconomic forecasting?. Journal of Applied
Econometrics, 37(5), pp.920-964.
Web Access
52. Gu, S., Kelly, B. and Xiu, D., 2020. Empirical asset pricing via machine learning. The
Review of Financial Studies, 33(5), pp.2223-2273.
Web Access
53. Lin Zi, Bukovski, K., Journey C., 2025. Smart Personalised Finance. MSc Dissertation in
collaboration between Sopra Steria and University of Oxford’s Mathematical Institute
(Mathematical and Computational Finance MSc).
54. Matellio, 2024. Customer segmentation analytics in banking: Unlocking Insights for
Enhanced Decision-Making.
Web Access
55. Selvaraj, A., Sivathapandi, P., Namperumal, G., 2022. Privacy-Preserving Synthetic
Data Generation in Financial Services: Implementing Differential Privacy in AI-Driven
Data Synthesis for Regulatory Compliance. Journal of Artificial Intelligence Research
Vol. 2 No. 1.
Web Access
56. Berry, M. L. - EM360Tech, 2025. Is Synthetic Data GDPR-Compliant? What Security
and Privacy Leaders Need to Know
Web Access
57. Financial Conduct Authority (FCA), 2024. Using synthetic data in financial services.
The Synthetic Data Expert Group.
Web Access
58. Financial Conduct Authority (FCA), 2023. Exploring synthetic data validation: Privacy,
utility and fidelity.
Web Access
Financial Regulation Innovation Lab (FRIL) | 36

59. Centre for Data Ethics and Innovation, 2021. Unlocking the value of data: Exploring
the role of data intermediaries.
Web Access
60. Mirzoev, V. and Machado, M.R., 2025. The impact of synthetic data augmentation on
algorithmic bias in credit risk assessment. University of Twente.
Web Access
61. Bailey, K. - Corporate Finance Institute. The ethics of AI in finance: How to detect and
prevent bias.
Web Access
62. Bogiatzis-Gibbons, D., Charles, L., Dewing, H., Gretschel, C., Jomy, M., Reid, A., Slack,
R. - Financial Conduct Authority (FCA), 2024. A literature review on bias in supervised
machine learning.
Web Access
63. Turner Lee, N., Resnick, P. and Barton, G. - Brookings, 2019. Algorithmic bias
detection and mitigation: Best practices and policies to reduce consumer harms.
Web Access
64. Irons, A., Bukovski, K., 2024. Intelligent financial health evaluation. MSc Dissertation
in collaboration between Sopra Steria and University of Oxford’s Mathematical
Institute (Mathematical and Computational Finance MSc).
65. Department for Business and Trade (UK Government), 2024. The Smart Data
roadmap: Action the government is taking in 2024 to 2025.
Web Access
66. Finexer, 2025. PSD3: All you need to know in 2025.
Web Access
67. Bentleys, 2025. How to improve cash flow: Best strategies for business success.
Web Access
68. Treelife, 2024. Cash Flow Optimization – Meaning, Techniques, Forecasting.
Web Access
69. HM Land Registry and Office for National Statistics (ONS), 2025. UK House Price
Index: May 2025 summary.
Web Access
70. Office for National Statistics (ONS), 2025. Private rent and house prices, UK: July 2025.
Web Access
71. Tookitaki, 2025. Smarter Surveillance: How Machine Learning Is Transforming
Transaction Monitoring.
Web Access
Financial Regulation Innovation Lab (FRIL) | 37

72. Gresenz, C.R., Mitchell, J.M., Rodriguez, B., Turner, R.S. and Van der Klaauw, W.,
2025. The financial consequences of undiagnosed memory disorders. Journal of
Financial Economics, 172, 104149.
Web Access
73. Agarwal, S. and Muckley, C.B., 2025. Money management difficulty, customer
protection and the detection of early-stage dementia. Michael J. Brennan Irish
Finance Working Paper Series Research Paper, (24-4).
Web Access
74. Hu, Q., Levine, R., Lin, C. and Tai, M., 2024. Credit Market Conditions and Mental
Health. Management Science, 71(3), pp.1967-1987.
Web Access
75. Carlin, B., Umar, T. and Yi, H., 2023. Deputizing financial institutions to fight elder
abuse. Journal of Financial Economics, 149(3), pp.557-577.
Web Access
76. de Souza Santos, R., Fronchetti, F., Freire, S. and Spinola, R., 2025. Software fairness
debt: Building a research agenda for addressing bias in AI systems. ACM Transactions
on Software Engineering and Methodology, 34(5), pp.1-21.
Web Access
77. Das, A., Uddin, G., Chowdhury, S., Akhond, M.R. and Hemmati, H., 2025. Applications
and Challenges of Fairness APIs in Machine Learning Software. ACM Transactions on
Software Engineering and Methodology.
Web Access
78. Chen, Z., Zhang, J.M., Hort, M., Harman, M. and Sarro, F., 2022. Fairness testing: A
comprehensive survey and analysis of trends. ACM Transactions on Software
Engineering and Methodology, 33(5), pp.1-59.
Web Access
79. Conlon, T., Cotter, J. and Kynigakis, I., 2025. Asset allocation with factor-based
covariance matrices. European Journal of Operational Research, 325(1), pp.189-203.
Web Access
80. Goulet Coulombe, P., Leroux, M., Stevanovic, D. and Surprenant, S., 2022. How is
machine learning useful for macroeconomic forecasting?. Journal of Applied
Econometrics, 37(5), pp.920-964.
Web Access
81. Giglio, S., Kelly, B. and Xiu, D., 2022. Factor models, machine learning, and asset
pricing. Annual Review of Financial Economics, 14(1), pp.337-368.
Web Access
Financial Regulation Innovation Lab (FRIL) | 38

82. Duflo, E. and Banerjee, A., 2011. Poor economics (Vol. 619). New York: PublicAffairs.
& parts of chapters 6-9 (insurance, lending, saving and business for the poor,
microcredit.)
Web Access
83. Holistique Training, 2023. Optimising cash flow: Strategies For Financial Stability.
Web Access
84. KPMG. Cash flow forecasting and stabilisation.
Web Access
85. McBride, J. - Stewardship Wealth Advisors, 2021. The financial needs hierarchy.
Web Access
86. Carbonaro, C. - Ashton Thomas Private Wealth, 2024. How Maslow’s pyramid
intersects with the financial planning pyramid.
Web Access
87. Chen, O., 2024. Maslow’s hierarchy of needs and money.
Web Access
88. Hamzat, L., 2025. Real-Time Financial Resilience and Debt Optimization for
Entrepreneurs: Tackling Debt Management as a Financial Health Pandemic and
Empowering Small Business Growth Through Early Detection of Financial Distress and
Effortless Capital Management. International Journal of Research Publication and
Reviews, Vol 02, Issue 05, pp 202-223
Web Access
89. Banerjee, A.V. and Duflo, E., 2019. Good economics for hard times. PublicAffairs.
Web Access
90. Kaur, J. - Akira AI, 2024. Financial Robo-Advisory: Harnessing Agentic AI.
Web Access
91. Kashyap, A., 2025. AI-driven financial advisory: The rise of robo-advisors.
Web Access
92. Beshears, J., Choi, J.J., Clayton, C., Harris, C., Laibson, D. and Madrian, B.C., 2025.
Optimal illiquidity. Journal of Financial Economics, 165, p.103996.
Web Access
93. Gargano, A. and Rossi, A.G., 2024. Goal setting and saving in the fintech era. The
Journal of Finance, 79(3), pp.1931-1976.
Web Access
94. Beshears, J., Choi, J.J., Laibson, D., Madrian, B.C. and Skimmyhorn, W.L., 2022.
Borrowing to save? The impact of automatic enrollment on debt. The Journal of
Finance, 77(1), pp.403-447.
Web Access
Financial Regulation Innovation Lab (FRIL) | 39

95. Reiff, J., Dai, H., Beshears, J., Milkman, K.L. and Benartzi, S., 2023. Save more today or
tomorrow: the role of urgency in precommitment design. Journal of Marketing
Research, 60(6), pp.1095-1113.
Web Access
96. Benartzi, S., Beshears, J., Milkman, K.L., Sunstein, C.R., Thaler, R.H., Shankar, M.,
Tucker-Ray, W., Congdon, W.J. and Galing, S., 2017. Should governments invest more
in nudging?. Psychological Science, 28(8), pp.1041-1055.
Web Access
97. Beshears, J., Dai, H., Milkman, K.L. and Benartzi, S., 2021. Using fresh starts to nudge
increased retirement savings. Organizational Behavior and Human Decision
Processes, 167, pp.72-87.
Web Access
98. Beshears, J. and Kosowsky, H., 2020. Nudging: Progress to date and future directions.
Organizational behavior and human decision processes, 161, pp.3-19.
Web Access
99. Bank of England, 2023. Financial Stability in Focus: The FPC’s approach to assessing
risks in market-based finance.
Web Access
Financial Regulation Innovation Lab (FRIL) | 40

About the Authors
Kal Bukovski is Consulting Senior Manager and Director of Academia &
Research at Sopra Steria. He specialises in the financial services domain,
driving transformative projects and data-driven excellence. With expertise in
analytics, data science, business intelligence and data visualisation, he
supports clients in making strategic decisions and gaining a competitive edge
in this dynamic, regulated domain. Kal leads business projects and
collaborations with Academia, fostering innovation, compliance and data-
driven storytelling. His main areas of expertise are regulatory modelling, credit risk, consumers’
financial health, scorecards, pricing and others, enhancing risk management and customer experience
for sustained success.
Dr Kushagra Jain is a Research Associate at the Financial Regulation Innovation Lab
(FRIL), Strathclyde Business School. His research interests include artificial
intelligence, machine learning, financial/regulatory technology, textual analysis,
international finance and risk management, among others. He is a recipient of
doctoral scholarships from the Financial Mathematics and Computation Cluster
(FMCC), Science Foundation Ireland (SFI), Higher Education Authority (HEA) and
Michael Smurfit Graduate Business School, University College Dublin (UCD).
Previously, he worked within wealth management and as a statutory auditor. He is
due to complete his doctoral studies in Finance from UCD in 2023, and obtained his MSc in Finance
from UCD, his Accounting Technician accreditation from the Institute of Chartered Accountants of India
and his undergraduate degree from Bangalore University. He is a FMCC Database Management Group
Data Manager, Research Assistant, PhD Representative and Teaching Assistant for undergraduate,
graduate and MBA programmes.
Professor Mark Cummins is Professor of Financial Technology at the
Strathclyde Business School, University of Strathclyde, where he leads the
FinTech Cluster as part of the university’s Technology and Innovation Zone
leadership and connection into the Glasgow City Innovation District. As part of
this role, he is driving collaboration between the FinTech Cluster and the other
strategic clusters identified by the University of Strathclyde, in particular the
Space, Quantum and Industrial Informatics Clusters. Professor Cummins is the
lead investigator at the University of Strathclyde on the newly funded (via UK
Government and Glasgow City Council) Financial Regulation Innovation Lab initiative, a novel industry
project under the leadership of FinTech Scotland and in collaboration with the University of Glasgow.
He previously held the posts of Professor of Finance at the Dublin City University (DCU) Business School
and Director of the Irish Institute of Digital Business. Professor Cummins has research interests in the
following areas: financial technology (FinTech), with particular interest in Explainable AI and Generative
AI; quantitative finance; energy and commodity finance; sustainable finance; model risk management.
Professor Cummins has over 50 publication outputs. He has published in leading international discipline
journals such as: European Journal of Operational Research; Journal of Money, Credit and Banking;
Journal of Banking and Finance; Journal of Financial Markets; Journal of Empirical Finance; and
International Review of Financial Analysis. Professor Cummins is co-editor of the open access Palgrave
title Disrupting Finance: Fintech and Strategy in the 21st Century. He is also co-author of the Wiley
Finance title Handbook of Multi-Commodity Markets and Products: Structuring, Trading and Risk
Management.
Financial Regulation Innovation Lab (FRIL) | 41

Dr James Bowden is Senior Lecturer in Financial Technology at Strathclyde Business
School, University of Strathclyde, where he is the programme director of the MSc
Financial Technology. Prior to this, he gained experience as a Knowledge Transfer
Partnership (KTP) Associate at Bangor Business School, and he has previous industry
experience within the global financial index team at FTSE Russell. Dr Bowden’s
research focusses on different areas of financial technology (FinTech), and his
published work involves the application of text analysis algorithms to financial
disclosures, news reporting, and social media. More recently he has been working on
projects incorporating audio analysis into existing financial text analysis models and investigating the
use cases of satellite imagery for the purpose of corporate environmental monitoring. Dr Bowden has
published in respected international journals, such as the European Journal of Finance, the Journal of
Comparative Economics, and the Journal of International Financial Markets, Institutions and Money.
He has also contributed chapters to books including “Disruptive Technology in Banking and Finance”,
published by Palgrave Macmillan. His commentary on financial events has previously been published in
The Conversation UK, the World Economic Forum, MarketWatch and Business Insider, and he has
appeared on international TV stations to discuss financial innovations such as non-fungible tokens
(NFTs).
Dr Godsway Korku Tetteh is a Knowledge Exchange Associate at the Fraser of
Allander Institute where he conducts economic evaluation of public sector
programmes and projects. Previously, he worked for the Financial Regulation
Innovation Lab as a Research Associate at the University of Strathclyde. His research
explores the impact of digital technologies and financial innovation (FinTech) on
welfare and private sector development. In addition to research, he has active
engagement with the policy community. He worked with the Cambridge Centre for Alternative Finance
to build the capacity of regulators and policymakers from across the globe in FinTech and regulatory
innovation. He shares his research insights with international development organisations. Godsway has
recently served as a panellist during the 3rd International Conference for Alternative Finance Research
to discuss alternative finance and financial inclusion. He has a Ph.D. in Economics from Maastricht
University and published in reputable journals such as Small Business Economics and World
Development.
Jackie (Zi Khang) Lin holds an MSc in Mathematical and Computational Finance
from the University of Oxford, graduating with Distinction in 2025. For his
dissertation, he developed a proof-of-concept data pipeline that processes raw,
granular datasets and applies Bayesian imputation to infer demographic labels,
followed by clustering techniques to identify distinct customer groups for
personalised financial insights. Before his MSc, Jackie earned a BA in Mathematics
from the University of Cambridge. He brings five years of experience in the asset
management industry, having served as a fixed income reserves portfolio manager at the Central Bank
of Malaysia. He is also a CFA charter holder. Jackie is currently working at a hedge fund in London.
Financial Regulation Innovation Lab (FRIL) | 42

Get in touch
FRIL@FinTechScotland.com
Financial Regulation Innovation Lab (FRIL) | 43