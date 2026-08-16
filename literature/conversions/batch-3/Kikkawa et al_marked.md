---
conversion_metadata:
  converted_at: "2026-07-21T13:47:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kikkawa et al.pdf"
  source_pdf_sha256: "ff48dbed8a15814d620abb2aa571d6b4a26669a391b39ee6d1d079d6155c8246"
  page_count: 39
  markdown_char_count: 205703
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Kikkawa, Aiko; Gaspar, Raymond; Kim, Kijin; Mariasingham, Mahinthan J.; Zamora,
Christian Marvin

Working Paper
Measuring the contribution of international remittances
to household expenditures and economic output: A micro-
macro analysis for the Philippines

ADB Economics Working Paper Series, No. 714

Provided in Cooperation with:
Asian Development Bank (ADB), Manila

Suggested Citation: Kikkawa, Aiko; Gaspar, Raymond; Kim, Kijin; Mariasingham, Mahinthan J.;
Zamora, Christian Marvin (2024) : Measuring the contribution of international remittances to
household expenditures and economic output: A micro-macro analysis for the Philippines, ADB
Economics Working Paper Series, No. 714, Asian Development Bank (ADB), Manila,
https://doi.org/10.22617/WPS240025-2

This Version is available at:
https://hdl.handle.net/10419/298160

Standard-Nutzungsbedingungen:

Terms of use:

Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen
Zwecken und zum Privatgebrauch gespeichert und kopiert werden.

Documents in EconStor may be saved and copied for your personal
and scholarly purposes.

Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich
machen, vertreiben oder anderweitig nutzen.

You are not to copy documents for public or commercial purposes, to
exhibit the documents publicly, to make them publicly available on the
internet, or to distribute or otherwise use the documents in public.

Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten,
gelten abweichend von diesen Nutzungsbedingungen die in der dort
genannten Lizenz gewährten Nutzungsrechte.

If the documents have been made available under an Open Content
Licence (especially Creative Commons Licences), you may exercise
further usage rights as specified in the indicated licence.

https://creativecommons.org/licenses/by/3.0/igo/

---

<!-- PAGE 2 -->

Measuring the Contribution of International Remittances  
to Household Expenditures and Economic Output
A Micro–Macro Analysis for the Philippines

This study assesses the simultaneous contribution of international remittance income reported by recipient 
households to the overall economy of the Philippines by integrating micro data and macro simulation based 
on an input–output framework. It finds that remittance-driven household expenditures and investments 
contributed 3.5% of the country’s total output, 3.4% of the gross domestic product, and 3.7% of the total 
employment in 2018. Industries that received the bulk of remittances in the form of final consumption are 
manufacturing, agriculture, and wholesale and retail trade.

About the Asian Development Bank

ADB is committed to achieving a prosperous, inclusive, resilient, and sustainable Asia and the Pacific,  
while sustaining its efforts to eradicate extreme poverty. Established in 1966, it is owned by 68 members  
—49 from the region. Its main instruments for helping its developing member countries are policy dialogue, 
loans, equity investments, guarantees, grants, and technical assistance.

MEASURING THE CONTRIBUTION 
OF INTERNATIONAL REMITTANCES 
TO HOUSEHOLD EXPENDITURES 
AND ECONOMIC OUTPUT 
A MICRO–MACRO ANALYSIS FOR THE PHILIPPINES

Aiko Kikkawa, Raymond Gaspar, Kijin Kim, Mahinthan J. Mariasingham,  
and Christian Marvin Zamora

NO. 714

February 2024

ADB ECONOMICS
WORKING PAPER SERIES

---

<!-- PAGE 3 -->

ADB Economics Working Paper Series

Measuring the Contribution of International Remittances  
to Household Expenditures and Economic Output:  
A Micro–Macro Analysis for the Philippines

Aiko Kikkawa, Raymond Gaspar,  
Kijin Kim, Mahinthan J. Mariasingham,  
and Christian Marvin Zamora

No. 714  |  February 2024

The ADB Economics Working Paper Series 
presents research in progress to elicit comments 
and encourage debate on development issues 
in Asia and the Pacific. The views expressed 
are those of the authors and do not necessarily 
reflect the views and policies of ADB or 
its Board of Governors or the governments 
they represent.

Aiko Kikkawa (akikkawa@adb.org) and Kijin Kim 
(kijinkim@adb.org) are senior economists; Mahinthan 
J. Mariasingham (mmariasingham@adb.org) is a senior 
statistician; and Raymond Gaspar (rgaspar.consultant@
adb.org) and Christian Marvin Zamora (czamora.
consultant@adb.org) are consultants at the Economic 
Research and Development Impact Department,  
Asian Development Bank.

---

<!-- PAGE 4 -->

Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)

© 2024 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org

Some rights reserved. Published in 2024.

ISSN 2313-6537 (print), 2313-6545 (electronic)
Publication Stock No. WPS240025-2
DOI: http://dx.doi.org/10.22617/WPS240025-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies 
of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any 
consequence of their use. The mention of specific companies or products of manufacturers does not imply that they 
are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area, or by using the term “country” 
in this publication, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)  
https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound 
by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions 
and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed 
to another source, please contact the copyright owner or publisher of that source for permission to reproduce it.  
ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish 
to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use 
the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

Notes: 
In this publication, “P” refers to Philippine pesos and “$” refers to United States dollars. 
ADB recognizes “China” as the People’s Republic of China, “Kyrgyzstan” as the Kyrgyz Republic,  
and “Vietnam” as Viet Nam.

---

<!-- PAGE 5 -->

ABSTRACT

The macroeconomic studies that assess the contribution of international remittances to the origin 
countries of migrants use a different definition of remittances than the microeconomic literature 
that  examines  the  impact  at  the  household  and  community  levels.  This  study  overcomes  this 
difference in definition by integrating household expenditure data into the input-output analysis. 
Using the 2018 Family Income and Expenditure Surveys (FIES) of the Philippines, we find that 
remittance-financed household consumption and investment totaled ₱742.2 billion ($14.1 billion) 
and contributed 3.5% of the country’s total output, 3.4% of gross domestic product (GDP), and 
3.7%  of  total  employment  in  2018.  We  note  that  the  largest  value  added  is  accruing  to  the 
manufacturing sector as it accounts for more than a third of remittance recipients’ spending basket 
followed by the trade and agriculture, forestry, and fisheries sectors, which are closely linked to 
the manufacturing industry. The international remittances income reported by households is less 
than half (43.8%) of the ₱1.7 trillion ($32.2 billion) aggregate international remittances reported 
by the central bank in the same year based on the balance of payments definition.

Keywords: international remittance, household expenditure, micro–macro analysis, Philippines

JEL codes: F24, C67, D12

_______________________

The authors would also like to acknowledge the contribution of the other members of the ADB Statistics 
and  Data  Innovation  team:  Elyssa  Mariel  Mores,  Julian  Thomas  Alvarez,  Arushi  Gupta,  and  Mimika 
Mukherjee.

---

<!-- PAGE 6 -->

1.  Introduction

In 2022, about $350 billion worth of international remittances flowed to developing economies in 
Asia.1 The economic contribution of remittances, commonly measured by their relative share of a 
country’s  gross  domestic  product  (GDP),  is  substantial  in  the  major  migrant  source  countries, 
including Nepal (23%), the Philippines (9%), Pakistan (8%),  and many Pacific countries such as 
Tonga (44%), and therefore plays an important role in advancing economic development.

Remittances largely go to migrants’ families, supporting their consumption and sometimes their 
investment activities. Given the continued inflow of remittances to developing countries, there is 
a  large  body  of  empirical  literature  that  examines  its  short-  and  long-term  effects  on  recipient 
families’ poverty status, savings and investment patterns, and human capital development. The 
impact of remittances is also well studied at the aggregate level, with links to national output and 
growth as well as economic cycles and other macroeconomic fundamentals.

Evidence from the microeconomic literature suggests that international remittances help smooth 
household  consumption  of  basic  foods  and  other  essentials,  improving  the  welfare  and  living 
conditions  of  migrant  families  (e.g.,  Awan  et  al.  2017;  Acosta,  Fajnzylber,  and  Lopez  2007; 
Mezger  and  Beauchemin  2010;  and  Woodruff  and  Zenteno  2007).  Remittances  also  flow  into 
children’s  education  and  family  businesses,  increasing  long-term  household  productivity  (e.g., 
Yang 2008; Cox Edwards and Ureta 2003; Gibson et al. 2019). There is an equally large body of 
macroeconomic literature that examines the impact of remittances  on overall economic growth 
(e.g., Meyer and Shera 2017; Giuliano and Ruiz-Arranz 2009; and Cooray 2012), poverty (e.g., 
Ahmed, Sugiyarto, and Jha 2010; Yoshino, Taghizadeh-Hesary, and Otsuka 2017; and Adams 
and Page 2005), and other economic fundamentals (e.g., Ratha 2005).

In  general, microeconomic  and  macroeconomic  literature complement  each  other to  provide  a 
comprehensive  assessment  of  the  impact  of  remittances  on  migrants’  households  and 
communities, as well as on the overall economy of countries of origin. However, caution should 
be  exercised  when  comparing  the  two  sets  of  literature,  as  the  definition  and  data  source  for 
international remittances differ significantly. In micro-level studies, remittances refer to the amount 
of income households report receiving from abroad, whether in cash or in kind. At the macro level, 
by contrast, remittances are the aggregated total of personal remittances reported by financial 
institutions and intermediaries, which necessarily include the amount that migrants send to their 
families and to elsewhere such as their own personal bank accounts.

A notable source of discrepancy can be attributed to the large sums of remittances that migrants 
and the diaspora transfer directly to their bank accounts back home or to other investments that 
remain independent of and undisclosed to household members. This type of remittance may be 
captured  in  macro  remittances  but  is  unlikely  to  be  reported  in  household  surveys.  Another 
important  source  of  difference  is  in  the  way  informal  remittances,  or  funds  that  flow  through 
nonformal channels, are treated. At the household level, remittance income is reported regardless 
of  the  channels  through  which  the  funds  flow,  although  there  may  be  cases  where  informal

1 This refers to developing member countries (DMCs) of the Asian Development Bank.

---

<!-- PAGE 7 -->

2

remittances  are  underreported.  In  contrast,  aggregate  remittance  statistics  reported  by  central 
banks often do not include informal remittances.2

Clemens  and  McKenzie  (2018)  documented  a  large  discrepancy  in  the  growth  trend  of 
remittances between micro and macro remittance data sources. They found that total remittance 
growth reported  by  all households  typically ranges  from  about  8% (in  the  case of  Pakistan) to 
72%  (El  Salvador)  of  the  growth  in  aggregate  remittances  reported  by  central  banks  over  the 
same  period.  These  differences  in  definition  make  it  difficult  to  evaluate  the  contribution  of 
remittances  to  economic  output  and  growth  in  a  way  that  is  consistent  across  micro  and 
macroeconomic settings.

In this paper, we propose to assess the simultaneous contribution of international remittances to 
household  expenditures  and  the  overall  economic  output  of  the  migrants’  country  of  origin  by 
using  the  definition  of  remittances  from  the  micro  literature. 3 We  examine  how  the  reported 
expenditures  (referring  here  to  both  consumption  and  savings  or  investment  activities)  of 
remittance-recipient households effectively flow through the overall economy, taking into account 
the impact on individual sectors and their linkages. Using the case of the Philippines, one of the 
major source countries of international migrants, this study links household data and insights to 
the  input-output  table,  which  systematically  presents  all  economic  activities  of  a  country, 
consisting  of  production,  consumption,  and  investment,  while  showing  the  interdependencies 
among industries. Based on this micro-macro analysis approach, we estimate the combined first-
degree impact of remittances generated by direct consumption or expenditure and the second-
degree impact, capturing how remittance-induced purchases of goods and services spill over to 
other sectors through multiplier effects and the value chain.

We  note  that  based  on  the  2018  Family  Income  and  Expenditure  Surveys  (FIES),  household 
expenditures  financed  by  remittances  were  estimated  at  ₱742.2  billion  (or  $14.1  billion).4 It  is 
worth  noting  that  this  amount  represents  less  than  half  (44%)  of  the  total  official  international 
remittance inflows to the country reported by the Bangko Sentral ng Pilipinas (BSP) for the same 
year.  We  observe  different  household  expenditure  patterns  between  remittance-receiving 
households  and  non-remittance-receiving  households  depending  on  the  extent  of  their 
dependence  on  remittance  income.  On  average,  recipient  households  spend  more  (as  a 
percentage of their total expenditures) on education, real property and construction, and health.

Our  micro-macro  analysis  shows  that  remittance-induced  household  expenditures  contributed 
3.5% of the country’s total output, leading to 3.4% of the country’s GDP through its value addition 
and  to  3.7%  of  total  employment  in  2018.5 The  industries that  generate the  most  value  added 
from the direct revenue of the consumption portion of remittances include manufacturing (25% of 
the  total  contribution  to  GDP),  followed  by  wholesale  and  retail  trade  (17%),  and  agriculture, 
forestry, and fishing (14%). The savings or investment portion of household remittance income 
goes  mostly  to  construction  (9%).  Should  international  remittances  received  by  households 
arbitrarily increase by 10% (equivalent to ₱74.2 billion or $1.4 billion), total domestic demand will

2 Some countries, based on information of their nationals abroad, adjust their inward international remittance statistics 
to include remittances from informal channels; thus, the aggregate remittance statistics reported by the World Bank 
are also adjusted for informal remittances (Freund and Spatafora 2008).  
3 This paper focuses on international remittances, which can be compared with data from BOP. Therefore, we do not 
include domestic remittances when referring to remittances unless specifically stated.  
4 Based on the average exchange rate of the Philippine peso to the US dollar rate of ₱52.66 in 2018. 
5 The BSP reported the headline figure of aggregate remittances at the equivalent of 9.3% of GDP in 2018 based on 
balance of payments definition.

---

<!-- PAGE 8 -->

3

be 0.29 percentage points higher than in the baseline scenario, resulting in an increase in output 
of  0.35  percentage  points  (≈$2.4  billion)  and  contributing  to  overall  GDP  growth  of  0.34 
percentage points (≈$1.2 billion) and employment growth of 0.36 percentage points (equivalent 
to nearly 150,000 jobs). The  influence of an increase in remittance income on the expenditure 
reallocation toward investment activities boosts demand and thus the output for real estate and 
construction activities.

The  next  section  provides  a  brief  overview  of  the  literature  on  remittances  and  economic 
development,  focusing  on  empirical  evidence  of  their  influence  on  household  expenditure  and 
savings  and  the  overall  macroeconomy.  Section  3  outlines  the  data  and  methods  used  in  the 
micro-macro analysis and modeling exercises. Section 4 presents key insights and other findings 
from the micro-household data, while section 5 presents the results of the micro-macro analysis, 
quantifying  the  sectoral  and  overall  impact  of  remittances  on  growth.  The  final  section  draws 
evidence-based policy implications and concludes.

2.  Background and Literature Review

The extensive literature quantifying the impact of remittances can be divided into two groups of 
papers. One examines the effect on the welfare and productivity of recipient households based 
on  micro  datasets,  while  the  other  performs  either  panel  data  estimation  or  macro-modeling 
techniques using aggregate data on remittance inflows and estimates the impact on the overall 
economy and other macroeconomic indicators.

Researchers  find  that  the  receipt  of  remittances  has  enabled  households  to  fund  daily 
consumption  and  productive  investment.  Yang  (2008)  showed  that  the  exogenous  increase  in 
remittances  due  to  the  exchange  rate  shock  triggered  by  the  1997  Asian  financial  crisis  was 
primarily used by Filipino households for investment-related expenditures, especially education 
and microenterprises. In Guatemala, Adams and Cuecuecha (2010) found that households that 
received international remittances from the United States spent more on education (194%) and 
housing  (81%)  than  they  would  have  spent  on  these  items  in  the  absence  of  remittances. 
Amuedo-Dorantes  and  Pozo  (2014)  found  that  income  from  international  remittances  had  a 
greater impact on Mexican households’ health expenditures than other sources of income. Using 
visa  lottery  as  a  natural  experiment,  Gibson  et  al.  (2019)  show  that  large  gains  from  Pacific 
migrants are not only short term but also long term. Mishra, Kondratjeva, and Shively (2022), who 
conducted an instrumental variable analysis using the 2010/11 Nepal Living Standards Survey, 
found that households receiving remittances spend more on food and education, suggesting a 
long-term increase in productivity. According to their estimate, a 10% increase in the annual value 
of  remittances  received  increases  average  monthly  food  consumption  by  0.9%  and  annual 
educational expenditure by 8%.

Remittances  supplement  domestic  income  and  help  households  escape  poverty  and  insure 
against income shocks. Yang and Martinez (2006) observed 2.8 percentage point reductions in 
the poverty rate among recipients of international remittances in the Philippines amid an increase 
in  migrant  households’  remittance  receipts  equivalent  to  10%  of  precrisis  household  income. 
Remittances have also been found to help households in rural Viet Nam exit poverty, particularly 
through  asset  growth,  although  the  impact  varies  by  the  welfare  status  and  ethnicity  of  the 
recipient  (Amare  and  Hohfeld  2016).  Meanwhile,  also  in  the  Philippines,  using  local  rainfall 
changes as an identification strategy, Yang and Choi (2007) generally observed how remittances

---

<!-- PAGE 9 -->

4

respond  to  income  shocks,  smoothing  household  consumption.  Other  researchers  also  find  a 
significant increase in establishing capital-intensive enterprises among recipient households.

However, not all empirical studies attribute positive outcomes to remittances. Several studies also 
suggest that remittances may fuel conspicuous consumption and/or disincentivize human capital 
investment if a typical job abroad does not require skills or if the children left behind, especially 
boys,  are  mobilized  to  work  to  meet  labor  needs  (e.g.,  McKenzie  and  Rapoport  2011;  Ang, 
Sugiyarto, and Jha 2009; and Gao, Kikkawa, and Kang 2021). In some countries, income from 
remittances is found to reduce the incentive to work in recipient households (e.g., Acosta, Lartey, 
and Mandelman 2009; Murakami, Yamada, and Sioson 2021).

Meanwhile,  the  macro-level  empirical  literature  tackled  the  contribution  of  international 
remittances to the recipient country’s macroeconomic fundamentals, including growth, inflation, 
exchange  rate,  and  national  poverty  rate.  Cooray  (2012)  used  the  growth  model  approach  to 
examine a panel data of South Asian countries over the period 1970–2008 and found that a 1% 
increase  in migrant  remittances  contributed  to  a 0.01%  increase  in economic  growth.  Giuliano 
and  Ruiz-Arranz  (2009)  also  reached  a  similar  finding  using  a  newly  constructed  dataset  for 
remittances  covering  about  100  developing  countries.  However,  the  positive  reinforcement  of 
remittances on growth is more pronounced in countries with less developed financial systems, 
suggesting that these flows have helped overcome liquidity constraints. Similar findings can be 
found in Meyer and Shera (2017), who examine panel data of high remittance-receiving countries 
in Eastern Europe during the period 1999–2013.

Using  computable  general  equilibrium  model,  Ahmed,  Sugiyarto,  and  Jha  (2010)  found  that  a 
hypothetical 50% reduction in remittance flows would have a devastating impact on the poverty 
situation in Pakistan—with the poverty headcount ratio increasing by 6.4%. By constructing and 
analyzing  a  broader  set  of  71  developing  countries,  Adams  and  Page  (2005)  found  that 
international  remittances  significantly  reduce  the  level,  depth,  and  severity  of  poverty  in  the 
developing  world.  Addressing  endogeneity  issues,  they  found  that  a  10%  increase  in  official 
international remittances per capita leads to a 3.5% decline in the share of people living in poverty. 
Relatedly,  Yoshino,  Taghizadeh-Hesary,  and  Otsuka  (2017)  studied  data  from  10  developing 
Asian countries from 1980 to 2014 and found that a 1% increase in international remittances (as 
a percentage of GDP) can lead to a 22.6% decline in the poverty gap and a 16.0% decline in the 
poverty severity ratio. Using the Philippines as a case study, Goce-Dakila and Dakila, Jr. (2009) 
found that a 5% reduction in remittances received by households is accompanied by a decrease 
in overall gross output of less than half a percentage point, with the largest impact observed in 
the  services  sector.  Further,  Ratha  (2005)  has  elaborated  on  the  importance  of  workers’ 
remittances as a stable source of external funding in developing recipient countries, which may 
even  be  countercyclical  during  a  growth  slowdown.  This  was  evident  during  the  coronavirus 
disease (COVID-19) pandemic (Kikkawa et al. 2021).

The empirical insights at the micro and macro levels complement each other and allow for a more 
comprehensive assessment of the impact of remittances on migrants’ families and communities, 
as well as on the overall economies of countries of origin. However, care must be taken when 
comparing and synthesizing the two sets of findings, as the definitions of international remittances 
used in the micro and macro literature are not identical and the data sources are distinct.  In micro-
level  studies,  international  remittances  typically  refer  to  the  cash  or  in-kind  income  that 
households  reported  receiving  from  abroad  in  surveys.  At  the  macro  level,  international

---

<!-- PAGE 10 -->

5

remittances refer to nationally aggregated external financing reported by financial institutions and 
intermediaries.

Varying definitions and data sources mean that some remittance flows are counted in one country 
but not in another country. One stream of remittances that is captured in macro statistics but not 
likely in micro data is the remittances  that flow into migrants’ own bank accounts or into direct 
investments  such  as real  estate.    Personal  bank  accounts  that  are  not  known  or  accessed  by 
other family members are reportedly preferred by migrant workers because it gives them more 
control over the allocation (Ashraf et al. 2015).

Another  source  of  inward  remittances  that  is treated  differently  in  micro and  macro  remittance 
statistics is informal remittances, which generally refer to transfers of funds that are not coursed 
through  formal  financial  intermediaries.  Household  surveys  potentially  report  all  remittance 
income received by households in a given period, regardless of the channels through which these 
funds  were  transferred,  although  there  may  be  cases  where  households  underreport  informal 
remittances. In contrast, macroeconomic remittance statistics, typically reported by central banks, 
do  not  include  informal  remittances  except  that  some  countries  or  datasets  adjust  aggregate 
remittance  data  based  on  migrant  stock  abroad  to  include  informal  remittances  (World  Bank 
2023). There is also a form of income from abroad that does not appear in any of the statistics, 
such as unreported cash hand-carried by migrants that they save or consume themselves.

Apart from definitions, measurement errors can also lead to different sizes and trends in macro 
and  micro  remittance  data.  For  macro  data,  there  have  been  frequent  changes  in  the  official 
definition.  Until  2005,  using  the  Balance  of  Payments  Manual  (BPM)  5,  remittances  comprise 
workers’ remittances and compensation of employees. Amid the difficulty of separating transfers 
made  by  migrant  workers  from  their  employment  income  from  a  number  of  other  transfers, 
remittance  statistics  using  the  BPM6  now  comprise  personal  transfers  and  compensation  of 
employees (Clemens and McKenzie 2018).6 Even remittance data based on household surveys 
are not free of measurement error, particularly due to misreporting and recall errors. In addition, 
a  typical  national  household  income  expenditure  survey  may  not  report  (exclude)  remittances 
receipts that are channeled to family businesses and cottage industries because the funds are 
then  categorized  to  a  separate  household  production  module  to  derive  household  business 
income.

The discrepancy in remittance growth between macro data and household survey-based micro 
data is documented in Clemens and McKenzie (2018) for many major migrant-sending developing 
economies. They note that the growth in total remittances reported by households typically ranges 
from about 8% (Pakistan) to 72% (El Salvador) of the growth in aggregate remittances reported 
by the central bank for the same period. The discrepancy between the data could possibly explain 
the differences in the results of the analysis used to evaluate the impact of remittances in migrants’ 
countries of origin in the micro and macro literature.

We propose to assess the short-run contribution of remittances to household expenditures and 
national-level output by using a consistent definition of remittances: the expenditure of recipient 
households. We feed micro-level remittance data to that of the macro-level analysis in accordance 
to  how  households  spend,  save,  and  invest  their  remittance  income  in  specific  sectors  of  the

6 Another item that may be included in macro remittances but not in micro household data is the inward transfer of a 
third-country national (as seen recently in the surge in remittances to Central Asian countries from migrating Russian 
nationals due to the Russian invasion of Ukraine).

---

<!-- PAGE 11 -->

6

economy and examine the magnitude of the macroeconomic impact of remittances using the so-
called  network  of  input–output  linkages  between  different  economic  sectors.  It  can  be 
hypothesized that household spending on goods and services in certain sectors that have strong 
sectoral economic linkages and value chains amplify the effect of remittances on the aggregate 
economy  beyond  direct  consumption.  The  input-output  (I-O)  framework  is  one  of  the 
macroeconomic  models  that  allows  aggregate  household-level  expenditure  and  savings  to  be 
applied to industry sectors and the economy as a whole, and the impact to be assessed at a given 
point in time (Miller and Blair 2009). It clearly illustrates how different sectors contribute to the 
overall output by considering the interlinkages using a country-specific matrix that represents the 
structure of the economy.7

To  date,  there  are  a  few  studies  that  attempt  to  evaluate  the  macroeconomic  contribution  of 
remittance-induced  expenditure  using  the  I-O  model,  or  that  attempt  to  feed  micro-level 
information and insights into the framework to evaluate its impact on overall growth. The work of 
Dridi  et  al.  (2019)  and  Glytsos  (1993)  are  most  relevant  to  our  proposed  methodology  for 
establishing  micro-macro  linkages  to  evaluate  the  contribution  of  remittances  to  household 
expenditure and the overall economy.  Dridi et al. (2019) proposed a macroeconomic model to 
quantify how changes in aggregate demand due to additional income from household remittances 
propagate through the network of input-output linkages in sub-Saharan African countries. They 
find  that  countries  with  intricate  and  mutually  dependent  industrial  linkages  benefit  more  from 
remittance-led  demand.    In  this  paper,  consumption  preferences  are  determined  using  a 
macroeconomic  model,  but  without  micro  data  that  provide  more  detailed  preferences  of 
heterogeneous  households,  including  those  with  and  without  remittances.  Given  that  many 
studies  indicate  distinct  consumption  patterns  of  migrant  households,  the  assumption  of 
homogeneous households is questionable.

Meanwhile, Glytsos (1993) incorporated information on the pattern of expenditure of remittance 
recipients from a Greek household survey into the country’s input-output table. By converting the 
pattern of consumer expenditures into a structure of industry final demand, he estimated that the 
remittances received resulted in a gross output equivalent to 4.1% of the economy’s total gross 
production  in  1971  and  created  74,000  new  jobs  in  the  non-agriculture  sector.  The  model 
proposed  by  the  study,  however,  is  very  data  intensive,  as  it  requires  a  longitudinal  series  of 
household micro data accompanied by corresponding I-O tables to establish causal impact.

3.  Methodology and Data Sources

The paper conducts a micro-macro analysis using data from a single-year household survey—
the 2018 FIES—and I-O tables to estimate the effect of remittances on household expenditures 
and on the sectoral and overall economy. It uses a simple and straightforward methodology that 
illustrates and quantifies the short-term contribution of remittances to household expenditures and 
overall  economic  output,  taking  into  account  the  impact  on  individual  sectors  and  their 
interlinkages.  The  micro-macro  analytical  approach  requires  a  minimum  set  of  data  that  are 
commonly  available  in  many  developing  economies:  (i)  household  income  and  expenditure

7 The I-O framework has been used in the existing literature to assess the environmental impact of household 
consumption (e.g., Seriño and Klasen 2015; Schepelmann et al. 2020) or evaluating the impact of tourism on output 
and growth (e.g., Pratt 2015 for seven small-island developing states). Unlike the CGE model, the I-O model’s impact 
assessment can also be done with simple data and solution software.

---

<!-- PAGE 12 -->

7

surveys, and (ii) I-O tables. We follow a two-step process: (i) tracing remittance income received 
by  households  and  identifying  how  it  is  spent,  invested,  or  saved;  and  (ii)  quantifying  the 
contribution of this expenditure to sectoral and overall economic output. We use the Philippines, 
which  is  one  of the  largest sources  of  migrant workers  and  remittance recipients  in  Asia,  as  a 
case study.

STEP 1: Micro-level analysis of household spending and saving pattern

The first step is to examine the expenditure patterns and the allocation by commodity items of 
remittance-receiving households.8 We generate descriptive statistics and estimate consumption 
equations to derive the marginal propensity to consume, which we allow to vary by household 
characteristics  such  as  income  quintile  and  remittance  dependency.  We  use  the  Philippine 
Statistics  Authority’s  microdata  of  the  2018  FIES.  The  survey  interviewed  a  sample  of  about 
180,000  households,  and  the  dataset  generates  the  weighted  sample  of  about  25  million 
households  deemed  present  in  2018.9 The  dataset  provides  reliable  estimates  of  income  and 
expenditure at different spatial levels, including national, regional, provincial, and highly urbanized 
cities (PSA 2020).

The  per  item  consumption  equations  are  estimated,  taking  into  consideration  the  households’ 
remittance-receiving  status.  This  information  allows  us  to  allocate  changes  in  aggregate 
consumption when we conduct simulations for remittance shock scenarios using the I-O model. 
We  estimate  the  consumption  equations  closely  following  the  empirical  specification  of  Wang, 
Hagedorn, and Chi (2021), with some additional assumptions about how income from remittances 
is allocated and utilized in a remittance-receiving household:

(cid:2872)
𝐶(cid:3036)(cid:3037) = 𝛼(cid:3036) + 𝛽(cid:3036)𝑇𝐼𝑛𝑐(cid:3037) + ∑
(cid:3041)(cid:2880)(cid:2869)

𝛾(cid:3036)(cid:3041)
𝜌(cid:3036)(cid:3041) (cid:3435)𝑇𝐼𝑛𝑐(cid:3037) × 𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦(cid:3037)(cid:3439)

𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦(cid:3037) +

(cid:2872)
 ∑
(cid:3041)(cid:2880)(cid:2869)

+ 𝛿𝐗𝐣 + 𝜀(cid:3036)(cid:3037)

(Equation 1)

The dependent variable, 𝐶(cid:3036)(cid:3037), refers to the share of each expenditure item 𝑖 in the total expenditure 
of  household 𝑗.  Here,  we  categorize  total  household  living  expenses  into  16  broad  commodity 
items:  food,  tobacco  and  alcohol,  housing  and  utilities,  durables  (including  vehicles),  clothing, 
furnishings, health, transport, communications, education, recreation, finance, real property and 
construction, miscellaneous expenses, real property and new construction, and bank savings and 
investments. Note that the limited  details  in the FIES do not allow the identification of relevant 
expenditures  related  to  family  enterprises  that  may  have  been  financed  by  the  receipt  of 
remittances.

The coefficient, 𝛽(cid:3036), refers to the percentage point change in the share of expenditure item 𝑖 in total 
expenditure given a percentage change in total household income. Unlike Wang, Hagedorn, and 
Chi (2021), who distinguish between remittance and non-remittance income by obtaining a unique 
parameter of marginal propensity to consume for each income, we use household’s 𝑇𝐼𝑛𝑐(cid:3037) or total 
income (in log) regardless of sources. In other words, we assume that remittance income is as 
fungible  as  all  other  sources  of  income,  such  as  wages  and  salaries.  This  is  consistent  with

8Throughout the paper, remittance-receiving households are defined as households receiving cash income from 
abroad, which is our measure of remittance income. Note that this variable from the FIES questionnaire also includes 
other sources of income from abroad, such as (i) pensions, retirement, workmen’s compensation, and other benefits; 
(ii) cash gifts, support, relief, etc. from abroad; and (iii) dividends from investments abroad. 
9 This translates to about 25 million Filipino households in 2018 as defined by the Philippine Statistics Authority, 
which is highly consistent with the more than 26 million Filipino households recorded in the 2020 Census of 
Population and Housing. The survey response rate was 92.5% (PSA 2020).

---

<!-- PAGE 13 -->

8

several studies that corroborate Friedman’s (1957) permanent income hypothesis. For example, 
Castaldo and Reilly (2007) found only modest effect of receipt of international remittances on the 
marginal spending behavior of households in Albania. Further, such a modest effect was found 
only  for  food  consumption.  Meanwhile,  a  study  based  on  the  2005  Ghana  Living  Standards 
Survey found almost negligible changes in household spending behavior (Adams and Cuecuecha 
2013).

Our  assumption  of  fungibility  of  remittance  income  also  seems  consistent  with  the  pattern  of 
remittances and other sources of income among Filipino households. Descriptive statistics show 
that Filipino households typically rely on more than two sources of income and that the share of 
overseas remittances to the total household income does not exceed 50% for the majority (83.9%) 
of remittance-receiving households (see more details on descriptive statistics in the next section). 
In addition, we found that as much as 64% of recipient households of international remittances 
also report income from domestic remittances, which poses a methodological challenge to identify 
the particularities of the expenditure allocation of international remittances income.

In  equation  1,  we  also  introduced  a  control  variable  indicating  the  extent  of  household 
dependence  on  remittance  income  by  adding the  interaction  between  total  household  income, 
𝑇𝐼𝑛𝑐(cid:3037), and the categorical variable, 𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦(cid:3037), which is based on the share of remittance 
income to the total income of household 𝑗  at a 25% interval (hence, resulting in five independent 
household  groups  including  nonrecipients).  The  coefficient  𝜌(cid:3036)  provides  a  measure  of  how 𝛽(cid:3036) 
differs  across  household  groups.  This  approach  is  intended  to  capture  the  possibility  that  the 
share of income from remittances may have different effects on consumption patterns.

Household-level characteristics 𝐗𝐣, include household size, share of members below the age of 
5, share of members aged 5 to 17 years, and household head characteristics such as age, gender, 
marital  status,  educational  attainment,  and  job  status.  Place  of  residence  (urban  or  rural)  and 
region  are  also  controlled  for  in  the  model.  The  idiosyncratic  error  term 𝜀(cid:3036)(cid:3037)  is  assumed  to  be 
uncorrelated  with  the  explanatory  variables.  The  set  of  equations  in  (1)  is  estimated  using the 
seemingly unrelated regression technique of Shonkwiler and Yen (1999), allowing the error to be 
correlated across equations (Moon and Perron 2005).

The  consumption  equations  do  not  provide  insights  to  evaluate  the  potential  impact  or  causal 
inference  of  migration  and  remittances  on  the  consumption  behavior  of  recipient  households. 
Instead, our primary objective is to understand how households allocate their income, including 
income  from  international  remittances  and  expenditures  based  on  their  revealed  expenditure 
patterns.

STEP 2: Macrosimulation using the input-output framework

The second step in constructing the micro-macro analysis model is to aggregate households’ total 
income  from  international  remittances  and  their  expenditures  (consumption  and  investment) 
reported  in  the  FIES  and  map  them  to  the  macro-level  input-output  table.  As  mentioned,  it  is 
expected  that  the  total  income  from  remittances  reported  by  households  will  differ  from  the 
international remittance data reported by the central bank due to the differences in definitions and 
data  sources.  We  feed  remittance  income  allocated  toward  expenditure  and  savings  and 
investment to the 2018 Benchmark Input-Output (I-O) Accounts of the Philippines in the form of 
final  demand  from  households  and  evaluate  its  impact  on  sectoral  and  overall  output.  As  an 
additional exercise, we simulate how a 10% increase in remittance income changes expenditure

---

<!-- PAGE 14 -->

9

patterns using the consumption equation and how the changes translate to sectoral and overall 
output.

a.  Mapping commodity items to I-O sectors

Commodity items from the 2018 FIES are mapped to the 80-sector disaggregation of the 2018 I-
O table.10 The FIES-IO concordance matrix11 allows a one-to-one matching that largely considers 
the sectors that produced (or delivered) the commodity (or service). However, the matrix leaves 
out retail and wholesale trade sectors (I-O sectors 54 and 55) from which a majority of the goods 
were purchased. To overcome this limitation, we collect retail and wholesale trade margins by 
sector from the 2016 Annual Survey of Philippine Business and Industry and use them to allocate 
a portion of the value of commodity items that should go to retail and wholesale trade sectors.12  
We also differentiate the purchase of domestic products out of remittances from that of foreign 
products  (whereby  the  latter  does  not  constitute  domestic  output  except  in  retail  sectors).  We 
derive a matrix containing import demand levels of intermediate and final demand components 
by sector and deduct it from the published 2018 input-output table.

b.  Deriving I-O household final demand driven by remittance income

The  final  demand  from  households  refers  to  their  final  expenditure,  which  consists  of  their 
consumption (the sum of household spending on various consumption items) and their savings 
or investment (items such as bank savings, real estate purchases, and construction and/or major 
renovations). To determine the aggregate expenditure of households, we first calculate the portion 
of  remittance  income  used  for  consumption  and  savings  or  investment  per  household.  We 
assume  that  households  spend  their  remittance  income  on  consumption  in  the  proportion 
equivalent to the share of remittance income in total income. Household savings are the residual 
of income and their total consumption plus deposits in banks/investments, purchase/amortization 
of real property, and money used either to build a new house or for major repair or renovation of 
an  existing  house,  according  to  the  System  of  National  Accounts  2008  guide  (European 
Commission et al. 2009).

We  calculate  the  sum  of  remittance-financed  consumption  and  savings  of  all  households  to 
determine the aggregate amount of expenditure and the savings component of remittances. The 
sum of expenditures forms part of household final consumption expenditures, while the savings

10 The 2018 Benchmark I-O Accounts of the Philippines include the I-O transaction table, the technical coefficient 
matrix, and the Leontief inverse matrix in three dimensions (i.e., 16x16, 80x80, and 240x240) corresponding to the 
sectoral disaggregation. 
11 The detailed expenditure items in the FIES follow the classification system, Philippine Classification of Individual 
Consumption According to Purpose (PCOICOP). To maintain their equivalence with the I-O sector, we follow the four-
step conversion process in consultation with the Philippine Statistics Authority:

1)  PCOICOP to 2002 Philippine Central Product Classification (PCPC) 
2)  2002 PCPC to 1994 Philippine Standard Industrial Classification (PSIC) 
3)  1994 PSIC to 2009 PSIC (Updates to 1994 PSIC) 
4)  2009 PSIC to 2018 I-O Sectors

Using the concordance above, the commodity items with PCOICOP codes 011121 (corn on the cob), 011121 (whole 
corn/grain),  011121  (corn  grits),  and  011121  (other  corn,  corn  starch,  etc.)  are  all  classified  under  I-O  sector  02 
(Growing of corn). 
12 For example, retail and wholesale trade margins for I-O sector 02 of commodities are both 9%; thus, if the total 
expenditure on such commodities is ₱100.00, we allocate ₱9.00 each to retail and wholesale trade.

---

<!-- PAGE 15 -->

10

form part of gross fixed capital formation. The combined aggregate of the two is synonymous to 
the level of final demand induced by remittances, which we shall collate as the vector 𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047).

c.  Estimating impact of remittance-sourced household final demand on output and employment

The contemporaneous impact of remittance-financed demand on the gross output of the economy 
is  estimated  using  the  80-sector  I-O  table.  For  ease  of  presentation,  the  estimates  are  later 
aggregated into 16 I-O sectors. To estimate the baseline outputs per production sector i induced 
(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)) ,  the  final  demand  vector  derived  from  the  earlier  steps,  𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047) ,  is 
by  remittances  (𝑥(cid:3036)
multiplied  by  the  80-sector  Leontief  inverse  matrix (𝑩) published  by  the  Philippine  Statistics 
Authority (PSA), i.e.,

𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047) = 𝑩 ⋅ 𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)

where 𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)denotes  the  vector  of  sectoral  gross  outputs  realized  through  remittances,  which 
entail both direct and indirect impacts. Once 𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047) is obtained, it is multiplied elementwise by the 
vector of sectoral employment-to-output ratios, 𝑒 , to derive the level of employment per sector 
associated  with  remittances.  Sectoral  employment-to-output  ratios  are  estimated  using  the 
employment per I-O sector based on the 2018 Labor Force Survey and gross output per sector 
based on the 2018 I-O table.

d.  Extension–Simulation with exogenous change in remittance income

As an extension of the model, we also simulate the impact of a 10% increase in remittance income 
on gross output and employment. We estimate the share of each sector in every household’s total 
expenditure  with  and  without  the  hypothetical  increase  in  remittance  income.  The  hypothetical 
change  in  the  aggregate  expenditure  (both  consumption  and  savings)  is  derived  from  a  micro 
simulation based on the results of the consumption equations.

4.  Remittance Income and Reported Household Expenditures in the Philippines

The Philippines is a major country of origin for international migrants, sending an average of more 
than 2 million workers each year since 2016.13 The United Nations Department of Economic and 
Social Affairs Population Division (2021) estimates that about 6.1 million Filipinos currently live 
abroad, representing 5.4% of the country’s total population. In 2018, up to 29.7% of all households 
in the Philippines received cash from abroad. Remittance-receiving households are distributed 
across all income groups, with a higher representation in the higher quintiles (Figure 1a). This is 
consistent with the general observation that international migration is not as common among the 
poor,  who  cannot  afford the  initial costs  of  migration  (de  Haas  2010).  The  share  of  remittance 
income in total household income increases with income level, from an average of only 16% in 
the lowest quintile to 31% in the highest income group. International remittances have the highest 
share (31%) in the top income quintile, which is even higher than income from wages and salaries.

13 However, this number declined during the COVID-19 pandemic due to travel restrictions and suppressed global 
economic activity.

---

<!-- PAGE 16 -->

Figure 1: Philippine Households by Receipt of and Dependence on International 
Remittances and Income Quintile, 2018

a. By Receipt of International Remittances

b. Remittance-Receiving Households’ 
Dependence on Remittances

11

Notes: In (a), the numbers inside the blue bar represent the share of remittance-receiving households to total number 
of households per income quintile. 
Source: Authors’ calculations.

Remittance  income  accounts  for  only  a  quarter  or  less  of  their  total  income  for  more  than  the 
majority (61.8%) of the overall remittance-receiving households (Figure 1b). Another 22.1% report 
that  remittances  account  for  26%–50%  of  their  total  income,  while  the  remaining  households 
(16.1%) use remittances as their primary source of income, with about one-third of households 
reporting that they rely heavily on remittances (over 75%). The dependency on remittances as a 
source of income is greater among households in higher income brackets.

Household Consumption and Savings by Remittance Receiving Status

The average annual spending of a Filipino household reached ₱239,000 (≈ $4,538.4). Figure 2 
shows the share of each broad commodity including savings and investments, in total household 
expenditures,  comparing  the  remittance-receiving  and  non-recipient  households.  The  overall 
spending  allocation  patterns  of  the  two  groups  of  households  on  the  various  commodities  are 
similar. However, there are significant differences in the share of some commodity items, such as 
food, housing, health, and education. The allocation of remittance-receiving households in food 
expenditures (35.6%) is relatively lower than the share of non-remittance-receiving households 
(42%). In contrast, spending on housing and on productivity-enhancing items such as health and 
education is relatively higher among remittance recipients. Remittance-receiving households also 
spend more on investments, in terms of share to their total expenditure, such as real property, 
major repairs or renovations, and construction of new houses, as well as on bank savings and 
investments.

---

<!-- PAGE 17 -->

Figure 2: Share of Broad Expenditure Items to Total Expenditure, by Receipt of 
Remittances, 2018

12

Source: Authors’ calculations.

The observed heterogeneity in expenditure patterns could be due to the skewed distribution by 
income  of  remittance-receiving  households.  Figure  3  shows  the  share  of  total  expenditure  on 
broad commodity items, by income quintile and receipt of remittances. Expenditure patterns are 
largely  the  same  between  the  remittance-recipient  and  non-recipient  groups,  but  notable 
differences  are  still  observed  in  education,  health,  financial  services,  real  property  and 
construction, recreation, and transportation. These differences are more pronounced in the higher 
income  quintiles.  The  use  of  financial  services  is  found  to  be  higher  among  non-remittance 
receiving  households.  While  this  is  somewhat  counterintuitive,  given  that  many  households 
receive funds through financial intermediaries, it may suggest that financial inclusion and use of 
financial services remains limited among remittance recipients.

---

<!-- PAGE 18 -->

Figure 3: Share of Broad Commodity Items to Total Expenditure, by Income Quintile and 
Receipt of Remittances, 2018

13

Source: Authors’ calculations.

Descriptive  data  show  that  savings  behavior  does  not  show  significant  differences  between 
remittance- and non-remittance-receiving households. In 2018, the average share of savings in 
household  income  is  17.3% (Figure  4).  Remittance-receiving  households  have  a  slightly  lower 
savings  ratio  (17.1%)  than  non-remittance-receiving  households  (17.8%).  As  expected, 
households with bank accounts have a higher savings rate (25.5% versus 17.2%), although their 
numbers  account  for  no  more  than  1%  of  total  households.  Comparing  the  two  groups  of 
households,  the  savings  rate  of  remittance  recipients  is  slightly  higher  (26.3%)  than  the  non-
remittance-receiving households (24.4%).

Figure 4: Savings Rate, by Bank Use and Receipt of Remittances, 2018

26.3

25.5

24.4

17.3

17.1

17.8

17.2

17.1

17.7

t
n
e
c
r
e
P

30

20

10

0

All

Bank

Nonbank

All households
Remittance-receiving households
Non-remittance-receving households

Source: Authors’ calculations.

---

<!-- PAGE 19 -->

14

Findings from Household Consumption Equations

We  further  investigate  the  expenditure  pattern  of  remittance  recipients  and  non-recipients  by 
estimating  the  consumption  equation  presented  in  section  3.  Table  1  presents  our  empirical 
results. Following the relevant literature, such as Zhu et al. (2014) and Wang, Hagedorn, and Chi 
(2021),  the  coefficients,  𝛽(cid:3036) ,  of  total  household  income  can  be  interpreted  as  the  marginal 
propensity to consume, which varies by receipt of remittances as well as the extent of dependency 
to  such  income  source  with  the  interaction  term, 𝜌(cid:3036) .  In  terms  of  magnitude,  bank  savings  or 
investments  are  observed  to  have  the  largest  increase  in  any  expenditure  item  amid  a  similar 
increase in total household income. For a 10% increase in total household income, the share that 
average  households  allocate  to  bank  savings  and  investments  increases  by  0.43  percentage 
points. This is followed by durables (including vehicles), finance, and recreation. Allocation toward 
real property and housing construction also rises by 0.12 percentage points with a 10% increase 
in household income.

---

<!-- PAGE 20 -->

Table 1: Consumption Equation Regression Results, by Broad Expenditure Items

Variables

(1) 
Food

(2) 
Tobacco and 
Alcohol

(3) 
Housing

(4) 
Utilities

(5) 
Durables 
(including 
vehicles)

(6) 
Clothing

(7) 
Furnishing

(8) 
Health

15

Total household income (log)

-11.797***

-0.332***

(0.001) 
Remittance dependency group (Benchmark = Non-remittance 
receiving households) 
Group 1 = 0% < Remittance-to-
income ratio ≤ 25%

-2.391***

(0.004)

0.490***

Group 2 = 25% < Remittance-
to-income ratio ≤ 50%

Group 3 = 50% < Remittance-
to-income ratio ≤ 75%

Group 4 = Remittance-to-
income ratio > 75%

(0.095)

0.576***

(0.157)

-4.972***

(0.230)

-1.693***

(0.300)

(0.029)

-0.068

(0.048)

-0.995***

(0.070)

-4.987***

(0.092)

Interaction term (Total household income x remittance dependency 
group) 
Group 1 = 0% < Remittance-to-
income ratio ≤ 25%

-0.049***

0.144***

Group 2 = 25% < Remittance-
to-income ratio ≤ 50%

Group 3 = 50% < Remittance-
to-income ratio ≤ 75%

Group 4 = Remittance-to-
income ratio > 75%

(0.008)

(0.002)

-0.082***

(0.012)

0.320***

(0.018)

0.076***

(0.023)

-0.014***

(0.004)

0.054***

(0.006)

0.353***

(0.007)

0.145***

(0.003)

-1.036***

1.688***

(0.002)

(0.003)

0.391***

(0.001)

0.134***

0.796***

(0.001)

(0.002)

-1.669***

1.877***

0.548***

-0.195***

-1.885***

-2.678***

(0.068)

(0.034)

(0.057)

(0.018)

(0.017)

(0.044)

2.086***

(0.113)

-0.247

(0.165)

3.692***

-2.884***

(0.056)

(0.094)

4.555***

2.521***

(0.082)

(0.138)

15.913***

10.198***

-4.485***

(0.216)

(0.107)

(0.180)

0.343***

(0.030)

0.255***

(0.044)

4.785***

(0.058)

-3.694***

-2.869***

(0.028)

(0.074)

-5.153***

-1.501***

(0.040)

(0.108)

0.522***

2.101***

(0.053)

(0.141)

0.221***

(0.005)

-0.124***

-0.043***

(0.003)

(0.005)

0.026***

(0.001)

0.149***

0.248***

(0.001)

(0.004)

-0.061***

-0.238***

0.249***

-0.016***

0.301***

0.273***

(0.009)

(0.004)

(0.007)

(0.002)

(0.002)

(0.006)

0.078***

(0.013)

-0.312***

-0.171***

(0.006)

(0.011)

-0.001

(0.003)

0.412***

0.133***

(0.003)

(0.008)

-1.335***

-0.744***

0.408***

-0.359***

-0.050***

-0.204***

(0.017)

(0.008)

(0.014)

(0.005)

(0.004)

(0.011)

Constant

178.386***

(0.053)

6.802***

(0.016)

10.509***

17.560***

-17.570***

-1.959***

0.808***

-9.075***

(0.038)

(0.019)

(0.032)

(0.010)

(0.009)

(0.025)

Household characteristics

Household head characteristics

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

---

<!-- PAGE 21 -->

16

Variables

(1) 
Food

(2) 
Tobacco and 
Alcohol

(3) 
Housing

(4) 
Utilities

(5) 
Durables 
(including 
vehicles)

(6) 
Clothing

(7) 
Furnishing

(8) 
Health

Region dummies

YES

YES

YES

YES

YES

YES

YES

YES

Weighted no. of observations

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

R-squared

0.598

0.085

0.258

0.092

0.035

0.071

0.039

0.075

Table 1. continued.

Variables

(9) 
Transport

(10) 
Communication

(11) 
Education

(12) 
Recreation

(13) 
Finance

(14) 
Miscellaneous 
Expenses

(15) 
Real Property 
and Housing 
Construction

(16) 
Bank 
Savings/Investments

Total household income (log)

1.065***

(0.002)

0.604***

(0.001)

0.542***

1.383***

(0.002)

(0.003)

1.454***

(0.001)

-0.505***

(0.001)

1.178***

(0.002)

4.289***

(0.003)

Remittance dependency group (Benchmark = Non-remittance 
receiving households) 
Group 1 = 0% < Remittance-to-
income ratio ≤ 25%

-0.990***

0.623***

-2.827***

8.030***

(0.041)

(0.014)

(0.034)

(0.073)

Group 2 = 25% < Remittance-
to-income ratio ≤ 50%

Group 3 = 50% < Remittance-
to-income ratio ≤ 75%

Group 4 = Remittance-to-
income ratio > 75%

4.450***

(0.069)

3.983***

(0.100)

7.255***

(0.131)

-1.003***

(0.023)

0.973***

(0.033)

7.711***

(0.044)

Interaction term (Total household income x remittance dependency 
group) 
Group 1 = 0% < Remittance-to-
income ratio ≤ 25%

-0.061***

0.094***

1.899***

(0.023)

6.019***

(0.038)

-9.412***

8.562***

(0.057)

(0.122)

-16.519***

16.741***

8.064***

(0.083)

(0.178)

(0.055)

1.626***

(0.024)

1.183***

(0.040)

3.161***

(0.059)

-3.544***

(0.046)

-9.425***

(0.077)

-19.323***

(0.113)

1.089***

(0.070)

2.441***

(0.117)

8.453***

(0.171)

-19.772***

24.813***

10.551***

5.062***

-39.047***

-18.929***

(0.109)

(0.233)

(0.072)

(0.077)

(0.148)

(0.223)

Group 2 = 25% < Remittance-
to-income ratio ≤ 50%

Group 3 = 50% < Remittance-
to-income ratio ≤ 75%

0.249***

-0.698***

-0.181***

-0.119***

(0.003)

(0.001)

(0.003)

(0.006)

(0.002)

(0.002)

-0.408***

0.110***

0.815***

-0.782***

-0.550***

-0.089***

(0.005)

(0.002)

(0.005)

(0.010)

(0.003)

(0.003)

0.290***

(0.004)

0.772***

(0.006)

-0.145***

(0.006)

-0.281***

(0.009)

-0.386***

-0.031***

1.436***

-1.446***

-0.738***

-0.248***

1.632***

-0.733***

---

<!-- PAGE 22 -->

17

(9) 
Transport

(10) 
Communication

(11) 
Education

(12) 
Recreation

(13) 
Finance

(14) 
Miscellaneous 
Expenses

(15) 
Real Property 
and Housing 
Construction

(16) 
Bank 
Savings/Investments

Variables

Group 4 = Remittance-to-
income ratio > 75%

(0.008)

(0.003)

(0.007)

(0.014)

(0.004)

(0.005)

(0.009)

(0.013)

-0.663***

-0.545***

1.764***

-2.077***

-0.940***

-0.401***

(0.010)

(0.003)

(0.008)

(0.018)

(0.006)

(0.006)

3.209***

(0.012)

1.507***

(0.017)

Constant

-7.719***

-5.818***

-6.272***

-0.484***

-15.310***

11.689***

-12.535***

-49.011***

(0.023)

(0.008)

(0.019)

(0.041)

(0.013)

(0.014)

(0.026)

(0.039)

Household characteristics

Household head characteristics

Region dummies

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

YES

Weighted no. of observations

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

23,179,315

R-squared

0.076

0.270

0.112

0.150

0.206

0.048

0.044

0.148

Notes: Household level characteristics include household size, share of members aged less than 5 years, share of member aged between 5 and 17 years. Household head characteristics 
are age, gender, marital status, educational attainment, and job status. Due to missing information in some explanatory variables, the effective weighted number of observations is lower 
than the total number of households in 2018. 
Standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.1 
Source: Authors’ calculations.

---

<!-- PAGE 23 -->

18

This  also  applies  to  disbursements  toward  transport,  health,  communication,  and  education. 
Meanwhile, the share to total expenditure on food shows the largest decline when households 
can earn a higher income, i.e., their allocation on food drops by 1.2 percentage points on average 
when  they  have  a  10%  increase  in  income.  The  shares  for  other  expenditure  items,  such  as 
tobacco  and alcohol, and for utilities decrease on average with higher household income.  The 
table  also  shows  that  expenditure  allocation  differs  significantly  between  remittance-receiving 
households  and  those  that  do  not,  as  indicated  by  the  statistically  significant  coefficient  in 𝛾(cid:3036)(cid:3041). 
This finding is consistent with the observations from descriptive data.

The extent of remittance-receiving households’ dependency on remittance income, indicated by 
the  group  dummies  in  the  equation,  is  correlating  to  consumption  choices.  Non-remittance-
receiving  households  slash  a  relatively  higher  share  of  food  expenditures  when  their  income 
increases  than  remittance-recipient  households.  On  average,  a  10%  increase  in  household 
income  among  non-remittance  recipients  is  associated  with  a  decrease  in  the  share  of  food 
consumption by 1.2 percentage points but such response is attenuated for remittance recipients. 
It is interesting to note that remittances appear to have a significant influence on the allocation of 
recipient  households  to  long-term productivity-enhancing  and  investment-related  spending  and 
activities.  While  the  increase  in  the  share  of  education-related  expenses  to  total  household 
expenditures  in  response  to  a  rise  in  household  income  is  seen  across  all  households,  the 
coefficient  is  larger for remittance-receiving  households,  even  when the model controls for  the 
share of children in different age groups in the household.

Similarly, the average share of expenditure on real property investment is 0.12 percentage points 
higher for every 10% increase in household income, with additional rates ranging from 0.03 to 0.3 
percentage  points  among  remittance  recipients,  highest  among  those  with  a  high  reliance  on 
remittances. Regarding health expenditures, remittance-receiving households except those with 
the highest reliance on remittances, allocate more than non-recipient households when income 
increases. One explanation for this could be that, unlike other investment items, health care costs 
generally do not exceed a certain threshold or that this group of remittance recipients has better 
health conditions given their better income situation. Further, the allocation toward disbursements 
relating  to  bank  savings  and  investment  is  higher  for  all  remittance-receiving  households  than 
non-recipient households except for the households most dependent on remittances. However, it 
is worth noting that only the households with the highest dependence on remittance income have 
a higher proxy marginal propensity to consume than the non-remittance-receiving households, 
suggesting  that  remittance  income  encourages  bank  savings  and  investment.  Meanwhile,  the 
coefficients  on  recreation  and,  to  some  extent,  on  food  show  a  lower  marginal  propensity  to 
consume for remittance-receiving households compared to non-recipient households.

In  summary,  remittance-receiving  households  tend  to  have  higher  productive  spending  in 
education and health and investment-related activities, especially in real estate and bank savings, 
compared to their non-recipient counterparts. We also find no evidence that remittance income 
exacerbates conspicuous consumption among recipient households. However, it is worth further 
investigating the factors behind the limited use of financial services among remittance-receiving 
households.

---

<!-- PAGE 24 -->

19

5.  Micro-Macro Analysis on the Impact of Remittance-Driven Household Demand

(Consumption and Investment)

In  2018,  remittance  income  reported  by  households  in  the  FIES  totaled  ₱742.2  billion  ($14.1 
billion),  equivalent  to  4.1%  of  the  GDP.  This  is  slightly  less  than  half  (43.8%)  of  the  official 
aggregate international remittances into the country reported by the Bangko Sentral ng Pilipinas 
(BSP), which amounted to ₱1.7 trillion or $32.2 billion, or approximately 9.3% of GDP. The BSP 
compiles  statistics  on  personal  remittances  according  to  the  latest  Balance  of  Payments 
guidelines. 14  It  is  worth  noting  that  unlike  many  other  central  banks,  the  BSP  estimates 
remittances sent through informal channels using surveys, including the FIES (World Bank 2023), 
and adds them to the official remittance statistics, which helps reduce the gap in micro and macro 
remittance statistics.

Household final demand (consumption and savings/investment) by sector

Total  household  final  demand,  consisting  of  consumption  and  savings/investment  financed  by 
remittance  income,  accounts  for  5.6%  of  total  household  final  demand  reported  in  the  I-O 
transactions  table  in  the  same  year.  We  note  that  household  final  consumption  in  the 
manufacturing sector is the highest at almost ₱2.1 trillion ($38.9 billion), or 37.9% of the aggregate 
consumption  (Table  2).  Philippine  households’  final  consumption  for  manufacturing  consists 
mainly  of  food,  which  accounts  for  65.6%  of  total  household  demand  from  manufacturing, 
beverages,  petroleum,  and  chemical  products.  The  manufacturing  sector  is  followed  by 
accommodation  and  food  services  (11.9%)  and  agriculture,  forestry,  and  fishing  (11.8%).  The 
trade  sector,  which  distributes  final  goods  to  households  mainly  through  retail  activities,  also 
claims a relatively high share (11.4%).

The pattern of final household demands of remittance-receiving and non-recipient households at 
aggregate level across 16 input-output sectors is shown in Table 2. It mimics the consumption 
pattern  of  the  FIES-based  grouping  of  expenditures  in  section  4.  Non-remittance-receiving 
households  have  more  than  2  percentage  points  higher  share  of  consumption  in  the 
manufacturing and agriculture sectors. They also have a slightly higher share of consumption on 
wholesale and retail trade, of about 1.3 percentage points. In comparison, remittance-receiving 
households have higher consumption allocation for real estate and ownership of dwellings (about 
2 percentage points). Other sectors with a  higher share than non-recipient  households include 
utilities  (1.2  percentage  points),  education  (1.0  percentage  points),  and  information  and 
communication (0.8 percentage points). Remittance recipients also have a slightly higher share 
in the health sector than non-recipients.

Based on our calculations, the share of remittance income used for household consumption is 
about 72.9%, while the rest is either saved or allocated to capital formation activities such as real 
property and construction. Our analysis decomposing the imported content of intermediate and 
final demand shows that about 84.3% of remittance income represents final demand for domestic 
goods, while the rest (15.7%) are imports, which do not constitute domestic output except for the

14 The BSP records remittance transactions as part of the country’s Balance of Payments, so data on personal 
remittances include (1) net compensation received (i.e., gross earnings less taxes, social security contributions, and 
transportation and travel expenses) of overseas Filipino workers abroad who are temporary residents or also referred 
to as “resident OFWs”; (2) personal transfers in cash or in kind of overseas Filipino workers, who have acquired long-
term residence in their host country or “nonresident OFWs”; and (3) capital transfers between resident and 
nonresident households for capital-generating activities such as residential housing construction (Tuaño-Amador et 
al. 2022).

---

<!-- PAGE 25 -->

retail sector. In the following section, we report only the contribution of remittances to domestic 
outputs and value added.

Table 2: Allocation of Household Consumption by Remittance-Receiving and Non-
Remittance-Recipient Households by Sector in 2018 (%)

20

Overall

Remittance- 
Receiving 
Households

Sector

Agriculture, forestry, and fishing 
Mining and quarrying 
Manufacturing

Electricity, steam, water and waste management

Construction 
Wholesale and retail trade; repair of motor 
vehicles and motorcycles 
Transportation and storage

Accommodation and food service activities

Information and communication

Financial and insurance activities

Real estate and ownership of dwellings

Professional and business services 
Public administration and defense; Compulsory 
social security 
Education

Human health and social work activities

11.8 
– 
37.9

4.9

0.1

11.4

3.9

11.9

1.8

1.6

10.6

0.2

0.0

1.9

0.7

Other services 
– = denotes no allocation, FIES = Family Income and Expenditure Survey. 
Source: Authors’ calculations from FIES 2018 microdata.

1.1

Non-Remittance-
Receiving 
Households 
12.4 
– 
38.6

4.6

0.1

11.7

4.0

11.9

1.6

1.7

10.0

0.2

0.0

1.6

0.6

1.0

10.3 
– 
36.4

5.8

0.2

10.5

3.7

11.8

2.3

1.6

12.0

0.2

0.0

2.6

1.0

1.4

Table 3 shows the distribution of baseline remittance-induced final household demand (both in 
terms of amount and share) across sectors that contributed to the production of domestic goods 
and  services  in  the  Philippines  in  2018.  It  shows  that  remittances  contribute  significantly  to 
demand through final consumption. Consumption financed by remittances predominantly goes to 
the manufacturing (₱162 billion), wholesale and retail trade (₱61.2 billion), and agriculture (₱59.2 
billion)  sectors.  Meanwhile,  the  savings/investment  portion  of  remittances  flows  mostly  to  the 
construction sector at ₱118 billion, accounting for a large share of more than 70%. This is followed 
by manufacturing (₱24.7 billion) and agriculture (₱15.9 billion).

---

<!-- PAGE 26 -->

Table 3. Share of Consumption and Savings/Investments in Remittance Income, 2018

21

Sector

Agriculture, forestry, and fishing 
Mining and quarrying

Manufacturing

Electricity, steam, water and waste management

Construction 
Wholesale and retail trade; repair of motor vehicles 
and motorcycles

Transportation and storage

Accommodation and food service activities

Information and communication

Financial and insurance activities

Real estate and ownership of dwellings

Professional and business services 
Public administration and defense; Compulsory 
social security

Education

Human health and social work activities

Other services

Consumption

Savings/Investment

(₱ billion)

(%)

(₱ billion)

(%)

59.2 
–

162.0

26.6

0.6

61.2

19.8

39.4

9.1

8.4

56.1

0.9

0.2

10.0

4.0

5.9

12.8 
–

35.0

5.7

0.1

13.2

4.3

8.5

2.0

1.8

12.1

0.2

0.0

2.2

0.9

1.3

15.9 
0.6

24.7

0.1

118.0

0.1

0.0

0.0

0.8

0.1

0.3

1.2

0.0

0.2

0.1

0.2

162.3

9.8 
0.3

15.2

0.0

72.7

0.1

0.0

0.0

0.5

0.1

0.2

0.7

0.0

0.1

0.1

0.1

Overall 
– = denotes no allocation, FIES = Family Income and Expenditure Survey. 
Source: Authors’ calculations from FIES 2018 microdata.

463.3

Overall contribution of remittance income

Our  micro-macro  model  shows  that  the  share  of  remittance  income  used  by  households  for 
consumption and investment-related activities (in Table 3) translates to about 3.5% of the overall 
economic output (amounting to ₱1.3 trillion or  $24.4 billion) and 3.4% of domestic gross value 
added  (amounting  to  ₱626  billion  or  $11.9  billion)  that  goes  through  various  sectors  of  the 
Philippine economy in 2018.15 Such remittance-induced final demand also implies that about 1.5 
million people are employed, equivalent to 3.7% of the country’s total employment.

Table  4  decomposes  the  overall  economic  contribution  of  remittance-driven  household  final 
demand (both consumption and savings/investment) to the broad 16 I-O sectors. Given the huge 
allocation in the manufacturing sector, the effect of remittance income is largest in the sector in 
both  gross  output  (₱455  billion  or  35.5%  of  gross  output  contribution)  and  value  added  (₱143 
billion or 23% of gross value added).16 This is not only due to the large inflow of remittances into 
the sector but also due to the high sectoral interdependence and output multipliers. As shown in 
Figure  5,  manufacturing  has  the  highest  intersectoral  linkage  for  both  forward  (2.97)  and

15 Note that this contribution only accounts for the purchase of domestic products, while excluding import contents, 
which do not constitute domestic output except in retail sectors. The foreign content (imports) of household final 
demand by remittance recipients amount to 0.7% of GDP. 
16 The contribution of manufacturing to GDP is lower than the contribution to output due to the relatively large import 
contents in the outputs.

---

<!-- PAGE 27 -->

22

backward (1.33) measures.17 Sectors with higher backward and forward linkage indices tend to 
have larger output multipliers, as they generate significant demand for inputs from other sectors 
while  triggering  increased  production  in  the  industries  that  supply  their  inputs.  This  is  intuitive 
because  production  requires  inputs  from  relevant  upstream  sectors  such  as  agriculture  and 
extractive  activities,  while  the  outputs  produced  are  often  used  as  intermediate  input  by  other 
industries.  On  closer  examination,  this  is  particularly  true  for  the  manufacture  of  electrical 
equipment; rubber and plastic products; wood, bamboo, cane, rattan articles and related products; 
paper  and  paper  products;  transport  equipment;  and  machinery  and  equipment  other  than 
electrical.

After manufacturing, agriculture (₱178 billion) and wholesale and retail trade (₱150 billion) also 
generate a large share of remittance-led outputs. Retail trading activities, with a relatively large 
share of expenditure among recipient households, have a high forward linkage index. The savings 
and investment portion of their remittance income also boosts economic output, largely due to 
their  expenditure  on  real  property  and  construction  activities.  In  terms  of  employment  impact, 
remittance-induced final demand benefits the 644,000 people employed in the agriculture sector 
(43%  of  total  employment).  The  impact  of  employment  is  also  high  in  the  wholesale  and retail 
trade sector (209,000) and in construction (154,000).

17 The forward linkage index, also known as the index of sensitivity of dispersion, captures the extent to which the 
sector’s output is used by other sectors as input. In other words, it measures the increase in an industry’s production 
that is driven by an increase in final demand across all sectors of the economy. The backward linkage index, or index 
of power of dispersion, determines the extent to which a sector’s production depends on inputs from other sectors. 
Therefore, an increase in the production of sectors that have relatively high backward linkages generates greater 
demand for the output of other sectors. The output multiplier refers to the total amount of economy-wide production 
induced by final demand in different economic sectors (Miller and Blair 2009).

---

<!-- PAGE 28 -->

23

Table 4: Economic Contribution of Remittance Income by Sector, 2018

Sector

Agriculture, forestry, and 
fishing 
Mining and quarrying 
Manufacturing 
Electricity, steam, water and 
waste management 
Construction 
Wholesale and retail trade; 
repair of motor vehicles and 
motorcycles 
Transportation and storage 
Accommodation and food 
service activities 
Information and 
communication 
Financial and insurance 
activities 
Real estate and ownership of 
dwellings 
Professional and business 
services 
Public administration and 
defense; Compulsory social 
security 
Education 
Human health and social work 
activities 
Other services

Gross Output

(₱ billion) 
178

33 
455 
50

120 
150

44 
46

20

48

81

29

1

15 
5

8

(%) 
14

3 
35 
4

9 
12

3 
4

2

4

6

2

0

1 
0

1

Total 
Source: Authors’ calculations.

1,283

100

Gross Value Added 
(₱ billion) 
89

(%) 
14

Employment 
(‘000s) 
644

(%) 
43

25 
143 
31

55 
106

20 
16

10

26

67

17

0

13 
3

5

626

4 
23 
5

9 
17

3 
3

2

4

11

3

0

2 
0

1

12 
135 
7

154 
209

117 
81

8

9

7

27

1

20 
5

70

1 
9 
0

10 
14

8 
5

1

1

0

2

0

1 
0

5

100

1,506

100

---

<!-- PAGE 29 -->

Figure 5: Sectoral Interdependency and Output Multipliers, 2018

24

Source: Authors’ calculations.

Extension: Simulating a 10% increase in remittance income using the micro-macro model

Extending our micro-macro analysis of remittances, we examine the macroeconomic impact of a 
hypothetical and exogenous 10% across-the-board increase in remittance income of remittance-
receiving  households  in  the  Philippines,  equivalent  to  ₱74.2  billion  ($14.1  billion).  The  model 
integrates a micro-simulated reallocation of household expenditures resulting from higher income 
based on the consumption equation (Equation 1). This will complement our understanding of the 
contribution  of  remittance-led  household  expenditures,  savings,  and  investments  by  providing 
more  insights  into  sector-specific  contributions  to  economic  output  and  value  added.  This 
assumes that non-recipient households are not affected by this exogenous change via potential 
spillover effects.

Figure  6  illustrates  the  results  of  the  microsimulation  results  of  a  10%  increase  in  remittances 
received.  It  shows  that  such  additional  income  reduces  the  average  share  of  food  in  total 
expenditure by 0.09 percentage points among remittance-receiving households.  This decline is 
offset  by  an  increase  in  the  share  spent  on  bank  savings  and  investments  (0.03  percentage 
points)  and  spending  on  real  property  and  housing  construction  (0.03  percentage  points), 
education  (0.02  percentage  points),  durable  goods  (0.02  percentage  points),  and  health  (0.01 
percentage points). In comparison, the estimated reduction in the share of food is much higher 
than the 0.0001 percentage points estimated in Wang, Hagedorn, and Chi (2021) in the context 
of remittance-receiving households in the Kyrgyz Republic as well as the associated increase in 
the  share  of  spending  on  medical  and  related  expenses  (i.e.,  0.0001  percentage  points).  The 
remittance receiving families in the Kyrgyz Republic are mostly in the poor income groups that 
are  highly  dependent  on  remittances  (Gao,  Kikkawa,  and  Kang  2021).  This  could  explain  the 
inelasticity of food items in the shock scenario.

---

<!-- PAGE 30 -->

Figure 6: Simulated Reallocation Impact in the Share of Broad Expenditure Items to Total 
Household Spending

25

Note: Data labels refer to the percent change in the share of expenditure on each commodity item to total 
expenditure. 
Source: Authors’ calculations.

The reallocation effect varies by household income level. The decline in the share of food to total 
expenditures  is  greatest  for  the  higher  income  quintiles  (Figure  Annex  1).  Accordingly,  the 
spending  allocation  to  productive  and  investment  activities  is  also  higher  among  the  wealthier 
households. Aside from food consumption, the share of spending on housing and utilities, as well 
as recreational items such as restaurants and accommodations, has also fallen in the top income 
quintiles. We also note the same pattern of spending reallocation when we look at households 
with different levels of dependence on remittance income, and that the share of food expenditure 
declines when remittance-receiving households have higher dependence on remittance income 
(Figure Annex 2). In addition, the increase in remittances would also boost the share of spending 
on  investment  and  productivity-inducing  items  such  as  bank  savings  and  investments,  real 
property and housing, and education.

Incorporating  the  above  insights  into  the  I-O  analysis,  Table  5  presents  the  simulated 
macroeconomic impact of a 10% increase in remittance income received by households. Overall 
gross output is estimated to be 0.35 percentage points higher (₱128.4 billion or $2.4 billion) than 
the  baseline  level  (₱36.5  trillion  or  $693.9  billion)  if  households  spend,  save,  or  invest  this 
additional  receipt  in  various  sectors  of the  economy.  Downstream  sectors such  as mining  and 
quarrying, as well as electricity, steam, water and waste management, and agriculture, benefit 
from the higher remittance flows and the corresponding increase in final demand from recipient 
families. They benefit from the high output multiplier of the manufacturing sector, which despite 
some  reduction  in  allocations,  continues  to  account  for  a  large  chunk  of  total  spending  by 
remittance-receiving households.

---

<!-- PAGE 31 -->

Table 5: Estimated Impact of a 10% Increase in Remittance Income by Sector, 2018

26

Sector

Agriculture, forestry, and fishing

Mining and quarrying

Manufacturing

Electricity, steam, water and waste 
management 
Construction

Wholesale and retail trade; repair of 
motor vehicles and motorcycles 
Transportation and storage

Accommodation and food service 
activities 
Information and communication

Financial and insurance activities

Real estate and ownership of 
dwellings 
Professional and business services

Public administration and defense; 
Compulsory social security 
Education

Human health and social work 
activities 
Other services

Overall 
Source: Authors’ calculations.

(₱ billion) 
17.8

3.3

45.5

5.0

11.8

15.0

4.4

4.6

2.0

4.8

8.1

2.9

0.1

1.5

0.5

0.8

128.4

Gross Output

% Change 
to Baseline  (₱ billion) 
8.9

Gross Value Added 
% Change 
to Baseline 
0.51

0.52

Employment

(‘000s) 
64.5

1.2

13.5

0.7

15.2

21.0

11.7

8.1

0.8

0.9

0.7

2.7

0.1

2.0

0.6

7.1

150.7

% Change 
to Baseline

0.64

0.57

0.37

0.50

0.39

0.26

0.36

0.47

0.19

0.16

0.36

0.15

0.01

0.17

0.11

0.23

0.37

1.35

0.42

0.56

0.39

0.32

0.26

0.43

0.19

0.18

0.53

0.15

0.01

0.17

0.11

0.14

0.35

2.5

14.3

3.1

5.4

10.6

2.0

1.6

1.0

2.6

6.7

1.7

0.0

1.3

0.3

0.5

62.6

1.55

0.41

0.56

0.39

0.33

0.28

0.39

0.19

0.17

0.57

0.15

0.01

0.17

0.11

0.13

0.34

The results also suggest that the additional remittance income, with its influence to be allocated 
more toward real estate activities, will induce higher output for the real estate and ownership of 
dwellings  and  construction  activities.  Given 
the  high  baseline  expenditure  share  of 
accommodation and food services, the macroeconomic impact of additional remittances in this 
sector remains high. Further, with reallocation toward education and health, the economic output 
induced by higher receipt of remittances also benefits the health care and education sectors. The 
same  pattern  also  applies  to  the  impact  on  value  added  per  sector,  which  is  0.34  percentage 
points  higher  than  the  baseline,  equivalent  to  $1.19  billion  in  2018.  Our  results  are  generally 
consistent  with  those  of  Goce-Dakila  and  Dakila,  Jr.  (2009)  based  on  a  general  equilibrium 
approach. They found that a 5% reduction in remittances received by households is accompanied 
by a decrease in the overall gross output of less than half a percentage point, with the largest 
impact observed in the services sector. Apart from the fact that their analysis uses macro statistics 
for remittances, which can be at least double the actual remittance income of households, their 
results are comparable.

---

<!-- PAGE 32 -->

27

6.  Conclusion and Policy Implications

This study evaluated the contribution of international remittances to overall economic output of 
the migrants’ country of origin using a consistent definition of remittances which is drawn from the 
reported  international  remittance  income  of  the  recipient  households.  Using  the  input-output 
framework, we illustrated how household income from remittances flows into each industry and 
ultimately  into  the  overall  economy.  We  find  that  remittance  income  reported  by  Philippine 
households amounted to ₱1.7 trillion in 2018, equivalent to 44% of the aggregate international 
remittance inflows officially reported by the central bank in the same year. Remittance-financed 
household consumption and investment contributed to 3.5% of the country’s total gross output 
($24.4  billion),  3.4%  ($11.9  billion)  of  gross  domestic  product  (GDP),  and  3.7%  (1.5  million 
individuals)  of  total  employment  in  2018.  In  our  simulation,  a  general  increase  in  international 
remittance income of 10% (equivalent to $1.4 billion) leads to an increase in the country’s GDP 
of  0.34  percentage  points  over  the  baseline,  i.e.,  about  $1.2  billion  in  2018.  The  sectors  that 
benefit the most from the additional remittance-led consumption and savings/investment include 
manufacturing,  construction,  and  agriculture.  Demand  from  remittance  recipients  for  these 
sectors can provide an additional boost to domestic output and value added, as these sectors 
have high multiplier effect.  Sectors such as mining and quarrying and electricity, steam, water 
and  waste  management,  which  have  relatively  low  direct  allocation  on  upstream  sectors, 
experienced  large  increases  in  gross  output  and  gross  value  added  (relative  to  their  baseline 
levels)  because  of  their  strong  linkages  with  manufacturing.  The  exogenous  increase  in 
remittances induces households to reallocate more to investment-related spending, which boosts 
demand and output in the real estate and construction sectors.

Our analysis and findings can guide policymakers in migrants’ countries of origin in many ways. 
First, the study confirms the existence of large differences in the size of international remittances 
reported  by  households  and  the  central  bank,  which  is  an  important  factor  to  consider  for  
remittance data  analysis  at the micro, macro, or both levels. The findings also indicate that an 
attempt to promote the productive use of remittances should not only include remittance-recipient 
households  as  the  target  audiences,  but  also  reach  out  to  migrants/immigrants  and  diaspora 
investors, who likely remit a sizable share of international remittances.

Second, the proposed input-output analysis can be used as a tool to examine how income from 
remittances flows from households to different sectors and to the overall economy, whether they 
are channeled into productive sectors with high sectoral dependence, and what impact it has on 
job  creation. In  other  words,  it  is  possible to  assess  whether remittances  are  creating  virtuous 
cascading  effects  on  the  output  of  the  whole  economy.  The  benefit  of  this  analysis  becomes 
clearer when applied to multiple countries, allowing for comparison. An additional benefit of the 
proposed  micro-macro  analysis,  which  examines  the  share  of  import  contents  that  remittance 
income purchases, is also an alternative assessment of its direct contribution to the economy of 
the migrants’ home country. In addition, our analytical tool can help governments anticipate the 
household- and industry-specific effects of possible fluctuations in remittance flows with relatively 
little data requirement.

Future  research  is  needed  to  close the  gap  between  micro  and  macro remittance  studies  and 
overcome definitional differences.  One is to study the flow of remittance-sourced expenditures 
related  to  family  businesses  or  family  business  investments  that  can  be  financed  from 
remittances. Many household surveys are silent on the source of such investment funds, reporting 
only the net profits earned from the family business as income.  It is also important to conduct

---

<!-- PAGE 33 -->

more research on how migrants, immigrants, and the diaspora themselves consume and invest 
remittances in countries of origin (apart from remitting funds to families) so that we can fill the gap 
in the data and literature. In addition, because of its simple data requirements, our approach can 
be applied to other migrant countries of origin for comparison to broaden our understanding of 
the  impact  and  mechanisms  through  which  remittances  influence  the  economies  of  these 
countries.

28

---

<!-- PAGE 34 -->

29

REFERENCES

Acosta, P. A., P. Fajnzylber, and H. López. 2007. The Impact of Remittances on Poverty and 
Human Capital: Evidence from Latin American Household Surveys. World Bank Policy 
Research Working Paper. No. 4247. Washington, DC: World Bank.

Acosta, E. K., K. Lartey, and F. S. Mandelman. 2009. Remittances and the Dutch Disease.

Journal of International Economics. 79 (1). pp. 102–116. 
https://doi.org/10.1016/j.jinteco.2009.06.007.

Adams, R. H. and A. Cuecuecha. 2010. Remittances, Household Expenditure and Investment in

Guatemala. World Development. 38 (11). pp. 1626–1641.

_____. 2013. The Impact of Remittances on Investment and Poverty in Ghana. World

Development. 50. pp. 24-40. https://doi.org/10.1016/j.worlddev.2013.04.009.

Adams, R. H. and J. Page. 2005. Do International Migration and Remittances Reduce Poverty

in Developing Countries? World Development. 33 (10). pp. 1645–1669. 
https://doi.org/10.1016/j.worlddev.2005.05.004.

Ahmed, V., G. Sugiyarto, and S. Jha. 2010. Remittances and Household Welfare: A Case Study

of Pakistan. ADB Economics Working Paper Series. No. 194. Manila: Asian 
Development Bank (ADB). https://www.adb.org/publications/remittances-and-household-
welfare-case-study-pakistan.

Amare, M. and L. Hohfeld. 2016. Poverty Transition in Rural Vietnam: The Role of Migration and

Remittances. The Journal of Development Studies. 52 (10). pp. 1463–1478.  
https://www.tandfonline.com/doi/abs/10.1080/00220388.2016.1139696.

Amuedo-Dorantes, C. and S. Pozo. 2014. On the Intended and Unintended Consequences of 
Enhanced U.S. Border and Interior Immigration Enforcement: Evidence from Mexican 
Deportees. Demography. 51 (6). pp. 2255–79.  https://www.jstor.org/stable/43697504.

Ang, A., G. Sugiyarto, and S. Jha. 2009. Remittances and Household Behavior in the

Philippines. ADB Economics Working Paper. No. 188.  
https://www.adb.org/publications/remittances-and-household-behavior-philippines.

Ashraf, N., D. Aycinena, C. Martínez, and D. Yang. 2015. Savings in Transnational Households:

A Field Experiment Among Migrants from El Salvardor. The Review of Economics and 
Statistics. 97 (2). pp. 332–51.

Awan, R. U., F. Waqar, S. Rahim, and F. Sher. 2017. Impact of Remittances on Expenditures

and Poverty at Household Level in Pakistan. Pakistan Economic and Social Review. 55 
(2). pp. 415–434. https://www.jstor.org/stable/26616720.

Castaldo, A. and B. Reilly. 2007. Do Migrant Remittances Affect the Consumption Patterns of 
Albanian Households? South-Eastern Europe Journal of Economics. 5 (1). pp. 25–44.

Clemens, M. A. and D. McKenzie. 2018. Why Don't Remittances Appear to Affect Growth? The 
Economic Journal. 128 (612). pp. F179–F209. https://doi.org/10.1111/ecoj.12463.

---

<!-- PAGE 35 -->

30

Cooray, A. 2012. The Impact of Migrant Remittances on Economic Growth: Evidence from

South Asia. Review of International Economics. 20 (5). pp. 985–998.  
https://onlinelibrary.wiley.com/doi/10.1111/roie.12008.

Cox Edwards, A. and M. Ureta. 2003. International Migration, Remittances, and Schooling:

Evidence from El Salvador. Journal of Development Economics. 72 (2). pp. 429–461. 
https://doi.org/10.1016/S0304-3878(03)00115-9.

de Haas, H. 2010. Migration and Development: A Theoretical Perspective. International

Migration Review. 44 (1). pp. 227–264. https://doi.org/10.1111/j.1747-
7379.2009.00804.x.

Dridi, J., T. Gursoy, H. Perez-Saiz, and M. Bar. 2019. The Impact of Remittances on Economic

Activity: The Importance of Sectoral Linkages. IMF Working Paper. No. 175. 
Washington, DC: International Monetary Fund. 
https://www.imf.org/en/Publications/WP/Issues/2019/08/16/The-Impact-of-Remittances-
on-Economic-Activity-The-Importance-of-Sectoral-Linkages-47091.

European Commission, International Monetary Fund, Organisation for Economic Co-operation 
and Development, United Nations, and World Bank. 2009. System of National Accounts 
2008. https://www.elibrary.imf.org/display/book/9789211615227/9789211615227.xml.

Freund, C. and N. Spatafora. 2008. Remittances, transaction costs, and informality. Journal of

Development Economics. 86 (2). pp. 356-366. 
https://www.sciencedirect.com/science/article/abs/pii/S0304387807000818.

Friedman, M. 1957. The Permanent Income Hypothesis. In A Theory of the Consumption

Function. pp. 20–37. National Bureau of Economic Research, Inc.

Gao, X., A. Kikkawa, and J. W. Kang. 2021. Evaluating the Impact of Remittances on Human

Capital Investment in the Kyrgyz Republic. ADB Economics Working Paper Series. No. 
637. Manila: ADB.

Gibson, J., D. McKenzie, H. Rohorua, and S. Stillman. 2019. The Long-Term Impact of

International Migration on Economic Decision-Making: Evidence from a Migration Lottery 
and Lab-in-the-Field Experiments. Journal of Development Economics. 138. pp. 99–115. 
https://doi.org/10.1016/j.jdeveco.2018.12.007.

Giuliano, P. and M. Ruiz-Arranz. 2009. Remittances, Financial Development, and Growth.

Journal of Development Economics. 90 (1). pp. 144–152.  
https://www.sciencedirect.com/science/article/pii/S0304387808001077.

Glytsos, N. P. 1993. Measuring the Income Effects of Migrant Remittances: A Methodological 
Approach Applied to Greece. Economic Development and Cultural Change. 42 (1). pp. 
131–168.

Goce-Dakila, C. and F. G. Dakila, Jr. 2009. Spatial Impact of Overseas Filipino Workers’

Remittances on the Philippine Economy. The Philippine Review of Economics. 46 (2). 
pp. 221–241.

---

<!-- PAGE 36 -->

31

Kikkawa, A., G. Sugiyarto, J. Villafuerte, K. Kim, B. Narayanan, and R. Gaspar. 2021. Labor

Mobility and Remittances in Asia and the Pacific during and after the COVID-19 
Pandemic. ADB Brief. No. 204. Manila: ADB. 
https://www.adb.org/sites/default/files/publication/761401/adb-brief-204-labor-mobility-
remittances-asia-pacific-covid-19.pdf.

McKenzie, D. and H. Rapoport. 2011. Can Migration Reduce Educational Attainment? Evidence

from Mexico. Journal of Population Economics. 24 (4). pp. 1331–58. 
http://www.jstor.org/stable/41488354.

Meyer, D. and A. Shera. 2017. The Impact of Remittances on Economic Growth: An

Econometric Model. EconomiA. 18 (2). pp. 147–155. 
https://doi.org/10.1016/j.econ.2016.06.001.

Mezger, C. and C. Beauchemin. 2010. The Role of International Migration Experience for

Investment at Home: The Case of Senegal. Paris: MAFE.

Miller, R. E. and P. D. Blair. 2009. Input-Output Analysis: Foundations and Extensions. 2nd

Edition. Cambridge: Cambridge University Press.

Mishra, K., O. Kondratjeva, and G. E. Shively. 2022. Do Remittances Reshape Household

Expenditures? Evidence from Nepal. World Development. 157. 105926. 
https://doi.org/10.1016/j.worlddev.2022.105926.

Moon, H. R. and B. Perron. 2005. Efficient Estimation of the Seemingly Unrelated Regression

Cointegration Model and Testing for Purchasing Power Parity. Econometric Reviews. 23 
(4). pp. 293–323. https://doi.org/10.1081/ETC-200040777.

Murakami, E., E. Yamada, and E. P. Sioson. 2021. The Impact of Migration and Remittances on

Labor Supply in Tajikistan. Journal of Asian Economics. 73. 
https://doi.org/10.1016/j.asieco.2020.101268.

Philippine Statistics Authority (PSA). 2020. 2018 Family Income and Expenditure Survey.  
https://library.psa.gov.ph/cgi-bin/koha/opac-detail.pl?biblionumber=15584.

Pratt, S. 2015. The Economic Impact of Tourism in SIDS. Annals of Tourism Research. 52. pp.

148–160.

Ratha, D. 2005. Workers’ Remittances: An Important and Stable Source of External

Development Finance. In Remittances: Development Impact and Future Prospects 
(edited by S.M. Maimbo and D. Ratha). pp. 19-51. 
https://www.knomad.org/sites/default/files/2017-09/32598a.pdf.

Schepelmann, P., A. Vercalsteren, J. Acosta-Fernandez, M. Saurat, K. Boonen, M. Christis, G.

Marin, R. Zoboli, and C. Maguire. 2020. Driving Forces of Changing Environmental 
Pressures from Consumption in the European Food System. Sustainability. 12 (19). p. 
8265. https://doi.org/10.3390/su12198265.

Seriño, M. N. V. and S. Klasen. 2015. Estimation and Determinants of the Philippines'

Household Carbon Footprint. The Developing Economies. 53 (1). pp. 44–62. 
https://doi.org/10.1111/deve.12065.

---

<!-- PAGE 37 -->

32

Shonkwiler, J. S. and S. T. Yen. 1999. Two-Step Estimation of a Censored System of 
Equations. American Journal of Agricultural Economics. 81 (4). pp. 972–982. 
https://doi.org/10.2307/1244339.

Tuaño-Amador, M. A. C. N., V. B. Bayangos, M. E. G. Romarate, and C. F. C. Maliwat. 2022.

Remittances from Overseas Filipinos in the Time of COVID-19: Spillovers and Policy 
Imperatives. Bangko Sentral ng Pilipinas Discussion Paper Series. No. 010. 
https://www.bsp.gov.ph/Pages/MediaAndResearch/PublicationsAndReports/Discussion
%20Papers/DP202201.pdf.

United Nations Department of Economic and Social Affairs, Population Division. 2021.

International Migrant Stock 2020. 
https://www.un.org/development/desa/pd/content/international-migrant-stock.

Wang, D., A. Hagedorn, and G. Chi. 2021. Remittances and Household Spending Strategies:

Evidence from the Life in Kyrgyzstan Study, 2011–2013. Journal of Ethnic and Migration 
Studies. 47 (13). pp. 3015–3036.  
https://www.tandfonline.com/doi/full/10.1080/1369183X.2019.1683442.

Woodruff, C. and R. Zenteno. 2007. Migration Networks and Microenterprises in Mexico.

Journal of Development Economics. 82 (2). pp. 509–528. 
https://doi.org/10.1016/j.jdeveco.2006.03.006.

World Bank. 2023. World Development Report 2023: Migrants, Refugees, and Societies.

Washington, DC. doi:10.1596/978-1-4648-1941-4.

Yang, D. 2008. International Migration, Remittances and Household Investment: Evidence from 
Philippine Migrants’ Exchange Rate Shocks. The Economic Journal. 118 (528). pp. 591–
630. https://doi.org/10.1111/j.1468-0297.2008.02134.x.

Yang, D. and C. A. Martinez. 2006. Remittances and Poverty in Migrants’ Home Areas:

Evidence from the Philippines. In C. Ozden and M. Schiff, eds. International Migration, 
Remittances, and the Brain Drain. Washington, DC: Palgrave Macmillan.

Yang, D. and H. J. Choi. 2007. Are Remittances Insurance? Evidence from Rainfall Shocks in

the Philippines. The World Bank Economic Review. 21 (2). pp. 219–248. 
https://doi.org/10.1093/wber/lhm003.

Yoshino, N., F. Taghizadeh-Hesary, and M. Otsuka. 2017. International Remittances and

Poverty Reduction: Evidence from Asian Developing Countries. ADBI Working Paper 
Series. No. 759. Tokyo: Asian Development Bank Institute. 
https://www.adb.org/publications/international-remittances-and-poverty-reduction.

Zhu Y, Z. Wu, L. Peng, and L. Sheng. 2014. Where Did All the Remittances Go? Understanding 
the Impact of Remittances on Consumption Patterns in Rural China. Applied Economics, 
46(12):1312–1322. 
https://www.tandfonline.com/doi/abs/10.1080/00036846.2013.872764.

---

<!-- PAGE 38 -->

Figure A1: Simulated Reallocation Impact in the Share of Broad Expenditure Items to Total Household Spending, by Income 
Quintile

APPENDIX

33

Source: Authors’ calculations.

Figure  A2:  Simulated  Reallocation  Impact  in  the  Share  of  Broad  Expenditure  Items  to  Total  Household  Spending,  by 
Remittance Dependency

Source: Authors’ calculations.

---

<!-- PAGE 39 -->

Measuring the Contribution of International Remittances  
to Household Expenditures and Economic Output
A Micro–Macro Analysis for the Philippines

This study assesses the simultaneous contribution of international remittance income reported by recipient 
households to the overall economy of the Philippines by integrating micro data and macro simulation based 
on an input–output framework. It finds that remittance-driven household expenditures and investments 
contributed 3.5% of the country’s total output, 3.4% of the gross domestic product, and 3.7% of the total 
employment in 2018. Industries that received the bulk of remittances in the form of final consumption are 
manufacturing, agriculture, and wholesale and retail trade.

About the Asian Development Bank

ADB is committed to achieving a prosperous, inclusive, resilient, and sustainable Asia and the Pacific,  
while sustaining its efforts to eradicate extreme poverty. Established in 1966, it is owned by 68 members  
—49 from the region. Its main instruments for helping its developing member countries are policy dialogue, 
loans, equity investments, guarantees, grants, and technical assistance.

MEASURING THE CONTRIBUTION 
OF INTERNATIONAL REMITTANCES 
TO HOUSEHOLD EXPENDITURES 
AND ECONOMIC OUTPUT 
A MICRO–MACRO ANALYSIS FOR THE PHILIPPINES

Aiko Kikkawa, Raymond Gaspar, Kijin Kim, Mahinthan J. Mariasingham,  
and Christian Marvin Zamora

NO. 714

February 2024

ADB ECONOMICS
WORKING PAPER SERIES

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Kikkawa, Aiko; Gaspar, Raymond; Kim, Kijin; Mariasingham, Mahinthan J.; Zamora,
Christian Marvin
Working Paper
Measuring the contribution of international remittances
to household expenditures and economic output: A micro-
macro analysis for the Philippines
ADB Economics Working Paper Series, No. 714
Provided in Cooperation with:
Asian Development Bank (ADB), Manila
Suggested Citation: Kikkawa, Aiko; Gaspar, Raymond; Kim, Kijin; Mariasingham, Mahinthan J.;
Zamora, Christian Marvin (2024) : Measuring the contribution of international remittances to
household expenditures and economic output: A micro-macro analysis for the Philippines, ADB
Economics Working Paper Series, No. 714, Asian Development Bank (ADB), Manila,
https://doi.org/10.22617/WPS240025-2
This Version is available at:
https://hdl.handle.net/10419/298160
Standard-Nutzungsbedingungen: Terms of use:
Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen Documents in EconStor may be saved and copied for your personal
Zwecken und zum Privatgebrauch gespeichert und kopiert werden. and scholarly purposes.
Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle You are not to copy documents for public or commercial purposes, to
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich exhibit the documents publicly, to make them publicly available on the
machen, vertreiben oder anderweitig nutzen. internet, or to distribute or otherwise use the documents in public.
Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen If the documents have been made available under an Open Content
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten, Licence (especially Creative Commons Licences), you may exercise
gelten abweichend von diesen Nutzungsbedingungen die in der dort further usage rights as specified in the indicated licence.
genannten Lizenz gewährten Nutzungsrechte.
https://creativecommons.org/licenses/by/3.0/igo/

Measuring the Contribution of International Remittances
to Household Expenditures and Economic Output
A Micro–Macro Analysis for the Philippines
This study assesses the simultaneous contribution of international remittance income reported by recipient
households to the overall economy of the Philippines by integrating micro data and macro simulation based
on an input–output framework. It finds that remittance-driven household expenditures and investments
contributed 3.5% of the country’s total output, 3.4% of the gross domestic product, and 3.7% of the total
employment in 2018. Industries that received the bulk of remittances in the form of final consumption are
manufacturing, agriculture, and wholesale and retail trade.
MEASURING THE CONTRIBUTION
OF INTERNATIONAL REMITTANCES
About the Asian Development Bank
TO HOUSEHOLD EXPENDITURES
ADB is committed to achieving a prosperous, inclusive, resilient, and sustainable Asia and the Pacific,
while sustaining its efforts to eradicate extreme poverty. Established in 1966, it is owned by 68 members
—49 from the region. Its main instruments for helping its developing member countries are policy dialogue, AND ECONOMIC OUTPUT
loans, equity investments, guarantees, grants, and technical assistance.
A MICRO–MACRO ANALYSIS FOR THE PHILIPPINES
Aiko Kikkawa, Raymond Gaspar, Kijin Kim, Mahinthan J. Mariasingham,
and Christian Marvin Zamora
ADB ECONOMICS
NO. 714
WORKING PAPER SERIES
February 2024
ASIAN DEVELOPMENT BANK
6 ADB Avenue, Mandaluyong City
1550 Metro Manila, Philippines ASIAN DEVELOPMENT BANK
www.adb.org

ADB Economics Working Paper Series
Measuring the Contribution of International Remittances
to Household Expenditures and Economic Output:
A Micro–Macro Analysis for the Philippines
Aiko Kikkawa, Raymond Gaspar, Aiko Kikkawa (akikkawa@adb.org) and Kijin Kim
Kijin Kim, Mahinthan J. Mariasingham, (kijinkim@adb.org) are senior economists; Mahinthan
and Christian Marvin Zamora J. Mariasingham (mmariasingham@adb.org) is a senior
statistician; and Raymond Gaspar (rgaspar.consultant@
No. 714 | February 2024
adb.org) and Christian Marvin Zamora (czamora.
consultant@adb.org) are consultants at the Economic
Research and Development Impact Department,
The ADB Economics Working Paper Series Asian Development Bank.
presents research in progress to elicit comments
and encourage debate on development issues
in Asia and the Pacific. The views expressed
are those of the authors and do not necessarily
reflect the views and policies of ADB or
its Board of Governors or the governments
they represent.
ASIAN DEVELOPMENT BANK

Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)
© 2024 Asian Development Bank
6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines
Tel +63 2 8632 4444; Fax +63 2 8636 2444
www.adb.org
Some rights reserved. Published in 2024.
ISSN 2313-6537 (print), 2313-6545 (electronic)
Publication Stock No. WPS240025-2
DOI: http://dx.doi.org/10.22617/WPS240025-2
The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies
of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.
ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any
consequence of their use. The mention of specific companies or products of manufacturers does not imply that they
are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.
By making any designation of or reference to a particular territory or geographic area, or by using the term “country”
in this publication, ADB does not intend to make any judgments as to the legal or other status of any territory or area.
This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)
https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound
by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions
and terms of use at https://www.adb.org/terms-use#openaccess.
This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed
to another source, please contact the copyright owner or publisher of that source for permission to reproduce it.
ADB cannot be held liable for any claims that arise as a result of your use of the material.
Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish
to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use
the ADB logo.
Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.
Notes:
In this publication, “P” refers to Philippine pesos and “$” refers to United States dollars.
ADB recognizes “China” as the People’s Republic of China, “Kyrgyzstan” as the Kyrgyz Republic,
and “Vietnam” as Viet Nam.

ABSTRACT
The macroeconomic studies that assess the contribution of international remittances to the origin
countries of migrants use a different definition of remittances than the microeconomic literature
that examines the impact at the household and community levels. This study overcomes this
difference in definition by integrating household expenditure data into the input-output analysis.
Using the 2018 Family Income and Expenditure Surveys (FIES) of the Philippines, we find that
remittance-financed household consumption and investment totaled ₱742.2 billion ($14.1 billion)
and contributed 3.5% of the country’s total output, 3.4% of gross domestic product (GDP), and
3.7% of total employment in 2018. We note that the largest value added is accruing to the
manufacturing sector as it accounts for more than a third of remittance recipients’ spending basket
followed by the trade and agriculture, forestry, and fisheries sectors, which are closely linked to
the manufacturing industry. The international remittances income reported by households is less
than half (43.8%) of the ₱1.7 trillion ($32.2 billion) aggregate international remittances reported
by the central bank in the same year based on the balance of payments definition.
Keywords: international remittance, household expenditure, micro–macro analysis, Philippines
JEL codes: F24, C67, D12
_______________________
The authors would also like to acknowledge the contribution of the other members of the ADB Statistics
and Data Innovation team: Elyssa Mariel Mores, Julian Thomas Alvarez, Arushi Gupta, and Mimika
Mukherjee.

1. Introduction
In 2022, about $350 billion worth of international remittances flowed to developing economies in
Asia.1 The economic contribution of remittances, commonly measured by their relative share of a
country’s gross domestic product (GDP), is substantial in the major migrant source countries,
including Nepal (23%), the Philippines (9%), Pakistan (8%), and many Pacific countries such as
Tonga (44%), and therefore plays an important role in advancing economic development.
Remittances largely go to migrants’ families, supporting their consumption and sometimes their
investment activities. Given the continued inflow of remittances to developing countries, there is
a large body of empirical literature that examines its short- and long-term effects on recipient
families’ poverty status, savings and investment patterns, and human capital development. The
impact of remittances is also well studied at the aggregate level, with links to national output and
growth as well as economic cycles and other macroeconomic fundamentals.
Evidence from the microeconomic literature suggests that international remittances help smooth
household consumption of basic foods and other essentials, improving the welfare and living
conditions of migrant families (e.g., Awan et al. 2017; Acosta, Fajnzylber, and Lopez 2007;
Mezger and Beauchemin 2010; and Woodruff and Zenteno 2007). Remittances also flow into
children’s education and family businesses, increasing long-term household productivity (e.g.,
Yang 2008; Cox Edwards and Ureta 2003; Gibson et al. 2019). There is an equally large body of
macroeconomic literature that examines the impact of remittances on overall economic growth
(e.g., Meyer and Shera 2017; Giuliano and Ruiz-Arranz 2009; and Cooray 2012), poverty (e.g.,
Ahmed, Sugiyarto, and Jha 2010; Yoshino, Taghizadeh-Hesary, and Otsuka 2017; and Adams
and Page 2005), and other economic fundamentals (e.g., Ratha 2005).
In general, microeconomic and macroeconomic literature complement each other to provide a
comprehensive assessment of the impact of remittances on migrants’ households and
communities, as well as on the overall economy of countries of origin. However, caution should
be exercised when comparing the two sets of literature, as the definition and data source for
international remittances differ significantly. In micro-level studies, remittances refer to the amount
of income households report receiving from abroad, whether in cash or in kind. At the macro level,
by contrast, remittances are the aggregated total of personal remittances reported by financial
institutions and intermediaries, which necessarily include the amount that migrants send to their
families and to elsewhere such as their own personal bank accounts.
A notable source of discrepancy can be attributed to the large sums of remittances that migrants
and the diaspora transfer directly to their bank accounts back home or to other investments that
remain independent of and undisclosed to household members. This type of remittance may be
captured in macro remittances but is unlikely to be reported in household surveys. Another
important source of difference is in the way informal remittances, or funds that flow through
nonformal channels, are treated. At the household level, remittance income is reported regardless
of the channels through which the funds flow, although there may be cases where informal
1 This refers to developing member countries (DMCs) of the Asian Development Bank.

2
remittances are underreported. In contrast, aggregate remittance statistics reported by central
banks often do not include informal remittances.2
Clemens and McKenzie (2018) documented a large discrepancy in the growth trend of
remittances between micro and macro remittance data sources. They found that total remittance
growth reported by all households typically ranges from about 8% (in the case of Pakistan) to
72% (El Salvador) of the growth in aggregate remittances reported by central banks over the
same period. These differences in definition make it difficult to evaluate the contribution of
remittances to economic output and growth in a way that is consistent across micro and
macroeconomic settings.
In this paper, we propose to assess the simultaneous contribution of international remittances to
household expenditures and the overall economic output of the migrants’ country of origin by
using the definition of remittances from the micro literature.3 We examine how the reported
expenditures (referring here to both consumption and savings or investment activities) of
remittance-recipient households effectively flow through the overall economy, taking into account
the impact on individual sectors and their linkages. Using the case of the Philippines, one of the
major source countries of international migrants, this study links household data and insights to
the input-output table, which systematically presents all economic activities of a country,
consisting of production, consumption, and investment, while showing the interdependencies
among industries. Based on this micro-macro analysis approach, we estimate the combined first-
degree impact of remittances generated by direct consumption or expenditure and the second-
degree impact, capturing how remittance-induced purchases of goods and services spill over to
other sectors through multiplier effects and the value chain.
We note that based on the 2018 Family Income and Expenditure Surveys (FIES), household
expenditures financed by remittances were estimated at ₱742.2 billion (or $14.1 billion).4 It is
worth noting that this amount represents less than half (44%) of the total official international
remittance inflows to the country reported by the Bangko Sentral ng Pilipinas (BSP) for the same
year. We observe different household expenditure patterns between remittance-receiving
households and non-remittance-receiving households depending on the extent of their
dependence on remittance income. On average, recipient households spend more (as a
percentage of their total expenditures) on education, real property and construction, and health.
Our micro-macro analysis shows that remittance-induced household expenditures contributed
3.5% of the country’s total output, leading to 3.4% of the country’s GDP through its value addition
and to 3.7% of total employment in 2018.5 The industries that generate the most value added
from the direct revenue of the consumption portion of remittances include manufacturing (25% of
the total contribution to GDP), followed by wholesale and retail trade (17%), and agriculture,
forestry, and fishing (14%). The savings or investment portion of household remittance income
goes mostly to construction (9%). Should international remittances received by households
arbitrarily increase by 10% (equivalent to ₱74.2 billion or $1.4 billion), total domestic demand will
2 Some countries, based on information of their nationals abroad, adjust their inward international remittance statistics
to include remittances from informal channels; thus, the aggregate remittance statistics reported by the World Bank
are also adjusted for informal remittances (Freund and Spatafora 2008).
3 This paper focuses on international remittances, which can be compared with data from BOP. Therefore, we do not
include domestic remittances when referring to remittances unless specifically stated.
4 Based on the average exchange rate of the Philippine peso to the US dollar rate of ₱52.66 in 2018.
5 The BSP reported the headline figure of aggregate remittances at the equivalent of 9.3% of GDP in 2018 based on
balance of payments definition.

3
be 0.29 percentage points higher than in the baseline scenario, resulting in an increase in output
of 0.35 percentage points (≈$2.4 billion) and contributing to overall GDP growth of 0.34
percentage points (≈$1.2 billion) and employment growth of 0.36 percentage points (equivalent
to nearly 150,000 jobs). The influence of an increase in remittance income on the expenditure
reallocation toward investment activities boosts demand and thus the output for real estate and
construction activities.
The next section provides a brief overview of the literature on remittances and economic
development, focusing on empirical evidence of their influence on household expenditure and
savings and the overall macroeconomy. Section 3 outlines the data and methods used in the
micro-macro analysis and modeling exercises. Section 4 presents key insights and other findings
from the micro-household data, while section 5 presents the results of the micro-macro analysis,
quantifying the sectoral and overall impact of remittances on growth. The final section draws
evidence-based policy implications and concludes.
2. Background and Literature Review
The extensive literature quantifying the impact of remittances can be divided into two groups of
papers. One examines the effect on the welfare and productivity of recipient households based
on micro datasets, while the other performs either panel data estimation or macro-modeling
techniques using aggregate data on remittance inflows and estimates the impact on the overall
economy and other macroeconomic indicators.
Researchers find that the receipt of remittances has enabled households to fund daily
consumption and productive investment. Yang (2008) showed that the exogenous increase in
remittances due to the exchange rate shock triggered by the 1997 Asian financial crisis was
primarily used by Filipino households for investment-related expenditures, especially education
and microenterprises. In Guatemala, Adams and Cuecuecha (2010) found that households that
received international remittances from the United States spent more on education (194%) and
housing (81%) than they would have spent on these items in the absence of remittances.
Amuedo-Dorantes and Pozo (2014) found that income from international remittances had a
greater impact on Mexican households’ health expenditures than other sources of income. Using
visa lottery as a natural experiment, Gibson et al. (2019) show that large gains from Pacific
migrants are not only short term but also long term. Mishra, Kondratjeva, and Shively (2022), who
conducted an instrumental variable analysis using the 2010/11 Nepal Living Standards Survey,
found that households receiving remittances spend more on food and education, suggesting a
long-term increase in productivity. According to their estimate, a 10% increase in the annual value
of remittances received increases average monthly food consumption by 0.9% and annual
educational expenditure by 8%.
Remittances supplement domestic income and help households escape poverty and insure
against income shocks. Yang and Martinez (2006) observed 2.8 percentage point reductions in
the poverty rate among recipients of international remittances in the Philippines amid an increase
in migrant households’ remittance receipts equivalent to 10% of precrisis household income.
Remittances have also been found to help households in rural Viet Nam exit poverty, particularly
through asset growth, although the impact varies by the welfare status and ethnicity of the
recipient (Amare and Hohfeld 2016). Meanwhile, also in the Philippines, using local rainfall
changes as an identification strategy, Yang and Choi (2007) generally observed how remittances

4
respond to income shocks, smoothing household consumption. Other researchers also find a
significant increase in establishing capital-intensive enterprises among recipient households.
However, not all empirical studies attribute positive outcomes to remittances. Several studies also
suggest that remittances may fuel conspicuous consumption and/or disincentivize human capital
investment if a typical job abroad does not require skills or if the children left behind, especially
boys, are mobilized to work to meet labor needs (e.g., McKenzie and Rapoport 2011; Ang,
Sugiyarto, and Jha 2009; and Gao, Kikkawa, and Kang 2021). In some countries, income from
remittances is found to reduce the incentive to work in recipient households (e.g., Acosta, Lartey,
and Mandelman 2009; Murakami, Yamada, and Sioson 2021).
Meanwhile, the macro-level empirical literature tackled the contribution of international
remittances to the recipient country’s macroeconomic fundamentals, including growth, inflation,
exchange rate, and national poverty rate. Cooray (2012) used the growth model approach to
examine a panel data of South Asian countries over the period 1970–2008 and found that a 1%
increase in migrant remittances contributed to a 0.01% increase in economic growth. Giuliano
and Ruiz-Arranz (2009) also reached a similar finding using a newly constructed dataset for
remittances covering about 100 developing countries. However, the positive reinforcement of
remittances on growth is more pronounced in countries with less developed financial systems,
suggesting that these flows have helped overcome liquidity constraints. Similar findings can be
found in Meyer and Shera (2017), who examine panel data of high remittance-receiving countries
in Eastern Europe during the period 1999–2013.
Using computable general equilibrium model, Ahmed, Sugiyarto, and Jha (2010) found that a
hypothetical 50% reduction in remittance flows would have a devastating impact on the poverty
situation in Pakistan—with the poverty headcount ratio increasing by 6.4%. By constructing and
analyzing a broader set of 71 developing countries, Adams and Page (2005) found that
international remittances significantly reduce the level, depth, and severity of poverty in the
developing world. Addressing endogeneity issues, they found that a 10% increase in official
international remittances per capita leads to a 3.5% decline in the share of people living in poverty.
Relatedly, Yoshino, Taghizadeh-Hesary, and Otsuka (2017) studied data from 10 developing
Asian countries from 1980 to 2014 and found that a 1% increase in international remittances (as
a percentage of GDP) can lead to a 22.6% decline in the poverty gap and a 16.0% decline in the
poverty severity ratio. Using the Philippines as a case study, Goce-Dakila and Dakila, Jr. (2009)
found that a 5% reduction in remittances received by households is accompanied by a decrease
in overall gross output of less than half a percentage point, with the largest impact observed in
the services sector. Further, Ratha (2005) has elaborated on the importance of workers’
remittances as a stable source of external funding in developing recipient countries, which may
even be countercyclical during a growth slowdown. This was evident during the coronavirus
disease (COVID-19) pandemic (Kikkawa et al. 2021).
The empirical insights at the micro and macro levels complement each other and allow for a more
comprehensive assessment of the impact of remittances on migrants’ families and communities,
as well as on the overall economies of countries of origin. However, care must be taken when
comparing and synthesizing the two sets of findings, as the definitions of international remittances
used in the micro and macro literature are not identical and the data sources are distinct. In micro-
level studies, international remittances typically refer to the cash or in-kind income that
households reported receiving from abroad in surveys. At the macro level, international

5
remittances refer to nationally aggregated external financing reported by financial institutions and
intermediaries.
Varying definitions and data sources mean that some remittance flows are counted in one country
but not in another country. One stream of remittances that is captured in macro statistics but not
likely in micro data is the remittances that flow into migrants’ own bank accounts or into direct
investments such as real estate. Personal bank accounts that are not known or accessed by
other family members are reportedly preferred by migrant workers because it gives them more
control over the allocation (Ashraf et al. 2015).
Another source of inward remittances that is treated differently in micro and macro remittance
statistics is informal remittances, which generally refer to transfers of funds that are not coursed
through formal financial intermediaries. Household surveys potentially report all remittance
income received by households in a given period, regardless of the channels through which these
funds were transferred, although there may be cases where households underreport informal
remittances. In contrast, macroeconomic remittance statistics, typically reported by central banks,
do not include informal remittances except that some countries or datasets adjust aggregate
remittance data based on migrant stock abroad to include informal remittances (World Bank
2023). There is also a form of income from abroad that does not appear in any of the statistics,
such as unreported cash hand-carried by migrants that they save or consume themselves.
Apart from definitions, measurement errors can also lead to different sizes and trends in macro
and micro remittance data. For macro data, there have been frequent changes in the official
definition. Until 2005, using the Balance of Payments Manual (BPM) 5, remittances comprise
workers’ remittances and compensation of employees. Amid the difficulty of separating transfers
made by migrant workers from their employment income from a number of other transfers,
remittance statistics using the BPM6 now comprise personal transfers and compensation of
employees (Clemens and McKenzie 2018).6 Even remittance data based on household surveys
are not free of measurement error, particularly due to misreporting and recall errors. In addition,
a typical national household income expenditure survey may not report (exclude) remittances
receipts that are channeled to family businesses and cottage industries because the funds are
then categorized to a separate household production module to derive household business
income.
The discrepancy in remittance growth between macro data and household survey-based micro
data is documented in Clemens and McKenzie (2018) for many major migrant-sending developing
economies. They note that the growth in total remittances reported by households typically ranges
from about 8% (Pakistan) to 72% (El Salvador) of the growth in aggregate remittances reported
by the central bank for the same period. The discrepancy between the data could possibly explain
the differences in the results of the analysis used to evaluate the impact of remittances in migrants’
countries of origin in the micro and macro literature.
We propose to assess the short-run contribution of remittances to household expenditures and
national-level output by using a consistent definition of remittances: the expenditure of recipient
households. We feed micro-level remittance data to that of the macro-level analysis in accordance
to how households spend, save, and invest their remittance income in specific sectors of the
6 Another item that may be included in macro remittances but not in micro household data is the inward transfer of a
third-country national (as seen recently in the surge in remittances to Central Asian countries from migrating Russian
nationals due to the Russian invasion of Ukraine).

6
economy and examine the magnitude of the macroeconomic impact of remittances using the so-
called network of input–output linkages between different economic sectors. It can be
hypothesized that household spending on goods and services in certain sectors that have strong
sectoral economic linkages and value chains amplify the effect of remittances on the aggregate
economy beyond direct consumption. The input-output (I-O) framework is one of the
macroeconomic models that allows aggregate household-level expenditure and savings to be
applied to industry sectors and the economy as a whole, and the impact to be assessed at a given
point in time (Miller and Blair 2009). It clearly illustrates how different sectors contribute to the
overall output by considering the interlinkages using a country-specific matrix that represents the
structure of the economy.7
To date, there are a few studies that attempt to evaluate the macroeconomic contribution of
remittance-induced expenditure using the I-O model, or that attempt to feed micro-level
information and insights into the framework to evaluate its impact on overall growth. The work of
Dridi et al. (2019) and Glytsos (1993) are most relevant to our proposed methodology for
establishing micro-macro linkages to evaluate the contribution of remittances to household
expenditure and the overall economy. Dridi et al. (2019) proposed a macroeconomic model to
quantify how changes in aggregate demand due to additional income from household remittances
propagate through the network of input-output linkages in sub-Saharan African countries. They
find that countries with intricate and mutually dependent industrial linkages benefit more from
remittance-led demand. In this paper, consumption preferences are determined using a
macroeconomic model, but without micro data that provide more detailed preferences of
heterogeneous households, including those with and without remittances. Given that many
studies indicate distinct consumption patterns of migrant households, the assumption of
homogeneous households is questionable.
Meanwhile, Glytsos (1993) incorporated information on the pattern of expenditure of remittance
recipients from a Greek household survey into the country’s input-output table. By converting the
pattern of consumer expenditures into a structure of industry final demand, he estimated that the
remittances received resulted in a gross output equivalent to 4.1% of the economy’s total gross
production in 1971 and created 74,000 new jobs in the non-agriculture sector. The model
proposed by the study, however, is very data intensive, as it requires a longitudinal series of
household micro data accompanied by corresponding I-O tables to establish causal impact.
3. Methodology and Data Sources
The paper conducts a micro-macro analysis using data from a single-year household survey—
the 2018 FIES—and I-O tables to estimate the effect of remittances on household expenditures
and on the sectoral and overall economy. It uses a simple and straightforward methodology that
illustrates and quantifies the short-term contribution of remittances to household expenditures and
overall economic output, taking into account the impact on individual sectors and their
interlinkages. The micro-macro analytical approach requires a minimum set of data that are
commonly available in many developing economies: (i) household income and expenditure
7 The I-O framework has been used in the existing literature to assess the environmental impact of household
consumption (e.g., Seriño and Klasen 2015; Schepelmann et al. 2020) or evaluating the impact of tourism on output
and growth (e.g., Pratt 2015 for seven small-island developing states). Unlike the CGE model, the I-O model’s impact
assessment can also be done with simple data and solution software.

7
surveys, and (ii) I-O tables. We follow a two-step process: (i) tracing remittance income received
by households and identifying how it is spent, invested, or saved; and (ii) quantifying the
contribution of this expenditure to sectoral and overall economic output. We use the Philippines,
which is one of the largest sources of migrant workers and remittance recipients in Asia, as a
case study.
STEP 1: Micro-level analysis of household spending and saving pattern
The first step is to examine the expenditure patterns and the allocation by commodity items of
remittance-receiving households.8 We generate descriptive statistics and estimate consumption
equations to derive the marginal propensity to consume, which we allow to vary by household
characteristics such as income quintile and remittance dependency. We use the Philippine
Statistics Authority’s microdata of the 2018 FIES. The survey interviewed a sample of about
180,000 households, and the dataset generates the weighted sample of about 25 million
households deemed present in 2018.9 The dataset provides reliable estimates of income and
expenditure at different spatial levels, including national, regional, provincial, and highly urbanized
cities (PSA 2020).
The per item consumption equations are estimated, taking into consideration the households’
remittance-receiving status. This information allows us to allocate changes in aggregate
consumption when we conduct simulations for remittance shock scenarios using the I-O model.
We estimate the consumption equations closely following the empirical specification of Wang,
Hagedorn, and Chi (2021), with some additional assumptions about how income from remittances
is allocated and utilized in a remittance-receiving household:
𝐶 =𝛼 +𝛽𝑇𝐼𝑛𝑐 +∑(cid:2872) 𝛾 𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦 +
(cid:3036)(cid:3037) (cid:3036) (cid:3036) (cid:3037) (cid:3041)(cid:2880)(cid:2869) (cid:3036)(cid:3041) (cid:3037)
∑(cid:2872) 𝜌 (cid:3435)𝑇𝐼𝑛𝑐 ×𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦 (cid:3439)+𝛿𝐗 +𝜀 (Equation 1)
(cid:3041)(cid:2880)(cid:2869) (cid:3036)(cid:3041) (cid:3037) (cid:3037) 𝐣 (cid:3036)(cid:3037)
The dependent variable, 𝐶 , refers to the share of each expenditure item 𝑖 in the total expenditure
(cid:3036)(cid:3037)
of household 𝑗. Here, we categorize total household living expenses into 16 broad commodity
items: food, tobacco and alcohol, housing and utilities, durables (including vehicles), clothing,
furnishings, health, transport, communications, education, recreation, finance, real property and
construction, miscellaneous expenses, real property and new construction, and bank savings and
investments. Note that the limited details in the FIES do not allow the identification of relevant
expenditures related to family enterprises that may have been financed by the receipt of
remittances.
The coefficient, 𝛽, refers to the percentage point change in the share of expenditure item 𝑖 in total
(cid:3036)
expenditure given a percentage change in total household income. Unlike Wang, Hagedorn, and
Chi (2021), who distinguish between remittance and non-remittance income by obtaining a unique
parameter of marginal propensity to consume for each income, we use household’s 𝑇𝐼𝑛𝑐 or total
(cid:3037)
income (in log) regardless of sources. In other words, we assume that remittance income is as
fungible as all other sources of income, such as wages and salaries. This is consistent with
8Throughout the paper, remittance-receiving households are defined as households receiving cash income from
abroad, which is our measure of remittance income. Note that this variable from the FIES questionnaire also includes
other sources of income from abroad, such as (i) pensions, retirement, workmen’s compensation, and other benefits;
(ii) cash gifts, support, relief, etc. from abroad; and (iii) dividends from investments abroad.
9 This translates to about 25 million Filipino households in 2018 as defined by the Philippine Statistics Authority,
which is highly consistent with the more than 26 million Filipino households recorded in the 2020 Census of
Population and Housing. The survey response rate was 92.5% (PSA 2020).

8
several studies that corroborate Friedman’s (1957) permanent income hypothesis. For example,
Castaldo and Reilly (2007) found only modest effect of receipt of international remittances on the
marginal spending behavior of households in Albania. Further, such a modest effect was found
only for food consumption. Meanwhile, a study based on the 2005 Ghana Living Standards
Survey found almost negligible changes in household spending behavior (Adams and Cuecuecha
2013).
Our assumption of fungibility of remittance income also seems consistent with the pattern of
remittances and other sources of income among Filipino households. Descriptive statistics show
that Filipino households typically rely on more than two sources of income and that the share of
overseas remittances to the total household income does not exceed 50% for the majority (83.9%)
of remittance-receiving households (see more details on descriptive statistics in the next section).
In addition, we found that as much as 64% of recipient households of international remittances
also report income from domestic remittances, which poses a methodological challenge to identify
the particularities of the expenditure allocation of international remittances income.
In equation 1, we also introduced a control variable indicating the extent of household
dependence on remittance income by adding the interaction between total household income,
𝑇𝐼𝑛𝑐 , and the categorical variable, 𝑟𝑒𝑚𝑖𝑑𝑒𝑝𝑒𝑛𝑑𝑒𝑛𝑐𝑦 , which is based on the share of remittance
(cid:3037) (cid:3037)
income to the total income of household 𝑗 at a 25% interval (hence, resulting in five independent
household groups including nonrecipients). The coefficient 𝜌 provides a measure of how 𝛽
(cid:3036) (cid:3036)
differs across household groups. This approach is intended to capture the possibility that the
share of income from remittances may have different effects on consumption patterns.
Household-level characteristics 𝐗 , include household size, share of members below the age of
𝐣
5, share of members aged 5 to 17 years, and household head characteristics such as age, gender,
marital status, educational attainment, and job status. Place of residence (urban or rural) and
region are also controlled for in the model. The idiosyncratic error term 𝜀 is assumed to be
(cid:3036)(cid:3037)
uncorrelated with the explanatory variables. The set of equations in (1) is estimated using the
seemingly unrelated regression technique of Shonkwiler and Yen (1999), allowing the error to be
correlated across equations (Moon and Perron 2005).
The consumption equations do not provide insights to evaluate the potential impact or causal
inference of migration and remittances on the consumption behavior of recipient households.
Instead, our primary objective is to understand how households allocate their income, including
income from international remittances and expenditures based on their revealed expenditure
patterns.
STEP 2: Macrosimulation using the input-output framework
The second step in constructing the micro-macro analysis model is to aggregate households’ total
income from international remittances and their expenditures (consumption and investment)
reported in the FIES and map them to the macro-level input-output table. As mentioned, it is
expected that the total income from remittances reported by households will differ from the
international remittance data reported by the central bank due to the differences in definitions and
data sources. We feed remittance income allocated toward expenditure and savings and
investment to the 2018 Benchmark Input-Output (I-O) Accounts of the Philippines in the form of
final demand from households and evaluate its impact on sectoral and overall output. As an
additional exercise, we simulate how a 10% increase in remittance income changes expenditure

9
patterns using the consumption equation and how the changes translate to sectoral and overall
output.
a. Mapping commodity items to I-O sectors
Commodity items from the 2018 FIES are mapped to the 80-sector disaggregation of the 2018 I-
O table.10 The FIES-IO concordance matrix11 allows a one-to-one matching that largely considers
the sectors that produced (or delivered) the commodity (or service). However, the matrix leaves
out retail and wholesale trade sectors (I-O sectors 54 and 55) from which a majority of the goods
were purchased. To overcome this limitation, we collect retail and wholesale trade margins by
sector from the 2016 Annual Survey of Philippine Business and Industry and use them to allocate
a portion of the value of commodity items that should go to retail and wholesale trade sectors.12
We also differentiate the purchase of domestic products out of remittances from that of foreign
products (whereby the latter does not constitute domestic output except in retail sectors). We
derive a matrix containing import demand levels of intermediate and final demand components
by sector and deduct it from the published 2018 input-output table.
b. Deriving I-O household final demand driven by remittance income
The final demand from households refers to their final expenditure, which consists of their
consumption (the sum of household spending on various consumption items) and their savings
or investment (items such as bank savings, real estate purchases, and construction and/or major
renovations). To determine the aggregate expenditure of households, we first calculate the portion
of remittance income used for consumption and savings or investment per household. We
assume that households spend their remittance income on consumption in the proportion
equivalent to the share of remittance income in total income. Household savings are the residual
of income and their total consumption plus deposits in banks/investments, purchase/amortization
of real property, and money used either to build a new house or for major repair or renovation of
an existing house, according to the System of National Accounts 2008 guide (European
Commission et al. 2009).
We calculate the sum of remittance-financed consumption and savings of all households to
determine the aggregate amount of expenditure and the savings component of remittances. The
sum of expenditures forms part of household final consumption expenditures, while the savings
10 The 2018 Benchmark I-O Accounts of the Philippines include the I-O transaction table, the technical coefficient
matrix, and the Leontief inverse matrix in three dimensions (i.e., 16x16, 80x80, and 240x240) corresponding to the
sectoral disaggregation.
11 The detailed expenditure items in the FIES follow the classification system, Philippine Classification of Individual
Consumption According to Purpose (PCOICOP). To maintain their equivalence with the I-O sector, we follow the four-
step conversion process in consultation with the Philippine Statistics Authority:
1) PCOICOP to 2002 Philippine Central Product Classification (PCPC)
2) 2002 PCPC to 1994 Philippine Standard Industrial Classification (PSIC)
3) 1994 PSIC to 2009 PSIC (Updates to 1994 PSIC)
4) 2009 PSIC to 2018 I-O Sectors
Using the concordance above, the commodity items with PCOICOP codes 011121 (corn on the cob), 011121 (whole
corn/grain), 011121 (corn grits), and 011121 (other corn, corn starch, etc.) are all classified under I-O sector 02
(Growing of corn).
12 For example, retail and wholesale trade margins for I-O sector 02 of commodities are both 9%; thus, if the total
expenditure on such commodities is ₱100.00, we allocate ₱9.00 each to retail and wholesale trade.

10
form part of gross fixed capital formation. The combined aggregate of the two is synonymous to
the level of final demand induced by remittances, which we shall collate as the vector 𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047).
c. Estimating impact of remittance-sourced household final demand on output and employment
The contemporaneous impact of remittance-financed demand on the gross output of the economy
is estimated using the 80-sector I-O table. For ease of presentation, the estimates are later
aggregated into 16 I-O sectors. To estimate the baseline outputs per production sector i induced
by remittances (𝑥(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)), the final demand vector derived from the earlier steps, 𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047), is
(cid:3036)
multiplied by the 80-sector Leontief inverse matrix (𝑩) published by the Philippine Statistics
Authority (PSA), i.e.,
𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047) = 𝑩⋅𝒚(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)
where 𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047)denotes the vector of sectoral gross outputs realized through remittances, which
entail both direct and indirect impacts. Once 𝒙(cid:3045)(cid:3032)(cid:3040)(cid:3036)(cid:3047) is obtained, it is multiplied elementwise by the
vector of sectoral employment-to-output ratios, 𝑒 , to derive the level of employment per sector
associated with remittances. Sectoral employment-to-output ratios are estimated using the
employment per I-O sector based on the 2018 Labor Force Survey and gross output per sector
based on the 2018 I-O table.
d. Extension–Simulation with exogenous change in remittance income
As an extension of the model, we also simulate the impact of a 10% increase in remittance income
on gross output and employment. We estimate the share of each sector in every household’s total
expenditure with and without the hypothetical increase in remittance income. The hypothetical
change in the aggregate expenditure (both consumption and savings) is derived from a micro
simulation based on the results of the consumption equations.
4. Remittance Income and Reported Household Expenditures in the Philippines
The Philippines is a major country of origin for international migrants, sending an average of more
than 2 million workers each year since 2016.13 The United Nations Department of Economic and
Social Affairs Population Division (2021) estimates that about 6.1 million Filipinos currently live
abroad, representing 5.4% of the country’s total population. In 2018, up to 29.7% of all households
in the Philippines received cash from abroad. Remittance-receiving households are distributed
across all income groups, with a higher representation in the higher quintiles (Figure 1a). This is
consistent with the general observation that international migration is not as common among the
poor, who cannot afford the initial costs of migration (de Haas 2010). The share of remittance
income in total household income increases with income level, from an average of only 16% in
the lowest quintile to 31% in the highest income group. International remittances have the highest
share (31%) in the top income quintile, which is even higher than income from wages and salaries.
13 However, this number declined during the COVID-19 pandemic due to travel restrictions and suppressed global
economic activity.

11
Figure 1: Philippine Households by Receipt of and Dependence on International
Remittances and Income Quintile, 2018
a. By Receipt of International Remittances b. Remittance-Receiving Households’
Dependence on Remittances
Notes: In (a), the numbers inside the blue bar represent the share of remittance-receiving households to total number
of households per income quintile.
Source: Authors’ calculations.
Remittance income accounts for only a quarter or less of their total income for more than the
majority (61.8%) of the overall remittance-receiving households (Figure 1b). Another 22.1% report
that remittances account for 26%–50% of their total income, while the remaining households
(16.1%) use remittances as their primary source of income, with about one-third of households
reporting that they rely heavily on remittances (over 75%). The dependency on remittances as a
source of income is greater among households in higher income brackets.
Household Consumption and Savings by Remittance Receiving Status
The average annual spending of a Filipino household reached ₱239,000 (≈ $4,538.4). Figure 2
shows the share of each broad commodity including savings and investments, in total household
expenditures, comparing the remittance-receiving and non-recipient households. The overall
spending allocation patterns of the two groups of households on the various commodities are
similar. However, there are significant differences in the share of some commodity items, such as
food, housing, health, and education. The allocation of remittance-receiving households in food
expenditures (35.6%) is relatively lower than the share of non-remittance-receiving households
(42%). In contrast, spending on housing and on productivity-enhancing items such as health and
education is relatively higher among remittance recipients. Remittance-receiving households also
spend more on investments, in terms of share to their total expenditure, such as real property,
major repairs or renovations, and construction of new houses, as well as on bank savings and
investments.

12
Figure 2: Share of Broad Expenditure Items to Total Expenditure, by Receipt of
Remittances, 2018
Source: Authors’ calculations.
The observed heterogeneity in expenditure patterns could be due to the skewed distribution by
income of remittance-receiving households. Figure 3 shows the share of total expenditure on
broad commodity items, by income quintile and receipt of remittances. Expenditure patterns are
largely the same between the remittance-recipient and non-recipient groups, but notable
differences are still observed in education, health, financial services, real property and
construction, recreation, and transportation. These differences are more pronounced in the higher
income quintiles. The use of financial services is found to be higher among non-remittance
receiving households. While this is somewhat counterintuitive, given that many households
receive funds through financial intermediaries, it may suggest that financial inclusion and use of
financial services remains limited among remittance recipients.

13
Figure 3: Share of Broad Commodity Items to Total Expenditure, by Income Quintile and
Receipt of Remittances, 2018
Source: Authors’ calculations.
Descriptive data show that savings behavior does not show significant differences between
remittance- and non-remittance-receiving households. In 2018, the average share of savings in
household income is 17.3% (Figure 4). Remittance-receiving households have a slightly lower
savings ratio (17.1%) than non-remittance-receiving households (17.8%). As expected,
households with bank accounts have a higher savings rate (25.5% versus 17.2%), although their
numbers account for no more than 1% of total households. Comparing the two groups of
households, the savings rate of remittance recipients is slightly higher (26.3%) than the non-
remittance-receiving households (24.4%).
Figure 4: Savings Rate, by Bank Use and Receipt of Remittances, 2018
30
26.3
25.5
24.4
20
17.3 17.1 17.8 17.2 17.1 17.7
10
0
All Bank Nonbank
Source: Authors’ calculations.
tnecreP
All households
Remittance-receiving households
Non-remittance-receving households

14
Findings from Household Consumption Equations
We further investigate the expenditure pattern of remittance recipients and non-recipients by
estimating the consumption equation presented in section 3. Table 1 presents our empirical
results. Following the relevant literature, such as Zhu et al. (2014) and Wang, Hagedorn, and Chi
(2021), the coefficients, 𝛽 , of total household income can be interpreted as the marginal
(cid:3036)
propensity to consume, which varies by receipt of remittances as well as the extent of dependency
to such income source with the interaction term, 𝜌 . In terms of magnitude, bank savings or
(cid:3036)
investments are observed to have the largest increase in any expenditure item amid a similar
increase in total household income. For a 10% increase in total household income, the share that
average households allocate to bank savings and investments increases by 0.43 percentage
points. This is followed by durables (including vehicles), finance, and recreation. Allocation toward
real property and housing construction also rises by 0.12 percentage points with a 10% increase
in household income.

15
Table 1: Consumption Equation Regression Results, by Broad Expenditure Items
(1) (2) (3) (4) (5) (6) (7) (8)
Food Tobacco and Housing Utilities Durables Clothing Furnishing Health
Alcohol (including
Variables vehicles)
Total household income (log) -11.797*** -0.332*** 0.145*** -1.036*** 1.688*** 0.391*** 0.134*** 0.796***
(0.004) (0.001) (0.003) (0.002) (0.003) (0.001) (0.001) (0.002)
Remittance dependency group (Benchmark = Non-remittance
receiving households)
Group 1 = 0% < Remittance-to-
income ratio ≤ 25% -2.391*** 0.490*** -1.669*** 1.877*** 0.548*** -0.195*** -1.885*** -2.678***
(0.095) (0.029) (0.068) (0.034) (0.057) (0.018) (0.017) (0.044)
Group 2 = 25% < Remittance-
to-income ratio ≤ 50% 0.576*** -0.068 2.086*** 3.692*** -2.884*** 0.343*** -3.694*** -2.869***
(0.157) (0.048) (0.113) (0.056) (0.094) (0.030) (0.028) (0.074)
Group 3 = 50% < Remittance-
to-income ratio ≤ 75% -4.972*** -0.995*** -0.247 4.555*** 2.521*** 0.255*** -5.153*** -1.501***
(0.230) (0.070) (0.165) (0.082) (0.138) (0.044) (0.040) (0.108)
Group 4 = Remittance-to-
income ratio > 75% -1.693*** -4.987*** 15.913*** 10.198*** -4.485*** 4.785*** 0.522*** 2.101***
(0.300) (0.092) (0.216) (0.107) (0.180) (0.058) (0.053) (0.141)
Interaction term (Total household income x remittance dependency
group)
Group 1 = 0% < Remittance-to-
income ratio ≤ 25% 0.144*** -0.049*** 0.221*** -0.124*** -0.043*** 0.026*** 0.149*** 0.248***
(0.008) (0.002) (0.005) (0.003) (0.005) (0.001) (0.001) (0.004)
Group 2 = 25% < Remittance-
to-income ratio ≤ 50% -0.082*** -0.014*** -0.061*** -0.238*** 0.249*** -0.016*** 0.301*** 0.273***
(0.012) (0.004) (0.009) (0.004) (0.007) (0.002) (0.002) (0.006)
Group 3 = 50% < Remittance-
to-income ratio ≤ 75% 0.320*** 0.054*** 0.078*** -0.312*** -0.171*** -0.001 0.412*** 0.133***
(0.018) (0.006) (0.013) (0.006) (0.011) (0.003) (0.003) (0.008)
Group 4 = Remittance-to-
income ratio > 75% 0.076*** 0.353*** -1.335*** -0.744*** 0.408*** -0.359*** -0.050*** -0.204***
(0.023) (0.007) (0.017) (0.008) (0.014) (0.005) (0.004) (0.011)
Constant 178.386*** 6.802*** 10.509*** 17.560*** -17.570*** -1.959*** 0.808*** -9.075***
(0.053) (0.016) (0.038) (0.019) (0.032) (0.010) (0.009) (0.025)
Household characteristics YES YES YES YES YES YES YES YES
Household head characteristics YES YES YES YES YES YES YES YES

16
(1) (2) (3) (4) (5) (6) (7) (8)
Food Tobacco and Housing Utilities Durables Clothing Furnishing Health
Alcohol (including
Variables vehicles)
Region dummies YES YES YES YES YES YES YES YES
Weighted no. of observations 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315
R-squared 0.598 0.085 0.258 0.092 0.035 0.071 0.039 0.075
Table 1. continued.
(9) (10) (11) (12) (13) (14) (15) (16)
Transport Communication Education Recreation Finance Miscellaneous Real Property Bank
Expenses and Housing Savings/Investments
Construction
Variables
Total household income (log) 1.065*** 0.604*** 0.542*** 1.383*** 1.454*** -0.505*** 1.178*** 4.289***
(0.002) (0.001) (0.002) (0.003) (0.001) (0.001) (0.002) (0.003)
Remittance dependency group (Benchmark = Non-remittance
receiving households)
Group 1 = 0% < Remittance-to-
income ratio ≤ 25% 0.623*** -0.990*** -2.827*** 8.030*** 1.899*** 1.626*** -3.544*** 1.089***
(0.041) (0.014) (0.034) (0.073) (0.023) (0.024) (0.046) (0.070)
Group 2 = 25% < Remittance-
to-income ratio ≤ 50% 4.450*** -1.003*** -9.412*** 8.562*** 6.019*** 1.183*** -9.425*** 2.441***
(0.069) (0.023) (0.057) (0.122) (0.038) (0.040) (0.077) (0.117)
Group 3 = 50% < Remittance-
to-income ratio ≤ 75% 3.983*** 0.973*** -16.519*** 16.741*** 8.064*** 3.161*** -19.323*** 8.453***
(0.100) (0.033) (0.083) (0.178) (0.055) (0.059) (0.113) (0.171)
Group 4 = Remittance-to-
income ratio > 75% 7.255*** 7.711*** -19.772*** 24.813*** 10.551*** 5.062*** -39.047*** -18.929***
(0.131) (0.044) (0.109) (0.233) (0.072) (0.077) (0.148) (0.223)
Interaction term (Total household income x remittance dependency
group)
Group 1 = 0% < Remittance-to-
income ratio ≤ 25% -0.061*** 0.094*** 0.249*** -0.698*** -0.181*** -0.119*** 0.290*** -0.145***
(0.003) (0.001) (0.003) (0.006) (0.002) (0.002) (0.004) (0.006)
Group 2 = 25% < Remittance-
to-income ratio ≤ 50% -0.408*** 0.110*** 0.815*** -0.782*** -0.550*** -0.089*** 0.772*** -0.281***
(0.005) (0.002) (0.005) (0.010) (0.003) (0.003) (0.006) (0.009)
Group 3 = 50% < Remittance-
to-income ratio ≤ 75% -0.386*** -0.031*** 1.436*** -1.446*** -0.738*** -0.248*** 1.632*** -0.733***

17
(9) (10) (11) (12) (13) (14) (15) (16)
Transport Communication Education Recreation Finance Miscellaneous Real Property Bank
Expenses and Housing Savings/Investments
Construction
Variables
(0.008) (0.003) (0.007) (0.014) (0.004) (0.005) (0.009) (0.013)
Group 4 = Remittance-to-
income ratio > 75% -0.663*** -0.545*** 1.764*** -2.077*** -0.940*** -0.401*** 3.209*** 1.507***
(0.010) (0.003) (0.008) (0.018) (0.006) (0.006) (0.012) (0.017)
Constant -7.719*** -5.818*** -6.272*** -0.484*** -15.310*** 11.689*** -12.535*** -49.011***
(0.023) (0.008) (0.019) (0.041) (0.013) (0.014) (0.026) (0.039)
Household characteristics YES YES YES YES YES YES YES YES
Household head characteristics YES YES YES YES YES YES YES YES
Region dummies YES YES YES YES YES YES YES YES
Weighted no. of observations 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315 23,179,315
R-squared 0.076 0.270 0.112 0.150 0.206 0.048 0.044 0.148
Notes: Household level characteristics include household size, share of members aged less than 5 years, share of member aged between 5 and 17 years. Household head characteristics
are age, gender, marital status, educational attainment, and job status. Due to missing information in some explanatory variables, the effective weighted number of observations is lower
than the total number of households in 2018.
Standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.1
Source: Authors’ calculations.

18
This also applies to disbursements toward transport, health, communication, and education.
Meanwhile, the share to total expenditure on food shows the largest decline when households
can earn a higher income, i.e., their allocation on food drops by 1.2 percentage points on average
when they have a 10% increase in income. The shares for other expenditure items, such as
tobacco and alcohol, and for utilities decrease on average with higher household income. The
table also shows that expenditure allocation differs significantly between remittance-receiving
households and those that do not, as indicated by the statistically significant coefficient in 𝛾 .
(cid:3036)(cid:3041)
This finding is consistent with the observations from descriptive data.
The extent of remittance-receiving households’ dependency on remittance income, indicated by
the group dummies in the equation, is correlating to consumption choices. Non-remittance-
receiving households slash a relatively higher share of food expenditures when their income
increases than remittance-recipient households. On average, a 10% increase in household
income among non-remittance recipients is associated with a decrease in the share of food
consumption by 1.2 percentage points but such response is attenuated for remittance recipients.
It is interesting to note that remittances appear to have a significant influence on the allocation of
recipient households to long-term productivity-enhancing and investment-related spending and
activities. While the increase in the share of education-related expenses to total household
expenditures in response to a rise in household income is seen across all households, the
coefficient is larger for remittance-receiving households, even when the model controls for the
share of children in different age groups in the household.
Similarly, the average share of expenditure on real property investment is 0.12 percentage points
higher for every 10% increase in household income, with additional rates ranging from 0.03 to 0.3
percentage points among remittance recipients, highest among those with a high reliance on
remittances. Regarding health expenditures, remittance-receiving households except those with
the highest reliance on remittances, allocate more than non-recipient households when income
increases. One explanation for this could be that, unlike other investment items, health care costs
generally do not exceed a certain threshold or that this group of remittance recipients has better
health conditions given their better income situation. Further, the allocation toward disbursements
relating to bank savings and investment is higher for all remittance-receiving households than
non-recipient households except for the households most dependent on remittances. However, it
is worth noting that only the households with the highest dependence on remittance income have
a higher proxy marginal propensity to consume than the non-remittance-receiving households,
suggesting that remittance income encourages bank savings and investment. Meanwhile, the
coefficients on recreation and, to some extent, on food show a lower marginal propensity to
consume for remittance-receiving households compared to non-recipient households.
In summary, remittance-receiving households tend to have higher productive spending in
education and health and investment-related activities, especially in real estate and bank savings,
compared to their non-recipient counterparts. We also find no evidence that remittance income
exacerbates conspicuous consumption among recipient households. However, it is worth further
investigating the factors behind the limited use of financial services among remittance-receiving
households.

19
5. Micro-Macro Analysis on the Impact of Remittance-Driven Household Demand
(Consumption and Investment)
In 2018, remittance income reported by households in the FIES totaled ₱742.2 billion ($14.1
billion), equivalent to 4.1% of the GDP. This is slightly less than half (43.8%) of the official
aggregate international remittances into the country reported by the Bangko Sentral ng Pilipinas
(BSP), which amounted to ₱1.7 trillion or $32.2 billion, or approximately 9.3% of GDP. The BSP
compiles statistics on personal remittances according to the latest Balance of Payments
guidelines.14 It is worth noting that unlike many other central banks, the BSP estimates
remittances sent through informal channels using surveys, including the FIES (World Bank 2023),
and adds them to the official remittance statistics, which helps reduce the gap in micro and macro
remittance statistics.
Household final demand (consumption and savings/investment) by sector
Total household final demand, consisting of consumption and savings/investment financed by
remittance income, accounts for 5.6% of total household final demand reported in the I-O
transactions table in the same year. We note that household final consumption in the
manufacturing sector is the highest at almost ₱2.1 trillion ($38.9 billion), or 37.9% of the aggregate
consumption (Table 2). Philippine households’ final consumption for manufacturing consists
mainly of food, which accounts for 65.6% of total household demand from manufacturing,
beverages, petroleum, and chemical products. The manufacturing sector is followed by
accommodation and food services (11.9%) and agriculture, forestry, and fishing (11.8%). The
trade sector, which distributes final goods to households mainly through retail activities, also
claims a relatively high share (11.4%).
The pattern of final household demands of remittance-receiving and non-recipient households at
aggregate level across 16 input-output sectors is shown in Table 2. It mimics the consumption
pattern of the FIES-based grouping of expenditures in section 4. Non-remittance-receiving
households have more than 2 percentage points higher share of consumption in the
manufacturing and agriculture sectors. They also have a slightly higher share of consumption on
wholesale and retail trade, of about 1.3 percentage points. In comparison, remittance-receiving
households have higher consumption allocation for real estate and ownership of dwellings (about
2 percentage points). Other sectors with a higher share than non-recipient households include
utilities (1.2 percentage points), education (1.0 percentage points), and information and
communication (0.8 percentage points). Remittance recipients also have a slightly higher share
in the health sector than non-recipients.
Based on our calculations, the share of remittance income used for household consumption is
about 72.9%, while the rest is either saved or allocated to capital formation activities such as real
property and construction. Our analysis decomposing the imported content of intermediate and
final demand shows that about 84.3% of remittance income represents final demand for domestic
goods, while the rest (15.7%) are imports, which do not constitute domestic output except for the
14 The BSP records remittance transactions as part of the country’s Balance of Payments, so data on personal
remittances include (1) net compensation received (i.e., gross earnings less taxes, social security contributions, and
transportation and travel expenses) of overseas Filipino workers abroad who are temporary residents or also referred
to as “resident OFWs”; (2) personal transfers in cash or in kind of overseas Filipino workers, who have acquired long-
term residence in their host country or “nonresident OFWs”; and (3) capital transfers between resident and
nonresident households for capital-generating activities such as residential housing construction (Tuaño-Amador et
al. 2022).

20

retail sector. In the following section, we report only the contribution of remittances to domestic
outputs and value added.

Table 2: Allocation of Household Consumption by Remittance-Receiving and Non-
Remittance-Recipient Households by Sector in 2018 (%)
|                                     |          | Remittance-  |       | Non-Remittance- |       |
| ----------------------------------- | -------- | ------------ | ----- | --------------- | ----- |
| Sector                              | Overall  | Receiving    |       | Receiving       |       |
|                                     |          | Households   |       | Households      |       |
| Agriculture, forestry, and fishing  |          | 11.8         | 10.3  |                 | 12.4  |
| Mining and quarrying                |          | –            | –     |                 | –     |
| Manufacturing                       |          | 37.9         | 36.4  |                 | 38.6  |
Electricity, steam, water and waste management  4.9  5.8  4.6
| Construction  |     | 0.1  | 0.2  |     | 0.1  |
| ------------- | --- | ---- | ---- | --- | ---- |
Wholesale and retail trade; repair of motor
|     |     | 11.4  | 10.5  |     | 11.7  |
| --- | --- | ----- | ----- | --- | ----- |
vehicles and motorcycles
| Transportation and storage                 |     | 3.9   | 3.7   |     | 4.0   |
| ------------------------------------------ | --- | ----- | ----- | --- | ----- |
| Accommodation and food service activities  |     | 11.9  | 11.8  |     | 11.9  |
| Information and communication              |     | 1.8   | 2.3   |     | 1.6   |
| Financial and insurance activities         |     | 1.6   | 1.6   |     | 1.7   |
| Real estate and ownership of dwellings     |     | 10.6  | 12.0  |     | 10.0  |
| Professional and business services         |     | 0.2   | 0.2   |     | 0.2   |
Public administration and defense; Compulsory
|     |     | 0.0  | 0.0  |     | 0.0  |
| --- | --- | ---- | ---- | --- | ---- |
social security
| Education                                |     | 1.9  | 2.6  |     | 1.6  |
| ---------------------------------------- | --- | ---- | ---- | --- | ---- |
| Human health and social work activities  |     | 0.7  | 1.0  |     | 0.6  |
| Other services                           |     | 1.1  | 1.4  |     | 1.0  |
– = denotes no allocation, FIES = Family Income and Expenditure Survey.
Source: Authors’ calculations from FIES 2018 microdata.

Table 3 shows the distribution of baseline remittance-induced final household demand (both in
terms of amount and share) across sectors that contributed to the production of domestic goods
and services in the Philippines in 2018. It shows that remittances contribute significantly to
demand through final consumption. Consumption financed by remittances predominantly goes to
the manufacturing (₱162 billion), wholesale and retail trade (₱61.2 billion), and agriculture (₱59.2
billion) sectors. Meanwhile, the savings/investment portion of remittances flows mostly to the
construction sector at ₱118 billion, accounting for a large share of more than 70%. This is followed
by manufacturing (₱24.7 billion) and agriculture (₱15.9 billion).

21

Table 3. Share of Consumption and Savings/Investments in Remittance Income, 2018
|     |     | Consumption  |     |     | Savings/Investment  |     |     |
| --- | --- | ------------ | --- | --- | ------------------- | --- | --- |
Sector
|                                     | (₱ billion)  |        | (%)   |     | (₱ billion)  |     | (%)   |
| ----------------------------------- | ------------ | ------ | ----- | --- | ------------ | --- | ----- |
| Agriculture, forestry, and fishing  |              | 59.2   | 12.8  |     | 15.9         |     | 9.8   |
| Mining and quarrying                |              | –      |       | –   | 0.6          |     | 0.3   |
| Manufacturing                       |              | 162.0  | 35.0  |     | 24.7         |     | 15.2  |
Electricity, steam, water and waste management  26.6  5.7  0.1  0.0
| Construction  |     | 0.6  |     | 0.1  | 118.0  |     | 72.7  |
| ------------- | --- | ---- | --- | ---- | ------ | --- | ----- |
Wholesale and retail trade; repair of motor vehicles
| and motorcycles             |     | 61.2  | 13.2  |     | 0.1  |     | 0.1  |
| --------------------------- | --- | ----- | ----- | --- | ---- | --- | ---- |
| Transportation and storage  |     | 19.8  | 4.3   |     | 0.0  |     | 0.0  |
Accommodation and food service activities  39.4  8.5  0.0  0.0
| Information and communication       |     | 9.1  | 2.0  |     | 0.8  |     | 0.5  |
| ----------------------------------- | --- | ---- | ---- | --- | ---- | --- | ---- |
| Financial and insurance activities  |     | 8.4  | 1.8  |     | 0.1  |     | 0.1  |
Real estate and ownership of dwellings  56.1  12.1  0.3  0.2
| Professional and business services  |     | 0.9  | 0.2  |     | 1.2  |     | 0.7  |
| ----------------------------------- | --- | ---- | ---- | --- | ---- | --- | ---- |
Public administration and defense; Compulsory
| social security                          |     | 0.2    |      | 0.0  | 0.0     |     | 0.0  |
| ---------------------------------------- | --- | ------ | ---- | ---- | ------- | --- | ---- |
| Education                                |     | 10.0   |      | 2.2  | 0.2     |     | 0.1  |
| Human health and social work activities  |     | 4.0    | 0.9  |      | 0.1     |     | 0.1  |
| Other services                           |     | 5.9    |      | 1.3  | 0.2     |     | 0.1  |
| Overall                                  |     | 463.3  |      |      | 162.3   |     |      |
– = denotes no allocation, FIES = Family Income and Expenditure Survey.
Source: Authors’ calculations from FIES 2018 microdata.

Overall contribution of remittance income
Our micro-macro model shows that the share of remittance income used by households for
consumption and investment-related activities (in Table 3) translates to about 3.5% of the overall
economic output (amounting to ₱1.3 trillion or $24.4 billion) and 3.4% of domestic gross value
added (amounting to ₱626 billion or $11.9 billion) that goes through various sectors of the
Philippine economy in 2018.15 Such remittance-induced final demand also implies that about 1.5
million people are employed, equivalent to 3.7% of the country’s total employment.
Table 4 decomposes the overall economic contribution of remittance-driven household final
demand (both consumption and savings/investment) to the broad 16 I-O sectors. Given the huge
allocation in the manufacturing sector, the effect of remittance income is largest in the sector in
both gross output (₱455 billion or 35.5% of gross output contribution) and value added (₱143
billion or 23% of gross value added).16 This is not only due to the large inflow of remittances into
the sector but also due to the high sectoral interdependence and output multipliers. As shown in
Figure  5,  manufacturing  has  the  highest  intersectoral  linkage  for  both  forward  (2.97)  and

15 Note that this contribution only accounts for the purchase of domestic products, while excluding import contents,
which do not constitute domestic output except in retail sectors. The foreign content (imports) of household final
demand by remittance recipients amount to 0.7% of GDP.
16 The contribution of manufacturing to GDP is lower than the contribution to output due to the relatively large import
contents in the outputs.

22
backward (1.33) measures.17 Sectors with higher backward and forward linkage indices tend to
have larger output multipliers, as they generate significant demand for inputs from other sectors
while triggering increased production in the industries that supply their inputs. This is intuitive
because production requires inputs from relevant upstream sectors such as agriculture and
extractive activities, while the outputs produced are often used as intermediate input by other
industries. On closer examination, this is particularly true for the manufacture of electrical
equipment; rubber and plastic products; wood, bamboo, cane, rattan articles and related products;
paper and paper products; transport equipment; and machinery and equipment other than
electrical.
After manufacturing, agriculture (₱178 billion) and wholesale and retail trade (₱150 billion) also
generate a large share of remittance-led outputs. Retail trading activities, with a relatively large
share of expenditure among recipient households, have a high forward linkage index. The savings
and investment portion of their remittance income also boosts economic output, largely due to
their expenditure on real property and construction activities. In terms of employment impact,
remittance-induced final demand benefits the 644,000 people employed in the agriculture sector
(43% of total employment). The impact of employment is also high in the wholesale and retail
trade sector (209,000) and in construction (154,000).
17 The forward linkage index, also known as the index of sensitivity of dispersion, captures the extent to which the
sector’s output is used by other sectors as input. In other words, it measures the increase in an industry’s production
that is driven by an increase in final demand across all sectors of the economy. The backward linkage index, or index
of power of dispersion, determines the extent to which a sector’s production depends on inputs from other sectors.
Therefore, an increase in the production of sectors that have relatively high backward linkages generates greater
demand for the output of other sectors. The output multiplier refers to the total amount of economy-wide production
induced by final demand in different economic sectors (Miller and Blair 2009).

23

Table 4: Economic Contribution of Remittance Income by Sector, 2018
|     |     | Gross Output  |     | Gross Value Added  |     |     | Employment  |     |
| --- | --- | ------------- | --- | ------------------ | --- | --- | ----------- | --- |
Sector
|                             | (₱ billion)  |      | (%)  | (₱ billion)  |     | (%)  | (‘000s)  | (%)  |
| --------------------------- | ------------ | ---- | ---- | ------------ | --- | ---- | -------- | ---- |
| Agriculture, forestry, and  |              | 178  | 14   |              | 89  | 14   | 644      | 43   |
fishing
| Mining and quarrying           |     | 33   | 3   |     | 25   | 4   | 12   | 1   |
| ------------------------------ | --- | ---- | --- | --- | ---- | --- | ---- | --- |
| Manufacturing                  |     | 455  | 35  |     | 143  | 23  | 135  | 9   |
| Electricity, steam, water and  |     | 50   | 4   |     | 31   | 5   | 7    | 0   |
waste management
| Construction                 |     | 120  | 9   |     | 55   | 9   | 154  | 10  |
| ---------------------------- | --- | ---- | --- | --- | ---- | --- | ---- | --- |
| Wholesale and retail trade;  |     | 150  | 12  |     | 106  | 17  | 209  | 14  |
repair of motor vehicles and
motorcycles
| Transportation and storage  |     | 44  | 3   |     | 20  | 3   | 117  | 8   |
| --------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- |
| Accommodation and food      |     | 46  | 4   |     | 16  | 3   | 81   | 5   |
service activities
| Information and  |     | 20  | 2   |     | 10  | 2   | 8   | 1   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
communication
| Financial and insurance  |     | 48  | 4   |     | 26  | 4   | 9   | 1   |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
activities
| Real estate and ownership of  |     | 81  | 6   |     | 67  | 11  | 7   | 0   |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dwellings
| Professional and business  |     | 29  | 2   |     | 17  | 3   | 27  | 2   |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
services
| Public administration and  |     | 1   | 0   |     | 0   | 0   | 1   | 0   |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
defense; Compulsory social
security
| Education                     |     | 15  | 1   |     | 13  | 2   | 20  | 1   |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Human health and social work  |     | 5   | 0   |     | 3   | 0   | 5   | 0   |
activities
| Other services  |     | 8      | 1    |     | 5    | 1    | 70     | 5    |
| --------------- | --- | ------ | ---- | --- | ---- | ---- | ------ | ---- |
|                 |     | 1,283  | 100  |     | 626  | 100  | 1,506  | 100  |
Total
Source: Authors’ calculations.

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

24
Figure 5: Sectoral Interdependency and Output Multipliers, 2018
Source: Authors’ calculations.
Extension: Simulating a 10% increase in remittance income using the micro-macro model
Extending our micro-macro analysis of remittances, we examine the macroeconomic impact of a
hypothetical and exogenous 10% across-the-board increase in remittance income of remittance-
receiving households in the Philippines, equivalent to ₱74.2 billion ($14.1 billion). The model
integrates a micro-simulated reallocation of household expenditures resulting from higher income
based on the consumption equation (Equation 1). This will complement our understanding of the
contribution of remittance-led household expenditures, savings, and investments by providing
more insights into sector-specific contributions to economic output and value added. This
assumes that non-recipient households are not affected by this exogenous change via potential
spillover effects.
Figure 6 illustrates the results of the microsimulation results of a 10% increase in remittances
received. It shows that such additional income reduces the average share of food in total
expenditure by 0.09 percentage points among remittance-receiving households. This decline is
offset by an increase in the share spent on bank savings and investments (0.03 percentage
points) and spending on real property and housing construction (0.03 percentage points),
education (0.02 percentage points), durable goods (0.02 percentage points), and health (0.01
percentage points). In comparison, the estimated reduction in the share of food is much higher
than the 0.0001 percentage points estimated in Wang, Hagedorn, and Chi (2021) in the context
of remittance-receiving households in the Kyrgyz Republic as well as the associated increase in
the share of spending on medical and related expenses (i.e., 0.0001 percentage points). The
remittance receiving families in the Kyrgyz Republic are mostly in the poor income groups that
are highly dependent on remittances (Gao, Kikkawa, and Kang 2021). This could explain the
inelasticity of food items in the shock scenario.

25
Figure 6: Simulated Reallocation Impact in the Share of Broad Expenditure Items to Total
Household Spending
Note: Data labels refer to the percent change in the share of expenditure on each commodity item to total
expenditure.
Source: Authors’ calculations.
The reallocation effect varies by household income level. The decline in the share of food to total
expenditures is greatest for the higher income quintiles (Figure Annex 1). Accordingly, the
spending allocation to productive and investment activities is also higher among the wealthier
households. Aside from food consumption, the share of spending on housing and utilities, as well
as recreational items such as restaurants and accommodations, has also fallen in the top income
quintiles. We also note the same pattern of spending reallocation when we look at households
with different levels of dependence on remittance income, and that the share of food expenditure
declines when remittance-receiving households have higher dependence on remittance income
(Figure Annex 2). In addition, the increase in remittances would also boost the share of spending
on investment and productivity-inducing items such as bank savings and investments, real
property and housing, and education.
Incorporating the above insights into the I-O analysis, Table 5 presents the simulated
macroeconomic impact of a 10% increase in remittance income received by households. Overall
gross output is estimated to be 0.35 percentage points higher (₱128.4 billion or $2.4 billion) than
the baseline level (₱36.5 trillion or $693.9 billion) if households spend, save, or invest this
additional receipt in various sectors of the economy. Downstream sectors such as mining and
quarrying, as well as electricity, steam, water and waste management, and agriculture, benefit
from the higher remittance flows and the corresponding increase in final demand from recipient
families. They benefit from the high output multiplier of the manufacturing sector, which despite
some reduction in allocations, continues to account for a large chunk of total spending by
remittance-receiving households.

26
Table 5: Estimated Impact of a 10% Increase in Remittance Income by Sector, 2018
Gross Output Gross Value Added Employment
Sector % Change % Change % Change
(₱ billion) to Baseline (₱ billion) to Baseline (‘000s) to Baseline
Agriculture, forestry, and fishing 17.8 0.52 8.9 0.51 64.5 0.64
Mining and quarrying 3.3 1.35 2.5 1.55 1.2 0.57
Manufacturing 45.5 0.42 14.3 0.41 13.5 0.37
Electricity, steam, water and waste 5.0 0.56 3.1 0.56 0.7 0.50
management
Construction 11.8 0.39 5.4 0.39 15.2 0.39
Wholesale and retail trade; repair of 15.0 0.32 10.6 0.33 21.0 0.26
motor vehicles and motorcycles
Transportation and storage 4.4 0.26 2.0 0.28 11.7 0.36
Accommodation and food service 4.6 0.43 1.6 0.39 8.1 0.47
activities
Information and communication 2.0 0.19 1.0 0.19 0.8 0.19
Financial and insurance activities 4.8 0.18 2.6 0.17 0.9 0.16
Real estate and ownership of 8.1 0.53 6.7 0.57 0.7 0.36
dwellings
Professional and business services 2.9 0.15 1.7 0.15 2.7 0.15
Public administration and defense; 0.1 0.01 0.0 0.01 0.1 0.01
Compulsory social security
Education 1.5 0.17 1.3 0.17 2.0 0.17
Human health and social work 0.5 0.11 0.3 0.11 0.6 0.11
activities
Other services 0.8 0.14 0.5 0.13 7.1 0.23
Overall 128.4 0.35 62.6 0.34 150.7 0.37
Source: Authors’ calculations.
The results also suggest that the additional remittance income, with its influence to be allocated
more toward real estate activities, will induce higher output for the real estate and ownership of
dwellings and construction activities. Given the high baseline expenditure share of
accommodation and food services, the macroeconomic impact of additional remittances in this
sector remains high. Further, with reallocation toward education and health, the economic output
induced by higher receipt of remittances also benefits the health care and education sectors. The
same pattern also applies to the impact on value added per sector, which is 0.34 percentage
points higher than the baseline, equivalent to $1.19 billion in 2018. Our results are generally
consistent with those of Goce-Dakila and Dakila, Jr. (2009) based on a general equilibrium
approach. They found that a 5% reduction in remittances received by households is accompanied
by a decrease in the overall gross output of less than half a percentage point, with the largest
impact observed in the services sector. Apart from the fact that their analysis uses macro statistics
for remittances, which can be at least double the actual remittance income of households, their
results are comparable.

27
6. Conclusion and Policy Implications
This study evaluated the contribution of international remittances to overall economic output of
the migrants’ country of origin using a consistent definition of remittances which is drawn from the
reported international remittance income of the recipient households. Using the input-output
framework, we illustrated how household income from remittances flows into each industry and
ultimately into the overall economy. We find that remittance income reported by Philippine
households amounted to ₱1.7 trillion in 2018, equivalent to 44% of the aggregate international
remittance inflows officially reported by the central bank in the same year. Remittance-financed
household consumption and investment contributed to 3.5% of the country’s total gross output
($24.4 billion), 3.4% ($11.9 billion) of gross domestic product (GDP), and 3.7% (1.5 million
individuals) of total employment in 2018. In our simulation, a general increase in international
remittance income of 10% (equivalent to $1.4 billion) leads to an increase in the country’s GDP
of 0.34 percentage points over the baseline, i.e., about $1.2 billion in 2018. The sectors that
benefit the most from the additional remittance-led consumption and savings/investment include
manufacturing, construction, and agriculture. Demand from remittance recipients for these
sectors can provide an additional boost to domestic output and value added, as these sectors
have high multiplier effect. Sectors such as mining and quarrying and electricity, steam, water
and waste management, which have relatively low direct allocation on upstream sectors,
experienced large increases in gross output and gross value added (relative to their baseline
levels) because of their strong linkages with manufacturing. The exogenous increase in
remittances induces households to reallocate more to investment-related spending, which boosts
demand and output in the real estate and construction sectors.
Our analysis and findings can guide policymakers in migrants’ countries of origin in many ways.
First, the study confirms the existence of large differences in the size of international remittances
reported by households and the central bank, which is an important factor to consider for
remittance data analysis at the micro, macro, or both levels. The findings also indicate that an
attempt to promote the productive use of remittances should not only include remittance-recipient
households as the target audiences, but also reach out to migrants/immigrants and diaspora
investors, who likely remit a sizable share of international remittances.
Second, the proposed input-output analysis can be used as a tool to examine how income from
remittances flows from households to different sectors and to the overall economy, whether they
are channeled into productive sectors with high sectoral dependence, and what impact it has on
job creation. In other words, it is possible to assess whether remittances are creating virtuous
cascading effects on the output of the whole economy. The benefit of this analysis becomes
clearer when applied to multiple countries, allowing for comparison. An additional benefit of the
proposed micro-macro analysis, which examines the share of import contents that remittance
income purchases, is also an alternative assessment of its direct contribution to the economy of
the migrants’ home country. In addition, our analytical tool can help governments anticipate the
household- and industry-specific effects of possible fluctuations in remittance flows with relatively
little data requirement.
Future research is needed to close the gap between micro and macro remittance studies and
overcome definitional differences. One is to study the flow of remittance-sourced expenditures
related to family businesses or family business investments that can be financed from
remittances. Many household surveys are silent on the source of such investment funds, reporting
only the net profits earned from the family business as income. It is also important to conduct

28
more research on how migrants, immigrants, and the diaspora themselves consume and invest
remittances in countries of origin (apart from remitting funds to families) so that we can fill the gap
in the data and literature. In addition, because of its simple data requirements, our approach can
be applied to other migrant countries of origin for comparison to broaden our understanding of
the impact and mechanisms through which remittances influence the economies of these
countries.

29
REFERENCES
Acosta, P. A., P. Fajnzylber, and H. López. 2007. The Impact of Remittances on Poverty and
Human Capital: Evidence from Latin American Household Surveys. World Bank Policy
Research Working Paper. No. 4247. Washington, DC: World Bank.
Acosta, E. K., K. Lartey, and F. S. Mandelman. 2009. Remittances and the Dutch Disease.
Journal of International Economics. 79 (1). pp. 102–116.
https://doi.org/10.1016/j.jinteco.2009.06.007.
Adams, R. H. and A. Cuecuecha. 2010. Remittances, Household Expenditure and Investment in
Guatemala. World Development. 38 (11). pp. 1626–1641.
_____. 2013. The Impact of Remittances on Investment and Poverty in Ghana. World
Development. 50. pp. 24-40. https://doi.org/10.1016/j.worlddev.2013.04.009.
Adams, R. H. and J. Page. 2005. Do International Migration and Remittances Reduce Poverty
in Developing Countries? World Development. 33 (10). pp. 1645–1669.
https://doi.org/10.1016/j.worlddev.2005.05.004.
Ahmed, V., G. Sugiyarto, and S. Jha. 2010. Remittances and Household Welfare: A Case Study
of Pakistan. ADB Economics Working Paper Series. No. 194. Manila: Asian
Development Bank (ADB). https://www.adb.org/publications/remittances-and-household-
welfare-case-study-pakistan.
Amare, M. and L. Hohfeld. 2016. Poverty Transition in Rural Vietnam: The Role of Migration and
Remittances. The Journal of Development Studies. 52 (10). pp. 1463–1478.
https://www.tandfonline.com/doi/abs/10.1080/00220388.2016.1139696.
Amuedo-Dorantes, C. and S. Pozo. 2014. On the Intended and Unintended Consequences of
Enhanced U.S. Border and Interior Immigration Enforcement: Evidence from Mexican
Deportees. Demography. 51 (6). pp. 2255–79. https://www.jstor.org/stable/43697504.
Ang, A., G. Sugiyarto, and S. Jha. 2009. Remittances and Household Behavior in the
Philippines. ADB Economics Working Paper. No. 188.
https://www.adb.org/publications/remittances-and-household-behavior-philippines.
Ashraf, N., D. Aycinena, C. Martínez, and D. Yang. 2015. Savings in Transnational Households:
A Field Experiment Among Migrants from El Salvardor. The Review of Economics and
Statistics. 97 (2). pp. 332–51.
Awan, R. U., F. Waqar, S. Rahim, and F. Sher. 2017. Impact of Remittances on Expenditures
and Poverty at Household Level in Pakistan. Pakistan Economic and Social Review. 55
(2). pp. 415–434. https://www.jstor.org/stable/26616720.
Castaldo, A. and B. Reilly. 2007. Do Migrant Remittances Affect the Consumption Patterns of
Albanian Households? South-Eastern Europe Journal of Economics. 5 (1). pp. 25–44.
Clemens, M. A. and D. McKenzie. 2018. Why Don't Remittances Appear to Affect Growth? The
Economic Journal. 128 (612). pp. F179–F209. https://doi.org/10.1111/ecoj.12463.

30
Cooray, A. 2012. The Impact of Migrant Remittances on Economic Growth: Evidence from
South Asia. Review of International Economics. 20 (5). pp. 985–998.
https://onlinelibrary.wiley.com/doi/10.1111/roie.12008.
Cox Edwards, A. and M. Ureta. 2003. International Migration, Remittances, and Schooling:
Evidence from El Salvador. Journal of Development Economics. 72 (2). pp. 429–461.
https://doi.org/10.1016/S0304-3878(03)00115-9.
de Haas, H. 2010. Migration and Development: A Theoretical Perspective. International
Migration Review. 44 (1). pp. 227–264. https://doi.org/10.1111/j.1747-
7379.2009.00804.x.
Dridi, J., T. Gursoy, H. Perez-Saiz, and M. Bar. 2019. The Impact of Remittances on Economic
Activity: The Importance of Sectoral Linkages. IMF Working Paper. No. 175.
Washington, DC: International Monetary Fund.
https://www.imf.org/en/Publications/WP/Issues/2019/08/16/The-Impact-of-Remittances-
on-Economic-Activity-The-Importance-of-Sectoral-Linkages-47091.
European Commission, International Monetary Fund, Organisation for Economic Co-operation
and Development, United Nations, and World Bank. 2009. System of National Accounts
2008. https://www.elibrary.imf.org/display/book/9789211615227/9789211615227.xml.
Freund, C. and N. Spatafora. 2008. Remittances, transaction costs, and informality. Journal of
Development Economics. 86 (2). pp. 356-366.
https://www.sciencedirect.com/science/article/abs/pii/S0304387807000818.
Friedman, M. 1957. The Permanent Income Hypothesis. In A Theory of the Consumption
Function. pp. 20–37. National Bureau of Economic Research, Inc.
Gao, X., A. Kikkawa, and J. W. Kang. 2021. Evaluating the Impact of Remittances on Human
Capital Investment in the Kyrgyz Republic. ADB Economics Working Paper Series. No.
637. Manila: ADB.
Gibson, J., D. McKenzie, H. Rohorua, and S. Stillman. 2019. The Long-Term Impact of
International Migration on Economic Decision-Making: Evidence from a Migration Lottery
and Lab-in-the-Field Experiments. Journal of Development Economics. 138. pp. 99–115.
https://doi.org/10.1016/j.jdeveco.2018.12.007.
Giuliano, P. and M. Ruiz-Arranz. 2009. Remittances, Financial Development, and Growth.
Journal of Development Economics. 90 (1). pp. 144–152.
https://www.sciencedirect.com/science/article/pii/S0304387808001077.
Glytsos, N. P. 1993. Measuring the Income Effects of Migrant Remittances: A Methodological
Approach Applied to Greece. Economic Development and Cultural Change. 42 (1). pp.
131–168.
Goce-Dakila, C. and F. G. Dakila, Jr. 2009. Spatial Impact of Overseas Filipino Workers’
Remittances on the Philippine Economy. The Philippine Review of Economics. 46 (2).
pp. 221–241.

31
Kikkawa, A., G. Sugiyarto, J. Villafuerte, K. Kim, B. Narayanan, and R. Gaspar. 2021. Labor
Mobility and Remittances in Asia and the Pacific during and after the COVID-19
Pandemic. ADB Brief. No. 204. Manila: ADB.
https://www.adb.org/sites/default/files/publication/761401/adb-brief-204-labor-mobility-
remittances-asia-pacific-covid-19.pdf.
McKenzie, D. and H. Rapoport. 2011. Can Migration Reduce Educational Attainment? Evidence
from Mexico. Journal of Population Economics. 24 (4). pp. 1331–58.
http://www.jstor.org/stable/41488354.
Meyer, D. and A. Shera. 2017. The Impact of Remittances on Economic Growth: An
Econometric Model. EconomiA. 18 (2). pp. 147–155.
https://doi.org/10.1016/j.econ.2016.06.001.
Mezger, C. and C. Beauchemin. 2010. The Role of International Migration Experience for
Investment at Home: The Case of Senegal. Paris: MAFE.
Miller, R. E. and P. D. Blair. 2009. Input-Output Analysis: Foundations and Extensions. 2nd
Edition. Cambridge: Cambridge University Press.
Mishra, K., O. Kondratjeva, and G. E. Shively. 2022. Do Remittances Reshape Household
Expenditures? Evidence from Nepal. World Development. 157. 105926.
https://doi.org/10.1016/j.worlddev.2022.105926.
Moon, H. R. and B. Perron. 2005. Efficient Estimation of the Seemingly Unrelated Regression
Cointegration Model and Testing for Purchasing Power Parity. Econometric Reviews. 23
(4). pp. 293–323. https://doi.org/10.1081/ETC-200040777.
Murakami, E., E. Yamada, and E. P. Sioson. 2021. The Impact of Migration and Remittances on
Labor Supply in Tajikistan. Journal of Asian Economics. 73.
https://doi.org/10.1016/j.asieco.2020.101268.
Philippine Statistics Authority (PSA). 2020. 2018 Family Income and Expenditure Survey.
https://library.psa.gov.ph/cgi-bin/koha/opac-detail.pl?biblionumber=15584.
Pratt, S. 2015. The Economic Impact of Tourism in SIDS. Annals of Tourism Research. 52. pp.
148–160.
Ratha, D. 2005. Workers’ Remittances: An Important and Stable Source of External
Development Finance. In Remittances: Development Impact and Future Prospects
(edited by S.M. Maimbo and D. Ratha). pp. 19-51.
https://www.knomad.org/sites/default/files/2017-09/32598a.pdf.
Schepelmann, P., A. Vercalsteren, J. Acosta-Fernandez, M. Saurat, K. Boonen, M. Christis, G.
Marin, R. Zoboli, and C. Maguire. 2020. Driving Forces of Changing Environmental
Pressures from Consumption in the European Food System. Sustainability. 12 (19). p.
8265. https://doi.org/10.3390/su12198265.
Seriño, M. N. V. and S. Klasen. 2015. Estimation and Determinants of the Philippines'
Household Carbon Footprint. The Developing Economies. 53 (1). pp. 44–62.
https://doi.org/10.1111/deve.12065.

32
Shonkwiler, J. S. and S. T. Yen. 1999. Two-Step Estimation of a Censored System of
Equations. American Journal of Agricultural Economics. 81 (4). pp. 972–982.
https://doi.org/10.2307/1244339.
Tuaño-Amador, M. A. C. N., V. B. Bayangos, M. E. G. Romarate, and C. F. C. Maliwat. 2022.
Remittances from Overseas Filipinos in the Time of COVID-19: Spillovers and Policy
Imperatives. Bangko Sentral ng Pilipinas Discussion Paper Series. No. 010.
https://www.bsp.gov.ph/Pages/MediaAndResearch/PublicationsAndReports/Discussion
%20Papers/DP202201.pdf.
United Nations Department of Economic and Social Affairs, Population Division. 2021.
International Migrant Stock 2020.
https://www.un.org/development/desa/pd/content/international-migrant-stock.
Wang, D., A. Hagedorn, and G. Chi. 2021. Remittances and Household Spending Strategies:
Evidence from the Life in Kyrgyzstan Study, 2011–2013. Journal of Ethnic and Migration
Studies. 47 (13). pp. 3015–3036.
https://www.tandfonline.com/doi/full/10.1080/1369183X.2019.1683442.
Woodruff, C. and R. Zenteno. 2007. Migration Networks and Microenterprises in Mexico.
Journal of Development Economics. 82 (2). pp. 509–528.
https://doi.org/10.1016/j.jdeveco.2006.03.006.
World Bank. 2023. World Development Report 2023: Migrants, Refugees, and Societies.
Washington, DC. doi:10.1596/978-1-4648-1941-4.
Yang, D. 2008. International Migration, Remittances and Household Investment: Evidence from
Philippine Migrants’ Exchange Rate Shocks. The Economic Journal. 118 (528). pp. 591–
630. https://doi.org/10.1111/j.1468-0297.2008.02134.x.
Yang, D. and C. A. Martinez. 2006. Remittances and Poverty in Migrants’ Home Areas:
Evidence from the Philippines. In C. Ozden and M. Schiff, eds. International Migration,
Remittances, and the Brain Drain. Washington, DC: Palgrave Macmillan.
Yang, D. and H. J. Choi. 2007. Are Remittances Insurance? Evidence from Rainfall Shocks in
the Philippines. The World Bank Economic Review. 21 (2). pp. 219–248.
https://doi.org/10.1093/wber/lhm003.
Yoshino, N., F. Taghizadeh-Hesary, and M. Otsuka. 2017. International Remittances and
Poverty Reduction: Evidence from Asian Developing Countries. ADBI Working Paper
Series. No. 759. Tokyo: Asian Development Bank Institute.
https://www.adb.org/publications/international-remittances-and-poverty-reduction.
Zhu Y, Z. Wu, L. Peng, and L. Sheng. 2014. Where Did All the Remittances Go? Understanding
the Impact of Remittances on Consumption Patterns in Rural China. Applied Economics,
46(12):1312–1322.
https://www.tandfonline.com/doi/abs/10.1080/00036846.2013.872764.

33
APPENDIX
Figure A1: Simulated Reallocation Impact in the Share of Broad Expenditure Items to Total Household Spending, by Income
Quintile
Source: Authors’ calculations.
Figure A2: Simulated Reallocation Impact in the Share of Broad Expenditure Items to Total Household Spending, by
Remittance Dependency
Source: Authors’ calculations.

Measuring the Contribution of International Remittances
to Household Expenditures and Economic Output
A Micro–Macro Analysis for the Philippines
This study assesses the simultaneous contribution of international remittance income reported by recipient
households to the overall economy of the Philippines by integrating micro data and macro simulation based
on an input–output framework. It finds that remittance-driven household expenditures and investments
contributed 3.5% of the country’s total output, 3.4% of the gross domestic product, and 3.7% of the total
employment in 2018. Industries that received the bulk of remittances in the form of final consumption are
manufacturing, agriculture, and wholesale and retail trade.
MEASURING THE CONTRIBUTION
OF INTERNATIONAL REMITTANCES
About the Asian Development Bank
TO HOUSEHOLD EXPENDITURES
ADB is committed to achieving a prosperous, inclusive, resilient, and sustainable Asia and the Pacific,
while sustaining its efforts to eradicate extreme poverty. Established in 1966, it is owned by 68 members
—49 from the region. Its main instruments for helping its developing member countries are policy dialogue, AND ECONOMIC OUTPUT
loans, equity investments, guarantees, grants, and technical assistance.
A MICRO–MACRO ANALYSIS FOR THE PHILIPPINES
Aiko Kikkawa, Raymond Gaspar, Kijin Kim, Mahinthan J. Mariasingham,
and Christian Marvin Zamora
ADB ECONOMICS
NO. 714
WORKING PAPER SERIES
February 2024
ASIAN DEVELOPMENT BANK
6 ADB Avenue, Mandaluyong City
1550 Metro Manila, Philippines ASIAN DEVELOPMENT BANK
www.adb.org