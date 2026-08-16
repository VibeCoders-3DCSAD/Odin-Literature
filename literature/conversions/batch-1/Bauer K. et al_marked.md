---
conversion_metadata:
  converted_at: "2026-07-22T12:18:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bauer K. et al.pdf"
  source_pdf_sha256: "cf96908b7f4751ee2e88b95534736cc5fff6e67b506cacd7ffad8450e5833f85"
  page_count: 22
  markdown_char_count: 271724
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

This article was downloaded by: [27.49.19.50] On: 06 July 2026, At: 23:30
Publisher: Institute for Operations Research and the Management Sciences (INFORMS)
INFORMS is located in Maryland, USA

Information Systems Research

Publication details, including instructions for authors and subscription information:
http://pubsonline.informs.org

Expl(AI)ned: The Impact of Explainable Artificial
Intelligence on Users’ Information Processing

Kevin Bauer, Moritz von Zahn, Oliver Hinz

To cite this article:
Kevin Bauer, Moritz von Zahn, Oliver Hinz (2023) Expl(AI)ned: The Impact of Explainable Artificial Intelligence
on Users’ Information Processing. Information Systems Research 34(4):1582-1602. https://doi.org/10.1287/
isre.2023.1199

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License. You are free to download this work and share with others, but cannot change in any way or use
commercially without permission, and you must attribute this work as “Information Systems Research. Copyright ©
2023 The Author(s). https://doi.org/10.1287/isre.2023.1199, used under a Creative Commons Attribution License:
https://creativecommons.org/licenses/by-nc-nd/4.0/.”

Copyright © 2023 The Author(s)

Please scroll down for article—it is on subsequent pages

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations
research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning
opportunities for individual professionals, and organizations of all types and sizes, to better understand and use
O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.
For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

---

<!-- PAGE 2 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

https://pubsonline.informs.org/journal/isre

INFORMATION SYSTEMS RESEARCH 
Vol. 34, No. 4, December 2023, pp. 1582–1602 
ISSN 1047-7047 (print), ISSN 1526-5536 (online)

Expl(AI)ned: The Impact of Explainable Artificial Intelligence on 
Users’ Information Processing

Kevin Bauer,a,* Moritz von Zahn,b  Oliver Hinzb

a Information Systems Department, University of Mannheim, 68161 Mannheim, Germany; b Information Systems Department, Goethe 
University, 60323 Frankfurt am Main, Germany 
*Corresponding author 
Contact: kevin.bauer@uni-mannheim.de,

https://orcid.org/0000-0001-8172-1261 (KB); vzahn@wiwi.uni-frankfurt.de,

https://orcid.org/0000-0003-1160-1007 (MvZ); ohinz@wiwi.uni-frankfurt.de,

https://orcid.org/0000-0003-4757-0599 (OH)

Received:  June  11,  2021 
Revised:  June  2,  2022;  October  28,  2022 
Accepted:  December  17,  2022 
Published  Online  in  Articles  in  Advance: 
March  3,  2023

https://doi.org/10.1287/isre.2023.1199

Copyright:  ©  2023  The  Author(s)

Abstract.  Because of a growing number of initiatives and regulations, predictions of mod-
ern artificial intelligence (AI) systems increasingly come with explanations about why they 
behave the way they do. In this paper, we explore the impact of feature-based explanations 
on  users’  information  processing.  We  designed  two  complementary  empirical  studies 
where participants either made incentivized decisions on their own, with the aid of opaque 
predictions, or with explained predictions. In Study 1, laypeople engaged in the deliberately 
abstract investment game task. In Study 2, experts from the real estate industry estimated 
listing prices for real German apartments. Our results indicate that the provision of feature- 
based explanations paves the way for AI systems to reshape users’ sense making of infor-
mation  and  understanding  of  the  world  around  them.  Specifically,  explanations  change 
users’ situational weighting of available information and evoke mental model adjustments. 
Crucially, mental model adjustments are subject to the confirmation bias so that misconcep-
tions can persist and even accumulate, possibly leading to suboptimal or biased decisions. 
Additionally, mental model adjustments create spillover effects that alter user behavior in 
related yet disparate domains. Overall, this paper provides important insights into potential 
downstream consequences of the broad employment of modern explainable AI methods. In 
particular, side effects of mental model adjustments present a potential risk of manipulating 
user behavior, promoting discriminatory inclinations, and increasing noise in decision mak-
ing. Our findings may inform the refinement of current efforts of companies building AI 
systems and regulators that aim to mitigate problems associated with the black-box nature 
of many modern AI systems.

History: Alessandro Acquisti, senior editor; Jason Chan, associate editor. 
Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial- 
NoDerivatives 4.0 International License. You are free to download this work and share with others, 
but cannot change in any way or use commercially without permission, and you must attribute this 
work as  “Information Systems  Research. Copyright  © 2023  The Author(s).  https://doi.org/10.1287/ 
isre.2023.1199, used under a Creative Commons Attribution License: https://creativecommons.org/ 
licenses/by-nc-nd/4.0/.”

Funding: This work was supported by the Deutsche Forschungsgemeinschaft (DFG) (Projek 449023539),

Volkswagen Foundation (ML2MT), and LeibnizInstitute for Financial Research SAFE.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.1199.

Keywords:

explainable artificial intelligence • user behavior • information processing • mental models

1. Introduction
Contemporary  artificial  intelligence  (AI)  systems’  high 
predictive performance frequently comes at the expense 
of users’ understanding of why systems produce a certain 
output (Gunning et al. 2019, Meske et al. 2022). For AI sys-
tems that provide predictions to augment highly conse-
quential  processes  such  as  hiring  decisions  (Hoffman 
et al. 2018), investment decisions (Ban et al. 2018), or med-
ical  diagnosing  (Jussupow  et  al.  2021),  this  “black  box” 
nature  can  create  considerable  downsides.  These  issues 
include impaired user trust, reduced error safeguarding,

restricted  contestability,  and  limited  accountability  (see 
Rosenfeld and Richardson 2019 for a review). Having rec-
ognized  these  problems,  organizations  developing  AI 
and governments increasingly adopt principles and regu-
lations  (EU  2016,  2021;  Google  AI  2019;  Meta  AI  2021) 
effectively  stipulating  that  AI  systems  need  to  provide 
meaningful  explanations  about  why  they  make  certain 
predictions (Goodman and Flaxman 2017, Cabral 2021). 
In light of these developments, the implementation and 
use of explainable AI (XAI) methods are becoming more 
widespread and mandated by law.

1582

---

<!-- PAGE 3 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1583

The purpose of XAI methods is to make AI systems’ 
hidden  logic  intelligible  to  humans  by  answering  the 
question: Why does an AI system make the predictions it 
does? Thereby, XAI methods aim to achieve high predic-
tive  performance  and  interpretability  at  the  same  time. 
Many  state-of-the-art  XAI  techniques  convey  insights 
into  AI  systems’  logic  after  training  and  explain  beha-
viors  by  depicting  the  contribution  of  individual  input 
features  to  the  outputted  prediction  (Doshi-Velez  and 
Kim 2017). Although there is reason to believe that XAI 
can mitigate black-box problems (Bauer et al. 2021), the 
pivotal question is how users respond to modern expla-
nations,  given  that  the  human  factor  frequently  creates 
unanticipated,  unintended  consequences  even  in  well- 
designed information systems (Willison and Warkentin 
2013, Chatterjee et al. 2015).

Nascent research on human-XAI interaction examines 
how  explainability  affects  humans’  perceptions,  attitu-
des, and use of the system, for example, trust (Erlei et al. 
2020),  detection  of  malfunctioning  (Poursabzi-Sangdeh 
et al. 2021), (over)reliance (Bussone et al. 2015), and task 
performance  (Senoner  et  al.  2021).  Prior  research,  how-
ever,  does  not  consider  the  potential  consequences  of 
providing explanations for users’ situational information 
processing (the use of currently available information in 
the given situation) and mental models (cognitive repre-
sentations that encode beliefs, facts, and knowledge). By 
depicting the contribution of individual features to speci-
fic predictions, feature-based XAI enables users to recog-
nize previously unknown relationships between features 
and  ground  truth  labels  that  the  AI  system  autono-
mously  learned  from  complex  data  structures.  In  that 
sense, XAI may constitute the channel through which AI 
systems  impact  humans’  conceptualization  and  under-
standing of their environment. This effect could reinforce 
the already considerable influence contemporary AI sys-
tems have on human societies (Rahwan et al. 2019) by, 
for better or worse, allowing human users to adopt sys-
tems’ inner logic and problem-solving strategies. Despite 
the increasing (legally required) implementation of XAI 
methods, a systematic study of these effects is yet miss-
ing. The paper at hand aims to fill this important gap.

We ask three research questions. Does the additional 
provision of feature-based explanations affect AI system 
users’  situational  processing  of  observed  information? 
Does it affect users’ underlying mental models? What are 
important moderating factors? Consider, for instance, a 
loan officer who works with an AI system to predict an 
applicant’s  risk  parameters  and  determine  the  credit 
approval.  Because  of  legal  requirements  (e.g.,  Artificial 
Intelligence Act; EU 2021), the AI system recently started 
to  provide  feature-based  explanations,  showing  that  it 
strongly  relies  on  people’s  smartphone  charging  be-
havior  to  predict  creditworthiness.1 Although  previous 
research  examines  how  this  explanation  may  affect  the 
loan  officer’s  perceptions  of  the  system,  we  conjecture

that the explanation also, and maybe more importantly, 
affects his processing of currently available information 
and his underlying mental models of the determinants of 
creditworthiness. By changing mental models, explana-
tions  may  even  reshape  the  loan  officer’s  behaviors  in 
related domains beyond the loan approval decision, for 
example, assessing the faithfulness of his daughter’s new 
boyfriend based on the smartphone charging behavior.2

Considerable challenges arise when trying to answer 
our research questions. First, measuring how XAI meth-
ods  affect  users’  situational  processing  of  information 
and mental models is extremely difficult because these 
cognitive  processes  are  typically  unobserved.  Second, 
we  need  to  control  for  possible  external  cues,  unin-
tended stimuli, additionally attainable information, and 
preferences that may affect these cognitive processes in 
any given situation. Third, whether people interact with 
an (X)AI system, let alone rely on it, is highly endoge-
nous and depends on factors such as culture, technolog-
ical  literacy,  and  the  socio-technological  environment. 
Thus, isolating effects associated with the provision of 
explanations  in  addition  to  predictions  is  particularly 
demanding,  if  not  outright  impracticable,  in  a  natural 
(organizational)  setting.  To  address  these  challenges, 
we  rely  on  two  complementary,  incentivized  experi-
mental studies.

In  Study  1  (n  � 607),  laypeople  played  a  series  of 
investment games (Berg et al. 1995), making sequential 
economic transaction decisions in an intentionally ab-
stract  setting.  In  Study  2  (n  � 153),  experts  from  the 
real-estate  industry  predicted  listing  prices  for  real 
apartments located in Germany. Study 2 extends Study 
1  by  testing  the  generalizability  of  our  findings  and 
elaborating on mechanisms driving the results. In both 
studies, conditional on the treatment, participants either 
received no decision support, support from an AI system 
in  the  form  of  opaque  predictions  or  an  XAI  system 
with  predictions  plus  feature-based  explanations.  We 
answer our research questions by eliciting and compar-
ing changes in both participants’ decision-making pat-
terns and their beliefs about feature-label relationships.

The two studies strongly complement each other for 
three  reasons.  First,  laypeople  (Study  1)  and  experts 
(Study 2) are the two diametrical archetypes of AI sys-
tem  users  affected  by  growing  explainability  require-
ments. Studying both types’ responses to XAI methods 
enables  us  to  identify  possibly  differential  effects  and 
make inferences about the generalizability of our find-
ings.  Second,  we  consider  two  fundamental  types  of 
prediction problems where AI systems are frequently in 
use: transaction outcome predictions (Study 1) and price 
predictions (Study 2) (Ban et al. 2018, Rico-Juan and de 
La  Paz  2021).  Examining  the  two  settings  allows  us  to 
understand better whether the interplay between XAI and 
cognitive processes is task specific. Third, using local inter-
pretable model-agnostic  explanations (LIME) (Study 1)

---

<!-- PAGE 4 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1584

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

and SHapley Additive exPlanations (SHAP) explanations 
(Study 2), the two most popular feature-based XAI meth-
ods  (Gramegna  and  Giudici  2021),  allows  us  to  draw 
more  general  conclusions  about  the  interplay  between 
feature-based explainability and cognitive processes.

Our  findings  paint  a  consistent  picture:  Providing 
explanations is the critical factor that enables AI systems 
to influence the way people make sense of and leverage 
information, both situationally and more permanently. 
Crucially, we find an asymmetric enduring effect that can 
foster  preconceptions  and  spill  over  to  other  decisions, 
thereby promoting certain (possibly biased) behaviors.

Our paper proceeds as follows. Section 2 presents the-
oretical  foundations,  whereas  Section  3 explains  our 
experimental studies and results. Section 4 concludes by 
discussing our results, the limitations of our work, and 
directions for future research.

2. Theory
In this section, we first discuss modern XAI methods (Sec-
tion  2.1).  Subsequently,  we  outline  the  relation  between 
providing explanations and cognitive processes (Section 
2.2) and discuss our work’s contribution to the literature 
(Section 2.3).

2.1. Explainable AI
Following Doshi-Velez and Kim (2017), we conceptual-
ize XAI as methods that possess the ability to present in 
understandable  terms  to  a  human  why  an  AI  system 
makes certain predictions. Over the last couple of years, 
researchers  developed  ample  XAI  methods  that  help 
elucidate  the  opaque  logic  of  machine  learning  (ML)- 
based AI systems (Ribeiro et al. 2016, Lundberg and Lee 
2017, Koh and Liang 2017, Lakkaraju et al. 2019). Very gen-
erally, XAI methods aim to alleviate problems associated 
with the black-box nature (e.g., distrust, lack of accountabil-
ity, and error safeguarding) while maintaining a high level 
of prediction accuracy (Bauer et al. 2021).

Our  study  focuses  on  feature-based  XAI  methods, 
hereafter XAI methods, that can explain the behavior of 
any ML-based AI system by showing the contribution 
of  individual  features  to  the  prediction.  We  do  so  for 
several  reasons.  First,  these  explanations  are  the  most 
widespread in practice (Bhatt et al. 2020, Senoner et al. 
2021,  Gramegna  and  Giudici  2021).  Second,  they  are 
highly intuitive and straightforward to interpret as they 
satisfy most requirements for human-friendly explana-
tions (Molnar 2020). Third, they are typically applicable 
to systems using structured and unstructured data (Gar-
reau and Luxburg 2020). Fourth, these methods can ex-
plain  individual  predictions,  local  explainability,  which 
might be the only method legally compliant with (upcom-
ing) regulations (Goodman and Flaxman 2017).

Many researchers recognize two related XAI methods 
as state-of-the-art: LIME and SHAP (Gramegna and Giudici

2021, Molnar 2020). LIME (Ribeiro et al. 2016) and SHAP 
(Lundberg and Lee 2017) provide explanations through 
additive  feature  attributions,  that  is,  linear  models  that 
depict the numeric contribution of each feature value to 
the overall black box model prediction. Both approaches 
learn  these  interpretable  “surrogate  models”  on  input- 
prediction pairs of the black box model and are applica-
ble to virtually all classes of ML models, that is, are model 
agnostic.  On  the  individual  level,  SHAP  and  LIME 
provide contrastive explanations that inform users why 
predictions for a specific instance diverge from the pre-
diction  for  an  average  instance  (Molnar  2020).  For 
example,  if  the  SHAP  value  for  the  feature  Balcony 
equals +500 (�200), it indicates that having a balcony 
marginally increases (decreases) the current apartment’s 
listing price prediction by $500 ($200). The big difference 
between LIME and SHAP is the way of estimating the 
additive  feature  attributions.  LIME  creates  synthetic, 
perturbed data points in the local neighborhood of the 
observation of interest and fits a weighted linear model 
to  explain  the  relationship  between  the  synthetic  data 
and  the  relevant  black  box  predictions.  Importantly, 
LIME weights synthetic instances based on their proxim-
ity  to  the  original  data  point.  By  contrast,  SHAP  is 
inspired by coalitional game theory and treats input fea-
tures  as  a  team  of  players  that  cooperate  to  generate  a 
payoff (the prediction). The method essentially estimates 
the  marginal  contribution  of  each  player  to  the  overall 
payoff, Shapley values (Shapley 1953), using a linear model 
that weights instances based on characteristics of coalitions. 
Given  these  mathematical  differences,  the  two  methods 
can produce (slightly) different feature attributions for the 
same  instance.  However,  from  the  perspective  of  a  user 
who  is  not  familiar  with  these  details,  the  intuition  and 
interpretation of the two methods’ explanations are rea-
sonably similar (Molnar 2020). Notably, LIME and SHAP 
closely relate to the seminal description of Gregor and Ben-
basat (1999) of “why and why not explanations” in the con-
text of knowledge-based expert systems.

With  the  development  of  modern  explainability  meth-
ods, research on the impact of contemporary XAI on user 
behavior  has  become  increasingly  essential  (Vilone  and 
Longo  2021).  Nascent  research  in  this  domain  typically 
focuses on how explanations affect user attitudes and reli-
ance  on  the  AI  system  (Lu  and  Yin  2021).  These  studies 
produce  mixed  evidence  on  the  consequences  of  XAI  on 
decision performance, user trust, perception, and decision- 
making performance. Several studies depict that explana-
tions can enhance trust in and positive perceptions of the 
system (Rader et al. 2018, Dodge et al. 2019, Yang et al. 
2020),  whereas  others  provide  reversed  evidence  (Erlei 
et  al.  2020,  Poursabzi-Sangdeh  et  al.  2021).  Although 
prior  studies  produce  important  insights  regarding  the 
interplay  between  XAI  and  user  perceptions,  none  of 
them considers that the additional provision of explana-
tions  may  also  reshape  users’  information  processing,

---

<!-- PAGE 5 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1585

both  situationally  and  more  permanently.  For  instance, 
using SHAP to show the contribution of input features to 
a creditworthiness prediction may not only affect a loan 
officer’s perception of the AI system in use. Instead, she 
may  process  currently  available  information  about  the 
applicant differently and develop a novel understanding 
of the determinants of creditworthiness, that is, adjust her 
mental  model.  With  the  increasing  adoption  of  explain-
ability principles by organizations (Google AI 2019, Meta AI 
2021) and the growing number of regulatory transparency 
requirements  (EU  2016,  2021),  it  is  pivotal  to  understand 
how contemporary XAI methods influence cognitive pro-
cesses  that  lie  at  the  heart  of  people’s  knowledge, 
behavior, and problem-solving capabilities.

2.2. Cognitive Perspective on XAI Employment
Through  feature-based  explanations  about  an  AI  sys-
tem’s  prediction,  human  users  can  observe  possibly 
unknown  feature-label  relationships  that  the  system 
learned from complex data structures by itself (Agarwal 
and Dhar 2014, Berente et al. 2021). Although providing 
explanations, in general, can have a variety of cognitive 
effects,  researchers  across  disciplines  generally  agree 
that they primarily enhance people’s understanding of 
someone  or  something,  improve  reasoning,  and  facili-
tate learning (Gregor 2006, Malle 2006). From a cogni-
tive perspective, obtaining explanations can entail two 
effects: First, it may change people’s situational proces-
sing  of  available  information:  their  use  of  available 
information  while  observing  explanations.  Second,  it 
can lead to an adjustment of their beliefs about feature- 
label  relationships  the  AI  system  inherently  models: 
their mental representation of real-world processes. In 
this paper, we follow previous work in information sys-
tems and rely on the “Mental Models Framework” to con-
ceptualize relevant cognitive processes (Vandenbosch and 
Higgins 1996, Lim et al. 1997, Alavi et al. 2002).

Mental  models  are  “all  forms  of  mental  representa-
tion, general or specific, from any domain, causal, inten-
tional or spatial” (Brewer 1987, p. 193), encoding beliefs, 
facts, and knowledge (Jones et al. 2011). Through imagi-
nary  manipulations  of  model  components,  people  can 
reason  and  make  inferences  about  how  to  solve  pro-
blems  (Rouse  and  Morris  1986).  Much  of  the  people’s 
decision making is based on these simulations that figu-
ratively create informal algorithms for carrying out spe-
cific tasks (Johnson-Laird et al. 2017). For instance, real 
estate  agents  can  mentally  simulate  how  listing  prices 
might change if an apartment for sale had a balcony.

When  people  perform  tasks,  they  draw  on  relevant 
mental models that guide their processing of incoming 
information to form expectations and make (expectedly) 
optimal decisions. Working with an AI system that pro-
vides black box predictions, that is, information relevant 
to the task, allows people to reflect on their own expecta-
tions and compare it to the machine prediction (Sch¨on

2017). This mental process might entice people to revise 
their  expectations  and  thus  make  different  decisions 
because  the  machine  prediction  effectively  substitutes 
for  people’s  own  mental  model  driven  formation  of 
expectations (Agrawal et al. 2019). However, the black 
box  nature  does  not  allow  users  to  directly  compare 
their underlying beliefs and logic with that of the AI sys-
tem.  This  comparison  can  only  occur  when  they  learn 
how the system combines available information to arrive 
at a prediction. In the previous example, the real estate 
agent may have access to an XAI system that provides a 
listing  price  prediction  together  with  an  explanation  of 
how  specific  apartment  attributes  contribute  to  it.  The 
agent can compare the explanation to her own initial per-
ception  of  the  individual  attribute  contributions  to  the 
listing price. As a result, the agent may detect inconsis-
tencies  that  prompt  her  to  revise  her  logic  by  putting 
more or less emphasis on specific information currently 
available  to  evaluate  the  apartment.  This  explanation- 
enabled  situational  process  (Sch¨on  2017)  can  reconcile 
the  distinct  logic  that  humans  and  machines  apply  to 
arrive at a certain assessment. From this perspective, pro-
viding explanations on top of predictions may constitute 
a pivotal factor in allowing users to reflect on how they 
leverage  information  to  solve  a  problem  and  adapt  it 
according to the AI system’s logic for the given task.

Apart from situationally changing cognitive processes 
that  shape  the  current  decision,  the  interaction  between 
mental  models  and  explanations  may  also  yield  lasting 
effects  because  mental  models  possess  the  dynamic 
capacity  to  change  (Jones  et  al.  2011).  Repeatedly  ob-
serving explanations about how feature X contributes 
to prediction  ˆY and engaging in reflection processes may 
evoke adjustments of the underlying mental model in use. 
Following Vandenbosch and Higgins (1996), exposure to 
external stimuli, here explanations, can lead to two mental 
model  adjustment  processes:  maintenance  and  building. 
Under  mental  model  maintenance,  people  feel  encour-
aged to maintain or reinforce current beliefs and decision- 
making rules. This process occurs when they perceive or 
select new information to fit into their current beliefs and 
routines.  Under  mental  model  building,  individuals 
profoundly  restructure  or  build  new  mental  models  in 
response  to  handling  novel,  disconfirming  information. 
As a result of these processes, individuals may adopt dif-
ferent beliefs about how X contributes to the real label Y, 
enticing  them  to  process  information  differently  even 
when explanations are no longer present. Put differently: 
users  may  not  merely  combine  situationally  observed 
explanations  with  their  own  logic  to  solve  a  given  task. 
Instead,  observing  the  system’s  logic  may  more  funda-
mentally reshape users’ way of solving problems in gen-
eral, that is, evoke learning. Therefore, users may exhibit 
different problem-solving strategies whenever they draw 
on the explanation-adjusted mental model, even in situa-
tions where they do not observe explanations anymore.

---

<!-- PAGE 6 -->

1586

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

In sum, cognitive theories give reason to believe that 
providing  explanations  in  addition  to  predictions  can 
influence users’ processing of information about feature 
X, both situationally and more fundamentally. Because 
of the latter effect, modern XAI methods may constitute 
a  cornerstone  of  effective  knowledge  transfers  from 
ML-based AI systems to human users, helping them to 
learn from the AI how X relates to Y. Hence, explana-
tions  could  facilitate  learning  machine  knowledge:  new 
knowledge  AI  systems  autonomously  learned  from 
Big  Data  and  previously  missed  by  domain  experts 
(Teodorescu et al. 2021, van den Broek et al. 2021).

2.3. Contribution to the Literature
Our study complements three different streams of liter-
ature.  The  first  and  most  closely  related  line  of  work 
studies the interplay between XAI techniques and user 
behavior  (see  Rosenfeld  and  Richardson  (2019)  and 
Vilone and Longo (2021) for an overview). About two 
decades  ago,  several  studies  found  that  suitably  de-
signed explanations about the functioning and purpose 
of legacy knowledge-based expert systems can increase 
users’ trust in the systems, improve users’ perceptions 
of  the  system,  and  enhance  decision-making  perfor-
mance (Dhaliwal and Benbasat 1996, Gregor and Benba-
sat  1999,  Ji-Ye  Mao  2000,  Wang  and  Benbasat  2007). 
However, these expert systems codify knowledge from 
human experts as explicit procedures, instructions, rules, 
and constraints in a digital format. They do not represent 
machine knowledge that modern ML-based AI systems 
learn  independently  of  domain  experts  by  training  on 
large data sets (van den Broek et al. 2021). Given the 
inherent distinctions between expert systems and ML- 
based AI systems in terms of encoded knowledge, con-
temporary explainability methods present an entirely 
different  form  of  reasoning  to  users,  namely  that  of 
machines (Vilone and Longo 2021, Meske et al. 2022). 
More recent research on the impact of explainability on 
user  behavior  mainly  focuses  on  how  contemporary 
XAI methods impact users’ perceptions of the AI sys-
tem.  This  nascent  literature  shows  that  explainability 
often improves reliance on and trust in the system (Bus-
sone et al. 2015), fairness perceptions (Dodge et al. 2019), 
human-AI collaboration (Yang et al. 2020), task efficiency 
(Senoner et al. 2021), and users’ understanding of the sys-
tem’s  malfunctions  (Rader  et  al.  2018).  However,  there 
is  also  evidence  of  disadvantages  relating  to  infor-
mational  overload  (Poursabzi-Sangdeh  et  al.  2021), 
reduced user trust (Erlei et al. 2020), and overreliance 
(Bussone et al. 2015). Moreover, explanations that are 
unstable  and  sensitive  even  to  small  perturbations  to 
inputs have the potential to mislead human users into 
trusting a problematic black box, for example, by selec-
tively  providing  explanations  that  conceal  biased

behaviors and malfunctions (Kaur et al. 2020, Lakkar-
aju  and  Bastani  2020).  Hence,  explanations  may  be  a 
security  concern  if  adversaries  use  perturbations  of 
inputs  and  model  attributes  to  produce  intentionally 
misleading  explanations  that  manipulate  users’  trust 
and behaviors (Ghorbani et al. 2019). We complement 
this  pivotal  and  insightful  work  by  examining  the 
impact of contemporary XAI on users’ situational infor-
mation processing and mental models. Understanding 
how the provision of explanations about the workings 
of  ML-based  AI  systems  may  reshape  these  cognitive 
processes  is  pivotal  for  anticipating  the  downstream 
consequences  of  this  technology  on  human  societies 
and designing effective transparency and explainability 
regulations.

The second set of literature we complement explores 
the mechanisms of learning in socio-technological envir-
onments.  A  common  theoretical  foundation  builds  on 
Bayes  rule  as  a  rational  benchmark  of  how  humans 
accommodate  new  information  (Holt  and  Smith  2009). 
However,  research  has  shown  systematic  deviations 
from Bayes’ rule. Reasons include over- or underweight-
ing  of  new  information  (Rabin  and  Schrag  1999)  and  a 
general tendency to asymmetrically discount information 
conflicting with prior beliefs while readily internalizing 
confirming information (Yin et al. 2016). We complement 
this research stream by showing how human users devi-
ate from Bayes rule in the context of learning from mod-
ern AI systems. Notably, there exists a limited number of 
prior  research  examining  how  black  box  predictions 
change users’ decision-making habits (Abdel-Karim et al. 
2020, 2022; F ¨ugener et al. 2021a, b; Jussupow et al. 2021). 
Relatedly, in a formal model, Agrawal et al. (2019) show 
that  the  predictions  of  black  box  AI  systems  can  alter 
users’ abilities by providing them with incentives to learn 
to assess the (negative) consequences of their actions for 
the  task  supported  by  the  AI.3 None  of  these  studies, 
however, examines the role of feature-based explanations 
in learning, which could pave the way for more funda-
mental changes in the way users understand real-world 
processes.  Our  paper  intends  to  fill  this  gap.  We  study 
how the provision of explanations about how an AI sys-
tem solves prediction tasks allows users to integrate the 
presented machine knowledge into their mental models, 
that is, learn from XAI. A better understanding of how 
explainability  may  contribute  to  machine  teaching,  the 
notion that AI systems first learn novel knowledge that 
experts  neither  conceive  nor  anticipate  from  data  and 
then  transfer  this  knowledge  to  human  users  (Abdel- 
Karim  et  al.  2020),  is  particularly  significant  given  the 
growing requirements to implement explainability meth-
ods when using AI systems.

The third stream of literature we add to studies how 
humans collaborate with computerized systems to solve

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

---

<!-- PAGE 7 -->

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1587

Figure 1.  Structure of Empirical Studies

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Notes.  We provide an overview of the main sequence of our two empirical studies.

problems.  Previous  research  in  this  area  dates  back 
decades.  Several  studies  document  that  humans  resist 
using computerized decision aids, despite possible per-
formance  benefits  (Kleinmuntz  1990),  whereas  others 
find that humans possess a strong preference for using 
them (Dijkstra 1999). With the growing employment of 
modern  AI  systems  in  a  broad  range  of  domains,  the 
examination of human-machine collaboration has seen 
a considerable resurgence, for example, in the domain 
of  finance  (Ge  et  al.  2021),  medicine  (Jussupow  et  al. 
2021),  customer  service  (Schanke  et  al.  2021),  and  on- 
demand  tasks  (F ¨ugener  et  al.  2021a).  Research  on 
“centaur”  systems  (Goldstein  et  al.  2017,  Case  2018) 
documents  how  hybrid  human-AI  systems  (i.e.,  cen-
taur  systems)  achieve  superior  results  in  comparison 
with the entities operating independently (Dellermann 
et  al.  2019,  Tschandl  et al.  2020),  promising  consider-
able benefits from successful human-AI collaboration. 
Several  factors  moderate  the  interaction  of  humans 
and AI systems including the perceived subjectivity of 
the task (Castelo et al. 2019, Logg et al. 2019), seeing the 
system err (Dietvorst et al. 2015), being able to modify 
predictions (Dietvorst et al. 2018), the divergence bet-
ween actual and expected predictive performance (Jus-
supow  et  al.  2020),  and,  most  importantly  for  our 
research,  understanding  the  system’s  internal  logic 
(Gregor and Benbasat 1999, Hemmer et al. 2021). Fol-
lowing our conjecture that explanations pave the way 
for  AI  systems  to  affect  people’s  cognitive  processes, 
contemporary XAI methods introduce another layer of 
complexity  in  human-AI  interaction  and  its  success: 
an  interaction  between  machine  and  human  problem- 
solving strategies. Our work provides novel insights into 
whether and under what circumstances people prefer to 
rely on their own way of leveraging information or will-
ingly adjust it according to machine explanations. In this 
sense, our work contributes to the literature on (hybrid) 
human-AI  collaboration  by  analyzing  the  underlying 
cognitive processes that may facilitate or hinder the reali-
zation of the promise of this technology.

3. Empirical Studies
We now present the design and results of Studies 1 and 
2.  In  both  studies,  participants  made  decisions  under 
uncertainty (providing loans and predicting apartment 
listing  prices)  either  with  the  aid  of  an  opaque  AI,  an 
explainable AI, or without any support. We paid partici-
pants  according  to  their  decision-making  performance 
to reveal actual preferences and beliefs.4 We implemen-
ted  both  studies  using  oTree, Python,  and  HTML  and 
ran  them  online.  In  Study  1,  we  recruited  607  partici-
pants  on  Prolific  and  let  them  engage  in  deliberately 
abstract  investment  games  (Berg  et  al.  1995).  Results 
allow us to observe how the provision of explanations 
on  top  of  predictions  shapes  information  processing 
and  mental  models  for  laypeople  in  a  very  general 
sequential transaction domain. Study 2 extends the first 
study  by  testing  the  generalizability  of  mental  model 
adjustments  regarding  the  task  domain  (listing  price 
predictions), decision-maker expertise, and the explana-
tion  presentation,  and  elaborates  on  important  asym-
metric effects. With the help of our industry partner, the 
Real Estate Association Germany (IVD), we recruited 153 
experts  from  the  real  estate  industry  to  participate  in 
Study  2.  We report  the designs  and  results of  the  two 
studies consecutively. Figure 1 portrays an overview of 
the experimental designs.

3.1. Study 1
3.1.1. Design.  In  Study  1,  participants  repeatedly  en-
gaged  in  one-shot  investment  games  (Berg  et  al.  1995) 
that possess the following structure. An investor receives 
10 monetary units (MU). The investor initially observes 
10 deliberately abstract borrower characteristics and deci-
des whether  to  invest  her 10 MU  with the borrower.  If 
she does not invest, the game ends without the borrower 
making a decision, and both the investor and borrower 
earn a payoff of 10 MU. If she invests, the borrower pos-
sesses 30 MU and can keep the whole amount without 
repercussions.  Crucially,  the  borrower  can  repay  the

---

<!-- PAGE 8 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1588

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

investor 10 MU, thereby reciprocating the investor’s ini-
tial trust. In case of repayment, the investor receives 20 
MU  (we  double  the  amount);  otherwise,  the  investor 
earns  0  MU  while  the  borrower  gets  30  MU.  The  bor-
rower, in the absence of sufficiently strong social motives, 
for example, altruism, egalitarian concerns, or moral pre-
ferences  (Miettinen  et  al.  2020),  will  not  make  a  repay-
ment and maximize his personal income. As a result, the 
payoff structure of the investment game is of an adver-
sarial nature from the investor’s perspective because her 
material well-being is at the mercy of the borrower if 
she invests. The investor loses her initial investment of 
10 MU whenever the borrower pursues pure income- 
maximizing  or  adversarial  motives  like  wanting  to 
minimize  the  investors’  payoffs.  Given  this  payoff 
structure, an income-maximizing investor in the exper-
iment  will  only  invest  if  (i)  her  belief  that  the  bor-
rower’s  motive  leads  him  to  repay  her  is  sufficiently 
strong, and (ii) she ultimately judges that the prospect 
of doubling her income is worth risking the loss of her 
investment.5 Study 1 participants always played as inves-
tors. Borrowers are subjects from a previous incentivized 
field study who had to decide on repayment assuming 
an initial investment; that is, they have already commit-
ted  to  a  repayment  decision  and  cannot  strategically 
change this choice ex post. We did not provide inter-
mediary  feedback  to  prevent  the  development  of  idio-
syncratic  expertise,  experience,  or  investment  strategies 
that  may  confound  our  results.  We  randomly  matched 
investor and borrower decisions to determine game out-
comes at the end of the study and pay both according to 
the earned MU.

Study  1  comprised  a  baseline  (AI)  and  a  treatment 
(XAI) condition, each with three stages.6 In Stage I, each 
participant  made  10  investment  decisions  for  distinct, 
randomly drawn borrowers without intermediary feed-
back. They  always observed the 10  characteristics  of a 
borrower and did not obtain any aid. The idea is that the 
10  borrower  characteristics  allow  investors  to  get  an 
idea of the likelihood that an individual borrower will 
make a repayment, for whatever motives, and to assess 
whether it is worth taking the risk of losing their invest-
ment. We deliberately chose 10 unintuitive traits corre-
lated  with  a  person’s  repayment  inclination  so  that 
participants  did  not  possess  strong  prior  beliefs  about 
the  informativeness  of  characteristics  for  someone’s 
repayment  behavior  (see  Table  4  in  the  online  appen-
dix). The main reason for choosing just these character-
istics  is  that  previous  empirical  tests  have  shown  that 
they are appropriate features for developing an AI sys-
tem that accurately predicts repayment with which par-
ticipants  interact  in  Stage  II.  Importantly,  participants 
learned that the AI system makes predictions based on 
the same 10 borrower characteristics they also observe, 
mitigating concerns that they believed the AI system to 
have access to more information.

Stage II introduced our treatment variation. Partici-
pants  made  20  decisions  for  new  random  borrowers 
observing  all  10  borrower  traits.  Additionally,  base-
line participants saw an AI system’s prediction about 
whether  borrowers  will  repay  an  initial  investment. 
Again, we did not provide intermediary feedback. We 
trained the AI system on 1,054 distinct data points col-
lected in a previous field study, the same data set that 
the borrowers that participants encounter in the exper-
iment stem from (see the online appendix for details).7
The system did not continue to learn during the experi-
ment.  Treatment  participants,  on  top  of  predictions, 
observed  LIME  explanations  (Ribeiro  et  al.  2016)  for 
each borrower characteristic, informing them of its con-
tribution  to  the  repayment  prediction.  Revealing  LIME 
values  on  top  of  identical  predictions  constituted  the 
treatment  variation.  As  is  often  the  case,  we  depicted 
LIME values graphically using colored bars of different 
lengths. Participants received detailed information about 
the model, input features, performance on a representa-
tive test set, and how to interpret LIME explanations.

Stage III perfectly mirrored Stage I. Importantly, par-
ticipants engaged with the same borrowers from Stage I 
in random order. We did not draw participants’ atten-
tion  to  this  fact  to  alleviate  concerns  about  the  experi-
menter’s  demand  effect.  The  study  concluded  with  a 
brief questionnaire on socio-economic control variables.

3.1.2. Results.  Throughout our analyses of Study 1, we 
mainly rely on the following regression model:

Yijs � β1 · Xj + β2 · (Xj × Is) + β3 · (Xj × Expli)
+ β4 · (Xj × Expli × Is) + γijs + ɛ:

(1)

Yijs  is  a  dummy  indicating  whether  participant  i  in-
vested with borrower j in Stage s. Hence, β(cid:0)coefficients 
measure variation in the probability to invest with a bor-
rower, and Xj is a vector reflecting the 10 observed bor-
rower traits, the overall prediction, and LIME values.8
Most relevant to our analyses, Is  and Expli  are dummy 
variables,  respectively,  indicating  whether  a  decision 
takes place in Stage s compared with Stage I (i.e., Stage I 
serves as the reference category) and whether partici-
pant  i  is  in  the  XAI  treatment  (observes  explanations 
on  top  of  predictions  in  Stage  II),  and  γis  represents 
individual-state fixed effects. We report standardized 
regression coefficients with robust standard errors. Our 
main  interest  lies  in  the  interaction  terms  β3  and  β4, 
respectively,  capturing  the  isolated  effects  of  observing 
the prediction and additionally observing LIME explana-
tions.  As  β4  constitutes  a  difference-in-difference  (DiD) 
estimator, it is pivotal to check that before the interven-
tion,  there  are  no  treatment  differences  (parallel  trends 
assumption).  Regression  analyses  reveal  that  baseline 
and treatment participants in Stage I did not place signifi-
cantly different weight on any trait; hence, the use of a

---

<!-- PAGE 9 -->

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1589

DiD identification strategy appears generally valid. Nev-
ertheless, because participants placed significant weight 
on  Gender,  Conscientiousness,  Neuroticism,  and  Younger 
Siblings  in  only  one  of  the  two  conditions,  there  is  still 
some  concern  about  the  appropriate  interpretation  of 
DiD estimates for these traits.9 To avoid drawing incor-
rect  conclusions,  we  conservatively  refrain  from  inter-
preting these traits’ estimates while still including them 
as controls in the model.

3.1.2.1. Situational Information Processing.  We start 
analyzing  how participants’ weighting  of  borrower char-
acteristics  changed  from  Stage  I  to  II,  that  is,  changes  in 
participants’  situational  information  processing.  Figure  2
illustrates our results. Figure 2(a) depicts the average LIME 
values (color saturation) participants observed for different 
feature  values  (y  and  x  axis).  Higher  positive  (negative) 
LIME values depict a higher positive (negative) contribu-
tion  of  a  given  feature  value  to  the  predicted  probability 
that a borrower makes a repayment. Figure 2(b) portrays 
how the provision of predictions and explanations affected 
the  weighting  of  a  given  borrower  trait.  The  diamond 
marker represents the original weighting in Stage I (β1). 
The  dashed  and  solid  arrows,  respectively,  illustrate 
the  isolated  effects  of  observing  predictions  (β3)  and 
additional explanations (β4). Depicted results stem from 
regressions reported in Table 9 in the online appendix.

There are two main insights. First, prediction effects 
in Figure 2(b) suggest that the provision of opaque pre-
dictions  generally  decreased  the  weight  participants 
placed  on  observed  borrower  traits.  On  average,  the 
absolute  magnitude  of  coefficients  changed  by  63.6%. 
Although only the estimates for Agreeableness, Patience, 
and  Older  Siblings  are  significant,  predictions  reduced 
the  absolute  magnitude  of  all  variables.  Second,  the

provision of explanations on top of predictions entailed 
significant weight changes that mirror the relationship 
between  borrower  traits  and  repayment  behavior  as 
depicted by the LIME values. Here, the average magni-
tude  of  absolute  weight  changes  equals  73.9%.  Figure 
2(a)  shows  that  the  predicted  repayment  probability 
markedly decreases (increases) with a borrower’s level 
of  Competitiveness  (Patience).  Figure  2(b)  reveals  that 
these are the two traits whose weighting the provision 
of explanations significantly fostered: observing expla-
nations rendered the relationship between a borrower’s 
Competitiveness (Patience) and a participant’s investment 
likelihood significantly more negative (positive). Nota-
bly, explanations as such increased the absolute magni-
tude  of  the  coefficient  for  Competitiveness  (Patience)  by 
240.0%  (94.6%). LIME  values  reveal  that  Agreeableness, 
the  trait  participants  initially  weighted  the  most,  has 
almost no impact on the repayment prediction. Accord-
ingly, we find that the provision of explanations led to a 
significant decrease in the magnitude of the weight parti-
cipants placed on this trait (�44.7%). Additional analyses 
confirm that LIME values for these three characteristics 
had  a  significantly  positive  influence  on  participants’ 
investment decisions, corroborating the notion that parti-
cipants paid attention to and adjusted their weighting of 
traits according to observed explanations (see Table 11 in 
the online appendix). Taken together, participants signifi-
cantly  adjusted  their  weighting  of  information  in  the 
direction of observed explanations for (i) the trait they ini-
tially perceived as most important and (ii) the traits LIME 
highlighted  as  most  important.10 Finally,  although  not 
shown in the Figure 2 for ease of interpretation, regres-
sion  analyses  further  reveal  that  explanations  signifi-
cantly  reduced  the  weight  participants  placed  on  the 
prediction  as  such  (magnitude  of  coefficient  decreased

Figure 2.  (Color online) Prediction and Explanation Effects on Situational Information Processing

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Notes.  We illustrate how the provision of opaque predictions and LIME explanations on top of predictions affect participants situational informa-
tion processing. (a) LIME values (z axis) for different feature values (x axis) participants observed in the study. For the binary feature Older sib-
lings, we show the LIME values for No and Yes at the outer limits of the continuous feature scale. (b) Estimated prediction and explanation 
effects, respectively, of β3 and β4 in Model (1) with s � 2. Initial values represent β1. We denote significance levels by *p < 0.1, **p < 0.05, and ***p 
< 0.01.

---

<!-- PAGE 10 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1590

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

by 26.8%); that is, they were less likely to follow a predic-
tion that a borrower makes a repayment.11

Result  1.1. Observing  explanations  changed  participants’ 
situational  processing  of  the  overall  prediction  and  borrower 
traits  that  explanations  or  they  themselves  consider  most 
important. The direction of adjustments mirrors explanations.

Result  1.1 agrees  with  our  theoretical  elaborations: 
People adjust their situational information processing in 
response and according to explanations they currently 
observe. Notably, elicited expectations about the predic-
tion accuracy did not differ significantly for predictions 
with or without explanations (71.8% and 70.6%, respec-
tively;  p  � 0.751,  Wilcoxon  rank-sum  test).  Therefore, 
changes in the weighting of predictions do not seem to 
result  from  lower  performance  expectations.  Next,  we 
test the conjecture that explanations affect beliefs about 
the  relationship  between  borrower  characteristics  and 
repayment behavior, that is, mental models.

3.1.2.2. Mental Model Adjustments.  We compare par-
ticipants’ information weighting across Stages I and III 
to test the conjecture that explanations affect mental mod-
els  about  the  relationship  between  borrower  traits  and 
repayment  behavior.  We  rely  on  the  regression  model 
(1), setting s � 3 and excluding controls for the prediction 
and  LIME  values.  Figure  3 illustrates  regression  results 
that we report in Table 12 in the online appendix.

Figure  3 portrays  how  the  provision  of  predictions 
and explanations lastingly changed the weighting of a 
given borrower trait across Stages I and III, where parti-
cipants had no (X)AI aid. The diamond marker depicts 
the  original  weighting in  Stage  I  (β1).  The  dashed  and

Figure 3.  Mental Model Adjustments

Notes.  We  depict  participants’  mental  model  adjustments  as  mea-
sured  by  their  change  in  the  weighting  of  borrower  traits  across 
Stages  I  and  III.  The  estimated  prediction  and  explanation  effects 
respectively represent β3 and β4 in Model (1) with s � 3. Initial values 
represent β1. We denote significance levels by *p < 0.1, **p < 0.05, and 
***p < 0.01.

solid arrows, respectively, show how having observed 
predictions (β3) and explanations on top of predictions 
(β4)  did  fundamentally  alter  participants’  information 
processing, that is, mental models.

Observing opaque predictions did not result in a sig-
nificant  change  in  participants’  weighting  of  borrower 
traits. By contrast, depicted results suggest that providing 
explanations did entail an adjustment of mental models 
with the absolute magnitude of coefficients changing by 
61.8%  on  average.  Importantly,  this  adjustment  was 
asymmetric.  Observing  explanations  led  participants  to 
place  significantly  more  weight  on  borrowers’  Competi-
tiveness (+148.6%) and Patience (+59.4%) in Stage III than 
in Stage I. The weight changes again mirror the observed 
LIME explanations. After observing explanations that the 
AI system places the most weight on borrowers’ Competi-
tiveness and Patience, participants increased their weight-
ing  of  these  attributes  even  for  investment  decisions 
where  they  no  longer  observed  explanations.  Intrigu-
ingly, we do not find that explanations about the low rel-
evance  of  Agreeableness  led  participants  to  adjust  their 
marked weighting of this trait significantly. Although par-
ticipants  weighted  Agreeableness  significantly  less  while 
observing  explanations,  they  returned  to  their  original 
weighting  of  it  once  they  lost  access  to  the  XAI  system. 
Naturally,  one may  wonder  about  this asymmetry’s  ori-
gins. One plausible interpretation is that explanations are 
less  likely  to  evoke  pronounced  mental  model  adjust-
ments when they conflict with strong preconceptions. Put 
differently, people are more inclined to engage in mental 
model maintenance rather than building because it is less 
cognitively demanding and creates less psychological dis-
tress (Vandenbosch and Higgins 1996). In Stage I, partici-
pants  put  by  far  the  most  emphasis  on  a  borrower’s 
Agreeableness to decide on investing. LIME values, how-
ever, suggested that this conception is incorrect because it 
is  among  the  least  relevant  predictors  for  borrowers’ 
repayment  inclination.  Although  one would expect  that 
participants engaged in mental model building to reshape 
their beliefs about the relationship between Agreeableness 
and  repayment  behavior,  we  do  not  find  significant 
adjustments.  For  Competitiveness  (Patience),  explanations 
depicted  an  important  negative  (positive)  influence, 
which, given their initial weighting of it, confirmed par-
ticipants’  prior  beliefs.  Following  the  Mental  Models 
framework, confirming explanations should evoke the 
maintenance  or  reinforcement  of  prior  beliefs.  Given 
the significant explanation effects, it seems that partici-
pants willingly engaged in this process. This inclination 
to  engage  in  mental  model  maintenance  rather  than 
building  more  generally  concurs  with  the  frequently 
documented confirmation bias (Yin et al. 2016), that is, 
the  tendency  to  selectively  process  information  in  a 
way that allows for the continuation or strengthening 
of beliefs. We elaborate on this issue in Study 2 and the 
discussion.12

---

<!-- PAGE 11 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1591

Result 1.2. Machine explanations entailed asymmetric men-
tal  model  adjustments.  Participants  reinforced  priors  that 
explanations  confirmed  but  did  not  abandon  priors  that 
explanations markedly contradicted.

3.1.2.3. Investment Performance.  Thus far, it remains 
open how providing explanations on top of predictions 
affected  participants’  decision-making  performance  in 
our  setting.  Table  1 summarizes  participants’  perfor-
mance measured by the accuracy (share of payoff maxi-
mizing decisions) and recall (share of investments with 
repaying borrowers). We also report p values of F tests 
to illustrate significant treatment differences.13

Although there are no differences in Stage I, treatment 
participants  performed  significantly  worse  than  base-
line  ones  in  Stage  II  (�8.9%  and  �11.0%  for  accuracy 
and recall, respectively).14 Treatment participants’ rela-
tively  lower  performance  in  Stage  II  stems  from  not 
investing  with  the  most  competitive  borrowers  (with 
most negative LIME values), whereas the overall predic-
tion implies doing so, that is, from overruling positive 
predictions.15

They  overruled  positive  predictions  and  refrained 
from  investing  in  46.5%  of  these  cases,  resulting  in  a 
decision  accuracy  of  merely  53.5%.  Baseline  partici-
pants, for most competitive borrowers, overruled posi-
tive predictions only in 21.2% of the cases and achieved 
a  decision  accuracy  of  78.9%;  that  is,  they  are  47.5% 
more  likely  to  make  an  income  maximizing  decision 
than  treatment  participants.  For  all  other  borrowers, 
treatment (baseline) participants overruled positive pre-
dictions and made optimal decisions in 23% (19.4%) and 
69.6%  (71.1%)  of  the  cases,  respectively.  Hence,  treat-
ment participants seem to have placed too much weight 
on very high competitiveness, leading them to overrule 
the overall prediction inefficiently often.

Examining Stage III, we find that this overweighting of 
the  highest  competitiveness  level  persisted  even  when 
participants did not observe explanations anymore (see 
Table 13 in the online appendix). In Stage III, treatment 
(baseline)  participants  invested  with  most  competitive 
borrowers in 44.7% (54.7%, p < 0.01, F test) of the cases 
and with other borrowers in 68.2% (67.6%, p < 0.7, F test)

Table 1.  Investment Performance Across Stages

of the cases. As a result, treatment and baseline partici-
pants respectively achieved a decision accuracy of 51.7% 
and 57.2% (�9.6%, p < 0.01, F test) for most competitive 
borrowers and 59.5% and 62.8% (�5.3%, p < 0.05, F test) 
for other borrowers. Notably, participants already associ-
ated  very  high  competitiveness  with  a  low  repayment 
likelihood  in  Stage  I:  Most  competitive  borrowers  re-
ceived an investment in 56.3% of the cases, whereas all 
others  did  so  in  69.5%  of  the  cases  (there  do  not  exist 
treatment  differences).  Against  this  background,  expla-
nations  seem  to  have  exacerbated  this  inaccurate  pat-
tern16 to  an  extent  that  treatment  participants  made 
significantly worse decisions than before. Put differently, 
confirming explanations inappropriately reinforced pre-
conceptions  about  most  competitive  borrowers  not  re-
paying an investment in our setting.

Result  1.3. Participants excessively increased the isolated 
weighting  of  a  trait  they  already  believe  to  be  evidence 
against  repayment.  This  reaction  inefficiently  decreased 
participants’  likelihood  to  invest  with  repaying  borrowers 
that were highly competitive.

In sum, the results for Study 1 are highly consistent 
with the notion that the provision of explanations cre-
ates  a  novel  channel  through  which  AI  systems  may 
reshape users’ way of processing information, both situ-
ationally  and  more  permanently.  For  the  latter  effect, 
we observe an asymmetry that is reminiscent of a confir-
mation bias and, in our setting, decreased participants’ 
decision-making  performance  by  excessively  reinfor-
cing inaccurate preconceptions.

3.2. Study 2
The goal of Study 2 is twofold. First, we extend Study 1 
results  by  testing  the  generalizability  of  mental  model 
adjustment  findings  regarding  the  task  domain,  user 
expertise, and explanation presentation and examining 
whether the asymmetry we found for explanation-driven 
mental model adjustments in Study 1 is indeed a manifes-
tation of the confirmation bias. Second, we explore if men-
tal model adjustments spill over to related but disparate 
domains.

Stage I (no aid)

Stage II (with aid)

Stage III (no aid)

Accuracy

Recall

Accuracy

Recall

Accuracy

Recall

Baseline (AI) (%)
Treatment (XAI) (%)
F test: Baseline versus treatment

60.3
60.7
p � 0.79

64.9
67.4
p � 0.31

63.1
57.5
p < 0.01***

64.6
57.5
p < 0.01***

62.7
56.5
p < 0.02**

65.1
60.2
p < 0.04**

Notes.  We depict participants’ investment performance as measured by their accuracy (share of payoff maximizing decisions) and recall (share 
of investments with repaying borrowers) in Stages I, II, and III. We report results separately for baseline (AI) and treatment (XAI) participants. F 
tests reveal the significance of treatment differences per measure and stage.

*p < 0.1; **p < 0.05; and ***p < 0.01.

---

<!-- PAGE 12 -->

1592

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

3.2.1. Design.  Study 2 comprises four consecutive stages, 
where recruited real estate experts estimated the list-
ing price per square meter in Euros of apartments that 
we  previously  collected  from  a  large  online  plat-
form.17 Participants  saw  10  apartment  characteristics 
to make an informed guess and did not receive inter-
mediate feedback. To reduce the task complexity and 
avoid  informational  overload,  we  fixed  seven  apart-
ment characteristics across all stages, that is, apartments 
only  differed  regarding  the  same  three  characteristics: 
Location  (Frankfurt/Cologne),  Balcony  (Yes/No),  and 
Green voter share in the district (Below city average/City 
average/Above city  average).18 We  provide screenshots 
of the interfaces from each stage in the online appendix.

In Stage I, we elicited participants’ initial beliefs about 
the  relationship  between  the  three  variable  apartment 
characteristics and listing prices. Participants estimated 
the listing price of four random apartments with differ-
ent combinations of the variable attributes by entering 
their marginal contributions to the price using a slider. 
Sliders ranged from minus to plus 2.500e in steps of 50e. 
We initially set the marginal contributions and overall 
price  estimation  to  0e  and  the  average  listing  price 
(9,600e),  respectively.  Participants  additionally  stated 
their  confidence  in  the  entered  marginal  contributions 
and the resulting price estimation on a five-point scale.

Stage  II  introduced  our  treatment  variations.  In  all 
variations, participants estimated listing prices for eight 
random apartments with different combinations of vari-
able attributes they did not encounter in Stage I. In con-
trast to Stage I, participants directly entered the estimated 
listing price. As a reference point, they again observed the 
average listing price for an apartment. Participants stated 
their confidence on a five-point scale. In our baseline con-
dition (NoAid), participants estimated the price without 
any aid. Participants in the AI condition observed opaque 
listing price predictions of a steady, that is, nonlearning, 
AI  system  trained  on  4,975  collected  observations.19 In 
our XAI condition, in addition to observing these predic-
tions, participants also saw numerically presented SHAP 
values  for  the  three  variable  apartment  characteristics, 
that is, marginal contributions to the prediction in Euros. 
After they entered all eight listing price estimates, parti-
cipants in treatments with decision support filled out a 
survey  containing  items  on  their  trust,  degree  of  reli-
ance, and perceived transparency of the AI system (and 
explanations).

Stage III replicated Stage I to measure posterior beliefs. 
Independent  of  the  condition,  participants  again  made 
decisions without any aid for the same apartments.

Finally, in Stage IV, participants estimated the listing 
price  for  one  last  apartment  without  any  decision aid. 
Across  participants,  we  varied  the  balcony  and  green 
voter attribute of the apartment, whereas the seven fixed 
attributes  were  identical  to  the  previous  listings.  Most

importantly, the apartment was in a midsize city in east-
ern Germany (Chemnitz). For historical, demographic, 
and socioeconomic reasons, Chemnitz is very different 
from “A-cities” such as Frankfurt and Cologne, so the 
housing market is also very different. Germans in gen-
eral  and  real  estate  agents  in  particular  are  usually 
aware  of  this  East-West  disparity.20 The  study  con-
cluded  with  a  questionnaire  on  participants’  socio- 
demographics.

3.2.2. Results.  We  report  our  results  in  three  steps. 
First,  we  outline  the  experts’  belief  adjustments  from 
Stage I to Stage III. Second, we examine the occurrence 
of  confirmation  bias  in  these  adjustment  processes. 
Finally,  we  analyze  experts’  listing  price  estimates  in 
Stage IV.

3.2.2.1. Mental  Model  Adjustments.  Figure  4 shows 
the distribution of absolute differences between experts’ 
beliefs about the marginal contribution of the three vari-
able  attributes  before  and  after  the  treatment  interven-
tion.  We  show  results  for  the  NoAid,  AI,  and  XAI 
conditions. The distributions for the NoAid and AI con-
ditions are remarkably similar and skewed toward zero, 
indicating that experts frequently did not adjust beliefs. 
The distribution for XAI participants is considerably less 
right-skewed;  that  is,  they  adjusted  their  beliefs  across 
Stages I and III more. On average, NoAid, AI, and XAI 
participants’ absolute belief adjustments equaled 166.4e, 
165.4e,  and  299.1e,  respectively.  Only  the  differences 
between NoAid versus XAI (+79.7%, p < 0.01, F test), and 
AI versus XAI (+80.8%, p < 0.01, F test) conditions are sta-
tistically significant (see Table 24 in the online appendix), 
that is, observing explanations led to remarkably stron-
ger adjustments of beliefs. Our notion is that real estate 
experts  updated initially  held mental models  about the 
relationship  between  apartment  attributes  and  listing 
prices as they encountered SHAP explanations. Contrast-
ing  our  first  study,  we  directly  measure  participants’ 
prior and posterior beliefs about the contribution of dis-
tinct apartment characteristics to listing prices in Study 2. 
This  design  facet  enables  us  to  estimate  mental  model 
adjustments directly, leveraging the accepted framework 
by DeGroot (1974). Specifically, we assume that agent i’s 
posterior  belief  about  the relationship  of  characteristic j 
and the listing price Posti,j � ai,j · Priori,j + (1 � ai,j) · Expli,j 
is  a  weighted  combination  of  the  corresponding  prior 
belief  Priori,j  and  the  personally  observed  explanation 
Expli,j; 1 � ai,j  represents the extent of belief adaptation in 
the direction of the explanation, whereas ai,j describes the 
anchoring  of  the  previous  belief.  For  instance,  in  the 
extreme case of 1 � ai,j � 1, individual i completely aban-
dons  her  prior  mental  model  and  adopts  the  observed 
explanation  as  her  new  one.  We  estimate  the  weights 
(1 � ai) and  ai  for  our  three  study  conditions  using  a

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

---

<!-- PAGE 13 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1593

regression model comprising treatment interactions that 
has the following form:

Posijk � β1 · Priijk + β2 · (AIi × Priijk) + β3 · (Expli × Priijk)
+ β4 · SVij + β5 · (AIi × SVij) + β6 · (Expli × SVij)
+ γi + δk + ɛ:

(2)

The  variables  Posijk  and  Priijk,  respectively,  represent 
expert i’s posterior and prior beliefs about attribute j’s 
contribution  to  apartment  k’s  listing  price  in  Euros. 
Most  importantly,  AIi  is  a  dummy  variable  indicating 
that expert i observed a prediction, whereas the dummy 
Expli  equals  one  if  a  participant  additionally  observed 
explanations;  SVij  represents  the  average  SHAP  value 
for apartment attribute j of the apartments participant i 
encountered  in  Stage  II;  and  γi  and  δk  are  expert  and 
apartment controls, respectively.

On  an  individual  level,  Model  (2)  estimates  how 
observed SHAP values affected participants’ adjustments 
of beliefs about the relationship between a given charac-
teristic and the listing price. It enables us to quantify the 
“stickiness” of  prior  beliefs  (β1 � β3)  and  “gravitational 
pull” of explanations (β4 � β6) and directly test the occur-
rence of confirmation bias. Importantly, this estimation is 
only  possible  for  Study  2,  where  we  elicited  prior  and 
posterior beliefs about distinct feature-label relationships. 
In  Study  1,  we  measured  the  ultimate  investment  deci-
sions only and observed belief changes indirectly through 
changes in those decisions. As a result, we cannot individ-
ually  quantify  the  impact  of  observed  explanations  on 
specific  beliefs  nor  can  we  analyze  confirmation  bias:  a 
key contribution of our second study.

Table  2 depicts regression  results  for  Model  (2).  Re-
sults show that in our NoAid and AI conditions where 
participants did not observe explanations, SHAP values

Figure 4.  (Color online) Distribution of Absolute Belief 
Changes

Notes.  We  depict  the  distribution  of  experts’  absolute  belief  adjust-
ments  across  Stages  I  and  III.  We  aggregate  the  belief  adjustments 
over all apartment attributes. Different distributions show results sep-
arately for NoAid, AI, and XAI participants.

Table 2.  Posterior Belief Formation

Dependent variable: Posterior belief

(1)

(2)

Prior belief (β1)

Prior belief × AI (β2)

Prior belief × Expl. (β3)

Avg. SHAP (β4)

Avg. SHAP × AI (β5)

Avg. SHAP × Expl. (β6)

Fixed effects
N
R2

0.634***
(0.060)
0.070
(0.104)
�0.276***
(0.084)
0.025
(0.040)
0.078
(0.053)
0.265***
(0.053)
No
1,836
0.740

0.782***
(0.063)
�0.027
(0.084)
�0.240***
(0.075)
0.033
(0.039)
0.083
(0.050)
0.249***
(0.052)
Yes
1,836
0.787

Notes.  We  depict  results  from  OLS  regression  models  with  robust 
standard  errors  reported  in  parentheses.  The  dependent  variable 
equals  participants’ posterior  belief  about the  marginal contribution 
of  apartment  attributes  to  the  listing  price  in  euros.  The  main 
independent  variables  of  interest  are  participants’  prior  beliefs,  the 
average SHAP values for apartment attributes in Stage II, a dummy 
indicating  that  participants  observed  a  prediction  in  Stage  II  (AI),  a 
dummy indicating that participants observed explanations in Stage II 
(XAI),  and  interaction  terms.  We  further  control  for  the  overall 
posterior listing price participants entered for  the apartment and its 
interaction with treatment dummies, and the average prediction they 
observed  in  Stage  II.  In  column  (2),  we  additionally  include 
individual and apartment fixed effects.
*p < 0.1; **p < 0.05; and ***p < 0.01.

(unsurprisingly) have no significant explanatory power 
regarding posterior beliefs (see β4 and β5).21 When parti-
cipants  did  not  obtain  machine  aid  or  only  observed 
predictions, their prior and posterior beliefs were more 
than 60% positively correlated (β1 and β2); that is, parti-
cipants barely adjusted their beliefs. Only when partici-
pants observed explanations in addition to predictions 
did  the  displayed  SHAP  values  have  positive,  statisti-
cally significant effects. β6  reveals that XAI participants 
significantly  adjusted  their  beliefs  in  the  direction  of 
observed explanations. According to the estimate, pos-
terior  beliefs  resembled  SHAP  values  more  closely 
in  the  XAI  treatment  condition  compared  with  the 
NoAid and AI conditions (approximately +25 percent-
age points). Observing explanations also caused XAI 
participants’  posterior  beliefs  to  resemble  their  prior 
significantly less (β3), that is, prior beliefs became less 
“sticky” compared with the NoAid and AI conditions 
(approximately �25 percentage points). In sum, these 
results suggest that observing SHAP explanations led 
participants  to  adjust  their  beliefs  in  the  direction  of 
explanations  and  abandon  their  priors.  This  insight 
corroborates our Result 1.2 in Study 1 on an individual 
level, revealing that explanation-driven mental model 
adjustments  also  occur  for  experienced  experts,  who 
are arguably familiar with apartment traits and listing 
price predictions.22

---

<!-- PAGE 14 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1594

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

3.2.2.2. Confirmation  Bias.  In  Study  1,  we  observed 
asymmetric mental model adjustments that are reminis-
cent  of  the  confirmation  bias.  The  design  of  Study  2 
allows us to test for confirmation bias in mental model 
adjustment  processes  more  directly  by  examining 
whether XAI participants’ adjustments depended on 
the alignment of explanations and prior beliefs.

We  define  that  explanations  confirmed  an  expert’s 
preconception about the price contribution of a specific 
apartment attribute if the prior and the observed aver-
age  SHAP  value  for  the  corresponding  attribute  have 
the  same  sign.  With  this  definition,  observed  explana-
tions  confirm  prior  beliefs  in  49.6%  of  the  cases.23 We 
analyze differences in belief adjustments with respect to 
confirming and conflicting explanations using a modi-
fied version of Model (2). Specifically, we are interested 
in whether the convergence of XAI participants’ poste-
rior beliefs toward observed SHAP values only occurred 
when  explanations  confirmed  prior  beliefs.  Therefore, 
we focus on the subsample of XAI participants allowing 
us  to  omit  treatment  dummies  and  interaction  terms 
which facilitates the interpretation of results. Along the 
lines of Model (2), we regress XAI participants’ posterior 
beliefs about the relationship between apartment charac-
teristics  and  the  listing  price  on  their  prior  beliefs  and 
observed SHAP values. Most importantly, we now add 
a dummy variable (Confirm) indicating whether explana-
tions  confirmed  prior  beliefs  and  its  interaction  with 
average SHAP values and prior beliefs as independent 
variables. The interaction Avg. SHAP × Confirm will pro-
vide  insights  into  whether  the  influence  of  observed 
SHAP  values  on  belief  adjustments  depended  on  the 
alignment  of  explanations  and  prior  beliefs,  which  are 
insights we cannot obtain from Study 1 using Model (1).

Corroborating  our  interpretation  of  Result  1.2 from 
Study 1, we find that explanation-driven belief adjust-
ment processes depended on whether explanations con-
firmed or conflicted with prior beliefs. The estimate for 
the  interaction  term  Avg.  SHAP  × Confirm  is  positive 
and statistically significant (see column (1) in Table 3). 
Following the estimate, posterior beliefs resembled ob-
served  SHAP  values  significantly  more  closely  (about 
50% more) if they confirmed their prior beliefs. Hence, 
consistent with confirmation bias, the belief adjustment 
was  asymmetric  regarding  the  confirmatory  nature  of 
explanations.  If  participants  had  updated  beliefs  ratio-
nally according to Bayes rule, the interaction term should 
be insignificant as Bayesian observers would not weight 
explanations  conditional  on  their  alignment  with  prior 
beliefs (Rabin and Schrag 1999).

To  elaborate  on  the  notion  that  these  asymmetric 
belief  adjustments  are  a  manifestation  of  confirmation 
bias, we further consider the role of experts’ confidence 
in their prior beliefs. Prior research shows that confirma-
tion bias is strongest for entrenched beliefs (Pyszczynski 
and  Greenberg 1987,  Knobloch-Westerwick  and Meng

Table 3.  Confirmation Bias and Posterior Belief Formation

Dependent 
variable: 
Posterior belief

Prior belief

Avg. SHAP

Confirm

Avg. SHAP 
× Confirm

N
R2

(1)

Overall

0.492***
(0.091)
0.303***
(0.043)
12.039
(27.949)

0.166***
(0.059)
708
0.746

(2)
Low 
confidencebeliefs

(3)
High 
confidencebeliefs

0.483***
(0.105)
0.344***
(0.055)
�10.838
(39.552)
0.107
(0.077)
481
0.725

0.496***
(0.136)
0.145**
(0.067)
115.724
(73.702)

0.301***
(0.094)
222
0.843

Notes.  We depict results from OLS regression models with individual 
and apartment fixed effects. We report robust standard errors reported 
in  parentheses.  The  dependent  variable  equals  XAI  participants’ 
posterior belief about the marginal contribution of apartment attributes 
to the listing price in euros. The main independent variables of interest 
are participants’ prior beliefs, the average SHAP values for apartment 
attributes in Stage II, a dummy indicating that observed SHAP values 
in Stage II confirmed participants’ priors, measured by an equal sign of 
prior  beliefs  and  average  SHAP  values  for  a  given  attribute,  and 
interaction  terms.  We  further  control  for  the  overall  posterior  listing 
price participants entered for the apartment and the average prediction 
they observed in Stage II. Column (1) presents results for all decisions. 
Columns  (2)  and  (3)  respectively  depict  results  for  the  shares  of 
decisions  where  XAI  participants  report  low  and  high  confidence  in 
their prior.

*p < 0.1; **p < 0.05; and ***p < 0.01.

2009).  To  test  the  existence  of  such  heterogeneity,  we 
consider  experts’  reported  confidence  in  prior  beliefs 
and  define  that  an  expert  possessed  low  (high)  confi-
dence in a prior, if, on a five-point scale, they reported a 
confidence level of less than 4 (at least 4). In columns (2) 
and (3) of Table 3, we, respectively, repeat the regression 
analysis  reported  in  column  (1)  for  the  subsamples  of 
low- and high-confidence prior beliefs.

Reported  estimates  provide  further  evidence  that 
explanation-enabled  mental  model  adjustments  were 
subject to confirmation bias. According to the estimated 
coefficient of Avg. SHAP × Confirm, for low-confidence 
priors, the influence of observed SHAP values on poste-
rior  beliefs  did  not  depend  on  whether  explanations 
confirmed  prior  beliefs  (see  column  (2)).  Considering 
the positive and significant estimate of Avg. SHAP, the 
belief  updating  was in  line  with  Bayes rule.  By  con-
trast,  for  high-confidence  priors,  belief  adjustments 
were highly sensitive to whether SHAP values confirmed 
priors  (see  column  (3)).  The  estimate  for  Avg.  SHAP  ×
Confirm suggests that the magnitude of the adjustment of 
high-confidence priors was about two times larger when 
observed explanations were in line with them.

Result 2.1. Study 1 findings extend to expert users, SHAP 
explanations,  and  the  domain  of  apartment  price  predic-
tions:  SHAP  explanations  led  real  estate  experts  to  adjust 
prior beliefs about the relation between apartment attributes

---

<!-- PAGE 15 -->

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1595

and listing prices. Adjustment processes were subject to the 
confirmation bias.

3.2.2.3. Spillover  Effects.  Although  we  observe  that 
real  estate  experts  (asymmetrically)  adjusted  prior  be-
liefs, all previously reported results pertain to the same 
market:  Participants  observed  SHAP  explanations  for 
the same two A-cities in Western Germany, for which 
we  elicited  prior  and  posterior  beliefs.  What  remains 
open is whether explanation-driven belief adjustments 
spilled  over  to  the  listing  price  estimation  for  apart-
ments in different markets. We put this idea to the test 
by examining the distribution of participants’ final price 
predictions for an apartment in a medium-sized eastern 
German city that is not an “A city”: Chemnitz.24

Figure  5 shows  the  distribution  of  listing  price  esti-
mates conditional on the share of green voters in the dis-
trict  for  NoAid,  AI,  and  XAI  participants.  The  results 
indicate  that  observing  explanations  impacted  partici-
pants’ price estimates for Chemnitz apartments in neigh-
borhoods with high and low proportions of green voters. 
Figure 5(a) shows that the distribution of listing prices for 
an apartment in a district with a low green voter share is 
considerably more right-skewed for XAI than NoAid or 
AI participants; that is, they estimate relatively low prices 
more  frequently.  NoAid,  AI,  and  XAI  participants  on 
average  estimated  a  listing  price  of  4,752e,  5,141e,  and 
3,140e, respectively. Only the differences between NoAid 
versus XAI and AI versus XAI are statistically significant 
in regression analyses (p < 0.05, F test, for both). The dis-
tribution of price estimates in districts with high shares of 
green voters has a stronger left-skew for XAI participants 
than their NoAid and AI counterparts (Figure 5(b)). On 
average,  NoAid,  AI,  and  XAI  participants  estimated  a 
listing price of 5,231e, 4,600e, and 6,092e, respectively, for 
an apartment in a district with a high percentage of green 
voters. Again, we only find significant explanation effects 
(p  < 0.1,  F  test,  for  both).  These  results  reveal  the  eco-
nomic significance in the changes of price distributions.

Figure 5.  (Color online) Price Distributions in Chemnitz

Specifically,  compared  with  observing  no  predictions 
(opaque  predictions),  observing  explained  predictions 
decreased Chemnitz price estimates by 33.9% (38.9%) if 
the  share  of  green  voters  was  low  and  increased  price 
estimates  by  16.5% (32.4%) if  the  share  of  green  voters 
was high. As one might expect, the direction of the differ-
ence in experts’ evaluation of the green voter share attri-
bute  is  in  line  with  explanations  observed  in  Stage  II: 
SHAP values indicated that in Frankfurt and Cologne, a 
high (low) share of green voters marginally contributes 
to listing prices by about +652e (�613e). We do not find 
any effect for experts who only observed opaque predic-
tions in Stage II.

To  elaborate  on  these  findings,  we  also  perform  a 
median  split  and  analyze  the  subsamples  of  experts 
whose average absolute belief adjustment for the attri-
bute  “Green  voter”  is  below  and  above  the  median. 
Consistent  with  the  idea  that  belief  spillover  effects 
drive differences in listing price estimates in Chemnitz, 
experts who strongly adjusted their beliefs about the rel-
evance of “Green voters” from Stage I to III drive our 
aggregate-level results. We do not find significant treat-
ment differences in the accuracy of participants’ listing 
price  estimates  as  measured  by the  absolute  deviation 
from actual prices. Nevertheless, our results show that 
using XAI as a decision support tool in one market can 
affect aggregate listing prices in another market in an eco-
nomically  considerably  way  (average  absolute  change: 
approximately  20%),  which  is  not  the  case  for  opaque 
systems. This result demonstrates that XAI methods can 
link disparate decision-making tasks.

Result  2.2. Pronounced  explanation-driven  belief  adjust-
ments spill over to experts’ listing price estimation in a fun-
damentally different market.

In summary, our results from Study 2 (i) demonstrate 
the  robustness  of  our  results  from  Study  1  on  mental 
model  adjustments  in  terms  of  system  user  expertise, 
explanation  representation,  and  decision  domain;  (ii)

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Notes.  We depict the distribution of experts’ listing price estimates in Chemnitz. (a) and (b) Price distribution for apartments in a district with a 
low and high share of green voters, respectively. Different distributions show results separately for NoAid, AI, and XAI participants.

---

<!-- PAGE 16 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1596

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

provide strong evidence that explanation-driven mental 
model adjustments are subject to confirmation bias; and 
(iii) show that explanation-driven mental model adjust-
ments generate significant spillover effects.

4. Discussion and Conclusion
We report results from two empirical studies that pro-
vide novel insights into the interplay between the use of 
feature-based  XAI  methods  and  users’  cognitive  pro-
cesses.  Our  main  contribution  is  the  identification  of 
considerable  side  effects  of  providing  feature-based 
explanations,  the  most  popular  form  of  XAI  methods, 
on users’ situational information processing and mental 
models. We find that the latter effect (i) is subject to the 
confirmation  bias  so  that  misconceptions  can  persist 
and  even  accumulate,  possibly  leading  to  suboptimal 
decisions,  and  (ii)  can  create  spillover  effects  into  other 
decision domains. These overarching results suggest that 
the  growing,  partially  legally  required,  use  of  feature- 
based XAI methods opens a new channel through which 
AI systems may fundamentally reshape the way humans 
understand real-world relationships between features X 
and target variables Y. In the following, we discuss our 
results,  present implications for organizations and  soci-
ety, and, based on the limitations of our studies, provide 
directions for future research.

4.1. Discussion of Results
Study 1 demonstrates that the provision of explanations 
can situationally lead lay users to adjust their weighing 
of features accordingly, the average absolute change in 
estimates equals 73.9%, and to put less emphasis on the 
overall  prediction  (�26.8%).  Explanations  also  evoked 
asymmetric changes in lay users’ conceptions about the 
relationship  between  borrower  traits  and  repayment 
inclinations that influence behaviors even when they do 
not observe explanations anymore, the average absolute 
change  in  estimated  coefficients  equals  61.8%;  that  is, 
explanations affect mental models. Explanation-driven 
effects  decreased  lay  users’  decision-making  perfor-
mance  in  our  setting.  Compared  with  opaque  predic-
tions,  explanations  decreased  participants  investment 
performance by 8.9% while observing them and by 9.8% 
even when not observing explanations anymore. Study 
2  extended  these  results  in  three  ways.  First,  we  find 
that  even  expert users  in  a  considerably  more  applied 
domain adjusted mental models by about 25 percentage 
points. Second, results indicate that asymmetric mental 
model adjustments were a manifestation of the confirma-
tion  bias  because  posterior  beliefs  resembled  observed 
explanations about 50% more closely if explanations con-
firmed  prior  beliefs.  Third,  Study  2  reveals  that  mental 
model adjustments created spillover effects leading to an 
average absolute change in apartment price estimates for 
a different market by approximately 20%.

From a theoretical perspective, our results contribute 
to our understanding of the role of popular XAI meth-
ods in effective knowledge transfers from ML-based AI 
systems to human users. A key promise of modern AI 
systems  is  that  the  application  of  ML  techniques  will 
discover new knowledge from Big Data that has previ-
ously  eluded  even  experienced  experts  (Berente  et  al. 
2021, van den Broek et al. 2021). This “machine knowl-
edge” is typically codified in the form of a complex pre-
dictive model that outperforms humans. We show that 
providing  predictions  alone  is  insufficient  to  achieve 
systematic  knowledge  transfers  from  AI  systems  to 
human  users.  In  both  our  studies,  neither  laymen  nor 
experts  adapted  their  understanding  of  the  relation-
ships  between  features  X  and  label  Y  according  to 
“machine  knowledge”  when  observing  only  opaque 
predictions. Merely in treatments where users also had 
access  to  explanations,  they  began  to  adapt  their  app-
roach to solving the task so that it more closely matched 
the strategy of the AI system. Therefore, XAI methods 
appear to be a pivotal factor contributing to an effective 
channel  through  which  AI  systems  can  pass  on  their 
self-learned  knowledge  to  human  users.  Crucially, 
feature-based XAI methods seem to induce an asymme-
try  in  mental  model  adjustments:  users  adjust  their 
beliefs more in the direction of observed explanations if 
they  confirm  rather  than  disconfirm  their  priors.  This 
asymmetry contradicts with the updating behavior of a 
Bayesian observer who would neither over- nor under-
weight explanations conditional on them confirming or 
disconfirming  prior  beliefs.  This  asymmetry  occurred 
regardless  of  whether  we  provide  graphically  visual-
ized LIME or numerically represented SHAP explana-
tions.  It  therefore  seems  as  if  additive  feature-based 
explanations more generally evoke cognitive processes 
leading  users  to  learn  from  the  machine  selectively. 
Researchers across disciplines commonly refer to such an 
asymmetry as confirmation bias (Yin et al. 2016). Study 2 
provides  consistent  evidence  that  explanation-driven 
knowledge transfers from an AI to a human similarly suf-
fer from confirmation bias as knowledge transfers in the 
human-to-human  domain.  For  example,  confidence  in 
prior  conceptions  and  their  difference  from  the  new 
information  moderate  confirmation  bias  (Pyszczynski 
and  Greenberg  1987).  Similar  to  learning  from  other 
humans, users seem unwilling to internalize potentially 
helpful,  XAI-channeled  machine  knowledge  if  it  is  in-
consistent  with  what  they  already,  perhaps  incorrectly, 
believe  to  be  true.  From  the  perspective  of  the  Mental 
Models framework, individuals more frequently engage 
in maintaining rather than in building mental models of 
the relationships between features and labels. One reason 
for this effect could be the need to attain or maintain a 
high level of self-esteem (Klayman 1995), leading users 
to  focus  inappropriately  on  explanations  that  make 
them feel competent. In other words, they may derive

---

<!-- PAGE 17 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1597

a  positive  intrinsic  benefit  from  being  in  the  right 
(Gilad et al. 1987). From this perspective, people may 
misuse the XAI as a tool to enhance their self-esteem. If 
left unaddressed, the asymmetric adaptation of mental 
models by humans may prevent modern (X)AI appli-
cations from fulfilling their promise of making humans 
smarter, which (ironically) may also hinder the further 
development of AI applications by humans.

Interpreting  our  results in  the  light  of the  model by 
Agrawal et al. (2019) yields another theoretical insight 
regarding the ramifications of XAI. Our results indicate 
that  users’  willingness  to  follow  XAI  predictions  de-
pends on whether the explanations conform with their 
mental models. One way to rationalize this behavior is 
that their objective function includes a component that 
accounts  for  experiencing  some  positive  (negative)  in-
trinsic utility when obtaining a signal that their mental 
model may (not) be accurate (Festinger 1962, Gilad et al. 
1987,  Harmon-Jones  2019).  In  the  model  by  Agrawal 
et al. (2019), AI systems make predictions about uncer-
tain states of the world that relate to the profitability of 
taking specific actions. Human users, in turn, assess the 
expected payoffs associated with specific actions, that is, 
make judgments. Our results suggest that human judg-
ment in this model encompasses not only the material 
consequences of an action but also the psychological 
impact  of  receiving  a  signal  that  implicitly  shows 
whether current mental models are correct. If expla-
nations reveal that the AI system arrived at a prediction 
in a way that contradicts their held mental models, tak-
ing an action that follows this prediction effectively con-
stitutes a signal to oneself that the current mental model 
is incorrect, creating psychological distress, for example, 
in  the  form  of  a  cognitive  dissonance  (Harmon-Jones 
2019). This mental toll may lead users not to follow the 
prediction in the first place. Conversely, users may fol-
low unreliable predictions more often if the explanations 
are consistent with their current mental models because 
doing so provides a psychologically valuable self-signal 
that they are in the right (Gilad et al. 1987). Against this 
background,  users’  inclination  to  follow  predictions  of 
an  XAI  system,  and  thus  their  ultimate  decisions  and 
gains, is subject to greater variance than with a black-box 
AI.  That  is  because  users’  propensity  to  follow  predic-
tions  depends  on  the  consistency  of  the  explanations 
with their mental models.

Another  theoretical  contribution  of  our  work  is  to 
show the potential of feature-based XAI to link different 
decision domains by influencing users’ beliefs about the 
feature-label  relationship.  Study  2  results  show  that 
observing explanations for listing price predictions for 
apartments in Market A influenced the price estimation 
of experts in a different Market B, where the learned pat-
tern does not exist, and they did not have access to XAI 
decision support. We find that listing prices estimated by 
experts who observed explanations differed significantly

from those estimated by experts who either had no deci-
sion aid or only observed opaque predictions. This spill-
over effect seems to occur because of the adjustment of 
mental models  that experts  draw on  in both  situations. 
Therefore, as an unintended side effect, increasing public 
and  private  efforts  to  promote  the  use  of  XAI  methods 
may  extend  the  already  significant  influence  of  AI  sys-
tems from areas where we interact with them (Rahwan 
et al. 2019) to areas where such systems are not in use. 
Feature-based  XAI  methods’  potential  to  link  different 
domains is particularly concerning given recent evidence 
on  their  susceptibility  to  intentional  manipulation  and 
adversarial  attacks  (Lipton  2018).  Many  modern  XAI 
methods, including  LIME and SHAP, optimize fidelity, 
that is, ensure that explanations accurately mimic the pre-
dictions  of  the  black  box  model.  However,  even  small 
perturbations of the input data (e.g., deliberate manipula-
tion  and  measurement  errors)  can  lead  to  considerably 
different  explanations  for  identical  predictions,  that  is, 
depict  different  feature-label  relations  (Ghorbani  et  al. 
2019, Lakkaraju and Bastani 2020). The potential instabil-
ity of explanations allows manipulating user behaviors. 
Following our results, the creation of misleading explana-
tions  may  not  only  affect  users’  trust  in  the  AI  system 
(Lakkaraju and Bastani 2020) but also lead to an (asym-
metric)  adjustment  of  mental  models  that  affect  users’ 
decision making beyond the XAI augmented decision at 
hand.  Specifically,  the  depiction  of  certain  feature-label 
relationships that are not present can evoke inappropri-
ate mental model adjustments that, given the documen-
ted  asymmetry,  will  cause  users  who  already  believe 
these patterns to be true, to feel vindicated and reinforce 
these beliefs. In general, the documented spillover effects 
may magnify the reach and impact of intentional manip-
ulations  of  explanations,  increasing  deceiving  parties’ 
incentive to do so.

4.2. Implications
Reported results have important practical implications 
for  organizations  and  policymakers.  Our  finding  that 
XAI can change human thinking points to potential pit-
falls for companies that want, or have to, use XAI. Con-
sider a company that plans to implement XAI methods 
to  explain  to  its  employees  why  an  AI  system  makes 
certain  predictions.  As  Study  1  shows,  providing  exp-
lanations  in  addition  to  predictions  may  draw  users’ 
attention  excessively  to  the  explanations,  to  the  detri-
ment of the prediction itself. Users may place too much 
emphasis on individual explanations that confirm their 
prior beliefs, rather than adhering to the overall predic-
tion.  As  a  result,  employees’  decision-making  perfor-
mance for the task at hand may deteriorate, which is in 
line  with  evidence  from  related  research  (Poursabzi- 
Sangdeh et al. 2021). In domains where explanations are 
becoming a regulatory standard, managers need to take 
such potential downsides into account and contemplate

---

<!-- PAGE 18 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1598

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

the  ramifications  of  implementing  explainability  mea-
sures.  Following  our  results,  managers  who,  in  the 
future, are obliged to put XAI methods in place, should 
not take these steps too lightly. From a business perspec-
tive, our documented downsides of explainability could 
render the continued use of AI-based decision support 
systems  unattractive.  Considering  that  AI  systems  are 
often  deeply  interwoven  with  business  processes,  this 
XAI-driven discontinuance may entail considerable orga-
nizational  change.  As  a  result,  managers  may  be  well 
advised  to  assess  potential  inconsistencies  between  the 
AI system’s internal logic and employees’ understanding 
of  the  task  it  supports  before  rolling  out  explainability 
measures. This puts managers in a position to evaluate 
the magnitude of the potential downside of explainability 
and  use  countermeasures.  For  example,  managers  may 
obviate confirmation bias by openly discussing explana-
tions  that  conflict  with  employees’  mental  models  and 
showcasing arguments in support of the explanation.

Another pitfall for companies concerns the transfer of 
knowledge from AI systems to human users. As Study 2 
shows, even experts can overgeneralize learned feature- 
label relationships that are only applicable in the context 
in which they interact with the system. With the confir-
matory learning from explanations, existing differences 
in  employees’  initial  conceptions  may  lead  to  differ-
ences in how they collaborate with and what they learn 
from the XAI, for example, fostering the biased weight-
ing  of  certain  information.  From  this  perspective,  pro-
viding  explanations  might  decrease  individual  level 
noise in the decision-making process (Kahneman et al. 
2021) because individuals’ decisions become more con-
sistent. This is in line with F ¨ugener et al. (2021b), who 
find decisions to be increasingly consistent among users 
engaging with opaque predictions. On a more aggregate 
level, however, our results suggest that explained pre-
dictions  may  additionally  foster  differences  in  the 
decision-making  process  across  subgroups  of  users 
that possess heterogeneous priors. As a consequence, 
the variation of decisions on a group level can grow. 
As pointed out by Kahneman et al. (2021), variation in 
decisions  can  substantially  contribute  to  errors  and 
ultimately harm business performance. Consider our 
previous example of loan officers. XAI may cause loan 
approval decisions to increasingly depend on the par-
ticular  employee,  with  idiosyncratic  mental  models, 
assessing  the  applicant’s  creditworthiness.  This  in-
crease in loan approval variation may create consider-
able  business,  legal,  and  reputational  risks.  Against 
this background, managers should closely monitor the 
introduction  of  XAI  to  identify  a  possible  increase  in 
decision variance. For instance, managers could com-
plement XAI with “noise audits” and the development 
of “reasoned rules” (as proposed by Kahneman et al. 
2021)  to  overcome  the  hidden  costs  of  XAI-driven 
increases in inconsistent decision making.

From a societal perspective, our results indicate that 
broad, indiscriminate implementation of XAI methods 
may create unintended downstream ramifications. Our 
finding that XAI can lead users to adjust mental models 
in a confirmatory way and carry over learned patterns 
to  other  domains  may,  in  an  extreme  case,  foster  dis-
crimination and social divisions. Assume all recruiters 
start to collaborate with an XAI system to support hiring 
decisions. For example, a subgroup of recruiters may dis-
criminate  against  women  because  they  believe  female 
applicants  to  be  less  productive  on  the  job.  If  the  XAI 
(occasionally)  provides  local  explanations  that  depict 
being female as negative evidence for high future per-
formance, the subgroup that statistically discriminates 
based on gender will readily reinforce its prior belief, 
that  is,  engage  in  mental  model  maintenance.  As  a 
result,  these  recruiters  may  become  more  biased  and 
less  noisy  in  their  behavior  as  they  hire  female  appli-
cants  consistently  less.  Given  the  spillover  effects  we 
find, they may even carry over their strengthened con-
ceptions about women’s productivity to other jobs, fur-
ther  reinforcing  discriminatory  patterns.  Additionally, 
because  nondiscriminating  recruiters  will  most  likely 
refrain  from  adjusting  their  mental  model,  that  is,  not 
engage in mental model building, social divisions among 
recruiters may develop and accumulate along the lines of 
gender biases. Hence, without any malicious intent, the 
broad use of XAI may ironically foster human discrimi-
natory  tendencies  and  divide  social  groups.  Notably, 
with the possibility to manipulate explanations, deceiv-
ing third parties could also intentionally cause explana-
tions  to  exhibit  specific  prediction  contributions  for 
sensitive  attributes  such  as  race,  gender,  or  age.  This 
effect could lead human users who already hold preju-
dices, stereotypes, or discriminatory tendencies to rein-
force their views, which could promote certain political 
agendas.

4.3. Limitations and Future Research
As  with  any other  research  study,  ours  is  not without 
limitations.  In  light  of  increasing  regulatory  require-
ments and private initiatives, we believe that these lim-
itations  open  up  fruitful  avenues  for  future  research. 
One  limitation  of  our  work  concerns  the  lack  of  feed-
back  on  the  decision  outcomes  and  thus  the  perfor-
mance of the AI system. In both our studies, we did not 
provide feedback for two reasons. First, it adds a consid-
erable  layer  of  complexity  that  impedes  the  measure-
ment and interpretation of isolated explanation-driven 
effects on users’ cognitive processes. Second, in practice, 
many  AI-supported  decisions  do  not  yield  immediate 
feedback, or only yield feedback for some of the predic-
tions.  Hence,  users  have  to  interact  with  the  system 
without  learning  its  prediction  accuracy,  at  least  for  a 
certain period. Examples include hiring decisions sup-
ported  by  an  on-the-job  performance  predicting  AI

---

<!-- PAGE 19 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1599

system,  investment  decisions  supported  by  a  return 
predicting  AI  system,  and  drug  treatment  decisions 
supported by an effectiveness predicting AI system. Con-
sequently, explanations may alter users’ situational infor-
mation  processing  and  mental  models  before  feedback 
on system performance arrives. Nonetheless, we strongly 
encourage  future  research  to  examine  the  role  of  feed-
back  as  it  may  introduce  unexpected  dynamics  in  the 
cognitive  effects  we  document.  For  instance,  the  (selec-
tive) reinforcement of their mental models through exp-
lanations,  may  lead  users  to  be  more  forgiving  and 
maintain trust in the AI system, even if they eventually 
see  it  making  mistakes.  In  this  way,  the  interaction 
between  feedback  and  explanations  might  constitute  a 
factor  contributing  to  unwarranted  algorithm  apprecia-
tion (Logg et al. 2019), leading users to rely on incorrect 
outcomes blindly. Additionally, people’s adjustments of 
the situational information processing and existing men-
tal  models  possibly  depend  on  the  extent  to  which  the 
XAI system’s predictions outperform their own. If users 
learn that an XAI system’s predictions perform consider-
ably better than their subjective ones, the magnitude of 
reported  confirmation  biases  may  vary.  Conversely, 
when users’ predictions are better than the XAI, their 
confirmation  bias  might  be  even  stronger.  Future  re-
search  could  examine  to  what  extent  our  reported 
effects, at the intensive margin, depend on users’ per-
ceptions  about  differences  in  their  own  and  the  XAI 
system’s predictive performance.

Another limitation of our work originates from letting 
participants interact with local, feature-based XAI meth-
ods.  We  opted  to  use  these  explanations  because  they 
are already widely in use in practice and because there 
are  arguments  that  feature-based  explanations  on  an 
individual level are necessary to comply with (upcom-
ing) regulatory requirements (Goodman and Flaxman 
2017). Yet, there exist other forms of explanations, for 
example,  global  feature-based  explanations  or  even 
example-based  explanations.  Although  an  investiga-
tion and comparison of the interplay between different 
forms  of  explanations  and  cognitive  processes  are 
beyond  the  scope  of  this  paper,  it  is  worthwhile  for 
future research to explore whether, and if so why, the 
effects we document would change if users (addition-
ally) obtain other forms of explanations. Consider, for 
instance, global explanations. Although local explana-
tions  help  understand  why  an  AI  system  produces  a 
prediction on a case-by-case basis, global explanations 
reveal important high-level patterns and nonlinearities 
in  the  system’s  logic.  Such  global  explanations  effec-
tively  aggregate  individual-level  information  for  the 
user  and  help to  understand  the system’s  overall  logic. 
By taking over this information aggregation task, global 
explainability could mitigate concerns about the selec-
tive processing of isolated local explanations that argu-
ably contribute to the occurrence of confirmation bias.

Additionally,  the  global  representation  may  facilitate 
comparison  and  reflection  processes  that  ultimately 
improves  the  transfer  of  knowledge  from  the  AI  sys-
tem to the user.

4.4. Conclusion
A concluding remark is worth making. Of course, our 
work is not meant to be an argument, let alone a plea, 
against making “black box” AI systems more explain-
able or transparent. Instead, we comprehend our find-
ings as a warning that the indiscriminate use of modern 
XAI methods as an isolated measure may lead to unin-
tended,  unforeseen  problems  because  it  creates  a  new 
channel  through  which  AI  systems  can  affect  human 
behaviors across domains. The pervasive human incli-
nation  to  process  information  in  a  way  that  confirms 
their preconceptions while ignoring potentially helpful 
yet  conflicting  information  needs  addressing  if  exp-
lainability  is  to  become  an  effective  means to  combat 
accountability, transparency, and fairness issues with-
out creating adverse second-order effects. For instance, 
one might restrict the provision of explanations of sen-
sitive features for end users of the system and only use 
them to ensure the proper and unbiased functioning of 
the AI system during the development process. Addi-
tionally, it  might  be important  to  provide developers 
and data scientists with cognitive awareness trainings 
to make them more sensitive to their own biased men-
tal processes.

Endnotes
1 For  anecdotal  evidence  of  such  nontraditional  data  use,  see  Lend 
doEFL.com  or  https://money.cnn.com/2016/08/24/technology/ 
lenddo-smartphone-battery-loan/index.html.
2 On  a  high  level,  both  decisions  effectively  constitute  sequential 
economic  transactions  under  uncertainty  that  strongly  depend  on 
trust.
3 Explainability may enter the model of Agrawal et al. by changing 
the prediction reliability. Following Proposition 2, the necessity for 
providing  explanations  decreases  with  the  users’  judgment.  How-
ever, the model does not consider the idea presented in our paper 
that explainability may also affect users’ understanding of the pro-
cess that determines the uncertain state of the world the AI tries to 
predict.  One  could  integrate  this  notion  into  the  framework  by 
modeling  that  explanations  affect  users’  judgment  capabilities  by 
influencing  beliefs  about  underlying  processes.  Extending  the 
model of Agrawal et al. in this direction may be a fruitful endeavor 
to better understand whether explainability modulates the relation-
ship  between  prediction  and  judgment.  However,  an  extension  of 
the  formal  model  is  beyond  the  scope  of  this  paper  and  left  for 
future research.
4 See  the  online  appendix  for  details  on  the  experimental  proce-
dures including payments, instructions, and screenshots.
5 When  a  risk-neutral,  purely  self-interested  investor  expects  that  the 
borrower repays her with a probability of p > 0.5, for example, because 
she  believes  the  borrower  to  possess  altruistic,  efficiency,  or  fairness 
preferences,  they  have  a  strict  incentive  to  invest  because  they  maxi-
mize  their expected  earnings. Importantly,  holding  such  expectations 
about the borrower’s preferences is  justified and  frequently observed

---

<!-- PAGE 20 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

1600

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

in  sequential  games:  A  considerable  share  of  people  does  respond 
reciprocally in sequential exchanges if they are trusted (see Miettinen 
et al. 2020 for an overview).
6 To reduce the complexity for the reader, we only report the three 
main  stages  of  the  experiment.  Right  before  and  after  Stage  II,  we 
additionally measured participants’ prior and posterior preferences 
to observe three borrower characteristics. We use these measures as 
robustness and consistency checks. We provide a detailed descrip-
tion of these measurements in the online appendix.
7 The  questionnaire  items  included  in  the  field  study  were  selected 
partly  for  exploratory  reasons  and  partly  motivated  by  previous 
research  documenting  their  association  with  individuals’  repayment 
behavior in investment games (Ben-Ner and Halldorsson 2010).
8 For most traits, values and LIME values are almost perfectly corre-
lated producing severe problems of multicollinearity (see Table 7 in 
the online appendix). Therefore, in our regression analyses, we only 
include LIME explanations for which there exists a tolerable correla-
tion  between  the trait and LIME values:  Openness, Agreeableness, 
and Conscientiousness.
9 See Table 8 in the online appendix.
10 These  results  do  not  allow  us  to  isolate  how  explanations  affect 
what  investors  consider  to  be  a  borrower’s  motivation  to  repay 
them or not. The change in the weighting of competitiveness could 
stem  from  a  reinforced  perception  that  competitiveness  predicts  a 
low repayment likelihood because it proxies for antisocial, income- 
maximizing, or relative income-maximizing motives. Although we 
cannot  isolate  investors’  latent  belief(s)  about  borrowers’  motives, 
our results effectively show that the provision of explanations does 
entail a change in at least one of these perceived latent motives, that 
is,  that  XAI  can  change  the  processing  of  information.  A  similar 
argument  applies  regarding  mental  model  adjustments  outlined 
later.
11 Reported results are robust to excluding participants who always 
or never invested in our analyses, respectively, alleviating concerns 
that our results are driven by pure altruists or players who always 
choose the game-theoretically dominant strategy (see the subsection 
on  additional  robustness  checks  in  the  online  appendix).  Instead, 
our  results  stem  from  those  participants  whose  behavior  suggests 
that they try to invest with borrowers whom they believe will make 
a  repayment,  that  is,  individuals  who,  from  a  conceptual  point  of 
view,  should  be  most  inclined  to  learn  to  recognize  repaying  bor-
rowers.  Results  1.2 and  1.3 are  equally  robust  to  excluding  these 
“extreme” types, warranting a similar interpretation.
12 The  significant  explanation  effect  for  Openness  and  Extraversion 
may be a consequence of participants’ significantly stronger weight-
ing of borrowers’ Competitiveness and Patience and a limited capacity 
to  process  information.  Specifically,  XAI  participants  in  Stage  III 
place similarly low weight on all borrower traits but Competitiveness, 
Agreeableness,  and  Patience.  This  pattern  may  suggest  that  partici-
pants heuristically focus on the three characteristics that they them-
selves and the AI system deemed most relevant to the decision. As 
a result, they place less weight on all other traits, which for Open-
ness led to a statistically significant effect.
13 We show ROC curves in Figures 17 to 19 in the online appendix.
14 Participants  neither  knew  their  own  nor the  AI  system’s  perfor-
mance  because  we  did  not  provide  intermediate  feedback.  There-
fore,  they  could  not  see  how  much  better  or  worse  the  system 
performs compared with themselves. Although unknown to partici-
pants, predictions are accurate in about 69.3% of the cases. This per-
formance holds equally for both repaying (69.7%) and nonrepaying 
borrowers (67.7%). Participants in Stage I correctly invested with (non- 
)repaying borrowers in 66.1% (41.2%) of the cases and overall in 60.5% 
of  the  cases.  Put  differently,  the  AI  system  outperforms  them overall 
(+14.5%)  and  especially  for  the  identification  of  nonrepaying  ones

(+64.3%). As  a  result,  participants  could  have  benefited  from  relying 
on the predictions, which baseline participants did at least partially.
15 Across Stages I and II, baseline participants’ access to the AI system 
significantly increased the accuracy by 4.6% (p < 0.01, F test), whereas 
the  recall effectively remained  constant (p < 0.82,  F test).  XAI partici-
pants performance significantly decreased regarding both the accuracy 
(�5.3%; p < 0.01, F test) and recall score (�14.6%; p < 0.01, F test).
16 A  purely  linear  distinction  between  most  competitive  and  other 
borrowers  does  not  allow  to  draw  conclusions  about  their  repay-
ment likelihood: they, respectively, made a repayment in 77.4% and 
79.8% of the cases (p � 0.85, F test).
17 We scraped data from a large online platform in February 2022. 
We  collected  observations  for  all  apartments  listed  for  sale  in  the 
seven  major  cities  of  Germany  (“A-Cities”)  and  a  medium-sized 
eastern German city (Chemnitz). We constructed a data set consist-
ing  of  eight  apartment  attributes  and  the  listing  price  directly 
obtained from the platform and two additionally collected features 
from public statistics. We provide summary statistics in the online 
appendix (Table 6).
18 We selected these three characteristics for technical reasons regard-
ing the ML model and based on the input from our industry partner. 
The notion is that these characteristics together are (i) sufficiently rele-
vant to the prediction and (ii) familiar/accessible to experts.
19 The AI system is a random forest that achieves a performance of 
R2 � 0:72 on unseen test data. See the online appendix for additional 
information.
20 For instance, A-cities exhibit considerably higher average wages, 
more liberal political attitudes, and faster population growth (Cajias 
et al. 2020).
21 The  positive  coefficient  for  β5  may  be  related  to  the  fact  that 
SHAP values and overall predictions are inextricably linked. Merely 
observing  high  (low)  predictions  may  lead  to  adjustments  of 
reported beliefs upward (downward), creating a positive, however, 
insignificant correlation with underlying SHAP values in the data.
22 Participants, on average, have worked in the real estate industry 
for 13.8 years and, on a scale from 1 to 10, report that their experi-
ence level in rating apartment listing prices is 5.7.
23 Our  main  insights  are  robust  to  defining  more  restrictively  that 
explanations  confirm  priors  if  the  absolute  distance  between  the 
prior  and  the  observed  average  SHAP  value  is  smaller  than  the 
absolute  distance  between  the  prior  and  0e  and,  at  the  same  time, 
smaller than the absolute distance between the prior and the closest 
extreme, that is, 62,500e (see Table 25 in the online appendix).
24 We  did  not  include  Chemnitz  observations  in  the  data  to  train 
the  AI  model.  We  conducted  several  analyses  showing  that  the 
most  important  predictors  for  listing  prices  in  Frankfurt  and 
Cologne  (cities  in  Stages  I  to  III)  differ  considerably  from  listing 
price predictors in Chemnitz. Real estate experts are arguably aware 
of the structural differences in apartment markets.

References
Abdel-Karim  BM,  Pfeuffer  N,  Carl  V,  Hinz  O  (2022) How  AI-based 
systems can induce reflections: The case of AI-augmented diag-
nostic work. Management Inform. Systems Quart. Forthcoming.
Abdel-Karim  BM,  Pfeuffer  N,  Rohde  G,  Hinz  O  (2020)  How  and 
what can humans learn from being in the loop? German J. Artifi-
cial Intelligence 34(2):199–207.

Agarwal R, Dhar V (2014) Big data, data science, and analytics: The 
opportunity  and  challenge  for  IS  research.  Inform.  Systems  Res. 
25(3):443–448.

Agrawal A, Gans JS, Goldfarb A (2019) Exploring the impact of arti-
ficial  intelligence:  Prediction  vs.  judgment.  Inform.  Econom.  Pol-
icy 47:1–6.

---

<!-- PAGE 21 -->

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

1601

Alavi  M,  Marakas  GM,  Yoo  Y  (2002)  A  comparative  study  of  dis-
tributed  learning  environments  on  learning  outcomes.  Inform. 
Systems Res. 13(4):404–415.

Ban GY, El Karoui N, Lim AE (2018) Machine learning and portfolio

optimization. Management Sci. 64(3):1136–1154.

Bauer K, Hinz O, van der Aalst W, Weinhardt C (2021) Expl(AI)n it 
to  me:  Explainable  AI  and  information  systems  research.  Bus. 
Inform. Systems Engrg. 63(2):79–82.

Ben-Ner  A,  Halldorsson  F  (2010)  Trusting  and  trustworthiness: 
What are they, how to measure them, and what affects them. J. 
Econom. Psych. 31(1):64–79.

Berente  N,  Gu  B,  Recker  J,  Santhanam  R  (2021)  Managing  artificial 
intelligence. Management Inform. Systems Quart. 45(3):1433–1450.
Berg  J,  Dickhaut  J,  McCabe  K  (1995)  Trust,  reciprocity,  and  social

history. Games Econom. Behav. 10(1):122–142.

Bhatt U, Xiang A, Sharma S, Weller A, Taly A, Jia Y, Ghosh J, et al. 
(2020)  Explainable  machine  learning  in  deployment.  Proc.  Conf. 
on  Fairness,  Accountability,  and  Transparency  (Association  for 
Computing Machinery, New York).

EU (2021) Proposal for  a regulation EU of  the European Parliament 
and  of  the  Council  of  April  21,  2021,  laying  down  harmonised 
rules  on  artificial  intelligence  (Artificial  Intelligence  Act)  and 
amending  certain  Union  legislative  acts.  Official  J.  Eur.  Union 
Law 119. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri= 
celex%3A52021PC0206.

Festinger L (1962) Cognitive dissonance. Sci. Amer. 207(4):93–106.
F ¨ugener A, Grahl J, Gupta A, Ketter W (2021a) Cognitive challenges 
in human–artificial intelligence collaboration: Investigating the path 
toward productive delegation. Inform. Systems Res. 33(2): 678–696.
F ¨ugener  A,  Grahl  J,  Gupta  A,  Ketter  W  (2021b)  Will  humans-in-the- 
loop become borgs? Merits and pitfalls of working with AI. Man-
agement Inform. Systems Quart. 45(3b):1527–1556.

Garreau D, Luxburg U (2020) Explaining the explainer: A first theo-
retical  analysis  of  LIME.  Proc.  Internat.  Conf.  on  Artificial  Intelli-
gence and Statist.

Ge  R,  Zheng  Z,  Tian  X,  Liao  L  (2021)  Human–robot  interaction: 
When investors adjust the usage of robo-advisors in peer-to-peer 
lending. Inform. Systems Res. 32(3):774–785.

Brewer  WF  (1987)  Schemas  vs.  mental  models  in  human  memory. 
Morris  P,  ed.  Modelling  Cognition  (John  Wiley  &  Sons,  Oxford, 
UK), 187–197.

Ghorbani A, Abid A, Zou J (2019) Interpretation of neural networks 
is  fragile.  Proc.  AAAI  Conf.  on  Artificial  Intelligence.  33(1): 
3681–3688.

Bussone  A,  Stumpf  S,  O’Sullivan  D  (2015)  The  role  of  explanations 
on  trust  and  reliance  in  clinical  decision  support  systems.  Proc. 
Internat.  Conf.  on  Healthcare  Informatics  (Institute  of  Electrical 
and Electronics Engineers (IEEE), New York).

Cabral  TS  (2021)  AI  and  the  right  to  explanation:  Three  legal  bases 
under the GDPR. Data Protection Artificial Intelligence 13:29–56.
Cajias  M,  Freudenreich  P,  Freudenreich  A,  Sch¨afers  W  (2020) 
Liquidity and prices: A cluster analysis  of the  German residen-
tial real estate market. J. Bus. Econom. 90(7):1021–1056.

Case  N  (2018)  How  to  become  a  centaur.  J.  Design  Sci. https://jods. 
mitpress.mit.edu/pub/issue3-case/release/6?version=53b19e72- 
d43a-4eda-8c48-6ed3cdc03218.

Castelo N, Bos MW, Lehmann DR (2019) Task-dependent algorithm

aversion. J. Marketing Res. 56(5):809–825.

Chatterjee  S,  Sarker  S,  Valacich  JS  (2015)  The  behavioral  roots  of 
information  systems  security:  Exploring  key  factors  related  to 
unethical IT use. J. Management Inform. Systems 31(4):49–87.
DeGroot  MH  (1974)  Reaching  a  consensus.  J.  Amer.  Statist.  Assoc.

69(345):118–121.

Gilad B, Kaish S, Loeb PD (1987) Cognitive dissonance and utility maxi-
mization: A general framework. J. Econom. Behav. Organ. 8(1):61–73.
Goldstein IM, Lawrence J, Miner AS (2017) Human-machine collab-
oration  in  cancer  and  beyond:  The  centaur  care  model.  JAMA 
Oncology 3(10):1303–1304.

Goodman B, Flaxman S (2017) European Union regulations on algo-
rithmic decision-making and a “right to explanation”. AI Maga-
zine 38(3):50–57.

Google AI (2019) Responsible AI practices: Interpretability. Accessed 
March 8, 2022, https://ai.google/responsibilities/responsible-ai- 
practices/?category=interpretability.

Gramegna  A,  Giudici  P  (2021)  SHAP  and  LIME:  An  evaluation  of 
discriminative power in credit risk. Frontiers Artificial Intelligence 
4:752558.

Gregor  S  (2006)  The  nature  of  theory  in  information  systems.  Man-

agement Inform. Systems Quart. 30(3):611–642.

Gregor  S,  Benbasat  I  (1999)  Explanations  from  intelligent  systems: 
Theoretical  foundations  and  implications  for  practice.  Manage-
ment Inform. Systems Quart. 23(4):497–530.

Dellermann D, Ebel P, S¨ollner M, Leimeister JM (2019) Hybrid intel-

Gunning  D,  Stefik  M,  Choi  J,  Miller  T,  Stumpf  S,  Yang  GZ  (2019)

ligence. Bus. Inform. Systems Engrg. 61(5):637–643.

Dhaliwal  JS,  Benbasat  I  (1996)  The  use  and  effects  of  knowledge- 
based system explanations: Theoretical foundations and a frame-
work for empirical evaluation. Inform. Systems Res. 7(3):342–362.

Dietvorst BJ, Simmons JP, Massey C (2015) Algorithm aversion: Peo-
ple erroneously avoid algorithms after seeing them err. J. Exper-
iment. Psych. General 144(1):114–126.

Dietvorst  BJ,  Simmons  JP,  Massey  C  (2018)  Overcoming  algorithm 
aversion: People will use imperfect algorithms if they can (even 
slightly) modify them. Management Sci. 64(3):1155–1170.

Dijkstra  JJ  (1999)  User  agreement  with  incorrect  expert  system

advice. Behav. Informs. Tech. 18(6):399–411.

Dodge J, Liao QV, Zhang Y, Bellamy RK, Dugan C (2019) Explaining 
models: An empirical study of how explanations impact fairness 
judgment. Proc. Internat. Conf. on Intelligent User Interfaces.

Doshi-Velez F, Kim B (2017) Toward a rigorous science of interpret-
able  machine  learning.  Preprint,  submitted  March  2,  https:// 
arxiv.org/abs/1702.08608.

Erlei A, Nekdem F, Meub L, Anand A, Gadiraju U (2020) Impact of 
algorithmic  decision  making  on  human  behavior:  Evidence 
from  ultimatum  bargaining.  Proc.  AAAI  Conf.  on  Human  Com-
put. and Crowdsourcing.

EU (2016) Regulation EU 2016/679 of the European Parliament and 
of  the  Council  of  27  April  2016,  article  22.  Official  J.  Eur.  Union 
Law 119:59.

XAI—explainable artificial intelligence. Sci. Robot 4(37):eaay7120.

Harmon-Jones  EE  (2019)  Cognitive  Dissonance:  Reexamining  a  Pivotal 
Theory in Psychology (American Psychological Association).
Hemmer  P,  Schemmer  M,  V¨ossing  M,  K ¨uhl  N  (2021)  Human-AI 
complementarity  in  hybrid  intelligence  systems:  A  structured 
literature review. Proc. 28th Pacific Asia Conf. on Inform. Systems.

Hoffman  M,  Kahn  LB,  Li  D  (2018)  Discretion  in  hiring.  Quart.  J.

Econom. 133(2):765–800.

Holt  CA,  Smith  AM  (2009)  An  update  on  Bayesian  updating.  J.

Econom. Behav. Organ. 69(2):125–134.

Ji-Ye  Mao  IB  (2000)  The  use  of  explanations  in  knowledge-based 
systems:  Cognitive  perspectives  and  a  process-tracing  analysis. 
J. Management Inform. Systems 17(2):153–179.

Johnson-Laird PN, Goodwin GP, Khemlani SS (2017) Mental models 
and  reasoning.  The  Routledge  International  Handbook  of  Thinking 
and Reasoning (Routledge, Abingdon-on-Thames, UK), 346–365.
Jones NA, Ross  H, Lynam  T, Perez  P, Leitch A  (2011) Mental  mod-
els:  An  interdisciplinary  synthesis  of  theory  and  methods.  Eco-
logical Soc. 16(1). https://www.jstor.org/stable/26268859#metadata_ 
info_tab_contents.

Jussupow E, Benbasat I, Heinzl A (2020) Why are we averse toward 
algorithms?  A  comprehensive  literature  review  on  algorithm 
aversion. Proc. Eur. Conf. on Inform. Systems.

Jussupow  E,  Spohrer  K,  Heinzl  A,  Gawlitza  J  (2021)  Augmenting 
medical  diagnosis  decisions?  An  investigation  into  physicians’

---

<!-- PAGE 22 -->

1602

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing 
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)

decision-making  process  with  artificial  intelligence.  Inform.  Sys-
tems Res. 32(3):713–735.

Kahneman D, Sibony O, Sunstein CR (2021) Noise: A Flaw in Human

Judgment (Little, Brown).

Kaur  H,  Nori  H,  Jenkins  S,  Caruana  R,  Wallach  H,  Wortman 
Vaughan  J  (2020)  Interpreting  interpretability:  Understanding 
data  scientists’  use  of  interpretability  tools  for  machine  learn-
ing. Proc. CHI Conf. on Human Factors in Comput. Systems.

Klayman  J  (1995)  Varieties  of  confirmation  bias.  Psych.  Learning

Motives 32:385–418.

Kleinmuntz  B  (1990)  Why  we  still  use  our  heads  instead  of  formu-
las: Toward an integrative approach. Psych. Bull. 107(3):296.
Knobloch-Westerwick  S,  Meng  J  (2009)  Looking  the  other  way: 
Selective  exposure  to  attitude-consistent  and  counterattitudinal 
political information. Comm. Res. 36(3):426–448.

Koh  PW,  Liang  P  (2017)  Understanding  black-box  predictions  via

influence functions. Proc. Internat. Conf. on Machine Learn.

Lakkaraju H, Bastani O (2020) “How do I fool you?” Manipulating 
user  trust  via  misleading  black  box  explanations.  Proc.  AAAI/ 
ACM Conf. on AI, Ethics, and Society.

Lakkaraju H, Kamar E, Caruana R, Leskovec J (2019) Faithful and cus-
tomizable  explanations  of  black  box  models.  Proc.  AAAI/ACM 
Conf. on AI, Ethics, and Society.

Lim  KH,  Ward  LM,  Benbasat  I  (1997)  An  empirical  study  of  com-
puter  system  learning:  Comparison  of  co-discovery  and  self- 
discovery methods. Inform. Systems Res. 8(3):254–272.

Lipton  ZC  (2018)  The  mythos  of  model  interpretability:  In  machine 
learning,  the  concept  of  interpretability  is  both  important  and 
slippery. Queue 16(3):31–57.

Logg  JM,  Minson  JA,  Moore  DA  (2019)  Algorithm  appreciation: 
People  prefer  algorithmic  to  human  judgment.  Organ.  Behav. 
Human Decision Processes 151:90–103.

Lu  Z,  Yin  M  (2021)  Human  reliance  on  machine  learning  models 
when  performance  feedback  is  limited:  Heuristics  and  risks. 
Proc. CHI Conf. on Human Factors in Comput. Systems.

Lundberg SM, Lee SI (2017) A unified approach to interpreting model

predictions. Proc. Conf. on Neural Inform. Processing Systems.

Malle  BF  (2006)  How  the  Mind  Explains  Behavior:  Folk  Explanations, 
Meaning, and Social Interaction (MIT Press, Cambridge, MA).
Meske  C,  Bunde  E,  Schneider  J,  Gersch  M  (2022)  Explainable  artifi-
cial  intelligence:  Objectives,  stakeholders,  and  future  research 
opportunities. Inform. Systems Management 39(1):53–63.

Meta  AI  (2021)  Facebook’s  five  pillars  of  responsible  AI.  Accessed 
March  8,  2022,  https://ai.facebook.com/blog/facebooks-five- 
pillars-of-responsible-ai/.

Miettinen  T,  Kosfeld  M,  Fehr  E,  Weibull  J  (2020)  Revealed  prefer-
ences in a sequential prisoners’ dilemma: A horse-race between 
six utility functions. J. Econom. Behav. Organ. 173:1–25.

Molnar  C  (2020)  Interpretable  Machine  Learning:  A  Guide  for  Making 
Black Box Models Explainable. Accessed January 14, 2022, https:// 
christophm.github.io/interpretable-ml-book.

Poursabzi-Sangdeh F, Goldstein DG, Hofman JM, Wortman Vaughan 
JW, Wallach H (2021) Manipulating and measuring model inter-
pretability. Proc. CHI Conf. on Human Factors in Comput. Systems.

Pyszczynski T, Greenberg J (1987) Toward an integration of cognitive 
and  motivational  perspectives  on  social  inference:  A  biased 
hypothesis-testing model. Adv. Experiment. Soc. Psych. 20:297–340.
Rabin M, Schrag JL (1999) First impressions matter: A model of con-

firmatory bias. Quart. J. Econom. 114(1):37–82.

Rader  E,  Cotter  K,  Cho  J  (2018)  Explanations  as  mechanisms  for 
supporting algorithmic transparency. Proc. CHI Conf. on Human 
Factors in Comput. Systems.

Rahwan I, Cebrian M, Obradovich N, Bongard J, Bonnefon JF, Brea-
zeal  C,  Crandall  JW,  et  al.  (2019)  Machine  behaviour.  Nature 
568(7753):477–486.

Ribeiro  MT,  Singh  S,  Guestrin  C  (2016)  “Why  should  I  trust  you?” 
Explaining the predictions of any classifier. Proc. ACM SIGKDD 
Internat. Conf. on Knowledge Discovery and Data Mining.

Rico-Juan  JR,  de  La  Paz  PT  (2021)  Machine  learning  with  explain-
ability  or  spatial  hedonics  tools?  An  analysis  of  the  asking 
prices  in  the  housing  market  in  Alicante,  Spain.  Expert  Systems 
Appl. 171:114590.

Rosenfeld  A,  Richardson  A  (2019)  Explainability  in  human–agent 
systems. Autonomic Agent Multi Agent Systems 33(6):673–705.
Rouse  WB,  Morris  NM  (1986)  On  looking  into  the  black  box:  Pro-
spects  and  limits  in  the  search  for  mental  models.  Psych.  Bull. 
100(3):349.

Schanke  S,  Burtch  G,  Ray  G  (2021)  Estimating  the  impact  of 
“humanizing”  customer  service  chatbots.  Inform.  Systems  Res. 
32(3):736–751.

Sch¨on DA (2017) The Reflective Practitioner: How Professionals Think in

Action (Routledge, Abingdon-on-Thames, UK).

Senoner  J,  Netland  T,  Feuerriegel  S  (2021)  Using  explainable  artifi-
cial  intelligence  to  improve  process  quality:  Evidence  from 
semiconductor manufacturing. Management Sci. 68(8):5704–5723.
Shapley  LS  (1953)  A  value  for  n-person  games.  Contributions  to  the 
Theory  of  Games  (AM-28),  vol.  II  (Princeton  University  Press, 
Princeton, NJ).

Teodorescu  MH,  Morse  L,  Awwad  Y,  Kane  GC  (2021)  Failures  of 
fairness in automation require a deeper understanding of human- 
ML  augmentation.  Management  Inform.  Systems  Quart.  45(3b): 
1483–1499.

Tschandl P, Rinner C, Apalla Z, Argenziano G, Codella N, Halpern 
A,  Janda  M,  et  al.  (2020)  Human–computer  collaboration  for 
skin cancer recognition. Nature Medicine 26(8):1229–1234.

van  den  Broek  E,  Sergeeva  A,  Huysman  M  (2021)  When  the 
machine  meets  the  expert:  An  ethnography  of  developing 
AI  for  hiring.  Management  Inform.  Systems  Quart.  45(3): 
1557–1580.

Vandenbosch B, Higgins C (1996) Information acquisition and men-
tal  models:  An  investigation  into  the  relationship  between 
behaviour and learning. Inform. Systems Res. 7(2):198–214.

Vilone  G,  Longo  L  (2021)  Notions  of  explainability  and  evaluation 
approaches  for  explainable  artificial  intelligence.  Inform.  Fusion 
76:89–106.

Wang  W,  Benbasat  I  (2007)  Recommendation  agents  for  electronic 
commerce:  Effects  of  explanation  facilities  on  trusting  beliefs. J. 
Management Inform. Systems 23(4):217–246.

Willison  R,  Warkentin  M  (2013)  Beyond  deterrence:  An  expanded 
view of employee computer abuse. Management  Inform. Systems 
Quart. 37(1):1–20.

Yang F, Huang Z, Scholtz J, Arendt DL (2020) How do visual expla-
nations foster end users’ appropriate trust in machine learning? 
Proc. Internat. Conf. on Intelligent User Interfaces.

Yin D, Mitra S, Zhang H (2016) Research note—When do consumers 
value positive  vs. negative reviews? An empirical investigation 
of  confirmation  bias  in  online  word  of  mouth.  Inform.  Systems 
Res. 27(1):131–144.

.
d
e
v
r
e
s
e
r

s
t
h
g
i
r

l
l
a

,
y
l
n
o

e
s
u

l
a
n
o
s
r
e
p

r
o
F

.

0
3
:
3
2

t
a

,
6
2
0
2

y
l
u
J

6
0

n
o

]
0
5
.
9
1
.
9
4
.
7
2
[

y
b

g
r
o
.
s

m
r
o
f
n
i

m
o
r
f

d
e
d
a
o
l
n
w
o
D

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

This article was downloaded by: [27.49.19.50] On: 06 July 2026, At: 23:30
Publisher: Institute for Operations Research and the Management Sciences (INFORMS)
INFORMS is located in Maryland, USA
Information Systems Research
Publication details, including instructions for authors and subscription information:
http://pubsonline.informs.org
Expl(AI)ned: The Impact of Explainable Artificial
Intelligence on Users’ Information Processing
Kevin Bauer, Moritz von Zahn, Oliver Hinz
To cite this article:
Kevin Bauer, Moritz von Zahn, Oliver Hinz (2023) Expl(AI)ned: The Impact of Explainable Artificial Intelligence
on Users’ Information Processing. Information Systems Research 34(4):1582-1602. https://doi.org/10.1287/
isre.2023.1199
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License. You are free to download this work and share with others, but cannot change in any way or use
commercially without permission, and you must attribute this work as “Information Systems Research. Copyright ©
2023 The Author(s). https://doi.org/10.1287/isre.2023.1199, used under a Creative Commons Attribution License:
https://creativecommons.org/licenses/by-nc-nd/4.0/.”
Copyright © 2023 The Author(s)
Please scroll down for article—it is on subsequent pages
With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations
research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning
opportunities for individual professionals, and organizations of all types and sizes, to better understand and use
O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.
For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

INFORMATION SYSTEMS RESEARCH
Vol. 34, No. 4, December 2023, pp. 1582–1602
https://pubsonline.informs.org/journal/isre ISSN 1047-7047 (print), ISSN 1526-5536 (online)
Expl(AI)ned: The Impact of Explainable Artificial Intelligence on
Users’ Information Processing
Kevin Bauer,a,* Moritz von Zahn,b Oliver Hinzb
aInformation Systems Department, University of Mannheim, 68161 Mannheim, Germany; bInformation Systems Department, Goethe
University, 60323 Frankfurt am Main, Germany
*Corresponding author
Contact: kevin.bauer@uni-mannheim.de, https://orcid.org/0000-0001-8172-1261(KB); vzahn@wiwi.uni-frankfurt.de,
https://orcid.org/0000-0003-1160-1007(MvZ); ohinz@wiwi.uni-frankfurt.de, https://orcid.org/0000-0003-4757-0599(OH)
Received: June 11, 2021 Abstract. Because of a growing number of initiatives and regulations, predictions of mod-
Revised: June 2, 2022; October 28, 2022 ern artificial intelligence (AI) systems increasingly come with explanations about why they
Accepted: December 17, 2022 behave the way they do. In this paper, we explore the impact of feature-based explanations
Published Online in Articles in Advance: on users’ information processing. We designed two complementary empirical studies
March 3, 2023 where participants either made incentivized decisions on their own, with the aid of opaque
predictions, or with explained predictions. In Study 1, laypeople engaged in the deliberately
https://doi.org/10.1287/isre.2023.1199 abstract investment game task. In Study 2, experts from the real estate industry estimated
listing prices for real German apartments. Our results indicate that the provision of feature-
Copyright: © 2023 The Author(s)
based explanations paves the way for AI systems to reshape users’ sense making of infor-
mation and understanding of the world around them. Specifically, explanations change
users’ situational weighting of available information and evoke mental model adjustments.
Crucially, mental model adjustments are subject to the confirmation bias so that misconcep-
tions can persist and even accumulate, possibly leading to suboptimal or biased decisions.
Additionally, mental model adjustments create spillover effects that alter user behavior in
related yet disparate domains. Overall, this paper provides important insights into potential
downstream consequences of the broad employment of modern explainable AI methods. In
particular, side effects of mental model adjustments present a potential risk of manipulating
user behavior, promoting discriminatory inclinations, and increasing noise in decision mak-
ing. Our findings may inform the refinement of current efforts of companies building AI
systems and regulators that aim to mitigate problems associated with the black-box nature
of many modern AI systems.
History:Alessandro Acquisti, senior editor; Jason Chan, associate editor.
Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License. You are free to download this work and share with others,
but cannot change in any way or use commercially without permission, and you must attribute this
work as “Information Systems Research. Copyright © 2023 The Author(s). https://doi.org/10.1287/
isre.2023.1199, used under a Creative Commons Attribution License: https://creativecommons.org/
licenses/by-nc-nd/4.0/.”
Funding:This work was supported by the Deutsche Forschungsgemeinschaft (DFG) (Projek 449023539),
Volkswagen Foundation (ML2MT), and LeibnizInstitute for Financial Research SAFE.
Supplemental Material:The online appendix is available at https://doi.org/10.1287/isre.2023.1199.
Keywords: explainable artificial intelligence • user behavior • information processing • mental models
1. Introduction restricted contestability, and limited accountability (see
Contemporary artificial intelligence (AI) systems’ high Rosenfeld and Richardson 2019for a review). Having rec-
predictive performance frequently comes at the expense ognized these problems, organizations developing AI
of users’ understanding of why systems produce a certain and governments increasingly adopt principles and regu-
output (Gunning et al. 2019, Meske et al. 2022). For AI sys- lations (EU 2016, 2021; Google AI 2019; Meta AI 2021)
tems that provide predictions to augment highly conse- effectively stipulating that AI systems need to provide
quential processes such as hiring decisions (Hoffman meaningful explanations about why they make certain
et al. 2018), investment decisions (Ban et al. 2018), or med- predictions (Goodman and Flaxman 2017, Cabral 2021).
ical diagnosing (Jussupow et al. 2021), this “black box” In light of these developments, the implementation and
nature can create considerable downsides. These issues use of explainable AI (XAI) methods are becoming more
include impaired user trust, reduced error safeguarding, widespread and mandated by law.
1582
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1583
The purpose of XAI methods is to make AI systems’ that the explanation also, and maybe more importantly,
hidden logic intelligible to humans by answering the affects his processing of currently available information
question: Why does an AI system make the predictions it and his underlying mental models of the determinants of
does? Thereby, XAI methods aim to achieve high predic- creditworthiness. By changing mental models, explana-
tive performance and interpretability at the same time. tions may even reshape the loan officer’s behaviors in
Many state-of-the-art XAI techniques convey insights related domains beyond the loan approval decision, for
into AI systems’ logic after training and explain beha- example, assessing the faithfulness of his daughter’s new
viors by depicting the contribution of individual input boyfriend based on the smartphone charging behavior.2
features to the outputted prediction (Doshi-Velez and Considerable challenges arise when trying to answer
Kim 2017). Although there is reason to believe that XAI our research questions. First, measuring how XAI meth-
can mitigate black-box problems (Bauer et al. 2021), the ods affect users’ situational processing of information
pivotal question is how users respond to modern expla- and mental models is extremely difficult because these
nations, given that the human factor frequently creates cognitive processes are typically unobserved. Second,
unanticipated, unintended consequences even in well- we need to control for possible external cues, unin-
designed information systems (Willison and Warkentin tended stimuli, additionally attainable information, and
2013, Chatterjee et al. 2015). preferences that may affect these cognitive processes in
Nascent research on human-XAI interaction examines any given situation. Third, whether people interact with
how explainability affects humans’ perceptions, attitu- an (X)AI system, let alone rely on it, is highly endoge-
des, and use of the system, for example, trust (Erlei et al. nous and depends on factors such as culture, technolog-
2020), detection of malfunctioning (Poursabzi-Sangdeh ical literacy, and the socio-technological environment.
et al. 2021), (over)reliance (Bussone et al. 2015), and task Thus, isolating effects associated with the provision of
performance (Senoner et al. 2021). Prior research, how- explanations in addition to predictions is particularly
ever, does not consider the potential consequences of demanding, if not outright impracticable, in a natural
providing explanations for users’ situational information (organizational) setting. To address these challenges,
processing (the use of currently available information in we rely on two complementary, incentivized experi-
the given situation) and mental models (cognitive repre- mental studies.
sentations that encode beliefs, facts, and knowledge). By In Study 1 (n � 607), laypeople played a series of
depicting the contribution of individual features to speci- investment games (Berg et al. 1995), making sequential
fic predictions, feature-based XAI enables users to recog- economic transaction decisions in an intentionally ab-
nize previously unknown relationships between features stract setting. In Study 2 (n � 153), experts from the
and ground truth labels that the AI system autono- real-estate industry predicted listing prices for real
mously learned from complex data structures. In that apartments located in Germany. Study 2 extends Study
sense, XAI may constitute the channel through which AI 1 by testing the generalizability of our findings and
systems impact humans’ conceptualization and under- elaborating on mechanisms driving the results. In both
standing of their environment. This effect could reinforce studies, conditional on the treatment, participants either
the already considerable influence contemporary AI sys- received no decision support, support from an AI system
tems have on human societies (Rahwan et al. 2019) by, in the form of opaque predictions or an XAI system
for better or worse, allowing human users to adopt sys- with predictions plus feature-based explanations. We
tems’ inner logic and problem-solving strategies. Despite answer our research questions by eliciting and compar-
the increasing (legally required) implementation of XAI ing changes in both participants’ decision-making pat-
methods, a systematic study of these effects is yet miss- terns and their beliefs about feature-label relationships.
ing. The paper at hand aims to fill this important gap. The two studies strongly complement each other for
We ask three research questions. Does the additional three reasons. First, laypeople (Study 1) and experts
provision of feature-based explanations affect AI system (Study 2) are the two diametrical archetypes of AI sys-
users’ situational processing of observed information? tem users affected by growing explainability require-
Does it affect users’ underlying mental models? What are ments. Studying both types’ responses to XAI methods
important moderating factors? Consider, for instance, a enables us to identify possibly differential effects and
loan officer who works with an AI system to predict an make inferences about the generalizability of our find-
applicant’s risk parameters and determine the credit ings. Second, we consider two fundamental types of
approval. Because of legal requirements (e.g., Artificial prediction problems where AI systems are frequently in
Intelligence Act; EU 2021), the AI system recently started use: transaction outcome predictions (Study 1) and price
to provide feature-based explanations, showing that it predictions (Study 2) (Ban et al. 2018, Rico-Juan and de
strongly relies on people’s smartphone charging be- La Paz 2021). Examining the two settings allows us to
havior to predict creditworthiness.1 Although previous understand better whether the interplay between XAI and
research examines how this explanation may affect the cognitive processes is task specific. Third, using local inter-
loan officer’s perceptions of the system, we conjecture pretable model-agnostic explanations (LIME) (Study 1)
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1584 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
and SHapley Additive exPlanations (SHAP) explanations 2021, Molnar 2020). LIME (Ribeiro et al. 2016) and SHAP
(Study 2), the two most popular feature-based XAI meth- (Lundberg and Lee 2017) provide explanations through
ods (Gramegna and Giudici 2021), allows us to draw additive feature attributions, that is, linear models that
more general conclusions about the interplay between depict the numeric contribution of each feature value to
feature-based explainability and cognitive processes. the overall black box model prediction. Both approaches
Our findings paint a consistent picture: Providing learn these interpretable “surrogate models” on input-
explanations is the critical factor that enables AI systems prediction pairs of the black box model and are applica-
to influence the way people make sense of and leverage ble to virtually all classes of ML models, that is, are model
information, both situationally and more permanently. agnostic. On the individual level, SHAP and LIME
Crucially, we find an asymmetric enduring effect that can provide contrastive explanations that inform users why
foster preconceptions and spill over to other decisions, predictions for a specific instance diverge from the pre-
thereby promoting certain (possibly biased) behaviors. diction for an average instance (Molnar 2020). For
Our paper proceeds as follows. Section 2presents the- example, if the SHAP value for the feature Balcony
oretical foundations, whereas Section 3 explains our equals +500 (�200), it indicates that having a balcony
experimental studies and results. Section 4concludes by marginally increases (decreases) the current apartment’s
discussing our results, the limitations of our work, and listing price prediction by $500 ($200). The big difference
directions for future research. between LIME and SHAP is the way of estimating the
additive feature attributions. LIME creates synthetic,
2. Theory perturbed data points in the local neighborhood of the
observation of interest and fits a weighted linear model
In this section, we first discuss modern XAI methods (Sec-
to explain the relationship between the synthetic data
tion 2.1). Subsequently, we outline the relation between
and the relevant black box predictions. Importantly,
providing explanations and cognitive processes (Section
LIME weights synthetic instances based on their proxim-
2.2) and discuss our work’s contribution to the literature
ity to the original data point. By contrast, SHAP is
(Section 2.3).
inspired by coalitional game theory and treats input fea-
tures as a team of players that cooperate to generate a
2.1. Explainable AI
payoff (the prediction). The method essentially estimates
Following Doshi-Velez and Kim (2017), we conceptual-
the marginal contribution of each player to the overall
ize XAI as methods that possess the ability to present in
payoff, Shapley values (Shapley 1953), using a linear model
understandable terms to a human why an AI system
that weights instances based on characteristics of coalitions.
makes certain predictions. Over the last couple of years,
Given these mathematical differences, the two methods
researchers developed ample XAI methods that help
can produce (slightly) different feature attributions for the
elucidate the opaque logic of machine learning (ML)-
same instance. However, from the perspective of a user
based AI systems (Ribeiro et al. 2016, Lundberg and Lee
who is not familiar with these details, the intuition and
2017, Koh and Liang 2017, Lakkaraju et al. 2019). Very gen-
interpretation of the two methods’ explanations are rea-
erally, XAI methods aim to alleviate problems associated
sonably similar (Molnar 2020). Notably, LIME and SHAP
with the black-box nature (e.g., distrust, lack of accountabil-
closely relate to the seminal description of Gregor and Ben-
ity, and error safeguarding) while maintaining a high level
basat (1999) of “why and why not explanations” in the con-
of prediction accuracy (Bauer et al. 2021). text of knowledge-based expert systems.
Our study focuses on feature-based XAI methods, With the development of modern explainability meth-
hereafter XAI methods, that can explain the behavior of ods, research on the impact of contemporary XAI on user
any ML-based AI system by showing the contribution behavior has become increasingly essential (Vilone and
of individual features to the prediction. We do so for Longo 2021). Nascent research in this domain typically
several reasons. First, these explanations are the most focuses on how explanations affect user attitudes and reli-
widespread in practice (Bhatt et al. 2020, Senoner et al. ance on the AI system (Lu and Yin 2021). These studies
2021, Gramegna and Giudici 2021). Second, they are produce mixed evidence on the consequences of XAI on
highly intuitive and straightforward to interpret as they decision performance, user trust, perception, and decision-
satisfy most requirements for human-friendly explana- making performance. Several studies depict that explana-
tions (Molnar 2020). Third, they are typically applicable tions can enhance trust in and positive perceptions of the
to systems using structured and unstructured data (Gar- system (Rader et al. 2018, Dodge et al. 2019, Yang et al.
reau and Luxburg 2020). Fourth, these methods can ex- 2020), whereas others provide reversed evidence (Erlei
plain individual predictions, local explainability, which et al. 2020, Poursabzi-Sangdeh et al. 2021). Although
might be the only method legally compliant with (upcom- prior studies produce important insights regarding the
ing) regulations (Goodman and Flaxman 2017). interplay between XAI and user perceptions, none of
Many researchers recognize two related XAI methods them considers that the additional provision of explana-
as state-of-the-art: LIME and SHAP (Gramegna and Giudici tions may also reshape users’ information processing,
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1585
both situationally and more permanently. For instance, 2017). This mental process might entice people to revise
using SHAP to show the contribution of input features to their expectations and thus make different decisions
a creditworthiness prediction may not only affect a loan because the machine prediction effectively substitutes
officer’s perception of the AI system in use. Instead, she for people’s own mental model driven formation of
may process currently available information about the expectations (Agrawal et al. 2019). However, the black
applicant differently and develop a novel understanding box nature does not allow users to directly compare
of the determinants of creditworthiness, that is, adjust her their underlying beliefs and logic with that of the AI sys-
mental model. With the increasing adoption of explain- tem. This comparison can only occur when they learn
ability principles by organizations (Google AI 2019, Meta AI how the system combines available information to arrive
2021) and the growing number of regulatory transparency at a prediction. In the previous example, the real estate
requirements (EU 2016, 2021), it is pivotal to understand agent may have access to an XAI system that provides a
how contemporary XAI methods influence cognitive pro- listing price prediction together with an explanation of
cesses that lie at the heart of people’s knowledge, how specific apartment attributes contribute to it. The
behavior, and problem-solving capabilities. agent can compare the explanation to her own initial per-
ception of the individual attribute contributions to the
2.2. Cognitive Perspective on XAI Employment listing price. As a result, the agent may detect inconsis-
Through feature-based explanations about an AI sys- tencies that prompt her to revise her logic by putting
tem’s prediction, human users can observe possibly more or less emphasis on specific information currently
unknown feature-label relationships that the system available to evaluate the apartment. This explanation-
learned from complex data structures by itself (Agarwal enabled situational process (Scho¨n 2017) can reconcile
and Dhar 2014, Berente et al. 2021). Although providing the distinct logic that humans and machines apply to
explanations, in general, can have a variety of cognitive arrive at a certain assessment. From this perspective, pro-
effects, researchers across disciplines generally agree viding explanations on top of predictions may constitute
that they primarily enhance people’s understanding of a pivotal factor in allowing users to reflect on how they
someone or something, improve reasoning, and facili- leverage information to solve a problem and adapt it
tate learning (Gregor 2006, Malle 2006). From a cogni- according to the AI system’s logic for the given task.
tive perspective, obtaining explanations can entail two Apart from situationally changing cognitive processes
effects: First, it may change people’s situational proces- that shape the current decision, the interaction between
sing of available information: their use of available mental models and explanations may also yield lasting
information while observing explanations. Second, it effects because mental models possess the dynamic
can lead to an adjustment of their beliefs about feature- capacity to change (Jones et al. 2011). Repeatedly ob-
label relationships the AI system inherently models: serving explanations about how feature X contributes
ˆ
their mental representation of real-world processes. In to prediction Y and engaging in reflection processes may
this paper, we follow previous work in information sys- evoke adjustments of the underlying mental model in use.
tems and rely on the “Mental Models Framework” to con- Following Vandenbosch and Higgins (1996), exposure to
ceptualize relevant cognitive processes (Vandenbosch and external stimuli, here explanations, can lead to two mental
Higgins 1996, Lim et al. 1997, Alavi et al. 2002). model adjustment processes: maintenance and building.
Mental models are “all forms of mental representa- Under mental model maintenance, people feel encour-
tion, general or specific, from any domain, causal, inten- aged to maintain or reinforce current beliefs and decision-
tional or spatial” (Brewer 1987, p. 193), encoding beliefs, making rules. This process occurs when they perceive or
facts, and knowledge (Jones et al. 2011). Through imagi- select new information to fit into their current beliefs and
nary manipulations of model components, people can routines. Under mental model building, individuals
reason and make inferences about how to solve pro- profoundly restructure or build new mental models in
blems (Rouse and Morris 1986). Much of the people’s response to handling novel, disconfirming information.
decision making is based on these simulations that figu- As a result of these processes, individuals may adopt dif-
ratively create informal algorithms for carrying out spe- ferent beliefs about how X contributes to the real label Y,
cific tasks (Johnson-Laird et al. 2017). For instance, real enticing them to process information differently even
estate agents can mentally simulate how listing prices when explanations are no longer present. Put differently:
might change if an apartment for sale had a balcony. users may not merely combine situationally observed
When people perform tasks, they draw on relevant explanations with their own logic to solve a given task.
mental models that guide their processing of incoming Instead, observing the system’s logic may more funda-
information to form expectations and make (expectedly) mentally reshape users’ way of solving problems in gen-
optimal decisions. Working with an AI system that pro- eral, that is, evoke learning. Therefore, users may exhibit
vides black box predictions, that is, information relevant different problem-solving strategies whenever they draw
to the task, allows people to reflect on their own expecta- on the explanation-adjusted mental model, even in situa-
tions and compare it to the machine prediction (Scho¨n tions where they do not observe explanations anymore.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1586 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
In sum, cognitive theories give reason to believe that behaviors and malfunctions (Kaur et al. 2020, Lakkar-
providing explanations in addition to predictions can aju and Bastani 2020). Hence, explanations may be a
influence users’ processing of information about feature security concern if adversaries use perturbations of
X, both situationally and more fundamentally. Because inputs and model attributes to produce intentionally
of the latter effect, modern XAI methods may constitute misleading explanations that manipulate users’ trust
a cornerstone of effective knowledge transfers from and behaviors (Ghorbani et al. 2019). We complement
ML-based AI systems to human users, helping them to this pivotal and insightful work by examining the
learn from the AI how X relates to Y. Hence, explana- impact of contemporary XAI on users’ situational infor-
tions could facilitate learning machine knowledge: new mation processing and mental models. Understanding
knowledge AI systems autonomously learned from how the provision of explanations about the workings
Big Data and previously missed by domain experts of ML-based AI systems may reshape these cognitive
(Teodorescu et al. 2021, van den Broek et al. 2021). processes is pivotal for anticipating the downstream
consequences of this technology on human societies
2.3. Contribution to the Literature and designing effective transparency and explainability
Our study complements three different streams of liter- regulations.
ature. The first and most closely related line of work The second set of literature we complement explores
studies the interplay between XAI techniques and user the mechanisms of learning in socio-technological envir-
behavior (see Rosenfeld and Richardson (2019) and onments. A common theoretical foundation builds on
Vilone and Longo (2021) for an overview). About two Bayes rule as a rational benchmark of how humans
decades ago, several studies found that suitably de- accommodate new information (Holt and Smith 2009).
signed explanations about the functioning and purpose However, research has shown systematic deviations
of legacy knowledge-based expert systems can increase from Bayes’ rule. Reasons include over- or underweight-
users’ trust in the systems, improve users’ perceptions ing of new information (Rabin and Schrag 1999) and a
of the system, and enhance decision-making perfor- general tendency to asymmetrically discount information
mance (Dhaliwal and Benbasat 1996, Gregor and Benba- conflicting with prior beliefs while readily internalizing
sat 1999, Ji-Ye Mao 2000, Wang and Benbasat 2007). confirming information (Yin et al. 2016). We complement
However, these expert systems codify knowledge from this research stream by showing how human users devi-
human experts as explicit procedures, instructions, rules, ate from Bayes rule in the context of learning from mod-
and constraints in a digital format. They do not represent ern AI systems. Notably, there exists a limited number of
machine knowledge that modern ML-based AI systems prior research examining how black box predictions
learn independently of domain experts by training on change users’ decision-making habits (Abdel-Karim et al.
large data sets (van den Broek et al. 2021). Given the 2020, 2022; Fu¨gener et al. 2021a, b; Jussupow et al. 2021).
inherent distinctions between expert systems and ML- Relatedly, in a formal model, Agrawal et al. (2019) show
based AI systems in terms of encoded knowledge, con- that the predictions of black box AI systems can alter
temporary explainability methods present an entirely users’ abilities by providing them with incentives to learn
different form of reasoning to users, namely that of to assess the (negative) consequences of their actions for
machines (Vilone and Longo 2021, Meske et al. 2022). the task supported by the AI.3 None of these studies,
More recent research on the impact of explainability on however, examines the role of feature-based explanations
user behavior mainly focuses on how contemporary in learning, which could pave the way for more funda-
XAI methods impact users’ perceptions of the AI sys- mental changes in the way users understand real-world
tem. This nascent literature shows that explainability processes. Our paper intends to fill this gap. We study
often improves reliance on and trust in the system (Bus- how the provision of explanations about how an AI sys-
sone et al. 2015), fairness perceptions (Dodge et al. 2019), tem solves prediction tasks allows users to integrate the
human-AI collaboration (Yang et al. 2020), task efficiency presented machine knowledge into their mental models,
(Senoner et al. 2021), and users’ understanding of the sys- that is, learn from XAI. A better understanding of how
tem’s malfunctions (Rader et al. 2018). However, there explainability may contribute to machine teaching, the
is also evidence of disadvantages relating to infor- notion that AI systems first learn novel knowledge that
mational overload (Poursabzi-Sangdeh et al. 2021), experts neither conceive nor anticipate from data and
reduced user trust (Erlei et al. 2020), and overreliance then transfer this knowledge to human users (Abdel-
(Bussone et al. 2015). Moreover, explanations that are Karim et al. 2020), is particularly significant given the
unstable and sensitive even to small perturbations to growing requirements to implement explainability meth-
inputs have the potential to mislead human users into ods when using AI systems.
trusting a problematic black box, for example, by selec- The third stream of literature we add to studies how
tively providing explanations that conceal biased humans collaborate with computerized systems to solve
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1587
Figure 1. Structure of Empirical Studies
Notes. We provide an overview of the main sequence of our two empirical studies.
problems. Previous research in this area dates back 3. Empirical Studies
decades. Several studies document that humans resist We now present the design and results of Studies 1 and
using computerized decision aids, despite possible per- 2. In both studies, participants made decisions under
formance benefits (Kleinmuntz 1990), whereas others uncertainty (providing loans and predicting apartment
find that humans possess a strong preference for using listing prices) either with the aid of an opaque AI, an
them (Dijkstra 1999). With the growing employment of explainable AI, or without any support. We paid partici-
modern AI systems in a broad range of domains, the pants according to their decision-making performance
examination of human-machine collaboration has seen to reveal actual preferences and beliefs.4We implemen-
a considerable resurgence, for example, in the domain ted both studies using oTree, Python, and HTML and
of finance (Ge et al. 2021), medicine (Jussupow et al.
ran them online. In Study 1, we recruited 607 partici-
2021), customer service (Schanke et al. 2021), and on-
pants on Prolific and let them engage in deliberately
demand tasks (Fu¨gener et al. 2021a). Research on
abstract investment games (Berg et al. 1995). Results
“centaur” systems (Goldstein et al. 2017, Case 2018)
allow us to observe how the provision of explanations
documents how hybrid human-AI systems (i.e., cen-
on top of predictions shapes information processing
taur systems) achieve superior results in comparison
and mental models for laypeople in a very general
with the entities operating independently (Dellermann
sequential transaction domain. Study 2 extends the first
et al. 2019, Tschandl et al. 2020), promising consider-
study by testing the generalizability of mental model
able benefits from successful human-AI collaboration.
adjustments regarding the task domain (listing price
Several factors moderate the interaction of humans
predictions), decision-maker expertise, and the explana-
and AI systems including the perceived subjectivity of
tion presentation, and elaborates on important asym-
the task (Castelo et al. 2019, Logg et al. 2019), seeing the
metric effects. With the help of our industry partner, the
system err (Dietvorst et al. 2015), being able to modify
Real Estate Association Germany (IVD), we recruited 153
predictions (Dietvorst et al. 2018), the divergence bet-
experts from the real estate industry to participate in
ween actual and expected predictive performance (Jus-
Study 2. We report the designs and results of the two
supow et al. 2020), and, most importantly for our
studies consecutively. Figure 1portrays an overview of
research, understanding the system’s internal logic
the experimental designs.
(Gregor and Benbasat 1999, Hemmer et al. 2021). Fol-
lowing our conjecture that explanations pave the way
for AI systems to affect people’s cognitive processes, 3.1. Study 1
contemporary XAI methods introduce another layer of 3.1.1. Design. In Study 1, participants repeatedly en-
complexity in human-AI interaction and its success: gaged in one-shot investment games (Berg et al. 1995)
an interaction between machine and human problem- that possess the following structure. An investor receives
solving strategies. Our work provides novel insights into 10 monetary units (MU). The investor initially observes
whether and under what circumstances people prefer to 10 deliberately abstract borrower characteristics and deci-
rely on their own way of leveraging information or will- des whether to invest her 10 MU with the borrower. If
ingly adjust it according to machine explanations. In this she does not invest, the game ends without the borrower
sense, our work contributes to the literature on (hybrid) making a decision, and both the investor and borrower
human-AI collaboration by analyzing the underlying earn a payoff of 10 MU. If she invests, the borrower pos-
cognitive processes that may facilitate or hinder the reali- sesses 30 MU and can keep the whole amount without
zation of the promise of this technology. repercussions. Crucially, the borrower can repay the
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1588 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
investor 10 MU, thereby reciprocating the investor’s ini- Stage II introduced our treatment variation. Partici-
tial trust. In case of repayment, the investor receives 20 pants made 20 decisions for new random borrowers
MU (we double the amount); otherwise, the investor observing all 10 borrower traits. Additionally, base-
earns 0 MU while the borrower gets 30 MU. The bor- line participants saw an AI system’s prediction about
rower, in the absence of sufficiently strong social motives, whether borrowers will repay an initial investment.
for example, altruism, egalitarian concerns, or moral pre- Again, we did not provide intermediary feedback. We
ferences (Miettinen et al. 2020), will not make a repay- trained the AI system on 1,054 distinct data points col-
ment and maximize his personal income. As a result, the lected in a previous field study, the same data set that
payoff structure of the investment game is of an adver- the borrowers that participants encounter in the exper-
sarial nature from the investor’s perspective because her iment stem from (see the online appendix for details).7
material well-being is at the mercy of the borrower if The system did not continue to learn during the experi-
she invests. The investor loses her initial investment of ment. Treatment participants, on top of predictions,
10 MU whenever the borrower pursues pure income- observed LIME explanations (Ribeiro et al. 2016) for
maximizing or adversarial motives like wanting to each borrower characteristic, informing them of its con-
minimize the investors’ payoffs. Given this payoff tribution to the repayment prediction. Revealing LIME
structure, an income-maximizing investor in the exper- values on top of identical predictions constituted the
iment will only invest if (i) her belief that the bor- treatment variation. As is often the case, we depicted
rower’s motive leads him to repay her is sufficiently LIME values graphically using colored bars of different
strong, and (ii) she ultimately judges that the prospect lengths. Participants received detailed information about
of doubling her income is worth risking the loss of her the model, input features, performance on a representa-
investment.5Study 1 participants always played as inves- tive test set, and how to interpret LIME explanations.
tors. Borrowers are subjects from a previous incentivized
Stage III perfectly mirrored Stage I. Importantly, par-
field study who had to decide on repayment assuming
ticipants engaged with the same borrowers from Stage I
an initial investment; that is, they have already commit-
in random order. We did not draw participants’ atten-
ted to a repayment decision and cannot strategically tion to this fact to alleviate concerns about the experi-
change this choice ex post. We did not provide inter-
menter’s demand effect. The study concluded with a
mediary feedback to prevent the development of idio-
brief questionnaire on socio-economic control variables.
syncratic expertise, experience, or investment strategies
that may confound our results. We randomly matched
3.1.2. Results. Throughout our analyses of Study 1, we
investor and borrower decisions to determine game out-
mainly rely on the following regression model:
comes at the end of the study and pay both according to
the earned MU. Y ijs �β 1 ·X j +β 2 ·(X j ×I s )+β 3 ·(X j ×Expl i )
Study 1 comprised a baseline (AI) and a treatment +β ·(X ×Expl ×I )+γ +ɛ: (1)
4 j i s ijs
(XAI) condition, each with three stages.6In Stage I, each
Y is a dummy indicating whether participant i in-
participant made 10 investment decisions for distinct, ijs
vested with borrower j in Stage s. Hence, β(cid:0)coefficients
randomly drawn borrowers without intermediary feed-
back. They always observed the 10 characteristics of a measure variation in the probability to invest with a bor-
borrower and did not obtain any aid. The idea is that the rower, and X j is a vector reflecting the 10 observed bor-
10 borrower characteristics allow investors to get an rower traits, the overall prediction, and LIME values.8
idea of the likelihood that an individual borrower will Most relevant to our analyses, I s and Expl i are dummy
make a repayment, for whatever motives, and to assess variables, respectively, indicating whether a decision
whether it is worth taking the risk of losing their invest- takes place in Stage s compared with Stage I (i.e., Stage I
ment. We deliberately chose 10 unintuitive traits corre- serves as the reference category) and whether partici-
lated with a person’s repayment inclination so that pant i is in the XAI treatment (observes explanations
participants did not possess strong prior beliefs about on top of predictions in Stage II), and γ is represents
the informativeness of characteristics for someone’s individual-state fixed effects. We report standardized
repayment behavior (see Table 4 in the online appen- regression coefficients with robust standard errors. Our
dix). The main reason for choosing just these character- main interest lies in the interaction terms β 3 and β 4 ,
istics is that previous empirical tests have shown that respectively, capturing the isolated effects of observing
they are appropriate features for developing an AI sys- the prediction and additionally observing LIME explana-
tem that accurately predicts repayment with which par- tions. As β constitutes a difference-in-difference (DiD)
4
ticipants interact in Stage II. Importantly, participants estimator, it is pivotal to check that before the interven-
learned that the AI system makes predictions based on tion, there are no treatment differences (parallel trends
the same 10 borrower characteristics they also observe, assumption). Regression analyses reveal that baseline
mitigating concerns that they believed the AI system to and treatment participants in Stage I did not place signifi-
have access to more information. cantly different weight on any trait; hence, the use of a
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1589
DiD identification strategy appears generally valid. Nev- provision of explanations on top of predictions entailed
ertheless, because participants placed significant weight significant weight changes that mirror the relationship
on Gender, Conscientiousness, Neuroticism, and Younger between borrower traits and repayment behavior as
Siblings in only one of the two conditions, there is still depicted by the LIME values. Here, the average magni-
some concern about the appropriate interpretation of tude of absolute weight changes equals 73.9%. Figure
DiD estimates for these traits.9 To avoid drawing incor- 2(a) shows that the predicted repayment probability
rect conclusions, we conservatively refrain from inter- markedly decreases (increases) with a borrower’s level
preting these traits’ estimates while still including them of Competitiveness (Patience). Figure 2(b) reveals that
as controls in the model. these are the two traits whose weighting the provision
of explanations significantly fostered: observing expla-
3.1.2.1. Situational Information Processing. We start nations rendered the relationship between a borrower’s
analyzing how participants’ weighting of borrower char- Competitiveness (Patience) and a participant’s investment
acteristics changed from Stage I to II, that is, changes in likelihood significantly more negative (positive). Nota-
participants’ situational information processing. Figure 2 bly, explanations as such increased the absolute magni-
illustrates our results. Figure 2(a) depicts the average LIME tude of the coefficient for Competitiveness (Patience) by
values (color saturation) participants observed for different 240.0% (94.6%). LIME values reveal that Agreeableness,
feature values (y and x axis). Higher positive (negative) the trait participants initially weighted the most, has
LIME values depict a higher positive (negative) contribu- almost no impact on the repayment prediction. Accord-
tion of a given feature value to the predicted probability ingly, we find that the provision of explanations led to a
that a borrower makes a repayment. Figure 2(b) portrays significant decrease in the magnitude of the weight parti-
how the provision of predictions and explanations affected cipants placed on this trait (�44.7%). Additional analyses
the weighting of a given borrower trait. The diamond confirm that LIME values for these three characteristics
marker represents the original weighting in Stage I (β ). had a significantly positive influence on participants’
1
The dashed and solid arrows, respectively, illustrate investment decisions, corroborating the notion that parti-
the isolated effects of observing predictions (β ) and cipants paid attention to and adjusted their weighting of
3
additional explanations (β ). Depicted results stem from traits according to observed explanations (see Table 11 in
4
regressions reported in Table 9 in the online appendix. the online appendix). Taken together, participants signifi-
There are two main insights. First, prediction effects cantly adjusted their weighting of information in the
in Figure 2(b) suggest that the provision of opaque pre- direction of observed explanations for (i) the trait they ini-
dictions generally decreased the weight participants tially perceived as most important and (ii) the traits LIME
placed on observed borrower traits. On average, the highlighted as most important.10 Finally, although not
absolute magnitude of coefficients changed by 63.6%. shown in the Figure 2 for ease of interpretation, regres-
Although only the estimates for Agreeableness, Patience, sion analyses further reveal that explanations signifi-
and Older Siblings are significant, predictions reduced cantly reduced the weight participants placed on the
the absolute magnitude of all variables. Second, the prediction as such (magnitude of coefficient decreased
Figure 2. (Color online) Prediction and Explanation Effects on Situational Information Processing
Notes. We illustrate how the provision of opaque predictions and LIME explanations on top of predictions affect participants situational informa-
tion processing. (a) LIME values (z axis) for different feature values (x axis) participants observed in the study. For the binary feature Older sib-
lings, we show the LIME values for No and Yes at the outer limits of the continuous feature scale. (b) Estimated prediction and explanation
effects, respectively, of β and β in Model (1) with s �2. Initial values represent β. We denote significance levels by *p <0.1, **p <0.05, and ***p
3 4 1
<0.01.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1590 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
by 26.8%); that is, they were less likely to follow a predic- solid arrows, respectively, show how having observed
tion that a borrower makes a repayment.11 predictions (β ) and explanations on top of predictions
3
(β ) did fundamentally alter participants’ information
Result 1.1. Observing explanations changed participants’ 4
processing, that is, mental models.
situational processing of the overall prediction and borrower
Observing opaque predictions did not result in a sig-
traits that explanations or they themselves consider most
nificant change in participants’ weighting of borrower
important. The direction of adjustments mirrors explanations.
traits. By contrast, depicted results suggest that providing
Result 1.1 agrees with our theoretical elaborations: explanations did entail an adjustment of mental models
People adjust their situational information processing in with the absolute magnitude of coefficients changing by
response and according to explanations they currently 61.8% on average. Importantly, this adjustment was
observe. Notably, elicited expectations about the predic- asymmetric. Observing explanations led participants to
tion accuracy did not differ significantly for predictions place significantly more weight on borrowers’ Competi-
with or without explanations (71.8% and 70.6%, respec- tiveness (+148.6%) and Patience (+59.4%) in Stage III than
tively; p � 0.751, Wilcoxon rank-sum test). Therefore, in Stage I. The weight changes again mirror the observed
changes in the weighting of predictions do not seem to LIME explanations. After observing explanations that the
result from lower performance expectations. Next, we AI system places the most weight on borrowers’ Competi-
test the conjecture that explanations affect beliefs about tiveness and Patience, participants increased their weight-
the relationship between borrower characteristics and ing of these attributes even for investment decisions
repayment behavior, that is, mental models. where they no longer observed explanations. Intrigu-
ingly, we do not find that explanations about the low rel-
3.1.2.2. Mental Model Adjustments. We compare par- evance of Agreeableness led participants to adjust their
ticipants’ information weighting across Stages I and III marked weighting of this trait significantly. Although par-
to test the conjecture that explanations affect mental mod- ticipants weighted Agreeableness significantly less while
els about the relationship between borrower traits and observing explanations, they returned to their original
repayment behavior. We rely on the regression model weighting of it once they lost access to the XAI system.
(1), setting s �3 and excluding controls for the prediction Naturally, one may wonder about this asymmetry’s ori-
and LIME values. Figure 3 illustrates regression results gins. One plausible interpretation is that explanations are
that we report in Table 12 in the online appendix. less likely to evoke pronounced mental model adjust-
Figure 3 portrays how the provision of predictions ments when they conflict with strong preconceptions. Put
and explanations lastingly changed the weighting of a differently, people are more inclined to engage in mental
given borrower trait across Stages I and III, where parti- model maintenance rather than building because it is less
cipants had no (X)AI aid. The diamond marker depicts cognitively demanding and creates less psychological dis-
the original weighting in Stage I (β ). The dashed and tress (Vandenbosch and Higgins 1996). In Stage I, partici-
1
pants put by far the most emphasis on a borrower’s
Agreeableness to decide on investing. LIME values, how-
Figure 3. Mental Model Adjustments
ever, suggested that this conception is incorrect because it
is among the least relevant predictors for borrowers’
repayment inclination. Although one would expect that
participants engaged in mental model building to reshape
their beliefs about the relationship between Agreeableness
and repayment behavior, we do not find significant
adjustments. For Competitiveness (Patience), explanations
depicted an important negative (positive) influence,
which, given their initial weighting of it, confirmed par-
ticipants’ prior beliefs. Following the Mental Models
framework, confirming explanations should evoke the
maintenance or reinforcement of prior beliefs. Given
the significant explanation effects, it seems that partici-
pants willingly engaged in this process. This inclination
to engage in mental model maintenance rather than
building more generally concurs with the frequently
Notes. We depict participants’ mental model adjustments as mea- documented confirmation bias (Yin et al. 2016), that is,
sured by their change in the weighting of borrower traits across the tendency to selectively process information in a
Stages I and III. The estimated prediction and explanation effects
way that allows for the continuation or strengthening
respectively represent β and β in Model (1) with s �3. Initial values
represent β. We denote 3 s ignific 4 a nce levels by *p <0.1, **p <0.05, and of beliefs. We elaborate on this issue in Study 2 and the
1
***p <0.01. discussion.12
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1591
Result 1.2. Machine explanations entailed asymmetric men- of the cases. As a result, treatment and baseline partici-
tal model adjustments. Participants reinforced priors that pants respectively achieved a decision accuracy of 51.7%
explanations confirmed but did not abandon priors that and 57.2% (�9.6%, p <0.01, F test) for most competitive
explanations markedly contradicted. borrowers and 59.5% and 62.8% (�5.3%, p <0.05, F test)
for other borrowers. Notably, participants already associ-
3.1.2.3. Investment Performance. Thus far, it remains ated very high competitiveness with a low repayment
open how providing explanations on top of predictions likelihood in Stage I: Most competitive borrowers re-
affected participants’ decision-making performance in ceived an investment in 56.3% of the cases, whereas all
our setting. Table 1 summarizes participants’ perfor- others did so in 69.5% of the cases (there do not exist
mance measured by the accuracy (share of payoff maxi- treatment differences). Against this background, expla-
mizing decisions) and recall (share of investments with nations seem to have exacerbated this inaccurate pat-
repaying borrowers). We also report p values of F tests tern16 to an extent that treatment participants made
to illustrate significant treatment differences.13 significantly worse decisions than before. Put differently,
Although there are no differences in Stage I, treatment confirming explanations inappropriately reinforced pre-
participants performed significantly worse than base- conceptions about most competitive borrowers not re-
line ones in Stage II (�8.9% and �11.0% for accuracy paying an investment in our setting.
and recall, respectively).14Treatment participants’ rela-
Result 1.3. Participants excessively increased the isolated
tively lower performance in Stage II stems from not
weighting of a trait they already believe to be evidence
investing with the most competitive borrowers (with
against repayment. This reaction inefficiently decreased
most negative LIME values), whereas the overall predic-
participants’ likelihood to invest with repaying borrowers
tion implies doing so, that is, from overruling positive
predictions.15 that were highly competitive.
They overruled positive predictions and refrained In sum, the results for Study 1 are highly consistent
from investing in 46.5% of these cases, resulting in a with the notion that the provision of explanations cre-
decision accuracy of merely 53.5%. Baseline partici- ates a novel channel through which AI systems may
pants, for most competitive borrowers, overruled posi-
reshape users’ way of processing information, both situ-
tive predictions only in 21.2% of the cases and achieved
ationally and more permanently. For the latter effect,
a decision accuracy of 78.9%; that is, they are 47.5%
we observe an asymmetry that is reminiscent of a confir-
more likely to make an income maximizing decision
mation bias and, in our setting, decreased participants’
than treatment participants. For all other borrowers,
decision-making performance by excessively reinfor-
treatment (baseline) participants overruled positive pre-
cing inaccurate preconceptions.
dictions and made optimal decisions in 23% (19.4%) and
69.6% (71.1%) of the cases, respectively. Hence, treat-
ment participants seem to have placed too much weight 3.2. Study 2
on very high competitiveness, leading them to overrule The goal of Study 2 is twofold. First, we extend Study 1
the overall prediction inefficiently often. results by testing the generalizability of mental model
Examining Stage III, we find that this overweighting of adjustment findings regarding the task domain, user
the highest competitiveness level persisted even when expertise, and explanation presentation and examining
participants did not observe explanations anymore (see whether the asymmetry we found for explanation-driven
Table 13 in the online appendix). In Stage III, treatment mental model adjustments in Study 1 is indeed a manifes-
(baseline) participants invested with most competitive tation of the confirmation bias. Second, we explore if men-
borrowers in 44.7% (54.7%, p < 0.01, F test) of the cases tal model adjustments spill over to related but disparate
and with other borrowers in 68.2% (67.6%, p <0.7, F test) domains.
Table 1. Investment Performance Across Stages
Stage I (no aid) Stage II (with aid) Stage III (no aid)
Accuracy Recall Accuracy Recall Accuracy Recall
Baseline (AI) (%) 60.3 64.9 63.1 64.6 62.7 65.1
Treatment (XAI) (%) 60.7 67.4 57.5 57.5 56.5 60.2
F test: Baseline versus treatment p �0.79 p �0.31 p <0.01*** p <0.01*** p <0.02** p <0.04**
Notes. We depict participants’ investment performance as measured by their accuracy (share of payoff maximizing decisions) and recall (share
of investments with repaying borrowers) in Stages I, II, and III. We report results separately for baseline (AI) and treatment (XAI) participants. F
tests reveal the significance of treatment differences per measure and stage.
*p <0.1; **p <0.05; and ***p <0.01.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1592 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
3.2.1. Design. Study 2 comprises four consecutive stages, importantly, the apartment was in a midsize city in east-
where recruited real estate experts estimated the list- ern Germany (Chemnitz). For historical, demographic,
ing price per square meter in Euros of apartments that and socioeconomic reasons, Chemnitz is very different
we previously collected from a large online plat- from “A-cities” such as Frankfurt and Cologne, so the
form.17 Participants saw 10 apartment characteristics housing market is also very different. Germans in gen-
to make an informed guess and did not receive inter- eral and real estate agents in particular are usually
mediate feedback. To reduce the task complexity and aware of this East-West disparity.20 The study con-
avoid informational overload, we fixed seven apart- cluded with a questionnaire on participants’ socio-
ment characteristics across all stages, that is, apartments demographics.
only differed regarding the same three characteristics:
Location (Frankfurt/Cologne), Balcony (Yes/No), and 3.2.2. Results. We report our results in three steps.
Green voter share in the district (Below city average/City First, we outline the experts’ belief adjustments from
average/Above city average).18 We provide screenshots Stage I to Stage III. Second, we examine the occurrence
of the interfaces from each stage in the online appendix. of confirmation bias in these adjustment processes.
In Stage I, we elicited participants’ initial beliefs about Finally, we analyze experts’ listing price estimates in
the relationship between the three variable apartment Stage IV.
characteristics and listing prices. Participants estimated
the listing price of four random apartments with differ- 3.2.2.1. Mental Model Adjustments. Figure 4 shows
ent combinations of the variable attributes by entering the distribution of absolute differences between experts’
their marginal contributions to the price using a slider. beliefs about the marginal contribution of the three vari-
Sliders ranged from minus to plus 2.500e in steps of 50e. able attributes before and after the treatment interven-
We initially set the marginal contributions and overall tion. We show results for the NoAid, AI, and XAI
price estimation to 0e and the average listing price conditions. The distributions for the NoAid and AI con-
(9,600e), respectively. Participants additionally stated ditions are remarkably similar and skewed toward zero,
their confidence in the entered marginal contributions indicating that experts frequently did not adjust beliefs.
and the resulting price estimation on a five-point scale. The distribution for XAI participants is considerably less
Stage II introduced our treatment variations. In all right-skewed; that is, they adjusted their beliefs across
variations, participants estimated listing prices for eight Stages I and III more. On average, NoAid, AI, and XAI
random apartments with different combinations of vari- participants’ absolute belief adjustments equaled 166.4e,
able attributes they did not encounter in Stage I. In con- 165.4e, and 299.1e, respectively. Only the differences
trast to Stage I, participants directly entered the estimated between NoAid versus XAI (+79.7%, p <0.01, F test), and
listing price. As a reference point, they again observed the AI versus XAI (+80.8%, p <0.01, F test) conditions are sta-
average listing price for an apartment. Participants stated tistically significant (see Table 24 in the online appendix),
their confidence on a five-point scale. In our baseline con- that is, observing explanations led to remarkably stron-
dition (NoAid), participants estimated the price without ger adjustments of beliefs. Our notion is that real estate
any aid. Participants in the AI condition observed opaque experts updated initially held mental models about the
listing price predictions of a steady, that is, nonlearning, relationship between apartment attributes and listing
AI system trained on 4,975 collected observations.19 In prices as they encountered SHAP explanations. Contrast-
our XAI condition, in addition to observing these predic- ing our first study, we directly measure participants’
tions, participants also saw numerically presented SHAP prior and posterior beliefs about the contribution of dis-
values for the three variable apartment characteristics, tinct apartment characteristics to listing prices in Study 2.
that is, marginal contributions to the prediction in Euros. This design facet enables us to estimate mental model
After they entered all eight listing price estimates, parti- adjustments directly, leveraging the accepted framework
cipants in treatments with decision support filled out a by DeGroot (1974). Specifically, we assume that agent i’s
survey containing items on their trust, degree of reli- posterior belief about the relationship of characteristic j
ance, and perceived transparency of the AI system (and and the listing price Post �a ·Prior +(1�a )·Expl
i,j i,j i,j i,j i,j
explanations). is a weighted combination of the corresponding prior
Stage III replicated Stage I to measure posterior beliefs. belief Prior and the personally observed explanation
i,j
Independent of the condition, participants again made Expl ; 1�a represents the extent of belief adaptation in
i,j i,j
decisions without any aid for the same apartments. the direction of the explanation, whereas a describes the
i,j
Finally, in Stage IV, participants estimated the listing anchoring of the previous belief. For instance, in the
price for one last apartment without any decision aid. extreme case of 1�a �1, individual i completely aban-
i,j
Across participants, we varied the balcony and green dons her prior mental model and adopts the observed
voter attribute of the apartment, whereas the seven fixed explanation as her new one. We estimate the weights
attributes were identical to the previous listings. Most (1�a) and a for our three study conditions using a
i i
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)  1593
regression model comprising treatment interactions that  Table 2. Posterior Belief Formation
has the following form:
|     |         |     |           |            |      |     | Dependent variable: Posterior belief |     | (1) | (2) |
| --- | ------- | --- | --------- | ---------- | ---- | --- | ------------------------------------ | --- | --- | --- |
| Pos | �β ·Pri | +β  | ·(AI ×Pri | )+β ·(Expl | ×Pri | )   |                                      |     |     |     |
ijk 1 ijk 2 i ijk 3 i ijk Prior belief (β ) 0.634*** 0.782***
1
|     | +β  | ·SV +β | ·(AI ×SV | )+β ·(Expl | ×SV | )    |                        |     | (0.060)   | (0.063)   |
| --- | --- | ------ | -------- | ---------- | --- | ---- | ---------------------- | --- | --------- | --------- |
|     | 4   | ij     | 5 i      | ij 6       | i   | ij   |                        |     |           |           |
|     |     |        |          |            |     |      | Prior belief ×AI (β)   |     | 0.070     | �0.027    |
|     | +γ  | +δ +ɛ: |          |            |     | (2)  |                        | 2   |           |           |
|     | i   | k      |          |            |     |      |                        |     | (0.104)   | (0.084)   |
|     |     |        |          |            |     |      | Prior belief ×Expl. (β | )   | �0.276*** | �0.240*** |
3
 .devreser sthgir lla ,ylno esu lanosrep roF . 03:32 ta ,6202 yluJ 60 no ]05.91.94.72[ yb gro.smrofni morf dedaolnwoD The variables Pos ijk  and Pri ijk , respectively, represent  (0.084) (0.075)
expert i’s posterior and prior beliefs about attribute j’s  Avg. SHAP (β ) 0.025 0.033
4
contribution to apartment k’s listing price in Euros.  (0.040) (0.039)
|                      |     |     |                                 |     |     |     | Avg. SHAP ×AI (β | )   | 0.078   | 0.083   |
| -------------------- | --- | --- | ------------------------------- | --- | --- | --- | ---------------- | --- | ------- | ------- |
| Most importantly, AI |     |     | is a dummy variable indicating  |     |     |     |                  | 5   |         |         |
|                      |     |     | i                               |     |     |     |                  |     | (0.053) | (0.050) |
that expert i observed a prediction, whereas the dummy
|     |     |     |     |     |     |     | Avg. SHAP ×Expl. (β | )   | 0.265*** | 0.249*** |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | -------- |
6
Expl equals one if a participant additionally observed  (0.053) (0.052)
i
explanations; SV represents the average SHAP value  Fixed effects No Yes
ij
|     |     |     |     |     |     |     | N   |     | 1,836 | 1,836 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
for apartment attribute j of the apartments participant i
|                                |     |     |     |       |                 |     | R2  |     | 0.740 | 0.787 |
| ------------------------------ | --- | --- | --- | ----- | --------------- | --- | --- | --- | ----- | ----- |
| encountered in Stage II; and γ |     |     |     | and δ | are expert and  |     |     |     |       |       |
|                                |     |     |     | i  k  |                 |     |     |     |       |       |
Notes. We depict results from OLS regression models with robust
apartment controls, respectively.
standard errors reported in parentheses. The dependent variable
| On  | an  individual  |     | level,  | Model  (2)  | estimates  | how  |     |     |     |     |
| --- | --------------- | --- | ------- | ----------- | ---------- | ---- | --- | --- | --- | --- |
equals participants’ posterior belief about the marginal contribution
observed SHAP values affected participants’ adjustments
of apartment attributes to the listing price in euros. The main
of beliefs about the relationship between a given charac- independent variables of interest are participants’ prior beliefs, the
teristic and the listing price. It enables us to quantify the  average SHAP values for apartment attributes in Stage II, a dummy
“stickiness” of prior beliefs (β �β indicating that participants observed a prediction in Stage II (AI), a
) and “gravitational  dummy indicating that participants observed explanations in Stage II
|     |     |     |     | 1 3 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pull” of explanations (β �β ) and directly test the occur- (XAI), and interaction terms. We further control for the overall
|     |     |     | 4 6 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rence of confirmation bias. Importantly, this estimation is  posterior listing price participants entered for the apartment and its
interaction with treatment dummies, and the average prediction they
only possible for Study 2, where we elicited prior and
|     |     |     |     |     |     |     | observed  in  | Stage  II.  In  column  | (2),  we  additionally  | include  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------------- | ----------------------- | -------- |
posterior beliefs about distinct feature-label relationships.
individual and apartment fixed effects.
In Study 1, we measured the ultimate investment deci- *p <0.1; **p <0.05; and ***p <0.01.
sions only and observed belief changes indirectly through
changes in those decisions. As a result, we cannot individ-
(unsurprisingly) have no significant explanatory power
ually quantify the impact of observed explanations on
|     |     |     |     |     |     |     | regarding posterior beliefs (see β |     | and β ).21When parti- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --------------------- | --- |
specific beliefs nor can we analyze confirmation bias: a  4  5
cipants did not obtain machine aid or only observed
key contribution of our second study.
predictions, their prior and posterior beliefs were more
| Table 2 | depicts regression results for Model (2). Re- |     |     |     |     |     |                                   |     |                               |     |
| ------- | --------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------- | --- | ----------------------------- | --- |
|         |                                               |     |     |     |     |     | than 60% positively correlated (β |     | 1  and β 2 ); that is, parti- |     |
sults show that in our NoAid and AI conditions where
cipants barely adjusted their beliefs. Only when partici-
participants did not observe explanations, SHAP values
pants observed explanations in addition to predictions
did the displayed SHAP values have positive, statisti-
|                                                           |     |     |     |     |     |     | cally significant effects. β |     | reveals that XAI participants  |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | ------------------------------ | --- |
| Figure 4. (Color online) Distribution of Absolute Belief  |     |     |     |     |     |     |                              | 6   |                                |     |
Changes  significantly adjusted their beliefs in the direction of
observed explanations. According to the estimate, pos-
terior beliefs resembled SHAP values more closely
in the XAI treatment condition compared with the
NoAid and AI conditions (approximately +25 percent-
age points). Observing explanations also caused XAI
participants’ posterior beliefs to resemble their prior
|     |     |     |     |     |     |     | significantly less (β | ), that is, prior beliefs became less  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | -------------------------------------- | --- | --- |
3
“sticky” compared with the NoAid and AI conditions
(approximately �25 percentage points). In sum, these
results suggest that observing SHAP explanations led
participants to adjust their beliefs in the direction of
explanations and abandon their priors. This insight
corroborates our Result 1.2in Study 1 on an individual
level, revealing that explanation-driven mental model
Notes. We depict the distribution of experts’ absolute belief adjust-
adjustments also occur for experienced experts, who
ments across Stages I and III. We aggregate the belief adjustments
are arguably familiar with apartment traits and listing
over all apartment attributes. Different distributions show results sep-
price predictions.22
arately for NoAid, AI, and XAI participants.

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1594 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
3.2.2.2. Confirmation Bias. In Study 1, we observed Table 3. Confirmation Bias and Posterior Belief Formation
asymmetric mental model adjustments that are reminis-
Dependent (1) (2) (3)
cent of the confirmation bias. The design of Study 2
variable: Low High
allows us to test for confirmation bias in mental model
Posterior belief Overall confidencebeliefs confidencebeliefs
adjustment processes more directly by examining
whether XAI participants’ adjustments depended on Prior belief 0.492*** 0.483*** 0.496***
(0.091) (0.105) (0.136)
the alignment of explanations and prior beliefs.
Avg. SHAP 0.303*** 0.344*** 0.145**
We define that explanations confirmed an expert’s
(0.043) (0.055) (0.067)
preconception about the price contribution of a specific Confirm 12.039 �10.838 115.724
apartment attribute if the prior and the observed aver- (27.949) (39.552) (73.702)
age SHAP value for the corresponding attribute have Avg. SHAP 0.166*** 0.107 0.301***
×Confirm (0.059) (0.077) (0.094)
the same sign. With this definition, observed explana-
N 708 481 222
tions confirm prior beliefs in 49.6% of the cases.23 We R2 0.746 0.725 0.843
analyze differences in belief adjustments with respect to
Notes. We depict results from OLS regression models with individual
confirming and conflicting explanations using a modi-
and apartment fixed effects. We report robust standard errors reported
fied version of Model (2). Specifically, we are interested in parentheses. The dependent variable equals XAI participants’
in whether the convergence of XAI participants’ poste- posterior belief about the marginal contribution of apartment attributes
rior beliefs toward observed SHAP values only occurred to the listing price in euros. The main independent variables of interest
are participants’ prior beliefs, the average SHAP values for apartment
when explanations confirmed prior beliefs. Therefore,
attributes in Stage II, a dummy indicating that observed SHAP values
we focus on the subsample of XAI participants allowing in Stage II confirmed participants’ priors, measured by an equal sign of
us to omit treatment dummies and interaction terms prior beliefs and average SHAP values for a given attribute, and
interaction terms. We further control for the overall posterior listing
which facilitates the interpretation of results. Along the
price participants entered for the apartment and the average prediction
lines of Model (2), we regress XAI participants’ posterior
they observed in Stage II. Column (1) presents results for all decisions.
beliefs about the relationship between apartment charac- Columns (2) and (3) respectively depict results for the shares of
teristics and the listing price on their prior beliefs and decisions where XAI participants report low and high confidence in
their prior. observed SHAP values. Most importantly, we now add
*p <0.1; **p <0.05; and ***p <0.01.
a dummy variable (Confirm) indicating whether explana-
tions confirmed prior beliefs and its interaction with
average SHAP values and prior beliefs as independent
2009). To test the existence of such heterogeneity, we
variables. The interaction Avg. SHAP ×Confirm will pro-
consider experts’ reported confidence in prior beliefs
vide insights into whether the influence of observed
and define that an expert possessed low (high) confi-
SHAP values on belief adjustments depended on the
dence in a prior, if, on a five-point scale, they reported a
alignment of explanations and prior beliefs, which are
confidence level of less than 4 (at least 4). In columns (2)
insights we cannot obtain from Study 1 using Model (1).
and (3) of Table 3, we, respectively, repeat the regression
Corroborating our interpretation of Result 1.2 from
analysis reported in column (1) for the subsamples of
Study 1, we find that explanation-driven belief adjust-
low- and high-confidence prior beliefs.
ment processes depended on whether explanations con-
Reported estimates provide further evidence that
firmed or conflicted with prior beliefs. The estimate for
explanation-enabled mental model adjustments were
the interaction term Avg. SHAP × Confirm is positive
subject to confirmation bias. According to the estimated
and statistically significant (see column (1) in Table 3).
coefficient of Avg. SHAP × Confirm, for low-confidence
Following the estimate, posterior beliefs resembled ob-
priors, the influence of observed SHAP values on poste-
served SHAP values significantly more closely (about
rior beliefs did not depend on whether explanations
50% more) if they confirmed their prior beliefs. Hence,
confirmed prior beliefs (see column (2)). Considering
consistent with confirmation bias, the belief adjustment
the positive and significant estimate of Avg. SHAP, the
was asymmetric regarding the confirmatory nature of
belief updating was in line with Bayes rule. By con-
explanations. If participants had updated beliefs ratio-
trast, for high-confidence priors, belief adjustments
nally according to Bayes rule, the interaction term should
were highly sensitive to whether SHAP values confirmed
be insignificant as Bayesian observers would not weight
priors (see column (3)). The estimate for Avg. SHAP ×
explanations conditional on their alignment with prior
Confirm suggests that the magnitude of the adjustment of
beliefs (Rabin and Schrag 1999).
high-confidence priors was about two times larger when
To elaborate on the notion that these asymmetric
observed explanations were in line with them.
belief adjustments are a manifestation of confirmation
bias, we further consider the role of experts’ confidence Result 2.1. Study 1 findings extend to expert users, SHAP
in their prior beliefs. Prior research shows that confirma- explanations, and the domain of apartment price predic-
tion bias is strongest for entrenched beliefs (Pyszczynski tions: SHAP explanations led real estate experts to adjust
and Greenberg 1987, Knobloch-Westerwick and Meng prior beliefs about the relation between apartment attributes
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1595
and listing prices. Adjustment processes were subject to the Specifically, compared with observing no predictions
confirmation bias. (opaque predictions), observing explained predictions
decreased Chemnitz price estimates by 33.9% (38.9%) if
3.2.2.3. Spillover Effects. Although we observe that the share of green voters was low and increased price
real estate experts (asymmetrically) adjusted prior be- estimates by 16.5% (32.4%) if the share of green voters
liefs, all previously reported results pertain to the same was high. As one might expect, the direction of the differ-
market: Participants observed SHAP explanations for ence in experts’ evaluation of the green voter share attri-
the same two A-cities in Western Germany, for which bute is in line with explanations observed in Stage II:
we elicited prior and posterior beliefs. What remains SHAP values indicated that in Frankfurt and Cologne, a
open is whether explanation-driven belief adjustments high (low) share of green voters marginally contributes
spilled over to the listing price estimation for apart- to listing prices by about +652e (�613e). We do not find
ments in different markets. We put this idea to the test any effect for experts who only observed opaque predic-
by examining the distribution of participants’ final price tions in Stage II.
predictions for an apartment in a medium-sized eastern To elaborate on these findings, we also perform a
German city that is not an “A city”: Chemnitz.24 median split and analyze the subsamples of experts
Figure 5 shows the distribution of listing price esti- whose average absolute belief adjustment for the attri-
mates conditional on the share of green voters in the dis- bute “Green voter” is below and above the median.
trict for NoAid, AI, and XAI participants. The results Consistent with the idea that belief spillover effects
indicate that observing explanations impacted partici- drive differences in listing price estimates in Chemnitz,
pants’ price estimates for Chemnitz apartments in neigh- experts who strongly adjusted their beliefs about the rel-
borhoods with high and low proportions of green voters. evance of “Green voters” from Stage I to III drive our
Figure 5(a) shows that the distribution of listing prices for aggregate-level results. We do not find significant treat-
an apartment in a district with a low green voter share is ment differences in the accuracy of participants’ listing
considerably more right-skewed for XAI than NoAid or price estimates as measured by the absolute deviation
AI participants; that is, they estimate relatively low prices from actual prices. Nevertheless, our results show that
more frequently. NoAid, AI, and XAI participants on using XAI as a decision support tool in one market can
average estimated a listing price of 4,752e, 5,141e, and affect aggregate listing prices in another market in an eco-
3,140e, respectively. Only the differences between NoAid nomically considerably way (average absolute change:
versus XAI and AI versus XAI are statistically significant approximately 20%), which is not the case for opaque
in regression analyses (p <0.05, F test, for both). The dis- systems. This result demonstrates that XAI methods can
tribution of price estimates in districts with high shares of link disparate decision-making tasks.
green voters has a stronger left-skew for XAI participants
Result 2.2. Pronounced explanation-driven belief adjust-
than their NoAid and AI counterparts (Figure 5(b)). On
ments spill over to experts’ listing price estimation in a fun-
average, NoAid, AI, and XAI participants estimated a
damentally different market.
listing price of 5,231e, 4,600e, and 6,092e, respectively, for
an apartment in a district with a high percentage of green In summary, our results from Study 2 (i) demonstrate
voters. Again, we only find significant explanation effects the robustness of our results from Study 1 on mental
(p < 0.1, F test, for both). These results reveal the eco- model adjustments in terms of system user expertise,
nomic significance in the changes of price distributions. explanation representation, and decision domain; (ii)
Figure 5. (Color online) Price Distributions in Chemnitz
Notes. We depict the distribution of experts’ listing price estimates in Chemnitz. (a) and (b) Price distribution for apartments in a district with a
low and high share of green voters, respectively. Different distributions show results separately for NoAid, AI, and XAI participants.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1596 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
provide strong evidence that explanation-driven mental From a theoretical perspective, our results contribute
model adjustments are subject to confirmation bias; and to our understanding of the role of popular XAI meth-
(iii) show that explanation-driven mental model adjust- ods in effective knowledge transfers from ML-based AI
ments generate significant spillover effects. systems to human users. A key promise of modern AI
systems is that the application of ML techniques will
4. Discussion and Conclusion discover new knowledge from Big Data that has previ-
We report results from two empirical studies that pro- ously eluded even experienced experts (Berente et al.
2021, van den Broek et al. 2021). This “machine knowl-
vide novel insights into the interplay between the use of
edge” is typically codified in the form of a complex pre-
feature-based XAI methods and users’ cognitive pro-
dictive model that outperforms humans. We show that
cesses. Our main contribution is the identification of
providing predictions alone is insufficient to achieve
considerable side effects of providing feature-based
systematic knowledge transfers from AI systems to
explanations, the most popular form of XAI methods,
human users. In both our studies, neither laymen nor
on users’ situational information processing and mental
experts adapted their understanding of the relation-
models. We find that the latter effect (i) is subject to the
ships between features X and label Y according to
confirmation bias so that misconceptions can persist
“machine knowledge” when observing only opaque
and even accumulate, possibly leading to suboptimal
predictions. Merely in treatments where users also had
decisions, and (ii) can create spillover effects into other
access to explanations, they began to adapt their app-
decision domains. These overarching results suggest that
roach to solving the task so that it more closely matched
the growing, partially legally required, use of feature-
the strategy of the AI system. Therefore, XAI methods
based XAI methods opens a new channel through which
appear to be a pivotal factor contributing to an effective
AI systems may fundamentally reshape the way humans
channel through which AI systems can pass on their
understand real-world relationships between features X
self-learned knowledge to human users. Crucially,
and target variables Y. In the following, we discuss our
feature-based XAI methods seem to induce an asymme-
results, present implications for organizations and soci-
try in mental model adjustments: users adjust their
ety, and, based on the limitations of our studies, provide
beliefs more in the direction of observed explanations if
directions for future research.
they confirm rather than disconfirm their priors. This
asymmetry contradicts with the updating behavior of a
4.1. Discussion of Results
Bayesian observer who would neither over- nor under-
Study 1 demonstrates that the provision of explanations
weight explanations conditional on them confirming or
can situationally lead lay users to adjust their weighing
disconfirming prior beliefs. This asymmetry occurred
of features accordingly, the average absolute change in
regardless of whether we provide graphically visual-
estimates equals 73.9%, and to put less emphasis on the
ized LIME or numerically represented SHAP explana-
overall prediction (�26.8%). Explanations also evoked
tions. It therefore seems as if additive feature-based
asymmetric changes in lay users’ conceptions about the
explanations more generally evoke cognitive processes
relationship between borrower traits and repayment
leading users to learn from the machine selectively.
inclinations that influence behaviors even when they do
Researchers across disciplines commonly refer to such an
not observe explanations anymore, the average absolute
asymmetry as confirmation bias (Yin et al. 2016). Study 2
change in estimated coefficients equals 61.8%; that is,
provides consistent evidence that explanation-driven
explanations affect mental models. Explanation-driven
knowledge transfers from an AI to a human similarly suf-
effects decreased lay users’ decision-making perfor- fer from confirmation bias as knowledge transfers in the
mance in our setting. Compared with opaque predic- human-to-human domain. For example, confidence in
tions, explanations decreased participants investment prior conceptions and their difference from the new
performance by 8.9% while observing them and by 9.8% information moderate confirmation bias (Pyszczynski
even when not observing explanations anymore. Study and Greenberg 1987). Similar to learning from other
2 extended these results in three ways. First, we find humans, users seem unwilling to internalize potentially
that even expert users in a considerably more applied helpful, XAI-channeled machine knowledge if it is in-
domain adjusted mental models by about 25 percentage consistent with what they already, perhaps incorrectly,
points. Second, results indicate that asymmetric mental believe to be true. From the perspective of the Mental
model adjustments were a manifestation of the confirma- Models framework, individuals more frequently engage
tion bias because posterior beliefs resembled observed in maintaining rather than in building mental models of
explanations about 50% more closely if explanations con- the relationships between features and labels. One reason
firmed prior beliefs. Third, Study 2 reveals that mental for this effect could be the need to attain or maintain a
model adjustments created spillover effects leading to an high level of self-esteem (Klayman 1995), leading users
average absolute change in apartment price estimates for to focus inappropriately on explanations that make
a different market by approximately 20%. them feel competent. In other words, they may derive
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1597
a positive intrinsic benefit from being in the right from those estimated by experts who either had no deci-
(Gilad et al. 1987). From this perspective, people may sion aid or only observed opaque predictions. This spill-
misuse the XAI as a tool to enhance their self-esteem. If over effect seems to occur because of the adjustment of
left unaddressed, the asymmetric adaptation of mental mental models that experts draw on in both situations.
models by humans may prevent modern (X)AI appli- Therefore, as an unintended side effect, increasing public
cations from fulfilling their promise of making humans and private efforts to promote the use of XAI methods
smarter, which (ironically) may also hinder the further may extend the already significant influence of AI sys-
development of AI applications by humans. tems from areas where we interact with them (Rahwan
Interpreting our results in the light of the model by et al. 2019) to areas where such systems are not in use.
Agrawal et al. (2019) yields another theoretical insight Feature-based XAI methods’ potential to link different
regarding the ramifications of XAI. Our results indicate domains is particularly concerning given recent evidence
that users’ willingness to follow XAI predictions de- on their susceptibility to intentional manipulation and
pends on whether the explanations conform with their adversarial attacks (Lipton 2018). Many modern XAI
mental models. One way to rationalize this behavior is methods, including LIME and SHAP, optimize fidelity,
that their objective function includes a component that that is, ensure that explanations accurately mimic the pre-
accounts for experiencing some positive (negative) in- dictions of the black box model. However, even small
trinsic utility when obtaining a signal that their mental perturbations of the input data (e.g., deliberate manipula-
model may (not) be accurate (Festinger 1962, Gilad et al. tion and measurement errors) can lead to considerably
1987, Harmon-Jones 2019). In the model by Agrawal different explanations for identical predictions, that is,
et al. (2019), AI systems make predictions about uncer- depict different feature-label relations (Ghorbani et al.
tain states of the world that relate to the profitability of 2019, Lakkaraju and Bastani 2020). The potential instabil-
taking specific actions. Human users, in turn, assess the ity of explanations allows manipulating user behaviors.
expected payoffs associated with specific actions, that is, Following our results, the creation of misleading explana-
make judgments. Our results suggest that human judg- tions may not only affect users’ trust in the AI system
ment in this model encompasses not only the material (Lakkaraju and Bastani 2020) but also lead to an (asym-
consequences of an action but also the psychological metric) adjustment of mental models that affect users’
impact of receiving a signal that implicitly shows decision making beyond the XAI augmented decision at
whether current mental models are correct. If expla- hand. Specifically, the depiction of certain feature-label
nations reveal that the AI system arrived at a prediction relationships that are not present can evoke inappropri-
in a way that contradicts their held mental models, tak- ate mental model adjustments that, given the documen-
ing an action that follows this prediction effectively con- ted asymmetry, will cause users who already believe
stitutes a signal to oneself that the current mental model these patterns to be true, to feel vindicated and reinforce
is incorrect, creating psychological distress, for example, these beliefs. In general, the documented spillover effects
in the form of a cognitive dissonance (Harmon-Jones may magnify the reach and impact of intentional manip-
2019). This mental toll may lead users not to follow the ulations of explanations, increasing deceiving parties’
prediction in the first place. Conversely, users may fol- incentive to do so.
low unreliable predictions more often if the explanations
are consistent with their current mental models because 4.2. Implications
doing so provides a psychologically valuable self-signal Reported results have important practical implications
that they are in the right (Gilad et al. 1987). Against this for organizations and policymakers. Our finding that
background, users’ inclination to follow predictions of XAI can change human thinking points to potential pit-
an XAI system, and thus their ultimate decisions and falls for companies that want, or have to, use XAI. Con-
gains, is subject to greater variance than with a black-box sider a company that plans to implement XAI methods
AI. That is because users’ propensity to follow predic- to explain to its employees why an AI system makes
tions depends on the consistency of the explanations certain predictions. As Study 1 shows, providing exp-
with their mental models. lanations in addition to predictions may draw users’
Another theoretical contribution of our work is to attention excessively to the explanations, to the detri-
show the potential of feature-based XAI to link different ment of the prediction itself. Users may place too much
decision domains by influencing users’ beliefs about the emphasis on individual explanations that confirm their
feature-label relationship. Study 2 results show that prior beliefs, rather than adhering to the overall predic-
observing explanations for listing price predictions for tion. As a result, employees’ decision-making perfor-
apartments in Market A influenced the price estimation mance for the task at hand may deteriorate, which is in
of experts in a different Market B, where the learned pat- line with evidence from related research (Poursabzi-
tern does not exist, and they did not have access to XAI Sangdeh et al. 2021). In domains where explanations are
decision support. We find that listing prices estimated by becoming a regulatory standard, managers need to take
experts who observed explanations differed significantly such potential downsides into account and contemplate
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1598 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
the ramifications of implementing explainability mea- From a societal perspective, our results indicate that
sures. Following our results, managers who, in the broad, indiscriminate implementation of XAI methods
future, are obliged to put XAI methods in place, should may create unintended downstream ramifications. Our
not take these steps too lightly. From a business perspec- finding that XAI can lead users to adjust mental models
tive, our documented downsides of explainability could in a confirmatory way and carry over learned patterns
render the continued use of AI-based decision support to other domains may, in an extreme case, foster dis-
systems unattractive. Considering that AI systems are crimination and social divisions. Assume all recruiters
often deeply interwoven with business processes, this start to collaborate with an XAI system to support hiring
XAI-driven discontinuance may entail considerable orga- decisions. For example, a subgroup of recruiters may dis-
nizational change. As a result, managers may be well criminate against women because they believe female
advised to assess potential inconsistencies between the applicants to be less productive on the job. If the XAI
AI system’s internal logic and employees’ understanding (occasionally) provides local explanations that depict
of the task it supports before rolling out explainability being female as negative evidence for high future per-
measures. This puts managers in a position to evaluate formance, the subgroup that statistically discriminates
the magnitude of the potential downside of explainability based on gender will readily reinforce its prior belief,
and use countermeasures. For example, managers may that is, engage in mental model maintenance. As a
obviate confirmation bias by openly discussing explana- result, these recruiters may become more biased and
tions that conflict with employees’ mental models and less noisy in their behavior as they hire female appli-
showcasing arguments in support of the explanation. cants consistently less. Given the spillover effects we
Another pitfall for companies concerns the transfer of find, they may even carry over their strengthened con-
knowledge from AI systems to human users. As Study 2 ceptions about women’s productivity to other jobs, fur-
shows, even experts can overgeneralize learned feature- ther reinforcing discriminatory patterns. Additionally,
label relationships that are only applicable in the context because nondiscriminating recruiters will most likely
in which they interact with the system. With the confir- refrain from adjusting their mental model, that is, not
matory learning from explanations, existing differences engage in mental model building, social divisions among
in employees’ initial conceptions may lead to differ- recruiters may develop and accumulate along the lines of
ences in how they collaborate with and what they learn gender biases. Hence, without any malicious intent, the
from the XAI, for example, fostering the biased weight- broad use of XAI may ironically foster human discrimi-
ing of certain information. From this perspective, pro- natory tendencies and divide social groups. Notably,
viding explanations might decrease individual level with the possibility to manipulate explanations, deceiv-
noise in the decision-making process (Kahneman et al. ing third parties could also intentionally cause explana-
2021) because individuals’ decisions become more con- tions to exhibit specific prediction contributions for
sistent. This is in line with Fu¨gener et al. (2021b), who sensitive attributes such as race, gender, or age. This
find decisions to be increasingly consistent among users effect could lead human users who already hold preju-
engaging with opaque predictions. On a more aggregate dices, stereotypes, or discriminatory tendencies to rein-
level, however, our results suggest that explained pre- force their views, which could promote certain political
dictions may additionally foster differences in the agendas.
decision-making process across subgroups of users
that possess heterogeneous priors. As a consequence, 4.3. Limitations and Future Research
the variation of decisions on a group level can grow. As with any other research study, ours is not without
As pointed out by Kahneman et al. (2021), variation in limitations. In light of increasing regulatory require-
decisions can substantially contribute to errors and ments and private initiatives, we believe that these lim-
ultimately harm business performance. Consider our itations open up fruitful avenues for future research.
previous example of loan officers. XAI may cause loan One limitation of our work concerns the lack of feed-
approval decisions to increasingly depend on the par- back on the decision outcomes and thus the perfor-
ticular employee, with idiosyncratic mental models, mance of the AI system. In both our studies, we did not
assessing the applicant’s creditworthiness. This in- provide feedback for two reasons. First, it adds a consid-
crease in loan approval variation may create consider- erable layer of complexity that impedes the measure-
able business, legal, and reputational risks. Against ment and interpretation of isolated explanation-driven
this background, managers should closely monitor the effects on users’ cognitive processes. Second, in practice,
introduction of XAI to identify a possible increase in many AI-supported decisions do not yield immediate
decision variance. For instance, managers could com- feedback, or only yield feedback for some of the predic-
plement XAI with “noise audits” and the development tions. Hence, users have to interact with the system
of “reasoned rules” (as proposed by Kahneman et al. without learning its prediction accuracy, at least for a
2021) to overcome the hidden costs of XAI-driven certain period. Examples include hiring decisions sup-
increases in inconsistent decision making. ported by an on-the-job performance predicting AI
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1599
system, investment decisions supported by a return Additionally, the global representation may facilitate
predicting AI system, and drug treatment decisions comparison and reflection processes that ultimately
supported by an effectiveness predicting AI system. Con- improves the transfer of knowledge from the AI sys-
sequently, explanations may alter users’ situational infor- tem to the user.
mation processing and mental models before feedback
on system performance arrives. Nonetheless, we strongly 4.4. Conclusion
encourage future research to examine the role of feed- A concluding remark is worth making. Of course, our
back as it may introduce unexpected dynamics in the work is not meant to be an argument, let alone a plea,
cognitive effects we document. For instance, the (selec- against making “black box” AI systems more explain-
tive) reinforcement of their mental models through exp- able or transparent. Instead, we comprehend our find-
lanations, may lead users to be more forgiving and ings as a warning that the indiscriminate use of modern
maintain trust in the AI system, even if they eventually XAI methods as an isolated measure may lead to unin-
see it making mistakes. In this way, the interaction tended, unforeseen problems because it creates a new
between feedback and explanations might constitute a channel through which AI systems can affect human
factor contributing to unwarranted algorithm apprecia- behaviors across domains. The pervasive human incli-
tion (Logg et al. 2019), leading users to rely on incorrect nation to process information in a way that confirms
outcomes blindly. Additionally, people’s adjustments of their preconceptions while ignoring potentially helpful
the situational information processing and existing men- yet conflicting information needs addressing if exp-
tal models possibly depend on the extent to which the lainability is to become an effective means to combat
XAI system’s predictions outperform their own. If users accountability, transparency, and fairness issues with-
learn that an XAI system’s predictions perform consider- out creating adverse second-order effects. For instance,
ably better than their subjective ones, the magnitude of one might restrict the provision of explanations of sen-
reported confirmation biases may vary. Conversely, sitive features for end users of the system and only use
when users’ predictions are better than the XAI, their them to ensure the proper and unbiased functioning of
confirmation bias might be even stronger. Future re- the AI system during the development process. Addi-
search could examine to what extent our reported tionally, it might be important to provide developers
effects, at the intensive margin, depend on users’ per- and data scientists with cognitive awareness trainings
ceptions about differences in their own and the XAI to make them more sensitive to their own biased men-
system’s predictive performance. tal processes.
Another limitation of our work originates from letting
participants interact with local, feature-based XAI meth- Endnotes
ods. We opted to use these explanations because they
1For anecdotal evidence of such nontraditional data use, see Lend
are already widely in use in practice and because there
doEFL.com or https://money.cnn.com/2016/08/24/technology/
are arguments that feature-based explanations on an lenddo-smartphone-battery-loan/index.html.
individual level are necessary to comply with (upcom- 2On a high level, both decisions effectively constitute sequential
ing) regulatory requirements (Goodman and Flaxman economic transactions under uncertainty that strongly depend on
2017). Yet, there exist other forms of explanations, for trust.
example, global feature-based explanations or even 3Explainability may enter the model of Agrawal et al. by changing
example-based explanations. Although an investiga- the prediction reliability. Following Proposition 2, the necessity for
providing explanations decreases with the users’ judgment. How-
tion and comparison of the interplay between different
ever, the model does not consider the idea presented in our paper
forms of explanations and cognitive processes are
that explainability may also affect users’ understanding of the pro-
beyond the scope of this paper, it is worthwhile for cess that determines the uncertain state of the world the AI tries to
future research to explore whether, and if so why, the predict. One could integrate this notion into the framework by
effects we document would change if users (addition- modeling that explanations affect users’ judgment capabilities by
influencing beliefs about underlying processes. Extending the
ally) obtain other forms of explanations. Consider, for
model of Agrawal et al. in this direction may be a fruitful endeavor
instance, global explanations. Although local explana-
to better understand whether explainability modulates the relation-
tions help understand why an AI system produces a ship between prediction and judgment. However, an extension of
prediction on a case-by-case basis, global explanations the formal model is beyond the scope of this paper and left for
reveal important high-level patterns and nonlinearities future research.
in the system’s logic. Such global explanations effec- 4See the online appendix for details on the experimental proce-
tively aggregate individual-level information for the dures including payments, instructions, and screenshots.
user and help to understand the system’s overall logic. 5When a risk-neutral, purely self-interested investor expects that the
By taking over this information aggregation task, global borrower repays her with a probability of p >0.5, for example, because
she believes the borrower to possess altruistic, efficiency, or fairness
explainability could mitigate concerns about the selec-
preferences, they have a strict incentive to invest because they maxi-
tive processing of isolated local explanations that argu-
mize their expected earnings. Importantly, holding such expectations
ably contribute to the occurrence of confirmation bias. about the borrower’s preferences is justified and frequently observed
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1600 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
in sequential games: A considerable share of people does respond (+64.3%). As a result, participants could have benefited from relying
reciprocally in sequential exchanges if they are trusted (see Miettinen on the predictions, which baseline participants did at least partially.
et al. 2020for an overview). 15Across Stages I and II, baseline participants’ access to the AI system
6To reduce the complexity for the reader, we only report the three significantly increased the accuracy by 4.6% (p <0.01, F test), whereas
main stages of the experiment. Right before and after Stage II, we the recall effectively remained constant (p <0.82, F test). XAI partici-
additionally measured participants’ prior and posterior preferences pants performance significantly decreased regarding both the accuracy
to observe three borrower characteristics. We use these measures as (�5.3%; p <0.01, F test) and recall score (�14.6%; p <0.01, F test).
robustness and consistency checks. We provide a detailed descrip- 16A purely linear distinction between most competitive and other
tion of these measurements in the online appendix. borrowers does not allow to draw conclusions about their repay-
7The questionnaire items included in the field study were selected ment likelihood: they, respectively, made a repayment in 77.4% and
partly for exploratory reasons and partly motivated by previous 79.8% of the cases (p �0.85, F test).
research documenting their association with individuals’ repayment 17We scraped data from a large online platform in February 2022.
behavior in investment games (Ben-Ner and Halldorsson 2010). We collected observations for all apartments listed for sale in the
8For most traits, values and LIME values are almost perfectly corre- seven major cities of Germany (“A-Cities”) and a medium-sized
lated producing severe problems of multicollinearity (see Table 7 in eastern German city (Chemnitz). We constructed a data set consist-
the online appendix). Therefore, in our regression analyses, we only ing of eight apartment attributes and the listing price directly
include LIME explanations for which there exists a tolerable correla- obtained from the platform and two additionally collected features
tion between the trait and LIME values: Openness, Agreeableness, from public statistics. We provide summary statistics in the online
and Conscientiousness. appendix (Table 6).
9See Table 8 in the online appendix. 18We selected these three characteristics for technical reasons regard-
10These results do not allow us to isolate how explanations affect ing the ML model and based on the input from our industry partner.
The notion is that these characteristics together are (i) sufficiently rele-
what investors consider to be a borrower’s motivation to repay
vant to the prediction and (ii) familiar/accessible to experts.
them or not. The change in the weighting of competitiveness could
stem from a reinforced perception that competitiveness predicts a 19The AI system is a random forest that achieves a performance of
low repayment likelihood because it proxies for antisocial, income- R2�0:72 on unseen test data. See the online appendix for additional
maximizing, or relative income-maximizing motives. Although we information.
cannot isolate investors’ latent belief(s) about borrowers’ motives, 20For instance, A-cities exhibit considerably higher average wages,
our results effectively show that the provision of explanations does more liberal political attitudes, and faster population growth (Cajias
entail a change in at least one of these perceived latent motives, that et al. 2020).
is, that XAI can change the processing of information. A similar 21The positive coefficient for β may be related to the fact that
argument applies regarding mental model adjustments outlined 5
SHAP values and overall predictions are inextricably linked. Merely
later.
observing high (low) predictions may lead to adjustments of
11Reported results are robust to excluding participants who always reported beliefs upward (downward), creating a positive, however,
or never invested in our analyses, respectively, alleviating concerns insignificant correlation with underlying SHAP values in the data.
that our results are driven by pure altruists or players who always 22Participants, on average, have worked in the real estate industry
choose the game-theoretically dominant strategy (see the subsection
for 13.8 years and, on a scale from 1 to 10, report that their experi-
on additional robustness checks in the online appendix). Instead,
ence level in rating apartment listing prices is 5.7.
our results stem from those participants whose behavior suggests
23Our main insights are robust to defining more restrictively that
that they try to invest with borrowers whom they believe will make
explanations confirm priors if the absolute distance between the
a repayment, that is, individuals who, from a conceptual point of
prior and the observed average SHAP value is smaller than the
view, should be most inclined to learn to recognize repaying bor-
absolute distance between the prior and 0e and, at the same time,
rowers. Results 1.2 and 1.3 are equally robust to excluding these
smaller than the absolute distance between the prior and the closest
“extreme” types, warranting a similar interpretation.
extreme, that is, 62,500e (see Table 25 in the online appendix).
12The significant explanation effect for Openness and Extraversion
24We did not include Chemnitz observations in the data to train
may be a consequence of participants’ significantly stronger weight-
the AI model. We conducted several analyses showing that the
ing of borrowers’ Competitiveness and Patience and a limited capacity
most important predictors for listing prices in Frankfurt and
to process information. Specifically, XAI participants in Stage III
Cologne (cities in Stages I to III) differ considerably from listing
place similarly low weight on all borrower traits but Competitiveness,
price predictors in Chemnitz. Real estate experts are arguably aware
Agreeableness, and Patience. This pattern may suggest that partici-
of the structural differences in apartment markets.
pants heuristically focus on the three characteristics that they them-
selves and the AI system deemed most relevant to the decision. As
a result, they place less weight on all other traits, which for Open-
References
ness led to a statistically significant effect.
Abdel-Karim BM, Pfeuffer N, Carl V, Hinz O (2022) How AI-based
13We show ROC curves in Figures 17 to 19 in the online appendix.
systems can induce reflections: The case of AI-augmented diag-
14Participants neither knew their own nor the AI system’s perfor- nostic work. Management Inform. Systems Quart. Forthcoming.
mance because we did not provide intermediate feedback. There- Abdel-Karim BM, Pfeuffer N, Rohde G, Hinz O (2020) How and
fore, they could not see how much better or worse the system what can humans learn from being in the loop? German J. Artifi-
performs compared with themselves. Although unknown to partici- cial Intelligence 34(2):199–207.
pants, predictions are accurate in about 69.3% of the cases. This per- Agarwal R, Dhar V (2014) Big data, data science, and analytics: The
formance holds equally for both repaying (69.7%) and nonrepaying opportunity and challenge for IS research. Inform. Systems Res.
borrowers (67.7%). Participants in Stage I correctly invested with (non- 25(3):443–448.
)repaying borrowers in 66.1% (41.2%) of the cases and overall in 60.5% Agrawal A, Gans JS, Goldfarb A (2019) Exploring the impact of arti-
of the cases. Put differently, the AI system outperforms them overall ficial intelligence: Prediction vs. judgment. Inform. Econom. Pol-
(+14.5%) and especially for the identification of nonrepaying ones icy 47:1–6.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s) 1601
Alavi M, Marakas GM, Yoo Y (2002) A comparative study of dis- EU (2021) Proposal for a regulation EU of the European Parliament
tributed learning environments on learning outcomes. Inform. and of the Council of April 21, 2021, laying down harmonised
Systems Res. 13(4):404–415. rules on artificial intelligence (Artificial Intelligence Act) and
Ban GY, El Karoui N, Lim AE (2018) Machine learning and portfolio amending certain Union legislative acts. Official J. Eur. Union
optimization. Management Sci. 64(3):1136–1154. Law 119. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
Bauer K, Hinz O, van der Aalst W, Weinhardt C (2021) Expl(AI)n it celex%3A52021PC0206.
to me: Explainable AI and information systems research. Bus. Festinger L (1962) Cognitive dissonance. Sci. Amer. 207(4):93–106.
Inform. Systems Engrg. 63(2):79–82. Fu¨gener A, Grahl J, Gupta A, Ketter W (2021a) Cognitive challenges
Ben-Ner A, Halldorsson F (2010) Trusting and trustworthiness: in human–artificial intelligence collaboration: Investigating the path
What are they, how to measure them, and what affects them. J. toward productive delegation. Inform. Systems Res. 33(2): 678–696.
Econom. Psych. 31(1):64–79. Fu¨gener A, Grahl J, Gupta A, Ketter W (2021b) Will humans-in-the-
Berente N, Gu B, Recker J, Santhanam R (2021) Managing artificial loop become borgs? Merits and pitfalls of working with AI. Man-
intelligence. Management Inform. Systems Quart. 45(3):1433–1450. agement Inform. Systems Quart. 45(3b):1527–1556.
Berg J, Dickhaut J, McCabe K (1995) Trust, reciprocity, and social Garreau D, Luxburg U (2020) Explaining the explainer: A first theo-
history. Games Econom. Behav. 10(1):122–142. retical analysis of LIME. Proc. Internat. Conf. on Artificial Intelli-
Bhatt U, Xiang A, Sharma S, Weller A, Taly A, Jia Y, Ghosh J, et al. gence and Statist.
(2020) Explainable machine learning in deployment. Proc. Conf. Ge R, Zheng Z, Tian X, Liao L (2021) Human–robot interaction:
on Fairness, Accountability, and Transparency (Association for When investors adjust the usage of robo-advisors in peer-to-peer
Computing Machinery, New York). lending. Inform. Systems Res. 32(3):774–785.
Brewer WF (1987) Schemas vs. mental models in human memory. Ghorbani A, Abid A, Zou J (2019) Interpretation of neural networks
Morris P, ed. Modelling Cognition (John Wiley & Sons, Oxford, is fragile. Proc. AAAI Conf. on Artificial Intelligence. 33(1):
UK), 187–197. 3681–3688.
Bussone A, Stumpf S, O’Sullivan D (2015) The role of explanations Gilad B, Kaish S, Loeb PD (1987) Cognitive dissonance and utility maxi-
on trust and reliance in clinical decision support systems. Proc. mization: A general framework. J. Econom. Behav. Organ. 8(1):61–73.
Internat. Conf. on Healthcare Informatics (Institute of Electrical Goldstein IM, Lawrence J, Miner AS (2017) Human-machine collab-
and Electronics Engineers (IEEE), New York). oration in cancer and beyond: The centaur care model. JAMA
Cabral TS (2021) AI and the right to explanation: Three legal bases Oncology 3(10):1303–1304.
under the GDPR. Data Protection Artificial Intelligence 13:29–56. Goodman B, Flaxman S (2017) European Union regulations on algo-
Cajias M, Freudenreich P, Freudenreich A, Scha¨fers W (2020) rithmic decision-making and a “right to explanation”. AI Maga-
Liquidity and prices: A cluster analysis of the German residen- zine 38(3):50–57.
tial real estate market. J. Bus. Econom. 90(7):1021–1056. Google AI (2019) Responsible AI practices: Interpretability. Accessed
Case N (2018) How to become a centaur. J. Design Sci. https://jods. March 8, 2022, https://ai.google/responsibilities/responsible-ai-
mitpress.mit.edu/pub/issue3-case/release/6?version=53b19e72- practices/?category=interpretability.
d43a-4eda-8c48-6ed3cdc03218. Gramegna A, Giudici P (2021) SHAP and LIME: An evaluation of
Castelo N, Bos MW, Lehmann DR (2019) Task-dependent algorithm discriminative power in credit risk. Frontiers Artificial Intelligence
aversion. J. Marketing Res. 56(5):809–825. 4:752558.
Chatterjee S, Sarker S, Valacich JS (2015) The behavioral roots of Gregor S (2006) The nature of theory in information systems. Man-
information systems security: Exploring key factors related to agement Inform. Systems Quart. 30(3):611–642.
unethical IT use. J. Management Inform. Systems 31(4):49–87. Gregor S, Benbasat I (1999) Explanations from intelligent systems:
DeGroot MH (1974) Reaching a consensus. J. Amer. Statist. Assoc. Theoretical foundations and implications for practice. Manage-
69(345):118–121. ment Inform. Systems Quart. 23(4):497–530.
Dellermann D, Ebel P, So¨llner M, Leimeister JM (2019) Hybrid intel- Gunning D, Stefik M, Choi J, Miller T, Stumpf S, Yang GZ (2019)
ligence. Bus. Inform. Systems Engrg. 61(5):637–643. XAI—explainable artificial intelligence. Sci. Robot 4(37):eaay7120.
Dhaliwal JS, Benbasat I (1996) The use and effects of knowledge- Harmon-Jones EE (2019) Cognitive Dissonance: Reexamining a Pivotal
based system explanations: Theoretical foundations and a frame- Theory in Psychology (American Psychological Association).
work for empirical evaluation. Inform. Systems Res. 7(3):342–362. Hemmer P, Schemmer M, Vo¨ssing M, Ku¨hl N (2021) Human-AI
Dietvorst BJ, Simmons JP, Massey C (2015) Algorithm aversion: Peo- complementarity in hybrid intelligence systems: A structured
ple erroneously avoid algorithms after seeing them err. J. Exper- literature review. Proc. 28th Pacific Asia Conf. on Inform. Systems.
iment. Psych. General 144(1):114–126. Hoffman M, Kahn LB, Li D (2018) Discretion in hiring. Quart. J.
Dietvorst BJ, Simmons JP, Massey C (2018) Overcoming algorithm Econom. 133(2):765–800.
aversion: People will use imperfect algorithms if they can (even Holt CA, Smith AM (2009) An update on Bayesian updating. J.
slightly) modify them. Management Sci. 64(3):1155–1170. Econom. Behav. Organ. 69(2):125–134.
Dijkstra JJ (1999) User agreement with incorrect expert system Ji-Ye Mao IB (2000) The use of explanations in knowledge-based
advice. Behav. Informs. Tech. 18(6):399–411. systems: Cognitive perspectives and a process-tracing analysis.
Dodge J, Liao QV, Zhang Y, Bellamy RK, Dugan C (2019) Explaining J. Management Inform. Systems 17(2):153–179.
models: An empirical study of how explanations impact fairness Johnson-Laird PN, Goodwin GP, Khemlani SS (2017) Mental models
judgment. Proc. Internat. Conf. on Intelligent User Interfaces. and reasoning. The Routledge International Handbook of Thinking
Doshi-Velez F, Kim B (2017) Toward a rigorous science of interpret- and Reasoning (Routledge, Abingdon-on-Thames, UK), 346–365.
able machine learning. Preprint, submitted March 2, https:// Jones NA, Ross H, Lynam T, Perez P, Leitch A (2011) Mental mod-
arxiv.org/abs/1702.08608. els: An interdisciplinary synthesis of theory and methods. Eco-
Erlei A, Nekdem F, Meub L, Anand A, Gadiraju U (2020) Impact of logical Soc. 16(1). https://www.jstor.org/stable/26268859#metadata_
algorithmic decision making on human behavior: Evidence info_tab_contents.
from ultimatum bargaining. Proc. AAAI Conf. on Human Com- Jussupow E, Benbasat I, Heinzl A (2020) Why are we averse toward
put. and Crowdsourcing. algorithms? A comprehensive literature review on algorithm
EU (2016) Regulation EU 2016/679 of the European Parliament and aversion. Proc. Eur. Conf. on Inform. Systems.
of the Council of 27 April 2016, article 22. Official J. Eur. Union Jussupow E, Spohrer K, Heinzl A, Gawlitza J (2021) Augmenting
Law 119:59. medical diagnosis decisions? An investigation into physicians’
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD

Bauer, von Zahn, and Hinz: Explainable AI and Users' Information Processing
1602 Information Systems Research, 2023, vol. 34, no. 4, pp. 1582–1602, © 2023 The Author(s)
decision-making process with artificial intelligence. Inform. Sys- Rader E, Cotter K, Cho J (2018) Explanations as mechanisms for
tems Res. 32(3):713–735. supporting algorithmic transparency. Proc. CHI Conf. on Human
Kahneman D, Sibony O, Sunstein CR (2021) Noise: A Flaw in Human Factors in Comput. Systems.
Judgment (Little, Brown). Rahwan I, Cebrian M, Obradovich N, Bongard J, Bonnefon JF, Brea-
Kaur H, Nori H, Jenkins S, Caruana R, Wallach H, Wortman zeal C, Crandall JW, et al. (2019) Machine behaviour. Nature
Vaughan J (2020) Interpreting interpretability: Understanding 568(7753):477–486.
data scientists’ use of interpretability tools for machine learn- Ribeiro MT, Singh S, Guestrin C (2016) “Why should I trust you?”
ing. Proc. CHI Conf. on Human Factors in Comput. Systems. Explaining the predictions of any classifier. Proc. ACM SIGKDD
Klayman J (1995) Varieties of confirmation bias. Psych. Learning Internat. Conf. on Knowledge Discovery and Data Mining.
Motives 32:385–418. Rico-Juan JR, de La Paz PT (2021) Machine learning with explain-
Kleinmuntz B (1990) Why we still use our heads instead of formu- ability or spatial hedonics tools? An analysis of the asking
las: Toward an integrative approach. Psych. Bull. 107(3):296. prices in the housing market in Alicante, Spain. Expert Systems
Knobloch-Westerwick S, Meng J (2009) Looking the other way: Appl. 171:114590.
Selective exposure to attitude-consistent and counterattitudinal Rosenfeld A, Richardson A (2019) Explainability in human–agent
political information. Comm. Res. 36(3):426–448. systems. Autonomic Agent Multi Agent Systems 33(6):673–705.
Koh PW, Liang P (2017) Understanding black-box predictions via Rouse WB, Morris NM (1986) On looking into the black box: Pro-
influence functions. Proc. Internat. Conf. on Machine Learn. spects and limits in the search for mental models. Psych. Bull.
Lakkaraju H, Bastani O (2020) “How do I fool you?” Manipulating 100(3):349.
user trust via misleading black box explanations. Proc. AAAI/ Schanke S, Burtch G, Ray G (2021) Estimating the impact of
ACM Conf. on AI, Ethics, and Society. “humanizing” customer service chatbots. Inform. Systems Res.
Lakkaraju H, Kamar E, Caruana R, Leskovec J (2019) Faithful and cus- 32(3):736–751.
tomizable explanations of black box models. Proc. AAAI/ACM Scho¨n DA (2017) The Reflective Practitioner: How Professionals Think in
Conf. on AI, Ethics, and Society. Action (Routledge, Abingdon-on-Thames, UK).
Lim KH, Ward LM, Benbasat I (1997) An empirical study of com- Senoner J, Netland T, Feuerriegel S (2021) Using explainable artifi-
puter system learning: Comparison of co-discovery and self- cial intelligence to improve process quality: Evidence from
discovery methods. Inform. Systems Res. 8(3):254–272. semiconductor manufacturing. Management Sci. 68(8):5704–5723.
Lipton ZC (2018) The mythos of model interpretability: In machine Shapley LS (1953) A value for n-person games. Contributions to the
learning, the concept of interpretability is both important and Theory of Games (AM-28), vol. II (Princeton University Press,
slippery. Queue 16(3):31–57. Princeton, NJ).
Logg JM, Minson JA, Moore DA (2019) Algorithm appreciation: Teodorescu MH, Morse L, Awwad Y, Kane GC (2021) Failures of
People prefer algorithmic to human judgment. Organ. Behav. fairness in automation require a deeper understanding of human-
Human Decision Processes 151:90–103. ML augmentation. Management Inform. Systems Quart. 45(3b):
Lu Z, Yin M (2021) Human reliance on machine learning models 1483–1499.
when performance feedback is limited: Heuristics and risks. Tschandl P, Rinner C, Apalla Z, Argenziano G, Codella N, Halpern
Proc. CHI Conf. on Human Factors in Comput. Systems. A, Janda M, et al. (2020) Human–computer collaboration for
Lundberg SM, Lee SI (2017) A unified approach to interpreting model skin cancer recognition. Nature Medicine 26(8):1229–1234.
predictions. Proc. Conf. on Neural Inform. Processing Systems. van den Broek E, Sergeeva A, Huysman M (2021) When the
Malle BF (2006) How the Mind Explains Behavior: Folk Explanations, machine meets the expert: An ethnography of developing
Meaning, and Social Interaction (MIT Press, Cambridge, MA). AI for hiring. Management Inform. Systems Quart. 45(3):
Meske C, Bunde E, Schneider J, Gersch M (2022) Explainable artifi- 1557–1580.
cial intelligence: Objectives, stakeholders, and future research Vandenbosch B, Higgins C (1996) Information acquisition and men-
opportunities. Inform. Systems Management 39(1):53–63. tal models: An investigation into the relationship between
Meta AI (2021) Facebook’s five pillars of responsible AI. Accessed behaviour and learning. Inform. Systems Res. 7(2):198–214.
March 8, 2022, https://ai.facebook.com/blog/facebooks-five- Vilone G, Longo L (2021) Notions of explainability and evaluation
pillars-of-responsible-ai/. approaches for explainable artificial intelligence. Inform. Fusion
Miettinen T, Kosfeld M, Fehr E, Weibull J (2020) Revealed prefer- 76:89–106.
ences in a sequential prisoners’ dilemma: A horse-race between Wang W, Benbasat I (2007) Recommendation agents for electronic
six utility functions. J. Econom. Behav. Organ. 173:1–25. commerce: Effects of explanation facilities on trusting beliefs. J.
Molnar C (2020) Interpretable Machine Learning: A Guide for Making Management Inform. Systems 23(4):217–246.
Black Box Models Explainable. Accessed January 14, 2022, https:// Willison R, Warkentin M (2013) Beyond deterrence: An expanded
christophm.github.io/interpretable-ml-book. view of employee computer abuse. Management Inform. Systems
Poursabzi-Sangdeh F, Goldstein DG, Hofman JM, Wortman Vaughan Quart. 37(1):1–20.
JW, Wallach H (2021) Manipulating and measuring model inter- Yang F, Huang Z, Scholtz J, Arendt DL (2020) How do visual expla-
pretability. Proc. CHI Conf. on Human Factors in Comput. Systems. nations foster end users’ appropriate trust in machine learning?
Pyszczynski T, Greenberg J (1987) Toward an integration of cognitive Proc. Internat. Conf. on Intelligent User Interfaces.
and motivational perspectives on social inference: A biased Yin D, Mitra S, Zhang H (2016) Research note—When do consumers
hypothesis-testing model. Adv. Experiment. Soc. Psych. 20:297–340. value positive vs. negative reviews? An empirical investigation
Rabin M, Schrag JL (1999) First impressions matter: A model of con- of confirmation bias in online word of mouth. Inform. Systems
firmatory bias. Quart. J. Econom. 114(1):37–82. Res. 27(1):131–144.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
03:32
ta
,6202
yluJ
60
no
]05.91.94.72[
yb
gro.smrofni
morf
dedaolnwoD