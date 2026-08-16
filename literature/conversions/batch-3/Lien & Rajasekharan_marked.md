---
conversion_metadata:
  converted_at: "2026-07-21T14:01:41Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Lien & Rajasekharan.pdf"
  source_pdf_sha256: "5772bdf239e6bbe05b035a76e3da42b10c46df32f852a44141603a9dbfc71582"
  page_count: 13
  markdown_char_count: 156994
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Energy & Buildings 325 (2024) 114954

Contents lists available at ScienceDirect

Energy & Buildings

journal homepage: www.elsevier.com/locate/enb

Automatic standard building category classification from smart meter data 
– A supervised learning approach

Synne Krekling Lien a,b,*, Jayaprakash Rajasekharan a
a Norwegian University of Science and Technology (NTNU), Department for Electric Energy, NO-7491 Trondheim, Norway
b SINTEF Community Oslo, Pb 124 Blindern, 0314 Oslo, Norway

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Buildings
Energy
Electricity
Measurements
Classification
Machine learning
Building category

Increased availability of smart meter data offers better insight into buildings’  electricity usage. By classifying 
smart meter data by building type and presence of heating appliances, we can efficiently gain metadata about the 
buildings that is useful for research, grid planning, and energy efficiency policy employment. However, current 
smart  meter  classification  approaches  are  largely  based  on  limited  datasets  and  building  classes,  or  on  unsu-
pervised methods that don’t align with standard building categories and offer limited control over grouping. This 
article presents a supervised automatic building category classification approach for labelling smart meter data 
from buildings into standard building categories in the Norwegian building regulations (TEK17), and whether 
they have electric heating or not. 82 novel physics-based domain features are presented which can be extracted 
from any hourly electricity smart meter data series from buildings with a duration of months-years. The features 
are  specifically  designed  to  identify  the  building  and  heating  type  of  a  smart  meter  data  series  by  capturing 
patterns such as seasonality, daily usage trends, similarities with standardized building load profiles, temperature 
dependency,  and  other  domain-specific  characteristics.  The  classification  approach  is  trained  and  tested  on  a 
large dataset of 2724 buildings from 12 different building categories, both residential and non-residential, and 
correctly identifies the heating type and building category of unseen Norwegian smart meter data from buildings 
in 84 % of the test cases. The approach is generalizable to meter data from other Norwegian buildings and is also 
tested on buildings from other climate zones. The proposed method for smart meter data classification is proven 
to have high accuracy and applicability for extracting metadata for both residential and non-residential buildings 
in Norway.

1. Introduction

In 2021, the operation of buildings was responsible for 30 % of final 
global energy consumption and 27 % of total energy sector emissions 
(out of which 8 % is related to direct emissions from buildings, while 19 
% refers to emissions from generation of heat and electricity consumed 
by buildings) [1]. The electrification of buildings has been identified as a 
key alternative to achieve a more sustainable energy system and miti-
gate the corresponding emission of gases that result in climate change 
[2]. To tackle these challenges, more knowledge about building energy 
use is needed. Due to recent roll-out of smart grid infrastructures and 
advanced  digital  metering  systems,  building  energy  data  has  become 
more available. Norway mandated the installation of smart electricity 
meters for all electricity consumers as part of advanced metering sys-
tems  (AMS)  by  2020  [3].  These  meters  record  customers’  hourly

electricity usage and transmit data to grid companies, and can, if ana-
lysed,  provide  more  information  about  electricity  use  patterns  for 
different electricity consumers. The use of electrical heating appliances 
is widespread in Norway due to historically low electricity prices [4]. It 
is estimated that electricity for heating makes up more than 60 % of the 
total  electricity  consumption  in  Norwegian  buildings  [5].  The  use  of 
electricity for heating hence contributes to high peaks in the electricity 
grid during the colder winter days [6]. Buildings with electrical heating 
hence typically have a stronger strain on the electricity grid compared to 
buildings  with  non-electric  heating.  To  address  the  challenges  of 
increased electricity demand in the grid, and to utilize the availability of 
more electricity data from buildings, the implementation of classifica-
tion methods for electricity measurements becomes valuable. By clas-
sifying  smart  meter  data  by  building  type,  we  can  efficiently  gain 
metadata about the buildings that is useful for research, grid planning,

* Corresponding author.

E-mail address: synne.k.lien@ntnu.no (S.K. Lien).

https://doi.org/10.1016/j.enbuild.2024.114954
Received 15 August 2024; Received in revised form 9 October 2024; Accepted 22 October 2024  
Available online 26 October 2024 
0378-7788/© 2024 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

---

<!-- PAGE 2 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

and  energy  efficiency.  Unsupervised  methods  have  been  applied  in 
various ways to classify smart meter data, as demonstrated in [7] and 
[8], where clustering techniques were used to group households based 
on their demand response potential, and in [9] and [10] which looked at 
grouping of buildings into distinct consumer classes to design tailored 
tariffs aimed at reducing grid strain. Other examples include [11] which 
investigated  K-means  clustering  applied  to  clustering  of  14  non- 
residential  buildings  on  a  university  campus  (of  types  office/library/ 
teaching) and clustered into two different consumer groups. The effec-
tiveness of unsupervised methods/clustering relies on multiple factors 
and can be measured by diverse indicators to assess how well the clus-
ters  represents  the  data,  including  the  silhouette  score  [12],  Davis 
Bouldin index and the Dunn index [13]. While these indicators can tell 
us how well the buildings within each group fit together, unsupervised 
clustering techniques may group together buildings have several simi-
larities but serve different purposes. Another challenge with unsuper-
vised methods  is  that the  number of optimal clusters is generally not 
known. There are numerous methods for estimating the optimal number 
of clusters but depending on the problem, unsupervised methods may 
not be the most suitable for assigning a class to a building load profile. 
The classification of buildings’  smart meter data has historically been 
considered an unsupervised machine learning task [14,15] due to both 
the  lack  of  properly  labelled  smart  meter  data  and  the  challenge  of 
determining  the  correct  or  optimal  number  of  clusters.  However,  un-
supervised methods are not necessarily the best approach when aiming 
to classify buildings into set, pre-defined building categories. In Norway 
standardized  building  category  groups  are  used  in  the  Norwegian 
building code TEK–17 [16], and in the standard for energy calculations 
of buildings in Norway [17] and divide buildings/part of buildings into 
13  main  categories  (“small  house”,  “apartment”,  “school”,  “office”, 
“nursing home”, etc.). Each category has specific energy efficiency re-
quirements, making it essential to understand the composition of these 
categories within an area for effective grid and energy planning. Clas-
sifying buildings’  smart meter data into these standardized categories 
can provide a more accurate and practical categorization of buildings. 
For instance, while schools and kindergartens may exhibit similar en-
ergy consumption patterns, a notable distinction arises in the heating 
systems employed in these building categories. Kindergartens often have 
point  source  heating,  while  schools  often  utilize  water-borne  heating 
systems, providing them with greater flexibility to alter heating sources 
and  control  strategies.  Likewise,  a  nursing  home  might  have  similar 
energy consumption profiles as an apartment building, yet an important 
difference  between  these  types  of  buildings  are  the  ownership  struc-
tures. Publicly owned buildings may be in a different economical posi-
tion  compared  to  privately  owned  residential  properties,  and 
policymakers  wield  more  influence  in  enforcing  legislation  and  re-
furbishments in the former. Cabins equipped with electrical heating may 
have similar technical systems compared with single family houses, but 
their geographical location introduces unique considerations. Situated 
in areas with limited grid capacity and sparse occupancy on most days, 
areas  with  many  cabins  may  experience  a  pronounced  coincidence 
factor  during  holidays  when  numerous  consumers  are  present.  These 
differences  may  not  be  captured  when  using  unsupervised  clustering 
algorithms, and the clusters generated with unsupervised clustering al-
gorithms may be capturing unintended attributes about building electric 
load patterns than anticipated. Supervised classification methods pro-
vide an alternative to clustering that offers more control of the assign-
ment of labels to building load profiles. While supervised classification is 
widely used in many classification tasks, only a few supervised classi-
fication  of  electricity  load  profiles  from  buildings  have  been  demon-
strated in research for deriving the building class and meta data about 
buildings,  likely  since  supervised  learning  techniques  require  a  large 
amount of labelled data for training, validation, and testing with clear 
segmentation.  One  example  where  supervised  classification  has  been 
used on smart meter data is for prediction building energy consumption, 
such as in [18] for an office building in New York to categorize energy

consumption into one of four predefined patterns, representing weekend 
use,  night  use,  and  weekday  use  during  summer/winter.  Supervised 
classification has also been used to classify the energy performance of 
2717 commercial buildings in Hong Kong from meta data and measured 
energy  use  when  their  size  were  unknown,  achieving  an  accuracy  of 
78.8 % with random forest. This approach did however rely on meta 
data  as  input  features  which  are  usually  not  available  within  smart 
meter databases or in publicly available statistics elsewhere. Similarly, 
[19] demonstrated  a  classification  model  based  on  artificial  neural 
network  for  classifying  energy  performance  certificated  of  Italian 
buildings. The input features of this classification were mostly meta data 
present  in  the  buildings’  EPCs,  like  U-values,  area,  degree  days  and 
volume etc, and the only measured input value was CO2-emissions from 
the  buildings.  The  model  showed  to  receive  up  to  99  %  accuracy 
depending on included features but could only achieve an accuracy of 
75  %  without  measured/calculated  data  of  energy  use  or  CO2-use, 
which is directly linked to the EPC of the building.

There are a few examples where meta data from buildings has been 
extracted  from  smart  meter  data  using  supervised  classification.  One 
supervised classification of building categories used a semi-supervised 
approach  to  group  3  months  data  from  114  non-residential  buildings 
into 17 different building typologies using a follow-the-leader clustering 
approach and achieved an accuracy of 80 % [20]. In another example, a 
supervised  learning  approach  with  domain-informed  and  domain- 
agnostic features were used to estimate the country of buildings from 
4 different countries [21]. Supervised learning was used in two studies 
with  several  thousand  smart  meters  from  Ireland  to  extract  metadata 
about the households such as heating type, floor area, age and number of 
inhabitants.  48  (number  of  bedrooms,  4  classes)  –  84  %  (single/not 
single  occupant)  accuracy  dependent-independent  data  classification 
(DID)  and  probabilistic  regression  [22],  and  in  [23] to  estimate  the 
household  size  class  (number  of  adults  and  children)  of  the  Irish 
dwellings. The latter did however show that that the smart meter data 
alone was limited to distinguish the household category and achieved a 
low  accuracy.  To  the  best  of  the  authors  knowledge,  there  exist  no 
method or application for classifying the standard building category and 
heating  type  of  buildings  from  their  smart  meter  data,  and  there  is 
limited  research  on  supervised  classification  of  smart  meter  data  for 
extraction of building meta data in datasets containing both residential 
and non-residential buildings.

1.1. Contributions

The  primary  research  problem  addressed  in  this  article  is  how  to 
collect metadata for buildings’ smart meter data when it is not readily 
available,  specifically  their  building  category  and  heating  type.  Col-
lecting  information  about  buildings  is  a  difficult  and  time-consuming 
task  that  typically  requires  manual  effort.  To  address  this,  there  is  a 
need for a method that is generalizable to smart meter data of different 
durations, without relying on additional metadata, that can be applied 
to buildings of varying locations, types, sizes, ages, and energy perfor-
mance levels.”

This article introduces a novel supervised classification method for 
segmenting  smart  meter  data  from  buildings  into  standardized  cate-
gories. While the true number of classes is considered unknown in most 
classification  approaches  of  smart  meter  data,  this  approach  uses  the 
standard building categories from the Norwegian building regulations as 
labels  to  develop  a  model  that  can  differentiate  between  different 
building  categories,  including  both  residential  and  non-residential 
buildings. In short, the contributions of this paper are:

-  A  supervised  classification  approach  for  segmenting  smart  meter 
data from buildings into standardized building categories, including 
both residential and non-residential buildings as well as their heating 
class (electric and non-electric).

2

---

<!-- PAGE 3 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

-  The classification approach is trained and tested on a large and novel 
dataset  of  hourly  data  from  more  than  2700  Norwegian  buildings 
from 11 building categories (including 4 residential categories and 7 
non-residential  categories).  To  the  best  of  the  authors  knowledge, 
there  are  no  other  building  category  classification  approaches  in 
research based on a dataset on this scale, and most approaches found 
in the literature are focused on either residential or non-residential 
buildings separately.

- For the classification, 82 physics-based domain features are extrac-
ted from each of the smart meter time series from the buildings. The 
features  can  be  extracted  from  any  hourly  electricity  smart  meter 
data series from buildings with a duration of months-years.

- A comparison between the proposed supervised method and an un-
supervised  classification  of  the  smart  meter  data  using  K-means 
clustering is presented, showing how a supervised approach is more 
suited  for  classifying  buildings  into  their  standardized  building 
categories.

-  The method is generalizable to other Norwegian buildings outside 
the dataset and is in addition tested against external, openly avail-
able datasets of electricity consumption in buildings from other lo-
cations and climate zones and compared the model results from the 
suggested  approach  against  unsupervised  methods  for  building 
category classification.

2. Methodology

This article presents a method to classify buildings’ AMS-data into a 
building category and heating type (electric/non-electric). This section 
describes the dataset used to develop and test this method, the labels of 
the buildings in the dataset, the physics-based domain features extracted 
for  each  building,  and  different  models  tested  for  the  classification 
problem.

2.1. Dataset and labels

To develop and test the classification method, a large data set con-
taining files with several years of hourly electricity and outdoor tem-
perature measurements from 2724 buildings located in Norway is used. 
The dataset consists of both openly available data and classified data 
provided  by  Drammen  Municipality,  FME  ZEB  [24],  FME  ZEN  [25], 
Elvia, Statkraft, Risvollan Housing Association, Sikom, Statsbygg, and 
other project partners. More information about the file structure of the 
building  files  is  described  in  [26].  Every  building  in  the  data  set  is 
labelled  with  a  building  category  (cid:0) describing  the  primary  use  of  the 
building (cid:0) which are the standardized building categories used in the 
Norwegian building code TEK-17 [16], and in the standard for energy 
calculations of buildings in Norway [17]. Each building is also labelled 
with a heating type (describing whether the building has electric/non- 
electric space heating) and with a resulting building type (combination 
of the building category and heating type). A summary of the labels and the 
support within each building type is given in Table 1.

2.2. Feature generation

Table 1 
Building type labels and the number of buildings in the dataset.

Building 
category in 
TEK17

Building 
category 
label

Building 
type label

Number 
of 
buildings

Heating 
type 
(Electric 
Heating 
(EH)/ non- 
electric 
heating 
(NEH))

Labels for 
building 
category 
and type 
(not 
present 
in 
dataset 
in grey)

House

Hou

Apartment

Apt

Apartment 
blocks*
Cabin/ 
Holiday 
house
Office

Nursing 
home
Hotel

Apb

Cab

Off

Nsh

Htl

Kindergarten

Kdg

School

Shop

Hospital

Culture

Sport

University

Sch

Shp

Hsp

Cul

Spo

Uni

NEH
EH
NEH
EH
NEH
EH
NEH
EH

NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH
NEH
EH

*In the database and in the Norwegian building codes

TEK17, apartments (section within an apartment block) 
and apartment blocks are both labelled the same. In this 
dataset, these are separated into apartments and 
apartment blocks.

Hou_NEH
Hou_EH
Apt_NEH
Apt_EH
Apb_EH
Apb_NEH
Cab_NEH
Cab_EH

Off_NEH
Off_EH
Nsh_NEH
Nsh_EH
Htl_NEH
Htl_EH
Kdg_NEH
Kdg_EH
Sch_NEH
Sch_EH
Shp_NEH
Shp_EH
Hsp_NEH
Hsp_EH
Cul_NEH
Cul_EH
Spo_NEH
Spo_EH
Uni_NEH
Uni_EH
Total

67
473
1344
400
53
51
0
128

54
7
21
6
7
0
11
20
32
16
28
0
6
0
0
0
0
0
0
0
2724

make  the  building  time  series  data  comparable.  By  focusing  on  key 
features such as average energy consumption, seasonal variations, and 
usage patterns, we can reduce the bias in the dataset caused by differ-
ences in e.g. durations and improve  the accuracy of predictions. This 
approach ensures that the classification model compares similar features 
across different datasets and reduce the data quantity and the running 
time.  Here,  82  physics-based  domain  features  are  generated  for  each 
building from its electricity load and temperature time series. The fea-
tures are categorized into 5 feature groups:

-  Non-normalized electricity load features.
-  Electricity load variation features.
-  Seasonal differences features.
-  Average daily profile features.
-  Standard load profile correlation features.

Smart  meter  data  collected  from  different  sources  will  often  have 
varying  start  dates,  end  dates,  seasons,  and  durations.  These  discrep-
ancies in time series data can lead to inaccurate predictions, as it may 
result  in  comparing  apples  to  oranges.  One  can  consider  a  scenario 
where image recognition is used to differentiate between schools and 
apartment blocks based on their smart meter data. If all school buildings, 
except one, have data spanning four years, while all apartment blocks 
have data covering only one year, the single school with only one year of 
data might be incorrectly classified due to the difference in data dura-
tion. To address this issue, feature extraction can be employed. Feature 
extraction  involves  identifying  and  extracting  relevant  patterns  and 
characteristics from the smart meter data, which can then be used to

A list of all features within each group is given in the following sub

chapters.

2.2.1. Non-normalized electricity load features

Four  features  describe  the  non-normalized  data  of  the  buildings’ 
electricity load. These features capture the size of the peak load, and 
mean electricity use and the relationship between the electricity load 
and outdoor temperature. These features extract information about the 
size of the building (which is important to gain information about the 
building type) and the temperature dependency of the load. The last two 
features  look  at  the  relationship  between  the  electricity  use  and  the

3

---

<!-- PAGE 4 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

outdoor temperature. The first is the outdoor temperature at the peak 
electricity load, and the second is the imported electricity at the mini-
mum  outdoor  temperature.  A  summary  of  the  Non-normalized  elec-
tricity load features are given in Table 2.

2.2.2. Electricity load variation features

The 32 electricity load variation features are normalized electricity 
load features that look at peak load (max), average load, the relationship 
between  them,  and  the  hour  of  the  day  when  peak  load  occurs  for 
different  subsets  of  the  data  –  for  example,  during  the  wintertime, 
summertime, or for the entire dataset. The subsets are chosen to examine 
season  and  temperature  dependent  variations.  The  winter  season  is 
defined as December-February, spring as March-May, summer as June- 
August  and  autumn  from  September-November.The  electricithy  load 
vatriation features are summarized in Table 3.

2.2.3. Seasonal differences features

Seasonal  variation  and  temperature  dependency  can  provide  an 
indication of whether the building uses electricity for space/ventilation 
heating. To further capture such effects, 6 seasonal differences features 
are added. They are intended to complement the electricity load varia-
tion features and to specifically investigate the relationship between the 
summer and winter features as these are the most important features to 
evaluate whether a building has electric heating or not. These features 
examine the differences in the mean and max in summer and winter. The 
seasonal differences features are summarized in Table 4.

2.2.4. Average daily profile features (normalized data)

The  16  “Average  daily  profile  features”  are  features  which  are 
generated  to  extract  traits  from  the  daily  load  profile  are  given  in 
Table  5,These  features  represent  specific  patterns  that  explain  user 
behaviour and variations throughout a day that can indicate the type of 
building  from  its  electricity  load  profile.  The  features  are  selected  to 
capture  the  most  important  elements  that  can  indicate  the  building 
category based on domain knowledge. These features provide a stronger 
insight compared to just giving the daily load profile values (Fig. 1).

2.2.5. Standard load profile correlation features (normalized data)

To capture the similarities between the daily user patterns in build-
ings and the user patterns of similar building types, 24 standard load 
profile  correlation  features  are  extracted  as  shown  in  Table  6.  The 
standard load profile correlation features describe the extent of corre-
lation of daily load profile of each building with standard load profiles of 
different building types. The standard load profiles are generated using 
the PROFet model [25]. PROFet is an aggregated load profile generator 
which  can  predict  hourly  load  profiles  for  both  thermal  loads  and 
electric loads, based solely on outdoor temperatures and building area. 
PROFet is based on panel regression of energy measurements of build-
ings  from trEASURE,  a database, of monitored  buildings, mostly con-
nected to district heating. PROFet can estimate the typical load profile of 
an area based solely on building area input (for 12 building categories 
and 3 energy efficiency levels as described in the categorization) and 
outdoor  temperatures  [25,27,28].  PROFet  has  been  used  to  create 
standard load profiles for 11 building categories (all building categories

Table 2 
Non-normalized electricity load features.

Feature notation

Description

ElImp_actual_max

ElImp_actual_mean

Tout_at_ElImp_max

ElImp_at_Tout_min

The actual (non-normalized) peak load of the imported 
electricity load profile of the building
The actual (non-normalized) mean value of the imported 
electricity load profile of the building
The outdoor temperature when the electricity peak load 
occurs.
The electricity load when the minimum outdoor temperature 
occurs.

Table 3 
Electricity load variation features.

Feature notation

Description

Subset of data

All data, winter, spring, 
summer, autumn, Weekdays, 
Weekends, the outdoor 
temperature is below 10C

ElImp_max

ElImp_mean

ElImp_max_vs_mean

ElImp_max_hour

The actual peak load of the 
imported electricity load 
profile of the building
The mean value of the 
imported electricity load 
profile of the building
The maximum peak load 
divided by the mean of the 
peak load profile of the 
building.
The hour of day when the 
peak load occurs.

Table 4 
Seasonal differences features.

Feature notation

Description

ElImp_max_vs_summer_max

ElImp_mean_vs_summer_mean

ElImp_winter_mean_vs_summer_mean

ElImp_max_vs_winter_max

ElImp_mean_vs_winter_mean

ElImp_winter_max_vs_summer_max

The maximum peak load divided by the 
peak load during the summer
The mean electricity load divided by the 
mean peak load during the summer
The mean electricity load during winter 
divided by the mean electricity load during 
summer
The peak load divided by the peak load 
during the winter
The mean electricity load divided by the 
mean electricity load during the winter
The peak load during the winter divided by 
the peak load during the summer.

Table 5 
Average daily profile features.

Feature notation

Description

daily_average_profile_max

daily_average_profile_max_hour
daily_average_profile_min

daily_average_profile_min_hour
daily_average_max_over_min

daily_average_median
daily_average_profile_max_after

daily_average_profile_max_before

daily_average_std

daily_average_var
daily_average_profile_second_max

daily_average_profile_second_max_hour

daily_average_profile_max_change

daily_average_profile_max_change_hour

daily_average_profile_min_change

daily_average_profile_min_change_hour

A. Maximum value during the average 
day.
B. Hour when maximum value (A) occurs
C. Minimum value during the average 
day.
D. Hour when minimum value (C) occurs
Maximum divided by minimum value (A/ 
C)
E. Median value of the daily load profile.
The value at the hour after the maximum 
value (value at B + 1)
The value at the hour before the minimum 
value (value at B-1)
Standard deviation of the daily average 
profile
Variation of the standard profile
F. The second highest hourly value during 
the average day.
G. The hour when the second highest 
value occurs.
F. The hour when the change is biggest 
(positive) from the past hour to the 
current hour.
G. The hour after the biggest (positive) 
change during the day.
H. The highest negative change during the 
average day from the past hour to the 
current hour.
I. The hour after the largest negative 
occurs.

in Table  1, excluding cabins,  industry and  cultural buildings) using a 
standard weather profile from Norwegian Standards NS3031 [29]. To 
create  standard  profiles  that  represent  the  average  energy  efficiency 
standard of the building stock, it is assumed that the buildings are 82 %

4

---

<!-- PAGE 5 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

to differences in the outdoor temperatures throughout the year. Resi-
dential buildings typically have a small peak in the morning and a higher 
peak in the evening, while service buildings have a peak during the day. 
The rise in energy consumption in the mornings typically starts earlier in 
buildings with electric heating compared to buildings without electric 
heating due to the time needed to heat buildings in the morning, and due 
to the electricity need for hot water in residential buildings. Standard 
load profile features are calculated as the correlation between each of 
the standard daily load profiles and the average daily load profile of the 
building. There is one feature for the correlation between the building 
and each of the available load profiles.

2.3. Classification models

For the classification task of assigning building category and building 
type  labels  to  previously  unseen  electricity  time  series  data  from 
buildings,  a  selection  of  machine  learning  classifiers  were  explored 
utilizing the Scikit Learn library in Python version 1.3.0 [30]. The tested 
classifiers include the following with default parameters: Decision Tree 
Classifier [31], RandomForest Classifier [32]., Support Vector Machines 
Classifier  [33],  Gradient  Boosting  Classifier  [34],  AdaBoost  Classifier 
[35] and CatBoost Classifier [36] In addition, the best performing from 
this list is evaluated against Unsupervised K-means clustering [37] and 
Soft-voting ensemble learning [38].

2.4. Training and testing

To train and test the classification methods, the dataset comprising 
2724 buildings has been randomly split with an 80/20 partition into the 
training set (2179 buildings) and a test set (545 buildings).

2.5. Performance metrics

To evaluate the performance of the different classification models, a 
diverse set of performance metrics are employed. These metrics serve as 
quantitative measures to gauge various aspects of model performance, 
including accuracy, accuracy when providing two possible labels, pre-
cision, recall and F1-score. By applying these performance metrics, it is 
possible to quantitatively get an understanding how well the models can 
correctly  label  previously  unseen  data.  The  performance  metrics  are 
described in Table 7.

3. Results

3.1. Prediction of building type

Different models are applied on the dataset with extracted features to 
classify the building type (building category + heating type). Classifica-
tion  of  the  test  set  has  been  performed  based  on  training  the  models

Fig. 1. The average daily load profile of a building and indication of where the 
features in Table 5 are collected from the daily profile.

Table 6 
Standard load profile correlation features.

Feature notation

Description

correlation_daily_SLP_*_EH

correlation_daily_SLP_*_NEH

Correlation between the daily load profile of the 
building and the standard category with electric 
heating
Correlation between the daily load profile of the 
building and the standard category without electric 
heating

*One of the following category abbreviations (see Table 1): Apt, Hsp, Hou, Htl, Kdg,

Nsh, Off, Oth, Sch, Shp, Spo, Uni

“regular”  and  18  %  “efficient”.  To  make  standard  load  profiles  for 
buildings with and without electric heating, it is assumed that buildings 
with electric heating has an electricity consumption equal to the total 
demand of the buildings (including electric specific demand, domestic 
hot water heating and space heating). It is also assumed that buildings 
without electric heating have an electricity consumption equal to the 
energy  demand  for  electric  specific  loads.  An  example  of  the  daily 
standard  load  profiles  for  apartments  and  schools  with  and  without 
electric heating is shown in Fig. 2.

The standard load profiles are generated for one year before they are 
normalized.  Average  hourly  daily  load  profiles  are  then  created.  The 
average daily load profiles for some of the standard building categories 
are shown below. Several patterns can be observed from these figures. 
Buildings with NEH tend to  have higher  normalized loads during the 
average day due to less variations during the year compared to buildings 
with electric heating, where there are large variations in the peaks due

Fig. 2. Standard daily load profile of different building categories (a) with and (b) without electric heating.

5

---

<!-- PAGE 6 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Table 7 
Definition and description of performance measures.

Metric

Equation

Description

Accuracy

(Acc) (32)

Top-2

accuracy
Precision(33)

Recall  
(33)
F1-score  
(33)

TP + TN
TP + TN + FP + FN
A1(cid:0) 2
TP + TN + FP + FN

TP
TP + FP
TP
TP + FN
2 • prec. • recall
prec. + recall

The share of predictions that were correct

The share of predictions that were correct in 
one of the two most likely classes.
The share of predicted positive that were 
correct.
The share predictions that should have been 
predicted as true that were correct.
Combination of precision and recall that 
strongly penalizes low precision or recall.

Example with

classification of 
a building as 
“Office”.

Actual

Office

Not 
Office

Predicted
Office

Not Office

True 
Positive 
(TP)
False 
Positive 
(FP)

False 
Negative 
(FN)
True 
Negative 
(TN)

A1(cid:0) 2 = Number of cases where 
the true label is in the top 2 
predicted labels. 
R = number of classes. Mr=
performance. metric for class r. 
N = total number of samples. 
Nr= number of samples within 
class r.

described in section II. C. on the training set. The results of the perfor-
mance in correctly identifying the labels of the unseen training set are 
described  in  Table  8 and  in  the  confusion  matrices  of  the  test  set  as 
shown in Fig. 3. The results show that the Random Forest Classifier and 
CatBoost Classifier perform the best overall on all performance metrics. 
They achieve similar results, with an overall accuracy of approximately 
0.84.  When  considering  two  possible  labels  (top  2  accuracy),  these 
models achieve an accuracy of 0.92, meaning there is a 92 % chance that 
one out of the two provided categories is the correct label for the given 
load profile. They outperform each other on different metrics, but the 
differences  are  minimal.  Given  this  information,  the  Random  Forest 
Classifier may be preferred over the CatBoost Classifier as it is a much 
faster  algorithm,  while  still  offering  similar  overall  performance.  The 
Gradient  Boosting  Classifier  and  Decision  Tree  Classifier  also  provide 
satisfactory results with accuracies of 0.77 and 0.81, respectively, while 
Support Vector Machines (SVM) classifier and AdaBoost Classifier show 
poor  performance,  with  accuracies  of  0.60  and  0.28  respectively.  Ex-
amination of the confusion matrices reveals a tendency for these clas-
sifiers  to  disproportionately  allocate  unseen  data  labels  to  classes 
abundant in the training set, indicating a bias towards unbalanced data.
Analysis of the confusion matrices for the Random Forest Classifier 
and CatBoost Classifier indicates minimal confusion between residential 
and  commercial  buildings  overall.  However,  within  these  categories, 
there exists confusion among specific subcategories.

3.2. Prediction of building category

In another experiment, the best performing models, Random Forest 
Classifier and CatBoost Classifier, are tested on how well they perform in 
predicting only the building category without the heating type (electric/ 
non-electric).  The  results  are  summarized  in  Table  9 and  the  corre-
sponding  confusion  matrix  in  Fig.  5.  The  overall  performance  on

Table 8 
Performance of different models on the test set when predicting building type.

Model

Acc.

Decision Tree
Random Forest
Gradient

Boosting

SVM
Ada Boost
Cat Boost

0.765
0.844
0.809

0.596
0.281
0.842

Acc. top 
2

0.771
0.925
0.897

0.000
0.325
0.919

Preci- 
sion

0.782
0.827
0.805

0.453
0.492
0.835

Recall

F1

0.765
0.844
0.809

0.596
0.281
0.842

0.767
0.832
0.801

0.496
0.180
0.834

Run 
time

0.4 s
2.8 s
179.4 s

0.2 s
1.9 s
121.9 s

estimation of the building category is approximately 0.89 in accuracy, 
precision, recall and F1-score for both models, while the top-2 accuracy 
is  0.97–0.98.  The  performance  is  hence  better  for  the  classification 
approach  when  only  predicting  building  category  and  not  also  the 
heating type. This is likely due to a combination of less complexity as 
well  as  uncertainty  in  the  labelling  of  the  heating  categories  of  the 
buildings.

3.3. Prediction of building type with feature selection

To check if there are more optimal solutions with a different com-
bination  of  features,  Forward  Sequential  Feature  Selection  (FSFS)  is 
applied to find best performance from various subsets of 82 features. In 
this  technique,  an  iterative  model  is  built  by  adding  one  feature  at  a 
time, starting from an empty set of features. At each iteration, the al-
gorithm evaluates the performance of the model with the addition of 
each  feature  and  selects  the  one  that  results  in  the  best  performance 
according  to  accuracy.  This  process  continues  until  all  features  are 
included. Fig. 6 shows the evolution of the best accuracy on the test set 
when the number of features included is varied from 1 to 82. The per-
formance appears to reach an elbow when 7–12 features are included. 
Table 10 shows the top 9 features that are included stepwise and the 
corresponding improvement in performance.

3.4. Comparison with ensemble learning

Ensemble  models  in  classification  problems  involve  combining 
multiple individual classifiers to generate a more accurate and robust 
prediction  than  any  single  model  could  achieve  alone.  Common 
ensemble techniques include bagging, boosting, and stacking. Ensemble 
models  are  widely  utilized  in  various  domains  due  to  their  ability  to 
improve  classification  accuracy  and  generalization  while  reducing 
overfitting. To estimate if the classification accuracy can be improved 
through  ensemble  learning,  an  ensemble  voting  classifier  with  soft 
voting  is  investigated.  Two  ensemble  models  are  tested:  one  which 
combines the Random Forest and CatBoost classifiers, and one where 
also Gradient Boosting is included. Ensemble models can be affected by 
class imbalance in data. To investigate if this is the case for this classi-
fication problem, a second test is performed where the ensemble models 
are applied on a subset of the dataset with only residential buildings. The 
results of applying ensemble model on the entire dataset and only on 
residential buildings in the dataset is shown Table 11. The results show 
that the ensemble model has a performance lower but close to the per-
formance  of  using  the  Random  Forest  or  CatBoost  Classifiers  alone 
(approximately 84 % on the entire dataset as shown in Table 11 for both 
the entire dataset and for the subset containing only residential build-
ings. A reason for this may be that these models associate a very high 
value or importance to the same set of features as shown in Fig. 4, and 
combining  them  does  not  provide  any  advantage  in  improving  the 
performance measures (Table 12).

3.4.1. Comparison with k-means clustering

K-means  clustering  is  a  popular  unsupervised  learning  algorithm 
used to partition a dataset into clusters based on similarity. It works by 
iteratively assigning data points to the nearest cluster centroid and then 
recalculating the centroids based on the mean of the points assigned to 
each cluster. This process continues until the centroids converge or a 
specified number of iterations is reached. In classification, the clusters 
generated  by  k-means  can  represent  different  classes  or  categories 
within the data. The elbow method and silhouette score are both tech-
niques  used  to  help  find  the  optimal  number  of  clusters  in  k-means 
clustering. The elbow method helps find the best number of clusters in k- 
means by looking for a bend (elbow) in the plot of cluster number vs. 
within-cluster sum of squares. The silhouette score measures how close 
each  point  in  one  cluster  is  to  points  in  the  neighbouring  clusters, 
indicating cluster quality. Higher silhouette scores and noticeable bends

6

---

<!-- PAGE 7 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Fig. 3. Confusion matrix of building type classification with different classifiers. Fig. 4 shows feature importance exhibited by the CatBoost, Random Forest and 
gradient boost classifiers.

in the elbow plot suggest better clustering solutions.

The elbow method and silhouette scores were calculated for different 
numbers of  k on the dataset with  results shown in Fig. 7.  The Elbow 
method suggest the number of optimal clusters for the given dataset is 
around 6. Fig. 8a shows how the buildings in the test set are assigned to 
different  clusters  when  6  clusters  are  used.  It  shows  that  residential 
buildings  are  all  grouped  together,  while  commercial  buildings  are 
grouped in three other groups. Fig. 8b shows the outcome of grouping 
the buildings in the dataset into 17 clusters, the same number of clusters 
as available labels in the dataset. It notably segregates various residen-
tial buildings to a greater extent compared to the solution with 6 clus-
ters,  capturing  the  variation  in  the  original  labels  more  closely. 
However, it suggests a prioritization of certain similarities over those 
represented by the labels. If the objective of classification is to correctly 
categorize  buildings  according  to  the  categories  used  in  Norwegian 
building codes and standards, supervised learning appears to excel in 
assigning  the  correct  labels  compared  to  unsupervised  k-means 
algorithms.

3.5. Testing of model on external datasets

To investigate the generalizability and transferability of the trained 
model, features and labels, the classification approach is tested on three

external datasets, published by researchers outside of the project, but 
relabelled by the authors for testing the classification methods devel-
oped  in  this  paper.  The  purpose  of  this  is  to  investigate  whether  the 
building categories/types and selected features are transferrable across 
countries  and  climate  zones.  The  external  datasets  include  the  iFlex- 
dataset [39] with electricity time series data from residential buildings 
in  Norway,  the  HUE-dataset  [40] which  is  an  hourly  dataset  of  elec-
tricity use in Canadian residential buildings, and the BDG2-dataset [41]
which  includes  non-residential  buildings  in  the  USA  and  the  United 
Kingdom.  For  each  external  dataset  the  buildings  were  relabelled  ac-
cording to the labels presented in Table 1. The same 82 features were 
extracted  from  the  electricity  meter  data  for  the  external  datasets. 
Different tests were conducted, where the original dataset presented in 
this article were used for training, and the external datasets were used 
for testing (and training).

3.5.1. Application on iFlex dataset (Norwegian households)

The  iFlex  dataset  consists  of  a  year  of  hourly  AMS-measurements 
from  over  2000  residential  units  (apartments  and  houses)  in  Norway 
from 2020 to 2021 [39]. The buildings were relabelled to the same la-
bels used in Table 1 based on survey answers from the residents. The 
classification method was tested on the iFlex-dataset in two ways – first, 
using the original training set and the iFlex-dataset as the test set and

7

---

<!-- PAGE 8 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Fig. 4. Feature importance for Random Forest for building type classification.

Table 9 
Performance of CatBoost and Random Forest on the test set when predicting only 
the building category.

Model

Accuracy

Accuracy Top 2

Precision

Recall

F1

Random Forest
CatBoost

0.892
0.888

0.967
0.98

0.895
0.894

0.892
0.888

0.891
0.888

Fig.  5. Confusion  matrix  for  Random  Forest  on  the  test  set  when  predicting 
only the building category.

next, splitting the iFlex dataset into a training and testing set. Applying 
the  method  resulted  in  an  accuracy  of  0.7  when  using  the  original 
dataset for the training and iFlex-dataset for the testing. When using the 
iFlex-dataset  for  both  testing  and  training,  the  accuracy  improved  to 
0.75. A reason for the performance not being higher for the iFlex-dataset

8

is that it only contains residential buildings, where the accuracy is lower 
compared to the accuracy for the entire dataset.

3.5.2. Application on HUE dataset (Canadian households)

HUE (The Hourly Usage of Energy Dataset for Buildings in British 
Columbia)  is  a  dataset  that  comprises  of  hourly  energy  use  measure-
ments  from  28  residential  buildings  in  Canada  (26  with  sufficient  la-
bels).  The  buildings  were  relabelled  as  either  “Hou”  or  “Apt”.  The 
buildings in the HUE dataset were all correctly identified as residential 
buildings. The method however failed to correctly identify the correct 
building type in more than half of the cases and was unable to accurately 
separate  between  houses  and  apartments.  When  predicting  only  the 
building category (and not the heating type) all apartments are correctly 
predicted, while houses were mostly confused for being apartments as 
well. The top 2 accuracy was however perfect for predicting the building 
category.

3.5.3. Application on BDG2 dataset (USA and UK service buildings)

BDG2 (Buildings Data Genome 2) is a dataset with 2 years of hourly 
energy measurements (gas, cooling water, steam, and electricity) from 
1636  non-residential  buildings/rooms  located  in  North  America/ 
Europe. Two tests were conducted with the BDG2-dataset. In the first 
test,  a  selection  of  buildings  were  relabelled  based  on  their  primary 
building category to the corresponding labels in Table 1. In the second 
test,  the  BDG2-dataset  was  used  for  both  training  and  testing  and 
without  relabelling,  but  instead  using  the  original  “Primary  use  cate-
gory”  as labels. Some buildings were excluded due to missing data or 
labels.

4. Discussion

4.1. Results for classification of building type and category

This article has presented results for building type classification of 
electricity time series from buildings. RandomForest Classifier and the

---

<!-- PAGE 9 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Fig. 6. Evolution of accuracy and precision for the building type classification using Random Forest Classifier and FSFS.

Table 10 
Evolution  of  accuracy  and precision  for the building  type  classification using 
Random Forest Classifier and FSFS until the 9th feature is added.

N

1
2
3
4
5
6
7
8
9

Feature added

Accuracy

Precision

ElImp_actual_mean
+ daily_average_std
+ correlation_daily_SLP_SLP_Apt_EH
+ ElImp_max_vs_mean_weekend_is_1
+ ElImp_mean_vs_winter_mean
+ ElImp_actual_max
+ ElImp_max_weekend_is_1
+ ElImp_max_weekend_is_0
+ ElImp_max_season_is_1

0.624
0.761
0.802
0.820
0.831
0.850
0.861
0.862
0.864

0.616
0.752
0.785
0.799
0.816
0.831
0.839
0.841
0.843

CatBoost  classifier  give  similar  performance  results,  but  the  Random-
Forest Classifier is a much faster approach and is hence preferred for this 
classification. The building type (building category and heating type) is 
correctly identified in 84 % of the cases, and with a 92 % top-2 accuracy. 
The accuracy reaches a peak of approximately 86 % when feature se-
lection  is  used.  This  is  a  high  and  sufficient  accuracy  for  this  task, 
especially given as there is some uncertainty in the labels of the dataset, 
which is further elaborated in F.

4.2. Features and feature selection

The features extracted in II. B. are chosen based on domain knowl-
edge  on  Norwegian  load  profiles.  Other  features  considered  but  not 
included were hourly values of the typical day, average daily values of 
the typical week with variations on seasons and day types. These fea-
tures were discarded in an early phase as they reduced the performance 
by increasing the number of features too much, and because the infor-
mation  from  these  features  are  captured  by  other  features.  Another 
possible way to capture the daily load profiles or yearly profiles could be 
to use pattern based or shape based features as shown in [42].

The SLP-features use standard load profiles based on [24,25]. 123 
buildings  from  the  dataset  used  in  this  work  were  also  amongst  the 
buildings used to extract information to generate the PROFet tool which 
was used as a base to generate the SLP features. Using these features 
could have introduced a small data leakage. To investigate this effect, 
the  accuracy  of  predicting  the  building  type  as  shown  in  III.  A.  was 
calculated  with  and  without  these  features.  The  accuracy  with  SLP 
features is 0.844 as compared to 0.839 without using the SLP features.
The number of and combination of features used affects the perfor-
mance  of  the  classifier.  It  is  therefore  possible  that  a  more  optimal 
combination  of  features  could  exist  or  features  not  suggested  in  this

Table 11 
Performance of ensemble model, CatBoost and random forest when applied to the whole dataset and only residential buildings.

All

Residential

Model

Ensemble_model_soft (RF + CB)
Ensemble_model_soft(RF + CB + GB)
RandomForest
CatBoost
Ensemble_model_soft (RF + CB)

Acc.

0.844
0.840
0.861
0.847
0.858

Acc. top 2

Preci-sion

0.917
0.919
0.935
0.937
0.937

0.831
0.827
0.836
0.826
0.833

Recall

0.844
0.840
0.861
0.847
0.858

Table 12 
Performance of the method when applied to three external datasets (iFlex, HUE and BDG2).

iFLEX

HUE

BDG2

Train: Original
Test: iFlex
Train: 0.8 iFlex
Test: 0.2 iFlex
Train: Original
Test: HUE
Train: Original
Test: BDG2 
(selected)
Train: 0.8 BDG2
Test: 0.2 BDG2

N

2179
1096
876
220
2179
26
2179
566

1224
306

Target

Building type

Building type

Building category

Building category

Acc.

0.711

0.750

0.462

0.203

Acc. top 2

Precision

0.876

0.923

1.000

0.357

0.719

0.743

0.821

0.533

Recall

0.711

0.750

0.462

0.203

Primary categories from BDG2

0.565

0.755

0.519

0.565

0.521

9

F1

0.833
0.830
0.848
0.836
0.846

F1

0.708

0.745

0.439

0.237

---

<!-- PAGE 10 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Fig. 7. (a) Distortion and (b) silhouette score for different numbers of clusters using k-means clustering.

Fig. 8. Clustering of buildings in the dataset when using (a) 6 and (b) 17 clusters with k-means clustering. In both cases, the test set has no buildings assigned to one 
of the clusters.

article may lead to further improvement in accuracy. The performance 
will also vary slightly depending on which buildings are included in the 
training and test set.

4.3. Ensemble learning

While ensemble models are often powerful tools for improving ac-
curacy, soft-voting ensemble models did not improve the performance 
compared  to  RandomForest  and  CatBoost  classifiers  alone  in  III.  D. 
Ensemble models may not enhance performance due to several factors. 
These  include  redundancy  and  correlated  errors  among  base  models. 
This was to be expected due to the similarities in feature importances for 
these models but could not be ruled out without investigation.

4.4. Supervised vs. Unsupervised classification

The literature on building electricity load profiles shows that there 
are  many  examples  of  unsupervised  clustering  algorithms  used  for 
classification of buildings, efficiency classification of buildings and fault 
recognition of building electricity use. While unsupervised clustering of 
building  load  profiles  are  useful  for  many  applications,  including 
assigning pricing clusters of different costumers, supervised classifica-
tion  allows  to  get  more  tailored  labels  for  the  data,  which  can  help 
efficiently  collect  metadata.  In  this  article,  buildings  are  labelled and 
classified  according  to  the  building categories  used in  the  Norwegian 
building  code.  Achieving  the  same  classification  with  unsupervised 
methods  is  not  possible,  as  there  may  be  similarities  and  differences 
between  buildings  of  the  predefined  categories  which  will  not  auto-
matically be captured by an algorithm without training on labelled data 
and the domain-specific features.

4.5. Testing on datasets across geography and climate zones

The  classification  method  has  exhibited  good  generalizability  and 
transferability  to  Norwegian  residential  buildings,  but  poor  trans-
ferability to the HUE and BDG2-datasets. There are a few possible ex-
planations  for  this.  First,  the  primary  building  categories  used  in  the 
BGD2 dataset are broad categories with large disparities between the 
buildings within them. For example, the category “Education” contains 
the subcategories “School”, “Research”, “Student Centre”, “Classroom” 
among others, which are buildings which can be expected to have large 
disparities  in  user  behaviour  and  energy  systems,  while  the  building 
categories  in  the  original  dataset  contain  more  uniform  buildings, 
making them easier to distinguish from each other. Secondly, the fea-
tures extracted from the original dataset may not be the most suitable to 
predict  the  building category from other countries/climate  zones and 
with different labels, for instance, looking at features more targeted at 
changes  in  the  load  caused  by  cooling  and  ventilation  rather  than 
heating may improve the results. Another reason may be that service 
buildings such as schools, may have user patterns that differ greatly in 
different countries for aspects such as needs for cooling, ventilation and 
heating, different control strategies and HVAC systems. Finally, there is 
a large uncertainty in the quality of the labels of the buildings in the 
BDG2-database, as [43] showed the way a building’s occupants use the 
spaces  can  be  different  than  what  was  intended,  which  may  cause 
misclassification  or  oversimplification.  It  was  found  that  26  %  of  the 
buildings in the original BDG-dataset was potentially mislabelled based 
on their load shape behaviour.

Onsite  renewable  energy  production,  such  as  photovoltaic  (PV) 
panels mounted on buildings, can theoretically influence building load 
profiles by reducing the demand for imported electricity during periods 
of production. Although PV installations are becoming more common, 
most buildings  in the database currently do not have PV systems. PV

10

---

<!-- PAGE 11 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

generation typically peaks midday, especially during summer months. 
The  key  features  identified  by  feature  selection  focus  on  both  the 
average energy usage throughout the year and peak loads at different 
time periods. While mean and median electricity consumption might be 
affected  by  PV  generation,  peak  loads,  which  generally  occur  during 
winter  months,  are  less  likely  to  be  significantly  impacted  due  to 
reduced solar radiation and lower PV output during the winter season. 
The extent to which local renewable generation influences a building’s 
electricity import profile also depends on the ratio of energy production 
to consumption—the higher the production relative to consumption, the 
greater the impact on reducing imported electricity. While the classifi-
cation of building type (building category and heating category) may 
not be largely affected  by the presence  of PV, disaggregation of elec-
tricity use for different appliances becomes more challenging without 
separate  meters  for  PV  generation,  electricity  export,  and  self- 
consumption,  as  total  electricity  consumption  is  necessary  for  the 
disaggregation task. Classifying buildings with and without PV is a task 
that  could  be  considered  for  further  research,  if  data  from  more  pro-
sumers are attained. The buildings’ time series data include both smart 
meter  data  and  climate  data,  including  solar  radiation.  The  method 
presented is adaptable, so given the availability of a dataset with meta 
data about PV-installations, the method could be adapted to classify the 
presence  of  PV-panels  e.g.  by  adding  features  that  consider  the  rela-
tionship between solar radiation and electricity consumption.

4.6. Data quality and labelling

The reliability of the labels in the dataset used in this article are not 
completely  certain.  The  collection  of  metadata  to  be  used  for  the 
labelling  of  the  buildings  has  been  conducted  by  several  researchers 
using a variety of approaches, such as looking into building energy la-
bels  and  the  Norwegian  building  registry  (cadastre),  interviewing 
operational personnel, and building managers, and surveys.

The building categories of buildings in this database are the same as 
the building categories used in the Norwegian Standard NS 3031 “En-
ergy and Power Demand for Heating of Buildings (cid:0) Calculation Rules” 
[29] and  for  the  energy  requirements  in  the  regulations  on  technical 
requirements  for  construction  works  within  the  Norwegian  Building 
Acts  and Regulations [16].  Some  of these  building categories  contain 
buildings with large variations in energy consumption and user patterns, 
e.g. “Cultural buildings” which include buildings from churches to big 
concerts halls. The building categories used in these regulations differ 
from building types used in the cadastre, which divide buildings intro 
more groups. Another issue with the labelling of buildings in the data-
base is that buildings can only have one label, while a single building 
may have several uses, for example, a single building can consist of one 
part which is a school and another part which is an office but can only be 
assigned to one label in the database. Similarly, there is also some un-
certainty in the labelling of buildings with “Electric Heating (EH)”  or 
“Non-electric heating (NEH)”. The metadata about the heating system of 
different buildings are acquired by different researchers with different 
approaches, and the while the metadata indicates the kind of heating 
system  installed,  it  does  not  necessarily  indicate  if  all  the  installed 
heating appliances are in use. For some buildings, there may also have 
been a change in the heating system during the duration of the mea-
surements. One example is the use of oil and gas furnaces, which may 
have been in use until 2020 but exchanged later due to the fossil fuel ban 
for heating purposes in buildings that was enforced from January 2020. 
The use of heating appliances and electricity for heating may have been 
changed  for  several  buildings  with  measurements  that  span  across 
several years, but the label of heating appliances may not necessarily 
have been updated for all buildings in the database. The classifiers are 
trained only on certain building categories and cannot recognize other 
building  categories  not  present  in  the  dataset,  such  as,  industrial 
buildings, parking houses, culture buildings, universities, sports build-
ings, and others. The model could however benefit from being able to

recognize if a building should not be assigned to any of the labels present 
and classify them as “Other” or “NA”.

4.7. Consequences of misclassification

Predicting the wrong building category in the classification of elec-
tricity time series can have varying degrees of consequences depending 
on the subsequent use of the results. If utilized for labelling buildings 
before storing the data in a database for further reference, it is crucial to 
explicitly  note  that  the  assigned  building  category  is  an  estimation. 
Moreover, it may be beneficial to provide the two most probable cate-
gories to mitigate the risk of propagating errors throughout subsequent 
processes such as energy pricing, integration into demand forecasting 
models,  recommendations  for  energy-saving  measures,  and  further 
analysis and research.

In  the  authors’  ongoing  research,  the  intention  is  to  employ  the 
predicted building category to develop a disaggregation algorithm for 
separating electric space heating loads from total building loads, with 
the predicted category serving as an input. If a building with electric 
heating is falsely classified as a building without electric heating using 
this method, the disaggregation algorithm may fail to accurately identify 
the electric heating energy usage as intended. Separating buildings with 
air-to-air  heat  pumps  and  buildings  that  use  primarily  electric  panel 
heaters  can  be  challenging  on  hourly  data,  as  these  are  expected  to 
exhibit similar patterns, especially during.

peak  hours,  but  also  have  a  slightly  lower  daily  load  profile  on 
average. The model could be improved to estimate the heating type of 
buildings by adding more standard load profiles that differentiates be-
tween buildings with different building heating appliances.

4.8. Applications

As  described  in  the  introduction,  the  electrification  of  all  end-use 
sectors  is  essential  for  transitioning  to  a  sustainable  low-carbon  soci-
ety.  In  Norway,  the  building  sector  consumes  more  than  half  of  the 
nation’s electricity consumptions, primarily for heating, with demand 
peaking  during  the  coldest  days  of  winter.  With  electrification,  peak 
loads are expected to grow, and this raises the question on how we can 
limit the growth of peak loads. The suggested method has several ap-
plications and potential implementations that can aid in improving the 
knowledge on peak loads in buildings and areas, as well as on how to 
limit  the  peak  load.  By  classifying  the  presence  of  electrical  heating 
appliances, this approach offers a clearer understanding of energy con-
sumption  patterns  across  different  building  types.  If  the  method  is 
applied  by  energy  providers,  it  could  help  identify  and  tailor  energy 
efficiency and demand flexibility measures for electricity customers or 
analyse  the  use  of  different  grid  capacity  tariffs.  Additionally,  the 
method could support improved grid and area planning by estimating 
the presence of specific customer types in a given region, which could 
help predict coincidence factors and peak loads. In data collection, the 
classification of building types provides metadata which can often be 
time-consuming to collect manually. The estimated class of a building 
could be used as an input feature in a disaggregation task, such as dis-
aggregating electricity used for heating from a building’s electricity load 
profile, thereby improving disaggregation accuracy. In the future, the 
method could be expanded to classify other forms of metadata, such as 
electric  vehicle  charging,  photovoltaic  systems,  and  heating  types, 
further broadening its applications.

4.9. Future work

Future work includes enhancement and refinement of the presented 
methodology  for  classification  of  buildings.  Firstly,  one  may  benefit 
from  expanding  the  current  method  to  classify  the  type  of  electric 
heating systems present within buildings, which would provide valuable 
insights  into  energy  usage  patterns  and  aid  in  load  disaggregation.

11

---

<!-- PAGE 12 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

Similarly, the method could be extended to classify whether building is 
equipped  with  chargers  for  electric  vehicles  or  not.  This  could  be 
particularly useful for estimating the increasing prevalence of electric 
vehicles and their significant effect on building energy loads. Finally, to 
enhance  the  method’s  generalizability  and  applicability  across  other 
countries/climate zones, it could be beneficial to reevaluate the existing 
features,  incorporate  additional  relevant  features,  and  add  additional 
data from various countries and climate zones to the training data set. 
Additional relevant features include pattern/shape based features, and 
possibly  model  based  features  [42].  Further,  the  method  could  be 
extended to predict the energy efficiency class of the buildings.

5. Conclusion

This  article  has  introduced  82  domain-specific  features  and  a  su-
pervised  automatic  building  category  classification  approach  for  pre-
dicting the building category and heating type of Norwegian buildings 
from  their  electricity  load  profiles  with  high  accuracy.  While  prior 
research has predominantly focused on unsupervised methods for clas-
sifying electricity consumers, the proposed approach has been tailored 
to label building load profiles according to Norwegian building regula-
tions (TEK17) standard building categories, making it a more practical 
categorization which is useful for grid and area planning. The method 
was  developed  and  tested  on  a  large  and  original  dataset  of  2740 
buildings across 10 building categories, including both residential and 
non-residential buildings, and achieved an accuracy of 84 % in identi-
fying  correct  building  and  heating  categories  on  the  testing  set. 
Furthermore, the proposed classification method demonstrates excellent 
generalizability and transferability when applied to unseen electricity 
data from Norwegian apartments. However, testing on buildings from 
other  climate  zones  showed  less  transferability,  indicating  a  need  for 
more features tailored to different climate zones and locations.

CRediT authorship contribution statement

Synne Krekling Lien: Writing – review & editing, Writing – original 
draft,  Validation,  Methodology,  Data  curation,  Conceptualization. 
Jayaprakash Rajasekharan: Writing – review & editing, Supervision, 
Project administration.

Declaration of competing interest

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

Acknowledgment

This  article  has  been  written  within  the  research  project  “Coinci-
dence factors and peak loads of buildings in the Norwegian low carbon 
society” (COFACTOR). The authors gratefully acknowledge the support 
from  the  Research  Council  of  Norway  (project  number  326891), 
research partners, industry partners and data providers.

Data availability

Parts of the data is openly available, while other parts will be made 
avilable at a later time. Readers may request access to anonymized data 
from the authors.

References

[1] IEA, «https://www.iea.org/reports/buildings».
[2] Energy Transitions Commission, «Making Mission Possible», Health Progress, bd.

76, nr. 6, s. 45–7, 60, 2020.

12

[3] NVE, «NVE.no: Smarte strømmålere (AMS)». [Online]. Tilgjengelig på: https:// 
www.nve.no/reguleringsmyndigheten/kunde/strom/stromkunde/smarte- 
stroemmaalere-ams/.

[4] The Norwegian Water Resources and Energy Directorate (NVE) og The Norwegian

Building Authority (DiBK), «Underlag for langsiktig strategi for 
energieffektivisering ved renovering av bygninger [Foundation for the long term 
strategy for energy efficiency by renovation of building]», mar. 2022.

[5] Direktoratet for byggkvalitet (DiBK) og Norges vassdrags- og energidirektorat

(NVE), «Underlag for langsiktig strategi for energieffektivisering ved renoverng av 
bygninger. Utredning for Kommunal- og distriktsdepartementet og Olje- og 
energidepartementet», jun. 2022.

[6] L. Ødegården og S. Bhantana, Status og prognoser for kraftsystemet 2018 rapportnr. 
103-2018. NVE, 2018. Åpnet: 31. mai 2023. [Online]. Tilgjengelig på: http:// 
publikasjoner.nve.no/rapport/2018/rapport2018_103.pdf.

[7] J. Kwac, J. Flora, og R. Rajagopal, «Household Energy Consumption Segmentation 
Using Hourly Data», IEEE Transactions on Smart Grid, bd. 5, nr. 1, s. 420–430, jan. 
2014, doi: 10.1109/TSG.2013.2278477.

[8] A. Rajabi, A pattern recognition methodology for analyzing residential customers 
load data and targeting demand response applications, Energy Build. 203 (2019), 
https://doi.org/10.1016/j.enbuild.2019.109455 s. 109455.

[9] N. Mahmoudi-Kohan, M. P. Moghaddam, M. K. Sheikh-El-Eslami, og E. Shayesteh, 
«A three-stage strategy for optimal price offering by a retailer based on clustering 
techniques», Int. J. Electr. Power Energy Syst., bd. 32, nr. 10, s. 1135–1142, des. 
2010, doi: 10.1016/j.ijepes.2010.06.011.

[10] I. Prahastono, D. King, og C. S. Ozveren, «A review of Electricity Load Profile 
Classification methods», i 2007 42nd International Universities Power Engineering 
Conference, sep. 2007, s. 1187–1191. doi: 10.1109/UPEC.2007.4469120.
[11] M. Bourdeau, Classification of daily electric load profiles of non-residential 
buildings, Energy and Buildings 233 (2021), https://doi.org/10.1016/j. 
enbuild.2020.110670, 110670.

[12] K. R. Shahapure og C. Nicholas, «Cluster Quality Analysis Using Silhouette Score», i 
2020 IEEE 7th International Conference on Data Science and Advanced Analytics 
(DSAA), okt. 2020, s. 747–748. doi: 10.1109/DSAA49011.2020.00096.

[13] J.-C. Lamirel, N. Dugu´e, og P. Cuxac, «New efficient clustering quality indexes», i 
2016 International Joint Conference on Neural Networks (IJCNN), jul. 2016, s. 
3649–3657. doi: 10.1109/IJCNN.2016.7727669.

[14] I.P. Panapakidis, T.A. Papadopoulos, G.C. Christoforidis, G.K. Papagiannis, Pattern 
recognition algorithms for electricity load curve analysis of buildings, Energy 
Build. 73 (2014) 137–145, https://doi.org/10.1016/j.enbuild.2014.01.002.
[15] T. Zhang, G. Zhang, J. Lu, X. Feng, og W. Yang, «A New Index and Classification 
Approach for Load Pattern Analysis of Large Electricity Customers», IEEE 
Transactions on Power Systems, bd. 27, nr. 1, s. 153–160, feb. 2012, doi: 10.1109/ 
TPWRS.2011.2167524.

[16] Direktoratet for byggkvalitet, Byggteknisk forskrift (TEK17). 2017. Åpnet: 19.

oktober 2021. [Online]. Tilgjengelig på: https://dibk.no/regelverk/byggteknisk- 
forskrift-tek17/.

[17] SN/TS 3031:2016, «Bygningers energiytelse - Beregning av energibehov og

energiforsyning / Energy performance of buildings - Calculation of energy needs 
and energy supply». Standard Norge, 2016. Åpnet: 29. oktober 2021. [Online]. 
Tilgjengelig på: https://www.standard.no/no/Nettbutikk/produktkatalogen/ 
Produktpresentasjon/?ProductID=859500.

[18] Z. Dong, J. Liu, B. Liu, K. Li, X. Li, Hourly energy consumption prediction of an 
office building based on ensemble learning and energy consumption pattern 
classification, Energy Build. 241 (2021), https://doi.org/10.1016/j. 
enbuild.2021.110929, 110929.

[19] T. Tsoka, X. Ye, Y. Chen, D. Gong, X. Xia, Explainable artificial intelligence for

building energy performance certificate labelling classification, J. Clean. Product. 
355 (2022), https://doi.org/10.1016/j.jclepro.2022.131626, 131626.

[20] M.S. Piscitelli, S. Brandi, A. Capozzoli, ecognition and classification of typical load 
profiles in buildings with non-intrusive learning approach, 113727, Appl. Energy 
255 (2019), https://doi.org/10.1016/j.apenergy.2019.113727.

[21] A. Canaydin, C. Fu, A. Balint, M. Khalil, C. Miller, H. Kazmi, Interpretable domain- 
informed and domain-agnostic features for supervised and unsupervised learning 
on building energy demand data, Appl. Energy 360 (2024), https://doi.org/ 
10.1016/j.apenergy.2024.122741, 122741.

[22] M. Sodenkamp, I. Kozlovskiy, T. Staake, Supervised classification with

interdependent variables to support targeted energy efficiency measures in the 
residential sector, Decision Anal. 3 (1) (2016) 1, https://doi.org/10.1186/s40165- 
015-0018-2.

[23] P. Carroll, T. Murphy, M. Hanley, D. Dempsey, J. Dunne, Household classification 
using smart meter data, J. off. Statistics 34 (1) (2018) 1–25, https://doi.org/ 
10.1515/jos-2018-0001.

[24] K. B. Lindberg, «Impact of Zero Energy Buildings on the Power System», s. 192.
[25] K. Heimar Andersen, S. Krekling Lien, K. Byskov Lindberg, H. Taxt Walnum, og I. 
Sartori, «Further development and validation of the ‘PROFet’ energy demand load 
profiles estimator», presentert på 2021 Building Simulation Conference, sep. 2021. 
doi: 10.26868/25222708.2021.30159.

[26] S. K. Lien, H. T. Walnum, og Å. L. Sørensen, «COFACTOR Drammen dataset. 4 years 
of hourly energy use data from 45 public buildings in Drammen, Norway», 
Submitted to: Scientific Data, mai 2024.

[27] S. K. Lien, D. Ivanko, og I. Sartori, Domestic hot water decomposition from measured 
total heat load in Norwegian buildings. SINTEF Academic Press, 2020. Åpnet: 3. juli 
2023. [Online]. Tilgjengelig på: https://ntnuopen.ntnu.no/ntnu-xmlui/handle/ 
11250/2684373.

---

<!-- PAGE 13 -->

S.K. Lien and J. Rajasekharan

Energy & Buildings 325 (2024) 114954

[28] K. B. Lindberg, S. J. Bakker, og I. Sartori, «Modelling electric and heat load profiles 
of non-residential buildings for use in long-term aggregate load forecasts», Utilities 
Policy, bd. 58, s. 63–88, jun. 2019, doi: 10.1016/j.jup.2019.03.004.

[29] Standard Norge, «SN-NSPEK 3031:2020 Bygningers energiytelse — Beregning av

energibehov og energiforsyning».

[30] F. Pedregosa, Scikit-learn: machine learning in python, J. Machine Learning Res.

12 (85) (2011) 2825–2830.

[31] J. Fürnkranz, «Decision Tree», i Encyclopedia of Machine Learning, C. Sammut og G.

I. Webb, Red., Boston, MA: Springer US, 2010, s. 263–267. doi: 10.1007/978-0- 
387-30164-8_204.

[32] L. Breiman, «Random Forests», Machine Learning, bd. 45, nr. 1, s. 5–32, okt. 2001,

doi: 10.1023/A:1010933404324.

[33] X. Zhang, «Support Vector Machines», i Encyclopedia of Machine Learning, C.

Sammut og G. I. Webb, Red., Boston, MA: Springer US, 2010, s. 941–946. doi: 
10.1007/978-0-387-30164-8_804.

[34] «sklearn.ensemble.GradientBoostingClassifier», scikit-learn. Åpnet: 29. februar 
2024. [Online]. Tilgjengelig på: https://scikit-learn/stable/modules/generated/ 
sklearn.ensemble.GradientBoostingClassifier.html.

[35] G. Brown, «Ensemble Learning», i Encyclopedia of Machine Learning, C. Sammut og 
G. I. Webb, Red., Boston, MA: Springer US, 2010, s. 312–320. doi: 10.1007/978-0- 
387-30164-8_252.

[36] J. T. Hancock og T. M. Khoshgoftaar, «CatBoost for big data: an interdisciplinary 
review», Journal of Big Data, bd. 7, nr. 1, s. 94, nov. 2020, doi: 10.1186/s40537- 
020-00369-8.

[37] X. Jin og J. Han, «K-Means Clustering», i Encyclopedia of Machine Learning and Data 
Mining, C. Sammut og G. I. Webb, Red., Boston, MA: Springer US, 2017, s. 695–697. 
doi: 10.1007/978-1-4899-7687-1_431.

[38] Z.-H. Zhou, «Ensemble Learning», i Encyclopedia of Biometrics, S. Z. Li og A. Jain, 
Red., Boston, MA: Springer US, 2009, s. 270–273. doi: 10.1007/978-0-387-73003- 
5_293.

[39] M. Hofmann og T. Siebenbrunner, «A rich dataset of hourly residential electricity 
consumption data and survey answers from the iFlex dynamic pricing experiment», 
Data in Brief, bd. 50, s. 109571, okt. 2023, doi: 10.1016/j.dib.2023.109571.
[40] S. Makonin, «HUE: The Hourly Usage of Energy Dataset for Buildings in British 
Columbia». Harvard Dataverse, 4. september 2018. doi: 10.7910/DVN/N3HGRN.
[41] C. Miller mfl., «The Building Data Genome Project 2, energy meter data from the 
ASHRAE Great Energy Predictor III competition», Sci Data, bd. 7, nr. 1, Art. nr. 1, 
okt. 2020, doi: 10.1038/s41597-020-00712-x.

[42] C. Miller, «What’s in the box?! Towards explainable machine learning applied to 
non-residential building smart meter classification», Energy and Buildings, bd. 199, 
s. 523–536, sep. 2019, doi: 10.1016/j.enbuild.2019.07.019.

[43] M. Quintana, P. Arjunan, og C. Miller, «Islands of misfit buildings: Detecting

uncharacteristic electricity use behavior using load shape clustering», Build. Simul., 
bd. 14, nr. 1, s. 119–130, feb. 2021, doi: 10.1007/s12273-020-0626-1.

13

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Energy & Buildings 325 (2024) 114954
Contents lists available at ScienceDirect
&
Energy Buildings
journal homepage: www.elsevier.com/locate/enb
Automatic standard building category classification from smart meter data
– A supervised learning approach
Synne Krekling Liena,b,*, Jayaprakash Rajasekharana
aNorwegian University of Science and Technology (NTNU), Department for Electric Energy, NO-7491 Trondheim, Norway
bSINTEF Community Oslo, Pb 124 Blindern, 0314 Oslo, Norway
A R T I C L E I N F O A B S T R A C T
Keywords: Increased availability of smart meter data offers better insight into buildings’ electricity usage. By classifying
Buildings smart meter data by building type and presence of heating appliances, we can efficiently gain metadata about the
Energy buildings that is useful for research, grid planning, and energy efficiency policy employment. However, current
Electricity
smart meter classification approaches are largely based on limited datasets and building classes, or on unsu-
Measurements
pervised methods that don’t align with standard building categories and offer limited control over grouping. This
Classification
Machine learning article presents a supervised automatic building category classification approach for labelling smart meter data
Building category from buildings into standard building categories in the Norwegian building regulations (TEK17), and whether
they have electric heating or not. 82 novel physics-based domain features are presented which can be extracted
from any hourly electricity smart meter data series from buildings with a duration of months-years. The features
are specifically designed to identify the building and heating type of a smart meter data series by capturing
patterns such as seasonality, daily usage trends, similarities with standardized building load profiles, temperature
dependency, and other domain-specific characteristics. The classification approach is trained and tested on a
large dataset of 2724 buildings from 12 different building categories, both residential and non-residential, and
correctly identifies the heating type and building category of unseen Norwegian smart meter data from buildings
in 84 % of the test cases. The approach is generalizable to meter data from other Norwegian buildings and is also
tested on buildings from other climate zones. The proposed method for smart meter data classification is proven
to have high accuracy and applicability for extracting metadata for both residential and non-residential buildings
in Norway.
1. Introduction electricity usage and transmit data to grid companies, and can, if ana-
lysed, provide more information about electricity use patterns for
In 2021, the operation of buildings was responsible for 30 % of final different electricity consumers. The use of electrical heating appliances
global energy consumption and 27 % of total energy sector emissions is widespread in Norway due to historically low electricity prices [4]. It
(out of which 8 % is related to direct emissions from buildings, while 19 is estimated that electricity for heating makes up more than 60 % of the
% refers to emissions from generation of heat and electricity consumed total electricity consumption in Norwegian buildings [5]. The use of
by buildings) [1]. The electrification of buildings has been identified as a electricity for heating hence contributes to high peaks in the electricity
key alternative to achieve a more sustainable energy system and miti- grid during the colder winter days [6]. Buildings with electrical heating
gate the corresponding emission of gases that result in climate change hence typically have a stronger strain on the electricity grid compared to
[2]. To tackle these challenges, more knowledge about building energy buildings with non-electric heating. To address the challenges of
use is needed. Due to recent roll-out of smart grid infrastructures and increased electricity demand in the grid, and to utilize the availability of
advanced digital metering systems, building energy data has become more electricity data from buildings, the implementation of classifica-
more available. Norway mandated the installation of smart electricity tion methods for electricity measurements becomes valuable. By clas-
meters for all electricity consumers as part of advanced metering sys- sifying smart meter data by building type, we can efficiently gain
tems (AMS) by 2020 [3]. These meters record customers’ hourly metadata about the buildings that is useful for research, grid planning,
* Corresponding author.
E-mail address: synne.k.lien@ntnu.no(S.K. Lien).
https://doi.org/10.1016/j.enbuild.2024.114954
Received 15 August 2024; Received in revised form 9 October 2024; Accepted 22 October 2024
Available online 26 October 2024
0378-7788/© 2024 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
and energy efficiency. Unsupervised methods have been applied in consumption into one of four predefined patterns, representing weekend
various ways to classify smart meter data, as demonstrated in [7]and use, night use, and weekday use during summer/winter. Supervised
[8], where clustering techniques were used to group households based classification has also been used to classify the energy performance of
on their demand response potential, and in [9]and [10]which looked at 2717 commercial buildings in Hong Kong from meta data and measured
grouping of buildings into distinct consumer classes to design tailored energy use when their size were unknown, achieving an accuracy of
tariffs aimed at reducing grid strain. Other examples include [11]which 78.8 % with random forest. This approach did however rely on meta
investigated K-means clustering applied to clustering of 14 non- data as input features which are usually not available within smart
residential buildings on a university campus (of types office/library/ meter databases or in publicly available statistics elsewhere. Similarly,
teaching) and clustered into two different consumer groups. The effec- [19] demonstrated a classification model based on artificial neural
tiveness of unsupervised methods/clustering relies on multiple factors network for classifying energy performance certificated of Italian
and can be measured by diverse indicators to assess how well the clus- buildings. The input features of this classification were mostly meta data
ters represents the data, including the silhouette score [12], Davis present in the buildings’ EPCs, like U-values, area, degree days and
Bouldin index and the Dunn index [13]. While these indicators can tell volume etc, and the only measured input value was CO2-emissions from
us how well the buildings within each group fit together, unsupervised the buildings. The model showed to receive up to 99 % accuracy
clustering techniques may group together buildings have several simi- depending on included features but could only achieve an accuracy of
larities but serve different purposes. Another challenge with unsuper- 75 % without measured/calculated data of energy use or CO2-use,
vised methods is that the number of optimal clusters is generally not which is directly linked to the EPC of the building.
known. There are numerous methods for estimating the optimal number There are a few examples where meta data from buildings has been
of clusters but depending on the problem, unsupervised methods may extracted from smart meter data using supervised classification. One
not be the most suitable for assigning a class to a building load profile. supervised classification of building categories used a semi-supervised
The classification of buildings’ smart meter data has historically been approach to group 3 months data from 114 non-residential buildings
considered an unsupervised machine learning task [14,15]due to both into 17 different building typologies using a follow-the-leader clustering
the lack of properly labelled smart meter data and the challenge of approach and achieved an accuracy of 80 % [20]. In another example, a
determining the correct or optimal number of clusters. However, un- supervised learning approach with domain-informed and domain-
supervised methods are not necessarily the best approach when aiming agnostic features were used to estimate the country of buildings from
to classify buildings into set, pre-defined building categories. In Norway 4 different countries [21]. Supervised learning was used in two studies
standardized building category groups are used in the Norwegian with several thousand smart meters from Ireland to extract metadata
building code TEK–17 [16], and in the standard for energy calculations about the households such as heating type, floor area, age and number of
of buildings in Norway [17]and divide buildings/part of buildings into inhabitants. 48 (number of bedrooms, 4 classes) – 84 % (single/not
13 main categories (“small house”, “apartment”, “school”, “office”, single occupant) accuracy dependent-independent data classification
“nursing home”, etc.). Each category has specific energy efficiency re- (DID) and probabilistic regression [22], and in [23] to estimate the
quirements, making it essential to understand the composition of these household size class (number of adults and children) of the Irish
categories within an area for effective grid and energy planning. Clas- dwellings. The latter did however show that that the smart meter data
sifying buildings’ smart meter data into these standardized categories alone was limited to distinguish the household category and achieved a
can provide a more accurate and practical categorization of buildings. low accuracy. To the best of the authors knowledge, there exist no
For instance, while schools and kindergartens may exhibit similar en- method or application for classifying the standard building category and
ergy consumption patterns, a notable distinction arises in the heating heating type of buildings from their smart meter data, and there is
systems employed in these building categories. Kindergartens often have limited research on supervised classification of smart meter data for
point source heating, while schools often utilize water-borne heating extraction of building meta data in datasets containing both residential
systems, providing them with greater flexibility to alter heating sources and non-residential buildings.
and control strategies. Likewise, a nursing home might have similar
energy consumption profiles as an apartment building, yet an important
difference between these types of buildings are the ownership struc- 1.1. Contributions
tures. Publicly owned buildings may be in a different economical posi-
tion compared to privately owned residential properties, and The primary research problem addressed in this article is how to
policymakers wield more influence in enforcing legislation and re- collect metadata for buildings’ smart meter data when it is not readily
furbishments in the former. Cabins equipped with electrical heating may available, specifically their building category and heating type. Col-
have similar technical systems compared with single family houses, but lecting information about buildings is a difficult and time-consuming
their geographical location introduces unique considerations. Situated task that typically requires manual effort. To address this, there is a
in areas with limited grid capacity and sparse occupancy on most days, need for a method that is generalizable to smart meter data of different
areas with many cabins may experience a pronounced coincidence durations, without relying on additional metadata, that can be applied
factor during holidays when numerous consumers are present. These to buildings of varying locations, types, sizes, ages, and energy perfor-
differences may not be captured when using unsupervised clustering mance levels.”
algorithms, and the clusters generated with unsupervised clustering al- This article introduces a novel supervised classification method for
gorithms may be capturing unintended attributes about building electric segmenting smart meter data from buildings into standardized cate-
load patterns than anticipated. Supervised classification methods pro- gories. While the true number of classes is considered unknown in most
vide an alternative to clustering that offers more control of the assign- classification approaches of smart meter data, this approach uses the
ment of labels to building load profiles. While supervised classification is standard building categories from the Norwegian building regulations as
widely used in many classification tasks, only a few supervised classi- labels to develop a model that can differentiate between different
fication of electricity load profiles from buildings have been demon- building categories, including both residential and non-residential
strated in research for deriving the building class and meta data about buildings. In short, the contributions of this paper are:
buildings, likely since supervised learning techniques require a large
amount of labelled data for training, validation, and testing with clear - A supervised classification approach for segmenting smart meter
segmentation. One example where supervised classification has been data from buildings into standardized building categories, including
used on smart meter data is for prediction building energy consumption, both residential and non-residential buildings as well as their heating
such as in [18]for an office building in New York to categorize energy class (electric and non-electric).
2

S.K. Lien and J. Rajasekharan                                                                                                                                                                                  E  n e  r g  y   &     B  u  i ld  i n  g s    3 25 (2024) 114954
| - The classification approach is trained and tested on a large and novel  | Table 1  |     |     |     |
| ------------------------------------------------------------------------- | -------- | --- | --- | --- |
dataset of hourly data from more than 2700 Norwegian buildings  Building type labels and the number of buildings in the dataset.
from 11 building categories (including 4 residential categories and 7
|     |     | Building  | Building  Heating  | Building  Number  |
| --- | --- | --------- | ------------------ | ----------------- |
non-residential categories). To the best of the authors knowledge,  category in  category  type  type label of
|     |     | TEK17 | label (Electric  | buildings |
| --- | --- | ----- | ---------------- | --------- |
there are no other building category classification approaches in
Heating
research based on a dataset on this scale, and most approaches found
(EH)/ non-
in the literature are focused on either residential or non-residential
electric
| buildings separately. |     |     | heating  |     |
| --------------------- | --- | --- | -------- | --- |
- For the classification, 82 physics-based domain features are extrac- (NEH))
ted from each of the smart meter time series from the buildings. The
|     | Labels for  | House | Hou NEH | Hou_NEH 67 |
| --- | ----------- | ----- | ------- | ---------- |
features can be extracted from any hourly electricity smart meter  building  EH Hou_EH 473
data series from buildings with a duration of months-years. category  Apartment Apt NEH Apt_NEH 1344
- A comparison between the proposed supervised method and an un- and type  EH Apt_EH 400
supervised classification of the smart meter data using K-means  (not  Apartment  Apb NEH Apb_EH 53
|     | present  | blocks* | EH  | Apb_NEH 51 |
| --- | -------- | ------- | --- | ---------- |
clustering is presented, showing how a supervised approach is more  in  Cabin/  Cab NEH Cab_NEH 0
suited for classifying buildings into their standardized building  dataset  Holiday  EH Cab_EH 128
|     | in grey) | house |     |     |
| --- | -------- | ----- | --- | --- |
categories.
|     |     | Office | Off NEH | Off_NEH 54 |
| --- | --- | ------ | ------- | ---------- |
- The method is generalizable to other Norwegian buildings outside
|     |     |     | EH  | Off_EH 7 |
| --- | --- | --- | --- | -------- |
the dataset and is in addition tested against external, openly avail-
|     |     | Nursing  | Nsh NEH | Nsh_NEH 21 |
| --- | --- | -------- | ------- | ---------- |
able datasets of electricity consumption in buildings from other lo- home EH Nsh_EH 6
cations and climate zones and compared the model results from the  Hotel Htl NEH Htl_NEH 7
suggested approach against unsupervised methods for building  EH Htl_EH 0
|     |     | Kindergarten | Kdg NEH | Kdg_NEH 11 |
| --- | --- | ------------ | ------- | ---------- |
category classification.
|                |     |        | EH      | Kdg_EH 20  |
| -------------- | --- | ------ | ------- | ---------- |
|                |     | School | Sch NEH | Sch_NEH 32 |
| 2. Methodology |     |        | EH      | Sch_EH 16  |
|                |     | Shop   | Shp NEH | Shp_NEH 28 |
This article presents a method to classify buildings’ AMS-data into a  EH Shp_EH 0
|     |     | Hospital | Hsp NEH | Hsp_NEH 6 |
| --- | --- | -------- | ------- | --------- |
building category and heating type (electric/non-electric). This section  EH Hsp_EH 0
describes the dataset used to develop and test this method, the labels of  Culture Cul NEH Cul_NEH 0
the buildings in the dataset, the physics-based domain features extracted  EH Cul_EH 0
for each building, and different models tested for the classification  Sport Spo NEH Spo_NEH 0
|     |     |     | EH  | Spo_EH 0 |
| --- | --- | --- | --- | -------- |
problem.
|     |     | University | Uni NEH | Uni_NEH 0 |
| --- | --- | ---------- | ------- | --------- |
|     |     |            | EH      | Uni_EH 0  |
2.1. Dataset and labels *In the database and in the Norwegian building codes  Total 2724
TEK17, apartments (section within an apartment block)
and apartment blocks are both labelled the same. In this
To develop and test the classification method, a large data set con-
dataset, these are separated into apartments and
taining files with several years of hourly electricity and outdoor tem- apartment blocks.
perature measurements from 2724 buildings located in Norway is used.
The dataset consists of both openly available data and classified data
make the building time series data comparable. By focusing on key
provided by Drammen Municipality, FME ZEB [24], FME ZEN [25],
Elvia, Statkraft, Risvollan Housing Association, Sikom, Statsbygg, and  features such as average energy consumption, seasonal variations, and
other project partners. More information about the file structure of the  usage patterns, we can reduce the bias in the dataset caused by differ-
building files is described in [26]. Every building in the data set is  ences in e.g. durations and improve the accuracy of predictions. This
labelled with a building category (cid:0) describing the primary use of the  approach ensures that the classification model compares similar features
building (cid:0) which are the standardized building categories used in the  across different datasets and reduce the data quantity and the running
Norwegian building code TEK-17 [16], and in the standard for energy  time. Here, 82 physics-based domain features are generated for each
building from its electricity load and temperature time series. The fea-
calculations of buildings in Norway [17]. Each building is also labelled
tures are categorized into 5 feature groups:
with a heating type (describing whether the building has electric/non-
electric space heating) and with a resulting building type (combination
- Non-normalized electricity load features.
of the building category and heating type). A summary of the labels and the
- Electricity load variation features.
support within each building type is given in Table 1.
- Seasonal differences features.
| 2.2. Feature generation | - Average daily profile features. |     |     |     |
| ----------------------- | --------------------------------- | --- | --- | --- |
- Standard load profile correlation features.
Smart meter data collected from different sources will often have
varying start dates, end dates, seasons, and durations. These discrep- A list of all features within each group is given in the following sub
chapters.
ancies in time series data can lead to inaccurate predictions, as it may
result in comparing apples to oranges. One can consider a scenario
2.2.1. Non-normalized electricity load features
where image recognition is used to differentiate between schools and
Four features describe the non-normalized data of the buildings’
apartment blocks based on their smart meter data. If all school buildings,
electricity load. These features capture the size of the peak load, and
except one, have data spanning four years, while all apartment blocks
mean electricity use and the relationship between the electricity load
have data covering only one year, the single school with only one year of
data might be incorrectly classified due to the difference in data dura- and outdoor temperature. These features extract information about the
tion. To address this issue, feature extraction can be employed. Feature  size of the building (which is important to gain information about the
extraction involves identifying and extracting relevant patterns and  building type) and the temperature dependency of the load. The last two
characteristics from the smart meter data, which can then be used to  features look at the relationship between the electricity use and the
3

S.K. Lien and J. Rajasekharan                                                                                                                                                                                  E  n e  r g  y   &     B  u  i ld  i n  g s    3 25 (2024) 114954
| outdoor temperature. The first is the outdoor temperature at the peak  |     | Table 3  |     |     |
| ---------------------------------------------------------------------- | --- | -------- | --- | --- |
electricity load, and the second is the imported electricity at the mini- Electricity load variation features.
mum outdoor temperature. A summary of the Non-normalized elec-
|     |     | Feature notation | Description | Subset of data |
| --- | --- | ---------------- | ----------- | -------------- |
tricity load features are given in Table 2.
|     |     | ElImp_max | The actual peak load of the  | All data, winter, spring,  |
| --- | --- | --------- | ---------------------------- | -------------------------- |
|     |     |           | imported electricity load    | summer, autumn, Weekdays,  |
2.2.2. Electricity load variation features profile of the building Weekends, the outdoor
The 32 electricity load variation features are normalized electricity  ElImp_mean The mean value of the  temperature is below 10C
load features that look at peak load (max), average load, the relationship  imported electricity load
profile of the building
between them, and the hour of the day when peak load occurs for
|     |     | ElImp_max_vs_mean | The maximum peak load  |     |
| --- | --- | ----------------- | ---------------------- | --- |
different subsets of the data – for example, during the wintertime,
divided by the mean of the
summertime, or for the entire dataset. The subsets are chosen to examine  peak load profile of the
season and temperature dependent variations. The winter season is  building.
defined as December-February, spring as March-May, summer as June-  ElImp_max_hour The hour of day when the
August and autumn from September-November.The electricithy load  peak load occurs.
vatriation features are summarized in Table 3.
Table 4
2.2.3. Seasonal differences features
Seasonal differences features.
Seasonal variation and temperature dependency can provide an
indication of whether the building uses electricity for space/ventilation  Feature notation Description
heating. To further capture such effects, 6 seasonal differences features  ElImp_max_vs_summer_max The maximum peak load divided by the
are added. They are intended to complement the electricity load varia- peak load during the summer
tion features and to specifically investigate the relationship between the  ElImp_mean_vs_summer_mean The mean electricity load divided by the
mean peak load during the summer
summer and winter features as these are the most important features to
|     |     | ElImp_winter_mean_vs_summer_mean |     | The mean electricity load during winter  |
| --- | --- | -------------------------------- | --- | ---------------------------------------- |
evaluate whether a building has electric heating or not. These features
divided by the mean electricity load during
examine the differences in the mean and max in summer and winter. The
summer
|     |     | ElImp_max_vs_winter_max |     | The peak load divided by the peak load  |
| --- | --- | ----------------------- | --- | --------------------------------------- |
seasonal differences features are summarized in Table 4.
during the winter
|     |     | ElImp_mean_vs_winter_mean |     | The mean electricity load divided by the  |
| --- | --- | ------------------------- | --- | ----------------------------------------- |
2.2.4. Average daily profile features (normalized data) mean electricity load during the winter
The 16 “Average daily profile features” are features which are  ElImp_winter_max_vs_summer_max The peak load during the winter divided by
generated to extract traits from the daily load profile are given in  the peak load during the summer.
Table 5,These features represent specific patterns that explain user
behaviour and variations throughout a day that can indicate the type of
building from its electricity load profile. The features are selected to
Table 5
capture the most important elements that can indicate the building  Average daily profile features.
category based on domain knowledge. These features provide a stronger
|     |     | Feature notation |     | Description |
| --- | --- | ---------------- | --- | ----------- |
insight compared to just giving the daily load profile values (Fig. 1).
|     |     | daily_average_profile_max |     | A. Maximum value during the average  |
| --- | --- | ------------------------- | --- | ------------------------------------ |
day.
2.2.5. Standard load profile correlation features (normalized data) daily_average_profile_max_hour B. Hour when maximum value (A) occurs
To capture the similarities between the daily user patterns in build- daily_average_profile_min C. Minimum value during the average
ings and the user patterns of similar building types, 24 standard load  day.
|     |     | daily_average_profile_min_hour |     | D. Hour when minimum value (C) occurs |
| --- | --- | ------------------------------ | --- | ------------------------------------- |
profile correlation features are extracted as shown in Table 6. The
|     |     | daily_average_max_over_min |     | Maximum divided by minimum value (A/  |
| --- | --- | -------------------------- | --- | ------------------------------------- |
standard load profile correlation features describe the extent of corre-
C)
lation of daily load profile of each building with standard load profiles of
|     |     | daily_average_median |     | E. Median value of the daily load profile. |
| --- | --- | -------------------- | --- | ------------------------------------------ |
different building types. The standard load profiles are generated using  daily_average_profile_max_after The value at the hour after the maximum
the PROFet model [25]. PROFet is an aggregated load profile generator  value (value at B +1)
which can predict hourly load profiles for both thermal loads and  daily_average_profile_max_before The value at the hour before the minimum
value (value at B-1)
electric loads, based solely on outdoor temperatures and building area.  daily_average_std Standard deviation of the daily average
PROFet is based on panel regression of energy measurements of build- profile
ings from trEASURE, a database, of monitored buildings, mostly con- daily_average_var Variation of the standard profile
|     |     | daily_average_profile_second_max |     | F. The second highest hourly value during  |
| --- | --- | -------------------------------- | --- | ------------------------------------------ |
nected to district heating. PROFet can estimate the typical load profile of
the average day.
an area based solely on building area input (for 12 building categories
|     |     | daily_average_profile_second_max_hour |     | G. The hour when the second highest  |
| --- | --- | ------------------------------------- | --- | ------------------------------------ |
and 3 energy efficiency levels as described in the categorization) and  value occurs.
outdoor temperatures [25,27,28]. PROFet has been used to create  daily_average_profile_max_change F. The hour when the change is biggest
standard load profiles for 11 building categories (all building categories  (positive) from the past hour to the
current hour.
|          |     | daily_average_profile_max_change_hour |     | G. The hour after the biggest (positive)  |
| -------- | --- | ------------------------------------- | --- | ----------------------------------------- |
| Table 2  |     |                                       |     | change during the day.                    |
Non-normalized electricity load features. daily_average_profile_min_change H. The highest negative change during the
average day from the past hour to the
| Feature notation  | Description                                             |                                       |     | current hour.                           |
| ----------------- | ------------------------------------------------------- | ------------------------------------- | --- | --------------------------------------- |
|                   |                                                         | daily_average_profile_min_change_hour |     | I. The hour after the largest negative  |
| ElImp_actual_max  | The actual (non-normalized) peak load of the imported   |                                       |     |                                         |
|                   | electricity load profile of the building                |                                       |     | occurs.                                 |
| ElImp_actual_mean | The actual (non-normalized) mean value of the imported  |                                       |     |                                         |
electricity load profile of the building
in Table 1, excluding cabins, industry and cultural buildings) using a
| Tout_at_ElImp_max | The outdoor temperature when the electricity peak load  |     |     |     |
| ----------------- | ------------------------------------------------------- | --- | --- | --- |
occurs. standard weather profile from Norwegian Standards NS3031 [29]. To
ElImp_at_Tout_min The electricity load when the minimum outdoor temperature  create standard profiles that represent the average energy efficiency
occurs. standard of the building stock, it is assumed that the buildings are 82 %
4

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
to differences in the outdoor temperatures throughout the year. Resi-
dential buildings typically have a small peak in the morning and a higher
peak in the evening, while service buildings have a peak during the day.
The rise in energy consumption in the mornings typically starts earlier in
buildings with electric heating compared to buildings without electric
heating due to the time needed to heat buildings in the morning, and due
to the electricity need for hot water in residential buildings. Standard
load profile features are calculated as the correlation between each of
the standard daily load profiles and the average daily load profile of the
building. There is one feature for the correlation between the building
and each of the available load profiles.
2.3. Classification models
For the classification task of assigning building category and building
type labels to previously unseen electricity time series data from
buildings, a selection of machine learning classifiers were explored
Fig. 1. The average daily load profile of a building and indication of where the utilizing the Scikit Learn library in Python version 1.3.0 [30]. The tested
features in Table 5are collected from the daily profile. classifiers include the following with default parameters: Decision Tree
Classifier [31], RandomForest Classifier [32]., Support Vector Machines
Classifier [33], Gradient Boosting Classifier [34], AdaBoost Classifier
Table 6
[35]and CatBoost Classifier [36]In addition, the best performing from
Standard load profile correlation features.
this list is evaluated against Unsupervised K-means clustering [37]and
Feature notation Description Soft-voting ensemble learning [38].
correlation_daily_SLP_*_EH Correlation between the daily load profile of the
building and the standard category with electric 2.4. Training and testing
heating
correlation_daily_SLP_*_NEH Correlation between the daily load profile of the
building and the standard category without electric To train and test the classification methods, the dataset comprising
heating 2724 buildings has been randomly split with an 80/20 partition into the
*One of the following category abbreviations (see Table 1): Apt, Hsp, Hou, Htl, Kdg, training set (2179 buildings) and a test set (545 buildings).
Nsh, Off, Oth, Sch, Shp, Spo, Uni
2.5. Performance metrics
“regular” and 18 % “efficient”. To make standard load profiles for
buildings with and without electric heating, it is assumed that buildings To evaluate the performance of the different classification models, a
with electric heating has an electricity consumption equal to the total diverse set of performance metrics are employed. These metrics serve as
demand of the buildings (including electric specific demand, domestic quantitative measures to gauge various aspects of model performance,
hot water heating and space heating). It is also assumed that buildings including accuracy, accuracy when providing two possible labels, pre-
without electric heating have an electricity consumption equal to the cision, recall and F1-score. By applying these performance metrics, it is
energy demand for electric specific loads. An example of the daily possible to quantitatively get an understanding how well the models can
standard load profiles for apartments and schools with and without correctly label previously unseen data. The performance metrics are
electric heating is shown in Fig. 2. described in Table 7.
The standard load profiles are generated for one year before they are
normalized. Average hourly daily load profiles are then created. The 3. Results
average daily load profiles for some of the standard building categories
are shown below. Several patterns can be observed from these figures. 3.1. Prediction of building type
Buildings with NEH tend to have higher normalized loads during the
average day due to less variations during the year compared to buildings Different models are applied on the dataset with extracted features to
with electric heating, where there are large variations in the peaks due classify the building type (building category +heating type). Classifica-
tion of the test set has been performed based on training the models
Fig. 2. Standard daily load profile of different building categories (a) with and (b) without electric heating.
5

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
Table 7 estimation of the building category is approximately 0.89 in accuracy,
Definition and description of performance measures. precision, recall and F1-score for both models, while the top-2 accuracy
Metric Equation Description is 0.97–0.98. The performance is hence better for the classification
approach when only predicting building category and not also the
Accuracy TP+TN The share of predictions that were correct
(Acc) (32) TP+TN+FP+FN heating type. This is likely due to a combination of less complexity as
Top-2 A1(cid:0)2 The share of predictions that were correct in well as uncertainty in the labelling of the heating categories of the
accuracy TP+TN+FP+FN one of the two most likely classes. buildings.
Precision(33) TP The share of predicted positive that were
TP+FP correct.
3.3. Prediction of building type with feature selection
Recall TP The share predictions that should have been
(33) TP+FN predicted as true that were correct.
F1-
(
s
3
c
3
o
)
re 2•
p
p
r
r
e
e
c
c
.
.
+
•r
r
e
e
c
c
a
a
l
l
l
l
C
st
o
ro
m
n
b
g
i
l
n
y
a
p
ti
e
o
n
n
a
o
li
f
z e
p
s
r e
lo
ci
w
si o
p
n
re
a
c
n
is
d
io
r
n
e c
o
a
r
l l
r e
th
ca
a
l
t
l . bina
T
t
o
io
c
n
h e
o
c
f
k
f e
if
a t
t
u
h
r
e
e
r
s
e
,
a
F
r
o
e
r
m
wa
o
r
r
d
e o
S
p
e
t
q
i
u
m
e
a
n
l
t i
s
a
o
l
l u
F
t
e
io
a
n
tu
s
r
w
e
i
S
th
el e
a
c
d
ti
i
o
ff
n
e r
(
e
F
n
S
t
F
c
S
o
)
m
is
-
Example with Predicted A1(cid:0)2 =Number of cases where applied to find best performance from various subsets of 82 features. In
classification of Office Not Office the true label is in the top 2 this technique, an iterative model is built by adding one feature at a
a building as predicted labels. time, starting from an empty set of features. At each iteration, the al-
“Office”. R =number of classes. Mr =
gorithm evaluates the performance of the model with the addition of
Actual Office True False performance. metric for class r.
Positive Negative N =total number of samples. each feature and selects the one that results in the best performance
(TP) (FN) Nr =number of samples within according to accuracy. This process continues until all features are
Not False True class r. included. Fig. 6shows the evolution of the best accuracy on the test set
Office Positive Negative when the number of features included is varied from 1 to 82. The per-
(FP) (TN)
formance appears to reach an elbow when 7–12 features are included.
Table 10shows the top 9 features that are included stepwise and the
described in section II. C. on the training set. The results of the perfor- corresponding improvement in performance.
mance in correctly identifying the labels of the unseen training set are
described in Table 8 and in the confusion matrices of the test set as 3.4. Comparison with ensemble learning
shown in Fig. 3. The results show that the Random Forest Classifier and
CatBoost Classifier perform the best overall on all performance metrics. Ensemble models in classification problems involve combining
They achieve similar results, with an overall accuracy of approximately multiple individual classifiers to generate a more accurate and robust
0.84. When considering two possible labels (top 2 accuracy), these prediction than any single model could achieve alone. Common
models achieve an accuracy of 0.92, meaning there is a 92 % chance that ensemble techniques include bagging, boosting, and stacking. Ensemble
one out of the two provided categories is the correct label for the given models are widely utilized in various domains due to their ability to
load profile. They outperform each other on different metrics, but the improve classification accuracy and generalization while reducing
differences are minimal. Given this information, the Random Forest overfitting. To estimate if the classification accuracy can be improved
Classifier may be preferred over the CatBoost Classifier as it is a much through ensemble learning, an ensemble voting classifier with soft
faster algorithm, while still offering similar overall performance. The voting is investigated. Two ensemble models are tested: one which
Gradient Boosting Classifier and Decision Tree Classifier also provide combines the Random Forest and CatBoost classifiers, and one where
satisfactory results with accuracies of 0.77 and 0.81, respectively, while also Gradient Boosting is included. Ensemble models can be affected by
Support Vector Machines (SVM) classifier and AdaBoost Classifier show class imbalance in data. To investigate if this is the case for this classi-
poor performance, with accuracies of 0.60 and 0.28 respectively. Ex- fication problem, a second test is performed where the ensemble models
amination of the confusion matrices reveals a tendency for these clas- are applied on a subset of the dataset with only residential buildings. The
sifiers to disproportionately allocate unseen data labels to classes results of applying ensemble model on the entire dataset and only on
abundant in the training set, indicating a bias towards unbalanced data. residential buildings in the dataset is shown Table 11. The results show
Analysis of the confusion matrices for the Random Forest Classifier that the ensemble model has a performance lower but close to the per-
and CatBoost Classifier indicates minimal confusion between residential formance of using the Random Forest or CatBoost Classifiers alone
and commercial buildings overall. However, within these categories, (approximately 84 % on the entire dataset as shown in Table 11for both
there exists confusion among specific subcategories. the entire dataset and for the subset containing only residential build-
ings. A reason for this may be that these models associate a very high
3.2. Prediction of building category value or importance to the same set of features as shown in Fig. 4, and
combining them does not provide any advantage in improving the
In another experiment, the best performing models, Random Forest performance measures (Table 12).
Classifier and CatBoost Classifier, are tested on how well they perform in
predicting only the building category without the heating type (electric/ 3.4.1. Comparison with k-means clustering
non-electric). The results are summarized in Table 9 and the corre- K-means clustering is a popular unsupervised learning algorithm
sponding confusion matrix in Fig. 5. The overall performance on used to partition a dataset into clusters based on similarity. It works by
iteratively assigning data points to the nearest cluster centroid and then
recalculating the centroids based on the mean of the points assigned to
Table 8
each cluster. This process continues until the centroids converge or a
Performance of different models on the test set when predicting building type.
specified number of iterations is reached. In classification, the clusters
Model Acc. Acc. top Preci- Recall F1 Run
generated by k-means can represent different classes or categories
2 sion time
within the data. The elbow method and silhouette score are both tech-
Decision Tree 0.765 0.771 0.782 0.765 0.767 0.4 s niques used to help find the optimal number of clusters in k-means
Random Forest 0.844 0.925 0.827 0.844 0.832 2.8 s
clustering. The elbow method helps find the best number of clusters in k-
Gradient 0.809 0.897 0.805 0.809 0.801 179.4 s
Boosting means by looking for a bend (elbow) in the plot of cluster number vs.
SVM 0.596 0.000 0.453 0.596 0.496 0.2 s within-cluster sum of squares. The silhouette score measures how close
Ada Boost 0.281 0.325 0.492 0.281 0.180 1.9 s each point in one cluster is to points in the neighbouring clusters,
Cat Boost 0.842 0.919 0.835 0.842 0.834 121.9 s
indicating cluster quality. Higher silhouette scores and noticeable bends
6

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
Fig. 3. Confusion matrix of building type classification with different classifiers. Fig. 4shows feature importance exhibited by the CatBoost, Random Forest and
gradient boost classifiers.
in the elbow plot suggest better clustering solutions. external datasets, published by researchers outside of the project, but
The elbow method and silhouette scores were calculated for different relabelled by the authors for testing the classification methods devel-
numbers of k on the dataset with results shown in Fig. 7. The Elbow oped in this paper. The purpose of this is to investigate whether the
method suggest the number of optimal clusters for the given dataset is building categories/types and selected features are transferrable across
around 6. Fig. 8a shows how the buildings in the test set are assigned to countries and climate zones. The external datasets include the iFlex-
different clusters when 6 clusters are used. It shows that residential dataset [39]with electricity time series data from residential buildings
buildings are all grouped together, while commercial buildings are in Norway, the HUE-dataset [40] which is an hourly dataset of elec-
grouped in three other groups. Fig. 8b shows the outcome of grouping tricity use in Canadian residential buildings, and the BDG2-dataset [41]
the buildings in the dataset into 17 clusters, the same number of clusters which includes non-residential buildings in the USA and the United
as available labels in the dataset. It notably segregates various residen- Kingdom. For each external dataset the buildings were relabelled ac-
tial buildings to a greater extent compared to the solution with 6 clus- cording to the labels presented in Table 1. The same 82 features were
ters, capturing the variation in the original labels more closely. extracted from the electricity meter data for the external datasets.
However, it suggests a prioritization of certain similarities over those Different tests were conducted, where the original dataset presented in
represented by the labels. If the objective of classification is to correctly this article were used for training, and the external datasets were used
categorize buildings according to the categories used in Norwegian for testing (and training).
building codes and standards, supervised learning appears to excel in
assigning the correct labels compared to unsupervised k-means 3.5.1. Application on iFlex dataset (Norwegian households)
algorithms. The iFlex dataset consists of a year of hourly AMS-measurements
from over 2000 residential units (apartments and houses) in Norway
from 2020 to 2021 [39]. The buildings were relabelled to the same la-
3.5. Testing of model on external datasets bels used in Table 1based on survey answers from the residents. The
classification method was tested on the iFlex-dataset in two ways – first,
To investigate the generalizability and transferability of the trained using the original training set and the iFlex-dataset as the test set and
model, features and labels, the classification approach is tested on three
7

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
Fig. 4. Feature importance for Random Forest for building type classification.
is that it only contains residential buildings, where the accuracy is lower
Table 9
compared to the accuracy for the entire dataset.
Performance of CatBoost and Random Forest on the test set when predicting only
the building category.
3.5.2. Application on HUE dataset (Canadian households)
Model Accuracy Accuracy Top 2 Precision Recall F1 HUE (The Hourly Usage of Energy Dataset for Buildings in British
Random Forest 0.892 0.967 0.895 0.892 0.891 Columbia) is a dataset that comprises of hourly energy use measure-
CatBoost 0.888 0.98 0.894 0.888 0.888 ments from 28 residential buildings in Canada (26 with sufficient la-
bels). The buildings were relabelled as either “Hou” or “Apt”. The
buildings in the HUE dataset were all correctly identified as residential
buildings. The method however failed to correctly identify the correct
building type in more than half of the cases and was unable to accurately
separate between houses and apartments. When predicting only the
building category (and not the heating type) all apartments are correctly
predicted, while houses were mostly confused for being apartments as
well. The top 2 accuracy was however perfect for predicting the building
category.
3.5.3. Application on BDG2 dataset (USA and UK service buildings)
BDG2 (Buildings Data Genome 2) is a dataset with 2 years of hourly
energy measurements (gas, cooling water, steam, and electricity) from
1636 non-residential buildings/rooms located in North America/
Europe. Two tests were conducted with the BDG2-dataset. In the first
test, a selection of buildings were relabelled based on their primary
building category to the corresponding labels in Table 1. In the second
test, the BDG2-dataset was used for both training and testing and
without relabelling, but instead using the original “Primary use cate-
gory” as labels. Some buildings were excluded due to missing data or
Fig. 5. Confusion matrix for Random Forest on the test set when predicting labels.
only the building category.
4. Discussion
next, splitting the iFlex dataset into a training and testing set. Applying
the method resulted in an accuracy of 0.7 when using the original 4.1. Results for classification of building type and category
dataset for the training and iFlex-dataset for the testing. When using the
iFlex-dataset for both testing and training, the accuracy improved to This article has presented results for building type classification of
0.75. A reason for the performance not being higher for the iFlex-dataset electricity time series from buildings. RandomForest Classifier and the
8

S.K. Lien and J. Rajasekharan                                                                                                                                                                                  E  n e  r g  y   &     B  u  i ld  i n  g s    3 25 (2024) 114954
Fig. 6. Evolution of accuracy and precision for the building type classification using Random Forest Classifier and FSFS.
4.2. Features and feature selection
Table 10
Evolution of accuracy and precision for the building type classification using
The features extracted in II. B. are chosen based on domain knowl-
Random Forest Classifier and FSFS until the 9th feature is added.
edge on Norwegian load profiles. Other features considered but not
N Feature added Accuracy Precision included were hourly values of the typical day, average daily values of
1 ElImp_actual_mean 0.624 0.616 the typical week with variations on seasons and day types. These fea-
| 2 +daily_average_std |     | 0.761 | 0.752 |     |     |     |     |
| -------------------- | --- | ----- | ----- | --- | --- | --- | --- |
tures were discarded in an early phase as they reduced the performance
| 3 +correlation_daily_SLP_SLP_Apt_EH |     | 0.802 | 0.785 |     |     |     |     |
| ----------------------------------- | --- | ----- | ----- | --- | --- | --- | --- |
+ElImp_max_vs_mean_weekend_is_1 by increasing the number of features too much, and because the infor-
| 4   |     | 0.820 | 0.799 |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- |
5 +ElImp_mean_vs_winter_mean 0.831 0.816 mation from these features are captured by other features. Another
6 +ElImp_actual_max 0.850 0.831 possible way to capture the daily load profiles or yearly profiles could be
+ElImp_max_weekend_is_1
7 0.861 0.839 to use pattern based or shape based features as shown in [42].
| 8 +ElImp_max_weekend_is_0 |     | 0.862 | 0.841 |     |     |     |     |
| ------------------------- | --- | ----- | ----- | --- | --- | --- | --- |
The SLP-features use standard load profiles based on [24,25]. 123
| 9 +ElImp_max_season_is_1 |     | 0.864 | 0.843 |     |     |     |     |
| ------------------------ | --- | ----- | ----- | --- | --- | --- | --- |
buildings from the dataset used in this work were also amongst the
buildings used to extract information to generate the PROFet tool which
CatBoost classifier give similar performance results, but the Random- was used as a base to generate the SLP features. Using these features
Forest Classifier is a much faster approach and is hence preferred for this  could have introduced a small data leakage. To investigate this effect,
the accuracy of predicting the building type as shown in III. A. was
classification. The building type (building category and heating type) is
correctly identified in 84 % of the cases, and with a 92 % top-2 accuracy.  calculated with and without these features. The accuracy with SLP
The accuracy reaches a peak of approximately 86 % when feature se- features is 0.844 as compared to 0.839 without using the SLP features.
lection is used. This is a high and sufficient accuracy for this task,  The number of and combination of features used affects the perfor-
especially given as there is some uncertainty in the labels of the dataset,  mance of the classifier. It is therefore possible that a more optimal
which is further elaborated in F. combination of features could exist or features not suggested in this
Table 11
Performance of ensemble model, CatBoost and random forest when applied to the whole dataset and only residential buildings.
|     | Model |     | Acc. | Acc. top 2 | Preci-sion | Recall | F1  |
| --- | ----- | --- | ---- | ---------- | ---------- | ------ | --- |
All Ensemble_model_soft (RF +CB) 0.844 0.917 0.831 0.844 0.833
Ensemble_model_soft(RF +CB +GB)
|             |              |     | 0.840 | 0.919 | 0.827 | 0.840 | 0.830 |
| ----------- | ------------ | --- | ----- | ----- | ----- | ----- | ----- |
| Residential | RandomForest |     | 0.861 | 0.935 | 0.836 | 0.861 | 0.848 |
|             | CatBoost     |     | 0.847 | 0.937 | 0.826 | 0.847 | 0.836 |
Ensemble_model_soft (RF +CB)
|     |     |     | 0.858 | 0.937 | 0.833 | 0.858 | 0.846 |
| --- | --- | --- | ----- | ----- | ----- | ----- | ----- |
Table 12
Performance of the method when applied to three external datasets (iFlex, HUE and BDG2).
|     | N   | Target |     | Acc. Acc. top 2 | Precision | Recall | F1  |
| --- | --- | ------ | --- | --------------- | --------- | ------ | --- |
iFLEX Train: Original 2179 Building type 0.711 0.876 0.719 0.711 0.708
| Test: iFlex | 1096 |     |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- | --- |
Train: 0.8 iFlex 876 Building type 0.750 0.923 0.743 0.750 0.745
| Test: 0.2 iFlex | 220 |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
HUE Train: Original 2179 Building category 0.462 1.000 0.821 0.462 0.439
| Test: HUE | 26  |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
BDG2 Train: Original 2179 Building category 0.203 0.357 0.533 0.203 0.237
| Test: BDG2  | 566 |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
(selected)
Train: 0.8 BDG2 1224 Primary categories from BDG2 0.565 0.755 0.519 0.565 0.521
| Test: 0.2 BDG2 | 306 |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
9

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
Fig. 7. (a) Distortion and (b) silhouette score for different numbers of clusters using k-means clustering.
Fig. 8. Clustering of buildings in the dataset when using (a) 6 and (b) 17 clusters with k-means clustering. In both cases, the test set has no buildings assigned to one
of the clusters.
article may lead to further improvement in accuracy. The performance 4.5. Testing on datasets across geography and climate zones
will also vary slightly depending on which buildings are included in the
training and test set. The classification method has exhibited good generalizability and
transferability to Norwegian residential buildings, but poor trans-
4.3. Ensemble learning ferability to the HUE and BDG2-datasets. There are a few possible ex-
planations for this. First, the primary building categories used in the
While ensemble models are often powerful tools for improving ac- BGD2 dataset are broad categories with large disparities between the
curacy, soft-voting ensemble models did not improve the performance buildings within them. For example, the category “Education” contains
compared to RandomForest and CatBoost classifiers alone in III. D. the subcategories “School”, “Research”, “Student Centre”, “Classroom”
Ensemble models may not enhance performance due to several factors. among others, which are buildings which can be expected to have large
These include redundancy and correlated errors among base models. disparities in user behaviour and energy systems, while the building
This was to be expected due to the similarities in feature importances for categories in the original dataset contain more uniform buildings,
these models but could not be ruled out without investigation. making them easier to distinguish from each other. Secondly, the fea-
tures extracted from the original dataset may not be the most suitable to
4.4. Supervised vs. Unsupervised classification predict the building category from other countries/climate zones and
with different labels, for instance, looking at features more targeted at
The literature on building electricity load profiles shows that there changes in the load caused by cooling and ventilation rather than
are many examples of unsupervised clustering algorithms used for heating may improve the results. Another reason may be that service
classification of buildings, efficiency classification of buildings and fault buildings such as schools, may have user patterns that differ greatly in
recognition of building electricity use. While unsupervised clustering of different countries for aspects such as needs for cooling, ventilation and
building load profiles are useful for many applications, including heating, different control strategies and HVAC systems. Finally, there is
assigning pricing clusters of different costumers, supervised classifica- a large uncertainty in the quality of the labels of the buildings in the
tion allows to get more tailored labels for the data, which can help BDG2-database, as [43]showed the way a building’s occupants use the
efficiently collect metadata. In this article, buildings are labelled and spaces can be different than what was intended, which may cause
classified according to the building categories used in the Norwegian misclassification or oversimplification. It was found that 26 % of the
building code. Achieving the same classification with unsupervised buildings in the original BDG-dataset was potentially mislabelled based
methods is not possible, as there may be similarities and differences on their load shape behaviour.
between buildings of the predefined categories which will not auto- Onsite renewable energy production, such as photovoltaic (PV)
matically be captured by an algorithm without training on labelled data panels mounted on buildings, can theoretically influence building load
and the domain-specific features. profiles by reducing the demand for imported electricity during periods
of production. Although PV installations are becoming more common,
most buildings in the database currently do not have PV systems. PV
10

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
generation typically peaks midday, especially during summer months. recognize if a building should not be assigned to any of the labels present
The key features identified by feature selection focus on both the and classify them as “Other” or “NA”.
average energy usage throughout the year and peak loads at different
time periods. While mean and median electricity consumption might be 4.7. Consequences of misclassification
affected by PV generation, peak loads, which generally occur during
winter months, are less likely to be significantly impacted due to Predicting the wrong building category in the classification of elec-
reduced solar radiation and lower PV output during the winter season. tricity time series can have varying degrees of consequences depending
The extent to which local renewable generation influences a building’s on the subsequent use of the results. If utilized for labelling buildings
electricity import profile also depends on the ratio of energy production before storing the data in a database for further reference, it is crucial to
to consumption—the higher the production relative to consumption, the explicitly note that the assigned building category is an estimation.
greater the impact on reducing imported electricity. While the classifi- Moreover, it may be beneficial to provide the two most probable cate-
cation of building type (building category and heating category) may gories to mitigate the risk of propagating errors throughout subsequent
not be largely affected by the presence of PV, disaggregation of elec- processes such as energy pricing, integration into demand forecasting
tricity use for different appliances becomes more challenging without models, recommendations for energy-saving measures, and further
separate meters for PV generation, electricity export, and self- analysis and research.
consumption, as total electricity consumption is necessary for the In the authors’ ongoing research, the intention is to employ the
disaggregation task. Classifying buildings with and without PV is a task predicted building category to develop a disaggregation algorithm for
that could be considered for further research, if data from more pro- separating electric space heating loads from total building loads, with
sumers are attained. The buildings’ time series data include both smart the predicted category serving as an input. If a building with electric
meter data and climate data, including solar radiation. The method heating is falsely classified as a building without electric heating using
presented is adaptable, so given the availability of a dataset with meta this method, the disaggregation algorithm may fail to accurately identify
data about PV-installations, the method could be adapted to classify the the electric heating energy usage as intended. Separating buildings with
presence of PV-panels e.g. by adding features that consider the rela- air-to-air heat pumps and buildings that use primarily electric panel
tionship between solar radiation and electricity consumption. heaters can be challenging on hourly data, as these are expected to
exhibit similar patterns, especially during.
4.6. Data quality and labelling peak hours, but also have a slightly lower daily load profile on
average. The model could be improved to estimate the heating type of
The reliability of the labels in the dataset used in this article are not buildings by adding more standard load profiles that differentiates be-
completely certain. The collection of metadata to be used for the tween buildings with different building heating appliances.
labelling of the buildings has been conducted by several researchers
using a variety of approaches, such as looking into building energy la- 4.8. Applications
bels and the Norwegian building registry (cadastre), interviewing
operational personnel, and building managers, and surveys. As described in the introduction, the electrification of all end-use
The building categories of buildings in this database are the same as sectors is essential for transitioning to a sustainable low-carbon soci-
the building categories used in the Norwegian Standard NS 3031 “En- ety. In Norway, the building sector consumes more than half of the
ergy and Power Demand for Heating of Buildings (cid:0) Calculation Rules” nation’s electricity consumptions, primarily for heating, with demand
[29] and for the energy requirements in the regulations on technical peaking during the coldest days of winter. With electrification, peak
requirements for construction works within the Norwegian Building loads are expected to grow, and this raises the question on how we can
Acts and Regulations [16]. Some of these building categories contain limit the growth of peak loads. The suggested method has several ap-
buildings with large variations in energy consumption and user patterns, plications and potential implementations that can aid in improving the
e.g. “Cultural buildings” which include buildings from churches to big knowledge on peak loads in buildings and areas, as well as on how to
concerts halls. The building categories used in these regulations differ limit the peak load. By classifying the presence of electrical heating
from building types used in the cadastre, which divide buildings intro appliances, this approach offers a clearer understanding of energy con-
more groups. Another issue with the labelling of buildings in the data- sumption patterns across different building types. If the method is
base is that buildings can only have one label, while a single building applied by energy providers, it could help identify and tailor energy
may have several uses, for example, a single building can consist of one efficiency and demand flexibility measures for electricity customers or
part which is a school and another part which is an office but can only be analyse the use of different grid capacity tariffs. Additionally, the
assigned to one label in the database. Similarly, there is also some un- method could support improved grid and area planning by estimating
certainty in the labelling of buildings with “Electric Heating (EH)” or the presence of specific customer types in a given region, which could
“Non-electric heating (NEH)”. The metadata about the heating system of help predict coincidence factors and peak loads. In data collection, the
different buildings are acquired by different researchers with different classification of building types provides metadata which can often be
approaches, and the while the metadata indicates the kind of heating time-consuming to collect manually. The estimated class of a building
system installed, it does not necessarily indicate if all the installed could be used as an input feature in a disaggregation task, such as dis-
heating appliances are in use. For some buildings, there may also have aggregating electricity used for heating from a building’s electricity load
been a change in the heating system during the duration of the mea- profile, thereby improving disaggregation accuracy. In the future, the
surements. One example is the use of oil and gas furnaces, which may method could be expanded to classify other forms of metadata, such as
have been in use until 2020 but exchanged later due to the fossil fuel ban electric vehicle charging, photovoltaic systems, and heating types,
for heating purposes in buildings that was enforced from January 2020. further broadening its applications.
The use of heating appliances and electricity for heating may have been
changed for several buildings with measurements that span across 4.9. Future work
several years, but the label of heating appliances may not necessarily
have been updated for all buildings in the database. The classifiers are Future work includes enhancement and refinement of the presented
trained only on certain building categories and cannot recognize other methodology for classification of buildings. Firstly, one may benefit
building categories not present in the dataset, such as, industrial from expanding the current method to classify the type of electric
buildings, parking houses, culture buildings, universities, sports build- heating systems present within buildings, which would provide valuable
ings, and others. The model could however benefit from being able to insights into energy usage patterns and aid in load disaggregation.
11

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
Similarly, the method could be extended to classify whether building is [3] NVE, «NVE.no: Smarte strømmålere (AMS)». [Online]. Tilgjengelig på: https://
equipped with chargers for electric vehicles or not. This could be www.nve.no/reguleringsmyndigheten/kunde/strom/stromkunde/smarte-
stroemmaalere-ams/.
particularly useful for estimating the increasing prevalence of electric [4] The Norwegian Water Resources and Energy Directorate (NVE) og The Norwegian
vehicles and their significant effect on building energy loads. Finally, to Building Authority (DiBK), «Underlag for langsiktig strategi for
enhance the method’s generalizability and applicability across other energieffektivisering ved renovering av bygninger [Foundation for the long term
strategy for energy efficiency by renovation of building]», mar. 2022.
countries/climate zones, it could be beneficial to reevaluate the existing
[5] Direktoratet for byggkvalitet (DiBK) og Norges vassdrags- og energidirektorat
features, incorporate additional relevant features, and add additional (NVE), «Underlag for langsiktig strategi for energieffektivisering ved renoverng av
data from various countries and climate zones to the training data set. bygninger. Utredning for Kommunal- og distriktsdepartementet og Olje- og
energidepartementet», jun. 2022.
Additional relevant features include pattern/shape based features, and [6] L. Ødegården og S. Bhantana, Status og prognoser for kraftsystemet 2018 rapportnr.
possibly model based features [42]. Further, the method could be 103-2018. NVE, 2018. Åpnet: 31. mai 2023. [Online]. Tilgjengelig på: http://
extended to predict the energy efficiency class of the buildings. publikasjoner.nve.no/rapport/2018/rapport2018_103.pdf.
[7] J. Kwac, J. Flora, og R. Rajagopal, «Household Energy Consumption Segmentation
Using Hourly Data», IEEE Transactions on Smart Grid, bd. 5, nr. 1, s. 420–430, jan.
5. Conclusion 2014, doi: 10.1109/TSG.2013.2278477.
[8] A. Rajabi, A pattern recognition methodology for analyzing residential customers
load data and targeting demand response applications, Energy Build. 203 (2019),
This article has introduced 82 domain-specific features and a su- https://doi.org/10.1016/j.enbuild.2019.109455 s. 109455.
pervised automatic building category classification approach for pre- [9] N. Mahmoudi-Kohan, M. P. Moghaddam, M. K. Sheikh-El-Eslami, og E. Shayesteh,
dicting the building category and heating type of Norwegian buildings «A three-stage strategy for optimal price offering by a retailer based on clustering
techniques», Int. J. Electr. Power Energy Syst., bd. 32, nr. 10, s. 1135–1142, des.
from their electricity load profiles with high accuracy. While prior
2010, doi: 10.1016/j.ijepes.2010.06.011.
research has predominantly focused on unsupervised methods for clas- [10] I. Prahastono, D. King, og C. S. Ozveren, «A review of Electricity Load Profile
sifying electricity consumers, the proposed approach has been tailored Classification methods», i 2007 42nd International Universities Power Engineering
Conference, sep. 2007, s. 1187–1191. doi: 10.1109/UPEC.2007.4469120.
to label building load profiles according to Norwegian building regula-
[11] M. Bourdeau, Classification of daily electric load profiles of non-residential
tions (TEK17) standard building categories, making it a more practical buildings, Energy and Buildings 233 (2021), https://doi.org/10.1016/j.
categorization which is useful for grid and area planning. The method enbuild.2020.110670, 110670.
[12] K. R. Shahapure og C. Nicholas, «Cluster Quality Analysis Using Silhouette Score», i
was developed and tested on a large and original dataset of 2740
2020 IEEE 7th International Conference on Data Science and Advanced Analytics
buildings across 10 building categories, including both residential and (DSAA), okt. 2020, s. 747–748. doi: 10.1109/DSAA49011.2020.00096.
non-residential buildings, and achieved an accuracy of 84 % in identi- [13] J.-C. Lamirel, N. Dugu´e, og P. Cuxac, «New efficient clustering quality indexes», i
2016 International Joint Conference on Neural Networks (IJCNN), jul. 2016, s.
fying correct building and heating categories on the testing set.
3649–3657. doi: 10.1109/IJCNN.2016.7727669.
Furthermore, the proposed classification method demonstrates excellent [14] I.P. Panapakidis, T.A. Papadopoulos, G.C. Christoforidis, G.K. Papagiannis, Pattern
generalizability and transferability when applied to unseen electricity recognition algorithms for electricity load curve analysis of buildings, Energy
data from Norwegian apartments. However, testing on buildings from Build. 73 (2014) 137–145, https://doi.org/10.1016/j.enbuild.2014.01.002.
[15] T. Zhang, G. Zhang, J. Lu, X. Feng, og W. Yang, «A New Index and Classification
other climate zones showed less transferability, indicating a need for Approach for Load Pattern Analysis of Large Electricity Customers», IEEE
more features tailored to different climate zones and locations. Transactions on Power Systems, bd. 27, nr. 1, s. 153–160, feb. 2012, doi: 10.1109/
TPWRS.2011.2167524.
[16] Direktoratet for byggkvalitet, Byggteknisk forskrift (TEK17). 2017. Åpnet: 19.
CRediT authorship contribution statement oktober 2021. [Online]. Tilgjengelig på: https://dibk.no/regelverk/byggteknisk-
forskrift-tek17/.
Synne Krekling Lien: Writing – review & editing, Writing – original [17] SN/TS 3031:2016, «Bygningers energiytelse - Beregning av energibehov og
energiforsyning / Energy performance of buildings - Calculation of energy needs
draft, Validation, Methodology, Data curation, Conceptualization. and energy supply». Standard Norge, 2016. Åpnet: 29. oktober 2021. [Online].
Jayaprakash Rajasekharan: Writing – review & editing, Supervision, Tilgjengelig på: https://www.standard.no/no/Nettbutikk/produktkatalogen/
Produktpresentasjon/?ProductID=859500.
Project administration.
[18] Z. Dong, J. Liu, B. Liu, K. Li, X. Li, Hourly energy consumption prediction of an
office building based on ensemble learning and energy consumption pattern
classification, Energy Build. 241 (2021), https://doi.org/10.1016/j.
Declaration of competing interest enbuild.2021.110929, 110929.
[19] T. Tsoka, X. Ye, Y. Chen, D. Gong, X. Xia, Explainable artificial intelligence for
building energy performance certificate labelling classification, J. Clean. Product.
The authors declare that they have no known competing financial 355 (2022), https://doi.org/10.1016/j.jclepro.2022.131626, 131626.
interests or personal relationships that could have appeared to influence [20] M.S. Piscitelli, S. Brandi, A. Capozzoli, ecognition and classification of typical load
profiles in buildings with non-intrusive learning approach, 113727, Appl. Energy
the work reported in this paper.
255 (2019), https://doi.org/10.1016/j.apenergy.2019.113727.
[21] A. Canaydin, C. Fu, A. Balint, M. Khalil, C. Miller, H. Kazmi, Interpretable domain-
informed and domain-agnostic features for supervised and unsupervised learning
Acknowledgment
on building energy demand data, Appl. Energy 360 (2024), https://doi.org/
10.1016/j.apenergy.2024.122741, 122741.
This article has been written within the research project “Coinci- [22] M. Sodenkamp, I. Kozlovskiy, T. Staake, Supervised classification with
interdependent variables to support targeted energy efficiency measures in the
dence factors and peak loads of buildings in the Norwegian low carbon
residential sector, Decision Anal. 3 (1) (2016) 1, https://doi.org/10.1186/s40165-
society” (COFACTOR). The authors gratefully acknowledge the support 015-0018-2.
from the Research Council of Norway (project number 326891), [23] P. Carroll, T. Murphy, M. Hanley, D. Dempsey, J. Dunne, Household classification
research partners, industry partners and data providers. using smart meter data, J. off. Statistics 34 (1) (2018) 1–25, https://doi.org/
10.1515/jos-2018-0001.
[24] K. B. Lindberg, «Impact of Zero Energy Buildings on the Power System», s. 192.
Data availability [25] K. Heimar Andersen, S. Krekling Lien, K. Byskov Lindberg, H. Taxt Walnum, og I.
Sartori, «Further development and validation of the ‘PROFet’ energy demand load
profiles estimator», presentert på 2021 Building Simulation Conference, sep. 2021.
Parts of the data is openly available, while other parts will be made
doi: 10.26868/25222708.2021.30159.
avilable at a later time. Readers may request access to anonymized data [26] S. K. Lien, H. T. Walnum, og Å. L. Sørensen, «COFACTOR Drammen dataset. 4 years
from the authors. of hourly energy use data from 45 public buildings in Drammen, Norway»,
Submitted to: Scientific Data, mai 2024.
[27] S. K. Lien, D. Ivanko, og I. Sartori, Domestic hot water decomposition from measured
References total heat load in Norwegian buildings. SINTEF Academic Press, 2020. Åpnet: 3. juli
2023. [Online]. Tilgjengelig på: https://ntnuopen.ntnu.no/ntnu-xmlui/handle/
[1] IEA, «https://www.iea.org/reports/buildings». 11250/2684373.
[2] Energy Transitions Commission, «Making Mission Possible», Health Progress, bd.
76, nr. 6, s. 45–7, 60, 2020.
12

S.K. Lien and J. Rajasekharan E n e r g y & B u i ld i n g s 3 25 (2024) 114954
[28] K. B. Lindberg, S. J. Bakker, og I. Sartori, «Modelling electric and heat load profiles [36] J. T. Hancock og T. M. Khoshgoftaar, «CatBoost for big data: an interdisciplinary
of non-residential buildings for use in long-term aggregate load forecasts», Utilities review», Journal of Big Data, bd. 7, nr. 1, s. 94, nov. 2020, doi: 10.1186/s40537-
Policy, bd. 58, s. 63–88, jun. 2019, doi: 10.1016/j.jup.2019.03.004. 020-00369-8.
[29] Standard Norge, «SN-NSPEK 3031:2020 Bygningers energiytelse — Beregning av [37] X. Jin og J. Han, «K-Means Clustering», i Encyclopedia of Machine Learning and Data
energibehov og energiforsyning». Mining, C. Sammut og G. I. Webb, Red., Boston, MA: Springer US, 2017, s. 695–697.
[30] F. Pedregosa, Scikit-learn: machine learning in python, J. Machine Learning Res. doi: 10.1007/978-1-4899-7687-1_431.
12 (85) (2011) 2825–2830. [38] Z.-H. Zhou, «Ensemble Learning», i Encyclopedia of Biometrics, S. Z. Li og A. Jain,
[31] J. Fürnkranz, «Decision Tree», i Encyclopedia of Machine Learning, C. Sammut og G. Red., Boston, MA: Springer US, 2009, s. 270–273. doi: 10.1007/978-0-387-73003-
I. Webb, Red., Boston, MA: Springer US, 2010, s. 263–267. doi: 10.1007/978-0- 5_293.
387-30164-8_204. [39] M. Hofmann og T. Siebenbrunner, «A rich dataset of hourly residential electricity
[32] L. Breiman, «Random Forests», Machine Learning, bd. 45, nr. 1, s. 5–32, okt. 2001, consumption data and survey answers from the iFlex dynamic pricing experiment»,
doi: 10.1023/A:1010933404324. Data in Brief, bd. 50, s. 109571, okt. 2023, doi: 10.1016/j.dib.2023.109571.
[33] X. Zhang, «Support Vector Machines», i Encyclopedia of Machine Learning, C. [40] S. Makonin, «HUE: The Hourly Usage of Energy Dataset for Buildings in British
Sammut og G. I. Webb, Red., Boston, MA: Springer US, 2010, s. 941–946. doi: Columbia». Harvard Dataverse, 4. september 2018. doi: 10.7910/DVN/N3HGRN.
10.1007/978-0-387-30164-8_804. [41] C. Miller mfl., «The Building Data Genome Project 2, energy meter data from the
[34] «sklearn.ensemble.GradientBoostingClassifier», scikit-learn. Åpnet: 29. februar ASHRAE Great Energy Predictor III competition», Sci Data, bd. 7, nr. 1, Art. nr. 1,
2024. [Online]. Tilgjengelig på: https://scikit-learn/stable/modules/generated/ okt. 2020, doi: 10.1038/s41597-020-00712-x.
sklearn.ensemble.GradientBoostingClassifier.html. [42] C. Miller, «What’s in the box?! Towards explainable machine learning applied to
[35] G. Brown, «Ensemble Learning», i Encyclopedia of Machine Learning, C. Sammut og non-residential building smart meter classification», Energy and Buildings, bd. 199,
G. I. Webb, Red., Boston, MA: Springer US, 2010, s. 312–320. doi: 10.1007/978-0- s. 523–536, sep. 2019, doi: 10.1016/j.enbuild.2019.07.019.
387-30164-8_252. [43] M. Quintana, P. Arjunan, og C. Miller, «Islands of misfit buildings: Detecting
uncharacteristic electricity use behavior using load shape clustering», Build. Simul.,
bd. 14, nr. 1, s. 119–130, feb. 2021, doi: 10.1007/s12273-020-0626-1.
13