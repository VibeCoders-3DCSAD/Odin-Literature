---
conversion_metadata:
  converted_at: "2026-07-21T14:00:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li J..pdf"
  source_pdf_sha256: "be29e207bcee3ef3ddd5c912d089a2b5918805471b8316dc1a26eda3a457a9cb"
  page_count: 9
  markdown_char_count: 64438
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Computer, Signal, and System Research

Review 
Research on Personalized Asset Allocation Using AI Agents in 
Robo-Advisory Scenarios

Jialong Li 1,*

1  Ethic Inc., Jersey City, New Jersey, USA 
*  Correspondence: Jialong Li, Ethic Inc., Jersey City, New Jersey, USA

Abstract: This review paper provides a systematic review of personalized asset allocation facilitated 
by  AI  agents  within  robo-advisory  platforms.  Robo-advisors,  employing  algorithms  to  automate 
investment decisions, are increasingly incorporating sophisticated AI techniques to tailor portfolios 
to  individual  investor  needs  and  preferences.  This  paper  investigates  the  evolution  of  these  AI-
driven systems, examining key themes such as risk profiling, dynamic asset allocation strategies, 
and  the  integration  of  behavioral  finance  principles.  A  comparative  analysis  of  current 
methodologies  highlights  their  strengths  and  limitations,  particularly  concerning  transparency, 
explainability, and robustness in volatile market conditions. Furthermore, the review addresses the 
challenges associated with data privacy, regulatory compliance, and the potential for algorithmic 
bias.  By  synthesizing  current  research,  we  identify  promising  future  directions,  including  the 
development of more interpretable AI models, the incorporation of alternative data sources, and the 
creation  of  more  seamless  and  personalized  user  experiences.  This  review  aims  to  provide  a 
comprehensive  overview  of  the  current  landscape,  fostering  a  deeper  understanding  of  the 
opportunities  and  challenges  presented  by  AI-powered  personalized  asset  allocation  in  robo-
advisory contexts.

Keywords:  robo-advisory;  AI  agents;  personalized  asset  allocation;  algorithmic  investing; 
behavioral finance; machine learning; financial technology

1. Introduction

1.1. The Rise of Robo-Advisors and Personalized Investing

Robo-advisors have experienced remarkable growth in recent years, democratizing 
investment  management  by  offering  automated,  low-cost  services.  This  rise  reflects  a 
growing  demand  for  accessible  and  efficient  investment  solutions,  particularly  among 
digitally  native  generations.  However,  standard  robo-advisory  models  often  employ 
generalized  algorithms  that  may  not  adequately  address  the  unique  financial 
circumstances,  risk  tolerance,  and  investment  goals  of  each  individual.  Traditional 
investment approaches, relying on broad asset allocation strategies based on factors like 
age  and  risk  questionnaires,  frequently  fall  short  of  delivering  truly  personalized 
outcomes.  This  limitation motivates  the  development  of  more  sophisticated,  AI-driven 
personalization techniques capable of adapting to the dynamic needs and preferences of 
individual  investors,  ultimately  aiming  to  optimize  investment  performance  and 
satisfaction.  The  potential  benefits  of  personalized  asset  allocation  are  substantial, 
promising improved risk-adjusted returns and a more tailored investment experience [1].

1.2. Scope and Objectives of the Review

This review aims to delineate the current landscape of AI-driven personalized asset 
allocation  within  robo-advisory  contexts.  The  scope  encompasses  an  examination  of 
various  AI  techniques,  including  but  not  limited  to  machine  learning  algorithms,

168

Vol. 3 No. 2 (2026)

Received: 13 March 2026

Revised: 05 May 2026

Accepted: 20 May 2026

Published: 25 May 2026

Copyright:  ©   2026  by  the  authors.

Submitted  for  possible  open  access

publication  under  the  terms  and

conditions of the Creative Commons

Attribution

(CC

BY)

license

(https://creativecommons.org/license

s/by/4.0/).

---

<!-- PAGE 2 -->

Journal of Computer, Signal, and System Research

reinforcement  learning,  and  natural  language  processing,  used  to  tailor  investment 
strategies to individual investor profiles. Key research questions addressed include: How 
effectively do different AI agents capture investor risk preferences (𝑟) and financial goals 
(𝑔)? What  are the  prevailing methodologies for  dynamically adjusting asset  allocations 
based  on  market  conditions  ( 𝑚 )  and  investor  life  stages  ( 𝑡 )?  What  are  the  ethical 
considerations and regulatory challenges associated with deploying AI in personalized 
finance?  The  objective  is  to  provide  a  comprehensive  overview  that  identifies  research 
gaps and future directions in this rapidly evolving field [2].

2. Historical Overview of Robo-Advisory and AI in Finance

2.1. Early Robo-Advisors: Rule-Based Systems

Early attempts at automating financial reporting leveraged rule-based systems and 
expert systems (as shown in Table 1). These systems primarily relied on algorithms that 
mapped client risk profiles, often assessed through questionnaires, to corresponding asset 
allocations.  A  common  approach  involved  assigning  weights  to  different  asset  classes 
based  on  a  risk  score,  for  example,  allocating  a  higher  percentage  to  equities  for  risk-
tolerant investors. These early algorithms, while providing a low-cost and accessible entry 
point to investment management, suffered from limitations. They lacked the adaptability 
to dynamically adjust to changing market conditions or individual investor circumstances 
beyond the initial risk assessment. The simplicity of the rule-based approach also meant 
a  limited  capacity  to  incorporate  complex  financial  goals  or  sophisticated  investment 
strategies [3].

Table 1. Comparison of Early Robo-Advisory Models.

Feature 
Core Algorithm 
Risk Assessment

Asset Allocation

Dynamic Adjustment

Investment Strategy 
Complexity 
Cost

Description 
Rule-based, utilizing pre-defined algorithms. 
Primarily based on questionnaires and risk profiles. 
Maps risk score to asset class weights (e.g., higher equity allocation 
for risk-tolerant investors). 
Limited capability. Lacks adaptability to changing market 
conditions or individual circumstances beyond initial assessment. 
Simple strategies. Limited capacity to incorporate complex 
financial goals or sophisticated investment strategies. 
Low-cost entry point to investment management.

2.2. The Incorporation of Machine Learning

The  incorporation  of  machine  learning  marked  a  significant  evolution  in  robo-
advisory,  transitioning  from  rule-based  systems  to  data-driven  approaches.  Early 
applications focused on enhancing risk assessment and portfolio optimization. Machine 
learning algorithms enabled a more nuanced understanding of investor risk profiles by 
analyzing  a  wider  range  of  data  points  than  traditional  questionnaires.  For  instance, 
algorithms could predict risk tolerance based on behavioral data and investment patterns. 
In  portfolio  optimization,  techniques  like  regression  and  clustering  were  employed  to 
identify  optimal  asset  allocations  based  on  historical market  data  and  predicted  future 
performance.  This  allowed  for  the  creation  of  personalized  portfolios  tailored  to 
individual investor needs and risk preferences, aiming to maximize returns for a given 
level of risk  𝑟  [4].

2.3. AI Agents for Enhanced Personalization

The evolution of robo-advisory witnessed the  emergence  of AI agents designed to 
enhance  personalization  by  adapting  to  individual  investor  profiles  and  preferences. 
These  agents  leverage  algorithms  that  learn  from  user  behavior,  such  as  risk  tolerance 
questionnaires,  investment  choices,  and  portfolio  interactions.  Furthermore,  they

169

Vol. 3 No. 2 (2026)

---

<!-- PAGE 3 -->

Journal of Computer, Signal, and System Research

incorporate  market  dynamics,  including  historical  data  and  real-time  trends,  to  refine 
investment  strategies.  Key  advancements  include  the  development  of  reinforcement 
learning models that optimize  asset  allocation based on individual  𝑢𝑖’s utility function 
and  evolutionary  algorithms  that  explore  diverse  portfolio  compositions,  adapting  to 
changing  market  conditions  and  investor  𝑟𝑖  risk  appetite.  The  goal  is  to  move  beyond 
static, rule-based systems towards dynamic, personalized investment solutions (see Table 
2 for the integration timeline) [5].

Table 2. Timeline of AI Integration in Robo-Advisory.

Stage

AI Feature

Early Stage 
  2010-2015

Personalized AI 
Agents

Intermediate 
Stage 
  2016-2020 
Advanced 
Stage 
  2021-present

Enhanced Data 
Integration

Reinforcement 
Learning

Future Stage

Evolutionary 
Algorithms

Description 
Emergence of AI agents designed to adapt to 
individual investor profiles and preferences by 
learning from user behavior. 
Incorporation of market dynamics, including historical 
data and real-time trends, to refine investment 
strategies. 
Development of reinforcement learning models that 
optimize asset allocation based on individual  𝑢𝑖’s 
utility function. 
Exploration of diverse portfolio compositions, adapting 
to changing market conditions and investor  𝑟𝑖  risk 
appetite using evolutionary algorithms.

3. Core Theme A: Risk Profiling and Investor Segmentation Using AI

3.1. Traditional Risk Profiling Methods: Limitations

Traditional  risk  profiling  methods,  primarily  relying  on  questionnaires,  have  long 
been  the  cornerstone  of  investment  advisory.  These  questionnaires  typically  employ  a 
series  of  questions  designed  to  gauge  an  investor’s  risk  tolerance,  time  horizon, 
investment  knowledge,  and  financial  situation.  Based  on  the  responses,  investors  are 
categorized into predefined risk profiles, such as conservative, moderate, or aggressive. 
However, these methods suffer from several inherent limitations.

Firstly,  questionnaires  often  present  simplified  scenarios  that  fail  to  capture  the 
complexities of real-world investment decisions. The  static  nature of these  assessments 
struggles to reflect the dynamic and evolving nature of individual risk preferences, which 
can  be  influenced  by  market  conditions,  personal  circumstances,  and  emotional biases. 
Secondly, the subjective interpretation of questions and the potential for response bias can 
significantly skew the results. Investors may consciously or unconsciously misrepresent 
their true risk appetite, leading to inaccurate risk profile assignments. Furthermore,  the 
reliance on self-reported data neglects valuable behavioral insights that could be gleaned 
from actual investment behavior. Finally, the coarse granularity of predefined risk profiles 
often fails to adequately address the nuanced needs of individual investors, resulting in 
suboptimal asset allocation strategies that may not align with their specific financial goals 
and risk preferences. The  𝑅2  value of these models is often low, indicating a poor fit [6].

3.2. AI-Driven Risk Assessment: Deep Learning and NLP

Deep  learning  and  natural  language  processing  (NLP)  offer  powerful  tools  for 
enhancing risk assessment in robo-advisory. Traditional risk profiling often relies on static 
questionnaires, which may fail to capture the nuances of an investor’s true risk tolerance. 
AI,  particularly  deep  learning  models,  can  analyze  vast  datasets  of  investor  behavior, 
including transaction history, portfolio composition, and even website activity, to identify 
patterns indicative of risk preferences. For example, recurrent neural networks (RNNs) 
can be trained on time-series data of trading activity to predict an investor’s reaction to

170

Vol. 3 No. 2 (2026)

---

<!-- PAGE 4 -->

Journal of Computer, Signal, and System Research

market  volatility.  The  differences  between  these  AI-driven  approaches  and  traditional 
techniques are compared in Table 3.

Table 3. Comparison of Risk Profiling Methods.

Feature

Traditional Risk 
Profiling

Data Source

Static Questionnaires

Analysis Method

Rules-Based, Limited 
Statistical Analysis

Dynamic Capability

Static, Inflexible

Personalization

Data Type

Risk Preference 
Representation

Insight Extraction

Limited, Generalized 
Profiles 
Structured 
(Questionnaire 
Responses) 
Explicit Statements in 
Questionnaires 
Limited to 
Questionnaire 
Answers

Volatility Prediction

Limited

AI-Enhanced Risk Profiling

Questionnaires, Transaction History, 
Portfolio Composition, Website Activity, 
Investor Communication 
Deep Learning (e.g., RNNs), NLP 
(Sentiment Analysis, Topic Modeling) 
Dynamic, Adapts to Evolving Investor 
Behavior 
Highly Personalized, Tailored to Individual 
Investor Characteristics

Structured and Unstructured (Transaction 
Data, Text)

Function  𝑓(𝑥), where  𝑥  represents diverse 
data inputs 
Extracts Insights from Trading Activity, 
Communication (e.g., emotional state, 
investment goals) 
Uses RNNs on time-series data to predict 
reaction to market volatility

Furthermore, NLP techniques enable the extraction of valuable insights from textual 
data. Investors’ written communication, such as emails to advisors or responses to open-
ended questions, can be analyzed using sentiment analysis and topic modeling to gauge 
their  emotional  state  and  investment  goals.  This  allows  for  a  more  comprehensive 
understanding of their risk appetite beyond what is explicitly stated in questionnaires. For 
instance,  the  frequency  of  words  associated  with  anxiety  or  uncertainty  could  be 
correlated with a lower risk tolerance. The combination of deep learning and NLP allows 
for a more dynamic and personalized risk assessment, moving beyond static profiles to 
capture the evolving nature of investor risk preferences, represented as a function  𝑓(𝑥), 
where  𝑥  represents the diverse data inputs [4].

3.3. Investor Segmentation and Persona Creation

AI  algorithms  offer  sophisticated  methods  for  segmenting  investors  beyond 
traditional  demographic  classifications.  By  analyzing  vast  datasets  encompassing  risk 
tolerance  scores,  financial  goals  (e.g.,  retirement,  education,  wealth  accumulation), 
investment horizons (𝑡), and preferred asset classes, machine learning models can identify 
distinct  investor  groups.  Clustering  algorithms,  such  as  k-means  and  hierarchical 
clustering,  group  investors  with  similar  characteristics,  while  classification  models  can 
predict an investor’s segment based on their input data.

The resulting investor segments are then used to create detailed investor personas. 
Each persona represents a typical investor within a specific segment, characterized by a 
narrative description of their financial situation, risk appetite (𝑟), investment knowledge, 
and  aspirations.  These  personas  serve  as  archetypes  for  personalizing  investment 
strategies.  For  example,  a  “Conservative  Retiree”  persona  might  prioritize  capital 
preservation  and  income  generation,  leading  to  a  portfolio  heavily  weighted  in  bonds, 
while  an  “Aggressive  Young  Professional”  persona  might  favor  growth  stocks  and 
tolerate higher volatility in pursuit of long-term capital appreciation. The creation of these

171

Vol. 3 No. 2 (2026)

---

<!-- PAGE 5 -->

Journal of Computer, Signal, and System Research

personas allows robo-advisors to tailor investment recommendations and communication 
styles to resonate with individual investors, enhancing user engagement and satisfaction.

4. Core Theme B: Dynamic Asset Allocation and Portfolio Optimization

4.1. Static vs. Dynamic Asset Allocation

Static asset  allocation, a cornerstone  of traditional portfolio management, involves 
establishing  a  fixed  asset  mix  based  on  an  investor’s  risk  tolerance,  time  horizon,  and 
financial goals. This predetermined allocation remains constant over time, regardless of 
market fluctuations. For example, a portfolio might be set at 60% stocks and 40% bonds 
and  rebalanced  periodically  to  maintain  this  ratio.  The  primary  advantage  of  this 
approach lies in its simplicity and low transaction costs. However, it inherently assumes 
that  market  conditions  remain  relatively  stable  and  that  an  investor’s  needs  do  not 
significantly change.

Dynamic  asset  allocation,  conversely,  actively  adjusts  the  portfolio’s  asset  mix  in 
response to evolving market conditions and investor circumstances. This approach seeks 
to capitalize on perceived market inefficiencies and mitigate potential losses by shifting 
assets  between  different  classes.  For  instance,  if  economic  indicators  suggest  an 
impending recession, a dynamic strategy might reduce exposure to equities and increase 
holdings  in  safer  assets  like  government  bonds  or  cash.  The  potential  benefits  include 
enhanced returns and reduced risk compared to static allocation. Sophisticated algorithms 
and  AI  agents  can  play  a  crucial  role  in  identifying  these  opportunities  and  executing 
timely adjustments. However, dynamic allocation typically incurs higher transaction costs 
and  requires  more  sophisticated  monitoring  and  analysis.  Furthermore,  the  success  of 
dynamic  strategies  hinges  on  the  accuracy  of  market  predictions,  which  are  inherently 
uncertain. The  optimal  allocation at time  𝑡  can  be  represented  as  𝐴𝑡 = 𝑓(𝑀𝑡, 𝐼𝑡), where 
𝑀𝑡  represents market conditions and  𝐼𝑡  represents investor needs [7].

4.2. Reinforcement Learning for Adaptive Portfolios

Reinforcement  learning  (RL)  offers  a  powerful  framework  for  dynamic  asset 
allocation, enabling the creation of adaptive portfolios that respond to evolving market 
conditions. Unlike traditional methods that rely on historical data and pre-defined rules, 
RL  agents  learn  optimal  trading  strategies  through  direct  interaction  with  the  market 
environment. This interaction is modeled as a Markov Decision Process (MDP), where the 
agent observes the current state  𝑠𝑡(e.g., asset prices, economic indicators), takes an action 
𝑎𝑡(e.g., adjust portfolio weights), and receives a reward  𝑟𝑡  (e.g., portfolio return).

𝑇
𝑡=0

The agent’s objective  is to maximize  the  cumulative  discounted reward over time, 
represented  as  ∑ 𝛾𝑡
𝑟𝑡,  where  𝛾  is  a  discount  factor  that  weighs  immediate  rewards 
more heavily than future rewards. Through repeated interactions, the RL agent learns a 
policy  𝜋(𝑎𝑡|𝑠𝑡)  that maps states to actions, effectively determining the optimal portfolio 
allocation  strategy.  Various  RL  algorithms,  such  as  Q-learning,  SARSA,  and  Deep  Q-
Networks (DQN), can be employed to train these agents. The use of deep neural networks 
allows RL agents to handle high-dimensional state spaces and learn complex, non-linear 
relationships between market variables and optimal portfolio decisions. This adaptability 
makes RL a robust approach for navigating the complexities and uncertainties of financial 
markets [8].

4.3. Integrating Behavioral Finance Insights

Integrating  behavioral  finance  insights  into  AI-driven  asset  allocation  provides  a 
valuable  framework  for  enhancing  portfolio  performance  and  investor  satisfaction. 
Traditional  asset  allocation  models  often  assume  rational  investor  behavior,  neglecting 
the  pervasive  influence  of  cognitive  biases.  These  biases,  such  as  loss  aversion, 
confirmation bias, and anchoring, can lead to suboptimal investment decisions. AI agents, 
however, can be programmed to recognize and mitigate these biases (as summarized in 
Table 4).

172

Vol. 3 No. 2 (2026)

---

<!-- PAGE 6 -->

Journal of Computer, Signal, and System Research

Table 4. Behavioral Biases and Mitigation Strategies in AI Robo-Advisors.

Behavioral Bias

Loss Aversion

AI Mitigation Strategy 
AI prompts investor to reconsider 
strategy based on long-term goals, 
not short-term fluctuations.

Confirmation 
Bias

AI presents diverse perspectives and 
challenges pre-existing beliefs.

Anchoring

Overconfidence

Herding Bias

AI provides objective data and 
analysis to reframe investment 
decisions away from arbitrary 
anchors. 
AI provides realistic risk assessments 
and performance projections based 
on historical data and market 
analysis. 
AI emphasizes portfolio 
diversification and personalized risk 
tolerance, discouraging impulsive 
reactions to market trends.

Metrics/Quantification 
Bias Score  𝐵𝑠  representing 
influence of loss aversion on 
decision. 
Bias Score  𝐵𝑠  representing 
influence of confirmation bias on 
decision.

Bias Score  𝐵𝑠  representing 
influence of anchoring bias on 
decision.

Bias Score  𝐵𝑠  representing 
influence of overconfidence bias 
on decision.

Bias Score  𝐵𝑠  representing 
influence of herding bias on 
decision.

For example, an AI agent can be  trained to identify instances where  an investor is 
exhibiting loss aversion, prompting them to reconsider their investment strategy based on 
long-term goals rather than short-term market fluctuations. Similarly, AI can counteract 
confirmation bias by presenting investors with diverse perspectives and challenging their 
pre-existing  beliefs.  By  analyzing  investor  behavior  patterns  and  identifying  potential 
biases,  AI  can  provide  personalized  recommendations  that  promote  more  rational 
decision-making. The system can quantify the impact of biases using metrics like the bias 
score  𝐵𝑠, which represents the degree of influence a specific bias has on the investment 
decision. Furthermore, AI can dynamically adjust asset allocation based on an investor’s 
evolving risk profile and behavioral tendencies, leading to more robust and personalized 
portfolios [9].

5. Comparison of Methodologies and Challenges

5.1. Comparative Analysis of AI Algorithms

Different  AI  algorithms  offer  unique  approaches  to  personalized  asset  allocation. 
Deep learning models, particularly recurrent neural networks (RNNs), excel at capturing 
temporal dependencies in financial data, predicting market trends, and modeling investor 
risk  profiles.  However,  they  require  substantial  data  and  computational  resources. 
Reinforcement learning (RL) agents learn optimal allocation strategies through trial and 
error,  adapting  to  changing  market  conditions  and  individual  preferences.  RL’s 
exploration-exploitation  dilemma  and  sensitivity  to  reward  function  design  pose 
challenges. Genetic algorithms (GAs) offer a population-based approach, evolving asset 
allocation strategies over generations to optimize investor-specific objectives. GAs can be 
computationally  expensive  and  may  converge  to  suboptimal  solutions  if  not  carefully 
configured.  The  performance  of  each  algorithm  depends  heavily  on  data  quality, 
parameter tuning, and the specific investment scenario [10].

173

Vol. 3 No. 2 (2026)

---

<!-- PAGE 7 -->

Journal of Computer, Signal, and System Research

5.2. Transparency, Explainability, and Trust

A significant hurdle in deploying AI-driven investment systems lies in their inherent 
lack  of  transparency  and  explainability.  Many  advanced  algorithms,  particularly  deep 
learning models, operate as “black boxes,” making it difficult to understand how specific 
investment decisions are reached. This opacity erodes user trust, especially when dealing 
with sensitive financial matters. Building trust requires enhancing user understanding of 
the AI agent’s reasoning. Techniques like SHAP values or LIME can provide insights into 
feature importance, showing which factors most influence investment recommendations. 
Furthermore,  clear  communication  about  the  model’s  limitations  and  potential  risks  is 
crucial for fostering confidence and promoting responsible AI adoption in robo-advisory 
scenarios [11].

5.3. Data Privacy, Security, and Regulatory Compliance

The deployment of AI in personalized asset allocation raises significant data privacy 
and security concerns. Robo-advisors, handling sensitive financial data like income, assets 
(𝑎), and risk tolerance (𝑟), become attractive targets for cyberattacks. Protecting this data 
requires  robust  encryption,  access  controls,  and  continuous  monitoring.  Furthermore, 
compliance  with  regulations  like  GDPR  and  CCPA  is  crucial,  necessitating  transparent 
data  usage  policies  and  user  consent  mechanisms.  Ethical  considerations  also  demand 
fairness  and  non-discrimination  in  AI  algorithms,  preventing  biased  investment 
recommendations that could disproportionately affect certain demographic groups. These 
key challenges and their corresponding mitigation strategies are summarized in Table 5. 
Addressing these challenges is paramount for building trust and ensuring the responsible 
adoption of AI in robo-advisory services [12].

Table 5. Key Challenges and Mitigation Strategies.

Challenge

Data Privacy and 
Security

Cyberattacks Targeting 
Sensitive Data

Regulatory Compliance 
(GDPR, CCPA)

Ethical Concerns (Bias 
and Discrimination)

Lack of Trust in AI 
Recommendations

Mitigation Strategy 
Robust encryption of financial data (e.g., income, assets  𝑎, risk 
tolerance  𝑟); strict access controls; continuous security 
monitoring and threat detection. 
Implement multi-factor authentication; regularly update 
security protocols; conduct penetration testing; incident 
response plan. 
Develop transparent data usage policies; obtain explicit user 
consent for data collection and processing; establish data 
subject rights processes (e.g., right to access, right to be 
forgotten). 
Employ fairness-aware AI algorithms; regularly audit AI 
models for bias; use diverse training datasets; establish 
explainability and interpretability of AI decisions; independent 
ethics review board. 
Improve transparency in AI decision-making processes; 
provide clear explanations of investment recommendations; 
offer human advisor oversight to provide reassurance and 
address user concerns.

6. Future Perspectives

6.1. Emerging Trends in AI and Robo-Advisory

The  future  of  robo-advisory  is  inextricably  linked  to  advancements  in  artificial 
intelligence.  Federated  learning,  enabling  model  training  across  decentralized  datasets 
without  direct  data  sharing,  promises  enhanced  personalization  while  preserving  user 
privacy.  Explainable  AI  (XAI)  is  crucial  for  building  trust  and  ensuring  regulatory 
compliance  by  providing  transparent  justifications  for  algorithmic  recommendations.

174

Vol. 3 No. 2 (2026)

---

<!-- PAGE 8 -->

Journal of Computer, Signal, and System Research

Furthermore, the integration of alternative data sources, such as social media sentiment 
and  macroeconomic  indicators  ( 𝑥𝑖 ),  can  improve  predictive  accuracy  and  risk 
management.  These  trends  collectively  suggest  a  future  where  robo-advisors  are  more 
personalized, transparent, and robust, offering sophisticated financial advice accessible to 
a wider audience.

6.2. The Future of Personalized Investment

The future of personalized investment envisions AI agents evolving into proactive 
financial partners. Hyper-personalization will become the norm, with algorithms deeply 
understanding individual risk tolerance, financial goals, and even psychological biases. 
Investment  strategies  will  dynamically  adapt  to  life  events,  market  fluctuations,  and 
evolving preferences, moving beyond static risk profiles. AI agents will anticipate future 
needs,  proactively  suggesting  adjustments  to  asset  allocations  and  financial  plans. 
Imagine a system that not only manages investments but also optimizes spending, debt 
management,  and 
individual’s  unique 
insurance  coverage,  all  tailored  to  the 
circumstances and maximizing their long-term financial well-being [12].

7. Conclusion

This review highlights significant progress in AI-driven personalized asset allocation 
within robo-advisory. AI agents, leveraging techniques like reinforcement learning and 
deep  learning,  demonstrate  the  ability  to  adapt  asset  allocations  to  individual  investor 
profiles,  considering  factors  such  as  risk  tolerance  ( 𝑟 ),  investment  horizon  ( 𝑡 ),  and 
financial goals (𝑔). Our analysis reveals improved portfolio performance, particularly in 
volatile  markets,  compared  to  traditional  rule-based  approaches.  However,  challenges 
remain  in  addressing  issues  like  explainability,  bias  mitigation  in  training  data,  and 
ensuring robustness across diverse market conditions. Further research is needed to build 
trust and enhance the practical applicability of these AI-powered systems.

AI agents hold immense potential to revolutionize robo-advisory services, offering 
personalized asset  allocation strategies tailored to individual risk profiles and financial 
goals.  By  leveraging  sophisticated  algorithms  and  machine  learning  techniques,  these 
agents  can  adapt  to  changing  market  conditions  and  investor  preferences,  potentially 
leading  to  improved  investment  outcomes  compared  to  traditional,  static  approaches. 
Future research should focus on addressing challenges related to explainability and trust 
in AI-driven investment decisions.

References 
1.

J.  P.  Shetty,  P.  Singh,  and  S.  Verma,  “Robo-Advisors  in  Financial  Services:  Redefining  Wealth  Management  in  the  Age  of 
Artificial Intelligence,” Finance Research Open, 100090, 2026. 
S. K. Abbas, “AI Meets Finance: The Rise of AI-Powered Robo-Advisors,” J. Electrical Systems, vol. 20, no. 11, pp. 1011-1016, 
2024.

2.

3.  R. Feng, H. Li, and M. Liu, “Robo-Advisors Beyond Automation: Principles and Roadmap for AI-Driven Financial Planning,”

arXiv preprint arXiv:2509.09922, 2025.

4.  Z.  Shen,  Z.  Wang,  J.  Chew,  K.  Hu,  and  Y.  Wang,  “Artificial  intelligence  empowering  robo-advisors:  A  data-driven  wealth

management model analysis,” Int. J. Management Science Research, vol. 8, no. 3, pp. 1-12, 2025.

5.  M. Tahvildari, “Integrating generative AI in Robo-Advisory: A systematic review of opportunities, challenges, and strategic

solutions,” Multidisciplinary Reviews, vol. 8, no. 12, pp. 2025379-2025379, 2025.

6.  H. Zhu, Understanding Customers in AI-empowered Financial Advisory Systems and Services: An interdisciplinary study of

Robo-advisors, Doctoral dissertation, KTH Royal Institute of Technology, 2023.

7.  A. Litty, “Explainable AI for Personalized Financial Advice: Building Trust and Transparency in Robo-Advisory Platforms,”

8.

Working Paper, 2024. 
F.  Khosravi,  “Transforming  Investment  Advisory  Services  Through  Artificial  Intelligence:  A  Study  on  Robo-Advisors  and 
Algorithmic Portfolio Management,” Nuvern Applied Science Reviews, vol. 8, no. 9, pp. 1-8, 2024.

9.  M. Rizinski and D. Trajanov, “AI Agents in Finance and Fintech: A Scientific Review of Agent-Based Systems, Applications,

and Future Horizons,” Computers, Materials and Continua, vol. 86, no. 1, pp. 1-34, 2025.

10.  F. Akhtar, S. Akhtar, and M. Laeeq, “Evolution of Robo‐Advisors: A Literature Review and Future Research Agenda,”  Int. J.

Consumer Studies, vol. 49, no. 6, e70131, 2025.

175

Vol. 3 No. 2 (2026)

---

<!-- PAGE 9 -->

Journal of Computer, Signal, and System Research

11.  S.  Bhardwaj,  “Artiﬁcial  Intelligence  in  Wealth  Management:  Transforming  the  Future  of  Financial  Advisory  Services,”  J.

Multidisciplinary Knowledge, vol. 5, no. 2, pp. 85-96, 2025.

12.  S.  B.  Koneti,  “Artificial  intelligence  Applications  in  Retail  and  Investment  Banking:  Personalization,  Robo-Advisory  and 
Behavioral Analytics,” Artificial Intelligence-Powered Finance: Algorithms, Analytics, and Automation for the Next Financial Revolution, 
vol. 4, p. 72, 2025.

Disclaimer/Publisher’s  Note:  The  statements,  opinions  and  data  contained  in  all  publications  are  solely  those  of  the  individual 
author(s) and contributor(s) and not of GBP and/or the editor(s). GBP and/or the editor(s) disclaim responsibility for any injury to 
people or property resulting from any ideas, methods, instructions or products referred to in the content.

176

Vol. 3 No. 2 (2026)

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Computer, Signal, and System Research
Review
Research on Personalized Asset Allocation Using AI Agents in
Robo-Advisory Scenarios
Jialong Li 1,*
1 Ethic Inc., Jersey City, New Jersey, USA
* Correspondence: Jialong Li, Ethic Inc., Jersey City, New Jersey, USA
Abstract: This review paper provides a systematic review of personalized asset allocation facilitated
by AI agents within robo-advisory platforms. Robo-advisors, employing algorithms to automate
investment decisions, are increasingly incorporating sophisticated AI techniques to tailor portfolios
to individual investor needs and preferences. This paper investigates the evolution of these AI-
driven systems, examining key themes such as risk profiling, dynamic asset allocation strategies,
and the integration of behavioral finance principles. A comparative analysis of current
methodologies highlights their strengths and limitations, particularly concerning transparency,
explainability, and robustness in volatile market conditions. Furthermore, the review addresses the
challenges associated with data privacy, regulatory compliance, and the potential for algorithmic
bias. By synthesizing current research, we identify promising future directions, including the
development of more interpretable AI models, the incorporation of alternative data sources, and the
creation of more seamless and personalized user experiences. This review aims to provide a
comprehensive overview of the current landscape, fostering a deeper understanding of the
opportunities and challenges presented by AI-powered personalized asset allocation in robo-
advisory contexts.
Keywords: robo-advisory; AI agents; personalized asset allocation; algorithmic investing;
behavioral finance; machine learning; financial technology
1. Introduction
1.1. The Rise of Robo-Advisors and Personalized Investing
Robo-advisors have experienced remarkable growth in recent years, democratizing
investment management by offering automated, low-cost services. This rise reflects a
Received: 13 March 2026
growing demand for accessible and efficient investment solutions, particularly among
Revised: 05 May 2026
digitally native generations. However, standard robo-advisory models often employ
Accepted: 20 May 2026
generalized algorithms that may not adequately address the unique financial
Published: 25 May 2026
circumstances, risk tolerance, and investment goals of each individual. Traditional
investment approaches, relying on broad asset allocation strategies based on factors like
age and risk questionnaires, frequently fall short of delivering truly personalized
Copyright: © 2026 by the authors.
outcomes. This limitation motivates the development of more sophisticated, AI-driven
Submitted for possible open access
personalization techniques capable of adapting to the dynamic needs and preferences of
publication under the terms and
individual investors, ultimately aiming to optimize investment performance and
conditions of the Creative Commons
satisfaction. The potential benefits of personalized asset allocation are substantial,
Attribution (CC BY) license
promising improved risk-adjusted returns and a more tailored investment experience [1].
(https://creativecommons.org/license
s/by/4.0/).
1.2. Scope and Objectives of the Review
This review aims to delineate the current landscape of AI-driven personalized asset
allocation within robo-advisory contexts. The scope encompasses an examination of
various AI techniques, including but not limited to machine learning algorithms,
168 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
reinforcement learning, and natural language processing, used to tailor investment
strategies to individual investor profiles. Key research questions addressed include: How
effectively do different AI agents capture investor risk preferences (𝑟) and financial goals
(𝑔)? What are the prevailing methodologies for dynamically adjusting asset allocations
based on market conditions (𝑚) and investor life stages (𝑡)? What are the ethical
considerations and regulatory challenges associated with deploying AI in personalized
finance? The objective is to provide a comprehensive overview that identifies research
gaps and future directions in this rapidly evolving field [2].
2. Historical Overview of Robo-Advisory and AI in Finance
2.1. Early Robo-Advisors: Rule-Based Systems
Early attempts at automating financial reporting leveraged rule-based systems and
expert systems (as shown in Table 1). These systems primarily relied on algorithms that
mapped client risk profiles, often assessed through questionnaires, to corresponding asset
allocations. A common approach involved assigning weights to different asset classes
based on a risk score, for example, allocating a higher percentage to equities for risk-
tolerant investors. These early algorithms, while providing a low-cost and accessible entry
point to investment management, suffered from limitations. They lacked the adaptability
to dynamically adjust to changing market conditions or individual investor circumstances
beyond the initial risk assessment. The simplicity of the rule-based approach also meant
a limited capacity to incorporate complex financial goals or sophisticated investment
strategies [3].
Table 1. Comparison of Early Robo-Advisory Models.
Feature Description
Core Algorithm Rule-based, utilizing pre-defined algorithms.
Risk Assessment Primarily based on questionnaires and risk profiles.
Maps risk score to asset class weights (e.g., higher equity allocation
Asset Allocation
for risk-tolerant investors).
Limited capability. Lacks adaptability to changing market
Dynamic Adjustment
conditions or individual circumstances beyond initial assessment.
Investment Strategy Simple strategies. Limited capacity to incorporate complex
Complexity financial goals or sophisticated investment strategies.
Cost Low-cost entry point to investment management.
2.2. The Incorporation of Machine Learning
The incorporation of machine learning marked a significant evolution in robo-
advisory, transitioning from rule-based systems to data-driven approaches. Early
applications focused on enhancing risk assessment and portfolio optimization. Machine
learning algorithms enabled a more nuanced understanding of investor risk profiles by
analyzing a wider range of data points than traditional questionnaires. For instance,
algorithms could predict risk tolerance based on behavioral data and investment patterns.
In portfolio optimization, techniques like regression and clustering were employed to
identify optimal asset allocations based on historical market data and predicted future
performance. This allowed for the creation of personalized portfolios tailored to
individual investor needs and risk preferences, aiming to maximize returns for a given
level of risk 𝑟 [4].
2.3. AI Agents for Enhanced Personalization
The evolution of robo-advisory witnessed the emergence of AI agents designed to
enhance personalization by adapting to individual investor profiles and preferences.
These agents leverage algorithms that learn from user behavior, such as risk tolerance
questionnaires, investment choices, and portfolio interactions. Furthermore, they
169 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
incorporate market dynamics, including historical data and real-time trends, to refine
investment strategies. Key advancements include the development of reinforcement
learning models that optimize asset allocation based on individual 𝑢 ’s utility function
𝑖
and evolutionary algorithms that explore diverse portfolio compositions, adapting to
changing market conditions and investor 𝑟 risk appetite. The goal is to move beyond
𝑖
static, rule-based systems towards dynamic, personalized investment solutions (see Table
2 for the integration timeline) [5].
Table 2. Timeline of AI Integration in Robo-Advisory.
Stage AI Feature Description
Emergence of AI agents designed to adapt to
Early Stage Personalized AI
individual investor profiles and preferences by
2010-2015 Agents
learning from user behavior.
Intermediate Incorporation of market dynamics, including historical
Enhanced Data
Stage data and real-time trends, to refine investment
Integration
2016-2020 strategies.
Advanced Development of reinforcement learning models that
Reinforcement
Stage optimize asset allocation based on individual 𝑢 ’s
Learning 𝑖
2021-present utility function.
Exploration of diverse portfolio compositions, adapting
Evolutionary
Future Stage to changing market conditions and investor 𝑟 risk
𝑖
Algorithms
appetite using evolutionary algorithms.
3. Core Theme A: Risk Profiling and Investor Segmentation Using AI
3.1. Traditional Risk Profiling Methods: Limitations
Traditional risk profiling methods, primarily relying on questionnaires, have long
been the cornerstone of investment advisory. These questionnaires typically employ a
series of questions designed to gauge an investor’s risk tolerance, time horizon,
investment knowledge, and financial situation. Based on the responses, investors are
categorized into predefined risk profiles, such as conservative, moderate, or aggressive.
However, these methods suffer from several inherent limitations.
Firstly, questionnaires often present simplified scenarios that fail to capture the
complexities of real-world investment decisions. The static nature of these assessments
struggles to reflect the dynamic and evolving nature of individual risk preferences, which
can be influenced by market conditions, personal circumstances, and emotional biases.
Secondly, the subjective interpretation of questions and the potential for response bias can
significantly skew the results. Investors may consciously or unconsciously misrepresent
their true risk appetite, leading to inaccurate risk profile assignments. Furthermore, the
reliance on self-reported data neglects valuable behavioral insights that could be gleaned
from actual investment behavior. Finally, the coarse granularity of predefined risk profiles
often fails to adequately address the nuanced needs of individual investors, resulting in
suboptimal asset allocation strategies that may not align with their specific financial goals
and risk preferences. The 𝑅2 value of these models is often low, indicating a poor fit [6].
3.2. AI-Driven Risk Assessment: Deep Learning and NLP
Deep learning and natural language processing (NLP) offer powerful tools for
enhancing risk assessment in robo-advisory. Traditional risk profiling often relies on static
questionnaires, which may fail to capture the nuances of an investor’s true risk tolerance.
AI, particularly deep learning models, can analyze vast datasets of investor behavior,
including transaction history, portfolio composition, and even website activity, to identify
patterns indicative of risk preferences. For example, recurrent neural networks (RNNs)
can be trained on time-series data of trading activity to predict an investor’s reaction to
170 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
market volatility. The differences between these AI-driven approaches and traditional
techniques are compared in Table 3.
Table 3. Comparison of Risk Profiling Methods.
Traditional Risk
Feature AI-Enhanced Risk Profiling
Profiling
Questionnaires, Transaction History,
Data Source Static Questionnaires Portfolio Composition, Website Activity,
Investor Communication
Rules-Based, Limited Deep Learning (e.g., RNNs), NLP
Analysis Method
Statistical Analysis (Sentiment Analysis, Topic Modeling)
Dynamic, Adapts to Evolving Investor
Dynamic Capability Static, Inflexible
Behavior
Limited, Generalized Highly Personalized, Tailored to Individual
Personalization
Profiles Investor Characteristics
Structured
Structured and Unstructured (Transaction
Data Type (Questionnaire
Data, Text)
Responses)
Risk Preference Explicit Statements in Function 𝑓(𝑥), where 𝑥 represents diverse
Representation Questionnaires data inputs
Limited to Extracts Insights from Trading Activity,
Insight Extraction Questionnaire Communication (e.g., emotional state,
Answers investment goals)
Uses RNNs on time-series data to predict
Volatility Prediction Limited
reaction to market volatility
Furthermore, NLP techniques enable the extraction of valuable insights from textual
data. Investors’ written communication, such as emails to advisors or responses to open-
ended questions, can be analyzed using sentiment analysis and topic modeling to gauge
their emotional state and investment goals. This allows for a more comprehensive
understanding of their risk appetite beyond what is explicitly stated in questionnaires. For
instance, the frequency of words associated with anxiety or uncertainty could be
correlated with a lower risk tolerance. The combination of deep learning and NLP allows
for a more dynamic and personalized risk assessment, moving beyond static profiles to
capture the evolving nature of investor risk preferences, represented as a function 𝑓(𝑥),
where 𝑥 represents the diverse data inputs [4].
3.3. Investor Segmentation and Persona Creation
AI algorithms offer sophisticated methods for segmenting investors beyond
traditional demographic classifications. By analyzing vast datasets encompassing risk
tolerance scores, financial goals (e.g., retirement, education, wealth accumulation),
investment horizons (𝑡), and preferred asset classes, machine learning models can identify
distinct investor groups. Clustering algorithms, such as k-means and hierarchical
clustering, group investors with similar characteristics, while classification models can
predict an investor’s segment based on their input data.
The resulting investor segments are then used to create detailed investor personas.
Each persona represents a typical investor within a specific segment, characterized by a
narrative description of their financial situation, risk appetite (𝑟), investment knowledge,
and aspirations. These personas serve as archetypes for personalizing investment
strategies. For example, a “Conservative Retiree” persona might prioritize capital
preservation and income generation, leading to a portfolio heavily weighted in bonds,
while an “Aggressive Young Professional” persona might favor growth stocks and
tolerate higher volatility in pursuit of long-term capital appreciation. The creation of these
171 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
personas allows robo-advisors to tailor investment recommendations and communication
styles to resonate with individual investors, enhancing user engagement and satisfaction.
4. Core Theme B: Dynamic Asset Allocation and Portfolio Optimization
4.1. Static vs. Dynamic Asset Allocation
Static asset allocation, a cornerstone of traditional portfolio management, involves
establishing a fixed asset mix based on an investor’s risk tolerance, time horizon, and
financial goals. This predetermined allocation remains constant over time, regardless of
market fluctuations. For example, a portfolio might be set at 60% stocks and 40% bonds
and rebalanced periodically to maintain this ratio. The primary advantage of this
approach lies in its simplicity and low transaction costs. However, it inherently assumes
that market conditions remain relatively stable and that an investor’s needs do not
significantly change.
Dynamic asset allocation, conversely, actively adjusts the portfolio’s asset mix in
response to evolving market conditions and investor circumstances. This approach seeks
to capitalize on perceived market inefficiencies and mitigate potential losses by shifting
assets between different classes. For instance, if economic indicators suggest an
impending recession, a dynamic strategy might reduce exposure to equities and increase
holdings in safer assets like government bonds or cash. The potential benefits include
enhanced returns and reduced risk compared to static allocation. Sophisticated algorithms
and AI agents can play a crucial role in identifying these opportunities and executing
timely adjustments. However, dynamic allocation typically incurs higher transaction costs
and requires more sophisticated monitoring and analysis. Furthermore, the success of
dynamic strategies hinges on the accuracy of market predictions, which are inherently
uncertain. The optimal allocation at time 𝑡 can be represented as 𝐴 =𝑓(𝑀 ,𝐼 ), where
𝑡 𝑡 𝑡
𝑀 represents market conditions and 𝐼 represents investor needs [7].
𝑡 𝑡
4.2. Reinforcement Learning for Adaptive Portfolios
Reinforcement learning (RL) offers a powerful framework for dynamic asset
allocation, enabling the creation of adaptive portfolios that respond to evolving market
conditions. Unlike traditional methods that rely on historical data and pre-defined rules,
RL agents learn optimal trading strategies through direct interaction with the market
environment. This interaction is modeled as a Markov Decision Process (MDP), where the
agent observes the current state 𝑠 (e.g., asset prices, economic indicators), takes an action
𝑡
𝑎 (e.g., adjust portfolio weights), and receives a reward 𝑟 (e.g., portfolio return).
𝑡 𝑡
The agent’s objective is to maximize the cumulative discounted reward over time,
represented as ∑𝑇 𝛾𝑡𝑟, where 𝛾 is a discount factor that weighs immediate rewards
𝑡=0 𝑡
more heavily than future rewards. Through repeated interactions, the RL agent learns a
policy 𝜋(𝑎 |𝑠 ) that maps states to actions, effectively determining the optimal portfolio
𝑡 𝑡
allocation strategy. Various RL algorithms, such as Q-learning, SARSA, and Deep Q-
Networks (DQN), can be employed to train these agents. The use of deep neural networks
allows RL agents to handle high-dimensional state spaces and learn complex, non-linear
relationships between market variables and optimal portfolio decisions. This adaptability
makes RL a robust approach for navigating the complexities and uncertainties of financial
markets [8].
4.3. Integrating Behavioral Finance Insights
Integrating behavioral finance insights into AI-driven asset allocation provides a
valuable framework for enhancing portfolio performance and investor satisfaction.
Traditional asset allocation models often assume rational investor behavior, neglecting
the pervasive influence of cognitive biases. These biases, such as loss aversion,
confirmation bias, and anchoring, can lead to suboptimal investment decisions. AI agents,
however, can be programmed to recognize and mitigate these biases (as summarized in
Table 4).
172 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research

Table 4. Behavioral Biases and Mitigation Strategies in AI Robo-Advisors.
Behavioral Bias  AI Mitigation Strategy  Metrics/Quantification
|     |     | AI prompts investor to reconsider  | Bias Score 𝐵 |  representing  |
| --- | --- | ---------------------------------- | ------------ | -------------- |
𝑠
Loss Aversion  strategy based on long-term goals,  influence of loss aversion on
|     |               | not short-term fluctuations.          |              | decision.      |
| --- | ------------- | ------------------------------------- | ------------ | -------------- |
|     |               |                                       | Bias Score 𝐵 |  representing  |
|     | Confirmation  | AI presents diverse perspectives and  |              | 𝑠              |
influence of confirmation bias on
|     | Bias  | challenges pre-existing beliefs.  |     |     |
| --- | ----- | --------------------------------- | --- | --- |
decision.
AI provides objective data and
|     |     |     | Bias Score 𝐵 |  representing  |
| --- | --- | --- | ------------ | -------------- |
𝑠
analysis to reframe investment
|     | Anchoring  |     | influence of anchoring bias on  |     |
| --- | ---------- | --- | ------------------------------- | --- |
decisions away from arbitrary
decision.
anchors.
AI provides realistic risk assessments
|     |     |     | Bias Score 𝐵 |  representing  |
| --- | --- | --- | ------------ | -------------- |
𝑠
and performance projections based
|     | Overconfidence  |     | influence of overconfidence bias  |     |
| --- | --------------- | --- | --------------------------------- | --- |
on historical data and market
on decision.
analysis.
AI emphasizes portfolio
|     |               |                                        | Bias Score 𝐵                  |  representing  |
| --- | ------------- | -------------------------------------- | ----------------------------- | -------------- |
|     |               | diversification and personalized risk  |                               | 𝑠              |
|     | Herding Bias  |                                        | influence of herding bias on  |                |
tolerance, discouraging impulsive
decision.
reactions to market trends.
For example, an AI agent can be trained to identify instances where an investor is
exhibiting loss aversion, prompting them to reconsider their investment strategy based on
long-term goals rather than short-term market fluctuations. Similarly, AI can counteract
confirmation bias by presenting investors with diverse perspectives and challenging their
pre-existing beliefs. By analyzing investor behavior patterns and identifying potential
biases,  AI  can  provide  personalized  recommendations  that  promote  more  rational
decision-making. The system can quantify the impact of biases using metrics like the bias
score 𝐵
𝑠 , which represents the degree of influence a specific bias has on the investment
decision. Furthermore, AI can dynamically adjust asset allocation based on an investor’s
evolving risk profile and behavioral tendencies, leading to more robust and personalized
portfolios [9].
5. Comparison of Methodologies and Challenges
5.1. Comparative Analysis of AI Algorithms
Different AI algorithms offer unique approaches to personalized asset allocation.
Deep learning models, particularly recurrent neural networks (RNNs), excel at capturing
temporal dependencies in financial data, predicting market trends, and modeling investor
risk  profiles.  However,  they  require  substantial  data  and  computational  resources.
Reinforcement learning (RL) agents learn optimal allocation strategies through trial and
error,  adapting  to  changing  market  conditions  and  individual  preferences.  RL’s
exploration-exploitation  dilemma  and  sensitivity  to  reward  function  design  pose
challenges. Genetic algorithms (GAs) offer a population-based approach, evolving asset
allocation strategies over generations to optimize investor-specific objectives. GAs can be
computationally expensive and may converge to suboptimal solutions if not carefully
configured.  The  performance  of  each  algorithm  depends  heavily  on  data  quality,
parameter tuning, and the specific investment scenario [10].
|     |     |      |     |                      |
| --- | --- | ---- | --- | -------------------- |
|     |     | 173  |     | Vol. 3 No. 2 (2026)  |

Journal of Computer, Signal, and System Research
5.2. Transparency, Explainability, and Trust
A significant hurdle in deploying AI-driven investment systems lies in their inherent
lack of transparency and explainability. Many advanced algorithms, particularly deep
learning models, operate as “black boxes,” making it difficult to understand how specific
investment decisions are reached. This opacity erodes user trust, especially when dealing
with sensitive financial matters. Building trust requires enhancing user understanding of
the AI agent’s reasoning. Techniques like SHAP values or LIME can provide insights into
feature importance, showing which factors most influence investment recommendations.
Furthermore, clear communication about the model’s limitations and potential risks is
crucial for fostering confidence and promoting responsible AI adoption in robo-advisory
scenarios [11].
5.3. Data Privacy, Security, and Regulatory Compliance
The deployment of AI in personalized asset allocation raises significant data privacy
and security concerns. Robo-advisors, handling sensitive financial data like income, assets
(𝑎), and risk tolerance (𝑟), become attractive targets for cyberattacks. Protecting this data
requires robust encryption, access controls, and continuous monitoring. Furthermore,
compliance with regulations like GDPR and CCPA is crucial, necessitating transparent
data usage policies and user consent mechanisms. Ethical considerations also demand
fairness and non-discrimination in AI algorithms, preventing biased investment
recommendations that could disproportionately affect certain demographic groups. These
key challenges and their corresponding mitigation strategies are summarized in Table 5.
Addressing these challenges is paramount for building trust and ensuring the responsible
adoption of AI in robo-advisory services [12].
Table 5. Key Challenges and Mitigation Strategies.
Challenge Mitigation Strategy
Robust encryption of financial data (e.g., income, assets 𝑎, risk
Data Privacy and
tolerance 𝑟); strict access controls; continuous security
Security
monitoring and threat detection.
Implement multi-factor authentication; regularly update
Cyberattacks Targeting
security protocols; conduct penetration testing; incident
Sensitive Data
response plan.
Develop transparent data usage policies; obtain explicit user
Regulatory Compliance consent for data collection and processing; establish data
(GDPR, CCPA) subject rights processes (e.g., right to access, right to be
forgotten).
Employ fairness-aware AI algorithms; regularly audit AI
Ethical Concerns (Bias models for bias; use diverse training datasets; establish
and Discrimination) explainability and interpretability of AI decisions; independent
ethics review board.
Improve transparency in AI decision-making processes;
Lack of Trust in AI provide clear explanations of investment recommendations;
Recommendations offer human advisor oversight to provide reassurance and
address user concerns.
6. Future Perspectives
6.1. Emerging Trends in AI and Robo-Advisory
The future of robo-advisory is inextricably linked to advancements in artificial
intelligence. Federated learning, enabling model training across decentralized datasets
without direct data sharing, promises enhanced personalization while preserving user
privacy. Explainable AI (XAI) is crucial for building trust and ensuring regulatory
compliance by providing transparent justifications for algorithmic recommendations.
174 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
Furthermore, the integration of alternative data sources, such as social media sentiment
and macroeconomic indicators ( 𝑥 ), can improve predictive accuracy and risk
𝑖
management. These trends collectively suggest a future where robo-advisors are more
personalized, transparent, and robust, offering sophisticated financial advice accessible to
a wider audience.
6.2. The Future of Personalized Investment
The future of personalized investment envisions AI agents evolving into proactive
financial partners. Hyper-personalization will become the norm, with algorithms deeply
understanding individual risk tolerance, financial goals, and even psychological biases.
Investment strategies will dynamically adapt to life events, market fluctuations, and
evolving preferences, moving beyond static risk profiles. AI agents will anticipate future
needs, proactively suggesting adjustments to asset allocations and financial plans.
Imagine a system that not only manages investments but also optimizes spending, debt
management, and insurance coverage, all tailored to the individual’s unique
circumstances and maximizing their long-term financial well-being [12].
7. Conclusion
This review highlights significant progress in AI-driven personalized asset allocation
within robo-advisory. AI agents, leveraging techniques like reinforcement learning and
deep learning, demonstrate the ability to adapt asset allocations to individual investor
profiles, considering factors such as risk tolerance (𝑟), investment horizon (𝑡), and
financial goals (𝑔). Our analysis reveals improved portfolio performance, particularly in
volatile markets, compared to traditional rule-based approaches. However, challenges
remain in addressing issues like explainability, bias mitigation in training data, and
ensuring robustness across diverse market conditions. Further research is needed to build
trust and enhance the practical applicability of these AI-powered systems.
AI agents hold immense potential to revolutionize robo-advisory services, offering
personalized asset allocation strategies tailored to individual risk profiles and financial
goals. By leveraging sophisticated algorithms and machine learning techniques, these
agents can adapt to changing market conditions and investor preferences, potentially
leading to improved investment outcomes compared to traditional, static approaches.
Future research should focus on addressing challenges related to explainability and trust
in AI-driven investment decisions.
References
1. J. P. Shetty, P. Singh, and S. Verma, “Robo-Advisors in Financial Services: Redefining Wealth Management in the Age of
Artificial Intelligence,” Finance Research Open, 100090, 2026.
2. S. K. Abbas, “AI Meets Finance: The Rise of AI-Powered Robo-Advisors,” J. Electrical Systems, vol. 20, no. 11, pp. 1011-1016,
2024.
3. R. Feng, H. Li, and M. Liu, “Robo-Advisors Beyond Automation: Principles and Roadmap for AI-Driven Financial Planning,”
arXiv preprint arXiv:2509.09922, 2025.
4. Z. Shen, Z. Wang, J. Chew, K. Hu, and Y. Wang, “Artificial intelligence empowering robo-advisors: A data-driven wealth
management model analysis,” Int. J. Management Science Research, vol. 8, no. 3, pp. 1-12, 2025.
5. M. Tahvildari, “Integrating generative AI in Robo-Advisory: A systematic review of opportunities, challenges, and strategic
solutions,” Multidisciplinary Reviews, vol. 8, no. 12, pp. 2025379-2025379, 2025.
6. H. Zhu, Understanding Customers in AI-empowered Financial Advisory Systems and Services: An interdisciplinary study of
Robo-advisors, Doctoral dissertation, KTH Royal Institute of Technology, 2023.
7. A. Litty, “Explainable AI for Personalized Financial Advice: Building Trust and Transparency in Robo-Advisory Platforms,”
Working Paper, 2024.
8. F. Khosravi, “Transforming Investment Advisory Services Through Artificial Intelligence: A Study on Robo-Advisors and
Algorithmic Portfolio Management,” Nuvern Applied Science Reviews, vol. 8, no. 9, pp. 1-8, 2024.
9. M. Rizinski and D. Trajanov, “AI Agents in Finance and Fintech: A Scientific Review of Agent-Based Systems, Applications,
and Future Horizons,” Computers, Materials and Continua, vol. 86, no. 1, pp. 1-34, 2025.
10. F. Akhtar, S. Akhtar, and M. Laeeq, “Evolution of Robo‐Advisors: A Literature Review and Future Research Agenda,” Int. J.
Consumer Studies, vol. 49, no. 6, e70131, 2025.
175 Vol. 3 No. 2 (2026)

Journal of Computer, Signal, and System Research
11. S. Bhardwaj, “Artificial Intelligence in Wealth Management: Transforming the Future of Financial Advisory Services,” J.
Multidisciplinary Knowledge, vol. 5, no. 2, pp. 85-96, 2025.
12. S. B. Koneti, “Artificial intelligence Applications in Retail and Investment Banking: Personalization, Robo-Advisory and
Behavioral Analytics,” Artificial Intelligence-Powered Finance: Algorithms, Analytics, and Automation for the Next Financial Revolution,
vol. 4, p. 72, 2025.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of GBP and/or the editor(s). GBP and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
176 Vol. 3 No. 2 (2026)