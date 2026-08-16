---
conversion_metadata:
  converted_at: "2026-07-21T08:26:14Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Saghafi et al.pdf"
  source_pdf_sha256: "8e7bda68f3b5efd0dbd71133cfd8af5b0d04c89825a26ec8bc336bf39a5248f5"
  page_count: 14
  markdown_char_count: 189689
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Decision Support Systems 196 (2025) 114499

Contents lists available at ScienceDirect

Decision Support Systems

journal homepage: www.elsevier.com/locate/dss

Impact of categorization autonomy on effective use and adoption intentions

Arash Saghafi a,*, Poonacha Medappa b, Ariton Debrliev c
a Ted Rogers School of Management, Toronto Metropolitan University, 55 Dundas St W., Toronto, ON M5G 2C3, Canada
b Tilburg School of Economics and Management, Tilburg University, 5037, AB, Tilburg, the Netherlands
c Gartner Nederland B.V., De Entree 79, 1101 BH, Amsterdam, the Netherlands

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Categorization
Autonomy
Cognitive schema theory
Restrictiveness
HCI

Category tree view is an omnipresent element in graphical user interfaces where it captures information in terms 
of a hierarchical structure. These categorization trees facilitate human users’  cognitive economy and decision- 
making.  While  previous  research  has  investigated  the  utilities  of  using  unstructured  data  compared  to  pre- 
categorized  information  by  business  users,  the  effectiveness  of  allowing  users  the  autonomy  to  create  their 
own categorization hierarchies from generic object types remains unexplored. This paper evaluates the benefits 
of categorization autonomy in terms of search precision, as an objective measure, as well as subjective intentions 
to  use  the  system.  We  examined  users’  interactions  with  a  platform  in  information  seeking  tasks  with  201 
subjects. Our findings indicate that categorization autonomy leads to superior results, both in terms of effective 
use and behavioral perceptions. We also found that the impact of categorization autonomy is moderated by task 
flexibility, such that the benefits are more apparent in tasks that necessitate open-ended search approaches. By 
focusing on how user-driven categorization influences system interaction, our study contributes to the design of 
decision support systems that are better aligned with users’ cognitive structures and task demands.

1. Introduction

The field of human-computer interaction (HCI) has studied different 
designs  of  computer  systems  and  analyzed  the  interactions  between 
human users and technology with the aim of improving the means of 
attaining the systems’ goals [1]. Research has shown that designs that 
“match the preferences and information needs of [users] are efficient; 
those that do not, forgo potential profit” [2,p. 202]. For example, when 
Intel implemented a verbal advisor to help customers find the relevant 
software, successful downloads increased by 27 % [2]. Thus, allowing 
users  to  choose  a  design  that  matches  their  cognitive  style  would  be 
advantageous to a singular interface design.

One  design  choice  that  determines  the  efficiency  of  information 
assimilation [3] and enables a better cognitive fit with the preferences 
and needs of users is related to how data is categorized and presented to 
users. Categories reflect repeating patterns of properties [4], and cate-
gorization is the ability to detect recurring characteristics of phenomena 
[5].  Categories  aid  humans  with  the  processing  of  information  in  a 
cognitively  economical  manner  [6].  In  information  systems,  category 
trees  are  widely  used  to  provide  users  with  the  same  utilities  of 
abstraction from the way the information in databases is organized [7],

to how items are grouped and presented on almost every user interface 
[8],  whether  in  Decision  Support  Systems  (DSS),  online  banking,  in-
ventory management systems, or e-commerce. In particular, focusing on 
improving  the  decision-making process  through  the  development and 
evaluation of systems that provide users with enhanced information and 
support is central to the design of effective decision support systems [9]. 
From a DSS perspective, categorization tools function as cognitive sup-
port mechanisms that assist users in identifying relevant information. 
Design  decisions  that  shape  this  structuring  –  such  as  granting  or 
restricting autonomy –  could therefore impact the effectiveness of de-
cision support.

In this work, we study the effect of categorization autonomy, defined 
as the extent to which users have the ability to define their own cate-
gorization schemes from a base level of object types. In order to feasibly 
examine the impact of categorization autonomy, we chose to focus on e- 
commerce, since users of such platforms access large amounts of infor-
mation without the need for prior technical training [10] – making it an 
appropriate setting to study how users’ internal categorization mecha-
nisms can be best utilized in processing information and making accu-
rate  decisions  [11].  Although  other  applications  such  as  content 
management systems or organizational resource planning systems could

* Corresponding author.

E-mail addresses: saghafi@torontomu.ca (A. Saghafi), p.k.medappa@tilburguniversity.edu (P. Medappa), ariton.debrliev@gartner.com (A. Debrliev).

https://doi.org/10.1016/j.dss.2025.114499
Received 22 October 2024; Received in revised form 16 June 2025; Accepted 24 June 2025  
Available online 25 June 2025 
0167-9236/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- 
nc-nd/4.0/ ).

---

<!-- PAGE 2 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

have  been  fitting  contexts  to  study  the  benefits  of  categorization  au-
tonomy, we believe that the accessibility offered by e-commerce plat-
forms justifies the choice. While we are not limiting our contributions to 
the e-commerce context, we acknowledge that pre-defined categoriza-
tion  trees  are  considered  “must-have”  design  elements  in  many  in-
terfaces  [12];  however,  not  exploring  a  new  design  that  potentially 
provides a better fit with the cognitive styles of users is akin to forgoing 
profit [2]. Furthermore, DSS research has long emphasized the impor-
tance of adaptive system features that support decision quality across a 
variety of user profiles and task contexts [13]. Categorization autonomy 
aligns with this principle by enabling the system to better fit the needs of 
individual users.

Prior research on human users’ interaction with data categorization 
includes  studies  on  usage  of  non-classified  data  (or  instance-based), 
where  only  things  and  their  attributes  are  recorded  devoid  of  pre- 
defined  structures [7].  Namely, it  was  shown  that content  generators 
on a citizen science platform were able to provide higher quality data 
when they had the option to record their observations free of classifi-
cation  [14,15].  From  a  different  perspective,  content  consumers  in  a 
self-service business intelligence setting were able to write more accu-
rate queries and identify higher quality patterns when they had access to 
non-classified data versus class-based data [16].

We believe one potential solution that offers individuals the ability to 
reap  the  benefits  of  categorization  in  decision-making,  while  also 
providing  a  better  fit  between  the  categorization  scheme  and  the  in-
dividual’s  information  needs,  is  to  allow  them  to  define  their  own 
categorization hierarchies (rather than stripping data of all categoriza-
tion/classification, which distinguishes our work from previous efforts). 
In fact, our premise is that the most effective categorization scheme varies 
substantially across users due to their unique ways of assimilating in-
formation  [3].  To  the  best  of  our  knowledge,  providing  autonomy  to 
general users in creating customized categorizations based on similarity 
of existing lower-level categories or object types in an inclusive setting, 
such as e-commerce, has not been studied before. This notion resonates 
with DSS literature on user-driven modeling and tailoring of information 
structures [17], which suggests that empowering users to organize in-
formation  according  to  their  decision  logic  can  lead  to  better  system 
outcomes.

Rooted  in  March’s  [18]  learning  taxonomy,  “two  types  of  system 
usage can drive individual task performance: exploitation and explora-
tion” [19,p. 236]. Hence, in order to conduct a comprehensive investi-
gation of how categorization autonomy could be used in practice, we 
follow  this  taxonomy  in  our  study  design.  In  the  context  of  online 
searches  on  an  e-commerce  platform,  exploitation  corresponds  to 
searches  where  users  pursue well-defined goals  by  following a  closed 
and structured approach (e.g., searching for a 16-gigabyte USB storage), 
whereas  exploration  involves  searches  characterized  by  greater  vari-
ability and openness in the search process (e.g., browsing for Christmas 
gifts for friends and family). In this paper, we capture the two modes of 
system usage with the Task Flexibility concept – defined as the extent to 
which a task allows for multiple ways of achieving the desired outcome. 
Tasks with low flexibility align with exploitation, where users follow a 
predetermined  and  closed-ended  path.  Conversely,  tasks  with  high 
flexibility encourage open-ended questioning and variability.

Considering the usage types, we examine the impact of categoriza-
tion  autonomy  from  an  objective  usage  effectiveness  perspective  in 
terms  of  users’  ability  to  fulfill  a  certain  usage  goal,  in  line  with  the 
definition of effective use [20], as well as subjective behavioral percep-
tions. System Use has been described in terms of a user, system, and task, 
and defined a task as a “goal-directed activity”  [19 ,p. 231]. Further, 
system use and effective use can be distinguished from one another by 
emphasizing on the performance of “a goal-directed activity to using it 
in a way that helps attain the relevant goal” [20 ,p. 633], instead of just 
being simply able to use the system. With a goal as a “cognitive repre-
sentation of a desired end-point” [21 ,p. 491], it is assumed that goal- 
attainment  has  objective  qualities,  which  can  be  operationally

assessed in terms of the performance of an observable behavior [20]. In 
this paper, we set out to evaluate the efficacy of categorization auton-
omy  from  both  perspectives  of  objective  performance  as  well  as  sub-
jective intentions to use the system given the chance. The objective and 
subjective analysis is further motivated by the multidimensional nature 
of Information Systems (IS) success [22]. Demonstrating that categori-
zation autonomy not only helps in the attainment of usage goals (i.e., 
objective  measure),  but  also  leads  to  higher  subjective  perceptions, 
provides strong support for its efficacy as a viable design.

To  study  the  potential  benefits  of  categorization  autonomy,  we 
conducted an online laboratory experiment with a total of 201 subjects 
who  were  surrogates  of  actual  online  shoppers.  We  developed  an 
experimental website using data scraped from a major North American 
e-retailer  (with  annual  revenue  of  more  than  US$50  billion)  offering 
subjects the same level of product information as a typical e-commerce 
platform.  Based  on  random  assignment  of  subjects  to  three  levels  of 
categorization  autonomy (i.e., no autonomy as in the source website, 
partial autonomy, and full autonomy), we found that online shoppers 
who defined their own product category trees were able to search for 
products  more  accurately  in  both  closed  and  open-ended  searches. 
Furthermore, task flexibility was also found to demonstrate a significant 
moderating effect, indicating that the effect of categorization autonomy 
is  indeed  stronger  for  tasks  with  higher  flexibility  (i.e.,  exploratory 
tasks). The behavioral usage intentions were also positively improved 
for users who had full categorization autonomy. Advantageous results in 
both  objective  and  subjective  metrics  for  categorization  autonomy 
provide  strong  evidence  for  the  effectiveness  of  this  design.  We  also 
performed  a  post-hoc  analysis  to  understand  the  differences  between 
individuals’ self-defined categories and their variations from the base-
line of the e-retailer’s pre-defined scheme. Our findings indicated that 
individualized categories were indeed dissimilar from one another and 
the e-retailer’s – corroborating that users assimilate information differ-
ently [3]. The differences from the baseline were significantly stronger 
for users who demonstrated greater levels of the openness personality 
trait, which is associated with the generation of novel ideas and crea-
tivity [23].

2. Conceptual development

Categories help human users process information more efficiently, 
and  in  information  systems,  they  are  used  in  various  settings  from 
database  organization  [7]  to  grouping  products  on  e-commerce  plat-
forms, aiding shoppers in navigating options. Categorization trees are 
considered one of the “core elements of a retail e-commerce website” 
[24,p. 2]. Their importance is highlighted beyond just website search 
functions,  noting  that  effective  searches  require  knowledge  of  the 
domain  to  input  the  right  keywords  [25].  Even  with  some  domain 
expertise,  users  might  favor  browsing  categories  for  a  more  compre-
hensive  overview,  especially  on  platforms  with  less  effective  search 
engines than Google. In decision support systems, also, taxonomies have 
been  shown  as  effective  decision  support  aids,  particularly  for  non- 
expert  users  [26].  Moreover,  even  a  knowledgeable  user  still  needs 
good querying skills for efficient searches, as certain terms lead to better 
results [25] (e.g., “romantic comedy”  over “funny movie for a date”). 
Thus,  categorization trees  are  indeed  valuable features for users with 
average domain familiarity and querying skills. Offering improvements 
to the categorization tool could increase the utility of this design feature 
even further.

Prior categorization research in Information Systems has discussed 
human users’ ability to create and interpret categories.1 The stream that

1 Automation  of  categorization  is  also  discussed  in  the  literature  (e.g., 
[27,28]), however, the database design (by humans or machine) is beyond our 
scope  as  our  focus  is  on  the  individual  content  consumer  who  uses  the  cate-
gorization scheme for their own individual use.

2

---

<!-- PAGE 3 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

studies humans’  decisions with regards to creating categorization pre-
scribes  how  basic  classes  can  be  identified  by  a  system’s  designer  in 
order  to  create  better  interfaces  (e.g.,  [29]),  but  that  perspective  is 
beyond our scope as it takes the point of view of a designer rather than 
the end-users. In the other line of research that focuses on human users’ 
interactions with and understanding of categories, we could refer to the 
instance-based paradigm [7], as a data management approach that is an 
alternative to class-based. The instance-based paradigm is conceptual-
ized in a two-layered architecture: the first layer includes the instances 
and  their  attributes  (e.g.,  a  round  thing  that  is  red,  has  a  30-in. 
circumference, and weighs 620 g), and the other layer includes classes 
(e.g.,  basketball,  baseball,  hockey  puck)  along  with  their  definitions. 
This stream developed further, namely, from content-generator [14,15] 
and content-consumer perspectives [16]. Prior research has found evi-
dence  that  enabling  instanced-based  data  entry  for  a  ‘crowd’  that 
uploaded user-generated content to a citizen science platform increased 
overall  accuracy  and  crowd  information  quality  [14].  The  content- 
consumer  perspective  investigated  users’  ability  to  run  queries  and 
also engage in business intelligence and pattern detection on datasets 
that were free of classification (i.e., instances and their properties). It 
was found that users of instance-based data achieved higher query ac-
curacy, and performed significantly better in pattern discovery [16].

The present study is different from the instance-based paradigm as 
we kept the classes assigned to products and thus, did not directly study 
instances and attributes. Moreover, this paper is not focused on auto-
mating the creation of categories within e-commerce, where algorithms 
certainly play an important role in handling a large number of items that 
need  to  be  classified.  The  distinction  in  this  research  is  in  allowing 
general users to define their categorization trees and hierarchies based 
on a given set of already specified leaf-level categories (such as televi-
sion, camera, or fridge).

2.1. Impact of categorization autonomy on effective use

Categorization provides a form of cognitive economy [6] by helping 
organisms, such as humans, gain the maximum amount of information 
through minimum effort, optimizing the impact on their finite cognitive 
resources. This description of categorization plays into what we consider 
heuristics. Heuristics are problem-solving ‘shortcuts’ that usually lead to 
an outcome, which may not be the optimal solution, but use relatively 
low amounts of cognitive resources to do so [30]. Humans create cate-
gories  through  learning  and  information  processing.  There  are  several 
models  that  try  to  explain  how  information  processing  occurs  in  in-
dividuals. Here, we discuss the ramifications of self-defined categories 
from  the  perspectives  of  cognitive  schemas  [3]  and  decision-making 
[30].

Cognitive schema theory (CST) posits that human memory is made of 
‘memory objects’ that form ‘mental models’ [3]. Memory objects are the 
building  blocks  that  contain  general  facts  about  something  (e.g.,  I 
remember the weather was sunny). CST implies that individuals develop 
memory objects through life experiences, such as their studies, events, 
and their culture. Memory objects that are linked to one another form 
mental models, which tend to be more situational in nature. In the in-
formation assimilation process, a model is adjusted to the situation at 
hand.  These  mental  models  allow  individuals  to  form  patterns  that 
consist of multiple types of memory objects, such as facts, emotions, and 
the  relations  between  objects;  for  example,  “I  remember  the  weather 
was sunny (fact), and I felt good (emotion) – sunny weather makes me 
feel good (pattern)”.

This is an important aspect when looking at pre-defined versus self- 
defined  categorization  (i.e.,  categorization  autonomy).  According  to 
CST, we understand that an individual’s mental models are dependent 
on their personal experiences. As everyone’s personal experiences are 
unique, we can assume that the patterns they have formed are distinct as 
well. In this paper’s context, these patterns entail the way a product tree 
is categorized. The tree created by a systems designer in an organization

would have used different memory objects and patterns than the ones a 
given  end-user  is  familiar  with.  This  could  result  in  an  incongruent 
product tree for the user, leading to inefficiencies in using it.

From  a  different  perspective,  Tversky  and  Kahneman  [30]  discuss 
heuristics as mental shortcuts that are used in human decision-making. 
Initial information cues or starting points also act as heuristics that can 
influence individuals [31]. In essence, we can consider high-level cate-
gories as anchor points for lower-level categories. Tversky and Kahne-
man [30] discuss that these heuristics function as anchors that bias and 
limit one’s decisions. In the absence of such anchors, an individual tends 
to have a greater degree of freedom in thinking and decision-making. 
Hence,  we  posit  that  pre-defined  categorizations  (i.e.,  the  condition 
with  no  categorization  autonomy)  act  as  anchors  that  bias  one’s  de-
cisions  towards  the  original  designers’  perspective.  Self-defined  cate-
gories – once created – could also act as anchors in future use, but they 
would be more congruent with the given individual’s view in the first 
place  (i.e.,  as  the  result  of  full  categorization  autonomy).  Moreover, 
according to Cognitive Fit Theory [32], performance improves when the 
information representation aligns with the user’s cognitive processes. In 
other words, allowing users to create their own categorization schemes 
provides a better cognitive fit, which should lead to higher search pre-
cision,  as  users  can  structure  information  in  a  way  that  mirrors  their 
internal problem-solving strategies. Recent DSS studies have extended 
Cognitive Fit Theory by showing how the alignment between informa-
tion  representation  and  task  characteristics  improves  decision  perfor-
mance  across  various  contexts.  For  example,  the  literature  has 
demonstrated  that  presentation  format  interacts with  product  type  to 
shape decision quality in e-commerce, highlighting the importance of 
matching system features with the nature of the user’s task [33]. Simi-
larly,  it  was  also  shown  that  even  within  data  visualization  contexts, 
users  experience  varying  levels  of  cognitive  effort  depending  on  how 
well the design fits the task demands [34]. These perspectives emphasize 
the need for systems to support diverse cognitive processes.

Based  on  the  aforementioned  perspectives,  our  proposition  is  that 
users who define their own categories will assimilate information better, 
and hence, will be able to attain their goals of using the system. A goal 
can be conceptualized as a “cognitive representation for a desired end- 
point” [21 ,p. 491]. Building on this, effective use was defined as “using 
a system in a way that helps attain the goals for using the system” [20 ,p. 
633]. The goal-attainment factor is what distinguishes effective use from 
general use. Further, assuming objective qualities to goal-attainment, it 
was posited that effective use can operationally be assessed in terms of 
performance of an observable behavior [20]. In e-commerce, the goal is 
to search and find products, and its fulfillment can be measured in terms 
of users being able to correctly search and identify items with certain 
attributes (or reach the ‘desired end-point’ in terms of a goal). Therefore, 
we  hypothesize  that  because  of  better  assimilation  of  information, 
subjects having autonomy to create their own categorization schemes 
will be more successful in searching and identifying correct items (and 
achieve their usage goals):

: Categorization autonomy leads  to higher levels of search  precision

H1.
while using the system.

Search precision is the operationalization of effective use, which we 
calculated as the ratio of the correctly identified items over the number 
of pre-specified items (i.e., the goal) in this study.

2.2. Task flexibility moderating the impact of categorization autonomy on 
effective use

While  categorization  autonomy  offers  users  a  greater  degree  of 
control  over  how  they  structure  information,  its  effectiveness  may 
depend on the nature of the task being performed. In particular, Task 
Flexibility - defined as the extent to which a task allows for multiple ways 
of achieving the desired outcome - may shape how beneficial categori-
zation autonomy is in improving search precision and decision-making.

3

---

<!-- PAGE 4 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Some  tasks  are  inherently  flexible  and  allow  users  to  pursue  various 
paths and options (e.g., browsing for a birthday gift for a friend), while 
others are relatively rigid and afford limited flexibility (e.g., locating a 
replacement cartridge for a particular printer model). This variation in 
how a task can be approached may influence whether users benefit more 
from a predefined categorization tree or from the ability to define their 
own categories.

This distinction aligns with Cognitive Fit Theory [32], which posits 
that task performance improves when the representation of information 
matches the cognitive processes required for the task. When a task is 
flexible, users can benefit more from the ability to define categories in a 
way  that  reflects  their  personalized  strategies  and  evolving  sense  of 
relevance. Categorization autonomy, in this context, provides a better 
cognitive fit by supporting adaptive information structures. In contrast, 
when tasks are inflexible and allow only a narrow set of procedural steps 
or criteria, the user may not require (or be able to take full advantage of) 
the freedom offered by categorization autonomy, as the rigid nature of 
the task already constrains their decision-making path.

A related lens is provided by Task-Technology Fit Theory [35], which 
suggests that a system is more likely to enhance performance when its 
functionality matches the demands of the task. In flexible tasks, cate-
gorization  autonomy  increases  the  alignment  between  task  and  tech-
nology by enabling users to construct a structure that suits their evolving 
needs. For inflexible tasks, however, the fit between technology and task 
may not be as much improved by the introduction of autonomy, as the 
standard  categorization  approach  may  already  be  predefined  by  the 
task’s limited degrees of freedom. Based on this rationale, we expect that 
propose the following hypothesis:

H2.
:  Task  flexibility  moderates  the  relationship  between  categorization 
autonomy and search precision such that the effect of categorization auton-
omy would stronger for more flexible tasks.

different decisions). From a different angle, it has been discussed how 
the  “autonomy  over  the  communication  process”  [39 ,p.  737]  with  a 
system  would  lead  to  higher  adoption  intentions.  In  our  context,  we 
expect  categorization  autonomy  to  positively  affect  usage  intentions, 
and this relationship to be mediated by perceptions of restrictiveness:

H3.

: Categorization autonomy leads to higher usage intentions.

: Perceived restrictiveness will mediate the relationship between cate-

H4.
gorization autonomy and usage intentions.

The proposed nomological research model is captured in Fig. 1.
While we recognize that in a longitudinal study of habits, perceptions 
could  affect  performance,  or  vice  versa,  we  considered  the  objective 
performance to be independent from subjective perceptions during our 
study (which was a one-time task). We believe that in some situations, 
an individual may not necessarily have a positive perception towards a 
task  (e.g.,  not  enjoying  a  warm-up  drill  before  a  sports  game),  yet, 
positive  results  may  be  achieved  from  an  objective  perspective  (e.g., 
better agility while playing the game). Or, alternatively, subjects may 
have positive perceptions (e.g., enjoying candies before a match), and as 
a  result,  have  poorer  objective  performance  (e.g.,  experiencing  sugar 
crash  and  fatigue).  Hence,  we  decided  to  investigate  objective  and 
subjective measures independently of one another and did not make any 
hypotheses about their possible interactions.

As mentioned, to thoroughly inspect the phenomenon, we conducted 
an  experiment  that  operationalized  March’s  [18]  exploitation- 
exploration  taxonomy  as  task  flexibility,  moderating  the  impact  of 
categorization  autonomy  on  effective  use.  The  IS  literature  [20]  also 
adapted March’s taxonomy and defined exploitation of information as a 
task involving the use and search for things already known or a routine 
execution  of  knowledge  in  a  closed-ended  task.  Exploration  of  infor-
mation is the search for things in an open-ended setting.

2.3. Effect of categorization autonomy on behavioral perceptions

3. Methodology and experimental setup

As  mentioned  earlier,  when  assessing  the  efficacy  of  a  design,  in 
addition to evaluating objective performance measures (such as search 
precision),  understanding  behavioral  dimensions  is  also  crucial  in 
determining  its  success  and  adoption  by  users  [22].  Providing  online 
users with the autonomy to create self-defined categorization schemes 
could affect their intentions to use a platform. We study the relationship 
between  categorization  autonomy  and  usage  intentions  through  the 
mediation effect of perceived restrictiveness of the interface. Silver [36] 
defines the restrictiveness of a system as the extent to which a system 
constrains the user’s “decision-making processes to a particular subset of 
all  possible  processes”  [36 ,  p.  52].  Restrictiveness  is  considered  a 
relative term, where the set of supported processes or actions in a system 
could  be  larger  or  more  limited  compared  to  another  system’s  set  of 
supported  actions  [36].  In  our  context,  perceived  restrictiveness  is 
relevant since in the fixed categorization condition, the system does not 
allow the user to perform any actions with regard to categorization of 
concepts –  hence, that condition is restricted. With categorization au-
tonomy, on the other hand, the system allows users to create categori-
zation  trees  based  on  their  world  view.  As  a  result,  categorization 
autonomy is less restrictive and is expected to be perceived as such by 
the users.

We  predict  that  subjects  would  have  lower  intentions  to  use  an 
interface that has fixed categorization schemes compared to a system 
that offers categorization autonomy. This reasoning is in line with prior 
work [37] in which they studied decision support aids with additive- 
compensatory,  eliminatory,  and  hybrid  strategies  and  showed  that 
when a user’s desired support functionalities were not offered by a de-
cision  support  system,  the  psychological  reactance  reduced  their  in-
tentions to use the system - as per the reactance theory [38]. In their 
study,  the  relationship  between  decision  strategy  and  adoption  in-
tentions  was  mediated  by  perceived  restrictiveness  (resulting  from

The concept of ‘effective use’ – as the users’ ability to fulfill the goals 
of  using  a  system  –  is  often  operationalized  by  performance  [20].  To 
study  this  in  the  context  of  categorization  autonomy,  we  created  a 
website to simulate the task of online shopping. Participants’ ability to 
find products that meet their search goals is a measure of performance or 
effective use.

We  hired  an  experienced  developer  to  create  the  experiment’s 
website  by  scraping  the  contents  of  a  prominent  North  American 
Multinational Consumer Electronics (NAMCE) retailer with an annual 
revenue  of  more  than  US$50  billion.  The  scraped  product  data  was 
imported into our experimental website, and using the WooCommerce – 
Store Exporter plugin, a list of category names and associated URLs was 
generated  in  JSON  format  to  populate  the  interactive  platform.  The 
experimental website included over 10,000 products, with prices, de-
scriptions,  and  images,  and  was  fully  functional  –  allowing  users  to 
browse, add items to their cart, and proceed to a checkout screen.

Fig. 1. Nomological research model.

4

---

<!-- PAGE 5 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Separate  environments  were  created  for  each  condition,  all  con-
taining the same products to ensure informational equivalence [40]. The 
product category tree on NAMCE was captured in a three-level hierar-
chy; for example, Appliances as a top level, included Major Appliances 
and  Small  Kitchen  Appliances  in  the  middle  tier,  and  then  general 
product  types  such  as  Dishwashers  and  Coffee  Makers  as  leaf-level 
general product types. We also adopted this three-level categorization 
hierarchy in our study – Fig. 2 shows a screenshot of our website.

The NAMCE contained around 250 leaf-level categories (e.g., tablet, 
air conditioner, laser printer). For practical reasons, we had to limit the 
number of leaf-level categories as it would have taken a considerable 
amount of time to classify the whole set of 250 categories. In the real 
world, in case categorization autonomy was offered by a platform, users 
could  create  their  categories  over  multiple  sessions;  however,  that 
would  not  have  been  feasible  for  our  studies.  Hence,  we  conducted 
multiple trials online with 10 Amazon Mechanical Turk (AMT) workers 
in  each  iteration,  and  trimmed  30  to  40  leaf-level  categories  (while 
maintaining a relatively consistent distribution at higher levels of the 
tree) in each attempt until the categorization time reached the average 
of 15 min with 78 leaf-level categories remaining. Given that attention 
typically declines after 10–15 min [41], we set 15 min as a reasonable 
time for participants to create categories before starting the main task.
We  used  three  conditions  in  our  studies.  The  first  condition,  or 
control, was based on the NAMCE’s website and all three levels of the 
category tree were fixed (i.e., no autonomy in changing the categories by 
users)  –  from  here  on  we  use  fixed  categorization  and  no  autonomy 
interchangeably. Our treatment condition provided full autonomy, and 
showed  subjects  only  the  leaf-level  categories.  Their  interface  had  a 
feature that allowed them to create high-level (i.e., Level 1) and sub-
categories (i.e., Level 2) and populate them by dragging and dropping 
the leaf-level categories (i.e., Level 3) inside them. The flexible catego-
rization interface was developed using JavaScript on the Vue.js frame-
work, and included an ‘edit’ interactive panel. Fig. 3 shows the edit page 
where a subject created one top-level category named “Home” with two 
subcategories of “Kitchen” and “Living Room”. The leaf-level categories 
on the right-side pane could be dragged and dropped under them by the 
users. The users’ self-defined categories were storied as structured JSON 
objects.

We also created a middle condition where Level 1 and Level 2 were 
the same as the source website, but participants had to manually drag 
and drop the leaf-level categories under these fixed levels. We consider 
this condition to offer partial autonomy. We did not develop formal hy-
potheses  regarding  this  condition,  as  it  is  not  part  of  our  theoretical 
development. Rather, we included this to rule out alternative explana-
tions for the effects observed in the full autonomy condition. Namely, 
the partial autonomy condition helps clarify whether the observed im-
provements in performance and perceptions were due to the effect of 
categorization  autonomy  itself,  or  from  greater  time  spent  engaging 
with  the  interface.  The  partial  autonomy  condition  strengthened  the 
internal  validity  of  our  findings  by  serving  as  a  control  for  potential 
confounds related to effort and user involvement.

3.1. Experimental design

We  adopted  a  3  × 2  between-subjects  experimental  design  to 
investigate the impact of Categorization Autonomy (fixed, partial, full) 
on users’ search precision, and to examine whether this relationship is 
moderated  by  Task  Flexibility  (low  in  exploitive  search  vs.  high  in 
exploratory search). Categorization Autonomy was the primary manip-
ulated  factor,  representing  different  levels  of  user  control  over  the 
categorization structure. Task Flexibility, treated as a moderating factor, 
is  conceptualized  as  the  degree  of  variability  in  how  a  task  can  be 
approached  and  completed.  Higher  task  flexibility  enables  greater 
variability and openness in decision-making processes, whereas lower 
task flexibility constrains users to follow a more closed and predefined 
path. Participants were randomly assigned to one of the six experimental

conditions resulting from the factorial combination of the two variables. 
This design enabled us to assess the main effect of Categorization Au-
tonomy on search performance, as well as whether the strength of this 
effect varied across levels of Task Flexibility. After reviewing the consent 
form,  subjects  received  pre-experiment  questions,  which  collected  in-
formation about e-commerce experience, openness (a big-five person-
ality trait [42]), and demographics.

Subjects in all six conditions viewed a  training video that demon-
strated browsing, ordering, and adding to cart functions. Subjects in the 
partial and full categorization autonomy groups received an additional 
five-minute tutorial on using the ‘edit categories’ page and creating their 
own  categories  –  as  the  category  ‘edit’  feature  was  only  available  to 
them. We used different products in the training demonstration (which 
were  not  available  in  the  main  experiment)  to  avoid  biasing  the 
participants.

Next,  the  subjects  in  the  partial  and  full  autonomy  conditions 
(whether in high task flexibility or low) were asked to edit or create their 
categories respectively, and the fixed categorization (i.e., control) group 
was asked to spend five minutes inspecting the categories. The manda-
tory inspection time given to the control group allowed us to provide an 
equivalent condition (with regard to familiarization and engagement) 
for browsing the categories between all three conditions. Further, the 
time that the participants spent on the page was measured to account for 
any differences between the groups. These steps were consistent in all 
conditions,  and  as  reported  in  the  post-hoc  analysis  section,  the  time 
spent in this stage was not a significant covariate on the results. Then, 
subjects received the scenarios for the respective studies and were asked 
to perform the assigned task. At the end, participants answered survey 
questions regarding their usage intentions (Appendix A).

3.2. Sample selection

For our studies, we used Amazon Mechanical Turk (AMT) workers 
belonging to the ‘master worker’  category –  top performers who were 
granted the ‘master’ qualification by Amazon – with more than 100 jobs 
completed and at least a 95 % approval rate. We also limited the sample 
to participants located in the United States or Canada (where the source 
e-retailer also operates). Several studies have shown that AMT workers 
exhibit  comparable  biases  and  performance  to  other  participants  in 
traditional laboratory experiments [14,43]. In addition, we believe that 
AMT subjects are appropriate surrogates for typical e-commerce users 
with similar demographic profiles; hence, their recruitment is justified. 
Based on the initial statistical power analysis on a pilot with 20 subjects, 
we decided on a sample size of around 35 in each condition based on the 
desired  power  of  0.8.  Moreover,  it  has  been  stated  that  for  a  sample 
containing minor subgroups, a minimum of 20 to 50 elements is needed 
per group [44]. The subjects received fixed compensation depending on 
the experimental condition that was higher than the minimum hourly 
wage in the United States.2 Participants were 45 % female and 55 % 
male with 36 % in the age bracket of 30–40 years old. We eliminated 
duplicate  entries,  treatment  participants  who  had  not  created  a  cate-
gory, subjects who had not placed an order, and those who failed the 
trap question in the survey.3

The scales for the behavioral measures were tested for validity and 
reliability (Appendix B). All the variables exhibited high factor loadings 
and  thus  warranted  no  further  adjustments.  Next,  we  examined  the 
Cronbach’s alpha and Average Variance Extracted (AVE) measures for

2 In  pilot  studies,  control  subjects  averaged  30  min,  while  partial  and  full 
autonomy groups averaged 37 and 45 min, respectively. Accordingly, partici-
pants were paid $6 (fixed), $7 (partial autonomy), and $8 (full autonomy).

3 We initially recruited 77 subjects in the fixed, 73 in the partial, and 75 in 
full categorization autonomy conditions. After the exclusions, we analyzed 69 
subjects  in  fixed,  67  in  partial,  and  65  in  the  full  categorization  autonomy 
group.

5

---

<!-- PAGE 6 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Fig. 2. Three levels in the product category tree, as in the source website.

Fig. 3. Treatment Condition Interface with Category Edit Feature.

the different constructs. The results demonstrated a Cronbach’s alpha of 
above 0.9 for all constructs, which indicated high reliability [45]. The 
AVE of all constructs was high as well (>0.5), indicating high conver-
gent validity [46]. Appendix B provides the details.

3.3. Experiment

As mentioned, subjects were randomly assigned to one of the main 
conditions of control (i.e., fixed categorization), partial categorization 
autonomy with the first two levels of the category tree fixed according to 
NAMCE’s design, and treatment conditions (i.e., full categorization au-
tonomy),  and  either  performed  the  closed-ended  exploitive  task  (i.e., 
low  task  flexibility),  or  the  open-ended  exploratory  search  (i.e.,  high 
task  flexibility).  The  subjects  in  the  fixed  categorization  group  were 
instructed to study the product tree, while the subjects in the partial and 
full categorization autonomy conditions had to categorize 78 leaf-level 
product  types  into  higher  level  categories.  We  employed  a  live  chat 
function for subjects in every condition, and we were reachable to them 
throughout the experiment. The actual task scenario was locked behind 
a password-protected page. Subjects in the fixed condition received the 
password after five minutes, and subjects in the partial and full auton-
omy condition had to let us know when they were done with the cate-
gorization activity, and once we verified their completion of building the 
category  trees,  we  offered  them  the  password  that  allowed  them  to 
proceed  to  the  main  task.  The  scenario  for  the  tasks  is  available  in

Appendix C.

Subjects did not have access to a keyword search function and had to 
locate the items using the categorization tree of their respective condi-
tions. The search function feature was removed due to the intention to 
run a controlled laboratory experiment, where extraneous factors and 
their  potential interactions  were  held  constant  to isolate  the  effect of 
categorization autonomy. Once subjects finished adding the items to the 
shopping  cart,  they  proceeded  to  the  post-experiment  questionnaire 
about behavioral perceptions. Table 1 presents the descriptive statistics.
The  first  hypothesis  was  related  to  subjects’  ability  to  search  and 
identify  the  correct  products  based  on  the  given  scenario.  Two  inde-
pendent coders went through the shopping carts of subjects in all three 
conditions and rated whether the item was acceptable with regard to the 
specifications. The intra-class correlation between the two coders was 
95 %, which indicates a high degree of reliability.

Subjects received a point for every correct item they had identified 
(e.g., one point if they had chosen a 27-in. monitor as per the scenario, or 
an  air-fryer  as  a  gift  for  a  cooking  enthusiast,  but  no  points  were 
awarded  for  a  product  that  did  not  match  the  specifications).  To 
compare the precision of the results, we calculated the ratio of correct 
answers to the total number of required items (i.e., dividing each score 
by the number of items subjects were instructed to buy). Since catego-
rization autonomy can be treated as an ordinal variable (fixed catego-
rization or no autonomy < partial autonomy < full autonomy), we ran 
regression  tests  (after  checking  for  normality  of  distribution)  to

6

---

<!-- PAGE 7 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Table 1 
Descriptive statistics.

Variable 
Condition

Search 
Precision 
Mean (SD)

Perceived 
Restrictiveness Mean 
(SD)

Intention to 
Use 
Mean (SD)

Fixed – Low

Flexibility, N = 36

Fixed – High

Flexibility, N = 33
Partial autonomy –

Low Flexibility, N =
30

Partial autonomy –

High Flexibility, N 
= 37

Full autonomy – Low 
Flexibility, N = 34
Full autonomy, High 
Flexibility, N = 31

0.822 
(0.233)
0.737 
(0.371)
0.811 
(0.226)

0.677 
(0.329)

0.971 
(0.068)
0.914 
(0.171)

4.231 (1.441)

4.689 (1.592)

3.533 (1.464)

3.387 (1.827)

3.069 (1.618)

2.785 (1.447)

4.389 
(1.573)
4.263 
(1.659)
5.577 
(1.229)

5.811 
(1.158)

4.932 
(1.395)
5.204 
(1.497)

investigate which group orders showed the effect. The ordinal analysis is 
in line with a prior study with a similar design [47] on decomposition of 
conceptual models and the adherence to Good Decomposition Principles 
at three levels (comparing good vs. bad, good vs. moderate, and mod-
erate vs. bad). Similar to their analysis, we investigated whether higher 
degrees of categorization autonomy led to advantageous results. Table 2
shows that offering categorization autonomy resulted in an overall in-
crease in search precision (0.077, p < 0.05; Model 1). In our group-wise 
comparisons,  we  find  that  search  precision  for  subjects  who  had  full 
categorization  autonomy  was  significantly  higher  (0.155,  p  < 0.01; 
Model 2) than users of pre-defined categories from the original retailer’s 
website (i.e., fixed categorization or no autonomy). Subjects in the full 
autonomy  condition  also  significantly  outperformed  subjects  in  the 
partial  autonomy  (0.204,  p  < 0.01;  Model  3),  but  the  difference  in 
performance  between  fixed  categorization  and  partial  autonomy  con-
ditions was not statistically significant. This result is expected, as only 
the full autonomy allowed participants to adjust the information struc-
ture  to  fit  their  cognitive  processes  [32],  whereas  partial  autonomy 
constrained them to fixed Level 1 and 2 categories, limiting flexibility to 
product placement only at the leaf level. Overall, the first hypothesis was 
corroborated.

We  tested  the  moderation  effect  of  Task  Flexibility  (exploitive  or 
closed-ended vs. exploratory or open-ended tasks) on the relationship

Table 2 
Regression analysis for impact of categorization autonomy on search precision – 
Hypothesis 1.

Outcome: Search 
Precision

Categorization 
Autonomy 
(0 ¼ Fixed; 1 ¼
Partial; 2 ¼ Full)

Fixed vs. Full 
Autonomy 
(0 ¼ Fixed; 1 ¼
Full)

Partial v. Full 
Autonomy 
(0 ¼ Partial; 1 ¼
Full)

Fixed vs. Partial 
Autonomy 
(0 ¼ Fixed; 1 ¼
Partial)

N
R-Sq

** p < 0.01 * p < 0.05.

Model 2 
Coefficient 
(Standard 
Error)

Model 3 
Coefficient 
(Standard 
Error)

Model 4 
Coefficient 
(Standard 
Error)

Model 1 
Coefficient 
(Standard 
Error)

0.077  
(0.019)**

0.155 
(0.039)**

0.204 
(0.327)**

(cid:0) 0.048  
(0.051)

201
0.0570

134
0.1006

132
0.1729

134
0.0067

between categorization autonomy and search precision as  our second 
hypothesis. The results in Table 3 show that the interaction effect of task 
flexibility  and  categorization  autonomy  is  significant  in  a  continuous 
operationalization  (0.179,  p  < 0.01;  Model  1).  After  checking  for 
normality of the distribution, we found that task flexibility moderates 
the effect of categorization autonomy on search precision in comparison 
of  fixed  vs.  full  autonomy  (0.161,  p  < 0.05;  Model  2),  and  also  in 
comparison of partial vs. full autonomy (0.229, p < 0.01; Model 3,).

To examine the influence of categorization autonomy on the usage 
intention (Hypothesis 3), we used regression models with robust stan-
dard errors, as shown in Table 4. Similar to the previous analyses, we 
first ran regression analysis using the continuous operationalization of 
categorization  autonomy  to  check  if  it  has  a  significant  effect  on  in-
tentions to use. Once we confirmed that there was a significant effect of 
categorization autonomy on intentions to use (0.362, p < 0.01; Model 
1), we then ran regression tests (after checking for normality of distri-
bution) to investigate which group orders showed the effect. From our 
analysis of the different subgroups (Models 2–4), H3 is corroborated in 
the  comparison  between  the  fixed  vs.  full  categorization  autonomy 
(0.359, p < 0.01; Model 2) and fixed vs. partial categorization autonomy 
(1.373, p < 0.01; Model 4).

Next, to study the mediating role of restrictiveness in the relationship 
between categorization autonomy and usage intentions (Hypothesis 4), 
we  tested  both  the  product  of  coefficients  (Sobel  test)  and  the  boot-
strapped confidence interval of the indirect effects (following Preacher 
and Hayes [48]). In the Sobel test, we checked if the indirect effect was 
significantly different from zero. The Sobel test assumes normality in the 
distribution of the indirect effect. Methodologists therefore recommend 
that it be supplemented with bootstrap confidence intervals, which do 
not make assumptions about the shape of the sampling distribution [48]. 
If the confidence intervals exclude zero, the indirect effect (i.e., medi-
ation) is considered meaningful. We therefore calculated bias-corrected 
and accelerated confidence intervals across 5000 bootstrap resamples.

Table 5 provides the coefficients and standard errors of the indirect, 
direct, and total effects of the mediated relationship between categori-
zation autonomy and usage intentions. The mediation analysis provides 
support for H4 for the two comparison groups fixed vs. full autonomy 
(0.482, p < 0.01, Sobel Test, 0.481 p < 0.01 Preacher and Hayes Test) 
and fixed vs. partial categorization autonomy (0.516, p < 0.01, Sobel 
Test  and  Preacher  and  Hayes  Test).  In  the  mediation  Table  4,  the  ‘a

Table 3 
Regression analysis for the moderation effect of task flexibility – Hypotheses 2.

Interaction Effects 
Outcome: Search 
Precision

Task Flexibility

Categorization

Autonomy (0 ¼
Fixed; 1 ¼ Partial; 
2 ¼ Full) * Task 
Specificity
Fixed vs. Full

Autonomy (0 ¼
Fixed; 1 ¼ Full) * 
Task Openness

Partial v. Full 
Autonomy 
(0 ¼ Partial; 1 ¼
Full) * Task 
Openness

Fixed vs. Partial 
Autonomy (0 ¼
Fixed; 1 ¼ Partial) * 
Task Openness

N
R-Sq

7

Model 2 
Coefficient 
(Standard 
Error)

(cid:0) 0.152 
(0.066)*

Model 3 
Coefficient 
(Standard 
Error)

(cid:0) 0.223 
(0.058)**

Model 4 
Coefficient 
(Standard 
Error)

(cid:0) 0.072 
(0.068)

Model 1 
Coefficient 
(Standard 
Error)

(cid:0) 0.179 
(0.059)**
0.079 
(0.035)*

0.161 
(0.069)*

0.229 
(0.062)**

(cid:0) 0.067 
(0.082)

201
0.0640

134
0.0734

132
0.1655

134
0.0394

---

<!-- PAGE 8 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Table 4 
Regression analysis for the effect on usage intentions – Hypothesis 3.

4. Post-hoc analyses

Outcome: 
Intention to Use

Categorization 
Autonomy 
(0 ¼ Fixed; 1 ¼
Partial; 2 ¼ Full)

Fixed vs. Full 
Autonomy 
(0 ¼ Fixed; 1 ¼
Full)

Partial v. Full 
Autonomy 
(0 ¼ Partial; 1 ¼
Full)

Fixed vs. Partial 
Autonomy 
(0 ¼ Fixed; 1 ¼
Partial)

N
R-Sq

** p < 0.01 * p < 0.05.

Model 2 
Coefficient 
(Standard 
Error)

Model 3 
Coefficient 
(Standard 
Error)

Model 4 
Coefficient 
(Standard 
Error)

Model 1 
Coefficient 
(Standard 
Error)

0.362  
(0.131)**

0.359 
(0.128)**

(cid:0) 0.653 
(0.225)

1.373  
(0.239)**

201
0.0383

134
0.0532

132
0.0580

134
0.1926

4.1. Heterogeneous treatment effect

The overarching premise of this paper is that the individuals’ mental 
models depend on their personal experiences, which results in signifi-
cant differences in how they categorize items. To test this premise and 
gain  a  deeper  understanding  of  the  differences  between  personalized 
categories created by participants in the treatment group (where they 
had categorization autonomy, and as a result, one could observe the full 
effects), we captured the vector representations of the product trees of 
each participant’s categorization scheme. Using vector representations 
[49,50],  one  can  compare  the  similarities  and  differences  between 
participants in the treatment group and investigate the antecedents to 
their differing product trees. The vector representations for two hypo-
thetical participants with five products are illustrated in Fig. 4.

In our analysis, the full vector representation is generated using all 
combinations  of  category  labels  created  by  the  65  treatment  partici-
pants4 and  the  NAMCE’s  scheme  (as  a  baseline  for  comparison). 
Adopting such a high-dimensional representation (each new combina-
tion of categories creates a new dimension) of the categorization trees is 
possible  in  our  sample  because  (a)  our  experiment  was  restricted  to

Table 5 
Analysis on the Mediation Effect of Restrictiveness on usage Intentions – Hypotheses 4.

Outcome: Intention to Use

a Coefficient

b 
Coefficient

Indirect Effect 
aXb

Direct Effect 
c’

Total Effect c

Sobel Test

Categorization Autonomy

(0 ¼ Fixed; 1 ¼ Partial; 2 ¼
Full)

Fixed vs. Full Autonomy

Partial v. Full Autonomy

Fixed vs. Partial Autonomy

** p < 0.01 * p < 0.05.

(cid:0) 0.698 (0.134) 
**

(cid:0) 0.561 (0.053) 
**

(cid:0) 0.697 (0.131) 
**
(cid:0) 0.424 
(0.277)
(cid:0) 0.970 (0.272) 
**

(cid:0) 0.691 (0.060) 
**
(cid:0) 0.405 
(0.062)**
(cid:0) 0.532 (0.061) 
**

0.391 
(0.084)**

0.482 
(0.099)**
0.172 
(0.115)
0.516  
(0.156)**

(cid:0) 0.029 
(0.108)

0.362 
(0.126)**

(cid:0) 0.122 
(0.101)
(cid:0) 0.826 
(0.200)**
0.857 (0.203) 
**

0.360 
(0.129)**
(cid:0) 0.654 
(0.227)
1.373 (0.241) 
**

0.391 
(0.084)**

0.482 
(0.099)**
0.172 
(0.115)
0.516 
(0.156)**

Preacher & 
Hayes

0.391 
(0.091)**

0.481 
(0.100)**
0.171 (0.114)

0.516 (0.171)**

coefficient’  represents  the  effect  of  categorization  autonomy  on 
restrictiveness  and  the  ‘b  coefficient’  represents  the  effect  of  restric-
tiveness and intention to use. We note that the effect of categorization 
autonomy  is  negative  and  significant  for  the  fixed  vs.  full  autonomy 
((cid:0) 0.697,  p  < 0.01)  and  the  fixed  vs.  partial  autonomy  ((cid:0) 0.970,  p  <
0.01)  comparisons.  Furthermore,  we  find  a  negative  and  significant 
relationship between restrictiveness and intentions to use across all our 
analyses (b coefficient). Lastly, in the case of the fixed categorization vs. 
full autonomy conditions, we observe a full mediation as the direct effect 
becomes insignificant in the presence of the mediator. For the fixed vs. 
partial categorization autonomy comparison, however, we observed a 
partial mediation.

Overall, we believe the benefits of categorization autonomy would 
be  best  realized  when  the  task  itself  is  free  of  prior  anchoring  biases 
(discussed earlier, referring to [3]). Considering that exploratory tasks 
have  more  open-ended  requirements,  categorization  autonomy  pro-
vided a more open and flexible means of navigation for users; hence, the 
moderating effect of Task Flexibility. Moreover, categorization auton-
omy  positively  impacts  usage  intentions,  particularly  when  users  are 
allowed to explore the categories and select items according to their own 
knowledge  and  expectations  with  greater  freedom.  A  more  elaborate 
behavioral research model regarding additional antecedents to adoption 
is presented in Appendix D.

creating a categorization tree of a maximum of three levels (e.g., Ap-
pliances  -  > Large  appliances  -  > Dishwashers  –  similar  to  NAMCE’s 
design) and (b) the number of leaf categories was limited to 78 items. To 
further reduce the number of possible combinations of categories, one of 
the authors analyzed the participant-created category names for syno-
nyms, and another evaluated the identified synonyms to ensure validity. 
During this exercise, category names that were found to mean the same 
concept (e.g., computer accessories and peripherals, or cell phone and 
mobile)  were  identified  as  equivalents.  Our  final  representation  was 
generated by evaluating all combinations of categories created by the 
participants in the treatment group, and the NAMCE category tree used 
for the control group comprised of 247 (category combinations; rows in 
Fig. 4) and 78 (leaf categories or products, columns in Fig. 4).

4.1.1. Analysis of the participants’ product category trees

The  vector  representation  of  the  product  category  tree  offers  the 
advantage  of  quantifying  and  comparing  the  similarities  (or  rather, 
dissimilarities) of category trees created by the participants in treatment 
conditions. Using vector representations, we studied how participants 
differ from each other by calculating the cosine similarities of the par-
ticipants’  category trees. We note that the participants’  category trees 
are  considerably  different  from  one  another,  with  a  maximum  cosine

4 We combined treatment subjects from both levels of task flexibility, since 
the  task  was  presented  after  the  categorization  trees  were  created,  and  the 
scenario had no effect on subjects at the creation stage.

8

---

<!-- PAGE 9 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Fig. 4. Vector Representation of Product Categorization Tree.

similarity of 0.58 between them. Further, we find that the participants’ 
self-defined category trees differ considerably from the baseline NAMCE 
category  tree,  having  a  mean  cosine  similarity  of  0.36.  The  findings 
support the premise that individuals tend to develop unique schematic 
representations based on prior experiences [3,31].

4.1.2. Antecedents to the differing expressions of the product category trees
Given the differences reported earlier, we investigated whether de-
mographic and personality traits of participants might have an influence 
on the cosine similarity measures of treatment users’  vector represen-
tations  of  self-defined  categories  and  NAMCE’s  schema.  As  a  major 
antecedent of the diversity of expression of individuals, literature points 
to  the  important  role  that  openness  to  experience  plays  in  divergent 
thinking  [51,52].  Specifically,  openness  is  one  of  the  key  personality 
traits that is necessary to produce new ideas [23]. In our experiment, 
openness was operationalized as the extent to which a person was open 
to experiences and their degree of creativity [42]. Along with openness, 
we also collected demographic information, including age, gender, in-
come,  and  level  of  education.  Table  6 provides  the  coefficients  and 
standard errors in estimating the cosine similarity of the participant’s 
category tree with the NAMCE category tree using the Ordinary Least 
Squares (OLS) regression model. Based on the analysis, we found that 
the  openness  factor  was  negative  and  significant  ((cid:0) 0.31,  p  < 0.05; 
Table  6).  This  confirms  prior  literature  suggesting  that  openness  is 
related to how diverse individual expressions are. In other words, this 
implies that users with higher levels of openness (as a personality trait), 
tend to create product categorization trees that are less similar to a pre- 
defined scheme created by the vendors. The other demographic factors 
did  not  have  a  significant  effect  on  the  dissimilarity  measure  of  self- 
defined categories to the baseline.

Table 6 
Demographics and (Dis)similarity with NAMCE as a baseline.

Dependent Variable: Cosine Similarity 
to NAMCE

Regression Coefficients (and 
Standard Errors)

Openness
Age
Gender
Income
Level of education
R-Sq
N

** p < 0.01 * p < 0.05.

(cid:0) 0.31* (0.14)
(cid:0) 0.147 (0.791)
0.560 (2.712)
(cid:0) 0.656 (0.935)
(cid:0) 0.258 (2.03)
0.103
65

9

4.2. Impact of time

We analyzed the effect of time spent on observing pre-defined cat-
egories, or creating self-defined categories (i.e., before the scenario was 
given)  in  both  conditions  of  task  flexibility  as  covariates  on  overall 
search  precision.  The  time  spent  on  observing  or  creating  categories 
(depending on condition) in the exploitive scenario had the p-value of 
0.984. Similarly, in the exploratory setting, the time spent on observing 
or creating categories had the p-value of 0.328 as a covariate on search 
precision. We conclude that the time spent before the tasks did not have 
a significant effect on performance. We also checked for the effect of 
time spent on creating or browsing categories (i.e., pre-task time) and 
the time spent on the task as covariates on usage intentions, and neither 
were significant (p = 0.483 and p = 0.363 respectively).

Comparing  the  actual  time  spent  on  the  experimental  task  (post- 
initial observation or creation of categories depending on condition), we 
found significant differences in both task types with the order of longest 
time spent by subjects in the partial categorization autonomy condition, 
then by the treatment (full categorization autonomy), and control (no 
autonomy).  Task  completion  time  could  be  considered  a  measure  of 
efficiency; however, since subjects were not instructed to finish the task 
as soon as possible, we do not necessarily consider the observed differ-
ence to indicate inefficiency.

5. Discussions and conclusion

We  studied  categorization  autonomy  as  a  design  principle  and 
explored its impact in terms of effective use, as well as usage intentions. 
While the primary focus and therefore the contribution of our research 
lies within the domains of Human-Computer Interaction (HCI) and De-
cision Support Systems (DSS), it also aligns with the components of a 
design theoretical model [53], as it defines a clear purpose – enhancing 
user decision-making through categorization autonomy – supported by 
theoretical  constructs  such  as  task  flexibility  and  effective  use.  The 
principles  of  form  and  function  are  reflected  in  hierarchical  categori-
zation trees, while the evaluation of performance and behavioral out-
comes  provides  testable  propositions.  The  design  is  grounded  in 
knowledge drawn from cognitive schema, cognitive fit, task-technology 
fit, and reactance theories.

Our study was set in the context of e-commerce, as the users access 
and  browse  large  amounts  of  information,  making  it  an  appropriate 
platform [10]. The benefits of categorization autonomy can be realized 
in other contexts and business domains as well. For example, YNAB (You 
Need a Budget), one of the most popular budgeting applications, offers

---

<!-- PAGE 10 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

users the autonomy to create and customize budget categories that align 
with  their  personal  financial  goals,  enabling  a  tailored  expense  man-
agement approach.5 This autonomy has generated user engagement, as 
evidenced by the r/YNAB subreddit, where thousands of members share 
their unique categorization strategies.6

Our findings provide strong empirical support for the positive impact 
of categorization autonomy on users’ search precision when compared 
to  fixed  categorization.  Furthermore,  the  moderating  effect  of  Task 
Flexibility  was  statistically  significant,  indicating  that  the  benefits  of 
categorization autonomy are more pronounced in tasks characterized by 
higher flexibility. We also included a mid-level condition with partial 
categorization autonomy, in order to rule out alternative explanations of 
learning effect (improving effective use) and extended interaction with 
an  interface  leading  to  more  favorable  perceptions  (e.g.,  intention  to 
use). Our  results were consistent  in that treatment (i.e., full categori-
zation autonomy) performed better than both fixed categorization and 
partial autonomy condition in terms of search precision. However, the 
difference between fixed and partial autonomy conditions was not sta-
tistically significant. This could indicate that offering partial autonomy 
at the lower levels (product level), may not provide the full benefits of 
categorization  autonomy, since  the  top  two category  levels  (from  the 
source) were not congruent with the users’ mental models.

We also examined the effect of categorization  autonomy on usage 
intentions, as well as the mediation effect of perceived restrictiveness on 
this relation. In the exploitive searches, we found the direct relationship 
of categorization autonomy on usage intentions (H3) to be statistically 
significant, so was the mediation effect of perceived restrictiveness (H4), 
particularly in the comparison between control and treatment (i.e., no 
categorization autonomy vs. full autonomy). In comparing the partial 
autonomy condition to full categorization autonomy, hypotheses H3 and 
H4  were  not  corroborated.  These  results  were  consistent  in  both 
exploitive  and  exploratory  searches.  The  summary  of  our  results  that 
were  corroborated or  rejected  are presented  in Table  7.  We conclude 
that  categorization  autonomy  leads  to  greater  search  precision  (i.e., 
objective  effective  use)  compared  to  conditions  with  partial  or  no 
categorization  autonomy.  The  impact  of  categorization  autonomy  on 
usage intentions is significant, particularly in comparison between fixed 
vs. full autonomy, or fixed vs. partial autonomy.

5.1. Implications

This paper contributes to categorization, schema theory, and human- 
computer  interaction  literature.  Categorization  research  has  mainly

Table 7 
Summary of results – corroborated and rejected hypotheses.

Hypothesis

Condition

H1 
Search 
Precision

H2 
Moderation 
by Task 
Flexibility

H3 
Intention 
to Use

H4 
Mediation by 
restrictiveness

Fixed

Yes

Yes

Yes

Yes

No

Yes

No

Yes

Categorization 
vs. Full 
Autonomy
Partial v. Full

Categorization 
Autonomy

Yes

Yes

Fixed

No

No

Categorization 
vs. Partial 
Autonomy

5 https://www.ynab.com/
6 https://www.reddit.com/r/ynab/

focused on creating categories that provide higher utility and cognitive 
economy  in  general  applications.  Our  findings  indicate  that  greater 
utility can be achieved in terms of higher search precision when users 
create  their  custom-made  categorization  trees  (i.e.,  the  “what”  and 
“how”). It is also in line with schema theory [3], which indicates that 
humans assimilate information better when they create mental models 
that are congruent with their experiences (i.e., the “why”) and enhance 
their  decision-making  [54].  The  post-hoc  analysis  illustrated  this 
distinction; specifically, the cosine similarities of the participants’ self- 
defined  categories  were  divergent  from  one  another  and  the  baseline 
(i.e.,  for  “whom”).  This  difference  could  partly  be  attributed  to  the 
openness character trait, which was a statistically significant determi-
nant  of  the  dissimilarity  of  the  individuals’  vector  representation 
matrices from the NAMCE baseline.

From the human-computer interaction perspectives, we investigated 
a novel data representation design in the form of categorization auton-
omy.  We  found  that  self-defined  categories  can  influence  important 
factors  such  as  perceptions  of  restrictiveness  and  intention  to  use. 
Moreover, we found the nature of the task to be a determining factor in 
the  effect,  with  the  difference  being  more  prominent  in  higher  task 
flexibility  or  exploratory  searches  (i.e.,  “when”).  One  explanation  for 
this finding might reside in the fact that creating individualized cate-
gories engages one’s brain in an exploratory mindset.

Prior research has also studied eye-tracking movements in the two 
scenarios of exploration and exploitation and found that participants in 
the exploratory task demonstrated greater amounts of decision-making 
creativity  [55].  Similarly,  in  our  experiment,  the  greater  freedom 
offered by categorization autonomy could be a reason that task flexi-
bility had a significant moderating effect on search precision. Moreover, 
our  findings  contribute  to  the  ongoing  refinement  of  Cognitive  Fit 
Theory within the DSS literature. It has been argued that fit is not merely 
a  function  of  task-structure  alignment  but  may  also  reflect  adaptive 
mechanisms and user-level strategies [56]. In line with this, we find that 
categorization autonomy can support decision effectiveness when users 
are given the flexibility to tailor information structures to their goals. 
However, consistent with prior work (e.g., [34]), our results suggest that 
fit is sensitive to task framing and user involvement.

From practitioners’  perspective, this research shows how categori-
zation autonomy can benefit a platform used by general users, such as e- 
commerce.  Categorization  autonomy  would  enable  users  to  find  the 
items  they  are  looking  for  more  accurately.  Additionally,  by  offering 
categorization autonomy on a website, an organization might improve 
key  consumer  behavior  factors  such  as  intention  to  use.  While  our 
findings show that categorization autonomy improves both search pre-
cision and behavioral intentions, we recognize that these effects may not 
directly translate into real-world adoption. In practice, factors such as 
user  learning  curves,  training  demands,  organizational  resistance  to 
change, and integration with existing workflows can all impact adoption 
outcomes [57]. These issues are beyond the scope of our study, but they 
represent  important  considerations  for  practitioners  evaluating  the 
viability of categorization autonomy in live systems.

Our  recommendation  for  websites  is  to  give  users  the  option  to 
choose between self-defined and pre-defined categorization and inform 
them  of  the  benefits  of  categorization  autonomy.  Further,  since  the 
openness  trait  of  individuals  is  positively  correlated  to  the  extent  to 
which they may differ in the way they categorize product trees (Table 6, 
supported by [52]), platforms catering to a more open psychographic 
profile  may  benefit  more  from  offering  categorization  autonomy. 
However, even as this research aims to demonstrate how categorization 
autonomy  could  be  beneficial,  we  acknowledge  the  utilities  that  pre- 
defined categorization might offer. First of all, pre-defined categoriza-
tion  provides  cognitive  economy.  Even  if  a  schema  created  by  the 
developer might not be fully congruent with the users’ mental models, it 
is still easier to comprehend than viewing a list of all categories in a short 
period of time. Moreover, creating personalized categorization schemes 
can  be  quite  time-consuming.  For  one-time  shoppers  from  a  given  e-

10

---

<!-- PAGE 11 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

commerce  website,  this  may  not  be  a  valuable  time  investment.  The 
benefits of creating personalized categories are best realized for return 
customers and frequent shoppers on a given platform. We also note that 
a  one-size-fits-all  approach  is  not  the  best  solution.  In  other  words, 
forcing all users to create their own categories may not have a univer-
sally beneficial effect. Similarly, a prior study found that Intel’s verbal 
advisor that increased successful downloads by 27 % was “not for every 
customer.  Less  verbal  and  more  analytic  customers  found  the  verbal 
advisor annoying and preferred a more graphic list” [2 ,p. 202]. Hence, 
we suggest that both options of full categorization autonomy and pre- 
defined schemes be offered and the choice be left to the users.

Lastly,  on  many  e-commerce  platforms,  shoppers  use  the  search 
function to find the items they are looking for (e.g., an HDMI cable, or a 
phone  charger).  We  argue  that  such  a  task  is  more  in  line  with  the 
exploitation search type. In cases where a person is deciding on how to 
use a gift card they received, for example, they might browse through 
the  product  trees, and  that  exploration could  benefit  most  from cate-
gorization autonomy.

5.2. Limitations

Prior research points to the varying levels of exploration requiring 
different levels of creativity [55]. In our study, the tasks were simplified 
and thus, did not fully capture the whole spectrum of information re-
quirements. Tasks entailing more rigid frameworks, as well as objectives 
with  greater  levels  of  exploration  freedom  can  be  examined  in  the 
future.

This research was conducted on an experimental website. While it 
allowed us to investigate the effects, we realize that real-world settings 
might yield different results for behavioral intentions - academic pro-
jects  such  as  ours  may  never  be  able  to  capture  the  ramifications  of 
spending actual money on real products. Moreover, in real-world cases, 
users (of e-commerce or organizational systems) tend to interact with a 
given system over a continued period of time – as opposed to our study 
where users spent one hour interacting with the system on average. A 
longitudinal study could offer additional insights on interactions with a 
system that offers categorization autonomy. Furthermore, while our use 
of  Cognitive  Fit  Theory  helps  explain  performance  differences  in  the 
short term, we acknowledge that cognitive fit may evolve over extended 
usage. Factors such as learning, adaptation, or user fatigue could alter 
how  well  a  system  aligns  with  a  user’s  cognitive  style over  time.  We 
therefore apply CFT specifically in the context of immediate system use 
and  recognize  that  longer-term  cognitive  alignment  remains  an  open 
area for future investigation. We also cannot rule out the possibility that 
perceived  effort  or  user  investment  may  have  contributed  to  the 
observed  effects  on  performance  of  users  with  full  categorization  au-
tonomy.  Although,  the  results  from  the  partial  autonomy  condition 
could offer support that the improved search precision and higher usage 
intentions were not only the result of effort and time investment with the 
interface.

5.3. Future research

be  interesting  to  study  the  differences  in  cognitive  load  by  observing 
brain activity using fMRI  and electroencephalography (EEG)  tools, or 
tracking eye movements.

We believe the benefits of categorization autonomy can be realized 
in  contexts  other  than  e-commerce  as  well.  For  example,  users  of 
banking applications could benefit from control over how expenses are 
categorized (e.g., ‘car insurance’ along with ‘health insurance’ under the 
category of ‘insurances’, or grouped next to ‘fuel expenses’  and  ‘road 
taxes’  under  ‘transportation’  or  ‘car  ownership’  categories).  Future 
research  might  also  involve  different  product  types  (e.g.,  specialized 
items such as a hydraulic pump for a production facility versus a com-
modity  like  a  carton  of  milk)  to  see  if  users’  prior  expertise  and 
knowledge  in  the  subject  area  could  impact  their  interactions  with  a 
system  that  offers  categorization  autonomy.  Studying  the  impact  of 
categorization autonomy in high-stakes or expertise-driven domains – 
where, in certain circumstances, it could even be counterproductive – is 
certainly  an  interesting  topic  for  future  research.  In  fact,  one  could 
explore  the  trade-off  between  user  autonomy  and  system-imposed 
structure, and how each may enhance or hinder performance, particu-
larly in contexts with varying levels of task flexibility (routine or closed 
vs. creative or open) and task complexity (low vs. high expertise). Based 
on task demands, hybrid architectures could also be considered, where 
user-defined  and  system-generated  categorization  approaches  are 
effectively  combined  in  response  to  user  characteristics  and  task 
requirements.

Moreover,  scholars  could  examine  users’  willingness  to  engage  in 
categorization  for  subjects  with  varying  degrees  of  attachment  to  a 
system (i.e., new users versus veterans), what the barriers are, and in 
what factors may contribute to their long-term usage of categorization 
autonomy.

Our post-hoc analysis shows that the openness personality trait can 
determine how divergent the individuals’ categorization trees are from 
the  baseline.  Identifying  additional  antecedents  that  may  influence 
users’ categorization scheme could be a direction for future research.

Another area for continuing this research program might lie within 
understanding how individuals create categories. Our work was based 
on  analyzing  the  ‘product’  of  a  user’s  categorization  activity.  Future 
studies on the process itself, by collecting clickstream data for example, 
could shed more light on the intricacies of the cognitive categorization 
process.

CRediT authorship contribution statement

Arash Saghafi: Writing – review & editing, Writing – original draft, 
Validation,  Supervision,  Methodology,  Investigation,  Formal  analysis, 
Data  curation,  Conceptualization.  Poonacha  Medappa:  Writing  –  re-
view  &  editing,  Writing  –  original  draft,  Validation,  Methodology, 
Investigation,  Data  curation,  Conceptualization.  Ariton  Debrliev: 
Writing 
curation, 
Conceptualization.

draft,  Methodology,  Data

original

–

There  are  several  points  of  further  research  opportunities  that  we 
wish to indicate. First and foremost, additional studies are required to 
understand  the  deeper  cognitive  differences  between  exploratory  and 
exploitive searches when the users create their own categories. It would

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

Declaration of competing interest

11

---

<!-- PAGE 12 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

Appendix A. Scale items

Table A1 
Survey Questions - Adapted from [37].

1: I had limited control over the way the presented information was categorized.
2: In terms of my preferred way of viewing the information, the categorization was confined.
3: In terms of my preferred way of viewing the information, the categories were restricted.
4: Next time I need to perform such tasks, I would like to use this kind of categorization
5: Assuming I had access to the provided categorization, I would use this website again in the future.
6: Given I had access to the categorization offered by this site, I would use it to perform such tasks if needed.
QTrap: If you are reading this, please answer ‘somewhat disagree’

Appendix B. Validity and robustness

Table B1 
Validity and Reliability of Constructs.

Item

Intention to use 1
Intention to use 2
Intention to use 3
Restrictiveness 1
Restrictiveness 2
Restrictiveness 3

Intention to use

Restrictiveness

0.963
0.972
0.959

0.896
0.900
0.948

Table B2 
Reliability and convergent validity.

Cronbach’s Alpha

Average Variance Extracted

Intention to use
Restrictiveness

0.962
0.902

0.930
0.837

Table B3 
Discriminant validity – heterotrait-monotrait ratio.

Categorization

Intention to use

Restrictiveness

Categorization
Intention to use

Restrictiveness

0.333

0.596

0.776

Appendix C. Scenarios

Information Exploitation Scenario:
Imagine you are an office manager tasked with purchasing the following items:

- Two new monitors for the office workers. The office needs a 24″ monitor and a 27″ monitor. 
- The office microwave is broken! Find a microwave cheaper than $700 with at least 2-cubic foot of space. 
- Please buy a corded Motorola brand phone with cordless handset. 
- For calls from your PC you are supposed to buy an on-ear headphone with a visible microphone. 
- A cellphone power bank. 
- Finally, please find a pencil sharpener.

Information Exploration Scenario:
Suppose you are buying three distinct gifts for your best friend’s wedding to satisfy the following three criteria:

You know that one of the newlyweds is a cooking enthusiast, you also know that both of them are very active and enjoy 
outdoor activities. In addition, you know that they love watching movies at home.

Appendix D. (Behavioral Data)

To extend our understanding of the consequences of categorization autonomy, we developed a set of hypotheses linking autonomy to users’ 
satisfaction, trust, and intentions to use the system. Hypothesis 5 posits that categorization autonomy increases user satisfaction, as the ability to 
impose one’s own organizational logic enhances cognitive alignment and perceived control. Hypothesis 6 proposes that this relationship is mediated

12

---

<!-- PAGE 13 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

by trust, such that autonomy fosters trust in the system, which in turn drives satisfaction. And, Hypothesis 7 suggests that greater satisfaction leads to 
higher intentions to use the system, consistent with existing models of IS success and technology adoption. Fig. D-1 illustrates the research model with 
only the subjective variables (i.e., excluding H1 and H2, namely, Search Precision and Task Flexibility’s moderation effect).

Fig. D-1. Behavioral research model.

The results offer strong support for all three hypotheses. H5 was supported, with categorization autonomy significantly increasing satisfaction (β =
0.323, p = 0.009). For H6, we found that categorization autonomy significantly increased trust (β = 0.347, p = 0.001), and that trust strongly predicted 
satisfaction (β  = 0.858, p < 0.001), fully mediating the direct effect of autonomy (which became non-significant when trust was included). This 
provides evidence for full mediation, supporting H6. Finally, H7 was also strongly supported, as satisfaction emerged as a robust predictor of usage 
intentions (β = 0.935, p < 0.001). Collectively, these findings reinforce the role of categorization autonomy not only in improving task performance, 
but also in enhancing users’ affective and behavioral responses to the system through mechanisms of trust and satisfaction. Table D-1 offers the full 
statistical analysis using regression.

Table D1 
Regression analysis on additional behavioral hypotheses.

Hypothesis

Path

H5
H6

H7

Categorization Autonomy - > Satisfaction
Categorization Autonomy - > Trust
Trust - > Satisfaction (with Autonomy)
Categorization Autonomy - > Satisfaction (+ Trust)
Satisfaction - > Usage Intentions

Beta 
(Unstandardized)

p-value

Supported

0.323
0.346
0.858
0.026
0.935

0.009
0.001
0
0.775
0

Yes
Yes
Yes
No (Full Mediation)
Yes

Data availability

Data will be made available on request.

References

[1] P. Zhang, F.F.H. Nah, I. Benbasat, Human-computer interaction research in 
management information systems, J. Manag. Inf. Syst. 22 (2005) 9–14.

[2] J. Hauser, G. Urban, G. Liberali, M. Braun, Website morphing, Mark. Sci. 28 (2009)

202–223.

[3] S. Derry, Cognitive schema theory in the constructivist debate, Educ. Psychol. 31

(1996) 163–174.

[4] J. Parsons, Y. Wand, Using cognitive principles to guide classification in

information systems modeling, MIS Q. 32 (2008) 839–868.

[5] J. Smith, Prototypes, exemplars, and the natural history of categorization, Psychon.

Bull. Rev. 21 (2013) 312–333.

[12] S. Kodali, S. Compton, Must-Have E-Commerce Features, Roadmap Report,

Forrester Research, 2022.

[13] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives

on strategy selection, Inf. Syst. Res. 10 (1999) 356–374.

[14] R. Lukyanenko, J. Parsons, Y.F. Wiersma, The IQ of the crowd: understanding and 
improving information quality in structured user-generated content, Inf. Syst. Res. 
25 (2014) 669–689.

[15] R. Lukyanenko, J. Parsons, Y. Wiersma, M. Maddah, Expecting the unexpected:

effects of data collection design choices on the quality of crowdsourced user- 
generated content, MIS Q. 43 (2019) 623–647.

[16] A. Saghafi, Y. Wand, J. Parsons, Skipping class: improving human-driven data

exploration and querying through instances, Eur. J. Inf. Syst. 31 (2022) 463–491.
[17] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline,

Decis. Support. Syst. 44 (2008) 657–672.

[18] J. March, Exploration and exploitation in organizational learning, Organ. Sci. 2

(1991) 71–87.

[19] A. Burton-Jones, D.W. Straub, Reconceptualizing system usage: an approach and

empirical test, Inf. Syst. Res. 17 (2006) 228–246.

[6] G. Lakoff, Women, Fire, and Dangerous Things: What Categories Reveal about the

[20] A. Burton-Jones, C. Grange, From use to effective use: a representation theory

Mind, University of Chicago Press, Chicago, 2008.

[7] J. Parsons, Y. Wand, Emancipating instances from the tyranny of classes in 
information modeling, ACM Transac. on Database Syst. (TODS) 25 (2000) 
228–268.

perspective, Inf. Syst. Res. 24 (2013) 632–658.

[21] A. Fishbach, M.J. Ferguson, The goal construct in social psychology, in: A.

W. Kruglanski, E.T. Higgins (Eds.), Social Psychology: Handbook of Basic 
Principles, 2nd ed., Guilford, New York, 2007, pp. 490–515.

[8] A.D. Moore, Python GUI Programming with Tkinter: Design and Build Functional

[22] K.R. Larsen, A taxonomy of antecedents of information systems success: variable

and User-Friendly GUI Applications, Packt Publishing, Birmingham, 2021.

[9] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, 
present, and future of decision support technology, Decis. Support. Syst. 33 (2002) 
111–126.

[10] S. Al-Natour, I. Benbasat, R.T. Cenfetelli, The effects of process and outcome

similarity on users’ evaluations of decision aids, Decis. Sci. 39 (2008) 175–211.

[11] W. Kosinski, G. Dziczkowski, B. Gol´enia, K. Wegrzyn-Wolska, Towards an Optimal 
Decision Support System, in: Decision Support Systems, Advances in, IntechOpen, 
2010.

analysis studies, J. Manag. Inf. Syst. 20 (2003) 169–246.

[23] A. Taylor, H.R. Greve, Superman or the fantastic four? Knowledge combination and

experience in innovative teams, Acad. Manag. J. 49 (2006) 723–740.

[24] Jenkins J.L., Denison A., Valacich J.S., Wilson D., Detecting goal-oriented vs. 
browsing users through behavior analysis, in: 2023 46th MIPRO ICT and 
electronics convention (MIPRO), IEEE, 2023, pp. 13–18.

[25] R. Budiu, Search Is Not Enough: Synergy between Navigation and Search, Nielsen

Norman Group, 2014.

13

---

<!-- PAGE 14 -->

A. Saghafi et al.

Decision Support Systems 196 (2025) 114499

[26] X. Liu, K. Werder, A. Maedche, Novice digital service designers’ decision-making 
with decision aids—a comparison of taxonomy and tags, Decis. Support. Syst. 137 
(2020) 113367.

[27] Z. Kozareva, Everyone likes shopping! Multi-class product categorization for e- 
commerce, in: Conference of the North American Chapter of the Association for 
Computational Linguistics, 2015, pp. 1329–1333.

[28] D. Romanov, V. Molokanov, N. Kazantsev, A.K. Jha, Removing order effects from 
human-classified datasets: a machine learning method to improve decision making 
systems, Decis. Support. Syst. 165 (2023) 113891.

[48] K.J. Preacher, A.F. Hayes, Assessing mediation in communication research, in: A. 
F. Hayes, M.D. Slater, L.B. Snyder (Eds.), The Sage Sourcebook of Advanced Data 
Analysis Methods for Communication Research, Sage, Thousand Oaks, 2008, 
pp. 13–54.

[49] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, J. Dean, Distributed representations 
of words and phrases and their compositionality, Adv. Neural Inf. Proces. Syst. 26 
(2013).

[50] Y.-L. Chen, C.-H. Hsiao, C.-C. Wu, An ensemble model for link prediction based on

graph embedding, Decis. Support. Syst. 157 (2022) 113753.

[29] A. Castellanos, M.C. Tremblay, R. Lukyanenko, B. Samuel, Basic classes in

[51] R.R. McCrae, Creativity, divergent thinking, and openness to experience, J. Pers.

conceptual modeling: Theory and practical guidelines, J. Associ Inform. Syst. 21 
(2020) 1001–1044.

[30] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases,

Science 185 (1974) 1124–1131.

Soc. Psychol. 52 (1987) 1258–1265.

[52] S.M.B. Thatcher, S.A. Brown, Individual creativity in teams: the importance of

communication media mix, Decis. Support. Syst. 49 (2010) 290–300.

[53] S. Gregor, D. Jones, The anatomy of a design theory, J. Assoc. Inf. Syst. 8 (2007)

[31] G. Chapman, E. Johnson, The limits of anchoring, J. Behav. Decis. Mak. 7 (1994)

312–335.

223–242.

[32] I. Vessey, Cognitive fit: a theory-based analysis of the graphs versus tables

literature, Decis. Sci. 22 (1991) 219–240.

[54] H.Y. Hung, Y. Hu, N. Lee, H.T. Tsai, Exploring online consumer review-

management response dynamics: a heuristic-systematic perspective, Decis. 
Support. Syst. 177 (2024) 114087.

[33] P. Xu, L. Chen, R. Santhanam, Will video be the next generation of e-commerce

[55] E. Choi, C. Kim, K. Lee, Consumer decision-making creativity and its relation to

product reviews? Presentation format and the role of product type, Decis. Support. 
Syst. 73 (2015) 85–96.

[34] D. Baˇci´c, R. Henry, Advancing our understanding and assessment of cognitive

effort in the cognitive fit theory and data visualization context: eye tracking-based 
approach, Decis. Support. Syst. 163 (2022) 113862.

exploitation–exploration activities: eye-tracking approach, Front. Psychol. 12 
(2021) 3629.

[56] S. Bina, T. Kaskela, D.R. Jones, E. Walden, W.B. Graue, Incorporating evolutionary 
adaptions into the cognitive fit model for data visualization, Decis. Support. Syst. 
171 (2023) 113979.

[35] D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance,

[57] J.T. Gourville, The curse of innovation: a theory of why innovative new products

MIS Q. 19 (1995) 213–236.

fail in the marketplace, HBS Marketing Research Paper (2005) 05–06.

[36] M. Silver, User perceptions of decision support system restrictiveness: an

experiment, J. Manag. Inf. Syst. 5 (1988) 51–65.

[37] W. Wang, I. Benbasat, Interactive decision aids for consumer decision making in e- 
commerce: influence of perceived strategy restrictiveness, MIS Q. 33 (2009) 
293–320.

[38] J.W. Brehm, A Theory of Psychological Reactance, Academic Press, New York,

1966.

[39] S. Ebrahimi, M. Ghasemaghaei, I. Benbasat, The impact of trust and 
recommendation quality on adopting interactive and non-interactive 
recommendation agents: a meta-analysis, J. Manag. Inf. Syst. 39 (2022) 733–764.
[40] A. Dafoe, B. Zhang, D. Caughey, Information equivalence in survey experiments,

Polit. Anal. 26 (2018) 399–416.

[41] L.T. Benjamin Jr., Lecturing, in: S.F. Davis, W. Buskist (Eds.), The Teaching of

Psychology: Essays in Honor of W.J. McKeachie and C.L, Brewer, Lawrence 
Erlbaum, Mahwah, 2002, pp. 57–67.

[42] T.J. Brown, J.C. Mowen, D.T. Donavan, J.W. Licata, The customer orientation of 
service workers: personality trait effects on self and supervisor performance 
ratings, J. Mark. Res. 39 (2002) 110–119.

[43] E. Peer, G. Paolacci, J. Chandler, P. Mueller, Screening participants from previous

studies on Amazon mechanical Turk and Qualtrics, SSRN E-J (2012) 1–5.

[44] S. Sudman, Applied Sampling, Academic Press, New York, 1976.
[45] J. Cortina, What is coefficient alpha? An examination of theory and applications,

J. Appl. Psychol. 78 (1993) 98–104.

[46] C. Fornell, D. Larcker, Evaluating structural equation models with unobservable

variables and measurement error, J. Mark. Res. 18 (1981) 39–50.

[47] A. Burton-Jones, P.N. Meso, Conceptualizing systems for understanding: an

empirical test of decomposition principles in object-oriented analysis, Inf. Syst. 
Res. 17 (2006) 38–60.

Arash Saghafi is an Assistant Professor of Information Systems at Ted Rogers School of 
Management,  Toronto  Metropolitan  University.  His  degrees  include  a  BSc  in  Software 
Engineering from Sharif University of Technology, and MM, MScB, and PhD from Uni-
versity of British Columbia. He was appointed as a lecturer and research fellow at Sauder 
School of Business, and an Assistant Professor at Tilburg School of Economics and Man-
agement prior to joining Toronto Metropolitan University. His research has focused on 
information  and  knowledge  representation,  application  of  ontology  in  conceptual 
modeling, systems development methodologies, and empirical evaluation of design arti-
facts.  His  work  has  been  published  at  the  European  Journal  of  Information  Systems, 
Journal of Database Management, and proceedings of various AIS conferences.

Poonacha Medappa is an Assistant Professor in the Information Management group at the 
Department of Management at Tilburg University. Prior to joining Tilburg University, he 
completed his Ph.D in Information Systems from HEC Paris. His research interests lie in the 
areas  of  project  management,  open-source  software  development,  online  communities, 
and methodological applications of machine learning techniques in research. His research 
has been published in top-tier journals such as Information Systems Research, European 
Journal of Information Systems and in the proceedings of several leading conferences.

Ariton Debrliev is a consultant at Gartner. He has a BSc in Business Administration and 
MSc in Marketing Management from the Erasmus University, Rotterdam School of Man-
agement, and a MSc in Information Management from Tilburg University, TiSEM. Main 
research  interest  areas  include:  consumer  behavior,  decision-making,  heuristics  and 
biases.

14

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Decision Support Systems 196 (2025) 114499
Contents lists available at ScienceDirect
Decision Support Systems
journal homepage: www.elsevier.com/locate/dss
Impact of categorization autonomy on effective use and adoption intentions
Arash Saghafia,*, Poonacha Medappab, Ariton Debrlievc
aTed Rogers School of Management, Toronto Metropolitan University, 55 Dundas St W., Toronto, ON M5G 2C3, Canada
bTilburg School of Economics and Management, Tilburg University, 5037, AB, Tilburg, the Netherlands
cGartner Nederland B.V., De Entree 79, 1101 BH, Amsterdam, the Netherlands
A R T I C L E I N F O A B S T R A C T
Keywords: Category tree view is an omnipresent element in graphical user interfaces where it captures information in terms
Categorization of a hierarchical structure. These categorization trees facilitate human users’ cognitive economy and decision-
Autonomy making. While previous research has investigated the utilities of using unstructured data compared to pre-
Cognitive schema theory
categorized information by business users, the effectiveness of allowing users the autonomy to create their
Restrictiveness
own categorization hierarchies from generic object types remains unexplored. This paper evaluates the benefits
HCI
of categorization autonomy in terms of search precision, as an objective measure, as well as subjective intentions
to use the system. We examined users’ interactions with a platform in information seeking tasks with 201
subjects. Our findings indicate that categorization autonomy leads to superior results, both in terms of effective
use and behavioral perceptions. We also found that the impact of categorization autonomy is moderated by task
flexibility, such that the benefits are more apparent in tasks that necessitate open-ended search approaches. By
focusing on how user-driven categorization influences system interaction, our study contributes to the design of
decision support systems that are better aligned with users’ cognitive structures and task demands.
1. Introduction to how items are grouped and presented on almost every user interface
[8], whether in Decision Support Systems (DSS), online banking, in-
The field of human-computer interaction (HCI) has studied different ventory management systems, or e-commerce. In particular, focusing on
designs of computer systems and analyzed the interactions between improving the decision-making process through the development and
human users and technology with the aim of improving the means of evaluation of systems that provide users with enhanced information and
attaining the systems’ goals [1]. Research has shown that designs that support is central to the design of effective decision support systems [9].
“match the preferences and information needs of [users] are efficient; From a DSS perspective, categorization tools function as cognitive sup-
those that do not, forgo potential profit” [2,p. 202]. For example, when port mechanisms that assist users in identifying relevant information.
Intel implemented a verbal advisor to help customers find the relevant Design decisions that shape this structuring – such as granting or
software, successful downloads increased by 27 % [2]. Thus, allowing restricting autonomy – could therefore impact the effectiveness of de-
users to choose a design that matches their cognitive style would be cision support.
advantageous to a singular interface design. In this work, we study the effect of categorization autonomy, defined
One design choice that determines the efficiency of information as the extent to which users have the ability to define their own cate-
assimilation [3] and enables a better cognitive fit with the preferences gorization schemes from a base level of object types. In order to feasibly
and needs of users is related to how data is categorized and presented to examine the impact of categorization autonomy, we chose to focus on e-
users. Categories reflect repeating patterns of properties [4], and cate- commerce, since users of such platforms access large amounts of infor-
gorization is the ability to detect recurring characteristics of phenomena mation without the need for prior technical training [10] – making it an
[5]. Categories aid humans with the processing of information in a appropriate setting to study how users’ internal categorization mecha-
cognitively economical manner [6]. In information systems, category nisms can be best utilized in processing information and making accu-
trees are widely used to provide users with the same utilities of rate decisions [11]. Although other applications such as content
abstraction from the way the information in databases is organized [7], management systems or organizational resource planning systems could
* Corresponding author.
E-mail addresses: saghafi@torontomu.ca(A. Saghafi), p.k.medappa@tilburguniversity.edu(P. Medappa), ariton.debrliev@gartner.com(A. Debrliev).
https://doi.org/10.1016/j.dss.2025.114499
Received 22 October 2024; Received in revised form 16 June 2025; Accepted 24 June 2025
Available online 25 June 2025
0167-9236/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
have been fitting contexts to study the benefits of categorization au- assessed in terms of the performance of an observable behavior [20]. In
tonomy, we believe that the accessibility offered by e-commerce plat- this paper, we set out to evaluate the efficacy of categorization auton-
forms justifies the choice. While we are not limiting our contributions to omy from both perspectives of objective performance as well as sub-
the e-commerce context, we acknowledge that pre-defined categoriza- jective intentions to use the system given the chance. The objective and
tion trees are considered “must-have” design elements in many in- subjective analysis is further motivated by the multidimensional nature
terfaces [12]; however, not exploring a new design that potentially of Information Systems (IS) success [22]. Demonstrating that categori-
provides a better fit with the cognitive styles of users is akin to forgoing zation autonomy not only helps in the attainment of usage goals (i.e.,
profit [2]. Furthermore, DSS research has long emphasized the impor- objective measure), but also leads to higher subjective perceptions,
tance of adaptive system features that support decision quality across a provides strong support for its efficacy as a viable design.
variety of user profiles and task contexts [13]. Categorization autonomy To study the potential benefits of categorization autonomy, we
aligns with this principle by enabling the system to better fit the needs of conducted an online laboratory experiment with a total of 201 subjects
individual users. who were surrogates of actual online shoppers. We developed an
Prior research on human users’ interaction with data categorization experimental website using data scraped from a major North American
includes studies on usage of non-classified data (or instance-based), e-retailer (with annual revenue of more than US$50 billion) offering
where only things and their attributes are recorded devoid of pre- subjects the same level of product information as a typical e-commerce
defined structures [7]. Namely, it was shown that content generators platform. Based on random assignment of subjects to three levels of
on a citizen science platform were able to provide higher quality data categorization autonomy (i.e., no autonomy as in the source website,
when they had the option to record their observations free of classifi- partial autonomy, and full autonomy), we found that online shoppers
cation [14,15]. From a different perspective, content consumers in a who defined their own product category trees were able to search for
self-service business intelligence setting were able to write more accu- products more accurately in both closed and open-ended searches.
rate queries and identify higher quality patterns when they had access to Furthermore, task flexibility was also found to demonstrate a significant
non-classified data versus class-based data [16]. moderating effect, indicating that the effect of categorization autonomy
We believe one potential solution that offers individuals the ability to is indeed stronger for tasks with higher flexibility (i.e., exploratory
reap the benefits of categorization in decision-making, while also tasks). The behavioral usage intentions were also positively improved
providing a better fit between the categorization scheme and the in- for users who had full categorization autonomy. Advantageous results in
dividual’s information needs, is to allow them to define their own both objective and subjective metrics for categorization autonomy
categorization hierarchies (rather than stripping data of all categoriza- provide strong evidence for the effectiveness of this design. We also
tion/classification, which distinguishes our work from previous efforts). performed a post-hoc analysis to understand the differences between
In fact, our premise is that the most effective categorization scheme varies individuals’ self-defined categories and their variations from the base-
substantially across users due to their unique ways of assimilating in- line of the e-retailer’s pre-defined scheme. Our findings indicated that
formation [3]. To the best of our knowledge, providing autonomy to individualized categories were indeed dissimilar from one another and
general users in creating customized categorizations based on similarity the e-retailer’s – corroborating that users assimilate information differ-
of existing lower-level categories or object types in an inclusive setting, ently [3]. The differences from the baseline were significantly stronger
such as e-commerce, has not been studied before. This notion resonates for users who demonstrated greater levels of the openness personality
with DSS literature on user-driven modeling and tailoring of information trait, which is associated with the generation of novel ideas and crea-
structures [17], which suggests that empowering users to organize in- tivity [23].
formation according to their decision logic can lead to better system
outcomes. 2. Conceptual development
Rooted in March’s [18] learning taxonomy, “two types of system
usage can drive individual task performance: exploitation and explora- Categories help human users process information more efficiently,
tion” [19,p. 236]. Hence, in order to conduct a comprehensive investi- and in information systems, they are used in various settings from
gation of how categorization autonomy could be used in practice, we database organization [7] to grouping products on e-commerce plat-
follow this taxonomy in our study design. In the context of online forms, aiding shoppers in navigating options. Categorization trees are
searches on an e-commerce platform, exploitation corresponds to considered one of the “core elements of a retail e-commerce website”
searches where users pursue well-defined goals by following a closed [24,p. 2]. Their importance is highlighted beyond just website search
and structured approach (e.g., searching for a 16-gigabyte USB storage), functions, noting that effective searches require knowledge of the
whereas exploration involves searches characterized by greater vari- domain to input the right keywords [25]. Even with some domain
ability and openness in the search process (e.g., browsing for Christmas expertise, users might favor browsing categories for a more compre-
gifts for friends and family). In this paper, we capture the two modes of hensive overview, especially on platforms with less effective search
system usage with the Task Flexibility concept – defined as the extent to engines than Google. In decision support systems, also, taxonomies have
which a task allows for multiple ways of achieving the desired outcome. been shown as effective decision support aids, particularly for non-
Tasks with low flexibility align with exploitation, where users follow a expert users [26]. Moreover, even a knowledgeable user still needs
predetermined and closed-ended path. Conversely, tasks with high good querying skills for efficient searches, as certain terms lead to better
flexibility encourage open-ended questioning and variability. results [25] (e.g., “romantic comedy” over “funny movie for a date”).
Considering the usage types, we examine the impact of categoriza- Thus, categorization trees are indeed valuable features for users with
tion autonomy from an objective usage effectiveness perspective in average domain familiarity and querying skills. Offering improvements
terms of users’ ability to fulfill a certain usage goal, in line with the to the categorization tool could increase the utility of this design feature
definition of effective use [20], as well as subjective behavioral percep- even further.
tions. System Use has been described in terms of a user, system, and task, Prior categorization research in Information Systems has discussed
and defined a task as a “goal-directed activity” [19 ,p. 231]. Further, human users’ ability to create and interpret categories.1The stream that
system use and effective use can be distinguished from one another by
emphasizing on the performance of “a goal-directed activity to using it
in a way that helps attain the relevant goal” [20,p. 633], instead of just 1 Automation of categorization is also discussed in the literature (e.g.,
being simply able to use the system. With a goal as a “cognitive repre- [27,28]), however, the database design (by humans or machine) is beyond our
sentation of a desired end-point” [21,p. 491], it is assumed that goal- scope as our focus is on the individual content consumer who uses the cate-
attainment has objective qualities, which can be operationally gorization scheme for their own individual use.
2

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
studies humans’ decisions with regards to creating categorization pre- would have used different memory objects and patterns than the ones a
scribes how basic classes can be identified by a system’s designer in given end-user is familiar with. This could result in an incongruent
order to create better interfaces (e.g., [29]), but that perspective is product tree for the user, leading to inefficiencies in using it.
beyond our scope as it takes the point of view of a designer rather than From a different perspective, Tversky and Kahneman [30] discuss
the end-users. In the other line of research that focuses on human users’ heuristics as mental shortcuts that are used in human decision-making.
interactions with and understanding of categories, we could refer to the Initial information cues or starting points also act as heuristics that can
instance-based paradigm [7], as a data management approach that is an influence individuals [31]. In essence, we can consider high-level cate-
alternative to class-based. The instance-based paradigm is conceptual- gories as anchor points for lower-level categories. Tversky and Kahne-
ized in a two-layered architecture: the first layer includes the instances man [30] discuss that these heuristics function as anchors that bias and
and their attributes (e.g., a round thing that is red, has a 30-in. limit one’s decisions. In the absence of such anchors, an individual tends
circumference, and weighs 620 g), and the other layer includes classes to have a greater degree of freedom in thinking and decision-making.
(e.g., basketball, baseball, hockey puck) along with their definitions. Hence, we posit that pre-defined categorizations (i.e., the condition
This stream developed further, namely, from content-generator [14,15] with no categorization autonomy) act as anchors that bias one’s de-
and content-consumer perspectives [16]. Prior research has found evi- cisions towards the original designers’ perspective. Self-defined cate-
dence that enabling instanced-based data entry for a ‘crowd’ that gories – once created – could also act as anchors in future use, but they
uploaded user-generated content to a citizen science platform increased would be more congruent with the given individual’s view in the first
overall accuracy and crowd information quality [14]. The content- place (i.e., as the result of full categorization autonomy). Moreover,
consumer perspective investigated users’ ability to run queries and according to Cognitive Fit Theory [32], performance improves when the
also engage in business intelligence and pattern detection on datasets information representation aligns with the user’s cognitive processes. In
that were free of classification (i.e., instances and their properties). It other words, allowing users to create their own categorization schemes
was found that users of instance-based data achieved higher query ac- provides a better cognitive fit, which should lead to higher search pre-
curacy, and performed significantly better in pattern discovery [16]. cision, as users can structure information in a way that mirrors their
The present study is different from the instance-based paradigm as internal problem-solving strategies. Recent DSS studies have extended
we kept the classes assigned to products and thus, did not directly study Cognitive Fit Theory by showing how the alignment between informa-
instances and attributes. Moreover, this paper is not focused on auto- tion representation and task characteristics improves decision perfor-
mating the creation of categories within e-commerce, where algorithms mance across various contexts. For example, the literature has
certainly play an important role in handling a large number of items that demonstrated that presentation format interacts with product type to
need to be classified. The distinction in this research is in allowing shape decision quality in e-commerce, highlighting the importance of
general users to define their categorization trees and hierarchies based matching system features with the nature of the user’s task [33]. Simi-
on a given set of already specified leaf-level categories (such as televi- larly, it was also shown that even within data visualization contexts,
sion, camera, or fridge). users experience varying levels of cognitive effort depending on how
well the design fits the task demands [34]. These perspectives emphasize
2.1. Impact of categorization autonomy on effective use the need for systems to support diverse cognitive processes.
Based on the aforementioned perspectives, our proposition is that
Categorization provides a form of cognitive economy [6] by helping users who define their own categories will assimilate information better,
organisms, such as humans, gain the maximum amount of information and hence, will be able to attain their goals of using the system. A goal
through minimum effort, optimizing the impact on their finite cognitive can be conceptualized as a “cognitive representation for a desired end-
resources. This description of categorization plays into what we consider point” [21,p. 491]. Building on this, effective use was defined as “using
heuristics. Heuristics are problem-solving ‘shortcuts’ that usually lead to a system in a way that helps attain the goals for using the system” [20,p.
an outcome, which may not be the optimal solution, but use relatively 633]. The goal-attainment factor is what distinguishes effective use from
low amounts of cognitive resources to do so [30]. Humans create cate- general use. Further, assuming objective qualities to goal-attainment, it
gories through learning and information processing. There are several was posited that effective use can operationally be assessed in terms of
models that try to explain how information processing occurs in in- performance of an observable behavior [20]. In e-commerce, the goal is
dividuals. Here, we discuss the ramifications of self-defined categories to search and find products, and its fulfillment can be measured in terms
from the perspectives of cognitive schemas [3] and decision-making of users being able to correctly search and identify items with certain
[30]. attributes (or reach the ‘desired end-point’ in terms of a goal). Therefore,
Cognitive schema theory (CST) posits that human memory is made of we hypothesize that because of better assimilation of information,
‘memory objects’ that form ‘mental models’ [3]. Memory objects are the subjects having autonomy to create their own categorization schemes
building blocks that contain general facts about something (e.g., I will be more successful in searching and identifying correct items (and
remember the weather was sunny). CST implies that individuals develop achieve their usage goals):
memory objects through life experiences, such as their studies, events,
H1. : Categorization autonomy leads to higher levels of search precision
and their culture. Memory objects that are linked to one another form
while using the system.
mental models, which tend to be more situational in nature. In the in-
formation assimilation process, a model is adjusted to the situation at Search precision is the operationalization of effective use, which we
hand. These mental models allow individuals to form patterns that calculated as the ratio of the correctly identified items over the number
consist of multiple types of memory objects, such as facts, emotions, and of pre-specified items (i.e., the goal) in this study.
the relations between objects; for example, “I remember the weather
was sunny (fact), and I felt good (emotion) – sunny weather makes me 2.2. Task flexibility moderating the impact of categorization autonomy on
feel good (pattern)”. effective use
This is an important aspect when looking at pre-defined versus self-
defined categorization (i.e., categorization autonomy). According to While categorization autonomy offers users a greater degree of
CST, we understand that an individual’s mental models are dependent control over how they structure information, its effectiveness may
on their personal experiences. As everyone’s personal experiences are depend on the nature of the task being performed. In particular, Task
unique, we can assume that the patterns they have formed are distinct as Flexibility - defined as the extent to which a task allows for multiple ways
well. In this paper’s context, these patterns entail the way a product tree of achieving the desired outcome - may shape how beneficial categori-
is categorized. The tree created by a systems designer in an organization zation autonomy is in improving search precision and decision-making.
3

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
Some tasks are inherently flexible and allow users to pursue various different decisions). From a different angle, it has been discussed how
paths and options (e.g., browsing for a birthday gift for a friend), while the “autonomy over the communication process” [39 ,p. 737] with a
others are relatively rigid and afford limited flexibility (e.g., locating a system would lead to higher adoption intentions. In our context, we
replacement cartridge for a particular printer model). This variation in expect categorization autonomy to positively affect usage intentions,
how a task can be approached may influence whether users benefit more and this relationship to be mediated by perceptions of restrictiveness:
from a predefined categorization tree or from the ability to define their
H3. : Categorization autonomy leads to higher usage intentions.
own categories.
This distinction aligns with Cognitive Fit Theory [32], which posits H4. : Perceived restrictiveness will mediate the relationship between cate-
that task performance improves when the representation of information gorization autonomy and usage intentions.
matches the cognitive processes required for the task. When a task is
The proposed nomological research model is captured in Fig. 1.
flexible, users can benefit more from the ability to define categories in a
While we recognize that in a longitudinal study of habits, perceptions
way that reflects their personalized strategies and evolving sense of
could affect performance, or vice versa, we considered the objective
relevance. Categorization autonomy, in this context, provides a better
performance to be independent from subjective perceptions during our
cognitive fit by supporting adaptive information structures. In contrast,
study (which was a one-time task). We believe that in some situations,
when tasks are inflexible and allow only a narrow set of procedural steps
an individual may not necessarily have a positive perception towards a
or criteria, the user may not require (or be able to take full advantage of)
task (e.g., not enjoying a warm-up drill before a sports game), yet,
the freedom offered by categorization autonomy, as the rigid nature of
positive results may be achieved from an objective perspective (e.g.,
the task already constrains their decision-making path.
better agility while playing the game). Or, alternatively, subjects may
A related lens is provided by Task-Technology Fit Theory [35], which
have positive perceptions (e.g., enjoying candies before a match), and as
suggests that a system is more likely to enhance performance when its
a result, have poorer objective performance (e.g., experiencing sugar
functionality matches the demands of the task. In flexible tasks, cate-
crash and fatigue). Hence, we decided to investigate objective and
gorization autonomy increases the alignment between task and tech-
subjective measures independently of one another and did not make any
nology by enabling users to construct a structure that suits their evolving
hypotheses about their possible interactions.
needs. For inflexible tasks, however, the fit between technology and task
As mentioned, to thoroughly inspect the phenomenon, we conducted
may not be as much improved by the introduction of autonomy, as the
an experiment that operationalized March’s [18] exploitation-
standard categorization approach may already be predefined by the
exploration taxonomy as task flexibility, moderating the impact of
task’s limited degrees of freedom. Based on this rationale, we expect that
categorization autonomy on effective use. The IS literature [20] also
propose the following hypothesis:
adapted March’s taxonomy and defined exploitation of information as a
H2. : Task flexibility moderates the relationship between categorization task involving the use and search for things already known or a routine
autonomy and search precision such that the effect of categorization auton- execution of knowledge in a closed-ended task. Exploration of infor-
omy would stronger for more flexible tasks. mation is the search for things in an open-ended setting.
3. Methodology and experimental setup
2.3. Effect of categorization autonomy on behavioral perceptions
The concept of ‘effective use’ – as the users’ ability to fulfill the goals
As mentioned earlier, when assessing the efficacy of a design, in
of using a system – is often operationalized by performance [20]. To
addition to evaluating objective performance measures (such as search
study this in the context of categorization autonomy, we created a
precision), understanding behavioral dimensions is also crucial in
website to simulate the task of online shopping. Participants’ ability to
determining its success and adoption by users [22]. Providing online
find products that meet their search goals is a measure of performance or
users with the autonomy to create self-defined categorization schemes
effective use.
could affect their intentions to use a platform. We study the relationship
We hired an experienced developer to create the experiment’s
between categorization autonomy and usage intentions through the
website by scraping the contents of a prominent North American
mediation effect of perceived restrictiveness of the interface. Silver [36]
Multinational Consumer Electronics (NAMCE) retailer with an annual
defines the restrictiveness of a system as the extent to which a system
revenue of more than US$50 billion. The scraped product data was
constrains the user’s “decision-making processes to a particular subset of
imported into our experimental website, and using the WooCommerce –
all possible processes” [36 , p. 52]. Restrictiveness is considered a
Store Exporter plugin, a list of category names and associated URLs was
relative term, where the set of supported processes or actions in a system
generated in JSON format to populate the interactive platform. The
could be larger or more limited compared to another system’s set of
experimental website included over 10,000 products, with prices, de-
supported actions [36]. In our context, perceived restrictiveness is
scriptions, and images, and was fully functional – allowing users to
relevant since in the fixed categorization condition, the system does not
browse, add items to their cart, and proceed to a checkout screen.
allow the user to perform any actions with regard to categorization of
concepts – hence, that condition is restricted. With categorization au-
tonomy, on the other hand, the system allows users to create categori-
zation trees based on their world view. As a result, categorization
autonomy is less restrictive and is expected to be perceived as such by
the users.
We predict that subjects would have lower intentions to use an
interface that has fixed categorization schemes compared to a system
that offers categorization autonomy. This reasoning is in line with prior
work [37] in which they studied decision support aids with additive-
compensatory, eliminatory, and hybrid strategies and showed that
when a user’s desired support functionalities were not offered by a de-
cision support system, the psychological reactance reduced their in-
tentions to use the system - as per the reactance theory [38]. In their
study, the relationship between decision strategy and adoption in-
tentions was mediated by perceived restrictiveness (resulting from Fig. 1. Nomological research model.
4

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
Separate environments were created for each condition, all con- conditions resulting from the factorial combination of the two variables.
taining the same products to ensure informational equivalence [40]. The This design enabled us to assess the main effect of Categorization Au-
product category tree on NAMCE was captured in a three-level hierar- tonomy on search performance, as well as whether the strength of this
chy; for example, Appliances as a top level, included Major Appliances effect varied across levels of Task Flexibility. After reviewing the consent
and Small Kitchen Appliances in the middle tier, and then general form, subjects received pre-experiment questions, which collected in-
product types such as Dishwashers and Coffee Makers as leaf-level formation about e-commerce experience, openness (a big-five person-
general product types. We also adopted this three-level categorization ality trait [42]), and demographics.
hierarchy in our study – Fig. 2shows a screenshot of our website. Subjects in all six conditions viewed a training video that demon-
The NAMCE contained around 250 leaf-level categories (e.g., tablet, strated browsing, ordering, and adding to cart functions. Subjects in the
air conditioner, laser printer). For practical reasons, we had to limit the partial and full categorization autonomy groups received an additional
number of leaf-level categories as it would have taken a considerable five-minute tutorial on using the ‘edit categories’ page and creating their
amount of time to classify the whole set of 250 categories. In the real own categories – as the category ‘edit’ feature was only available to
world, in case categorization autonomy was offered by a platform, users them. We used different products in the training demonstration (which
could create their categories over multiple sessions; however, that were not available in the main experiment) to avoid biasing the
would not have been feasible for our studies. Hence, we conducted participants.
multiple trials online with 10 Amazon Mechanical Turk (AMT) workers Next, the subjects in the partial and full autonomy conditions
in each iteration, and trimmed 30 to 40 leaf-level categories (while (whether in high task flexibility or low) were asked to edit or create their
maintaining a relatively consistent distribution at higher levels of the categories respectively, and the fixed categorization (i.e., control) group
tree) in each attempt until the categorization time reached the average was asked to spend five minutes inspecting the categories. The manda-
of 15 min with 78 leaf-level categories remaining. Given that attention tory inspection time given to the control group allowed us to provide an
typically declines after 10–15 min [41], we set 15 min as a reasonable equivalent condition (with regard to familiarization and engagement)
time for participants to create categories before starting the main task. for browsing the categories between all three conditions. Further, the
We used three conditions in our studies. The first condition, or time that the participants spent on the page was measured to account for
control, was based on the NAMCE’s website and all three levels of the any differences between the groups. These steps were consistent in all
category tree were fixed (i.e., no autonomy in changing the categories by conditions, and as reported in the post-hoc analysis section, the time
users) – from here on we use fixed categorization and no autonomy spent in this stage was not a significant covariate on the results. Then,
interchangeably. Our treatment condition provided full autonomy, and subjects received the scenarios for the respective studies and were asked
showed subjects only the leaf-level categories. Their interface had a to perform the assigned task. At the end, participants answered survey
feature that allowed them to create high-level (i.e., Level 1) and sub- questions regarding their usage intentions (Appendix A).
categories (i.e., Level 2) and populate them by dragging and dropping
the leaf-level categories (i.e., Level 3) inside them. The flexible catego-
3.2. Sample selection
rization interface was developed using JavaScript on the Vue.js frame-
work, and included an ‘edit’ interactive panel. Fig. 3shows the edit page
For our studies, we used Amazon Mechanical Turk (AMT) workers
where a subject created one top-level category named “Home” with two
belonging to the ‘master worker’ category – top performers who were
subcategories of “Kitchen” and “Living Room”. The leaf-level categories
granted the ‘master’ qualification by Amazon – with more than 100 jobs
on the right-side pane could be dragged and dropped under them by the
completed and at least a 95 % approval rate. We also limited the sample
users. The users’ self-defined categories were storied as structured JSON
to participants located in the United States or Canada (where the source
objects.
e-retailer also operates). Several studies have shown that AMT workers
We also created a middle condition where Level 1 and Level 2 were
exhibit comparable biases and performance to other participants in
the same as the source website, but participants had to manually drag
traditional laboratory experiments [14,43]. In addition, we believe that
and drop the leaf-level categories under these fixed levels. We consider
AMT subjects are appropriate surrogates for typical e-commerce users
this condition to offer partial autonomy. We did not develop formal hy-
with similar demographic profiles; hence, their recruitment is justified.
potheses regarding this condition, as it is not part of our theoretical
Based on the initial statistical power analysis on a pilot with 20 subjects,
development. Rather, we included this to rule out alternative explana-
we decided on a sample size of around 35 in each condition based on the
tions for the effects observed in the full autonomy condition. Namely,
desired power of 0.8. Moreover, it has been stated that for a sample
the partial autonomy condition helps clarify whether the observed im-
containing minor subgroups, a minimum of 20 to 50 elements is needed
provements in performance and perceptions were due to the effect of
per group [44]. The subjects received fixed compensation depending on
categorization autonomy itself, or from greater time spent engaging
the experimental condition that was higher than the minimum hourly
with the interface. The partial autonomy condition strengthened the
wage in the United States.2 Participants were 45 % female and 55 %
internal validity of our findings by serving as a control for potential
male with 36 % in the age bracket of 30–40 years old. We eliminated
confounds related to effort and user involvement.
duplicate entries, treatment participants who had not created a cate-
gory, subjects who had not placed an order, and those who failed the
3.1. Experimental design trap question in the survey.3
The scales for the behavioral measures were tested for validity and
We adopted a 3 × 2 between-subjects experimental design to
reliability (Appendix B). All the variables exhibited high factor loadings
investigate the impact of Categorization Autonomy (fixed, partial, full)
and thus warranted no further adjustments. Next, we examined the
on users’ search precision, and to examine whether this relationship is
Cronbach’s alpha and Average Variance Extracted (AVE) measures for
moderated by Task Flexibility (low in exploitive search vs. high in
exploratory search). Categorization Autonomy was the primary manip-
ulated factor, representing different levels of user control over the
2 In pilot studies, control subjects averaged 30 min, while partial and full
categorization structure. Task Flexibility, treated as a moderating factor,
autonomy groups averaged 37 and 45 min, respectively. Accordingly, partici-
is conceptualized as the degree of variability in how a task can be
pants were paid $6 (fixed), $7 (partial autonomy), and $8 (full autonomy).
approached and completed. Higher task flexibility enables greater 3 We initially recruited 77 subjects in the fixed, 73 in the partial, and 75 in
variability and openness in decision-making processes, whereas lower full categorization autonomy conditions. After the exclusions, we analyzed 69
task flexibility constrains users to follow a more closed and predefined subjects in fixed, 67 in partial, and 65 in the full categorization autonomy
path. Participants were randomly assigned to one of the six experimental group.
5

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
Fig. 2. Three levels in the product category tree, as in the source website.
Fig. 3. Treatment Condition Interface with Category Edit Feature.
the different constructs. The results demonstrated a Cronbach’s alpha of Appendix C.
above 0.9 for all constructs, which indicated high reliability [45]. The Subjects did not have access to a keyword search function and had to
AVE of all constructs was high as well (>0.5), indicating high conver- locate the items using the categorization tree of their respective condi-
gent validity [46]. Appendix B provides the details. tions. The search function feature was removed due to the intention to
run a controlled laboratory experiment, where extraneous factors and
their potential interactions were held constant to isolate the effect of
3.3. Experiment
categorization autonomy. Once subjects finished adding the items to the
shopping cart, they proceeded to the post-experiment questionnaire
As mentioned, subjects were randomly assigned to one of the main
about behavioral perceptions. Table 1presents the descriptive statistics.
conditions of control (i.e., fixed categorization), partial categorization
The first hypothesis was related to subjects’ ability to search and
autonomy with the first two levels of the category tree fixed according to
NAMCE’s design, and treatment conditions (i.e., full categorization au- identify the correct products based on the given scenario. Two inde-
pendent coders went through the shopping carts of subjects in all three
tonomy), and either performed the closed-ended exploitive task (i.e.,
conditions and rated whether the item was acceptable with regard to the
low task flexibility), or the open-ended exploratory search (i.e., high
specifications. The intra-class correlation between the two coders was
task flexibility). The subjects in the fixed categorization group were
95 %, which indicates a high degree of reliability.
instructed to study the product tree, while the subjects in the partial and
Subjects received a point for every correct item they had identified
full categorization autonomy conditions had to categorize 78 leaf-level
(e.g., one point if they had chosen a 27-in. monitor as per the scenario, or
product types into higher level categories. We employed a live chat
an air-fryer as a gift for a cooking enthusiast, but no points were
function for subjects in every condition, and we were reachable to them
awarded for a product that did not match the specifications). To
throughout the experiment. The actual task scenario was locked behind
compare the precision of the results, we calculated the ratio of correct
a password-protected page. Subjects in the fixed condition received the
answers to the total number of required items (i.e., dividing each score
password after five minutes, and subjects in the partial and full auton-
by the number of items subjects were instructed to buy). Since catego-
omy condition had to let us know when they were done with the cate-
rization autonomy can be treated as an ordinal variable (fixed catego-
gorization activity, and once we verified their completion of building the
rization or no autonomy <partial autonomy <full autonomy), we ran
category trees, we offered them the password that allowed them to
regression tests (after checking for normality of distribution) to
proceed to the main task. The scenario for the tasks is available in
6

A. Saghafi et al.                                                                                                                                                                                             D   e c i s  i o n    S  u  p p  o  r t   S  y  s t e m   s  196 (2025) 114499
Table 1  between categorization autonomy and search precision as our second
Descriptive statistics. hypothesis. The results in Table 3show that the interaction effect of task
flexibility and categorization autonomy is significant in a continuous
| Variable  | Search  | Perceived  |     | Intention to  |     |     |     |     |     |
| --------- | ------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- |
operationalization (0.179, p <
Condition Precision  Restrictiveness Mean  Use  0.01; Model 1). After checking for
|     | Mean (SD) | (SD) |     | Mean (SD) |     |     |     |     |     |
| --- | --------- | ---- | --- | --------- | --- | --- | --- | --- | --- |
normality of the distribution, we found that task flexibility moderates
Fixed – Low  0.822  4.231 (1.441) 4.389  the effect of categorization autonomy on search precision in comparison
| Flexibility, N =36 |         |     |     |         | of fixed vs. full autonomy (0.161, p < |     |                              |     |     |
| ------------------ | ------- | --- | --- | ------- | -------------------------------------- | --- | ---------------------------- | --- | --- |
|                    | (0.233) |     |     | (1.573) |                                        |     | 0.05; Model 2), and also in  |     |     |
Fixed – High
0.737  4.689 (1.592) 4.263  comparison of partial vs. full autonomy (0.229, p <0.01; Model 3,).
| Flexibility, N =33 | (0.371) |     |     | (1.659) |     |     |     |     |     |
| ------------------ | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
To examine the influence of categorization autonomy on the usage
| Partial autonomy –  | 0.811  | 3.533 (1.464) |     | 5.577  |     |     |     |     |     |
| ------------------- | ------ | ------------- | --- | ------ | --- | --- | --- | --- | --- |
Low Flexibility, N = intention (Hypothesis 3), we used regression models with robust stan-
|     | (0.226) |     |     | (1.229) |     |     |     |     |     |
| --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
30 dard errors, as shown in Table 4. Similar to the previous analyses, we
Partial autonomy –  0.677  3.387 (1.827) 5.811  first ran regression analysis using the continuous operationalization of
High Flexibility, N  (0.329) (1.158) categorization autonomy to check if it has a significant effect on in-
=37
tentions to use. Once we confirmed that there was a significant effect of
| Full autonomy – Low  | 0.971  | 3.069 (1.618) |     | 4.932  |     |     |     |     |     |
| -------------------- | ------ | ------------- | --- | ------ | --- | --- | --- | --- | --- |
categorization autonomy on intentions to use (0.362, p <0.01; Model
| Flexibility, N =34 | (0.068) |     |     | (1.395) |     |     |     |     |     |
| ------------------ | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
Full autonomy, High  0.914  2.785 (1.447) 5.204  1), we then ran regression tests (after checking for normality of distri-
| Flexibility, N =31 | (0.171) |     |     | (1.497) |     |     |     |     |     |
| ------------------ | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
bution) to investigate which group orders showed the effect. From our
analysis of the different subgroups (Models 2–4), H3 is corroborated in
the comparison between the fixed vs. full categorization autonomy
investigate which group orders showed the effect. The ordinal analysis is
(0.359, p <0.01; Model 2) and fixed vs. partial categorization autonomy
in line with a prior study with a similar design [47] on decomposition of
(1.373, p <0.01; Model 4).
conceptual models and the adherence to Good Decomposition Principles
Next, to study the mediating role of restrictiveness in the relationship
at three levels (comparing good vs. bad, good vs. moderate, and mod-
between categorization autonomy and usage intentions (Hypothesis 4),
erate vs. bad). Similar to their analysis, we investigated whether higher
we tested both the product of coefficients (Sobel test) and the boot-
degrees of categorization autonomy led to advantageous results. Table 2
strapped confidence interval of the indirect effects (following Preacher
shows that offering categorization autonomy resulted in an overall in-
crease in search precision (0.077, p <0.05; Model 1). In our group-wise  and Hayes [48]). In the Sobel test, we checked if the indirect effect was
comparisons, we find that search precision for subjects who had full  significantly different from zero. The Sobel test assumes normality in the
categorization autonomy was significantly higher (0.155, p < 0.01;  distribution of the indirect effect. Methodologists therefore recommend
Model 2) than users of pre-defined categories from the original retailer’s  that it be supplemented with bootstrap confidence intervals, which do
not make assumptions about the shape of the sampling distribution [48].
website (i.e., fixed categorization or no autonomy). Subjects in the full
If the confidence intervals exclude zero, the indirect effect (i.e., medi-
autonomy condition also significantly outperformed subjects in the
partial autonomy (0.204, p < ation) is considered meaningful. We therefore calculated bias-corrected
0.01; Model 3), but the difference in
and accelerated confidence intervals across 5000 bootstrap resamples.
performance between fixed categorization and partial autonomy con-
Table 5provides the coefficients and standard errors of the indirect,
ditions was not statistically significant. This result is expected, as only
direct, and total effects of the mediated relationship between categori-
the full autonomy allowed participants to adjust the information struc-
zation autonomy and usage intentions. The mediation analysis provides
ture to fit their cognitive processes [32], whereas partial autonomy
constrained them to fixed Level 1 and 2 categories, limiting flexibility to  support for H4 for the two comparison groups fixed vs. full autonomy
(0.482, p <0.01, Sobel Test, 0.481 p <0.01 Preacher and Hayes Test)
product placement only at the leaf level. Overall, the first hypothesis was
and fixed vs. partial categorization autonomy (0.516, p <0.01, Sobel
corroborated.
Test and Preacher and Hayes Test). In the mediation Table 4, the ‘a
We tested the moderation effect of Task Flexibility (exploitive or
closed-ended vs. exploratory or open-ended tasks) on the relationship
Table 3
Regression analysis for the moderation effect of task flexibility – Hypotheses 2.
Table 2
Regression analysis for impact of categorization autonomy on search precision –  Interaction Effects  Model 1  Model 2  Model 3  Model 4
Hypothesis 1. Outcome: Search  Coefficient  Coefficient  Coefficient  Coefficient
|     |     |     |     |     | Precision | (Standard  | (Standard  | (Standard  | (Standard  |
| --- | --- | --- | --- | --- | --------- | ---------- | ---------- | ---------- | ---------- |
Outcome: Search  Model 1  Model 2  Model 3  Model 4  Error) Error) Error) Error)
Precision Coefficient  Coefficient  Coefficient  Coefficient  (cid:0) (cid:0) (cid:0) (cid:0)
(Standard  (Standard  (Standard  (Standard  Task Flexibility 0.179  0.152  0.223  0.072
|     |        |        |        |        |                 | (0.059)** | (0.066)* | (0.058)** | (0.068) |
| --- | ------ | ------ | ------ | ------ | --------------- | --------- | -------- | --------- | ------- |
|     | Error) | Error) | Error) | Error) |                 |           |          |           |         |
|     |        |        |        |        | Categorization  | 0.079     |          |           |         |
Autonomy (0 ¼
| Categorization  | 0.077     |     |     |     |                     | (0.035)* |     |     |     |
| --------------- | --------- | --- | --- | --- | ------------------- | -------- | --- | --- | --- |
| Autonomy        | (0.019)** |     |     |     | Fixed; 1 ¼Partial;  |          |     |     |     |
| (0 ¼Fixed; 1 ¼  |           |     |     |     | 2 ¼Full) * Task     |          |     |     |     |
Partial; 2 ¼Full)
Specificity
| Fixed vs. Full   |     | 0.155     |           |     |                    |     |          |           |     |
| ---------------- | --- | --------- | --------- | --- | ------------------ | --- | -------- | --------- | --- |
|                  |     |           |           |     | Fixed vs. Full     |     | 0.161    |           |     |
| Autonomy         |     | (0.039)** |           |     | Autonomy (0 ¼      |     | (0.069)* |           |     |
| (0 ¼Fixed; 1 ¼   |     |           |           |     | Fixed; 1 ¼Full) *  |     |          |           |     |
| Full)            |     |           |           |     | Task Openness      |     |          |           |     |
| Partial v. Full  |     |           | 0.204     |     |                    |     |          |           |     |
|                  |     |           |           |     | Partial v. Full    |     |          | 0.229     |     |
| Autonomy         |     |           | (0.327)** |     | Autonomy           |     |          | (0.062)** |     |
(0 ¼Partial; 1 ¼
(0 ¼Partial; 1 ¼
Full)
Full) * Task
| Fixed vs. Partial  |     |     |     | (cid:0) 0.048   | Openness           |     |     |     |                |
| ------------------ | --- | --- | --- | --------------- | ------------------ | --- | --- | --- | -------------- |
| Autonomy           |     |     |     | (0.051)         | Fixed vs. Partial  |     |     |     | (cid:0) 0.067  |
| (0 ¼Fixed; 1 ¼     |     |     |     |                 | Autonomy (0 ¼      |     |     |     |                |
(0.082)
| Partial)              |        |        |        |        | Fixed; 1 ¼Partial) *  |        |        |        |        |
| --------------------- | ------ | ------ | ------ | ------ | --------------------- | ------ | ------ | ------ | ------ |
| N                     | 201    | 134    | 132    | 134    | Task Openness         |        |        |        |        |
| R-Sq                  | 0.0570 | 0.1006 | 0.1729 | 0.0067 | N                     | 201    | 134    | 132    | 134    |
| ** p <0.01 * p <0.05. |        |        |        |        | R-Sq                  | 0.0640 | 0.0734 | 0.1655 | 0.0394 |
7

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
Table 4 4. Post-hoc analyses
Regression analysis for the effect on usage intentions – Hypothesis 3.
Outcome: Model 1 Model 2 Model 3 Model 4 4.1. Heterogeneous treatment effect
Intention to Use Coefficient Coefficient Coefficient Coefficient
(Standard (Standard (Standard (Standard The overarching premise of this paper is that the individuals’ mental
Error) Error) Error) Error) models depend on their personal experiences, which results in signifi-
Categorization 0.362 cant differences in how they categorize items. To test this premise and
Autonomy (0.131)** gain a deeper understanding of the differences between personalized
(0 ¼Fixed; 1 ¼
categories created by participants in the treatment group (where they
Partial; 2 ¼Full)
Fixed vs. Full 0.359 had categorization autonomy, and as a result, one could observe the full
Autonomy (0.128)** effects), we captured the vector representations of the product trees of
(0 ¼Fixed; 1 ¼ each participant’s categorization scheme. Using vector representations
Full) [49,50], one can compare the similarities and differences between
Partial v. Full (cid:0) 0.653
participants in the treatment group and investigate the antecedents to
Autonomy (0.225)
(0 ¼Partial; 1 ¼ their differing product trees. The vector representations for two hypo-
Full) thetical participants with five products are illustrated in Fig. 4.
Fixed vs. Partial 1.373 In our analysis, the full vector representation is generated using all
Autonomy (0.239)**
combinations of category labels created by the 65 treatment partici-
(0 ¼Fixed; 1 ¼
Partial) pants4 and the NAMCE’s scheme (as a baseline for comparison).
N 201 134 132 134 Adopting such a high-dimensional representation (each new combina-
R-Sq 0.0383 0.0532 0.0580 0.1926 tion of categories creates a new dimension) of the categorization trees is
** p <0.01 * p <0.05. possible in our sample because (a) our experiment was restricted to
Table 5
Analysis on the Mediation Effect of Restrictiveness on usage Intentions – Hypotheses 4.
Outcome: Intention to Use a Coefficient b Indirect Effect Direct Effect Total Effect c Sobel Test Preacher &
Coefficient aXb c’ Hayes
Categorization Autonomy (cid:0) 0.698 (0.134) (cid:0) 0.561 (0.053) 0.391 (cid:0) 0.029 0.362 0.391 0.391
(0 ¼Fixed; 1 ¼Partial; 2 ¼ ** ** (0.084)** (0.108) (0.126)** (0.084)** (0.091)**
Full)
Fixed vs. Full Autonomy (cid:0) 0.697 (0.131) (cid:0) 0.691 (0.060) 0.482 (cid:0) 0.122 0.360 0.482 0.481
** ** (0.099)** (0.101) (0.129)** (0.099)** (0.100)**
Partial v. Full Autonomy (cid:0) 0.424 (cid:0) 0.405 0.172 (cid:0) 0.826 (cid:0) 0.654 0.172 0.171 (0.114)
(0.277) (0.062)** (0.115) (0.200)** (0.227) (0.115)
Fixed vs. Partial Autonomy (cid:0) 0.970 (0.272) (cid:0) 0.532 (0.061) 0.516 0.857 (0.203) 1.373 (0.241) 0.516 0.516 (0.171)**
** ** (0.156)** ** ** (0.156)**
** p <0.01 * p <0.05.
coefficient’ represents the effect of categorization autonomy on creating a categorization tree of a maximum of three levels (e.g., Ap-
restrictiveness and the ‘b coefficient’ represents the effect of restric- pliances - > Large appliances - > Dishwashers – similar to NAMCE’s
tiveness and intention to use. We note that the effect of categorization design) and (b) the number of leaf categories was limited to 78 items. To
autonomy is negative and significant for the fixed vs. full autonomy further reduce the number of possible combinations of categories, one of
((cid:0) 0.697, p < 0.01) and the fixed vs. partial autonomy ((cid:0) 0.970, p < the authors analyzed the participant-created category names for syno-
0.01) comparisons. Furthermore, we find a negative and significant nyms, and another evaluated the identified synonyms to ensure validity.
relationship between restrictiveness and intentions to use across all our During this exercise, category names that were found to mean the same
analyses (b coefficient). Lastly, in the case of the fixed categorization vs. concept (e.g., computer accessories and peripherals, or cell phone and
full autonomy conditions, we observe a full mediation as the direct effect mobile) were identified as equivalents. Our final representation was
becomes insignificant in the presence of the mediator. For the fixed vs. generated by evaluating all combinations of categories created by the
partial categorization autonomy comparison, however, we observed a participants in the treatment group, and the NAMCE category tree used
partial mediation. for the control group comprised of 247 (category combinations; rows in
Overall, we believe the benefits of categorization autonomy would Fig. 4) and 78 (leaf categories or products, columns in Fig. 4).
be best realized when the task itself is free of prior anchoring biases
(discussed earlier, referring to [3]). Considering that exploratory tasks 4.1.1. Analysis of the participants’ product category trees
have more open-ended requirements, categorization autonomy pro- The vector representation of the product category tree offers the
vided a more open and flexible means of navigation for users; hence, the advantage of quantifying and comparing the similarities (or rather,
moderating effect of Task Flexibility. Moreover, categorization auton- dissimilarities) of category trees created by the participants in treatment
omy positively impacts usage intentions, particularly when users are conditions. Using vector representations, we studied how participants
allowed to explore the categories and select items according to their own differ from each other by calculating the cosine similarities of the par-
knowledge and expectations with greater freedom. A more elaborate ticipants’ category trees. We note that the participants’ category trees
behavioral research model regarding additional antecedents to adoption are considerably different from one another, with a maximum cosine
is presented in Appendix D.
4 We combined treatment subjects from both levels of task flexibility, since
the task was presented after the categorization trees were created, and the
scenario had no effect on subjects at the creation stage.
8

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
Fig. 4. Vector Representation of Product Categorization Tree.
similarity of 0.58 between them. Further, we find that the participants’ 4.2. Impact of time
self-defined category trees differ considerably from the baseline NAMCE
category tree, having a mean cosine similarity of 0.36. The findings We analyzed the effect of time spent on observing pre-defined cat-
support the premise that individuals tend to develop unique schematic egories, or creating self-defined categories (i.e., before the scenario was
representations based on prior experiences [3,31]. given) in both conditions of task flexibility as covariates on overall
search precision. The time spent on observing or creating categories
4.1.2. Antecedents to the differing expressions of the product category trees (depending on condition) in the exploitive scenario had the p-value of
Given the differences reported earlier, we investigated whether de- 0.984. Similarly, in the exploratory setting, the time spent on observing
mographic and personality traits of participants might have an influence or creating categories had the p-value of 0.328 as a covariate on search
on the cosine similarity measures of treatment users’ vector represen- precision. We conclude that the time spent before the tasks did not have
tations of self-defined categories and NAMCE’s schema. As a major a significant effect on performance. We also checked for the effect of
antecedent of the diversity of expression of individuals, literature points time spent on creating or browsing categories (i.e., pre-task time) and
to the important role that openness to experience plays in divergent the time spent on the task as covariates on usage intentions, and neither
thinking [51,52]. Specifically, openness is one of the key personality were significant (p =0.483 and p =0.363 respectively).
traits that is necessary to produce new ideas [23]. In our experiment, Comparing the actual time spent on the experimental task (post-
openness was operationalized as the extent to which a person was open initial observation or creation of categories depending on condition), we
to experiences and their degree of creativity [42]. Along with openness, found significant differences in both task types with the order of longest
we also collected demographic information, including age, gender, in- time spent by subjects in the partial categorization autonomy condition,
come, and level of education. Table 6 provides the coefficients and then by the treatment (full categorization autonomy), and control (no
standard errors in estimating the cosine similarity of the participant’s autonomy). Task completion time could be considered a measure of
category tree with the NAMCE category tree using the Ordinary Least efficiency; however, since subjects were not instructed to finish the task
Squares (OLS) regression model. Based on the analysis, we found that as soon as possible, we do not necessarily consider the observed differ-
the openness factor was negative and significant ((cid:0) 0.31, p < 0.05; ence to indicate inefficiency.
Table 6). This confirms prior literature suggesting that openness is
related to how diverse individual expressions are. In other words, this 5. Discussions and conclusion
implies that users with higher levels of openness (as a personality trait),
tend to create product categorization trees that are less similar to a pre- We studied categorization autonomy as a design principle and
defined scheme created by the vendors. The other demographic factors explored its impact in terms of effective use, as well as usage intentions.
did not have a significant effect on the dissimilarity measure of self- While the primary focus and therefore the contribution of our research
defined categories to the baseline. lies within the domains of Human-Computer Interaction (HCI) and De-
cision Support Systems (DSS), it also aligns with the components of a
design theoretical model [53], as it defines a clear purpose – enhancing
user decision-making through categorization autonomy – supported by
Table 6 theoretical constructs such as task flexibility and effective use. The
Demographics and (Dis)similarity with NAMCE as a baseline. principles of form and function are reflected in hierarchical categori-
zation trees, while the evaluation of performance and behavioral out-
Dependent Variable: Cosine Similarity Regression Coefficients (and
to NAMCE Standard Errors) comes provides testable propositions. The design is grounded in
knowledge drawn from cognitive schema, cognitive fit, task-technology
Openness (cid:0) 0.31* (0.14)
Age (cid:0) 0.147 (0.791) fit, and reactance theories.
Gender 0.560 (2.712) Our study was set in the context of e-commerce, as the users access
Income (cid:0) 0.656 (0.935) and browse large amounts of information, making it an appropriate
Level of education (cid:0) 0.258 (2.03) platform [10]. The benefits of categorization autonomy can be realized
R-Sq 0.103
in other contexts and business domains as well. For example, YNAB (You
N 65
Need a Budget), one of the most popular budgeting applications, offers
** p <0.01 * p <0.05.
9

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
users the autonomy to create and customize budget categories that align focused on creating categories that provide higher utility and cognitive
with their personal financial goals, enabling a tailored expense man- economy in general applications. Our findings indicate that greater
agement approach.5This autonomy has generated user engagement, as utility can be achieved in terms of higher search precision when users
evidenced by the r/YNAB subreddit, where thousands of members share create their custom-made categorization trees (i.e., the “what” and
their unique categorization strategies.6 “how”). It is also in line with schema theory [3], which indicates that
Our findings provide strong empirical support for the positive impact humans assimilate information better when they create mental models
of categorization autonomy on users’ search precision when compared that are congruent with their experiences (i.e., the “why”) and enhance
to fixed categorization. Furthermore, the moderating effect of Task their decision-making [54]. The post-hoc analysis illustrated this
Flexibility was statistically significant, indicating that the benefits of distinction; specifically, the cosine similarities of the participants’ self-
categorization autonomy are more pronounced in tasks characterized by defined categories were divergent from one another and the baseline
higher flexibility. We also included a mid-level condition with partial (i.e., for “whom”). This difference could partly be attributed to the
categorization autonomy, in order to rule out alternative explanations of openness character trait, which was a statistically significant determi-
learning effect (improving effective use) and extended interaction with nant of the dissimilarity of the individuals’ vector representation
an interface leading to more favorable perceptions (e.g., intention to matrices from the NAMCE baseline.
use). Our results were consistent in that treatment (i.e., full categori- From the human-computer interaction perspectives, we investigated
zation autonomy) performed better than both fixed categorization and a novel data representation design in the form of categorization auton-
partial autonomy condition in terms of search precision. However, the omy. We found that self-defined categories can influence important
difference between fixed and partial autonomy conditions was not sta- factors such as perceptions of restrictiveness and intention to use.
tistically significant. This could indicate that offering partial autonomy Moreover, we found the nature of the task to be a determining factor in
at the lower levels (product level), may not provide the full benefits of the effect, with the difference being more prominent in higher task
categorization autonomy, since the top two category levels (from the flexibility or exploratory searches (i.e., “when”). One explanation for
source) were not congruent with the users’ mental models. this finding might reside in the fact that creating individualized cate-
We also examined the effect of categorization autonomy on usage gories engages one’s brain in an exploratory mindset.
intentions, as well as the mediation effect of perceived restrictiveness on Prior research has also studied eye-tracking movements in the two
this relation. In the exploitive searches, we found the direct relationship scenarios of exploration and exploitation and found that participants in
of categorization autonomy on usage intentions (H3) to be statistically the exploratory task demonstrated greater amounts of decision-making
significant, so was the mediation effect of perceived restrictiveness (H4), creativity [55]. Similarly, in our experiment, the greater freedom
particularly in the comparison between control and treatment (i.e., no offered by categorization autonomy could be a reason that task flexi-
categorization autonomy vs. full autonomy). In comparing the partial bility had a significant moderating effect on search precision. Moreover,
autonomy condition to full categorization autonomy, hypotheses H3 and our findings contribute to the ongoing refinement of Cognitive Fit
H4 were not corroborated. These results were consistent in both Theory within the DSS literature. It has been argued that fit is not merely
exploitive and exploratory searches. The summary of our results that a function of task-structure alignment but may also reflect adaptive
were corroborated or rejected are presented in Table 7. We conclude mechanisms and user-level strategies [56]. In line with this, we find that
that categorization autonomy leads to greater search precision (i.e., categorization autonomy can support decision effectiveness when users
objective effective use) compared to conditions with partial or no are given the flexibility to tailor information structures to their goals.
categorization autonomy. The impact of categorization autonomy on However, consistent with prior work (e.g., [34]), our results suggest that
usage intentions is significant, particularly in comparison between fixed fit is sensitive to task framing and user involvement.
vs. full autonomy, or fixed vs. partial autonomy. From practitioners’ perspective, this research shows how categori-
zation autonomy can benefit a platform used by general users, such as e-
commerce. Categorization autonomy would enable users to find the
5.1. Implications
items they are looking for more accurately. Additionally, by offering
categorization autonomy on a website, an organization might improve
This paper contributes to categorization, schema theory, and human-
key consumer behavior factors such as intention to use. While our
computer interaction literature. Categorization research has mainly
findings show that categorization autonomy improves both search pre-
cision and behavioral intentions, we recognize that these effects may not
Table 7
directly translate into real-world adoption. In practice, factors such as
Summary of results – corroborated and rejected hypotheses.
user learning curves, training demands, organizational resistance to
Hypothesis H1 H2 H3 H4 change, and integration with existing workflows can all impact adoption
Search Moderation Intention Mediation by
outcomes [57]. These issues are beyond the scope of our study, but they
Condition Precision by Task to Use restrictiveness
Flexibility represent important considerations for practitioners evaluating the
viability of categorization autonomy in live systems.
Fixed Yes Yes Yes Yes
Our recommendation for websites is to give users the option to
Categorization
vs. Full choose between self-defined and pre-defined categorization and inform
Autonomy them of the benefits of categorization autonomy. Further, since the
Partial v. Full Yes Yes No No openness trait of individuals is positively correlated to the extent to
Categorization
which they may differ in the way they categorize product trees (Table 6,
Autonomy
Fixed No No Yes Yes supported by [52]), platforms catering to a more open psychographic
Categorization profile may benefit more from offering categorization autonomy.
vs. Partial However, even as this research aims to demonstrate how categorization
Autonomy
autonomy could be beneficial, we acknowledge the utilities that pre-
defined categorization might offer. First of all, pre-defined categoriza-
tion provides cognitive economy. Even if a schema created by the
developer might not be fully congruent with the users’ mental models, it
is still easier to comprehend than viewing a list of all categories in a short
5 https://www.ynab.com/ period of time. Moreover, creating personalized categorization schemes
6 https://www.reddit.com/r/ynab/ can be quite time-consuming. For one-time shoppers from a given e-
10

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
commerce website, this may not be a valuable time investment. The be interesting to study the differences in cognitive load by observing
benefits of creating personalized categories are best realized for return brain activity using fMRI and electroencephalography (EEG) tools, or
customers and frequent shoppers on a given platform. We also note that tracking eye movements.
a one-size-fits-all approach is not the best solution. In other words, We believe the benefits of categorization autonomy can be realized
forcing all users to create their own categories may not have a univer- in contexts other than e-commerce as well. For example, users of
sally beneficial effect. Similarly, a prior study found that Intel’s verbal banking applications could benefit from control over how expenses are
advisor that increased successful downloads by 27 % was “not for every categorized (e.g., ‘car insurance’ along with ‘health insurance’ under the
customer. Less verbal and more analytic customers found the verbal category of ‘insurances’, or grouped next to ‘fuel expenses’ and ‘road
advisor annoying and preferred a more graphic list” [2,p. 202]. Hence, taxes’ under ‘transportation’ or ‘car ownership’ categories). Future
we suggest that both options of full categorization autonomy and pre- research might also involve different product types (e.g., specialized
defined schemes be offered and the choice be left to the users. items such as a hydraulic pump for a production facility versus a com-
Lastly, on many e-commerce platforms, shoppers use the search modity like a carton of milk) to see if users’ prior expertise and
function to find the items they are looking for (e.g., an HDMI cable, or a knowledge in the subject area could impact their interactions with a
phone charger). We argue that such a task is more in line with the system that offers categorization autonomy. Studying the impact of
exploitation search type. In cases where a person is deciding on how to categorization autonomy in high-stakes or expertise-driven domains –
use a gift card they received, for example, they might browse through where, in certain circumstances, it could even be counterproductive – is
the product trees, and that exploration could benefit most from cate- certainly an interesting topic for future research. In fact, one could
gorization autonomy. explore the trade-off between user autonomy and system-imposed
structure, and how each may enhance or hinder performance, particu-
5.2. Limitations larly in contexts with varying levels of task flexibility (routine or closed
vs. creative or open) and task complexity (low vs. high expertise). Based
Prior research points to the varying levels of exploration requiring on task demands, hybrid architectures could also be considered, where
different levels of creativity [55]. In our study, the tasks were simplified user-defined and system-generated categorization approaches are
and thus, did not fully capture the whole spectrum of information re- effectively combined in response to user characteristics and task
quirements. Tasks entailing more rigid frameworks, as well as objectives requirements.
with greater levels of exploration freedom can be examined in the Moreover, scholars could examine users’ willingness to engage in
future. categorization for subjects with varying degrees of attachment to a
This research was conducted on an experimental website. While it system (i.e., new users versus veterans), what the barriers are, and in
allowed us to investigate the effects, we realize that real-world settings what factors may contribute to their long-term usage of categorization
might yield different results for behavioral intentions - academic pro- autonomy.
jects such as ours may never be able to capture the ramifications of Our post-hoc analysis shows that the openness personality trait can
spending actual money on real products. Moreover, in real-world cases, determine how divergent the individuals’ categorization trees are from
users (of e-commerce or organizational systems) tend to interact with a the baseline. Identifying additional antecedents that may influence
given system over a continued period of time – as opposed to our study users’ categorization scheme could be a direction for future research.
where users spent one hour interacting with the system on average. A Another area for continuing this research program might lie within
longitudinal study could offer additional insights on interactions with a understanding how individuals create categories. Our work was based
system that offers categorization autonomy. Furthermore, while our use on analyzing the ‘product’ of a user’s categorization activity. Future
of Cognitive Fit Theory helps explain performance differences in the studies on the process itself, by collecting clickstream data for example,
short term, we acknowledge that cognitive fit may evolve over extended could shed more light on the intricacies of the cognitive categorization
usage. Factors such as learning, adaptation, or user fatigue could alter process.
how well a system aligns with a user’s cognitive style over time. We
therefore apply CFT specifically in the context of immediate system use CRediT authorship contribution statement
and recognize that longer-term cognitive alignment remains an open
area for future investigation. We also cannot rule out the possibility that Arash Saghafi: Writing – review & editing, Writing – original draft,
perceived effort or user investment may have contributed to the Validation, Supervision, Methodology, Investigation, Formal analysis,
observed effects on performance of users with full categorization au- Data curation, Conceptualization. Poonacha Medappa: Writing – re-
tonomy. Although, the results from the partial autonomy condition view & editing, Writing – original draft, Validation, Methodology,
could offer support that the improved search precision and higher usage Investigation, Data curation, Conceptualization. Ariton Debrliev:
intentions were not only the result of effort and time investment with the Writing – original draft, Methodology, Data curation,
interface. Conceptualization.
5.3. Future research
Declaration of competing interest
There are several points of further research opportunities that we
wish to indicate. First and foremost, additional studies are required to The authors declare that they have no known competing financial
understand the deeper cognitive differences between exploratory and interests or personal relationships that could have appeared to influence
exploitive searches when the users create their own categories. It would the work reported in this paper.
11

A. Saghafi et al.                                                                                                                                                                                             D   e c i s  i o n    S  u  p p  o  r t   S  y  s t e m   s  196 (2025) 114499
Appendix A. Scale items
Table A1
Survey Questions - Adapted from [37].
1: I had limited control over the way the presented information was categorized.
2: In terms of my preferred way of viewing the information, the categorization was confined.
3: In terms of my preferred way of viewing the information, the categories were restricted.
4: Next time I need to perform such tasks, I would like to use this kind of categorization
5: Assuming I had access to the provided categorization, I would use this website again in the future.
6: Given I had access to the categorization offered by this site, I would use it to perform such tasks if needed.
QTrap: If you are reading this, please answer ‘somewhat disagree’
Appendix B. Validity and robustness
Table B1
Validity and Reliability of Constructs.
|     | Item               |     | Intention to use |     | Restrictiveness |     |
| --- | ------------------ | --- | ---------------- | --- | --------------- | --- |
|     | Intention to use 1 |     | 0.963            |     |                 |     |
|     | Intention to use 2 |     | 0.972            |     |                 |     |
|     | Intention to use 3 |     | 0.959            |     |                 |     |
|     | Restrictiveness 1  |     |                  |     | 0.896           |     |
|     | Restrictiveness 2  |     |                  |     | 0.900           |     |
|     | Restrictiveness 3  |     |                  |     | 0.948           |     |
Table B2
Reliability and convergent validity.
Cronbach’s Alpha
Average Variance Extracted
|     | Intention to use |     | 0.962 |     | 0.930 |     |
| --- | ---------------- | --- | ----- | --- | ----- | --- |
|     | Restrictiveness  |     | 0.902 |     | 0.837 |     |
Table B3
Discriminant validity – heterotrait-monotrait ratio.
|     |     | Categorization |     | Intention to use |     | Restrictiveness |
| --- | --- | -------------- | --- | ---------------- | --- | --------------- |
Categorization
| Intention to use |     | 0.333 |     |       |     |     |
| ---------------- | --- | ----- | --- | ----- | --- | --- |
| Restrictiveness  |     | 0.596 |     | 0.776 |     |     |
Appendix C. Scenarios
Information Exploitation Scenario:
Imagine you are an office manager tasked with purchasing the following items:
- Two new monitors for the office workers. The office needs a 24″ monitor and a 27″ monitor.
- The office microwave is broken! Find a microwave cheaper than $700 with at least 2-cubic foot of space.
- Please buy a corded Motorola brand phone with cordless handset.
- For calls from your PC you are supposed to buy an on-ear headphone with a visible microphone.
- A cellphone power bank.
- Finally, please find a pencil sharpener.
Information Exploration Scenario:
Suppose you are buying three distinct gifts for your best friend’s wedding to satisfy the following three criteria:
You know that one of the newlyweds is a cooking enthusiast, you also know that both of them are very active and enjoy
outdoor activities. In addition, you know that they love watching movies at home.
Appendix D. (Behavioral Data)
To extend our understanding of the consequences of categorization autonomy, we developed a set of hypotheses linking autonomy to users’
satisfaction, trust, and intentions to use the system. Hypothesis 5 posits that categorization autonomy increases user satisfaction, as the ability to
impose one’s own organizational logic enhances cognitive alignment and perceived control. Hypothesis 6 proposes that this relationship is mediated
12

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
by trust, such that autonomy fosters trust in the system, which in turn drives satisfaction. And, Hypothesis 7 suggests that greater satisfaction leads to
higher intentions to use the system, consistent with existing models of IS success and technology adoption. Fig. D-1illustrates the research model with
only the subjective variables (i.e., excluding H1 and H2, namely, Search Precision and Task Flexibility’s moderation effect).
Fig. D-1. Behavioral research model.
The results offer strong support for all three hypotheses. H5 was supported, with categorization autonomy significantly increasing satisfaction (β =
0.323, p =0.009). For H6, we found that categorization autonomy significantly increased trust (β =0.347, p =0.001), and that trust strongly predicted
satisfaction (β =0.858, p <0.001), fully mediating the direct effect of autonomy (which became non-significant when trust was included). This
provides evidence for full mediation, supporting H6. Finally, H7 was also strongly supported, as satisfaction emerged as a robust predictor of usage
intentions (β =0.935, p <0.001). Collectively, these findings reinforce the role of categorization autonomy not only in improving task performance,
but also in enhancing users’ affective and behavioral responses to the system through mechanisms of trust and satisfaction. Table D-1 offers the full
statistical analysis using regression.
Table D1
Regression analysis on additional behavioral hypotheses.
Hypothesis Path Beta p-value Supported
(Unstandardized)
H5 Categorization Autonomy - >Satisfaction 0.323 0.009 Yes
H6 Categorization Autonomy - >Trust 0.346 0.001 Yes
Trust - >Satisfaction (with Autonomy) 0.858 0 Yes
Categorization Autonomy - >Satisfaction (+Trust) 0.026 0.775 No (Full Mediation)
H7 Satisfaction - >Usage Intentions 0.935 0 Yes
Data availability [12] S. Kodali, S. Compton, Must-Have E-Commerce Features, Roadmap Report,
Forrester Research, 2022.
[13] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives
Data will be made available on request. on strategy selection, Inf. Syst. Res. 10 (1999) 356–374.
[14] R. Lukyanenko, J. Parsons, Y.F. Wiersma, The IQ of the crowd: understanding and
improving information quality in structured user-generated content, Inf. Syst. Res.
References 25 (2014) 669–689.
[15] R. Lukyanenko, J. Parsons, Y. Wiersma, M. Maddah, Expecting the unexpected:
[1] P. Zhang, F.F.H. Nah, I. Benbasat, Human-computer interaction research in effects of data collection design choices on the quality of crowdsourced user-
management information systems, J. Manag. Inf. Syst. 22 (2005) 9–14. generated content, MIS Q. 43 (2019) 623–647.
[2] J. Hauser, G. Urban, G. Liberali, M. Braun, Website morphing, Mark. Sci. 28 (2009) [16] A. Saghafi, Y. Wand, J. Parsons, Skipping class: improving human-driven data
202–223. exploration and querying through instances, Eur. J. Inf. Syst. 31 (2022) 463–491.
[3] S. Derry, Cognitive schema theory in the constructivist debate, Educ. Psychol. 31 [17] D. Arnott, G. Pervan, Eight key issues for the decision support systems discipline,
(1996) 163–174. Decis. Support. Syst. 44 (2008) 657–672.
[4] J. Parsons, Y. Wand, Using cognitive principles to guide classification in [18] J. March, Exploration and exploitation in organizational learning, Organ. Sci. 2
information systems modeling, MIS Q. 32 (2008) 839–868. (1991) 71–87.
[5] J. Smith, Prototypes, exemplars, and the natural history of categorization, Psychon. [19] A. Burton-Jones, D.W. Straub, Reconceptualizing system usage: an approach and
Bull. Rev. 21 (2013) 312–333. empirical test, Inf. Syst. Res. 17 (2006) 228–246.
[6] G. Lakoff, Women, Fire, and Dangerous Things: What Categories Reveal about the [20] A. Burton-Jones, C. Grange, From use to effective use: a representation theory
Mind, University of Chicago Press, Chicago, 2008. perspective, Inf. Syst. Res. 24 (2013) 632–658.
[7] J. Parsons, Y. Wand, Emancipating instances from the tyranny of classes in [21] A. Fishbach, M.J. Ferguson, The goal construct in social psychology, in: A.
information modeling, ACM Transac. on Database Syst. (TODS) 25 (2000) W. Kruglanski, E.T. Higgins (Eds.), Social Psychology: Handbook of Basic
228–268. Principles, 2nd ed., Guilford, New York, 2007, pp. 490–515.
[8] A.D. Moore, Python GUI Programming with Tkinter: Design and Build Functional [22] K.R. Larsen, A taxonomy of antecedents of information systems success: variable
and User-Friendly GUI Applications, Packt Publishing, Birmingham, 2021. analysis studies, J. Manag. Inf. Syst. 20 (2003) 169–246.
[9] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, [23] A. Taylor, H.R. Greve, Superman or the fantastic four? Knowledge combination and
present, and future of decision support technology, Decis. Support. Syst. 33 (2002) experience in innovative teams, Acad. Manag. J. 49 (2006) 723–740.
111–126. [24] Jenkins J.L., Denison A., Valacich J.S., Wilson D., Detecting goal-oriented vs.
[10] S. Al-Natour, I. Benbasat, R.T. Cenfetelli, The effects of process and outcome browsing users through behavior analysis, in: 2023 46th MIPRO ICT and
similarity on users’ evaluations of decision aids, Decis. Sci. 39 (2008) 175–211. electronics convention (MIPRO), IEEE, 2023, pp. 13–18.
[11] W. Kosinski, G. Dziczkowski, B. Gol´enia, K. Wegrzyn-Wolska, Towards an Optimal [25] R. Budiu, Search Is Not Enough: Synergy between Navigation and Search, Nielsen
Decision Support System, in: Decision Support Systems, Advances in, IntechOpen, Norman Group, 2014.
2010.
13

A. Saghafi et al. D e c i s i o n S u p p o r t S y s t e m s 196 (2025) 114499
[26] X. Liu, K. Werder, A. Maedche, Novice digital service designers’ decision-making [48] K.J. Preacher, A.F. Hayes, Assessing mediation in communication research, in: A.
with decision aids—a comparison of taxonomy and tags, Decis. Support. Syst. 137 F. Hayes, M.D. Slater, L.B. Snyder (Eds.), The Sage Sourcebook of Advanced Data
(2020) 113367. Analysis Methods for Communication Research, Sage, Thousand Oaks, 2008,
[27] Z. Kozareva, Everyone likes shopping! Multi-class product categorization for e- pp. 13–54.
commerce, in: Conference of the North American Chapter of the Association for [49] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, J. Dean, Distributed representations
Computational Linguistics, 2015, pp. 1329–1333. of words and phrases and their compositionality, Adv. Neural Inf. Proces. Syst. 26
[28] D. Romanov, V. Molokanov, N. Kazantsev, A.K. Jha, Removing order effects from (2013).
human-classified datasets: a machine learning method to improve decision making [50] Y.-L. Chen, C.-H. Hsiao, C.-C. Wu, An ensemble model for link prediction based on
systems, Decis. Support. Syst. 165 (2023) 113891. graph embedding, Decis. Support. Syst. 157 (2022) 113753.
[29] A. Castellanos, M.C. Tremblay, R. Lukyanenko, B. Samuel, Basic classes in [51] R.R. McCrae, Creativity, divergent thinking, and openness to experience, J. Pers.
conceptual modeling: Theory and practical guidelines, J. Associ Inform. Syst. 21 Soc. Psychol. 52 (1987) 1258–1265.
(2020) 1001–1044. [52] S.M.B. Thatcher, S.A. Brown, Individual creativity in teams: the importance of
[30] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, communication media mix, Decis. Support. Syst. 49 (2010) 290–300.
Science 185 (1974) 1124–1131. [53] S. Gregor, D. Jones, The anatomy of a design theory, J. Assoc. Inf. Syst. 8 (2007)
[31] G. Chapman, E. Johnson, The limits of anchoring, J. Behav. Decis. Mak. 7 (1994) 312–335.
223–242. [54] H.Y. Hung, Y. Hu, N. Lee, H.T. Tsai, Exploring online consumer review-
[32] I. Vessey, Cognitive fit: a theory-based analysis of the graphs versus tables management response dynamics: a heuristic-systematic perspective, Decis.
literature, Decis. Sci. 22 (1991) 219–240. Support. Syst. 177 (2024) 114087.
[33] P. Xu, L. Chen, R. Santhanam, Will video be the next generation of e-commerce [55] E. Choi, C. Kim, K. Lee, Consumer decision-making creativity and its relation to
product reviews? Presentation format and the role of product type, Decis. Support. exploitation–exploration activities: eye-tracking approach, Front. Psychol. 12
Syst. 73 (2015) 85–96. (2021) 3629.
[34] D. Baˇci´c, R. Henry, Advancing our understanding and assessment of cognitive [56] S. Bina, T. Kaskela, D.R. Jones, E. Walden, W.B. Graue, Incorporating evolutionary
effort in the cognitive fit theory and data visualization context: eye tracking-based adaptions into the cognitive fit model for data visualization, Decis. Support. Syst.
approach, Decis. Support. Syst. 163 (2022) 113862. 171 (2023) 113979.
[35] D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, [57] J.T. Gourville, The curse of innovation: a theory of why innovative new products
MIS Q. 19 (1995) 213–236. fail in the marketplace, HBS Marketing Research Paper (2005) 05–06.
[36] M. Silver, User perceptions of decision support system restrictiveness: an
experiment, J. Manag. Inf. Syst. 5 (1988) 51–65.
Arash Saghafi is an Assistant Professor of Information Systems at Ted Rogers School of
[37] W. Wang, I. Benbasat, Interactive decision aids for consumer decision making in e-
Management, Toronto Metropolitan University. His degrees include a BSc in Software
commerce: influence of perceived strategy restrictiveness, MIS Q. 33 (2009)
293–320. Engineering from Sharif University of Technology, and MM, MScB, and PhD from Uni-
versity of British Columbia. He was appointed as a lecturer and research fellow at Sauder
[38] J.W. Brehm, A Theory of Psychological Reactance, Academic Press, New York,
School of Business, and an Assistant Professor at Tilburg School of Economics and Man-
1966.
agement prior to joining Toronto Metropolitan University. His research has focused on
[39] S. Ebrahimi, M. Ghasemaghaei, I. Benbasat, The impact of trust and
information and knowledge representation, application of ontology in conceptual
recommendation quality on adopting interactive and non-interactive
recommendation agents: a meta-analysis, J. Manag. Inf. Syst. 39 (2022) 733–764. modeling, systems development methodologies, and empirical evaluation of design arti-
facts. His work has been published at the European Journal of Information Systems,
[40] A. Dafoe, B. Zhang, D. Caughey, Information equivalence in survey experiments,
Polit. Anal. 26 (2018) 399–416. Journal of Database Management, and proceedings of various AIS conferences.
[41] L.T. Benjamin Jr., Lecturing, in: S.F. Davis, W. Buskist (Eds.), The Teaching of
Psychology: Essays in Honor of W.J. McKeachie and C.L, Brewer, Lawrence Poonacha Medappa is an Assistant Professor in the Information Management group at the
Erlbaum, Mahwah, 2002, pp. 57–67. Department of Management at Tilburg University. Prior to joining Tilburg University, he
[42] T.J. Brown, J.C. Mowen, D.T. Donavan, J.W. Licata, The customer orientation of completed his Ph.D in Information Systems from HEC Paris. His research interests lie in the
service workers: personality trait effects on self and supervisor performance areas of project management, open-source software development, online communities,
ratings, J. Mark. Res. 39 (2002) 110–119. and methodological applications of machine learning techniques in research. His research
[43] E. Peer, G. Paolacci, J. Chandler, P. Mueller, Screening participants from previous has been published in top-tier journals such as Information Systems Research, European
studies on Amazon mechanical Turk and Qualtrics, SSRN E-J (2012) 1–5. Journal of Information Systems and in the proceedings of several leading conferences.
[44] S. Sudman, Applied Sampling, Academic Press, New York, 1976.
[45] J. Cortina, What is coefficient alpha? An examination of theory and applications,
Ariton Debrliev is a consultant at Gartner. He has a BSc in Business Administration and
J. Appl. Psychol. 78 (1993) 98–104.
MSc in Marketing Management from the Erasmus University, Rotterdam School of Man-
[46] C. Fornell, D. Larcker, Evaluating structural equation models with unobservable
agement, and a MSc in Information Management from Tilburg University, TiSEM. Main
variables and measurement error, J. Mark. Res. 18 (1981) 39–50.
research interest areas include: consumer behavior, decision-making, heuristics and
[47] A. Burton-Jones, P.N. Meso, Conceptualizing systems for understanding: an
biases.
empirical test of decomposition principles in object-oriented analysis, Inf. Syst.
Res. 17 (2006) 38–60.
14