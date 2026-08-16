---
conversion_metadata:
  converted_at: "2026-07-21T08:25:07Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Saeedian.pdf"
  source_pdf_sha256: "f88e9f72fcc908f93af21c5cb84c4d1a13f2c718f054e25a7930561231b30893"
  page_count: 120
  markdown_char_count: 511869
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A  Comparative  Review  of 
Electricity  Load  Forecasting 
Methods  Across  Temporal 
Horizons

TESI DI LAUREA MAGISTRALE IN

ELECTRICAL ENGINEERING

INGEGNERIA ELETTRICA

Author: Zahra Saeedian

Student ID: 222206 
Advisor: Samuele Grillo 
Co-advisor: Daniele Linaro 
Academic Year: 2024-25

---

<!-- PAGE 3 -->

i

Abstract

Accurate electricity load forecasting is a critical component of modern energy system 
planning  and  operation,  particularly  in  the  context  of  growing  electrification, 
renewable  energy  integration,  and  demand-side  flexibility.  This  thesis  presents  a 
structured review of forecasting methods across three key time horizons: short-term 
(up to 1 week), medium-term (1 week to 1 month), and long-term (beyond 1 month). 
Each category is examined with respect to its methodological strengths, limitations, 
and data requirements.

Statistical  models  such  as  multiple  linear  regression  and  SARIMA  are  found  to  be 
effective for short-term forecasting due to their interpretability and low data demands. 
Machine  learning  approaches—including  support  vector  regression  and  tree-based 
ensembles—offer  improved  flexibility  for  medium-term  predictions.  For  long-term 
forecasting, deep learning models such as LSTM and Transformer-based architectures 
demonstrate  superior performance in capturing  complex  temporal patterns. Hybrid 
models, combining elements from fuzzy systems, optimization techniques, and deep 
learning, achieve the highest accuracy but require significant data and computational 
resources.

The thesis introduces a classification framework that aligns forecasting methods with 
time  horizons  and  data  availability  scales—from  household-level  to  national-level 
applications.  Visual  guides  are  provided  to  support  model  selection  based  on 
forecasting objectives and data conditions. The study concludes that no single model 
is  universally  optimal;  effective  forecasting  requires  context-sensitive  method 
selection, balancing accuracy, interpretability, and resource constraints.

Key-words: Load Forecasting, Electricity Demand, Machine Learning, Deep Learning, 
Hybrid Models.

---

<!-- PAGE 5 -->

ii

Abstract in italiano

Una  previsione  accurata  del  carico  elettrico  è  un  elemento  fondamentale  nella 
pianificazione  e  nella  gestione  dei  sistemi  energetici  moderni,  soprattutto  alla  luce 
dell’elettrificazione  crescente,  dell’integrazione  delle  fonti  rinnovabili  e  della 
flessibilità della domanda. Questa tesi propone una revisione strutturata dei principali 
metodi  di  previsione  del  carico  elettrico,  suddivisi  in  tre  orizzonti  temporali:  breve 
termine (fino a 1 settimana), medio termine (da 1 settimana a 1 mese) e lungo termine 
(oltre 1 mese). Ogni categoria viene analizzata in relazione ai punti di forza, ai limiti 
metodologici e ai requisiti di dati.

I  modelli statistici, come la regressione lineare multipla e SARIMA,  risultano  adatti 
alla  previsione  a  breve  termine  per  la  loro  semplicità  e  bassa  esigenza  di  dati.  Le 
tecniche  di  machine  learning,  tra  cui  la  regressione  con  support  vectors  o  alberi 
decisionali, offrono maggiore flessibilità per previsioni a medio termine. Per previsioni 
a  lungo  termine,  i  modelli  di  deep  learning  come  LSTM  e  le  architetture  basate  su 
Transformer  si  distinguono  per  la  capacità  di  modellare  sequenze  complesse  nel 
tempo. I modelli ibridi—che combinano sistemi fuzzy, algoritmi di ottimizzazione e 
deep learning—raggiungono la massima accuratezza, ma richiedono una disponibilità 
significativa di dati e risorse computazionali.

La  tesi  propone  un  quadro  di  classificazione  che  collega  i  metodi  previsionali  agli 
orizzonti temporali e ai livelli di disponibilità dei dati, da applicazioni domestiche fino 
a quelle a scala nazionale. Vengono forniti strumenti visivi per supportare la scelta del 
modello in base agli obiettivi previsionali e alle condizioni di disponibilità dei dati. Si 
conclude che non esiste un modello universalmente migliore: una previsione efficace 
richiede  la  scelta  di  metodi  sensibili  al  contesto,  che  bilancino  precisione, 
interpretabilità e risorse disponibili.

Parole  chiave:  Previsione  del  Carico,  Domanda  di  Elettricità,  Apprendimento 
Automatico, Deep Learning, Modelli Ibridi.

---

<!-- PAGE 7 -->

| Contents

iii

Contents

Abstract ................................................................................................................................. i

Abstract in italiano .......................................................................................................... iii

Contents ............................................................................................................................... v

1

Introduction ............................................................................................................... 1

1.1.

1.2.

1.3.

Importance of load forecasting .................................................................... 2

Objectives and scope of the thesis ............................................................... 2

Structure of the thesis ................................................................................... 3

2

Load Forecasting ....................................................................................................... 4

2.1.

Time-based categorization of load forecasting ......................................... 4 
Short-term load forecasting ..................................................................... 4 
2.1.1. 
2.1.2.  Medium-term load forecasting ................................................................ 5 
Long-term load forecasting ...................................................................... 5 
2.1.3.

2.2.

Factors affecting load forecasting ............................................................... 5 
2.2.1.  Weather and climate ................................................................................. 6 
Building and appliance attributes ........................................................... 6 
2.2.2. 
Sociodemographic and economic factors .............................................. 7 
2.2.3. 
Technological factors and new appliances ............................................ 8 
2.2.4. 
Behavioral and social factors ................................................................... 9 
2.2.5.

2.3.

Challenges of load forecasting .................................................................. 10 
2.3.1.  Data quality and availability ................................................................. 10 
2.3.2.  Model accuracy and complexity ........................................................... 11 
2.3.3.  Uncertainty ............................................................................................... 13 
Consumer variability .............................................................................. 14 
2.3.4.

2.4.

Summary ...................................................................................................... 14

3

Short-term load forecasting .................................................................................. 15

3.1.

Statistical models ......................................................................................... 15 
3.1.1. 
Regression-based methods .................................................................... 15 
3.1.2.  ARIMA and SARIMA ............................................................................. 18

3.2.

3.2.1.

ML models .................................................................................................... 19 
Support vector regression ...................................................................... 20

---

<!-- PAGE 8 -->

iv

Tree-based models ................................................................................... 22 
3.2.2. 
3.2.3. 
k-nearest neighbors ................................................................................. 26 
3.2.4.  Artificial neural networks ...................................................................... 28

3.3.

3.3.1. 
3.3.2.

Deep learning models ................................................................................. 31 
Recurrent neural networks ..................................................................... 31 
Transformer-based models .................................................................... 34

3.4.

Hybrid models ............................................................................................. 36 
Statistical & ML hybrids ......................................................................... 36 
3.4.1. 
3.4.2. 
Ensemble tree-based methods ............................................................... 37 
3.4.3.  Neural network-based hybrids ............................................................. 38 
Intelligent and fuzzy logic hybrids ....................................................... 40 
3.4.4. 
Transformer-based hybrids .................................................................... 40 
3.4.5.

3.5.

Summary ....................................................................................................... 43

4  Medium-term load forecasting ............................................................................ 45

4.1.

Statistical methods ....................................................................................... 45 
Regression-based methods ..................................................................... 46 
4.1.1. 
4.1.2.  ARIMA and SARIMA ............................................................................. 48

4.2.

ML models .................................................................................................... 49 
Tree-based models ................................................................................... 50 
4.2.1. 
4.2.2. 
k-NN .......................................................................................................... 55 
4.2.3.  ANN .......................................................................................................... 58

4.3.

4.3.1. 
4.3.2.

Deep learning models ................................................................................. 60 
RNN ........................................................................................................... 60 
Transformer-based models .................................................................... 62

4.4.

Hybrid models ............................................................................................. 64 
Statistical–deep learning hybrids .......................................................... 65 
4.4.1. 
Transformer-based hybrids .................................................................... 66 
4.4.2. 
CNN–LSTM hybrids ............................................................................... 66 
4.4.3. 
4.4.4. 
Signal decomposition-based hybrids ................................................... 67 
4.4.5.  Neural Prophet–LSTM hybrids ............................................................. 68

4.5.

Summary ....................................................................................................... 70

5

Long-term load forecasting ................................................................................... 72

5.1.

Statistical methods ....................................................................................... 72 
5.1.1. 
Regression-based models ....................................................................... 73 
5.1.2.  ARIMA and SARIMA ............................................................................. 74

5.2.

5.2.1.

Machine learning methods ......................................................................... 76 
SVR ............................................................................................................ 76

---

<!-- PAGE 9 -->

| Contents

v

5.2.2. 
Tree-based models .................................................................................. 78 
5.2.3.  ANN .......................................................................................................... 79

5.3.

Deep learning ............................................................................................... 80 
5.3.1.  Multilayer perceptron ............................................................................. 81 
LSTM ......................................................................................................... 82 
5.3.2. 
Transformer-based models .................................................................... 84 
5.3.3.

5.4.

5.4.1. 
5.4.2. 
5.4.3. 
5.4.4. 
5.4.5.

Hybrid models ............................................................................................. 86 
Fuzzy-Neural Network-Based Hybrid Models .................................. 86 
Fuzzy-RNN-based models ..................................................................... 87 
Fuzzy-SVM and grey system hybrid models ...................................... 88 
LSTM-based hybrid deep learning models ......................................... 89 
Transformer-based hybrid deep learning models .............................. 89

5.5.

Summary ...................................................................................................... 91

6

Conclusion and future research directions ....................................................... 92

6.1.

6.2.

6.3.

6.4.

6.5.

6.6.

Recapitulation of research objectives and contributions ....................... 92

Strategic alignment between forecasting horizons and methods ........ 94

Method suitability based on data scale .................................................... 94

Implications for practice and policy ......................................................... 95

Limitations and future research directions ............................................. 95

Final remarks ............................................................................................... 96

Bibliography ..................................................................................................................... 97

List of Figures ................................................................................................................. 105

List of Tables .................................................................................................................. 107

Acknowledgments ......................................................................................................... 109

---

<!-- PAGE 10 -->

iv

---

<!-- PAGE 11 -->

1

1  Introduction

Electricity  is  an  essential  part  of  modern  life,  powering  homes,  industries,  and 
transportation  systems.  As  Figure  1.1  shows,  among  all  energy  consumers,  the 
residential sector represents a significant share of total electricity demand. Households 
consume  energy  for  heating,  cooling,  lighting,  cooking,  and  running  electrical 
appliances,  with  consumption  patterns  varying  based  on  factors  such  as  weather 
conditions, socio-economic status, building structure, and consumer  behavior [1]. In 
2022,  residential  electricity  consumption  accounted  for  25.8%  of  final  energy 
consumption in the European Union, reflecting its importance in overall power system 
management [2].

Understanding  the  dynamics  of  residential  electricity  consumption  is  essential  for 
ensuring an efficient and stable power supply. Electricity demand fluctuates due to 
daily  and  seasonal  variations,  economic  conditions,  and  external  influences  such  as 
policy  changes,  technological  advancements,  and  renewable  energy  integration  [3]. 
Accurately  forecasting  electricity  demand  is  therefore  crucial  for  power  system 
operation,  enabling  utilities  and  policymakers  to  make  informed  decisions  on  grid 
stability, energy pricing, and infrastructure investments.

Figure 1.1: Electricity consumption by sectors (GWh) [1].

---

<!-- PAGE 12 -->

2

| Introduction

1.1.  Importance of load forecasting

Global electricity demand continues to surge, even as traditional fossil fuel reserves 
become  increasingly  difficult  to  extract  and  deplete.  Meanwhile,  renewable  energy 
technologies  remain  in  early  adoption  stages,  exacerbating  the  energy  crisis. 
According  to  the  International  Energy  Agency  (IEA),  accurate  load  forecasting  is 
essential  for  effective  energy  planning,  power  dispatch,  and  achieving  Sustainable 
Development  Goals  (SDG-7  and  SDG-13).  Benefits  of  electricity  prediction  is 
mentioned  in  Figure  1.2.  Precise  forecasts  not  only  enable  utilities  to  optimize 
generation schedules and control operational costs but also enhance grid stability by 
preventing overloads and blackouts [4], [5].

The integration of smart grids within smart cities further underscores the importance 
of advanced forecasting. Smart grids leverage digital communication technologies to 
enable real-time monitoring and bidirectional data exchange between consumers and 
utilities,  thereby  optimizing  energy  consumption  and  facilitating  demand-side 
management. This data-driven approach not only supports the efficient deployment 
of  renewable  energy  sources  and  clean  transportation  options  but  also  informs 
strategic  urban  planning  and  resource  allocation.  By  enabling  both  short-term  and 
long-term  predictions,  these  systems  empower  policymakers  to  make  informed 
decisions that enhance urban sustainability and resilience [6].

Figure 1.2: Benefits of electricity consumption prediction [4]

1.2.  Objectives and scope of the thesis

The objectives and scope of this thesis are centered on a comprehensive examination 
of contemporary load forecasting techniques across various time horizons, including 
short-term, medium-term, and long-term forecasts. This study aims to systematically 
classify  and  assess  a  wide  range  of  forecasting  models,  encompassing  traditional 
statistical approaches, machine learning algorithms, deep learning architectures, and 
hybrid  methodologies.  Particular  attention  is  given  to  evaluating  the  effectiveness, 
advantages,  and  limitations  of  these  techniques  in  accurately  predicting  electricity 
demand.

---

<!-- PAGE 13 -->

| Introduction

3

Rather than focusing on empirical data collection, preprocessing steps, or specific case 
studies, the thesis adopts a conceptual and methodological perspective. It investigates 
the key factors that influence power consumption and analyzes how these variables 
impact the precision and reliability of forecasting models.

Additionally,  the  work  critically  engages  with  the  ongoing  challenges  and  recent 
developments in the field, highlighting areas where existing methods may fall short 
and where improvements are most needed. By identifying current research gaps and 
future directions, the thesis contributes to the broader discourse on how forecasting 
can evolve to meet the demands of modern energy systems.

Ultimately, this research is intended to offer valuable insights for scholars, industry 
professionals,  and  policymakers,  helping  them  to  make  informed  decisions  when 
selecting,  designing,  or  applying  forecasting  tools  within  the  context  of  energy 
planning and management.

1.3.  Structure of the thesis

This  thesis  is  structured  into  six  chapters,  each  building  a  comprehensive 
understanding of load forecasting methods across varying time horizons. Chapter  2 
provides an overview of the fundamental concepts of load forecasting, including the 
key variables that influence electricity demand, and the principal challenges associated 
with forecasting load behavior.

Chapter  3  delves  into  Short-Term  Load  Forecasting  (STLF),  presenting  a  range  of 
methodologies such as traditional statistical techniques, machine learning algorithms, 
and deep learning models. Chapter 4 shifts focus to Medium-Term Load Forecasting 
(MTLF), analyzing models designed to predict energy demand over intervals ranging 
from days to several months, and discussing strategies employed to improve forecast 
accuracy.  In  Chapter  5,  the  thesis  explores  Long-Term  Load  Forecasting  (LTLF), 
covering  both  econometric  approaches  and  artificial  intelligence-based  techniques 
used to project demand over extended time frames.

Finally, Chapter Error! Reference source not found. offers a comparative assessment o
f  the  models  presented  in  earlier  chapters,  evaluating  their  relative  strengths, 
limitations, and suitability for different forecasting horizons. This chapter also reviews 
recent advancements in the field, outlines emerging research directions, and concludes 
with  key 
forecasting 
insights  and  recommendations  aimed  at  enhancing 
methodologies.

By  offering  a  structured  and  critical  analysis  of  load  forecasting  techniques  across 
short-,  medium-,  and  long-term  horizons,  this  thesis  seeks  to  contribute  to  the 
development  of  more  accurate,  adaptable,  and  robust  forecasting  solutions  for  the 
evolving needs of modern power systems.

---

<!-- PAGE 14 -->

4

| Load Forecasting

2  Load Forecasting

Load forecasting refers to the process of predicting future electricity demand based on 
historical  consumption  data,  weather  conditions,  economic  indicators,  and  other 
influencing  factors.  Accurate  forecasting  is  essential  for  ensuring  grid  stability, 
optimizing power generation, and minimizing operational costs [5].

2.1.  Time-based categorization of load forecasting

[7] categorized load forecasting into four time horizons: very short term, short-term, 
medium-term,  and  long-term.  However,  for  the  purposes  of  this  thesis,  load 
forecasting is categorized into three primary time-horizons, shown in Figure 2.1, based 
on forecasting needs and the duration of the prediction.

Figure 2.1: Load forecasting time horizontal.

2.1.1.  Short-term load forecasting

Short-term load forecasting predicts electricity demand for a period ranging  from a 
few minutes to one week. This time frame is crucial for operational decisions, such as 
power  generation  scheduling,  unit  commitment,  load  switching,  and  demand-side 
management. By providing accurate forecasts for such short time frames, utilities can 
optimize resource utilization, reduce operational costs, and maintain grid stability [7].

---

<!-- PAGE 15 -->

| Load Forecasting

5

2.1.2.   Medium-term load forecasting

Medium-term load forecasting covers periods from one week to one month. It is useful 
for tasks like outage scheduling, maintenance planning, and tariff regulation. MTLF 
helps utilities plan for intermediate-term fluctuations in electricity demand, ensuring 
they are prepared for variations during high and low consumption periods [7].

2.1.3.   Long-term load forecasting

Long-term  load  forecasting  focuses  on  predicting  electricity  demand  for  periods 
extending  beyond  one  month.  These  forecasts  are  essential  for  strategic  planning, 
energy  infrastructure  development,  and  policymaking.  Long-term  predictions  are 
used  to  anticipate  future  power  needs,  ensuring  that  utilities  can  make  informed 
decisions  regarding  grid  capacity  expansion,  resource  allocation,  and  investment  in 
renewable energy [7].

2.2.  Factors affecting load forecasting

In  this  section,  we  explore  the  various  factors  that  significantly  influence  electricity 
consumption  and  load  forecasting.  Residential  electricity  consumption  (REC)  is 
shaped  by  a  combination  of  socioeconomic  indicators,  building  characteristics, 
appliance ownership, and usage patterns which are shown in

Figure  2.2.  Climate  and  location  also  play  crucial  roles,  as  heating  and  cooling 
requirements  are  highly  sensitive  to  temperature  fluctuations,  making  city-scale 
energy usage particularly responsive to weather conditions [8]. Additionally, factors 
such  as  household  size,  income,  energy  efficiency  measures,  and  technological 
progress contribute to demand variability. As electricity generation and consumption 
have notable environmental and social costs, understanding these drivers is vital for 
developing effective policies and strategies for sustainable energy use.

Figure 2.2: Key factors affecting load forecasting.

---

<!-- PAGE 16 -->

6

| Load Forecasting

At the broader national level, REC is the aggregate of individual household decisions, 
influenced by demographic changes, consumer preferences, and economic factors. The 
increasing  complexity  of  REC  forecasting  arises  from  shifting  societal  trends, 
urbanization, the emergence of new appliances, and unpredictable human behavior, 
all of which pose challenges for predictive models. Despite advancements, there  are 
still obstacles due to inaccurate data, evolving consumption patterns, and unforeseen 
events  such  as  public  health  crises  [9].  Therefore,  accurate  load  forecasting  must 
account  for  both  technological  and  social  factors  that  impact  energy  use  across 
different scales and regions [4], [10].

2.2.1.  Weather and climate

Weather  and  climate  are  crucial  factors  influencing  electricity  consumption, 
particularly in areas where heating and cooling demands vary with seasonal changes. 
Temperature,  humidity,  and  other  weather  variables  have  a  significant  impact  on 
electricity  usage,  especially  in  residential  and  commercial  sectors.  During  extreme 
weather conditions, such as very hot or cold temperatures, energy consumption tends 
to rise due to increased use of air conditioning or heating systems. For instance, city-
scale electricity usage is highly temperature-sensitive, with heating and cooling needs 
contributing  significantly  to  total  energy  consumption.  Seasonal  variations  further 
lead  to  fluctuations  in  demand,  with  higher  electricity  usage  during  summer  and 
winter months.

Humidity also plays a key role in influencing electricity demand, particularly in hot 
climates.  The  heat  index,  which  reflects  human  perception  of  temperature,  is 
determined  by  combining  air  temperature  and  relative  humidity.  When  relative 
humidity is high, the evaporation process in the human body slows down, causing the 
body to retain more heat. As a result, the perceived temperature increases, leading to 
higher  energy  consumption  for  cooling.  Therefore,  areas  with  high  humidity, 
especially during the summer, experience a marked increase in energy demand due to 
the added stress on cooling devices.

The growing impact of climate change has led to more frequent and extreme weather 
events,  further  complicating  traditional  forecasting  models.  As  weather  patterns 
become  more  unpredictable,  advanced  forecasting  models  are  needed  to  ensure 
reliable  predictions.  Additionally,  the  increasing  integration  of  renewable  energy 
sources such as solar and wind power, which are intermittent and weather-dependent, 
introduces  further  uncertainty  into  load  demand.  This  requires  more  sophisticated 
forecasting  methods  to  integrate  renewable  energy  efficiently  into  the  grid  while 
maintaining a stable supply and demand balance [4], [8], [10], [11].

2.2.2.  Building and appliance attributes

The type of building and the appliances within it are significant factors that influence 
electricity  consumption.  Buildings  with  poor  insulation,  older  electrical  systems,  or

---

<!-- PAGE 17 -->

| Load Forecasting

7

inefficient appliances tend to have higher energy demand compared to those that are 
well-insulated and equipped with modern, energy-efficient systems. The design and 
size of a building also play a role in determining how much energy is consumed. For 
example,  larger  homes  or  buildings  typically  require  more  electricity  for  heating, 
cooling, and lighting, while energy-efficient designs and materials can reduce overall 
demand.  Determining  the  influence  of  occupancy,  dwelling  size,  and  building 
topologies  on  consumption  is  equally  important  in  building  accurate  predictive 
models for load forecasting [3].

Appliance  usage  patterns  are  another  critical  factor  in  load  forecasting.  Household 
appliances,  such  as  air  conditioners,  refrigerators,  washing  machines,  and  lighting 
systems, directly impact the total electricity demand. The ownership and frequency of 
use of these appliances are often linked to lifestyle choices, income levels, and regional 
factors.  In  warmer  climates,  the  widespread  use  of  air  conditioning  systems 
significantly  increases  electricity  consumption,  especially  during  peak  summer 
months.

The increasing adoption of energy-efficient appliances and building technologies can 
mitigate  some  of  the  demand  pressure  on  the  grid.  Energy-efficient  appliances 
consume less power and are becoming more prevalent in households and commercial 
establishments due to technological advancements and incentives. These innovations 
help  lower  the  overall  electricity  consumption,  especially  during  peak  times, 
contributing to more stable load profiles and easing the pressure on electricity grids. 
By  considering  the  type,  usage,  and  efficiency  of  buildings  and  appliances,  load 
forecasting models can provide more accurate predictions and facilitate better energy 
management [8], [9].

2.2.3.  Sociodemographic and economic factors

Sociodemographic  and  economic  factors  play  a  crucial  role  in  shaping  electricity 
consumption patterns. Key elements such as income, household size, education, and 
urbanization influence energy demand significantly. Higher-income households tend 
to consume  more  electricity due to increased usage of electrical appliances, heating 
and cooling systems, and other electronic devices. Similarly, larger households require 
more energy for daily activities, leading to higher electricity consumption compared 
to smaller households. Additionally, lifestyle factors, such as the number of residents 
working from home, can significantly impact consumption levels, particularly during 
certain times of the day [8].

Economic  conditions  also  affect  electricity  demand.  During  periods  of  economic 
growth, electricity consumption rises due to increased industrial activity and higher 
consumer spending. Conversely, during economic downturns, demand tends to fall as 
businesses scale back operations and households adopt more energy-efficient practices 
to save on costs. Furthermore, population growth directly influences total electricity 
consumption, requiring utilities to adjust their forecasts accordingly. Projections show

---

<!-- PAGE 18 -->

8

| Load Forecasting

that countries and regions experiencing rapid urbanization, such as India, China, and 
Southeast  Asia,  will  see  substantial  increases  in  electricity  demand  over  the  next 
decade, with India’s demand increasing by 40%, China’s by 25%, and Southeast Asia's 
by 30% from 2019 to 2030 [10].

Urbanization  is  another  significant  factor.  As  urban  populations  grow,  electricity 
demand increases due to the higher number of households, commercial buildings, and 
transportation needs. In urban areas, electricity consumption is heavily driven by the 
need for lighting, heating, cooling, and powering appliances in both residential and 
commercial spaces. This leads to higher overall demand for electricity in cities [9].

Moreover, sociodemographic factors such as the dependency ratio—the proportion of 
non-working individuals (children and elderly) to the working-age population—also 
affect  electricity  consumption.  Households  with  high  dependency  ratios  tend  to 
allocate  more  income  toward  basic  needs,  including  electricity,  which  may  reduce 
their savings potential and increase overall demand for electricity [1].

In  conclusion,  sociodemographic  and  economic  factors,  including  household 
characteristics,  urbanization,  economic  growth,  and  technological  advancements, 
significantly  influence  electricity  consumption.  Understanding  these  factors  is 
essential  for  developing  accurate  forecasting  models,  which  help  optimize  energy 
supply management and design targeted demand response strategies.

2.2.4.  Technological factors and new appliances

Technological advancements and behavioral shifts, such as the widespread adoption 
of electric vehicles (EVs) and smart devices, have introduced new patterns in electricity 
demand.  EVs  require  substantial  charging  infrastructure,  which  can  shift  demand 
peaks and increase load during specific times of the day. Similarly, the integration of 
distributed  renewable  energy  systems,  such  as  rooftop  solar  panels,  is  reshaping 
traditional energy usage models. While these innovations promote energy efficiency 
and  enable  partial  self-generation,  they  can  also  introduce  new  demand  peaks, 
particularly when EVs are charged simultaneously during off-peak hours [5], [9].

A  particularly  notable  challenge  is  the  substantial  increase  in  electricity  demand 
resulting from widespread EV adoption. This trend poses a serious burden on power 
grids, especially residential distribution networks. For example, around 80% of EVs 
are charged using residential in-home chargers, meaning their charging habits often 
align  with  household  consumption  peaks  [8].  As  electrification  expands,  U.S. 
electricity demand is projected to rise by 23% by 2050, with EVs accounting for up to 
300 TWh of consumption. Moreover, if EV penetration reaches 30%, it could result in 
a  50%  increase  in  peak  load  at  the  residential  distribution  transformer  level, 
significantly stressing local grid infrastructure [12].

In parallel, the integration of smart grids and Internet of Things (IoT) technologies has 
enhanced load forecasting accuracy. Smart meters and real-time monitoring systems

---

<!-- PAGE 19 -->

| Load Forecasting

9

provide  granular  insights  into  consumer  behavior,  enabling  more  adaptive  and 
dynamic energy management strategies [7].

Additionally, energy efficiency improvements, such as more efficient appliances, the 
transition to LED lighting, and enhanced building insulation, have led to reductions 
in per capita electricity use. These developments require regular updates to traditional 
forecasting models to reflect evolving consumption patterns [5].

Demand-side  management  strategies,  including  time-of-use  pricing  and  demand 
response programs, have also started influencing user behavior. These approaches aim 
to  shift  electricity  usage  away  from  peak  times,  flattening  demand  curves  and 
improving  grid  stability.  However,  their  effectiveness  still  depends  on  consumer 
engagement, which can vary widely [5].

In summary, while technological advancements introduce opportunities for smarter 
and more efficient energy use, they also bring significant complexity and uncertainty 
to  forecasting  models.  The  adoption  rate,  usage  patterns,  and  integration  of  new 
technologies  like  EVs  and  smart  appliances  must  be  carefully  considered  when 
planning for future energy needs.

2.2.5.  Behavioral and social factors

Human  behavior  plays  a  crucial,  yet  inherently  unpredictable  role  in  electricity 
consumption,  introducing  significant  challenges  for  accurate  load  forecasting. 
Lifestyle changes, daily routines, cultural events such as holidays or festivals, and even 
social norms can all lead to sudden and irregular fluctuations in electricity demand. 
For example, increased home occupancy during weekends or national celebrations can 
significantly  raise  residential  electricity  usage,  making  short-term  forecasting  more 
difficult [9].

Moreover,  growing  awareness  around  environmental  issues  and  participation  in 
demand-side management (DSM) programs has influenced consumer behavior. These 
programs encourage users to modify their consumption habits, such as shifting energy 
use to off-peak hours or reducing overall consumption, adding further variability to 
usage patterns, and impacting forecast accuracy [9].

On  an  individual  level,  electricity  consumption  is  strongly  influenced  by  personal 
decision-making,  which  is  characterized  by  its  stochastic  and  dynamic  nature.  As  a 
result, disaggregated or household-level forecasting models are particularly sensitive 
to  behavioral  factors,  often  leading  to  higher  variability  and  prediction  errors.  In 
contrast, when energy demand is aggregated over a large population, the variability 
introduced  by  individual  behavior  tends  to  balance  out,  resulting  in  relatively 
smoother and more predictable trends [13].

These behavioral and social elements introduce a complex, human-centric dimension 
to  energy  forecasting  that  cannot  be  fully  captured  by  technical  models  alone.  As 
energy  systems  evolve  to  include  more  user-driven  dynamics  such  as  flexible

---

<!-- PAGE 20 -->

10

| Load Forecasting

consumption, remote work habits, and real-time energy feedback, the need for models 
that integrate behavioral insights becomes increasingly important.

2.3.  Challenges of load forecasting

Despite  advancements  in  forecasting  techniques,  several  challenges  remain,  as 
described in the following.

2.3.1.  Data quality and availability

Accurate  electricity  consumption  forecasting  relies  heavily  on  the  availability  and 
quality of data. However, several challenges complicate this process, especially when 
forecasting individual consumption patterns.

Collecting detailed and reliable consumption data can be particularly difficult. Many 
previous  studies  have  relied  on  sub-metered  data  from  individual  appliances  or 
customer  surveys,  but  obtaining  such  detailed  information  on  a  scale  is  often 
impractical. When dealing with a large number of households, gathering daily usage 
schedules  or  appliance-specific  data  becomes  infeasible.  In  addition,  concerns  over 
data privacy, particularly regarding personal appliance usage patterns, present further 
barriers to widespread data collection [13].

Beyond  access,  the  quality  of  the  available  data  is  another  critical  issue.  Energy 
consumption  data  sets  frequently  suffer  from  missing  values,  outliers,  and 
inconsistencies caused by sensor errors, manual data entry mistakes, or transmission 
problems. These irregularities, if not addressed through effective  data cleaning  and 
preprocessing,  can  significantly  compromise  the  performance  and  reliability  of 
forecasting models [4].

Another challenge arises from the high-dimensional nature of electricity consumption 
data. Forecasting load accurately involves analyzing multiple interdependent factors, 
such  as  weather  conditions,  economic  variables,  and  consumer  behaviors.  The 
complexity  and  volume  of  these  variables  make  it  difficult  to  extract  meaningful 
patterns,  particularly  when  individual  household  differences  are  considered. 
Successful  forecasting  models  must  be  capable  of  managing  such  high-dimensional 
data to identify the underlying trends and relationships [14].

Furthermore,  with  the  increasing  deployment  of  smart  grid  technologies,  the  data 
landscape has become even more complex. Smart grids generate multifaceted datasets 
collected  from  a  variety  of  sources,  ranging  from  individual  meters  to  city-wide 
monitoring  systems.  While  this  data  offers  valuable  insights  into  electricity 
consumption  patterns  at  different  levels  of  aggregation,  its  complexity  and  volume 
pose significant analytical challenges. Effective integration and analysis of smart grid 
data  are  essential  for  enhancing  the  accuracy  and  reliability  of  consumption 
forecasting models [6].

---

<!-- PAGE 21 -->

| Load Forecasting

11

2.3.2.  Model accuracy and complexity

Accurate  load  forecasting  requires  selecting  an  appropriate  model  that  balances 
forecasting performance with computational efficiency. Electricity demand data often 
exhibits nonlinear relationships influenced by external factors, posing challenges for 
both traditional statistical methods and modern machine learning techniques.

Traditional  models,  such  as  ARIMA  (AutoRegressive  Integrated  Moving  Average) 
and SARIMA (Seasonal ARIMA), are effective for capturing linear patterns in time-
series  data.  However,  their  predictive  performance  declines  when  dealing  with 
complex nonlinear relationships or sudden behavioral changes caused by factors such 
as economic fluctuations or weather variability. In contrast, machine learning models 
like Long Short-Term Memory (LSTM) networks and Convolutional Neural Networks 
(CNNs)  are  better  suited  for  identifying  intricate  nonlinear  patterns.  These  models 
significantly  improve  forecasting  accuracy  but  demand  substantial  computational 
resources and large datasets for training, which makes them computationally intensive 
and time-consuming [6], [9], [15].

To address the limitations of both traditional and advanced deep learning approaches, 
hybrid models have been developed. These models combine the strengths of statistical 
methods  and  artificial  intelligence  techniques,  such  as  integrating  ARIMA  with 
Generative  Adversarial  Networks  (GANs)  or  LSTM  networks.  Hybrid  approaches 
have demonstrated improved prediction performance by leveraging both linear and 
nonlinear modeling capabilities. However, they introduce new challenges related to 
optimization,  interpretability,  and  computational  cost.  Training  hybrid  models  is 
computationally demanding, and interpreting their outputs can be complex, reducing 
their practicality for real-time forecasting applications [15].

The  reliance  on  deep  learning  and  hybrid  models  has  also  raised  concerns  about 
computational complexity and resource constraints. Models like XGBoost and Deep 
Neural  Networks  (DNNs)  require  extensive  datasets  and  considerable  processing 
power to achieve high accuracy [6], [9]. Hyperparameter tuning, which is essential for 
enhancing  model  performance,  further  exacerbates  computational  demands.  As  a 
result,  deploying  these  models  for  real-time  or  large-scale  forecasting  in  the  power 
systems  industry  can  be  challenging.  While  AI-driven  approaches  offer  substantial 
improvements 
in  forecasting  accuracy,  ensuring  that  these  models  remain 
computationally efficient and scalable is crucial for their practical application.

In  summary,  although  deep  learning  and  hybrid  models  present  significant 
advantages  in  terms  of  forecasting  accuracy,  optimizing  them  for  computational 
efficiency, and ensuring their feasibility for real-time implementation remain critical 
challenges.

In load forecasting literature, evaluating the accuracy of predictive models is essential 
for understanding their effectiveness and guiding their  practical application. Model 
performance  is  typically  quantified  using  established  error  metrics  that  assess  how

---

<!-- PAGE 22 -->

12

| Load Forecasting

closely the predicted values align with the actual observed data. These metrics not only 
allow  researchers  to  compare  different  forecasting  approaches  but  also  reveal  how 
models behave under various conditions and time horizons.

Commonly  used  accuracy  measures  include  the  Mean  Absolute  Error  (MAE),  Root 
Mean  Squared  Error  (RMSE)  and  Mean  Absolute  Percentage  Error  (MAPE).  Each 
provides  distinct  insights:  MAE  gives  the  average  magnitude  of  prediction  errors, 
RMSE penalizes larger errors more heavily due to the squaring operation, and MAPE 
expresses errors as a percentage, which is useful for comparing across different load 
scales.

Table 2.1 summarizes the most commonly used evaluation metrics in load forecasting 
research, including their mathematical formulations.

Table 2.1: Common error metrics used in the load forecasting literature.

Metric Name

Formula

Mean Absolute

Error

𝑀𝐴𝐸 =

1
𝑛

𝑛
∑|𝑦𝑖 − 𝑦𝑖̂ |
𝑡=1

Mean Squared

Error

𝑀𝑆𝐸 =

1
𝑛

𝑛
∑(𝑦𝑖 − 𝑦𝑖̂)2
𝑡=1

Root Mean Squared

Error

𝑅𝑀𝑆𝐸 = √

1
𝑛

𝑛
∑(𝑦𝑖 − 𝑦̂)2
𝑡=1

Mean Absolute

Percentage Error

𝑀𝐴𝑃𝐸 =

1
𝑛

𝑛

∑ |

𝑡=1

(𝑦𝑖 − 𝑦𝑖̂)2
𝑦𝑖

| × 100

Coefficient of

Determination

𝑅2 = 1 −

(𝑦𝑖 − 𝑦𝑖̂)2
(𝑦𝑖 − 𝑌̅)2

---

<!-- PAGE 23 -->

| Load Forecasting

13

Coefficient of

Variation of the

Root Mean Square

𝐶𝑉𝑅𝑀𝑆𝐸 =

Error

√1
𝑛

∑ (𝑦𝑖 − 𝑦̂)2

𝑛
𝑡=1
𝑌̅

× 100

2.3.3.  Uncertainty

Load forecasting is inherently uncertain due to the wide range of unpredictable factors 
influencing  electricity  demand.  These  uncertainties  complicate  accurate  prediction 
and must be carefully considered to ensure reliable power system operation.

Unexpected public health events and behavioral shifts are major sources of forecasting 
uncertainty.  For  example,  during  the  COVID-19  pandemic,  electricity  consumption 
patterns  changed  significantly.  Countries  with  strict  lockdown  measures,  such  as 
Spain  and  Italy,  experienced  electricity  usage  profiles  resembling  pre-pandemic 
weekends, whereas countries like Sweden, with fewer restrictions, observed smaller 
decreases in consumption [4]. Such events highlight how historical consumption data 
may become unreliable for forecasting future demand.

Climate  change  also  plays  a  critical  role  in  altering  load  patterns.  The  increasing 
frequency and intensity of extreme weather events, such as severe heatwaves or cold 
snaps,  can  cause  sudden  peak  loads  in  power  systems  [4],  [16].  These  load  spikes 
threaten grid stability by pushing distribution transformers and other equipment to 
unsafe  operational  limits.  As  climate-driven  changes  make  temperature-sensitive 
demand more volatile, historical trends become less predictive, posing challenges for 
short-term and peak load forecasting.

The variability introduced by renewable energy sources, particularly solar and wind 
power,  further  adds  to  the  uncertainty  in  load  forecasting  [5].  Since  renewable 
generation depends heavily on weather conditions, predicting the available electricity 
supply becomes more complex. To address this, forecasting models must increasingly 
incorporate probabilistic and scenario-based techniques to manage renewable energy 
fluctuations and maintain grid reliability.

Economic  fluctuations  and  unexpected  power  plant  outages  introduce  additional 
layers  of  uncertainty  [4],  [9].  Economic  downturns  or  booms  can  significantly  shift 
electricity demand, especially in the industrial sector. Similarly, unplanned outages at 
power  plants  can  abruptly  disrupt  supply  patterns,  making  load  forecasting  even 
more volatile and challenging.

In  summary,  uncertainty  in  load  forecasting  arises  from  diverse  factors  including 
public  health  crises,  climate  change,  renewable  energy  variability,  economic 
conditions,  and  supply  disruptions.  Addressing  these  challenges  requires  the 
development  of  advanced  forecasting  models  capable  of  accounting  for  such 
uncertainties, ensuring more resilient and reliable energy system operations.

---

<!-- PAGE 24 -->

14

| Load Forecasting

2.3.4.  Consumer variability

for

load

forecasting,  particularly  due

The growing integration of smart grid technologies and emerging energy systems has 
the 
introduced  new  challenges 
unpredictability of consumer behavior. Smart meters and demand response programs 
now provide utilities with greater control over load management, enabling dynamic 
pricing  and  real-time  adjustments  to  optimize  energy  consumption  [5].  However, 
consumer participation in these programs is highly variable, as individual willingness 
to  modify  energy  use  based  on  price  signals  or  grid  demands  differs  significantly. 
Factors such as weather conditions, economic circumstances, and personal preferences 
further influence participation levels, adding uncertainty to forecasting efforts.

to

Emerging  technologies  like  electric  vehicles  (EVs),  battery  storage  systems,  and 
distributed energy generation are also reshaping traditional load demand profiles [5], 
[12]. The widespread adoption of EVs introduces new and less predictable demand 
patterns,  as  charging  times  and  energy  requirements  may  not  align  with  historical 
usage data. Similarly, battery storage and rooftop solar installations allow consumers 
to both store and inject electricity into the grid, significantly altering net load profiles. 
These  technological  developments  add  further  complexity  for  forecasting  models, 
necessitating  continuous  adaptation  to  evolving  consumption  patterns  and  the 
accelerating pace of technological innovation.

2.4.  Summary

Chapter 2 highlighted the key challenges in electricity load forecasting, focusing on 
factors like data quality, model complexity, and uncertainty. It discussed how weather, 
economic changes, and unexpected events contribute to the volatility of load forecasts, 
especially with the impact of climate change and extreme weather.

Traditional  forecasting  models  struggle  with  capturing  nonlinear  relationships, 
leading to the adoption of advanced machine learning techniques like deep learning 
and  hybrid  models.  However,  these  methods  come  with  increased  computational 
demands.  The  integration  of  renewable  energy  sources  and  emerging  technologies 
such  as  smart  grids,  electric  vehicles,  and  battery  storage  further  complicates 
forecasting.

The chapter also emphasized the importance of accurate short-term load forecasting, 
particularly  during  peak  load  conditions,  to  ensure  the  stability  of  power  systems. 
Smart grid technologies and better metering infrastructure make this more achievable, 
supporting effective power dispatching and reducing grid stress.

In conclusion, addressing the challenges in load forecasting requires advanced models 
that balance accuracy and computational efficiency, enabling reliable predictions in an 
increasingly dynamic environment.

---

<!-- PAGE 25 -->

| Short-term load forecasting

15

3  Short-term load forecasting

In this study, short-term load forecasting (STLF) refers to the prediction of electricity 
demand over time horizons ranging from a few minutes up to a week. STLF plays a 
vital role in various aspects of power system operations, including unit commitment, 
load dispatch, demand response programs, and real-time energy market transactions 
[7].  Accurate  short-term  forecasts  enable  utilities  and  grid  operators  to  optimize 
generation schedules, maintain system reliability, and minimize operational costs.

STLF  models  must  account  for  a  wide range  of  influencing  factors  such  as  weather 
conditions,  consumer  behavior,  public  holidays,  economic  trends,  and  building 
characteristics [11], [14]. These variables, combined with the inherently nonlinear and 
stochastic nature of electricity demand, make the development of precise forecasting 
models a complex task.

Over the years, STLF techniques have evolved from traditional statistical methods to 
more sophisticated machine learning  and deep learning  approaches. More recently, 
hybrid models that integrate multiple techniques have emerged, offering promising 
improvements in forecast accuracy and adaptability to dynamic grid environments.

STLF  techniques  are  typically  categorized  based  on  their  modeling  approach  and 
capacity to manage different patterns in electricity demand. The four primary groups 
include statistical methods, machine learning techniques, deep learning models, and 
hybrid or ensemble approaches.

3.1.  Statistical models

Statistical  methods,  such  as  ARIMA  and  SARIMA,  rely  on  historical  patterns  and 
linear assumptions. They are valued for their interpretability and simplicity but are 
limited in capturing nonlinear and complex dependencies. For example, SARIMA has 
been  shown  to  perform  well  under  stable  seasonal  conditions  but  struggles  with 
dynamic or non-stationary inputs [17].

3.1.1.  Regression-based methods

Regression-based models have historically formed the backbone of STLF, particularly 
due  to  their  clarity,  computational  efficiency,  and  ability  to  extract  interpretable 
insights from historical data. These models assume a functional relationship between

---

<!-- PAGE 26 -->

16

| Short-term load forecasting

input  variables  (e.g.,  weather,  calendar  features)  and  electricity  demand.  Several 
variants exist; each suited to different forecasting contexts.

Linear  Regression  (LR)  is  a  classical  statistical  method  widely  used  in  STLF, 
particularly in early applications where simplicity, interpretability, and computational 
efficiency are critical. In its standard form, linear regression models the relationship 
between  a  dependent  variable  (e.g.,  electrical  load)  and  one  or  more  independent 
variables (e.g., temperature, hour of the day, or occupancy) under the assumption of 
linearity.

The general multiple linear regression model is expressed in Equation (3.1):

𝑌̂ = 𝛽0 + 𝛽₁𝑋₁  +  𝛽₂𝑋₂ + . . . + 𝛽ₙ𝑋ₙ  +  𝜀,

(3.1)

where: 𝑌̂ is the dependent variable (e.g., electricity consumption), 𝛽0 is the intercept 
(constant term), 𝛽1, 𝛽2, … , 𝛽𝑛  are the coefficients for the independent variables, and 𝜀 is 
an error term.

Katić  et  al.  [18]  provided  quantitative  error  metrics  comparing  multiple  linear 
regression (MLR) and artificial neural network (ANN) models for predicting heating 
energy consumption in school buildings. Their findings indicate that the ANN model 
outperformed the MLR model in terms of predictive accuracy.

Specifically,  the  ANN  model  achieved  a  lower  Mean  Absolute  Error  and  RMSE 
compared to the MLR model. For instance, the ANN model's MAE was approximately 
12% lower, and its RMSE was about 15% lower than those of the MLR model. These 
results  suggest  that  the  ANN  model  was  more  effective  in  capturing  the  complex, 
nonlinear  relationships  between  building  characteristics  and  heating  energy 
consumption.

The  superior  performance  of  the  ANN  model  is  attributed  to  its  ability  to  model 
intricate  patterns  and  interactions  among  variables,  which  are  often  present  in 
building  energy  consumption  data.  In  contrast,  the  MLR  model,  while  simpler  and 
more interpretable, may not adequately capture such complexities, leading to higher 
prediction errors.

In summary, the study by Katić et al. [18] demonstrates that while MLR models offer 
simplicity  and  ease  of  interpretation,  ANN  models  provide  enhanced  predictive 
accuracy for modeling heating energy consumption in school buildings, particularly 
when dealing with complex and nonlinear data relationships.

Nano [19] enhanced traditional MLR models by integrating calendar-based variables 
such as weekdays, holidays, and seasonal patterns. This integration aimed to improve 
the accuracy of daily and weekly load forecasts. While specific error metrics were not 
detailed, the inclusion of these calendar variables likely contributed to a reduction in 
forecasting errors by accounting for recurring patterns in electricity consumption.

---

<!-- PAGE 27 -->

| Short-term load forecasting

17

Dudek [20] introduced a pattern-based local linear regression approach for short-term 
load  forecasting.  This  method  involved  clustering  daily  load  profiles  and  applying 
separate linear regressions to each cluster, effectively capturing recurring short-term 
load  fluctuations.  The  study  compared  this  approach  with  other  models,  including 
ARIMA,  exponential  smoothing,  neural  networks,  and  the  Nadaraya-Watson 
estimator.  The  pattern-based  local  linear  regression  demonstrated  high  accuracy, 
particularly  in  modeling  daily  load  cycles,  and  offered  advantages  in  terms  of 
simplicity and computational efficiency.

Nsangou et al. [21] conducted a comparative analysis of quantile regression, decision 
tree,  and  ANN  models  to  analyze  household  electricity  consumption  under 
uncertainty. Their findings indicate that the ANN model outperformed the other two 
methods, achieving lower values in RMSE, MAE, and Mean Absolute Percentage Error 
(MAPE),  along  with  a  higher  coefficient  of  determination  (R2).  This  superior 
performance  is  attributed  to  the  ANN's  ability  to  model  complex,  nonlinear 
relationships in the data.

Table 3.1: Strengths and limitations of regression methods in STLF.

Model Type

Strengths

Weaknesses

Linear regression

to compute; good as

underperforms in dynamic or

Simple; interpretable; fast

Limited to linear patterns;

baseline.

nonlinear contexts.

Local linear

regression

Adapts to temporal

Requires clustering or

variations; better for

segmentation; sensitive to

pattern-based loads.

pattern definition.

Quantile regression

uncertainty; robust to

interpret compared to mean-

Captures variability and

More complex; harder to

outliers.

based methods.

Regression models are often integrated into hybrid frameworks or used in ensemble 
methods, especially when interpretability and speed are needed alongside accuracy. 
In many real-world STLF systems, as mentioned in Table 3.1, regression serves as a 
fast,  initial  approximation  before  more  complex  machine  learning  models  are 
employed.

---

<!-- PAGE 28 -->

18

| Short-term load forecasting

3.1.2.  ARIMA and SARIMA

The ARIMA  model and its seasonal extension, SARIMA,  are widely  used statistical 
methods in STLF. These models are designed to capture time-based dependencies and 
trends in electricity consumption, making them particularly useful in settings where 
demand exhibits consistent temporal patterns.

An  ARIMA  model  is  defined  by  three  parameters:  p,  d,  and  q.  p  is  the  number  of 
autoregressive terms, meaning it defines how many past values of the time series are 
used to predict the current value; d indicates the degree  of differencing required to 
make  the  series  stationary—that  is,  removing  trends  or  seasonality  that  distort  the 
forecasting model; finally, q represents the number of lagged forecast errors included 
in the model, which captures the influence of past deviations between predicted and 
actual values.

When  electricity  demand  exhibits  seasonal  patterns—such  as  higher  consumption 
during  specific  hours,  days,  or  months—the  SARIMA  model  extends  ARIMA  by 
incorporating seasonal components. This is typically denoted as SARIMA (p, d, q) (P, 
D, Q) [m], where the uppercase parameters (P, D, Q) mirror the ARIMA structure but 
are applied to the seasonal cycle defined by m (e.g., m = 12 for monthly data or m = 24 
for hourly data in daily cycles).

Bilgili  and  Pinar  [17]  applied  SARIMA  to  forecast  Turkey’s  gross  electricity 
consumption  and  compared  its  performance  with  LSTM.  SARIMA  successfully 
captured  recurring  seasonal  trends  and  produced  reasonable  short-term  forecasts; 
however,  it  struggled  with  modeling  nonlinear  and  long-range  dependencies.  In 
contrast,  LSTM  significantly  outperformed  SARIMA  across  all  error  metrics. 
Specifically,  LSTM  achieved  a  MAPE  of  2.42%,  MAE  of  215.35  GWh,  and  RMSE  of 
329.9 GWh, along with an R-value of 0.9992. These results highlight LSTM’s superior 
ability  to  capture  complex  temporal  dynamics,  especially  during  volatile  periods, 
making it a more robust tool for forecasting electricity demand.

Gellert et al. [22] used ARIMA and (Trigonometric, Box-Cox transformation, ARMA 
errors, Trend, and Seasonal components) TBATS to forecast electricity consumption 
and PV energy production in smart homes, applying these models to datasets with 5-
minute,  hourly,  and  bi-hourly  resolutions.  ARIMA  performed  well  under  stable, 
structured  conditions  but  struggled  with  high-frequency  variability  and  irregular 
generation patterns. TBATS outperformed ARIMA and even neural models in those 
scenarios, achieving a lower MAE of 73.62 W. Its ability to manage multiple seasonality 
and adapt to complex fluctuations made TBATS a more suitable option for short-term 
forecasting in smart home environments.

---

<!-- PAGE 29 -->

| Short-term load forecasting

19

Table 3.2: Strengths and limitations of ARIMA and SARIMA methods in STLF.

Model Type

Strengths

Weaknesses

ARIMA

Captures short-term

Assumes linearity,

temporal dependencies,

requires data stationarity,

easy to interpret,

not suited for complex,

low computational cost.

nonlinear systems.

Effective models seasonal

complex,

Parameter tuning can be

SARIMA

patterns,

performance declines with

widely used in practice.

high-frequency variability or

external shocks.

In summary, ARIMA and SARIMA have proven to be effective baseline methods for 
short-term  load  forecasting  when  the  data  exhibits  strong  linearity  and  regular 
seasonal trends. As demonstrated in the studies by Bilgili and Pinar [17] and Gellert et 
al.  [22],  these  models  perform  well  under  stable  conditions  and  structured 
consumption patterns. SARIMA, in particular, can manage seasonal effects efficiently 
and  offers  interpretability  with  relatively  low  computational  cost.  However,  both 
ARIMA and SARIMA show clear limitations in more complex, volatile environments 
where  nonlinear  dependencies,  high-frequency  variability,  or  long-range  temporal 
relationships are present. In such cases, more advanced models like LSTM or TBATS 
consistently outperform them, making traditional statistical models less suitable for 
modern, dynamic energy systems in short-term forecasting applications. A summary 
of the strengths and limitations of ARIMA and SARIMA in short-term load forecasting 
is provided in Table 3.2.

3.2.  ML models

With the increasing complexity of electricity consumption patterns and the availability 
of large volumes of smart meter data, machine learning (ML) models have emerged as 
powerful  tools  for  STLF.  Unlike  traditional  statistical  methods,  ML  techniques  can 
capture nonlinear relationships and complex interactions between multiple variables 
without explicit assumptions about the underlying data distribution.

ML  models  learn  directly  from  historical  data  by  identifying  patterns  and 
dependencies, often using features such as time, temperature, humidity, occupancy, 
or  appliance  usage.  These  models  have  demonstrated  superior  accuracy  and 
adaptability in scenarios with high variability or when external factors significantly 
influence consumption [10], [14].

---

<!-- PAGE 30 -->

20

| Short-term load forecasting

3.2.1.  Support vector regression

Support  Vector  Regression  (SVR)  is  a  machine  learning  technique  derived  from 
Support Vector Machines (SVM), widely used in regression tasks involving complex, 
nonlinear,  and  high-dimensional  data.  It  is  particularly  effective  in  STLF  due  to  its 
robustness, generalization capability, and adaptability to various data distributions.

The SVR regression function uses a dot product in high-dimensional space via a kernel 
function. The formal expression is given in Equation (3.2). This formulation has been 
widely used in load forecasting literature, including recent studies such as Bendaoud 
et al. [23].

𝑚

𝑓(𝑥) =   ∑ 𝜔𝑖

𝜑𝑖(𝑥) + 𝛽 = 𝜔𝑇𝜑(𝑥) + 𝛽,

(3.2)

𝑖=1

Where f(x) is the predicted output, 𝜑(𝑥) is a nonlinear function mapping the input data 
into  a  higher-dimensional  space,  𝜔  is  the  weight  vector, 𝛽  is  the  bias  term, 𝜔𝑇𝜑(𝑥) 
represents  the  dot  product  between  the  weight  vector  and  the  transformed  input 
features.

This formulation enables SVR to perform nonlinear regression by applying the kernel 
trick, which replaces the explicit computation of 𝜑(𝑥) with kernel functions such as 
radial  basis  function  (RBF),  polynomial,  or  linear  kernels.  The  kernel  function 
implicitly,  significantly  reducing 
the 
computes 
computational complexity.

inner  product  𝜑(𝑥𝑖)𝑇𝜑(𝑥𝑖)

Figure 3.1: SVR model.

As  it  is  shown  in  Figure  3.1  ,SVR operates  by  using  the kernel  function  to  map  the 
input data to a higher-dimensional space, where data are fit with a linear regression 
model while introducing an ε-insensitive loss margin, within which deviations from 
the true value are not penalized. This results in a sparse model where only data points 
lying outside the ε-margin (called support vectors) influence the solution. The model

---

<!-- PAGE 31 -->

| Short-term load forecasting

21

is regularized by a parameter C, which controls the trade-off between model linearity 
(in the higher dimensional space) and tolerance to error outside the ε-margin [23].

Bendaoud et al. [23] conducted a comparative study on short-term load forecasting in 
Algeria, evaluating SVR alongside ANN, CNN, and Gradient Boosting methods. SVR 
demonstrated robust performance, outperforming ANN and linear regression models, 
and achieving a MAPE of 2.17%. Its effectiveness was particularly notable in capturing 
nonlinear  load  behaviors  during  weekends,  indicating  its  suitability  for  modeling 
complex consumption patterns in short-term forecasts.

Haque and Rahman [24] compared SVR with shallow ANN and deep learning models 
like LSTM networks for energy consumption forecasting. While LSTM achieved the 
lowest  forecasting  errors,  SVR  offered  a  compelling  balance  between  accuracy  and 
computational efficiency. It outperformed traditional models and was less resource-
intensive  than  deep  networks,  making  it  a  practical  choice  for  scenarios  with 
structured yet moderately complex patterns.

Zhang  et  al.  [25]  integrated  SVR  into  an  Explainable  Artificial  Intelligence  (XAI) 
framework to estimate building energy consumption and greenhouse gas emissions. 
The study demonstrated that SVR could deliver competitive predictive accuracy while 
interpretability  through  SHAP  (SHapley  Additive 
supporting  partial  model 
exPlanations) values. This approach provided insights into the relative importance of 
different input features, enhancing the transparency of the forecasting model.

Hasan et al. [26] enhanced SVR's predictive capabilities by combining it with Genetic 
Algorithms  (GA)  to  optimize  hyperparameters  for  energy  consumption  forecasting 
across  four  economic  sectors.  The  GA-optimized  SVR  model  achieved  significantly 
improved  performance,  showcasing 
integrating  heuristic 
optimization techniques to address challenges posed by multivariate, nonlinear, and 
large-scale datasets.

the  advantage  of

These  studies  collectively  underscore  SVR's  versatility  and  effectiveness  in  energy 
consumption forecasting, particularly when dealing with nonlinear patterns and when 
computational  resources  are  a  consideration.  For  a  detailed  overview  of  SVR's 
strengths and weaknesses, please refer to Table 3.3.

---

<!-- PAGE 32 -->

22

| Short-term load forecasting

Table 3.3: Strengths and limitations of SVR method in STLF.

Model Type

Strengths

Weaknesses

SVR

Strong performance with

nonlinear and high-

dimensional datasets;

Robust to overfitting in

small to medium-sized

datasets; Flexible kernel

functions support complex

feature transformations;

Performs well as both a

standalone model and

within hybrid optimization

frameworks

Requires careful tuning of

kernel parameters (e.g., C, ε,

kernel type); Can be

computationally expensive for

very large datasets; Less

interpretable than simpler

models unless combined with

explainable AI; May

underperform deep models in

highly dynamic or long-

horizon scenarios

3.2.2.  Tree-based models

Tree-based models have become a central component of modern ML thanks to their 
ability  to  model  complex  nonlinear  relationships,  capture  interactions  between 
variables,  and  provide  interpretable  outputs  in  many  cases.  In  the  context  of  STLF, 
they  offer  strong  predictive  performance  while  managing  structured  tabular  data, 
time-based features, and weather inputs with ease. This section discusses three  key 
approaches:  Decision  Tree  Regression,  Random  Forests,  and  Extreme  Gradient 
Boosting (XGBoost), each building on the foundational principles of decision trees.

Figure 3.2: Tree-based model.

---

<!-- PAGE 33 -->

| Short-term load forecasting

23

Figure 3.2 illustration of the structural differences between Decision Tree Regression 
(DTR),  Random  Forest  (RF),  and  XGBoost  models.  In  DTR,  a  single  tree  is  used  to 
generate  one  prediction.  RF  builds  multiple  decision  trees  in  parallel  and  averages 
their  outputs  to  produce  the  final  result.  XGBoost,  on  the  other  hand,  builds  trees 
sequentially,  where  each  tree  corrects  the  errors  of  the  previous  one,  and  the  final 
prediction is obtained from the last tree in the sequence.

3.2.2.1.  Decision tree regression

A DTR model operates by recursively partitioning the input space to reduce variance 
within  each  subset.  At  each  internal  node,  the  algorithm  selects  a  feature  𝑥𝑗  and 
threshold t that minimizes the sum of squared errors across the two resulting regions. 
This criterion is expressed mathematically in Equation (3.3):

min
𝑗,𝑡

[ ∑ (𝑦𝑖 − 𝑦̅𝑅1)2 + ∑ (𝑦𝑖 − 𝑦̅𝑅2)2
𝑥𝑖∈𝑅1(𝑗,𝑡)

𝑥𝑖∈𝑅2(𝑗,𝑡)

] ,

(3.3)

Where: 𝑅1 and 𝑅2 are the left and right branches split on feature 𝑥𝑗 at threshold t, 𝑦̅𝑅𝑘 
is the Mean of the target values in each region.

Peteleaza  et  al.  [6]  conducted  a  comprehensive  study  on  electricity  consumption 
forecasting  for  sustainable  smart  cities  using  machine  learning  methods.  Their 
research involved a comparative analysis of seven different models, including decision 
trees,  applied  to  datasets  from  three  metropolitan  areas  in  the  United  States:  Los 
Angeles, Sacramento, and New York. The decision tree models demonstrated strong 
interpretability and adaptability to daily and seasonal patterns, making them valuable 
for  understanding  energy  use  behaviors  in  smart-city  contexts.  Notably,  the  study 
found  that  Light  Gradient  Boosting  Machine  (LightGBM),  a  decision  tree-based 
ensemble method, provided the best results with a Coefficient of Variation of the Root 
Mean Square Error (CVRMSE) of 6.5% for Los Angeles, 4.6% for Sacramento, and 4.1% 
for New York. These findings highlight the effectiveness of decision tree approaches 
in capturing complex consumption patterns across diverse urban settings.

Nsangou et al. [21] explored the application of decision trees in explaining household 
electricity  consumption  in  Cameroon.  Their  study  compared  the  performance  of 
decision trees with quantile regression and ANN in assessing electricity consumption 
drivers.  The  decision  tree  models  were  instrumental  in  identifying  key  factors 
influencing energy use, such as equipment usage, household income levels, housing 
structures, and weather conditions. While the ANN model outperformed the others in 
terms  of  predictive  accuracy, 
the  decision  tree  approach  offered  superior 
interpretability, allowing for a clearer understanding of how various factors contribute 
to electricity consumption.

These studies underscore the utility of Decision Tree methods in energy consumption 
forecasting, particularly in scenarios where model interpretability and adaptability to

---

<!-- PAGE 34 -->

24

| Short-term load forecasting

varying consumption patterns are crucial. For a detailed overview of the strengths and 
weaknesses of Decision Tree models in this context, please refer to Table 3.4.

3.2.2.2.  Random Forests

Building  upon  this  concept,  Random  Forests  introduce  an  ensemble  strategy  by 
training  multiple  decision  trees  on  bootstrapped  subsets  of  the  data.  Each  tree 
contributes  a  prediction,  and  the  final  result  is  computed  as  the  average  of  all 
individual outputs. This aggregation approach is formalized in Equation (3.4):

𝑦̂ =

1
𝑇

𝑇

∑ ℎ𝑡(𝑥)
𝑡=1

,

(3.4)

Where T is the number of decision trees, ℎ𝑡(𝑥) is the prediction from the 𝑡𝑡ℎ tree.

Rafiq et al. [3] conducted an in-depth analysis of residential electricity consumption 
patterns  in  Dubai,  utilizing  high-resolution  smart  meter  data,  weather  information, 
and voluntary survey data on household characteristics. The study employed K-means 
clustering  to  group  households  based  on  their  consumption  profiles  and  applied 
various  classification  algorithms,  including  Random  Forest,  to  predict  household 
consumption patterns based on dwelling and occupant characteristics. The RF model 
demonstrated  strong  performance  and  interpretability,  effectively  identifying  key 
factors driving consumption patterns, such as cooling systems, number of occupants, 
and  dwelling  size.  This  approach  provided  valuable  insights  for  demand-side 
management  initiatives  and  the  design  of  energy-saving  strategies  in  residential 
sectors.

Peteleaza et al. [6] explored electricity consumption forecasting for sustainable smart 
cities  using  machine  learning  methods.  The  study  compared  the  performance  of 
various models, including Random Forest, in predicting electricity consumption at the 
city  level.  The  RF  model  outperformed  individual  decision  trees,  demonstrating 
higher  accuracy  and  robustness  in  capturing  complex  consumption  patterns  across 
diverse urban settings. The ensemble nature of RF, which combines multiple decision 
trees, contributed to its improved generalization and reduced overfitting, making it a 
suitable choice for load forecasting in smart city applications.

These  studies  underscore  the  utility  of  Random  Forest  methods  in  energy 
consumption forecasting, particularly in scenarios where model interpretability and 
adaptability to varying consumption patterns are crucial. For a detailed overview of 
the strengths and weaknesses of Random Forest models in this context, please refer to 
Table 3.1.

3.2.2.3.  Extreme gradient boosting

Further extending the ensemble concept, XGBoost builds trees sequentially, with each 
new tree aiming to correct the residual errors of the combined prior models. XGBoost

---

<!-- PAGE 35 -->

| Short-term load forecasting

25

is a regularized implementation of GBMs, offering advantages in speed, accuracy, and 
overfitting control. The cumulative prediction of an XGBoost model can be expressed 
as shown in Equation (3.5):

𝑀
𝐹(𝑥) =   ∑ 𝛾𝑚ℎ𝑚(𝑥)
𝑚=1

,

(3.5)

Where ℎ𝑚(𝑥) is the 𝑚𝑡ℎ decision tree, 𝛾𝑚 is the learning rate applied to its output.

Bendaoud  et  al.  [23]  conducted  a  comparative  study  evaluating  the  performance  of 
various machine learning models, including SVR, ANN, CNN, and XGBoost, for STLF 
in Algeria. The study found that XGBoost outperformed the other models, achieving 
the  lowest  MAPE  of  1.88%.  This  superior  performance  was  attributed  to  XGBoost's 
ability  to  manage  complex  nonlinear  relationships  and  its  robustness  against 
overfitting,  making  it  particularly  effective  in  capturing  the  intricacies  of  electricity 
consumption patterns.

Deng et al. [16] proposed a hybrid Bagging–XGBoost model aimed at improving load 
forecasting  accuracy  under  extreme  weather  conditions.  By  integrating  the  Bagging 
ensemble method with XGBoost, the model enhanced generalization capabilities and 
reduced variance, leading to more reliable predictions during volatile environmental 
scenarios.  The  hybrid  approach  demonstrated  robustness  and  accuracy,  effectively 
addressing  the  challenges  posed  by  extreme  weather  events  in  energy  demand 
forecasting.

Zhang  et  al.  [25]  incorporated  XGBoost  into  an  XAI  framework  to  predict  building 
energy  consumption  and  greenhouse  gas  emissions.  Utilizing  SHapley  Additive 
exPlanations values, the study provided insights into the contribution of each feature 
to the model's predictions, enhancing interpretability. The integration of XGBoost with 
SHAP  allowed  for  accurate  forecasting  while  offering  transparency,  enabling 
stakeholders to understand the driving factors behind energy consumption patterns.

Rafiq et al. [3] applied XGBoost for household classification tasks based on smart meter 
data  in  Dubai.  The  model  achieved  high  accuracy  levels  above  95%,  effectively 
distinguishing  between  different  household  electricity  usage  profiles.  XGBoost's 
capability to manage large datasets with numerous features contributed to its strong 
performance, making it a valuable tool for energy consumption analysis and customer 
segmentation.

These studies collectively highlight XGBoost's versatility and effectiveness in energy 
consumption  forecasting,  particularly  in  handling  complex  datasets,  providing 
accurate  predictions,  and  offering  interpretability  when  combined  with  tools  like 
SHAP. For a detailed overview of XGBoost's strengths and weaknesses in this context, 
please refer to Table 3.4.

---

<!-- PAGE 36 -->

26

| Short-term load forecasting

Table 3.4: Strengths and Limitations of Tree-Based Methods in STLF.

Model Type

Strengths

Weaknesses

Decision Tree

Simple; interpretable;

Prone to overfitting; sensitive

models non-linearity

to data changes

Random Forest

generalization; manages

Reduces overfitting; good

XGBoost

missing data

High accuracy;

Regularized; manages

feature interactions and

missing values

Less interpretable; Large

models can be slow

Requires tuning;

computationally more

intensive

3.2.3.  k-nearest neighbors

The k-NN algorithm is a non-parametric and instance-based learning method that has 
been  widely  applied  in  STLF  due  to  its  simplicity  and  ability  to  model  nonlinear 
relationships without requiring an explicit training phase. In regression settings, k-NN 
predicts the output for a new instance by averaging the target values of the k most 
similar observations in the historical dataset.

The  standard  k-NN  regression  function  can  be  mathematically  represented  in 
Equation (3.6):

𝑦̂(𝑥) =

1
𝑘

∑ 𝑦𝑖

,

𝑖∈𝑁𝑘(𝑥)

(3.6)

Where 𝑦̂(𝑥) is the predicted load value for the input instance  x, 𝑁𝑘(𝑥) is the set of k 
nearest  neighbors  to  x,  based  on  a  chosen  distance  metric  (commonly  Euclidean 
distance), 𝑦𝑖 is the observed load associated with the neighbor i.

This method assumes that similar inputs produce similar outputs, making it especially 
useful for recognizing recurring load patterns over time.

K-NN algorithm has been widely used in both standalone and hybrid frameworks for 
interpretability,  and 
energy  consumption  forecasting  due  to 
effectiveness  in  pattern  recognition.  Peteleaza  et  al.  [6]  included  k-NN  in  a 
comparative  study  involving  various  machine  learning  models  for  smart  city

its  simplicity,

---

<!-- PAGE 37 -->

| Short-term load forecasting

27

electricity  consumption  forecasting  across  metropolitan  areas  in  the  United  States. 
While k-NN performed reasonably well in identifying similar historical consumption 
profiles,  it  was  ultimately  surpassed  by  more  advanced  ensemble  models  such  as 
XGBoost  in  terms  of  accuracy.  However,  the  authors  emphasized  that  the 
interpretability  and  pattern-matching  capabilities  of  k-NN  remain  advantageous  in 
applications where understanding consumption behavior is as important as predictive 
precision.

Rafiq et al. [3] employed k-NN in a classification task based on residential electricity 
consumption data from Dubai. The study used k-means clustering to group household 
consumption  patterns  and  then  applied  k-NN  as  a  baseline  classifier  to  identify 
similarities  between  user  profiles.  Although  more  sophisticated  classifiers  were 
introduced later in the study, k-NN played a crucial role in modelling userbehavior 
and establishing an interpretable reference point for further algorithmic comparisons.

Similarly,  Zhou  et  al.  [27]  utilized  k-NN  to  enhance  cluster-based  short-term  load 
forecasting for different building types in a Chinese case study. By grouping buildings 
with  similar  consumption  characteristics,  the  model  applied  k-NN  to  exploit  local 
similarities  in  daily  demand  trends.  This  approach  was  particularly  effective  in 
contexts  with  high  building  diversity  and  limited  historical  data,  where  leveraging 
neighbourhood-based predictions helped improve accuracy without the complexity of 
deep learning methods.

Together,  these  studies  demonstrate  the  ongoing  relevance  of  k-NN  in  energy 
forecasting, particularly in scenarios involving  heterogeneous datasets, limited data 
history,  or  a  need  for  transparent,  easy-to-understand  models.  A  summary  of  the 
strengths and limitations of the k-NN method in this context is presented in Table 3.5.

Table 3.5: Strengths and limitations of k-NN method in STLF.

Model Type

Strengths

Weaknesses

k-NN

Simple and intuitive to

implement; No training

phase required; Effective in

capturing local patterns

and repeated load

behaviors; Works well for

nonlinear relationships;

Easily adaptable for both

regression and

classification tasks.

Computationally expensive

with large datasets; Sensitive

to irrelevant or unscaled

features; Performance

degrades in high-dimensional

spaces; Does not manage

temporal dependencies unless

explicitly engineered; Model

performance depends heavily

on the choice of distance

metric and k value.

---

<!-- PAGE 38 -->

28

| Short-term load forecasting

3.2.4.  Artificial neural networks

ANNs  are  computational  models  inspired  by  the  biological  structure  of  the  human 
brain. They consist of interconnected layers of processing units (neurons) capable of 
learning  complex,  nonlinear  relationships  between  inputs  and  outputs.  In  STLF, 
ANNs  have  proven  to  be  highly  effective  due  to  their  flexibility,  ability  to  capture 
hidden patterns, and capacity to model temporal and seasonal dynamics in electricity 
consumption.

A typical feedforward neural network (FFNN) as it is shown in Figure 3.3 consists of 
an input layer, one or more hidden layers, and an output layer. Each neuron in the 
network computes the weighted sum of its inputs and applies an activation function 
to introduce nonlinearity. The model is trained to minimize the prediction error using 
backpropagation  and  gradient  descent,  adjusting  the  weights  of  the  connections 
between neurons to improve accuracy over successive iterations.

1.  Feedforward  Neural  Network:  The  simplest  ANN  architecture  used  in

forecasting tasks is the FFNN. It consists of three components:

•  Input Layer: This layer represents the input features such as historical 
electricity  consumption,  time  of  day,  temperature,  and  other  relevant 
factors.

•  Hidden  Layers:  These  layers  apply  nonlinear  transformations  to  the 
input data. Each neuron in the hidden layer computes a weighted sum 
of its inputs and passes the result through an activation function.

•  Output Layer: The output layer produces the final prediction, which in 
load  forecasting  is  usually  the  predicted  electricity  consumption  at  a 
future time point.

The output of each neuron in the hidden layers is computed based on Equation 
(3.7):

𝑛

(𝑙) = ∑ 𝑤𝑖𝑗
𝑧𝑗

(𝑙)𝑥𝑖

(𝑙−1) + 𝑏𝑗

(𝑙),

(3.7)

𝑖=1

(𝑙)

(𝑙)
  is  the  input  to  the  𝑗𝑡ℎ  neuron  in  layer  l,  𝑤𝑖𝑗

Where  𝑧𝑗
connection between neuron i in the previous layer and neuron j in the current 
layer, 𝑥𝑖
 is the bias term for 
neuron j in layer l.

is the output from the previous layer, and 𝑏𝑗

is  the  weight  of  the

(𝑙−1)

(𝑙)

The neuron then applies an activation function 𝜎 (such as Sigmoid or ReLU) to 
the weighted sum to produce the output based on Equation (3.8):

(𝑙) = 𝜎(𝑧𝑗
𝑎𝑗

(𝑙)),

(3.8)

Where 𝜎 is a nonlinear activation function like Sigmoid in Equation (3.9):

---

<!-- PAGE 39 -->

| Short-term load forecasting

𝜎(𝑥) =

1
1 + 𝑒−𝑥,

Or ReLU by Equation (3.10):

𝜎(𝑥) = max(0, 𝑥),

29

(3.9)

(3.10)

2.  Training the Network: The training of an ANN involves adjusting the weights 
to  minimize  the  error  between  the  predicted  and  actual  values.  The  error  is 
computed  using  a  loss  function,  such  as  MSE  for  regression  tasks  that  are 
defined in Equation Error! Reference source not found.(3.11):

𝐿 =

1
𝑁

𝑁
∑(𝑦𝑖 − 𝑦̂𝑖)2,
𝑖=1

(3.11)

Where L is the loss function or error, N is the number of data points (samples) 
in  the  dataset, 𝑦𝑖  is  the  true  value  (actual  electricity  consumption)  for  the  𝑖𝑡ℎ 
sample, 𝑦̂𝑖 is the predicted value (forecasted electricity consumption) for the 𝑖𝑡ℎ  
sample,  (𝑦𝑖 − 𝑦̂𝑖)2  represents  the  squared  error  for  the  𝑖𝑡ℎ  sample,  which 
measures how far the predicted value is from the actual value. 
Backpropagation  is  used  to  compute  the  gradient  of  the  loss  function  with 
respect  to  each  weight,  which  allows  the  network  to  adjust  the  weights 
iteratively  to  reduce  the  error.  The  weight  updates  are  performed  using  an 
optimization algorithm like Stochastic Gradient Descent (SGD) or Adam based 
on Equation (3.12):

𝜔 ← ω − 𝜂. ∇𝜔𝐿,

(3.12)

Where 𝜔 represents the weights of the network, 𝜂 is the learning rate, ∇𝜔𝐿 is the 
gradient of the loss function with respect to the weights. 
Through  multiple  iterations,  the  model  learns  to  predict  future  load  with 
increasing accuracy by adjusting the weights to better fit the data.

---

<!-- PAGE 40 -->

30

| Short-term load forecasting

Figure 3.3: Feedforward and backpropagation architecture of ANN.

Bendaoud  et  al.  [23]  conducted  a  comparative  study  evaluating  the  performance  of 
various  machine  learning  models,  including  SVR,  CNN,  Gradient  Boosting,  and 
ANNs, for STLF in Algeria. The study found that while Gradient Boosting achieved 
the highest accuracy,  ANNs performed commendably, achieving a MAPE of 2.39%. 
This indicates that ANNs are effective in environments where model simplicity and 
adaptability are preferred.

Haque and Rahman [24] applied ANN models to both 30-minute and 24-hour ahead 
load  forecasts.  Their  findings  revealed  that  ANNs  outperformed  SVR  and  linear 
models, offering a favorable balance between complexity and accuracy. However, in 
more dynamic scenarios, LSTM networks surpassed ANNs in predictive performance, 
highlighting  the  importance  of  model  selection  based  on  the  specific  forecasting 
context.

Katić et al. [18] developed ANN models to estimate heating energy consumption in 
school  buildings.  Their  research  demonstrated  that  ANN  models  achieved  lower 
RMSE and CVRMSE compared to multiple linear regression models. This affirms the 
value of ANNs in building-level energy forecasting, particularly in capturing complex, 
nonlinear relationships inherent in energy consumption data.

Despite their strengths, ANNs also present certain challenges. They require substantial 
datasets for effective training and necessitate careful tuning of hyperparameters, such 
as  learning  rates,  the  number  of  hidden  layers,  and  neuron  counts.  Additionally, 
ANNs  often  lack  interpretability,  making  it  difficult  to  understand  the  underlying 
decision-making process. Without proper regularization, they are prone to overfitting, 
especially when applied to small or noisy datasets.

---

<!-- PAGE 41 -->

| Short-term load forecasting

31

These  studies  collectively  underscore  the  applicability  of  ANNs  in  energy 
consumption forecasting, highlighting their strengths in modeling complex patterns 
and  their  limitations  concerning  data  requirements  and  interpretability  that 
mentioned in Table 3.6.

Table 3.6: Strengths and limitations of ANNs in STLF.

Model Type

Strengths

Weaknesses

Capable of modeling

complex, nonlinear

relationships,

Effective in both short-term

and pattern-based load

ANN

forecasting,

Can integrate diverse

features (e.g., temperature,

calendar, occupancy),

Adaptable to hybrid or

deep learning frameworks.

Prone to overfitting with small

or noisy datasets,

Requires careful tuning of

network architecture,

Difficult to interpret ("black

box" behavior),

Computationally intensive

during training.

3.3.  Deep learning models

DL models are a specialized subset of ANNs that involve architectures with multiple 
hidden layers, enabling them to learn high-level abstractions and hierarchical feature 
representations.  In  the  context  of  STLF,  DL  techniques  have  shown  superior 
performance in modeling nonlinear, temporal, and seasonal electricity consumption 
patterns,  particularly  in  complex  environments  such  as  smart  grids  and  real-time 
demand prediction.

Unlike  shallow  neural  networks,  deep  learning  models  can  automatically  extract 
meaningful  features  from  raw  data,  minimizing  the  need  for  manual  feature 
engineering. Among the most commonly used deep learning architectures in energy 
forecasting are Recurrent Neural Networks (RNNs), LSTM, and CNNs.

3.3.1.  Recurrent neural networks

RNNs  are  designed  to  process  sequential  data  by  maintaining  internal  memory 
through feedback connections. This makes them ideal for time-series tasks such as load 
forecasting.  However,  standard  RNNs  suffer  from  the  vanishing  gradient  problem 
described below, which limits their ability to capture long-term dependencies.

---

<!-- PAGE 42 -->

32

| Short-term load forecasting

RNNs are designed to process sequential data by maintaining an internal hidden state 
that  evolves  over  time.  This  architecture  allows  RNNs  to  capture  temporal 
dependencies,  making  them  suitable  for  tasks  like  electricity  load  forecasting. 
However,  training  RNNs  over  long  sequences  presents  significant  challenges, 
particularly due to the vanishing gradient problem.

As shown by Pascanu et al. [28], when training RNNs using Backpropagation Through 
Time (BPTT), gradients are propagated backward through many time steps. During 
this  process,  the  gradients  are  repeatedly  multiplied  by  the  Jacobian  matrix  of  the 
recurrent weights. If the spectral radius (i.e., the largest absolute eigenvalue) of this 
matrix is less than one, the gradients shrink exponentially with each time step. As a 
result, early layers in the sequence receive near-zero gradients, effectively preventing 
the model from learning long-term dependencies.

This  vanishing  effect  causes  the  RNN  to  focus  mainly  on  recent  inputs  while 
"forgetting" information from earlier time steps, which undermines its ability to model 
in  time  series 
long-range  correlations—a 
forecasting where historical context is crucial.

limitation  particularly  problematic

Pascanu et al.[28] also showed that the exploding gradient problem can occur in the 
opposite  scenario,  when  gradients  grow  exponentially  due  to  large  weight  values. 
Together, these issues severely hamper RNN training.

To address the vanishing gradient problem, gated architectures like LSTM and Gated 
Recurrent Units (GRUs) were developed. These models incorporate mechanisms that 
allow  gradients  to  pass  through  many  time  steps  without  significant  attenuation, 
enabling them to learn long-term dependencies more effectively.

To address this, LSTM networks were introduced: they incorporate memory cells and 
gating  mechanisms  (input,  output,  and  forget  gates),  enabling  them  to  learn  long-
range dependencies more effectively.

The internal operations of an LSTM unit can be summarized by the set of equations 
(3.13):

𝑓𝑡 = 𝜎(𝑊𝑓 ∙ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑓
𝑖𝑡 = 𝜎(𝑊𝑖 ∙ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑖
𝑜𝑡 = 𝜎(𝑊𝑜 ∙ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑜
𝐶𝑡̃ = tanh (𝑊𝐶 ∙ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝐶
𝐶𝑡 = 𝑓𝑡 ∗ 𝐶𝑡−1 + 𝑖𝑡 ∗ 𝐶̃𝑡
ℎ𝑡 = 𝑜𝑡 ∗ tanh (𝐶𝑡)

{

(3.13)

---

<!-- PAGE 43 -->

| Short-term load forecasting

33

Where 𝑥𝑡 is the input at time t, ℎ𝑡 is the hidden state, 𝐶𝑡 is the cell state, 𝜎 is the sigmoid 
function, ∗ denotes element-wise multiplication.

Figure 3.4: Schematic diagram of the LSTM [29].

These equations and Figure 3.4 describe how the model selectively forgets, updates, 
and outputs information across time steps, making it ideal for sequence forecasting 
tasks like STLF.

LSTM  networks  have  shown  substantial  promise  in  the  domain  of  electricity  load 
forecasting, especially when compared to traditional statistical and shallow learning 
models. In a study by Bilgili and Pinar [17], LSTM was evaluated against the SARIMA 
model  for  forecasting  Turkey’s  gross  electricity  consumption.  Their  findings 
demonstrated  that  LSTM  significantly  outperformed  SARIMA,  particularly  in 
modelling  nonlinear  trends  and  seasonal  variations.  The  LSTM  model  achieved 
notably lower error metrics, with a MAPE of 2.42%, MAE of 215.35 GWh, and RMSE 
of 329.9 GWh, emphasizing its strength in capturing complex temporal dependencies 
that  SARIMA  could  not  manage  effectively.  Similarly,  Haque  and  Rahman  [24] 
applied LSTM to both 30-minute and 24-hour-ahead forecasting tasks, comparing its 
performance with SVR and ANN. While ANN and SVR provided reasonable accuracy, 
the LSTM model consistently achieved the lowest MAPE and RMSE values across both 
time  horizons.  These  results  highlight  LSTM’s  ability  to  learn  from  both  short-term 
fluctuations  and  long-term  demand  trends,  making  it  particularly  well-suited  for 
forecasting electricity consumption in dynamic and non-stationary environments.

Further  demonstrating  its  potential,  Memarzadeh  and  Keynia  [30]  proposed  an 
optimally  tuned  LSTM-based  neural  network  specifically  designed  for  short-term 
forecasting  of  electricity  load  and  price.  By  fine-tuning  the  architecture  and 
hyperparameters  using  real-world  grid  data,  their  model  achieved  high  forecasting 
accuracy  across  both  daily  and  hourly  intervals.  This  study  reinforces  LSTM's 
adaptability  and  effectiveness  in  practical  energy  forecasting  scenarios,  especially 
when precision is required for operational decisions.

Collectively,  these  studies  affirm  that  LSTM  models  offer  a  powerful  and  flexible 
approach to short-term load forecasting, capable of handling complex sequences and

---

<!-- PAGE 44 -->

34

| Short-term load forecasting

providing higher accuracy than conventional and many machine learning models that 
is mentioned in Table 3.7.

Table 3.7: Strengths and limitations of RNNs and LSTMs in STLF.

Model Type

Strengths

Weaknesses

Effective in modeling

Require large datasets to

sequential and time-

generalize well,

dependent data,

Computationally expensive,

LSTM captures long-term

especially with long

dependencies using

sequences,

RNN

memory and gates,

Difficult to interpret and

Manages seasonality,

debug due to complex

trends, and lagged effects

architecture,

in electricity demand,

Performs well in multi-step

Sensitive to hyperparameter

forecasting and dynamic

tuning (e.g., number of layers,

environments.

hidden units).

3.3.2.  Transformer-based models

Transformer-based models have recently gained traction in STLF due to their ability 
to model complex temporal dependencies using self-attention mechanisms. Originally 
developed for natural language processing tasks, transformers differ from traditional 
recurrent architectures (like RNNs or LSTMs) in that they process input sequences in 
parallel,  not  sequentially,  enabling  both  faster  training  and  better  long-range 
dependency modeling.

At  the  core  of  the  transformer  architecture  is  the  scaled  dot-product  attention 
mechanism, defined in Equation (3.14):

𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 (𝑄, 𝐾, 𝑉) = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 (

𝑄𝐾𝑇

√𝑑𝑘

) 𝑉

(3.14)

Where Q, K, and V are the query, key, and value matrices, 𝑑𝑘 is the dimensionality of 
the key vectors.

This mechanism allows the model to dynamically weigh the importance of different 
time steps in the input sequence when making predictions, which is especially useful 
in multivariate and irregular load datasets.

---

<!-- PAGE 45 -->

| Short-term load forecasting

35

Table 3.8: Strengths and Limitations of Transformer-Based Models in STLF.

Model Type

Strengths

Weaknesses

Captures long-term

dependencies better than

RNN/LSTM,

Highly parallelizable

during training,

Transformer-Based

Scales well to high-

Models

dimensional multivariate

input,

Provides interpretability

via attention weights,

Performs well in multi-step

and missing data scenarios.

Requires more data and 
computational power, 
Model architecture and tuning 
are more complex, 
Needs careful handling of 
time positional encoding in 
time series forecasting, 
Still relatively new in power 
systems forecasting — less 
validated in practice, 
May overfit on small datasets 
without regularization.

Transformer-based architectures have emerged as powerful tools for electricity load 
forecasting due to their ability to model long-range temporal dependencies and handle 
heterogeneous  input  features.  Unlike  traditional  recurrent  models,  Transformers 
leverage attention mechanisms to selectively focus on the most relevant parts of the 
input sequence, making them particularly effective in time series forecasting tasks.

Ahmad et al. [34] proposed TFTformer, a specialized Transformer architecture tailored 
for electricity load prediction. This model integrates temporal attention mechanisms 
with feature selection strategies to model both static and dynamic covariates. Notable 
components include variable selection networks that enhance input relevance, gated 
residual networks (GRNs) that  facilitate information flow, and multi-head attention 
layers that capture temporal dependencies across multiple time scales. Their results 
demonstrated  that  TFTformer  significantly  outperformed  RNN-based  architectures, 
especially  in  multi-step  forecasting  scenarios  and  in  datasets  containing  missing 
values.  This  highlights  the  model’s  robustness  and  adaptability  in  real-world 
forecasting contexts.

Chan and Yeo [36] implemented a general Transformer architecture to forecast short-
term  electricity  demand.  Their  model  made  use  of  the  self-attention  mechanism  to 
identify  key  time  steps  in  historical  data,  providing  not  only  improved  forecasting 
accuracy  but  also  enhanced  interpretability.  Compared  to  LSTM  models,  the 
Transformer model achieved lower forecasting  errors and revealed which historical 
inputs  contributed  most  to  the  predictions  via  attention  scores.  This  transparency 
allows for a deeper understanding of load dynamics and enhances confidence in the 
forecasting outputs.

---

<!-- PAGE 46 -->

36

| Short-term load forecasting

Together,  these  studies  demonstrate  the  growing  importance  of  Transformer-based 
architectures in energy forecasting. As mentioned in Table 3.8, by offering both high 
accuracy  and  interpretability,  these  models  address  key  limitations  of  traditional 
methods  and  present  a  promising  path  forward  for  short-term  load  forecasting 
applications.

3.4.  Hybrid models

To  address  the  increasing  complexity  of  short-term  electricity  demand  patterns—
affected  by  weather,  human  behavior,  and  distributed  energy  resources—many 
researchers have developed hybrid and ensemble models. These approaches aim to 
combine  the  strengths  of  different  forecasting  techniques  to  improve  prediction 
accuracy, reduce variance, and enhance generalization. Hybrid models are particularly 
beneficial  in  STLF  tasks,  where  they  help  address  both  linear  and  nonlinear 
characteristics in data.

3.4.1.  Statistical & ML hybrids

Hybrid models that combine statistical and machine learning techniques have gained 
prominence in energy load forecasting due to their ability to capture both linear and 
nonlinear  patterns  in  time  series  data.  By  leveraging  the  strengths  of  different 
methodologies, these models aim to improve forecasting accuracy and robustness.

Figure 3.5: Proposed model of GA-optimized SVR [26].

---

<!-- PAGE 47 -->

| Short-term load forecasting

37

Bendaoud et al. [23]proposed a hybrid model that integrates Exponential Smoothing 
with GBRT for short-term electricity load forecasting. In this approach, Exponential 
Smoothing is employed to model the linear and seasonal components of the load data, 
effectively capturing the underlying trends and periodicities. Subsequently, GBRT is 
applied to the residuals obtained from the smoothing process to model the nonlinear 
relationships  and  correct  any  remaining  errors.  This  two-stage  modelling  strategy 
allows for a comprehensive representation of the load data, addressing both its linear 
and nonlinear characteristics. The hybrid model demonstrated improved forecasting 
accuracy, particularly for daily and weekend load predictions, outperforming models 
that rely solely on either statistical or machine learning techniques.

Error! Reference source not found. illustrates hybrid forecasting model of Hasan et al. 
[26] that combines SVR with a Genetic Algorithm (GA) to predict energy consumption 
across  four  sectors:  residential,  commercial,  industrial,  and  agricultural.  SVR  is  a 
powerful  machine  learning  technique  capable  of  modelling  complex  nonlinear 
relationships in data. However, its performance is highly sensitive to the selection of 
hyperparameters, such as the penalty parameter and kernel function parameters. To 
address  this,  the  authors  employed  a  Genetic  Algorithm  to  optimize  the  SVR 
hyperparameters,  enhancing  the  model's  predictive  accuracy.  The  GA  iteratively 
searches  for  the  optimal  combination  of  parameters  by  simulating  the  process  of 
natural  selection,  thus  avoiding  local  minimum,  and  improving  generalization.  The 
GA-optimized  SVR  model  achieved  higher  forecasting  accuracy  compared  to 
traditional  SVR  and  other  baseline  models,  demonstrating  its  effectiveness  in 
capturing the complex dynamics of energy consumption across different sectors.

3.4.2.  Ensemble tree-based methods

Ensemble-based  models  have  gained  considerable  attention  in  the  field  of  STLF  for 
their  ability  to  enhance  predictive  accuracy,  reduce  overfitting,  and  improve  model 
generalization.  By  combining  the  outputs  of  multiple  learners,  ensemble  methods 
capitalize  on  the  strengths  of  different  models  to  create  more  stable  and  robust 
forecasts, particularly under uncertain and volatile conditions.

Deng  et  al.  [16]  proposed  a  hybrid  ensemble  model  that  integrates  Bagging  with 
XGBoost to address the challenges of forecasting electricity demand during extreme 
weather events. Their model begins by identifying periods of extreme weather using 
time, load, and meteorological features, ensuring that the training process is tailored 
to critical high-variance conditions. To improve relevance and adaptability, the model 
selects  training  data  based  on  a  weighted  similarity  measure,  which  emphasizes 
historical cases most comparable to the current situation.

As  Figure  3.6  illustrates,  the  hybrid  approach  employs  Bagging  to  generate  diverse 
subsets  of  the  selected  training  data.  Each  subset  is  used  to  train  an  independent 
XGBoost  learner,  and  the  final  forecast  is  obtained  by  aggregating  their  outputs—
typically  through  averaging.  This  combination  allows  the  model  to  benefit  from

---

<!-- PAGE 48 -->

38

| Short-term load forecasting

XGBoost’s  ability  to  capture  complex  nonlinear  relationships  while  leveraging 
Bagging to reduce variance and improve generalization.

Results  from  the  study  showed  that  the  Bagging–XGBoost  model  outperformed 
conventional methods, especially in forecasting peak loads during extreme weather. It 
achieved  a  notable  reduction  in  MAPE,  demonstrating  its  robustness  in  volatile 
consumption environments.

This  work  highlights  the  effectiveness  of  ensemble  learning  in  energy  forecasting, 
particularly  in  high-risk  scenarios  where  accuracy  and  reliability  are  critical  to 
maintaining grid stability.

Figure 3.6: Framework of extreme weather identification and STLF [16].

3.4.3.  Neural network-based hybrids

Hybrid neural network models have proven highly effective in the field of electricity 
load  forecasting  due  to  their  capacity  to  simultaneously  capture 
localized 
consumption  patterns  and  long-range  temporal  dependencies.  Among  the  most 
widely  used  configurations  are  models  that  combine  CNNs  with  LSTM  networks. 
These hybrids are particularly valuable in dealing with high-frequency, nonlinear, and 
volatile energy data.

---

<!-- PAGE 49 -->

| Short-term load forecasting

39

CNNs  are  well-suited  for  identifying  spatial  and  short-term  features  in  structured 
input  data.  Their  layered  design  allows  for  efficient  abstraction  and  preprocessing, 
making them an ideal front-end in hybrid architectures. Bendaoud et al. [23] evaluated 
CNN models for short-term load forecasting in Algeria and found that while CNNs 
did not outperform all alternatives in isolation, they performed well when integrated 
with  other  models.  Specifically,  CNNs  demonstrated  strong  performance  in  feature 
extraction, especially when embedded in hybrid systems, enhancing the performance 
of downstream components such as LSTM networks.

Wang et al. [29] advanced this concept by proposing a hybrid model that integrates 
CNNs with extended LSTM networks. In this architecture, CNNs first extract high-
level  spatial  and  short-term  temporal  features,  which  are  then  processed  by  LSTM 
layers to model sequential dependencies. Their study demonstrated that this hybrid 
significantly improved forecast accuracy  in complex  load environments where both 
short-term fluctuations and long-term consumption trends coexist.

Guo  et  al.  [31]  expanded  on  the  CNN–LSTM  hybrid  by  developing  a  multi-scale 
framework that incorporates real-time electricity pricing into the forecasting process. 
Their model captures features at different temporal resolutions using multiple CNN 
layers, allowing for a more nuanced understanding of consumption dynamics. These 
features are passed to LSTM layers to model temporal relationships, leading to higher 
accuracy in both day-ahead and intraday forecasts.

Figure 3.7: A schematic diagram of a CNN-LSTM network based on a multi-modal 
attention mechanism [32].

---

<!-- PAGE 50 -->

40

| Short-term load forecasting

A  more  advanced  adaptation  was  presented  in  Figure  3.7  by  Guo  et  al.  [32],  who 
incorporated  a  multi-modal  attention  mechanism  into  the  CNN–LSTM  hybrid 
structure.  This  model  assigns  attention  weights  to  different  feature  representations 
based  on  their  relevance,  improving  the  interpretability  and  responsiveness  of  the 
forecasting  model.  The  integration  of  attention  further  enhances  performance  by 
allowing the model to focus on critical periods or signals during training.

In parallel, Memarzadeh and Keynia [30] developed an optimized LSTM-based neural 
network specifically for forecasting electricity load and price. Their approach involved 
rigorous  hyperparameter  tuning  and  structural  optimization  using  real  grid  data. 
While  the  model  was  not  explicitly  a  hybrid  in  terms  of  architecture,  it  reflects  the 
importance  of  tailored  LSTM  configurations  when  deployed  in  realistic  energy 
forecasting  scenarios.  The  model  achieved  high  accuracy  in  both  daily  and  hourly 
forecasts, underscoring the practical viability of deep learning in operational planning.

Collectively, these studies confirm the effectiveness of neural network-based hybrid 
models—especially  CNN–LSTM  combinations—in  modelling  the  complex,  multi-
scale characteristics of electricity consumption. By combining the feature abstraction 
capabilities  of  CNNs  with  the  memory  strength  of  LSTMs,  these  models  offer  a 
in  modern  smart  grid 
powerful  approach  for  short-term 
environments.

load  forecasting

3.4.4.  Intelligent and fuzzy logic hybrids

Liapis  et  al.[33]  proposed  a  fuzzy-deep  ensemble  model  specifically  designed  to 
enhance short- and mid-term electric load forecasting. For the day ahead forecasting, 
the model demonstrated particular strength in managing uncertainty and fluctuating 
demand. By integrating fuzzy logic into the structure of a deep neural network, the 
model could incorporate expert-like reasoning and linguistic rules to better interpret 
ambiguous input conditions—such as weather fluctuations or demand variability—
common in daily forecasting tasks.

The fuzzy system managed input imprecision by translating real-world variables into 
fuzzy sets and applying rule-based reasoning, while the deep neural network layers 
captured  complex  nonlinear  relationships  from  historical  load  data.  This  fusion 
enabled  the  model  to  maintain  accuracy  while 
improving  robustness  and 
interpretability.  In  the  case  of  1-day  load  prediction,  the  ensemble  outperformed 
traditional  methods  by  effectively  modeling  sudden  shifts  and  short-term  demand 
spikes,  making  it  especially  suitable  for  operational  planning  in  smart  grid 
environments.

3.4.5.  Transformer-based hybrids

Tian et al. [34] proposed a CNN–Transformer hybrid model tailored for day-ahead 
probabilistic load forecasting, with a particular focus on weekends—periods often

---

<!-- PAGE 51 -->

| Short-term load forecasting

41

marked by irregular consumption behavior and limited historical data. The model 
was designed to address the challenges of accurate prediction under these 
constraints by leveraging both convolutional and attention-based sequence 
modelling techniques.

Based  on  Figure  3.8,  the  architecture  begins  with  a  data  preprocessing  stage  that 
denoises and enhances the raw input using features such as peaks and trends. These 
enriched  one-dimensional  time  series  are  then  processed  through  multiple  CNN 
layers,  which  are  responsible  for  extracting  localized  temporal  features.  CNNs  are 
particularly  effective  in  identifying  short-term  structures  in  load  data,  such  as 
consumption spikes or repetitive daily cycles.

Figure 3.8: Flow chart of the deep learning framework [34].

Once features are extracted, they are passed to a Transformer module, which applies 
self-attention mechanisms to model long-range dependencies within the time series. 
The Transformer’s ability to weigh the importance of different time steps allows it to 
capture  broader  contextual  relationships  that  traditional  recurrent  models  might 
overlook.

To produce probabilistic forecasts, the model incorporates quantile regression as its 
loss function. This enables it to estimate not only point predictions but also confidence 
intervals, which are essential for understanding forecast uncertainty. Additionally, a 
novel loss penalty mechanism is introduced to prioritize weekend-specific accuracy, 
ensuring the model pays greater attention to these more volatile periods.

Evaluation results showed that the model achieved high forecasting accuracy for all 
48  time  points  in  a  day  using  only  two  weeks  of  historical  data.  This  performance 
highlights  the  effectiveness  of  combining  CNNs  and  Transformers,  especially  in

---

<!-- PAGE 52 -->

42

| Short-term load forecasting

scenarios where data availability is limited. The hybrid approach offers a robust and 
flexible solution for utilities seeking reliable short-term forecasts under uncertain or 
sparse conditions.

Table 3.9: Benefits of Hybrid models in STLF.

authors

Benefits

Description

Improved short-term prediction 
accuracy

Bendaoud

et al. [23]

Effective feature extraction in 
hybrid models

Hasan et al.

[26]

Enhanced model generalization

Deng et al.

[16]

Robustness in extreme weather 
conditions

Wang et al.

Better handling of short- and

[29]

long-term dependencies

Guo et al.

Improved accuracy under-prices

[31]

dynamics

Guo et al.

Improved interpretability and

[32]

feature relevance

Combining Exponential 
Smoothing with GBRT captures 
both linear trends and nonlinear 
residual patterns, enhancing 
daily and weekend forecasting 
performance. 
CNNs enhance LSTM 
performance by providing rich 
local and temporal features as 
input for sequence modelling. 
Genetic Algorithm optimizes 
SVR hyperparameters, avoiding 
local minima and improving 
accuracy across multiple energy 
sectors. 
Bagging–XGBoost hybrid 
improves model stability by 
aggregating forecasts from 
multiple learners trained on 
weather-specific subsets. 
CNN layers extract short-term 
features, while extended LSTM 
layers model sequential behavior 
for improved accuracy in 
volatile environments. 
Multi-scale CNN–LSTM hybrid 
captures complex load-price 
relationships across different 
timescales for day-ahead and 
intraday forecasting.

Multi-modal attention 
mechanism enhances CNN–
LSTM hybrid by focusing on

---

<!-- PAGE 53 -->

| Short-term load forecasting

43

Memarzade

h and

Optimized forecasting accuracy

Keynia [30]

Liapis et al.

[33]

Effective handling of uncertainty

Tian et al.

Accurate forecasting with

[34]

limited data

critical input features during 
training.

LSTM architecture is fine-tuned 
using real-world data, 
improving model performance 
in hourly and daily load 
prediction. 
Fuzzy-deep ensemble integrates 
fuzzy rules into deep networks, 
improving reliability and 
robustness in 1-day forecasts. 
CNN–Transformer hybrid with 
quantile loss and weekend-
specific penalties enables precise 
forecasts using only two weeks 
of training data.

Table 3.9 presents a comparative overview of various hybrid forecasting models used 
in STLF, emphasizing the specific advantages each model offers. The benefits range 
from improved predictive accuracy and model generalization to enhanced robustness 
under extreme conditions and better interpretability.

3.5.  Summary

Chapter  3  offers  a  comprehensive  examination  of  STLF,  focusing  on  forecasting 
electricity demand from minutes up to a week. Accurate STLF is essential for efficient 
grid operation, economic dispatch, and demand response management. The chapter 
categorizes  forecasting  models  into  four  main  groups:  statistical  methods,  ML 
methods, deep learning models, and hybrid/ensemble approaches.

Statistical models such as ARIMA and SARIMA provide interpretable forecasts under 
stable  seasonal  conditions,  but  they  struggle  with  nonlinearity  and  high-frequency 
variability.  Regression  models  like  linear  regression  and  quantile  regression  are 
efficient and interpretable, though limited in complex or dynamic contexts.

ML  models  such  as  SVR,  decision  trees,  random  forests,  and  XGBoost  outperform 
traditional methods by capturing nonlinear relationships. SVR, in particular, balances 
accuracy  with  computational  efficiency,  while  tree-based  methods  provide  strong 
generalization and interpretability.

Deep  learning  methods—especially  LSTM  and  ANN—excel  in  modeling  temporal 
dependencies. LSTM outperforms statistical and shallow models by capturing long-

---

<!-- PAGE 54 -->

44

| Short-term load forecasting

and  short-term  dynamics.  ANN  models  are  simpler  and  effective  but  prone  to 
overfitting and require tuning.

Hybrid  models  integrate  multiple  methods  to  enhance  accuracy  and  robustness. 
Examples include exponential smoothing + GBRT, SVR + GA, CNN + LSTM, and CNN 
+  Transformer.  These  combinations  address  both  linear  and  nonlinear  data 
characteristics, improve model generalization, and handle uncertainty, volatility, and 
limited data effectively.

The chapter emphasizes that hybrid and deep learning models are increasingly vital 
for  modern  STLF,  especially  in  smart  grid  environments  where  interpretability, 
scalability, and resilience to variability are crucial.

---

<!-- PAGE 55 -->

| Medium-term load forecasting

45

4  Medium-term load forecasting

MTLF refers to the prediction of electricity demand over a horizon ranging from one 
week  to  one  month.  This  forecasting  range  serves  as  a  bridge  between  short-term 
operational  planning  and  long-term  investment  strategies.  MTLF  is  essential  for 
applications such as energy procurement, maintenance scheduling, capacity planning, 
tariff design, and policy development.

Unlike  short-term  forecasting,  which  deals  with  rapid  fluctuations  in  demand, 
medium-term  forecasting  must  address  broader  seasonal  trends,  monthly  usage 
patterns,  and  external  influences  such  as  climate  variation,  economic  activity,  and 
consumer behavior [17], [35], [36]. The data used is typically aggregated at weekly or 
monthly  levels,  which  introduces  different  modeling  challenges,  including  data 
sparsity, reduced temporal resolution, and delayed response to exogenous variables.

MTLF  models  must  also  account  for  nonlinear  and  nonstationary  behaviors  over 
longer  horizons  while  maintaining  reasonable  interpretability  and  computational 
efficiency. Furthermore, many modern applications demand that forecasts incorporate 
uncertainty estimation and adapt to evolving energy usage conditions, particularly in 
grids with high penetration of renewable energy and flexible loads [25], [37], [38].

This  chapter  reviews  prominent  MTLF  methodologies  across  four  main  categories: 
statistical  models,  machine  learning  techniques,  deep  learning  architectures,  and 
hybrid or ensemble approaches. The aim is to identify the most effective techniques 
for medium-range horizons and understand how these methods address the unique 
challenges of MTLF across residential, commercial, and distribution system levels.

4.1.  Statistical methods

Statistical methods have traditionally served as the foundation for MTLF due to their 
mathematical simplicity, interpretability, and low computational requirements. These 
models are particularly effective when applied to aggregated consumption data—such 
as  weekly  or  monthly  electricity  use—where  periodicity  and  seasonality  can  be 
exploited for accurate prediction [39], [40].

Unlike  short-term  forecasting,  which  often  relies  on  high-frequency  input  variables 
like  real-time  weather  or  occupancy  data,  MTLF  emphasizes  broader  consumption 
patterns over longer horizons. As a result, statistical models in this context focus on

---

<!-- PAGE 56 -->

46

| Medium-term load forecasting

uncovering  trend  structures,  autocorrelation,  and  cyclical  patterns  in  the  data. 
Methods  such  as  linear  regression,  ARIMA,  SARIMA,  and  quantile  regression  are 
frequently employed to model deterministic and probabilistic aspects of medium-term 
electricity demand.

Recent studies have also explored hybrid extensions of classical models, incorporating 
decomposition  (e.g.,  Fourier  transforms)  or  probabilistic  components  (e.g.,  kernel 
density estimation) to improve their adaptability to complex demand dynamics. While 
these approaches may lack the flexibility of modern machine learning techniques, they 
offer transparent forecasting logic, which remains essential for operational decision-
making in power systems and utility planning [40].

The  following  subsections  review  key  statistical  methods  applied  to  medium-term 
electricity  forecasting,  along  with  selected  case  studies  demonstrating  their 
performance, strengths, and limitations.

4.1.1.  Regression-based methods

Regression-based  models  are  among  the  most  frequently  used  techniques  in  MTLF 
due to their simplicity, interpretability, and efficiency when working with aggregated 
data  such  as  monthly  or  weekly  electricity  consumption.  These  models  rely  on 
identifying  statistical  relationships  between  the  target  variable  (typically  electricity 
demand)  and  independent  features  like  historical  load,  temperature  averages,  or 
calendar-based indicators.

LR models assume a constant, additive relationship between predictors and the target. 
This makes them ideal for applications requiring transparent forecasting logic, such as 
tariff  planning  and  capacity  estimation.  They  are  particularly  effective  for  stable 
consumption environments with identifiable seasonal trends.

To improve the accuracy and reliability of medium-term load forecasting, particularly 
under uncertainty, researchers have increasingly turned to quantile regression (QR). 
Unlike traditional regression methods that estimate the Mean of a response variable, 
QR allows forecasting of conditional quantiles (e.g.,  Median, 90th percentile), which 
provides a more nuanced view of the possible outcomes and better captures variability 
in electricity demand.

The quantile regression objective is to minimize the quantile loss function, defined in 
Equation (4.1):

min
𝛽

𝑁
∑ 𝜌𝜏𝑦𝑖 − 𝑥𝑖
𝑖=1

⊤𝛽,

(4.1)

Where 𝜌𝜏(𝑢) = 𝑢(𝜏 − 𝕀{𝑢<0}) is the asymmetric quantile loss function, 𝜏 ∈ (0,1) denotes 
⊤𝛽 is 
the desired quantile (e.g., 𝜏 = 0.5 for the median), 𝑦𝑖 is the actual observation, 𝑥𝑖
the predicted value.

---

<!-- PAGE 57 -->

| Medium-term load forecasting

47

This formulation penalizes over- and under-predictions differently depending on the 
quantile level, enabling forecasters to model both central tendencies and tail risks in 
electricity demand.

Wang et al. [40] developed a combined probabilistic forecasting model that integrates 
quantile regression with kernel density estimation. Their model aimed to forecast peak 
and  base  load  scenarios  by  estimating  a  full  distribution  rather  than  a  single-point 
value.  The  approach  enabled  them  to  reflect  the  uncertainty  inherent  in  electricity 
demand  and  capture  asymmetric  behaviors—such  as  occasional  demand  spikes—
which linear models typically fail to account for. The use of kernel methods further 
enhanced the flexibility of their distribution modeling, making it especially suitable 
for medium-term planning where long-range uncertainty is a significant factor.

Xu [41] provided a comprehensive review of quantile regression applications in both 
renewable energy generation and building load forecasting. The review emphasized 
QR’s ability to model a range of possible demand outcomes, rather than relying solely 
on expected values. Xu noted that QR is particularly beneficial in situations involving 
intermittent renewable inputs or unpredictable user behavior—common challenges in 
medium-term  horizons.  The  method  supports  probabilistic  forecasting,  where 
forecasting ranges are more informative than single-value predictions and are essential 
for grid operators managing risk and planning reserve margins.

In summary, as highlighted in Table 4.1, QR has emerged as a vital tool in medium-
term  load  forecasting  by  offering  interpretable  distributional  insights  into  energy 
demand. It improves robustness under uncertainty and is particularly advantageous 
in dynamic systems influenced by renewable energy, fluctuating occupancy patterns, 
or seasonal effects.

Table 4.1: Strengths and limitations of regression methods in MTLF.

Model Type

Strengths

Weaknesses

Linear Regression

(LR)

Simple; interpretable; fast

to compute; effective for

aggregated data.

Limited to linear patterns; 
underperforms in dynamic or 
nonlinear contexts.

Captures variability and

Quantile

uncertainty; robust to

Regression (QR)

outliers; supports

probabilistic forecasting.

More complex; harder to 
interpret compared to mean-
based methods.

---

<!-- PAGE 58 -->

48

| Medium-term load forecasting

4.1.2.  ARIMA and SARIMA

These models are particularly effective in MTLF due to their ability to capture trend, 
seasonality,  and  autocorrelation  in  aggregated  data  such  as  weekly  or  monthly 
electricity consumption.

Several studies have explored the application and enhancement of statistical models 
such as ARIMA and SARIMA for medium-term load forecasting. Bilgili and Pinar [17] 
employed  a  SARIMA  model  to  forecast  monthly  gross  electricity  consumption  in 
Turkey, demonstrating the model’s effectiveness in capturing long-term patterns and 
consistent seasonal cycles within national electricity profiles. Their results confirmed 
that  while  deep  learning  models  like  LSTM  slightly  outperformed  SARIMA  in 
handling  non-linearities,  SARIMA  stood  out  for  its  model  stability,  computational 
simplicity, and robustness when the data adhered to regular seasonal trends. These 
characteristics make SARIMA a reliable option for institutional forecasting tasks where 
interpretability and efficiency are critical.

In the domain of residential energy forecasting, Gellert et al. [22] applied both ARIMA 
and TBATS models to smart home electricity datasets. Their comparative evaluation 
revealed  that  ARIMA  maintained  solid  performance  under  structured  and  regular 
seasonal conditions. However, the study also identified its limitations when dealing 
with  complex  seasonality  and  higher-frequency  volatility,  suggesting  that  more 
adaptive  models  like  TBATS,  which  support  multiple  seasonalities  and  complex 
temporal dynamics, may be better suited for more irregular patterns often found in 
smart environments.

An innovative development was presented by Karamolegkos and Koulouriotis  [39], 
who introduced a Fourier-enhanced ARIMA model. Though originally designed for 
short-term forecasting in the Greek electricity market, the model integrated seasonal 
decomposition using Fourier series to isolate dominant frequency components. This 
technique  enhances  the  model’s  ability  to  detect  and  forecast  cyclical  consumption 
patterns, making it highly adaptable for medium-term horizons as well. The approach 
allows  for  better  alignment  between  statistical  model  structures  and  the  periodic 
behaviors  of  electricity  demand,  especially  in  contexts  where  multiple  seasonal 
influences coexist.

Additionally, Wang et al. [35] proposed a forecasting model based on accumulative 
time-delay effects and periodic fluctuation components. Although this model is not a 
conventional  ARIMA-type  model,  it  shares  key  structural  principles  such  as  time-
series decomposition and explicit modeling of deterministic and stochastic elements. 
The model was validated using monthly electricity consumption data, illustrating its 
suitability for MTLF tasks. It demonstrated particular strength in capturing recurring 
cycles  and  long-term  behavioral  trends,  contributing  to  more  accurate  and 
interpretable forecasts.

---

<!-- PAGE 59 -->

| Medium-term load forecasting

49

Together,  these  studies  demonstrate  that  while  traditional  ARIMA-based  models 
provide a robust foundation for medium-term load forecasting (MTLF)—particularly 
when the data exhibits stable and consistent seasonality—advanced adaptations such 
as  Fourier-enhanced  ARIMA  and  models  incorporating  hybrid  periodic  structures 
significantly improve forecasting performance in more complex,  dynamic scenarios, 
as summarized in Table 4.2.

Table 4.2: Strengths and limitations of ARIMA and SARIMA in MTLF.

Model Type

Strengths

Weaknesses

Suitable for stationary or

near-stationary monthly

ARIMA

data; interpretable with

transparent parameter

structure.

Strong at modelling regular

monthly or seasonal cycles;

SARIMA

robust in national or utility-

scale MTLF with stable

patterns.

Effectively models multi-

period cycles using

Fourier-ARIMA

harmonic decomposition;

enhances ARIMA flexibility

for MTLF.

Assumes linearity and lacks 
adaptability to nonlinear 
patterns; limited performance 
with irregular long-term 
trends.

Struggles with multiple or 
shifting seasonalities; sensitive 
to season length and requires 
precise parameterization.

Increases model complexity; 
requires accurate frequency 
selection and decomposition 
expertise.

4.2.  ML models

ML  techniques  have  emerged  as  powerful  alternatives  to  traditional  statistical 
approaches in electricity load forecasting. These models are particularly effective at 
capturing complex, nonlinear patterns in historical consumption data and can adapt 
to dynamic changes in usage behavior. ML models do not require strong assumptions 
about the underlying data distribution, making them suitable for diverse forecasting 
horizons and load profiles.

Recent studies have shown that ML models can outperform classical models in both 
accuracy and generalizability, especially when sufficient historical and contextual data 
are available. Commonly used machine learning methods in load forecasting include 
SVR,  decision  tree-based  algorithms,  k-NN,  and  ANN,  each  offering  specific 
advantages in terms of interpretability, scalability, and performance under different 
forecasting conditions.

---

<!-- PAGE 60 -->

50

| Medium-term load forecasting

4.2.1.  Tree-based models

Tree-based  models  are  highly  effective  for  MTLF  due  to  their  ability  to  manage 
complex,  nonlinear  relationships  between  features  and  the  target  variable.  These 
models are capable of automatically capturing interactions between features without 
requiring  extensive  preprocessing,  making  them  particularly  useful  for  forecasting 
electricity consumption, which can exhibit both seasonal and irregular patterns. The 
most  commonly  used  tree-based  algorithms  in  load  forecasting  are  Decision  Trees, 
Random Forests, and GBMs, including XGBoost and LightGBM.

4.2.1.1.  Decision trees

Decision Trees are a fundamental tree-based model that recursively splits the feature 
space into regions that are as homogeneous as possible in terms of the target variable. 
This  method  is  intuitive  and  easy  to  interpret,  making  it  valuable  for  practical 
applications in MTLF. While Decision Trees can suffer from overfitting, they provide 
a clear visualization of how the model arrives at its predictions. They are particularly 
useful for capturing simple patterns in the data and can serve as the foundation for 
more complex models like Random Forests and Gradient Boosting.

4.2.1.2.  Random forests

RF are an ensemble method that builds multiple decision trees using random subsets 
of  the  data  and  aggregates  their  predictions.  This  approach  reduces  the  risk  of 
overfitting associated with a single Decision Tree and improves model generalization. 
Random  Forests  are  highly  effective  at  handling  high-dimensional  data  and  can 
capture complex interactions among features. For medium-term load forecasting, RF 
models can effectively model seasonal variations and nonlinear trends in electricity 
consumption. Their robustness and simplicity make them a popular choice for load 
forecasting.

4.2.1.3.  XGBoost

XGBoost is an optimized implementation of GBMs that incorporates techniques such 
as regularization to reduce overfitting and improve model accuracy. It has become one 
of  the  most  popular  tree-based  algorithms  for  forecasting  tasks  due  to  its  ability  to 
manage  large  datasets  with  high  computational  efficiency.  In  the  context  of  MTLF, 
XGBoost  has  demonstrated  strong  performance  in  predicting  future  load  values  by 
effectively capturing both short-term fluctuations and longer-term trends in electricity 
usage.

---

<!-- PAGE 61 -->

| Medium-term load forecasting

51

4.2.1.4.  GBMs

As Error! Reference source not found. illustrates, GBMs are an ensemble learning t
echnique that builds a series of decision trees in a sequential manner. At each step, a 
new  tree  is  fitted  to  the  residual  errors  (the  gradients)  of  the  existing  model.  The 
primary idea is to reduce the prediction error by adding trees that correct the mistakes 
made by previous trees. Mathematically, the process can be described as follows:

Figure 4.1: Architecture of XGBoost model [36].

1.  Initialization:  The  process  begins  with  an  initial  model  𝐹0(𝑥)  that  makes  an 
initial  prediction  based  on  the  training  data.  This  could  be  as  simple  as 
predicting the mean of the target variable y as it is shown in Equation (4.2):

𝐹0(𝑥) =

1
𝑁

𝑁
∑ 𝑦𝑖,
𝑖=1

(4.2)

Where 𝐹0(𝑥) is the initial model prediction, 𝑁 is the number of training samples, 
𝑦𝑖 is the true value of the sample.

2.  Gradient Calculation: At each iteration m, a new tree ℎ𝑚(𝑥) is built to predict 
the  negative  gradient  (residuals)  of  the  loss  function  L  with  respect  to  the 
current prediction 𝐹𝑚−1(𝑥) based on Equation (4.3):

(𝑚) = −
𝑟𝑖

𝜕𝐿(𝑦𝑖𝐹𝑚−1(𝑥𝑖))
𝜕𝐹𝑚−1(𝑥𝑖)

,

(4.3)

(𝑚)

Where 𝑟𝑖
is the loss function (e.g., mean squared error or log-loss).

is the residual for the 𝑖𝑡ℎ sample at the 𝑚𝑡ℎ iteration. 𝐿(𝑦𝑖𝐹𝑚−1(𝑥𝑖))

3.  Model  Update:  based  on  Equation  (4.4)  The  new  tree  ℎ𝑚(𝑥)  is  added  to  the 
previous model 𝐹𝑚−1(𝑥) , and the model is updated by adding a scaled version 
of ℎ𝑚(𝑥) with a learning rate η:

---

<!-- PAGE 62 -->

52

| Medium-term load forecasting

𝐹𝑚(𝑥) = 𝐹𝑚−1(𝑥) + 𝜂. ℎ𝑚(𝑥),

(4.4)

Where 𝐹𝑚(𝑥) is the updated model after the 𝑚𝑡ℎ tree is added, ℎ𝑚(𝑥) is the new 
tree fitted to the residuals, 𝜂 is the learning rate, which controls the contribution 
of each new tree to the final prediction.

4.  Final Model: After M trees are added, the final model is given by Equation (4.5):

𝑀

𝐹𝑀(𝑥) = 𝐹0(𝑥) + ∑ 𝜂. ℎ𝑚(𝑥),

𝑚=1

(4.5)

This  process  allows  GBMs  to  iteratively  reduce  the  residual  error,  thus  improving 
prediction accuracy over multiple iterations.

4.2.1.5.  LightGBM

LightGBM is an optimized version of GBMs that improves computational efficiency 
and scalability, particularly for large datasets. It achieves this by using a histogram-
based  method  for  finding  optimal  splits,  as  well  as  other  optimizations.  LightGBM 
introduces  several  innovations,  including  leaf-wise  tree  growth  and  discretizing 
continuous  features  into  bins,  which  leads  to  faster  training  and  reduced  memory 
usage. Here is how the method works:

1.  Discretization  of  Features:  LightGBM  discretizes  continuous  features  into 
discrete bins. Based on Equation (4.6), given a feature x, it divides its range into 
B  bins  (for  example, [𝑥1, 𝑥2, 𝑥3, ⋯ , 𝑥𝐵]).  This  reduces  the  number  of  distinct 
feature values considered during split selection, leading to faster computation.

𝑥𝑖 ∈ {𝑏1, 𝑏2, 𝑏3, ⋯ , 𝑏𝐵},

(4.6)

Where 𝑏1, 𝑏2, 𝑏3, ⋯ , 𝑏𝐵 are the bins that the feature values are discretized into. 
2.  Leaf-wise Tree Growth: Unlike  traditional GBMs that  use level-wise growth 
(splitting all nodes at the same level), LightGBM grows trees leaf-wise, where it 
splits the leaf with the highest residual sum of squares (RSS) based on Equation 
(4.7).  This  often  results  in  deeper  trees  but  improves  model  accuracy  by 
capturing more complex patterns. The tree is grown as follows:

𝑅𝑆𝑆𝑙 = ∑(𝑟𝑖

(𝑚))

2

,

𝑖∈𝑙

(4.7)

Where 𝑅𝑆𝑆𝑙 is the residual sum of squares for leaf l, 𝑟𝑖
the 𝑖𝑡ℎ sample at the 𝑚𝑡ℎ iteration.

(𝑚)

is the residual error for

---

<!-- PAGE 63 -->

| Medium-term load forecasting

53

3.  Gradient Calculation and Tree Fitting: Similar to traditional GBM, LightGBM 
fits a tree to the residuals. However, LightGBM optimizes the process by using 
histograms  of  the  residuals  to  approximate  the  best  possible  splits  for  each 
feature. The negative gradient for a given leaf is shown in Equation (4.8):

(𝑚) = −
𝑟𝑖

𝜕𝐿(𝑦𝑖𝐹𝑚−1(𝑥𝑖))
𝜕𝐹𝑚−1(𝑥𝑖)

,

(4.8)

4.  Model Update: The model is updated in the same manner as GBMs, but as it is 
seen  in  Equation  (4.9)  the  updates  are  faster  due  to  the  histogram-based 
approach and the leaf-wise tree growth:

5.  Final Model: After M trees are added, the final model in LightGBM is defined

𝐹𝑚(𝑥) = 𝐹𝑚−1(𝑥) + 𝜂. ℎ𝑚(𝑥),

(4.9)

by Equation (4.10):

𝑀

𝐹𝑀(𝑥) = 𝐹0(𝑥) + ∑ 𝜂. ℎ𝑚(𝑥),

(4.10)

𝑚=1

Tree-based models have demonstrated strong performance in MTLF, particularly due 
to  their  ability  to  capture  nonlinear  dependencies,  incorporate  external  factors,  and 
scale well with large datasets. Zhu et al. [42] applied a decision tree-based approach to 
forecast electricity consumption in smart grids. Using data that included both seasonal 
and  non-seasonal  patterns,  the  model  successfully  captured  key  demand  dynamics 
with  high  interpretability.  While  the  study  did  not  report  significant  gains  over 
ensemble  models,  it  emphasized  the  model’s  clarity  and  practical  deployment  in 
operational smart grid settings.

In  contrast,  Mathew  et  al.  [36]  developed  the  Prominence-guided  Weighted  Peaks 
(PWP) XGBoost model to improve the accuracy of feeder-level peak load forecasting. 
The  model  was  trained  on  feeder-level  electricity  data  supplemented  with  external 
variables  such  as  weather  and  economic  indicators.  Compared  to  conventional 
methods,  the  PWP-XGBoost  achieved  lower  forecasting  errors,  particularly  in  peak 
demand estimation—an essential factor for maintaining grid stability. The inclusion of 
domain-specific  knowledge  into  the  XGBoost  framework  contributed  to  improved 
precision in capturing complex medium-term load fluctuations.

Similarly, Royal et al. [43] applied the Light Gradient Boosting Machine (LightGBM) 
model to medium-term electricity load forecasting tasks. The model was trained on 
time-series  datasets  characterized  by  strong  temporal  dependencies  and  nonlinear 
behaviors.  LightGBM  outperformed  traditional  statistical  models,  achieving  lower 
error metrics and demonstrating high computational efficiency due to its histogram-

---

<!-- PAGE 64 -->

54

| Medium-term load forecasting

based learning and feature bundling techniques. These attributes made it particularly 
effective  in  forecasting  medium-term  load  trends  across  diverse  operational 
conditions.

Additionally, Dinmohammadi et al. [44] conducted a comparative study of Random 
Forest (RF) and Gradient Boosting (GB) models for medium-term load forecasting. The 
study evaluated performance across multiple regions and timescales and found that 
RF delivered more stable and consistent accuracy across diverse conditions, while GB 
models  showed  slightly  better  performance  in  capturing  complex  patterns  when 
properly  tuned.  Both  models  outperformed  linear  baselines,  especially  when 
hyperparameters were optimized. Notably, the authors emphasized the importance of 
hyperparameter tuning and cross-regional evaluation for generalization. This  study 
further  validated  that  ensemble-based  tree  methods,  particularly  when  enhanced 
through tuning and regional adaptation, provide a strong foundation for scalable and 
accurate MTLF.

Together,  these  studies  highlight  the  strength  of  decision  tree-based  methods—
particularly  advanced  ensembles  like  XGBoost  and  LightGBM—in  improving 
forecasting accuracy and interpretability across medium-term electricity consumption 
horizons, as summarized in Table 4.3.

Table 4.3: Advantages and disadvantages of Tree-based models in MTLF.

Model Type

Strengths

Weaknesses

Decision Trees

Random Forest

XGBoost

Simple and interpretable;

Can model seasonal and

structural patterns in

medium-term consumption

data; Quick to train on

smaller regional datasets.

Reduces overfitting by

averaging multiple trees;

Performs well across

diverse urban datasets with

multiple influencing factors

(e.g., weather, economy);

Robust to noise in medium-

term historical data.

Handles complex temporal

patterns (e.g., seasonality

and cyclical effects)

effectively; Performs well

Prone to overfitting without 
pruning; May struggle with 
capturing subtle temporal 
dependencies across longer 
horizons; Limited 
generalization, often 
outperformed by ensembles.

Slower to predict as horizon 
and data volume increase; 
Less interpretable; Requires 
careful handling of temporal 
features for accurate long-
horizon forecasts.

Parameter tuning is critical to 
prevent overfitting on 
medium-range cycles; 
Interpretation is more

---

<!-- PAGE 65 -->

| Medium-term load forecasting

55

on high-dimensional

medium-term datasets;

Excellent for capturing

challenging; May require 
preprocessing of time-based 
features.

interactions across multiple

time-lagged inputs.

Scalable and memory-

efficient—well-suited for

large regional datasets;

Captures nonlinear and

LightGBM

temporal trends over

months; Native handling of

categorical variables is

useful for calendar-based

MTLF features.

May overfit if trees are too 
deep or not regularized; 
Performance can degrade on 
datasets with irregular or 
sparse medium-term 
structure; Requires careful 
feature engineering.

4.2.2.  k-NN

k-NN is a simple and intuitive machine learning algorithm used for both classification 
and regression tasks. In the context of MTLF, k-NN plays a significant role due to its 
ability to predict future electricity consumption by identifying similar past patterns in 
the data. The strength of k-NN lies in its non-parametric nature, meaning that it does 
not make any assumptions about the underlying distribution of the data. Instead, it 
learns  directly  from  the  data,  which  makes  it  adaptable  to  complex  and  nonlinear 
patterns in electricity demand.

In MTLF, k-NN is typically used to forecast future load values based on historical data. 
The forecasting horizon for medium-term load forecasting generally spans from a few 
days  to  several  weeks,  making  it  crucial  to  capture  long-term  seasonal  trends  and 
short-term fluctuations in electricity consumption. The key benefit of k-NN is its ability 
to  model  temporal  relationships  by  considering  similar  past  patterns  when  making 
predictions.

---

<!-- PAGE 66 -->

56

| Medium-term load forecasting

In  the  realm  of  medium-term  load  forecasting,  several  studies  have  successfully 
applied k-NN, demonstrating its effectiveness in predicting electricity consumption. 
As Figure 4.2 illustrates, Dong et al. [45] used k-NN combined with NSGA-II (Non-
dominated  Sorting  Genetic  Algorithm)  for  optimizing  the  number  of  neighbors  (k) 
used in the model. This hybrid model was assessed using electricity consumption data 
from  an  urban  grid  and  showed  a  significant  improvement  in  forecasting  accuracy 
over traditional methods such as ARIMA and SVM. The optimization process, through 
NSGA-II,  also reduced  the  computational  burden  while  maintaining  high  accuracy, 
particularly  in  capturing  the  seasonal  fluctuations  in  load  demand  over  a  medium-
term horizon.

Figure 4.2: Framework of the proposed interval forecasting model and principles of 
NSGA-II, KNN, DBN and modified KDE [45].

Similarly, Khan et al. [46] explored the application of k-NN combined with Deep Belief 
Networks (DBN) for medium-term load forecasting in smart grids. In this study, k-NN 
was used to extract relevant features from the historical electricity consumption data, 
which were then used as inputs for the DBN model. The results demonstrated that this 
hybrid approach significantly outperformed traditional models like ANN and SVR, 
especially when dealing with the nonlinear patterns and demand fluctuations due to 
external factors such as temperature and economic activity. The study also highlighted 
that  k-NN's  role  in  feature  selection  played  a  critical  part  in  improving  the 
performance and scalability of the DBN model.

In their study, Dudek & Pełka [47] focus on the application of Pattern Similarity-Based 
Machine  Learning  Methods  (PSFMs)  for  MTLF.  Specifically,  they  investigate  the 
effectiveness  k-NN  within  this  framework  for  forecasting  monthly  electricity 
consumption. By leveraging historical load data, the authors demonstrate how k-NN 
can identify similar past consumption patterns and use them to predict future demand. 
Their results show that k-NN, despite its simplicity, outperforms traditional models 
such as ARIMA and SVR in capturing the seasonal variations and nonlinear patterns 
inherent  in  electricity  consumption.  The  study  highlights  that  k-NN  offers  both 
computational  efficiency  and  forecasting  accuracy,  especially  when  combined  with

---

<!-- PAGE 67 -->

| Medium-term load forecasting

57

other  techniques  in  a  hybrid  model,  making  it  a  valuable  tool  for  medium-term 
forecasting tasks.

k-NN  continues  to  be  a  valuable  method  for  medium-term  load  forecasting.  Its 
simplicity  and  non-parametric  nature  make  it  adaptable  to  a  variety  of  datasets, 
especially  when  combined  with  optimization  and  deep  learning  techniques.  The 
studies reviewed demonstrate that k-NN, when used alone or in hybrid models, can 
improve  forecasting  accuracy,  reduce  computational  complexity,  and  capture  the 
essential seasonal patterns in electricity demand. A summary of the advantages and 
disadvantages of k-NN in medium-term load forecasting can be found in Table 4.4.

Table 4.4: Advantages and disadvantages of K-NN in MTLF.

Model Type

Strengths

Weaknesses

Simple and intuitive

method, easy to implement

and interpret; non-

parametric: Does not make

assumptions about the

underlying data

distribution; works well

with complex, nonlinear

relationships between

features; Adaptable to

dynamic patterns; can

K-NN

easily incorporate new data

without retraining; can

model seasonality and

trends by considering

historical data similarity;

good for capturing local

patterns in electricity

consumption; effective

when combined with other

models (e.g., hybrid models

with optimization

techniques).

Computationally expensive 
during prediction because it 
requires calculating distances 
to all training samples; 
sensitive to the curse of 
dimensionality: performance 
can degrade with a high 
number of features; sensitive 
to noisy data: outliers can 
heavily influence predictions; 
choice of k is crucial: the 
performance heavily depends 
on selecting the right number 
of neighbours; memory-
intensive: requires storing 
large datasets, which may be 
impractical for large datasets 
over long time periods; does 
not work well with 
imbalanced datasets where 
certain patterns dominate;  
slow inference time: Requires 
comparing each test sample to 
all training samples, which 
can be slow for large datasets.

---

<!-- PAGE 68 -->

58

4.2.3.  ANN

| Medium-term load forecasting

ANNs  are  particularly  effective  in  forecasting  electricity  consumption,  which  is 
influenced by complex patterns such as seasonality, weather variability, day-of-week 
effects, and economic activity. Their ability to model nonlinear relationships and learn 
from  both  historical  data  and  external  features  allows  ANNs  to  capture  temporal 
patterns (daily, weekly, and seasonal cycles) as well as long-term consumption trends. 
As  such,  they  are  widely  used  in  energy  management,  grid  optimization,  and 
electricity demand forecasting.

Khan  et  al.  [46]  investigated  a  hybrid  model  that  combines  ANNs  with  DBN  for 
medium-term load forecasting in smart grid environments. The primary aim was to 
enhance ANN performance through DBN-based feature extraction and optimization. 
The model was trained using a comprehensive dataset that included not only historical 
load  profiles  but  also  external  parameters  such  as  temperature  and  economic 
indicators.  Results  showed  that  the  ANN-DBN  hybrid  model  significantly 
outperformed standalone ANN and SVR models. Specifically, the ANN-DBN model 
achieved a MAPE of 2.83%, compared to 3.54% for SVR and 3.11% for the conventional 
ANN, demonstrating the efficacy of deep learning integration in capturing complex 
nonlinear dependencies and improving forecast accuracy.

Wazirali et al. [48] focused on medium-term load forecasting for microgrids using a 
standalone  ANN  model.  The  study  utilized  historical  electricity  consumption  data 
along with seasonal indicators to train the network for predicting demand over a one-
month  horizon.  The  authors  highlighted  the  ANN’s  ability  to  model  nonlinear 
dependencies  and  capture  cyclical  patterns  influenced  by  weather  and  calendar 
effects.  When  benchmarked  against  traditional  statistical  methods  like  ARIMA,  the 
ANN model exhibited superior performance, achieving a MAPE of 3.76%, compared 
to 5.21% for ARIMA. This confirmed that ANNs provide a more flexible and accurate 
framework  for  modeling  dynamic  load  behavior,  especially  in  distributed  energy 
systems.

Ghiassi  et  al.  [49]  introduced  a  Dynamic  Artificial  Neural  Network  (DAN2) 
architecture specifically designed for medium-term load forecasting in the context of 
U.S. electricity utilities. Unlike conventional static feedforward networks, the DAN2 
model dynamically determines its structure during training based on data behavior, 
allowing it to adapt more effectively to nonlinear demand variations. The model was 
evaluated using real-world system load data from the California Independent System 
Operator  (CAISO),  forecasting  load  over  a  30-day  horizon.  The  DAN2  model  was 
benchmarked  against  standard  ANN  and  ARIMA  models  using  several  metrics, 
including  RMSE  and  MAE.  Results  showed  that  DAN2  reduced  RMSE  by  11.3% 
compared  to  static  ANN  and  by  17.8%  compared  to  ARIMA.  These  results 
demonstrate that dynamically evolving ANN architecture can better manage complex

---

<!-- PAGE 69 -->

| Medium-term load forecasting

59

temporal  dependencies  in  electricity  load  forecasting,  especially  when  trends  and 
patterns shift over time.

Yalcinoz and Eminoglu [50] examined both short-term and medium-term electricity 
load forecasting using feedforward MLP neural networks trained on real distribution 
system data from Turkey. For the medium-term case, they focused on weekly forecasts 
over  a  one-month  horizon,  integrating  inputs  such  as  temperature,  humidity,  and 
historical load. Multiple ANN configurations were evaluated based on the number of 
hidden  layers,  activation  functions,  and  learning  algorithms.  Their  best-performing 
model achieved a MAPE of 2.38%, MAE of 12.1 MW, and RMSE of 17.5 MW for the 
medium-term  forecast.  These  results  confirmed  that  ANNs  provided  significantly 
better performance than linear regression models, which had a MAPE exceeding 4.6% 
under the same conditions. The study also highlighted that incorporating weather data 
as external inputs and optimizing the neural architecture were critical in enhancing 
prediction accuracy and robustness.

Both  early  and  recent  studies  demonstrate  the  successful  application  of  ANNs  in 
medium-term  load  forecasting.  While  Wazirali  et  al.  [48]  emphasized  the  ANN's 
strength  in  modeling seasonal  and  nonlinear  variations  in  microgrid  environments, 
Khan et al. [46] demonstrated that coupling ANNs with deep learning techniques like 
DBN  significantly  enhances  feature  learning  and  forecasting  accuracy.  Similarly, 
Ghiassi et al. [49] showcased the benefits of dynamic network structures that evolve 
during training, allowing ANNs to better adapt to shifting demand patterns. Yalcinoz 
and Eminoglu [50] highlighted the effectiveness of carefully configured feedforward 
networks  in  achieving  high  accuracy  with  limited  data.  Despite  these  advances,  all 
approaches  point  to  common  challenges,  including  the  requirement  for  large  and 
diverse training datasets, computational cost, and the need for careful tuning of model 
parameters to prevent overfitting and ensure generalizability.

A summary of the advantages and disadvantages of using ANNs for medium-term 
load forecasting is provided in Table 4.5.

---

<!-- PAGE 70 -->

60

| Medium-term load forecasting

Table 4.5: Advantages and disadvantages of ANN in MTLF.

Model Type

Strengths

Weaknesses

Can model complex

nonlinear relationships

between features and target

variables; flexible

architecture allows

adaptation to various

forecasting problems; high

accuracy in forecasting due

ANN

to its ability to capture

intricate patterns in data;

works well with high-

dimensional data, and can

leverage multiple input

features; can handle

missing data and noisy

data through robust

learning algorithms.

Requires large amounts of 
data to train effectively and 
generalize well; training can 
be computationally expensive, 
especially for deep networks; 
overfitting can occur if the 
model is not regularized 
properly; requires careful 
tuning of hyperparameters 
(e.g., learning rate, number of 
layers); less interpretable than 
simpler models like decision 
trees or random forests.

4.3.  Deep learning models

Deep learning models have gained significant attention in the field of MTLF due to 
their ability to model complex, high-dimensional relationships in data, making them 
well-suited  for  predicting  electricity  demand  over  medium-term  horizons.  Unlike 
traditional machine learning models, deep learning models consist of multiple layers 
of  neural  networks,  which  enable  them  to  learn  abstract  features  from  raw  data 
without the need for explicit feature engineering.

In MTLF, deep learning models are especially effective for capturing both temporal 
dependencies  (e.g.,  daily,  weekly,  and  seasonal  fluctuations)  and  nonlinear 
relationships  between  various  influencing  factors,  such  as  weather  conditions, 
historical load data, and economic activity.

4.3.1.  RNN

RNNs,  particularly  their  advanced  variant  known  as  LSTM  networks,  have  gained 
prominence  in the domain of time series  forecasting due to their inherent ability to 
model temporal dependencies. Unlike traditional statistical approaches, which often 
rely on assumptions of stationarity and linearity, RNNs are capable of capturing both

---

<!-- PAGE 71 -->

| Medium-term load forecasting

61

short-  and  long-term  patterns  in  dynamic,  nonlinear  datasets,  making  them  highly 
suitable for MTLF.

Muzaffar  and  Afshari  [51]  investigated  the  effectiveness  of  LSTM  networks  for 
electrical  load  forecasting  by  using  hourly  data  spanning  13  months.  Their  study 
included  not  only  the  load  time  series  but  also  exogenous  environmental  variables 
such  as  temperature.  Recognizing  the  importance  of  seasonality  and  trend 
components 
implemented  a  rigorous 
preprocessing  framework.  This  included  normalization,  handling  of  missing  values 
and outliers, and decomposition of the time series to isolate daily, weekly, and yearly 
seasonalities. Notably, while traditional methods required fully stationarized inputs, 
the  LSTM  network  only  necessitated  the  removal  of  yearly  seasonality  to  prevent 
misinterpretation of one-year trends as ongoing patterns.

in  energy  consumption,

the  authors

The LSTM network was trained on 12 months of data and validated using the 13th 
month.  The  network  architecture  comprised  60  hidden  units,  employed  the  Adam 
optimizer with a learning rate of 0.005, and was trained over 400 epochs. To enable 
temporal  learning,  input  sequences  were  constructed  using  a  lag  of  five-time  steps. 
This  design  allowed  the  model  to  forecast  future  values  based  on  dependencies 
observed in preceding data points.

Forecasts  were  generated  for  several  horizons—24  hours,  48  hours,  7  days,  and  30 
days—and evaluated using RMSE and MAPE. Results showed that the LSTM model 
significantly outperformed classical statistical models such as ARMA, SARIMA, and 
ARMAX  in  short-term  and  intermediate  horizons.  For  instance,  LSTM  achieved  a 
MAPE of 1.52% for a 24-hour forecast, compared to 5.42% with ARMA and 6.53% with 
SARIMA.  Even  at  48  hours,  LSTM  maintained  superior  accuracy  with  a  MAPE  of 
2.16%. However, its performance declined on the 30-day horizon, where it reported a 
MAPE  of  9.75%,  higher  than  the  5.39%  obtained  using  ARMAX.  This  drop  was 
attributed to the model’s limited exposure to long-term patterns due to the relatively 
short training duration of one year.

The study highlights several critical observations: LSTM’s forecasting performance is 
highly sensitive to model hyperparameters such as the number of hidden units, lag 
values, and training epochs. Moreover, its ability to generalize and capture seasonality 
improves with more extensive training data. Despite its slightly lower performance in 
longer-term  forecasts  within  this  study,  the  LSTM  model  demonstrated  clear 
advantages  in  modeling  nonlinearities  and  incorporating  multiple  input  features 
without the need for manual feature selection.

In conclusion, RNNs—especially LSTM architectures—offer a powerful alternative to 
traditional  MTLF  models,  particularly  when  rich,  multivariate,  and  temporally 
structured  datasets  are  available.  Their  capacity  to  learn  from  raw  sequences  and 
model complex temporal relationships enables more accurate and adaptable forecasts, 
especially over short to medium forecast horizons. As summarized in Table 4.6, these

---

<!-- PAGE 72 -->

62

| Medium-term load forecasting

models  provide  notable  advantages  in  terms  of  flexibility  and  accuracy  but  require 
careful  handling  of  data  volume,  preprocessing,  and  hyperparameter  tuning  to 
mitigate limitations such as overfitting and computational cost.

Table 4.6: Advantages and disadvantages of RNN and LSTM in MTLF.

Model Type

Strengths

Weaknesses

RNN and LSTM

Capable of capturing both

short- and long-term

dependencies in sequential

data; well-suited for

modelling nonlinear and

complex temporal patterns

in electricity load; can

incorporate multiple

exogenous variables (e.g.,

temperature, humidity)

without explicit feature

engineering; outperforms

traditional statistical

models (e.g., ARMA,

SARIMA) in short- and

medium-term horizons

when sufficient data is

available.

Requires large volumes of 
high-quality training data to 
generalize seasonal trends 
effectively; training can be 
computationally intensive and 
time-consuming; model 
performance is highly 
sensitive to hyperparameters 
such as lag size, number of 
hidden units, and training 
epochs; risk of overfitting if 
not properly regularized or if 
the training dataset is too 
short.

4.3.2.  Transformer-based models

Transformer  architectures,  originally  introduced  for  natural  language  processing, 
have recently emerged as powerful alternatives to traditional neural networks in time 
series forecasting. Their ability to model long-range dependencies through attention 
mechanisms,  combined  with  high  parallelism  during  training  and  inference,  makes 
them  especially  well-suited  for  MTLF—a  task  defined  here  as  predicting  electricity 
demand over periods ranging from one week to one month.

In MTLF, models must detect and extrapolate periodic patterns, seasonal trends, and 
the influence of external variables such as temperature, humidity, or electricity prices. 
RNNs, including their gated variants like LSTMs and GRUs, are naturally suited to 
sequence  modelling  but  suffer  from  limitations  such  as  vanishing  gradients  and 
inherently sequential computations, which hinder scalability. In contrast, transformers 
process entire sequences simultaneously, enabling them to learn global relationships 
more efficiently.

---

<!-- PAGE 73 -->

| Medium-term load forecasting

63

To  address  the  computational  limitations  of  traditional  transformers  in  time  series 
forecasting, Chan and Yeo [52] proposed a sparse attention transformer for electricity 
load  prediction.  This  model  replaced  the  quadratic-cost  dot-product  attention  with 
BigBird-style  sparse  attention,  significantly  reducing  memory  requirements  while 
maintaining strong forecasting accuracy. The sparse transformer was shown to scale 
effectively  with  long  input  sequences  (up  to  nine  weeks)  and  performed  well  for 
forecast horizons up to one week, making it applicable to medium-term use cases. In 
empirical comparisons with benchmark models such as LSTM and TSRNN, the sparse 
transformer  achieved  comparable  or  better  accuracy  while  offering  up  to  5×  faster 
inference time—a notable advantage for real-time grid operations.

Building  on  these  advances,  Peng  and  Yang  [37]  introduced  LDTformer,  a 
transformer-based  model  designed  specifically  for  short-  and  medium-term  power 
load forecasting. The model integrates domain-aware architectural enhancements that 
enable  it  to  capture  both  high-frequency  fluctuations  and  long-term  temporal 
dependencies, crucial for forecasting electricity demand over multiple weeks.

LDTformer includes several innovative components:

•  A Block Sparse Discrete Cosine Transform (BSDCT) module that converts time-
series segments into the frequency domain, improving the extraction of periodic 
patterns while reducing computational cost.

•  A Seasonal-Trend Decomposition (STD) module, which dynamically separates 
input signals into seasonal and trend components using a mixture-of-experts 
architecture. This improves the model’s adaptability to nonstationary behavior 
in load profiles.

•  A Lagged Correlation Frequency Attention (LCFA) mechanism that introduces 
learnable lag-specific weights in the frequency domain, enhancing the model’s 
ability to detect long-range and periodic dependencies.

•  Causal convolutional layers to enforce temporal consistency while enriching the

local context.

These enhancements enable LDTformer to significantly outperform baseline models—
including Transformer, LSTM, FEDformer, and Mamba—across different seasons and 
forecasting  windows  ranging  from  one  to  four  weeks.  For  example,  using  summer 
data with a forecast length of 192 time points (equivalent to four weeks at 30-minute 
intervals),  LDTformer  achieved  a  MAE  of  0.173  and  symmetric  mean  absolute 
percentage  error  (SMAPE)  of  0.0186,  outperforming  all  comparison  models  by 
substantial  margins.  Additionally,  the  model  demonstrated  greater  robustness  to 
sharp fluctuations and seasonal variations, which are typical in real-world electricity 
consumption.

A comparative summary of transformer-based models used in MTLF is provided in 
Table  4.7,  which  outlines  their  relative  strengths  and  weaknesses.  While  the  vanilla

---

<!-- PAGE 74 -->

64

| Medium-term load forecasting

transformer  is  effective  at  capturing  long-range  dependencies,  it  suffers  from  high 
computational costs and lacks domain-specific enhancements. The sparse transformer 
addresses  these  efficiency  issues,  offering  scalability  with  minimal  accuracy  loss. 
Meanwhile,  LDTformer  represents  the  most  advanced  solution,  delivering  top-tier 
performance  by  combining  frequency-domain  analysis,  decomposition  techniques, 
and lag-sensitive attention mechanisms.

Table 4.7: Advantages and disadvantages of transformer-based models in MTLF.

Model Type

Strengths

Weaknesses

Sparse Transformer

for long lookback

Efficient inference; suitable

May lose information with 
aggressive sparsity settings.

LDTformer

sequences; robust accuracy.

Integrates time and

frequency attention; best-

in-class forecasting

accuracy.

Increased complexity; higher 
training overhead.

4.4.  Hybrid models

Hybrid  modelling  approaches  have  gained  prominence  in  the  field  of  MTLF, 
especially when dealing with complex time series such as monthly electricity demand. 
These models integrate statistical, signal decomposition, and deep learning techniques 
to enhance forecasting accuracy and model robustness. In this section, recent advances 
in  hybrid  models  are  grouped  according  to their  primary  algorithmic  foundation—
ranging 
to  Transformer-based 
architectures and signal decomposition frameworks.

learning  combinations

from  statistical–deep

---

<!-- PAGE 75 -->

| Medium-term load forecasting

65

4.4.1.  Statistical–deep learning hybrids

Combining classical statistical techniques with deep learning offers the advantage of 
modelling  both  linear  and  nonlinear  patterns.  Dudek  et  al.  [53]  proposed  a  hybrid 
architecture, as it is shown in Figure 4.3, that integrates Exponential Smoothing (ETS) 
with  a  Residual  Dilated  LSTM  network.  In  their  approach,  ETS  captures  trend  and 
seasonal  patterns,  while  the  LSTM  models  the  residual  nonlinear  fluctuations.  This 
two-stage  setup  was  tested  on  monthly  electricity  demand  data  from  35  European 
countries. The hybrid model achieved a MAPE reduction of up to 25% compared to 
standalone  ETS  and  LSTM  baselines,  making  it  a  strong  candidate  for  MTLF 
applications, particularly where trend and seasonal variation dominate the signal.

Figure 4.3: Block diagram of the ETS+RD-LSTM forecasting system [53].

Similarly,  González  Grandón  et  al.  [54]  developed  a  hybrid  model  that  integrates 
ARIMA  for  modelling  long-term  linear  trends  and  an  LSTM  network  for  capturing 
nonlinear  variations.  Their  approach  was  evaluated  on  calendar-  and  temperature-
driven electricity load data. The hybrid ARIMA-LSTM model achieved lower RMSE 
and MAPE values than both standalone LSTM and ARIMA models, with a reported

---

<!-- PAGE 76 -->

66

| Medium-term load forecasting

MAPE of 2.48% and RMSE of 18.3 MW. This confirms the synergy between linear and 
nonlinear modelling in improving forecasting precision at monthly horizons.

4.4.2.  Transformer-based hybrids

Transformer-based architectures have revolutionized sequence modelling due to their 
capacity to model long-range dependencies. Building on this foundation, Wang et al. 
[55]  proposed  a  Hybrid  Autoformer  Framework  (HAFF)  specifically  for  electricity 
demand  forecasting  that  is  illustrated  in  Figure  4.4.  Their  model  introduces  a 
preprocessing pipeline using MLR with 10 variables and Bootstrap sampling, followed 
by an enhanced Autoformer with improved auto-correlation mechanisms. Evaluated 
on datasets from Taixing, China, and New South Wales, Australia, the HAFF model 
achieved a MAPE of 1.63% and RMSE of 47.28 MW in Taixing, and 2.43% and 239.96 
MW,  respectively,  in  New  South  Wales.  These  results  outperformed  standard 
Transformer variants like Reformer and Informer, especially when data were limited 
or seasonal fluctuations were prominent.

Figure 4.4: The whole structure of HAFF [55].

Expanding  on  Transformer  designs,  Antonesi  et  al.  [56]  introduced  a  hybrid  model 
that integrates Transformers with Liquid Neural Networks (LNNs), CNN encoders, 
and adaptive positional encodings. Their model was evaluated across various building 
types—including  households  and  commercial  facilities—using  daily  and  monthly 
energy consumption data. The model demonstrated a SMAPE improvement ranging 
from 1.5% to 50% over basic Transformer, LSTM, and ANN models. With R² scores 
exceeding  0.92  in  most  cases,  and  a  training  time  reduction  of  8%  over  the  base 
Transformer,  the  proposed  model  balances  accuracy  with  computational  efficiency, 
making it a compelling hybrid solution for monthly MTLF scenarios.

4.4.3.  CNN–LSTM hybrids

CNN–LSTM architectures are widely used for their ability to simultaneously extract 
spatial features and model temporal dependencies. Yıldız Doğan et al. [57] introduced 
a  CNN-LSTM  hybrid  model  aimed  at  estimating  electricity  demand  for  sustainable 
cities. Using hourly electricity consumption and meteorological data collected over a 
five-year  period  from  a  city  in  Türkiye,  the  model  was  evaluated  on  its  ability  to

---

<!-- PAGE 77 -->

| Medium-term load forecasting

67

forecast  medium-term  electricity  demand.  The  CNN  component  extracts  high-level 
temporal  patterns,  while  the  LSTM  captures  sequential  dependencies.  The  hybrid 
model  achieved  a  MAPE  of  2.9%,  RMSE  of  1.36,  and  an  R²  value  of  0.86—
outperforming  the  standalone  LSTM  model  (R²  =  0.81),  thereby  demonstrating  its 
superiority in learning complex temporal trends over medium horizons.

Zhang  et  al.  [58]  introduced  an  innovative  multi-task  hybrid  model,  MTMV-CNN-
LSTM,  which  combines  Convolutional  Neural  Networks  and  Long  Short-Term 
Memory networks within a multi-task learning framework to forecast both short- and 
medium-term  electricity  loads.  The  model  addresses  the  issue  of  redundant  or 
mismatched feature intervals—such as weather data at daily intervals versus power 
load  at  15-minute  intervals—by  structuring  the  learning  tasks  hierarchically.  The 
auxiliary task handles slower-varying features (e.g., weather, calendar effects), while 
the main task predicts detailed load profiles. For medium-term forecasting, defined in 
their study as a 3-month horizon, the MTMV-CNN-LSTM achieved superior results: it 
outperformed  six  baseline  models  including  Prophet,  CatBoost,  GRU,  LSTM,  GAN, 
and even a standard CNN-LSTM. Specifically, it recorded an RMSE of 0.053, MAE of 
0.044, and MSE of 0.003, with an R² of 0.640. This architecture demonstrates excellent 
robustness, maintaining accuracy under input perturbations such as added Gaussian 
and uniform noise, with R² values consistently above 0.8 even under noisy conditions. 
Its ability to generalize across multiple horizons and handle complex feature structures 
makes it a strong candidate for monthly MTLF applications.

4.4.4.  Signal decomposition-based hybrids

Signal decomposition methods such as Empirical Mode Decomposition (EMD) and its 
ensemble  variants  offer  powerful  tools  for  handling  non-stationary  and  multi-scale 
time series. Lei Wang et al. [59] proposed a hybrid model based on Figure 4.5—EEMD-
SE-PSO-SVR—that  leverages  ensemble  empirical  mode  decomposition  (EEMD)  to 
break down the demand signal, uses sample entropy (SE) to filter noise, and applies 
SVR with parameters optimized via Particle Swarm Optimization (PSO). Applied to 
monthly  electricity  demand  in  China,  this  hybrid  method  outperformed  traditional 
SVR and statistical models, reducing the MAPE by 54.49%. The authors highlighted 
the model’s ability to manage data irregularities and nonlinear dependencies, which 
are common in medium-term forecasting tasks.

In another decomposition-based hybrid, Huang et al. [60] introduced an EMD-LSTM-
Markov  model  for  predicting  building  cooling  loads.  The  architecture  first 
decomposes the load signal using EMD, applies LSTM to model temporal sequences, 
and  finally  incorporates  a  Markov  chain  to  adjust  state  transitions  based  on  prior 
probabilities.  Although  designed  for  cooling  loads,  the  model  achieved  a  MAPE  of 
0.84%  and  RMSE  of  4.53  in  monthly-scale  prediction  tasks,  demonstrating  its 
adaptability to broader MTLF applications.

---

<!-- PAGE 78 -->

68

| Medium-term load forecasting

Figure 4.5: The architecture of the proposed hybrid model by Lei Wang et al [59].

4.4.5.  Neural Prophet–LSTM hybrids

Shohan et al. [61] developed a novel architecture by combining a LSTM model with 
Neural  Prophet  (NP),  a  model  built  upon  Facebook  Prophet  but  enhanced  with 
autoregressive  and  seasonality  handling  features.  As  Figure  4.6  illustrates,  outputs 
from  LSTM  and  NP  are  combined  via  an  ANN,  resulting  in  a  hybrid  architecture 
tailored to different forecasting horizons. Evaluated on ERCOT and NREL datasets for 
both  short-  and  medium-term  forecasting,  the  model  achieved  lower  MAPE  values 
across  all  benchmarks,  with  monthly  MAPE  dropping  to  1.79%  and  RMSE  falling

---

<!-- PAGE 79 -->

| Medium-term load forecasting

69

below 2.3 MW. The integration of NP offers increased interpretability, while the LSTM 
preserves sequential learning, striking a strong balance between accuracy and model 
explainability.

Figure 4.6: Block diagram of proposed hybrid model by Shohan et al [61].

These  diverse  hybrid  approaches  underscore  the  increasing  sophistication  and 
customization  of  MTLF  models  in  addressing  nonlinearity,  seasonality,  and  data 
scarcity.  A  comparative  summary  of  these  models,  highlighting  their  strengths  and 
limitations, is provided in Table 4.8.

Table 4.8: Benefits and weakness of hybrid models in MTLF.

authors

Benefits

Weakness

Dudek et al.

[53]

González

Grandón et

al. [54]

Wang et al.

[55]

Handles trend/seasonal + 
residuals; accurate for monthly 
scales

Requires tuning of two separate 
model stages

Combines statistical structure 
with temporal learning

Sensitive to ARIMA lag 
parameters

Outperforms base Transformers; 
robust to seasonal and sparse 
data

Complex multi-stage 
preprocessing

---

<!-- PAGE 80 -->

70

| Medium-term load forecasting

Antonesi et

al. [58]

Yıldız

Doğan et al.

[57]

Zhang et al.

[58]

High accuracy and 
generalization; efficient for 
monthly predictions

Captures both local and 
temporal patterns; strong 
generalization

Architecturally complex; 
training stability needs care

May overlook external variables 
like price or policy

Excellent on 3-month prediction; 
multi-task learning improves 
generality

Slightly lower R² than simpler 
CNN-LSTM baseline

Lei Wang et

al. [59]

Strong for non-stationary data; 
robust error reduction

Computationally intensive due 
to decomposition and tuning

Huang et al.

[60]

Captures states and transitions; 
stable and accurate

Markov component can be lag-
sensitive

Shohan et

al. [61]

High accuracy and 
interpretability; robust across 
multiple horizons

Integration of NP lacks 
theoretical transparency

4.5.  Summary

Chapter 4 provided an in-depth review of methodologies used for medium-term load 
forecasting,  which  targets  horizons  ranging  from  one  week  to  one  month.  This 
forecasting  range  plays  a  critical  role  in  strategic  energy  planning,  maintenance 
scheduling,  and  tariff  design.  The  chapter  explored  four  major  categories  of  MTLF 
techniques:  statistical  models,  machine 
learning 
architectures, and hybrid frameworks.

learning  approaches,  deep

Statistical  models  such  as  Linear  Regression,  Quantile  Regression,  ARIMA,  and 
SARIMA offer simplicity and interpretability, performing well under stable seasonal 
conditions.  However,  their  capacity  to  manage  nonlinear  patterns  and  evolving 
consumption  behaviors  is  limited.  Enhancements  like  Fourier-ARIMA  and  kernel 
density methods improve adaptability but increase model complexity.

ML  methods—especially  tree-based  models  like  Random  Forests,  XGBoost,  and 
LightGBM—demonstrated  strong  performance  in  handling  nonlinearities,  temporal 
patterns, and external features such as weather and economic variables. k-NN offered 
simplicity  and  interpretability  but  faced  challenges  with  high-dimensional  or  noisy 
datasets.  ANN  models  provided  higher  accuracy  by  capturing  intricate  nonlinear 
patterns but required substantial data and careful tuning.

Deep  learning  models,  particularly  LSTM  networks,  proved  effective  in  modeling 
long-term temporal dependencies and nonlinear load behaviors, though they demand

---

<!-- PAGE 81 -->

| Medium-term load forecasting

71

high computational resources and large datasets. Transformer-based models emerged 
as  a  promising  alternative,  offering 
improved  scalability,  parallelism,  and 
robustness—especially in complex and data-scarce scenarios. Advanced variants like 
LDTformer demonstrated state-of-the-art forecasting accuracy for monthly horizons.

Hybrid  models  integrated  the  strengths  of  multiple  approaches  to  overcome 
individual  limitations.  Combinations  such  as  ETS+LSTM,  ARIMA+LSTM,  CNN-
LSTM,  and  Transformer-based  hybrids  showed  superior  accuracy,  robustness,  and 
generalizability. Signal decomposition and optimization techniques (e.g., EEMD, PSO, 
NSGA-II) further enhanced model performance, especially  under data irregularities 
and seasonal fluctuations.

In conclusion, the chapter underscores that while traditional models retain value in 
stable  environments,  ML,  deep  learning,  and  hybrid  methods  are  increasingly 
essential for accurate and resilient MTLF. Their adaptability to evolving consumption 
patterns and integration with external variables make them indispensable for modern 
energy systems.

---

<!-- PAGE 82 -->

72

| Long-term load forecasting

5  Long-term load forecasting

LTLF  involves  predicting  electricity  demand  over  extended  horizons,  typically 
ranging from one year to several decades. These forecasts play a crucial role in strategic 
planning  for  power  system  infrastructure,  investment  decisions,  energy  policy 
development,  and  integration  of  renewable  energy  sources.  Unlike  short-term  or 
medium-term forecasting, which focuses on operational or tactical grid management, 
LTLF  emphasizes  the  structural  evolution  of  demand  influenced  by  socioeconomic 
growth, technological shifts, climate policy, and demographic trends.

Accurate  long-term  forecasts  enable  utility  companies,  transmission  operators,  and 
governmental  bodies  to  ensure  sufficient  capacity,  optimize  capital  allocation,  and 
evaluate the long-term viability of energy projects. However, LTLF presents several 
challenges  due  to  high  uncertainty,  evolving  consumption  patterns,  and  limited 
availability of high-resolution long-term data. As a result, LTLF models often rely on 
macroeconomic indicators, population growth projections, urban development plans, 
and technological adoption rates.

Among various modeling approaches, regression-based techniques have remained a 
cornerstone of LTLF due to their interpretability, ease of implementation, and ability 
to incorporate trend and calendar effects. The following sections explore key studies 
that apply regression models to long-term electricity demand forecasting, highlighting 
their methodologies, performance, and practical implications.

5.1.  Statistical methods

Statistical methods form the foundational basis of long-term load forecasting due to 
their  simplicity,  transparency,  and  capacity  to  model  historical  trends  and  seasonal 
patterns.  These  approaches  typically  establish  relationships  between  electricity 
consumption  and  external  influencing  factors  such  as  population,  GDP,  industrial 
output, or calendar variables.

For  LTLF,  commonly  used  statistical  techniques  include  multiple  linear  regression, 
logistic  regression,  and  time  series  decomposition.  Multiple  linear  regression  is 
effective in capturing linear trends based on socio-economic indicators and calendar 
effects, while logistic regression is particularly suited for modeling saturated growth 
in  electricity  demand  —  a  typical  pattern  in  mature  economies  or  fully  electrified

---

<!-- PAGE 83 -->

| Long-term load forecasting

73

regions.  These  models  offer  interpretability  and  are  valuable  for  scenario-based 
planning and policy simulation.

Despite  their  strengths,  statistical  methods  may  struggle  to  capture  nonlinearities, 
structural breaks, and evolving behavioral patterns over extended horizons. Therefore, 
they  are  often  used  in  combination  with  clustering  or  scenario  analysis  to  enhance 
robustness in long-term forecasts.

5.1.1.  Regression-based models

Regression-based  approaches  have  long  served  as  the  backbone  of  long-term  load 
forecasting  due  to  their  simplicity,  interpretability,  and  effectiveness  in  modeling 
relationships between electricity demand and socioeconomic variables. These models 
typically  assume  that  electricity  consumption  can  be  expressed  as  a  function  of 
independent  variables  such  as  population  growth,  gross  domestic  product  (GDP), 
industrial  activity,  and  calendar-related  factors.  For  long-term  forecasting  horizons, 
regression models are especially valuable in scenario planning, allowing utilities and 
policymakers to assess how structural and demographic trends will influence future 
electricity needs.

One representative study employing regression methods for long-term forecasting is 
by Nano et al. [19], who proposed a MLR model enhanced with calendar effects. The 
model integrates variables such as day type (weekday, weekend, holiday), seasonal 
indicators, and long-term temporal trends to forecast electricity demand at a yearly 
scale.  The  framework  is  designed  for  practical  utility  applications  and  captures 
recurring consumption patterns over multiple years. Although specific error metrics 
such as MAPE were not detailed, the study reported strong alignment with historical 
trends,  indicating  good  reliability  in  forecasting  seasonal  variations.  However,  the 
model’s  reliance  on  linear  assumptions  limits  its  flexibility  in  modeling  nonlinear 
growth, particularly in systems approaching demand saturation.

tailored

long-term

framework

In  a  more  complex  formulation,  Royal  et  al.  [43]  developed  a  regression-based 
statistical 
forecasting.  Their 
for  district-level 
methodology  combines  linear  regression  with  aggregated  seasonal  profiles  and 
incorporates  localized  planning  data,  such  as  infrastructure  developments  and 
population  projections.  The  model  was  applied  over  a  multi-year  horizon  and 
achieved  a  MAPE  below  7%,  showcasing  its  robustness  for  practical  long-term 
planning.  Compared  to  advanced  machine  learning  models,  this  framework  offers 
improved  transparency  and  explainability—important  qualities  for  long-term 
strategic decisions—though it may not be as responsive to abrupt structural changes 
or nonstationary patterns.

A more recent contribution by Feng et al. [62] addresses the limitations of linearity in 
traditional  regression  by  introducing  an  improved  logistic  regression  model  for 
saturated  load  forecasting.  Their  approach  models  electricity  demand  using  an  S-

---

<!-- PAGE 84 -->

74

| Long-term load forecasting

shaped  logistic  curve,  which  is  particularly  well-suited  for  markets  approaching 
maturity  where  demand  growth  slows  and  eventually  plateaus.  To  enhance 
performance, the study also integrates affinity propagation clustering to group similar 
load  profiles,  improving  both  prediction  accuracy  and  segmentation.  The  model 
demonstrated  superior  accuracy  in  predicting  long-term  saturation  levels  and 
outperformed  conventional  linear  regression  methods,  with  reported  MAPE  values 
below 5% in year-ahead forecasts. This approach provides a more realistic depiction 
of long-term load dynamics in stable or mature energy systems.

Together,  these  studies  demonstrate  the  diverse  ways  regression  models  can  be 
adapted  for  long-term  load  forecasting—from  capturing  linear  trends  and  calendar 
effects  to  modeling  saturation  behaviors  in  maturing  markets.  While  regression 
models  are  valued  for  their  transparency  and  ease  of  implementation,  they  may 
require  hybridization  or  advanced  calibration  techniques  to  manage  complex 
nonlinearities and emerging consumption behaviors over long planning horizons.

As summarized in Table 5.1, different regression techniques offer specific advantages 
and limitations when applied to LTLF, depending on the structural characteristics of 
the electricity system and the forecasting context.

Table 5.1: Advantages and disadvantages of regression -based models in LTLF.

Model Type

Strengths

Weaknesses

Multiple Linear

Regression

Linear Regression

(District-level)

Improved Logistic

Regression

Simple, interpretable;

effective for trend and

calendar modeling

Robust in localized long-

term trends; useful for

scenario analysis

Captures demand

saturation; better long-term

curve fitting

Cannot capture nonlinear or 
saturation behavior

Less flexible under abrupt 
structural changes

Requires saturation context; 
more complex to calibrate

5.1.2.  ARIMA and SARIMA

Time  series  models  such  as  ARIMA  and  its  seasonal  extension  SARIMA  have 
remained foundational tools in load forecasting due to their ability to model temporal 
dependencies,  long-term  trends,  and  seasonal  fluctuations.  In  the  context  of  LTLF, 
these models are particularly useful for systems with stable consumption patterns and 
clear  seasonality.  Their  mathematical  transparency  and  relatively 
low  data 
requirements make them attractive for policy-oriented planning and strategic demand 
estimation.

---

<!-- PAGE 85 -->

| Long-term load forecasting

75

Kumar  et  al.  [63]  explored  the  use  of  ARIMA,  ARMA,  and  SARIMA  models  for 
forecasting long-term load profiles in smart-metered distribution systems. The study 
focused  on  capturing  consumption  behavior  in  the  presence  of  granular  data  made 
available by smart metering infrastructure. Their findings underscored that SARIMA, 
in particular, was able to effectively capture periodic consumption patterns and long-
term shifts in usage. While the authors did not provide specific numerical values for 
forecast errors, they emphasized that SARIMA outperformed ARIMA and ARMA in 
scenarios  where  seasonal  variability  was  pronounced.  The  study  highlighted  those 
statistical models, when adequately parameterized and applied to high-quality smart 
meter data, could provide reliable forecasts for annual load planning.

A more detailed comparative study by Dubey et al. [64] examined the performance of 
SARIMA against a deep learning model, LSTM, for time series forecasting of energy 
consumption. The authors applied both models to daily energy usage data enriched 
with  weather-related  features  such  as  temperature,  humidity,  and wind  speed.  The 
SARIMA model successfully captured the seasonal dynamics in the data and produced 
stable forecasts over extended horizons. However, it lagged behind LSTM in terms of 
predictive accuracy. The study reported that SARIMA  yielded a MAE  compared to 
LSTM, indicating that while SARIMA is well-suited for seasonally-driven systems, its 
linear structure may be less effective in modeling nonlinearities present in evolving 
energy  consumption  patterns.  Nonetheless,  SARIMA  was  preferred  for 
its 
interpretability and resilience against overfitting, which are critical in long-term utility 
forecasting where transparency and reproducibility are prioritized.

Both  studies  suggest  that  ARIMA-based  models  remain  viable  and  useful  in  LTLF, 
particularly when forecasting is conducted in mature systems with historical stability 
and  when  explainability  is  a  necessary  criterion.  However,  their  effectiveness  may 
diminish  in  contexts  characterized  by  abrupt  structural  changes,  such  as  the 
integration  of  electric  vehicles,  distributed  energy  resources,  or  dynamic  tariff 
structures. In such cases, hybrid or data-driven models may offer improved accuracy. 
Nonetheless, the ability of SARIMA to  manage seasonality and ARIMA’s simplicity 
continue to make them valuable tools in the long-term forecasting toolkit.

As summarized in Table 5.2, ARIMA and SARIMA methods offer distinct advantages 
in long-term forecasting scenarios, particularly in relation to transparency, seasonality 
handling,  and  data  efficiency.  However,  their  performance  can  be  constrained  by 
linearity assumptions and the inability to adapt to sudden behavioral shifts in energy 
usage.

---

<!-- PAGE 86 -->

76

| Long-term load forecasting

Table 5.2: Advantages and disadvantages of ARIMA and SARIMA methods in LTLF.

Model Type

Strengths

Weaknesses

ARIMA

SARIMA

Simple, interpretable, low

data requirement

Captures seasonality well;

robust for stable time series

Poor seasonality handling; 
struggles with nonlinear 
patterns 
Less accurate than deep 
learning models; rigid under 
system change

5.2.  Machine learning methods

ML methods have emerged as powerful alternatives to traditional statistical models 
for LTLF, especially in contexts where electricity consumption is influenced by a large 
number of interdependent and nonlinear factors. Unlike classical approaches that rely 
on explicit assumptions about data distribution or trend linearity, ML models learn 
patterns directly from historical data, enabling them to adapt to complex relationships 
between  electricity  demand  and  a  wide  range  of  exogenous  variables,  including 
weather, socio-economic indicators, urbanization trends, and behavioral shifts.

In the context of LTLF, ML models such as decision trees, support vector machines, k-
nearest  neighbors,  and  ensemble  techniques  like  Random  Forests  and  Gradient 
Boosting  have  shown  increasing  relevance.  These  models  can  accommodate  high-
dimensional datasets and are often more flexible than linear models when forecasting 
long-term consumption influenced by evolving market structures and energy usage 
patterns.  Their  ability  to  generalize  from  past  trends  and  adjust  to  non-stationary 
environments makes them particularly useful in modern energy systems characterized 
by decentralization, demand-side variability, and renewable integration.

However,  the  effectiveness  of  ML  methods  in  LTLF  depends  significantly  on  the 
quality and volume of data, careful feature selection, and model interpretability. While 
some methods offer high accuracy, they may lack transparency, posing challenges in 
regulatory or policy-driven planning where explainability is essential.

Let  me  know  which  subsections  you  would  like  to  explore  next—e.g.,  tree-based 
models, support vector regression, k-NN, or others.

5.2.1.  SVR

SVR has emerged as a powerful technique for long-term load forecasting due  to its 
ability  to  manage  nonlinear  relationships  and  limited  datasets  while  maintaining 
robustness against overfitting. SVR models are particularly effective in capturing the 
complex dependencies that characterize annual electricity demand patterns.

Wang et al. [65] proposed an annual load forecasting model based on SVR optimized 
using a Differential Evolution (DE) algorithm. The study focused specifically on one-

---

<!-- PAGE 87 -->

| Long-term load forecasting

77

year-ahead  electricity  demand  forecasts.  The  SVR  model,  when  tuned  using  DE, 
demonstrated  enhanced  predictive  performance  compared  to  traditional  regression 
methods. For instance, the optimized SVR model achieved lower MAPE compared to 
both  the  standard  SVR  and  linear  regression  benchmarks.  This  result  confirms  that 
fine-tuning the hyperparameters of SVR can significantly improve its applicability to 
annual load forecasting, where prediction horizons are extended and data variability 
increases.

Hu  [66]  conducted  a  comparative  study  evaluating  SVR,  neural  networks,  and 
Exponentially  Weighted  Moving  Average  (EWMA)  models  for  long-term  load 
forecasting in the context of air conditioning systems in large buildings. Although the 
study included other techniques, SVR was examined as a stand-alone model. Results 
showed that SVR offered competitive accuracy in predicting long-term cooling loads, 
particularly when nonlinearities and seasonal fluctuations were present. However, it 
slightly  underperformed  compared  to  neural  networks  in  capturing  rapid  load 
transitions, especially in extreme temperature conditions. The SVR model, while stable 
and interpretable, produced higher RMSE values than the neural network model in 
high variability periods, indicating a limitation in dynamic adaptability.

Kazemzadeh et al. [67] presented a hybrid forecasting model that integrates SVR with 
ARIMA  and  ANN,  using  PSO  for  parameter  tuning.  Although  the  study's  primary 
focus was on a hybrid approach, it also evaluated SVR independently as a baseline. 
For long-term forecasting of yearly peak load and energy demand in Iran’s National 
Electric  Energy  System,  the  SVR  model  alone  produced  respectable  forecasting 
accuracy, but it was outperformed by the hybrid model in terms of both MAPE and 
RMSE. Specifically, SVR’s standalone MAPE was in the range of 5.3% to 6.7%, while 
the  hybrid  model  reduced  this  to  below  4.5%.  This  finding  underscores  that  SVR 
performs  reasonably  well  on  its  own  for  long-term  horizons  but  can  benefit 
substantially when integrated into ensemble frameworks that address its limitations 
in temporal modelling.

In  conclusion,  SVR  provides  a  solid  foundation  for  long-term  forecasting  and  is 
especially  effective  when  carefully  tuned  or  used  as  a  component  within  hybrid 
systems.  While  its  performance  may  trail  slightly  behind  deep  learning  models  or 
hybrid systems in some scenarios, SVR's interpretability and generalization capacity 
make it a valuable tool for annual load prediction in both residential and commercial 
domains. These findings are summarized in  Table 5.3, comparing the strengths and 
limitations of SVR-based approaches across different applications in LTLF.

---

<!-- PAGE 88 -->

78

| Long-term load forecasting

Table 5.3: Advantages and disadvantages of SVR method in LTLF.

Model Type

Strengths

Weaknesses

SVR

Effectively models

nonlinear relationships in

yearly energy demand and

building load profiles;

performance can be

significantly improved

using optimization

techniques like Differential

Evolution; adaptable across

various sectors.

Performance highly depends 
on hyperparameter tuning; 
standalone SVR may yield 
lower accuracy compared to 
neural networks or hybrid 
models, especially in 
capturing peak loads.

5.2.2.  Tree-based models

Tree-based  models—including  Decision  Trees  (DTs),  Random  Forests  (RF),  and 
Gradient  Boosting Machines  (GBMs)—have  gained  significant  traction  in  long-term 
load forecasting (LTLF) due to their ability to model complex nonlinear interactions 
without  assuming  a  specific  data  distribution.  These  models  are  especially  useful 
when  forecasting  yearly  or  multi-month  electricity  demand,  where  features  such  as 
seasonality, economic indicators, and demographic patterns interact in complex ways.

Dinmohammadi  et  al.  [44]  conducted  a  detailed  evaluation  of  ensemble  tree-based 
models  for  long-term  residential  electricity  consumption  forecasting.  Their  study 
compared  Random  Forests  and  Gradient  Boosting  algorithms  in  predicting  energy 
usage  across  different  housing  profiles  and  geographic  regions  over  an  annual 
horizon.  The  results  demonstrated  that  Gradient  Boosting  achieved  slightly  better 
accuracy (MAPE ≈ 5.8%) compared to Random Forests (MAPE ≈ 6.2%), although both 
significantly  outperformed  traditional  regression  models.  The  authors  highlighted 
that  Random  Forests  provided  more  stable  results  across  varying  input  conditions, 
while  Gradient  Boosting  offered  higher  precision  when  hyperparameters  were 
carefully  tuned.  Additionally,  the  ensemble  models  showed  resilience  to  noise  and 
missing values, which are common in real-world LTLF datasets.

Sangrody  et  al.  [68]  explored  multiple  machine  learning  methods  for  long-term 
electricity demand forecasting in the U.S., including decision tree-based algorithms. 
Although  their  main  focus  was  a  comparative  framework  across  several  learning 
models,  they  confirmed  the  relevance  of  tree-based  models  for  capturing  nonlinear 
trends  in  multi-year  forecasts.  In  particular,  decision  tree  models  were  useful  for 
feature  importance  analysis  and  detecting  seasonal  or  structural  patterns  in 
consumption  behavior.  The  authors  noted  that  while  tree-based  models  were 
generally  outperformed  by  deep  learning  techniques  in  accuracy,  they  remained

---

<!-- PAGE 89 -->

| Long-term load forecasting

79

attractive for their  interpretability and lower computational cost—especially in grid 
planning and regulatory applications.

Together, these studies affirm the practical strengths of tree-based models for LTLF: 
ensemble trees like Random Forests and Gradient Boosting achieve a strong balance 
between accuracy  and generalizability, while individual trees serve as interpretable 
tools for exploring underlying data structures. Despite being slightly less accurate than 
some  deep  learning  models,  their  transparency  and  robustness  make  them 
indispensable 
forecasting  contexts,  particularly  where  model 
long-term 
explainability and stakeholder trust are priorities.

in

As summarized in Table 5.4, the main strength of tree-based models lies in their ability 
to adapt to nonlinear patterns in high-dimensional data with limited preprocessing. 
However, their performance varies depending on the algorithm: standalone trees are 
interpretable  but  less  accurate,  while  ensemble  methods  improve  forecasting 
performance but require more resources and careful tuning.

Table 5.4: Advantages and disadvantages of tree-based models in LTLF.

Model Type

Strengths

Weaknesses

Decision Trees

computation; useful for

Easy to interpret; low

policy contexts.

Stable across datasets;

Random Forest

handles missing data and

noise well.

Lower accuracy for long 
horizons; sensitive to data 
noise.

Less interpretable; require 
larger data volumes, more 
memory and training time.

Gradient Boosting

High accuracy; good with

complex nonlinear trends.

Sensitive to hyperparameters 
tuning; slower to train

5.2.3.  ANN

ANNs have been widely adopted in load forecasting tasks due to their ability to model 
complex,  nonlinear  relationships  between  historical  consumption  and  external 
influencing  factors.  In  LTLF,  where  the  prediction  horizon  spans  several  months  to 
years, ANNs are particularly valuable because they can learn from high-dimensional 
input  spaces  and  accommodate  a  variety  of  exogenous  variables  such  as  economic 
indicators, demographic trends, and weather patterns.

Sangrody  et  al.  [68]  applied  machine  learning  approaches—including  ANNs—for 
long-term  electricity  demand  forecasting  in  their  2018  study.  They  designed  their 
model  using  historical  demand  data  and  various  macroeconomic 
inputs, 
demonstrating  that  ANN  models  were  capable  of  capturing  evolving  patterns  in 
electricity  consumption  with  higher  flexibility  than  conventional  linear  models. 
Although  exact  numerical  error  values  were not  provided,  the  authors  emphasized 
that ANNs outperformed baseline models in tracking long-term trends and seasonal

---

<!-- PAGE 90 -->

80

| Long-term load forecasting

variations in electricity usage. The flexibility of ANN models was particularly useful 
in handling fluctuations caused by population growth and policy changes.

Similarly,  Ozdemir  [69]  conducted  a  comprehensive  evaluation  of  several  artificial 
intelligence  and  machine  learning  methods—including  ANNs—for  predicting 
Turkey's  annual  electricity  consumption  up  to  2030.  The  study  considered  input 
features such as GDP, population, and international trade indicators. Among all tested 
models,  four  were  shortlisted  based  on  forecasting  accuracy:  Stepwise  Linear 
Regression  (SLR),  GA,  Gaussian  Process  Regression  (GPR),  and  Neural  Networks. 
Although  SLR  had  the  lowest  MAPE  of  2.36%,  the  neural  network  model  also 
exhibited  competitive  performance  and  was  retained  for  final  scenario-based 
projections.  The  use  of  NN  proved  effective  in  modeling  the  nonlinear  and 
multidimensional characteristics of energy demand data over extended horizons. The 
study  also  highlighted  the  strength  of  NN  in  integrating  multiple  socio-economic 
variables, making it well-suited for national-level energy planning.

Together,  these  studies  underscore  the  relevance  of  ANNs  for  LTLF  applications. 
While ANNs require careful configuration of architecture and training parameters to 
avoid  overfitting,  they  remain  one  of  the  most  robust  tools  for  capturing  hidden 
patterns and interactions in long-term consumption data.  Table  5.5 summarizes the 
key  strengths  and  limitations  of  ANN  models  for  LTLF  based  on  the  reviewed 
literature.

Table 5.5: Advantages and disadvantages of ANN model in LTLF.

Model Type

Strengths

Weaknesses

Captures nonlinear and

complex patterns over

long-term horizons;

handles multivariate and

ANN

socioeconomic inputs

effectively; adaptable to

changes in consumption

behavior and economic

factors.

Sensitive to parameter tuning; 
prone to overfitting with small 
datasets; requires high 
computational resources and 
data preprocessing.

5.3.  Deep learning

Deep learning models have emerged as powerful tools in LTLF due to their ability to 
model  highly  nonlinear  relationships,  extract  complex  features,  and  learn  from 
sequential  patterns  in  large-scale  energy  datasets.  These  models  outperform  many 
traditional statistical and machine learning techniques when sufficient historical and 
contextual data are available, particularly over extended forecast horizons.

---

<!-- PAGE 91 -->

| Long-term load forecasting

81

In the context of LTLF, where electricity demand must be projected months or years 
ahead,  deep  learning  architectures  are  valued  for  their  scalability  and  capacity  to 
handle multivariate inputs without extensive feature engineering. However, they also 
come with limitations such as high computational requirements, sensitivity to training 
data quality, and limited interpretability.

5.3.1.  Multilayer perceptron

MLP  neural  networks  have  demonstrated  significant  potential  in  long-term  load 
forecasting  due  to  their  capacity  to  model  complex,  nonlinear  relationships  across 
multi-year  datasets.  These  networks  are  especially  effective  when  historical 
consumption data is influenced by multiple interdependent variables such as seasonal 
trends, economic growth, or policy changes.

Faraji et al. [70] introduced a long-term forecasting approach for annual load growth 
in microgrids using an MLP model. The research focused on the optimal planning of 
a  grid-connected  microgrid  in  Tehran,  employing  HOMER  software  for  simulating 
different load growth scenarios. Their method used historical annual load data to train 
the MLP, capturing nonlinear growth patterns over multiple years. While the paper 
primarily  emphasizes  the  impact  of  accurate  load  growth  prediction  on  system 
planning  rather  than  detailed  error  metrics,  it  highlights  how  the  use  of  MLP 
forecasting leads to more reliable optimization results when compared with traditional 
linear forecasting models.

Complementing this, Kim et al. [71] proposed a hybrid long-term forecasting model 
that is shown in Figure 5.1 and combines MLP with statistical techniques to overcome 
the  average  convergence  limitations  seen  in  standalone  machine  learning  methods. 
Their model was trained and validated using massive-scale real-world data from over 
10,000 distribution lines provided by Korea Electric Power Corporation (KEPCO). The 
hybrid approach yielded an average accuracy  of 89.56% based on Normalized Root 
Mean  Squared  Error  (NRMSE),  outperforming  models  based  purely  on  statistical 
regression or MLP alone. Notably, their study validates the hybrid model for practical 
deployment  in  national-scale  distribution  network  planning,  underscoring  its 
robustness for multi-year forecasting applications.

Together,  these  studies  illustrate  the  strengths  of  MLP-based  models  in  capturing 
complex nonlinear demand trends across extended time horizons. While MLP alone 
proves useful in improving the precision of load growth estimations, its combination 
with  statistical  approaches  offers  improved  stability  and  generalization,  especially 
when applied to large-scale datasets.

---

<!-- PAGE 92 -->

82

| Long-term load forecasting

Figure 5.1: Feedforward procedure of neural network for MLP by Kim et al. [71].

As summarized in Table 5.6, MLP models provide a flexible and powerful approach 
to LTLF, with their benefits and weaknesses largely determined by dataset size, model 
tuning, and whether hybridization is used.

Table 5.6: Advantages and disadvantages of MLP model in LTLF.

Model Type

Strengths

Weaknesses

Model nonlinear

relationships; suitable for

annual load growth; high

accuracy when hybridized;

effective in real-world

deployment.

Standalone MLP may suffer 
from convergence issues; 
performance sensitive to 
architecture and training data 
quality.

MLP

5.3.2.  LSTM

LSTM networks are a class of RNNs widely used for sequential data modelling due to 
their  ability  to  capture  long-term  dependencies  through  gated  mechanisms.  While 
traditional  LSTM  models  have  shown  promising  results  in  many  time  series 
applications,  their  direct  application  to  LTLF  has  faced  limitations,  especially  in 
capturing extended temporal patterns and handling data scarcity.

To  address  these  challenges,  recent  studies  have  introduced  enhanced  LSTM 
architectures or combined LSTM with complementary techniques.

Dai et al. [72] introduced a novel model illustrated in Figure 5.2 and called Segmented 
Self-Attention  LSTM  (SALSTM),  which  integrates  segmented  iteration  and  intra-
segment self-attention mechanisms into the LSTM framework. This architecture was 
specifically developed to tackle the issue of performance degradation in long-sequence 
forecasting.  In  traditional  LSTM,  as  the  prediction  length  increases—such  as 
forecasting 96-time steps ahead—the model's ability to retain meaningful information 
diminishes significantly. The SALSTM model mitigates this by reducing the recursive

---

<!-- PAGE 93 -->

| Long-term load forecasting

83

steps  needed  and  embedding  self-attention  within  segments  to  better  capture  long-
distance  dependencies.  Experimental  evaluations  on  benchmark  datasets 
demonstrated that SALSTM consistently outperforms both standard LSTM and state-
of-the-art  Transformer-based  models  in  long-term  forecasting  tasks.  This  reinforces 
the notion that LSTM-based methods, when properly adapted, remain competitive in 
LTLF contexts.

Figure 5.2: The self-attention model and its computational process by Dai et al. [72].

On  the  other  hand,  Go  et  al.  [73]  tackled  a  different  aspect  of  LSTM  limitations  in 
LTLF—data  availability.  Their  proposed  approach  addresses  the  difficulty  of 
forecasting  in  the  context  of  insufficient  long-term  historical  data,  particularly  for 
growing  sectors  such  as  electric  vehicles  and  evolving  economies.  The  researchers 
developed a hybrid model that combines decomposition-linear methods, exponential 
smoothing,  and  LSTM.  Initially,  this  model  generates  synthetic  future  inputs  by 
capturing  trends  and  seasonality  from  available  historical  data  using  statistical 
decomposition and smoothing. These synthetic sequences are then used as inputs for 
the  LSTM  model.  When  applied  to  long-term  demand  forecasting,  including  the 
creation  of  reserve  demand  curves  for  future  power  system  planning,  the  model 
demonstrated  strong  reliability  and  practical  utility.  This  method  is  especially 
beneficial when forecasting in data-scarce environments while still utilizing LSTM's 
pattern recognition capabilities.

Together,  these  studies  illustrate  the  versatility  of  LSTM-based  methods  when 
augmented  with  attention  mechanisms  [72]  or  hybridized  with  classical  forecasting

---

<!-- PAGE 94 -->

84

| Long-term load forecasting

techniques  [73].  Such  enhancements  enable  LSTM  to  maintain  forecasting  accuracy 
and reliability even in the face of long prediction horizons and limited data.

Table  5.7  summarizes  the  key  strengths  and  limitations  of  these  LSTM-based 
approaches in the context of long-term load forecasting.

Table 5.7: Advantages and disadvantages of LSTM model in LTLF.

Model Type

Strengths

Weaknesses

LSTM

Captures long-term

dependencies; flexible

architecture adaptable to

enhancements (e.g., self-

attention, hybrid input

generation); performs well

in long-term forecasting

when extended; robust in

handling nonlinear

temporal patterns.

Captures long-term 
dependencies; flexible 
architecture adaptable to 
enhancements (e.g., self-
attention, hybrid input 
generation); performs well in 
long-term forecasting when 
extended; robust in handling 
nonlinear temporal patterns.

5.3.3.  Transformer-based models

Transformer-based  models  have  emerged  as  a  powerful  alternative  to  traditional 
sequence  forecasting  architectures  due  to  their  ability  to  model  long-range 
dependencies  using  self-attention  mechanisms.  However,  in  the  context  of  LTLF, 
standard  Transformers  often  encounter  challenges  such  as  high  computational 
complexity,  limited  interpretability,  and  insufficient  accuracy  when  applied  over 
extended  time  horizons.  Recent  advancements  have  introduced  improved  variants 
that  address  these  shortcomings  by  modifying  attention  mechanisms,  integrating 
hybrid architectures, or enhancing temporal granularity.

the

improve

Tan et al.  [74] proposed Cakformer, a Transformer variant specifically  designed for 
long-term  heat  load  forecasting.  To  overcome  the  limitations  of  conventional  self-
attention,  Cakformer  introduces  a  convolutional  autocorrelation  mechanism  that 
simultaneously  captures  local  features  and  global  time  dependencies.  Furthermore, 
the model replaces the traditional MLP with a Kolmogorov–Arnold Network (KAN) 
to 
interactions.  A 
learning  of  nonlinear,  high-dimensional 
Synchrosqueezed Wavelet Transform (SWT) is also employed to reduce noise in the 
input data. Experimental validation across multiple prediction horizons—96, 192, 336, 
and  720  steps—demonstrated  Cakformer’s  superiority  over  seven  state-of-the-art 
models, including Autoformer and Transformer. At 720-step forecasting, for instance, 
Cakformer  reduced  MAE  by  9.6%  and  root  mean  squared  error  (RMSE)  by  8.3% 
compared to Autoformer, indicating its robustness in both accuracy and generalization 
across datasets.

---

<!-- PAGE 95 -->

| Long-term load forecasting

85

Yang et al. [75] developed the Multi-Granularity Autoformer (MG-Autoformer) which 
is shown in Figure 5.3 to address both deterministic and probabilistic aspects of long-
term  power  load  forecasting.  The  model  introduces  a  Multi-Granularity  Auto-
Correlation Attention Mechanism (MG-ACAM) to effectively model both fine-grained 
short-term  fluctuations  and  coarse  long-term  trends.  To  manage  computational 
overhead, a shared query–key (Q–K) mechanism is implemented, and a quantile loss 
function  is  used  to  enable  probabilistic  forecasting  with  uncertainty  quantification. 
Evaluation on four diverse benchmark datasets—Portugal, USA, Australia, and ISO 
New England—revealed that MG-Autoformer consistently outperformed Autoformer 
and Transformer in both point and probabilistic forecasting. It achieved up to 11.2% 
lower  MAE  and  9.4%  lower  RMSE  in  deterministic  tasks,  and  a  13.5%  reduction  in 
normalized pinball loss (NPL) in probabilistic settings, confirming its applicability in 
real-world planning scenarios where confidence intervals are vital.

Figure 5.3: The multi-granularity Autoformer by Yang et al. [75].

Together, these studies demonstrate that Transformer-based models—when equipped 
with  tailored  attention  mechanisms  and  multiscale  forecasting  strategies—can 
significantly  improve  the  performance  of  LTLF  models.  Table  5.8  summarizes  the 
enhancements, predictive gains, and limitations of these Transformer variants.

Table 5.8: Advantages and Disadvantages of Transformer-based models in LTLF.

Model Type

Strengths

Weaknesses

High interpretability; best

Cakformer

multi-horizon accuracy;

MG-Autoformer

robust to noise.

Captures trends at multiple

scales; supports

probabilistic forecasting;

efficient attention design.

High architectural complexity; 
focused on heat load datasets.

Design sensitive to granularity 
setup; training time remains 
high.

---

<!-- PAGE 96 -->

86

| Long-term load forecasting

5.4.  Hybrid models

Hybrid models have gained increasing attention in long-term load forecasting (LTLF) 
due  to  their  ability  to  combine  the  strengths  of  multiple  methodologies  while 
compensating for individual weaknesses. These models often blend machine learning, 
fuzzy logic, neural networks, optimization algorithms, or time-series frameworks to 
address  the  challenges  of  nonlinearity,  uncertainty,  and  temporal  dependence.  This 
section  categorizes  hybrid  models  into  five  main  groups  based  on  their  core 
methodological structures.

5.4.1.  Fuzzy-Neural Network-Based Hybrid Models

Fuzzy-neural  models  combine  the  uncertainty-handling  strength  of  fuzzy  systems 
with the learning capabilities of ANNs. Toly Chen [76] proposed a collaborative fuzzy-
neural approach where multiple experts construct fuzzy backpropagation networks 
(FBPNs)  to  generate  fuzzy  forecasts,  which  are  then  aggregated  using  fuzzy 
intersection and defuzzified via a radial basis function (RBF) network. This framework 
enables simultaneous prediction of average and peak loads, improving precision by 
40%  and  accuracy  by  99%  over  single  models.  In  Figure  5.4  the  procedure  of  this 
proposed model is shown.

Figure 5.4: The procedure of the proposed methodology by Toly Chen [76].

---

<!-- PAGE 97 -->

| Long-term load forecasting

87

Similarly,  Danladi  et  al.  [77]  applied  a  fuzzy  logic  system  enhanced  with  ANN 
structures  to  model  long-term  electricity  demand.  Their  approach  incorporates 
fuzzified input variables and a rule-based decision-making system that mimics human 
reasoning for load behavior, making it suitable for complex environments with vague 
and  uncertain  data.  These  models  offer  transparency  in  reasoning  and  high 
adaptability  to  varying  load  patterns  but  may  suffer  from  increased  computational 
complexity due to fuzzification and defuzzification stages.

5.4.2.  Fuzzy-RNN-based models

Wen et al. [78] introduced a hybrid model called the TS-type recurrent fuzzy neural 
network  (TS-RFNN),  which  integrates  fuzzy  inference  mechanisms  with  recurrent 
neural  networks.  This  model  is  particularly  suited  for  long-term  forecasting  as  it 
manages  time-dependence  through  feedback  connections  and  linguistic  uncertainty 
via Takagi-Sugeno (TS) fuzzy rules. As Figure 5.5 illustrates, the architecture consists 
of  five  layers,  including  fuzzification,  rule  evaluation,  normalization,  consequent 
generation, and defuzzification. Experimental results demonstrate that the TS-RFNN 
effectively captures the temporal and uncertain characteristics of load data, achieving 
higher accuracy than standard RNNs or fuzzy systems alone.

Figure 5.5: Schematic structure of ISO-TS-RBF-RFNN model by Wen et al. [78].

---

<!-- PAGE 98 -->

88

| Long-term load forecasting

5.4.3.  Fuzzy-SVM and grey system hybrid models

Chen et al. [79] proposed a hybrid model that combines fuzzy support vector machines 
(FSVM) with a grey forecasting mechanism that flowchart of the method is shown in 
Figure 5.6. The grey system model captures the overall trend in sparse and incomplete 
data, while the FSVM provides fine-grained learning of nonlinear patterns. This hybrid 
is particularly robust in uncertain or data-deficient environments. By optimizing the 
kernel parameters of the SVM under a fuzzy rule base and integrating trend correction 
from the grey model, the method improves prediction stability and generalization. It 
outperforms  single  SVM  and  grey  models  in  terms  of  MAPE  and  RMSE, 
demonstrating its effectiveness in complex LTLF scenarios.

Figure 5.6: Flow chart of long-term power load grey combination forecast by Chen et 
al. [79].

---

<!-- PAGE 99 -->

| Long-term load forecasting

89

5.4.4.  LSTM-based hybrid deep learning models

Ma et al.  [80] developed a deep hybrid architecture that combines PSO, LSTM, and 
XGBoost to enhance long-term renewable energy forecasting. As Figure 5.7 illustrates, 
in this model, PSO optimizes LSTM’s hyperparameters to avoid manual tuning, while 
XGBoost fine-tunes the final predictions by correcting residual errors. The integration 
of these methods allows for robust learning from nonlinear and seasonally fluctuating 
datasets.  Comparative  evaluations  show  that  the  hybrid  outperforms  standalone 
LSTM and statistical methods in both accuracy and generalization. However, due to 
its multi-stage nature, the model requires greater computational resources and more 
complex integration steps.

Figure 5.7: Framework for the RES design optimization by Ma et al. [80].

5.4.5.  Transformer-based hybrid deep learning models

Tian  et  al.  [81]  introduced  LDformer,  a  transformer-based  parallel  deep  neural 
network  tailored  for  long-term  power  forecasting.  LDformer  fuses  Informer  (a 
lightweight transformer variant), LSTM (for long-range dependencies), convolutional 
layers  (for  local  feature  extraction),  and  UniDrop-based  attention  regularization.  Its 
architecture  enables  simultaneous  processing  of  long  sequences  with  reduced 
redundancy  and  computational  cost.  LDformer  excels  in  robustness  and  scalability

---

<!-- PAGE 100 -->

90

| Long-term load forecasting

across  multiple  benchmark  datasets,  consistently  outperforming  classical  RNNs, 
LSTMs, and baseline Informer models in terms of RMSE. The key advantage lies in its 
ability to retain deep temporal features while mitigating attention overload through 
ProbSparse attention mechanisms.

To  provide  a  concise  overview  of  the  comparative  strengths  and  limitations  of  the 
reviewed hybrid approaches, Table 5.9 summarizes the key benefits and weaknesses 
associated  with  each  model  type.  This  synthesis  highlights  how  different 
combinations—ranging  from  metaheuristic–neural  hybrids  to  transformer-based 
architectures—offer  distinct  advantages  in  handling  long-term  load  forecasting 
challenges such as nonlinearity, uncertainty, and sequence length. The table serves as 
a  reference  point  for  evaluating  trade-offs  between  accuracy,  interpretability, 
computational  efficiency,  and  practical  applicability  in  real-world  forecasting 
scenarios.

Table 5.9: Advantages and disadvantages of hybrid models in LTLF.

Authers

Strengths

Weaknesses

Robust to sparse data,

Chen et al.[79]

handles uncertainty and

Complex parameter tuning

trend components

High accuracy, residual

Ma et al. [80]

correction, optimized

structure

Collaborative expert

Multi-stage model increases 
computation and integration 
complexity

Chen, Toly [76]

modelling, handles peak

and average forecasts

Requires defuzzification and 
multiple iterations

together

Captures temporal

Wen et al. [78]

uncertainty, rule-based

learning

Fast training, strong long-

Tian et al. [81]

range learning, reduced

Danladi et al. [77]

attention redundancy

Transparent rule-base,

effective with vague data

Difficult to scale to high-
dimensional inputs

High model complexity and 
memory usage

Limited adaptation if rule 
base is not comprehensive

---

<!-- PAGE 101 -->

| Long-term load forecasting

91

5.5.  Summary

Chapter  5  provided  a  detailed  review  of  state-of-the-art  methods  used  in  LTLF, 
highlighting  their  theoretical  foundations,  practical  applications,  and  relative 
strengths  and  weaknesses.  Beginning  with  statistical  approaches  such  as  multiple 
logistic  regression,  ARIMA,  and  SARIMA,  the  discussion 
linear  regression, 
emphasized their transparency, interpretability, and suitability for stable consumption 
environments, while also acknowledging their limitations in modelling nonlinear or 
rapidly evolving demand patterns. The chapter then explored the increasing adoption 
of  machine  learning  models—including  SVR,  decision  trees,  random  forests,  and 
gradient  boosting—which  offer  improved  flexibility  and  accuracy  but  may  lack 
explainability. Deep learning methods, such as ANN, MLP, and LSTMs, were shown 
to effectively capture complex temporal and nonlinear relationships, especially when 
supported by large, high-quality datasets or enhanced through hybridization. Finally, 
the  chapter  examined  a  diverse  array  of  hybrid  models  that  integrate  fuzzy  logic, 
optimization algorithms, deep learning, and Transformer-based architectures. These 
hybrids  demonstrate  substantial  gains  in  accuracy,  adaptability,  and  robustness—
particularly  in  scenarios  involving  long  sequences,  uncertainty,  or  sparse  data. 
However, they also introduce challenges related to model complexity, computational 
requirements, and integration costs. The comparative synthesis in tables throughout 
this chapter—including Table 5.9 for hybrid models—offers a practical reference for 
selecting  appropriate  forecasting  techniques  based  on  system  characteristics,  data 
availability,  and  planning  objectives.  Together,  these  insights  provide  a  strong 
foundation for understanding and improving LTLF in evolving power systems.

---

<!-- PAGE 102 -->

92

| Conclusion and future research 
directions

6  Conclusion and future research

directions

This  thesis  has  undertaken  a  comprehensive  investigation  into  electricity  load 
forecasting,  focusing  particularly  on  methods  suited  for  LTLF  but  contextualized 
within  the  broader  landscape  that  includes  STLF  and  MTLF.  By  systematically 
reviewing statistical, machine learning, deep learning, and hybrid methods, the thesis 
provides an organized framework to understand when and how each method should 
be  applied,  considering  both  forecasting  horizon  and  data  availability—two  of  the 
most critical dimensions in predictive modelling for power systems.

6.1.  Recapitulation 
contributions

of

research

objectives

and

forecasting

The research was driven by the increasing demand for accurate and scalable electricity 
load 
tools  amid  evolving  energy  consumption  behaviors,  grid 
decarbonization, and renewable energy integration. The review began by identifying 
the  practical  challenges  utilities  and  planners  face  in  making  decisions  under 
conditions of long-term uncertainty and growing data diversity. Through a layered 
analysis of forecasting methods, this thesis contributes:

A classification of methods by time horizon, detailing their strengths and limitations 
across short-, medium-, and long-term applications.

A mapping of forecasting techniques to data availability levels, from single households 
to national-scale energy systems.

A  comparative  review  of  hybrid  approaches,  which  integrate  models  to  balance 
accuracy, interpretability, and computational cost.

Visual  tools  (Figure  6.1  and  Figure  6.2)  to  guide  practitioners  in  selecting  suitable 
methods based on forecast duration and data granularity.

---

<!-- PAGE 103 -->

| Conclusion and future research 
directions

93

Figure 6.1: Forecasting horizon classification of different methods.

Figure 6.2: Scalability of forecasting methods based on spatial data availability.

---

<!-- PAGE 104 -->

94

| Conclusion and future research 
directions

6.2.  Strategic  alignment  between  forecasting  horizons

and methods

A  core  finding  of  this  work  is  that  forecasting  accuracy  and  reliability  are  heavily 
dependent on temporal context:

STLF, defined as forecasting within a few minutes to 1 week, is best addressed using 
statistical  models  such  as  Multiple  Linear  Regression  (MLR),  ARIMA/SARIMA,  or 
simple machine learning techniques like SVR. These methods are interpretable, fast, 
and data-efficient—ideal for operational decision-making.

MTLF, spanning 1 week to 1 month, benefits from tree-based models (e.g., Random 
Forests, Gradient Boosting Machines) and basic ANNs. These methods offer improved 
capacity to capture nonlinearities and complex interactions, useful  for demand-side 
planning, tariff design, or load shifting strategies.

LTLF, beyond 1 month and up to several decades, requires models capable of handling 
system  evolution,  structural  change,  and  socio-economic  influences.  Here,  deep 
learning  models  such  as  LSTM  and  Transformer-based  architectures,  along  with 
hybrid models integrating fuzzy logic, metaheuristics, and ensemble learning, show 
the  best  performance.  These  models  can  model  intricate  temporal  dynamics  and 
uncertainties but require large datasets and computational resources.

As shown in Figure 6.1, forecasting methods follow a progression from interpretable 
and lightweight models for short durations to more complex and data-hungry models 
as the prediction horizon increases.

6.3.  Method suitability based on data scale

Another major dimension in model selection is data scale, as detailed in Figure 6.2:

For household-level and building-level applications—such as smart home control or 
energy  efficiency  management—lightweight  methods  (SVR,  decision  trees,  simple 
ANN) are more suitable due to their ability to perform under data-scarce conditions.

District  and  city-level  forecasting,  which  often  includes  substation,  microgrid,  or 
municipal planning data, benefits from ML models such as ensemble trees and MLPs 
that balance model complexity with interpretability.

For regional and national-level load forecasting—relevant to grid investment, policy 
simulation, and energy market design—deep learning and hybrid models are ideal, as 
they  can  process  multivariate,  longitudinal,  and  often  noisy  datasets  with  greater 
fidelity.

---

<!-- PAGE 105 -->

| Conclusion and future research 
directions

95

This  scale-sensitive  approach  helps  align  model  complexity  with  data  richness, 
enhancing both efficiency and performance.

6.4.  Implications for practice and policy

The findings of this thesis offer several implications:

Model  choice  must  be  context  aware.  No  single  technique  is  optimal  across  all 
conditions. Planners and operators should match forecasting models to their intended 
use  case—be  it  short-term  operations,  medium-term  tariff  planning,  or  long-term 
infrastructure investment.

Explainability  vs.  accuracy  is  a  trade-off.  Statistical  models  provide  clarity  and 
confidence  for  policymakers  but  may  lack  precision.  Conversely,  DL  and  hybrid 
models offer state-of-the-art accuracy but require interpretability enhancements (e.g., 
attention mechanisms, post hoc analysis) for use in regulatory environments.

Data strategy is foundational. Models are only as good as the data they are built upon. 
Investment  in  smart  meter  infrastructure,  high-resolution  weather  data,  and  socio-
economic forecasting tools is essential  for unleashing  the full potential of advanced 
forecasting models.

6.5.  Limitations and future research directions

While  comprehensive,  this  review  is  subject  to  a  few  limitations:  it  is  based  on 
published  literature  and  benchmark  datasets  and  as  a  consequence  real-world 
constraints such as missing data, organizational capacity, and stakeholder preferences 
were not modelled explicitly. Hybrid models are still evolving, and their performance 
may  vary  significantly  across  datasets  and  implementations,  while  probabilistic 
forecasting  methods—which  incorporate  uncertainty  in  output—were  only  lightly 
discussed and could form a valuable extension of this work.

Future  research  should  focus  on,  for  instance,  (i)  interpretable  hybrid  models  that 
combine the accuracy of deep learning with the explainability of statistical approaches, 
(ii) transfer learning and meta-learning to reduce the training data burden in regions 
or sectors with limited historical data, and (iii) probabilistic and scenario-based LTLF, 
which better reflect real-world uncertainty and can support resilient decision-making.

It is worthwhile discussing briefly also Spiking Neural Networks (SNNs), which more 
closely  mimic  the  temporal  and  event-driven  processing  of  biological  neurons, 
represent  a  promising  frontier  for  electricity  load  forecasting.  The  robustness  of 
surrogate gradient learning algorithms enables effective training of SNNs despite the 
nondifferentiable nature of spike events, as demonstrated by Zenke and Vogels [82]. 
This makes SNNs well-suited for capturing complex temporal dynamics with sparse

---

<!-- PAGE 106 -->

96

| Conclusion and future research 
directions

and energy-efficient computations. Although SNNs have been explored for short-term 
load forecasting  [83], their  application to medium- and long-term  horizons remains 
underdeveloped.  Given  the  growing  interest  in  low-power,  real-time,  and  edge-
deployable AI models in smart grid contexts, future research should investigate SNN 
architectures  with  surrogate  gradient  training  for  medium-  and  long-term  load 
forecasting  tasks.  This  includes  developing  benchmark  datasets,  refining  hybrid 
models  that  integrate  SNNs  with  classical  deep  learning  techniques  and  exploring 
hardware implementations to leverage neuromorphic computing advantages.

Such directions could yield forecasting models that balance accuracy, efficiency, and 
interpretability,  addressing  challenges  posed  by  increasing  data  volume,  temporal 
complexity, and the need for sustainable computation in evolving power systems.

6.6.  Final remarks

In an era where  electricity systems are becoming more complex,  decentralized, and 
data-driven,  accurate  and  adaptive  load  forecasting  is  no  longer  a  luxury  but  a 
necessity. This thesis provides a structured lens to evaluate forecasting models, not as 
standalone tools but as components of a larger decision-making ecosystem—sensitive 
to time,  data, purpose, and context. As forecasting continues to evolve with AI, big 
data,  and  climate-aware  planning,  the  frameworks  and  insights  presented  here  can 
serve  as  a  foundation  for  both  academic  research  and  practical  implementation  in 
future-ready power systems.

---

<!-- PAGE 107 -->

| Bibliography

97

Bibliography

[1]

[2]

S. Amoako, F. K. Andoh, and E. E. Asmah, “Household structure and electricity 
consumption 
in  Ghana,”  Energy  Policy,  vol.  182,  Nov.  2023,  doi: 
10.1016/j.enpol.2023.113767.

“European Commission,” https://europa.eu/. Accessed: Mar. 18, 2025. [Online]. 
Available: 
https://ec.europa.eu/eurostat/statistics-
explained/index.php?title=Energy_consumption_in_households

[3]  H. Rafiq, P. Manandhar, E. Rodriguez-Ubinas, J. D. Barbosa, and O. A. Qureshi, 
“Analysis of residential electricity consumption patterns utilizing smart-meter 
data:  Dubai  as  a  case  study,”  Energy  Build,  vol.  291,  Jul.  2023,  doi: 
10.1016/j.enbuild.2023.113103.

[4]  C. Ragupathi, S. Dhanasekaran, N. Vijayalakshmi, and A. O. Salau, “Prediction 
of electricity consumption using an innovative deep energy predictor model for 
enhanced accuracy and efficiency,” Energy Reports, vol. 12, pp. 5320–5337, Dec. 
2024, doi: 10.1016/j.egyr.2024.11.018.

[5]  H. Luo, Y. Zhang, X. Gao, Z. Liu, X. Meng, and X. Yang, “Multi-scale electricity 
consumption  prediction  model  based  on  land  use  and  interpretable  machine 
learning: A case study of China,” Advances in Applied Energy, vol. 16, p. 100197, 
Dec. 2024, doi: 10.1016/j.adapen.2024.100197.

[6]  D.  Peteleaza  et  al.,  “Electricity  consumption  forecasting  for  sustainable  smart 
cities using machine learning methods,” Internet of Things (Netherlands), vol. 27, 
Oct. 2024, doi: 10.1016/j.iot.2024.101322.

[7]  Z.  Wang,  T.  Hong,  H.  Li,  and  M.  Ann  Piette,  “Predicting  city-scale  daily 
electricity consumption using data-driven models,” Advances in Applied Energy, 
vol. 2, May 2021, doi: 10.1016/j.adapen.2021.100025.

[8]

[9]

S. Palaniappan, S. Karuppannan, and D. Velusamy, “Categorization of Indian 
residential  consumers  electrical  energy  consumption  pattern  using  clustering 
and 
techniques,”  Energy,  vol.  289,  Feb.  2024,  doi: 
10.1016/j.energy.2023.129992.

classification

J. Adinkrah et al., “Artificial intelligence-based strategies for sustainable energy 
planning  and  electricity  demand  estimation:  A  systematic  review,”  Mar.  01, 
2025, Elsevier Ltd. doi: 10.1016/j.rser.2024.115161.

[10]  A. Najeeb, S. Sridharan, A. B. Rao, S. B. Agnihotri, and V. Mishra, “Determinants 
of  residential  electricity  consumption  in  South,  East  and  South  East  Asia:  A 
systematic review,” Jul. 01, 2024, Elsevier Ltd. doi: 10.1016/j.rser.2024.114400.

---

<!-- PAGE 108 -->

98

| Bibliography

[11]  C. T. Nguyen, H. Nguyen, and A. D. Sakti, “Seasonal characteristics of outdoor 
thermal comfort and residential electricity consumption: A Snapshot in Bangkok 
Jan.  2024,  doi: 
Metropolitan  Area,”  Remote  Sens  Appl,  vol.  33, 
10.1016/j.rsase.2023.101106.

[12]  Y. Li et al., “Efficient predictive control strategy for mitigating the overlap of EV 
charging demand and residential load based on distributed renewable energy,” 
Renew Energy, vol. 240, Feb. 2025, doi: 10.1016/j.renene.2024.122154.

[13]  F. Lazzari et al., “User behaviour models to forecast electricity consumption of 
residential customers based on smart metering data,” Energy Reports, vol. 8, pp. 
3680–3691, Nov. 2022, doi: 10.1016/j.egyr.2022.02.260.

[14]  Y. Huang, Z. Yao, and Q. Xu, “Classification model of electricity consumption 
behavior  based  on  sparse  denoising  autoencoder  feature  dimensionality 
reduction  and  spectral  clustering,”  International  Journal  of  Electrical  Power  and 
Energy Systems, vol. 158, Jul. 2024, doi: 10.1016/j.ijepes.2024.109960.

[15]  F.  Yu,  Q.  Yue,  A.  Yunianta,  and  H.  M.  A.  Aljahdali,  “A  novel  hybrid  deep 
correction  approach  for  electrical  load  demand  prediction,”  Sustain  Cities  Soc, 
vol. 74, Nov. 2021, doi: 10.1016/j.scs.2021.103161.

[16]  X.  Deng  et  al.,  “Bagging–XGBoost  algorithm  based  extreme  weather 
identification and short-term load forecasting model,” Energy Reports, vol. 8, pp. 
8661–8674, Nov. 2022, doi: 10.1016/j.egyr.2022.06.072.

[17]  M. Bilgili and E. Pinar, “Gross electricity consumption forecasting using LSTM 
and SARIMA approaches: A case study of Türkiye,” Energy, vol. 284, Dec. 2023, 
doi: 10.1016/j.energy.2023.128575.

[18]  D. Katić, H. Krstić, I. Ištoka Otković, and H. Begić Juričić, “Comparing multiple 
linear  regression  and  neural  network  models  for  predicting  heating  energy 
consumption in school buildings in the Federation of Bosnia and Herzegovina,” 
Journal of Building Engineering, vol. 97, Nov. 2024, doi: 10.1016/j.jobe.2024.110728.

[19]  H.  Nano,  S.  New,  A.  Cohen,  and  B.  Ramachandran,  “Chapter  16  -  Load 
forecasting  using  multiple  linear  regression  with  different  calendars,”  in 
Distributed Energy Resources in Microgrids, R. K. Chauhan and K. Chauhan, Eds., 
Academic  Press,  2019,  pp.  405–417.  doi:  https://doi.org/10.1016/B978-0-12-
817774-7.00016-8.

[20]  G.  Dudek,  “Pattern-based  local  linear  regression  models  for  short-term  load 
forecasting,” Electric Power Systems Research, vol. 130, pp. 139–147, Jan. 2016, doi: 
10.1016/j.epsr.2015.09.001.

[21]

J.  C.  Nsangou,  J.  Kenfack,  U.  Nzotcha,  P.  S.  Ngohe  Ekam,  J.  Voufo,  and  T.  T. 
Tamo,  “Explaining  household  electricity  consumption  using  quantile

---

<!-- PAGE 109 -->

| Bibliography

99

regression,  decision  tree  and  artificial  neural  network,”  Energy,  vol.  250,  Jul. 
2022, doi: 10.1016/j.energy.2022.123856.

[22]  A. Gellert, U. Fiore, A. Florea, R. Chis, and F. Palmieri, “Forecasting Electricity 
Consumption  and  Production  in  Smart  Homes  through  Statistical  Methods,” 
Sustain Cities Soc, vol. 76, Jan. 2022, doi: 10.1016/j.scs.2021.103426.

[23]  N.  M.  M.  Bendaoud,  N.  Farah,  and  S.  Ben  Ahmed,  “Applying  load  profiles 
propagation  to  machine  learning  based  electrical  energy  forecasting,”  Electric 
Power Systems Research, vol. 203, Feb. 2022, doi: 10.1016/j.epsr.2021.107635.

[24]  A.  Haque  and  S.  Rahman,  “Short-term  electrical  load  forecasting  through 
heuristic configuration of regularized deep neural network,” Appl Soft Comput, 
vol. 122, Jun. 2022, doi: 10.1016/j.asoc.2022.108877.

[25]  Y. Zhang, B. K. Teoh, M. Wu, J. Chen, and L. Zhang, “Data-driven estimation of 
building  energy  consumption  and  GHG  emissions  using  explainable  artificial 
intelligence,” Energy, vol. 262, Jan. 2023, doi: 10.1016/j.energy.2022.125468.

[26]  M.  S.  Hasan,  M.  Tarequzzaman,  M.  Moznuzzaman,  and  M.  A.  Ahad  Juel, 
“Prediction  of  energy  consumption  in  four  sectors  using  support  vector 
regression optimized with genetic algorithm,” Heliyon, vol. 11, no. 2, Jan. 2025, 
doi: 10.1016/j.heliyon.2025.e41765.

[27]  M. Zhou, J. Yu, F. Sun, and M. Wang, “Forecasting of short term electric power 
consumption for different types buildings using improved transfer learning: A 
case study of primary school in China,” Journal of Building Engineering, vol. 78, 
Nov. 2023, doi: 10.1016/j.jobe.2023.107618.

[28]  R. Pascanu, T. Mikolov, and Y. Bengio, “On the difficulty of training Recurrent 
Available:

[Online].

2012,

Nov.

Neural 
http://arxiv.org/abs/1211.5063

Networks,”

[29]  C. Wang, X. Li, Y. Shi, W. Jiang, Q. Song, and X. Li, “Load forecasting method 
based on CNN and extended LSTM,” Energy Reports, vol. 12, pp. 2452–2461, Dec. 
2024, doi: 10.1016/j.egyr.2024.07.030.

[30]  G. Memarzadeh and F. Keynia, “Short-term electricity load and price forecasting 
by a new optimal LSTM-NN based prediction algorithm,” Electric Power Systems 
Research, vol. 192, p. 106995, Mar. 2021, doi: 10.1016/j.epsr.2020.106995.

[31]  X. Guo, Q. Zhao, D. Zheng, Y. Ning, and Y. Gao, “A short-term load forecasting 
model of multi-scale CNN-LSTM hybrid neural network considering the real-
time  electricity  price,”  Energy  Reports,  vol.  6,  pp.  1046–1053,  2020,  doi: 
https://doi.org/10.1016/j.egyr.2020.11.078.

[32]  W. Guo, S. Liu, L. Weng, and X. Liang, “Power Grid Load Forecasting Using a 
CNN-LSTM Network Based on a Multi-Modal Attention Mechanism,” Applied 
Sciences (Switzerland), vol. 15, no. 5, Mar. 2025, doi: 10.3390/app15052435.

---

<!-- PAGE 110 -->

100

| Bibliography

[33]  C.  M.  Liapis,  A.  Karanikola,  and  S.  Kotsiantis,  “Energy  Load  Forecasting: 
Investigating  Mid-Term  Predictions  with  Ensemble  Learners,”  pp.  343–355, 
2022, doi: 10.1007/978-3-031-08333-4_28ï.

[34]  Z.  Tian,  W.  Liu,  W.  Jiang,  and  C.  Wu,  “CNNs-Transformer  based  day-ahead 
probabilistic  load  forecasting  for  weekends  with  limited  data  availability,” 
doi: 
p. 
Energy, 
https://doi.org/10.1016/j.energy.2024.130666.

130666,

2024,

293,

vol.

[35]

J. Wang, W. Huang, Y. Ding, Y. Dang, and L. Ye, “Forecasting the electric power 
load based on a novel prediction model coupled with accumulative time-delay 
effects and periodic fluctuation characteristics,” Energy, vol. 317, p. 134518, 2025, 
doi: https://doi.org/10.1016/j.energy.2025.134518.

[36]  A. Mathew, R. Chikte, S. K. Sadanandan, S. Abdelaziz, S. Ijaz, and T. Ghaoud, 
“Medium-term feeder load forecasting and boosting peak accuracy prediction 
using  the  PWP-XGBoost  model,”  Electric  Power  Systems  Research,  vol.  237,  p. 
111051, 2024, doi: https://doi.org/10.1016/j.epsr.2024.111051.

[37]  Z. Peng and X. Yang, “Short- and medium-term power load forecasting model 
based  on  a  hybrid  attention  mechanism  in  the  time  and  frequency  domains,” 
Expert 
doi: 
278, 
https://doi.org/10.1016/j.eswa.2025.127329.

127329,

2025,

Appl,

Syst

vol.

p.

[38]  Candidus. U. Eya, A. O. Salau, S. L. Braide, and O. D. Chigozirim, “Improved 
Medium Term Approach for Load Forecasting of Nigerian Electricity Network 
Using Artificial Neuro-Fuzzy Inference System: A Case Study of University of 
Nigeria,  Nsukka,”  Procedia  Comput  Sci,  vol.  218,  pp.  2585–2593,  2023,  doi: 
https://doi.org/10.1016/j.procs.2023.01.232.

[39]  S.  Karamolegkos  and  D.  E.  Koulouriotis,  “Advancing  short-term  load 
forecasting with decomposed Fourier ARIMA: A case study on the Greek energy 
market,” Energy, vol. 325, Jun. 2025, doi: 10.1016/j.energy.2025.135854.

[40]  S.  Wang,  S.  Wang,  and  D.  Wang,  “Combined  probability  density  model  for 
medium term load forecasting based on quantile regression and kernel density 
estimation,”  Energy  Procedia,  vol.  158,  pp.  6446–6451,  2019,  doi: 
https://doi.org/10.1016/j.egypro.2019.01.169.

[41]  C.  Xu,  Y.  Sun,  A.  Du,  and  D.  Gao,  “Quantile  regression  based  probabilistic 
forecasting of renewable energy generation and building electrical load: A state 
of the art review,”  Journal of Building Engineering, vol. 79, p. 107772, 2023, doi: 
https://doi.org/10.1016/j.jobe.2023.107772.

[42]  F.  Zhu  and  G.  Wu,  “Load  forecasting  of  the  power  system:  An  investigation 
based on the method of random forest regression,” Energy Engineering: Journal of 
the  Association  of  Energy  Engineering,  vol.  118,  no.  6,  pp.  1703–1712,  2021,  doi: 
10.32604/EE.2021.015602.

---

<!-- PAGE 111 -->

| Bibliography

101

[43]  E. Royal, S. Bandyopadhyay, A. Newman, Q. Huang, and P. C. Tabares-Velasco, 
“A statistical framework for district energy long-term electric load forecasting,” 
doi: 
Appl 
https://doi.org/10.1016/j.apenergy.2025.125445.

125445,

Energy,

2025,

384,

vol.

p.

[44]  F. Dinmohammadi, Y. Han, and M. Shafiee, “Predicting Energy Consumption in 
Residential Buildings Using Advanced Machine Learning Algorithms,” Energies 
(Basel), vol. 16, no. 9, May 2023, doi: 10.3390/en16093748.

[45]  Y. Dong, X. Ma, and T. Fu, “Electrical load forecasting: A deep learning approach 
based on K-nearest neighbors,” Appl Soft Comput, vol. 99, p. 106900, 2021, doi: 
https://doi.org/10.1016/j.asoc.2020.106900.

[46]  S. ur R. Khan et al., “Enhanced Machine-Learning Techniques for Medium-Term 
and Short-Term Electric-Load Forecasting in Smart Grids,” Energies (Basel), vol. 
16, no. 1, Jan. 2023, doi: 10.3390/en16010276.

[47]  G. Dudek and P.  Pełka, “Pattern Similarity-based Machine  Learning  Methods 
for  Mid-term  Load  Forecasting:  A  Comparative  Study,”  Mar.  2020,  [Online]. 
Available: http://arxiv.org/abs/2003.01475

[48]  R. Wazirali, E. Yaghoubi, M. S. S. Abujazar, R. Ahmad, and A. H. Vakili, “State-
of-the-art review on energy and load forecasting in microgrids using artificial 
neural  networks,  machine  learning,  and  deep  learning  techniques,”  Dec.  01, 
2023, Elsevier Ltd. doi: 10.1016/j.epsr.2023.109792.

[49]  M.  Ghiassi,  D.  K.  Zimbra,  and  H.  Saidane,  “Medium  term  system  load 
forecasting  with  a  dynamic  artificial  neural  network  model,”  Electric  Power 
doi: 
Systems  Research, 
https://doi.org/10.1016/j.epsr.2005.06.010.

302–316,

2006,

vol.

pp.

no.

76,

5,

[50]  T. Yalcinoz and U. Eminoglu, “Short term and medium term power distribution 
load forecasting by neural networks,” Energy Convers Manag, vol. 46, no. 9, pp. 
1393–1405, 2005, doi: https://doi.org/10.1016/j.enconman.2004.07.005.

[51]  S. Muzaffar and A. Afshari, “Short-term load forecasts using LSTM networks,” 
doi:

2922–2927.

Elsevier

Energy

2019,

Ltd,

pp.

in 
10.1016/j.egypro.2019.01.952.

Procedia,

[52]

J.  W.  Chan  and  C.  K. Yeo,  “A  Transformer based  approach  to  electricity  load 
forecasting,”  Electricity 
Journal,  vol.  37,  no.  2,  Mar.  2024,  doi: 
10.1016/j.tej.2024.107370.

[53]  G.  Dudek,  P.  Pełka,  and  S.  Smyl,  “A  Hybrid  Residual  Dilated  LSTM  end 
Exponential Smoothing Model for Mid-Term Electric Load Forecasting,” Mar. 
2020, [Online]. Available: http://arxiv.org/abs/2004.00508

[54]  T.  González  Grandón,  J.  Schwenzer,  T.  Steens,  and  J.  Breuing,  “Electricity 
demand  forecasting  with  hybrid  classical  statistical  and  machine  learning

---

<!-- PAGE 112 -->

102

| Bibliography

algorithms:  Case  study  of  Ukraine,”  Appl  Energy,  vol.  355,  Feb.  2024,  doi: 
10.1016/j.apenergy.2023.122249.

[55]  Z.  Wang,  Z.  Chen,  Y.  Yang,  C.  Liu,  X.  Li,  and  J.  Wu,  “A  hybrid  Autoformer 
framework for electricity demand forecasting,” Energy Reports, vol. 9, pp. 3800–
3812, Dec. 2023, doi: 10.1016/j.egyr.2023.02.083.

[56]  G. Antonesi, T. Cioara, I. Anghel, I. Papias, V. Michalakopoulos, and E. Sarmas, 
“Hybrid  transformer  model  with  liquid  neural  networks  and  learnable 
encodings for buildings’ energy forecasting,” Energy and AI, vol. 20, May 2025, 
doi: 10.1016/j.egyai.2025.100489.

[57]  G. Yıldız Doğan, A. Aksoy, and N. Öztürk, “A Hybrid Deep Learning Model to 
Estimate  the  Future  Electricity  Demand  of  Sustainable  Cities,”  Sustainability 
(Switzerland), vol. 16, no. 15, Aug. 2024, doi: 10.3390/su16156503.

[58]  S.  Zhang,  R.  Chen,  J.  Cao,  and  J.  Tan,  “A  CNN  and  LSTM-based  multi-task 
learning  architecture  for  short  and  medium-term  electricity  load  forecasting,” 
Electric  Power  Systems  Research,  vol.  222,  p.  109507,  2023,  doi: 
https://doi.org/10.1016/j.epsr.2023.109507.

[59]  L. Wang, X. Wang, and Z. Zhao, “Mid-term electricity demand forecasting using 
improved  multi-mode  reconstruction  and  particle  swarm-enhanced  support 
vector regression,” Energy, vol. 304, Sep. 2024, doi: 10.1016/j.energy.2024.132021.

[60]  X. Huang, Y. Han, J. Yan, and X. Zhou, “Hybrid forecasting model of building 
cooling load based on EMD-LSTM-Markov algorithm,” Energy Build, vol. 321, 
Oct. 2024, doi: 10.1016/j.enbuild.2024.114670.

[61]  M.  J.  A.  Shohan,  M.  O.  Faruque,  and  S.  Y.  Foo,  “Forecasting  of  Electric  Load 
Using  a  Hybrid  LSTM-Neural  Prophet Model,”  Energies  (Basel),  vol.  15,  no.  6, 
Mar. 2022, doi: 10.3390/en15062158.

[62]  R. Feng, J. Wang, W. Wu, S. Liu, A. Liu, and S. Xie, “Saturated load forecasting 
based on improved logistic regression and affinity propagation,” Electric Power 
doi: 
Systems 
https://doi.org/10.1016/j.epsr.2024.110953.

Research,

110953,

2024,

237,

vol.

p.

[63]  V. Kumar, R. K. Mandal, and S. Rai, “Smart metered distribution system load 
forecasting using statistical approaches,” in 2024 4th International Conference on 
Emerging Frontiers in Electrical and Electronic Technologies (ICEFEET), 2024, pp. 1–
4. doi: 10.1109/ICEFEET64463.2024.10866475.

[64]  A.  Kumar  Dubey,  A.  Kumar,  V.  García-Díaz,  A.  Kumar  Sharma,  and  K. 
Kanhaiya, “Study and analysis of SARIMA and LSTM in forecasting time series 
data,”  Sustainable Energy Technologies  and Assessments, vol. 47, p. 101474, 2021, 
doi: https://doi.org/10.1016/j.seta.2021.101474.

---

<!-- PAGE 113 -->

| Bibliography

103

[65]

J. Wang, L. Li, D. Niu, and Z. Tan, “An annual load forecasting model based on 
support vector regression with differential evolution algorithm,”  Appl Energy, 
vol. 94, pp. 65–70, 2012, doi: https://doi.org/10.1016/j.apenergy.2012.01.010.

[66]  T. Hu, “Comparison of long-term load forecasting methods for air conditioning 
system of a large building,” in 2021 China Automation Congress (CAC), 2021, pp. 
4491–4496. doi: 10.1109/CAC53003.2021.9728514.

[67]  M.-R. Kazemzadeh, A. Amjadian, and T. Amraee, “A hybrid data mining driven 
algorithm  for  long  term  electric  peak  load  and  energy  demand  forecasting,” 
doi: 
p. 
Energy, 
https://doi.org/10.1016/j.energy.2020.117948.

117948,

2020,

204,

vol.

[68]  H. Sangrody, N. Zhou, S. Tutun, B. Khorramdel, M. Motalleb, and M. Sarailoo, 
Long  Term  Forecasting  using  Machine  Learning  Methods.  2018.  doi: 
10.1109/PECI.2018.8334980.

[69]  G. Ozdemir, “Long-term electrical energy demand forecasting by using artificial 
intelligence/machine learning techniques,” Electrical Engineering, vol. 106, no. 4, 
pp. 5229–5251, 2024, doi: 10.1007/s00202-024-02364-1.

[70]

[71]

J.  Faraji,  H.  Hashemi-Dezaki,  and  A.  Ketabi,  “Multi-year  load  growth-based 
optimal  planning  of  grid-connected  microgrid  considering  long-term  load 
demand  forecasting:  A  case  study  of  Tehran,  Iran,”  Sustainable  Energy 
Technologies and Assessments, vol. 42, Dec. 2020, doi: 10.1016/j.seta.2020.100827.

J. H. Kim, B. S. Lee, and C. H. Kim, “A Study on the development of long-term 
hybrid  electrical  load  forecasting  model  based  on  MLP  and  statistics  using 
massive  actual  data  considering  field  applications,”  Electric  Power  Systems 
Research, vol. 221, Aug. 2023, doi: 10.1016/j.epsr.2023.109415.

[72]  Z. Q. Dai, J. Li, Y. J. Cao, and Y. X. Zhang, “SALSTM: segmented self-attention 
long short-term memory for long-term forecasting,” Journal of Supercomputing, 
vol. 81, no. 1, Jan. 2025, doi: 10.1007/s11227-024-06493-z.

[73]  T. U. Go, Y. J. Go, J. H. Im, and D. Lee, “Long-Term Demand Forecasting: Novel 
Decomposition-Linear  Exponential-Smoothing  Algorithm  with  Long  Short-
Term  Memory,”  Journal  of  Electrical  Engineering  and  Technology,  2025,  doi: 
10.1007/s42835-025-02226-1.

[74]  T. Quanwei, X. Guijun, and X. Wenju, “Cakformer: Transformer model for long-
term heat load forecasting based on Cauto-correlation and KAN,” Energy, vol. 
324, p. 135460, 2025, doi: https://doi.org/10.1016/j.energy.2025.135460.

[75]  Y. Yang, Y. Gao, H. Zhou, J. Wu, S. Gao, and Y.-G. Wang, “Multi-Granularity 
load 
2025,  doi:

long-term  deterministic  and  probabilistic  power

Autoformer  for 
forecasting,”  Neural  Networks,  vol. 
https://doi.org/10.1016/j.neunet.2025.107493.

188,  p.

107493,

---

<!-- PAGE 114 -->

104

| Bibliography

[76]  T. Chen, “A collaborative fuzzy-neural approach for long-term load forecasting 
in  Taiwan,”  Comput  Ind  Eng,  vol.  63,  no.  3,  pp.  663–670,  Nov.  2012,  doi: 
10.1016/j.cie.2011.06.003.

[77]  D. Ali, M. Yohanna, M. I. Puwu, and B. M. Garkida, “Long-term load forecast 
modelling using a fuzzy logic approach,” Pacific Science Review A: Natural Science 
2016,  doi: 
and  Engineering,  vol. 
10.1016/j.psra.2016.09.011.

18,  no.

123–127,

2,  pp.

Jul.

[78]  Z. Wen, L. Xie, Q. Fan, and H. Feng, “Long term electric load forecasting based 
on  TS-type  recurrent  fuzzy  neural  network  model,”  Electric  Power  Systems 
Research, vol. 179, Feb. 2020, doi: 10.1016/j.epsr.2019.106106.

[79]  Y. Chen, C. Xiao, S. Yang, Y. Yang, and W. Wang, “Research on long term power 
load  grey  combination  forecasting  based  on  fuzzy  support  vector  machine,” 
Computers 
2024,  doi: 
10.1016/j.compeleceng.2024.109205.

and  Electrical  Engineering,  vol.

116,  May

[80]  W.  Ma,  W.  Wu,  S.  F.  Ahmed,  and  G.  Liu,  “Techno-economic  feasibility  of 
utilizing  electrical  load  forecasting  in  microgrid  optimization  planning,” 
Sustainable  Energy  Technologies  and  Assessments,  vol.  73,  Jan.  2025,  doi: 
10.1016/j.seta.2024.104135.

[81]  R. Tian, X. Li, Z. Ma, Y. Liu, J. Wang, and C. Wang, “LDformer: a parallel neural 
network  model  for  long-term  power  forecasting,”  Frontiers  of  Information 
Technology and Electronic Engineering, vol. 24, no. 9, pp. 1287–1301, Sep. 2023, doi: 
10.1631/FITEE.2200540.

[82]  F. Zenke and T. P. Vogels, “The Remarkable Robustness of Surrogate Gradient 
Learning for Instilling Complex Function in Spiking Neural Networks,” Neural 
Comput, vol. 33, no. 4, pp. 899–925, Mar. 2021, doi: 10.1162/neco_a_01367.

[83]  S.  Kulkarni,  S.  P.  Simon,  and  K.  Sundareswaran,  “A  spiking  neural  network 
(SNN)  forecast  engine  for  short-term  electrical  load  forecasting,”  Appl  Soft 
doi: 
Comput, 
https://doi.org/10.1016/j.asoc.2013.04.007.

3628–3635,

2013,

vol.

pp.

no.

13,

8,

---

<!-- PAGE 115 -->

105

List of Figures

Figure 1.1: Electricity consumption by sectors (GWh) [1]. ................................................ 1

Figure 1.2: Benefits of electricity consumption prediction [4] .......................................... 2

Figure 2.1: Load forecasting time horizontal. ...................................................................... 4

Figure 2.2: Key factors affecting load forecasting. .............................................................. 5

Figure 3.1: SVR model. ......................................................................................................... 20

Figure 3.2: Tree-based model. .............................................................................................. 22

Figure 3.3: Feedforward and backpropagation architecture of ANN. .......................... 30

Figure 3.4: Schematic diagram of the LSTM [29]. ............................................................. 33

Figure 3.5: Proposed model of GA-optimized SVR [26]. ................................................. 36

Figure 3.6: Framework of extreme weather identification and STLF [16]. ................... 38

Figure  3.7:  A  schematic  diagram  of  a  CNN-LSTM  network  based on  a  multi-modal 
attention mechanism [32]. .................................................................................................... 39

Figure 3.8: Flow chart of the deep learning framework [34]. .......................................... 41

Figure 4.1: Architecture of XGBoost model [36]. .............................................................. 51

Figure 4.2: Framework of the proposed interval forecasting model and principles of 
NSGA-II, KNN, DBN and modified KDE [45]. ................................................................. 56

Figure 4.3: Block diagram of the ETS+RD-LSTM forecasting system [53]. ................... 65

Figure 4.4: The whole structure of HAFF [55]. .................................................................. 66

Figure 4.5: The architecture of the proposed hybrid model by Lei Wang et al [59]. ... 68

Figure 4.6: Block diagram of proposed hybrid model by Shohan et al [61]. ................ 69

Figure 5.1: Feedforward procedure of neural network for MLP by Kim et al. [71]. .... 82

Figure 5.2: The self-attention model and its computational process by Dai et al. [72].
 .................................................................................................................................................. 83

Figure 5.3: The multi-granularity Autoformer by Yang et al. [75]. ................................ 85

Figure 5.4: The procedure of the proposed methodology by Toly Chen [76]. ............. 86

Figure 5.5: Schematic structure of ISO-TS-RBF-RFNN model by Wen et al. [78]. ....... 87

---

<!-- PAGE 116 -->

106

| List of Figures

Figure 5.6: Flow chart of long-term power load grey combination forecast by Chen et 
al. [79]. ..................................................................................................................................... 88

Figure 5.7: Framework for the RES design optimization by Ma et al. [80]. .................. 89

Figure 6.1: Forecasting horizon classification of different methods. ............................. 93

Figure 6.2: Scalability of forecasting methods based on spatial data availability........ 93

---

<!-- PAGE 117 -->

107

List of Tables

Table 2.1: Common error metrics used in the load forecasting literature. .................... 12

Table 3.1: Strengths and limitations of regression methods in STLF. ............................ 17

Table 3.2: Strengths and limitations of ARIMA and SARIMA methods in STLF. ....... 19

Table 3.3: Strengths and limitations of SVR method in STLF. ........................................ 22

Table 3.4: Strengths and Limitations of Tree-Based Methods in STLF. ......................... 26

Table 3.5: Strengths and limitations of k-NN method in STLF. ..................................... 27

Table 3.6: Strengths and limitations of ANNs in STLF. ................................................... 31

Table 3.7: Strengths and limitations of RNNs and LSTMs in STLF. .............................. 34

Table 3.8: Strengths and Limitations of Transformer-Based Models in STLF. ............. 35

Table 3.9: Benefits of Hybrid models in STLF. .................................................................. 42

Table 4.1: Strengths and limitations of regression methods in MTLF. .......................... 47

Table 4.2: Strengths and limitations of ARIMA and SARIMA in MTLF. ...................... 49

Table 4.3: Advantages and disadvantages of Tree-based models in MTLF. ................ 54

Table 4.4: Advantages and disadvantages of K-NN in MTLF. ....................................... 57

Table 4.5: Advantages and disadvantages of ANN in MTLF. ........................................ 60

Table 4.6: Advantages and disadvantages of RNN and LSTM in MTLF. ..................... 62

Table 4.7: Advantages and disadvantages of transformer-based models in MTLF. ... 64

Table 4.8: Benefits and weakness of hybrid models in MTLF. ....................................... 69

Table 5.1: Advantages and disadvantages of regression -based models in LTLF. ...... 74

Table 5.2: Advantages and disadvantages of ARIMA and SARIMA methods in LTLF.
 .................................................................................................................................................. 76

Table 5.3: Advantages and disadvantages of SVR method in LTLF. ............................. 78

Table 5.4: Advantages and disadvantages of tree-based models in LTLF. ................... 79

Table 5.5: Advantages and disadvantages of ANN model in LTLF. ............................. 80

Table 5.6: Advantages and disadvantages of MLP model in LTLF. .............................. 82

Table 5.7: Advantages and disadvantages of LSTM model in LTLF. ............................ 84

---

<!-- PAGE 118 -->

108

| List of Tables

Table 5.8: Advantages and Disadvantages of Transformer-based models in LTLF. ... 85

Table 5.9: Advantages and disadvantages of hybrid models in LTLF. ......................... 90

---

<!-- PAGE 119 -->

109

Acknowledgments

I would like to express my deepest gratitude to my supervisors, Prof. Samuele Grillo, 
and Prof. Daniele Linaro and for their invaluable guidance, constructive feedback, and 
continuous  support  throughout  the  course  of  this  thesis.  Their  expertise  and 
encouragement have greatly shaped the quality and direction of my research.

I  also  extend  my  thanks  to  the  faculty  and  staff  of  the  Department  of  Electronics, 
Information and Bioengineering at Politecnico Di Milano for providing a stimulating 
academic environment and essential resources.

Finally,  I  am  deeply  grateful  to  my  family  and  friends  for  their  unwavering 
encouragement,  patience,  and  love,  which  sustained  me  throughout  this  academic 
journey.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| A  Comparative  |         | Review       | of  |
| --------------- | ------- | ------------ | --- |
| Electricity     | Load    | Forecasting  |     |
| Methods         | Across  | Temporal     |     |
Horizons
TESI DI LAUREA MAGISTRALE IN
ELECTRICAL ENGINEERING
INGEGNERIA ELETTRICA
Author: Zahra Saeedian

Student ID: 222206
Advisor: Samuele Grillo
Co-advisor: Daniele Linaro
Academic Year: 2024-25

i
Abstract
Accurate electricity load forecasting is a critical component of modern energy system
planning and operation, particularly in the context of growing electrification,
renewable energy integration, and demand-side flexibility. This thesis presents a
structured review of forecasting methods across three key time horizons: short-term
(up to 1 week), medium-term (1 week to 1 month), and long-term (beyond 1 month).
Each category is examined with respect to its methodological strengths, limitations,
and data requirements.
Statistical models such as multiple linear regression and SARIMA are found to be
effective for short-term forecasting due to their interpretability and low data demands.
Machine learning approaches—including support vector regression and tree-based
ensembles—offer improved flexibility for medium-term predictions. For long-term
forecasting, deep learning models such as LSTM and Transformer-based architectures
demonstrate superior performance in capturing complex temporal patterns. Hybrid
models, combining elements from fuzzy systems, optimization techniques, and deep
learning, achieve the highest accuracy but require significant data and computational
resources.
The thesis introduces a classification framework that aligns forecasting methods with
time horizons and data availability scales—from household-level to national-level
applications. Visual guides are provided to support model selection based on
forecasting objectives and data conditions. The study concludes that no single model
is universally optimal; effective forecasting requires context-sensitive method
selection, balancing accuracy, interpretability, and resource constraints.
Key-words: Load Forecasting, Electricity Demand, Machine Learning, Deep Learning,
Hybrid Models.

ii
Abstract in italiano
Una previsione accurata del carico elettrico è un elemento fondamentale nella
pianificazione e nella gestione dei sistemi energetici moderni, soprattutto alla luce
dell’elettrificazione crescente, dell’integrazione delle fonti rinnovabili e della
flessibilità della domanda. Questa tesi propone una revisione strutturata dei principali
metodi di previsione del carico elettrico, suddivisi in tre orizzonti temporali: breve
termine (fino a 1 settimana), medio termine (da 1 settimana a 1 mese) e lungo termine
(oltre 1 mese). Ogni categoria viene analizzata in relazione ai punti di forza, ai limiti
metodologici e ai requisiti di dati.
I modelli statistici, come la regressione lineare multipla e SARIMA, risultano adatti
alla previsione a breve termine per la loro semplicità e bassa esigenza di dati. Le
tecniche di machine learning, tra cui la regressione con support vectors o alberi
decisionali, offrono maggiore flessibilità per previsioni a medio termine. Per previsioni
a lungo termine, i modelli di deep learning come LSTM e le architetture basate su
Transformer si distinguono per la capacità di modellare sequenze complesse nel
tempo. I modelli ibridi—che combinano sistemi fuzzy, algoritmi di ottimizzazione e
deep learning—raggiungono la massima accuratezza, ma richiedono una disponibilità
significativa di dati e risorse computazionali.
La tesi propone un quadro di classificazione che collega i metodi previsionali agli
orizzonti temporali e ai livelli di disponibilità dei dati, da applicazioni domestiche fino
a quelle a scala nazionale. Vengono forniti strumenti visivi per supportare la scelta del
modello in base agli obiettivi previsionali e alle condizioni di disponibilità dei dati. Si
conclude che non esiste un modello universalmente migliore: una previsione efficace
richiede la scelta di metodi sensibili al contesto, che bilancino precisione,
interpretabilità e risorse disponibili.
Parole chiave: Previsione del Carico, Domanda di Elettricità, Apprendimento
Automatico, Deep Learning, Modelli Ibridi.

| Contents iii
Contents
Abstract ................................................................................................................................. i
Abstract in italiano .......................................................................................................... iii
Contents ............................................................................................................................... v
1 Introduction ............................................................................................................... 1
1.1. Importance of load forecasting .................................................................... 2
1.2. Objectives and scope of the thesis ............................................................... 2
1.3. Structure of the thesis ................................................................................... 3
2 Load Forecasting ....................................................................................................... 4
2.1. Time-based categorization of load forecasting ......................................... 4
2.1.1. Short-term load forecasting ..................................................................... 4
2.1.2. Medium-term load forecasting ................................................................ 5
2.1.3. Long-term load forecasting ...................................................................... 5
2.2. Factors affecting load forecasting ............................................................... 5
2.2.1. Weather and climate ................................................................................. 6
2.2.2. Building and appliance attributes ........................................................... 6
2.2.3. Sociodemographic and economic factors .............................................. 7
2.2.4. Technological factors and new appliances ............................................ 8
2.2.5. Behavioral and social factors ................................................................... 9
2.3. Challenges of load forecasting .................................................................. 10
2.3.1. Data quality and availability ................................................................. 10
2.3.2. Model accuracy and complexity ........................................................... 11
2.3.3. Uncertainty ............................................................................................... 13
2.3.4. Consumer variability .............................................................................. 14
2.4. Summary ...................................................................................................... 14
3 Short-term load forecasting .................................................................................. 15
3.1. Statistical models ......................................................................................... 15
3.1.1. Regression-based methods .................................................................... 15
3.1.2. ARIMA and SARIMA ............................................................................. 18
3.2. ML models .................................................................................................... 19
3.2.1. Support vector regression ...................................................................... 20

iv
3.2.2. Tree-based models ................................................................................... 22
3.2.3. k-nearest neighbors ................................................................................. 26
3.2.4. Artificial neural networks ...................................................................... 28
3.3. Deep learning models ................................................................................. 31
3.3.1. Recurrent neural networks ..................................................................... 31
3.3.2. Transformer-based models .................................................................... 34
3.4. Hybrid models ............................................................................................. 36
3.4.1. Statistical & ML hybrids ......................................................................... 36
3.4.2. Ensemble tree-based methods ............................................................... 37
3.4.3. Neural network-based hybrids ............................................................. 38
3.4.4. Intelligent and fuzzy logic hybrids ....................................................... 40
3.4.5. Transformer-based hybrids .................................................................... 40
3.5. Summary ....................................................................................................... 43
4 Medium-term load forecasting ............................................................................ 45
4.1. Statistical methods ....................................................................................... 45
4.1.1. Regression-based methods ..................................................................... 46
4.1.2. ARIMA and SARIMA ............................................................................. 48
4.2. ML models .................................................................................................... 49
4.2.1. Tree-based models ................................................................................... 50
4.2.2. k-NN .......................................................................................................... 55
4.2.3. ANN .......................................................................................................... 58
4.3. Deep learning models ................................................................................. 60
4.3.1. RNN ........................................................................................................... 60
4.3.2. Transformer-based models .................................................................... 62
4.4. Hybrid models ............................................................................................. 64
4.4.1. Statistical–deep learning hybrids .......................................................... 65
4.4.2. Transformer-based hybrids .................................................................... 66
4.4.3. CNN–LSTM hybrids ............................................................................... 66
4.4.4. Signal decomposition-based hybrids ................................................... 67
4.4.5. Neural Prophet–LSTM hybrids ............................................................. 68
4.5. Summary ....................................................................................................... 70
5 Long-term load forecasting ................................................................................... 72
5.1. Statistical methods ....................................................................................... 72
5.1.1. Regression-based models ....................................................................... 73
5.1.2. ARIMA and SARIMA ............................................................................. 74
5.2. Machine learning methods ......................................................................... 76
5.2.1. SVR ............................................................................................................ 76

| Contents v
5.2.2. Tree-based models .................................................................................. 78
5.2.3. ANN .......................................................................................................... 79
5.3. Deep learning ............................................................................................... 80
5.3.1. Multilayer perceptron ............................................................................. 81
5.3.2. LSTM ......................................................................................................... 82
5.3.3. Transformer-based models .................................................................... 84
5.4. Hybrid models ............................................................................................. 86
5.4.1. Fuzzy-Neural Network-Based Hybrid Models .................................. 86
5.4.2. Fuzzy-RNN-based models ..................................................................... 87
5.4.3. Fuzzy-SVM and grey system hybrid models ...................................... 88
5.4.4. LSTM-based hybrid deep learning models ......................................... 89
5.4.5. Transformer-based hybrid deep learning models .............................. 89
5.5. Summary ...................................................................................................... 91
6 Conclusion and future research directions ....................................................... 92
6.1. Recapitulation of research objectives and contributions ....................... 92
6.2. Strategic alignment between forecasting horizons and methods ........ 94
6.3. Method suitability based on data scale .................................................... 94
6.4. Implications for practice and policy ......................................................... 95
6.5. Limitations and future research directions ............................................. 95
6.6. Final remarks ............................................................................................... 96
Bibliography ..................................................................................................................... 97
List of Figures ................................................................................................................. 105
List of Tables .................................................................................................................. 107
Acknowledgments ......................................................................................................... 109

iv

1
1
Introduction
Electricity is an essential part of modern life, powering homes, industries, and
transportation systems. As Figure 1.1 shows, among all energy consumers, the
residential sector represents a significant share of total electricity demand. Households
consume energy for heating, cooling, lighting, cooking, and running electrical
appliances, with consumption patterns varying based on factors such as weather
conditions, socio-economic status, building structure, and consumer behavior [1]. In
2022, residential electricity consumption accounted for 25.8% of final energy
consumption in the European Union, reflecting its importance in overall power system
management [2].
Understanding the dynamics of residential electricity consumption is essential for
ensuring an efficient and stable power supply. Electricity demand fluctuates due to
daily and seasonal variations, economic conditions, and external influences such as
policy changes, technological advancements, and renewable energy integration [3].
Accurately forecasting electricity demand is therefore crucial for power system
operation, enabling utilities and policymakers to make informed decisions on grid
stability, energy pricing, and infrastructure investments.
Figure 1.1: Electricity consumption by sectors (GWh) [1].

2 | Introduction
1.1. Importance of load forecasting
Global electricity demand continues to surge, even as traditional fossil fuel reserves
become increasingly difficult to extract and deplete. Meanwhile, renewable energy
technologies remain in early adoption stages, exacerbating the energy crisis.
According to the International Energy Agency (IEA), accurate load forecasting is
essential for effective energy planning, power dispatch, and achieving Sustainable
Development Goals (SDG-7 and SDG-13). Benefits of electricity prediction is
mentioned in Figure 1.2. Precise forecasts not only enable utilities to optimize
generation schedules and control operational costs but also enhance grid stability by
preventing overloads and blackouts [4], [5].
The integration of smart grids within smart cities further underscores the importance
of advanced forecasting. Smart grids leverage digital communication technologies to
enable real-time monitoring and bidirectional data exchange between consumers and
utilities, thereby optimizing energy consumption and facilitating demand-side
management. This data-driven approach not only supports the efficient deployment
of renewable energy sources and clean transportation options but also informs
strategic urban planning and resource allocation. By enabling both short-term and
long-term predictions, these systems empower policymakers to make informed
decisions that enhance urban sustainability and resilience [6].
Figure 1.2: Benefits of electricity consumption prediction [4]
1.2. Objectives and scope of the thesis
The objectives and scope of this thesis are centered on a comprehensive examination
of contemporary load forecasting techniques across various time horizons, including
short-term, medium-term, and long-term forecasts. This study aims to systematically
classify and assess a wide range of forecasting models, encompassing traditional
statistical approaches, machine learning algorithms, deep learning architectures, and
hybrid methodologies. Particular attention is given to evaluating the effectiveness,
advantages, and limitations of these techniques in accurately predicting electricity
demand.

| Introduction 3
Rather than focusing on empirical data collection, preprocessing steps, or specific case
studies, the thesis adopts a conceptual and methodological perspective. It investigates
the key factors that influence power consumption and analyzes how these variables
impact the precision and reliability of forecasting models.
Additionally, the work critically engages with the ongoing challenges and recent
developments in the field, highlighting areas where existing methods may fall short
and where improvements are most needed. By identifying current research gaps and
future directions, the thesis contributes to the broader discourse on how forecasting
can evolve to meet the demands of modern energy systems.
Ultimately, this research is intended to offer valuable insights for scholars, industry
professionals, and policymakers, helping them to make informed decisions when
selecting, designing, or applying forecasting tools within the context of energy
planning and management.
1.3. Structure of the thesis
This thesis is structured into six chapters, each building a comprehensive
understanding of load forecasting methods across varying time horizons. Chapter 2
provides an overview of the fundamental concepts of load forecasting, including the
key variables that influence electricity demand, and the principal challenges associated
with forecasting load behavior.
Chapter 3 delves into Short-Term Load Forecasting (STLF), presenting a range of
methodologies such as traditional statistical techniques, machine learning algorithms,
and deep learning models. Chapter 4 shifts focus to Medium-Term Load Forecasting
(MTLF), analyzing models designed to predict energy demand over intervals ranging
from days to several months, and discussing strategies employed to improve forecast
accuracy. In Chapter 5, the thesis explores Long-Term Load Forecasting (LTLF),
covering both econometric approaches and artificial intelligence-based techniques
used to project demand over extended time frames.
Finally, Chapter Error! Reference source not found. offers a comparative assessment o
f the models presented in earlier chapters, evaluating their relative strengths,
limitations, and suitability for different forecasting horizons. This chapter also reviews
recent advancements in the field, outlines emerging research directions, and concludes
with key insights and recommendations aimed at enhancing forecasting
methodologies.
By offering a structured and critical analysis of load forecasting techniques across
short-, medium-, and long-term horizons, this thesis seeks to contribute to the
development of more accurate, adaptable, and robust forecasting solutions for the
evolving needs of modern power systems.

4 | Load Forecasting
2
Load Forecasting
Load forecasting refers to the process of predicting future electricity demand based on
historical consumption data, weather conditions, economic indicators, and other
influencing factors. Accurate forecasting is essential for ensuring grid stability,
optimizing power generation, and minimizing operational costs [5].
2.1. Time-based categorization of load forecasting
[7] categorized load forecasting into four time horizons: very short term, short-term,
medium-term, and long-term. However, for the purposes of this thesis, load
forecasting is categorized into three primary time-horizons, shown in Figure 2.1, based
on forecasting needs and the duration of the prediction.
Figure 2.1: Load forecasting time horizontal.
2.1.1. Short-term load forecasting
Short-term load forecasting predicts electricity demand for a period ranging from a
few minutes to one week. This time frame is crucial for operational decisions, such as
power generation scheduling, unit commitment, load switching, and demand-side
management. By providing accurate forecasts for such short time frames, utilities can
optimize resource utilization, reduce operational costs, and maintain grid stability [7].

| Load Forecasting 5
2.1.2. Medium-term load forecasting
Medium-term load forecasting covers periods from one week to one month. It is useful
for tasks like outage scheduling, maintenance planning, and tariff regulation. MTLF
helps utilities plan for intermediate-term fluctuations in electricity demand, ensuring
they are prepared for variations during high and low consumption periods [7].
2.1.3. Long-term load forecasting
Long-term load forecasting focuses on predicting electricity demand for periods
extending beyond one month. These forecasts are essential for strategic planning,
energy infrastructure development, and policymaking. Long-term predictions are
used to anticipate future power needs, ensuring that utilities can make informed
decisions regarding grid capacity expansion, resource allocation, and investment in
renewable energy [7].
2.2. Factors affecting load forecasting
In this section, we explore the various factors that significantly influence electricity
consumption and load forecasting. Residential electricity consumption (REC) is
shaped by a combination of socioeconomic indicators, building characteristics,
appliance ownership, and usage patterns which are shown in
Figure 2.2. Climate and location also play crucial roles, as heating and cooling
requirements are highly sensitive to temperature fluctuations, making city-scale
energy usage particularly responsive to weather conditions [8]. Additionally, factors
such as household size, income, energy efficiency measures, and technological
progress contribute to demand variability. As electricity generation and consumption
have notable environmental and social costs, understanding these drivers is vital for
developing effective policies and strategies for sustainable energy use.
Figure 2.2: Key factors affecting load forecasting.

6 | Load Forecasting
At the broader national level, REC is the aggregate of individual household decisions,
influenced by demographic changes, consumer preferences, and economic factors. The
increasing complexity of REC forecasting arises from shifting societal trends,
urbanization, the emergence of new appliances, and unpredictable human behavior,
all of which pose challenges for predictive models. Despite advancements, there are
still obstacles due to inaccurate data, evolving consumption patterns, and unforeseen
events such as public health crises [9]. Therefore, accurate load forecasting must
account for both technological and social factors that impact energy use across
different scales and regions [4], [10].
2.2.1. Weather and climate
Weather and climate are crucial factors influencing electricity consumption,
particularly in areas where heating and cooling demands vary with seasonal changes.
Temperature, humidity, and other weather variables have a significant impact on
electricity usage, especially in residential and commercial sectors. During extreme
weather conditions, such as very hot or cold temperatures, energy consumption tends
to rise due to increased use of air conditioning or heating systems. For instance, city-
scale electricity usage is highly temperature-sensitive, with heating and cooling needs
contributing significantly to total energy consumption. Seasonal variations further
lead to fluctuations in demand, with higher electricity usage during summer and
winter months.
Humidity also plays a key role in influencing electricity demand, particularly in hot
climates. The heat index, which reflects human perception of temperature, is
determined by combining air temperature and relative humidity. When relative
humidity is high, the evaporation process in the human body slows down, causing the
body to retain more heat. As a result, the perceived temperature increases, leading to
higher energy consumption for cooling. Therefore, areas with high humidity,
especially during the summer, experience a marked increase in energy demand due to
the added stress on cooling devices.
The growing impact of climate change has led to more frequent and extreme weather
events, further complicating traditional forecasting models. As weather patterns
become more unpredictable, advanced forecasting models are needed to ensure
reliable predictions. Additionally, the increasing integration of renewable energy
sources such as solar and wind power, which are intermittent and weather-dependent,
introduces further uncertainty into load demand. This requires more sophisticated
forecasting methods to integrate renewable energy efficiently into the grid while
maintaining a stable supply and demand balance [4], [8], [10], [11].
2.2.2. Building and appliance attributes
The type of building and the appliances within it are significant factors that influence
electricity consumption. Buildings with poor insulation, older electrical systems, or

| Load Forecasting 7
inefficient appliances tend to have higher energy demand compared to those that are
well-insulated and equipped with modern, energy-efficient systems. The design and
size of a building also play a role in determining how much energy is consumed. For
example, larger homes or buildings typically require more electricity for heating,
cooling, and lighting, while energy-efficient designs and materials can reduce overall
demand. Determining the influence of occupancy, dwelling size, and building
topologies on consumption is equally important in building accurate predictive
models for load forecasting [3].
Appliance usage patterns are another critical factor in load forecasting. Household
appliances, such as air conditioners, refrigerators, washing machines, and lighting
systems, directly impact the total electricity demand. The ownership and frequency of
use of these appliances are often linked to lifestyle choices, income levels, and regional
factors. In warmer climates, the widespread use of air conditioning systems
significantly increases electricity consumption, especially during peak summer
months.
The increasing adoption of energy-efficient appliances and building technologies can
mitigate some of the demand pressure on the grid. Energy-efficient appliances
consume less power and are becoming more prevalent in households and commercial
establishments due to technological advancements and incentives. These innovations
help lower the overall electricity consumption, especially during peak times,
contributing to more stable load profiles and easing the pressure on electricity grids.
By considering the type, usage, and efficiency of buildings and appliances, load
forecasting models can provide more accurate predictions and facilitate better energy
management [8], [9].
2.2.3. Sociodemographic and economic factors
Sociodemographic and economic factors play a crucial role in shaping electricity
consumption patterns. Key elements such as income, household size, education, and
urbanization influence energy demand significantly. Higher-income households tend
to consume more electricity due to increased usage of electrical appliances, heating
and cooling systems, and other electronic devices. Similarly, larger households require
more energy for daily activities, leading to higher electricity consumption compared
to smaller households. Additionally, lifestyle factors, such as the number of residents
working from home, can significantly impact consumption levels, particularly during
certain times of the day [8].
Economic conditions also affect electricity demand. During periods of economic
growth, electricity consumption rises due to increased industrial activity and higher
consumer spending. Conversely, during economic downturns, demand tends to fall as
businesses scale back operations and households adopt more energy-efficient practices
to save on costs. Furthermore, population growth directly influences total electricity
consumption, requiring utilities to adjust their forecasts accordingly. Projections show

8 | Load Forecasting
that countries and regions experiencing rapid urbanization, such as India, China, and
Southeast Asia, will see substantial increases in electricity demand over the next
decade, with India’s demand increasing by 40%, China’s by 25%, and Southeast Asia's
by 30% from 2019 to 2030 [10].
Urbanization is another significant factor. As urban populations grow, electricity
demand increases due to the higher number of households, commercial buildings, and
transportation needs. In urban areas, electricity consumption is heavily driven by the
need for lighting, heating, cooling, and powering appliances in both residential and
commercial spaces. This leads to higher overall demand for electricity in cities [9].
Moreover, sociodemographic factors such as the dependency ratio—the proportion of
non-working individuals (children and elderly) to the working-age population—also
affect electricity consumption. Households with high dependency ratios tend to
allocate more income toward basic needs, including electricity, which may reduce
their savings potential and increase overall demand for electricity [1].
In conclusion, sociodemographic and economic factors, including household
characteristics, urbanization, economic growth, and technological advancements,
significantly influence electricity consumption. Understanding these factors is
essential for developing accurate forecasting models, which help optimize energy
supply management and design targeted demand response strategies.
2.2.4. Technological factors and new appliances
Technological advancements and behavioral shifts, such as the widespread adoption
of electric vehicles (EVs) and smart devices, have introduced new patterns in electricity
demand. EVs require substantial charging infrastructure, which can shift demand
peaks and increase load during specific times of the day. Similarly, the integration of
distributed renewable energy systems, such as rooftop solar panels, is reshaping
traditional energy usage models. While these innovations promote energy efficiency
and enable partial self-generation, they can also introduce new demand peaks,
particularly when EVs are charged simultaneously during off-peak hours [5], [9].
A particularly notable challenge is the substantial increase in electricity demand
resulting from widespread EV adoption. This trend poses a serious burden on power
grids, especially residential distribution networks. For example, around 80% of EVs
are charged using residential in-home chargers, meaning their charging habits often
align with household consumption peaks [8]. As electrification expands, U.S.
electricity demand is projected to rise by 23% by 2050, with EVs accounting for up to
300 TWh of consumption. Moreover, if EV penetration reaches 30%, it could result in
a 50% increase in peak load at the residential distribution transformer level,
significantly stressing local grid infrastructure [12].
In parallel, the integration of smart grids and Internet of Things (IoT) technologies has
enhanced load forecasting accuracy. Smart meters and real-time monitoring systems

| Load Forecasting 9
provide granular insights into consumer behavior, enabling more adaptive and
dynamic energy management strategies [7].
Additionally, energy efficiency improvements, such as more efficient appliances, the
transition to LED lighting, and enhanced building insulation, have led to reductions
in per capita electricity use. These developments require regular updates to traditional
forecasting models to reflect evolving consumption patterns [5].
Demand-side management strategies, including time-of-use pricing and demand
response programs, have also started influencing user behavior. These approaches aim
to shift electricity usage away from peak times, flattening demand curves and
improving grid stability. However, their effectiveness still depends on consumer
engagement, which can vary widely [5].
In summary, while technological advancements introduce opportunities for smarter
and more efficient energy use, they also bring significant complexity and uncertainty
to forecasting models. The adoption rate, usage patterns, and integration of new
technologies like EVs and smart appliances must be carefully considered when
planning for future energy needs.
2.2.5. Behavioral and social factors
Human behavior plays a crucial, yet inherently unpredictable role in electricity
consumption, introducing significant challenges for accurate load forecasting.
Lifestyle changes, daily routines, cultural events such as holidays or festivals, and even
social norms can all lead to sudden and irregular fluctuations in electricity demand.
For example, increased home occupancy during weekends or national celebrations can
significantly raise residential electricity usage, making short-term forecasting more
difficult [9].
Moreover, growing awareness around environmental issues and participation in
demand-side management (DSM) programs has influenced consumer behavior. These
programs encourage users to modify their consumption habits, such as shifting energy
use to off-peak hours or reducing overall consumption, adding further variability to
usage patterns, and impacting forecast accuracy [9].
On an individual level, electricity consumption is strongly influenced by personal
decision-making, which is characterized by its stochastic and dynamic nature. As a
result, disaggregated or household-level forecasting models are particularly sensitive
to behavioral factors, often leading to higher variability and prediction errors. In
contrast, when energy demand is aggregated over a large population, the variability
introduced by individual behavior tends to balance out, resulting in relatively
smoother and more predictable trends [13].
These behavioral and social elements introduce a complex, human-centric dimension
to energy forecasting that cannot be fully captured by technical models alone. As
energy systems evolve to include more user-driven dynamics such as flexible

10 | Load Forecasting
consumption, remote work habits, and real-time energy feedback, the need for models
that integrate behavioral insights becomes increasingly important.
2.3. Challenges of load forecasting
Despite advancements in forecasting techniques, several challenges remain, as
described in the following.
2.3.1. Data quality and availability
Accurate electricity consumption forecasting relies heavily on the availability and
quality of data. However, several challenges complicate this process, especially when
forecasting individual consumption patterns.
Collecting detailed and reliable consumption data can be particularly difficult. Many
previous studies have relied on sub-metered data from individual appliances or
customer surveys, but obtaining such detailed information on a scale is often
impractical. When dealing with a large number of households, gathering daily usage
schedules or appliance-specific data becomes infeasible. In addition, concerns over
data privacy, particularly regarding personal appliance usage patterns, present further
barriers to widespread data collection [13].
Beyond access, the quality of the available data is another critical issue. Energy
consumption data sets frequently suffer from missing values, outliers, and
inconsistencies caused by sensor errors, manual data entry mistakes, or transmission
problems. These irregularities, if not addressed through effective data cleaning and
preprocessing, can significantly compromise the performance and reliability of
forecasting models [4].
Another challenge arises from the high-dimensional nature of electricity consumption
data. Forecasting load accurately involves analyzing multiple interdependent factors,
such as weather conditions, economic variables, and consumer behaviors. The
complexity and volume of these variables make it difficult to extract meaningful
patterns, particularly when individual household differences are considered.
Successful forecasting models must be capable of managing such high-dimensional
data to identify the underlying trends and relationships [14].
Furthermore, with the increasing deployment of smart grid technologies, the data
landscape has become even more complex. Smart grids generate multifaceted datasets
collected from a variety of sources, ranging from individual meters to city-wide
monitoring systems. While this data offers valuable insights into electricity
consumption patterns at different levels of aggregation, its complexity and volume
pose significant analytical challenges. Effective integration and analysis of smart grid
data are essential for enhancing the accuracy and reliability of consumption
forecasting models [6].

| Load Forecasting 11
2.3.2. Model accuracy and complexity
Accurate load forecasting requires selecting an appropriate model that balances
forecasting performance with computational efficiency. Electricity demand data often
exhibits nonlinear relationships influenced by external factors, posing challenges for
both traditional statistical methods and modern machine learning techniques.
Traditional models, such as ARIMA (AutoRegressive Integrated Moving Average)
and SARIMA (Seasonal ARIMA), are effective for capturing linear patterns in time-
series data. However, their predictive performance declines when dealing with
complex nonlinear relationships or sudden behavioral changes caused by factors such
as economic fluctuations or weather variability. In contrast, machine learning models
like Long Short-Term Memory (LSTM) networks and Convolutional Neural Networks
(CNNs) are better suited for identifying intricate nonlinear patterns. These models
significantly improve forecasting accuracy but demand substantial computational
resources and large datasets for training, which makes them computationally intensive
and time-consuming [6], [9], [15].
To address the limitations of both traditional and advanced deep learning approaches,
hybrid models have been developed. These models combine the strengths of statistical
methods and artificial intelligence techniques, such as integrating ARIMA with
Generative Adversarial Networks (GANs) or LSTM networks. Hybrid approaches
have demonstrated improved prediction performance by leveraging both linear and
nonlinear modeling capabilities. However, they introduce new challenges related to
optimization, interpretability, and computational cost. Training hybrid models is
computationally demanding, and interpreting their outputs can be complex, reducing
their practicality for real-time forecasting applications [15].
The reliance on deep learning and hybrid models has also raised concerns about
computational complexity and resource constraints. Models like XGBoost and Deep
Neural Networks (DNNs) require extensive datasets and considerable processing
power to achieve high accuracy [6], [9]. Hyperparameter tuning, which is essential for
enhancing model performance, further exacerbates computational demands. As a
result, deploying these models for real-time or large-scale forecasting in the power
systems industry can be challenging. While AI-driven approaches offer substantial
improvements in forecasting accuracy, ensuring that these models remain
computationally efficient and scalable is crucial for their practical application.
In summary, although deep learning and hybrid models present significant
advantages in terms of forecasting accuracy, optimizing them for computational
efficiency, and ensuring their feasibility for real-time implementation remain critical
challenges.
In load forecasting literature, evaluating the accuracy of predictive models is essential
for understanding their effectiveness and guiding their practical application. Model
performance is typically quantified using established error metrics that assess how

12  | Load Forecasting

closely the predicted values align with the actual observed data. These metrics not only
allow researchers to compare different forecasting approaches but also reveal how
models behave under various conditions and time horizons.
Commonly used accuracy measures include the Mean Absolute Error (MAE), Root
Mean Squared Error (RMSE) and Mean Absolute Percentage Error (MAPE). Each
provides distinct insights: MAE gives the average magnitude of prediction errors,
RMSE penalizes larger errors more heavily due to the squaring operation, and MAPE
expresses errors as a percentage, which is useful for comparing across different load
scales.
Table 2.1 summarizes the most commonly used evaluation metrics in load forecasting
research, including their mathematical formulations.
Table 2.1: Common error metrics used in the load forecasting literature.
Metric Name
Formula

𝑛
Mean Absolute  1
| 𝑀𝐴𝐸 | =  ∑|𝑦 | −𝑦̂|  |
| --- | ------ | ----- |
|     | 𝑛 𝑖    | 𝑖     |
Error
𝑡=1
𝑛
Mean Squared  1
| 𝑀𝑆𝐸 | = ∑(𝑦 −𝑦̂)2  |     |
| --- | ------------ | --- |
𝑖 𝑖
Error  𝑛
𝑡=1
𝑛
Root Mean Squared  1
| 𝑅𝑀𝑆𝐸 | = √ ∑(𝑦 | −𝑦̂)2  |
| ---- | ------- | ------ |
𝑖
Error  𝑛
𝑡=1
𝑛 −𝑦̂)2
Mean Absolute  1 (𝑦
|         | 𝑖   | 𝑖      |
| ------- | --- | ------ |
| 𝑀𝐴𝑃𝐸 =  | ∑|  | |×100  |
|         | 𝑛 𝑦 |        |
Percentage Error  𝑖
𝑡=1
| Coefficient of  | (𝑦 −𝑦̂)2 |     |
| --------------- | -------- | --- |
|                 | 𝑖        | 𝑖   |
| 𝑅2              | = 1−     |     |
| Determination   | (𝑦 −𝑌̅)2 |     |
𝑖

| Load Forecasting 13
Coefficient of
1
Variation of the √ ∑𝑛 (𝑦 −𝑦̂)2
𝑛 𝑡=1 𝑖
Root Mean Square 𝐶𝑉𝑅𝑀𝑆𝐸 = ×100
𝑌̅
Error
2.3.3. Uncertainty
Load forecasting is inherently uncertain due to the wide range of unpredictable factors
influencing electricity demand. These uncertainties complicate accurate prediction
and must be carefully considered to ensure reliable power system operation.
Unexpected public health events and behavioral shifts are major sources of forecasting
uncertainty. For example, during the COVID-19 pandemic, electricity consumption
patterns changed significantly. Countries with strict lockdown measures, such as
Spain and Italy, experienced electricity usage profiles resembling pre-pandemic
weekends, whereas countries like Sweden, with fewer restrictions, observed smaller
decreases in consumption [4]. Such events highlight how historical consumption data
may become unreliable for forecasting future demand.
Climate change also plays a critical role in altering load patterns. The increasing
frequency and intensity of extreme weather events, such as severe heatwaves or cold
snaps, can cause sudden peak loads in power systems [4], [16]. These load spikes
threaten grid stability by pushing distribution transformers and other equipment to
unsafe operational limits. As climate-driven changes make temperature-sensitive
demand more volatile, historical trends become less predictive, posing challenges for
short-term and peak load forecasting.
The variability introduced by renewable energy sources, particularly solar and wind
power, further adds to the uncertainty in load forecasting [5]. Since renewable
generation depends heavily on weather conditions, predicting the available electricity
supply becomes more complex. To address this, forecasting models must increasingly
incorporate probabilistic and scenario-based techniques to manage renewable energy
fluctuations and maintain grid reliability.
Economic fluctuations and unexpected power plant outages introduce additional
layers of uncertainty [4], [9]. Economic downturns or booms can significantly shift
electricity demand, especially in the industrial sector. Similarly, unplanned outages at
power plants can abruptly disrupt supply patterns, making load forecasting even
more volatile and challenging.
In summary, uncertainty in load forecasting arises from diverse factors including
public health crises, climate change, renewable energy variability, economic
conditions, and supply disruptions. Addressing these challenges requires the
development of advanced forecasting models capable of accounting for such
uncertainties, ensuring more resilient and reliable energy system operations.

14 | Load Forecasting
2.3.4. Consumer variability
The growing integration of smart grid technologies and emerging energy systems has
introduced new challenges for load forecasting, particularly due to the
unpredictability of consumer behavior. Smart meters and demand response programs
now provide utilities with greater control over load management, enabling dynamic
pricing and real-time adjustments to optimize energy consumption [5]. However,
consumer participation in these programs is highly variable, as individual willingness
to modify energy use based on price signals or grid demands differs significantly.
Factors such as weather conditions, economic circumstances, and personal preferences
further influence participation levels, adding uncertainty to forecasting efforts.
Emerging technologies like electric vehicles (EVs), battery storage systems, and
distributed energy generation are also reshaping traditional load demand profiles [5],
[12]. The widespread adoption of EVs introduces new and less predictable demand
patterns, as charging times and energy requirements may not align with historical
usage data. Similarly, battery storage and rooftop solar installations allow consumers
to both store and inject electricity into the grid, significantly altering net load profiles.
These technological developments add further complexity for forecasting models,
necessitating continuous adaptation to evolving consumption patterns and the
accelerating pace of technological innovation.
2.4. Summary
Chapter 2 highlighted the key challenges in electricity load forecasting, focusing on
factors like data quality, model complexity, and uncertainty. It discussed how weather,
economic changes, and unexpected events contribute to the volatility of load forecasts,
especially with the impact of climate change and extreme weather.
Traditional forecasting models struggle with capturing nonlinear relationships,
leading to the adoption of advanced machine learning techniques like deep learning
and hybrid models. However, these methods come with increased computational
demands. The integration of renewable energy sources and emerging technologies
such as smart grids, electric vehicles, and battery storage further complicates
forecasting.
The chapter also emphasized the importance of accurate short-term load forecasting,
particularly during peak load conditions, to ensure the stability of power systems.
Smart grid technologies and better metering infrastructure make this more achievable,
supporting effective power dispatching and reducing grid stress.
In conclusion, addressing the challenges in load forecasting requires advanced models
that balance accuracy and computational efficiency, enabling reliable predictions in an
increasingly dynamic environment.

| Short-term load forecasting 15
3
Short-term load forecasting
In this study, short-term load forecasting (STLF) refers to the prediction of electricity
demand over time horizons ranging from a few minutes up to a week. STLF plays a
vital role in various aspects of power system operations, including unit commitment,
load dispatch, demand response programs, and real-time energy market transactions
[7]. Accurate short-term forecasts enable utilities and grid operators to optimize
generation schedules, maintain system reliability, and minimize operational costs.
STLF models must account for a wide range of influencing factors such as weather
conditions, consumer behavior, public holidays, economic trends, and building
characteristics [11], [14]. These variables, combined with the inherently nonlinear and
stochastic nature of electricity demand, make the development of precise forecasting
models a complex task.
Over the years, STLF techniques have evolved from traditional statistical methods to
more sophisticated machine learning and deep learning approaches. More recently,
hybrid models that integrate multiple techniques have emerged, offering promising
improvements in forecast accuracy and adaptability to dynamic grid environments.
STLF techniques are typically categorized based on their modeling approach and
capacity to manage different patterns in electricity demand. The four primary groups
include statistical methods, machine learning techniques, deep learning models, and
hybrid or ensemble approaches.
3.1. Statistical models
Statistical methods, such as ARIMA and SARIMA, rely on historical patterns and
linear assumptions. They are valued for their interpretability and simplicity but are
limited in capturing nonlinear and complex dependencies. For example, SARIMA has
been shown to perform well under stable seasonal conditions but struggles with
dynamic or non-stationary inputs [17].
3.1.1. Regression-based methods
Regression-based models have historically formed the backbone of STLF, particularly
due to their clarity, computational efficiency, and ability to extract interpretable
insights from historical data. These models assume a functional relationship between

16 | Short-term load forecasting
input variables (e.g., weather, calendar features) and electricity demand. Several
variants exist; each suited to different forecasting contexts.
Linear Regression (LR) is a classical statistical method widely used in STLF,
particularly in early applications where simplicity, interpretability, and computational
efficiency are critical. In its standard form, linear regression models the relationship
between a dependent variable (e.g., electrical load) and one or more independent
variables (e.g., temperature, hour of the day, or occupancy) under the assumption of
linearity.
The general multiple linear regression model is expressed in Equation (3.1):
𝑌̂ = 𝛽 +𝛽₁𝑋₁ + 𝛽₂𝑋₂ + ...+ 𝛽ₙ𝑋ₙ + 𝜀, (3.1)
0
where: 𝑌̂ is the dependent variable (e.g., electricity consumption), 𝛽 is the intercept
0
(constant term), 𝛽 ,𝛽 ,…,𝛽 are the coefficients for the independent variables, and 𝜀 is
1 2 𝑛
an error term.
Katić et al. [18] provided quantitative error metrics comparing multiple linear
regression (MLR) and artificial neural network (ANN) models for predicting heating
energy consumption in school buildings. Their findings indicate that the ANN model
outperformed the MLR model in terms of predictive accuracy.
Specifically, the ANN model achieved a lower Mean Absolute Error and RMSE
compared to the MLR model. For instance, the ANN model's MAE was approximately
12% lower, and its RMSE was about 15% lower than those of the MLR model. These
results suggest that the ANN model was more effective in capturing the complex,
nonlinear relationships between building characteristics and heating energy
consumption.
The superior performance of the ANN model is attributed to its ability to model
intricate patterns and interactions among variables, which are often present in
building energy consumption data. In contrast, the MLR model, while simpler and
more interpretable, may not adequately capture such complexities, leading to higher
prediction errors.
In summary, the study by Katić et al. [18] demonstrates that while MLR models offer
simplicity and ease of interpretation, ANN models provide enhanced predictive
accuracy for modeling heating energy consumption in school buildings, particularly
when dealing with complex and nonlinear data relationships.
Nano [19] enhanced traditional MLR models by integrating calendar-based variables
such as weekdays, holidays, and seasonal patterns. This integration aimed to improve
the accuracy of daily and weekly load forecasts. While specific error metrics were not
detailed, the inclusion of these calendar variables likely contributed to a reduction in
forecasting errors by accounting for recurring patterns in electricity consumption.

| Short-term load forecasting 17
Dudek [20] introduced a pattern-based local linear regression approach for short-term
load forecasting. This method involved clustering daily load profiles and applying
separate linear regressions to each cluster, effectively capturing recurring short-term
load fluctuations. The study compared this approach with other models, including
ARIMA, exponential smoothing, neural networks, and the Nadaraya-Watson
estimator. The pattern-based local linear regression demonstrated high accuracy,
particularly in modeling daily load cycles, and offered advantages in terms of
simplicity and computational efficiency.
Nsangou et al. [21] conducted a comparative analysis of quantile regression, decision
tree, and ANN models to analyze household electricity consumption under
uncertainty. Their findings indicate that the ANN model outperformed the other two
methods, achieving lower values in RMSE, MAE, and Mean Absolute Percentage Error
(MAPE), along with a higher coefficient of determination (R2). This superior
performance is attributed to the ANN's ability to model complex, nonlinear
relationships in the data.
Table 3.1: Strengths and limitations of regression methods in STLF.
Model Type Strengths Weaknesses
Simple; interpretable; fast Limited to linear patterns;
Linear regression to compute; good as underperforms in dynamic or
baseline. nonlinear contexts.
Adapts to temporal Requires clustering or
Local linear
variations; better for segmentation; sensitive to
regression
pattern-based loads. pattern definition.
Captures variability and More complex; harder to
Quantile regression uncertainty; robust to interpret compared to mean-
outliers. based methods.
Regression models are often integrated into hybrid frameworks or used in ensemble
methods, especially when interpretability and speed are needed alongside accuracy.
In many real-world STLF systems, as mentioned in Table 3.1, regression serves as a
fast, initial approximation before more complex machine learning models are
employed.

18 | Short-term load forecasting
3.1.2. ARIMA and SARIMA
The ARIMA model and its seasonal extension, SARIMA, are widely used statistical
methods in STLF. These models are designed to capture time-based dependencies and
trends in electricity consumption, making them particularly useful in settings where
demand exhibits consistent temporal patterns.
An ARIMA model is defined by three parameters: p, d, and q. p is the number of
autoregressive terms, meaning it defines how many past values of the time series are
used to predict the current value; d indicates the degree of differencing required to
make the series stationary—that is, removing trends or seasonality that distort the
forecasting model; finally, q represents the number of lagged forecast errors included
in the model, which captures the influence of past deviations between predicted and
actual values.
When electricity demand exhibits seasonal patterns—such as higher consumption
during specific hours, days, or months—the SARIMA model extends ARIMA by
incorporating seasonal components. This is typically denoted as SARIMA (p, d, q) (P,
D, Q) [m], where the uppercase parameters (P, D, Q) mirror the ARIMA structure but
are applied to the seasonal cycle defined by m (e.g., m = 12 for monthly data or m = 24
for hourly data in daily cycles).
Bilgili and Pinar [17] applied SARIMA to forecast Turkey’s gross electricity
consumption and compared its performance with LSTM. SARIMA successfully
captured recurring seasonal trends and produced reasonable short-term forecasts;
however, it struggled with modeling nonlinear and long-range dependencies. In
contrast, LSTM significantly outperformed SARIMA across all error metrics.
Specifically, LSTM achieved a MAPE of 2.42%, MAE of 215.35 GWh, and RMSE of
329.9 GWh, along with an R-value of 0.9992. These results highlight LSTM’s superior
ability to capture complex temporal dynamics, especially during volatile periods,
making it a more robust tool for forecasting electricity demand.
Gellert et al. [22] used ARIMA and (Trigonometric, Box-Cox transformation, ARMA
errors, Trend, and Seasonal components) TBATS to forecast electricity consumption
and PV energy production in smart homes, applying these models to datasets with 5-
minute, hourly, and bi-hourly resolutions. ARIMA performed well under stable,
structured conditions but struggled with high-frequency variability and irregular
generation patterns. TBATS outperformed ARIMA and even neural models in those
scenarios, achieving a lower MAE of 73.62 W. Its ability to manage multiple seasonality
and adapt to complex fluctuations made TBATS a more suitable option for short-term
forecasting in smart home environments.

| Short-term load forecasting 19
Table 3.2: Strengths and limitations of ARIMA and SARIMA methods in STLF.
Model Type Strengths Weaknesses
Captures short-term Assumes linearity,
temporal dependencies, requires data stationarity,
ARIMA
easy to interpret, not suited for complex,
low computational cost. nonlinear systems.
Parameter tuning can be
Effective models seasonal complex,
SARIMA patterns, performance declines with
widely used in practice. high-frequency variability or
external shocks.
In summary, ARIMA and SARIMA have proven to be effective baseline methods for
short-term load forecasting when the data exhibits strong linearity and regular
seasonal trends. As demonstrated in the studies by Bilgili and Pinar [17] and Gellert et
al. [22], these models perform well under stable conditions and structured
consumption patterns. SARIMA, in particular, can manage seasonal effects efficiently
and offers interpretability with relatively low computational cost. However, both
ARIMA and SARIMA show clear limitations in more complex, volatile environments
where nonlinear dependencies, high-frequency variability, or long-range temporal
relationships are present. In such cases, more advanced models like LSTM or TBATS
consistently outperform them, making traditional statistical models less suitable for
modern, dynamic energy systems in short-term forecasting applications. A summary
of the strengths and limitations of ARIMA and SARIMA in short-term load forecasting
is provided in Table 3.2.
3.2. ML models
With the increasing complexity of electricity consumption patterns and the availability
of large volumes of smart meter data, machine learning (ML) models have emerged as
powerful tools for STLF. Unlike traditional statistical methods, ML techniques can
capture nonlinear relationships and complex interactions between multiple variables
without explicit assumptions about the underlying data distribution.
ML models learn directly from historical data by identifying patterns and
dependencies, often using features such as time, temperature, humidity, occupancy,
or appliance usage. These models have demonstrated superior accuracy and
adaptability in scenarios with high variability or when external factors significantly
influence consumption [10], [14].

20 | Short-term load forecasting
3.2.1. Support vector regression
Support Vector Regression (SVR) is a machine learning technique derived from
Support Vector Machines (SVM), widely used in regression tasks involving complex,
nonlinear, and high-dimensional data. It is particularly effective in STLF due to its
robustness, generalization capability, and adaptability to various data distributions.
The SVR regression function uses a dot product in high-dimensional space via a kernel
function. The formal expression is given in Equation (3.2). This formulation has been
widely used in load forecasting literature, including recent studies such as Bendaoud
et al. [23].
𝑚
𝑓(𝑥) = ∑𝜔 𝜑 (𝑥)+𝛽 = 𝜔𝑇𝜑(𝑥)+𝛽, (3.2)
𝑖 𝑖
𝑖=1
Where f(x) is the predicted output, 𝜑(𝑥) is a nonlinear function mapping the input data
into a higher-dimensional space, 𝜔 is the weight vector, 𝛽 is the bias term, 𝜔𝑇𝜑(𝑥)
represents the dot product between the weight vector and the transformed input
features.
This formulation enables SVR to perform nonlinear regression by applying the kernel
trick, which replaces the explicit computation of 𝜑(𝑥) with kernel functions such as
radial basis function (RBF), polynomial, or linear kernels. The kernel function
computes the inner product 𝜑(𝑥 )𝑇𝜑(𝑥 ) implicitly, significantly reducing
𝑖 𝑖
computational complexity.
Figure 3.1: SVR model.
As it is shown in Figure 3.1 ,SVR operates by using the kernel function to map the
input data to a higher-dimensional space, where data are fit with a linear regression
model while introducing an ε-insensitive loss margin, within which deviations from
the true value are not penalized. This results in a sparse model where only data points
lying outside the ε-margin (called support vectors) influence the solution. The model

| Short-term load forecasting 21
is regularized by a parameter C, which controls the trade-off between model linearity
(in the higher dimensional space) and tolerance to error outside the ε-margin [23].
Bendaoud et al. [23] conducted a comparative study on short-term load forecasting in
Algeria, evaluating SVR alongside ANN, CNN, and Gradient Boosting methods. SVR
demonstrated robust performance, outperforming ANN and linear regression models,
and achieving a MAPE of 2.17%. Its effectiveness was particularly notable in capturing
nonlinear load behaviors during weekends, indicating its suitability for modeling
complex consumption patterns in short-term forecasts.
Haque and Rahman [24] compared SVR with shallow ANN and deep learning models
like LSTM networks for energy consumption forecasting. While LSTM achieved the
lowest forecasting errors, SVR offered a compelling balance between accuracy and
computational efficiency. It outperformed traditional models and was less resource-
intensive than deep networks, making it a practical choice for scenarios with
structured yet moderately complex patterns.
Zhang et al. [25] integrated SVR into an Explainable Artificial Intelligence (XAI)
framework to estimate building energy consumption and greenhouse gas emissions.
The study demonstrated that SVR could deliver competitive predictive accuracy while
supporting partial model interpretability through SHAP (SHapley Additive
exPlanations) values. This approach provided insights into the relative importance of
different input features, enhancing the transparency of the forecasting model.
Hasan et al. [26] enhanced SVR's predictive capabilities by combining it with Genetic
Algorithms (GA) to optimize hyperparameters for energy consumption forecasting
across four economic sectors. The GA-optimized SVR model achieved significantly
improved performance, showcasing the advantage of integrating heuristic
optimization techniques to address challenges posed by multivariate, nonlinear, and
large-scale datasets.
These studies collectively underscore SVR's versatility and effectiveness in energy
consumption forecasting, particularly when dealing with nonlinear patterns and when
computational resources are a consideration. For a detailed overview of SVR's
strengths and weaknesses, please refer to Table 3.3.

22 | Short-term load forecasting
Table 3.3: Strengths and limitations of SVR method in STLF.
Model Type Strengths Weaknesses
Strong performance with
Requires careful tuning of
nonlinear and high-
kernel parameters (e.g., C, ε,
dimensional datasets;
kernel type); Can be
Robust to overfitting in
computationally expensive for
small to medium-sized
very large datasets; Less
datasets; Flexible kernel
SVR interpretable than simpler
functions support complex
models unless combined with
feature transformations;
explainable AI; May
Performs well as both a
underperform deep models in
standalone model and
highly dynamic or long-
within hybrid optimization
horizon scenarios
frameworks
3.2.2. Tree-based models
Tree-based models have become a central component of modern ML thanks to their
ability to model complex nonlinear relationships, capture interactions between
variables, and provide interpretable outputs in many cases. In the context of STLF,
they offer strong predictive performance while managing structured tabular data,
time-based features, and weather inputs with ease. This section discusses three key
approaches: Decision Tree Regression, Random Forests, and Extreme Gradient
Boosting (XGBoost), each building on the foundational principles of decision trees.
Figure 3.2: Tree-based model.

| Short-term load forecasting 23
Figure 3.2 illustration of the structural differences between Decision Tree Regression
(DTR), Random Forest (RF), and XGBoost models. In DTR, a single tree is used to
generate one prediction. RF builds multiple decision trees in parallel and averages
their outputs to produce the final result. XGBoost, on the other hand, builds trees
sequentially, where each tree corrects the errors of the previous one, and the final
prediction is obtained from the last tree in the sequence.
3.2.2.1. Decision tree regression
A DTR model operates by recursively partitioning the input space to reduce variance
within each subset. At each internal node, the algorithm selects a feature 𝑥 and
𝑗
threshold t that minimizes the sum of squared errors across the two resulting regions.
This criterion is expressed mathematically in Equation (3.3):
min[ ∑ (𝑦 −𝑦̅𝑅 )2+ ∑ (𝑦 −𝑦̅𝑅 )2], (3.3)
𝑖 1 𝑖 2
𝑗,𝑡
𝑥
𝑖
∈𝑅1(𝑗,𝑡) 𝑥
𝑖
∈𝑅2(𝑗,𝑡)
Where: 𝑅 and 𝑅 are the left and right branches split on feature 𝑥 at threshold t, 𝑦̅𝑅
1 2 𝑗 𝑘
is the Mean of the target values in each region.
Peteleaza et al. [6] conducted a comprehensive study on electricity consumption
forecasting for sustainable smart cities using machine learning methods. Their
research involved a comparative analysis of seven different models, including decision
trees, applied to datasets from three metropolitan areas in the United States: Los
Angeles, Sacramento, and New York. The decision tree models demonstrated strong
interpretability and adaptability to daily and seasonal patterns, making them valuable
for understanding energy use behaviors in smart-city contexts. Notably, the study
found that Light Gradient Boosting Machine (LightGBM), a decision tree-based
ensemble method, provided the best results with a Coefficient of Variation of the Root
Mean Square Error (CVRMSE) of 6.5% for Los Angeles, 4.6% for Sacramento, and 4.1%
for New York. These findings highlight the effectiveness of decision tree approaches
in capturing complex consumption patterns across diverse urban settings.
Nsangou et al. [21] explored the application of decision trees in explaining household
electricity consumption in Cameroon. Their study compared the performance of
decision trees with quantile regression and ANN in assessing electricity consumption
drivers. The decision tree models were instrumental in identifying key factors
influencing energy use, such as equipment usage, household income levels, housing
structures, and weather conditions. While the ANN model outperformed the others in
terms of predictive accuracy, the decision tree approach offered superior
interpretability, allowing for a clearer understanding of how various factors contribute
to electricity consumption.
These studies underscore the utility of Decision Tree methods in energy consumption
forecasting, particularly in scenarios where model interpretability and adaptability to

24 | Short-term load forecasting
varying consumption patterns are crucial. For a detailed overview of the strengths and
weaknesses of Decision Tree models in this context, please refer to Table 3.4.
3.2.2.2. Random Forests
Building upon this concept, Random Forests introduce an ensemble strategy by
training multiple decision trees on bootstrapped subsets of the data. Each tree
contributes a prediction, and the final result is computed as the average of all
individual outputs. This aggregation approach is formalized in Equation (3.4):
𝑇
1
𝑦̂ = ∑ℎ (𝑥), (3.4)
𝑇 𝑡
𝑡=1
Where T is the number of decision trees, ℎ (𝑥) is the prediction from the 𝑡𝑡ℎ tree.
𝑡
Rafiq et al. [3] conducted an in-depth analysis of residential electricity consumption
patterns in Dubai, utilizing high-resolution smart meter data, weather information,
and voluntary survey data on household characteristics. The study employed K-means
clustering to group households based on their consumption profiles and applied
various classification algorithms, including Random Forest, to predict household
consumption patterns based on dwelling and occupant characteristics. The RF model
demonstrated strong performance and interpretability, effectively identifying key
factors driving consumption patterns, such as cooling systems, number of occupants,
and dwelling size. This approach provided valuable insights for demand-side
management initiatives and the design of energy-saving strategies in residential
sectors.
Peteleaza et al. [6] explored electricity consumption forecasting for sustainable smart
cities using machine learning methods. The study compared the performance of
various models, including Random Forest, in predicting electricity consumption at the
city level. The RF model outperformed individual decision trees, demonstrating
higher accuracy and robustness in capturing complex consumption patterns across
diverse urban settings. The ensemble nature of RF, which combines multiple decision
trees, contributed to its improved generalization and reduced overfitting, making it a
suitable choice for load forecasting in smart city applications.
These studies underscore the utility of Random Forest methods in energy
consumption forecasting, particularly in scenarios where model interpretability and
adaptability to varying consumption patterns are crucial. For a detailed overview of
the strengths and weaknesses of Random Forest models in this context, please refer to
Table 3.1.
3.2.2.3. Extreme gradient boosting
Further extending the ensemble concept, XGBoost builds trees sequentially, with each
new tree aiming to correct the residual errors of the combined prior models. XGBoost

| Short-term load forecasting 25
is a regularized implementation of GBMs, offering advantages in speed, accuracy, and
overfitting control. The cumulative prediction of an XGBoost model can be expressed
as shown in Equation (3.5):
𝑀
𝐹(𝑥) = ∑ 𝛾 ℎ (𝑥), (3.5)
𝑚 𝑚
𝑚=1
Where ℎ (𝑥) is the 𝑚𝑡ℎ decision tree, 𝛾 is the learning rate applied to its output.
𝑚 𝑚
Bendaoud et al. [23] conducted a comparative study evaluating the performance of
various machine learning models, including SVR, ANN, CNN, and XGBoost, for STLF
in Algeria. The study found that XGBoost outperformed the other models, achieving
the lowest MAPE of 1.88%. This superior performance was attributed to XGBoost's
ability to manage complex nonlinear relationships and its robustness against
overfitting, making it particularly effective in capturing the intricacies of electricity
consumption patterns.
Deng et al. [16] proposed a hybrid Bagging–XGBoost model aimed at improving load
forecasting accuracy under extreme weather conditions. By integrating the Bagging
ensemble method with XGBoost, the model enhanced generalization capabilities and
reduced variance, leading to more reliable predictions during volatile environmental
scenarios. The hybrid approach demonstrated robustness and accuracy, effectively
addressing the challenges posed by extreme weather events in energy demand
forecasting.
Zhang et al. [25] incorporated XGBoost into an XAI framework to predict building
energy consumption and greenhouse gas emissions. Utilizing SHapley Additive
exPlanations values, the study provided insights into the contribution of each feature
to the model's predictions, enhancing interpretability. The integration of XGBoost with
SHAP allowed for accurate forecasting while offering transparency, enabling
stakeholders to understand the driving factors behind energy consumption patterns.
Rafiq et al. [3] applied XGBoost for household classification tasks based on smart meter
data in Dubai. The model achieved high accuracy levels above 95%, effectively
distinguishing between different household electricity usage profiles. XGBoost's
capability to manage large datasets with numerous features contributed to its strong
performance, making it a valuable tool for energy consumption analysis and customer
segmentation.
These studies collectively highlight XGBoost's versatility and effectiveness in energy
consumption forecasting, particularly in handling complex datasets, providing
accurate predictions, and offering interpretability when combined with tools like
SHAP. For a detailed overview of XGBoost's strengths and weaknesses in this context,
please refer to Table 3.4.

26 | Short-term load forecasting
Table 3.4: Strengths and Limitations of Tree-Based Methods in STLF.
Model Type Strengths Weaknesses
Simple; interpretable; Prone to overfitting; sensitive
Decision Tree
models non-linearity to data changes
Reduces overfitting; good
Less interpretable; Large
Random Forest generalization; manages
models can be slow
missing data
High accuracy;
Requires tuning;
Regularized; manages
XGBoost computationally more
feature interactions and
intensive
missing values
3.2.3. k-nearest neighbors
The k-NN algorithm is a non-parametric and instance-based learning method that has
been widely applied in STLF due to its simplicity and ability to model nonlinear
relationships without requiring an explicit training phase. In regression settings, k-NN
predicts the output for a new instance by averaging the target values of the k most
similar observations in the historical dataset.
The standard k-NN regression function can be mathematically represented in
Equation (3.6):
1
𝑦̂(𝑥) = ∑ 𝑦 ,
𝑘 𝑖 (3.6)
𝑖∈𝑁 (𝑥)
𝑘
Where 𝑦̂(𝑥) is the predicted load value for the input instance x, 𝑁 (𝑥) is the set of k
𝑘
nearest neighbors to x, based on a chosen distance metric (commonly Euclidean
distance), 𝑦 is the observed load associated with the neighbor i.
𝑖
This method assumes that similar inputs produce similar outputs, making it especially
useful for recognizing recurring load patterns over time.
K-NN algorithm has been widely used in both standalone and hybrid frameworks for
energy consumption forecasting due to its simplicity, interpretability, and
effectiveness in pattern recognition. Peteleaza et al. [6] included k-NN in a
comparative study involving various machine learning models for smart city

| Short-term load forecasting 27
electricity consumption forecasting across metropolitan areas in the United States.
While k-NN performed reasonably well in identifying similar historical consumption
profiles, it was ultimately surpassed by more advanced ensemble models such as
XGBoost in terms of accuracy. However, the authors emphasized that the
interpretability and pattern-matching capabilities of k-NN remain advantageous in
applications where understanding consumption behavior is as important as predictive
precision.
Rafiq et al. [3] employed k-NN in a classification task based on residential electricity
consumption data from Dubai. The study used k-means clustering to group household
consumption patterns and then applied k-NN as a baseline classifier to identify
similarities between user profiles. Although more sophisticated classifiers were
introduced later in the study, k-NN played a crucial role in modelling userbehavior
and establishing an interpretable reference point for further algorithmic comparisons.
Similarly, Zhou et al. [27] utilized k-NN to enhance cluster-based short-term load
forecasting for different building types in a Chinese case study. By grouping buildings
with similar consumption characteristics, the model applied k-NN to exploit local
similarities in daily demand trends. This approach was particularly effective in
contexts with high building diversity and limited historical data, where leveraging
neighbourhood-based predictions helped improve accuracy without the complexity of
deep learning methods.
Together, these studies demonstrate the ongoing relevance of k-NN in energy
forecasting, particularly in scenarios involving heterogeneous datasets, limited data
history, or a need for transparent, easy-to-understand models. A summary of the
strengths and limitations of the k-NN method in this context is presented in Table 3.5.
Table 3.5: Strengths and limitations of k-NN method in STLF.
Model Type Strengths Weaknesses
Computationally expensive
Simple and intuitive to
with large datasets; Sensitive
implement; No training
to irrelevant or unscaled
phase required; Effective in
features; Performance
capturing local patterns
degrades in high-dimensional
and repeated load
k-NN spaces; Does not manage
behaviors; Works well for
temporal dependencies unless
nonlinear relationships;
explicitly engineered; Model
Easily adaptable for both
performance depends heavily
regression and
on the choice of distance
classification tasks.
metric and k value.

28 | Short-term load forecasting
3.2.4. Artificial neural networks
ANNs are computational models inspired by the biological structure of the human
brain. They consist of interconnected layers of processing units (neurons) capable of
learning complex, nonlinear relationships between inputs and outputs. In STLF,
ANNs have proven to be highly effective due to their flexibility, ability to capture
hidden patterns, and capacity to model temporal and seasonal dynamics in electricity
consumption.
A typical feedforward neural network (FFNN) as it is shown in Figure 3.3 consists of
an input layer, one or more hidden layers, and an output layer. Each neuron in the
network computes the weighted sum of its inputs and applies an activation function
to introduce nonlinearity. The model is trained to minimize the prediction error using
backpropagation and gradient descent, adjusting the weights of the connections
between neurons to improve accuracy over successive iterations.
1. Feedforward Neural Network: The simplest ANN architecture used in
forecasting tasks is the FFNN. It consists of three components:
• Input Layer: This layer represents the input features such as historical
electricity consumption, time of day, temperature, and other relevant
factors.
• Hidden Layers: These layers apply nonlinear transformations to the
input data. Each neuron in the hidden layer computes a weighted sum
of its inputs and passes the result through an activation function.
• Output Layer: The output layer produces the final prediction, which in
load forecasting is usually the predicted electricity consumption at a
future time point.
The output of each neuron in the hidden layers is computed based on Equation
(3.7):
𝑛
(𝑙) (𝑙) (𝑙−1) (𝑙)
𝑧 = ∑𝑤 𝑥 +𝑏 , (3.7)
𝑗 𝑖𝑗 𝑖 𝑗
𝑖=1
(𝑙) (𝑙)
Where 𝑧 is the input to the 𝑗 neuron in layer l, 𝑤 is the weight of the
𝑗 𝑡ℎ 𝑖𝑗
connection between neuron i in the previous layer and neuron j in the current
(𝑙−1) (𝑙)
layer, 𝑥 is the output from the previous layer, and 𝑏 is the bias term for
𝑖 𝑗
neuron j in layer l.
The neuron then applies an activation function 𝜎 (such as Sigmoid or ReLU) to
the weighted sum to produce the output based on Equation (3.8):
(𝑙) (𝑙)
𝑎 = 𝜎(𝑧 ), (3.8)
𝑗 𝑗
Where 𝜎 is a nonlinear activation function like Sigmoid in Equation (3.9):

| Short-term load forecasting 29
1
𝜎(𝑥) = , (3.9)
1+𝑒−𝑥
Or ReLU by Equation (3.10):
𝜎(𝑥) = max(0,𝑥), (3.10)
2. Training the Network: The training of an ANN involves adjusting the weights
to minimize the error between the predicted and actual values. The error is
computed using a loss function, such as MSE for regression tasks that are
defined in Equation Error! Reference source not found.(3.11):
𝑁
1
𝐿 = ∑(𝑦 −𝑦̂ )2, (3.11)
𝑁 𝑖 𝑖
𝑖=1
Where L is the loss function or error, N is the number of data points (samples)
in the dataset, 𝑦 is the true value (actual electricity consumption) for the 𝑖
𝑖 𝑡ℎ
sample, 𝑦̂ is the predicted value (forecasted electricity consumption) for the 𝑖
𝑖 𝑡ℎ
sample, (𝑦 −𝑦̂ )2 represents the squared error for the 𝑖 sample, which
𝑖 𝑖 𝑡ℎ
measures how far the predicted value is from the actual value.
Backpropagation is used to compute the gradient of the loss function with
respect to each weight, which allows the network to adjust the weights
iteratively to reduce the error. The weight updates are performed using an
optimization algorithm like Stochastic Gradient Descent (SGD) or Adam based
on Equation (3.12):
𝜔 ← ω−𝜂.∇ 𝐿, (3.12)
𝜔
Where 𝜔 represents the weights of the network, 𝜂 is the learning rate, ∇ 𝐿 is the
𝜔
gradient of the loss function with respect to the weights.
Through multiple iterations, the model learns to predict future load with
increasing accuracy by adjusting the weights to better fit the data.

30 | Short-term load forecasting
Figure 3.3: Feedforward and backpropagation architecture of ANN.
Bendaoud et al. [23] conducted a comparative study evaluating the performance of
various machine learning models, including SVR, CNN, Gradient Boosting, and
ANNs, for STLF in Algeria. The study found that while Gradient Boosting achieved
the highest accuracy, ANNs performed commendably, achieving a MAPE of 2.39%.
This indicates that ANNs are effective in environments where model simplicity and
adaptability are preferred.
Haque and Rahman [24] applied ANN models to both 30-minute and 24-hour ahead
load forecasts. Their findings revealed that ANNs outperformed SVR and linear
models, offering a favorable balance between complexity and accuracy. However, in
more dynamic scenarios, LSTM networks surpassed ANNs in predictive performance,
highlighting the importance of model selection based on the specific forecasting
context.
Katić et al. [18] developed ANN models to estimate heating energy consumption in
school buildings. Their research demonstrated that ANN models achieved lower
RMSE and CVRMSE compared to multiple linear regression models. This affirms the
value of ANNs in building-level energy forecasting, particularly in capturing complex,
nonlinear relationships inherent in energy consumption data.
Despite their strengths, ANNs also present certain challenges. They require substantial
datasets for effective training and necessitate careful tuning of hyperparameters, such
as learning rates, the number of hidden layers, and neuron counts. Additionally,
ANNs often lack interpretability, making it difficult to understand the underlying
decision-making process. Without proper regularization, they are prone to overfitting,
especially when applied to small or noisy datasets.

| Short-term load forecasting 31
These studies collectively underscore the applicability of ANNs in energy
consumption forecasting, highlighting their strengths in modeling complex patterns
and their limitations concerning data requirements and interpretability that
mentioned in Table 3.6.
Table 3.6: Strengths and limitations of ANNs in STLF.
Model Type Strengths Weaknesses
Capable of modeling
complex, nonlinear
Prone to overfitting with small
relationships,
or noisy datasets,
Effective in both short-term
Requires careful tuning of
and pattern-based load
network architecture,
ANN forecasting,
Difficult to interpret ("black
Can integrate diverse
box" behavior),
features (e.g., temperature,
Computationally intensive
calendar, occupancy),
during training.
Adaptable to hybrid or
deep learning frameworks.
3.3. Deep learning models
DL models are a specialized subset of ANNs that involve architectures with multiple
hidden layers, enabling them to learn high-level abstractions and hierarchical feature
representations. In the context of STLF, DL techniques have shown superior
performance in modeling nonlinear, temporal, and seasonal electricity consumption
patterns, particularly in complex environments such as smart grids and real-time
demand prediction.
Unlike shallow neural networks, deep learning models can automatically extract
meaningful features from raw data, minimizing the need for manual feature
engineering. Among the most commonly used deep learning architectures in energy
forecasting are Recurrent Neural Networks (RNNs), LSTM, and CNNs.
3.3.1. Recurrent neural networks
RNNs are designed to process sequential data by maintaining internal memory
through feedback connections. This makes them ideal for time-series tasks such as load
forecasting. However, standard RNNs suffer from the vanishing gradient problem
described below, which limits their ability to capture long-term dependencies.

32  | Short-term load forecasting

RNNs are designed to process sequential data by maintaining an internal hidden state
that  evolves  over  time.  This  architecture  allows  RNNs  to  capture  temporal
dependencies,  making  them  suitable  for  tasks  like  electricity  load  forecasting.
However,  training  RNNs  over  long  sequences  presents  significant  challenges,
particularly due to the vanishing gradient problem.
As shown by Pascanu et al. [28], when training RNNs using Backpropagation Through
Time (BPTT), gradients are propagated backward through many time steps. During
this process, the gradients are repeatedly multiplied by the Jacobian matrix of the
recurrent weights. If the spectral radius (i.e., the largest absolute eigenvalue) of this
matrix is less than one, the gradients shrink exponentially with each time step. As a
result, early layers in the sequence receive near-zero gradients, effectively preventing
the model from learning long-term dependencies.
This  vanishing  effect  causes  the  RNN  to  focus  mainly  on  recent  inputs  while
"forgetting" information from earlier time steps, which undermines its ability to model
long-range  correlations—a  limitation  particularly  problematic  in  time  series
forecasting where historical context is crucial.
Pascanu et al.[28] also showed that the exploding gradient problem can occur in the
opposite scenario, when gradients grow exponentially due to large weight values.
Together, these issues severely hamper RNN training.
To address the vanishing gradient problem, gated architectures like LSTM and Gated
Recurrent Units (GRUs) were developed. These models incorporate mechanisms that
allow gradients to pass through many time steps without significant attenuation,
enabling them to learn long-term dependencies more effectively.
To address this, LSTM networks were introduced: they incorporate memory cells and
gating mechanisms (input, output, and forget gates), enabling them to learn long-
range dependencies more effectively.
The internal operations of an LSTM unit can be summarized by the set of equations
(3.13):
| 𝑓 = | 𝜎(𝑊 | ∙[ℎ | ,𝑥 ]+𝑏 |     |
| --- | --- | --- | ------ | --- |
| 𝑡   | 𝑓   | 𝑡−1 | 𝑡 𝑓    |     |

| 𝑖   | = 𝜎(𝑊 | ∙[ℎ | ,𝑥 ]+𝑏 |     |
| --- | ----- | --- | ------ | --- |

|   𝑡   | 𝑖       | 𝑡−1      | 𝑡 𝑖    |         |
| ----- | ------- | -------- | ------ | ------- |
|       |         | ∙[ℎ      | ]+𝑏    |         |
| 𝑜     | = 𝜎(𝑊   |          | ,𝑥     |         |
| 𝑡     | 𝑜       | 𝑡−1      | 𝑡 𝑜    | (3.13)  |
|  𝐶̃ = | tanh (𝑊 | ∙[ℎ      | ,𝑥 ]+𝑏 |         |
| 𝑡     |         | 𝐶 𝑡−1    | 𝑡 𝐶    |         |
|   𝐶   | = 𝑓 ∗𝐶  | +𝑖       | ∗𝐶̃    |         |
|       | 𝑡 𝑡     | 𝑡−1      | 𝑡 𝑡    |         |
| {     | ℎ = 𝑜   | ∗tanh (𝐶 | )      |         |
|       | 𝑡 𝑡     |          | 𝑡      |         |

| Short-term load forecasting 33
Where 𝑥 is the input at time t, ℎ is the hidden state, 𝐶 is the cell state, 𝜎 is the sigmoid
𝑡 𝑡 𝑡
function, ∗ denotes element-wise multiplication.
Figure 3.4: Schematic diagram of the LSTM [29].
These equations and Figure 3.4 describe how the model selectively forgets, updates,
and outputs information across time steps, making it ideal for sequence forecasting
tasks like STLF.
LSTM networks have shown substantial promise in the domain of electricity load
forecasting, especially when compared to traditional statistical and shallow learning
models. In a study by Bilgili and Pinar [17], LSTM was evaluated against the SARIMA
model for forecasting Turkey’s gross electricity consumption. Their findings
demonstrated that LSTM significantly outperformed SARIMA, particularly in
modelling nonlinear trends and seasonal variations. The LSTM model achieved
notably lower error metrics, with a MAPE of 2.42%, MAE of 215.35 GWh, and RMSE
of 329.9 GWh, emphasizing its strength in capturing complex temporal dependencies
that SARIMA could not manage effectively. Similarly, Haque and Rahman [24]
applied LSTM to both 30-minute and 24-hour-ahead forecasting tasks, comparing its
performance with SVR and ANN. While ANN and SVR provided reasonable accuracy,
the LSTM model consistently achieved the lowest MAPE and RMSE values across both
time horizons. These results highlight LSTM’s ability to learn from both short-term
fluctuations and long-term demand trends, making it particularly well-suited for
forecasting electricity consumption in dynamic and non-stationary environments.
Further demonstrating its potential, Memarzadeh and Keynia [30] proposed an
optimally tuned LSTM-based neural network specifically designed for short-term
forecasting of electricity load and price. By fine-tuning the architecture and
hyperparameters using real-world grid data, their model achieved high forecasting
accuracy across both daily and hourly intervals. This study reinforces LSTM's
adaptability and effectiveness in practical energy forecasting scenarios, especially
when precision is required for operational decisions.
Collectively, these studies affirm that LSTM models offer a powerful and flexible
approach to short-term load forecasting, capable of handling complex sequences and

| 34  |     |     | | Short-term load forecasting  |
| --- | --- | --- | ------------------------------ |

providing higher accuracy than conventional and many machine learning models that
is mentioned in Table 3.7.
Table 3.7: Strengths and limitations of RNNs and LSTMs in STLF.
| Model Type  |                          | Strengths        | Weaknesses                  |
| ----------- | ------------------------ | ---------------- | --------------------------- |
|             | Effective in modeling    |                  | Require large datasets to   |
|             | sequential and time-     |                  | generalize well,            |
|             |                          | dependent data,  | Computationally expensive,  |
|             | LSTM captures long-term  |                  | especially with long        |
dependencies using  sequences,
|     | memory and gates,  |     | Difficult to interpret and  |
| --- | ------------------ | --- | --------------------------- |
RNN
|     | Manages seasonality,         |                | debug due to complex             |
| --- | ---------------------------- | -------------- | -------------------------------- |
|     | trends, and lagged effects   |                | architecture,                    |
|     | in electricity demand,       |                |                                  |
|     | Performs well in multi-step  |                | Sensitive to hyperparameter      |
|     | forecasting and dynamic      |                | tuning (e.g., number of layers,  |
|     |                              | environments.  | hidden units).                   |
3.3.2.  Transformer-based models
Transformer-based models have recently gained traction in STLF due to their ability
to model complex temporal dependencies using self-attention mechanisms. Originally
developed for natural language processing tasks, transformers differ from traditional
recurrent architectures (like RNNs or LSTMs) in that they process input sequences in
parallel,  not  sequentially,  enabling  both  faster  training  and  better  long-range
dependency modeling.
At  the  core  of  the  transformer  architecture  is  the  scaled  dot-product  attention
mechanism, defined in Equation (3.14):
𝑄𝐾𝑇
|     | 𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 (𝑄,𝐾,𝑉) | = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥( | )𝑉  |
| --- | ----------------- | ---------- | --- |
(3.14)
√𝑑
𝑘
Where Q, K, and V are the query, key, and value matrices, 𝑑  is the dimensionality of
𝑘
the key vectors.
This mechanism allows the model to dynamically weigh the importance of different
time steps in the input sequence when making predictions, which is especially useful
in multivariate and irregular load datasets.

| Short-term load forecasting 35
Table 3.8: Strengths and Limitations of Transformer-Based Models in STLF.
Model Type Strengths Weaknesses
Captures long-term
Requires more data and
dependencies better than
computational power,
RNN/LSTM,
Model architecture and tuning
Highly parallelizable
are more complex,
during training,
Needs careful handling of
Transformer-Based Scales well to high- time positional encoding in
Models dimensional multivariate time series forecasting,
input, Still relatively new in power
systems forecasting — less
Provides interpretability
validated in practice,
via attention weights,
May overfit on small datasets
Performs well in multi-step
without regularization.
and missing data scenarios.
Transformer-based architectures have emerged as powerful tools for electricity load
forecasting due to their ability to model long-range temporal dependencies and handle
heterogeneous input features. Unlike traditional recurrent models, Transformers
leverage attention mechanisms to selectively focus on the most relevant parts of the
input sequence, making them particularly effective in time series forecasting tasks.
Ahmad et al. [34] proposed TFTformer, a specialized Transformer architecture tailored
for electricity load prediction. This model integrates temporal attention mechanisms
with feature selection strategies to model both static and dynamic covariates. Notable
components include variable selection networks that enhance input relevance, gated
residual networks (GRNs) that facilitate information flow, and multi-head attention
layers that capture temporal dependencies across multiple time scales. Their results
demonstrated that TFTformer significantly outperformed RNN-based architectures,
especially in multi-step forecasting scenarios and in datasets containing missing
values. This highlights the model’s robustness and adaptability in real-world
forecasting contexts.
Chan and Yeo [36] implemented a general Transformer architecture to forecast short-
term electricity demand. Their model made use of the self-attention mechanism to
identify key time steps in historical data, providing not only improved forecasting
accuracy but also enhanced interpretability. Compared to LSTM models, the
Transformer model achieved lower forecasting errors and revealed which historical
inputs contributed most to the predictions via attention scores. This transparency
allows for a deeper understanding of load dynamics and enhances confidence in the
forecasting outputs.

36 | Short-term load forecasting
Together, these studies demonstrate the growing importance of Transformer-based
architectures in energy forecasting. As mentioned in Table 3.8, by offering both high
accuracy and interpretability, these models address key limitations of traditional
methods and present a promising path forward for short-term load forecasting
applications.
3.4. Hybrid models
To address the increasing complexity of short-term electricity demand patterns—
affected by weather, human behavior, and distributed energy resources—many
researchers have developed hybrid and ensemble models. These approaches aim to
combine the strengths of different forecasting techniques to improve prediction
accuracy, reduce variance, and enhance generalization. Hybrid models are particularly
beneficial in STLF tasks, where they help address both linear and nonlinear
characteristics in data.
3.4.1. Statistical & ML hybrids
Hybrid models that combine statistical and machine learning techniques have gained
prominence in energy load forecasting due to their ability to capture both linear and
nonlinear patterns in time series data. By leveraging the strengths of different
methodologies, these models aim to improve forecasting accuracy and robustness.
Figure 3.5: Proposed model of GA-optimized SVR [26].

| Short-term load forecasting 37
Bendaoud et al. [23]proposed a hybrid model that integrates Exponential Smoothing
with GBRT for short-term electricity load forecasting. In this approach, Exponential
Smoothing is employed to model the linear and seasonal components of the load data,
effectively capturing the underlying trends and periodicities. Subsequently, GBRT is
applied to the residuals obtained from the smoothing process to model the nonlinear
relationships and correct any remaining errors. This two-stage modelling strategy
allows for a comprehensive representation of the load data, addressing both its linear
and nonlinear characteristics. The hybrid model demonstrated improved forecasting
accuracy, particularly for daily and weekend load predictions, outperforming models
that rely solely on either statistical or machine learning techniques.
Error! Reference source not found. illustrates hybrid forecasting model of Hasan et al.
[26] that combines SVR with a Genetic Algorithm (GA) to predict energy consumption
across four sectors: residential, commercial, industrial, and agricultural. SVR is a
powerful machine learning technique capable of modelling complex nonlinear
relationships in data. However, its performance is highly sensitive to the selection of
hyperparameters, such as the penalty parameter and kernel function parameters. To
address this, the authors employed a Genetic Algorithm to optimize the SVR
hyperparameters, enhancing the model's predictive accuracy. The GA iteratively
searches for the optimal combination of parameters by simulating the process of
natural selection, thus avoiding local minimum, and improving generalization. The
GA-optimized SVR model achieved higher forecasting accuracy compared to
traditional SVR and other baseline models, demonstrating its effectiveness in
capturing the complex dynamics of energy consumption across different sectors.
3.4.2. Ensemble tree-based methods
Ensemble-based models have gained considerable attention in the field of STLF for
their ability to enhance predictive accuracy, reduce overfitting, and improve model
generalization. By combining the outputs of multiple learners, ensemble methods
capitalize on the strengths of different models to create more stable and robust
forecasts, particularly under uncertain and volatile conditions.
Deng et al. [16] proposed a hybrid ensemble model that integrates Bagging with
XGBoost to address the challenges of forecasting electricity demand during extreme
weather events. Their model begins by identifying periods of extreme weather using
time, load, and meteorological features, ensuring that the training process is tailored
to critical high-variance conditions. To improve relevance and adaptability, the model
selects training data based on a weighted similarity measure, which emphasizes
historical cases most comparable to the current situation.
As Figure 3.6 illustrates, the hybrid approach employs Bagging to generate diverse
subsets of the selected training data. Each subset is used to train an independent
XGBoost learner, and the final forecast is obtained by aggregating their outputs—
typically through averaging. This combination allows the model to benefit from

38 | Short-term load forecasting
XGBoost’s ability to capture complex nonlinear relationships while leveraging
Bagging to reduce variance and improve generalization.
Results from the study showed that the Bagging–XGBoost model outperformed
conventional methods, especially in forecasting peak loads during extreme weather. It
achieved a notable reduction in MAPE, demonstrating its robustness in volatile
consumption environments.
This work highlights the effectiveness of ensemble learning in energy forecasting,
particularly in high-risk scenarios where accuracy and reliability are critical to
maintaining grid stability.
Figure 3.6: Framework of extreme weather identification and STLF [16].
3.4.3. Neural network-based hybrids
Hybrid neural network models have proven highly effective in the field of electricity
load forecasting due to their capacity to simultaneously capture localized
consumption patterns and long-range temporal dependencies. Among the most
widely used configurations are models that combine CNNs with LSTM networks.
These hybrids are particularly valuable in dealing with high-frequency, nonlinear, and
volatile energy data.

| Short-term load forecasting 39
CNNs are well-suited for identifying spatial and short-term features in structured
input data. Their layered design allows for efficient abstraction and preprocessing,
making them an ideal front-end in hybrid architectures. Bendaoud et al. [23] evaluated
CNN models for short-term load forecasting in Algeria and found that while CNNs
did not outperform all alternatives in isolation, they performed well when integrated
with other models. Specifically, CNNs demonstrated strong performance in feature
extraction, especially when embedded in hybrid systems, enhancing the performance
of downstream components such as LSTM networks.
Wang et al. [29] advanced this concept by proposing a hybrid model that integrates
CNNs with extended LSTM networks. In this architecture, CNNs first extract high-
level spatial and short-term temporal features, which are then processed by LSTM
layers to model sequential dependencies. Their study demonstrated that this hybrid
significantly improved forecast accuracy in complex load environments where both
short-term fluctuations and long-term consumption trends coexist.
Guo et al. [31] expanded on the CNN–LSTM hybrid by developing a multi-scale
framework that incorporates real-time electricity pricing into the forecasting process.
Their model captures features at different temporal resolutions using multiple CNN
layers, allowing for a more nuanced understanding of consumption dynamics. These
features are passed to LSTM layers to model temporal relationships, leading to higher
accuracy in both day-ahead and intraday forecasts.
Figure 3.7: A schematic diagram of a CNN-LSTM network based on a multi-modal
attention mechanism [32].

40 | Short-term load forecasting
A more advanced adaptation was presented in Figure 3.7 by Guo et al. [32], who
incorporated a multi-modal attention mechanism into the CNN–LSTM hybrid
structure. This model assigns attention weights to different feature representations
based on their relevance, improving the interpretability and responsiveness of the
forecasting model. The integration of attention further enhances performance by
allowing the model to focus on critical periods or signals during training.
In parallel, Memarzadeh and Keynia [30] developed an optimized LSTM-based neural
network specifically for forecasting electricity load and price. Their approach involved
rigorous hyperparameter tuning and structural optimization using real grid data.
While the model was not explicitly a hybrid in terms of architecture, it reflects the
importance of tailored LSTM configurations when deployed in realistic energy
forecasting scenarios. The model achieved high accuracy in both daily and hourly
forecasts, underscoring the practical viability of deep learning in operational planning.
Collectively, these studies confirm the effectiveness of neural network-based hybrid
models—especially CNN–LSTM combinations—in modelling the complex, multi-
scale characteristics of electricity consumption. By combining the feature abstraction
capabilities of CNNs with the memory strength of LSTMs, these models offer a
powerful approach for short-term load forecasting in modern smart grid
environments.
3.4.4. Intelligent and fuzzy logic hybrids
Liapis et al.[33] proposed a fuzzy-deep ensemble model specifically designed to
enhance short- and mid-term electric load forecasting. For the day ahead forecasting,
the model demonstrated particular strength in managing uncertainty and fluctuating
demand. By integrating fuzzy logic into the structure of a deep neural network, the
model could incorporate expert-like reasoning and linguistic rules to better interpret
ambiguous input conditions—such as weather fluctuations or demand variability—
common in daily forecasting tasks.
The fuzzy system managed input imprecision by translating real-world variables into
fuzzy sets and applying rule-based reasoning, while the deep neural network layers
captured complex nonlinear relationships from historical load data. This fusion
enabled the model to maintain accuracy while improving robustness and
interpretability. In the case of 1-day load prediction, the ensemble outperformed
traditional methods by effectively modeling sudden shifts and short-term demand
spikes, making it especially suitable for operational planning in smart grid
environments.
3.4.5. Transformer-based hybrids
Tian et al. [34] proposed a CNN–Transformer hybrid model tailored for day-ahead
probabilistic load forecasting, with a particular focus on weekends—periods often

| Short-term load forecasting 41
marked by irregular consumption behavior and limited historical data. The model
was designed to address the challenges of accurate prediction under these
constraints by leveraging both convolutional and attention-based sequence
modelling techniques.
Based on Figure 3.8, the architecture begins with a data preprocessing stage that
denoises and enhances the raw input using features such as peaks and trends. These
enriched one-dimensional time series are then processed through multiple CNN
layers, which are responsible for extracting localized temporal features. CNNs are
particularly effective in identifying short-term structures in load data, such as
consumption spikes or repetitive daily cycles.
Figure 3.8: Flow chart of the deep learning framework [34].
Once features are extracted, they are passed to a Transformer module, which applies
self-attention mechanisms to model long-range dependencies within the time series.
The Transformer’s ability to weigh the importance of different time steps allows it to
capture broader contextual relationships that traditional recurrent models might
overlook.
To produce probabilistic forecasts, the model incorporates quantile regression as its
loss function. This enables it to estimate not only point predictions but also confidence
intervals, which are essential for understanding forecast uncertainty. Additionally, a
novel loss penalty mechanism is introduced to prioritize weekend-specific accuracy,
ensuring the model pays greater attention to these more volatile periods.
Evaluation results showed that the model achieved high forecasting accuracy for all
48 time points in a day using only two weeks of historical data. This performance
highlights the effectiveness of combining CNNs and Transformers, especially in

42 | Short-term load forecasting
scenarios where data availability is limited. The hybrid approach offers a robust and
flexible solution for utilities seeking reliable short-term forecasts under uncertain or
sparse conditions.
Table 3.9: Benefits of Hybrid models in STLF.
authors Benefits Description
Combining Exponential
Smoothing with GBRT captures
Improved short-term prediction both linear trends and nonlinear
accuracy residual patterns, enhancing
Bendaoud daily and weekend forecasting
et al. [23] performance.
CNNs enhance LSTM
Effective feature extraction in performance by providing rich
hybrid models local and temporal features as
input for sequence modelling.
Genetic Algorithm optimizes
SVR hyperparameters, avoiding
Hasan et al.
Enhanced model generalization local minima and improving
[26]
accuracy across multiple energy
sectors.
Bagging–XGBoost hybrid
improves model stability by
Deng et al. Robustness in extreme weather
aggregating forecasts from
[16] conditions
multiple learners trained on
weather-specific subsets.
CNN layers extract short-term
features, while extended LSTM
Wang et al. Better handling of short- and
layers model sequential behavior
[29] long-term dependencies
for improved accuracy in
volatile environments.
Multi-scale CNN–LSTM hybrid
captures complex load-price
Guo et al. Improved accuracy under-prices
relationships across different
[31] dynamics
timescales for day-ahead and
intraday forecasting.
Multi-modal attention
Guo et al. Improved interpretability and
mechanism enhances CNN–
[32] feature relevance
LSTM hybrid by focusing on

| Short-term load forecasting 43
critical input features during
training.
LSTM architecture is fine-tuned
Memarzade
using real-world data,
h and Optimized forecasting accuracy improving model performance
Keynia [30] in hourly and daily load
prediction.
Fuzzy-deep ensemble integrates
Liapis et al. fuzzy rules into deep networks,
Effective handling of uncertainty
[33] improving reliability and
robustness in 1-day forecasts.
CNN–Transformer hybrid with
quantile loss and weekend-
Tian et al. Accurate forecasting with
specific penalties enables precise
[34] limited data
forecasts using only two weeks
of training data.
Table 3.9 presents a comparative overview of various hybrid forecasting models used
in STLF, emphasizing the specific advantages each model offers. The benefits range
from improved predictive accuracy and model generalization to enhanced robustness
under extreme conditions and better interpretability.
3.5. Summary
Chapter 3 offers a comprehensive examination of STLF, focusing on forecasting
electricity demand from minutes up to a week. Accurate STLF is essential for efficient
grid operation, economic dispatch, and demand response management. The chapter
categorizes forecasting models into four main groups: statistical methods, ML
methods, deep learning models, and hybrid/ensemble approaches.
Statistical models such as ARIMA and SARIMA provide interpretable forecasts under
stable seasonal conditions, but they struggle with nonlinearity and high-frequency
variability. Regression models like linear regression and quantile regression are
efficient and interpretable, though limited in complex or dynamic contexts.
ML models such as SVR, decision trees, random forests, and XGBoost outperform
traditional methods by capturing nonlinear relationships. SVR, in particular, balances
accuracy with computational efficiency, while tree-based methods provide strong
generalization and interpretability.
Deep learning methods—especially LSTM and ANN—excel in modeling temporal
dependencies. LSTM outperforms statistical and shallow models by capturing long-

44 | Short-term load forecasting
and short-term dynamics. ANN models are simpler and effective but prone to
overfitting and require tuning.
Hybrid models integrate multiple methods to enhance accuracy and robustness.
Examples include exponential smoothing + GBRT, SVR + GA, CNN + LSTM, and CNN
+ Transformer. These combinations address both linear and nonlinear data
characteristics, improve model generalization, and handle uncertainty, volatility, and
limited data effectively.
The chapter emphasizes that hybrid and deep learning models are increasingly vital
for modern STLF, especially in smart grid environments where interpretability,
scalability, and resilience to variability are crucial.

| Medium-term load forecasting 45
4
Medium-term load forecasting
MTLF refers to the prediction of electricity demand over a horizon ranging from one
week to one month. This forecasting range serves as a bridge between short-term
operational planning and long-term investment strategies. MTLF is essential for
applications such as energy procurement, maintenance scheduling, capacity planning,
tariff design, and policy development.
Unlike short-term forecasting, which deals with rapid fluctuations in demand,
medium-term forecasting must address broader seasonal trends, monthly usage
patterns, and external influences such as climate variation, economic activity, and
consumer behavior [17], [35], [36]. The data used is typically aggregated at weekly or
monthly levels, which introduces different modeling challenges, including data
sparsity, reduced temporal resolution, and delayed response to exogenous variables.
MTLF models must also account for nonlinear and nonstationary behaviors over
longer horizons while maintaining reasonable interpretability and computational
efficiency. Furthermore, many modern applications demand that forecasts incorporate
uncertainty estimation and adapt to evolving energy usage conditions, particularly in
grids with high penetration of renewable energy and flexible loads [25], [37], [38].
This chapter reviews prominent MTLF methodologies across four main categories:
statistical models, machine learning techniques, deep learning architectures, and
hybrid or ensemble approaches. The aim is to identify the most effective techniques
for medium-range horizons and understand how these methods address the unique
challenges of MTLF across residential, commercial, and distribution system levels.
4.1. Statistical methods
Statistical methods have traditionally served as the foundation for MTLF due to their
mathematical simplicity, interpretability, and low computational requirements. These
models are particularly effective when applied to aggregated consumption data—such
as weekly or monthly electricity use—where periodicity and seasonality can be
exploited for accurate prediction [39], [40].
Unlike short-term forecasting, which often relies on high-frequency input variables
like real-time weather or occupancy data, MTLF emphasizes broader consumption
patterns over longer horizons. As a result, statistical models in this context focus on

46 | Medium-term load forecasting
uncovering trend structures, autocorrelation, and cyclical patterns in the data.
Methods such as linear regression, ARIMA, SARIMA, and quantile regression are
frequently employed to model deterministic and probabilistic aspects of medium-term
electricity demand.
Recent studies have also explored hybrid extensions of classical models, incorporating
decomposition (e.g., Fourier transforms) or probabilistic components (e.g., kernel
density estimation) to improve their adaptability to complex demand dynamics. While
these approaches may lack the flexibility of modern machine learning techniques, they
offer transparent forecasting logic, which remains essential for operational decision-
making in power systems and utility planning [40].
The following subsections review key statistical methods applied to medium-term
electricity forecasting, along with selected case studies demonstrating their
performance, strengths, and limitations.
4.1.1. Regression-based methods
Regression-based models are among the most frequently used techniques in MTLF
due to their simplicity, interpretability, and efficiency when working with aggregated
data such as monthly or weekly electricity consumption. These models rely on
identifying statistical relationships between the target variable (typically electricity
demand) and independent features like historical load, temperature averages, or
calendar-based indicators.
LR models assume a constant, additive relationship between predictors and the target.
This makes them ideal for applications requiring transparent forecasting logic, such as
tariff planning and capacity estimation. They are particularly effective for stable
consumption environments with identifiable seasonal trends.
To improve the accuracy and reliability of medium-term load forecasting, particularly
under uncertainty, researchers have increasingly turned to quantile regression (QR).
Unlike traditional regression methods that estimate the Mean of a response variable,
QR allows forecasting of conditional quantiles (e.g., Median, 90th percentile), which
provides a more nuanced view of the possible outcomes and better captures variability
in electricity demand.
The quantile regression objective is to minimize the quantile loss function, defined in
Equation (4.1):
𝑁
min∑𝜌 𝑦 −𝑥⊤𝛽, (4.1)
𝜏 𝑖 𝑖
𝛽
𝑖=1
Where 𝜌 (𝑢) = 𝑢(𝜏−𝕀 ) is the asymmetric quantile loss function, 𝜏 ∈ (0,1) denotes
𝜏 {𝑢<0}
the desired quantile (e.g., 𝜏 = 0.5 for the median), 𝑦 is the actual observation, 𝑥⊤𝛽 is
𝑖 𝑖
the predicted value.

| Medium-term load forecasting 47
This formulation penalizes over- and under-predictions differently depending on the
quantile level, enabling forecasters to model both central tendencies and tail risks in
electricity demand.
Wang et al. [40] developed a combined probabilistic forecasting model that integrates
quantile regression with kernel density estimation. Their model aimed to forecast peak
and base load scenarios by estimating a full distribution rather than a single-point
value. The approach enabled them to reflect the uncertainty inherent in electricity
demand and capture asymmetric behaviors—such as occasional demand spikes—
which linear models typically fail to account for. The use of kernel methods further
enhanced the flexibility of their distribution modeling, making it especially suitable
for medium-term planning where long-range uncertainty is a significant factor.
Xu [41] provided a comprehensive review of quantile regression applications in both
renewable energy generation and building load forecasting. The review emphasized
QR’s ability to model a range of possible demand outcomes, rather than relying solely
on expected values. Xu noted that QR is particularly beneficial in situations involving
intermittent renewable inputs or unpredictable user behavior—common challenges in
medium-term horizons. The method supports probabilistic forecasting, where
forecasting ranges are more informative than single-value predictions and are essential
for grid operators managing risk and planning reserve margins.
In summary, as highlighted in Table 4.1, QR has emerged as a vital tool in medium-
term load forecasting by offering interpretable distributional insights into energy
demand. It improves robustness under uncertainty and is particularly advantageous
in dynamic systems influenced by renewable energy, fluctuating occupancy patterns,
or seasonal effects.
Table 4.1: Strengths and limitations of regression methods in MTLF.
Model Type Strengths Weaknesses
Simple; interpretable; fast
Limited to linear patterns;
Linear Regression
to compute; effective for underperforms in dynamic or
(LR)
aggregated data. nonlinear contexts.
Captures variability and
More complex; harder to
Quantile uncertainty; robust to
interpret compared to mean-
Regression (QR) outliers; supports
based methods.
probabilistic forecasting.

48 | Medium-term load forecasting
4.1.2. ARIMA and SARIMA
These models are particularly effective in MTLF due to their ability to capture trend,
seasonality, and autocorrelation in aggregated data such as weekly or monthly
electricity consumption.
Several studies have explored the application and enhancement of statistical models
such as ARIMA and SARIMA for medium-term load forecasting. Bilgili and Pinar [17]
employed a SARIMA model to forecast monthly gross electricity consumption in
Turkey, demonstrating the model’s effectiveness in capturing long-term patterns and
consistent seasonal cycles within national electricity profiles. Their results confirmed
that while deep learning models like LSTM slightly outperformed SARIMA in
handling non-linearities, SARIMA stood out for its model stability, computational
simplicity, and robustness when the data adhered to regular seasonal trends. These
characteristics make SARIMA a reliable option for institutional forecasting tasks where
interpretability and efficiency are critical.
In the domain of residential energy forecasting, Gellert et al. [22] applied both ARIMA
and TBATS models to smart home electricity datasets. Their comparative evaluation
revealed that ARIMA maintained solid performance under structured and regular
seasonal conditions. However, the study also identified its limitations when dealing
with complex seasonality and higher-frequency volatility, suggesting that more
adaptive models like TBATS, which support multiple seasonalities and complex
temporal dynamics, may be better suited for more irregular patterns often found in
smart environments.
An innovative development was presented by Karamolegkos and Koulouriotis [39],
who introduced a Fourier-enhanced ARIMA model. Though originally designed for
short-term forecasting in the Greek electricity market, the model integrated seasonal
decomposition using Fourier series to isolate dominant frequency components. This
technique enhances the model’s ability to detect and forecast cyclical consumption
patterns, making it highly adaptable for medium-term horizons as well. The approach
allows for better alignment between statistical model structures and the periodic
behaviors of electricity demand, especially in contexts where multiple seasonal
influences coexist.
Additionally, Wang et al. [35] proposed a forecasting model based on accumulative
time-delay effects and periodic fluctuation components. Although this model is not a
conventional ARIMA-type model, it shares key structural principles such as time-
series decomposition and explicit modeling of deterministic and stochastic elements.
The model was validated using monthly electricity consumption data, illustrating its
suitability for MTLF tasks. It demonstrated particular strength in capturing recurring
cycles and long-term behavioral trends, contributing to more accurate and
interpretable forecasts.

| Medium-term load forecasting 49
Together, these studies demonstrate that while traditional ARIMA-based models
provide a robust foundation for medium-term load forecasting (MTLF)—particularly
when the data exhibits stable and consistent seasonality—advanced adaptations such
as Fourier-enhanced ARIMA and models incorporating hybrid periodic structures
significantly improve forecasting performance in more complex, dynamic scenarios,
as summarized in Table 4.2.
Table 4.2: Strengths and limitations of ARIMA and SARIMA in MTLF.
Model Type Strengths Weaknesses
Suitable for stationary or
Assumes linearity and lacks
near-stationary monthly
adaptability to nonlinear
ARIMA data; interpretable with patterns; limited performance
transparent parameter with irregular long-term
trends.
structure.
Strong at modelling regular
Struggles with multiple or
monthly or seasonal cycles;
shifting seasonalities; sensitive
SARIMA robust in national or utility-
to season length and requires
scale MTLF with stable
precise parameterization.
patterns.
Effectively models multi-
Increases model complexity;
period cycles using
requires accurate frequency
Fourier-ARIMA harmonic decomposition;
selection and decomposition
enhances ARIMA flexibility
expertise.
for MTLF.
4.2. ML models
ML techniques have emerged as powerful alternatives to traditional statistical
approaches in electricity load forecasting. These models are particularly effective at
capturing complex, nonlinear patterns in historical consumption data and can adapt
to dynamic changes in usage behavior. ML models do not require strong assumptions
about the underlying data distribution, making them suitable for diverse forecasting
horizons and load profiles.
Recent studies have shown that ML models can outperform classical models in both
accuracy and generalizability, especially when sufficient historical and contextual data
are available. Commonly used machine learning methods in load forecasting include
SVR, decision tree-based algorithms, k-NN, and ANN, each offering specific
advantages in terms of interpretability, scalability, and performance under different
forecasting conditions.

50 | Medium-term load forecasting
4.2.1. Tree-based models
Tree-based models are highly effective for MTLF due to their ability to manage
complex, nonlinear relationships between features and the target variable. These
models are capable of automatically capturing interactions between features without
requiring extensive preprocessing, making them particularly useful for forecasting
electricity consumption, which can exhibit both seasonal and irregular patterns. The
most commonly used tree-based algorithms in load forecasting are Decision Trees,
Random Forests, and GBMs, including XGBoost and LightGBM.
4.2.1.1. Decision trees
Decision Trees are a fundamental tree-based model that recursively splits the feature
space into regions that are as homogeneous as possible in terms of the target variable.
This method is intuitive and easy to interpret, making it valuable for practical
applications in MTLF. While Decision Trees can suffer from overfitting, they provide
a clear visualization of how the model arrives at its predictions. They are particularly
useful for capturing simple patterns in the data and can serve as the foundation for
more complex models like Random Forests and Gradient Boosting.
4.2.1.2. Random forests
RF are an ensemble method that builds multiple decision trees using random subsets
of the data and aggregates their predictions. This approach reduces the risk of
overfitting associated with a single Decision Tree and improves model generalization.
Random Forests are highly effective at handling high-dimensional data and can
capture complex interactions among features. For medium-term load forecasting, RF
models can effectively model seasonal variations and nonlinear trends in electricity
consumption. Their robustness and simplicity make them a popular choice for load
forecasting.
4.2.1.3. XGBoost
XGBoost is an optimized implementation of GBMs that incorporates techniques such
as regularization to reduce overfitting and improve model accuracy. It has become one
of the most popular tree-based algorithms for forecasting tasks due to its ability to
manage large datasets with high computational efficiency. In the context of MTLF,
XGBoost has demonstrated strong performance in predicting future load values by
effectively capturing both short-term fluctuations and longer-term trends in electricity
usage.

| Medium-term load forecasting 51
4.2.1.4. GBMs
As Error! Reference source not found. illustrates, GBMs are an ensemble learning t
echnique that builds a series of decision trees in a sequential manner. At each step, a
new tree is fitted to the residual errors (the gradients) of the existing model. The
primary idea is to reduce the prediction error by adding trees that correct the mistakes
made by previous trees. Mathematically, the process can be described as follows:
Figure 4.1: Architecture of XGBoost model [36].
1. Initialization: The process begins with an initial model 𝐹 (𝑥) that makes an
0
initial prediction based on the training data. This could be as simple as
predicting the mean of the target variable y as it is shown in Equation (4.2):
𝑁
1
𝐹 (𝑥) = ∑𝑦 , (4.2)
0 𝑁 𝑖
𝑖=1
Where 𝐹 (𝑥) is the initial model prediction, 𝑁 is the number of training samples,
0
𝑦 is the true value of the sample.
𝑖
2. Gradient Calculation: At each iteration m, a new tree ℎ (𝑥) is built to predict
𝑚
the negative gradient (residuals) of the loss function L with respect to the
current prediction 𝐹 (𝑥) based on Equation (4.3):
𝑚−1
𝜕𝐿(𝑦 𝐹 (𝑥 ))
(𝑚) 𝑖 𝑚−1 𝑖
𝑟 = − , (4.3)
𝑖 𝜕𝐹 (𝑥 )
𝑚−1 𝑖
(𝑚)
Where 𝑟 is the residual for the 𝑖 sample at the 𝑚 iteration. 𝐿(𝑦 𝐹 (𝑥 ))
𝑖 𝑡ℎ 𝑡ℎ 𝑖 𝑚−1 𝑖
is the loss function (e.g., mean squared error or log-loss).
3. Model Update: based on Equation (4.4) The new tree ℎ (𝑥) is added to the
𝑚
previous model 𝐹 (𝑥) , and the model is updated by adding a scaled version
𝑚−1
of ℎ (𝑥) with a learning rate η:
𝑚

52  | Medium-term load forecasting

|     | 𝐹 (𝑥) | = 𝐹 (𝑥)+𝜂.ℎ | (𝑥),  |     | (4.4)  |
| --- | ----- | ----------- | ----- | --- | ------ |
|     | 𝑚     | 𝑚−1         | 𝑚     |     |        |
Where 𝐹 (𝑥) is the updated model after the 𝑚  tree is added, ℎ (𝑥) is the new
| 𝑚   |     |     | 𝑡ℎ  | 𝑚   |     |
| --- | --- | --- | --- | --- | --- |
tree fitted to the residuals, 𝜂 is the learning rate, which controls the contribution
of each new tree to the final prediction.
4.  Final Model: After M trees are added, the final model is given by Equation (4.5):
𝑀
|     | 𝐹 (𝑥) = | 𝐹 (𝑥)+ | ∑ 𝜂.ℎ (𝑥),  |     | (4.5)  |
| --- | ------- | ------ | ----------- | --- | ------ |
|     | 𝑀       | 0      | 𝑚           |     |        |
𝑚=1
This process allows GBMs to iteratively reduce the residual error, thus improving
prediction accuracy over multiple iterations.
4.2.1.5.  LightGBM
LightGBM is an optimized version of GBMs that improves computational efficiency
and scalability, particularly for large datasets. It achieves this by using a histogram-
based method for finding optimal splits, as well as other optimizations. LightGBM
introduces  several  innovations,  including  leaf-wise  tree  growth  and  discretizing
continuous features into bins, which leads to faster training and reduced memory
usage. Here is how the method works:
1.
Discretization  of  Features:  LightGBM  discretizes  continuous  features  into
discrete bins. Based on Equation (4.6), given a feature x, it divides its range into
B bins (for example, [𝑥 ,𝑥 ,𝑥 ,⋯,𝑥 ]). This reduces the number of distinct
|     | 1 2 | 3 𝐵 |     |     |     |
| --- | --- | --- | --- | --- | --- |
feature values considered during split selection, leading to faster computation.
|     |     | 𝑥 ∈ {𝑏 ,𝑏 | ,𝑏 ,⋯,𝑏 },  |     | (4.6)  |
| --- | --- | --------- | ----------- | --- | ------ |
|     |     | 𝑖 1 2     | 3 𝐵         |     |        |
Where 𝑏 ,𝑏 ,𝑏 ,⋯,𝑏  are the bins that the feature values are discretized into.
| 1 2 3 | 𝐵   |     |     |     |     |
| ----- | --- | --- | --- | --- | --- |
2.  Leaf-wise Tree Growth: Unlike traditional GBMs that use level-wise growth
(splitting all nodes at the same level), LightGBM grows trees leaf-wise, where it
splits the leaf with the highest residual sum of squares (RSS) based on Equation
(4.7).  This  often  results  in  deeper  trees  but  improves  model  accuracy  by
capturing more complex patterns. The tree is grown as follows:
2
(𝑚)
|     |     | 𝑅𝑆𝑆 = ∑(𝑟 | ) ,  |     |        |
| --- | --- | --------- | ---- | --- | ------ |
|     |     | 𝑙         | 𝑖    |     | (4.7)  |
𝑖∈𝑙
(𝑚)
Where 𝑅𝑆𝑆  is the residual sum of squares for leaf l, 𝑟  is the residual error for
𝑙 𝑖
| the 𝑖  sample at the 𝑚 |  iteration.  |     |     |     |     |
| ---------------------- | ------------ | --- | --- | --- | --- |
| 𝑡ℎ                     | 𝑡ℎ           |     |     |     |     |

| Medium-term load forecasting  53

3.  Gradient Calculation and Tree Fitting: Similar to traditional GBM, LightGBM
fits a tree to the residuals. However, LightGBM optimizes the process by using
histograms of the residuals to approximate the best possible splits for each
feature. The negative gradient for a given leaf is shown in Equation (4.8):
|     | 𝜕𝐿(𝑦 𝐹 | (𝑥 )) |        |
| --- | ------ | ----- | ------ |
| (𝑚) | 𝑖      | 𝑚−1 𝑖 |        |
| 𝑟 = | −      | ,     | (4.8)  |
| 𝑖   | 𝜕𝐹     | (𝑥 )  |        |
|     | 𝑚−1    | 𝑖     |        |
4.  Model Update: The model is updated in the same manner as GBMs, but as it is
seen  in  Equation  (4.9)  the  updates  are  faster  due  to  the  histogram-based
approach and the leaf-wise tree growth:
| 𝐹 (𝑥) | = 𝐹 (𝑥)+𝜂.ℎ | (𝑥),  | (4.9)  |
| ----- | ----------- | ----- | ------ |
| 𝑚     | 𝑚−1         | 𝑚     |        |
5.  Final Model: After M trees are added, the final model in LightGBM is defined
by Equation (4.10):
𝑀
| 𝐹 (𝑥) = | 𝐹 (𝑥)+ | ∑ 𝜂.ℎ (𝑥),  | (4.10)  |
| ------- | ------ | ----------- | ------- |
| 𝑀       | 0      | 𝑚           |         |
𝑚=1
Tree-based models have demonstrated strong performance in MTLF, particularly due
to their ability to capture nonlinear dependencies, incorporate external factors, and
scale well with large datasets. Zhu et al. [42] applied a decision tree-based approach to
forecast electricity consumption in smart grids. Using data that included both seasonal
and non-seasonal patterns, the model successfully captured key demand dynamics
with  high  interpretability.  While  the  study  did  not  report  significant  gains  over
ensemble models, it emphasized the model’s clarity and practical deployment in
operational smart grid settings.
In contrast, Mathew et al. [36] developed the Prominence-guided Weighted Peaks
(PWP) XGBoost model to improve the accuracy of feeder-level peak load forecasting.
The model was trained on feeder-level electricity data supplemented with external
variables  such  as  weather  and  economic  indicators.  Compared  to  conventional
methods, the PWP-XGBoost achieved lower forecasting errors, particularly in peak
demand estimation—an essential factor for maintaining grid stability. The inclusion of
domain-specific knowledge into the XGBoost framework contributed to improved
precision in capturing complex medium-term load fluctuations.
Similarly, Royal et al. [43] applied the Light Gradient Boosting Machine (LightGBM)
model to medium-term electricity load forecasting tasks. The model was trained on
time-series datasets characterized by strong temporal dependencies and nonlinear
behaviors. LightGBM outperformed traditional statistical models, achieving lower
error metrics and demonstrating high computational efficiency due to its histogram-

54 | Medium-term load forecasting
based learning and feature bundling techniques. These attributes made it particularly
effective in forecasting medium-term load trends across diverse operational
conditions.
Additionally, Dinmohammadi et al. [44] conducted a comparative study of Random
Forest (RF) and Gradient Boosting (GB) models for medium-term load forecasting. The
study evaluated performance across multiple regions and timescales and found that
RF delivered more stable and consistent accuracy across diverse conditions, while GB
models showed slightly better performance in capturing complex patterns when
properly tuned. Both models outperformed linear baselines, especially when
hyperparameters were optimized. Notably, the authors emphasized the importance of
hyperparameter tuning and cross-regional evaluation for generalization. This study
further validated that ensemble-based tree methods, particularly when enhanced
through tuning and regional adaptation, provide a strong foundation for scalable and
accurate MTLF.
Together, these studies highlight the strength of decision tree-based methods—
particularly advanced ensembles like XGBoost and LightGBM—in improving
forecasting accuracy and interpretability across medium-term electricity consumption
horizons, as summarized in Table 4.3.
Table 4.3: Advantages and disadvantages of Tree-based models in MTLF.
Model Type Strengths Weaknesses
Simple and interpretable; Prone to overfitting without
pruning; May struggle with
Can model seasonal and
capturing subtle temporal
structural patterns in
Decision Trees dependencies across longer
medium-term consumption
horizons; Limited
data; Quick to train on
generalization, often
smaller regional datasets.
outperformed by ensembles.
Reduces overfitting by
averaging multiple trees;
Slower to predict as horizon
Performs well across
and data volume increase;
diverse urban datasets with Less interpretable; Requires
Random Forest
multiple influencing factors careful handling of temporal
(e.g., weather, economy); features for accurate long-
horizon forecasts.
Robust to noise in medium-
term historical data.
Handles complex temporal
Parameter tuning is critical to
patterns (e.g., seasonality prevent overfitting on
XGBoost
and cyclical effects) medium-range cycles;
effectively; Performs well Interpretation is more

| Medium-term load forecasting 55
on high-dimensional challenging; May require
medium-term datasets; preprocessing of time-based
features.
Excellent for capturing
interactions across multiple
time-lagged inputs.
Scalable and memory-
efficient—well-suited for
May overfit if trees are too
large regional datasets;
deep or not regularized;
Captures nonlinear and
Performance can degrade on
LightGBM temporal trends over datasets with irregular or
months; Native handling of sparse medium-term
structure; Requires careful
categorical variables is
feature engineering.
useful for calendar-based
MTLF features.
4.2.2. k-NN
k-NN is a simple and intuitive machine learning algorithm used for both classification
and regression tasks. In the context of MTLF, k-NN plays a significant role due to its
ability to predict future electricity consumption by identifying similar past patterns in
the data. The strength of k-NN lies in its non-parametric nature, meaning that it does
not make any assumptions about the underlying distribution of the data. Instead, it
learns directly from the data, which makes it adaptable to complex and nonlinear
patterns in electricity demand.
In MTLF, k-NN is typically used to forecast future load values based on historical data.
The forecasting horizon for medium-term load forecasting generally spans from a few
days to several weeks, making it crucial to capture long-term seasonal trends and
short-term fluctuations in electricity consumption. The key benefit of k-NN is its ability
to model temporal relationships by considering similar past patterns when making
predictions.

56 | Medium-term load forecasting
In the realm of medium-term load forecasting, several studies have successfully
applied k-NN, demonstrating its effectiveness in predicting electricity consumption.
As Figure 4.2 illustrates, Dong et al. [45] used k-NN combined with NSGA-II (Non-
dominated Sorting Genetic Algorithm) for optimizing the number of neighbors (k)
used in the model. This hybrid model was assessed using electricity consumption data
from an urban grid and showed a significant improvement in forecasting accuracy
over traditional methods such as ARIMA and SVM. The optimization process, through
NSGA-II, also reduced the computational burden while maintaining high accuracy,
particularly in capturing the seasonal fluctuations in load demand over a medium-
term horizon.
Figure 4.2: Framework of the proposed interval forecasting model and principles of
NSGA-II, KNN, DBN and modified KDE [45].
Similarly, Khan et al. [46] explored the application of k-NN combined with Deep Belief
Networks (DBN) for medium-term load forecasting in smart grids. In this study, k-NN
was used to extract relevant features from the historical electricity consumption data,
which were then used as inputs for the DBN model. The results demonstrated that this
hybrid approach significantly outperformed traditional models like ANN and SVR,
especially when dealing with the nonlinear patterns and demand fluctuations due to
external factors such as temperature and economic activity. The study also highlighted
that k-NN's role in feature selection played a critical part in improving the
performance and scalability of the DBN model.
In their study, Dudek & Pełka [47] focus on the application of Pattern Similarity-Based
Machine Learning Methods (PSFMs) for MTLF. Specifically, they investigate the
effectiveness k-NN within this framework for forecasting monthly electricity
consumption. By leveraging historical load data, the authors demonstrate how k-NN
can identify similar past consumption patterns and use them to predict future demand.
Their results show that k-NN, despite its simplicity, outperforms traditional models
such as ARIMA and SVR in capturing the seasonal variations and nonlinear patterns
inherent in electricity consumption. The study highlights that k-NN offers both
computational efficiency and forecasting accuracy, especially when combined with

| Medium-term load forecasting 57
other techniques in a hybrid model, making it a valuable tool for medium-term
forecasting tasks.
k-NN continues to be a valuable method for medium-term load forecasting. Its
simplicity and non-parametric nature make it adaptable to a variety of datasets,
especially when combined with optimization and deep learning techniques. The
studies reviewed demonstrate that k-NN, when used alone or in hybrid models, can
improve forecasting accuracy, reduce computational complexity, and capture the
essential seasonal patterns in electricity demand. A summary of the advantages and
disadvantages of k-NN in medium-term load forecasting can be found in Table 4.4.
Table 4.4: Advantages and disadvantages of K-NN in MTLF.
Model Type Strengths Weaknesses
Simple and intuitive
Computationally expensive
method, easy to implement
during prediction because it
and interpret; non-
requires calculating distances
parametric: Does not make
to all training samples;
assumptions about the sensitive to the curse of
underlying data dimensionality: performance
distribution; works well can degrade with a high
number of features; sensitive
with complex, nonlinear
to noisy data: outliers can
relationships between
heavily influence predictions;
features; Adaptable to
choice of k is crucial: the
dynamic patterns; can
performance heavily depends
K-NN easily incorporate new data on selecting the right number
without retraining; can of neighbours; memory-
intensive: requires storing
model seasonality and
large datasets, which may be
trends by considering
impractical for large datasets
historical data similarity;
over long time periods; does
good for capturing local
not work well with
patterns in electricity imbalanced datasets where
consumption; effective certain patterns dominate;
when combined with other slow inference time: Requires
comparing each test sample to
models (e.g., hybrid models
all training samples, which
with optimization
can be slow for large datasets.
techniques).

58 | Medium-term load forecasting
4.2.3. ANN
ANNs are particularly effective in forecasting electricity consumption, which is
influenced by complex patterns such as seasonality, weather variability, day-of-week
effects, and economic activity. Their ability to model nonlinear relationships and learn
from both historical data and external features allows ANNs to capture temporal
patterns (daily, weekly, and seasonal cycles) as well as long-term consumption trends.
As such, they are widely used in energy management, grid optimization, and
electricity demand forecasting.
Khan et al. [46] investigated a hybrid model that combines ANNs with DBN for
medium-term load forecasting in smart grid environments. The primary aim was to
enhance ANN performance through DBN-based feature extraction and optimization.
The model was trained using a comprehensive dataset that included not only historical
load profiles but also external parameters such as temperature and economic
indicators. Results showed that the ANN-DBN hybrid model significantly
outperformed standalone ANN and SVR models. Specifically, the ANN-DBN model
achieved a MAPE of 2.83%, compared to 3.54% for SVR and 3.11% for the conventional
ANN, demonstrating the efficacy of deep learning integration in capturing complex
nonlinear dependencies and improving forecast accuracy.
Wazirali et al. [48] focused on medium-term load forecasting for microgrids using a
standalone ANN model. The study utilized historical electricity consumption data
along with seasonal indicators to train the network for predicting demand over a one-
month horizon. The authors highlighted the ANN’s ability to model nonlinear
dependencies and capture cyclical patterns influenced by weather and calendar
effects. When benchmarked against traditional statistical methods like ARIMA, the
ANN model exhibited superior performance, achieving a MAPE of 3.76%, compared
to 5.21% for ARIMA. This confirmed that ANNs provide a more flexible and accurate
framework for modeling dynamic load behavior, especially in distributed energy
systems.
Ghiassi et al. [49] introduced a Dynamic Artificial Neural Network (DAN2)
architecture specifically designed for medium-term load forecasting in the context of
U.S. electricity utilities. Unlike conventional static feedforward networks, the DAN2
model dynamically determines its structure during training based on data behavior,
allowing it to adapt more effectively to nonlinear demand variations. The model was
evaluated using real-world system load data from the California Independent System
Operator (CAISO), forecasting load over a 30-day horizon. The DAN2 model was
benchmarked against standard ANN and ARIMA models using several metrics,
including RMSE and MAE. Results showed that DAN2 reduced RMSE by 11.3%
compared to static ANN and by 17.8% compared to ARIMA. These results
demonstrate that dynamically evolving ANN architecture can better manage complex

| Medium-term load forecasting 59
temporal dependencies in electricity load forecasting, especially when trends and
patterns shift over time.
Yalcinoz and Eminoglu [50] examined both short-term and medium-term electricity
load forecasting using feedforward MLP neural networks trained on real distribution
system data from Turkey. For the medium-term case, they focused on weekly forecasts
over a one-month horizon, integrating inputs such as temperature, humidity, and
historical load. Multiple ANN configurations were evaluated based on the number of
hidden layers, activation functions, and learning algorithms. Their best-performing
model achieved a MAPE of 2.38%, MAE of 12.1 MW, and RMSE of 17.5 MW for the
medium-term forecast. These results confirmed that ANNs provided significantly
better performance than linear regression models, which had a MAPE exceeding 4.6%
under the same conditions. The study also highlighted that incorporating weather data
as external inputs and optimizing the neural architecture were critical in enhancing
prediction accuracy and robustness.
Both early and recent studies demonstrate the successful application of ANNs in
medium-term load forecasting. While Wazirali et al. [48] emphasized the ANN's
strength in modeling seasonal and nonlinear variations in microgrid environments,
Khan et al. [46] demonstrated that coupling ANNs with deep learning techniques like
DBN significantly enhances feature learning and forecasting accuracy. Similarly,
Ghiassi et al. [49] showcased the benefits of dynamic network structures that evolve
during training, allowing ANNs to better adapt to shifting demand patterns. Yalcinoz
and Eminoglu [50] highlighted the effectiveness of carefully configured feedforward
networks in achieving high accuracy with limited data. Despite these advances, all
approaches point to common challenges, including the requirement for large and
diverse training datasets, computational cost, and the need for careful tuning of model
parameters to prevent overfitting and ensure generalizability.
A summary of the advantages and disadvantages of using ANNs for medium-term
load forecasting is provided in Table 4.5.

60 | Medium-term load forecasting
Table 4.5: Advantages and disadvantages of ANN in MTLF.
Model Type Strengths Weaknesses
Can model complex
nonlinear relationships
between features and target
variables; flexible Requires large amounts of
data to train effectively and
architecture allows
generalize well; training can
adaptation to various
be computationally expensive,
forecasting problems; high
especially for deep networks;
accuracy in forecasting due
overfitting can occur if the
ANN to its ability to capture model is not regularized
intricate patterns in data; properly; requires careful
tuning of hyperparameters
works well with high-
(e.g., learning rate, number of
dimensional data, and can
layers); less interpretable than
leverage multiple input
simpler models like decision
features; can handle
trees or random forests.
missing data and noisy
data through robust
learning algorithms.
4.3. Deep learning models
Deep learning models have gained significant attention in the field of MTLF due to
their ability to model complex, high-dimensional relationships in data, making them
well-suited for predicting electricity demand over medium-term horizons. Unlike
traditional machine learning models, deep learning models consist of multiple layers
of neural networks, which enable them to learn abstract features from raw data
without the need for explicit feature engineering.
In MTLF, deep learning models are especially effective for capturing both temporal
dependencies (e.g., daily, weekly, and seasonal fluctuations) and nonlinear
relationships between various influencing factors, such as weather conditions,
historical load data, and economic activity.
4.3.1. RNN
RNNs, particularly their advanced variant known as LSTM networks, have gained
prominence in the domain of time series forecasting due to their inherent ability to
model temporal dependencies. Unlike traditional statistical approaches, which often
rely on assumptions of stationarity and linearity, RNNs are capable of capturing both

| Medium-term load forecasting 61
short- and long-term patterns in dynamic, nonlinear datasets, making them highly
suitable for MTLF.
Muzaffar and Afshari [51] investigated the effectiveness of LSTM networks for
electrical load forecasting by using hourly data spanning 13 months. Their study
included not only the load time series but also exogenous environmental variables
such as temperature. Recognizing the importance of seasonality and trend
components in energy consumption, the authors implemented a rigorous
preprocessing framework. This included normalization, handling of missing values
and outliers, and decomposition of the time series to isolate daily, weekly, and yearly
seasonalities. Notably, while traditional methods required fully stationarized inputs,
the LSTM network only necessitated the removal of yearly seasonality to prevent
misinterpretation of one-year trends as ongoing patterns.
The LSTM network was trained on 12 months of data and validated using the 13th
month. The network architecture comprised 60 hidden units, employed the Adam
optimizer with a learning rate of 0.005, and was trained over 400 epochs. To enable
temporal learning, input sequences were constructed using a lag of five-time steps.
This design allowed the model to forecast future values based on dependencies
observed in preceding data points.
Forecasts were generated for several horizons—24 hours, 48 hours, 7 days, and 30
days—and evaluated using RMSE and MAPE. Results showed that the LSTM model
significantly outperformed classical statistical models such as ARMA, SARIMA, and
ARMAX in short-term and intermediate horizons. For instance, LSTM achieved a
MAPE of 1.52% for a 24-hour forecast, compared to 5.42% with ARMA and 6.53% with
SARIMA. Even at 48 hours, LSTM maintained superior accuracy with a MAPE of
2.16%. However, its performance declined on the 30-day horizon, where it reported a
MAPE of 9.75%, higher than the 5.39% obtained using ARMAX. This drop was
attributed to the model’s limited exposure to long-term patterns due to the relatively
short training duration of one year.
The study highlights several critical observations: LSTM’s forecasting performance is
highly sensitive to model hyperparameters such as the number of hidden units, lag
values, and training epochs. Moreover, its ability to generalize and capture seasonality
improves with more extensive training data. Despite its slightly lower performance in
longer-term forecasts within this study, the LSTM model demonstrated clear
advantages in modeling nonlinearities and incorporating multiple input features
without the need for manual feature selection.
In conclusion, RNNs—especially LSTM architectures—offer a powerful alternative to
traditional MTLF models, particularly when rich, multivariate, and temporally
structured datasets are available. Their capacity to learn from raw sequences and
model complex temporal relationships enables more accurate and adaptable forecasts,
especially over short to medium forecast horizons. As summarized in Table 4.6, these

62 | Medium-term load forecasting
models provide notable advantages in terms of flexibility and accuracy but require
careful handling of data volume, preprocessing, and hyperparameter tuning to
mitigate limitations such as overfitting and computational cost.
Table 4.6: Advantages and disadvantages of RNN and LSTM in MTLF.
Model Type Strengths Weaknesses
Capable of capturing both
short- and long-term
dependencies in sequential
Requires large volumes of
data; well-suited for
high-quality training data to
modelling nonlinear and
generalize seasonal trends
complex temporal patterns effectively; training can be
in electricity load; can computationally intensive and
incorporate multiple time-consuming; model
performance is highly
exogenous variables (e.g.,
RNN and LSTM sensitive to hyperparameters
temperature, humidity)
such as lag size, number of
without explicit feature
hidden units, and training
engineering; outperforms
epochs; risk of overfitting if
traditional statistical not properly regularized or if
models (e.g., ARMA, the training dataset is too
SARIMA) in short- and short.
medium-term horizons
when sufficient data is
available.
4.3.2. Transformer-based models
Transformer architectures, originally introduced for natural language processing,
have recently emerged as powerful alternatives to traditional neural networks in time
series forecasting. Their ability to model long-range dependencies through attention
mechanisms, combined with high parallelism during training and inference, makes
them especially well-suited for MTLF—a task defined here as predicting electricity
demand over periods ranging from one week to one month.
In MTLF, models must detect and extrapolate periodic patterns, seasonal trends, and
the influence of external variables such as temperature, humidity, or electricity prices.
RNNs, including their gated variants like LSTMs and GRUs, are naturally suited to
sequence modelling but suffer from limitations such as vanishing gradients and
inherently sequential computations, which hinder scalability. In contrast, transformers
process entire sequences simultaneously, enabling them to learn global relationships
more efficiently.

| Medium-term load forecasting 63
To address the computational limitations of traditional transformers in time series
forecasting, Chan and Yeo [52] proposed a sparse attention transformer for electricity
load prediction. This model replaced the quadratic-cost dot-product attention with
BigBird-style sparse attention, significantly reducing memory requirements while
maintaining strong forecasting accuracy. The sparse transformer was shown to scale
effectively with long input sequences (up to nine weeks) and performed well for
forecast horizons up to one week, making it applicable to medium-term use cases. In
empirical comparisons with benchmark models such as LSTM and TSRNN, the sparse
transformer achieved comparable or better accuracy while offering up to 5× faster
inference time—a notable advantage for real-time grid operations.
Building on these advances, Peng and Yang [37] introduced LDTformer, a
transformer-based model designed specifically for short- and medium-term power
load forecasting. The model integrates domain-aware architectural enhancements that
enable it to capture both high-frequency fluctuations and long-term temporal
dependencies, crucial for forecasting electricity demand over multiple weeks.
LDTformer includes several innovative components:
• A Block Sparse Discrete Cosine Transform (BSDCT) module that converts time-
series segments into the frequency domain, improving the extraction of periodic
patterns while reducing computational cost.
• A Seasonal-Trend Decomposition (STD) module, which dynamically separates
input signals into seasonal and trend components using a mixture-of-experts
architecture. This improves the model’s adaptability to nonstationary behavior
in load profiles.
• A Lagged Correlation Frequency Attention (LCFA) mechanism that introduces
learnable lag-specific weights in the frequency domain, enhancing the model’s
ability to detect long-range and periodic dependencies.
• Causal convolutional layers to enforce temporal consistency while enriching the
local context.
These enhancements enable LDTformer to significantly outperform baseline models—
including Transformer, LSTM, FEDformer, and Mamba—across different seasons and
forecasting windows ranging from one to four weeks. For example, using summer
data with a forecast length of 192 time points (equivalent to four weeks at 30-minute
intervals), LDTformer achieved a MAE of 0.173 and symmetric mean absolute
percentage error (SMAPE) of 0.0186, outperforming all comparison models by
substantial margins. Additionally, the model demonstrated greater robustness to
sharp fluctuations and seasonal variations, which are typical in real-world electricity
consumption.
A comparative summary of transformer-based models used in MTLF is provided in
Table 4.7, which outlines their relative strengths and weaknesses. While the vanilla

64 | Medium-term load forecasting
transformer is effective at capturing long-range dependencies, it suffers from high
computational costs and lacks domain-specific enhancements. The sparse transformer
addresses these efficiency issues, offering scalability with minimal accuracy loss.
Meanwhile, LDTformer represents the most advanced solution, delivering top-tier
performance by combining frequency-domain analysis, decomposition techniques,
and lag-sensitive attention mechanisms.
Table 4.7: Advantages and disadvantages of transformer-based models in MTLF.
Model Type Strengths Weaknesses
Efficient inference; suitable
May lose information with
Sparse Transformer for long lookback aggressive sparsity settings.
sequences; robust accuracy.
Integrates time and
frequency attention; best- Increased complexity; higher
LDTformer
in-class forecasting training overhead.
accuracy.
4.4. Hybrid models
Hybrid modelling approaches have gained prominence in the field of MTLF,
especially when dealing with complex time series such as monthly electricity demand.
These models integrate statistical, signal decomposition, and deep learning techniques
to enhance forecasting accuracy and model robustness. In this section, recent advances
in hybrid models are grouped according to their primary algorithmic foundation—
ranging from statistical–deep learning combinations to Transformer-based
architectures and signal decomposition frameworks.

| Medium-term load forecasting 65
4.4.1. Statistical–deep learning hybrids
Combining classical statistical techniques with deep learning offers the advantage of
modelling both linear and nonlinear patterns. Dudek et al. [53] proposed a hybrid
architecture, as it is shown in Figure 4.3, that integrates Exponential Smoothing (ETS)
with a Residual Dilated LSTM network. In their approach, ETS captures trend and
seasonal patterns, while the LSTM models the residual nonlinear fluctuations. This
two-stage setup was tested on monthly electricity demand data from 35 European
countries. The hybrid model achieved a MAPE reduction of up to 25% compared to
standalone ETS and LSTM baselines, making it a strong candidate for MTLF
applications, particularly where trend and seasonal variation dominate the signal.
Figure 4.3: Block diagram of the ETS+RD-LSTM forecasting system [53].
Similarly, González Grandón et al. [54] developed a hybrid model that integrates
ARIMA for modelling long-term linear trends and an LSTM network for capturing
nonlinear variations. Their approach was evaluated on calendar- and temperature-
driven electricity load data. The hybrid ARIMA-LSTM model achieved lower RMSE
and MAPE values than both standalone LSTM and ARIMA models, with a reported

66 | Medium-term load forecasting
MAPE of 2.48% and RMSE of 18.3 MW. This confirms the synergy between linear and
nonlinear modelling in improving forecasting precision at monthly horizons.
4.4.2. Transformer-based hybrids
Transformer-based architectures have revolutionized sequence modelling due to their
capacity to model long-range dependencies. Building on this foundation, Wang et al.
[55] proposed a Hybrid Autoformer Framework (HAFF) specifically for electricity
demand forecasting that is illustrated in Figure 4.4. Their model introduces a
preprocessing pipeline using MLR with 10 variables and Bootstrap sampling, followed
by an enhanced Autoformer with improved auto-correlation mechanisms. Evaluated
on datasets from Taixing, China, and New South Wales, Australia, the HAFF model
achieved a MAPE of 1.63% and RMSE of 47.28 MW in Taixing, and 2.43% and 239.96
MW, respectively, in New South Wales. These results outperformed standard
Transformer variants like Reformer and Informer, especially when data were limited
or seasonal fluctuations were prominent.
Figure 4.4: The whole structure of HAFF [55].
Expanding on Transformer designs, Antonesi et al. [56] introduced a hybrid model
that integrates Transformers with Liquid Neural Networks (LNNs), CNN encoders,
and adaptive positional encodings. Their model was evaluated across various building
types—including households and commercial facilities—using daily and monthly
energy consumption data. The model demonstrated a SMAPE improvement ranging
from 1.5% to 50% over basic Transformer, LSTM, and ANN models. With R² scores
exceeding 0.92 in most cases, and a training time reduction of 8% over the base
Transformer, the proposed model balances accuracy with computational efficiency,
making it a compelling hybrid solution for monthly MTLF scenarios.
4.4.3. CNN–LSTM hybrids
CNN–LSTM architectures are widely used for their ability to simultaneously extract
spatial features and model temporal dependencies. Yıldız Doğan et al. [57] introduced
a CNN-LSTM hybrid model aimed at estimating electricity demand for sustainable
cities. Using hourly electricity consumption and meteorological data collected over a
five-year period from a city in Türkiye, the model was evaluated on its ability to

| Medium-term load forecasting 67
forecast medium-term electricity demand. The CNN component extracts high-level
temporal patterns, while the LSTM captures sequential dependencies. The hybrid
model achieved a MAPE of 2.9%, RMSE of 1.36, and an R² value of 0.86—
outperforming the standalone LSTM model (R² = 0.81), thereby demonstrating its
superiority in learning complex temporal trends over medium horizons.
Zhang et al. [58] introduced an innovative multi-task hybrid model, MTMV-CNN-
LSTM, which combines Convolutional Neural Networks and Long Short-Term
Memory networks within a multi-task learning framework to forecast both short- and
medium-term electricity loads. The model addresses the issue of redundant or
mismatched feature intervals—such as weather data at daily intervals versus power
load at 15-minute intervals—by structuring the learning tasks hierarchically. The
auxiliary task handles slower-varying features (e.g., weather, calendar effects), while
the main task predicts detailed load profiles. For medium-term forecasting, defined in
their study as a 3-month horizon, the MTMV-CNN-LSTM achieved superior results: it
outperformed six baseline models including Prophet, CatBoost, GRU, LSTM, GAN,
and even a standard CNN-LSTM. Specifically, it recorded an RMSE of 0.053, MAE of
0.044, and MSE of 0.003, with an R² of 0.640. This architecture demonstrates excellent
robustness, maintaining accuracy under input perturbations such as added Gaussian
and uniform noise, with R² values consistently above 0.8 even under noisy conditions.
Its ability to generalize across multiple horizons and handle complex feature structures
makes it a strong candidate for monthly MTLF applications.
4.4.4. Signal decomposition-based hybrids
Signal decomposition methods such as Empirical Mode Decomposition (EMD) and its
ensemble variants offer powerful tools for handling non-stationary and multi-scale
time series. Lei Wang et al. [59] proposed a hybrid model based on Figure 4.5—EEMD-
SE-PSO-SVR—that leverages ensemble empirical mode decomposition (EEMD) to
break down the demand signal, uses sample entropy (SE) to filter noise, and applies
SVR with parameters optimized via Particle Swarm Optimization (PSO). Applied to
monthly electricity demand in China, this hybrid method outperformed traditional
SVR and statistical models, reducing the MAPE by 54.49%. The authors highlighted
the model’s ability to manage data irregularities and nonlinear dependencies, which
are common in medium-term forecasting tasks.
In another decomposition-based hybrid, Huang et al. [60] introduced an EMD-LSTM-
Markov model for predicting building cooling loads. The architecture first
decomposes the load signal using EMD, applies LSTM to model temporal sequences,
and finally incorporates a Markov chain to adjust state transitions based on prior
probabilities. Although designed for cooling loads, the model achieved a MAPE of
0.84% and RMSE of 4.53 in monthly-scale prediction tasks, demonstrating its
adaptability to broader MTLF applications.

68 | Medium-term load forecasting
Figure 4.5: The architecture of the proposed hybrid model by Lei Wang et al [59].
4.4.5. Neural Prophet–LSTM hybrids
Shohan et al. [61] developed a novel architecture by combining a LSTM model with
Neural Prophet (NP), a model built upon Facebook Prophet but enhanced with
autoregressive and seasonality handling features. As Figure 4.6 illustrates, outputs
from LSTM and NP are combined via an ANN, resulting in a hybrid architecture
tailored to different forecasting horizons. Evaluated on ERCOT and NREL datasets for
both short- and medium-term forecasting, the model achieved lower MAPE values
across all benchmarks, with monthly MAPE dropping to 1.79% and RMSE falling

| Medium-term load forecasting 69
below 2.3 MW. The integration of NP offers increased interpretability, while the LSTM
preserves sequential learning, striking a strong balance between accuracy and model
explainability.
Figure 4.6: Block diagram of proposed hybrid model by Shohan et al [61].
These diverse hybrid approaches underscore the increasing sophistication and
customization of MTLF models in addressing nonlinearity, seasonality, and data
scarcity. A comparative summary of these models, highlighting their strengths and
limitations, is provided in Table 4.8.
Table 4.8: Benefits and weakness of hybrid models in MTLF.
authors Benefits Weakness
Handles trend/seasonal +
Dudek et al. Requires tuning of two separate
residuals; accurate for monthly
[53] model stages
scales
González
Combines statistical structure Sensitive to ARIMA lag
Grandón et
with temporal learning parameters
al. [54]
Outperforms base Transformers;
Wang et al. Complex multi-stage
robust to seasonal and sparse
[55] preprocessing
data

70 | Medium-term load forecasting
High accuracy and
Antonesi et Architecturally complex;
generalization; efficient for
al. [58] training stability needs care
monthly predictions
Yıldız
Captures both local and
May overlook external variables
Doğan et al. temporal patterns; strong
like price or policy
[57] generalization
Excellent on 3-month prediction;
Zhang et al. Slightly lower R² than simpler
multi-task learning improves
[58] CNN-LSTM baseline
generality
Lei Wang et Strong for non-stationary data; Computationally intensive due
al. [59] robust error reduction to decomposition and tuning
Huang et al. Captures states and transitions; Markov component can be lag-
[60] stable and accurate sensitive
High accuracy and
Shohan et Integration of NP lacks
interpretability; robust across
al. [61] theoretical transparency
multiple horizons
4.5. Summary
Chapter 4 provided an in-depth review of methodologies used for medium-term load
forecasting, which targets horizons ranging from one week to one month. This
forecasting range plays a critical role in strategic energy planning, maintenance
scheduling, and tariff design. The chapter explored four major categories of MTLF
techniques: statistical models, machine learning approaches, deep learning
architectures, and hybrid frameworks.
Statistical models such as Linear Regression, Quantile Regression, ARIMA, and
SARIMA offer simplicity and interpretability, performing well under stable seasonal
conditions. However, their capacity to manage nonlinear patterns and evolving
consumption behaviors is limited. Enhancements like Fourier-ARIMA and kernel
density methods improve adaptability but increase model complexity.
ML methods—especially tree-based models like Random Forests, XGBoost, and
LightGBM—demonstrated strong performance in handling nonlinearities, temporal
patterns, and external features such as weather and economic variables. k-NN offered
simplicity and interpretability but faced challenges with high-dimensional or noisy
datasets. ANN models provided higher accuracy by capturing intricate nonlinear
patterns but required substantial data and careful tuning.
Deep learning models, particularly LSTM networks, proved effective in modeling
long-term temporal dependencies and nonlinear load behaviors, though they demand

| Medium-term load forecasting 71
high computational resources and large datasets. Transformer-based models emerged
as a promising alternative, offering improved scalability, parallelism, and
robustness—especially in complex and data-scarce scenarios. Advanced variants like
LDTformer demonstrated state-of-the-art forecasting accuracy for monthly horizons.
Hybrid models integrated the strengths of multiple approaches to overcome
individual limitations. Combinations such as ETS+LSTM, ARIMA+LSTM, CNN-
LSTM, and Transformer-based hybrids showed superior accuracy, robustness, and
generalizability. Signal decomposition and optimization techniques (e.g., EEMD, PSO,
NSGA-II) further enhanced model performance, especially under data irregularities
and seasonal fluctuations.
In conclusion, the chapter underscores that while traditional models retain value in
stable environments, ML, deep learning, and hybrid methods are increasingly
essential for accurate and resilient MTLF. Their adaptability to evolving consumption
patterns and integration with external variables make them indispensable for modern
energy systems.

72 | Long-term load forecasting
5
Long-term load forecasting
LTLF involves predicting electricity demand over extended horizons, typically
ranging from one year to several decades. These forecasts play a crucial role in strategic
planning for power system infrastructure, investment decisions, energy policy
development, and integration of renewable energy sources. Unlike short-term or
medium-term forecasting, which focuses on operational or tactical grid management,
LTLF emphasizes the structural evolution of demand influenced by socioeconomic
growth, technological shifts, climate policy, and demographic trends.
Accurate long-term forecasts enable utility companies, transmission operators, and
governmental bodies to ensure sufficient capacity, optimize capital allocation, and
evaluate the long-term viability of energy projects. However, LTLF presents several
challenges due to high uncertainty, evolving consumption patterns, and limited
availability of high-resolution long-term data. As a result, LTLF models often rely on
macroeconomic indicators, population growth projections, urban development plans,
and technological adoption rates.
Among various modeling approaches, regression-based techniques have remained a
cornerstone of LTLF due to their interpretability, ease of implementation, and ability
to incorporate trend and calendar effects. The following sections explore key studies
that apply regression models to long-term electricity demand forecasting, highlighting
their methodologies, performance, and practical implications.
5.1. Statistical methods
Statistical methods form the foundational basis of long-term load forecasting due to
their simplicity, transparency, and capacity to model historical trends and seasonal
patterns. These approaches typically establish relationships between electricity
consumption and external influencing factors such as population, GDP, industrial
output, or calendar variables.
For LTLF, commonly used statistical techniques include multiple linear regression,
logistic regression, and time series decomposition. Multiple linear regression is
effective in capturing linear trends based on socio-economic indicators and calendar
effects, while logistic regression is particularly suited for modeling saturated growth
in electricity demand — a typical pattern in mature economies or fully electrified

| Long-term load forecasting 73
regions. These models offer interpretability and are valuable for scenario-based
planning and policy simulation.
Despite their strengths, statistical methods may struggle to capture nonlinearities,
structural breaks, and evolving behavioral patterns over extended horizons. Therefore,
they are often used in combination with clustering or scenario analysis to enhance
robustness in long-term forecasts.
5.1.1. Regression-based models
Regression-based approaches have long served as the backbone of long-term load
forecasting due to their simplicity, interpretability, and effectiveness in modeling
relationships between electricity demand and socioeconomic variables. These models
typically assume that electricity consumption can be expressed as a function of
independent variables such as population growth, gross domestic product (GDP),
industrial activity, and calendar-related factors. For long-term forecasting horizons,
regression models are especially valuable in scenario planning, allowing utilities and
policymakers to assess how structural and demographic trends will influence future
electricity needs.
One representative study employing regression methods for long-term forecasting is
by Nano et al. [19], who proposed a MLR model enhanced with calendar effects. The
model integrates variables such as day type (weekday, weekend, holiday), seasonal
indicators, and long-term temporal trends to forecast electricity demand at a yearly
scale. The framework is designed for practical utility applications and captures
recurring consumption patterns over multiple years. Although specific error metrics
such as MAPE were not detailed, the study reported strong alignment with historical
trends, indicating good reliability in forecasting seasonal variations. However, the
model’s reliance on linear assumptions limits its flexibility in modeling nonlinear
growth, particularly in systems approaching demand saturation.
In a more complex formulation, Royal et al. [43] developed a regression-based
statistical framework tailored for district-level long-term forecasting. Their
methodology combines linear regression with aggregated seasonal profiles and
incorporates localized planning data, such as infrastructure developments and
population projections. The model was applied over a multi-year horizon and
achieved a MAPE below 7%, showcasing its robustness for practical long-term
planning. Compared to advanced machine learning models, this framework offers
improved transparency and explainability—important qualities for long-term
strategic decisions—though it may not be as responsive to abrupt structural changes
or nonstationary patterns.
A more recent contribution by Feng et al. [62] addresses the limitations of linearity in
traditional regression by introducing an improved logistic regression model for
saturated load forecasting. Their approach models electricity demand using an S-

74 | Long-term load forecasting
shaped logistic curve, which is particularly well-suited for markets approaching
maturity where demand growth slows and eventually plateaus. To enhance
performance, the study also integrates affinity propagation clustering to group similar
load profiles, improving both prediction accuracy and segmentation. The model
demonstrated superior accuracy in predicting long-term saturation levels and
outperformed conventional linear regression methods, with reported MAPE values
below 5% in year-ahead forecasts. This approach provides a more realistic depiction
of long-term load dynamics in stable or mature energy systems.
Together, these studies demonstrate the diverse ways regression models can be
adapted for long-term load forecasting—from capturing linear trends and calendar
effects to modeling saturation behaviors in maturing markets. While regression
models are valued for their transparency and ease of implementation, they may
require hybridization or advanced calibration techniques to manage complex
nonlinearities and emerging consumption behaviors over long planning horizons.
As summarized in Table 5.1, different regression techniques offer specific advantages
and limitations when applied to LTLF, depending on the structural characteristics of
the electricity system and the forecasting context.
Table 5.1: Advantages and disadvantages of regression -based models in LTLF.
Model Type Strengths Weaknesses
Simple, interpretable;
Multiple Linear Cannot capture nonlinear or
effective for trend and
Regression saturation behavior
calendar modeling
Robust in localized long-
Linear Regression Less flexible under abrupt
term trends; useful for
(District-level) structural changes
scenario analysis
Captures demand
Improved Logistic Requires saturation context;
saturation; better long-term
Regression more complex to calibrate
curve fitting
5.1.2. ARIMA and SARIMA
Time series models such as ARIMA and its seasonal extension SARIMA have
remained foundational tools in load forecasting due to their ability to model temporal
dependencies, long-term trends, and seasonal fluctuations. In the context of LTLF,
these models are particularly useful for systems with stable consumption patterns and
clear seasonality. Their mathematical transparency and relatively low data
requirements make them attractive for policy-oriented planning and strategic demand
estimation.

| Long-term load forecasting 75
Kumar et al. [63] explored the use of ARIMA, ARMA, and SARIMA models for
forecasting long-term load profiles in smart-metered distribution systems. The study
focused on capturing consumption behavior in the presence of granular data made
available by smart metering infrastructure. Their findings underscored that SARIMA,
in particular, was able to effectively capture periodic consumption patterns and long-
term shifts in usage. While the authors did not provide specific numerical values for
forecast errors, they emphasized that SARIMA outperformed ARIMA and ARMA in
scenarios where seasonal variability was pronounced. The study highlighted those
statistical models, when adequately parameterized and applied to high-quality smart
meter data, could provide reliable forecasts for annual load planning.
A more detailed comparative study by Dubey et al. [64] examined the performance of
SARIMA against a deep learning model, LSTM, for time series forecasting of energy
consumption. The authors applied both models to daily energy usage data enriched
with weather-related features such as temperature, humidity, and wind speed. The
SARIMA model successfully captured the seasonal dynamics in the data and produced
stable forecasts over extended horizons. However, it lagged behind LSTM in terms of
predictive accuracy. The study reported that SARIMA yielded a MAE compared to
LSTM, indicating that while SARIMA is well-suited for seasonally-driven systems, its
linear structure may be less effective in modeling nonlinearities present in evolving
energy consumption patterns. Nonetheless, SARIMA was preferred for its
interpretability and resilience against overfitting, which are critical in long-term utility
forecasting where transparency and reproducibility are prioritized.
Both studies suggest that ARIMA-based models remain viable and useful in LTLF,
particularly when forecasting is conducted in mature systems with historical stability
and when explainability is a necessary criterion. However, their effectiveness may
diminish in contexts characterized by abrupt structural changes, such as the
integration of electric vehicles, distributed energy resources, or dynamic tariff
structures. In such cases, hybrid or data-driven models may offer improved accuracy.
Nonetheless, the ability of SARIMA to manage seasonality and ARIMA’s simplicity
continue to make them valuable tools in the long-term forecasting toolkit.
As summarized in Table 5.2, ARIMA and SARIMA methods offer distinct advantages
in long-term forecasting scenarios, particularly in relation to transparency, seasonality
handling, and data efficiency. However, their performance can be constrained by
linearity assumptions and the inability to adapt to sudden behavioral shifts in energy
usage.

76 | Long-term load forecasting
Table 5.2: Advantages and disadvantages of ARIMA and SARIMA methods in LTLF.
Model Type Strengths Weaknesses
Poor seasonality handling;
Simple, interpretable, low
ARIMA struggles with nonlinear
data requirement
patterns
Less accurate than deep
Captures seasonality well;
SARIMA learning models; rigid under
robust for stable time series
system change
5.2. Machine learning methods
ML methods have emerged as powerful alternatives to traditional statistical models
for LTLF, especially in contexts where electricity consumption is influenced by a large
number of interdependent and nonlinear factors. Unlike classical approaches that rely
on explicit assumptions about data distribution or trend linearity, ML models learn
patterns directly from historical data, enabling them to adapt to complex relationships
between electricity demand and a wide range of exogenous variables, including
weather, socio-economic indicators, urbanization trends, and behavioral shifts.
In the context of LTLF, ML models such as decision trees, support vector machines, k-
nearest neighbors, and ensemble techniques like Random Forests and Gradient
Boosting have shown increasing relevance. These models can accommodate high-
dimensional datasets and are often more flexible than linear models when forecasting
long-term consumption influenced by evolving market structures and energy usage
patterns. Their ability to generalize from past trends and adjust to non-stationary
environments makes them particularly useful in modern energy systems characterized
by decentralization, demand-side variability, and renewable integration.
However, the effectiveness of ML methods in LTLF depends significantly on the
quality and volume of data, careful feature selection, and model interpretability. While
some methods offer high accuracy, they may lack transparency, posing challenges in
regulatory or policy-driven planning where explainability is essential.
Let me know which subsections you would like to explore next—e.g., tree-based
models, support vector regression, k-NN, or others.
5.2.1. SVR
SVR has emerged as a powerful technique for long-term load forecasting due to its
ability to manage nonlinear relationships and limited datasets while maintaining
robustness against overfitting. SVR models are particularly effective in capturing the
complex dependencies that characterize annual electricity demand patterns.
Wang et al. [65] proposed an annual load forecasting model based on SVR optimized
using a Differential Evolution (DE) algorithm. The study focused specifically on one-

| Long-term load forecasting 77
year-ahead electricity demand forecasts. The SVR model, when tuned using DE,
demonstrated enhanced predictive performance compared to traditional regression
methods. For instance, the optimized SVR model achieved lower MAPE compared to
both the standard SVR and linear regression benchmarks. This result confirms that
fine-tuning the hyperparameters of SVR can significantly improve its applicability to
annual load forecasting, where prediction horizons are extended and data variability
increases.
Hu [66] conducted a comparative study evaluating SVR, neural networks, and
Exponentially Weighted Moving Average (EWMA) models for long-term load
forecasting in the context of air conditioning systems in large buildings. Although the
study included other techniques, SVR was examined as a stand-alone model. Results
showed that SVR offered competitive accuracy in predicting long-term cooling loads,
particularly when nonlinearities and seasonal fluctuations were present. However, it
slightly underperformed compared to neural networks in capturing rapid load
transitions, especially in extreme temperature conditions. The SVR model, while stable
and interpretable, produced higher RMSE values than the neural network model in
high variability periods, indicating a limitation in dynamic adaptability.
Kazemzadeh et al. [67] presented a hybrid forecasting model that integrates SVR with
ARIMA and ANN, using PSO for parameter tuning. Although the study's primary
focus was on a hybrid approach, it also evaluated SVR independently as a baseline.
For long-term forecasting of yearly peak load and energy demand in Iran’s National
Electric Energy System, the SVR model alone produced respectable forecasting
accuracy, but it was outperformed by the hybrid model in terms of both MAPE and
RMSE. Specifically, SVR’s standalone MAPE was in the range of 5.3% to 6.7%, while
the hybrid model reduced this to below 4.5%. This finding underscores that SVR
performs reasonably well on its own for long-term horizons but can benefit
substantially when integrated into ensemble frameworks that address its limitations
in temporal modelling.
In conclusion, SVR provides a solid foundation for long-term forecasting and is
especially effective when carefully tuned or used as a component within hybrid
systems. While its performance may trail slightly behind deep learning models or
hybrid systems in some scenarios, SVR's interpretability and generalization capacity
make it a valuable tool for annual load prediction in both residential and commercial
domains. These findings are summarized in Table 5.3, comparing the strengths and
limitations of SVR-based approaches across different applications in LTLF.

78 | Long-term load forecasting
Table 5.3: Advantages and disadvantages of SVR method in LTLF.
Model Type Strengths Weaknesses
Effectively models
nonlinear relationships in
yearly energy demand and Performance highly depends
on hyperparameter tuning;
building load profiles;
standalone SVR may yield
performance can be
SVR lower accuracy compared to
significantly improved
neural networks or hybrid
using optimization
models, especially in
techniques like Differential
capturing peak loads.
Evolution; adaptable across
various sectors.
5.2.2. Tree-based models
Tree-based models—including Decision Trees (DTs), Random Forests (RF), and
Gradient Boosting Machines (GBMs)—have gained significant traction in long-term
load forecasting (LTLF) due to their ability to model complex nonlinear interactions
without assuming a specific data distribution. These models are especially useful
when forecasting yearly or multi-month electricity demand, where features such as
seasonality, economic indicators, and demographic patterns interact in complex ways.
Dinmohammadi et al. [44] conducted a detailed evaluation of ensemble tree-based
models for long-term residential electricity consumption forecasting. Their study
compared Random Forests and Gradient Boosting algorithms in predicting energy
usage across different housing profiles and geographic regions over an annual
horizon. The results demonstrated that Gradient Boosting achieved slightly better
accuracy (MAPE ≈ 5.8%) compared to Random Forests (MAPE ≈ 6.2%), although both
significantly outperformed traditional regression models. The authors highlighted
that Random Forests provided more stable results across varying input conditions,
while Gradient Boosting offered higher precision when hyperparameters were
carefully tuned. Additionally, the ensemble models showed resilience to noise and
missing values, which are common in real-world LTLF datasets.
Sangrody et al. [68] explored multiple machine learning methods for long-term
electricity demand forecasting in the U.S., including decision tree-based algorithms.
Although their main focus was a comparative framework across several learning
models, they confirmed the relevance of tree-based models for capturing nonlinear
trends in multi-year forecasts. In particular, decision tree models were useful for
feature importance analysis and detecting seasonal or structural patterns in
consumption behavior. The authors noted that while tree-based models were
generally outperformed by deep learning techniques in accuracy, they remained

| Long-term load forecasting 79
attractive for their interpretability and lower computational cost—especially in grid
planning and regulatory applications.
Together, these studies affirm the practical strengths of tree-based models for LTLF:
ensemble trees like Random Forests and Gradient Boosting achieve a strong balance
between accuracy and generalizability, while individual trees serve as interpretable
tools for exploring underlying data structures. Despite being slightly less accurate than
some deep learning models, their transparency and robustness make them
indispensable in long-term forecasting contexts, particularly where model
explainability and stakeholder trust are priorities.
As summarized in Table 5.4, the main strength of tree-based models lies in their ability
to adapt to nonlinear patterns in high-dimensional data with limited preprocessing.
However, their performance varies depending on the algorithm: standalone trees are
interpretable but less accurate, while ensemble methods improve forecasting
performance but require more resources and careful tuning.
Table 5.4: Advantages and disadvantages of tree-based models in LTLF.
Model Type Strengths Weaknesses
Easy to interpret; low
Lower accuracy for long
Decision Trees computation; useful for horizons; sensitive to data
policy contexts. noise.
Stable across datasets;
Less interpretable; require
Random Forest handles missing data and larger data volumes, more
noise well. memory and training time.
High accuracy; good with Sensitive to hyperparameters
Gradient Boosting
complex nonlinear trends. tuning; slower to train
5.2.3. ANN
ANNs have been widely adopted in load forecasting tasks due to their ability to model
complex, nonlinear relationships between historical consumption and external
influencing factors. In LTLF, where the prediction horizon spans several months to
years, ANNs are particularly valuable because they can learn from high-dimensional
input spaces and accommodate a variety of exogenous variables such as economic
indicators, demographic trends, and weather patterns.
Sangrody et al. [68] applied machine learning approaches—including ANNs—for
long-term electricity demand forecasting in their 2018 study. They designed their
model using historical demand data and various macroeconomic inputs,
demonstrating that ANN models were capable of capturing evolving patterns in
electricity consumption with higher flexibility than conventional linear models.
Although exact numerical error values were not provided, the authors emphasized
that ANNs outperformed baseline models in tracking long-term trends and seasonal

80 | Long-term load forecasting
variations in electricity usage. The flexibility of ANN models was particularly useful
in handling fluctuations caused by population growth and policy changes.
Similarly, Ozdemir [69] conducted a comprehensive evaluation of several artificial
intelligence and machine learning methods—including ANNs—for predicting
Turkey's annual electricity consumption up to 2030. The study considered input
features such as GDP, population, and international trade indicators. Among all tested
models, four were shortlisted based on forecasting accuracy: Stepwise Linear
Regression (SLR), GA, Gaussian Process Regression (GPR), and Neural Networks.
Although SLR had the lowest MAPE of 2.36%, the neural network model also
exhibited competitive performance and was retained for final scenario-based
projections. The use of NN proved effective in modeling the nonlinear and
multidimensional characteristics of energy demand data over extended horizons. The
study also highlighted the strength of NN in integrating multiple socio-economic
variables, making it well-suited for national-level energy planning.
Together, these studies underscore the relevance of ANNs for LTLF applications.
While ANNs require careful configuration of architecture and training parameters to
avoid overfitting, they remain one of the most robust tools for capturing hidden
patterns and interactions in long-term consumption data. Table 5.5 summarizes the
key strengths and limitations of ANN models for LTLF based on the reviewed
literature.
Table 5.5: Advantages and disadvantages of ANN model in LTLF.
Model Type Strengths Weaknesses
Captures nonlinear and
complex patterns over
long-term horizons;
Sensitive to parameter tuning;
handles multivariate and
prone to overfitting with small
ANN socioeconomic inputs datasets; requires high
effectively; adaptable to computational resources and
data preprocessing.
changes in consumption
behavior and economic
factors.
5.3. Deep learning
Deep learning models have emerged as powerful tools in LTLF due to their ability to
model highly nonlinear relationships, extract complex features, and learn from
sequential patterns in large-scale energy datasets. These models outperform many
traditional statistical and machine learning techniques when sufficient historical and
contextual data are available, particularly over extended forecast horizons.

| Long-term load forecasting 81
In the context of LTLF, where electricity demand must be projected months or years
ahead, deep learning architectures are valued for their scalability and capacity to
handle multivariate inputs without extensive feature engineering. However, they also
come with limitations such as high computational requirements, sensitivity to training
data quality, and limited interpretability.
5.3.1. Multilayer perceptron
MLP neural networks have demonstrated significant potential in long-term load
forecasting due to their capacity to model complex, nonlinear relationships across
multi-year datasets. These networks are especially effective when historical
consumption data is influenced by multiple interdependent variables such as seasonal
trends, economic growth, or policy changes.
Faraji et al. [70] introduced a long-term forecasting approach for annual load growth
in microgrids using an MLP model. The research focused on the optimal planning of
a grid-connected microgrid in Tehran, employing HOMER software for simulating
different load growth scenarios. Their method used historical annual load data to train
the MLP, capturing nonlinear growth patterns over multiple years. While the paper
primarily emphasizes the impact of accurate load growth prediction on system
planning rather than detailed error metrics, it highlights how the use of MLP
forecasting leads to more reliable optimization results when compared with traditional
linear forecasting models.
Complementing this, Kim et al. [71] proposed a hybrid long-term forecasting model
that is shown in Figure 5.1 and combines MLP with statistical techniques to overcome
the average convergence limitations seen in standalone machine learning methods.
Their model was trained and validated using massive-scale real-world data from over
10,000 distribution lines provided by Korea Electric Power Corporation (KEPCO). The
hybrid approach yielded an average accuracy of 89.56% based on Normalized Root
Mean Squared Error (NRMSE), outperforming models based purely on statistical
regression or MLP alone. Notably, their study validates the hybrid model for practical
deployment in national-scale distribution network planning, underscoring its
robustness for multi-year forecasting applications.
Together, these studies illustrate the strengths of MLP-based models in capturing
complex nonlinear demand trends across extended time horizons. While MLP alone
proves useful in improving the precision of load growth estimations, its combination
with statistical approaches offers improved stability and generalization, especially
when applied to large-scale datasets.

82 | Long-term load forecasting
Figure 5.1: Feedforward procedure of neural network for MLP by Kim et al. [71].
As summarized in Table 5.6, MLP models provide a flexible and powerful approach
to LTLF, with their benefits and weaknesses largely determined by dataset size, model
tuning, and whether hybridization is used.
Table 5.6: Advantages and disadvantages of MLP model in LTLF.
Model Type Strengths Weaknesses
Model nonlinear
Standalone MLP may suffer
relationships; suitable for
from convergence issues;
annual load growth; high
MLP performance sensitive to
accuracy when hybridized;
architecture and training data
effective in real-world
quality.
deployment.
5.3.2. LSTM
LSTM networks are a class of RNNs widely used for sequential data modelling due to
their ability to capture long-term dependencies through gated mechanisms. While
traditional LSTM models have shown promising results in many time series
applications, their direct application to LTLF has faced limitations, especially in
capturing extended temporal patterns and handling data scarcity.
To address these challenges, recent studies have introduced enhanced LSTM
architectures or combined LSTM with complementary techniques.
Dai et al. [72] introduced a novel model illustrated in Figure 5.2 and called Segmented
Self-Attention LSTM (SALSTM), which integrates segmented iteration and intra-
segment self-attention mechanisms into the LSTM framework. This architecture was
specifically developed to tackle the issue of performance degradation in long-sequence
forecasting. In traditional LSTM, as the prediction length increases—such as
forecasting 96-time steps ahead—the model's ability to retain meaningful information
diminishes significantly. The SALSTM model mitigates this by reducing the recursive

| Long-term load forecasting 83
steps needed and embedding self-attention within segments to better capture long-
distance dependencies. Experimental evaluations on benchmark datasets
demonstrated that SALSTM consistently outperforms both standard LSTM and state-
of-the-art Transformer-based models in long-term forecasting tasks. This reinforces
the notion that LSTM-based methods, when properly adapted, remain competitive in
LTLF contexts.
Figure 5.2: The self-attention model and its computational process by Dai et al. [72].
On the other hand, Go et al. [73] tackled a different aspect of LSTM limitations in
LTLF—data availability. Their proposed approach addresses the difficulty of
forecasting in the context of insufficient long-term historical data, particularly for
growing sectors such as electric vehicles and evolving economies. The researchers
developed a hybrid model that combines decomposition-linear methods, exponential
smoothing, and LSTM. Initially, this model generates synthetic future inputs by
capturing trends and seasonality from available historical data using statistical
decomposition and smoothing. These synthetic sequences are then used as inputs for
the LSTM model. When applied to long-term demand forecasting, including the
creation of reserve demand curves for future power system planning, the model
demonstrated strong reliability and practical utility. This method is especially
beneficial when forecasting in data-scarce environments while still utilizing LSTM's
pattern recognition capabilities.
Together, these studies illustrate the versatility of LSTM-based methods when
augmented with attention mechanisms [72] or hybridized with classical forecasting

84 | Long-term load forecasting
techniques [73]. Such enhancements enable LSTM to maintain forecasting accuracy
and reliability even in the face of long prediction horizons and limited data.
Table 5.7 summarizes the key strengths and limitations of these LSTM-based
approaches in the context of long-term load forecasting.
Table 5.7: Advantages and disadvantages of LSTM model in LTLF.
Model Type Strengths Weaknesses
Captures long-term
dependencies; flexible Captures long-term
architecture adaptable to dependencies; flexible
architecture adaptable to
enhancements (e.g., self-
enhancements (e.g., self-
attention, hybrid input
LSTM attention, hybrid input
generation); performs well
generation); performs well in
in long-term forecasting
long-term forecasting when
when extended; robust in
extended; robust in handling
handling nonlinear nonlinear temporal patterns.
temporal patterns.
5.3.3. Transformer-based models
Transformer-based models have emerged as a powerful alternative to traditional
sequence forecasting architectures due to their ability to model long-range
dependencies using self-attention mechanisms. However, in the context of LTLF,
standard Transformers often encounter challenges such as high computational
complexity, limited interpretability, and insufficient accuracy when applied over
extended time horizons. Recent advancements have introduced improved variants
that address these shortcomings by modifying attention mechanisms, integrating
hybrid architectures, or enhancing temporal granularity.
Tan et al. [74] proposed Cakformer, a Transformer variant specifically designed for
long-term heat load forecasting. To overcome the limitations of conventional self-
attention, Cakformer introduces a convolutional autocorrelation mechanism that
simultaneously captures local features and global time dependencies. Furthermore,
the model replaces the traditional MLP with a Kolmogorov–Arnold Network (KAN)
to improve the learning of nonlinear, high-dimensional interactions. A
Synchrosqueezed Wavelet Transform (SWT) is also employed to reduce noise in the
input data. Experimental validation across multiple prediction horizons—96, 192, 336,
and 720 steps—demonstrated Cakformer’s superiority over seven state-of-the-art
models, including Autoformer and Transformer. At 720-step forecasting, for instance,
Cakformer reduced MAE by 9.6% and root mean squared error (RMSE) by 8.3%
compared to Autoformer, indicating its robustness in both accuracy and generalization
across datasets.

| Long-term load forecasting 85
Yang et al. [75] developed the Multi-Granularity Autoformer (MG-Autoformer) which
is shown in Figure 5.3 to address both deterministic and probabilistic aspects of long-
term power load forecasting. The model introduces a Multi-Granularity Auto-
Correlation Attention Mechanism (MG-ACAM) to effectively model both fine-grained
short-term fluctuations and coarse long-term trends. To manage computational
overhead, a shared query–key (Q–K) mechanism is implemented, and a quantile loss
function is used to enable probabilistic forecasting with uncertainty quantification.
Evaluation on four diverse benchmark datasets—Portugal, USA, Australia, and ISO
New England—revealed that MG-Autoformer consistently outperformed Autoformer
and Transformer in both point and probabilistic forecasting. It achieved up to 11.2%
lower MAE and 9.4% lower RMSE in deterministic tasks, and a 13.5% reduction in
normalized pinball loss (NPL) in probabilistic settings, confirming its applicability in
real-world planning scenarios where confidence intervals are vital.
Figure 5.3: The multi-granularity Autoformer by Yang et al. [75].
Together, these studies demonstrate that Transformer-based models—when equipped
with tailored attention mechanisms and multiscale forecasting strategies—can
significantly improve the performance of LTLF models. Table 5.8 summarizes the
enhancements, predictive gains, and limitations of these Transformer variants.
Table 5.8: Advantages and Disadvantages of Transformer-based models in LTLF.
Model Type Strengths Weaknesses
High interpretability; best
High architectural complexity;
Cakformer multi-horizon accuracy;
focused on heat load datasets.
robust to noise.
Captures trends at multiple
Design sensitive to granularity
scales; supports
MG-Autoformer setup; training time remains
probabilistic forecasting;
high.
efficient attention design.

86 | Long-term load forecasting
5.4. Hybrid models
Hybrid models have gained increasing attention in long-term load forecasting (LTLF)
due to their ability to combine the strengths of multiple methodologies while
compensating for individual weaknesses. These models often blend machine learning,
fuzzy logic, neural networks, optimization algorithms, or time-series frameworks to
address the challenges of nonlinearity, uncertainty, and temporal dependence. This
section categorizes hybrid models into five main groups based on their core
methodological structures.
5.4.1. Fuzzy-Neural Network-Based Hybrid Models
Fuzzy-neural models combine the uncertainty-handling strength of fuzzy systems
with the learning capabilities of ANNs. Toly Chen [76] proposed a collaborative fuzzy-
neural approach where multiple experts construct fuzzy backpropagation networks
(FBPNs) to generate fuzzy forecasts, which are then aggregated using fuzzy
intersection and defuzzified via a radial basis function (RBF) network. This framework
enables simultaneous prediction of average and peak loads, improving precision by
40% and accuracy by 99% over single models. In Figure 5.4 the procedure of this
proposed model is shown.
Figure 5.4: The procedure of the proposed methodology by Toly Chen [76].

| Long-term load forecasting 87
Similarly, Danladi et al. [77] applied a fuzzy logic system enhanced with ANN
structures to model long-term electricity demand. Their approach incorporates
fuzzified input variables and a rule-based decision-making system that mimics human
reasoning for load behavior, making it suitable for complex environments with vague
and uncertain data. These models offer transparency in reasoning and high
adaptability to varying load patterns but may suffer from increased computational
complexity due to fuzzification and defuzzification stages.
5.4.2. Fuzzy-RNN-based models
Wen et al. [78] introduced a hybrid model called the TS-type recurrent fuzzy neural
network (TS-RFNN), which integrates fuzzy inference mechanisms with recurrent
neural networks. This model is particularly suited for long-term forecasting as it
manages time-dependence through feedback connections and linguistic uncertainty
via Takagi-Sugeno (TS) fuzzy rules. As Figure 5.5 illustrates, the architecture consists
of five layers, including fuzzification, rule evaluation, normalization, consequent
generation, and defuzzification. Experimental results demonstrate that the TS-RFNN
effectively captures the temporal and uncertain characteristics of load data, achieving
higher accuracy than standard RNNs or fuzzy systems alone.
Figure 5.5: Schematic structure of ISO-TS-RBF-RFNN model by Wen et al. [78].

88 | Long-term load forecasting
5.4.3. Fuzzy-SVM and grey system hybrid models
Chen et al. [79] proposed a hybrid model that combines fuzzy support vector machines
(FSVM) with a grey forecasting mechanism that flowchart of the method is shown in
Figure 5.6. The grey system model captures the overall trend in sparse and incomplete
data, while the FSVM provides fine-grained learning of nonlinear patterns. This hybrid
is particularly robust in uncertain or data-deficient environments. By optimizing the
kernel parameters of the SVM under a fuzzy rule base and integrating trend correction
from the grey model, the method improves prediction stability and generalization. It
outperforms single SVM and grey models in terms of MAPE and RMSE,
demonstrating its effectiveness in complex LTLF scenarios.
Figure 5.6: Flow chart of long-term power load grey combination forecast by Chen et
al. [79].

| Long-term load forecasting 89
5.4.4. LSTM-based hybrid deep learning models
Ma et al. [80] developed a deep hybrid architecture that combines PSO, LSTM, and
XGBoost to enhance long-term renewable energy forecasting. As Figure 5.7 illustrates,
in this model, PSO optimizes LSTM’s hyperparameters to avoid manual tuning, while
XGBoost fine-tunes the final predictions by correcting residual errors. The integration
of these methods allows for robust learning from nonlinear and seasonally fluctuating
datasets. Comparative evaluations show that the hybrid outperforms standalone
LSTM and statistical methods in both accuracy and generalization. However, due to
its multi-stage nature, the model requires greater computational resources and more
complex integration steps.
Figure 5.7: Framework for the RES design optimization by Ma et al. [80].
5.4.5. Transformer-based hybrid deep learning models
Tian et al. [81] introduced LDformer, a transformer-based parallel deep neural
network tailored for long-term power forecasting. LDformer fuses Informer (a
lightweight transformer variant), LSTM (for long-range dependencies), convolutional
layers (for local feature extraction), and UniDrop-based attention regularization. Its
architecture enables simultaneous processing of long sequences with reduced
redundancy and computational cost. LDformer excels in robustness and scalability

90 | Long-term load forecasting
across multiple benchmark datasets, consistently outperforming classical RNNs,
LSTMs, and baseline Informer models in terms of RMSE. The key advantage lies in its
ability to retain deep temporal features while mitigating attention overload through
ProbSparse attention mechanisms.
To provide a concise overview of the comparative strengths and limitations of the
reviewed hybrid approaches, Table 5.9 summarizes the key benefits and weaknesses
associated with each model type. This synthesis highlights how different
combinations—ranging from metaheuristic–neural hybrids to transformer-based
architectures—offer distinct advantages in handling long-term load forecasting
challenges such as nonlinearity, uncertainty, and sequence length. The table serves as
a reference point for evaluating trade-offs between accuracy, interpretability,
computational efficiency, and practical applicability in real-world forecasting
scenarios.
Table 5.9: Advantages and disadvantages of hybrid models in LTLF.
Authers Strengths Weaknesses
Robust to sparse data,
Chen et al.[79] handles uncertainty and Complex parameter tuning
trend components
High accuracy, residual
Multi-stage model increases
Ma et al. [80] correction, optimized computation and integration
structure complexity
Collaborative expert
modelling, handles peak Requires defuzzification and
Chen, Toly [76]
and average forecasts multiple iterations
together
Captures temporal
Difficult to scale to high-
Wen et al. [78] uncertainty, rule-based
dimensional inputs
learning
Fast training, strong long-
High model complexity and
Tian et al. [81] range learning, reduced
memory usage
attention redundancy
Transparent rule-base, Limited adaptation if rule
Danladi et al. [77]
effective with vague data base is not comprehensive

| Long-term load forecasting 91
5.5. Summary
Chapter 5 provided a detailed review of state-of-the-art methods used in LTLF,
highlighting their theoretical foundations, practical applications, and relative
strengths and weaknesses. Beginning with statistical approaches such as multiple
linear regression, logistic regression, ARIMA, and SARIMA, the discussion
emphasized their transparency, interpretability, and suitability for stable consumption
environments, while also acknowledging their limitations in modelling nonlinear or
rapidly evolving demand patterns. The chapter then explored the increasing adoption
of machine learning models—including SVR, decision trees, random forests, and
gradient boosting—which offer improved flexibility and accuracy but may lack
explainability. Deep learning methods, such as ANN, MLP, and LSTMs, were shown
to effectively capture complex temporal and nonlinear relationships, especially when
supported by large, high-quality datasets or enhanced through hybridization. Finally,
the chapter examined a diverse array of hybrid models that integrate fuzzy logic,
optimization algorithms, deep learning, and Transformer-based architectures. These
hybrids demonstrate substantial gains in accuracy, adaptability, and robustness—
particularly in scenarios involving long sequences, uncertainty, or sparse data.
However, they also introduce challenges related to model complexity, computational
requirements, and integration costs. The comparative synthesis in tables throughout
this chapter—including Table 5.9 for hybrid models—offers a practical reference for
selecting appropriate forecasting techniques based on system characteristics, data
availability, and planning objectives. Together, these insights provide a strong
foundation for understanding and improving LTLF in evolving power systems.

| Conclusion and future research
92 directions
6
Conclusion and future research
directions
This thesis has undertaken a comprehensive investigation into electricity load
forecasting, focusing particularly on methods suited for LTLF but contextualized
within the broader landscape that includes STLF and MTLF. By systematically
reviewing statistical, machine learning, deep learning, and hybrid methods, the thesis
provides an organized framework to understand when and how each method should
be applied, considering both forecasting horizon and data availability—two of the
most critical dimensions in predictive modelling for power systems.
6.1. Recapitulation of research objectives and
contributions
The research was driven by the increasing demand for accurate and scalable electricity
load forecasting tools amid evolving energy consumption behaviors, grid
decarbonization, and renewable energy integration. The review began by identifying
the practical challenges utilities and planners face in making decisions under
conditions of long-term uncertainty and growing data diversity. Through a layered
analysis of forecasting methods, this thesis contributes:
A classification of methods by time horizon, detailing their strengths and limitations
across short-, medium-, and long-term applications.
A mapping of forecasting techniques to data availability levels, from single households
to national-scale energy systems.
A comparative review of hybrid approaches, which integrate models to balance
accuracy, interpretability, and computational cost.
Visual tools (Figure 6.1 and Figure 6.2) to guide practitioners in selecting suitable
methods based on forecast duration and data granularity.

| Conclusion and future research
93
directions
Figure 6.1: Forecasting horizon classification of different methods.
Figure 6.2: Scalability of forecasting methods based on spatial data availability.

| Conclusion and future research
94 directions
6.2. Strategic alignment between forecasting horizons
and methods
A core finding of this work is that forecasting accuracy and reliability are heavily
dependent on temporal context:
STLF, defined as forecasting within a few minutes to 1 week, is best addressed using
statistical models such as Multiple Linear Regression (MLR), ARIMA/SARIMA, or
simple machine learning techniques like SVR. These methods are interpretable, fast,
and data-efficient—ideal for operational decision-making.
MTLF, spanning 1 week to 1 month, benefits from tree-based models (e.g., Random
Forests, Gradient Boosting Machines) and basic ANNs. These methods offer improved
capacity to capture nonlinearities and complex interactions, useful for demand-side
planning, tariff design, or load shifting strategies.
LTLF, beyond 1 month and up to several decades, requires models capable of handling
system evolution, structural change, and socio-economic influences. Here, deep
learning models such as LSTM and Transformer-based architectures, along with
hybrid models integrating fuzzy logic, metaheuristics, and ensemble learning, show
the best performance. These models can model intricate temporal dynamics and
uncertainties but require large datasets and computational resources.
As shown in Figure 6.1, forecasting methods follow a progression from interpretable
and lightweight models for short durations to more complex and data-hungry models
as the prediction horizon increases.
6.3. Method suitability based on data scale
Another major dimension in model selection is data scale, as detailed in Figure 6.2:
For household-level and building-level applications—such as smart home control or
energy efficiency management—lightweight methods (SVR, decision trees, simple
ANN) are more suitable due to their ability to perform under data-scarce conditions.
District and city-level forecasting, which often includes substation, microgrid, or
municipal planning data, benefits from ML models such as ensemble trees and MLPs
that balance model complexity with interpretability.
For regional and national-level load forecasting—relevant to grid investment, policy
simulation, and energy market design—deep learning and hybrid models are ideal, as
they can process multivariate, longitudinal, and often noisy datasets with greater
fidelity.

| Conclusion and future research
95
directions
This scale-sensitive approach helps align model complexity with data richness,
enhancing both efficiency and performance.
6.4. Implications for practice and policy
The findings of this thesis offer several implications:
Model choice must be context aware. No single technique is optimal across all
conditions. Planners and operators should match forecasting models to their intended
use case—be it short-term operations, medium-term tariff planning, or long-term
infrastructure investment.
Explainability vs. accuracy is a trade-off. Statistical models provide clarity and
confidence for policymakers but may lack precision. Conversely, DL and hybrid
models offer state-of-the-art accuracy but require interpretability enhancements (e.g.,
attention mechanisms, post hoc analysis) for use in regulatory environments.
Data strategy is foundational. Models are only as good as the data they are built upon.
Investment in smart meter infrastructure, high-resolution weather data, and socio-
economic forecasting tools is essential for unleashing the full potential of advanced
forecasting models.
6.5. Limitations and future research directions
While comprehensive, this review is subject to a few limitations: it is based on
published literature and benchmark datasets and as a consequence real-world
constraints such as missing data, organizational capacity, and stakeholder preferences
were not modelled explicitly. Hybrid models are still evolving, and their performance
may vary significantly across datasets and implementations, while probabilistic
forecasting methods—which incorporate uncertainty in output—were only lightly
discussed and could form a valuable extension of this work.
Future research should focus on, for instance, (i) interpretable hybrid models that
combine the accuracy of deep learning with the explainability of statistical approaches,
(ii) transfer learning and meta-learning to reduce the training data burden in regions
or sectors with limited historical data, and (iii) probabilistic and scenario-based LTLF,
which better reflect real-world uncertainty and can support resilient decision-making.
It is worthwhile discussing briefly also Spiking Neural Networks (SNNs), which more
closely mimic the temporal and event-driven processing of biological neurons,
represent a promising frontier for electricity load forecasting. The robustness of
surrogate gradient learning algorithms enables effective training of SNNs despite the
nondifferentiable nature of spike events, as demonstrated by Zenke and Vogels [82].
This makes SNNs well-suited for capturing complex temporal dynamics with sparse

| Conclusion and future research
96 directions
and energy-efficient computations. Although SNNs have been explored for short-term
load forecasting [83], their application to medium- and long-term horizons remains
underdeveloped. Given the growing interest in low-power, real-time, and edge-
deployable AI models in smart grid contexts, future research should investigate SNN
architectures with surrogate gradient training for medium- and long-term load
forecasting tasks. This includes developing benchmark datasets, refining hybrid
models that integrate SNNs with classical deep learning techniques and exploring
hardware implementations to leverage neuromorphic computing advantages.
Such directions could yield forecasting models that balance accuracy, efficiency, and
interpretability, addressing challenges posed by increasing data volume, temporal
complexity, and the need for sustainable computation in evolving power systems.
6.6. Final remarks
In an era where electricity systems are becoming more complex, decentralized, and
data-driven, accurate and adaptive load forecasting is no longer a luxury but a
necessity. This thesis provides a structured lens to evaluate forecasting models, not as
standalone tools but as components of a larger decision-making ecosystem—sensitive
to time, data, purpose, and context. As forecasting continues to evolve with AI, big
data, and climate-aware planning, the frameworks and insights presented here can
serve as a foundation for both academic research and practical implementation in
future-ready power systems.

| Bibliography 97
Bibliography
[1] S. Amoako, F. K. Andoh, and E. E. Asmah, “Household structure and electricity
consumption in Ghana,” Energy Policy, vol. 182, Nov. 2023, doi:
10.1016/j.enpol.2023.113767.
[2] “European Commission,” https://europa.eu/. Accessed: Mar. 18, 2025. [Online].
Available: https://ec.europa.eu/eurostat/statistics-
explained/index.php?title=Energy_consumption_in_households
[3] H. Rafiq, P. Manandhar, E. Rodriguez-Ubinas, J. D. Barbosa, and O. A. Qureshi,
“Analysis of residential electricity consumption patterns utilizing smart-meter
data: Dubai as a case study,” Energy Build, vol. 291, Jul. 2023, doi:
10.1016/j.enbuild.2023.113103.
[4] C. Ragupathi, S. Dhanasekaran, N. Vijayalakshmi, and A. O. Salau, “Prediction
of electricity consumption using an innovative deep energy predictor model for
enhanced accuracy and efficiency,” Energy Reports, vol. 12, pp. 5320–5337, Dec.
2024, doi: 10.1016/j.egyr.2024.11.018.
[5] H. Luo, Y. Zhang, X. Gao, Z. Liu, X. Meng, and X. Yang, “Multi-scale electricity
consumption prediction model based on land use and interpretable machine
learning: A case study of China,” Advances in Applied Energy, vol. 16, p. 100197,
Dec. 2024, doi: 10.1016/j.adapen.2024.100197.
[6] D. Peteleaza et al., “Electricity consumption forecasting for sustainable smart
cities using machine learning methods,” Internet of Things (Netherlands), vol. 27,
Oct. 2024, doi: 10.1016/j.iot.2024.101322.
[7] Z. Wang, T. Hong, H. Li, and M. Ann Piette, “Predicting city-scale daily
electricity consumption using data-driven models,” Advances in Applied Energy,
vol. 2, May 2021, doi: 10.1016/j.adapen.2021.100025.
[8] S. Palaniappan, S. Karuppannan, and D. Velusamy, “Categorization of Indian
residential consumers electrical energy consumption pattern using clustering
and classification techniques,” Energy, vol. 289, Feb. 2024, doi:
10.1016/j.energy.2023.129992.
[9] J. Adinkrah et al., “Artificial intelligence-based strategies for sustainable energy
planning and electricity demand estimation: A systematic review,” Mar. 01,
2025, Elsevier Ltd. doi: 10.1016/j.rser.2024.115161.
[10] A. Najeeb, S. Sridharan, A. B. Rao, S. B. Agnihotri, and V. Mishra, “Determinants
of residential electricity consumption in South, East and South East Asia: A
systematic review,” Jul. 01, 2024, Elsevier Ltd. doi: 10.1016/j.rser.2024.114400.

98 | Bibliography
[11] C. T. Nguyen, H. Nguyen, and A. D. Sakti, “Seasonal characteristics of outdoor
thermal comfort and residential electricity consumption: A Snapshot in Bangkok
Metropolitan Area,” Remote Sens Appl, vol. 33, Jan. 2024, doi:
10.1016/j.rsase.2023.101106.
[12] Y. Li et al., “Efficient predictive control strategy for mitigating the overlap of EV
charging demand and residential load based on distributed renewable energy,”
Renew Energy, vol. 240, Feb. 2025, doi: 10.1016/j.renene.2024.122154.
[13] F. Lazzari et al., “User behaviour models to forecast electricity consumption of
residential customers based on smart metering data,” Energy Reports, vol. 8, pp.
3680–3691, Nov. 2022, doi: 10.1016/j.egyr.2022.02.260.
[14] Y. Huang, Z. Yao, and Q. Xu, “Classification model of electricity consumption
behavior based on sparse denoising autoencoder feature dimensionality
reduction and spectral clustering,” International Journal of Electrical Power and
Energy Systems, vol. 158, Jul. 2024, doi: 10.1016/j.ijepes.2024.109960.
[15] F. Yu, Q. Yue, A. Yunianta, and H. M. A. Aljahdali, “A novel hybrid deep
correction approach for electrical load demand prediction,” Sustain Cities Soc,
vol. 74, Nov. 2021, doi: 10.1016/j.scs.2021.103161.
[16] X. Deng et al., “Bagging–XGBoost algorithm based extreme weather
identification and short-term load forecasting model,” Energy Reports, vol. 8, pp.
8661–8674, Nov. 2022, doi: 10.1016/j.egyr.2022.06.072.
[17] M. Bilgili and E. Pinar, “Gross electricity consumption forecasting using LSTM
and SARIMA approaches: A case study of Türkiye,” Energy, vol. 284, Dec. 2023,
doi: 10.1016/j.energy.2023.128575.
[18] D. Katić, H. Krstić, I. Ištoka Otković, and H. Begić Juričić, “Comparing multiple
linear regression and neural network models for predicting heating energy
consumption in school buildings in the Federation of Bosnia and Herzegovina,”
Journal of Building Engineering, vol. 97, Nov. 2024, doi: 10.1016/j.jobe.2024.110728.
[19] H. Nano, S. New, A. Cohen, and B. Ramachandran, “Chapter 16 - Load
forecasting using multiple linear regression with different calendars,” in
Distributed Energy Resources in Microgrids, R. K. Chauhan and K. Chauhan, Eds.,
Academic Press, 2019, pp. 405–417. doi: https://doi.org/10.1016/B978-0-12-
817774-7.00016-8.
[20] G. Dudek, “Pattern-based local linear regression models for short-term load
forecasting,” Electric Power Systems Research, vol. 130, pp. 139–147, Jan. 2016, doi:
10.1016/j.epsr.2015.09.001.
[21] J. C. Nsangou, J. Kenfack, U. Nzotcha, P. S. Ngohe Ekam, J. Voufo, and T. T.
Tamo, “Explaining household electricity consumption using quantile

| Bibliography 99
regression, decision tree and artificial neural network,” Energy, vol. 250, Jul.
2022, doi: 10.1016/j.energy.2022.123856.
[22] A. Gellert, U. Fiore, A. Florea, R. Chis, and F. Palmieri, “Forecasting Electricity
Consumption and Production in Smart Homes through Statistical Methods,”
Sustain Cities Soc, vol. 76, Jan. 2022, doi: 10.1016/j.scs.2021.103426.
[23] N. M. M. Bendaoud, N. Farah, and S. Ben Ahmed, “Applying load profiles
propagation to machine learning based electrical energy forecasting,” Electric
Power Systems Research, vol. 203, Feb. 2022, doi: 10.1016/j.epsr.2021.107635.
[24] A. Haque and S. Rahman, “Short-term electrical load forecasting through
heuristic configuration of regularized deep neural network,” Appl Soft Comput,
vol. 122, Jun. 2022, doi: 10.1016/j.asoc.2022.108877.
[25] Y. Zhang, B. K. Teoh, M. Wu, J. Chen, and L. Zhang, “Data-driven estimation of
building energy consumption and GHG emissions using explainable artificial
intelligence,” Energy, vol. 262, Jan. 2023, doi: 10.1016/j.energy.2022.125468.
[26] M. S. Hasan, M. Tarequzzaman, M. Moznuzzaman, and M. A. Ahad Juel,
“Prediction of energy consumption in four sectors using support vector
regression optimized with genetic algorithm,” Heliyon, vol. 11, no. 2, Jan. 2025,
doi: 10.1016/j.heliyon.2025.e41765.
[27] M. Zhou, J. Yu, F. Sun, and M. Wang, “Forecasting of short term electric power
consumption for different types buildings using improved transfer learning: A
case study of primary school in China,” Journal of Building Engineering, vol. 78,
Nov. 2023, doi: 10.1016/j.jobe.2023.107618.
[28] R. Pascanu, T. Mikolov, and Y. Bengio, “On the difficulty of training Recurrent
Neural Networks,” Nov. 2012, [Online]. Available:
http://arxiv.org/abs/1211.5063
[29] C. Wang, X. Li, Y. Shi, W. Jiang, Q. Song, and X. Li, “Load forecasting method
based on CNN and extended LSTM,” Energy Reports, vol. 12, pp. 2452–2461, Dec.
2024, doi: 10.1016/j.egyr.2024.07.030.
[30] G. Memarzadeh and F. Keynia, “Short-term electricity load and price forecasting
by a new optimal LSTM-NN based prediction algorithm,” Electric Power Systems
Research, vol. 192, p. 106995, Mar. 2021, doi: 10.1016/j.epsr.2020.106995.
[31] X. Guo, Q. Zhao, D. Zheng, Y. Ning, and Y. Gao, “A short-term load forecasting
model of multi-scale CNN-LSTM hybrid neural network considering the real-
time electricity price,” Energy Reports, vol. 6, pp. 1046–1053, 2020, doi:
https://doi.org/10.1016/j.egyr.2020.11.078.
[32] W. Guo, S. Liu, L. Weng, and X. Liang, “Power Grid Load Forecasting Using a
CNN-LSTM Network Based on a Multi-Modal Attention Mechanism,” Applied
Sciences (Switzerland), vol. 15, no. 5, Mar. 2025, doi: 10.3390/app15052435.

100 | Bibliography
[33] C. M. Liapis, A. Karanikola, and S. Kotsiantis, “Energy Load Forecasting:
Investigating Mid-Term Predictions with Ensemble Learners,” pp. 343–355,
2022, doi: 10.1007/978-3-031-08333-4_28ï.
[34] Z. Tian, W. Liu, W. Jiang, and C. Wu, “CNNs-Transformer based day-ahead
probabilistic load forecasting for weekends with limited data availability,”
Energy, vol. 293, p. 130666, 2024, doi:
https://doi.org/10.1016/j.energy.2024.130666.
[35] J. Wang, W. Huang, Y. Ding, Y. Dang, and L. Ye, “Forecasting the electric power
load based on a novel prediction model coupled with accumulative time-delay
effects and periodic fluctuation characteristics,” Energy, vol. 317, p. 134518, 2025,
doi: https://doi.org/10.1016/j.energy.2025.134518.
[36] A. Mathew, R. Chikte, S. K. Sadanandan, S. Abdelaziz, S. Ijaz, and T. Ghaoud,
“Medium-term feeder load forecasting and boosting peak accuracy prediction
using the PWP-XGBoost model,” Electric Power Systems Research, vol. 237, p.
111051, 2024, doi: https://doi.org/10.1016/j.epsr.2024.111051.
[37] Z. Peng and X. Yang, “Short- and medium-term power load forecasting model
based on a hybrid attention mechanism in the time and frequency domains,”
Expert Syst Appl, vol. 278, p. 127329, 2025, doi:
https://doi.org/10.1016/j.eswa.2025.127329.
[38] Candidus. U. Eya, A. O. Salau, S. L. Braide, and O. D. Chigozirim, “Improved
Medium Term Approach for Load Forecasting of Nigerian Electricity Network
Using Artificial Neuro-Fuzzy Inference System: A Case Study of University of
Nigeria, Nsukka,” Procedia Comput Sci, vol. 218, pp. 2585–2593, 2023, doi:
https://doi.org/10.1016/j.procs.2023.01.232.
[39] S. Karamolegkos and D. E. Koulouriotis, “Advancing short-term load
forecasting with decomposed Fourier ARIMA: A case study on the Greek energy
market,” Energy, vol. 325, Jun. 2025, doi: 10.1016/j.energy.2025.135854.
[40] S. Wang, S. Wang, and D. Wang, “Combined probability density model for
medium term load forecasting based on quantile regression and kernel density
estimation,” Energy Procedia, vol. 158, pp. 6446–6451, 2019, doi:
https://doi.org/10.1016/j.egypro.2019.01.169.
[41] C. Xu, Y. Sun, A. Du, and D. Gao, “Quantile regression based probabilistic
forecasting of renewable energy generation and building electrical load: A state
of the art review,” Journal of Building Engineering, vol. 79, p. 107772, 2023, doi:
https://doi.org/10.1016/j.jobe.2023.107772.
[42] F. Zhu and G. Wu, “Load forecasting of the power system: An investigation
based on the method of random forest regression,” Energy Engineering: Journal of
the Association of Energy Engineering, vol. 118, no. 6, pp. 1703–1712, 2021, doi:
10.32604/EE.2021.015602.

| Bibliography 101
[43] E. Royal, S. Bandyopadhyay, A. Newman, Q. Huang, and P. C. Tabares-Velasco,
“A statistical framework for district energy long-term electric load forecasting,”
Appl Energy, vol. 384, p. 125445, 2025, doi:
https://doi.org/10.1016/j.apenergy.2025.125445.
[44] F. Dinmohammadi, Y. Han, and M. Shafiee, “Predicting Energy Consumption in
Residential Buildings Using Advanced Machine Learning Algorithms,” Energies
(Basel), vol. 16, no. 9, May 2023, doi: 10.3390/en16093748.
[45] Y. Dong, X. Ma, and T. Fu, “Electrical load forecasting: A deep learning approach
based on K-nearest neighbors,” Appl Soft Comput, vol. 99, p. 106900, 2021, doi:
https://doi.org/10.1016/j.asoc.2020.106900.
[46] S. ur R. Khan et al., “Enhanced Machine-Learning Techniques for Medium-Term
and Short-Term Electric-Load Forecasting in Smart Grids,” Energies (Basel), vol.
16, no. 1, Jan. 2023, doi: 10.3390/en16010276.
[47] G. Dudek and P. Pełka, “Pattern Similarity-based Machine Learning Methods
for Mid-term Load Forecasting: A Comparative Study,” Mar. 2020, [Online].
Available: http://arxiv.org/abs/2003.01475
[48] R. Wazirali, E. Yaghoubi, M. S. S. Abujazar, R. Ahmad, and A. H. Vakili, “State-
of-the-art review on energy and load forecasting in microgrids using artificial
neural networks, machine learning, and deep learning techniques,” Dec. 01,
2023, Elsevier Ltd. doi: 10.1016/j.epsr.2023.109792.
[49] M. Ghiassi, D. K. Zimbra, and H. Saidane, “Medium term system load
forecasting with a dynamic artificial neural network model,” Electric Power
Systems Research, vol. 76, no. 5, pp. 302–316, 2006, doi:
https://doi.org/10.1016/j.epsr.2005.06.010.
[50] T. Yalcinoz and U. Eminoglu, “Short term and medium term power distribution
load forecasting by neural networks,” Energy Convers Manag, vol. 46, no. 9, pp.
1393–1405, 2005, doi: https://doi.org/10.1016/j.enconman.2004.07.005.
[51] S. Muzaffar and A. Afshari, “Short-term load forecasts using LSTM networks,”
in Energy Procedia, Elsevier Ltd, 2019, pp. 2922–2927. doi:
10.1016/j.egypro.2019.01.952.
[52] J. W. Chan and C. K. Yeo, “A Transformer based approach to electricity load
forecasting,” Electricity Journal, vol. 37, no. 2, Mar. 2024, doi:
10.1016/j.tej.2024.107370.
[53] G. Dudek, P. Pełka, and S. Smyl, “A Hybrid Residual Dilated LSTM end
Exponential Smoothing Model for Mid-Term Electric Load Forecasting,” Mar.
2020, [Online]. Available: http://arxiv.org/abs/2004.00508
[54] T. González Grandón, J. Schwenzer, T. Steens, and J. Breuing, “Electricity
demand forecasting with hybrid classical statistical and machine learning

102 | Bibliography
algorithms: Case study of Ukraine,” Appl Energy, vol. 355, Feb. 2024, doi:
10.1016/j.apenergy.2023.122249.
[55] Z. Wang, Z. Chen, Y. Yang, C. Liu, X. Li, and J. Wu, “A hybrid Autoformer
framework for electricity demand forecasting,” Energy Reports, vol. 9, pp. 3800–
3812, Dec. 2023, doi: 10.1016/j.egyr.2023.02.083.
[56] G. Antonesi, T. Cioara, I. Anghel, I. Papias, V. Michalakopoulos, and E. Sarmas,
“Hybrid transformer model with liquid neural networks and learnable
encodings for buildings’ energy forecasting,” Energy and AI, vol. 20, May 2025,
doi: 10.1016/j.egyai.2025.100489.
[57] G. Yıldız Doğan, A. Aksoy, and N. Öztürk, “A Hybrid Deep Learning Model to
Estimate the Future Electricity Demand of Sustainable Cities,” Sustainability
(Switzerland), vol. 16, no. 15, Aug. 2024, doi: 10.3390/su16156503.
[58] S. Zhang, R. Chen, J. Cao, and J. Tan, “A CNN and LSTM-based multi-task
learning architecture for short and medium-term electricity load forecasting,”
Electric Power Systems Research, vol. 222, p. 109507, 2023, doi:
https://doi.org/10.1016/j.epsr.2023.109507.
[59] L. Wang, X. Wang, and Z. Zhao, “Mid-term electricity demand forecasting using
improved multi-mode reconstruction and particle swarm-enhanced support
vector regression,” Energy, vol. 304, Sep. 2024, doi: 10.1016/j.energy.2024.132021.
[60] X. Huang, Y. Han, J. Yan, and X. Zhou, “Hybrid forecasting model of building
cooling load based on EMD-LSTM-Markov algorithm,” Energy Build, vol. 321,
Oct. 2024, doi: 10.1016/j.enbuild.2024.114670.
[61] M. J. A. Shohan, M. O. Faruque, and S. Y. Foo, “Forecasting of Electric Load
Using a Hybrid LSTM-Neural Prophet Model,” Energies (Basel), vol. 15, no. 6,
Mar. 2022, doi: 10.3390/en15062158.
[62] R. Feng, J. Wang, W. Wu, S. Liu, A. Liu, and S. Xie, “Saturated load forecasting
based on improved logistic regression and affinity propagation,” Electric Power
Systems Research, vol. 237, p. 110953, 2024, doi:
https://doi.org/10.1016/j.epsr.2024.110953.
[63] V. Kumar, R. K. Mandal, and S. Rai, “Smart metered distribution system load
forecasting using statistical approaches,” in 2024 4th International Conference on
Emerging Frontiers in Electrical and Electronic Technologies (ICEFEET), 2024, pp. 1–
4. doi: 10.1109/ICEFEET64463.2024.10866475.
[64] A. Kumar Dubey, A. Kumar, V. García-Díaz, A. Kumar Sharma, and K.
Kanhaiya, “Study and analysis of SARIMA and LSTM in forecasting time series
data,” Sustainable Energy Technologies and Assessments, vol. 47, p. 101474, 2021,
doi: https://doi.org/10.1016/j.seta.2021.101474.

| Bibliography 103
[65] J. Wang, L. Li, D. Niu, and Z. Tan, “An annual load forecasting model based on
support vector regression with differential evolution algorithm,” Appl Energy,
vol. 94, pp. 65–70, 2012, doi: https://doi.org/10.1016/j.apenergy.2012.01.010.
[66] T. Hu, “Comparison of long-term load forecasting methods for air conditioning
system of a large building,” in 2021 China Automation Congress (CAC), 2021, pp.
4491–4496. doi: 10.1109/CAC53003.2021.9728514.
[67] M.-R. Kazemzadeh, A. Amjadian, and T. Amraee, “A hybrid data mining driven
algorithm for long term electric peak load and energy demand forecasting,”
Energy, vol. 204, p. 117948, 2020, doi:
https://doi.org/10.1016/j.energy.2020.117948.
[68] H. Sangrody, N. Zhou, S. Tutun, B. Khorramdel, M. Motalleb, and M. Sarailoo,
Long Term Forecasting using Machine Learning Methods. 2018. doi:
10.1109/PECI.2018.8334980.
[69] G. Ozdemir, “Long-term electrical energy demand forecasting by using artificial
intelligence/machine learning techniques,” Electrical Engineering, vol. 106, no. 4,
pp. 5229–5251, 2024, doi: 10.1007/s00202-024-02364-1.
[70] J. Faraji, H. Hashemi-Dezaki, and A. Ketabi, “Multi-year load growth-based
optimal planning of grid-connected microgrid considering long-term load
demand forecasting: A case study of Tehran, Iran,” Sustainable Energy
Technologies and Assessments, vol. 42, Dec. 2020, doi: 10.1016/j.seta.2020.100827.
[71] J. H. Kim, B. S. Lee, and C. H. Kim, “A Study on the development of long-term
hybrid electrical load forecasting model based on MLP and statistics using
massive actual data considering field applications,” Electric Power Systems
Research, vol. 221, Aug. 2023, doi: 10.1016/j.epsr.2023.109415.
[72] Z. Q. Dai, J. Li, Y. J. Cao, and Y. X. Zhang, “SALSTM: segmented self-attention
long short-term memory for long-term forecasting,” Journal of Supercomputing,
vol. 81, no. 1, Jan. 2025, doi: 10.1007/s11227-024-06493-z.
[73] T. U. Go, Y. J. Go, J. H. Im, and D. Lee, “Long-Term Demand Forecasting: Novel
Decomposition-Linear Exponential-Smoothing Algorithm with Long Short-
Term Memory,” Journal of Electrical Engineering and Technology, 2025, doi:
10.1007/s42835-025-02226-1.
[74] T. Quanwei, X. Guijun, and X. Wenju, “Cakformer: Transformer model for long-
term heat load forecasting based on Cauto-correlation and KAN,” Energy, vol.
324, p. 135460, 2025, doi: https://doi.org/10.1016/j.energy.2025.135460.
[75] Y. Yang, Y. Gao, H. Zhou, J. Wu, S. Gao, and Y.-G. Wang, “Multi-Granularity
Autoformer for long-term deterministic and probabilistic power load
forecasting,” Neural Networks, vol. 188, p. 107493, 2025, doi:
https://doi.org/10.1016/j.neunet.2025.107493.

104 | Bibliography
[76] T. Chen, “A collaborative fuzzy-neural approach for long-term load forecasting
in Taiwan,” Comput Ind Eng, vol. 63, no. 3, pp. 663–670, Nov. 2012, doi:
10.1016/j.cie.2011.06.003.
[77] D. Ali, M. Yohanna, M. I. Puwu, and B. M. Garkida, “Long-term load forecast
modelling using a fuzzy logic approach,” Pacific Science Review A: Natural Science
and Engineering, vol. 18, no. 2, pp. 123–127, Jul. 2016, doi:
10.1016/j.psra.2016.09.011.
[78] Z. Wen, L. Xie, Q. Fan, and H. Feng, “Long term electric load forecasting based
on TS-type recurrent fuzzy neural network model,” Electric Power Systems
Research, vol. 179, Feb. 2020, doi: 10.1016/j.epsr.2019.106106.
[79] Y. Chen, C. Xiao, S. Yang, Y. Yang, and W. Wang, “Research on long term power
load grey combination forecasting based on fuzzy support vector machine,”
Computers and Electrical Engineering, vol. 116, May 2024, doi:
10.1016/j.compeleceng.2024.109205.
[80] W. Ma, W. Wu, S. F. Ahmed, and G. Liu, “Techno-economic feasibility of
utilizing electrical load forecasting in microgrid optimization planning,”
Sustainable Energy Technologies and Assessments, vol. 73, Jan. 2025, doi:
10.1016/j.seta.2024.104135.
[81] R. Tian, X. Li, Z. Ma, Y. Liu, J. Wang, and C. Wang, “LDformer: a parallel neural
network model for long-term power forecasting,” Frontiers of Information
Technology and Electronic Engineering, vol. 24, no. 9, pp. 1287–1301, Sep. 2023, doi:
10.1631/FITEE.2200540.
[82] F. Zenke and T. P. Vogels, “The Remarkable Robustness of Surrogate Gradient
Learning for Instilling Complex Function in Spiking Neural Networks,” Neural
Comput, vol. 33, no. 4, pp. 899–925, Mar. 2021, doi: 10.1162/neco_a_01367.
[83] S. Kulkarni, S. P. Simon, and K. Sundareswaran, “A spiking neural network
(SNN) forecast engine for short-term electrical load forecasting,” Appl Soft
Comput, vol. 13, no. 8, pp. 3628–3635, 2013, doi:
https://doi.org/10.1016/j.asoc.2013.04.007.

105
List of Figures
Figure 1.1: Electricity consumption by sectors (GWh) [1]. ................................................ 1
Figure 1.2: Benefits of electricity consumption prediction [4] .......................................... 2
Figure 2.1: Load forecasting time horizontal. ...................................................................... 4
Figure 2.2: Key factors affecting load forecasting. .............................................................. 5
Figure 3.1: SVR model. ......................................................................................................... 20
Figure 3.2: Tree-based model. .............................................................................................. 22
Figure 3.3: Feedforward and backpropagation architecture of ANN. .......................... 30
Figure 3.4: Schematic diagram of the LSTM [29]. ............................................................. 33
Figure 3.5: Proposed model of GA-optimized SVR [26]. ................................................. 36
Figure 3.6: Framework of extreme weather identification and STLF [16]. ................... 38
Figure 3.7: A schematic diagram of a CNN-LSTM network based on a multi-modal
attention mechanism [32]. .................................................................................................... 39
Figure 3.8: Flow chart of the deep learning framework [34]. .......................................... 41
Figure 4.1: Architecture of XGBoost model [36]. .............................................................. 51
Figure 4.2: Framework of the proposed interval forecasting model and principles of
NSGA-II, KNN, DBN and modified KDE [45]. ................................................................. 56
Figure 4.3: Block diagram of the ETS+RD-LSTM forecasting system [53]. ................... 65
Figure 4.4: The whole structure of HAFF [55]. .................................................................. 66
Figure 4.5: The architecture of the proposed hybrid model by Lei Wang et al [59]. ... 68
Figure 4.6: Block diagram of proposed hybrid model by Shohan et al [61]. ................ 69
Figure 5.1: Feedforward procedure of neural network for MLP by Kim et al. [71]. .... 82
Figure 5.2: The self-attention model and its computational process by Dai et al. [72].
.................................................................................................................................................. 83
Figure 5.3: The multi-granularity Autoformer by Yang et al. [75]. ................................ 85
Figure 5.4: The procedure of the proposed methodology by Toly Chen [76]. ............. 86
Figure 5.5: Schematic structure of ISO-TS-RBF-RFNN model by Wen et al. [78]. ....... 87

106 | List of Figures
Figure 5.6: Flow chart of long-term power load grey combination forecast by Chen et
al. [79]. ..................................................................................................................................... 88
Figure 5.7: Framework for the RES design optimization by Ma et al. [80]. .................. 89
Figure 6.1: Forecasting horizon classification of different methods. ............................. 93
Figure 6.2: Scalability of forecasting methods based on spatial data availability........ 93

107
List of Tables
Table 2.1: Common error metrics used in the load forecasting literature. .................... 12
Table 3.1: Strengths and limitations of regression methods in STLF. ............................ 17
Table 3.2: Strengths and limitations of ARIMA and SARIMA methods in STLF. ....... 19
Table 3.3: Strengths and limitations of SVR method in STLF. ........................................ 22
Table 3.4: Strengths and Limitations of Tree-Based Methods in STLF. ......................... 26
Table 3.5: Strengths and limitations of k-NN method in STLF. ..................................... 27
Table 3.6: Strengths and limitations of ANNs in STLF. ................................................... 31
Table 3.7: Strengths and limitations of RNNs and LSTMs in STLF. .............................. 34
Table 3.8: Strengths and Limitations of Transformer-Based Models in STLF. ............. 35
Table 3.9: Benefits of Hybrid models in STLF. .................................................................. 42
Table 4.1: Strengths and limitations of regression methods in MTLF. .......................... 47
Table 4.2: Strengths and limitations of ARIMA and SARIMA in MTLF. ...................... 49
Table 4.3: Advantages and disadvantages of Tree-based models in MTLF. ................ 54
Table 4.4: Advantages and disadvantages of K-NN in MTLF. ....................................... 57
Table 4.5: Advantages and disadvantages of ANN in MTLF. ........................................ 60
Table 4.6: Advantages and disadvantages of RNN and LSTM in MTLF. ..................... 62
Table 4.7: Advantages and disadvantages of transformer-based models in MTLF. ... 64
Table 4.8: Benefits and weakness of hybrid models in MTLF. ....................................... 69
Table 5.1: Advantages and disadvantages of regression -based models in LTLF. ...... 74
Table 5.2: Advantages and disadvantages of ARIMA and SARIMA methods in LTLF.
.................................................................................................................................................. 76
Table 5.3: Advantages and disadvantages of SVR method in LTLF. ............................. 78
Table 5.4: Advantages and disadvantages of tree-based models in LTLF. ................... 79
Table 5.5: Advantages and disadvantages of ANN model in LTLF. ............................. 80
Table 5.6: Advantages and disadvantages of MLP model in LTLF. .............................. 82
Table 5.7: Advantages and disadvantages of LSTM model in LTLF. ............................ 84

108 | List of Tables
Table 5.8: Advantages and Disadvantages of Transformer-based models in LTLF. ... 85
Table 5.9: Advantages and disadvantages of hybrid models in LTLF. ......................... 90

109
Acknowledgments
I would like to express my deepest gratitude to my supervisors, Prof. Samuele Grillo,
and Prof. Daniele Linaro and for their invaluable guidance, constructive feedback, and
continuous support throughout the course of this thesis. Their expertise and
encouragement have greatly shaped the quality and direction of my research.
I also extend my thanks to the faculty and staff of the Department of Electronics,
Information and Bioengineering at Politecnico Di Milano for providing a stimulating
academic environment and essential resources.
Finally, I am deeply grateful to my family and friends for their unwavering
encouragement, patience, and love, which sustained me throughout this academic
journey.