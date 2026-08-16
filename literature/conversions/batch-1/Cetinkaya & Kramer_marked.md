---
conversion_metadata:
  converted_at: "2026-07-22T12:43:38Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cetinkaya & Kramer.pdf"
  source_pdf_sha256: "891d630b19877efd02f2ba4ae29c144ee2b0cd7f8a1fe57dd3494c59e011f5b5"
  page_count: 16
  markdown_char_count: 167873
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Behaviour & Information Technology

ISSN: 0144-929X (Print) 1362-3001 (Online) Journal homepage: www.tandfonline.com/journals/tbit20

Between transparency and trust: identifying key
factors in AI system perception

Nur Efsan Cetinkaya & Nicole Krämer

To cite this article: Nur Efsan Cetinkaya & Nicole Krämer (2026) Between transparency and
trust: identifying key factors in AI system perception, Behaviour & Information Technology,
45:5, 840-854, DOI: 10.1080/0144929X.2025.2533358

To link to this article:  https://doi.org/10.1080/0144929X.2025.2533358

© 2025 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group

Published online: 20 Jul 2025.

Submit your article to this journal

Article views: 7271

View related articles

View Crossmark data

Citing articles: 11 View citing articles

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tbit20

---

<!-- PAGE 2 -->

BEHAVIOUR  &  INFORMATION  TECHNOLOGY 
2026,  VOL.  45,  NO.  5,  840–854 
https://doi.org/10.1080/0144929X.2025.2533358

Between transparency and trust: identifying key factors in AI system perception
Nur Efsan Cetinkayaa,b and  Nicole Krämera,b

aSocial Psychology: Media and Communication, University of Duisburg-Essen, Duisburg, Germany; bResearch Center Trustworthy Data Science 
and  Security,  Dortmund,  Germany

ABSTRACT
With  the  deployment  of  AI  systems  across  multiple  domains,  understanding  how  users  develop 
trust  has  becomecrucial  for  successful  implementation.  This  study  investigates  how  different  AI 
features  influence  the  decision  to  use  an  AI  system  and  which  characteristics  users  prioritise 
when  evaluating  them.  We  focus  on  whether  users  prefer  systems  whose  functioning  they  can 
understand  or  whose  trustworthiness  is  certified.  We  examined  whether  users  favour  system 
transparency  through  explainability  features  or  rely  more  on  external  trust  signals,  such  as  AI 
certification seals, while considering how these preferences interact with technical reliability and 
fairness. Using conjoint analysis, we systematically compared the influence of four key attributes 
(transparency  by  explainability  features,  technical  reliability,  external  trust  signals  through  AI 
certifications,  and  fairness)  on  user  decisions  to  use  an  AI  system.  Through  cluster  analysis,  we 
identified  two  groups  with  opposing  preferences  and  demographic  differences.  The  first  group 
prioritised  high  explainability  and  strong  AI  certification  while  showing  negative  preferences  for 
fairness,  whereas  the  second  group  favoured  fairness  and  reliability  while  displaying  negative 
attitudes toward explainability and  AI  certification. These contrasting prioritisation  patterns raise 
important  questions  about  AI  systems  development,  particularly  regarding  challenges  of 
addressing competing user requirements for trust-related features.

ARTICLE  HISTORY
Received  25  April  2025 
Accepted  7  July  2025

KEYWORDS
Artificial  intelligence;  XAI; 
trust in AI; reliability; fairness

1 Introduction

The use of artificial intelligence (AI) has grown rapidly 
in  recent  years,  fundamentally  transforming  various 
aspects  of  society.  As  AI  becomes  more  deeply  inte-
grated into daily life, understanding how users evaluate 
and  choose  to  adopt  AI  systems  becomes  increasingly 
critical.  Research  has  extensively  investigated  various 
attributes that influence AI adoption and trust, examin-
ing  factors  such  as  system  explainability  (Wing  2021), 
reliability (Ryan 2020), and fairness (Varona and Suárez 
2022).  While  these  individual  studies  have  provided 
valuable  insights,  they  predominantly  examine  each 
attribute in isolation, leaving a critical gap in our under-
standing of how these attributes interact and compare in 
importance when users make actual adoption decisions.
This gap is particularly significant as users in practice 
must evaluate multiple attributes simultaneously, not in 
isolation. When deciding whether to adopt an AI system 
in high-stakes scenarios, users cannot consider explain-
ability without also weighing factors like reliability and 
fairness. Moreover, with the emergence of trust signals 
such  as  AI  certification  seals  (Scharowski  et  al.  2023),

users  now  have  additional  external  indicators  to  con-
sider alongside system attributes. This creates a complex 
decision environment where understanding the relative 
importance  of  each  attribute  becomes  crucial  for  both 
theory and practice.

The relationship between understanding and trust in 
AI  systems  presents  a  fundamental  tension  in  user 
adoption decisions.  While  some  researchers argue  that 
understanding  AI  systems  through  explainability  leads 
to increased user (Shin 2021; Weitz et al. 2019), others 
suggest that  external trust  mechanisms may  be equally 
or more important (Krämer, Wischnewski, and Müller 
2023). The latter assumption is based on the observation 
that users might show unwillingness (Ngo and Krämer 
2021) or inability (Bromme and Gierth 2021) to under-
stand complex functioning and issues. This leads to the 
important question whether users prefer to understand 
AI systems directly, or whether they are willing to rely 
more heavily on external validations of trustworthiness.
Research  has  identified  several  key  attributes  that 
influence  AI  adoption.  Explainability  enables  users  to 
understand  system  decisions  (Sheth  et  al.  2021),  while

nur.cetinkaya@uni-due.de

CONTACT  Nur Efsan Cetinkaya 
120,  47057  Duisburg,  Germany
©  2025  The Author(s).  Published  by Informa  UK  Limited,  trading  as  Taylor  & Francis  Group 
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, 
distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this article has been published allow the posting of the Accepted 
Manuscript  in  a  repository  by  the  author(s)  or  with  their  consent.

Social Psychology: Media and Communication, University of Duisburg-Essen, Bismarckstraße

---

<!-- PAGE 3 -->

reliability ensures consistent performance under specific 
conditions  (Hong  et  al.  2022).  External  trust  signals, 
such as AI seals of approval, offer third-party validation 
of  system  quality  (Scharowski  et  al.  2023),  particularly 
valuable  for  non-expert  users  (LaRose  and  Rifon 
2006).  Fairness,  defined  as  the  equitable  treatment  of 
diverse  user  groups,  has  emerged  as  another  critical 
consideration as AI systems increasingly make decisions 
that affect different populations. The growing awareness 
of algorithmic bias and its potential societal impacts has 
made fairness a key factor in users’ evaluation of AI sys-
tems  (Bartneck  et  al.  2021).  Each  of  these  attributes 
potentially influences users’ willingness to adopt AI sys-
tems, yet their relative importance remains unclear.

To address these questions, our study employs con-
joint analysis  to examine how users weigh different AI 
system  attributes  when  making  adoption  decisions  in 
high-stakes scenarios. This methodological approach is 
particularly  well-suited  for  our  research  as  it  requires 
participants to make realistic trade-offs between differ-
ent  system  attributes,  revealing  their  true  preferences 
more  accurately  than  direct  questioning.  While  our 
study  does  not  directly  measure  trust,  it  operates  on 
the  premise  that  user  preferences  for  these  attributes 
indicate what users value most when deciding whether 
to adopt an AI system.

Our  research  focuses  particularly  on  the  interplay 
between understanding and trust, whether users prefer 
to understand AI systems directly through explainabil-
ity,  or  whether  they  rely  more  heavily  on  external 
trust  signals  such  as  certifications.  By  examining  these 
factors alongside reliability and fairness, we aim to pro-
vide  insights  that  can  guide  both  theoretical  develop-
ment  and  practical  implementation  of  AI  systems.  For 
organisations  developing  AI  systems  for  critical  appli-
cations,  understanding  which  attributes  most  strongly 
influence user acceptance can guide resource allocation 
and  development  priorities.  For  researchers,  insights 
into how these attributes interact can inform more com-
prehensive models of AI adoption and trust.

2 Theoretical  background

Given  the  increasing  use  of  artificial  intelligence  (AI) 
systems in decision-making processes, there is a  grow-
ing  need  to  understand  how  users  develop  trust  in 
these systems as well as what is affecting their adoption 
decision.

2.1  Trust  development  in  AI  systems

Trust  and  trustworthiness  represent  fundamental  yet 
distinct concepts in the context of artificial intelligence

BEHAVIOUR & INFORMATION TECHNOLOGY

841

adoption.  While  trust  encompasses  users’  subjective 
perceptions  of  a  system’s  reliability,  trustworthiness 
refers to the system’s objective characteristics, including 
its technical capabilities and performance (Schlicker and 
Langer 2021). This distinction is crucial for understand-
ing how users interact with and accept AI technologies 
across various fields.

It is also important to distinguish between trust and 
reliance, as these concepts, while related, are not identi-
cal. In accordance with the findings of Lee and See (Lee 
and See 2004), trust can be defined as users’ subjective 
perception  and  attitude  towards  a  system’s  reliability. 
In contrast, reliance can be defined as the actual behav-
ioural  outcome  of  adopting  or  using  the  system.  This 
distinction is crucial to the present study, as it examines 
users’  choices  between  different  AI  systems  (a  form  of 
intended reliance) rather than directly measuring their 
trust  attitudes.  While  trust  is  known  to  influence 
reliance,  other  factors  may  also  affect  the  decision  to 
use a system. This highlights the importance of consid-
ering both concepts when examining AI adoption (Lee 
and See 2004).

The theoretical foundation for understanding  trust 
in  AI  systems  largely  derives  from  Mayer  et  al.’s 
(Mayer, Davis, and David Schoorman 1995) model of 
organisational  trust,  which  posits  that  trust  develops 
based  on  a  trustor’s  perceptions  of  a  trustee’s  ability, 
benevolence,  and  integrity.  Recognising  that  this 
organisational  model  may  not  perfectly  translate  to 
human-machine  interactions  (Madhavan  and  Wieg-
mann  2007), Lee  and See  (Lee and  See 2004)  adapted 
it specifically for automation contexts. In their frame-
work, trust assessment relies on three key aspects: the 
machine’s  reliability  and  functionality  (ability = per-
formance),  the  intentions  behind  its  design  (benevo-
lence = purpose),  and  its  intelligibility  (integrity =  
process).  They  conceptualise  trust  in  automation  as 
the belief that a machine will help achieve one’s objec-
tives,  particularly  in  situations  involving  uncertainty 
and risk.

Building  on  this  foundation,  research  has  explored 
various aspects of trust formation in technological sys-
tems.  One  important  consideration  is  epistemic  trust, 
which  represents  the  confidence  users  place  in  experts 
or  institutions  based  on  their  perceived  competence 
and  integrity  (Sperber  et  al.  2010).  This  concept  high-
lights  how  trust  in  AI  systems  can  be  influenced  by 
users’ faith in the system’s developers and implementing 
organisations.  Another  crucial  aspect  in  trust  develop-
ment is the concept of calibrated trust, which examines 
the alignment between users’ trust levels and a system’s 
actual  reliability  (Wischnewski,  Krämer,  and  Müller 
for  ensuring 
2023).  This  alignment

is  essential

---

<!-- PAGE 4 -->

842

N. E. CETINKAYA AND N. KRÄMER

appropriate  reliance  on  AI  systems,  as  both  over-trust 
and under-trust can lead to suboptimal outcomes.

sufficient  knowledge  in  all  relevant  socio-scientific 
issues (inability, [ Bromme and Gierth 2021]).

Recent  research  has  further  differentiated  between 
understanding  and  trust  as  distinct  outcomes 
in 
human-AI  interaction  (De  Brito  Duarte  et  al.  2023). 
Understanding refers to comprehending the operational 
mechanisms of AI systems, while trust represents confi-
dence  in  the  system’s  outputs.  This  distinction  is  par-
ticularly  relevant  when  examining 
the  roles  of 
explainability and trust seals in fostering user trust.

2.2  Understanding  versus  trust:  explainability 
and  trust  seals

the

However,

regarding

Explainability and trust seals represent two fundamen-
tally  different  approaches  to  building  trust  in  AI  sys-
tems.  Recently, and  in line with considerable efforts of 
the  explainable  AI  (XAI)  community  (Das  and  Rad 
2020; Gunning et al.  2019; Langer  et al. 2021; Norkute 
et  al.  2021;  Saeed  and  Omlin  2023),  explainability, 
defined  as  the  ability  to  attribute  comprehensible  and 
interpretable reasons for an AI’s decisions and actions, 
has  been widely recognised as  an essential prerequisite 
for  building  user  trust.  It  provides  users  with  a  deeper 
understanding  of  AI  behaviour  and  reduces  perceived 
risks and uncertainties (Shin and Park 2019). A signifi-
cant  body  of  research  highlights  that  explainability  is 
crucial  for  establishing  AI  trustworthiness  (Caspers 
2021; Jacovi et al. 2021).
research

relationship 
between  explainability  and  trust  has  yielded  complex 
and  sometimes  contradictory  findings.  While  some 
studies demonstrate that human-understandable expla-
nations  can  enhance user  comprehension  and  increase 
trust  in  AI  performance  (Nourani  et  al.  2019;  Wang, 
Pynadath, and Hill 2015), others reveal a more nuanced 
dynamic.  Ferrario  and  Loi  (Ferrario  and  Loi  2022) 
found  that  enhancing  system  comprehension  through 
explainability  may  actually result  in decreased  trust,  as 
users  gain  deeper  insights  into  system  limitations  and 
potential  failure  modes,  leading  to  a  more  critical  per-
spective  of  the  system’s  capabilities.  In  addition,  the 
attempt to foster a better understanding of system capa-
bilities  might  be  met  with  people’s  unwillingness  or 
inability  to  understand  (Krämer,  Wischnewski,  and 
Müller  2023).  Here,  it  has  been  demonstrated  that 
users sometimes do not want to understand algorithmic 
systems as they, for example, avoid to be scared off their 
usage  (unwillingness,  [  Ngo  and  Krämer  2021]).  Also, 
systems  are  increasingly  complex  to  understand  and 
merely  a  small  part  of  everyday  life  problems  that 
might be important to understand (e.g. climate change, 
vaccines),  so  that  people  are  not  able  to  achieve

Instead  of  building  on understanding,  Bromme  and 
Gierth (Bromme and Gierth 2021) propose to shift the 
(too  complicated)  question  of  what  to  believe  or  to 
know,  respectively,  to  the  less  demanding  but  equally 
rational question of whom to trust. This form of ‘episte-
mic  trust’  (Sperber  et  al.  2010)  is  exemplified  in  trust 
seals. Trust seals, therefore, offer an alternative pathway 
to building trust through institutional validation rather 
than  direct  understanding.  These  trust  cues,  which 
include  certifications  and  seals  of  approval  from  repu-
table  organisations,  provide  users  with  tangible  signals 
of  an  AI  system’s  credibility  and  security  (Scharowski 
et  al.  2023).  AI  certifications  represent  formal  recog-
nition  from  independent  third  parties  that  a  system 
meets  predefined  standards  through  thorough  evalu-
ation  and  auditing.  These  certifications  aim  to  address 
the inherent complexity and uncertainty of AI systems 
by providing clear indicators of trustworthiness (Wisch-
newski, Krämer, and Müller 2023).

The effectiveness of trust seals is supported by research 
suggesting  that  public  trust  primarily  requires  robust 
regulatory oversight rather than technical understanding 
(Knowles and Richards 2021). This includes the establish-
ment of authoritative bodies to enforce compliance with 
ethical standards and validate AI systems’ trustworthiness 
through mandatory conformity assessments and algorith-
mic  auditing  (Afroogh  et  al.  2024).  This  approach 
acknowledges  that  users  often  rely  more  effectively  on 
institutional  validation  (‘whom  to  trust’)  than  personal 
understanding  (‘what  to  know’)  when  confronting  com-
plex socio-scientific issues (Bromme and Gierth 2021).

trust  as  distinct  outcomes

Recent  research  has  begun  to  differentiate  between 
understanding  and 
in 
human-AI  interaction  (De  Brito  Duarte  et  al.  2023). 
While  understanding  involves  comprehending  oper-
ational  mechanisms,  trust  represents  confidence  in  sys-
tem  outputs.  The  influence  of  explainability  on  these 
outcomes  varies:  detailed  technical  explanations  can 
enhance understanding while potentially reducing blind 
trust,  leading  to  more  informed  and  appropriate  levels 
of reliance on the system (Mehrotra et al. 2024). This dis-
tinction  helps  explain  why  increased  explainability  does 
not automatically translate to increased trust and suggests 
that  the  goal  should  be  to  foster  informed  trust  rather 
than maximising trust indiscriminately.

Despite  extensive  research  on  both  mechanisms, 
there  remains  a  significant  gap  in  understanding  how 
users weigh explainability against trust seals when eval-
uating  AI  systems.  This  study  addresses  this  gap  by 
directly comparing these approaches while considering 
additional influential factors.

---

<!-- PAGE 5 -->

BEHAVIOUR & INFORMATION TECHNOLOGY

843

2.3  Additional  factors:  reliability  and  fairness

2.4  Hypotheses  and  research  questions

While  our  primary  focus  remains  on  the  interplay 
between  explainability  and  trust  seals,  we  include 
reliability  and  fairness  as  critical  additional  factors  to 
provide  a  more  comprehensive  understanding  of 
trust-building mechanisms in AI systems.

Reliability is defined as the probability that a system 
will fulfill its desired function under specific conditions 
over  a  designated  period  (Ebeling  2019).  In  the  litera-
ture,  reliability  and  robustness  are  often  used  inter-
changeably,  though  reliability  specifically  emphasises 
the  temporal  aspect  of  system  performance  (Hong 
et al. 2022). The concept has emerged as a crucial factor 
in  ensuring  the  security  and  accuracy  of  AI-based  sys-
tems (Belgaum et al. 2021), with reliability being closely 
intertwined  with  performance  metrics,  particularly 
accuracy (Mishra et al. 2024). Research shows a strong 
correlation between reliability levels and user trust and 
adoption  rates  (Kaplan  et  al.  2023).  In  this  study, 
reliability therefore is included as a potential ‘gold stan-
dard’ for selecting a system to use.

Fairness,  albeit  a  newer  consideration  in  AI  system 
development,  has  gained  significant  attention  due  to 
its  implications  for  user  trust  and  system  adoption. 
Research  demonstrates  that  users’  trust  in  AI  systems 
is  significantly  influenced  by  their  perceptions of  algo-
rithmic fairness (Sullivan, De Bourmont, and Dunaway 
2022).  When  AI  systems  demonstrate  equitable  treat-
ment  across  different  demographic  groups,  users  are 
more likely to develop and maintain trust in these tech-
nologies. Conversely, instances of algorithmic discrimi-
nation can severely undermine user trust and impede AI 
adoption (Zhou et al. 2021). Algorithmic bias can mani-
fest  in  various  forms,  often  stemming  from  historical 
inequities in training data or inherent flaws in algorithm 
design  (Jain  and  Menon  2023).  For  example,  studies 
have documented cases where AI systems exhibited dis-
criminatory  patterns  in  healthcare  diagnostics  (Ober-
meyer  et  al.  2019)  and  hiring  decisions  (Peña  et  al. 
2020).  Users  who  encounter  or  become  aware  of  such 
biases  are  significantly  less  likely  to  trust  and  engage 
with AI systems, regardless of their technical capabilities 
(Marassi 2023).

The inclusion of these additional factors allows us to 
evaluate  how  users  prioritise  different  trust-building 
mechanisms  while  acknowledging  that  reliability  and 
fairness  play  important  roles  in  the  broader  context 
of  AI  system  adoption.  This  approach  enables  us  to 
better  understand  the  relative  importance  of  our  pri-
mary variables – explainability and trust seals – within 
the larger landscape of factors influencing user trust in 
AI systems.

Building on this theoretical framework, we identify sev-
eral  key  research  gaps  regarding  how  users  prioritise 
different  trust-building  mechanisms  in  AI  systems. 
While  extensive  research  exists  on  individual  factors, 
there  is  limited  understanding  of  how  users  weigh 
these factors against each other, particularly in the con-
text  of  explainability  versus  institutional  validation 
through trust seals.

A study has shown that fairness and performance are 
equally important to respondents whereas explainability 
is  slightly  less  important  (Kieslich,  Keller,  and  Starke 
2022).  These  findings  also  show  the  importance  of 
reliability, since reliability is often categorised as a per-
formance  related  factor  (Kaplan  et  al.  2023).  Further-
more,  Kaplan  et  al.  (Kaplan  et  al.  2023)  demonstrated 
in their meta-analysis of trust in AI systems, reliability 
was identified as one of the most heavily weighted fac-
tors concerning the AI component. This is particularly 
evident  in  high-risk  decision-making  scenarios,  where 
reliability emerges as the primary determinant of system 
adoption (Chancey et al. 2017). Therefore, the following 
hypothesis is proposed:

H1:  People  will  prefer  reliability  over  fairness  and 
explainability.

The  relationship  between  explainability  and  trust 
seals presents a particularly interesting area for further 
examination. Explainability helps people to gain a dee-
per  understanding  of  the  decision-making  process  of 
an  AI  system  (Zhou,  Chen,  and  Holzinger  2022).  In 
contrast,  trust  seals  represent  an  external  seal  of 
approval  that  validates  trust  in  the  system  without 
requiring  understanding  of  its  internal  mechanisms 
(Cremers et al. 2019; Paaß and Hecker 2020). This dis-
tinction  raises  an  important  question  about  whether 
people prefer to understand the functioning of the sys-
tem or whether they are ready to trust a system which 
has  been  certified  as  safe  and  trustworthy  by  a  third 
party.

Building  on  the  previously  discussed  framework  of 
epistemic trust, research has shown that human under-
standing  of  algorithmic  functioning  is  limited,  with 
users  frequently  developing  only  superficial  mental 
models  of  AI  systems  (DeVito  et  al.  2018;  Kunkel 
et al. 2021; Ngo et al. 2020). While explanations might 
contribute  to  understanding,  trust  seals  could  poten-
tially  offer  a  more  direct  path  to  achieving  calibrated 
trust,  particularly  when  issued  by  competent  insti-
tutions  perceived  as  both  honest  and  well-meaning 
(Hendriks,  Kienhues,  and  Bromme  2015).  This  is 
especially  important  given  that  research  has  shown

---

<!-- PAGE 6 -->

844

N. E. CETINKAYA AND N. KRÄMER

system

fearing

information,

that  providing  extensive  explanations  can  sometimes 
decrease users’ ability to detect and correct system mis-
takes  (Poursabzi-Sangdeh  et  al.  2021).  Furthermore, 
studies  have  shown  that  users  sometimes  actively 
avoid  detailed 
that 
increased  knowledge  about  data  processing  might  dis-
courage  future  use  (Ngo  and  Krämer  2021;  Springer 
and  Whittaker  2020).  This  behavioural  pattern,  com-
bined  with  the  cognitive  demands  of  processing  com-
plex  technical  information,  suggests  that  trust  seals 
might  provide  a  more  accessible  means  of  fostering 
appropriate trust levels. Based on these considerations, 
we  hypothesise  that  people  will  prefer  trust  seals  over 
explanations  when  establishing  trust  in  AI  systems. 
Therefore, the following hypothesis is proposed:

H2: People will prefer trust seal over explanations.

However, for the AI system to be trusted by the users, 
the  AI’s  trustworthiness  must  be  truly  perceived  by 
them.  This  requires  certain  cues  to  be  provided  to  the 
users,  which  could  be  achieved  through  proper  docu-
mentation.  Therefore,  other  non-technical  axiological 
factors  for  building  trust,  especially  human-related 
ones,  could  be  engineered  to  enhance  trust  without 
the need to improve the trustworthiness of AI (Afroogh 
et al. 2024). These axiological factors could be trust cues 
in  the  form  of  AI  seals  and  also  enabling  fair  and 
unbiased  AI  systems.  Therefore,  the  following  hypoth-
esis is proposed:

H3:  People  will  prefer  communicated  trustworthiness, 
enhanced  through  proper  documentation  (AI  seal), 
over  actual  technical  trustworthiness  (reliability  and 
fairness).

The degree of trust placed in AI is not a simple, uni-
versal  phenomenon.  Rather,  it  is  a  multifaceted  and 
context-specific  construct  (Chen  2021).  It  is  possible 
that  users  may  assign  differential  weights  to  different 
attributes,  depending  on  the  specific  application  and 
their  individual  concerns  (Dorton  and  Harper  2022). 
For instance, in the context of healthcare, explainability 
importance, 
and  performance  are  of  paramount 
whereas  in  customer  service,  user  satisfaction  may  be 
the overarching concern (Geng and Chu 2012; Markus, 
Kors, and Rijnbeek 2021; Pierce et al. 2022).

factors,

The  degree  of  trust  placed  in  AI  is  influenced  by  a 
number  of 
the  explainability, 
including 
reliability,  trust  cues  like  AI  seals  and  fairness  of  the 
technology  in  question.  Each  attribute  contributes  to 
overall  trust  in  a  distinct  manner  (Angerschmid  et  al. 
2022;  De  Brito  Duarte  et  al.  2023;  Dorton  and  Harper 
2022;  Shin  2021;  Wischnewski,  Krämer,  and  Müller 
2023).  The  interaction  between  attributes  can  be

complex.  For  example,  high  explainability  might  com-
pensate for lower reliability or might mitigate concerns 
about  fairness.  It  can  be  concluded  that  certain  attri-
butes  may  exert  a  more  profound  influence  on  trust 
than  others.  For  instance,  reliability  is  frequently 
regarded  as  a  foundational  attribute  (Hong  et  al. 
2022),  yet  fairness  can  also  assume  an  important  role 
contingent  on  the  context.  An  understanding  of  the 
relative  influence  of  different  attributes  can  assist  AI 
developers  in  directing  their  efforts  towards  the  most 
impactful areas. For instance, if it is demonstrated that 
performance  and  fairness  significantly  enhance  trust, 
designers may prioritise these features, even if achieving 
absolute reliability is challenging. This research question 
emphasises the necessity of a user-centred approach to 
the  design  of  AI  systems,  whereby  user  trust  consider-
ations  should  guide  the  development  process.  It  also 
aims  to  identify  which  individual  attributes  or  combi-
nations  thereof  have  the  most  significant  impact  on 
trust.  Therefore,  we  propose  the  following  research 
question:
RQ: which combinations of attributes will be preferred 
the most?

2.5. RQ: which combinations of attributes will be 
preferred  the  most?

3 Method

The study design as well as the hypotheses were prere-
gistered  on  the  Open  Science  Framework  (OSF)  prior 
to  data  collection  in  November  2024  (https://osf.io/ 
mw4dq/?view_only = 04327e74dfa34e4ca2babc170e86c 
048).  All  study  materials,  including  instructions  and 
data,  are  publicly  available  in  the  associated  project 
repository. An approval by the responsible ethics com-
mittee  of  the  University  Duisburg-Essen  was  given  to 
conduct  the  study.  Statistical  data  analysis  was  per-
formed using version 29 of IBM SPSS Statistics software 
for  Windows  (IBM  Corp.,  2023)  and  Python  (Version 
3.9.6)

3.1  Measures

3.1.1  Choice-Based  conjoint  analysis
The  present  study  employed  choice-based  conjoint 
analysis  (CBC)  to  systematically  evaluate  participants’ 
trust preferences between different AI system configur-
ations  in  healthcare  decision-making.  The  CBC  is  a 
method  of  presenting  choice  scenarios  to  participants, 
who are required to make trade-offs between attributes. 
The method has been developed for the purpose of iden-
tifying  true  preference  structures  and  determining  the

---

<!-- PAGE 7 -->

relative importance attributed to distinct characteristics. 
Despite  its  apparent  simplicity,  CBC  is  an  effective 
method  of  capturing  real-world  decision  processes  by 
forcing  users  to  make  concrete  trade-offs  rather  than 
rating features in isolation (Orme 2010). Prior to com-
mencing  the  choice  tasks,  participants  were  presented 
with  comprehensive  instructions  and  a  healthcare 
decision scenario that framed their evaluation specifically 
in  terms  of  trust.  The  scenario  described  an  AI  system 
designed  to  assist  with  important  health  decisions, 
including  treatment  selection,  health  data  monitoring, 
and  personalised  health  advice.  Participants  were 
instructed to deliberate on which AI system profile they 
would  entrust  with  greater  confidence,  contemplating 
the  potential  hazards  of  imprecise  or  prejudiced  rec-
ommendations  within  healthcare  contexts.  The  exper-
imental  design  incorporated  four  key  attributes  with 
varying levels: explainability (three levels: no explainabil-
ity,  low  explainability,  high  explainability),  reliability 
(two levels: medium reliability at 65%, high reliability at 
99%),  trust  cues  (three  levels:  no  AI  seal,  low  AI  seal, 
high  AI  seal),  and  fairness  (two  levels:  low  fairness, 
high fairness). To ensure a comprehensive understanding 
of the experimental design, participants received detailed 
descriptions  of  each  attribute  and  its  associated  levels, 
with  definitions  readily  available  throughout  the  study 
for  reference.  The  design  generated  36  unique  attribute 
combinations,  which  were  presented  across  18  discrete 
choice tasks (i.e. every participant had to make 18 choices 
between to system descriptions each). In each task, par-
ticipants  were  shown  two  competing  AI  system  profiles 
simultaneously and were required to indicate which sys-
tem they would trust more based on the presented attri-
butes  (see  Figure  1).  This  forced-choice  methodology 
enabled the assessment of how different attribute combi-
nations  influenced  participants’  trust  decisions.  The

BEHAVIOUR & INFORMATION TECHNOLOGY

845

systematic  variation  of  attribute  levels  across  profiles 
enabled the subsequent estimation of part-worth utilities 
and  relative  importance  weights  for  each  attribute  and 
level in trust formation.

3.1.2  Additional  measures
Attitude  towards  Artificial  Intelligence  was  measured 
using  the  German  version  of  the  Attitude  Towards 
Artificial Intelligence (ATAI) scale developed by Sinder-
mann et al. (Sindermann et al. 2021). The scale consists 
of  five  items  assessing  two  dimensions:  Acceptance  (2 
items) and Fear (3 items) of Artificial Intelligence (e.g. 
‘Artificial intelligence will benefit humankind’). Partici-
pants  responded  on  an  11-point  Likert  scale  ranging 
from  0  (‘strongly  disagree’)  to  10  (‘strongly  agree’). 
The  subscales  demonstrated  acceptable  reliability  in 
our  sample,  with  Cronbach’s  α = .66  for  Acceptance 
and α = .70 for Fear.

3.2  Procedure

The  online  study  was  conducted  on  the  SoSci-Survey 
platform. Prior to the commencement of the study, par-
ticipants were provided with a detailed instruction and 
asked to give consent. Following this, consent to partici-
pate  was  obtained.  Participants  then  completed  a 
choice-based conjoint analysis to assess their trust pre-
ferences  in  AI  healthcare  systems.  Following  this,  they 
responded to a questionnaire measuring their attitudes 
toward  artificial  intelligence,  specifically  focusing  on 
AI  acceptance  and  fear  of  AI.  The  survey  concluded 
with  the  collection  of  socio-demographic  information, 
including  gender,  age,  educational  qualifications,  and 
employment status. Upon completion of all study com-
ponents, participants received a debriefing that outlined 
the study’s objectives and purpose. The entire procedure

Figure  1.  Example  of  a  choice  task  in  the  conjoint  analysis  study.

---

<!-- PAGE 8 -->

846

N. E. CETINKAYA AND N. KRÄMER

was conducted in German to ensure participants could 
fully  understand  and  respond  to  all  materials  in  their 
native language.

3.3  Sample

The  data  collection  process  was  carried  out  through  an 
online study implemented on the SoSci-Survey platform. 
The  required  sample  size  was  calculated  using  Johnson 
and  Orme’s  (Johnson  and  Orme  2010)  formula,  which 
was  specifically  designed  for  choice-based  conjoint  ana-
lyses.  The  sample  size  was  determined  using  the  John-
son-Orme  formula  (Johnson  and  Orme  2010)  for 
choice-based  conjoint  analyses.  While  the  calculated 
minimum  sample  threshold  was  42  participants,  we 
selected a substantially larger sample size to enhance stat-
istical power. Participants were recruited from Germany 
through the online panel Prolific between November 11- 
12, 2024. German language proficiency was established as 
an inclusion criterion since the survey was conducted in 
German.  Furthermore,  participants  were  required  to  be 
at  least  18  years  of  age.  The  initial  dataset  comprised 
323 participants. Following a thorough data cleaning pro-
cedure, which involved the exclusion of eight participants 
due to incomplete responses, the final sample comprised 
315  participants  (see  Table  2 for  detailed  sociodemo-
graphic  characteristics).  Participants  were  remunerated 
for their participation through the Prolific platform.

4 Results

4.1  Overview  of  analysis  approach

Based on the preregistered analysis plan, we employed a 
conventional conjoint approach. As this analysis did not 
reveal  user  preferences  for  specific  attributes,  we  con-
ducted additional, explorative cluster analyses in order 
to  test  for  the  presence  of  heterogeneous  preferences 
within 
the  sample  population.  This  observation 
prompted the implementation of an explorative analysis 
with a segmentation approach to identify and examine 
potential heterogeneity in preferences. The analysis uti-
lised  a  two-stage  methodology:  initially,  a  latent  class 
analysis  (LCA)  employing  a  Gaussian  mixture  model 
with two components to identify distinct preference pat-
terns, followed by logistic regression for each identified 
cluster.  The  analysis  examined  four  key  attributes: 
explainability, reliability, AI certification seal, and  fair-
ness.  For  each  segment,  the  approach  generated  prob-
ability-based  preference 
attribute 
combinations,  allowing  the  identification  of  segment- 
specific  preferred  combinations  while  considering  the 
interaction effects between attributes.

across

scores

Table  1.  Logistic  regression.

Total  sample.  (n  
= 315)

Cluster  1.  (n =  
182)

Cluster  2.  (n =  
133)

Explainability
Reliability
AI  certification

0.0042
0.0183
0.0111

0.1447***

−0.0669

0.1926***

−0.1899***
0.1371*
−0.2395***

0.0155

−0.2692***

seal
Fairness
Results  show  regression  coefficients  (β)  that  indicate  attribute  preferences 
within  each  cluster  based  on  logistic  regression  analysis.  Positive  coeffi-
cients indicate positive preferences for an attribute, while negative coeffi-
cients indicate negative preferences. Statistical significance determined by 
z-tests.  P-values  indicate  significance  levels:  *p < 0.05,  **p < 0.01,  ***p <  
0.001.

0.4090***

4.2  Hypothesis  testing  results

The analysis of the complete sample revealed no signifi-
cant preferences across the four key attributes explain-
ability,  reliability,  AI  certification  and  fairness  (see 
Table  1).  For  the  analyses including the  whole  sample, 
all hypotheses need to be rejected.

4.3  Research  question:  most  preferred  attribute 
combinations

The Choice-Based Conjoint Analysis of the total sample 
revealed a consistent preference pattern, with the most 
preferred  combination  achieving  a  50.8%  selection 
probability.  The  optimal  combination  consisted  of  no 
explainability,  medium  reliability  (65%),  no  AI  certifi-
cation  seal,  and  high  fairness.  The  observed  similarity 
in  the  range  of  preference  probabilities  (50.3%  to

Table  2.  Sample  size  and  description.
Total 
sample.  (n  
= 315)

Cluster  1.  (n = 182)

Women

Men

Diverse
Not  Specified
Age

University 
Degree

Highest  School

Degree
University 
Entrance 
Qualification
AI  Acceptance

AI  Fear

158

(50.16%)

153

(48.57%)
3  (0.95%)
1  (0.32%)
18–92  (M  
= 32.6; 
SD =  
10.7)

183

(58.1%)
71  (22.5%)

86  (47.3%)

92  (50.5%)

3  (1.6%)
1  (0.5%)

18–92  (M = 32.5;  SD = 10.4)

103  (56.6%)

44  (24.2%)

61  (19.4%)

35  (19.2%)

M = 7.18  (SD = 1.74)

M = 4.79  (SD = 1.90)

M = 7.27 
(SD =  
1.75)
M = 4.65 
(SD =  
1.83)

Cluster 
2.  (n =  
133)

67

(50.4%)

66

(49.6%)

–
–
18–92  (M  
= 32.9; 
SD =  
10.1)

80

(60.2%)

27

(20.3%)

17

(12.8%)

M = 7.40 
(SD =  
1.75)
M = 4.46 
(SD =  
1.69)

---

<!-- PAGE 9 -->

50.8%)  across  the  top  combinations  suggests  the  pres-
ence of relatively uniform preferences within the overall 
sample.

4.4  Explorative  analysis

4.4.1  Cluster  analysis  results
We  employed  Latent  Class  Analysis  (LCA),  a  special 
type of finite mixture model for clustering with discrete 
variables,  rather  than  k-means.  LCA  has  been  demon-
strated  to  be  advantageous for  our Choice-Based  Con-
joint  data,  as  it  has  been  shown  to  directly  model 
choice  probabilities  and  to  better  handle  categorical 
attributes. In the context of model selection, a compara-
tive  analysis  was  conducted  between  BIC  and  AIC 
values  across  a  range  of  1–5  cluster  solutions.  The  2- 
cluster  solution  was  identified  as  optimal,  exhibiting 
both  significant  improvement  over  a  single  cluster  (χ²  
= 83.2,  p < 0.001)  and  high  entropy  (0.82),  indicative 
of clear segment separation. The LCA identified two dis-
tinct  participant  clusters  (n₁ = 133,  n₂ = 182),  each 
demonstrating  significantly  different  preferences  for 
AI  system  attributes.  The  analysis  revealed  notable 
differences  in  both  preference  patterns  (see  Table  1) 
and demographic characteristics between the identified 
clusters,  providing  more  actionable  insights  than  the 
initial overall analysis.

4.4.2  Hypothesis  testing  results  for  both  clusters
Separate logistic regression analyses were conducted for 
each  cluster  to  test  our  hypotheses,  with  choice  as  the 
dependent variable and attribute levels as the indepen-
dent  variables.  Statistical  significance  was  assessed 
using  z-tests  (p < 0.05).  The  model  showed  good  fit 
with  Pseudo  R²  values  of  0.01027  (Cluster  1)  and 
0.01900  (Cluster  2),  and  highly  significant  likelihood 
ratio tests (p < 0.001).

In the context of the study, hypothesis H1 postulated 
that individuals would prioritise reliability over fairness 
and  explainability.  However,  the  analysis  revealed  that 
this hypothesis is not supported in both clusters. Cluster 
1  exhibited  no  significant  effect  for  reliability  (β =  
−0.067,  z = −1.344,  p = 0.179)  and  a  negative  fairness 
effect  (β = −0.269,  z = −5.409,  p < 0.001).  Cluster  2 
demonstrated  significant  effects  for  both  reliability  (β  
= 0.137,  z = 2.341,  p = 0.019)  and  fairness  (β = 0.409,  z  
= 6.980,  p < 0.001),  with  fairness  showing  stronger 
influence.

The second hypothesis, which posited that trust seals 
would  be  more  effective  than  explanations,  received 
mixed support across clusters. Cluster 1 exhibited stron-
ger preferences for AI certification (β = 0.193, z = 6.310, 
p < 0.001)  compared  to  explainability  (β = 0.145,  z =

BEHAVIOUR & INFORMATION TECHNOLOGY

847

4.742,  p < 0.001),  thereby  providing  support  for  the 
hypothesis. Conversely, Cluster 2 exhibited adverse pre-
ferences  for  both  attributes,  with  AI  certification 
demonstrating  a  more  pronounced  negative  effect  (β  
= −0.240,  z = −6.660,  p < 0.001)  compared  to  explain-
ability (β = −0.190, z = −5.285, p < 0.001).

The  third  hypothesis  postulated  that  individuals 
would  demonstrate  stronger  preference  for  communi-
cated  trustworthiness  (AI  seal)  over  actual  technical 
trustworthiness  (reliability  and  fairness).  This  hypoth-
esis received partial support. Cluster 0 exhibited stron-
ger  preferences  for  communicated  trustworthiness 
through AI certification (β = 0.193, p < 0.001) compared 
to  technical  trustworthiness  indicators.  In  contrast, 
Cluster  1  demonstrated  stronger  inclination  toward 
technical 
indicators  (fairness:  β =  
0.409,  p < 0.001;  reliability:  β = 0.137,  p = 0.019)  over 
AI certification (β = −0.240, p < 0.001).

trustworthiness

4.4.3  Research  question:  most  preferred  attribute 
combinations  for  both  clusters
The results of the first cluster demonstrated a clear pre-
ference structure, with the most preferred combination 
achieving  a  62.4%  selection  probability.  This  optimal 
combination  comprised  of  no  explainability,  high 
reliability (99%), no AI certificate, and limited fairness. 
The results of the second cluster revealed different pre-
ferences, with the most preferred combination attain-
ing  a  66.9%  selection  probability.  This  optimal 
combination was characterised by its low explainabil-
ity,  medium  reliability  (65%),  low  AI  certificate,  and 
high fairness.

4.4.4  Demographic  and  attitudinal  differences 
between  clusters
Further  statistical  analysis  revealed  significant  demo-
graphic differences between the clusters. Statistical ana-
lyses were performed using independent samples t-tests 
for  continuous  variables,  while  chi-square  tests  were 
employed for categorical variables. The t-tests revealed 
significant differences between the clusters in AI accep-
tance  (t = −6.453,  p < .001)  and  AI  fear  (t = 9.701,  p  
< .001),  as  well  as  age  (t = −2.147,  p = .  032).  Cluster  1 
reported  higher  AI  acceptance  and  lower  AI  anxiety, 
whereas  cluster  2  reported  lower  AI  acceptance  and 
higher  AI  anxiety.  While  age  differences  were  small, 
Cluster  2  participants  were  slightly  older  than  Cluster 
1  participants.  Detailed  demographic  characteristics 
for  both  clusters  can  be  found  in  Table  2.  Educational 
backgrounds differed significantly between clusters (χ²  
= 86.289, p < .001). The distribution of educational qua-
lifications  varied  notably,  with  Cluster  1  showing  a 
higher  proportion  of  university  degrees,  while  Cluster

---

<!-- PAGE 10 -->

848

N. E. CETINKAYA AND N. KRÄMER

2  had  a  higher  percentage  of  participants  with  highest 
school  degrees  and  university  entrance  qualifications. 
Gender  distribution  also  showed  significant  variation 
between clusters (χ² = 111.259, p < .001). While Cluster 
1  demonstrated  an  almost  equal  distribution  between 
female  and  male  participants,  Cluster  2  showed  a 
more  diverse  pattern,  including  small  percentages  of 
participants  identifying  as  other  gender  or  preferring 
not  to  specify.  Comprehensive  descriptive  statistics  for 
both clusters are presented in Table 2.

5 Discussion

This  study  examined  user  preferences  regarding  key 
attributes of AI systems, with a particular focus on the 
relative importance of explainability, reliability, AI cer-
tification, and fairness in users’ decisions to engage with 
AI  systems.  The  findings  of  the  study  revealed  a  more 
complex  picture  than  initially  hypothesised,  with  no 
attributes  standing  out  when  analysing  the  whole 
sample.  Cluster  analyses,  however,  revealed  that  there 
are  distinct  user  groups  with  opposite  preferences. 
These results offer significant implications for both the 
theoretical  understanding  of  AI  system  development 
and the practical applications of these systems.

5.1  Heterogeneous  user  preferences  and  trust 
development

The  lack  of  significant  overall  preferences  across  the 
entire  sample  is  notable,  as  it  suggests  that  the  prefer-
ences  of  different  user  groups  effectively  balance  each 
other out. However further analysis, employing cluster 
analysis, revealed two distinct clusters of users with con-
trasting preferences, challenging the assumption of uni-
form  user  priorities  in  AI  system  adoption.  Cluster  1 
demonstrated  strong  preferences  for  AI  certification 
and explainability while expressing negative preferences 
for  fairness.  In  contrast,  Cluster  2  prioritised  fairness 
and  reliability  while  showing  negative  preference 
towards  choosing  explainability  and  AI  certification. 
This  group  demonstrated  higher  AI  acceptance  and 
lower  AI  fear  scores,  indicating  a  more  confident 
approach to AI interaction.

These  findings  contradict  our  first  hypothesis  that 
users  would  universally  prefer  reliability  over  fairness 
and  explainability.  Instead,  we  found  that  reliability’s 
importance  varies  significantly  between  user  groups, 
with  Cluster  2  showing  moderate  preference  for 
reliability  while  Cluster  1  showed  no  significant  effect. 
This  challenges  previous  findings  by  Kaplan  et  al. 
(2023) who identified reliability as the primary predictor 
of  trust  in  AI  systems.  Our  results  suggest  that  the

relationship between system reliability and user prefer-
ence may be more nuanced and influenced by individual 
differences in AI attitudes.

5.1.  Understanding  versus  trust:  the  role  of 
explainability  and  certification

An  analysis  of  the  relationship  between  explainability 
and trust signals (H2) across the entire sample revealed 
no  significant  overall  preferences,  consistent  with  our 
findings  regarding  other  attributes.  However,  distinct 
patterns  emerged  at  the  cluster  level,  indicating  that 
while users lack universal preferences, individual groups 
demonstrate clear  inclinations  towards  or  against  both 
mechanisms.

The findings of the present study showed that prefer-
ences for transparency (i.e. explainability) and trust sig-
nals (i.e. AI certification seals) are interconnected. These 
results contradict the hypothesis (H2) that users would 
prioritise one over the other. Cluster 1 exhibited a pre-
ference for both explainability and certification, indicat-
ing  that  these  users  seek  diverse  forms  of  external 
validation  when  evaluating  AI  systems.  This  finding  is 
consistent  with  theoretical  frameworks  suggesting  that 
users  may  employ  multiple  trust-building  mechanisms 
when dealing with complex systems (Paaß and Hecker 
2020).

In contrast, Cluster 2 demonstrated negative prefer-
ences  for  both  explainability  and  certification  while 
favouring  fairness  and  reliability.  This  pattern  chal-
lenges  previous  assumptions  about  users  universally 
needing system understanding or validation. Whilst an 
initial interpretation indicated that users might establish 
trust  through  alternative  means,  such  as  direct  system 
performance  observation,  a  more  nuanced  interpret-
ation  is  required.  It  is  crucial  to  acknowledge  that  the 
present  study  measured  system  choice  as  opposed  to 
trust directly, as these are related yet distinct concepts. 
This  perspective  aligns  with  the  findings  reported  by 
(Kieslich,  Keller,  and  Starke  2022)  and  (Bao  et  al. 
2022),  which  suggest  that  some  users  may  exhibit 
indifference  towards  specific  ethical  considerations  of 
AI  systems,  particularly  transparency  mechanisms.  In 
contrast  to  actively  seeking  diverse  trust  pathways, 
these  users  may  prioritise  performance-oriented  attri-
butes  with  immediate  practical  impact  (e.g.  fairness 
and  reliability),  while  demonstrating  comparatively 
less concern for the justification of system decisions or 
for external validation. This finding extends the obser-
vation  made  by  Ferrario  and  Loi  (Ferrario  and  Loi 
2022) regarding the potential of increased system famili-
arity to reduce reliance on conventional trust mechan-
isms.  The  results  suggest  that  user  preferences  for  AI

---

<!-- PAGE 11 -->

system  attributes  are  more  intricate  and  diverse  than 
previously understood.

The parallel preferences for or against both transpar-
ency and trust mechanisms across clusters suggest that 
these attributes may be more interconnected than pre-
viously  theorised,  potentially  representing  different 
aspects  of  a  single  underlying  approach  to  AI  system 
evaluation,  potentially  relying  on  external  communi-
cation about the system.

5.2.  Technical  versus  communicated 
trustworthiness

Analysis of preferences between technical and commu-
nicated  trustworthiness  (H3)  revealed  no  significant 
trends  across  the  complete  sample.  However,  distinct 
patterns  emerged  at  the  cluster  level,  demonstrating 
how  different  user groups  approach trust  development 
in  contrasting  ways.  Our  third  hypothesis  regarding 
the  preference  for  communicated  trustworthiness  over 
technical  trustworthiness  revealed  a  more  complex 
dynamic  than  anticipated.  The  analysis  showed  a  clear 
division  between  clusters  in  how  they  evaluate  and 
prioritise different forms of trustworthiness.

Cluster  1’s  stronger  preference  for  AI  certification 
aligns  with  Knowles  and  Richards’  (Knowles  and 
Richards 2021) argument about the importance of regu-
latory frameworks in building public trust. The fact that 
this  group  showed  no  significant  preference  for 
reliability,  traditionally  considered  a  cornerstone  of 
technical 
the 
interpretation  that  they  rely  more  heavily  on  external 
validation than direct performance assessment.

trustworthiness,

supports

further

in

In  contrast,  Cluster  2’s  clear  preference  for  technical 
trustworthiness  indicators  (fairness  and  reliability)  over 
certification  presents  an  unexpected  pattern  that  chal-
lenges  conventional  wisdom  about  trust  development. 
This group appeared to reject communicated trustworthi-
ness 
indicators, 
favour  of  direct  performance 
suggesting that some users might be more critical of exter-
nal validation mechanisms, preferring instead to evaluate 
systems based on their actual performance characteristics.
These contrasting  preferences raise  important  ques-
tions  about  the  conventional  approach  to  AI  system 
deployment,  which  often  emphasises  standardised  cer-
tification  and  documentation  practices.  Our  results 
suggest that different user groups might require funda-
mentally  different  approaches  to  establishing  trust-
worthiness.  This  has  significant  implications  for  our 
research  question  about  attribute  combinations,  as  it 
indicates that the effectiveness of various trust-building 
features  might  depend  heavily  on  users’  underlying 
technology  evaluation.  The  finding 
approach

to

BEHAVIOUR & INFORMATION TECHNOLOGY

849

challenges  the  assumption  that  adding  more  trust  sig-
nals  universally  enhances  system 
trustworthiness, 
suggesting  instead  that  targeted  combinations  might 
be more effective for specific user groups.

5.3.  Preferred  attribute  combinations  and  their 
implications

The Choice-Based Conjoint Analysis of the total sample 
revealed  a  consistent  preference  pattern,  with  similar 
selection probabilities (50.3% to 50.8%) across top com-
binations. The combination that was selected most fre-
quently,  achieving  a  50.8%  selection  probability, 
featured  no  explainability,  medium  reliability  (65%), 
no AI certification seal, and high fairness. This relative 
uniformity in preference probabilities suggests balanced 
preferences within the overall sample. However, cluster 
analysis revealed more nuanced patterns.

Cluster  1’s  optimal  combination  revealed  an  unex-
pected  preference  pattern:  they  favoured  high  reliability 
without  explainability  or  fairness  features.  This  finding 
suggests  a  minimalist  approach  that  focuses  solely  on 
technical  performance.  This  pattern  might  indicate  that 
for some users, system complexity itself could be a source 
of concern, leading them to prefer simpler, more straight-
forward implementations when given direct choice scen-
arios.  This  interpretation  aligns  with  Springer  and 
Whittaker’s  (Springer  and  Whittaker  2020)  observation 
that  some  users  actively  avoid  detailed  system  infor-
mation, fearing that increased knowledge about data pro-
cessing might discourage future use.

Cluster 2’s preferred combination presents an equally 
unexpected but different pattern: they opted for systems 
with  low  explainability,  moderate  reliability  (65%),  low 
AI certification, but high fairness. This preference pattern 
is particularly significant as it challenges multiple assump-
tions about AI system design. Their strong emphasis on 
fairness  while  accepting  lower  levels  of  other  attributes 
supports Sullivan et al.’s (2022) findings about the growing 
importance of ethical considerations in user trust develop-
ment. The willingness to accept moderate reliability when 
paired  with  high  fairness  suggests  that  users  might  be 
making  sophisticated  trade-offs  between  technical  per-
formance and ethical considerations.

This  finding  extends  beyond  simple  feature  prefer-
ences to suggest deeper differences in how users concep-
tualise  and  evaluate  AI  trustworthiness.  While  system 
designers often strive to maximise all positive attributes, 
our  results  indicate  that  different  user  groups  might 
have fundamentally different visions of what constitutes 
an ideal AI system. This has significant implications for 
AI system development, suggesting that optimising for 
all features simultaneously might actually make systems

---

<!-- PAGE 12 -->

850

N. E. CETINKAYA AND N. KRÄMER

less  appealing  to  certain  user  groups  who  prefer  more 
focused or streamlined implementations. These patterns 
also suggest an important refinement to theories about 
trust  development  in  AI  systems.  Rather  than  treating 
trust  as  a  cumulative  product  of  positive  features,  our 
findings indicate that users might employ different stra-
tegic  approaches  to  system  evaluation,  with  some  pre-
ferring  focused,  performance-oriented  systems  while 
others seek more balanced implementations that prior-
itise  ethical  considerations  over  maximum  technical 
performance.

5.4.  Limitations  and  future  research

Despite  the  fact  that  the  methodological  approach  of 
presenting  isolated  attribute  combinations  may  appear 
to  be  abstracted  from  real-world  AI  interactions,  this 
design  choice  offers  crucial  advantages.  As  Orme 
(Orme  2010)  observes,  conjoint  analysis  allows  for  the 
precise measurement of relative preferences for specific 
AI system attributes by deliberately reducing complexity 
for  confounding  variables.  This 
and  controlling 
approach  enables  the  observation  of  realistic  decision- 
making  processes  through  forced  trade-offs.  Whilst 
the present controlled experimental setting may appear 
to be detached from reality, it offers unique insights that 
would be difficult to obtain from studying complete AI 
systems where multiple factors interact simultaneously.
Nevertheless, several limitations should be considered 
when  interpreting these results. First, our study  focused 
on  a  specific  healthcare  decision-making  scenario,  and 
findings  may  not  generalise  to  other  AI  applications. 
Second,  while  our  sample  was  diverse  in  terms  of  age 
and  education,  it  was  limited  to  German  participants 
and may not be fully representative of all potential AI sys-
tem users. A final limitation of the present study concerns 
the  abstract  representation  of  system  attributes.  While 
these standardised presentations are necessary for the iso-
lation of attribute effects, they may not fully capture real- 
world user experiences with AI systems, potentially result-
ing in a limitation of ecological validity. It is recommended 
that  future  studies  build  upon  the  present  approach  by 
incorporating research that employs more concrete, inter-
active  representations  of  explainability  features  through 
functional prototypes or simulations that better approxi-
mate real-world AI interactions.

A significant consideration for future research is the 
role of AI literacy in shaping user preferences and trust 
development, building on recent work on digital literacy 
and  AI  adoption.  The  stark  differences  between  our 
identified  clusters  align  with  previous  findings  (Cox 
2024)  suggesting  that  varying  levels  of  AI  literacy  sig-
nificantly  influence  how  users  approach  and  evaluate

AI  systems.  Future  studies  should  explicitly  measure 
AI literacy to examine whether it mediates the relation-
ship  between  system  attributes  and  user  trust.  This 
could  help  explain  why  some  users  prioritise  technical 
performance while others rely more heavily on external 
validation. Future research could also explore how these 
preference patterns manifest in different AI application 
contexts, and how they might be influenced by cultural 
and organisational factors. The development of adaptive 
trust-building  mechanisms  that  can  accommodate 
different user groups remains an important avenue for 
investigation.  Additionally,  longitudinal  studies  exam-
ining  how  trust  development  patterns  evolve  with 
increased AI exposure and literacy would provide valu-
able insights for system design and implementation.

6 Conclusion

The present study examined the development of user trust 
in AI systems, revealing four crucial insights. Firstly, the 
findings contradict the prevalent assumption that a uni-
form pattern exists; instead, we observed contrasting pre-
ferences  among  user  groups  that  cancel  each  other  out. 
Secondly,  the  present  study  found  that  user  preferences 
regarding understanding (explainability) and trust signals 
(AI certification seal) are coupled. This finding challenges 
the  initial  research  question  about  whether  users  prefer 
one approach over the other. Instead of a clear preference 
for one over the other, a distinct group of users exhibited a 
desire  for  both  mechanisms,  suggesting  a  balanced 
approach  to  trust  and  transparency.  Thirdly,  distinct 
user  clusters  with  contrasting  trust-building  strategies 
were identified: one group relies heavily on both external 
validation and transparency, exhibiting higher AI anxiety; 
in contrast, another prioritises externally communicated 
reliability aspects and fairness metrics and shows greater 
AI  acceptance.  These  results  raise  important  questions 
about 
transparency 
approaches  in  reaching  all  user  populations,  and  the 
potential  need  for  alternative  strategies  to  engage  users 
who demonstrate less interest in critically examining AI 
systems beyond their direct performance outcomes. The 
methodological  approach  employed  in  this  study  has 
exposed sophisticated tradeoffs in user preferences, par-
ticularly regarding the prioritisation of technical perform-
ance over ethical considerations. Users comfortable with 
AI  technology  often  accept  moderate  reliability  when 
paired  with  high  fairness,  while  AI-anxious  users  place 
greater  emphasis  on  transparency  measures  and  certifi-
cation  seals.  The  findings  demonstrate  that  effective  AI 
integration  requires  a  shift  from  universal  design  prin-
ciples to adaptive approaches that acknowledge combined 
preferences and adapt to diverse user groups.

the  effectiveness  of  current

---

<!-- PAGE 13 -->

Acknowledgements

appreciate

the 
This  work  has  been  partly  supported  by 
Research Center Trustworthy Data Science and Security 
(https://rc-trust.ai/),  one  of  the  Research  Alliance  cen-
ters  within  the  UA  Ruhr  (https://uaruhr.de).  We  sin-
support.  Additionally, 
cerely 
generative  AI  tools,  specifically  Claude  3.7  Sonnet, 
were used during the writing process to support the lin-
guistic refinement and structural revision of texts orig-
including  text 
inally  authored  by  the  researcher, 
formulation,  proofreading,  and  debugging  of  code 
segments

their

Author  contributions

CRediT: Nur Efsan Cetinkaya: Conceptualization, Data cura-
tion,  Formal  analysis,  Funding  acquisition,  Investigation, 
Methodology,  Project  administration,  Resources,  Software, 
Supervision,  Validation,  Visualization,  Writing  –  original 
draft;  Nicole  Krämer:  Conceptualization,  Funding  acqui-
sition,  Methodology,  Resources,  Supervision,  Writing  – 
review & editing.

Disclosure statement

No potential conflict of interest was reported by the author(s).

Funding

This  work  was  supported  by  Research  Center  Trustworthy 
Data Science and Security.

References

Afroogh,  Saleh,  Ali  Akbari,  Emmie  Malone,  Mohammadali 
Kargar,  and  Hananeh  Alambeigi.  2024.  “Trust  in  AI: 
Progress,  Challenges,  and  Future  Directions.”  Humanities 
and  Social  Sciences  Communications  11  (1):  1568.  https:// 
doi.org/10.1057/s41599-024-04044-8.

Angerschmid,  Alessa,  Jianlong  Zhou,  Kevin  Theuermann, 
Fang  Chen,  and  Andreas  Holzinger.  2022.  “Fairness  and 
Explanation  in  AI-Informed  Decision  Making.”  Machine 
Learning  and  Knowledge  Extraction  4  (2):  556–579. 
https://doi.org/10.3390/make4020026.

Bao, Luye, Nicole M. Krause, Mikhaila N. Calice, Dietram A. 
Scheufele,  Christopher  D.  Wirz,  Dominique  Brossard, 
Todd  P.  Newman,  and  Michael  A.  Xenos.  2022.  “Whose 
AI?  How  Different  Publics  Think  about  AI  and  Its  Social 
Impacts.”  Computers  in  Human  Behavior  130:107182. 
https://doi.org/10.1016/j.chb.2022.107182.

Bartneck,  Christoph,  Christoph  Lütge,  Alan  Wagner,  and 
Sean  Welsh. 2021.  “Trust  and Fairness  in AI  Systems.” In 
An  Introduction  to  Ethics  in  Robotics  and  AI,  27–38. 
Cham:  Springer  International  Publishing..  https://doi.org/ 
10.1007/978-3-030-51110-4_4

Belgaum, M., Z. Alansari, S. Musa, M. Mansoor Alam, and M. 
Mazliham.  2021.  “Role  of  Artificial  Intelligence  in  Cloud

BEHAVIOUR & INFORMATION TECHNOLOGY

851

Computing,  Iot  and  Sdn:  Reliability  and  Scalability 
Issues.”  International  Journal  of  Electrical  and  Computer 
Engineering  (IJECE)  11  (5):  4458–4470.  https://doi.org/10. 
11591/ijece.v11i5.pp4458-4470.

Bromme, Rainer, and Lukas Gierth. 2021. “Rationality and the 
Public  Understanding  of  Science.”  In  The  Handbook  of 
Rationality,  edited  by  Markus  Knauff  and  Wolfgang 
Spohn, 767–776. Cambridge, MA: MIT Press.

Caspers,  Julian.  2021.  “Translation  of  Predictive  Modeling 
and  AI  into  Clinics:  A  Question  of  Trust.”  European 
Radiology  31  (7):  4947–4948.  https://doi.org/10.1007/ 
s00330-021-07977-9.

Chancey,  Eric  T.,  James  P.  Bliss,  Yusuke  Yamani,  and  Holly 
A.  H.  Handley.  2017.  “Trust  and  the  Compliance– 
Reliance  Paradigm:  The  Effects  of  Risk,  Error  Bias,  and 
Reliability  on  Trust  and  Dependence.”  Human  Factors: 
The Journal of the Human Factors and Ergonomics Society 
59 
https://doi.org/10.1177/ 
0018720816682648.

333–345.

(3):

Chen,  Melvin.  2021.  “Trust  and  Trust-Engineering

in 
Artificial  Intelligence  Research:  Theory  and  Praxis.” 
Philosophy  &  Technology  34  (4):  1429–1447.  https://doi. 
org/10.1007/s13347-021-00465-4.

Cox,  Andrew.  2024.  “Algorithmic  Literacy,  AI  Literacy  and 
Responsible  Generative  AI  Literacy.”  Journal  of  Web 
Librarianship  18  (3):  93–110.  https://doi.org/10.1080/ 
19322909.2024.2395341.

Cremers,  Armin  B,  Alex  Englander,  Markus  Gabriel,  Dirk 
Hecker,  Michael  Mock,  Maximilian  Poretschkin,  Julia 
Rosenzweig,  et  al.  2019.  Trustworthy  Use  of  Artificial 
Intelligence:  Priorities  from  a  Philosophical,  Ethical, 
Legal,  and  Technological  Viewpoint  as  a  Basis  for 
Certification of Artificial Intelligence.

Das,  Arun,  and  Paul  Rad.  2020.  “Opportunities  and 
Challenges  in  Explainable  Artificial  Intelligence  (XAI):  A 
Survey.”  ArXiv.  https://doi.org/10.48550/ARXIV.2006. 
11371.

De Brito Duarte, Regina, Filipa Correia, Patrícia Arriaga, and 
Ana  Paiva.  2023.  “AI  Trust:  Can  Explainable  AI  Enhance 
Warranted  Trust?”  Human  Behavior  and  Emerging 
Technologies 
2023:1–12.  https://doi.org/10.1155/2023/ 
4637678.

DeVito,  Michael  A,  Jeremy  Birnholtz,  Jeffery  T.  Hancock, 
Megan  French,  and  Sunny  Liu.  2018.  How  People  Form 
Folk  Theories  of  Social  Media  Feeds  and  What  It  Means 
for  How  We  Study  Self-presentation.  In  Proceedings  of 
the  2018  CHI  Conference  on  Human  Factors 
in 
Computing  Systems,  April  19,  2018.  ACM,  Montreal  QC 
Canada, 1–12. https://doi.org/10.1145/3173574.3173694
Dorton,  Stephen  L.,  and  Samantha  B.  Harper.  2022.  “A 
Naturalistic  Investigation  of  Trust,  AI,  and  Intelligence 
Work.”  Journal  of  Cognitive  Engineering  and  Decision 
222–236.  https://doi.org/10.1177/ 
(4): 
Making 
15553434221103718.

16

Ebeling,  Charles  E.  2019.  An  Introduction  to  Reliability  and 
Maintainability  Engineering.  Long  Grove,  IL:  Waveland 
Press.

Ferrario, Andrea, and Michele Loi. 2022. “How Explainability 
Contributes to Trust in AI.” In 2022 ACM Conference on 
Fairness,  Accountability,  and  Transparency,  June  20, 
2022.  ACM,  Seoul  Republic  of  Korea,  1457–1466.  https:// 
doi.org/10.1145/3531146.3533202

---

<!-- PAGE 14 -->

852

N. E. CETINKAYA AND N. KRÄMER

Geng,  Xiuli,  and  Xuening  Chu.  2012.  “A  new  Importance– 
Performance  Analysis  Approach 
for  Customer 
Satisfaction  Evaluation  Supporting  PSS  Design.”  Expert 
Systems  with  Applications  39  (1):  1492–1502.  https://doi. 
org/10.1016/j.eswa.2011.08.038.

Gunning,  David,  Mark  Stefik,  Jaesik  Choi,  Timothy  Miller, 
Simone  Stumpf,  and  Guang-Zhong  Yang.  2019.  “XAI— 
Explainable  Artificial  Intelligence.”  Science  Robotics  4  (37): 
eaay7120. https://doi.org/10.1126/scirobotics.aay7120.

Hendriks, Friederike, Dorothe Kienhues, and Rainer Bromme. 
2015.  “Measuring  Laypeople’s  Trust  in  Experts  in  a  Digital 
Age:  The  Muenster  Epistemic  Trustworthiness  Inventory 
(METI).”  PLoS  One  10  (10):  e0139309.  https://doi.org/10. 
1371/journal.pone.0139309.

Hong, Yili, Jiayi Lian, Li Xu, Jie Min, Yueyao Wang, Laura J. 
Freeman, and Xinwei Deng. 2022. “Statistical Perspectives 
on  Reliability  of  Artificial  Intelligence  Systems.”  Quality 
Engineering  35 
(1):  56–78.  https://doi.org/10.1080/ 
08982112.2022.2089854.

in  Artificial

Jacovi, Alon, Ana Marasović, Tim Miller, and Yoav Goldberg. 
2021.  Formalizing  Trust 
Intelligence: 
Prerequisites,  Causes  and  Goals  of  Human  Trust  in  AI. 
In Proceedings of the 2021 ACM Conference on Fairness, 
Accountability,  and  Transparency  (FAccT  ‘21,  March  03, 
2021.  ACM,  New  York,  NY,  USA,  624–635.  https://doi. 
org/10.1145/3442188.3445923

Jain, Lakshitha R, and Vineetha Menon. 2023. AI Algorithmic 
Bias:  Understanding  Its  Causes,  Ethical  and  Social 
Implications. In 2023 IEEE 35th International Conference 
on  Tools  with  Artificial  Intelligence  (ICTAI),  November 
06,  2023.  IEEE,  Atlanta,  GA,  USA,  460–467.  https://doi. 
org/10.1109/ICTAI59109.2023.00073

Johnson, Richard M, and Bryan K Orme. 2010. “Sample Size 
Issues  for  Conjoint  Analysis.”  In  Getting  Started  with 
Conjoint  Analysis:  Strategies  for  Product  Design  and 
Pricing  Research,  edited  by  Bryan  K  Orme,  57–66. 
Madison: Research Publishers.

Kaplan, Alexandra D., Theresa T. Kessler, J. Christopher Brill, 
and  P.  A.  Hancock.  2023.  “Trust  in  Artificial  Intelligence: 
Meta-analytic  Findings.”  Human  Factors:  The  Journal  of 
the  Human  Factors  and  Ergonomics  Society  65  (2):  337– 
359. https://doi.org/10.1177/00187208211013988.

Kieslich,  Kimon,  Birte  Keller,  and  Christopher  Starke.  2022. 
“AI-Ethics  by  Design.  Evaluating  Public  Perception  on 
the  Importance  of  Ethical  Design  Principles  of  AI.”  Big 
Data  &  Society  9  (1):  205395172210929.  https://doi.org/ 
10.1177/20539517221092956.

Knowles, Bran, and John T. Richards. 2021. “The Sanction of 
Authority: Promoting Public Trust in AI.” In Proceedings 
of the 2021 ACM Conference on Fairness, Accountability, 
and  Transparency  (FAccT  ‘21),  2021.  ACM,  New  York, 
NY,  USA,  262–271.  https://doi.org/10.1145/3442188. 
3445890

Krämer,  Nicole,  Magdalena  Wischnewski,  and  Emmanuel 
Müller.  2023.  “Interacting  with Autonomous  Systems  and 
Intelligent  Algorithms  –  new  Theoretical  Considerations 
on  the  Relation  of  Understanding  and  Trust.”  https://doi. 
org/10.31234/osf.io/h32ze.

Kunkel,  Johannes,  Thao  Ngo,  Jürgen  Ziegler,  and  Nicole 
Krämer. 2021. “Identifying Group-Specific Mental Models 
of  Recommender  Systems:  A  Novel  Quantitative 
– 
Approach.”

In  Human-Computer

Interaction

INTERACT  2021,  edited  by  Carmelo  Ardito,  Rosa 
Lanzilotti,  Alessio  Malizia,  Helen  Petrie,  Antonio 
Piccinno,  Giuseppe  Desolda,  and  Kori  Inkpen,  383–404. 
Cham:  Springer  International  Publishing.  https://doi.org/ 
10.1007/978-3-030-85610-6_23

Langer,  Markus,  Daniel  Oster,  Timo  Speith,  Holger 
Hermanns,  Lena  Kästner,  Eva  Schmidt,  Andreas  Sesing, 
and  Kevin  Baum.  2021.  “What  Do  We  Want  from 
Explainable  Artificial  Intelligence  (XAI)?  –  a  Stakeholder 
Perspective  on  XAI  and  a  Conceptual  Model  Guiding 
Interdisciplinary  XAI  Research.”  Artificial  Intelligence 
296:103473. https://doi.org/10.1016/j.artint.2021.103473.
LaRose,  Robert,  and  Nora  Rifon.  2006.  “Your  Privacy  Is 
Assured  -  of  Being  Disturbed:  Websites  with  and  without 
Privacy  Seals.”  New  Media  &  Society  8  (6):  1009–1029. 
https://doi.org/10.1177/1461444806069652.

Lee,  J.  D.,  and  K.  A.  See.  2004.  “Trust  in  Automation: 
Designing  for  Appropriate  Reliance.”  Human  Factors: 
The Journal of the Human Factors and Ergonomics Society 
46 (1): 50–80. https://doi.org/10.1518/hfes.46.1.50_30392.
Madhavan, P.,  and D. A. Wiegmann. 2007.  “Similarities and 
Differences  between  Human–Human  and  Human– 
Automation  Trust:  An  Integrative  Review.”  Theoretical 
Issues  in  Ergonomics  Science  8  (4):  277–301.  https://doi. 
org/10.1080/14639220500337708.

Marassi,  Lidia.  2023.  Assessing  User  Perceptions  of  Bias  in 
Generative  AI  Models:  Promoting  Social  Awareness  for 
Trustworthy  AI.  In  Proceedings  of  the  2023  Conference 
on Human Centered Artificial Intelligence: Education and 
Practice,  December  14,  2023.  ACM,  Dublin  Ireland,  46– 
46. https://doi.org/10.1145/3633083.3633094

Markus,  Aniek  F.,  Jan  A.  Kors,  and  Peter  R.  Rijnbeek.  2021. 
“The  Role  of  Explainability  in  Creating  Trustworthy 
Artificial  Intelligence  for  Health  Care:  A  Comprehensive 
the  Terminology,  Design  Choices,  and 
Survey  of 
Evaluation  Strategies.”  Journal  of  Biomedical  Informatics 
113:103655. https://doi.org/10.1016/j.jbi.2020.103655.

Mayer,  Roger  C.,  James  H.  Davis,  and  F.  David  Schoorman. 
1995.  “An  Integrative  Model  of  Organizational  Trust.” 
The  Academy  of  Management  Review  20  (3):  709–734. 
https://doi.org/10.2307/258792.

Mehrotra,

Siddharth,  Chadha  Degachi,  Oleksandra 
Vereschak,  Catholijn  M.  Jonker,  and  Myrthe  L.  Tielman. 
2024.  “A  Systematic  Review  on  Fostering  Appropriate 
Trust  in  Human-AI  Interaction:  Trends,  Opportunities 
and  Challenges.”  ACM  Journal  on  Responsible  Computing 
1: 26. https://doi.org/10.1145/3696449.

Mishra,  Saurabh,  Anand  Rao,  Ramayya  Krishnan,  Bilal 
Ayyub,  Amin  Aria,  and  Enrico  Zio.  2024.  “Reliability, 
Resilience 
for 
Trustworthy  AI  Systems.”   arXiv  preprint.  https://doi.org/ 
10.48550/arXiv.2411.08981.

and  Human  Factors  Engineering

Ngo, Thao, and Nicole Krämer. 2021. “Exploring Folk Theories 
of  Algorithmic  News  Curation  for  Explainable  Design.” 
Behaviour  &  Information  Technology  41  (15):  3346–3359. 
https://doi.org/10.1080/0144929X.2021.1987522.

Ngo,  Thao,  Johannes  Kunkel,  and  Jürgen  Ziegler.  2020. 
and 
“Exploring  Mental  Models 
Controllable  Recommender  Systems:  A  Qualitative 
Study.”  Proceedings  of  the  28th  ACM  Conference  on  User 
Modeling,  Adaptation  and  Personalization,  July  07,  2020.

for  Transparent

---

<!-- PAGE 15 -->

ACM,  Genoa  Italy,  183–191.  https://doi.org/10.1145/ 
3340631.3394841

the  Usefulness  and 
Features

Norkute,  Milda,  Nadja  Herger,  Leszek  Michalak,  Andrew 
Mulder,  and  Sally  Gao.  2021.  Towards  Explainable  AI: 
Impact  of  Added 
Assessing 
Explainability 
Document 
Legal 
Summarization.  In  Extended  Abstracts  of  the  2021  CHI 
Conference  on  Human  Factors  in  Computing  Systems, 
May  08,  2021.  ACM,  Yokohama  Japan,  1–7.  https://doi. 
org/10.1145/3411763.3443441

in

Nourani,  Mahsan,  Samia  Kabir,  Sina  Mohseni,  and  Eric  D. 
Ragan. 2019.  “The Effects of Meaningful and Meaningless 
Explanations  on  Trust  and  Perceived  System  Accuracy  in 
Intelligent  Systems.”  Proceedings  of  the  AAAI  Conference 
on  Human  Computation  and  Crowdsourcing  7:97–105. 
https://doi.org/10.1609/hcomp.v7i1.5284.

Obermeyer, Ziad, Brian Powers, Christine Vogeli, and Sendhil 
Mullainathan.  2019.  “Dissecting  Racial  Bias 
in  an 
Algorithm  Used  to  Manage  the  Health  of  Populations.” 
Science  366  (6464):  447–453.  https://doi.org/10.1126/ 
science.aax2342.

Orme, Bryan K. 2010. Getting Started with Conjoint Analysis: 
for  Product  Design  and  Pricing  Research.

Strategies 
Madison: Research Publisher LCC.

Paaß, Gerhard and Dirk Hecker. 2020. KI und ihre Chancen, 
Herausforderungen und Risiken. In Künstliche Intelligenz. 
Wiesbaden:  Springer  Vieweg,  375–444.  https://doi.org/10. 
1007/978-3-658-30211-5_10.

Peña, Alejandro, Ignacio Serna, Aythami Morales, and Julian 
Fierrez.  2020.  “FairCVtest  Demo:  Understanding  Bias  in 
Multimodal  Learning  with  a  Testbed  in  Fair  Automatic 
Recruitment.”  In  Proceedings  of  the  2020  International 
Conference on  Multimodal Interaction,  October 21, 2020. 
ACM,  Virtual  Event  Netherlands,  760–761.  https://doi. 
org/10.1145/3382507.3421165

Pierce,  Robin  L,  Wim  Van  Biesen,  Daan  Van  Cauwenberge, 
Johan  Decruyenaere, 
2022. 
and 
Explainability  in  medicine  in  an  era  of  AI-based  clinical 
decision  support  systems.  Frontiers 
in  Genetics.  13: 
903600. https://doi.org/10.3389/fgene.2022.903600.

Sterckx.

Sigrid

Poursabzi-Sangdeh,  Forough,  Daniel  G  Goldstein,  Jake  M 
Hofman,  Jennifer  Wortman  Wortman  Vaughan,  and 
Hanna  Wallach.  2021.  Manipulating  and  Measuring 
Model  Interpretability.  In  Proceedings  of  the  2021  CHI 
Conference  on  Human  Factors  in  Computing  Systems 
(CHI  ‘21),  2021.  ACM,  New  York,  NY,  USA,  1–52. 
https://doi.org/10.1145/3411764.3445315

Ryan,  Mark.  2020.  “In  AI  We  Trust:  Ethics,  Artificial 
Intelligence,  and  Reliability.”  Science  and  Engineering 
Ethics  26  (5):  2749–2767.  https://doi.org/10.1007/s11948- 
020-00228-y.

Saeed, Waddah, and Christian Omlin. 2023. “Explainable AI 
(XAI):  A  Systematic  Meta-survey  of  Current  Challenges 
and  Future  Opportunities.”  Knowledge-Based  Systems 
263:110273. https://doi.org/10.1016/j.knosys.2023.110273.
Scharowski,  Nicolas,  Michaela  Benk,  Swen  J.  Kühne,  Léane 
Wettstein,  and  Florian  Brühlmann.  2023.  “Certification 
Labels  for  Trustworthy  AI:  Insights  From  an  Empirical 
Mixed-Method  Study.”  In  Proceedings  of  the  2023  ACM 
Conference 
and 
Transparency  (FAccT  ‘23),  2023.  ACM,  Chicago  IL  USA, 
248–260. https://doi.org/10.1145/3593013.3593994

Accountability,

Fairness,

on

BEHAVIOUR & INFORMATION TECHNOLOGY

853

Schlicker,  Nadine  and  Markus  Langer.  2021.  “Towards 
Warranted  Trust:  A  Model  on  the  Relation  Between 
In 
Actual  and  Perceived  System  Trustworthiness.” 
Proceedings  of  Mensch  und  Computer  2021  (MuC  ‘21), 
2021.  ACM,  Ingolstadt  Germany,  325–329.  https://doi. 
org/10.1145/3473856.3474018

Sheth,  Amit,  Manas  Gaur,  Kaushik  Roy,  and  Keyur 
Language 
2021. 
Faldu. 
Understanding 
for  Explainable  AI.”  IEEE  Internet 
Computing  25  (5):  19–24.  https://doi.org/10.1109/MIC. 
2021.3101919.

“Knowledge-Intensive

Shin,  Donghee.  2021.  “The  Effects  of  Explainability  and 
Causability  on  Perception,  Trust,  and  Acceptance: 
Implications  for  Explainable  AI.”  International  Journal  of 
Human-Computer  Studies  146:102551.  https://doi.org/10. 
1016/j.ijhcs.2020.102551.

Shin,  Donghee,  and  Yong  Jin  Park.  2019.  “Role  of  Fairness, 
Accountability, 
in  Algorithmic 
and  Transparency 
Affordance.”  Computers  in  Human  Behavior  98:277–284. 
https://doi.org/10.1016/j.chb.2019.04.019.

Sindermann,  Cornelia,  Peng  Sha,  Min  Zhou,  Jennifer 
Wernicke,  Helena  S.  Schmitt,  Mei  Li,  Rayna  Sariyska, 
Maria  Stavrou,  Benjamin  Becker,  and  Christian  Montag. 
2021. 
towards  Artificial 
the  Attitude 
Intelligence:  Introduction  of  a  Short  Measure  in  German, 
-  Künstliche 
Chinese,  and  English  Language.”  KI 
Intelligenz  35 
(1):  109–118.  doi:10.1007/s13218-020- 
00689-0

“Assessing

Sperber,  Dan,  Fabrice  Clément,  Christophe  Heintz,  Olivier 
Mascaro,  Hugo  Mercier,  Gloria  Origgi,  and  Deirdre 
Wilson.  2010.  “Epistemic  Vigilance.”  KI  -  Künstliche 
Intelligenz  25 
(4):  359–393.  https://doi.org/10.1007/ 
s13218-020-00689-0

Springer,  Aaron,  and  Steve  Whittaker.  2020.  “Progressive 
Disclosure:  When,  Why,  and  How  Do  Users  Want 
Algorithmic 
ACM 
Transactions  on  Interactive  Intelligent  Systems  10  (4):  1– 
32. https://doi.org/10.1145/3374218.

Information?”

Transparency

Sullivan,  Yulia,  Marc  De  Bourmont,  and  Mary  Dunaway. 
2022.  “Appraisals  of  Harms  and  Injustice  Trigger  an 
Eerie  Feeling  That  Decreases  Trust 
in  Artificial 
Intelligence  Systems.”  Annals  of  Operations  Research  308 
(1-2): 525–548. https://doi.org/10.1007/s10479-020-03702- 
9.

Varona, Daniel, and Juan Luis Suárez. 2022. “Discrimination, 
Bias,  Fairness,  and  Trustworthy  AI.”  Applied  Sciences 
12:5826. https://doi.org/10.3390/app12125826.

Wang,  Ning,  David  V.  Pynadath,  and  Susan  G.  Hill.  2015. 
in  a  Human-Robot  Team  with 
“Building  Trust 
Automatically  Generated  Explanations.”  In  Proceedings  of 
the interservice/industry training, simulation and education 
conference (I/ITSEC) 15315: 1–12.

Weitz,  Katharina,  Dominik  Schiller,  Ruben  Schlagowski, 
Tobias  Huber,  and  Elisabeth  André.  2019.  “Do  you  trust 
me?": Increasing User-Trust by Integrating Virtual Agents 
in  Explainable  AI  Interaction  Design.”  In  Proceedings  of 
the  19th  ACM  International  Conference  on  Intelligent 
Virtual  Agents  (IVA  ’19),  7–9.  New  York,  NY,  USA: 
Association  for  Computing  Machinery.  https://doi.org/10. 
1145/3308532.3329441.

Wing, Jeannette M. 2021. Trustworthy AI. Commun. ACM 64, 
10 (October 2021), 64–71. https://doi.org/10.1145/3448248

---

<!-- PAGE 16 -->

854

N. E. CETINKAYA AND N. KRÄMER

Wischnewski,  Magdalena,  Nicole  Krämer,  and  Emmanuel 
Müller.  2023.  Measuring  and  Understanding  Trust 
Calibrations  for  Automated  Systems:  A  Survey  of  the 
State-Of-The-Art  and  Future  Directions.  In  Proceedings 
of  the  2023  CHI  Conference  on  Human  Factors  in 
Computing  Systems  (CHI  ‘23),  2023.  Association  for 
Computing  Machinery,  New  York,  NY,  USA,  1–16. 
https://doi.org/10.1145/3544548.3581197

Zhou,  Jianlong,  Fang  Chen,  and  Andreas  Holzinger.  2022. 
Towards  Explainability  for  AI  Fairness.  In  xxAI  -  beyond

Explainable  AI,  Andreas  Holzinger,  Randy  Goebel,  Ruth 
Fong,  Taesup  Moon,  Klaus-Robert  Müller  and  Wojciech 
Samek.  Springer  International  Publishing,  Cham,  375– 
386. https://doi.org/10.1007/978-3-031-04083-2_18

Zhou, Jianlong, Sunny Verma, Mudit Mittal, and Fang Chen. 
2021.  Understanding  Relations  Between  Perception  of 
Fairness  and  Trust  in  Algorithmic  Decision  Making.  In 
8th  International  Conference  on  Behavioral  and  Social 
Computing  (BESC),  October  29,  2021.  IEEE,  Doha, 
Qatar, 1–5

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Behaviour & Information Technology
ISSN: 0144-929X (Print) 1362-3001 (Online) Journal homepage: www.tandfonline.com/journals/tbit20
Between transparency and trust: identifying key
factors in AI system perception
Nur Efsan Cetinkaya & Nicole Krämer
To cite this article: Nur Efsan Cetinkaya & Nicole Krämer (2026) Between transparency and
trust: identifying key factors in AI system perception, Behaviour & Information Technology,
45:5, 840-854, DOI: 10.1080/0144929X.2025.2533358
To link to this article: https://doi.org/10.1080/0144929X.2025.2533358
© 2025 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 20 Jul 2025.
Submit your article to this journal
Article views: 7271
View related articles
View Crossmark data
Citing articles: 11 View citing articles
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tbit20

BEHAVIOUR & INFORMATION TECHNOLOGY
2026, VOL. 45, NO. 5, 840–854
https://doi.org/10.1080/0144929X.2025.2533358
Between transparency and trust: identifying key factors in AI system perception
Nur Efsan Cetinkayaa,b and Nicole Krämera,b
aSocial Psychology: Media and Communication, University of Duisburg-Essen, Duisburg, Germany; bResearch Center Trustworthy Data Science
and Security, Dortmund, Germany
ABSTRACT ARTICLE HISTORY
With the deployment of AI systems across multiple domains, understanding how users develop Received 25 April 2025
trust has becomecrucial for successful implementation. This study investigates how different AI Accepted 7 July 2025
features influence the decision to use an AI system and which characteristics users prioritise
when evaluating them. We focus on whether users prefer systems whose functioning they can KEYWORDS
Artificial intelligence; XAI;
understand or whose trustworthiness is certified. We examined whether users favour system
trust in AI; reliability; fairness
transparency through explainability features or rely more on external trust signals, such as AI
certification seals, while considering how these preferences interact with technical reliability and
fairness. Using conjoint analysis, we systematically compared the influence of four key attributes
(transparency by explainability features, technical reliability, external trust signals through AI
certifications, and fairness) on user decisions to use an AI system. Through cluster analysis, we
identified two groups with opposing preferences and demographic differences. The first group
prioritised high explainability and strong AI certification while showing negative preferences for
fairness, whereas the second group favoured fairness and reliability while displaying negative
attitudes toward explainability and AI certification. These contrasting prioritisation patterns raise
important questions about AI systems development, particularly regarding challenges of
addressing competing user requirements for trust-related features.
1 Introduction
users now have additional external indicators to con-
The use of artificial intelligence (AI) has grown rapidly sider alongside system attributes. This creates a complex
in recent years, fundamentally transforming various decision environment where understanding the relative
aspects of society. As AI becomes more deeply inte- importance of each attribute becomes crucial for both
grated into daily life, understanding how users evaluate theory and practice.
and choose to adopt AI systems becomes increasingly The relationship between understanding and trust in
critical. Research has extensively investigated various AI systems presents a fundamental tension in user
attributes that influence AI adoption and trust, examin- adoption decisions. While some researchers argue that
ing factors such as system explainability (Wing 2021), understanding AI systems through explainability leads
reliability (Ryan 2020), and fairness (Varona and Suárez to increased user (Shin 2021; Weitz et al. 2019), others
2022). While these individual studies have provided suggest that external trust mechanisms may be equally
valuable insights, they predominantly examine each or more important (Krämer, Wischnewski, and Müller
attribute in isolation, leaving a critical gap in our under- 2023). The latter assumption is based on the observation
standing of how these attributes interact and compare in that users might show unwillingness (Ngo and Krämer
importance when users make actual adoption decisions. 2021) or inability (Bromme and Gierth 2021) to under-
This gap is particularly significant as users in practice stand complex functioning and issues. This leads to the
must evaluate multiple attributes simultaneously, not in important question whether users prefer to understand
isolation. When deciding whether to adopt an AI system AI systems directly, or whether they are willing to rely
in high-stakes scenarios, users cannot consider explain- more heavily on external validations of trustworthiness.
ability without also weighing factors like reliability and Research has identified several key attributes that
fairness. Moreover, with the emergence of trust signals influence AI adoption. Explainability enables users to
such as AI certification seals (Scharowski et al. 2023), understand system decisions (Sheth et al. 2021), while
CONTACT Nur Efsan Cetinkaya nur.cetinkaya@uni-due.de Social Psychology: Media and Communication, University of Duisburg-Essen, Bismarckstraße
120, 47057 Duisburg, Germany
© 2025 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use,
distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this article has been published allow the posting of the Accepted
Manuscript in a repository by the author(s) or with their consent.

BEHAVIOUR & INFORMATION TECHNOLOGY 841
reliability ensures consistent performance under specific adoption. While trust encompasses users’ subjective
conditions (Hong et al. 2022). External trust signals, perceptions of a system’s reliability, trustworthiness
such as AI seals of approval, offer third-party validation refers to the system’s objective characteristics, including
of system quality (Scharowski et al. 2023), particularly its technical capabilities and performance (Schlicker and
valuable for non-expert users (LaRose and Rifon Langer 2021). This distinction is crucial for understand-
2006). Fairness, defined as the equitable treatment of ing how users interact with and accept AI technologies
diverse user groups, has emerged as another critical across various fields.
consideration as AI systems increasingly make decisions It is also important to distinguish between trust and
that affect different populations. The growing awareness reliance, as these concepts, while related, are not identi-
of algorithmic bias and its potential societal impacts has cal. In accordance with the findings of Lee and See (Lee
made fairness a key factor in users’ evaluation of AI sys- and See 2004), trust can be defined as users’ subjective
tems (Bartneck et al. 2021). Each of these attributes perception and attitude towards a system’s reliability.
potentially influences users’ willingness to adopt AI sys- In contrast, reliance can be defined as the actual behav-
tems, yet their relative importance remains unclear. ioural outcome of adopting or using the system. This
To address these questions, our study employs con- distinction is crucial to the present study, as it examines
joint analysis to examine how users weigh different AI users’ choices between different AI systems (a form of
system attributes when making adoption decisions in intended reliance) rather than directly measuring their
high-stakes scenarios. This methodological approach is trust attitudes. While trust is known to influence
particularly well-suited for our research as it requires reliance, other factors may also affect the decision to
participants to make realistic trade-offs between differ- use a system. This highlights the importance of consid-
ent system attributes, revealing their true preferences ering both concepts when examining AI adoption (Lee
more accurately than direct questioning. While our and See 2004).
study does not directly measure trust, it operates on The theoretical foundation for understanding trust
the premise that user preferences for these attributes in AI systems largely derives from Mayer et al.’s
indicate what users value most when deciding whether (Mayer, Davis, and David Schoorman 1995) model of
to adopt an AI system. organisational trust, which posits that trust develops
Our research focuses particularly on the interplay based on a trustor’s perceptions of a trustee’s ability,
between understanding and trust, whether users prefer benevolence, and integrity. Recognising that this
to understand AI systems directly through explainabil- organisational model may not perfectly translate to
ity, or whether they rely more heavily on external human-machine interactions (Madhavan and Wieg-
trust signals such as certifications. By examining these mann 2007), Lee and See (Lee and See 2004) adapted
factors alongside reliability and fairness, we aim to pro- it specifically for automation contexts. In their frame-
vide insights that can guide both theoretical develop- work, trust assessment relies on three key aspects: the
ment and practical implementation of AI systems. For machine’s reliability and functionality (ability = per-
organisations developing AI systems for critical appli- formance), the intentions behind its design (benevo-
cations, understanding which attributes most strongly lence = purpose), and its intelligibility (integrity =
influence user acceptance can guide resource allocation process). They conceptualise trust in automation as
and development priorities. For researchers, insights the belief that a machine will help achieve one’s objec-
into how these attributes interact can inform more com- tives, particularly in situations involving uncertainty
prehensive models of AI adoption and trust. and risk.
Building on this foundation, research has explored
various aspects of trust formation in technological sys-
2 Theoretical background
tems. One important consideration is epistemic trust,
Given the increasing use of artificial intelligence (AI) which represents the confidence users place in experts
systems in decision-making processes, there is a grow- or institutions based on their perceived competence
ing need to understand how users develop trust in and integrity (Sperber et al. 2010). This concept high-
these systems as well as what is affecting their adoption lights how trust in AI systems can be influenced by
decision. users’ faith in the system’s developers and implementing
organisations. Another crucial aspect in trust develop-
ment is the concept of calibrated trust, which examines
2.1 Trust development in AI systems
the alignment between users’ trust levels and a system’s
Trust and trustworthiness represent fundamental yet actual reliability (Wischnewski, Krämer, and Müller
distinct concepts in the context of artificial intelligence 2023). This alignment is essential for ensuring

842 N. E. CETINKAYA AND N. KRÄMER
appropriate reliance on AI systems, as both over-trust sufficient knowledge in all relevant socio-scientific
and under-trust can lead to suboptimal outcomes. issues (inability, [ Bromme and Gierth 2021]).
Recent research has further differentiated between Instead of building on understanding, Bromme and
understanding and trust as distinct outcomes in Gierth (Bromme and Gierth 2021) propose to shift the
human-AI interaction (De Brito Duarte et al. 2023). (too complicated) question of what to believe or to
Understanding refers to comprehending the operational know, respectively, to the less demanding but equally
mechanisms of AI systems, while trust represents confi- rational question of whom to trust. This form of ‘episte-
dence in the system’s outputs. This distinction is par- mic trust’ (Sperber et al. 2010) is exemplified in trust
ticularly relevant when examining the roles of seals. Trust seals, therefore, offer an alternative pathway
explainability and trust seals in fostering user trust. to building trust through institutional validation rather
than direct understanding. These trust cues, which
include certifications and seals of approval from repu-
2.2 Understanding versus trust: explainability
table organisations, provide users with tangible signals
and trust seals
of an AI system’s credibility and security (Scharowski
Explainability and trust seals represent two fundamen- et al. 2023). AI certifications represent formal recog-
tally different approaches to building trust in AI sys- nition from independent third parties that a system
tems. Recently, and in line with considerable efforts of meets predefined standards through thorough evalu-
the explainable AI (XAI) community (Das and Rad ation and auditing. These certifications aim to address
2020; Gunning et al. 2019; Langer et al. 2021; Norkute the inherent complexity and uncertainty of AI systems
et al. 2021; Saeed and Omlin 2023), explainability, by providing clear indicators of trustworthiness (Wisch-
defined as the ability to attribute comprehensible and newski, Krämer, and Müller 2023).
interpretable reasons for an AI’s decisions and actions, The effectiveness of trust seals is supported by research
has been widely recognised as an essential prerequisite suggesting that public trust primarily requires robust
for building user trust. It provides users with a deeper regulatory oversight rather than technical understanding
understanding of AI behaviour and reduces perceived (Knowles and Richards 2021). This includes the establish-
risks and uncertainties (Shin and Park 2019). A signifi- ment of authoritative bodies to enforce compliance with
cant body of research highlights that explainability is ethical standards and validate AI systems’ trustworthiness
crucial for establishing AI trustworthiness (Caspers through mandatory conformity assessments and algorith-
2021; Jacovi et al. 2021). mic auditing (Afroogh et al. 2024). This approach
However, research regarding the relationship acknowledges that users often rely more effectively on
between explainability and trust has yielded complex institutional validation (‘whom to trust’) than personal
and sometimes contradictory findings. While some understanding (‘what to know’) when confronting com-
studies demonstrate that human-understandable expla- plex socio-scientific issues (Bromme and Gierth 2021).
nations can enhance user comprehension and increase Recent research has begun to differentiate between
trust in AI performance (Nourani et al. 2019; Wang, understanding and trust as distinct outcomes in
Pynadath, and Hill 2015), others reveal a more nuanced human-AI interaction (De Brito Duarte et al. 2023).
dynamic. Ferrario and Loi (Ferrario and Loi 2022) While understanding involves comprehending oper-
found that enhancing system comprehension through ational mechanisms, trust represents confidence in sys-
explainability may actually result in decreased trust, as tem outputs. The influence of explainability on these
users gain deeper insights into system limitations and outcomes varies: detailed technical explanations can
potential failure modes, leading to a more critical per- enhance understanding while potentially reducing blind
spective of the system’s capabilities. In addition, the trust, leading to more informed and appropriate levels
attempt to foster a better understanding of system capa- of reliance on the system (Mehrotra et al. 2024). This dis-
bilities might be met with people’s unwillingness or tinction helps explain why increased explainability does
inability to understand (Krämer, Wischnewski, and not automatically translate to increased trust and suggests
Müller 2023). Here, it has been demonstrated that that the goal should be to foster informed trust rather
users sometimes do not want to understand algorithmic than maximising trust indiscriminately.
systems as they, for example, avoid to be scared off their Despite extensive research on both mechanisms,
usage (unwillingness, [ Ngo and Krämer 2021]). Also, there remains a significant gap in understanding how
systems are increasingly complex to understand and users weigh explainability against trust seals when eval-
merely a small part of everyday life problems that uating AI systems. This study addresses this gap by
might be important to understand (e.g. climate change, directly comparing these approaches while considering
vaccines), so that people are not able to achieve additional influential factors.

BEHAVIOUR & INFORMATION TECHNOLOGY 843
2.3 Additional factors: reliability and fairness 2.4 Hypotheses and research questions
While our primary focus remains on the interplay Building on this theoretical framework, we identify sev-
between explainability and trust seals, we include eral key research gaps regarding how users prioritise
reliability and fairness as critical additional factors to different trust-building mechanisms in AI systems.
provide a more comprehensive understanding of While extensive research exists on individual factors,
trust-building mechanisms in AI systems. there is limited understanding of how users weigh
Reliability is defined as the probability that a system these factors against each other, particularly in the con-
will fulfill its desired function under specific conditions text of explainability versus institutional validation
over a designated period (Ebeling 2019). In the litera- through trust seals.
ture, reliability and robustness are often used inter- A study has shown that fairness and performance are
changeably, though reliability specifically emphasises equally important to respondents whereas explainability
the temporal aspect of system performance (Hong is slightly less important (Kieslich, Keller, and Starke
et al. 2022). The concept has emerged as a crucial factor 2022). These findings also show the importance of
in ensuring the security and accuracy of AI-based sys- reliability, since reliability is often categorised as a per-
tems (Belgaum et al. 2021), with reliability being closely formance related factor (Kaplan et al. 2023). Further-
intertwined with performance metrics, particularly more, Kaplan et al. (Kaplan et al. 2023) demonstrated
accuracy (Mishra et al. 2024). Research shows a strong in their meta-analysis of trust in AI systems, reliability
correlation between reliability levels and user trust and was identified as one of the most heavily weighted fac-
adoption rates (Kaplan et al. 2023). In this study, tors concerning the AI component. This is particularly
reliability therefore is included as a potential ‘gold stan- evident in high-risk decision-making scenarios, where
dard’ for selecting a system to use. reliability emerges as the primary determinant of system
Fairness, albeit a newer consideration in AI system adoption (Chancey et al. 2017). Therefore, the following
development, has gained significant attention due to hypothesis is proposed:
its implications for user trust and system adoption.
H1: People will prefer reliability over fairness and
Research demonstrates that users’ trust in AI systems
explainability.
is significantly influenced by their perceptions of algo-
rithmic fairness (Sullivan, De Bourmont, and Dunaway The relationship between explainability and trust
2022). When AI systems demonstrate equitable treat- seals presents a particularly interesting area for further
ment across different demographic groups, users are examination. Explainability helps people to gain a dee-
more likely to develop and maintain trust in these tech- per understanding of the decision-making process of
nologies. Conversely, instances of algorithmic discrimi- an AI system (Zhou, Chen, and Holzinger 2022). In
nation can severely undermine user trust and impede AI contrast, trust seals represent an external seal of
adoption (Zhou et al. 2021). Algorithmic bias can mani- approval that validates trust in the system without
fest in various forms, often stemming from historical requiring understanding of its internal mechanisms
inequities in training data or inherent flaws in algorithm (Cremers et al. 2019; Paaß and Hecker 2020). This dis-
design (Jain and Menon 2023). For example, studies tinction raises an important question about whether
have documented cases where AI systems exhibited dis- people prefer to understand the functioning of the sys-
criminatory patterns in healthcare diagnostics (Ober- tem or whether they are ready to trust a system which
meyer et al. 2019) and hiring decisions (Peña et al. has been certified as safe and trustworthy by a third
2020). Users who encounter or become aware of such party.
biases are significantly less likely to trust and engage Building on the previously discussed framework of
with AI systems, regardless of their technical capabilities epistemic trust, research has shown that human under-
(Marassi 2023). standing of algorithmic functioning is limited, with
The inclusion of these additional factors allows us to users frequently developing only superficial mental
evaluate how users prioritise different trust-building models of AI systems (DeVito et al. 2018; Kunkel
mechanisms while acknowledging that reliability and et al. 2021; Ngo et al. 2020). While explanations might
fairness play important roles in the broader context contribute to understanding, trust seals could poten-
of AI system adoption. This approach enables us to tially offer a more direct path to achieving calibrated
better understand the relative importance of our pri- trust, particularly when issued by competent insti-
mary variables – explainability and trust seals – within tutions perceived as both honest and well-meaning
the larger landscape of factors influencing user trust in (Hendriks, Kienhues, and Bromme 2015). This is
AI systems. especially important given that research has shown

844 N. E. CETINKAYA AND N. KRÄMER
that providing extensive explanations can sometimes complex. For example, high explainability might com-
decrease users’ ability to detect and correct system mis- pensate for lower reliability or might mitigate concerns
takes (Poursabzi-Sangdeh et al. 2021). Furthermore, about fairness. It can be concluded that certain attri-
studies have shown that users sometimes actively butes may exert a more profound influence on trust
avoid detailed system information, fearing that than others. For instance, reliability is frequently
increased knowledge about data processing might dis- regarded as a foundational attribute (Hong et al.
courage future use (Ngo and Krämer 2021; Springer 2022), yet fairness can also assume an important role
and Whittaker 2020). This behavioural pattern, com- contingent on the context. An understanding of the
bined with the cognitive demands of processing com- relative influence of different attributes can assist AI
plex technical information, suggests that trust seals developers in directing their efforts towards the most
might provide a more accessible means of fostering impactful areas. For instance, if it is demonstrated that
appropriate trust levels. Based on these considerations, performance and fairness significantly enhance trust,
we hypothesise that people will prefer trust seals over designers may prioritise these features, even if achieving
explanations when establishing trust in AI systems. absolute reliability is challenging. This research question
Therefore, the following hypothesis is proposed: emphasises the necessity of a user-centred approach to
the design of AI systems, whereby user trust consider-
H2: People will prefer trust seal over explanations.
ations should guide the development process. It also
However, for the AI system to be trusted by the users, aims to identify which individual attributes or combi-
the AI’s trustworthiness must be truly perceived by nations thereof have the most significant impact on
them. This requires certain cues to be provided to the trust. Therefore, we propose the following research
users, which could be achieved through proper docu- question:
mentation. Therefore, other non-technical axiological RQ: which combinations of attributes will be preferred
factors for building trust, especially human-related the most?
ones, could be engineered to enhance trust without
the need to improve the trustworthiness of AI (Afroogh
2.5. RQ: which combinations of attributes will be
et al. 2024). These axiological factors could be trust cues
preferred the most?
in the form of AI seals and also enabling fair and
unbiased AI systems. Therefore, the following hypoth- 3 Method
esis is proposed:
The study design as well as the hypotheses were prere-
H3: People will prefer communicated trustworthiness, gistered on the Open Science Framework (OSF) prior
enhanced through proper documentation (AI seal), to data collection in November 2024 (https://osf.io/
over actual technical trustworthiness (reliability and
mw4dq/?view_only = 04327e74dfa34e4ca2babc170e86c
fairness).
048). All study materials, including instructions and
The degree of trust placed in AI is not a simple, uni- data, are publicly available in the associated project
versal phenomenon. Rather, it is a multifaceted and repository. An approval by the responsible ethics com-
context-specific construct (Chen 2021). It is possible mittee of the University Duisburg-Essen was given to
that users may assign differential weights to different conduct the study. Statistical data analysis was per-
attributes, depending on the specific application and formed using version 29 of IBM SPSS Statistics software
their individual concerns (Dorton and Harper 2022). for Windows (IBM Corp., 2023) and Python (Version
For instance, in the context of healthcare, explainability 3.9.6)
and performance are of paramount importance,
whereas in customer service, user satisfaction may be
3.1 Measures
the overarching concern (Geng and Chu 2012; Markus,
Kors, and Rijnbeek 2021; Pierce et al. 2022). 3.1.1 Choice-Based conjoint analysis
The degree of trust placed in AI is influenced by a The present study employed choice-based conjoint
number of factors, including the explainability, analysis (CBC) to systematically evaluate participants’
reliability, trust cues like AI seals and fairness of the trust preferences between different AI system configur-
technology in question. Each attribute contributes to ations in healthcare decision-making. The CBC is a
overall trust in a distinct manner (Angerschmid et al. method of presenting choice scenarios to participants,
2022; De Brito Duarte et al. 2023; Dorton and Harper who are required to make trade-offs between attributes.
2022; Shin 2021; Wischnewski, Krämer, and Müller The method has been developed for the purpose of iden-
2023). The interaction between attributes can be tifying true preference structures and determining the

BEHAVIOUR & INFORMATION TECHNOLOGY 845
relative importance attributed to distinct characteristics. systematic variation of attribute levels across profiles
Despite its apparent simplicity, CBC is an effective enabled the subsequent estimation of part-worth utilities
method of capturing real-world decision processes by and relative importance weights for each attribute and
forcing users to make concrete trade-offs rather than level in trust formation.
rating features in isolation (Orme 2010). Prior to com-
mencing the choice tasks, participants were presented 3.1.2 Additional measures
with comprehensive instructions and a healthcare
Attitude towards Artificial Intelligence was measured
decision scenario that framed their evaluation specifically
using the German version of the Attitude Towards
in terms of trust. The scenario described an AI system
Artificial Intelligence (ATAI) scale developed by Sinder-
designed to assist with important health decisions,
mann et al. (Sindermann et al. 2021). The scale consists
including treatment selection, health data monitoring,
of five items assessing two dimensions: Acceptance (2
and personalised health advice. Participants were
items) and Fear (3 items) of Artificial Intelligence (e.g.
instructed to deliberate on which AI system profile they
‘Artificial intelligence will benefit humankind’). Partici-
would entrust with greater confidence, contemplating
pants responded on an 11-point Likert scale ranging
the potential hazards of imprecise or prejudiced rec-
from 0 (‘strongly disagree’) to 10 (‘strongly agree’).
ommendations within healthcare contexts. The exper-
The subscales demonstrated acceptable reliability in
imental design incorporated four key attributes with
our sample, with Cronbach’s α = .66 for Acceptance
varying levels: explainability (three levels: no explainabil-
and α = .70 for Fear.
ity, low explainability, high explainability), reliability
(two levels: medium reliability at 65%, high reliability at
99%), trust cues (three levels: no AI seal, low AI seal, 3.2 Procedure
high AI seal), and fairness (two levels: low fairness,
The online study was conducted on the SoSci-Survey
high fairness). To ensure a comprehensive understanding
platform. Prior to the commencement of the study, par-
of the experimental design, participants received detailed
ticipants were provided with a detailed instruction and
descriptions of each attribute and its associated levels,
asked to give consent. Following this, consent to partici-
with definitions readily available throughout the study
pate was obtained. Participants then completed a
for reference. The design generated 36 unique attribute
choice-based conjoint analysis to assess their trust pre-
combinations, which were presented across 18 discrete
ferences in AI healthcare systems. Following this, they
choice tasks (i.e. every participant had to make 18 choices
responded to a questionnaire measuring their attitudes
between to system descriptions each). In each task, par-
toward artificial intelligence, specifically focusing on
ticipants were shown two competing AI system profiles
AI acceptance and fear of AI. The survey concluded
simultaneously and were required to indicate which sys-
with the collection of socio-demographic information,
tem they would trust more based on the presented attri-
including gender, age, educational qualifications, and
butes (see Figure 1). This forced-choice methodology
employment status. Upon completion of all study com-
enabled the assessment of how different attribute combi-
ponents, participants received a debriefing that outlined
nations influenced participants’ trust decisions. The
the study’s objectives and purpose. The entire procedure
Figure 1. Example of a choice task in the conjoint analysis study.

846  N. E. CETINKAYA AND N. KRÄMER
was conducted in German to ensure participants could  Table 1. Logistic regression.
fully understand and respond to all materials in their  Total sample. (n   Cluster 1. (n =   Cluster 2. (n =
|     |     |     |     |     |     | = 315) |     | 182) |     | 133) |
| --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- | ---- |
native language.
|            |     |     |     | Explainability    |     | 0.0042 |     | 0.1447***  | −0.1899*** |     |
| ---------- | --- | --- | --- | ----------------- | --- | ------ | --- | ---------- | ---------- | --- |
|            |     |     |     | Reliability       |     | 0.0183 |     | −0.0669    | 0.1371*    |     |
|            |     |     |     | AI certification  |     | 0.0111 |     | 0.1926***  | −0.2395*** |     |
| 3.3 Sample |     |     |     | seal              |     |        |     |            |            |     |
|            |     |     |     | Fairness          |     | 0.0155 |     | −0.2692*** | 0.4090***  |     |
The data collection process was carried out through an  Results show regression coefficients (β) that indicate attribute preferences
online study implemented on the SoSci-Survey platform.  within each cluster based on logistic regression analysis. Positive coeffi-
cients indicate positive preferences for an attribute, while negative coeffi-
The required sample size was calculated using Johnson
cients indicate negative preferences. Statistical significance determined by
z-tests. P-values indicate significance levels: *p < 0.05, **p < 0.01, ***p <
and Orme’s (Johnson and Orme 2010) formula, which
0.001.
was specifically designed for choice-based conjoint ana-
lyses. The sample size was determined using the John-
| son-Orme  | formula  (Johnson  | and  Orme  | 2010)  for  |     |     |     |     |     |     |     |
| --------- | ------------------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
4.2 Hypothesis testing results
| choice-based  | conjoint  analyses.  | While  | the  calculated  |     |     |     |     |     |     |     |
| ------------- | -------------------- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- |
minimum  sample  threshold  was  42  participants,  we  The analysis of the complete sample revealed no signifi-
selected a substantially larger sample size to enhance stat-
cant preferences across the four key attributes explain-
istical power. Participants were recruited from Germany
|     |     |     |     | ability,  reliability,  |     | AI  | certification  | and  | fairness  | (see  |
| --- | --- | --- | --- | ----------------------- | --- | --- | -------------- | ---- | --------- | ----- |
through the online panel Prolific between November 11-
Table 1). For the analyses including the whole sample,
12, 2024. German language proficiency was established as
all hypotheses need to be rejected.
an inclusion criterion since the survey was conducted in
German. Furthermore, participants were required to be
at least 18 years of age. The initial dataset comprised  4.3 Research question: most preferred attribute
323 participants. Following a thorough data cleaning pro-
combinations
cedure, which involved the exclusion of eight participants
The Choice-Based Conjoint Analysis of the total sample
due to incomplete responses, the final sample comprised
revealed a consistent preference pattern, with the most
| 315 participants (see Table 2 |     | for detailed sociodemo- |     |            |              |     |            |           |            |     |
| ----------------------------- | --- | ----------------------- | --- | ---------- | ------------ | --- | ---------- | --------- | ---------- | --- |
|                               |     |                         |     | preferred  | combination  |     | achieving  | a  50.8%  | selection  |     |
graphic characteristics). Participants were remunerated
for their participation through the Prolific platform. probability. The optimal combination consisted of no
explainability, medium reliability (65%), no AI certifi-
cation seal, and high fairness. The observed similarity
4 Results in  the  range  of  preference  probabilities  (50.3%  to
4.1 Overview of analysis approach
Based on the preregistered analysis plan, we employed a
Table 2. Sample size and description.
conventional conjoint approach. As this analysis did not  Total  Cluster
|     |     |     |     |     | sample. (n   |     |     |     |     | 2. (n =   |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --------- |
reveal user preferences for specific attributes, we con-
|     |     |     |     |     |     | = 315) | Cluster 1. (n = 182) |     |     | 133) |
| --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | ---- |
ducted additional, explorative cluster analyses in order
|     |     |     |     | Women | 158  |     | 86 (47.3%) |     |     | 67  |
| --- | --- | --- | --- | ----- | ---- | --- | ---------- | --- | --- | --- |
to test for the presence of heterogeneous preferences  (50.16%) (50.4%)
within  the  sample  population.  This  observation  Men 153  92 (50.5%) 66
|     |     |     |     |     | (48.57%) |     |     |     |     | (49.6%) |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------- |
prompted the implementation of an explorative analysis
|     |     |     |     | Diverse       | 3 (0.95%) |     | 3 (1.6%) |     |     | –   |
| --- | --- | --- | --- | ------------- | --------- | --- | -------- | --- | --- | --- |
|     |     |     |     | Not Specified | 1 (0.32%) |     | 1 (0.5%) |     |     | –   |
with a segmentation approach to identify and examine
|     |     |     |     | Age | 18–92 (M   |     | 18–92 (M = 32.5; SD = 10.4) |     |     | 18–92 (M   |
| --- | --- | --- | --- | --- | ---------- | --- | --------------------------- | --- | --- | ---------- |
potential heterogeneity in preferences. The analysis uti-
|     |     |     |     |     | = 32.6;  |     |     |     |     | = 32.9;  |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | -------- |
lised a two-stage methodology: initially, a latent class  SD =   SD =
analysis (LCA) employing a Gaussian mixture model  10.7) 10.1)
|     |     |     |     | University  | 183  |     | 103 (56.6%) |     |     | 80  |
| --- | --- | --- | --- | ----------- | ---- | --- | ----------- | --- | --- | --- |
with two components to identify distinct preference pat- Degree (58.1%) (60.2%)
|     |     |     |     | Highest School  | 71 (22.5%) |     | 44 (24.2%) |     |     | 27  |
| --- | --- | --- | --- | --------------- | ---------- | --- | ---------- | --- | --- | --- |
terns, followed by logistic regression for each identified
|           |                          |            |              | Degree      |            |     |            |     |     | (20.3%) |
| --------- | ------------------------ | ---------- | ------------ | ----------- | ---------- | --- | ---------- | --- | --- | ------- |
| cluster.  | The  analysis  examined  | four  key  | attributes:  |             |            |     |            |     |     |         |
|           |                          |            |              | University  | 61 (19.4%) |     | 35 (19.2%) |     |     | 17      |
|           |                          |            |              | Entrance    |            |     |            |     |     | (12.8%) |
explainability, reliability, AI certification seal, and fair-
Qualification
ness. For each segment, the approach generated prob-
|     |     |     |     | AI Acceptance | M = 7.27  |     | M = 7.18 (SD = 1.74) |     |     | M = 7.40  |
| --- | --- | --- | --- | ------------- | --------- | --- | -------------------- | --- | --- | --------- |
ability-based  preference  scores  across  attribute  (SD =   (SD =
|     |     |     |     |     | 1.75) |     |     |     |     | 1.75) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- |
combinations, allowing the identification of segment-  AI Fear M = 4.65  M = 4.79 (SD = 1.90) M = 4.46
specific preferred combinations while considering the  (SD =   (SD =
|     |     |     |     |     | 1.83) |     |     |     |     | 1.69) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- |
interaction effects between attributes.

BEHAVIOUR & INFORMATION TECHNOLOGY 847
50.8%) across the top combinations suggests the pres- 4.742, p < 0.001), thereby providing support for the
ence of relatively uniform preferences within the overall hypothesis. Conversely, Cluster 2 exhibited adverse pre-
sample. ferences for both attributes, with AI certification
demonstrating a more pronounced negative effect (β
= −0.240, z = −6.660, p < 0.001) compared to explain-
4.4 Explorative analysis
ability (β = −0.190, z = −5.285, p < 0.001).
4.4.1 Cluster analysis results The third hypothesis postulated that individuals
We employed Latent Class Analysis (LCA), a special would demonstrate stronger preference for communi-
type of finite mixture model for clustering with discrete cated trustworthiness (AI seal) over actual technical
variables, rather than k-means. LCA has been demon- trustworthiness (reliability and fairness). This hypoth-
strated to be advantageous for our Choice-Based Con- esis received partial support. Cluster 0 exhibited stron-
joint data, as it has been shown to directly model ger preferences for communicated trustworthiness
choice probabilities and to better handle categorical through AI certification (β = 0.193, p < 0.001) compared
attributes. In the context of model selection, a compara- to technical trustworthiness indicators. In contrast,
tive analysis was conducted between BIC and AIC Cluster 1 demonstrated stronger inclination toward
values across a range of 1–5 cluster solutions. The 2- technical trustworthiness indicators (fairness: β =
cluster solution was identified as optimal, exhibiting 0.409, p < 0.001; reliability: β = 0.137, p = 0.019) over
both significant improvement over a single cluster (χ² AI certification (β = −0.240, p < 0.001).
= 83.2, p < 0.001) and high entropy (0.82), indicative
of clear segment separation. The LCA identified two dis- 4.4.3 Research question: most preferred attribute
tinct participant clusters (n₁ = 133, n₂ = 182), each combinations for both clusters
demonstrating significantly different preferences for The results of the first cluster demonstrated a clear pre-
AI system attributes. The analysis revealed notable ference structure, with the most preferred combination
differences in both preference patterns (see Table 1) achieving a 62.4% selection probability. This optimal
and demographic characteristics between the identified combination comprised of no explainability, high
clusters, providing more actionable insights than the reliability (99%), no AI certificate, and limited fairness.
initial overall analysis. The results of the second cluster revealed different pre-
ferences, with the most preferred combination attain-
4.4.2 Hypothesis testing results for both clusters ing a 66.9% selection probability. This optimal
Separate logistic regression analyses were conducted for combination was characterised by its low explainabil-
each cluster to test our hypotheses, with choice as the ity, medium reliability (65%), low AI certificate, and
dependent variable and attribute levels as the indepen- high fairness.
dent variables. Statistical significance was assessed
using z-tests (p < 0.05). The model showed good fit 4.4.4 Demographic and attitudinal differences
with Pseudo R² values of 0.01027 (Cluster 1) and between clusters
0.01900 (Cluster 2), and highly significant likelihood Further statistical analysis revealed significant demo-
ratio tests (p < 0.001). graphic differences between the clusters. Statistical ana-
In the context of the study, hypothesis H1 postulated lyses were performed using independent samples t-tests
that individuals would prioritise reliability over fairness for continuous variables, while chi-square tests were
and explainability. However, the analysis revealed that employed for categorical variables. The t-tests revealed
this hypothesis is not supported in both clusters. Cluster significant differences between the clusters in AI accep-
1 exhibited no significant effect for reliability (β = tance (t = −6.453, p < .001) and AI fear (t = 9.701, p
−0.067, z = −1.344, p = 0.179) and a negative fairness < .001), as well as age (t = −2.147, p = . 032). Cluster 1
effect (β = −0.269, z = −5.409, p < 0.001). Cluster 2 reported higher AI acceptance and lower AI anxiety,
demonstrated significant effects for both reliability (β whereas cluster 2 reported lower AI acceptance and
= 0.137, z = 2.341, p = 0.019) and fairness (β = 0.409, z higher AI anxiety. While age differences were small,
= 6.980, p < 0.001), with fairness showing stronger Cluster 2 participants were slightly older than Cluster
influence. 1 participants. Detailed demographic characteristics
The second hypothesis, which posited that trust seals for both clusters can be found in Table 2. Educational
would be more effective than explanations, received backgrounds differed significantly between clusters (χ²
mixed support across clusters. Cluster 1 exhibited stron- = 86.289, p < .001). The distribution of educational qua-
ger preferences for AI certification (β = 0.193, z = 6.310, lifications varied notably, with Cluster 1 showing a
p < 0.001) compared to explainability (β = 0.145, z = higher proportion of university degrees, while Cluster

848 N. E. CETINKAYA AND N. KRÄMER
2 had a higher percentage of participants with highest relationship between system reliability and user prefer-
school degrees and university entrance qualifications. ence may be more nuanced and influenced by individual
Gender distribution also showed significant variation differences in AI attitudes.
between clusters (χ² = 111.259, p < .001). While Cluster
1 demonstrated an almost equal distribution between
5.1. Understanding versus trust: the role of
female and male participants, Cluster 2 showed a
explainability and certification
more diverse pattern, including small percentages of
participants identifying as other gender or preferring An analysis of the relationship between explainability
not to specify. Comprehensive descriptive statistics for and trust signals (H2) across the entire sample revealed
both clusters are presented in Table 2. no significant overall preferences, consistent with our
findings regarding other attributes. However, distinct
patterns emerged at the cluster level, indicating that
5 Discussion
while users lack universal preferences, individual groups
This study examined user preferences regarding key demonstrate clear inclinations towards or against both
attributes of AI systems, with a particular focus on the mechanisms.
relative importance of explainability, reliability, AI cer- The findings of the present study showed that prefer-
tification, and fairness in users’ decisions to engage with ences for transparency (i.e. explainability) and trust sig-
AI systems. The findings of the study revealed a more nals (i.e. AI certification seals) are interconnected. These
complex picture than initially hypothesised, with no results contradict the hypothesis (H2) that users would
attributes standing out when analysing the whole prioritise one over the other. Cluster 1 exhibited a pre-
sample. Cluster analyses, however, revealed that there ference for both explainability and certification, indicat-
are distinct user groups with opposite preferences. ing that these users seek diverse forms of external
These results offer significant implications for both the validation when evaluating AI systems. This finding is
theoretical understanding of AI system development consistent with theoretical frameworks suggesting that
and the practical applications of these systems. users may employ multiple trust-building mechanisms
when dealing with complex systems (Paaß and Hecker
2020).
5.1 Heterogeneous user preferences and trust
In contrast, Cluster 2 demonstrated negative prefer-
development
ences for both explainability and certification while
The lack of significant overall preferences across the favouring fairness and reliability. This pattern chal-
entire sample is notable, as it suggests that the prefer- lenges previous assumptions about users universally
ences of different user groups effectively balance each needing system understanding or validation. Whilst an
other out. However further analysis, employing cluster initial interpretation indicated that users might establish
analysis, revealed two distinct clusters of users with con- trust through alternative means, such as direct system
trasting preferences, challenging the assumption of uni- performance observation, a more nuanced interpret-
form user priorities in AI system adoption. Cluster 1 ation is required. It is crucial to acknowledge that the
demonstrated strong preferences for AI certification present study measured system choice as opposed to
and explainability while expressing negative preferences trust directly, as these are related yet distinct concepts.
for fairness. In contrast, Cluster 2 prioritised fairness This perspective aligns with the findings reported by
and reliability while showing negative preference (Kieslich, Keller, and Starke 2022) and (Bao et al.
towards choosing explainability and AI certification. 2022), which suggest that some users may exhibit
This group demonstrated higher AI acceptance and indifference towards specific ethical considerations of
lower AI fear scores, indicating a more confident AI systems, particularly transparency mechanisms. In
approach to AI interaction. contrast to actively seeking diverse trust pathways,
These findings contradict our first hypothesis that these users may prioritise performance-oriented attri-
users would universally prefer reliability over fairness butes with immediate practical impact (e.g. fairness
and explainability. Instead, we found that reliability’s and reliability), while demonstrating comparatively
importance varies significantly between user groups, less concern for the justification of system decisions or
with Cluster 2 showing moderate preference for for external validation. This finding extends the obser-
reliability while Cluster 1 showed no significant effect. vation made by Ferrario and Loi (Ferrario and Loi
This challenges previous findings by Kaplan et al. 2022) regarding the potential of increased system famili-
(2023) who identified reliability as the primary predictor arity to reduce reliance on conventional trust mechan-
of trust in AI systems. Our results suggest that the isms. The results suggest that user preferences for AI

BEHAVIOUR & INFORMATION TECHNOLOGY 849
system attributes are more intricate and diverse than challenges the assumption that adding more trust sig-
previously understood. nals universally enhances system trustworthiness,
The parallel preferences for or against both transpar- suggesting instead that targeted combinations might
ency and trust mechanisms across clusters suggest that be more effective for specific user groups.
these attributes may be more interconnected than pre-
viously theorised, potentially representing different
5.3. Preferred attribute combinations and their
aspects of a single underlying approach to AI system
implications
evaluation, potentially relying on external communi-
cation about the system. The Choice-Based Conjoint Analysis of the total sample
revealed a consistent preference pattern, with similar
selection probabilities (50.3% to 50.8%) across top com-
5.2. Technical versus communicated
binations. The combination that was selected most fre-
trustworthiness
quently, achieving a 50.8% selection probability,
Analysis of preferences between technical and commu- featured no explainability, medium reliability (65%),
nicated trustworthiness (H3) revealed no significant no AI certification seal, and high fairness. This relative
trends across the complete sample. However, distinct uniformity in preference probabilities suggests balanced
patterns emerged at the cluster level, demonstrating preferences within the overall sample. However, cluster
how different user groups approach trust development analysis revealed more nuanced patterns.
in contrasting ways. Our third hypothesis regarding Cluster 1’s optimal combination revealed an unex-
the preference for communicated trustworthiness over pected preference pattern: they favoured high reliability
technical trustworthiness revealed a more complex without explainability or fairness features. This finding
dynamic than anticipated. The analysis showed a clear suggests a minimalist approach that focuses solely on
division between clusters in how they evaluate and technical performance. This pattern might indicate that
prioritise different forms of trustworthiness. for some users, system complexity itself could be a source
Cluster 1’s stronger preference for AI certification of concern, leading them to prefer simpler, more straight-
aligns with Knowles and Richards’ (Knowles and forward implementations when given direct choice scen-
Richards 2021) argument about the importance of regu- arios. This interpretation aligns with Springer and
latory frameworks in building public trust. The fact that Whittaker’s (Springer and Whittaker 2020) observation
this group showed no significant preference for that some users actively avoid detailed system infor-
reliability, traditionally considered a cornerstone of mation, fearing that increased knowledge about data pro-
technical trustworthiness, further supports the cessing might discourage future use.
interpretation that they rely more heavily on external Cluster 2’s preferred combination presents an equally
validation than direct performance assessment. unexpected but different pattern: they opted for systems
In contrast, Cluster 2’s clear preference for technical with low explainability, moderate reliability (65%), low
trustworthiness indicators (fairness and reliability) over AI certification, but high fairness. This preference pattern
certification presents an unexpected pattern that chal- is particularly significant as it challenges multiple assump-
lenges conventional wisdom about trust development. tions about AI system design. Their strong emphasis on
This group appeared to reject communicated trustworthi- fairness while accepting lower levels of other attributes
ness in favour of direct performance indicators, supports Sullivan et al.’s (2022) findings about the growing
suggesting that some users might be more critical of exter- importance of ethical considerations in user trust develop-
nal validation mechanisms, preferring instead to evaluate ment. The willingness to accept moderate reliability when
systems based on their actual performance characteristics. paired with high fairness suggests that users might be
These contrasting preferences raise important ques- making sophisticated trade-offs between technical per-
tions about the conventional approach to AI system formance and ethical considerations.
deployment, which often emphasises standardised cer- This finding extends beyond simple feature prefer-
tification and documentation practices. Our results ences to suggest deeper differences in how users concep-
suggest that different user groups might require funda- tualise and evaluate AI trustworthiness. While system
mentally different approaches to establishing trust- designers often strive to maximise all positive attributes,
worthiness. This has significant implications for our our results indicate that different user groups might
research question about attribute combinations, as it have fundamentally different visions of what constitutes
indicates that the effectiveness of various trust-building an ideal AI system. This has significant implications for
features might depend heavily on users’ underlying AI system development, suggesting that optimising for
approach to technology evaluation. The finding all features simultaneously might actually make systems

850 N. E. CETINKAYA AND N. KRÄMER
less appealing to certain user groups who prefer more AI systems. Future studies should explicitly measure
focused or streamlined implementations. These patterns AI literacy to examine whether it mediates the relation-
also suggest an important refinement to theories about ship between system attributes and user trust. This
trust development in AI systems. Rather than treating could help explain why some users prioritise technical
trust as a cumulative product of positive features, our performance while others rely more heavily on external
findings indicate that users might employ different stra- validation. Future research could also explore how these
tegic approaches to system evaluation, with some pre- preference patterns manifest in different AI application
ferring focused, performance-oriented systems while contexts, and how they might be influenced by cultural
others seek more balanced implementations that prior- and organisational factors. The development of adaptive
itise ethical considerations over maximum technical trust-building mechanisms that can accommodate
performance. different user groups remains an important avenue for
investigation. Additionally, longitudinal studies exam-
ining how trust development patterns evolve with
5.4. Limitations and future research
increased AI exposure and literacy would provide valu-
Despite the fact that the methodological approach of able insights for system design and implementation.
presenting isolated attribute combinations may appear
to be abstracted from real-world AI interactions, this
6 Conclusion
design choice offers crucial advantages. As Orme
(Orme 2010) observes, conjoint analysis allows for the The present study examined the development of user trust
precise measurement of relative preferences for specific in AI systems, revealing four crucial insights. Firstly, the
AI system attributes by deliberately reducing complexity findings contradict the prevalent assumption that a uni-
and controlling for confounding variables. This form pattern exists; instead, we observed contrasting pre-
approach enables the observation of realistic decision- ferences among user groups that cancel each other out.
making processes through forced trade-offs. Whilst Secondly, the present study found that user preferences
the present controlled experimental setting may appear regarding understanding (explainability) and trust signals
to be detached from reality, it offers unique insights that (AI certification seal) are coupled. This finding challenges
would be difficult to obtain from studying complete AI the initial research question about whether users prefer
systems where multiple factors interact simultaneously. one approach over the other. Instead of a clear preference
Nevertheless, several limitations should be considered for one over the other, a distinct group of users exhibited a
when interpreting these results. First, our study focused desire for both mechanisms, suggesting a balanced
on a specific healthcare decision-making scenario, and approach to trust and transparency. Thirdly, distinct
findings may not generalise to other AI applications. user clusters with contrasting trust-building strategies
Second, while our sample was diverse in terms of age were identified: one group relies heavily on both external
and education, it was limited to German participants validation and transparency, exhibiting higher AI anxiety;
and may not be fully representative of all potential AI sys- in contrast, another prioritises externally communicated
tem users. A final limitation of the present study concerns reliability aspects and fairness metrics and shows greater
the abstract representation of system attributes. While AI acceptance. These results raise important questions
these standardised presentations are necessary for the iso- about the effectiveness of current transparency
lation of attribute effects, they may not fully capture real- approaches in reaching all user populations, and the
world user experiences with AI systems, potentially result- potential need for alternative strategies to engage users
ing in a limitation of ecological validity. It is recommended who demonstrate less interest in critically examining AI
that future studies build upon the present approach by systems beyond their direct performance outcomes. The
incorporating research that employs more concrete, inter- methodological approach employed in this study has
active representations of explainability features through exposed sophisticated tradeoffs in user preferences, par-
functional prototypes or simulations that better approxi- ticularly regarding the prioritisation of technical perform-
mate real-world AI interactions. ance over ethical considerations. Users comfortable with
A significant consideration for future research is the AI technology often accept moderate reliability when
role of AI literacy in shaping user preferences and trust paired with high fairness, while AI-anxious users place
development, building on recent work on digital literacy greater emphasis on transparency measures and certifi-
and AI adoption. The stark differences between our cation seals. The findings demonstrate that effective AI
identified clusters align with previous findings (Cox integration requires a shift from universal design prin-
2024) suggesting that varying levels of AI literacy sig- ciples to adaptive approaches that acknowledge combined
nificantly influence how users approach and evaluate preferences and adapt to diverse user groups.

|     |     |     |     |     |     |     |     | BEHAVIOUR & INFORMATION TECHNOLOGY  |     |     |     |     |     | 851 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Acknowledgements
|     |     |     |     |     |     |     | Computing,  |     | Iot  and  | Sdn:  | Reliability  | and  | Scalability  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ----- | ------------ | ---- | ------------ | --- |
Issues.” International Journal of Electrical and Computer
This  work  has  been  partly  supported  by  the  Engineering (IJECE) 11 (5): 4458–4470. https://doi.org/10.
Research Center Trustworthy Data Science and Security  11591/ijece.v11i5.pp4458-4470.
Bromme, Rainer, and Lukas Gierth. 2021. “Rationality and the
(https://rc-trust.ai/), one of the Research Alliance cen-
ters within the UA Ruhr (https://uaruhr.de). We sin- Public Understanding of Science.” In The Handbook of
|         |             |        |           |     |                |     | Rationality,  | edited  | by  | Markus  | Knauff  |     | and  Wolfgang  |     |
| ------- | ----------- | ------ | --------- | --- | -------------- | --- | ------------- | ------- | --- | ------- | ------- | --- | -------------- | --- |
| cerely  | appreciate  | their  | support.  |     | Additionally,  |     |               |         |     |         |         |     |                |     |
Spohn, 767–776. Cambridge, MA: MIT Press.
generative  AI  tools,  specifically  Claude  3.7  Sonnet,  Caspers, Julian. 2021. “Translation of Predictive Modeling
were used during the writing process to support the lin- and  AI  into  Clinics:  A  Question  of  Trust.”  European
guistic refinement and structural revision of texts orig- Radiology  31  (7):  4947–4948.  https://doi.org/10.1007/
inally  authored  by  the  researcher,  including  text  s00330-021-07977-9.
Chancey, Eric T., James P. Bliss, Yusuke Yamani, and Holly
| formulation,  | proofreading,  |     | and  | debugging  |     | of  code  |         |           |        |         |      |      |              |     |
| ------------- | -------------- | --- | ---- | ---------- | --- | --------- | ------- | --------- | ------ | ------- | ---- | ---- | ------------ | --- |
|               |                |     |      |            |     |           | A.  H.  | Handley.  | 2017.  | “Trust  | and  | the  | Compliance–  |     |
segments Reliance Paradigm: The Effects of Risk, Error Bias, and
Reliability on Trust and Dependence.” Human Factors:
The Journal of the Human Factors and Ergonomics Society
Author contributions
|     |     |     |     |     |     |     | 59  | (3):  | 333–345.  |     | https://doi.org/10.1177/  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ------------------------- | --- | --- | --- |
0018720816682648.
CRediT: Nur Efsan Cetinkaya: Conceptualization, Data cura-
|                |            |          |     |               |                 |     | Chen,  Melvin.  |     | 2021.  | “Trust  | and  | Trust-Engineering  |     | in  |
| -------------- | ---------- | -------- | --- | ------------- | --------------- | --- | --------------- | --- | ------ | ------- | ---- | ------------------ | --- | --- |
| tion,  Formal  | analysis,  | Funding  |     | acquisition,  | Investigation,  |     |                 |     |        |         |      |                    |     |     |
Methodology, Project administration, Resources, Software,  Artificial  Intelligence  Research:  Theory  and  Praxis.”
Philosophy & Technology 34 (4): 1429–1447. https://doi.
| Supervision,  | Validation,  | Visualization,  |     | Writing  |     | –  original  |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --------------- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
org/10.1007/s13347-021-00465-4.
| draft;  Nicole  | Krämer:  | Conceptualization,  |     |     | Funding  | acqui- |     |     |     |     |     |     |     |     |
| --------------- | -------- | ------------------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Cox, Andrew. 2024. “Algorithmic Literacy, AI Literacy and
| sition,  Methodology,  |     | Resources,  |     | Supervision,  |     | Writing  –  |              |             |     |     |             |          |     |      |
| ---------------------- | --- | ----------- | --- | ------------- | --- | ----------- | ------------ | ----------- | --- | --- | ----------- | -------- | --- | ---- |
|                        |     |             |     |               |     |             | Responsible  | Generative  |     | AI  | Literacy.”  | Journal  | of  | Web  |
review & editing.
|     |     |     |     |     |     |     | Librarianship  |     | 18  (3):  | 93–110.  | https://doi.org/10.1080/  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | -------- | ------------------------- | --- | --- | --- |
19322909.2024.2395341.
Disclosure statement Cremers, Armin B, Alex Englander, Markus Gabriel, Dirk
|     |     |     |     |     |     |     | Hecker,  | Michael  | Mock,  | Maximilian  |     | Poretschkin,  |     | Julia  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | ----------- | --- | ------------- | --- | ------ |
No potential conflict of interest was reported by the author(s).
|     |     |     |     |     |     |     | Rosenzweig,    | et                  | al.  2019.  | Trustworthy  |                    | Use  | of  Artificial  |      |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | ----------- | ------------ | ------------------ | ---- | --------------- | ---- |
|     |     |     |     |     |     |     | Intelligence:  |                     | Priorities  | from         | a  Philosophical,  |      | Ethical,        |      |
|     |     |     |     |     |     |     | Legal,         | and  Technological  |             | Viewpoint    |                    | as   | a  Basis        | for  |
Funding
Certification of Artificial Intelligence.
|     |     |     |     |     |     |     | Das,  Arun,  | and  | Paul  | Rad.  | 2020.  | “Opportunities  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | ----- | ------ | --------------- | --- | ---- |
This work was supported by Research Center Trustworthy
Challenges in Explainable Artificial Intelligence (XAI): A
Data Science and Security.
|     |     |     |     |     |     |     | Survey.”  | ArXiv.  | https://doi.org/10.48550/ARXIV.2006.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------------------------------- | --- | --- | --- | --- | --- |
11371.
De Brito Duarte, Regina, Filipa Correia, Patrícia Arriaga, and
References
Ana Paiva. 2023. “AI Trust: Can Explainable AI Enhance
Afroogh, Saleh, Ali Akbari, Emmie Malone, Mohammadali  Warranted  Trust?”  Human  Behavior  and  Emerging
| Kargar,                                                   | and  Hananeh  |     | Alambeigi.  | 2024.  | “Trust  | in  AI:  |               |     |             |                                |     |     |     |     |
| --------------------------------------------------------- | ------------- | --- | ----------- | ------ | ------- | -------- | ------------- | --- | ----------- | ------------------------------ | --- | --- | --- | --- |
|                                                           |               |     |             |        |         |          | Technologies  |     | 2023:1–12.  | https://doi.org/10.1155/2023/  |     |     |     |     |
| Progress, Challenges, and Future Directions.” Humanities  |               |     |             |        |         |          | 4637678.      |     |             |                                |     |     |     |     |
and Social Sciences Communications 11 (1): 1568. https://  DeVito, Michael A, Jeremy Birnholtz, Jeffery T. Hancock,
doi.org/10.1057/s41599-024-04044-8. Megan French, and Sunny Liu. 2018. How People Form
Angerschmid,  Alessa,  Jianlong  Zhou,  Kevin  Theuermann,  Folk Theories of Social Media Feeds and What It Means
Fang Chen, and Andreas Holzinger. 2022. “Fairness and
for How We Study Self-presentation. In Proceedings of
Explanation in AI-Informed Decision Making.” Machine  the  2018  CHI  Conference  on  Human  Factors  in
Learning  and  Knowledge  Extraction  4  (2):  556–579.  Computing Systems, April 19, 2018. ACM, Montreal QC
https://doi.org/10.3390/make4020026. Canada, 1–12. https://doi.org/10.1145/3173574.3173694
Bao, Luye, Nicole M. Krause, Mikhaila N. Calice, Dietram A.  Dorton,  Stephen  L.,  and  Samantha  B.  Harper.  2022.  “A
| Scheufele,  | Christopher  |     | D.  Wirz,  | Dominique  |     | Brossard,  |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Naturalistic Investigation of Trust, AI, and Intelligence
Todd P. Newman, and Michael A. Xenos. 2022. “Whose  Work.”  Journal  of  Cognitive  Engineering  and  Decision
AI? How Different Publics Think about AI and Its Social  Making  16  (4):  222–236.  https://doi.org/10.1177/
| Impacts.”  | Computers  | in  | Human  | Behavior  |     | 130:107182.  | 15553434221103718. |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------ | --------- | --- | ------------ | ------------------ | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1016/j.chb.2022.107182. Ebeling, Charles E. 2019. An Introduction to Reliability and
Bartneck, Christoph, Christoph Lütge, Alan Wagner, and
Maintainability Engineering. Long Grove, IL: Waveland
| Sean Welsh. 2021. “Trust and Fairness in AI Systems.” In  |     |     |     |     |     |     | Press. |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
An  Introduction  to  Ethics  in  Robotics  and  AI,  27–38.  Ferrario, Andrea, and Michele Loi. 2022. “How Explainability
Cham: Springer International Publishing.. https://doi.org/  Contributes to Trust in AI.” In 2022 ACM Conference on
10.1007/978-3-030-51110-4_4 Fairness,  Accountability,  and  Transparency,  June  20,
Belgaum, M., Z. Alansari, S. Musa, M. Mansoor Alam, and M.
2022. ACM, Seoul Republic of Korea, 1457–1466. https://
Mazliham. 2021. “Role of Artificial Intelligence in Cloud  doi.org/10.1145/3531146.3533202

852 N. E. CETINKAYA AND N. KRÄMER
Geng, Xiuli, and Xuening Chu. 2012. “A new Importance– INTERACT 2021, edited by Carmelo Ardito, Rosa
Performance Analysis Approach for Customer Lanzilotti, Alessio Malizia, Helen Petrie, Antonio
Satisfaction Evaluation Supporting PSS Design.” Expert Piccinno, Giuseppe Desolda, and Kori Inkpen, 383–404.
Systems with Applications 39 (1): 1492–1502. https://doi. Cham: Springer International Publishing. https://doi.org/
org/10.1016/j.eswa.2011.08.038. 10.1007/978-3-030-85610-6_23
Gunning, David, Mark Stefik, Jaesik Choi, Timothy Miller, Langer, Markus, Daniel Oster, Timo Speith, Holger
Simone Stumpf, and Guang-Zhong Yang. 2019. “XAI— Hermanns, Lena Kästner, Eva Schmidt, Andreas Sesing,
Explainable Artificial Intelligence.” Science Robotics 4 (37): and Kevin Baum. 2021. “What Do We Want from
eaay7120. https://doi.org/10.1126/scirobotics.aay7120. Explainable Artificial Intelligence (XAI)? – a Stakeholder
Hendriks, Friederike, Dorothe Kienhues, and Rainer Bromme. Perspective on XAI and a Conceptual Model Guiding
2015. “Measuring Laypeople’s Trust in Experts in a Digital Interdisciplinary XAI Research.” Artificial Intelligence
Age: The Muenster Epistemic Trustworthiness Inventory 296:103473. https://doi.org/10.1016/j.artint.2021.103473.
(METI).” PLoS One 10 (10): e0139309. https://doi.org/10. LaRose, Robert, and Nora Rifon. 2006. “Your Privacy Is
1371/journal.pone.0139309. Assured - of Being Disturbed: Websites with and without
Hong, Yili, Jiayi Lian, Li Xu, Jie Min, Yueyao Wang, Laura J. Privacy Seals.” New Media & Society 8 (6): 1009–1029.
Freeman, and Xinwei Deng. 2022. “Statistical Perspectives https://doi.org/10.1177/1461444806069652.
on Reliability of Artificial Intelligence Systems.” Quality Lee, J. D., and K. A. See. 2004. “Trust in Automation:
Engineering 35 (1): 56–78. https://doi.org/10.1080/ Designing for Appropriate Reliance.” Human Factors:
08982112.2022.2089854. The Journal of the Human Factors and Ergonomics Society
Jacovi, Alon, Ana Marasović, Tim Miller, and Yoav Goldberg. 46 (1): 50–80. https://doi.org/10.1518/hfes.46.1.50_30392.
2021. Formalizing Trust in Artificial Intelligence: Madhavan, P., and D. A. Wiegmann. 2007. “Similarities and
Prerequisites, Causes and Goals of Human Trust in AI. Differences between Human–Human and Human–
In Proceedings of the 2021 ACM Conference on Fairness, Automation Trust: An Integrative Review.” Theoretical
Accountability, and Transparency (FAccT ‘21, March 03, Issues in Ergonomics Science 8 (4): 277–301. https://doi.
2021. ACM, New York, NY, USA, 624–635. https://doi. org/10.1080/14639220500337708.
org/10.1145/3442188.3445923 Marassi, Lidia. 2023. Assessing User Perceptions of Bias in
Jain, Lakshitha R, and Vineetha Menon. 2023. AI Algorithmic Generative AI Models: Promoting Social Awareness for
Bias: Understanding Its Causes, Ethical and Social Trustworthy AI. In Proceedings of the 2023 Conference
Implications. In 2023 IEEE 35th International Conference on Human Centered Artificial Intelligence: Education and
on Tools with Artificial Intelligence (ICTAI), November Practice, December 14, 2023. ACM, Dublin Ireland, 46–
06, 2023. IEEE, Atlanta, GA, USA, 460–467. https://doi. 46. https://doi.org/10.1145/3633083.3633094
org/10.1109/ICTAI59109.2023.00073 Markus, Aniek F., Jan A. Kors, and Peter R. Rijnbeek. 2021.
Johnson, Richard M, and Bryan K Orme. 2010. “Sample Size “The Role of Explainability in Creating Trustworthy
Issues for Conjoint Analysis.” In Getting Started with Artificial Intelligence for Health Care: A Comprehensive
Conjoint Analysis: Strategies for Product Design and Survey of the Terminology, Design Choices, and
Pricing Research, edited by Bryan K Orme, 57–66. Evaluation Strategies.” Journal of Biomedical Informatics
Madison: Research Publishers. 113:103655. https://doi.org/10.1016/j.jbi.2020.103655.
Kaplan, Alexandra D., Theresa T. Kessler, J. Christopher Brill, Mayer, Roger C., James H. Davis, and F. David Schoorman.
and P. A. Hancock. 2023. “Trust in Artificial Intelligence: 1995. “An Integrative Model of Organizational Trust.”
Meta-analytic Findings.” Human Factors: The Journal of The Academy of Management Review 20 (3): 709–734.
the Human Factors and Ergonomics Society 65 (2): 337– https://doi.org/10.2307/258792.
359. https://doi.org/10.1177/00187208211013988. Mehrotra, Siddharth, Chadha Degachi, Oleksandra
Kieslich, Kimon, Birte Keller, and Christopher Starke. 2022. Vereschak, Catholijn M. Jonker, and Myrthe L. Tielman.
“AI-Ethics by Design. Evaluating Public Perception on 2024. “A Systematic Review on Fostering Appropriate
the Importance of Ethical Design Principles of AI.” Big Trust in Human-AI Interaction: Trends, Opportunities
Data & Society 9 (1): 205395172210929. https://doi.org/ and Challenges.” ACM Journal on Responsible Computing
10.1177/20539517221092956. 1: 26. https://doi.org/10.1145/3696449.
Knowles, Bran, and John T. Richards. 2021. “The Sanction of Mishra, Saurabh, Anand Rao, Ramayya Krishnan, Bilal
Authority: Promoting Public Trust in AI.” In Proceedings Ayyub, Amin Aria, and Enrico Zio. 2024. “Reliability,
of the 2021 ACM Conference on Fairness, Accountability, Resilience and Human Factors Engineering for
and Transparency (FAccT ‘21), 2021. ACM, New York, Trustworthy AI Systems.” arXiv preprint. https://doi.org/
NY, USA, 262–271. https://doi.org/10.1145/3442188. 10.48550/arXiv.2411.08981.
3445890 Ngo, Thao, and Nicole Krämer. 2021. “Exploring Folk Theories
Krämer, Nicole, Magdalena Wischnewski, and Emmanuel of Algorithmic News Curation for Explainable Design.”
Müller. 2023. “Interacting with Autonomous Systems and Behaviour & Information Technology 41 (15): 3346–3359.
Intelligent Algorithms – new Theoretical Considerations https://doi.org/10.1080/0144929X.2021.1987522.
on the Relation of Understanding and Trust.” https://doi. Ngo, Thao, Johannes Kunkel, and Jürgen Ziegler. 2020.
org/10.31234/osf.io/h32ze. “Exploring Mental Models for Transparent and
Kunkel, Johannes, Thao Ngo, Jürgen Ziegler, and Nicole Controllable Recommender Systems: A Qualitative
Krämer. 2021. “Identifying Group-Specific Mental Models Study.” Proceedings of the 28th ACM Conference on User
of Recommender Systems: A Novel Quantitative Modeling, Adaptation and Personalization, July 07, 2020.
Approach.” In Human-Computer Interaction –

BEHAVIOUR & INFORMATION TECHNOLOGY 853
ACM, Genoa Italy, 183–191. https://doi.org/10.1145/ Schlicker, Nadine and Markus Langer. 2021. “Towards
3340631.3394841 Warranted Trust: A Model on the Relation Between
Norkute, Milda, Nadja Herger, Leszek Michalak, Andrew Actual and Perceived System Trustworthiness.” In
Mulder, and Sally Gao. 2021. Towards Explainable AI: Proceedings of Mensch und Computer 2021 (MuC ‘21),
Assessing the Usefulness and Impact of Added 2021. ACM, Ingolstadt Germany, 325–329. https://doi.
Explainability Features in Legal Document org/10.1145/3473856.3474018
Summarization. In Extended Abstracts of the 2021 CHI Sheth, Amit, Manas Gaur, Kaushik Roy, and Keyur
Conference on Human Factors in Computing Systems, Faldu. 2021. “Knowledge-Intensive Language
May 08, 2021. ACM, Yokohama Japan, 1–7. https://doi. Understanding for Explainable AI.” IEEE Internet
org/10.1145/3411763.3443441 Computing 25 (5): 19–24. https://doi.org/10.1109/MIC.
Nourani, Mahsan, Samia Kabir, Sina Mohseni, and Eric D. 2021.3101919.
Ragan. 2019. “The Effects of Meaningful and Meaningless Shin, Donghee. 2021. “The Effects of Explainability and
Explanations on Trust and Perceived System Accuracy in Causability on Perception, Trust, and Acceptance:
Intelligent Systems.” Proceedings of the AAAI Conference Implications for Explainable AI.” International Journal of
on Human Computation and Crowdsourcing 7:97–105. Human-Computer Studies 146:102551. https://doi.org/10.
https://doi.org/10.1609/hcomp.v7i1.5284. 1016/j.ijhcs.2020.102551.
Obermeyer, Ziad, Brian Powers, Christine Vogeli, and Sendhil Shin, Donghee, and Yong Jin Park. 2019. “Role of Fairness,
Mullainathan. 2019. “Dissecting Racial Bias in an Accountability, and Transparency in Algorithmic
Algorithm Used to Manage the Health of Populations.” Affordance.” Computers in Human Behavior 98:277–284.
Science 366 (6464): 447–453. https://doi.org/10.1126/ https://doi.org/10.1016/j.chb.2019.04.019.
science.aax2342. Sindermann, Cornelia, Peng Sha, Min Zhou, Jennifer
Orme, Bryan K. 2010. Getting Started with Conjoint Analysis: Wernicke, Helena S. Schmitt, Mei Li, Rayna Sariyska,
Strategies for Product Design and Pricing Research. Maria Stavrou, Benjamin Becker, and Christian Montag.
Madison: Research Publisher LCC. 2021. “Assessing the Attitude towards Artificial
Paaß, Gerhard and Dirk Hecker. 2020. KI und ihre Chancen, Intelligence: Introduction of a Short Measure in German,
Herausforderungen und Risiken. In Künstliche Intelligenz. Chinese, and English Language.” KI - Künstliche
Wiesbaden: Springer Vieweg, 375–444. https://doi.org/10. Intelligenz 35 (1): 109–118. doi:10.1007/s13218-020-
1007/978-3-658-30211-5_10. 00689-0
Peña, Alejandro, Ignacio Serna, Aythami Morales, and Julian Sperber, Dan, Fabrice Clément, Christophe Heintz, Olivier
Fierrez. 2020. “FairCVtest Demo: Understanding Bias in Mascaro, Hugo Mercier, Gloria Origgi, and Deirdre
Multimodal Learning with a Testbed in Fair Automatic Wilson. 2010. “Epistemic Vigilance.” KI - Künstliche
Recruitment.” In Proceedings of the 2020 International Intelligenz 25 (4): 359–393. https://doi.org/10.1007/
Conference on Multimodal Interaction, October 21, 2020. s13218-020-00689-0
ACM, Virtual Event Netherlands, 760–761. https://doi. Springer, Aaron, and Steve Whittaker. 2020. “Progressive
org/10.1145/3382507.3421165 Disclosure: When, Why, and How Do Users Want
Pierce, Robin L, Wim Van Biesen, Daan Van Cauwenberge, Algorithmic Transparency Information?” ACM
Johan Decruyenaere, and Sigrid Sterckx. 2022. Transactions on Interactive Intelligent Systems 10 (4): 1–
Explainability in medicine in an era of AI-based clinical 32. https://doi.org/10.1145/3374218.
decision support systems. Frontiers in Genetics. 13: Sullivan, Yulia, Marc De Bourmont, and Mary Dunaway.
903600. https://doi.org/10.3389/fgene.2022.903600. 2022. “Appraisals of Harms and Injustice Trigger an
Poursabzi-Sangdeh, Forough, Daniel G Goldstein, Jake M Eerie Feeling That Decreases Trust in Artificial
Hofman, Jennifer Wortman Wortman Vaughan, and Intelligence Systems.” Annals of Operations Research 308
Hanna Wallach. 2021. Manipulating and Measuring (1-2): 525–548. https://doi.org/10.1007/s10479-020-03702-
Model Interpretability. In Proceedings of the 2021 CHI 9.
Conference on Human Factors in Computing Systems Varona, Daniel, and Juan Luis Suárez. 2022. “Discrimination,
(CHI ‘21), 2021. ACM, New York, NY, USA, 1–52. Bias, Fairness, and Trustworthy AI.” Applied Sciences
https://doi.org/10.1145/3411764.3445315 12:5826. https://doi.org/10.3390/app12125826.
Ryan, Mark. 2020. “In AI We Trust: Ethics, Artificial Wang, Ning, David V. Pynadath, and Susan G. Hill. 2015.
Intelligence, and Reliability.” Science and Engineering “Building Trust in a Human-Robot Team with
Ethics 26 (5): 2749–2767. https://doi.org/10.1007/s11948- Automatically Generated Explanations.” In Proceedings of
020-00228-y. the interservice/industry training, simulation and education
Saeed, Waddah, and Christian Omlin. 2023. “Explainable AI conference (I/ITSEC) 15315: 1–12.
(XAI): A Systematic Meta-survey of Current Challenges Weitz, Katharina, Dominik Schiller, Ruben Schlagowski,
and Future Opportunities.” Knowledge-Based Systems Tobias Huber, and Elisabeth André. 2019. “Do you trust
263:110273. https://doi.org/10.1016/j.knosys.2023.110273. me?": Increasing User-Trust by Integrating Virtual Agents
Scharowski, Nicolas, Michaela Benk, Swen J. Kühne, Léane in Explainable AI Interaction Design.” In Proceedings of
Wettstein, and Florian Brühlmann. 2023. “Certification the 19th ACM International Conference on Intelligent
Labels for Trustworthy AI: Insights From an Empirical Virtual Agents (IVA ’19), 7–9. New York, NY, USA:
Mixed-Method Study.” In Proceedings of the 2023 ACM Association for Computing Machinery. https://doi.org/10.
Conference on Fairness, Accountability, and 1145/3308532.3329441.
Transparency (FAccT ‘23), 2023. ACM, Chicago IL USA, Wing, Jeannette M. 2021. Trustworthy AI. Commun. ACM 64,
248–260. https://doi.org/10.1145/3593013.3593994 10 (October 2021), 64–71. https://doi.org/10.1145/3448248

854 N. E. CETINKAYA AND N. KRÄMER
Wischnewski, Magdalena, Nicole Krämer, and Emmanuel Explainable AI, Andreas Holzinger, Randy Goebel, Ruth
Müller. 2023. Measuring and Understanding Trust Fong, Taesup Moon, Klaus-Robert Müller and Wojciech
Calibrations for Automated Systems: A Survey of the Samek. Springer International Publishing, Cham, 375–
State-Of-The-Art and Future Directions. In Proceedings 386. https://doi.org/10.1007/978-3-031-04083-2_18
of the 2023 CHI Conference on Human Factors in Zhou, Jianlong, Sunny Verma, Mudit Mittal, and Fang Chen.
Computing Systems (CHI ‘23), 2023. Association for 2021. Understanding Relations Between Perception of
Computing Machinery, New York, NY, USA, 1–16. Fairness and Trust in Algorithmic Decision Making. In
https://doi.org/10.1145/3544548.3581197 8th International Conference on Behavioral and Social
Zhou, Jianlong, Fang Chen, and Andreas Holzinger. 2022. Computing (BESC), October 29, 2021. IEEE, Doha,
Towards Explainability for AI Fairness. In xxAI - beyond Qatar, 1–5